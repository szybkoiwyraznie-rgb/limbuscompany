# Grzesznik #11: Outis — Tożsamości, umiejętności, pasywki i głos (część a) — Limbus Company

Kompletny zestaw kart Tożsamości postaci **Outis** (오티스) wraz z umiejętnościami na ulepszeniach 1–4, efektami monet, pasywkami i kwestiami głosowymi.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Grzesznik #11: Outis (오티스)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 오티스
   źródło: Characters.json :: dataList[id=11].name
   limit: do 40 znaków
   EN: Outis
   PL:
2. [Akta więźnia — nazwa] 오티스
   źródło: IntroduceCharacter.json :: dataList[id=오티스].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
3. [Akta więźnia — opis] 관리자의 역량에 따라 훌륭한 조언자가 되어줄 수도 있는 수감자입니다.\n하지만 오지랖이 과한 수감자이기도 하므로 적당히 맞장구를\n쳐주는 것을 권장합니다. 전술을 포함한 여러 경험에 있어서는 숙련자이므로\n조언을 구하는 편이 효율적입니다. 덤으로 공방 기술들에 대한\n해박한 지식도 있으니 버스의 간단한 수리 정도는 맡겨도 될 것입니다.\n[주의] - 다른 수감자들과는 달리 과거사의 열람이 허락되지 않습니다.\n[주의] - 임무 외에 머리 굴러가는 소리가 나지 않도록 감독하십시오.
   źródło: IntroduceCharacter.json :: dataList[id=오티스].description
   limit: do 920 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This Sinner could serve as an excellent advisor depending on your capability.\nHowever, she also has a meddlesome tendency, so it is recommended to keep her satisfied with short replies of agreement.\nShe is an expert when it comes to tactics and various pearls of wisdom about life,\nmaking her advice all the more valuable for your mission.\nIn addition, she possesses a vast knowledge of workshop technologies;\nyou could trust her with simple repairs of the bus.\n[NOTICE]: Unlike the other Sinners, accessing records pertaining to the past of this Sinner is not permitted.\n[WARNING]: Keep an eye on this Sinner and beware that she does not exercise her cunning intellect\nfor purposes other than completing our company's mission.
   PL: Grzesznica, która zależnie od umiejętności Kierownika może być znakomitą doradczynią.\nMa jednak skłonność do wtrącania się we wszystko, dlatego zalecamy\nw miarę jej przytakiwać. W taktyce i wielu innych dziedzinach ma bogate\ndoświadczenie, warto więc zasięgać jej rady. Dodatkowo zna się świetnie\nna technologiach Warsztatów, można jej więc powierzać drobne naprawy autobusu.\n[UWAGA] - W odróżnieniu od innych Grzeszników wgląd w jej przeszłość jest zabroniony.\n[UWAGA] - Proszę pilnować, by poza misją nie było słychać, jak obracają się trybiki w jej głowie.

## [0] LCB Sinner — Outis — LCB 수감자
- ID Tożsamości: `11101` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 60 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture

4. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=11101].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL:
5. [Karta Tożsamości — nazwa] 오티스
   źródło: Personalities.json :: dataList[id=11101].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — nazwa z tytułem] 오티스
   źródło: Personalities.json :: dataList[id=11101].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Karta Tożsamości — opis] 오티스의 첫번째 인격
   źródło: Personalities.json :: dataList[id=11101].desc
   limit: do 120 znaków
   EN: Outis’s 1st Identity
   PL:
8. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 칼날 빼기
   źródło: Skills.json :: dataList[id=1110101].levelList[level=1].name ; dataList[id=1110101].levelList[level=2].name ; dataList[id=1110101].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 3 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Pulled Blade
   PL:
9. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1110101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL:
10. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1110101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1110101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL:
11. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1110101].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Rupture
   PL:
12. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 배후 베기
   źródło: Skills.json :: dataList[id=1110102].levelList[level=1].name ; dataList[id=1110102].levelList[level=2].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Backslash
   PL:
13. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상보다 속도가 빠르면 피해량 +10%
   źródło: Skills.json :: dataList[id=1110102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: If user’s Speed is faster than target’s, +10% Damage
   PL:
14. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] 대상보다 속도가 빠르면 피해량 +10%
   źródło: Skills.json :: dataList[id=1110102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
15. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] 대상보다 속도가 빠르면 피해량 +20%
   źródło: Skills.json :: dataList[id=1110102].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: If user’s Speed is faster than target’s, +20% Damage
   PL:
16. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] 대상보다 속도가 빠르면 피해량 +20%
   źródło: Skills.json :: dataList[id=1110102].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 뚫어내기
   źródło: Skills.json :: dataList[id=1110103].levelList[level=3].name ; dataList[id=1110103].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 7 · monety: 1 (+14)
   limit: do 40 znaków
   EN: Piercing Thrust
   PL:
18. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] 대상의 체력이 50% 이상이면, 피해량 +20%
   źródło: Skills.json :: dataList[id=1110103].levelList[level=3].desc ; dataList[id=1110103].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target’s HP is above 50%, deal +20% damage
   PL:
19. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 1 증가
   źródło: Skills.json :: dataList[id=1110103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Rupture Count
   PL:
20. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1110104].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: unik · moc bazowa: 2 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL:
21. [Pasywka bojowa (od ulepszenia 1, posiadane 4× Sloth) — nazwa] 처형
   źródło: Passives.json :: dataList[id=1110101].name
   limit: do 40 znaków
   EN: Executor
   PL:
22. [Pasywka bojowa (od ulepszenia 1, posiadane 4× Sloth) — opis] 대상의 정신력이 0 미만일 때 피해량 +10%
   źródło: Passives.json :: dataList[id=1110101].desc
   limit: do 120 znaków
   EN: If target’s SP is below 0, deal +10% damage.
   PL:
23. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Sloth) — nazwa] 군인정신
   źródło: Passives.json :: dataList[id=1110121].name
   limit: do 40 znaków
   EN: Military Mindset
   PL:
24. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Sloth) — opis] 현재 체력이 가장 높은 아군 1명 정신력이 0 미만인 적 공격 시 피해량 +30%
   źródło: Passives.json :: dataList[id=1110121].desc
   limit: do 120 znaków
   EN: 1 ally with the most HP deals +30% damage to enemies below 0 SP.
   PL:
25. [Kwestia głosowa [get_11101_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=get_11101_1].desc
   limit: do 120 znaków
   EN: Identity Acquisition
   PL:
26. [Kwestia głosowa [get_11101_1] (Identity Acquisition)] 오티스입니다. 제 이름을 기억해주십시오. 관리자님.
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=get_11101_1].dlg
   limit: do 120 znaków
   EN: My name is Outis. I hope you’ll remember it well, Executive Manager.
   PL:
27. [Kwestia głosowa [lobby_morning_11101_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=lobby_morning_11101_1].desc
   limit: do 120 znaków
   EN: Morning Greeting
   PL:
28. [Kwestia głosowa [lobby_morning_11101_1] (Morning Greeting)] 아침 식사는 챙겨 드셨습니까 관리자님! 영 비실해보이시는데, 균형 있는 영양 식단이 무엇보다 중요합니다!
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=lobby_morning_11101_1].dlg
   limit: do 210 znaków
   EN: A fine morning, Executive Manager! Have you had your breakfast? You seem concerningly feeble; allow me to remind you that it’s important to have a balanced diet!
   PL:
29. [Kwestia głosowa [lobby_noon_11101_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=lobby_noon_11101_1].desc
   limit: do 120 znaków
   EN: Afternoon Greeting
   PL:
30. [Kwestia głosowa [lobby_noon_11101_1] (Afternoon Greeting)] 관리자님 같은 분이 혼자 밥을 먹는 찌질한 행위를 하셔서는 안 됩니다! 제가 같이 먹어드리겠습니다!
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=lobby_noon_11101_1].dlg
   limit: do 190 znaków
   EN: An outstanding leader such as yourself should not be subject to the pathetic humiliation of eating all alone! I shall join you at your table!
   PL:
31. [Kwestia głosowa [lobby_night_11101_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=lobby_night_11101_1].desc
   limit: do 120 znaków
   EN: Evening Greeting
   PL:
32. [Kwestia głosowa [lobby_night_11101_1] (Evening Greeting)] 내일도 좋은 컨디션으로 임하시려면 일찍 자두는 것이 좋습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=lobby_night_11101_1].dlg
   limit: do 120 znaków
   EN: I advise you to sleep early in order to take on tomorrow’s tasks in good shape.
   PL:
33. [Kwestia głosowa [smalltalk_11101_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=smalltalk_11101_1].desc
   limit: do 120 znaków
   EN: Chatter #1
   PL:
34. [Kwestia głosowa [smalltalk_11101_1] (Chatter #1)] 바쁘긴 합니다만, 관리자님이 부르신다면 하던 일 따위 즉시 중단하고 오겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=smalltalk_11101_1].dlg
   limit: do 120 znaków
   EN: While I am busy, I am fully willing to pause all my ongoing tasks if you summon me.
   PL:
35. [Kwestia głosowa [smalltalk_11101_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=smalltalk_11101_2].desc
   limit: do 120 znaków
   EN: Chatter #2
   PL:
36. [Kwestia głosowa [smalltalk_11101_2] (Chatter #2)] 관리자님은 승리를 위해 어디까지 내어줄 수 있으십니까. 어디까지… 자신을 놓아버릴 수 있으십니까?
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=smalltalk_11101_2].dlg
   limit: do 180 znaków
   EN: How much are you ready to sacrifice for victory, Executive Manager? How much of yourself are you willing to let go if it means you can win…?
   PL:
37. [Kwestia głosowa [smalltalk_11101_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=smalltalk_11101_3].desc
   limit: do 120 znaków
   EN: Chatter #3
   PL:
38. [Kwestia głosowa [smalltalk_11101_3] (Chatter #3)] 전장에 직접 서보지도 않은 애송이들 따위랑 임무를 수행해야 하다니… 아 물론 관리자님을 두고 말한 건 아닙니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=smalltalk_11101_3].dlg
   limit: do 230 znaków
   EN: The absurdity of having to carry out missions with rookies who haven’t even set foot on a real battlefield… Ah, I am most definitely not referring to you, Executive Manager.
   PL:
39. [Kwestia głosowa [neglect_11101_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=neglect_11101_1].desc
   limit: do 120 znaków
   EN: Idle
   PL:
40. [Kwestia głosowa [neglect_11101_1] (Idle)] 관리자님? 전투 능력도 변변찮으신데 혼자 다니는 건 위험합니다!
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=neglect_11101_1].dlg
   limit: do 150 znaków
   EN: Executive Manager? It’s dangerous to go out alone, especially for someone who is as incapable of combat as you are!
   PL:
41. [Kwestia głosowa [formation_11101_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=formation_11101_1].desc
   limit: do 120 znaków
   EN: Deployment
   PL:
42. [Kwestia głosowa [formation_11101_1] (Deployment)] 즉시 출격하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=formation_11101_1].dlg
   limit: do 120 znaków
   EN: I will make a sortie right away.
   PL:
43. [Kwestia głosowa [battleentry_11101_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battleentry_11101_1].desc
   limit: do 120 znaków
   EN: Stage Entry
   PL:
44. [Kwestia głosowa [battleentry_11101_1] (Stage Entry)] 이 오티스. 참전합니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battleentry_11101_1].dlg
   limit: do 120 znaków
   EN: Outis, joining the battle.
   PL:
45. [Kwestia głosowa [battle_select_11101_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_select_11101_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle
   PL:
46. [Kwestia głosowa [battle_select_11101_1] (Viewed in Battle)] 볼 일이 있나요? 관리자님.
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_select_11101_1].dlg
   limit: do 120 znaków
   EN: Do you have any business with me, Executive Manager?
   PL:
47. [Kwestia głosowa [battle_endcommand_11101_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_endcommand_11101_1].desc
   limit: do 120 znaków
   EN: Commencing Attack
   PL:
48. [Kwestia głosowa [battle_endcommand_11101_1] (Commencing Attack)] 명령대로 하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_endcommand_11101_1].dlg
   limit: do 120 znaków
   EN: As you order.
   PL:
49. [Kwestia głosowa [battle_enemy_break_11101_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_enemy_break_11101_1].desc
   limit: do 120 znaków
   EN: Enemy Stagger
   PL:
50. [Kwestia głosowa [battle_enemy_break_11101_1] (Enemy Stagger)] 순조로운 전략입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_enemy_break_11101_1].dlg
   limit: do 120 znaków
   EN: The plan is going smoothly.
   PL:
51. [Kwestia głosowa [battle_break_11101_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_break_11101_1].desc
   limit: do 120 znaków
   EN: Staggered
   PL:
52. [Kwestia głosowa [battle_break_11101_1] (Staggered)] 윽!
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_break_11101_1].dlg
   limit: do 120 znaków
   EN: Ugh!
   PL:
53. [Kwestia głosowa [battle_kill_11101_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_kill_11101_1].desc
   limit: do 120 znaków
   EN: Enemy Killed
   PL:
54. [Kwestia głosowa [battle_kill_11101_1] (Enemy Killed)] 좋은 전략입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_kill_11101_1].dlg
   limit: do 120 znaków
   EN: A sound strategy.
   PL:
55. [Kwestia głosowa [battle_allydead_11101_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_allydead_11101_1].desc
   limit: do 120 znaków
   EN: Ally Death
   PL:
56. [Kwestia głosowa [battle_allydead_11101_1] (Ally Death)] 이래서 애송이들이란.
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_allydead_11101_1].dlg
   limit: do 120 znaków
   EN: Rookies.
   PL:
57. [Kwestia głosowa [choice_success_p_11101_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=choice_success_p_11101_1].desc
   limit: do 120 znaków
   EN: Check Passed
   PL:
58. [Kwestia głosowa [choice_success_p_11101_1] (Check Passed)] 훌륭한 작전 덕분에 승리했을 뿐입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=choice_success_p_11101_1].dlg
   limit: do 120 znaków
   EN: This victory can only be attributed to your excellent planning.
   PL:
59. [Kwestia głosowa [choice_fail_n_11101_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=choice_fail_n_11101_1].desc
   limit: do 120 znaków
   EN: Check Failed
   PL:
60. [Kwestia głosowa [choice_fail_n_11101_1] (Check Failed)] 저의 실책입니다…
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=choice_fail_n_11101_1].dlg
   limit: do 120 znaków
   EN: The fault is mine…
   PL:
61. [Kwestia głosowa [battle_clear_11101_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_clear_11101_1].desc
   limit: do 120 znaków
   EN: Victory Cry
   PL:
62. [Kwestia głosowa [battle_clear_11101_1] (Victory Cry)] 여억시! 관리자님이십니다!
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_clear_11101_1].dlg
   limit: do 120 znaków
   EN: Splendid as always, Executive Manager!
   PL:
63. [Kwestia głosowa [battle_clear_ex_11101_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_clear_ex_11101_1].desc
   limit: do 120 znaków
   EN: Extra Conditions Fulfilled
   PL:
64. [Kwestia głosowa [battle_clear_ex_11101_1] (Extra Conditions Fulfilled)] 관리자님의 99% 명령과 1%의 제 실력이 합쳐진 결과였습니다!
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_clear_ex_11101_1].dlg
   limit: do 120 znaków
   EN: This was 99% your brilliant leadership and 1% my competence!
   PL:
65. [Kwestia głosowa [battle_defeat_11101_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_defeat_11101_1].desc
   limit: do 120 znaków
   EN: Defeat Wail
   PL:
66. [Kwestia głosowa [battle_defeat_11101_1] (Defeat Wail)] 뭐가 됐던 관리자님이나 제 책임은 아닙니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LCB_11101.json :: dataList[id=battle_defeat_11101_1].dlg
   limit: do 120 znaków
   EN: In any case, it’s neither of our faults, Executive Manager.
   PL:

## [00] Blade Lineage Salsu — Outis — 검계 살수
- ID Tożsamości: `11102` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Poise

67. [Karta Tożsamości — tytuł] 검계\n살수
   źródło: Personalities.json :: dataList[id=11102].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Blade Lineage\nSalsu
   PL:
68. [Karta Tożsamości — nazwa] 오티스
   źródło: Personalities.json :: dataList[id=11102].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [Karta Tożsamości — nazwa z tytułem] 오티스
   źródło: Personalities.json :: dataList[id=11102].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Karta Tożsamości — opis] 오티스의 두번째 인격
   źródło: Personalities.json :: dataList[id=11102].desc
   limit: do 120 znaków
   EN: Outis’s 2nd Identity
   PL:
71. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 발검
   źródło: Skills.json :: dataList[id=1110201].levelList[level=1].name ; dataList[id=1110201].levelList[level=2].name ; dataList[id=1110201].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Draw of the Sword
   PL:
72. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1110201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath]
   PL:
73. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 호흡 4 얻음
   źródło: Skills.json :: dataList[id=1110201].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 4 [Breath]
   PL:
74. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 [Breath]이 5 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1110201].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 5+ [Breath], Coin Power +1
   PL:
75. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 4 얻음
   źródło: Skills.json :: dataList[id=1110201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 4 [Breath]
   PL:
76. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 자법
   źródło: Skills.json :: dataList[id=1110202].levelList[level=1].name ; dataList[id=1110202].levelList[level=2].name ; dataList[id=1110202].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Acupuncture
   PL:
77. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 참격 피해량 증가 1 얻음
   źródło: Skills.json :: dataList[id=1110202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain 1 Slash DMG Up next turn
   PL:
78. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WinDuel] 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1110202].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WinDuel] Gain +1 [Breath] Count
   PL:
79. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 참격 피해량 증가 2 얻음
   źródło: Skills.json :: dataList[id=1110202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1110202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain 2 Slash DMG Up next turn
   PL:
80. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WinDuel] 자신의 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1110202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WinDuel] Gain +2 [Breath] Count
   PL:
81. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 요격세
   źródło: Skills.json :: dataList[id=1110203].levelList[level=3].name ; dataList[id=1110203].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 6 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Decisive Dive
   PL:
82. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 체력이 25% 미만일 때 최종 위력 +2
   źródło: Skills.json :: dataList[id=1110203].levelList[level=3].desc
   limit: do 120 znaków
   EN: If target’s HP is below 25%, Final Power +2
   PL:
83. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] 피해량의 20%만큼 첫번째 흐트러짐 구간을 손상시킴
   źródło: Skills.json :: dataList[id=1110203].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1110203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Raise first Stagger Threshold by 20% of damage dealt
   PL:
84. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 체력이 50% 미만일 때 최종 위력 +2
   źródło: Skills.json :: dataList[id=1110203].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target’s HP is below 50%, Final Power +2
   PL:
85. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1110204].levelList[level=1].name ; dataList[id=1110204].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 3 · monety: 1 (+10)
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Obrona (ulepszenie 4) — opis] 자신의 [Breath]이 6 이상이면, 코인 위력 +3
   źródło: Skills.json :: dataList[id=1110204].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 6+ [Breath], Coin Power +3
   PL:
87. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Pride) — nazwa] 냉정
   źródło: Passives.json :: dataList[id=1110201].name
   limit: do 40 znaków
   EN: Levelheaded
   PL:
88. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Pride) — opis] 체력이 25%미만인 적 공격 시 피해량 +20%
   źródło: Passives.json :: dataList[id=1110201].desc
   limit: do 120 znaków
   EN: Deal +20% damage to targets below 25% HP.
   PL:
89. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — nazwa] 확인사살
   źródło: Passives.json :: dataList[id=1110221].name
   limit: do 40 znaków
   EN: Double Tap
   PL:
90. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — opis] 정신력이 가장 높은 아군 1명 체력이 25% 미만인 적 공격 시 피해량 +30%
   źródło: Passives.json :: dataList[id=1110221].desc
   limit: do 120 znaków
   EN: 1 ally with the most SP deals +30% damage to enemies below 25% HP.
   PL:
91. [Kwestia głosowa [get_11102_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=get_11102_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Kwestia głosowa [get_11102_1] (Identity Acquisition)] 흐름을 따라 이곳에 왔으니, 이를 막는 건 무엇이든 베어내겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=get_11102_1].dlg
   limit: do 120 znaków
   EN: I’ve followed the flow to this place, and I’ll cut down all that impedes it.
   PL:
93. [Kwestia głosowa [lobby_morning_11102_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=lobby_morning_11102_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Kwestia głosowa [lobby_morning_11102_1] (Morning Greeting)] 전 주로 새벽에 일어나는 편입니다. 해가 솟아나는 순간을 직면해야, 하루의 시작을 하는 기분이거든요.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=lobby_morning_11102_1].dlg
   limit: do 150 znaków
   EN: I normally rise early in the morning. Watching the sun on the horizon gives me the feeling that the day has begun.
   PL:
95. [Kwestia głosowa [lobby_noon_11102_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=lobby_noon_11102_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Kwestia głosowa [lobby_noon_11102_1] (Afternoon Greeting)] 로지온이… 자꾸만 식당을 소개시켜주겠다 하더군요. 생소하지만, 먹는 것에도 즐거움을 느끼는 자들도 있는 것 같습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=lobby_noon_11102_1].dlg
   limit: do 200 znaków
   EN: Rodion… She kept on insisting that she take me to a restaurant. Though the concept is foreign to me, it would seem that some people derive joy from eating.
   PL:
97. [Kwestia głosowa [lobby_night_11102_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=lobby_night_11102_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Kwestia głosowa [lobby_night_11102_1] (Evening Greeting)] 마음을 정리하고 싶을 땐 달빛을 올려다보는 것도 도움이 됩니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=lobby_night_11102_1].dlg
   limit: do 120 znaków
   EN: When you wish to clear your mind, admiring the moonlight can help.
   PL:
99. [Kwestia głosowa [smalltalk_11102_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=smalltalk_11102_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Kwestia głosowa [smalltalk_11102_1] (Chatter #1)] 눈 앞에 장애물이 있다면 베는 것을 망설이지 마시길 바랍니다. 설령 그것이 관리자님의 마음을 베게 되더라도.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=smalltalk_11102_1].dlg
   limit: do 160 znaków
   EN: You shouldn’t restrain yourself from cutting down whatever obstructs your way, even if it is to wound your heart as well.
   PL:
101. [Kwestia głosowa [smalltalk_11102_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=smalltalk_11102_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [Kwestia głosowa [smalltalk_11102_2] (Chatter #2)] 긴 대화는 좋아하지 않습니다. 칼을 부딪히는 것보다 마음 솔직한 대화는 없었으니까요.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=smalltalk_11102_2].dlg
   limit: do 120 znaków
   EN: I dislike long conversation. No words hold more weight than those of clashing blades.
   PL:
103. [Kwestia głosowa [smalltalk_11102_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=smalltalk_11102_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Kwestia głosowa [smalltalk_11102_3] (Chatter #3)] 칼을  지니다 보면 자연스럽게 침착하고 신속해지기 마련입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=smalltalk_11102_3].dlg
   limit: do 120 znaków
   EN: Bearing a sword naturally makes your mind calm and your actions swift.
   PL:
105. [Kwestia głosowa [smalltalk_11102_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=smalltalk_11102_4].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 1
   PL:
106. [Kwestia głosowa [smalltalk_11102_4] (Post-Uptie Chat 1)] 이끄는 자가 된다는 건 망망대해에 선다는 것과 닮았군요. 막막하면서도 까마득하지만… 물러설 곳이 없습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=smalltalk_11102_4].dlg
   limit: do 190 znaków
   EN: To become a leader is to sail a vast sea. It is a wide-spanning ordeal, with no destination in clear sight… yet there is nowhere to fall back to.
   PL:
107. [Kwestia głosowa [smalltalk_11102_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=smalltalk_11102_5].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 2
   PL:
108. [Kwestia głosowa [smalltalk_11102_5] (Post-Uptie Chat 2)] 관리자님은 목표를 위해서 어디까지 할 수 있으십니까. 그리고 어디까지… 내어질 수 있으십니까.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=smalltalk_11102_5].dlg
   limit: do 200 znaków
   EN: To what extents are you willing to go for the sake of your goal, Executive Manager? Alongside that… how much of yourself can you withstand to forfeit?
   PL:
109. [Kwestia głosowa [neglect_11102_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=neglect_11102_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
110. [Kwestia głosowa [neglect_11102_1] (Idle)] 요새는 기술이 좋아져서 핏자국 같은 건 순식간에 지워지더군요. 죽음 따윈 가볍게 잊어버리는 것이 도리인 것 마냥.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=neglect_11102_1].dlg
   limit: do 190 znaków
   EN: These days, advanced technology makes erasing bloodstains a trivial task, as though it were only right that we forget about death that easily.
   PL:
111. [Kwestia głosowa [gacksung_11102_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=gacksung_11102_1].desc
   limit: do 120 znaków
   EN: Uptying
   PL:
112. [Kwestia głosowa [gacksung_11102_1] (Uptying)] 그러기를 바라신다면… 받들도록 하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=gacksung_11102_1].dlg
   limit: do 120 znaków
   EN: If you so wish… I shall serve you.
   PL:
113. [Kwestia głosowa [formation_11102_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=formation_11102_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Kwestia głosowa [formation_11102_1] (Deployment)] 베어내겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=formation_11102_1].dlg
   limit: do 120 znaków
   EN: I will dispatch them.
   PL:
115. [Kwestia głosowa [battleentry_11102_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battleentry_11102_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Kwestia głosowa [battleentry_11102_1] (Stage Entry)] 칼을 부딪칠 시간입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battleentry_11102_1].dlg
   limit: do 120 znaków
   EN: It’s time to have blades meet.
   PL:
117. [Kwestia głosowa [battle_select_11102_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_select_11102_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Kwestia głosowa [battle_select_11102_1] (Viewed in Battle)] 간단하게라면 좋습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_select_11102_1].dlg
   limit: do 120 znaków
   EN: I’d appreciate it if you could keep it simple.
   PL:
119. [Kwestia głosowa [battle_endcommand_11102_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_endcommand_11102_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Kwestia głosowa [battle_endcommand_11102_1] (Commencing Attack)] 물러서지 않겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_endcommand_11102_1].dlg
   limit: do 120 znaków
   EN: I won’t stand back.
   PL:
121. [Kwestia głosowa [battle_enemy_break_11102_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_enemy_break_11102_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Kwestia głosowa [battle_enemy_break_11102_1] (Enemy Stagger)] 베어내기 충분합니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_enemy_break_11102_1].dlg
   limit: do 120 znaków
   EN: I should be able to slay them with ease.
   PL:
123. [Kwestia głosowa [battle_break_11102_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_break_11102_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Kwestia głosowa [battle_break_11102_1] (Staggered)] 읍!
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_break_11102_1].dlg
   limit: do 120 znaków
   EN: Mmpf!
   PL:
125. [Kwestia głosowa [battle_kill_11102_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_kill_11102_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Kwestia głosowa [battle_kill_11102_1] (Enemy Killed)] 침착한 결과입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_kill_11102_1].dlg
   limit: do 120 znaków
   EN: A result earned through calmness.
   PL:
127. [Kwestia głosowa [battle_allydead_11102_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_allydead_11102_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Kwestia głosowa [battle_allydead_11102_1] (Ally Death)] 힘드시겠습니다. 관리자님.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_allydead_11102_1].dlg
   limit: do 120 znaków
   EN: That must be tough to recover, Executive Manager.
   PL:
129. [Kwestia głosowa [choice_success_p_11102_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=choice_success_p_11102_1].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Kwestia głosowa [choice_success_p_11102_1] (Check Passed)] 칼의 사용법을 잘 아시는군요.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=choice_success_p_11102_1].dlg
   limit: do 120 znaków
   EN: I see you know your way around a sword.
   PL:
131. [Kwestia głosowa [choice_fail_n_11102_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=choice_fail_n_11102_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Kwestia głosowa [choice_fail_n_11102_1] (Check Failed)] 단련하지 않은 제 잘못입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=choice_fail_n_11102_1].dlg
   limit: do 120 znaków
   EN: It was my fault for neglecting to train.
   PL:
133. [Kwestia głosowa [battle_clear_11102_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_clear_11102_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Kwestia głosowa [battle_clear_11102_1] (Victory Cry)] 길이 보여 따라갔을 뿐.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_clear_11102_1].dlg
   limit: do 120 znaków
   EN: I only followed the path I saw.
   PL:
135. [Kwestia głosowa [battle_clear_ex_11102_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_clear_ex_11102_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Kwestia głosowa [battle_clear_ex_11102_1] (Extra Conditions Fulfilled)] 흐름을 따라 전부 베어냈습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_clear_ex_11102_1].dlg
   limit: do 120 znaków
   EN: I slew them all, dancing along with the flow.
   PL:
137. [Kwestia głosowa [battle_defeat_11102_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_defeat_11102_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Kwestia głosowa [battle_defeat_11102_1] (Defeat Wail)] 후회는 없습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_SwordGroup_11102.json :: dataList[id=battle_defeat_11102_1].dlg
   limit: do 120 znaków
   EN: I hold no regrets.
   PL:

## [00] G Corp. Head Manager — Outis — G사 부장
- ID Tożsamości: `11103` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 1 · HP bazowe: 76 · szybkość: 4–6 / 4–7 / 4–8 / 4–8
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Sinking

139. [Karta Tożsamości — tytuł] G사\n부장
   źródło: Personalities.json :: dataList[id=11103].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: G Corp.\nHead Manager
   PL:
140. [Karta Tożsamości — nazwa] 오티스
   źródło: Personalities.json :: dataList[id=11103].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Karta Tożsamości — nazwa z tytułem] 오티스
   źródło: Personalities.json :: dataList[id=11103].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [Karta Tożsamości — opis] 오티스의 세번째 인격
   źródło: Personalities.json :: dataList[id=11103].desc
   limit: do 120 znaków
   EN: Outis’s 3rd Identity
   PL:
143. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 지휘
   źródło: Skills.json :: dataList[id=1110301].levelList[level=1].name ; dataList[id=1110301].levelList[level=2].name ; dataList[id=1110301].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Order
   PL:
144. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 속도가 가장 낮은 아군에게 보호 1 부여
   źródło: Skills.json :: dataList[id=1110301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Apply 1 Protection to the ally with the slowest Speed
   PL:
145. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 속도가 가장 낮은 아군에게 보호 2 부여
   źródło: Skills.json :: dataList[id=1110301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1110301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Apply 2 Protection to the ally with the slowest Speed
   PL:
146. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Sinking]이 5 이상이면, 스킬 위력 +2
   źródło: Skills.json :: dataList[id=1110301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: If target has 5+ [Sinking], Coin Power +2
   PL:
147. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 공격 명령
   źródło: Skills.json :: dataList[id=1110302].levelList[level=1].name ; dataList[id=1110302].levelList[level=2].name ; dataList[id=1110302].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 6 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Onslaught Command
   PL:
148. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 속도가 가장 낮은 아군에게 피해량 증가 1 부여
   źródło: Skills.json :: dataList[id=1110302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Apply 1 Damage Up to the ally with the slowest Speed
   PL:
149. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WhenUse] 속도가 가장 낮은 아군에게 공격 위력 증가 1 부여
   źródło: Skills.json :: dataList[id=1110302].levelList[level=2].desc ; dataList[id=1110302].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Apply 1 Attack Power Up to the ally with the slowest Speed
   PL:
150. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 속도가 가장 낮은 아군에게 피해량 증가 2 부여
   źródło: Skills.json :: dataList[id=1110302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Apply 2 Damage Up to the ally with the slowest Speed
   PL:
151. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 속도가 가장 낮은 아군에게 피해량 증가 2 부여
   źródło: Skills.json :: dataList[id=1110302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Apply 2 Damage Up to the ally with the slowest Speed
   PL:
152. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 기합
   źródło: Skills.json :: dataList[id=1110303].levelList[level=3].name ; dataList[id=1110303].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 6 · monety: 1 (+16)
   limit: do 40 znaków
   EN: Focus
   PL:
153. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 5 부여
   źródło: Skills.json :: dataList[id=1110303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1110303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking]
   PL:
154. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 공격 위력 감소 2 부여
   źródło: Skills.json :: dataList[id=1110303].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1110303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Attack Power Down
   PL:
155. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 침잠 4 부여
   źródło: Skills.json :: dataList[id=1110303].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 4 [Sinking]
   PL:
156. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1110304].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 9 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Guard
   PL:
157. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Sloth) — nazwa] 사기진작
   źródło: Passives.json :: dataList[id=1110301].name
   limit: do 40 znaków
   EN: Morale Boost
   PL:
158. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Sloth) — opis] 다음 턴 시작 시 자신과 이번 턴에 조작 패널에서 자신의 양옆에 있는 아군에게 신속 2 부여
   źródło: Passives.json :: dataList[id=1110301].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Next turn, apply 2 [Agility] to self and allies who are adjacent to this unit on the Dashboard this turn.
   PL:
159. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Sloth) — nazwa] 각오
   źródło: Passives.json :: dataList[id=1110321].name
   limit: do 40 znaków
   EN: Valor
   PL:
160. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Sloth) — opis] 현재 체력이 가장 높은 아군 1명 전투 시작 시 수비 위력 증가 1, 공격 위력 증가 1, 보호 1 중 무작위 1개 효과를 얻음
   źródło: Passives.json :: dataList[id=1110321].desc
   limit: do 170 znaków
   EN: 1 ally with the most HP randomly gains 1 Attack Power Up, 1 Defense Power Up, or 1 Protection at the start of the combat phase.
   PL:
161. [Kwestia głosowa [get_11103_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=get_11103_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [Kwestia głosowa [get_11103_1] (Identity Acquisition)] 지금 이 순간부터, 날 보고 눈살을 찌푸린 자들은 모두 열외자로 간주하겠다.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=get_11103_1].dlg
   limit: do 120 znaków
   EN: As of this moment, anyone who frowns at me will be dishonorably discharged.
   PL:
163. [Kwestia głosowa [lobby_morning_11103_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=lobby_morning_11103_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Kwestia głosowa [lobby_morning_11103_1] (Morning Greeting)] 제 사전에 늦잠 따위는 허용하지 않습니다. 전시에도 태평하게 늘어져 있다가는 곧바로 절명하기 십상입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=lobby_morning_11103_1].dlg
   limit: do 140 znaków
   EN: Oversleeping is not tolerated on my watch. Such tardiness in wartime is flat out asking to be killed.
   PL:
165. [Kwestia głosowa [lobby_noon_11103_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=lobby_noon_11103_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Kwestia głosowa [lobby_noon_11103_1] (Afternoon Greeting)] 다들 한가하게 밥이나 먹으러 쏘다닐 생각을 하다니… 버스에 전투식량을 상시 구비해놓는 건 어떻습니까.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=lobby_noon_11103_1].dlg
   limit: do 160 znaków
   EN: Look at those slackers, getting ready to roam about looking for a place to eat… I suggest we stock rations on the bus.
   PL:
167. [Kwestia głosowa [lobby_night_11103_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=lobby_night_11103_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Kwestia głosowa [lobby_night_11103_1] (Evening Greeting)] 잠을 제대로 들지 못한 지는 꽤 되었습니다. 한 번 눈을 감는 순간, 모든 게 폐허가 될 수가 있다는 걸, 직접 보았으니까요.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=lobby_night_11103_1].dlg
   limit: do 170 znaków
   EN: I haven’t had the luxury of proper sleep for a long time. I saw firsthand the devastation that awaited me after a moment of rest.
   PL:
169. [Kwestia głosowa [smalltalk_11103_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=smalltalk_11103_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Kwestia głosowa [smalltalk_11103_1] (Chatter #1)] 이곳에서 그를 마주칠 줄은 생각도 못 했습니다. 전쟁이 끝나자마자 사라져 버린, 전장의 영웅…
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=smalltalk_11103_1].dlg
   limit: do 140 znaków
   EN: I never quite expected to meet the man here—our wartime hero who had vanished as soon as the war was over…
   PL:
171. [Kwestia głosowa [smalltalk_11103_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=smalltalk_11103_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Kwestia głosowa [smalltalk_11103_2] (Chatter #2)] 벌레떼들은 포기라는 걸 모릅니다. 돌진에는 일말의 망설임이 없으며 시체까지 갉아먹으니까요.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=smalltalk_11103_2].dlg
   limit: do 160 znaków
   EN: A swarm of insects never knows retreat. They rush out without a hint of reservation, and their jaws gnaw even the dead.
   PL:
173. [Kwestia głosowa [smalltalk_11103_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=smalltalk_11103_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Kwestia głosowa [smalltalk_11103_3] (Chatter #3)] 옛 부하들은… 제 손짓 한 번으로 살아있는 모든 것이 껍데기만 남게 될 때까지 돌진을 멈추지 않았습니다. 이곳과는 다르게 말입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=smalltalk_11103_3].dlg
   limit: do 230 znaków
   EN: My old subordinates… They would charge ahead at a single gesture of my hand, advancing until nothing but empty husks remained in their wake. A stark contrast to what I have here.
   PL:
175. [Kwestia głosowa [smalltalk_11103_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=smalltalk_11103_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Kwestia głosowa [smalltalk_11103_4] (Post-Uptie Chat 1)] 푸른 하늘은 아직까지도 어색합니다. 공기를 자유롭게 들이키면서 숨을 쉴 수 있는 것도. 함성과 고함소리로 하루를 시작하지 않는다는 것도.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=smalltalk_11103_4].dlg
   limit: do 210 znaków
   EN: I am still unaccustomed to the blue sky, as well as the fact that I can freely breathe this air… and the absence of shouts and cries that would break the dawn.
   PL:
177. [Kwestia głosowa [smalltalk_11103_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=smalltalk_11103_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Kwestia głosowa [smalltalk_11103_5] (Post-Uptie Chat 2)] 전투 경험도 없는 이의 지휘를 받는다는 건 제 사전엔 용납되지 않는 일이었습니다. 하지만… 무엇이든 예외라는 것도 있다는 걸 깨닫는 중입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=smalltalk_11103_5].dlg
   limit: do 200 znaków
   EN: Receiving commands from someone with zero experience in combat was unfathomable to me. However… I’m learning here that every rule has its exceptions.
   PL:
179. [Kwestia głosowa [neglect_11103_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=neglect_11103_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Kwestia głosowa [neglect_11103_1] (Idle)] 단체 점호라도 해야 하나…
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=neglect_11103_1].dlg
   limit: do 120 znaków
   EN: Perhaps a squad-wide roll call will knock some sense into them…
   PL:
181. [Kwestia głosowa [gacksung_11103_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=gacksung_11103_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Kwestia głosowa [gacksung_11103_1] (Uptying)] 충성. 최선을 다하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=gacksung_11103_1].dlg
   limit: do 120 znaków
   EN: Salutations. I shall do my utmost to serve.
   PL:
183. [Kwestia głosowa [formation_11103_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=formation_11103_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Kwestia głosowa [formation_11103_1] (Deployment)] 돌격 준비 완료!
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=formation_11103_1].dlg
   limit: do 120 znaków
   EN: Ready to sortie!
   PL:
185. [Kwestia głosowa [battleentry_11103_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battleentry_11103_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Kwestia głosowa [battleentry_11103_1] (Stage Entry)] 이번 지휘도 부탁드립니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battleentry_11103_1].dlg
   limit: do 120 znaków
   EN: I’m counting on your command.
   PL:
187. [Kwestia głosowa [battle_select_11103_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_select_11103_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Kwestia głosowa [battle_select_11103_1] (Viewed in Battle)] 조언이 필요하십니까?
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_select_11103_1].dlg
   limit: do 120 znaków
   EN: Do you need my advice?
   PL:
189. [Kwestia głosowa [battle_endcommand_11103_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_endcommand_11103_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Kwestia głosowa [battle_endcommand_11103_1] (Commencing Attack)] 돌격합니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_endcommand_11103_1].dlg
   limit: do 120 znaków
   EN: Charging in.
   PL:
191. [Kwestia głosowa [battle_enemy_break_11103_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_enemy_break_11103_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Kwestia głosowa [battle_enemy_break_11103_1] (Enemy Stagger)] 허점을 찾았습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_enemy_break_11103_1].dlg
   limit: do 120 znaków
   EN: I spotted a vulnerability.
   PL:
193. [Kwestia głosowa [battle_break_11103_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_break_11103_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Kwestia głosowa [battle_break_11103_1] (Staggered)] 쳇!
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_break_11103_1].dlg
   limit: do 120 znaków
   EN: Tch!
   PL:
195. [Kwestia głosowa [battle_kill_11103_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_kill_11103_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Kwestia głosowa [battle_kill_11103_1] (Enemy Killed)] 다음은 어디입니까?
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_kill_11103_1].dlg
   limit: do 120 znaków
   EN: Where do I go next?
   PL:
197. [Kwestia głosowa [battle_allydead_11103_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_allydead_11103_1].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Kwestia głosowa [battle_allydead_11103_1] (Ally Death)] 오늘은 단체 점호다.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_allydead_11103_1].dlg
   limit: do 120 znaków
   EN: There will be full-on roll call tonight.
   PL:
199. [Kwestia głosowa [choice_success_p_11103_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=choice_success_p_11103_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Kwestia głosowa [choice_success_p_11103_2] (Check Passed)] 탁월한 지휘였습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=choice_success_p_11103_2].dlg
   limit: do 120 znaków
   EN: Excellent command.
   PL:
201. [Kwestia głosowa [choice_fail_n_11103_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=choice_fail_n_11103_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Kwestia głosowa [choice_fail_n_11103_1] (Check Failed)] 모든 지휘가 완벽할 순 없습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=choice_fail_n_11103_1].dlg
   limit: do 120 znaków
   EN: I can’t expect every order to be flawless.
   PL:
203. [Kwestia głosowa [battle_clear_11103_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_clear_11103_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Kwestia głosowa [battle_clear_11103_1] (Victory Cry)] 벌레떼들보다 못한 것들.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_clear_11103_1].dlg
   limit: do 120 znaków
   EN: You’re worse than pests.
   PL:
205. [Kwestia głosowa [battle_clear_ex_11103_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_clear_ex_11103_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Kwestia głosowa [battle_clear_ex_11103_1] (Extra Conditions Fulfilled)] 인정합니다. 저와 견줄만한 지휘 실력을 갖추셨군요.
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_clear_ex_11103_1].dlg
   limit: do 120 znaków
   EN: I must acknowledge that your leadership rivals mine.
   PL:
207. [Kwestia głosowa [battle_defeat_11103_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_defeat_11103_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Kwestia głosowa [battle_defeat_11103_1] (Defeat Wail)] 내가 총지휘권만 가졌더라도…
   źródło: PersonalityVoiceDlg/Voice_Outis_GCorpBoss_11103.json :: dataList[id=battle_defeat_11103_1].dlg
   limit: do 120 znaków
   EN: If only I had assumed total command…
   PL:

## [000] Seven Assoc. South Section 6 Director — Outis — 남부 세븐 협회 6과 부장
- ID Tożsamości: `11104` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 86 · szybkość: 5–6 / 5–7 / 5–8 / 5–8
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Rupture

209. [Karta Tożsamości — tytuł] 남부 세븐 협회\n6과 부장
   źródło: Personalities.json :: dataList[id=11104].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Seven Assoc.\nSouth Section 6 Director
   PL:
210. [Karta Tożsamości — nazwa] 오티스
   źródło: Personalities.json :: dataList[id=11104].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Karta Tożsamości — nazwa z tytułem] 오티스
   źródło: Personalities.json :: dataList[id=11104].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Karta Tożsamości — opis] 오티스의 네번째 인격
   źródło: Personalities.json :: dataList[id=11104].desc
   limit: do 120 znaków
   EN: Outis’s 4th Identity
   PL:
213. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 예측 분석
   źródło: Skills.json :: dataList[id=1110401].levelList[level=1].name ; dataList[id=1110401].levelList[level=2].name ; dataList[id=1110401].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 6 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Predictive Analysis
   PL:
214. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 합 진행 시 대상의 합 위력 - 1
   źródło: Skills.json :: dataList[id=1110401].levelList[level=1].desc
   limit: do 120 znaków
   EN: In a clash, opponent has -1 Clash Power
   PL:
215. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 마비 1 부여
   źródło: Skills.json :: dataList[id=1110401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Paralyze next turn
   PL:
216. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] 합 진행 시 대상의 합 위력 - 2
   źródło: Skills.json :: dataList[id=1110401].levelList[level=2].desc ; dataList[id=1110401].levelList[level=4].desc
   limit: do 120 znaków
   EN: In a clash, opponent has -2 Clash Power
   PL:
217. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills.json :: dataList[id=1110401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1110401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Paralyze next turn
   PL:
218. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1110401].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Rupture
   PL:
219. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 현장 지휘
   źródło: Skills.json :: dataList[id=1110402].levelList[level=1].name ; dataList[id=1110402].levelList[level=2].name ; dataList[id=1110402].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 5 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Field Command
   PL:
220. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 합 진행 시 대상의 합 위력 - 1
   źródło: Skills.json :: dataList[id=1110402].levelList[level=1].desc
   (powtórzenie elementu 214 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 횟수 1 증가
   źródło: Skills.json :: dataList[id=1110402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Rupture Count
   PL:
222. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1110402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Defense Level Down next turn
   PL:
223. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 횟수 1 증가
   źródło: Skills.json :: dataList[id=1110402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1110402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] 합 진행 시 대상의 합 위력 - 2
   źródło: Skills.json :: dataList[id=1110402].levelList[level=2].desc ; dataList[id=1110402].levelList[level=4].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 1 증가
   źródło: Skills.json :: dataList[id=1110402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1110402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1110402].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1110402].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Defense Level Down next turn
   PL:
228. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 1 증가
   źródło: Skills.json :: dataList[id=1110402].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1110402].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1110402].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1110402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Rupture Count
   PL:
231. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 빈틈 간파
   źródło: Skills.json :: dataList[id=1110403].levelList[level=3].name ; dataList[id=1110403].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 6 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Exploit the Gap
   PL:
232. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 합 진행 시 대상의 합 위력 - 2
   źródło: Skills.json :: dataList[id=1110403].levelList[level=3].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1110403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1110403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Offense Level Down next turn
   PL:
234. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 피해량의 15%만큼 참격 추가 피해
   źródło: Skills.json :: dataList[id=1110403].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1110403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal bonus Slash damage by 15% of damage dealt
   PL:
235. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 약점 분석 부여
   źródło: Skills.json :: dataList[id=1110403].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1110403].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Weakness Analyzed next turn
   PL:
236. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 합 진행 시 대상의 합 위력 - 2\n대상의 [Burst]이 7 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1110403].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: In a clash, opponent has -2 Clash Power\nIf target has 7+ [Burst], Coin Power +2
   PL:
237. [Obrona (ulepszenie 1) — nazwa] 앞장서겠다
   źródło: Skills.json :: dataList[id=1110404].levelList[level=1].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 13 · monety: 1 (+7)
   limit: do 40 znaków
   EN: I'll Take the Lead
   PL:
238. [Obrona (ulepszenie 1) — opis] [WhenUse] 다음 턴에 신속 1, 수비 위력 증가 1을 얻음
   źródło: Skills.json :: dataList[id=1110404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Haste and 1 Defense Power Up next turn
   PL:
239. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — nazwa] 약점 파악
   źródło: Passives.json :: dataList[id=1110401].name
   limit: do 40 znaków
   EN: Grasping Vulnerabilities
   PL:
240. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — opis] 상대의 약점이나 취약 속성으로 공격할 때 피해량 +10%
   źródło: Passives.json :: dataList[id=1110401].desc
   limit: do 130 znaków
   EN: When attacking a target with a damage type the target is “Weak” or “Fatal” to, deal +10% damage.
   PL:
241. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 정보 공유
   źródło: Passives.json :: dataList[id=1110421].name
   limit: do 40 znaków
   EN: Relay Intelligence
   PL:
242. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 속도가 가장 높은 아군 1명이 상대의 약점이나 취약 속성으로 공격할 때 피해량 +10%
   źródło: Passives.json :: dataList[id=1110421].desc
   limit: do 170 znaków
   EN: 1 ally with the fastest Speed deals +10% damage when attacking a target with a damage type the target is “Weak” or “Fatal” to.
   PL:
243. [Kwestia głosowa [get_11104_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=get_11104_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [Kwestia głosowa [get_11104_1] (Identity Acquisition)] 음, 오티스다. 찾아온 이유라도 있나?
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=get_11104_1].dlg
   limit: do 120 znaków
   EN: Hm, it’s Outis. What brings you here?
   PL:
245. [Kwestia głosowa [lobby_morning_11104_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=lobby_morning_11104_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Kwestia głosowa [lobby_morning_11104_1] (Morning Greeting)] 근무 준비 시간이라 지금 찾아와도 해줄 수 있는게 없다만… 뭐, 들어나 볼까.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=lobby_morning_11104_1].dlg
   limit: do 190 znaków
   EN: Work is under prep at this time of day, so I can do little for you even if you visit me now… Well, I suppose I can hear what you have to say.
   PL:
247. [Kwestia głosowa [lobby_noon_11104_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=lobby_noon_11104_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [Kwestia głosowa [lobby_noon_11104_1] (Afternoon Greeting)] 점심? 아, 거기 갖다 두게. 지금 이걸 읽느라 바빠서… 아, 같이 먹으러 나가자는 이야기였나. 미안, 바쁘군.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=lobby_noon_11104_1].dlg
   limit: do 180 znaków
   EN: Lunch? Ah, you can leave it there. I’m rather busy with this document… Oh, you were asking to eat out? Sorry, I can’t make time for that.
   PL:
249. [Kwestia głosowa [lobby_night_11104_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=lobby_night_11104_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Kwestia głosowa [lobby_night_11104_1] (Evening Greeting)] 나는 너무 걱정하지 말고, 먼저 퇴근하도록. 상관이 고된 일을 맡는 게 당연한 일이지.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=lobby_night_11104_1].dlg
   limit: do 140 znaków
   EN: You can leave the office before I do—I’ll be fine. It’s only right that superiors take on difficult matters.
   PL:
251. [Kwestia głosowa [smalltalk_11104_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=smalltalk_11104_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Kwestia głosowa [smalltalk_11104_1] (Chatter #1)] 홍차 한 잔 사와줄 수 있겠나? 값은 이걸로 치뤄주게. 자네 것도 사고.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=smalltalk_11104_1].dlg
   limit: do 120 znaków
   EN: Could you get me some black tea? Here’s the money you need. Get something for yourself too.
   PL:
253. [Kwestia głosowa [smalltalk_11104_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=smalltalk_11104_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Kwestia głosowa [smalltalk_11104_2] (Chatter #2)] 그다지 많은 시간은 할애할 수 없지만… 그렇게 기다리고 있으니 들어라도 볼까. 무슨일이지?
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=smalltalk_11104_2].dlg
   limit: do 130 znaków
   EN: Although I can’t spare much time… I can’t keep someone waiting forever. What is your business?
   PL:
255. [Kwestia głosowa [smalltalk_11104_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=smalltalk_11104_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Kwestia głosowa [smalltalk_11104_3] (Chatter #3)] 현장에서 하는 일도 나쁘진 않지만… 역시, 책상머리 앞이 안정감이 들긴 하는군.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=smalltalk_11104_3].dlg
   limit: do 130 znaków
   EN: While fieldwork isn’t all too bad… It just doesn’t compare to the comfort of sitting at a desk.
   PL:
257. [Kwestia głosowa [smalltalk_11104_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=smalltalk_11104_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Kwestia głosowa [smalltalk_11104_4] (Post-Uptie Chat 1)] 6과가 한참 말단이라고는 해도, 귀한 인재는 꽤 있는 법이지. 최근 들어 눈에 띄는 인재들이 있어서 말이야…\n음료 취향도 맞고 말이지.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=smalltalk_11104_4].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Section 6 may be on the bottom rung, but it does have its share of valuable individuals. I’ve been noticing more of them lately…\nTheir taste in drinks matches mine, too.
   PL:
259. [Kwestia głosowa [smalltalk_11104_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=smalltalk_11104_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Kwestia głosowa [smalltalk_11104_5] (Post-Uptie Chat 2)] …그래서 말인데, 특별히 신뢰하는 자네이니 생각을 좀 듣고 싶다만.\n…졸았나? 음, 일이 고되었던 모양인데, 특별 반차를 내줄테니 가서 좀 쉴 수 있도록. 회복한 다음에 이야기 나누지.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=smalltalk_11104_5].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: …with all that said, I’ve been meaning to hear the thoughts of someone I know I can trust.\n…re you dozing off? Hm, work must have worn you out. I’ll give you half a day off, so go get the rest you need. We can talk after you’ve recovered.
   PL:
261. [Kwestia głosowa [neglect_11104_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=neglect_11104_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Kwestia głosowa [neglect_11104_1] (Idle)] 남부 6과 부장 오티스다. 지금은 부재중이니, 중요한 안건이라면 삐 소리 후에 남기도록.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=neglect_11104_1].dlg
   limit: do 210 znaków
   EN: This is Outis, Director of the Southern Branch’s Section 6. I’m away right now, so if you have any important matters to share, leave a message after the beep.
   PL:
263. [Kwestia głosowa [gacksung_11104_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=gacksung_11104_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Kwestia głosowa [gacksung_11104_1] (Uptying)] 현장일이 더 많아진다는 뜻인가… 뭐, 좋다. 현장 지휘도 경험이지.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=gacksung_11104_1].dlg
   limit: do 130 znaków
   EN: This means more fieldwork for me, doesn’t it… Well, fine. I won’t turn down additional experience.
   PL:
265. [Kwestia głosowa [formation_11104_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=formation_11104_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Kwestia głosowa [formation_11104_1] (Deployment)] 현장 지휘자가 필요한가?
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=formation_11104_1].dlg
   limit: do 120 znaków
   EN: Need a field commander?
   PL:
267. [Kwestia głosowa [battleentry_11104_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battleentry_11104_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Kwestia głosowa [battleentry_11104_1] (Stage Entry)] …가보지.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battleentry_11104_1].dlg
   limit: do 120 znaków
   EN: …Let’s go.
   PL:
269. [Kwestia głosowa [battle_select_11104_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_select_11104_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [Kwestia głosowa [battle_select_11104_1] (Viewed in Battle)] 뭔가, 의견이 있나?
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_select_11104_1].dlg
   limit: do 120 znaków
   EN: Do you have an opinion you want to voice?
   PL:
271. [Kwestia głosowa [battle_endcommand_11104_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_endcommand_11104_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Kwestia głosowa [battle_endcommand_11104_1] (Commencing Attack)] 직접 나서지.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_endcommand_11104_1].dlg
   limit: do 120 znaków
   EN: I’ll take charge.
   PL:
273. [Kwestia głosowa [battle_enemy_break_11104_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_enemy_break_11104_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Kwestia głosowa [battle_enemy_break_11104_1] (Enemy Stagger)] 빈틈 투성이로군.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_enemy_break_11104_1].dlg
   limit: do 120 znaków
   EN: You’re full of gaps.
   PL:
275. [Kwestia głosowa [battle_break_11104_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_break_11104_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Kwestia głosowa [battle_break_11104_1] (Staggered)] 큭…
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_break_11104_1].dlg
   limit: do 120 znaków
   EN: Kgh…
   PL:
277. [Kwestia głosowa [battle_kill_11104_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_kill_11104_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Kwestia głosowa [battle_kill_11104_1] (Enemy Killed)] 쓰러졌군.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_kill_11104_1].dlg
   limit: do 120 znaków
   EN: There goes one.
   PL:
279. [Kwestia głosowa [battle_dead_11104_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_dead_11104_1].desc
   limit: do 120 znaków
   EN: Death
   PL:
280. [Kwestia głosowa [battle_dead_11104_1] (Death)] 역시… 현장은 체질이 아니었나…
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_dead_11104_1].dlg
   limit: do 120 znaków
   EN: As I feared… I’m not fit for the field…
   PL:
281. [Kwestia głosowa [choice_success_p_11104_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=choice_success_p_11104_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Kwestia głosowa [choice_success_p_11104_2] (Check Passed)] 예상했던 결과다.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=choice_success_p_11104_2].dlg
   limit: do 120 znaków
   EN: Just as predicted.
   PL:
283. [Kwestia głosowa [choice_fail_n_11104_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=choice_fail_n_11104_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Kwestia głosowa [choice_fail_n_11104_1] (Check Failed)] 예상에서… 빗나갔군.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=choice_fail_n_11104_1].dlg
   limit: do 120 znaków
   EN: This was… not quite what I predicted.
   PL:
285. [Kwestia głosowa [battle_clear_11104_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_clear_11104_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Kwestia głosowa [battle_clear_11104_1] (Victory Cry)] 괜찮은 산책이었다. 책상으로 돌아가지.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_clear_11104_1].dlg
   limit: do 120 znaków
   EN: That was a fine constitutional. Let’s get back to the office.
   PL:
287. [Kwestia głosowa [battle_clear_ex_11104_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_clear_ex_11104_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Kwestia głosowa [battle_clear_ex_11104_1] (Extra Conditions Fulfilled)] 생각보다 날뛰어버렸군… 책상에서만 썩기 아까운 솜씨인걸.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_clear_ex_11104_1].dlg
   limit: do 140 znaków
   EN: Ran riot a little harder than I thought… It would be a waste to confine these capabilities to a desk.
   PL:
289. [Kwestia głosowa [battle_defeat_11104_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_defeat_11104_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Kwestia głosowa [battle_defeat_11104_1] (Defeat Wail)] 쯧… 벌써… 이렇게 녹슬다니.
   źródło: PersonalityVoiceDlg/Voice_Outist_SevenAsso6_11104.json :: dataList[id=battle_defeat_11104_1].dlg
   limit: do 120 znaków
   EN: Tch… I’ve rusted all too soon, haven’t I?
   PL:

## [000] Molar Office Fixer — Outis — 어금니 사무소 해결사
- ID Tożsamości: `11105` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 2 · HP bazowe: 68 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Tremor

291. [Karta Tożsamości — tytuł] 어금니 사무소\n해결사
   źródło: Personalities.json :: dataList[id=11105].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Molar Office\nFixer
   PL:
292. [Karta Tożsamości — nazwa] 오티스
   źródło: Personalities.json :: dataList[id=11105].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Karta Tożsamości — nazwa z tytułem] 오티스
   źródło: Personalities.json :: dataList[id=11105].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Karta Tożsamości — opis] 오티스의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=11105].desc
   limit: do 120 znaków
   EN: Outis's 5th Identity
   PL:
295. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 잠깐!
   źródło: Skills_personality-11.json :: dataList[id=1110501].levelList[level=1].name ; dataList[id=1110501].levelList[level=2].name ; dataList[id=1110501].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Wait Up!
   PL:
296. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 이 스킬이 버려지면 자신의 진동 횟수 3 증가
   źródło: Skills_personality-11.json :: dataList[id=1110501].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this Skill is Discarded, gain +3 Tremor Count
   PL:
297. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 진동 횟수만큼 흐트러짐 회복 (최대 10)
   źródło: Skills_personality-11.json :: dataList[id=1110501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Lower user's Stagger Threshold for every Tremor Count on self (Max 10)
   PL:
298. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 이 스킬이 버려지면 자신의 진동 횟수 4 증가\n[WhenUse] 자신의 진동 횟수 2 증가\n자신의 진동 횟수가 6 이상이면 최종 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1110501].levelList[level=2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is Discarded, gain +4 Tremor Count\n[WhenUse] Gain +2 Tremor Count\nAt 6+ Tremor Count, gain Final Power +1
   PL:
299. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수만큼 흐트러짐 회복 (최대 10)
   źródło: Skills_personality-11.json :: dataList[id=1110501].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1110501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold for every Tremor Count on self (Max 10)
   PL:
300. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 이 스킬이 버려지면 자신의 진동 횟수 4 증가\n[WhenUse] 자신의 진동 횟수 2 증가\n자신의 진동 횟수가 6 이상이면 최종 위력 +2
   źródło: Skills_personality-11.json :: dataList[id=1110501].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is Discarded, gain +4 Tremor Count\n[WhenUse] Gain +2 Tremor Count\nAt 6+ Tremor Count, gain Final Power +2
   PL:
301. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 가르기
   źródło: Skills_personality-11.json :: dataList[id=1110502].levelList[level=1].name ; dataList[id=1110502].levelList[level=2].name ; dataList[id=1110502].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 3 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Slice
   PL:
302. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림
   źródło: Skills_personality-11.json :: dataList[id=1110502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Discard the Skill of lowest rank in all of this unit's Skill Slots
   PL:
303. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Tremor
   PL:
304. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수가 6 이상일 때, 진동 폭발. 대상의 진동 횟수 1 감소
   źródło: Skills_personality-11.json :: dataList[id=1110502].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1110502].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1110502].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 6+ Tremor Count, trigger Tremor Burst. Reduce target's Tremor Count by 1
   PL:
306. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] 이 스킬이 버려지면 공격 레벨 증가 1을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림
   źródło: Skills_personality-11.json :: dataList[id=1110502].levelList[level=2].desc ; dataList[id=1110502].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [AttackUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: If this Skill is Discarded, gain 1 [AttackUp]\n[WhenUse] Discard the Skill of lowest rank in all of this unit's Skill Slots
   PL:
307. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110502].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Tremor
   PL:
308. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110502].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1110502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Tremor
   PL:
310. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1110502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 과감한 판단
   źródło: Skills_personality-11.json :: dataList[id=1110503].levelList[level=3].name ; dataList[id=1110503].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Daring Decision
   PL:
312. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 모든 스킬 슬롯의 스킬을 등급이 높은 순으로 버림.\n자신의 진동 횟수 10을 소모하여 코인 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1110503].levelList[level=3].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Discard this unit's Skills in descending order of ranks from all of its Skill Slots\nSpend 10 Tremor Count to gain Coin Power +1
   PL:
313. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 4 부여
   źródło: Skills_personality-11.json :: dataList[id=1110503].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1110503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Tremor
   PL:
314. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 스킬 사용 시 진동 횟수를 소모했으면, 진동 횟수 3 증가
   źródło: Skills_personality-11.json :: dataList[id=1110503].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1110503].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If the Skill spent Tremor Count, inflict +3 Tremor Count
   PL:
315. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 폭발. 대상의 진동 횟수 1 감소
   źródło: Skills_personality-11.json :: dataList[id=1110503].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Trigger Tremor Burst; after Tremor Burst, reduce target's Tremor Count by 1
   PL:
316. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 진동 폭발. 대상의 진동 횟수 1 감소
   źródło: Skills_personality-11.json :: dataList[id=1110503].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttackHead] 진동 폭발. 대상의 진동 횟수 1 감소
   źródło: Skills_personality-11.json :: dataList[id=1110503].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 자신의 모든 스킬 슬롯의 스킬을 등급이 높은 순으로 버림.\n자신의 진동 횟수 10을 소모하여 코인 위력 +2
   źródło: Skills_personality-11.json :: dataList[id=1110503].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Discard this unit's Skills in descending order of ranks from all of its Skill Slots\nSpend 10 Tremor Count to gain Coin Power +2
   PL:
319. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 폭발. 대상의 진동 횟수 1 감소
   źródło: Skills_personality-11.json :: dataList[id=1110503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Trigger Tremor Burst; after Tremor Burst, reduce target's Tremor Count by 1
   PL:
320. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 폭발. 대상의 진동 횟수 1 감소
   źródło: Skills_personality-11.json :: dataList[id=1110503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 진동 폭발. 대상의 진동 횟수 1 감소
   źródło: Skills_personality-11.json :: dataList[id=1110503].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [Obrona (ulepszenia 1,4) — nazwa] 숙취 해소
   źródło: Skills_personality-11.json :: dataList[id=1110504].levelList[level=1].name ; dataList[id=1110504].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Hangover Cure
   PL:
323. [Obrona (ulepszenia 1,4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림
   źródło: Skills_personality-11.json :: dataList[id=1110504].levelList[level=1].desc ; dataList[id=1110504].levelList[level=4].desc
   (powtórzenie elementu 302 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — nazwa] 무용담
   źródło: Passives.json :: dataList[id=1110501].name
   limit: do 40 znaków
   EN: Drinking Boast
   PL:
325. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — opis] 적에게 진동 폭발 시 흐트러짐 손상의 30%만큼 나태 속성 피해를 입힘 (최대 20. 소수점 버림)
   źródło: Passives.json :: dataList[id=1110501].desc
   limit: do 160 znaków
   EN: Upon triggering Tremor Burst on an enemy, inflict 30% of Raised Stagger Threshold as Sloth damage (Max 20; rounded down)
   PL:
326. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — nazwa] 윽박과 응원
   źródło: Passives.json :: dataList[id=1110521].name
   limit: do 40 znaków
   EN: Carrot & Stick
   PL:
327. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — opis] 진동 횟수가 가장 높은 아군 1명이 스킬 효과로 얻는 진동 횟수 +1
   źródło: Passives.json :: dataList[id=1110521].desc
   limit: do 120 znaków
   EN: 1 ally that has the most Tremor Count gains +1 more Tremor Count from Skill effects
   PL:
328. [Kwestia głosowa [get_11105_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=get_11105_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Kwestia głosowa [get_11105_1] (Identity Acquisition)] 아… 무슨 일이지? 머리 울리니까, 조금 천천히 말해줬으면 좋겠어.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=get_11105_1].dlg
   limit: do 120 znaków
   EN: Ah... What is it? Slowly, I've got a hell of a hangover.
   PL:
330. [Kwestia głosowa [lobby_morning_11105_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=lobby_morning_11105_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Kwestia głosowa [lobby_morning_11105_1] (Morning Greeting)] 윽… 아직도 숙취가… 아, 의뢰인가? 미안한데, 사무소 안에 다른 사람한테… 부탁, 우웁.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=lobby_morning_11105_1].dlg
   limit: do 120 znaków
   EN: Ugh... Damn hangovers... Ah, a contract? I'm sorry, but please go talk to the other— Hurk.
   PL:
332. [Kwestia głosowa [lobby_noon_11105_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=lobby_noon_11105_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [Kwestia głosowa [lobby_noon_11105_1] (Afternoon Greeting)] 후, 이제야 정신이 좀 돌아오는군. 오늘 점심식사에 반주는 걸러야겠어.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=lobby_noon_11105_1].dlg
   limit: do 120 znaków
   EN: Phew, I'm finally starting to feel a bit better. I think I'll skip wine this lunch.
   PL:
334. [Kwestia głosowa [lobby_night_11105_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=lobby_night_11105_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Kwestia głosowa [lobby_night_11105_1] (Evening Greeting)] 아, 저녁은 약속이 따로 있어서. 실례하지.\n…술을 마시는 건 아니냐고? 어쩔 수 없지 않은가! 이것도 중요한 거래처 약속이라고.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=lobby_night_11105_1].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ah, I'm meeting someone for dinner tonight, so if you'll excuse me...\n... Am I going out for drinks again? Well, it's not like I have a choice in the matter! It's for a meeting with a very important client, I'll have you know.
   PL:
336. [Kwestia głosowa [smalltalk_11105_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=smalltalk_11105_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Kwestia głosowa [smalltalk_11105_1] (Chatter #1)] 때로는 과감한 판단이 필요할 때가 있지.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=smalltalk_11105_1].dlg
   limit: do 120 znaków
   EN: Sometimes, what you need is a daring decision.
   PL:
338. [Kwestia głosowa [smalltalk_11105_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=smalltalk_11105_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Kwestia głosowa [smalltalk_11105_2] (Chatter #2)] 친구는 소중히 하는게 좋지. 언제 어디서 도움이 될지 모르니까 말이야.\n…속물이 아니냐고? 모르는 소리. 꼭 그런 금전적인 것만을 말한게 아니란 말이다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=smalltalk_11105_2].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Keep your friends close. You never know when or where they'll come in handy.\n... I'm too materialistic? Don't be so obtuse. I'm not talking about money... exclusively.
   PL:
340. [Kwestia głosowa [smalltalk_11105_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=smalltalk_11105_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Kwestia głosowa [smalltalk_11105_3] (Chatter #3)] 하아… 벌써부터 걱정이군. 이번 의뢰는 워프 열차를 타야하는데, 그건 타기만 하면 속이 울렁거리니…\n쯧, 술을 안마셔도 울렁거린다고!
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=smalltalk_11105_3].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Haah... I'm already nervous. We're going to have to take the WARP train for this contract, but every time I ride one of those things I feel like I'm about to hurl.\nUgh, it's not because I'm drunk!
   PL:
342. [Kwestia głosowa [smalltalk_11105_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=smalltalk_11105_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Kwestia głosowa [smalltalk_11105_4] (Post-Uptie Chat 1)] 나도 싸울 때 정도는 신중한 구석이 있다고. 자, 봐라. 이럴땐 적을 갈라버리는 것 보다는, 침착하게 막아낸 후에!\n처리하는 거지.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=smalltalk_11105_4].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I can be pretty crafty when it comes to fighting. Now, observe. Instead of going in straight for an attack, create an opening through a parry first!... Before taking them out.
   PL:
344. [Kwestia głosowa [smalltalk_11105_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=smalltalk_11105_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Kwestia głosowa [smalltalk_11105_5] (Post-Uptie Chat 2)] 뒷골목에 있었을 때는 이런 싸움이 일상이었지. 그래서 나설만한 일이 아니면 다른 두 녀석들에게 맡기고 싶지만…\n또, 그게 마음대로 되는 건 아니니까.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=smalltalk_11105_5].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: These scuffles were around every corner when I lived in the Backstreets. That's why, if it's not anything too challenging, I'd rather leave it to the other two...\nBut things don't always work out the way I want them to, do they?
   PL:
346. [Kwestia głosowa [neglect_11105_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=neglect_11105_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [Kwestia głosowa [neglect_11105_1] (Idle)] 물… 물을 좀 마셔둬야겠어…
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=neglect_11105_1].dlg
   limit: do 120 znaków
   EN: Water... I need some water...
   PL:
348. [Kwestia głosowa [gacksung_11105_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=gacksung_11105_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [Kwestia głosowa [gacksung_11105_1] (Uptying)] 굳이 나까지 나서야 할 정도는 아닌 듯 싶지만… 뭐, 부탁을 한다고 하니까. 알겠다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=gacksung_11105_1].dlg
   limit: do 120 znaków
   EN: Do I really need to get involved in this...? But since you're asking nicely, sure.
   PL:
350. [Kwestia głosowa [formation_11105_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=formation_11105_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Kwestia głosowa [formation_11105_1] (Deployment)] 아… 출발인가.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=formation_11105_1].dlg
   limit: do 120 znaków
   EN: Ah... Heading out?
   PL:
352. [Kwestia głosowa [battleentry_11105_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battleentry_11105_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Kwestia głosowa [battleentry_11105_1] (Stage Entry)] 자, 잠깐만. 천천히…
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battleentry_11105_1].dlg
   limit: do 120 znaków
   EN: W—wait up, slow down a sec...
   PL:
354. [Kwestia głosowa [battle_select_11105_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_select_11105_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Kwestia głosowa [battle_select_11105_1] (Viewed in Battle)] 뭐, 문제라도 있나.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_select_11105_1].dlg
   limit: do 120 znaków
   EN: What, something wrong?
   PL:
356. [Kwestia głosowa [battle_endcommand_11105_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_endcommand_11105_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [Kwestia głosowa [battle_endcommand_11105_1] (Commencing Attack)] 한바탕 해볼까.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_endcommand_11105_1].dlg
   limit: do 120 znaków
   EN: Let's get this party started.
   PL:
358. [Kwestia głosowa [battle_enemy_break_11105_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_enemy_break_11105_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Kwestia głosowa [battle_enemy_break_11105_1] (Enemy Stagger)] 아~ 힘조절이…
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_enemy_break_11105_1].dlg
   limit: do 120 znaków
   EN: Ah~ Did I hit ya too hard?
   PL:
360. [Kwestia głosowa [battle_break_11105_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_break_11105_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Kwestia głosowa [battle_break_11105_1] (Staggered)] 칫.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_break_11105_1].dlg
   limit: do 120 znaków
   EN: Tsk.
   PL:
362. [Kwestia głosowa [battle_kill_11105_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_kill_11105_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Kwestia głosowa [battle_kill_11105_1] (Enemy Killed)] 힘들군! 후, 그러니 알아서 잘 피해야지.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_kill_11105_1].dlg
   limit: do 120 znaków
   EN: Phew! Hmph, you could’ve tried dodging that.
   PL:
364. [Kwestia głosowa [battle_dead_11105_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_dead_11105_1].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
365. [Kwestia głosowa [battle_dead_11105_1] (Death)] 아… 너무 몸만 나섰나… 미련… 했군.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_dead_11105_1].dlg
   limit: do 120 znaków
   EN: Suppose... I went in too deep... without a good backup... That was foolish... of me.
   PL:
366. [Kwestia głosowa [choice_success_p_11105_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=choice_success_p_11105_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Kwestia głosowa [choice_success_p_11105_2] (Check Passed)] 흠? 좀 김이 빠지는데…
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=choice_success_p_11105_2].dlg
   limit: do 120 znaków
   EN: Huh? That's it...?
   PL:
368. [Kwestia głosowa [choice_fail_n_11105_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=choice_fail_n_11105_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Kwestia głosowa [choice_fail_n_11105_1] (Check Failed)] 젠장… 술 좀 깨고 해야했나.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=choice_fail_n_11105_1].dlg
   limit: do 120 znaków
   EN: Dammit... Should've sobered up first.
   PL:
370. [Kwestia głosowa [battle_clear_11105_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_clear_11105_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Kwestia głosowa [battle_clear_11105_1] (Victory Cry)] 뭐, 적당히 힘 쓴 결과지. 나쁘지 않지?
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_clear_11105_1].dlg
   limit: do 120 znaków
   EN: I wasn't even trying that hard. Not bad though, huh?
   PL:
372. [Kwestia głosowa [battle_clear_ex_11105_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_clear_ex_11105_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Kwestia głosowa [battle_clear_ex_11105_1] (Extra Conditions Fulfilled)] 다음 술자리 모험담은 이거군. 아주 완벽했어… 후후.
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_clear_ex_11105_1].dlg
   limit: do 120 znaków
   EN: Another tale to share with my drinking buddies. Huhu, excellent.
   PL:
374. [Kwestia głosowa [battle_defeat_11105_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_defeat_11105_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [Kwestia głosowa [battle_defeat_11105_1] (Defeat Wail)] 이럴 리가… 없는데? 하, 나 때문인가…
   źródło: PersonalityVoiceDlg/Voice_Outis_Molar_11105.json :: dataList[id=battle_defeat_11105_1].dlg
   limit: do 120 znaków
   EN: No... way...! Haah, was it my fault...?
   PL:

## [00] Cinq Assoc. South Section 4 — Outis — 남부 섕크 협회 4과
- ID Tożsamości: `11106` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Poise

376. [Karta Tożsamości — tytuł] 남부 섕크 협회\n4과
   źródło: Personalities.json :: dataList[id=11106].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cinq Assoc.\nSouth Section 4
   PL:
377. [Karta Tożsamości — nazwa] 오티스
   źródło: Personalities.json :: dataList[id=11106].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Karta Tożsamości — nazwa z tytułem] 오티스
   źródło: Personalities.json :: dataList[id=11106].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Karta Tożsamości — opis] 오티스의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=11106].desc
   limit: do 120 znaków
   EN: Outis's 6th Identity
   PL:
380. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 마르쉬
   źródło: Skills_personality-11.json :: dataList[id=1110601].levelList[level=1].name ; dataList[id=1110601].levelList[level=2].name ; dataList[id=1110601].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Marche
   PL:
381. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility] 2를 얻음
   źródło: Skills_personality-11.json :: dataList[id=1110601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste
   EN: [WhenUse] Gain 2 [Agility] next turn
   PL:
382. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1110601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain +1 [Breath] Count
   PL:
383. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1110601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 382 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 [Agility] 2를 얻음\n[WhenUse] 다음 턴에 이 슬롯이 [Aggro] 1을 얻음
   źródło: Skills_personality-11.json :: dataList[id=1110601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Agility], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain 2 [Agility] next turn\n[WhenUse] This slot gains 1 [Aggro] next turn
   PL:
385. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1110601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1110601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL:
386. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1110601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1110601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 [Agility] 2를 얻음\n[WhenUse] 다음 턴에 이 슬롯이 [Aggro] 3을 얻음
   źródło: Skills_personality-11.json :: dataList[id=1110601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Agility], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain 2 [Agility] next turn\n[WhenUse] This slot gains 3 [Aggro] next turn
   PL:
388. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 퍼니시옹
   źródło: Skills_personality-11.json :: dataList[id=1110602].levelList[level=1].name ; dataList[id=1110602].levelList[level=2].name ; dataList[id=1110602].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Punition
   PL:
389. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1110602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL:
390. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 2 얻음
   źródło: Skills_personality-11.json :: dataList[id=1110602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath]
   PL:
391. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL:
392. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 자신의 속도가 대상보다 높으면 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[WhenUse] 다음 턴에 이 슬롯이 [Aggro] 2를 얻음
   źródło: Skills_personality-11.json :: dataList[id=1110602].levelList[level=2].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Aggro] = 도발치 / Aggro
   EN: If this unit's Speed is faster than the target's, Coin Power +1\n[WhenUse] Gain +2 [Breath] Count\n[WhenUse] This Skill Slot gains 2 [Aggro] next turn
   PL:
393. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-11.json :: dataList[id=1110602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1110602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
394. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1110602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1110602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL:
395. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 속도가 대상보다 높으면 코인 위력 +2\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[WhenUse] 다음 턴에 이 슬롯이 [Aggro] 4를 얻음
   źródło: Skills_personality-11.json :: dataList[id=1110602].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Aggro] = 도발치 / Aggro
   EN: If this unit's Speed is faster than the target's, Coin Power +2\n[WhenUse] Gain +2 [Breath] Count\n[WhenUse] This Skill Slot gains 4 [Aggro] next turn
   PL:
396. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 발레스트라 팡트
   źródło: Skills_personality-11.json :: dataList[id=1110603].levelList[level=3].name ; dataList[id=1110603].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 8 · monety: 1 (+14)
   limit: do 40 znaków
   EN: Balestra Fente
   PL:
397. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 [Breath]이 7 이상이면 최종 위력 + 2\n[WinDuel] 합 횟수만큼 [Breath]을 얻음 (최대 10)
   źródło: Skills_personality-11.json :: dataList[id=1110603].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [WinDuel]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: At 7+ [Breath], Final Power +2\n[WinDuel] Gain [Breath] based on Clash count (Max 10)
   PL:
398. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DuelDeclaration_Outis] 부여
   źródło: Skills_personality-11.json :: dataList[id=1110603].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1110603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DuelDeclaration_Outis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DuelDeclaration_Outis] = 결투 선포 - 오티스 / Declared Duel - Outis
   EN: [OnSucceedAttack] Inflict [DuelDeclaration_Outis]
   PL:
399. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 속도가 가장 느린 아군 2명에게 다음 턴에 신속 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110603].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Apply 1 Haste next turn to 2 allies with the slowest Speed
   PL:
400. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 크리티컬 피해량 +50%
   źródło: Skills_personality-11.json :: dataList[id=1110603].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] +50% Damage on Critical Hit
   PL:
401. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 [Breath]이 7 이상이면 최종 위력 + 4\n[WinDuel] 합 횟수만큼 [Breath]을 얻음 (최대 10)
   źródło: Skills_personality-11.json :: dataList[id=1110603].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [WinDuel]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: At 7+ [Breath], Final Power +4\n[WinDuel] Gain [Breath] based on Clash Count (Max 10)
   PL:
402. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 속도가 가장 느린 아군 2명에게 다음 턴에 신속 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1110603].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Apply 2 Haste next turn to 2 allies with the slowest Speed
   PL:
403. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 크리티컬 피해량 +70%
   źródło: Skills_personality-11.json :: dataList[id=1110603].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] +70% Damage on Critical Hit
   PL:
404. [Obrona (ulepszenia 1,4) — nazwa] 르트레트
   źródło: Skills_personality-11.json :: dataList[id=1110604].levelList[level=1].name ; dataList[id=1110604].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 5 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Retraite
   PL:
405. [Obrona (ulepszenie 1) — opis] 자신의 속도가 공격자보다 높으면 코인 위력 +1\n[OnSucceedEvade] [Breath] 1 얻음 (최대 5)
   źródło: Skills_personality-11.json :: dataList[id=1110604].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedEvade], [Breath]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's, Coin Power +1\n[OnSucceedEvade] Gain 1 [Breath] (Max 5)
   PL:
406. [Obrona (ulepszenie 4) — opis] 자신의 속도가 공격자보다 높을수록 코인 위력 +1 (속도 차이 1 당 코인 위력 +1. 최대 3)\n[OnSucceedEvade] [Breath] 1 얻음 (최대 10)
   źródło: Skills_personality-11.json :: dataList[id=1110604].levelList[level=4].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedEvade], [Breath]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every Speed difference; max 3)\n[OnSucceedEvade] Gain 1 [Breath] (Max 10)
   PL:
407. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — nazwa] 흘리기
   źródło: Passives.json :: dataList[id=1110601].name
   limit: do 40 znaków
   EN: Redirect
   PL:
408. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — opis] 회피 성공 시 다음 턴에 [Agility] 1을 얻음 (최대 3회)
   źródło: Passives.json :: dataList[id=1110601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: On Evade, gain 1 [Agility] next turn (Max 3)
   PL:
409. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Pride) — nazwa] 흘리기
   źródło: Passives.json :: dataList[id=1110611].name
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Pride) — opis] 회피 성공 시 다음 턴에 [Agility] 1을 얻고, 자신의 흐트러짐 5 회복  (최대 3회)
   źródło: Passives.json :: dataList[id=1110611].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: On Evade, gain 1 [Agility] next turn; lower this unit's Stagger Threshold by 5 (Max 3)
   PL:
411. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — nazwa] 멘토의 지도
   źródło: Passives.json :: dataList[id=1110621].name
   limit: do 40 znaków
   EN: Mentor's Counsel
   PL:
412. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — opis] 속도가 가장 빠른 아군 1명의 속도가 모든 적보다 높으면, 해당 아군의 합 위력 +1
   źródło: Passives.json :: dataList[id=1110621].desc
   limit: do 140 znaków
   EN: If the fastest ally's Speed is faster than Speed of all enemies, the fastest ally gains Clash Power +1
   PL:
413. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Pride) — nazwa] 멘토의 지도
   źródło: Passives.json :: dataList[id=1110631].name
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Pride) — opis] 속도가 가장 빠른 아군 1명의 속도가 모든 적보다 높으면, 해당 아군의 합 위력 +1\n효과를 적용받는 아군이 섕크 협회 해결사면, 해당 캐릭터의 관통 피해량 +10%
   źródło: Passives.json :: dataList[id=1110631].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If the fastest ally's Speed is faster than Speed of all enemies, the fastest ally gains Clash Power +1\nIf the said ally is a Cinq Association Fixer, the fastest ally deals +10% Pierce Damage
   PL:
415. [Kwestia głosowa [get_11106_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=get_11106_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Kwestia głosowa [get_11106_1] (Identity Acquisition)] 자, 결투를 받아들여라. 혹은 추하게 도망치거나.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=get_11106_1].dlg
   limit: do 120 znaków
   EN: Now, accept the duel. Or flee like the dirty coward you are.
   PL:
417. [Kwestia głosowa [lobby_morning_11106_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=lobby_morning_11106_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Kwestia głosowa [lobby_morning_11106_1] (Morning Greeting)] 간밤 동안에는 안녕하셨습니까. 인사를 짧게 드려 죄송하군요. 금방 다음 일정이 있기 때문에.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=lobby_morning_11106_1].dlg
   limit: do 140 znaków
   EN: I hope you had a pleasant night. I must apologize for my curt greeting. I have business to attend to.
   PL:
419. [Kwestia głosowa [lobby_noon_11106_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=lobby_noon_11106_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Kwestia głosowa [lobby_noon_11106_1] (Afternoon Greeting)] 아하, 점심은 이쪽에서 드실 예정이셨군요. 간단하고 빠르지만, 고급스러운 일품 식사가 매력적이죠. 그럼, 저는 먼저 일어나보겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=lobby_noon_11106_1].dlg
   limit: do 210 znaków
   EN: Aha, so you plan to dine here. This place is well known for its simple, quick, yet high-quality à la carte meals. Now, if you will excuse me, I must take my leave.
   PL:
421. [Kwestia głosowa [lobby_night_11106_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=lobby_night_11106_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Kwestia głosowa [lobby_night_11106_1] (Evening Greeting)] 이만 들어가시는군요. 편안히 쉬십시오.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=lobby_night_11106_1].dlg
   limit: do 120 znaków
   EN: Turning in for the night, I see. Rest well.
   PL:
423. [Kwestia głosowa [smalltalk_11106_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=smalltalk_11106_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Kwestia głosowa [smalltalk_11106_1] (Chatter #1)] 순찰… 은 아닙니다. 골목가에는 꼭 대리 결투를 바라는 자들이 있기에, 영업 차원으로 돌아다닐 뿐이죠.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=smalltalk_11106_1].dlg
   limit: do 190 znaków
   EN: I wouldn't call this a patrol... no. The alleys are rife with those who seek us to duel in their stead. I am simply in search of potential clients.
   PL:
425. [Kwestia głosowa [smalltalk_11106_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=smalltalk_11106_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Kwestia głosowa [smalltalk_11106_2] (Chatter #2)] 모든 전투의 움직임이 중요하겠지만… 저는 그 중에서도 딱 한 합이 중요하다고 생각합니다.\n반드시 상대를 꿰뚫고 말겠다는… 진정함을 담은 한 합 말입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=smalltalk_11106_2].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In combat, every move is critical indeed... But I am of the opinion that there is one move that holds paramount importance.\nA single clash, a determined thrust to impale my opponent.
   PL:
427. [Kwestia głosowa [smalltalk_11106_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=smalltalk_11106_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Kwestia głosowa [smalltalk_11106_3] (Chatter #3)] 아무래도, 다수의 적을 상대하는 건 저희의 전투 방식과는 거리가 멀긴 합니다.\n하지만, 그들이 좁은 골목에서 줄지어 온다면 얼마든지 대응해 줄 수 있습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=smalltalk_11106_3].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Fighting multiple enemies at once is antithetical to the way we duel, yes.\nBut if they were to be corralled into a narrow alleyway, I am rather confident that I should have no trouble making short work of them.
   PL:
429. [Kwestia głosowa [smalltalk_11106_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=smalltalk_11106_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Kwestia głosowa [smalltalk_11106_4] (Post-Uptie Chat 1)] 검을 놀리는 것만이 예사는 아닙니다. 기다란 검날이 거치적 거릴 정도로 가까운 거리의 적을 상대할 경우도 많습니다.\n그럴 때를 대비한 비장의 기술 하나 정도는, 갖추어야 겠지요.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=smalltalk_11106_4].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One cannot twirl their sword through every battle. Sometimes we face foes that prefer close-quarters combat, so close that our blades become unwieldy.\nI would need to keep a trick up my sleeve in case of such instances.
   PL:
431. [Kwestia głosowa [smalltalk_11106_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=smalltalk_11106_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Kwestia głosowa [smalltalk_11106_5] (Post-Uptie Chat 2)] 잔뜩 흥분한 적이 달려들어오는 때야 말로, 가장 커다란 기회입니다.\n그 힘을 그대로 이용해 적에게 돌려줄 수 있기 때문이죠. 아무 힘을 들이지도 않고 말입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=smalltalk_11106_5].dlg
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A duelist's greatest opportunity is when the opponent attempts a furious charge.\nI can redirect that very force against them without spending much of my own energy.
   PL:
433. [Kwestia głosowa [neglect_11106_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=neglect_11106_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Kwestia głosowa [neglect_11106_1] (Idle)] 특별한 용건이 없다면… 잠시 자리를 비우겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=neglect_11106_1].dlg
   limit: do 120 znaków
   EN: I will take my leave, if you have no further business to discuss.
   PL:
435. [Kwestia głosowa [gacksung_11106_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=gacksung_11106_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Kwestia głosowa [gacksung_11106_1] (Uptying)] 예, 인정해 주신다면 영광일 따름입니다. 계속해서 실망스럽지 않은 모습을 보여드리겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=gacksung_11106_1].dlg
   limit: do 120 znaków
   EN: Yes, it is an honor to be acknowledged by you. I will not disappoint.
   PL:
437. [Kwestia głosowa [formation_11106_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=formation_11106_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Kwestia głosowa [formation_11106_1] (Deployment)] 언제나 준비되어있다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=formation_11106_1].dlg
   limit: do 120 znaków
   EN: I'm always ready.
   PL:
439. [Kwestia głosowa [battleentry_11106_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battleentry_11106_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Kwestia głosowa [battleentry_11106_1] (Stage Entry)] 나의 상대는, 어디 있는가!
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battleentry_11106_1].dlg
   limit: do 120 znaków
   EN: Step forth, my opponent!
   PL:
441. [Kwestia głosowa [battle_select_11106_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_select_11106_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Kwestia głosowa [battle_select_11106_1] (Viewed in Battle)] …지금은 바쁩니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_select_11106_1].dlg
   limit: do 120 znaków
   EN: ... I'm a bit preoccupied at the moment.
   PL:
443. [Kwestia głosowa [battle_endcommand_11106_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_endcommand_11106_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Kwestia głosowa [battle_endcommand_11106_1] (Commencing Attack)] 완벽한 거리군.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_endcommand_11106_1].dlg
   limit: do 120 znaków
   EN: A perfect distance.
   PL:
445. [Kwestia głosowa [battle_enemy_break_11106_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_enemy_break_11106_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Kwestia głosowa [battle_enemy_break_11106_1] (Enemy Stagger)] 흥, 뻔하지.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_enemy_break_11106_1].dlg
   limit: do 120 znaków
   EN: Hmph, predictable.
   PL:
447. [Kwestia głosowa [battle_break_11106_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_break_11106_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Kwestia głosowa [battle_break_11106_1] (Staggered)] 윽…
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_break_11106_1].dlg
   limit: do 120 znaków
   EN: Agh...
   PL:
449. [Kwestia głosowa [battle_kill_11106_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_kill_11106_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Kwestia głosowa [battle_kill_11106_1] (Enemy Killed)] 자, 나의 승리다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_kill_11106_1].dlg
   limit: do 120 znaków
   EN: Ah, my victory.
   PL:
451. [Kwestia głosowa [battle_dead_11106_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_dead_11106_1].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Kwestia głosowa [battle_dead_11106_1] (Death)] 크윽… 이런… 수치가…
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_dead_11106_1].dlg
   limit: do 120 znaków
   EN: Gah... what... a shame...
   PL:
453. [Kwestia głosowa [choice_success_p_11106_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=choice_success_p_11106_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Kwestia głosowa [choice_success_p_11106_2] (Check Passed)] 흠, 어려운 수법은 아니더군.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=choice_success_p_11106_2].dlg
   limit: do 120 znaków
   EN: Hm, that was rather straightforward.
   PL:
455. [Kwestia głosowa [choice_fail_n_11106_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=choice_fail_n_11106_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Kwestia głosowa [choice_fail_n_11106_1] (Check Failed)] …이런 결투는 예상에 없던…
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=choice_fail_n_11106_1].dlg
   limit: do 120 znaków
   EN: ... I wasn't expecting to duel something like this...
   PL:
457. [Kwestia głosowa [battle_clear_11106_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_clear_11106_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Kwestia głosowa [battle_clear_11106_1] (Victory Cry)] 깔끔한 결투였습니다. 모두가 이 검 앞에 침묵했군요.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_clear_11106_1].dlg
   limit: do 120 znaków
   EN: A fair duel. All fell silent before this blade.
   PL:
459. [Kwestia głosowa [battle_clear_ex_11106_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_clear_ex_11106_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Kwestia głosowa [battle_clear_ex_11106_1] (Extra Conditions Fulfilled)] 방금의 결투를 그림으로 그려냈다면, 분명 이것은 걸작이었을 것입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_clear_ex_11106_1].dlg
   limit: do 130 znaków
   EN: I can say with certainty that a painting of this duel would become nothing short of a masterpiece.
   PL:
461. [Kwestia głosowa [battle_defeat_11106_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_defeat_11106_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Kwestia głosowa [battle_defeat_11106_1] (Defeat Wail)] 결과에 승복하는 것도 결투자의 예법… 이겠죠.
   źródło: PersonalityVoiceDlg/Voice_Outis_Cinq_11106.json :: dataList[id=battle_defeat_11106_1].dlg
   limit: do 120 znaków
   EN: I suppose a proper duelist must accept when she is... beaten.
   PL:

## [000] Lobotomy E.G.O::Magic Bullet — Outis — 로보토미 E.G.O:: 마탄
- ID Tożsamości: `11107` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9102 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Burn

463. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n마탄
   źródło: Personalities.json :: dataList[id=11107].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::Magic Bullet
   PL:
464. [Karta Tożsamości — nazwa] 오티스
   źródło: Personalities.json :: dataList[id=11107].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Karta Tożsamości — nazwa z tytułem] 오티스
   źródło: Personalities.json :: dataList[id=11107].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Karta Tożsamości — opis] 오티스의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=11107].desc
   limit: do 120 znaków
   EN: Outis's 7th Identity
   PL:
467. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 착화
   źródło: Skills_personality-11.json :: dataList[id=1110701].levelList[level=1].name ; dataList[id=1110701].levelList[level=2].name ; dataList[id=1110701].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Ignition
   PL:
468. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [DarkFlame] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110701].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1110701].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DarkFlame]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DarkFlame] = 흑염 / Dark Flame
   EN: [OnSucceedAttackHead] Inflict 1 [DarkFlame] next turn
   PL:
469. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [DarkFlame]만큼 [Combustion] 부여
   źródło: Skills_personality-11.json :: dataList[id=1110701].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1110701].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1110701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DarkFlame], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DarkFlame] = 흑염 / Dark Flame; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict [Combustion] equal to [DarkFlame] on target
   PL:
470. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Combustion] 3 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-11.json :: dataList[id=1110701].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Coin Power +1 for every 3 [Combustion] on target (Max 2)
   PL:
471. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Combustion] 3 당 코인 위력 +1 (최대 3)
   źródło: Skills_personality-11.json :: dataList[id=1110701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Coin Power +1 for every 3 [Combustion] on target (Max 3)
   PL:
472. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DarkFlame] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DarkFlame]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DarkFlame] = 흑염 / Dark Flame
   EN: [OnSucceedAttack] Inflict 1 [DarkFlame] next turn
   PL:
473. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 마탄 기폭
   źródło: Skills_personality-11.json :: dataList[id=1110702].levelList[level=1].name ; dataList[id=1110702].levelList[level=2].name ; dataList[id=1110702].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Detonate Magic Bullet
   PL:
474. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 대상의 [Combustion]이 6 이상이면 코인 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1110702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Coin Power +1
   PL:
475. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [FreischutzShotCount]이 4 미만이면 [FreischutzShotCount]이 1 증가하고, 다음 턴에 [FreischutzShotCount]만큼 [DarkFlame] 부여
   źródło: Skills_personality-11.json :: dataList[id=1110702].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1110702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1110702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FreischutzShotCount], [DarkFlame]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FreischutzShotCount] = 마탄 / Magic Bullet; [DarkFlame] = 흑염 / Dark Flame
   EN: [OnSucceedAttack] At less than 4 [FreischutzShotCount], gain 1 [FreischutzShotCount]; then, inflict [DarkFlame] equal to [FreischutzShotCount] next turn
   PL:
476. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 대상의 [DarkFlame]만큼 [Combustion] 부여
   źródło: Skills_personality-11.json :: dataList[id=1110702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DarkFlame], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DarkFlame] = 흑염 / Dark Flame; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Inflict [Combustion] equal to [DarkFlame] on target
   PL:
477. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Combustion] 6 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-11.json :: dataList[id=1110702].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Coin Power +1 for every 6 [Combustion] on target (Max 2)
   PL:
478. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [DarkFlame]만큼 [Combustion] 부여
   źródło: Skills_personality-11.json :: dataList[id=1110702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1110702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Combustion] 6 당 코인 위력 +1 (최대 3)
   źródło: Skills_personality-11.json :: dataList[id=1110702].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Coin Power +1 for every 6 [Combustion] on target (Max 3)
   PL:
480. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 마탄 사격
   źródło: Skills_personality-11.json :: dataList[id=1110703].levelList[level=3].name ; dataList[id=1110703].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 15 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Magic Bullet Fire
   PL:
481. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Combustion] 수치 1당 피해량 0.5% 증가 (최대 15%)\n\n[BeforeAttack] [FreischutzShotCount] 1 증가\n- ([FreischutzShotCount] - 1) x 5 만큼 정신력 감소\n- 공격 가중치가 [FreischutzShotCount] 값으로 변경\n- 정신력이 10 이하일 때 50% 확률로 피아식별 없이 공격\n\n[EndSkill] [FreischutzShotCount]이 7이면 0으로 초기화 (마지막 탄환을 소모한 것으로 취급함)
   źródło: Skills_personality-11.json :: dataList[id=1110703].levelList[level=3].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [BeforeAttack], [FreischutzShotCount], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [FreischutzShotCount] = 마탄 / Magic Bullet; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +0.5% damage for every [Combustion] on target (Max 15%)\n\n[BeforeAttack] Gain 1 [FreischutzShotCount]\n- Lose (([FreischutzShotCount] -1)x5) SP\n- Atk Weight becomes equal to [FreischutzShotCount] value\n- At 10 or less SP, 50% chance to attack indiscriminately\n\n[EndSkill] If at 7 [FreischutzShotCount], reset to 0 (Counts as spending the last Ammo)
   PL:
482. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [FreischutzShotCount]만큼 [DarkFlame] 부여
   źródło: Skills_personality-11.json :: dataList[id=1110703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1110703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FreischutzShotCount], [DarkFlame]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FreischutzShotCount] = 마탄 / Magic Bullet; [DarkFlame] = 흑염 / Dark Flame
   EN: [OnSucceedAttack] Inflict [DarkFlame] equal to [FreischutzShotCount] next turn
   PL:
483. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">대상의 [Combustion] 수치 1당 피해량 1% 증가 (최대 30%)</style>\n\n[BeforeAttack] [FreischutzShotCount] 1 증가\n- ([FreischutzShotCount] - 1) x 5 만큼 정신력 감소\n- 공격 가중치가 [FreischutzShotCount] 값으로 변경\n- 정신력이 10 이하일 때 50% 확률로 피아식별 없이 공격\n\n[EndSkill] [FreischutzShotCount]이 7이면 0으로 초기화 (마지막 탄환을 소모한 것으로 취급함)
   źródło: Skills_personality-11.json :: dataList[id=1110703].levelList[level=4].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [BeforeAttack], [FreischutzShotCount], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [FreischutzShotCount] = 마탄 / Magic Bullet; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">Deal +1% damage for every [Combustion] on target (Max 30%)</style>\n\n[BeforeAttack] Gain 1 [FreischutzShotCount]\n- Lose (([FreischutzShotCount] -1)x5) SP\n- Atk Weight becomes equal to [FreischutzShotCount] value\n- At 10 or less SP, 50% chance to attack indiscriminately\n\n[EndSkill] If at 7 [FreischutzShotCount], reset to 0 (Counts as spending the last Ammo)
   PL:
484. [Obrona (ulepszenia 1,4) — nazwa] 마탄의 대가
   źródło: Skills_personality-11.json :: dataList[id=1110704].levelList[level=1].name ; dataList[id=1110704].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: The Price of a Bullet
   PL:
485. [Obrona (ulepszenie 1) — opis] [WhenUse] [FreischutzShotCount] 1 증가 (턴 당 1회)\n[EndSkillAll] [FreischutzShotCount]만큼 정신력 감소
   źródło: Skills_personality-11.json :: dataList[id=1110704].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [FreischutzShotCount], [EndSkillAll]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FreischutzShotCount] = 마탄 / Magic Bullet; [EndSkillAll] = [스킬 종료시] / [Skill End]
   EN: [WhenUse] Gain 1 [FreischutzShotCount] (Once per turn)\n[EndSkillAll] Lose SP equal to [FreischutzShotCount]
   PL:
486. [Obrona (ulepszenie 4) — opis] [WhenUse] [FreischutzShotCount] 1 증가 (턴 당 1회)\n[WhenUse] ([FreischutzShotCount] x 2)만큼 최종 위력이 증가\n[EndSkillAll] [FreischutzShotCount]만큼 정신력 감소
   źródło: Skills_personality-11.json :: dataList[id=1110704].levelList[level=4].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [FreischutzShotCount], [EndSkillAll]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FreischutzShotCount] = 마탄 / Magic Bullet; [EndSkillAll] = [스킬 종료시] / [Skill End]
   EN: [WhenUse] Gain 1 [FreischutzShotCount] (Once per turn)\n[WhenUse] Gain Final Power equal to ([FreischutzShotCount] x2)\n[EndSkillAll] Lose SP equal to [FreischutzShotCount]
   PL:
487. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — nazwa] 사수의 파이프
   źródło: Passives.json :: dataList[id=1110701].name
   limit: do 40 znaków
   EN: The Marksman's Smoking Pipe
   PL:
488. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — opis] 메인 공격 대상의 방어 레벨이 4 이상 감소된 상태면, 공격 전 (메인 공격 대상의 [Combustion]/2)만큼 [Breath]을 얻음 (턴 당 최대 20)
   źródło: Passives.json :: dataList[id=1110701].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Breath]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Breath] = 호흡 / Poise
   EN: If the main target's Defense Level is currently lowered by 4 or more, gain ([Combustion] on main target/2) [Breath] Before Attack (Max 20 per turn)
   PL:
489. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Pride) — nazwa] 사수의 파이프
   źródło: Passives.json :: dataList[id=1110711].name
   (powtórzenie elementu 487 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Pride) — opis] 메인 공격 대상의 방어 레벨이 4 이상 감소된 상태면, 공격 전 메인 공격 대상의 [Combustion]만큼 [Breath]을 얻음 (턴 당 최대 20)
   źródło: Passives.json :: dataList[id=1110711].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Breath]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Breath] = 호흡 / Poise
   EN: If the main target's Defense Level is currently lowered by 4 or more, gain ([Combustion] on main target) [Breath] Before Attack (Max 20 per turn)
   PL:
491. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — nazwa] 의뢰 작업
   źródło: Passives.json :: dataList[id=1110721].name
   limit: do 40 znaków
   EN: Request Work
   PL:
492. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — opis] 정신력이 가장 높은 아군 1명의 E.G.O 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1110721].desc
   limit: do 120 znaków
   EN: 1 ally with the most SP deals +10% damage with E.G.O Skills
   PL:
493. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Pride) — nazwa] 의뢰 작업
   źródło: Passives.json :: dataList[id=1110731].name
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Pride) — opis] 정신력이 가장 높은 아군 1명의 E.G.O 스킬의 피해량 +10%\nE.G.O 자원을 7개 이상 소모하는 E.G.O 스킬이면, 추가로 피해량 +5%
   źródło: Passives.json :: dataList[id=1110731].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 1 ally with the most SP deals +10% damage with E.G.O Skills\nIf the E.G.O Skill consumes 7+ E.G.O resources, deal additional +5% damage
   PL:
495. [Kwestia głosowa [get_11107_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=get_11107_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Kwestia głosowa [get_11107_1] (Identity Acquisition)] 내 앞에 서지 말도록. 악마가 깃든 탄환의 과녁 중 하나가 되고 싶은 게 아니라면.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=get_11107_1].dlg
   limit: do 140 znaków
   EN: Don't step into my line of fire. Unless you'd like to be made a target of the Devil's Bullet, that is.
   PL:
497. [Kwestia głosowa [lobby_morning_11107_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=lobby_morning_11107_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Kwestia głosowa [lobby_morning_11107_1] (Morning Greeting)] 아침의 고요엔 익숙해지지 마시길 바랍니다, 곧 격리실의 유리가 꿰뚫리는 탄환 소리가 들려올테니까.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=lobby_morning_11107_1].dlg
   limit: do 170 znaków
   EN: Don't get too used to the tranquility of this morning. A stray bullet will soon shatter through the windows of a containment unit.
   PL:
499. [Kwestia głosowa [lobby_noon_11107_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=lobby_noon_11107_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Kwestia głosowa [lobby_noon_11107_1] (Afternoon Greeting)] 다른 부서에서는 베이거나 찢어진 상처들을 일종의 훈장처럼 여기는 것 같습니다. 참 덧없는 소리입니다, 이 부서에선 살아남은 것 자체가 훈장일텐데.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=lobby_noon_11107_1].dlg
   limit: do 230 znaków
   EN: It seems that other departments wear their cuts and bruises like medals. A most meaningless posturing. In our department... survival alone is more than enough of a recognition.
   PL:
501. [Kwestia głosowa [lobby_night_11107_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=lobby_night_11107_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Kwestia głosowa [lobby_night_11107_1] (Evening Greeting)] 소등이 되고 나면 더욱 긴장해야 합니다. 그것은 어둠 속에서도 우리를 조준하고 있을테니.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=lobby_night_11107_1].dlg
   limit: do 160 znaków
   EN: We must be at full alert if the light goes out. That thing... must be watching us through its sights. Even in the dark.
   PL:
503. [Kwestia głosowa [smalltalk_11107_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=smalltalk_11107_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Kwestia głosowa [smalltalk_11107_1] (Chatter #1)] 만약 제가 이곳에 오지 않았다면, 어느 날개의 군인이 되었을지도 모르겠습니다. 모두가 고함을 지르며 도망가고 있을 때, 저는 달궈진 무기를 들고 화학연기가 자욱한 이곳의 어둠을 정확하게 조준하는 방법을 익히려고 했으니.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=smalltalk_11107_1].dlg
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Had I not found my home here, perhaps I would have become a soldier of a different Wing.\nWhen all personnel began fleeing in terror, I held my firearm fast, its muzzle glowing red-hot, and sought my target in the dull gloom of the chemical smoke.
   PL:
505. [Kwestia głosowa [smalltalk_11107_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=smalltalk_11107_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Kwestia głosowa [smalltalk_11107_2] (Chatter #2)] 교육팀의 팀장으로써 제가 알려주는 것은 한 가지입니다. 이 곳에서는 인간의 이성을 믿지 말라고. 나조차.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=smalltalk_11107_2].dlg
   limit: do 170 znaków
   EN: As Captain of the Training Team, I have but one advice. You must NOT place your faith in human rationality here. Not even mine.
   PL:
507. [Kwestia głosowa [smalltalk_11107_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=smalltalk_11107_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Kwestia głosowa [smalltalk_11107_3] (Chatter #3)] 팀원 중엔 저를 영웅 마냥 존경하는 자들도, 혹은 피도 눈물도 없는 냉혈한으로 두려워 하는 이들도 있나 봅니다. 우습지 않습니까, 저는 언제나 관리자님의 명령을 행했을 뿐인데 말이죠.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=smalltalk_11107_3].dlg
   limit: do 240 znaków
   EN: Some of my team look up to me as a hero. Some fear me, thinking me a cold-blooded killer. Ridiculous, isn't it? All I have ever done was to follow the manager's orders to the letter.
   PL:
509. [Kwestia głosowa [smalltalk_11107_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=smalltalk_11107_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Kwestia głosowa [smalltalk_11107_4] (Post-Uptie Chat 1)] 저를 가장 망설이게 했던 건, 제 총구가 조준하는 것들에 대한 정의입니다. 탄환이 그들의 심장을 꿰뚫고 관자놀이를 관통할 거라는 제 생각이, 결국 제 총의 조준력을 떨어뜨린다니… 호드님에게 상담을 받고 생각을 고쳤습니다. 이 총구가 조준하는 건 그저… 과녁들일 뿐이라고.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=smalltalk_11107_4].dlg
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I used to hesitate about... the 'definition' of what I killed. Because if I were to define my targets in certain ways... the thought of the bullet puncturing their hearts and breaking their skulls caused my aim to waver...\nSo I went to Ms. Hod for her counsel. There, I came to an understanding that they're all just... targets. Nothing more, nothing less.
   PL:
511. [Kwestia głosowa [smalltalk_11107_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=smalltalk_11107_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Kwestia głosowa [smalltalk_11107_5] (Post-Uptie Chat 2)] 알고 있습니다. 언젠가 이 탄환이 떨어진다면, 마지막 탄환은 저의 머리를 향할 겁니다. 그리고 고통 없이 정확히 한가운데를 명중시키겠지요. 제가 겨냥했던 모든 것들이 그랬듯이.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=smalltalk_11107_5].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Yes, I am aware. That at the bottom of this magazine awaits a bullet with my name on it. It will strike me down with a painless precision.\n... As I have done so to all that I have set my sights on.
   PL:
513. [Kwestia głosowa [neglect_11107_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=neglect_11107_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Kwestia głosowa [neglect_11107_1] (Idle)] 이 탄환에는 세금이 매겨지지 않는지 궁금합니다. 환상체로부터 나온 것에는 제한이 없는 것인지, 아니면 이 또한 로보토미사에서 비용을 치르고 있는지.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=neglect_11107_1].dlg
   limit: do 220 znaków
   EN: One must wonder if this bullet is taxed as well. Are they an exception, as they were generated by an Abnormality? Or is the Lobotomy Corporation taxed for them regardless?
   PL:
515. [Kwestia głosowa [gacksung_11107_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=gacksung_11107_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Kwestia głosowa [gacksung_11107_1] (Uptying)] 그것이 제게 계약에 대해 제안했을 때가 떠오르는군요.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=gacksung_11107_1].dlg
   limit: do 120 znaków
   EN: I remember the day when it offered me the contract.
   PL:
517. [Kwestia głosowa [formation_11107_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=formation_11107_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Kwestia głosowa [formation_11107_1] (Deployment)] 준비는 항상 되어있습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=formation_11107_1].dlg
   limit: do 120 znaków
   EN: I am always ready.
   PL:
519. [Kwestia głosowa [battleentry_11107_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battleentry_11107_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Kwestia głosowa [battleentry_11107_1] (Stage Entry)] 탄피가 떨어질 때군요.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battleentry_11107_1].dlg
   limit: do 120 znaków
   EN: Time to let the shells hit the floor.
   PL:
521. [Kwestia głosowa [battle_select_11107_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_select_11107_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Kwestia głosowa [battle_select_11107_1] (Viewed in Battle)] 조준중입니다. 신속하게 용건을…
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_select_11107_1].dlg
   limit: do 120 znaków
   EN: I have them in my sights. State your business, quickly.
   PL:
523. [Kwestia głosowa [battle_endcommand_11107_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_endcommand_11107_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Kwestia głosowa [battle_endcommand_11107_1] (Commencing Attack)] 완벽한 한발을 위해.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_endcommand_11107_1].dlg
   limit: do 120 znaków
   EN: For the perfect shot.
   PL:
525. [Kwestia głosowa [battle_enemy_break_11107_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_enemy_break_11107_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Kwestia głosowa [battle_enemy_break_11107_1] (Enemy Stagger)] 적중.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_enemy_break_11107_1].dlg
   limit: do 120 znaków
   EN: Bullseye.
   PL:
527. [Kwestia głosowa [battle_break_11107_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_break_11107_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Kwestia głosowa [battle_break_11107_1] (Staggered)] 큭…
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_break_11107_1].dlg
   limit: do 120 znaków
   EN: Ach...
   PL:
529. [Kwestia głosowa [battle_kill_11107_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_kill_11107_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Kwestia głosowa [battle_kill_11107_1] (Enemy Killed)] 안심해라, 고통은 없어.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_kill_11107_1].dlg
   limit: do 120 znaków
   EN: Worry not. There won't be any pain.
   PL:
531. [Kwestia głosowa [battle_dead_11107_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_dead_11107_1].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Kwestia głosowa [battle_dead_11107_1] (Death)] …계약은 이것으로 끝이 아닐테지…
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_dead_11107_1].dlg
   limit: do 120 znaków
   EN: ... The contract won't end here...
   PL:
533. [Kwestia głosowa [choice_success_p_11107_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=choice_success_p_11107_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Kwestia głosowa [choice_success_p_11107_2] (Check Passed)] 무엇이든 맞출 수 있는 탄환이니 말입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=choice_success_p_11107_2].dlg
   limit: do 120 znaków
   EN: Indeed. These bullets are infallible.
   PL:
535. [Kwestia głosowa [choice_fail_n_11107_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=choice_fail_n_11107_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Kwestia głosowa [choice_fail_n_11107_1] (Check Failed)] 지금은 빗나간 것처럼 보여도 탄환은 돌아올 것입니다. 그런 계약이니까.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=choice_fail_n_11107_1].dlg
   limit: do 130 znaków
   EN: Though you may see a missed shot, I see an inevitability. For that is the nature of the contract.
   PL:
537. [Kwestia głosowa [battle_clear_11107_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_clear_11107_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Kwestia głosowa [battle_clear_11107_1] (Victory Cry)] 탄환은 계속해서 만들어지고 방아쇠도 계속해서 당겨질 겁니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_clear_11107_1].dlg
   limit: do 120 znaków
   EN: The bullets will continue to regenerate, and I will continue to pull the trigger.
   PL:
539. [Kwestia głosowa [battle_clear_ex_11107_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_clear_ex_11107_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Kwestia głosowa [battle_clear_ex_11107_1] (Extra Conditions Fulfilled)] 관리자님이 명하는 것이라면, 탄환은 어디든 무엇이든 누구든 관통해냅니다. 설령 사랑하는 사람일지라도.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_clear_ex_11107_1].dlg
   limit: do 200 znaków
   EN: Should the Manager order me to fire... the bullet will penetrate the target. Wherever it is, whichever it is, or whoever it is. Even... the loved ones.
   PL:
541. [Kwestia głosowa [battle_defeat_11107_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_defeat_11107_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Kwestia głosowa [battle_defeat_11107_1] (Defeat Wail)] 아직까지도 저의 총구엔 까닭 모를 망설임이 남아있었나 봅니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_LEGO_11107.json :: dataList[id=battle_defeat_11107_1].dlg
   limit: do 120 znaków
   EN: Perhaps a certain hesitation remained still in my sights.
   PL:

## [000] Wuthering Heights Chief Butler — Outis — 워더링하이츠 치프 버틀러
- ID Tożsamości: `11108` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 4 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Sinking

543. [Karta Tożsamości — tytuł] 워더링하이츠\n치프 버틀러
   źródło: Personalities.json :: dataList[id=11108].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Wuthering Heights\nChief Butler
   PL:
544. [Karta Tożsamości — nazwa] 오티스
   źródło: Personalities.json :: dataList[id=11108].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Karta Tożsamości — nazwa z tytułem] 오티스
   źródło: Personalities.json :: dataList[id=11108].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Karta Tożsamości — opis] 오티스의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=11108].desc
   limit: do 120 znaków
   EN: Outis's 8th Identity
   PL:
547. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 노크
   źródło: Skills_personality-11.json :: dataList[id=1110801].levelList[level=1].name ; dataList[id=1110801].levelList[level=2].name ; dataList[id=1110801].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Knocking
   PL:
548. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1110801].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1110801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1110801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL:
549. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상의 [Sinking]이 7 이상이면 코인 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1110801].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 7+ Sinking, Coin Power +1
   PL:
550. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking]이 5 이상이면 코인 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1110801].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 5+ [Sinking], Coin Power +1
   PL:
551. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 먼지 털이
   źródło: Skills_personality-11.json :: dataList[id=1110802].levelList[level=1].name ; dataList[id=1110802].levelList[level=2].name ; dataList[id=1110802].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Dusting
   PL:
552. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] [Sinking] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1110802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Sinking]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Sinking] = 침잠 / Sinking
   EN: [WinDuel] Inflict +1 [Sinking] Count
   PL:
553. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_personality-11.json :: dataList[id=1110802].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1110802].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1110802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL:
554. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1110802].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1110802].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1110802].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WinDuel] [Sinking] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1110802].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Sinking]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Sinking] = 침잠 / Sinking
   EN: [WinDuel] Inflict +2 [Sinking] Count
   PL:
556. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking]이 5 이상이면 코인 위력 +1\n[WinDuel] [Sinking] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1110802].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has 5+ [Sinking], Coin Power +1\n[WinDuel] Inflict +2 [Sinking] Count
   PL:
557. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 마님의 뜻대로
   źródło: Skills_personality-11.json :: dataList[id=1110803].levelList[level=3].name ; dataList[id=1110803].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: As Mistress Commands
   PL:
558. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WinDuel] [Sinking] 횟수 3 증가
   źródło: Skills_personality-11.json :: dataList[id=1110803].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Sinking]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Sinking] = 침잠 / Sinking
   EN: [WinDuel] Inflict +3 [Sinking] Count
   PL:
559. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [EchoOfMansion] 3 부여
   źródło: Skills_personality-11.json :: dataList[id=1110803].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1110803].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EchoOfMansion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor
   EN: [OnSucceedAttack] Inflict 3 [EchoOfMansion] next turn
   PL:
560. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상에게 [EchoOfMansion]가 있으면, 대상의 [Sinking] 위력의 절반만큼 우울 속성 피해를 줌 (최대 20)
   źródło: Skills_personality-11.json :: dataList[id=1110803].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EchoOfMansion], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target has [EchoOfMansion], inflict Gloom Affinity damage equal to half of [Sinking] Potency on target (max 20)
   PL:
561. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking]이 7 이상이면 코인 위력 +1\n[WinDuel] [Sinking] 횟수 3 증가
   źródło: Skills_personality-11.json :: dataList[id=1110803].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has 7+ [Sinking], Coin Power +1\n[WinDuel] Inflict +3 [Sinking] Count
   PL:
562. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상에게 [EchoOfMansion]가 있으면, 대상의 [Sinking] 위력만큼 우울 속성 피해를 줌 (최대 30)
   źródło: Skills_personality-11.json :: dataList[id=1110803].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EchoOfMansion], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target has [EchoOfMansion], inflict Gloom Affinity damage equal to [Sinking] Potency on target (max 30)
   PL:
563. [Obrona (ulepszenia 1,4) — nazwa] 무례한 것...!
   źródło: Skills_personality-11.json :: dataList[id=1110804].levelList[level=1].name ; dataList[id=1110804].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Insolent Fool...!
   PL:
564. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] [Sinking] 1 부여 (턴 당 최대 3회)
   źródło: Skills_personality-11.json :: dataList[id=1110804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Sinking]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedEvade] Inflict 1 [Sinking] (3 times per turn)
   PL:
565. [Obrona (ulepszenie 4) — opis] [OnSucceedEvade] [Sinking] 1 부여 (턴 당 최대 6회)
   źródło: Skills_personality-11.json :: dataList[id=1110804].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Sinking]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedEvade] Inflict 1 [Sinking] (6 times per turn)
   PL:
566. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — nazwa] 마님의 소리가...!
   źródło: Passives.json :: dataList[id=1110801].name
   limit: do 40 znaków
   EN: The Mistress's Voice...!
   PL:
567. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — opis] - 정신력이 -25 미만인 대상과 합 진행 시 합 위력 +1, 피해량 +10%\n- [EchoOfMansion]가 있는 대상에게 가하는 피해량 +15%\n- 모든 코인이 남은 상태로 합 승리 시 정신력 10 회복. 정신력이 이미 최대라면, 다음 턴에 [AttackUp] 2 얻음 (턴 당 2회)
   źródło: Passives.json :: dataList[id=1110801].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [EchoOfMansion], [AttackUp]
   znaczenie tagów: [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: - When clashing against targets that have less than -25 SP, Clash Power +1 and deal +10% damage\n- Deal +15% damage against targets that have [EchoOfMansion]\n- When winning a Clash without losing a single Coin, heal 10 SP. If this unit is already at max SP, gain 2 [AttackUp] next turn (2 times per turn)
   PL:
568. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — podsumowanie] 정신력이 낮은 대상과 합 진행 시 합 위력 +1, 피해량 +10%\n대상에게 [EchoOfMansion]가 있으면 피해량 +15%\n합 승리 시 정신력 회복
   źródło: Passives.json :: dataList[id=1110801].summary
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [EchoOfMansion]
   znaczenie tagów: [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor
   EN: Against targets that have low SP, Clash Power +1 and deal +10% damage\nDeal +15% damage if the target has [EchoOfMansion]\nHeal SP on Clash Win
   PL:
569. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — nazwa] 마님의 소리가...!
   źródło: Passives.json :: dataList[id=1110811].name
   (powtórzenie elementu 566 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — opis] - 정신력이 0 미만인 대상과 합 진행 시 합 위력 +1, 피해량 +20%\n- [EchoOfMansion]가 있는 대상에게 가하는 피해량 +30%\n- 모든 코인이 남은 상태로 합 승리 시 정신력 10 회복. 정신력이 이미 최대라면, 다음 턴에 [AttackUp] 3 얻음 (턴 당 2회)
   źródło: Passives.json :: dataList[id=1110811].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [EchoOfMansion], [AttackUp]
   znaczenie tagów: [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: - When clashing against targets that have less than 0 SP, Clash Power +1 and deal +20% damage\n- Deal +30% damage against targets that have [EchoOfMansion]\n- When winning a Clash without losing a single Coin, heal 10 SP. If this unit is already at max SP, gain 3 [AttackUp] next turn (2 times per turn)
   PL:
571. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — podsumowanie] 정신력이 낮은 대상과 합 진행 시 합 위력 +1, 피해량 +20%\n대상에게 [EchoOfMansion]가 있으면 피해량 +30%\n합 승리 시 정신력 회복
   źródło: Passives.json :: dataList[id=1110811].summary
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [EchoOfMansion]
   znaczenie tagów: [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor
   EN: Against targets that have low SP, Clash Power +1 and deal +20% damage\nDeal +30% damage if the target has [EchoOfMansion]\nHeal SP on Clash Win
   PL:
572. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — nazwa] 버틀러 교육
   źródło: Passives.json :: dataList[id=1110821].name
   limit: do 40 znaków
   EN: Butler Training
   PL:
573. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — opis] 정신력이 가장 높은 아군 1명이 정신력이 -25 미만인 대상과 합 진행 시 합 위력 +1
   źródło: Passives.json :: dataList[id=1110821].desc
   limit: do 140 znaków
   EN: Clash Power +1 to 1 ally that has the most SP when Clashing against targets that have less than -25 SP
   PL:
574. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — podsumowanie] 정신력이 -25 미만인 대상과 합 진행 시 합 위력 +1
   źródło: Passives.json :: dataList[id=1110821].summary
   limit: do 120 znaków
   EN: Clash Power +1 when Clashing against targets that have less than -25 SP
   PL:
575. [Kwestia głosowa [get_11108_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=get_11108_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Kwestia głosowa [get_11108_1] (Identity Acquisition)] 신발의 흙은 제대로 터셨습니까? 부디 당부드리건대, 이 저택에서 제 허락 없이 가구 하나 함부로 건드시지 않는 편이 좋을 겁니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=get_11108_1].dlg
   limit: do 210 znaków
   EN: Did you make sure to clean the dirt from your boots? I implore you to not touch a single thing, even furniture, in this manor without my explicit permission.
   PL:
577. [Kwestia głosowa [lobby_morning_11108_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=lobby_morning_11108_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Kwestia głosowa [lobby_morning_11108_1] (Morning Greeting)] 이 저택의 숨통을 터주어야 할 시간이군. 자, 다들 커튼을 열어라. 몰아치는 바람과 한 줌의 햇빛이 이곳 허파까지 들어올 수 있도록 활짝.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=lobby_morning_11108_1].dlg
   limit: do 180 znaków
   EN: It's time to let the manor breathe. Open the curtains. Let the rushing gale and the pale ray of sunlight breathe through the manor's lungs!
   PL:
579. [Kwestia głosowa [lobby_noon_11108_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=lobby_noon_11108_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Kwestia głosowa [lobby_noon_11108_1] (Afternoon Greeting)] 추위를 느끼신다면 이 난롯가에 몸을 녹이십시오. 아마 당신이 이 저택에서 따뜻함을 느낄 수 있는 유일한 장소일테니까요.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=lobby_noon_11108_1].dlg
   limit: do 190 znaków
   EN: Warm yourself by this hearth should you feel the chill in your bones. It is the only place in this manor where you may feel any degree of warmth.
   PL:
581. [Kwestia głosowa [lobby_night_11108_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=lobby_night_11108_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Kwestia głosowa [lobby_night_11108_1] (Evening Greeting)] 폭풍이 몰아치고 있군요. 그러니 창문을 열어놓겠습니다. 그래야 마님이… 마님의 말씀이 더 선명하게 들릴 테니까.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=lobby_night_11108_1].dlg
   limit: do 150 znaków
   EN: The tempest howls... I shall open the windows. So that... so that the voice of my Mistress grow clearer to my ears.
   PL:
583. [Kwestia głosowa [smalltalk_11108_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=smalltalk_11108_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Kwestia głosowa [smalltalk_11108_1] (Chatter #1)] 혹시 찾을 것이 있다면 제게 말씀하십시오. 이 곳의 모든 식기와 가구의 배치는 제 손아귀 안에 있으니까요.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=smalltalk_11108_1].dlg
   limit: do 250 znaków
   EN: Do not hesitate to ask me if you are looking for something. I know this manor like the back of my hand; I know every location of every item in this house, from furniture to the smallest utensil.
   PL:
585. [Kwestia głosowa [smalltalk_11108_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=smalltalk_11108_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Kwestia głosowa [smalltalk_11108_2] (Chatter #2)] 시럽은 두 스푼 반, 온도는 적당히 미지근하게, 오늘 보실 서류는 올려두었습니다. 미친 늑대의 사냥은 얼마 남지 않았으며, 저희는 모두 빠짐없이 준비되었습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=smalltalk_11108_2].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Two and a half spoons of syrup, temperature moderately yet pleasantly warm. Documents waiting for your review have been placed on the desk.\n... The hunt for the frenzied wolf is nigh, and our preparation cannot be more complete.
   PL:
587. [Kwestia głosowa [smalltalk_11108_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=smalltalk_11108_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Kwestia głosowa [smalltalk_11108_3] (Chatter #3)] 제 선대들은 모두 이 저택 아래에 묻혀있습니다. 이 기약 없는 계약은 까마득하겠지만, 반드시 이행될 날이 올 것입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=smalltalk_11108_3].dlg
   limit: do 220 znaków
   EN: My ancestors are all laid to rest beneath this manor. Though the end of this contract lies in an ineffably far future... I know that its terms shall one day come to be.
   PL:
589. [Kwestia głosowa [smalltalk_11108_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=smalltalk_11108_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Kwestia głosowa [smalltalk_11108_4] (Post-Uptie Chat 1)] 이따금 이 땅 깊은 곳에서부터 참을 수 없는 갈증을 느낄 때가 있지만… 언젠간 보답받을 그날을 위해 견디고 있습니다. 마침내 모든 고행이 끝나고 한 모금을 목울대에 넣을 때, 얼마나 황홀할지…
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=smalltalk_11108_4].dlg
   limit: do 310 znaków
   EN: There are times when I would feel this insatiable, hypogean thirst... But I endure, for I await the day when this suffering would be rewarded. When that single swill of the waters graces my parched throat... oh, it shall be so ecstatic...
   PL:
591. [Kwestia głosowa [smalltalk_11108_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=smalltalk_11108_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Kwestia głosowa [smalltalk_11108_5] (Post-Uptie Chat 2)] 우리는 이 저택이 딛은 땅과 계약을 맺은 존재들입니다. 그 계약이 완수되기 전까지 어떤 것도 저희를 감히 막을 수 없죠. 몰아치는 폭풍도, 벼락도, 그 망할 늑대 놈도.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=smalltalk_11108_5].dlg
   limit: do 220 znaków
   EN: We are contracted with the earth that this manor is built upon. No wuthering tempest, no lightning, no accursed wolf shall stand in our way until the contract is fulfilled.
   PL:
593. [Kwestia głosowa [neglect_11108_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=neglect_11108_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Kwestia głosowa [neglect_11108_1] (Idle)] 당신이 이 저택에 발을 들인 순간부터, 어디에 숨어있든 마님은 느낄 수 있습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=neglect_11108_1].dlg
   limit: do 170 znaków
   EN: She's noticed your presence the moment you stepped foot in this manor. You cannot hide from the Mistress, no matter where you are.
   PL:
595. [Kwestia głosowa [gacksung_11108_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=gacksung_11108_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Kwestia głosowa [gacksung_11108_1] (Uptying)] 아, 마님이 내리신 선물이군요. 감사히 받아들이겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=gacksung_11108_1].dlg
   limit: do 120 znaków
   EN: Ah, a gift from the Mistress of the manor. I most graciously accept her offering.
   PL:
597. [Kwestia głosowa [formation_11108_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=formation_11108_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Kwestia głosowa [formation_11108_1] (Deployment)] 불청객을 맞이할 시간인가 보군요.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=formation_11108_1].dlg
   limit: do 120 znaków
   EN: Time to receive the uninvited guests.
   PL:
599. [Kwestia głosowa [battleentry_11108_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battleentry_11108_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Kwestia głosowa [battleentry_11108_1] (Stage Entry)] 다음 오찬까지는 돌아오겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battleentry_11108_1].dlg
   limit: do 120 znaków
   EN: I shall return before the next luncheon.
   PL:
601. [Kwestia głosowa [battle_select_11108_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_select_11108_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Kwestia głosowa [battle_select_11108_1] (Viewed in Battle)] 불편한 점이라도 있으십니까.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_select_11108_1].dlg
   limit: do 120 znaków
   EN: Is something not to your liking?
   PL:
603. [Kwestia głosowa [battle_endcommand_11108_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_endcommand_11108_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Kwestia głosowa [battle_endcommand_11108_1] (Commencing Attack)] 이 땅과 마님에게 손끝이라도 대려는 자가 있다면…
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_endcommand_11108_1].dlg
   limit: do 120 znaków
   EN: If anyone even dares to lay their hands on this land, on the Mistress...
   PL:
605. [Kwestia głosowa [battle_enemy_break_11108_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_enemy_break_11108_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Kwestia głosowa [battle_enemy_break_11108_1] (Enemy Stagger)] 불청객은 찌그러져 있도록.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_enemy_break_11108_1].dlg
   limit: do 120 znaków
   EN: Leave now or suffer, uninvited guest.
   PL:
607. [Kwestia głosowa [battle_break_11108_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_break_11108_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Kwestia głosowa [battle_break_11108_1] (Staggered)] 들린다… 저 밑에서 나를 부르는 물소리가…
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_break_11108_1].dlg
   limit: do 120 znaków
   EN: Oh, I hear it. The rush of the hypogean waters... it beckons me...
   PL:
609. [Kwestia głosowa [battle_kill_11108_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_kill_11108_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Kwestia głosowa [battle_kill_11108_1] (Enemy Killed)] 초대받지 않은 것들은 모조리 치워버린다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_kill_11108_1].dlg
   limit: do 120 znaków
   EN: Every uninvited thing must be removed from the premises.
   PL:
611. [Kwestia głosowa [battle_dead_11108_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_dead_11108_1].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Kwestia głosowa [battle_dead_11108_1] (Death)] 안돼, 아직… 그 물을 한 모금 마시기 전엔…
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_dead_11108_1].dlg
   limit: do 120 znaków
   EN: No, I can't... not before I drink from the waters...
   PL:
613. [Kwestia głosowa [choice_success_p_11108_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=choice_success_p_11108_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Kwestia głosowa [choice_success_p_11108_2] (Check Passed)] 분부대로 완료했습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=choice_success_p_11108_2].dlg
   limit: do 120 znaków
   EN: I have done as you commanded.
   PL:
615. [Kwestia głosowa [choice_fail_n_11108_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=choice_fail_n_11108_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Kwestia głosowa [choice_fail_n_11108_1] (Check Failed)] 저의 실책입니다, 죄송합니다. …마님.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=choice_fail_n_11108_1].dlg
   limit: do 120 znaków
   EN: This was my fault. My deepest apologies... Mistress.
   PL:
617. [Kwestia głosowa [battle_clear_11108_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_clear_11108_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Kwestia głosowa [battle_clear_11108_1] (Victory Cry)] 자, 이제 워더링하이츠로 복귀한다. 밀려있는 저택 일이 한가득이니.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_clear_11108_1].dlg
   limit: do 120 znaków
   EN: Now, let us return to Wuthering Heights. There are many tasks at hand.
   PL:
619. [Kwestia głosowa [battle_clear_ex_11108_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_clear_ex_11108_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Kwestia głosowa [battle_clear_ex_11108_1] (Extra Conditions Fulfilled)] 보고 계시는군요, 마님. 칭찬 감사합니다. 불청객들을 남김없이 모조리 처리했습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_clear_ex_11108_1].dlg
   limit: do 160 znaków
   EN: Ah, you have witnessed me, my Mistress. I thank for your commendations; every single uninvited guest has been dealt with.
   PL:
621. [Kwestia głosowa [battle_defeat_11108_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_defeat_11108_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Kwestia głosowa [battle_defeat_11108_1] (Defeat Wail)] 교육과 준비가… 부족했습니다. 죄송합니다, 마님.
   źródło: PersonalityVoiceDlg/Voice_Outis_Butler_11108.json :: dataList[id=battle_defeat_11108_1].dlg
   limit: do 120 znaków
   EN: My deepest apologies, Mistress. We were... underprepared.
   PL:

## [00] The Ring Pointillist Student — Outis — 약지 점묘파 스튜던트
- ID Tożsamości: `11109` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 69 · szybkość: 2–5 / 2–5 / 3–6 / 3–6
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed

623. [Karta Tożsamości — tytuł] 약지 점묘파\n스튜던트
   źródło: Personalities.json :: dataList[id=11109].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Ring Pointillist\nStudent
   PL:
624. [Karta Tożsamości — nazwa] 오티스
   źródło: Personalities.json :: dataList[id=11109].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Karta Tożsamości — nazwa z tytułem] 오티스
   źródło: Personalities.json :: dataList[id=11109].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Karta Tożsamości — opis] 오티스의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=11109].desc
   limit: do 120 znaków
   EN: Outis's 9th Identity
   PL:
627. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 점찍기
   źródło: Skills_personality-11.json :: dataList[id=1110901].levelList[level=1].name ; dataList[id=1110901].levelList[level=2].name ; dataList[id=1110901].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Dotting
   PL:
628. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 1 [Laceration]
   PL:
629. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Laceration]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1110901].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration], Clash Power +1
   PL:
631. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110901].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1110901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
632. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1110901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Laceration]이 6 이상이면, 합 위력 +1\n<style="highlight">대상의 [Laceration]이 10 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-11.json :: dataList[id=1110901].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration], Clash Power +1\n<style="highlight">If target has 10+ [Laceration], Coin Power +1 </style>
   PL:
634. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 혈묘화
   źródło: Skills_personality-11.json :: dataList[id=1110902].levelList[level=1].name ; dataList[id=1110902].levelList[level=2].name ; dataList[id=1110902].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Sanguine Painting
   PL:
635. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 20% 확률로 코인 1회 재사용. 대상이 보유한 부정적인 효과 1개당 재사용 확률 +20%
   źródło: Skills_personality-11.json :: dataList[id=1110902].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1110902].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] 20% chance to Reuse Coin once. +20% more chance to Reuse Coin for every type of negative effect on target
   PL:
636. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1110902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
637. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Laceration]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1110902].levelList[level=2].desc
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가\n자신의 코인 효과로 코인 재사용 시 증가시키는 [Laceration] 횟수 +1
   źródło: Skills_personality-11.json :: dataList[id=1110902].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1110902].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count\nWhen Reusing Coin with this unit's Coin effects, inflict +1 more [Laceration] Count
   PL:
639. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Laceration]이 6 이상이면, 합 위력 +2
   źródło: Skills_personality-11.json :: dataList[id=1110902].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration], Clash Power +2
   PL:
640. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 40% 확률로 코인 재사용. 대상이 보유한 부정적인 효과 1개당 재사용 확률 +20% (스킬당 최대 2회 재사용 가능)
   źródło: Skills_personality-11.json :: dataList[id=1110902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] 40% chance to Reuse Coin. +20% more chance to Reuse Coin for every type of negative effect on target (2 times max per Skill)
   PL:
641. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 작품 점검
   źródło: Skills_personality-11.json :: dataList[id=1110903].levelList[level=3].name ; dataList[id=1110903].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Artwork Inspection
   PL:
642. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상이 보유한 부정적인 효과 1개당 피해량 +10% (최대 30%)\n[WhenUse] 조작 패널에서 자신의 양 옆에 있는 아군에게 다음 턴에 [Agility] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110903].levelList[level=3].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste
   EN: Deal +10% damage for every type of negative effect on target (max 30%)\n[WhenUse] Apply 1 [Agility] next turn to 2 allies adjacent to this unit on the Dashboard
   PL:
643. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-11.json :: dataList[id=1110903].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1110903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
644. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 3 부여
   źródło: Skills_personality-11.json :: dataList[id=1110903].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1110903].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 Potency for 1 of the following effects: [Combustion], [Laceration], [Vibration], [Burst], or [Sinking]. Effect selected at random.
   PL:
645. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 3 — opis] [EndSkill] 대상이 흐트러짐 상태가 되거나 사망했으면, 자신을 제외하고 정신력이 가장 높은 아군 1명에게 다음 턴에 [PenetrateDamageUp] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110903].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [PenetrateDamageUp]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: [EndSkill] If target is Staggered or defeated, apply 1 [PenetrateDamageUp] next turn to 1 other ally with the highest SP
   PL:
646. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n대상이 보유한 부정적인 효과 1개당 피해량 +12.5% (최대 50%)\n[WhenUse] 조작 패널에서 자신의 양 옆에 있는 아군에게 다음 턴에 [Agility] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1110903].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [Agility]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste
   EN: If target has 6+ [Laceration], Coin Power +1\nDeal +12.5% damage for every type of negative effect on target (max 50%)\n[WhenUse] Apply 1 [Agility] next turn to 2 allies adjacent to this unit on the Dashboard
   PL:
647. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [EndSkill] 대상이 흐트러짐 상태가 되거나 사망했으면, 자신을 제외하고 정신력이 가장 높은 아군 1명에게 다음 턴에 [PenetrateDamageUp] 1 부여. <style="highlight">대상이 약지 소속 조직원이면 [PenetrateResultUp] 1 추가 부여</style>
   źródło: Skills_personality-11.json :: dataList[id=1110903].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkill], [PenetrateDamageUp], [PenetrateResultUp]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up
   EN: [EndSkill] If target is Staggered or defeated, apply 1 [PenetrateDamageUp] next turn to 1 other ally with the highest SP. <style="highlight">If the affected ally is a member of the Ring, apply 1 [PenetrateResultUp] as well</style>
   PL:
648. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-11.json :: dataList[id=1110904].levelList[level=1].name ; dataList[id=1110904].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 7 · monety: 1 (+6)
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Obrona (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 10 이상이면, 코인 위력 +3
   źródło: Skills_personality-11.json :: dataList[id=1110904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 10+ [Laceration], Coin Power +3
   PL:
650. [Obrona (ulepszenie 4) — opis] [WhenUse] 대상의 [Laceration]이 10 이상이면, 코인 위력 +7
   źródło: Skills_personality-11.json :: dataList[id=1110904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 10+ [Laceration], Coin Power +7
   PL:
651. [Pasywka bojowa (od ulepszenia 1) — nazwa] 혈점묘파
   źródło: Passives.json :: dataList[id=1110902].name
   limit: do 40 znaków
   EN: Sanguine Pointillist
   PL:
652. [Pasywka bojowa (od ulepszenia 1) — opis] 이 인격은 [Laceration]을 부여하는 인격으로만 취급됨. 랜덤으로 [Combustion], [Laceration], [Vibration], [Burst], [Sinking]을 부여하는 스킬이 이 효과로 인해서 해당 키워드를 부여하는 스킬로 취급되지 않음.
   źródło: Passives.json :: dataList[id=1110902].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: [Laceration], [Combustion], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: This Identity only counts as an "Identity that inflicts [Laceration]". This Identity's Skills that randomly inflict [Combustion], [Laceration], [Vibration], [Burst], and [Sinking] do not count as Skills that inflict each respective Keyword
   PL:
653. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — nazwa] 여러 점
   źródło: Passives.json :: dataList[id=1110901].name
   limit: do 40 znaków
   EN: Multitude of Dots
   PL:
654. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — opis] 전투 시작 시 부정적인 효과를 가장 적게 보유한 적 1명에게 [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 2 부여\n(집중 전투인 경우, 부위로 판정)
   źródło: Passives.json :: dataList[id=1110901].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: Combat Start: Inflict 2 Potency for 1 of the following effects on 1 enemy that has the least types of negative effects: [Combustion], [Laceration], [Vibration], [Burst], or [Sinking]. Effect selected at random.\n(In Focused Encounters, a Part)
   PL:
655. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — podsumowanie] 전투 시작 시 적 1명에게 무작위 상태이상 2 부여
   źródło: Passives.json :: dataList[id=1110901].summary
   limit: do 120 znaków
   EN: Combat Start: Inflict 2 Potency for a random status effect to an enemy
   PL:
656. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — nazwa] 여러 점
   źródło: Passives.json :: dataList[id=1110911].name
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — opis] 전투 시작 시 부정적인 효과를 가장 적게 보유한 적 <style="highlight">2</style>명에게 [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 2 부여\n(집중 전투인 경우, 부위로 판정)
   źródło: Passives.json :: dataList[id=1110911].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: Combat Start: Inflict 2 Potency for 1 of the following effects on <style="highlight">2</style> enemies that have the least types of negative effects: [Combustion], [Laceration], [Vibration], [Burst], or [Sinking]. Effect selected at random.\n(In Focused Encounters, Parts)
   PL:
658. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — podsumowanie] 전투 시작 시 적 2명에게 무작위 상태이상 2 부여
   źródło: Passives.json :: dataList[id=1110911].summary
   limit: do 120 znaków
   EN: Combat Start: Inflict 2 Potency for a random status effect to 2 enemies
   PL:
659. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 밑그림
   źródło: Passives.json :: dataList[id=1110921].name
   limit: do 40 znaków
   EN: Rough Sketch
   PL:
660. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 정신력이 가장 낮은 아군 1명이 [Laceration]이 부여된 적 처치 시 정신력 4 회복.\n대상이 보유한 부정적인 효과 1개당 추가 1 회복.(최대 4. 턴 당 최대 1회 발동)
   źródło: Passives.json :: dataList[id=1110921].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: 1 ally that has the least SP heals 4 SP when defeating an enemy that has [Laceration].\nHeal 1 additional SP for every type of negative effect on the target. (max 4. Once per turn)
   PL:
661. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — podsumowanie] [Laceration]이 있는 적 처치 시 정신력 회복
   źródło: Passives.json :: dataList[id=1110921].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Heal SP on self On Kill against targets that have [Laceration]
   PL:
662. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Lust) — nazwa] 밑그림
   źródło: Passives.json :: dataList[id=1110931].name
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Lust) — opis] 정신력이 가장 낮은 아군 1명이 [Laceration]이 부여된 적 처치 시 정신력 4 회복.\n대상이 보유한 부정적인 효과 1개당 추가 1 회복.(최대 4. 턴 당 최대 3회 발동)
   źródło: Passives.json :: dataList[id=1110931].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: 1 ally that has the least SP heals 4 SP when defeating an enemy that has [Laceration].\nHeal 1 additional SP for every type of negative effect on the target. (max 4. 3 times per turn)
   PL:
664. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Lust) — podsumowanie] [Laceration]이 있는 적 처치 시 정신력 회복
   źródło: Passives.json :: dataList[id=1110931].summary
   (powtórzenie elementu 661 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Kwestia głosowa [get_11109_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=get_11109_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Kwestia głosowa [get_11109_1] (Identity Acquisition)] 점수는 F. 반론은 듣지 않겠다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=get_11109_1].dlg
   limit: do 120 znaków
   EN: You're getting an 'F', end of story. No, I don't accept appeals.
   PL:
667. [Kwestia głosowa [lobby_morning_11109_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=lobby_morning_11109_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Kwestia głosowa [lobby_morning_11109_1] (Morning Greeting)] 이른 시간부터 소란스럽게 굴지 마라.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=lobby_morning_11109_1].dlg
   limit: do 120 znaków
   EN: It's only morning. Keep it down.
   PL:
669. [Kwestia głosowa [lobby_noon_11109_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=lobby_noon_11109_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Kwestia głosowa [lobby_noon_11109_1] (Afternoon Greeting)] 이 그림은 못 쓰겠군. 후… 잠시 바람이라도 쐬러 가지. 이 시간만 되면 머리가 굳어서.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=lobby_noon_11109_1].dlg
   limit: do 170 znaków
   EN: This won't do. This won't do at all. Haah... Why don't we go out for some air? I just seem to lose all momentum at this time of day.
   PL:
671. [Kwestia głosowa [lobby_night_11109_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=lobby_night_11109_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Kwestia głosowa [lobby_night_11109_1] (Evening Greeting)] 주어진 작업을 끝내기 전까지, 누구도 잠들 수 없다. 밤을 새서라도 완성하도록.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=lobby_night_11109_1].dlg
   limit: do 180 znaków
   EN: None of us are going to sleep until we deal with this task, understood? I don't care if we have to work through the night—just get it done.
   PL:
673. [Kwestia głosowa [smalltalk_11109_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=smalltalk_11109_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Kwestia głosowa [smalltalk_11109_1] (Chatter #1)] 할 수 있는 걸 브리핑해라.\n지휘와 상담… 이라고… 쉽지 않군. 어쨌든 얹혀가는 건 용납할 수 없다. 최선을 다해 작품에 일조하도록.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=smalltalk_11109_1].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Now, brief me on your capabilities.\n'Command' and 'consultations'...? I... okay. I see. Still, contribute as much as you are able to the production of this work. We're doing a group project—I won't accept any freeloaders.
   PL:
675. [Kwestia głosowa [smalltalk_11109_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=smalltalk_11109_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Kwestia głosowa [smalltalk_11109_2] (Chatter #2)] 쉽게 더러워지는 걸 몰라서 우리가 하얀 옷을 입는 것이 아니다.\n작품이 끝났을 때 온갖 색으로 칠해진 옷은 그것대로 감상할 가치가 있는 예술이기 때문이지.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=smalltalk_11109_2].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We wear white not because we're stupid and don't know that it stains easily.\nWe wear white because clothes stained with all kinds of color at the end of the grueling artistic process is, in of itself, a piece of art that deserves appreciation.
   PL:
677. [Kwestia głosowa [smalltalk_11109_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=smalltalk_11109_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Kwestia głosowa [smalltalk_11109_3] (Chatter #3)] 단체 과제를 하다가 만나는 조원 다섯 중 한 명은 구제불능의 쓰레기다.\n여기는 비율 상 두세 명이 그렇겠군.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=smalltalk_11109_3].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: As a rule, one out of five participants in most group projects are unsalvageable scum who have nothing to contribute to the team effort.\nGoing by that rule, I bet this group has at least two or three such members.
   PL:
679. [Kwestia głosowa [smalltalk_11109_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=smalltalk_11109_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Kwestia głosowa [smalltalk_11109_4] (Post-Uptie Chat 1)] 물감으로 찍는 점이 다가 아니다. 구멍, 상처, 시선, 철조망. 세상에는 수많은 점이 있지.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=smalltalk_11109_4].dlg
   limit: do 180 znaków
   EN: There are more 'dots' to this world than the ones drawn with a brush. A hole. A wound. A gaze. Barbed wires. The possibilities are endless.
   PL:
681. [Kwestia głosowa [smalltalk_11109_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=smalltalk_11109_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Kwestia głosowa [smalltalk_11109_5] (Post-Uptie Chat 2)] 잠깐. 거기 가만히 서 있도록. 흠… 심장 쪽에 구멍 세개만 뚫어도 되나? 제법 괜찮은 작품이…\n왜 도망가는 거지? 모두 이쪽으로 와서 저자를 잡는다, 실시!
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=smalltalk_11109_5].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You there, wait. Stand still. Hm... would you allow me to puncture three little holes in your heart? I must say, it should make for a rather fascinating—\n... Why are they running? Team! Get over here and seize them, stat!
   PL:
683. [Kwestia głosowa [neglect_11109_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=neglect_11109_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Kwestia głosowa [neglect_11109_1] (Idle)] 초점이 어긋났나? 여기를 봐라.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=neglect_11109_1].dlg
   limit: do 120 znaków
   EN: Are your eyes glazing over? Focus.
   PL:
685. [Kwestia głosowa [gacksung_11109_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=gacksung_11109_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Kwestia głosowa [gacksung_11109_1] (Uptying)] 점이 모여 만드는 빛과 그림자의 미학을 이해하고 있나? 모른다면 지금부터라도 숙지해라.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=gacksung_11109_1].dlg
   limit: do 200 znaków
   EN: Do you understand the allure of contours of light and shadow? The beauty born from countless collections of dots? No? Then allow me to enlighten you.
   PL:
687. [Kwestia głosowa [formation_11109_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=formation_11109_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Kwestia głosowa [formation_11109_1] (Deployment)] 나를 점찍었다면, 격에 맞는 조원도 함께 준비하도록.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=formation_11109_1].dlg
   limit: do 130 znaków
   EN: If you wish to have me on your team, then the rest of the group better be up to my standards.
   PL:
689. [Kwestia głosowa [battleentry_11109_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battleentry_11109_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Kwestia głosowa [battleentry_11109_1] (Stage Entry)] 전원 집합. 이번 작품에 대해 논의할 시간이다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battleentry_11109_1].dlg
   limit: do 120 znaków
   EN: Gather around, everyone. It's time to discuss our project.
   PL:
691. [Kwestia głosowa [battle_select_11109_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_select_11109_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Kwestia głosowa [battle_select_11109_1] (Viewed in Battle)] 작품을 고안하는 중이니 용건만 간단히.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_select_11109_1].dlg
   limit: do 120 znaków
   EN: I'm still in the conceptualization phase. Be quick about it.
   PL:
693. [Kwestia głosowa [battle_endcommand_11109_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_endcommand_11109_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Kwestia głosowa [battle_endcommand_11109_1] (Commencing Attack)] 일리있는 의견이다. 그걸로 하지.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_endcommand_11109_1].dlg
   limit: do 120 znaków
   EN: A sound opinion. Let's go with that.
   PL:
695. [Kwestia głosowa [battle_enemy_break_11109_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_enemy_break_11109_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Kwestia głosowa [battle_enemy_break_11109_1] (Enemy Stagger)] 밑그림은 완성했다. 빠르게 칠하도록.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_enemy_break_11109_1].dlg
   limit: do 120 znaków
   EN: The rough sketch is complete. Now be quick and paint over it.
   PL:
697. [Kwestia głosowa [battle_break_11109_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_break_11109_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Kwestia głosowa [battle_break_11109_1] (Staggered)] 큭…
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_break_11109_1].dlg
   limit: do 120 znaków
   EN: Agh...
   PL:
699. [Kwestia głosowa [battle_kill_11109_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_kill_11109_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Kwestia głosowa [battle_kill_11109_1] (Enemy Killed)] 작품 완성. 돌아가면 의견을 나누지.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_kill_11109_1].dlg
   limit: do 120 znaków
   EN: This artwork is complete. Let us critique it once we return.
   PL:
701. [Kwestia głosowa [battle_dead_11109_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_dead_11109_1].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Kwestia głosowa [battle_dead_11109_1] (Death)] 조원을… 잘못 구했군…
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_dead_11109_1].dlg
   limit: do 120 znaków
   EN: I should've gotten... better teammates...
   PL:
703. [Kwestia głosowa [choice_success_p_11109_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=choice_success_p_11109_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Kwestia głosowa [choice_success_p_11109_2] (Check Passed)] 내 덕에 모두 좋은 평가를 받겠군.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=choice_success_p_11109_2].dlg
   limit: do 130 znaków
   EN: I expect that our group project will receive a commendable review. And it's all thanks to me.
   PL:
705. [Kwestia głosowa [choice_fail_n_11109_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=choice_fail_n_11109_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Kwestia głosowa [choice_fail_n_11109_1] (Check Failed)] …예술을 하면서 이 정도 고난은 있어야 하는 법이지.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=choice_fail_n_11109_1].dlg
   limit: do 120 znaków
   EN: ... Such tribulations are but an expected part of pursuing the path of art.
   PL:
707. [Kwestia głosowa [battle_clear_11109_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_clear_11109_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [Kwestia głosowa [battle_clear_11109_1] (Victory Cry)] 학점으로 치자면 B. 그럭저럭 나쁘지 않은 전투였다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_clear_11109_1].dlg
   limit: do 120 znaków
   EN: I'll give this performance a 'B'. Not bad, not great.
   PL:
709. [Kwestia głosowa [battle_clear_ex_11109_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_clear_ex_11109_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Kwestia głosowa [battle_clear_ex_11109_1] (Extra Conditions Fulfilled)] A+. 예술적인 전투였다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_clear_ex_11109_1].dlg
   limit: do 120 znaków
   EN: A+. What an artful battle that was.
   PL:
711. [Kwestia głosowa [battle_defeat_11109_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_defeat_11109_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Kwestia głosowa [battle_defeat_11109_1] (Defeat Wail)] …이번 지휘를 작품이라 생각하면, 낙제점이다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Rings_11109.json :: dataList[id=battle_defeat_11109_1].dlg
   limit: do 120 znaków
   EN: If you consider this mess you call 'command' an art... then I have to flunk you.
   PL:

## [000] W Corp. L3 Cleanup Captain — Outis — W사 3등급 정리 요원 팀장
- ID Tożsamości: `11110` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 70 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Charge, Rupture

713. [Karta Tożsamości — tytuł] W사 3등급\n정리 요원 팀장
   źródło: Personalities.json :: dataList[id=11110].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L3\nCleanup Captain
   PL:
714. [Karta Tożsamości — nazwa] 오티스
   źródło: Personalities.json :: dataList[id=11110].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Karta Tożsamości — nazwa z tytułem] 오티스
   źródło: Personalities.json :: dataList[id=11110].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Karta Tożsamości — opis] 오티스의 열번째 인격
   źródło: Personalities.json :: dataList[id=11110].desc
   limit: do 120 znaków
   EN: Outis’s 10th Identity
   PL:
717. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 파동
   źródło: Skills_personality-11.json :: dataList[id=1111001].levelList[level=1].name ; dataList[id=1111001].levelList[level=2].name ; dataList[id=1111001].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Ripple
   PL:
718. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수가 4 이상이면, 합 위력 +1\n[WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 4+ [Charge] Count, Clash Power +1\n[WhenUse] Gain +2 [Charge] Count
   PL:
719. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1111001].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1111001].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +1 [Charge] Count
   PL:
720. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Charge] 횟수가 4 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [Charge] 횟수가 6 이상이면, 합 위력 +1\n[WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111001].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 4+ [Charge] Count, Base Power +1\n[WhenUse] At 6+ [Charge] Count, Clash Power +1\n[WhenUse] Gain +2 [Charge] Count
   PL:
721. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Charge] 횟수가 4 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [Charge] 횟수 5 당, 합 위력 +1 (최대 2)\n[WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111001].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 4+ [Charge] Count, Base Power +1\n[WhenUse] Clash Power +1 for every 5 [Charge] Count on self (max 2)\n[WhenUse] Gain +2 [Charge] Count
   PL:
722. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count
   PL:
723. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 충전 도약
   źródło: Skills_personality-11.json :: dataList[id=1111002].levelList[level=1].name ; dataList[id=1111002].levelList[level=2].name ; dataList[id=1111002].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 5 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Charged Leap
   PL:
724. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수를 6 소모하여, 기본 위력 +1\n[WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111002].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 6 [Charge] Count on self to gain Base Power +1\n[WhenUse] Gain +2 [Charge] Count
   PL:
725. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1111002].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1111002].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1111002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111002].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1111002].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1111002].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 [Charge] 횟수를 6 소모하여, 기본 위력 +1\n- [Charge] 횟수를 소모했다면, 자신과 [Charge] 횟수를 가장 적게 보유한 아군 2명에게 [ChargeForceField]을 ([Charge] + 1) 부여 (최대 7, 턴 당 최대 1회 발동)\n[WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111002].levelList[level=2].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [ChargeForceField]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: [WhenUse] Consume 6 [Charge] Count on self to gain Base Power +1\n- If this unit consumed [Charge] Count, apply ([Charge] + 1) [ChargeForceField] to self and 2 other allies that have the least [Charge] Count. (Max 7 [ChargeForceField] per ally. Activates once per turn max)\n[WhenUse] Gain +2 [Charge] Count
   PL:
729. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111002].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1111002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 3 — opis] [OnSucceedAttackHead] 이 스킬 사용 시 [Charge] 횟수를 소모하였다면, 다음 턴에 [Binding] 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1111002].levelList[level=2].coinlist[#1].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Charge], [Binding]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Charge] = 충전 / Charge; [Binding] = 속박 / Bind
   EN: [OnSucceedAttackHead] If this Skill consumed [Charge] Count on use, inflict 2 [Binding] next turn
   PL:
731. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 [Charge] 횟수를 6 소모하여, 코인 위력 +1\n- [Charge] 횟수를 소모했다면, 자신과 [Charge] 횟수를 가장 적게 보유한 아군 2명에게 [ChargeForceField]을 ([Charge] + <style="highlight">2</style>) 부여 (최대 <style="highlight">8</style>, 턴 당 최대 <style="highlight">2</style>회 발동)\n[WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111002].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge], [ChargeForceField]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: [WhenUse] Consume 6 [Charge] Count on self to gain Coin Power +1\n- If this unit consumed [Charge] Count, apply ([Charge] + <style="highlight">2</style>) [ChargeForceField] to self and 2 other allies that have the least [Charge] Count. (Max <style="highlight">8</style> [ChargeForceField] per ally. Activates <style="highlight">2 times</style> per turn max)\n[WhenUse] Gain +2 [Charge] Count
   PL:
732. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 이 스킬 사용 시 [Charge] 횟수를 소모하였다면, 다음 턴에 [Binding] 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1111002].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] If this Skill consumed [Charge] Count on use, inflict 2 [Binding] next turn
   PL:
734. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 차원 절단
   źródło: Skills_personality-11.json :: dataList[id=1111003].levelList[level=3].name ; dataList[id=1111003].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Rip Dimension
   PL:
735. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] 자신과 [Charge]을 보유한 아군 (최대 공명 수)명에게 [ChargeLoad]를 [Charge]만큼 부여\n(최대 부여 대상 수: 자신 제외 5명)\n[WhenUse] [Charge]이 2이상이고 [Charge] 횟수가 7 이상, 15 미만이면, 보유한 [Charge] 횟수를 전부 소모하여 코인 위력 + 1\n[WhenUse] [Charge] 횟수를 15 소모하여 코인 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1111003].levelList[level=3].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Charge], [ChargeLoad], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Charge] = 충전 / Charge; [ChargeLoad] = 부하 / Load; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] To self and (highest Reson.) allies that have [Charge]: apply [ChargeLoad] equal to [Charge] on self\n(Max 5 other allies)\n[WhenUse] At 2+ [Charge] and 7~14 [Charge] Count, consume all [Charge] Count on self to gain Coin Power +1\n[WhenUse] Consume 15 [Charge] Count to gain Coin Power +1
   PL:
736. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111003].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1111003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
737. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111003].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1111003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 이 스킬 사용 시 [Charge] 횟수를 15 소모하였으면, [Burst] 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1111003].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If this Skill consumed 15 [Charge] Count on use, inflict 2 [Burst]
   PL:
739. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] (5 - [Charge])만큼 자신의 [Charge] 횟수 증가 (최소 0)
   źródło: Skills_personality-11.json :: dataList[id=1111003].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1111003].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain (5 - [Charge]) [Charge] Count (Min 0)
   PL:
740. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [StartBattle] 자신과 [Charge]을 보유한 아군 (최대 공명 수)명에게 [ChargeLoad]를 [Charge]만큼 부여\n(최대 부여 대상 수: 자신 제외 5명)\n[WhenUse] [Charge]이 2이상이고 [Charge] 횟수가 7 이상, 15 미만이면, 보유한 [Charge] 횟수를 전부 소모하여 코인 위력 + 2\n[WhenUse] [Charge] 횟수를 15 소모하여 코인 위력 +2
   źródło: Skills_personality-11.json :: dataList[id=1111003].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Charge], [ChargeLoad], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Charge] = 충전 / Charge; [ChargeLoad] = 부하 / Load; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] To self and (highest Reson.) allies that have [Charge]: apply [ChargeLoad] equal to [Charge] on self\n(Max 5 other allies)\n[WhenUse] At 2+ [Charge] and 7~14 [Charge] Count, consume all [Charge] Count on self to gain Coin Power +2\n[WhenUse] Consume 15 [Charge] Count to gain Coin Power +2
   PL:
741. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 이 스킬 사용 시 [Charge] 횟수를 15 소모하였으면, [Burst] 3 부여
   źródło: Skills_personality-11.json :: dataList[id=1111003].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If this Skill consumed 15 [Charge] Count on use, inflict 3 [Burst]
   PL:
743. [Obrona (ulepszenia 1,4) — nazwa] 플라즈마 전개
   źródło: Skills_personality-11.json :: dataList[id=1111004].levelList[level=1].name ; dataList[id=1111004].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Deploy Plasma
   PL:
744. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 2당 기본 위력 +1 (최대 5)\n[WhenUse] 자신의 [Charge] 횟수 2 증가 (턴 당 최대 2회)
   źródło: Skills_personality-11.json :: dataList[id=1111004].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Base Power +1 for every 2 [Charge] Count on self (max 5)\n[WhenUse] Gain +2 [Charge] Count (2 times per turn)
   PL:
745. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 [Charge] <style="highlight">횟수당</style> 기본 위력 +1 (최대 <style="highlight">10</style>)\n[WhenUse] 자신의 [Charge] 횟수 2 증가 (턴 당 최대 <style="highlight">3</style>회)
   źródło: Skills_personality-11.json :: dataList[id=1111004].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Base Power +1 for <style="highlight">every</style> [Charge] Count on self (max <style="highlight">10</style>)\n[WhenUse] Gain +2 [Charge] Count (<style="highlight">3</style> times per turn)
   PL:
746. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 과충전 / 정리 지시
   źródło: Passives.json :: dataList[id=1111001].name
   limit: do 40 znaków
   EN: Overcharge / Cleanup Order
   PL:
747. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다 [Charge]을 1 얻음\n턴 종료 시, 자신을 포함한 W사 직원 ([Charge])명에게 편성 순서가 가장 뒤인 순으로 다음 턴에 [ParryingResultUp] 1 부여 (최대 부여 대상 수: 5명)
   źródło: Passives.json :: dataList[id=1111001].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [ParryingResultUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\nTurn End: Apply 1 [ParryingResultUp] next turn to ([Charge]) W Corp. employees, including this unit, in reverse Deployment order (max: 5 allies)
   PL:
748. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Envy) — nazwa] 굴절
   źródło: Passives.json :: dataList[id=1111021].name
   limit: do 40 znaków
   EN: Refraction
   PL:
749. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Envy) — opis] 턴 시작 시 [Charge] 횟수가 가장 많은 아군 1명의 [Charge] 횟수를 7 이상 소모한 스킬 피해량 +10% (턴 당 1회)
   źródło: Passives.json :: dataList[id=1111021].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: 1 ally who has the most [Charge] Count at Turn Start: deal +10% damage with Skills that consumed 7+ [Charge] Count (once per turn)
   PL:
750. [Kwestia głosowa [get_11110_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=get_11110_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Kwestia głosowa [get_11110_1] (Identity Acquisition)] 열차 정돈을 시작한다. 승객분들이 모두 제자리에 착석할 수 있도록.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=get_11110_1].dlg
   limit: do 120 znaków
   EN: Commencing train cleanup mission. Let's bring those passengers back to their seats.
   PL:
752. [Kwestia głosowa [lobby_morning_11110_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=lobby_morning_11110_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Kwestia głosowa [lobby_morning_11110_1] (Morning Greeting)] 아침은 빈속으로 출근하는 편입니다. 승객들을 보는 것은 익숙해져도, 열차 안의 냄새는 도통 익숙해지지 않는지라…
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=lobby_morning_11110_1].dlg
   limit: do 210 znaków
   EN: I prefer to keep an empty stomach in the morning. I can get used to the sight of our passengers, but the smell... The smell is quite difficult to acclimate to.
   PL:
754. [Kwestia głosowa [lobby_noon_11110_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=lobby_noon_11110_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Kwestia głosowa [lobby_noon_11110_1] (Afternoon Greeting)] 점심은 보통 워프 열차 정거장에서 판매하는 특선 도시락을 먹는 편입니다.\n듣기로는 본사 쪽 승강장의 도시락이 제일 맛있다더군요. 기회가 된다면 꼭 드셔보시길.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=lobby_noon_11110_1].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: For lunch, I usually eat the premium boxed lunch sold at each WARP train station platform.\nFrom what I hear, the boxed lunch sold at the station located in the headquarters is the best of them all. I suggest that you seek it out if you ever have the chance.
   PL:
756. [Kwestia głosowa [lobby_night_11110_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=lobby_night_11110_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Kwestia głosowa [lobby_night_11110_1] (Evening Greeting)] 먼저 들어가셔도 괜찮습니다, 관리자님…\n저는 오늘도 막차… 아니, 첫차 시간까지 근무가 예정되어 있기에…
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=lobby_night_11110_1].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Don't mind me, Executive Manager. You may return to your quarters.\nOnce again, my shift extends to the last train of the day... I mean, the first train of tomorrow. I'll be here for a while...
   PL:
758. [Kwestia głosowa [smalltalk_11110_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=smalltalk_11110_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Kwestia głosowa [smalltalk_11110_1] (Chatter #1)] 근래 불미스러운 사고들로 푯값을 인하하고, 일반 승객을 늘린다더니… 덩달아 정리해야 할 것도 몇 배나 늘어버렸군.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=smalltalk_11110_1].dlg
   limit: do 220 znaków
   EN: I suppose the ticket price cuts and economy car ticket expansion caused by certain... unfortunate events are to blame for multiplying our workload by several magnitudes.
   PL:
760. [Kwestia głosowa [smalltalk_11110_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=smalltalk_11110_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Kwestia głosowa [smalltalk_11110_2] (Chatter #2)] 잘 봐라, 도착한 열차 안에서 승객들이 문을 막고 농성할 때는 이렇게… 공간 절단으로 문을 뜯어 진입하는 게 유효하다. 단, 열차가 정지했을 때만 공간 절단을 사용하도록.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=smalltalk_11110_2].dlg
   limit: do 280 znaków
   EN: Now observe. If the passengers have barricaded themselves inside the car, then... rip the space to tear open the door before entering. A word of warning, however: do that only after the train has come to a complete stop.
   PL:
762. [Kwestia głosowa [smalltalk_11110_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=smalltalk_11110_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Kwestia głosowa [smalltalk_11110_3] (Chatter #3)] 우리의 업무는 유전인자를 정확히 식별하고, 파편을 모아 승객을 제자리에 돌려놓는 일이다.\n승객들의 제압은 업무를 위한 부가적인 행위에 불과하지.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=smalltalk_11110_3].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Our mission is to properly recognize and match the correct genomes, put the parts back together, and bring the passengers back to their seats.\nPassenger neutralization is not our primary objective; it's just a part of the process.
   PL:
764. [Kwestia głosowa [smalltalk_11110_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=smalltalk_11110_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Kwestia głosowa [smalltalk_11110_4] (Post-Uptie Chat 1)] 자신이 이 일에 맞지 않다고 생각하는 정리 요원도 간혹 있습니다만… 리더라면 그런 의욕 없는 자도 이끌어야 하는 법입니다.\n특히 그런 자들은 쓸데없는 생각을 하지 않아, 차후 도움이 될 여지가 많더군요.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=smalltalk_11110_4].dlg
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Some Cleanup Agents believe that they are unfit for this line of work, but... a leader should know how to make use of unmotivated subordinates as well.\nThere may come a moment in which they show their usefulness, as they usually don't hold certain unnecessary ideations.
   PL:
766. [Kwestia głosowa [smalltalk_11110_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=smalltalk_11110_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Kwestia głosowa [smalltalk_11110_5] (Post-Uptie Chat 2)] 열차 안의 광경에 그렇게 역겨워하실 필요는 없습니다. 날개의 일이란… 보통 이런 법일 테니.\n보기 힘드시다면, 다른 곳을 보다 오시는 게 좋을 겁니다. 정리 업무 중에는 고깃덩이밖에 보이지 않을 테니.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=smalltalk_11110_5].dlg
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Please, don't let the sights of the train disturb you. I am quite certain that this is business as usual for most Wings.\nIf you find it difficult to stomach the sight, then I suggest coming back later. Because you'll be seeing these chunks of meat throughout the entire cleanup process.
   PL:
768. [Kwestia głosowa [neglect_11110_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=neglect_11110_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Kwestia głosowa [neglect_11110_1] (Idle)] …매일 열차를 타고서도 돌아가지 못하는가.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=neglect_11110_1].dlg
   limit: do 120 znaków
   EN: ... I can't seem to return. No matter how many trains I board day after day.
   PL:
770. [Kwestia głosowa [gacksung_11110_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=gacksung_11110_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Kwestia głosowa [gacksung_11110_1] (Uptying)] 돌아가기 위한 과정은…! 큭… 아직까지도 험난하군.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=gacksung_11110_1].dlg
   limit: do 120 znaków
   EN: The homeward journey is...! Agh... it's still tumultuous.
   PL:
772. [Kwestia głosowa [formation_11110_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=formation_11110_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Kwestia głosowa [formation_11110_1] (Deployment)] 각 정리 요원은 위치로. 곧 열차 정리가 시작된다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=formation_11110_1].dlg
   limit: do 120 znaków
   EN: All Cleanup personnel to positions. Your shift's about to begin.
   PL:
774. [Kwestia głosowa [battleentry_11110_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battleentry_11110_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Kwestia głosowa [battleentry_11110_1] (Stage Entry)] 차원 파동 장갑, 충전 완료.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battleentry_11110_1].dlg
   limit: do 120 znaków
   EN: Dimensional Ripple Gauntlets charged and at the ready.
   PL:
776. [Kwestia głosowa [battle_select_11110_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_select_11110_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Kwestia głosowa [battle_select_11110_1] (Viewed in Battle)] 이번 차량을 정리한 후에 답 드리겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_select_11110_1].dlg
   limit: do 120 znaków
   EN: Please wait until this train is cleaned up. Then I'll answer your questions.
   PL:
778. [Kwestia głosowa [battle_endcommand_11110_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_endcommand_11110_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Kwestia głosowa [battle_endcommand_11110_1] (Commencing Attack)] 충전 기능 점검. 단숨에 정리하도록.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_endcommand_11110_1].dlg
   limit: do 120 znaków
   EN: Testing gear charges. Let's clean them up in one fell swoop.
   PL:
780. [Kwestia głosowa [battle_enemy_break_11110_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_enemy_break_11110_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Kwestia głosowa [battle_enemy_break_11110_1] (Enemy Stagger)] 승객 무력화 확인.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_enemy_break_11110_1].dlg
   limit: do 120 znaków
   EN: Passenger neutralization confirmed.
   PL:
782. [Kwestia głosowa [battle_break_11110_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_break_11110_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Kwestia głosowa [battle_break_11110_1] (Staggered)] 흡…
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_break_11110_1].dlg
   limit: do 120 znaków
   EN: Hup...
   PL:
784. [Kwestia głosowa [battle_kill_11110_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_kill_11110_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Kwestia głosowa [battle_kill_11110_1] (Enemy Killed)] 제압 완료. 승객 복원 준비.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_kill_11110_1].dlg
   limit: do 120 znaków
   EN: Neutralization complete. Passenger reconstruction procedure, ready to commence.
   PL:
786. [Kwestia głosowa [battle_dead_11110_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_dead_11110_1].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Kwestia głosowa [battle_dead_11110_1] (Death)] 결국 떠돌아가는 길에서… 이렇게…
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_dead_11110_1].dlg
   limit: do 120 znaków
   EN: So this is how I... in this wandering path with no end in sight...
   PL:
788. [Kwestia głosowa [choice_success_p_11110_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=choice_success_p_11110_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Kwestia głosowa [choice_success_p_11110_2] (Check Passed)] 매뉴얼은 모두 직접 숙지시켰으니… 당연한 결과다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=choice_success_p_11110_2].dlg
   limit: do 130 znaków
   EN: I made sure that everyone on the team read the manual to the letter. This is but an expected result.
   PL:
790. [Kwestia głosowa [choice_fail_n_11110_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=choice_fail_n_11110_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Kwestia głosowa [choice_fail_n_11110_1] (Check Failed)] …매뉴얼에 개선이 필요하겠군.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=choice_fail_n_11110_1].dlg
   limit: do 120 znaków
   EN: ... The manual needs an update.
   PL:
792. [Kwestia głosowa [battle_clear_11110_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_clear_11110_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Kwestia głosowa [battle_clear_11110_1] (Victory Cry)] 정리 완료. 이제부터 승객분들에게 아무 일도 없었던 것처럼 행동한다. 본 것, 들은 것, 전부 함구하도록.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_clear_11110_1].dlg
   limit: do 170 znaków
   EN: Cleanup complete. Now, since we're with the passengers, pretend what you saw didn't happen. Not a word of anything you saw or heard.
   PL:
794. [Kwestia głosowa [battle_clear_ex_11110_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_clear_ex_11110_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Kwestia głosowa [battle_clear_ex_11110_1] (Extra Conditions Fulfilled)] 정리가 예상보다 일찍 끝났군. 보고서는 내가 작성해 둘 테니, 다음 정리 전에 휴식을 취하도록.
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_clear_ex_11110_1].dlg
   limit: do 170 znaków
   EN: We wrapped that up much earlier than expected. Rest up while we wait for the next train. I'll deal with the report in the meantime.
   PL:
796. [Kwestia głosowa [battle_defeat_11110_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_defeat_11110_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Kwestia głosowa [battle_defeat_11110_1] (Defeat Wail)] …정리는 실패했고, 장비의 충전량은 바닥. 돌아갈 방법이… 없군…
   źródło: PersonalityVoiceDlg/Voice_Outis_Wcorp_11110.json :: dataList[id=battle_defeat_11110_1].dlg
   limit: do 120 znaków
   EN: ... Cleanup failed. Gear charge at... zero. I can't... go back...
   PL:

## [000] The Barber of La Manchaland — Outis — 라만차랜드 이발사
- ID Tożsamości: `11111` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 73 · szybkość: 2–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed

798. [Karta Tożsamości — tytuł] 라만차랜드\n이발사
   źródło: Personalities.json :: dataList[id=11111].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Barber\nof La Manchaland
   PL:
799. [Karta Tożsamości — nazwa] 오티스
   źródło: Personalities.json :: dataList[id=11111].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Karta Tożsamości — nazwa z tytułem] 오티스
   źródło: Personalities.json :: dataList[id=11111].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Karta Tożsamości — opis] 오티스의 열한번째 인격
   źródło: Personalities.json :: dataList[id=11111].desc
   limit: do 120 znaków
   EN: Outis’s 11th Identity
   PL:
802. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 재봉
   źródło: Skills_personality-11.json :: dataList[id=1111101].levelList[level=1].name ; dataList[id=1111101].levelList[level=2].name ; dataList[id=1111101].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Sewing
   PL:
803. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 10%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 40 소모하여, [BloodDinner] 8 당 [BloodScissorPersonalityFirst] 1 얻음\n- [BloodDinner]을 소모하지 못했으면, 자신의 [Laceration] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111101].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodScissorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades; [Laceration] = 출혈 / Bleed
   EN: On Hit with this Skill: heal 10% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 40 [BloodDinner] and gain 1 [BloodScissorPersonalityFirst] for every 8 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain +2 [Laceration] Count
   PL:
804. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111101].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1111101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1111101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111101].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1111101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1111101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 10%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 40 소모하여, [BloodDinner] 8 당 [BloodScissorPersonalityFirst] 1 얻음\n- [BloodDinner]을 소모하지 못했으면, 자신의 [Laceration] 횟수 2 증가\n<style="highlight">[WhenUse] 대상의 [Laceration] 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-11.json :: dataList[id=1111101].levelList[level=2].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodScissorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades; [Laceration] = 출혈 / Bleed
   EN: On Hit with this Skill: heal 10% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 40 [BloodDinner] and gain 1 [BloodScissorPersonalityFirst] for every 8 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain +2 [Laceration] Count\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>
   PL:
807. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 대상에게 [LineCuttingPersonality]이 있으면, [Laceration] 횟수 1 증가</style>
   źródło: Skills_personality-11.json :: dataList[id=1111101].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [LineCuttingPersonality], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LineCuttingPersonality] = 재봉 대상 / Sewing Target; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack] If target has [LineCuttingPersonality], inflict +1 [Laceration] Count</style>
   PL:
808. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 대상에게 [LineCuttingPersonality]이 있으면, [Laceration] 횟수 1 증가</style>
   źródło: Skills_personality-11.json :: dataList[id=1111101].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 807 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 10%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 40 소모하여, [BloodDinner] 8 당 [BloodScissorPersonalityFirst] 1 얻음\n- [BloodDinner]을 소모하지 못했으면, 자신의 [Laceration] 횟수 2 증가\n[WhenUse] 대상의 [Laceration] <style="highlight">6 당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-11.json :: dataList[id=1111101].levelList[level=4].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodScissorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades; [Laceration] = 출혈 / Bleed
   EN: On Hit with this Skill: heal 10% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 40 [BloodDinner] and gain 1 [BloodScissorPersonalityFirst] for every 8 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain +2 [Laceration] Count\n[WhenUse] <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>
   PL:
810. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [LineCuttingPersonality]이 있으면, [Laceration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111101].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [LineCuttingPersonality], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LineCuttingPersonality] = 재봉 대상 / Sewing Target; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has [LineCuttingPersonality], inflict +1 [Laceration] Count<style="highlight"></style>
   PL:
811. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [LineCuttingPersonality]이 있으면, [Laceration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 810 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
812. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 컷 오프
   źródło: Skills_personality-11.json :: dataList[id=1111102].levelList[level=1].name ; dataList[id=1111102].levelList[level=2].name ; dataList[id=1111102].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Scission
   PL:
813. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 10%만큼 체력 회복 (최대 20 회복)\n[WhenUse] [BloodDinner]을 최대 60 소모하여, [BloodDinner] 6 당 [BloodScissorPersonalityFirst] 1 얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음
   źródło: Skills_personality-11.json :: dataList[id=1111102].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodScissorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades; [Laceration] = 출혈 / Bleed
   EN: On Hit with this Skill: heal 10% of the HP damage dealt (max 20)\n[WhenUse] Consume up to 60 [BloodDinner] and gain 1 [BloodScissorPersonalityFirst] for every 6 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]
   PL:
814. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111102].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1111102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1111102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [LineCuttingPersonality]이 있으면, [Laceration] 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1111102].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1111102].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1111102].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [LineCuttingPersonality], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LineCuttingPersonality] = 재봉 대상 / Sewing Target; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has [LineCuttingPersonality], inflict 2 [Laceration]
   PL:
816. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111102].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1111102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1111102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [LineCuttingPersonality]이 있으면, [Laceration] 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1111102].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1111102].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1111102].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 815 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [BloodScissorPersonalityFirst] 10 이상이면, 대상에게 다음 턴에 [LineCuttingPersonality] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111102].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1111102].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloodScissorPersonalityFirst], [LineCuttingPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades; [LineCuttingPersonality] = 재봉 대상 / Sewing Target
   EN: [OnSucceedAttack] At 10+ [BloodScissorPersonalityFirst], inflict 1 [LineCuttingPersonality] on target next turn
   PL:
819. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 20%만큼 체력 회복 (최대 20 회복)\n[WhenUse] [BloodDinner]을 최대 60 소모하여, [BloodDinner] 6 당 [BloodScissorPersonalityFirst] 1 얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n<style="highlight">[WhenUse] 대상의 [Laceration] 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-11.json :: dataList[id=1111102].levelList[level=2].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodScissorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades; [Laceration] = 출혈 / Bleed
   EN: On Hit with this Skill: heal 20% of the HP damage dealt (max 20)\n[WhenUse] Consume up to 60 [BloodDinner] and gain 1 [BloodScissorPersonalityFirst] for every 6 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>
   PL:
820. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 20%만큼 체력 회복 (최대 20 회복)\n[WhenUse] [BloodDinner]을 최대 60 소모하여, [BloodDinner] 6 당 [BloodScissorPersonalityFirst] 1 얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n[WhenUse] 대상의 [Laceration] 6 이상이면, 코인 위력 +1<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111102].levelList[level=4].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodScissorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades; [Laceration] = 출혈 / Bleed
   EN: On Hit with this Skill: heal 20% of the HP damage dealt (max 20)\n[WhenUse] Consume up to 60 [BloodDinner] and gain 1 [BloodScissorPersonalityFirst] for every 6 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n[WhenUse] If target has 6+ [Laceration], Coin Power +1<style="highlight"></style>
   PL:
821. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 다음 턴에 [LineCuttingPersonality] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111102].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [LineCuttingPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LineCuttingPersonality] = 재봉 대상 / Sewing Target
   EN: [OnSucceedAttack] Inflict 1 [LineCuttingPersonality] on target next turn
   PL:
822. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 새 드레스를 맞춰주지!
   źródło: Skills_personality-11.json :: dataList[id=1111103].levelList[level=3].name ; dataList[id=1111103].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 3 · monety: 4 (+3)
   limit: do 40 znaków
   EN: I'll Make You a New Dress!
   PL:
823. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 20 회복)\n[BeforeAttack] [BloodScissorPersonalityFirst] 10 이상이면, 공격 가중치 +1\n[WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration] 6 당, 합 위력 +1 (최대 2)\n[EndSkill] 증가한 공격 가중치당 [BloodScissorPersonalityFirst] 15 소모\n[EndSkill] 대상이 사망한 경우, [BloodDinner] 10 증가. 이 스킬에서 소모한 [BloodScissorPersonalityFirst] 절반 돌려받음 (턴 당 1회)
   źródło: Skills_personality-11.json :: dataList[id=1111103].levelList[level=3].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [BloodScissorPersonalityFirst], [WhenUse], [Laceration], [EndSkill], [BloodDinner]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [BloodDinner] = 혈찬 / Bloodfeast
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 20)\n[BeforeAttack] At 10+ [BloodScissorPersonalityFirst], Atk Weight +1\n[WhenUse] If target has 5+ [Laceration], Coin Power +1\n[WhenUse] Clash Power +1 for every 6 [Laceration] on target (max 2)\n[EndSkill] Consume 15 [BloodScissorPersonalityFirst] for every Atk Weight gained\n[EndSkill] If target is killed, increase [BloodDinner] by 10. Regain half of [BloodScissorPersonalityFirst] consumed by this Skill (once per turn)
   PL:
824. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [BloodScissorPersonalityFirst] 10 이상이면, 피해량 +([BloodScissorPersonalityFirst] X 2)% (최대 38%)\n- [BloodScissorPersonalityFirst] 20 이상이면, 대신 피해량 +([BloodScissorPersonalityFirst] X 3)% (최대 90%)
   źródło: Skills_personality-11.json :: dataList[id=1111103].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [BloodScissorPersonalityFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades
   EN: [OnSucceedAttack] At 10+ [BloodScissorPersonalityFirst], deal +([BloodScissorPersonalityFirst] x 2)% damage (max 38%)\n- At 20+ [BloodScissorPersonalityFirst], deal +([BloodScissorPersonalityFirst] x 3)% damage instead (max 90%)
   PL:
828. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 20 회복)\n[BeforeAttack] [BloodScissorPersonalityFirst] 10 이상이면, 공격 가중치 +1\n<style="highlight">- [BloodScissorPersonalityFirst] 20 이상이면, 효과를 대신하여 공격 가중치 +2</style>\n[WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration] 6 당, 합 위력 +1 (최대 2)\n[EndSkill] 증가한 공격 가중치당 [BloodScissorPersonalityFirst] <style="highlight">10</style> 소모\n[EndSkill] 대상이 사망한 경우, [BloodDinner] <style="highlight">20</style> 증가. 이 스킬에서 소모한 [BloodScissorPersonalityFirst] 절반을 돌려받음 (턴 당 1회)\n<style="highlight">- 대상이 [LineCuttingPersonality]이면, [BloodDinner] 20 추가 증가, [BloodScissorPersonalityFirst] 5 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-11.json :: dataList[id=1111103].levelList[level=4].desc
   limit: do 910 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [BloodScissorPersonalityFirst], [WhenUse], [Laceration], [EndSkill], [BloodDinner], [LineCuttingPersonality]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [BloodDinner] = 혈찬 / Bloodfeast; [LineCuttingPersonality] = 재봉 대상 / Sewing Target
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 20)\n[BeforeAttack] At 10+ [BloodScissorPersonalityFirst], Atk Weight +1\n<style="highlight">- At 20+ [BloodScissorPersonalityFirst], replace the above effect with Atk Weight +2 instead</style>\n[WhenUse] If target has 5+ [Laceration], Coin Power +1\n[WhenUse] Clash Power +1 for every 6 [Laceration] on target (max 2)\n[EndSkill] Consume <style="highlight">10</style> [BloodScissorPersonalityFirst] for every Atk Weight gained\n[EndSkill] If target is killed, increase [BloodDinner] by <style="highlight">20</style>. Regain half of [BloodScissorPersonalityFirst] consumed by this Skill (once per turn)\n<style="highlight">- If target is [LineCuttingPersonality], additionally increase [BloodDinner] by 20 more, and gain 5 [BloodScissorPersonalityFirst] (once per turn)</style>
   PL:
829. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-11.json :: dataList[id=1111103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Laceration]
   PL:
830. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-11.json :: dataList[id=1111103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 829 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-11.json :: dataList[id=1111103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 829 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [BloodScissorPersonalityFirst] 10 이상이면, 피해량 +([BloodScissorPersonalityFirst] X <style="highlight">3</style>)% (최대 <style="highlight">57</style>%)\n- [BloodScissorPersonalityFirst] 20 이상이면, 대신 피해량 +([BloodScissorPersonalityFirst] X <style="highlight">4</style>)% (최대 <style="highlight">120</style>%)
   źródło: Skills_personality-11.json :: dataList[id=1111103].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [BloodScissorPersonalityFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades
   EN: [OnSucceedAttack] At 10+ [BloodScissorPersonalityFirst], deal +([BloodScissorPersonalityFirst] x <style="highlight">3</style>)% damage (max <style="highlight">57</style>%)\n- At 20+ [BloodScissorPersonalityFirst], deal +([BloodScissorPersonalityFirst] x <style="highlight">4</style>)% damage instead (max <style="highlight">120</style>%)
   PL:
833. [Obrona (ulepszenia 1,4) — nazwa] 예의에 어긋나는군!
   źródło: Skills_personality-11.json :: dataList[id=1111104].levelList[level=1].name ; dataList[id=1111104].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 7 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Quite Discourteous!
   PL:
834. [Obrona (ulepszenie 1) — opis] [WhenUse] [BloodScissorPersonalityFirst] 10 이상이면 기본 위력 +1\n[WhenUse] 자신의 [Laceration] 5 이상이면, 코인 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1111104].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodScissorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] At 10+ [BloodScissorPersonalityFirst], Base Power +1\n[WhenUse] At 5+ [Laceration], Coin Power +1
   PL:
835. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111104].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1111104].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
836. [Obrona (ulepszenie 4) — opis] [WhenUse] [BloodScissorPersonalityFirst] 10 이상이면 기본 위력 +1<style="highlight">\n- [BloodScissorPersonalityFirst] 20 이상이면 효과를 대신하여 기본 위력 +2</style>\n[WhenUse] 자신의 [Laceration] <style="highlight">5 당</style>, 코인 위력 +1 <style="highlight">(최대 3)</style>
   źródło: Skills_personality-11.json :: dataList[id=1111104].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodScissorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] At 10+ [BloodScissorPersonalityFirst], Base Power +1<style="highlight">\n- At 20+ [BloodScissorPersonalityFirst], gain Base Power +2 instead</style>\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Laceration] on self (max 3)</style>
   PL:
837. [Pasywka bojowa (od ulepszenia 1) — nazwa] 혈찬
   źródło: Passives.json :: dataList[id=1111102].name
   limit: do 40 znaków
   EN: Bloodfeast
   PL:
838. [Pasywka bojowa (od ulepszenia 1) — opis] 이 캐릭터가 전투에 등장해 있거나, 등장할 리스트에 포함되어 있으면, 1턴부터 모든 캐릭터가 받은 [Laceration] 피해만큼 [BloodDinner]이 증가함.\n이 캐릭터가 전투에 등장할 때 전장에 흩뿌려진 잠재된 피가 더욱 드러난다.
   źródło: Passives.json :: dataList[id=1111102].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: If this unit is on field, or is one of the units that can appear on this Stage, increase [BloodDinner] value by the amount of [Laceration] damage collectively received by every unit. \nWhen this unit enters the field, the sleeping blood drenching the battlefield will rise above the surface.
   PL:
839. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — nazwa] 그 옷이 아니야!!!
   źródło: Passives.json :: dataList[id=1111101].name
   limit: do 40 znaków
   EN: WRONG COSTUME!!!
   PL:
840. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — opis] 적중시 자신의 [BloodDinner_Accumulation] 10당, 피해량 +1% (최대 20%)
   źródło: Passives.json :: dataList[id=1111101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BloodDinner_Accumulation]
   znaczenie tagów: [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed
   EN: On Hit, deal +1% damage for every 10 [BloodDinner_Accumulation] by self (max 20%)
   PL:
841. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — podsumowanie] 누적 소모 혈찬에 비례하여 피해량 증가
   źródło: Passives.json :: dataList[id=1111101].summary
   limit: do 120 znaków
   EN: Deal more damage based on cumulative Bloodfeast consumed
   PL:
842. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — nazwa] 그 옷이 아니야!!!
   źródło: Passives.json :: dataList[id=1111111].name
   (powtórzenie elementu 839 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — opis] [LineCuttingPersonality]과 합을 할 때, 합 위력 +1.\n적중시 자신의 [BloodDinner_Accumulation] 10당, 피해량 +1.5% (최대 30%)\n적중시 대상의 [Laceration]당 피해량 +0.5% (최대 10%)
   źródło: Passives.json :: dataList[id=1111111].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [LineCuttingPersonality], [BloodDinner_Accumulation], [Laceration]
   znaczenie tagów: [LineCuttingPersonality] = 재봉 대상 / Sewing Target; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed; [Laceration] = 출혈 / Bleed
   EN: In a Clash against [LineCuttingPersonality], Clash Power +1.\nOn Hit, deal +1.5% damage for every 10 [BloodDinner_Accumulation] by self (max 30%)\nOn Hit, deal +0.5% damage for every [Laceration] on the target (max 10%)
   PL:
844. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — podsumowanie] 재봉 대상과 합을 할 때, 합 위력 +1
   źródło: Passives.json :: dataList[id=1111111].summary
   limit: do 120 znaków
   EN: In a Clash against Sewing Target, Clash Power +1
   PL:
845. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — nazwa] 돈키호테류 경혈 8식 가위
   źródło: Passives.json :: dataList[id=1111121].name
   limit: do 60 znaków
   EN: Don Quixote Hardblood Arts 8: Scissors
   PL:
846. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — opis] 속도가 가장 빠른 아군 1명이 공격 종료 시 적이 사망했다면, 체력 10 회복 (턴 당 최대 2회)\n속도가 가장 빠른 아군 1명이 공격 종료 시 적이 사망했다면, 다음 턴동안 스킬, 코인 효과로 [Laceration] 위력 부여 시 [Laceration] 횟수 1 증가 (턴 당 최대 3회)
   źródło: Passives.json :: dataList[id=1111121].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: 1 ally with the fastest Speed: If the enemy is killed at Attack End, heal 10 HP (2 times per turn)\n1 ally with the fastest Speed: If the enemy is killed at Attack End, inflict +1 [Laceration] Count when inflicting [Laceration] Potency with Skill or Coin effects for the next turn (3 times per turn)
   PL:
847. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — podsumowanie] 공격 종료 시 적이 사망했다면, 체력 회복
   źródło: Passives.json :: dataList[id=1111121].summary
   limit: do 120 znaków
   EN: Attack End: If the enemy is dead, heal HP
   PL:
848. [Kwestia głosowa [get_11111_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=get_11111_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Kwestia głosowa [get_11111_1] (Identity Acquisition)] 잘 왔군. 이제 진짜 치장이란 게 무엇인지 직접 보여주도록 하지… 기대하도록.
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=get_11111_1].dlg
   limit: do 120 znaków
   EN: Welcome. I'll show you what it means to really 'dress up'... You may look forward to it.
   PL:
850. [Kwestia głosowa [lobby_morning_11111_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=lobby_morning_11111_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Kwestia głosowa [lobby_morning_11111_1] (Morning Greeting)] 퍼레이드가 밤에 있다고 늘어져들 있지 마라. 거기 너, 옷의 실밥이 터져있군. 당장 꿰맬 테니 어디 가지 말고 서있어. 아침은 결식이다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=lobby_morning_11111_1].dlg
   limit: do 240 znaków
   EN: Don't laze around just because the Parade doesn't start until nightfall. You there, your seams are tearing. Stand still and I'll fix you right up—and you're skipping breakfast today.
   PL:
852. [Kwestia głosowa [lobby_noon_11111_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=lobby_noon_11111_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Kwestia głosowa [lobby_noon_11111_1] (Afternoon Greeting)] 혈액바… 그 골판지 같은 걸 씹는 것 보단 차라리 굶는게 낫지. 아! 차라리 나와 슈팅 게임 코너나 점검하지. 아직도 나를 넘어선 점수를 낸 녀석을 본 적이 없거든.
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=lobby_noon_11111_1].dlg
   limit: do 210 znaków
   EN: Hemobars... I'd rather starve than chew on that piece of cardboard. Ah! Why don't you help me test the shooting range? No one's managed to best my score just yet.
   PL:
854. [Kwestia głosowa [lobby_night_11111_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=lobby_night_11111_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Kwestia głosowa [lobby_night_11111_1] (Evening Greeting)] 음… 좋아. 아주 아름다워. 내 의상과 가면들이 밤거리를 거니는 걸 보면 피곤한 기분 따위는 싹 날아가지.\n…잠깐, 저녀석 옷을 또 거꾸로…
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=lobby_night_11111_1].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Mm... very well. Positively dashing. Feasting my eyes on the costumes and the masks of my creation walking the night streets does wonders for alleviating my fatigue.\n... Hold on, that fool's worn his outfit inside-out again...
   PL:
856. [Kwestia głosowa [smalltalk_11111_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=smalltalk_11111_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Kwestia głosowa [smalltalk_11111_1] (Chatter #1)] 실력이 출중하니까 대표 이발사의 자리를 꿰차는 거다. 제3권속일 뿐이지만, 그 실력만큼은 이 가족 안에서 내가 가장 뛰어나다…\n아, 이건 어버이에 대한 도전이 아니니 오해하진 말도록.
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=smalltalk_11111_1].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I'm not THE Barber for nothing. Though I am but a Third Kindred, my skill with the art of cutting is second to none in our Familia...\n... This is not a challenge against the Father, so I would prefer if you didn't misconstrue my claims.
   PL:
858. [Kwestia głosowa [smalltalk_11111_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=smalltalk_11111_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Kwestia głosowa [smalltalk_11111_2] (Chatter #2)] 피부에 직접 꿰어놓기 위해서는 질기고 튼튼한 실… 아니, 아예 가죽 끈이 낫겠어.\n하아… 또 아무 가죽이나 쓸 순 없지. 내가 직접 구하러 다녀야겠군.
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=smalltalk_11111_2].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I need sturdy, durable string to sew these onto the skin... hm, no. I suppose leather straps would work better for that purpose.\nHaah... I suppose I can't use just any leather. I'll go find it myself.
   PL:
860. [Kwestia głosowa [smalltalk_11111_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=smalltalk_11111_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Kwestia głosowa [smalltalk_11111_3] (Chatter #3)] 잠깐… 누구야, 어제 어트랙션 관리한 놈! 총을 맞았는데 과녁이 안 넘어가잖아! 어버이께서 안 보고 계신다고 대충대충 할 생각이냐!
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=smalltalk_11111_3].dlg
   limit: do 290 znaków
   EN: Wait... which one of you was responsible for the attraction maintenance yesterday?! You saw me hit the target, yes? Did you see it go down? No! Don't tell me you're slacking because Father isn't here to watch your every move!
   PL:
862. [Kwestia głosowa [smalltalk_11111_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=smalltalk_11111_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Kwestia głosowa [smalltalk_11111_4] (Post-Uptie Chat 1)] 싹둑, 싹둑. 거스러미 같은 천 조각은 전부 잘라내야하지. 카니발에 어울리지 않는 손님도 마찬가지야. 전부 귀퉁이 천만도 못하니.
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=smalltalk_11111_4].dlg
   limit: do 250 znaków
   EN: Snip, snip. Every thread of fabric hanging like hangnails must be snipped off. Same goes for guests who do not mesh so well with the Carnival, those lesser than even my scraps of leftover fabric.
   PL:
864. [Kwestia głosowa [smalltalk_11111_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=smalltalk_11111_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Kwestia głosowa [smalltalk_11111_5] (Post-Uptie Chat 2)] 하! 하하하하! 어이가 없어서 웃음이 다 나는군! 그런 격식 없는 복장으로 이 몸이 만든 어트랙션을 즐기려하다니!\n죽여… 아니지. 그대로 가만히. 직접 오려서 격식이라는 걸 만들어 주지!
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=smalltalk_11111_5].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ha! Hahahaha! The sheer audacity makes me laugh! How dare you saunter in here with clothes so unbecoming of my attraction?!\nI'll kill— No. Sit still, and I'll cut you up and teach you what it means to dress for the occasion!
   PL:
866. [Kwestia głosowa [neglect_11111_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=neglect_11111_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
867. [Kwestia głosowa [neglect_11111_1] (Idle)] 이곳이 내 집이야. 집으로 돌아가던 길이었는데… 아니, 여기에 내 가족이 있고 어버이와 자식들이 있어.
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=neglect_11111_1].dlg
   limit: do 160 znaków
   EN: This is my home. I was on my journey home, when— no. This is where my Family is. This is where my Father and Children are.
   PL:
868. [Kwestia głosowa [gacksung_11111_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=gacksung_11111_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Kwestia głosowa [gacksung_11111_1] (Uptying)] 퍼레이드의 준비는 끝났나? 의상은? 무대 장식은? 하… 물렁해 빠진 것들. 내가 최종 점검한다!
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=gacksung_11111_1].dlg
   limit: do 190 znaków
   EN: How are the preparations for the Parade going? Costumes? Stage prop? Haah... you lazy bums. I will take over the final review of the preparations!
   PL:
870. [Kwestia głosowa [formation_11111_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=formation_11111_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Kwestia głosowa [formation_11111_1] (Deployment)] 나를 불렀나?
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=formation_11111_1].dlg
   limit: do 120 znaków
   EN: You called?
   PL:
872. [Kwestia głosowa [battleentry_11111_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battleentry_11111_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
873. [Kwestia głosowa [battleentry_11111_1] (Stage Entry)] 카니발 타임.
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battleentry_11111_1].dlg
   limit: do 120 znaków
   EN: Carnival time.
   PL:
874. [Kwestia głosowa [battle_select_11111_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_select_11111_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Kwestia głosowa [battle_select_11111_1] (Viewed in Battle)] 음? 가면 꿰맨 끈이 떨어졌나?
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_select_11111_1].dlg
   limit: do 120 znaków
   EN: Hm? Did the strap for your mask fall off?
   PL:
876. [Kwestia głosowa [battle_endcommand_11111_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_endcommand_11111_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [Kwestia głosowa [battle_endcommand_11111_1] (Commencing Attack)] 떨거지는 잘라낸다!
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_endcommand_11111_1].dlg
   limit: do 120 znaków
   EN: I'll snip off the carbage!
   PL:
878. [Kwestia głosowa [battle_enemy_break_11111_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_enemy_break_11111_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Kwestia głosowa [battle_enemy_break_11111_1] (Enemy Stagger)] 허. 실밥이 터졌나?
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_enemy_break_11111_1].dlg
   limit: do 120 znaków
   EN: Huh. Did the seams burst?
   PL:
880. [Kwestia głosowa [battle_break_11111_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_break_11111_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [Kwestia głosowa [battle_break_11111_1] (Staggered)] 칫…
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_break_11111_1].dlg
   limit: do 120 znaków
   EN: Tsk...
   PL:
882. [Kwestia głosowa [battle_kill_11111_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_kill_11111_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [Kwestia głosowa [battle_kill_11111_1] (Enemy Killed)] 기워낼 가치는 없군. 그대로 무너져라.
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_kill_11111_1].dlg
   limit: do 120 znaków
   EN: Not even worth a patchwork. Fall apart where you stand.
   PL:
884. [Kwestia głosowa [battle_dead_11111_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_dead_11111_1].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
885. [Kwestia głosowa [battle_dead_11111_1] (Death)] 가, 가면은 씌운 채로…! 죽여… 줘…
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_dead_11111_1].dlg
   limit: do 120 znaków
   EN: A-at least let me keep the mask on...! ... Then... kill me...
   PL:
886. [Kwestia głosowa [choice_success_p_11111_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=choice_success_p_11111_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [Kwestia głosowa [choice_success_p_11111_2] (Check Passed)] 훗. 당연히 내가 1등 스코어지.
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=choice_success_p_11111_2].dlg
   limit: do 120 znaków
   EN: Heh. I knew I'd be coming first.
   PL:
888. [Kwestia głosowa [choice_fail_n_11111_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=choice_fail_n_11111_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [Kwestia głosowa [choice_fail_n_11111_1] (Check Failed)] …이 어트랙션, 왜 작동을 안하지?
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=choice_fail_n_11111_1].dlg
   limit: do 120 znaków
   EN: ... Why won't this ride start?
   PL:
890. [Kwestia głosowa [battle_clear_11111_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_clear_11111_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
891. [Kwestia głosowa [battle_clear_11111_1] (Victory Cry)] 퍼레이드는 문제 없었지만… 몇몇 복장 불량이 보이는군. 내 의상이 그런 식으로 보여지는 건 용납 못한다고 말했을 텐데…!
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_clear_11111_1].dlg
   limit: do 300 znaków
   EN: The Parade itself went off without a hitch... but I saw some of you wearing outfits not up to my uniform regulations. Haven't I told you that I will not tolerate anyone wearing the clothes of my own making in such slovenly manners?
   PL:
892. [Kwestia głosowa [battle_clear_ex_11111_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_clear_ex_11111_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [Kwestia głosowa [battle_clear_ex_11111_1] (Extra Conditions Fulfilled)] 카니발 그 자체를 대표할 만한 퍼레이드였어… 훗. 주인공 의상이 오늘 따라 한층 더 돋보이는군. 누구 작품이겠나?
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_clear_ex_11111_1].dlg
   limit: do 210 znaków
   EN: That was a Parade worthy of the Carnival... Heh. The Lady of the Parade wears a particularly dazzling dress... I needn't tell you whose design it is, must I?
   PL:
894. [Kwestia głosowa [battle_defeat_11111_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_defeat_11111_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
895. [Kwestia głosowa [battle_defeat_11111_1] (Defeat Wail)] 모든 게! 전부! 엉망이지 않나! 집에 돌아가기 부끄럽군… 아… 내가 돌아갈 집이 남아는 있던가?
   źródło: PersonalityVoiceDlg/Voice_Outis_Bloodfiend_11111.json :: dataList[id=battle_defeat_11111_1].dlg
   limit: do 190 znaków
   EN: Are! You! Seeing! This! Mess! I'm almost ashamed to return home in this state... Oh... But... to what home will I return? Is it even there, still?
   PL:

## [000] Heishou Pack - Mao Branch — Outis — 흑수 - 묘
- ID Tożsamości: `11112` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 69 · szybkość: 3–5 / 3–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture

896. [Karta Tożsamości — tytuł] 흑수 - 묘
   źródło: Personalities.json :: dataList[id=11112].title
   limit: do 40 znaków
   EN: Heishou Pack - Mao Branch
   PL:
897. [Karta Tożsamości — nazwa] 오티스
   źródło: Personalities.json :: dataList[id=11112].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Karta Tożsamości — nazwa z tytułem] 오티스
   źródło: Personalities.json :: dataList[id=11112].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [Karta Tożsamości — opis] 오티스의 열두번째 인격
   źródło: Personalities.json :: dataList[id=11112].desc
   limit: do 120 znaków
   EN: Outis’s 12th Identity
   PL:
900. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 순보
   źródło: Skills_personality-11.json :: dataList[id=1111201].levelList[level=1].name ; dataList[id=1111201].levelList[level=2].name ; dataList[id=1111201].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Blinkstep
   PL:
901. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1111201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 6+ [Burst], Coin Power +1
   PL:
902. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111201].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1111201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1111201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
903. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111201].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1111201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1111201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
904. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상의 [Burst]이 <style="highlight">4</style> 이상이면, 코인 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1111201].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has <style="highlight">4</style>+ [Burst], Coin Power +1
   PL:
905. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 속도가 12 이상이면, 코인 1회 재사용 (스킬당 1회)</style>
   źródło: Skills_personality-11.json :: dataList[id=1111201].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] At 12+ Speed, Reuse Coin once (once per Skill)</style>
   PL:
906. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 3 이상 높으면 코인 위력 +1</style>\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1111201].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: <style="highlight">If this unit's Speed is faster than the target's by 3 or more, Coin Power +1</style>\n[WhenUse] If target has 4+ [Burst], Coin Power +1
   PL:
907. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 <style="highlight">10</style> 이상이면, 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-11.json :: dataList[id=1111201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At <style="highlight">10</style>+ Speed, Reuse Coin once (once per Skill)
   PL:
908. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 척살
   źródło: Skills_personality-11.json :: dataList[id=1111202].levelList[level=1].name ; dataList[id=1111202].levelList[level=2].name ; dataList[id=1111202].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Perforating Kill
   PL:
909. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1111202].levelList[level=1].desc
   (powtórzenie elementu 901 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +10%
   źródło: Skills_personality-11.json :: dataList[id=1111202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   EN: At 10+ Speed, deal +10% damage
   PL:
911. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1111202].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1111202].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1111202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL:
912. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상의 [Burst]이 <style="highlight">4</style> 이상이면, 코인 위력 +1\n<style="highlight">[OnDirectAttack] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-11.json :: dataList[id=1111202].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [OnDirectAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [OnDirectAttack] = [일방 공격 시] / [On Unopposed Attack]
   EN: [WhenUse] If target has <style="highlight">4</style>+ [Burst], Coin Power +1\n<style="highlight">[OnDirectAttack] Inflict +1 [Burst] Count</style>
   PL:
913. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-11.json :: dataList[id=1111202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] Inflict +1 [Burst] Count</style>
   PL:
914. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +<style="highlight">20</style>%
   źródło: Skills_personality-11.json :: dataList[id=1111202].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: At 10+ Speed, deal +<style="highlight">20</style>% damage
   PL:
915. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 3 이상 높으면 코인 위력 +1</style>\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n[OnDirectAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1111202].levelList[level=4].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [OnDirectAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [OnDirectAttack] = [일방 공격 시] / [On Unopposed Attack]
   EN: <style="highlight">If this unit's Speed is faster than the target's by 3 or more, Coin Power +1</style>\n[WhenUse] If target has 4+ [Burst], Coin Power +1\n[OnDirectAttack] Inflict +1 [Burst] Count
   PL:
916. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count<style="highlight"></style>
   PL:
917. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [Agility] 1 얻음 (턴 당 2회)</style>
   źródło: Skills_personality-11.json :: dataList[id=1111202].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: <style="highlight">[OnSucceedAttack] Gain 1 [Agility] next turn (2 times per turn)</style>
   PL:
918. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +<style="highlight">30</style>%
   źródło: Skills_personality-11.json :: dataList[id=1111202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: At 10+ Speed, deal +<style="highlight">30</style>% damage
   PL:
919. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 각주살검
   źródło: Skills_personality-11.json :: dataList[id=1111203].levelList[level=3].name ; dataList[id=1111203].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Cursewrit Butcherblade
   PL:
920. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n자신의 속도가 대상보다 2 이상 높으면 코인 위력 +1\n[WhenUse] [LegStrength] 3 얻음\n[OnDirectAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111203].levelList[level=3].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse], [LegStrength], [OnDirectAttack]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】; [OnDirectAttack] = [일방 공격 시] / [On Unopposed Attack]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\nIf this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[WhenUse] Gain 3 [LegStrength]\n[OnDirectAttack] Inflict +2 [Burst] Count
   PL:
921. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1111203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_personality-11.json :: dataList[id=1111203].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1111203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstAgility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: [OnSucceedAttack] Inflict [BurstAgility]
   PL:
923. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111203].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1111203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
924. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-11.json :: dataList[id=1111203].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1111203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
925. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-11.json :: dataList[id=1111203].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1111203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Speed, Reuse Coin once (once per Skill)
   PL:
926. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n<style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 2)\n[WhenUse] 대상의 [Burst]이 15 이상이면, 코인 위력 +1</style>\n[WhenUse] [LegStrength] 3 얻음\n[OnDirectAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111203].levelList[level=4].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [WhenUse], [LegStrength], [OnDirectAttack]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】; [OnDirectAttack] = [일방 공격 시] / [On Unopposed Attack]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\n<style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)\n[WhenUse] If target has 15+ [Burst], Coin Power +1</style>\n[WhenUse] Gain 3 [LegStrength]\n[OnDirectAttack] Inflict +2 [Burst] Count
   PL:
927. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] <style="highlight">[ReUseOnSucceedAttack] [BurstAgility] 부여</style>
   źródło: Skills_personality-11.json :: dataList[id=1111203].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [BurstAgility]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: <style="highlight">[ReUseOnSucceedAttack] Inflict [BurstAgility]</style>
   PL:
928. [Obrona (ulepszenia 1,4) — nazwa] 부분 흑수화
   źródło: Skills_personality-11.json :: dataList[id=1111204].levelList[level=1].name ; dataList[id=1111204].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 5 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Partial Heishou Mutation
   PL:
929. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] [LegStrength] 3 얻음\n[WhenUse] 자신의 속도가 대상보다 2 이상 높으면, 기본 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1111204].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [LegStrength]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [DuelCounter]\n[WhenUse] Gain 3 [LegStrength]\n[WhenUse] If this unit's Speed is faster than the target's by 2 or more, Base Power +1
   PL:
930. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1111204].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1111204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 911 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
931. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[WhenUse] [LegStrength] 3 얻음\n<style="highlight">[WhenUse] 자신의 속도가 대상보다 높을수록, 기본 위력 +1 (속도 차이 2 당 기본 위력 +1. 최대 2)</style>
   źródło: Skills_personality-11.json :: dataList[id=1111204].levelList[level=4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [WhenUse], [LegStrength]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [DuelCounter]\n[WhenUse] Gain 3 [LegStrength]\n<style="highlight">[WhenUse] If this unit's Speed is faster than the target's, gain Base Power based on Speed difference (Base Power +1 for every 2 Speed difference; max 2)</style>
   PL:
932. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — nazwa] 흑수화[묘]
   źródło: Passives.json :: dataList[id=1111201].name
   limit: do 40 znaków
   EN: Heishou Mutation [Mao]
   PL:
933. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — opis] 자신에게 [LegStrength]가 있고 대상에게 [BurstAgility]이 있으면 [LegStrength]당 가하는 피해량 +5% (최대 15%)
   źródło: Passives.json :: dataList[id=1111201].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [LegStrength], [BurstAgility]
   znaczenie tagów: [LegStrength] = 각력【묘】 / Strider【Mao】; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: If this unit has [LegStrength] and the target has [BurstAgility], deal +5% damage for every [LegStrength] (max 15%)
   PL:
934. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — nazwa] 무리짓는 토끼
   źródło: Passives.json :: dataList[id=1111221].name
   limit: do 40 znaków
   EN: A Husk of Hares
   PL:
935. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — opis] 속도가 가장 빠른 아군 1명이 [Burst]이 있는 대상을 공격할 때, 가하는 피해량 +10%\n다음 턴에 [Agility] 1 얻음 (턴 당 최대 1회)
   źródło: Passives.json :: dataList[id=1111221].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Agility]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Agility] = 신속 / Haste
   EN: 1 ally with the fastest Speed: when attacking targets with [Burst], deal +10% damage\nGain 1 [Agility] next turn (once per turn)
   PL:
936. [Kwestia głosowa [get_11112_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=get_11112_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
937. [Kwestia głosowa [get_11112_1] (Identity Acquisition)] 토끼에게 붙을 이름은 없다. 나는 그저, 아무것도 아닌 그림자 속 짐승일 뿐이니.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=get_11112_1].dlg
   limit: do 120 znaków
   EN: The hare has no name. I am nothing but an animal lurking in the shadows.
   PL:
938. [Kwestia głosowa [lobby_morning_11112_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=lobby_morning_11112_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
939. [Kwestia głosowa [lobby_morning_11112_1] (Morning Greeting)] 부르심이 없다면, 저는 볕이 들어 있는 동안 없는 것과 마찬가지의 존재입니다. 주군께선 주군의 집무에 충실하소서.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=lobby_morning_11112_1].dlg
   limit: do 150 znaków
   EN: Without your calling, the shadow dissipates under the sun. You may focus on your business of the day, my lord.
   PL:
940. [Kwestia głosowa [lobby_noon_11112_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=lobby_noon_11112_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
941. [Kwestia głosowa [lobby_noon_11112_1] (Afternoon Greeting)] 오찬이 준비되었다 합니다. 말씀하신 대로 식사 중에 일어날 부딪힘을 대비하기 위해, 저는 응달 속에 숨도록 하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=lobby_noon_11112_1].dlg
   limit: do 170 znaków
   EN: Your luncheon is prepared. Now, I retreat into the shadows to ready myself for the assault you foresaw would unfold over this meal.
   PL:
942. [Kwestia głosowa [lobby_night_11112_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=lobby_night_11112_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
943. [Kwestia głosowa [lobby_night_11112_1] (Evening Greeting)] 각자 자리했습니다. 아주 작은 신호만 전해주신다면, 토끼 떼가 달빛을 전부 가리울 것입니다. 적들의 눈에 마지막으로 담는 빛도 그것이 마지막일 테죠.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=lobby_night_11112_1].dlg
   limit: do 210 znaków
   EN: All in position. Give us but the smallest signal, and this husk of hares shall descend and blot out the very moon—the very last light your foes shall ever see.
   PL:
944. [Kwestia głosowa [smalltalk_11112_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=smalltalk_11112_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [Kwestia głosowa [smalltalk_11112_1] (Chatter #1)] 주군께 감히 충고하건대, 저희를 도구로서 가까이하시되 마음으로는 멀리 두소서. 그림자에 사는 짐승들은 그저 주군이라 정해진 자에게 충성할 뿐, 사람에게 충성하지는 않으므로.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=smalltalk_11112_1].dlg
   limit: do 300 znaków
   EN: Impertinent as it may be, I must impart to you a word of advice. Hold us close as tools in your hands, my lord, but never close to your heart. The loyalty of beasts lurking in the umbra lies with the title, not the one who wears it.
   PL:
946. [Kwestia głosowa [smalltalk_11112_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=smalltalk_11112_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
947. [Kwestia głosowa [smalltalk_11112_2] (Chatter #2)] 하나가 죽어도 둘이 나타나 상대할 것입니다. 사로잡힌다 한들, 저희는 그저 사라질 뿐 주군의 말은 들은 적이 없고, 주군의 행적은 본 적도 없는 몸입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=smalltalk_11112_2].dlg
   limit: do 230 znaków
   EN: Where a shadow falls, two shall spring from whence it fell. Were we to be captured, we will dissipate like the traceless dust; we will have never heard nor seen of you, my lord.
   PL:
948. [Kwestia głosowa [smalltalk_11112_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=smalltalk_11112_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
949. [Kwestia głosowa [smalltalk_11112_3] (Chatter #3)] 다른 흑수에게는 관심이 없습니다. 이미 그들에 대해, 필요한 정보는 전부 알고 있으므로. 주군께서 몇 무리의 흑수를 부리시는지, 그들이 각각 누구인지… 제게 알리실 필요 없습니다.\n제가 듣더라도 그건 한 순간의 그림자 연극일 뿐, 저는 도로 그것을 모르는 자로 돌아갈 것입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=smalltalk_11112_3].dlg
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I have no interest in the other Heishou, for I already know all that I must know about them. You needn't inform me of which Pack you wield, or the individualities of whom you wield.\nWere you to regale me of them nonetheless, it shall be but the ephemeral play of shadows, to be forgotten soon since.
   PL:
950. [Kwestia głosowa [smalltalk_11112_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=smalltalk_11112_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
951. [Kwestia głosowa [smalltalk_11112_4] (Post-Uptie Chat 1)] 주군, 이 자리는 끝이 난 것 같습니다. 다른 토끼들은 이 건물에 더 물어뜯을 것은 없는지 주위를 맴돌고 있습니다.\n명하실 것이 더 없다면, 물러가겠습니다만… 혹시나 숨은 짐승이 없는지 주의 깊게 관찰토록 하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=smalltalk_11112_4].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There is no more to be done here, my lord. The other hares are scouring the building in search of more to graze on.\nIf you have no remaining commands, I will excuse myself... but I will remain vigilant of other lurking beasts.
   PL:
952. [Kwestia głosowa [smalltalk_11112_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=smalltalk_11112_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
953. [Kwestia głosowa [smalltalk_11112_5] (Post-Uptie Chat 2)] 야음의 땅은 짐승들에게 있어 가장 우위를 갖는 공간이다.\n…알겠나. 토끼가 네놈을 바라보고 있던 시점부터, 네 명줄이 그 순간 끊어졌다는 것이다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=smalltalk_11112_5].dlg
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The cover of darkness provides a great advantage to the beasts...\nDo you understand? Your life was forfeit the moment this hare locked its eyes upon you.
   PL:
954. [Kwestia głosowa [neglect_11112_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=neglect_11112_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
955. [Kwestia głosowa [neglect_11112_1] (Idle)] …….
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=neglect_11112_1].dlg
   limit: do 120 znaków
   EN: …….
   PL:
956. [Kwestia głosowa [gacksung_11112_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=gacksung_11112_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [Kwestia głosowa [gacksung_11112_1] (Uptying)] 일러주신 적은 처리되었습니다. 다음으로 뜀박질할 곳을 알려주시겠습니까.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=gacksung_11112_1].dlg
   limit: do 120 znaków
   EN: Your foe has been eliminated. To where must I hop next?
   PL:
958. [Kwestia głosowa [formation_11112_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=formation_11112_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
959. [Kwestia głosowa [formation_11112_1] (Deployment)] 명을 받듭니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=formation_11112_1].dlg
   limit: do 120 znaków
   EN: I accept your command.
   PL:
960. [Kwestia głosowa [battleentry_11112_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battleentry_11112_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
961. [Kwestia głosowa [battleentry_11112_1] (Stage Entry)] 야음을 틈타.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battleentry_11112_1].dlg
   limit: do 120 znaków
   EN: Through the dead of night.
   PL:
962. [Kwestia głosowa [battle_select_11112_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_select_11112_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
963. [Kwestia głosowa [battle_select_11112_1] (Viewed in Battle)] 주군께서 찾아오시는 건… 아니, 말씀하십시오.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_select_11112_1].dlg
   limit: do 120 znaków
   EN: My lord, to be present here in your person is— No, my lord. Please, do speak your will.
   PL:
964. [Kwestia głosowa [battle_endcommand_11112_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_endcommand_11112_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
965. [Kwestia głosowa [battle_endcommand_11112_1] (Commencing Attack)] 베어내리.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_endcommand_11112_1].dlg
   limit: do 120 znaków
   EN: I will cut them down.
   PL:
966. [Kwestia głosowa [battle_enemy_break_11112_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_enemy_break_11112_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
967. [Kwestia głosowa [battle_enemy_break_11112_1] (Enemy Stagger)] 불쌍하게 울부짖는군.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_enemy_break_11112_1].dlg
   limit: do 120 znaków
   EN: What a pathetic cry.
   PL:
968. [Kwestia głosowa [battle_break_11112_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_break_11112_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
969. [Kwestia głosowa [battle_break_11112_1] (Staggered)] …큭.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_break_11112_1].dlg
   limit: do 120 znaków
   EN: ... Kah.
   PL:
970. [Kwestia głosowa [battle_kill_11112_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_kill_11112_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
971. [Kwestia głosowa [battle_kill_11112_1] (Enemy Killed)] 이제 끝내지.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_kill_11112_1].dlg
   limit: do 120 znaków
   EN: You're finished.
   PL:
972. [Kwestia głosowa [battle_dead_11112_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_dead_11112_1].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
973. [Kwestia głosowa [battle_dead_11112_1] (Death)] 내가… 죽어도… 묘는…
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_dead_11112_1].dlg
   limit: do 120 znaków
   EN: I may die here... but... the Mao branch shall...
   PL:
974. [Kwestia głosowa [choice_success_p_11112_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=choice_success_p_11112_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
975. [Kwestia głosowa [choice_success_p_11112_2] (Check Passed)] 간단한 명령입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=choice_success_p_11112_2].dlg
   limit: do 120 znaków
   EN: Effortlessly handled.
   PL:
976. [Kwestia głosowa [choice_fail_n_11112_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=choice_fail_n_11112_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
977. [Kwestia głosowa [choice_fail_n_11112_1] (Check Failed)] …이 일에 더 적합한 토끼를 찾죠.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=choice_fail_n_11112_1].dlg
   limit: do 120 znaków
   EN: ... Let us find a hare better suited to handle this.
   PL:
978. [Kwestia głosowa [battle_clear_11112_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_clear_11112_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
979. [Kwestia głosowa [battle_clear_11112_1] (Victory Cry)] 명을 수행했습니다. 비록 묘의 손실은 컸지만, 신경 쓰실 것 없습니다. 사라진 만큼 묘는 다시 얼굴을 드러낼 것입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_clear_11112_1].dlg
   limit: do 200 znaków
   EN: I have carried out your command. The Mao branch has suffered significant losses, yet it is not for you to worry. More of us shall appear to fill the void.
   PL:
980. [Kwestia głosowa [battle_clear_ex_11112_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_clear_ex_11112_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
981. [Kwestia głosowa [battle_clear_ex_11112_1] (Extra Conditions Fulfilled)] 그림자가 그들을 덮었습니다. 청소부가 다녀가고 날이 밝으면, 죽은 자의 흔적을 찾으려는 자들이 와도 아무것도 알 수 없을 것입니다. 볕이 들면 그림자는 거두어지므로.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_clear_ex_11112_1].dlg
   limit: do 260 znaków
   EN: They are now in the shadows. Once the Sweepers finish their night's labor, once the day breaks anew, those seeking traces of the departed shall leave empty-handed. The umbra dissipates in the sun's light.
   PL:
982. [Kwestia głosowa [battle_defeat_11112_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_defeat_11112_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
983. [Kwestia głosowa [battle_defeat_11112_1] (Defeat Wail)] 제 실패가 흑수의 실패는 아닙니다. 저 역시 수많은 짐승 중 하나인, 아무것도 아닌 자일 뿐. 곧 실패를 덮기 위한 다른 짐승 떼가 나타날 것입니다.
   źródło: PersonalityVoiceDlg/Voice_Outis_Blackwater_11112.json :: dataList[id=battle_defeat_11112_1].dlg
   limit: do 210 znaków
   EN: My failure is not the failure of our Heishou Pack. I am but one of many beasts... for I am nobody, nothing at all. More will arrive in droves to erase this failure.
   PL:

## [000] T Corp. Class 3 VDCU Staff — Outis — T사 3등급 강력징수직 직원
- ID Tożsamości: `11113` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 73 · szybkość: 2–5 / 3–6 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor

984. [Karta Tożsamości — tytuł] T사 3등급\n강력징수직 직원
   źródło: Personalities.json :: dataList[id=11113].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: T Corp. Class 3\nVDCU Staff
   PL:
985. [Karta Tożsamości — nazwa] 오티스
   źródło: Personalities.json :: dataList[id=11113].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
986. [Karta Tożsamości — nazwa z tytułem] 오티스
   źródło: Personalities.json :: dataList[id=11113].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
987. [Karta Tożsamości — opis] 오티스의 열세번째 인격
   źródło: Personalities.json :: dataList[id=11113].desc
   limit: do 120 znaków
   EN: Outis’s 13th Identity
   PL:
988. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 징수 준비
   źródło: Skills_personality-11.json :: dataList[id=1111301].levelList[level=1].name ; dataList[id=1111301].levelList[level=2].name ; dataList[id=1111301].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Prepare To Collect
   PL:
989. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1111301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +1 [Vibration] Count
   PL:
990. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1111301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL:
991. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-11.json :: dataList[id=1111301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 990 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
992. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Vibration] 횟수 <style="highlight">2</style> 증가\n<style="highlight">[WhenUse] 대상의 [Vibration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-11.json :: dataList[id=1111301].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +<style="highlight">2</style> [Vibration] Count\n<style="highlight">[WhenUse] If target has 6+ [Vibration], Coin Power +1</style>
   PL:
993. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1111301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count<style="highlight"></style>
   PL:
994. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111301].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1111301].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 993 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
995. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 <style="highlight">3</style> 증가\n[WhenUse] 대상의 [Vibration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1111301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +<style="highlight">3</style> [Vibration] Count\n[WhenUse] If target has 6+ [Vibration], Coin Power +1
   PL:
996. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] T사식 공진 모듈
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=1].name ; dataList[id=1111302].levelList[level=2].name ; dataList[id=1111302].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 3 · monety: 3 (+5)
   limit: do 40 znaków
   EN: T Corp. Microcavity Module
   PL:
997. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count
   PL:
998. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
999. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 998 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1000. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 3 이상이면, [VibrationExplosion] 1회. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 3+ [Vibration] Count, trigger [VibrationExplosion] once; then, reduce target's [Vibration] Count by 1
   PL:
1001. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 [Vibration] 횟수 <style="highlight">3</style> 증가\n<style="highlight">[WhenUse] 대상의 [Vibration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +<style="highlight">3</style> [Vibration] Count\n<style="highlight">[WhenUse] If target has 6+ [Vibration], Coin Power +1</style>
   PL:
1002. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1111302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]<style="highlight"></style>
   PL:
1003. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1111302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1002 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1004. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 대상의 [Vibration]이 10 이상이면, 대상의 [Vibration]을 4 소모하여 대상과 자신의 [Vibration] 횟수 2 증가</style>
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] If target has 10+ [Vibration], consume 4 [Vibration] on target to apply +2 [Vibration] Count to both the target and self</style>
   PL:
1005. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 대상이 [Switch_Vibration]이나 [FusionVibration] 상태가 아니면, 자신의 [Vibration] 횟수를 3 소모하여 [VibrationChainPersonality]로 [Switch_Vibration]</style>
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Switch_Vibration], [FusionVibration], [Vibration], [VibrationChainPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement; [Vibration] = 진동 / Tremor; [VibrationChainPersonality] = 진동 - 사슬 / Tremor - Chain
   EN: <style="highlight">[OnSucceedAttack] If the target isn't in [Switch_Vibration] or [FusionVibration] states, consume 3 [Vibration] Count on self to trigger [Switch_Vibration] into [VibrationChainPersonality]</style>
   PL:
1006. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 3 이상이면, [VibrationExplosion] 1회. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 3+ [Vibration] Count, trigger [VibrationExplosion] once; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL:
1007. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 <style="highlight">4</style> 증가\n[WhenUse] 대상의 [Vibration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +<style="highlight">4</style> [Vibration] Count\n[WhenUse] If target has 6+ [Vibration], Coin Power +1
   PL:
1008. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration]이 10 이상이면, 대상의 [Vibration]을 4 소모하여 대상과 자신의 [Vibration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If target has 10+ [Vibration], consume 4 [Vibration] on target to apply +2 [Vibration] Count to both the target and self<style="highlight"></style>
   PL:
1009. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">대상이 [Switch_Vibration]이나 [FusionVibration] 상태면, 이 코인 피해량 +60%</style>
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Switch_Vibration], [FusionVibration]
   znaczenie tagów: [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: <style="highlight"> If target is in either [Switch_Vibration] or [FusionVibration] states, this Coin deals +60% damage</style>
   PL:
1010. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상이 [Switch_Vibration]이나 [FusionVibration] 상태가 아니면, 자신의 [Vibration] 횟수를 3 소모하여 [VibrationChainPersonality]로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Switch_Vibration], [FusionVibration], [Vibration], [VibrationChainPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement; [Vibration] = 진동 / Tremor; [VibrationChainPersonality] = 진동 - 사슬 / Tremor - Chain
   EN: [OnSucceedAttack] If the target isn't in [Switch_Vibration] or [FusionVibration] states, consume 3 [Vibration] Count on self to trigger [Switch_Vibration] into [VibrationChainPersonality]<style="highlight"></style>
   PL:
1011. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 3 이상이면, [VibrationExplosion] 1회. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111302].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 1006 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1012. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] T3형 징수 철퇴 최대 전개
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=3].name ; dataList[id=1111303].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 50 znaków
   EN: T-3 Collector Mace Max Activation
   PL:
1013. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상이 [TimeSuspend]를 보유한 상태면, 피해량 +30%\n[WhenUse] 대상의 [Vibration]이 6 이상이면, 코인 위력 +1\n[EndSkill] 자신의 [TimeRentalTwoPersonality] 소멸\n[EndSkill] [OutisNoHat] 얻음 (전투 당 1회)
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=3].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [TimeSuspend], [WhenUse], [Vibration], [EndSkill], [TimeRentalTwoPersonality], [OutisNoHat]
   znaczenie tagów: [TimeSuspend] = 시간 유예 / Time Moratorium; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [OutisNoHat] = 강력 징수 집행 / Violent Collections
   EN: If target has [TimeSuspend], deal +30% damage\n[WhenUse] If target has 6+ [Vibration], Coin Power +1\n[EndSkill] Lose [TimeRentalTwoPersonality] on self\n[EndSkill] Gain [OutisNoHat] (once per Encounter)
   PL:
1014. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
1015. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration]을 최대 3 소모\n- (소모한 [Vibration] x 2)만큼 자신의 진동 횟수 증가\n- 다음 턴에 (소모한 [Vibration] - 1)만큼 [Binding] 부여
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Vibration], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Consume up to 3 [Vibration] on target\n- Gain +([Vibration] consumed x 2) [Vibration] Count\n- Inflict ([Vibration] consumed - 1) [Binding] next turn
   PL:
1016. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 3+ [Vibration] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
1017. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnStartCoin] 자신의 [Vibration] 횟수를 모두 소모\n- 소모한 [Vibration] 횟수 5당 코인 위력 +1 (최대 5)\n- 소모한 [Vibration] 횟수 1 당 피해량 +1% (최대 50%)
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [OnStartCoin], [Vibration]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Vibration] = 진동 / Tremor
   EN: [OnStartCoin] Consume all [Vibration] Count on self\n- Coin Power +1 for every 5 [Vibration] Count consumed (max 5)\n- Deal +1% damage for every 1 [Vibration] Count consumed (max 50%)
   PL:
1018. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
1019. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신이 [TimeRentalTwoPersonality]를 보유한 상태면, [VibrationExplosion]
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TimeRentalTwoPersonality], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If this unit has [TimeRentalTwoPersonality], trigger [VibrationExplosion]
   PL:
1020. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 자신이 [TimeRentalTwoPersonality]를 보유한 상태면, [TimeSuspend] 2 부여
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TimeRentalTwoPersonality], [TimeSuspend]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [TimeSuspend] = 시간 유예 / Time Moratorium
   EN: [OnSucceedAttack] If this unit has [TimeRentalTwoPersonality], inflict 2 [TimeSuspend]
   PL:
1021. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">대상이 [Switch_Vibration]이나 [FusionVibration] 상태면, 피해량 +30%</style>\n대상이 [TimeSuspend] 상태면, 피해량 +30%\n<style="highlight">[WhenUse] 대상의 [Vibration] 6 당 코인 위력 +1 (최대 2)</style>\n<style="highlight">[WhenUse] 대상에게 [Binding]이 있으면, 합 위력 +1</style>\n[EndSkill] 자신의 [TimeRentalTwoPersonality] 소멸\n[EndSkill] [OutisNoHat] 얻음 (전투 당 1회)
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=4].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Switch_Vibration], [FusionVibration], [TimeSuspend], [WhenUse], [Vibration], [Binding], [EndSkill], [TimeRentalTwoPersonality], [OutisNoHat]
   znaczenie tagów: [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement; [TimeSuspend] = 시간 유예 / Time Moratorium; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Binding] = 속박 / Bind; [EndSkill] = [공격 종료시] / [Attack End]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time …
   EN: <style="highlight">If target is in either [Switch_Vibration] or [FusionVibration] states, deal +30% damage</style>\nIf target has [TimeSuspend], deal +30% damage\n<style="highlight">[WhenUse] Coin Power +1 for every 6 [Vibration] on target (max 2)</style>\n<style="highlight">[WhenUse] If target has [Binding] Clash Power +1</style>\n[EndSkill] Lose [TimeRentalTwoPersonality] on self\n[EndSkill] Gain [OutisNoHat] (once per Encounter)
   PL:
1022. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count<style="highlight"></style>
   PL:
1023. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration]을 최대 3 소모<style="highlight"></style>\n- (소모한 [Vibration] x 2)만큼 자신의 진동 횟수 증가<style="highlight"></style>\n- 다음 턴에 (소모한 [Vibration] - 1)만큼 [Binding] 부여<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Vibration], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Consume up to 3 [Vibration] on target<style="highlight"></style>\n- Gain +([Vibration] consumed x 2) [Vibration] Count<style="highlight"></style>\n- Inflict ([Vibration] consumed - 1) [Binding] next turn<style="highlight"></style>
   PL:
1024. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 3+ [Vibration] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL:
1025. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnStartCoin] 자신의 [Vibration] 횟수를 모두 소모<style="highlight"></style>\n- 소모한 [Vibration] 횟수 <style="highlight">4</style>당 코인 위력 +1 (최대 5)\n- 소모한 [Vibration] 횟수 1당 피해량 <style="highlight">+2%</style> (최대 100%)
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnStartCoin], [Vibration]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Vibration] = 진동 / Tremor
   EN: [OnStartCoin] Consume all [Vibration] Count on self<style="highlight"></style>\n- Coin Power +1 for every <style="highlight">4</style> [Vibration] Count consumed (max 5)\n- Deal +<style="highlight">2</style>% damage for every 1 [Vibration] Count consumed (max 100%)
   PL:
1026. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL:
1027. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신이 [TimeRentalTwoPersonality]를 보유한 상태면, [VibrationExplosion]<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [TimeRentalTwoPersonality], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If this unit has [TimeRentalTwoPersonality], trigger [VibrationExplosion]<style="highlight"></style>
   PL:
1028. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 자신이 [TimeRentalTwoPersonality]를 보유한 상태면, [TimeSuspend] 2 부여<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111303].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [TimeRentalTwoPersonality], [TimeSuspend]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [TimeSuspend] = 시간 유예 / Time Moratorium
   EN: [OnSucceedAttack] If this unit has [TimeRentalTwoPersonality], inflict 2 [TimeSuspend]<style="highlight"></style>
   PL:
1029. [Obrona (ulepszenia 1,4) — nazwa] 시간 대여 - 공진
   źródło: Skills_personality-11.json :: dataList[id=1111304].levelList[level=1].name ; dataList[id=1111304].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 3 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Borrowed Time - Microcavity
   PL:
1030. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] [TimeRentalTwoPersonality] 상태가 아니면, 턴 종료 시 [TimeRentalTwoPersonality] 4 얻음 (턴 당 1회)\n[WinDuel] 대상과 자신의 [Vibration] 횟수 2 증가\n[DefeatDuel] 자신의 [Vibration] 횟수 4 증가
   źródło: Skills_personality-11.json :: dataList[id=1111304].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [TimeRentalTwoPersonality], [WinDuel], [Vibration], [DefeatDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [WinDuel] = [합 승리시] / [Clash Win]; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [CanDuelGuard]\n[StartBattle] If this unit is not in a [TimeRentalTwoPersonality] state, gain 4 [TimeRentalTwoPersonality] at Turn End (once per turn)\n[WinDuel] Apply +2 [Vibration] Count to both the target and self\n[DefeatDuel] Gain +4 [Vibration] Count
   PL:
1031. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-11.json :: dataList[id=1111304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
1032. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[StartBattle] [TimeRentalTwoPersonality] 상태가 아니면, 턴 종료 시 [TimeRentalTwoPersonality] 4 얻음 (턴 당 1회)\n[WinDuel] 대상과 자신의 [Vibration] 횟수 2 증가\n[DefeatDuel] 자신의 [Vibration] 횟수 4 증가<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111304].levelList[level=4].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [StartBattle], [TimeRentalTwoPersonality], [WinDuel], [Vibration], [DefeatDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [WinDuel] = [합 승리시] / [Clash Win]; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [CanDuelGuard]\n[StartBattle] If this unit is not in a [TimeRentalTwoPersonality] state, gain 4 [TimeRentalTwoPersonality] at Turn End (once per turn)\n[WinDuel] Apply +2 [Vibration] Count to both the target and self\n[DefeatDuel] Gain +4 [Vibration] Count<style="highlight"></style>
   PL:
1033. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-11.json :: dataList[id=1111304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL:
1034. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — nazwa] 황금 시간 - 공진
   źródło: Passives.json :: dataList[id=1111301].name
   limit: do 40 znaków
   EN: Golden Time - Microcavity
   PL:
1035. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — opis] 턴 종료 시 체력이 10% ~ 20% 사이로 남았을 때, 전체 체력의 80%만큼 즉시 회복. 흐트러짐 상태 해제 (전투 당 1회)\n\n자신이 [TimeRentalTwoPersonality] 상태면, 자신의 스킬 최종 위력 +1
   źródło: Passives.json :: dataList[id=1111301].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [TimeRentalTwoPersonality]
   znaczenie tagów: [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time
   EN: Turn End: If this unit's HP is between 10% ~ 20%, instantly heal 80% of this unit's max HP, and recover from Stagger. (once per Encounter)\n\nIf this unit has [TimeRentalTwoPersonality], its Skills gain Final Power +1
   PL:
1036. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — podsumowanie] [TimeRentalTwoPersonality] 상태면, 스킬 최종 위력 +1
   źródło: Passives.json :: dataList[id=1111301].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TimeRentalTwoPersonality]
   znaczenie tagów: [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time
   EN: In [TimeRentalTwoPersonality] state, Skills gain Final Power +1
   PL:
1037. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Sloth) — nazwa] 신속 공무 집행
   źródło: Passives.json :: dataList[id=1111321].name
   limit: do 60 znaków
   EN: Expeditious Execution of Official Duties
   PL:
1038. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Sloth) — opis] 속도가 가장 빠른 아군 1명이 흐트러짐 상태인 대상을 공격할 때, 피해량 +10%
   źródło: Passives.json :: dataList[id=1111321].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed deals +10% damage when attacking a Staggered target.
   PL:
1039. [Kwestia głosowa [get_11113_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=get_11113_1].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1040. [Kwestia głosowa [get_11113_1] (Identity Acquisition)] 변론은 31초. 기준은 T사 중앙 시계탑을 기준. 그 이상은 허락하지 않겠다.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=get_11113_1].dlg
   limit: do 160 znaków
   EN: You have thirty-one T Corp. central clock tower seconds to present your defense. No additional time will be allocated.
   PL:
1041. [Kwestia głosowa [lobby_morning_11113_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=lobby_morning_11113_1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1042. [Kwestia głosowa [lobby_morning_11113_1] (Morning Greeting)] 하루를 아침, 점심, 저녁으로 구분하는 것만큼 의미 없는 일도 없지. 어차피… 나의 아침은 고액 체납자 네놈들의 하루를 합친 것보다 길테니.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=lobby_morning_11113_1].dlg
   limit: do 210 znaków
   EN: It's pointless to divide your days into mornings, days, and afternoons. My morning has to be longer than the sum of all of you significant defaulters' days anyway.
   PL:
1043. [Kwestia głosowa [lobby_noon_11113_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=lobby_noon_11113_1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1044. [Kwestia głosowa [lobby_noon_11113_1] (Afternoon Greeting)] 나의 점심식사 시간이 3시간 20분인 것은, 너무나 바쁘게 살아가는 나에게 최소한의 사회적 교류를 할 시간을 제공하기 위해서지. 누군가에게는 아침, 누군가에게는 저녁일 순 있겠지만 말이다.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=lobby_noon_11113_1].dlg
   limit: do 300 znaków
   EN: Part of the reason I enjoy a three-hour-and-twenty-minute lunch is to give myself a minimum allotted socializing time in midst of this busy hustle of a life. Though, for some, it could be breakfast while it may be dinnertime for others.
   PL:
1045. [Kwestia głosowa [lobby_night_11113_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=lobby_night_11113_1].desc
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1046. [Kwestia głosowa [lobby_night_11113_1] (Evening Greeting)] 걱정마라. 나의 밤은 길다. 시간주의 사회에서 밤의 길이가 다른 것은 누구의 탓도 아닌 네 탓이다. 좀 더 근면히 살아가도록.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=lobby_night_11113_1].dlg
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Don't worry. I have long nights.\nComing out on the wrong side of the nighttime wealth disparity in a meritocracy is a personal failure. Learn to be frugal.
   PL:
1047. [Kwestia głosowa [smalltalk_11113_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=smalltalk_11113_1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1048. [Kwestia głosowa [smalltalk_11113_1] (Chatter #1)] 어이, 내가 말한 시간 적금은 제대로 들고 있겠지? 한심하게 늦잠이나 자겠다고 시간을 쓰진 말도록. 알겠나? 시간이란 건 꼭 써야할 때 없는 법이니까.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=smalltalk_11113_1].dlg
   limit: do 290 znaków
   EN: Hey. Have you been keeping up with deposits into an installment savings account like I told you to? Don't waste your time on insignificant fancies like sleeping in, am I understood? There is never enough time when you need it.
   PL:
1049. [Kwestia głosowa [smalltalk_11113_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=smalltalk_11113_2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1050. [Kwestia głosowa [smalltalk_11113_2] (Chatter #2)] 조직적으로 시간을 불법유통하는 놈들에게는 더 특별한 징수가 필요하지… 그게 강력징수직이 있는 이유다. 수탈한 시간을 이용해 떼로 덤비더라도, 가볍게 제압할 수 있는 징수직. 그게… 바로 우리다.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=smalltalk_11113_2].dlg
   limit: do 370 znaków
   EN: Organized time trafficking efforts require a more specialized collection methodology. That is why the Violent Defaulter Collections Unit exists. Elite Collection Staff who can handily withstand and wipe the floor with whoever dares to come at us with their ill-gotten time... that's us.
   PL:
1051. [Kwestia głosowa [smalltalk_11113_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=smalltalk_11113_3].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1052. [Kwestia głosowa [smalltalk_11113_3] (Chatter #3)] 이 모자는 신분의 표시… 더 높은 등급의 직원이 될수록 그 위상을 드높이듯 모자의 길이 또한 높고 길어진다.\n당연히 품위있는 고등급 직원이라면 그 모자를 떨어뜨리지 않고 징수를 수행할 수 있다는 속 깊은 뜻 또한 존재하지.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=smalltalk_11113_3].dlg
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This hat's a status symbol... the higher we rise in the employee Class hierarchy, the taller the hat gets, just like our statuses.\nOf course, therein exists a double meaning—that higher-ranking employees with proper class possess the finesse to conduct their collection efforts without losing their hats.
   PL:
1053. [Kwestia głosowa [smalltalk_11113_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=smalltalk_11113_4].desc
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1054. [Kwestia głosowa [smalltalk_11113_4] (Post-Uptie Chat 1)] …그래. 아직 나는 미숙한 점이 있다는 뜻이겠지. 고전하곤 있지만, 모자를 떨어뜨리다니. 적어도 이 임무만큼은… 시간 낭비가 되진 않겠어.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=smalltalk_11113_4].dlg
   limit: do 220 znaków
   EN: ... Indeed. This could only mean that I do have some room for improvement. I'm far from struggling, but... to drop my hat? At least this mission'll make it worth my time.
   PL:
1055. [Kwestia głosowa [smalltalk_11113_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=smalltalk_11113_5].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1056. [Kwestia głosowa [smalltalk_11113_5] (Post-Uptie Chat 2)] 하, 시간 금고인가? 액자 뒤에 숨긴다면 모를 줄 알았나. 시공간 계측기를 사용하지 않아도 티가 난다.\n밀수한 시계를 모아두는 데에 이런 값 싼 금고를 쓴다니… 금기를 어기는 놈들이라 그런가, 알아줄 만한 바보군.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=smalltalk_11113_5].dlg
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hah, time vault? Did you really think that behind a picture frame was an inconspicuous place to hide it? I didn't even need to break out the Time-space Counter.\nAnd using such a cheap, shoddy vault for precious time...? I suppose it's that same <i>extraordinary</i> intellect that led them to break Taboos.
   PL:
1057. [Kwestia głosowa [neglect_11113_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=neglect_11113_1].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1058. [Kwestia głosowa [neglect_11113_1] (Idle)] 신경 쓰지 마라. 나는 네가 아무런 말을 하고 있지 않는 이 때에도 계속해서 일을 처리하고 있으니. 흠, 벌써 네 건의 징수를 완료했지.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=neglect_11113_1].dlg
   limit: do 170 znaków
   EN: Pay no mind. I'm still working on various responsibilities even in lieu of your commentary. Hm. Tally's already at four collections.
   PL:
1059. [Kwestia głosowa [gacksung_11113_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=gacksung_11113_1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1060. [Kwestia głosowa [gacksung_11113_1] (Uptying)] 내가 모자를 놓치게 하다니… 칭찬해주지. T3형 징수기 모델 - 철퇴, 최대 전개.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=gacksung_11113_1].dlg
   limit: do 120 znaków
   EN: You made me drop my hat... impressive. T-3 Repossessor Model - Mace, engage max activation.
   PL:
1061. [Kwestia głosowa [formation_11113_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=formation_11113_1].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1062. [Kwestia głosowa [formation_11113_1] (Deployment)] 바로 가지. 이 순간에도 시간이 새고 있다.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=formation_11113_1].dlg
   limit: do 120 znaków
   EN: Let's leave right away. We're wasting time milling around.
   PL:
1063. [Kwestia głosowa [battleentry_11113_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battleentry_11113_1].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1064. [Kwestia głosowa [battleentry_11113_1] (Stage Entry)] 징수 시간이다.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battleentry_11113_1].dlg
   limit: do 120 znaków
   EN: Collection time.
   PL:
1065. [Kwestia głosowa [battle_select_11113_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_select_11113_1].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1066. [Kwestia głosowa [battle_select_11113_1] (Viewed in Battle)] 가속중에는이야기해봐야잘들리지않는다.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_select_11113_1].dlg
   limit: do 120 znaków
   EN: <i>It'sHardToCommunicateWhenI'mInAcceleratedTime.</i>
   PL:
1067. [Kwestia głosowa [battle_endcommand_11113_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_endcommand_11113_1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1068. [Kwestia głosowa [battle_endcommand_11113_1] (Commencing Attack)] 정당한 공무 집행이다.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_endcommand_11113_1].dlg
   limit: do 120 znaków
   EN: This is a warranted execution of official duties.
   PL:
1069. [Kwestia głosowa [battle_enemy_break_11113_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_enemy_break_11113_1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1070. [Kwestia głosowa [battle_enemy_break_11113_1] (Enemy Stagger)] 벌써 버벅이나?
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_enemy_break_11113_1].dlg
   limit: do 120 znaków
   EN: Slowed to a crawl already?
   PL:
1071. [Kwestia głosowa [battle_break_11113_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_break_11113_1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1072. [Kwestia głosowa [battle_break_11113_1] (Staggered)] 크윽, 시간이…
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_break_11113_1].dlg
   limit: do 120 znaków
   EN: Hnngh... The time...
   PL:
1073. [Kwestia głosowa [battle_kill_11113_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_kill_11113_1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1074. [Kwestia głosowa [battle_kill_11113_1] (Enemy Killed)] 흠… 완전히 멈췄나. 체납한 시간은 전부 징수했으니, 상관 없지.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_kill_11113_1].dlg
   limit: do 120 znaków
   EN: Hmmm, came to a full stop, did you? No matter. Your time debt's been collected.
   PL:
1075. [Kwestia głosowa [battle_dead_11113_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_dead_11113_1].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1076. [Kwestia głosowa [battle_dead_11113_1] (Death)] 말도 안 되는… 일이… 아직 그 날을 위해 모아둔 시간을… 제대로 쓰지도…
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_dead_11113_1].dlg
   limit: do 120 znaków
   EN: Impossible... But... I saved up so much time... for that day... I never got... to...
   PL:
1077. [Kwestia głosowa [choice_success_p_11113_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=choice_success_p_11113_2].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1078. [Kwestia głosowa [choice_success_p_11113_2] (Check Passed)] 현명한 업무 명령이었다. 덕분에 시간을 아꼈으니, 감사를 표하지.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=choice_success_p_11113_2].dlg
   limit: do 120 znaków
   EN: You know how to work smart. I saved some time thanks to you.
   PL:
1079. [Kwestia głosowa [choice_fail_n_11113_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=choice_fail_n_11113_1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1080. [Kwestia głosowa [choice_fail_n_11113_1] (Check Failed)] 이런 일에 쓰는 시간이 제일 아깝군… 되감고 싶을 뿐이다.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=choice_fail_n_11113_1].dlg
   limit: do 120 znaków
   EN: What a waste of time... If only it could be rewound.
   PL:
1081. [Kwestia głosowa [battle_clear_11113_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_clear_11113_1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1082. [Kwestia głosowa [battle_clear_11113_1] (Victory Cry)] 필요한 시간은 전부 징수되었다. 아, 나는 또 다른 징수 임무가 있어서. 아, 이 말을 잊었군. 보고서는 맡기지. 아니, 여기 있네. 제대로 쓸 지 걱정하는 시간에 내가 쓰는게 낫겠다고 생각했다.
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_clear_11113_1].dlg
   limit: do 390 znaków
   EN: All necessary time has been collected. Ah, I'm off to my next collection. Oh, forgot to tell you this earlier, but I'll leave the report to you. No, never mind. Here's the report. I thought the time wasted worrying about whether you'd write a good report was better used for writing the report myself.
   PL:
1083. [Kwestia głosowa [battle_clear_ex_11113_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_clear_ex_11113_1].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1084. [Kwestia głosowa [battle_clear_ex_11113_1] (Extra Conditions Fulfilled)] 승자는 시간을 관리하며 살고, 패자는 시간에 질질 끌려가며 사는 법. 오늘 출근길 조간 신문에 있던 문구다. 훗, 참으로 시의적절하지 않나?
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_clear_ex_11113_1].dlg
   limit: do 270 znaków
   EN: Success is all about time management; winners wisely manage their time, while losers get pushed around by time. Read it in the morning paper I picked up on the way to work. I certainly lived up to it, didn't I?
   PL:
1085. [Kwestia głosowa [battle_defeat_11113_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_defeat_11113_1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1086. [Kwestia głosowa [battle_defeat_11113_1] (Defeat Wail)] 너희에게… 내일은 찾아오지 않을 거다… 4등급 미래절단직들이 오면… 그 내일은 반드시 찢겨나갈 테니까…!
   źródło: PersonalityVoiceDlg/Voice_Outis_TCorp_11113.json :: dataList[id=battle_defeat_11113_1].dlg
   limit: do 160 znaków
   EN: You... don't have a tomorrow... When the Class 4 Future Severance Unit arrives... they'll rip your tomorrows away...!
   PL:
