# Grzesznik #02: Faust — Tożsamości, umiejętności, pasywki i głos (część a) — Limbus Company

Kompletny zestaw kart Tożsamości postaci **Faust** (파우스트) wraz z umiejętnościami na ulepszeniach 1–4, efektami monet, pasywkami i kwestiami głosowymi.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Grzesznik #02: Faust (파우스트)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 파우스트
   źródło: Characters.json :: dataList[id=2].name
   limit: do 40 znaków
   EN: Faust
   PL:
2. [Akta więźnia — nazwa] 파우스트
   źródło: IntroduceCharacter.json :: dataList[id=파우스트].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
3. [Akta więźnia — opis] Limbus Company의 버스인 메피스토펠레스의 엔진을 개발한 수감자입니다.\n도시 내에 대등히 지식과 지혜를 겨룰 수 있는 자는 없을 거라고 스스로\n주장하지만, 틀린 말도 아닙니다. 관리자님을 대할 때 어쩔 수 없이 말을 섞는\n것뿐이라는 수감자의 태도가 기분 나쁠 수도 있습니다. 모든 사람에게도\n드러나지 않는 거만한 행동을 취하기에 개선의 가능성은 없으므로\n대충 고개 끄덕이는 것을 권장합니다. 그 누구보다도 천재적이지만 우리는\n이것의 사용법을 모릅니다. 어쩌면 관리자님이 알아낼 수도 있을지도요?
   źródło: IntroduceCharacter.json :: dataList[id=파우스트].description
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Sinner who developed the engine of Mephistopheles, the bus operated by Limbus Company.\nShe claims that there is no one in the City who could rival her library of knowledge and wisdom,\nand she isn't necessarily wrong.\nYou might find her high and mighty attitude when she allows you to converse with her displeasing,\nbut as seen with how she treats everyone with subtle gestures of arrogance, there is no hope of her parting with it, ever.\nWe recommend simply nodding once and getting over it.\nEven though she has an unparalleled genius, we can't quite figure out how to use this one.\nPerhaps you could be the one to find out?
   PL: Grzesznica, która opracowała silnik Mephistophelesa, autobusu Limbus Company.\nTwierdzi, że w całym Mieście nikt nie dorównuje jej wiedzą ani mądrością,\ni nie ma w tym przesady. Może pana razić jej postawa, jakby rozmawiała\nz Kierownikiem wyłącznie z konieczności. Ponieważ tę samą wyniosłość,\nskrywaną przed światem, okazuje wszystkim, nie ma szans na poprawę;\nzalecamy po prostu kiwnąć głową. To geniusz jak nikt inny, ale my\nnie wiemy, jak z niego korzystać. Może to pan odkryje?

## [0] LCB Sinner — Faust — LCB 수감자
- ID Tożsamości: `10201` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 84 · szybkość: 1–3 / 2–3 / 2–4 / 2–4
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: —

4. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10201].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL:
5. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10201].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10201].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Karta Tożsamości — opis] 파우스트의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10201].desc
   limit: do 120 znaków
   EN: Faust’s 1st Identity
   PL:
8. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 내려베기
   źródło: Skills.json :: dataList[id=1020101].levelList[level=1].name ; dataList[id=1020101].levelList[level=2].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Downward Slash
   PL:
9. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마비 1 부여
   źródło: Skills.json :: dataList[id=1020101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Paralysis]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttackHead] Inflict 1 [Paralysis]
   PL:
10. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마비 1 부여
   źródło: Skills.json :: dataList[id=1020101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 1 [Paralysis]
   PL:
11. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 올려베기
   źródło: Skills.json :: dataList[id=1020102].levelList[level=1].name ; dataList[id=1020102].levelList[level=2].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Upward Slash
   PL:
12. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 공격 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1020102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [AttackDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttackHead] Inflict 2 [AttackDown] next turn
   PL:
13. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 레벨 감소 3 부여
   źródło: Skills.json :: dataList[id=1020102].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 3 [AttackDown] next turn
   PL:
14. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 후벼찌르기
   źródło: Skills.json :: dataList[id=1020103].levelList[level=3].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 7 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Drilling Stab
   PL:
15. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1020103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Reduction]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttackHead] Inflict 1 [Reduction] next turn
   PL:
16. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1020103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] next turn
   PL:
17. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1020104].levelList[level=1].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 2 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL:
18. [Pasywka bojowa (od ulepszenia 1, rezonans 2× Pride) — nazwa] 분석
   źródło: Passives.json :: dataList[id=1020101].name
   limit: do 40 znaków
   EN: Analytic Eye
   PL:
19. [Pasywka bojowa (od ulepszenia 1, rezonans 2× Pride) — opis] 부정적인 효과가 걸려있는 대상에게 가하는 피해량 +10%
   źródło: Passives.json :: dataList[id=1020101].desc
   limit: do 120 znaków
   EN: Deal +10% damage to targets that have negative status effects
   PL:
20. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — nazwa] 관찰
   źródło: Passives.json :: dataList[id=1020121].name
   limit: do 40 znaków
   EN: Keen Observation
   PL:
21. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — opis] 최대 체력이 가장 높은 아군 1명 공격 적중 시 25% 확률로 공격 레벨 감소 2 부여
   źródło: Passives.json :: dataList[id=1020121].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDown]
   znaczenie tagów: [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: 1 ally that has the highest max HP inflicts 2 [AttackDown] at 25% chance on hit
   PL:
22. [Kwestia głosowa [get_10201_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=get_10201_1].desc
   limit: do 120 znaków
   EN: Identity Acquisition
   PL:
23. [Kwestia głosowa [get_10201_1] (Identity Acquisition)] 파우스트예요. 당신이 인생에서 한 번 마주칠까 말까 하는 천재죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=get_10201_1].dlg
   limit: do 120 znaków
   EN: It’s Faust. A genius with whom you’re lucky to cross paths even once in your life.
   PL:
24. [Kwestia głosowa [lobby_morning_10201_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=lobby_morning_10201_1].desc
   limit: do 120 znaków
   EN: Morning Greeting
   PL:
25. [Kwestia głosowa [lobby_morning_10201_1] (Morning Greeting)] 옛날부터 3시간 이상의 수면을 취하면 저절로 눈이 떠지곤 했어요. 자연스러운 현상인 줄 알았는데 모든 분들이 그렇진 않더군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=lobby_morning_10201_1].dlg
   limit: do 200 znaków
   EN: I would always get up after three hours of sleep. I thought it was a natural phenomenon, but I later learned it wasn’t the case for every individual.
   PL:
26. [Kwestia głosowa [lobby_noon_10201_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=lobby_noon_10201_1].desc
   limit: do 120 znaków
   EN: Afternoon Greeting
   PL:
27. [Kwestia głosowa [lobby_noon_10201_1] (Afternoon Greeting)] 파우스트는 잠깐의 햇빛을 쬐는 행위를 유용한 활동이라고 여겨요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=lobby_noon_10201_1].dlg
   limit: do 120 znaków
   EN: Faust considers short periods of exposure to sunlight to be a useful activity.
   PL:
28. [Kwestia głosowa [lobby_night_10201_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=lobby_night_10201_1].desc
   limit: do 120 znaków
   EN: Evening Greeting
   PL:
29. [Kwestia głosowa [lobby_night_10201_1] (Evening Greeting)] 취미라는 걸 구태여 만들진 않지만, 한때는 별을 관측하는 걸 즐기곤 했어요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=lobby_night_10201_1].dlg
   limit: do 120 znaków
   EN: Though I don’t bother myself much with hobbies, I once enjoyed stargazing.
   PL:
30. [Kwestia głosowa [smalltalk_10201_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=smalltalk_10201_1].desc
   limit: do 120 znaków
   EN: Chatter #1
   PL:
31. [Kwestia głosowa [smalltalk_10201_1] (Chatter #1)] …일단 불러놓고 할 말을 생각하시는 유형이라면, 문서 전달을 추천드려요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=smalltalk_10201_1].dlg
   limit: do 180 znaków
   EN: …If you’re the type of person who likes to summon others before considering what to say, I would suggest using documents to communicate.
   PL:
32. [Kwestia głosowa [smalltalk_10201_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=smalltalk_10201_2].desc
   limit: do 120 znaków
   EN: Chatter #2
   PL:
33. [Kwestia głosowa [smalltalk_10201_2] (Chatter #2)] 수감자들 별로 대화의 수준 차이를 다르게 적용할지 생각 중이에요. 두 번 이상씩 말을 반복하는 건 비효율적이니까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=smalltalk_10201_2].dlg
   limit: do 170 znaków
   EN: I’m considering adjusting my level of speech for different Sinners. Repeating myself twice or more can be rather inefficient.
   PL:
34. [Kwestia głosowa [smalltalk_10201_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=smalltalk_10201_3].desc
   limit: do 120 znaków
   EN: Chatter #3
   PL:
35. [Kwestia głosowa [smalltalk_10201_3] (Chatter #3)] 단테, 모든 답을 알고 있다는 뜻이 제가 모든 질문에 대답해줄 수 있다는 뜻은 아니에요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=smalltalk_10201_3].dlg
   limit: do 160 znaków
   EN: Dante, I want you to understand that omniscience does not necessarily mean a willingness to answer your every question.
   PL:
36. [Kwestia głosowa [neglect_10201_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=neglect_10201_1].desc
   limit: do 120 znaków
   EN: Idle
   PL:
37. [Kwestia głosowa [neglect_10201_1] (Idle)] 잠깐의 일탈 정도는 허용범위에요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=neglect_10201_1].dlg
   limit: do 120 znaków
   EN: Brief deviations are within permitted ranges.
   PL:
38. [Kwestia głosowa [formation_10201_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=formation_10201_1].desc
   limit: do 120 znaków
   EN: Deployment
   PL:
39. [Kwestia głosowa [formation_10201_1] (Deployment)] 따라가겠어요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=formation_10201_1].dlg
   limit: do 120 znaków
   EN: I’ll tag along.
   PL:
40. [Kwestia głosowa [battleentry_10201_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battleentry_10201_1].desc
   limit: do 120 znaków
   EN: Stage Entry
   PL:
41. [Kwestia głosowa [battleentry_10201_1] (Stage Entry)] 따라갈 준비는 끝났습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battleentry_10201_1].dlg
   limit: do 120 znaków
   EN: I’m ready to accompany you.
   PL:
42. [Kwestia głosowa [battle_select_10201_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_select_10201_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle
   PL:
43. [Kwestia głosowa [battle_select_10201_1] (Viewed in Battle)] 무슨 일인가요? 관리자님.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_select_10201_1].dlg
   limit: do 120 znaków
   EN: What is it, Manager?
   PL:
44. [Kwestia głosowa [battle_endcommand_10201_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_endcommand_10201_1].desc
   limit: do 120 znaków
   EN: Commencing Attack
   PL:
45. [Kwestia głosowa [battle_endcommand_10201_1] (Commencing Attack)] 행동을 개시합니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_endcommand_10201_1].dlg
   limit: do 120 znaków
   EN: Commencing action.
   PL:
46. [Kwestia głosowa [battle_enemy_break_10201_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_enemy_break_10201_1].desc
   limit: do 120 znaków
   EN: Enemy Stagger
   PL:
47. [Kwestia głosowa [battle_enemy_break_10201_1] (Enemy Stagger)] 지금이 기회입니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_enemy_break_10201_1].dlg
   limit: do 120 znaków
   EN: An opportunity has arrived.
   PL:
48. [Kwestia głosowa [battle_break_10201_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_break_10201_1].desc
   limit: do 120 znaków
   EN: Staggered
   PL:
49. [Kwestia głosowa [battle_break_10201_1] (Staggered)] 윽!
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_break_10201_1].dlg
   limit: do 120 znaków
   EN: Ugh!
   PL:
50. [Kwestia głosowa [battle_kill_10201_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_kill_10201_1].desc
   limit: do 120 znaków
   EN: Enemy Killed
   PL:
51. [Kwestia głosowa [battle_kill_10201_1] (Enemy Killed)] 당연한 결과죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_kill_10201_1].dlg
   limit: do 120 znaków
   EN: An obvious outcome.
   PL:
52. [Kwestia głosowa [battle_allydead_10201_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_allydead_10201_1].desc
   limit: do 120 znaków
   EN: Ally Death
   PL:
53. [Kwestia głosowa [battle_allydead_10201_1] (Ally Death)] 효율적이진 않네요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_allydead_10201_1].dlg
   limit: do 120 znaków
   EN: That wasn’t the most efficient.
   PL:
54. [Kwestia głosowa [choice_success_p_10201_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=choice_success_p_10201_1].desc
   limit: do 120 znaków
   EN: Check Passed
   PL:
55. [Kwestia głosowa [choice_success_p_10201_1] (Check Passed)] 성공에 연연해하지 마세요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=choice_success_p_10201_1].dlg
   limit: do 120 znaków
   EN: Try not to cling to this success.
   PL:
56. [Kwestia głosowa [choice_fail_n_10201_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=choice_fail_n_10201_1].desc
   limit: do 120 znaków
   EN: Check Failed
   PL:
57. [Kwestia głosowa [choice_fail_n_10201_1] (Check Failed)] 실패에 연연해하지 마세요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=choice_fail_n_10201_1].dlg
   limit: do 120 znaków
   EN: Try not to dwell on this failure.
   PL:
58. [Kwestia głosowa [battle_clear_10201_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_clear_10201_1].desc
   limit: do 120 znaków
   EN: Victory Cry
   PL:
59. [Kwestia głosowa [battle_clear_10201_1] (Victory Cry)] 이런 일에 기뻐해야 할 이유가 있을까요?
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_clear_10201_1].dlg
   limit: do 120 znaków
   EN: Is there a reason to be excited over this?
   PL:
60. [Kwestia głosowa [battle_clear_ex_10201_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_clear_ex_10201_1].desc
   limit: do 120 znaków
   EN: Extra Conditions Fulfilled
   PL:
61. [Kwestia głosowa [battle_clear_ex_10201_1] (Extra Conditions Fulfilled)] 예상보다는 조금 우수해졌군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_clear_ex_10201_1].dlg
   limit: do 120 znaków
   EN: You’ve become more competent than once expected.
   PL:
62. [Kwestia głosowa [battle_defeat_10201_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_defeat_10201_1].desc
   limit: do 120 znaków
   EN: Defeat Wail
   PL:
63. [Kwestia głosowa [battle_defeat_10201_1] (Defeat Wail)] 많은 기대는 걸지 않았어요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCB_10201.json :: dataList[id=battle_defeat_10201_1].dlg
   limit: do 120 znaków
   EN: Much wasn’t expected out of you.
   PL:

## [00] W Corp. L2 Cleanup Agent — Faust — W사 2등급 정리 요원
- ID Tożsamości: `10202` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 88 · szybkość: 1–3 / 2–3 / 2–4 / 2–4
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Charge

64. [Karta Tożsamości — tytuł] W사 2등급\n정리 요원
   źródło: Personalities.json :: dataList[id=10202].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L2\nCleanup Agent
   PL:
65. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10202].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10202].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [Karta Tożsamości — opis] 파우스트의 두번째 인격
   źródło: Personalities.json :: dataList[id=10202].desc
   limit: do 120 znaków
   EN: Faust’s 2nd Identity
   PL:
68. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 에너지 순환
   źródło: Skills.json :: dataList[id=1020201].levelList[level=1].name ; dataList[id=1020201].levelList[level=2].name ; dataList[id=1020201].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Energy Cycle
   PL:
69. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 1 증가
   źródło: Skills.json :: dataList[id=1020201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +1 [Charge] Count
   PL:
70. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1020201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count
   PL:
71. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1020201].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +2 [Charge] Count
   PL:
72. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 도약
   źródło: Skills.json :: dataList[id=1020202].levelList[level=1].name ; dataList[id=1020202].levelList[level=2].name ; dataList[id=1020202].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 6 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Leap
   PL:
73. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 충전 횟수를 3 소모하여 다음 턴에 속박 4 부여
   źródło: Skills.json :: dataList[id=1020202].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1020202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Consume 3 [Charge] Count to inflict 4 [Binding] next turn
   PL:
74. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 3 증가
   źródło: Skills.json :: dataList[id=1020202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +3 [Charge] Count
   PL:
75. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 3 증가
   źródło: Skills.json :: dataList[id=1020202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +3 [Charge] Count
   PL:
76. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 과충전
   źródło: Skills.json :: dataList[id=1020203].levelList[level=3].name ; dataList[id=1020203].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 6 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Overcharge
   PL:
77. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 충전 횟수를 5 소모하여 다음 턴에 공격 위력 감소 2 부여. 마비 3 부여
   źródło: Skills.json :: dataList[id=1020203].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1020203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Reduction], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Reduction] = 공격 위력 감소 / Attack Power Down; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Consume 5 [Charge] Count to inflict 2 [Reduction] and 3 [Paralysis] next turn
   PL:
78. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 충전 횟수가 5 이상이면, 합 위력 +2
   źródło: Skills.json :: dataList[id=1020203].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 5+ [Charge] Count, Clash Power +2
   PL:
79. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1020204].levelList[level=1].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+2)
   limit: do 40 znaków
   EN: Guard
   PL:
80. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Envy) — nazwa] 자가충전
   źródło: Passives.json :: dataList[id=1020201].name
   limit: do 40 znaków
   EN: Self-charging
   PL:
81. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Envy) — opis] 공격 종료 시 충전 횟수 1 증가
   źródło: Passives.json :: dataList[id=1020201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain +1 [Charge] Count at Attack End
   PL:
82. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — nazwa] 무전
   źródło: Passives.json :: dataList[id=1020221].name
   limit: do 40 znaków
   EN: Radio Comms
   PL:
83. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — opis] 최대 체력이 가장 낮은 아군 1명 충전 횟수 얻는 값 +1
   źródło: Passives.json :: dataList[id=1020221].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: 1 ally that has the lowest max HP gains +1 [Charge] Count
   PL:
84. [Kwestia głosowa [get_10202_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=get_10202_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Kwestia głosowa [get_10202_1] (Identity Acquisition)] 신속하게… 처리해드리도록 하죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=get_10202_1].dlg
   limit: do 120 znaków
   EN: Your problems… will be dealt with posthaste.
   PL:
86. [Kwestia głosowa [lobby_morning_10202_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=lobby_morning_10202_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Kwestia głosowa [lobby_morning_10202_1] (Morning Greeting)] 파우스트는 열차 타는 걸 즐기지 않아요. 꼭 몸이 장소를 이동해야 하는 건 아니니까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=lobby_morning_10202_1].dlg
   limit: do 180 znaków
   EN: Faust doesn’t particularly enjoy locomotive travel. On a trip, it doesn’t always have to be the body that moves from one place to another.
   PL:
88. [Kwestia głosowa [lobby_noon_10202_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=lobby_noon_10202_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Kwestia głosowa [lobby_noon_10202_1] (Afternoon Greeting)] 사물의 본질을 꿰뚫는 것이 중요해요. 당신의 시계는 시계가 아니며, 워프 열차는 워프를 하지 않듯.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=lobby_noon_10202_1].dlg
   limit: do 180 znaków
   EN: It’s important to see through to the essence of things. For instance, your clock isn’t really a clock, and WARP trains don’t exactly warp.
   PL:
90. [Kwestia głosowa [lobby_night_10202_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=lobby_night_10202_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Kwestia głosowa [lobby_night_10202_1] (Evening Greeting)] 소문을 흘려듣지 마세요, 단테. 소문의 모든 시작은 한 조각의 진실로부터 나오니까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=lobby_night_10202_1].dlg
   limit: do 120 znaków
   EN: Don’t let rumors slip under your notice, Dante. Every canard starts from a crumb of truth.
   PL:
92. [Kwestia głosowa [smalltalk_10202_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=smalltalk_10202_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [Kwestia głosowa [smalltalk_10202_1] (Chatter #1)] 사실 파우스트는 청소를 즐겨하지는 않았어요. 오히려 반대였죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=smalltalk_10202_1].dlg
   limit: do 120 znaków
   EN: To tell you the truth, Faust did not enjoy cleaning. It was the opposite, rather.
   PL:
94. [Kwestia głosowa [smalltalk_10202_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=smalltalk_10202_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Kwestia głosowa [smalltalk_10202_2] (Chatter #2)] 결과만 우수하다면 과정은 아무런 상관이 없는 것일까요? 당신이 죽을듯한 고통과 등가교환 하여 그들을 되살리는 것처럼.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=smalltalk_10202_2].dlg
   limit: do 140 znaków
   EN: Do the ends really justify the means? Is the excruciating pain you bear really worth bringing them back?
   PL:
96. [Kwestia głosowa [smalltalk_10202_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=smalltalk_10202_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Kwestia głosowa [smalltalk_10202_3] (Chatter #3)] 제게 비해서 당신은 스스로의 처지에 대해 질문이 없는 편이군요. 아니면 그저 받아들이기로 결심한 건가요?
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=smalltalk_10202_3].dlg
   limit: do 150 znaków
   EN: You don’t seem to be as inquisitive of your situation as I am. Rather, have you decided to accept it, perhaps?
   PL:
98. [Kwestia głosowa [smalltalk_10202_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=smalltalk_10202_4].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 1
   PL:
99. [Kwestia głosowa [smalltalk_10202_4] (Post-Uptie Chat 1)] 언젠간 도시의 모든 비밀들을 모아 하나의 그림으로 만들어보고 싶어요. 그런 다음 찬찬히 감상하는 거죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=smalltalk_10202_4].dlg
   limit: do 160 znaków
   EN: One day, I plan to collect every secret of the City and paint them all on a canvas. It’ll be something to appreciate.
   PL:
100. [Kwestia głosowa [smalltalk_10202_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=smalltalk_10202_5].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 2
   PL:
101. [Kwestia głosowa [smalltalk_10202_5] (Post-Uptie Chat 2)] 파우스트는 도시 이곳저곳을 돌아다니는 걸 선호해요. 이곳만큼 적합한 곳은 없는 거죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=smalltalk_10202_5].dlg
   limit: do 130 znaków
   EN: Faust likes to travel from place to place. There is no better occupation than this in that regard.
   PL:
102. [Kwestia głosowa [neglect_10202_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=neglect_10202_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Kwestia głosowa [neglect_10202_1] (Idle)] …종종 말없이 사라지기도 하는 모양이다. 녹음 종료.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=neglect_10202_1].dlg
   limit: do 120 znaków
   EN: …They apparently disappear without notice on occasion. End of log.
   PL:
104. [Kwestia głosowa [gacksung_10202_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=gacksung_10202_1].desc
   limit: do 120 znaków
   EN: Uptying
   PL:
105. [Kwestia głosowa [gacksung_10202_1] (Uptying)] 이곳도 점점 파악되어가기 시작했어요.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=gacksung_10202_1].dlg
   limit: do 120 znaków
   EN: I’m starting to get a good grasp of this place.
   PL:
106. [Kwestia głosowa [formation_10202_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=formation_10202_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Kwestia głosowa [formation_10202_1] (Deployment)] 네, 출발하죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=formation_10202_1].dlg
   limit: do 120 znaków
   EN: Got it, let’s move.
   PL:
108. [Kwestia głosowa [battleentry_10202_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battleentry_10202_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Kwestia głosowa [battleentry_10202_1] (Stage Entry)] 파우스트. 전투 시작합니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battleentry_10202_1].dlg
   limit: do 120 znaków
   EN: Faust, commencing battle.
   PL:
110. [Kwestia głosowa [battle_select_10202_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_select_10202_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [Kwestia głosowa [battle_select_10202_1] (Viewed in Battle)] 지금은 조금 바쁩니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_select_10202_1].dlg
   limit: do 120 znaków
   EN: Things are rather busying at the moment.
   PL:
112. [Kwestia głosowa [battle_endcommand_10202_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_endcommand_10202_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Kwestia głosowa [battle_endcommand_10202_1] (Commencing Attack)] 신속히 처리하죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_endcommand_10202_1].dlg
   limit: do 120 znaków
   EN: It will be quick work.
   PL:
114. [Kwestia głosowa [battle_enemy_break_10202_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_enemy_break_10202_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Kwestia głosowa [battle_enemy_break_10202_1] (Enemy Stagger)] 약점 파악 완료.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_enemy_break_10202_1].dlg
   limit: do 120 znaków
   EN: Weakness noted.
   PL:
116. [Kwestia głosowa [battle_break_10202_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_break_10202_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Kwestia głosowa [battle_break_10202_1] (Staggered)] 칫!
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_break_10202_1].dlg
   limit: do 120 znaków
   EN: Tch!
   PL:
118. [Kwestia głosowa [battle_kill_10202_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_kill_10202_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Kwestia głosowa [battle_kill_10202_1] (Enemy Killed)] 처리했어요.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_kill_10202_1].dlg
   limit: do 120 znaków
   EN: The job is done.
   PL:
120. [Kwestia głosowa [battle_allydead_10202_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_allydead_10202_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Kwestia głosowa [battle_allydead_10202_1] (Ally Death)] 열차를 싫어하는 이유에요.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_allydead_10202_1].dlg
   limit: do 120 znaków
   EN: This is why I dislike trains.
   PL:
122. [Kwestia głosowa [choice_success_p_10202_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=choice_success_p_10202_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Kwestia głosowa [choice_success_p_10202_1] (Check Passed)] 파우스트 임무 완료.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=choice_success_p_10202_1].dlg
   limit: do 120 znaków
   EN: Faust, mission accomplished.
   PL:
124. [Kwestia głosowa [choice_fail_n_10202_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=choice_fail_n_10202_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Kwestia głosowa [choice_fail_n_10202_1] (Check Failed)] 신속하게 하려 했기 때문일까요?
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=choice_fail_n_10202_1].dlg
   limit: do 120 znaków
   EN: Perhaps we were too hasty?
   PL:
126. [Kwestia głosowa [battle_clear_10202_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_clear_10202_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Kwestia głosowa [battle_clear_10202_1] (Victory Cry)] 다음엔 좀 더 신속하게 끝내보죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_clear_10202_1].dlg
   limit: do 120 znaków
   EN: Let’s try and make it quicker next time.
   PL:
128. [Kwestia głosowa [battle_clear_ex_10202_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_clear_ex_10202_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Kwestia głosowa [battle_clear_ex_10202_1] (Extra Conditions Fulfilled)] 파우스트, 이번 작전도 완벽히 종료.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_clear_ex_10202_1].dlg
   limit: do 120 znaków
   EN: Faust, reporting in with another flawless success.
   PL:
130. [Kwestia głosowa [battle_defeat_10202_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_defeat_10202_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Kwestia głosowa [battle_defeat_10202_1] (Defeat Wail)] 몇몇 분들의 불필요한 움직임이 있었어요.
   źródło: PersonalityVoiceDlg/Voice_Faust_WCorp6_10202.json :: dataList[id=battle_defeat_10202_1].dlg
   limit: do 120 znaków
   EN: Some personnel made rather unnecessary movements.
   PL:

## [00] Lobotomy Corp. Remnant — Faust — 살아남은 로보토미 직원
- ID Tożsamości: `10203` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 1 · HP bazowe: 69 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture, Poise

132. [Karta Tożsamości — tytuł] 살아남은 로보토미 직원
   źródło: Personalities.json :: dataList[id=10203].title
   limit: do 40 znaków
   EN: Lobotomy Corp. Remnant
   PL:
133. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10203].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10203].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Karta Tożsamości — opis] 파우스트의 세번째 인격
   źródło: Personalities.json :: dataList[id=10203].desc
   limit: do 120 znaków
   EN: Faust’s 3rd Identity
   PL:
136. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 단격
   źródło: Skills.json :: dataList[id=1020301].levelList[level=1].name ; dataList[id=1020301].levelList[level=2].name ; dataList[id=1020301].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Sole Strike
   PL:
137. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1020301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 1 [Burst]
   PL:
138. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1020301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
139. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1020301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL:
140. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 깊게베기
   źródło: Skills.json :: dataList[id=1020302].levelList[level=1].name ; dataList[id=1020302].levelList[level=2].name ; dataList[id=1020302].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Deep Cuts
   PL:
141. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath] next turn
   PL:
142. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 신속 2 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Agility]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttackHead] Gain 2 [Agility] next turn
   PL:
144. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath] next turn
   PL:
145. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 신속 4 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1020302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 4 [Agility] next turn
   PL:
147. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1020302].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 기회 노리기
   źródło: Skills.json :: dataList[id=1020303].levelList[level=3].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 2 (+8)
   limit: do 40 znaków
   EN: Opportunistic Slash
   PL:
149. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이전 턴에 피해를 받지 않은 경우 코인 위력 +3
   źródło: Skills.json :: dataList[id=1020303].levelList[level=3].desc
   limit: do 120 znaków
   EN: If this unit took no damage last turn, Coin Power +3
   PL:
150. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 5 부여
   źródło: Skills.json :: dataList[id=1020303].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 5 [Burst]
   PL:
151. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1020304].levelList[level=1].name
   kontekst: grzech: Envy · typ: obrona: unik · moc bazowa: 3 · monety: 1 (+10)
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Lust) — nazwa] 각오
   źródło: Passives.json :: dataList[id=1020301].name
   limit: do 40 znaków
   EN: Resolution
   PL:
153. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Lust) — opis] 다음 턴 시작 시 호흡 횟수가 4 이상이면 신속 2를 얻음
   źródło: Passives.json :: dataList[id=1020301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath], [Agility]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: At the next Turn Start, at 4+ [Breath] Count, gain 2 [Agility]
   PL:
154. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Lust) — nazwa] 지지
   źródło: Passives.json :: dataList[id=1020321].name
   limit: do 40 znaków
   EN: Backing
   PL:
155. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Lust) — opis] 최대 체력이 가장 낮은 아군 1명 수비 스킬의 최종 위력 +2
   źródło: Passives.json :: dataList[id=1020321].desc
   limit: do 120 znaków
   EN: 1 ally that has the lowest max HP gains Final Power +2 for its Defense Skills
   PL:
156. [Kwestia głosowa [get_10203_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=get_10203_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Kwestia głosowa [get_10203_1] (Identity Acquisition)] 파우스트예요, 잘 부탁드려요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=get_10203_1].dlg
   limit: do 120 znaków
   EN: This is Faust, a pleasure to meet you.
   PL:
158. [Kwestia głosowa [lobby_morning_10203_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=lobby_morning_10203_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Kwestia głosowa [lobby_morning_10203_1] (Morning Greeting)] 항상 주위를 심도 있게 관찰하는 버릇이 생겼어요. 지금 당신이 어디를 갈지도, 파악은 되어있어요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=lobby_morning_10203_1].dlg
   limit: do 140 znaków
   EN: I’d gained a habit of carefully observing my surroundings. I’ve got your current destination down, too.
   PL:
160. [Kwestia głosowa [lobby_noon_10203_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=lobby_noon_10203_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Kwestia głosowa [lobby_noon_10203_1] (Afternoon Greeting)] 모두가 긴장을 놓아도 되는 시간이 있다는 건 이로운 일 이에요. 정신 건강을 관리하는 것은 생각보다 제일 까다로우니까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=lobby_noon_10203_1].dlg
   limit: do 170 znaków
   EN: It’s beneficial to allocate a time of the day when all of us can relax. Mental health management can be surprisingly difficult.
   PL:
162. [Kwestia głosowa [lobby_night_10203_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=lobby_night_10203_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Kwestia głosowa [lobby_night_10203_1] (Evening Greeting)] 어두운 것엔 익숙해요. 정전이 된 좁은 방에 홀로 59일을 있어본 적도 있어요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=lobby_night_10203_1].dlg
   limit: do 120 znaków
   EN: I’m used to darkness. One time, I stayed alone in a cramped room with no power for 59 days.
   PL:
164. [Kwestia głosowa [smalltalk_10203_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=smalltalk_10203_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Kwestia głosowa [smalltalk_10203_1] (Chatter #1)] 예전 회사는 지하에 있었어요. 들어오는 빛이라고는 싸늘한 인공조명이 다였죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=smalltalk_10203_1].dlg
   limit: do 120 znaków
   EN: My old workplace was underground. A cold artificial light was all we had.
   PL:
166. [Kwestia głosowa [smalltalk_10203_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=smalltalk_10203_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Kwestia głosowa [smalltalk_10203_2] (Chatter #2)] 대부분의 이치들을 이해하고자 노력하는 저이지만… 세상에는 이해를 포기해야 하는 존재들도 있더군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=smalltalk_10203_2].dlg
   limit: do 150 znaków
   EN: While I strive to comprehend most laws and denizens of the world… Some things are simply not meant to be understood.
   PL:
168. [Kwestia głosowa [smalltalk_10203_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=smalltalk_10203_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Kwestia głosowa [smalltalk_10203_3] (Chatter #3)] …그곳에서도 관리자님이 계셨어요. 비록 이렇게 얼굴을 마주 보면서 대화를 해본 적은 없지만. 생소하면서도… 나쁘지 않네요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=smalltalk_10203_3].dlg
   limit: do 180 znaków
   EN: …My old job had a manager, too. Though I never had a chance to talk with them directly like I do now. This is new to me… but it isn’t bad.
   PL:
170. [Kwestia głosowa [smalltalk_10203_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=smalltalk_10203_4].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Kwestia głosowa [smalltalk_10203_4] (Post-Uptie Chat 1)] 어제, 맞은편에서 식사를 했던 동료가 그 다음 날 시체가 되어 처분해야 할 때가 종종 있었어요. 적어도 여긴… 그러지 않는군요. 네, 나쁘진 않아요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=smalltalk_10203_4].dlg
   limit: do 220 znaków
   EN: I often had to clean up the bodies of coworkers with whom I had dined the day before. Here… I don’t experience such things, at least. Yes, I’d say it’s not too bad here.
   PL:
172. [Kwestia głosowa [smalltalk_10203_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=smalltalk_10203_5].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Kwestia głosowa [smalltalk_10203_5] (Post-Uptie Chat 2)] 참을 수 없는 고통, 정체조차 알 수 없는 괴물, 죽어가는 동료… 제가 두려운 건 이런 것들이 아니에요. 제가 두려워하는 건…
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=smalltalk_10203_5].dlg
   limit: do 130 znaków
   EN: Intolerable pain, unknowable monsters, dying colleagues… Those aren’t what I fear. Rather, it’s…
   PL:
174. [Kwestia głosowa [neglect_10203_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=neglect_10203_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Kwestia głosowa [neglect_10203_1] (Idle)] 갑작스러운 실종. 익숙해요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=neglect_10203_1].dlg
   limit: do 120 znaków
   EN: A sudden disappearance, often seen.
   PL:
176. [Kwestia głosowa [gacksung_10203_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=gacksung_10203_1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Kwestia głosowa [gacksung_10203_1] (Uptying)] 이번에도 노력은 해보죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=gacksung_10203_1].dlg
   limit: do 120 znaków
   EN: I suppose I’ll put forth some effort one more time.
   PL:
178. [Kwestia głosowa [formation_10203_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=formation_10203_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Kwestia głosowa [formation_10203_1] (Deployment)] 전 준비되었어요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=formation_10203_1].dlg
   limit: do 120 znaków
   EN: I’m ready.
   PL:
180. [Kwestia głosowa [battleentry_10203_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battleentry_10203_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Kwestia głosowa [battleentry_10203_1] (Stage Entry)] 잘 되었으면 좋겠네요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battleentry_10203_1].dlg
   limit: do 120 znaków
   EN: Hopefully this goes well.
   PL:
182. [Kwestia głosowa [battle_select_10203_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_select_10203_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Kwestia głosowa [battle_select_10203_1] (Viewed in Battle)] 어떤 실수를 했나요?
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_select_10203_1].dlg
   limit: do 120 znaków
   EN: What was done wrong?
   PL:
184. [Kwestia głosowa [battle_endcommand_10203_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_endcommand_10203_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Kwestia głosowa [battle_endcommand_10203_1] (Commencing Attack)] 지금은 두렵지 않아요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_endcommand_10203_1].dlg
   limit: do 120 znaków
   EN: There’s no fear right now.
   PL:
186. [Kwestia głosowa [battle_enemy_break_10203_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_enemy_break_10203_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Kwestia głosowa [battle_enemy_break_10203_1] (Enemy Stagger)] 다음을 부탁해요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_enemy_break_10203_1].dlg
   limit: do 120 znaków
   EN: You’re up next.
   PL:
188. [Kwestia głosowa [battle_break_10203_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_break_10203_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Kwestia głosowa [battle_break_10203_1] (Staggered)] 앗!
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_break_10203_1].dlg
   limit: do 120 znaków
   EN: Ah!
   PL:
190. [Kwestia głosowa [battle_kill_10203_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_kill_10203_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Kwestia głosowa [battle_kill_10203_1] (Enemy Killed)] 두렵진 않네요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_kill_10203_1].dlg
   limit: do 120 znaków
   EN: That wasn’t scary.
   PL:
192. [Kwestia głosowa [battle_allydead_10203_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_allydead_10203_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Kwestia głosowa [battle_allydead_10203_1] (Ally Death)] 당신이 있어 다행이에요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_allydead_10203_1].dlg
   limit: do 120 znaków
   EN: It’s good to have had you, at least.
   PL:
194. [Kwestia głosowa [choice_success_p_10203_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=choice_success_p_10203_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Kwestia głosowa [choice_success_p_10203_1] (Check Passed)] 준비되었다면, 쉽죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=choice_success_p_10203_1].dlg
   limit: do 120 znaków
   EN: Preparation makes things easy.
   PL:
196. [Kwestia głosowa [choice_fail_n_10203_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=choice_fail_n_10203_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Kwestia głosowa [choice_fail_n_10203_1] (Check Failed)] 이런 건 익숙할 뿐이죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=choice_fail_n_10203_1].dlg
   limit: do 120 znaków
   EN: I’m all too used to this.
   PL:
198. [Kwestia głosowa [battle_clear_10203_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_clear_10203_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Kwestia głosowa [battle_clear_10203_1] (Victory Cry)] 이 정도의 전투는 쉬운 편이에요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_clear_10203_1].dlg
   limit: do 120 znaków
   EN: This is far from the hardest battle I’ve fought.
   PL:
200. [Kwestia głosowa [battle_clear_ex_10203_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_clear_ex_10203_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Kwestia głosowa [battle_clear_ex_10203_1] (Extra Conditions Fulfilled)] 어디에서나 파우스트는 우수했어요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_clear_ex_10203_1].dlg
   limit: do 120 znaków
   EN: Faust has always been competent.
   PL:
202. [Kwestia głosowa [battle_defeat_10203_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_defeat_10203_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Kwestia głosowa [battle_defeat_10203_1] (Defeat Wail)] 다음 기회라는 것이 있다는게 행운이군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Yuri_10203.json :: dataList[id=battle_defeat_10203_1].dlg
   limit: do 120 znaków
   EN: It’s fortunate that we have another chance.
   PL:

## [000] The One Who Grips — Faust — 쥐는 자
- ID Tożsamości: `10204` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 1 · HP bazowe: 66 · szybkość: 4–5 / 4–6 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Bleed

204. [Karta Tożsamości — tytuł] 쥐는 자
   źródło: Personalities.json :: dataList[id=10204].title
   limit: do 40 znaków
   EN: The One Who Grips
   PL:
205. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10204].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10204].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Karta Tożsamości — opis] 파우스트의 네번째 인격
   źródło: Personalities.json :: dataList[id=10204].desc
   limit: do 120 znaków
   EN: Faust’s 4th Identity
   PL:
208. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 광소
   źródło: Skills.json :: dataList[id=1020401].levelList[level=1].name ; dataList[id=1020401].levelList[level=2].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Cackle
   PL:
209. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WinDuel] 대상의 정신력 3 감소
   źródło: Skills.json :: dataList[id=1020401].levelList[level=1].desc ; dataList[id=1020401].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Target loses 3 SP
   PL:
210. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 못 1 부여
   źródło: Skills.json :: dataList[id=1020401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [NailPersonality]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttackHead] Inflict 1 [NailPersonality]
   PL:
211. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1020401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
212. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 못 1 부여
   źródło: Skills.json :: dataList[id=1020401].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 1 [NailPersonality]
   PL:
213. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1020401].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
214. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 쥐어짐
   źródło: Skills.json :: dataList[id=1020402].levelList[level=1].name ; dataList[id=1020402].levelList[level=2].name ; dataList[id=1020402].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: The Gripping
   PL:
215. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 못 3 부여
   źródło: Skills.json :: dataList[id=1020402].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1020402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 3 [NailPersonality]
   PL:
216. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 주시 부여
   źródło: Skills.json :: dataList[id=1020402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [MarkOfHeresy]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [MarkOfHeresy] = 주시 / Gaze
   EN: [OnSucceedAttackHead] Inflict [MarkOfHeresy] next turn
   PL:
217. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 마비 1 부여
   źródło: Skills.json :: dataList[id=1020402].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1020402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Paralysis]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttackHead] Inflict 1 [Paralysis] next turn
   PL:
218. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 주시 부여
   źródło: Skills.json :: dataList[id=1020402].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1020402].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MarkOfHeresy]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MarkOfHeresy] = 주시 / Gaze
   EN: [OnSucceedAttack] Inflict [MarkOfHeresy] next turn
   PL:
219. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 못 2 부여
   źródło: Skills.json :: dataList[id=1020402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 2 [NailPersonality]
   PL:
220. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 처단
   źródło: Skills.json :: dataList[id=1020403].levelList[level=3].name ; dataList[id=1020403].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 6 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Execution
   PL:
221. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] 이 스킬로 적 처치 시 모든 아군의 정신력을 10 회복시키고, 모든 아군에게 관통 피해량 증가, 타격 피해량 증가 1 부여
   źródło: Skills.json :: dataList[id=1020403].levelList[level=3].desc ; dataList[id=1020403].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PenetrateDamageUp], [HitDamageUp]
   znaczenie tagów: [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up
   EN: On kill, heal 10 SP for all allies and apply 1 [PenetrateDamageUp] and [HitDamageUp]
   PL:
222. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 못 2 부여
   źródło: Skills.json :: dataList[id=1020403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1020403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 못 2 부여
   źródło: Skills.json :: dataList[id=1020403].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1020403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [NailPersonality]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttackHead] Inflict 2 [NailPersonality]
   PL:
224. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 대상에게 못이 5 이상 있으면, 피해량 +50%
   źródło: Skills.json :: dataList[id=1020403].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NailPersonality]
   znaczenie tagów: [NailPersonality] = 못 / Nails
   EN: Deal +50% damage to targets that have 5+ [NailPersonality]
   PL:
225. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 대상에게 못이 5 이상 있으면, 피해량 +70%
   źródło: Skills.json :: dataList[id=1020403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NailPersonality]
   znaczenie tagów: [NailPersonality] = 못 / Nails
   EN: Deal +70% damage to targets that have 5+ [NailPersonality]
   PL:
226. [Obrona (ulepszenie 1) — nazwa] 불결하군요
   źródło: Skills.json :: dataList[id=1020404].levelList[level=1].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Such Filth
   PL:
227. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] 대상의 정신력 3 감소
   źródło: Skills.json :: dataList[id=1020404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Target loses 3 SP
   PL:
228. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Lust) — nazwa] 휘파람
   źródło: Passives.json :: dataList[id=1020401].name
   limit: do 40 znaków
   EN: Whistles
   PL:
229. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Lust) — opis] 전투 시작 시 정신력이 가장 낮은 아군 2명의 정신력 15 회복.\n대상이 N사 광신도면 광신 1 부여
   źródło: Passives.json :: dataList[id=1020401].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [AssemblePersonality]
   znaczenie tagów: [AssemblePersonality] = 광신 / Fanatic
   EN: Combat Start: Heal 15 SP for 2 allies that have the lowest SP\nIf the ally is an "N Corp. Fanatic", also apply 1 [AssemblePersonality]
   PL:
230. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — nazwa] 속삭임
   źródło: Passives.json :: dataList[id=1020421].name
   limit: do 40 znaków
   EN: Whispers
   PL:
231. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — opis] 전투 시작 시 정신력이 가장 낮은 아군 1명의 정신력 15 회복.\n대상이 N사 광신도면 광신 1 부여
   źródło: Passives.json :: dataList[id=1020421].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [AssemblePersonality]
   znaczenie tagów: [AssemblePersonality] = 광신 / Fanatic
   EN: Combat Start: Heal 15 SP for 1 ally that has the lowest SP\nIf the ally is an "N Corp. Fanatic", also apply 1 [AssemblePersonality]
   PL:
232. [Kwestia głosowa [get_10204_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=get_10204_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Kwestia głosowa [get_10204_1] (Identity Acquisition)] 함께 하시겠나요…? 추악함을 정화하는 대업을.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=get_10204_1].dlg
   limit: do 120 znaków
   EN: Will you join me… in the great task to purify the abominable filth?
   PL:
234. [Kwestia głosowa [lobby_morning_10204_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=lobby_morning_10204_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Kwestia głosowa [lobby_morning_10204_1] (Morning Greeting)] 연설시간에 맞춰오셨군요! 후후, 기특하군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=lobby_morning_10204_1].dlg
   limit: do 120 znaków
   EN: You came just in time for the sermons! Huhu, you deserve some praise.
   PL:
236. [Kwestia głosowa [lobby_noon_10204_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=lobby_noon_10204_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Kwestia głosowa [lobby_noon_10204_1] (Afternoon Greeting)] 아… 밖은 지금 점심 시간인가보죠? 큭큭… 너무 관심사 밖이라.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=lobby_noon_10204_1].dlg
   limit: do 120 znaków
   EN: Oh… Is it lunchtime outside? Keehee… Pardon, I couldn’t care less about such things.
   PL:
238. [Kwestia głosowa [lobby_night_10204_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=lobby_night_10204_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [Kwestia głosowa [lobby_night_10204_1] (Evening Greeting)] 정화의 시간입니다… 더러운 것들을 순수의 흙에서 떼어내 버릴 시간이죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=lobby_night_10204_1].dlg
   limit: do 120 znaków
   EN: It is the time of purification… the hour for us to remove filth from the soil of purity.
   PL:
240. [Kwestia głosowa [smalltalk_10204_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=smalltalk_10204_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
241. [Kwestia głosowa [smalltalk_10204_1] (Chatter #1)] 고통을 받아들여야 해요! 그걸 초월한 순간에야… 다시 태어날 수 있으니까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=smalltalk_10204_1].dlg
   limit: do 120 znaków
   EN: You must accept the pain! You have to transcend it… Only then may you be reborn.
   PL:
242. [Kwestia głosowa [smalltalk_10204_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=smalltalk_10204_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Kwestia głosowa [smalltalk_10204_2] (Chatter #2)] 파우스트를 따라오세요… 제게 쥐여지는 겁니다… 크흣.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=smalltalk_10204_2].dlg
   limit: do 120 znaków
   EN: Come, follow Faust… You will be gripped by my hands… Keehee.
   PL:
244. [Kwestia głosowa [smalltalk_10204_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=smalltalk_10204_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Kwestia głosowa [smalltalk_10204_3] (Chatter #3)] 인간을 구성하는 것은 살과 피… 그리고 뼈. 그 밖의 것은 불결할뿐이에요.\n…그 가면 정도는 봐드리죠. 의복과 다를 바 없으니까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=smalltalk_10204_3].dlg
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: What constitutes a human is flesh, blood… and bone. All else is filth.\n…I can give that mask of yours a pass. It’s essentially a piece of clothing.
   PL:
246. [Kwestia głosowa [smalltalk_10204_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=smalltalk_10204_4].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Kwestia głosowa [smalltalk_10204_4] (Post-Uptie Chat 1)] 당신은… 손에 묻은 것을 씻어내지 않나요?\n킥킥… 거봐요. 불결한 것을 씻어내는건 당연한 이치랍니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=smalltalk_10204_4].dlg
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Do you… not wash your hands when they are begrimed?\nKeekee… See now, to cleanse filth is a natural thing to do.
   PL:
248. [Kwestia głosowa [smalltalk_10204_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=smalltalk_10204_5].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Kwestia głosowa [smalltalk_10204_5] (Post-Uptie Chat 2)] 회사가… 항상 정답은 아니지요. 때로는… 스스로 개척할 때도 필요하답니다?
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=smalltalk_10204_5].dlg
   limit: do 140 znaków
   EN: The company… doesn’t always have the right answer. At times… you need to forge your own path, you know?
   PL:
250. [Kwestia głosowa [neglect_10204_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=neglect_10204_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Kwestia głosowa [neglect_10204_1] (Idle)] 할말도 없는데 파우스트를 잡고 있던 건가요…? 훗, 이번만 넘어가드리죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=neglect_10204_1].dlg
   limit: do 130 znaków
   EN: You’ve been keeping Faust here with nothing to say…? Hah, forgiveness comes to you just this once.
   PL:
252. [Kwestia głosowa [gacksung_10204_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=gacksung_10204_1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Kwestia głosowa [gacksung_10204_1] (Uptying)] 높이… 더 높이! 더욱… 순수한 몸으로… 후훗!
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=gacksung_10204_1].dlg
   limit: do 120 znaków
   EN: Higher… Still higher! Let me advance… toward a purer body… Huhu!
   PL:
254. [Kwestia głosowa [formation_10204_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=formation_10204_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Kwestia głosowa [formation_10204_1] (Deployment)] 망치를 쥐고.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=formation_10204_1].dlg
   limit: do 120 znaków
   EN: With hammer in hand.
   PL:
256. [Kwestia głosowa [battleentry_10204_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battleentry_10204_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Kwestia głosowa [battleentry_10204_1] (Stage Entry)] 파우스트가 나설 만한 곳이어야 할겁니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battleentry_10204_1].dlg
   limit: do 120 znaków
   EN: This had better be worthy of Faust’s participation.
   PL:
258. [Kwestia głosowa [battle_select_10204_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_select_10204_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Kwestia głosowa [battle_select_10204_1] (Viewed in Battle)] 고해는 나중에.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_select_10204_1].dlg
   limit: do 120 znaków
   EN: Save your confession for later.
   PL:
260. [Kwestia głosowa [battle_endcommand_10204_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_endcommand_10204_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Kwestia głosowa [battle_endcommand_10204_1] (Commencing Attack)] 정화!
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_endcommand_10204_1].dlg
   limit: do 120 znaków
   EN: Purge!
   PL:
262. [Kwestia głosowa [battle_enemy_break_10204_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_enemy_break_10204_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Kwestia głosowa [battle_enemy_break_10204_1] (Enemy Stagger)] 흙에서…
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_enemy_break_10204_1].dlg
   limit: do 120 znaków
   EN: From dirt…
   PL:
264. [Kwestia głosowa [battle_break_10204_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_break_10204_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Kwestia głosowa [battle_break_10204_1] (Staggered)] …맙소사.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_break_10204_1].dlg
   limit: do 120 znaków
   EN: …Goodness.
   PL:
266. [Kwestia głosowa [battle_kill_10204_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_kill_10204_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Kwestia głosowa [battle_kill_10204_1] (Enemy Killed)] …흙으로!
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_kill_10204_1].dlg
   limit: do 120 znaków
   EN: …to dirt!
   PL:
268. [Kwestia głosowa [battle_dead_10204_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_dead_10204_1].desc
   limit: do 120 znaków
   EN: Death
   PL:
269. [Kwestia głosowa [battle_dead_10204_1] (Death)] 아직… 완전해지지…
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_dead_10204_1].dlg
   limit: do 120 znaków
   EN: I’ve… yet to be whole…
   PL:
270. [Kwestia głosowa [choice_success_p_10204_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=choice_success_p_10204_2].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Kwestia głosowa [choice_success_p_10204_2] (Check Passed)] 당연하지!
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=choice_success_p_10204_2].dlg
   limit: do 120 znaków
   EN: Naturally!
   PL:
272. [Kwestia głosowa [choice_fail_n_10204_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=choice_fail_n_10204_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Kwestia głosowa [choice_fail_n_10204_1] (Check Failed)] …뭐야?
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=choice_fail_n_10204_1].dlg
   limit: do 120 znaków
   EN: How could…?
   PL:
274. [Kwestia głosowa [battle_clear_10204_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_clear_10204_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Kwestia głosowa [battle_clear_10204_1] (Victory Cry)] 정화는 끝났나…? 흐흣.
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_clear_10204_1].dlg
   limit: do 120 znaków
   EN: Is the purification over…? Heeheh.
   PL:
276. [Kwestia głosowa [battle_clear_ex_10204_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_clear_ex_10204_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Kwestia głosowa [battle_clear_ex_10204_1] (Extra Conditions Fulfilled)] 가장 순수한 세상으로!
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_clear_ex_10204_1].dlg
   limit: do 120 znaków
   EN: Toward the purest world!
   PL:
278. [Kwestia głosowa [battle_defeat_10204_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_defeat_10204_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Kwestia głosowa [battle_defeat_10204_1] (Defeat Wail)] 패배…? 믿을 수가 없네. 망치들은 어디갔지?
   źródło: PersonalityVoiceDlg/Voice_Faust_Ncorp_10204.json :: dataList[id=battle_defeat_10204_1].dlg
   limit: do 120 znaków
   EN: Defeat…? This is unbelievable. Where are my hammers?
   PL:

## [00] Zwei Assoc. South Section 4 — Faust — 남부 츠바이 협회 4과
- ID Tożsamości: `10205` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 3–5 / 4–5 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: —

280. [Karta Tożsamości — tytuł] 남부 츠바이 협회\n4과
   źródło: Personalities.json :: dataList[id=10205].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Zwei Assoc.\nSouth Section 4
   PL:
281. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10205].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10205].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Karta Tożsamości — opis] 파우스트의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10205].desc
   limit: do 120 znaków
   EN: Faust’s 5th Identity
   PL:
284. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 순찰
   źródło: Skills_personality-02.json :: dataList[id=1020501].levelList[level=1].name ; dataList[id=1020501].levelList[level=2].name ; dataList[id=1020501].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Patrolling
   PL:
285. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [DefeatDuel] 방어 레벨 증가 2를 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel], [DefenseUp]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [DefeatDuel] Gain 2 [DefenseUp]
   PL:
286. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 증가 2를 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttackHead] Gain 2 [DefenseUp] next turn
   PL:
287. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [DefeatDuel] 방어 레벨 증가 3을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020501].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel], [DefenseUp]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [DefeatDuel] Gain 3 [DefenseUp]
   PL:
288. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 증가 2를 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 2 [DefenseUp] next turn
   PL:
289. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 2 증가\n[DefeatDuel] 방어 레벨 증가 3을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Aggro], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Aggro] = 도발치 / Aggro; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain +2 [Aggro] to this Skill Slot next turn\n[DefeatDuel] Gain 3 [DefenseUp]
   PL:
290. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 고객 경호
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=1].name ; dataList[id=1020502].levelList[level=2].name ; dataList[id=1020502].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Client Protection
   PL:
291. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 현재 체력 비율이 가장 낮은 아군에게 방어 레벨 증가 2 부여 (턴 당 최대 3회 발동)
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Apply 2 [DefenseUp] to the ally that has the lowest current HP percentage (3 times per turn)
   PL:
292. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttackHead] Gain 1 [DefenseUp] next turn
   PL:
293. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 현재 체력 비율이 가장 낮은 아군에게 방어 레벨 증가 3 부여 (턴 당 최대 3회 발동)\n자신의 방어 레벨 증가 가 5 이상이면, 합 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Apply 3 [DefenseUp] to the ally that has the lowest current HP percentage (3 times per turn)\nAt 5+ [DefenseUp], Clash Power +1
   PL:
296. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 1 [DefenseUp] next turn
   PL:
297. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 증가 1을 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1020502].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 현재 체력 비율이 가장 낮은 아군에게 방어 레벨 증가 4 부여 (턴 당 최대 3회 발동)\n자신의 방어 레벨 증가 가 5 이상이면, 합 위력 +2
   źródło: Skills_personality-02.json :: dataList[id=1020502].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Apply 4 [DefenseUp] to the ally that has the lowest current HP percentage (3 times per turn)\nAt 5+ [DefenseUp], Clash Power +2
   PL:
300. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 치안 수호
   źródło: Skills_personality-02.json :: dataList[id=1020503].levelList[level=3].name ; dataList[id=1020503].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 6 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Law and Order
   PL:
301. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 방어 레벨 증가 가 5 이상이면, 코인 위력 +1\n[WinDuel] 체력 2 회복
   źródło: Skills_personality-02.json :: dataList[id=1020503].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [DefenseUp]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: At 5+ [DefenseUp], Coin Power +1\n[WinDuel] Heal 2 HP
   PL:
302. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] 현재 체력 비율이 가장 낮은 아군에게 다음 턴에 신속 1, 방어 레벨 증가 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1020503].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1020503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Agility], [DefenseUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Apply 1 [Agility] and 2 [DefenseUp] to the ally that has the lowest current HP percentage next turn
   PL:
303. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 방어 레벨 증가 가 5 이상이면, 코인 위력 +1\n[WinDuel] 체력 4 회복
   źródło: Skills_personality-02.json :: dataList[id=1020503].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [DefenseUp]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: At 5+ [DefenseUp], Coin Power +1\n[WinDuel] Heal 4 HP
   PL:
304. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] 대상이 츠바이 협회 해결사면, 신속 1, 방어 레벨 증가 1 추가 부여
   źródło: Skills_personality-02.json :: dataList[id=1020503].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility], [DefenseUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: If the ally is a Zwei Association Fixer, apply an additional 1 [Agility], 1 [DefenseUp]
   PL:
305. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-02.json :: dataList[id=1020504].levelList[level=1].name ; dataList[id=1020504].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+6)
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020504].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn
   PL:
307. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Gloom) — nazwa] 지역 보호
   źródło: Passives.json :: dataList[id=1020501].name
   limit: do 40 znaków
   EN: Territory Protection
   PL:
308. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Gloom) — opis] 전투 시작 시 조작 패널에서 양 옆의 아군에게 방어 레벨 증가 2 부여
   źródło: Passives.json :: dataList[id=1020501].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Combat Start: Apply 2 [DefenseUp] to the 2 allies adjacent to this unit on the Dashboard
   PL:
309. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Gloom) — nazwa] 지역 보호
   źródło: Passives.json :: dataList[id=1020511].name
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Gloom) — opis] 전투 시작 시 조작 패널에서 양 옆의 아군에게 방어 레벨 증가 2 부여\n대상의 체력이 50% 미만이면 추가로 2 부여
   źródło: Passives.json :: dataList[id=1020511].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Combat Start: Apply 2 [DefenseUp] to the 2 allies adjacent to this unit on the Dashboard\nIf the allies have less than 50% HP, apply an additional 2 [DefenseUp]
   PL:
311. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Gloom) — nazwa] 보호 요청 수신
   źródło: Passives.json :: dataList[id=1020521].name
   limit: do 40 znaków
   EN: Protection Request Received
   PL:
312. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Gloom) — opis] 전투 시작 시 체력 비율이 가장 낮은 아군 1명에게 방어 레벨 증가 2 부여\n대상의 체력이 50% 미만이면 추가로 2 부여
   źródło: Passives.json :: dataList[id=1020521].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Combat Start: Apply 2 [DefenseUp] to the ally that has the lowest HP percentage\nIf the ally has less than 50% HP, apply an additional 2 [DefenseUp]
   PL:
313. [Kwestia głosowa [get_10205_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=get_10205_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Kwestia głosowa [get_10205_1] (Identity Acquisition)] 파우스트, 수신했습니다. 보호 요청이 온 곳으로 이동합니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=get_10205_1].dlg
   limit: do 120 znaków
   EN: Request received. This is Faust. Advancing to protection target location.
   PL:
315. [Kwestia głosowa [lobby_morning_10205_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=lobby_morning_10205_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Kwestia głosowa [lobby_morning_10205_1] (Morning Greeting)] 안전한 아침입니다. 오늘도 지역 안전에 만전을 기하겠습니다. 좋은 하루 되세요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=lobby_morning_10205_1].dlg
   limit: do 140 znaków
   EN: A safe morning. As always, we are committed to ensuring the security of the local premises. Have a nice day.
   PL:
317. [Kwestia głosowa [lobby_noon_10205_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=lobby_noon_10205_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Kwestia głosowa [lobby_noon_10205_1] (Afternoon Greeting)] 정오 순찰 결과도 문제 없음을 보고드립니다. 아… 식사는 걱정 하지 않으셔도 됩니다. 파우스트가 식사하는 동안에는, 파트너가 순찰을 하기 때문에.\n아, 그 분 역시 4과의 인재이므로 마음쓰실 필요 없습니다. 파우스트가 더 뛰어나지만.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=lobby_noon_10205_1].dlg
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reporting in to inform you that no issues were detected during the noon patrol. Ah... There is no need to be worried about whether we've had our meal. While Faust dines, her partner handles the patrolling.\nOh, there is no need to be worried about said partner, either; Faust works with an exceptional individual from Section 4. Faust is still superior, however.
   PL:
319. [Kwestia głosowa [lobby_night_10205_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=lobby_night_10205_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Kwestia głosowa [lobby_night_10205_1] (Evening Greeting)] 야간은… 가능하면 파우스트와의 간격을 좁혀주시기 바랍니다. 시야가 좁아지기 때문에, 주간보다 보호 이동이 늦을 가능성이 높으므로.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=lobby_night_10205_1].dlg
   limit: do 170 znaków
   EN: During nighttime... Please remain in close proximity to Faust. The narrowed field of vision may delay the protective maneuvers.
   PL:
321. [Kwestia głosowa [smalltalk_10205_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=smalltalk_10205_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [Kwestia głosowa [smalltalk_10205_1] (Chatter #1)] 지역 보호는 많은 인원과 그들 각각의 능력을 요구하는 일입니다. 계약된 구역 전체에 인원들을 투입해야하니까요.\n그만큼 고액의 보수를 요구하지만… 효과는 보장드릴 수 있습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=smalltalk_10205_1].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Territory protection requires significant manpower as well as individual capability, as personnel must be deployed over the entire contract area. While the service is costly... the added safety is well worth the price.
   PL:
323. [Kwestia głosowa [smalltalk_10205_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=smalltalk_10205_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Kwestia głosowa [smalltalk_10205_2] (Chatter #2)] 지역 보호 임무 중에는 가능한 사복으로 임무를 수행하고 있습니다. 눈에 띄지 않는 편이, 보호 대상을 노리는 세력을 색출하기 쉬우니까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=smalltalk_10205_2].dlg
   limit: do 220 znaków
   EN: We try to dress ourselves in civilian clothes for territory protection contracts. It is better to hide in plain sight to recognize those that seek to harm our clients.
   PL:
325. [Kwestia głosowa [smalltalk_10205_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=smalltalk_10205_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [Kwestia głosowa [smalltalk_10205_3] (Chatter #3)] 모든 츠바이가 지역 보호 임무를 수행하지는 않습니다. 물론, 저희 4과도 지역 보호 임무만을 수행하지는 않고요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=smalltalk_10205_3].dlg
   limit: do 200 znaków
   EN: Not all Zwei agents accept territory protection contracts. Of course, territory protection contracts aren't the sole dedication of Section 4, either.
   PL:
327. [Kwestia głosowa [smalltalk_10205_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=smalltalk_10205_4].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Kwestia głosowa [smalltalk_10205_4] (Post-Uptie Chat 1)] 보통의 경우, 보호해야 할 인물이 다수 일 때 이 계약이 진행됩니다.\n그런만큼… 다수의 적에게서 고객을 보호하는 역할을 요구받죠. 파우스트도 마찬가지랍니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=smalltalk_10205_4].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Normally, these contracts are signed when the client requests several protection targets. \nTherefore... we often end up defending our clients against multiple threats. And so does Faust.
   PL:
329. [Kwestia głosowa [smalltalk_10205_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=smalltalk_10205_5].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Kwestia głosowa [smalltalk_10205_5] (Post-Uptie Chat 2)] 일의 고됨을 물으시는 건가요. 크게 신경써본 적은 없군요. 파우스트는 보호 대상의 안전만을 생각한답니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=smalltalk_10205_5].dlg
   limit: do 180 znaków
   EN: Is my work strenuous, you ask? Such details are not a part of my consideration. Faust considers only the safety of her protection targets.
   PL:
331. [Kwestia głosowa [neglect_10205_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=neglect_10205_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Kwestia głosowa [neglect_10205_1] (Idle)] 특별한 용건이 없다면, 다음 순찰 일정을 소화하고 싶네요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=neglect_10205_1].dlg
   limit: do 120 znaków
   EN: If there is nothing else, I would like to leave for my next scheduled patrol.
   PL:
333. [Kwestia głosowa [gacksung_10205_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=gacksung_10205_1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Kwestia głosowa [gacksung_10205_1] (Uptying)] 그렇군요. 우수한 자가 더 많은 구역을 담당하는 것이 옳은 이치죠. 잘 부탁합니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=gacksung_10205_1].dlg
   limit: do 170 znaków
   EN: Yes, indeed. It is only natural that greater responsibilities are assigned to finer agents. I look forward to working with you.
   PL:
335. [Kwestia głosowa [formation_10205_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=formation_10205_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Kwestia głosowa [formation_10205_1] (Deployment)] 준비되어 있습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=formation_10205_1].dlg
   limit: do 120 znaków
   EN: On standby.
   PL:
337. [Kwestia głosowa [battleentry_10205_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battleentry_10205_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Kwestia głosowa [battleentry_10205_1] (Stage Entry)] 보호 요청, 수신.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battleentry_10205_1].dlg
   limit: do 120 znaków
   EN: Protection request received.
   PL:
339. [Kwestia głosowa [battle_select_10205_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_select_10205_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Kwestia głosowa [battle_select_10205_1] (Viewed in Battle)] 다른 구역도 문제인가요?
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_select_10205_1].dlg
   limit: do 120 znaków
   EN: Do other territories require my attention?
   PL:
341. [Kwestia głosowa [battle_endcommand_10205_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_endcommand_10205_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Kwestia głosowa [battle_endcommand_10205_1] (Commencing Attack)] 보호합니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_endcommand_10205_1].dlg
   limit: do 120 znaków
   EN: Moving to protect.
   PL:
343. [Kwestia głosowa [battle_enemy_break_10205_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_enemy_break_10205_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Kwestia głosowa [battle_enemy_break_10205_1] (Enemy Stagger)] 움직이지 못하겠죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_enemy_break_10205_1].dlg
   limit: do 120 znaków
   EN: You've been immobilized.
   PL:
345. [Kwestia głosowa [battle_break_10205_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_break_10205_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Kwestia głosowa [battle_break_10205_1] (Staggered)] 윽…
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_break_10205_1].dlg
   limit: do 120 znaków
   EN: Ngh...
   PL:
347. [Kwestia głosowa [battle_kill_10205_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_kill_10205_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Kwestia głosowa [battle_kill_10205_1] (Enemy Killed)] 적대 세력을 배제했습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_kill_10205_1].dlg
   limit: do 120 znaków
   EN: Hostiles eliminated.
   PL:
349. [Kwestia głosowa [battle_dead_10205_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_dead_10205_1].desc
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Kwestia głosowa [battle_dead_10205_1] (Death)] 걱정… 마세요. 다른 인원이… 고객님을…
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_dead_10205_1].dlg
   limit: do 120 znaków
   EN: Worry... not. My colleagues will... protect...
   PL:
351. [Kwestia głosowa [choice_success_p_10205_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=choice_success_p_10205_2].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Kwestia głosowa [choice_success_p_10205_2] (Check Passed)] 이런 문제는 단순합니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=choice_success_p_10205_2].dlg
   limit: do 120 znaków
   EN: An elementary problem.
   PL:
353. [Kwestia głosowa [choice_fail_n_10205_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=choice_fail_n_10205_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Kwestia głosowa [choice_fail_n_10205_1] (Check Failed)] 파우스트와는 맞지 않는 문제였군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=choice_fail_n_10205_1].dlg
   limit: do 120 znaków
   EN: This did not align with Faust's strengths.
   PL:
355. [Kwestia głosowa [battle_clear_10205_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_clear_10205_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Kwestia głosowa [battle_clear_10205_1] (Victory Cry)] 보호 요청에 대한 임무를 완수 했습니다. 다시 순찰로 돌아가죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_clear_10205_1].dlg
   limit: do 120 znaków
   EN: Protection request fulfilled. Returning to patrol.
   PL:
357. [Kwestia głosowa [battle_clear_ex_10205_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_clear_ex_10205_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Kwestia głosowa [battle_clear_ex_10205_1] (Extra Conditions Fulfilled)] 이 지역에서 예상되는 문제는 전부 해결했네요. 오늘 순찰은 이걸로 끝내죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_clear_ex_10205_1].dlg
   limit: do 140 znaków
   EN: We have taken care of all potential troubles in this territory. Let us end our patrol for the day here.
   PL:
359. [Kwestia głosowa [battle_defeat_10205_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_defeat_10205_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Kwestia głosowa [battle_defeat_10205_1] (Defeat Wail)] 괜… 찮습니다. 츠바이의 방패는 저만이 아니니까요. 계약 종료에 대한 고려는 좀 더 심사숙고를….
   źródło: PersonalityVoiceDlg/Voice_Faust_Zwei_10205.json :: dataList[id=battle_defeat_10205_1].dlg
   limit: do 140 znaków
   EN: It's... okay. There are other shields at Zwei. Please reconsider your decision to terminate our contract...
   PL:

## [000] Seven Assoc. South Section 4 — Faust — 남부 세븐 협회 4과
- ID Tożsamości: `10206` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 76 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Rupture

361. [Karta Tożsamości — tytuł] 남부 세븐 협회\n4과
   źródło: Personalities.json :: dataList[id=10206].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Seven Assoc.\nSouth Section 4
   PL:
362. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10206].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10206].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Karta Tożsamości — opis] 파우스트의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10206].desc
   limit: do 120 znaków
   EN: Faust’s 6th Identity
   PL:
365. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 예측 분석
   źródło: Skills.json :: dataList[id=1020601].levelList[level=1].name ; dataList[id=1020601].levelList[level=2].name ; dataList[id=1020601].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Predictive Analysis
   PL:
366. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills.json :: dataList[id=1020601].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1020601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL:
367. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>이 3 이상이면 코인 위력 +1
   źródło: Skills.json :: dataList[id=1020601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>
   EN: If target has 3+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u>, Coin Power +1
   PL:
368. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 파열 3 당 코인 위력 +1 (최대 2)
   źródło: Skills.json :: dataList[id=1020601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Coin Power +1 for every 3 [Burst] on target (max 2)
   PL:
369. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 대상 해체
   źródło: Skills.json :: dataList[id=1020602].levelList[level=1].name ; dataList[id=1020602].levelList[level=2].name ; dataList[id=1020602].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Dissect Target
   PL:
370. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills.json :: dataList[id=1020602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 3 [Burst]
   PL:
371. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>이 6 이상 있으면, 다음 턴에 약점 분석 부여
   źródło: Skills.json :: dataList[id=1020602].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1020602].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1020602].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, [OnSucceedAttack], [WeaknessAnalysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [WeaknessAnalysis] = 약점 분석 / Weakness Analyzed
   EN: [OnSucceedAttack] If target has 6+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u>, inflict [WeaknessAnalysis] next turn
   PL:
372. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상에게 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>이 6 이상 있으면 코인 위력 +1\n[WinDuel] 파열 횟수 3 증가
   źródło: Skills.json :: dataList[id=1020602].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, \n, [WinDuel], [Burst]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture
   EN: If target has 6+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u>, Coin Power +1\n[WinDuel] Inflict +3 [Burst] Count
   PL:
373. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills.json :: dataList[id=1020602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 파열 6 당 코인 위력 +1 (최대 2)\n[WinDuel] 파열 횟수 3 증가
   źródło: Skills.json :: dataList[id=1020602].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Burst]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture
   EN: Coin Power +1 for every 6 [Burst] on target (max 2)\n[WinDuel] Inflict +3 [Burst] Count
   PL:
375. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 프로파일링
   źródło: Skills.json :: dataList[id=1020603].levelList[level=3].name ; dataList[id=1020603].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Profiling
   PL:
376. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 파열 3 당 피해량 +10% (최대 20%)
   źródło: Skills.json :: dataList[id=1020603].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Deal +10% damage for every 3 [Burst] on target (max 20%)
   PL:
377. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills.json :: dataList[id=1020603].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture
   PL:
378. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [EndSkill] 대상이 흐트러짐 상태가 되거나 사망하면, 다음 턴에 신속 1, 참격 위력 증가 1을 얻음
   źródło: Skills.json :: dataList[id=1020603].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1020603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Agility], [SlashResultUp]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Agility] = 신속 / Haste; [SlashResultUp] = 참격 위력 증가 / Slash Power Up
   EN: [EndSkill] If target is Staggered or defeated, gain 1 [Agility], 1 [SlashResultUp] next turn
   PL:
379. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 파열 3 당 피해량 +10% (최대 50%)\n[WinDuel] 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1020603].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Burst]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture
   EN: Deal +10% damage for every 3 [Burst] on target (max 50%)\n[WinDuel] Inflict +2 [Burst] Count
   PL:
380. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills.json :: dataList[id=1020603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [Obrona (ulepszenia 1,4) — nazwa] 빠르게 해결하죠
   źródło: Skills.json :: dataList[id=1020604].levelList[level=1].name ; dataList[id=1020604].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Let's Wrap It Up
   PL:
382. [Obrona (ulepszenia 1,4) — opis] [WhenUse] 다음 턴에 신속 1을 얻음 (턴 당 최대 3)
   źródło: Skills.json :: dataList[id=1020604].levelList[level=1].desc ; dataList[id=1020604].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste
   EN: [WhenUse] Gain 1 [Agility] next turn (3 times per turn)
   PL:
383. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — nazwa] 차가 식기 전에...
   źródło: Passives.json :: dataList[id=1020601].name
   limit: do 40 znaków
   EN: Before the Tea Cools...
   PL:
384. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — opis] 상대의 약점, 취약 속성(내성 1 초과) 으로 공격할 때, 공격 전 대상의 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>만큼 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>을 얻음 (턴 당 최대 20)
   źródło: Passives.json :: dataList[id=1020601].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, <sprite name="Breath">, <color=#f8c200>, <link="Breath">, [Breath], [Burst]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: When attacking a target using a damage type the target is "Weak" or "Fatal" (Resistance>x1) to, gain [Breath] equal to [Burst] on target before the attack (max 20 per turn)
   PL:
385. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — podsumowanie] 약점, 취약 속성으로 공격할 때, 공격 전 대상의 파열만큼 호흡을 얻음
   źródło: Passives.json :: dataList[id=1020601].summary
   limit: do 160 znaków
   EN: When attacking using a damage type the target is Weak or Fatal to, gain Poise equal to Rupture on target before the attack
   PL:
386. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 세븐 협회의 티타임
   źródło: Passives.json :: dataList[id=1020621].name
   limit: do 40 znaków
   EN: Seven Association Tea Time
   PL:
387. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 속도가 가장 빠른 아군 1명이 상대의 취약 속성(내성 1.5 초과)으로 공격 시 대상의 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>에 비례하여 피해량이 증가\n(파열 1 당 1.5%. 최대 15%)
   źródło: Passives.json :: dataList[id=1020621].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, \n
   EN: 1 ally with the fastest Speed deals +1.5% damage for every <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u> on target when attacking using a damage type that the target is "Fatal" (Resistance>x1.5) to (max 15%)
   PL:
388. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — podsumowanie] 속도가 가장 빠른 아군 1명이 취약 속성으로 공격 시 대상의 파열에 따라 피해량이 증가
   źródło: Passives.json :: dataList[id=1020621].summary
   limit: do 180 znaków
   EN: 1 ally with the fastest Speed deals more damage based on the target's Rupture when attacking using a damage type the target is Fatal to
   PL:
389. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 세븐 협회의 티타임
   źródło: Passives.json :: dataList[id=1020631].name
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Glut.) — opis] 속도가 가장 빠른 아군 1명이 <style="highlight">약점, 취약 속성(내성 1 초과)</style>으로 공격 시 대상의 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>에 비례하여 피해량이 증가\n(파열 1 당 1.5%. 최대 15%)\n<style="highlight">효과를 적용받은 대상이 세븐 협회 해결사면, 피해량 추가 증가\n(파열 1 당 0.5%. 최대 5%)</style>
   źródło: Passives.json :: dataList[id=1020631].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: 1 ally with the fastest Speed deals +1.5% damage for every <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u> on target when attacking using a damage type that the target is <style="highlight">"Weak" or "Fatal" (Resistance>x1)</style> to (max 15%)\n\n<style="highlight">If the ally is a Seven Association Fixer, deal additional damage (+0.5% for every [Burst]; max 5%)</style>
   PL:
391. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Glut.) — podsumowanie] 속도가 가장 빠른 아군 1명이 약점, 취약 속성으로 공격 시 대상의 파열에 따라 피해량이 증가\n대상이 세븐 협회 해결사면, 피해량 추가 증가
   źródło: Passives.json :: dataList[id=1020631].summary
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 1 ally with the fastest Speed deals more damage based on the target's Rupture when attacking using a damage type the target is Weak or Fatal to\nIf the ally is a Seven Association Fixer, deal additional damage
   PL:
392. [Kwestia głosowa [get_10206_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=get_10206_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Kwestia głosowa [get_10206_1] (Identity Acquisition)] 어서오세요. 주문은 이쪽에서 받겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=get_10206_1].dlg
   limit: do 120 znaków
   EN: Welcome. I will take your orders here.
   PL:
394. [Kwestia głosowa [lobby_morning_10206_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=lobby_morning_10206_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Kwestia głosowa [lobby_morning_10206_1] (Morning Greeting)] 이 공간이 혼잡하지 않은 시간대는 없지만, 가장 빽빽한 때가 지금이랍니다.\n아침을 깨는 차를 즐기지 못하면, 하루가 뒤숭숭할테니까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=lobby_morning_10206_1].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This cafeteria is consistently bustling, but now is its busiest hour. Quite understandable, as to go through a day without a cup of tea would be to stumble through it with a mind that is only half awake.
   PL:
396. [Kwestia głosowa [lobby_noon_10206_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=lobby_noon_10206_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Kwestia głosowa [lobby_noon_10206_1] (Afternoon Greeting)] 잠시 머리를 식히기 위한 티타임은 업무 효율을 고려했을 때 가장 현명한 판단이죠.\n이쪽에서 주문을 받아드리겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=lobby_noon_10206_1].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Designating time for quick elevenses or an afternoon tea is a wise managerial choice, considering they are known to improve work efficiency. I will take your orders here.
   PL:
398. [Kwestia głosowa [lobby_night_10206_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=lobby_night_10206_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Kwestia głosowa [lobby_night_10206_1] (Evening Greeting)] 저희는 심야 업무를 진행하는 협회원을 위해 늦게까지 주문을 받고 있습니다. 비번이시라면, 간단하게 셰리나 브랜디를 첨가한 차는 어떠실까요?
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=lobby_night_10206_1].dlg
   limit: do 230 znaków
   EN: We take orders into the late hours for our colleagues working night shifts or overtime. If you are off duty tonight, may I brew you some nice tea with a dash of Sherry or Brandy?
   PL:
400. [Kwestia głosowa [smalltalk_10206_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=smalltalk_10206_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Kwestia głosowa [smalltalk_10206_1] (Chatter #1)] 이 공간은 세븐 협회 안에서 누구보다 차를 사랑하는 사람들이 자체적으로 운영하는 카페테리아입니다.\n모든 분들이 자원해서 근무하고, 담당하는 날이 아니라면 평소의 협회 업무로 돌아가죠. 아, 벌어들인 수익은 당연히 더 좋은 찻잎과 티팟을 사는데 쓰입니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=smalltalk_10206_1].dlg
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This cafeteria is an employee—run establishment by members of the Seven Association who love tea more than anything else in the world. Shifts are all voluntary, and we return to our usual duties on our off hours. Ah, and it goes without saying that all profits go to purchasing higher—quality tea leaves and teapots.
   PL:
402. [Kwestia głosowa [smalltalk_10206_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=smalltalk_10206_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Kwestia głosowa [smalltalk_10206_2] (Chatter #2)] 우유는! …가능하면 차를 잔에 붓기 전에 먼저 넣으시는 걸 권장… 드립니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=smalltalk_10206_2].dlg
   limit: do 130 znaków
   EN: THE MILK!...should already be in the cup before the tea is poured. That is our...recommended way.
   PL:
404. [Kwestia głosowa [smalltalk_10206_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=smalltalk_10206_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Kwestia głosowa [smalltalk_10206_3] (Chatter #3)] 얼음…을? 아. 죄송하지만 아이스티는 취급하고 있지 않습니다.\n…실례가 되지 않는다면, 홍차를 뜨겁게 즐겨야 하는 이유에 대해서 설명하는 시간을 가져도 되겠습니까?
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=smalltalk_10206_3].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You'd like some... ice? Apologies, but this establishment does not serve iced 'tea'.\nIf it is of no trouble to you, may I take a moment of your time to explicate why black tea must be enjoyed at higher temperatures?
   PL:
406. [Kwestia głosowa [smalltalk_10206_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=smalltalk_10206_4].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Kwestia głosowa [smalltalk_10206_4] (Post-Uptie Chat 1)] 아. 지금은 다른 임무를 진행중입니다.\n당신과 함께 하는 차에 대한 잡담은 언제나 즐겁지만, 잠시만 있다가 하도록 하죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=smalltalk_10206_4].dlg
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ah, I am occupied at the present moment.\nWhile I always enjoy our tea discussions, it must wait for now.
   PL:
408. [Kwestia głosowa [smalltalk_10206_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=smalltalk_10206_5].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Kwestia głosowa [smalltalk_10206_5] (Post-Uptie Chat 2)] 정교한 임무 수행과 잡맛 없는 차를 우리는 능력. 파우스트는 이 두 가지 일을 양립하는 것을 최우선으로 생각합니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=smalltalk_10206_5].dlg
   limit: do 160 znaków
   EN: Precise work ethic and talent for brewing tea of exact, pure flavor. Faust considers these as her two primary objectives.
   PL:
410. [Kwestia głosowa [neglect_10206_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=neglect_10206_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Kwestia głosowa [neglect_10206_1] (Idle)] 찻잎을 너무 우리는 것은 잡스러운 맛이 올라오는 것을 방치하는 것과 마찬가지 입니다. 지양하는 걸 추천드립니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=neglect_10206_1].dlg
   limit: do 120 znaków
   EN: To over—infuse your tea is to allow impure flavors to surface. Please refrain from doing so.
   PL:
412. [Kwestia głosowa [gacksung_10206_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=gacksung_10206_1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Kwestia głosowa [gacksung_10206_1] (Uptying)] 네, 기꺼이요. 파우스트의 능력이 필요하다면 언제든 불러주세요. 아, 티타임은 제외하도록 하죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=gacksung_10206_1].dlg
   limit: do 140 znaków
   EN: Yes, of course. You may call upon me at any time should the need arise. Unless it's tea time, that is.
   PL:
414. [Kwestia głosowa [formation_10206_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=formation_10206_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Kwestia głosowa [formation_10206_1] (Deployment)] 급행 주문이군요?
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=formation_10206_1].dlg
   limit: do 120 znaków
   EN: An urgent order, yes?
   PL:
416. [Kwestia głosowa [battleentry_10206_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battleentry_10206_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Kwestia głosowa [battleentry_10206_1] (Stage Entry)] 현장에서 직접 뵙죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battleentry_10206_1].dlg
   limit: do 120 znaków
   EN: I will rendezvous with you out in the field.
   PL:
418. [Kwestia głosowa [battle_select_10206_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_select_10206_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Kwestia głosowa [battle_select_10206_1] (Viewed in Battle)] 차가 식기 전에.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_select_10206_1].dlg
   limit: do 120 znaków
   EN: Before the tea cools.
   PL:
420. [Kwestia głosowa [battle_endcommand_10206_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_endcommand_10206_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Kwestia głosowa [battle_endcommand_10206_1] (Commencing Attack)] 깔끔하게.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_endcommand_10206_1].dlg
   limit: do 120 znaków
   EN: Flawless.
   PL:
422. [Kwestia głosowa [battle_enemy_break_10206_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_enemy_break_10206_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Kwestia głosowa [battle_enemy_break_10206_1] (Enemy Stagger)] …부숴진 홍차 잎 같군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_enemy_break_10206_1].dlg
   limit: do 120 znaków
   EN: Like shattered tea leaves.
   PL:
424. [Kwestia głosowa [battle_break_10206_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_break_10206_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Kwestia głosowa [battle_break_10206_1] (Staggered)] 아…
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_break_10206_1].dlg
   limit: do 120 znaków
   EN: Ah…
   PL:
426. [Kwestia głosowa [battle_kill_10206_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_kill_10206_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Kwestia głosowa [battle_kill_10206_1] (Enemy Killed)] 더 이상 얻을 정보는 없군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_kill_10206_1].dlg
   limit: do 120 znaków
   EN: There is no more information to be gained.
   PL:
428. [Kwestia głosowa [battle_dead_10206_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_dead_10206_1].desc
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Kwestia głosowa [battle_dead_10206_1] (Death)] 하… 다음 카페 근무… 이어 받을 사람이 없… 는데.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_dead_10206_1].dlg
   limit: do 120 znaków
   EN: Haah... But... I don't have anyone... to cover my next shift...
   PL:
430. [Kwestia głosowa [choice_success_p_10206_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=choice_success_p_10206_2].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Kwestia głosowa [choice_success_p_10206_2] (Check Passed)] 빈틈 없는 관찰의 결과죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=choice_success_p_10206_2].dlg
   limit: do 120 znaków
   EN: A result of meticulous observation.
   PL:
432. [Kwestia głosowa [choice_fail_n_10206_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=choice_fail_n_10206_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Kwestia głosowa [choice_fail_n_10206_1] (Check Failed)] …보기만 하고, 관찰하지 못했군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=choice_fail_n_10206_1].dlg
   limit: do 120 znaków
   EN: ... I should have observed more carefully.
   PL:
434. [Kwestia głosowa [battle_clear_10206_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_clear_10206_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Kwestia głosowa [battle_clear_10206_1] (Victory Cry)] 임무는 성공적이었군요. 아, 다음 카페 근무가 있어서. 먼저 실례하죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_clear_10206_1].dlg
   limit: do 140 znaków
   EN: This mission was a success. Ah, now I must leave for my shift at the cafeteria. So, if you will excuse me...
   PL:
436. [Kwestia głosowa [battle_clear_ex_10206_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_clear_ex_10206_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Kwestia głosowa [battle_clear_ex_10206_1] (Extra Conditions Fulfilled)] 밀크티. 젓지 말고, 가볍게 부어서 부탁드립니다. 역시, 남이 타주는 차가 가장 맛있죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_clear_ex_10206_1].dlg
   limit: do 170 znaków
   EN: Milk tea, please. Poured, not stirred. Indeed, tea tastes better when it is served to you rather than when you serve it yourself.
   PL:
438. [Kwestia głosowa [battle_defeat_10206_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_defeat_10206_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Kwestia głosowa [battle_defeat_10206_1] (Defeat Wail)] 의도한 대로 되지 않았군요… 차가 부족했기 때문이겠죠. 티타임을 가지고 다시 시도해보죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Seven_10206.json :: dataList[id=battle_defeat_10206_1].dlg
   limit: do 160 znaków
   EN: That was... unexpected. We must not have ingested enough tea. Let us take some time off for tea before our next attempt.
   PL:

## [000] Lobotomy E.G.O::Regret — Faust — 로보토미 E.G.O:: 후회
- ID Tożsamości: `10207` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9101 · HP bazowe: 82 · szybkość: 2–5 / 2–5 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Tremor

440. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n후회
   źródło: Personalities.json :: dataList[id=10207].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::Regret
   PL:
441. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10207].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10207].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Karta Tożsamości — opis] 파우스트의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10207].desc
   limit: do 120 znaków
   EN: Faust’s 7th Identity
   PL:
444. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 조여오는 구속구
   źródło: Skills_personality-02.json :: dataList[id=1020701].levelList[level=1].name ; dataList[id=1020701].levelList[level=2].name ; dataList[id=1020701].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Contracting Straight-jacket
   PL:
445. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 진동 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020701].levelList[level=1].desc ; dataList[id=1020701].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count
   PL:
446. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020701].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1020701].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain +3 [Vibration] Count
   PL:
447. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020701].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
448. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020701].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1020701].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL:
449. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 진동 횟수 3 증가\n[DefeatDuel] 자신의 진동 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count\n[DefeatDuel] Gain +3 [Vibration] Count
   PL:
450. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 금속성 울림
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=1].name ; dataList[id=1020702].levelList[level=2].name ; dataList[id=1020702].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Metallic Ringing
   PL:
451. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 진동 횟수 4 증가
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +4 [Vibration] Count
   PL:
452. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 공격 레벨 감소 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [AttackDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttackHead] Inflict 1 [AttackDown] next turn
   PL:
453. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 4 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]
   PL:
454. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [StartBattle] 자신의 진동 횟수 5를 소모하여 이 스킬의 공격 가중치 +1\n[WhenUse] 자신의 진동 횟수 4 증가
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=2].desc ; dataList[id=1020702].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] Consume 5 [Vibration] Count on self and gain +1 Atk Weight for this Skill\n[WhenUse] Gain +4 [Vibration] Count
   PL:
455. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 진동 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Gain +1 [Vibration] Count
   PL:
456. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 공격 레벨 감소 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=2].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
457. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 5 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1020702].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]
   PL:
458. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 더하기 코인 약화 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [PlusCoinValueDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop
   EN: [OnSucceedAttackHead] Inflict 1 [PlusCoinValueDown] next turn
   PL:
459. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 공격 레벨 감소 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown] next turn
   PL:
460. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 더하기 코인 약화 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020702].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PlusCoinValueDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop
   EN: [OnSucceedAttack] Inflict 1 [PlusCoinValueDown] next turn
   PL:
461. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 풀려난 폭력성
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=3].name ; dataList[id=1020703].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 3 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Unleashed Violence
   PL:
462. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] 자신의 진동 횟수 5를 소모하여 이 스킬의 공격 가중치 +1 (최대 +2)\n[DefeatDuel] 정신력 20 감소\n대상이 보유한 부정적인 효과 1개당 피해량이 3% 증가(최대 15%)\n[EnemyKill] 자신의 진동 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=3].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefeatDuel], [EnemyKill], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EnemyKill] = [적 처치 시] / [On Kill]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] Consume 5 [Vibration] Count on self and gain +1 Atk Weight for this Skill (max +2)\n[DefeatDuel] Lose 20 SP\nDeal +3% damage for every type of negative effect on target (max 15%)\n[EnemyKill] Gain +2 [Vibration] Count
   PL:
463. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 최종 흐트러짐 손상의 20%만큼 분노 피해를 줌.(최대 13)
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion],\nthen deal Wrath damage equal to 20% of the final Stagger Threshold raised by [VibrationExplosion] (max 13)
   PL:
464. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 최종 흐트러짐 손상의 20%만큼 분노 피해를 줌.(최대 13)
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 최종 흐트러짐 손상의 20%만큼 분노 피해를 줌.(최대 13)\n진동 횟수 3 감소
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion],\nthen deal Wrath damage equal to 20% of the final Stagger Threshold raised by [VibrationExplosion] (max 13)\nReduce [Vibration] Count by 3
   PL:
466. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [StartBattle] 자신의 진동 횟수 5를 소모하여 이 스킬의 공격 가중치 +1 (최대 +2)\n[DefeatDuel] 정신력 20 감소\n대상이 보유한 부정적인 효과 1개당 피해량이 6% 증가(최대 30%)\n[EnemyKill] 자신의 진동 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefeatDuel], [EnemyKill], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EnemyKill] = [적 처치 시] / [On Kill]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] Consume 5 [Vibration] Count on self and gain +1 Atk Weight for this Skill (max +2)\n[DefeatDuel] Lose 20 SP\nDeal +6% damage for every type of negative effect on target (max 30%)\n[EnemyKill] Gain +2 [Vibration] Count
   PL:
467. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 최종 흐트러짐 손상의 30%만큼 분노 피해를 줌.(최대 20)
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion],\nthen deal Wrath damage equal to 30% of the final Stagger Threshold raised by [VibrationExplosion] (max 20)
   PL:
468. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 최종 흐트러짐 손상의 30%만큼 분노 피해를 줌.(최대 20)
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 최종 흐트러짐 손상의 30%만큼 분노 피해를 줌.(최대 20)\n진동 횟수 3 감소
   źródło: Skills_personality-02.json :: dataList[id=1020703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion],\nthen deal Wrath damage equal to 30% of the final Stagger Threshold raised by [VibrationExplosion] (max 20)\nReduce [Vibration] Count by 3
   PL:
470. [Obrona (ulepszenia 1,4) — nazwa] 앙금 쌓기
   źródło: Skills_personality-02.json :: dataList[id=1020704].levelList[level=1].name ; dataList[id=1020704].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: kontra · moc bazowa: 9 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Gathering Spite
   PL:
471. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 진동 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020704].levelList[level=1].desc
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 진동 횟수 6 증가
   źródło: Skills_personality-02.json :: dataList[id=1020704].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +6 [Vibration] Count
   PL:
473. [Pasywka bojowa (od ulepszenia 2, posiadane 6× Wrath) — nazwa] 떠밀린 후회
   źródło: Passives.json :: dataList[id=1020701].name
   limit: do 40 znaków
   EN: Coerced Regret
   PL:
474. [Pasywka bojowa (od ulepszenia 2, posiadane 6× Wrath) — opis] - 합 진행 시 대상이 보유한 부정적인 효과가 3개 이상이면, 대상의 합 위력 -1\n- 자신이 생존해있을 때, [VibrationExplosion]을 당하는 적이 방어 레벨 감소 2를 얻음. (턴 당 적 1명당 최대 1회)\n- 정신 오염: 턴 종료 시 정신력이 -25 미만일 때 다음 턴에 속박 2,  타격 위력 증가 1을 얻음
   źródło: Passives.json :: dataList[id=1020701].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationExplosion], [DefenseDown], [Binding], [HitResultUp]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Binding] = 속박 / Bind; [HitResultUp] = 타격 위력 증가 / Blunt Power Up
   EN: - In a Clash, if target has 3+ types of negative effect, target's Clash Power -1\n- When this unit is alive, enemies affected by [VibrationExplosion] gain 2 [DefenseDown] (once per enemy per turn)\n- Mental Corruption: If at less than -25 SP at Turn End, gain 2 [Binding] and 1 [HitResultUp] next turn
   PL:
475. [Pasywka bojowa (od ulepszenia 4, posiadane 6× Wrath) — nazwa] 떠밀린 후회
   źródło: Passives.json :: dataList[id=1020711].name
   (powtórzenie elementu 473 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Pasywka bojowa (od ulepszenia 4, posiadane 6× Wrath) — opis] - 합 진행 시 대상이 보유한 부정적인 효과 3개 당 대상의 합 위력 -1 (최대 2)\n- 자신이 생존해있을 때, [VibrationExplosion]을 당하는 적이 방어 레벨 감소 2를 얻음 (턴 당 적 1명당 최대 3회)\n- 정신 오염: 턴 종료 시 정신력이 -25 미만일 때 다음 턴에 속박 2,  타격 위력 증가 1을 얻음
   źródło: Passives.json :: dataList[id=1020711].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationExplosion], [DefenseDown], [Binding], [HitResultUp]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Binding] = 속박 / Bind; [HitResultUp] = 타격 위력 증가 / Blunt Power Up
   EN: - In a Clash, target's Clash Power -1 for every 3 types of negative effect it has (max -2 Clash Power)\n- When this unit is alive, enemies affected by [VibrationExplosion] gain 2 [DefenseDown] (3 times per enemy per turn)\n- Mental Corruption: If at less than -25 SP at Turn End, gain 2 [Binding] and 1 [HitResultUp] next turn
   PL:
477. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — nazwa] 억압 작업
   źródło: Passives.json :: dataList[id=1020721].name
   limit: do 40 znaków
   EN: Repression Work
   PL:
478. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — opis] 속도가 가장 느린 아군 1명이 합 진행 시 대상이 보유한 부정적인 효과가 3개 이상이면, 대상의 합 위력 -1
   źródło: Passives.json :: dataList[id=1020721].desc
   limit: do 160 znaków
   EN: In a Clash, if the target of the ally with the slowest Speed has 3+ types of negative effect, target's Clash Power -1
   PL:
479. [Kwestia głosowa [get_10207_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=get_10207_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Kwestia głosowa [get_10207_1] (Identity Acquisition)] T-01-54, 격리 환상체에 대한 작업을 시작합니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=get_10207_1].dlg
   limit: do 120 znaków
   EN: Starting work on Contained Abnormality T-01-54.
   PL:
481. [Kwestia głosowa [lobby_morning_10207_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=lobby_morning_10207_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Kwestia głosowa [lobby_morning_10207_1] (Morning Greeting)] 아, 좋은 아침입니다. 관리자님. 오늘 진행될 환상체의 작업 순서를 준비해 주신다면, 팀원들에게 전달하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=lobby_morning_10207_1].dlg
   limit: do 170 znaków
   EN: Good morning, Manager. Please share with me today's descending list of Work for the Abnormalities, and I will relay it to the team.
   PL:
483. [Kwestia głosowa [lobby_noon_10207_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=lobby_noon_10207_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Kwestia głosowa [lobby_noon_10207_1] (Afternoon Greeting)] 사무직 분들은 사이좋게 모여서 식사를 하시는 것 같네요. 저희 지휘팀 관리직은 특별히 그룹을 지어 식사하진 않는데… 말쿠트님은 저런 것을 원했을까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=lobby_noon_10207_1].dlg
   limit: do 260 znaków
   EN: It seems to me that the Clerks are having a nice lunch together. Us Control Team Agents don't particularly prefer to dine in groups... But I must wonder if that is what Ms. Malkuth would want us to do.
   PL:
485. [Kwestia głosowa [lobby_night_10207_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=lobby_night_10207_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Kwestia głosowa [lobby_night_10207_1] (Evening Greeting)] 금일 작업은 95% 마무리가 되었습니다. 정상적으로 목표하던 PE-BOX에 도달할 것 같네요. 오늘도 고생 많으셨습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=lobby_night_10207_1].dlg
   limit: do 130 znaków
   EN: Work progress at 95%. We should have no trouble reaching our target PE-Box goal today. Good work.
   PL:
487. [Kwestia głosowa [smalltalk_10207_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=smalltalk_10207_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Kwestia głosowa [smalltalk_10207_1] (Chatter #1)] '버려진 살인마' 말씀이시군요. 특별하게 선호하는 작업이 없는 것이 특징이라고 할 수 있겠네요. 아, 억압 작업만은 피하는 것이 좋아 보였습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=smalltalk_10207_1].dlg
   limit: do 240 znaków
   EN: The 'Forsaken Murderer'? Hm. I suppose it stands out in that it does not have a particular preference for any kind of Work. It seemed that avoiding Repression Work is advisable, however.
   PL:
489. [Kwestia głosowa [smalltalk_10207_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=smalltalk_10207_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Kwestia głosowa [smalltalk_10207_2] (Chatter #2)] 작업에 대한 이해도가 있는 직원이 담당하면, 크게 문제될 것도 없어보입니다. 다만, 나쁜 작업 결과는 환상체의 탈출로 이어지니… 그 부분을 유념해주시면 좋겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=smalltalk_10207_2].dlg
   limit: do 230 znaków
   EN: I foresee little trouble ahead, as long as the assigned employee has a decent understanding of this Work. A bad result, however, may lead to Abnormalities breaching containment.
   PL:
491. [Kwestia głosowa [smalltalk_10207_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=smalltalk_10207_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Kwestia głosowa [smalltalk_10207_3] (Chatter #3)] 배정받은 E.G.O 수트는 무난히 쓸만한 것 같습니다. 화이트 피해에는 약하여, 정신이 여린 직원들은 간혹 이 구속구가 자기를 조이는 것 같다는 이야기도 나오지만요…
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=smalltalk_10207_3].dlg
   limit: do 320 znaków
   EN: The E.G.O suits assigned to us seem adequate. However, I have been hearing reports from employees with weaker mental fortitude that it feels as though the straight-jacket is contracting around them. These suits are weak to WHITE damage, after all...
   PL:
493. [Kwestia głosowa [smalltalk_10207_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=smalltalk_10207_4].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Kwestia głosowa [smalltalk_10207_4] (Post-Uptie Chat 1)] 어느새 채워져있는 E.G.O 기프트가 예상한 것보다 불편하지는 않습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=smalltalk_10207_4].dlg
   limit: do 130 znaków
   EN: This E.G.O gift isn't as uncomfortable as I expected. Though it was equipped without my knowledge.
   PL:
495. [Kwestia głosowa [smalltalk_10207_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=smalltalk_10207_5].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Kwestia głosowa [smalltalk_10207_5] (Post-Uptie Chat 2)] 머리가 철이 되어간다는 느낌은 무엇이었을까요. 이 망치를 휘둘러 적을 으깨버릴 때마다, 그것은 자신의 머리가 두드려지는 기분을 느끼게 되는 걸까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=smalltalk_10207_5].dlg
   limit: do 190 znaków
   EN: I am curious: how does it feel when its head slowly turns into metal? Can it feel that? Does its head ring when this hammer crushes our enemies?
   PL:
497. [Kwestia głosowa [neglect_10207_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=neglect_10207_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Kwestia głosowa [neglect_10207_1] (Idle)] …또, 머리를 부딪히는 소리…
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=neglect_10207_1].dlg
   limit: do 120 znaków
   EN: ... More banging noises, again...
   PL:
499. [Kwestia głosowa [gacksung_10207_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=gacksung_10207_1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Kwestia głosowa [gacksung_10207_1] (Uptying)] 지휘팀 관리직 팀장 파우스트. 관리자 님의 명령대로 녹빛 여명 시련 제압에 들어갑니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=gacksung_10207_1].dlg
   limit: do 150 znaków
   EN: Control Team Captain, Agent Faust. Commencing suppression of the Green Dawn Ordeal as per the Manager's orders.
   PL:
501. [Kwestia głosowa [formation_10207_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=formation_10207_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Kwestia głosowa [formation_10207_1] (Deployment)] 준비 되었습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=formation_10207_1].dlg
   limit: do 120 znaków
   EN: I am ready.
   PL:
503. [Kwestia głosowa [battleentry_10207_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battleentry_10207_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Kwestia głosowa [battleentry_10207_1] (Stage Entry)] 제압을 준비합니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battleentry_10207_1].dlg
   limit: do 120 znaków
   EN: Preparing to suppress.
   PL:
505. [Kwestia głosowa [battle_select_10207_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_select_10207_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Kwestia głosowa [battle_select_10207_1] (Viewed in Battle)] 다른 작업이 필요한가요?
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_select_10207_1].dlg
   limit: do 120 znaków
   EN: Do you require more Work to be done?
   PL:
507. [Kwestia głosowa [battle_endcommand_10207_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_endcommand_10207_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Kwestia głosowa [battle_endcommand_10207_1] (Commencing Attack)] 탈출 개체 확인.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_endcommand_10207_1].dlg
   limit: do 120 znaków
   EN: Containment Breach confirmed.
   PL:
509. [Kwestia głosowa [battle_enemy_break_10207_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_enemy_break_10207_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Kwestia głosowa [battle_enemy_break_10207_1] (Enemy Stagger)] 개체가 약화되는 것 같습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_enemy_break_10207_1].dlg
   limit: do 120 znaków
   EN: The entity is weakening.
   PL:
511. [Kwestia głosowa [battle_break_10207_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_break_10207_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Kwestia głosowa [battle_break_10207_1] (Staggered)] 엇…
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_break_10207_1].dlg
   limit: do 120 znaków
   EN: Uh...
   PL:
513. [Kwestia głosowa [battle_kill_10207_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_kill_10207_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Kwestia głosowa [battle_kill_10207_1] (Enemy Killed)] 탈출 개체가 정리되었습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_kill_10207_1].dlg
   limit: do 120 znaków
   EN: Escaped entity neutralized.
   PL:
515. [Kwestia głosowa [battle_dead_10207_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_dead_10207_1].desc
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Kwestia głosowa [battle_dead_10207_1] (Death)] 제압작업 실패…
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_dead_10207_1].dlg
   limit: do 120 znaków
   EN: Suppression Work failed...
   PL:
517. [Kwestia głosowa [choice_success_p_10207_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=choice_success_p_10207_2].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Kwestia głosowa [choice_success_p_10207_2] (Check Passed)] 보조 업무로 수행하기에 나쁘지 않은 일이네요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=choice_success_p_10207_2].dlg
   limit: do 120 znaków
   EN: That was an adequate side work.
   PL:
519. [Kwestia głosowa [choice_fail_n_10207_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=choice_fail_n_10207_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Kwestia głosowa [choice_fail_n_10207_1] (Check Failed)] 적합하지 않은 관리 작업이었군요… 관리 기록에 적어둬야겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=choice_fail_n_10207_1].dlg
   limit: do 120 znaków
   EN: This Work does not align with my strengths... I will make a note of it in the logs.
   PL:
521. [Kwestia głosowa [battle_clear_10207_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_clear_10207_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Kwestia głosowa [battle_clear_10207_1] (Victory Cry)] 제압 작업은 이것으로 완료하면 되겠군요. 다시 관리 작업으로 돌아가겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_clear_10207_1].dlg
   limit: do 120 znaków
   EN: We can end the Suppression Work here. Returning to management.
   PL:
523. [Kwestia głosowa [battle_clear_ex_10207_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_clear_ex_10207_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Kwestia głosowa [battle_clear_ex_10207_1] (Extra Conditions Fulfilled)] 제압 완료. 경보에는 익숙해지시는게 좋을 겁니다. 아직 50일까지 많은 날이 남은 것을 파우스트는 알고 있으니까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_clear_ex_10207_1].dlg
   limit: do 190 znaków
   EN: Threat Suppressed. I recommend that you familiarize yourself with these alarms. Faust knows that we have many days to go before the 50th day.
   PL:
525. [Kwestia głosowa [battle_defeat_10207_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_defeat_10207_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Kwestia głosowa [battle_defeat_10207_1] (Defeat Wail)] 지휘팀 제압 실패. 다음 부서에게 지원을 요청합니다…
   źródło: PersonalityVoiceDlg/Voice_Faust_LEGO_10207.json :: dataList[id=battle_defeat_10207_1].dlg
   limit: do 120 znaków
   EN: Control Team's Suppression Work failed. Requesting assistance from the other departments...
   PL:

## [000] Blade Lineage Salsu — Faust — 검계 살수
- ID Tożsamości: `10208` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 3 · HP bazowe: 76 · szybkość: 3–6 / 3–7 / 3–8 / 3–8
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Poise, Bleed

527. [Karta Tożsamości — tytuł] 검계\n살수
   źródło: Personalities.json :: dataList[id=10208].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Blade Lineage\nSalsu
   PL:
528. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10208].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10208].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Karta Tożsamości — opis] 파우스트의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10208].desc
   limit: do 120 znaków
   EN: Faust’s 8th Identity
   PL:
531. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 월하검무
   źródło: Skills_personality-02.json :: dataList[id=1020801].levelList[level=1].name ; dataList[id=1020801].levelList[level=2].name ; dataList[id=1020801].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 3 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Moonlit Blade Dance
   PL:
532. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020801].levelList[level=1].desc ; dataList[id=1020801].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL:
533. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [CriticalOnSucceedAttack] [RedApricotBlossom] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020801].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1020801].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1020801].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [RedApricotBlossom]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [RedApricotBlossom] = 홍매화 / Red Plum Blossom
   EN: [CriticalOnSucceedAttack] Inflict 1 [RedApricotBlossom]
   PL:
534. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1020801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath]
   PL:
535. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 5 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020801].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 5+ [Breath], Coin Power +1</style>\n[WhenUse] Gain +2 [Breath] Count
   PL:
536. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 자법
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=1].name ; dataList[id=1020802].levelList[level=2].name ; dataList[id=1020802].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Acupuncture
   PL:
537. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=1].desc ; dataList[id=1020802].levelList[level=2].desc
   (powtórzenie elementu 532 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL:
539. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] [RedApricotBlossom] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [RedApricotBlossom]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [RedApricotBlossom] = 홍매화 / Red Plum Blossom
   EN: [CriticalOnSucceedAttack] Inflict 2 [RedApricotBlossom]
   PL:
540. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1020802].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL:
541. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1020802].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: Deal +30% damage on Critical Hit
   PL:
542. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL:
543. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [RedApricotBlossom] 2 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1020802].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [RedApricotBlossom]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [RedApricotBlossom] = 홍매화 / Red Plum Blossom
   EN: [CriticalOnSucceedAttack] Inflict 2 [RedApricotBlossom]<style="highlight"></style>
   PL:
544. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 7 이상이면, 코인 위력 +1\n</style>[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020802].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 7+ [Breath], Coin Power +1\n</style>[WhenUse] Gain +2 [Breath] Count
   PL:
545. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 흩날리는 홍매화
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=3].name ; dataList[id=1020803].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 5 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Red Plum Blossoms Scatter
   PL:
546. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [RedApricotBlossom] 1 당 피해량 +3%\n[WinDuel] 자신의 [Breath] 횟수를 절반 감소하고, 감소한 양만큼 [Breath]을 얻음. (최대 10)
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [RedApricotBlossom], [WinDuel], [Breath]
   znaczenie tagów: [RedApricotBlossom] = 홍매화 / Red Plum Blossom; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: Deal +3% damage for every [RedApricotBlossom] on target\n[WinDuel] Consume half the [Breath] Count on self, then gain [Breath] equal to the [Breath] Count consumed (max 10)
   PL:
547. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] [RedApricotBlossom] 5 부여
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1020803].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [RedApricotBlossom]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [RedApricotBlossom] = 홍매화 / Red Plum Blossom
   EN: [CriticalOnSucceedAttack] Inflict 5 [RedApricotBlossom]
   PL:
548. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] [RedApricotBlossom] 5 부여
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1020803].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 547 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [RedApricotBlossom] 1 당 피해량 +3%\n<style="highlight">자신의 [Breath] 7 당 코인 위력 +1 (최대 3)</style>\n[WinDuel] 자신의 [Breath] 횟수를 절반 감소하고, 감소한 양만큼 [Breath]을 얻음. (최대 10)\n<style="highlight">이 스킬로 크리티컬 적중 시 [RedApricotBlossom]가 감소하지 않음</style>
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RedApricotBlossom], [Breath], [WinDuel]
   znaczenie tagów: [RedApricotBlossom] = 홍매화 / Red Plum Blossom; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Deal +3% damage for every [RedApricotBlossom] on target\n<style="highlight">Coin Power +1 for every 7 [Breath] on self (max 3)</style>\n[WinDuel] Consume half the [Breath] Count on self, then gain [Breath] equal to the [Breath] Count consumed (max 10)\n<style="highlight">This Skill does not consume [RedApricotBlossom] On Crit</style>
   PL:
550. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 대상의 [RedApricotBlossom]가 10이면, 참격 취약 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [RedApricotBlossom], [SlashTakeDamageUp]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [RedApricotBlossom] = 홍매화 / Red Plum Blossom; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [CriticalOnSucceedAttack] If target has 10 [RedApricotBlossom], inflict 1 [SlashTakeDamageUp]
   PL:
551. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 대상의 [RedApricotBlossom]가 10이면, 참격 취약 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1020803].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Obrona (ulepszenia 1,4) — nazwa] 흘려내기
   źródło: Skills_personality-02.json :: dataList[id=1020804].levelList[level=1].name ; dataList[id=1020804].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Redirect
   PL:
553. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 4 당 최종 위력 +1 (최대 3)
   źródło: Skills_personality-02.json :: dataList[id=1020804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] For every 4 [Breath] on self, gain Final Power +1 (max 3)
   PL:
554. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath] 4 당 최종 위력 +1 (최대 5)
   źródło: Skills_personality-02.json :: dataList[id=1020804].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] For every 4 [Breath] on self, gain Final Power +1 (max 5)
   PL:
555. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — nazwa] 매화 같이 터져나오는 피
   źródło: Passives.json :: dataList[id=1020801].name
   limit: do 40 znaków
   EN: Sanguine Plum Blossoms
   PL:
556. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — opis] 크리티컬 적중 시 [RedApricotBlossom] 1 부여. (최대 3회)
   źródło: Passives.json :: dataList[id=1020801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RedApricotBlossom]
   znaczenie tagów: [RedApricotBlossom] = 홍매화 / Red Plum Blossom
   EN: On Crit, inflict 1 [RedApricotBlossom] (max 3 times)
   PL:
557. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Pride) — nazwa] 매화 같이 터져나오는 피
   źródło: Passives.json :: dataList[id=1020811].name
   (powtórzenie elementu 555 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Pride) — opis] 크리티컬 적중 시 [RedApricotBlossom] 1 부여. 대상의 [RedApricotBlossom]가 10이면, 대신 방어 레벨 감소 1 부여 (최대 6회)
   źródło: Passives.json :: dataList[id=1020811].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [RedApricotBlossom], [DefenseDown]
   znaczenie tagów: [RedApricotBlossom] = 홍매화 / Red Plum Blossom; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: On Crit, inflict 1 [RedApricotBlossom]\nIf target has 10 [RedApricotBlossom], inflict 1 [DefenseDown] instead (max 6 times)
   PL:
559. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — nazwa] 미련 서린 검끝
   źródło: Passives.json :: dataList[id=1020821].name
   limit: do 40 znaków
   EN: Lingering Bladepoint
   PL:
560. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — opis] 편성 순서가 가장 빠른 아군이 참격 속성 스킬로 크리티컬 적중 시 방어 레벨 감소 1 부여 (턴 당 적 1명당 최대 3)
   źródło: Passives.json :: dataList[id=1020821].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [DefenseDown]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When the ally with the earliest Deployment order hits Critically using a Slash Skill, inflict 1 [DefenseDown] (max 3 times per enemy per turn)
   PL:
561. [Kwestia głosowa [get_10208_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=get_10208_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Kwestia głosowa [get_10208_1] (Identity Acquisition)] 출정전야는 반드시 고요한 법이죠. 마침… 달도 가득 차올랐군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=get_10208_1].dlg
   limit: do 120 znaków
   EN: A night before a battle is always so silent. Ah, and the moon has waxed full tonight, too.
   PL:
563. [Kwestia głosowa [lobby_morning_10208_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=lobby_morning_10208_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Kwestia głosowa [lobby_morning_10208_1] (Morning Greeting)] 좋은 아침입니다. 소박한 식사와 따스한 차 한 잔을 즐기기 좋은 시간이군요. 서두를 필요는 없겠지요.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=lobby_morning_10208_1].dlg
   limit: do 150 znaków
   EN: Good morning. This is an opportune time for a modest meal and a warm cup of tea. There is no need for urgency.
   PL:
565. [Kwestia głosowa [lobby_noon_10208_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=lobby_noon_10208_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Kwestia głosowa [lobby_noon_10208_1] (Afternoon Greeting)] 정오 훈련은 다음으로 미루려 합니다.\n오히려… 지금은 혹시 빠졌던 사실은 없었는지, 검술을 기록한 책자를 검토하는 것이 좋겠네요.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=lobby_noon_10208_1].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I plan to postpone my noon training until next time.\nI... believe that it is best that I review my book of techniques to ensure that I have not left anything behind.
   PL:
567. [Kwestia głosowa [lobby_night_10208_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=lobby_night_10208_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Kwestia głosowa [lobby_night_10208_1] (Evening Greeting)] 달이 새하얗게 빛나고 있습니다. 밝게, 가리워지는 부분 없이. 지금이 적기겠군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=lobby_night_10208_1].dlg
   limit: do 120 znaków
   EN: The pale moon glimmers white. With no trace of shadows, bright. Now is the time most apt.
   PL:
569. [Kwestia głosowa [smalltalk_10208_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=smalltalk_10208_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Kwestia głosowa [smalltalk_10208_1] (Chatter #1)] 홍매화의 꽃잎을 던지고, 그 잎들을 조각내는 무예를 연습했던 적도 있었죠. 붉은 꽃잎이 사방으로 흩날리는 것은, 과히 아름다웠습니다.\n지금도 종종, 그 아름다운 광경을 보곤 합니다. 좀 더 액체에 가깝기는 하나.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=smalltalk_10208_1].dlg
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I once trained my precision by casting the red plum petals under the starry sky... and rending them before they hit the floor. The sight of scattering red petals was... I daresay that it was quite beautiful.\nI witness that beauty still, from time to time. The only difference is that the petals are more liquid than solid.
   PL:
571. [Kwestia głosowa [smalltalk_10208_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=smalltalk_10208_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Kwestia głosowa [smalltalk_10208_2] (Chatter #2)] 검술에 집착하는 건 어느 누구든, 계에 몸을 담고 있는 일원이라면 같겠지만…\n몸으로 배우는 시기는 이미 지난 터라, 이렇게 머리로 하는 공부를 하고 있습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=smalltalk_10208_2].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Obsession with the blade is a shared passion among those who are a part of the Lineage.\nBut I believe that I am past the stage of learning via muscle memory. Now, I train with my mind.
   PL:
573. [Kwestia głosowa [smalltalk_10208_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=smalltalk_10208_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Kwestia głosowa [smalltalk_10208_3] (Chatter #3)] 검의 흐름을 보면, 간혹 그것이 무술이라기 보단 예술 같다는 생각이 들지 않나요.\n흐름이 끊기지 않게, 유려히 하늘 위를 도화지 삼아… 아, 이런. 잠시 상상에 취해버렸군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=smalltalk_10208_3].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Witness the whirling arc of the blade. Does it not resemble art beyond the realms of martial techniques?\nLet the sky be the paper upon which my blade draws an arc that breaks not... Ah, I seem to have lost myself for a moment.
   PL:
575. [Kwestia głosowa [smalltalk_10208_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=smalltalk_10208_4].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Kwestia głosowa [smalltalk_10208_4] (Post-Uptie Chat 1)] 이 정도 뿐입니까, 흑운회. 야음을 틈타 우리의 터전 턱 끝까지 점거한 무뢰한들 치고는 성의 없이 흩어지는군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=smalltalk_10208_4].dlg
   limit: do 210 znaków
   EN: After going through so much trouble to advance before our gates under the cover of night... is this all you could muster, Kurokumo Clan? You scatter so helplessly.
   PL:
577. [Kwestia głosowa [smalltalk_10208_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=smalltalk_10208_5].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Kwestia głosowa [smalltalk_10208_5] (Post-Uptie Chat 2)] 저들은 스스로 흩날리는 꽃잎이 된 것도 자각하지 못할 것입니다. 같은 '검'이라는 도구를 쓰면서도 격의 차이가 이리도 현격하니.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=smalltalk_10208_5].dlg
   limit: do 260 znaków
   EN: They will not, to their last moments of consciousness, understand that they have become naught but red petals blowing in the wind. Though our tools are much alike, I remain a step above them still.
   PL:
579. [Kwestia głosowa [neglect_10208_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=neglect_10208_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Kwestia głosowa [neglect_10208_1] (Idle)] 종일 가만히 있으셔도 괜찮습니다. 달과 좀 더 이야기하죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=neglect_10208_1].dlg
   limit: do 120 znaków
   EN: You may remain still all day. I shall converse with the moon.
   PL:
581. [Kwestia głosowa [gacksung_10208_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=gacksung_10208_1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Kwestia głosowa [gacksung_10208_1] (Uptying)] 오늘은 검무를 펼치기 좋은 밤입니다. 달을 머금은 칼날 끝에서 피어나는 꽃무리가 절경이죠. 꽃놀이는 어떠신지.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=gacksung_10208_1].dlg
   limit: do 230 znaków
   EN: This is a good night to engage in a dance of blades. Particularly exquisite are the flowers blossoming from the tip of a moon-dipped blade. Why not go and appreciate the petals?
   PL:
583. [Kwestia głosowa [formation_10208_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=formation_10208_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Kwestia głosowa [formation_10208_1] (Deployment)] 출정이군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=formation_10208_1].dlg
   limit: do 120 znaków
   EN: So we march.
   PL:
585. [Kwestia głosowa [battleentry_10208_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battleentry_10208_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Kwestia głosowa [battleentry_10208_1] (Stage Entry)] 꽃을 피워볼까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battleentry_10208_1].dlg
   limit: do 120 znaków
   EN: Let the flowers bloom.
   PL:
587. [Kwestia głosowa [battle_select_10208_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_select_10208_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Kwestia głosowa [battle_select_10208_1] (Viewed in Battle)] 즐기고 계신가요?
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_select_10208_1].dlg
   limit: do 120 znaków
   EN: Are you enjoying yourself?
   PL:
589. [Kwestia głosowa [battle_endcommand_10208_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_endcommand_10208_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Kwestia głosowa [battle_endcommand_10208_1] (Commencing Attack)] 무뢰배들.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_endcommand_10208_1].dlg
   limit: do 120 znaków
   EN: Scoundrels.
   PL:
591. [Kwestia głosowa [battle_enemy_break_10208_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_enemy_break_10208_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Kwestia głosowa [battle_enemy_break_10208_1] (Enemy Stagger)] 흐드러지게.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_enemy_break_10208_1].dlg
   limit: do 120 znaków
   EN: Let it blossom.
   PL:
593. [Kwestia głosowa [battle_break_10208_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_break_10208_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Kwestia głosowa [battle_break_10208_1] (Staggered)] 으음.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_break_10208_1].dlg
   limit: do 120 znaków
   EN: Mmm.
   PL:
595. [Kwestia głosowa [battle_kill_10208_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_kill_10208_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Kwestia głosowa [battle_kill_10208_1] (Enemy Killed)] 피어나리.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_kill_10208_1].dlg
   limit: do 120 znaków
   EN: Like a bed of flowers.
   PL:
597. [Kwestia głosowa [battle_dead_10208_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_dead_10208_1].desc
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Kwestia głosowa [battle_dead_10208_1] (Death)] 홍매화… 제게도… 피어나는 것… 이었군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_dead_10208_1].dlg
   limit: do 120 znaków
   EN: So... the red plum blossom... blooms from me all the same...
   PL:
599. [Kwestia głosowa [choice_success_p_10208_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=choice_success_p_10208_2].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Kwestia głosowa [choice_success_p_10208_2] (Check Passed)] 어긋날 연유도 없죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=choice_success_p_10208_2].dlg
   limit: do 120 znaków
   EN: No cause for it to be amiss.
   PL:
601. [Kwestia głosowa [choice_fail_n_10208_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=choice_fail_n_10208_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Kwestia głosowa [choice_fail_n_10208_1] (Check Failed)] 어그러지는 것 또한 필연.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=choice_fail_n_10208_1].dlg
   limit: do 120 znaków
   EN: It was fated to be amiss.
   PL:
603. [Kwestia głosowa [battle_clear_10208_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_clear_10208_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Kwestia głosowa [battle_clear_10208_1] (Victory Cry)] 불량한 꽃들을 흩뜨려냈습니다. 이제 우리가 지낼 자리를 봐두어 볼까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_clear_10208_1].dlg
   limit: do 120 znaków
   EN: I have cast the unsightly flowers from here. Let us see where we will now reside.
   PL:
605. [Kwestia głosowa [battle_clear_ex_10208_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_clear_ex_10208_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Kwestia głosowa [battle_clear_ex_10208_1] (Extra Conditions Fulfilled)] 꽃은 지고, 새로운 나무가 이 곳에 움틀 것입니다. 그것이 우리의 터전을 수호할 재목이라는 건 틀림없는 사실이죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_clear_ex_10208_1].dlg
   limit: do 180 znaków
   EN: When the flowers wither, a new tree shall take root here. It will grow to be a pillar that will protect our home. I am certain of that.
   PL:
607. [Kwestia głosowa [battle_defeat_10208_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_defeat_10208_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Kwestia głosowa [battle_defeat_10208_1] (Defeat Wail)] 우리는… 정처 없이 떠도는 떠돌이, 흙에 내려 앉지 못한 씨앗… 언제쯤 정착할 수 있을지.
   źródło: PersonalityVoiceDlg/Voice_Faust_SwordGroup_10208.json :: dataList[id=battle_defeat_10208_1].dlg
   limit: do 140 znaków
   EN: We are... wanderers without destinations. Seeds without soil to take root in... When will our home be found?
   PL:

## [00] Wuthering Heights Butler — Faust — 워더링하이츠 버틀러
- ID Tożsamości: `10209` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 4 · HP bazowe: 76 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Sinking

609. [Karta Tożsamości — tytuł] 워더링하이츠\n버틀러
   źródło: Personalities.json :: dataList[id=10209].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Wuthering Heights\nButler
   PL:
610. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10209].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10209].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Karta Tożsamości — opis] 파우스트의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10209].desc
   limit: do 120 znaków
   EN: Faust's 9th Identity
   PL:
613. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 압수
   źródło: Skills_personality-02.json :: dataList[id=1020901].levelList[level=1].name ; dataList[id=1020901].levelList[level=2].name ; dataList[id=1020901].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Confiscation
   PL:
614. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Sinking] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1020901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 2 [Sinking]
   PL:
615. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1020901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1020901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL:
616. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1020901].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 6+ [Sinking], Coin Power +1
   PL:
617. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 불청객 맞이
   źródło: Skills_personality-02.json :: dataList[id=1020902].levelList[level=1].name ; dataList[id=1020902].levelList[level=2].name ; dataList[id=1020902].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Interloper Reception
   PL:
618. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Sinking] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +2 [Sinking] Count
   PL:
619. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상의 [Sinking]이 5 이상이면 , 합 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1020902].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 5+ [Sinking], Clash Power +1
   PL:
620. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1020902].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL:
621. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking]이 5 이상이면 , 합 위력 +1\n[WhenUse] 대상의 [Sinking] 횟수가 3 이상이면, 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1020902].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 5+ [Sinking], Clash Power +1\n[WhenUse] If target has 3+ [Sinking] Count, Coin Power +1
   PL:
622. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
623. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 접객도 4식 봉심
   źródło: Skills_personality-02.json :: dataList[id=1020903].levelList[level=3].name ; dataList[id=1020903].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Reception Arts 4: Heartseal
   PL:
624. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020903].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1020903].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 622 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [EchoOfMansion] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1020903].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1020903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EchoOfMansion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor
   EN: [OnSucceedAttack] Inflict 2 [EchoOfMansion] next turn
   PL:
626. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상에게 [EchoOfMansion]가 있으면, [Sinking] 횟수 3 증가
   źródło: Skills_personality-02.json :: dataList[id=1020903].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1020903].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EchoOfMansion], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target has [EchoOfMansion], inflict +3 [Sinking] Count
   PL:
627. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking] 횟수가 5 이상이면, 코인 위력 +2
   źródło: Skills_personality-02.json :: dataList[id=1020903].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 5+ [Sinking] Count, Coin Power +2
   PL:
628. [Obrona (ulepszenia 1,4) — nazwa] 사냥 대비
   źródło: Skills_personality-02.json :: dataList[id=1020904].levelList[level=1].name ; dataList[id=1020904].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 7 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Hunting Plans
   PL:
629. [Obrona (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking]이 10 이상이면, 코인 위력 +3
   źródło: Skills_personality-02.json :: dataList[id=1020904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 10+ [Sinking], Coin Power +3
   PL:
630. [Obrona (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking]이 10 이상이면, 코인 위력 +7
   źródło: Skills_personality-02.json :: dataList[id=1020904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 10+ [Sinking], Coin Power +7
   PL:
631. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Gloom) — nazwa] 버틀러식 대응
   źródło: Passives.json :: dataList[id=1020901].name
   limit: do 40 znaków
   EN: Butler Style Response
   PL:
632. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Gloom) — opis] - 합 승리 시 대상에게 [Sinking] 1 부여 (턴 당 3회)
   źródło: Passives.json :: dataList[id=1020901].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: - Clash Win: Inflict 1 [Sinking] on target (3 times per turn)
   PL:
633. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Gloom) — podsumowanie] 합 승리 시 [Sinking] 1 부여
   źródło: Passives.json :: dataList[id=1020901].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Clash Win: Inflict 1 [Sinking]
   PL:
634. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Gloom) — nazwa] 버틀러식 대응
   źródło: Passives.json :: dataList[id=1020911].name
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Gloom) — opis] - 합 승리 시 대상에게 [Sinking] 1 부여 (턴 당 3회)\n- 대상에게 [EchoOfMansion]가 있으면 대신 3 부여
   źródło: Passives.json :: dataList[id=1020911].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [EchoOfMansion]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor
   EN: - Clash Win: Inflict 1 [Sinking] on target (3 times per turn)\n- If the target has [EchoOfMansion], inflict 3 [Sinking] instead
   PL:
636. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Gloom) — podsumowanie] 합 승리 시 [Sinking] 1 부여
   źródło: Passives.json :: dataList[id=1020911].summary
   (powtórzenie elementu 633 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — nazwa] 그 날을 위한 훈련
   źródło: Passives.json :: dataList[id=1020921].name
   limit: do 40 znaków
   EN: Anticipatory Training
   PL:
638. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — opis] 정신력이 가장 낮은 아군 1명이 [Sinking]이 5 이상 부여된 대상에게 공격 적중 시 자신의 정신력 2 회복 (턴 당 4회)
   źródło: Passives.json :: dataList[id=1020921].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When 1 ally that has the lowest SP hits an enemy that has 5+ [Sinking], the ally heals 2 SP On Hit (4 times per turn)
   PL:
639. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — podsumowanie] 조건 만족 시 정신력 회복
   źródło: Passives.json :: dataList[id=1020921].summary
   limit: do 120 znaków
   EN: Conditional SP healing
   PL:
640. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Gloom) — nazwa] 그 날을 위한 훈련
   źródło: Passives.json :: dataList[id=1020931].name
   (powtórzenie elementu 637 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Gloom) — opis] 정신력이 가장 낮은 아군 1명이 [Sinking]이 5 이상 부여된 대상에게 공격 적중 시 자신의 정신력 3 회복 (턴 당 4회)
   źródło: Passives.json :: dataList[id=1020931].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When 1 ally that has the lowest SP hits an enemy that has 5+ [Sinking], the ally heals 3 SP On Hit (4 times per turn)
   PL:
642. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Gloom) — podsumowanie] 조건 만족 시 정신력 회복
   źródło: Passives.json :: dataList[id=1020931].summary
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Kwestia głosowa [get_10209_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=get_10209_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Kwestia głosowa [get_10209_1] (Identity Acquisition)] 실례하겠습니다. 당가에서 준비한 애프터눈 티입니다.\n편안한 시간 되시기를.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=get_10209_1].dlg
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Excuse me. Here is a cup of afternoon tea, courtesy of this house.\nPlease, enjoy your time here.
   PL:
645. [Kwestia głosowa [lobby_morning_10209_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=lobby_morning_10209_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Kwestia głosowa [lobby_morning_10209_1] (Morning Greeting)] 아침 식사는 간단한 커스터드와 곁들이실 포도주를 준비했습니다. 식후 즐기실 홍차도 준비할 예정이니, 차분히 즐기시기를.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=lobby_morning_10209_1].dlg
   limit: do 210 znaków
   EN: We have prepared a simple spread of custard and a glass of wine for your breakfast. Please relax and enjoy; a cup of black tea will be provided after this meal.
   PL:
647. [Kwestia głosowa [lobby_noon_10209_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=lobby_noon_10209_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Kwestia głosowa [lobby_noon_10209_1] (Afternoon Greeting)] 이 저택은 해가 잘 들지 않습니다. 오티스 님의 명령대로, 화목난로를 더욱 세게 지폈습니다. 가까이 와서 몸을 녹이시길.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=lobby_noon_10209_1].dlg
   limit: do 200 znaków
   EN: This manor rarely gets any sunlight. Fuel has been added to the wood stove as per Chief Butler Outis' orders. Warm yourself by the flame, if you will.
   PL:
649. [Kwestia głosowa [lobby_night_10209_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=lobby_night_10209_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [Kwestia głosowa [lobby_night_10209_1] (Evening Greeting)] 추위에 잘 버틸 수 있는 오리 깃털이 든 침구로 준비하라고 하시더군요. 그럼, 편안한 밤이 되시기를.\n저희는 사냥과 관련된 회의가 소집되어.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=lobby_night_10209_1].dlg
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A warm, thick duck-down bedding has been prepared in anticipation of the cold. Please have a restful night.\nWe must depart to join a meeting regarding a hunt.
   PL:
651. [Kwestia głosowa [smalltalk_10209_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=smalltalk_10209_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Kwestia głosowa [smalltalk_10209_1] (Chatter #1)] 오티스 님은 저희를 대신해서 마님과 많은 소통을 나누시더군요. 어쩔 땐 그 다음 날까지 그 이야기가 끊이지 않고 이어지는 적도 있더군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=smalltalk_10209_1].dlg
   limit: do 190 znaków
   EN: Chief Butler Outis converses day and night with the Mistress in our stead. Some nights, her communication with the mistress lasts until sunrise.
   PL:
653. [Kwestia głosowa [smalltalk_10209_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=smalltalk_10209_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [Kwestia głosowa [smalltalk_10209_2] (Chatter #2)] 금일 지하가… 다소 소란스러울 수 있겠습니다. 사냥을 대비하여 버틀러들의 합을 맞추는 시간이 있을 수 있으니, 날붙이 소리 등이 울려퍼져도 안심하시길 부탁드립니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=smalltalk_10209_2].dlg
   limit: do 230 znaków
   EN: You may hear some... commotion coming from the basement. The Butlers are training in preparation for the hunt; please do not allow the sounds of clashing metal to worry your mind.
   PL:
655. [Kwestia głosowa [smalltalk_10209_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=smalltalk_10209_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Kwestia głosowa [smalltalk_10209_3] (Chatter #3)] 차는 제뱌찌 협회를 통해 배송 받는 최상급 잎을, 전혀 부수지 않는 방식으로 준비하여 대접해드리고 있습니다. 선대부터 끊이지 않는, 이 워더링하이츠를 대표하는 차종이죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=smalltalk_10209_3].dlg
   limit: do 390 znaków
   EN: This tea is prepared using leaves delivered to this location by the Devyat' Association, which are then infused directly without being broken. It would be no hyperbole to say that this tea variety represents the utmost excellence of Wuthering Heights that has been passed down through the generations.
   PL:
657. [Kwestia głosowa [smalltalk_10209_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=smalltalk_10209_4].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Kwestia głosowa [smalltalk_10209_4] (Post-Uptie Chat 1)] 아, 다소 소란스러웠나요. 죄송합니다. 이번 불청객은 다소 날뛰는 경향이 있어… 퇴거시키는데 조금 힘든 부분이 있었습니다.\n모쪼록, 이해해주시기를.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=smalltalk_10209_4].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ah, has the noise disturbed you? Our sincere apologies. An uninvited guest had appeared on the premises... and it took the Butlers quite the effort to persuade them to leave the premises.\nPlease, do understand.
   PL:
659. [Kwestia głosowa [smalltalk_10209_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=smalltalk_10209_5].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Kwestia głosowa [smalltalk_10209_5] (Post-Uptie Chat 2)] 물론, 불청객의 대응을 하면서 생긴 파손품이나 얼룩은 청소를 전담하는 이 저택의 우수 버틀러들이 해결할 것입니다.\n주인께서는 걱정하실 필요 없습니다. 모든 것은, 일어나기 전으로 돌아갈 것입니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=smalltalk_10209_5].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Naturally, any and all damages or stains incurred in response to the uninvited guests will be taken care of by the excellent cleaning-expert Butlers of this manor.\nThere is no need for the Master to worry; it will all be returned to as it was before.
   PL:
661. [Kwestia głosowa [neglect_10209_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=neglect_10209_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [Kwestia głosowa [neglect_10209_1] (Idle)] …생각을 하시는데 제가 방해된다면, 잠시 자리를 비워드리겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=neglect_10209_1].dlg
   limit: do 130 znaków
   EN: ... If my presence disturbs your deliberation, then the room will be vacated for your sole use.
   PL:
663. [Kwestia głosowa [gacksung_10209_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=gacksung_10209_1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [Kwestia głosowa [gacksung_10209_1] (Uptying)] …방문객께서는 이쪽으로. 외람되오나 초대받지 않으신 분께서는 …즉시 퇴거 절차를 밟아주셔야겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=gacksung_10209_1].dlg
   limit: do 220 znaków
   EN: ... Come this way, dear guests. For any and all uninvited guests, though we sincerely apologize for this impudence, we must ask you to immediately vacate the premises.
   PL:
665. [Kwestia głosowa [formation_10209_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=formation_10209_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Kwestia głosowa [formation_10209_1] (Deployment)] 부르신다면 언제든.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=formation_10209_1].dlg
   limit: do 120 znaków
   EN: Always ready to be summoned.
   PL:
667. [Kwestia głosowa [battleentry_10209_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battleentry_10209_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Kwestia głosowa [battleentry_10209_1] (Stage Entry)] 파우스트가 맞이하죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battleentry_10209_1].dlg
   limit: do 120 znaków
   EN: Faust will receive the guests.
   PL:
669. [Kwestia głosowa [battle_select_10209_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_select_10209_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Kwestia głosowa [battle_select_10209_1] (Viewed in Battle)] 불편하신 점이라도.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_select_10209_1].dlg
   limit: do 120 znaków
   EN: Is something not to your liking?
   PL:
671. [Kwestia głosowa [battle_endcommand_10209_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_endcommand_10209_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Kwestia głosowa [battle_endcommand_10209_1] (Commencing Attack)] …이쪽으로.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_endcommand_10209_1].dlg
   limit: do 120 znaków
   EN: ... This way, please.
   PL:
673. [Kwestia głosowa [battle_enemy_break_10209_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_enemy_break_10209_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Kwestia głosowa [battle_enemy_break_10209_1] (Enemy Stagger)] 품행이 단정하지 않군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_enemy_break_10209_1].dlg
   limit: do 120 znaków
   EN: How ill-mannered.
   PL:
675. [Kwestia głosowa [battle_break_10209_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_break_10209_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Kwestia głosowa [battle_break_10209_1] (Staggered)] 헛…
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_break_10209_1].dlg
   limit: do 120 znaków
   EN: Hup...
   PL:
677. [Kwestia głosowa [battle_kill_10209_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_kill_10209_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Kwestia głosowa [battle_kill_10209_1] (Enemy Killed)] 즉시, 퇴거하시지요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_kill_10209_1].dlg
   limit: do 120 znaków
   EN: Please vacate the premises. Immediately.
   PL:
679. [Kwestia głosowa [battle_dead_10209_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_dead_10209_1].desc
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Kwestia głosowa [battle_dead_10209_1] (Death)] 죄송합니다… 오티스 님, 마님. 제게 주어진 일을…
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_dead_10209_1].dlg
   limit: do 120 znaków
   EN: My deepest apologies, Lady Outis, Mistress. I have failed to complete my... duties...
   PL:
681. [Kwestia głosowa [choice_success_p_10209_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=choice_success_p_10209_2].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Kwestia głosowa [choice_success_p_10209_2] (Check Passed)] 간단합니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=choice_success_p_10209_2].dlg
   limit: do 120 znaków
   EN: Effortless.
   PL:
683. [Kwestia głosowa [choice_fail_n_10209_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=choice_fail_n_10209_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Kwestia głosowa [choice_fail_n_10209_1] (Check Failed)] 아직 미숙한 부분이 있을 줄은…
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=choice_fail_n_10209_1].dlg
   limit: do 120 znaków
   EN: These deficiencies were unexpected...
   PL:
685. [Kwestia głosowa [battle_clear_10209_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_clear_10209_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Kwestia głosowa [battle_clear_10209_1] (Victory Cry)] 불청객의 대응을 완료했습니다. 아직, 그 날의 사냥을 진행하기에는 조금 모자람이 있군요. 보완하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_clear_10209_1].dlg
   limit: do 190 znaków
   EN: The uninvited guests have been properly taken care of. A few possible points of failure for the hunt have been identified. They will be addressed.
   PL:
687. [Kwestia głosowa [battle_clear_ex_10209_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_clear_ex_10209_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Kwestia głosowa [battle_clear_ex_10209_1] (Extra Conditions Fulfilled)] 완벽하게 대응했습니다. 이 기세로… 치프 버틀러가 계획하는 사냥까지 성공적으로 완수해보이죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_clear_ex_10209_1].dlg
   limit: do 120 znaków
   EN: A perfect response. Let this success inspire us to lead the Chief Butler's hunt to victory.
   PL:
689. [Kwestia głosowa [battle_defeat_10209_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_defeat_10209_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Kwestia głosowa [battle_defeat_10209_1] (Defeat Wail)] 죄송합니다. 응대에 문제가 생긴 것 같습니다. …다음 번엔 심려를 끼치지 않을 수 있도록 최선을 다하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Butler_10209.json :: dataList[id=battle_defeat_10209_1].dlg
   limit: do 150 znaków
   EN: My most sincere apologies; our response was far from acceptable. ... I shall try my utmost to not disappoint you.
   PL:

## [000] MultiCrack Office Rep — Faust — 멀티크랙 사무소 대표
- ID Tożsamości: `10210` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 4 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Charge

691. [Karta Tożsamości — tytuł] 멀티크랙 사무소\n대표
   źródło: Personalities.json :: dataList[id=10210].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: MultiCrack Office\nRep
   PL:
692. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10210].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10210].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Karta Tożsamości — opis] 파우스트의 열번째 인격
   źródło: Personalities.json :: dataList[id=10210].desc
   limit: do 120 znaków
   EN: Faust's 10th Identity
   PL:
695. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 40Y-3 가동
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=1].name ; dataList[id=1021001].levelList[level=2].name ; dataList[id=1021001].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: 40Y-3 Activation
   PL:
696. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수를 5 소모하여 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Coin Power +1
   PL:
697. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count
   PL:
698. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] [Charge] 횟수를 5 소모하여 코인 위력 +1<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Coin Power +1<style="highlight"></style>
   PL:
699. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +<style="highlight">3</style> [Charge] Count
   PL:
700. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] [Charge] 횟수를 5 소모하여 코인 위력 <style="highlight">+2</style>
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Coin Power <style="highlight">+2</style>
   PL:
701. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +3 [Charge] Count<style="highlight"></style>
   PL:
702. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 충전 역류
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=1].name ; dataList[id=1021002].levelList[level=2].name ; dataList[id=1021002].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Charge Countercurrent
   PL:
703. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면, 최대 체력의 2 x (10 - 현재 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수가 10으로 증가\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power +1
   PL:
704. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] 이 스킬을 포함한 공명이 3 이상이면, 보유한 [Charge] 횟수를 전부 소모하여 이 스킬로 소모한 [Charge] 횟수당 피해량 +([Charge])% (최대 60%)
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 3+ Reson. including this Skill, consume all [Charge] Count on self and deal +([Charge])% damage for every [Charge] Count consumed by this Skill (max 60%)
   PL:
705. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면, 최대 체력의 2 x (10 - 현재 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수가 10으로 증가\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 +1<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power +1<style="highlight"></style>
   PL:
706. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] 이 스킬을 포함한 공명이 3 이상이면, 보유한 [Charge] 횟수를 전부 소모하여 이 스킬로 소모한 [Charge] 횟수당 피해량 +<style="highlight">([Charge] + 3)% (최대 120%)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 3+ Reson. including this Skill, consume all [Charge] Count on self and deal +<style="highlight">([Charge] + 3)</style>% damage for every [Charge] Count consumed by this Skill (max <style="highlight">120%</style>)
   PL:
707. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면, 최대 체력의 2 x (10 - 현재 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수가 10으로 증가\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 <style="highlight">+2</style>
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power <style="highlight">+2</style>
   PL:
708. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] 이 스킬을 포함한 공명이 3 이상이면, 보유한 [Charge] 횟수를 전부 소모하여 이 스킬로 소모한 [Charge] 횟수당 피해량 +<style="highlight">([Charge] + 4)% (최대 180%)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021002].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 3+ Reson. including this Skill, consume all [Charge] Count on self and deal +<style="highlight">([Charge] + 4)</style>% damage for every [Charge] Count consumed by this Skill (max <style="highlight">180%</style>)
   PL:
709. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 40Y-3 충전
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=3].name ; dataList[id=1021003].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: 40Y-3 Charge
   PL:
710. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [Charge]이 2 이상이면, 코인 위력 +2
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 2+ [Charge], Coin Power +2
   PL:
711. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] ([Charge] + 4)만큼 자신의 [Charge] 횟수 증가 (최대 7)
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] + 4) [Charge] Count (max 7)
   PL:
712. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] ([Charge] + 4)만큼 자신의 [Charge] 횟수 증가 (최대 7)
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 711 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [Charge]이 3 이상이면, [Charge]당 피해량 +4% (최대 20%)
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 3+ [Charge], deal +4% damage for every [Charge] (max 20%)
   PL:
714. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">[Charge]당 코인 위력 +1 (최대 4)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: <style="highlight">Coin Power +1 for every [Charge] (max 4)</style>
   PL:
715. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] ([Charge] + <style="highlight">5</style>)만큼 자신의 [Charge] 횟수 증가 (최대 <style="highlight">8</style>)
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] + <style="highlight">5</style>) [Charge] Count (max <style="highlight">8</style>)
   PL:
716. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] ([Charge] + <style="highlight">5</style>)만큼 자신의 [Charge] 횟수 증가 (최대 <style="highlight">8</style>)
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 715 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [Charge]이 3 이상이면, [Charge]당 피해량 <style="highlight">+8%</style> (최대 <style="highlight">40%</style>)
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 3+ [Charge], deal <style="highlight">+8%</style> damage for every [Charge] (max <style="highlight">40%</style>)
   PL:
718. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 질투 취약 1 부여\n- [Charge]이 2 이상이면, 추가로 1 부여</style>
   źródło: Skills_personality-02.json :: dataList[id=1021003].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Charge], [VioletTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [VioletTakeDamageUp] = 질투 취약 / Envy Fragility
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [VioletTakeDamageUp] next turn\n- At 2+ [Charge], inflict 1 additional [VioletTakeDamageUp]</style>
   PL:
719. [Obrona (ulepszenia 1,4) — nazwa] 충전
   źródło: Skills_personality-02.json :: dataList[id=1021004].levelList[level=1].name ; dataList[id=1021004].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Charge
   PL:
720. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 2 증가 (턴 당 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +2 [Charge] Count (2 times per turn)
   PL:
721. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 [Charge] 횟수 <style="highlight">4</style> 증가 (턴 당 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021004].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +<style="highlight">4</style> [Charge] Count (2 times per turn)
   PL:
722. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 전류 해체
   źródło: Passives.json :: dataList[id=1021001].name
   limit: do 40 znaków
   EN: Electrocurrent Dismantling
   PL:
723. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음\n[Charge]이 2 이상이면, 피해량이 ([Charge] x 3)%만큼 증가 (최대 15%)\n\n적을 처치하면 자신과 [Charge] 횟수가 가장 적은 아군 1명이 [Charge]만큼 [Charge] 횟수 증가 (최대 3, [Charge]을 소모하거나 스스로 획득하는 스킬을 보유한 아군에게 우선으로 적용됨)
   źródło: Passives.json :: dataList[id=1021001].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\nAt 2+ [Charge], deal +([Charge] x 3)% damage (max 15%)\n\nOn Kill, this unit and 1 ally that has the lowest [Charge] Count gain [Charge] Count equal to [Charge] (max 3, prioritizes allies that consume or gain [Charge])
   PL:
724. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — podsumowanie] [Charge] 횟수 10 소모할 때마다 [Charge] 얻음\n[Charge] 2 이상이면, 피해량 증가\n적 처치 시, 자신과 아군 1명 [Charge] 횟수 증가
   źródło: Passives.json :: dataList[id=1021001].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain [Charge] with every 10 [Charge] Count consumption\nAt 2+ [Charge], deal more damage\nOn Kill, this unit and 1 ally gain [Charge] Count
   PL:
725. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — nazwa] 전류 해체
   źródło: Passives.json :: dataList[id=1021011].name
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음\n[Charge]이 2 이상이면, 피해량이 ([Charge] x 3)%만큼 증가 (최대 15%)\n<style="highlight">- 대상의 체력이 50% 미만이면 ([Charge] x 5)%만큼 추가로 증가 (최대 25%)</style>\n\n적을 처치하면 자신과 [Charge] 횟수가 가장 적은 아군 <style="highlight">2</style>명이 <style="highlight">(2 + [Charge])</style>만큼 [Charge] 횟수 증가 (최대 <style="highlight">5</style>, [Charge]을 소모하거나 스스로 획득하는 스킬을 보유한 아군에게 우선으로 적용됨)
   źródło: Passives.json :: dataList[id=1021011].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\nAt 2+ [Charge], deal +([Charge] x 3)% damage (max 15%)\n<style="highlight">- If the target is at less than 50% HP, deal +([Charge] x 5)% more damage (max 25%)</style>\n\nOn Kill, this unit and <style="highlight">2 allies</style> that have the lowest [Charge] Count gain [Charge] Count equal to <style="highlight">([Charge] + 2)</style> (max <style="highlight">5</style>, prioritizes allies that consume or gain [Charge])
   PL:
727. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — podsumowanie] [Charge] 횟수 10 소모할 때마다 [Charge] 얻음\n[Charge] 2 이상이면, 피해량이 증가\n적 처치 시, 자신과 아군 2명 [Charge] 횟수 증가
   źródło: Passives.json :: dataList[id=1021011].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain [Charge] with every 10 [Charge] Count consumption\nAt 2+ [Charge], deal more damage\nOn Kill, this unit and 2 allies gain [Charge] Count
   PL:
728. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — nazwa] 해체 보조 전류
   źródło: Passives.json :: dataList[id=1021021].name
   limit: do 50 znaków
   EN: Auxiliary Dismantling Current
   PL:
729. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — opis] [Charge] 횟수가 가장 낮은 아군 1명이 적 처치 시 [Charge] 횟수 2 증가 (턴 당 1회, [Charge]을 소모하거나 스스로 획득하는 스킬을 보유한 아군에게 우선으로 적용됨)
   źródło: Passives.json :: dataList[id=1021021].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: When 1 ally that has the lowest [Charge] Count kills an enemy, the ally gains +2 [Charge] Count (once per turn, prioritizes allies that consume or gain [Charge])
   PL:
730. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Envy) — nazwa] 해체 보조 전류
   źródło: Passives.json :: dataList[id=1021031].name
   (powtórzenie elementu 728 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Envy) — opis] [Charge] 횟수가 가장 낮은 아군 1명이 적 처치 시 [Charge] 횟수 3 증가 (턴 당 1회, [Charge]을 소모하거나 스스로 획득하는 스킬을 보유한 아군에게 우선으로 적용됨)
   źródło: Passives.json :: dataList[id=1021031].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: When 1 ally that has the lowest [Charge] Count kills an enemy, the ally gains +3 [Charge] Count (once per turn, prioritizes allies that consume or gain [Charge])
   PL:
732. [Kwestia głosowa [get_10210_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=get_10210_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Kwestia głosowa [get_10210_1] (Identity Acquisition)] 이 계획에는 다수의 결함이 존재합니다만, 파우스트가 이 허점투성이 계획을 완전무결하게 만들어드리죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=get_10210_1].dlg
   limit: do 170 znaków
   EN: While there are numerous deficiencies and points of failure to this plan, Faust will hone it into utter, unfailing perfection.
   PL:
734. [Kwestia głosowa [lobby_morning_10210_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=lobby_morning_10210_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Kwestia głosowa [lobby_morning_10210_1] (Morning Greeting)] 아침의 커피 한 잔을 위해 팔 하나 정도는 항상 비워둘 수 있어요. 그래도 세 개가 남기 때문에…
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=lobby_morning_10210_1].dlg
   limit: do 150 znaków
   EN: An arm can always be spared for a cup of coffee in the morning. There are three more arms to utilize, after all.
   PL:
736. [Kwestia głosowa [lobby_noon_10210_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=lobby_noon_10210_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Kwestia głosowa [lobby_noon_10210_1] (Afternoon Greeting)] 사무소 카드를 사용했다면, 영수증은 반드시 제출해주세요.\n계속 누락한다면 점심 식사는 사비로 해결하도록 방침을 바꾸겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=lobby_noon_10210_1].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Please remember to submit the receipts after using a corporate credit card.\nThis Office may no longer provide a lunch budget should the employees continuously fail to submit their receipts.
   PL:
738. [Kwestia głosowa [lobby_night_10210_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=lobby_night_10210_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Kwestia głosowa [lobby_night_10210_1] (Evening Greeting)] 해 질 무렵까지 일해도 의체는 아프지 않아요.\n…삐걱거리게 된다면 정비를 해야겠지만요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=lobby_night_10210_1].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The prosthetic body does not feel muscular pain, even if it were to be put to work from sunrise to sunset.\n... However, a regular maintenance may be needed to prevent creaking.
   PL:
740. [Kwestia głosowa [smalltalk_10210_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=smalltalk_10210_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
741. [Kwestia głosowa [smalltalk_10210_1] (Chatter #1)] 혹시 머리 외에도 다른 의체를 고려하신다면, 트레스 협회의 인증을 받은 G10 모델 의족을 추천드립니다.\n좋은 다리를 가지면, 당신도 위험한 상황에서 빠르게 도망칠 수 있을 거예요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=smalltalk_10210_1].dlg
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If you would ever consider replacing more parts of your body than your head with prostheses, a good recommendation would be the Tres Association certified G10 model prosthetic legs.\nA high-performance ambulatory apparatus is very useful for making oneself scarce from high-risk situations.
   PL:
742. [Kwestia głosowa [smalltalk_10210_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=smalltalk_10210_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [Kwestia głosowa [smalltalk_10210_2] (Chatter #2)] 워프 열차 왕복권은 사비로 결제했습니다. 파우스트는 일등석으로 예약했죠.\n일반석이 아니라, 일등석을 예약한 이유에 대해서 아직 저는 알 수 없어요. 하지만 파우스트는 알고 있겠죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=smalltalk_10210_2].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The WARP train round trip ticket has been purchased via private funds, with Faust reserving a first class seat.\nI do not yet know why the first class ticket has been purchased instead of the economy class ticket; however, Faust must know of the reason.
   PL:
744. [Kwestia głosowa [smalltalk_10210_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=smalltalk_10210_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Kwestia głosowa [smalltalk_10210_3] (Chatter #3)] 전신 의체에 대해서도 고려해 보지 않은 건 아니지만… 더 좋은 의체로의 교체 비용과 리스크를 감당할 수 없어 선택하지 않았습니다.\n파우스트가 생각하기에, 교체가 편리한 부분 의체로 점차 업그레이드하는 것이 더 효율적이겠죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=smalltalk_10210_3].dlg
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A whole-body prosthetic has been considered, yes. ... However, the upgrade budget for higher-quality prosthetics and the related risks were too significant to be followed through.\nFaust believed it would be more efficient to slowly upgrade this body toward an increasingly stronger partial prosthetic.
   PL:
746. [Kwestia głosowa [smalltalk_10210_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=smalltalk_10210_4].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Kwestia głosowa [smalltalk_10210_4] (Post-Uptie Chat 1)] 이 정도 크기의 대검은 누구나 다룰 수 있습니다. 충분한 돈과 약간의 적응 시간, 그리고 믿을 수 있는 공방만 있다면 하루아침에 휘두를 수 있죠.\n물론 그걸로 어떤 전투 스타일을 추구할지는 본인의 재량이지만요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=smalltalk_10210_4].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A greatsword of this size can be wielded by any individual as long as they possess sufficient budget, enough time to acclimatize, and the work of a trusted workshop.\nOf course, it is up to each individual as to what kind of combat style they wish to employ.
   PL:
748. [Kwestia głosowa [smalltalk_10210_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=smalltalk_10210_5].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [Kwestia głosowa [smalltalk_10210_5] (Post-Uptie Chat 2)] 의체화된 신체는 대부분 통각을 느끼지 않죠. 그렇기에 저희 의체 해결사에겐 고통이나 부상에 대한 두려움이 없답니다.\n돈은 일반적인 치료보다 많이 들겠지만요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=smalltalk_10210_5].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Prosthetic bodies are rarely installed with pain receptors. Therefore, Fixers such as ourselves who utilize prosthetic bodies do not fear pain or injury.\n... It is much more expensive to fix a prosthetic than it is to heal flesh, however.
   PL:
750. [Kwestia głosowa [neglect_10210_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=neglect_10210_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Kwestia głosowa [neglect_10210_1] (Idle)] 부른 뒤에 조용히 사라지다니. 비효율적인 행동이네요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=neglect_10210_1].dlg
   limit: do 120 znaków
   EN: To summon someone and not address them is a highly inefficient action.
   PL:
752. [Kwestia głosowa [gacksung_10210_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=gacksung_10210_1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Kwestia głosowa [gacksung_10210_1] (Uptying)] 의뢰 목표를 처리했습니다. 이번 원정 의뢰도 철저히 준비한 보람이 있군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=gacksung_10210_1].dlg
   limit: do 170 znaków
   EN: The contract target has been taken care of. The meticulous preparation for this contract expedition has certainly borne fruit.
   PL:
754. [Kwestia głosowa [formation_10210_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=formation_10210_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Kwestia głosowa [formation_10210_1] (Deployment)] 준비는 완료했습니다. 출발하죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=formation_10210_1].dlg
   limit: do 120 znaków
   EN: All preparations have been made. Let us depart.
   PL:
756. [Kwestia głosowa [battleentry_10210_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battleentry_10210_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Kwestia głosowa [battleentry_10210_1] (Stage Entry)] 모델 40Y-3 충전. 전투 준비 완료.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battleentry_10210_1].dlg
   limit: do 120 znaków
   EN: Model 40Y-3 fully charged. Ready for deployment.
   PL:
758. [Kwestia głosowa [battle_select_10210_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_select_10210_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Kwestia głosowa [battle_select_10210_1] (Viewed in Battle)] 계획을 잊으셨나요?
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_select_10210_1].dlg
   limit: do 120 znaków
   EN: Have you forgotten the plan?
   PL:
760. [Kwestia głosowa [battle_endcommand_10210_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_endcommand_10210_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Kwestia głosowa [battle_endcommand_10210_1] (Commencing Attack)] 공격 범위 확인.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_endcommand_10210_1].dlg
   limit: do 120 znaków
   EN: Attack range confirmed.
   PL:
762. [Kwestia głosowa [battle_enemy_break_10210_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_enemy_break_10210_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Kwestia głosowa [battle_enemy_break_10210_1] (Enemy Stagger)] 효율적으로…
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_enemy_break_10210_1].dlg
   limit: do 120 znaków
   EN: Efficiently...
   PL:
764. [Kwestia głosowa [battle_break_10210_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_break_10210_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Kwestia głosowa [battle_break_10210_1] (Staggered)] 어…
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_break_10210_1].dlg
   limit: do 120 znaków
   EN: Uh...
   PL:
766. [Kwestia głosowa [battle_kill_10210_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_kill_10210_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Kwestia głosowa [battle_kill_10210_1] (Enemy Killed)] …처리했습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_kill_10210_1].dlg
   limit: do 120 znaków
   EN: ... dispatched.
   PL:
768. [Kwestia głosowa [battle_dead_10210_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_dead_10210_1].desc
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Kwestia głosowa [battle_dead_10210_1] (Death)] 보험은… 들어두었습니다…
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_dead_10210_1].dlg
   limit: do 120 znaków
   EN: I have... insurance...
   PL:
770. [Kwestia głosowa [choice_success_p_10210_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=choice_success_p_10210_2].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Kwestia głosowa [choice_success_p_10210_2] (Check Passed)] 파우스트의 계산대로네요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=choice_success_p_10210_2].dlg
   limit: do 120 znaków
   EN: As per Faust's calculations.
   PL:
772. [Kwestia głosowa [choice_fail_n_10210_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=choice_fail_n_10210_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Kwestia głosowa [choice_fail_n_10210_1] (Check Failed)] 오류가 있었군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=choice_fail_n_10210_1].dlg
   limit: do 120 znaków
   EN: There was an error.
   PL:
774. [Kwestia głosowa [battle_clear_10210_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_clear_10210_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Kwestia głosowa [battle_clear_10210_1] (Victory Cry)] 이 정도 승리는 당연한 일이죠. 파우스트의 지식대로 움직였으니까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_clear_10210_1].dlg
   limit: do 120 znaków
   EN: A predictable victory, guided by Faust's knowledge.
   PL:
776. [Kwestia głosowa [battle_clear_ex_10210_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_clear_ex_10210_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Kwestia głosowa [battle_clear_ex_10210_1] (Extra Conditions Fulfilled)] 계획보다 더 일찍 의뢰를 완수했네요. 저와 파우스트의 뛰어난 능력 덕분이지만, 여러분의 노력도 나쁘지 않았어요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_clear_ex_10210_1].dlg
   limit: do 210 znaków
   EN: This contract was completed far ahead of schedule. A majority of credit would go to Faust and my expertise, but your effort was at an acceptable level as well.
   PL:
778. [Kwestia głosowa [battle_defeat_10210_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_defeat_10210_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Kwestia głosowa [battle_defeat_10210_1] (Defeat Wail)] 원정은 실패했습니다. 퇴각 후 파손된 의체를 교체하고, 다시 준비해야겠군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Meca_10210.json :: dataList[id=battle_defeat_10210_1].dlg
   limit: do 180 znaków
   EN: This expedition was a failure. Expeditious retreat and prosthetic replacement are necessary before we prepare for the expedition once again.
   PL:

## [000] LCE E.G.O:: Ardor Blossom Star — Faust — LCE E.G.O:: 홍염살
- ID Tożsamości: `10211` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Burn

780. [Karta Tożsamości — tytuł] LCE E.G.O::\n홍염살
   źródło: Personalities.json :: dataList[id=10211].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCE E.G.O::\nArdor Blossom\nStar
   PL:
781. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10211].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10211].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Karta Tożsamości — opis] 파우스트의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10211].desc
   limit: do 120 znaków
   EN: Faust's 11th Identity
   PL:
784. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 착화
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=1].name ; dataList[id=1021101].levelList[level=2].name ; dataList[id=1021101].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Ignition
   PL:
785. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Combustion]이 10 이상이면, 피해량 +10%\n[WhenUse] [Combustion] 7 얻음, 자신의 [Combustion] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: [WhenUse] At 10+ [Combustion], deal +10% damage\n[WhenUse] Gain 7 [Combustion] and +1 [Combustion] Count
   PL:
786. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1021101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL:
787. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1021101].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1021101].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Gain 2 [Combustion]
   PL:
788. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1021101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1021101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 786 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 787 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Combustion]이 10 이상이면, 피해량 +10%\n[WhenUse] [Combustion] 7 얻음, 자신의 [Combustion] 횟수 1 증가\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 10 이상이면, 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: [WhenUse] At 10+ [Combustion], deal +10% damage\n[WhenUse] Gain 7 [Combustion] and +1 [Combustion] Count\n[WhenUse] At 10+ ([Combustion] on self + [Combustion] on target), Coin Power +1
   PL:
791. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack]자신의 [Combustion]이 10 이상이면, [Combustion] 1 추가 부여</style>
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[OnSucceedAttack] At 10+ [Combustion], inflict additional 1 [Combustion]</style>
   PL:
792. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=2].coinlist[#1].coindescs[#2].desc ; dataList[id=1021101].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Gain 2 [Combustion]<style="highlight"></style>
   PL:
793. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Combustion]이 10 이상이면, 피해량 +10%\n[WhenUse] [Combustion] 7 얻음, 자신의 [Combustion] 횟수 1 증가\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 10 당, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: [WhenUse] At 10+ [Combustion], deal +10% damage\n[WhenUse] Gain 7 [Combustion] and +1 [Combustion] Count\n[WhenUse] Coin Power +1 for every 10 ([Combustion] on self + [Combustion] on target) (max 2)
   PL:
794. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Combustion]이 10 이상이면, [Combustion] <style="highlight">3</style> 추가 부여
   źródło: Skills_personality-02.json :: dataList[id=1021101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] At 10+ [Combustion], inflict additional <style="highlight">3</style> [Combustion]
   PL:
795. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] E.G.O 홍염살 전개
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=1].name ; dataList[id=1021102].levelList[level=2].name ; dataList[id=1021102].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: E.G.O - A.B.S Activation
   PL:
796. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 자신의 [Combustion]이 10 이상이면, 피해량 +10%\n[WhenUse] 자신의 [Combustion] 횟수 4 증가
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [WhenUse]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]
   EN: At 10+ [Combustion], deal +10% damage\n[WhenUse] Gain +4 [Combustion] Count
   PL:
797. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1021102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 786 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1021102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1021102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 786 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1021102].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1021102].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
800. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Combustion]
   PL:
801. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 자신의 [Combustion] 10 당, 피해량 +10% (최대 20%)\n[WhenUse] 자신의 [Combustion] 횟수 4 증가\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 4 이상이면, 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [WhenUse]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]
   EN: Deal +10% damage for every 10 [Combustion] on self (max 20%)\n[WhenUse] Gain +4 [Combustion] Count\n[WhenUse] At 4+ ([Combustion] on self + [Combustion] on target), Coin Power +1
   PL:
802. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1021102].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Combustion]
   PL:
803. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 [Combustion] 10 당, 피해량 +10% (최대 20%)\n[WhenUse] 자신의 [Combustion] 횟수 4 증가\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 4 당, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [WhenUse]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]
   EN: Deal +10% damage for every 10 [Combustion] on self (max 20%)\n[WhenUse] Gain +4 [Combustion] Count\n[WhenUse] Coin Power +1 for every 4 ([Combustion] on self + [Combustion] on target) (max 2)
   PL:
804. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 대상의 [Combustion]이 15 이상이면, [Combustion] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021102].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 15+ [Combustion], inflict +2 [Combustion] Count on target
   PL:
805. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 불에 끌리는 마음으로
   źródło: Skills_personality-02.json :: dataList[id=1021103].levelList[level=3].name ; dataList[id=1021103].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Drawn by Flame
   PL:
806. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] [Combustion] 7 얻음, 자신의 [Combustion] 횟수 1 증가\n[BeforeUse] 자신의 [Combustion]이 30 이상이면, ‘홍염살 최대 감응 【열화침식】’으로 발동\n자신의 [Combustion] 5 당, 피해량 +7.5% (최대 30%)\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 10 이상이면, 기본 위력 +1\n[WhenUse] 자신의 잃은 체력이 30% 이상이면, 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1021103].levelList[level=3].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Combustion], [BeforeUse], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Combustion] = 화상 / Burn; [BeforeUse] = [사용전] / [Before Use]; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Gain 7 [Combustion] and +1 [Combustion] Count\n[BeforeUse] At 30+ [Combustion], activate "A.B.S Max Attunement 【Degraded Corrosion】" instead\nDeal +7.5% damage for every 5 [Combustion] on self (max 30%)\n[WhenUse] At 10+ ([Combustion] on self + [Combustion] on target), Base Power +1\n[WhenUse] If this unit is missing 30%+ HP, Coin Power +1
   PL:
807. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021103].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1021103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]
   PL:
808. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021103].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1021103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 807 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [StartBattle] [Combustion] 7 얻음, 자신의 [Combustion] 횟수 1 증가\n[BeforeUse] 자신의 [Combustion]이 30 이상이면, ‘홍염살 최대 감응 【열화침식】’으로 발동\n자신의 [Combustion] 5 당, 피해량 +12.5% (최대 50%)\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 10당, 기본 위력 +1 (최대 2)\n[WhenUse] 자신의 잃은 체력 30% 당, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-02.json :: dataList[id=1021103].levelList[level=4].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Combustion], [BeforeUse], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Combustion] = 화상 / Burn; [BeforeUse] = [사용전] / [Before Use]; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Gain 7 [Combustion] and +1 [Combustion] Count\n[BeforeUse] At 30+ [Combustion], activate "A.B.S Max Attunement 【Degraded Corrosion】" instead\nDeal +12.5% damage for every 5 [Combustion] on self (max 50%)\n[WhenUse] Base Power +1 for every 10 ([Combustion] on self + [Combustion] on target) (max 2)\n[WhenUse] For every 30% missing HP on this unit, Coin Power +1 (max 2)
   PL:
810. [Umiejętność 4 (×0) (ulepszenia 1,4) — nazwa] 홍염살 최대 감응 【열화침식】
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].name ; dataList[id=1021105].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 60 znaków
   EN: A.B.S Max Attunement 【Degraded Corrosion】
   PL:
811. [Umiejętność 4 (×0) (ulepszenie 1) — opis] 이 스킬 공격 종료 시 사망함.\n- 이 스킬을 사용하는 동안 체력이 1이 되면, 체력이 1로 유지됨.\n[WhenUse] 자신의 [Combustion] 5 당 피해량 +7.5% (최대 30%)\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 10 이상이면, 기본 위력 +1\n[WhenUse] 자신의 잃은 체력 30% 당, 코인 위력 +1 (최대 2)\n[BeforeAttack] 자신의 잃은 체력 20% 당, 공격 가중치 +1 (최대 2)
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: This unit dies after using this Skill\n- If HP drops to 1 while using this Skill, maintains HP at 1 for the duration of the Skill\n[WhenUse] Deal +7.5% damage for every 5 [Combustion] on self (max 30%)\n[WhenUse] At 10+ ([Combustion] on self + [Combustion] on target), Base Power +1\n[WhenUse] Coin Power +1 for every 30% missing HP on self (max 2)\n[BeforeAttack] Atk Weight +1 for every 20% missing HP on self (max 2)
   PL:
812. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1021105].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 799 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 807 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1021105].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 799 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 807 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1021105].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 799 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 잃은 체력 20% 당, 피해량 +10% (최대 30%)
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1021105].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal +10% damage for every 20% missing HP on self (max 30%)
   PL:
818. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 이 스킬 공격 종료 시 사망함.\n- 이 스킬을 사용하는 동안 체력이 1이 되면, 체력이 1로 유지됨.\n[WhenUse] 자신의 [Combustion] 5 당 피해량 +12.5% (최대 50%)\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 10당, 기본 위력 +1 (최대 2)\n[WhenUse] 자신의 잃은 체력 30% 당, 코인 위력 +1 (최대 3)\n[BeforeAttack] 자신의 잃은 체력 20% 당, 공격 가중치 +1 (최대 4)
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=4].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: This unit dies after using this Skill\n- If HP drops to 1 while using this Skill, maintains HP at 1 for the duration of the Skill\n[WhenUse] Deal +12.5% damage for every 5 [Combustion] on self (max 50%)\n[WhenUse] Base Power +1 for every 10 ([Combustion] on self + [Combustion] on target) (max 2)\n[WhenUse] Coin Power +1 for every 30% missing HP on self (max 3)\n[BeforeAttack] Atk Weight +1 for every 20% missing HP on self (max 4)
   PL:
819. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 4 [Combustion]
   PL:
820. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_personality-02.json :: dataList[id=1021105].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 819 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
821. [Obrona (ulepszenia 1,4) — nazwa] 홍염살의 감응도를 올려 공명하겠습니다.
   źródło: Skills_personality-02.json :: dataList[id=1021104].levelList[level=1].name ; dataList[id=1021104].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 60 znaków
   EN: Resonating by Raising A.B.S Attunement.
   PL:
822. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Combustion] 5 감소 (턴 당 1회)\n[OnSucceedEvade] 자신의 [Combustion] 5 감소 (턴 당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021104].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [OnSucceedEvade]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [WhenUse] Lose 5 [Combustion] (once per turn)\n[OnSucceedEvade] Lose 5 [Combustion] (once per turn)
   PL:
823. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 [Combustion]이 10 이상이면, 코인 위력 +3\n[WhenUse] 자신의 [Combustion] 5 감소 (턴 당 1회)\n[OnSucceedEvade] 자신의 [Combustion] 5 감소 (턴 당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021104].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [OnSucceedEvade]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [WhenUse] At 10+ [Combustion], Coin Power +3\n[WhenUse] Lose 5 [Combustion] (once per turn)\n[OnSucceedEvade] Lose 5 [Combustion] (once per turn)
   PL:
824. [Pasywka bojowa (od ulepszenia 1) — nazwa] 내화
   źródło: Passives.json :: dataList[id=1021101].name
   limit: do 40 znaków
   EN: Fireproof
   PL:
825. [Pasywka bojowa (od ulepszenia 1) — opis] [Combustion] 피해로 흐트러짐 상태가 되거나 체력이 1 미만으로 감소하지 않음.
   źródło: Passives.json :: dataList[id=1021101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Cannot be Staggered or fall below 1 HP due to [Combustion] damage
   PL:
826. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Wrath) — nazwa] 불나방
   źródło: Passives.json :: dataList[id=1021111].name
   limit: do 40 znaków
   EN: Flame Moth
   PL:
827. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Wrath) — opis] 전투 시작 시 자신의 잃은 체력이 80% 이상이고 [Combustion]이 30 미만이면, [Combustion]을 30까지 얻음. (스테이지 당 1회)\n\n턴 종료 시 자신의 [Combustion] 6당, 다음 턴에 [AttackUp] 1 얻음 (최대 5)\n\n사망 시 아래의 효과 발동\n- 모든 적에게 [Combustion] 2 부여. 자신의 [Combustion]을 나누어 부여 (1명당 최대 3)\n- 가장 부족한 속성의 E.G.O 자원 2종 2개씩 획득\n\n홍염살 최대 감응 【열화침식】 스킬의 효과로 사망하였으면, 효과가 강화됨\n- 모든 적에게 [Combustion] 3 부여. 자신의 [Combustion]을 나누어 부여 (1명당 최대 5)\n- 가장 부족한 속성의 E.G.O 자원 2종 2개씩 획득\n- 자신의 [Combustion]이 30 이상이었으면, 대기 해제되는 인원 1명에게 [AttackUp] 3 부여
   źródło: Passives.json :: dataList[id=1021111].desc
   limit: do 960 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [AttackUp]
   znaczenie tagów: [Combustion] = 화상 / Burn; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Combat Start: At 80%+ missing HP, and at less than 30 [Combustion], gain up to 30 [Combustion] (once per Encounter)\n\nTurn End: Gain 1 [AttackUp] next turn for every 6 [Combustion] on self (max 5)\n\nOn death, activate the following:\n- Inflict 2 [Combustion] on all enemies and inflict this unit's [Combustion] between all enemies (max 3 per enemy)\n- Gain 2 E.G.O resource for the 2 least-owned Affinities\n\nIf this unit died due to the A.B.S. Max Attunement 【Degraded Corrosion】 Skill, enhance the effect:\n- Inflict 3 [Combustion] on all enemies and inflict this unit's [Combustion] between all enemies (max 5 per enemy)\n- Gain 2 E.G.O resource for 2 least-owned E.G.O resources\n- If this unit had 30+ [Combustion], apply 3 [AttackUp] to 1 ally that Substitutes in
   PL:
828. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 잔열
   źródło: Passives.json :: dataList[id=1021121].name
   limit: do 40 znaków
   EN: Residual Heat
   PL:
829. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 정신력이 가장 낮은 아군 1명이 기본 스킬의 적중시 효과로 [Combustion]을 부여할 때 [Combustion] 2 추가 부여 (최대 3회 발동)\n- 피격 대상의 [Combustion]이 30 이상이면, 대신 [Combustion] 횟수 1 증가 (최대 3회 발동)
   źródło: Passives.json :: dataList[id=1021121].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When 1 ally that has the lowest SP inflicts [Combustion] with a Base Skill's On Hit effect, inflict 2 additional [Combustion] (max 3 times)\n- If the target the ally is attacking has 30+ [Combustion], inflict +1 [Combustion] Count instead (max 3 times)
   PL:
830. [Kwestia głosowa [get_10211_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=get_10211_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Kwestia głosowa [get_10211_1] (Identity Acquisition)] 개체의 전투 위협도 다소 높음, 하지만 특정 상황에서 자멸하는 특성을 반영하여… 홍염나방 최종 판정, WAW-5.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=get_10211_1].dlg
   limit: do 230 znaków
   EN: Subject's engagement threat level: moderately high. However, considering its self-destructive nature under specific circumstances... Ardor Blossom Moth final designation: WAW-5.
   PL:
832. [Kwestia głosowa [lobby_morning_10211_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=lobby_morning_10211_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Kwestia głosowa [lobby_morning_10211_1] (Morning Greeting)] 오전에 해야할 일로는 뒤틀림 진행 척도 확인, 죄종 개체수 점검, 환상체 격리 작업이 있습니다.\n오늘 하루도 꽤 바쁜 일정이 되겠군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=lobby_morning_10211_1].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The following tasks must be completed this morning: Distortion progression rate check, Peccatula population inspection, and Abnormality containment work.\nThere is much to be done today.
   PL:
834. [Kwestia głosowa [lobby_noon_10211_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=lobby_noon_10211_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
835. [Kwestia głosowa [lobby_noon_10211_1] (Afternoon Greeting)] 클리어 부서의 애프터 팀에서 새로운 환상체를 포획. 운반 중입니다.\n점심 시간은… 새 환상체에 대한 연구 시간으로 대신하는 편이 좋겠네요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=lobby_noon_10211_1].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The After Team of the Clearance department has captured a new Abnormality, which is currently en route to this facility.\nIt may be best that we replace today's allotted lunchtime with... research time for the new Abnormality.
   PL:
836. [Kwestia głosowa [lobby_night_10211_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=lobby_night_10211_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Kwestia głosowa [lobby_night_10211_1] (Evening Greeting)] 이상 씨, 열의는 좋지만, 너무 늦은 수면은 연구 효율에 악영향을 줍니다. LCE는 연구원의 정시 퇴근을…\n뭐. 이렇게 말해도 소용없겠군요. <color=#d4e1e8>자, 잠깐 불은 끄지 마시오. 아직…</color>
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=lobby_night_10211_1].dlg
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#d4e1e8>, </color>, \n
   EN: Yi Sang. Your passion is admirable, but delayed bedtime may adversely affect the efficacy of your research contributions. LCE promotes the timely departure of its employees—\n... Well, I don't suppose mere words will make him budge. <color=#d4e1e8>J-just a moment, I implore you to leave the lights on for now. There is still much—</color>
   PL:
838. [Kwestia głosowa [smalltalk_10211_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=smalltalk_10211_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Kwestia głosowa [smalltalk_10211_1] (Chatter #1)] 음. 유능함을 기준으로 보자면 LCE의 수석 연구원은 파우스트여야 옳습니다.\n그저… 지금의 제가 있을 자리가 아닌 것 뿐일 테죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=smalltalk_10211_1].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Mm. If merit were to be the sole criterion by which one's aptitude for the LCE Chief researcher position may be measured, then that role would have rightly gone to Faust.\nYet... that is simply not my place to be as I am now.
   PL:
840. [Kwestia głosowa [smalltalk_10211_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=smalltalk_10211_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [Kwestia głosowa [smalltalk_10211_2] (Chatter #2)] 뒤틀림이나 환상체는, 파우스트 정도의 천재가 아니라면 단순한 통계와 이론만으로 접근해서는 안 됩니다.\n시류를 읽는 직관과 학습에 대한 열의… 거기에 약간의 행운도 필요할 테죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=smalltalk_10211_2].dlg
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Unless one is a genius of Faust's caliber, one mustn't approach Distortions and Abnormalities equipped with only basic statistics and theories.\nThe other ingredients include intuition to be able to identify and read the trends, passion for the academics, and... some luck.
   PL:
842. [Kwestia głosowa [smalltalk_10211_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=smalltalk_10211_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Kwestia głosowa [smalltalk_10211_3] (Chatter #3)] PE 박스 형태로 추출되는 엔케팔린부터, 무너진 지부 출신의 연구원까지… LCE가 로보토미 코퍼레이션을 실질적으로 계승했다고 봐도 무방하겠죠.\n아직은 그 흔적을 쫓아가기 바쁘지만, 머지않아 앞서는 날도 도래할 것입니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=smalltalk_10211_3].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCE extracts Enkephalin in PE-Box forms and even employs a former L Corp. branch researcher... It would be no hyperbole to say that LCE has, in every way that matters, succeeded Lobotomy Corporation.\nThough we are still quite busy playing catch-up, we will one day surpass them.
   PL:
844. [Kwestia głosowa [smalltalk_10211_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=smalltalk_10211_4].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Kwestia głosowa [smalltalk_10211_4] (Post-Uptie Chat 1)] 날개는 인간에게 없는 신체 부위였기에, 처음 이 E.G.O로 날아오를 때는 많은 시행착오가 있었습니다. 그때를 생각하면… 실험섹터의 천장은 조금 높아지는 편이 좋을 것 같군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=smalltalk_10211_4].dlg
   limit: do 360 znaków
   EN: Given that wings were not originally a part of the human set of limbs, the very first attempts at flight with this E.G.O gear resulted in several... trials and errors. Using this experience as a lesson, perhaps it would be wise to raise the ceilings of the experiment sector somewhat.
   PL:
846. [Kwestia głosowa [smalltalk_10211_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=smalltalk_10211_5].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Kwestia głosowa [smalltalk_10211_5] (Post-Uptie Chat 2)] LCE에 모인 연구원들은 대부분 새로운 지식을 쫓아 모여들었죠. 마치, 불빛에 홀려 모여든 나방떼처럼.\n파우스트도 마찬가지였죠. 어쩌면 이 E.G.O를 배정 받은 것도 같은 이유일지도 모르겠네요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=smalltalk_10211_5].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Most researchers here at the LCE were enticed by the promise of new knowledge—like moths drawn to a flicker of flame.\nSo was Faust. Perhaps that explains the assignment of this E.G.O.
   PL:
848. [Kwestia głosowa [neglect_10211_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=neglect_10211_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Kwestia głosowa [neglect_10211_1] (Idle)] …관측이 끝나셨다면, 단말기는 종료하시는 걸 추천드립니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=neglect_10211_1].dlg
   limit: do 120 znaków
   EN: ... If you have completed your observation, it is recommended that you turn off the device.
   PL:
850. [Kwestia głosowa [gacksung_10211_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=gacksung_10211_1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Kwestia głosowa [gacksung_10211_1] (Uptying)] 아른거리는 불에 홀려 다가온다면, 흔적도 없이 태워버릴 뿐.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=gacksung_10211_1].dlg
   limit: do 120 znaków
   EN: Those enticed by the lapping flames will be incinerated without a trace.
   PL:
852. [Kwestia głosowa [formation_10211_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=formation_10211_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Kwestia głosowa [formation_10211_1] (Deployment)] 이번엔 어떤 실험인가요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=formation_10211_1].dlg
   limit: do 120 znaków
   EN: What kind of experiment is it, this time?
   PL:
854. [Kwestia głosowa [battleentry_10211_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battleentry_10211_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Kwestia głosowa [battleentry_10211_1] (Stage Entry)] 개체 유형 확인.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battleentry_10211_1].dlg
   limit: do 120 znaków
   EN: Subject type identified.
   PL:
856. [Kwestia głosowa [battle_select_10211_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_select_10211_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Kwestia głosowa [battle_select_10211_1] (Viewed in Battle)] 다가오지 마세요. 이 불꽃은, 어디까지라도 번질 수 있으니.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_select_10211_1].dlg
   limit: do 120 znaków
   EN: Keep your distance. This flame spreads far.
   PL:
858. [Kwestia głosowa [battle_endcommand_10211_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_endcommand_10211_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Kwestia głosowa [battle_endcommand_10211_1] (Commencing Attack)] 개체 억압, 진행하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_endcommand_10211_1].dlg
   limit: do 120 znaków
   EN: Proceeding with subject repression.
   PL:
860. [Kwestia głosowa [battle_enemy_break_10211_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_enemy_break_10211_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Kwestia głosowa [battle_enemy_break_10211_1] (Enemy Stagger)] 형태 붕괴 확인.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_enemy_break_10211_1].dlg
   limit: do 120 znaków
   EN: Structural integrity collapse confirmed.
   PL:
862. [Kwestia głosowa [battle_break_10211_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_break_10211_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Kwestia głosowa [battle_break_10211_1] (Staggered)] 흣…
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_break_10211_1].dlg
   limit: do 120 znaków
   EN: Hngh...
   PL:
864. [Kwestia głosowa [battle_kill_10211_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_kill_10211_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Kwestia głosowa [battle_kill_10211_1] (Enemy Killed)] 개체. 소각되었습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_kill_10211_1].dlg
   limit: do 120 znaków
   EN: Subject incinerated.
   PL:
866. [Kwestia głosowa [battle_dead_10211_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_dead_10211_1].desc
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
867. [Kwestia głosowa [battle_dead_10211_1] (Death)] 이 실험은… 실패하겠군요…
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_dead_10211_1].dlg
   limit: do 120 znaków
   EN: This experiment... will be a failure...
   PL:
868. [Kwestia głosowa [choice_success_p_10211_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=choice_success_p_10211_2].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Kwestia głosowa [choice_success_p_10211_2] (Check Passed)] 실험 성공. 예상대로의 결과네요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=choice_success_p_10211_2].dlg
   limit: do 120 znaków
   EN: Experiment success. As expected.
   PL:
870. [Kwestia głosowa [choice_fail_n_10211_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=choice_fail_n_10211_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Kwestia głosowa [choice_fail_n_10211_1] (Check Failed)] …변수 확인. 새로운 가설이 필요하겠군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=choice_fail_n_10211_1].dlg
   limit: do 120 znaków
   EN: ... New variable identified. The hypothesis will have to be updated.
   PL:
872. [Kwestia głosowa [battle_clear_10211_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_clear_10211_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
873. [Kwestia głosowa [battle_clear_10211_1] (Victory Cry)] 실험 종료. 선행 연구에서 진전된 부분은 없네요. 실패하진 않았지만, 성공이라 볼 수도 없을 테죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_clear_10211_1].dlg
   limit: do 160 znaków
   EN: Experiment complete. No progress from the preceding research data. Not a failure, but this can hardly be deemed a success.
   PL:
874. [Kwestia głosowa [battle_clear_ex_10211_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_clear_ex_10211_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Kwestia głosowa [battle_clear_ex_10211_1] (Extra Conditions Fulfilled)] E.G.O 동화율 정상. 개체의 행동 패턴 추출 완료. 이 정도 성과라면, 다음 연구로 이어나갈 수 있겠군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_clear_ex_10211_1].dlg
   limit: do 200 znaków
   EN: E.G.O Synchronization rate normal. Subject behavior pattern extraction complete. Progressing to the next research seems viable at this level of success.
   PL:
876. [Kwestia głosowa [battle_defeat_10211_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_defeat_10211_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [Kwestia głosowa [battle_defeat_10211_1] (Defeat Wail)] …E.G.O::홍염살의 파손률 70%. 더 이상의 실험 속행은 불가능합니다. 이 실험은… 조금 더 많은 준비가 필요하겠네요.
   źródło: PersonalityVoiceDlg/Voice_Faust_LCE_10211.json :: dataList[id=battle_defeat_10211_1].dlg
   limit: do 220 znaków
   EN: ... E.G.O:Ardor Blossom Star damage level at 70%. Experiment continuation is infeasible. ... Further preparation seems necessary before the continuation of this experiment.
   PL:

## [000] Heishou Pack - Mao Branch Adept — Faust — 흑수 - 묘 필두
- ID Tożsamości: `10212` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 76 · szybkość: 3–6 / 3–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture

878. [Karta Tożsamości — tytuł] 흑수 - 묘 필두
   źródło: Personalities.json :: dataList[id=10212].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heishou Pack -\nMao Branch Adept
   PL:
879. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10212].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
880. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10212].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [Karta Tożsamości — opis] 파우스트의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10212].desc
   limit: do 120 znaków
   EN: Faust's 12th Identity
   PL:
882. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 순보
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=1].name ; dataList[id=1021201].levelList[level=2].name ; dataList[id=1021201].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Blinkstep
   PL:
883. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 6+ [Burst], Coin Power +1
   PL:
884. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
885. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL:
886. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상의 [Burst]이 <style="highlight">4</style> 이상이면, 코인 위력 +1\n<style="highlight">[WinDuel] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has <style="highlight">4</style>+ [Burst], Coin Power +1\n<style="highlight">[WinDuel] Inflict +1 [Burst] Count</style>
   PL:
887. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]<style="highlight"></style>
   PL:
888. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1021201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count<style="highlight"></style>
   PL:
889. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬 당 1회)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] At 10+ Speed, Reuse Coin once (once per Skill)</style>
   PL:
890. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 3 이상 높으면, 코인 위력 +1</style>\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">If this unit's Speed is faster than the target's by 3 or more, Coin Power +1</style>\n[WhenUse] If target has 4+ [Burst], Coin Power +1\n[WinDuel] Inflict +1 [Burst] Count
   PL:
891. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬 당 1회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Speed, Reuse Coin once (once per Skill)<style="highlight"></style>
   PL:
892. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 길을 뚫겠습니다. 주군.
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=1].name ; dataList[id=1021202].levelList[level=2].name ; dataList[id=1021202].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Clearing the Path, My Lord.
   PL:
893. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has 4+ [Burst], Coin Power +1\n[WinDuel] Inflict +1 [Burst] Count
   PL:
894. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 885 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
895. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] 대상에게 [BurstAgility] 또는 [BurstZilu]가 있으면, 피해량 +30%
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BurstAgility], [BurstZilu]
   znaczenie tagów: [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: If target has [BurstAgility] or [BurstZilu], deal +30% damage
   PL:
896. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n<style="highlight">[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴 당 1회)</style>\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [Agility], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Agility] = 신속 / Haste; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has 4+ [Burst], Coin Power +1\n<style="highlight">[WhenUse] Gain 2 [Agility] next turn (once per turn)</style>\n[WinDuel] Inflict +1 [Burst] Count
   PL:
897. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 888 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] 대상에게 [BurstAgility] 또는 [BurstZilu]가 있으면, 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BurstAgility], [BurstZilu]
   znaczenie tagów: [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: If target has [BurstAgility] or [BurstZilu], deal +30% damage<style="highlight"></style>
   PL:
899. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 자신의 [EnhanceZilu])%만큼 피해량이 증가 (최대 50%)</style>\n<style="highlight">자신의 속도가 대상보다 3 이상 높으면, 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1</style>\n[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴 당 1회)\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [EnhanceZilu], [WhenUse], [Burst], [Agility], [WinDuel]
   znaczenie tagów: [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Agility] = 신속 / Haste; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">If this unit's Speed is faster than the target's, deal +(Speed difference x [EnhanceZilu] on self)% damage (max 50%)</style>\n<style="highlight">If this unit's Speed is faster than the target's by 3 or more, Coin Power +1\n[WhenUse] If target has 4+ [Burst], Coin Power +1</style>\n[WhenUse] Gain 2 [Agility] next turn (once per turn)\n[WinDuel] Inflict +1 [Burst] Count
   PL:
900. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Burst] 1 부여</style>
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Burst]</style>
   PL:
901. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] 대상에게 [BurstAgility] 또는 [BurstZilu]가 있으면, 피해량 <style="highlight">+50%</style>
   źródło: Skills_personality-02.json :: dataList[id=1021202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BurstAgility], [BurstZilu]
   znaczenie tagów: [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: If target has [BurstAgility] or [BurstZilu], deal <style="highlight">+50%</style> damage
   PL:
902. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 눈으로도 귀로도 쫓지 못하게.
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].name ; dataList[id=1021203].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 50 znaków
   EN: Traceless to Sight and Sound Alike.
   PL:
903. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n자신의 속도가 대상보다 2 이상 높으면, 코인 위력 +1\n[StartBattle] [SupportProtect] 1 얻음 (턴 당 1회)\n[BeforeUse] [EnhanceZilu]가 10 이상이면, '흑수 묘 오의 - 운해현현'으로 발동됨\n[WhenUse] [LegStrength] 3 얻음\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [StartBattle], [SupportProtect], [BeforeUse], [EnhanceZilu], [WhenUse], [LegStrength], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [BeforeUse] = [사용전] / [Before Use]; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\nIf this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[StartBattle] Gain 1 [SupportProtect] (once per turn)\n[BeforeUse] At 10+ [EnhanceZilu], activate "Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation" instead\n[WhenUse] Gain 3 [LegStrength]\n[WinDuel] Inflict +2 [Burst] Count
   PL:
904. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 885 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstAgility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: [OnSucceedAttack] Inflict [BurstAgility]
   PL:
906. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 884 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +30%
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: At 10+ Speed, deal +30% damage
   PL:
908. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL:
909. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬 당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Speed, Reuse Coin once (once per Skill)
   PL:
910. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n<style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 2)</style>\n[StartBattle] [SupportProtect] 1 얻음 (턴 당 1회)\n[BeforeUse] [EnhanceZilu]가 10 이상이면, '흑수 묘 오의 - 운해현현'으로 발동됨\n<style="highlight">[WhenUse] 대상의 [Burst]이 15 이상이면, 코인 위력 +1</style>\n[WhenUse] [LegStrength] 3 얻음\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [StartBattle], [SupportProtect], [BeforeUse], [EnhanceZilu], [WhenUse], [LegStrength], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [BeforeUse] = [사용전] / [Before Use]; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\n<style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)</style>\n[StartBattle] Gain 1 [SupportProtect] (once per turn)\n[BeforeUse] At 10+ [EnhanceZilu], activate "Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation" instead\n<style="highlight">[WhenUse] If target has 15+ [Burst], Coin Power +1</style>\n[WhenUse] Gain 3 [LegStrength]\n[WinDuel] Inflict +2 [Burst] Count
   PL:
911. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 888 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BurstAgility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: [OnSucceedAttack] Inflict [BurstAgility]<style="highlight"></style>
   PL:
913. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
914. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: At 10+ Speed, deal +30% damage<style="highlight"></style>
   PL:
915. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]<style="highlight"></style>
   PL:
916. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬 당 1회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 891 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
917. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] <style="highlight">[ReUseOnSucceedAttack] [BurstAgility] 부여</style>
   źródło: Skills_personality-02.json :: dataList[id=1021203].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [BurstAgility]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: <style="highlight">[ReUseOnSucceedAttack] Inflict [BurstAgility]</style>
   PL:
918. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 흑수 묘 오의 - 운해현현
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].name ; dataList[id=1021205].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 90 znaków
   EN: Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation
   PL:
919. [Umiejętność 4 (×0) (ulepszenie 3) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n자신의 속도가 대상보다 2 이상 높으면, 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15 이상이면, 코인 위력 +1\n[WhenUse] 자신의 속도가 10 이상이면 [Breath]을 20 얻고, 자신의 [Breath] 횟수가 4 미만이면, [Breath] 횟수를 최대 4 까지 얻음\n[WhenUse] [LegStrength] 3 얻음\n[WinDuel] [Burst] 횟수 2 증가\n[EndSkill] [EnhanceZilu] 10 소모
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse], [Breath], [LegStrength], [WinDuel], [EndSkill], [EnhanceZilu]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [LegStrength] = 각력【묘】 / Strider【Mao】; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\nIf this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[WhenUse] If target has 15+ [Burst], Coin Power +1\n[WhenUse] At 10+ Speed, gain 20 [Breath]; if this unit has less than 4 [Breath] Count, raise [Breath] Count up to 4\n[WhenUse] Gain 3 [LegStrength]\n[WinDuel] Inflict +2 [Burst] Count\n[EndSkill] Consume 10 [EnhanceZilu]
   PL:
920. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 885 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
921. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstZilu] 부여
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstZilu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: [OnSucceedAttack] Inflict [BurstZilu]
   PL:
922. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 905 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
923. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 884 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
924. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +30%
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 907 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
925. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 908 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬 당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 909 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
927. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 4 — opis] [ReUseOnSucceedAttack] [BurstZilu] 부여
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [BurstZilu]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: [ReUseOnSucceedAttack] Inflict [BurstZilu]
   PL:
928. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n<style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 2)</style>\n<style="highlight">[WhenUse] 대상의 [Burst] 10 당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 속도가 10 이상이면 [Breath]을 20 얻고, 자신의 [Breath] 횟수가 4 미만이면, [Breath] 횟수를 최대 4 까지 얻음\n[WhenUse] [LegStrength] 3 얻음\n[WinDuel] [Burst] 횟수 2 증가\n[EndSkill] [EnhanceZilu] 10 소모
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [WhenUse], [Breath], [LegStrength], [WinDuel], [EndSkill], [EnhanceZilu]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [LegStrength] = 각력【묘】 / Strider【Mao】; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\n<style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)</style>\n<style="highlight">[WhenUse] Coin Power +1 for every 10 [Burst] on target (max 2)</style>\n[WhenUse] At 10+ Speed, gain 20 [Breath]; if this unit has less than 4 [Breath] Count, raise [Breath] Count up to 4\n[WhenUse] Gain 3 [LegStrength]\n[WinDuel] Inflict +2 [Burst] Count\n[EndSkill] Consume 10 [EnhanceZilu]
   PL:
929. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 888 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
930. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstZilu] 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BurstZilu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: [OnSucceedAttack] Inflict [BurstZilu]<style="highlight"></style>
   PL:
931. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [BurstAgility] 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 912 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
932. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
933. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 914 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
934. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 915 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
935. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬 당 1회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 891 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
936. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 4 — opis] [ReUseOnSucceedAttack] [BurstZilu] 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [BurstZilu]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [BurstZilu] = 주살【파】 / Deathrite 【Fissure】
   EN: [ReUseOnSucceedAttack] Inflict [BurstZilu]<style="highlight"></style>
   PL:
937. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 5 — opis] <style="highlight">[ReUseOnSucceedAttack] [BurstAgility] 부여</style>
   źródło: Skills_personality-02.json :: dataList[id=1021205].levelList[level=4].coinlist[#2].coindescs[#4].desc
   (powtórzenie elementu 917 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
938. [Obrona (ulepszenia 1,4) — nazwa] 존명.
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=1].name ; dataList[id=1021204].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: It Shall Be Done.
   PL:
939. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] [SupportProtect] 1 얻음 (턴 당 1회)\n[WhenUse] 자신이 이번 전투에서 잃은 체력 누적 10% 당, 이 스킬의 공격 레벨 +1 (최대 6. 발동 시점 최대 체력 기준)\n[WhenUse] [LegStrength] 3 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [SupportProtect], [WhenUse], [LegStrength]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [DuelCounter]\n[StartBattle] Gain 1 [SupportProtect] (once per turn)\n[WhenUse] This Skill gains +1 Offense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)\n[WhenUse] Gain 3 [LegStrength]
   PL:
940. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 884 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
941. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 884 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
942. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[StartBattle] [SupportProtect] 1 얻음 (턴 당 1회)\n[WhenUse] 자신이 이번 전투에서 잃은 체력 누적 10% 당, 이 스킬의 공격 레벨 +1 (최대 6. 발동 시점 최대 체력 기준)\n[WhenUse] [LegStrength] 3 얻음\n<style="highlight">[WhenUse] 자신의 속도가 대상보다 높을수록 기본 위력 +1 (속도 차이 2당 기본 위력 +1. 최대 2)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=4].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [SupportProtect], [WhenUse], [LegStrength]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [DuelCounter]\n[StartBattle] Gain 1 [SupportProtect] (once per turn)\n[WhenUse] This Skill gains +1 Offense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)\n[WhenUse] Gain 3 [LegStrength]\n<style="highlight">[WhenUse] If this unit's Speed is faster than the target's by 2 or more, gain Base Power based on Speed difference (Base Power +1 for every 2 Speed difference; max 2)</style>
   PL:
943. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
944. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021204].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 887 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [Obrona (ulepszenia 1,4) — nazwa] 초속호위
   źródło: Skills_personality-02.json :: dataList[id=1021206].levelList[level=1].name ; dataList[id=1021206].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Swiftfeet Protection
   PL:
946. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n[BeforeUse] [EnhanceZilu]가 10 이상이면, '흑수 묘 오의 - 운해현현'으로 발동됨\n[WhenUse] 자신이 이번 전투에서 잃은 체력 누적 10% 당, 이 스킬의 방어 레벨 +1 (최대 6. 발동 시점 최대 체력 기준)\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WhenUse] [Protection] 2 얻음 (턴 당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021206].levelList[level=1].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [SupportProtect], [BeforeUse], [EnhanceZilu], [WhenUse], [Protection]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [BeforeUse] = [사용전] / [Before Use]; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade; [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection
   EN: [CanDuelGuard]\nExclusive Skill for [SupportProtect]\n[BeforeUse] At 10+ [EnhanceZilu], activates "Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation" instead\n[WhenUse] This Skill gains +1 Defense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)\n[WhenUse] Cannot be Staggered by damage until this Skill ends\n[WhenUse] Gain 2 [Protection] (once per turn)
   PL:
947. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-02.json :: dataList[id=1021206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 799 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
948. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n[BeforeUse] [EnhanceZilu]가 10 이상이면, '흑수 묘 오의 - 운해현현'으로 발동됨\n[WhenUse] 자신이 이번 전투에서 잃은 체력 누적 10% 당, 이 스킬의 방어 레벨 +1 (최대 6. 발동 시점 최대 체력 기준)\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WhenUse] [Protection] 2 얻음 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021206].levelList[level=4].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [SupportProtect], [BeforeUse], [EnhanceZilu], [WhenUse], [Protection]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [BeforeUse] = [사용전] / [Before Use]; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade; [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection
   EN: [CanDuelGuard]\nExclusive Skill for [SupportProtect]\n[BeforeUse] At 10+ [EnhanceZilu], activates "Ascendant Heishou - Mao Technique: Cloudsplitting Manifestation" instead\n[WhenUse] This Skill gains +1 Defense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)\n[WhenUse] Cannot be Staggered by damage until this Skill ends\n[WhenUse] Gain 2 [Protection] (once per turn)<style="highlight"></style>
   PL:
949. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021206].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL:
950. [Pasywka bojowa (od ulepszenia 1) — nazwa] 천구성
   źródło: Passives.json :: dataList[id=1021203].name
   limit: do 40 znaków
   EN: Tianjiu Star
   PL:
951. [Pasywka bojowa (od ulepszenia 1) — opis] [BurstZilu]의 수치가 0이 되어 소멸시, [BurstVulnerableZilu]이 부여됨
   źródło: Passives.json :: dataList[id=1021203].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BurstZilu], [BurstVulnerableZilu]
   znaczenie tagów: [BurstZilu] = 주살【파】 / Deathrite 【Fissure】; [BurstVulnerableZilu] = 붕괴 표식 / Mark of Decay
   EN: When [BurstZilu] Stack drops to 0 and expires, gain [BurstVulnerableZilu]
   PL:
952. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — nazwa] 흑수화[묘] / 묘 필두
   źródło: Passives.json :: dataList[id=1021201].name
   limit: do 60 znaków
   EN: Heishou Mutation [Mao] / Mao Branch Adept
   PL:
953. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — opis] 자신의 속도가 대상보다 빠르면, 속도 차이 1 당 가하는 피해량 +2% (최대 10%)\n\n전투 중 아군이 주살 효과를 발동시킬 때마다, [EnhanceZilu] 1 얻음 (턴 당 최대 5회)\n- 자신이 발동시켰으면, [EnhanceZilu] 추가로 1 얻음\n[SupportProtect] 효과 발동시, [EnhanceZilu] 5 얻음
   źródło: Passives.json :: dataList[id=1021201].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [EnhanceZilu], [SupportProtect]
   znaczenie tagów: [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade; [SupportProtect] = 원호 방어 / Assist Defense
   EN: If this unit's Speed is faster than the target's, deal +2% more damage for every 1 Speed difference (max 10%)\n\nGain 1 [EnhanceZilu] every time an ally triggers a Deathrite effect (5 times per turn)\n- If this unit triggered a Deathrite effect, gain 1 additional [EnhanceZilu]\nWhen activating the [SupportProtect] effect, gain 5 [EnhanceZilu]
   PL:
954. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — podsumowanie] 속도 차이 비례 피해량 증가[TabExplain]\n주살 또는 [SupportProtect] 효과 발동시, [EnhanceZilu] 얻음
   źródło: Passives.json :: dataList[id=1021201].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain], [SupportProtect], [EnhanceZilu]
   znaczenie tagów: [SupportProtect] = 원호 방어 / Assist Defense; [EnhanceZilu] = 천구성도 / Tianjiu Star's Blade
   EN: Deal more damage based on Speed difference\nWhen activating Deathrite or [SupportProtect] effects, gain [EnhanceZilu]
   PL:
955. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — nazwa] 쾌도
   źródło: Passives.json :: dataList[id=1021221].name
   limit: do 40 znaków
   EN: Blinkblade
   PL:
956. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — opis] 속도가 가장 빠른 아군이 [Burst] 피해를 입히면, 다음 턴에 [AttackUp] 1 얻음 (턴 당 최대 3회)
   źródło: Passives.json :: dataList[id=1021221].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Burst], [AttackUp]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: When 1 ally with the fastest Speed inflicts [Burst] damage, gain 1 [AttackUp] next turn (3 times per turn)
   PL:
957. [Kwestia głosowa [get_10212_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=get_10212_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
958. [Kwestia głosowa [get_10212_1] (Identity Acquisition)] 그 대답으로 충분합니다, 주군.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=get_10212_1].dlg
   limit: do 120 znaków
   EN: That answer will suffice, my lord.
   PL:
959. [Kwestia głosowa [lobby_morning_10212_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=lobby_morning_10212_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
960. [Kwestia głosowa [lobby_morning_10212_1] (Morning Greeting)] 간밤에 맡기신 일에 대한 결과는 이쪽입니다. 전부 뜻대로 이루어졌죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=lobby_morning_10212_1].dlg
   limit: do 120 znaków
   EN: The outcome of the night's assignment can be reviewed here. All has been done as willed.
   PL:
961. [Kwestia głosowa [lobby_noon_10212_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=lobby_noon_10212_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
962. [Kwestia głosowa [lobby_noon_10212_1] (Afternoon Greeting)] 당장 주군의 모든 가르침을 전부 이해할 수는 없으나, 해가 떠있는 동안 제 것으로 만들어 보이겠습니다. 파우스트는 그것에 능합니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=lobby_noon_10212_1].dlg
   limit: do 210 znaków
   EN: Though there is no immediate path toward learning all of my lord's teachings, I will attempt to acquire them in full while the sun shines. It is Faust's expertise.
   PL:
963. [Kwestia głosowa [lobby_night_10212_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=lobby_night_10212_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
964. [Kwestia głosowa [lobby_night_10212_1] (Evening Greeting)] 야밤의 달빛과 함께 사라지는 것이 저의 필요 이유. 그러나 부름이 필요하시다면, 달이 구름에 숨은 틈을 타 주군께 서겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=lobby_night_10212_1].dlg
   limit: do 200 znaków
   EN: My purpose is to fade with the night's glint of the moon. Yet, should I be summoned, I shall stand by my lord as the moon shelters behind the clouds.
   PL:
965. [Kwestia głosowa [smalltalk_10212_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=smalltalk_10212_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
966. [Kwestia głosowa [smalltalk_10212_1] (Chatter #1)] 배우고 묻는 일에 무슨 쓸모가 있을까. 그런 고민을 했던 시기도 있었죠. 주군이 아니었다면… 저는 아직도 파우스트가 아닌, 한낱 범인으로 살아갔을 테니까요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=smalltalk_10212_1].dlg
   limit: do 220 znaków
   EN: What use is there to learning, to questioning...? A conundrum that had once harrowed my mind. Were it not for my lord... I would have been a mere ordinary human, not Faust.
   PL:
967. [Kwestia głosowa [smalltalk_10212_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=smalltalk_10212_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
968. [Kwestia głosowa [smalltalk_10212_2] (Chatter #2)] 흑수는 한낱 도구에 불과할 수도 있지만, 파우스트는 그렇지 않아요. 흑수 - 묘로서의 저도, 소지로서도… 이름을 돌려받은 저는 주군의 충실한 검이자 노력하는 제자입니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=smalltalk_10212_2].dlg
   limit: do 240 znaków
   EN: A Heishou may be but a tool... but Faust is different. As a beast of the Heishou - Mao Branch... as a Pinky... I am, with my name restored, a loyal blade and a devoted disciple of my lord.
   PL:
969. [Kwestia głosowa [smalltalk_10212_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=smalltalk_10212_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
970. [Kwestia głosowa [smalltalk_10212_3] (Chatter #3)] 게젤샤프트에 접속하는 것은… 필요한 일이지만, 꺼려집니다. 그들은 자꾸 무언가를 알려주려 하지만, 막상 저는 주군의 가르침을 소화하는데도 시일이 걸리니.\n그러나 배움을 위해서라면, 다소의 꺼려짐도 감수해야 하는 일이겠죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=smalltalk_10212_3].dlg
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Accessing the Gesellschaft is... necessary, but I do so with reluctance. They attempt again and again to instruct and enlighten me, but gaining an understanding of my lord's teachings already consumes a majority of my days.\n... Yet, one must face their disinclinations for the pursuit of learning.
   PL:
971. [Kwestia głosowa [smalltalk_10212_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=smalltalk_10212_4].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
972. [Kwestia głosowa [smalltalk_10212_4] (Post-Uptie Chat 1)] 운해현현(雲解顯現). 재갈의 끈을 주군께 부여 받았으니, 묘는 즉각 나를 따라라.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=smalltalk_10212_4].dlg
   limit: do 150 znaków
   EN: Cloudsplitting Manifestation(雲解顯現). Beasts of the Mao must follow in my wake, for my lord has bestowed me the leash.
   PL:
973. [Kwestia głosowa [smalltalk_10212_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=smalltalk_10212_5].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
974. [Kwestia głosowa [smalltalk_10212_5] (Post-Uptie Chat 2)] 의로운 자는 무력을 앞세우지 않는다고, 주군께선 누누이 말씀하셨습니다.\n하지만… 말보다 검이 앞서는 이런 저라도 의를 향해 나아간다면, 그것 또한 도(道)가 아닐지.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=smalltalk_10212_5].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: My lord has impressed upon us many times that the righteous do not make weapons of their might.\nYet... even I, a brute whose blade swings before her lips speak, persevere toward righteousness... perhaps that is a road, a way(道) for one to walk down.
   PL:
975. [Kwestia głosowa [neglect_10212_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=neglect_10212_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
976. [Kwestia głosowa [neglect_10212_1] (Idle)] 원망하지도, 탐을 내지도 않으니 저 또한 훌륭한 사람 중 하나일 테죠. 주군… 웃지 마십시오.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=neglect_10212_1].dlg
   limit: do 150 znaków
   EN: I must be one of the great humans as well, as I have no resentment or covetousness in me. ... My lord, do not laugh.
   PL:
977. [Kwestia głosowa [gacksung_10212_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=gacksung_10212_1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
978. [Kwestia głosowa [gacksung_10212_1] (Uptying)] 어떤 뜻을 이루시려는지 이해했습니다. 다음은 속히 그 의를 행할 뿐입니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=gacksung_10212_1].dlg
   limit: do 120 znaków
   EN: Your will is understood; that vision of righteousness shall swiftly be realized.
   PL:
979. [Kwestia głosowa [formation_10212_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=formation_10212_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
980. [Kwestia głosowa [formation_10212_1] (Deployment)] 의로움을 세우기 위해서라면.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=formation_10212_1].dlg
   limit: do 120 znaków
   EN: To restore the righteousness that was lost.
   PL:
981. [Kwestia głosowa [battleentry_10212_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battleentry_10212_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
982. [Kwestia głosowa [battleentry_10212_1] (Stage Entry)] 필두, 출진.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battleentry_10212_1].dlg
   limit: do 120 znaków
   EN: Adept Heishou, into the fray.
   PL:
983. [Kwestia głosowa [battle_select_10212_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_select_10212_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
984. [Kwestia głosowa [battle_select_10212_1] (Viewed in Battle)] 개의치 않고 말씀을.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_select_10212_1].dlg
   limit: do 120 znaków
   EN: Command without hesitation.
   PL:
985. [Kwestia głosowa [battle_endcommand_10212_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_endcommand_10212_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
986. [Kwestia głosowa [battle_endcommand_10212_1] (Commencing Attack)] 불가위야(不可違也). 막아내지 못하리.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_endcommand_10212_1].dlg
   limit: do 120 znaków
   EN: Futility inheres in impossibility(不可違也). I will not be restrained.
   PL:
987. [Kwestia głosowa [battle_enemy_break_10212_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_enemy_break_10212_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
988. [Kwestia głosowa [battle_enemy_break_10212_1] (Enemy Stagger)] 무용하군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_enemy_break_10212_1].dlg
   limit: do 120 znaków
   EN: Futile.
   PL:
989. [Kwestia głosowa [battle_break_10212_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_break_10212_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
990. [Kwestia głosowa [battle_break_10212_1] (Staggered)] …과연.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_break_10212_1].dlg
   limit: do 120 znaków
   EN: ... Indeed.
   PL:
991. [Kwestia głosowa [battle_kill_10212_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_kill_10212_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
992. [Kwestia głosowa [battle_kill_10212_1] (Enemy Killed)] 이제 깨우치시길.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_kill_10212_1].dlg
   limit: do 120 znaków
   EN: Find your enlightenment, now.
   PL:
993. [Kwestia głosowa [battle_dead_10212_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_dead_10212_1].desc
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
994. [Kwestia głosowa [battle_dead_10212_1] (Death)] …삿갓을 바로 해주시죠. 네. 그걸로… 충분…
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_dead_10212_1].dlg
   limit: do 120 znaków
   EN: ... Please straighten my bamboo hat. Yes. That is... enough...
   PL:
995. [Kwestia głosowa [choice_success_p_10212_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=choice_success_p_10212_2].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
996. [Kwestia głosowa [choice_success_p_10212_2] (Check Passed)] 때로는 검이 문제를 해결해주기도 합니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=choice_success_p_10212_2].dlg
   limit: do 120 znaków
   EN: There are times when a blade has the makings of a solution.
   PL:
997. [Kwestia głosowa [choice_fail_n_10212_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=choice_fail_n_10212_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
998. [Kwestia głosowa [choice_fail_n_10212_1] (Check Failed)] 형세를 파악하지 못했군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=choice_fail_n_10212_1].dlg
   limit: do 120 znaków
   EN: Failed to read the situation at hand.
   PL:
999. [Kwestia głosowa [battle_clear_10212_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_clear_10212_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1000. [Kwestia głosowa [battle_clear_10212_1] (Victory Cry)] 언제나 티끌 하나 없는 끝은 없을테죠. 그러나 그에 가까워지려 노력한다면, 또한 문제도 없을 것입니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_clear_10212_1].dlg
   limit: do 170 znaków
   EN: Perpetual flawlessness is an impossibility. Yet, perseverance in that infinite approach to perfection makes this a non-issue.
   PL:
1001. [Kwestia głosowa [battle_clear_ex_10212_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_clear_ex_10212_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1002. [Kwestia głosowa [battle_clear_ex_10212_1] (Extra Conditions Fulfilled)] 오늘, 부끄럽지 않았습니다. 의를 바로 세우는데 일조하였으니, 내일은 더 떳떳히 살아갈 수 있겠군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_clear_ex_10212_1].dlg
   limit: do 170 znaków
   EN: Today was a day of no shame, for I have made my contributions to bringing about righteousness. I shall face tomorrow with pride.
   PL:
1003. [Kwestia głosowa [battle_defeat_10212_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_defeat_10212_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1004. [Kwestia głosowa [battle_defeat_10212_1] (Defeat Wail)] …이래서는, 범인이었던 지난날과 다를 바가 무엇인지. …떠오르는 해가 부끄럽군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_Blackwater_10212.json :: dataList[id=battle_defeat_10212_1].dlg
   limit: do 170 znaków
   EN: ... The rising sun brings me shame. ... My display of incompetence today was no different from my years as an ordinary human.
   PL:

## [000] Shi Assoc. East Section 3 — Faust — 동부 시 협회 3과
- ID Tożsamości: `10213` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 60 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Poise

1005. [Karta Tożsamości — tytuł] 동부 시 협회\n3과
   źródło: Personalities.json :: dataList[id=10213].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Shi Assoc.\nEast Section 3
   PL:
1006. [Karta Tożsamości — nazwa] 파우스트
   źródło: Personalities.json :: dataList[id=10213].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1007. [Karta Tożsamości — nazwa z tytułem] 파우스트
   źródło: Personalities.json :: dataList[id=10213].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1008. [Karta Tożsamości — opis] 파우스트의 열세번째 인격
   źródło: Personalities.json :: dataList[id=10213].desc
   limit: do 120 znaków
   EN: Faust's 13th Identity
   PL:
1009. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 베어내기
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=1].name ; dataList[id=1021301].levelList[level=2].name ; dataList[id=1021301].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Cleave
   PL:
1010. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] [Breath] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 1 [Breath]
   PL:
1011. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1021301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1021301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
1012. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1021301].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1011 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1013. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합이 4 이상이면, 코인 위력 +1</style>\n[WhenUse] [Breath] <style="highlight">2</style> 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[WhenUse] At 4+ ([Breath] on self + [Laceration] on target), Coin Power +1</style>\n[WhenUse] Gain <style="highlight">2</style> [Breath]
   PL:
1014. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합이 4 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] At 4+ ([Breath] on self + [Laceration] on target), Coin Power +1\n[WhenUse] Gain 2 [Breath] <style="highlight"></style>
   PL:
1015. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-02.json :: dataList[id=1021301].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Laceration]
   PL:
1016. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 거리 확보
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=1].name ; dataList[id=1021302].levelList[level=2].name ; dataList[id=1021302].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Positioning Maneuver
   PL:
1017. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 4당 피해량 +11% (최대 44%)\n[WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Deal +11% damage for every 4 [Breath] on self (max 44%)\n[WhenUse] Gain +1 [Breath] Count
   PL:
1018. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1021302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
1019. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL:
1020. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 1 — opis] [CriticalOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1021302].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict 2 [Laceration]
   PL:
1021. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 4당, 합 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Breath] 4당 피해량 +11% (최대 44%)\n[WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[WhenUse] Clash Power +1 for every 4 ([Breath] on self + [Laceration] on target) (max 2)</style>\n[WhenUse] Deal +11% damage for every 4 [Breath] on self (max 44%)\n[WhenUse] Gain +1 [Breath] Count
   PL:
1022. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] <style="highlight">2</style> 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain <style="highlight">2</style> [Breath]
   PL:
1023. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 4당, 합 위력 +1 (최대 <style="highlight">4</style>)\n[WhenUse] 자신의 [Breath] 4당 피해량 +11% (최대 44%)\n<style="highlight">[WhenUse] 소모한 [ArrowShiFau] 1당 피해량 +11% (최대 44%)</style>\n[WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=4].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Laceration], [ArrowShiFau]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [ArrowShiFau] = 화살 - 시 / Arrow - Shi
   EN: [WhenUse] Clash Power +1 for every 4 ([Breath] on self + [Laceration] on target) (max <style="highlight">4</style>)\n[WhenUse] Deal +11% damage for every 4 [Breath] on self (max 44%)\n<style="highlight">[WhenUse] Deal +11% damage for every [ArrowShiFau] spent (max 44%)</style>\n[WhenUse] Gain +1 [Breath] Count
   PL:
1024. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Laceration] Count
   PL:
1025. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]<style="highlight"></style>
   PL:
1026. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack]</style> [Laceration] 2 부여
   źródło: Skills_personality-02.json :: dataList[id=1021302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack]</style> Inflict 2 [Laceration]
   PL:
1027. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 궁섬[弓閃]
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].name ; dataList[id=1021303].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Glimmering Bow [弓閃]
   PL:
1028. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 4당 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Breath] 4당 피해량 +11% (최대 44%)\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Coin Power +1 for every 4 ([Breath] on self + [Laceration] on target) (max 2)\n[WhenUse] Deal +11% damage for every 4 [Breath] on self (max 44%)\n[WhenUse] Gain +2 [Breath] Count
   PL:
1029. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1019 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1030. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1021303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain +1 [Breath] Count
   PL:
1031. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1018 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1032. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1021303].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
1033. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1021303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL:
1034. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [CriticalOnSucceedAttack] 다음 턴에 [DefenseDown] 1 부여 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [DefenseDown]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [CriticalOnSucceedAttack] Inflict 1 [DefenseDown] next turn (once per turn)
   PL:
1035. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 4당 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Breath] 4당 피해량 +11% (최대 44%)\n<style="highlight">[WhenUse] 소모한 [ArrowShiFau] 1당 피해량 +11% (최대 44%)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=4].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Laceration], [ArrowShiFau]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [ArrowShiFau] = 화살 - 시 / Arrow - Shi
   EN: [WhenUse] Coin Power +1 for every 4 ([Breath] on self + [Laceration] on target) (max 2)\n[WhenUse] Deal +11% damage for every 4 [Breath] on self (max 44%)\n<style="highlight">[WhenUse] Deal +11% damage for every [ArrowShiFau] spent (max 44%)</style>\n[WhenUse] Gain +2 [Breath] Count
   PL:
1036. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] <style="highlight">2</style> 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1022 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1037. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1024 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1038. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [CriticalOnSucceedAttack] 다음 턴에 [DefenseDown] <style="highlight">2</style> 부여 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021303].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [DefenseDown]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [CriticalOnSucceedAttack] Inflict <style="highlight">2</style> [DefenseDown] next turn (once per turn)
   PL:
1039. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 섬궁[閃弓]
   źródło: Skills_personality-02.json :: dataList[id=1021305].levelList[level=3].name ; dataList[id=1021305].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Bow's Glimmer [閃弓]
   PL:
1040. [Umiejętność 4 (×0) (ulepszenie 3) — opis] [CantDuel]\n이 스킬은 외부 효과로 재사용이 불가능함\n[AimForTheGoal] 1당 피해량 +24% (최대 72%)\n[AimForTheGoal] 1당 크리티컬 피해량 +24% (최대 72%)\n- [AimForTheGoal]이 4면, 위 두 효과 대신 크리티컬 피해량 +444%\n[WhenUse] 자신의 [Breath]이 4 이상이면, 기본 위력 +2\n[WhenUse] [AimForTheGoal] 1당 코인 위력 +2 (최대 4)\n[WhenUse] [AimForTheGoal] 1당 [Breath] 5 얻음\n[EndSkill] ([AimForTheGoal] x 5)만큼 [Breath] 감소\n[EndSkill] [SnipingArrowMode] 제거, [AimForTheGoal] 제거
   źródło: Skills_personality-02.json :: dataList[id=1021305].levelList[level=3].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [AimForTheGoal], [WhenUse], [Breath], [EndSkill], [SnipingArrowMode]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [AimForTheGoal] = 목표 조준 / Target Aim; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [SnipingArrowMode] = 저격 자세 / Ready to Loose
   EN: [CantDuel]\nExternal effects cannot trigger this Skill to be Reused\nDeal +24% damage for every [AimForTheGoal] (max 72%)\nDeal +24% damage on Critical Hit for every [AimForTheGoal] (max 72%)\n- At 4 [AimForTheGoal], instead of the two above effects, deal +444% damage on Critical Hit\n[WhenUse] At 4+ [Breath], Base Power +2\n[WhenUse] Coin Power +2 for every [AimForTheGoal] (max 4)\n[WhenUse] Gain 5 [Breath] for every [AimForTheGoal]\n[EndSkill] Lose ([AimForTheGoal] x 5) [Breath]\n[EndSkill] Remove [SnipingArrowMode] and [AimForTheGoal] from self
   PL:
1041. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [ArrowInTheEyeFau] 1 부여, 부여 성공 시 [ArrowShiFau] 1 감소
   źródło: Skills_personality-02.json :: dataList[id=1021305].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1021305].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ArrowInTheEyeFau], [ArrowShiFau]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ArrowInTheEyeFau] = 박힌 화살 / Lodged Arrow; [ArrowShiFau] = 화살 - 시 / Arrow - Shi
   EN: [OnSucceedAttack] Inflict 1 [ArrowInTheEyeFau]; once inflicted, lose 1 [ArrowShiFau]
   PL:
1042. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [EnemyKill] 다음 턴에 [AStrokeOfDeath] 1 얻음
   źródło: Skills_personality-02.json :: dataList[id=1021305].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1021305].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [AStrokeOfDeath]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [AStrokeOfDeath] = 절명 / Liferender
   EN: [EnemyKill] Gain 1 [AStrokeOfDeath] next turn
   PL:
1043. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [CantDuel]\n이 스킬은 외부 효과로 재사용이 불가능함\n[AimForTheGoal] 1당 피해량 +<style="highlight">48</style>% (최대 <style="highlight">144</style>%)\n[AimForTheGoal] 1당 크리티컬 피해량 +<style="highlight">48</style>% (최대 <style="highlight">144</style>%)\n- [AimForTheGoal]이 4면, 위 두 효과 대신 크리티컬 피해량 +444%\n[WhenUse] 자신의 [Breath] 4<style="highlight">당 기본 위력 +2 (최대 10)</style>\n[WhenUse] [AimForTheGoal] 1당 코인 위력 +<style="highlight">4</style> (최대 <style="highlight">10</style>)\n[WhenUse] [AimForTheGoal] 1당 [Breath] 5 얻음\n[EndSkill] (<style="highlight">([AimForTheGoal] - 1)</style> x 5)만큼 [Breath] 감소\n[EndSkill] [SnipingArrowMode] 제거, [AimForTheGoal] 제거
   źródło: Skills_personality-02.json :: dataList[id=1021305].levelList[level=4].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [AimForTheGoal], [WhenUse], [Breath], [EndSkill], [SnipingArrowMode]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [AimForTheGoal] = 목표 조준 / Target Aim; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [SnipingArrowMode] = 저격 자세 / Ready to Loose
   EN: [CantDuel]\nExternal effects cannot trigger this Skill to be Reused\nDeal +<style="highlight">48</style>% damage for every [AimForTheGoal] (max <style="highlight">144</style>%)\nDeal +<style="highlight">48</style>% damage on Critical Hit for every [AimForTheGoal] (max <style="highlight">144</style>%)\n- At 4 [AimForTheGoal], instead of the two above effects, deal +444% damage on Critical Hit\n[WhenUse] <style="highlight">Base Power +2 for every 4 [Breath] on self (max 10)</style>\n[WhenUse] Coin Power +<style="highlight">4</style> for every [AimForTheGoal] (max <style="highlight">10</style>)\n[WhenUse] Gain 5 [Breath] for every [AimForTheGoal]\n[EndSkill] Lose (<style="highlight">([AimForTheGoal] - 1)</style> x 5) [Breath]\n[EndSkill] Remove [SnipingArrowMode] and [AimForTheGoal] from self
   PL:
1044. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] <style="highlight">[CriticalEnemyTargetKill] 자신의 [Breath] 횟수 4 증가</style>
   źródło: Skills_personality-02.json :: dataList[id=1021305].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalEnemyTargetKill], [Breath]
   znaczenie tagów: [CriticalEnemyTargetKill] = [크리티컬 적 처치 시] / [On Crit Kill Against Enemy]; [Breath] = 호흡 / Poise
   EN: <style="highlight">[CriticalEnemyTargetKill] Gain +4 [Breath] Count</style>
   PL:
1045. [Obrona (ulepszenia 1,3,4) — nazwa] 궁도[弓刀] 전개
   źródło: Skills_personality-02.json :: dataList[id=1021304].levelList[level=1].name ; dataList[id=1021304].levelList[level=3].name ; dataList[id=1021304].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 14 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Unfold Bowblade [弓刀]
   PL:
1046. [Obrona (ulepszenie 3) — opis] <style="highlight">자신에게 [ArrowShiFau]가 없으면 ‘회피’로 발동됨\n\n[StartBattle] ‘섬궁’ 사용 예정이면 ‘회피’로 변경됨\n[StartBattle] 자신에게 [SnipingArrowMode]가 있으면, 해당 턴 동안 (36 / [AimForTheGoal] 수치)만큼 보호막을 얻음 (턴당 1회)\n\n[EndBattle] 자신에게 [SnipingArrowMode]가 있고, 이번 턴에 공격 스킬을 사용하지 않았으면, 다음 턴에 [AimForTheGoal] 1 얻음 (턴당 1회)\n[EndBattle] 자신에게 [SnipingArrowMode]가 없고, [ArrowShiFau]가 1 이상이면, 다음 턴에 [SnipingArrowMode], [AimForTheGoal] 1 얻음 (턴당 1회)</style>
   źródło: Skills_personality-02.json :: dataList[id=1021304].levelList[level=3].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ArrowShiFau], [StartBattle], [SnipingArrowMode], [AimForTheGoal], [EndBattle]
   znaczenie tagów: [ArrowShiFau] = 화살 - 시 / Arrow - Shi; [StartBattle] = [전투 시작시] / [Combat Start]; [SnipingArrowMode] = 저격 자세 / Ready to Loose; [AimForTheGoal] = 목표 조준 / Target Aim; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: <style="highlight">If this unit does not have [ArrowShiFau], activate "Evade" instead\n\n[StartBattle] If this unit is about to use "Bow's Glimmer", use "Evade" instead\n[StartBattle] If this unit has [SnipingArrowMode], gain (36 / [AimForTheGoal] Stack) Shield for the turn (once per turn)\n\n[EndBattle] If this unit has [SnipingArrowMode], and did not use an Attack Skill this turn, gain 1 [AimForTheGoal] next turn (once per turn)\n[EndBattle] If this unit does not have [SnipingArrowMode], and has 1+ [ArrowShiFau], gain 1 of each [SnipingArrowMode] and [AimForTheGoal] next turn (once per turn)</style>
   PL:
1047. [Obrona (ulepszenie 4) — opis] 자신에게 [ArrowShiFau]가 없으면 ‘회피’로 발동됨\n\n[StartBattle] ‘섬궁’ 사용 예정이면 ‘회피’로 변경됨\n[StartBattle] 자신에게 [SnipingArrowMode]가 있으면, 해당 턴 동안 (<style="highlight">60</style> / [AimForTheGoal] 수치)만큼 보호막을 얻음 (턴당 1회)\n\n[EndBattle] 자신에게 [SnipingArrowMode]가 있고, 이번 턴에 공격 스킬을 사용하지 않았으면, 다음 턴에 [AimForTheGoal] 1 얻음 (턴당 1회)\n[EndBattle] 자신에게 [SnipingArrowMode]가 없고, [ArrowShiFau]가 1 이상이면, 다음 턴에 [SnipingArrowMode], [AimForTheGoal] 1 얻음 (턴당 1회)
   źródło: Skills_personality-02.json :: dataList[id=1021304].levelList[level=4].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ArrowShiFau], [StartBattle], [SnipingArrowMode], [AimForTheGoal], [EndBattle]
   znaczenie tagów: [ArrowShiFau] = 화살 - 시 / Arrow - Shi; [StartBattle] = [전투 시작시] / [Combat Start]; [SnipingArrowMode] = 저격 자세 / Ready to Loose; [AimForTheGoal] = 목표 조준 / Target Aim; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: If this unit does not have [ArrowShiFau], activate "Evade" instead\n\n[StartBattle] If this unit is about to use "Bow's Glimmer", use "Evade" instead\n[StartBattle] If this unit has [SnipingArrowMode], gain (<style="highlight">60</style> / [AimForTheGoal] Stack) Shield for the turn (once per turn)\n\n[EndBattle] If this unit has [SnipingArrowMode], and did not use an Attack Skill this turn, gain 1 [AimForTheGoal] next turn (once per turn)\n[EndBattle] If this unit does not have [SnipingArrowMode], and has 1+ [ArrowShiFau], gain 1 of each [SnipingArrowMode] and [AimForTheGoal] next turn (once per turn)
   PL:
1048. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills_personality-02.json :: dataList[id=1021306].levelList[level=1].name ; dataList[id=1021306].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1049. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] 자신의 [Breath] 횟수 1 증가 (턴당 2회)
   źródło: Skills_personality-02.json :: dataList[id=1021306].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Breath]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [OnSucceedEvade] Gain +1 [Breath] Count (2 times per turn)
   PL:
1050. [Obrona (ulepszenie 4) — opis] [OnSucceedEvade] 자신의 [Breath] 횟수 1 증가 (턴당 3회)
   źródło: Skills_personality-02.json :: dataList[id=1021306].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Breath]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [OnSucceedEvade] Gain +1 [Breath] Count (3 times per turn)
   PL:
1051. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust) — nazwa] 시노유미
   źródło: Passives.json :: dataList[id=1021301].name
   limit: do 40 znaków
   EN: Shi-no-Yumi
   PL:
1052. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust) — opis] 자신의 [ArrowShiFau]가 4면, 기본 공격 스킬 효과로 [Breath] 위력을 얻을 때, [Breath] 횟수 1 증가 (전투당 2회, [ArrowShiFau]가 3이 될 때 발동 횟수 초기화)\n[AimForTheGoal]이 2 이상일 때 ‘섬궁’을 사용했으면, 다음 턴에 [SlashDamageUp] 1 얻음
   źródło: Passives.json :: dataList[id=1021301].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [ArrowShiFau], [Breath], [AimForTheGoal], [SlashDamageUp]
   znaczenie tagów: [ArrowShiFau] = 화살 - 시 / Arrow - Shi; [Breath] = 호흡 / Poise; [AimForTheGoal] = 목표 조준 / Target Aim; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: At 4 [ArrowShiFau] Stack: When this unit gains [Breath] Potency from Base Attack Skill effects, gain +1 [Breath] Count (2 times per Encounter; per-Encounter cap resets when [ArrowShiFau] drops to 3)\nIf this unit used "Bow's Glimmer" Skill at 2+ [AimForTheGoal], gain 1 [SlashDamageUp] next turn
   PL:
1053. [Pasywka bojowa (od ulepszenia 3) — nazwa] 저격 - 활
   źródło: Passives.json :: dataList[id=1021302].name
   limit: do 40 znaków
   EN: Snipe - Archery
   PL:
1054. [Pasywka bojowa (od ulepszenia 3) — opis] 자신이 [SnipingArrowMode] 상태면, 가장 왼쪽에 장착한 기본 공격 스킬을 ‘섬궁’으로 변경하여 전투 시작 시 사용함.\n- 이 효과 발동시 자신의 [AimForTheGoal]이 최대 수치이고, 조작 패널과 예비 스킬 슬롯에 스킬 3이 없으면, \n가장 왼쪽 슬롯에 장착한 수비 스킬을 스킬 3으로 취급하여 ‘섬궁’으로 변경함\n\n사용하는 기본 공격 스킬에 따라 아래 효과 적용 (죄악 속성은 사용한 스킬 속성을 따름)\n- 스킬 1: 기본 위력 +1, 피해량 +11%\n- 스킬 2: 기본 위력 +1, 코인 위력 +1, 피해량 +22%\n- 스킬 3: 기본 위력 +4, 코인 위력 +4, 피해량 +44%\n\n※ E.G.O 스킬 장착하여 전투를 시작한 경우, [SnipingArrowMode]가 해제되고 ‘섬궁’이 사용되지 않음.
   źródło: Passives.json :: dataList[id=1021302].desc
   limit: do 1040 znaków
   tokeny: zachowaj dokładnie: \n, [SnipingArrowMode], [AimForTheGoal]
   znaczenie tagów: [SnipingArrowMode] = 저격 자세 / Ready to Loose; [AimForTheGoal] = 목표 조준 / Target Aim
   EN: If this unit is in [SnipingArrowMode] state, replace the leftmost Base Attack Skill equipped on the Dashboard with "Bow's Glimmer", then use it at Combat Start\n- If, at max [AimForTheGoal] Stack, this unit's Skill 3 is on neither the Dashboard nor the upcoming list of Skills when this effect activates, the Defense Skill equipped on the leftmost Skill Slot counts as a Skill 3, and will be used to activate "Bow's Glimmer"\n\nGain the following effects based on which Base Attack Skill was replaced (Sin Affinity carries over from the replaced Skill)\n- Skill 1: Base Power +1, deal +11% damage\n- Skill 2: Base Power +1, Coin Power +1, deal +22% damage\n- Skill 3: Base Power +4, Coin Power +4, deal +44% damage\n\n※ If an E.G.O Skill was equipped at Combat Start, remove [SnipingArrowMode] and this unit does not use "Bow's Glimmer"
   PL:
1055. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust) — nazwa] 시노유미
   źródło: Passives.json :: dataList[id=1021311].name
   (powtórzenie elementu 1051 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1056. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust) — opis] 자신의 [ArrowShiFau]가 4면, 기본 공격 스킬 효과로 [Breath] 위력을 얻을 때, [Breath] 횟수 1 증가 (전투당 <style="highlight">3</style>회, [ArrowShiFau]가 3이 될 때 발동 횟수 초기화)\n[AimForTheGoal]이 2 이상일 때 ‘섬궁’을 사용했으면, 다음 턴에 [SlashDamageUp] <style="highlight">2</style> 얻음
   źródło: Passives.json :: dataList[id=1021311].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ArrowShiFau], [Breath], [AimForTheGoal], [SlashDamageUp]
   znaczenie tagów: [ArrowShiFau] = 화살 - 시 / Arrow - Shi; [Breath] = 호흡 / Poise; [AimForTheGoal] = 목표 조준 / Target Aim; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: At 4 [ArrowShiFau] Stack: When this unit gains [Breath] Potency from Base Attack Skill effects, gain +1 [Breath] Count (<style="highlight">3</style> times per Encounter; per-Encounter cap resets when [ArrowShiFau] drops to 3)\nIf this unit used "Bow's Glimmer" Skill at 2+ [AimForTheGoal], gain <style="highlight">2</style> [SlashDamageUp] next turn
   PL:
1057. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Lust) — nazwa] 한점 노리기
   źródło: Passives.json :: dataList[id=1021321].name
   limit: do 40 znaków
   EN: Aiming for the Bullseye
   PL:
1058. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Lust) — opis] 턴 종료 시 전투 중 스킬 및 패시브로 적에게 [Laceration] 위력을 가장 많이 부여한 아군 1명에게 다음 턴에 [PenetrateDamageUp] 1 부여 (E.G.O스킬 포함, [Laceration] 부여량이 동일하다면 편성 순서가 빠른 순으로 결정함, 해당 턴에 [Laceration] 위력을 부여하지 않았다면 발동하지 않음)
   źródło: Passives.json :: dataList[id=1021321].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: [Laceration], [PenetrateDamageUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: Turn End: Apply 1 [PenetrateDamageUp] next turn to the ally who inflicted the most [Laceration] Potency to enemies with its Skills and Passives (includes those from E.G.O Skills; if multiple Identities share the highest [Laceration] inflicted record for the turn, select the Identity earliest in the Deployment order. Does not activate if no one inflicted [Laceration] Potency that turn)
   PL:
1059. [Kwestia głosowa [get_10213_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=get_10213_1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1060. [Kwestia głosowa [get_10213_1] (Identity Acquisition)] 비 들이쳐 어수선하니, 골목께엔 서두르는 소리.\n…그 또한 이제 멎었구나.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=get_10213_1].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rain pelts awake hearts,\nAlleyways puddle with steps;\nThe rest is silence.
   PL:
1061. [Kwestia głosowa [lobby_morning_10213_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=lobby_morning_10213_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1062. [Kwestia głosowa [lobby_morning_10213_1] (Morning Greeting)] 협회의 일이 반드시 밤에만 이뤄진다는 건 뜬소문일 뿐입니다. 저희는 그저 목표에게 어울리는 시간을 찾을 뿐. 야트막한 빛과 새벽내음 사이에도 저희는 존재합니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=lobby_morning_10213_1].dlg
   limit: do 380 znaków
   EN: It is an unfounded rumor that the Association operates only at night; there is no specific time during which we carry out our operations, as they are practicality-based decisions that vary for each target. We also exist in the liminal space between the first light and the early scent of dawn.
   PL:
1063. [Kwestia głosowa [lobby_noon_10213_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=lobby_noon_10213_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1064. [Kwestia głosowa [lobby_noon_10213_1] (Afternoon Greeting)] 잠시, 차를 마시는 시간을 갖지 않으시겠습니까. 격무 속에서도 휴식은 중요합니다. 이 사소한 진실을 간과하면… 언젠가 놓치지 않을 목숨을 놓치기 마련이죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=lobby_noon_10213_1].dlg
   limit: do 310 znaków
   EN: Will you not take a moment to imbibe a cup of tea? One must never forget to take breaks, even when swamped by continuous work. By disregarding this simple fact, one may even be forced to let live a life that was not supposed to see tomorrow.
   PL:
1065. [Kwestia głosowa [lobby_night_10213_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=lobby_night_10213_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1066. [Kwestia głosowa [lobby_night_10213_1] (Evening Greeting)] 밤이 깊었습니다. 공연히 밖에 나오시지 말고 쉬시지요. …파우스트는 가능하면 이 시간대에 한 가지 부류만 만나고 싶습니다. 움직이는 과녁들 말이지요.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=lobby_night_10213_1].dlg
   limit: do 210 znaków
   EN: The hour is late. Rest, and do not unnecessarily expose yourself to the night air. ... Faust prefers to see only one type of life at this hour: moving targets.
   PL:
1067. [Kwestia głosowa [smalltalk_10213_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=smalltalk_10213_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1068. [Kwestia głosowa [smalltalk_10213_1] (Chatter #1)] 목표를 암살하는 것에 정답은 없습니다. 검을 쓰든, 살을 쏘든, 혹은 바닥에 떨어진 돌멩이조차도 훌륭한 암살도구가 될 수 있겠죠.\n각 지부가 가진 환경에 따라 무기를 갖추고 사용할 뿐입니다. 저희는 그것이 궁도(弓刀)일 뿐.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=smalltalk_10213_1].dlg
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There is no single correct answer to assassinations. Anything—a sword, an arrow, or even a pebble on the ground—can be an effective tool for the task.\nEach branch has simply chosen different weapons that fit their environs better. And for us, it happens to be the bowblade.
   PL:
1069. [Kwestia głosowa [smalltalk_10213_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=smalltalk_10213_2].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1070. [Kwestia głosowa [smalltalk_10213_2] (Chatter #2)] 수요에 비해 공급이 지나치게 적지 않은가… 파우스트도 비슷하게 생각합니다. 도시에는 이 장대비처럼, 원한이 빗발치고 있으니까요.\n…그러니만큼, 그 일을 수행할 수 있는 인물이 소수인 것은, 어쩔 수 없는 일인 것입니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=smalltalk_10213_2].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One may wonder if the supply is far behind demand in this business... and so does Faust, to a degree. Resentment floods the City like this pouring rain, after all.\n... Which is why... it cannot be helped that only a few can carry out the deed.
   PL:
1071. [Kwestia głosowa [smalltalk_10213_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=smalltalk_10213_3].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1072. [Kwestia głosowa [smalltalk_10213_3] (Chatter #3)] 바르게 쏘면 반드시 맞기 마련입니다. 그렇지 않았다는 것은 과녁에 쓸데없는 감정을 지녔다는 것이겠죠.\n과녁엔 얼굴도, 기억도, 가족이나 친구도 없습니다. 혹여나 그런 것들을 느끼는 자라면, 이 일에 맞지 않는 것이겠죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=smalltalk_10213_3].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A straight shot will always strike true. If it hasn't, there can be only one explanation: an excessive, unnecessary attachment to the target.\nThe target has no face, no history, no family or friends. Those who see them have no place in this business.
   PL:
1073. [Kwestia głosowa [smalltalk_10213_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=smalltalk_10213_4].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1074. [Kwestia głosowa [smalltalk_10213_4] (Post-Uptie Chat 1)] 온갖 격차가 존재하는 도시 안에서도 한가지 확실한 것은, 죽음이 공평히 찾아온다는 것입니다.\n젖은 땅 위에 무릎 꿇은 걸인에게도… 그자를 내려다보며 고래고래 소리를 지르는 대부업자에게도.\n…의뢰 2건 해결 완료.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=smalltalk_10213_4].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Even in the City of inequities, one thing remains fair: death.\nFairness for the beggar who kneels over the wet pavement... and for the loan shark who disparages him from above.\n... Both contracts completed.
   PL:
1075. [Kwestia głosowa [smalltalk_10213_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=smalltalk_10213_5].desc
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1076. [Kwestia głosowa [smalltalk_10213_5] (Post-Uptie Chat 2)] 활이 적절치 않은 환경 또한 분명 존재합니다. 그렇다면 이 검날로 베어낼 뿐입니다. 근거리와 원거리를 자유로이 활용하는 암살자를 상대하는 건… 제법 곤란할테죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=smalltalk_10213_5].dlg
   limit: do 250 znaków
   EN: Bows are not universally applicable tools, of course, and that is why it has a blade as well. An assassin equipped for both ranged and melee combat makes for a rather... formidable opponent.
   PL:
1077. [Kwestia głosowa [neglect_10213_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=neglect_10213_1].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1078. [Kwestia głosowa [neglect_10213_1] (Idle)] …함께, 들으시겠나요.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=neglect_10213_1].dlg
   limit: do 120 znaków
   EN: ... Will you listen to the rain, together?
   PL:
1079. [Kwestia głosowa [gacksung_10213_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=gacksung_10213_1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1080. [Kwestia głosowa [gacksung_10213_1] (Uptying)] 살을 메기고, 쏩니다. 그러면 과녁엔 구멍이 뚫리고, 곧 쓰러집니다. 그저 그럴 뿐인, 단순한 작업. 빗나감은 일어날 수 없는 일이죠.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=gacksung_10213_1].dlg
   limit: do 170 znaków
   EN: Nock the arrow, pull, loose—it punches through the target, felling it. It is simple, manual labor with very little chance of error.
   PL:
1081. [Kwestia głosowa [formation_10213_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=formation_10213_1].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1082. [Kwestia głosowa [formation_10213_1] (Deployment)] 과녁이 생겼나요.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=formation_10213_1].dlg
   limit: do 120 znaków
   EN: Has the target been designated?
   PL:
1083. [Kwestia głosowa [battleentry_10213_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battleentry_10213_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1084. [Kwestia głosowa [battleentry_10213_1] (Stage Entry)] 우치오코시(打起し).
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battleentry_10213_1].dlg
   limit: do 120 znaków
   EN: Uchiokoshi.
   PL:
1085. [Kwestia głosowa [battle_select_10213_1] — sytuacja] 전투 중 인격 선택 1
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_select_10213_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle 1
   PL:
1086. [Kwestia głosowa [battle_select_10213_1] (Viewed in Battle 1)] 적기를 기다리고 있습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_select_10213_1].dlg
   limit: do 120 znaków
   EN: Waiting for the right moment.
   PL:
1087. [Kwestia głosowa [battle_select_10213_2] — sytuacja] 전투 중 인격 선택 2
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_select_10213_2].desc
   limit: do 120 znaków
   EN: Viewed in Battle 2
   PL:
1088. [Kwestia głosowa [battle_select_10213_2] (Viewed in Battle 2)] …조준 중입니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_select_10213_2].dlg
   limit: do 120 znaków
   EN: ... Target locked.
   PL:
1089. [Kwestia głosowa [battle_endcommand_10213_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_endcommand_10213_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1090. [Kwestia głosowa [battle_endcommand_10213_1] (Commencing Attack)] 빗소리 속에 묻히도록.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_endcommand_10213_1].dlg
   limit: do 120 znaków
   EN: Let the pelting rain bury you.
   PL:
1091. [Kwestia głosowa [battle_enemy_break_10213_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_enemy_break_10213_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1092. [Kwestia głosowa [battle_enemy_break_10213_1] (Enemy Stagger)] 폐를 꿰어냈습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_enemy_break_10213_1].dlg
   limit: do 120 znaków
   EN: Clean shot through the lung.
   PL:
1093. [Kwestia głosowa [battle_break_10213_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_break_10213_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1094. [Kwestia głosowa [battle_break_10213_1] (Staggered)] 음…
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_break_10213_1].dlg
   limit: do 120 znaków
   EN: Mm...
   PL:
1095. [Kwestia głosowa [battle_kill_10213_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_kill_10213_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1096. [Kwestia głosowa [battle_kill_10213_1] (Enemy Killed)] 명중.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_kill_10213_1].dlg
   limit: do 120 znaków
   EN: Bullseye.
   PL:
1097. [Kwestia głosowa [battle_dead_10213_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_dead_10213_1].desc
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1098. [Kwestia głosowa [battle_dead_10213_1] (Death)] 평등함이 제게도 찾아왔을… 뿐입니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_dead_10213_1].dlg
   limit: do 120 znaków
   EN: Again, fairness is simply a universal concept—even... for me.
   PL:
1099. [Kwestia głosowa [choice_success_p_10213_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=choice_success_p_10213_2].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1100. [Kwestia głosowa [choice_success_p_10213_2] (Check Passed)] 암살자에겐 너무 기초적인 일이군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=choice_success_p_10213_2].dlg
   limit: do 120 znaków
   EN: Elementary work for an assassin.
   PL:
1101. [Kwestia głosowa [choice_fail_n_10213_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=choice_fail_n_10213_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1102. [Kwestia głosowa [choice_fail_n_10213_1] (Check Failed)] …활을 너무 높게 쥐었군요.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=choice_fail_n_10213_1].dlg
   limit: do 120 znaków
   EN: ... Aimed too high.
   PL:
1103. [Kwestia głosowa [battle_clear_10213_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_clear_10213_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1104. [Kwestia głosowa [battle_clear_10213_1] (Victory Cry)] 의뢰는 완수했습니다. 종국에 가서 근접전을 펼쳐야만 했던 것은 다소 아쉽지만… 늘 그렇듯, 목격한 자가 없는 마무리였습니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_clear_10213_1].dlg
   limit: do 140 znaków
   EN: Contract fulfilled. While having to resort to melee was regrettable... as always, there were no witnesses.
   PL:
1105. [Kwestia głosowa [battle_clear_ex_10213_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_clear_ex_10213_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1106. [Kwestia głosowa [battle_clear_ex_10213_1] (Extra Conditions Fulfilled)] 하늘에서 쏟아지는 장대비 사이에는 쏜살들이 숨어있었습니다. 저들은 어디서 들이치는 빗발인지도 모르고 명을 달리했겠지요. 이것이 동부의 암살법입니다.
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_clear_ex_10213_1].dlg
   limit: do 200 znaków
   EN: The pelting raindrops shroud the falling arrows, and they will die in the downpour without knowing what killed them. This is how the eastern branch kills.
   PL:
1107. [Kwestia głosowa [battle_defeat_10213_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_defeat_10213_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1108. [Kwestia głosowa [battle_defeat_10213_1] (Defeat Wail)] 제 핏물을 활줄에 먹여가며 싸워냈지만… 기회도, 운도 따라주지 않았습니다. 의뢰의 실패는 곧 죽음이니… 사(死)의 경계에서 미끄러진 저는, 여기서 명을 달리하겠군요…
   źródło: PersonalityVoiceDlg/Voice_Faust_ShiAsso2_10213.json :: dataList[id=battle_defeat_10213_1].dlg
   limit: do 310 znaków
   EN: Though I infused this bow with my very own blood... neither opportunity nor luck were on my side. As a failure to complete a contract results in death... this shall be my end, for I have slipped to the wrong side of the boundary of death.
   PL:
