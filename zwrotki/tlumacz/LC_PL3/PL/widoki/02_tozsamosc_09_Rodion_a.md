# Grzesznik #09: Rodion — Tożsamości, umiejętności, pasywki i głos (część a) — Limbus Company

Kompletny zestaw kart Tożsamości postaci **Rodion** (로쟈) wraz z umiejętnościami na ulepszeniach 1–4, efektami monet, pasywkami i kwestiami głosowymi.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Grzesznik #09: Rodion (로쟈)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 로쟈
   źródło: Characters.json :: dataList[id=9].name
   limit: do 40 znaków
   EN: Rodion
   PL:
2. [Akta więźnia — nazwa] 로쟈
   źródło: IntroduceCharacter.json :: dataList[id=로쟈].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
3. [Akta więźnia — opis] 뒷골목 태생이라는 안타까운 특징이 노골적으로 드러나는 수감자입니다.\n돈을 밝히며 도박과 내기를 즐겨하므로 관리자의 세심한 주의가 필요합니다.\n지시를 내릴 때 되도 않는 윙크로 화답하거나 실없는 농담으로 맞받아치는\n경향을 보이므로 때론 관리자로서 엄한 자세를 보이는 것을 추천합니다.\n가라앉은 상태가 비주기적으로 나타날 때가 있는데 관리자님 측에서\n해줄 수 있는 방법은 없으니 조용히 기다리는 것이 효율적입니다.
   źródło: IntroduceCharacter.json :: dataList[id=로쟈].description
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The unfortunate traits of being Backstreets-born are apparent in this Sinner.\nShe loves money, gambling, and betting—so it is advised to pay close attention to her as the manager.\nShe tends to deflect orders with an unimpressive wink or a silly joke;\nwe recommend taking a stern stance at times to remind her that you are her superior.\nHer mood may be down at irregular intervals.\nThere is nothing you can do to aid her in that state, so we recommend waiting for it to pass.
   PL: Grzesznica, po której jaskrawo widać przykre piętno urodzenia w Zaułkach.\nLubi pieniądze, hazard i zakłady, dlatego wymaga baczniejszej uwagi Kierownika.\nNa polecenia ma zwyczaj odpowiadać nieudolnym mrugnięciem albo głupim żartem,\ndlatego czasem zalecamy okazać jej surowość przełożonego.\nNieregularnie popada w przygnębienie; Kierownik nie może wtedy nic\nzrobić, najskuteczniej jest spokojnie przeczekać.

## [0] LCB Sinner — Rodion — LCB 수감자
- ID Tożsamości: `10901` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 78 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Bleed

4. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10901].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL:
5. [Karta Tożsamości — nazwa] 로쟈
   źródło: Personalities.json :: dataList[id=10901].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — nazwa z tytułem] 로쟈
   źródło: Personalities.json :: dataList[id=10901].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Karta Tożsamości — opis] 로쟈의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10901].desc
   limit: do 120 znaków
   EN: Rodion’s 1st Identity
   PL:
8. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 내려찍기
   źródło: Skills.json :: dataList[id=1090101].levelList[level=1].name ; dataList[id=1090101].levelList[level=2].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Strike Down
   PL:
9. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1090101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed
   PL:
10. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1090101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL:
11. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 연속 베기
   źródło: Skills.json :: dataList[id=1090102].levelList[level=1].name ; dataList[id=1090102].levelList[level=2].name ; dataList[id=1090102].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Axe Combo
   PL:
12. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1090102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
13. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1090102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
14. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1090102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1090102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
15. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1090102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1090102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
16. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1090102].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Bleed Count
   PL:
17. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 처단
   źródło: Skills.json :: dataList[id=1090103].levelList[level=3].name ; dataList[id=1090103].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Slay
   PL:
18. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] 자신의 정신력이 0미만이면 스킬 위력 + 1
   źródło: Skills.json :: dataList[id=1090103].levelList[level=3].desc ; dataList[id=1090103].levelList[level=4].desc
   limit: do 120 znaków
   EN: Skill Power +1 when below 0 SP
   PL:
19. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 6 이상이면, 피해량 +20%
   źródło: Skills.json :: dataList[id=1090103].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1090103].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 6+ [Laceration], deal +20% damage
   PL:
20. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1090103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL:
21. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1090103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
22. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1090103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
23. [Obrona (ulepszenie 1) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1090104].levelList[level=1].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 7 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Counter
   PL:
24. [Pasywka bojowa (od ulepszenia 1, posiadane 5× Wrath) — nazwa] 단악
   źródło: Passives.json :: dataList[id=1090101].name
   limit: do 40 znaków
   EN: Split Evil
   PL:
25. [Pasywka bojowa (od ulepszenia 1, posiadane 5× Wrath) — opis] 공격 적중 시 50% 확률로 출혈 1 부여
   źródło: Passives.json :: dataList[id=1090101].desc
   limit: do 120 znaków
   EN: On hit, inflict 1 Bleed at a 50% chance.
   PL:
26. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — nazwa] 도박사
   źródło: Passives.json :: dataList[id=1090121].name
   limit: do 40 znaków
   EN: Gambler
   PL:
27. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — opis] 현재 체력이 가장 높은 아군 1명 앞면이 나온 코인의 피해량 +20%
   źródło: Passives.json :: dataList[id=1090121].desc
   limit: do 120 znaków
   EN: 1 ally with the most HP deals +20% damage with Heads Coins.
   PL:
28. [Kwestia głosowa [get_10901_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=get_10901_1].desc
   limit: do 120 znaków
   EN: Identity Acquisition
   PL:
29. [Kwestia głosowa [get_10901_1] (Identity Acquisition)] 안녕~ 로쟈야. 긴 이름도 있는데, 정 없어 보이니까 그냥 로쟈라고 불러줘~
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=get_10901_1].dlg
   limit: do 130 znaków
   EN: Hiya~ I’m Rodya. I have a longer name, but that makes things look cold, so just stick with Rodya~
   PL:
30. [Kwestia głosowa [lobby_morning_10901_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=lobby_morning_10901_1].desc
   limit: do 120 znaków
   EN: Morning Greeting
   PL:
31. [Kwestia głosowa [lobby_morning_10901_1] (Morning Greeting)] 하암~ 벌써 일어난 거야? 난 조금만 더 잘게. 누가 아침밥 안 해주려나.
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=lobby_morning_10901_1].dlg
   limit: do 120 znaków
   EN: Yawn~ Up already? I’m gonna get some more sleep. I hope someone makes me breakfast.
   PL:
32. [Kwestia głosowa [lobby_noon_10901_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=lobby_noon_10901_1].desc
   limit: do 120 znaków
   EN: Afternoon Greeting
   PL:
33. [Kwestia głosowa [lobby_noon_10901_1] (Afternoon Greeting)] 점심은 뭐 먹었어? 난 육즙이 뚝뚝 떨어지는… 고기 먹고 싶었는데, 파우스트가 안된대.
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=lobby_noon_10901_1].dlg
   limit: do 130 znaków
   EN: What’d you have for lunch? As for me, a juicy hunk of meat… was what I wanted, but Faust said no.
   PL:
34. [Kwestia głosowa [lobby_night_10901_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=lobby_night_10901_1].desc
   limit: do 120 znaków
   EN: Evening Greeting
   PL:
35. [Kwestia głosowa [lobby_night_10901_1] (Evening Greeting)] 잠 안 와? 나랑 포커 한 판 칠래? 헤즈업으로. 후훗.
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=lobby_night_10901_1].dlg
   limit: do 120 znaków
   EN: Having trouble sleeping? How about a round of poker with me? We’ll play heads-up. Fuhu.
   PL:
36. [Kwestia głosowa [smalltalk_10901_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=smalltalk_10901_1].desc
   limit: do 120 znaków
   EN: Chatter #1
   PL:
37. [Kwestia głosowa [smalltalk_10901_1] (Chatter #1)] 남들은 돈을 멀리하라고 하지만… 말도 안 되는 소리야. 돈을 숭배하는 사람은 망하지만, 나처럼 돈을 사랑하는 사람은 무조건 성공한다니까.
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=smalltalk_10901_1].dlg
   limit: do 230 znaków
   EN: People say you should shun money… but that’s a load of crap. Sure, worshipping money is a highway to disaster, but when you’re a lover of money like me, you’re set for success.
   PL:
38. [Kwestia głosowa [smalltalk_10901_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=smalltalk_10901_2].desc
   limit: do 120 znaków
   EN: Chatter #2
   PL:
39. [Kwestia głosowa [smalltalk_10901_2] (Chatter #2)] 단테, 가끔은 쉬엄쉬엄해도 될 것 같지 않아? 누구든 휴식이 필요하잖아. …그러니까 나가서 맛있는 것 좀 사 와봐. 응?
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=smalltalk_10901_2].dlg
   limit: do 190 znaków
   EN: You gotta take it easy with the work, Dante. Everyone needs a break from time to time. …Why don’t you go out and buy me some sweets, then. Hm?
   PL:
40. [Kwestia głosowa [smalltalk_10901_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=smalltalk_10901_3].desc
   limit: do 120 znaków
   EN: Chatter #3
   PL:
41. [Kwestia głosowa [smalltalk_10901_3] (Chatter #3)] 내가 제일 좋아하는 건… 군침 도는 고급스러운 고기를 베어 물면서 카드를 치는 거야. 물론 어느 게임이든 승자는 나야.
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=smalltalk_10901_3].dlg
   limit: do 160 znaków
   EN: My favorite things… Taking a bite of premium meat and playing card games. And I’ll be the winner no matter what we play.
   PL:
42. [Kwestia głosowa [smalltalk_10901_4] — sytuacja] 대화 4
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=smalltalk_10901_4].desc
   limit: do 120 znaków
   EN: Chatter #4
   PL:
43. [Kwestia głosowa [smalltalk_10901_4] (Chatter #4)] 내 고향은 엄청 추웠어. 거기에 비하면 이곳은 온실이지. 가끔은 지나치게 따뜻한 건 아닌가 싶기도 해. 단테 고향은 어땠어? 아, 그렇지… 기억이 나면 꼭 말해주기다?
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=smalltalk_10901_4].dlg
   limit: do 240 znaków
   EN: My hometown was freezing cold. This is a total greenhouse compared to that. Sometimes feels a little too warm, though. What about yours, Dante? Oh, right… Tell me when you remember, ‘kay?
   PL:
44. [Kwestia głosowa [smalltalk_10901_5] — sytuacja] 대화 5
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=smalltalk_10901_5].desc
   limit: do 120 znaków
   EN: Chatter #5
   PL:
45. [Kwestia głosowa [smalltalk_10901_5] (Chatter #5)] 가끔 단테를 보면 진짜 신기해. 어떻게 그렇게 세상을 재미 없게만 살 수 있어? 머리를 잃어버리면서 좋아하는 것들도 같이 잊어버린 거라면… 응, 그건 좀 슬프네…
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=smalltalk_10901_5].dlg
   limit: do 250 znaków
   EN: You really are an odd one, Dante, darling. How can you stand living such a boring life? Did you forget all about your favorite stuff when you lost your head? If so, that’s… Yeah, that’s kinda sad…
   PL:
46. [Kwestia głosowa [neglect_10901_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=neglect_10901_1].desc
   limit: do 120 znaków
   EN: Idle
   PL:
47. [Kwestia głosowa [neglect_10901_1] (Idle)] 단테? 맛있는 거 사러 나간 거지? 나, 기대한다?
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=neglect_10901_1].dlg
   limit: do 120 znaków
   EN: Dante? Are you out shopping? Can I count on you to get me some grub?
   PL:
48. [Kwestia głosowa [formation_10901_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=formation_10901_1].desc
   limit: do 120 znaków
   EN: Deployment
   PL:
49. [Kwestia głosowa [formation_10901_1] (Deployment)] 내가 필요해?
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=formation_10901_1].dlg
   limit: do 120 znaków
   EN: Need a hand?
   PL:
50. [Kwestia głosowa [battleentry_10901_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battleentry_10901_1].desc
   limit: do 120 znaków
   EN: Stage Entry
   PL:
51. [Kwestia głosowa [battleentry_10901_1] (Stage Entry)] 빨리 끝내고 밥 먹으러 가자구~
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battleentry_10901_1].dlg
   limit: do 120 znaków
   EN: Let’s get this done quickly and get some snackage~
   PL:
52. [Kwestia głosowa [battle_select_10901_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_select_10901_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle
   PL:
53. [Kwestia głosowa [battle_select_10901_1] (Viewed in Battle)] 뭐야? 내가 보고 싶었던 거야?
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_select_10901_1].dlg
   limit: do 120 znaków
   EN: What? Did you miss me?
   PL:
54. [Kwestia głosowa [battle_endcommand_10901_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_endcommand_10901_1].desc
   limit: do 120 znaków
   EN: Commencing Attack
   PL:
55. [Kwestia głosowa [battle_endcommand_10901_1] (Commencing Attack)] 금방 다녀올게~
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_endcommand_10901_1].dlg
   limit: do 120 znaków
   EN: Be back in a jiffy~
   PL:
56. [Kwestia głosowa [battle_enemy_break_10901_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_enemy_break_10901_1].desc
   limit: do 120 znaków
   EN: Enemy Stagger
   PL:
57. [Kwestia głosowa [battle_enemy_break_10901_1] (Enemy Stagger)] 겨우 이정도야?
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_enemy_break_10901_1].dlg
   limit: do 120 znaków
   EN: Is that all?
   PL:
58. [Kwestia głosowa [battle_break_10901_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_break_10901_1].desc
   limit: do 120 znaków
   EN: Staggered
   PL:
59. [Kwestia głosowa [battle_break_10901_1] (Staggered)] 읏…!
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_break_10901_1].dlg
   limit: do 120 znaków
   EN: Ngh…!
   PL:
60. [Kwestia głosowa [battle_kill_10901_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_kill_10901_1].desc
   limit: do 120 znaków
   EN: Enemy Killed
   PL:
61. [Kwestia głosowa [battle_kill_10901_1] (Enemy Killed)] 한 건 했다! 맛있는 거 준비해줘, 단테~
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_kill_10901_1].dlg
   limit: do 120 znaków
   EN: Score! You owe me a treat, Dante~
   PL:
62. [Kwestia głosowa [battle_allydead_10901_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_allydead_10901_1].desc
   limit: do 120 znaków
   EN: Ally Death
   PL:
63. [Kwestia głosowa [battle_allydead_10901_1] (Ally Death)] 에구… 단테, 고생이 많아~
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_allydead_10901_1].dlg
   limit: do 120 znaków
   EN: Oh, gee… You’ve got some work cut out for you, Dante~
   PL:
64. [Kwestia głosowa [choice_success_p_10901_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=choice_success_p_10901_1].desc
   limit: do 120 znaków
   EN: Check Passed
   PL:
65. [Kwestia głosowa [choice_success_p_10901_1] (Check Passed)] 다른 애들이었으면 못했을걸?
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=choice_success_p_10901_1].dlg
   limit: do 120 znaków
   EN: I bet the others woulda gone bust.
   PL:
66. [Kwestia głosowa [choice_fail_n_10901_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=choice_fail_n_10901_1].desc
   limit: do 120 znaków
   EN: Check Failed
   PL:
67. [Kwestia głosowa [choice_fail_n_10901_1] (Check Failed)] 하~ 내가 경고했잖아.
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=choice_fail_n_10901_1].dlg
   limit: do 120 znaków
   EN: Bah~ I warned ya.
   PL:
68. [Kwestia głosowa [battle_clear_10901_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_clear_10901_1].desc
   limit: do 120 znaków
   EN: Victory Cry
   PL:
69. [Kwestia głosowa [battle_clear_10901_1] (Victory Cry)] 이 정도야 뭐~ 칭찬은 말보다는… 알지?
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_clear_10901_1].dlg
   limit: do 120 znaków
   EN: Piece of cake~ Y’know I’m looking forward to a bigger reward than compliments… Ya dig?
   PL:
70. [Kwestia głosowa [battle_clear_ex_10901_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_clear_ex_10901_1].desc
   limit: do 120 znaków
   EN: Extra Conditions Fulfilled
   PL:
71. [Kwestia głosowa [battle_clear_ex_10901_1] (Extra Conditions Fulfilled)] 완~ 벽~ 하네! 오히려 살짝 싱거웠달까?
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_clear_ex_10901_1].dlg
   limit: do 120 znaków
   EN: Perrrrrfection! Heck, I might even say that was below my level.
   PL:
72. [Kwestia głosowa [battle_defeat_10901_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_defeat_10901_1].desc
   limit: do 120 znaków
   EN: Defeat Wail
   PL:
73. [Kwestia głosowa [battle_defeat_10901_1] (Defeat Wail)] 잘 좀 해보지 그랬어~ 내 탓은 아니다?
   źródło: PersonalityVoiceDlg/Voice_Rodion_LCB_10901.json :: dataList[id=battle_defeat_10901_1].dlg
   limit: do 120 znaków
   EN: You coulda done better~ Just saying, not my fault.
   PL:

## [000] Kurokumo Clan Wakashu — Rodion — 흑운회 와카슈
- ID Tożsamości: `10902` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 86 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Poise

74. [Karta Tożsamości — tytuł] 흑운회\n와카슈
   źródło: Personalities.json :: dataList[id=10902].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Kurokumo Clan\nWakashu
   PL:
75. [Karta Tożsamości — nazwa] 로쟈
   źródło: Personalities.json :: dataList[id=10902].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Karta Tożsamości — nazwa z tytułem] 로쟈
   źródło: Personalities.json :: dataList[id=10902].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [Karta Tożsamości — opis] 로쟈의 두번째 인격
   źródło: Personalities.json :: dataList[id=10902].desc
   limit: do 120 znaków
   EN: Rodion’s 2nd Identity
   PL:
78. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 날카로운 칼날
   źródło: Skills.json :: dataList[id=1090201].levelList[level=1].name ; dataList[id=1090201].levelList[level=2].name ; dataList[id=1090201].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Sharpened Blade
   PL:
79. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1090201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath]
   PL:
80. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 호흡 4 얻음
   źródło: Skills.json :: dataList[id=1090201].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 4 [Breath]
   PL:
81. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 [Breath]이 4 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1090201].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 4+ [Breath], Coin Power +2
   PL:
82. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 4 얻음
   źródło: Skills.json :: dataList[id=1090201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 4 [Breath]
   PL:
83. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 흩어지는 검격
   źródło: Skills.json :: dataList[id=1090202].levelList[level=1].name ; dataList[id=1090202].levelList[level=2].name ; dataList[id=1090202].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 6 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Scattering Slash
   PL:
84. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1090202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath]
   PL:
85. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1090202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL:
86. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1090202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1090202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1090202].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +1 [Breath] Count
   PL:
89. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1090202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1090202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
90. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1090202].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1090202].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 호흡 3 얻음
   źródło: Skills.json :: dataList[id=1090202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1090202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL:
92. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills.json :: dataList[id=1090202].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1090202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL:
93. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 호흡 횟수 2 증가\n[Breath]이 5이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1090202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count\nAt 5+ [Breath], Coin Power +2
   PL:
94. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 쾌청 베기
   źródło: Skills.json :: dataList[id=1090203].levelList[level=3].name ; dataList[id=1090203].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 7 · monety: 1 (+18)
   limit: do 40 znaków
   EN: Sky-clearing Cut
   PL:
95. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상에게 [Laceration]이 6이상있다면, 크리티컬 발동 확률 2배
   źródło: Skills.json :: dataList[id=1090203].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration], double the crit chance
   PL:
96. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 출혈 10 부여
   źródło: Skills.json :: dataList[id=1090203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1090203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict 10 Bleed
   PL:
97. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상에게 [Laceration]이 6이상있다면, 크리티컬 발동 확률 2배\n[Breath]이 10 이상이면, 크리티컬 피해량 +100%
   źródło: Skills.json :: dataList[id=1090203].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Breath]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Breath] = 호흡 / Poise
   EN: If target has 6+ [Laceration], double the crit chance\nAt 10+ [Breath], +100% Critical Damage
   PL:
98. [Obrona (ulepszenia 1,4) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1090204].levelList[level=1].name ; dataList[id=1090204].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 9 · monety: 1 (+6)
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Obrona (ulepszenie 1) — opis] [WhenUse] 보호 1 얻음
   źródło: Skills.json :: dataList[id=1090204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Protection
   PL:
100. [Obrona (ulepszenie 4) — opis] [WhenUse] 보호 1 얻음\n[WhenUse] 자신의 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1090204].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 1 Protection\n[WhenUse] Gain +2 [Breath] Count
   PL:
101. [Obrona (ulepszenia 2,4) — nazwa] 쾌청 베기
   źródło: Skills.json :: dataList[id=1090205].levelList[level=2].name ; dataList[id=1090205].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 7 · monety: 1 (+18)
   (powtórzenie elementu 94 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [Obrona (ulepszenie 2) — opis] 대상에게 [Laceration]이 6이상있다면, 크리티컬 발동 확률 2배
   źródło: Skills.json :: dataList[id=1090205].levelList[level=2].desc
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Obrona (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 출혈 10 부여
   źródło: Skills.json :: dataList[id=1090205].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1090205].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Obrona (ulepszenie 4) — opis] 대상에게 [Laceration]이 6이상있다면, 크리티컬 발동 확률 2배\n[Breath]이 10 이상이면, 크리티컬 피해량 +100%
   źródło: Skills.json :: dataList[id=1090205].levelList[level=4].desc
   (powtórzenie elementu 97 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — nazwa] 흑운도
   źródło: Passives.json :: dataList[id=1090201].name
   limit: do 40 znaków
   EN: Dark Cloud Blade
   PL:
106. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — opis] 반격 시 자신의 [Breath]이 5 이상이면 스킬 3으로 발동
   źródło: Passives.json :: dataList[id=1090201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 5+ [Breath], counter skills use Skill 3.
   PL:
107. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — nazwa] 흑운검술
   źródło: Passives.json :: dataList[id=1090221].name
   limit: do 40 znaków
   EN: Dark Cloud Swordsmanship
   PL:
108. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — opis] 속도가 가장 낮은 아군 1명 참격 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1090221].desc
   limit: do 120 znaków
   EN: 1 ally with the slowest Speed deals +10% Slash damage.
   PL:
109. [Kwestia głosowa [get_10902_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=get_10902_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
110. [Kwestia głosowa [get_10902_1] (Identity Acquisition)] 베러 왔어. 사람이던, 흐르는 물이던, 떠다니는 구름이던, 누군가의 마음이던.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=get_10902_1].dlg
   limit: do 130 znaków
   EN: I’m here to split things apart. Be it people, flowing water, drifting clouds, or a beating heart.
   PL:
111. [Kwestia głosowa [lobby_morning_10902_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=lobby_morning_10902_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [Kwestia głosowa [lobby_morning_10902_1] (Morning Greeting)] 내 시간은 밤부터 시작돼~ 그 말인즉슨… 이 시간엔 날 깨우지 말라는 소리지.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=lobby_morning_10902_1].dlg
   limit: do 120 znaków
   EN: My day starts at night~ In other words… Don’t wake me up at this hour.
   PL:
113. [Kwestia głosowa [lobby_noon_10902_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=lobby_noon_10902_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Kwestia głosowa [lobby_noon_10902_1] (Afternoon Greeting)] 단테! 점심은 어떤 거 먹었어? 나보다 더 맛있는 거 먹기만 했어봐.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=lobby_noon_10902_1].dlg
   limit: do 120 znaków
   EN: ‘Sup, Dante! What’d you have for lunch? Better not’ve had a better meal than mine.
   PL:
115. [Kwestia głosowa [lobby_night_10902_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=lobby_night_10902_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Kwestia głosowa [lobby_night_10902_1] (Evening Greeting)] 오늘은 보호비 두둑하게 벌었어~ 이걸 어디에 쓰지? 히히.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=lobby_night_10902_1].dlg
   limit: do 120 znaków
   EN: Earned a hefty sum of protection fees today~ Now where will I spend this? Heehee.
   PL:
117. [Kwestia głosowa [smalltalk_10902_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=smalltalk_10902_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Kwestia głosowa [smalltalk_10902_1] (Chatter #1)] 내 검은 매우 날카로워. 그리고 성급하지. 당신 명령을 아주 가~끔은 못 들을 수도 있다는 소리야. 내가 아니라, 내 검이. 후후.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=smalltalk_10902_1].dlg
   limit: do 190 znaków
   EN: My sword is terribly sharp. Pretty darn rash, too. I’m saying it miiiight just fail to hear your orders once in a blue moon. Not me, my sword. Fuhu.
   PL:
119. [Kwestia głosowa [smalltalk_10902_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=smalltalk_10902_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Kwestia głosowa [smalltalk_10902_2] (Chatter #2)] 있지~ 자꾸 꼬맹이가 잔소리를 해대는 거 있지? 너무 잔인하게 싸운다나 뭐라나… 내 검은 매우 날카롭고, 상대는 너무 무른 걸 어떡해. 후, 귀찮게 하질 말던가.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=smalltalk_10902_2].dlg
   limit: do 250 znaków
   EN: Heyo~ That kid just won’t stop pestering me, y’know? Says I’m being too vicious with the way I fight or whatevs… It’s not my fault my foes are too soft for my sharp sword. Whew, what a nuisance.
   PL:
121. [Kwestia głosowa [smalltalk_10902_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=smalltalk_10902_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Kwestia głosowa [smalltalk_10902_3] (Chatter #3)] 미리 말하는 거지만~ 난 지루해지면 언제든 여길 벗어날 거야. 잡을 생각은 하지 마~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=smalltalk_10902_3].dlg
   limit: do 150 znaków
   EN: Just letting you know~ I’ll be leaving this place whenever I get bored. Don’t you even think about stopping me~
   PL:
123. [Kwestia głosowa [smalltalk_10902_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=smalltalk_10902_4].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 1
   PL:
124. [Kwestia głosowa [smalltalk_10902_4] (Post-Uptie Chat 1)] 난 뒷골목이 좋아~ 적당히 더럽거든. 나같이 화려한 검술이 빛나려면 어느 정도 누추함은 필요하니까.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=smalltalk_10902_4].dlg
   limit: do 160 znaków
   EN: I like the Backstreets~ It’s the right level of grimy—a perfectly humble backdrop for letting my swank swordry shine.
   PL:
125. [Kwestia głosowa [smalltalk_10902_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=smalltalk_10902_5].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 2
   PL:
126. [Kwestia głosowa [smalltalk_10902_5] (Post-Uptie Chat 2)] 세상에는 너무 인색한 놈들이 많아. 돈을 꽁꽁 감춰두기만 하는 건 돈의 의미를 잃게 만드는 거잖아. …그러니까 의미를 되찾아 주자고.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=smalltalk_10902_5].dlg
   limit: do 230 znaków
   EN: Way too many stingy folks in the world. Keeping all that money in a vault is going against the whole point of currency. …So let’s help that stockpiled cash find its true purpose.
   PL:
127. [Kwestia głosowa [neglect_10902_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=neglect_10902_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Kwestia głosowa [neglect_10902_1] (Idle)] 으음~ 나 기다리게 하는 시간은 좀 비싼데. 감당돼?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=neglect_10902_1].dlg
   limit: do 120 znaków
   EN: Mmm~ Keepin’ me waiting is gonna be a tad bit pricey. Think you can pay out?
   PL:
129. [Kwestia głosowa [gacksung_10902_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=gacksung_10902_1].desc
   limit: do 120 znaków
   EN: Uptying
   PL:
130. [Kwestia głosowa [gacksung_10902_1] (Uptying)] 길바닥 인생한테 뭐 하나 더 해준다고 달라질 거는 없어. 어차피 계속 여기에 붙어있을 것도 아니고… 그래도, 뭐… 기분은 좋네.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=gacksung_10902_1].dlg
   limit: do 210 znaków
   EN: Ain’t gonna make a wick of difference doing a street dweller like me extra favors. It’s not like I’m here to stay… But still, I guess it’s nice to get something.
   PL:
131. [Kwestia głosowa [formation_10902_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=formation_10902_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Kwestia głosowa [formation_10902_1] (Deployment)] 수금할 시간이야~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=formation_10902_1].dlg
   limit: do 120 znaków
   EN: Time to pay up~
   PL:
133. [Kwestia głosowa [battleentry_10902_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battleentry_10902_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Kwestia głosowa [battleentry_10902_1] (Stage Entry)] 단테, 이번에는 누굴 베어버리면 되는 거야?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battleentry_10902_1].dlg
   limit: do 120 znaków
   EN: So, Dante, who do I cut down this time?
   PL:
135. [Kwestia głosowa [battle_select_10902_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_select_10902_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Kwestia głosowa [battle_select_10902_1] (Viewed in Battle)] 어머, 일할 때 건드는 건 싫은데~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_select_10902_1].dlg
   limit: do 120 znaków
   EN: My, I don’t like to be bothered when I’m working~
   PL:
137. [Kwestia głosowa [battle_endcommand_10902_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_endcommand_10902_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Kwestia głosowa [battle_endcommand_10902_1] (Commencing Attack)] 베는 맛은 있는 편이 좋은데~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_endcommand_10902_1].dlg
   limit: do 120 znaków
   EN: I like some substance in my victims~
   PL:
139. [Kwestia głosowa [battle_enemy_break_10902_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_enemy_break_10902_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Kwestia głosowa [battle_enemy_break_10902_1] (Enemy Stagger)] 그렇게 무르진 않네?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_enemy_break_10902_1].dlg
   limit: do 120 znaków
   EN: You’re not too soft, huh?
   PL:
141. [Kwestia głosowa [battle_break_10902_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_break_10902_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [Kwestia głosowa [battle_break_10902_1] (Staggered)] 흐…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_break_10902_1].dlg
   limit: do 120 znaków
   EN: Hngh…
   PL:
143. [Kwestia głosowa [battle_kill_10902_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_kill_10902_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Kwestia głosowa [battle_kill_10902_1] (Enemy Killed)] 역시, 무르네.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_kill_10902_1].dlg
   limit: do 120 znaków
   EN: Turned out mushy.
   PL:
145. [Kwestia głosowa [battle_allydead_10902_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_allydead_10902_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Kwestia głosowa [battle_allydead_10902_1] (Ally Death)] 어후. 어디 가서 힘쓴다는 말은 하지 마라~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_allydead_10902_1].dlg
   limit: do 120 znaków
   EN: Yeesh. Don’t try to convince anyone that you’re a tough one~
   PL:
147. [Kwestia głosowa [choice_success_p_10902_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=choice_success_p_10902_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Kwestia głosowa [choice_success_p_10902_1] (Check Passed)] 이런 일은 실패 해본 적이 없지!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=choice_success_p_10902_1].dlg
   limit: do 120 znaków
   EN: Never failed this kind of job!
   PL:
149. [Kwestia głosowa [choice_fail_n_10902_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=choice_fail_n_10902_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Kwestia głosowa [choice_fail_n_10902_1] (Check Failed)] 에잉~ 텄네, 텄어.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=choice_fail_n_10902_1].dlg
   limit: do 120 znaków
   EN: Nyeh~ This one’s a flub.
   PL:
151. [Kwestia głosowa [battle_clear_10902_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_clear_10902_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Kwestia głosowa [battle_clear_10902_1] (Victory Cry)] 조잡한 일이었어. 좀 더 재미난 건 없어?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_clear_10902_1].dlg
   limit: do 120 znaków
   EN: That was a pretty crude job. Don’t you have something more fun?
   PL:
153. [Kwestia głosowa [battle_clear_ex_10902_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_clear_ex_10902_1].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Kwestia głosowa [battle_clear_ex_10902_1] (Extra Conditions Fulfilled)] 역시, 내가 못 베는 건 없어.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_clear_ex_10902_1].dlg
   limit: do 120 znaków
   EN: See, there’s nothing I can’t cut.
   PL:
155. [Kwestia głosowa [battle_defeat_10902_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_defeat_10902_1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Kwestia głosowa [battle_defeat_10902_1] (Defeat Wail)] 망할 때도 있는 거지~ 내 검은 잘못 없어.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kurokumo_10902.json :: dataList[id=battle_defeat_10902_1].dlg
   limit: do 120 znaków
   EN: Things just don’t work out sometimes~ It’s not my sword’s fault.
   PL:

## [00] LCCB Assistant Manager — Rodion — LCCB 대리
- ID Tożsamości: `10903` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 1 · HP bazowe: 63 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: —

157. [Karta Tożsamości — tytuł] LCCB\n대리
   źródło: Personalities.json :: dataList[id=10903].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCCB\nAssistant Manager
   PL:
158. [Karta Tożsamości — nazwa] 로쟈
   źródło: Personalities.json :: dataList[id=10903].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Karta Tożsamości — nazwa z tytułem] 로쟈
   źródło: Personalities.json :: dataList[id=10903].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Karta Tożsamości — opis] 로쟈의 세번째 인격
   źródło: Personalities.json :: dataList[id=10903].desc
   limit: do 120 znaków
   EN: Rodion’s 3rd Identity
   PL:
161. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 타격
   źródło: Skills.json :: dataList[id=1090301].levelList[level=1].name ; dataList[id=1090301].levelList[level=2].name ; dataList[id=1090301].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Bludgeon
   PL:
162. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마비 1 부여
   źródło: Skills.json :: dataList[id=1090301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Paralyze
   PL:
163. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마비 3 부여
   źródło: Skills.json :: dataList[id=1090301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1090301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Paralyze
   PL:
164. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 조작 패널에서 다음 스킬이 타격 스킬이면 이 스킬의 코인 위력 +2
   źródło: Skills.json :: dataList[id=1090301].levelList[level=4].desc
   limit: do 120 znaków
   EN: If the next skill on the Dashboard does Blunt DMG, this skill's Coin Power +2
   PL:
165. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 찌르기
   źródło: Skills.json :: dataList[id=1090302].levelList[level=1].name ; dataList[id=1090302].levelList[level=2].name ; dataList[id=1090302].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 6 · monety: 2 (+1)
   limit: do 40 znaków
   EN: Thrust
   PL:
166. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 수비 위력 감소 2 부여
   źródło: Skills.json :: dataList[id=1090302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Defense Power Down
   PL:
167. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 수비 위력 감소 4 부여
   źródło: Skills.json :: dataList[id=1090302].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1090302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Defense Power Down
   PL:
168. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 조작 패널에서 다음 스킬이 타격 스킬이면 이 스킬의 코인 위력 +2
   źródło: Skills.json :: dataList[id=1090302].levelList[level=4].desc
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 제압
   źródło: Skills.json :: dataList[id=1090303].levelList[level=3].name ; dataList[id=1090303].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 7 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Suppress
   PL:
170. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상이 이번 턴에 공격으로 피해를 받지 않았으면 코인 위력 +2
   źródło: Skills.json :: dataList[id=1090303].levelList[level=3].desc
   limit: do 120 znaków
   EN: If target took no damage from attacks this turn, Coin Power +2
   PL:
171. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 수비 위력 감소 4 부여
   źródło: Skills.json :: dataList[id=1090303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1090303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 4 Defense Power Down
   PL:
172. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 방어 레벨 감소 4 부여
   źródło: Skills.json :: dataList[id=1090303].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1090303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Defense Level Down
   PL:
173. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 마비 3 부여
   źródło: Skills.json :: dataList[id=1090303].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1090303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상이 이번 턴에 공격으로 피해를 받지 않았으면 코인 위력 +3
   źródło: Skills.json :: dataList[id=1090303].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target took no damage from attacks this turn, Coin Power +3
   PL:
175. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1090304].levelList[level=1].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Guard
   PL:
176. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Envy) — nazwa] 방어 허물기
   źródło: Passives.json :: dataList[id=1090301].name
   limit: do 40 znaków
   EN: Breach Defense
   PL:
177. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Envy) — opis] 이번 턴에 수비스킬을 사용한 적에게 입히는 피해량 +10%
   źródło: Passives.json :: dataList[id=1090301].desc
   limit: do 120 znaków
   EN: Deal +10% damage to enemies that used defense skills this turn.
   PL:
178. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — nazwa] 브리칭
   źródło: Passives.json :: dataList[id=1090321].name
   limit: do 40 znaków
   EN: Breaching
   PL:
179. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — opis] 현재 체력이 가장 높은 아군 1명 이번 턴에 수비스킬을 사용한 적에게 입히는 피해량 +20%
   źródło: Passives.json :: dataList[id=1090321].desc
   limit: do 120 znaków
   EN: 1 ally with the most HP deals +20% damage to enemies that used defense skills this turn.
   PL:
180. [Kwestia głosowa [get_10903_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=get_10903_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Kwestia głosowa [get_10903_1] (Identity Acquisition)] 아~ 당신이야? 나한테 명령내린다던 사람이?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=get_10903_1].dlg
   limit: do 120 znaków
   EN: Oh~ So it’s you? You’re the one who’ll be bossing me around?
   PL:
182. [Kwestia głosowa [lobby_morning_10903_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=lobby_morning_10903_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Kwestia głosowa [lobby_morning_10903_1] (Morning Greeting)] 설마 이제 일어난 건 아니지? 그 시계에 자명종 기능은 없었던 거야?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=lobby_morning_10903_1].dlg
   limit: do 120 znaków
   EN: You really woke up this late? Doesn’t your head have an alarm or something?
   PL:
184. [Kwestia głosowa [lobby_noon_10903_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=lobby_noon_10903_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Kwestia głosowa [lobby_noon_10903_1] (Afternoon Greeting)] 체력 단련하기 적당한 날씨네. 거기 계속 서 있을 거야? 뭐, 구경하고 싶으면 하던가.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=lobby_noon_10903_1].dlg
   limit: do 140 znaków
   EN: Weather’s just right for some exercise. Are you gonna stand there and watch? Well, go right on ahead then.
   PL:
186. [Kwestia głosowa [lobby_night_10903_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=lobby_night_10903_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Kwestia głosowa [lobby_night_10903_1] (Evening Greeting)] 고요한 밤이야. 달빛도 적고… 잠입하기에 딱 적당하지.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=lobby_night_10903_1].dlg
   limit: do 120 znaków
   EN: A quiet night. Moon’s not too bright… Perfect for infiltration.
   PL:
188. [Kwestia głosowa [smalltalk_10903_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=smalltalk_10903_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Kwestia głosowa [smalltalk_10903_1] (Chatter #1)] 내가 와준 걸 감사히 여겨야 할 거야. 나는 꽤 우수하거든.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=smalltalk_10903_1].dlg
   limit: do 120 znaków
   EN: You should be grateful that I joined you. You’re gabbing with a skilled worker here.
   PL:
190. [Kwestia głosowa [smalltalk_10903_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=smalltalk_10903_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Kwestia głosowa [smalltalk_10903_2] (Chatter #2)] 여기 애들 말이야~ 나랑 너무 수준 안 맞아. 특히, 그 툭하면 소리 지르는 애 말이야. 그거 히스테릭 아니야?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=smalltalk_10903_2].dlg
   limit: do 160 znaków
   EN: Gotta say~ The crew here is way below my class. Especially that one who screams all the time—ain’t that a sign of hysteria?
   PL:
192. [Kwestia głosowa [smalltalk_10903_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=smalltalk_10903_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Kwestia głosowa [smalltalk_10903_3] (Chatter #3)] 길게 얘기할 거 없어. 우리가 갈 목적지, 처리해야 할 적만 이야기해. 나머진 내가 다 알아서 할 테니.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=smalltalk_10903_3].dlg
   limit: do 140 znaków
   EN: No need to make it long. Just tell me where to go and what to deal with. I’ll make sure to handle the rest.
   PL:
194. [Kwestia głosowa [smalltalk_10903_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=smalltalk_10903_4].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Kwestia głosowa [smalltalk_10903_4] (Post-Uptie Chat 1)] 나도 처음부터 마냥 자신만만한 건 아니었어. …그래야만 하니까 어느 순간 변한 거지.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=smalltalk_10903_4].dlg
   limit: do 120 znaków
   EN: I wasn’t this confident at the start. …I just had to become like this.
   PL:
196. [Kwestia głosowa [smalltalk_10903_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=smalltalk_10903_5].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Kwestia głosowa [smalltalk_10903_5] (Post-Uptie Chat 2)] 사전관측과는 따지고 보면 버리는 패 같은 거야. 위험한 데에다가 쉽게 쉽게 던져버린다고. 그러니까 혼자서 5과씩이나 존재하는 거지… 뭐, 돈은 잘 주지만.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=smalltalk_10903_5].dlg
   limit: do 260 znaków
   EN: The Preliminary Observation Department’s damn expendable if we’re being real. They toss staff into danger all willy-nilly. No wonder it’s got five whole sections… Well, does pay well for what it’s worth.
   PL:
198. [Kwestia głosowa [neglect_10903_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=neglect_10903_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Kwestia głosowa [neglect_10903_1] (Idle)] 한가한가 봐? 쏘다닐 시간도 있고. 그럴 시간에 보고서 정리나 도와줘.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=neglect_10903_1].dlg
   limit: do 150 znaków
   EN: Got a lot of free time on your hands, huh? Why don’tcha quit loitering and come help me document these instead, hun.
   PL:
200. [Kwestia głosowa [gacksung_10903_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=gacksung_10903_1].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Kwestia głosowa [gacksung_10903_1] (Uptying)] 드디어 승진하는 거야? 보상은? 연봉 인상? 애프터 팀 이전? …둘 다 아니라고? 에잉.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=gacksung_10903_1].dlg
   limit: do 130 znaków
   EN: A promotion at last? What’s on the table? A raise? Transfer to the After Team? …Neither? Phooey.
   PL:
202. [Kwestia głosowa [formation_10903_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=formation_10903_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Kwestia głosowa [formation_10903_1] (Deployment)] 에구. 작전 호출~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=formation_10903_1].dlg
   limit: do 120 znaków
   EN: Ah, geez. Reporting in~
   PL:
204. [Kwestia głosowa [battleentry_10903_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battleentry_10903_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Kwestia głosowa [battleentry_10903_1] (Stage Entry)] 네, 네. 작전 지역으로 이동 중~ 교신 끝!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battleentry_10903_1].dlg
   limit: do 120 znaków
   EN: Yeah, yeah. Heading to the mission area~ Rodya out!
   PL:
206. [Kwestia głosowa [battle_select_10903_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_select_10903_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Kwestia głosowa [battle_select_10903_1] (Viewed in Battle)] 응? 뭐 필요한 거 있어?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_select_10903_1].dlg
   limit: do 120 znaków
   EN: Hm? Ya need something?
   PL:
208. [Kwestia głosowa [battle_endcommand_10903_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_endcommand_10903_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Kwestia głosowa [battle_endcommand_10903_1] (Commencing Attack)] 로쟈, 교전 시작!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_endcommand_10903_1].dlg
   limit: do 120 znaków
   EN: Rodya, engaging enemy forces!
   PL:
210. [Kwestia głosowa [battle_enemy_break_10903_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_enemy_break_10903_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Kwestia głosowa [battle_enemy_break_10903_1] (Enemy Stagger)] 목표, 일시 무력화.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_enemy_break_10903_1].dlg
   limit: do 120 znaków
   EN: Target’s incapacitated.
   PL:
212. [Kwestia głosowa [battle_break_10903_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_break_10903_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Kwestia głosowa [battle_break_10903_1] (Staggered)] 칫…!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_break_10903_1].dlg
   limit: do 120 znaków
   EN: Tch…!
   PL:
214. [Kwestia głosowa [battle_kill_10903_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_kill_10903_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Kwestia głosowa [battle_kill_10903_1] (Enemy Killed)] 목표, 완전 무력화!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_kill_10903_1].dlg
   limit: do 120 znaków
   EN: Target neutralization confirmed!
   PL:
216. [Kwestia głosowa [battle_allydead_10903_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_allydead_10903_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Kwestia głosowa [battle_allydead_10903_1] (Ally Death)] 에잉, 부상 발생! …부상 정도가 아닌가?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_allydead_10903_1].dlg
   limit: do 120 znaków
   EN: Shoot, we’ve got an injured unit! …Or even worse?
   PL:
218. [Kwestia głosowa [choice_success_p_10903_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=choice_success_p_10903_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Kwestia głosowa [choice_success_p_10903_1] (Check Passed)] 역시, 빨간 전선이 정답이었어!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=choice_success_p_10903_1].dlg
   limit: do 120 znaków
   EN: Had a gut feeling it was the red wire!
   PL:
220. [Kwestia głosowa [choice_fail_n_10903_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=choice_fail_n_10903_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Kwestia głosowa [choice_fail_n_10903_1] (Check Failed)] 음… 빨간 전선을 잘랐어야 했나…?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=choice_fail_n_10903_1].dlg
   limit: do 120 znaków
   EN: Hmm… Was I supposed to cut the red wire…?
   PL:
222. [Kwestia głosowa [battle_clear_10903_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_clear_10903_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Kwestia głosowa [battle_clear_10903_1] (Victory Cry)] 아, 아. 관측 완료~ 뭐가 이렇게 시시해?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_clear_10903_1].dlg
   limit: do 120 znaków
   EN: Ahh, ahh. Observation complete~ Isn’t this too much of a cakewalk?
   PL:
224. [Kwestia głosowa [battle_clear_ex_10903_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_clear_ex_10903_1].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Kwestia głosowa [battle_clear_ex_10903_1] (Extra Conditions Fulfilled)] 임무 목표, 완전 해결! 이제 복귀할게~ 교신 끝!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_clear_ex_10903_1].dlg
   limit: do 120 znaków
   EN: Mission objectives all met! Returning to base now~ Rodya out!
   PL:
226. [Kwestia głosowa [battle_defeat_10903_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_defeat_10903_1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Kwestia głosowa [battle_defeat_10903_1] (Defeat Wail)] 하… 임무 실패. 쯧, 기분 잡치네.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Epi_10903.json :: dataList[id=battle_defeat_10903_1].dlg
   limit: do 120 znaków
   EN: Pah… Mission failed. Tsk, talk about a downer.
   PL:

## [00] N Corp. Mittelhammer — Rodion — N사 중간 망치
- ID Tożsamości: `10904` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 1 · HP bazowe: 69 · szybkość: 2–6 / 2–7 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed

228. [Karta Tożsamości — tytuł] N사\n중간 망치
   źródło: Personalities.json :: dataList[id=10904].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: N Corp.\nMittelhammer
   PL:
229. [Karta Tożsamości — nazwa] 로쟈
   źródło: Personalities.json :: dataList[id=10904].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Karta Tożsamości — nazwa z tytułem] 로쟈
   źródło: Personalities.json :: dataList[id=10904].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Karta Tożsamości — opis] 로쟈의 네번째 인격
   źródło: Personalities.json :: dataList[id=10904].desc
   limit: do 120 znaków
   EN: Rodion’s 4th Identity
   PL:
232. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 충실한 못질
   źródło: Skills.json :: dataList[id=1090401].levelList[level=1].name ; dataList[id=1090401].levelList[level=2].name ; dataList[id=1090401].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Devoted Hammering
   PL:
233. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1090401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1090401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1090401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1090401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1090401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1090401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 못이 있을 때, 못 1 부여
   źródło: Skills.json :: dataList[id=1090401].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Nails, inflict 1 Nails
   PL:
238. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 못이 있을 때, 못 1 부여
   źródło: Skills.json :: dataList[id=1090401].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 광적인 정화
   źródło: Skills.json :: dataList[id=1090402].levelList[level=1].name ; dataList[id=1090402].levelList[level=2].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 6 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Zealous Purge
   PL:
240. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 못 1 부여
   źródło: Skills.json :: dataList[id=1090402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1090402].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Nails next turn
   PL:
241. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — podsumowanie] [OnSucceedAttack] 다음 턴에 못 1 부여
   źródło: Skills.json :: dataList[id=1090402].levelList[level=1].coinlist[#0].coindescs[#0].summary ; dataList[id=1090402].levelList[level=2].coinlist[#0].coindescs[#0].summary
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills.json :: dataList[id=1090402].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1090402].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Paralyze next turn
   PL:
243. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WinDuel] 다음 턴에 광신 1 얻음
   źródło: Skills.json :: dataList[id=1090402].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 1 Fanatic next turn
   PL:
244. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 철의 단죄
   źródło: Skills.json :: dataList[id=1090403].levelList[level=3].name ; dataList[id=1090403].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Ironclad Retribution
   PL:
245. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신에게 광신이 있으면 피해량 +15%
   źródło: Skills.json :: dataList[id=1090403].levelList[level=3].desc
   limit: do 120 znaków
   EN: +15% Damage while this unit is Fanatic
   PL:
246. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1090403].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1090403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1090403].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1090403].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신에게 광신이 있으면 피해량 +15%\n파티의 생존한 N사 광신도 수당 피해량 +5%
   źródło: Skills.json :: dataList[id=1090403].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If this unit is Fanatic, deal +15% damage\nDeal +5% damage for each 'N Corp. Fanatic' present in the party
   PL:
249. [Obrona (ulepszenia 1,4) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1090404].levelList[level=1].name ; dataList[id=1090404].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 7 · monety: 1 (+6)
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 못 1 부여
   źródło: Skills.json :: dataList[id=1090404].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Nails
   PL:
251. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Wrath) — nazwa] 처단의 기쁨
   źródło: Passives.json :: dataList[id=1090401].name
   limit: do 40 znaków
   EN: Joy of Execution
   PL:
252. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Wrath) — opis] 적이 사망하면 다음 턴 시작 시 신속 1, 피해량 증가 1을 얻음. 자신이 적을 처치한 경우 광신 1을 얻음.(턴 당 1회 발동)
   źródło: Passives.json :: dataList[id=1090401].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: After an enemy is defeated, gain 1 [Agility] and 1 Damage Up next turn.\nIf this unit defeated an enemy, also gain 1 Fanatic. (Once per turn.)
   PL:
253. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Wrath) — nazwa] 차오르는 신앙
   źródło: Passives.json :: dataList[id=1090421].name
   limit: do 40 znaków
   EN: Rising Faith
   PL:
254. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Wrath) — opis] 적이 사망하면 정신력이 가장 높은 아군 1명이 다음 턴에 신속 1, 피해량 증가 1을 얻음 (턴 당 1회 발동)
   źródło: Passives.json :: dataList[id=1090421].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: After an enemy is defeated, apply 1 [Agility] and 1 Damage Up next turn to the ally with the most SP. (Once per turn.)
   PL:
255. [Kwestia głosowa [get_10904_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=get_10904_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Kwestia głosowa [get_10904_1] (Identity Acquisition)] 드디어, 저를 쓰시는군요…! 우훗, 후회하지 않으실 겁니다.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=get_10904_1].dlg
   limit: do 120 znaków
   EN: You’ve decided to use me at last…! Ufu, you certainly won’t regret it.
   PL:
257. [Kwestia głosowa [lobby_morning_10904_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=lobby_morning_10904_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Kwestia głosowa [lobby_morning_10904_1] (Morning Greeting)] 쥐는 자께서 하시는 아침연설은 언제나 최고입니다… 당신도 듣겠어요?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=lobby_morning_10904_1].dlg
   limit: do 140 znaków
   EN: The morning sermons given by the One Who Grips never fail to fascinate me… Would you like to hear some, too?
   PL:
259. [Kwestia głosowa [lobby_noon_10904_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=lobby_noon_10904_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Kwestia głosowa [lobby_noon_10904_1] (Afternoon Greeting)] 식사는 맛있게 하셨나요? 저요? 저는, 가장 순수한 상태를 만들기 위해 단식을 수행하는 중이죠.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=lobby_noon_10904_1].dlg
   limit: do 120 znaków
   EN: Have you enjoyed your meal? Oh, me? For myself, I am fasting to attain my purest state.
   PL:
261. [Kwestia głosowa [lobby_night_10904_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=lobby_night_10904_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Kwestia głosowa [lobby_night_10904_1] (Evening Greeting)] 오늘 정화할 지역은… 아, 당신이군요? 오늘은 정화가 있는 날이라 좀 바빠요. 다음에 이야기하죠. 후후.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=lobby_night_10904_1].dlg
   limit: do 190 znaków
   EN: Let’s see, the area to purify today is… Oh, you’re here. I’m rather busy tonight. Got some purification to do, you see, so let’s talk later. Fuhu.
   PL:
263. [Kwestia głosowa [smalltalk_10904_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=smalltalk_10904_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Kwestia głosowa [smalltalk_10904_1] (Chatter #1)] 쥐는 자… 쥐는 자께서 그것을 원하므로…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=smalltalk_10904_1].dlg
   limit: do 120 znaków
   EN: O One Who Grips… For the One Who Grips so desires it…
   PL:
265. [Kwestia głosowa [smalltalk_10904_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=smalltalk_10904_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Kwestia głosowa [smalltalk_10904_2] (Chatter #2)] 의체… 그런걸 왜 다는지 모르겠네요. 팔이 잘린 사람은 어떡하냐고요? 푸흣, 그야 잘려나갔다면 그 순간의 고통을 즐겨야지, 뒷일을 왜 걱정하나요?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=smalltalk_10904_2].dlg
   limit: do 270 znaków
   EN: Prosthetics… I dunno why anyone would slap on such things. “What should someone whose arm got lopped off do, then?” Pfh, I mean, can’t you just savor the pain of the moment? Why worry about what comes after?
   PL:
267. [Kwestia głosowa [smalltalk_10904_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=smalltalk_10904_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Kwestia głosowa [smalltalk_10904_3] (Chatter #3)] 저는 중간 망치가 된 지 얼마 안 되었답니다. 작은 것들 중에서 가장 신앙심이 뛰어나서 그렇게 된 것이죠! 후훗, 스스로가 너무 자랑스러워요…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=smalltalk_10904_3].dlg
   limit: do 200 znaków
   EN: I became a Mittelhammer pretty recently. I earned it for being the most faithful among all the little Klein ones! Fuhu, I am so dang proud of myself…
   PL:
269. [Kwestia głosowa [smalltalk_10904_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=smalltalk_10904_4].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [Kwestia głosowa [smalltalk_10904_4] (Post-Uptie Chat 1)] 당신… 당신도 이단인가요? 그 시계는… 아, 가면이라구요? 아하하, 나 참… 큰일날 뻔했잖아요. 이제 조금 친해졌는데, 못에 꿰어버릴 뻔했잖아요.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=smalltalk_10904_4].dlg
   limit: do 210 znaków
   EN: You… Are you a heretic? That clock— Oh, just a mask? Ahaha, got it… This could’ve been a real mess. I was this close to piercing my new acquaintance with a nail.
   PL:
271. [Kwestia głosowa [smalltalk_10904_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=smalltalk_10904_5].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Kwestia głosowa [smalltalk_10904_5] (Post-Uptie Chat 2)] 후훗, 크흐흣…! 이단놈들을 꿰, 꿰뚫을 수록… 내가 온전해지는 것만 같아…! …흐흠. 언제부터 거기 있었죠? 당신에게 보이기 적절한 모습은 아니었네요.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=smalltalk_10904_5].dlg
   limit: do 230 znaków
   EN: Fuhu, kuhuhu…! With each heretic I p-pierce… I feel myself becoming more and more whole…! …Ahem. How long were you there? That wasn’t exactly appropriate behavior to show you.
   PL:
273. [Kwestia głosowa [neglect_10904_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=neglect_10904_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Kwestia głosowa [neglect_10904_1] (Idle)] …3장 9절. 쥐는 자께서 망치들을 부르시며… 아, 저는 신경쓰지 마세요. 교리를 읽는 중이니.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=neglect_10904_1].dlg
   limit: do 150 znaków
   EN: …In 3:9 it states, “The One Who Grips called their hammers…” Oh, don’t mind me. I’m just studying my doctrines.
   PL:
275. [Kwestia głosowa [gacksung_10904_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=gacksung_10904_1].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Kwestia głosowa [gacksung_10904_1] (Uptying)] 반드시, 반드시! 부름에 보답할 것입니다… 후훗!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=gacksung_10904_1].dlg
   limit: do 120 znaków
   EN: I swear, I swear to you! I will return this favor… Fuhu!
   PL:
277. [Kwestia głosowa [formation_10904_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=formation_10904_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Kwestia głosowa [formation_10904_1] (Deployment)] 기다리고 있었죠.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=formation_10904_1].dlg
   limit: do 120 znaków
   EN: I have been waiting.
   PL:
279. [Kwestia głosowa [battleentry_10904_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battleentry_10904_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Kwestia głosowa [battleentry_10904_1] (Stage Entry)] 이단에게… 철의 단죄를.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battleentry_10904_1].dlg
   limit: do 120 znaków
   EN: The heretics… shall be punished by steel.
   PL:
281. [Kwestia głosowa [battle_select_10904_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_select_10904_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Kwestia głosowa [battle_select_10904_1] (Viewed in Battle)] 부르셨나요?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_select_10904_1].dlg
   limit: do 120 znaków
   EN: Did you call for me?
   PL:
283. [Kwestia głosowa [battle_endcommand_10904_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_endcommand_10904_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Kwestia głosowa [battle_endcommand_10904_1] (Commencing Attack)] 정화!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_endcommand_10904_1].dlg
   limit: do 120 znaków
   EN: Purge!
   PL:
285. [Kwestia głosowa [battle_enemy_break_10904_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_enemy_break_10904_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Kwestia głosowa [battle_enemy_break_10904_1] (Enemy Stagger)] 이단이 휘청거리는군.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_enemy_break_10904_1].dlg
   limit: do 120 znaków
   EN: The heretic falters.
   PL:
287. [Kwestia głosowa [battle_break_10904_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_break_10904_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Kwestia głosowa [battle_break_10904_1] (Staggered)] 약해빠져서는!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_break_10904_1].dlg
   limit: do 120 znaków
   EN: Such weakness!
   PL:
289. [Kwestia głosowa [battle_kill_10904_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_kill_10904_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Kwestia głosowa [battle_kill_10904_1] (Enemy Killed)] 죽음으로 참회하라.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_kill_10904_1].dlg
   limit: do 120 znaków
   EN: You will repent with your death.
   PL:
291. [Kwestia głosowa [battle_dead_10904_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_dead_10904_1].desc
   limit: do 120 znaków
   EN: Death
   PL:
292. [Kwestia głosowa [battle_dead_10904_1] (Death)] 이럴… 리가…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_dead_10904_1].dlg
   limit: do 120 znaków
   EN: This… can’t be…
   PL:
293. [Kwestia głosowa [choice_success_p_10904_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=choice_success_p_10904_2].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Kwestia głosowa [choice_success_p_10904_2] (Check Passed)] 신임에 보답했죠. 후훗.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=choice_success_p_10904_2].dlg
   limit: do 120 znaków
   EN: I answered your trust. Fuhu.
   PL:
295. [Kwestia głosowa [choice_fail_n_10904_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=choice_fail_n_10904_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Kwestia głosowa [choice_fail_n_10904_1] (Check Failed)] …처음부터 다시 공부하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=choice_fail_n_10904_1].dlg
   limit: do 120 znaków
   EN: …I will study again from the beginning.
   PL:
297. [Kwestia głosowa [battle_clear_10904_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_clear_10904_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Kwestia głosowa [battle_clear_10904_1] (Victory Cry)] 신앙의 승리죠.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_clear_10904_1].dlg
   limit: do 120 znaków
   EN: A victory to faith.
   PL:
299. [Kwestia głosowa [battle_clear_ex_10904_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_clear_ex_10904_1].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Kwestia głosowa [battle_clear_ex_10904_1] (Extra Conditions Fulfilled)] 아하핫! 이, 이걸로 나는 더 높은 자리로…!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_clear_ex_10904_1].dlg
   limit: do 120 znaków
   EN: Ahaha! W-With this, I shall be exalted to an even higher place…!
   PL:
301. [Kwestia głosowa [battle_defeat_10904_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_defeat_10904_1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Kwestia głosowa [battle_defeat_10904_1] (Defeat Wail)] 이… 치욕… 절대 잊지 않을 거야…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Ncorp_10904.json :: dataList[id=battle_defeat_10904_1].dlg
   limit: do 120 znaków
   EN: This… humiliation… will not be forgotten…
   PL:

## [000] Rosespanner Workshop Rep — Rodion — 장미스패너 공방 대표
- ID Tożsamości: `10905` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 2 · HP bazowe: 73 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Tremor, Charge

303. [Karta Tożsamości — tytuł] 장미스패너 공방\n대표
   źródło: Personalities.json :: dataList[id=10905].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rosespanner Workshop\nRep
   PL:
304. [Karta Tożsamości — nazwa] 로쟈
   źródło: Personalities.json :: dataList[id=10905].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Karta Tożsamości — nazwa z tytułem] 로쟈
   źródło: Personalities.json :: dataList[id=10905].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Karta Tożsamości — opis] 로쟈의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10905].desc
   limit: do 120 znaków
   EN: Rodion’s 5th Identity
   PL:
307. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 시동 걸기
   źródło: Skills.json :: dataList[id=1090501].levelList[level=1].name ; dataList[id=1090501].levelList[level=2].name ; dataList[id=1090501].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Rev Up
   PL:
308. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1090501].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1090501].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1090501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 1 [Vibration]
   PL:
309. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 충전 횟수 4 증가
   źródło: Skills.json :: dataList[id=1090501].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1090501].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1090501].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +4 Charge Count
   PL:
310. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1090501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict +1 [Vibration] Count
   PL:
311. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1090501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1090501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL:
312. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1090501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Charge Count
   PL:
313. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 진동압착
   źródło: Skills.json :: dataList[id=1090502].levelList[level=1].name ; dataList[id=1090502].levelList[level=2].name ; dataList[id=1090502].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 6 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Vibration Compression
   PL:
314. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1090502].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1090502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1090502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여\n자신의 충전 횟수가 3 이상이면, 앞면이 나올 때마다 이 코인 재사용 (최대 2회)\n이 코인이 2회 재사용된 경우, 진동 부여 후 진동 폭발\n진동 폭발 시 진동 횟수 1 감소
   źródło: Skills.json :: dataList[id=1090502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Inflict 2 [Vibration]\nAt 3+ Charge Count, reuse this Coin if it lands Heads (Up to 2 times)\nIf the Coin is reused twice, inflict [Vibration], then trigger [VibrationExplosion]\nAfter [VibrationExplosion], reduce [Vibration] Count by 1
   PL:
316. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — podsumowanie] [OnSucceedAttack] 진동 폭발.\n조건 만족 시 코인 재사용. 재사용 시 부여 진동 +2.\n2회 재사용 시 진동 폭발 후 진동 횟수 감소
   źródło: Skills.json :: dataList[id=1090502].levelList[level=1].coinlist[#1].coindescs[#0].summary ; dataList[id=1090502].levelList[level=2].coinlist[#1].coindescs[#0].summary
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion].\nReuse Coin if conditions are met; Inflict +2 [Vibration] if reused.\nIf the Coin is reused twice, trigger [VibrationExplosion], then reduce [Vibration] Count
   PL:
317. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여\n자신의 충전 횟수가 3 이상이면, 앞면이 나올 때마다 이 코인 재사용 (최대 2회)\n재사용 시마다 부여하는 진동 + 2\n이 코인이 2회 재사용된 경우, 진동 부여 후 진동 폭발\n진동 폭발 시 진동 횟수 1 감소
   źródło: Skills.json :: dataList[id=1090502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1090502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Inflict 2 [Vibration]\nAt 3+ Charge Count, reuse this Coin if it lands Heads (Up to 2 times)\nInflict 2 more [Vibration] each time the Coin is reused\nIf the Coin is reused twice, inflict [Vibration], then trigger [VibrationExplosion]\nAfter [VibrationExplosion], reduce [Vibration] Count by 1
   PL:
318. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 진동 횟수가 10 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1090502].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 10+ [Vibration] Count, Coin Power +1
   PL:
319. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — podsumowanie] [OnSucceedAttack] 진동 폭발.\n조건 만족 시 코인 재사용. 재사용 시 부여 진동 +2.\n2회 재사용 시 진동 폭발 후 진동 횟수 감소
   źródło: Skills.json :: dataList[id=1090502].levelList[level=4].coinlist[#1].coindescs[#0].summary
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]\nReuse Coin if conditions are met; Inflict +2 [Vibration] if reused.\nIf the Coin is reused twice, trigger [VibrationExplosion], then reduce [Vibration] Count
   PL:
320. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 한탕 해볼까
   źródło: Skills.json :: dataList[id=1090503].levelList[level=3].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Let’s Rack Up Some Scores
   PL:
321. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 충전 횟수 6 증가
   źródło: Skills.json :: dataList[id=1090503].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +6 Charge Count
   PL:
322. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 2 증가
   źródło: Skills.json :: dataList[id=1090503].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
323. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills.json :: dataList[id=1090503].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 2 [Vibration]
   PL:
324. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 진동 폭발.\n진동 폭발 시 진동 횟수 1 감소
   źródło: Skills.json :: dataList[id=1090503].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion].\nAfter [VibrationExplosion], reduce [Vibration] Count by 1
   PL:
325. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 폭발.\n진동 폭발 시 진동 횟수 1 감소
   źródło: Skills.json :: dataList[id=1090503].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상이 흐트러짐 상태면 피해량의 25%만큼 추가 피해
   źródło: Skills.json :: dataList[id=1090503].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target is Staggered, deal 25% of damage dealt as bonus damage
   PL:
327. [Obrona (ulepszenie 1) — nazwa] 예열
   źródło: Skills.json :: dataList[id=1090504].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Preheat
   PL:
328. [Obrona (ulepszenie 1) — opis] [StartBattle] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1090504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain +2 Charge Count
   PL:
329. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — nazwa] 빠른 퇴근을 위하여~
   źródło: Passives.json :: dataList[id=1090501].name
   limit: do 40 znaków
   EN: Here’s to Getting Off Early~
   PL:
330. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — opis] [VibrationExplosion] 시 충전 횟수 3을 소모하여, [VibrationExplosion]의 흐트러짐 피해량 +40%\n[VibrationExplosion] 발동 시 다음 턴에 신속 1, 타격 피해량 증가 1을 얻음
   źródło: Passives.json :: dataList[id=1090501].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationExplosion], [Agility]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Agility] = 신속 / Haste
   EN: On [VibrationExplosion], spend 3 Charge Count to increase the Stagger Threshold raise by +40%.\nAfter triggering [VibrationExplosion], gain 1 [Agility] and 1 Blunt DMG Up next turn.
   PL:
331. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — nazwa] 공진 스패너
   źródło: Passives.json :: dataList[id=1090521].name
   limit: do 40 znaków
   EN: Resonant Spanner
   PL:
332. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — opis] 속도가 가장 느린 아군 1명이 [VibrationExplosion]로 입히는 흐트러짐 피해량 +20%
   źródło: Passives.json :: dataList[id=1090521].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: When 1 ally with the slowest Speed triggers [VibrationExplosion], increase the Stagger Threshold raise by +20%.
   PL:
333. [Kwestia głosowa [get_10905_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=get_10905_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Kwestia głosowa [get_10905_1] (Identity Acquisition)] 안녕, 안녕~ 장미스패너 공방 대표, 로쟈야~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=get_10905_1].dlg
   limit: do 120 znaków
   EN: Hello, privyet~ Presenting the rep of Rosespanner Workshop, I’m Rodya~
   PL:
335. [Kwestia głosowa [lobby_morning_10905_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=lobby_morning_10905_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Kwestia głosowa [lobby_morning_10905_1] (Morning Greeting)] 흐암… 쉬엄쉬엄해~ 커피도 좀 타서 마시고. 아침부터 너무 힘 빼지 말자고~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=lobby_morning_10905_1].dlg
   limit: do 140 znaków
   EN: Yaaawn… Take it easy, baby~ Get some coffee if you wanna. No need to wear yourself out so early in the morn~
   PL:
337. [Kwestia głosowa [lobby_noon_10905_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=lobby_noon_10905_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Kwestia głosowa [lobby_noon_10905_1] (Afternoon Greeting)] 왔어? 이거 봐봐! 또~ 따버렸지 뭐야~ 점심시간에 카드 쳐서 버는게 일주일 벌이보다 많다니까~\n…흑흑.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=lobby_noon_10905_1].dlg
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You’re here? Check this out! I did it~ Won big again~ I earn more from playing card games during lunch than I do with a week’s work of running this joint~\n…Sniffle.
   PL:
339. [Kwestia głosowa [lobby_night_10905_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=lobby_night_10905_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Kwestia głosowa [lobby_night_10905_1] (Evening Greeting)] 나 먼저 퇴근할게~ 뭐야, 야근이야? 어이구… 고생이네. 수당은 챙겨줄게!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=lobby_night_10905_1].dlg
   limit: do 180 znaków
   EN: I’ll be going first~ What the, you’re staying for overtime? Oh boy… Got some work cut out, huh. You’ll get paid handsomely, I promise!
   PL:
341. [Kwestia głosowa [smalltalk_10905_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=smalltalk_10905_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Kwestia głosowa [smalltalk_10905_1] (Chatter #1)] 우리가 쓰는 무기는 전부 우리 공방에서 직접 만든다구~ 앗, 이거 왜 이래…\n하하, 고, 고치는 것도 우리가 직접 하지.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=smalltalk_10905_1].dlg
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We make all the weapons we use~ Oh, what’s wrong with this stupid thing…\nHaha, w—we also fix ‘em all by ourselves.
   PL:
343. [Kwestia głosowa [smalltalk_10905_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=smalltalk_10905_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Kwestia głosowa [smalltalk_10905_2] (Chatter #2)] 오~ 뭐야뭐야? 일거리라도 물어 온 거야?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=smalltalk_10905_2].dlg
   limit: do 120 znaków
   EN: Ooh~ Whuzzat, whuzzat? Got a job for me?
   PL:
345. [Kwestia głosowa [smalltalk_10905_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=smalltalk_10905_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Kwestia głosowa [smalltalk_10905_3] (Chatter #3)] 일은 안 하냐고? 나는~ 현장이 적성에 맞거든. 후후. 다른 녀석들이 잘 해주니까 괜찮을 거야~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=smalltalk_10905_3].dlg
   limit: do 190 znaków
   EN: Am I not doing any work? Well, you see~ I’m a fieldwork kinda person. Fuhu. It’s gonna be fine, others’ve got the desk work covered, I’m sure~
   PL:
347. [Kwestia głosowa [smalltalk_10905_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=smalltalk_10905_4].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Kwestia głosowa [smalltalk_10905_4] (Post-Uptie Chat 1)] 뭐~?! 슬롯머신? 아휴, 바보야. 그걸로 진짜 돈이 벌릴 거라고 생각하는 거야?\n실력으로 승부해야지!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=smalltalk_10905_4].dlg
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Whaaat~?! Slot machines? Ugh, you dummy. You really think you can win money from that?\nYou gotta use your skills!
   PL:
349. [Kwestia głosowa [smalltalk_10905_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=smalltalk_10905_5].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Kwestia głosowa [smalltalk_10905_5] (Post-Uptie Chat 2)] 자, 자 여기 앉아봐… 마우스 쥐고! 그렇지. 이걸 누르면~ 이제 쟤랑 붙는 거야!\n어… 포 카드?!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=smalltalk_10905_5].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Alright, take a seat here… Hold the mouse! That’s right. And when you click this~ You get into a game with that bucko!\nWha… Four of a kind?!
   PL:
351. [Kwestia głosowa [neglect_10905_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=neglect_10905_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Kwestia głosowa [neglect_10905_1] (Idle)] 엇 차~ 잠깐 누워 볼까요~?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=neglect_10905_1].dlg
   limit: do 120 znaków
   EN: Whoocha~ Guess I’ll lie down for a wee bit~
   PL:
353. [Kwestia głosowa [gacksung_10905_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=gacksung_10905_1].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Kwestia głosowa [gacksung_10905_1] (Uptying)] 음~? 나는 대표라 더 올라갈 곳이 없는데~ 대신, 일거리만 더 물어다 줘!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=gacksung_10905_1].dlg
   limit: do 140 znaków
   EN: Hm~? I’m already the rep, I don’t see how I can get to a higher position~ Just get us more work instead!
   PL:
355. [Kwestia głosowa [formation_10905_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=formation_10905_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Kwestia głosowa [formation_10905_1] (Deployment)] 좋아, 몸 좀 풀어보자구!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=formation_10905_1].dlg
   limit: do 120 znaków
   EN: Aight, let’s go for a round!
   PL:
357. [Kwestia głosowa [battleentry_10905_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battleentry_10905_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Kwestia głosowa [battleentry_10905_1] (Stage Entry)] 돈 벌러 가자~!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battleentry_10905_1].dlg
   limit: do 120 znaków
   EN: Let’s get this bread~!
   PL:
359. [Kwestia głosowa [battle_select_10905_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_select_10905_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Kwestia głosowa [battle_select_10905_1] (Viewed in Battle)] 으응? 지금 바쁜데, 용건만 빨리!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_select_10905_1].dlg
   limit: do 120 znaków
   EN: Mm? Bit busy right now, make it quick!
   PL:
361. [Kwestia głosowa [battle_endcommand_10905_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_endcommand_10905_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Kwestia głosowa [battle_endcommand_10905_1] (Commencing Attack)] 가자!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_endcommand_10905_1].dlg
   limit: do 120 znaków
   EN: Let’s go!
   PL:
363. [Kwestia głosowa [battle_enemy_break_10905_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_enemy_break_10905_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Kwestia głosowa [battle_enemy_break_10905_1] (Enemy Stagger)] 흐흥, 제대로 찝었군!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_enemy_break_10905_1].dlg
   limit: do 120 znaków
   EN: Hmheh, pinched ‘em right!
   PL:
365. [Kwestia głosowa [battle_break_10905_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_break_10905_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Kwestia głosowa [battle_break_10905_1] (Staggered)] 큭…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_break_10905_1].dlg
   limit: do 120 znaków
   EN: Kuh…
   PL:
367. [Kwestia głosowa [battle_kill_10905_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_kill_10905_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Kwestia głosowa [battle_kill_10905_1] (Enemy Killed)] 자, 한 건 했고!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_kill_10905_1].dlg
   limit: do 120 znaków
   EN: Yeah, that’s one done!
   PL:
369. [Kwestia głosowa [battle_dead_10905_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_dead_10905_1].desc
   (powtórzenie elementu 291 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Kwestia głosowa [battle_dead_10905_1] (Death)] 이럴 줄 알았으면… 한탕 좀 제대로 해보고… 올 걸.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_dead_10905_1].dlg
   limit: do 120 znaków
   EN: If I knew this would happen… I woulda gone for a bigger spree… the other day.
   PL:
371. [Kwestia głosowa [choice_success_p_10905_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=choice_success_p_10905_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Kwestia głosowa [choice_success_p_10905_1] (Check Passed)] 흥, 이런 건 누워서 떡 먹기지!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=choice_success_p_10905_1].dlg
   limit: do 120 znaków
   EN: Hmph, what a piece of rice cake!
   PL:
373. [Kwestia głosowa [choice_fail_n_10905_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=choice_fail_n_10905_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Kwestia głosowa [choice_fail_n_10905_1] (Check Failed)] 치… 맞는 공구가 없었다고.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=choice_fail_n_10905_1].dlg
   limit: do 120 znaków
   EN: Psh… None of my tools fit.
   PL:
375. [Kwestia głosowa [battle_clear_10905_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_clear_10905_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Kwestia głosowa [battle_clear_10905_1] (Victory Cry)] 좋아! 입에 풀칠은 하겠네~ 애들 월급 주려면 돈~ 좀~ 불려야 겠어~ 후훗.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_clear_10905_1].dlg
   limit: do 180 znaków
   EN: Got it! That should keep us afloat~ And if I wanna pay my bosom buddies a handsome salary, I’ve gotta make more fortune out of it~ Huhu.
   PL:
377. [Kwestia głosowa [battle_clear_ex_10905_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_clear_ex_10905_1].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Kwestia głosowa [battle_clear_ex_10905_1] (Extra Conditions Fulfilled)] 히야, 이 정도면 너무 성공적인데? 추가 보수 나오는 거 아냐?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_clear_ex_10905_1].dlg
   limit: do 120 znaków
   EN: Heehey, this is a huge success, ain’t it? Am I gonna get a bonus?
   PL:
379. [Kwestia głosowa [battle_defeat_10905_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_defeat_10905_1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Kwestia głosowa [battle_defeat_10905_1] (Defeat Wail)] 하… 이러면 계약 파기인데…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Kcorp_10905.json :: dataList[id=battle_defeat_10905_1].dlg
   limit: do 120 znaków
   EN: Ha… This might can the contract…
   PL:

## [00] Zwei Assoc. South Section 5 — Rodion — 남부 츠바이 협회 5과
- ID Tożsamości: `10906` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 88 · szybkość: 1–3 / 2–3 / 2–4 / 2–4
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Poise

381. [Karta Tożsamości — tytuł] 남부 츠바이 협회\n5과
   źródło: Personalities.json :: dataList[id=10906].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Zwei Assoc.\nSouth Section 5
   PL:
382. [Karta Tożsamości — nazwa] 로쟈
   źródło: Personalities.json :: dataList[id=10906].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Karta Tożsamości — nazwa z tytułem] 로쟈
   źródło: Personalities.json :: dataList[id=10906].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Karta Tożsamości — opis] 로쟈의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10906].desc
   limit: do 120 znaków
   EN: Rodion’s 6th Identity
   PL:
385. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 견제
   źródło: Skills.json :: dataList[id=1090601].levelList[level=1].name ; dataList[id=1090601].levelList[level=2].name ; dataList[id=1090601].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Careful Obstruction
   PL:
386. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1090601].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1090601].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain +1 [Breath] Count
   PL:
387. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1090601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1090601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1090601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL:
389. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 2 증가\n[DefeatDuel] 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1090601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 Aggro to this Skill Slot next turn\n[DefeatDuel] Gain +2 [Breath] Count
   PL:
390. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1090601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 집중 방어
   źródło: Skills.json :: dataList[id=1090602].levelList[level=1].name ; dataList[id=1090602].levelList[level=2].name ; dataList[id=1090602].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 6 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Focused Defense
   PL:
392. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [WhenUse] 자신의 보호막이 15 이상이면, 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1090602].levelList[level=1].desc ; dataList[id=1090602].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] At 15+ Shield, gain +2 [Breath] Count
   PL:
393. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1090602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1090602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL:
394. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 보호막이 15 이상이면, 호흡 횟수 2 증가\n[WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n[WhenUse] 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1090602].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] At 15+ Shield, gain +2 [Breath] Count\n[WhenUse] Gain +4 Aggro to this Skill Slot next turn\n[WhenUse] Gain +2 [Breath] Count
   PL:
395. [Umiejętność 3 (×1) (ulepszenia 1,4) — nazwa] 위협 대상 제압
   źródło: Skills.json :: dataList[id=1090603].levelList[level=1].name ; dataList[id=1090603].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 5 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Subdue Threat
   PL:
396. [Umiejętność 3 (×1) (ulepszenie 1) — opis] 자신의 보호막이 15 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1090603].levelList[level=1].desc
   limit: do 120 znaków
   EN: At 15+ shield, Coin Power +1
   PL:
397. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 3, efekt 1 — opis] [CriticalOnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills.json :: dataList[id=1090603].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1090603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict 1 Fragile next turn
   PL:
398. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 보호막이 15 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1090603].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 15+ Shield, Coin Power +2
   PL:
399. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1090604].levelList[level=1].name ; dataList[id=1090604].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   (powtórzenie elementu 175 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 5 증가
   źródło: Skills.json :: dataList[id=1090604].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +5 Aggro to this Skill Slot next turn
   PL:
401. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Wrath) — nazwa] 방어 호흡
   źródło: Passives.json :: dataList[id=1090601].name
   limit: do 40 znaków
   EN: Defensive Breathing
   PL:
402. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Wrath) — opis] 전투 시작 시 호흡 횟수 1 마다 보호막을 2 얻음 (최대 20)
   źródło: Passives.json :: dataList[id=1090601].desc
   limit: do 120 znaków
   EN: At the start of the combat phase, gain 2 Shield per 1 Poise Count. (Max 20)
   PL:
403. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 지정 보호
   źródło: Passives.json :: dataList[id=1090621].name
   limit: do 40 znaków
   EN: Designated Protection
   PL:
404. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 전투 시작 시 현재 체력 비율이 가장 낮은 아군 1명이 자신의 호흡 횟수 1 당 보호막을 1 얻음 (최대 10)
   źródło: Passives.json :: dataList[id=1090621].desc
   limit: do 160 znaków
   EN: At the start of the combat phase, 1 ally with the lowest HP percentage gains 1 Shield per 1 Poise Count next turn. (Max 10)
   PL:
405. [Kwestia głosowa [get_10906_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=get_10906_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Kwestia głosowa [get_10906_1] (Identity Acquisition)] 음~ 날씨 좋다. 자, 그래서 누굴 보호해야 한다고 했지?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=get_10906_1].dlg
   limit: do 120 znaków
   EN: Mm~ What nice weather. Right, so who needed my protection?
   PL:
407. [Kwestia głosowa [lobby_morning_10906_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=lobby_morning_10906_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Kwestia głosowa [lobby_morning_10906_1] (Morning Greeting)] 아침에 일어나는 게 쉬운 건 아니지만… 그래도 날씨가 이럴 때면~ 개운하게 일어날 수 있지 않아?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=lobby_morning_10906_1].dlg
   limit: do 180 znaków
   EN: It's no easy feat to wake up early in the morning... But with weather as nice as this, you just feel refreshed when you get up, yeah?
   PL:
409. [Kwestia głosowa [lobby_noon_10906_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=lobby_noon_10906_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Kwestia głosowa [lobby_noon_10906_1] (Afternoon Greeting)] 오늘 점심은… 간단하게 도넛하고 커피로 하자고. 뭐? 물린다고? 이게 잠복임무의 정석이라고~!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=lobby_noon_10906_1].dlg
   limit: do 190 znaków
   EN: For lunch... let's keep it simple with donuts and coffee. What? You're sick of 'em? Too bad, these are the staple diet of a Fixer on stakeout~!
   PL:
411. [Kwestia głosowa [lobby_night_10906_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=lobby_night_10906_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Kwestia głosowa [lobby_night_10906_1] (Evening Greeting)] 어유… 이거, 선글라스 좀 벗으면 안되나? 시꺼매서 뭐가 보여야지~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=lobby_night_10906_1].dlg
   limit: do 120 znaków
   EN: Aw, geez... Can't I take these sunglasses off? I can't see a thing through this dark tint~
   PL:
413. [Kwestia głosowa [smalltalk_10906_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=smalltalk_10906_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Kwestia głosowa [smalltalk_10906_1] (Chatter #1)] 나는~ 지정보호 전담이야. 고객께서 생활에 불편함을 느끼시지 않게~ 자연스러운 방패가 되어 드릴 수 있거든.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=smalltalk_10906_1].dlg
   limit: do 170 znaków
   EN: My job~ It's to protect appointed persons. Make sure my client doesn't feel bothered at all~ I can be a natural shield like that.
   PL:
415. [Kwestia głosowa [smalltalk_10906_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=smalltalk_10906_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Kwestia głosowa [smalltalk_10906_2] (Chatter #2)] …후후, 너무 튀지 않냐고? 후~ 나보다는 다른 친구들이 걱정인걸.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=smalltalk_10906_2].dlg
   limit: do 120 znaków
   EN: ...Fuhu, you think I might stand out? Whew~ I'm more worried about the others, really.
   PL:
417. [Kwestia głosowa [smalltalk_10906_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=smalltalk_10906_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Kwestia głosowa [smalltalk_10906_3] (Chatter #3)] 이런 잠복임무… 너무 좀이 쑤시단 말이지… 으으. 무슨 일 안생기나~?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=smalltalk_10906_3].dlg
   limit: do 120 znaków
   EN: A stealth mission like this... ugh, it's too boring... won't anything please happen?
   PL:
419. [Kwestia głosowa [smalltalk_10906_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=smalltalk_10906_4].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Kwestia głosowa [smalltalk_10906_4] (Post-Uptie Chat 1)] 아~ 왔구나? 협회 코트를 입고 있는 모습은 익숙하지 않으려나? 뭐, 나도 이런 모습이 있다구~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=smalltalk_10906_4].dlg
   limit: do 120 znaków
   EN: Ah~ You're here? Not used to seeing me wear the Association coat? Well, I have many forms~
   PL:
421. [Kwestia głosowa [smalltalk_10906_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=smalltalk_10906_5].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Kwestia głosowa [smalltalk_10906_5] (Post-Uptie Chat 2)] 너무 가까이 오진 마, 피 묻겠다.\n별로… 보기 좋은 모습은 아니잖아?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=smalltalk_10906_5].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Don't come too close. You'll get blood on you.\nAnd that's... not a very good look, is it?
   PL:
423. [Kwestia głosowa [neglect_10906_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=neglect_10906_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Kwestia głosowa [neglect_10906_1] (Idle)] 으으으~ 휴. 나 잠깐 낮잠 좀 잘게~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=neglect_10906_1].dlg
   limit: do 120 znaków
   EN: Hnnnngh~ Phew. Lemme take a nap for a minute~
   PL:
425. [Kwestia głosowa [gacksung_10906_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=gacksung_10906_1].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Kwestia głosowa [gacksung_10906_1] (Uptying)] 인정 받는 건 기분 좋은 일이지~ 음… 그것 보다는 임무수당이나 더 챙겨주면 좋겠는데~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=gacksung_10906_1].dlg
   limit: do 120 znaków
   EN: It's good to be recognized~ Hm... Though, I'd prefer better pay for the missions~
   PL:
427. [Kwestia głosowa [formation_10906_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=formation_10906_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Kwestia głosowa [formation_10906_1] (Deployment)] 선글라스 벗고~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=formation_10906_1].dlg
   limit: do 120 znaków
   EN: Sunglasses off~
   PL:
429. [Kwestia głosowa [battleentry_10906_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battleentry_10906_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Kwestia głosowa [battleentry_10906_1] (Stage Entry)] 임무 시작.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battleentry_10906_1].dlg
   limit: do 120 znaków
   EN: Commencing mission.
   PL:
431. [Kwestia głosowa [battle_select_10906_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_select_10906_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Kwestia głosowa [battle_select_10906_1] (Viewed in Battle)] 내 등 뒤에 숨어있어!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_select_10906_1].dlg
   limit: do 120 znaków
   EN: Stay behind my back!
   PL:
433. [Kwestia głosowa [battle_endcommand_10906_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_endcommand_10906_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Kwestia głosowa [battle_endcommand_10906_1] (Commencing Attack)] 제압 실시!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_endcommand_10906_1].dlg
   limit: do 120 znaków
   EN: Subduing target!
   PL:
435. [Kwestia głosowa [battle_enemy_break_10906_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_enemy_break_10906_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Kwestia głosowa [battle_enemy_break_10906_1] (Enemy Stagger)] 휴~ 기절했나?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_enemy_break_10906_1].dlg
   limit: do 120 znaków
   EN: Phew~ Did they get knocked out cold?
   PL:
437. [Kwestia głosowa [battle_break_10906_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_break_10906_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Kwestia głosowa [battle_break_10906_1] (Staggered)] 이, 이런…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_break_10906_1].dlg
   limit: do 120 znaków
   EN: Oh, oh boy...
   PL:
439. [Kwestia głosowa [battle_kill_10906_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_kill_10906_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Kwestia głosowa [battle_kill_10906_1] (Enemy Killed)] 위협 대상, 제거~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_kill_10906_1].dlg
   limit: do 120 znaków
   EN: Threat, removed~
   PL:
441. [Kwestia głosowa [battle_dead_10906_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_dead_10906_1].desc
   (powtórzenie elementu 291 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Kwestia głosowa [battle_dead_10906_1] (Death)] 아… 이러면… 실적이…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_dead_10906_1].dlg
   limit: do 120 znaków
   EN: Ah... but... my performance records...
   PL:
443. [Kwestia głosowa [choice_success_p_10906_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=choice_success_p_10906_2].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Kwestia głosowa [choice_success_p_10906_2] (Check Passed)] 훗, 쉽지~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=choice_success_p_10906_2].dlg
   limit: do 120 znaków
   EN: Heh, that's easy~
   PL:
445. [Kwestia głosowa [choice_fail_n_10906_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=choice_fail_n_10906_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Kwestia głosowa [choice_fail_n_10906_1] (Check Failed)] 이, 이런건 내 전문 분야가 아니라…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=choice_fail_n_10906_1].dlg
   limit: do 120 znaków
   EN: T-This isn't one of my specialties, y'know...
   PL:
447. [Kwestia głosowa [battle_clear_10906_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_clear_10906_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Kwestia głosowa [battle_clear_10906_1] (Victory Cry)] 자~ 이번 임무도 순조롭게 끝! 돌아가는 길에 맥주 한 잔 할래?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_clear_10906_1].dlg
   limit: do 120 znaków
   EN: Whew~ That's another smooth-sailing mission! How about we grab a beer on the way back?
   PL:
449. [Kwestia głosowa [battle_clear_ex_10906_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_clear_ex_10906_1].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Kwestia głosowa [battle_clear_ex_10906_1] (Extra Conditions Fulfilled)] 완벽한 임무였어! 후후, 다음에도 저희 츠바이를 이용해주세요!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_clear_ex_10906_1].dlg
   limit: do 120 znaków
   EN: A perfect mission! Fuhu, please hire Zwei again!
   PL:
451. [Kwestia głosowa [battle_defeat_10906_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_defeat_10906_1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Kwestia głosowa [battle_defeat_10906_1] (Defeat Wail)] 아… 시말서 써야하잖아… 흑흑.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Zwei_10906.json :: dataList[id=battle_defeat_10906_1].dlg
   limit: do 120 znaków
   EN: Crap... Now I've got letters of explanation to write... Sniffle.
   PL:

## [000] Dieci Assoc. South Section 4 — Rodion — 남부 디에치 협회 4과
- ID Tożsamości: `10907` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 88 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Sinking

453. [Karta Tożsamości — tytuł] 남부 디에치 협회\n4과
   źródło: Personalities.json :: dataList[id=10907].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Dieci Assoc.\nSouth Section 4
   PL:
454. [Karta Tożsamości — nazwa] 로쟈
   źródło: Personalities.json :: dataList[id=10907].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Karta Tożsamości — nazwa z tytułem] 로쟈
   źródło: Personalities.json :: dataList[id=10907].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Karta Tożsamości — opis] 로쟈의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10907].desc
   limit: do 120 znaków
   EN: Rodion's 7th Identity
   PL:
457. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 무지를 밝히리
   źródło: Skills_personality-09.json :: dataList[id=1090701].levelList[level=1].name ; dataList[id=1090701].levelList[level=2].name ; dataList[id=1090701].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 3 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Illuminate Thy Vacuity
   PL:
458. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 이 스킬이 버려지면 (탐구한 지식 x 최대 체력의 3%)만큼 보호막을 얻음
   źródło: Skills_personality-09.json :: dataList[id=1090701].levelList[level=1].desc
   limit: do 120 znaków
   EN: Gain (Insight x 3% of Max HP) Shield if this Skill is Discarded
   PL:
459. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 5 회복
   źródło: Skills_personality-09.json :: dataList[id=1090701].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 5
   PL:
460. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 이 스킬이 버려지면 (탐구한 지식 x 최대 체력의 4%)만큼 보호막을 얻음\n[WhenUse] 탐구한 지식 이 2 이상이면, (탐구한 지식 - 1)만큼 코인 위력이 증가
   źródło: Skills_personality-09.json :: dataList[id=1090701].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: Gain (Insight x 4% of Max HP) Shield if this Skill is Discarded\n[WhenUse] If Insight is 2 or higher, gain Coin Power by (Insight -1)
   PL:
461. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 8 회복
   źródło: Skills_personality-09.json :: dataList[id=1090701].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 8
   PL:
462. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 이 스킬이 버려지면 (탐구한 지식 x 최대 체력의 5%)만큼 보호막을 얻음\n[WhenUse] 탐구한 지식 이 2 이상이면, (탐구한 지식 - 1)만큼 코인 위력이 증가
   źródło: Skills_personality-09.json :: dataList[id=1090701].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: Gain (Insight x 5% of Max HP) Shield if this Skill is Discarded\n[WhenUse] If Insight is 2 or higher, gain Coin Power by (Insight -1)
   PL:
463. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 10 회복
   źródło: Skills_personality-09.json :: dataList[id=1090701].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 10
   PL:
464. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 지식의 무게
   źródło: Skills_personality-09.json :: dataList[id=1090702].levelList[level=1].name ; dataList[id=1090702].levelList[level=2].name ; dataList[id=1090702].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 3 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Weight of Knowledge
   PL:
465. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 이 스킬이 버려지면 (탐구한 지식 x 최대 체력의 5%)만큼 보호막을 얻음.\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림\n[WhenUse] 다음 턴에 이 슬롯이 도발치 2를 얻음
   źródło: Skills_personality-09.json :: dataList[id=1090702].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: Gain (Insight x 5% of Max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the lowest rank in all of this unit's Skill Slots\n[WhenUse] This Slot gains 2 Aggro next turn
   PL:
466. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills_personality-09.json :: dataList[id=1090702].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Sinking
   PL:
467. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 이 스킬이 버려지면 (탐구한 지식 x 최대 체력의 8%)만큼 보호막을 얻음.\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림\n[WhenUse] 다음 턴에 이 슬롯이 도발치 3을 얻음
   źródło: Skills_personality-09.json :: dataList[id=1090702].levelList[level=2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: Gain (Insight x 8% of Max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the lowest rank in all of this unit's Skill Slots\n[WhenUse] This Slot gains 3 Aggro next turn
   PL:
468. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_personality-09.json :: dataList[id=1090702].levelList[level=2].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Sinking
   PL:
469. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 이 스킬이 버려지면 (탐구한 지식 x 최대 체력의 10%)만큼 보호막을 얻음.\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림\n[WhenUse] 다음 턴에 이 슬롯이 도발치 5를 얻음\n[WhenUse] 대상의 [Sinking]이 5 이상이면, 합 위력 +2
   źródło: Skills_personality-09.json :: dataList[id=1090702].levelList[level=4].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: Gain (Insight x 10% of Max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the lowest rank in all of this unit's Skill Slots\n[WhenUse] This Slot gains 5 Aggro next turn\n[WhenUse] If target has 5+ [Sinking], gain Clash Power +2
   PL:
470. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 침잠 5 부여
   źródło: Skills_personality-09.json :: dataList[id=1090702].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Sinking
   PL:
471. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 고통스러운 계몽
   źródło: Skills_personality-09.json :: dataList[id=1090703].levelList[level=3].name ; dataList[id=1090703].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Excruciating Study
   PL:
472. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이 스킬이 버려지면 (탐구한 지식 x 최대 체력의 15%)만큼 보호막을 얻음.\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 2개를 버림\n[WhenUse] 다음 턴에 이 슬롯이 도발치 3을 얻음
   źródło: Skills_personality-09.json :: dataList[id=1090703].levelList[level=3].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: Gain (Insight x 15% of Max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 2 Skills of the lowest ranks in all of this unit's Skill Slots\n[WhenUse] This Slot gains 3 Aggro next turn
   PL:
473. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 횟수 4 증가
   źródło: Skills_personality-09.json :: dataList[id=1090703].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +4 Sinking Count
   PL:
474. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 2 증가
   źródło: Skills_personality-09.json :: dataList[id=1090703].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1090703].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Sinking Count
   PL:
475. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 이 스킬이 버려지면 (탐구한 지식 x 최대 체력의 20%)만큼 보호막을 얻음.\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 2개를 버림\n[WhenUse] 다음 턴에 이 슬롯이 도발치 5를 얻음\n[WhenUse] 대상의 [Sinking]이 7 이상이면, 코인 위력 +1
   źródło: Skills_personality-09.json :: dataList[id=1090703].levelList[level=4].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: Gain (Insight x 20% of Max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 2 Skills of the lowest ranks in all of this unit's Skill Slots\n[WhenUse] This Slot gains 5 Aggro next turn\n[WhenUse] If target has 7+ [Sinking], gain Coin Power +1
   PL:
476. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 4 증가
   źródło: Skills_personality-09.json :: dataList[id=1090703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +4 Sinking Count
   PL:
477. [Obrona (ulepszenia 3–4) — nazwa] 탐구 몰입
   źródło: Skills_personality-09.json :: dataList[id=1090704].levelList[level=3].name ; dataList[id=1090704].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Fixated Study
   PL:
478. [Obrona (ulepszenie 3) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림\n[WhenUse] 다음 턴에 이 슬롯이 도발치 2를 얻음
   źródło: Skills_personality-09.json :: dataList[id=1090704].levelList[level=3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots\n[WhenUse] This Slot gains 2 Aggro next turn
   PL:
479. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림\n[WhenUse] 다음 턴에 이 슬롯이 도발치 5를 얻음
   źródło: Skills_personality-09.json :: dataList[id=1090704].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots\n[WhenUse] This Slot gains 5 Aggro next turn
   PL:
480. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Gloom) — nazwa] 깨달음의 빛
   źródło: Passives.json :: dataList[id=1090701].name
   limit: do 40 znaków
   EN: Incandescent Enlightenment
   PL:
481. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Gloom) — opis] 이번 턴 동안 받은 피해량에 비례하여 다음 턴에 <sprite name="HitDamageUp"><color=#f8c200><u><link="HitDamageUp">타격 피해량 증가</link></u></color>를 얻음.\n(보호막으로 받은 피해도 받은 피해량에 포함됨. 턴 시작 시 체력의 25%만큼 피해를 받았을 때 최대로 획득. 최대 획득 값: 5)\n턴 종료 시 [KnowledgeExplored]이 3 이면, 자신에게 부여된 부정적인 효과 중 1개를 제거
   źródło: Passives.json :: dataList[id=1090701].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <sprite name="HitDamageUp">, <color=#f8c200>, <u>, <link="HitDamageUp">, </link>, </u>, </color>, \n, [KnowledgeExplored]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: Gain <sprite name="HitDamageUp"><color=#f8c200><u><link="HitDamageUp">Blunt DMG Up</link></u></color> next turn based on the damage that this unit took this turn.\n(Shield damage included in the calculation. Maxes out when taking damage equal to 25% of Max HP at turn start. Max Blunt DMG Up gained by this effect: 5)\nIf this unit has 3 [KnowledgeExplored] at the end of the turn, remove 1 negative effect applied to self
   PL:
482. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — nazwa] 지식 전도
   źródło: Passives.json :: dataList[id=1090721].name
   limit: do 40 znaków
   EN: Missionary of Knowledge
   PL:
483. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — opis] 최대 체력이 가장 높은 아군 1명이 이번 턴 동안 받은 피해량에 비례하여 다음 턴에 <sprite name="HitDamageUp"><color=#f8c200><u><link="HitDamageUp">타격 피해량 증가</link></u></color>를 얻음.\n(보호막으로 받은 피해도 받은 피해량에 포함됨. 턴 시작 시 체력의 15%만큼 피해를 받았을 때 최대로 획득. 최대 획득 값: 3)
   źródło: Passives.json :: dataList[id=1090721].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <sprite name="HitDamageUp">, <color=#f8c200>, <u>, <link="HitDamageUp">, </link>, </u>, </color>, \n
   EN: 1 ally with the highest Max HP gains <sprite name="HitDamageUp"><color=#f8c200><u><link="HitDamageUp">Blunt DMG Up</link></u></color> next turn based on the damage that they took this turn.\n(Shield damage included in the calculation. Maxes out when taking damage equal to 15% of Max HP at turn start. Max Blunt DMG Up gained by this effect: 3)
   PL:
484. [Kwestia głosowa [get_10907_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=get_10907_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Kwestia głosowa [get_10907_1] (Identity Acquisition)] 쉿…! 이거 먹어. 티는 내지마. 그리고 그냥 씹어. 감사는 됐어. 훗.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=get_10907_1].dlg
   limit: do 140 znaków
   EN: Shhh...! Hey, eat this. Don't act surprised. Just put it in your mouth and chew—no need to thank me, fuhu.
   PL:
486. [Kwestia głosowa [lobby_morning_10907_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=lobby_morning_10907_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Kwestia głosowa [lobby_morning_10907_1] (Morning Greeting)] 어우우… 아침부터 모여서 연구시키는 거, 하루 이틀은 좀 봐주면 안되나? 머리에 제대로 들어오지도 않는데.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=lobby_morning_10907_1].dlg
   limit: do 140 znaków
   EN: Ughhh... Can we take at least a day or two off from these morning research sessions? I'm still waking up...
   PL:
488. [Kwestia głosowa [lobby_noon_10907_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=lobby_noon_10907_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Kwestia głosowa [lobby_noon_10907_1] (Afternoon Greeting)] 점심은 건너 뛰어도 될 것 같아. 웬일이냐고? 어… 그, 협회 도서관에서… 군것질을 너무 많이 했거든.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=lobby_noon_10907_1].dlg
   limit: do 200 znaków
   EN: I think I'll skip lunch today. What? "As I live and breathe..."? That's because, uhh... Well, I snacked a little... too much at the Association library.
   PL:
490. [Kwestia głosowa [lobby_night_10907_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=lobby_night_10907_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Kwestia głosowa [lobby_night_10907_1] (Evening Greeting)] 너도 야자야? 하휴… 다른 사람들은 어쩜 그렇게 의자에 못박힌 듯 앉아있을 수 있는거야? 가만, 진짜 못을 박았나?!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=lobby_night_10907_1].dlg
   limit: do 180 znaków
   EN: You're going to the late night studies, too? Whew... It's like everyone's nailed their butts to their seats. Wait, did they actually—?!
   PL:
492. [Kwestia głosowa [smalltalk_10907_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=smalltalk_10907_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Kwestia głosowa [smalltalk_10907_1] (Chatter #1)] 나눠 먹는 건 좋은데, 감독 사서 님한테만 걸리지 않게 해줘… 알았지?\n또 걸리면 일주일 도서관 출입 금지로는 안 끝날 거라고.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=smalltalk_10907_1].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I don't mind sharing, but let's keep this out of the head librarian's eyes, okay?\nIf I get caught snacking again, I don't think it'll end with a weeklong library ban.
   PL:
494. [Kwestia głosowa [smalltalk_10907_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=smalltalk_10907_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Kwestia głosowa [smalltalk_10907_2] (Chatter #2)] 몰래 먹는 노하우라… 가장 중요한 건 눈빛이지. 그 누구보다 허망한 눈을 하는 거야.\n머리에 지식을 밀어넣다 쥐가 왔다는 듯이. 사실 빵을 밀어넣은 거지만.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=smalltalk_10907_2].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The key to stealthy snacking...? It's all in the eyes. Make the deadest, most zoned-out eyes ever.\nLike your brain's been overloaded with so much knowledge... when it's just that your face's been overloaded with pastry.
   PL:
496. [Kwestia głosowa [smalltalk_10907_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=smalltalk_10907_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Kwestia głosowa [smalltalk_10907_3] (Chatter #3)] 새로운 지식만큼 매혹적인 것도 없다지만… 윤기가 흐르는 이… 먹거리들도… 너무 매혹적인데?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=smalltalk_10907_3].dlg
   limit: do 170 znaków
   EN: They say that there's nothing as seductive as new knowledge... But aren't these freshly cooked delicacies... about as seductive?
   PL:
498. [Kwestia głosowa [smalltalk_10907_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=smalltalk_10907_4].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Kwestia głosowa [smalltalk_10907_4] (Post-Uptie Chat 1)] 어떻게 이렇게 강할 수 있냐고? 에휴, 그 간단한 말조차 모르니까 이렇게 당하지.\n잘 들어… '지식이 곧 힘이다.'
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=smalltalk_10907_4].dlg
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: How am I so strong? Sigh, how do you not know something so basic?\nListen up... 'Knowledge is power'.
   PL:
500. [Kwestia głosowa [smalltalk_10907_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=smalltalk_10907_5].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Kwestia głosowa [smalltalk_10907_5] (Post-Uptie Chat 2)] 우리 협회는 크게 열쇠 파와 격투 파로 나눠져 있어. 어, 나?  훗. 척 보면 모르겠어? 무지한 놈들을… 이 주먹으로 깨닫게 해주는 거지.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=smalltalk_10907_5].dlg
   limit: do 220 znaków
   EN: Our Association has two large divisions: the Keys and the Fists. Which one am I? Fuhu, can'tcha tell? I'll knock some enlightenment into them blockheads with these fists.
   PL:
502. [Kwestia głosowa [neglect_10907_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=neglect_10907_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Kwestia głosowa [neglect_10907_1] (Idle)] 냠… 네? 아뇨, 사서 님. 공부 중이었어요.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=neglect_10907_1].dlg
   limit: do 120 znaków
   EN: Nom... Yes? No ma'am. I was just studying.
   PL:
504. [Kwestia głosowa [gacksung_10907_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=gacksung_10907_1].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Kwestia głosowa [gacksung_10907_1] (Uptying)] 뭐더라… 아! 지식이 곧 나의 열쇠이니… 문을 열기 위해 정진하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=gacksung_10907_1].dlg
   limit: do 140 znaków
   EN: How'd it go again? With knowledge as my key... I shall continue to devote myself to the opening of the door.
   PL:
506. [Kwestia głosowa [formation_10907_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=formation_10907_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Kwestia głosowa [formation_10907_1] (Deployment)] 어, 전가요?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=formation_10907_1].dlg
   limit: do 120 znaków
   EN: Huh? Me?
   PL:
508. [Kwestia głosowa [battleentry_10907_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battleentry_10907_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Kwestia głosowa [battleentry_10907_1] (Stage Entry)] 고통 없이 지식을 얻지 못한다나 뭐라나…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battleentry_10907_1].dlg
   limit: do 120 znaków
   EN: No knowledge is earned without pain... or whatever, blah blah...
   PL:
510. [Kwestia głosowa [battle_select_10907_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_select_10907_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Kwestia głosowa [battle_select_10907_1] (Viewed in Battle)] 어? 간식인가?!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_select_10907_1].dlg
   limit: do 120 znaków
   EN: Ooh? Is it snack time?!
   PL:
512. [Kwestia głosowa [battle_endcommand_10907_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_endcommand_10907_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Kwestia głosowa [battle_endcommand_10907_1] (Commencing Attack)] 직접 알게 함이라.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_endcommand_10907_1].dlg
   limit: do 120 znaków
   EN: Let the truths be self-evident to them.
   PL:
514. [Kwestia głosowa [battle_enemy_break_10907_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_enemy_break_10907_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Kwestia głosowa [battle_enemy_break_10907_1] (Enemy Stagger)] 무지하니까…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_enemy_break_10907_1].dlg
   limit: do 120 znaków
   EN: Ignoramuses...
   PL:
516. [Kwestia głosowa [battle_break_10907_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_break_10907_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Kwestia głosowa [battle_break_10907_1] (Staggered)] 어!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_break_10907_1].dlg
   limit: do 120 znaków
   EN: Ah!
   PL:
518. [Kwestia głosowa [battle_kill_10907_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_kill_10907_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Kwestia głosowa [battle_kill_10907_1] (Enemy Killed)] 맞는 거야.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_kill_10907_1].dlg
   limit: do 120 znaków
   EN: Get smacked.
   PL:
520. [Kwestia głosowa [battle_dead_10907_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_dead_10907_1].desc
   (powtórzenie elementu 291 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Kwestia głosowa [battle_dead_10907_1] (Death)] 선배 말처럼… 공부를… 좀 더 할 걸 그랬나…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_dead_10907_1].dlg
   limit: do 120 znaków
   EN: I should've studied... like my seniors always told me to...
   PL:
522. [Kwestia głosowa [choice_success_p_10907_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=choice_success_p_10907_2].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Kwestia głosowa [choice_success_p_10907_2] (Check Passed)] 아, 이건 아는 거였어!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=choice_success_p_10907_2].dlg
   limit: do 120 znaków
   EN: Ohh! I know this one!
   PL:
524. [Kwestia głosowa [choice_fail_n_10907_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=choice_fail_n_10907_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Kwestia głosowa [choice_fail_n_10907_1] (Check Failed)] 아… 어디서 읽었었는데?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=choice_fail_n_10907_1].dlg
   limit: do 120 znaków
   EN: Agh... But I'm sure I've read about this before?!
   PL:
526. [Kwestia głosowa [battle_clear_10907_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_clear_10907_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Kwestia głosowa [battle_clear_10907_1] (Victory Cry)] 무지 외에 암흑은 없나니. …아, 그 뒤가 뭐더라…?!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_clear_10907_1].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The only abyss is the abyss of ignorance, and... \nAnd uh... crap. How'd that go again?
   PL:
528. [Kwestia głosowa [battle_clear_ex_10907_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_clear_ex_10907_1].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Kwestia głosowa [battle_clear_ex_10907_1] (Extra Conditions Fulfilled)] 후, 결국 내 공부가 부족하지 않았다는 거네. 그치? 좋았어.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_clear_ex_10907_1].dlg
   limit: do 120 znaków
   EN: Whew, so I'm not falling behind on my studies, right? Hell yeah.
   PL:
530. [Kwestia głosowa [battle_defeat_10907_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_defeat_10907_1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Kwestia głosowa [battle_defeat_10907_1] (Defeat Wail)] 너무 먹어만 댔나… 약간 몸도 둔한 것 같고… 역시 공부를 좀 더 하긴 해야겠어….
   źródło: PersonalityVoiceDlg/Voice_Rodion_Dieci_10907.json :: dataList[id=battle_defeat_10907_1].dlg
   limit: do 130 znaków
   EN: Ugh, maybe I've been eating too much... I feel sluggish, too... I guess I shoulda studied harder...
   PL:

## [000] Liu Assoc. South Section 4 Director — Rodion — 남부 리우 협회 4과 부장
- ID Tożsamości: `10908` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 79 · szybkość: 2–6 / 2–7 / 3–7 / 3–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Burn

532. [Karta Tożsamości — tytuł] 남부 리우 협회\n4과 부장
   źródło: Personalities.json :: dataList[id=10908].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Liu Assoc.\nSouth Section 4 Director
   PL:
533. [Karta Tożsamości — nazwa] 로쟈
   źródło: Personalities.json :: dataList[id=10908].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Karta Tożsamości — nazwa z tytułem] 로쟈
   źródło: Personalities.json :: dataList[id=10908].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Karta Tożsamości — opis] 로쟈의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10908].desc
   limit: do 120 znaków
   EN: Rodion's 8th Identity
   PL:
536. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 염권격
   źródło: Skills_personality-09.json :: dataList[id=1090801].levelList[level=1].name ; dataList[id=1090801].levelList[level=2].name ; dataList[id=1090801].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Flaming Fists
   PL:
537. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1090801].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1090801].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1090801].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL:
538. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1090801].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1090801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1090801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Combustion]이 3 이상이면 코인 위력 +1
   źródło: Skills_personality-09.json :: dataList[id=1090801].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 3+ [Combustion], Coin Power +1
   PL:
540. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Combustion] 3당, 코인 위력 +1(최대 2)
   źródło: Skills_personality-09.json :: dataList[id=1090801].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Coin Power +1 for every 3 [Combustion] on target (Max 2)
   PL:
541. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 염수격-연
   źródło: Skills_personality-09.json :: dataList[id=1090802].levelList[level=1].name ; dataList[id=1090802].levelList[level=2].name ; dataList[id=1090802].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Fiery Knifehand-Combust
   PL:
542. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1090802].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1090802].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1090802].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count
   PL:
543. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1090802].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1090802].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1090802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion] 횟수가 6 이상이면, [Combustion]이 없거나 [Combustion] 횟수가 가장 낮은 적 2명에게 [Combustion] 3 부여
   źródło: Skills_personality-09.json :: dataList[id=1090802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion] Count, apply 3 [Combustion] to 2 targets that have no [Combustion] or have the least [Combustion] Count.
   PL:
545. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Combustion]이 6 이상이면 코인 위력 +1
   źródło: Skills_personality-09.json :: dataList[id=1090802].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Coin Power +1
   PL:
546. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1090802].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1090802].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Inflict +1 [Combustion] Count
   PL:
547. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion] 횟수가 6 이상이면, [Combustion]이 없거나 [Combustion] 횟수가 가장 낮은 적 2명에게 [Combustion] 3 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1090802].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1090802].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion] Count, apply 3 [Combustion] to 2 targets that have no [Combustion] or have the least [Combustion] Count<style="highlight"></style>
   PL:
548. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Combustion] 6당, 코인 위력 +1(최대 2)
   źródło: Skills_personality-09.json :: dataList[id=1090802].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Coin Power +1 for every 6 [Combustion] on target (Max 2)
   PL:
549. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 일점돌파
   źródło: Skills_personality-09.json :: dataList[id=1090803].levelList[level=3].name ; dataList[id=1090803].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Pinpoint Blitz
   PL:
550. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Combustion]과 [Combustion] 횟수가 6 이상이면, 피해량 +30%
   źródło: Skills_personality-09.json :: dataList[id=1090803].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion] and [Combustion] Count, Deal +30% damage
   PL:
551. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1090803].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1090803].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1090803].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1090803].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-09.json :: dataList[id=1090803].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1090803].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL:
554. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion] 위력의 절반만큼 분노 속성 피해를 줌.(최대 20) 대상의 [Combustion] 횟수 2 감소
   źródło: Skills_personality-09.json :: dataList[id=1090803].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict Wrath Affinity damage equal to half of [Combustion] Potency on target. (Max 20) Reduce Target's [Combustion] Count by 2
   PL:
555. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">대상의 [Combustion]이 6 이상이면 코인 위력 +1</style>\n대상의 [Combustion]과 [Combustion] 횟수가 6 이상이면, 피해량 +30%
   źródło: Skills_personality-09.json :: dataList[id=1090803].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: <style="highlight">If target has 6+ [Combustion], Coin Power +1</style>\nIf target has 6+ [Combustion] and [Combustion] Count, deal +30% damage
   PL:
556. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion] 위력만큼 분노 속성 피해를 줌.(최대 30) 대상의 [Combustion] 횟수 2 감소
   źródło: Skills_personality-09.json :: dataList[id=1090803].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict Wrath Affinity damage equal to [Combustion] Potency on target. (Max 30) Reduce Target's [Combustion] Count by 2
   PL:
557. [Obrona (ulepszenia 1,4) — nazwa] 반격
   źródło: Skills_personality-09.json :: dataList[id=1090804].levelList[level=1].name ; dataList[id=1090804].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 9 · monety: 1 (+7)
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1090804].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1090804].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — nazwa] 뜨거운 기세
   źródło: Passives.json :: dataList[id=1090801].name
   limit: do 40 znaków
   EN: Burning Passion
   PL:
560. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — opis] 대상의 [Combustion] 위력 6 당 피해량 +5% (최대 15%)\n전투 시작 시 모든 적에게 [Combustion]이 6 이상 부여되어 있으면, 아군 (최대 분노 완전 공명 수) 명에게 편성 순으로 [CrimsonDamageUp] 1 부여\n- 집중 전투에서는 부위로 판정
   źródło: Passives.json :: dataList[id=1090801].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [CrimsonDamageUp]
   znaczenie tagów: [Combustion] = 화상 / Burn; [CrimsonDamageUp] = 분노 피해량 증가 / Wrath DMG Up
   EN: Deal +5% damage for every 6 [Combustion] Potency on target (Max 15%)\nCombat Start: If all enemies have 6+ [Combustion] Potency, apply 1 [CrimsonDamageUp] to (highest Wrath A-Reson.) allies in Deployment order\n- In Focused Encounters, the above activates when all enemy Parts have 6+ [Combustion] Potency
   PL:
561. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — podsumowanie] 대상의 [Combustion] 위력 6 당 피해량 +5% (최대 15%)\n화상, 분노 완전 공명 조건에 따라 아군에게 강화 효과 부여
   źródło: Passives.json :: dataList[id=1090801].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal +5% damage for every 6 [Combustion] Potency on target (Max 15%)\nUnder certain Burn and Wrath A-Reson. conditions, apply buff to allies
   PL:
562. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Wrath) — nazwa] 뜨거운 기세
   źródło: Passives.json :: dataList[id=1090811].name
   (powtórzenie elementu 559 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Wrath) — opis] 대상의 [Combustion] 위력 6 당 피해량 +10% (최대 30%)\n전투 시작 시 모든 적에게 [Combustion]이 6 이상 부여되어 있으면, 아군 (최대 분노 완전 공명 수) 명에게 편성 순으로 [CrimsonDamageUp] 1 부여\n- 집중 전투에서는 부위로 판정\n- 대상이 리우 협회 해결사면, 공격 위력 증가 1 부여
   źródło: Passives.json :: dataList[id=1090811].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [CrimsonDamageUp]
   znaczenie tagów: [Combustion] = 화상 / Burn; [CrimsonDamageUp] = 분노 피해량 증가 / Wrath DMG Up
   EN: Deal +10% damage for every 6 [Combustion] Potency on target (Max 30%)\nCombat Start: If all enemies have 6+ [Combustion] Potency, apply 1 [CrimsonDamageUp] to (highest Wrath A-Reson.) allies in Deployment order\n- In Focused Encounters, the above activates when all enemy Parts have 6+ [Combustion] Potency\n- If the ally is a Liu Association Fixer, apply 1 Attack Power Up
   PL:
564. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Wrath) — podsumowanie] 대상의 [Combustion] 위력 6 당 피해량 +10% (최대 30%)\n화상, 분노 완전 공명 조건에 따라 아군에게 강화 효과 부여
   źródło: Passives.json :: dataList[id=1090811].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal +10% damage for every 6 [Combustion] Potency on target (Max 30%)\nUnder certain Burn and Wrath A-Reson. conditions, apply buff to allies
   PL:
565. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Wrath) — nazwa] 화끈한 격려
   źródło: Passives.json :: dataList[id=1090821].name
   limit: do 40 znaków
   EN: Passionate Cheer
   PL:
566. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Wrath) — opis] 정신력이 가장 낮은 아군 1명이 공격 적중 시 대상의 [Combustion] 위력 6 당 관통 피해량 +5% (최대 15%)
   źródło: Passives.json :: dataList[id=1090821].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: 1 ally with the least SP deals +5% Pierce damage for every 6 [Combustion] Potency on target On Hit (Max 15%)
   PL:
567. [Kwestia głosowa [get_10908_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=get_10908_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Kwestia głosowa [get_10908_1] (Identity Acquisition)] 역시 세상에서 제일 즐거운 건 쇼핑할 때라니까~ 자! 또 뭐 먹으러 갈래?
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=get_10908_1].dlg
   limit: do 120 znaków
   EN: Shopping is totally the greatest pastime in the world~ Okay! What do you wanna eat next?
   PL:
569. [Kwestia głosowa [lobby_morning_10908_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=lobby_morning_10908_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Kwestia głosowa [lobby_morning_10908_1] (Morning Greeting)] 놀러 나갈 때는 아침 일찍 나가야 한다니까? 자는 시간은 매일 같은데, 조금이라도 늦게 나가면 손해 보는 기분이잖아!
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=lobby_morning_10908_1].dlg
   limit: do 180 znaków
   EN: Always leave early on your day off! If you're going to sleep the same hours anyway, might as well make the best of the daylight, hmm?
   PL:
571. [Kwestia głosowa [lobby_noon_10908_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=lobby_noon_10908_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Kwestia głosowa [lobby_noon_10908_1] (Afternoon Greeting)] 점심은 뭐 먹을까? 건두부 볶음? 마파두부? 아무튼 매콤하고 화끈한 게 좋단 말이지~
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=lobby_noon_10908_1].dlg
   limit: do 130 znaków
   EN: What should I get for lunch? Dried tofu stir-fry? Mapo tofu? Let's get something hot and spicy!
   PL:
573. [Kwestia głosowa [lobby_night_10908_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=lobby_night_10908_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Kwestia głosowa [lobby_night_10908_1] (Evening Greeting)] 후~ 오늘도 바쁜 하루였어. 여기저기 돌아다니느라 발에 불 날 뻔했지 뭐야.\n하~ 내일도 모레도 놀러나가면 좋을 것 같은데…
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=lobby_night_10908_1].dlg
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Phew... what a busy day. My feet are on fire from walking around all day.\nHaah... if only we had the next two days off too...
   PL:
575. [Kwestia głosowa [smalltalk_10908_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=smalltalk_10908_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Kwestia głosowa [smalltalk_10908_1] (Chatter #1)] 부장이라고 뭐 다를게 있겠어? 리우는 모두 따듯한 가족들이라구. 다같이 맛있는 식사 한 번 하면 사기도 오르고, 능률도 오르고! 좋지?
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=smalltalk_10908_1].dlg
   limit: do 260 znaków
   EN: The position of a director ain't nothing special! We're all like a big, happy family here at Liu. A nice hearty meal together helps not only with morale but also efficiency! Two birds with one stone, huh?
   PL:
577. [Kwestia głosowa [smalltalk_10908_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=smalltalk_10908_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Kwestia głosowa [smalltalk_10908_2] (Chatter #2)] 어허, 과소비라니! 버는 사람이 잘 써줘야지, 모두가 다 잘 살 수 있는 거라니까?\n과…식? 그, 그건… 먹어둘 수 있을 때 먹어줘야…
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=smalltalk_10908_2].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hey! What do you mean I'm 'overspending'? People with dough's gotta spend 'em for the good of everyone else, right?\nOh, you meant that I'm... overeating...? W-well, you gotta eat when you gotta eat, right...?
   PL:
579. [Kwestia głosowa [smalltalk_10908_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=smalltalk_10908_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Kwestia głosowa [smalltalk_10908_3] (Chatter #3)] 아니, 우리 협회 사람들 나눠줄 거라니까? 내가 어떻게 이걸 다 먹겠어~ 그치? 이스마엘?\n…신중하게 말해~ 그래야 자기 먹을 거리 양이 늘 거야~
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=smalltalk_10908_3].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This is for *everyone* in the Association, 'kay? It's not like I can eat all of this on my own~ Right, Ishmael? \n... Choose your next words carefully, Ishy~ Who knows? A 'yes' from you could mean more food for you~
   PL:
581. [Kwestia głosowa [smalltalk_10908_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=smalltalk_10908_4].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Kwestia głosowa [smalltalk_10908_4] (Post-Uptie Chat 1)] 자, 저기 대장 같아 보이는 녀석은 내가 책임지고 끝장 낼게. 너희들은 항상 하던 것처럼~ 옆에서 거슬리게 구는 놈들을 부탁해!
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=smalltalk_10908_4].dlg
   limit: do 160 znaków
   EN: All right! Leave the big cheese to me. Everyone else, just do your usual thing and keep the lackeys off my back, 'kay?!
   PL:
583. [Kwestia głosowa [smalltalk_10908_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=smalltalk_10908_5].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Kwestia głosowa [smalltalk_10908_5] (Post-Uptie Chat 2)] 많은 적을 한 번에 제압하는 힘. 그건 역시 '화력'에서 오는 거지. 제 아무리 많은 사람이 몰려와도, 불구덩이 속으로는 쉽사리 들어올 수도~ 나갈 수도 없는 법이니까.\n리우 사람들은 빼고, 훗.
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=smalltalk_10908_5].dlg
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A power to suppress multiple waves of enemies at once... it all comes from 'firepower'. Doesn't matter how many enemies throw themselves at us if we throw them all into a pit of fire. No chance they're crawling outta that one~\nUnless they're also from Liu, that is. Heh.
   PL:
585. [Kwestia głosowa [neglect_10908_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=neglect_10908_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Kwestia głosowa [neglect_10908_1] (Idle)] 딸기, 청포도, 귤… 어떤 걸 먹어볼까~
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=neglect_10908_1].dlg
   limit: do 120 znaków
   EN: Strawberries... green grapes... tangerines... Which fruit should I eat next~
   PL:
587. [Kwestia głosowa [gacksung_10908_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=gacksung_10908_1].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Kwestia głosowa [gacksung_10908_1] (Uptying)] 일점 집중. 비록 아무 무기 없는 맨손일지라도… 굳은 심지를 갖고 한 점을 향해 찔러버리면, 그건 거의… 칼과 창에 가깝지.
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=gacksung_10908_1].dlg
   limit: do 200 znaków
   EN: Focus on a singular point. A single, determined strike against a sole point could hurt just as much as a spear or a sword. Even if you stab 'em bare-handed.
   PL:
589. [Kwestia głosowa [formation_10908_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=formation_10908_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Kwestia głosowa [formation_10908_1] (Deployment)] 어, 잠깐만~ 마저 먹고!
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=formation_10908_1].dlg
   limit: do 120 znaków
   EN: Uhh, wait up! I'm still eating!
   PL:
591. [Kwestia głosowa [battleentry_10908_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battleentry_10908_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Kwestia głosowa [battleentry_10908_1] (Stage Entry)] 후~ 벌써 화끈하네.
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battleentry_10908_1].dlg
   limit: do 120 znaków
   EN: Phewie, heating up already?
   PL:
593. [Kwestia głosowa [battle_select_10908_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_select_10908_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Kwestia głosowa [battle_select_10908_1] (Viewed in Battle)] 어우, 안 뜨거워? 멀리서 말해도 들려!
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_select_10908_1].dlg
   limit: do 120 znaków
   EN: Whew, watch out for the heat! I can hear ya just as well from a distance, y'know~
   PL:
595. [Kwestia głosowa [battle_endcommand_10908_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_endcommand_10908_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Kwestia głosowa [battle_endcommand_10908_1] (Commencing Attack)] 단번에 끝낸다!
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_endcommand_10908_1].dlg
   limit: do 120 znaków
   EN: With a single strike!
   PL:
597. [Kwestia głosowa [battle_enemy_break_10908_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_enemy_break_10908_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Kwestia głosowa [battle_enemy_break_10908_1] (Enemy Stagger)] 괜히 저항하지 말고 받아들여. 그게 덜 아플걸.
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_enemy_break_10908_1].dlg
   limit: do 120 znaków
   EN: Stop fighting and just accept it. It'll hurt less that way.
   PL:
599. [Kwestia głosowa [battle_break_10908_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_break_10908_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Kwestia głosowa [battle_break_10908_1] (Staggered)] 아잇…
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_break_10908_1].dlg
   limit: do 120 znaków
   EN: Agh...
   PL:
601. [Kwestia głosowa [battle_kill_10908_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_kill_10908_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Kwestia głosowa [battle_kill_10908_1] (Enemy Killed)] 괜찮아. 이젠 안 아플거야.
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_kill_10908_1].dlg
   limit: do 120 znaków
   EN: Relax. You won't be hurting anymore.
   PL:
603. [Kwestia głosowa [battle_dead_10908_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_dead_10908_1].desc
   (powtórzenie elementu 291 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Kwestia głosowa [battle_dead_10908_1] (Death)] 쿨럭… 잿더미에 깔리는 게… 내가 될 줄은…
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_dead_10908_1].dlg
   limit: do 120 znaków
   EN: Cough... Didn't think... I'd be buried in ash myself...
   PL:
605. [Kwestia głosowa [choice_success_p_10908_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=choice_success_p_10908_2].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Kwestia głosowa [choice_success_p_10908_2] (Check Passed)] 이런 건~ 얼마나 집중할 수 있냐에 따라 달렸지!
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=choice_success_p_10908_2].dlg
   limit: do 120 znaków
   EN: This kinda thing~ is all about focus!
   PL:
607. [Kwestia głosowa [choice_fail_n_10908_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=choice_fail_n_10908_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Kwestia głosowa [choice_fail_n_10908_1] (Check Failed)] 아… 너무 무식하게 했나?
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=choice_fail_n_10908_1].dlg
   limit: do 120 znaków
   EN: Oh... I guess brute force wasn't the right way to go?
   PL:
609. [Kwestia głosowa [battle_clear_10908_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_clear_10908_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Kwestia głosowa [battle_clear_10908_1] (Victory Cry)] 좋아, 일은 나쁘지 않게 끝냈네. 배도 고픈데, 가는 길에 뭐라도 먹자!
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_clear_10908_1].dlg
   limit: do 140 znaków
   EN: Nice, we wrapped that up nicely. I'm hankerin' for some grub... we should grab something on our way back!
   PL:
611. [Kwestia głosowa [battle_clear_ex_10908_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_clear_ex_10908_1].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Kwestia głosowa [battle_clear_ex_10908_1] (Extra Conditions Fulfilled)] 두드려 패고 꿰뚫는다! 이게 우리 4과지. 후우, 덥다. 뭐 시원한 거 먹으러 가는 게 어때? 빙수 같은거!
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_clear_ex_10908_1].dlg
   limit: do 210 znaków
   EN: Beat 'em up and penetrate 'em! Now that's the Section 4 I know and love. Phew, it's so hot... we should go get something cold to cool us down. Bingsu, anyone?!
   PL:
613. [Kwestia głosowa [battle_defeat_10908_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_defeat_10908_1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Kwestia głosowa [battle_defeat_10908_1] (Defeat Wail)] 뭐… 매번 싸워서 이길 수는 없는 거니까. 든든하게 먹고 또 열심히 수련하면, 다시 해볼 수 있을 거야!
   źródło: PersonalityVoiceDlg/Voice_Rodion_LiuAsso4_10908.json :: dataList[id=battle_defeat_10908_1].dlg
   limit: do 160 znaków
   EN: Welp, ya win some, ya lose some. Let's fill up with some food, train hard, and try again! I'm sure we'll get 'em next time.
   PL:

## [00] T Corp. Class 2 Collection Staff — Rodion — T사 2등급 징수직 직원
- ID Tożsamości: `10909` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 86 · szybkość: 3–6 / 3–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Tremor

615. [Karta Tożsamości — tytuł] T사 2등급\n징수직 직원
   źródło: Personalities.json :: dataList[id=10909].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: T Corp. Class 2\nCollection Staff
   PL:
616. [Karta Tożsamości — nazwa] 로쟈
   źródło: Personalities.json :: dataList[id=10909].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Karta Tożsamości — nazwa z tytułem] 로쟈
   źródło: Personalities.json :: dataList[id=10909].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Karta Tożsamości — opis] 로쟈의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10909].desc
   limit: do 120 znaków
   EN: Rodion's 9th Identity
   PL:
619. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 징수 준비
   źródło: Skills_personality-09.json :: dataList[id=1090901].levelList[level=1].name ; dataList[id=1090901].levelList[level=2].name ; dataList[id=1090901].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Prepare To Collect
   PL:
620. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-09.json :: dataList[id=1090901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count
   PL:
621. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1090901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL:
622. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1090901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain +1 [Vibration] Count
   PL:
623. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [WinDuelAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1090901].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Vibration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Vibration] = 진동 / Tremor
   EN: [WinDuelAttack] Inflict +1 [Vibration] Count
   PL:
624. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">[WhenUse] 대상의 [Vibration]이 6 이상이면, 합 위력 +1</style>
   źródło: Skills_personality-09.json :: dataList[id=1090901].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n<style="highlight">[WhenUse] If target has 6+ [Vibration], Clash Power +1</style>
   PL:
625. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1090901].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]<style="highlight"></style>
   PL:
626. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1090901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1090901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain +1 [Vibration] Count<style="highlight"></style>
   PL:
627. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [WinDuelAttack] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1090901].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1090901].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WinDuelAttack], [Vibration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Vibration] = 진동 / Tremor
   EN: [WinDuelAttack] Inflict +1 [Vibration] Count<style="highlight"></style>
   PL:
628. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n[WhenUse] 대상의 [Vibration] <style="highlight">6 당 합 위력 +1 (최대 2)</style>
   źródło: Skills_personality-09.json :: dataList[id=1090901].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n[WhenUse] <style="highlight">Clash Power +1 for every 6 [Vibration] on target (max 2)</style>
   PL:
629. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-09.json :: dataList[id=1090901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Vibration]
   PL:
630. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] T사식 제압 격투
   źródło: Skills_personality-09.json :: dataList[id=1090902].levelList[level=1].name ; dataList[id=1090902].levelList[level=2].name ; dataList[id=1090902].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: T Corp. Martial Suppression
   PL:
631. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-09.json :: dataList[id=1090902].levelList[level=1].desc
   (powtórzenie elementu 620 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-09.json :: dataList[id=1090902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain +2 [Vibration] Count
   PL:
633. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">[WhenUse] 대상의 [Vibration]이 6 이상이면, 합 위력 +1</style>
   źródło: Skills_personality-09.json :: dataList[id=1090902].levelList[level=2].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1090902].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1090902].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain +2 [Vibration] Count<style="highlight"></style>
   PL:
635. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[WinDuelAttack] [Vibration] 횟수 2 증가</style>
   źródło: Skills_personality-09.json :: dataList[id=1090902].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WinDuelAttack], [Vibration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[WinDuelAttack] Inflict +2 [Vibration] Count</style>
   PL:
636. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">대상의 [Binding] 1 당 피해량 +5% (최대 15%)</style>\n[WhenUse] 자신의 [Vibration] 횟수 2 증가\n[WhenUse] 대상의 [Vibration] <style="highlight">6 당 합 위력 +1 (최대 2)</style>
   źródło: Skills_personality-09.json :: dataList[id=1090902].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Binding], [WhenUse], [Vibration]
   znaczenie tagów: [Binding] = 속박 / Bind; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">Deal +5% damage for every [Binding] on target (max 15%)</style>\n[WhenUse] Gain +2 [Vibration] Count\n[WhenUse] <style="highlight">Clash Power +1 for every 6 [Vibration] on target (max 2)</style>
   PL:
637. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [WinDuelAttack] [Vibration] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-09.json :: dataList[id=1090902].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WinDuelAttack], [Vibration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Vibration] = 진동 / Tremor
   EN: [WinDuelAttack] Inflict +<style="highlight">3</style> [Vibration] Count
   PL:
638. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [Binding] 1 부여</style>
   źródło: Skills_personality-09.json :: dataList[id=1090902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Binding] next turn</style>
   PL:
639. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 대상의 [Vibration]이 6 이상이면, 다음 턴에 [Binding] 1 부여</style>
   źródło: Skills_personality-09.json :: dataList[id=1090902].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [Binding] = 속박 / Bind
   EN: <style="highlight">[OnSucceedAttack] If target has 6+ [Vibration], inflict 1 [Binding] next turn</style>
   PL:
640. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 징수 집행
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=3].name ; dataList[id=1090903].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 2 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Execute Collections
   PL:
641. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 [Vibration]이 8 이상이면, 합 위력 +1\n[WhenUse] 자신의 진동 횟수를 8 소모하여 코인 위력 +1
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 8+ [Vibration], Clash Power +1\n[WhenUse] Consume 8 [Vibration] Count on self to gain Coin Power +1
   PL:
642. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
643. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 621 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
645. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL:
646. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 자신이 [TimeRentalTwoPersonality] 상태면, [TimeSuspend] 2 부여
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TimeRentalTwoPersonality], [TimeSuspend]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [TimeSuspend] = 시간 유예 / Time Moratorium
   EN: [OnSucceedAttack] If this unit is in a [TimeRentalTwoPersonality] state, inflict 2 [TimeSuspend]
   PL:
647. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">대상의 [Binding] 1 당 피해량 +5% (최대 20%)</style>\n[WhenUse] 대상의 [Vibration]이 8 이상이면, 합 위력 +<style="highlight">2</style>\n[WhenUse] 자신의 [Vibration] 횟수를 8 소모하여 코인 위력 +1
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Binding], [WhenUse], [Vibration]
   znaczenie tagów: [Binding] = 속박 / Bind; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">Deal +5% damage for every [Binding] on target (max 20%)</style>\n[WhenUse] If target has 8+ [Vibration], Clash Power +<style="highlight">2</style>\n[WhenUse] Consume 8 [Vibration] Count on self to gain Coin Power +1
   PL:
648. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +<style="highlight">3</style> [Vibration] Count
   PL:
649. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 625 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]<style="highlight"></style>
   PL:
651. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn<style="highlight"></style>
   PL:
652. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 스킬 사용시 [Vibration] 횟수를 소모했다면, 다음 턴에 [Binding] 2 부여</style>
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [Binding] = 속박 / Bind
   EN: <style="highlight">[OnSucceedAttack] If this unit consumed [Vibration] Count with Skill use, inflict 2 [Binding] next turn</style>
   PL:
653. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 자신이 [TimeRentalTwoPersonality] 상태면, [TimeSuspend] 2 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [TimeRentalTwoPersonality], [TimeSuspend]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [TimeSuspend] = 시간 유예 / Time Moratorium
   EN: [OnSucceedAttack] If this unit is in a [TimeRentalTwoPersonality] state, inflict 2 [TimeSuspend]<style="highlight"></style>
   PL:
654. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 4 — opis] <style="highlight">[OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_personality-09.json :: dataList[id=1090903].levelList[level=4].coinlist[#3].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL:
655. [Obrona (ulepszenia 1,4) — nazwa] 시간 대여
   źródło: Skills_personality-09.json :: dataList[id=1090904].levelList[level=1].name ; dataList[id=1090904].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Borrow Time
   PL:
656. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [StartBattle] [TimeRentalTwoPersonality] 상태가 아니면, 턴 종료 시 [TimeRentalTwoPersonality] 3 얻음 (턴 당 1회)\n[WhenUse] 이번 턴 동안 적에게 피격 시, 다음 턴에 대상에게 [Vibration] 2 부여 (턴 당 2회)
   źródło: Skills_personality-09.json :: dataList[id=1090904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [TimeRentalTwoPersonality], [WhenUse], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] If this unit is not in a [TimeRentalTwoPersonality] state, gain 3 [TimeRentalTwoPersonality] at Turn End (once per turn)\n[WhenUse] For this turn: when hit by an enemy, inflict 2 [Vibration] on target next turn (2 times per turn)
   PL:
657. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [StartBattle] [TimeRentalTwoPersonality] 상태가 아니면, 턴 종료 시 [TimeRentalTwoPersonality] 3 얻음 (턴 당 1회)\n[WhenUse] 이번 턴 동안 적에게 피격 시, 다음 턴에 대상에게 [Vibration] 2 부여 (턴 당 <style="highlight">6</style>회)
   źródło: Skills_personality-09.json :: dataList[id=1090904].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [TimeRentalTwoPersonality], [WhenUse], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] If this unit is not in a [TimeRentalTwoPersonality] state, gain 3 [TimeRentalTwoPersonality] at Turn End (once per turn)\n[WhenUse] For this turn: when hit by an enemy, inflict 2 [Vibration] on target next turn (<style="highlight">6 times</style> per turn)
   PL:
658. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — nazwa] 황금 시간 - 맞서기
   źródło: Passives.json :: dataList[id=1090901].name
   limit: do 40 znaków
   EN: Golden Time - Standoff
   PL:
659. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — opis] 턴 종료 시 체력이 16% ~ 20% 사이로 남았을 때, 전체 체력의 60%만큼 즉시 회복. 흐트러짐 상태 해제 (전투 당 1회)\n\n[TimeSuspend]를 보유한 대상과 합을 진행할 때 합 위력 +2\n[TimeSuspend]를 보유한 적에게 피해를 받을 때, 받는 피해량 -10%
   źródło: Passives.json :: dataList[id=1090901].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [TimeSuspend]
   znaczenie tagów: [TimeSuspend] = 시간 유예 / Time Moratorium
   EN: Turn End: If this unit's HP is between 16% ~ 20%, instantly heal up to 60% of Max HP, and recover from Stagger. (once per Encounter)\n\nWhen Clashing against targets that have [TimeSuspend], Clash Power +2\nTake -10% damage from targets that have [TimeSuspend]
   PL:
660. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — nazwa] T사식 격투술
   źródło: Passives.json :: dataList[id=1090921].name
   limit: do 40 znaków
   EN: T Corp. Martial Arts
   PL:
661. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — opis] 속도가 가장 빠른 아군 1명이 [Vibration]을 5 이상 보유한 적과 합 진행 시 합 위력 +1
   źródło: Passives.json :: dataList[id=1090921].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: To 1 ally with the fastest Speed: Clash Power +1 when Clashing against targets that have 5+ [Vibration]
   PL:
662. [Kwestia głosowa [get_10909_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=get_10909_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Kwestia głosowa [get_10909_1] (Identity Acquisition)] 후… 이런 구질구질한 색의 고기를 시간 내서 먹고 있다니… 차라리 아예 색을 모른 채 자랐으면 좋았을텐데.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=get_10909_1].dlg
   limit: do 160 znaków
   EN: Haah... I can't believe I'm wasting my time on this gross-colored meat. Makes me wish I'd never seen color growing up.
   PL:
664. [Kwestia głosowa [lobby_morning_10909_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=lobby_morning_10909_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Kwestia głosowa [lobby_morning_10909_1] (Morning Greeting)] 똑같은 하루의 시작이지만… 그래도 좋은 아침이야.\n어제와는 다른 하루였으면 좋겠네.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=lobby_morning_10909_1].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Just another day, huh. ... Still, good morning.\nHere's hoping today'll bring something new.
   PL:
666. [Kwestia głosowa [lobby_noon_10909_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=lobby_noon_10909_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Kwestia głosowa [lobby_noon_10909_1] (Afternoon Greeting)] 아직도 점심 시간이라니. 어휴, 시간 참 안 간다.\n언젠가는 내가 좀 더 특별한 시간 속에 살 줄 알았는데… 여전히 지루한 걸 보니, 그때까지 시간이 좀 걸리려나봐.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=lobby_noon_10909_1].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Is it still noon? Whew, what a slow day.\nY'know, I thought I'd be living in a bit more special time by now. But... given this boring, tedious life, I guess I've still got a ways to go.
   PL:
668. [Kwestia głosowa [lobby_night_10909_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=lobby_night_10909_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Kwestia głosowa [lobby_night_10909_1] (Evening Greeting)] T사에 있으면서 밤이 좋아졌어. 왜 그런줄 알아?\n훗, 빛이 사라지고 나면… 짙은 갈색의 세상도 조금은 볼만해지거든.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=lobby_night_10909_1].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The longer I stay in T Corp., the more I enjoy the night. Wanna know why?\nWhen the light of day fades... heh, this world of deep sepia becomes slightly more tolerable.
   PL:
670. [Kwestia głosowa [smalltalk_10909_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=smalltalk_10909_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Kwestia głosowa [smalltalk_10909_1] (Chatter #1)] 되도록 색이 있는 곳에서 불러줬으면 좋겠어, 단테.\n유리창 너머가 흐릿해서 잘 보이진 않아도… 기분이 그나마 나아져서 그래.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=smalltalk_10909_1].dlg
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Mind calling me over in places with color, Dante?\nI can't get a clear view of your world through this opaque window, but... it makes me feel better.
   PL:
672. [Kwestia głosowa [smalltalk_10909_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=smalltalk_10909_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Kwestia głosowa [smalltalk_10909_2] (Chatter #2)] 여기 T사도 윗사람 아랫사람 따지는 게 심하다니까. 한마디 할 수도 있는 거지, 쪼잔하게…\n그래도 요즘 같이 다니는 상사는 융통성이 있어서 좀 괜찮더라구. 앞으로도 이런 상사만 있으면 좋겠는데.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=smalltalk_10909_2].dlg
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This place is more hierarchical than it looks. The cocky higher-ups just can't take good-faith criticism, know what I mean? What a bunch of crybabies.\nWell, my current partner and boss is a bit more flexible, though. Hope I get assigned to people like her more often.
   PL:
674. [Kwestia głosowa [smalltalk_10909_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=smalltalk_10909_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Kwestia głosowa [smalltalk_10909_3] (Chatter #3)] 나도 시간을 징수하지만, 상대가 규칙을 많이 위반한 고액 체납자거나 대단한 거물이면 고등급 직원이, 금기를 어기면 금기사냥꾼이 처리해.\n그러니 평소엔 불심검문을 하고… 가끔은 미등록 발명품 단속까지… 사실상 잡일 담당이나 마찬가지네.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=smalltalk_10909_3].dlg
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I'm a Time Collector, but... if someone owes a lot of Time Tax, or if they're some big shot, they usually send the higher-ranking Staff after them. And if they broke a Taboo... well, they send the Taboo Hunters after them.\nSo I guess all I do are some stop-and-searches, patrols for unregistered inventions, and... yeah, I guess I'm saddled with all the busywork.
   PL:
676. [Kwestia głosowa [smalltalk_10909_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=smalltalk_10909_4].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Kwestia głosowa [smalltalk_10909_4] (Post-Uptie Chat 1)] 달마다 T사에선 징수직 전용 보급 시계에 시간을 넣어줘. 이걸로 체납자를 제압하거나 그럴 때 시간을 꺼내 쓸 수 있지.\n응? 당연히 부족하지~ 고등급 직원은 넉넉하게 넣어준다던데… 아직은 내 시간까지 써서 일해야지 뭐.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=smalltalk_10909_4].dlg
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: T Corp. gives an additional monthly time allowance to T Corp. Collector standard-issue timepieces. This is supposed to give us some extra time to use when taking down tax evaders.\nHm? Oh, it's nowhere near enough, of course. I heard that higher Class staff are given a lot more time, but... oh well. I guess it'll have to come out of my own pocket watch for now.
   PL:
678. [Kwestia głosowa [smalltalk_10909_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=smalltalk_10909_5].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Kwestia głosowa [smalltalk_10909_5] (Post-Uptie Chat 2)] 뭐, 너무 그렇게 보진 마. 납부할 시간세에 고작 3시간쯤 더 얹어서 징수한 거니까.\n열심히 일했는데… 내 몫의 시간 정도는 따로 챙길 수 있는 거 아냐? 이렇게라도 안 하면 우리도 시간이 부족하다구.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=smalltalk_10909_5].dlg
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hey, don't give me that look. It's simple: I'm just collecting three extra tax hours from them so I can skim a little off the top. Like, that's pocket change.\nI work hard, so I think I'm pretty justified in taking a little time for myself. C'mon, we're always running out of time too, y'know.
   PL:
680. [Kwestia głosowa [neglect_10909_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=neglect_10909_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Kwestia głosowa [neglect_10909_1] (Idle)] 너무 기다리게 하진 마. 너의 시간과 나의 시간은 가치가 다르니까…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=neglect_10909_1].dlg
   limit: do 120 znaków
   EN: Don't make me wait. My time and your time... aren't worth the same.
   PL:
682. [Kwestia głosowa [gacksung_10909_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=gacksung_10909_1].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Kwestia głosowa [gacksung_10909_1] (Uptying)] 이제는 저항해도 소용 없어. 시간을 땡겨온 나는, 너희보다 빠를 테니.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=gacksung_10909_1].dlg
   limit: do 140 znaków
   EN: It's pointless to resist. I'll always be one step ahead of you because I'm pulling time from the future.
   PL:
684. [Kwestia głosowa [formation_10909_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=formation_10909_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Kwestia głosowa [formation_10909_1] (Deployment)] 오늘은 시간을 얼마나 뜯으려나.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=formation_10909_1].dlg
   limit: do 120 znaków
   EN: How much time will I be robbing from them today, I wonder.
   PL:
686. [Kwestia głosowa [battleentry_10909_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battleentry_10909_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Kwestia głosowa [battleentry_10909_1] (Stage Entry)] 현시간부로 근무 시작.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battleentry_10909_1].dlg
   limit: do 120 znaków
   EN: Clocking in.
   PL:
688. [Kwestia głosowa [battle_select_10909_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_select_10909_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Kwestia głosowa [battle_select_10909_1] (Viewed in Battle)] 빨리 말해줄래? 말 그대로 시간이 아깝거든.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_select_10909_1].dlg
   limit: do 120 znaków
   EN: Can ya speak a bit faster? You're literally wasting my time.
   PL:
690. [Kwestia głosowa [battle_endcommand_10909_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_endcommand_10909_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Kwestia głosowa [battle_endcommand_10909_1] (Commencing Attack)] 얼마 안 걸릴 거야.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_endcommand_10909_1].dlg
   limit: do 120 znaków
   EN: This won't take long.
   PL:
692. [Kwestia głosowa [battle_enemy_break_10909_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_enemy_break_10909_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Kwestia głosowa [battle_enemy_break_10909_1] (Enemy Stagger)] 지불할 능력도 의사도 없다면…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_enemy_break_10909_1].dlg
   limit: do 120 znaków
   EN: If you lack both the capability and the will to make your payments...
   PL:
694. [Kwestia głosowa [battle_break_10909_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_break_10909_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Kwestia głosowa [battle_break_10909_1] (Staggered)] 윽…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_break_10909_1].dlg
   limit: do 120 znaków
   EN: Ugh...
   PL:
696. [Kwestia głosowa [battle_kill_10909_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_kill_10909_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Kwestia głosowa [battle_kill_10909_1] (Enemy Killed)] …남은 시간을 탈탈 털어주는 수밖에.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_kill_10909_1].dlg
   limit: do 120 znaków
   EN: ... then I have no choice but to completely drain your time.
   PL:
698. [Kwestia głosowa [battle_dead_10909_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_dead_10909_1].desc
   (powtórzenie elementu 291 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Kwestia głosowa [battle_dead_10909_1] (Death)] 하하… 이렇게 끝날 줄은…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_dead_10909_1].dlg
   limit: do 120 znaków
   EN: Ha... ha... so this is how... how it ends...?
   PL:
700. [Kwestia głosowa [choice_success_p_10909_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=choice_success_p_10909_2].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Kwestia głosowa [choice_success_p_10909_2] (Check Passed)] 후, 시간만 충분하면 이 정도는 쉽지.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=choice_success_p_10909_2].dlg
   limit: do 120 znaków
   EN: Haah... As long as I've got time, this is a piece of cake.
   PL:
702. [Kwestia głosowa [choice_fail_n_10909_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=choice_fail_n_10909_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Kwestia głosowa [choice_fail_n_10909_1] (Check Failed)] …시간이 부족해서 어쩔 수 없었다고.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=choice_fail_n_10909_1].dlg
   limit: do 120 znaków
   EN: ... Hey, I didn't have enough time for that.
   PL:
704. [Kwestia głosowa [battle_clear_10909_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_clear_10909_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Kwestia głosowa [battle_clear_10909_1] (Victory Cry)] 좋아. 예상보다 시간을 더 소모했지만, 누군가는 해야 할 일이니까.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_clear_10909_1].dlg
   limit: do 120 znaków
   EN: Well, that took more time than I expected. But someone had to do it.
   PL:
706. [Kwestia głosowa [battle_clear_ex_10909_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_clear_ex_10909_1].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Kwestia głosowa [battle_clear_ex_10909_1] (Extra Conditions Fulfilled)] 오… 이렇게 성과를 내는건 얼마만인지 몰라. 이제야 주목을 좀 받으려나.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_clear_ex_10909_1].dlg
   limit: do 160 znaków
   EN: Woah... I think that was a pretty good performance, all things considered. I wonder if I'll finally get some recognition.
   PL:
708. [Kwestia głosowa [battle_defeat_10909_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_defeat_10909_1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Kwestia głosowa [battle_defeat_10909_1] (Defeat Wail)] 이번 일은 실패했지만 너무 신경쓰진 마. 다시… 시간을 들여서 처음부터 하면 돼.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Tcorp_10909.json :: dataList[id=battle_defeat_10909_1].dlg
   limit: do 150 znaków
   EN: We failed this mission, but don't be too hard on yourself. We'll... take our time and try it again. From the start.
   PL:

## [000] Devyat' Assoc. North Section 3 — Rodion — 북부 제뱌찌 협회 3과
- ID Tożsamości: `10910` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 81 · szybkość: 3–5 / 3–6 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Rupture

710. [Karta Tożsamości — tytuł] 북부 제뱌찌 협회\n3과
   źródło: Personalities.json :: dataList[id=10910].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Devyat' Assoc.\nNorth Section 3
   PL:
711. [Karta Tożsamości — nazwa] 로쟈
   źródło: Personalities.json :: dataList[id=10910].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Karta Tożsamości — nazwa z tytułem] 로쟈
   źródło: Personalities.json :: dataList[id=10910].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Karta Tożsamości — opis] 로쟈의 열번째 인격
   źródło: Personalities.json :: dataList[id=10910].desc
   limit: do 120 znaków
   EN: Rodion's 10th Identity
   PL:
714. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 딜리버리 캐리어 - 붕괴 나이프
   źródło: Skills_personality-09.json :: dataList[id=1091001].levelList[level=1].name ; dataList[id=1091001].levelList[level=2].name ; dataList[id=1091001].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Courier Trunk - Decay Knife
   PL:
715. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 적중시 효과로 [Burst]을 부여하지 않는 대신 적중시 [Burst] 횟수를 소모하지 않음
   źródło: Skills_personality-09.json :: dataList[id=1091001].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not consume target's [Burst] Count On Hit, but does not inflict [Burst] with this Skill's On Hit effects
   PL:
716. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DevyatDimensionalSack] 1 얻음
   źródło: Skills_personality-09.json :: dataList[id=1091001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DevyatDimensionalSack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion
   EN: [OnSucceedAttack] Gain 1 [DevyatDimensionalSack]
   PL:
717. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-09.json :: dataList[id=1091001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
718. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[DevyatDimensionalSack]가 10 이상이거나 대상의 [Burst]이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 적중시 효과로 [Burst]을 부여하지 않는 대신 적중시 [Burst] 횟수를 소모하지 않음
   źródło: Skills_personality-09.json :: dataList[id=1091001].levelList[level=2].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DevyatDimensionalSack], [Burst], [WhenUse]
   znaczenie tagów: [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 10+ [DevyatDimensionalSack], or if target has 6+ [Burst], Coin Power +1</style>\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not consume target's [Burst] Count On Hit, but does not inflict [Burst] with this Skill's On Hit effects
   PL:
719. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DevyatDimensionalSack] 1 얻음\n<style="highlight">- [DevyatDimensionalSack]가 15 미만이면, [DevyatDimensionalSack] 1 추가로 얻음</style>
   źródło: Skills_personality-09.json :: dataList[id=1091001].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [DevyatDimensionalSack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion
   EN: [OnSucceedAttack] Gain 1 [DevyatDimensionalSack]\n<style="highlight">- If this unit has less than 15 [DevyatDimensionalSack], gain 1 additional [DevyatDimensionalSack]</style>
   PL:
720. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091001].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]<style="highlight"></style>
   PL:
721. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">[DevyatDimensionalSack] 10 또는 대상의 [Burst] 6당 코인 위력 +1 (최대 2)</style>\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 적중시 효과로 [Burst]을 부여하지 않는 대신 적중시 [Burst] 횟수를 소모하지 않음
   źródło: Skills_personality-09.json :: dataList[id=1091001].levelList[level=4].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DevyatDimensionalSack], [Burst], [WhenUse]
   znaczenie tagów: [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">Coin Power +1 for every 10 [DevyatDimensionalSack] or for every 6 [Burst] on target (max 2)</style>\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not consume target's [Burst] Count On Hit, but does not inflict [Burst] with this Skill's On Hit effects
   PL:
722. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DevyatDimensionalSack] 1 얻음\n- [DevyatDimensionalSack]가 15 미만이면, [DevyatDimensionalSack] 1 추가로 얻음<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091001].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [DevyatDimensionalSack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion
   EN: [OnSucceedAttack] Gain 1 [DevyatDimensionalSack]\n- If this unit has less than 15 [DevyatDimensionalSack], gain 1 additional [DevyatDimensionalSack]<style="highlight"></style>
   PL:
723. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] <style="highlight">3</style> 부여
   źródło: Skills_personality-09.json :: dataList[id=1091001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Burst]
   PL:
724. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 딜리버리 캐리어 - 가젯 사출
   źródło: Skills_personality-09.json :: dataList[id=1091002].levelList[level=1].name ; dataList[id=1091002].levelList[level=2].name ; dataList[id=1091002].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 50 znaków
   EN: Courier Trunk - Gadget Reveal
   PL:
725. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [DevyatDimensionalSack]가 10 이상이거나 대상의 [Burst]이 6 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬로 적중시 [Burst] 횟수를 소모하지 않음
   źródło: Skills_personality-09.json :: dataList[id=1091002].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [DevyatDimensionalSack], [Burst], [WhenUse]
   znaczenie tagów: [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: At 10+ [DevyatDimensionalSack], or if target has 6+ [Burst], Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not consume target's [Burst] Count On Hit
   PL:
726. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DevyatDimensionalSack] 1 얻음
   źródło: Skills_personality-09.json :: dataList[id=1091002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 716 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [Agility] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-09.json :: dataList[id=1091002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Agility]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttackHead] Gain 1 [Agility] next turn (once per turn)
   PL:
728. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [DevyatDimensionalSack] 10 또는 대상의 [Burst] 5당 [DefenseDown] 1 부여 (최대 2, 턴 당 1회)
   źródło: Skills_personality-09.json :: dataList[id=1091002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DevyatDimensionalSack], [Burst], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown] for every 10 [DevyatDimensionalSack] on self or for every 5 [Burst] on target (max 2, once per turn)
   PL:
729. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[DevyatDimensionalSack] 10 또는 대상의 [Burst] 6당 코인 위력 +1 (최대 2)</style>\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬로 적중시 [Burst] 횟수를 소모하지 않음
   źródło: Skills_personality-09.json :: dataList[id=1091002].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DevyatDimensionalSack], [Burst], [WhenUse]
   znaczenie tagów: [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">Coin Power +1 for every 10 [DevyatDimensionalSack] or for every 6 [Burst] on target (max 2)</style>\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not consume target's [Burst] Count On Hit
   PL:
730. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DevyatDimensionalSack] 1 얻음\n<style="highlight">- [DevyatDimensionalSack]가 15 미만이면, [DevyatDimensionalSack] 1 추가로 얻음</style>
   źródło: Skills_personality-09.json :: dataList[id=1091002].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [Agility] 1 얻음 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091002].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Agility]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttackHead] Gain 1 [Agility] next turn (once per turn)<style="highlight"></style>
   PL:
732. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [DevyatDimensionalSack] <style="highlight">5</style> 또는 대상의 [Burst] 5당 [DefenseDown] 1 부여 (최대 <style="highlight">4</style>, 턴 당 1회)
   źródło: Skills_personality-09.json :: dataList[id=1091002].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DevyatDimensionalSack], [Burst], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown] for every <style="highlight">5</style> [DevyatDimensionalSack] on self or for every 5 [Burst] on target (max <style="highlight">4</style>, once per turn)
   PL:
733. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">[DevyatDimensionalSack] 1당 피해량 +2% (최대 40%)</style>\n[DevyatDimensionalSack] 10 또는 대상의 [Burst] 6당 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬로 적중시 [Burst] 횟수를 소모하지 않음
   źródło: Skills_personality-09.json :: dataList[id=1091002].levelList[level=4].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DevyatDimensionalSack], [Burst], [WhenUse]
   znaczenie tagów: [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">Deal +2% damage for every [DevyatDimensionalSack] on self (max 40%)</style>\nCoin Power +1 for every 10 [DevyatDimensionalSack] or for every 6 [Burst] on target (max 2)\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not consume target's [Burst] Count On Hit
   PL:
734. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DevyatDimensionalSack] 1 얻음\n- [DevyatDimensionalSack]가 15 미만이면, [DevyatDimensionalSack] <style="highlight">2</style> 추가로 얻음
   źródło: Skills_personality-09.json :: dataList[id=1091002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [DevyatDimensionalSack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion
   EN: [OnSucceedAttack] Gain 1 [DevyatDimensionalSack]\n- If this unit has less than 15 [DevyatDimensionalSack], gain <style="highlight">2</style> additional [DevyatDimensionalSack]
   PL:
735. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [Agility] 1 얻음 (턴 당 1회)\n<style="highlight">- [DevyatDimensionalSack]가 15 이상이면, [Agility] 1 추가로 얻음</style>
   źródło: Skills_personality-09.json :: dataList[id=1091002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttackHead], [Agility], [DevyatDimensionalSack]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Agility] = 신속 / Haste; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion
   EN: [OnSucceedAttackHead] Gain 1 [Agility] next turn (once per turn)\n<style="highlight">- At 15+ [DevyatDimensionalSack], gain 1 additional [Agility]</style>
   PL:
736. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [DevyatDimensionalSack] 5 또는 대상의 [Burst] 5당 [DefenseDown] 1 부여 (최대 <style="highlight">6</style>, 턴 당 1회)
   źródło: Skills_personality-09.json :: dataList[id=1091002].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DevyatDimensionalSack], [Burst], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown] for every 5 [DevyatDimensionalSack] on self or for every 5 [Burst] on target (max <style="highlight">6</style>, once per turn)
   PL:
737. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 플루! 힘 좀 써줘!
   źródło: Skills_personality-09.json :: dataList[id=1091003].levelList[level=3].name ; dataList[id=1091003].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: I Trust Ya, Polu!
   PL:
738. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [DevyatDimensionalSack] 1당 피해량 +2% (최대 40%)\n[DevyatDimensionalSack]가 10 이상이거나 대상의 [Burst]이 6 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 적중시 효과로 [Burst] 횟수를 부여하지 않는 대신 마지막 코인을 재사용
   źródło: Skills_personality-09.json :: dataList[id=1091003].levelList[level=3].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [DevyatDimensionalSack], [Burst], [WhenUse]
   znaczenie tagów: [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: Deal +2% damage for every [DevyatDimensionalSack] (max 40%)\nAt 10+ [DevyatDimensionalSack] on self, or if target has 6+ [Burst], Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Count with its On Hit effects; instead, Reuse its last Coin
   PL:
739. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가 (턴 당 1회)
   źródło: Skills_personality-09.json :: dataList[id=1091003].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count (once per turn)
   PL:
740. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [DevyatDimensionalSack]가 15 이상이면, 피해량 +15%
   źródło: Skills_personality-09.json :: dataList[id=1091003].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DevyatDimensionalSack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion
   EN: [OnSucceedAttack] At 15+ [DevyatDimensionalSack], deal +15% damage
   PL:
741. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [EndSkill] 대상이 흐트러짐 상태가 되거나 사망하면, 다음 턴에 [Agility] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-09.json :: dataList[id=1091003].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Agility]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Agility] = 신속 / Haste
   EN: [EndSkill] If target is Staggered or defeated, gain 1 [Agility] next turn (once per turn)
   PL:
742. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [DevyatDimensionalSack] 1당 피해량 <style="highlight">+4%</style> (최대 <style="highlight">80%</style>)\n<style="highlight">[DevyatDimensionalSack] 10 또는 대상의 [Burst] 6당 코인 위력 +1 (최대 2)</style>\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 적중시 효과로 [Burst] 횟수를 부여하지 않는 대신 마지막 코인을 재사용
   źródło: Skills_personality-09.json :: dataList[id=1091003].levelList[level=4].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DevyatDimensionalSack], [Burst], [WhenUse]
   znaczenie tagów: [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: Deal <style="highlight">+4%</style> damage for every [DevyatDimensionalSack] (max <style="highlight">80%</style>)\n<style="highlight">Coin Power +1 for every 10 [DevyatDimensionalSack] on self or for every 6 [Burst] on target (max 2)</style>\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not inflict [Burst] Count with its On Hit effects; instead, Reuse its last Coin
   PL:
743. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가 (턴 당 1회)\n<style="highlight">- [DevyatDimensionalSack] 10당 [Burst] 횟수 1 추가로 증가 (최대 2)</style>
   źródło: Skills_personality-09.json :: dataList[id=1091003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Burst], [DevyatDimensionalSack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count (once per turn)\n<style="highlight">- Inflict +1 more [Burst] Count for every 10 [DevyatDimensionalSack] (max 2)</style>
   PL:
744. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [DevyatDimensionalSack]가 15 이상이면, 피해량 <style="highlight">+25%</style>
   źródło: Skills_personality-09.json :: dataList[id=1091003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DevyatDimensionalSack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion
   EN: [OnSucceedAttack] At 15+ [DevyatDimensionalSack], deal <style="highlight">+25%</style> damage
   PL:
745. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [EndSkill] 대상이 흐트러짐 상태가 되거나 사망하면, 다음 턴에 [Agility] <style="highlight">2</style> 얻음 (턴 당 1회)
   źródło: Skills_personality-09.json :: dataList[id=1091003].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkill], [Agility]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Agility] = 신속 / Haste
   EN: [EndSkill] If target is Staggered or defeated, gain <style="highlight">2</style> [Agility] next turn (once per turn)
   PL:
746. [Obrona (ulepszenia 1,4) — nazwa] 배달 보조 및 통제 시퀀스
   źródło: Skills_personality-09.json :: dataList[id=1091004].levelList[level=1].name ; dataList[id=1091004].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 9 · monety: 1 (+7)
   limit: do 50 znaków
   EN: Courier Support & Control Sequence
   PL:
747. [Obrona (ulepszenie 1) — opis] [StartBattle] [DevyatDimensionalSack]가 15 이상이면, ‘이건... 잠시 전략적 휴식이야!’로 발동함 (턴 당 1회)\n[StartBattle] 이 스킬로 발동 예정인 경우, 자신의 최대 체력의 ([DevyatDimensionalSack]/2)%만큼 보호막을 얻음 (최대 15%, 턴 당 1회)\n[WhenUse] [DevyatDimensionalSack] 2 얻음 (턴 당 1회)\n- [DevyatDimensionalSack]가 15 미만이면, [DevyatDimensionalSack] 1 추가로 얻음
   źródło: Skills_personality-09.json :: dataList[id=1091004].levelList[level=1].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DevyatDimensionalSack], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] At 15+ [DevyatDimensionalSack], activate 'Just... a Strategic Time Off!' instead (once per turn)\n[StartBattle] If this Skill is to be activated, gain ([DevyatDimensionalSack]/2)% of this unit's max HP as Shield (max 15%, once per turn)\n[WhenUse] Gain 2 [DevyatDimensionalSack] (once per turn)\n- At less than 15 [DevyatDimensionalSack], gain 1 additional [DevyatDimensionalSack]
   PL:
748. [Obrona (ulepszenie 4) — opis] [StartBattle] [DevyatDimensionalSack]가 15 이상이면, ‘이건... 잠시 전략적 휴식이야!’로 발동함 (턴 당 1회)\n[StartBattle] 이 스킬로 발동 예정인 경우, 자신의 최대 체력의 <style="highlight">([DevyatDimensionalSack])%</style>만큼 보호막을 얻음 (최대 <style="highlight">25%</style>, 턴 당 1회)\n[WhenUse] [DevyatDimensionalSack] 2 얻음 (턴 당 1회)\n- [DevyatDimensionalSack]가 15 미만이면, [DevyatDimensionalSack] 1 추가로 얻음
   źródło: Skills_personality-09.json :: dataList[id=1091004].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [DevyatDimensionalSack], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] At 15+ [DevyatDimensionalSack], activate 'Just... a Strategic Time Off!' instead (once per turn)\n[StartBattle] If this Skill is to be activated, gain <style="highlight">([DevyatDimensionalSack])%</style> of this unit's max HP as Shield (max <style="highlight">25%</style>, once per turn)\n[WhenUse] Gain 2 [DevyatDimensionalSack] (once per turn)\n- At less than 15 [DevyatDimensionalSack], gain 1 additional [DevyatDimensionalSack]
   PL:
749. [Obrona (ulepszenia 1,4) — nazwa] 이건... 잠시 전략적 휴식이야!
   źródło: Skills_personality-09.json :: dataList[id=1091005].levelList[level=1].name ; dataList[id=1091005].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 9 · monety: 1 (+7)
   limit: do 50 znaków
   EN: Just... a Strategic Time Off!
   PL:
750. [Obrona (ulepszenie 1) — opis] [StartBattle] 이 스킬로 발동 예정인 경우, 자신의 최대 체력의 ([DevyatDimensionalSack]/2)%만큼 보호막을 얻음 (최대 15%, 턴 당 1회)\n[EndBattle] [Retreat] 발동
   źródło: Skills_personality-09.json :: dataList[id=1091005].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DevyatDimensionalSack], [EndBattle], [Retreat]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [EndBattle] = [턴 종료 시] / [Turn End]; [Retreat] = 전략적 휴식 복지 모드 / Strategic R&R Mode
   EN: [StartBattle] If this Skill is to be activated, gain ([DevyatDimensionalSack]/2)% of this unit's max HP as Shield (max 15%, once per turn)\n[EndBattle] Activate [Retreat]
   PL:
751. [Obrona (ulepszenie 4) — opis] [StartBattle] 이 스킬로 발동 예정인 경우, 자신의 최대 체력의 <style="highlight">([DevyatDimensionalSack])%</style>만큼 보호막을 얻음 (최대 <style="highlight">25%</style>, 턴 당 1회)\n[EndBattle] [Retreat] 발동
   źródło: Skills_personality-09.json :: dataList[id=1091005].levelList[level=4].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [DevyatDimensionalSack], [EndBattle], [Retreat]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [EndBattle] = [턴 종료 시] / [Turn End]; [Retreat] = 전략적 휴식 복지 모드 / Strategic R&R Mode
   EN: [StartBattle] If this Skill is to be activated, gain <style="highlight">([DevyatDimensionalSack])%</style> of this unit's max HP as Shield (max <style="highlight">25%</style>, once per turn)\n[EndBattle] Activate [Retreat]
   PL:
752. [Pasywka bojowa (od ulepszenia 1) — nazwa] 한 번만 봐주면 진짜 제대로 배달 끝낼게!
   źródło: Passives.json :: dataList[id=1091002].name
   limit: do 60 znaków
   EN: Lemme go and I swear I'll make it in time!
   PL:
753. [Pasywka bojowa (od ulepszenia 1) — opis] <연속 전투 전용> '[Retreat]'가 발동하여 퇴각한 다음 다시 전투에 참여할 때, [DevyatDimensionalSack]가 절반으로 감소 (전투당 1회, 올림하여 처리)
   źródło: Passives.json :: dataList[id=1091002].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [Retreat], [DevyatDimensionalSack]
   znaczenie tagów: [Retreat] = 전략적 휴식 복지 모드 / Strategic R&R Mode; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion
   EN: <For Chain Battles> When, after Retreating with '[Retreat]', if this unit rejoins the battle, halve the [DevyatDimensionalSack] value (once per Encounter, rounded up)
   PL:
754. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] [DevyatDimensionalSack] 절반으로 감소
   źródło: Passives.json :: dataList[id=1091002].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DevyatDimensionalSack]
   znaczenie tagów: [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion
   EN: Halve the [DevyatDimensionalSack] value
   PL:
755. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — nazwa] 신속 배달
   źródło: Passives.json :: dataList[id=1091001].name
   limit: do 40 znaków
   EN: Speedy Delivery
   PL:
756. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — opis] 턴 시작 시 속도가 6 이상이거나 [Agility]을 보유하였다면, 자신의 최대 체력의 ([DevyatDimensionalSack]/2)%만큼 보호막을 얻음 (최대 15%)\n\n퇴각 시, 다음 턴에 아군 둘에게 [ParryingResultUp] 1 부여 (대기 해제된 인격에게 우선으로 부여되며, 그 다음으로는 편성 순서가 빠른 순으로 적용)
   źródło: Passives.json :: dataList[id=1091001].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [DevyatDimensionalSack], [ParryingResultUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Turn Start: At 6+ Speed, or if this unit has [Agility], gain ([DevyatDimensionalSack]/2)% of this unit's max HP as Shield (max 15%)\n\nUpon Retreat, apply 1 [ParryingResultUp] to 2 allies next turn (prioritizes Substituted units first, then in Deployment order)
   PL:
757. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — podsumowanie] 최대 체력의 ([DevyatDimensionalSack]/2)%만큼 보호막 얻음\n퇴각 시, 무작위 아군 둘에게 [ParryingResultUp] 1 부여
   źródło: Passives.json :: dataList[id=1091001].summary
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [DevyatDimensionalSack], [ParryingResultUp]
   znaczenie tagów: [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Gain ([DevyatDimensionalSack]/2)% of this unit's max HP as Shield\nUpon Retreat, apply 1 [ParryingResultUp] to 2 random allies
   PL:
758. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 신속 배달
   źródło: Passives.json :: dataList[id=1091011].name
   (powtórzenie elementu 755 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — opis] 턴 시작 시 속도가 6 이상이거나 [Agility]을 보유하였다면, 자신의 최대 체력의 <style="highlight">([DevyatDimensionalSack])%</style>만큼 보호막을 얻음 (최대 <style="highlight">20%</style>)\n\n퇴각 시, 다음 턴에 아군 둘에게 [ParryingResultUp] 1 부여 (대기 해제된 인격에게 우선으로 부여되며, 그 다음으로는 편성 순서가 빠른 순으로 적용)\n<style="highlight">- 자신이 보유한 [DevyatDimensionalSack] 15당 유지 턴 수 1 증가 (최대 2턴 증가)</style>
   źródło: Passives.json :: dataList[id=1091011].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Agility], [DevyatDimensionalSack], [ParryingResultUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Turn Start: At 6+ Speed, or if this unit has [Agility], gain <style="highlight">([DevyatDimensionalSack])%</style> of this unit's max HP as Shield (max <style="highlight">20%</style>)\n\nUpon Retreat, apply 1 [ParryingResultUp] to 2 allies next turn (prioritizes Substituted units first, then in Deployment order)\n<style="highlight">- Lasts for 1 additional turn for every 15 [DevyatDimensionalSack] on self (2 more turns max)</style>
   PL:
760. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — podsumowanie] 최대 체력의 ([DevyatDimensionalSack])%만큼 보호막 얻음\n퇴각 시, 무작위 아군 둘에게 [ParryingResultUp] 1 부여
   źródło: Passives.json :: dataList[id=1091011].summary
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [DevyatDimensionalSack], [ParryingResultUp]
   znaczenie tagów: [DevyatDimensionalSack] = 딜리버리 캐리어 - 로쟈 / Courier Trunk - Rodion; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Gain ([DevyatDimensionalSack])% of this unit's max HP as Shield\nUpon Retreat, apply 1 [ParryingResultUp] to 2 random allies
   PL:
761. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Glut.) — nazwa] 우수 배달부
   źródło: Passives.json :: dataList[id=1091021].name
   limit: do 40 znaków
   EN: Outstanding Courier
   PL:
762. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Glut.) — opis] 속도가 가장 빠른 아군 1명의 [Burst] 위력, 횟수를 부여하는 스킬의 합 위력 +1
   źródło: Passives.json :: dataList[id=1091021].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: To 1 ally with the fastest Speed: Clash Power +1 to Skills that apply [Burst] Potency or Count
   PL:
763. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Glut.) — podsumowanie] [Burst] 위력, 횟수를 부여하는 스킬의 합 위력 +1
   źródło: Passives.json :: dataList[id=1091021].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Skills that apply [Burst] Potency or Count gain Clash Power +1
   PL:
764. [Kwestia głosowa [get_10910_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=get_10910_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Kwestia głosowa [get_10910_1] (Identity Acquisition)] 후우… 쉴 만큼 쉬었으니까, 다시 가볼까? 다들, 옷 단단히 여미고~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=get_10910_1].dlg
   limit: do 120 znaków
   EN: Phew... Now that's enough rest. Let's keep on keeping on, everyone. And stay toasty~
   PL:
766. [Kwestia głosowa [lobby_morning_10910_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=lobby_morning_10910_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Kwestia głosowa [lobby_morning_10910_1] (Morning Greeting)] 으으, 이 지방은 해가 떠도 너무 춥단 말이지… 야영하다가 죽는 거 아닌가 싶어.\n뭐, 진짜 죽을 것 같이 체온이 내려가면 가방이 알아서 온열기능을 켜버리겠지만…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=lobby_morning_10910_1].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Nngh... It's so cold here, even during midday. I'm worried about freezing to death every time I try to sleep on the road.\nWell, if it does get cold enough to kill me, I guess the trunk will automatically activate its thermal protection function...
   PL:
768. [Kwestia głosowa [lobby_noon_10910_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=lobby_noon_10910_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Kwestia głosowa [lobby_noon_10910_1] (Afternoon Greeting)] 자, 체크포인트 17까지 왔네… 으~ 오늘 점심은 여기서 먹자구. 매번 걸으면서 에너지바로 처리하는 것도 지겹잖아? 플루, 가방 열어.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=lobby_noon_10910_1].dlg
   limit: do 220 znaków
   EN: Right, let's see... we're at checkpoint 17. Nngh~ Let's lunch here, how 'bout that? Aren'tcha tired of munching on energy bars for three meals straight? Open up, Polu!
   PL:
770. [Kwestia głosowa [lobby_night_10910_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=lobby_night_10910_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Kwestia głosowa [lobby_night_10910_1] (Evening Greeting)] 해 떨어지면 빨리 잘 준비를 해야 해. 지반도 좀 다져놓고…\n저번에도 배달 시간이 살짝 촉박해서 밤까지 움직였다가, 크레바스에 빠져서 죽을 뻔했다니까?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=lobby_night_10910_1].dlg
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Better get ready to sleep ASAP when the sun goes down. Remember to flatten the terrain you're about to lie down on, too...\nWanna know what happened when we tried to move through the night because we were running low on time? I almost fell into a crevasse and died.
   PL:
772. [Kwestia głosowa [smalltalk_10910_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=smalltalk_10910_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Kwestia głosowa [smalltalk_10910_1] (Chatter #1)] 배달일이 재밌어서 하는 건 아니지. 뭐, 처음엔 로망도 있고 그러긴 했지만…\n아, 그래도 돌아다니면서 바뀌는 풍경을 보는 건 아직도 즐겁긴 해.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=smalltalk_10910_1].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Well, I don't do delivery work for fun. I guess there was some sense of purpose at first, but...\nOh! Yeah, I still love seeing all the sights as I move across the City, though.
   PL:
774. [Kwestia głosowa [smalltalk_10910_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=smalltalk_10910_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Kwestia głosowa [smalltalk_10910_2] (Chatter #2)] 이 가방에는 뭐든지 들어간다구~ 물론 한도가 있긴 하지만… 그래도 아무리 무거운 걸 넣더라도 가방의 무게가 바뀌지 않는다는 건 장점이지! <color=#9eada4><size=60%><i>[주의. 허가된 배달품 외의 물품 보관은-]</i></size></color> 에헤이~ 플루, 쉿?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=smalltalk_10910_2].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <color=#9eada4>, <size=60%>, <i>, </i>, </size>, </color>
   EN: You can fit pretty much anything into these trunks~ If they fit the maximum capacity, of course... Still, it's a pretty big plus that the weight doesn't change no matter what you stuff into 'em! <color=#9eada4><size=60%><i>[WARNING. Unauthorized storage of non-designated delivery items is—]</i></size></color> Ehehe, shush, Polu!
   PL:
776. [Kwestia głosowa [smalltalk_10910_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=smalltalk_10910_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Kwestia głosowa [smalltalk_10910_3] (Chatter #3)] 아… 이 가방? 개인용으로 새거가 지급되고 그러는 건 아니고. 글쎄~ 이게 몇 대째 물건일까… 배달 나갔다가 죽어버린 사람의 가방을 회수해서 쓰고, 또 쓰고… 그러는 거거든. 하하.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=smalltalk_10910_3].dlg
   limit: do 400 znaków
   EN: Ah... what, this trunk? Nah, we don't get personalized trunks. Hmm~ how many people's hands used this trunk, I wonder... Oh, yeah. When someone gets killed in a delivery, we send people to pick it up and it becomes theirs. And when they die, someone else goes out to pick it up, and... ya get the gist, right? Ha ha.
   PL:
778. [Kwestia głosowa [smalltalk_10910_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=smalltalk_10910_4].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Kwestia głosowa [smalltalk_10910_4] (Post-Uptie Chat 1)] 좋아~ 이 정도면 금방 처리하고 떠날 수 있겠다. 너희들도 밍기적거리지 말고! 괜히 배달비 삭감된다고 나중에 툴툴대지 말고~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=smalltalk_10910_4].dlg
   limit: do 230 znaków
   EN: Niiice~ This looks like a piece of cake. Quit dragging your feet, let's get a move on, people! And don'tcha dare complain to me later about getting paid a reduced delivery fee~
   PL:
780. [Kwestia głosowa [smalltalk_10910_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=smalltalk_10910_5].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Kwestia głosowa [smalltalk_10910_5] (Post-Uptie Chat 2)] 아우 무거워… 남부 애들은 수트케이스 같은 걸 갖고 다닌다던데, 우리는 왜 이렇게 무거운 걸 쓰나 몰라… 한 번 휘두를 때마다 어깨가 빠질 것 같단 말이야.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=smalltalk_10910_5].dlg
   limit: do 290 znaków
   EN: Nngh, so heavy... I heard the guys down south carry around a slimmer suitcase, so what's up with us in the north getting saddled with something so bulky? I feel like I'm going to dislocate my shoulder swingin' this thing around.
   PL:
782. [Kwestia głosowa [neglect_10910_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=neglect_10910_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Kwestia głosowa [neglect_10910_1] (Idle)] 후우… 요 근처에 육포를 숨겨뒀던 것 같은데… <color=#9eada4><size=60%><i>[배달 좌표 이외에서의 잠금 해제를 확인]</i></size></color> 앗, 기록 삭제 버튼이 어디 있더라?! <color=#9eada4><size=60%><i>[권한 없음]</i></size></color>
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=neglect_10910_1].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#9eada4>, <size=60%>, <i>, </i>, </size>, </color>
   EN: Hmm... I think I hid a pack of beef jerky somewhere in there... <color=#9eada4><size=60%><i>[Unauthorized lock release outside of delivery coordinates detected]</i></size></color> Crap, how do I wipe that data?! <color=#9eada4><size=60%><i>[Unauthorized behavior detected]</i></size></color>
   PL:
784. [Kwestia głosowa [gacksung_10910_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=gacksung_10910_1].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Kwestia głosowa [gacksung_10910_1] (Uptying)] 딜리버리 캐리어 작동 1단계… 자, 3단계까지 가기 전에 끝낸다!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=gacksung_10910_1].dlg
   limit: do 120 znaków
   EN: Courier Trunk activation level 1... Alright, let's take care of this before it gets to 3!
   PL:
786. [Kwestia głosowa [formation_10910_1] — sytuacja] 인격 편성 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=formation_10910_1].desc
   limit: do 120 znaków
   EN: Deployment 1
   PL:
787. [Kwestia głosowa [formation_10910_1] (Deployment 1)] 일 들어왔네… 플루, 가볼까? <color=#9eada4><size=60%><i>[기동음]</i></size></color>
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=formation_10910_1].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#9eada4>, <size=60%>, <i>, </i>, </size>, </color>
   EN: Looks like a job... Let's go, Polu. <color=#9eada4><size=60%><i>[Activating]</i></size></color>
   PL:
788. [Kwestia głosowa [formation_10910_2] — sytuacja] 인격 편성 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=formation_10910_2].desc
   limit: do 120 znaków
   EN: Deployment 2
   PL:
789. [Kwestia głosowa [formation_10910_2] (Deployment 2)] 이번 플루드니차는 재미없긴 해도 착실한 것 같네~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=formation_10910_2].dlg
   limit: do 120 znaków
   EN: Welp, this Poludnitsa is kinda boring, but at least she's competent~
   PL:
790. [Kwestia głosowa [battleentry_10910_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battleentry_10910_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Kwestia głosowa [battleentry_10910_1] (Stage Entry)] 늦겠다, 뛰자!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battleentry_10910_1].dlg
   limit: do 120 znaków
   EN: Guys, we're gonna be late! Run!
   PL:
792. [Kwestia głosowa [battle_select_10910_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_select_10910_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Kwestia głosowa [battle_select_10910_1] (Viewed in Battle)] 이따가 얘기해. 배달 시간 끌면 위험해서.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_select_10910_1].dlg
   limit: do 120 znaków
   EN: Talk later, hmm? Can't be late for delivery.
   PL:
794. [Kwestia głosowa [battle_endcommand_10910_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_endcommand_10910_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Kwestia głosowa [battle_endcommand_10910_1] (Commencing Attack)] 길 좀 막지 마!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_endcommand_10910_1].dlg
   limit: do 120 znaków
   EN: Get outta my way, c'mon!
   PL:
796. [Kwestia głosowa [battle_enemy_break_10910_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_enemy_break_10910_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Kwestia głosowa [battle_enemy_break_10910_1] (Enemy Stagger)] 시간 끌지 말고…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_enemy_break_10910_1].dlg
   limit: do 120 znaków
   EN: Stop wasting my time...
   PL:
798. [Kwestia głosowa [battle_break_10910_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_break_10910_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Kwestia głosowa [battle_break_10910_1] (Staggered)] 윽…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_break_10910_1].dlg
   limit: do 120 znaków
   EN: Ngh...
   PL:
800. [Kwestia głosowa [battle_kill_10910_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_kill_10910_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Kwestia głosowa [battle_kill_10910_1] (Enemy Killed)] 길에서 비켜!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_kill_10910_1].dlg
   limit: do 120 znaków
   EN: ... and get outta my way!
   PL:
802. [Kwestia głosowa [battle_dead_10910_1] — sytuacja] 본인 사망 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_dead_10910_1].desc
   limit: do 120 znaków
   EN: Death #1
   PL:
803. [Kwestia głosowa [battle_dead_10910_1] (Death #1)] 아… 이렇게 나도 가방만… 남기게 되나…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_dead_10910_1].dlg
   limit: do 120 znaków
   EN: Ah... I'll be... just another trunk recovery mission, huh...
   PL:
804. [Kwestia głosowa [battle_dead_10910_2] — sytuacja] 본인 사망 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_dead_10910_2].desc
   limit: do 120 znaków
   EN: Death #2
   PL:
805. [Kwestia głosowa [battle_dead_10910_2] (Death #2)] 아, 안돼! 여기서 금방 벗어날 테니까 <color=#9eada4><size=60%><i>[가방 작동]</i></size></color>
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_dead_10910_2].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#9eada4>, <size=60%>, <i>, </i>, </size>, </color>
   EN: N-no, stop! I'll get moving right now, oka— <color=#9eada4><size=60%><i>[Trunk Activated]</i></size></color>
   PL:
806. [Kwestia głosowa [choice_success_p_10910_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=choice_success_p_10910_2].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Kwestia głosowa [choice_success_p_10910_2] (Check Passed)] 자, 됐지? 시간 없는데 이런걸 시켜…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=choice_success_p_10910_2].dlg
   limit: do 120 znaków
   EN: Done. Happy now? Jeez, it's not like I'm rolling in time...
   PL:
808. [Kwestia głosowa [choice_fail_n_10910_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=choice_fail_n_10910_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Kwestia głosowa [choice_fail_n_10910_1] (Check Failed)] 아… 이런 거 잘 못하는데, 시간만 뺏고 말이야…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=choice_fail_n_10910_1].dlg
   limit: do 120 znaków
   EN: Ah... I'm not so good at these. Ugh, what a waste of my time...
   PL:
810. [Kwestia głosowa [battle_clear_10910_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_clear_10910_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Kwestia głosowa [battle_clear_10910_1] (Victory Cry)] 생각보다 시간을 너무 썼는데… 뭐, 배달 가방에 먹히는 것보단 낫지. 자, 바로 뛴다!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_clear_10910_1].dlg
   limit: do 180 znaków
   EN: That took way longer than I expected, but... eh, better than getting devoured by the delivery box. Alrighty, let's get back on the road!
   PL:
812. [Kwestia głosowa [battle_clear_ex_10910_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_clear_ex_10910_1].desc
   limit: do 120 znaków
   EN: Extra Condition Fulfilled
   PL:
813. [Kwestia głosowa [battle_clear_ex_10910_1] (Extra Condition Fulfilled)] 음~ 여유로웠어. 아예 여기서 밥 좀 먹다가 출발해도 될 것 같은데? 다들 식량 꺼내!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_clear_ex_10910_1].dlg
   limit: do 140 znaków
   EN: Mm~ we've got plenty of time to spare. I think we can rest up here for a meal? Guys, time to chow down!
   PL:
814. [Kwestia głosowa [battle_defeat_10910_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_defeat_10910_1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Kwestia głosowa [battle_defeat_10910_1] (Defeat Wail)] …빨리, 빨리 다시 싸워야 해. 이러다가 진짜… 배달을… 못 마칠지도 몰라… 그렇게 되면…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Devjat_10910.json :: dataList[id=battle_defeat_10910_1].dlg
   limit: do 170 znaków
   EN: ... W-we gotta try this fight again now. C'mon, let's go at 'em right now. I might be late for delivery, for real... T-then...
   PL:

## [000] The Princess of La Manchaland — Rodion — 라만차랜드 공주
- ID Tożsamości: `10911` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 79 · szybkość: 2–5 / 3–6 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Bleed, Rupture

816. [Karta Tożsamości — tytuł] 라만차랜드\n공주
   źródło: Personalities.json :: dataList[id=10911].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Princess\nof La Manchaland
   PL:
817. [Karta Tożsamości — nazwa] 로쟈
   źródło: Personalities.json :: dataList[id=10911].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Karta Tożsamości — nazwa z tytułem] 로쟈
   źródło: Personalities.json :: dataList[id=10911].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Karta Tożsamości — opis] 로쟈의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10911].desc
   limit: do 120 znaków
   EN: Rodion's 11th Identity
   PL:
820. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 물러가도록...
   źródło: Skills_personality-09.json :: dataList[id=1091101].levelList[level=1].name ; dataList[id=1091101].levelList[level=2].name ; dataList[id=1091101].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Begone...
   PL:
821. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [StartBattle] 자신과 최대 체력이 가장 높은 아군 1명에게 [BloodDinner]을 최대 20 소모하여, [BloodDinner] 10당 [BloomingThornsRodionFirst] 1 부여 (턴 당 최대 2회)\n- <혈귀>인 아군에게 우선 부여\n- 부여한 아군이 <혈귀>면, [BloomingThornsRodionFirst] 1 추가 부여\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음
   źródło: Skills_personality-09.json :: dataList[id=1091101].levelList[level=1].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [BloodDinner], [BloomingThornsRodionFirst], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BloodDinner] = 혈찬 / Bloodfeast; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn; [Laceration] = 출혈 / Bleed
   EN: [StartBattle] On self and 1 ally that has the highest max HP: consume up to 20 [BloodDinner] and apply 1 [BloomingThornsRodionFirst] for every 10 [BloodDinner] this unit consumed (2 times per turn)\n- Prioritizes <Bloodfiend> allies\n- If the affected ally is a <Bloodfiend>, this unit applies 1 additional [BloomingThornsRodionFirst]\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]
   PL:
822. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1091101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
823. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1091101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
824. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [StartBattle] 자신과 최대 체력이 가장 높은 아군 1명에게 [BloodDinner]을 최대 20 소모하여, [BloodDinner] 10당 [BloomingThornsRodionFirst] 1 부여 (턴 당 최대 2회)\n- <혈귀>인 아군에게 우선 부여\n- 부여한 아군이 <혈귀>면, [BloomingThornsRodionFirst] 1 추가 부여\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n<style="highlight">[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-09.json :: dataList[id=1091101].levelList[level=2].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [BloodDinner], [BloomingThornsRodionFirst], [Laceration], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BloodDinner] = 혈찬 / Bloodfeast; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] On self and 1 ally that has the highest max HP: consume up to 20 [BloodDinner] and apply 1 [BloomingThornsRodionFirst] for every 10 [BloodDinner] this unit consumed (2 times per turn)\n- Prioritizes <Bloodfiend> allies\n- If the affected ally is a <Bloodfiend>, this unit applies 1 additional [BloomingThornsRodionFirst]\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>
   PL:
825. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1091101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]<style="highlight"></style>
   PL:
826. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091101].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1091101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]<style="highlight"></style>
   PL:
827. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [StartBattle] 자신과 최대 체력이 가장 높은 아군 1명에게 [BloodDinner]을 최대 20 소모하여, [BloodDinner] 10당 [BloomingThornsRodionFirst] 1 부여 (턴 당 최대 2회)\n- <혈귀>인 아군에게 우선 부여\n- 부여한 아군이 <혈귀>면, [BloomingThornsRodionFirst] 1 추가 부여\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n<style="highlight">[WhenUse] 대상의 [Laceration] 6 당 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-09.json :: dataList[id=1091101].levelList[level=4].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [BloodDinner], [BloomingThornsRodionFirst], [Laceration], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BloodDinner] = 혈찬 / Bloodfeast; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] On self and 1 ally that has the highest max HP: consume up to 20 [BloodDinner] and apply 1 [BloomingThornsRodionFirst] for every 10 [BloodDinner] this unit consumed (2 times per turn)\n- Prioritizes <Bloodfiend> allies\n- If the affected ally is a <Bloodfiend>, this unit applies 1 additional [BloomingThornsRodionFirst]\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n<style="highlight">[WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)</style>
   PL:
828. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 흩뿌리며 갈려나가라
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=1].name ; dataList[id=1091102].levelList[level=2].name ; dataList[id=1091102].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: In Finely Ground Mistfall
   PL:
829. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [StartBattle] 자신과 최대 체력이 가장 낮은 아군 1명에게 [Enhancement] 1 부여, [BloodDinner]을 최대 30 소모하여 [BloodDinner] 10당 [BloomingThornsRodionFirst] 1 부여 (턴 당 최대 2회)\n- <혈귀>인 아군에게 우선 부여\n- 부여한 아군이 <혈귀>면, [Enhancement] 1, [BloomingThornsRodionFirst] 2 추가 부여\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=1].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Enhancement], [BloodDinner], [BloomingThornsRodionFirst], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [BloodDinner] = 혈찬 / Bloodfeast; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn; [Laceration] = 출혈 / Bleed
   EN: [StartBattle] On self and 1 ally that has the lowest max HP: apply 1 [Enhancement], consume up to 30 [BloodDinner] and apply 1 [BloomingThornsRodionFirst] for every 10 [BloodDinner] this unit consumed (2 times per turn)\n- Prioritizes <Bloodfiend> allies\n- If the affected ally is a <Bloodfiend>, this unit applies additional 1 [Enhancement] and 2 [BloomingThornsRodionFirst]\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]
   PL:
830. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL:
831. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
832. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 823 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [StartBattle] 자신과 최대 체력이 가장 낮은 아군 1명에게 [Enhancement] 1을 부여, [BloodDinner]을 최대 30 소모하여 [BloodDinner] 10당 [BloomingThornsRodionFirst] 1 부여 (턴 당 최대 2회)\n- <혈귀>인 아군에게 우선 부여\n- 부여한 아군이 <혈귀>면, [Enhancement] 1, [BloomingThornsRodionFirst] 2 추가 부여\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n<style="highlight">[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=2].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [Enhancement], [BloodDinner], [BloomingThornsRodionFirst], [Laceration], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [BloodDinner] = 혈찬 / Bloodfeast; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] On self and 1 ally that has the lowest max HP: apply 1 [Enhancement], consume up to 30 [BloodDinner] and apply 1 [BloomingThornsRodionFirst] for every 10 [BloodDinner] this unit consumed (2 times per turn)\n- Prioritizes <Bloodfiend> allies\n- If the affected ally is a <Bloodfiend>, this unit applies additional 1 [Enhancement] and 2 [BloomingThornsRodionFirst]\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>
   PL:
835. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Burst] Count
   PL:
836. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Laceration] Count
   PL:
837. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1091102].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 826 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1091102].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 825 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [StartBattle] 자신과 최대 체력이 가장 낮은 아군 1명에게 [Enhancement] 1 부여, [BloodDinner]을 최대 30 소모하여 [BloodDinner] 10당 [BloomingThornsRodionFirst] 1 부여 (턴 당 최대 2회)\n- <혈귀>인 아군에게 우선 부여\n- 부여한 아군이 <혈귀>면, [Enhancement] 1, [BloomingThornsRodionFirst] 2 추가 부여\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n<style="highlight">[WhenUse] 대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=4].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [Enhancement], [BloodDinner], [BloomingThornsRodionFirst], [Laceration], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [BloodDinner] = 혈찬 / Bloodfeast; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] On self and 1 ally that has the lowest max HP: apply 1 [Enhancement], consume up to 30 [BloodDinner] and apply 1 [BloomingThornsRodionFirst] for every 10 [BloodDinner] this unit consumed (2 times per turn)\n- Prioritizes <Bloodfiend> allies\n- If the affected ally is a <Bloodfiend>, this unit applies additional 1 [Enhancement] and 2 [BloomingThornsRodionFirst]\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n<style="highlight">[WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)</style>
   PL:
840. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count<style="highlight"></style>
   PL:
841. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091102].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count<style="highlight"></style>
   PL:
842. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 축제는 끝날거야
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=3].name ; dataList[id=1091103].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: The Festival Will End
   PL:
843. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [BeforeUse] 자신의 [BloomingThornsRodionFirst]가 25 이상이면, '돈키호테류 경혈[TabExplain] 오의 피날레'로 발동됨\n[WhenUse] 자신과 아군 (최대 공명 수)명에게 이번 턴과 다음 턴에 [FestivalFeverRodion] 3 + (자신의 [BloodDinner_Accumulation] 50 당 1) 부여 (최대 10)\n[WhenUse] 자신과 아군 (최대 공명 수)명에게 [BloomingThornsRodionFirst] 3 부여
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=3].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [BloomingThornsRodionFirst], [TabExplain], [WhenUse], [FestivalFeverRodion], [BloodDinner_Accumulation]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn; [WhenUse] = [사용시] / [On Use]; [FestivalFeverRodion] = 축제의 열기 / Festive Fever; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed
   EN: [BeforeUse] At 25+ [BloomingThornsRodionFirst], activate 'Ascendant Don Quixote Hardblood[TabExplain] Arts - The Finale' instead\n[WhenUse] To self and (highest Reson.) allies: apply (3 + (1 for every 50 [BloodDinner_Accumulation] by this unit) [FestivalFeverRodion] this turn and next turn (max 10)\n[WhenUse] To self and (highest Reson.) allies: apply 3 [BloomingThornsRodionFirst]
   PL:
844. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 830 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
846. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 823 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 823 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
850. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [BeforeUse] 자신의 [BloomingThornsRodionFirst]가 25 이상이면, '돈키호테류 경혈[TabExplain] 오의 피날레'로 발동됨\n<style="highlight">[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신과 아군 (최대 공명 수)명에게 이번 턴과 다음 턴에 [FestivalFeverRodion] 3 + (자신의 [BloodDinner_Accumulation] 50 당 1) 부여 (최대 10)\n[WhenUse] 자신과 아군 (최대 공명 수)명에게 [BloomingThornsRodionFirst] 3 부여
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=4].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeUse], [BloomingThornsRodionFirst], [TabExplain], [WhenUse], [Laceration], [FestivalFeverRodion], [BloodDinner_Accumulation]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [FestivalFeverRodion] = 축제의 열기 / Festive Fever; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed
   EN: [BeforeUse] At 25+ [BloomingThornsRodionFirst], activate 'Ascendant Don Quixote Hardblood[TabExplain] Arts - The Finale' instead\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>\n[WhenUse] To self and (highest Reson.) allies: apply (3 + (1 for every 50 [BloodDinner_Accumulation] by this unit) [FestivalFeverRodion] this turn and next turn (max 10)\n[WhenUse] To self and (highest Reson.) allies: apply 3 [BloomingThornsRodionFirst]
   PL:
851. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count<style="highlight"></style>
   PL:
852. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count<style="highlight"></style>
   PL:
853. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 826 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 825 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 826 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
856. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091103].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 825 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Umiejętność 4 (×0) (ulepszenia 1,4) — nazwa] 돈키호테류 경혈 오의 피날레
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=1].name ; dataList[id=1091105].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 3 (+5)
   limit: do 70 znaków
   EN: Ascendant Don Quixote Hardblood Arts - The Finale
   PL:
858. [Umiejętność 4 (×0) (ulepszenie 1) — opis] [WhenUse] 자신과 아군 (최대 공명 수)명에게 이번 턴과 다음 턴에 [FestivalFeverRodion] 5 + (자신의 [BloodDinner_Accumulation] 50 당 1) 부여 (최대 10)\n[WhenUse] 자신과 아군 (최대 공명 수)명에게 [BloomingThornsRodionFirst] 5 부여\n자신의 [BloodDinner_Accumulation] 5 당 피해량 1% 증가 (최대 50%)\n[EndSkill] 자신의 [BloomingThornsRodionFirst] 전부 소모
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [FestivalFeverRodion], [BloodDinner_Accumulation], [BloomingThornsRodionFirst], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FestivalFeverRodion] = 축제의 열기 / Festive Fever; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] To self and (highest Reson.) allies: apply 5 + (1 for every 50 [BloodDinner_Accumulation] by this unit) [FestivalFeverRodion] this turn and next turn (max 10)\n[WhenUse] To self and (highest Reson.) allies: apply 5 [BloomingThornsRodionFirst]\nDeal +1% damage for every 5 [BloodDinner_Accumulation] by this unit (max 50%)\n[EndSkill] Consume all [BloomingThornsRodionFirst] on self
   PL:
859. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 830 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
862. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
863. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
864. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 862 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Umiejętność 4 (×0) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신과 아군 (최대 공명 수)명에게 이번 턴과 다음 턴에 [FestivalFeverRodion] 5 + (자신의 [BloodDinner_Accumulation] 50 당 1) 부여 (최대 10)\n[WhenUse] 자신과 아군 (최대 공명 수)명에게 [BloomingThornsRodionFirst] 5 부여\n자신의 [BloodDinner_Accumulation] 5 당 피해량 1% 증가 (최대 50%)\n[EndSkill] 자신의 [BloomingThornsRodionFirst] 전부 소모
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=4].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [FestivalFeverRodion], [BloodDinner_Accumulation], [BloomingThornsRodionFirst], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [FestivalFeverRodion] = 축제의 열기 / Festive Fever; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>\n[WhenUse] To self and (highest Reson.) allies: apply 5 + (1 for every 50 [BloodDinner_Accumulation] by this unit) [FestivalFeverRodion] this turn and next turn (max 10)\n[WhenUse] To self and (highest Reson.) allies: apply 5 [BloomingThornsRodionFirst]\nDeal +1% damage for every 5 [BloodDinner_Accumulation] by this unit (max 50%)\n[EndSkill] Consume all [BloomingThornsRodionFirst] on self
   PL:
866. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 835 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
867. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 836 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
868. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 720 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]<style="highlight"></style>
   PL:
870. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 720 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091105].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 869 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
872. [Obrona (ulepszenia 1,4) — nazwa] 돈키호테류 경혈 15식 양산
   źródło: Skills_personality-09.json :: dataList[id=1091104].levelList[level=1].name ; dataList[id=1091104].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 60 znaków
   EN: Don Quixote Hardblood Arts 15: Parasol
   PL:
873. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 자신을 제외하고 ([Laceration] x [Laceration] 횟수) 값이 가장 높은 아군 2명의 [Laceration] 횟수를 3 감소시키고, (감소 전 [Laceration] x 감소시킨 [Laceration] 횟수) 만큼 [BloodDinner] 증가\n - 이 효과로 [Laceration] 횟수가 0이 되면 [Laceration] 소멸\n[WinDuel] [BloomingThornsRodionFirst] 4 얻음
   źródło: Skills_personality-09.json :: dataList[id=1091104].levelList[level=1].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Laceration], [BloodDinner], [WinDuel], [BloomingThornsRodionFirst]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [WinDuel] = [합 승리시] / [Clash Win]; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn
   EN: [DuelCounter]\n[WhenUse] Reduce [Laceration] Count by 3 for 2 other allies that have the highest ([Laceration] Potency x Count) value, and increase [BloodDinner] by (pre-reduction [Laceration] Potency x Count reduced)\n  - If this effect reduces [Laceration] Count to 0, [Laceration] expires\n[WinDuel] Gain 4 [BloomingThornsRodionFirst]
   PL:
874. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-09.json :: dataList[id=1091104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 862 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1091104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 831 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
876. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[WhenUse] 자신을 제외하고 ([Laceration] x [Laceration] 횟수) 값이 가장 높은 아군 2명의 [Laceration] 횟수를 3 감소시키고, (감소 전 [Laceration] x 감소시킨 [Laceration] 횟수) 만큼 [BloodDinner] 증가\n - 이 효과로 [Laceration] 횟수가 0이 되면 [Laceration] 소멸\n<style="highlight"> - 대상 아군이 <혈귀>면, [Laceration] 횟수 추가 2 감소</style>\n[WinDuel] [BloomingThornsRodionFirst] 4 얻음
   źródło: Skills_personality-09.json :: dataList[id=1091104].levelList[level=4].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [WhenUse], [Laceration], [BloodDinner], [WinDuel], [BloomingThornsRodionFirst]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [WinDuel] = [합 승리시] / [Clash Win]; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn
   EN: [DuelCounter]\n[WhenUse] Reduce [Laceration] Count by 3 for 2 other allies that have the highest ([Laceration] Potency x Count) value, and increase [BloodDinner] by (pre-reduction [Laceration] Potency x Count reduced)\n  - If this effect reduces [Laceration] Count to 0, [Laceration] expires\n<style="highlight">  - If the affected ally is a <Bloodfiend>, reduce their [Laceration] Count by 2 more</style>\n[WinDuel] Gain 4 [BloomingThornsRodionFirst]
   PL:
877. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091104].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 869 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
878. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091104].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 852 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Pasywka bojowa (od ulepszenia 1) — nazwa] 혈찬
   źródło: Passives.json :: dataList[id=1091102].name
   limit: do 40 znaków
   EN: Bloodfeast
   PL:
880. [Pasywka bojowa (od ulepszenia 1) — opis] 이 캐릭터가 전투에 등장해 있거나, 등장할 리스트에 포함되어 있으면, 1턴부터 모든 캐릭터가 받은 [Laceration] 피해만큼 [BloodDinner]이 증가함.\n이 캐릭터가 전투에 등장할 때 전장에 흩뿌려진 잠재된 피가 더욱 크게 드러난다.
   źródło: Passives.json :: dataList[id=1091102].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: If this unit is on field, or is one of the units that can appear on this Stage, increase [BloodDinner] value by the amount of [Laceration] damage collectively received by every unit. \nWhen this unit enters the field, the sleeping blood drenching the battlefield will fill the surface.
   PL:
881. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust, posiadane 2× Envy) — nazwa] 경혈의 가시
   źródło: Passives.json :: dataList[id=1091101].name
   limit: do 40 znaków
   EN: Hardblood Thorn
   PL:
882. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust, posiadane 2× Envy) — opis] 자신을 제외한 아군이 [Laceration] 피해를 받거나 [BloodDinner]을 소모할 때마다, 자신이 [BloomingThornsRodionFirst] 1 얻음 (턴 당 최대 3회)\n자신이 기본 스킬로 가한 피해량의 20%만큼 자신의 체력 회복 (스킬당 최대 10)
   źródło: Passives.json :: dataList[id=1091101].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner], [BloomingThornsRodionFirst]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn
   EN: When another ally takes [Laceration] damage or consumes [BloodDinner], gain 1 [BloomingThornsRodionFirst] (3 times per turn)\nHeal HP on self by 20% of the damage dealt with base Skills (max 10 per Skill)
   PL:
883. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust, posiadane 2× Envy) — nazwa] 경혈의 가시
   źródło: Passives.json :: dataList[id=1091111].name
   (powtórzenie elementu 881 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
884. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust, posiadane 2× Envy) — opis] 자신을 제외한 아군이 [Laceration] 피해를 받거나 [BloodDinner]을 소모할 때마다, 자신이 [BloomingThornsRodionFirst] 1 얻음 (턴 당 최대 5회)\n자신이 기본 스킬로 가한 피해량의 20%만큼 자신의 체력 회복 (스킬당 최대 10)\n- 자신이 최대 체력이면, 초과하는 회복량만큼 현재 체력 비율이 가장 낮은 아군 1명의 체력 회복
   źródło: Passives.json :: dataList[id=1091111].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner], [BloomingThornsRodionFirst]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn
   EN: When another ally takes [Laceration] damage or consumes [BloodDinner], this unit gains 1 [BloomingThornsRodionFirst] (5 times per turn)\nHeal HP on self by 20% of the damage dealt using base Skills (max 10 per Skill)\n- At max HP, heal 1 ally that has the lowest HP percentage by excess healing
   PL:
885. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Lust, posiadane 3× Envy) — nazwa] "피를 피워내.."
   źródło: Passives.json :: dataList[id=1091121].name
   limit: do 40 znaków
   EN: "Blossom with Blood..."
   PL:
886. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Lust, posiadane 3× Envy) — opis] 턴 종료시 [Laceration] 위력이 가장 높은 아군 1명의 [Laceration] 위력을 최대 6 감소시키고, (감소한 출혈 위력 / 2)만큼 [BloomingThornsRodionFirst] 부여 (소수점 버림)
   źródło: Passives.json :: dataList[id=1091121].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [Laceration], [BloomingThornsRodionFirst]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn
   EN: To 1 ally that has the highest [Laceration] Potency at Turn End: Reduce the ally's [Laceration] Potency by 6 max, and apply (Bleed Potency reduced / 2) [BloomingThornsRodionFirst] (rounded down)
   PL:
887. [Kwestia głosowa [get_10911_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=get_10911_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
888. [Kwestia głosowa [get_10911_1] (Identity Acquisition)] 라만차랜드의 카니발에 오신 걸 환영합니다. …끝없는 퍼레이드를, 함께 해주시겠나요?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=get_10911_1].dlg
   limit: do 130 znaków
   EN: Welcome to the grand Carnival of La Manchaland. ... Will you join us in this... eternal Parade?
   PL:
889. [Kwestia głosowa [lobby_morning_10911_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=lobby_morning_10911_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
890. [Kwestia głosowa [lobby_morning_10911_1] (Morning Greeting)] 음… 너무 이른 시간에 찾아오는 건 점잖지 못하네. 태양빛은 피부에 좋지 않아. 알잖아?\n…그 계획에 대한 건 조금 나중에 의논하도록 하자. 아침부터 어버이를 떠올리는 것도 힘에 부쳐.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=lobby_morning_10911_1].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Mm... it's a bit rude of you to visit me so early in the morning, isn't it? You know how bad sunlight is for the skin.\n... Let's talk about that plan a bit later. Thinking of Father this early in the morning is... stressful.
   PL:
891. [Kwestia głosowa [lobby_noon_10911_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=lobby_noon_10911_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
892. [Kwestia głosowa [lobby_noon_10911_1] (Afternoon Greeting)] 그래. 슬슬 퍼레이드 준비를 해야겠네. …아니, 나는 굶을게. 점심부터 혈액바를 집어먹으면… 아니, 혈액바로 연명을 해야 한다는게… 이젠 견딜 수 없어졌거든.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=lobby_noon_10911_1].dlg
   limit: do 300 znaków
   EN: Yeah, it's about time we got started on the Parade prep. ... No, I'll skip lunch. Another hemobar for lunch and I'll... ... I just can't handle it anymore. That we have to subsist on hemobars just to survive. It's... intolerably bad.
   PL:
893. [Kwestia głosowa [lobby_night_10911_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=lobby_night_10911_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
894. [Kwestia głosowa [lobby_night_10911_1] (Evening Greeting)] 이 밤의 열기 속에서 가장 빛나는 위치에 놓인다는 건… 당연하면서도 공허한 일이야. 실상은 나도 대열에 갇혀있을 뿐이니까.\n…하지만 그 커다란 죄를 짓고 나면, 이 끝없는 순환도 끝이 나겠지.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=lobby_night_10911_1].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The glory of taking center stage, of getting the limelight in the heat of this night is deservedly mine... for how hollow it is. Because I'm just another doll in the Parade.\nBut... once I commit that capital sin... this endless cycle will come to an end.
   PL:
895. [Kwestia głosowa [smalltalk_10911_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=smalltalk_10911_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
896. [Kwestia głosowa [smalltalk_10911_1] (Chatter #1)] …아, 미안. 너무 당연한 일이라 생각해본 적이 없네. 퍼레이드에 내가 포함되지 않는다는 상상이라니.\n…그분께서 무탈하게 투구만 찾아와주신다면, 끝날 수 있으려나.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=smalltalk_10911_1].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ... Oh, sorry. Just the thought of not being a part of the Parade anymore... that alone is too preposterous to even imagine. \nPerhaps it will all end should Father return safely with the helm.
   PL:
897. [Kwestia głosowa [smalltalk_10911_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=smalltalk_10911_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Kwestia głosowa [smalltalk_10911_2] (Chatter #2)] 혈귀가 되기 전… 글쎄, 기억이 잘 나진 않아. …이 아름다움을 영원히 가질 수 있다는 사실에 조금 기뻤을지도 모르겠네.\n그때는 아마 몰랐을 거야. 영원이라는 단어가 달콤함 외의 맛을 가질 줄은.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=smalltalk_10911_2].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Before I became a Bloodfiend...? Well, I don't quite recall what my life was like then. Maybe I was glad to know that my beauty was to be everlasting.\nI must not have known then, that eternity could be anything other than sweet.
   PL:
899. [Kwestia głosowa [smalltalk_10911_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=smalltalk_10911_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
900. [Kwestia głosowa [smalltalk_10911_3] (Chatter #3)] 두려운 건, 내가 가장 두려운 건… 피에 대한 욕망을 주체하지 못하고 추잡하게 전락하는 일이야.\n권속들이 모두 먹고 지내려면 혈액바가 있어야만 한다는 건 동의하지만, 애초에 어버이께서… 하아, 이 이야기는 그만하자.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=smalltalk_10911_3].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: My fear, my worst fear... is losing my elegance to that ghastly ugliness of bloodlust.\nI agree that hemobars were necessary to feed every Kindred, sure. But the core of this problem is, if only Father didn't— ... Haah, can we talk about something else?
   PL:
901. [Kwestia głosowa [smalltalk_10911_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=smalltalk_10911_4].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [Kwestia głosowa [smalltalk_10911_4] (Post-Uptie Chat 1)] 이 피보라를 봐, 아름답지 않니. 흩날리는 꽃종이도, 밤 하늘을 수놓는 폭죽도 이보다 황홀하진 못할 거야.\n…어버이를 슬프게 하긴 했지만, 결국 이걸로 우리 모두가 행복해졌어. 그렇지?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=smalltalk_10911_4].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Take in the raining blood. It's more ecstatically beautiful than colorful explosions of confetti or bright fireworks illuminating the clouds in the night sky.\n... We've saddened our Father, but... we're all happy now, aren't we?
   PL:
903. [Kwestia głosowa [smalltalk_10911_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=smalltalk_10911_5].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
904. [Kwestia głosowa [smalltalk_10911_5] (Post-Uptie Chat 2)] 신부는 고통을 인내하는 것이 미덕이라고 말하지만… 나의 미덕은 아름다움에 있으니까. 그리고 내 권속들도… 그들의 아이들도 항상 아름다웠으면 좋겠거든.\n그러니까… 이제 그만 하려고 해.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=smalltalk_10911_5].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Priest always lectures me that enduring the pain is a virtue, but... my virtue lies in beauty. Thus, I always wish nothing but beauty for my Kindreds... and their Children.\nSo... I'm going to stop, now.
   PL:
905. [Kwestia głosowa [neglect_10911_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=neglect_10911_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
906. [Kwestia głosowa [neglect_10911_1] (Idle)] 영원토록 이어지는…♬ 축복의 카니발…♬
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=neglect_10911_1].dlg
   limit: do 120 znaków
   EN: In this endlessly, this eternally...♬ ♬Blessed Carnival...♬
   PL:
907. [Kwestia głosowa [gacksung_10911_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=gacksung_10911_1].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Kwestia głosowa [gacksung_10911_1] (Uptying)] 오늘 밤의 퍼레이드는 조금 다를 거야… 진짜 카니발의 시작이니까.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=gacksung_10911_1].dlg
   limit: do 120 znaków
   EN: The Parade will be... different tonight. The real Carnival begins now.
   PL:
909. [Kwestia głosowa [formation_10911_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=formation_10911_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Kwestia głosowa [formation_10911_1] (Deployment)] …그러던가.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=formation_10911_1].dlg
   limit: do 120 znaków
   EN: ... Do as you will.
   PL:
911. [Kwestia głosowa [battleentry_10911_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battleentry_10911_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [Kwestia głosowa [battleentry_10911_1] (Stage Entry)] 피를 머금을 시간이네.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battleentry_10911_1].dlg
   limit: do 120 znaków
   EN: Time to draw blood.
   PL:
913. [Kwestia głosowa [battle_select_10911_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_select_10911_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
914. [Kwestia głosowa [battle_select_10911_1] (Viewed in Battle)] 퍼레이드 중에는 말 걸지 않는게 좋겠지?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_select_10911_1].dlg
   limit: do 120 znaków
   EN: Talking to me in the middle of a Parade isn't so polite, hm?
   PL:
915. [Kwestia głosowa [battle_endcommand_10911_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_endcommand_10911_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
916. [Kwestia głosowa [battle_endcommand_10911_1] (Commencing Attack)] 고귀하게.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_endcommand_10911_1].dlg
   limit: do 120 znaków
   EN: With grace.
   PL:
917. [Kwestia głosowa [battle_enemy_break_10911_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_enemy_break_10911_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
918. [Kwestia głosowa [battle_enemy_break_10911_1] (Enemy Stagger)] …추잡하네.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_enemy_break_10911_1].dlg
   limit: do 120 znaków
   EN: ... Hideous.
   PL:
919. [Kwestia głosowa [battle_break_10911_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_break_10911_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
920. [Kwestia głosowa [battle_break_10911_1] (Staggered)] 아… 하하.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_break_10911_1].dlg
   limit: do 120 znaków
   EN: Ah... ha ha.
   PL:
921. [Kwestia głosowa [battle_kill_10911_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_kill_10911_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [Kwestia głosowa [battle_kill_10911_1] (Enemy Killed)] 이쁘네, 네 피분수.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_kill_10911_1].dlg
   limit: do 120 znaków
   EN: Your fountain of blood... How pretty.
   PL:
923. [Kwestia głosowa [battle_dead_10911_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_dead_10911_1].desc
   (powtórzenie elementu 291 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
924. [Kwestia głosowa [battle_dead_10911_1] (Death)] 마침내… 끝나는 걸까…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_dead_10911_1].dlg
   limit: do 120 znaków
   EN: Can we... finally come to a stop...?
   PL:
925. [Kwestia głosowa [choice_success_p_10911_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=choice_success_p_10911_2].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [Kwestia głosowa [choice_success_p_10911_2] (Check Passed)] 이런 건 이발사나 신부에게 시켜.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=choice_success_p_10911_2].dlg
   limit: do 120 znaków
   EN: Go ask the Barber or the Priest for these menial chores.
   PL:
927. [Kwestia głosowa [choice_fail_n_10911_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=choice_fail_n_10911_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
928. [Kwestia głosowa [choice_fail_n_10911_1] (Check Failed)] …잠깐만. 한 번 더 해볼게.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=choice_fail_n_10911_1].dlg
   limit: do 120 znaków
   EN: ... Wait. Let me try that again.
   PL:
929. [Kwestia głosowa [battle_clear_10911_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_clear_10911_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
930. [Kwestia głosowa [battle_clear_10911_1] (Victory Cry)] 오늘도 끝났네. 내일도… 똑같겠지. 아무런 고조도, 하강도 없이 그저 끝없이 맴도는… 나날이겠지.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_clear_10911_1].dlg
   limit: do 150 znaków
   EN: Another day floats by. And tomorrow will, too. No ups or downs at all, just a flat circle, going round and round.
   PL:
931. [Kwestia głosowa [battle_clear_ex_10911_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_clear_ex_10911_1].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
932. [Kwestia głosowa [battle_clear_ex_10911_1] (Extra Conditions Fulfilled)] 피분수가 폭죽보다도 높이 솟아올랐어. 아아, 아냐. 이렇게 크게 웃으면 안돼. 아름다움을 잃지 않게, 그리고… 제2권속으로서의 품위도 잃지 않게 하자.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_clear_ex_10911_1].dlg
   limit: do 260 znaków
   EN: The fountain of blood burst high into the air, higher than the soaring fireworks. Ahh, no. I shouldn't guffaw so ungracefully. I must remain beautiful... and maintain my dignity as a Second Kindred.
   PL:
933. [Kwestia głosowa [battle_defeat_10911_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_defeat_10911_1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
934. [Kwestia głosowa [battle_defeat_10911_1] (Defeat Wail)] …어쩌면 잘 된 일일지도 모르겠어. 가끔은 누군가 퍼레이드를 끝내줬으면 했으니까. 잠시… 쉬어볼까.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Bloodfiend_10911.json :: dataList[id=battle_defeat_10911_1].dlg
   limit: do 190 znaków
   EN: ... Maybe this is a blessing in disguise. I often wondered if anyone would come along to put an end to the Parade. I suppose... I'll rest a little.
   PL:

## [000] Heishou Pack - Si Branch — Rodion — 흑수 - 사
- ID Tożsamości: `10912` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 69 · szybkość: 2–5 / 2–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture, Poise

935. [Karta Tożsamości — tytuł] 흑수 - 사
   źródło: Personalities.json :: dataList[id=10912].title
   limit: do 40 znaków
   EN: Heishou Pack - Si Branch
   PL:
936. [Karta Tożsamości — nazwa] 로쟈
   źródło: Personalities.json :: dataList[id=10912].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
937. [Karta Tożsamości — nazwa z tytułem] 로쟈
   źródło: Personalities.json :: dataList[id=10912].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
938. [Karta Tożsamości — opis] 로쟈의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10912].desc
   limit: do 120 znaków
   EN: Rodion's 12th Identity
   PL:
939. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 사섬
   źródło: Skills_personality-09.json :: dataList[id=1091201].levelList[level=1].name ; dataList[id=1091201].levelList[level=2].name ; dataList[id=1091201].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Serpent Glint
   PL:
940. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1091201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +1 [Breath] Count
   PL:
941. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1091201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 823 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
942. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-09.json :: dataList[id=1091201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 823 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
943. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합이 10 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-09.json :: dataList[id=1091201].levelList[level=2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: <style="highlight">[WhenUse] At 10+ ([Breath] on self + [Burst] on target), Coin Power +1</style>\n[WhenUse] Gain +<style="highlight">2</style> [Breath] Count
   PL:
944. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1091201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 826 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1091201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 826 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
946. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] 자신에게 [SnakeStance]이 있으면, [Burst] 1 부여</style>
   źródło: Skills_personality-09.json :: dataList[id=1091201].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [SnakeStance], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [SnakeStance] = 사완 / Serpent Arm; [Burst] = 파열 / Rupture
   EN: <style="highlight">[CriticalOnSucceedAttack] If this unit has [SnakeStance], inflict 1 [Burst]</style>
   PL:
947. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 10 당 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-09.json :: dataList[id=1091201].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: <style="highlight">[WhenUse] Coin Power +1 for every 10 ([Breath] on self + [Burst] on target) (max 2)</style>\n[WhenUse] Gain +2 [Breath] Count
   PL:
948. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 자신에게 [SnakeStance]이 있으면, [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-09.json :: dataList[id=1091201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [SnakeStance], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [SnakeStance] = 사완 / Serpent Arm; [Burst] = 파열 / Rupture
   EN: [CriticalOnSucceedAttack] If this unit has [SnakeStance], inflict <style="highlight">2</style> [Burst]
   PL:
949. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 뱀 송곳니
   źródło: Skills_personality-09.json :: dataList[id=1091202].levelList[level=1].name ; dataList[id=1091202].levelList[level=2].name ; dataList[id=1091202].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Snake Fang
   PL:
950. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] [Burst] 횟수 2 증가\n[WinDuel] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1091202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Burst], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [WinDuel] Inflict +2 [Burst] Count\n[WinDuel] Gain +1 [Breath] Count
   PL:
951. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1091202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 830 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
952. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [BurstPoison] 부여
   źródło: Skills_personality-09.json :: dataList[id=1091202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstPoison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [OnSucceedAttack] Inflict [BurstPoison]
   PL:
953. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합이 10 이상이면, 코인 위력 +1</style>\n[WinDuel] [Burst] 횟수 2 증가\n[WinDuel] 자신의 [Breath] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-09.json :: dataList[id=1091202].levelList[level=2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">[WhenUse] At 10+ ([Breath] on self + [Burst] on target), Coin Power +1</style>\n[WinDuel] Inflict +2 [Burst] Count\n[WinDuel] Gain +<style="highlight">2</style> [Breath] Count
   PL:
954. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1091202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
955. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Breath]이 30 이상이면, [Breath] 10 소모하여 코인 1회 재사용 (최대 1회)</style>
   źródło: Skills_personality-09.json :: dataList[id=1091202].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: <style="highlight">[OnSucceedAttack] At 30+ [Breath], consume 10 [Breath] on self to Reuse Coin once (1 time max)</style>
   PL:
956. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [BurstPoison] 부여<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091202].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1091202].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BurstPoison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [OnSucceedAttack] Inflict [BurstPoison]<style="highlight"></style>
   PL:
957. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력의 합 10 당 코인 위력 +1 (최대 2)</style>\n[WinDuel] [Burst] 횟수 2 증가\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-09.json :: dataList[id=1091202].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">[WhenUse] Coin Power +1 for every 10 ([Breath] on self + [Burst] on target) (max 2)</style>\n[WinDuel] Inflict +2 [Burst] Count\n[WinDuel] Gain +2 [Breath] Count
   PL:
958. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Burst] 1 부여</style>
   źródło: Skills_personality-09.json :: dataList[id=1091202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Burst]</style>
   PL:
959. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Breath]이 30 이상이면, [Breath] 10 소모하여 코인 1회 재사용 (최대 1회)<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] At 30+ [Breath], consume 10 [Breath] on self to Reuse Coin once (1 time max)<style="highlight"></style>
   PL:
960. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] <style="highlight">[CriticalOnSucceedAttack] [SnakeStance] 1 얻음</style>
   źródło: Skills_personality-09.json :: dataList[id=1091202].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [SnakeStance]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [SnakeStance] = 사완 / Serpent Arm
   EN: <style="highlight">[CriticalOnSucceedAttack] Gain 1 [SnakeStance]</style>
   PL:
961. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 절명사난
   źródło: Skills_personality-09.json :: dataList[id=1091203].levelList[level=3].name ; dataList[id=1091203].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Serpent's Mortal Flurry
   PL:
962. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WideAreaRampage]\n[WhenUse] 자신의 [Breath] 위력과 메인 공격 대상의 [Burst] 위력의 합이 10 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [SnakeStance]만큼 합 위력이 증가\n[WhenUse] [SnakeStance] 3 얻음\n[WinDuel] 모든 대상의 [Burst] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1091203].levelList[level=3].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [WhenUse], [Breath], [Burst], [SnakeStance], [WinDuel]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [SnakeStance] = 사완 / Serpent Arm; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WideAreaRampage]\n[WhenUse] At 10+ ([Breath] on self + [Burst] on the main target), Coin Power +1\n[WhenUse] Gain Clash Power equal to [SnakeStance] on self\n[WhenUse] Gain 3 [SnakeStance]\n[WinDuel] Inflict +1 [Burst] Count against all targets
   PL:
963. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 횟수 2 증가
   źródło: Skills_personality-09.json :: dataList[id=1091203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL:
964. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-09.json :: dataList[id=1091203].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
965. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1091203].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 830 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
966. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] 대상의 [BurstPoison] 1 감소
   źródło: Skills_personality-09.json :: dataList[id=1091203].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [BurstPoison]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [CriticalOnSucceedAttack] Reduce [BurstPoison] on target by 1
   PL:
967. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] 이 코인 1회 재사용 (스킬당 2회)
   źródło: Skills_personality-09.json :: dataList[id=1091203].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Reuse this Coin once (2 times per Skill)
   PL:
968. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WideAreaRampage]\n<style="highlight">[WhenUse] 자신의 [Breath] 위력과 메인 공격 대상의 [Burst] 위력의 합 10 당 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [SnakeStance]만큼 합 위력이 증가\n[WhenUse] [SnakeStance] 3 얻음\n[WinDuel] 모든 대상의 [Burst] 횟수 1 증가
   źródło: Skills_personality-09.json :: dataList[id=1091203].levelList[level=4].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WideAreaRampage], [WhenUse], [Breath], [Burst], [SnakeStance], [WinDuel]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [SnakeStance] = 사완 / Serpent Arm; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WideAreaRampage]\n<style="highlight">[WhenUse] Coin Power +1 for every 10 ([Breath] on self + [Burst] on the main target) (max 2)</style>\n[WhenUse] Gain Clash Power equal to [SnakeStance] on self\n[WhenUse] Gain 3 [SnakeStance]\n[WinDuel] Inflict +1 [Burst] Count on all targets
   PL:
969. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count<style="highlight"></style>
   PL:
970. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]<style="highlight"></style>
   PL:
971. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
972. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] 대상의 [BurstPoison] 1 감소<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [BurstPoison]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: [CriticalOnSucceedAttack] Reduce [BurstPoison] on target by 1<style="highlight"></style>
   PL:
973. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] 이 코인 1회 재사용 (스킬당 2회)<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091203].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Reuse this Coin once (2 times per Skill)<style="highlight"></style>
   PL:
974. [Obrona (ulepszenia 1,4) — nazwa] 반축
   źródło: Skills_personality-09.json :: dataList[id=1091204].levelList[level=1].name ; dataList[id=1091204].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 3 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Reversal Kick
   PL:
975. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] 다음 턴에 [SnakeStance] 3 얻음
   źródło: Skills_personality-09.json :: dataList[id=1091204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [SnakeStance]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [SnakeStance] = 사완 / Serpent Arm
   EN: [CanDuelGuard] \n[StartBattle] Gain 3 [SnakeStance] next turn
   PL:
976. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-09.json :: dataList[id=1091204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
977. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[StartBattle] 다음 턴에 [SnakeStance] 3 얻음\n<style="highlight">[WhenUse] 자신의 [Breath]이 10 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-09.json :: dataList[id=1091204].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [StartBattle], [SnakeStance], [WhenUse], [Breath]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [SnakeStance] = 사완 / Serpent Arm; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [CanDuelGuard]\n[StartBattle] Gain 3 [SnakeStance] next turn\n<style="highlight">[WhenUse] At 10+ [Breath] Count, Coin Power +1</style>
   PL:
978. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-09.json :: dataList[id=1091204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL:
979. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — nazwa] 흑수화[사]
   źródło: Passives.json :: dataList[id=1091201].name
   limit: do 40 znaków
   EN: Heishou Mutation [Si]
   PL:
980. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — opis] 자신에게 [SnakeStance]이 있으면, 가하는 피해량 +5%\n대상에게 [BurstPoison]이 있으면, 가하는 피해량 +5%
   źródło: Passives.json :: dataList[id=1091201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [SnakeStance], [BurstPoison]
   znaczenie tagów: [SnakeStance] = 사완 / Serpent Arm; [BurstPoison] = 주살【독】 / Deathrite【Venom】
   EN: If this unit has [SnakeStance], deal +5% damage\nIf target has [BurstPoison], deal +5% damage
   PL:
981. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 피에 흐르는 독
   źródło: Passives.json :: dataList[id=1091221].name
   limit: do 40 znaków
   EN: Intravascular Venom
   PL:
982. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 속도가 가장 빠른 아군 1명이 적에게 [Burst] 피해를 입히면, 다음 턴에 [AttackDown] 1, [DefenseDown] 1 부여 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1091221].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Burst], [AttackDown], [DefenseDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When 1 ally with the fastest Speed inflicts [Burst] damage to an enemy, inflict 1 [AttackDown] and 1 [DefenseDown] next turn (once per turn)
   PL:
983. [Kwestia głosowa [get_10912_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=get_10912_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
984. [Kwestia głosowa [get_10912_1] (Identity Acquisition)] 시키는 임무도 다 했어… 충의를 다 했는데… 어째서… 내가 아니야?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=get_10912_1].dlg
   limit: do 120 znaków
   EN: I did everything as I was told... I was fiercely loyal... so... why wasn't it me?
   PL:
985. [Kwestia głosowa [lobby_morning_10912_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=lobby_morning_10912_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
986. [Kwestia głosowa [lobby_morning_10912_1] (Morning Greeting)] 날이 밝았으니 주군에게 보고하러 가야 해. 후훗, 이번에도 잔뜩 칭찬받겠는걸?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=lobby_morning_10912_1].dlg
   limit: do 120 znaków
   EN: Sun's up, gotta keep m'lord updated. Fuhu, he's gonna love me for it.
   PL:
987. [Kwestia głosowa [lobby_noon_10912_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=lobby_noon_10912_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
988. [Kwestia głosowa [lobby_noon_10912_1] (Afternoon Greeting)] 사환을 먹은 뒤론 뭘 먹어도 밍밍해서 영… 그래도 식감이 좋은 음식을 먹는 건 여전히 즐거운 것 같아.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=lobby_noon_10912_1].dlg
   limit: do 140 znaków
   EN: Once I took the Si Bolus, I lost most of my sense of taste... but hey, I can still enjoy the texture.
   PL:
989. [Kwestia głosowa [lobby_night_10912_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=lobby_night_10912_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
990. [Kwestia głosowa [lobby_night_10912_1] (Evening Greeting)] 나는 밤이 좋더라. 이것저것 임무도 많고, 어쩌다 적의 습격이라도 막아내면… 높으신 분의 눈에 들기 이만한 상황이 없거든~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=lobby_night_10912_1].dlg
   limit: do 310 znaków
   EN: I like nights. I get tons 'o missions, and there's always a chance an assassin for me to dramatically defeat might sneak in... If I defeat 'em right as the big shots' eyes are on me... Heh, no better way to make a name for myself, right~?
   PL:
991. [Kwestia głosowa [smalltalk_10912_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=smalltalk_10912_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
992. [Kwestia głosowa [smalltalk_10912_1] (Chatter #1)] 그거 알아? 흑수의 소유권이 많이 남아있을 때 포기하거나 그에 준하는 대가를 치르면… 그 흑수의 일원 중 한명을 흑수에서 해방시켜 줄 수 있어. 이 몰개성한 검은 짐승에서 벗어날 수 있는 거야…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=smalltalk_10912_1].dlg
   limit: do 370 znaków
   EN: Ya know something? If these lords have surplus claims to the Heishou, they can either give them up or pay up an equivalent value for a single beast... to release a member of the Pack. It means there’s a chance that I don't have to be this kind of featureless silhouette of an animal anymore.
   PL:
993. [Kwestia głosowa [smalltalk_10912_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=smalltalk_10912_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
994. [Kwestia głosowa [smalltalk_10912_2] (Chatter #2)] 흑수는 사람이 아니라, 주군에게 충성한다. 질리도록 들은 말이지. 그런데… 허물을 벗고, 더 빛나려면… 사람에게 충성해야 해. 그래야만 나를 눈여겨 보고 꺼내줄 테니까.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=smalltalk_10912_2].dlg
   limit: do 370 znaków
   EN: A Heishou's loyalty is to the title of the lord, not to the one who wears it. Heard that more times than I can count. But... how could I hope to free myself from this slough and really shine without showing some loyalty to the person who holds my leash? I need 'em to help me molt, after all.
   PL:
995. [Kwestia głosowa [smalltalk_10912_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=smalltalk_10912_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
996. [Kwestia głosowa [smalltalk_10912_3] (Chatter #3)] 징그럽고 흉측하지 않아? 시간이 지나면 지금보다 더 심하게 변할 거야. 점점 다른 뱀들처럼, 흑수들처럼 모든 것에 무감각해지겠지.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=smalltalk_10912_3].dlg
   limit: do 230 znaków
   EN: It's disgusting and ugly, isn't it? It gets worse with time. I'm going to be like the other snakes, like the other beasts of the Heishou Pack... becoming numb to everything.
   PL:
997. [Kwestia głosowa [smalltalk_10912_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=smalltalk_10912_4].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
998. [Kwestia głosowa [smalltalk_10912_4] (Post-Uptie Chat 1)] 괘, 괜찮아. 밤에 곰곰이 생각해 봤는데, 흑수로 남아있는 게 낫겠더라구. 괜히 뽑혀서 나가봤자 암투에나 휘말려서 요절할 거라니까?\n그리고 저번 주군은 영 아니었잖아. 모시기에는… 내가 아까웠지.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=smalltalk_10912_4].dlg
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I-I'm okay. I gave it some thought last night, and... I think it's better to stay leashed as a Heishou. I mean, even if I were to be freed, what other prospects do I have? Get killed after getting dragged into some random, unrelated conspiracy?\nBesides, our last lord wasn't all that, was he? I'm... too good for him.
   PL:
999. [Kwestia głosowa [smalltalk_10912_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=smalltalk_10912_5].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1000. [Kwestia głosowa [smalltalk_10912_5] (Post-Uptie Chat 2)] 가주 후보자들은 자기들이 제일 불행하다고 생각하나 봐. 귀한 집에서 태어나서, 비단옷을 입고, 먹고 싶은 걸 실컷 먹으면서 뭐가 그렇게 불행할까.\n매일매일 목숨을 위협 받는 건 넝마를 입고 배를 곯는 뒷골목 사람들도 똑같잖아.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=smalltalk_10912_5].dlg
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Family Hierarch candidates are a bunch of drama queens who act like they got dealt the worst possible hand in life. I mean, those rich kids have everything—silken clothes, good food... what more could they want?\nBackstreets people got dealt the same shitty hand. All the downsides of living here where life is precarious... except, instead of luxuries, they get tattered rags and starving stomachs.
   PL:
1001. [Kwestia głosowa [neglect_10912_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=neglect_10912_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1002. [Kwestia głosowa [neglect_10912_1] (Idle)] 이걸로 팔십… 조금만 더 채우면 짐승으로 사는 것도 끝일 거야.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=neglect_10912_1].dlg
   limit: do 130 znaków
   EN: That makes it eighty missions... Just a few more, and I won't have to live like some animal anymore.
   PL:
1003. [Kwestia głosowa [gacksung_10912_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=gacksung_10912_1].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1004. [Kwestia głosowa [gacksung_10912_1] (Uptying)] 보였어? 안 보였을 텐데… 휘어진 뱀은 소리보다 빠르거든.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=gacksung_10912_1].dlg
   limit: do 130 znaków
   EN: Didya see that? Doubt ya did... A crooked snake whips faster than the speed of sound, you know.
   PL:
1005. [Kwestia głosowa [formation_10912_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=formation_10912_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1006. [Kwestia głosowa [formation_10912_1] (Deployment)] 잠깐! 이번 임무는 내가 나갈게. 괜찮지?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=formation_10912_1].dlg
   limit: do 120 znaków
   EN: Wait! I'll take this mission. Is that okay with ya?
   PL:
1007. [Kwestia głosowa [battleentry_10912_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battleentry_10912_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1008. [Kwestia głosowa [battleentry_10912_1] (Stage Entry)] 이런 임무는 뱀 중에서도 내가 제일이지~
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battleentry_10912_1].dlg
   limit: do 120 znaków
   EN: You won't find a better snake for this job~
   PL:
1009. [Kwestia głosowa [battle_select_10912_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_select_10912_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1010. [Kwestia głosowa [battle_select_10912_1] (Viewed in Battle)] 불렀어, 주군? 필요한 일 있으면 언제든지 말해.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_select_10912_1].dlg
   limit: do 120 znaków
   EN: Didya call, m'lord? Feel free to summon me for anything ya need.
   PL:
1011. [Kwestia głosowa [battle_endcommand_10912_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_endcommand_10912_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1012. [Kwestia głosowa [battle_endcommand_10912_1] (Commencing Attack)] 목을 콱 물어버리자구.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_endcommand_10912_1].dlg
   limit: do 120 znaków
   EN: Let's sink our fangs into that thing.
   PL:
1013. [Kwestia głosowa [battle_enemy_break_10912_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_enemy_break_10912_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1014. [Kwestia głosowa [battle_enemy_break_10912_1] (Enemy Stagger)] 어머, 놀랐어?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_enemy_break_10912_1].dlg
   limit: do 120 znaków
   EN: My, did I catch ya off guard?
   PL:
1015. [Kwestia głosowa [battle_break_10912_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_break_10912_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1016. [Kwestia głosowa [battle_break_10912_1] (Staggered)] 윽…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_break_10912_1].dlg
   (powtórzenie elementu 799 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1017. [Kwestia głosowa [battle_kill_10912_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_kill_10912_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1018. [Kwestia głosowa [battle_kill_10912_1] (Enemy Killed)] 빈틈투성이네.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_kill_10912_1].dlg
   limit: do 120 znaków
   EN: So sloppy.
   PL:
1019. [Kwestia głosowa [battle_dead_10912_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_dead_10912_1].desc
   (powtórzenie elementu 291 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1020. [Kwestia głosowa [battle_dead_10912_1] (Death)] 나는… 뭘 위해… 지금까지, 주군을…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_dead_10912_1].dlg
   limit: do 120 znaków
   EN: What... was the point...? All that time... I wasted... for the lord...
   PL:
1021. [Kwestia głosowa [choice_success_p_10912_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=choice_success_p_10912_2].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1022. [Kwestia głosowa [choice_success_p_10912_2] (Check Passed)] 봤어? 이런 건 다른 뱀들보다 내가 더 잘한다구.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=choice_success_p_10912_2].dlg
   limit: do 120 znaków
   EN: See? I'm better at this than the other snakes.
   PL:
1023. [Kwestia głosowa [choice_fail_n_10912_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=choice_fail_n_10912_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1024. [Kwestia głosowa [choice_fail_n_10912_1] (Check Failed)] 이건… 사소한 실수야. 다음에는 꼭 성공할게.
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=choice_fail_n_10912_1].dlg
   limit: do 120 znaków
   EN: This... this was just a slip-up, 'kay? I'll do it right next time.
   PL:
1025. [Kwestia głosowa [battle_clear_10912_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_clear_10912_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1026. [Kwestia głosowa [battle_clear_10912_1] (Victory Cry)] 좋아. 이걸로 성공한 임무만 아흔 번이 넘었어. 따로 하는 부탁도 다 들어줬고… 이만하면 주군도 나를 중요한 심복으로 생각하지 않을까?
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_clear_10912_1].dlg
   limit: do 190 znaków
   EN: Great, that's ninety successful missions, fulfilled all their extra requests, too... Maybe my lord'll finally consider me to be his number one gal?
   PL:
1027. [Kwestia głosowa [battle_clear_ex_10912_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_clear_ex_10912_1].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1028. [Kwestia głosowa [battle_clear_ex_10912_1] (Extra Conditions Fulfilled)] 저번에 약속한 거 안 잊었지, 주군? 그 왜~ 임무를 성공적으로 백 번만 수행하면…\n주군? 설마 소유권을 벌써 다 쓴 거야…? 말도 안 돼… 이건 약속이랑 다르잖아!
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_clear_ex_10912_1].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Remember the promise ya made, m'lord? Ya know~ ya told me to complete a hundred missions, and you'd...\nLord? Don't tell me you already used up all of your claims...? A-are you kidding me...? This isn't what you promised!
   PL:
1029. [Kwestia głosowa [battle_defeat_10912_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_defeat_10912_1].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1030. [Kwestia głosowa [battle_defeat_10912_1] (Defeat Wail)] …이번 주군도 글러 먹었네. 그래. 처음부터 싹이 별로긴 했지. 다음 주군에게 잘하면 돼. 그러다 보면 언젠간…
   źródło: PersonalityVoiceDlg/Voice_Rodion_Blackwater_10912.json :: dataList[id=battle_defeat_10912_1].dlg
   limit: do 230 znaków
   EN: ... Looks like this lord's don't got much time left, either. Well, I never expected much from him anyway. I just have to butter up our next lord. And... and one day, I'll...
   PL:
