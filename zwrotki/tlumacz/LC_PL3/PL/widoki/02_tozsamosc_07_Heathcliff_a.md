# Grzesznik #07: Heathcliff — Tożsamości, umiejętności, pasywki i głos (część a) — Limbus Company

Kompletny zestaw kart Tożsamości postaci **Heathcliff** (히스클리프) wraz z umiejętnościami na ulepszeniach 1–4, efektami monet, pasywkami i kwestiami głosowymi.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Grzesznik #07: Heathcliff (히스클리프)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 히스클리프
   źródło: Characters.json :: dataList[id=7].name
   limit: do 40 znaków
   EN: Heathcliff
   PL:
2. [Akta więźnia — nazwa] 히스클리프
   źródło: IntroduceCharacter.json :: dataList[id=히스클리프].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
3. [Akta więźnia — opis] 논리적인 사고보다는 행동으로 실행하는 것을 더 선호하는 수감자입니다.\n생각과 감정이 표정과 말에서 다 드러나며 숨길 노력도 하지 않으므로\n관리자님과의 관계 형성에서 두통을(또는 물리적인 외상까지...)\n유발할 수도 있습니다. 수감자의 사고 체계에 심각한\n문제가 있는 것은 아님을 숙지해 주시길 바랍니다. 만일 장시간 동안\n분노가 가라앉지 않는다면 인사 부서에 문의주세요. 하지만 이런 유형일수록\n생각이 멍청하고 단순하다는 것만 익힌다면 다루기 쉬운 법이죠.
   źródło: IntroduceCharacter.json :: dataList[id=히스클리프].description
   limit: do 750 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This Sinner prefers to take action rather than wait for logic to dictate his course.\nHis thoughts and feelings are blatantly visible in his demeanor, and he has no intention of hiding them;\nhis brashness may cause headaches (or physical injury leading to a headache) in the process of forming a relationship.\nPlease do note that this is not an indication of serious damage to the Sinner's thought process.\nIf his fit of rage persists, please contact the human resources department.\nOnce you realize that he is the type that tends to be simple-minded,\nyou'll have an easier time handling him.
   PL: Grzesznik, który od logicznego myślenia woli działanie.\nMyśli i uczucia ma wypisane na twarzy i w słowach, i nawet nie próbuje ich ukryć,\nmoże więc przysporzyć panu bólu głowy (albo i obrażeń fizycznych…)\nprzy budowaniu wzajemnych relacji. Prosimy pamiętać, że nie świadczy to\no poważnym zaburzeniu jego procesów myślowych. Jeśli gniew długo nie mija,\nprosimy o kontakt z działem kadr. Ale z takimi typami jest łatwo,\ngdy tylko się pojmie, że myślą głupio i prosto.

## [0] LCB Sinner — Heathcliff — LCB 수감자
- ID Tożsamości: `10701` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 78 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor

4. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10701].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL:
5. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10701].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10701].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Karta Tożsamości — opis] 히스클리프의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10701].desc
   limit: do 120 znaków
   EN: Heathcliff’s 1st Identity
   PL:
8. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 배트 치기
   źródło: Skills.json :: dataList[id=1070101].levelList[level=1].name ; dataList[id=1070101].levelList[level=2].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Bat Bash
   PL:
9. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 3 부여
   źródło: Skills.json :: dataList[id=1070101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 3 [Vibration]
   PL:
10. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills.json :: dataList[id=1070101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL:
11. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 내려박기
   źródło: Skills.json :: dataList[id=1070102].levelList[level=1].name ; dataList[id=1070102].levelList[level=2].name ; dataList[id=1070102].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Smackdown
   PL:
12. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills.json :: dataList[id=1070102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Attack Power Up next turn
   PL:
13. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WhenUse] 다음 턴에 공격 위력 증가, 피해량 증가 1 얻음
   źródło: Skills.json :: dataList[id=1070102].levelList[level=2].desc ; dataList[id=1070102].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Attack Power Up and Damage Up next turn
   PL:
14. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills.json :: dataList[id=1070102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 2 [Vibration]
   PL:
15. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 분풀기
   źródło: Skills.json :: dataList[id=1070103].levelList[level=3].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 4 · monety: 2 (+8)
   limit: do 40 znaków
   EN: Upheaval
   PL:
16. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 코인 위력 +2
   źródło: Skills.json :: dataList[id=1070103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Next Coin has +2 Power
   PL:
17. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills.json :: dataList[id=1070103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL:
18. [Obrona (ulepszenie 1) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1070104].levelList[level=1].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 7 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Counter
   PL:
19. [Pasywka bojowa (od ulepszenia 1, rezonans 4× Envy) — nazwa] 르쌍티망
   źródło: Passives.json :: dataList[id=1070101].name
   limit: do 40 znaków
   EN: Ressentiment
   PL:
20. [Pasywka bojowa (od ulepszenia 1, rezonans 4× Envy) — opis] 대상이 자신보다 최대 체력이 높으면 피해량 +10%
   źródło: Passives.json :: dataList[id=1070101].desc
   limit: do 120 znaków
   EN: Deal +10% damage to targets that have higher Max HP.
   PL:
21. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — nazwa] 악에 받친
   źródło: Passives.json :: dataList[id=1070121].name
   limit: do 40 znaków
   EN: Spite-driven
   PL:
22. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — opis] 최대 체력이 가장 낮은 아군 1명 타격 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1070121].desc
   limit: do 120 znaków
   EN: 1 ally that has the lowest Max HP deals +10% Blunt damage.
   PL:
23. [Kwestia głosowa [get_10701_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=get_10701_1].desc
   limit: do 120 znaków
   EN: Identity Acquisition
   PL:
24. [Kwestia głosowa [get_10701_1] (Identity Acquisition)] 히스클리프. 사람 박살 내는 건 내 전문이지. 물론, 내가 내킬 때만.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=get_10701_1].dlg
   limit: do 120 znaków
   EN: Name’s Heathcliff. Clobbering people is my specialty. ‘Course, only when I fancy it.
   PL:
25. [Kwestia głosowa [lobby_morning_10701_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=lobby_morning_10701_1].desc
   limit: do 120 znaków
   EN: Morning Greeting
   PL:
26. [Kwestia głosowa [lobby_morning_10701_1] (Morning Greeting)] 아침부터 그 시계 좀 치워라… 거슬리니까.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=lobby_morning_10701_1].dlg
   limit: do 120 znaków
   EN: Keep that clock away from my face… It’s irritating.
   PL:
27. [Kwestia głosowa [lobby_noon_10701_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=lobby_noon_10701_1].desc
   limit: do 120 znaków
   EN: Afternoon Greeting
   PL:
28. [Kwestia głosowa [lobby_noon_10701_1] (Afternoon Greeting)] 왜? 점심은 뭐 드셨어요? 이딴 말 기대하고 나한테 온 건 아니지?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=lobby_noon_10701_1].dlg
   limit: do 120 znaków
   EN: What? Expecting me to ask what scran you had for lunch or some mince?
   PL:
29. [Kwestia głosowa [lobby_night_10701_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=lobby_night_10701_1].desc
   limit: do 120 znaków
   EN: Evening Greeting
   PL:
30. [Kwestia głosowa [lobby_night_10701_1] (Evening Greeting)] 아 잠깐, 또 훈련이니 작전이니 시킬 거라면 다시 생각하고 말하는 게 좋을 거야.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=lobby_night_10701_1].dlg
   limit: do 130 znaków
   EN: Now stop your gob. If you’re thinking of ordering more training or missions, you’d best think twice.
   PL:
31. [Kwestia głosowa [smalltalk_10701_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=smalltalk_10701_1].desc
   limit: do 120 znaków
   EN: Chatter #1
   PL:
32. [Kwestia głosowa [smalltalk_10701_1] (Chatter #1)] 관리자라고 해서 훈계하거나 쓸데없는 계획 세울 생각은 하지 마라. 난 남의 말은 안 듣거든.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=smalltalk_10701_1].dlg
   limit: do 170 znaków
   EN: Just ‘cause you’re the manager doesn’t mean you get to lecture me or shove me into shoddy plans. I don’t follow anyone’s orders.
   PL:
33. [Kwestia głosowa [smalltalk_10701_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=smalltalk_10701_2].desc
   limit: do 120 znaków
   EN: Chatter #2
   PL:
34. [Kwestia głosowa [smalltalk_10701_2] (Chatter #2)] 형씨, 궁금하지 않아? 그 시계 안쪽이 어떻게 생겼을지 말이야. 하핫. 농담이야 왜 몸을 떨고 그래?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=smalltalk_10701_2].dlg
   limit: do 220 znaków
   EN: Don’t you ever get curious about what’s on the other side of that clock on your shoulders, mate? Hahah, I was just taking the piss. What’s got you shaking like timber?
   PL:
35. [Kwestia głosowa [smalltalk_10701_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=smalltalk_10701_3].desc
   limit: do 120 znaków
   EN: Chatter #3
   PL:
36. [Kwestia głosowa [smalltalk_10701_3] (Chatter #3)] 우리 사이에 긴 대화는 필요 없지. 주먹으로 하는 거라면 모를까.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=smalltalk_10701_3].dlg
   limit: do 120 znaków
   EN: No need for long gabs between us. Not about to turn down an exchange of punches, though.
   PL:
37. [Kwestia głosowa [neglect_10701_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=neglect_10701_1].desc
   limit: do 120 znaków
   EN: Idle
   PL:
38. [Kwestia głosowa [neglect_10701_1] (Idle)] 그래, 한 대 맞고 싶다는 거지? 딱 기다려.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=neglect_10701_1].dlg
   limit: do 120 znaków
   EN: Right, so you wanna get smacked, ey? Stay right there.
   PL:
39. [Kwestia głosowa [formation_10701_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=formation_10701_1].desc
   limit: do 120 znaków
   EN: Deployment
   PL:
40. [Kwestia głosowa [formation_10701_1] (Deployment)] 몸이 찌뿌둥하던 참이었어. 때려 부수러 갈 시간이다!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=formation_10701_1].dlg
   limit: do 120 znaków
   EN: I was craving a workout. Time to smash stuff right up!
   PL:
41. [Kwestia głosowa [battleentry_10701_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battleentry_10701_1].desc
   limit: do 120 znaków
   EN: Stage Entry
   PL:
42. [Kwestia głosowa [battleentry_10701_1] (Stage Entry)] 길게 끌 거 없어, 바로 간다!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battleentry_10701_1].dlg
   limit: do 120 znaków
   EN: Don’t make it long, I’m going in!
   PL:
43. [Kwestia głosowa [battle_select_10701_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_select_10701_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle
   PL:
44. [Kwestia głosowa [battle_select_10701_1] (Viewed in Battle)] 왜? 뭐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_select_10701_1].dlg
   limit: do 120 znaków
   EN: What? Why?
   PL:
45. [Kwestia głosowa [battle_endcommand_10701_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_endcommand_10701_1].desc
   limit: do 120 znaków
   EN: Commencing Attack
   PL:
46. [Kwestia głosowa [battle_endcommand_10701_1] (Commencing Attack)] 먼저 간다!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_endcommand_10701_1].dlg
   limit: do 120 znaków
   EN: Already there!
   PL:
47. [Kwestia głosowa [battle_enemy_break_10701_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_enemy_break_10701_1].desc
   limit: do 120 znaków
   EN: Enemy Stagger
   PL:
48. [Kwestia głosowa [battle_enemy_break_10701_1] (Enemy Stagger)] 하핫, 어떠냐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_enemy_break_10701_1].dlg
   limit: do 120 znaków
   EN: Haha, how do ya like that?
   PL:
49. [Kwestia głosowa [battle_break_10701_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_break_10701_1].desc
   limit: do 120 znaków
   EN: Staggered
   PL:
50. [Kwestia głosowa [battle_break_10701_1] (Staggered)] 윽…!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_break_10701_1].dlg
   limit: do 120 znaków
   EN: Grh…!
   PL:
51. [Kwestia głosowa [battle_kill_10701_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_kill_10701_1].desc
   limit: do 120 znaków
   EN: Enemy Killed
   PL:
52. [Kwestia głosowa [battle_kill_10701_1] (Enemy Killed)] 쉽네.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_kill_10701_1].dlg
   limit: do 120 znaków
   EN: Piss easy.
   PL:
53. [Kwestia głosowa [battle_allydead_10701_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_allydead_10701_1].desc
   limit: do 120 znaków
   EN: Ally Death
   PL:
54. [Kwestia głosowa [battle_allydead_10701_1] (Ally Death)] 뭐야, 언제 으깨졌냐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_allydead_10701_1].dlg
   limit: do 120 znaków
   EN: What? When’d you get smashed to bits?
   PL:
55. [Kwestia głosowa [choice_success_p_10701_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=choice_success_p_10701_1].desc
   limit: do 120 znaków
   EN: Check Passed
   PL:
56. [Kwestia głosowa [choice_success_p_10701_1] (Check Passed)] 너 왜 뿌듯해 보이냐? 내가 해낸 건데.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=choice_success_p_10701_1].dlg
   limit: do 120 znaków
   EN: What’s that proud look? I’m the one who dealt with it.
   PL:
57. [Kwestia głosowa [choice_fail_n_10701_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=choice_fail_n_10701_1].desc
   limit: do 120 znaków
   EN: Check Failed
   PL:
58. [Kwestia głosowa [choice_fail_n_10701_1] (Check Failed)] …열받네. 내가 딴 놈 보내라 하지 않았었냐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=choice_fail_n_10701_1].dlg
   limit: do 120 znaków
   EN: …This is really narking me. Didn’t I tell you to get someone else?
   PL:
59. [Kwestia głosowa [battle_clear_10701_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_clear_10701_1].desc
   limit: do 120 znaków
   EN: Victory Cry
   PL:
60. [Kwestia głosowa [battle_clear_10701_1] (Victory Cry)] 뭐, 이 정도에 좋다고 히죽거리고 싶진 않아.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_clear_10701_1].dlg
   limit: do 120 znaków
   EN: Well, don’t wanna giggle over small victories.
   PL:
61. [Kwestia głosowa [battle_clear_ex_10701_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_clear_ex_10701_1].desc
   limit: do 120 znaków
   EN: Extra Conditions Fulfilled
   PL:
62. [Kwestia głosowa [battle_clear_ex_10701_1] (Extra Conditions Fulfilled)] 흥, 보여? 마구잡이로 때려 부숴놓았지!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_clear_ex_10701_1].dlg
   limit: do 120 znaków
   EN: Heh, see that? I did a real bang up job!
   PL:
63. [Kwestia głosowa [battle_defeat_10701_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_defeat_10701_1].desc
   limit: do 120 znaków
   EN: Defeat Wail
   PL:
64. [Kwestia głosowa [battle_defeat_10701_1] (Defeat Wail)] 젠장, 이거 진짜 열받네! 형씨, 여기서 안 끝낼 거지?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LCB_10701.json :: dataList[id=battle_defeat_10701_1].dlg
   limit: do 120 znaków
   EN: Bugger all, this’s got me pure raging! You ain’t gonna let this go, right, mate?
   PL:

## [00] Shi Assoc. South Section 5 — Heathcliff — 남부 시 협회 5과
- ID Tożsamości: `10702` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Poise

65. [Karta Tożsamości — tytuł] 남부 시 협회\n5과
   źródło: Personalities.json :: dataList[id=10702].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Shi Assoc.\nSouth Section 5
   PL:
66. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10702].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10702].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [Karta Tożsamości — opis] 히스클리프의 두번째 인격
   źródło: Personalities.json :: dataList[id=10702].desc
   limit: do 120 znaków
   EN: Heathcliff’s 2nd Identity
   PL:
69. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 극검
   źródło: Skills.json :: dataList[id=1070201].levelList[level=1].name ; dataList[id=1070201].levelList[level=2].name ; dataList[id=1070201].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Extreme Edge
   PL:
70. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 자신의 체력이 25%미만일 때 스킬 위력 +1
   źródło: Skills.json :: dataList[id=1070201].levelList[level=1].desc
   limit: do 120 znaków
   EN: At less than 25% HP, +1 Skill Power
   PL:
71. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 자신의 체력이 25%미만일 때 스킬 위력 +2
   źródło: Skills.json :: dataList[id=1070201].levelList[level=2].desc
   limit: do 120 znaków
   EN: At less than 25% HP, +2 Skill Power
   PL:
72. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 체력이 50%미만일 때 스킬 위력 +2\n[WhenUse] 호흡 횟수 3 얻음
   źródło: Skills.json :: dataList[id=1070201].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: At less than 50% HP, Skill Power +2\n[WhenUse] Gain +3 [Breath] Count
   PL:
73. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 비검
   źródło: Skills.json :: dataList[id=1070202].levelList[level=1].name ; dataList[id=1070202].levelList[level=2].name ; dataList[id=1070202].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 5 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Flying Sword
   PL:
74. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 자신의 체력이 25%미만일 때 스킬 위력 +1
   źródło: Skills.json :: dataList[id=1070202].levelList[level=1].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 자신의 체력이 25%미만일 때 스킬 위력 +2
   źródło: Skills.json :: dataList[id=1070202].levelList[level=2].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 체력이 50%미만일 때 스킬 위력 +2\n[WhenUse] 호흡 3 얻음
   źródło: Skills.json :: dataList[id=1070202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: At less than 50% HP, +2 Skill Power\n[WhenUse] Gain 3 [Breath]
   PL:
77. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 섬격
   źródło: Skills.json :: dataList[id=1070203].levelList[level=3].name ; dataList[id=1070203].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Flashing Strike
   PL:
78. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 체력이 25%미만일 때 스킬 위력 +2
   źródło: Skills.json :: dataList[id=1070203].levelList[level=3].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [BeforeAttack] 자신의 체력 5 감소, 이 코인의 스킬 피해량 +50%
   źródło: Skills.json :: dataList[id=1070203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1070203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] Lose 5 HP; +50% Skill Damage for this Coin
   PL:
80. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [BeforeAttack] 자신의 체력 5 감소, 이 코인의 스킬 피해량 +50%
   źródło: Skills.json :: dataList[id=1070203].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1070203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 호흡 횟수가 10 이상이면, 스킬 위력 +2\n자신의 체력이 50%미만일 때, 공격 가중치 +1
   źródło: Skills.json :: dataList[id=1070203].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 10+ [Breath] Count, Skill Power +2\nAt less than 50% HP, Atk Weight +1
   PL:
82. [Obrona (ulepszenia 1,4) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1070204].levelList[level=1].name ; dataList[id=1070204].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 8 · monety: 1 (+5)
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 체력 5 감소\n자신의 호흡 횟수가 3 이상이면, 피해량 +50%
   źródło: Skills.json :: dataList[id=1070204].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Lose 5 HP\nAt 3+ [Breath] Count, Damage +50%
   PL:
84. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — nazwa] 호흡
   źródło: Passives.json :: dataList[id=1070201].name
   limit: do 40 znaków
   EN: Respiration
   PL:
85. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — opis] 이번 턴에 공격으로 피해를 받으면 피해량 +10%
   źródło: Passives.json :: dataList[id=1070201].desc
   limit: do 120 znaków
   EN: After taking damage from attacks this turn, deal +10% damage.
   PL:
86. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 자신을 돌보지 않음
   źródło: Passives.json :: dataList[id=1070221].name
   limit: do 40 znaków
   EN: Self-neglect
   PL:
87. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 현재 체력이 가장 낮은 아군 1명 가하는 피해량 +20%, 받는 피해량 +20%
   źródło: Passives.json :: dataList[id=1070221].desc
   limit: do 120 znaków
   EN: 1 ally with the least HP deals and takes +20% damage.
   PL:
88. [Kwestia głosowa [get_10702_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=get_10702_1].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Kwestia głosowa [get_10702_1] (Identity Acquisition)] 공평하게 죽음을… 쯧. 뭐랬더라, 아무튼 다 박살 내러 왔다.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=get_10702_1].dlg
   limit: do 120 znaków
   EN: Equal death to something or… Tch. Whatever, I’m here to wreck stuff.
   PL:
90. [Kwestia głosowa [lobby_morning_10702_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=lobby_morning_10702_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Kwestia głosowa [lobby_morning_10702_1] (Morning Greeting)] 아씨… 아까 자명종 계속 안 끄고 자던 놈 누구였냐? 가만 안 두겠어…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=lobby_morning_10702_1].dlg
   limit: do 130 znaków
   EN: Bollocks… Who’s the one that kept sleeping while their alarm was clanging off? I’ll make ‘em pay…
   PL:
92. [Kwestia głosowa [lobby_noon_10702_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=lobby_noon_10702_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [Kwestia głosowa [lobby_noon_10702_1] (Afternoon Greeting)] 점심은… 싱싱한 날 음식이나 먹고 싶네. 피가 뚝뚝 떨어지거나 하는 거 말이야.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=lobby_noon_10702_1].dlg
   limit: do 120 znaków
   EN: For lunch… I’d like something raw. The kind of stuff that’s got blood dripping from it.
   PL:
94. [Kwestia głosowa [lobby_night_10702_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=lobby_night_10702_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Kwestia głosowa [lobby_night_10702_1] (Evening Greeting)] 형씨는 붉은 달을 본 적 있어? 끝내주게 아름답거든. 순식간에 반해버렸지 뭐야.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=lobby_night_10702_1].dlg
   limit: do 120 znaków
   EN: Ever see a red moon, mate? It’s a stoater. Fell in love with it at first sight.
   PL:
96. [Kwestia głosowa [smalltalk_10702_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=smalltalk_10702_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Kwestia głosowa [smalltalk_10702_1] (Chatter #1)] …상처가 걱정된다고? 방금 온몸에 소름 돋았거든? 다신 그딴 말 꺼내지 마라.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=smalltalk_10702_1].dlg
   limit: do 130 znaków
   EN: …Worried about my wounds? Bloody hell, that’s a right scunner. Don’t you ever say that to me again.
   PL:
98. [Kwestia głosowa [smalltalk_10702_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=smalltalk_10702_2].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Kwestia głosowa [smalltalk_10702_2] (Chatter #2)] 목격자가 전부 뒤지면 그게 암살이지 뭐겠어? 젠장, 다들 나한테만 성질이야.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=smalltalk_10702_2].dlg
   limit: do 160 znaków
   EN: If there’s no witnesses alive to clepe, that’s assassination—what more do you need? Buggers won’t stop narking me about it.
   PL:
100. [Kwestia głosowa [smalltalk_10702_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=smalltalk_10702_3].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Kwestia głosowa [smalltalk_10702_3] (Chatter #3)] 급소만 찌르는 건 사실 재미 없어. 시시하잖아?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=smalltalk_10702_3].dlg
   limit: do 120 znaków
   EN: Stabbing the jugular all the time’s frankly boring. Outright unfun even, innit?
   PL:
102. [Kwestia głosowa [smalltalk_10702_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=smalltalk_10702_4].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 1
   PL:
103. [Kwestia głosowa [smalltalk_10702_4] (Post-Uptie Chat 1)] 다들 말 같지도 않는 말만 나불거려. 마음을 가라앉히고 고요하게 어쩌고저쩌고… 그냥 싸그리 부숴버리면 서로 편한 거 아니겠어?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=smalltalk_10702_4].dlg
   limit: do 200 znaków
   EN: My mates keep saying daft rubbish. All that mince about inner peace n’ quiet or what have you… Ain’t it best for all of us to just wreck shite and move on?
   PL:
104. [Kwestia głosowa [smalltalk_10702_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=smalltalk_10702_5].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 2
   PL:
105. [Kwestia głosowa [smalltalk_10702_5] (Post-Uptie Chat 2)] 그래도 형씨는 군 말없이 시계 돌려줘서 맘에 들어. 특히 지난번에 어깨가 꿰뚫렸던 건 드럽게 아팠을 텐데 말이야.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=smalltalk_10702_5].dlg
   limit: do 200 znaków
   EN: I like that ya turn that clock without complaining much. That hole someone jabbed in my shoulder the other day must’ve been a right bugger to heal, too.
   PL:
106. [Kwestia głosowa [neglect_10702_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=neglect_10702_1].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Kwestia głosowa [neglect_10702_1] (Idle)] 어디 간 거야? 젠장, 이스마엘이었으면 바로 찾아냈을 텐데…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=neglect_10702_1].dlg
   limit: do 120 znaków
   EN: Where’d you get off to? Damn, Ishmael would’ve spotted them in seconds…
   PL:
108. [Kwestia głosowa [gacksung_10702_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=gacksung_10702_1].desc
   limit: do 120 znaków
   EN: Uptying
   PL:
109. [Kwestia głosowa [gacksung_10702_1] (Uptying)] 그만하라고 말릴 때까지 다 썰어버릴 수 있어!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=gacksung_10702_1].dlg
   limit: do 120 znaków
   EN: I can keep on butchering ‘em ‘til you tell me to stop!
   PL:
110. [Kwestia głosowa [formation_10702_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=formation_10702_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [Kwestia głosowa [formation_10702_1] (Deployment)] 그래, 후회하지 않게 해주지!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=formation_10702_1].dlg
   limit: do 120 znaków
   EN: Right, I’ll give you something you won’t regret!
   PL:
112. [Kwestia głosowa [battleentry_10702_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battleentry_10702_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Kwestia głosowa [battleentry_10702_1] (Stage Entry)] 그냥 눈에 보이는 거 다 박살 내면 되는 거지?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battleentry_10702_1].dlg
   limit: do 120 znaków
   EN: Just have to crush everything I see, aye?
   PL:
114. [Kwestia głosowa [battle_select_10702_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_select_10702_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Kwestia głosowa [battle_select_10702_1] (Viewed in Battle)] 그래, 누굴 조지면 되는 거야?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_select_10702_1].dlg
   limit: do 120 znaków
   EN: Alright, who do you want me to scrap?
   PL:
116. [Kwestia głosowa [battle_endcommand_10702_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_endcommand_10702_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Kwestia głosowa [battle_endcommand_10702_1] (Commencing Attack)] 그래, 베러 가자!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_endcommand_10702_1].dlg
   limit: do 120 znaków
   EN: Aye, I’ll go cut ‘em!
   PL:
118. [Kwestia głosowa [battle_enemy_break_10702_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_enemy_break_10702_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Kwestia głosowa [battle_enemy_break_10702_1] (Enemy Stagger)] 어때, 죽을 것 같지?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_enemy_break_10702_1].dlg
   limit: do 120 znaków
   EN: How’s that? Hurts to death, don’t it?
   PL:
120. [Kwestia głosowa [battle_break_10702_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_break_10702_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Kwestia głosowa [battle_break_10702_1] (Staggered)] 쳇…!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_break_10702_1].dlg
   limit: do 120 znaków
   EN: Tch…!
   PL:
122. [Kwestia głosowa [battle_kill_10702_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_kill_10702_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Kwestia głosowa [battle_kill_10702_1] (Enemy Killed)] 타겟, 제거~
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_kill_10702_1].dlg
   limit: do 120 znaków
   EN: Target wiped~
   PL:
124. [Kwestia głosowa [battle_allydead_10702_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_allydead_10702_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Kwestia głosowa [battle_allydead_10702_1] (Ally Death)] 실력도 없는데 드러내고 다니니 그러지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_allydead_10702_1].dlg
   limit: do 120 znaków
   EN: Shouldn’t be out in the open if you don’t have the skills to handle it.
   PL:
126. [Kwestia głosowa [choice_success_p_10702_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=choice_success_p_10702_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Kwestia głosowa [choice_success_p_10702_1] (Check Passed)] 이거 봐. 과정은 어쨌든 결과는 좋잖아?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=choice_success_p_10702_1].dlg
   limit: do 120 znaków
   EN: Look ‘ere. Process be damned, it all turned out well and fine in the end, aye?
   PL:
128. [Kwestia głosowa [choice_fail_n_10702_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=choice_fail_n_10702_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Kwestia głosowa [choice_fail_n_10702_1] (Check Failed)] 하여간에, 맞지도 않는 곳에 보내는 건 어느 놈이든 똑같네.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=choice_fail_n_10702_1].dlg
   limit: do 120 znaków
   EN: Not the first time I’m sent to do work I’m not fit for.
   PL:
130. [Kwestia głosowa [battle_clear_10702_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_clear_10702_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Kwestia głosowa [battle_clear_10702_1] (Victory Cry)] 이 정도야 기본이지. 또 찌를 거 없냐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_clear_10702_1].dlg
   limit: do 120 znaków
   EN: This was simple. Anything else for me to stab?
   PL:
132. [Kwestia głosowa [battle_clear_ex_10702_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_clear_ex_10702_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Kwestia głosowa [battle_clear_ex_10702_1] (Extra Conditions Fulfilled)] 다 내 먹잇감들이었지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_clear_ex_10702_1].dlg
   limit: do 120 znaków
   EN: They were all prey to me.
   PL:
134. [Kwestia głosowa [battle_defeat_10702_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_defeat_10702_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Kwestia głosowa [battle_defeat_10702_1] (Defeat Wail)] 아직 내 칼은 안 끝났어! 형씨, 한 번 더 가자고!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_ShiAsso4_10702.json :: dataList[id=battle_defeat_10702_1].dlg
   limit: do 120 znaków
   EN: My sword says it ain’t done yet! Mate, we’re going back in!
   PL:

## [000] R Corp. 4th Pack Rabbit — Heathcliff — R사 제 4무리 토끼팀
- ID Tożsamości: `10703` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Charge, Bleed, Rupture

136. [Karta Tożsamości — tytuł] R사 제 4무리\n토끼팀
   źródło: Personalities.json :: dataList[id=10703].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: R Corp. 4th Pack\nRabbit
   PL:
137. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10703].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10703].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Karta Tożsamości — opis] 히스클리프의 세번째 인격
   źródło: Personalities.json :: dataList[id=10703].desc
   limit: do 120 znaków
   EN: Heathcliff’s 3rd Identity
   PL:
140. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 풀뜯기
   źródło: Skills.json :: dataList[id=1070301].levelList[level=1].name ; dataList[id=1070301].levelList[level=2].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Graze the Grass
   PL:
141. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] 탄환 1 소모
   źródło: Skills.json :: dataList[id=1070301].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1070301].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: Spend 1 Ammo
   PL:
142. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] 탄환 1 소모
   źródło: Skills.json :: dataList[id=1070301].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1070301].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 1 증가
   źródło: Skills.json :: dataList[id=1070301].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +1 Charge Count
   PL:
144. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 3 증가
   źródło: Skills.json :: dataList[id=1070301].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +3 Charge Count
   PL:
145. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 집중 사격
   źródło: Skills.json :: dataList[id=1070302].levelList[level=1].name ; dataList[id=1070302].levelList[level=2].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Concentrated Fire
   PL:
146. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070302].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1070302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: Spend 1 Ammo\n[OnSucceedAttack] Inflict 1 Bleed
   PL:
147. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070302].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1070302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070302].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1070302].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 속도가 6 이상이면, 코인 위력 + 1
   źródło: Skills.json :: dataList[id=1070302].levelList[level=2].desc
   limit: do 120 znaków
   EN: Coin Power +1 at 6+ Speed
   PL:
150. [Umiejętność 3 (×1) (ulepszenie 1) — nazwa] 신속한 제압
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 3 · monety: 5 (+2)
   limit: do 40 znaków
   EN: Quick Suppression
   PL:
151. [Umiejętność 3 (×1) (ulepszenie 1) — opis] 속도가 6 이상이면, 코인 위력 + 2
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].desc
   limit: do 120 znaków
   EN: Coin Power +2 at 6+ Speed
   PL:
152. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 1, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 취약 2 부여
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: Spend 1 Ammo\n[OnSucceedAttack] Inflict 2 Fragile
   PL:
153. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 2, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 취약 2 부여
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Rupture
   PL:
155. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL:
156. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 5, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].coinlist[#4].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture
   PL:
157. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1070304].levelList[level=1].name ; dataList[id=1070304].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL:
158. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 1 증가
   źródło: Skills.json :: dataList[id=1070304].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +1 Charge Count
   PL:
159. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — nazwa] 풀 뜯을 준비
   źródło: Passives.json :: dataList[id=1070301].name
   limit: do 40 znaków
   EN: Raring to Graze
   PL:
160. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — opis] 다음 턴 시작 시 (분노 공명 수)만큼 충전 횟수 증가.\n충전 횟수가 5 이상이면 신속 1, 공격 위력 증가 1을 얻음
   źródło: Passives.json :: dataList[id=1070301].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Gain (Wrath Reson.) Charge Count next turn.\nAt 5+ Charge Count, gain 1 [Agility] and Attack Power Up.
   PL:
161. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — nazwa] 집념
   źródło: Passives.json :: dataList[id=1070321].name
   limit: do 40 znaków
   EN: Doggedness
   PL:
162. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — opis] 속도가 가장 높은 아군 1명 관통 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1070321].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed deals +10% Pierce damage.
   PL:
163. [Kwestia głosowa [get_10703_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=get_10703_1].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Kwestia głosowa [get_10703_1] (Identity Acquisition)] 깡총깡총… 뛰면서… 토끼가 왔다. 다 쳐부수러!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=get_10703_1].dlg
   limit: do 120 znaków
   EN: Hippity-hop… Out on a bop… The rabbit hops in. To smash it to bits!
   PL:
165. [Kwestia głosowa [lobby_morning_10703_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=lobby_morning_10703_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Kwestia głosowa [lobby_morning_10703_1] (Morning Greeting)] 뭐? 새벽에 세수하러 온 토끼 처음 보냐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=lobby_morning_10703_1].dlg
   limit: do 120 znaków
   EN: What? Never seen a hare up early to wash his face before?
   PL:
167. [Kwestia głosowa [lobby_noon_10703_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=lobby_noon_10703_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Kwestia głosowa [lobby_noon_10703_1] (Afternoon Greeting)] 어디 괜찮은 작전 없나? 생각만 해도 피가 돌고 눈이 붉어질 것 같은… 그런 화끈한 작전 말이야.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=lobby_noon_10703_1].dlg
   limit: do 150 znaków
   EN: Got any good missions for me? The kind that gets the blood pumping and eyes fierce… One of those exciting ones.
   PL:
169. [Kwestia głosowa [lobby_night_10703_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=lobby_night_10703_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Kwestia głosowa [lobby_night_10703_1] (Evening Greeting)] 이래 보여도 난 야행성이야. 어둠은 날 더 날뛰게 해준다는 뜻이지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=lobby_night_10703_1].dlg
   limit: do 120 znaków
   EN: I may not look it, but I’m a nocturnal creature—means the dark spurs me further.
   PL:
171. [Kwestia głosowa [smalltalk_10703_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=smalltalk_10703_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Kwestia głosowa [smalltalk_10703_1] (Chatter #1)] 이봐! 가만히 앉아서 시시껄렁한 수다나 떨 시간에 임무나 하나 더 보내줘.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=smalltalk_10703_1].dlg
   limit: do 120 znaków
   EN: Oi there! If you’ve got time for silly chinwags, send me on a mission instead.
   PL:
173. [Kwestia głosowa [smalltalk_10703_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=smalltalk_10703_2].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Kwestia głosowa [smalltalk_10703_2] (Chatter #2)] 난 토끼야. 풀이 있는 곳이라면 어디든 가서 전부 해치워 버리지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=smalltalk_10703_2].dlg
   limit: do 120 znaków
   EN: I’m a rabbit. I go anywhere with grass to graze.
   PL:
175. [Kwestia głosowa [smalltalk_10703_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=smalltalk_10703_3].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Kwestia głosowa [smalltalk_10703_3] (Chatter #3)] 토끼가 약하다고 누가 그러지? 굶주린 토끼 떼들을 만나면 무슨 일이 일어나는지, 본 적 있어?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=smalltalk_10703_3].dlg
   limit: do 130 znaków
   EN: Who says rabbits’re weak? Ever seen what happens when you try to fight a horde of starving coneys?
   PL:
177. [Kwestia głosowa [smalltalk_10703_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=smalltalk_10703_4].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Kwestia głosowa [smalltalk_10703_4] (Post-Uptie Chat 1)] 혹시 내가 싸우다가 형씨까지 공격하더라도 너무 원망하지는 마. 토끼의 습성이니까.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=smalltalk_10703_4].dlg
   limit: do 120 znaków
   EN: Don’t get too bitter if I wallop you while I’m fightin’, mate. It’s in the rabbit’s nature.
   PL:
179. [Kwestia głosowa [smalltalk_10703_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=smalltalk_10703_5].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Kwestia głosowa [smalltalk_10703_5] (Post-Uptie Chat 2)] 그 시계 대가리 좀 쓸만한 거 같은데, 같이 토끼 팀이 되어서 뜀박질해 볼 생각은 없어?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=smalltalk_10703_5].dlg
   limit: do 130 znaków
   EN: That clock of yours seems pretty useful, so why don’tcha join the Rabbit Team and hop with me?
   PL:
181. [Kwestia głosowa [neglect_10703_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=neglect_10703_1].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Kwestia głosowa [neglect_10703_1] (Idle)] 그거 알아? 토끼는, 귀도 밝아.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=neglect_10703_1].dlg
   limit: do 120 znaków
   EN: Did you know? A rabbit’s got good ears, too.
   PL:
183. [Kwestia głosowa [gacksung_10703_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=gacksung_10703_1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Kwestia głosowa [gacksung_10703_1] (Uptying)] 그래, 진작 이랬어야지!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=gacksung_10703_1].dlg
   limit: do 120 znaków
   EN: Alright, now that’s what I like to see!
   PL:
185. [Kwestia głosowa [formation_10703_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=formation_10703_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Kwestia głosowa [formation_10703_1] (Deployment)] 자, 풀 뜯을 시간이다.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=formation_10703_1].dlg
   limit: do 120 znaków
   EN: Right, time to graze some grass.
   PL:
187. [Kwestia głosowa [battleentry_10703_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battleentry_10703_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Kwestia głosowa [battleentry_10703_1] (Stage Entry)] 싱싱한 풀이 보이네!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battleentry_10703_1].dlg
   limit: do 120 znaków
   EN: I spy with my eyes a fresh patch of grass!
   PL:
189. [Kwestia głosowa [battle_select_10703_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_select_10703_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Kwestia głosowa [battle_select_10703_1] (Viewed in Battle)] 화끈한 계획이라도 생각난 거야?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_select_10703_1].dlg
   limit: do 120 znaków
   EN: Got some sort of bombastic plan?
   PL:
191. [Kwestia głosowa [battle_endcommand_10703_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_endcommand_10703_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Kwestia głosowa [battle_endcommand_10703_1] (Commencing Attack)] 깡총!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_endcommand_10703_1].dlg
   limit: do 120 znaków
   EN: Hop on!
   PL:
193. [Kwestia głosowa [battle_enemy_break_10703_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_enemy_break_10703_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Kwestia głosowa [battle_enemy_break_10703_1] (Enemy Stagger)] 더 날뛰어보라고!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_enemy_break_10703_1].dlg
   limit: do 120 znaków
   EN: Go on and get wild for me!
   PL:
195. [Kwestia głosowa [battle_break_10703_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_break_10703_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Kwestia głosowa [battle_break_10703_1] (Staggered)] 하…!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_break_10703_1].dlg
   limit: do 120 znaków
   EN: Hah…!
   PL:
197. [Kwestia głosowa [battle_kill_10703_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_kill_10703_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Kwestia głosowa [battle_kill_10703_1] (Enemy Killed)] 후, 씹는 맛이 있는데.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_kill_10703_1].dlg
   limit: do 120 znaków
   EN: Huff, that feels good to chew.
   PL:
199. [Kwestia głosowa [battle_allydead_10703_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_allydead_10703_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Kwestia głosowa [battle_allydead_10703_1] (Ally Death)] 외로웠나? 벌써부터 죽어버리게.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_allydead_10703_1].dlg
   limit: do 120 znaków
   EN: Kicked it already? Were you getting lonely or what.
   PL:
201. [Kwestia głosowa [choice_success_p_10703_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=choice_success_p_10703_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Kwestia głosowa [choice_success_p_10703_1] (Check Passed)] 샐러드 먹는 것만큼 쉽구만.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=choice_success_p_10703_1].dlg
   limit: do 120 znaków
   EN: Easy as salad.
   PL:
203. [Kwestia głosowa [choice_fail_n_10703_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=choice_fail_n_10703_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Kwestia głosowa [choice_fail_n_10703_1] (Check Failed)] 난 시키는 대로 했어. 불만은 상부에 찌르라고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=choice_fail_n_10703_1].dlg
   limit: do 120 znaków
   EN: I was following the orders. You can say your complaints to the high heid yins.
   PL:
205. [Kwestia głosowa [battle_clear_10703_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_clear_10703_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Kwestia głosowa [battle_clear_10703_1] (Victory Cry)] 어때? 끝내주게 강하고 믿을 수 없이 빨랐지?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_clear_10703_1].dlg
   limit: do 120 znaków
   EN: How’s that? Remarkably strong and unbelievably fast, eh?
   PL:
207. [Kwestia głosowa [battle_clear_ex_10703_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_clear_ex_10703_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Kwestia głosowa [battle_clear_ex_10703_1] (Extra Conditions Fulfilled)] 근육이 신나서 날뛰는군. 더 해치울 거 없어? 난 이제 시작인데!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_clear_ex_10703_1].dlg
   limit: do 130 znaków
   EN: My muscles are quivering with excitement. Got anyone else to scuffle? I’m just getting started!
   PL:
209. [Kwestia głosowa [battle_defeat_10703_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_defeat_10703_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Kwestia głosowa [battle_defeat_10703_1] (Defeat Wail)] 쉴 시간 따위 없어. 바로 다시 간다!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_RCorp4_10703.json :: dataList[id=battle_defeat_10703_1].dlg
   limit: do 120 znaków
   EN: No time for rest. We’re going right back in!
   PL:

## [00] N Corp. Kleinhammer — Heathcliff — N사 작은 망치
- ID Tożsamości: `10704` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 1 · HP bazowe: 76 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed

211. [Karta Tożsamości — tytuł] N사\n작은 망치
   źródło: Personalities.json :: dataList[id=10704].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: N Corp.\nKleinhammer
   PL:
212. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10704].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10704].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Karta Tożsamości — opis] 히스클리프의 네번째 인격
   źródło: Personalities.json :: dataList[id=10704].desc
   limit: do 120 znaków
   EN: Heathcliff’s 4th Identity
   PL:
215. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 미숙한 못질
   źródło: Skills.json :: dataList[id=1070401].levelList[level=1].name ; dataList[id=1070401].levelList[level=2].name ; dataList[id=1070401].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Gawky Nailing
   PL:
216. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 1 Bleed
   PL:
217. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL:
218. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 못 1 부여
   źródło: Skills.json :: dataList[id=1070401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1070401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Nails next turn
   PL:
219. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttackTail] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070401].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1070401].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL:
221. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 못 1 부여
   źródło: Skills.json :: dataList[id=1070401].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Nails
   PL:
222. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 정...화!
   źródło: Skills.json :: dataList[id=1070402].levelList[level=1].name ; dataList[id=1070402].levelList[level=2].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 6 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Puri…fy!
   PL:
223. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 정신력 3 회복
   źródło: Skills.json :: dataList[id=1070402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Heal 3 SP
   PL:
224. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 더하기 코인 약화 1 부여
   źródło: Skills.json :: dataList[id=1070402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Plus Coin Drop next turn
   PL:
225. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WinDuel] 정신력 5 회복
   źródło: Skills.json :: dataList[id=1070402].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Heal 5 SP
   PL:
226. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 더하기 코인 약화 2 부여
   źródło: Skills.json :: dataList[id=1070402].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Plus Coin Drop next turn
   PL:
227. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 미약한 단죄
   źródło: Skills.json :: dataList[id=1070403].levelList[level=3].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Infirm Retribution
   PL:
228. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 피해량 10% 만큼 추가 피해
   źródło: Skills.json :: dataList[id=1070403].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Deal bonus damage by 10% of damage dealt
   PL:
229. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 피해량 10% 만큼 추가 피해
   źródło: Skills.json :: dataList[id=1070403].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 피해량 10% 만큼 추가 피해
   źródło: Skills.json :: dataList[id=1070403].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1070404].levelList[level=1].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Guard
   PL:
232. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Envy) — nazwa] 젠장...
   źródło: Passives.json :: dataList[id=1070401].name
   limit: do 40 znaków
   EN: Bugger…
   PL:
233. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Envy) — opis] 아군이 사망하면 다음 턴 시작 시 정신력이 10 감소하고, 타격 위력 증가 1을 얻음
   źródło: Passives.json :: dataList[id=1070401].desc
   limit: do 120 znaków
   EN: When an ally is defeated, lose 10 SP and gain 1 Blunt Power Up next turn.
   PL:
234. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 독경
   źródło: Passives.json :: dataList[id=1070421].name
   limit: do 40 znaków
   EN: Cantillation
   PL:
235. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 속도가 가장 빠른 아군 1명의 못 부여 값 +1
   źródło: Passives.json :: dataList[id=1070421].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed inflicts +1 Nails.
   PL:
236. [Kwestia głosowa [get_10704_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=get_10704_1].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Kwestia głosowa [get_10704_1] (Identity Acquisition)] 넵, 저, 저는… 아, 선배가 아니잖아… 뭐야?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=get_10704_1].dlg
   limit: do 120 znaków
   EN: Right, I—I am… Wait, you’re not the superior… What?
   PL:
238. [Kwestia głosowa [lobby_morning_10704_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=lobby_morning_10704_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [Kwestia głosowa [lobby_morning_10704_1] (Morning Greeting)] 바쁜 시간이야. 말 걸지 마. 아… 책 어딨지?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=lobby_morning_10704_1].dlg
   limit: do 120 znaków
   EN: I’m busy at this time of day. Don’t talk to me. Oh… Where’d I put my book?
   PL:
240. [Kwestia głosowa [lobby_noon_10704_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=lobby_noon_10704_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
241. [Kwestia głosowa [lobby_noon_10704_1] (Afternoon Greeting)] 이단은 정화… 헉. 나 방금 뭐라고 했어? 아… 밥만 먹으면 이러네.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=lobby_noon_10704_1].dlg
   limit: do 120 znaków
   EN: Heretics shall be pur— Gah. What’d I just say? Bugger… This keeps happening after meals.
   PL:
242. [Kwestia głosowa [lobby_night_10704_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=lobby_night_10704_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Kwestia głosowa [lobby_night_10704_1] (Evening Greeting)] 오늘은 제 시간에 잘 수 있을까… 당신은 잘 수 있을 때 자둬.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=lobby_night_10704_1].dlg
   limit: do 120 znaków
   EN: Wonder if I can get to sleep on time tonight… You should sleep while you can.
   PL:
244. [Kwestia głosowa [smalltalk_10704_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=smalltalk_10704_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Kwestia głosowa [smalltalk_10704_1] (Chatter #1)] 자꾸 말 걸지마. 아까 외웠던 교리가 다 빠져나가니까.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=smalltalk_10704_1].dlg
   limit: do 120 znaków
   EN: Enough gabbing at me. I need this passage to stick in my head, and you aren’t helping.
   PL:
246. [Kwestia głosowa [smalltalk_10704_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=smalltalk_10704_2].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Kwestia głosowa [smalltalk_10704_2] (Chatter #2)] 제대로 된 식사 좀 했으면 좋겠어. 매번 물컹한게 담긴 통조림을 뜯는 것도 지겹고…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=smalltalk_10704_2].dlg
   limit: do 120 znaków
   EN: Hope I can get a proper meal someday. I’m sick of opening those cans of mushy stuff…
   PL:
248. [Kwestia głosowa [smalltalk_10704_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=smalltalk_10704_3].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Kwestia głosowa [smalltalk_10704_3] (Chatter #3)] 이단…! 아, 씨… 그딴 가면 좀 두고 다니면 안돼? 헷갈려서 죽일 뻔했잖아!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=smalltalk_10704_3].dlg
   limit: do 120 znaków
   EN: Heret—! Ah, bloody… Won’t you take off that minging mask? I almost killed you!
   PL:
250. [Kwestia głosowa [smalltalk_10704_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=smalltalk_10704_4].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Kwestia głosowa [smalltalk_10704_4] (Post-Uptie Chat 1)] 눈이 퀭하다고…? 아직 못잤거든. 저번에 집회에 5분 늦은 걸로 해가 뜰 때까지 독경을 시켜서 말이야.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=smalltalk_10704_4].dlg
   limit: do 190 znaków
   EN: My eyes look all sunken…? Yeah, I didn’t get my sleep. They made me recite the book all night for being five minutes late to the last gathering.
   PL:
252. [Kwestia głosowa [smalltalk_10704_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=smalltalk_10704_5].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Kwestia głosowa [smalltalk_10704_5] (Post-Uptie Chat 2)] 나는… 망치… 더러운 것을 두드려 정화하는… 쥐여질 자…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=smalltalk_10704_5].dlg
   limit: do 120 znaków
   EN: I am… a hammer… He who shall be gripped… to pound the filth away…
   PL:
254. [Kwestia głosowa [neglect_10704_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=neglect_10704_1].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Kwestia głosowa [neglect_10704_1] (Idle)] …아무도 없나? 잠깐… 쉬어도 되겠지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=neglect_10704_1].dlg
   limit: do 120 znaków
   EN: …No one around? Guess a… short break can’t hurt.
   PL:
256. [Kwestia głosowa [gacksung_10704_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=gacksung_10704_1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Kwestia głosowa [gacksung_10704_1] (Uptying)] 내가…? 아니, 나는 자격이 안되는 것 같은데… 뜻이 그렇다면 따라야겠지만.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=gacksung_10704_1].dlg
   limit: do 120 znaków
   EN: Me…? No, don’t think I deserve to get all this… Not like I can refuse if you mean it.
   PL:
258. [Kwestia głosowa [formation_10704_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=formation_10704_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Kwestia głosowa [formation_10704_1] (Deployment)] 넵! 아… 그래.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=formation_10704_1].dlg
   limit: do 120 znaków
   EN: Aye! Oh… Right.
   PL:
260. [Kwestia głosowa [battleentry_10704_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battleentry_10704_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Kwestia głosowa [battleentry_10704_1] (Stage Entry)] 하… 시간됐네.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battleentry_10704_1].dlg
   limit: do 120 znaków
   EN: Haaa… It’s time.
   PL:
262. [Kwestia głosowa [battle_select_10704_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_select_10704_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Kwestia głosowa [battle_select_10704_1] (Viewed in Battle)] 또, 무슨…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_select_10704_1].dlg
   limit: do 120 znaków
   EN: What is it now…
   PL:
264. [Kwestia głosowa [battle_endcommand_10704_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_endcommand_10704_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Kwestia głosowa [battle_endcommand_10704_1] (Commencing Attack)] 정화. 하라…였나?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_endcommand_10704_1].dlg
   limit: do 120 znaków
   EN: “Puri…fy.” Was that how it goes?
   PL:
266. [Kwestia głosowa [battle_enemy_break_10704_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_enemy_break_10704_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Kwestia głosowa [battle_enemy_break_10704_1] (Enemy Stagger)] 이단을 배제…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_enemy_break_10704_1].dlg
   limit: do 120 znaków
   EN: Eliminate the heretic…
   PL:
268. [Kwestia głosowa [battle_break_10704_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_break_10704_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Kwestia głosowa [battle_break_10704_1] (Staggered)] …헉! 여긴…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_break_10704_1].dlg
   limit: do 120 znaków
   EN: …Gah! Where am…
   PL:
270. [Kwestia głosowa [battle_kill_10704_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_kill_10704_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Kwestia głosowa [battle_kill_10704_1] (Enemy Killed)] …또 죽었나.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_kill_10704_1].dlg
   limit: do 120 znaków
   EN: …Another one goes.
   PL:
272. [Kwestia głosowa [battle_dead_10704_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_dead_10704_1].desc
   limit: do 120 znaków
   EN: Death
   PL:
273. [Kwestia głosowa [battle_dead_10704_1] (Death)] 젠장… 캐서린…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_dead_10704_1].dlg
   limit: do 120 znaków
   EN: Dammit… Catherine…
   PL:
274. [Kwestia głosowa [choice_success_p_10704_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=choice_success_p_10704_2].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Kwestia głosowa [choice_success_p_10704_2] (Check Passed)] 시키는 대로 했어.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=choice_success_p_10704_2].dlg
   limit: do 120 znaków
   EN: I did as I was told.
   PL:
276. [Kwestia głosowa [choice_fail_n_10704_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=choice_fail_n_10704_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Kwestia głosowa [choice_fail_n_10704_1] (Check Failed)] 시키는 대로 했는데…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=choice_fail_n_10704_1].dlg
   limit: do 120 znaków
   EN: I did as I was told, yet…
   PL:
278. [Kwestia głosowa [battle_clear_10704_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_clear_10704_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Kwestia głosowa [battle_clear_10704_1] (Victory Cry)] 이제… 돌아가는 건가?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_clear_10704_1].dlg
   limit: do 120 znaków
   EN: Are we… heading back now?
   PL:
280. [Kwestia głosowa [battle_clear_ex_10704_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_clear_ex_10704_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Kwestia głosowa [battle_clear_ex_10704_1] (Extra Conditions Fulfilled)] 이 정도면… 언젠가 돌아갈 수 있는 거겠지?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_clear_ex_10704_1].dlg
   limit: do 120 znaków
   EN: If I keep up… I’ll be able to go back one day, right?
   PL:
282. [Kwestia głosowa [battle_defeat_10704_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_defeat_10704_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Kwestia głosowa [battle_defeat_10704_1] (Defeat Wail)] 아, 안돼! 이, 이대로 돌아가면… 으윽!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Ncorp_10704.json :: dataList[id=battle_defeat_10704_1].dlg
   limit: do 120 znaków
   EN: No, it can’t! I—If I head back like this… Nrgh!
   PL:

## [000] Lobotomy E.G.O:: Sunshower — Heathcliff — 로보토미 E.G.O:: 여우비
- ID Tożsamości: `10705` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 2 · HP bazowe: 86 · szybkość: 2–4 / 2–5 / 3–5 / 3–5
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Sinking, Rupture

284. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n여우비
   źródło: Personalities.json :: dataList[id=10705].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::\nSunshower
   PL:
285. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10705].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10705].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Karta Tożsamości — opis] 히스클리프의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10705].desc
   limit: do 120 znaków
   EN: Heathcliff’s 5th Identity
   PL:
288. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 우산후리기
   źródło: Skills.json :: dataList[id=1070501].levelList[level=1].name ; dataList[id=1070501].levelList[level=2].name ; dataList[id=1070501].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 6 · monety: 3 (−2)
   limit: do 40 znaków
   EN: Umbrella Thwack
   PL:
289. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1070501].levelList[level=1].desc ; dataList[id=1070501].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Gain +1 [Sinking] Count
   PL:
290. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1070501].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL:
291. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackTail] 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1070501].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Sinking]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackTail] Inflict +1 [Sinking] Count
   PL:
292. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1070501].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1070501].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL:
293. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttackTail] 침잠 횟수 2 증가
   źródło: Skills.json :: dataList[id=1070501].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1070501].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Sinking]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackTail] Inflict +2 [Sinking] Count
   PL:
294. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 침잠 횟수 1 증가\n[DefeatDuel] 침잠 3 얻음
   źródło: Skills.json :: dataList[id=1070501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Gain +1 [Sinking] Count\n[DefeatDuel] Gain 3 [Sinking]
   PL:
295. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 진창다지기
   źródło: Skills.json :: dataList[id=1070502].levelList[level=1].name ; dataList[id=1070502].levelList[level=2].name ; dataList[id=1070502].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 10 · monety: 4 (−3)
   limit: do 40 znaków
   EN: Puddle Stomp
   PL:
296. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [WhenUse] 자신의 정신력이 -15 미만일 때 최종 위력 +2
   źródło: Skills.json :: dataList[id=1070502].levelList[level=1].desc ; dataList[id=1070502].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] When below -15 SP, Final Power +2
   PL:
297. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackTail] 파열 2 부여
   źródło: Skills.json :: dataList[id=1070502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 2 Rupture
   PL:
298. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackTail] 파열 2 부여
   źródło: Skills.json :: dataList[id=1070502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttackTail] 진동 폭발
   źródło: Skills.json :: dataList[id=1070502].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttackTail] Trigger [VibrationExplosion]
   PL:
300. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackTail] 파열 3 부여
   źródło: Skills.json :: dataList[id=1070502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 3 Rupture
   PL:
301. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttackTail] 파열 3 부여
   źródło: Skills.json :: dataList[id=1070502].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1070502].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 300 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 4, efekt 1 — opis] 자신의 침잠 5를 소모하여 피해량 +20%
   źródło: Skills.json :: dataList[id=1070502].levelList[level=2].coinlist[#3].coindescs[#0].desc ; dataList[id=1070502].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Spend 5 [Sinking] to deal +20% damage
   PL:
303. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 4, efekt 2 — opis] [OnSucceedAttackTail] 진동 폭발
   źródło: Skills.json :: dataList[id=1070502].levelList[level=2].coinlist[#3].coindescs[#1].desc ; dataList[id=1070502].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 299 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 정신력이 -15 미만일 때 최종 위력 +3\n[WhenUse] 자신의 정신력이 -25 미만일 때 최종 위력 +2
   źródło: Skills.json :: dataList[id=1070502].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] When below -15 SP, Final Power +3\n[WhenUse] When below -25 SP, Final Power +2
   PL:
305. [Umiejętność 3 (×1) (ulepszenie 1) — nazwa] 퍼져라!
   źródło: Skills.json :: dataList[id=1070503].levelList[level=1].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 18 · monety: 3 (−7)
   limit: do 40 znaków
   EN: Spread Out!
   PL:
306. [Umiejętność 3 (×1) (ulepszenie 1) — opis] [WhenUse] 침잠 6을 얻고, 자신의 침잠 횟수 3 증가
   źródło: Skills.json :: dataList[id=1070503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Gain 6 [Sinking] and +3 [Sinking] Count
   PL:
307. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 다음 턴에 마비 1 부여
   źródło: Skills.json :: dataList[id=1070503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 1 Paralyze next turn
   PL:
308. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills.json :: dataList[id=1070503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Rupture
   PL:
309. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackTail] 다음 턴에 취약 1 부여
   źródło: Skills.json :: dataList[id=1070503].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 1 Fragile next turn
   PL:
310. [Obrona (ulepszenia 1,4) — nazwa] 경고
   źródło: Skills.json :: dataList[id=1070504].levelList[level=1].name ; dataList[id=1070504].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 10 · monety: 2 (−5)
   limit: do 40 znaków
   EN: Warning
   PL:
311. [Obrona (ulepszenie 1) — opis] [WhenUse] 침잠 3 얻음
   źródło: Skills.json :: dataList[id=1070504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Gain 3 [Sinking]
   PL:
312. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 다음 턴에 마비 1을 얻음
   źródło: Skills.json :: dataList[id=1070504].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1070504].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Gain 1 Paralyze next turn
   PL:
313. [Obrona (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 5 부여
   źródło: Skills.json :: dataList[id=1070504].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1070504].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking]
   PL:
314. [Obrona (ulepszenia 1,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills.json :: dataList[id=1070504].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1070504].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 308 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Obrona (ulepszenie 4) — opis] [WhenUse] 침잠 5 얻음
   źródło: Skills.json :: dataList[id=1070504].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Gain 5 [Sinking]
   PL:
316. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 눈물비
   źródło: Passives.json :: dataList[id=1070501].name
   limit: do 40 znaków
   EN: Rain of Tears
   PL:
317. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 전투 시작 시 침잠 횟수를 1 소모하여 침잠 만큼 정신력 감소\n피격 전 자신의 침잠 만큼 보호를 얻음.(턴 당 획득 가능한 보호 : 최대 5)\n피격 시 다음 턴에 타격 피해량 증가 1을 얻음 (턴 당 최대 3)
   źródło: Passives.json :: dataList[id=1070501].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the combat phase, spend 1 Sinking Count and lose SP by the current amount of Sinking.\nBefore being hit by an attack, gain Protection equal to this unit's Sinking. (Up to 5 Protection can be gained per turn)\nWhen hit, gain 1 Blunt DMG Up next turn. (3 per turn)
   PL:
318. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — nazwa] 해진 우산
   źródło: Passives.json :: dataList[id=1070521].name
   limit: do 40 znaków
   EN: Ragged Umbrella
   PL:
319. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — opis] 정신력이 가장 낮은 아군 1명이 피격 시 정신력 10 감소하고, 다음 턴에 타격 피해량 증가 1을 얻음 (턴 당 1회 발동)
   źródło: Passives.json :: dataList[id=1070521].desc
   limit: do 150 znaków
   EN: 1 ally with the least SP loses 10 SP when hit by an attack and gains 1 Blunt DMG Up next turn. (Once per turn)
   PL:
320. [Kwestia głosowa [get_10705_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=get_10705_1].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Kwestia głosowa [get_10705_1] (Identity Acquisition)] …저리 가라. 괜히 와서 들쑤시지 마.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=get_10705_1].dlg
   limit: do 120 znaków
   EN: ...Go away. Don't bother poking at me.
   PL:
322. [Kwestia głosowa [lobby_morning_10705_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=lobby_morning_10705_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Kwestia głosowa [lobby_morning_10705_1] (Morning Greeting)] 해가 안 나니까 도통 시간을 모르겠네… 야, 지금 아침이냐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=lobby_morning_10705_1].dlg
   limit: do 120 znaków
   EN: I can't tell what time it is if the sun doesn't get in... Oi, is it morning now?
   PL:
324. [Kwestia głosowa [lobby_noon_10705_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=lobby_noon_10705_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Kwestia głosowa [lobby_noon_10705_1] (Afternoon Greeting)] 이 옷을 입고 잠에 들었다 깨면… 지금처럼 쓰레기 가득한 골목 구석이더군. 나랑 닮은 곳이지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=lobby_noon_10705_1].dlg
   limit: do 190 znaków
   EN: When I wake up after falling asleep in these clothes... I find myself in garbage-filled alleyways like here. It's a place that's just like me.
   PL:
326. [Kwestia głosowa [lobby_night_10705_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=lobby_night_10705_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Kwestia głosowa [lobby_night_10705_1] (Evening Greeting)] 일찍 자는게 좋아. 너무 늦으면… 잠들기 힘들 정도로 추워질 때도 있더라고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=lobby_night_10705_1].dlg
   limit: do 130 znaków
   EN: You'd better sleep early. If it gets too late... it sometimes becomes too cold to fall asleep.
   PL:
328. [Kwestia głosowa [smalltalk_10705_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=smalltalk_10705_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Kwestia głosowa [smalltalk_10705_1] (Chatter #1)] 자꾸 거슬리게 앞에서 돌아다니지 마라… 이 버려진 우산으로 너 하나 정도는 때려눕힐 수 있어.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=smalltalk_10705_1].dlg
   limit: do 150 znaków
   EN: Don't loiter before my eyes like that, you're being a nuisance... I can beat you down with this old umbrella.
   PL:
330. [Kwestia głosowa [smalltalk_10705_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=smalltalk_10705_2].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Kwestia głosowa [smalltalk_10705_2] (Chatter #2)] …이름? 안 지어 줬어. 이 녀석도 언제 나를 떠날 지 모르잖아.\n…눈 그 따위로 뜨지마라.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=smalltalk_10705_2].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ...Name? Didn't give one. It might leave my side whenever.\n...Don't give me that glance.
   PL:
332. [Kwestia głosowa [smalltalk_10705_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=smalltalk_10705_3].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [Kwestia głosowa [smalltalk_10705_3] (Chatter #3)] 뒷골목에 으슥한 곳이야 얼마든지 있지만… 여기는 그 중에서도 제일 마음이 안정 되는 곳이야.\n아무도 지나다니지 않고, 아무도 관심을 주지 않으니까.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=smalltalk_10705_3].dlg
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Plenty of dark corners in the Backstreets... This one lets me relax the most.\nNo one walks by, and no one gives me attention.
   PL:
334. [Kwestia głosowa [smalltalk_10705_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=smalltalk_10705_4].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Kwestia głosowa [smalltalk_10705_4] (Post-Uptie Chat 1)] 꼴값떨지마. 나는 세상에 있는 모든 기술들을 내 손으로 전부 부숴버릴 거야.\n…거기서 네가 방해 된다면, 망설임 없이 찔러버릴 거고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=smalltalk_10705_4].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Don't act all cocky. I'll destroy every technology in the world with my hands.\n...If you get in my way, I'll stab you then and there.
   PL:
336. [Kwestia głosowa [smalltalk_10705_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=smalltalk_10705_5].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Kwestia głosowa [smalltalk_10705_5] (Post-Uptie Chat 2)] 우산은 편리하지…\n너한테도 일말의 기대는 없어. 그냥… 한 번 해봐. 버려서 헤진 우산살에 꽂히면 얼마나 아픈지 겪게 해줄테니까.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=smalltalk_10705_5].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Umbrellas are handy...\nI'm not expecting anything from you. Just… go on and try it. I’ll show you how much it hurts to have ragged broken ribs from a dumped umbrella jammed in you.
   PL:
338. [Kwestia głosowa [neglect_10705_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=neglect_10705_1].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Kwestia głosowa [neglect_10705_1] (Idle)] 흥. 이제 다 갖고 놀았냐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=neglect_10705_1].dlg
   limit: do 120 znaków
   EN: Hmph. Done playing around with me?
   PL:
340. [Kwestia głosowa [gacksung_10705_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=gacksung_10705_1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Kwestia głosowa [gacksung_10705_1] (Uptying)] 네가 이렇게 친절을 베푸는 척 해도… 난 모든 기술이 해방되는 그 순간까지, 널 경계하고 의심할 거야.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=gacksung_10705_1].dlg
   limit: do 150 znaków
   EN: Go on and pretend to be nice all you want... I'll stay wary and suspicious of you until all technology is liberated.
   PL:
342. [Kwestia głosowa [formation_10705_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=formation_10705_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Kwestia głosowa [formation_10705_1] (Deployment)] …해방된 세상을 위해서라면.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=formation_10705_1].dlg
   limit: do 120 znaków
   EN: ...For a free world.
   PL:
344. [Kwestia głosowa [battleentry_10705_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battleentry_10705_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Kwestia głosowa [battleentry_10705_1] (Stage Entry)] 아주 뭉개버려주지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battleentry_10705_1].dlg
   limit: do 120 znaków
   EN: I'll crush 'em alright.
   PL:
346. [Kwestia głosowa [battle_select_10705_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_select_10705_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [Kwestia głosowa [battle_select_10705_1] (Viewed in Battle)] …뭐야?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_select_10705_1].dlg
   limit: do 120 znaków
   EN: ...What?
   PL:
348. [Kwestia głosowa [battle_endcommand_10705_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_endcommand_10705_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [Kwestia głosowa [battle_endcommand_10705_1] (Commencing Attack)] 먼지 나게 패주지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_endcommand_10705_1].dlg
   limit: do 120 znaków
   EN: I'll beat you to a pulp.
   PL:
350. [Kwestia głosowa [battle_enemy_break_10705_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_enemy_break_10705_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Kwestia głosowa [battle_enemy_break_10705_1] (Enemy Stagger)] 하핫, 미끄러지는 꼴 좀 보라지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_enemy_break_10705_1].dlg
   limit: do 120 znaków
   EN: Haha, look at 'em slip.
   PL:
352. [Kwestia głosowa [battle_break_10705_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_break_10705_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Kwestia głosowa [battle_break_10705_1] (Staggered)] 젠장!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_break_10705_1].dlg
   limit: do 120 znaków
   EN: Dammit!
   PL:
354. [Kwestia głosowa [battle_kill_10705_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_kill_10705_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Kwestia głosowa [battle_kill_10705_1] (Enemy Killed)] 너도 걸레짝이 되어버렸군.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_kill_10705_1].dlg
   limit: do 120 znaków
   EN: All messed up, eh.
   PL:
356. [Kwestia głosowa [battle_dead_10705_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_dead_10705_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [Kwestia głosowa [battle_dead_10705_1] (Death)] 아직 아니야… 내게는 할 일이…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_dead_10705_1].dlg
   limit: do 120 znaków
   EN: Not yet... I've still got things to do...
   PL:
358. [Kwestia głosowa [choice_success_p_10705_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=choice_success_p_10705_2].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Kwestia głosowa [choice_success_p_10705_2] (Check Passed)] 뭐, 간단했잖아?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=choice_success_p_10705_2].dlg
   limit: do 120 znaków
   EN: Well, it was simple, eh?
   PL:
360. [Kwestia głosowa [choice_fail_n_10705_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=choice_fail_n_10705_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Kwestia głosowa [choice_fail_n_10705_1] (Check Failed)] 일부러 그런 건 아니야. 알지?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=choice_fail_n_10705_1].dlg
   limit: do 120 znaków
   EN: I didn't do that on purpose. You know that, right?
   PL:
362. [Kwestia głosowa [battle_clear_10705_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_clear_10705_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Kwestia głosowa [battle_clear_10705_1] (Victory Cry)] 버려진 것들을 위해서…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_clear_10705_1].dlg
   limit: do 120 znaków
   EN: For the abandoned...
   PL:
364. [Kwestia głosowa [battle_clear_ex_10705_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_clear_ex_10705_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
365. [Kwestia głosowa [battle_clear_ex_10705_1] (Extra Conditions Fulfilled)] 하~ 힘 좀 더 써봤어.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_clear_ex_10705_1].dlg
   limit: do 120 znaków
   EN: Haah~ I tried a bit harder.
   PL:
366. [Kwestia głosowa [battle_defeat_10705_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_defeat_10705_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Kwestia głosowa [battle_defeat_10705_1] (Defeat Wail)] 쯧… 또 실패했어. 버릴 거냐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_LEGO_10705.json :: dataList[id=battle_defeat_10705_1].dlg
   limit: do 120 znaków
   EN: Tch... Failed again. You gonna throw me away?
   PL:

## [00] Seven Assoc. South Section 4 — Heathcliff — 남부 세븐 협회 4과
- ID Tożsamości: `10706` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 76 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Rupture

368. [Karta Tożsamości — tytuł] 남부 세븐 협회\n4과
   źródło: Personalities.json :: dataList[id=10706].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Seven Assoc.\nSouth Section 4
   PL:
369. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10706].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10706].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Karta Tożsamości — opis] 히스클리프의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10706].desc
   limit: do 120 znaków
   EN: Heathcliff’s 6th Identity
   PL:
372. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 직감
   źródło: Skills.json :: dataList[id=1070601].levelList[level=1].name ; dataList[id=1070601].levelList[level=2].name ; dataList[id=1070601].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Intuition
   PL:
373. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Rupture
   PL:
374. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1070601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>이 6  이상일 때 코인 위력 +1
   źródło: Skills.json :: dataList[id=1070601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>
   EN: If target has 6+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u>, Coin Power +1
   PL:
378. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070601].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070601].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 뒷수습
   źródło: Skills.json :: dataList[id=1070602].levelList[level=1].name ; dataList[id=1070602].levelList[level=2].name ; dataList[id=1070602].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 6 · monety: 1 (+10)
   limit: do 40 znaków
   EN: The Wrap-up
   PL:
381. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1070602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Rupture Count
   PL:
382. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WinDuel] 파열 횟수 1 증가
   źródło: Skills.json :: dataList[id=1070602].levelList[level=2].desc ; dataList[id=1070602].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Inflict +1 Rupture Count
   PL:
383. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 감소 1 부여
   źródło: Skills.json :: dataList[id=1070602].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Defense Level Down next turn
   PL:
384. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1070602].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1070602].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 감소 3 부여
   źródło: Skills.json :: dataList[id=1070602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Defense Level Down next turn
   PL:
386. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 현장 자료 분석
   źródło: Skills.json :: dataList[id=1070603].levelList[level=3].name ; dataList[id=1070603].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Forensics
   PL:
387. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills.json :: dataList[id=1070603].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1070603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Rupture Count
   PL:
388. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070603].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1070603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070603].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1070603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070603].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1070603].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [EnemyKill] 현재 파열 횟수가 가장 낮은 적 1명의 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1070603].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1070603].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Inflict +2 Rupture Count against the enemy that has the least Rupture Count
   PL:
392. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>이 6 이상일 때 코인 위력 +1
   źródło: Skills.json :: dataList[id=1070603].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>
   EN: If target has 6+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u>, Coin Power +1
   PL:
393. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1070604].levelList[level=1].name
   kontekst: grzech: Wrath · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — nazwa] 본능적 간파
   źródło: Passives.json :: dataList[id=1070601].name
   limit: do 40 znaków
   EN: Instinctive Read
   PL:
395. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — opis] 상대의 취약 속성(내성 1.5 초과) 으로 공격 시 스킬로 부여하는 파열 부여 값 +1
   źródło: Passives.json :: dataList[id=1070601].desc
   limit: do 170 znaków
   EN: When attacking a target with a damage type the target is "Fatal" (Resistance>x1.5) to, inflict +1 more Rupture with Skill effects
   PL:
396. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — podsumowanie] 취약 속성으로 공격 시 파열 부여 값 +1
   źródło: Passives.json :: dataList[id=1070601].summary
   limit: do 120 znaków
   EN: When attacking a target with a damage type the target is Fatal to, inflict +1 more Rupture
   PL:
397. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 본능적 간파
   źródło: Passives.json :: dataList[id=1070611].name
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — opis] 상대의 취약 속성(내성 1.5 초과) 으로 공격 시 스킬로 부여하는 파열 부여 값 +1\n<style="highlight">전투 시작 시 생존한 아군 세븐 협회 해결사가 자신 포함 4명 이상 있으면, 위 효과의 파열 부여 값 +1</style>
   źródło: Passives.json :: dataList[id=1070611].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n
   EN: When attacking a target with a damage type the target is "Fatal" (Resistance>x1.5) to, inflict +1 more Rupture with Skill effects\n<style="highlight">If 4 or more surviving units, including this unit, are Seven Association Fixers, additional +1 more Rupture</style>
   PL:
399. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — podsumowanie] 취약 속성으로 공격 시 파열 부여 값 +1\n아군 세븐 협회 해결사가 4명 이상이면, 추가로 +1
   źródło: Passives.json :: dataList[id=1070611].summary
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When attacking a target with a damage type the target is Fatal to, inflict +1 more Rupture\nWith 4 or more Seven Association Fixer allies, additional +1 more Rupture
   PL:
400. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 단서 연결
   źródło: Passives.json :: dataList[id=1070621].name
   limit: do 40 znaków
   EN: Connect The Dots
   PL:
401. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 최대 체력이 가장 많은 아군 1명이 상대의 취약 속성(내성 1.5 초과)으로 공격 시 스킬로 부여하는 파열 부여 값 +1
   źródło: Passives.json :: dataList[id=1070621].desc
   limit: do 220 znaków
   EN: 1 ally that has the highest Max HP inflicts +1 more Rupture with Skill effects when attacking a target with a damage type that the target is "Fatal"(Resistance>x1.5) to
   PL:
402. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — podsumowanie] 최대 체력이 가장 많은 아군 1명이 취약 속성으로 공격 시 파열 부여 값 +1
   źródło: Passives.json :: dataList[id=1070621].summary
   limit: do 150 znaków
   EN: 1 ally that has the highest Max HP inflicts +1 more Rupture when attacking with a damage type the target is Fatal to
   PL:
403. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 단서 연결
   źródło: Passives.json :: dataList[id=1070631].name
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Glut.) — opis] 최대 체력이 가장 많은 아군 1명이 상대의 취약 속성(내성 1.5 초과)으로 공격 시 스킬로 부여하는 파열 부여 값 +1\n<style="highlight">효과를 적용받은 대상이 세븐 협회 해결사면, 위 효과의 파열 부여 값 +1</style>
   źródło: Passives.json :: dataList[id=1070631].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n
   EN: 1 ally that has the highest Max HP inflicts +1 more Rupture with Skill effects when attacking a target with a damage type that the target is "Fatal"(Resistance>x1.5) to\n<style="highlight">If the ally is a Seven Association Fixer, additional +1 more Rupture</style>
   PL:
405. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Glut.) — podsumowanie] 최대 체력이 가장 많은 아군 1명이 취약 속성으로 공격 시 파열 부여 값 +1\n대상이 세븐 협회 해결사면, 추가로 +1
   źródło: Passives.json :: dataList[id=1070631].summary
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 1 ally that has the highest Max HP inflicts +1 more Rupture when attacking with a damage type the target is Fatal to\nIf the ally is a Seven Association Fixer, additional +1 more Rupture
   PL:
406. [Kwestia głosowa [get_10706_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=get_10706_1].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Kwestia głosowa [get_10706_1] (Identity Acquisition)] 현장 자료들을 볼 때 이번 사건에 대한 결론은… 아, 생각했었는데! 기다려봐.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=get_10706_1].dlg
   limit: do 150 znaków
   EN: All evidence points to the conclusion that this case was... Agh, bloody hell, I almost had it! Wait a moment.
   PL:
408. [Kwestia głosowa [lobby_morning_10706_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=lobby_morning_10706_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Kwestia głosowa [lobby_morning_10706_1] (Morning Greeting)] 아침부터 거치적거리지 마라. 한창 머리 돌리고 있어서 예민하니까.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=lobby_morning_10706_1].dlg
   limit: do 150 znaków
   EN: Don't disturb me this morning. I'm trying to wrap my head around this case, and I don't want any disruptions.
   PL:
410. [Kwestia głosowa [lobby_noon_10706_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=lobby_noon_10706_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Kwestia głosowa [lobby_noon_10706_1] (Afternoon Greeting)] 차… 아니, 점심이니까 마시고 싶긴 한데. 당연히… 하, 지금은 거기 가기 좀 그래. 자꾸 결론이 늦어져서 눈치 보인다고.\n카운터 너머에서 쏘아볼 눈을 생각하면… 으.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=lobby_noon_10706_1].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Tea...? Well, it's midday, so I wouldn't mind a cuppa, but... Haah, it's a bit awkward to go there at the moment. I'm long overdue for the conclusion of this case, and I don't want the cafeteria lass givin' me the glares over the counter.
   PL:
412. [Kwestia głosowa [lobby_night_10706_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=lobby_night_10706_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Kwestia głosowa [lobby_night_10706_1] (Evening Greeting)] 야근을 내가 하고 싶어서 하겠냐. 그냥… 이걸 지금 끝맺어 놓지 않으면 잠이 안온다고. 신경 쓰이는게 너무 많으니까.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=lobby_night_10706_1].dlg
   limit: do 220 znaków
   EN: I'm not here because I want to be here. It's just... I can't get a wink of sleep before this case is wrapped up. Otherwise, it'll nag at the back of my mind all night.
   PL:
414. [Kwestia głosowa [smalltalk_10706_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=smalltalk_10706_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Kwestia głosowa [smalltalk_10706_1] (Chatter #1)] 프로파일러 같은 거창한 말로 부르지 마라… 내가 하는 건 그리 대단한 것도 아냐. 그냥 이런 저런 흔적들을 보고 직감으로 추측하는 것 뿐이지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=smalltalk_10706_1].dlg
   limit: do 180 znaków
   EN: Don't call me a profiler or some other grand title. I'm doing nothing fancy... I just make conjectures based on junk I find here and there.
   PL:
416. [Kwestia głosowa [smalltalk_10706_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=smalltalk_10706_2].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Kwestia głosowa [smalltalk_10706_2] (Chatter #2)] 하… 완벽한 확신이 있는 건 아니지만… 이 새끼 굴러먹던 거 생각하면 무조건 이 놈들이 노릴거라고.\n…아, 방금 새끼라고 한 건 고객님한테 한 말 아니다? 아무튼 아니라고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=smalltalk_10706_2].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Haah... Can't say I'm absolutely certain, but look at his records. I reckon this wanker's already got a target on his back.\nUh, did I just—no, no. I didn't just refer to our client as 'this wanker'. Shut up, I didn't.
   PL:
418. [Kwestia głosowa [smalltalk_10706_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=smalltalk_10706_3].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Kwestia głosowa [smalltalk_10706_3] (Chatter #3)] 쯧. 사건에 대한 결론을 내놓는 것 보다 그걸 글로 만들어 내는게 더 어렵단 말이지.\n내가 생각하는 걸 떠들면 깔끔하게 문장으로 만들어주는 놈이 있음 좋겠는데.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=smalltalk_10706_3].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Tsk. You know what's harder than drawing conclusions about a case? Writing the follow—up report.\nIf only some bloke could organize my thoughts into a neat report as I narrate them.
   PL:
420. [Kwestia głosowa [smalltalk_10706_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=smalltalk_10706_4].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Kwestia głosowa [smalltalk_10706_4] (Post-Uptie Chat 1)] 뒷처리… 아니, 사후 처리에 대한 의뢰는 역시 우리 쪽에 맡기는게 좋네. 내 추측이 정말 맞았는지 확인도 할 수 있고…\n감정이입 했던 만큼 저 놈들을 쳐죽여줄 수도 있고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=smalltalk_10706_4].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I think we're pretty good at this shi—I mean, post—contract management. I can also confirm if my predictions were right...\nBesides, I get to smash some heads. I got pretty invested in the case over the course of this investigation, you know.
   PL:
422. [Kwestia głosowa [smalltalk_10706_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=smalltalk_10706_5].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Kwestia głosowa [smalltalk_10706_5] (Post-Uptie Chat 2)] 이런 것들 처리하는 일이 당연히 훨씬 쉽지. 머리 쓸 일도 없잖아. 뭐… 그렇다고 사건 분석하는게 싫은 건 아니고. 나름 재밌어. 이것도.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=smalltalk_10706_5].dlg
   limit: do 210 znaków
   EN: Of course, taking care of these idiots is a much easier job. I don't even need to use my brain. Well... not that I dislike case analyses. That's got its own charms.
   PL:
424. [Kwestia głosowa [neglect_10706_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=neglect_10706_1].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Kwestia głosowa [neglect_10706_1] (Idle)] 그러니까… 그게 그렇게 되어서… 하, 이 새끼들 봐라?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=neglect_10706_1].dlg
   limit: do 120 znaków
   EN: So... that's how it— Haah, would you look at that.
   PL:
426. [Kwestia głosowa [gacksung_10706_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=gacksung_10706_1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Kwestia głosowa [gacksung_10706_1] (Uptying)] 아. 어. 잠깐만. 지금 단서가 막 이어지려고 해. …그게 그래서 그런거였나… 이따 얘기해. 어.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=gacksung_10706_1].dlg
   limit: do 190 znaków
   EN: Ah. Uh—huh. Hold that thought. I'm starting to connect the dots. ...Ahh, so that's how that happened... Right. We'll chat later. Uh—huh, cheers.
   PL:
428. [Kwestia głosowa [formation_10706_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=formation_10706_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Kwestia głosowa [formation_10706_1] (Deployment)] 사후 처리로구만.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=formation_10706_1].dlg
   limit: do 120 znaków
   EN: A post—contract management, is it?
   PL:
430. [Kwestia głosowa [battleentry_10706_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battleentry_10706_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Kwestia głosowa [battleentry_10706_1] (Stage Entry)] 사건을 끝내러 가볼까?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battleentry_10706_1].dlg
   limit: do 120 znaków
   EN: Let's go solve this case, yeah?
   PL:
432. [Kwestia głosowa [battle_select_10706_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_select_10706_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Kwestia głosowa [battle_select_10706_1] (Viewed in Battle)] 어? 왜. 이 놈이 아냐? 그럴리 없는데.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_select_10706_1].dlg
   limit: do 120 znaków
   EN: Huh? What. It's not him? No way.
   PL:
434. [Kwestia głosowa [battle_endcommand_10706_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_endcommand_10706_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Kwestia głosowa [battle_endcommand_10706_1] (Commencing Attack)] 너냐?!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_endcommand_10706_1].dlg
   limit: do 120 znaków
   EN: Is it you?!
   PL:
436. [Kwestia głosowa [battle_enemy_break_10706_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_enemy_break_10706_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Kwestia głosowa [battle_enemy_break_10706_1] (Enemy Stagger)] 휘청거리기는.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_enemy_break_10706_1].dlg
   limit: do 120 znaków
   EN: Reeling, are you?
   PL:
438. [Kwestia głosowa [battle_break_10706_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_break_10706_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Kwestia głosowa [battle_break_10706_1] (Staggered)] 큭…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_break_10706_1].dlg
   limit: do 120 znaków
   EN: Kah...
   PL:
440. [Kwestia głosowa [battle_kill_10706_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_kill_10706_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Kwestia głosowa [battle_kill_10706_1] (Enemy Killed)] 그래, 얘는 처리했고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_kill_10706_1].dlg
   limit: do 120 znaków
   EN: Right, so that one's taken care of.
   PL:
442. [Kwestia głosowa [battle_dead_10706_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_dead_10706_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Kwestia głosowa [battle_dead_10706_1] (Death)] 아… 이상한… 데. 이런 패턴일… 리가.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_dead_10706_1].dlg
   limit: do 120 znaków
   EN: Ah... That's... odd. That deviates... from the patterns.
   PL:
444. [Kwestia głosowa [choice_success_p_10706_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=choice_success_p_10706_2].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Kwestia głosowa [choice_success_p_10706_2] (Check Passed)] 흥, 이런 걸 줄 알았지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=choice_success_p_10706_2].dlg
   limit: do 120 znaków
   EN: Hmph, I knew it.
   PL:
446. [Kwestia głosowa [choice_fail_n_10706_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=choice_fail_n_10706_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Kwestia głosowa [choice_fail_n_10706_1] (Check Failed)] 아니라고…? 그럴리가, 내 감으로는…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=choice_fail_n_10706_1].dlg
   limit: do 120 znaków
   EN: It's not? No way. But my hunch...
   PL:
448. [Kwestia głosowa [battle_clear_10706_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_clear_10706_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Kwestia głosowa [battle_clear_10706_1] (Victory Cry)] 결국 이번에도 내 삘이 맞았지? 나도 쓸만한 머리다, 이거야!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_clear_10706_1].dlg
   limit: do 120 znaków
   EN: I was right on the money in the end, weren't I? I'm no nitwit, I'll have you know!
   PL:
450. [Kwestia głosowa [battle_clear_ex_10706_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_clear_ex_10706_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Kwestia głosowa [battle_clear_ex_10706_1] (Extra Conditions Fulfilled)] 이것까지가 내 직감이었어. 이번에도… 틀리진 않았지?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_clear_ex_10706_1].dlg
   limit: do 120 znaków
   EN: And that's as far as my intuition will carry me. I'm not wrong again... am I?
   PL:
452. [Kwestia głosowa [battle_defeat_10706_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_defeat_10706_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Kwestia głosowa [battle_defeat_10706_1] (Defeat Wail)] 사후 처리를 하는 과정에서 망할 줄은 몰랐는데… 이런 결론을 떠올린 게 아니었다고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Seven_10706.json :: dataList[id=battle_defeat_10706_1].dlg
   limit: do 170 znaków
   EN: Bloody hell, I didn't expect things to go cock-up in the post—contract management... This isn't at all how I thought it'd go.
   PL:

## [000] The Pequod Harpooneer — Heathcliff — 피쿼드호 작살잡이
- ID Tożsamości: `10707` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 3 · HP bazowe: 99 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Poise, Bleed

454. [Karta Tożsamości — tytuł] 피쿼드호\n작살잡이
   źródło: Personalities.json :: dataList[id=10707].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Pequod\nHarpooneer
   PL:
455. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10707].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10707].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
457. [Karta Tożsamości — opis] 히스클리프의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10707].desc
   limit: do 120 znaków
   EN: Heathcliff's 7th Identity
   PL:
458. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 사냥감 추적
   źródło: Skills_personality-07.json :: dataList[id=1070701].levelList[level=1].name ; dataList[id=1070701].levelList[level=2].name ; dataList[id=1070701].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Stalk Prey
   PL:
459. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 호흡 횟수 2 증가\n[WhenUse] 다음 턴에 이 슬롯이 도발치 2을 얻음
   źródło: Skills_personality-07.json :: dataList[id=1070701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Poise Count\n[WhenUse] Gain +2 Aggro to this Skill Slot next turn
   PL:
460. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1070701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed
   PL:
461. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 호흡 횟수 3 증가\n[WhenUse] 다음 턴에 이 슬롯이 도발치 3을 얻음
   źródło: Skills_personality-07.json :: dataList[id=1070701].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +3 Poise Count\n[WhenUse] Gain +3 Aggro to this Skill Slot next turn
   PL:
462. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1070701].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL:
463. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 호흡 횟수 4 증가\n[WhenUse] 다음 턴에 이 슬롯이 도발치 5를 얻음
   źródło: Skills_personality-07.json :: dataList[id=1070701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +4 Poise Count\n[WhenUse] Gain +5 Aggro to this Skill Slot next turn
   PL:
464. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 작살박이
   źródło: Skills_personality-07.json :: dataList[id=1070702].levelList[level=1].name ; dataList[id=1070702].levelList[level=2].name ; dataList[id=1070702].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Snagharpoon
   PL:
465. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 2를 얻음
   źródło: Skills_personality-07.json :: dataList[id=1070702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Aggro to this Skill Slot next turn
   PL:
466. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] 대상의 출혈 위력의 1/4만큼 대상의 출혈 횟수 증가 (최대 10)
   źródło: Skills_personality-07.json :: dataList[id=1070702].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1070702].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict Bleed Count equal to 1/4 of Bleed Potency on target (Max 10)
   PL:
467. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 3을 얻음\n[WhenUse] 대상의 출혈 3당 호흡 1 얻음 (최대 10)
   źródło: Skills_personality-07.json :: dataList[id=1070702].levelList[level=2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +3 Aggro to this Skill Slot next turn\n[WhenUse] Gain 1 Poise for every 3 Bleed on target (Max 10)
   PL:
468. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 5를 얻음\n[WhenUse] 대상의 출혈 3당 호흡 1 얻음 (최대 10)
   źródło: Skills_personality-07.json :: dataList[id=1070702].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +5 Aggro to this Skill Slot next turn\n[WhenUse] Gain 1 Poise for every 3 Bleed on target (Max 10)
   PL:
469. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] 대상의 출혈 위력의 1/3만큼 대상의 출혈 횟수 증가 (최대 10)
   źródło: Skills_personality-07.json :: dataList[id=1070702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict Bleed Count equal to 1/3 of Bleed Potency on target (Max 10)
   PL:
470. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 매듭 끊기
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].name ; dataList[id=1070703].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Sever Knot
   PL:
471. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 질투 공명 3 이상이면 합 위력 +1\n질투 공명 4 이상이면 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 3+ Envy Reson., Clash Power +1\nAt 4+ Envy Reson., Coin Power +1
   PL:
472. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1070703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 220 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 50% 미만이면 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 50%- HP, inflict 1 Bleed
   PL:
474. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1070703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 220 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 50% 미만이면 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 473 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [CriticalOnSucceedAttack] 크리티컬 피해량 +30%
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] +30% Damage on Critical Hit
   PL:
477. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 질투 공명 3 이상이면 합 위력 +1\n질투 공명 4 이상이면 코인 위력 +1\n질투 완전 공명 6 이상이면 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 3+ Envy Reson., Clash Power +1\nAt 4+ Envy Reson., Coin Power +1\nAt 6+ Envy A-Reson., Coin Power +1
   PL:
478. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 75% 미만이면 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 75%- HP, inflict 1 Bleed
   PL:
479. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 50% 미만이면 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 473 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 75% 미만이면 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 50% 미만이면 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 473 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [CriticalOnSucceedAttack] 크리티컬 피해량 +50%
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] +50% Damage on Critical Hit
   PL:
483. [Obrona (ulepszenia 1,4) — nazwa] 되갚기
   źródło: Skills_personality-07.json :: dataList[id=1070704].levelList[level=1].name ; dataList[id=1070704].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Payback
   PL:
484. [Obrona (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 2를 얻음\n[StartBattle] 자신의 [Breath]만큼 [DefenseUp]를 얻음. (최대 10)
   źródło: Skills_personality-07.json :: dataList[id=1070704].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [StartBattle], [Breath], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain +2 Aggro to this Skill Slot next turn\n[StartBattle] Gain [DefenseUp] for every [Breath] on self (Max 10)
   PL:
485. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 5를 얻음\n[StartBattle] 자신의 [Breath]만큼 [DefenseUp]를 얻음. (최대 10)
   źródło: Skills_personality-07.json :: dataList[id=1070704].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [StartBattle], [Breath], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain +5 Aggro to this Skill Slot next turn\n[StartBattle] Gain [DefenseUp] for every [Breath] on self (Max 10)
   PL:
486. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — nazwa] 헤집어진 문신
   źródło: Passives.json :: dataList[id=1070701].name
   limit: do 40 znaków
   EN: Mutilated Tattoos
   PL:
487. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — opis] 자신을 포함한 아군이 피격당할 때마다 다음 턴에 [AttackUp] 1, [DefenseUp] 1을 얻는다. (최대 6)\n자신의 체력이 낮아질수록 가하는 피해량이 증가한다.\n- 자신의 잃은 체력 1%당 피해량 0.4% 증가
   źródło: Passives.json :: dataList[id=1070701].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Gain 1 [AttackUp] and 1 [DefenseUp] next turn every time an ally (including this unit) is attacked. (Max 6)\nDeal more damage at less HP.\n- Deal +0.4% damage for every 1% missing HP
   PL:
488. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — podsumowanie] 피격당할 때마다 다음 턴에 [AttackUp] 1, [DefenseUp] 1 얻음. 자신의 체력이 낮아질수록 피해량이 증가
   źródło: Passives.json :: dataList[id=1070701].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Gain 1 [AttackUp] and 1 [DefenseUp] every time this unit is attacked. Deal more damage the less HP this unit has.
   PL:
489. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Envy) — nazwa] 헤집어진 문신
   źródło: Passives.json :: dataList[id=1070711].name
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Envy) — opis] 자신을 포함한 아군이 피격당할 때마다 다음 턴에 [AttackUp] 1, [DefenseUp] 1을 얻는다. 피격 당한 아군이 피쿼드호 소속인 경우, 대신 2를 얻는다. (최대 9)\n자신의 체력이 낮아질수록 가하는 피해량이 증가한다.\n- 자신의 잃은 체력 1%당 피해량 1% 증가
   źródło: Passives.json :: dataList[id=1070711].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Gain 1 [AttackUp] and 1 [DefenseUp] next turn every time an ally (including this unit) is attacked. Gain 2 of each instead if the ally is from The Pequod. (Max 9)\nDeal more damage the less HP this unit has.\n- Deal +1% damage for every 1% missing HP
   PL:
491. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Envy) — podsumowanie] 피격당할 때마다 다음 턴에 [AttackUp] 1, [DefenseUp] 1 얻음. 자신의 체력이 낮아질수록 피해량이 증가
   źródło: Passives.json :: dataList[id=1070711].summary
   (powtórzenie elementu 488 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — nazwa] 절박
   źródło: Passives.json :: dataList[id=1070721].name
   limit: do 40 znaków
   EN: Desperation
   PL:
493. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — opis] 최대 체력이 가장 높은 아군 1명이 자신의 체력이 낮아질수록 <noparse>관통 피해량 증가</noparse>\n- 자신의 잃은 체력 1%당 피해량 0.15% 증가 (최대 15%)
   źródło: Passives.json :: dataList[id=1070721].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n
   EN: 1 ally with the highest max HP deals more Pierce Damage at less HP\n- Deal +0.15% damage for every 1% missing HP (Max 15%)
   PL:
494. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — podsumowanie] 최대 체력이 가장 높은 아군 1명이 자신의 체력이 낮아질수록 <noparse>관통 피해량 증가</noparse>
   źródło: Passives.json :: dataList[id=1070721].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>
   EN: 1 ally with the highest max HP deals more Pierce Damage at less HP
   PL:
495. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Envy) — nazwa] 절박
   źródło: Passives.json :: dataList[id=1070731].name
   (powtórzenie elementu 492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Envy) — opis] 최대 체력이 가장 높은 아군 1명이 자신의 체력이 낮아질수록 <noparse>관통 피해량 증가</noparse>\n- 자신의 잃은 체력 1%당 피해량 0.3% 증가 (최대 30%)
   źródło: Passives.json :: dataList[id=1070731].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n
   EN: 1 ally with the highest max HP deals more Pierce Damage at less HP\n- Deal +0.3% damage for every 1% missing HP (Max 30%)
   PL:
497. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Envy) — podsumowanie] 최대 체력이 가장 높은 아군 1명이 자신의 체력이 낮아질수록 <noparse>관통 피해량 증가</noparse>
   źródło: Passives.json :: dataList[id=1070731].summary
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Kwestia głosowa [get_10707_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=get_10707_1].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Kwestia głosowa [get_10707_1] (Identity Acquisition)] 밧줄. 꽉 잡아라. …가라앉기 싫으면.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=get_10707_1].dlg
   limit: do 120 znaków
   EN: This rope. Hold on tight. ... Or sink.
   PL:
500. [Kwestia głosowa [lobby_morning_10707_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=lobby_morning_10707_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Kwestia głosowa [lobby_morning_10707_1] (Morning Greeting)] 해가 떴다. 해야 할 일들을 시작해라. 성실, 하게.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=lobby_morning_10707_1].dlg
   limit: do 120 znaków
   EN: Sunrise. Time to start work. Work hard.
   PL:
502. [Kwestia głosowa [lobby_noon_10707_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=lobby_noon_10707_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Kwestia głosowa [lobby_noon_10707_1] (Afternoon Greeting)] 인어 지느러미살, 육포. 맛있는데. 너희는. 별로인가, 그렇게?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=lobby_noon_10707_1].dlg
   limit: do 120 znaków
   EN: Mermaid fin jerky. Good nosh. What, not good enough for you?
   PL:
504. [Kwestia głosowa [lobby_night_10707_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=lobby_night_10707_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Kwestia głosowa [lobby_night_10707_1] (Evening Greeting)] 밤은, 좋지. 밤이 오면, 노을도 오니까. 그리고, 덮어져. 내 몸도, 문신도.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=lobby_night_10707_1].dlg
   limit: do 120 znaków
   EN: Nights are good. Sunset comes, before night comes. Shadow covers my body. Covers my tattoos.
   PL:
506. [Kwestia głosowa [smalltalk_10707_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=smalltalk_10707_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Kwestia głosowa [smalltalk_10707_1] (Chatter #1)] 이건… 창피야. 내 껍질에, 직접 새겼던. 지우고 싶지만, 지울 수 없는.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=smalltalk_10707_1].dlg
   limit: do 120 znaków
   EN: This... is shame. Engraved it myself, on my skin. Want to erase. But can't erase.
   PL:
508. [Kwestia głosowa [smalltalk_10707_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=smalltalk_10707_2].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Kwestia głosowa [smalltalk_10707_2] (Chatter #2)] 숨어 있어. 내 말 속에도, 낙인이. 중지가. 그래서 헤집어 놓았어. 뇌와 혀를, 직접.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=smalltalk_10707_2].dlg
   limit: do 140 znaków
   EN: The Middle branded my tongue. My speech. So I cut them up. Cut up my brain and my tongue. Did it to myself.
   PL:
510. [Kwestia głosowa [smalltalk_10707_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=smalltalk_10707_3].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Kwestia głosowa [smalltalk_10707_3] (Chatter #3)] 이 매듭, 중지에서 썼어. 자주. 절박매듭. 풀리지 않지, 웬만한 일에는.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=smalltalk_10707_3].dlg
   limit: do 120 znaków
   EN: This knot, called Desperate's Knot. Used in the Middle. Hard to undo.
   PL:
512. [Kwestia głosowa [smalltalk_10707_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=smalltalk_10707_4].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Kwestia głosowa [smalltalk_10707_4] (Post-Uptie Chat 1)] 작살잡이는, 고래를 죽여. 고래를 죽이면, 끝낼 수 있겠지. 이 항해.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=smalltalk_10707_4].dlg
   limit: do 120 znaków
   EN: Harpooneers kill Whale. Kill the Whale... and it'll be over. This voyage.
   PL:
514. [Kwestia głosowa [smalltalk_10707_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=smalltalk_10707_5].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Kwestia głosowa [smalltalk_10707_5] (Post-Uptie Chat 2)] 선장 명령, 어긴 적 없지. 항상. 하지만, 아닌 것 같다. 내가 가려는 방향. 다르거든. 이제는, 알고 싶어. 내가 가고 싶은 방향.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=smalltalk_10707_5].dlg
   limit: do 160 znaków
   EN: Never broke Captain's orders. Never. But no more. My way. Not her way. It's different now. Now... want to know my path.
   PL:
516. [Kwestia głosowa [neglect_10707_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=neglect_10707_1].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Kwestia głosowa [neglect_10707_1] (Idle)] (작살을 갈고 매듭을 묶는 소리)
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=neglect_10707_1].dlg
   limit: do 120 znaków
   EN: (Sounds of whetting a harpoon and tying ropes to it)
   PL:
518. [Kwestia głosowa [gacksung_10707_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=gacksung_10707_1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Kwestia głosowa [gacksung_10707_1] (Uptying)] 왔군, 때가. 고래를, 죽이고. 심장을, 터트리고. 나갈 때.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=gacksung_10707_1].dlg
   limit: do 120 znaków
   EN: It is time. Time to kill the Whale. To destroy the Whale-heart. Time to escape.
   PL:
520. [Kwestia głosowa [formation_10707_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=formation_10707_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Kwestia głosowa [formation_10707_1] (Deployment)] 밧줄, 단단히 묶어라.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=formation_10707_1].dlg
   limit: do 120 znaków
   EN: Rope. Knot tight.
   PL:
522. [Kwestia głosowa [battleentry_10707_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battleentry_10707_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Kwestia głosowa [battleentry_10707_1] (Stage Entry)] 가자, 죽이러.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battleentry_10707_1].dlg
   limit: do 120 znaków
   EN: Let's go. Let's kill.
   PL:
524. [Kwestia głosowa [battle_select_10707_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_select_10707_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Kwestia głosowa [battle_select_10707_1] (Viewed in Battle)] 다시 묶어줄까? 절박매듭.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_select_10707_1].dlg
   limit: do 120 znaków
   EN: Want me to tie knot again? Desperate's Knot?
   PL:
526. [Kwestia głosowa [battle_endcommand_10707_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_endcommand_10707_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Kwestia głosowa [battle_endcommand_10707_1] (Commencing Attack)] 꽂아 넣어.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_endcommand_10707_1].dlg
   limit: do 120 znaków
   EN: Stab deep.
   PL:
528. [Kwestia głosowa [battle_enemy_break_10707_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_enemy_break_10707_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Kwestia głosowa [battle_enemy_break_10707_1] (Enemy Stagger)] 느려졌네, 저거. 맞추기, 쉽군.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_enemy_break_10707_1].dlg
   limit: do 120 znaków
   EN: That one. Slowed. Easy target.
   PL:
530. [Kwestia głosowa [battle_break_10707_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_break_10707_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Kwestia głosowa [battle_break_10707_1] (Staggered)] 으윽…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_break_10707_1].dlg
   limit: do 120 znaków
   EN: Aagh...
   PL:
532. [Kwestia głosowa [battle_kill_10707_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_kill_10707_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Kwestia głosowa [battle_kill_10707_1] (Enemy Killed)] 가까워진다, 항해의 끝.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_kill_10707_1].dlg
   limit: do 120 znaków
   EN: End of voyage. Nearing.
   PL:
534. [Kwestia głosowa [battle_dead_10707_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_dead_10707_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Kwestia głosowa [battle_dead_10707_1] (Death)] 노을, 보고 싶네… 일렁이는… 하늘.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_dead_10707_1].dlg
   limit: do 120 znaków
   EN: Miss the sunset... the shimmering... sky...
   PL:
536. [Kwestia głosowa [choice_success_p_10707_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=choice_success_p_10707_2].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Kwestia głosowa [choice_success_p_10707_2] (Check Passed)] 해냈어, 해결.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=choice_success_p_10707_2].dlg
   limit: do 120 znaków
   EN: Did it. Job done.
   PL:
538. [Kwestia głosowa [choice_fail_n_10707_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=choice_fail_n_10707_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Kwestia głosowa [choice_fail_n_10707_1] (Check Failed)] 이런 건, 못해. 다른 사람이, 잘하겠지. 더.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=choice_fail_n_10707_1].dlg
   limit: do 120 znaków
   EN: Can't do it. Someone else can do better.
   PL:
540. [Kwestia głosowa [battle_clear_10707_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_clear_10707_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Kwestia głosowa [battle_clear_10707_1] (Victory Cry)] 끊어놨어. 숨통. 죄다. 배로 이제, 돌아가자.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_clear_10707_1].dlg
   limit: do 120 znaków
   EN: Killed everyone. Let's return. To ship.
   PL:
542. [Kwestia głosowa [battle_clear_ex_10707_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_clear_ex_10707_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Kwestia głosowa [battle_clear_ex_10707_1] (Extra Conditions Fulfilled)] 들리지 않네, 심장 고동 소리. 모든 고래. 심장소리. 멈춰도. 있을까? 돌아갈 곳, 내가.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_clear_ex_10707_1].dlg
   limit: do 120 znaków
   EN: No more heart beating. Even when all Whale hearts stop beating... to where I return?
   PL:
544. [Kwestia głosowa [battle_defeat_10707_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_defeat_10707_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Kwestia głosowa [battle_defeat_10707_1] (Defeat Wail)] 관, 짜야해. …보내줘. 관에 넣어. 내 몸만은. 캐시에게. 언젠가…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Qui_10707.json :: dataList[id=battle_defeat_10707_1].dlg
   limit: do 150 znaków
   EN: Must build coffin. Send me away. Put me in the coffin. So at least my body... finds way back to Cathy. One day...
   PL:

## [000] Öufi Assoc. South Section 3 — Heathcliff — 남부 외우피 협회 3과
- ID Tożsamości: `10708` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: — · HP bazowe: 79 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Tremor

546. [Karta Tożsamości — tytuł] 남부 외우피 협회\n3과
   źródło: Personalities.json :: dataList[id=10708].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Öufi Assoc.\nSouth Section 3
   PL:
547. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10708].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10708].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Karta Tożsamości — opis] 히스클리프의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10708].desc
   limit: do 120 znaków
   EN: Heathcliff's 8th Identity
   PL:
550. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 이행 권고
   źródło: Skills_personality-07.json :: dataList[id=1070801].levelList[level=1].name ; dataList[id=1070801].levelList[level=2].name ; dataList[id=1070801].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Execution Advised
   PL:
551. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1070801].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1070801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
552. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Vibration]이 3 이상이면, 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070801].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 3+ [Vibration], Coin Power +1
   PL:
553. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Vibration] 3 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-07.json :: dataList[id=1070801].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Coin Power +1 for every 3 [Vibration] on target (Max 2)
   PL:
554. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 마지막 경고
   źródło: Skills_personality-07.json :: dataList[id=1070802].levelList[level=1].name ; dataList[id=1070802].levelList[level=2].name ; dataList[id=1070802].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Final Warning
   PL:
555. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1070802].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1070802].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1070802].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
556. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1070802].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1070802].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 555 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Vibration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070802].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 6+ [Vibration], Coin Power +1
   PL:
558. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Vibration] 6 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-07.json :: dataList[id=1070802].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Coin Power +1 for every 6 [Vibration] on target (Max 2)
   PL:
559. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 집행 선고
   źródło: Skills_personality-07.json :: dataList[id=1070803].levelList[level=3].name ; dataList[id=1070803].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Execution Sentencing
   PL:
560. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Vibration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070803].levelList[level=3].desc
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070803].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1070803].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL:
562. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070803].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1070803].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 위력과 횟수의 합이 20 이상이면, [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_personality-07.json :: dataList[id=1070803].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1070803].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationCollapse], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] If target has 20+ ([Vibration] + [Vibration] Count), trigger [Switch_Vibration] on target, converting [Vibration] to [VibrationCollapse]
   PL:
564. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Vibration] 6 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-07.json :: dataList[id=1070803].levelList[level=4].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Obrona (ulepszenia 1,4) — nazwa] 방해는 금지다
   źródło: Skills_personality-07.json :: dataList[id=1070804].levelList[level=1].name ; dataList[id=1070804].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Do Not Obstruct
   PL:
566. [Obrona (ulepszenia 1,4) — opis] 보호막이 있는 동안 피격 시 공격자의 [Vibration] 횟수 1 증가 (이 스킬의 효과는 중복되어 적용되지 않음)
   źródło: Skills_personality-07.json :: dataList[id=1070804].levelList[level=1].desc ; dataList[id=1070804].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: When attacked while this unit has Shield, inflict +1 [Vibration] Count on the attacker (this Skill's effect does not stack with multiple uses)
   PL:
567. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — nazwa] 엄중한 입회
   źródło: Passives.json :: dataList[id=1070801].name
   limit: do 40 znaków
   EN: Grave Attendance
   PL:
568. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — opis] 대상의 [Vibration] 위력 6 당 피해량 +5% (최대 15%)
   źródło: Passives.json :: dataList[id=1070801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Deal +5% damage for every 6 [Vibration] Potency on target (Max 15%)
   PL:
569. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Pride) — nazwa] 엄중한 입회
   źródło: Passives.json :: dataList[id=1070811].name
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Pride) — opis] 대상의 [Vibration] 위력 6 당 피해량 +10% (최대 30%)\n자신의 스킬 효과로 [VibrationCollapse] 변환 시 대상에게 [VibrationExplosion] 발동
   źródło: Passives.json :: dataList[id=1070811].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [VibrationCollapse], [VibrationExplosion]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: Deal +10% damage for every 6 [Vibration] Potency on target (Max 30%)\nWhen converting [Vibration] into [VibrationCollapse] with this unit's Skill effects, trigger [VibrationExplosion] on target
   PL:
571. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Pride) — nazwa] 의무 이행 확인
   źródło: Passives.json :: dataList[id=1070821].name
   limit: do 50 znaków
   EN: Verify Obligation Fulfillment
   PL:
572. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Pride) — opis] 속도가 가장 빠른 아군 1명의 [Vibration] 위력, 횟수를 부여하는 스킬의 합 위력 +1
   źródło: Passives.json :: dataList[id=1070821].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: To 1 ally with the fastest Speed: Clash Power +1 to Skills that apply [Vibration] Potency or Count
   PL:
573. [Kwestia głosowa [get_10708_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=get_10708_1].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Kwestia głosowa [get_10708_1] (Identity Acquisition)] 그럼, 지금부터 상호 입회 하의 계약 검토를 진행하겠다. 헛짓거리는 하지 말자고, 우리.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=get_10708_1].dlg
   limit: do 190 znaków
   EN: Now, we will proceed to review the contract with mutual attendance of both parties. Let's not do anything stupid and waste each other's time, yeah?
   PL:
575. [Kwestia głosowa [lobby_morning_10708_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=lobby_morning_10708_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Kwestia głosowa [lobby_morning_10708_1] (Morning Greeting)] 아침부터 보채지 좀 마라… 오늘 입회해야 할 계약 건만 다섯이라고. 아침은 좀 쉬게 해줘.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=lobby_morning_10708_1].dlg
   limit: do 190 znaków
   EN: Quit naggin' me... it's only the morn. I've got five different contract attendances lined up today, so let me rest the morning away at least.
   PL:
577. [Kwestia głosowa [lobby_noon_10708_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=lobby_noon_10708_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Kwestia głosowa [lobby_noon_10708_1] (Afternoon Greeting)] 다음으로 검토할 부분은… 미안하지만, 계약 진행 중에 취식행위를 하는 건 본 중개인이 용인할 수 없다. 점심은 이따가 먹어.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=lobby_noon_10708_1].dlg
   limit: do 230 znaków
   EN: Next.. we will review... Please, as a participating intermediary, I cannot permit the attendees to consume food in the middle of a contract write-up. Get somethin' to eat later.
   PL:
579. [Kwestia głosowa [lobby_night_10708_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=lobby_night_10708_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Kwestia głosowa [lobby_night_10708_1] (Evening Greeting)] 거기, 졸지 마라. 아직 제일 중요한 건을 확인하지 않았어. 나도 빨리 퇴근하고 자고 싶으니까, 업무에 협조해달라고…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=lobby_night_10708_1].dlg
   limit: do 190 znaków
   EN: You there, wake up. We haven't even gone over the most important clauses yet. Yeah, yeah. I want to head home as much as you do, so cooperate. Yeah?
   PL:
581. [Kwestia głosowa [smalltalk_10708_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=smalltalk_10708_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Kwestia głosowa [smalltalk_10708_1] (Chatter #1)] 외우피의 일은 계약의 중개와 입회. 그리고 그 계약을 이행하지 않으려 하거나 계약 자체에 훼방을 놓는 놈들을… 흥, 말을 듣게 하는 거지, 뭐.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=smalltalk_10708_1].dlg
   limit: do 260 znaków
   EN: The Öufi's primary field is mediating and observing contracts. If any poor sod refuses to carry out the terms, or obstructs the contract fulfillment... hmph, then we'll be forced to make them comply.
   PL:
583. [Kwestia głosowa [smalltalk_10708_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=smalltalk_10708_2].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Kwestia głosowa [smalltalk_10708_2] (Chatter #2)] 이 치렁치렁하고 답답한 옷은 그다지 마음에 들지는 않지만… 이런 것들이 계약을 집행하는 자의 권위를 상징한대나, 뭐래나.\n마음대로 벗을 수도 없으니 익숙해지는 수 밖에… 고급스러운 건 사실이고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=smalltalk_10708_2].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Can't say I enjoy this overly posh, uncomfortable clothing, but... these apparently represent the authority of the executors of a contract, or something along those lines.\nWell, since I can't be caught out of uniform... I suppose I'll have to get used to it. And it *is* quite posh.
   PL:
585. [Kwestia głosowa [smalltalk_10708_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=smalltalk_10708_3].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Kwestia głosowa [smalltalk_10708_3] (Chatter #3)] 외우피의 무기는 절단에 특화되어 있지. 계약이 이행되지 않거나, 규율을 어긴 자들을 처형하는 것이 중요하다고 하더라고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=smalltalk_10708_3].dlg
   limit: do 270 znaków
   EN: Weapons of the Öufi specialize in amputation. It is an important part of our job to execute those that have failed to carry out the contract, or those who have broken any relevant regulations. Or so they say.
   PL:
587. [Kwestia głosowa [smalltalk_10708_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=smalltalk_10708_4].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Kwestia głosowa [smalltalk_10708_4] (Post-Uptie Chat 1)] 아… 뭐, 이렇게 됐다. 그러게 마음에 안 드는 일이 있으면 서면으로 항의해야지, 소리나 꽥꽥 지르면서 계약을 방해하면 쓰나.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=smalltalk_10708_4].dlg
   limit: do 240 znaków
   EN: Well... I suppose it is what it is. You should have submitted a formal complaint instead of screamin' and throwin' a tantrum before everyone else during the contract. That's obstruction.
   PL:
589. [Kwestia głosowa [smalltalk_10708_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=smalltalk_10708_5].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Kwestia głosowa [smalltalk_10708_5] (Post-Uptie Chat 2)] 외우피가 주관하는 계약은 반드시 완수되어야 한다. 그것이 어긋나는 일은 있을 수 없어야 해. 어떤 계약이든 말이지.\n…누군가 피를 보는 약속이 되더라도.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=smalltalk_10708_5].dlg
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A contract overseen by the Öufi, no matter the conditions, must be fulfilled. It cannot, and should not, fall through.\n...Even if it means that there must be blood.
   PL:
591. [Kwestia głosowa [neglect_10708_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=neglect_10708_1].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Kwestia głosowa [neglect_10708_1] (Idle)] …침묵 또한 계약 검토를 불성실하게 참여하는 것으로 간주한다. 뭐라도 말해.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=neglect_10708_1].dlg
   limit: do 130 znaków
   EN: ... Total silence may also count under negligence to properly review the contract. Say something.
   PL:
593. [Kwestia głosowa [gacksung_10708_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=gacksung_10708_1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Kwestia głosowa [gacksung_10708_1] (Uptying)] 마지막 경고였다, 그게. 지금부터는 계약 집행 방해의 죄를 물어서… 전부 패버린다!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=gacksung_10708_1].dlg
   limit: do 190 znaków
   EN: That was your final warning. Now, as obstruction of contract execution has been observed, I am compelled to... beat the shite out of you all!
   PL:
595. [Kwestia głosowa [formation_10708_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=formation_10708_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Kwestia głosowa [formation_10708_1] (Deployment)] 계약이 또 어그러졌나보지?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=formation_10708_1].dlg
   limit: do 120 znaków
   EN: Another broken contract, eh?
   PL:
597. [Kwestia głosowa [battleentry_10708_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battleentry_10708_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Kwestia głosowa [battleentry_10708_1] (Stage Entry)] 입회한다.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battleentry_10708_1].dlg
   limit: do 120 znaków
   EN: I am in attendance.
   PL:
599. [Kwestia głosowa [battle_select_10708_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_select_10708_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Kwestia głosowa [battle_select_10708_1] (Viewed in Battle)] 집행 중 제삼자의 끼어들기도 금지야.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_select_10708_1].dlg
   limit: do 120 znaków
   EN: An unauthorized involvement of a third party is also prohibited.
   PL:
601. [Kwestia głosowa [battle_endcommand_10708_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_endcommand_10708_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Kwestia głosowa [battle_endcommand_10708_1] (Commencing Attack)] 조심하랬지!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_endcommand_10708_1].dlg
   limit: do 120 znaków
   EN: I told you to watch yourself!
   PL:
603. [Kwestia głosowa [battle_enemy_break_10708_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_enemy_break_10708_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Kwestia głosowa [battle_enemy_break_10708_1] (Enemy Stagger)] 지금이라도 말 들어.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_enemy_break_10708_1].dlg
   limit: do 120 znaków
   EN: You better start listening now.
   PL:
605. [Kwestia głosowa [battle_break_10708_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_break_10708_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Kwestia głosowa [battle_break_10708_1] (Staggered)] 큭…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_break_10708_1].dlg
   limit: do 120 znaków
   EN: Agh...
   PL:
607. [Kwestia głosowa [battle_kill_10708_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_kill_10708_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Kwestia głosowa [battle_kill_10708_1] (Enemy Killed)] 방해꾼 하나가 사라졌군.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_kill_10708_1].dlg
   limit: do 120 znaków
   EN: Now that's one less obstacle in our way.
   PL:
609. [Kwestia głosowa [battle_dead_10708_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_dead_10708_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Kwestia głosowa [battle_dead_10708_1] (Death)] 내가… 죽어도. 후, 외우피는 반드시… 집행을 끝낸다.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_dead_10708_1].dlg
   limit: do 130 znaków
   EN: You can kill me... but the Öufi will ensure that... the contract is executed to its full extent..
   PL:
611. [Kwestia głosowa [choice_success_p_10708_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=choice_success_p_10708_2].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Kwestia głosowa [choice_success_p_10708_2] (Check Passed)] 계약대로지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=choice_success_p_10708_2].dlg
   limit: do 120 znaków
   EN: As stipulated in the contract.
   PL:
613. [Kwestia głosowa [choice_fail_n_10708_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=choice_fail_n_10708_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Kwestia głosowa [choice_fail_n_10708_1] (Check Failed)] …계약을 잘못 해석했나?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=choice_fail_n_10708_1].dlg
   limit: do 120 znaków
   EN: ... Did I misunderstand the terms of the contract?
   PL:
615. [Kwestia głosowa [battle_clear_10708_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_clear_10708_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Kwestia głosowa [battle_clear_10708_1] (Victory Cry)] 일단 시작한 집행 방해에 대한 처벌은… 내가 아니더라도 반드시 외우피에서 완수한다. …기대하라고, 흥.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_clear_10708_1].dlg
   limit: do 210 znaków
   EN: The consequences for an obstruction of contract execution will be carried out no matter what. There will be another from the Öufi... so look forward to it, hmph.
   PL:
617. [Kwestia głosowa [battle_clear_ex_10708_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_clear_ex_10708_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Kwestia głosowa [battle_clear_ex_10708_1] (Extra Conditions Fulfilled)] 입회 완료. 계약에 따른 의무 이행 확인도 했고. 이제 할 건 다 했네!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_clear_ex_10708_1].dlg
   limit: do 160 znaków
   EN: Attendance completed. Since the contract's been carried out to the letter... there ain't much else for me to do here!
   PL:
619. [Kwestia głosowa [battle_defeat_10708_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_defeat_10708_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Kwestia głosowa [battle_defeat_10708_1] (Defeat Wail)] 또 계약 하나가 파기됐네. 하… 이런건 실적으로 칠 수도 없다고. 쯧, 다음 건으로 넘어가야지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Oufi_10708.json :: dataList[id=battle_defeat_10708_1].dlg
   limit: do 200 znaków
   EN: Another contract fell through. Haah... this doesn't even get reflected in the performance reviews. Tsk, I suppose I should move on to the next case soon.
   PL:

## [00] MultiCrack Office Fixer — Heathcliff — 멀티크랙 사무소 해결사
- ID Tożsamości: `10709` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 4 · HP bazowe: 71 · szybkość: 3–5 / 3–6 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Charge

621. [Karta Tożsamości — tytuł] 멀티크랙 사무소\n해결사
   źródło: Personalities.json :: dataList[id=10709].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: MultiCrack Office\nFixer
   PL:
622. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10709].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10709].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Karta Tożsamości — opis] 히스클리프의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10709].desc
   limit: do 120 znaków
   EN: Heathcliff's 9th Identity
   PL:
625. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 40S-2 가동
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=1].name ; dataList[id=1070901].levelList[level=2].name ; dataList[id=1070901].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: 40S-2 Activation
   PL:
626. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수를 5 소모하여 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Coin Power +1
   PL:
627. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count
   PL:
628. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] [WhenUse] [Charge] 횟수를 5 소모하여 코인 위력 +1<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=2].desc ; dataList[id=1070901].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Coin Power +1<style="highlight"></style>
   PL:
629. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 자신의 [Charge] 횟수 2 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: <style="highlight">[OnSucceedAttack] Gain +2 [Charge] Count</style>
   PL:
630. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count<style="highlight"></style>
   PL:
631. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 광전 표식
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=1].name ; dataList[id=1070902].levelList[level=2].name ; dataList[id=1070902].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Photoelectric Mark
   PL:
633. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면, 최대 체력의 2 x (10 - 현재 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수가 10으로 증가\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power +1
   PL:
634. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge]만큼 [PhotoElectricity] 부여 (최대 2)
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [PhotoElectricity]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [PhotoElectricity] = 광전 / Photoelectricity
   EN: [OnSucceedAttack] Inflict [PhotoElectricity] equal to [Charge] (max 2)
   PL:
635. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면, 최대 체력의 2 x (10 - 현재 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수가 10으로 증가\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 +1<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power +1<style="highlight"></style>
   PL:
636. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Charge] 횟수를 소모했으면, [DefenseDown] 2 부여</style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: <style="highlight">[OnSucceedAttack] If this unit consumed [Charge] Count, inflict 2 [DefenseDown]</style>
   PL:
637. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [TakeHpHealReduce] 1 부여</style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [TakeHpHealReduce]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [TakeHpHealReduce]</style>
   PL:
638. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge]만큼 [PhotoElectricity] 부여 (최대 <style="highlight">3</style>)
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [PhotoElectricity]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [PhotoElectricity] = 광전 / Photoelectricity
   EN: [OnSucceedAttack] Inflict [PhotoElectricity] equal to [Charge] (max <style="highlight">3</style>)
   PL:
639. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면, 최대 체력의 2 x (10 - 현재 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수가 10으로 증가\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 <style="highlight">+2</style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power <style="highlight">+2</style>
   PL:
640. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Charge] 횟수를 소모했으면, [DefenseDown] 2 부여</style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 636 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Charge] 횟수를 소모했으면, [DefenseDown] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] If this unit consumed [Charge] Count, inflict 2 [DefenseDown]<style="highlight"></style>
   PL:
642. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [TakeHpHealReduce] <style="highlight">2</style> 부여
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [TakeHpHealReduce]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [TakeHpHealReduce]
   PL:
643. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge]만큼 [PhotoElectricity] 부여 (최대 3)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [PhotoElectricity]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [PhotoElectricity] = 광전 / Photoelectricity
   EN: [OnSucceedAttack] Inflict [PhotoElectricity] equal to [Charge] (max 3)<style="highlight"></style>
   PL:
644. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 광전 작살
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=3].name ; dataList[id=1070903].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 5 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Photoelectric Harpoon
   PL:
645. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [Charge]이 2 이상이면, 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 2+ [Charge], Coin Power +1
   PL:
646. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +5 [Charge] Count
   PL:
647. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] ([Charge] x 3)만큼 자신의 [Charge] 횟수 증가 (최대 9)
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] x 3) [Charge] Count (max 9)
   PL:
648. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge]만큼 [PhotoElectricity] 부여 (최대 3)
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [PhotoElectricity]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [PhotoElectricity] = 광전 / Photoelectricity
   EN: [OnSucceedAttack] Inflict [PhotoElectricity] equal to [Charge] (max 3)
   PL:
649. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">[Charge] 2당 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: <style="highlight">Coin Power +1 for every 2 [Charge] on self (max 2)</style>
   PL:
650. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 <style="highlight">7</style> 증가
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +<style="highlight">7</style> [Charge] Count
   PL:
651. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] ([Charge] x 3)만큼 자신의 [Charge] 횟수 증가 (최대 9)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] x 3) [Charge] Count (max 9)<style="highlight"></style>
   PL:
652. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge]만큼 [PhotoElectricity] 부여 (최대 3)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 643 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 [Charge] 2당 [HitTakeDamageUp] 1 부여 (최대 2)</style>
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [HitTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [HitTakeDamageUp] = 타격 취약 / Blunt Fragility
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [HitTakeDamageUp] for every 2 [Charge] (max 2)</style>
   PL:
654. [Obrona (ulepszenia 1,4) — nazwa] 충전
   źródło: Skills_personality-07.json :: dataList[id=1070904].levelList[level=1].name ; dataList[id=1070904].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Charge
   PL:
655. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 3 증가 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1070904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +3 [Charge] Count (once per turn)
   PL:
656. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 [Charge] 횟수 3 증가 (턴 당 <style="highlight">2</style>회)
   źródło: Skills_personality-07.json :: dataList[id=1070904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +3 [Charge] Count (<style="highlight">2 times</style> per turn)
   PL:
657. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 모델 L37 충전
   źródło: Passives.json :: dataList[id=1070901].name
   limit: do 40 znaków
   EN: Charge Model L37
   PL:
658. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음\n\n턴 종료 시 [Charge]이 2 이상이면, 다음 턴에 [Agility] 1 얻음
   źródło: Passives.json :: dataList[id=1070901].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [Agility]
   znaczenie tagów: [Charge] = 충전 / Charge; [Agility] = 신속 / Haste
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\n\nTurn End: At 2+ [Charge], gain 1 [Agility] next turn
   PL:
659. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — podsumowanie] [Charge] 횟수 10 소모할 때마다 [Charge] 얻음
   źródło: Passives.json :: dataList[id=1070901].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain [Charge] with every 10 [Charge] Count consumption
   PL:
660. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — nazwa] 모델 L37 충전
   źródło: Passives.json :: dataList[id=1070911].name
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음\n턴 종료 시 [Charge]이 2 이상이면, 다음 턴에 [Agility] 1 얻음\n<style="highlight">턴 종료 시 [Charge]이 3 이상이면, 다음 턴에 [Agility] 1, [ParryingResultUp] 1 추가로 얻음</style>
   źródło: Passives.json :: dataList[id=1070911].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [Agility], [ParryingResultUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [Agility] = 신속 / Haste; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\nTurn End: At 2+ [Charge], gain 1 [Agility] next turn\n<style="highlight">Turn End: At 3+ [Charge], gain 1 additional [Agility] and 1 [ParryingResultUp] next turn</style>
   PL:
662. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — podsumowanie] [Charge] 횟수 10 소모할 때마다 [Charge] 얻음
   źródło: Passives.json :: dataList[id=1070911].summary
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Pasywka wsparcia (od ulepszenia 3, posiadane 7× Envy) — nazwa] 충전 모듈 추가
   źródło: Passives.json :: dataList[id=1070921].name
   limit: do 40 znaków
   EN: Charging Module Installation
   PL:
664. [Pasywka wsparcia (od ulepszenia 3, posiadane 7× Envy) — opis] 편성 순서가 1번인 아군의 [Charge] 횟수 최대치 +5\n(조건 충족 시, 다음 턴 시작 전까지 효과 적용)
   źródło: Passives.json :: dataList[id=1070921].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: #1 Deployed ally: Max [Charge] Count +5\n(When conditions are met, this effect will remain activated until the start of the next turn)
   PL:
665. [Kwestia głosowa [get_10709_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=get_10709_1].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Kwestia głosowa [get_10709_1] (Identity Acquisition)] 이야… 시간 한번 더럽게 잘 가네…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=get_10709_1].dlg
   limit: do 120 znaków
   EN: Today's slow as shite, innit...?
   PL:
667. [Kwestia głosowa [lobby_morning_10709_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=lobby_morning_10709_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Kwestia głosowa [lobby_morning_10709_1] (Morning Greeting)] 사무소 가자마자 외부 의뢰가 있으면 좋겠는데, 오전 내내 사무실에 처박혀 있는 것보단 낫거든.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=lobby_morning_10709_1].dlg
   limit: do 160 znaków
   EN: Hopefully there's a field contract waitin' for us at the Office. Beats having to sit on my arse all morning in there.
   PL:
669. [Kwestia głosowa [lobby_noon_10709_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=lobby_noon_10709_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Kwestia głosowa [lobby_noon_10709_1] (Afternoon Greeting)] 점심은 너희끼리 가라. 난… 낮잠이나 한숨 잘라니까.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=lobby_noon_10709_1].dlg
   limit: do 120 znaków
   EN: Enjoy your lunches, lads. I think I'll get a little shut-eye in the office.
   PL:
671. [Kwestia głosowa [lobby_night_10709_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=lobby_night_10709_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Kwestia głosowa [lobby_night_10709_1] (Evening Greeting)] 퇴근 시간인데 왜 죽상이냐고? 내일 또 나올 생각하니까 토악질 나와서.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=lobby_night_10709_1].dlg
   limit: do 180 znaków
   EN: You wanna know why I've the long face when it's time to clock out? 'Cuz clockin' in again tomorrow sounds downright dreadful, that's why.
   PL:
673. [Kwestia głosowa [smalltalk_10709_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=smalltalk_10709_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Kwestia głosowa [smalltalk_10709_1] (Chatter #1)] X사 합금 채굴 의뢰? 상층 동굴 정도면 생각 없이 하기엔 나쁘지 않은데…\n채굴 장비는 그쪽에서 빌려주나?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=smalltalk_10709_1].dlg
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: X Corp. alloy upper crust excavation contract? Well, I suppose that's alright for some mindless grindin'...\nAre they renting us their excavation gear?
   PL:
675. [Kwestia głosowa [smalltalk_10709_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=smalltalk_10709_2].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Kwestia głosowa [smalltalk_10709_2] (Chatter #2)] 고막가청… 어쩌고를 넓혀두긴 했는데, 시끄럽기만 하고 도움이 안 되잖아, 도움이.\n다른 걸로 교체할까? 비용은… 쯧, 어떻게든 되겠지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=smalltalk_10709_2].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I equipped something to expand my eardrums' audible frequency or what have you, but they amplify all kinds of noise... it's gettin' real irritating.\nMaybe I should swap 'em out for something else? But the cost... tsk, I suppose it'll work out somehow.
   PL:
677. [Kwestia głosowa [smalltalk_10709_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=smalltalk_10709_3].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Kwestia głosowa [smalltalk_10709_3] (Chatter #3)] 야, 시계. 네 불타는 머리만큼 신기한 거 보여줄까?\n의완은 사람 팔이랑 다르게 팔뚝이 위아래로 왔다갔다 하더라? 이거 봐~ 이거!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=smalltalk_10709_3].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Oi, clock. Wanna see something as neat as that burning head of yours?\nI can move my forearms on a vertical axis. Human elbows can't do that, yeah? Have a gander, look~!
   PL:
679. [Kwestia głosowa [smalltalk_10709_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=smalltalk_10709_4].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Kwestia głosowa [smalltalk_10709_4] (Post-Uptie Chat 1)] 여기 멀티크랙 사무소는 의체 해결사만 모집해. 의체를 가진 놈들은 전투에서 겁을 먹지 않는다나 뭐라나.\n뭐, 그러다 뒤지는 놈들도 꽤 있어. 다쳐도 아프질 않으니 몸에 무슨 이상이 생겼는지도 모르다가 어느 순간 뒤져있는 거지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=smalltalk_10709_4].dlg
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The MultiCrack Office accepts applications only from Fixers with prosthetics. Somethin' about how having prosthetic bodies helps dull the fear in combat, I think.\nWell, that's exactly how a lot of 'em bite the dust. How are they to know where they're hurt without pain?
   PL:
681. [Kwestia głosowa [smalltalk_10709_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=smalltalk_10709_5].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Kwestia głosowa [smalltalk_10709_5] (Post-Uptie Chat 2)] 원정 가는 곳이… 뭐야, T사면 그 저택 근처잖아? 꽤 번듯한 직장도 구했으니…\n하, 아니, 됐다. 살다살다 그 빌어먹을 집구석에 돌아갈 생각을 다 하네. 내가 다시 찾아갈 이유가… 없지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=smalltalk_10709_5].dlg
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Our business trip is to... huh, T Corp.? That's where that manor is. Well well well, now that I've found me a respectable career, I should—\n... Haah, ain't worth it. Why the hell did I even think about going back to that bloody dreadful manor? There's... absolutely no reason for me to crawl back into that hole.
   PL:
683. [Kwestia głosowa [neglect_10709_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=neglect_10709_1].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Kwestia głosowa [neglect_10709_1] (Idle)] …흐아암.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=neglect_10709_1].dlg
   limit: do 120 znaków
   EN: ... Yaaawn.
   PL:
685. [Kwestia głosowa [gacksung_10709_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=gacksung_10709_1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Kwestia głosowa [gacksung_10709_1] (Uptying)] 뭐야… 이 자식, 바람구멍 몇 개 생겼다고 벌써 저세상으로 가버렸는데?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=gacksung_10709_1].dlg
   limit: do 160 znaków
   EN: Oi, hey... This one's dead! Really, did you seriously kick the bucket from getting a few holes punctured on your torso?
   PL:
687. [Kwestia głosowa [formation_10709_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=formation_10709_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Kwestia głosowa [formation_10709_1] (Deployment)] 오…! 외부 의뢰냐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=formation_10709_1].dlg
   limit: do 120 znaków
   EN: Ooh...! Is it a field contract?
   PL:
689. [Kwestia głosowa [battleentry_10709_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battleentry_10709_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Kwestia głosowa [battleentry_10709_1] (Stage Entry)] 어어, 잠깐만… 아직 충전 덜 했거든?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battleentry_10709_1].dlg
   limit: do 120 znaków
   EN: Woah, hang on... I ain't fully charged yet.
   PL:
691. [Kwestia głosowa [battle_select_10709_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_select_10709_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Kwestia głosowa [battle_select_10709_1] (Viewed in Battle)] 뭐, 용건이라도 있는 거냐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_select_10709_1].dlg
   limit: do 120 znaków
   EN: Come on, out with it.
   PL:
693. [Kwestia głosowa [battle_endcommand_10709_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_endcommand_10709_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Kwestia głosowa [battle_endcommand_10709_1] (Commencing Attack)] 비켜! 내가 먼저다!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_endcommand_10709_1].dlg
   limit: do 120 znaków
   EN: Outta my way! Let me at 'em first!
   PL:
695. [Kwestia głosowa [battle_enemy_break_10709_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_enemy_break_10709_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Kwestia głosowa [battle_enemy_break_10709_1] (Enemy Stagger)] 얌전히 있어라…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_enemy_break_10709_1].dlg
   limit: do 120 znaków
   EN: Now sit tight, you...
   PL:
697. [Kwestia głosowa [battle_break_10709_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_break_10709_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Kwestia głosowa [battle_break_10709_1] (Staggered)] 엉…?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_break_10709_1].dlg
   limit: do 120 znaków
   EN: Huh...?
   PL:
699. [Kwestia głosowa [battle_kill_10709_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_kill_10709_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Kwestia głosowa [battle_kill_10709_1] (Enemy Killed)] 야, 설마 벌써 죽었냐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_kill_10709_1].dlg
   limit: do 120 znaków
   EN: Oi, you dead already?
   PL:
701. [Kwestia głosowa [battle_dead_10709_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_dead_10709_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Kwestia głosowa [battle_dead_10709_1] (Death)] 허, 이게 죽네…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_dead_10709_1].dlg
   limit: do 120 znaków
   EN: Huh, didn't think this would kill me...
   PL:
703. [Kwestia głosowa [choice_success_p_10709_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=choice_success_p_10709_2].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Kwestia głosowa [choice_success_p_10709_2] (Check Passed)] 이 기능이었던 것 같은데… 오, 됐다.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=choice_success_p_10709_2].dlg
   limit: do 120 znaków
   EN: I think this is how it's 'sposed to work... ah, I did it.
   PL:
705. [Kwestia głosowa [choice_fail_n_10709_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=choice_fail_n_10709_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Kwestia głosowa [choice_fail_n_10709_1] (Check Failed)] 아이 씨, 회로 탔잖아. 왜 이딴 걸 시키냐.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=choice_fail_n_10709_1].dlg
   limit: do 120 znaków
   EN: Oh bollocks, I fried my circuitry. Why'd you make me do this?
   PL:
707. [Kwestia głosowa [battle_clear_10709_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_clear_10709_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [Kwestia głosowa [battle_clear_10709_1] (Victory Cry)] 의뢰를 완수하긴 했는데, 뭐라고 할까… 재미없네…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_clear_10709_1].dlg
   limit: do 120 znaków
   EN: We did finish the contract but... hm, how should I put this? It ain't very... fulfilling...
   PL:
709. [Kwestia głosowa [battle_clear_ex_10709_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_clear_ex_10709_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Kwestia głosowa [battle_clear_ex_10709_1] (Extra Conditions Fulfilled)] 대충 다 작살낸 모양인데, 빨리빨리 돌아가자고. 이 정도면 의뢰한 놈도 만족하겠지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_clear_ex_10709_1].dlg
   limit: do 130 znaków
   EN: Right-o, I think our clients'll be right chuffed to see how much we've wrecked'em. Let's head back.
   PL:
711. [Kwestia głosowa [battle_defeat_10709_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_defeat_10709_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Kwestia głosowa [battle_defeat_10709_1] (Defeat Wail)] 괜히 안 해도 될 말 덧붙여서 신경 쓰이게 하지 마라. 안 그래도 이번 의뢰 망쳐서 굉장히 거슬리니까…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Meca_10709.json :: dataList[id=battle_defeat_10709_1].dlg
   limit: do 170 znaków
   EN: If you ain't sure if it's okay to say something, then say nothing. I'm already irritated as it is from this botched contract...
   PL:

## [000] Wild Hunt — Heathcliff — 와일드헌트
- ID Tożsamości: `10710` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 4 · HP bazowe: 73 · szybkość: 3–5 / 3–6 / 3–8 / 3–8
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Sinking

713. [Karta Tożsamości — tytuł] 와일드헌트
   źródło: Personalities.json :: dataList[id=10710].title
   limit: do 40 znaków
   EN: Wild Hunt
   PL:
714. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10710].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10710].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Karta Tożsamości — opis] 히스클리프의 열번째 인격
   źródło: Personalities.json :: dataList[id=10710].desc
   limit: do 120 znaków
   EN: Heathcliff’s 10th Identity
   PL:
717. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 참수
   źródło: Skills_personality-07.json :: dataList[id=1071001].levelList[level=1].name ; dataList[id=1071001].levelList[level=2].name ; dataList[id=1071001].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Beheading
   PL:
718. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking]이 8 이상이면 합 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1071001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 8+ [Sinking], Clash Power +1
   PL:
719. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071001].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1071001].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL:
720. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상의 [Sinking]이 6 이상이면 합 위력 +1\n<style="highlight">[WhenUse] 대상의 [Sinking] 횟수 3 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-07.json :: dataList[id=1071001].levelList[level=2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 6+ [Sinking], Clash Power +1\n<style="highlight">[WhenUse] If target has 3+ [Sinking] Count, Coin Power +1</style>
   PL:
721. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking]이 6 이상이면 합 위력 +1\n[WhenUse] 대상의 [Sinking] 횟수 <style="highlight">3 당</style> 코인 위력 +1 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071001].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 6+ [Sinking], Clash Power +1\n[WhenUse] <style="highlight">Coin Power +1 for every 3 [Sinking] Count on target (max 2)</style>
   PL:
722. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">3</style> 부여
   źródło: Skills_personality-07.json :: dataList[id=1071001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Sinking]
   PL:
723. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 추도 행진
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=1].name ; dataList[id=1071002].levelList[level=2].name ; dataList[id=1071002].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Memorial Procession
   PL:
724. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking]이 5 이상이면 코인 위력 +1\n[EndSkill] 자신에게 [NightPathfinding]이 있으면, 정신력 10 감소
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [EndSkill], [NightPathfinding]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [EndSkill] = [공격 종료시] / [Attack End]; [NightPathfinding] = 듀라한 / Dullahan
   EN: [WhenUse] If target has 5+ [Sinking], Coin Power +1\n[EndSkill] If this unit has [NightPathfinding], lose 10 SP
   PL:
725. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1071002].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1071002].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [WanderingFootsteps] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1071002].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1071002].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [WanderingFootsteps]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [WanderingFootsteps] = 다가오는 파탄 / Impending Ruin
   EN: [OnSucceedAttack] Inflict 2 [WanderingFootsteps] next turn
   PL:
728. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상의 [Sinking]이 5 이상이면 코인 위력 +1\n<style="highlight">[WhenUse] 자신의 [Coffin] 4 이상이면, 공격 가중치 +1\n[WhenUse] 자신에게 [NightPathfinding]이 있으면, 공격 가중치 +1</style>\n[EndSkill] 자신에게 [NightPathfinding]이 있으면, 정신력 10 감소
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Sinking], [Coffin], [NightPathfinding], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Coffin] = 관 / Coffin; [NightPathfinding] = 듀라한 / Dullahan; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] If target has 5+ [Sinking], Coin Power +1\n<style="highlight">[WhenUse] At 4+ [Coffin], Atk Weight +1\n[WhenUse] If this unit has [NightPathfinding], Atk Weight +1</style>\n[EndSkill] If this unit has [NightPathfinding], lose 10 SP
   PL:
729. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking] <style="highlight">5 당</style> 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [Coffin] <style="highlight">4당</style> 공격 가중치 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신에게 [NightPathfinding]이 있으면, 공격 가중치 +1\n[EndSkill] 자신에게 [NightPathfinding]이 있으면, 정신력 10 감소
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=4].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Sinking], [Coffin], [NightPathfinding], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Coffin] = 관 / Coffin; [NightPathfinding] = 듀라한 / Dullahan; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] <style="highlight">Coin Power +1 for every 5 Sinking on target (max 2)</style>\n[WhenUse] <style="highlight">Atk Weight +1 for every 4 [Coffin] on self (max 2)</style>\n[WhenUse] If this unit has [NightPathfinding], Atk Weight +1\n[EndSkill] If this unit has [NightPathfinding], lose 10 SP
   PL:
730. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">3</style> 부여
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 레퀴엠
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=3].name ; dataList[id=1071003].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 6 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Requiem
   PL:
732. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WinDuel] 정신력 10 회복\n[BeforeUse] 자신에게 [NightPathfinding]이 있으면, '비탄하고, 애탄하며, 파탄하라'로 발동됨\n[WhenUse] 대상의 [Sinking] 6 당 코인 위력 +1 (최대 2)\n자신의 [Coffin] 1당 피해량 +7% (최대 70%)\n[WhenUse] [Coffin] 1 얻음\n[EndSkill] 이 스킬 공격으로 대상 처치시 [Coffin] 2 얻음
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=3].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [BeforeUse], [NightPathfinding], [WhenUse], [Sinking], [Coffin], [EndSkill]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [BeforeUse] = [사용전] / [Before Use]; [NightPathfinding] = 듀라한 / Dullahan; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Coffin] = 관 / Coffin; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WinDuel] Heal 10 SP\n[BeforeUse] If this unit has [NightPathfinding], activate 'Lament, Mourn, and Despair' instead\n[WhenUse] Coin Power +1 for every 6 [Sinking] on target (max 2)\nDeal +7% damage for every [Coffin] on self (max 70%)\n[WhenUse] Gain 1 [Coffin]\n[EndSkill] If this Skill attack kills the target, gain 2 [Coffin]
   PL:
733. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
734. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [WanderingFootsteps]이 있으면, [Sinking] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1071003].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [WanderingFootsteps], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [WanderingFootsteps] = 다가오는 파탄 / Impending Ruin; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target has [WanderingFootsteps], inflict +2 [Sinking] Count
   PL:
735. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
736. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [EnemyKill] 처치한 대상의 ([Sinking] / 3)만큼 무작위 적 2명에게 [Sinking] 부여 (최대 3)
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Sinking]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Sinking] = 침잠 / Sinking
   EN: [EnemyKill] Inflict ([Sinking] on killed target/3) Sinking on 2 random enemies (max 3)
   PL:
737. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WinDuel] 정신력 10 회복\n[BeforeUse] 자신에게 [NightPathfinding]이 있으면, '비탄하고, 애탄하며, 파탄하라'로 발동됨\n[WhenUse] 대상의 [Sinking] <style="highlight">3 당</style> 코인 위력 +1 (최대 <style="highlight">4</style>)\n자신의 [Coffin] 1당 피해량 +12% (최대 120%)\n[WhenUse] [Coffin] 1 얻음\n[EndSkill] 이 스킬 공격으로 대상 처치시 [Coffin] 2 얻음
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WinDuel], [BeforeUse], [NightPathfinding], [WhenUse], [Sinking], [Coffin], [EndSkill]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [BeforeUse] = [사용전] / [Before Use]; [NightPathfinding] = 듀라한 / Dullahan; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Coffin] = 관 / Coffin; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WinDuel] Heal 10 SP\n[BeforeUse] If this unit has [NightPathfinding], activate 'Lament, Mourn, and Despair' instead\n[WhenUse] Coin Power +1 for <style="highlight">every 3</style> [Sinking] on target (max <style="highlight">4</style>)\nDeal +12% damage for every [Coffin] on self (max 120%)\n[WhenUse] Gain 1 [Coffin]\n[EndSkill] If this Skill attack kills the target, gain 2 [Coffin]
   PL:
738. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">+4</style> [Sinking] Count
   PL:
739. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">3</style> 부여
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
740. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [EnemyKill] 처치한 대상의 ([Sinking] / <style="highlight">2</style>)만큼 무작위 적 2명에게 [Sinking] 부여 (최대 <style="highlight">5</style>)
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EnemyKill], [Sinking]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Sinking] = 침잠 / Sinking
   EN: [EnemyKill] Inflict ([Sinking] on killed target/<style="highlight">2</style>) Sinking on 2 random enemies (max <style="highlight">5</style>)
   PL:
741. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 비탄하고, 애탄하며, 파탄하라
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].name ; dataList[id=1071005].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 31 · monety: 2 (−13)
   limit: do 40 znaków
   EN: Lament, Mourn, and Despair
   PL:
742. [Umiejętność 4 (×0) (ulepszenie 3) — opis] [WhenUse] 정신력 15 감소\n[WhenUse] 대상의 [Sinking] 5 당 기본 위력 +1 (최대 2)\n[WhenUse] 자신의 정신력이 낮을수록 피해량이 증가 (정신력 1당 +0.3%, 최대 21%)\n자신의 [Coffin] 1당 피해량 +7% (최대 70%)\n자신의 [NightPathfinding] 1당 피해량 +10% (최대 30%)\n[WhenUse] [Coffin] 1 얻음\n[EndSkill] 이 스킬 공격으로 대상 처치시 [Coffin] 2 얻음\n[EndSkill] 정신력이 0 미만이면, 정신력 10 회복. 정신력이 0보다 낮을수록 회복량 증가 (차이 1당 1 회복, 최대 25)\n[EndBattle] [NightPathfinding] 제거
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [Coffin], [NightPathfinding], [EndSkill], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Coffin] = 관 / Coffin; [NightPathfinding] = 듀라한 / Dullahan; [EndSkill] = [공격 종료시] / [Attack End]; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [WhenUse] Lose 15 SP\n[WhenUse] Base Power +1 for every 5 [Sinking] on target (max 2)\n[WhenUse] Deal more damage the further this unit's SP value is from 45 (+0.3% damage for every missing SP, max 21%)\nDeal +7% damage for every [Coffin] on self (max 70%)\nDeal +10% damage for every [NightPathfinding] on self (max 30%)\n[WhenUse] Gain 1 [Coffin]\n[EndSkill] If this Skill attack kills the target, gain 2 [Coffin]\n[EndSkill] At less than 0 SP, heal 10 SP. When at less than 0 SP, heal more SP the further this unit's SP value is from 0 (heal 1 additional SP for every missing SP; max 25)\n[EndBattle] Lose [NightPathfinding]
   PL:
743. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여, [Sinking] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking] and +1 [Sinking] Count
   PL:
744. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상 입힘
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise the target's Stagger Threshold by 20% of damage dealt
   PL:
745. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 우울 속성 피해를 줌 (최대 15)
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict Gloom Affinity damage equal to [Sinking] on target (max 15)
   PL:
746. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 2 — opis] [EnemyKill] 처치한 대상의 ([Sinking] / 3)만큼 무작위 적 2명에게 [Sinking] 부여 (최대 4)
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Sinking]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Sinking] = 침잠 / Sinking
   EN: [EnemyKill] Inflict ([Sinking] on killed target/3) Sinking on 2 random enemies (max 4)
   PL:
747. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 2, efekt 3 — opis] [EnemyKill] 정신력 15 회복
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=1071005].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Heal 15 SP
   PL:
748. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [WhenUse] 정신력 15 감소\n[WhenUse] 대상의 [Sinking] 5 당 기본 위력 +1 (최대 <style="highlight">4</style>)\n[WhenUse] 자신의 정신력이 낮을수록 피해량이 증가 (정신력 1당 +0.3%, 최대 21%)\n자신의 [Coffin] 1당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">100</style>%)\n자신의 [NightPathfinding] 1당 피해량 +<style="highlight">20</style>% (최대 <style="highlight">60</style>%)\n[WhenUse] [Coffin] <style="highlight">2</style> 얻음\n[EndSkill] 이 스킬 공격으로 대상 처치시 [Coffin] <style="highlight">3</style> 얻음\n[EndSkill] 정신력이 0 미만이면, 정신력 10 회복. 정신력이 0보다 낮을수록 회복량 증가 (차이 1당 <style="highlight">2</style> 회복, 최대 <style="highlight">50</style>)\n[EndBattle] [NightPathfinding] 제거
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=4].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Sinking], [Coffin], [NightPathfinding], [EndSkill], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Coffin] = 관 / Coffin; [NightPathfinding] = 듀라한 / Dullahan; [EndSkill] = [공격 종료시] / [Attack End]; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [WhenUse] Lose 15 SP\n[WhenUse] Base Power +1 for every 5 [Sinking] on target (max <style="highlight">4</style>)\n[WhenUse] Deal more damage the further this unit's SP value is from 45 (+0.3% damage for every missing SP, max 21%)\nDeal +<style="highlight">10</style>% damage for every [Coffin] on self (max <style="highlight">100</style>%)\nDeal +<style="highlight">20</style>% damage for every [NightPathfinding] on self (max <style="highlight">60</style>%)\n[WhenUse] Gain <style="highlight">2</style> [Coffin]\n[EndSkill] If this Skill attack kills the target, gain <style="highlight">3</style> [Coffin]\n[EndSkill] At less than 0 SP, heal 10 SP. When at less than 0 SP, heal more SP the further this unit's SP value is from 0 (heal <style="highlight">2</style> additional SP for every missing SP; max <style="highlight">50</style>)\n[EndBattle] Lose [NightPathfinding]
   PL:
749. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">5</style> 부여, [Sinking] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">5</style> [Sinking] and +2 [Sinking] Count
   PL:
750. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 <style="highlight">30</style>%만큼 흐트러짐 손상 입힘
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise the target's Stagger Threshold by <style="highlight">30</style>% of damage dealt
   PL:
751. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 우울 속성 피해를 줌 (최대 <style="highlight">30</style>)
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict Gloom Affinity damage equal to [Sinking] on target (max <style="highlight">30</style>)
   PL:
752. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [EnemyKill] 처치한 대상의 ([Sinking] / <style="highlight">2</style>)만큼 무작위 적 2명에게 [Sinking] 부여 (최대 <style="highlight">8</style>)
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EnemyKill], [Sinking]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Sinking] = 침잠 / Sinking
   EN: [EnemyKill] Inflict ([Sinking] on killed target/<style="highlight">2</style>) Sinking on 2 random enemies (max <style="highlight">8</style>)
   PL:
753. [Obrona (ulepszenia 1,3,4) — nazwa] 듀라한이여...!
   źródło: Skills_personality-07.json :: dataList[id=1071004].levelList[level=1].name ; dataList[id=1071004].levelList[level=3].name ; dataList[id=1071004].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: O Dullahan...!
   PL:
754. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] [NightPathfinding]이 없으면, 다음 턴에 [NightPathfinding]을 1 얻음 (턴 당 1회 발동)\n[EndBattle] [NightPathfinding]이 있으면 제거함
   źródło: Skills_personality-07.json :: dataList[id=1071004].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [NightPathfinding], [EndBattle]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [NightPathfinding] = 듀라한 / Dullahan; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [DuelCounter]\n[StartBattle] If this unit does not have [NightPathfinding], gain 1 [NightPathfinding] next turn (once per turn)\n[EndBattle] If this unit has [NightPathfinding], lose [NightPathfinding]
   PL:
755. [Obrona (ulepszenia 1,3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071004].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1071004].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Obrona (ulepszenie 3) — opis] [DuelCounter]\n<style="highlight">[BeforeUse] [NightPathfinding]이 있고 정신력이 15 이상이면, 비탄하고, 애탄하며, 파탄하라로 반격함 (턴 당 1회 발동)</style>\n[StartBattle] [NightPathfinding]이 없으면, 다음 턴에 [NightPathfinding]을 1 얻음 (턴 당 1회 발동)\n<style="highlight">[WhenUse] 대상의 [Sinking]이 6 이상이면, 코인 위력 +1</style>\n[EndBattle] [NightPathfinding]이 있으면 제거함
   źródło: Skills_personality-07.json :: dataList[id=1071004].levelList[level=3].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [BeforeUse], [NightPathfinding], [StartBattle], [WhenUse], [Sinking], [EndBattle]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [BeforeUse] = [사용전] / [Before Use]; [NightPathfinding] = 듀라한 / Dullahan; [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [DuelCounter]\n<style="highlight">[BeforeUse] If this unit has [NightPathfinding] and has 15+ SP, use 'Lament, Mourn, and Despair' as Counter (once per turn)</style>\n[StartBattle] If this unit does not have [NightPathfinding], gain 1 [NightPathfinding] next turn (once per turn)\n<style="highlight">[WhenUse] If target has 6+ [Sinking], Coin Power +1</style>\n[EndBattle] If this unit has [NightPathfinding], lose [NightPathfinding]
   PL:
757. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[BeforeUse] [NightPathfinding]이 있고 정신력이 15 이상이면, '비탄하고, 애탄하며, 파탄하라'로 반격함 (턴 당 1회 발동)\n[StartBattle] [NightPathfinding]이 없으면, 다음 턴에 [NightPathfinding]을 1 얻음 (턴 당 1회 발동)\n[WhenUse] 대상의 [Sinking] <style="highlight">3 당</style> 코인 위력 +1 <style="highlight">(최대 2)</style>\n<style="highlight">[WinDuel] (합 횟수/ 3)만큼 다음 턴에 [AttackUp]를 얻음 (최대 3, 턴 당 1회 발동)</style>\n[EndBattle] [NightPathfinding]이 있으면 제거함
   źródło: Skills_personality-07.json :: dataList[id=1071004].levelList[level=4].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [BeforeUse], [NightPathfinding], [StartBattle], [WhenUse], [Sinking], [WinDuel], [AttackUp], [EndBattle]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [BeforeUse] = [사용전] / [Before Use]; [NightPathfinding] = 듀라한 / Dullahan; [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]; [AttackUp] = 공격 레벨 증가 / Offense Level Up …
   EN: [DuelCounter]\n[BeforeUse] If this unit has [NightPathfinding] and has 15+ SP, use 'Lament, Mourn, and Despair' as Counter (once per turn)\n[StartBattle] If this unit does not have [NightPathfinding], gain 1 [NightPathfinding] next turn (once per turn)\n[WhenUse] <style="highlight">Coin Power +1 for every 3 [Sinking] on target (max 2)</style>\n<style="highlight">[WinDuel] Gain [AttackUp] next turn equal to (# of Clashes/3) (max 3, once per turn)</style>\n[EndBattle] If this unit has [NightPathfinding], lose [NightPathfinding]
   PL:
758. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여<style="highlight">, 침잠 횟수 1 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071004].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] <style="highlight">and +1 [Sinking] Count</style>
   PL:
759. [Obrona (ulepszenia 3–4) — nazwa] 비탄하고, 애탄하며, 파탄하라
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].name ; dataList[id=1071006].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: kontra · moc bazowa: 31 · monety: 2 (−13)
   (powtórzenie elementu 741 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [Obrona (ulepszenie 3) — opis] [WhenUse] 정신력 15 감소\n[WhenUse] 대상의 [Sinking] 5 당 기본 위력 +1 (최대 2)\n[WhenUse] 자신의 정신력이 낮을수록 피해량이 증가 (정신력 1당 +0.3%, 최대 21%)\n자신의 [Coffin] 1당 피해량 +7% (최대 70%)\n자신의 [NightPathfinding] 1당 피해량 +10% (최대 30%)\n[WhenUse] [Coffin] 1 얻음\n[EndSkill] 이 스킬 공격으로 대상 처치시 [Coffin] 2 얻음\n[EndSkill] 정신력이 0 미만이면, 정신력 10 회복. 정신력이 0보다 낮을수록 회복량 증가 (차이 1당 1 회복, 최대 25)\n[EndBattle] [NightPathfinding] 제거
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Obrona (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여, [Sinking] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 743 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Obrona (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상 입힘
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 744 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Obrona (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 우울 속성 피해를 줌 (최대 15)
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 745 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Obrona (ulepszenie 3) — moneta 2, efekt 2 — opis] [EnemyKill] 처치한 대상의 ([Sinking] / 3)만큼 무작위 적 2명에게 [Sinking] 부여 (최대 4)
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 746 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Obrona (ulepszenia 3–4) — moneta 2, efekt 3 — opis] [EnemyKill] 정신력 15 회복
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=1071006].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 747 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Obrona (ulepszenie 4) — opis] [WhenUse] 정신력 15 감소\n[WhenUse] 대상의 [Sinking] 5 당 기본 위력 +1 (최대 <style="highlight">4</style>)\n[WhenUse] 자신의 정신력이 낮을수록 피해량이 증가 (정신력 1당 +0.3%, 최대 21%)\n자신의 [Coffin] 1당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">100</style>%)\n자신의 [NightPathfinding] 1당 피해량 +<style="highlight">20</style>% (최대 <style="highlight">60</style>%)\n[WhenUse] [Coffin] <style="highlight">2</style> 얻음\n[EndSkill] 이 스킬 공격으로 대상 처치시 [Coffin] <style="highlight">3</style> 얻음\n[EndSkill] 정신력이 0 미만이면, 정신력 10 회복. 정신력이 0보다 낮을수록 회복량 증가 (차이 1당 <style="highlight">2</style> 회복, 최대 <style="highlight">50</style>)\n[EndBattle] [NightPathfinding] 제거
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=4].desc
   (powtórzenie elementu 748 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">5</style> 부여, [Sinking] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [Obrona (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 <style="highlight">30</style>%만큼 흐트러짐 손상 입힘
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 750 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 우울 속성 피해를 줌 (최대 <style="highlight">30</style>)
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 751 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Obrona (ulepszenie 4) — moneta 2, efekt 2 — opis] [EnemyKill] 처치한 대상의 ([Sinking] / <style="highlight">2</style>)만큼 무작위 적 2명에게 [Sinking] 부여 (최대 <style="highlight">8</style>)
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 752 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Pasywka bojowa (od ulepszenia 1) — nazwa] 듀라한
   źródło: Passives.json :: dataList[id=1071002].name
   limit: do 40 znaków
   EN: Dullahan
   PL:
772. [Pasywka bojowa (od ulepszenia 1) — opis] - 턴 시작 시 [NightPathfinding]이 있을 때, [NightPathfinding]에 탑승함\n- [NightPathfinding]에 탑승할 때마다 정신력 5 소모\n- 전투 중 사망한 아군이 3명 이상이면, 다음 턴에 [NightPathfinding]을 얻음. (전투당 1번)\n- [NightPathfinding]에 탑승할 때, 피해나 흐트러짐 손상으로 흐트러짐 상태가 된 경우, 흐트러짐 상태를 해제함. 해제할 수 없는 흐트러짐 상태인 경우, [NightPathfinding]에 탑승할 수 없음.\n- 대상 처치 시 관 1 얻음
   źródło: Passives.json :: dataList[id=1071002].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n, [NightPathfinding]
   znaczenie tagów: [NightPathfinding] = 듀라한 / Dullahan
   EN: - Turn Start: if this unit has [NightPathfinding], mount [NightPathfinding].\n- Lose 5 SP every time this unit mounts [NightPathfinding]\n- If 3+ allies have been defeated in this Encounter, gain [NightPathfinding] next turn. (once per Encounter)\n- If this unit gets Staggered due to damage or raised Stagger Threshold when mounting [NightPathfinding], recover from Stagger. If the Stagger is something that cannot be naturally recovered from, this unit does not mount [NightPathfinding].\n\n- Gain 1 Coffin when killing the target.
   PL:
773. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — nazwa] 마왕의 부름
   źródło: Passives.json :: dataList[id=1071001].name
   limit: do 40 znaków
   EN: Call of the Erlking
   PL:
774. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — opis] - 대상의 [Sinking] 1당 피해량 +1% (최대 15%)
   źródło: Passives.json :: dataList[id=1071001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: - Deal +1% damage for every 1 [Sinking] on target (max 15%)
   PL:
775. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — podsumowanie] 대상의 [Sinking]당 피해량이 증가
   źródło: Passives.json :: dataList[id=1071001].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Deal more damage based on [Sinking] on target
   PL:
776. [Pasywka bojowa (od ulepszenia 3, posiadane 5× Envy) — nazwa] 마왕의 부름
   źródło: Passives.json :: dataList[id=1071011].name
   (powtórzenie elementu 773 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Pasywka bojowa (od ulepszenia 3, posiadane 5× Envy) — opis] - 대상의 [Sinking] 1당 피해량 +1% (최대 15%)\n\n<style="highlight">- 전투 중 아군 1명이 사망에 이르는 피해를 받았을 때, 관 2를 소모하여 [WildHunt]를 부여 (턴 당 1회)\n\n- 다음 턴에 [WildHunt]를 부여한 인격에게 [AttackDmgUp] 2 부여\n- 워더링하이츠, 에드가 가문 소속이면, 다음 턴에 [Enhancement] 1 추가 부여</style>
   źródło: Passives.json :: dataList[id=1071011].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Sinking], [WildHunt], [AttackDmgUp], [Enhancement]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [WildHunt] = 와일드헌트 / Wild Hunt; [AttackDmgUp] = 피해량 증가 / Damage Up; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: - Deal +1% damage for every 1 [Sinking] on target (max 15%)\n\n<style="highlight">- When, during combat, 1 ally takes damage that would kill them, consume 2 Coffin to apply [WildHunt] to them (once per turn)\n\n- Apply 2 [AttackDmgUp] next turn to the ally that has [WildHunt]\n- If the said ally is from Wuthering Heights or Edgar Family, apply 1 [Enhancement] next turn as well</style>
   PL:
778. [Pasywka bojowa (od ulepszenia 3, posiadane 5× Envy) — podsumowanie] 대상의 [Sinking]당 피해량이 증가
   źródło: Passives.json :: dataList[id=1071011].summary
   (powtórzenie elementu 775 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Envy) — nazwa] 마왕의 부름
   źródło: Passives.json :: dataList[id=1071012].name
   (powtórzenie elementu 773 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Envy) — opis] - 대상의 [Sinking] 1당 피해량 +1% (최대 15%)\n\n- 전투 중 아군 1명이 사망에 이르는 피해를 받았을 때, 관 2를 소모하여 [WildHunt]를 부여 (턴 당 <style="highlight">2</style>회)\n\n- 다음 턴에 [WildHunt]를 부여한 인격에게 [AttackDmgUp] 2 부여\n- 워더링하이츠, 에드가 가문 소속이면, 다음 턴에 [Enhancement] 1 추가 부여
   źródło: Passives.json :: dataList[id=1071012].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Sinking], [WildHunt], [AttackDmgUp], [Enhancement]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [WildHunt] = 와일드헌트 / Wild Hunt; [AttackDmgUp] = 피해량 증가 / Damage Up; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: - Deal +1% damage for every 1 [Sinking] on target (max 15%)\n\n- When, during combat, 1 ally takes damage that would kill them, consume 2 Coffin to apply [WildHunt] to them (<style="highlight">2 times</style> per turn)\n\n- Apply 2 [AttackDmgUp] next turn to the ally that has [WildHunt]\n- If the said ally is from Wuthering Heights or Edgar Family, apply 1 [Enhancement] next turn as well
   PL:
781. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Envy) — podsumowanie] 대상의 [Sinking]당 피해량이 증가
   źródło: Passives.json :: dataList[id=1071012].summary
   (powtórzenie elementu 775 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — nazwa] 울고 또 울어라
   źródło: Passives.json :: dataList[id=1071021].name
   limit: do 40 znaków
   EN: Endless Lamentation
   PL:
783. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — opis] 정신력이 가장 높은 아군 1명이 정신력이 0 미만인 대상에게 입히는 피해량 +5%\n대상의 정신력이 0보다 낮을수록 입히는 피해량이 증가 (정신력 1당 +0.5%, 최대 20%)\n대상에게 정신력이 없는 경우, 대신 공격 스킬의 스킬, 코인 효과로 부여하는 [Sinking] 위력, 횟수 부여량 +1 (턴 당 최대 2회)
   źródło: Passives.json :: dataList[id=1071021].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: 1 ally that has the highest SP deals +5% damage to targets that have less than 0 SP\nIf the target has less than 0 SP: Deal even more damage the further the target's SP is from 0 (+0.5% damage per SP, max 20%)\nFor targets that are Non-SP Units, the said ally inflicts +1 more [Sinking] Potency and Count using their Skill and Coin Effects of their Attack Skills (2 times per turn)
   PL:
784. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — podsumowanie] 정신력이 0 미만인 대상에게 입히는 피해량이 증가
   źródło: Passives.json :: dataList[id=1071021].summary
   limit: do 120 znaków
   EN: Deal more damage to targets with less than 0 SP
   PL:
785. [Kwestia głosowa [get_10710_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=get_10710_1].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Kwestia głosowa [get_10710_1] (Identity Acquisition)] 다시 돌아왔다. 캐서린과… 그 찢어 발겨놓을 저택 놈들을 마주하러.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=get_10710_1].dlg
   limit: do 120 znaków
   EN: I have returned once again. To face Catherine... and the accursed wretches of the manor.
   PL:
787. [Kwestia głosowa [lobby_morning_10710_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=lobby_morning_10710_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [Kwestia głosowa [lobby_morning_10710_1] (Morning Greeting)] 숲의 아침은 일찍 시작된다… 악몽을 꾸고 일어났을 때는 특히, 더. 항상 캐서린이 사라져버리는 악몽을 꾼다. 나는, 항상…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=lobby_morning_10710_1].dlg
   limit: do 200 znaków
   EN: I stir awake early to the morning of the forest. Especially as the sun rises over a nightmare; in that nightmare, Catherine... fades away. And always, I...
   PL:
789. [Kwestia głosowa [lobby_noon_10710_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=lobby_noon_10710_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Kwestia głosowa [lobby_noon_10710_1] (Afternoon Greeting)] 지금쯤인가… 그 연약한 도련님이 점심 홍차를 대접받고 있겠군. 큭큭… 물어뜯긴 한쪽 팔이 제법 불편할테지?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=lobby_noon_10710_1].dlg
   limit: do 210 znaków
   EN: They must be serving that milksop 'Young Master' a cup of luncheon black tea by now. Heh heh... I'm sure the stump of his arm I mauled off his torso... aches.
   PL:
791. [Kwestia głosowa [lobby_night_10710_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=lobby_night_10710_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Kwestia głosowa [lobby_night_10710_1] (Evening Greeting)] 저녁 만찬에 초대되어본 적은 없지만, 캐서린이 내게 만찬장의 음식을 들고 찾아와주곤 했었지.\n…이제 와서는 전부 부질없는, 옛 기억일 뿐이지만.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=lobby_night_10710_1].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Though they have never once invited me to their dinner banquets, Catherine would always visit me with food she took from the kitchen.\n... All meaningless recollections of the bygone days, now.
   PL:
793. [Kwestia głosowa [smalltalk_10710_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=smalltalk_10710_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [Kwestia głosowa [smalltalk_10710_1] (Chatter #1)] 잘 됐군, 시계라… 곧 '약속'시간이 올테니, 거기에 참고하기 딱 좋겠어. 캐서린은 예전부터 기다리는 걸 딱 질색해 했으니까.\n…이렇게 변해버린 나를 정말로 환대할 수 있을 지는 모르겠지만.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=smalltalk_10710_1].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A timepiece, is it? Good. The 'promised' hour is nigh... I shall keep you in my sight. Patience was never Catherine's strong suit, after all.\n... Yet I do not know if she could bring herself to welcome me when I have changed so much.
   PL:
795. [Kwestia głosowa [smalltalk_10710_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=smalltalk_10710_2].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Kwestia głosowa [smalltalk_10710_2] (Chatter #2)] 이 곳은 숲치곤 고요하지… 근방의 것들은 모조리 먹어치웠으니까.\n그런 고요함 안에 있으면, 불현듯… 캐서린이 떠오르고… 곧이어 겉잡을 수 없이 가라앉는다.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=smalltalk_10710_2].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This place is rather silent for a forest, isn't it...? That is because I have made all living things here mine.\nIn that silence, memories of Catherine return... and I begin to sink like a rock.
   PL:
797. [Kwestia głosowa [smalltalk_10710_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=smalltalk_10710_3].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Kwestia głosowa [smalltalk_10710_3] (Chatter #3)] 어릴 적엔 나를 돌보던 녀석이 있었지… 언제나 이렇게 마주하게 되는군.\n하지만 마지막에는 처음과 반대로 내가 거둬들여주지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=smalltalk_10710_3].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There once was a woman who cared for me in my youth. Yet here I stand, soon to test my blade against her own.\nBut this time, I shall take her under my fold as she had done for me.
   PL:
799. [Kwestia głosowa [smalltalk_10710_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=smalltalk_10710_4].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Kwestia głosowa [smalltalk_10710_4] (Post-Uptie Chat 1)] 핫, 거의 쾌락에 맞닿아 있지 않은가! 이 분노에 몸을 맡기는 시간이!\n너도, 나도 아무런 생각을 할 필요가 없지. 그저 폭풍우가 치는 이 언덕 위에서 결판을 내는 거다!\n마지막에 누가 절벽 위에 서 있을지 궁금하군.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=smalltalk_10710_4].dlg
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hah, do you feel the intense rapture of letting the fury take hold?!\nRuminations of all kinds have no purpose here; not for you, not for me. All that remains is to settle this once and for all here, atop the storm-broken heights!\nWho shall remain standing here once it passes, I wonder.
   PL:
801. [Kwestia głosowa [smalltalk_10710_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=smalltalk_10710_5].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Kwestia głosowa [smalltalk_10710_5] (Post-Uptie Chat 2)] 나의 분노가 향하는 곳은 확실하다. 그 무엇보다… 강력한 내 삶의 동기, 동력이지.\n내 가슴까지 찢어발긴 너와… 그 만남의 씨앗이 되었던 워더링하이츠의 완벽한 몰락을 보고 말테다!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=smalltalk_10710_5].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The keen end of my wrath-blade aims true. It is the greatest fuel to my flame of existence.\nI shall bring utter ruination to you, who have broken my heart... and Wuthering Heights, the cradle of our meeting!
   PL:
803. [Kwestia głosowa [neglect_10710_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=neglect_10710_1].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Kwestia głosowa [neglect_10710_1] (Idle)] …내 캐서린이 세상을 떠난 날, 나도 죽은 것과 마찬가지였다.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=neglect_10710_1].dlg
   limit: do 120 znaków
   EN: ... My life ended the day my Catherine departed the world.
   PL:
805. [Kwestia głosowa [gacksung_10710_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=gacksung_10710_1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [Kwestia głosowa [gacksung_10710_1] (Uptying)] 약속한 만찬의 날이자 사냥의 날이 왔다. 털끝의 감각만으로도 알 수 있지. 오늘… 워더링하이츠가 갈기갈기 찢어지게 될 것이라는 걸.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=gacksung_10710_1].dlg
   limit: do 200 znaków
   EN: The dawn of the promised banquet, the day of the hunt rises. I can feel it even at the tip of my hair... that the destruction of Wuthering Heights is nigh.
   PL:
807. [Kwestia głosowa [formation_10710_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=formation_10710_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Kwestia głosowa [formation_10710_1] (Deployment)] 이 소리는… 폭풍인가… 마치 캐서린이 울부짖는 것 같군…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=formation_10710_1].dlg
   limit: do 120 znaków
   EN: This howling noise... must be the tempest. Catherine, she weeps...
   PL:
809. [Kwestia głosowa [battleentry_10710_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battleentry_10710_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Kwestia głosowa [battleentry_10710_1] (Stage Entry)] 와일드헌트여…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battleentry_10710_1].dlg
   limit: do 120 znaków
   EN: O Wild Hunt...
   PL:
811. [Kwestia głosowa [battle_select_10710_1] — sytuacja] 전투 중 인격 선택 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_select_10710_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle 1
   PL:
812. [Kwestia głosowa [battle_select_10710_1] (Viewed in Battle 1)] (광기에 찬 웃음소리)
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_select_10710_1].dlg
   limit: do 120 znaków
   EN: (Mad Laughter)
   PL:
813. [Kwestia głosowa [battle_select_10710_2] — sytuacja] 전투 중 인격 선택 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_select_10710_2].desc
   limit: do 120 znaków
   EN: Viewed in Battle 2
   PL:
814. [Kwestia głosowa [battle_select_10710_2] (Viewed in Battle 2)] (광기에 찬 웃음소리)
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_select_10710_2].dlg
   (powtórzenie elementu 812 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Kwestia głosowa [battle_select_10710_3] — sytuacja] 전투 중 인격 선택 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_select_10710_3].desc
   limit: do 120 znaków
   EN: Viewed in Battle 3
   PL:
816. [Kwestia głosowa [battle_select_10710_3] (Viewed in Battle 3)] (광기에 찬 웃음소리)
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_select_10710_3].dlg
   (powtórzenie elementu 812 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Kwestia głosowa [battle_endcommand_10710_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_endcommand_10710_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Kwestia głosowa [battle_endcommand_10710_1] (Commencing Attack)] 목을 내놓고 있도록…!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_endcommand_10710_1].dlg
   limit: do 120 znaków
   EN: ... Prepare for your execution...!
   PL:
819. [Kwestia głosowa [battle_enemy_break_10710_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_enemy_break_10710_1].desc
   limit: do 120 znaków
   EN: Enemy Staggered
   PL:
820. [Kwestia głosowa [battle_enemy_break_10710_1] (Enemy Staggered)] 폭풍 속에서…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_enemy_break_10710_1].dlg
   limit: do 120 znaków
   EN: In the tempest...
   PL:
821. [Kwestia głosowa [battle_break_10710_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_break_10710_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
822. [Kwestia głosowa [battle_break_10710_1] (Staggered)] 계속 해봐라! 이 폭풍이 잦아들 때까지!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_break_10710_1].dlg
   limit: do 120 znaków
   EN: Again! Again and again, until the storm sleeps!
   PL:
823. [Kwestia głosowa [battle_kill_10710_1] — sytuacja] 적 처치 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_kill_10710_1].desc
   limit: do 120 znaków
   EN: On Kill 1
   PL:
824. [Kwestia głosowa [battle_kill_10710_1] (On Kill 1)] 파묻혀 잠들어라.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_kill_10710_1].dlg
   limit: do 120 znaków
   EN: ... You shall slumber in burial.
   PL:
825. [Kwestia głosowa [battle_kill_10710_2] — sytuacja] 적 처치 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_kill_10710_2].desc
   limit: do 120 znaków
   EN: On Kill 2
   PL:
826. [Kwestia głosowa [battle_kill_10710_2] (On Kill 2)] 비명을 질러라.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_kill_10710_2].dlg
   limit: do 120 znaków
   EN: ... You shall scream.
   PL:
827. [Kwestia głosowa [battle_kill_10710_3] — sytuacja] 적 처치 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_kill_10710_3].desc
   limit: do 120 znaków
   EN: On Kill 3
   PL:
828. [Kwestia głosowa [battle_kill_10710_3] (On Kill 3)] 찢어놓아주마.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_kill_10710_3].dlg
   limit: do 120 znaków
   EN: ... You shall be torn apart.
   PL:
829. [Kwestia głosowa [battle_dead_10710_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_dead_10710_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [Kwestia głosowa [battle_dead_10710_1] (Death)] 죽어도… 나는… 다시…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_dead_10710_1].dlg
   limit: do 120 znaków
   EN: Even in death... I... shall...
   PL:
831. [Kwestia głosowa [choice_success_p_10710_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=choice_success_p_10710_2].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [Kwestia głosowa [choice_success_p_10710_2] (Check Passed)] 사냥을 위해서라면…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=choice_success_p_10710_2].dlg
   limit: do 120 znaków
   EN: For the hunt...
   PL:
833. [Kwestia głosowa [choice_fail_n_10710_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=choice_fail_n_10710_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Kwestia głosowa [choice_fail_n_10710_1] (Check Failed)] 사냥이 실패했군… 또 다시 발톱을 날카롭게 갈아낼 뿐이다.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=choice_fail_n_10710_1].dlg
   limit: do 120 znaków
   EN: The hunt has failed... no matter. This pain will only hone my claws.
   PL:
835. [Kwestia głosowa [battle_clear_10710_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_clear_10710_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [Kwestia głosowa [battle_clear_10710_1] (Victory Cry)] 아직, 아직 완전하지 않다. 와일드헌트여, 더 앞으로! 캐서린에게 내 사랑의 절규가 닿을 때까지…!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_clear_10710_1].dlg
   limit: do 130 znaków
   EN: No, it is yet incomplete. My Wild Hunt, march forth! Until my cry of love reaches Catherine...!
   PL:
837. [Kwestia głosowa [battle_clear_ex_10710_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_clear_ex_10710_1].desc
   limit: do 120 znaków
   EN: Extra Condition Fulfilled
   PL:
838. [Kwestia głosowa [battle_clear_ex_10710_1] (Extra Condition Fulfilled)] 끝장냈어! 이제 더는 폭풍 소리에 치를 떨 필요도, 캐서린의 꿈을 꾸고 슬픔에 빠질 필요도 없지! 전부, 전부… 끝내버린… 건가?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_clear_ex_10710_1].dlg
   limit: do 220 znaków
   EN: It is done! I will no longer tremble in the wuthering storm, no longer suffer Catherine's dream to suffocate me in grief, nevermore! I have...! I... I ended it... didn't I?
   PL:
839. [Kwestia głosowa [battle_defeat_10710_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_defeat_10710_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Kwestia głosowa [battle_defeat_10710_1] (Defeat Wail)] 우스운 꼬락서니군… 상관 없다. 나는 다시 돌아온다. 워더링하이츠를 통째로 씹어먹을 그 순간까지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Erlking_10710.json :: dataList[id=battle_defeat_10710_1].dlg
   limit: do 190 znaków
   EN: What a sorry mess this is... no matter. I will return. I will return again and again until the day I crush Wuthering Heights between my teeth.
   PL:

## [000] Full-Stop Office Fixer — Heathcliff — 마침표 사무소 해결사
- ID Tożsamości: `10711` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9105 · HP bazowe: 70 · szybkość: 3–6 / 3–6 / 3–8 / 3–8
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Poise

841. [Karta Tożsamości — tytuł] 마침표 사무소\n해결사
   źródło: Personalities.json :: dataList[id=10711].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Full-Stop Office\nFixer
   PL:
842. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10711].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10711].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Karta Tożsamości — opis] 히스클리프의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10711].desc
   limit: do 120 znaków
   EN: Heathcliff’s 11th Identity
   PL:
845. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 응사
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=1].name ; dataList[id=1071101].levelList[level=2].name ; dataList[id=1071101].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Return Fire
   PL:
846. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL:
847. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend 1 [Bullet]
   PL:
848. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 847 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 847 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
850. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가\n<style="highlight">[WhenUse] 다음 턴에 [Agility] 1 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: [WhenUse] Gain +2 [Breath] Count\n<style="highlight">[WhenUse] Gain 1 [Agility] next turn (once per turn)</style>
   PL:
851. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1071101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend 1 [Bullet]<style="highlight"></style>
   PL:
852. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 [Breath] 횟수 1 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: <style="highlight">[OnSucceedAttack] Gain +1 [Breath] Count</style>
   PL:
853. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1071101].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가\n[WhenUse] 다음 턴에 [Agility] <style="highlight">2</style> 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: [WhenUse] Gain +2 [Breath] Count\n[WhenUse] Gain <style="highlight">2</style> [Agility] next turn (once per turn)
   PL:
856. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count<style="highlight"></style>
   PL:
857. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 헤드샷
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=1].name ; dataList[id=1071102].levelList[level=2].name ; dataList[id=1071102].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 10 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Headshot
   PL:
858. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [Breath] 3 얻음. 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 3 [Breath] and +1 [Breath] Count
   PL:
859. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 847 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [PenetrateTakeDamageUp] 1 부여 (턴 당 2회)
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [OnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] (2 times per turn)
   PL:
861. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1 당 피해량 +10% (최대 30%)</style>\n[WhenUse] [Breath] 3 얻음. 자신의 [Breath] 횟수 1 증가\n<style="highlight">[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: <style="highlight">If this unit's Speed is faster than the target's, deal +10% damage for every 1 Speed difference (max 30%)</style>\n[WhenUse] Gain 3 [Breath] and +1 [Breath] Count\n<style="highlight">[WhenUse] Gain 2 [Agility] next turn (once per turn)</style>
   PL:
862. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1071102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">크리티컬 피해량 +30%</style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+30% Damage on Critical Hit</style>
   PL:
864. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [PenetrateTakeDamageUp] 1 부여 (턴 당 2회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=2].coinlist[#0].coindescs[#2].desc ; dataList[id=1071102].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [OnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] (2 times per turn)<style="highlight"></style>
   PL:
865. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 4 — opis] <style="highlight">[CriticalOnSucceedAttack] 다음 턴에 [PenetrateTakeDamageUp] 1 부여 (턴 당 1회)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=2].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] next turn (once per turn)</style>
   PL:
866. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1 당 피해량 +10% <style="highlight">(최대 50%)</style>\n[WhenUse] [Breath] 3 얻음. 자신의 [Breath] 횟수 <style="highlight">2</style> 증가\n[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: If this unit's Speed is faster than the target's, deal +10% damage for every 1 Speed difference <style="highlight">(max 50%)</style>\n[WhenUse] Gain 3 [Breath] and +<style="highlight">2</style> [Breath] Count\n[WhenUse] Gain 2 [Agility] next turn (once per turn)
   PL:
867. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] 크리티컬 피해량 <style="highlight">+50%</style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+50%</style> Damage on Critical Hit
   PL:
868. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] 다음 턴에 [PenetrateTakeDamageUp] 1 부여 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [CriticalOnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] next turn (once per turn)<style="highlight"></style>
   PL:
869. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 한 점만 노린다
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=3].name ; dataList[id=1071103].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 12 · monety: 1 (+14)
   limit: do 40 znaków
   EN: Goin' for the Bullseye
   PL:
870. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [BeforeUse] 자신에게 [Bullet_LogicAtelier]가 있으면, '로직 아틀리에제 고속분쇄탄'으로 발동\n대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1 당 피해량 +10% (최대 50%)\n[WhenUse] [Breath] 5 얻음\n[WhenUse] [LogicAtelierAM]을 전부 소모하여 (소모한 수치 x 2)만큼 호흡 위력을 얻고, 피해량 +(소모한 수치 x 12.5)%
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=3].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [Bullet_LogicAtelier], [WhenUse], [Breath], [LogicAtelierAM]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [Bullet_LogicAtelier] = 탄환 - 로직 아틀리에 / Ammo - Atelier Logic; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】
   EN: [BeforeUse] If this unit has [Bullet_LogicAtelier], activate 'AL-HV Pulverisation Round' instead\nIf this unit's Speed is faster than the target's, deal +10% damage for every 1 Speed difference (max 50%)\n[WhenUse] Gain 5 [Breath]\n[WhenUse] Consume all [LogicAtelierAM] on self, gain (value consumed x 2) Poise Potency, and deal +(value consumed x 12.5)% damage
   PL:
871. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 847 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
872. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +50%
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: +50% Damage on Critical Hit
   PL:
873. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 자신의 [Breath] 위력이 30을 초과하면, 30을 초과하는 [Breath] 위력을 최대 10까지 소모하여 피해량 +(소모한 [Breath] 위력 x 10)%
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] At more than 30 [Breath] Potency, consume up to 10 of [Breath] Potency over 30 to deal +([Breath] Potency consumed x 10)% damage
   PL:
874. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [BeforeUse] 자신에게 [Bullet_LogicAtelier]가 있으면, '로직 아틀리에제 고속분쇄탄'으로 발동\n대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1 당 피해량 +10% (최대 50%)\n[WhenUse] [Breath] 5 얻음\n[WhenUse] [LogicAtelierAM]을 전부 소모하여 (소모한 수치 x 2)만큼 호흡 위력을 얻고, 피해량 +(소모한 수치 x 12.5)%\n<style="highlight">[EndSkill] 자신의 [Breath] 횟수 2 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeUse], [Bullet_LogicAtelier], [WhenUse], [Breath], [LogicAtelierAM], [EndSkill]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [Bullet_LogicAtelier] = 탄환 - 로직 아틀리에 / Ammo - Atelier Logic; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeUse] If this unit has [Bullet_LogicAtelier], activate 'AL-HV Pulverisation Round' instead\nIf this unit's Speed is faster than the target's, deal +10% damage for every 1 Speed difference (max 50%)\n[WhenUse] Gain 5 [Breath]\n[WhenUse] Consume all [LogicAtelierAM] on self, gain (value consumed x 2) Poise Potency, and deal +(value consumed x 12.5)% damage\n<style="highlight">[EndSkill] Gain +2 [Breath] Count</style>
   PL:
875. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
876. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] 크리티컬 피해량 <style="highlight">+80%</style>
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+80%</style> Damage on Critical Hit
   PL:
877. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] <style="highlight">크리티컬 피해량 +(대상의 관통 내성 x 50)%</style>
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+(target's Pierce Res. x 50)% Damage on Critical Hit</style>
   PL:
878. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] 자신의 [Breath] 위력이 30을 초과하면, 30을 초과하는 [Breath] 위력을 최대 10까지 소모하여 피해량 +(소모한 [Breath] 위력 x 10)%<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] At more than 30 [Breath] Potency, consume up to 10 of [Breath] Potency over 30 to deal +([Breath] Potency consumed x 10)% damage<style="highlight"></style>
   PL:
879. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 로직 아틀리에제 고속분쇄탄
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=3].name ; dataList[id=1071105].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 15 · monety: 1 (+18)
   limit: do 40 znaków
   EN: AL-HV Pulverisation Round
   PL:
880. [Umiejętność 4 (×0) (ulepszenie 3) — opis] 대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1당 피해량 +10% (최대 50%)\n[WhenUse] [Breath] 5 얻음\n[WhenUse] [LogicAtelierAM]을 전부 소모하여, (소모한 수치 x 2)만큼 [Breath] 위력을 얻고, 피해량 +(소모한 수치 x 25)%
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=3].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [LogicAtelierAM]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】
   EN: If this unit's Speed is faster than the target's, deal +10% damage for every 1 Speed difference (max 50%)\n[WhenUse] Gain 5 [Breath]\n[WhenUse] Consume all [LogicAtelierAM] on self, gain (value consumed x 2) [Breath] Potency, and deal +(value consumed x 25)% damage
   PL:
881. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [Bullet_LogicAtelier] 1 소모
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet_LogicAtelier]
   znaczenie tagów: [Bullet_LogicAtelier] = 탄환 - 로직 아틀리에 / Ammo - Atelier Logic
   EN: Spend 1 [Bullet_LogicAtelier]
   PL:
882. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +100%
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: +100% Damage on Critical Hit
   PL:
883. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 자신의 [Breath] 위력이 30을 초과하면, 30을 초과하는 [Breath] 위력을 최대 10까지 소모하여 피해량 +(소모한 [Breath] 위력 x 10)%
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 873 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
884. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1당 피해량 +10% (최대 50%)\n[WhenUse] [Breath] 5 얻음\n[WhenUse] [LogicAtelierAM]을 전부 소모하여, (소모한 수치 x 2)만큼 [Breath] 위력을 얻고, 피해량 +(소모한 수치 x 25)%\n<style="highlight">[EndSkill] 자신의 [Breath] 횟수 5 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [LogicAtelierAM], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If this unit's Speed is faster than the target's, deal +10% damage for every 1 Speed difference (max 50%)\n[WhenUse] Gain 5 [Breath]\n[WhenUse] Consume all [LogicAtelierAM] on self, gain (value consumed x 2) [Breath] Potency, and deal +(value consumed x 25)% damage\n<style="highlight">[EndSkill] Gain +5 [Breath] Count</style>
   PL:
885. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [Bullet_LogicAtelier] 1 소모<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet_LogicAtelier]
   znaczenie tagów: [Bullet_LogicAtelier] = 탄환 - 로직 아틀리에 / Ammo - Atelier Logic
   EN: Spend 1 [Bullet_LogicAtelier]<style="highlight"></style>
   PL:
886. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] 크리티컬 피해량 <style="highlight">+130%</style>
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+130%</style> Damage on Critical Hit
   PL:
887. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] <style="highlight">크리티컬 피해량 +(대상의 관통 내성 x 50)%</style>
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 877 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
888. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] 자신의 [Breath] 위력이 30을 초과하면, 30을 초과하는 [Breath] 위력을 최대 10까지 소모하여 피해량 +(소모한 [Breath] 위력 x 10)%<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=4].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 878 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [Obrona (ulepszenia 1,4) — nazwa] 전투 호흡
   źródło: Skills_personality-07.json :: dataList[id=1071104].levelList[level=1].name ; dataList[id=1071104].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Combat Poise
   PL:
890. [Obrona (ulepszenie 1) — opis] 턴 시작시 탄환이 0이면 '엄폐'로 변경됨\n[WhenUse] 마침표 사무소 대표 홍루 인격이 전투에 등장해 있으면, 대상에게 [MeleeCover] 요청 (턴 당 1회)\n[EndBattle] 다음 턴에 [LogicAtelierAM] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071104].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [MeleeCover], [EndBattle], [LogicAtelierAM]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [MeleeCover] = 근접 지원 / Melee Support; [EndBattle] = [턴 종료 시] / [Turn End]; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】
   EN: Turn Start: At 0 Ammo, this Skill activates as 'Taking Cover' instead\n[WhenUse] If Full-Stop Office Rep. Hong Lu is on the field, request [MeleeCover] from that unit (once per turn)\n[EndBattle] Gain 1 [LogicAtelierAM] next turn (once per turn)
   PL:
891. [Obrona (ulepszenie 4) — opis] 턴 시작시 탄환이 0이면 '엄폐'로 변경됨\n[WhenUse] 마침표 사무소 대표 홍루 인격이 전투에 등장해 있으면, 대상에게 [MeleeCover] 요청 (턴 당 1회)\n<style="highlight">[OnSucceedEvade] [Breath] 3 얻음 (턴 당 최대 3회)</style>\n[EndBattle] 다음 턴에 [LogicAtelierAM] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071104].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [MeleeCover], [OnSucceedEvade], [Breath], [EndBattle], [LogicAtelierAM]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [MeleeCover] = 근접 지원 / Melee Support; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise; [EndBattle] = [턴 종료 시] / [Turn End]; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】
   EN: Turn Start: At 0 Ammo, this Skill activates as 'Taking Cover' instead\n[WhenUse] If Full-Stop Office Rep. Hong Lu is on the field, request [MeleeCover] from that unit (once per turn)\n<style="highlight">[OnSucceedEvade] Gain 3 [Breath] (3 times per turn)</style>\n[EndBattle] Gain 1 [LogicAtelierAM] next turn (once per turn)
   PL:
892. [Obrona (ulepszenia 1,4) — nazwa] 엄폐
   źródło: Skills_personality-07.json :: dataList[id=1071106].levelList[level=1].name ; dataList[id=1071106].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 2 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Taking Cover
   PL:
893. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[WhenUse] 마침표 사무소 대표 홍루 인격이 전투에 등장해 있으면, 대상에게 [MeleeCover] 요청 (턴 당 1회)\n[EndBattle] 다음 턴에 [LogicAtelierAM] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071106].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WhenUse], [MeleeCover], [EndBattle], [LogicAtelierAM]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [MeleeCover] = 근접 지원 / Melee Support; [EndBattle] = [턴 종료 시] / [Turn End]; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】
   EN: [CanDuelGuard]\n[WhenUse] If Full-Stop Office Rep. Hong Lu is on the field, request [MeleeCover] from that unit (once per turn)\n[EndBattle] Gain 1 [LogicAtelierAM] next turn (once per turn)
   PL:
894. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071106].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1071106].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL:
895. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[WhenUse] 마침표 사무소 대표 홍루 인격이 전투에 등장해 있으면, 대상에게 [MeleeCover] 요청 (턴 당 1회)\n<style="highlight">[WinDuel] 대상에게 [PenetrateResistDown] 1 부여 (턴 당 1회)</style>\n[EndBattle] 다음 턴에 [LogicAtelierAM] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071106].levelList[level=4].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [WhenUse], [MeleeCover], [WinDuel], [PenetrateResistDown], [EndBattle], [LogicAtelierAM]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [MeleeCover] = 근접 지원 / Melee Support; [WinDuel] = [합 승리시] / [Clash Win]; [PenetrateResistDown] = 관통 내성 약화 / Pierce Resist Down; [EndBattle] = [턴 종료 시] / [Turn End]; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】
   EN: [CanDuelGuard]\n[WhenUse] If Full-Stop Office Rep. Hong Lu is on the field, request [MeleeCover] from that unit (once per turn)\n<style="highlight">[WinDuel] Inflict 1 [PenetrateResistDown] (once per turn)</style>\n[EndBattle] Gain 1 [LogicAtelierAM] next turn (once per turn)
   PL:
896. [Pasywka bojowa (od ulepszenia 1) — nazwa] 저격
   źródło: Passives.json :: dataList[id=1071101].name
   limit: do 40 znaków
   EN: Snipe
   PL:
897. [Pasywka bojowa (od ulepszenia 1) — opis] 스테이지 시작시 [PenetrateResultUp] 3 얻음\n\n턴 종료시 자신의 모든 [Bullet]이 0이면, [Retreat_FullStop] (전투 당 1회)\n\n대기해제되었거나, [Retreat_FullStop] 이후 다시 전투에 참여했을 때, [LogicAtelierAM]이 최대가 되고, [PenetrateResultUp]를 3 얻고, [FullReload] ([Bullet_LogicAtelier] 제외, 전투 당 1회)
   źródło: Passives.json :: dataList[id=1071101].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [PenetrateResultUp], [Bullet], [Retreat_FullStop], [LogicAtelierAM], [FullReload], [Bullet_LogicAtelier]
   znaczenie tagów: [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [Bullet] = 탄환 / Ammo; [Retreat_FullStop] = 후방 지원 배치 / Overwatch Assignment; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】; [FullReload] = 재장전 / Reload; [Bullet_LogicAtelier] = 탄환 - 로직 아틀리에 / Ammo - Atelier Logic
   EN: Encounter Start: gain 3 [PenetrateResultUp]\n\nTurn End: If this unit does not have any remaining [Bullet] of any kind, activate [Retreat_FullStop] (once per Encounter)\n\nIf this unit is Substituted in, or is rejoining battle after [Retreat_FullStop], gain max [LogicAtelierAM], 3 [PenetrateResultUp], and [FullReload] (except [Bullet_LogicAtelier]; once per Encounter)
   PL:
898. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Pride) — nazwa] 정밀 조준
   źródło: Passives.json :: dataList[id=1071102].name
   limit: do 40 znaków
   EN: Precision Aim
   PL:
899. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Pride) — opis] 턴 종료시 자신의 [Breath] 10 당, 다음 턴에 [Agility] 1 얻음 (최대 2)\n\n턴 종료 시 이번 턴에 자신이 (E.G.O 스킬 포함, [CoveringFire] 제외) 공격 스킬을 사용하지 않았으면, 다음 턴에 [Breath] 10, [PenetrateResultUp] 1 얻음.
   źródło: Passives.json :: dataList[id=1071102].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Agility], [CoveringFire], [PenetrateResultUp]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [CoveringFire] = 타겟 포착 / Target Spotted; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up
   EN: Turn End: Gain 1 [Agility] next turn for every 10 [Breath] on self (max 2)\n\nTurn End: If this unit is not set to use any Attack Skills (including E.G.O Skills, excluding [CoveringFire]), gain 10 [Breath] and 1 [PenetrateResultUp] next turn.
   PL:
900. [Pasywka bojowa (od ulepszenia 3) — nazwa] 저격
   źródło: Passives.json :: dataList[id=1071103].name
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
901. [Pasywka bojowa (od ulepszenia 3) — opis] 스테이지 시작시 [PenetrateResultUp] 3 얻음\n\n<style="highlight">이 캐릭터가 전투에 등장할 때, [Bullet_LogicAtelier] 1 얻음 (전투 당 1회)</style>\n\n턴 종료시 자신의 모든 [Bullet]이 0이면, [Retreat_FullStop] (전투 당 1회)\n\n대기해제되었거나, [Retreat_FullStop] 이후 다시 전투에 참여했을 때, [LogicAtelierAM]이 최대가 되고, [PenetrateResultUp]를 3 얻고, [FullReload]\n([Bullet_LogicAtelier] 제외, 전투 당 1회)
   źródło: Passives.json :: dataList[id=1071103].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [PenetrateResultUp], [Bullet_LogicAtelier], [Bullet], [Retreat_FullStop], [LogicAtelierAM], [FullReload]
   znaczenie tagów: [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [Bullet_LogicAtelier] = 탄환 - 로직 아틀리에 / Ammo - Atelier Logic; [Bullet] = 탄환 / Ammo; [Retreat_FullStop] = 후방 지원 배치 / Overwatch Assignment; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】; [FullReload] = 재장전 / Reload
   EN: Encounter Start: gain 3 [PenetrateResultUp]\n\n<style="highlight">When this unit enters the Encounter, gain 1 [Bullet_LogicAtelier] (once per Encounter)</style>\n\nTurn End: If this unit does not have any remaining [Bullet] of any kind, activate [Retreat_FullStop] (once per Encounter)\n\nIf this unit is Substituted in, or is rejoining battle after [Retreat_FullStop], gain max [LogicAtelierAM], 3 [PenetrateResultUp], and [FullReload]\n(Except [Bullet_LogicAtelier]; once per Encounter)
   PL:
902. [Pasywka bojowa (od ulepszenia 4, rezonans 2× Pride) — nazwa] 정밀 조준
   źródło: Passives.json :: dataList[id=1071111].name
   (powtórzenie elementu 898 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
903. [Pasywka bojowa (od ulepszenia 4, rezonans 2× Pride) — opis] 턴 종료시 자신의 [Breath] 10 당, 다음 턴에 [Agility] 1 얻음 (최대 2)\n\n<style="highlight">전투 시작시 자신이 (E.G.O 스킬 포함) 공격 스킬을 사용할 예정이 아니면, 호흡 위력이 가장 낮은 아군 1명에게 [Breath] 3 부여</style>\n\n턴 종료 시 이번 턴에 자신이 (E.G.O 스킬 포함, [CoveringFire] 제외) 공격 스킬을 사용하지 않았으면, 다음 턴에 [Breath] 10, [PenetrateResultUp] 1 얻음
   źródło: Passives.json :: dataList[id=1071111].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [Agility], [CoveringFire], [PenetrateResultUp]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [CoveringFire] = 타겟 포착 / Target Spotted; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up
   EN: Turn End: Gain 1 [Agility] next turn for every 10 [Breath] on self (max 2)\n\n<style="highlight">Combat Start: If this unit is not set to use any Attack Skills (including E.G.O Skills), apply 3 [Breath] to 1 ally that has the least [Breath] Potency</style>\n\nTurn End: If this unit did not use any Attack Skills (including E.G.O Skills, excluding [CoveringFire]), gain 10 [Breath] and 1 [PenetrateResultUp] next turn
   PL:
904. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — nazwa] 감적수
   źródło: Passives.json :: dataList[id=1071121].name
   limit: do 40 znaków
   EN: Spotter
   PL:
905. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — opis] [Bullet]을 가장 적게 보유한 아군 1명이 [Bullet]을 소모하는 스킬을 사용할 때, [Breath] 횟수 2 증가\n- 대상이 마침표 사무소 인격이거나, 대상의 [Breath] 횟수가 5 미만이면, 대신 4 증가 (턴 당 1회. [Bullet]이 없는 대상에게는 적용되지 않음)
   źródło: Passives.json :: dataList[id=1071121].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [Breath] = 호흡 / Poise
   EN: 1 ally that has the least [Bullet] gains +2 [Breath] Count when using a Skill that consumes [Bullet].\n- If the said ally is a Full-Stop Office Identity, or if they have less than 5 [Breath] Count, gain +4 [Breath] Count instead (once per turn; does not apply to units without [Bullet])
   PL:
906. [Kwestia głosowa [get_10711_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=get_10711_1].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [Kwestia głosowa [get_10711_1] (Identity Acquisition)] 탄 일발 장전. 탄환은… 로직 아틀리에제 고속분쇄탄. 좋아, 저격 준비 끝.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=get_10711_1].dlg
   limit: do 150 znaków
   EN: Locked and loaded. Bullet type... Atelier Logic High Velocity Pulverisation Round. Right, then. Ready to fire.
   PL:
908. [Kwestia głosowa [lobby_morning_10711_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=lobby_morning_10711_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
909. [Kwestia głosowa [lobby_morning_10711_1] (Morning Greeting)] 밖은 슬슬… 아침인가? 행사가 시작되려면 아직도 한참 남았고. 하아아… 허리가 부서질 것 같네.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=lobby_morning_10711_1].dlg
   limit: do 150 znaków
   EN: Is it... morning outside? I 'spose there's still plenty of time left for the event to start. Haah... ow, my back.
   PL:
910. [Kwestia głosowa [lobby_noon_10711_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=lobby_noon_10711_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
911. [Kwestia głosowa [lobby_noon_10711_1] (Afternoon Greeting)] 아직 점심시간밖에 안 됐을텐데, 벌써부터 저녁 만찬 준비를 하는구만. 오늘 커다란 모임이 있다는 건 확실한가 보네.\n슬슬 탄환 점검을 해야겠어…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=lobby_noon_10711_1].dlg
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Already preparin' for dinner at lunchtime? Looks like somethin' big's about to go down for sure. I've got to make sure my bullets are all in fine condition...
   PL:
912. [Kwestia głosowa [lobby_night_10711_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=lobby_night_10711_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
913. [Kwestia głosowa [lobby_night_10711_1] (Evening Greeting)] 저녁 만찬이 끝나고 저 교주가 신도들에게 연설을 시작할 때… 그때가 최적의 타이밍이야. 딱 한 발이면 돼.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=lobby_night_10711_1].dlg
   limit: do 170 znaków
   EN: I'll take the shot when their leader starts the sermon before the worshippers following the dinner. It only takes one bullet.
   PL:
914. [Kwestia głosowa [smalltalk_10711_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=smalltalk_10711_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
915. [Kwestia głosowa [smalltalk_10711_1] (Chatter #1)] 이만큼 숨어들기 허술할 줄이야. 죄다 저 대갈통에 톱니를 박은 녀석한테 빠져가지곤… 처음엔 생포라길래 까다로운 의뢰겠다 싶었는데, 별거 없겠어.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=smalltalk_10711_1].dlg
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Didn't think it'd be this easy to slip by 'em. Must say, I don't quite get what it is with shoving a gear in your noggin' that leaves 'em slobberin' over your words...\nAnyway, this'll be easier than I'd expected. Thought a capture mission would be more difficult.
   PL:
916. [Kwestia głosowa [smalltalk_10711_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=smalltalk_10711_2].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
917. [Kwestia głosowa [smalltalk_10711_2] (Chatter #2)] 총을 만들 수 있는 공방은 그렇게 많지도 않고… 그걸 운용하는 사무소도 희박하지… 뭐, 그 덕에 이런 의뢰는 우리가 독식할 수 있긴 하지만.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=smalltalk_10711_2].dlg
   limit: do 250 znaków
   EN: There ain't that many Workshops out there buildin' guns... and there ain't that many Fixer Officers usin' guns... Well, I suppose that's why we don't have any trouble picking up these contracts.
   PL:
918. [Kwestia głosowa [smalltalk_10711_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=smalltalk_10711_3].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
919. [Kwestia głosowa [smalltalk_10711_3] (Chatter #3)] 톱니교단이 하는 짓이 유쾌하진 않지… 하지만 그건 그거고, 의뢰는 의뢰지. 사사롭게 총알에 감정을 담아봐야 조준만 흔들리잖냐.\n총알값도 더럽게 비싼데, 한 번에 똑바로 박아넣어야 수지가 맞는다고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=smalltalk_10711_3].dlg
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I don't like what the Church of Gear does. Of course I don't. But... that's that, and a contract's a contract. No point in gettin' too invested about it, it'll just end up messin' up my aim.\nCan't get a proper return on the investment if I don't make each shot count, given how expensive they are.
   PL:
920. [Kwestia głosowa [smalltalk_10711_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=smalltalk_10711_4].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
921. [Kwestia głosowa [smalltalk_10711_4] (Post-Uptie Chat 1)] 이런 씨… 빗맞았잖아. 무조건 대갈통에 박히는 각이었는데… 저 교주라는 인간, 어떻게 되어 먹은 거야?!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=smalltalk_10711_4].dlg
   limit: do 150 znaków
   EN: Oh bloody hell— I missed! But I had a good shot, straight for the noggin... The hell's goin' on with that 'leader'?!
   PL:
922. [Kwestia głosowa [smalltalk_10711_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=smalltalk_10711_5].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
923. [Kwestia głosowa [smalltalk_10711_5] (Post-Uptie Chat 2)] 이따위로 계속 싸우다간 뒤가 없어… 애초에 길게 싸우게 설계된 총이 아니란 말이야, 이대로는 과열되다가 총열이 터져버린다고!\n 야, 뭐 방법 없어?!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=smalltalk_10711_5].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Blimey, we've really got to wrap this up soon... This gun ain't built to last! If the battle gets any longer, it might overheat until the barrel bursts!\nOi, got any bright ideas?
   PL:
924. [Kwestia głosowa [neglect_10711_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=neglect_10711_1].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
925. [Kwestia głosowa [neglect_10711_1] (Idle)] …어, 잠깐 졸았네… 씁. 아직 시작 안 했냐.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=neglect_10711_1].dlg
   limit: do 120 znaków
   EN: .... Unh, I must've taken a short kip. ...Tsk. Still waiting for 'em to get started, eh?
   PL:
926. [Kwestia głosowa [gacksung_10711_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=gacksung_10711_1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
927. [Kwestia głosowa [gacksung_10711_1] (Uptying)] 들켰다! 너희들부터 뒤로 물러서! 내가 응사할테니까…!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=gacksung_10711_1].dlg
   limit: do 120 znaków
   EN: Oh bugger, they saw us! Fall back! I'll return fire...!
   PL:
928. [Kwestia głosowa [formation_10711_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=formation_10711_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
929. [Kwestia głosowa [formation_10711_1] (Deployment)] 어, 이번 의뢰는 몇 발이나 들고 가야하냐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=formation_10711_1].dlg
   limit: do 120 znaków
   EN: Uh, how many bullets should I bring for this contract?
   PL:
930. [Kwestia głosowa [battleentry_10711_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battleentry_10711_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
931. [Kwestia głosowa [battleentry_10711_1] (Stage Entry)] 총은 수지타산에 맞게. 한 발에 한 놈씩.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battleentry_10711_1].dlg
   limit: do 120 znaków
   EN: Let's try to make each bullet count. One shot, one kill.
   PL:
932. [Kwestia głosowa [battle_select_10711_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_select_10711_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
933. [Kwestia głosowa [battle_select_10711_1] (Viewed in Battle)] …숨 참고 있을 때 말 걸지 마라.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_select_10711_1].dlg
   limit: do 120 znaków
   EN: ... Don't try to chat me up when I'm holding my breath, yeah?
   PL:
934. [Kwestia głosowa [battle_endcommand_10711_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_endcommand_10711_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
935. [Kwestia głosowa [battle_endcommand_10711_1] (Commencing Attack)] 사격 개시!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_endcommand_10711_1].dlg
   limit: do 120 znaków
   EN: Opening fire!
   PL:
936. [Kwestia głosowa [battle_enemy_break_10711_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_enemy_break_10711_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
937. [Kwestia głosowa [battle_enemy_break_10711_1] (Enemy Stagger)] 좋아, 순탄하구만…!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_enemy_break_10711_1].dlg
   limit: do 120 znaków
   EN: Nice, it's been a breeze so far...!
   PL:
938. [Kwestia głosowa [battle_break_10711_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_break_10711_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
939. [Kwestia głosowa [battle_break_10711_1] (Staggered)] 으, 큭…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_break_10711_1].dlg
   limit: do 120 znaków
   EN: Ngh, dammit...
   PL:
940. [Kwestia głosowa [battle_kill_10711_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_kill_10711_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
941. [Kwestia głosowa [battle_kill_10711_1] (Enemy Killed)] 깔끔한 헤드샷. 머리통이 작살났다고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_kill_10711_1].dlg
   limit: do 120 znaków
   EN: Clean shot to the head. Bullseye.
   PL:
942. [Kwestia głosowa [battle_dead_10711_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_dead_10711_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
943. [Kwestia głosowa [battle_dead_10711_1] (Death)] 웃기지 마… 아직 끝난 게 아니야…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_dead_10711_1].dlg
   limit: do 120 znaków
   EN: You're shittin' me... I'm not finished yet...
   PL:
944. [Kwestia głosowa [choice_success_p_10711_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=choice_success_p_10711_2].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [Kwestia głosowa [choice_success_p_10711_2] (Check Passed)] 자, 됐냐? 저격수한테 이런 거 시키지 좀 마라.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=choice_success_p_10711_2].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Right, all chuffed now?\nThe hell's up with askin' a sniper to do shite like this...?
   PL:
946. [Kwestia głosowa [choice_fail_n_10711_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=choice_fail_n_10711_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
947. [Kwestia głosowa [choice_fail_n_10711_1] (Check Failed)] 아니… 나는 총 쏘는 놈이라니까? 이런 건…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=choice_fail_n_10711_1].dlg
   limit: do 120 znaków
   EN: Like I said, I'm just some bloke who shoots guns, yeah? Why'd anyone...
   PL:
948. [Kwestia głosowa [battle_clear_10711_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_clear_10711_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
949. [Kwestia głosowa [battle_clear_10711_1] (Victory Cry)] 한 건 넘겼나… 이걸로 넘어갈 수 있으면 좋겠는데. 총알을 너무 쓴 건 아닌가 걱정이네.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_clear_10711_1].dlg
   limit: do 120 znaków
   EN: 'Nother one down... Hope that did the job. I better not have spent too many bullets on this.
   PL:
950. [Kwestia głosowa [battle_clear_ex_10711_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_clear_ex_10711_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
951. [Kwestia głosowa [battle_clear_ex_10711_1] (Extra Conditions Fulfilled)] 하, 그 정도 화력으로 우리 사무소를 막을 수 있을 줄 알았냐? 저놈들 무기까지 주워서 철수하자고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_clear_ex_10711_1].dlg
   limit: do 150 znaków
   EN: Hah, thought you could stop us with that little firepower? C'mon, let's loot the weapons those sods left behind.
   PL:
952. [Kwestia głosowa [battle_defeat_10711_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_defeat_10711_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
953. [Kwestia głosowa [battle_defeat_10711_1] (Defeat Wail)] 거기서 좀 더 신중히 쏴야 했나…? 아니, 탄을 잘못 골랐나… 하, 뭐든 어때… 내가 좀 부족했던 건 사실이니까.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Fullstop_10711.json :: dataList[id=battle_defeat_10711_1].dlg
   limit: do 190 znaków
   EN: I should've taken a more careful shot... Or maybe I picked the wrong ammunition...? Hah, whatever... What matters is that I wasn't good enough.
   PL:

## [000] Kurokumo Clan Wakashu — Heathcliff — 흑운회 와카슈
- ID Tożsamości: `10712` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 70 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed

954. [Karta Tożsamości — tytuł] 흑운회\n와카슈
   źródło: Personalities.json :: dataList[id=10712].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Kurokumo Clan\nWakashu
   PL:
955. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10712].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
956. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10712].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [Karta Tożsamości — opis] 히스클리프의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10712].desc
   limit: do 120 znaków
   EN: Heathcliff’s 12th Identity
   PL:
958. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 구름베기
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=1].name ; dataList[id=1071201].levelList[level=2].name ; dataList[id=1071201].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Lenticular Rend
   PL:
959. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Endurance] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Endurance]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: [WhenUse] Gain 1 [Endurance] next turn (once per turn)
   PL:
960. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
961. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 960 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
962. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AttackDown] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown]
   PL:
963. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 다음 턴에 [Endurance] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [WhenUse], [Endurance]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: <style="highlight">If target has 6+ [Laceration], Coin Power +1</style>\n[WhenUse] Gain 1 [Endurance] next turn (once per turn)
   PL:
964. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1071201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]<style="highlight"></style>
   PL:
965. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 964 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
966. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AttackDown] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1071201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown]<style="highlight"></style>
   PL:
967. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 다음 턴에 [Endurance] <style="highlight">2</style> 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [WhenUse], [Endurance]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[WhenUse] Gain <style="highlight">2</style> [Endurance] next turn (once per turn)
   PL:
968. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 폭풍구름
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=1].name ; dataList[id=1071202].levelList[level=2].name ; dataList[id=1071202].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Stormcloud
   PL:
969. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
970. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
971. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Reduction] 1 부여 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] (once per turn)
   PL:
972. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: <style="highlight">If target has 6+ [Laceration], Coin Power +1</style>
   PL:
973. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1071202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]<style="highlight"></style>
   PL:
974. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [SlashTakeDamageUp] 1 부여</style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: <style="highlight">[OnSucceedAttackHead] Inflict 1 [SlashTakeDamageUp]</style>
   PL:
975. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count<style="highlight"></style>
   PL:
976. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Reduction] 1 부여 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] (once per turn)<style="highlight"></style>
   PL:
977. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)\n[WhenUse] 다음 턴에 [Endurance] 1 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [WhenUse], [Endurance]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)\n[WhenUse] Gain 1 [Endurance] next turn (once per turn)</style>
   PL:
978. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [SlashTakeDamageUp] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttackHead] Inflict 1 [SlashTakeDamageUp]<style="highlight"></style>
   PL:
979. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Reduction] 1 부여 (턴 당 <style="highlight">2</style>회)
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] (<style="highlight">2 times</style> per turn)
   PL:
980. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 천둥베기
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].name ; dataList[id=1071203].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Thundercleave
   PL:
981. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[StartBattle] 다음 턴에 [CloudWall] 1 얻음\n[WhenUse] 다음 턴에 [Endurance] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [StartBattle], [CloudWall], [WhenUse], [Endurance]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [CloudWall] = 구름 장벽 / Cumulus Wall; [WhenUse] = [사용시] / [On Use]; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: If target has 6+ [Laceration], Coin Power +1\n[StartBattle] Gain 1 [CloudWall] next turn\n[WhenUse] Gain 1 [Endurance] next turn (once per turn)
   PL:
982. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 969 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
983. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] The final Coin deals +10% damage
   PL:
984. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [SlashTakeDamageUp] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttack] Inflict 1 [SlashTakeDamageUp]
   PL:
985. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 983 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
986. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 대상이 보유한 부정적인 효과 1개당 피해량 +10% (최대 30%)
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +10% damage for every type of negative effect on target (max 30%)
   PL:
987. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]
   PL:
988. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)</style>\n[StartBattle] 다음 턴에 [CloudWall] 1 얻음\n[WhenUse] 다음 턴에 [Endurance] 1 얻음 (턴 당 1회)\n<style="highlight">[WinDuel] 다음 턴에 [BlackCloudBlade] 1 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [StartBattle], [CloudWall], [WhenUse], [Endurance], [WinDuel], [BlackCloudBlade]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [CloudWall] = 구름 장벽 / Cumulus Wall; [WhenUse] = [사용시] / [On Use]; [Endurance] = 수비 위력 증가 / Defense Power Up; [WinDuel] = [합 승리시] / [Clash Win]; [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[StartBattle] Gain 1 [CloudWall] next turn\n[WhenUse] Gain 1 [Endurance] next turn (once per turn)\n<style="highlight">[WinDuel] Gain 1 [BlackCloudBlade] next turn (once per turn)</style>
   PL:
989. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 973 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
990. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 마지막 코인의 피해량 +10%<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] The final Coin deals +10% damage<style="highlight"></style>
   PL:
991. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [SlashTakeDamageUp] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttack] Inflict 1 [SlashTakeDamageUp]<style="highlight"></style>
   PL:
992. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 마지막 코인의 피해량 +10%<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 990 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
993. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 대상이 보유한 부정적인 효과 1개당 피해량 +10% <style="highlight">(최대 100%)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal +10% damage for every type of negative effect on target <style="highlight">(max 100%)</style>
   PL:
994. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 6 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]<style="highlight"></style>
   PL:
995. [Umiejętność 4 (×0) (ulepszenia 1,4) — nazwa] 뒷골목의 규칙
   źródło: Skills_personality-07.json :: dataList[id=1071205].levelList[level=1].name ; dataList[id=1071205].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Rules of the Backstreets
   PL:
996. [Umiejętność 4 (×0) (ulepszenie 1) — opis] [WhenUse] 자신이 [CloudWall]을 보유하고 있으면, 이 스킬 코인의 재사용 효과를 조건 없이 모두 발동
   źródło: Skills_personality-07.json :: dataList[id=1071205].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [CloudWall]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [CloudWall] = 구름 장벽 / Cumulus Wall
   EN: [WhenUse] If this unit has [CloudWall], unconditionally activate all Reuse effects on this Skill's Coins
   PL:
997. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071205].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1071205].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 969 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
998. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신에게 [BlackCloudBlade]가 있으면 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071205].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1071205].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BlackCloudBlade]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: [OnSucceedAttack] If this unit has [BlackCloudBlade], Reuse Coin once (once per Skill)
   PL:
999. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신에게 [EngageToBattle]이 있으면 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071205].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=1071205].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EngageToBattle]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EngageToBattle] = 임전 / Battle Ready
   EN: [OnSucceedAttack] If this unit has [EngageToBattle], Reuse Coin once (once per Skill)
   PL:
1000. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n대상이 보유한 부정적인 효과 1개당 피해량 +10% (최대 100%)\n[WhenUse] 자신이 [CloudWall]을 보유하고 있으면, 이 스킬 코인의 재사용 효과를 조건 없이 모두 발동
   źródło: Skills_personality-07.json :: dataList[id=1071205].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [CloudWall]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [CloudWall] = 구름 장벽 / Cumulus Wall
   EN: If target has 6+ [Laceration], Coin Power +1\nDeal +10% damage for every type of negative effect on target (max 100%)\n[WhenUse] If this unit has [CloudWall], unconditionally activate all Reuse effects on this Skill's Coins
   PL:
1001. [Obrona (ulepszenia 1,4) — nazwa] 뒷골목의 규칙
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=1].name ; dataList[id=1071204].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 4 · monety: 1 (+5)
   (powtórzenie elementu 995 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1002. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n흑운회 부조장 이스마엘 인격이 전투에 등장해 있으면, 아래 효과가 적용됨\n- 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n- 합 패배시 이 스킬의 최종 위력 +3\n[WhenUse] 자신이 [CloudWall]을 보유하고 있으면, 이 스킬 코인의 재사용 효과를 조건 없이 모두 발동
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=1].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [SuperCoin], [WhenUse], [CloudWall]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [CloudWall] = 구름 장벽 / Cumulus Wall
   EN: [DuelCounter]\nIf Kurokumo Clan Captain Ishmael is on the field, activate the following:\n- Convert all Coins in this Skill into [SuperCoin]s\n- Final Power +3 to this Skill upon Clash Lose\n[WhenUse] If this unit has [CloudWall], unconditionally activate all Reuse effects on this Skill's Coins
   PL:
1003. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 969 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1004. [Obrona (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신에게 [BlackCloudBlade]가 있으면 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 998 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1005. [Obrona (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신에게 [EngageToBattle]이 있으면 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 999 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1006. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n흑운회 부조장 이스마엘 인격이 전투에 등장해 있으면, 아래 효과가 적용됨\n- 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n- 합 패배시 이 스킬의 최종 위력 <style="highlight">+4\n대상이 보유한 부정적인 효과 1개당 피해량 +10% (최대 100%)</style>\n[WhenUse] 자신이 [CloudWall]을 보유하고 있으면, 이 스킬 코인의 재사용 효과를 조건 없이 모두 발동
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=4].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [SuperCoin], [WhenUse], [CloudWall]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [CloudWall] = 구름 장벽 / Cumulus Wall
   EN: [DuelCounter]\nIf Kurokumo Clan Captain Ishmael is on the field, activate the following:\n- Convert all Coins in this Skill into [SuperCoin]s\n- Final Power +4 to this Skill upon Clash Lose\n<style="highlight">Deal +10% damage for every type of negative effect on target (max 100%)</style>\n[WhenUse] If this unit has [CloudWall], unconditionally activate all Reuse effects on this Skill's Coins
   PL:
1007. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 973 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1008. [Obrona (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신에게 [BlackCloudBlade]가 있으면 코인 1회 재사용 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BlackCloudBlade]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: [OnSucceedAttack] If this unit has [BlackCloudBlade], Reuse Coin once (once per Skill)<style="highlight"></style>
   PL:
1009. [Obrona (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신에게 [EngageToBattle]이 있으면 코인 1회 재사용 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [EngageToBattle]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EngageToBattle] = 임전 / Battle Ready
   EN: [OnSucceedAttack] If this unit has [EngageToBattle], Reuse Coin once (once per Skill)<style="highlight"></style>
   PL:
1010. [Pasywka bojowa (od ulepszenia 1) — nazwa] 임전
   źródło: Passives.json :: dataList[id=1071202].name
   limit: do 40 znaków
   EN: Battle Ready
   PL:
1011. [Pasywka bojowa (od ulepszenia 1) — opis] 흑운회 소속 아군이 사망하면, 이번 전투 동안 [SlashResultUp] 1 얻음\n\n흑운회 소속 아군이 3명 이상 사망하면 이번 전투 동안 [EngageToBattle]을 얻음
   źródło: Passives.json :: dataList[id=1071202].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [SlashResultUp], [EngageToBattle]
   znaczenie tagów: [SlashResultUp] = 참격 위력 증가 / Slash Power Up; [EngageToBattle] = 임전 / Battle Ready
   EN: When a Kurokumo Clan ally dies, gain 1 [SlashResultUp] for this Encounter\n\nWhen 3 or more Kurokumo Clan allies are defeated, gain [EngageToBattle] for this Encounter
   PL:
1012. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — nazwa] 흑운도
   źródło: Passives.json :: dataList[id=1071201].name
   limit: do 40 znaków
   EN: Dark Cloud Blade
   PL:
1013. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — opis] 자신을 포함해 전투에 참여한 아군 흑운회 소속 인격이 2명 이상이면 [BlackCloudBlade] 1 얻음 (최대 1)\n\n이번 턴에 수비 스킬을 사용한 적 또는 공격 시작 전에 최대 체력인 적에게 입히는 피해량 +10%\n\n이번 턴에 적이 자신을 제외한 아군을 스킬로 공격하여 피해를 입혔으면, 공격자를 스킬 1로 일방 공격함 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1071201].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [BlackCloudBlade]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: When there are 2+ allied Kurokumo Clan Identities on the field, including this unit, gain 1 [BlackCloudBlade] (max 1)\n\nAgainst enemies that, in this turn, used Defense Skills or were at max HP before attacking: deal +10% damage\n\nIf an enemy attacked another ally with a Skill and dealt damage this turn: use an Unopposed Attack against the attacker with Skill 1 (once per turn)
   PL:
1014. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — podsumowanie] [BlackCloudBlade] 얻음, 최대 체력이거나 수비 스킬을 사용한 적 대상 피해량 증가, 아군이 공격당하면 반격 발동
   źródło: Passives.json :: dataList[id=1071201].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [BlackCloudBlade]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: Gain [BlackCloudBlade]; deal more damage against enemies that were at max HP or used a Defense Skill; counterattack when an ally is attacked
   PL:
1015. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — nazwa] 흑운도
   źródło: Passives.json :: dataList[id=1071211].name
   (powtórzenie elementu 1012 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1016. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — opis] 자신을 포함해 전투에 참여한 아군 흑운회 소속 인격이 2명 이상이면 [BlackCloudBlade] 1 얻음 (최대 1)\n\n이번 턴에 수비 스킬을 사용한 적 또는 공격 시작 전에 최대 체력인 적에게 입히는 피해량 +10%\n\n적이 자신을 제외한 아군을 스킬로 공격하여 피해를 입혔으면, 공격자를 스킬 1로 일방 공격함 (턴 당 1회)\n\n<style="highlight">적이 자신을 제외한 아군을 처치했거나, 공격 종료후 공격당한 아군의 체력이 25% 미만이면, 공격자를 <뒷골목의 규칙> 으로 일방 공격함 (아군 캐릭터 당 1회, 턴 당 2회. 해당 효과로 발동된 스킬은 공격 스킬로 간주함)</style>
   źródło: Passives.json :: dataList[id=1071211].desc
   limit: do 840 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BlackCloudBlade]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: When there are 2+ allied Kurokumo Clan Identities on the field, including this unit, gain 1 [BlackCloudBlade] (max 1)\n\nAgainst enemies that, in this turn, used Defense Skills or were at max HP before attacking: deal +10% damage\n\nIf an enemy attacked another ally with a Skill and dealt damage this turn: use an Unopposed Attack against the attacker with Skill 1 (once per turn)\n\n<style="highlight">If the enemy killed another ally, or if the said ally's HP is at less than 25% after the enemy's attack, use an Unopposed Attack against the attacker with <Rules of the Backstreets> instead (once per ally; 2 times per turn; the Skill activated with this effect counts as an Attack Skill)</style>
   PL:
1017. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — podsumowanie] [BlackCloudBlade] 얻음, 최대 체력이거나 수비 스킬을 사용한 적 대상 피해량이 증가, 아군이 공격당하면 반격 발동
   źródło: Passives.json :: dataList[id=1071211].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [BlackCloudBlade]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: Gain [BlackCloudBlade]; deal more damage against enemies that were at max HP or used a Defense Skill; counterattack when an ally is attacked
   PL:
1018. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — nazwa] 후벼파기
   źródło: Passives.json :: dataList[id=1071221].name
   limit: do 40 znaków
   EN: Impale
   PL:
1019. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — opis] 속도가 가장 빠른 아군 1명이 이번 턴에 수비 스킬을 사용했거나, 공격 시작 전에 최대 체력인 적에게 가하는 피해량 +10%
   źródło: Passives.json :: dataList[id=1071221].desc
   limit: do 180 znaków
   EN: 1 ally with the fastest Speed: against enemies that used Defense Skills or were at max HP before attacking this turn: deal +10% damage
   PL:
1020. [Kwestia głosowa [get_10712_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=get_10712_1].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1021. [Kwestia głosowa [get_10712_1] (Identity Acquisition)] 조직끼리 모여서 한다는 게 이딴 시시한 회의라니…\n대체 결전은 언제 하는 건데?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=get_10712_1].dlg
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Is chatting politely in a circle all we're doing here? It's a gathering of Syndicates, dammit... When's the showdown anyway?
   PL:
1022. [Kwestia głosowa [lobby_morning_10712_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=lobby_morning_10712_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1023. [Kwestia głosowa [lobby_morning_10712_1] (Morning Greeting)] 해 떴으니 슬슬 나가볼까. 근처 한 바퀴 돌면서 우리 사업장에 찝쩍거리는 놈들 없는지 확인해 봐야 하거든. 겸사겸사 보호비도 좀 걷고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=lobby_morning_10712_1].dlg
   limit: do 240 znaków
   EN: Sun's up, time to get off your arses. Think I'll go on a patrol to see if there's anyone stupid enough to loiter around 'our' businesses. Might as well collect some protection money, too.
   PL:
1024. [Kwestia głosowa [lobby_noon_10712_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=lobby_noon_10712_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1025. [Kwestia głosowa [lobby_noon_10712_1] (Afternoon Greeting)] 야 거기. 그래 너. 대낮부터 우리 구역에 허락도 없이 들어와? 간이 아주 배 밖으로…\n잠깐. 너 설마 내 문신 보고 있었냐? 짜식, 말을 하지. 조금만 봐라. 그다음엔 얌전히 꺼지고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=lobby_noon_10712_1].dlg
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Oi, you there. Yeah, you. You've got to be one mad or stupid lad to saunter into our area in the middle of the—\nOh, hang on a minute. Were you eyin' my tats? Well, why didn't you say so from the beginning? Fine, take a gander. Just a little bit, though. Now fuck off kindly.
   PL:
1026. [Kwestia głosowa [lobby_night_10712_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=lobby_night_10712_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1027. [Kwestia głosowa [lobby_night_10712_1] (Evening Greeting)] 하… 내가 니들 마음 모르겠냐? 일 끝나고 술 한잔 걸치는 것까지 막진 않아, 근데!\n마셨으면 얌전히 자라. 사고 치면 부조장 귀에 들어가기 전에… 내가 먼저 그놈 머리통을 깨부술 테니까.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=lobby_night_10712_1].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Haah... of course I know how you feel, lads. There ain't nothing wrong with goin' for a few bevvies after work, yeah?\nBut once you do, you better go straight to bed. If any of you lads make a mistake while sloshed, I'll crack your skull open before the Captain even hears of it.
   PL:
1028. [Kwestia głosowa [smalltalk_10712_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=smalltalk_10712_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1029. [Kwestia głosowa [smalltalk_10712_1] (Chatter #1)] 그거 들었냐? 이번 회의엔 동부십검 중에 셋은 참가한다더라.\n쯧. 엄지 그 새끼들이 손목만 안 잘랐어도, 우리 조장도 아직 십검의 일원이었을텐데.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=smalltalk_10712_1].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Didya hear? Apparently three of the Ten Blades of the East'll be showin' up to the meeting.\nTsk, our Patriarch would've been one of 'em too if those Thumb fuckers hadn't cut off his wrist.
   PL:
1030. [Kwestia głosowa [smalltalk_10712_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=smalltalk_10712_2].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1031. [Kwestia głosowa [smalltalk_10712_2] (Chatter #2)] 왜 싸울 때도 주머니에서 손을 안 빼냐고? 야, 조직 생활하면 자기 힘의 3푼은 숨기라는 말 못 들어봤어?\n뭐? 3푼이 아니라 3할이라고? …그게 그거지. 쪼잔하게 그런 걸 따지고 있냐.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=smalltalk_10712_2].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Why do I keep one hand in a pocket? Oi, haven't you heard the old Syndicate wisdom? Always keep a trick up your britches, yeah?\nWha? It's sleeve, not britches? ... Well, it's all the same to me, ya little nit-pickin' bag of shite.
   PL:
1032. [Kwestia głosowa [smalltalk_10712_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=smalltalk_10712_3].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1033. [Kwestia głosowa [smalltalk_10712_3] (Chatter #3)] 철풍조에 묘고파… 저놈들은 극진회잖아? 뭐? 어떻게 그렇게 잘 아냐고?\n당연히 알지! 부조장 그 녀석이 옛날부터 얼마나 저놈들 얘기를 귀에 닳도록 읊어댔는데.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=smalltalk_10712_3].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: That one there's the Teppu Family, the Nekomata Mafia... and... oi, those blokes over there are from the Kyokushin Clan. Huh? How do I know all their names?\n'Course I do! Our Captain, that lass, she's been lecturin' me all about them sods since forever.
   PL:
1034. [Kwestia głosowa [smalltalk_10712_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=smalltalk_10712_4].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1035. [Kwestia głosowa [smalltalk_10712_4] (Post-Uptie Chat 1)] 야, 이거 보이냐? 이번에 부조장 덕에 새로 받은 강화 문신인데 구름의 문양이며, 성능까지… 아주 때깔부터 다르더라.\n예전이었으면 두동강 날 팔이, 이젠 그냥 생채기 조금 나고 버틴다니까?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=smalltalk_10712_4].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Oi, have a gander at my enhancement tattoos. I just got these thanks to the Captain. Look at the cloud patterns here... and it's bloody good to boot.\nA strike that would've cut off my arm leaves only a little cut now, ain't that neat?
   PL:
1036. [Kwestia głosowa [smalltalk_10712_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=smalltalk_10712_5].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1037. [Kwestia głosowa [smalltalk_10712_5] (Post-Uptie Chat 2)] 뭔… 급도 안되는 것들이 부조장한테 1대1 결투를 신청했다고? 이스마엘 그 녀석이 이제 막 부조장이 됐다고 만만하게 봤나 본데…\n뭐. 칼솜씨는 어디 가서 안 꿀리는 녀석이니까 걱정할 건 없고… 우린 시체 하나 치울 준비만 하면 돼.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=smalltalk_10712_5].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Wha...? Some small fries challenged the Captain to a duel? Hah, those sods must've underestimated Ishmael 'coz she's a new Captain...\nWell, there ain't nothing for us to worry about. We just need to get ready to clean up some dead bodies.
   PL:
1038. [Kwestia głosowa [neglect_10712_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=neglect_10712_1].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1039. [Kwestia głosowa [neglect_10712_1] (Idle)] 흐아암… 뭔데? 어지간한 안건 아니면 잘 때 깨우지 마라.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=neglect_10712_1].dlg
   limit: do 120 znaków
   EN: <i>Yaaaaawn...</i> Whassit? Wake me up only when something serious happens, yeah?
   PL:
1040. [Kwestia głosowa [gacksung_10712_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=gacksung_10712_1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1041. [Kwestia głosowa [gacksung_10712_1] (Uptying)] 후…! 또 덤비고 싶은 놈 없지?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=gacksung_10712_1].dlg
   limit: do 120 znaków
   EN: Hooah...! Anyone else lookin' for a thrashing?
   PL:
1042. [Kwestia głosowa [formation_10712_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=formation_10712_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1043. [Kwestia głosowa [formation_10712_1] (Deployment)] 드디어 내 차례냐?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=formation_10712_1].dlg
   limit: do 120 znaków
   EN: About time!
   PL:
1044. [Kwestia głosowa [battleentry_10712_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battleentry_10712_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1045. [Kwestia głosowa [battleentry_10712_1] (Stage Entry)] 어떤 조직 놈들인지, 면면 좀 봐둘까.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battleentry_10712_1].dlg
   limit: do 120 znaków
   EN: Let's see their stupid mugs, whichever Syndicate they're from.
   PL:
1046. [Kwestia głosowa [battle_select_10712_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_select_10712_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1047. [Kwestia głosowa [battle_select_10712_1] (Viewed in Battle)] 후… 잠깐 숨 좀 돌리자.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_select_10712_1].dlg
   limit: do 120 znaków
   EN: Phoo... let me catch my breath.
   PL:
1048. [Kwestia głosowa [battle_endcommand_10712_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_endcommand_10712_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1049. [Kwestia głosowa [battle_endcommand_10712_1] (Commencing Attack)] 전부 처 죽여!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_endcommand_10712_1].dlg
   limit: do 120 znaków
   EN: Kill 'em all!
   PL:
1050. [Kwestia głosowa [battle_enemy_break_10712_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_enemy_break_10712_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1051. [Kwestia głosowa [battle_enemy_break_10712_1] (Enemy Stagger)] 죽을 맛일걸?
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_enemy_break_10712_1].dlg
   limit: do 120 znaków
   EN: This'll hurt like hell.
   PL:
1052. [Kwestia głosowa [battle_break_10712_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_break_10712_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1053. [Kwestia głosowa [battle_break_10712_1] (Staggered)] 큭.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_break_10712_1].dlg
   limit: do 120 znaków
   EN: Agh.
   PL:
1054. [Kwestia głosowa [battle_kill_10712_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_kill_10712_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1055. [Kwestia głosowa [battle_kill_10712_1] (Enemy Killed)] 다음 놈, 나와!
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_kill_10712_1].dlg
   limit: do 120 znaków
   EN: Next! Chop-chop!
   PL:
1056. [Kwestia głosowa [battle_dead_10712_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_dead_10712_1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1057. [Kwestia głosowa [battle_dead_10712_1] (Death)] 벨 만큼은 베었으니까… 뒤는 맡긴다…
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_dead_10712_1].dlg
   limit: do 120 znaków
   EN: I've cut through enough of 'em... I'll leave the rest to you...
   PL:
1058. [Kwestia głosowa [choice_success_p_10712_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=choice_success_p_10712_2].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1059. [Kwestia głosowa [choice_success_p_10712_2] (Check Passed)] 봤냐? 와카슈쯤 되시면 이런 건 식은 죽 먹기지.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=choice_success_p_10712_2].dlg
   limit: do 120 znaków
   EN: See? I ain't a Wakashu for nothing.
   PL:
1060. [Kwestia głosowa [choice_fail_n_10712_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=choice_fail_n_10712_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1061. [Kwestia głosowa [choice_fail_n_10712_1] (Check Failed)] …사람 베는 거 말곤 좀 서툴다고 했잖냐.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=choice_fail_n_10712_1].dlg
   limit: do 120 znaków
   EN: ... I told you, I'm a bit inexperienced in things other than slicing and dicing.
   PL:
1062. [Kwestia głosowa [battle_clear_10712_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_clear_10712_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1063. [Kwestia głosowa [battle_clear_10712_1] (Victory Cry)] 야야. 적당히 해. 곧 손가락 걸기라는 거 잊었냐? 대가리끼리 서로 불편하지 않게 이쯤하고 철수하자고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_clear_10712_1].dlg
   limit: do 160 znaków
   EN: Oi, oi. That's enough. Finger bow-bell's comin' up—let's not make things too awkward for the big boys when they meet.
   PL:
1064. [Kwestia głosowa [battle_clear_ex_10712_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_clear_ex_10712_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1065. [Kwestia głosowa [battle_clear_ex_10712_1] (Extra Conditions Fulfilled)] 다들 고생했다. 부조장한텐 내가 말해둘 테니까, 뒷처리 끝나면 뜨끈하게 목욕탕에 가서 몸부터 씻자고.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_clear_ex_10712_1].dlg
   limit: do 160 znaków
   EN: Good work, lads. I'll deal with the Captain, so let's all go for a dip at the bathhouse once we're done with the cleanup.
   PL:
1066. [Kwestia głosowa [battle_defeat_10712_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_defeat_10712_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1067. [Kwestia głosowa [battle_defeat_10712_1] (Defeat Wail)] 아이씨… 쪽팔리게… 야, 난 이거 수습할 때까진 죽어도 안 돌아갈 거다. 부조장한테는… 다음 조직 회의 전까지는 돌아갈 거라고 전해.
   źródło: PersonalityVoiceDlg/Voice_Heathcliff_Kurokumo_10712.json :: dataList[id=battle_defeat_10712_1].dlg
   limit: do 210 znaków
   EN: Blimey, this is some embarrassin' shite... Oi, I ain't going back until we deal with this mess. Tell the Captain... that I'll be back before our next meeting.
   PL:
