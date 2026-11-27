# Grzesznik #06: Hong Lu — Tożsamości, umiejętności, pasywki i głos (część a) — Limbus Company

Kompletny zestaw kart Tożsamości postaci **Hong Lu** (홍루) wraz z umiejętnościami na ulepszeniach 1–4, efektami monet, pasywkami i kwestiami głosowymi.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Grzesznik #06: Hong Lu (홍루)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 홍루
   źródło: Characters.json :: dataList[id=6].name
   limit: do 40 znaków
   EN: Hong Lu
   PL:
2. [Akta więźnia — nazwa] 홍루
   źródło: IntroduceCharacter.json :: dataList[id=홍루].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
3. [Akta więźnia — opis] 우리 회사의 자산이 되기 전까지 부족함 없이 살아왔던 수감자입니다.\n그러므로 자유로움을 추구하려고 하지만 간혹, 타 수감자가\n제조한 음식을 보고 하위 저급문화에 대한 무지함을 드러냄과\n모멸적인 질문을 하는 등 다른 수감자들의 속을 뒤집어지게 만드는 상황이\n있을 수 있습니다. 하지만 비꼬는 것이 아닌 순수한 호기심에 불과하므로\n서로 날붙이를 꺼내 들게 하는 건 썩 좋은 방법이 아닙니다.
   źródło: IntroduceCharacter.json :: dataList[id=홍루].description
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A Sinner who had lived an affluent life before becoming our company's asset.\nAs such, he has a certain admiration for a free life;\nbut occasionally, he may make ignorant and unsavory questions in regards\nto the food cooked by a certain other Sinner or other aspects of the low-lives' lowly culture.\nThis can cause significant irritation for the other Sinners.\nHowever, it is important to note that no sarcastic undertones are contained in his curiosity-driven inquiries,\nso it is ill-advised to let them get physical over it.
   PL: Grzesznik, który do chwili, gdy stał się aktywem naszej firmy, nie zaznał niedostatku.\nDlatego ceni sobie swobodę, ale czasem, widząc potrawę przyrządzoną\nprzez innego Grzesznika, zdradza nieznajomość “niższej” kultury i zadaje\nuwłaczające pytania, co może wywracać innym Grzesznikom wnętrzności.\nNie kryje się w tym jednak drwina, a jedynie szczera ciekawość,\nnie warto więc dopuszczać do tego, by sięgali po ostrza.

## [0] LCB Sinner — Hong Lu — LCB 수감자
- ID Tożsamości: `10601` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 66 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Sinking, Rupture

4. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10601].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL:
5. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10601].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10601].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Karta Tożsamości — opis] 홍루의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10601].desc
   limit: do 120 znaków
   EN: Hong Lu’s 1st Identity
   PL:
8. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 내려베기
   źródło: Skills.json :: dataList[id=1060101].levelList[level=1].name ; dataList[id=1060101].levelList[level=2].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Downward Cleave
   PL:
9. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1060101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 2 [Sinking]
   PL:
10. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1060101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL:
11. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 이연격
   źródło: Skills.json :: dataList[id=1060102].levelList[level=1].name ; dataList[id=1060102].levelList[level=2].name ; dataList[id=1060102].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Dual Strike
   PL:
12. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1060102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 1 [Sinking]
   PL:
13. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1060102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL:
14. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] 이전 턴에 피해를 받지 않은 경우 코인 위력 +1
   źródło: Skills.json :: dataList[id=1060102].levelList[level=2].desc ; dataList[id=1060102].levelList[level=4].desc
   limit: do 120 znaków
   EN: If user took no damage last turn, Coin Power +1
   PL:
15. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1060102].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL:
16. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1060102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL:
17. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1060102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 선풍
   źródło: Skills.json :: dataList[id=1060103].levelList[level=3].name ; dataList[id=1060103].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 6 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Whirlwind
   PL:
19. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] 이전 턴에 피해를 받지 않은 경우 코인 위력 +2
   źródło: Skills.json :: dataList[id=1060103].levelList[level=3].desc ; dataList[id=1060103].levelList[level=4].desc
   limit: do 120 znaków
   EN: If user took no damage last turn, Coin Power +2
   PL:
20. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 공격 위력 감소 2 부여
   źródło: Skills.json :: dataList[id=1060103].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1060103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Attack Power Down
   PL:
21. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1060103].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
22. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1060103].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
23. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1060104].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: unik · moc bazowa: 2 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL:
24. [Pasywka bojowa (od ulepszenia 1, rezonans 2× Sloth) — nazwa] 유희
   źródło: Passives.json :: dataList[id=1060101].name
   limit: do 40 znaków
   EN: Entertainment
   PL:
25. [Pasywka bojowa (od ulepszenia 1, rezonans 2× Sloth) — opis] 다음 턴 시작 시 정신력 6 회복
   źródło: Passives.json :: dataList[id=1060101].desc
   limit: do 120 znaków
   EN: Heal 6 SP next turn.
   PL:
26. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Sloth) — nazwa] 실없는 농담
   źródło: Passives.json :: dataList[id=1060121].name
   limit: do 40 znaków
   EN: Frivolous Jokes
   PL:
27. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Sloth) — opis] 정신력이 가장 낮은 아군 1명 전투 시작 시 정신력 6 회복
   źródło: Passives.json :: dataList[id=1060121].desc
   limit: do 120 znaków
   EN: At the start of the combat phase, the ally with the least SP heals 6 SP.
   PL:
28. [Kwestia głosowa [get_10601_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=get_10601_1].desc
   limit: do 120 znaków
   EN: Identity Acquisition
   PL:
29. [Kwestia głosowa [get_10601_1] (Identity Acquisition)] 홍루라고 한답니다. 잘 해보자구요, 우리.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=get_10601_1].dlg
   limit: do 120 znaków
   EN: My name’s Hong Lu. I hope we can get along well.
   PL:
30. [Kwestia głosowa [lobby_morning_10601_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=lobby_morning_10601_1].desc
   limit: do 120 znaków
   EN: Morning Greeting
   PL:
31. [Kwestia głosowa [lobby_morning_10601_1] (Morning Greeting)] 좋은 아침이에요, 단테 님! 저희 주방장님이 그랬는데 아침에 피곤할 때는 송로버섯만큼 좋은 게 없다고 그러더라고요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=lobby_morning_10601_1].dlg
   limit: do 150 znaków
   EN: Good morning, Dante! My resident chef once taught me that truffles are wonderful for relieving morning fatigue~
   PL:
32. [Kwestia głosowa [lobby_noon_10601_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=lobby_noon_10601_1].desc
   limit: do 120 znaków
   EN: Afternoon Greeting
   PL:
33. [Kwestia głosowa [lobby_noon_10601_1] (Afternoon Greeting)] 이곳에 와서 흥미로웠던 점 중 하나는, 배고프다는 느낌을 처음 알 수 있었다는 거예요. 생소한 기분이더라고요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=lobby_noon_10601_1].dlg
   limit: do 160 znaków
   EN: An interesting thing I noted here was that I was able to learn how it feels to be hungry. What a curious sensation it is!
   PL:
34. [Kwestia głosowa [lobby_night_10601_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=lobby_night_10601_1].desc
   limit: do 120 znaków
   EN: Evening Greeting
   PL:
35. [Kwestia głosowa [lobby_night_10601_1] (Evening Greeting)] 저녁은 저녁만큼의 운치가 있어요. 비록 여기서 제 방만큼 풍경은 잘 안 보이지만… 단테 님이랑 같이 있어서 좋네요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=lobby_night_10601_1].dlg
   limit: do 170 znaków
   EN: The evening has its own beauty. Although the view isn’t as clear as my room’s window… it’s still nice that you’re here with me.
   PL:
36. [Kwestia głosowa [smalltalk_10601_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=smalltalk_10601_1].desc
   limit: do 120 znaków
   EN: Chatter #1
   PL:
37. [Kwestia głosowa [smalltalk_10601_1] (Chatter #1)] 나중에 집에 돌아가게 된다면, 단테 님을 초대해서 근사한 연회라도 열고 싶어요. 아버지께 새로 사귄 친구들도 소개시켜주고… 재미있을 것 같아요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=smalltalk_10601_1].dlg
   limit: do 190 znaków
   EN: When I go back home later, Dante, I’d love to invite you to a fabulous gala. I’ll introduce my new friends to Father, too… It’ll be such a fun time.
   PL:
38. [Kwestia głosowa [smalltalk_10601_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=smalltalk_10601_2].desc
   limit: do 120 znaków
   EN: Chatter #2
   PL:
39. [Kwestia głosowa [smalltalk_10601_2] (Chatter #2)] 마음이 어지러울 땐 간단해요, 그냥 안되면 어쩔 수 없지 뭐, 하는 생각이면 세상 어려울 게 없답니다.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=smalltalk_10601_2].dlg
   limit: do 180 znaków
   EN: When you’re distraught, simply remember that life goes on even if what you’re doing now doesn’t work out. Then, you’ll be free of worries.
   PL:
40. [Kwestia głosowa [smalltalk_10601_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=smalltalk_10601_3].desc
   limit: do 120 znaków
   EN: Chatter #3
   PL:
41. [Kwestia głosowa [smalltalk_10601_3] (Chatter #3)] 가족들이란… 서로를 지켜주는 안식처 같은 존재라면서요? 전 지금까지 뒤통수에 칼을 꽂아 넣는 게 당연한 관계인 줄 알았지 뭐예요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=smalltalk_10601_3].dlg
   limit: do 250 znaków
   EN: Family… I heard that family is like a sanctuary offering each other shelter, right? I thought it was more like a cohort of kin looking to stab each other in the back at every turn all my life~
   PL:
42. [Kwestia głosowa [neglect_10601_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=neglect_10601_1].desc
   limit: do 120 znaków
   EN: Idle
   PL:
43. [Kwestia głosowa [neglect_10601_1] (Idle)] 어라, 단테 님? 급한 일이 생기셨나 봐요? 천천히 갔다 오세요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=neglect_10601_1].dlg
   limit: do 120 znaków
   EN: Oh? Has an urgent matter arisen, Dante? Take your time~
   PL:
44. [Kwestia głosowa [formation_10601_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=formation_10601_1].desc
   limit: do 120 znaków
   EN: Deployment
   PL:
45. [Kwestia głosowa [formation_10601_1] (Deployment)] 우와, 기대되네요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=formation_10601_1].dlg
   limit: do 120 znaków
   EN: Golly, I can’t wait~
   PL:
46. [Kwestia głosowa [battleentry_10601_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battleentry_10601_1].desc
   limit: do 120 znaków
   EN: Stage Entry
   PL:
47. [Kwestia głosowa [battleentry_10601_1] (Stage Entry)] 흥미로운 일이 벌어지면 좋겠어요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battleentry_10601_1].dlg
   limit: do 120 znaków
   EN: I hope something fun happens~
   PL:
48. [Kwestia głosowa [battle_select_10601_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_select_10601_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle
   PL:
49. [Kwestia głosowa [battle_select_10601_1] (Viewed in Battle)] 어쩐 일이세요? 단테 님?
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_select_10601_1].dlg
   limit: do 120 znaków
   EN: What is it, Dante?
   PL:
50. [Kwestia głosowa [battle_endcommand_10601_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_endcommand_10601_1].desc
   limit: do 120 znaków
   EN: Commencing Attack
   PL:
51. [Kwestia głosowa [battle_endcommand_10601_1] (Commencing Attack)] 해보기는 할게요~ 안되면 어쩔 수 없지만요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_endcommand_10601_1].dlg
   limit: do 120 znaków
   EN: I’ll do what I can~ If it flunks, it flunks~
   PL:
52. [Kwestia głosowa [battle_enemy_break_10601_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_enemy_break_10601_1].desc
   limit: do 120 znaków
   EN: Enemy Stagger
   PL:
53. [Kwestia głosowa [battle_enemy_break_10601_1] (Enemy Stagger)] 하하. 재밌는 순간이에요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_enemy_break_10601_1].dlg
   limit: do 120 znaków
   EN: Haha. What an amusing moment~
   PL:
54. [Kwestia głosowa [battle_break_10601_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_break_10601_1].desc
   limit: do 120 znaków
   EN: Staggered
   PL:
55. [Kwestia głosowa [battle_break_10601_1] (Staggered)] 앗!
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_break_10601_1].dlg
   limit: do 120 znaków
   EN: Oh my!
   PL:
56. [Kwestia głosowa [battle_kill_10601_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_kill_10601_1].desc
   limit: do 120 znaków
   EN: Enemy Killed
   PL:
57. [Kwestia głosowa [battle_kill_10601_1] (Enemy Killed)] 늘 새롭다니까요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_kill_10601_1].dlg
   limit: do 120 znaków
   EN: I never run out of new sights to see~
   PL:
58. [Kwestia głosowa [battle_allydead_10601_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_allydead_10601_1].desc
   limit: do 120 znaków
   EN: Ally Death
   PL:
59. [Kwestia głosowa [battle_allydead_10601_1] (Ally Death)] 이런 많이 아픈가요? 나중에 말해주세요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_allydead_10601_1].dlg
   limit: do 120 znaków
   EN: Oh dear, does it hurt a lot? Please tell me later.
   PL:
60. [Kwestia głosowa [choice_success_p_10601_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=choice_success_p_10601_1].desc
   limit: do 120 znaków
   EN: Check Passed
   PL:
61. [Kwestia głosowa [choice_success_p_10601_1] (Check Passed)] 아하하, 너무 칭찬하진 말아 주세요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=choice_success_p_10601_1].dlg
   limit: do 120 znaków
   EN: Ahaha, there’s no need to shower me with praise.
   PL:
62. [Kwestia głosowa [choice_fail_n_10601_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=choice_fail_n_10601_1].desc
   limit: do 120 znaków
   EN: Check Failed
   PL:
63. [Kwestia głosowa [choice_fail_n_10601_1] (Check Failed)] 아~ 너무 자책하진 마세요. 그럴 수 있는 거죠.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=choice_fail_n_10601_1].dlg
   limit: do 120 znaków
   EN: Oh dear~ Don’t blame yourself too much. It just wasn’t your day.
   PL:
64. [Kwestia głosowa [battle_clear_10601_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_clear_10601_1].desc
   limit: do 120 znaków
   EN: Victory Cry
   PL:
65. [Kwestia głosowa [battle_clear_10601_1] (Victory Cry)] 어… 이거 제 덕분일까요? 이겼다니까 다행이네요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_clear_10601_1].dlg
   limit: do 120 znaków
   EN: Oh… Is this thanks to me, perhaps? Anyway, it’s nice to hear that we’ve won~
   PL:
66. [Kwestia głosowa [battle_clear_ex_10601_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_clear_ex_10601_1].desc
   limit: do 120 znaków
   EN: Extra Conditions Fulfilled
   PL:
67. [Kwestia głosowa [battle_clear_ex_10601_1] (Extra Conditions Fulfilled)] 너무 띄워주실 필요는 없어요~ 단테 님 덕분일 거예요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_clear_ex_10601_1].dlg
   limit: do 120 znaków
   EN: No need to shower me with compliments~ I’m sure you had a part in it, too.
   PL:
68. [Kwestia głosowa [battle_defeat_10601_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_defeat_10601_1].desc
   limit: do 120 znaków
   EN: Defeat Wail
   PL:
69. [Kwestia głosowa [battle_defeat_10601_1] (Defeat Wail)] 그럴 수도 있는 거 아니겠어요? 기운 내자고요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LCB_10601.json :: dataList[id=battle_defeat_10601_1].dlg
   limit: do 120 znaków
   EN: It is what it is, wouldn’t you agree? Don’t be so dour~
   PL:

## [00] Kurokumo Clan Wakashu — Hong Lu — 흑운회 와카슈
- ID Tożsamości: `10602` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 76 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed

70. [Karta Tożsamości — tytuł] 흑운회\n와카슈
   źródło: Personalities.json :: dataList[id=10602].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Kurokumo Clan\nWakashu
   PL:
71. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10602].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10602].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [Karta Tożsamości — opis] 홍루의 두번째 인격
   źródło: Personalities.json :: dataList[id=10602].desc
   limit: do 120 znaków
   EN: Hong Lu’s 2nd Identity
   PL:
74. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 베어내기
   źródło: Skills.json :: dataList[id=1060201].levelList[level=1].name ; dataList[id=1060201].levelList[level=2].name ; dataList[id=1060201].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Cleave
   PL:
75. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed
   PL:
76. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060201].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL:
77. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills.json :: dataList[id=1060201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL:
78. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 구름 절개
   źródło: Skills.json :: dataList[id=1060202].levelList[level=1].name ; dataList[id=1060202].levelList[level=2].name ; dataList[id=1060202].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Cloud Cutter
   PL:
79. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060202].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1060202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1060202].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1060202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL:
81. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [BeforeAttack] 대상의 출혈 횟수가 4미만이면 스킬의 1, 2코인이 추가됨
   źródło: Skills.json :: dataList[id=1060202].levelList[level=2].desc ; dataList[id=1060202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] If target has less than 4 Bleed Count, use Coin 1 and 2 an additional time
   PL:
82. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 구름 파열
   źródło: Skills.json :: dataList[id=1060203].levelList[level=3].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 7 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Cloudburst
   PL:
84. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] 이 스킬에서 부여하는 출혈, 마비 1 추가 부여
   źródło: Skills.json :: dataList[id=1060203].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] This skill inflicts 1 additional Bleed and Paralyze
   PL:
85. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060203].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 마비 5 부여
   źródło: Skills.json :: dataList[id=1060203].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Paralyze
   PL:
88. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1060204].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 9 · monety: 1 (+3)
   limit: do 40 znaków
   EN: Guard
   PL:
89. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — nazwa] 흑운도
   źródło: Passives.json :: dataList[id=1060201].name
   limit: do 40 znaków
   EN: Hēiyúndào
   PL:
90. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — opis] 연결한 죄 중 마지막 죄의 마지막 코인으로 공격할 때 출혈 3 부여
   źródło: Passives.json :: dataList[id=1060201].desc
   limit: do 120 znaków
   EN: The last Coin on the last skill in the chain inflicts 3 Bleed.
   PL:
91. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 조직의 보복
   źródło: Passives.json :: dataList[id=1060221].name
   limit: do 40 znaków
   EN: Syndicate Payback
   PL:
92. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 속도가 가장 높은 아군 1명 출혈 부여 값 +1
   źródło: Passives.json :: dataList[id=1060221].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed inflicts +1 Bleed.
   PL:
93. [Kwestia głosowa [get_10602_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=get_10602_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Kwestia głosowa [get_10602_1] (Identity Acquisition)] 명령하시는 건 다 따를 수 있어요~ 복종까지 바라면 곤란하지만~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=get_10602_1].dlg
   limit: do 120 znaków
   EN: I can follow your commands no problem~ Obedience might be a tall order, though~
   PL:
95. [Kwestia głosowa [lobby_morning_10602_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=lobby_morning_10602_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Kwestia głosowa [lobby_morning_10602_1] (Morning Greeting)] 아침에 일어나기가 너무 피곤할 때는 그냥 아무것도 하지 말고 쉬는 것도 답이에요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=lobby_morning_10602_1].dlg
   limit: do 120 znaków
   EN: When you’re too tired to get up, it might just be best to stay in and relax~
   PL:
97. [Kwestia głosowa [lobby_noon_10602_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=lobby_noon_10602_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Kwestia głosowa [lobby_noon_10602_1] (Afternoon Greeting)] 날이 너무 좋을 때면… 가끔 일광욕을 하기도 해요. 몸이 따뜻하게 데워지는 느낌이 좋거든요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=lobby_noon_10602_1].dlg
   limit: do 120 znaków
   EN: On wonderful days… I sometimes bathe in the sunlight. I like the warmth it wraps me up in.
   PL:
99. [Kwestia głosowa [lobby_night_10602_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=lobby_night_10602_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Kwestia głosowa [lobby_night_10602_1] (Evening Greeting)] 달빛조차도 구름에 가려지게 되는 캄캄한 밤이 되면… 이것 봐요, 정말 그림자와 하나가 되죠?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=lobby_night_10602_1].dlg
   limit: do 160 znaków
   EN: When dusk falls, and even the moonlight is shrouded by the clouds… Look, it really does blend with the shadows, doesn’t it?
   PL:
101. [Kwestia głosowa [smalltalk_10602_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=smalltalk_10602_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [Kwestia głosowa [smalltalk_10602_1] (Chatter #1)] 베는 건 언제나 즐거워요. 단, 명령 때문에 베는 건 조금… 재미없어요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=smalltalk_10602_1].dlg
   limit: do 130 znaków
   EN: It’s always fun to slash things. Doing it out of obligation, though… rather dampens the mood.
   PL:
103. [Kwestia głosowa [smalltalk_10602_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=smalltalk_10602_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Kwestia głosowa [smalltalk_10602_2] (Chatter #2)] 사람들은 왜 그렇게 자기 것에 집착하는지 모르겠어요. 마음을 넓~게 가지면 좋을 텐데 말이에요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=smalltalk_10602_2].dlg
   limit: do 150 znaków
   EN: It’s a mystery how people are so obsessed with what they own. If only they could nurture a spirit of generosity.
   PL:
105. [Kwestia głosowa [smalltalk_10602_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=smalltalk_10602_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Kwestia głosowa [smalltalk_10602_3] (Chatter #3)] 제가 맞설 상대는, 제가 정하는 게 좋아요. 정해진 대로만 살아가는 건… 의미가 없잖아요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=smalltalk_10602_3].dlg
   limit: do 160 znaków
   EN: I prefer to have autonomy in choosing my opponent. Doing as you’re told all the time… It’d end up being a pointless life.
   PL:
107. [Kwestia głosowa [smalltalk_10602_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=smalltalk_10602_4].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 1
   PL:
108. [Kwestia głosowa [smalltalk_10602_4] (Post-Uptie Chat 1)] 제가 진정으로 말을 높이는 분은, 단테 님 밖에 없어요. 마음이 가지 않는데 구태여 진심을 담아 존칭을 쓸 이유는 없잖아요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=smalltalk_10602_4].dlg
   limit: do 190 znaków
   EN: You’re the only one I treat with genuine respect, Lord Dante. I wouldn’t be calling you my lord if I didn’t truly feel that you deserve the title.
   PL:
109. [Kwestia głosowa [smalltalk_10602_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=smalltalk_10602_5].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 2
   PL:
110. [Kwestia głosowa [smalltalk_10602_5] (Post-Uptie Chat 2)] 단테 님은… 제가 수그리길 바라지 않아서 좋아요. 허리를 깍듯이 굽히면서 명령을 받드는 건… 영화에서나 재밌는 장면 아니겠어요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=smalltalk_10602_5].dlg
   limit: do 230 znaków
   EN: Lord Dante, what I like about you… is that you don’t demand I bow to you. Receiving orders from your boss with your back courteously bent… That’s only really fun in movies, no?
   PL:
111. [Kwestia głosowa [neglect_10602_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=neglect_10602_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [Kwestia głosowa [neglect_10602_1] (Idle)] 단테 님은 어디 가셨어요? 구름 속에 숨으셨나요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=neglect_10602_1].dlg
   limit: do 120 znaków
   EN: Where’d you go, Lord Dante? Have you hidden among the clouds?
   PL:
113. [Kwestia głosowa [gacksung_10602_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=gacksung_10602_1].desc
   limit: do 120 znaków
   EN: Uptying
   PL:
114. [Kwestia głosowa [gacksung_10602_1] (Uptying)] 고마워요. 제가 베어야 하는 게 또 있나요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=gacksung_10602_1].dlg
   limit: do 120 znaków
   EN: Thank you. Is there anything else you’d like me to fell?
   PL:
115. [Kwestia głosowa [formation_10602_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=formation_10602_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Kwestia głosowa [formation_10602_1] (Deployment)] 명령이라면~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=formation_10602_1].dlg
   limit: do 120 znaków
   EN: If that’s your orders~
   PL:
117. [Kwestia głosowa [battleentry_10602_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battleentry_10602_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Kwestia głosowa [battleentry_10602_1] (Stage Entry)] 제가 원하는 대로 베어버려도 되나요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battleentry_10602_1].dlg
   limit: do 120 znaków
   EN: Can I slit them however I see fit?
   PL:
119. [Kwestia głosowa [battle_select_10602_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_select_10602_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Kwestia głosowa [battle_select_10602_1] (Viewed in Battle)] 왔나요~ 단테 님.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_select_10602_1].dlg
   limit: do 120 znaków
   EN: Ah, you’re here, Lord Dante~
   PL:
121. [Kwestia głosowa [battle_endcommand_10602_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_endcommand_10602_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Kwestia głosowa [battle_endcommand_10602_1] (Commencing Attack)] 재미는 없겠지만, 그렇게 할게요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_endcommand_10602_1].dlg
   limit: do 120 znaków
   EN: It won’t be as fun, but I’ll do it~
   PL:
123. [Kwestia głosowa [battle_enemy_break_10602_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_enemy_break_10602_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Kwestia głosowa [battle_enemy_break_10602_1] (Enemy Stagger)] 좀 더 잘 벨 수 있을 거 같은데요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_enemy_break_10602_1].dlg
   limit: do 120 znaków
   EN: I think I could do a better job next time?
   PL:
125. [Kwestia głosowa [battle_break_10602_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_break_10602_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Kwestia głosowa [battle_break_10602_1] (Staggered)] 읍!
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_break_10602_1].dlg
   limit: do 120 znaków
   EN: Mmpf!
   PL:
127. [Kwestia głosowa [battle_kill_10602_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_kill_10602_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Kwestia głosowa [battle_kill_10602_1] (Enemy Killed)] 베는 건 즐겁네요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_kill_10602_1].dlg
   limit: do 120 znaków
   EN: What a joy it is to slash~
   PL:
129. [Kwestia głosowa [battle_allydead_10602_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_allydead_10602_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Kwestia głosowa [battle_allydead_10602_1] (Ally Death)] 고생이 많겠어요. 단테 님~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_allydead_10602_1].dlg
   limit: do 120 znaków
   EN: I don’t envy your outlook there, Lord Dante~
   PL:
131. [Kwestia głosowa [choice_success_p_10602_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=choice_success_p_10602_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Kwestia głosowa [choice_success_p_10602_1] (Check Passed)] 말했죠? 명령하시는 건 다 따른다고요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=choice_success_p_10602_1].dlg
   limit: do 120 znaków
   EN: I told you, I’ll follow your commands no problem~
   PL:
133. [Kwestia głosowa [choice_fail_n_10602_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=choice_fail_n_10602_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Kwestia głosowa [choice_fail_n_10602_1] (Check Failed)] 음… 괜찮죠~ 하라는 걸 했잖아요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=choice_fail_n_10602_1].dlg
   limit: do 120 znaków
   EN: Mmm… It’s fine~ I followed your orders after all, right?
   PL:
135. [Kwestia głosowa [battle_clear_10602_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_clear_10602_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Kwestia głosowa [battle_clear_10602_1] (Victory Cry)] 제 솜씨, 조금 멋스럽지 않았나요? 후후…
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_clear_10602_1].dlg
   limit: do 120 znaków
   EN: Wasn’t my swordsmanship snazzy to behold? Huhu…
   PL:
137. [Kwestia głosowa [battle_clear_ex_10602_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_clear_ex_10602_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Kwestia głosowa [battle_clear_ex_10602_1] (Extra Conditions Fulfilled)] 가야 할 곳으로 보내준 것뿐이죠. 보이는 걸 베어냈을 뿐이고요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_clear_ex_10602_1].dlg
   limit: do 120 znaków
   EN: I just sent them to where they belonged—by simply cutting down what I saw~
   PL:
139. [Kwestia głosowa [battle_defeat_10602_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_defeat_10602_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Kwestia głosowa [battle_defeat_10602_1] (Defeat Wail)] 검이 조금 무뎠나 봐요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kurokumo_10602.json :: dataList[id=battle_defeat_10602_1].dlg
   limit: do 120 znaków
   EN: The blade must’ve gotten a bit dull~
   PL:

## [000] Tingtang Gang Gangleader — Hong Lu — 콩콩이파 두목
- ID Tożsamości: `10603` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 1 · HP bazowe: 76 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed

141. [Karta Tożsamości — tytuł] 콩콩이파\n두목
   źródło: Personalities.json :: dataList[id=10603].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Tingtang Gang\nGangleader
   PL:
142. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10603].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10603].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Karta Tożsamości — opis] 홍루의 세번째 인격
   źródło: Personalities.json :: dataList[id=10603].desc
   limit: do 120 znaków
   EN: Hong Lu’s 3rd Identity
   PL:
145. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 목 긋기
   źródło: Skills.json :: dataList[id=1060301].levelList[level=1].name ; dataList[id=1060301].levelList[level=2].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Throat Slit
   PL:
146. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 4 부여
   źródło: Skills.json :: dataList[id=1060301].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 4 Bleed
   PL:
148. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 후비기
   źródło: Skills.json :: dataList[id=1060302].levelList[level=1].name ; dataList[id=1060302].levelList[level=2].name ; dataList[id=1060302].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 3 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Shank
   PL:
149. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 추가 피해 +2
   źródło: Skills.json :: dataList[id=1060302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Damage +2
   PL:
150. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 추가 피해 +2
   źródło: Skills.json :: dataList[id=1060302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 추가 피해 +3
   źródło: Skills.json :: dataList[id=1060302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Damage +3
   PL:
152. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 추가 피해 +3
   źródło: Skills.json :: dataList[id=1060302].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
153. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 적의 체력이 최대 체력의 25%미만일 때, 대상이 생존한 상태면 이 코인 1회 재사용\n앞면이 나오면 이 코인의 피해량 +50%
   źródło: Skills.json :: dataList[id=1060302].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1060302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] If target is below 25% HP, use this Coin an additional time if target survives\nHeads: +50% Damage for this Coin
   PL:
154. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [ReUseOnSucceedAttackHead] 이 코인 스킬 피해량 +50%
   źródło: Skills.json :: dataList[id=1060302].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1060302].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttackHead]
   znaczenie tagów: [ReUseOnSucceedAttackHead] = [재사용 앞면 적중 시] / [Reuse - Heads Hit]
   EN: [ReUseOnSucceedAttackHead] +50% Damage for this Coin
   PL:
155. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Laceration]이 7 이상이면, 피해량 +20%
   źródło: Skills.json :: dataList[id=1060302].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 7+ [Laceration], deal +20% damage
   PL:
156. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 난도질
   źródło: Skills.json :: dataList[id=1060303].levelList[level=3].name ; dataList[id=1060303].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 1 (+25)
   limit: do 40 znaków
   EN: Mutilate
   PL:
157. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] [EnemyKill] 이 스킬 1회 재사용
   źródło: Skills.json :: dataList[id=1060303].levelList[level=3].desc ; dataList[id=1060303].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Use this skill 1 more time
   PL:
158. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 추가 피해 +7
   źródło: Skills.json :: dataList[id=1060303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1060303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Damage +7
   PL:
159. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [ReUseOnSucceedAttackHead] 이 코인 스킬 피해량 +100%
   źródło: Skills.json :: dataList[id=1060303].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttackHead]
   znaczenie tagów: [ReUseOnSucceedAttackHead] = [재사용 앞면 적중 시] / [Reuse - Heads Hit]
   EN: [ReUseOnSucceedAttackHead] +100% Damage for this Coin
   PL:
160. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [ReUseOnSucceedAttackHead] 이 코인 스킬 피해량 +100%
   źródło: Skills.json :: dataList[id=1060303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttackHead]
   znaczenie tagów: [ReUseOnSucceedAttackHead] = [재사용 앞면 적중 시] / [Reuse - Heads Hit]
   EN: [ReUseOnSucceedAttackHead] +100% damage for this Coin
   PL:
161. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [ReUseOnSucceedAttackHead] 대상의 [Laceration]이 10 이상이면, 피해량 +50%
   źródło: Skills.json :: dataList[id=1060303].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttackHead], [Laceration]
   znaczenie tagów: [ReUseOnSucceedAttackHead] = [재사용 앞면 적중 시] / [Reuse - Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [ReUseOnSucceedAttackHead] If target has 10+ [Laceration], deal +50% damage
   PL:
162. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1060304].levelList[level=1].name ; dataList[id=1060304].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: unik · moc bazowa: 2 · monety: 1 (+14)
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Obrona (ulepszenie 4) — opis] 대상의 [Laceration]이 5 이상이면, 코인 위력 +2\n[OnSucceedEvade] 정신력 3 회복
   źródło: Skills.json :: dataList[id=1060304].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [OnSucceedEvade]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: If target has 5+ [Laceration], Coin Power +2\n[OnSucceedEvade] Heal 3 SP
   PL:
164. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Glut.) — nazwa] 유열
   źródło: Passives.json :: dataList[id=1060301].name
   limit: do 40 znaków
   EN: Gaiety
   PL:
165. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Glut.) — opis] 다음 턴 시작 시 (탐식 공명 수 x2) 만큼 정신력 회복
   źródło: Passives.json :: dataList[id=1060301].desc
   limit: do 120 znaków
   EN: Heal (2x Gluttony Reson.) SP next turn.
   PL:
166. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — nazwa] 승부수
   źródło: Passives.json :: dataList[id=1060321].name
   limit: do 40 znaków
   EN: Gambit
   PL:
167. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — opis] 정신력이 가장 높은 아군 1명 앞면이 나온 코인의 피해량 +20%
   źródło: Passives.json :: dataList[id=1060321].desc
   limit: do 120 znaków
   EN: 1 ally with the most SP deals +20% damage with Heads Coins.
   PL:
168. [Kwestia głosowa [get_10603_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=get_10603_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Kwestia głosowa [get_10603_1] (Identity Acquisition)] 누구죠, 날 부른 사람이? 감당되겠어요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=get_10603_1].dlg
   limit: do 120 znaków
   EN: Who chose to bring me here? Think you can handle the consequences?
   PL:
170. [Kwestia głosowa [lobby_morning_10603_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=lobby_morning_10603_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Kwestia głosowa [lobby_morning_10603_1] (Morning Greeting)] 아침은 저의 시간이 아니에요. 왜 사람들은 쓸데없이 일찍 일어나는 거에 에너지를 소비하는 걸까요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=lobby_morning_10603_1].dlg
   limit: do 130 znaków
   EN: Dawn isn’t the time for me. I wonder why people decide to waste their energy by getting up early?
   PL:
172. [Kwestia głosowa [lobby_noon_10603_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=lobby_noon_10603_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Kwestia głosowa [lobby_noon_10603_1] (Afternoon Greeting)] 와~ 다 썰어버리기 딱 좋은 날이네요~ 그렇지 않나요 단테? …아하, 농담이에요. 농담.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=lobby_noon_10603_1].dlg
   limit: do 130 znaków
   EN: Wow~ What a lovely day for mutilation~ Isn’t that right, Dante? …Aha, I was kidding, of course.
   PL:
174. [Kwestia głosowa [lobby_night_10603_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=lobby_night_10603_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Kwestia głosowa [lobby_night_10603_1] (Evening Greeting)] 로쟈씨가 그렇게 도박을 잘하신다면서요? 심심한데, 한 번 겨뤄보자 할까?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=lobby_night_10603_1].dlg
   limit: do 130 znaków
   EN: I heard Rodya is a rather skilled gambler, is that right? Perhaps I’ll ask her for a match or two?
   PL:
176. [Kwestia głosowa [smalltalk_10603_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=smalltalk_10603_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Kwestia głosowa [smalltalk_10603_1] (Chatter #1)] 단테, 그런 촌스러운 옷 말고 관리자답게, 개성 있는, 화려한 옷을 입어보는 게 어때요? 제가 하나 보내드릴까?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=smalltalk_10603_1].dlg
   limit: do 200 znaków
   EN: Dante, how about changing out of that drab outfit into something more unique that better suits a manager? I could lend you some clothing if you want.
   PL:
178. [Kwestia głosowa [smalltalk_10603_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=smalltalk_10603_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Kwestia głosowa [smalltalk_10603_2] (Chatter #2)] 혹시… 불만이라도 있는 건 아니죠, 단테? 표정이 안 보이니까 괜히 띠꺼워 보여서~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=smalltalk_10603_2].dlg
   limit: do 160 znaków
   EN: Now then… You’re not upset with me or anything, right, Dante? I can’t see your expressions, so it’s kinda been nagging me~
   PL:
180. [Kwestia głosowa [smalltalk_10603_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=smalltalk_10603_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Kwestia głosowa [smalltalk_10603_3] (Chatter #3)] 칼을 쥐는 법을 알려달라고요? 간단해요. 그냥 손에 쥐고 기분이 내키는 대로 휙휙 가르면 되는 거예요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=smalltalk_10603_3].dlg
   limit: do 150 znaków
   EN: How do you hold a knife? It’s simple. Just grab it as you like and swing it up, down, and around on your whims.
   PL:
182. [Kwestia głosowa [smalltalk_10603_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=smalltalk_10603_4].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Kwestia głosowa [smalltalk_10603_4] (Post-Uptie Chat 1)] 운은 말이죠… 쟁취하는 거예요. 인생은 가만히 앉아서 기다린다고 잭팟이 떠주지는 않는다고요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=smalltalk_10603_4].dlg
   limit: do 130 znaków
   EN: You see, luck… is something you earn. Life doesn’t serve you up a jackpot if you just sit and wait~
   PL:
184. [Kwestia głosowa [smalltalk_10603_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=smalltalk_10603_5].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Kwestia głosowa [smalltalk_10603_5] (Post-Uptie Chat 2)] 나중에 우리 애들 한 번 인사시켜줄게요~ 말은 좀 험하게 해도 성격은 다들 순해요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=smalltalk_10603_5].dlg
   limit: do 150 znaków
   EN: I’ll introduce you to my buddies later~ They can be rough talkers, but they’re all nice when you get to know them~
   PL:
186. [Kwestia głosowa [neglect_10603_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=neglect_10603_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Kwestia głosowa [neglect_10603_1] (Idle)] 와, 우리 단테 님은 목숨이 여러 개인가 보다, 그렇죠?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=neglect_10603_1].dlg
   limit: do 120 znaków
   EN: Gee, it looks like someone doesn’t value their own life, huh?
   PL:
188. [Kwestia głosowa [gacksung_10603_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=gacksung_10603_1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Kwestia głosowa [gacksung_10603_1] (Uptying)] 아, 뭘 이런 걸 다~ 사양은 안 할게요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=gacksung_10603_1].dlg
   limit: do 120 znaków
   EN: Oh, you’re flattering me~ I won’t say no to it, though~
   PL:
190. [Kwestia głosowa [formation_10603_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=formation_10603_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Kwestia głosowa [formation_10603_1] (Deployment)] 제 차례인가요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=formation_10603_1].dlg
   limit: do 120 znaków
   EN: Is it my turn?
   PL:
192. [Kwestia głosowa [battleentry_10603_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battleentry_10603_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Kwestia głosowa [battleentry_10603_1] (Stage Entry)] 몸 좀 풀어볼까요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battleentry_10603_1].dlg
   limit: do 120 znaków
   EN: Let’s get some warm-up~
   PL:
194. [Kwestia głosowa [battle_select_10603_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_select_10603_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Kwestia głosowa [battle_select_10603_1] (Viewed in Battle)] 도움이 필요하세요? 단테 님?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_select_10603_1].dlg
   limit: do 120 znaków
   EN: Do you need my help, Dante?
   PL:
196. [Kwestia głosowa [battle_endcommand_10603_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_endcommand_10603_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Kwestia głosowa [battle_endcommand_10603_1] (Commencing Attack)] 운이 따라준다면 좋겠네요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_endcommand_10603_1].dlg
   limit: do 120 znaków
   EN: I hope luck is on my side~
   PL:
198. [Kwestia głosowa [battle_enemy_break_10603_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_enemy_break_10603_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Kwestia głosowa [battle_enemy_break_10603_1] (Enemy Stagger)] 단테 님. 봤어요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_enemy_break_10603_1].dlg
   limit: do 120 znaków
   EN: Well, Dante? Did you see?
   PL:
200. [Kwestia głosowa [battle_break_10603_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_break_10603_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Kwestia głosowa [battle_break_10603_1] (Staggered)] 윽!
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_break_10603_1].dlg
   limit: do 120 znaków
   EN: Unk!
   PL:
202. [Kwestia głosowa [battle_kill_10603_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_kill_10603_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Kwestia głosowa [battle_kill_10603_1] (Enemy Killed)] 너무 쉽군요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_kill_10603_1].dlg
   limit: do 120 znaków
   EN: Just too easy~
   PL:
204. [Kwestia głosowa [battle_allydead_10603_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_allydead_10603_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Kwestia głosowa [battle_allydead_10603_1] (Ally Death)] 내 운을 빌려줄 걸 그랬나?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_allydead_10603_1].dlg
   limit: do 120 znaków
   EN: Maybe I should’ve lent a bit of my luck?
   PL:
206. [Kwestia głosowa [choice_success_p_10603_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=choice_success_p_10603_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Kwestia głosowa [choice_success_p_10603_1] (Check Passed)] 운은 실력과도 연관되어 있죠
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=choice_success_p_10603_1].dlg
   limit: do 120 znaków
   EN: Luck goes hand in hand with skill.
   PL:
208. [Kwestia głosowa [choice_fail_n_10603_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=choice_fail_n_10603_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Kwestia głosowa [choice_fail_n_10603_1] (Check Failed)] 음… 운이 따라주지 않네요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=choice_fail_n_10603_1].dlg
   limit: do 120 znaków
   EN: Hmm… Fortune isn’t on my side.
   PL:
210. [Kwestia głosowa [battle_clear_10603_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_clear_10603_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Kwestia głosowa [battle_clear_10603_1] (Victory Cry)] 이 정도야 뭐, 애들 장난이었죠~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_clear_10603_1].dlg
   limit: do 120 znaków
   EN: Well now, this was basically child’s play~
   PL:
212. [Kwestia głosowa [battle_clear_ex_10603_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_clear_ex_10603_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Kwestia głosowa [battle_clear_ex_10603_1] (Extra Conditions Fulfilled)] 어라, 언제 다 해치웠담~ 이제 가도 되죠?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_clear_ex_10603_1].dlg
   limit: do 120 znaków
   EN: Oh my, we’re done with them already~ I can go now, can’t I?
   PL:
214. [Kwestia głosowa [battle_defeat_10603_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_defeat_10603_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Kwestia głosowa [battle_defeat_10603_1] (Defeat Wail)] 이럴 리가… 없는데~?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kongkong_10603.json :: dataList[id=battle_defeat_10603_1].dlg
   limit: do 120 znaków
   EN: This… can’t be~?
   PL:

## [00] Liu Assoc. South Section 5 — Hong Lu — 남부 리우 협회 5과
- ID Tożsamości: `10604` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 76 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Burn

216. [Karta Tożsamości — tytuł] 남부 리우 협회\n5과
   źródło: Personalities.json :: dataList[id=10604].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Liu Assoc.\nSouth Section 5
   PL:
217. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10604].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10604].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Karta Tożsamości — opis] 홍루의 네번째 인격
   źródło: Personalities.json :: dataList[id=10604].desc
   limit: do 120 znaków
   EN: Hong Lu’s 4th Identity
   PL:
220. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 몸풀기
   źródło: Skills.json :: dataList[id=1060401].levelList[level=1].name ; dataList[id=1060401].levelList[level=2].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Warm Up
   PL:
221. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1060401].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1060401].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Burn
   PL:
222. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 정신력 3 회복
   źródło: Skills.json :: dataList[id=1060401].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 3 SP
   PL:
223. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 흐르는 불꽃
   źródło: Skills.json :: dataList[id=1060402].levelList[level=1].name ; dataList[id=1060402].levelList[level=2].name ; dataList[id=1060402].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 6 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Flowing Flame
   PL:
224. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여. 대상에게 [Combustion]이 있으면 1 추가 부여
   źródło: Skills.json :: dataList[id=1060402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1060402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]; if target already has [Combustion], inflict 1 more
   PL:
225. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills.json :: dataList[id=1060402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count
   PL:
226. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가. 자신의 정신력이 30 이상이면, 1, 45 이상이면, 2 추가 증가
   źródło: Skills.json :: dataList[id=1060402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count; at 30+ SP, inflict 1 more; at 45+ SP, inflict 2 more
   PL:
227. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Combustion] 횟수가 6 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1060402].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion] Count, Coin Power +2
   PL:
228. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 홍염권
   źródło: Skills.json :: dataList[id=1060403].levelList[level=3].name ; dataList[id=1060403].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Crimson Blaze Fist
   PL:
229. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여. 대상에게 [Combustion]이 있으면 [Combustion] 횟수 1 증가
   źródło: Skills.json :: dataList[id=1060403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1060403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]; if target already has [Combustion], inflict +1 [Combustion] Count
   PL:
230. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 정신력 6 회복
   źródło: Skills.json :: dataList[id=1060403].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1060403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal 6 SP
   PL:
231. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion] 횟수가 6 이상이면, 피해량의 30%만큼 흐트러짐 손상을 입힘
   źródło: Skills.json :: dataList[id=1060403].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1060403].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion] Count, raise Stagger Threshold by 30% of damage dealt
   PL:
232. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Combustion] 횟수가 6 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1060403].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion] Count, Coin Power +1
   PL:
233. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1060404].levelList[level=1].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — nazwa] 끓어오르는군요~
   źródło: Passives.json :: dataList[id=1060401].name
   limit: do 40 znaków
   EN: Flaring Up~
   PL:
235. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — opis] 자신의 정신력이 30 이상이면 공격 스킬의 스킬 효과, 코인 효과로 부여하는 화상 횟수 부여 값 +1
   źródło: Passives.json :: dataList[id=1060401].desc
   limit: do 120 znaków
   EN: At 30+ SP, inflict +1 Burn Count with the effects of attack skills/coins.
   PL:
236. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Wrath) — nazwa] 따뜻하죠?
   źródło: Passives.json :: dataList[id=1060421].name
   limit: do 40 znaków
   EN: Isn’t It Warm?
   PL:
237. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Wrath) — opis] 정신력이 가장 높은 아군 1명의 공격 스킬의 스킬 효과, 코인 효과로 부여하는 화상 횟수 부여 값 +1
   źródło: Passives.json :: dataList[id=1060421].desc
   limit: do 130 znaków
   EN: 1 ally with the most SP inflicts +1 Burn Count with the effects of their attack skills/coins.
   PL:
238. [Kwestia głosowa [get_10604_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=get_10604_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [Kwestia głosowa [get_10604_1] (Identity Acquisition)] 한잔 함께 하시지요. 따뜻해질 거예요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=get_10604_1].dlg
   limit: do 120 znaków
   EN: What do you say we have a drink together? It’ll warm you right up~
   PL:
240. [Kwestia głosowa [lobby_morning_10604_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=lobby_morning_10604_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
241. [Kwestia głosowa [lobby_morning_10604_1] (Morning Greeting)] 늦잠이 없으시네요~ 조금 정도는 게을러도 된답니다?
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=lobby_morning_10604_1].dlg
   limit: do 120 znaków
   EN: You’re an early riser, I see~ A little laziness wouldn’t hurt, you know?
   PL:
242. [Kwestia głosowa [lobby_noon_10604_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=lobby_noon_10604_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Kwestia głosowa [lobby_noon_10604_1] (Afternoon Greeting)] 기름진 식사 후에는 꼭 차를 곁들여야 한답니다~ 어떻게, 좀 드시겠어요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=lobby_noon_10604_1].dlg
   limit: do 120 znaków
   EN: A cup of tea is a must-have after a greasy meal~ So, would you care for some?
   PL:
244. [Kwestia głosowa [lobby_night_10604_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=lobby_night_10604_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Kwestia głosowa [lobby_night_10604_1] (Evening Greeting)] 이제 주무시나요? 이런… 그런 옷을 입고선 불편해서 잠이 안올 것 같은데요… 제 비단옷을 좀 빌려드려야겠어요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=lobby_night_10604_1].dlg
   limit: do 190 znaków
   EN: Will you retire for the night? Oh my… That outfit sure doesn’t look to be comfortable sleepwear… I’ll have to lend you one of my silk garments~
   PL:
246. [Kwestia głosowa [smalltalk_10604_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=smalltalk_10604_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Kwestia głosowa [smalltalk_10604_1] (Chatter #1)] 항상 하던 수련이 직업이 되었을 뿐이지만… 일은 언제든 피로하다는 기분이 드네요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=smalltalk_10604_1].dlg
   limit: do 150 znaków
   EN: What I do at my job is mostly the same as my usual training… Yet I can’t help but feel fatigued when it is work.
   PL:
248. [Kwestia głosowa [smalltalk_10604_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=smalltalk_10604_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Kwestia głosowa [smalltalk_10604_2] (Chatter #2)] 몸을 움직이는 것은 그다지 선호하진 않아요. 가끔씩, 내킬 때 할 뿐이죠… 그것보단 차를 내리는게 더 즐겁죠.\n본가에 있을 때는 내키지 않아도 움직여야 할 일이 많았어서… 하하!
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=smalltalk_10604_2].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I don’t particularly care for physical work. I only feel like it from time to time… Brewing tea is much more fun.\nBack home, many occasions needed me to get moving whether I wanted it or not… Haha!
   PL:
250. [Kwestia głosowa [smalltalk_10604_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=smalltalk_10604_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Kwestia głosowa [smalltalk_10604_3] (Chatter #3)] 불꽃을 일으키는 방법…? 그런 방법에 의문을 가지지 않는 것이 핵심이랍니다.\n그런걸 궁금해봐야 결국 아무 소용 없더라고요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=smalltalk_10604_3].dlg
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: How to make a fire...? The key is not to question how.\nThere was no use wondering about things like that, I'm telling you~
   PL:
252. [Kwestia głosowa [smalltalk_10604_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=smalltalk_10604_4].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Kwestia głosowa [smalltalk_10604_4] (Post-Uptie Chat 1)] 찻잎에 대해 흥미가 생기셨다고요? 물론이죠, 알려드릴 수 있어요~\n아… 그런데, 제가 쓰는 다기나 차는 꽤 고급이라… 저기, 괜찮으시죠?
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=smalltalk_10604_4].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You’re taking an interest in my tea leaves? Why sure, I can teach you~\nAh… I should mention that the tea sets and brews I have can be quite expensive… Um, are you alright?
   PL:
254. [Kwestia głosowa [smalltalk_10604_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=smalltalk_10604_5].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Kwestia głosowa [smalltalk_10604_5] (Post-Uptie Chat 2)] 직접 저희의 무투를 공부해보고 싶다면, 도와드릴 수 있어요~\n사실, 6과의 다른 후배 분들께도 가르쳐 드린 적이 있거든요~ 자신 있답니다!
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=smalltalk_10604_5].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If you’re interested in practicing our martial arts, I could help~\nIn fact, I’ve instructed a couple of my coworkers from Section 6, too~ I’m sure I’ll be a good teacher!
   PL:
256. [Kwestia głosowa [neglect_10604_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=neglect_10604_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Kwestia głosowa [neglect_10604_1] (Idle)] 흐음… 햇살 내음이 좋네요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=neglect_10604_1].dlg
   limit: do 120 znaków
   EN: Hmm… What a lovely scent the sun’s rays exude~
   PL:
258. [Kwestia głosowa [gacksung_10604_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=gacksung_10604_1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Kwestia głosowa [gacksung_10604_1] (Uptying)] 그렇군요~ 언제 쯤 말을 꺼내시나 기다리고 있기는 했답니다~
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=gacksung_10604_1].dlg
   limit: do 120 znaków
   EN: I see~ I was starting to wonder when you’d bring this up~
   PL:
260. [Kwestia głosowa [formation_10604_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=formation_10604_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Kwestia głosowa [formation_10604_1] (Deployment)] 따뜻하게, 혹은 뜨겁게.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=formation_10604_1].dlg
   limit: do 120 znaków
   EN: With warmth—sometimes heat.
   PL:
262. [Kwestia głosowa [battleentry_10604_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battleentry_10604_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Kwestia głosowa [battleentry_10604_1] (Stage Entry)] 끓어넘칠 시간이군요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battleentry_10604_1].dlg
   limit: do 120 znaków
   EN: It’s time to flare up, isn’t it?
   PL:
264. [Kwestia głosowa [battle_select_10604_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_select_10604_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Kwestia głosowa [battle_select_10604_1] (Viewed in Battle)] 하실 말씀이 있나요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_select_10604_1].dlg
   limit: do 120 znaków
   EN: Is there anything you want to say?
   PL:
266. [Kwestia głosowa [battle_endcommand_10604_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_endcommand_10604_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Kwestia głosowa [battle_endcommand_10604_1] (Commencing Attack)] 부드럽게!
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_endcommand_10604_1].dlg
   limit: do 120 znaków
   EN: With grace!
   PL:
268. [Kwestia głosowa [battle_enemy_break_10604_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_enemy_break_10604_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Kwestia głosowa [battle_enemy_break_10604_1] (Enemy Stagger)] 균형이 무너졌군요!
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_enemy_break_10604_1].dlg
   limit: do 120 znaków
   EN: Their balance is broken!
   PL:
270. [Kwestia głosowa [battle_break_10604_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_break_10604_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Kwestia głosowa [battle_break_10604_1] (Staggered)] 에구…
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_break_10604_1].dlg
   limit: do 120 znaków
   EN: Oh dear…
   PL:
272. [Kwestia głosowa [battle_kill_10604_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_kill_10604_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Kwestia głosowa [battle_kill_10604_1] (Enemy Killed)] 불타올랐군요!
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_kill_10604_1].dlg
   limit: do 120 znaków
   EN: It burns bright!
   PL:
274. [Kwestia głosowa [battle_dead_10604_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_dead_10604_1].desc
   limit: do 120 znaków
   EN: Death
   PL:
275. [Kwestia głosowa [battle_dead_10604_1] (Death)] 따뜻한… 차가 마시고… 싶어… 요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_dead_10604_1].dlg
   limit: do 120 znaków
   EN: Well, I… really could use… a warm cup… of tea.
   PL:
276. [Kwestia głosowa [choice_success_p_10604_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=choice_success_p_10604_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Kwestia głosowa [choice_success_p_10604_2] (Check Passed)] 좋은 향을 따라갔죠.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=choice_success_p_10604_2].dlg
   limit: do 120 znaków
   EN: I followed a nice scent.
   PL:
278. [Kwestia głosowa [choice_fail_n_10604_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=choice_fail_n_10604_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Kwestia głosowa [choice_fail_n_10604_1] (Check Failed)] 어쩐지 텁텁하더라니…
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=choice_fail_n_10604_1].dlg
   limit: do 120 znaków
   EN: No wonder the flavor was unpleasant…
   PL:
280. [Kwestia głosowa [battle_clear_10604_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_clear_10604_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Kwestia głosowa [battle_clear_10604_1] (Victory Cry)] 흠~ 좋은 몸풀기였네요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_clear_10604_1].dlg
   limit: do 120 znaków
   EN: Hm~ That gave me good exercise.
   PL:
282. [Kwestia głosowa [battle_clear_ex_10604_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_clear_ex_10604_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Kwestia głosowa [battle_clear_ex_10604_1] (Extra Conditions Fulfilled)] 이런~ 예상보다 더 흥분했나보네요. 아하핫…
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_clear_ex_10604_1].dlg
   limit: do 120 znaków
   EN: Oh my~ I guess I got a little more excited than I expected. Ahahah…
   PL:
284. [Kwestia głosowa [battle_defeat_10604_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_defeat_10604_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Kwestia głosowa [battle_defeat_10604_1] (Defeat Wail)] 자, 차나 마시러 가자구요. 가끔은 이럴 때도 있는거잖아요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_LiuAsso5_10604.json :: dataList[id=battle_defeat_10604_1].dlg
   limit: do 120 znaków
   EN: Come now, let’s move somewhere else for tea. These things just happen sometimes, no?
   PL:

## [000] K Corp. Class 3 Excision Staff — Hong Lu — K사 3등급 적출직 직원
- ID Tożsamości: `10605` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 2 · HP bazowe: 99 · szybkość: 1–5 / 2–5 / 2–6 / 2–6
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Rupture

286. [Karta Tożsamości — tytuł] K사 3등급\n적출직 직원
   źródło: Personalities.json :: dataList[id=10605].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: K Corp. Class 3\nExcision Staff
   PL:
287. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10605].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10605].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Karta Tożsamości — opis] 홍루의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10605].desc
   limit: do 120 znaków
   EN: Hong Lu’s 5th Identity
   PL:
290. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 침입자 차단
   źródło: Skills.json :: dataList[id=1060501].levelList[level=1].name ; dataList[id=1060501].levelList[level=2].name ; dataList[id=1060501].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Impede the Intruder
   PL:
291. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 대상에게 [Burst]이 5 이상 있으면 코인 위력 +1
   źródło: Skills.json :: dataList[id=1060501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 5+ [Burst], Coin Power +1
   PL:
292. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상에게 [Burst]이 5 이상 있으면 코인 위력 +2
   źródło: Skills.json :: dataList[id=1060501].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 5+ [Burst], Coin Power +2
   PL:
293. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상에게 [Burst]이 5 이상 있으면 코인 위력 +3\n[WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 5 증가
   źródło: Skills.json :: dataList[id=1060501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: If target has 5+ [Burst], Coin Power +3\n[WhenUse] Gain +5 Aggro to this Skill Slot next turn
   PL:
294. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 붕괴 칼날
   źródło: Skills.json :: dataList[id=1060502].levelList[level=1].name ; dataList[id=1060502].levelList[level=2].name ; dataList[id=1060502].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 6 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Decay Blade
   PL:
295. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여\n대상에게 [Burst]이 10 이상 있으면 피해량의 20%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1060502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 Rupture\nIf target has 10+ [Burst], heal by 20% of damage dealt
   PL:
296. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여\n대상에게 [Burst]이 10 이상 있으면 피해량의 20%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1060502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여\n대상에게 [Burst]이 10 이상 있으면 피해량의 50%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1060502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 Rupture\nIf target has 10+ [Burst], heal by 50% of damage dealt
   PL:
298. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여\n대상에게 [Burst]이 10 이상 있으면 피해량의 50%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1060502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 5 증가
   źródło: Skills.json :: dataList[id=1060502].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +5 Aggro to this Skill Slot next turn
   PL:
300. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 대상 적출
   źródło: Skills.json :: dataList[id=1060503].levelList[level=3].name ; dataList[id=1060503].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 8 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Excise Target
   PL:
301. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 현재 체력이 80% 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1060503].levelList[level=3].desc
   limit: do 120 znaków
   EN: At 80% or more HP, Coin Power +1
   PL:
302. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 4 부여
   źródło: Skills.json :: dataList[id=1060503].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1060503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Rupture
   PL:
303. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] K사 앰플 만큼 파열 횟수 증가. (K사 앰플 x 5)% 만큼 피해량이 증가함
   źródło: Skills.json :: dataList[id=1060503].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1060503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Rupture Count by the amount of K Corp Ampule; Deal +5% damage per K Corp Ampule
   PL:
304. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 현재 체력이 80% 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1060503].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 80% or more HP, Coin Power +2
   PL:
305. [Obrona (ulepszenia 1,4) — nazwa] 앰플 주입
   źródło: Skills.json :: dataList[id=1060504].levelList[level=1].name ; dataList[id=1060504].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Ampule Injection
   PL:
306. [Obrona (ulepszenie 1) — opis] [WhenUse] 다음 턴에 K사 앰플 1 얻음
   źródło: Skills.json :: dataList[id=1060504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 K Corp Ampule next turn
   PL:
307. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 K사 앰플 1 얻음\n[WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 5 증가
   źródło: Skills.json :: dataList[id=1060504].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 K Corp Ampule next turn\n[WhenUse] Gain +5 Aggro to this Skill Slot next turn
   PL:
308. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — nazwa] 재생 앰플 활성화
   źródło: Passives.json :: dataList[id=1060501].name
   limit: do 50 znaków
   EN: Regeneration Ampule Activation
   PL:
309. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — opis] 피격 시 현재 체력이 최대 체력의 20% 미만이면, 최대 체력의 90%만큼 체력을 회복하고 K사 앰플 1을 얻음\n위 효과가 발동되면 이번 전투동안 매 턴 취약 1을 얻음 (전투 당 1회)
   źródło: Passives.json :: dataList[id=1060501].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When hit, if at less than 20% HP, heal by 90% of Max HP and gain 1 K Corp Ampule.\nAfter this activates, gain 1 Fragile every turn for the rest of the battle. (Once per battle)
   PL:
310. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — nazwa] 고농축 앰플
   źródło: Passives.json :: dataList[id=1060521].name
   limit: do 40 znaków
   EN: High-grade Ampule
   PL:
311. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — opis] 전투 시작 시 현재 체력 비율이 가장 낮은 아군 1명에게 K사 앰플 2 부여
   źródło: Passives.json :: dataList[id=1060521].desc
   limit: do 130 znaków
   EN: At the start of the combat phase, give 2 K Corp Ampule to 1 ally with the lowest HP percentage.
   PL:
312. [Kwestia głosowa [get_10605_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=get_10605_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [Kwestia głosowa [get_10605_1] (Identity Acquisition)] 흠… 눈 앞의 사람들을 전부 적출해버리면 되는 거죠?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=get_10605_1].dlg
   limit: do 120 znaków
   EN: Hmm... So I need to excise everyone in sight, right?
   PL:
314. [Kwestia głosowa [lobby_morning_10605_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=lobby_morning_10605_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Kwestia głosowa [lobby_morning_10605_1] (Morning Greeting)] 바깥이 낮인지, 밤인지는 구분하기 힘들어요. 저는 적출이 필요할 때 빼고는 항상… 이곳에 있으니까.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=lobby_morning_10605_1].dlg
   limit: do 150 znaków
   EN: It's hard to tell if it's day or night outside. Other than times when excision is needed... I always stay here.
   PL:
316. [Kwestia głosowa [lobby_noon_10605_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=lobby_noon_10605_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Kwestia głosowa [lobby_noon_10605_1] (Afternoon Greeting)] 그렇군요… 지금이 낮인가요? 그립네요. 예전에는 느지막하게 차라도 마시고 있을 시간인데.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=lobby_noon_10605_1].dlg
   limit: do 150 znaków
   EN: I see... So it's daytime right now? That brings back memories. I used to lazily drink this at this time of the day.
   PL:
318. [Kwestia głosowa [lobby_night_10605_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=lobby_night_10605_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [Kwestia głosowa [lobby_night_10605_1] (Evening Greeting)] 아, 밤이라는 건 알고 있었답니다. 야간 근무를 하시는 분들이 방금 막 들렀다 가셨거든요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=lobby_night_10605_1].dlg
   limit: do 130 znaków
   EN: Ah, I was aware that it's nighttime. The staff working the night shift paid a visit just now.
   PL:
320. [Kwestia głosowa [smalltalk_10605_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=smalltalk_10605_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Kwestia głosowa [smalltalk_10605_1] (Chatter #1)] 필요한 상황이 아니면… 저희 3등급 적출직들은, 몸을 늘 HP앰플의 종류와 농도에 적합하도록 만들어야 하거든요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=smalltalk_10605_1].dlg
   limit: do 240 znaków
   EN: Outside of situations where we're needed... We Class 3 Excision staff members have to make sure our bodies are suitable for the type and concentration of the HP ampule to be administered.
   PL:
322. [Kwestia głosowa [smalltalk_10605_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=smalltalk_10605_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Kwestia głosowa [smalltalk_10605_2] (Chatter #2)] 재생앰플은 정말 유용한 기술인 것 같아요… 이렇게, 건강을 유지하고 몸을 고칠 수도 있고~ 농도를 바꿔서 붕괴시키는 공격수단으로 쓸 수도 있고.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=smalltalk_10605_2].dlg
   limit: do 240 znaków
   EN: Regeneration ampules are such a convenient invention... Like this, they can be used to keep us healthy and fix any wound~ And the concentration can be changed to induce decay in our foes.
   PL:
324. [Kwestia głosowa [smalltalk_10605_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=smalltalk_10605_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Kwestia głosowa [smalltalk_10605_3] (Chatter #3)] 아… 기계하고는 싸우기 싫은데. 제 무기엔 생체조직에만 반응하는 칼날이 달려있어서 기계에는 잘 안 통하더라고요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=smalltalk_10605_3].dlg
   limit: do 180 znaków
   EN: Ah... I don't like fighting against machines. The blade on my weapon only reacts to organic tissues, so it doesn't work that well on steel~
   PL:
326. [Kwestia głosowa [smalltalk_10605_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=smalltalk_10605_4].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Kwestia głosowa [smalltalk_10605_4] (Post-Uptie Chat 1)] 어떻게 이 일을 하게 되었냐고요? 하~ 벌써 가물가물한데…\n할머니가, 앞으로 여기서 일하라고 말씀하셔서 보내졌던 것 같네요. 뭐, 그 외에 별달리 이유가 있겠어요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=smalltalk_10605_4].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Are you wondering how I ended up in this job? Haah~ It feels like ages ago...\nI think my grandmother sent me here, telling me to work here from now on. Well, what other reason could there be?
   PL:
328. [Kwestia głosowa [smalltalk_10605_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=smalltalk_10605_5].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Kwestia głosowa [smalltalk_10605_5] (Post-Uptie Chat 2)] 당신한테만 알려드릴게요… 사실, 여기 높으신 분이 저희 집안 분들이랑 친분이 있으시대요!\n후후, 세간에서 말하는 낙하산이라는 게 이런 걸까요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=smalltalk_10605_5].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Here's a secret... Truth is, one of the higher-ups here is acquainted with my family!\nHuhu, is that what they call nepotism, I wonder?
   PL:
330. [Kwestia głosowa [neglect_10605_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=neglect_10605_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Kwestia głosowa [neglect_10605_1] (Idle)] 말동무는 더 해주시지 않는 건가요? 아쉽네요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=neglect_10605_1].dlg
   limit: do 120 znaków
   EN: You won't talk with me any longer? What a shame~
   PL:
332. [Kwestia głosowa [gacksung_10605_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=gacksung_10605_1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [Kwestia głosowa [gacksung_10605_1] (Uptying)] 투입… 인가요? 앞으로 더 많이 부르시겠다고요? 잘됐다~ 너무 심심했거든요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=gacksung_10605_1].dlg
   limit: do 160 znaków
   EN: Is it a... deployment order? You'll be calling me more often in the future? That's wonderful~ I've been terribly bored.
   PL:
334. [Kwestia głosowa [formation_10605_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=formation_10605_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Kwestia głosowa [formation_10605_1] (Deployment)] 언제든지요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=formation_10605_1].dlg
   limit: do 120 znaków
   EN: I'm ready anytime.
   PL:
336. [Kwestia głosowa [battleentry_10605_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battleentry_10605_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Kwestia głosowa [battleentry_10605_1] (Stage Entry)] 투입합니다.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battleentry_10605_1].dlg
   limit: do 120 znaków
   EN: Going in.
   PL:
338. [Kwestia głosowa [battle_select_10605_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_select_10605_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Kwestia głosowa [battle_select_10605_1] (Viewed in Battle)] 바쁜데~ 특별히 들어드릴게요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_select_10605_1].dlg
   limit: do 120 znaków
   EN: I'm busy right now~ But I'll make time to hear what you say.
   PL:
340. [Kwestia głosowa [battle_endcommand_10605_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_endcommand_10605_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Kwestia głosowa [battle_endcommand_10605_1] (Commencing Attack)] 적출할게요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_endcommand_10605_1].dlg
   limit: do 120 znaków
   EN: Excising now.
   PL:
342. [Kwestia głosowa [battle_enemy_break_10605_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_enemy_break_10605_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Kwestia głosowa [battle_enemy_break_10605_1] (Enemy Stagger)] 다시 복구하긴 힘들 걸요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_enemy_break_10605_1].dlg
   limit: do 120 znaków
   EN: That'll be hard to recover from.
   PL:
344. [Kwestia głosowa [battle_break_10605_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_break_10605_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Kwestia głosowa [battle_break_10605_1] (Staggered)] 아이쿠.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_break_10605_1].dlg
   limit: do 120 znaków
   EN: Oh dear.
   PL:
346. [Kwestia głosowa [battle_kill_10605_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_kill_10605_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [Kwestia głosowa [battle_kill_10605_1] (Enemy Killed)] 완전히 녹아내렸네?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_kill_10605_1].dlg
   limit: do 120 znaków
   EN: Melted into a puddle, have you?
   PL:
348. [Kwestia głosowa [battle_dead_10605_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_dead_10605_1].desc
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [Kwestia głosowa [battle_dead_10605_1] (Death)] 어라… 결국… 앰플이… 과주입된 건… 가?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_dead_10605_1].dlg
   limit: do 120 znaków
   EN: Oh my... Have I... overdosed... on the ampule...?
   PL:
350. [Kwestia głosowa [choice_success_p_10605_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=choice_success_p_10605_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Kwestia głosowa [choice_success_p_10605_2] (Check Passed)] 후후, 금방이죠.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=choice_success_p_10605_2].dlg
   limit: do 120 znaków
   EN: Huhu, it took no time at all.
   PL:
352. [Kwestia głosowa [choice_fail_n_10605_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=choice_fail_n_10605_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Kwestia głosowa [choice_fail_n_10605_1] (Check Failed)] 음… 적출직이 원래 이런 걸 하는 직책은 아니잖아요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=choice_fail_n_10605_1].dlg
   limit: do 120 znaków
   EN: Mm... It's not like this is what excision staff usually does, yes?
   PL:
354. [Kwestia głosowa [battle_clear_10605_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_clear_10605_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Kwestia głosowa [battle_clear_10605_1] (Victory Cry)] 하아~ 간만에 바깥 공기, 좋았어요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_clear_10605_1].dlg
   limit: do 120 znaków
   EN: Haah~ It was nice to breathe fresh air for the first time in a while.
   PL:
356. [Kwestia głosowa [battle_clear_ex_10605_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_clear_ex_10605_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [Kwestia głosowa [battle_clear_ex_10605_1] (Extra Conditions Fulfilled)] 후후, 제가 봐도 훌륭했네요. 잠깐 자유시간 좀 갖고 돌아가면 안되려나요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_clear_ex_10605_1].dlg
   limit: do 120 znaków
   EN: Huhu, that was excellent if I say so myself. Can I have a little free time before we return?
   PL:
358. [Kwestia głosowa [battle_defeat_10605_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_defeat_10605_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Kwestia głosowa [battle_defeat_10605_1] (Defeat Wail)] 이런… 아무래도 증원을 불렀어야 했나봐요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Kcorp_10605.json :: dataList[id=battle_defeat_10605_1].dlg
   limit: do 120 znaków
   EN: Oh dear... I suppose we should've called reinforcements.
   PL:

## [00] W Corp. L2 Cleanup Agent — Hong Lu — W사 2등급 정리 요원
- ID Tożsamości: `10606` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 3–5 / 4–5 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture, Charge

360. [Karta Tożsamości — tytuł] W사 2등급\n정리 요원
   źródło: Personalities.json :: dataList[id=10606].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L2\nCleanup Agent
   PL:
361. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10606].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10606].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Karta Tożsamości — opis] 홍루의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10606].desc
   limit: do 120 znaków
   EN: Hong Lu’s 6th Identity
   PL:
364. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 에너지 순환
   źródło: Skills_personality-06.json :: dataList[id=1060601].levelList[level=1].name ; dataList[id=1060601].levelList[level=2].name ; dataList[id=1060601].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Energy Cycle
   PL:
365. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1060601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Charge Count
   PL:
366. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1060601].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1060601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +1 Charge Count
   PL:
367. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1060601].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1060601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 충전 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1060601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +3 Charge Count
   PL:
369. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 4 증가
   źródło: Skills_personality-06.json :: dataList[id=1060601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +4 Charge Count
   PL:
370. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 정리 지원
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=1].name ; dataList[id=1060602].levelList[level=2].name ; dataList[id=1060602].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 6 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Cleanup Support
   PL:
371. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 2 증가\n자신에게 보호막이 있을 때 합 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Charge Count\nClash Power +1 when Shielded
   PL:
372. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신의 충전 횟수가 10 이상이면, 다음 턴에 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 2를 얻음
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] At 10+ Charge Count, gain 2 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> next turn
   PL:
373. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WhenUse] 자신의 충전 횟수 3 증가\n자신에게 보호막이 있을 때 합 위력 +2
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=2].desc ; dataList[id=1060602].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +3 Charge Count\nClash Power +2 when Shielded
   PL:
374. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +3 Charge Count
   PL:
375. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수가 10 이상이면, 다음 턴에 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 2를 얻음
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Charge Count, gain 2 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> next turn
   PL:
376. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수가 5 이상이면, 다음 턴에 충전 횟수 5 당 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 1을 얻음 (최대 4)
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 5+ Charge Count, gain 1 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> for every 5 Charge Count next turn (Max 4)
   PL:
377. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 충전 역장 전개
   źródło: Skills_personality-06.json :: dataList[id=1060603].levelList[level=3].name ; dataList[id=1060603].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Deploy Charge Barrier
   PL:
378. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] [WhenUse] 자신의 충전 횟수가 10 이상이면, 충전 횟수를 전부 소모하여 자신을 포함하여 현재 체력 비율이 낮은 아군 2명에게 (소모한 충전 횟수/2)만큼 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 부여 (소수점 버림)
   źródło: Skills_personality-06.json :: dataList[id=1060603].levelList[level=3].desc ; dataList[id=1060603].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At 10+ Charge Count, consume all Charge Count to apply (Consumed Charge Count / 2) <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> (Rounded Down) to 2 allies with the lowest HP percentage
   PL:
379. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_personality-06.json :: dataList[id=1060603].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture
   PL:
380. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 2를 얻음
   źródło: Skills_personality-06.json :: dataList[id=1060603].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1060603].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> next turn
   PL:
381. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills_personality-06.json :: dataList[id=1060603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Rupture
   PL:
382. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-06.json :: dataList[id=1060604].levelList[level=1].name ; dataList[id=1060604].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+6)
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Obrona (ulepszenie 1) — opis] [WhenUse] <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 2를 얻음 (턴 당 최대 3회)
   źródło: Skills_personality-06.json :: dataList[id=1060604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> (3 times per turn)
   PL:
384. [Obrona (ulepszenie 4) — opis] [WhenUse] <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> <style="highlight">3</style>을 얻음 (턴 당 최대 3회)
   źródło: Skills_personality-06.json :: dataList[id=1060604].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, <style="highlight">, </style>, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain <style="highlight">3</style> <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> (3 times per turn)
   PL:
385. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — nazwa] 익숙해진 정리 업무
   źródło: Passives.json :: dataList[id=1060601].name
   limit: do 40 znaków
   EN: Cleanup Mastery
   PL:
386. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — opis] 전투 시작 시 충전 횟수가 5 이상 있으면, 다음 턴에 신속 2를 얻음
   źródło: Passives.json :: dataList[id=1060601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: If at 5+ Charge Count at the start of the combat phase, gain 2 [Agility] next turn
   PL:
387. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — nazwa] 열차 정리 매뉴얼 전달
   źródło: Passives.json :: dataList[id=1060621].name
   limit: do 40 znaków
   EN: Train Cleanup Manual
   PL:
388. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — opis] 속도가 가장 느린 아군이 전투 시작 시 충전 횟수가 5 이상 있으면, 다음 턴에 신속 2를 얻음
   źródło: Passives.json :: dataList[id=1060621].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: An ally with the slowest Speed gains 2 [Agility] next turn if at 5+ Charge Count at the start of the combat phase
   PL:
389. [Kwestia głosowa [get_10606_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=get_10606_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Kwestia głosowa [get_10606_1] (Identity Acquisition)] 워프 열차라는 거, 생각보다 좁던데요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=get_10606_1].dlg
   limit: do 120 znaków
   EN: Those WARP trains tend to be rather cramped, don't you think?
   PL:
391. [Kwestia głosowa [lobby_morning_10606_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=lobby_morning_10606_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Kwestia głosowa [lobby_morning_10606_1] (Morning Greeting)] 아침에 눈을 뜨는 건 어렵지 않지만… 매번 똑같은 업무를 다시 할 생각을 하니, 조금 지루하긴 하네요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=lobby_morning_10606_1].dlg
   limit: do 150 znaków
   EN: I don't have much trouble getting up in the morning... But doing the same work day after day got old pretty fast.
   PL:
393. [Kwestia głosowa [lobby_noon_10606_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=lobby_noon_10606_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Kwestia głosowa [lobby_noon_10606_1] (Afternoon Greeting)] 음~ 바깥 날씨 좋더라고요! 이 가게 음료도 맛있네요. …저는 다시 열차 청소 준비하러 돌아가야 하지만.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=lobby_noon_10606_1].dlg
   limit: do 200 znaków
   EN: Mmm~ It's nice out today! The shop I visited serves great drinks, too. ... I'm gonna have to go back inside and prepare to clean up more trains, though.
   PL:
395. [Kwestia głosowa [lobby_night_10606_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=lobby_night_10606_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Kwestia głosowa [lobby_night_10606_1] (Evening Greeting)] 야간 열차도 꽤 있다보니까, 일하다보면 지금이 밤인 줄도 모를 때가 있다니까요? 플랫폼은 항상 밝으니까요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=lobby_night_10606_1].dlg
   limit: do 180 znaków
   EN: You know, sometimes I lose track of time working late into the night for those night trains. Train platforms always so brightly lit and all.
   PL:
397. [Kwestia głosowa [smalltalk_10606_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=smalltalk_10606_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Kwestia głosowa [smalltalk_10606_1] (Chatter #1)] 이 쪽에서 일하라는 할머니 말씀 때문에 오기는 했지만, 거기서 거기인 일을 하니, 지겹긴 하네요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=smalltalk_10606_1].dlg
   limit: do 130 znaków
   EN: Grandma told me to work here, but it does get a little boring doing the same things over and over~
   PL:
399. [Kwestia głosowa [smalltalk_10606_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=smalltalk_10606_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Kwestia głosowa [smalltalk_10606_2] (Chatter #2)] 으음~ 여행 같은 건 안 보내주려나요? 명색이 열차 정리 요원인데. 아! 그렇다고 워프 열차를 타고 싶다는 건 아니구요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=smalltalk_10606_2].dlg
   limit: do 220 znaków
   EN: I wonder if we'll ever get company sponsored trips? We're train cleaner agents, so it would be pretty appropriate. Oh, not that I want to take the WARP trains, of course~
   PL:
401. [Kwestia głosowa [smalltalk_10606_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=smalltalk_10606_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Kwestia głosowa [smalltalk_10606_3] (Chatter #3)] 아~ 다른 분들은 왜 점점 말 수가 적어지실까요? 표정도 처음보다 굳었고… 감기라도 걸리신 걸까요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=smalltalk_10606_3].dlg
   limit: do 160 znaków
   EN: Aw~ Everyone's been getting increasingly quiet. Their faces look gloomy, too... I wonder if there's a flu going around?
   PL:
403. [Kwestia głosowa [smalltalk_10606_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=smalltalk_10606_4].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Kwestia głosowa [smalltalk_10606_4] (Post-Uptie Chat 1)] 어휴… 이번에도 한가득 조각나있네요. 운이 좋을 때는~ 승객들이 다툼 하나 없이 그 자리에서 기도만 올리고 있었을 때도 있었다던데. 그러면 정말 수월했을지도요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=smalltalk_10606_4].dlg
   limit: do 230 znaków
   EN: Whew... Everyone's in pieces again. Apparently there was this one time when the passengers were praying in their seats, all nice and gentle. What an easy job that must've been!
   PL:
405. [Kwestia głosowa [smalltalk_10606_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=smalltalk_10606_5].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Kwestia głosowa [smalltalk_10606_5] (Post-Uptie Chat 2)] 열차 정리하는 게 힘들지는 않냐고요? 뭐… 가끔씩 이상해진 승객들을 정리하는 건 수고가 들긴 하지만요.\n아, 정신적으로요? 음… 그냥 일인데요, 뭐. 별 생각 없답니다?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=smalltalk_10606_5].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Is the train cleaning job difficult? Well... it can be, when it comes to cleaning up the weirder passengers.\nOh, you meant like psychologically? Hm... Nah, it's just a job, right? I don't really think about it.
   PL:
407. [Kwestia głosowa [neglect_10606_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=neglect_10606_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Kwestia głosowa [neglect_10606_1] (Idle)] 음~ 잠깐 집에서 온 편지 좀 확인하고 있을게요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=neglect_10606_1].dlg
   limit: do 120 znaków
   EN: Mm, I'll be checking the letters from my family, if you won't mind~
   PL:
409. [Kwestia głosowa [gacksung_10606_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=gacksung_10606_1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Kwestia głosowa [gacksung_10606_1] (Uptying)] 아~ 새로운 교육인가요? 음, 뭔가 안 해본 일거리가 생기면 좋겠는데요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=gacksung_10606_1].dlg
   limit: do 120 znaków
   EN: Oh, is this a new lesson? I hope it's about something new for once~
   PL:
411. [Kwestia głosowa [formation_10606_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=formation_10606_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Kwestia głosowa [formation_10606_1] (Deployment)] 청소 준비 완료~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=formation_10606_1].dlg
   limit: do 120 znaków
   EN: I'm all ready to clean~
   PL:
413. [Kwestia głosowa [battleentry_10606_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battleentry_10606_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Kwestia głosowa [battleentry_10606_1] (Stage Entry)] 정리 작업, 시작합니다.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battleentry_10606_1].dlg
   limit: do 120 znaków
   EN: Time to start cleaning.
   PL:
415. [Kwestia głosowa [battle_select_10606_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_select_10606_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Kwestia głosowa [battle_select_10606_1] (Viewed in Battle)] 오~ 일할 때 오시면 안되는데.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_select_10606_1].dlg
   limit: do 120 znaków
   EN: Oh dear~ You're not supposed to come in while we're cleaning up.
   PL:
417. [Kwestia głosowa [battle_endcommand_10606_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_endcommand_10606_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Kwestia głosowa [battle_endcommand_10606_1] (Commencing Attack)] 이상 승객을 정리합니다.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_endcommand_10606_1].dlg
   limit: do 120 znaków
   EN: Taking care of problem passengers.
   PL:
419. [Kwestia głosowa [battle_enemy_break_10606_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_enemy_break_10606_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Kwestia głosowa [battle_enemy_break_10606_1] (Enemy Stagger)] 자, 진정하세요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_enemy_break_10606_1].dlg
   limit: do 120 znaków
   EN: Stay calm and stay down, now~
   PL:
421. [Kwestia głosowa [battle_break_10606_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_break_10606_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Kwestia głosowa [battle_break_10606_1] (Staggered)] 어쿠!
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_break_10606_1].dlg
   limit: do 120 znaków
   EN: Ouch!
   PL:
423. [Kwestia głosowa [battle_kill_10606_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_kill_10606_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Kwestia głosowa [battle_kill_10606_1] (Enemy Killed)] 자, 이분은 이쪽으로 모으고~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_kill_10606_1].dlg
   limit: do 120 znaków
   EN: Okay, let's get their limbs and torsos over here~
   PL:
425. [Kwestia głosowa [battle_dead_10606_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_dead_10606_1].desc
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Kwestia głosowa [battle_dead_10606_1] (Death)] 아… 간단한… 정리 작업이었는데…?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_dead_10606_1].dlg
   limit: do 120 znaków
   EN: Ah... It was... supposed to be a simple cleanup...?
   PL:
427. [Kwestia głosowa [choice_success_p_10606_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=choice_success_p_10606_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Kwestia głosowa [choice_success_p_10606_2] (Check Passed)] 흐흠. 간단하죠.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=choice_success_p_10606_2].dlg
   limit: do 120 znaków
   EN: Hmhmm. That was simple.
   PL:
429. [Kwestia głosowa [choice_fail_n_10606_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=choice_fail_n_10606_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Kwestia głosowa [choice_fail_n_10606_1] (Check Failed)] 어… 매뉴얼에는 이렇게 하라던데.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=choice_fail_n_10606_1].dlg
   limit: do 120 znaków
   EN: Strange... The manuals taught me to do it this way.
   PL:
431. [Kwestia głosowa [battle_clear_10606_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_clear_10606_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Kwestia głosowa [battle_clear_10606_1] (Victory Cry)] 자, 끝마쳤네요. 잠깐 카페 좀 다녀와야겠어요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_clear_10606_1].dlg
   limit: do 120 znaków
   EN: Alright, now that that's over with, I should visit a café for a short break.
   PL:
433. [Kwestia głosowa [battle_clear_ex_10606_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_clear_ex_10606_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Kwestia głosowa [battle_clear_ex_10606_1] (Extra Conditions Fulfilled)] 오~ 오늘은 평소보다 훨씬 빨리 끝난 것 같은데요? 청소에 소질이 있을지도~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_clear_ex_10606_1].dlg
   limit: do 150 znaków
   EN: Ohh~ We've finished today's job much faster than usual, haven't we? Maybe you have the makings of a cleanup agent~
   PL:
435. [Kwestia głosowa [battle_defeat_10606_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_defeat_10606_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Kwestia głosowa [battle_defeat_10606_1] (Defeat Wail)] 이번엔 승객 분들이 좀 과하게 날뛰셨네요…
   źródło: PersonalityVoiceDlg/Voice_Honglu_Wcorp_10606.json :: dataList[id=battle_defeat_10606_1].dlg
   limit: do 120 znaków
   EN: The passengers were a little too rowdy this time...
   PL:

## [00] Hook Office Fixer — Hong Lu — 갈고리 사무소 해결사
- ID Tożsamości: `10607` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: wydarzenie 9101 · HP bazowe: 69 · szybkość: 2–6 / 2–7 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed

437. [Karta Tożsamości — tytuł] 갈고리 사무소\n해결사
   źródło: Personalities.json :: dataList[id=10607].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hook Office\nFixer
   PL:
438. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10607].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10607].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Karta Tożsamości — opis] 홍루의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10607].desc
   limit: do 120 znaków
   EN: Hong Lu's 7th Identity
   PL:
441. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 추적
   źródło: Skills_personality-06.json :: dataList[id=1060701].levelList[level=1].name ; dataList[id=1060701].levelList[level=2].name ; dataList[id=1060701].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Track
   PL:
442. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1060701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL:
443. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1060701].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1060701].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1060701].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Bleed Count
   PL:
444. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1060701].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 신속 이 2 이상이면, 최종 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1060701].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 2+ Haste, Final Power +1
   PL:
446. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 먼저 간다
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=1].name ; dataList[id=1060702].levelList[level=2].name ; dataList[id=1060702].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Goin' First
   PL:
447. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 신속 1을 얻음
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Haste next turn
   PL:
448. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1060702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1060702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신이 대상보다 속도가 높은 경우, 자신과 대상의 속도 차이만큼 출혈 횟수 증가 (최대 2)
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If this unit is faster than the target, inflict Bleed Count equal to their Speed difference (Max 2)
   PL:
451. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 신속 2를 얻음
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Haste next turn
   PL:
452. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신이 대상보다 속도가 높은 경우, 자신과 대상의 속도 차이만큼 출혈 횟수 증가 (최대 3)
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If this unit is faster than the target, inflict Bleed Count equal to their Speed difference (Max 3)
   PL:
453. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 속도가 6 이상이면, 코인 위력 +1\n[WhenUse] 다음 턴에 신속 2를 얻음
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: At 6+ Speed, Coin Power +1\n[WhenUse] Gain 2 Haste next turn
   PL:
454. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신이 대상보다 속도가 높은 경우, 자신과 대상의 속도 차이만큼 출혈 횟수 증가 (최대 4)
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If this unit is faster than the target, inflict Bleed Count equal to their Speed difference (Max 4)
   PL:
455. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 광란
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=3].name ; dataList[id=1060703].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Rampage
   PL:
456. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 8 이상이면, 코인 위력 +1\n대상의 잃은 체력에 비례하여 피해량이 증가함. (대상의 잃은 체력 1% 당 피해량 0.3% 증가)
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 8+ Speed, Coin Power +1\nDeal more damage based on target's missing HP (+0.3% damage per 1% missing HP)
   PL:
457. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 대상의 출혈 1당 정신력 1 회복 (최대 5)
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal 1 SP per Bleed on target (Max 5)
   PL:
458. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 속도가 6 이상이면, 코인 위력 +1\n대상의 잃은 체력에 비례하여 피해량이 증가함. (대상의 잃은 체력 1% 당 피해량 0.5% 증가)
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 6+ Speed, Coin Power +1\nDeal more damage based on target's missing HP (+0.5% damage per 1% missing HP)
   PL:
461. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 대상의 출혈 1당 정신력 1 회복 (최대 10)
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal 1 SP per Bleed on target (Max 10)
   PL:
462. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Obrona (ulepszenia 1,4) — nazwa] 재빠름
   źródło: Skills_personality-06.json :: dataList[id=1060704].levelList[level=1].name ; dataList[id=1060704].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 3 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Quickness
   PL:
465. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 신속 1을 얻음 (턴 당 최대 3회)
   źródło: Skills_personality-06.json :: dataList[id=1060704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Gain 1 Haste next turn (3 times per turn)
   PL:
466. [Obrona (ulepszenie 4) — opis] 대상의 출혈 이 7 이상이면 코인 위력 +2\n[OnSucceedEvade] 다음 턴에 신속 1을 얻음 (턴 당 최대 3회)
   źródło: Skills_personality-06.json :: dataList[id=1060704].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: If target has 7+ Bleed, gain +2 Coin Power\n[OnSucceedEvade] Gain 1 Haste next turn (3 times per turn)
   PL:
467. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Lust) — nazwa] 갈고리
   źródło: Passives.json :: dataList[id=1060701].name
   limit: do 40 znaków
   EN: Hook
   PL:
468. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Lust) — opis] 적 처치 시 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 최대 1회)
   źródło: Passives.json :: dataList[id=1060701].desc
   limit: do 120 znaków
   EN: Upon defeating an enemy, gain 1 Attack Power Up next turn (Once per turn)
   PL:
469. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — nazwa] 보급형 생체 장비
   źródło: Passives.json :: dataList[id=1060721].name
   limit: do 40 znaków
   EN: Mass-produced Bionic Gear
   PL:
470. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — opis] 속도가 가장 빠른 아군 1명이 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>이 부여된 적 처치 시 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 최대 1회)
   źródło: Passives.json :: dataList[id=1060721].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>
   EN: When 1 ally with the fastest Speed defeats an enemy that has <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u>, gain 1 Attack Power Up next turn (Once per turn)
   PL:
471. [Kwestia głosowa [get_10607_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=get_10607_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Kwestia głosowa [get_10607_1] (Identity Acquisition)] 와~ 이 사무소에서는 아무렇지 않게 사람을 죽여도 칭찬받는 거죠?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=get_10607_1].dlg
   limit: do 120 znaków
   EN: Wow~ We can just kill people left and right and get praised in this Office?
   PL:
473. [Kwestia głosowa [lobby_morning_10607_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=lobby_morning_10607_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Kwestia głosowa [lobby_morning_10607_1] (Morning Greeting)] 따뜻한 곳에서 아침밥을 먹을 수 있는 것도 참 오랜만이예요~  매번 길바닥 신세였는데.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=lobby_morning_10607_1].dlg
   limit: do 140 znaków
   EN: It's been a while since I had breakfast without trembling in the cold~ I'm used to eating in the streets.
   PL:
475. [Kwestia głosowa [lobby_noon_10607_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=lobby_noon_10607_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Kwestia głosowa [lobby_noon_10607_1] (Afternoon Greeting)] 이런이런~ 어제 사람을 너무 많이 찢어서 근육통이 와버렸지 뭐예요~ 남이 날뛰는 꼴을 보면 같이 들떠버리는 버릇도 고쳐야 하는데.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=lobby_noon_10607_1].dlg
   limit: do 200 znaków
   EN: My my~ I think I gave myself muscle cramps pulling so many people apart yesterday~ I should really stop getting swept up in other people's excitements.
   PL:
477. [Kwestia głosowa [lobby_night_10607_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=lobby_night_10607_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Kwestia głosowa [lobby_night_10607_1] (Evening Greeting)] 해가 지면 참 좋아요. 일할 때도 좋고~ 으슥할 때 깜짝 놀라게 하는 것도 재밌고. 뒷골목의 밤때까지만 아니라면, 뒷골목에서 제일 재밌는 시간이예요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=lobby_night_10607_1].dlg
   limit: do 280 znaków
   EN: I love these dark hours of the day. Not only is it good for my line of work, but it's also fun creeping people out in the shadows~ It's the most entertaining time of day, except during the Night in the Backstreets.
   PL:
479. [Kwestia głosowa [smalltalk_10607_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=smalltalk_10607_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Kwestia głosowa [smalltalk_10607_1] (Chatter #1)] 대표라는 사람도 사람이 참 좋죠. 저희 같은 살인조직 출신 사람들을 주워주고. 저희가 생각이나 했겠나요, 해결사로 일하게 될줄?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=smalltalk_10607_1].dlg
   limit: do 200 znaków
   EN: What a nice guy our representative is, picking up people from killer Syndicates like ours. I never imagined that people like us would be working as Fixers!
   PL:
481. [Kwestia głosowa [smalltalk_10607_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=smalltalk_10607_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Kwestia głosowa [smalltalk_10607_2] (Chatter #2)] 갈고리 사무소… 음, 여기 오래 있지는 못할지도 모르겠어요. 당장 갈 길도 멀어 보이고. 사무소라는게 우후죽순 생기는 만큼 갑자기 문을 닫는 경우도 많다잖아요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=smalltalk_10607_2].dlg
   limit: do 290 znaków
   EN: The Hook Office... Hm. I don't know how long I'll be working here. It's still got a long way to go... But you know how Offices can be. As easy as they are to start, it's just as easy for them to shut down without a warning.
   PL:
483. [Kwestia głosowa [smalltalk_10607_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=smalltalk_10607_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Kwestia głosowa [smalltalk_10607_3] (Chatter #3)] 사무소 이름은 그렇게 기억에 남지는 않는 것 같아요. 소속을 밝혀도 다들 기억을 잘 못한단 말이죠?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=smalltalk_10607_3].dlg
   limit: do 160 znaków
   EN: I don't think our Office name is very memorable. Even when I introduce myself, it rarely seems to ring a bell in people...?
   PL:
485. [Kwestia głosowa [smalltalk_10607_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=smalltalk_10607_4].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Kwestia głosowa [smalltalk_10607_4] (Post-Uptie Chat 1)] 음, 음. 나긋하게 말하지는 말아요. 살짝 기분이 나쁘거든요. 더 아프게 죽일지도 모르잖아요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=smalltalk_10607_4].dlg
   limit: do 150 znaków
   EN: Hm, hm. Don't talk softly like that. It's a little... irritating. Let's not make your death even more painful, hm?
   PL:
487. [Kwestia głosowa [smalltalk_10607_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=smalltalk_10607_5].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Kwestia głosowa [smalltalk_10607_5] (Post-Uptie Chat 2)] 이 공방에서 만든 생체 장비… 진짜 쓰기 편해요. 다른 생체 무기보다 부착도 간편하다하고요. 진짜 내 팔 다리 처럼 움직여 준단 말이죠. 썰고, 찢고, 장식하기 좋게 꾸미기에도 쓸모가 많아요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=smalltalk_10607_5].dlg
   limit: do 260 znaków
   EN: This bionic gear from that Workshop is really handy. Apparently it's easier to equip than others, too. And they move just like my very own limbs. Ripping, tearing, decorating... It's got a lot of uses~
   PL:
489. [Kwestia głosowa [neglect_10607_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=neglect_10607_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Kwestia głosowa [neglect_10607_1] (Idle)] 음~ 또 안 불러주네. 일거리가 그렇게 없나.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=neglect_10607_1].dlg
   limit: do 120 znaków
   EN: Mm~ Downtime again. Do they really have that little work to give us?
   PL:
491. [Kwestia głosowa [gacksung_10607_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=gacksung_10607_1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Kwestia głosowa [gacksung_10607_1] (Uptying)] 일을 잘 하기는 했죠~ 일거리를 조금만 더 많이 가져다 주시면, 더 활약해드릴 수 있는데. 해주실 거죠?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=gacksung_10607_1].dlg
   limit: do 150 znaków
   EN: I agree, I did good work~ Just bring me some more, and I'll show you what I'm really made of. You will, right?
   PL:
493. [Kwestia głosowa [formation_10607_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=formation_10607_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Kwestia głosowa [formation_10607_1] (Deployment)] 의뢰가 들어 왔나요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=formation_10607_1].dlg
   limit: do 120 znaków
   EN: Do we have a contract?
   PL:
495. [Kwestia głosowa [battleentry_10607_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battleentry_10607_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Kwestia głosowa [battleentry_10607_1] (Stage Entry)] 오늘은, 얼마나 찢을까?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battleentry_10607_1].dlg
   limit: do 120 znaków
   EN: How much shall I rip and tear today?
   PL:
497. [Kwestia głosowa [battle_select_10607_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_select_10607_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Kwestia głosowa [battle_select_10607_1] (Viewed in Battle)] 아, 이런 식으로 잘 보이게 걸어두는 거 아녜요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_select_10607_1].dlg
   limit: do 120 znaków
   EN: Ah, I wasn't supposed to hang them up like that?
   PL:
499. [Kwestia głosowa [battle_endcommand_10607_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_endcommand_10607_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Kwestia głosowa [battle_endcommand_10607_1] (Commencing Attack)] 이리로… 와!
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_endcommand_10607_1].dlg
   limit: do 120 znaków
   EN: Get over... here!
   PL:
501. [Kwestia głosowa [battle_enemy_break_10607_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_enemy_break_10607_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Kwestia głosowa [battle_enemy_break_10607_1] (Enemy Stagger)] 음~ 귀찮게 끌지 말지.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_enemy_break_10607_1].dlg
   limit: do 120 znaków
   EN: Hmm~ No point dragging on.
   PL:
503. [Kwestia głosowa [battle_break_10607_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_break_10607_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Kwestia głosowa [battle_break_10607_1] (Staggered)] 어라…
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_break_10607_1].dlg
   limit: do 120 znaków
   EN: Uh oh...
   PL:
505. [Kwestia głosowa [battle_kill_10607_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_kill_10607_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Kwestia głosowa [battle_kill_10607_1] (Enemy Killed)] 빨리 해치우고 그냥 가죠?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_kill_10607_1].dlg
   limit: do 120 znaków
   EN: Let's get this over with, okay?
   PL:
507. [Kwestia głosowa [battle_dead_10607_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_dead_10607_1].desc
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Kwestia głosowa [battle_dead_10607_1] (Death)] 어… 제 행동이… 읽혔… 었나요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_dead_10607_1].dlg
   limit: do 120 znaków
   EN: Oh... they were... predicting my moves...
   PL:
509. [Kwestia głosowa [choice_success_p_10607_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=choice_success_p_10607_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Kwestia głosowa [choice_success_p_10607_2] (Check Passed)] 흠, 쉽네. 먼저 갈게요!
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=choice_success_p_10607_2].dlg
   limit: do 120 znaków
   EN: Hm, that was easy. I'm leavin' first!
   PL:
511. [Kwestia głosowa [choice_fail_n_10607_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=choice_fail_n_10607_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Kwestia głosowa [choice_fail_n_10607_1] (Check Failed)] 이런 거 말고, 잘하는 걸 시키라고요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=choice_fail_n_10607_1].dlg
   limit: do 120 znaków
   EN: Give me something I'm good at. Not something like this.
   PL:
513. [Kwestia głosowa [battle_clear_10607_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_clear_10607_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Kwestia głosowa [battle_clear_10607_1] (Victory Cry)] 재미 없었네요, 그다지 강한 놈들도 아니고…
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_clear_10607_1].dlg
   limit: do 120 znaków
   EN: I didn't enjoy that. They couldn't hold out long enough for me.
   PL:
515. [Kwestia głosowa [battle_clear_ex_10607_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_clear_ex_10607_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Kwestia głosowa [battle_clear_ex_10607_1] (Extra Conditions Fulfilled)] 하~ 오랜만에 발 뻗고 눕네요! 계속 이대로 돈 모아서 더 좋은 장비를 달아야겠어요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_clear_ex_10607_1].dlg
   limit: do 160 znaków
   EN: Haah~ I think I'm finally starting to straighten out my life! I should keep saving up money and buy me some better gear.
   PL:
517. [Kwestia głosowa [battle_defeat_10607_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_defeat_10607_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Kwestia głosowa [battle_defeat_10607_1] (Defeat Wail)] 네…? 해결사가 되면 오히려 사람을 더 죽이는데 제약이 생긴다고요…? 속은 거군요…
   źródło: PersonalityVoiceDlg/Voice_Honglu_Hook_10607.json :: dataList[id=battle_defeat_10607_1].dlg
   limit: do 120 znaków
   EN: What...? Fixers aren't allowed to just kill people...? So they lied to me...
   PL:

## [000] Dieci Assoc. South Section 4 — Hong Lu — 남부 디에치 협회 4과
- ID Tożsamości: `10608` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 79 · szybkość: 2–6 / 2–7 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Sinking

519. [Karta Tożsamości — tytuł] 남부 디에치 협회\n4과
   źródło: Personalities.json :: dataList[id=10608].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Dieci Assoc.\nSouth Section 4
   PL:
520. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10608].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10608].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Karta Tożsamości — opis] 홍루의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10608].desc
   limit: do 120 znaków
   EN: Hong Lu's 8th Identity
   PL:
523. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 지식 소모
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=1].name ; dataList[id=1060801].levelList[level=2].name ; dataList[id=1060801].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 5 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Expend Knowledge
   PL:
524. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots
   PL:
525. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Sinking] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1060801].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060801].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +1 [Sinking] Count
   PL:
526. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림\n[WhenUse] [KnowledgeExplored]이 3 이상이면, 합 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [KnowledgeExplored]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots\n[WhenUse] At 3+ [KnowledgeExplored], Clash Power +1
   PL:
527. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [KnowledgeExplored]이 3 이상이면, 코인 1회 재사용
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [KnowledgeExplored]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [OnSucceedAttack] At 3+ [KnowledgeExplored], reuse Coin once
   PL:
528. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림\n[WhenUse] ([KnowledgeExplored] - 1)만큼 합 위력이 증가
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [KnowledgeExplored]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots\n[WhenUse] Clash Power +([KnowledgeExplored] - 1)
   PL:
529. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] ([KnowledgeExplored] - 1)만큼 코인 재사용
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [KnowledgeExplored]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [OnSucceedAttack] Reuse Coin ([KnowledgeExplored] - 1) times
   PL:
530. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 열어 젖히기
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=1].name ; dataList[id=1060802].levelList[level=2].name ; dataList[id=1060802].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Unveil
   PL:
531. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 무작위 스킬 2개를 등급이 낮은 순으로 버림
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Randomly Discard 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots
   PL:
532. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] [Sinking] 3 부여
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 3 [Sinking]
   PL:
533. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 무작위 스킬 2개를 등급이 낮은 순으로 버림\n[WhenUse] [KnowledgeExplored]이 3 이상이면, 코인 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [KnowledgeExplored]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [WhenUse] Randomly Discard 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots\n[WhenUse] At 3+ [KnowledgeExplored], Coin Power +1
   PL:
534. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL:
535. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 무작위 스킬 2개를 등급이 낮은 순으로 버림\n[WhenUse] ([KnowledgeExplored] - 1)만큼 코인 위력이 증가
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [KnowledgeExplored]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [WhenUse] Randomly Discard 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots\n[WhenUse] Coin Power +([KnowledgeExplored] - 1)
   PL:
536. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL:
537. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 순환하는 지식
   źródło: Skills_personality-06.json :: dataList[id=1060803].levelList[level=3].name ; dataList[id=1060803].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Cyclical Knowledge
   PL:
538. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] [KnowledgeExplored]이 2 이상이면, [KnowledgeExplored] 만큼 코인 위력이 증가\n대상의 [Sinking] 1당 피해량 +1.5% (최대 15%)
   źródło: Skills_personality-06.json :: dataList[id=1060803].levelList[level=3].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] At 2+ [KnowledgeExplored], gain Coin Power equal to [KnowledgeExplored]\nDeal +1.5% damage per [Sinking] on target (Max 15%)
   PL:
539. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1060803].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
540. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [EndSkill] 대상이 흐트러짐 상태가 되거나 사망하면, 정신력 10 회복
   źródło: Skills_personality-06.json :: dataList[id=1060803].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1060803].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] If target is Staggered or defeated, heal 10 SP
   PL:
541. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] [KnowledgeExplored]이 2 이상이면, [KnowledgeExplored]만큼 코인 위력이 증가\n대상의 [Sinking] 1당 피해량 +3% (최대 30%)
   źródło: Skills_personality-06.json :: dataList[id=1060803].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] At 2+ [KnowledgeExplored], gain Coin Power equal to [KnowledgeExplored]\nDeal +3% damage per [Sinking] on target (Max 30%)
   PL:
542. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 4 증가
   źródło: Skills_personality-06.json :: dataList[id=1060803].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +4 [Sinking] Count
   PL:
543. [Obrona (ulepszenia 1,4) — nazwa] 인도하는 걸음
   źródło: Skills_personality-06.json :: dataList[id=1060804].levelList[level=1].name ; dataList[id=1060804].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Guiding Steps
   PL:
544. [Obrona (ulepszenia 1,4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 무작위 스킬 2개를 등급이 낮은 순으로 버림
   źródło: Skills_personality-06.json :: dataList[id=1060804].levelList[level=1].desc ; dataList[id=1060804].levelList[level=4].desc
   (powtórzenie elementu 531 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — nazwa] 열쇠 들여다보기
   źródło: Passives.json :: dataList[id=1060801].name
   limit: do 40 znaków
   EN: Peering Through a Key
   PL:
546. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — opis] 자신이 스킬을 버릴 때 버린 스킬의 등급만큼 [AttackDmgUp]를 얻음. (턴 당 최대 3)
   źródło: Passives.json :: dataList[id=1060801].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: When Discarding a Skill, gain [AttackDmgUp] equal to the Discarded Skill's Rank. (Max 3 per turn)
   PL:
547. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — nazwa] 열쇠 들여다보기
   źródło: Passives.json :: dataList[id=1060811].name
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — opis] 자신이 스킬을 버릴 때 버린 스킬의 등급만큼 [AttackDmgUp]를 얻음. (턴 당 최대 3)\n자신을 제외한 아군이 스킬을 버릴 때, 버린 스킬의 등급이 자신의 [KnowledgeExplored]보다 높으면, 자신의 [KnowledgeExplored] +1
   źródło: Passives.json :: dataList[id=1060811].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDmgUp], [KnowledgeExplored]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: When Discarding a Skill, gain [AttackDmgUp] equal to the Discarded Skill Rank. (Max 3 per turn)\nWhen other allies Discard a Skill, and if the ally's Discarded Skill Rank is higher than this unit's [KnowledgeExplored] value, this unit gains +1 [KnowledgeExplored].
   PL:
549. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — nazwa] 깨우침
   źródło: Passives.json :: dataList[id=1060821].name
   limit: do 40 znaków
   EN: Enlightenment
   PL:
550. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — opis] 정신력이 가장 낮은 아군 1명이 공격 종료 후 대상을 흐트러짐 상태로 만들거나, 처치하면 정신력 7 회복
   źródło: Passives.json :: dataList[id=1060821].desc
   limit: do 170 znaków
   EN: Attack End: If the target is in a staggered or defeated state by an attack from 1 ally with the least SP, the ally heals 7 SP.
   PL:
551. [Kwestia głosowa [get_10608_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=get_10608_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Kwestia głosowa [get_10608_1] (Identity Acquisition)] 으흠~ 이건 이렇게 쓰여있나 보네요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=get_10608_1].dlg
   limit: do 120 znaków
   EN: Oho~ So that's how it's written~
   PL:
553. [Kwestia głosowa [lobby_morning_10608_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=lobby_morning_10608_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Kwestia głosowa [lobby_morning_10608_1] (Morning Greeting)] 아, 오셨어요? 마침 잘 오셨어요! 제가 오전 연구회에서 뭘 알게 되었냐면요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=lobby_morning_10608_1].dlg
   limit: do 160 znaków
   EN: Ah, welcome! I'm so glad I ran into you. I just have to tell you about what I learned from the morning seminar today~
   PL:
555. [Kwestia głosowa [lobby_noon_10608_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=lobby_noon_10608_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Kwestia głosowa [lobby_noon_10608_1] (Afternoon Greeting)] 점심은 드셨나요? 제가 오늘 열어 본 책에 해보지 않았던 요리법이 적혀있었거든요~ 제가 요리해볼테니까, 한 번 드셔보시지 않을래요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=lobby_noon_10608_1].dlg
   limit: do 180 znaków
   EN: Have you had your lunch yet? I read a cooking book today and learned a new recipe~ Would you like to try some of my cooking? My treat!
   PL:
557. [Kwestia głosowa [lobby_night_10608_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=lobby_night_10608_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Kwestia głosowa [lobby_night_10608_1] (Evening Greeting)] 밤에도 공부하시는 분들이 많긴 하지만, 저는 느긋하게 쉬는 편이 더 머리에 잘 들어오더라고요~ 공부를 할 땐 분배가 중요하죠!
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=lobby_night_10608_1].dlg
   limit: do 260 znaków
   EN: I know that many of us like to study late into the night, but I prefer to take it slow~ After a nice, long rest, I can absorb the knowledge like a sponge. It's important to pace yourself when studying!
   PL:
559. [Kwestia głosowa [smalltalk_10608_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=smalltalk_10608_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Kwestia głosowa [smalltalk_10608_1] (Chatter #1)] 열쇠에 대해서 궁금하시겠죠. 음~ 어떻게 설명해야 할까요. 지식을 여는 매개체…? 힘을 담는 그릇…? 직접 써보기 전에는 뭐라 말하기 어렵기는 해요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=smalltalk_10608_1].dlg
   limit: do 240 znaków
   EN: I'm sure you would like to know more about this 'key'. Hmm~ How do I put this? It's a medium...? A vessel for knowledge...? Kinda hard to explain to someone who hasn't used it before.
   PL:
561. [Kwestia głosowa [smalltalk_10608_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=smalltalk_10608_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Kwestia głosowa [smalltalk_10608_2] (Chatter #2)] 열쇠를 통해 들여다보면 보이지 않던 것들이 들여다보여진답니다. …아! 미안해요~ 열쇠파가 아니신 분이 들여다봐도 보이는 건 없어서~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=smalltalk_10608_2].dlg
   limit: do 240 znaków
   EN: Looking at things through this key reveals things that are normally unseen. ... Ah! My bad, I should've been clearer~ It doesn't reveal anything for people that aren't part of 'the Keys'~
   PL:
563. [Kwestia głosowa [smalltalk_10608_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=smalltalk_10608_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Kwestia głosowa [smalltalk_10608_3] (Chatter #3)] 아~ 주먹파 분들도 나름의 고충이 있으시다고 들었어요. 진리를 여는 도구도 없이 협회의 일을 하시려면~ 뭐, 쉽지는 않으시겠죠.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=smalltalk_10608_3].dlg
   limit: do 230 znaków
   EN: Ah~ I did hear that the Fists have their own share of concerns. Well, I suppose it can't be easy trying to do the Association business without the tool for unlocking the truth~
   PL:
565. [Kwestia głosowa [smalltalk_10608_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=smalltalk_10608_4].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Kwestia głosowa [smalltalk_10608_4] (Post-Uptie Chat 1)] 이런, 놀라셨나요? 이 열쇠는 이런 식으로 커지기도 하고, 작아지기도 한답니다. 지식을 담는 만큼~ 강해지죠.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=smalltalk_10608_4].dlg
   limit: do 180 znaków
   EN: Oh, did I catch you off guard? My key can grow and shrink... just like this! The more knowledge you stuff into it... the stronger it gets.
   PL:
567. [Kwestia głosowa [smalltalk_10608_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=smalltalk_10608_5].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Kwestia głosowa [smalltalk_10608_5] (Post-Uptie Chat 2)] 그렇죠. 아무래도 무기를 사용하는 것이 좀 더 지성적인 방식 아닐까요? 활용하는 방법도… 주먹보다야, 많겠지요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=smalltalk_10608_5].dlg
   limit: do 240 znaków
   EN: Yes. Wouldn't you say that using a weapon would be a more... enlightened way of engaging in combat? Weapons must have more varied applications than just throwing your fists around, right?
   PL:
569. [Kwestia głosowa [neglect_10608_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=neglect_10608_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Kwestia głosowa [neglect_10608_1] (Idle)] 다음으로 읽어볼 책은…
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=neglect_10608_1].dlg
   limit: do 120 znaków
   EN: Hmm, which book should I read next...?
   PL:
571. [Kwestia głosowa [gacksung_10608_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=gacksung_10608_1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Kwestia głosowa [gacksung_10608_1] (Uptying)] 현명하신 생각이네요. 깨우칠 것이 있다면 이 열쇠로 인도해드릴게요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=gacksung_10608_1].dlg
   limit: do 120 znaków
   EN: Good thinking. Let my key be the guide to your enlightenment.
   PL:
573. [Kwestia głosowa [formation_10608_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=formation_10608_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Kwestia głosowa [formation_10608_1] (Deployment)] 열쇠가 필요하신가요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=formation_10608_1].dlg
   limit: do 120 znaków
   EN: Looking for a key?
   PL:
575. [Kwestia głosowa [battleentry_10608_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battleentry_10608_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Kwestia głosowa [battleentry_10608_1] (Stage Entry)] 진리를 열기 위해.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battleentry_10608_1].dlg
   limit: do 120 znaków
   EN: To unveil the truth.
   PL:
577. [Kwestia głosowa [battle_select_10608_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_select_10608_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Kwestia głosowa [battle_select_10608_1] (Viewed in Battle)] 네~ 듣고 있어요!
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_select_10608_1].dlg
   limit: do 120 znaków
   EN: Yep~ I'm listening!
   PL:
579. [Kwestia głosowa [battle_endcommand_10608_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_endcommand_10608_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Kwestia głosowa [battle_endcommand_10608_1] (Commencing Attack)] 어두운 무지를 열어젖히러.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_endcommand_10608_1].dlg
   limit: do 120 znaków
   EN: To bring the umbra of ignorance to light.
   PL:
581. [Kwestia głosowa [battle_enemy_break_10608_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_enemy_break_10608_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Kwestia głosowa [battle_enemy_break_10608_1] (Enemy Stagger)] 굳게 닫힌 지성을…
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_enemy_break_10608_1].dlg
   limit: do 120 znaków
   EN: The sealed intellect...
   PL:
583. [Kwestia głosowa [battle_break_10608_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_break_10608_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Kwestia głosowa [battle_break_10608_1] (Staggered)] 어쿠…
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_break_10608_1].dlg
   limit: do 120 znaków
   EN: Ouch...
   PL:
585. [Kwestia głosowa [battle_kill_10608_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_kill_10608_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Kwestia głosowa [battle_kill_10608_1] (Enemy Killed)] 밝게, 열어 젖힌다.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_kill_10608_1].dlg
   limit: do 120 znaków
   EN: ... Shall be unveiled unto the light.
   PL:
587. [Kwestia głosowa [battle_dead_10608_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_dead_10608_1].desc
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Kwestia głosowa [battle_dead_10608_1] (Death)] 음… 요리에 대한 지식은… 크게 도움이 안되었… 나.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_dead_10608_1].dlg
   limit: do 120 znaków
   EN: Um... I guess knowledge about food recipes... weren't too useful...
   PL:
589. [Kwestia głosowa [choice_success_p_10608_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=choice_success_p_10608_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Kwestia głosowa [choice_success_p_10608_2] (Check Passed)] 평소에 공부해뒀던 거네요!
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=choice_success_p_10608_2].dlg
   limit: do 120 znaków
   EN: I'm familiar with this subject!
   PL:
591. [Kwestia głosowa [choice_fail_n_10608_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=choice_fail_n_10608_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Kwestia głosowa [choice_fail_n_10608_1] (Check Failed)] 이런 건… 모르는데~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=choice_fail_n_10608_1].dlg
   limit: do 120 znaków
   EN: I've got... no idea what this is~
   PL:
593. [Kwestia głosowa [battle_clear_10608_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_clear_10608_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Kwestia głosowa [battle_clear_10608_1] (Victory Cry)] 자~ 잘 해결한 것 같네요? 어… 뭘 더 했어야 했던가요…?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_clear_10608_1].dlg
   limit: do 120 znaków
   EN: Now~ I'd say that's a task well taken care of! Uh... were you expecting something more?
   PL:
595. [Kwestia głosowa [battle_clear_ex_10608_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_clear_ex_10608_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Kwestia głosowa [battle_clear_ex_10608_1] (Extra Conditions Fulfilled)] 흐음~ 하! 개운하게 정리됐어요! 아… 머리까지 너무 개운해진 것 같은데… 뭐, 다시 공부하면 되죠!
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_clear_ex_10608_1].dlg
   limit: do 190 znaków
   EN: Phew~ hah! It's all smoothly cleaned-up! Ah... I think my brain's been smoothly cleaned-up too... Well, no worries! I can always learn them again!
   PL:
597. [Kwestia głosowa [battle_defeat_10608_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_defeat_10608_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Kwestia głosowa [battle_defeat_10608_1] (Defeat Wail)] 조금 두루두루 공부를 해야 했던 걸까요… 하나에 너무 몰입하는 건 지양해야 할지도 모르겠어요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Dieci_10608.json :: dataList[id=battle_defeat_10608_1].dlg
   limit: do 170 znaków
   EN: Mm... Maybe I should've cast a wider net when collecting my knowledge... I probably shouldn't get too immersed in a single subject.
   PL:

## [000] District 20 Yurodivy — Hong Lu — 20구 유로지비
- ID Tożsamości: `10609` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 4 · HP bazowe: 70 · szybkość: 3–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Tremor

599. [Karta Tożsamości — tytuł] 20구\n유로지비
   źródło: Personalities.json :: dataList[id=10609].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: District 20\nYurodivy
   PL:
600. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10609].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10609].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Karta Tożsamości — opis] 홍루의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10609].desc
   limit: do 120 znaków
   EN: Hong Lu's 9th Identity
   PL:
603. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 추리시작
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=1].name ; dataList[id=1060901].levelList[level=2].name ; dataList[id=1060901].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Deduction Start
   PL:
604. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=1].desc ; dataList[id=1060901].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count
   PL:
605. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Vibration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 2 [Vibration]
   PL:
606. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Gain +2 [Vibration] Count
   PL:
607. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
608. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain +2 [Vibration] Count
   PL:
609. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">자신의 [Vibration] 횟수가 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n<style="highlight">At 6+ [Vibration] Count, Coin Power +1</style>
   PL:
610. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 변형 지팡이 호신술
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=1].name ; dataList[id=1060902].levelList[level=2].name ; dataList[id=1060902].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Morph Cane Technique
   PL:
611. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count
   PL:
612. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1060902].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060902].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain +3 [Vibration] Count
   PL:
613. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 607 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]이 9 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 9+ [Vibration], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
615. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Vibration]이 8 이상이면, 합 위력 +1</style>\n[WhenUse] 자신의 [Vibration] 횟수 3 증가\n<style="highlight">자신의 [Vibration] 횟수가 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[WhenUse] If target has 8+ [Vibration], Clash Power +1</style>\n[WhenUse] Gain +3 [Vibration] Count\n<style="highlight">At 6+ [Vibration] Count, Coin Power +1</style>
   PL:
616. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration]
   PL:
617. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]이 <style="highlight">7</style> 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has <style="highlight">7</style>+ [Vibration], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
618. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Vibration]이 <style="highlight">6</style> 이상이면, 합 위력 +1\n[WhenUse] 자신의 [Vibration] 횟수 3 증가\n자신의 [Vibration] 횟수가 <style="highlight">5</style> 이상이면, 코인 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has <style="highlight">6</style>+ [Vibration], Clash Power +1\n[WhenUse] Gain +3 [Vibration] Count\nAt <style="highlight">5</style>+ [Vibration] Count, Coin Power +1
   PL:
619. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]<style="highlight"></style>
   PL:
620. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]이 <style="highlight">6</style> 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has <style="highlight">6</style>+ [Vibration], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
621. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 범인은 당신이군요!
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=3].name ; dataList[id=1060903].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 3 · monety: 4 (+3)
   limit: do 40 znaków
   EN: You're the Culprit!
   PL:
622. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 [Vibration]이 6 이상이면 합 위력 +1\n[WhenUse] 자신의 [Vibration] 횟수를 10 소모하여 코인 위력 +2
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 6+ [Vibration], Clash Power +1\n[WhenUse] Consume 10 [Vibration] Count on self to gain Coin Power +2
   PL:
623. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 스킬 사용시 [Vibration] 횟수를 소모했다면, [VibrationEcho]으로 [FusionVibration]
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1060903].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationEcho], [FusionVibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationEcho] = 진동 - 반향 / Tremor - Reverb; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: [OnSucceedAttack] If this Skill consumed [Vibration] Count on use, trigger [FusionVibration] into [VibrationEcho]
   PL:
624. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1060903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
625. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- 스킬 사용시 [Vibration] 횟수를 소모하지 못했다면, 위 효과 발동 후 자신에게 [VibrationExplosion]
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- If this unit did not consume [Vibration] Count with Skill use, activate the above effect, then trigger [VibrationExplosion] on self
   PL:
626. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 대상의 [Vibration] <style="highlight">6당</style> 합 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 <style="highlight">[Vibration] 횟수가 15 미만이면,</style> [Vibration] 횟수 10 소모하여 코인 위력 +2\n<style="highlight">[WhenUse] 자신의 [Vibration] 횟수를 15 소모하여 코인 위력 +3</style>
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=4].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Clash Power +1 for every <style="highlight">6</style> [Vibration] on target <style="highlight">(max 2)</style>\n[WhenUse] At <style="highlight"> less than 15 [Vibration] Count on self</style>, consume 10 [Vibration] Count to gain Coin Power +2\n<style="highlight">[WhenUse] Consume 15 [Vibration] Count on self to gain Coin Power +3</style>
   PL:
627. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 스킬 사용시 [Vibration] 횟수를 10 이상 소모했다면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: <style="highlight">[OnSucceedAttack] If this Skill consumed 10+ [Vibration] Count on Skill Use, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL:
628. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 스킬 사용시 [Vibration] 횟수를 10 이상 소모했다면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- 소모한 [Vibration] 횟수가 15 미만이면, 위 효과 발동 후 자신에게도 [VibrationExplosion]</style>
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: <style="highlight">[OnSucceedAttack] If this Skill consumed 10+ [Vibration] Count on Skill Use, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- If this unit consumed less than 15 [Vibration] Count, trigger [VibrationExplosion] on self after activating the above effect</style>
   PL:
629. [Obrona (ulepszenia 1,4) — nazwa] 잠깐만요?!
   źródło: Skills_personality-06.json :: dataList[id=1060904].levelList[level=1].name ; dataList[id=1060904].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Wait?!
   PL:
630. [Obrona (ulepszenie 1) — opis] [WhenUse] 대상의 [Vibration] 횟수의 2배만큼 보호막 체력을 얻음 (최대 7)
   źródło: Skills_personality-06.json :: dataList[id=1060904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain 2 x ([Vibration] Count on target) as Shield HP (max 7)
   PL:
631. [Obrona (ulepszenie 4) — opis] [WhenUse] 대상의 [Vibration] 횟수의 2배만큼 보호막 체력을 얻음 (최대 <style="highlight">13</style>)
   źródło: Skills_personality-06.json :: dataList[id=1060904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain 2 x ([Vibration] Count on target) as Shield HP (max <style="highlight">13</style>)
   PL:
632. [Pasywka bojowa (od ulepszenia 2, posiadane 6× Sloth) — nazwa] 진동유착 변형 전투 지팡이 (미허가 발명품)
   źródło: Passives.json :: dataList[id=1060901].name
   limit: do 70 znaków
   EN: Vibroweld Morph-combat Cane (Unauthorized Invention)
   PL:
633. [Pasywka bojowa (od ulepszenia 2, posiadane 6× Sloth) — opis] 턴 종료 시 이번 턴에 자신이 [VibrationExplosion]을 시킨 횟수만큼 다음 턴에 [AttackDmgUp]를 얻음 (최대 3)
   źródło: Passives.json :: dataList[id=1060901].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion], [AttackDmgUp]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn End: gain [AttackDmgUp] next turn equal to the number of times this unit triggered [VibrationExplosion] this turn (max 3)
   PL:
634. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — nazwa] 내가 범인이라면...?
   źródło: Passives.json :: dataList[id=1060921].name
   limit: do 40 znaków
   EN: In the Culprit's Shoes
   PL:
635. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — opis] 편성 순서 1번인 아군의 스킬, 코인 효과로 [VibrationExplosion] 시 25% 확률로 [VibrationExplosion]이 1회 추가로 발동 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1060921].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: When #1 Deployed Identity triggers Tremor Burst with Skill or Coin effects, 25% chance to trigger an additional Tremor Burst (once per turn)
   PL:
636. [Kwestia głosowa [get_10609_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=get_10609_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Kwestia głosowa [get_10609_1] (Identity Acquisition)] 여기가 살인 사건 현장이군요? 음~ 이런 아마추어같은 마무리를 해두고 가다니, 어지간히 시간에 쫓겼나 봐요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=get_10609_1].dlg
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: So this is the murder scene?\nHmm... What an amateurish finish... They must've been really pressed for time.
   PL:
638. [Kwestia głosowa [lobby_morning_10609_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=lobby_morning_10609_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Kwestia głosowa [lobby_morning_10609_1] (Morning Greeting)] 좋은 아침이네요~ 바깥 공기가 매캐하죠? 이 주변이 좀 그런 것 같더라고요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=lobby_morning_10609_1].dlg
   limit: do 130 znaków
   EN: Good morning~ The air's a bit smoggy today, isn't it? I guess that's just how it is around here.
   PL:
640. [Kwestia głosowa [lobby_noon_10609_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=lobby_noon_10609_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Kwestia głosowa [lobby_noon_10609_1] (Afternoon Greeting)] 해가 가장 따스하게 내리쬐는 시간이네요. 세상 모든 게 불평등하게 조여져 있지만, 적어도 햇살만큼은 공평하게 내리쬔다는 기분이 들지 않나요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=lobby_noon_10609_1].dlg
   limit: do 230 znaków
   EN: This is the hour when the sun is its warmest. Though the world is like one big machine bolted together by screws of inequality, at least the sunlight feels pretty fair, hmm?
   PL:
642. [Kwestia głosowa [lobby_night_10609_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=lobby_night_10609_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Kwestia głosowa [lobby_night_10609_1] (Evening Greeting)] …아! 당신이셨군요? 밤에는 얼굴을 잘 보이게 하고 다니셔야 해요~ 깜빡 착각하면, 재분배의 대상인 줄 착각해 버린다니까요? 하하.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=lobby_night_10609_1].dlg
   limit: do 170 znaków
   EN: ... Oh! It's you! Don't hide your face at night, okay~? I almost mistook you for someone who deserves... redistribution. Ha ha.
   PL:
644. [Kwestia głosowa [smalltalk_10609_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=smalltalk_10609_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Kwestia głosowa [smalltalk_10609_1] (Chatter #1)] 이제는 유로지비라는 단체가 워낙 넓게 퍼져버려서요. 음~ 목에 두른 이 스카프를 빼면, 사실 서로 유로지비인지 알아채기도 어려울걸요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=smalltalk_10609_1].dlg
   limit: do 200 znaków
   EN: The Yurodiviye's spread so far and wide now. Mm~ at this point, we pretty much have to resort to recognizing each other by this scarf around our necks!
   PL:
646. [Kwestia głosowa [smalltalk_10609_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=smalltalk_10609_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Kwestia głosowa [smalltalk_10609_2] (Chatter #2)] 음… 저희 단체를 너무 어렵게 보실 필요는 없어요. 둥지와 날개에 불만을 가진 사람은 도시 어디에나 있고, 그분들 중에서도~ 조금 행동력이 뛰어나신 분들이 유로지비를 찾는 것뿐이죠.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=smalltalk_10609_2].dlg
   limit: do 320 znaków
   EN: Hm... there's nothing too complicated about our organization. The City is chock-full of people unhappy about the way things are, about the way the Wings are. We're just a collective of the same-minded, unhappy people with a bit more... initiative.
   PL:
648. [Kwestia głosowa [smalltalk_10609_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=smalltalk_10609_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Kwestia głosowa [smalltalk_10609_3] (Chatter #3)] 이 단안경은 예전에 공방에서 일했던 저희 구성원 분이 고안해 낸 것이랍니다. 이렇게 레버를 돌리면… 궁금했던 현상을 더 정확하게 관찰할 수 있죠!
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=smalltalk_10609_3].dlg
   limit: do 240 znaków
   EN: This monocle was invented by one of our comrades who used to be employed at a Workshop. Look. When I rotate the dial here... I can get a better look at things that pique my curiosity!
   PL:
650. [Kwestia głosowa [smalltalk_10609_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=smalltalk_10609_4].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Kwestia głosowa [smalltalk_10609_4] (Post-Uptie Chat 1)] 자… 사건을 재구성해 볼까요. 이 부근에 나 있는 날붙이의 흔적과 혈흔의 각도. 굳어버린 진흙을 단안경에 담아보면~\n여기가 목숨이 끊기던 지점이겠군요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=smalltalk_10609_4].dlg
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All right... let's connect the threads of evidence together. This area is clearly marked by a sharp object. Look at the angle of the blood splatters. And now, the dried mud here. Let's see how they appear through my monocle...\n... Ah, this is exact spot where the victim drew his final breath.
   PL:
652. [Kwestia głosowa [smalltalk_10609_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=smalltalk_10609_5].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Kwestia głosowa [smalltalk_10609_5] (Post-Uptie Chat 2)] 이런 사건을 정리하는 데에 둥지나 날개의 개입은 반드시 막아야죠. 유로지비끼리의 일은 유로지비 안에서.\n저희끼리도 가끔 의견이 맞지 않을 때가 있으니까~ 이런 사건도 왕왕 있곤 한답니다~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=smalltalk_10609_5].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We can't involve the Nests or the Wings in this case. Whatever a Yurodivy does... stays in the Yurodiviye.\nDisagreements are inevitable, you know? Things like this are bound to happen once in a while~
   PL:
654. [Kwestia głosowa [neglect_10609_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=neglect_10609_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Kwestia głosowa [neglect_10609_1] (Idle)] 음~ 흠~ 아, 사탕이 다 녹아 버렸네…
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=neglect_10609_1].dlg
   limit: do 120 znaków
   EN: Mm~ Hm~ Ah, my lollipop's gone.
   PL:
656. [Kwestia głosowa [gacksung_10609_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=gacksung_10609_1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [Kwestia głosowa [gacksung_10609_1] (Uptying)] 자… 나를 범인이라고 생각하고… 여기서 있었던 일을 천천히 상상해보면…\n후훗, 결국 진상을 파악할 수 있겠죠?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=gacksung_10609_1].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Okay, let's think. How would I do this, if I was the killer? I just have to slowly think it through, and...\n... Hehe, I suppose I'll find the truth sooner or later, hm?
   PL:
658. [Kwestia głosowa [formation_10609_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=formation_10609_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Kwestia głosowa [formation_10609_1] (Deployment)] 흐음, 가볼까요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=formation_10609_1].dlg
   limit: do 120 znaków
   EN: Hmm, shall we get a move on?
   PL:
660. [Kwestia głosowa [battleentry_10609_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battleentry_10609_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Kwestia głosowa [battleentry_10609_1] (Stage Entry)] 사건 속으로.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battleentry_10609_1].dlg
   limit: do 120 znaków
   EN: Into the case.
   PL:
662. [Kwestia głosowa [battle_select_10609_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_select_10609_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Kwestia głosowa [battle_select_10609_1] (Viewed in Battle)] 이 사건에 궁금한 점이 생기셨나요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_select_10609_1].dlg
   limit: do 120 znaków
   EN: Is there anything you'd like to know about the case?
   PL:
664. [Kwestia głosowa [battle_endcommand_10609_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_endcommand_10609_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Kwestia głosowa [battle_endcommand_10609_1] (Commencing Attack)] 직접 타도하죠!
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_endcommand_10609_1].dlg
   limit: do 120 znaków
   EN: We'll bring them down with our own hands!
   PL:
666. [Kwestia głosowa [battle_enemy_break_10609_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_enemy_break_10609_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Kwestia głosowa [battle_enemy_break_10609_1] (Enemy Stagger)] 대의에 거스르지 말고~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_enemy_break_10609_1].dlg
   limit: do 120 znaków
   EN: Don't fight the great cause~
   PL:
668. [Kwestia głosowa [battle_break_10609_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_break_10609_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Kwestia głosowa [battle_break_10609_1] (Staggered)] 읏… 아이쿠.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_break_10609_1].dlg
   limit: do 120 znaków
   EN: Ngh… Oh dear.
   PL:
670. [Kwestia głosowa [battle_kill_10609_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_kill_10609_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Kwestia głosowa [battle_kill_10609_1] (Enemy Killed)] 편하게, 가자구요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_kill_10609_1].dlg
   limit: do 120 znaków
   EN: And make this easy for all of us, okay?
   PL:
672. [Kwestia głosowa [battle_dead_10609_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_dead_10609_1].desc
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Kwestia głosowa [battle_dead_10609_1] (Death)] 아… 결국… 저는 이렇게 침묵해 버리나요…
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_dead_10609_1].dlg
   limit: do 120 znaków
   EN: Ah... so this... is how I'm silenced...
   PL:
674. [Kwestia głosowa [choice_success_p_10609_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=choice_success_p_10609_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Kwestia głosowa [choice_success_p_10609_2] (Check Passed)] 이 렌즈 너머로는 항상 정답이 보인다구요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=choice_success_p_10609_2].dlg
   limit: do 120 znaków
   EN: The answer always reveals itself past this lens~
   PL:
676. [Kwestia głosowa [choice_fail_n_10609_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=choice_fail_n_10609_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Kwestia głosowa [choice_fail_n_10609_1] (Check Failed)] 어라라… 이게 아닌가요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=choice_fail_n_10609_1].dlg
   limit: do 120 znaków
   EN: Whoops... I guess this wasn't it?
   PL:
678. [Kwestia głosowa [battle_clear_10609_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_clear_10609_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Kwestia głosowa [battle_clear_10609_1] (Victory Cry)] 만족스러운 활동이었어요. 음~ 여기는… 이렇게 두면 나중에 저희에게 불리한 증언이 나오겠어요. 치울까요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_clear_10609_1].dlg
   limit: do 220 znaków
   EN: Ah, that was very satisfying. Mm~ You know, this mess we left behind actually looks pretty bad. It might even lead to someone testifying against us. Shall I clean it up?
   PL:
680. [Kwestia głosowa [battle_clear_ex_10609_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_clear_ex_10609_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Kwestia głosowa [battle_clear_ex_10609_1] (Extra Conditions Fulfilled)] 대의에 맞서는 자들을 확실하게 굴복시켰죠! 흠… 그럼 다음 타겟을 설정해 볼까요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_clear_ex_10609_1].dlg
   limit: do 140 znaków
   EN: We sure showed them what happens to those who resist the great cause! Hm... what should we target next?
   PL:
682. [Kwestia głosowa [battle_defeat_10609_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_defeat_10609_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Kwestia głosowa [battle_defeat_10609_1] (Defeat Wail)] 뭐… 괜찮아요. 유로지비는 승리보다 패배가 익숙한 집단이니까요. 대신 큰 승리를 위해 지독히 많은 도전을 할 뿐이랍니다!
   źródło: PersonalityVoiceDlg/Voice_Honglu_Yurodivy_10609.json :: dataList[id=battle_defeat_10609_1].dlg
   limit: do 220 znaków
   EN: Well... It's okay. The Yurodiviye is no stranger to failures. But we're nothing if not persistent. We'll keep trying, trying, and trying again for the great triumph!
   PL:

## [00] Fanghunt Office Fixer — Hong Lu — 송곳니 사냥 사무소 해결사
- ID Tożsamości: `10610` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 5 · HP bazowe: 73 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Rupture

684. [Karta Tożsamości — tytuł] 송곳니 사냥 사무소\n해결사
   źródło: Personalities.json :: dataList[id=10610].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Fanghunt Office\nFixer
   PL:
685. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10610].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10610].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Karta Tożsamości — opis] 홍루의 열번째 인격
   źródło: Personalities.json :: dataList[id=10610].desc
   limit: do 120 znaków
   EN: Hong Lu’s 10th Identity
   PL:
688. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 내려치기
   źródło: Skills_personality-06.json :: dataList[id=1061001].levelList[level=1].name ; dataList[id=1061001].levelList[level=2].name ; dataList[id=1061001].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Slam
   PL:
689. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061001].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1061001].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1061001].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
690. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] 대상의 [Burst]이 6 이상일 때, 코인 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1061001].levelList[level=2].desc ; dataList[id=1061001].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 6+ [Burst], Coin Power +1
   PL:
691. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061001].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 689 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061001].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 1 [Burst]
   PL:
693. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061001].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 692 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 뼈 부수기
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=1].name ; dataList[id=1061002].levelList[level=2].name ; dataList[id=1061002].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Bonecrusher
   PL:
695. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1061002].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
696. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬에서 [Burst]과 [Burst] 횟수를 부여하지 않는 대신 코인 위력 +1\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not inflict [Burst] or [Burst] Count; instead, gain Coin Power +1\n[WinDuel] Inflict +1 [Burst] Count
   PL:
697. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1061002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL:
698. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [TakeHpHealReduce] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TakeHpHealReduce]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down
   EN: [OnSucceedAttack] Inflict 1 [TakeHpHealReduce] next turn
   PL:
699. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Burst]이 6 이상일 때, 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬에서 [Burst]과 [Burst] 횟수를 부여하지 않는 대신 코인 위력 +1\n- 대상이 <혈귀>, <피주머니>면, 추가로 코인 위력 +1\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If target has 6+ [Burst], Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not inflict [Burst] or [Burst] Count; instead, gain Coin Power +1\n- If target is a <Bloodfiend> or a <Bloodbag>, gain an additional Coin Power +1\n[WinDuel] Inflict +1 [Burst] Count
   PL:
700. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Burst] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict +1 [Burst] Count
   PL:
701. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [TakeHpHealReduce] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TakeHpHealReduce]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down
   EN: [OnSucceedAttack] Inflict 2 [TakeHpHealReduce] next turn
   PL:
702. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 상쾌한 사냥 마무리
   źródło: Skills_personality-06.json :: dataList[id=1061003].levelList[level=3].name ; dataList[id=1061003].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: A Cheerful Hunt's End
   PL:
703. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬에서 [Burst]과 [Burst] 횟수를 부여하지 않는 대신 코인 위력 +1\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061003].levelList[level=3].desc
   (powtórzenie elementu 696 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061003].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1061003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 692 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061003].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1061003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 2 [Burst]
   PL:
706. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Burst]이 6 이상일 때, 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬에서 [Burst]과 [Burst] 횟수를 부여하지 않는 대신 코인 위력 +1\n- 대상이 <혈귀>, <피주머니>면, 추가로 코인 위력 +1\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061003].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If target has 6+ [Burst], Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not inflict [Burst] or [Burst] Count; instead, gain Coin Power +1\n- If target is a <Bloodfiend> or a <Bloodbag>, gain an additional Coin Power +1\n[WinDuel] Inflict +2 [Burst] Count
   PL:
707. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Burst]이 15 이상이거나, 대상의 현재 체력이 최대 체력의 30% 미만이면, 이 코인 재사용 (스킬 당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has 15+ [Burst], or has less than 30% HP, Reuse this Coin (once per Skill)
   PL:
708. [Obrona (ulepszenia 1,4) — nazwa] 긴급 지혈
   źródło: Skills_personality-06.json :: dataList[id=1061004].levelList[level=1].name ; dataList[id=1061004].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Emergency Styptics
   PL:
709. [Obrona (ulepszenie 4) — opis] [StartBattle] 자신의 [Laceration] 위력 2 감소 (턴 당 3회. [Laceration]이 감소하여 0 이하가 되면, 출혈 소멸)
   źródło: Skills_personality-06.json :: dataList[id=1061004].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Laceration] = 출혈 / Bleed
   EN: [StartBattle] Lose 2 [Laceration] Potency on self (3 times per turn. If [Laceration] Potency drops to 0 or less, the Bleed effect expires)
   PL:
710. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — nazwa] 유쾌한 사냥법
   źródło: Passives.json :: dataList[id=1061001].name
   limit: do 40 znaków
   EN: How to Hunt Cheerfully
   PL:
711. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — opis] 대상이 <혈귀>, <피주머니>면 피해량 +10%\n스킬 사용시 자신에게 [Laceration]이 있으면, 공격 적중 시 [Burst] 3 부여 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1061001].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Burst]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: If the target is a <Bloodfiend> or a <Bloodbag>, deal +10% damage\nOn Skill Use, if this unit has [Laceration], inflict 3 [Burst] On Hit (once per turn)
   PL:
712. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 유쾌한 사냥법
   źródło: Passives.json :: dataList[id=1061011].name
   (powtórzenie elementu 710 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — opis] 대상이 <혈귀>, <피주머니>거나, 대상의 [Burst]이 10 이상이면 피해량 +10%\n스킬 사용시 자신에게 [Laceration]이 있으면, 공격 적중 시 [Burst] 3 부여 (턴 당 2회)
   źródło: Passives.json :: dataList[id=1061011].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Laceration]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Laceration] = 출혈 / Bleed
   EN: If the target is a <Bloodfiend>, <Bloodbag>, or if the target has 10+ [Burst], deal +10% damage\nOn Skill Use, if this unit has [Laceration], inflict 3 [Burst] On Hit (2 times per turn)
   PL:
714. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — nazwa] 혈귀 공략 교본 - 지혈
   źródło: Passives.json :: dataList[id=1061021].name
   limit: do 50 znaków
   EN: Bloodfiend Hunting Manual - Styptics
   PL:
715. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — opis] 전투 시작 시, [Laceration]과 [Laceration] 횟수의 합이 가장 높은 아군 1명의 [Laceration] 횟수 2 감소\n속도가 가장 빠른 아군 1명이 [Burst]이 있는 적에게 공격 적중시, [DefenseDown] 1 부여 (턴 당 최대 2회)
   źródło: Passives.json :: dataList[id=1061021].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Burst], [DefenseDown]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Combat Start: 1 ally that has the highest sum of [Laceration] Potency and Count loses 2 [Laceration] Count\nWhen 1 ally with the fastest Speed hits an enemy that has [Burst], inflict 1 [DefenseDown] (2 times per turn)
   PL:
716. [Kwestia głosowa [get_10610_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=get_10610_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Kwestia głosowa [get_10610_1] (Identity Acquisition)] 혈귀 분들은 악독하면서 끈질겨요. 그러니까~ 제대로 준비해야겠죠?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=get_10610_1].dlg
   limit: do 180 znaków
   EN: Bloodfiends are not only vile, they're also very persistent. So~ we should make sure we have everything ready to take them on, right?
   PL:
718. [Kwestia głosowa [lobby_morning_10610_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=lobby_morning_10610_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Kwestia głosowa [lobby_morning_10610_1] (Morning Greeting)] 어라? 벌써 해가 떴네요. 슬슬 사냥이 끝나겠어요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=lobby_morning_10610_1].dlg
   limit: do 120 znaków
   EN: Hm? Is it sunrise already? Seems like the hunt is coming to a close.
   PL:
720. [Kwestia głosowa [lobby_noon_10610_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=lobby_noon_10610_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Kwestia głosowa [lobby_noon_10610_1] (Afternoon Greeting)] 흐아암… 조금이라도 자둬야겠어요.\n혈귀들이 몰래 숨어있을 시간이니, 기습 걱정도 덜하잖아요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=lobby_noon_10610_1].dlg
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Yaaawn... I think I'll try to sleep a little.\nAll the Bloodfiends have crawled into their holes, hiding. I don't need to worry much about ambushes at this hour.
   PL:
722. [Kwestia głosowa [lobby_night_10610_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=lobby_night_10610_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Kwestia głosowa [lobby_night_10610_1] (Evening Greeting)] 밤에는 되도록 조심하세요. 사람들의 시선이 사라진 밤이면… 숨어지내던 혈귀들이 하나 둘씩 기어나와 피를 탐하거든요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=lobby_night_10610_1].dlg
   limit: do 170 znaków
   EN: Watch yourself at night. When people aren't looking... That's when Bloodfiends crawl out of their dens in search of our blood.
   PL:
724. [Kwestia głosowa [smalltalk_10610_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=smalltalk_10610_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Kwestia głosowa [smalltalk_10610_1] (Chatter #1)] 같은 혈귀 사냥꾼이라고 해도, 서로 잘 알진 못해요.\n하지만 만나면 알아챌 수 있답니다? 혈귀 사냥꾼 특유의… 그 질척한 분노와 증오가 느껴지거든요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=smalltalk_10610_1].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Not all Bloodfiend Hunters know each other well.\nBut did you know that we can immediately tell whenever we're out on a job? There's that... unique flavor of leaden wrath and hatred that is found only in Bloodfiend Hunters.
   PL:
726. [Kwestia głosowa [smalltalk_10610_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=smalltalk_10610_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Kwestia głosowa [smalltalk_10610_2] (Chatter #2)] 저번에 생포한 혈귀 분은 집에 보내드리기로 했어요.\n집안 어르신 분들이 좋아하실 걸요? 오래 사는 혈귀에 대해 분명 궁금해하실 테니까요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=smalltalk_10610_2].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I decided to send the Bloodfiend we captured last time to my home.\nThe elders back home will love it! I'm sure they'll have many things to ask that Bloodfiend, given the long lifespans of its kind.
   PL:
728. [Kwestia głosowa [smalltalk_10610_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=smalltalk_10610_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Kwestia głosowa [smalltalk_10610_3] (Chatter #3)] 혈귀는 맹수 같은 거예요. 가끔 곁에 다가올 수도 있고, 착한 일을 할 수도 있지만…\n그건 다 배가 불러서 그래요. 굶주린 혈귀가 인간에게 다정할 리가 없거든요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=smalltalk_10610_3].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Bloodfiends are like wild animals. Sometimes they'll approach you in a friendly manner, sometimes they'll even do something kind. But...\n... assume they're full when they're like that. A hungry Bloodfiend will never be that kind toward humans.
   PL:
730. [Kwestia głosowa [smalltalk_10610_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=smalltalk_10610_4].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Kwestia głosowa [smalltalk_10610_4] (Post-Uptie Chat 1)] 혈귀는 멋대로 남의 가족을 빼앗아… 억지로 뇌를 헤집어 자신의 가족으로 삼아버려요.\n혈귀가 되어버리면 원래 가족은 가족이 아니게 되어버리는 걸까요? 진짜 가족이란 뭘까요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=smalltalk_10610_4].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Bloodfiends snatch people away from their own families and contort their brains to turn them into one of their own.\nWill your real family no longer be your own after you get turned? What even is a real family, I wonder?
   PL:
732. [Kwestia głosowa [smalltalk_10610_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=smalltalk_10610_5].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Kwestia głosowa [smalltalk_10610_5] (Post-Uptie Chat 2)] 혈귀도 인간이라 생각하는 사람도 있어요. 인간이 아니었다면 진작에 머리에서 처리하지 않았겠냐고…\n하지만 기준이야 몰라도 저희는 혈귀가 인간이 아니라고 생각한답니다. 그들은 박멸해야할 사냥감일 뿐이죠.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=smalltalk_10610_5].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Some people consider Bloodfiends humans. Otherwise, why won't the Head go after them, right?\nWell, that's their criteria. In our eyes, Bloodfiends aren't humans. They are just vermin we have to exterminate.
   PL:
734. [Kwestia głosowa [neglect_10610_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=neglect_10610_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Kwestia głosowa [neglect_10610_1] (Idle)] 물 한 잔 마실래요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=neglect_10610_1].dlg
   limit: do 120 znaków
   EN: Would you like a cup of water?
   PL:
736. [Kwestia głosowa [gacksung_10610_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=gacksung_10610_1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Kwestia głosowa [gacksung_10610_1] (Uptying)] 하하… 먹잇감이라고 생각했던 존재에게 사냥당하는 기분은 어떠신가요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=gacksung_10610_1].dlg
   limit: do 120 znaków
   EN: Ha ha... How does it feel, getting hunted down by your prey?
   PL:
738. [Kwestia głosowa [formation_10610_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=formation_10610_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Kwestia głosowa [formation_10610_1] (Deployment)] 혈귀 분들이… 또 날뛰고 있나요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=formation_10610_1].dlg
   limit: do 120 znaków
   EN: Are Bloodfiends... making a fuss again?
   PL:
740. [Kwestia głosowa [battleentry_10610_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battleentry_10610_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
741. [Kwestia głosowa [battleentry_10610_1] (Stage Entry)] 실력 없으면 따라오지 마세요. 방해되거든요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battleentry_10610_1].dlg
   limit: do 120 znaków
   EN: Don't bother coming along if you don't have what it takes. You'll only step on my foot~
   PL:
742. [Kwestia głosowa [battle_select_10610_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_select_10610_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [Kwestia głosowa [battle_select_10610_1] (Viewed in Battle)] 무기에 묻은 피 좀 닦아야겠어요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_select_10610_1].dlg
   limit: do 120 znaków
   EN: I should wipe that blood off my weapon.
   PL:
744. [Kwestia głosowa [battle_endcommand_10610_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_endcommand_10610_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Kwestia głosowa [battle_endcommand_10610_1] (Commencing Attack)] 사냥 시작.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_endcommand_10610_1].dlg
   limit: do 120 znaków
   EN: Let's hunt.
   PL:
746. [Kwestia głosowa [battle_enemy_break_10610_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_enemy_break_10610_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Kwestia głosowa [battle_enemy_break_10610_1] (Enemy Stagger)] 괴로우신가요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_enemy_break_10610_1].dlg
   limit: do 120 znaków
   EN: Does it hurt?
   PL:
748. [Kwestia głosowa [battle_break_10610_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_break_10610_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [Kwestia głosowa [battle_break_10610_1] (Staggered)] 으윽…
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_break_10610_1].dlg
   limit: do 120 znaków
   EN: Agh...
   PL:
750. [Kwestia głosowa [battle_kill_10610_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_kill_10610_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Kwestia głosowa [battle_kill_10610_1] (Enemy Killed)] 하하핫!
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_kill_10610_1].dlg
   limit: do 120 znaków
   EN: Hahaha!
   PL:
752. [Kwestia głosowa [battle_dead_10610_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_dead_10610_1].desc
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Kwestia głosowa [battle_dead_10610_1] (Death)] 하나라도… 더 데려가야…
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_dead_10610_1].dlg
   limit: do 120 znaków
   EN: I'll take... one more of you with me...
   PL:
754. [Kwestia głosowa [choice_success_p_10610_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=choice_success_p_10610_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Kwestia głosowa [choice_success_p_10610_2] (Check Passed)] 사냥에 도움이 되겠는걸요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=choice_success_p_10610_2].dlg
   limit: do 120 znaków
   EN: This'll be helpful for the hunt!
   PL:
756. [Kwestia głosowa [choice_fail_n_10610_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=choice_fail_n_10610_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Kwestia głosowa [choice_fail_n_10610_1] (Check Failed)] 아이쿠… 미안해요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=choice_fail_n_10610_1].dlg
   limit: do 120 znaków
   EN: Oops... my bad.
   PL:
758. [Kwestia głosowa [battle_clear_10610_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_clear_10610_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Kwestia głosowa [battle_clear_10610_1] (Victory Cry)] 몇 마리 놓쳤지만 승리했으니 문제 없어요. 도망친 혈귀 분들도 지금쯤 두려움에 떨고 있겠죠?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_clear_10610_1].dlg
   limit: do 120 znaków
   EN: A few of them gave us the slip, but we won in the end. They must be cowering in fear by now.
   PL:
760. [Kwestia głosowa [battle_clear_ex_10610_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_clear_ex_10610_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Kwestia głosowa [battle_clear_ex_10610_1] (Extra Conditions Fulfilled)] 이 구역에 혈귀는 더 남지 않은 것 같아요. 그럼 이제… 다음 사냥터로 가볼까요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_clear_ex_10610_1].dlg
   limit: do 130 znaków
   EN: I think this area's been cleansed of Bloodfiends. Then... shall we head to our next hunting ground?
   PL:
762. [Kwestia głosowa [battle_defeat_10610_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_defeat_10610_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Kwestia głosowa [battle_defeat_10610_1] (Defeat Wail)] 하하… 잘난 척했는데… 꼴사납게 져버렸네요. 하지만 다음에는 반드시…
   źródło: PersonalityVoiceDlg/Voice_Honglu_Bloodhunter_10610.json :: dataList[id=battle_defeat_10610_1].dlg
   limit: do 140 znaków
   EN: Ha ha... we lost, huh? For all that big talk I did... it's a bit embarrassing. But next time, I'll...
   PL:

## [000] Full-Stop Office Rep — Hong Lu — 마침표 사무소 대표
- ID Tożsamości: `10611` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9105 · HP bazowe: 70 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Poise

764. [Karta Tożsamości — tytuł] 마침표 사무소\n대표
   źródło: Personalities.json :: dataList[id=10611].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Full-Stop Office\nRep
   PL:
765. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10611].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10611].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Karta Tożsamości — opis] 홍루의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10611].desc
   limit: do 120 znaków
   EN: Hong Lu’s 11th Identity
   PL:
768. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 발사
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].name ; dataList[id=1061101].levelList[level=2].name ; dataList[id=1061101].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 3 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Take the Shot
   PL:
769. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL:
770. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend 1 [Bullet]
   PL:
771. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL:
773. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count<style="highlight"></style>
   PL:
776. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1061101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend 1 [Bullet]<style="highlight"></style>
   PL:
777. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 776 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] <style="highlight">2</style> 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain <style="highlight">2</style> [Breath]
   PL:
779. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1061101].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 776 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Breath] <style="highlight">2</style> 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=2].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 778 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +<style="highlight">3</style> [Breath] Count
   PL:
782. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]<style="highlight"></style>
   PL:
783. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 782 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 타겟 지정
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=1].name ; dataList[id=1061102].levelList[level=2].name ; dataList[id=1061102].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Target Marked
   PL:
785. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 마침표 사무소 해결사 히스클리프 인격이 전투에 등장해 있으면, 가장 높은 공명 당 20% 확률로 [CoveringFire] 발동\n[WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [WhenUse], [CoveringFire], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [CoveringFire] = 타겟 포착 / Target Spotted; [Breath] = 호흡 / Poise
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] If Full-Stop Office Fixer Heathcliff is on the field, every Reson. of the highest Reson. adds 20% chance that this unit activates [CoveringFire]\n[WhenUse] Gain +1 [Breath] Count
   PL:
786. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
787. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [Bullet] 최대 3 소모
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend up to 3 [Bullet]
   PL:
788. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] 피해량 +(소모한 탄환 x 10)%
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Deal +([Bullet] spent x 10)% damage
   PL:
789. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] next turn
   PL:
790. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 마침표 사무소 해결사 히스클리프 인격이 전투에 등장해 있으면, 가장 높은 공명 당 20% 확률로 [CoveringFire] 발동\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=2].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet], [WhenUse], [CoveringFire], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [CoveringFire] = 타겟 포착 / Target Spotted; [Breath] = 호흡 / Poise
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] If Full-Stop Office Fixer Heathcliff is on the field, every Reson. of the highest Reson. adds 20% chance that this unit activates [CoveringFire]\n[WhenUse] Gain +<style="highlight">2</style> [Breath] Count
   PL:
791. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1061102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 782 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [Bullet] 최대 3 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend up to 3 [Bullet]<style="highlight"></style>
   PL:
793. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] 피해량 +(소모한 탄환 x 10)%<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1061102].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Deal +([Bullet] spent x 10)% damage<style="highlight"></style>
   PL:
794. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [Binding] 1 부여</style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Binding] next turn</style>
   PL:
795. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] next turn<style="highlight"></style>
   PL:
796. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 마침표 사무소 해결사 히스클리프 인격이 전투에 등장해 있으면, 가장 높은 공명 당 25% 확률로 [CoveringFire] 발동\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=4].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet], [WhenUse], [CoveringFire], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [CoveringFire] = 타겟 포착 / Target Spotted; [Breath] = 호흡 / Poise
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] If Full-Stop Office Fixer Heathcliff is on the field, every Reson. of the highest Reson. adds 25% chance that this unit activates [CoveringFire]\n[WhenUse] Gain +<style="highlight">3</style> [Breath] Count
   PL:
797. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 3 — opis] <style="highlight">크리티컬 피해량 +(소모한 탄환 x 10)%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: <style="highlight">+([Bullet] spent x 10)% Damage on Critical Hit</style>
   PL:
798. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">크리티컬 피해량 +20%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+20% Damage on Critical Hit</style>
   PL:
799. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn<style="highlight"></style>
   PL:
800. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 795 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 삶의 마침표
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].name ; dataList[id=1061103].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 7 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Full-Stop to Life
   PL:
802. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 마침표 사무소 해결사 히스클리프 인격이 전투에 등장해 있으면, [CoveringFire] 발동\n[WhenUse] [Breath] 5 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [WhenUse], [CoveringFire], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [CoveringFire] = 타겟 포착 / Target Spotted; [Breath] = 호흡 / Poise
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] If Full-Stop Office Fixer Heathcliff is on the field, activate [CoveringFire]\n[WhenUse] Gain 5 [Breath]
   PL:
803. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] 피해량 + (소모한 탄환 x 10)%
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Deal +([Bullet] spent x 10)% damage
   PL:
805. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise the target's Stagger Threshold by 10% of damage dealt
   PL:
806. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [Bullet] 최대 2 소모
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend up to 2 [Bullet]
   PL:
807. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] 피해량 + (소모한 탄환 x 10)%
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 804 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 805 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 대상이 흐트러짐 상태면 크리티컬 피해량 +30%
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: If target is Staggered, +30% Damage on Critical Hit
   PL:
810. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL:
811. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [PenetrateTakeDamageUp] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [OnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp]
   PL:
812. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 마침표 사무소 해결사 히스클리프 인격이 전투에 등장해 있으면, [CoveringFire] 발동\n[WhenUse] [Breath] 5 얻음\n<style="highlight">[WinDuel] 자신의 [Breath] 횟수 2 증가</style>
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet], [WhenUse], [CoveringFire], [Breath], [WinDuel]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [CoveringFire] = 타겟 포착 / Target Spotted; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] If Full-Stop Office Fixer Heathcliff is on the field, activate [CoveringFire]\n[WhenUse] Gain 5 [Breath]\n<style="highlight">[WinDuel] Gain +2 [Breath] Count</style>
   PL:
813. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 776 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] 피해량 + (소모한 탄환 x <style="highlight">15</style>)%
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Deal +([Bullet] spent x <style="highlight">15</style>)% damage
   PL:
815. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 <style="highlight">15</style>%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise the target's Stagger Threshold by <style="highlight">15</style>% of damage dealt
   PL:
816. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [Bullet] 최대 2 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend up to 2 [Bullet]<style="highlight"></style>
   PL:
817. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] 피해량 + (소모한 탄환 x <style="highlight">15</style>)%
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 814 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 피해량의 <style="highlight">15</style>%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 815 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 대상이 흐트러짐 상태면 크리티컬 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: If target is Staggered, +30% Damage on Critical Hit<style="highlight"></style>
   PL:
820. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] <style="highlight">2</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Binding] next turn
   PL:
821. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [PenetrateTakeDamageUp] <style="highlight">2</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [PenetrateTakeDamageUp]
   PL:
822. [Umiejętność 4 (×0) (ulepszenia 2,4) — nazwa] 연계: 타겟 지정
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].name ; dataList[id=1061105].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 4 · monety: 4 (+4)
   limit: do 40 znaków
   EN: Combo: Target Marked
   PL:
823. [Umiejętność 4 (×0) (ulepszenie 2) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[DefeatDuel] 최종 위력 +5
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [WhenUse], [Breath], [DefeatDuel]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] Gain +2 [Breath] Count\n[DefeatDuel] Final Power +5
   PL:
824. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 786 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 2, efekt 1 — opis] [Bullet] 최대 3 소모
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 787 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 2, efekt 2 — opis] 피해량 +(소모한 탄환 x 10)%
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 788 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 810 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
830. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 4, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   EN: +30% Damage on Critical Hit
   PL:
831. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">3</style> 증가\n[DefeatDuel] 최종 위력 +5
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet], [WhenUse], [Breath], [DefeatDuel]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] Gain +<style="highlight">3</style> [Breath] Count\n[DefeatDuel] Final Power +5
   PL:
832. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 782 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [Bullet] 최대 3 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 792 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] 피해량 +(소모한 탄환 x 10)%<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 793 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
835. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 3 — opis] <style="highlight">크리티컬 피해량 +(소모한 탄환 x 10)%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 797 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">크리티컬 피해량 +20%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 798 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 799 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 795 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL:
840. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 2 — opis] 크리티컬 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: +30% Damage on Critical Hit<style="highlight"></style>
   PL:
841. [Umiejętność 5 (×0) (ulepszenia 3–4) — nazwa] 연계: 삶의 마침표
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].name ; dataList[id=1061106].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 7 · monety: 4 (+4)
   limit: do 40 znaków
   EN: Combo: Full-Stop to Life
   PL:
842. [Umiejętność 5 (×0) (ulepszenie 3) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] [Breath] 5 얻음\n[DefeatDuel] 최종 위력 +5
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [WhenUse], [Breath], [DefeatDuel]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] Gain 5 [Breath]\n[DefeatDuel] Final Power +5
   PL:
843. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] 피해량 + (소모한 탄환 x 10)%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 804 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 805 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
846. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [Bullet] 최대 2 소모
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 806 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 2 — opis] 피해량 + (소모한 탄환 x 10)%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 804 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 805 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] 대상이 흐트러짐 상태면 크리티컬 피해량 +30%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 809 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
850. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 810 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [PenetrateTakeDamageUp] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
852. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 829 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 4, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 830 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 4, efekt 3 — opis] 피해량 + (대상의 관통 내성 x 50)%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   EN: Deal +(target's Pierce Res. x 50)% damage
   PL:
855. [Umiejętność 5 (×0) (ulepszenie 4) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] [Breath] 5 얻음\n<style="highlight">[WinDuel] 자신의 [Breath] 횟수 2 증가</style>\n[DefeatDuel] 최종 위력 +5
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet], [WhenUse], [Breath], [WinDuel], [DefeatDuel]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] Gain 5 [Breath]\n<style="highlight">[WinDuel] Gain +2 [Breath] Count</style>\n[DefeatDuel] Final Power +5
   PL:
856. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 776 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] 피해량 + (소모한 탄환 x <style="highlight">15</style>)%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 814 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
858. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 <style="highlight">15</style>%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 815 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [Bullet] 최대 2 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 816 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] 피해량 + (소모한 탄환 x <style="highlight">15</style>)%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 814 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 피해량의 <style="highlight">15</style>%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 815 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
862. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] 대상이 흐트러짐 상태면 크리티컬 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 819 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] <style="highlight">2</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 820 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
864. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [PenetrateTakeDamageUp] <style="highlight">2</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 4, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 839 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
866. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">크리티컬 피해량 +50%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+50% Damage on Critical Hit</style>
   PL:
867. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 4, efekt 3 — opis] 피해량 + (대상의 관통 내성 x 50)%<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal +(target's Pierce Res. x 50)% damage<style="highlight"></style>
   PL:
868. [Umiejętność 6 (×0) (ulepszenia 1,4) — nazwa] 근접 지원
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=1].name ; dataList[id=1061108].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Melee Support
   PL:
869. [Umiejętność 6 (×0) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=1].desc
   (powtórzenie elementu 769 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [Umiejętność 6 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Umiejętność 6 (×0) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
872. [Umiejętność 6 (×0) (ulepszenie 4) — opis] <style="highlight">크리티컬 피해량 +20%</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: <style="highlight">+20% Damage on Critical Hit</style>\n[WhenUse] Gain +2 [Breath] Count
   PL:
873. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]<style="highlight"></style>
   PL:
874. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 873 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Obrona (ulepszenia 1,4) — nazwa] 전투 호흡
   źródło: Skills_personality-06.json :: dataList[id=1061104].levelList[level=1].name ; dataList[id=1061104].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Combat Poise
   PL:
876. [Obrona (ulepszenie 1) — opis] 턴 시작 시 [Bullet]이 0이면, '그림자의 건너편'으로 변경됨\n[OnSucceedEvade] [Breath] 1 얻음 (턴 당 3회)
   źródło: Skills_personality-06.json :: dataList[id=1061104].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [OnSucceedEvade], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: Turn Start: at 0 [Bullet], activate 'Beyond the Shadow' instead\n[OnSucceedEvade] Gain 1 [Breath] (3 times per turn)
   PL:
877. [Obrona (ulepszenie 4) — opis] 턴 시작 시 [Bullet]이 0이면, '그림자의 건너편'으로 변경됨\n[OnSucceedEvade] [Breath] 1 얻음 (턴 당 <style="highlight">5</style>회)
   źródło: Skills_personality-06.json :: dataList[id=1061104].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet], [OnSucceedEvade], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: Turn Start: at 0 [Bullet], activate 'Beyond the Shadow' instead\n[OnSucceedEvade] Gain 1 [Breath] (<style="highlight">5</style> times per turn)
   PL:
878. [Obrona (ulepszenia 1,4) — nazwa] 그림자의 건너편
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=1].name ; dataList[id=1061107].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Beyond the Shadow
   PL:
879. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[EndBattle] [FullReload] (전투 당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Breath], [EndBattle], [FullReload]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndBattle] = [턴 종료 시] / [Turn End]; [FullReload] = 재장전 / Reload
   EN: [DuelCounter]\n[WhenUse] Gain +2 [Breath] Count\n[EndBattle] [FullReload] (once per Encounter)
   PL:
880. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
882. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n<style="highlight">크리티컬 피해량 +20%</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[EndBattle] [FullReload] (전투 당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [WhenUse], [Breath], [EndBattle], [FullReload]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndBattle] = [턴 종료 시] / [Turn End]; [FullReload] = 재장전 / Reload
   EN: [DuelCounter]\n<style="highlight">+20% Damage on Critical Hit</style>\n[WhenUse] Gain +2 [Breath] Count\n[EndBattle] [FullReload] (once per Encounter)
   PL:
883. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 873 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
884. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 873 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
885. [Pasywka bojowa (od ulepszenia 1) — nazwa] 집중
   źródło: Passives.json :: dataList[id=1061101].name
   limit: do 40 znaków
   EN: Concentration
   PL:
886. [Pasywka bojowa (od ulepszenia 1) — opis] [Bullet]을 소모하는 코인을 굴릴 때, [Bullet]이 없는 경우에도 해당 코인의 적중시 효과를 부여하지 않는 대신 공격이 취소되지 않음
   źródło: Passives.json :: dataList[id=1061101].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: When flipping a Coin that consumes [Bullet]: even when this unit is out of [Bullet], the attack does not get canceled. However, the affected Coins' On Hit effects do not activate in such cases.
   PL:
887. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — nazwa] 전술적 사격 지원
   źródło: Passives.json :: dataList[id=1061102].name
   limit: do 40 znaków
   EN: Tactical Fire Support
   PL:
888. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — opis] 마침표 사무소 해결사 히스클리프가 [Retreat_FullStop] 상태거나, 대기 인원으로 편성되어 있다면 마침표 사무소 대표 홍루 인격의 스킬2, 스킬3이 강화됨
   źródło: Passives.json :: dataList[id=1061102].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [Retreat_FullStop]
   znaczenie tagów: [Retreat_FullStop] = 후방 지원 배치 / Overwatch Assignment
   EN: If the Full-Stop Office Fixer Heathcliff is in [Retreat_FullStop] state, or has been Deployed as a Backup unit, empower Full-Stop Office Rep. Hong Lu's Skill 2 and Skill 3
   PL:
889. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Pride) — nazwa] 전술적 사격 지원
   źródło: Passives.json :: dataList[id=1061111].name
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
890. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Pride) — opis] 마침표 사무소 해결사 히스클리프가 [Retreat_FullStop] 상태거나, 대기 인원으로 편성되어 있다면 마침표 사무소 대표 홍루 인격의 스킬2, 스킬3이 강화됨\n\n전투 시작시 자신의 [Breath] 위력이 20 이상이면, [Breath] 횟수 1 얻음
   źródło: Passives.json :: dataList[id=1061111].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Retreat_FullStop], [Breath]
   znaczenie tagów: [Retreat_FullStop] = 후방 지원 배치 / Overwatch Assignment; [Breath] = 호흡 / Poise
   EN: If the Full-Stop Office Fixer Heathcliff is in [Retreat_FullStop] state, or has been Deployed as a Backup unit, empower Full-Stop Office Rep. Hong Lu's Skill 2 and Skill 3\n\nCombat Start: at 20+ [Breath] Potency, gain +1 [Breath] Count
   PL:
891. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — nazwa] 제압 사격
   źródło: Passives.json :: dataList[id=1061121].name
   limit: do 40 znaków
   EN: Suppressing Fire
   PL:
892. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — opis] [Bullet]을 가장 많이 보유한 아군 인격이 [Bullet]을 소모하는 스킬로 가하는 피해량 +10%\n([Bullet]이 없으면 적용되지 않음)
   źródło: Passives.json :: dataList[id=1061121].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Ally Identity that has the most [Bullet] deals +10% damage using Skills that spend [Bullet]\n(Does not activate when out of [Bullet])
   PL:
893. [Kwestia głosowa [get_10611_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=get_10611_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
894. [Kwestia głosowa [get_10611_1] (Identity Acquisition)] 자, 사격 중지. 앞쪽 시야가 확보되는 대로… 적들을 추적할게요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=get_10611_1].dlg
   limit: do 120 znaków
   EN: Hold your fire, now. We'll chase them down as soon as we get a clear shot.
   PL:
895. [Kwestia głosowa [lobby_morning_10611_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=lobby_morning_10611_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
896. [Kwestia głosowa [lobby_morning_10611_1] (Morning Greeting)] 일어나셨으면 총기 손질 먼저 해야죠~ 매일 청소해주지 않으면 쏘다가 고장나버릴지 모르잖아요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=lobby_morning_10611_1].dlg
   limit: do 170 znaków
   EN: Good morning, let's clean some guns~ Make sure they're in tip-top shape! We don't want them to jam in the middle of a fight, right?
   PL:
897. [Kwestia głosowa [lobby_noon_10611_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=lobby_noon_10611_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Kwestia głosowa [lobby_noon_10611_1] (Afternoon Greeting)] 점심 먹고 사격 연습이나 할까요? 탄환이 비싸다고 해도, 목숨보다 비싸겠어요?\n어, 그런데 그렇게 비싸게 느껴지시나요? 어… 신기하네요. 전 생각보다 굉장히 저렴해서 놀랐거든요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=lobby_noon_10611_1].dlg
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Want to go practice shooting after lunch? Bullets sure are expensive, but it can't be more expensive than your life, right?\nSeriously, though. Do you actually feel like these are that pricey? Huh... that's funny. I was actually pretty surprised because they were much cheaper than I thought they'd be.
   PL:
899. [Kwestia głosowa [lobby_night_10611_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=lobby_night_10611_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
900. [Kwestia głosowa [lobby_night_10611_1] (Evening Greeting)] 날이 어두워진 걸 보니 조금 있으면 연설이 시작되겠네요~\n교주는 히스클리프 씨에게 맡기고… 저희는 그 이후에 몰려올 신도들만 막으면 돼요. 까먹으신 건 아니죠?
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=lobby_night_10611_1].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It's getting dark outside... Looks like the speech is about to start~\nWe'll leave the leader to Heathcliff and focus on handling the worshipers who'll likely rush us after the deed is done. You remember the plan, right?
   PL:
901. [Kwestia głosowa [smalltalk_10611_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=smalltalk_10611_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [Kwestia głosowa [smalltalk_10611_1] (Chatter #1)] 로직 아틀리에도 괜찮은 공방이지만, S급 공방과 비교할 정도는 아니죠.\n큰 형이 어렵게 사온 S급 공방제 총을 본 적이 있는데… 저희가 쓰는 것과는 비교도 안 될 정도로 좋은 성능을 갖추고 있었거든요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=smalltalk_10611_1].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Atelier Logic is acceptable, but I wouldn't compare them to the S-class Workshops.\nI once saw an S-class firearm my big brother somehow managed to get his hands on, and it was much better than the ones we're using in our Office.
   PL:
903. [Kwestia głosowa [smalltalk_10611_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=smalltalk_10611_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
904. [Kwestia głosowa [smalltalk_10611_2] (Chatter #2)] 탄환 속도에 반응하지 못하는 고만고만한 대상을 신속하게 쓸어주는 게 저희 사무소의 셀링 포인트랍니다.\n반응할 수 있는 강자들을 만나면 어떡하냐구요? 당연히 도망쳐야죠~
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=smalltalk_10611_2].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The real selling point of our Office is that we can quickly mow down weaker enemies who can't react fast enough to bullets.\nOh, what about enemies who can react to bullets? We'll run, of course~
   PL:
905. [Kwestia głosowa [smalltalk_10611_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=smalltalk_10611_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
906. [Kwestia głosowa [smalltalk_10611_3] (Chatter #3)] 머리는 사람이 시시하게 죽어나가는 걸 원하지 않을 거예요. 하지만 시시한 죽음이란 뭘까요?\n죽음에 많은 의미를 부여해도, 결국 죽는 건 변치 않을텐데.
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=smalltalk_10611_3].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I don't think the Head wants people to die anticlimactically. But what <i>is </i>an anticlimactic death anyway?\nWe can put all kinds of meaningful labels on deaths, but it's still death at the end of the day.
   PL:
907. [Kwestia głosowa [smalltalk_10611_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=smalltalk_10611_4].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Kwestia głosowa [smalltalk_10611_4] (Post-Uptie Chat 1)] 하하. 탄환이 강철을 뚫지 못한다고 방심하셨나봐요.\n여러분에겐 안타까운 이야기지만… 탄환으로 강철을 부수는 건, 머리의 금기에 어긋나지 않는답니다~
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=smalltalk_10611_4].dlg
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ha ha, were you feeling safe back there because bullets can't penetrate steel?\nI have some bad news for you... shattering steel does not break the Head's Taboo~
   PL:
909. [Kwestia głosowa [smalltalk_10611_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=smalltalk_10611_5].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Kwestia głosowa [smalltalk_10611_5] (Post-Uptie Chat 2)] 불행하더라도, 뛰쳐나와선 안되는 자리도 있는 법이에요. 자리를 옮기려다 이렇게 톱니바퀴가 박살나면… 안타깝잖아요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=smalltalk_10611_5].dlg
   limit: do 240 znaków
   EN: I know it's tragic, but there are some covers where you shouldn't just jump out like that. Having your gear destroyed while trying to adjust your position is just... unfortunate, isn't it?
   PL:
911. [Kwestia głosowa [neglect_10611_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=neglect_10611_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [Kwestia głosowa [neglect_10611_1] (Idle)] 응? 돈은 없는데 탄약이 또 다 떨어졌다구요? 하하… 가문에 연락해야겠네요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=neglect_10611_1].dlg
   limit: do 140 znaków
   EN: Hm? We're out of both cash and ammunition? Ha ha... Looks like I'm going to have to give my family a call~
   PL:
913. [Kwestia głosowa [gacksung_10611_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=gacksung_10611_1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
914. [Kwestia głosowa [gacksung_10611_1] (Uptying)] 가슴에 세 발. 머리는… 쏠 필요도 없겠네요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=gacksung_10611_1].dlg
   limit: do 150 znaków
   EN: Three shots to the chest, and... doesn't look like I'll even need to shoot them in the head for good measure.
   PL:
915. [Kwestia głosowa [formation_10611_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=formation_10611_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
916. [Kwestia głosowa [formation_10611_1] (Deployment)] 지휘를 받는 건 오랜만이네요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=formation_10611_1].dlg
   limit: do 120 znaków
   EN: It's been a while since I was under someone else's command.
   PL:
917. [Kwestia głosowa [battleentry_10611_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battleentry_10611_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
918. [Kwestia głosowa [battleentry_10611_1] (Stage Entry)] 엄호 부탁드려요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battleentry_10611_1].dlg
   limit: do 120 znaków
   EN: Cover me, please~
   PL:
919. [Kwestia głosowa [battle_select_10611_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_select_10611_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
920. [Kwestia głosowa [battle_select_10611_1] (Viewed in Battle)] 긴장하셨나요? 그럴 땐 크게 심호흡을 하면 도움이 된답니다.
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_select_10611_1].dlg
   limit: do 120 znaków
   EN: Nervous? Take a deep, deep breath—it'll help.
   PL:
921. [Kwestia głosowa [battle_endcommand_10611_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_endcommand_10611_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [Kwestia głosowa [battle_endcommand_10611_1] (Commencing Attack)] 타겟 포착, 1시 방향.
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_endcommand_10611_1].dlg
   limit: do 120 znaków
   EN: Target in sight. One O'clock.
   PL:
923. [Kwestia głosowa [battle_enemy_break_10611_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_enemy_break_10611_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
924. [Kwestia głosowa [battle_enemy_break_10611_1] (Enemy Stagger)] 움직임이 어설퍼요~
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_enemy_break_10611_1].dlg
   limit: do 120 znaków
   EN: You don't really know what you're doing, do you~?
   PL:
925. [Kwestia głosowa [battle_break_10611_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_break_10611_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [Kwestia głosowa [battle_break_10611_1] (Staggered)] 윽…
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_break_10611_1].dlg
   limit: do 120 znaków
   EN: Ugh...!
   PL:
927. [Kwestia głosowa [battle_kill_10611_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_kill_10611_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
928. [Kwestia głosowa [battle_kill_10611_1] (Enemy Killed)] 다음 목표로.
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_kill_10611_1].dlg
   limit: do 120 znaków
   EN: Next target.
   PL:
929. [Kwestia głosowa [battle_dead_10611_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_dead_10611_1].desc
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
930. [Kwestia głosowa [battle_dead_10611_1] (Death)] 얕본 건… 저였나보군요…
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_dead_10611_1].dlg
   limit: do 120 znaków
   EN: Looks like I was the one who was made light of…
   PL:
931. [Kwestia głosowa [choice_success_p_10611_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=choice_success_p_10611_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
932. [Kwestia głosowa [choice_success_p_10611_2] (Check Passed)] 계획을 세워두면, 이런 것도 어렵지 않답니다.
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=choice_success_p_10611_2].dlg
   limit: do 120 znaków
   EN: Everything can be made manageable with a plan.
   PL:
933. [Kwestia głosowa [choice_fail_n_10611_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=choice_fail_n_10611_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
934. [Kwestia głosowa [choice_fail_n_10611_1] (Check Failed)] 음~ 잘 안 됐네요. 이제 어떻게 되는 걸까요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=choice_fail_n_10611_1].dlg
   limit: do 120 znaków
   EN: Hmm~ That didn't work out. What now?
   PL:
935. [Kwestia głosowa [battle_clear_10611_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_clear_10611_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
936. [Kwestia głosowa [battle_clear_10611_1] (Victory Cry)] 합당한 승리네요. 다들 이상은 없으신가요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_clear_10611_1].dlg
   limit: do 120 znaków
   EN: That sure was a rightful victory. Is everyone alright?
   PL:
937. [Kwestia głosowa [battle_clear_ex_10611_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_clear_ex_10611_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
938. [Kwestia głosowa [battle_clear_ex_10611_1] (Extra Conditions Fulfilled)] 의뢰비랑 보호 수당에서… 사용한 탄환값을 빼면… 와아~ 오늘은 제 사비로 손해를 메울 필요가 없네요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_clear_ex_10611_1].dlg
   limit: do 180 znaków
   EN: Contract fee plus safeguard fee minus bullet costs... Wow~ looks like I won't have to make up for the losses with my own funds this time!
   PL:
939. [Kwestia głosowa [battle_defeat_10611_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_defeat_10611_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
940. [Kwestia głosowa [battle_defeat_10611_1] (Defeat Wail)] 의뢰는 여기서 중단. 모두 퇴각하세요!\n…품에 있는 그건 뭔가요? 으음. 총은 다시 사면 된다니까요. 도망칠 때 걸리적거리니까 빨리 버리세요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_FullStop_10611.json :: dataList[id=battle_defeat_10611_1].dlg
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Abort contract. Everyone, fall back!\nWhat's that in your hand? Oh. Like I said, we can always buy new guns. Just discard it, it'll only slow you down.
   PL:

## [000] R Corp. 4th Pack Reindeer — Hong Lu — R사 제 4무리 순록팀
- ID Tożsamości: `10612` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 65 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Charge, Sinking

941. [Karta Tożsamości — tytuł] R사 제 4무리\n순록팀
   źródło: Personalities.json :: dataList[id=10612].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: R Corp. 4th Pack\nReindeer
   PL:
942. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10612].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
943. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10612].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
944. [Karta Tożsamości — opis] 홍루의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10612].desc
   limit: do 120 znaków
   EN: Hong Lu’s 12th Identity
   PL:
945. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 에너지 강타
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=1].name ; dataList[id=1061201].levelList[level=2].name ; dataList[id=1061201].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Energy Strike
   PL:
946. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [Charge]이 2 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [WhenUse]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: At 2+ [Charge], Coin Power +1\n[WhenUse] Gain +2 [Charge] Count
   PL:
947. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL:
948. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[Charge]당 피해량 +2% (최대 10%)</style>\n[Charge]이 2 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [WhenUse]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">Deal +2% damage for every [Charge] (max 10%)</style>\nAt 2+ [Charge], Coin Power +1\n[WhenUse] Gain +2 [Charge] Count
   PL:
949. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] ([Charge] + 1)만큼 자신의 [Charge] 횟수 증가 (최대 3)</style>
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: <style="highlight">[OnSucceedAttack] Gain +([Charge] + 1) [Charge] Count (max 3)</style>
   PL:
950. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]<style="highlight"></style>
   PL:
951. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [Charge]당 피해량 <style="highlight">+3%</style> (최대 <style="highlight">15%</style>)\n[Charge]이 2 이상이면, 코인 위력 +1\n<style="highlight">[Charge] 횟수가 5 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [WhenUse]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: Deal <style="highlight">+3%</style> damage for every [Charge] (max <style="highlight">15%</style>)\nAt 2+ [Charge], Coin Power +1\n<style="highlight">At 5+ [Charge] Count, Coin Power +1</style>\n[WhenUse] Gain +2 [Charge] Count
   PL:
952. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] ([Charge] + 1)만큼 자신의 [Charge] 횟수 증가 (최대 <style="highlight">4</style>)
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] + 1) [Charge] Count (max <style="highlight">4</style>)
   PL:
953. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 정신 채찍
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=1].name ; dataList[id=1061202].levelList[level=2].name ; dataList[id=1061202].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 2 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Mind Whip
   PL:
954. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면,\n- [Sinking] 15 얻음, [Charge] 횟수 10으로 증가\n- 이 스킬이 [CantIdentify], [WideAreaRampage] 상태가 되고 공격 가중치 +1\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [Sinking], [CantIdentify], [WideAreaRampage]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [Sinking] = 침잠 / Sinking; [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WideAreaRampage] = 광역 난사 / Unfocused Volley
   EN: [WhenUse] At 5~9 [Charge] Count:\n- Gain 15 [Sinking] and raise this unit's [Charge] Count to 10\n- This Skill gains the following attributes: [CantIdentify], [WideAreaRampage], and Atk Weight +1\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power +1
   PL:
955. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
956. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 947 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
958. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL:
959. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[Charge]당 피해량 +2% (최대 10%)</style>\n[WhenUse] [Charge] 횟수가 5 이상 10 미만이면,\n- [Sinking] 15 얻음, [Charge] 횟수 10으로 증가\n- 이 스킬이 [CantIdentify], [WideAreaRampage] 상태가 되고 공격 가중치 +1\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [WhenUse], [Sinking], [CantIdentify], [WideAreaRampage]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WideAreaRampage] = 광역 난사 / Unfocused Volley
   EN: <style="highlight">Deal +2% damage for every [Charge] (max 10%)</style>\n[WhenUse] At 5~9 [Charge] Count:\n- Gain 15 [Sinking] and raise this unit's [Charge] Count to 10\n- This Skill gains the following attributes: [CantIdentify], [WideAreaRampage], and Atk Weight +1\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power +1
   PL:
960. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1061202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 950 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
961. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 피해량의 5%만큼 흐트러짐 손상을 입힘</style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] Raise Stagger Threshold by 5% of damage dealt</style>
   PL:
962. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 950 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
963. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 피해량의 5%만큼 흐트러짐 손상을 입힘</style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 961 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
964. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1061202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 950 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
965. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 피해량의 5%만큼 흐트러짐 손상을 입힘</style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 961 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
966. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#3].coindescs[#0].desc ; dataList[id=1061202].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count<style="highlight"></style>
   PL:
967. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상을 입힘</style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] Raise Stagger Threshold by 10% of damage dealt</style>
   PL:
968. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [Charge]당 피해량 <style="highlight">+4%</style> (최대 <style="highlight">20%</style>)\n[WhenUse] [Charge] 횟수가 5 이상 10 미만이면,\n- [Sinking] <style="highlight">10</style> 얻음, [Charge] 횟수 10으로 증가\n- 이 스킬이 [CantIdentify], [WideAreaRampage] 상태가 되고 공격 가중치 +1\n<style="highlight">- [BeforeUse] [Charge]이 5 이상이면, [CantIdentify] 효과가 적용되지 않음</style>\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 <style="highlight">+2</style>\n<style="highlight">[BeforeAttack] 남은 [Charge] 횟수가 8 이상이면, [Charge] 횟수를 8 소모하여 피해량 +40%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=4].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [WhenUse], [Sinking], [CantIdentify], [WideAreaRampage], [BeforeUse], [BeforeAttack]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WideAreaRampage] = 광역 난사 / Unfocused Volley; [BeforeUse] = [사용전] / [Before Use]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: Deal <style="highlight">+4%</style> damage for every [Charge] (max <style="highlight">20%</style>)\n[WhenUse] At 5~9 [Charge] Count:\n- Gain <style="highlight">10</style> [Sinking] and raise this unit's [Charge] Count to 10\n- This Skill gains the following attributes: [CantIdentify], [WideAreaRampage], and Atk Weight +1\n<style="highlight">- [BeforeUse] At 5+ [Charge], this Skill does not gain the [CantIdentify] effect</style>\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power <style="highlight">+2</style>\n<style="highlight">[BeforeAttack] At 8+ remaining [Charge] Count, consume 8 [Charge] Count to deal +40% damage</style>
   PL:
969. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 5%만큼 흐트러짐 손상을 입힘<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 5% of damage dealt<style="highlight"></style>
   PL:
970. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량의 5%만큼 흐트러짐 손상을 입힘<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 969 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
971. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 피해량의 5%만큼 흐트러짐 손상을 입힘<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 969 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
972. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상을 입힘<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 10% of damage dealt<style="highlight"></style>
   PL:
973. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 집중
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=3].name ; dataList[id=1061203].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 8 · monety: 1 (+10)
   (powtórzenie elementu 885 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
974. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [Charge]당 코인 위력 +1 (최대 5)\n[Charge] 횟수가 10 이상이면, 최종 위력 +2\n[WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=3].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [WhenUse]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: Coin Power +1 for every [Charge] (max 5)\nAt 10+ [Charge] Count, Final Power +2\n[WhenUse] Gain +5 [Charge] Count
   PL:
975. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] 피해량 +(이 스킬의 위력 x 5)% (최대 100%)
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +(this Skill's Power x 5)% damage (max 100%)
   PL:
976. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] ([Charge] + 1)만큼 자신의 [Charge] 횟수 증가 (최대 6)
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] + 1) [Charge] Count (max 6)
   PL:
977. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Sinking] 4 부여, [Sinking] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking] and +2 [Sinking] Count
   PL:
978. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [Charge]당 <style="highlight">기본 위력 +1</style>, 코인 위력 +1 <style="highlight">(각각 최대 5)</style>\n[Charge] 횟수가 10 이상이면, 최종 위력 <style="highlight">+4</style>\n[WhenUse] 자신의 [Charge] 횟수 <style="highlight">7</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [WhenUse]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">Base Power +1</style> and Coin Power +1 for every [Charge] <style="highlight">(max 5 each)</style>\nAt 10+ [Charge] Count, Final Power <style="highlight">+4</style>\n[WhenUse] Gain <style="highlight">+7</style> [Charge] Count
   PL:
979. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] 피해량 +(이 스킬의 위력 x 5)% (최대 <style="highlight">150%</style>)
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal +(this Skill's Power x 5)% damage (max <style="highlight">150%</style>)
   PL:
980. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[Charge]이 3 이상이면, [Charge]당 피해량 +20% (최대 100%)</style>
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: <style="highlight">At 3+ [Charge], deal +20% damage for every [Charge] (max 100%)</style>
   PL:
981. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] ([Charge] + <style="highlight">3</style>)만큼 자신의 [Charge] 횟수 증가 (최대 <style="highlight">8</style>)
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] + <style="highlight">3</style>) [Charge] Count (max <style="highlight">8</style>)
   PL:
982. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Sinking] 4 부여, [Sinking] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking] and <style="highlight">+4</style> [Sinking] Count
   PL:
983. [Obrona (ulepszenia 1,4) — nazwa] 에너지 응집
   źródło: Skills_personality-06.json :: dataList[id=1061204].levelList[level=1].name ; dataList[id=1061204].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Energy Condensation
   PL:
984. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수가 10 이상이면, 코인 위력 +2\n[WhenUse] 자신의 [Charge] 횟수 3 증가 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061204].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 10+ [Charge] Count, Coin Power +2\n[WhenUse] Gain +3 [Charge] Count (once per turn)
   PL:
985. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 [Charge] 횟수가 10 이상이면, 코인 위력 <style="highlight">+4</style>\n[WhenUse] 자신의 [Charge] 횟수 3 증가 (턴당 <style="highlight">2</style>회)
   źródło: Skills_personality-06.json :: dataList[id=1061204].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 10+ [Charge] Count, Coin Power <style="highlight">+4</style>\n[WhenUse] Gain +3 [Charge] Count (<style="highlight">2 times</style> per turn)
   PL:
986. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 뇌파 충전 집속 뿔
   źródło: Passives.json :: dataList[id=1061201].name
   limit: do 50 znaków
   EN: Brainwave Charge-focusing Antlers
   PL:
987. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음\n\n[Charge]이 2 이상이면,\n- 기본 공격 스킬로 부여하는 [Sinking] 부여량 +1 ([Sinking] 횟수만 증가하거나 스스로 [Sinking]을 얻는 경우에는 적용되지 않음)\n- 기본 공격 스킬의 피해량이 ([Charge] x 3)%만큼 증가 (최대 15%)
   źródło: Passives.json :: dataList[id=1061201].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [Sinking]
   znaczenie tagów: [Charge] = 충전 / Charge; [Sinking] = 침잠 / Sinking
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\n\nAt 2+ [Charge]:\n- Inflict +1 more [Sinking] using Base Attack Skills (does not activate when inflicting only [Sinking] Count or when inflicting [Sinking] on self)\n- Deal +([Charge] x 3)% damage using Base Attack Skills (max 15%)
   PL:
988. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — nazwa] 뇌파 충전 집속 뿔
   źródło: Passives.json :: dataList[id=1061211].name
   (powtórzenie elementu 986 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
989. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음\n\n[Charge]이 2 이상이면,\n<style="highlight">- [Charge] 2당 기본 공격 스킬로 부여하는 [Sinking] 부여량 +1 (최대 2, [Sinking] 횟수만 증가하거나 스스로 [Sinking]을 얻는 경우에는 적용되지 않음)</style>\n- 기본 공격 스킬의 피해량이 ([Charge] x <style="highlight">5</style>)%만큼 증가 (최대 <style="highlight">25%</style>)
   źródło: Passives.json :: dataList[id=1061211].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [Sinking]
   znaczenie tagów: [Charge] = 충전 / Charge; [Sinking] = 침잠 / Sinking
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\n\nAt 2+ [Charge]:\n<style="highlight">- Inflict +1 more [Sinking] using Base Attack Skills for every 2 [Charge] (max 2, does not activate when inflicting only [Sinking] Count or when inflicting [Sinking] on self)</style>\n- Deal +([Charge] x <style="highlight">5</style>)% damage using Base Attack Skills (max <style="highlight">25%</style>)
   PL:
990. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — nazwa] 충전 분쇄 지원
   źródło: Passives.json :: dataList[id=1061221].name
   limit: do 50 znaków
   EN: Charged Pulverization Support
   PL:
991. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — opis] [Charge]이 가장 높은 아군 1명이 [Charge] 횟수를 획득하는 기본 공격 스킬 사용 시, 마지막 코인의 피해량 +10%
   źródło: Passives.json :: dataList[id=1061221].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: 1 ally that has the most [Charge]: When using a Base Attack Skill that gains [Charge] Count, deal +10% damage using the final Coin
   PL:
992. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Envy) — nazwa] 충전 분쇄 지원
   źródło: Passives.json :: dataList[id=1061231].name
   (powtórzenie elementu 990 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
993. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Envy) — opis] [Charge]이 가장 높은 아군 1명이 [Charge] 횟수를 획득하는 기본 공격 스킬 사용 시, 마지막 코인의 피해량 <style="highlight">+15%</style>
   źródło: Passives.json :: dataList[id=1061231].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: 1 ally that has the most [Charge]: When using a Base Attack Skill that gains [Charge] Count, deal <style="highlight">+15%</style> damage using the final Coin
   PL:
994. [Kwestia głosowa [get_10612_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=get_10612_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
995. [Kwestia głosowa [get_10612_1] (Identity Acquisition)] 하… 이번엔 순록이 가장 먼저 투입되는 건가? 토끼와 코뿔소에게 빨리 오지 않으면 뜯을 풀이 없을 거라고 전해주실래요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=get_10612_1].dlg
   limit: do 190 znaków
   EN: Haah... They're sending in the Reindeer team first? Hello, please tell Rabbits and Rhinos to hurry up, or there won't be any grass left to graze on.
   PL:
996. [Kwestia głosowa [lobby_morning_10612_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=lobby_morning_10612_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
997. [Kwestia głosowa [lobby_morning_10612_1] (Morning Greeting)] 자고 일어나도 나아지는 게 없네요. 이 지끈거리는 두통은 약을 먹고, 또 먹어도… 죽기 전까진 제 머리를 헤집어둘 거예요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=lobby_morning_10612_1].dlg
   limit: do 190 znaków
   EN: Sleep doesn't help at all. This pounding headache just won't go away no matter how many pills I pop... It'll keep messing with my head until I die.
   PL:
998. [Kwestia głosowa [lobby_noon_10612_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=lobby_noon_10612_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
999. [Kwestia głosowa [lobby_noon_10612_1] (Afternoon Greeting)] 식사는 꼬박꼬박 챙겨 먹는 편이 좋아요~ 섬멸 작전이 시작되면 밥을 먹을 시간 같은 건 없거든요.\n죽었다 정신 차려도… 부화장 안일 테고, 거긴 사람밖에 먹을 게 없답니다.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=lobby_noon_10612_1].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It's a good idea to get a nice meal when we can~ Once these extermination operations begin, we won't be given any time to eat.\nAnd even after I die... I'll just wake up inside the Hatchery. And the only sustenance in there is people.
   PL:
1000. [Kwestia głosowa [lobby_night_10612_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=lobby_night_10612_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1001. [Kwestia głosowa [lobby_night_10612_1] (Evening Greeting)] 밤이 찾아와도 섬멸은 끝나지 않아요. 이 지역에 있는 모든 인간을 사살할 때까지… 이 지팡이의 불빛은 꺼지지 않는답니다.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=lobby_night_10612_1].dlg
   limit: do 160 znaków
   EN: Extermination doesn't end when night falls. It'll take killing every human in the area... for this staff's light to go out.
   PL:
1002. [Kwestia głosowa [smalltalk_10612_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=smalltalk_10612_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1003. [Kwestia głosowa [smalltalk_10612_1] (Chatter #1)] 저는… 선발의 효율이 잘 나오지 않는다고 하더라구요. 복제된 저는… 대부분 순순히 죽음을 받아들이거든요.\n그들과 저는 무엇이 달랐을까요. 의미 없는 궁금증이지만, 언젠가 한번쯤은 알고 싶네요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=smalltalk_10612_1].dlg
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Apparently I don't get that big of a boost from getting put through the Hatchery. Most of my clones are so... ready to accept their deaths.\nI wonder what differentiates me from the rest of me. It's a meaningless question, but I'd like to know the answer anyway.
   PL:
1004. [Kwestia głosowa [smalltalk_10612_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=smalltalk_10612_2].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1005. [Kwestia głosowa [smalltalk_10612_2] (Chatter #2)] 제 1무리를 제외하면 각 무리 간의 무력 차이는 거의 없어요~ 서로의 역할이 다를 뿐이죠. 그렇기 때문에… 한 지역을 봉쇄하고, 그곳에 있는 걸 섬멸하는 의뢰에선 제 2무리도, 제 3무리도… 저희보다 유능하지 못할 거랍니다. 아마도요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=smalltalk_10612_2].dlg
   limit: do 350 znaków
   EN: There isn't much strength difference between Packs except for the 1st Pack~ We just have different roles to fulfill. We're probably better than both the 2nd and the 3rd Pack when it comes to locking down an extermination zone and killing everything in the area. Probably.
   PL:
1006. [Kwestia głosowa [smalltalk_10612_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=smalltalk_10612_3].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1007. [Kwestia głosowa [smalltalk_10612_3] (Chatter #3)] 날개의 직원, 협회의 해결사와 저희의 다른 점은… 역시 마음가짐이라고 생각해요. 그분들은 소속감이나 각자의 이권에 묶여있지만… 저희는 돈만 충분히 준다면, 어떤 일이라도 하거든요. 네, 정말 어떤 일이든지요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=smalltalk_10612_3].dlg
   limit: do 430 znaków
   EN: The difference between us and Wing employees and Association Fixers is... probably the attitudes we have toward our respective jobs. They're bound by something, like a sense of belonging or, more simply, individual interests, but we'll do anything as long as we get paid a sufficient amount for the task. Yeah, we'll do literally <i>anything</i>.
   PL:
1008. [Kwestia głosowa [smalltalk_10612_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=smalltalk_10612_4].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1009. [Kwestia głosowa [smalltalk_10612_4] (Post-Uptie Chat 1)] 그저 흐르는 대로 받아들이면 세상 어려울 게 없다고 생각했지요.\n그런데 여기서는 받아들이는 것만으로도 머리를 뚫고 자라나는 뿔이 신경을 갉아 먹어요. 무엇도 참을 수 없을 만큼 계속…
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=smalltalk_10612_4].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I didn't think there'd be anything difficult in life as long as I accepted the way the world flowed.\nBut here, even acceptance makes the antlers take root and grow from my head, pulling away at the nerves. And it makes everything so... unbearable...
   PL:
1010. [Kwestia głosowa [smalltalk_10612_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=smalltalk_10612_5].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1011. [Kwestia głosowa [smalltalk_10612_5] (Post-Uptie Chat 2)] 전장에서는 저희 순록과 얽혀 싸우는 걸 추천드리지 않는다고 누누이 말씀드렸잖아요. 그러게 왜 가까이 다가와서는… 하. 정신줄 놓고 걸리적거리는지.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=smalltalk_10612_5].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I told you time and again that it's not a good idea to stick too close to the Reindeer when on a mission.\nIs that simple idea so hard to understand...? Haah. What are you, a headless chicken? Quit getting in my way.
   PL:
1012. [Kwestia głosowa [neglect_10612_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=neglect_10612_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1013. [Kwestia głosowa [neglect_10612_1] (Idle)] 하하. 쉬게 해주시는 건가요? …고마워요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=neglect_10612_1].dlg
   limit: do 120 znaków
   EN: Ha ha. Do I get to rest now? ... Thank you.
   PL:
1014. [Kwestia głosowa [gacksung_10612_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=gacksung_10612_1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1015. [Kwestia głosowa [gacksung_10612_1] (Uptying)] 초조해하면 안 돼… 버티려면 생각을 비워야… 큭! 저리 꺼져!
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=gacksung_10612_1].dlg
   limit: do 120 znaków
   EN: Don't be anxious... don't be... I have to empty my thoughts to endure this— Agh! Get lost!
   PL:
1016. [Kwestia głosowa [formation_10612_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=formation_10612_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1017. [Kwestia głosowa [formation_10612_1] (Deployment)] 120번 홍루. 준비는 끝냈어요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=formation_10612_1].dlg
   limit: do 120 znaków
   EN: Hong Lu #120. Ready to deploy.
   PL:
1018. [Kwestia głosowa [battleentry_10612_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battleentry_10612_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1019. [Kwestia głosowa [battleentry_10612_1] (Stage Entry)] 여기는 순록. 섬멸 지역 진입했어요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battleentry_10612_1].dlg
   limit: do 120 znaków
   EN: Reindeer here. Entering extermination zone.
   PL:
1020. [Kwestia głosowa [battle_select_10612_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_select_10612_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1021. [Kwestia głosowa [battle_select_10612_1] (Viewed in Battle)] 조금만 조용히… 으윽! 할 말 있으면 전투 전에 미리 하라고 했잖아!
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_select_10612_1].dlg
   limit: do 120 znaków
   EN: Can you please be quie— Nngh! Why the hell did you wait until now to call me up?!
   PL:
1022. [Kwestia głosowa [battle_endcommand_10612_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_endcommand_10612_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1023. [Kwestia głosowa [battle_endcommand_10612_1] (Commencing Attack)] 집속 뿔… 뇌파 충전.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_endcommand_10612_1].dlg
   limit: do 120 znaków
   EN: Focusing Antlers... Brainwave Charge.
   PL:
1024. [Kwestia głosowa [battle_enemy_break_10612_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_enemy_break_10612_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1025. [Kwestia głosowa [battle_enemy_break_10612_1] (Enemy Stagger)] 제발… 조용히…
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_enemy_break_10612_1].dlg
   limit: do 120 znaków
   EN: Please... shut up...
   PL:
1026. [Kwestia głosowa [battle_break_10612_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_break_10612_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1027. [Kwestia głosowa [battle_break_10612_1] (Staggered)] 흐흐… 흐핫… 히힉…
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_break_10612_1].dlg
   limit: do 120 znaków
   EN: <i>Hehheh... Hehaha... Heeheeeheee...</i>
   PL:
1028. [Kwestia głosowa [battle_kill_10612_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_kill_10612_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1029. [Kwestia głosowa [battle_kill_10612_1] (Enemy Killed)] …한결 낫네요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_kill_10612_1].dlg
   limit: do 120 znaków
   EN: ... Much better.
   PL:
1030. [Kwestia głosowa [battle_dead_10612_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_dead_10612_1].desc
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1031. [Kwestia głosowa [battle_dead_10612_1] (Death)] 하핫… 나중에 또 보자구요. 무리는… 다시 몰려올 테니까.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_dead_10612_1].dlg
   limit: do 120 znaków
   EN: Haha... I'll seeya later. The Pack... it'll come back in a stampede in no time.
   PL:
1032. [Kwestia głosowa [choice_success_p_10612_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=choice_success_p_10612_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1033. [Kwestia głosowa [choice_success_p_10612_2] (Check Passed)] 이걸로 됐나요? 그럼… 어서 의뢰를 끝내는 게 좋을 것 같아요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=choice_success_p_10612_2].dlg
   limit: do 120 znaków
   EN: Good enough for you? Then... let's hurry up with the contract.
   PL:
1034. [Kwestia głosowa [choice_fail_n_10612_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=choice_fail_n_10612_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1035. [Kwestia głosowa [choice_fail_n_10612_1] (Check Failed)] 큭… 좀 제대로 명령하지 그러셨어요.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=choice_fail_n_10612_1].dlg
   limit: do 120 znaków
   EN: Gah... Can't you relay a proper command for once?
   PL:
1036. [Kwestia głosowa [battle_clear_10612_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_clear_10612_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1037. [Kwestia głosowa [battle_clear_10612_1] (Victory Cry)] 순록 몇 마리가 죽긴 했지만… 이 정도면 살처분은 피했네요~ 이만 돌아가서 새로운 순록들을 맞이할까요, 사령관님.
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_clear_10612_1].dlg
   limit: do 170 znaków
   EN: Some of the herd was lost, but... hey, at least we won't be getting culled~ Shall we return to greet the new Reindeer, Commander?
   PL:
1038. [Kwestia głosowa [battle_clear_ex_10612_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_clear_ex_10612_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1039. [Kwestia głosowa [battle_clear_ex_10612_1] (Extra Conditions Fulfilled)] 하하… 하하… 하… 휴우. 위험했네요. 임무를 완수하고도 미쳐서 처분당하는 줄 알았다니까요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_clear_ex_10612_1].dlg
   limit: do 160 znaków
   EN: Ha ha... ha ha... ha... Whew. That was close. I was worried they'd cull me for insanity regardless of the mission's success.
   PL:
1040. [Kwestia głosowa [battle_defeat_10612_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_defeat_10612_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1041. [Kwestia głosowa [battle_defeat_10612_1] (Defeat Wail)] 어라? 머리가 맑은 것도 그렇고… 눈 뜬 곳이 부화장인 걸 보니… '저'는 임무에 실패한 모양이네요?
   źródło: PersonalityVoiceDlg/Voice_Honglu_RCorp_10612.json :: dataList[id=battle_defeat_10612_1].dlg
   limit: do 130 znaków
   EN: Huh? No headache...? And... am I back at the Hatchery...? Looks like 'I' failed the mission, huh?
   PL:
