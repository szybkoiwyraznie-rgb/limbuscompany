# Grzesznik #12: Gregor — Tożsamości, umiejętności, pasywki i głos (część a) — Limbus Company

Kompletny zestaw kart Tożsamości postaci **Gregor** (그레고르) wraz z umiejętnościami na ulepszeniach 1–4, efektami monet, pasywkami i kwestiami głosowymi.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Grzesznik #12: Gregor (그레고르)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 그레고르
   źródło: Characters.json :: dataList[id=12].name
   limit: do 40 znaków
   EN: Gregor
   PL:
2. [Akta więźnia — nazwa] 그레고르
   źródło: IntroduceCharacter.json :: dataList[id=그레고르].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
3. [Akta więźnia — opis] 본 수감자는 다른 수감자에 비해 인격적인 면에선 다루기가 무난한 편입니다.\n하지만 감정 고조나 환경의 갑작스러운 변화에 따라서 신체의 일부,\n간혹 가다가는 전부가 벌레(갑각 충의 일부, ■■■■와 유사함)의 조직으로\n변합니다. 무례한 관리자가 되고 싶지 않다면(그럴 필요는 물론 없지만)\n역겨움을 드러내지 않도록 표정 관리는 철저히 하는 것을 권장합니다.\n냉소적인 어조를 일부 사용하지만 요령만 안다면 원만한 의사소통이\n가능한 수감자이므로 크게 어려움을 요하진 않습니다.
   źródło: IntroduceCharacter.json :: dataList[id=그레고르].description
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This Sinner is relatively easy to handle in terms of personality.\nHowever, an upsurge of emotion or a sudden change of environment\nmay cause parts or the whole of his body to transform into insectile\n(notably akin to a carapace, resembling that of the _________) tissues.\nIf you do not wish to be a rude manager (not that you're obligated to be nice),\nwe recommend keeping your facial expression in check so that your disgust is not visible to him.\nHe sometimes uses cynical language, but he can still be reasoned with,\nand you can get around him without much difficulty as long as you learn the knack of it.
   PL: Ten Grzesznik pod względem charakteru jest łatwiejszy w obyciu od pozostałych.\nJednak pod wpływem silnych emocji albo nagłej zmiany otoczenia część jego ciała,\na niekiedy całe, zmienia się w tkankę owada (fragmenty pancerza, podobne do ■■■■).\nJeśli nie chce pan być nieuprzejmym Kierownikiem (choć oczywiście nie musi pan),\nzalecamy pilnować wyrazu twarzy, by nie okazać obrzydzenia.\nBywa cyniczny, ale gdy pozna się sposób, można się z nim swobodnie porozumieć,\nnie sprawia więc większych trudności.

## [0] LCB Sinner — Gregor — LCB 수감자
- ID Tożsamości: `11201` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 72 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Rupture

4. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=11201].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL:
5. [Karta Tożsamości — nazwa] 그레고르
   źródło: Personalities.json :: dataList[id=11201].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — nazwa z tytułem] 그레고르
   źródło: Personalities.json :: dataList[id=11201].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Karta Tożsamości — opis] 그레고르의 첫번째 인격
   źródło: Personalities.json :: dataList[id=11201].desc
   limit: do 120 znaków
   EN: Gregor’s 1st Identity
   PL:
8. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 베기
   źródło: Skills.json :: dataList[id=1120101].levelList[level=1].name ; dataList[id=1120101].levelList[level=2].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Swipe
   PL:
9. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1120101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL:
10. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 4 부여
   źródło: Skills.json :: dataList[id=1120101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 4 Rupture
   PL:
11. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 후비기
   źródło: Skills.json :: dataList[id=1120102].levelList[level=1].name ; dataList[id=1120102].levelList[level=2].name ; dataList[id=1120102].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 5 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Jag
   PL:
12. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 횟수 1 증가
   źródło: Skills.json :: dataList[id=1120102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Rupture Count
   PL:
13. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 1 증가
   źródło: Skills.json :: dataList[id=1120102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1120102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Rupture Count
   PL:
14. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 관통 취약 1 부여
   źródło: Skills.json :: dataList[id=1120102].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1120102].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Pierce Fragility
   PL:
15. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1120102].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
16. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 썰어내기
   źródło: Skills.json :: dataList[id=1120103].levelList[level=3].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 6 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Chop Up
   PL:
17. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Burst]이 있을 때 피해량 +10%
   źródło: Skills.json :: dataList[id=1120103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has [Burst], +10% Damage
   PL:
18. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Burst]이 있을 때 피해량 +10%
   źródło: Skills.json :: dataList[id=1120103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
19. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 피해량의 30%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1120103].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal by 30% of damage dealt
   PL:
20. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1120104].levelList[level=1].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+3)
   limit: do 40 znaków
   EN: Guard
   PL:
21. [Pasywka bojowa (od ulepszenia 1, posiadane 3× Gloom) — nazwa] 강제생존
   źródło: Passives.json :: dataList[id=1120101].name
   limit: do 40 znaków
   EN: Forced Survival
   PL:
22. [Pasywka bojowa (od ulepszenia 1, posiadane 3× Gloom) — opis] 전투 시작 자신의 체력 5 회복
   źródło: Passives.json :: dataList[id=1120101].desc
   limit: do 120 znaków
   EN: Heal 5 HP at the start of the combat phase.
   PL:
23. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Gloom) — nazwa] 인자 코드 G-0
   źródło: Passives.json :: dataList[id=1120121].name
   limit: do 40 znaków
   EN: Gene Code G-0
   PL:
24. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Gloom) — opis] 현재 체력이 가장 낮은 아군 1명 전투 시작 시 체력 5 회복
   źródło: Passives.json :: dataList[id=1120121].desc
   limit: do 120 znaków
   EN: At the start of the combat phase, the ally with the least HP heals 5 HP.
   PL:
25. [Kwestia głosowa [get_11201_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=get_11201_1].desc
   limit: do 120 znaków
   EN: Identity Acquisition
   PL:
26. [Kwestia głosowa [get_11201_1] (Identity Acquisition)] 음… 그레고르다. 뭐, 자고 있을 때 빼고는 편하게 부르라고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=get_11201_1].dlg
   limit: do 120 znaków
   EN: Mm… It’s Gregor. Well, feel free to talk to me unless I’m asleep.
   PL:
27. [Kwestia głosowa [lobby_morning_11201_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=lobby_morning_11201_1].desc
   limit: do 120 znaków
   EN: Morning Greeting
   PL:
28. [Kwestia głosowa [lobby_morning_11201_1] (Morning Greeting)] 적당히 나쁘지 않은 아침이지?
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=lobby_morning_11201_1].dlg
   limit: do 120 znaków
   EN: Not a bad morning, is it?
   PL:
29. [Kwestia głosowa [lobby_noon_11201_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=lobby_noon_11201_1].desc
   limit: do 120 znaków
   EN: Afternoon Greeting
   PL:
30. [Kwestia głosowa [lobby_noon_11201_1] (Afternoon Greeting)] 자자, 아무리 바빠도 점심은 먹고 일해야지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=lobby_noon_11201_1].dlg
   limit: do 120 znaków
   EN: C’mon, I know you’re busy, but you gotta eat sometime.
   PL:
31. [Kwestia głosowa [lobby_night_11201_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=lobby_night_11201_1].desc
   limit: do 120 znaków
   EN: Evening Greeting
   PL:
32. [Kwestia głosowa [lobby_night_11201_1] (Evening Greeting)] 오늘 하루도 고생 많았어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=lobby_night_11201_1].dlg
   limit: do 120 znaków
   EN: Another busy day, wasn’t it. Good work out there.
   PL:
33. [Kwestia głosowa [smalltalk_11201_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=smalltalk_11201_1].desc
   limit: do 120 znaków
   EN: Chatter #1
   PL:
34. [Kwestia głosowa [smalltalk_11201_1] (Chatter #1)] 우리 관리자 양반은 평소에는 뭐하면서 지내나? 담배… 라도 권해주고 싶은데, 그러지도 못하겠군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=smalltalk_11201_1].dlg
   limit: do 160 znaków
   EN: So, what do you usually do in your free time, Manager Bud? I’d lend you a cig… but I guess it won’t be useful for you.
   PL:
35. [Kwestia głosowa [smalltalk_11201_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=smalltalk_11201_2].desc
   limit: do 120 znaków
   EN: Chatter #2
   PL:
36. [Kwestia głosowa [smalltalk_11201_2] (Chatter #2)] 내가 제일 싫어하는 거? 저 더듬이가 유별나게 기다랗고 까만 등 껍질을 단 그것들. 특히나 물에 빠져도 둥둥 떠다니고 있는 게 보일 정도로 악착같이 살아남는 그 끈질긴 게 싫어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=smalltalk_11201_2].dlg
   limit: do 210 znaków
   EN: My least favorite things? Those dark-shelled critters with a long pair of antennae. I especially hate the tenacity of those bugs, refusing to die even in water.
   PL:
37. [Kwestia głosowa [smalltalk_11201_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=smalltalk_11201_3].desc
   limit: do 120 znaków
   EN: Chatter #3
   PL:
38. [Kwestia głosowa [smalltalk_11201_3] (Chatter #3)] 관리자 양반, 혹시 안경 닦이 있… 아니다, 괜한 소리를 물었네. 안경 낄 일 없는 걸 다행으로 알라고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=smalltalk_11201_3].dlg
   limit: do 160 znaków
   EN: Hey, Manager Bud, you got some lens cleaner…? Nevermind, forget I asked. Just be glad if you don’t have to wear glasses.
   PL:
39. [Kwestia głosowa [smalltalk_11201_4] — sytuacja] 대화 4
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=smalltalk_11201_4].desc
   limit: do 120 znaków
   EN: Chatter #4
   PL:
40. [Kwestia głosowa [smalltalk_11201_4] (Chatter #4)] 기억을 잃었다는 양반한테 이런 이야기 하는 것도 거슥하지만… \n어떤 기억은 통째로 도려내도 아깝지 않을 것 같다는 생각이 가끔 들어. 무슨 말인지 알겠어? 마치 오지 않는 종전의 날을 기다리는 기분이지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=smalltalk_11201_4].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I know it’s not the most flattering thing to say to a pal suffering from amnesia…\nBut, I sometimes think there are a few memories I could do without. You get what I’m saying? It’s like waiting for the end of a war that’ll never come.
   PL:
41. [Kwestia głosowa [smalltalk_11201_5] — sytuacja] 대화 5
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=smalltalk_11201_5].desc
   limit: do 120 znaków
   EN: Chatter #5
   PL:
42. [Kwestia głosowa [smalltalk_11201_5] (Chatter #5)] 자르고 잘라내도 계속 생겨나더라고. 이 팔 말이야. 아, 다리라고 해야 되나… \n지금은 가족 같은 사이가 되었지. 싫으나 좋으나 함께하기를 받아들여야 했다는 뜻이야.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=smalltalk_11201_5].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This thing would keep on regrowing every time I tried to cut it off. My arm, I mean. Or should I call it a leg…\nIt’s basically like family now. Well, that’s to say I had to accept that I’m stuck with it, like it or hate it.
   PL:
43. [Kwestia głosowa [neglect_11201_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=neglect_11201_1].desc
   limit: do 120 znaków
   EN: Idle
   PL:
44. [Kwestia głosowa [neglect_11201_1] (Idle)] 음? 관리자 양반? 그새 어디 갔어?
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=neglect_11201_1].dlg
   limit: do 120 znaków
   EN: Hm? Manager Bud? Where’d you scuttle off to?
   PL:
45. [Kwestia głosowa [formation_11201_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=formation_11201_1].desc
   limit: do 120 znaków
   EN: Deployment
   PL:
46. [Kwestia głosowa [formation_11201_1] (Deployment)] 어, 최선은 다해볼게.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=formation_11201_1].dlg
   limit: do 120 znaków
   EN: Aight, I’ll do what I can.
   PL:
47. [Kwestia głosowa [battleentry_11201_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battleentry_11201_1].desc
   limit: do 120 znaków
   EN: Stage Entry
   PL:
48. [Kwestia głosowa [battleentry_11201_1] (Stage Entry)] 가라고? 나…? 하… 뭐, 최선은 다해보겠다만.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battleentry_11201_1].dlg
   limit: do 120 znaków
   EN: Go? You want me to…? Gah… Well, I guess I’ll give it my all.
   PL:
49. [Kwestia głosowa [battle_select_11201_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_select_11201_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle
   PL:
50. [Kwestia głosowa [battle_select_11201_1] (Viewed in Battle)] 뭐야, 나한테 볼일이야?
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_select_11201_1].dlg
   limit: do 120 znaków
   EN: What’s up? You got something to say?
   PL:
51. [Kwestia głosowa [battle_endcommand_11201_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_endcommand_11201_1].desc
   limit: do 120 znaków
   EN: Commencing Attack
   PL:
52. [Kwestia głosowa [battle_endcommand_11201_1] (Commencing Attack)] 좋아, 간다!
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_endcommand_11201_1].dlg
   limit: do 120 znaków
   EN: Alright, here I go!
   PL:
53. [Kwestia głosowa [battle_enemy_break_11201_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_enemy_break_11201_1].desc
   limit: do 120 znaków
   EN: Enemy Stagger
   PL:
54. [Kwestia głosowa [battle_enemy_break_11201_1] (Enemy Stagger)] 어이쿠, 생각보다 잘 들어갔네.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_enemy_break_11201_1].dlg
   limit: do 120 znaków
   EN: Whoa, that was a pretty clean hit.
   PL:
55. [Kwestia głosowa [battle_break_11201_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_break_11201_1].desc
   limit: do 120 znaków
   EN: Staggered
   PL:
56. [Kwestia głosowa [battle_break_11201_1] (Staggered)] 이런…
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_break_11201_1].dlg
   limit: do 120 znaków
   EN: Ah, shoot…
   PL:
57. [Kwestia głosowa [battle_kill_11201_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_kill_11201_1].desc
   limit: do 120 znaków
   EN: Enemy Killed
   PL:
58. [Kwestia głosowa [battle_kill_11201_1] (Enemy Killed)] 손쉽구만.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_kill_11201_1].dlg
   limit: do 120 znaków
   EN: That was a breeze.
   PL:
59. [Kwestia głosowa [battle_allydead_11201_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_allydead_11201_1].desc
   limit: do 120 znaków
   EN: Ally Death
   PL:
60. [Kwestia głosowa [battle_allydead_11201_1] (Ally Death)] 그… 관리자 양반. 시계 좀 돌려야겠는데?
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_allydead_11201_1].dlg
   limit: do 120 znaków
   EN: Oh boy… Guess you’ve got work to do, eh, Manager Bud?
   PL:
61. [Kwestia głosowa [choice_success_p_11201_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=choice_success_p_11201_1].desc
   limit: do 120 znaków
   EN: Check Passed
   PL:
62. [Kwestia głosowa [choice_success_p_11201_1] (Check Passed)] 관리자 양반! 이번 건 꽤 잘한 것 같지?
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=choice_success_p_11201_1].dlg
   limit: do 120 znaków
   EN: Check this out, Manager Bud! Did a pretty neat job, right?
   PL:
63. [Kwestia głosowa [choice_fail_n_11201_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=choice_fail_n_11201_1].desc
   limit: do 120 znaków
   EN: Check Failed
   PL:
64. [Kwestia głosowa [choice_fail_n_11201_1] (Check Failed)] 나는 말한 거 같은데… 이게 최선이였어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=choice_fail_n_11201_1].dlg
   limit: do 120 znaków
   EN: I’m pretty sure I did tell you… This was the best I could do.
   PL:
65. [Kwestia głosowa [battle_clear_11201_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_clear_11201_1].desc
   limit: do 120 znaków
   EN: Victory Cry
   PL:
66. [Kwestia głosowa [battle_clear_11201_1] (Victory Cry)] 하~ 어찌어찌 이겼네. 수고 많았어, 관리자 양반.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_clear_11201_1].dlg
   limit: do 120 znaków
   EN: Phew~ We beat ‘em somehow. Nice work, Manager Bud.
   PL:
67. [Kwestia głosowa [battle_clear_ex_11201_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_clear_ex_11201_1].desc
   limit: do 120 znaków
   EN: Extra Conditions Fulfilled
   PL:
68. [Kwestia głosowa [battle_clear_ex_11201_1] (Extra Conditions Fulfilled)] 훈장은 사양이야. 뭐, 담배라면 사양치 않겠지만.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_clear_ex_11201_1].dlg
   limit: do 120 znaków
   EN: Won’t take any medals. Cigarettes, on the other hand, are completely welcome.
   PL:
69. [Kwestia głosowa [battle_defeat_11201_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_defeat_11201_1].desc
   limit: do 120 znaków
   EN: Defeat Wail
   PL:
70. [Kwestia głosowa [battle_defeat_11201_1] (Defeat Wail)] 미안하군. 오늘따라 집중이 잘 안되었던 것 같아. 그런 날도 있는 거 아니겠어?
   źródło: PersonalityVoiceDlg/Voice_Gregor_LCB_11201.json :: dataList[id=battle_defeat_11201_1].dlg
   limit: do 120 znaków
   EN: Sorry ‘bout that. Couldn’t really keep my head in the game. Just one of those days, I guess.
   PL:

## [00] Liu Assoc. South Section 6 — Gregor — 남부 리우 협회 6과
- ID Tożsamości: `11202` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 63 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Burn

71. [Karta Tożsamości — tytuł] 남부 리우 협회\n6과
   źródło: Personalities.json :: dataList[id=11202].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Liu Assoc.\nSouth Section 6
   PL:
72. [Karta Tożsamości — nazwa] 그레고르
   źródło: Personalities.json :: dataList[id=11202].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [Karta Tożsamości — nazwa z tytułem] 그레고르
   źródło: Personalities.json :: dataList[id=11202].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Karta Tożsamości — opis] 그레고르의 두번째 인격
   źródło: Personalities.json :: dataList[id=11202].desc
   limit: do 120 znaków
   EN: Gregor’s 2nd Identity
   PL:
75. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 일점 찌르기
   źródło: Skills.json :: dataList[id=1120201].levelList[level=1].name ; dataList[id=1120201].levelList[level=2].name ; dataList[id=1120201].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Single-point Stab
   PL:
76. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Burn
   PL:
77. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1120201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Burn
   PL:
79. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1120201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Combustion]이 6 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1120201].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Coin Power +1
   PL:
81. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120201].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 몰아치기
   źródło: Skills.json :: dataList[id=1120202].levelList[level=1].name ; dataList[id=1120202].levelList[level=2].name ; dataList[id=1120202].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 5 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Rush Down
   PL:
84. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 화상 3 부여
   źródło: Skills.json :: dataList[id=1120202].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1120202].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1120202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Burn
   PL:
85. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120202].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills.json :: dataList[id=1120202].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1120202].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], gain 1 Attack Power Up next turn
   PL:
88. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Combustion]이 6 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1120202].levelList[level=4].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 연무 장타
   źródło: Skills.json :: dataList[id=1120203].levelList[level=3].name ; dataList[id=1120203].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Perfected Palm Strike
   PL:
92. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120203].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120203].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 화상 3 부여
   źródło: Skills.json :: dataList[id=1120203].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1120203].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Combustion]이 6 이상이면, 피해량 +10%
   źródło: Skills.json :: dataList[id=1120203].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], deal +10% damage
   PL:
97. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1120203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1120204].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+5)
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — nazwa] 발화
   źródło: Passives.json :: dataList[id=1120201].name
   limit: do 40 znaków
   EN: Ignition
   PL:
102. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — opis] 스킬의 3번째 코인부터 적중 시 화상 1 부여
   źródło: Passives.json :: dataList[id=1120201].desc
   limit: do 120 znaków
   EN: The 3rd and subsequent Coins of a skill inflict 1 Burn on hit.
   PL:
103. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Sloth) — nazwa] 내달리는 마음
   źródło: Passives.json :: dataList[id=1120221].name
   limit: do 40 znaków
   EN: Rushing Heart
   PL:
104. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Sloth) — opis] 속도가 가장 낮은 아군 1명 3번째 코인 이후부터 피해량 +30%
   źródło: Passives.json :: dataList[id=1120221].desc
   limit: do 120 znaków
   EN: 1 ally with the slowest Speed deals +30% damage with their 4th and subsequent Coins.
   PL:
105. [Kwestia głosowa [get_11202_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=get_11202_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Kwestia głosowa [get_11202_1] (Identity Acquisition)] 관리자 양반, 불꽃놀이 좋아하나?
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=get_11202_1].dlg
   limit: do 120 znaków
   EN: Say, Manager Bud, you like fireworks?
   PL:
107. [Kwestia głosowa [lobby_morning_11202_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=lobby_morning_11202_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Kwestia głosowa [lobby_morning_11202_1] (Morning Greeting)] 오늘따라 해가 밝네. 불은 충분하겠어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=lobby_morning_11202_1].dlg
   limit: do 120 znaków
   EN: Sun’s bright today. Oughta be more than enough light.
   PL:
109. [Kwestia głosowa [lobby_noon_11202_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=lobby_noon_11202_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
110. [Kwestia głosowa [lobby_noon_11202_1] (Afternoon Greeting)] 왜 그렇게 급하게들 나가나 했더니, 벌써 점심시간이었군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=lobby_noon_11202_1].dlg
   limit: do 120 znaków
   EN: No wonder everyone was in a rush, it’s lunchtime.
   PL:
111. [Kwestia głosowa [lobby_night_11202_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=lobby_night_11202_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [Kwestia głosowa [lobby_night_11202_1] (Evening Greeting)] 나 참, 다들 뭐가 그렇게 바쁜지. 적어도 담배 태울 시간은 줘야 되지 않겠어?
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=lobby_night_11202_1].dlg
   limit: do 140 znaków
   EN: Good grief, why do they have to keep everyone so late? Don’t I deserve some downtime to smoke, at least?
   PL:
113. [Kwestia głosowa [smalltalk_11202_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=smalltalk_11202_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Kwestia głosowa [smalltalk_11202_1] (Chatter #1)] 왜 그래? 심심한 거면 나랑 여기서 노가리나 잠깐 까다가 가도 되고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=smalltalk_11202_1].dlg
   limit: do 120 znaków
   EN: What’s up? If you’re bored, feel free to hang with me for a bit.
   PL:
115. [Kwestia głosowa [smalltalk_11202_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=smalltalk_11202_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Kwestia głosowa [smalltalk_11202_2] (Chatter #2)] 이것 봐, 관리자 양반. 불 필요할 때마다 라이터가 필요 없다니까. 지난번에 료슈 씨 불이 떨어졌길래 붙여주려고 했더니만, 예술적이지 못하다면서 화를 내더라고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=smalltalk_11202_2].dlg
   limit: do 250 znaków
   EN: Check this out, Manager Bud. Thanks to this here, I don’t need to carry a lighter around. Tried giving Ryōshū a light the other day, but she got all snappy, calling it “inartistic” or whatever.
   PL:
117. [Kwestia głosowa [smalltalk_11202_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=smalltalk_11202_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Kwestia głosowa [smalltalk_11202_3] (Chatter #3)] 뫼르소 말이야? 영… 답답한 친구긴 한데, 남들이 볼 땐 우리 둘이 시너지가 잘 맞는다 하더라고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=smalltalk_11202_3].dlg
   limit: do 120 znaków
   EN: ‘Bout Meursault? He’s, eh… kinda like a brick wall, but others say we make a good team.
   PL:
119. [Kwestia głosowa [smalltalk_11202_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=smalltalk_11202_4].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 1
   PL:
120. [Kwestia głosowa [smalltalk_11202_4] (Post-Uptie Chat 1)] 의수가 불편하지 않냐고? 전혀. 오히려 감각이 없다는 게 얼마나 격투에 도움이 되는지 몰라. 아픔을 모르는 이상 내 팔은 무적이지. 그것뿐이야.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=smalltalk_11202_4].dlg
   limit: do 250 znaków
   EN: “Isn’t this prosthetic arm uncomfortable?” Nah, not at all. You have no idea how much the lack of feeling helps me in fights. As long as it knows no pain, my arm’s invincible. That’s all I care.
   PL:
121. [Kwestia głosowa [smalltalk_11202_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=smalltalk_11202_5].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 2
   PL:
122. [Kwestia głosowa [smalltalk_11202_5] (Post-Uptie Chat 2)] 난 최전선이 싫어. 가능만 하다면 뒤에서 느긋하게, 불꽃이나 설렁설렁 날리면서 싸우고 싶어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=smalltalk_11202_5].dlg
   limit: do 150 znaków
   EN: I hate the frontline. If I can, I wanna stay at the back and chill, just flinging some flames every so often.
   PL:
123. [Kwestia głosowa [neglect_11202_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=neglect_11202_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Kwestia głosowa [neglect_11202_1] (Idle)] 어디 갔어, 관리자 양반? 그럼 나도 이 타이밍에 담배나…
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=neglect_11202_1].dlg
   limit: do 120 znaków
   EN: Where’d you go, Manager Bud? Welp, guess I’ll take a smoke break…
   PL:
125. [Kwestia głosowa [gacksung_11202_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=gacksung_11202_1].desc
   limit: do 120 znaków
   EN: Uptying
   PL:
126. [Kwestia głosowa [gacksung_11202_1] (Uptying)] 에이, 이런 거 필요 없다니까. 더 잘해야만 할 것 같잖아.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=gacksung_11202_1].dlg
   limit: do 120 znaków
   EN: C’mon, I don’t need all this. You’re pressuring me into working harder.
   PL:
127. [Kwestia głosowa [formation_11202_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=formation_11202_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Kwestia głosowa [formation_11202_1] (Deployment)] 그래, 태워보지 뭐.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=formation_11202_1].dlg
   limit: do 120 znaków
   EN: Sure, let’s burn some stuff.
   PL:
129. [Kwestia głosowa [battleentry_11202_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battleentry_11202_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Kwestia głosowa [battleentry_11202_1] (Stage Entry)] 몸이 따라줄지는 모르겠지만… 가라면 가야지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battleentry_11202_1].dlg
   limit: do 120 znaków
   EN: Not sure my body will work with me… but orders are orders.
   PL:
131. [Kwestia głosowa [battle_select_11202_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_select_11202_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Kwestia głosowa [battle_select_11202_1] (Viewed in Battle)] 어쩐 일이야, 관리자 양반?
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_select_11202_1].dlg
   limit: do 120 znaków
   EN: What is it, Manager Bud?
   PL:
133. [Kwestia głosowa [battle_endcommand_11202_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_endcommand_11202_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Kwestia głosowa [battle_endcommand_11202_1] (Commencing Attack)] 이대로 가보자고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_endcommand_11202_1].dlg
   limit: do 120 znaków
   EN: Let’s get right into it.
   PL:
135. [Kwestia głosowa [battle_break_11202_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_break_11202_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Kwestia głosowa [battle_break_11202_1] (Staggered)] 윽!
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_break_11202_1].dlg
   limit: do 120 znaków
   EN: Ugh!
   PL:
137. [Kwestia głosowa [battle_enemy_break_11202_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_enemy_break_11202_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Kwestia głosowa [battle_enemy_break_11202_1] (Enemy Stagger)] 생각보다 잘 타는걸?
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_enemy_break_11202_1].dlg
   limit: do 120 znaków
   EN: Pretty flammable, aren’t ya?
   PL:
139. [Kwestia głosowa [battle_kill_11202_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_kill_11202_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Kwestia głosowa [battle_kill_11202_1] (Enemy Killed)] 다음.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_kill_11202_1].dlg
   limit: do 120 znaków
   EN: Next.
   PL:
141. [Kwestia głosowa [battle_allydead_11202_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_allydead_11202_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [Kwestia głosowa [battle_allydead_11202_1] (Ally Death)] 조심하라고 했잖아…
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_allydead_11202_1].dlg
   limit: do 120 znaków
   EN: Told you to watch it…
   PL:
143. [Kwestia głosowa [choice_success_p_11202_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=choice_success_p_11202_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Kwestia głosowa [choice_success_p_11202_1] (Check Passed)] 생각보다 좋은 선택이였어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=choice_success_p_11202_1].dlg
   limit: do 120 znaków
   EN: A better choice than I expected.
   PL:
145. [Kwestia głosowa [choice_fail_n_11202_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=choice_fail_n_11202_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Kwestia głosowa [choice_fail_n_11202_1] (Check Failed)] 불은 어떻게 다루냐에 따라 결과가 달라지지…
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=choice_fail_n_11202_1].dlg
   limit: do 120 znaków
   EN: Fire can leave dire consequences if you aren’t careful with it…
   PL:
147. [Kwestia głosowa [battle_clear_11202_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_clear_11202_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Kwestia głosowa [battle_clear_11202_1] (Victory Cry)] 그… 마지막에 내 펀치, 멋있지 않았나?
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_clear_11202_1].dlg
   limit: do 120 znaków
   EN: Well… That punch I threw at the end was pretty cool, wasn’t it?
   PL:
149. [Kwestia głosowa [battle_clear_ex_11202_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_clear_ex_11202_1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Kwestia głosowa [battle_clear_ex_11202_1] (Extra Conditions Fulfilled)] 아, 너무 열심히 했어. 이걸로 일주일은 울궈먹을 수 있겠군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_clear_ex_11202_1].dlg
   limit: do 120 znaków
   EN: Man, I strained myself. That’s a week’s worth of excuses I could use.
   PL:
151. [Kwestia głosowa [battle_defeat_11202_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_defeat_11202_1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Kwestia głosowa [battle_defeat_11202_1] (Defeat Wail)] 오늘따라 불이 안 붙네…
   źródło: PersonalityVoiceDlg/Voice_Gregor_LiuAsso6_11202.json :: dataList[id=battle_defeat_11202_1].dlg
   limit: do 120 znaków
   EN: Ignition’s not working well today…
   PL:

## [000] G Corp. Manager Corporal — Gregor — G사 일등대리
- ID Tożsamości: `11203` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 1 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Rupture

153. [Karta Tożsamości — tytuł] G사\n일등대리
   źródło: Personalities.json :: dataList[id=11203].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: G Corp.\nManager Corporal
   PL:
154. [Karta Tożsamości — nazwa] 그레고르
   źródło: Personalities.json :: dataList[id=11203].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Karta Tożsamości — nazwa z tytułem] 그레고르
   źródło: Personalities.json :: dataList[id=11203].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Karta Tożsamości — opis] 그레고르의 세번째 인격
   źródło: Personalities.json :: dataList[id=11203].desc
   limit: do 120 znaków
   EN: Gregor’s 3rd Identity
   PL:
157. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 베어내기
   źródło: Skills.json :: dataList[id=1120301].levelList[level=1].name ; dataList[id=1120301].levelList[level=2].name ; dataList[id=1120301].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Hack
   PL:
158. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WinDuel] 피해량 +20%
   źródło: Skills.json :: dataList[id=1120301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] +20% damage
   PL:
159. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 피해량의 30%만큼 체력 회복.
   źródło: Skills.json :: dataList[id=1120301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal by 30% of damage dealt
   PL:
160. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WinDuel] 피해량 +40%
   źródło: Skills.json :: dataList[id=1120301].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] +40% damage
   PL:
161. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 피해량의 50%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1120301].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal by 50% of damage dealt
   PL:
162. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WinDuel] 피해량 +40%\n대상의 [Burst]이 5 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1120301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Burst]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture
   EN: [WinDuel] Damage +40%\nIf target has 5+ [Burst], Coin Power +1
   PL:
163. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1120301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal by 50% of damage dealt
   PL:
164. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 사지절단
   źródło: Skills.json :: dataList[id=1120302].levelList[level=1].name ; dataList[id=1120302].levelList[level=2].name ; dataList[id=1120302].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 6 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Dismember
   PL:
165. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills.json :: dataList[id=1120302].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1120302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1120302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Rupture
   PL:
166. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 피해량의 50%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1120302].levelList[level=2].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Burst]이 5 이상이면, 피해량 +50%
   źródło: Skills.json :: dataList[id=1120302].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 5+ [Burst], deal +50% damage
   PL:
168. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 50%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1120302].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 내장파기
   źródło: Skills.json :: dataList[id=1120303].levelList[level=3].name ; dataList[id=1120303].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Eviscerate
   PL:
170. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Burst]이 있을 때 피해량의 30%만큼 추가 피해
   źródło: Skills.json :: dataList[id=1120303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1120303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has [Burst], deal 30% of damage dealt as bonus damage
   PL:
171. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Burst]이 있을 때 피해량의 30%만큼 추가 피해
   źródło: Skills.json :: dataList[id=1120303].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1120303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 170 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Burst]이 있을 때 피해량의 30%만큼 추가 피해
   źródło: Skills.json :: dataList[id=1120303].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1120303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 170 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttackHead] 피해량의 100%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1120303].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal 100% of damage dealt
   PL:
174. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Burst]이 5 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1120303].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 5+ [Burst], Coin Power +1
   PL:
175. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 피해량의 100%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1120303].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal by 100% of damage dealt
   PL:
176. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1120304].levelList[level=1].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — nazwa] 긴급 식량보급
   źródło: Passives.json :: dataList[id=1120301].name
   limit: do 40 znaków
   EN: Emergency Rations
   PL:
178. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — opis] 체력이 25% 미만이면 합 승리 시 5%만큼 체력 회복
   źródło: Passives.json :: dataList[id=1120301].desc
   limit: do 120 znaków
   EN: At less than 25% HP, heal by 5% of Max HP after winning a clash.
   PL:
179. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 인자 코드 G-3
   źródło: Passives.json :: dataList[id=1120321].name
   limit: do 40 znaków
   EN: Gene Code G-3
   PL:
180. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 현재 체력이 가장 낮은 아군 1명 합 승리시 체력 5 회복
   źródło: Passives.json :: dataList[id=1120321].desc
   limit: do 120 znaków
   EN: The ally with the least HP heals 5 HP after winning a clash.
   PL:
181. [Kwestia głosowa [get_11203_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=get_11203_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Kwestia głosowa [get_11203_1] (Identity Acquisition)] 신고합니다! 입사를 명 받은 그레고르라고 합니다. 작전에 함께 투입되어서 영광입니다!
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=get_11203_1].dlg
   limit: do 120 znaków
   EN: Employee Gregor, reporting for duty! It’s an honor to join your mission, Manager!
   PL:
183. [Kwestia głosowa [lobby_morning_11203_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=lobby_morning_11203_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Kwestia głosowa [lobby_morning_11203_1] (Morning Greeting)] 충성! 아침 점호 간 이상 없었습니다!
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=lobby_morning_11203_1].dlg
   limit: do 120 znaków
   EN: Good morning, Manager! Morning roll call was all clear!
   PL:
185. [Kwestia głosowa [lobby_noon_11203_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=lobby_noon_11203_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Kwestia głosowa [lobby_noon_11203_1] (Afternoon Greeting)] 점심시간이군요! 오후 일과도 최선을 다하겠습니다!
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=lobby_noon_11203_1].dlg
   limit: do 120 znaków
   EN: It’s lunch hours, Manager! I’ll perform the remaining tasks with due diligence!
   PL:
187. [Kwestia głosowa [lobby_night_11203_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=lobby_night_11203_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Kwestia głosowa [lobby_night_11203_1] (Evening Greeting)] 근무 중 이상 없습니다. 충성!
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=lobby_night_11203_1].dlg
   limit: do 120 znaków
   EN: Nothing to report, Manager Dante!
   PL:
189. [Kwestia głosowa [smalltalk_11203_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=smalltalk_11203_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Kwestia głosowa [smalltalk_11203_1] (Chatter #1)] 관리자님! 아직 적응 중입니다만… 다들 잘 챙겨주셔서 문제없이 지내고 있습니다. 가끔 로쟈님이 징그럽다곤 하지만… 하하, 괜찮습니다.
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=smalltalk_11203_1].dlg
   limit: do 220 znaków
   EN: Manager! I’m still adjusting to life here… but thanks to everyone’s assistance, I am without trouble. Ms. Rodya often has unsavory comments, but… Haha, it’s alright.
   PL:
191. [Kwestia głosowa [smalltalk_11203_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=smalltalk_11203_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Kwestia głosowa [smalltalk_11203_2] (Chatter #2)] 망설이지 않고 싸우겠습니다. 신체 개조를 받는 기회를 운 좋게 얻었을 때부터, 다짐해왔습니다.
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=smalltalk_11203_2].dlg
   limit: do 180 znaków
   EN: I’ll fight my enemies without hesitation. I’d made up my mind the day I was honored with an opportunity to get the modification procedure.
   PL:
193. [Kwestia głosowa [smalltalk_11203_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=smalltalk_11203_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Kwestia głosowa [smalltalk_11203_3] (Chatter #3)] 아, 이 팔이요? 전 자랑스럽게 생각하고 있습니다. 무력하게 전쟁을 바라보는 것보단… 전장 한복판에 뛰어 들어갈 수 있다는 건 큰 행운이거든요.
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=smalltalk_11203_3].dlg
   limit: do 180 znaków
   EN: Oh, this arm? I’m proud of it. It’s a tremendous boon to be able to enter the fray of battle… rather than helplessly watch from afar.
   PL:
195. [Kwestia głosowa [smalltalk_11203_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=smalltalk_11203_4].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Kwestia głosowa [smalltalk_11203_4] (Post-Uptie Chat 1)] 신체 개조는… 후회하지 않습니다. 하지만… 전 평생 민간인의 삶으로 돌아갈 수는 없을 겁니다.
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=smalltalk_11203_4].dlg
   limit: do 150 znaków
   EN: The augmentation… I don’t regret it. One downside, though… is that I won’t ever be able to return to civilian life.
   PL:
197. [Kwestia głosowa [smalltalk_11203_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=smalltalk_11203_5].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Kwestia głosowa [smalltalk_11203_5] (Post-Uptie Chat 2)] 요새는… 최대한 아무 생각도 안 하려고 노력하고 있습니다. 그래야 버틸 수 있는 기분이거든요.
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=smalltalk_11203_5].dlg
   limit: do 140 znaków
   EN: Nowadays… I try not to think much about what I do. It’s getting too taxing to keep up with this otherwise.
   PL:
199. [Kwestia głosowa [neglect_11203_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=neglect_11203_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Kwestia głosowa [neglect_11203_1] (Idle)] 관리자님? 잠시 자리를 비우셨군요. 대기하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=neglect_11203_1].dlg
   limit: do 120 znaków
   EN: Manager? I see you’ve taken a temporary leave. I’ll be on standby.
   PL:
201. [Kwestia głosowa [gacksung_11203_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=gacksung_11203_1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Kwestia głosowa [gacksung_11203_1] (Uptying)] 충성! 앞으로도 최선을 다해서 보필하겠습니다, 관리자님!
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=gacksung_11203_1].dlg
   limit: do 120 znaków
   EN: Salutations! I’ll continue to aid you to the best of my ability, Manager!
   PL:
203. [Kwestia głosowa [formation_11203_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=formation_11203_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Kwestia głosowa [formation_11203_1] (Deployment)] 영광입니다!
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=formation_11203_1].dlg
   limit: do 120 znaków
   EN: It’s an honor, Manager!
   PL:
205. [Kwestia głosowa [battleentry_11203_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battleentry_11203_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Kwestia głosowa [battleentry_11203_1] (Stage Entry)] 최선을 다해 임하겠습니다!
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battleentry_11203_1].dlg
   limit: do 120 znaków
   EN: I will do my utmost!
   PL:
207. [Kwestia głosowa [battle_select_11203_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_select_11203_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Kwestia głosowa [battle_select_11203_1] (Viewed in Battle)] 일등대리 그레고르!
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_select_11203_1].dlg
   limit: do 120 znaków
   EN: Manager Corporal Gregor reporting!
   PL:
209. [Kwestia głosowa [battle_endcommand_11203_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_endcommand_11203_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Kwestia głosowa [battle_endcommand_11203_1] (Commencing Attack)] 명령대로!
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_endcommand_11203_1].dlg
   limit: do 120 znaków
   EN: Roger that!
   PL:
211. [Kwestia głosowa [battle_enemy_break_11203_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_enemy_break_11203_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Kwestia głosowa [battle_enemy_break_11203_1] (Enemy Stagger)] 제대로 들어갔습니다!
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_enemy_break_11203_1].dlg
   limit: do 120 znaków
   EN: I got a clean hit!
   PL:
213. [Kwestia głosowa [battle_break_11203_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_break_11203_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Kwestia głosowa [battle_break_11203_1] (Staggered)] 윽…
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_break_11203_1].dlg
   limit: do 120 znaków
   EN: Ngh…
   PL:
215. [Kwestia głosowa [battle_kill_11203_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_kill_11203_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Kwestia głosowa [battle_kill_11203_1] (Enemy Killed)] 처리했습니다!
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_kill_11203_1].dlg
   limit: do 120 znaków
   EN: I took one down!
   PL:
217. [Kwestia głosowa [battle_allydead_11203_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_allydead_11203_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Kwestia głosowa [battle_allydead_11203_1] (Ally Death)] 제가 더 노력해보겠습니다…
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_allydead_11203_1].dlg
   limit: do 120 znaków
   EN: I’ll work harder to make up for it…
   PL:
219. [Kwestia głosowa [choice_success_p_11203_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=choice_success_p_11203_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Kwestia głosowa [choice_success_p_11203_1] (Check Passed)] 관리자님! 멋진 전략이었습니다!
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=choice_success_p_11203_1].dlg
   limit: do 120 znaków
   EN: Splendid strategy, Manager!
   PL:
221. [Kwestia głosowa [choice_fail_n_11203_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=choice_fail_n_11203_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Kwestia głosowa [choice_fail_n_11203_1] (Check Failed)] 믿어주셨는데… 실패했습니다.
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=choice_fail_n_11203_1].dlg
   limit: do 120 znaków
   EN: You trusted me with it… and yet I failed.
   PL:
223. [Kwestia głosowa [battle_clear_11203_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_clear_11203_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [Kwestia głosowa [battle_clear_11203_1] (Victory Cry)] 덕분입니다, 관리자님. 좋은 전술이었습니다.
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_clear_11203_1].dlg
   limit: do 120 znaków
   EN: It’s all thanks to you, Manager. Your tactical prowess shined.
   PL:
225. [Kwestia głosowa [battle_clear_ex_11203_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_clear_ex_11203_1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Kwestia głosowa [battle_clear_ex_11203_1] (Extra Conditions Fulfilled)] 관리자님 덕분에 승리를 거둘 수 있었습니다.
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_clear_ex_11203_1].dlg
   limit: do 120 znaków
   EN: This victory was all thanks to you, Executive Manager.
   PL:
227. [Kwestia głosowa [battle_defeat_11203_1] — sytuacja] 전투 패배 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_defeat_11203_1].desc
   limit: do 120 znaków
   EN: Defeat Wail
   PL:
228. [Kwestia głosowa [battle_defeat_11203_1] (Defeat Wail)] 전쟁이란… 이런 것이군요. 전 자격 미달이었습니다.
   źródło: PersonalityVoiceDlg/Voice_Gregor_GCorp_11203.json :: dataList[id=battle_defeat_11203_1].dlg
   limit: do 120 znaków
   EN: This… is what a war is. I was wholly unqualified.
   PL:

## [00] R.B. Sous-chef — Gregor — 료. 고. 파. 조수
- ID Tożsamości: `11204` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 1 · HP bazowe: 76 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Bleed

229. [Karta Tożsamości — tytuł] 료. 고. 파.\n조수
   źródło: Personalities.json :: dataList[id=11204].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: R.B.\nSous-chef
   PL:
230. [Karta Tożsamości — nazwa] 그레고르
   źródło: Personalities.json :: dataList[id=11204].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Karta Tożsamości — nazwa z tytułem] 그레고르
   źródło: Personalities.json :: dataList[id=11204].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Karta Tożsamości — opis] 그레고르의 네번째 인격
   źródło: Personalities.json :: dataList[id=11204].desc
   limit: do 120 znaków
   EN: Gregor’s 4th Identity
   PL:
233. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 신선도 유지
   źródło: Skills.json :: dataList[id=1120401].levelList[level=1].name ; dataList[id=1120401].levelList[level=2].name ; dataList[id=1120401].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 4 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Keep It Fresh
   PL:
234. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마비 1 부여
   źródło: Skills.json :: dataList[id=1120401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Paralyze
   PL:
235. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1120401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL:
236. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마비 1 부여. 대상에게 [Laceration]이 있으면 다음 턴에 마비 1 부여
   źródło: Skills.json :: dataList[id=1120401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1120401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 Paralyze; if target has [Laceration], inflict 1 Paralyze next turn
   PL:
237. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1120401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1120401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL:
238. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Binding]이 4 이상이면, 피해량 +30%
   źródło: Skills.json :: dataList[id=1120401].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: If target has 4+ [Binding], deal +30% damage
   PL:
239. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 싱싱한 재료인가?
   źródło: Skills.json :: dataList[id=1120402].levelList[level=1].name ; dataList[id=1120402].levelList[level=2].name ; dataList[id=1120402].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 6 · monety: 1 (+8)
   limit: do 40 znaków
   EN: You Fresh Enough?
   PL:
240. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가, 다음 턴에 속박 1 부여
   źródło: Skills.json :: dataList[id=1120402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Bleed Count; Inflict 1 Bind next turn
   PL:
241. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 2 증가, 다음 턴에 속박 2 부여
   źródło: Skills.json :: dataList[id=1120402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1120402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Bleed Count; Inflict 2 Bind next turn
   PL:
242. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상보다 속도가 3 이상 빠르면, 코인 위력 +3
   źródło: Skills.json :: dataList[id=1120402].levelList[level=4].desc
   limit: do 120 znaków
   EN: If user's Speed is faster than target's by 3+, Coin Power +3
   PL:
243. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 재료 해체
   źródło: Skills.json :: dataList[id=1120403].levelList[level=3].name ; dataList[id=1120403].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 4 (+1)
   limit: do 40 znaków
   EN: Butcher Viand
   PL:
244. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1120403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1120403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 마비 1 부여
   źródło: Skills.json :: dataList[id=1120403].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1120403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Paralyze
   PL:
246. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 마비 1 부여
   źródło: Skills.json :: dataList[id=1120403].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1120403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]에 비례하여 체력 회복 (최대 20%)
   źródło: Skills.json :: dataList[id=1120403].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1120403].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Heal HP based on target’s [Laceration] (Max 20%)
   PL:
248. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 출혈 횟수가 10 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1120403].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target has 10+ Bleed Count, Coin Power +1
   PL:
249. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1120404].levelList[level=1].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — nazwa] 파이 포장
   źródło: Passives.json :: dataList[id=1120401].name
   limit: do 40 znaków
   EN: Packed Pies
   PL:
251. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — opis] 전투 시작 시 자신의 체력 8 회복
   źródło: Passives.json :: dataList[id=1120401].desc
   limit: do 120 znaków
   EN: Heal 8 HP at the start of the combat phase.
   PL:
252. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — nazwa] 조리 보조
   źródło: Passives.json :: dataList[id=1120421].name
   limit: do 40 znaków
   EN: Culinary Aid
   PL:
253. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — opis] 체력이 가장 낮은 아군 1명이 전투 시작 시 체력 5 회복\n료.고.파. 주방장 료슈 - 즉흥 조리 패시브의 체력 회복량 +5
   źródło: Passives.json :: dataList[id=1120421].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the combat phase, the ally with the least HP heals 5 HP.\nBoost the healing of R.B. Chef de Cuisine Ryōshū’s Passive ‘Rustle Up’ by 5.
   PL:
254. [Kwestia głosowa [get_11204_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=get_11204_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Kwestia głosowa [get_11204_1] (Identity Acquisition)] 쓸 만한 고기 있어…?
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=get_11204_1].dlg
   limit: do 120 znaków
   EN: Got some good meat for me…?
   PL:
256. [Kwestia głosowa [lobby_morning_11204_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=lobby_morning_11204_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Kwestia głosowa [lobby_morning_11204_1] (Morning Greeting)] 아침엔 가게 안 여는데. …재료를 구해오는 시간이거든.
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=lobby_morning_11204_1].dlg
   limit: do 120 znaków
   EN: Shop’s not open in the morn. …It’s when I bag ingredients.
   PL:
258. [Kwestia głosowa [lobby_noon_11204_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=lobby_noon_11204_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Kwestia głosowa [lobby_noon_11204_1] (Afternoon Greeting)] 료슈는 가게 안 쪽에 있어. …굳이 찾지 않는게 좋을 텐데. 너, 그러다가 고기 대신에 다져진다?
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=lobby_noon_11204_1].dlg
   limit: do 160 znaków
   EN: Ryōshū’s in the back of the shop. …Y’don’t wanna poke your head in there. Might be you that’s minced on the board, you dig?
   PL:
260. [Kwestia głosowa [lobby_night_11204_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=lobby_night_11204_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Kwestia głosowa [lobby_night_11204_1] (Evening Greeting)] …이 시간에 가게 앞에 서성거리지 마. …재료인 줄 착각할 뻔했잖아.
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=lobby_night_11204_1].dlg
   limit: do 120 znaków
   EN: …Don’t loiter in the front at this hour. Almost thought you to be a potential ingredient…
   PL:
262. [Kwestia głosowa [smalltalk_11204_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=smalltalk_11204_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Kwestia głosowa [smalltalk_11204_1] (Chatter #1)] 싱싱한 녀석들을 찾기가 어렵단 말이지…
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=smalltalk_11204_1].dlg
   limit: do 120 znaków
   EN: Fresh ones are hard to find…
   PL:
264. [Kwestia głosowa [smalltalk_11204_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=smalltalk_11204_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Kwestia głosowa [smalltalk_11204_2] (Chatter #2)] 우리 가게 파이, 아직 안 먹어 본 거야…? 없어서 못 먹는다고… 하하.
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=smalltalk_11204_2].dlg
   limit: do 120 znaków
   EN: Really now, you haven’t tried our pies…? Customers can’t get enough of ‘em… Haha.
   PL:
266. [Kwestia głosowa [smalltalk_11204_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=smalltalk_11204_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Kwestia głosowa [smalltalk_11204_3] (Chatter #3)] 담배를 끄고 요리해야 하는 거 아니냐고…? 그게 최고의 향신료인데 무슨 소리야…?
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=smalltalk_11204_3].dlg
   limit: do 160 znaków
   EN: I should keep the cigs outta my mouth when I’m cooking…? There’s no spice like it to add a zing, so what’re you on about…?
   PL:
268. [Kwestia głosowa [smalltalk_11204_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=smalltalk_11204_4].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Kwestia głosowa [smalltalk_11204_4] (Post-Uptie Chat 1)] 찰떡손파이… 먹고싶네. 매번 거래하던 녀석들에게서 받는 재료가 아니면 그 맛이 안난다고…
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=smalltalk_11204_4].dlg
   limit: do 150 znaków
   EN: Pasty hand pies… I sure miss ‘em. Just doesn’t taste the same if it’s not made from our usual suppliers’ produce…
   PL:
270. [Kwestia głosowa [smalltalk_11204_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=smalltalk_11204_5].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Kwestia głosowa [smalltalk_11204_5] (Post-Uptie Chat 2)] 적당히 타협할 줄도 알아야하는데… 미식의 예술이니 뭐니 하면서 매번 재료탓이란 말이지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=smalltalk_11204_5].dlg
   limit: do 150 znaków
   EN: Gotta know when to compromise, too… Girl’s too stubborn about her “art of delicacy”, always blaming the ingredients.
   PL:
272. [Kwestia głosowa [neglect_11204_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=neglect_11204_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Kwestia głosowa [neglect_11204_1] (Idle)] 으음… 이놈의 기계 팔이 결리네… 어쩌다 팔이 이렇게 됐냐고? 글쎄? 내 싱싱한 팔이 없어져서 어디로 가버렸을까?
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=neglect_11204_1].dlg
   limit: do 200 znaków
   EN: Mmgh… Mechanical arm’s sore again… What happened to my old arm, you ask? Well, whaddya think? Just where could a fresh and juicy limb go around these parts?
   PL:
274. [Kwestia głosowa [gacksung_11204_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=gacksung_11204_1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Kwestia głosowa [gacksung_11204_1] (Uptying)] 나를…? 하, 역시 진짜 셰프를 알아보는구만…?
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=gacksung_11204_1].dlg
   limit: do 120 znaków
   EN: Me…? Ha, guess you do know who the real chef is here, huh…?
   PL:
276. [Kwestia głosowa [formation_11204_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=formation_11204_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Kwestia głosowa [formation_11204_1] (Deployment)] 새 거래처를 찾으러 가는 거야?
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=formation_11204_1].dlg
   limit: do 120 znaków
   EN: Off to search for a new provider, are we?
   PL:
278. [Kwestia głosowa [battleentry_11204_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battleentry_11204_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Kwestia głosowa [battleentry_11204_1] (Stage Entry)] 신선한게 있으면 좋겠네.
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battleentry_11204_1].dlg
   limit: do 120 znaków
   EN: Hope there’s fresh finds.
   PL:
280. [Kwestia głosowa [battle_select_11204_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_select_11204_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Kwestia głosowa [battle_select_11204_1] (Viewed in Battle)] 어유, 깜짝아! 휘둘러 버릴 뻔했네.
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_select_11204_1].dlg
   limit: do 120 znaków
   EN: Yeesh, ya startled me! I almost swung at you.
   PL:
282. [Kwestia głosowa [battle_endcommand_11204_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_endcommand_11204_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Kwestia głosowa [battle_endcommand_11204_1] (Commencing Attack)] 썰어볼까!
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_endcommand_11204_1].dlg
   limit: do 120 znaków
   EN: Time to slice ‘n dice!
   PL:
284. [Kwestia głosowa [battle_enemy_break_11204_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_enemy_break_11204_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Kwestia głosowa [battle_enemy_break_11204_1] (Enemy Stagger)] 여기 썰고~ 저기 썰고~
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_enemy_break_11204_1].dlg
   limit: do 120 znaków
   EN: A cut goes here~ A chop goes there~
   PL:
286. [Kwestia głosowa [battle_break_11204_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_break_11204_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Kwestia głosowa [battle_break_11204_1] (Staggered)] 엇…
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_break_11204_1].dlg
   limit: do 120 znaków
   EN: Uh…
   PL:
288. [Kwestia głosowa [battle_kill_11204_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_kill_11204_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Kwestia głosowa [battle_kill_11204_1] (Enemy Killed)] 휴! 해체 끝~
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_kill_11204_1].dlg
   limit: do 120 znaków
   EN: Whew! All diced up~
   PL:
290. [Kwestia głosowa [battle_dead_11204_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_dead_11204_1].desc
   limit: do 120 znaków
   EN: Death
   PL:
291. [Kwestia głosowa [battle_dead_11204_1] (Death)] 아… 젠장…
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_dead_11204_1].dlg
   limit: do 120 znaków
   EN: Ah… Shoot…
   PL:
292. [Kwestia głosowa [choice_success_p_11204_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=choice_success_p_11204_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Kwestia głosowa [choice_success_p_11204_1] (Check Passed)] 이거 맞지?
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=choice_success_p_11204_1].dlg
   limit: do 120 znaków
   EN: This one, right?
   PL:
294. [Kwestia głosowa [choice_fail_n_11204_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=choice_fail_n_11204_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Kwestia głosowa [choice_fail_n_11204_1] (Check Failed)] 음… 상한 부위였나?
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=choice_fail_n_11204_1].dlg
   limit: do 120 znaków
   EN: Mmh… Was that part spoiled?
   PL:
296. [Kwestia głosowa [battle_clear_11204_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_clear_11204_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Kwestia głosowa [battle_clear_11204_1] (Victory Cry)] 썩 나쁘지 않은 수확이었어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_clear_11204_1].dlg
   limit: do 120 znaków
   EN: Not a bad haul by any means.
   PL:
298. [Kwestia głosowa [battle_clear_ex_11204_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_clear_ex_11204_1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Kwestia głosowa [battle_clear_ex_11204_1] (Extra Conditions Fulfilled)] 휴… 너무 많이 했나? 언제 들고 가지…
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_clear_ex_11204_1].dlg
   limit: do 120 znaków
   EN: Phew… Was that a bit too much? This’ll take a while to lug back…
   PL:
300. [Kwestia głosowa [battle_defeat_11204_1] — sytuacja] 전투 패배 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_defeat_11204_1].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [Kwestia głosowa [battle_defeat_11204_1] (Defeat Wail)] 으… 저건 맛 없는 고기 였을 거야.
   źródło: PersonalityVoiceDlg/Voice_Gregor_23GuCooker_11204.json :: dataList[id=battle_defeat_11204_1].dlg
   limit: do 120 znaków
   EN: Ugh… Bet it was bad meat anyway.
   PL:

## [00] Rosespanner Workshop Fixer — Gregor — 장미스패너 공방 해결사
- ID Tożsamości: `11205` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 2 · HP bazowe: 69 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Charge, Tremor, Rupture

302. [Karta Tożsamości — tytuł] 장미스패너 공방\n해결사
   źródło: Personalities.json :: dataList[id=11205].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rosespanner Workshop\nFixer
   PL:
303. [Karta Tożsamości — nazwa] 그레고르
   źródło: Personalities.json :: dataList[id=11205].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Karta Tożsamości — nazwa z tytułem] 그레고르
   źródło: Personalities.json :: dataList[id=11205].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Karta Tożsamości — opis] 그레고르의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=11205].desc
   limit: do 120 znaków
   EN: Gregor’s 5th Identity
   PL:
306. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 시동 걸기
   źródło: Skills.json :: dataList[id=1120501].levelList[level=1].name ; dataList[id=1120501].levelList[level=2].name ; dataList[id=1120501].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Rev Up
   PL:
307. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1120501].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1120501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1120501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL:
308. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] [WhenUse] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1120501].levelList[level=2].desc ; dataList[id=1120501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Charge Count
   PL:
309. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 진동 횟수가 5 이상이면, 파열 3 부여
   źródło: Skills.json :: dataList[id=1120501].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If target has 5+ [Vibration] Count, inflict 3 Rupture
   PL:
310. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 사슬 윤활
   źródło: Skills.json :: dataList[id=1120502].levelList[level=1].name ; dataList[id=1120502].levelList[level=2].name ; dataList[id=1120502].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Grease Chains
   PL:
311. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 2 증가
   źródło: Skills.json :: dataList[id=1120502].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1120502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1120502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
312. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 파열 횟수 1 증가
   źródło: Skills.json :: dataList[id=1120502].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1120502].levelList[level=2].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WhenUse] 자신의 충전 횟수 3 증가
   źródło: Skills.json :: dataList[id=1120502].levelList[level=2].desc ; dataList[id=1120502].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +3 Charge Count
   PL:
314. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1120502].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Rupture Count
   PL:
315. [Umiejętność 3 (×1) (ulepszenia 1,4) — nazwa] 갈아버리자고
   źródło: Skills.json :: dataList[id=1120503].levelList[level=1].name ; dataList[id=1120503].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Let's Grind 'Em
   PL:
316. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발. 진동 폭발 시 진동 횟수가 2 감소하고,\n충전 횟수를 최대 4 소모하여 소모한 충전 횟수만큼 파열 횟수 증가
   źródło: Skills.json :: dataList[id=1120503].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1120503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion], then reduce [Vibration] Count by 2 and consume up to 4 Charge Count on self to inflict Rupture Count equal to Charge Count consumed
   PL:
317. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1120503].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1120503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Rupture
   PL:
318. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상이 흐트러진 상태면 피해량 +10%
   źródło: Skills.json :: dataList[id=1120503].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1120503].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target is Staggered, deal +10% damage
   PL:
319. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1120503].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1120503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 317 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상이 흐트러진 상태면 피해량 +10%
   źródło: Skills.json :: dataList[id=1120503].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1120503].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 진동 횟수가 5 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1120503].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 5+ [Vibration] Count, Coin Power +1
   PL:
322. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상의 진동 횟수가 5 이상이면, 파열 3 부여
   źródło: Skills.json :: dataList[id=1120503].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 대상의 진동 횟수가 5 이상이면, 파열 3 부여
   źródło: Skills.json :: dataList[id=1120503].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1120504].levelList[level=1].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — nazwa] 톱날 가동
   źródło: Passives.json :: dataList[id=1120501].name
   limit: do 40 znaków
   EN: Sawblade Fired Up
   PL:
326. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — opis] [Vibration]이 있는 대상에게 부여하는 파열 +1
   źródło: Passives.json :: dataList[id=1120501].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Inflict +1 Rupture to targets that have [Vibration]
   PL:
327. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 톱날 정비
   źródło: Passives.json :: dataList[id=1120521].name
   limit: do 40 znaków
   EN: Sawblade Maintenance
   PL:
328. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 속도가 가장 느린 아군 1명이 [Vibration]이 있는 대상에게 부여하는 파열 +1
   źródło: Passives.json :: dataList[id=1120521].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: 1 ally with the slowest Speed inflicts +1 Rupture to targets that have [Vibration]
   PL:
329. [Kwestia głosowa [get_11205_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=get_11205_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Kwestia głosowa [get_11205_1] (Identity Acquisition)] 어어 그래, 나도 반갑고… 혹시 남는 나사 있나?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=get_11205_1].dlg
   limit: do 120 znaków
   EN: Yeah, hey there, nice to meet you... Got a screw to spare?
   PL:
331. [Kwestia głosowa [lobby_morning_11205_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=lobby_morning_11205_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Kwestia głosowa [lobby_morning_11205_1] (Morning Greeting)] 어디 보자~ 오늘 오전에 두 탕, 오후에 세 탕… 응, 커피 한 잔 정도 사치 부려도 되겠네.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=lobby_morning_11205_1].dlg
   limit: do 140 znaków
   EN: Let's see~ Two jobs for this morning, three in the afternoon... Yup, guess I can afford one coffee break.
   PL:
333. [Kwestia głosowa [lobby_noon_11205_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=lobby_noon_11205_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Kwestia głosowa [lobby_noon_11205_1] (Afternoon Greeting)] 혹시 우리 대장님 못 보셨나? 아까 후추 고추 상추 카레 맛 파이 내기에서 졌는데 갑자기 사라져서 말이야.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=lobby_noon_11205_1].dlg
   limit: do 170 znaków
   EN: Seen my boss around here? She lost a bet with pepper chili lettuce curry pie on the line a bit ago, and she hasn't returned yet.
   PL:
335. [Kwestia głosowa [lobby_night_11205_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=lobby_night_11205_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Kwestia głosowa [lobby_night_11205_1] (Evening Greeting)] 둥지의 야경은 언제 봐도 근사하지. 저 많은 빛들 중에 내 것이 없다는 게 문제지만.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=lobby_night_11205_1].dlg
   limit: do 120 znaków
   EN: The Nest's nightscape is always fascinating. Shame none of those lights are mine.
   PL:
337. [Kwestia głosowa [smalltalk_11205_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=smalltalk_11205_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Kwestia głosowa [smalltalk_11205_1] (Chatter #1)] 이봐, 그 시계 소리 때문에 괜히 초조해지는데 담배 정도는 맘 놓고 피게 해줘…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=smalltalk_11205_1].dlg
   limit: do 130 znaków
   EN: Hey, that ticking of your clock's making me nervous, can you let me smoke in peace at least...
   PL:
339. [Kwestia głosowa [smalltalk_11205_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=smalltalk_11205_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Kwestia głosowa [smalltalk_11205_2] (Chatter #2)] 보수만 제때제때 받으면 돼. 뭣하면 쓸만한 고철들로 줘도 괜찮고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=smalltalk_11205_2].dlg
   limit: do 130 znaków
   EN: Payments on time are all I ask for. If you're strapped for cash, I won't mind some useful scraps.
   PL:
341. [Kwestia głosowa [smalltalk_11205_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=smalltalk_11205_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Kwestia głosowa [smalltalk_11205_3] (Chatter #3)] 아니 잠깐 이게… 어어? 아… 괜찮아. 가끔 뻑날 때가 있어서… 응? 왜 그렇게 멀찌감치 떨어져 있나?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=smalltalk_11205_3].dlg
   limit: do 180 znaków
   EN: Wait a minute, what's wrong with... Huh? Oh... I'm fine. This thing just conks out sometimes... Hm? Why are you standing so far away?
   PL:
343. [Kwestia głosowa [smalltalk_11205_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=smalltalk_11205_4].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Kwestia głosowa [smalltalk_11205_4] (Post-Uptie Chat 1)] 응, 뭐 그때그때 팔을 바꿔 끼는 편이야. 원래는 불붙여 주는 용도의 팔도 있었는데 잘못하다 수염을 태워 먹었지 뭐야.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=smalltalk_11205_4].dlg
   limit: do 180 znaków
   EN: Well, yeah, I change this arm whenever needed. I used to have one for lighting fires, but I got careless and burned my beard with it.
   PL:
345. [Kwestia głosowa [smalltalk_11205_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=smalltalk_11205_5].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Kwestia głosowa [smalltalk_11205_5] (Post-Uptie Chat 2)] 당신, 나랑 좀 잘 맞는 것 같은데? 이번 의뢰 끝나고도 또 써먹을 일 있으면 우리 대장 통해서 연락 줘.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=smalltalk_11205_5].dlg
   limit: do 190 znaków
   EN: Say, you and I get along pretty well, don't you think? If you've got business for me after this request is done, tell my boss and I'll be there.
   PL:
347. [Kwestia głosowa [neglect_11205_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=neglect_11205_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Kwestia głosowa [neglect_11205_1] (Idle)] 혼자 두지 마. 나 은근히 외로움 타는 성격이거든.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=neglect_11205_1].dlg
   limit: do 120 znaków
   EN: Don't leave me alone, bud. I can get lonely pretty easily.
   PL:
349. [Kwestia głosowa [gacksung_11205_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=gacksung_11205_1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Kwestia głosowa [gacksung_11205_1] (Uptying)] 어, 음… 나 이곳에 계속 붙어 있을 생각은 아니었는데… 책임져 주는 거야?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=gacksung_11205_1].dlg
   limit: do 120 znaków
   EN: Oh, erm... I wasn't planning to stay here for long... You gonna take the responsibility?
   PL:
351. [Kwestia głosowa [formation_11205_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=formation_11205_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Kwestia głosowa [formation_11205_1] (Deployment)] 어디 가는지는 관심 없어. 안내나 해줘.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=formation_11205_1].dlg
   limit: do 120 znaków
   EN: Don't care where it is. Just lead the way.
   PL:
353. [Kwestia głosowa [battleentry_11205_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battleentry_11205_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Kwestia głosowa [battleentry_11205_1] (Stage Entry)] 아. 팔 배터리 교체, 했었나?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battleentry_11205_1].dlg
   limit: do 120 znaków
   EN: Right. Did I change the batteries for my arm?
   PL:
355. [Kwestia głosowa [battle_select_11205_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_select_11205_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Kwestia głosowa [battle_select_11205_1] (Viewed in Battle)] 뭐, 점검할 거라도 생긴 거야?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_select_11205_1].dlg
   limit: do 120 znaków
   EN: What, something needs maintenance?
   PL:
357. [Kwestia głosowa [battle_endcommand_11205_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_endcommand_11205_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Kwestia głosowa [battle_endcommand_11205_1] (Commencing Attack)] 시동 걸어볼까?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_endcommand_11205_1].dlg
   limit: do 120 znaków
   EN: Is it time to rev up?
   PL:
359. [Kwestia głosowa [battle_enemy_break_11205_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_enemy_break_11205_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Kwestia głosowa [battle_enemy_break_11205_1] (Enemy Stagger)] 할만하네.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_enemy_break_11205_1].dlg
   limit: do 120 znaków
   EN: Doable.
   PL:
361. [Kwestia głosowa [battle_break_11205_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_break_11205_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Kwestia głosowa [battle_break_11205_1] (Staggered)] 아이고… 살살해줘.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_break_11205_1].dlg
   limit: do 120 znaków
   EN: Ow... Easy, buddy.
   PL:
363. [Kwestia głosowa [battle_kill_11205_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_kill_11205_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Kwestia głosowa [battle_kill_11205_1] (Enemy Killed)] 어제 톱날을 열심히 손본 보람이 있네.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_kill_11205_1].dlg
   limit: do 120 znaków
   EN: Sharpening the sawblade yesterday paid off.
   PL:
365. [Kwestia głosowa [battle_dead_11205_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_dead_11205_1].desc
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Kwestia głosowa [battle_dead_11205_1] (Death)] 팔에… 자폭장치… 업그레이드 해둘걸…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_dead_11205_1].dlg
   limit: do 120 znaków
   EN: Should've... given my arm... a self-destruct upgrade...
   PL:
367. [Kwestia głosowa [choice_success_p_11205_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=choice_success_p_11205_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Kwestia głosowa [choice_success_p_11205_1] (Check Passed)] 뭐 이 정도 가지고 우쭐해하진 않아. 흠… 흠흠~
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=choice_success_p_11205_1].dlg
   limit: do 120 znaków
   EN: Well, I'm not one to get smug over this kind of stuff. Hmmm... Hmhmm~
   PL:
369. [Kwestia głosowa [choice_fail_n_11205_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=choice_fail_n_11205_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Kwestia głosowa [choice_fail_n_11205_1] (Check Failed)] 아이고, 오늘따라 팔이 왜 이렇게 뻐근한거야… 큼… 큼큼…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=choice_fail_n_11205_1].dlg
   limit: do 120 znaków
   EN: Oh boy, why's my arm so stiff today... Ahem... Kehm, hmm...
   PL:
371. [Kwestia głosowa [battle_clear_11205_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_clear_11205_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Kwestia głosowa [battle_clear_11205_1] (Victory Cry)] 이 정도는 해줘야지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_clear_11205_1].dlg
   limit: do 120 znaków
   EN: Better do my part.
   PL:
373. [Kwestia głosowa [battle_clear_ex_11205_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_clear_ex_11205_1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Kwestia głosowa [battle_clear_ex_11205_1] (Extra Conditions Fulfilled)] 뭐? 추가 수당 준다고? 사양은 안 할게.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_clear_ex_11205_1].dlg
   limit: do 120 znaków
   EN: What's that? You gonna pay me a bonus? I'm not about to turn it down.
   PL:
375. [Kwestia głosowa [battle_defeat_11205_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_defeat_11205_1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Kwestia głosowa [battle_defeat_11205_1] (Defeat Wail)] 아잇 참… 팔에 윤활제가 제대로 안 먹여서… 좀 삐그덕거렸어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kcorp_11205.json :: dataList[id=battle_defeat_11205_1].dlg
   limit: do 120 znaków
   EN: Ah, shoot... My arm keeps refusing to work with the grease... It was a little squeaky.
   PL:

## [000] Zwei Assoc. South Section 4 — Gregor — 남부 츠바이 협회 4과
- ID Tożsamości: `11206` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 90 · szybkość: 3–7 / 4–7 / 4–8 / 4–8
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: —

377. [Karta Tożsamości — tytuł] 남부 츠바이 협회\n4과
   źródło: Personalities.json :: dataList[id=11206].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Zwei Assoc.\nSouth Section 4
   PL:
378. [Karta Tożsamości — nazwa] 그레고르
   źródło: Personalities.json :: dataList[id=11206].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Karta Tożsamości — nazwa z tytułem] 그레고르
   źródło: Personalities.json :: dataList[id=11206].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Karta Tożsamości — opis] 그레고르의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=11206].desc
   limit: do 120 znaków
   EN: Gregor’s 6th Identity
   PL:
381. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 맞서기
   źródło: Skills_personality-12.json :: dataList[id=1120601].levelList[level=1].name ; dataList[id=1120601].levelList[level=2].name ; dataList[id=1120601].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Standoff
   PL:
382. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 방어 레벨 증가 2를 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Defense Level Up
   PL:
383. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 신속 1을 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain 1 Haste next turn
   PL:
384. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 방어 레벨 증가 2를 얻음\n[DefeatDuel] (자신의 방어 레벨 증가 X 3)만큼 보호막을 얻음. 다음 턴에 방어 레벨 증가 1을 얻음.
   źródło: Skills_personality-12.json :: dataList[id=1120601].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain 2 Defense Level Up\n[DefeatDuel] Gain Shield by (3 * Defense Level Up on self); Gain 1 Defense Level Up next turn
   PL:
385. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 신속 1을 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120601].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Haste next turn
   PL:
386. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 방어 레벨 증가 2를 얻음\n[DefeatDuel] (자신의 방어 레벨 증가 X 5)만큼 보호막을 얻음. 다음 턴에 방어 레벨 증가 2를 얻음.
   źródło: Skills_personality-12.json :: dataList[id=1120601].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain 2 Defense Level Up\n[DefeatDuel] Gain Shield by (5 * Defense Level Up on self); Gain 2 Defense Level Up next turn
   PL:
387. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 신속 2를 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 Haste next turn
   PL:
388. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 유연한 제압
   źródło: Skills_personality-12.json :: dataList[id=1120602].levelList[level=1].name ; dataList[id=1120602].levelList[level=2].name ; dataList[id=1120602].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 3 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Flexible Suppression
   PL:
389. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 방어 레벨 증가 2를 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120602].levelList[level=1].desc
   (powtórzenie elementu 382 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain 1 Defense Level Up next turn
   PL:
391. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 4, efekt 1 — opis] 자신의 방어 레벨 증가 가 6 이상이면, 피해량 +20%
   źródło: Skills_personality-12.json :: dataList[id=1120602].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: At 6+ Defense Level Up, deal +20% damage
   PL:
393. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 방어 레벨 증가 3을 얻음\n[WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 2 증가
   źródło: Skills_personality-12.json :: dataList[id=1120602].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 3 Defense Level Up\n[WhenUse] Gain +2 Aggro to this Skill Slot next turn
   PL:
394. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1120602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Defense Level Up next turn
   PL:
395. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1120602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 4, efekt 1 — opis] 자신의 방어 레벨 증가 가 6 이상이면, 피해량 +30%
   źródło: Skills_personality-12.json :: dataList[id=1120602].levelList[level=2].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: At 6+ Defense Level Up, deal +30% damage
   PL:
397. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 방어 레벨 증가 3을 얻음\n[WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 3 증가\n자신의 방어 레벨 증가 가 6 이상이면, 합 위력 +1
   źródło: Skills_personality-12.json :: dataList[id=1120602].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 3 Defense Level Up\n[WhenUse] Gain +3 Aggro to this Skill Slot next turn\nAt 6+ Defense Level Up, Clash Power +1
   PL:
398. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 4, efekt 1 — opis] 자신의 방어 레벨 증가 가 6 이상이면, 피해량 +40%
   źródło: Skills_personality-12.json :: dataList[id=1120602].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: At 6+ Defense Level Up, deal +40% damage
   PL:
399. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 수호자
   źródło: Skills_personality-12.json :: dataList[id=1120603].levelList[level=3].name ; dataList[id=1120603].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Guardian
   PL:
400. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 모든 아군에게 수비 위력 증가 2, 방어 레벨 증가 3 부여.\n자신의 방어 레벨 증가 가 6 이상이면, 코인 위력 +1\n자신의 방어 레벨 증가 가 10 이상이면, 피해량 +30%
   źródło: Skills_personality-12.json :: dataList[id=1120603].levelList[level=3].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Apply 2 Defense Power Up and 3 Defense Level Up to all allies\nAt 6+ Defense Level Up, Coin Power +1\nAt 10+ Defense Level Up, deal +30% damage
   PL:
401. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 모든 아군에게 방어 레벨 증가 3 부여
   źródło: Skills_personality-12.json :: dataList[id=1120603].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1120603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Apply 3 Defense Level Up to all allies next turn
   PL:
402. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 모든 아군에게 수비 위력 증가 2, 방어 레벨 증가 3 부여.\n자신의 방어 레벨 증가 6 당 코인 위력 +1 (최대 3)\n자신의 방어 레벨 증가 가 10 이상이면, 피해량 +50%
   źródło: Skills_personality-12.json :: dataList[id=1120603].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Apply 2 Defense Power Up and 3 Defense Level Up to all allies\nCoin Power +1 per 6 Defense Level Up (Max 3)\nAt 10+ Defense Level Up, deal +50% damage
   PL:
403. [Obrona (ulepszenia 1,4) — nazwa] 최선의 방어
   źródło: Skills_personality-12.json :: dataList[id=1120604].levelList[level=1].name ; dataList[id=1120604].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   limit: do 40 znaków
   EN: The Best Defense
   PL:
404. [Obrona (ulepszenie 1) — opis] [StartBattle] (자신의 방어 레벨 증가 X 2)만큼 보호막을 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain Shield by (2 * Defense Level Up on self)
   PL:
405. [Obrona (ulepszenie 4) — opis] [StartBattle] (자신의 방어 레벨 증가 X 2)만큼 보호막을 얻음\n[WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 5 증가
   źródło: Skills_personality-12.json :: dataList[id=1120604].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Gain Shield by (2 * Defense Level Up on self)\n[WhenUse] Gain +5 Aggro to this Skill Slot next turn
   PL:
406. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — nazwa] 전투 방패
   źródło: Passives.json :: dataList[id=1120601].name
   limit: do 40 znaków
   EN: Combat Shield
   PL:
407. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — opis] 전투 시작 시 2개 이상의 공격 타겟이 되었으면, 방어 레벨 증가 2를 얻음.\n전투 시작 시 자신의 체력이 50% 미만이면, 방어 레벨 증가 3을 얻음.
   źródło: Passives.json :: dataList[id=1120601].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If targeted by 2 or more attacks at the start of the combat phase, gain 2 Defense Level Up.\nIf at 50% or less HP at the start of the combat phase, gain 3 Defense Level Up.
   PL:
408. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Sloth) — nazwa] 당신의 방패
   źródło: Passives.json :: dataList[id=1120621].name
   limit: do 40 znaków
   EN: Your Shield
   PL:
409. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Sloth) — opis] 최대 체력이 가장 높은 아군 1명이 2개 이상의 공격 타겟이 되었으면, 방어 레벨 증가 3을 얻음
   źródło: Passives.json :: dataList[id=1120621].desc
   limit: do 120 znaków
   EN: If 1 ally with the highest Max HP is targeted by 2 or more attacks, gain 3 Defense Level Up
   PL:
410. [Kwestia głosowa [get_11206_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=get_11206_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Kwestia głosowa [get_11206_1] (Identity Acquisition)] 아! 아이구, 고객님… 혹시 라이터 한 번만 빌려줄 수 있으시나?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=get_11206_1].dlg
   limit: do 120 znaków
   EN: Ah! Hey, our client buddy, pal... Any chance I could borrow a light?
   PL:
412. [Kwestia głosowa [lobby_morning_11206_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=lobby_morning_11206_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Kwestia głosowa [lobby_morning_11206_1] (Morning Greeting)] 어휴, 아침부터 바쁘시네… 너무 앞서가지 마. 경호원이랑 발 좀 맞추자고. 응?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=lobby_morning_11206_1].dlg
   limit: do 150 znaków
   EN: Whew, you're an early riser. Don't stray too far, eh? Make it a little easier for your bodyguard to tag along.
   PL:
414. [Kwestia głosowa [lobby_noon_11206_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=lobby_noon_11206_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Kwestia głosowa [lobby_noon_11206_1] (Afternoon Greeting)] 밥은 먹고 하자고… 고객님? 당 떨어지면 싸우기 힘들단 말이야…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=lobby_noon_11206_1].dlg
   limit: do 130 znaków
   EN: 'Scuse me, client fella? Can we at least get something to eat? I can't fight on an empty stomach...
   PL:
416. [Kwestia głosowa [lobby_night_11206_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=lobby_night_11206_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Kwestia głosowa [lobby_night_11206_1] (Evening Greeting)] 밤엔 불빛이 얼마 없으니까 조심조심 하자고… 여차하면 옆에 꼭 붙고. 알겠지?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=lobby_night_11206_1].dlg
   limit: do 140 znaków
   EN: It gets dark at night, so let's watch our steps... If anything happens, just stick to my side. Got it?
   PL:
418. [Kwestia głosowa [smalltalk_11206_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=smalltalk_11206_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Kwestia głosowa [smalltalk_11206_1] (Chatter #1)] 설렁설렁이라니? 제일 좋은 경호가 티 안나는 경호라는 거, 몰라? 알만한 분이…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=smalltalk_11206_1].dlg
   limit: do 140 znaków
   EN: I don't look very vigilant? Come on, you should know that the best bodyguards are the least obvious ones.
   PL:
420. [Kwestia głosowa [smalltalk_11206_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=smalltalk_11206_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Kwestia głosowa [smalltalk_11206_2] (Chatter #2)] 아… 장갑? 훗, 처음부터 비장의 무기를 티내고 다니긴 좀 그렇잖아?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=smalltalk_11206_2].dlg
   limit: do 120 znaków
   EN: Oh, the glove? Heh, don't want to show all my cards just yet, wouldn't you agree?
   PL:
422. [Kwestia głosowa [smalltalk_11206_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=smalltalk_11206_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Kwestia głosowa [smalltalk_11206_3] (Chatter #3)] 여기서 한 대 태우고 가자구. 이야~ 이번 고객님은 흡연자라서 편해, 그치? 담배 태울 시간도 있고 말이야.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=smalltalk_11206_3].dlg
   limit: do 160 znaków
   EN: Let's take a smoke break here before moving on. Damn, aren't I lucky to have a client who smokes? Gives me time for a cig.
   PL:
424. [Kwestia głosowa [smalltalk_11206_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=smalltalk_11206_4].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Kwestia głosowa [smalltalk_11206_4] (Post-Uptie Chat 1)] 흣~ 자, 자. 뒤에 잘 숨어있으라고!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=smalltalk_11206_4].dlg
   limit: do 120 znaków
   EN: Heh~ Right, right. Stick close!
   PL:
426. [Kwestia głosowa [smalltalk_11206_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=smalltalk_11206_5].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Kwestia głosowa [smalltalk_11206_5] (Post-Uptie Chat 2)] 할 때는 한다니까~ 내가 실력도 없이 당신 옆에 붙어있었을까봐?\n어중간한 사람이 4과에 붙어있겠냐고~ 응?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=smalltalk_11206_5].dlg
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: What'd I say? Thought they'd send some greenhorn to protect you?\nI'm not in Section 4 for nothing, yeah?
   PL:
428. [Kwestia głosowa [neglect_11206_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=neglect_11206_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Kwestia głosowa [neglect_11206_1] (Idle)] 음흠~ 이렇게 기다리는 동안에는 맛있게 한 대… 아, 라이터가 안 켜졌었지…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=neglect_11206_1].dlg
   limit: do 120 znaków
   EN: Hmm hmm, time for a smoke break... Oh, right. I'm out of lighter fluid...
   PL:
430. [Kwestia głosowa [gacksung_11206_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=gacksung_11206_1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Kwestia głosowa [gacksung_11206_1] (Uptying)] 자~ 나서볼 때구만? 당신의 방패가 되어드리지!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=gacksung_11206_1].dlg
   limit: do 120 znaków
   EN: My time to shine, huh? Let me be your shield!
   PL:
432. [Kwestia głosowa [formation_11206_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=formation_11206_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Kwestia głosowa [formation_11206_1] (Deployment)] 어어. 금방 가지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=formation_11206_1].dlg
   limit: do 120 znaków
   EN: Uh huh. On my way.
   PL:
434. [Kwestia głosowa [battleentry_11206_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battleentry_11206_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Kwestia głosowa [battleentry_11206_1] (Stage Entry)] 습… 천천히 가자니까~
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battleentry_11206_1].dlg
   limit: do 120 znaków
   EN: Puff... Slow down, will ya?
   PL:
436. [Kwestia głosowa [battle_select_11206_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_select_11206_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Kwestia głosowa [battle_select_11206_1] (Viewed in Battle)] 어, 무슨 일이야?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_select_11206_1].dlg
   limit: do 120 znaków
   EN: Yeah, what's up?
   PL:
438. [Kwestia głosowa [battle_endcommand_11206_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_endcommand_11206_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Kwestia głosowa [battle_endcommand_11206_1] (Commencing Attack)] 내 뒤로!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_endcommand_11206_1].dlg
   limit: do 120 znaków
   EN: Get behind me!
   PL:
440. [Kwestia głosowa [battle_enemy_break_11206_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_enemy_break_11206_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Kwestia głosowa [battle_enemy_break_11206_1] (Enemy Stagger)] 어이쿠, 그정돈가?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_enemy_break_11206_1].dlg
   limit: do 120 znaków
   EN: Oof, did it hurt that much?
   PL:
442. [Kwestia głosowa [battle_break_11206_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_break_11206_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Kwestia głosowa [battle_break_11206_1] (Staggered)] 윽…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_break_11206_1].dlg
   limit: do 120 znaków
   EN: Ugh...
   PL:
444. [Kwestia głosowa [battle_kill_11206_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_kill_11206_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Kwestia głosowa [battle_kill_11206_1] (Enemy Killed)] 위협 요소 제거!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_kill_11206_1].dlg
   limit: do 120 znaków
   EN: Threat neutralized!
   PL:
446. [Kwestia głosowa [battle_dead_11206_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_dead_11206_1].desc
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Kwestia głosowa [battle_dead_11206_1] (Death)] 하아… 미안하구만… 고객… 님.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_dead_11206_1].dlg
   limit: do 120 znaków
   EN: Haah... Sorry about that... Client fella...
   PL:
448. [Kwestia głosowa [choice_success_p_11206_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=choice_success_p_11206_2].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Kwestia głosowa [choice_success_p_11206_2] (Check Passed)] 어때, 맘에 드시나?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=choice_success_p_11206_2].dlg
   limit: do 120 znaków
   EN: How do you like that?
   PL:
450. [Kwestia głosowa [choice_fail_n_11206_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=choice_fail_n_11206_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Kwestia głosowa [choice_fail_n_11206_1] (Check Failed)] 에잉… 뭐, 잘 안될 수도 있지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=choice_fail_n_11206_1].dlg
   limit: do 120 znaków
   EN: Darn... Well, things don't always work out, I guess.
   PL:
452. [Kwestia głosowa [battle_clear_11206_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_clear_11206_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Kwestia głosowa [battle_clear_11206_1] (Victory Cry)] 자, 계약 완수라고. 걱정할 필요 없었지?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_clear_11206_1].dlg
   limit: do 120 znaków
   EN: Contract fulfilled. See? It wasn't anything to worry about.
   PL:
454. [Kwestia głosowa [battle_clear_ex_11206_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_clear_ex_11206_1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Kwestia głosowa [battle_clear_ex_11206_1] (Extra Conditions Fulfilled)] 최선의 방어는 역시 공격이지… 하, 전투 방패라고 들어봤어?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_clear_ex_11206_1].dlg
   limit: do 120 znaków
   EN: The best defense is always offense... Ha, ever heard of offensive shield-use?
   PL:
456. [Kwestia głosowa [battle_defeat_11206_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_defeat_11206_1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
457. [Kwestia głosowa [battle_defeat_11206_1] (Defeat Wail)] 쓰읍… 임무 실패라… 쯧. 보수도 못 받고… 이참에 강제로 금연하게 생겼구만.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Zwei_11206.json :: dataList[id=battle_defeat_11206_1].dlg
   limit: do 120 znaków
   EN: Tsk... Mission failed, damn... Looks like I'll be forced to quit smoking for a while.
   PL:

## [000] Twinhook Pirates First Mate — Gregor — 쌍갈고리 해적단 부선장
- ID Tożsamości: `11207` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 3 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Poise, Bleed

458. [Karta Tożsamości — tytuł] 쌍갈고리 해적단\n부선장
   źródło: Personalities.json :: dataList[id=11207].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Twinhook Pirates\nFirst Mate
   PL:
459. [Karta Tożsamości — nazwa] 그레고르
   źródło: Personalities.json :: dataList[id=11207].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Karta Tożsamości — nazwa z tytułem] 그레고르
   źródło: Personalities.json :: dataList[id=11207].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Karta Tożsamości — opis] 그레고르의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=11207].desc
   limit: do 120 znaków
   EN: Gregor's 7th Identity
   PL:
462. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 협상 시작
   źródło: Skills_personality-12.json :: dataList[id=1120701].levelList[level=1].name ; dataList[id=1120701].levelList[level=2].name ; dataList[id=1120701].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Negotiation Start
   PL:
463. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 호흡 2 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Poise
   PL:
464. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신의 호흡 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1120701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +1 Poise Count
   PL:
465. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 호흡 3 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120701].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 3 Poise
   PL:
466. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1120701].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1120701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +1 Poise Count
   PL:
467. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-12.json :: dataList[id=1120701].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1120701].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict 2 Bleed
   PL:
468. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-12.json :: dataList[id=1120701].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1120701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 호흡 3 얻음\n대상의 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>이 7 이상이면 코인 위력 +1
   źródło: Skills_personality-12.json :: dataList[id=1120701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>, \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 3 Poise\nIf target has 7+ <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u>, Coin Power +1
   PL:
470. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 일방적 비즈니스
   źródło: Skills_personality-12.json :: dataList[id=1120702].levelList[level=1].name ; dataList[id=1120702].levelList[level=2].name ; dataList[id=1120702].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Unilateral Business
   PL:
471. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 호흡 횟수 2 증가
   źródło: Skills_personality-12.json :: dataList[id=1120702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Poise Count
   PL:
472. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 호흡 3 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain 3 Poise
   PL:
473. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_personality-12.json :: dataList[id=1120702].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1120702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1120702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL:
474. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-12.json :: dataList[id=1120702].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1120702].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1120702].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 호흡 횟수 3 증가
   źródło: Skills_personality-12.json :: dataList[id=1120702].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +3 Poise Count
   PL:
476. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 호흡 4 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120702].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain 4 Poise
   PL:
477. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-12.json :: dataList[id=1120702].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1120702].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 3 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-12.json :: dataList[id=1120702].levelList[level=2].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   EN: +30% Damage on Critical Hit
   PL:
479. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 출혈 7당 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 호흡 횟수 3 증가
   źródło: Skills_personality-12.json :: dataList[id=1120702].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: Coin Power +1 for every 7 Bleed on target (Max 2)\n[WhenUse] Gain +3 Poise Count
   PL:
480. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 4 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 4 Poise
   PL:
481. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 3 — opis] 크리티컬 피해량 +50%
   źródło: Skills_personality-12.json :: dataList[id=1120702].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   EN: +50% Damage on Critical Hit
   PL:
482. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 예정된 결렬
   źródło: Skills_personality-12.json :: dataList[id=1120703].levelList[level=3].name ; dataList[id=1120703].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Foregone Conclusion
   PL:
483. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 출혈 3당 호흡 1을 얻음 (최대 5)\n자신의 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></color></link></u>이 7 이상이면 코인 위력 +1
   źródło: Skills_personality-12.json :: dataList[id=1120703].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>, \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Poise per 3 Bleed on target (Max 5)\nAt 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></color></link></u>, Coin Power +1
   PL:
484. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 출혈 횟수 2 증가
   źródło: Skills_personality-12.json :: dataList[id=1120703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1120703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict +2 Bleed Count
   PL:
485. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] 탄환 1 소모
   źródło: Skills_personality-12.json :: dataList[id=1120703].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1120703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   EN: Spend 1 Ammo
   PL:
486. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] 크리티컬 피해량 +50%
   źródło: Skills_personality-12.json :: dataList[id=1120703].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 481 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 대상의 출혈 3당 호흡 1을 얻음 (최대 10)\n자신의 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></color></link></u> 7 당 코인 위력 +1 (최대 3)
   źródło: Skills_personality-12.json :: dataList[id=1120703].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>, \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Poise for every 3 Bleed on target (Max 10)\nGain Coin Power +1 for every 7 <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></color></link></u> on self (Max +3)
   PL:
488. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] 크리티컬 피해량 +100%
   źródło: Skills_personality-12.json :: dataList[id=1120703].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   EN: +100% Damage on Critical Hit
   PL:
489. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [EnemyKill] 다음 턴에 더하기 코인 강화 1을 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120703].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Gain 1 Plus Coin Boost next turn
   PL:
490. [Obrona (ulepszenia 1,4) — nazwa] 한 숨 돌릴까
   źródło: Skills_personality-12.json :: dataList[id=1120704].levelList[level=1].name ; dataList[id=1120704].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Take a Breather
   PL:
491. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] 호흡 1 얻음 (턴 당 최대 3)
   źródło: Skills_personality-12.json :: dataList[id=1120704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Gain 1 Poise (Max 3 per turn)
   PL:
492. [Obrona (ulepszenie 4) — opis] [OnSucceedEvade] 호흡 1 얻음 (턴 당 최대 5)
   źródło: Skills_personality-12.json :: dataList[id=1120704].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Gain 1 Poise (Max 5 per turn)
   PL:
493. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Pride) — nazwa] 총알은 비싸다고
   źródło: Passives.json :: dataList[id=1120701].name
   limit: do 40 znaków
   EN: Bullets are Pricey
   PL:
494. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Pride) — opis] - <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>이 부여된 대상에게 앞면 적중시 <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">부당 수익</color></link></u>을 얻음. (최대 4)\n- [Bullet]이 없는 경우, 대신 크리티컬 적중 시 <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">부당 수익</color></link></u>을 전부 소모하여, 피해량의 (5 x 소모한 <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">부당 수익</color></link></u>)% 만큼 추가 피해를 줌.
   źródło: Passives.json :: dataList[id=1120701].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>, <sprite name="Unjust_Enrichment">, <color=#f8c200>, <link="Unjust_Enrichment">, \n, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: - On Heads Hit against targets that have <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u>, gain <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">Unjust Enrichment</color></link></u>. (Max 4)\n- If this unit Critical Hits when out of [Bullet], spend all <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">Unjust Enrichment</color></link></u> and deal additional (5 x <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">Unjust Enrichment</color></link></u> consumed)% of damage dealt as bonus damage.
   PL:
495. [Pasywka bojowa (od ulepszenia 3, posiadane 2× Pride) — nazwa] 총알은 비싸다고
   źródło: Passives.json :: dataList[id=1120702].name
   (powtórzenie elementu 493 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Pasywka bojowa (od ulepszenia 3, posiadane 2× Pride) — opis] <style="highlight">- 상시 적용 : 탄환 7개 보유</style>\n- <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>이 부여된 대상에게 앞면 적중시 <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">부당 수익</color></link></u>을 얻음. (최대 4)\n<style="highlight">- 탄환 소모하는 코인 적중 시 <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">부당 수익</color></link></u>을 전부 소모하여, 피해량의 (25 x 소모한 <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">부당 수익</color></link></u>)% 만큼 추가 피해를 줌.</style>\n- [Bullet]이 없는 경우, 대신 크리티컬 적중 시 <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">부당 수익</color></link></u>을 전부 소모하여, (5 x 소모한 <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">부당 수익</color></link></u>)%만큼 추가 피해를 줌
   źródło: Passives.json :: dataList[id=1120702].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>, <sprite name="Unjust_Enrichment">, <color=#f8c200>, <link="Unjust_Enrichment">, \n, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: <style="highlight">- Always Active : Begin encounters with 7 Ammo</style>\n- On Heads Hit against targets that have <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u>, gain <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">Unjust Enrichment</color></link></u>. (Max 4)\n<style="highlight"> If a Coin that uses Ammo Hits, consume all <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">Unjust Enrichment</color></link></u> and deal additional (25 x <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">Unjust Enrichment</color></link></u> consumed)% of damage as bonus damage.</style>\n- If this unit Critical Hits when out of [Bullet], consume all <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">Unjust Enrichment</color></link></u> and deal additional (5 x <sprite name="Unjust_Enrichment"><color=#f8c200><u><link="Unjust_Enrichment">Unjust Enrichment</color></link></u> consumed)% of damage dealt as bonus damage.
   PL:
497. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — nazwa] 바람 구멍
   źródło: Passives.json :: dataList[id=1120721].name
   limit: do 40 znaków
   EN: New Breathing Hole
   PL:
498. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — opis] <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>을 가장 많이 보유한 아군 1명이 적 처치 시 다음 턴에 관통 피해량 증가 1 을 얻음. (턴 당 1회)
   źródło: Passives.json :: dataList[id=1120721].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>
   EN: If 1 ally that has the most <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u> defeats an enemy, gain 1 Pierce DMG Up next turn. (Once per turn)
   PL:
499. [Kwestia głosowa [get_11207_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=get_11207_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Kwestia głosowa [get_11207_1] (Identity Acquisition)] 푸하… 그래, 내가 쌍갈고리 해적단 부선장, 그레고르다. 사인이라도 해줘?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=get_11207_1].dlg
   limit: do 120 znaków
   EN: Hooh... Yeah, that's me. The first mate of the Twinhook Pirates. What, want an autograph?
   PL:
501. [Kwestia głosowa [lobby_morning_11207_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=lobby_morning_11207_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Kwestia głosowa [lobby_morning_11207_1] (Morning Greeting)] 어~ 굿모닝. 아, 얘기는 조금 이따 하자. 야~ 오늘 부업들 돌아가는 것 보고들 좀 해봐라~
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=lobby_morning_11207_1].dlg
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hey~ Good morning. Oh, talk'll have to wait.\nRight, lads! I want a report! How are our 'side jobs' doing~?
   PL:
503. [Kwestia głosowa [lobby_noon_11207_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=lobby_noon_11207_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Kwestia głosowa [lobby_noon_11207_1] (Afternoon Greeting)] 배 위에서 한가롭게 점심을 챙기고 그러진 않지. 배가 고프다 싶으면 적당히 그 때가 밥 먹을 때인 거야.\n물론, 허락없이 식량창고를 뒤지는 놈은 그대로 돛대에 묶여야지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=lobby_noon_11207_1].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lunch? On a ship? Lunch ain't a thing in the life of a sailorman, friend. Just eat when you're starting to feel peckish.\nIf you steal from our food storage, though... Now that's asking to get tied to the mast.
   PL:
505. [Kwestia głosowa [lobby_night_11207_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=lobby_night_11207_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Kwestia głosowa [lobby_night_11207_1] (Evening Greeting)] 밤도 됐겠다, 나가서 술이나 한 잔 하고 싶은데… 후크 이 놈이 도통 돌아와야지, 쯧. 자리를 비우고 싶어도 비울 수가 없네.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=lobby_night_11207_1].dlg
   limit: do 230 znaków
   EN: It's getting late... And I can feel the call of alcohol from outside. Hook, you bastard. Where the hell are you? I'd love to get out for a bit, but I've got responsibilities.
   PL:
507. [Kwestia głosowa [smalltalk_11207_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=smalltalk_11207_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Kwestia głosowa [smalltalk_11207_1] (Chatter #1)] 인어 향수는 그렇게 돈이 안돼. 결국 이것 저것 손을 벌려야만 돈이 들어오는 법이거든. 정보든, 고래기름이든, …사람이든!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=smalltalk_11207_1].dlg
   limit: do 150 znaków
   EN: Mermaid Perfume ain't such a lucrative venture. Gotta branch out like a kraken. Intel, Whale oil, or even people!
   PL:
509. [Kwestia głosowa [smalltalk_11207_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=smalltalk_11207_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Kwestia głosowa [smalltalk_11207_2] (Chatter #2)] 우리가 여기 저기 들쑤시고 다니는 거? 뭐, 해적이라면 당연한 거 아닌가? …우리는 든든한 뒷배도 있다고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=smalltalk_11207_2].dlg
   limit: do 180 znaków
   EN: What, we're poking too many hornet's nests? Well, that's just the life of a pirate. ... Besides, we've got somebody looking out for us.
   PL:
511. [Kwestia głosowa [smalltalk_11207_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=smalltalk_11207_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Kwestia głosowa [smalltalk_11207_3] (Chatter #3)] 어우, 잠깐 잠깐. 인질이라니, 말이 조금 험하네~ 우리 사업에 중요한 손님을 모신 것 뿐이라고. 조금 터프하게 대하는 거 뿐이야.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=smalltalk_11207_3].dlg
   limit: do 240 znaków
   EN: Hey, wait up. Wait up. Hostages? A bit crude to call them that, nah? We're just having... very important guests over for business. And we're just putting up some of that tough guy act.
   PL:
513. [Kwestia głosowa [smalltalk_11207_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=smalltalk_11207_4].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Kwestia głosowa [smalltalk_11207_4] (Post-Uptie Chat 1)] 어, 맞아 맞아. 이건 협박이야. 지금 우리들하고 따라가지 않으면 머리통에 바람구멍이 뚫릴 거라니까? 아니 아니, 총알은 비싸니까 이 갈고리로 뚫지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=smalltalk_11207_4].dlg
   limit: do 280 znaków
   EN: Uh huh. Yep yep. This is a threat. Come with us, or I'll give your skull a new hole to breathe out of. No, I'm not gonna shoot you. Bullets are pricey, y'know. Instead... lemme introduce you to my hook right here.
   PL:
515. [Kwestia głosowa [smalltalk_11207_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=smalltalk_11207_5].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Kwestia głosowa [smalltalk_11207_5] (Post-Uptie Chat 2)] 컨테이너에 잠깐 들어가 있는 거야, 잠깐~ 습! 벌써부터 왜 이렇게 떨어? 어차피 들어가면 추워서 많이 떨건데, 먼저 힘 빼지 말구~
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=smalltalk_11207_5].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Now just go in ahead and rest up in that shipping container, 'kay?\nWait~ Tsk tsk! Why are you shuddering? You'll have plenty of time for that once we get you situated nicely in that cold storage. Don't waste your strength now~
   PL:
517. [Kwestia głosowa [neglect_11207_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=neglect_11207_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Kwestia głosowa [neglect_11207_1] (Idle)] 후~ 항구선에서 멍하니 시덥지 않은 일하면서 대기하고 있다보면, 후크랑 호수에서 배를 털 때가 그리워지네…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=neglect_11207_1].dlg
   limit: do 190 znaków
   EN: Sigh~ Doin' this kinda boring desk job on a portship... Makes me miss the days Hook and I used to sail the high Lakes, looting treasures, ships...
   PL:
519. [Kwestia głosowa [gacksung_11207_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=gacksung_11207_1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Kwestia głosowa [gacksung_11207_1] (Uptying)] 동업하고 싶다고? 음~ 그래, 뭐. 너도 사이즈가 되는 것 같기도 하고. 어디, 잘 해보자고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=gacksung_11207_1].dlg
   limit: do 130 znaków
   EN: You wanna work together? Hmm~ Well, sure. I think you'll do. Well, then... let's make this work.
   PL:
521. [Kwestia głosowa [formation_11207_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=formation_11207_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Kwestia głosowa [formation_11207_1] (Deployment)] 부선장이 필요한가?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=formation_11207_1].dlg
   limit: do 120 znaków
   EN: Need a first mate?
   PL:
523. [Kwestia głosowa [battleentry_11207_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battleentry_11207_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Kwestia głosowa [battleentry_11207_1] (Stage Entry)] 직접 손 봐주지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battleentry_11207_1].dlg
   limit: do 120 znaków
   EN: Fine, I'll do it myself.
   PL:
525. [Kwestia głosowa [battle_select_11207_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_select_11207_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Kwestia głosowa [battle_select_11207_1] (Viewed in Battle)] 바빠, 밑에 애들한테 말해.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_select_11207_1].dlg
   limit: do 120 znaków
   EN: I'm busy. Go bother one of my underlings.
   PL:
527. [Kwestia głosowa [battle_endcommand_11207_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_endcommand_11207_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Kwestia głosowa [battle_endcommand_11207_1] (Commencing Attack)] 바람 구멍을 내주지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_endcommand_11207_1].dlg
   limit: do 120 znaków
   EN: I'll poke you a new breathing hole.
   PL:
529. [Kwestia głosowa [battle_enemy_break_11207_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_enemy_break_11207_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Kwestia głosowa [battle_enemy_break_11207_1] (Enemy Stagger)] 꼭 찢어진 돛같이 흐느적거리는구만.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_enemy_break_11207_1].dlg
   limit: do 120 znaków
   EN: Flapping like a torn sail, huh?
   PL:
531. [Kwestia głosowa [battle_break_11207_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_break_11207_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Kwestia głosowa [battle_break_11207_1] (Staggered)] 뭣…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_break_11207_1].dlg
   limit: do 120 znaków
   EN: What...
   PL:
533. [Kwestia głosowa [battle_kill_11207_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_kill_11207_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Kwestia głosowa [battle_kill_11207_1] (Enemy Killed)] 헹, 별 것도 아니네.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_kill_11207_1].dlg
   limit: do 120 znaków
   EN: Heh, that was nothing.
   PL:
535. [Kwestia głosowa [battle_dead_11207_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_dead_11207_1].desc
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Kwestia głosowa [battle_dead_11207_1] (Death)] 내, 내가… 죽을 리가… 주, 중지에게…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_dead_11207_1].dlg
   limit: do 120 znaków
   EN: I-I can't die like this... The M-Middle will...
   PL:
537. [Kwestia głosowa [choice_success_p_11207_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=choice_success_p_11207_2].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Kwestia głosowa [choice_success_p_11207_2] (Check Passed)] 흥, 보물상자 열쇠 따는 게 더 어렵겠어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=choice_success_p_11207_2].dlg
   limit: do 120 znaków
   EN: Heh, easier than picking open a treasure chest.
   PL:
539. [Kwestia głosowa [choice_fail_n_11207_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=choice_fail_n_11207_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Kwestia głosowa [choice_fail_n_11207_1] (Check Failed)] 나는 경고했어, 이런 거 잘 못한다고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=choice_fail_n_11207_1].dlg
   limit: do 120 znaków
   EN: What'd I say? I'm not good with this kinda thing.
   PL:
541. [Kwestia głosowa [battle_clear_11207_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_clear_11207_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Kwestia głosowa [battle_clear_11207_1] (Victory Cry)] 성공적인 비즈니스였지. 몇몇은 손님으로 들이자고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_clear_11207_1].dlg
   limit: do 120 znaków
   EN: Another day, another profitable business. Let's take some of 'em as our guests.
   PL:
543. [Kwestia głosowa [battle_clear_ex_11207_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_clear_ex_11207_1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Kwestia głosowa [battle_clear_ex_11207_1] (Extra Conditions Fulfilled)] 싹 다 정리해버렸네… 이러면 돈이 덜 나오는데. 흠, 이놈들 지갑 좀 볼까?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_clear_ex_11207_1].dlg
   limit: do 180 znaków
   EN: Well, we wiped the floor with them. That doesn't leave much for our... 'business'. Hm, let's check their wallets and see what they've got.
   PL:
545. [Kwestia głosowa [battle_defeat_11207_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_defeat_11207_1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Kwestia głosowa [battle_defeat_11207_1] (Defeat Wail)] 하… 전부 기억했어. 얼굴, 이름… 작은 누님이 나서면, 너희는 끝장이야.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Hook_11207.json :: dataList[id=battle_defeat_11207_1].dlg
   limit: do 130 znaków
   EN: Haah... I got your faces and names... Once the Big Sister gets here, you're finished. All of you.
   PL:

## [00] Kurokumo Clan Captain — Gregor — 흑운회 부조장
- ID Tożsamości: `11208` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 3 · HP bazowe: 76 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed

547. [Karta Tożsamości — tytuł] 흑운회\n부조장
   źródło: Personalities.json :: dataList[id=11208].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Kurokumo Clan\nCaptain
   PL:
548. [Karta Tożsamości — nazwa] 그레고르
   źródło: Personalities.json :: dataList[id=11208].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Karta Tożsamości — nazwa z tytułem] 그레고르
   źródło: Personalities.json :: dataList[id=11208].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Karta Tożsamości — opis] 그레고르의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=11208].desc
   limit: do 120 znaków
   EN: Gregor's 8th Identity
   PL:
551. [Umiejętność 1 (×3) (ulepszenia 1–4) — nazwa] 구름베기
   źródło: Skills_personality-12.json :: dataList[id=1120801].levelList[level=1].name ; dataList[id=1120801].levelList[level=2].name ; dataList[id=1120801].levelList[level=3].name ; dataList[id=1120801].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 5 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Lenticular Rend
   PL:
552. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WinDuel] [Laceration] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Laceration]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuel] Inflict 1 [Laceration]
   PL:
553. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1120801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict +1 [Laceration] Count
   PL:
554. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Laceration]이 7 이상이면 합 위력 +1</style>\n[WinDuel] [Laceration] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120801].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">[WhenUse] If target has 7+ [Laceration], Clash Power +1</style>\n[WinDuel] Inflict 1 [Laceration]
   PL:
555. [Umiejętność 1 (×3) (ulepszenia 2–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1120801].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1120801].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1120801].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
556. [Umiejętność 1 (×3) (ulepszenie 3) — opis] [WhenUse_Force] <color=#EBCAA2>대상의 [Laceration]이 7 이상이면 합 위력 +1</color>\n[WinDuel] [Laceration] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120801].levelList[level=3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#EBCAA2>, </color>, \n, [WhenUse_Force], [Laceration], [WinDuel]
   znaczenie tagów: [WhenUse_Force] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse_Force] <color=#EBCAA2>If target has 7+ [Laceration], Clash Power +1</color>\n[WinDuel] Inflict 1 [Laceration]
   PL:
557. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 [Laceration]이 7 이상이면 합 위력 +<style="highlight">2</style>\n[WinDuel] [Laceration] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120801].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has 7+ [Laceration], Clash Power +<style="highlight">2</style>\n[WinDuel] Inflict 1 [Laceration]
   PL:
558. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 먹구름
   źródło: Skills_personality-12.json :: dataList[id=1120802].levelList[level=1].name ; dataList[id=1120802].levelList[level=2].name ; dataList[id=1120802].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 5 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Shadow Cloud
   PL:
559. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 2 부여
   źródło: Skills_personality-12.json :: dataList[id=1120802].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1120802].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1120802].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 2 [Laceration]
   PL:
560. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 공격 레벨 감소 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120802].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1120802].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1120802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Offense Level Down
   PL:
561. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10 이상이면, 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120802].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1120802].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 10+ [Laceration], inflict 1 Attack Power Down next turn
   PL:
562. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Laceration]이 7 이상이면 합 위력 +2
   źródło: Skills_personality-12.json :: dataList[id=1120802].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 7+ [Laceration], Clash Power +2
   PL:
563. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 7 이상이면, 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120802].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 7+ [Laceration], inflict 1 Attack Power Down next turn
   PL:
564. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 먹구름 깨어가르기
   źródło: Skills_personality-12.json :: dataList[id=1120803].levelList[level=3].name ; dataList[id=1120803].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Shadowcloud Shattercleave
   PL:
565. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 [Laceration]이 7 이상이면 합 위력 +1
   źródło: Skills_personality-12.json :: dataList[id=1120803].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 7+ [Laceration], Clash Power +1
   PL:
566. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 공격 레벨 감소 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120803].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1120803].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 7 이상이면 다음 턴에 공격 레벨 감소 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120803].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1120803].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 7+ [Laceration], inflict 1 Offense Level Down next turn
   PL:
568. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 공격 레벨 감소 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120803].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1120803].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 7 이상이면 다음 턴에 공격 레벨 감소 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120803].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1120803].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10 이상이면, 다음 턴에 더하기 코인 약화 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120803].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 10+ [Laceration], inflict 1 Plus Coin Drop next turn
   PL:
571. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 대상의 [Laceration]이 7 이상이면 합 위력 +1\n[WhenUse] 대상의 [Laceration]이 10 이상이면 코인 위력 +1
   źródło: Skills_personality-12.json :: dataList[id=1120803].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 7+ [Laceration], Clash Power +1\n[WhenUse] If target has 10+ [Laceration], Coin Power +1
   PL:
572. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 3 부여
   źródło: Skills_personality-12.json :: dataList[id=1120803].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 3 [Laceration]
   PL:
573. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 <style="highlight">7</style> 이상이면, 다음 턴에 더하기 코인 약화 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120803].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has <style="highlight">7</style>+ [Laceration], inflict 1 Plus Coin Drop next turn
   PL:
574. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-12.json :: dataList[id=1120804].levelList[level=1].name ; dataList[id=1120804].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — nazwa] 흑운도
   źródło: Passives.json :: dataList[id=1120801].name
   limit: do 40 znaków
   EN: Dark Cloud Blade
   PL:
576. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — opis] 합 승리 시 [Laceration] 1 부여 (턴 당 3회)
   źródło: Passives.json :: dataList[id=1120801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Clash Win: inflict 1 [Laceration] (3 times per turn)
   PL:
577. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 흑운검법
   źródło: Passives.json :: dataList[id=1120821].name
   limit: do 40 znaków
   EN: Dark Cloud Style
   PL:
578. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 속도가 가장 느린 아군 1명이 [Laceration]이 10 이상 부여된 적에게 공격 적중 시 다음 턴에 공격 레벨 감소 1 부여 (턴 당 3회)
   źródło: Passives.json :: dataList[id=1120821].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: When 1 ally with the slowest Speed hits an enemy that has 10+ [Laceration], inflict 1 Offense Level Down next turn (3 times per turn)
   PL:
579. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Lust) — nazwa] 흑운검법
   źródło: Passives.json :: dataList[id=1120831].name
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Lust) — opis] 속도가 가장 느린 아군 1명이 [Laceration]이 7 이상 부여된 적에게 공격 적중 시 다음 턴에 공격 레벨 감소 1 부여 (턴 당 3회)
   źródło: Passives.json :: dataList[id=1120831].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: When 1 ally with the slowest Speed hits an enemy that has 7+ [Laceration], inflict 1 Offense Level Down next turn (3 times per turn)
   PL:
581. [Kwestia głosowa [get_11208_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=get_11208_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Kwestia głosowa [get_11208_1] (Identity Acquisition)] 아우, 이거. 맛있다아~ 한 병만 더… 흐히.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=get_11208_1].dlg
   limit: do 120 znaków
   EN: Man, this is some good wine~ Anotha bottle, please... Heheheh.
   PL:
583. [Kwestia głosowa [lobby_morning_11208_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=lobby_morning_11208_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Kwestia głosowa [lobby_morning_11208_1] (Morning Greeting)] 아침 숙취? 그런 건 없어~ 하루죙일 마시면 계속 구름을 떠다니는 기분이잖아? 응?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=lobby_morning_11208_1].dlg
   limit: do 130 znaków
   EN: Hangover? What hangover~? As long as I never sober up, I can be on cloud nine all day, eh? Eh?
   PL:
585. [Kwestia głosowa [lobby_noon_11208_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=lobby_noon_11208_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Kwestia głosowa [lobby_noon_11208_1] (Afternoon Greeting)] 오늘은 비번이잖아~ 너도, 낮술 한 잔 해! 자, 이리 와서 앉아. 여기! 젓가락이랑 잔 하나씩!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=lobby_noon_11208_1].dlg
   limit: do 210 znaków
   EN: C'mon, you're off duty today, ain'tcha? Day drinking on off hours is a-ok! C'mere, sit down. 'Scuse me! Can we get a pair of chopsticks and a shot glass here?
   PL:
587. [Kwestia głosowa [lobby_night_11208_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=lobby_night_11208_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Kwestia głosowa [lobby_night_11208_1] (Evening Greeting)] 으응~ 밤이 되니까 시끌시끌 하구만. 어! 밖에 별 일 없었지? 그치? 자~ 그러면 여기 와서 앉아라~ 내가 주는 술, 안 마신지 오래 됐잖아?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=lobby_night_11208_1].dlg
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ngh... It gets pretty rowdy out there at night, eh?\nOh, hey! All good out there? Then c'mere and join me~ Been a while since I got ya a drink, huh?
   PL:
589. [Kwestia głosowa [smalltalk_11208_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=smalltalk_11208_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Kwestia głosowa [smalltalk_11208_1] (Chatter #1)] 조직 생활이라는게 별 거 없다~ 시키는 거 잘 하구, 썰어 제낄 놈 썰고! 그러면 밑에 아우들도 생기고~ 그런 거야!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=smalltalk_11208_1].dlg
   limit: do 220 znaków
   EN: There ain't much to being a part of a Syndicate~ Just do as you're told and kill as you're told! Keep doin' that, get yourself some underlings, and so on. Know what I mean?
   PL:
591. [Kwestia głosowa [smalltalk_11208_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=smalltalk_11208_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Kwestia głosowa [smalltalk_11208_2] (Chatter #2)] 아… 그, 검가인가 범계인가 하는 걔네? 오늘 밤에 처들어 갈 거라고? 아후… 벌써 그런 날짜가 됐나?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=smalltalk_11208_2].dlg
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Oh, those, uh... Blade Rummage... no. Blunder Lineage... was it?\nHuh, we're attacking them tonight? Whew... time sure does fly, huh?
   PL:
593. [Kwestia głosowa [smalltalk_11208_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=smalltalk_11208_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Kwestia głosowa [smalltalk_11208_3] (Chatter #3)] 야! 출정주, 출정주! 이런 건 딱! 한 잔 돌려가면서 마시고서 끈끈한 우정을 안고 가는 거야! 왜 그렇게 딱딱하게 굴어~ 응?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=smalltalk_11208_3].dlg
   limit: do 260 znaków
   EN: Hey, hey! Are ya really about to go into battle without a shot of pre-battle drink? Come on, we'll share a liquor bowl and do some team buildin' before a big fight! Can't have ya going in there dry, huh?
   PL:
595. [Kwestia głosowa [smalltalk_11208_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=smalltalk_11208_4].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Kwestia głosowa [smalltalk_11208_4] (Post-Uptie Chat 1)] 그래. S사에서 넘어 온 떠돌이가 저것들이라고.\n애들은 다 준비해 뒀겠지? 이 곳이 누구 영역인지 확실히 각인시킨다. 돌격!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=smalltalk_11208_4].dlg
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gotcha. So they're the vagrants from S Corp.?\nAre the boys ready? Good, let's remind 'em whose turf they're treading on. Charge!
   PL:
597. [Kwestia głosowa [smalltalk_11208_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=smalltalk_11208_5].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Kwestia głosowa [smalltalk_11208_5] (Post-Uptie Chat 2)] 너 아직도 술 안 깼냐. 내가 마실 땐 마시고 할 땐 하자고 말 안했냐?\n하… 길게 말 안할게, 딱 2인분만 해갖고 와. 그럼 용서해 준다. 가라!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=smalltalk_11208_5].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Are you seriously still blitzed? What'd I say? What do I always say? Drink when you gotta drink, and sober up when you gotta sober up.\nHaah... I'll keep this short. Just do double your usual numbers, and I won't get mad. C'mon, go!
   PL:
599. [Kwestia głosowa [neglect_11208_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=neglect_11208_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Kwestia głosowa [neglect_11208_1] (Idle)] 음흠~ 어유, 술 기운이 벌써 풀리네. 에잉, 나 먼저 마신다?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=neglect_11208_1].dlg
   limit: do 120 znaków
   EN: Mmhm~ Man, I'm already starting to sober up. You don't mind if I get started first, do ya?
   PL:
601. [Kwestia głosowa [gacksung_11208_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=gacksung_11208_1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Kwestia głosowa [gacksung_11208_1] (Uptying)] 후… 어느 때보다 머리가 개운하구만. 담배 맛도 최고야. 날뛰기에는… 최고의 몸 상태군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=gacksung_11208_1].dlg
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hooah... My mind's clearer than ever, man. And with this delicious cig...\nI'd say I'm in peak physical shape... to wreck shop.
   PL:
603. [Kwestia głosowa [formation_11208_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=formation_11208_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Kwestia głosowa [formation_11208_1] (Deployment)] 으에? 지금 가야 해?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=formation_11208_1].dlg
   limit: do 120 znaków
   EN: Huh? We're leaving? Now?
   PL:
605. [Kwestia głosowa [battleentry_11208_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battleentry_11208_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Kwestia głosowa [battleentry_11208_1] (Stage Entry)] 크흠, 핫! 자, 해장 끝!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battleentry_11208_1].dlg
   limit: do 120 znaków
   EN: Ahm, hah! Right, now I'm all sobered up!
   PL:
607. [Kwestia głosowa [battle_select_11208_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_select_11208_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Kwestia głosowa [battle_select_11208_1] (Viewed in Battle)] 싸울 때 말 걸지 말라니까! …뭐야?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_select_11208_1].dlg
   limit: do 120 znaków
   EN: I told you, I don't talk and fight! ... So what is it?
   PL:
609. [Kwestia głosowa [battle_endcommand_11208_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_endcommand_11208_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Kwestia głosowa [battle_endcommand_11208_1] (Commencing Attack)] 단칼에!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_endcommand_11208_1].dlg
   limit: do 120 znaków
   EN: First try!
   PL:
611. [Kwestia głosowa [battle_enemy_break_11208_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_enemy_break_11208_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Kwestia głosowa [battle_enemy_break_11208_1] (Enemy Stagger)] 왜 이렇게 흐느적대?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_enemy_break_11208_1].dlg
   limit: do 120 znaków
   EN: What got you all wobbly?
   PL:
613. [Kwestia głosowa [battle_break_11208_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_break_11208_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Kwestia głosowa [battle_break_11208_1] (Staggered)] 악…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_break_11208_1].dlg
   limit: do 120 znaków
   EN: Agh...
   PL:
615. [Kwestia głosowa [battle_kill_11208_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_kill_11208_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Kwestia głosowa [battle_kill_11208_1] (Enemy Killed)] 거 참, 재미 없게.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_kill_11208_1].dlg
   limit: do 120 znaków
   EN: Man, what a letdown.
   PL:
617. [Kwestia głosowa [battle_dead_11208_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_dead_11208_1].desc
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Kwestia głosowa [battle_dead_11208_1] (Death)] 하필… 이면… 마시던 술… 생각이 나냐…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_dead_11208_1].dlg
   limit: do 120 znaków
   EN: Is my last thought... really gonna be... about... that drink I left back home...?
   PL:
619. [Kwestia głosowa [choice_success_p_11208_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=choice_success_p_11208_2].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Kwestia głosowa [choice_success_p_11208_2] (Check Passed)] 오! 이거 됐네! 상품 없냐?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=choice_success_p_11208_2].dlg
   limit: do 120 znaków
   EN: Oh! Hey, that worked! Do I get a prize?
   PL:
621. [Kwestia głosowa [choice_fail_n_11208_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=choice_fail_n_11208_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Kwestia głosowa [choice_fail_n_11208_1] (Check Failed)] 아유, 손 끝이 자꾸 떨려서… 미안~
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=choice_fail_n_11208_1].dlg
   limit: do 120 znaków
   EN: My bad, my bad... I've got a shaky hand, you know~
   PL:
623. [Kwestia głosowa [battle_clear_11208_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_clear_11208_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Kwestia głosowa [battle_clear_11208_1] (Victory Cry)] 뭐, 어찌저찌 체면은 살렸네… 야, 너희. 이것밖에 못할 거냐?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_clear_11208_1].dlg
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Well, at least that wasn't a complete disaster...\nGuys. Yeah, you guys. Was this really, really the best you could do?
   PL:
625. [Kwestia głosowa [battle_clear_ex_11208_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_clear_ex_11208_1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Kwestia głosowa [battle_clear_ex_11208_1] (Extra Conditions Fulfilled)] 흠~ 아주 만족스럽구만! 좋아, 오늘은 회식이다! 조장님 카드 갖고 온다? 아무도 빼지 마라!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_clear_ex_11208_1].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hm~ Now that's what I call a satisfying result! Perfect, then tonight's a team drinking night! Wait 'till I come back with the Patriarch's card.\nNone of you are allowed to sit this one out, got it?
   PL:
627. [Kwestia głosowa [battle_defeat_11208_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_defeat_11208_1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Kwestia głosowa [battle_defeat_11208_1] (Defeat Wail)] …우리 조. 오늘 아무도 밥 못 먹는다. 죄다 사무실 들어가서 대기해. 오늘은 니놈들 피를 갈아 마실테니까…!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Kurokumo_11208.json :: dataList[id=battle_defeat_11208_1].dlg
   limit: do 230 znaków
   EN: ... No dinner for anyone tonight. Go back to the office and remain on standby because I'm going to teach you all a lesson. Prepare to see some shit, you useless bastards...!
   PL:

## [000] Edgar Family Heir — Gregor — 에드가 가문 승계자
- ID Tożsamości: `11209` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 4 · HP bazowe: 66 · szybkość: 3–6 / 3–7 / 3–8 / 3–8
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Sinking

629. [Karta Tożsamości — tytuł] 에드가 가문\n승계자
   źródło: Personalities.json :: dataList[id=11209].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Edgar Family\nHeir
   PL:
630. [Karta Tożsamości — nazwa] 그레고르
   źródło: Personalities.json :: dataList[id=11209].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Karta Tożsamości — nazwa z tytułem] 그레고르
   źródło: Personalities.json :: dataList[id=11209].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Karta Tożsamości — opis] 그레고르의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=11209].desc
   limit: do 120 znaków
   EN: Gregor's 9th Identity
   PL:
633. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 세이버 슬래시
   źródło: Skills_personality-12.json :: dataList[id=1120901].levelList[level=1].name ; dataList[id=1120901].levelList[level=2].name ; dataList[id=1120901].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Sabre Slash
   PL:
634. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_personality-12.json :: dataList[id=1120901].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1120901].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1120901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL:
635. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상의 [Sinking]이 6 이상이면 코인 위력 +2
   źródło: Skills_personality-12.json :: dataList[id=1120901].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 6+ [Sinking], Coin Power +2
   PL:
636. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking] 3 당 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [Sinking] 횟수 3 당, 합 위력 +1 (최대 2)
   źródło: Skills_personality-12.json :: dataList[id=1120901].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Coin Power +1 for every 3 [Sinking] on target (max 2)\n[WhenUse] Clash Power +1 for every 3 [Sinking] Count on target (max 2)
   PL:
637. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 르미즈
   źródło: Skills_personality-12.json :: dataList[id=1120902].levelList[level=1].name ; dataList[id=1120902].levelList[level=2].name ; dataList[id=1120902].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Remise
   PL:
638. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] [Sinking] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1120902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Sinking]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Sinking] = 침잠 / Sinking
   EN: [WinDuel] Inflict +1 [Sinking] Count
   PL:
639. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]이 5 이상이면, 다음 턴에 [Agility] 1 얻음
   źródło: Skills_personality-12.json :: dataList[id=1120902].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1120902].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1120902].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] If target has 5+ [Sinking], gain 1 [Agility] next turn
   PL:
640. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-12.json :: dataList[id=1120902].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1120902].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1120902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
641. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상의 [Sinking] 횟수 3 당, 합 위력 +1 (최대 2)\n[WinDuel] [Sinking] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1120902].levelList[level=2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Clash Power +1 for every 3 [Sinking] Count on target (max 2)\n[WinDuel] Inflict +1 [Sinking] Count
   PL:
642. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking]이 6 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Sinking] 횟수 3 당, 합 위력 +1 (최대 2)\n[WinDuel] [Sinking] 횟수 2 증가
   źródło: Skills_personality-12.json :: dataList[id=1120902].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has 6+ [Sinking], Coin Power +1\n[WhenUse] Clash Power +1 for every 3 [Sinking] Count on target (max 2)\n[WinDuel] Inflict +2 [Sinking] Count
   PL:
643. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 악몽 사냥
   źródło: Skills_personality-12.json :: dataList[id=1120903].levelList[level=3].name ; dataList[id=1120903].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Nightmare Hunt
   PL:
644. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 [Sinking] 횟수 3 당 합 위력 +1 (최대 2)\n[EndSkill] 대상이 흐트러짐 상태면, [Sinking] 횟수 3 증가\n[EndSkill] 대상이 사망했으면, 무작위 적 1명의 [Sinking] 횟수 3 증가
   źródło: Skills_personality-12.json :: dataList[id=1120903].levelList[level=3].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Clash Power +1 for every 3 [Sinking] Count on target (max 2)\n[EndSkill] If target is Staggered, inflict +3 [Sinking] Count\n[EndSkill] If target is defeated, inflict +3 [Sinking] Count on 1 random enemy
   PL:
645. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120903].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1120903].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL:
646. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120903].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1120903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 645 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1120903].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1120903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 645 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]을 10 흡수하여 다음 턴에 [PlusCoinValueUp] 1, [AttackDmgUp] 1 얻음. 50% 확률로 [Sinking]을 흡수하지 않고 위 효과 발동
   źródło: Skills_personality-12.json :: dataList[id=1120903].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [PlusCoinValueUp], [AttackDmgUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [OnSucceedAttack] Absorb 10 [Sinking] from the target and gain 1 [PlusCoinValueUp] and 1 [AttackDmgUp] next turn. 50% chance to gain the above effects without absorbing [Sinking]
   PL:
649. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking] 횟수 3 당 합 위력 +1 (최대 3)\n[EndSkill] 대상이 흐트러짐 상태면, [Sinking] 횟수 3 증가\n[EndSkill] 대상이 사망했으면, 무작위 적 2명의 [Sinking] 횟수 3 증가
   źródło: Skills_personality-12.json :: dataList[id=1120903].levelList[level=4].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Clash Power +1 for every 3 [Sinking] Count on target (max 3)\n[EndSkill] If target is Staggered, inflict +3 [Sinking] Count\n[EndSkill] If target is defeated, inflict +3 [Sinking] Count on 2 random enemies
   PL:
650. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]을 10 흡수하여 다음 턴에 [PlusCoinValueUp] 1, [AttackDmgUp] 3 얻음. 50% 확률로 [Sinking]을 흡수하지 않고 위 효과 발동
   źródło: Skills_personality-12.json :: dataList[id=1120903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [PlusCoinValueUp], [AttackDmgUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [OnSucceedAttack] Absorb 10 [Sinking] from the target and gain 1 [PlusCoinValueUp] and 3 [AttackDmgUp] next turn. 50% chance to gain the above effects without absorbing [Sinking]
   PL:
651. [Obrona (ulepszenia 1,4) — nazwa] 네놈도 울고싶나?
   źródło: Skills_personality-12.json :: dataList[id=1120904].levelList[level=1].name ; dataList[id=1120904].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Do You Wish to Weep?
   PL:
652. [Obrona (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking]이 5 이상이면, 코인 위력 +1
   źródło: Skills_personality-12.json :: dataList[id=1120904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 5+ [Sinking], Coin Power +1
   PL:
653. [Obrona (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking] 3 당, 코인 위력 +1  (최대 3)
   źródło: Skills_personality-12.json :: dataList[id=1120904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Coin Power +1 for every 3 [Sinking] on target (max 3)
   PL:
654. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — nazwa] 끝 없는 악몽
   źródło: Passives.json :: dataList[id=1120901].name
   limit: do 40 znaków
   EN: Endless Nightmares
   PL:
655. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — opis] - 전투 시작 시 이전 턴 시작 시와의 정신력 차이 5 당 [AttackDmgUp] 1, [Vulnerable] 1 얻음 (최대 3)\n- 대상의 [Sinking] 위력 1 당 피해량 +1% (최대 20%)
   źródło: Passives.json :: dataList[id=1120901].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDmgUp], [Vulnerable], [Sinking]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile; [Sinking] = 침잠 / Sinking
   EN: - Combat Start: Gain 1 [AttackDmgUp] and 1 [Vulnerable] for every 5 SP difference between Combat Start and the last Turn Start (max 3)\n- Deal +1% damage for every [Sinking] Potency on target (max 20%)
   PL:
656. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — nazwa] 끝 없는 악몽
   źródło: Passives.json :: dataList[id=1120911].name
   (powtórzenie elementu 654 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — opis] - 전투 시작 시 이전 턴 시작 시와의 정신력 차이 5 당 [AttackDmgUp] 1, [Vulnerable] 1 얻음 (최대 5)\n- 대상의 [Sinking] 위력 1 당 피해량 +2% (최대 40%)
   źródło: Passives.json :: dataList[id=1120911].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDmgUp], [Vulnerable], [Sinking]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile; [Sinking] = 침잠 / Sinking
   EN: - Combat Start: Gain 1 [AttackDmgUp] and 1 [Vulnerable] for every 5 SP difference between Combat Start and the last Turn Start (max 5)\n- Deal +2% damage for every [Sinking] Potency on target (max 40%)
   PL:
658. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Gloom) — nazwa] 시달림
   źródło: Passives.json :: dataList[id=1120921].name
   limit: do 40 znaków
   EN: Suffering
   PL:
659. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Gloom) — opis] 전투 시작 시 정신력이 가장 낮은 아군 1명의 정신력이 7 감소하고, [AzureDamageUp] 1 얻음
   źródło: Passives.json :: dataList[id=1120921].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AzureDamageUp]
   znaczenie tagów: [AzureDamageUp] = 우울 피해량 증가 / Gloom DMG Up
   EN: Combat Start: 1 ally with the least SP loses 7 SP, then gains 1 [AzureDamageUp]
   PL:
660. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Gloom) — nazwa] 시달림
   źródło: Passives.json :: dataList[id=1120931].name
   (powtórzenie elementu 658 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Gloom) — opis] 전투 시작 시 정신력이 가장 낮은 아군 1명의 정신력이 5 감소하고, [AzureDamageUp] 1 얻음
   źródło: Passives.json :: dataList[id=1120931].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AzureDamageUp]
   znaczenie tagów: [AzureDamageUp] = 우울 피해량 증가 / Gloom DMG Up
   EN: Combat Start: 1 ally with the least SP loses 5 SP, then gains 1 [AzureDamageUp]
   PL:
662. [Kwestia głosowa [get_11209_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=get_11209_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Kwestia głosowa [get_11209_1] (Identity Acquisition)] 너도 그놈을 잡으러 온 건가? 아니면 그저… 이 몰락을 구경하려고 온 건가.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=get_11209_1].dlg
   limit: do 150 znaków
   EN: Are you here to join the hunt for that bastard as well? Or are you merely here to... take in this desolation?
   PL:
664. [Kwestia głosowa [lobby_morning_11209_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=lobby_morning_11209_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Kwestia głosowa [lobby_morning_11209_1] (Morning Greeting)] 혹시, 창문 좀 닫아주겠나? 찬바람 하나로도 밤새 기침을 토하는 몸으로 태어나서 말이야.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=lobby_morning_11209_1].dlg
   limit: do 170 znaków
   EN: Close the window, will you? I had the misfortune of being born in a body that goes into coughing fits at the slightest breeze.
   PL:
666. [Kwestia głosowa [lobby_noon_11209_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=lobby_noon_11209_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Kwestia głosowa [lobby_noon_11209_1] (Afternoon Greeting)] 이곳에서 햇빛 따위를 기대하진 마. 구름이 갤 일은 없을 거야. 평화가 깃들 날은 영영 오지 않는 것처럼.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=lobby_noon_11209_1].dlg
   limit: do 210 znaków
   EN: Don't expect to see the sun anytime soon as long as you are here. It hides forevermore beyond the overcast sky. It is as distant as the notion of peace is to us.
   PL:
668. [Kwestia głosowa [lobby_night_11209_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=lobby_night_11209_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Kwestia głosowa [lobby_night_11209_1] (Evening Greeting)] 잠이 겨우 들었다가도 폭풍 소리에 깨어나곤 해. 혹시 모르지, 내가 잊어버린 악몽들이 두들기는 소리일지도.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=lobby_night_11209_1].dlg
   limit: do 180 znaków
   EN: The rushing gale wakes me from my already shallow sleep. Perhaps my nightmares have returned from oblivion to rap at my windows again.
   PL:
670. [Kwestia głosowa [smalltalk_11209_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=smalltalk_11209_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Kwestia głosowa [smalltalk_11209_1] (Chatter #1)] 아, 자네였나. 달갑지 않은 손님이 방문할 때가 있거든. 지금은 어쩔 수 없이 등을 맡겨야 하지만 언제든 다시 서로를 찌를 수 있는 놈과 잠시 협정을 맺었지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=smalltalk_11209_1].dlg
   limit: do 250 znaków
   EN: Ah, it's you. A... rather disagreeable guest visits me from time to time. Though I have made an alliance with him as I had no alternative... I know that he is always ready to stab me in the back.
   PL:
672. [Kwestia głosowa [smalltalk_11209_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=smalltalk_11209_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Kwestia głosowa [smalltalk_11209_2] (Chatter #2)] 검이 예리할수록 정신도 또렷해진다는 말 따윈 믿지 않아. 비싼 값을 치른 내 검은 무엇보다 예리해. 하지만… 난 밤마다 깨서 이 모든 게 악몽에 불과하진 않았는지… 끊임없이 의심해야 하니.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=smalltalk_11209_2].dlg
   limit: do 370 znaków
   EN: A sharper blade leads to a sharper mind? It's a load of crap. My blade is sharper than anything... because I paid good money for it. But... every night... every time I stir awake, I am trapped in a world of endless doubt... wondering if all this had been nothing but a terrible nightmare.
   PL:
674. [Kwestia głosowa [smalltalk_11209_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=smalltalk_11209_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Kwestia głosowa [smalltalk_11209_3] (Chatter #3)] 그 저택을 본 적이 있나?  폭풍과 벼락만이 유일한 손님이 된 그 곳 말이야. 절망만을 안겨주지만, 아이러니하게 그게 내가 계속 버틸 수 있게 만드는 이유가 되더군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=smalltalk_11209_3].dlg
   limit: do 240 znaków
   EN: Have you seen that manor yourself? That desolate place visited only by the wuthering winds and lightning. It inspires nothing but despair... which is, ironically, what keeps me going.
   PL:
676. [Kwestia głosowa [smalltalk_11209_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=smalltalk_11209_4].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Kwestia głosowa [smalltalk_11209_4] (Post-Uptie Chat 1)] 가끔씩 이름 없는 비석을 볼 때마다 심장이 터질 것 같이 요동칠 때가 있는데, 이유가 뭔지 짐작 간다면 알려줄 수 있겠나?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=smalltalk_11209_4].dlg
   limit: do 180 znaków
   EN: Sometimes, when I see a gravestone without a name... my heart begins racing like it's about to explode. Now... do you know why that may be?
   PL:
678. [Kwestia głosowa [smalltalk_11209_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=smalltalk_11209_5].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Kwestia głosowa [smalltalk_11209_5] (Post-Uptie Chat 2)] 한 쪽 팔만 보란 듯이 남겨뒀어. 일부러 놓아준 거지. 내게 일컫길, 어렸을 때 못다 한 술래잡기를 하자더군. 누가 잡힐지는 곧 알게 되겠지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=smalltalk_11209_5].dlg
   limit: do 280 znaków
   EN: That bastard deliberately cut off only one of my arms. I didn't escape; I was let go. He tells me that we should partake in a game of hide-and-seek that we could not as children. We will see who hunts who in the end.
   PL:
680. [Kwestia głosowa [neglect_11209_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=neglect_11209_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Kwestia głosowa [neglect_11209_1] (Idle)] 괜찮아, 잊히는 거엔 익숙하니까.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=neglect_11209_1].dlg
   limit: do 120 znaków
   EN: Don't worry. I'm used to being forgotten.
   PL:
682. [Kwestia głosowa [gacksung_11209_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=gacksung_11209_1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Kwestia głosowa [gacksung_11209_1] (Uptying)] 그래, 칼날을 한 번 갈아줄 때도 되었지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=gacksung_11209_1].dlg
   limit: do 120 znaków
   EN: Yes... it's about time I sharpened the blade of my sword.
   PL:
684. [Kwestia głosowa [formation_11209_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=formation_11209_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Kwestia głosowa [formation_11209_1] (Deployment)] 사냥감을 찾은 건가.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=formation_11209_1].dlg
   limit: do 120 znaków
   EN: Have we found our prey?
   PL:
686. [Kwestia głosowa [battleentry_11209_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battleentry_11209_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Kwestia głosowa [battleentry_11209_1] (Stage Entry)] 애도의 시간이군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battleentry_11209_1].dlg
   limit: do 120 znaków
   EN: This is the time for lamentation.
   PL:
688. [Kwestia głosowa [battle_select_11209_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_select_11209_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Kwestia głosowa [battle_select_11209_1] (Viewed in Battle)] 내게 남길 말이 있나.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_select_11209_1].dlg
   limit: do 120 znaków
   EN: Have you something to say to me?
   PL:
690. [Kwestia głosowa [battle_endcommand_11209_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_endcommand_11209_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Kwestia głosowa [battle_endcommand_11209_1] (Commencing Attack)] 검날을 네게 바쳐주지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_endcommand_11209_1].dlg
   limit: do 120 znaków
   EN: I dedicate this blade to you.
   PL:
692. [Kwestia głosowa [battle_enemy_break_11209_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_enemy_break_11209_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Kwestia głosowa [battle_enemy_break_11209_1] (Enemy Stagger)] 이 전투에 명예 따윌 기대하고 있는 건 아니겠지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_enemy_break_11209_1].dlg
   limit: do 120 znaków
   EN: I hope you weren't expecting to find honor in this battle.
   PL:
694. [Kwestia głosowa [battle_break_11209_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_break_11209_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Kwestia głosowa [battle_break_11209_1] (Staggered)] 아니…고작 여기서 쓰러진다면 그놈이 날 얼마나 비웃겠나.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_break_11209_1].dlg
   limit: do 120 znaków
   EN: If I were to fall here... he would... mock me so savagely.
   PL:
696. [Kwestia głosowa [battle_kill_11209_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_kill_11209_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Kwestia głosowa [battle_kill_11209_1] (Enemy Killed)] 이제 고작 하나를 찔렀을 뿐…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_kill_11209_1].dlg
   limit: do 120 znaków
   EN: I have struck but one of your vital points...
   PL:
698. [Kwestia głosowa [battle_dead_11209_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_dead_11209_1].desc
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Kwestia głosowa [battle_dead_11209_1] (Death)] 드디어… 안개가 걷히고 꿈속에서만 그리워하던 그 사람을 볼 수 있는 건가…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_dead_11209_1].dlg
   limit: do 130 znaków
   EN: Ah, the mist fades... I can finally see the face of the one I so longed to see in my dreams...
   PL:
700. [Kwestia głosowa [choice_success_p_11209_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=choice_success_p_11209_2].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Kwestia głosowa [choice_success_p_11209_2] (Check Passed)] 지금까지 베어왔던 것들과 비교하면… 쉬웠어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=choice_success_p_11209_2].dlg
   limit: do 120 znaków
   EN: Compared to what I have cut down in my path, this was... easy.
   PL:
702. [Kwestia głosowa [choice_fail_n_11209_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=choice_fail_n_11209_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Kwestia głosowa [choice_fail_n_11209_1] (Check Failed)] 미처 눈치채지 못했군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=choice_fail_n_11209_1].dlg
   limit: do 120 znaków
   EN: It slipped my sight.
   PL:
704. [Kwestia głosowa [battle_clear_11209_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_clear_11209_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Kwestia głosowa [battle_clear_11209_1] (Victory Cry)] 최후의 결투는 아직 멀었어. 축배를 들 여유는 없지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_clear_11209_1].dlg
   limit: do 120 znaków
   EN: The final battle lies beyond still. There is hardly any time to celebrate.
   PL:
706. [Kwestia głosowa [battle_clear_ex_11209_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_clear_ex_11209_1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Kwestia głosowa [battle_clear_ex_11209_1] (Extra Conditions Fulfilled)] 이 칼날이 마침내 그놈의 검은 심장에도 박히게 된다면 좋겠어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_clear_ex_11209_1].dlg
   limit: do 120 znaków
   EN: Let this blade find its way into his black heart.
   PL:
708. [Kwestia głosowa [battle_defeat_11209_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_defeat_11209_1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Kwestia głosowa [battle_defeat_11209_1] (Defeat Wail)] 아직은 때가 아니었던 거지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Linton_11209.json :: dataList[id=battle_defeat_11209_1].dlg
   limit: do 120 znaków
   EN: It was simply not the time.
   PL:

## [000] The Priest of La Manchaland — Gregor — 라만차랜드 신부
- ID Tożsamości: `11210` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 108 · szybkość: 3–5 / 3–5 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Bleed, Rupture

710. [Karta Tożsamości — tytuł] 라만차랜드\n신부
   źródło: Personalities.json :: dataList[id=11210].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Priest\nof La Manchaland
   PL:
711. [Karta Tożsamości — nazwa] 그레고르
   źródło: Personalities.json :: dataList[id=11210].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Karta Tożsamości — nazwa z tytułem] 그레고르
   źródło: Personalities.json :: dataList[id=11210].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Karta Tożsamości — opis] 그레고르의 열번째 인격
   źródło: Personalities.json :: dataList[id=11210].desc
   limit: do 120 znaków
   EN: Gregor’s 10th Identity
   PL:
714. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 가족을 위한 헌신
   źródło: Skills_personality-12.json :: dataList[id=1121001].levelList[level=1].name ; dataList[id=1121001].levelList[level=2].name ; dataList[id=1121001].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Sacrifice for the Family
   PL:
715. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n[WhenUse] [Laceration] 10 얻음\n- 자신의 체력이 50% 이상이면, [Laceration] 15 추가로 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121001].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 10 [Laceration]\n- At 50%+ HP, gain +15 additional [Laceration]
   PL:
716. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
717. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
718. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloodyHandGregFirst] 1 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121001].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloodyHandGregFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodyHandGregFirst] = 피로 물든 손 / Bloodied Hand
   EN: [OnSucceedAttack] Gain 1 [BloodyHandGregFirst]
   PL:
719. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n<style="highlight">[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] [Laceration] 10 얻음\n- 자신의 체력이 50% 이상이면, [Laceration] 15 추가로 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121001].levelList[level=2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>\n[WhenUse] Gain 10 [Laceration]\n- At 50%+ HP, gain 15 additional [Laceration]
   PL:
720. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121001].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]<style="highlight"></style>
   PL:
721. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121001].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1121001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]<style="highlight"></style>
   PL:
722. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloodyHandGregFirst] <style="highlight">2</style> 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121001].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BloodyHandGregFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodyHandGregFirst] = 피로 물든 손 / Bloodied Hand
   EN: [OnSucceedAttack] Gain <style="highlight">2</style> [BloodyHandGregFirst]
   PL:
723. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n<style="highlight">[WhenUse] 대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] [Laceration] 10 얻음\n- 자신의 체력이 50% 이상이면, [Laceration] 15 추가로 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121001].levelList[level=4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n<style="highlight">[WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[WhenUse] Gain 10 [Laceration]\n- At 50%+ HP, gain 15 additional [Laceration]
   PL:
724. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-12.json :: dataList[id=1121001].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Laceration]
   PL:
725. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloodyHandGregFirst] <style="highlight">3</style> 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121001].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BloodyHandGregFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodyHandGregFirst] = 피로 물든 손 / Bloodied Hand
   EN: [OnSucceedAttack] Gain <style="highlight">3</style> [BloodyHandGregFirst]
   PL:
726. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 죄어드는 죄악감
   źródło: Skills_personality-12.json :: dataList[id=1121002].levelList[level=1].name ; dataList[id=1121002].levelList[level=2].name ; dataList[id=1121002].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Suffocating Guilt
   PL:
727. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n[WhenUse] [Laceration] 10 얻음\n[WhenUse] 자신의 [WornHeartGreg]이 5 이상이면, [BloodDinner]을 최대 60 소모하여, 소모한 [BloodDinner] 6당 [BloodyHandGregFirst] 1 얻음\n- [WornHeartGreg]이 5 미만이면, [Laceration] 10과 [BloodyHandGregFirst] 2 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121002].levelList[level=1].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Laceration], [WornHeartGreg], [BloodDinner], [BloodyHandGregFirst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Laceration] = 출혈 / Bleed; [WornHeartGreg] = 닳아버린 마음 / Ailing Heart; [BloodDinner] = 혈찬 / Bloodfeast; [BloodyHandGregFirst] = 피로 물든 손 / Bloodied Hand
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 10 [Laceration]\n[WhenUse] At 5+ [WornHeartGreg], consume up to 60 [BloodDinner]; then, gain 1 [BloodyHandGregFirst] for every 6 [BloodDinner] consumed\n- At less than 5 [WornHeartGreg], gain 10 [Laceration] and 2 [BloodyHandGregFirst]
   PL:
728. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 555 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloodyHandGregFirst] 1 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 718 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n<style="highlight">[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] [Laceration] 10 얻음\n[WhenUse] 자신의 [WornHeartGreg]이 5 이상이면, [BloodDinner]을 최대 60 소모하여, 소모한 [BloodDinner] 6당 [BloodyHandGregFirst] 1 얻음\n- [WornHeartGreg]이 5 미만이면, [Laceration] 10과 [BloodyHandGregFirst] 2 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121002].levelList[level=2].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Laceration], [WornHeartGreg], [BloodDinner], [BloodyHandGregFirst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Laceration] = 출혈 / Bleed; [WornHeartGreg] = 닳아버린 마음 / Ailing Heart; [BloodDinner] = 혈찬 / Bloodfeast; [BloodyHandGregFirst] = 피로 물든 손 / Bloodied Hand
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>\n[WhenUse] Gain 10 [Laceration]\n[WhenUse] At 5+ [WornHeartGreg], consume up to 60 [BloodDinner]; then, gain 1 [BloodyHandGregFirst] for every 6 [BloodDinner] consumed\n- At less than 5 [WornHeartGreg], gain 10 [Laceration] and 2 [BloodyHandGregFirst]
   PL:
732. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-12.json :: dataList[id=1121002].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Laceration] Count
   PL:
733. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121002].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1121002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloodyHandGregFirst] <style="highlight">2</style> 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121002].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n<style="highlight">[WhenUse] 대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] [Laceration] 10 얻음\n[WhenUse] 자신의 [WornHeartGreg]이 5 이상이면, [BloodDinner]을 최대 60 소모하여, 소모한 [BloodDinner] 6당 [BloodyHandGregFirst] 1 얻음\n- [WornHeartGreg]이 5 미만이면, [Laceration] 10과 [BloodyHandGregFirst] <style="highlight">3</style> 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121002].levelList[level=4].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Laceration], [WornHeartGreg], [BloodDinner], [BloodyHandGregFirst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Laceration] = 출혈 / Bleed; [WornHeartGreg] = 닳아버린 마음 / Ailing Heart; [BloodDinner] = 혈찬 / Bloodfeast; [BloodyHandGregFirst] = 피로 물든 손 / Bloodied Hand
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n<style="highlight">[WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[WhenUse] Gain 10 [Laceration]\n[WhenUse] At 5+ [WornHeartGreg], consume up to 60 [BloodDinner]; then, gain 1 [BloodyHandGregFirst] for every 6 [BloodDinner] consumed\n- At less than 5 [WornHeartGreg], gain 10 [Laceration] and <style="highlight">3</style> [BloodyHandGregFirst]
   PL:
736. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count<style="highlight"></style>
   PL:
737. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloodyHandGregFirst] <style="highlight">3</style> 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121002].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 씻을 수 없는 죄
   źródło: Skills_personality-12.json :: dataList[id=1121003].levelList[level=3].name ; dataList[id=1121003].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: The Unforgivable Sin
   PL:
739. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (스킬당 최대 100)\n[WhenUse] 자신의 잃은 체력 1%당 피해량 + 1% (최대 60%)\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WhenUse] [BloodyHandGregFirst]을 10을 초과하는 만큼 소모하여 아래 효과를 얻음\n- (소모한 수치 x 3)만큼 자신의 체력을 회복\n- 소모한 수치가 10 이상이면, 코인 위력 +1\n[WhenUse] [Laceration] 10 얻음\n[EndSkill] 최대 체력의 10%만큼 체력 회복
   źródło: Skills_personality-12.json :: dataList[id=1121003].levelList[level=3].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BloodyHandGregFirst], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodyHandGregFirst] = 피로 물든 손 / Bloodied Hand; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: heal 50% of the HP damage dealt (max 100 per Skill)\n[WhenUse] Deal +1% damage for every 1% missing HP on self (max 60%)\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[WhenUse] Consume every excess Stack of [BloodyHandGregFirst] past 10 Stack to gain the following effects:\n- Heal (Stacks consumed x 3) HP on self\n- If this unit consumed 10+ Stack, Coin Power +1\n[WhenUse] Gain 10 [Laceration]\n[EndSkill] Heal 10% HP on self
   PL:
740. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [BloodyHandGregFirst] 2 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121003].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloodyHandGregFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodyHandGregFirst] = 피로 물든 손 / Bloodied Hand
   EN: [OnSucceedAttack] Gain 2 [BloodyHandGregFirst]
   PL:
741. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121003].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 555 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121003].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL:
743. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121003].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 716 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121003].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (스킬당 최대 100)\n[WhenUse] 자신의 잃은 체력 1%당 피해량 <style="highlight">+ 1.5% (최대 90%)</style>\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WhenUse] [BloodyHandGregFirst]을 10을 초과하는 만큼 소모하여 아래 효과를 얻음\n- (소모한 수치 x 3)만큼 자신의 체력을 회복\n- 소모한 수치가 10 이상이면, 코인 위력 +1\n<style="highlight">- 소모한 수치가 20이면, 이 스킬의 마지막 코인 재사용</style>\n[WhenUse] [Laceration] 10 얻음\n[EndSkill] 최대 체력의 10%만큼 체력 회복
   źródło: Skills_personality-12.json :: dataList[id=1121003].levelList[level=4].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [BloodyHandGregFirst], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodyHandGregFirst] = 피로 물든 손 / Bloodied Hand; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: heal 50% of the HP damage dealt (max 100 per Skill)\n[WhenUse] Deal <style="highlight">+1.5%</style> damage for every 1% missing HP on self <style="highlight">(max 90%)</style>\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[WhenUse] Consume every excess Stack of [BloodyHandGregFirst] past 10 Stack to gain the following effects:\n- Heal (Stacks consumed x 3) HP on self\n- If this unit consumed 10+ Stack, Coin Power +1\n<style="highlight">- If this unit consumed 20 Stack, Reuse the final Coin</style>\n[WhenUse] Gain 10 [Laceration]\n[EndSkill] Heal 10% HP on self
   PL:
746. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [BloodyHandGregFirst] <style="highlight">3</style> 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-12.json :: dataList[id=1121003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 732 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
748. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-12.json :: dataList[id=1121003].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Burst] Count
   PL:
749. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-12.json :: dataList[id=1121003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 724 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-12.json :: dataList[id=1121003].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Burst]
   PL:
751. [Obrona (ulepszenia 1,4) — nazwa] 빛바랜 인내
   źródło: Skills_personality-12.json :: dataList[id=1121004].levelList[level=1].name ; dataList[id=1121004].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Faded Patience
   PL:
752. [Obrona (ulepszenie 1) — opis] [StartBattle] [WornHeartGreg] 3 얻음 (턴 당 1회)
   źródło: Skills_personality-12.json :: dataList[id=1121004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [WornHeartGreg]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WornHeartGreg] = 닳아버린 마음 / Ailing Heart
   EN: [StartBattle] Gain 3 [WornHeartGreg] (once per turn)
   PL:
753. [Obrona (ulepszenie 4) — opis] <style="highlight">[StartBattle] 자신의 현재 체력이 최대 체력의 40% 이상이면, [Laceration] 5 얻고 자신의 [Laceration] 최대 3회 발동 (턴 당 1회. 발동된 횟수만큼 [Laceration] 횟수 감소)\n[StartBattle] 자신의 현재 체력이 최대 체력의 40% 미만이면, [BloodDinner]을 최대 20 소모하여, 소모한 [BloodDinner]만큼 자신의 체력 회복 (턴 당 1회)</style>\n[StartBattle] [WornHeartGreg] 3 얻음 (턴 당 1회)
   źródło: Skills_personality-12.json :: dataList[id=1121004].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [Laceration], [BloodDinner], [WornHeartGreg]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [WornHeartGreg] = 닳아버린 마음 / Ailing Heart
   EN: <style="highlight">[StartBattle] At 40%+ HP, gain 5 [Laceration] and activate [Laceration] up to 3 times on self (once per turn; lose [Laceration] Count equal to the number of times it was activated)\n[StartBattle] At less than 40% HP, consume up to 20 [BloodDinner] and heal the same value as HP (once per turn)</style>\n[StartBattle] Gain 3 [WornHeartGreg] (once per turn)
   PL:
754. [Pasywka bojowa (od ulepszenia 1) — nazwa] 혈찬
   źródło: Passives.json :: dataList[id=1121002].name
   limit: do 40 znaków
   EN: Bloodfeast
   PL:
755. [Pasywka bojowa (od ulepszenia 1) — opis] 이 캐릭터가 전투에 등장해 있거나, 등장할 리스트에 포함되어 있으면, 1턴부터 모든 캐릭터가 받은 [Laceration] 피해만큼 [BloodDinner]이 증가함.\n이 캐릭터가 전투에 등장할 때 전장에 흩뿌려진 잠재된 피가 더욱 드러난다.
   źródło: Passives.json :: dataList[id=1121002].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: If this unit is on field, or is one of the units that can appear on this Stage, increase [BloodDinner] value by the amount of [Laceration] damage collectively received by every unit. \nWhen this unit enters the field, the sleeping blood drenching the battlefield will rise above the surface.
   PL:
756. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Lust) — nazwa] 자멸적 헌신
   źródło: Passives.json :: dataList[id=1121001].name
   limit: do 40 znaków
   EN: Self-destructive Dedication
   PL:
757. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Lust) — opis] 턴 종료시, 가장 정신력이 낮은 아군의 정신력을 (10 - 자신의 [WornHeartGreg])/2 만큼 회복시킴 (자신 또는 패닉, E.G.O 침식 상태인 아군 제외. 소수점 버림)\n이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고, 해당 턴 동안 체력이 1로 유지됨. (전투 당 1회)
   źródło: Passives.json :: dataList[id=1121001].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [WornHeartGreg]
   znaczenie tagów: [WornHeartGreg] = 닳아버린 마음 / Ailing Heart
   EN: Turn End: heal ((10 - [WornHeartGreg])/2) SP for the ally with the least SP (excluding: self or allies that are Panicked or Corroded; rounded down)\nIn this Encounter, when this unit takes damage that brings their HP down to 0, nullify that damage; then, this unit's HP cannot drop below 1 for the turn. (once per Encounter)
   PL:
758. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Lust) — nazwa] 자멸적 헌신
   źródło: Passives.json :: dataList[id=1121011].name
   (powtórzenie elementu 756 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Lust) — opis] 턴 종료시, 가장 정신력이 낮은 아군의 정신력을 (10 - 자신의 [WornHeartGreg]) 만큼 회복시킴 (자신 또는 패닉, E.G.O 침식 상태인 아군 제외)\n이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고, 해당 턴 동안 체력이 1로 유지됨. (전투 당 1회)
   źródło: Passives.json :: dataList[id=1121011].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [WornHeartGreg]
   znaczenie tagów: [WornHeartGreg] = 닳아버린 마음 / Ailing Heart
   EN: Turn End: heal (10 - [WornHeartGreg]) SP for the ally with the least SP (excluding: self or allies that are Panicked or Corroded)\nIn this Encounter, when this unit takes damage that brings their HP down to 0, nullify that damage; then, this unit's HP cannot drop below 1 for the turn. (once per Encounter)
   PL:
760. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — nazwa] 돈키호테류 경혈 6식 채찍
   źródło: Passives.json :: dataList[id=1121021].name
   limit: do 50 znaków
   EN: Don Quixote Hardblood Arts 6: Whip
   PL:
761. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — opis] 현재 체력 비율이 가장 낮은 아군이 공격 적중 시 체력 3 회복 (턴 당 3회)
   źródło: Passives.json :: dataList[id=1121021].desc
   limit: do 120 znaków
   EN: 1 ally with the lowest HP percentage heals 3 HP On Hit (3 times per turn)
   PL:
762. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Lust) — nazwa] 돈키호테류 경혈 6식 채찍
   źródło: Passives.json :: dataList[id=1121031].name
   (powtórzenie elementu 760 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Lust) — opis] 현재 체력 비율이 가장 낮은 아군이 공격 적중 시 체력 3 회복 (턴 당 3회)\n- 피격 대상이 [Laceration]을 보유하고 있으면, 추가로 3 회복
   źródło: Passives.json :: dataList[id=1121031].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: 1 ally with the lowest HP percentage heals 3 HP On Hit (3 times per turn)\n- If the target hit by the said ally had [Laceration], heal 3 additional HP
   PL:
764. [Kwestia głosowa [get_11210_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=get_11210_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Kwestia głosowa [get_11210_1] (Identity Acquisition)] 내가 그들을 대신하여 용서하더라도… 어버이는 날 용서치 않으시겠지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=get_11210_1].dlg
   limit: do 150 znaków
   EN: Though I may forgive them in Father's stead... he will not find the same clemency within him for my absolution.
   PL:
766. [Kwestia głosowa [lobby_morning_11210_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=lobby_morning_11210_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Kwestia głosowa [lobby_morning_11210_1] (Morning Greeting)] 곧 라만차랜드의 개장시간이군. 오늘은… 몇 명의 가족들이 내게 찾아올까. 나는 몇 번의 괜찮다는 말을 반복하게 될까.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=lobby_morning_11210_1].dlg
   limit: do 220 znaków
   EN: La Manchaland opens soon. How... many of the Family will visit me today, I wonder. How many times will I be forced to tell them 'It's going to be okay' today, I wonder.
   PL:
768. [Kwestia głosowa [lobby_noon_11210_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=lobby_noon_11210_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Kwestia głosowa [lobby_noon_11210_1] (Afternoon Greeting)] 혈액바가 위대하다고 믿어 의심치 않던 시절도 있었지.\n그게 얼마나 헛된 믿음이었는지는, 이 흙뭉치 같은 걸 씹을 때마다 깨닫고 있어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=lobby_noon_11210_1].dlg
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There once was a time when I believed in the greatness of hemobars.\nEvery gnashing of my teeth against this brick reminds me of the foolishness behind that faith.
   PL:
770. [Kwestia głosowa [lobby_night_11210_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=lobby_night_11210_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Kwestia głosowa [lobby_night_11210_1] (Evening Greeting)] 내게 방문하는 형제들의 손을 본 적 있나? 하나같이 손톱이 빠져있지. 끝없이 바닥을 긁고 파헤쳐서… \n 언제나 해줄 수 있는 말은 똑같아. 그냥… 살아가라고. 인내해야 한다고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=lobby_night_11210_1].dlg
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Did you ever get a good look at the hands of the Brothers who visit me? Their hands, their fingernails are all torn and pulled from digging through the dirt...\nBut I only have one thing to tell them. That they have to just live on, no matter what. That we have to endure this hardship.
   PL:
772. [Kwestia głosowa [smalltalk_11210_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=smalltalk_11210_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Kwestia głosowa [smalltalk_11210_1] (Chatter #1)] 우리의 유일한 식사는 인간들이 내어주는 피. 아, 참으로 달콤하여라.\n가족의 행복은 영원히 이 바닥 아래에 묻혀진 채로…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=smalltalk_11210_1].dlg
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Our only sustenance is blood given to us by humans. Ah, how sweet it is.\nYet the happiness of the Family remains buried forever in these grounds...
   PL:
774. [Kwestia głosowa [smalltalk_11210_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=smalltalk_11210_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Kwestia głosowa [smalltalk_11210_2] (Chatter #2)] 어트랙션에서 인간을 상담해주면서 알게 된 점이 있지.\n가족들은 갈증에 미쳐버릴 것 같아 무엇으로 견딜 수 있는지만 끊임없이 묻는 반면… 그들의 고민은 정말… 다양하더군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=smalltalk_11210_2].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Here's something I learned while giving consultations to humans in my attraction.\nMy Family has but one desperate, endlessly repeating question—a wish, even—how can we withstand this thirst? But human concerns are so... varied.
   PL:
776. [Kwestia głosowa [smalltalk_11210_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=smalltalk_11210_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Kwestia głosowa [smalltalk_11210_3] (Chatter #3)] 이것도 견뎌야 해… 그냥 내게 벌을 내리는 거야. 모험을 떠난 어버이가 내리지 못하는 벌을.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=smalltalk_11210_3].dlg
   limit: do 190 znaków
   EN: This too, must be endured... This is a discipline for myself. The retribution Father would have given me... had he not left on his adventure.
   PL:
778. [Kwestia głosowa [smalltalk_11210_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=smalltalk_11210_4].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Kwestia głosowa [smalltalk_11210_4] (Post-Uptie Chat 1)] 갈증을 참거나, 잊고자 하는 그 어떤 방법도 소용 없다는 건 알고 있어. 다 해봤거든.\n하지만… 그런 상투적인 말을 빼면 난 무슨 말을 해줄 수 있지? 그런 방법을 알고 있다면… 제발 나도…! 나도 알고 싶다고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=smalltalk_11210_4].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I know. Any attempts to try to suppress this thirst, to forget it for even a second... it's all pointless. I've tried them all myself.\nBut... what else can I do but feed them these... stock phrases? If you know anything else I can tell them, please... I...! I want to know, too.
   PL:
780. [Kwestia głosowa [smalltalk_11210_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=smalltalk_11210_5].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Kwestia głosowa [smalltalk_11210_5] (Post-Uptie Chat 2)] 피를 마시고 싶어… 안 돼. 떠올리지 마. 아, 어버이는 어디까지 오셨을까, 그 머리에 씌운다는 유물을 마침내 발견하셨을까?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=smalltalk_11210_5].dlg
   limit: do 160 znaków
   EN: I want... blood... no. Don't even think about it. Ah... where is Father now, I wonder? Did he find the helm, the Relic?
   PL:
782. [Kwestia głosowa [neglect_11210_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=neglect_11210_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Kwestia głosowa [neglect_11210_1] (Idle)] 오늘 피에 대한 생각을 해본 적이 있나? 있어. 그럼 어제는? 어제는 어땠지? 여전히 피가 생각 나나? 당연한 말을. 그렇다면 내일도 그럴 거라 확신해? 아니 그래선 안돼. 그런데 혈귀인 우리가 그럴 수 있는 존재였던가?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=neglect_11210_1].dlg
   limit: do 370 znaków
   EN: Did you think about blood today? I did. What about yesterday? Yeah, what about yesterday? Did you also think about blood? Of course I did. Then how about tomorrow? Will you think about blood tomorrow? Are you sure? No, we shouldn't. But can we not think about blood? We're Bloodfiends.
   PL:
784. [Kwestia głosowa [gacksung_11210_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=gacksung_11210_1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Kwestia głosowa [gacksung_11210_1] (Uptying)] 가면으로 수치를 가린다 하여도… 품었던 갈증은 여전히 나를 괴롭히는군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=gacksung_11210_1].dlg
   limit: do 120 znaków
   EN: Though this shame may be masked... the thirst underneath its surface won't leave me alone.
   PL:
786. [Kwestia głosowa [formation_11210_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=formation_11210_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Kwestia głosowa [formation_11210_1] (Deployment)] 원하신다면.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=formation_11210_1].dlg
   limit: do 120 znaków
   EN: If that is your wish.
   PL:
788. [Kwestia głosowa [battleentry_11210_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battleentry_11210_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Kwestia głosowa [battleentry_11210_1] (Stage Entry)] 오늘도 부디 정신을 유지할 수 있기를.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battleentry_11210_1].dlg
   limit: do 120 znaków
   EN: Let reason be with me today.
   PL:
790. [Kwestia głosowa [battle_select_11210_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_select_11210_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Kwestia głosowa [battle_select_11210_1] (Viewed in Battle)] 상담은 나중으로 하지… 지금은… 그럴 여유가 없군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_select_11210_1].dlg
   limit: do 120 znaków
   EN: Can you come back later for the consultation? I'm a bit... occupied at the moment.
   PL:
792. [Kwestia głosowa [battle_endcommand_11210_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_endcommand_11210_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Kwestia głosowa [battle_endcommand_11210_1] (Commencing Attack)] 그쪽도 죄인인가?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_endcommand_11210_1].dlg
   limit: do 120 znaków
   EN: Are you a sinner as well?
   PL:
794. [Kwestia głosowa [battle_enemy_break_11210_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_enemy_break_11210_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Kwestia głosowa [battle_enemy_break_11210_1] (Enemy Stagger)] 이 또한 용서할 테니…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_enemy_break_11210_1].dlg
   limit: do 120 znaków
   EN: This too shall be forgiven...
   PL:
796. [Kwestia głosowa [battle_break_11210_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_break_11210_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Kwestia głosowa [battle_break_11210_1] (Staggered)] 감내해야할 고통…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_break_11210_1].dlg
   limit: do 120 znaków
   EN: Pain... must be endured...
   PL:
798. [Kwestia głosowa [battle_kill_11210_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_kill_11210_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Kwestia głosowa [battle_kill_11210_1] (Enemy Killed)] …영원히 잠들어라.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_kill_11210_1].dlg
   limit: do 120 znaków
   EN: ... so rest now, forevermore.
   PL:
800. [Kwestia głosowa [battle_dead_11210_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_dead_11210_1].desc
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Kwestia głosowa [battle_dead_11210_1] (Death)] 허. 이제야… 굶주림에서…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_dead_11210_1].dlg
   limit: do 120 znaków
   EN: Hnh. Finally... freed from... the hunger...
   PL:
802. [Kwestia głosowa [choice_success_p_11210_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=choice_success_p_11210_2].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Kwestia głosowa [choice_success_p_11210_2] (Check Passed)] 고된 일이 있다면… 다음… 에도 찾아오라고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=choice_success_p_11210_2].dlg
   limit: do 130 znaków
   EN: I'm always here... for you. If something ails you... again, feel free to pay a visit any time.
   PL:
804. [Kwestia głosowa [choice_fail_n_11210_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=choice_fail_n_11210_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Kwestia głosowa [choice_fail_n_11210_1] (Check Failed)] 잠시… 시간이 필요해. 머릿속이 또 피에 대한 걸로 가득 차서…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=choice_fail_n_11210_1].dlg
   limit: do 120 znaków
   EN: I just... need some time. I can't think about anything other than... blood...
   PL:
806. [Kwestia głosowa [battle_clear_11210_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_clear_11210_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Kwestia głosowa [battle_clear_11210_1] (Victory Cry)] 잠깐의 목마름일 뿐이야. 승리에 취해 갈증을 채우는 일 따위가 일어나선 안 돼. 안 되고 말고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_clear_11210_1].dlg
   limit: do 150 znaków
   EN: This is just... a fleeting thirst. I shouldn't let this victory high compel me into quenching it. Of course not.
   PL:
808. [Kwestia głosowa [battle_clear_ex_11210_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_clear_ex_11210_1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Kwestia głosowa [battle_clear_ex_11210_1] (Extra Conditions Fulfilled)] 피가… 피가 잔뜩 흘러넘치고 있군… 한 모금, 아니 한 방울이라도 괜찮으니까 내게 줘! 어버이께서 용서치 않으신다해도!!
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_clear_ex_11210_1].dlg
   limit: do 210 znaków
   EN: Blood... there is... so much blood... overflowing... Give it to me! A sip— no, even a droplet of blood! Even if Father will never forgive me for it... I need this!!
   PL:
810. [Kwestia głosowa [battle_defeat_11210_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_defeat_11210_1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Kwestia głosowa [battle_defeat_11210_1] (Defeat Wail)] 어버이의 뜻을 거스르는 것도 모자라, 피를 탐하려했으니… 볼품없는 실패는 마땅한 결과 아니겠어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Bloodfiend_11210.json :: dataList[id=battle_defeat_11210_1].dlg
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Not only did I defy my Father... I sought blood...\nThis failure is the humiliation I deserve.
   PL:

## [000] Firefist Office Survivor — Gregor — 불주먹 사무소 생존자
- ID Tożsamości: `11211` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 82 · szybkość: 3–5 / 3–5 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Burn

812. [Karta Tożsamości — tytuł] 불주먹 사무소\n생존자
   źródło: Personalities.json :: dataList[id=11211].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Firefist Office\nSurvivor
   PL:
813. [Karta Tożsamości — nazwa] 그레고르
   źródło: Personalities.json :: dataList[id=11211].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Karta Tożsamości — nazwa z tytułem] 그레고르
   źródło: Personalities.json :: dataList[id=11211].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Karta Tożsamości — opis] 그레고르의 열한번째 인격
   źródło: Personalities.json :: dataList[id=11211].desc
   limit: do 120 znaków
   EN: Gregor’s 11th Identity
   PL:
816. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 화염방사
   źródło: Skills_personality-12.json :: dataList[id=1121101].levelList[level=1].name ; dataList[id=1121101].levelList[level=2].name ; dataList[id=1121101].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Flamethrow
   PL:
817. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 대상의 [Combustion]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-12.json :: dataList[id=1121101].levelList[level=1].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121101].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1121101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL:
819. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [FirePunchFuel]를 15 소모하여, [Combustion] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121101].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1121101].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FirePunchFuel], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Consume 15 [FirePunchFuel] and inflict +1 [Combustion] Count
   PL:
820. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Combustion]이 <style="highlight">3</style> 이상이면, 코인 위력 +1
   źródło: Skills_personality-12.json :: dataList[id=1121101].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has <style="highlight">3</style>+ [Combustion], Coin Power +1
   PL:
821. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 화상 <style="highlight">3 당</style>, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-12.json :: dataList[id=1121101].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">Coin Power +1 for every 3 Burn on target (max 2)</style>
   PL:
822. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_personality-12.json :: dataList[id=1121101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Combustion]
   PL:
823. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [FirePunchFuel]를 15 소모하여, [Combustion] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-12.json :: dataList[id=1121101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [FirePunchFuel], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Consume 15 [FirePunchFuel] and inflict +<style="highlight">2</style> [Combustion] Count
   PL:
824. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 더러운 피 한방울조차 남지 않게 전부 태워버리겠어
   źródło: Skills_personality-12.json :: dataList[id=1121102].levelList[level=1].name ; dataList[id=1121102].levelList[level=2].name ; dataList[id=1121102].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 2 (+6)
   limit: do 70 znaków
   EN: I'll burn away every last drop of your filthy blood
   PL:
825. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 대상의 [Combustion]이 6 이상이면, 코인 위력 +1\n[FirePunchFuelOverheated] 상태면, [FirePunchFuel]를 소모할 때 해당 코인의 피해량 +10%
   źródło: Skills_personality-12.json :: dataList[id=1121102].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [FirePunchFuelOverheated], [FirePunchFuel]
   znaczenie tagów: [Combustion] = 화상 / Burn; [FirePunchFuelOverheated] = 과열 연료 / Overheated Fuel; [FirePunchFuel] = 12구산 연료 / District 12 Fuel
   EN: If target has 6+ [Combustion], Coin Power +1\nWhen in [FirePunchFuelOverheated] state, deal +10% damage with Coins that consumed [FirePunchFuel]
   PL:
826. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-12.json :: dataList[id=1121102].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1121102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1121102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL:
827. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [FirePunchFuel]를 10 소모하여, [Combustion] 위력이 가장 낮은 적 2명에게 [Combustion] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FirePunchFuel], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Consume 10 [FirePunchFuel] and inflict 1 [Combustion] against 2 enemies that have the least [Combustion] Potency
   PL:
828. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121102].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1121102].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count
   PL:
829. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [FirePunchFuel]를 10 소모하여, [Combustion] 횟수가 가장 낮은 적 1명에게 [Combustion] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FirePunchFuel], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Consume 10 [FirePunchFuel] and inflict +1 [Combustion] Count against 1 enemy that has the least [Combustion] Count
   PL:
830. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Combustion]이 6 이상이면, 코인 위력 +1\n[FirePunchFuel]를 소모할 때 해당 코인의 피해량 +10%\n<style="highlight">- [FirePunchFuelOverheated] 상태면, 대신 피해량 +20%로 적용</style>
   źródło: Skills_personality-12.json :: dataList[id=1121102].levelList[level=2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [FirePunchFuel], [FirePunchFuelOverheated]
   znaczenie tagów: [Combustion] = 화상 / Burn; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [FirePunchFuelOverheated] = 과열 연료 / Overheated Fuel
   EN: If target has 6+ [Combustion], Coin Power +1\nCoins that consumed [FirePunchFuel] deal +10% damage\n<style="highlight">- When in [FirePunchFuelOverheated] state, deal +20% damage instead</style>
   PL:
831. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [FirePunchFuel]를 10 소모하여, [Combustion] 위력이 가장 낮은 적 2명에게 [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121102].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [FirePunchFuel], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Consume 10 [FirePunchFuel] and inflict 1 [Combustion] against 2 enemies that have the least [Combustion] Potency<style="highlight"></style>
   PL:
832. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [FirePunchFuel]를 10 소모하여, [Combustion] 횟수가 가장 낮은 적 <style="highlight">2</style>명에게 [Combustion] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121102].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [FirePunchFuel], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Consume 10 [FirePunchFuel] and inflict +1 [Combustion] Count against <style="highlight">2 enemies</style> that have the least [Combustion] Count
   PL:
833. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Combustion] 6 <style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[[FirePunchFuel]를 소모할 때 해당 코인의 피해량 +<style="highlight">15</style>%\n- [FirePunchFuelOverheated] 상태면, 대신 피해량 +<style="highlight">30</style>%로 적용
   źródło: Skills_personality-12.json :: dataList[id=1121102].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [FirePunchFuel], [FirePunchFuelOverheated]
   znaczenie tagów: [Combustion] = 화상 / Burn; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [FirePunchFuelOverheated] = 과열 연료 / Overheated Fuel
   EN: <style="highlight">Coin Power +1 for every 6 [Combustion] on target (max 2)</style>\nCoins that consumed [FirePunchFuel] deal +<style="highlight">15</style>% damage\n- When in [FirePunchFuelOverheated] state, deal +<style="highlight">30</style>% damage instead
   PL:
834. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [FirePunchFuel]를 10 소모하여, [Combustion] 위력이 가장 낮은 적 2명에게 [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_personality-12.json :: dataList[id=1121102].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [FirePunchFuel], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Consume 10 [FirePunchFuel] and inflict <style="highlight">2</style> [Combustion] against 2 enemies that have the least [Combustion] Potency
   PL:
835. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-12.json :: dataList[id=1121102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">+2</style> [Combustion] Count
   PL:
836. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [FirePunchFuel]를 10 소모하여, [Combustion] 횟수가 가장 낮은 적 2명에게 [Combustion] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121102].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FirePunchFuel], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Consume 10 [FirePunchFuel] and inflict +1 [Combustion] Count against 2 enemies that have the least [Combustion] Count
   PL:
837. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 불주먹
   źródło: Skills_personality-12.json :: dataList[id=1121103].levelList[level=3].name ; dataList[id=1121103].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Firefist
   PL:
838. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Combustion] 횟수 3 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Combustion] 6 당, 기본 위력 +1 (최대 2)\n[WhenUse] [FirePunchFuel]를 최대 25까지 소모하여 소모한 [FirePunchFuel]당 피해량 +1% (최대 25%)\n- [FirePunchFuelOverheated] 상태면, 소모한 [FirePunchFuel]당 피해량 +3% (최대 75%)\n[EndSkill] 대상이 사망했거나, 이 스킬에서 [FirePunchFuel]를 소모했다면, 다음 턴에 [HitDamageUp] 1 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121103].levelList[level=3].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [WhenUse], [FirePunchFuel], [FirePunchFuelOverheated], [EndSkill], [HitDamageUp]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [FirePunchFuelOverheated] = 과열 연료 / Overheated Fuel; [EndSkill] = [공격 종료시] / [Attack End]; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up
   EN: If target has 3+ [Combustion] Count, Coin Power +1\n[WhenUse] Base Power +1 for every 6 [Combustion] on target (max 2)\n[WhenUse] Consume up to 25 [FirePunchFuel] and deal +1% damage for every [FirePunchFuel] consumed (max 25%)\n- When in [FirePunchFuelOverheated] state, deal +3% damage for every [FirePunchFuel] consumed instead (max 75%)\n[EndSkill] If target is defeated, or if this Skill consumed [FirePunchFuel], gain 1 [HitDamageUp] next turn
   PL:
839. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [FirePunchFuel]를 소모했으면, [Combustion] 1 부여, [Combustion] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FirePunchFuel], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If this unit consumed [FirePunchFuel], inflict 1 [Combustion] and +1 [Combustion] Count
   PL:
840. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [FirePunchFuel]를 소모했으면, [Combustion] 1 부여, [Combustion] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 839 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 이 스킬에서 소모한 [FirePunchFuel]당, 피해량 +1% (최대 25%)\n- [FirePunchFuelOverheated] 상태면, 소모한 [FirePunchFuel]당 피해량 +3% (최대 75%)
   źródło: Skills_personality-12.json :: dataList[id=1121103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [FirePunchFuel], [FirePunchFuelOverheated]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [FirePunchFuelOverheated] = 과열 연료 / Overheated Fuel
   EN: [OnSucceedAttack] Deal +1% damage for every [FirePunchFuel] consumed by this Skill (max 25%)\n- When in [FirePunchFuelOverheated] state, deal +3% damage for every [FirePunchFuel] consumed instead (max 75%)
   PL:
842. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Combustion] 횟수 3 <style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 대상의 [Combustion] 6 당, 기본 위력 +1 (최대 <style="highlight">3</style>)\n[WhenUse] [FirePunchFuel]를 최대 25까지 소모하여 소모한 [FirePunchFuel]당 피해량 +<style="highlight">2</style>% (최대 <style="highlight">50</style>%)\n- [FirePunchFuelOverheated] 상태면, 소모한 [FirePunchFuel]당 피해량 +<style="highlight">4</style>% (최대 <style="highlight">100</style>%)\n[EndSkill] 대상이 사망했거나, 이 스킬에서[FirePunchFuel]를 소모했다면, 다음 턴에 [HitDamageUp] <style="highlight">2</style> 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121103].levelList[level=4].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [WhenUse], [FirePunchFuel], [FirePunchFuelOverheated], [EndSkill], [HitDamageUp]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [FirePunchFuelOverheated] = 과열 연료 / Overheated Fuel; [EndSkill] = [공격 종료시] / [Attack End]; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up
   EN: <style="highlight">Coin Power +1 for every 3 [Combustion] Count on target (max 2)</style>\n[WhenUse] Base Power +1 for every 6 [Combustion] on target (max <style="highlight">3</style>)\n[WhenUse] Consume up to 25 [FirePunchFuel] and deal +<style="highlight">2</style>% damage for every [FirePunchFuel] consumed (max <style="highlight">50</style>%)\n- When in [FirePunchFuelOverheated] state, deal +<style="highlight">4</style>% damage for every [FirePunchFuel] consumed (max <style="highlight">100</style>%)\n[EndSkill] If target is defeated, or if this Skill consumed [FirePunchFuel], gain <style="highlight">2</style> [HitDamageUp] next turn
   PL:
843. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [FirePunchFuel]를 소모했으면, [Combustion] <style="highlight">2</style> 부여, [Combustion] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [FirePunchFuel], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If this unit consumed [FirePunchFuel], inflict <style="highlight">2</style> [Combustion] and +1 [Combustion] Count
   PL:
844. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [FirePunchFuel]를 소모했으면, [Combustion] <style="highlight">2</style> 부여, [Combustion] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 843 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 이 스킬에서 소모한 [FirePunchFuel]당, 피해량 +<style="highlight">2</style>% (최대 <style="highlight">50</style>%)\n- [FirePunchFuelOverheated] 상태면, 소모한 [FirePunchFuel]당 피해량 +<style="highlight">4</style>% (최대 <style="highlight">100</style>%)
   źródło: Skills_personality-12.json :: dataList[id=1121103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [FirePunchFuel], [FirePunchFuelOverheated]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [FirePunchFuelOverheated] = 과열 연료 / Overheated Fuel
   EN: [OnSucceedAttack] Deal +<style="highlight">2</style>% damage for every [FirePunchFuel] consumed by this Skill (max <style="highlight">50</style>%)\n- When in [FirePunchFuelOverheated] state, deal +<style="highlight">4</style>% damage for every [FirePunchFuel] consumed instead (max <style="highlight">100</style>%)
   PL:
846. [Obrona (ulepszenia 1,4) — nazwa] 누님의 몫이 아직 남았다
   źródło: Skills_personality-12.json :: dataList[id=1121104].levelList[level=1].name ; dataList[id=1121104].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: kontra · moc bazowa: 9 · monety: 1 (+7)
   limit: do 50 znaków
   EN: I have to keep going for big sis
   PL:
847. [Obrona (ulepszenia 1,4) — opis] [DuelCounter]\n[StartBattle] [FirePunchFuel]를 100 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121104].levelList[level=1].desc ; dataList[id=1121104].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [FirePunchFuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [FirePunchFuel] = 12구산 연료 / District 12 Fuel
   EN: [DuelCounter]\n[StartBattle] Gain 100 [FirePunchFuel]
   PL:
848. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121104].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1121104].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 818 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Pasywka bojowa (od ulepszenia 1) — nazwa] 12구산 특제 공방 연료
   źródło: Passives.json :: dataList[id=1121102].name
   limit: do 50 znaków
   EN: District 12 Special Workshop Fuel
   PL:
850. [Pasywka bojowa (od ulepszenia 1) — opis] [FirePunchFuel] 100을 가지고 시작\n- 수치가 50 초과면, [FirePunchFuel]로 교체됨\n- 수치가 50 이하면, [FirePunchFuel]가 [FirePunchFuelOverheated]로 교체됨
   źródło: Passives.json :: dataList[id=1121102].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [FirePunchFuel], [FirePunchFuelOverheated]
   znaczenie tagów: [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [FirePunchFuelOverheated] = 과열 연료 / Overheated Fuel
   EN: Begin Encounters with 100 [FirePunchFuel]\n- At over 50 Stack, become [FirePunchFuel]\n- At 50 or less Stack, any [FirePunchFuel] becomes [FirePunchFuelOverheated]
   PL:
851. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — nazwa] 나만 살아남아버렸어...
   źródło: Passives.json :: dataList[id=1121101].name
   limit: do 40 znaków
   EN: I'm the only survivor...
   PL:
852. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — opis] 자신이 이번 전투에서 소모한 [FirePunchFuel], [FirePunchFuelOverheated]당 피해량 +0.2% (최대 40%)\n- 메인 타겟이 <혈귀>, <피주머니>거나, 대상의 [Combustion]과 [Combustion] 횟수의 합이 30 이상이면, 대신 피해량 +0.3% (최대 60%)\n\n[FirePunchFuel], [FirePunchFuelOverheated]가 1 이상일 때, [Combustion]이 부여된 적을 흐트러짐 상태로 만들거나 처치하면 [Combustion]이 없거나 [Combustion] 횟수가 가장 낮은 무작위 적 2명의 [Combustion] 횟수 2 증가 (턴 당 1 회)\n- 집중 전투인 경우 부위에 부여
   źródło: Passives.json :: dataList[id=1121101].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: \n, [FirePunchFuel], [FirePunchFuelOverheated], [Combustion]
   znaczenie tagów: [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [FirePunchFuelOverheated] = 과열 연료 / Overheated Fuel; [Combustion] = 화상 / Burn
   EN: Deal +0.2% damage for every [FirePunchFuel] and [FirePunchFuelOverheated] this unit consumed in this Encounter (max 40%)\n- If the main target is a <Bloodfiend>, <Bloodbag>, or if they have 30+ ([Combustion] + [Combustion] Count), deal +0.3% damage instead (max 60%)\n\nAt 1+ [FirePunchFuel] or [FirePunchFuelOverheated], if this unit Staggers or defeats enemies that have [Combustion], inflict +2 [Combustion] Count against 2 random enemies that do not have [Combustion] or has the least [Combustion] Count (once per turn)\n- For Focused Encounters, on Parts
   PL:
853. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — podsumowanie] 소모한 [FirePunchFuel], [FirePunchFuelOverheated]에 비례하여 피해량 증가[TabExplain]\n적 2명의 [Combustion] 횟수 증가 (턴당 1 회)
   źródło: Passives.json :: dataList[id=1121101].summary
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [FirePunchFuel], [FirePunchFuelOverheated], [TabExplain], [Combustion]
   znaczenie tagów: [FirePunchFuel] = 12구산 연료 / District 12 Fuel; [FirePunchFuelOverheated] = 과열 연료 / Overheated Fuel; [Combustion] = 화상 / Burn
   EN: Deal more damage based on [FirePunchFuel] and [FirePunchFuelOverheated] consumed\nInflict [Combustion] Count against 2 random enemies (once per turn)
   PL:
854. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 저건 우리 사무소의 복장이길...
   źródło: Passives.json :: dataList[id=1121121].name
   limit: do 50 znaków
   EN: I hope they're from our Office...
   PL:
855. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 속도가 가장 빠른 인격 1명이 공격 적중 시 대상의 [Combustion] 6 당, 분노 피해량 +5% (최대 20%)
   źródło: Passives.json :: dataList[id=1121121].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: 1 ally with the fastest Speed: On Hit, deal +5% more Wrath Damage for every 6 [Combustion] on the target (max 20%)
   PL:
856. [Kwestia głosowa [get_11211_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=get_11211_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Kwestia głosowa [get_11211_1] (Identity Acquisition)] 이건… 우리 불주먹 사무소의 복장이군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=get_11211_1].dlg
   limit: do 120 znaków
   EN: They're... all from our Office. Firefist Office.
   PL:
858. [Kwestia głosowa [lobby_morning_11211_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=lobby_morning_11211_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Kwestia głosowa [lobby_morning_11211_1] (Morning Greeting)] 해가 떠도 이곳은 그대로군. 썩은 공기, 눅눅한 벽, 한 줄기 볕조차 들지 않는 좁은 방…\n이런 반지하에서도 희망 따위를 품던 때가 있었다는 게… 이제 와선 농담처럼 느껴져.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=lobby_morning_11211_1].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Nothing changes here when the sun rises. A tiny room with rotten air, clammy walls... boxed in without even a ray of sunshine.\nThat we even used to dream of something stupid like hope in this semi-basement coffin... it all feels like a bad joke now.
   PL:
860. [Kwestia głosowa [lobby_noon_11211_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=lobby_noon_11211_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Kwestia głosowa [lobby_noon_11211_1] (Afternoon Greeting)] 아, 좀 일찍 나가는 편이 낫더군. P사에서 씨불여대던 브리핑은 낮부터 시작하거든.\n이미 귀에 처박을 대로 처박았지만… 그래도 들어두려는 편이지. 죽은 이들이 남긴 정보는 도움이 돼. 혈귀를 잡을 때든. 살아서 도망칠 때든.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=lobby_noon_11211_1].dlg
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ah, I like getting there early. P Corp. and their joke of a briefing starts around noon, you know.\nI've sat through it more than enough times to remember every little word of it, but... I always try to pay attention anyway. The dead leave good intel... both for killing and surviving Bloodfiends.
   PL:
862. [Kwestia głosowa [lobby_night_11211_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=lobby_night_11211_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Kwestia głosowa [lobby_night_11211_1] (Evening Greeting)] 그 빌어먹을 놀이공원이 개장하고 음악이 들리면… 잠시나마 익숙한 복장을 입고 있는 그리운 사람들이 보여.\n그 모든 것이 환각이라는 걸 알면서도 위안 삼는 건… 슬슬 그만두는 편이 좋겠지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=lobby_night_11211_1].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When that wretched amusement park opens, when that music begins to play... I can almost see them again. Wearing the same clothes they wore that day.\nBut it's all just a mirage... And I should stop letting illusions be my only solace.
   PL:
864. [Kwestia głosowa [smalltalk_11211_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=smalltalk_11211_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Kwestia głosowa [smalltalk_11211_1] (Chatter #1)] 혈귀 사냥꾼이 될 생각은 없어. 난 그들처럼 혈귀라는 괴물을 증오하는 게 아니거든.\n그저… 불주먹 사무소의 생존자로서 라만차랜드를 불태우고 싶을 뿐.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=smalltalk_11211_1].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I don't want to join the Bloodfiend Hunters. I don't hate those monsters—Bloodfiends—like the hunters do.\n... I just want to see La Manchaland burn. It's the least I can do as the last survivor of Firefist Office.
   PL:
866. [Kwestia głosowa [smalltalk_11211_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=smalltalk_11211_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
867. [Kwestia głosowa [smalltalk_11211_2] (Chatter #2)] 팔은 어디 공방에서 마련한 거냐고? 허. 차린지 한 달도 안 된 뒷골목 공방이었을 거야.\n주인이 신참에다 인맥도 없었던 건지 파리만 날리던 곳이었는데… 재능은 있었어. 뭐, 덕분에 괜찮은 걸 헐값에 살 수 있었지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=smalltalk_11211_2].dlg
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You want to know which Workshop I got this arm from? Huh. I think it was some Backstreets Workshop that hasn't even been open for a month and was already well on the way to closure.\nThe owner was clearly a new fella in the business with no connections to speak of, but had some talent. Which means that we managed to snag decent gears for cheap.
   PL:
868. [Kwestia głosowa [smalltalk_11211_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=smalltalk_11211_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Kwestia głosowa [smalltalk_11211_3] (Chatter #3)] 비가 오나… 떠올려보면 누님이 비를 그렇게 싫어하셨지. 불도 잘 안 붙고, 온몸이 축축해진다면서…\n그땐 아무래도 좋았지만, 지금은 나도 비가 썩 좋진 않아. 비가 올 땐, 놀이공원이 문을 열질 않아서 말이지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=smalltalk_11211_3].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rain... Big sis hated it. Said it makes everything feel clammy and cold, said she can't even spark the fire right when it rains...\nI didn't mind it then, but now... not so much. The amusement park doesn't open when it rains, you see.
   PL:
870. [Kwestia głosowa [smalltalk_11211_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=smalltalk_11211_4].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Kwestia głosowa [smalltalk_11211_4] (Post-Uptie Chat 1)] 미적지근한 공로를 내세워 기여금으로 입에 풀칠할 생각은 없어. 그랬다간 죽은 자들이 날 용서치 않을 테지.\n난… 끝까지 불태울 거야. 저 가증스러운 놀이공원도, 누님에게 입혀졌던 그 옷들도, 전부.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=smalltalk_11211_4].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I'm not gonna flaunt these middling results to line my pockets with contribution rewards. The dead won't forgive me if I do.\nInstead, I'm... I'm gonna burn it all down. That disgusting amusement park, and the clothes they forced onto her... all of it.
   PL:
872. [Kwestia głosowa [smalltalk_11211_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=smalltalk_11211_5].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
873. [Kwestia głosowa [smalltalk_11211_5] (Post-Uptie Chat 2)] 그래, 그거야. 물을 보고 두려워서 사람마냥 벌벌 떨어대는 것보다, 그토록 갈망하던 피가 불로 끓어 눌러붙은 꼴을 보고 짐승처럼 달려드는 쪽이… 좀 더 혈귀답잖아?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=smalltalk_11211_5].dlg
   limit: do 360 znaków
   EN: There it is, growling and skittering toward the burnt and congealed blood like the bloodsucking animals you are. Now you're behaving as Bloodfiends should, aren't you? Trembling in fear makes it look as though you're pretending to be human, even if it is water that makes you shudder.
   PL:
874. [Kwestia głosowa [neglect_11211_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=neglect_11211_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Kwestia głosowa [neglect_11211_1] (Idle)] …담배 하나만 줄 수 있나? 내가… 남은게 불밖에 없어서.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=neglect_11211_1].dlg
   limit: do 120 znaków
   EN: ... Care to spare me a cig? I've got light. ... I guess that's all I've got.
   PL:
876. [Kwestia głosowa [gacksung_11211_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=gacksung_11211_1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [Kwestia głosowa [gacksung_11211_1] (Uptying)] 이 차가운 도시에서도… 복수만큼은 화끈해야 하지 않겠나.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=gacksung_11211_1].dlg
   limit: do 120 znaków
   EN: It's a cold, cold City, bud… Let’s at least have the decency to serve revenge piping hot.
   PL:
878. [Kwestia głosowa [formation_11211_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=formation_11211_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Kwestia głosowa [formation_11211_1] (Deployment)] 연료는 잔뜩 준비해뒀지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=formation_11211_1].dlg
   limit: do 120 znaków
   EN: I've prepped plenty of fuel.
   PL:
880. [Kwestia głosowa [battleentry_11211_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battleentry_11211_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [Kwestia głosowa [battleentry_11211_1] (Stage Entry)] …입장을 알리는 음악 소리가 들리는군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battleentry_11211_1].dlg
   limit: do 120 znaków
   EN: ... They always open with this music.
   PL:
882. [Kwestia głosowa [battle_select_11211_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_select_11211_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [Kwestia głosowa [battle_select_11211_1] (Viewed in Battle)] 이야기는 폐장 후에… 마저 하지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_select_11211_1].dlg
   limit: do 120 znaków
   EN: This conversation can wait... until the park closes.
   PL:
884. [Kwestia głosowa [battle_endcommand_11211_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_endcommand_11211_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
885. [Kwestia głosowa [battle_endcommand_11211_1] (Commencing Attack)] 언제까지 버티나 보자고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_endcommand_11211_1].dlg
   limit: do 120 znaków
   EN: Let's see how much more of this you can take.
   PL:
886. [Kwestia głosowa [battle_enemy_break_11211_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_enemy_break_11211_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [Kwestia głosowa [battle_enemy_break_11211_1] (Enemy Stagger)] 남길 말은 없겠지?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_enemy_break_11211_1].dlg
   limit: do 120 znaków
   EN: I don't assume you have any last words?
   PL:
888. [Kwestia głosowa [battle_break_11211_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_break_11211_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [Kwestia głosowa [battle_break_11211_1] (Staggered)] 후… 괜찮아. 상처는 지졌으니까.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_break_11211_1].dlg
   limit: do 120 znaków
   EN: Haah... don't worry. Wound's been cauterized.
   PL:
890. [Kwestia głosowa [battle_kill_11211_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_kill_11211_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
891. [Kwestia głosowa [battle_kill_11211_1] (Enemy Killed)] …전부 불타버렸나.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_kill_11211_1].dlg
   limit: do 120 znaków
   EN: ... All burnt to ashes.
   PL:
892. [Kwestia głosowa [battle_dead_11211_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_dead_11211_1].desc
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [Kwestia głosowa [battle_dead_11211_1] (Death)] 하… 벌써 만나러 가는 건… 좀 이르지 않나…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_dead_11211_1].dlg
   limit: do 120 znaków
   EN: Haah... isn't it too... early for me to join them...?
   PL:
894. [Kwestia głosowa [choice_success_p_11211_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=choice_success_p_11211_2].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
895. [Kwestia głosowa [choice_success_p_11211_2] (Check Passed)] 먹고 살려고 어지간한 건 다 해봤거든.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=choice_success_p_11211_2].dlg
   limit: do 120 znaków
   EN: I've done all kinds of odd jobs to make ends meet.
   PL:
896. [Kwestia głosowa [choice_fail_n_11211_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=choice_fail_n_11211_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
897. [Kwestia głosowa [choice_fail_n_11211_1] (Check Failed)] …다음엔 좀 더 잘해보지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=choice_fail_n_11211_1].dlg
   limit: do 120 znaków
   EN: ... I'll do better next time.
   PL:
898. [Kwestia głosowa [battle_clear_11211_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_clear_11211_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [Kwestia głosowa [battle_clear_11211_1] (Victory Cry)] 이번에도 여기서 막혔나… 다음에는 저 앞의 빌어먹을 퍼레이드도 반드시… 불바다로 만들거다.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_clear_11211_1].dlg
   limit: do 150 znaków
   EN: So this is as far as I get this go around, huh... Next time, I'm coming back to burn that wretched parade alive.
   PL:
900. [Kwestia głosowa [battle_clear_ex_11211_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_clear_ex_11211_1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
901. [Kwestia głosowa [battle_clear_ex_11211_1] (Extra Conditions Fulfilled)] 거봐, 누님… 내가 뭐랬어. 돌아와서 모조리 불태울 거라고 했잖아.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_clear_ex_11211_1].dlg
   limit: do 120 znaków
   EN: What'd I say, big sis? I said I'd return to burn it all down.
   PL:
902. [Kwestia głosowa [battle_defeat_11211_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_defeat_11211_1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
903. [Kwestia głosowa [battle_defeat_11211_1] (Defeat Wail)] …다음에는 더 많이 불태울 거다. 너희가 마실 피 한 방울조차 남기지 않고, 모조리.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Firepunch_11211.json :: dataList[id=battle_defeat_11211_1].dlg
   limit: do 130 znaków
   EN: ... I'll leave nothing but ashes next time. I won't leave even a drop of blood for you to lap on.
   PL:

## [000] Heishou Pack - Si Branch — Gregor — 흑수 - 사
- ID Tożsamości: `11212` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 69 · szybkość: 2–5 / 2–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture, Poise

904. [Karta Tożsamości — tytuł] 흑수 - 사
   źródło: Personalities.json :: dataList[id=11212].title
   limit: do 40 znaków
   EN: Heishou Pack - Si Branch
   PL:
905. [Karta Tożsamości — nazwa] 그레고르
   źródło: Personalities.json :: dataList[id=11212].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
906. [Karta Tożsamości — nazwa z tytułem] 그레고르
   źródło: Personalities.json :: dataList[id=11212].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [Karta Tożsamości — opis] 그레고르의 열두번째 인격
   źródło: Personalities.json :: dataList[id=11212].desc
   limit: do 120 znaków
   EN: Gregor’s 12th Identity
   PL:
908. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 뱀 송곳니
   źródło: Skills_personality-12.json :: dataList[id=1121201].levelList[level=1].name ; dataList[id=1121201].levelList[level=2].name ; dataList[id=1121201].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Snake Fang
   PL:
909. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +1 [Breath] Count
   PL:
910. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
911. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합이 10 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-12.json :: dataList[id=1121201].levelList[level=2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: <style="highlight">[WhenUse] At 10+ ([Breath] on self + [Burst] on target), Coin Power +1</style>\n[WhenUse] Gain +<style="highlight">2</style> [Breath] Count
   PL:
913. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1121201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
914. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1121201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
915. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] 자신에게 [SnakeStance]이 있으면, [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-12.json :: dataList[id=1121201].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [SnakeStance], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [SnakeStance] = 사완 / Serpent Arm; [Burst] = 파열 / Rupture
   EN: <style="highlight">[CriticalOnSucceedAttack] If this unit has [SnakeStance], inflict +1 [Burst] Count</style>
   PL:
916. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 10 당 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-12.json :: dataList[id=1121201].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: <style="highlight">[WhenUse] Coin Power +1 for every 10 ([Breath] on self + [Burst] on target) (max 2)</style>\n[WhenUse] Gain +2 [Breath] Count
   PL:
917. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 자신에게 [SnakeStance]이 있으면, [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [SnakeStance], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [SnakeStance] = 사완 / Serpent Arm; [Burst] = 파열 / Rupture
   EN: [CriticalOnSucceedAttack] If this unit has [SnakeStance], inflict +1 [Burst] Count<style="highlight"></style>
   PL:
918. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 시야 밖에서 도려낸다
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=1].name ; dataList[id=1121202].levelList[level=2].name ; dataList[id=1121202].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Blindsiding Cleave
   PL:
919. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] [Burst] 횟수 1 증가\n[WinDuel] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Burst], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [WinDuel] Inflict +1 [Burst] Count\n[WinDuel] Gain +1 [Breath] Count
   PL:
920. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
921. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
923. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [BurstPoison] 부여
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstPoison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [OnSucceedAttack] Inflict [BurstPoison]
   PL:
924. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합이 10 이상이면, 코인 위력 +1</style>\n[WinDuel] [Burst] 횟수 1 증가\n[WinDuel] 자신의 [Breath] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">[WhenUse] At 10+ ([Breath] on self + [Burst] on target), Coin Power +1</style>\n[WinDuel] Inflict +1 [Burst] Count\n[WinDuel] Gain +<style="highlight">2</style> [Breath] Count
   PL:
925. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1121202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1121202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
927. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 750 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
928. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Breath]이 30 이상이면, [Breath] 10 소모하여 코인 1회 재사용 (최대 1회)</style>
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: <style="highlight">[OnSucceedAttack] At 30+ [Breath], consume 10 [Breath] on self to Reuse Coin once (1 time max)</style>
   PL:
929. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [BurstPoison] 부여<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=2].coinlist[#2].coindescs[#2].desc ; dataList[id=1121202].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BurstPoison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [OnSucceedAttack] Inflict [BurstPoison]<style="highlight"></style>
   PL:
930. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 10 당 코인 위력 +1 (최대 2)</style>\n[WinDuel] [Burst] 횟수 <style="highlight">2</style> 증가\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">[WhenUse] Coin Power +1 for every 10 ([Breath] on self + [Burst] on target) (max 2)</style>\n[WinDuel] Inflict +<style="highlight">2</style> [Burst] Count\n[WinDuel] Gain +2 [Breath] Count
   PL:
931. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]<style="highlight"></style>
   PL:
932. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Breath]이 30 이상이면, [Breath] 10 소모하여 코인 1회 재사용 (최대 1회)<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] At 30+ [Breath], consume 10 [Breath] on self to Reuse Coin once (1 time max)<style="highlight"></style>
   PL:
933. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 4 — opis] <style="highlight">[CriticalOnSucceedAttack] [SnakeStance] 1 얻음</style>
   źródło: Skills_personality-12.json :: dataList[id=1121202].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [SnakeStance]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [SnakeStance] = 사완 / Serpent Arm
   EN: <style="highlight">[CriticalOnSucceedAttack] Gain 1 [SnakeStance]</style>
   PL:
934. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 절사완철
   źródło: Skills_personality-12.json :: dataList[id=1121203].levelList[level=3].name ; dataList[id=1121203].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 8 · monety: 1 (+14)
   limit: do 40 znaków
   EN: Serpentshear Puncturing Arm
   PL:
935. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 8 당 코인 위력 +1 (최대 4)\n- 자신에게 [SnakeStance]이 있으면, 대신 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 5 당 코인 위력 +1 (최대 6)\n[WhenUse] [SnakeStance] 3 얻음\n[WinDuel] 대상의 [Burst]이 5 이상이면, [Breath] 5 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121203].levelList[level=3].desc ; dataList[id=1121203].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Burst], [SnakeStance], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [SnakeStance] = 사완 / Serpent Arm; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Coin Power +1 for every 8 ([Breath] on self + [Burst] on target) (max 4)\n- If this unit has [SnakeStance], Coin Power +1 for every 5 ([Breath] on self + [Burst] on target) instead (max 6)\n[WhenUse] Gain 3 [SnakeStance]\n[WinDuel] If target has 5+ [Burst], gain 5 [Breath]
   PL:
936. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] 대상의 ([Burst] 위력 + 자신의 [Breath] 위력)당 피해량 +5% (최대 150%)
   źródło: Skills_personality-12.json :: dataList[id=1121203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst], [Breath]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: Deal +5% damage for every ([Breath] on self + [Burst] on target) (max 150%)
   PL:
937. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] 자신에게 [SnakeStance]이 있으면, 크리티컬 피해량 +75%
   źródło: Skills_personality-12.json :: dataList[id=1121203].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SnakeStance]
   znaczenie tagów: [SnakeStance] = 사완 / Serpent Arm
   EN: If this unit has [SnakeStance], deal +75% Damage on Critical Hit
   PL:
938. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [BurstPoison] 2 소모
   źródło: Skills_personality-12.json :: dataList[id=1121203].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstPoison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [OnSucceedAttack] Reduce [BurstPoison] on target by 2
   PL:
939. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] [BurstPoison] 3 소모
   źródło: Skills_personality-12.json :: dataList[id=1121203].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [BurstPoison]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [CriticalOnSucceedAttack] Reduce [BurstPoison] on target by 3
   PL:
940. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [BurstPoison] 부여
   źródło: Skills_personality-12.json :: dataList[id=1121203].levelList[level=3].coinlist[#0].coindescs[#4].desc
   (powtórzenie elementu 923 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
941. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] 대상의 ([Burst] 위력 + 자신의 [Breath] 위력)당 피해량 <style="highlight">+10% (최대 200%)</style>
   źródło: Skills_personality-12.json :: dataList[id=1121203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Burst], [Breath]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: Deal <style="highlight">+10%</style> damage for every ([Breath] on self + [Burst] on target) <style="highlight">(max 200%)</style>
   PL:
942. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] 자신에게 [SnakeStance]이 있으면, 크리티컬 피해량 <style="highlight">+100%</style>
   źródło: Skills_personality-12.json :: dataList[id=1121203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SnakeStance]
   znaczenie tagów: [SnakeStance] = 사완 / Serpent Arm
   EN: If this unit has [SnakeStance], deal <style="highlight">+100%</style> Damage on Critical Hit
   PL:
943. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [BurstPoison] 2 소모<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121203].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BurstPoison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [OnSucceedAttack] Reduce [BurstPoison] on target by 2<style="highlight"></style>
   PL:
944. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] [BurstPoison] 3 소모<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121203].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [BurstPoison]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [CriticalOnSucceedAttack] Reduce [BurstPoison] on target by 3<style="highlight"></style>
   PL:
945. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 5 — opis] <style="highlight">[CriticalOnSucceedAttack] [Burst] 횟수 2 증가</style>
   źródło: Skills_personality-12.json :: dataList[id=1121203].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict +2 [Burst] Count</style>
   PL:
946. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 6 — opis] [OnSucceedAttack] [BurstPoison] 부여<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121203].levelList[level=4].coinlist[#0].coindescs[#5].desc
   (powtórzenie elementu 929 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
947. [Obrona (ulepszenia 1,4) — nazwa] 반축
   źródło: Skills_personality-12.json :: dataList[id=1121204].levelList[level=1].name ; dataList[id=1121204].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 3 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Reversal Kick
   PL:
948. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] 다음 턴에 [SnakeStance] 3 얻음
   źródło: Skills_personality-12.json :: dataList[id=1121204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [SnakeStance]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [SnakeStance] = 사완 / Serpent Arm
   EN: [CanDuelGuard] \n[StartBattle] Gain 3 [SnakeStance] next turn
   PL:
949. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-12.json :: dataList[id=1121204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
950. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[StartBattle] 다음 턴에 [SnakeStance] 3 얻음\n<style="highlight">[WhenUse] 자신의 [Breath]이 10 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-12.json :: dataList[id=1121204].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [StartBattle], [SnakeStance], [WhenUse], [Breath]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [SnakeStance] = 사완 / Serpent Arm; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [CanDuelGuard]\n[StartBattle] Gain 3 [SnakeStance] next turn\n<style="highlight">[WhenUse] At 10+ [Breath] Count, Coin Power +1</style>
   PL:
951. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL:
952. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — nazwa] 흑수화[사]
   źródło: Passives.json :: dataList[id=1121201].name
   limit: do 40 znaków
   EN: Heishou Mutation [Si]
   PL:
953. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — opis] 대상에게 [BurstPoison]이 있으면, 자신의 [SnakeStance]당 피해량 +5% (최대 15%)\n자신이 [BurstPoison]을 소모시켜 수치를 0으로 만들었으면, 다음 턴에 [PenetrateDamageUp] 1 얻음 (최대 2)
   źródło: Passives.json :: dataList[id=1121201].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [BurstPoison], [SnakeStance], [PenetrateDamageUp]
   znaczenie tagów: [BurstPoison] = 주살【독】 / Deathrite【Venom】; [SnakeStance] = 사완 / Serpent Arm; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: If the target has [BurstPoison], deal +5% damage for every [SnakeStance] on self (max 15%)\nIf this unit reduced the target's [BurstPoison] down to 0 Stack, gain 1 [PenetrateDamageUp] next turn (max 2)
   PL:
954. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 뱀과 같이 유연하고 늘어나며 급작스럽게
   źródło: Passives.json :: dataList[id=1121221].name
   limit: do 70 znaków
   EN: Like a Serpent: Flexible, Elastic, and Unpredictable
   PL:
955. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 전투 중 자신이 사망했으면, 이후 대기 해제되는 인격 중 편성 순서가 가장 빠른 대상 1명에게 매 턴 마다 전투 시작시 [Breath] 2 부여
   źródło: Passives.json :: dataList[id=1121221].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: If this unit is killed in this Encounter: every turn, at Combat Start, apply 2 [Breath] to the Substituting Identity of the earliest Deployment order
   PL:
956. [Kwestia głosowa [get_11212_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=get_11212_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [Kwestia głosowa [get_11212_1] (Identity Acquisition)] 이 정도면 사람 팔이구만 뭐. 난 또 이번에 시술받으면 팔 두 짝 다 뱀으로 변하나 싶었지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=get_11212_1].dlg
   limit: do 140 znaków
   EN: This is pretty much a human arm alright. I thought they were replacing both of my arms with actual snakes.
   PL:
958. [Kwestia głosowa [lobby_morning_11212_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=lobby_morning_11212_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
959. [Kwestia głosowa [lobby_morning_11212_1] (Morning Greeting)] 밤새 쓰고 나면, 아침엔 좀 쉬게 둬야지. 이번 주군은 아침에도 자꾸 부른단 말이야.\n뭐, 계약한 지 얼마 안 됐으니 모를 법도 하겠지~ 나중에는 아끼느라 써야 할 때도 놓칠걸.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=lobby_morning_11212_1].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Doesn't this lord have the common decency to let his Heishou relax after an all-nighter...? Not a fan of his morning summons.\nEh, guess he's got much to learn, being new in the game and everything~ He'll soon get so stingy with us that he might forget to summon us where we're needed.
   PL:
960. [Kwestia głosowa [lobby_noon_11212_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=lobby_noon_11212_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
961. [Kwestia głosowa [lobby_noon_11212_1] (Afternoon Greeting)] 처음엔 연초를 끊은 스트레스 때문에 살이 가죽만 남았나 했는데, 이 삐쩍 마른 몸은 사환의 효능이더라고.\n익숙해져야지~ 보기엔 흉해도 임무 중에는 이런 얇실한 몸이 도움이 되거든.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=lobby_noon_11212_1].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Thought I was losing weight from the stress of going cold turkey on tobacco, but... apparently it's an intended effect of the Si Bolus.\nGotta get used to it, I suppose~ This skin and bones body isn't pretty, but it really does come in handy for our missions.
   PL:
962. [Kwestia głosowa [lobby_night_11212_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=lobby_night_11212_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
963. [Kwestia głosowa [lobby_night_11212_1] (Evening Greeting)] 이 시간만 되면, 대관원이 참 조용해. 이 안락하고 멋진 집에서… 편히 잠도 못 자고 숨죽이고 있다니. 흑수도 흑수지만, 주군도 썩 할만한 건 못 되는 모양이야.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=lobby_night_11212_1].dlg
   limit: do 280 znaków
   EN: Daguanyuan gets real quiet around this hour. The lords live in such fancy, luxurious homes... but they can't even get a wink of sleep at night. Being a Heishou's no way to live, but these lords have it pretty rough, too.
   PL:
964. [Kwestia głosowa [smalltalk_11212_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=smalltalk_11212_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
965. [Kwestia głosowa [smalltalk_11212_1] (Chatter #1)] 뭐… 흑수마다 하는 일에 차이가 있다 보니, 뱀은 좀 더 유연한 게 낫더라고. 사고방식도, 처리 방식도.\n은밀하게 처리해야 하는 우리가 물불 안 가리고 달려드는 싸움닭들처럼 굴다간 될 일도 안 되거든.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=smalltalk_11212_1].dlg
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Well... Each branch of the Heishou specialize in different jobs, and we snakes benefit from having some flexibility. In both the literal and metaphorical meanings of the word.\nWe're more like covert operatives; can't go rushing into things like roosters in a cockfight, right?
   PL:
966. [Kwestia głosowa [smalltalk_11212_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=smalltalk_11212_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
967. [Kwestia głosowa [smalltalk_11212_2] (Chatter #2)] 팔 쭉쭉 늘어나는 거… 아마 상대한테는 꽤 까다로울 거야.\n거리 가늠도 잘 안될뿐더러, 언제 어떤 방향에서 공격이 들이닥칠지 도통 알 수가 없을 테니까.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=smalltalk_11212_2].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I bet these stretchy arms makes me a tricky enemy to fight.\nThese arms can blindside them by coming in from any distance, any direction.
   PL:
968. [Kwestia głosowa [smalltalk_11212_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=smalltalk_11212_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
969. [Kwestia głosowa [smalltalk_11212_3] (Chatter #3)] 흑수는 홍원의 은원에서 한 발짝 벗어나 있어. 덕분에 임무를 수행할 때 걸림이 없지.\n원한이란 건… 가까이 있는 존재에게나 갖는 거야. 잠깐 툭 튀어나왔다 사라지는 낯선 도구에 원한을 품는 건, 이상하잖아?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=smalltalk_11212_3].dlg
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Us Heishou are a step removed from the complicated network of resentments and favors that Hongyuan folks have, which means that we don't have much reason to hesitate when carrying out our missions.\nResentment is for someone close to you. It'd be weird to take revenge on a tool that goes away just as quickly as they appeared, right?
   PL:
970. [Kwestia głosowa [smalltalk_11212_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=smalltalk_11212_4].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
971. [Kwestia głosowa [smalltalk_11212_4] (Post-Uptie Chat 1)] 홍원에 있는 가문이란 가문은 다 모셔봤지. 멸문한 공씨도, 바닥을 기던 사씨도, 강성한 가씨도 모두.\n그걸 생각하면 나도 참 오래 살았단 말이야. 슬슬 죽을 때가 된 것 같은데, 허물만 벗고 또 살아 돌아왔으니…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=smalltalk_11212_4].dlg
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I've served every damn family in Hongyuan. The Kongs before they were massacred, the Shis during their decline, and the ever-powerful Jias.\nThat makes me realize just how long I've survived in this hole. I can feel death just around the corner, but... I just molt outta my slough and come back like nothing happened...
   PL:
972. [Kwestia głosowa [smalltalk_11212_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=smalltalk_11212_5].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
973. [Kwestia głosowa [smalltalk_11212_5] (Post-Uptie Chat 2)] 오래 살아남았지만… 별 의미가 없어. 삶이 점점 무던해지고, 죽으면 죽는구나. 살면 사는구나. 그러다가 더 이상 깎아낼 감정조차 사라지면… 그 순간이 죽음의 문턱 위지. 다른 게 아냐.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=smalltalk_11212_5].dlg
   limit: do 290 znaków
   EN: I'm a survivor. Been one for a long, long time... but it's all pointless. Life's grown so dull that I've lost all attachment to life and death. But I know that real death'll come when... the last of my emotions erode away.
   PL:
974. [Kwestia głosowa [neglect_11212_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=neglect_11212_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
975. [Kwestia głosowa [neglect_11212_1] (Idle)] …그새 주군이 명령을 내렸어? 아이고… 그럼 이렇게 멍때릴 때가 아니지. 어서 가자고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=neglect_11212_1].dlg
   limit: do 130 znaków
   EN: ... The lord sent out an order? Oh, man... I gotta stop zoning out like this. Let's hurry on.
   PL:
976. [Kwestia głosowa [gacksung_11212_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=gacksung_11212_1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
977. [Kwestia głosowa [gacksung_11212_1] (Uptying)] 눈 굴려봤자 소용없어. 이미 똬리를 틀었는데, 무슨 수로 도망가게.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=gacksung_11212_1].dlg
   limit: do 160 znaków
   EN: Hey, no point in looking around for a way out. I'm all coiled up now, ready to strike. You're not getting out of this.
   PL:
978. [Kwestia głosowa [formation_11212_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=formation_11212_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
979. [Kwestia głosowa [formation_11212_1] (Deployment)] 어디서 뱀 기어가는 소리 들리지 않아?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=formation_11212_1].dlg
   limit: do 120 znaków
   EN: Don't you hear a snake slithering somewhere?
   PL:
980. [Kwestia głosowa [battleentry_11212_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battleentry_11212_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
981. [Kwestia głosowa [battleentry_11212_1] (Stage Entry)] 이 경로는… 숨어들기 나쁘지 않군, 그래.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battleentry_11212_1].dlg
   limit: do 120 znaków
   EN: This... is a pretty good infiltration route.
   PL:
982. [Kwestia głosowa [battle_select_11212_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_select_11212_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
983. [Kwestia głosowa [battle_select_11212_1] (Viewed in Battle)] 똬리를 튼 뱀 근처엔 오지 말랬잖아.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_select_11212_1].dlg
   limit: do 120 znaków
   EN: Told you to watch yourself around a coiled-up snake.
   PL:
984. [Kwestia głosowa [battle_endcommand_11212_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_endcommand_11212_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
985. [Kwestia głosowa [battle_endcommand_11212_1] (Commencing Attack)] 자, 어느 쪽일지 잘 생각해 보라고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_endcommand_11212_1].dlg
   limit: do 120 znaków
   EN: Now, give it a real good guess. Which direction will my arm strike from?
   PL:
986. [Kwestia głosowa [battle_enemy_break_11212_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_enemy_break_11212_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
987. [Kwestia głosowa [battle_enemy_break_11212_1] (Enemy Stagger)] 이건 예상 못 했나 봐?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_enemy_break_11212_1].dlg
   limit: do 120 znaków
   EN: Didn't see that coming, did you?
   PL:
988. [Kwestia głosowa [battle_break_11212_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_break_11212_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
989. [Kwestia głosowa [battle_break_11212_1] (Staggered)] 헛…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_break_11212_1].dlg
   limit: do 120 znaków
   EN: Hup...
   PL:
990. [Kwestia głosowa [battle_kill_11212_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_kill_11212_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
991. [Kwestia głosowa [battle_kill_11212_1] (Enemy Killed)] 깔끔하게 물었군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_kill_11212_1].dlg
   limit: do 120 znaków
   EN: Clean bite, huh?
   PL:
992. [Kwestia głosowa [battle_dead_11212_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_dead_11212_1].desc
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
993. [Kwestia głosowa [battle_dead_11212_1] (Death)] 후… 이날이 오긴 오는구만.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_dead_11212_1].dlg
   limit: do 120 znaków
   EN: Haah... So death can claim me, after all.
   PL:
994. [Kwestia głosowa [choice_success_p_11212_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=choice_success_p_11212_2].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
995. [Kwestia głosowa [choice_success_p_11212_2] (Check Passed)] 어려울 거 없다고 했잖아, 주군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=choice_success_p_11212_2].dlg
   limit: do 120 znaków
   EN: Told you I can handle it, my lord.
   PL:
996. [Kwestia głosowa [choice_fail_n_11212_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=choice_fail_n_11212_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
997. [Kwestia głosowa [choice_fail_n_11212_1] (Check Failed)] 시작은 좋았는데, 뱀의 꼬리였군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=choice_fail_n_11212_1].dlg
   limit: do 120 znaków
   EN: Now, ain't that a snake's tail of an ending? A real letdown.
   PL:
998. [Kwestia głosowa [battle_clear_11212_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_clear_11212_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
999. [Kwestia głosowa [battle_clear_11212_1] (Victory Cry)] 몇 명 놓치긴 했지만… 주살 독을 맞은 이상, 오래 살긴 글렀을 거야. 이 정도면 주군도 만족하실 테니, 돌아가자고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_clear_11212_1].dlg
   limit: do 190 znaków
   EN: Let some of 'em get away, but I've already marked them with the Deathrite venom. They won't get very far. Let's head back, the lord'll be satisfied.
   PL:
1000. [Kwestia głosowa [battle_clear_ex_11212_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_clear_ex_11212_1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1001. [Kwestia głosowa [battle_clear_ex_11212_1] (Extra Conditions Fulfilled)] 이걸로… 이번 주군과 결별할 날도 머지않았나. 마지막까지 알뜰히 사용하시는 것 같으니 미련은 없겠다마는.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_clear_ex_11212_1].dlg
   limit: do 150 znaków
   EN: With this... looks like I'll be saying goodbye to this lord soon. He made sure he got the bang for his buck, though.
   PL:
1002. [Kwestia głosowa [battle_defeat_11212_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_defeat_11212_1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1003. [Kwestia głosowa [battle_defeat_11212_1] (Defeat Wail)] 당분간은 고개 숙이고 기어야겠군. 무리한 임무도 아닌 데 실패했으니, 이번 주군은 오래 보겠어?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Blackwater_11212.json :: dataList[id=battle_defeat_11212_1].dlg
   limit: do 170 znaków
   EN: Gonna have to keep things low-key for a while. Failing such an easy mission... guess I'll be sticking with this lord for a bit, huh?
   PL:

## [000] Night Awls Capitano — Gregor — 밤의 송곳 카피타노
- ID Tożsamości: `11213` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9107 · HP bazowe: 69 · szybkość: 1–4 / 2–5 / 3–6 / 3–6
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Tremor, Bleed

1004. [Karta Tożsamości — tytuł] 밤의 송곳\n카피타노
   źródło: Personalities.json :: dataList[id=11213].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Night Awls Capitano
   PL:
1005. [Karta Tożsamości — nazwa] 그레고르
   źródło: Personalities.json :: dataList[id=11213].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1006. [Karta Tożsamości — nazwa z tytułem] 그레고르
   źródło: Personalities.json :: dataList[id=11213].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1007. [Karta Tożsamości — opis] 그레고르의 열세번째 인격
   źródło: Personalities.json :: dataList[id=11213].desc
   limit: do 120 znaków
   EN: Gregor’s 13th Identity
   PL:
1008. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 틈새 찌르기
   źródło: Skills_personality-12.json :: dataList[id=1121301].levelList[level=1].name ; dataList[id=1121301].levelList[level=2].name ; dataList[id=1121301].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Gap Attack
   PL:
1009. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL:
1010. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121301].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1121301].levelList[level=2].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 716 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1011. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [HurtNightStiletto] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121301].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1121301].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1121301].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [HurtNightStiletto]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HurtNightStiletto] = 상처 / Open Wound
   EN: [OnSucceedAttack] Inflict 1 [HurtNightStiletto]
   PL:
1012. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상의 [Laceration]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-12.json :: dataList[id=1121301].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 6+ ([Laceration] + [Vibration]), Coin Power +1
   PL:
1013. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-12.json :: dataList[id=1121301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1121301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
1014. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 다음 턴에 [Agility] 1 얻음 (턴당 1회)</style>\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 6<style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-12.json :: dataList[id=1121301].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Agility], [Laceration], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[WhenUse] Gain 1 [Agility] next turn (once per turn)</style>\n[WhenUse] Coin Power +1 <style="highlight">for every</style> 6 ([Laceration] + [Vibration]) on target <style="highlight">(max 2)</style>
   PL:
1015. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-12.json :: dataList[id=1121301].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
1016. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 스틸레토 도피오
   źródło: Skills_personality-12.json :: dataList[id=1121302].levelList[level=1].name ; dataList[id=1121302].levelList[level=2].name ; dataList[id=1121302].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Stiletto Doppio
   PL:
1017. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-12.json :: dataList[id=1121302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [VibrationExplosion], [Vibration]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [WinDuel] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
1018. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121302].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1121302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1121302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL:
1019. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [HurtNightStiletto] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121302].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1121302].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1121302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1011 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1020. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상의 [Laceration]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1\n[WinDuel] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-12.json :: dataList[id=1121302].levelList[level=2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [Vibration], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [WhenUse] If target has 6+ ([Laceration] + [Vibration]), Coin Power +1\n[WinDuel] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
1021. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121302].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1121302].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 555 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1022. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 적(본체)의 체력이 20% 이하이면, ‘메르체’ 사용
   źródło: Skills_personality-12.json :: dataList[id=1121302].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If the enemy(Core) has 20%- HP, use 'Mercé'
   PL:
1023. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — podsumowanie] [OnSucceedAttack] ‘메르체’ 사용
   źródło: Skills_personality-12.json :: dataList[id=1121302].levelList[level=2].coinlist[#2].coindescs[#0].summary ; dataList[id=1121302].levelList[level=4].coinlist[#2].coindescs[#0].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Use 'Mercé'
   PL:
1024. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Laceration]과 [Vibration]의 합 6<style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WinDuel] <style="highlight">[Vibration] 1 부여.</style> [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-12.json :: dataList[id=1121302].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [Vibration], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [WhenUse] Coin Power +1 <style="highlight">for every</style> 6 ([Laceration] + [Vibration]) on target <style="highlight">(max 2)</style>\n[WinDuel] <style="highlight">Inflict 1 [Vibration]</style> and trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
1025. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 적(본체)의 체력이 20% 이하이거나, <style="highlight">대상에게 [HorrHurtNightStiletto]가 있으면,</style> ‘메르체’ 사용
   źródło: Skills_personality-12.json :: dataList[id=1121302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [HorrHurtNightStiletto]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HorrHurtNightStiletto] = 치명적인 상처 / Fatal Wound
   EN: [OnSucceedAttack] If the enemy(Core) has 20%- HP, or <style="highlight">if target has [HorrHurtNightStiletto]</style>, use 'Mercé'
   PL:
1026. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 엑시큐션
   źródło: Skills_personality-12.json :: dataList[id=1121303].levelList[level=3].name ; dataList[id=1121303].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Execution
   PL:
1027. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [BeforeUse] 대상에게 [CriHurtNightStiletto]가 있으면, 대신 ‘밤의 송곳’으로 발동됨 (턴당 1회)\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1\n[WinDuel] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-12.json :: dataList[id=1121303].levelList[level=3].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [CriHurtNightStiletto], [WhenUse], [Laceration], [Vibration], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [CriHurtNightStiletto] = 깊은 상처 / Deep Wound; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [BeforeUse] If target has [CriHurtNightStiletto], activate 'The Night's Awl' instead (once per turn)\n[WhenUse] If target has 6+ ([Laceration] + [Vibration]), Coin Power +1\n[WinDuel] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
1028. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-12.json :: dataList[id=1121303].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1015 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1029. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-12.json :: dataList[id=1121303].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1013 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1030. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [HurtNightStiletto] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121303].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1121303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 1011 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1031. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [VibrationBleeding]로 [Switch_Vibration]
   źródło: Skills_personality-12.json :: dataList[id=1121303].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1121303].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationBleeding], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationBleeding] = 진동 - 과다출혈 / Tremor - Hemorrhage; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationBleeding]
   PL:
1032. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-12.json :: dataList[id=1121303].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1121303].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
1033. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 대상이 흐트러짐 상태이거나, 적(본체)의 체력이 20% 이하이거나, 대상에게 [HorrHurtNightStiletto]가 있으면, ‘메르체’ 사용
   źródło: Skills_personality-12.json :: dataList[id=1121303].levelList[level=3].coinlist[#3].coindescs[#2].desc ; dataList[id=1121303].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [HorrHurtNightStiletto]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HorrHurtNightStiletto] = 치명적인 상처 / Fatal Wound
   EN: [OnSucceedAttack] If target is Staggered, or has [HorrHurtNightStiletto], or if the enemy(Core) has 20%- HP, use 'Mercé'
   PL:
1034. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 3 — podsumowanie] [OnSucceedAttack] ‘메르체’ 사용
   źródło: Skills_personality-12.json :: dataList[id=1121303].levelList[level=3].coinlist[#3].coindescs[#2].summary ; dataList[id=1121303].levelList[level=4].coinlist[#3].coindescs[#2].summary
   (powtórzenie elementu 1023 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1035. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [BeforeUse] 대상에게 [CriHurtNightStiletto]가 있으면, 대신 ‘밤의 송곳’으로 발동됨 (턴당 1회)\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 6<style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WinDuel] <style="highlight">[Vibration] 2 부여.</style> [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-12.json :: dataList[id=1121303].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeUse], [CriHurtNightStiletto], [WhenUse], [Laceration], [Vibration], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [CriHurtNightStiletto] = 깊은 상처 / Deep Wound; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [BeforeUse] If target has [CriHurtNightStiletto], activate 'The Night's Awl' instead (once per turn)\n[WhenUse] Coin Power +1 <style="highlight">for every</style> 6 ([Laceration] + [Vibration]) on target <style="highlight">(max 2)</style>\n[WinDuel] <style="highlight">Inflict 2 [Vibration]</style> and trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
1036. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-12.json :: dataList[id=1121303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
1037. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여, <style="highlight">[Vibration] 횟수 1 증가</style>
   źródło: Skills_personality-12.json :: dataList[id=1121303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration] and <style="highlight">+1 [Vibration] Count</style>
   PL:
1038. [Umiejętność 4 (×0) (ulepszenia 2,4) — nazwa] 메르체
   źródło: Skills_personality-12.json :: dataList[id=1121305].levelList[level=2].name ; dataList[id=1121305].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Mercé
   PL:
1039. [Umiejętność 4 (×0) (ulepszenie 2) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않고, E.G.O 자원을 획득할 수 없음\n적(본체)의 잃은 체력 20%당, 코인 위력 +1 (최대 2)\n적(본체)의 체력이 20% 이하면, 피해량 +80%
   źródło: Skills_personality-12.json :: dataList[id=1121305].levelList[level=2].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills and cannot gain E.G.O resources\nCoin Power +1 for every 20% missing HP on the enemy(Core) (max 2)\nIf the enemy(Core) has 20%- HP, deal +80% damage
   PL:
1040. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [HurtNightStiletto] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121305].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1011 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1041. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않고, E.G.O 자원을 획득할 수 없음\n적(본체)의 잃은 체력 20%당, 코인 위력 +1 (최대 <style="highlight">4</style>)\n<style="highlight">적(본체)의 잃은 체력 비율만큼 <noparse>피해량 증가</noparse></style>\n- 적(본체)의 체력이 20% 이하면, <style="highlight">대신</style> 피해량 +<style="highlight">120</style>%\n<style="highlight">[WhenUse] 다음 턴에 [Agility] 1 얻음 (턴당 1회)</style>
   źródło: Skills_personality-12.json :: dataList[id=1121305].levelList[level=4].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <noparse>, </noparse>, \n, [CantDuel], [WhenUse], [Agility]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills and cannot gain E.G.O resources\nCoin Power +1 for every 20% missing HP on the enemy(Core) (max <style="highlight">4</style>)\n<style="highlight">Deal +1% damage for every 1% missing HP on the enemy(Core)</style>\n- If the enemy(Core) has 20%- HP, <style="highlight">deal +120% damage instead</style>\n<style="highlight">[WhenUse] Gain 1 [Agility] next turn (once per turn)</style>
   PL:
1042. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121305].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 716 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1043. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-12.json :: dataList[id=1121305].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 1009 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1044. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [HurtNightStiletto] 1 부여<style="highlight"></style>
   źródło: Skills_personality-12.json :: dataList[id=1121305].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [HurtNightStiletto]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HurtNightStiletto] = 상처 / Open Wound
   EN: [OnSucceedAttack] Inflict 1 [HurtNightStiletto]<style="highlight"></style>
   PL:
1045. [Umiejętność 5 (×0) (ulepszenia 3–4) — nazwa] 밤의 송곳
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=3].name ; dataList[id=1121306].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: The Night's Awl
   PL:
1046. [Umiejętność 5 (×0) (ulepszenie 3) — opis] 자신의 [Agility]과 대상의 [Binding]의 합 1당, 피해량 +10% (최대 40%)\n적(본체)의 체력이 20% 이하면, 피해량 +50%\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 4당, 코인 위력 +1 (최대 2)\n[WinDuel] [VibrationExplosion]
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=3].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [Binding], [WhenUse], [Laceration], [Vibration], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [Agility] = 신속 / Haste; [Binding] = 속박 / Bind; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: Deal +10% damage for every 1 ([Agility] on self + [Binding] on target) (max 40%)\nDeal +50% damage if the enemy(Core) has 20%- HP\n[WhenUse] Coin Power +1 for every 4 ([Laceration] + [Vibration]) on target (max 2)\n[WinDuel][VibrationExplosion]
   PL:
1047. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1121306].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 949 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1048. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1121306].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 949 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1049. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL:
1050. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1121306].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 949 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1051. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 4 부여, [Vibration] 횟수 1 증가
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration] and +1 [Vibration] Count
   PL:
1052. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1121306].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 949 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1053. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [VibrationBleeding]로 [Switch_Vibration]
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1121306].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 1031 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1054. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=3].coinlist[#3].coindescs[#2].desc ; dataList[id=1121306].levelList[level=4].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 1032 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1055. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 4, efekt 4 — opis] [OnSucceedAttack] 대상에게 [Binding]이 있으면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=3].coinlist[#3].coindescs[#3].desc ; dataList[id=1121306].levelList[level=4].coinlist[#3].coindescs[#3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If target has [Binding], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
1056. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 4, efekt 5 — opis] [OnSucceedAttack] 다음 턴에 대상의 [CriHurtNightStiletto]를 [HorrHurtNightStiletto]로 변환
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=3].coinlist[#3].coindescs[#4].desc ; dataList[id=1121306].levelList[level=4].coinlist[#3].coindescs[#4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [CriHurtNightStiletto], [HorrHurtNightStiletto]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CriHurtNightStiletto] = 깊은 상처 / Deep Wound; [HorrHurtNightStiletto] = 치명적인 상처 / Fatal Wound
   EN: [OnSucceedAttack] Convert target's [CriHurtNightStiletto] into [HorrHurtNightStiletto] next turn
   PL:
1057. [Umiejętność 5 (×0) (ulepszenie 4) — opis] 자신의 [Agility]과 대상의 [Binding]의 합 1당, 피해량 +<style="highlight">15</style>% (최대 <style="highlight">60</style>%)\n<style="highlight">대상에게 보호막이 있으면, 피해량 +30% (집중 전투일 경우, 본체 또는 부위로 판정)</style>\n<style="highlight">적(본체)의 잃은 체력 비율만큼 <noparse>피해량 증가</noparse></style>\n- 적(본체)의 체력이 20% 이하면, <style="highlight">대신</style> 피해량 +<style="highlight">100</style>%\n<style="highlight">[WhenUse] [DefenseDown] 5 부여</style>\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 4당, 코인 위력 +1 (최대 <style="highlight">3</style>)\n[WinDuel] <style="highlight">[Vibration] 4 부여.</style> [VibrationExplosion]
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=4].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <noparse>, </noparse>, \n, [Agility], [Binding], [WhenUse], [DefenseDown], [Laceration], [Vibration], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [Agility] = 신속 / Haste; [Binding] = 속박 / Bind; [WhenUse] = [사용시] / [On Use]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: Deal +<style="highlight">15</style>% damage for every 1 ([Agility] on self + [Binding] on target) (max <style="highlight">60</style>%)\n<style="highlight">If target has Shield, deal +30% damage (in Focused Encounters, the Core or Parts)</style>\n<style="highlight">Deal +1% damage for every 1% missing HP on the enemy(Core)</style>\n- If the enemy(Core) has 20%- HP, <style="highlight">deal +100% damage instead</style>\n<style="highlight">[WhenUse] Inflict 5 [DefenseDown]</style>\n[WhenUse] Coin Power +1 for every 4 ([Laceration] + [Vibration]) on target (max <style="highlight">3</style>)\n[WinDuel] <style="highlight">Inflict 4 [Vibration]</style> and trigger [VibrationExplosion]
   PL:
1058. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여, <style="highlight">[Laceration] 횟수 1 증가</style>
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and <style="highlight">+1 [Laceration] Count</style>
   PL:
1059. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 4 부여, [Vibration] 횟수 2 증가
   źródło: Skills_personality-12.json :: dataList[id=1121306].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration] and +2 [Vibration] Count
   PL:
1060. [Obrona (ulepszenia 1,4) — nazwa] 궁지에서
   źródło: Skills_personality-12.json :: dataList[id=1121304].levelList[level=1].name ; dataList[id=1121304].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 3 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Dire Straits
   PL:
1061. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] 다음 턴에 [Agility] 1 얻음 (턴당 1회)\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-12.json :: dataList[id=1121304].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [Agility], [WhenUse], [Laceration], [Vibration]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [Agility] = 신속 / Haste; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [CanDuelGuard]\n[StartBattle] Gain 1 [Agility] next turn (once per turn)\n[WhenUse] If target has 6+ ([Laceration] + [Vibration]), Coin Power +1
   PL:
1062. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-12.json :: dataList[id=1121304].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1121304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 949 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1063. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n<style="highlight">[StartBattle] 이번 턴에 ‘패밀리의 숙청인’ 효과로 발동되는 ‘메르체’의 사용 가능 횟수가 턴당 2회로 증가</style>\n[StartBattle] 다음 턴에 [Agility] 1 얻음 (턴당 1회)\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 6<style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WinDuel] <style="highlight">[Vibration] 2 부여</style>
   źródło: Skills_personality-12.json :: dataList[id=1121304].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [StartBattle], [Agility], [WhenUse], [Laceration], [Vibration], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [Agility] = 신속 / Haste; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n<style="highlight">[StartBattle] For this turn, increase the number of times 'Mercé' can be used when triggered by the effect of 'Purge Enforcer of the Famiglie' to 2 per turn</style>\n[StartBattle] Gain 1 [Agility] next turn (once per turn)\n[WhenUse] Coin Power +1 <style="highlight">for every</style> 6 ([Laceration] + [Vibration]) on target <style="highlight">(max 2)</style>\n[WinDuel] <style="highlight"> Inflict 2 [Vibration]</style>
   PL:
1064. [Pasywka bojowa (od ulepszenia 2) — nazwa] 고통 없는 자비
   źródło: Passives.json :: dataList[id=1121302].name
   limit: do 40 znaków
   EN: Painless Mercy
   PL:
1065. [Pasywka bojowa (od ulepszenia 2) — opis] 밤의 송곳 카피타노 그레고르의 ‘메르체’는 외부 효과로 재사용된 경우를 제외하고 턴당 최대 2회 사용 가능
   źródło: Passives.json :: dataList[id=1121302].desc
   limit: do 150 znaków
   EN: Unless Reused via external effects, Night Awl Capitano Gregor's Skill 'Mercé' can be used up to 2 times per turn
   PL:
1066. [Pasywka bojowa (od ulepszenia 2) — podsumowanie] '메르체' 사용
   źródło: Passives.json :: dataList[id=1121302].summary
   limit: do 120 znaków
   EN: Use 'Mercé'
   PL:
1067. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Sloth, posiadane 2× Lust) — nazwa] 패밀리의 숙청인
   źródło: Passives.json :: dataList[id=1121301].name
   limit: do 50 znaków
   EN: Purge Enforcer of the Famiglie
   PL:
1068. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Sloth, posiadane 2× Lust) — opis] 자신이 적 처치 또는 부위 파괴 시, 다음 턴에 [PenetrateResultUp] 1 얻음 (턴당 1회)\n\n기본 공격 스킬 사용 시 대상의 속도가 자신보다 느리면 속도 차이 2당, 대상에게 [Disarming] 1 부여 (턴당 최대 1)\n\n아군이 적에게 기본 공격 스킬 종료 시 적(본체)의 체력이 20% 이하인 경우, 대상에게 ‘메르체’ 사용 (턴당 1회)
   źródło: Passives.json :: dataList[id=1121301].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [PenetrateResultUp], [Disarming]
   znaczenie tagów: [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [Disarming] = 수비 위력 감소 / Defense Power Down
   EN: When this unit kills an enemy or breaks a Part, gain 1 [PenetrateResultUp] next turn (once per turn)\n\nWhen using a Base Attack Skill, if this unit's Speed is faster than the target's, inflict [Disarming] on the target for every 2 Speed difference (max 1 per turn)\n\nAfter ally Attack using Base Attack Skills, if the enemy(Core) has 20%- HP, use 'Mercé' on the target (once per turn)
   PL:
1069. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Sloth, posiadane 2× Lust) — podsumowanie] [PenetrateResultUp] 얻음\n[Disarming] 부여\n‘메르체’ 사용
   źródło: Passives.json :: dataList[id=1121301].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [PenetrateResultUp], [Disarming]
   znaczenie tagów: [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [Disarming] = 수비 위력 감소 / Defense Power Down
   EN: Gain [PenetrateResultUp]\nInflict [Disarming]\nUse 'Mercé'
   PL:
1070. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Sloth, posiadane 2× Lust) — nazwa] 패밀리의 숙청인
   źródło: Passives.json :: dataList[id=1121311].name
   (powtórzenie elementu 1067 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1071. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Sloth, posiadane 2× Lust) — opis] 자신이 적 처치 또는 부위 파괴 시, 다음 턴에 [PenetrateResultUp] 2 얻음 (턴당 1회)\n\n기본 공격 스킬 사용 시 대상의 속도가 자신보다 느리면 속도 차이 2당, 대상에게 [Disarming] 1 부여 (턴당 최대 2)\n\n아군이 적에게 기본 공격 스킬 종료 시 적(본체)의 체력이 20% 이하인 경우, 대상에게 ‘메르체’ 사용 (턴당 1회)\n- 공격 종료 시 생존한 적이 1명이면, 대상이 흐트러짐 상태일 때에도 발동
   źródło: Passives.json :: dataList[id=1121311].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: \n, [PenetrateResultUp], [Disarming]
   znaczenie tagów: [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [Disarming] = 수비 위력 감소 / Defense Power Down
   EN: When this unit kills an enemy or breaks a Part, gain 2 [PenetrateResultUp] next turn (once per turn)\n\nWhen using a Base Attack Skill, if this unit's Speed is faster than the target's, inflict [Disarming] on the target for every 2 Speed difference (max 2 per turn)\n\nAfter ally Attack using Base Attack Skills, if the enemy(Core) has 20%- HP, use 'Mercé' on the target (once per turn)\n- If there is only 1 surviving enemy after an attack, this Passive also activates when the target is Staggered
   PL:
1072. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Sloth, posiadane 2× Lust) — podsumowanie] [PenetrateResultUp] 얻음\n[Disarming] 부여\n‘메르체’ 사용
   źródło: Passives.json :: dataList[id=1121311].summary
   (powtórzenie elementu 1069 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1073. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — nazwa] 틈새 노리기
   źródło: Passives.json :: dataList[id=1121321].name
   limit: do 40 znaków
   EN: Aim for the Gap
   PL:
1074. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — opis] 속도가 가장 빠른 아군 1명이 기본 공격 스킬 사용 시 메인 타겟의 속도가 자신보다 느리면 속도 차이 3당, 대상에게 [Disarming] 1 부여 (턴당 최대 2)
   źródło: Passives.json :: dataList[id=1121321].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: [Disarming]
   znaczenie tagów: [Disarming] = 수비 위력 감소 / Defense Power Down
   EN: 1 ally with the highest Speed: When using a Base Attack Skill, if this unit's Speed is faster than the main target's, inflict [Disarming] on the target for every 3 Speed difference (max 2 per turn)
   PL:
1075. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — podsumowanie] [Disarming] 부여
   źródło: Passives.json :: dataList[id=1121321].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Disarming]
   znaczenie tagów: [Disarming] = 수비 위력 감소 / Defense Power Down
   EN: Inflict [Disarming]
   PL:
1076. [Kwestia głosowa [get_11213_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=get_11213_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1077. [Kwestia głosowa [get_11213_1] (Identity Acquisition)] 비가 그칠 무렵에는 이 골목을 영영 떠나야겠어.\n후우… 나는 아직 살고 싶거든.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=get_11213_1].dlg
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gotta leave this alley for good once the rain lets up.\n*puff* I don’t intend on getting whacked just yet.
   PL:
1078. [Kwestia głosowa [lobby_morning_11213_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=lobby_morning_11213_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1079. [Kwestia głosowa [lobby_morning_11213_1] (Morning Greeting)] …하늘이 밝아질 때까지 숙청이 끝나지 않은 건 오랜만이군. 손가락 걸기를 앞두고, 입조심 못하는 멍청이들이 꽤 늘어난 걸테지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=lobby_morning_11213_1].dlg
   limit: do 240 znaków
   EN: ... Been a while since a Purge ran past dawn. Guess there are a lot more loudmouths these days who don't know when to hold their tongues even with the Finger Bow-Bell hanging overhead.
   PL:
1080. [Kwestia głosowa [lobby_noon_11213_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=lobby_noon_11213_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1081. [Kwestia głosowa [lobby_noon_11213_1] (Afternoon Greeting)] …그래, 고맙군. 이 일은… 죽는 순간까지 침묵할 것을 맹세하지.\n숙청이라. 일선에서 뛰며 얻은 인맥이… 쓸모없진 않아서 다행이군. 미리 알았으니… 도망칠 몇 명은 살 수 있겠어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=lobby_noon_11213_1].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ... Got it. Thanks—I'm taking this one to the grave. \nA Purge, is it? Well, a small relief that the acquaintances I'd made on the job... weren't completely useless. Now that we got an early warning... let's hope some of us can make it outta here alive.
   PL:
1082. [Kwestia głosowa [lobby_night_11213_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=lobby_night_11213_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1083. [Kwestia głosowa [lobby_night_11213_1] (Evening Greeting)] 심야의 숙청을 담당하던 우리가 이제는 숙청의 대상이 되었나…\n밤이 깊었으니 초대장을 써야겠군. 어딜 가나 어둠 뿐이라면… 도시의 별이라도 길잡이 삼는 편이 나을 테지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=lobby_night_11213_1].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ironic after all those nights being in charge of Purges... now we're the ones getting clipped.\nNight's fallen—time to put that Invitation to use. If we're doomed to walk in the darkness wherever we go... might as well let the Star of the City light our way.
   PL:
1084. [Kwestia głosowa [smalltalk_11213_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=smalltalk_11213_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1085. [Kwestia głosowa [smalltalk_11213_1] (Chatter #1)] 예상치 못한 일은 아니었어. 두목은… 젊어서 그런지 불의나 호기심을 참지 못하는 사람이었거든.\n그래서 그런가. 화가 나진 않더라고. 단지, 그 사고가… 대부님의 의중을 묻는 멍청한 말 한마디였다는 건… 후우… 다시 생각해도 어이가 없군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=smalltalk_11213_1].dlg
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It's not like I didn't see it coming. I knew the Boss... was too young and rash to let an injustice slide or to remember that curiosity kills the cat.\nGuess that's why I didn't flip my lid about how it all went down, but that "accident"... it just had to be a damn fool of a question, second-guessing the Padrino’s intentions... *sigh* the more I think about it, the more it blows my mind.
   PL:
1086. [Kwestia głosowa [smalltalk_11213_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=smalltalk_11213_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1087. [Kwestia głosowa [smalltalk_11213_2] (Chatter #2)] 짝다리 짚기, 식사하면서 말하기, 한숨 쉬기, 말 끊기. 하지 말라고 그렇게 말해도… 습관이라면서 못 고치는 놈들이 몇 있었지.\n엄지 산하에서 그런 경솔하고 가벼운 태도만큼… 스스로에게 끔찍한 습관도 없는데 말이야.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=smalltalk_11213_2].dlg
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Standing crooked, talking with their mouth full, sighing, cutting off a superior mid-sentence... I told 'em all, time and again—don't do it. But there are always numbskulls who say they can't kick the habit.\nUnder the Thumb, there's no faster way to dig your own grave than reckless, sloppy "habits."
   PL:
1088. [Kwestia głosowa [smalltalk_11213_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=smalltalk_11213_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1089. [Kwestia głosowa [smalltalk_11213_3] (Chatter #3)] 남부의 숙청자 중 하나. 그게 밤의 송곳이 올라갈 가장 높은 자리였겠지. 우리 조직은 명망 높은 패밀리 출신도 아니고, 힘 있는 파벌에 몸 담지도 못했으니까.\n…허탈하군. L사 뒷골목 한자리 먹어보겠다고 개처럼 구른 결과가 고작 이거라니.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=smalltalk_11213_3].dlg
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Just one of the many Enforcers of the Purge here in the South. That would've been about the top job us Night Awls could've landed—we're not from a particularly well-known Famiglia, and we've never been a part of the more powerful factions either...\nIt doesn't matter now. We clawed like mongrel dogs to carve out a turf of our own in L Corp.'s Backstreets, and... for what?
   PL:
1090. [Kwestia głosowa [smalltalk_11213_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=smalltalk_11213_4].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1091. [Kwestia głosowa [smalltalk_11213_4] (Post-Uptie Chat 1)] 엄지의 숙청 대상이 되었다면… 괜히 고통스럽게 죽지 말고 차라리 밤의 송곳을 찾아오라고.\n우리는 그래도… 자비롭게 급소를 노려서 단번에 목숨을 끊어주거든. 도시에 그것보다 나은 죽음이 몇이나 되겠어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=smalltalk_11213_4].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If you're marked to be Purged by the Thumb, best find the Night Awls if you'd rather be spared a painful death.\nAt the very least... we'll strike you where you're sure to die, merciful and quick. In the City, that's about as good a death as you'll get.
   PL:
1092. [Kwestia głosowa [smalltalk_11213_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=smalltalk_11213_5].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1093. [Kwestia głosowa [smalltalk_11213_5] (Post-Uptie Chat 2)] 공방에서 괜찮은 원단을 구한 애송이들은… 전투 중에 꼭 공격을 피하지 않고 한 번 맞아보더군.\n목숨 아까운 줄 모르는 거지. 어지간한 고급품이 아닌 이상, 강철로 만들어졌든, 공방제 천으로 만들어졌든… 옷에는 이음새가 있기 마련이니까.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=smalltalk_11213_5].dlg
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Greenhorns who manage to get their hands on some decent Workshop-made fabric... they always gotta take a hit in a scrap, see how much it can take.\nThey don't value their lives, if you ask me. Doesn't matter if it's made of steel, or something fresh off the Workshop-floor... if it's not the best out there, clothes are bound to have seams in them.
   PL:
1094. [Kwestia głosowa [neglect_11213_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=neglect_11213_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1095. [Kwestia głosowa [neglect_11213_1] (Idle)] 후우… 이 고요함… 나쁘지 않군.\n귀를 닫고, 눈을 가리고, 침묵을 지키는 자에겐 백 년의 평화가 따르는 법이지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=neglect_11213_1].dlg
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: *puff* This quiet... it's not so bad.\nHe who is deaf, blind, and silent will live a hundred years in peace.
   PL:
1096. [Kwestia głosowa [gacksung_11213_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=gacksung_11213_1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1097. [Kwestia głosowa [gacksung_11213_1] (Uptying)] 검지, W사, 시 협회… 소문대로 다양한 기술을 사용하는군.\n하지만… 어떤 상대라도 꿰뚫을 빈틈은 있기 마련이지. 살아남을 희망이… 조금은 보일지도 모르겠어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=gacksung_11213_1].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Index, W Corp., Shi Association... They're using all kinds of techniques, just as I've heard.\nStill, whoever you're up against, there's always a gap to strike through. There's still hope... We might just come out of this alive yet.
   PL:
1098. [Kwestia głosowa [formation_11213_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=formation_11213_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1099. [Kwestia głosowa [formation_11213_1] (Deployment)] 살아서 돌아갈 수만 있다면… 무엇이든.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=formation_11213_1].dlg
   limit: do 120 znaków
   EN: Survival matters the most... I'll do anything for it.
   PL:
1100. [Kwestia głosowa [battleentry_11213_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battleentry_11213_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1101. [Kwestia głosowa [battleentry_11213_1] (Stage Entry)] 마지막까지… 발버둥칠 수밖에.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battleentry_11213_1].dlg
   limit: do 120 znaków
   EN: No choice but to keep fighting... until the very end.
   PL:
1102. [Kwestia głosowa [battle_select_11213_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_select_11213_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1103. [Kwestia głosowa [battle_select_11213_1] (Viewed in Battle)] 전장에 집중하는 게 좋겠군. 개죽음 당하기 싫다면 말이지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_select_11213_1].dlg
   limit: do 120 znaków
   EN: Stay sharp and focus on the fight if you don't want to snuff it.
   PL:
1104. [Kwestia głosowa [battle_endcommand_11213_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_endcommand_11213_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1105. [Kwestia głosowa [battle_endcommand_11213_1] (Commencing Attack)] 빠르게 처리하지.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_endcommand_11213_1].dlg
   limit: do 120 znaków
   EN: Let's deal with this quickly.
   PL:
1106. [Kwestia głosowa [battle_enemy_break_11213_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_enemy_break_11213_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1107. [Kwestia głosowa [battle_enemy_break_11213_1] (Enemy Stagger)] 여기가 네 약점인가?
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_enemy_break_11213_1].dlg
   limit: do 120 znaków
   EN: Is this your weak spot?
   PL:
1108. [Kwestia głosowa [battle_break_11213_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_break_11213_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1109. [Kwestia głosowa [battle_break_11213_1] (Staggered)] 윽…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_break_11213_1].dlg
   limit: do 120 znaków
   EN: Gah...
   PL:
1110. [Kwestia głosowa [battle_kill_11213_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_kill_11213_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1111. [Kwestia głosowa [battle_kill_11213_1] (Enemy Killed)] 빈틈투성이군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_kill_11213_1].dlg
   limit: do 120 znaków
   EN: You were full of openings.
   PL:
1112. [Kwestia głosowa [battle_dead_11213_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_dead_11213_1].desc
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1113. [Kwestia głosowa [battle_dead_11213_1] (Death)] 도망친다고… 달라질 운명은 아니었나…
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_dead_11213_1].dlg
   limit: do 120 znaków
   EN: I guess running away... did nothing to unseal our fate...
   PL:
1114. [Kwestia głosowa [choice_success_p_11213_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=choice_success_p_11213_2].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1115. [Kwestia głosowa [choice_success_p_11213_2] (Check Passed)] 더 있나? 있다면 빠르게 처리하자고.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=choice_success_p_11213_2].dlg
   limit: do 120 znaków
   EN: Anything else left? Let's deal with it fast.
   PL:
1116. [Kwestia głosowa [choice_fail_n_11213_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=choice_fail_n_11213_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1117. [Kwestia głosowa [choice_fail_n_11213_1] (Check Failed)] …노력한다고 뭐든 해결되면, 얼마나 좋겠어.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=choice_fail_n_11213_1].dlg
   limit: do 120 znaków
   EN: ... If only hard work guaranteed results.
   PL:
1118. [Kwestia głosowa [battle_clear_11213_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_clear_11213_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1119. [Kwestia głosowa [battle_clear_11213_1] (Victory Cry)] 남은 인원은 몇명이지? 움직일 수 있나?\n…돌아가면 조직원부터 다시 모으는 편이 좋겠군. 고작 이 정도 인원으로 엄지를 찾아 갔다간… 대부님께서 우리를 쓸모 없다고 판단할지도 모르니까.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_clear_11213_1].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: How many do we have left? Can you all still stand?\nWe should start recruiting more once we make it out of here. Going back to the Thumb with so few of us left... would only make us look worthless in the Capo dei Capi's eyes.
   PL:
1120. [Kwestia głosowa [battle_clear_ex_11213_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_clear_ex_11213_1].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1121. [Kwestia głosowa [battle_clear_ex_11213_1] (Extra Conditions Fulfilled)] 서두르지. 수습이 늦어지면, 여기서 살아남은 게 다 헛수고가 될 테니.\n검지의 책… 일 마무리가 나쁘지 않았어. 이걸로 숙청은 면할 수 있겠군.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_clear_ex_11213_1].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We'd better hurry up, or surviving this long will have been for nothing.\nBook of the Index, eh... Wasn't half bad—we did manage to take care of this right. With this, we won't be Purged at the very least.
   PL:
1122. [Kwestia głosowa [battle_defeat_11213_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_defeat_11213_1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1123. [Kwestia głosowa [battle_defeat_11213_1] (Defeat Wail)] 도서관으로 갈지, 뒷골목을 통해 빠져나갈지… 괜한 고민이었군…\n후우… 엄지의 숙청을 피해 도망친다 한들… 정해진 죽음에게서 벗어날 수는… 없었나.
   źródło: PersonalityVoiceDlg/Voice_Gregor_Capitano_11213.json :: dataList[id=battle_defeat_11213_1].dlg
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Library, the Backstreets... It was pointless to think about escape routes.\n*shaky breath* Trying to outrun the Purge... couldn't cheat death... in the end.
   PL:
