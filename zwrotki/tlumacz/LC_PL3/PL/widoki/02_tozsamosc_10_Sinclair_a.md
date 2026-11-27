# Grzesznik #10: Sinclair — Tożsamości, umiejętności, pasywki i głos (część a) — Limbus Company

Kompletny zestaw kart Tożsamości postaci **Sinclair** (싱클레어) wraz z umiejętnościami na ulepszeniach 1–4, efektami monet, pasywkami i kwestiami głosowymi.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Grzesznik #10: Sinclair (싱클레어)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 싱클레어
   źródło: Characters.json :: dataList[id=10].name
   limit: do 40 znaków
   EN: Sinclair
   PL:
2. [Akta więźnia — nazwa] 싱클레어
   źródło: IntroduceCharacter.json :: dataList[id=싱클레어].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
3. [Akta więźnia — opis] 불안정한 성장 시기적 특징을 감안하여도 말을 걸 때 유독 놀라거나 인상을\n구기는 행동이 두드러지는 수감자입니다. 전투에도 익숙하지 못하여\n처음에는 내장을 보는 것도 힘겨워할 것입니다. 수감자 중엔 폭력적인\n성향을 띄는 이도 있을 것이므로 관리자님은 본 수감자에게 채찍보다는\n당근을 건네는 것이 권장됩니다. 본인도 인지 못 하는 살기를 띠고\n있기도 합니다만, 우리 회사의 사업분야에 대한 잠재성이 있다는 뜻이므로\n적절한 자극만 주어진다면 훌륭히 성장할 것으로 기대합니다.
   źródło: IntroduceCharacter.json :: dataList[id=싱클레어].description
   limit: do 830 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Even with the volatile nature of human growth around his age taken into consideration,\nthis Sinner seems to get particularly startled or frown when spoken to.\nHe isn't used to real combat at the moment,\nmeaning that he may struggle to keep himself together at the sight of something as mild as spilt innards at first.\nAs there may be those with violent tendencies among your crew,\nwe recommend taking an approach focused on positive reinforcement with this Sinner.\nHe appears to possess a murderous gaze that he himself isn't aware of;\nthis is a hopeful sign that he has the potential to grow into an expert of our company's profession with the right stimuli.
   PL: Nawet biorąc poprawkę na burzliwy okres dorastania, Grzesznik wyróżnia się tym,\nże zagadnięty, wyjątkowo łatwo się wzdryga albo krzywi. Nie jest też obyty\nz walką, więc na początku może mu być ciężko nawet patrzeć na wnętrzności.\nWśród Grzeszników są osoby skłonne do przemocy, dlatego zalecamy,\nby Kierownik stosował wobec niego raczej marchewkę niż kij.\nBywa, że ma w oczach żądzę mordu, której sam nie jest świadom, co jednak\noznacza potencjał w dziedzinie działalności naszej firmy; przy odpowiednich bodźcach liczymy, że wyrośnie na znakomitego fachowca.

## [0] LCB Sinner — Sinclair — LCB 수감자
- ID Tożsamości: `11001` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 60 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Rupture

4. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=11001].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL:
5. [Karta Tożsamości — nazwa] 싱클레어
   źródło: Personalities.json :: dataList[id=11001].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — nazwa z tytułem] 싱클레어
   źródło: Personalities.json :: dataList[id=11001].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Karta Tożsamości — opis] 싱클레어의 첫번째 인격
   źródło: Personalities.json :: dataList[id=11001].desc
   limit: do 120 znaków
   EN: Sinclair’s 1st Identity
   PL:
8. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 내려베기
   źródło: Skills.json :: dataList[id=1100101].levelList[level=1].name ; dataList[id=1100101].levelList[level=2].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Downward Swing
   PL:
9. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1100101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL:
10. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1100101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL:
11. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 연속 베기
   źródło: Skills.json :: dataList[id=1100102].levelList[level=1].name ; dataList[id=1100102].levelList[level=2].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Halberd Combo
   PL:
12. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 피해량 +10%
   źródło: Skills.json :: dataList[id=1100102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] +10% damage
   PL:
13. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WinDuel] 피해량 +30%
   źródło: Skills.json :: dataList[id=1100102].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] +30% damage
   PL:
14. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 헤집어 베기
   źródło: Skills.json :: dataList[id=1100103].levelList[level=3].name ; dataList[id=1100103].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Ravaging Cut
   PL:
15. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] [WinDuel] 공격 위력 증가 1 얻음
   źródło: Skills.json :: dataList[id=1100103].levelList[level=3].desc ; dataList[id=1100103].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 1 Attack Power Up
   PL:
16. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1100103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Rupture
   PL:
17. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1100103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1100103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
19. [Obrona (ulepszenie 1) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1100104].levelList[level=1].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 7 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Counter
   PL:
20. [Pasywka bojowa (od ulepszenia 1, posiadane 3× Pride) — nazwa] 각오
   źródło: Passives.json :: dataList[id=1100101].name
   limit: do 40 znaków
   EN: Pluckiness
   PL:
21. [Pasywka bojowa (od ulepszenia 1, posiadane 3× Pride) — opis] 이번 턴에 아군이 사망하면 다음 턴에 공격 위력 증가 1을 얻음
   źródło: Passives.json :: dataList[id=1100101].desc
   limit: do 120 znaków
   EN: When an ally is defeated, gain 1 Attack Power Up next turn.
   PL:
22. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — nazwa] 앙심
   źródło: Passives.json :: dataList[id=1100121].name
   limit: do 40 znaków
   EN: Grudge
   PL:
23. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — opis] 정신력이 가장 낮은 아군 1명 다른 아군이 사망하면 다음 턴에 공격 위력 증가 1을 얻음
   źródło: Passives.json :: dataList[id=1100121].desc
   limit: do 120 znaków
   EN: 1 ally with the least SP gains 1 Attack Power Up the turn after an ally is defeated.
   PL:
24. [Kwestia głosowa [get_11001_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=get_11001_1].desc
   limit: do 120 znaków
   EN: Identity Acquisition
   PL:
25. [Kwestia głosowa [get_11001_1] (Identity Acquisition)] 싱클레어예요… 에밀, 싱클레어. 아, 번호는 음… 11번
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=get_11001_1].dlg
   limit: do 120 znaków
   EN: I’m Sinclair… Emil Sinclair. Oh, my number is, uhm… eleven.
   PL:
26. [Kwestia głosowa [lobby_morning_11001_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=lobby_morning_11001_1].desc
   limit: do 120 znaków
   EN: Morning Greeting
   PL:
27. [Kwestia głosowa [lobby_morning_11001_1] (Morning Greeting)] 좋은 아침이에요! 잘 주무셨… 아 관리자님도 잠들 수 있는 거… 맞죠?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=lobby_morning_11001_1].dlg
   limit: do 120 znaków
   EN: Good morning! Did you have a good… Oh, you can sleep, right, Manager…?
   PL:
28. [Kwestia głosowa [lobby_noon_11001_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=lobby_noon_11001_1].desc
   limit: do 120 znaków
   EN: Afternoon Greeting
   PL:
29. [Kwestia głosowa [lobby_noon_11001_1] (Afternoon Greeting)] 전 이 시간대가 제일 마음이 편해지더라구요. 오후도 힘내세요, 관리자님.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=lobby_noon_11001_1].dlg
   limit: do 120 znaków
   EN: I feel the most comfortable at this time of the day. Have a nice afternoon, Manager.
   PL:
30. [Kwestia głosowa [lobby_night_11001_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=lobby_night_11001_1].desc
   limit: do 120 znaków
   EN: Evening Greeting
   PL:
31. [Kwestia głosowa [lobby_night_11001_1] (Evening Greeting)] 오늘 하루는 어떠셨나요? 전… 오늘 제대로 집중하지 못한 것 같아요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=lobby_night_11001_1].dlg
   limit: do 120 znaków
   EN: How was your day? As for me… I couldn’t really focus on my tasks, I think.
   PL:
32. [Kwestia głosowa [smalltalk_11001_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=smalltalk_11001_1].desc
   limit: do 120 znaków
   EN: Chatter #1
   PL:
33. [Kwestia głosowa [smalltalk_11001_1] (Chatter #1)] 아마 예전 같았으면 상상도 못 했을 거예요… 아, 그러니까 지금 제가 하는 일이 마음에 안 든다는 건 아니고요… 그냥 신기해서요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=smalltalk_11001_1].dlg
   limit: do 200 znaków
   EN: I don’t think I could ever have imagined doing this… Oh, it’s not that I dislike my job or anything, it’s just… something that randomly occurred to me.
   PL:
34. [Kwestia głosowa [smalltalk_11001_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=smalltalk_11001_2].desc
   limit: do 120 znaków
   EN: Chatter #2
   PL:
35. [Kwestia głosowa [smalltalk_11001_2] (Chatter #2)] 관리자님은 대단한 것 같아요… 전 아직도 적응 못해서 쩔쩔매고 있는데 관리자님은 기억을 잃어도 능숙하게 저희를 이끌고 계시잖아요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=smalltalk_11001_2].dlg
   limit: do 160 znaków
   EN: You really are amazing, Manager… I’m still struggling to adjust, and you’re leading us like a pro despite your memory loss.
   PL:
36. [Kwestia głosowa [smalltalk_11001_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=smalltalk_11001_3].desc
   limit: do 120 znaków
   EN: Chatter #3
   PL:
37. [Kwestia głosowa [smalltalk_11001_3] (Chatter #3)] 이것 봐요. 로쟈 씨가 군것질거리를 주셨어요. 아껴 먹으려고요. 헤헤.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=smalltalk_11001_3].dlg
   limit: do 120 znaków
   EN: Look, Rodya gave me some snacks. I’m gonna save some for later. Hehe.
   PL:
38. [Kwestia głosowa [smalltalk_11001_4] — sytuacja] 대화 4
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=smalltalk_11001_4].desc
   limit: do 120 znaków
   EN: Chatter #4
   PL:
39. [Kwestia głosowa [smalltalk_11001_4] (Chatter #4)] 단테 씨… 정말 그 머리를 하고 있으면… 아무렇지 않아요? 세상은… 여전히 똑바로 보이는 건가요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=smalltalk_11001_4].dlg
   limit: do 140 znaków
   EN: Say, Dante… Do you… really feel nothing having that for your head? Is the world… still normal to you?
   PL:
40. [Kwestia głosowa [smalltalk_11001_5] — sytuacja] 대화 5
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=smalltalk_11001_5].desc
   limit: do 120 znaków
   EN: Chatter #5
   PL:
41. [Kwestia głosowa [smalltalk_11001_5] (Chatter #5)] 단테 씨, 기억이 없다면 후회도 없으시겠네요? 어쩌면 무례한 말일지도 모르지만… 부러워요. 오롯이 지금만 볼 수 있는 거잖아요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=smalltalk_11001_5].dlg
   limit: do 260 znaków
   EN: So, if you don’t remember your past, I guess that means you don’t have regrets either, right, Dante? It might be rude of me to say this, but… I envy that. You get to completely focus on the present.
   PL:
42. [Kwestia głosowa [neglect_11001_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=neglect_11001_1].desc
   limit: do 120 znaków
   EN: Idle
   PL:
43. [Kwestia głosowa [neglect_11001_1] (Idle)] 관리자님…? 어디 가셨어요? 바쁘신가요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=neglect_11001_1].dlg
   limit: do 120 znaków
   EN: Um, Manager…? Where are you? Are you busy?
   PL:
44. [Kwestia głosowa [formation_11001_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=formation_11001_1].desc
   limit: do 120 znaków
   EN: Deployment
   PL:
45. [Kwestia głosowa [formation_11001_1] (Deployment)] 어… 저를요? 으음… 최선은 다해볼게요…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=formation_11001_1].dlg
   limit: do 120 znaków
   EN: Umm… You want me? Mmh… I will do my best…
   PL:
46. [Kwestia głosowa [battleentry_11001_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battleentry_11001_1].desc
   limit: do 120 znaków
   EN: Stage Entry
   PL:
47. [Kwestia głosowa [battleentry_11001_1] (Stage Entry)] 이게 최선이겠죠…?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battleentry_11001_1].dlg
   limit: do 120 znaków
   EN: I guess this is for the best, right…?
   PL:
48. [Kwestia głosowa [battle_select_11001_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_select_11001_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle
   PL:
49. [Kwestia głosowa [battle_select_11001_1] (Viewed in Battle)] 제가 무슨 실수라도 했나요…?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_select_11001_1].dlg
   limit: do 120 znaków
   EN: Did I do something wrong…?
   PL:
50. [Kwestia głosowa [battle_endcommand_11001_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_endcommand_11001_1].desc
   limit: do 120 znaków
   EN: Commencing Attack
   PL:
51. [Kwestia głosowa [battle_endcommand_11001_1] (Commencing Attack)] 해보겠습니다…!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_endcommand_11001_1].dlg
   limit: do 120 znaków
   EN: I’ll try…!
   PL:
52. [Kwestia głosowa [battle_enemy_break_11001_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_enemy_break_11001_1].desc
   limit: do 120 znaków
   EN: Enemy Stagger
   PL:
53. [Kwestia głosowa [battle_enemy_break_11001_1] (Enemy Stagger)] 제가 해낸 것 맞죠…?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_enemy_break_11001_1].dlg
   limit: do 120 znaków
   EN: I did it, right…?
   PL:
54. [Kwestia głosowa [battle_break_11001_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_break_11001_1].desc
   limit: do 120 znaków
   EN: Staggered
   PL:
55. [Kwestia głosowa [battle_break_11001_1] (Staggered)] 읏…!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_break_11001_1].dlg
   limit: do 120 znaków
   EN: Ngh…!
   PL:
56. [Kwestia głosowa [battle_kill_11001_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_kill_11001_1].desc
   limit: do 120 znaków
   EN: Enemy Killed
   PL:
57. [Kwestia głosowa [battle_kill_11001_1] (Enemy Killed)] 해냈어요!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_kill_11001_1].dlg
   limit: do 120 znaków
   EN: I did it!
   PL:
58. [Kwestia głosowa [battle_allydead_11001_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_allydead_11001_1].desc
   limit: do 120 znaków
   EN: Ally Death
   PL:
59. [Kwestia głosowa [battle_allydead_11001_1] (Ally Death)] 나도 저렇게 되는 걸까…?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_allydead_11001_1].dlg
   limit: do 120 znaków
   EN: Will that happen to me too…?
   PL:
60. [Kwestia głosowa [choice_success_p_11001_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=choice_success_p_11001_1].desc
   limit: do 120 znaków
   EN: Check Passed
   PL:
61. [Kwestia głosowa [choice_success_p_11001_1] (Check Passed)] 다행이에요. 성공해서…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=choice_success_p_11001_1].dlg
   limit: do 120 znaków
   EN: Thank goodness I made it…
   PL:
62. [Kwestia głosowa [choice_fail_n_11001_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=choice_fail_n_11001_1].desc
   limit: do 120 znaków
   EN: Check Failed
   PL:
63. [Kwestia głosowa [choice_fail_n_11001_1] (Check Failed)] 다 제 잘못이에요…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=choice_fail_n_11001_1].dlg
   limit: do 120 znaków
   EN: It’s all my fault…
   PL:
64. [Kwestia głosowa [battle_clear_11001_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_clear_11001_1].desc
   limit: do 120 znaków
   EN: Victory Cry
   PL:
65. [Kwestia głosowa [battle_clear_11001_1] (Victory Cry)] 어… 저희가 해낸 거예요? 다행이에요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_clear_11001_1].dlg
   limit: do 120 znaków
   EN: Umm… Did we make it? I’m so relieved.
   PL:
66. [Kwestia głosowa [battle_clear_ex_11001_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_clear_ex_11001_1].desc
   limit: do 120 znaków
   EN: Extra Conditions Fulfilled
   PL:
67. [Kwestia głosowa [battle_clear_ex_11001_1] (Extra Conditions Fulfilled)] 제 덕은 아닐 거예요. 그래도 칭찬해주셔서 감사해요, 관리자님. 순간, 제 어머니가 생각났어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_clear_ex_11001_1].dlg
   limit: do 160 znaków
   EN: I don’t really think it’s thanks to me. I appreciate the compliment, though. I was reminded of my mother for a moment.
   PL:
68. [Kwestia głosowa [battle_defeat_11001_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_defeat_11001_1].desc
   limit: do 120 znaków
   EN: Defeat Wail
   PL:
69. [Kwestia głosowa [battle_defeat_11001_1] (Defeat Wail)] 죄송해요. 제가 조금 더 잘했어야 했는데… 아직 미숙한 게 많나 봐요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LCB_11001.json :: dataList[id=battle_defeat_11001_1].dlg
   limit: do 120 znaków
   EN: Sorry. I should have done better… I still have a lot of room for improvement.
   PL:

## [000] Blade Lineage Salsu — Sinclair — 검계 살수
- ID Tożsamości: `11002` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 86 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Poise, Bleed

70. [Karta Tożsamości — tytuł] 검계\n살수
   źródło: Personalities.json :: dataList[id=11002].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Blade Lineage\nSalsu
   PL:
71. [Karta Tożsamości — nazwa] 싱클레어
   źródło: Personalities.json :: dataList[id=11002].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Karta Tożsamości — nazwa z tytułem] 싱클레어
   źródło: Personalities.json :: dataList[id=11002].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [Karta Tożsamości — opis] 싱클레어의 두번째 인격
   źródło: Personalities.json :: dataList[id=11002].desc
   limit: do 120 znaków
   EN: Sinclair’s 2nd Identity
   PL:
74. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 참관
   źródło: Skills.json :: dataList[id=1100201].levelList[level=1].name ; dataList[id=1100201].levelList[level=2].name ; dataList[id=1100201].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 5 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Slice then Stab
   PL:
75. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1100201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain +1 [Breath] Count
   PL:
76. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1100201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1100201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL:
77. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 호흡 횟수가 3 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1100201].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: If at 3+ [Breath] Count, Coin Power +1
   PL:
78. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 연참
   źródło: Skills.json :: dataList[id=1100202].levelList[level=1].name ; dataList[id=1100202].levelList[level=2].name ; dataList[id=1100202].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 6 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Slash Series
   PL:
79. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1100202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath]
   PL:
80. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1100202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath]
   PL:
81. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1100202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [DefeatDuel] 다음 턴에 공격 위력 증가 2 얻음
   źródło: Skills.json :: dataList[id=1100202].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Gain 2 Attack Power Up next turn
   PL:
83. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1100202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1100202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
84. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1100202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1100202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL:
85. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1100202].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1100202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [DefeatDuel] 다음 턴에 공격 위력 증가 2 얻음\n[WinDuel] 이번 스킬의 크리티컬 공격으로 호흡 횟수를 소모하지 않음
   źródło: Skills.json :: dataList[id=1100202].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel], [WinDuel], [Breath]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [DefeatDuel] Gain 2 Attack Power Up next turn\n[WinDuel] Do not spend [Breath] Count with critical attacks landed with this skill
   PL:
87. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 골단
   źródło: Skills.json :: dataList[id=1100203].levelList[level=3].name ; dataList[id=1100203].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 8 · monety: 1 (+18)
   limit: do 40 znaków
   EN: To Claim Their Bones
   PL:
88. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마비 5 부여
   źródło: Skills.json :: dataList[id=1100203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1100203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Paralyze
   PL:
89. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills.json :: dataList[id=1100203].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1100203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL:
90. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 호흡 횟수가 10 이상이면, 크리티컬 피해량 +150%
   źródło: Skills.json :: dataList[id=1100203].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 10+ [Breath] Count, +150% Critical Damage
   PL:
91. [Obrona (ulepszenia 1,4) — nazwa] 반격 - 초생
   źródło: Skills.json :: dataList[id=1100204].levelList[level=1].name ; dataList[id=1100204].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 9 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Newsprung Counter
   PL:
92. [Obrona (ulepszenie 1) — opis] [WhenUse] 다음 턴에 피해량 증가 1 얻음
   źródło: Skills.json :: dataList[id=1100204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Damage Up next turn
   PL:
93. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 피해량 증가 1 얻음\n[WhenUse] 호흡 횟수 3 증가
   źródło: Skills.json :: dataList[id=1100204].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 1 Damage Up next turn\n[WhenUse] Gain +3 [Breath] Count
   PL:
94. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Pride) — nazwa] 살수
   źródło: Passives.json :: dataList[id=1100201].name
   limit: do 40 znaków
   EN: Slayer
   PL:
95. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Pride) — opis] 연결한 죄 중 마지막 죄의 마지막 코인의 피해량 +20%
   źródło: Passives.json :: dataList[id=1100201].desc
   limit: do 120 znaków
   EN: The last Coin on the last skill in the chain deals +20% damage.
   PL:
96. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — nazwa] 피 묻힌 손
   źródło: Passives.json :: dataList[id=1100221].name
   limit: do 40 znaków
   EN: Bloodied Hands
   PL:
97. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — opis] 속도가 가장 낮은 아군 1명 마지막 스킬의 최종 위력 +1
   źródło: Passives.json :: dataList[id=1100221].desc
   limit: do 120 znaków
   EN: 1 ally with the slowest Speed gains +1 final Power for their last skill.
   PL:
98. [Kwestia głosowa [get_11002_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=get_11002_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Kwestia głosowa [get_11002_1] (Identity Acquisition)] 제가… 무엇을 베면 되는 거죠?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=get_11002_1].dlg
   limit: do 120 znaków
   EN: Tell me… What do I need to cut?
   PL:
100. [Kwestia głosowa [lobby_morning_11002_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=lobby_morning_11002_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Kwestia głosowa [lobby_morning_11002_1] (Morning Greeting)] 아침 공기를 맞으면서 칼을 휘두를 때가 제일 상쾌하죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=lobby_morning_11002_1].dlg
   limit: do 120 znaków
   EN: There’s nothing refreshing like swinging my sword through the morning air.
   PL:
102. [Kwestia głosowa [lobby_noon_11002_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=lobby_noon_11002_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Kwestia głosowa [lobby_noon_11002_1] (Afternoon Greeting)] 관리자님은 점심을 누구랑 드시나요? 어… 저는 보통 혼자 먹어요. 그게 편하더라고요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=lobby_noon_11002_1].dlg
   limit: do 150 znaków
   EN: Manager, who do you usually have your lunch with? Um… As for me, I tend to eat alone. I’m more comfortable that way.
   PL:
104. [Kwestia głosowa [lobby_night_11002_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=lobby_night_11002_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [Kwestia głosowa [lobby_night_11002_1] (Evening Greeting)] 어둡네요. 달을 베어낼 수 있다면 하늘이 더 밝아질 텐데. …아 농담이에요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=lobby_night_11002_1].dlg
   limit: do 130 znaków
   EN: It’s dark out. The sky would be brighter if I could cut out the moon. …I’m kidding, of course.
   PL:
106. [Kwestia głosowa [smalltalk_11002_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=smalltalk_11002_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Kwestia głosowa [smalltalk_11002_1] (Chatter #1)] 관리자님은 지금 하고 있는 일에 만족하나요? 보람을 느끼시나요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=smalltalk_11002_1].dlg
   limit: do 120 znaków
   EN: Are you satisfied with what you’re doing, Manager? Is your job fulfilling?
   PL:
108. [Kwestia głosowa [smalltalk_11002_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=smalltalk_11002_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Kwestia głosowa [smalltalk_11002_2] (Chatter #2)] 아, 관리자님! 경계를 서고 있는 중이었어요. 같이요…? 음… 네! 그래요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=smalltalk_11002_2].dlg
   limit: do 120 znaków
   EN: Oh, hi, Manager! I was just standing guard. You’ll join me…? Mmm… Sure! Go ahead.
   PL:
110. [Kwestia głosowa [smalltalk_11002_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=smalltalk_11002_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [Kwestia głosowa [smalltalk_11002_3] (Chatter #3)] 로쟈 씨가 부러워요. 뭐든 깊게 생각 안 하시고 마음 가는 대로 하시잖아요. 전 그게 옛날부터 안됐어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=smalltalk_11002_3].dlg
   limit: do 160 znaków
   EN: I envy Ms. Rodya. She never thinks too deeply and has no problem following her heart. It’s something I could never do.
   PL:
112. [Kwestia głosowa [smalltalk_11002_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=smalltalk_11002_4].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 1
   PL:
113. [Kwestia głosowa [smalltalk_11002_4] (Post-Uptie Chat 1)] 검을 쓸 땐 어떤 망설임도 없어야 한대요. 하지만 전 끊임없이 되물어요… 누군가의 목숨을 그렇게 쉽게 베어내도 괜찮은지…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=smalltalk_11002_4].dlg
   limit: do 230 znaków
   EN: I was taught that you should show no hesitation when you wield a sword. But I can’t help but keep questioning myself… asking if it’s really okay to take others’ lives so easily…
   PL:
114. [Kwestia głosowa [smalltalk_11002_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=smalltalk_11002_5].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 2
   PL:
115. [Kwestia głosowa [smalltalk_11002_5] (Post-Uptie Chat 2)] 하지만 막상 사람을 베어낼 땐… 저도 모르게 희열을 느끼곤 했어요. 이게 저 라는 사람의 본질이었나 봐요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=smalltalk_11002_5].dlg
   limit: do 130 znaków
   EN: However, when I actually cut someone down… I would get such a rush. I guess that’s my nature.
   PL:
116. [Kwestia głosowa [neglect_11002_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=neglect_11002_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Kwestia głosowa [neglect_11002_1] (Idle)] 어? 관리자님 어디 가셨지? 혹시 새로운 장난 같은 건가요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=neglect_11002_1].dlg
   limit: do 120 znaków
   EN: Huh? Manager, where did you go? Is this some kind of prank?
   PL:
118. [Kwestia głosowa [gacksung_11002_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=gacksung_11002_1].desc
   limit: do 120 znaków
   EN: Uptying
   PL:
119. [Kwestia głosowa [gacksung_11002_1] (Uptying)] 더 날카로운 검이 되겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=gacksung_11002_1].dlg
   limit: do 120 znaków
   EN: I’ll become a sharper blade.
   PL:
120. [Kwestia głosowa [formation_11002_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=formation_11002_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Kwestia głosowa [formation_11002_1] (Deployment)] 망설임 없이.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=formation_11002_1].dlg
   limit: do 120 znaków
   EN: Without hesitation.
   PL:
122. [Kwestia głosowa [battleentry_11002_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battleentry_11002_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Kwestia głosowa [battleentry_11002_1] (Stage Entry)] 벼릴 수 있는 기회겠죠…?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battleentry_11002_1].dlg
   limit: do 120 znaków
   EN: This will help me hone my edge, right…?
   PL:
124. [Kwestia głosowa [battle_select_11002_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_select_11002_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Kwestia głosowa [battle_select_11002_1] (Viewed in Battle)] 제 검을 믿어주세요…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_select_11002_1].dlg
   limit: do 120 znaków
   EN: Please trust my blade…
   PL:
126. [Kwestia głosowa [battle_endcommand_11002_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_endcommand_11002_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Kwestia głosowa [battle_endcommand_11002_1] (Commencing Attack)] 망설임이 없도록…!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_endcommand_11002_1].dlg
   limit: do 120 znaków
   EN: I won’t hesitate…!
   PL:
128. [Kwestia głosowa [battle_enemy_break_11002_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_enemy_break_11002_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Kwestia głosowa [battle_enemy_break_11002_1] (Enemy Stagger)] 다음번에는 벨 수 있겠죠?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_enemy_break_11002_1].dlg
   limit: do 120 znaków
   EN: I’ll be able to cut them down next, right?
   PL:
130. [Kwestia głosowa [battle_break_11002_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_break_11002_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Kwestia głosowa [battle_break_11002_1] (Staggered)] 으…!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_break_11002_1].dlg
   limit: do 120 znaków
   EN: Hng…!
   PL:
132. [Kwestia głosowa [battle_kill_11002_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_kill_11002_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Kwestia głosowa [battle_kill_11002_1] (Enemy Killed)] 베어냈어요!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_kill_11002_1].dlg
   limit: do 120 znaków
   EN: I slew them!
   PL:
134. [Kwestia głosowa [battle_allydead_11002_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_allydead_11002_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Kwestia głosowa [battle_allydead_11002_1] (Ally Death)] 이런 장난은 싫어…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_allydead_11002_1].dlg
   limit: do 120 znaków
   EN: Don’t joke with me like this…
   PL:
136. [Kwestia głosowa [choice_success_p_11002_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=choice_success_p_11002_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Kwestia głosowa [choice_success_p_11002_1] (Check Passed)] 단테 씨는 망설임이 없군요!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=choice_success_p_11002_1].dlg
   limit: do 120 znaków
   EN: You have no hesitation!
   PL:
138. [Kwestia głosowa [choice_fail_n_11002_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=choice_fail_n_11002_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Kwestia głosowa [choice_fail_n_11002_1] (Check Failed)] 생각지도 못한 일이에요…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=choice_fail_n_11002_1].dlg
   limit: do 120 znaków
   EN: This was inconceivable…
   PL:
140. [Kwestia głosowa [battle_clear_11002_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_clear_11002_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Kwestia głosowa [battle_clear_11002_1] (Victory Cry)] 조금 불안했는데… 무사히 끝나게 되어서 다행이에요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_clear_11002_1].dlg
   limit: do 120 znaków
   EN: I was a little nervous… but it’s nice to see that it ended well.
   PL:
142. [Kwestia głosowa [battle_clear_ex_11002_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_clear_ex_11002_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Kwestia głosowa [battle_clear_ex_11002_1] (Extra Conditions Fulfilled)] 누군가를 베는 건… 생각보다 희열이 느껴지는 일이었군요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_clear_ex_11002_1].dlg
   limit: do 120 znaków
   EN: To slay others… was more delightful than I thought.
   PL:
144. [Kwestia głosowa [battle_defeat_11002_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_defeat_11002_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Kwestia głosowa [battle_defeat_11002_1] (Defeat Wail)] 결정적인 순간에 망설였어요. 제 탓이에요…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_SwordGroup_11002.json :: dataList[id=battle_defeat_11002_1].dlg
   limit: do 120 znaków
   EN: I let my reluctance hold me back when it mattered most. It’s my fault.
   PL:

## [00] Zwei Assoc. South Section 6 — Sinclair — 남부 츠바이 협회 6과
- ID Tożsamości: `11003` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 88 · szybkość: 1–3 / 2–3 / 2–4 / 2–4
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor

146. [Karta Tożsamości — tytuł] 남부 츠바이 협회\n6과
   źródło: Personalities.json :: dataList[id=11003].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Zwei Assoc.\nSouth Section 6
   PL:
147. [Karta Tożsamości — nazwa] 싱클레어
   źródło: Personalities.json :: dataList[id=11003].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Karta Tożsamości — nazwa z tytułem] 싱클레어
   źródło: Personalities.json :: dataList[id=11003].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Karta Tożsamości — opis] 싱클레어의 세번째 인격
   źródło: Personalities.json :: dataList[id=11003].desc
   limit: do 120 znaków
   EN: Sinclair’s 3rd Identity
   PL:
150. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 타격
   źródło: Skills.json :: dataList[id=1100301].levelList[level=1].name ; dataList[id=1100301].levelList[level=2].name ; dataList[id=1100301].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Baton
   PL:
151. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills.json :: dataList[id=1100301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 2 [Vibration]
   PL:
152. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills.json :: dataList[id=1100301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1100301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
153. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [DefeatDuel] 보호 2를 얻음
   źródło: Skills.json :: dataList[id=1100301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Gain 2 Protection
   PL:
154. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 제압
   źródło: Skills.json :: dataList[id=1100302].levelList[level=1].name ; dataList[id=1100302].levelList[level=2].name ; dataList[id=1100302].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 6 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Suppress
   PL:
155. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 3 부여
   źródło: Skills.json :: dataList[id=1100302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 3 [Vibration]
   PL:
156. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 피해량 감소 1 부여
   źródło: Skills.json :: dataList[id=1100302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Damage Down next turn
   PL:
157. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 6 부여
   źródło: Skills.json :: dataList[id=1100302].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1100302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 6 [Vibration]
   PL:
158. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 피해량 감소 2 부여
   źródło: Skills.json :: dataList[id=1100302].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1100302].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Damage Down next turn
   PL:
159. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n[DefeatDuel] 진동 6 부여
   źródło: Skills.json :: dataList[id=1100302].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn\n[DefeatDuel] Inflict 6 [Vibration]
   PL:
160. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 강타
   źródło: Skills.json :: dataList[id=1100303].levelList[level=3].name ; dataList[id=1100303].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 7 · monety: 1 (+13)
   limit: do 40 znaków
   EN: Strong Strike
   PL:
161. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 다음 턴에 현재 체력이 가장 낮은 아군에게 보호 1 부여
   źródło: Skills.json :: dataList[id=1100303].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Give 1 Protection to the ally with the least HP next turn
   PL:
162. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills.json :: dataList[id=1100303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1100303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL:
163. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 타격 취약 2 부여
   źródło: Skills.json :: dataList[id=1100303].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Blunt Fragility
   PL:
164. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 현재 체력이 가장 낮은 아군에게 보호 1 부여\n[WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 10 증가
   źródło: Skills.json :: dataList[id=1100303].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Give 1 Protection to the ally with the least HP next turn\n[WhenUse] Gain +10 Aggro to this Skill Slot next turn
   PL:
165. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion] 시 대상의 진동 이 5 이상이면, 다음 턴에 보호 2 얻음
   źródło: Skills.json :: dataList[id=1100303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If target has 5+ [Vibration] upon [VibrationExplosion], gain 2 Protection next turn
   PL:
166. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 타격 취약 2 부여
   źródło: Skills.json :: dataList[id=1100303].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1100304].levelList[level=1].name ; dataList[id=1100304].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Guard
   PL:
168. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가
   źródło: Skills.json :: dataList[id=1100304].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn
   PL:
169. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Gloom) — nazwa] 당신의 방패
   źródło: Passives.json :: dataList[id=1100301].name
   limit: do 40 znaków
   EN: Your Shield
   PL:
170. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Gloom) — opis] 전투 시작 시 조작 패널에서 자신의 양 옆에 있는 캐릭터에게 이번 턴에 수비 위력 증가 2, 보호 1 부여
   źródło: Passives.json :: dataList[id=1100301].desc
   limit: do 170 znaków
   EN: At the start of the combat phase, apply 2 Defense Power Up and 1 Protection to allies adjacent to this unit on the Dashboard.
   PL:
171. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — nazwa] 뚝심
   źródło: Passives.json :: dataList[id=1100321].name
   limit: do 40 znaków
   EN: Stubbornness
   PL:
172. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — opis] 현재 체력이 가장 낮은 아군 1명 받는 피해량 -10%
   źródło: Passives.json :: dataList[id=1100321].desc
   limit: do 120 znaków
   EN: 1 ally with the least HP takes -10% damage.
   PL:
173. [Kwestia głosowa [get_11003_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=get_11003_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Kwestia głosowa [get_11003_1] (Identity Acquisition)] 관리자님, 최선을 다해 지켜드릴게요! 어어… 너무 앞에 서시진 마시고…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=get_11003_1].dlg
   limit: do 120 znaków
   EN: I’ll protect you with all I can, Manager! Oh, um… Don’t go too far ahead…
   PL:
175. [Kwestia głosowa [lobby_morning_11003_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=lobby_morning_11003_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Kwestia głosowa [lobby_morning_11003_1] (Morning Greeting)] 잠은 푹 주무셨나요? 네? 왜 이렇게 일찍 일어났냐고요? 원래 츠바이는 항상 그래요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=lobby_morning_11003_1].dlg
   limit: do 160 znaków
   EN: Have you had a good night’s sleep? Sorry? Oh, you’re wondering why I’m up so early? That’s just what the Zwei are like.
   PL:
177. [Kwestia głosowa [lobby_noon_11003_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=lobby_noon_11003_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Kwestia głosowa [lobby_noon_11003_1] (Afternoon Greeting)] 점심시간이네요. 전 주로 들고 먹기 편한 음식을 먹곤 해요. 훈련 때 먹던 게 버릇이 되었나 봐요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=lobby_noon_11003_1].dlg
   limit: do 150 znaków
   EN: It’s lunchtime. I usually have food that’s easy to carry around. I guess I’ve grown a habit from my training days.
   PL:
179. [Kwestia głosowa [lobby_night_11003_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=lobby_night_11003_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Kwestia głosowa [lobby_night_11003_1] (Evening Greeting)] 밤에는 눈을 항상 크게 뜨고 있어야 해요. 언제 급습이 일어날지 모르니까요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=lobby_night_11003_1].dlg
   limit: do 120 znaków
   EN: I should stay wide awake at night. You never know when an ambush might happen.
   PL:
181. [Kwestia głosowa [smalltalk_11003_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=smalltalk_11003_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Kwestia głosowa [smalltalk_11003_1] (Chatter #1)] 비록 제가 적에게 일격을 가할 수는 없을지라도… 대신 맞아드릴 수는 있어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=smalltalk_11003_1].dlg
   limit: do 120 znaków
   EN: Even if I can’t land a devastating blow… I can take one for you.
   PL:
183. [Kwestia głosowa [smalltalk_11003_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=smalltalk_11003_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Kwestia głosowa [smalltalk_11003_2] (Chatter #2)] 윽, 깜짝 놀랐어요…! 죄송해요, 몰래 다가오는 건 별로 좋아하지 않아서요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=smalltalk_11003_2].dlg
   limit: do 120 znaków
   EN: Wagh, you startled me…! Sorry, I just don’t really like being snuck up on.
   PL:
185. [Kwestia głosowa [smalltalk_11003_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=smalltalk_11003_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Kwestia głosowa [smalltalk_11003_3] (Chatter #3)] 처음에 돈키호테 씨랑 합동 훈련을 할 땐 조금 난감했는데… 지금은 돌발 행동에 많이 익숙해졌어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=smalltalk_11003_3].dlg
   limit: do 170 znaków
   EN: When I first started joint training with Don Quixote, it was rather troubling… But now, I’ve gotten quite used to her antics.
   PL:
187. [Kwestia głosowa [smalltalk_11003_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=smalltalk_11003_4].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Kwestia głosowa [smalltalk_11003_4] (Post-Uptie Chat 1)] 예전에는… 방법을 몰라서 소중한 사람들을 많이 잃었어요. 그래서 전 절박함을 알아요. 그래서 최선을 다할 수 있는 거예요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=smalltalk_11003_4].dlg
   limit: do 200 znaków
   EN: In the past… I’d lost many precious people because I didn’t know what to do. That experience taught me desperation. It’s what drives me to do my best now.
   PL:
189. [Kwestia głosowa [smalltalk_11003_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=smalltalk_11003_5].desc
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Kwestia głosowa [smalltalk_11003_5] (Post-Uptie Chat 2)] 도망갈 바에야 차라리 부서진 방패가 될 거예요. …더 이상 아무것도 잃고 싶지 않으니까요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=smalltalk_11003_5].dlg
   limit: do 120 znaków
   EN: I’d rather be a broken shield than a runaway. …I don’t want to suffer losing anyone else.
   PL:
191. [Kwestia głosowa [neglect_11003_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=neglect_11003_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Kwestia głosowa [neglect_11003_1] (Idle)] 관리자님.…? 앞으로는 사라질 때 꼭 저한테 말씀해주세요… 걱정된단 말이에요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=neglect_11003_1].dlg
   limit: do 120 znaków
   EN: Manager…? Please let me know in advance if you plan to go somewhere… I’m worried sick.
   PL:
193. [Kwestia głosowa [gacksung_11003_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=gacksung_11003_1].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Kwestia głosowa [gacksung_11003_1] (Uptying)] 지금보다 더 열심히 할게요! 실망시키지 않을 거에요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=gacksung_11003_1].dlg
   limit: do 120 znaków
   EN: I’ll work even harder! I’ll be sure to not let you down.
   PL:
195. [Kwestia głosowa [formation_11003_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=formation_11003_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Kwestia głosowa [formation_11003_1] (Deployment)] 뒷걸음질 치지 않는 방패가 되어.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=formation_11003_1].dlg
   limit: do 120 znaków
   EN: To be an unyielding shield.
   PL:
197. [Kwestia głosowa [battleentry_11003_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battleentry_11003_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Kwestia głosowa [battleentry_11003_1] (Stage Entry)] 최선을 다해 지켜낼게요!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battleentry_11003_1].dlg
   limit: do 120 znaków
   EN: I’ll protect you with all my strength!
   PL:
199. [Kwestia głosowa [battle_select_11003_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_select_11003_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Kwestia głosowa [battle_select_11003_1] (Viewed in Battle)] 최선을 다해 지켜 보이겠습니다!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_select_11003_1].dlg
   limit: do 120 znaków
   EN: I’ll try my best to keep the others safe!
   PL:
201. [Kwestia głosowa [battle_endcommand_11003_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_endcommand_11003_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Kwestia głosowa [battle_endcommand_11003_1] (Commencing Attack)] 따라와 주세요!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_endcommand_11003_1].dlg
   limit: do 120 znaków
   EN: This way!
   PL:
203. [Kwestia głosowa [battle_enemy_break_11003_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_enemy_break_11003_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Kwestia głosowa [battle_enemy_break_11003_1] (Enemy Stagger)] 지금이 기회에요!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_enemy_break_11003_1].dlg
   limit: do 120 znaków
   EN: Now’s our chance!
   PL:
205. [Kwestia głosowa [battle_break_11003_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_break_11003_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Kwestia głosowa [battle_break_11003_1] (Staggered)] 앗!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_break_11003_1].dlg
   limit: do 120 znaków
   EN: Ah!
   PL:
207. [Kwestia głosowa [battle_kill_11003_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_kill_11003_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Kwestia głosowa [battle_kill_11003_1] (Enemy Killed)] 지켜냈어!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_kill_11003_1].dlg
   limit: do 120 znaków
   EN: I did it!
   PL:
209. [Kwestia głosowa [battle_allydead_11003_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_allydead_11003_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Kwestia głosowa [battle_allydead_11003_1] (Ally Death)] 끝내 지켜내지 못했어…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_allydead_11003_1].dlg
   limit: do 120 znaków
   EN: I couldn’t protect you…
   PL:
211. [Kwestia głosowa [choice_success_p_11003_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=choice_success_p_11003_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Kwestia głosowa [choice_success_p_11003_1] (Check Passed)] 저를 믿어주셔서 감사해요!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=choice_success_p_11003_1].dlg
   limit: do 120 znaków
   EN: Thank you for having faith in me!
   PL:
213. [Kwestia głosowa [choice_fail_n_11003_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=choice_fail_n_11003_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Kwestia głosowa [choice_fail_n_11003_1] (Check Failed)] 지켜내지 못했어…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=choice_fail_n_11003_1].dlg
   limit: do 120 znaków
   EN: I couldn’t keep harm away…
   PL:
215. [Kwestia głosowa [battle_clear_11003_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_clear_11003_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Kwestia głosowa [battle_clear_11003_1] (Victory Cry)] 저도 이제 무언가를 제대로 지켜 내가고 있는 것 같아요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_clear_11003_1].dlg
   limit: do 120 znaków
   EN: I think I’m on the way to becoming a proper guardian.
   PL:
217. [Kwestia głosowa [battle_clear_ex_11003_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_clear_ex_11003_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Kwestia głosowa [battle_clear_ex_11003_1] (Extra Conditions Fulfilled)] 저 진짜 열심히 했어요, 인정받은 것 같아서 기뻐요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_clear_ex_11003_1].dlg
   limit: do 120 znaków
   EN: I gave it my all, and I’m glad my effort paid off.
   PL:
219. [Kwestia głosowa [battle_defeat_11003_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_defeat_11003_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Kwestia głosowa [battle_defeat_11003_1] (Defeat Wail)] 제대로 못 지켜냈네요. 이번엔 다를 줄 알았는데…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Zwei_11003.json :: dataList[id=battle_defeat_11003_1].dlg
   limit: do 120 znaków
   EN: I couldn’t protect the others. I thought things would be different this time…
   PL:

## [00] Los Mariachis Jefe — Sinclair — 마리아치 보스
- ID Tożsamości: `11004` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 1 · HP bazowe: 95 · szybkość: 1–2 / 1–2 / 2–3 / 2–3
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Poise, Sinking

221. [Karta Tożsamości — tytuł] 마리아치\n보스
   źródło: Personalities.json :: dataList[id=11004].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Los Mariachis\nJefe
   PL:
222. [Karta Tożsamości — nazwa] 싱클레어
   źródło: Personalities.json :: dataList[id=11004].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Karta Tożsamości — nazwa z tytułem] 싱클레어
   źródło: Personalities.json :: dataList[id=11004].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [Karta Tożsamości — opis] 싱클레어의 네번째 인격
   źródło: Personalities.json :: dataList[id=11004].desc
   limit: do 120 znaków
   EN: Sinclair’s 4th Identity
   PL:
225. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 춤사위
   źródło: Skills.json :: dataList[id=1100401].levelList[level=1].name ; dataList[id=1100401].levelList[level=2].name ; dataList[id=1100401].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Baile y Rola
   PL:
226. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1100401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 2 [Sinking]
   PL:
227. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 4 부여
   źródło: Skills.json :: dataList[id=1100401].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 4 [Sinking]
   PL:
228. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Sinking]이 4 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1100401].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: If target has 4+ [Sinking], Coin Power +1
   PL:
229. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 4 부여
   źródło: Skills.json :: dataList[id=1100401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL:
230. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 격정의 춤
   źródło: Skills.json :: dataList[id=1100402].levelList[level=1].name ; dataList[id=1100402].levelList[level=2].name ; dataList[id=1100402].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 5 · monety: 3 (+1)
   limit: do 40 znaków
   EN: Danza de Pasión
   PL:
231. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1100402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1100402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1100402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1100402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL:
233. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1100402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1100402].levelList[level=2].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1100402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1100402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL:
236. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1100402].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +1 [Sinking] Count
   PL:
237. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1100402].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1100402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Sinking]이 6 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1100402].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: If target has 6+ [Sinking], Coin Power +2
   PL:
239. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1100402].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL:
240. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1100402].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count
   PL:
241. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 파냐타 파티
   źródło: Skills.json :: dataList[id=1100403].levelList[level=3].name ; dataList[id=1100403].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 8 · monety: 1 (+11)
   limit: do 40 znaków
   EN: Pañata Party
   PL:
242. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 정신력이 0미만이면 대상의 정신력에 비례하여 크리티컬 발동 확률 증가
   źródło: Skills.json :: dataList[id=1100403].levelList[level=3].desc
   limit: do 120 znaków
   EN: If target’s SP is below 0, boost crit chance proportional to target’s SP
   PL:
243. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 피해량의 50%만큼 흐트러짐 회복
   źródło: Skills.json :: dataList[id=1100403].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Lower user’s Stagger Threshold by 50% of damage dealt
   PL:
244. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 정신력이 0미만이면 대상의 정신력에 비례하여 크리티컬 발동 확률 증가\n자신의 호흡 횟수가 5 이상이면, 크리티컬 피해량 +30%
   źródło: Skills.json :: dataList[id=1100403].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: If target's SP is below 0, boost crit chance proportional to target's SP\nIf user has 5+ [Breath] Count, +30% Critical Damage
   PL:
245. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 흐트러짐 회복
   źródło: Skills.json :: dataList[id=1100403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user’s Stagger Threshold by 50% of damage dealt
   PL:
246. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1100404].levelList[level=1].name ; dataList[id=1100404].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 5 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL:
247. [Obrona (ulepszenie 4) — opis] [OnSucceedEvade] 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1100404].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Breath]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [OnSucceedEvade] Gain +1 [Breath] Count
   PL:
248. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — nazwa] 유흥
   źródło: Passives.json :: dataList[id=1100401].name
   limit: do 40 znaków
   EN: Júbilo Hedonista
   PL:
249. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — opis] 회피 성공 시 (우울 공명 수 x5)% 확률로 회피 스킬의 위력만큼 흐트러짐 회복
   źródło: Passives.json :: dataList[id=1100401].desc
   limit: do 140 znaków
   EN: After a successful evade, lower Stagger Threshold by the evade skill’s Power at a (5x Gloom Reson.)% chance.
   PL:
250. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — nazwa] 농락
   źródło: Passives.json :: dataList[id=1100421].name
   limit: do 40 znaków
   EN: Jugar con Enemigos
   PL:
251. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — opis] 정신력이 가장 높은 아군 1명 자신보다 정신력이 낮은 적 공격 시 피해량 +10%
   źródło: Passives.json :: dataList[id=1100421].desc
   limit: do 120 znaków
   EN: 1 ally with the most SP deals +10% damage to enemies with lower SP.
   PL:
252. [Kwestia głosowa [get_11004_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=get_11004_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Kwestia głosowa [get_11004_1] (Identity Acquisition)] 안녕하세요… 제 흥을 돋구게 될 곳이 여기라고… 들었어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=get_11004_1].dlg
   limit: do 120 znaków
   EN: Salutations… I’ve been told that this is… where I’ll stir with entertainment.
   PL:
254. [Kwestia głosowa [lobby_morning_11004_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=lobby_morning_11004_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Kwestia głosowa [lobby_morning_11004_1] (Morning Greeting)] 상쾌한 아침이네요. 오늘 하루도 흥이 넘치게 시작해보자고요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=lobby_morning_11004_1].dlg
   limit: do 120 znaków
   EN: A fresh morning. Let’s kick off today with an energetic start.
   PL:
256. [Kwestia głosowa [lobby_noon_11004_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=lobby_noon_11004_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Kwestia głosowa [lobby_noon_11004_1] (Afternoon Greeting)] 나른하네요… 이럴 땐 양손으로 악기를 흔들어주면서 리듬을 타곤 해요. 이렇게, 이렇게.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=lobby_noon_11004_1].dlg
   limit: do 170 znaków
   EN: What a lazy afternoon… When I feel drowsy, I tend to shake the instruments in my hands to whatever rhythm. Like this, and like that.
   PL:
258. [Kwestia głosowa [lobby_night_11004_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=lobby_night_11004_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Kwestia głosowa [lobby_night_11004_1] (Evening Greeting)] 망자들이 좋아하는 시간이죠… 단테 씨는 언제 주무시나요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=lobby_night_11004_1].dlg
   limit: do 120 znaków
   EN: The favorite hours of the dead… When do you go to sleep, Dante?
   PL:
260. [Kwestia głosowa [smalltalk_11004_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=smalltalk_11004_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Kwestia głosowa [smalltalk_11004_1] (Chatter #1)] 아… 제 음악을 듣고 싶으신가요? 음… 정말 원하신다면 한 곡 연주해드릴게요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=smalltalk_11004_1].dlg
   limit: do 120 znaków
   EN: Oh… You wanna hear my music? Hmm… I’ll shake something out, if you insist.
   PL:
262. [Kwestia głosowa [smalltalk_11004_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=smalltalk_11004_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Kwestia głosowa [smalltalk_11004_2] (Chatter #2)] 싸울 때는 언제나 생각을 비워놔야 해요. 중요한 건 리듬이죠. 유쾌하지만, 실수 없이.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=smalltalk_11004_2].dlg
   limit: do 150 znaków
   EN: You should keep your head empty in a fight. It’s all about the rhythm. Stay lively, but without missing a beat.
   PL:
264. [Kwestia głosowa [smalltalk_11004_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=smalltalk_11004_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Kwestia głosowa [smalltalk_11004_3] (Chatter #3)] 관리자님은 마음이 복잡할 땐 무엇을 하시나요? 저와 함께 악기를 배워 보는 건 어때요? 많은 도움이 되었거든요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=smalltalk_11004_3].dlg
   limit: do 170 znaków
   EN: What do you do when your mind is disturbed, Manager? How about learning to play music with me? It’s something that helped me a lot.
   PL:
266. [Kwestia głosowa [smalltalk_11004_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=smalltalk_11004_4].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Kwestia głosowa [smalltalk_11004_4] (Post-Uptie Chat 1)] 처음부터 이랬던 건 아니었어요. 우연한 계기로 악기와 춤을 접하고… 그때 비로소 제 안을 들여다볼 수 있게 되었거든요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=smalltalk_11004_4].dlg
   limit: do 140 znaków
   EN: I wasn’t always like this. One day, I chanced upon music and dance… They opened a window into my own psyche.
   PL:
268. [Kwestia głosowa [smalltalk_11004_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=smalltalk_11004_5].desc
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Kwestia głosowa [smalltalk_11004_5] (Post-Uptie Chat 2)] 고통도 두려움도 불안함도 전부 털어낼 수 있는 방법에 대해 알고 있어요. 그저 몸을 맡기면, 리듬이 저를 이끌어 줄 거에요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=smalltalk_11004_5].dlg
   limit: do 200 znaków
   EN: I know of a way to shake off the agony, fear, anxiety, and all else that weighs you down. Just surrender yourself to the rhythm, and it will lead you.
   PL:
270. [Kwestia głosowa [neglect_11004_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=neglect_11004_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Kwestia głosowa [neglect_11004_1] (Idle)] …제 연주가 별로였나요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=neglect_11004_1].dlg
   limit: do 120 znaków
   EN: …Did you not like my performance?
   PL:
272. [Kwestia głosowa [gacksung_11004_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=gacksung_11004_1].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Kwestia głosowa [gacksung_11004_1] (Uptying)] 더 유쾌한 연주로 보답드릴게요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=gacksung_11004_1].dlg
   limit: do 120 znaków
   EN: I’ll repay you with merrier music.
   PL:
274. [Kwestia głosowa [formation_11004_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=formation_11004_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Kwestia głosowa [formation_11004_1] (Deployment)] 흔들어 보죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=formation_11004_1].dlg
   limit: do 120 znaków
   EN: Let’s shake it.
   PL:
276. [Kwestia głosowa [battleentry_11004_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battleentry_11004_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Kwestia głosowa [battleentry_11004_1] (Stage Entry)] 이게 옳은 선택일까…?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battleentry_11004_1].dlg
   limit: do 120 znaków
   EN: Is this the right choice…?
   PL:
278. [Kwestia głosowa [battle_select_11004_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_select_11004_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Kwestia głosowa [battle_select_11004_1] (Viewed in Battle)] 단테 씨, 무슨 일이야…?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_select_11004_1].dlg
   limit: do 120 znaków
   EN: What’s up, Dante…?
   PL:
280. [Kwestia głosowa [battle_endcommand_11004_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_endcommand_11004_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Kwestia głosowa [battle_endcommand_11004_1] (Commencing Attack)] 머리통을 박살 내주마.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_endcommand_11004_1].dlg
   limit: do 120 znaków
   EN: I’ll bust your head.
   PL:
282. [Kwestia głosowa [battle_enemy_break_11004_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_enemy_break_11004_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Kwestia głosowa [battle_enemy_break_11004_1] (Enemy Stagger)] 다음에는 머리다.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_enemy_break_11004_1].dlg
   limit: do 120 znaków
   EN: I’ll take your head next.
   PL:
284. [Kwestia głosowa [battle_break_11004_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_break_11004_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Kwestia głosowa [battle_break_11004_1] (Staggered)] 윽!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_break_11004_1].dlg
   limit: do 120 znaków
   EN: Unk!
   PL:
286. [Kwestia głosowa [battle_kill_11004_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_kill_11004_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Kwestia głosowa [battle_kill_11004_1] (Enemy Killed)] 너무 쉽잖아.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_kill_11004_1].dlg
   limit: do 120 znaków
   EN: Too easy.
   PL:
288. [Kwestia głosowa [battle_allydead_11004_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_allydead_11004_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Kwestia głosowa [battle_allydead_11004_1] (Ally Death)] 다음은 누구일까…?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_allydead_11004_1].dlg
   limit: do 120 znaków
   EN: Who’s up next…?
   PL:
290. [Kwestia głosowa [choice_success_p_11004_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=choice_success_p_11004_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Kwestia głosowa [choice_success_p_11004_1] (Check Passed)] 생각보다 쉬웠어.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=choice_success_p_11004_1].dlg
   limit: do 120 znaków
   EN: That was easier than I thought.
   PL:
292. [Kwestia głosowa [choice_fail_n_11004_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=choice_fail_n_11004_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Kwestia głosowa [choice_fail_n_11004_1] (Check Failed)] 이런걸 바란 게 아니야…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=choice_fail_n_11004_1].dlg
   limit: do 120 znaków
   EN: Not what I wished for…
   PL:
294. [Kwestia głosowa [battle_clear_11004_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_clear_11004_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Kwestia głosowa [battle_clear_11004_1] (Victory Cry)] 이제 막 흥이 돋궈지려고 했는데… 벌써 끝났군요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_clear_11004_1].dlg
   limit: do 120 znaków
   EN: Just as I was about to feel some enthusiasm… it’s over already.
   PL:
296. [Kwestia głosowa [battle_clear_ex_11004_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_clear_ex_11004_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Kwestia głosowa [battle_clear_ex_11004_1] (Extra Conditions Fulfilled)] 오늘 연주는 만족스러웠어요. 한없이 유쾌했죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_clear_ex_11004_1].dlg
   limit: do 120 znaków
   EN: Today’s performance was satisfying. It entertained me to no end.
   PL:
298. [Kwestia głosowa [battle_defeat_11004_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_defeat_11004_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Kwestia głosowa [battle_defeat_11004_1] (Defeat Wail)] 기회는 또 있어요. 다시 흔들면 되는 거예요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Mariachi_11004.json :: dataList[id=battle_defeat_11004_1].dlg
   limit: do 120 znaków
   EN: We can always try again. Nothing says we can’t give it another shake.
   PL:

## [000] The One Who Shall Grip — Sinclair — 쥐어들 자
- ID Tożsamości: `11005` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 1 · HP bazowe: 79 · szybkość: 3–6 / 3–7 / 3–8 / 3–8
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Bleed, Burn

300. [Karta Tożsamości — tytuł] 쥐어들 자
   źródło: Personalities.json :: dataList[id=11005].title
   limit: do 40 znaków
   EN: The One Who Shall Grip
   PL:
301. [Karta Tożsamości — nazwa] 싱클레어
   źródło: Personalities.json :: dataList[id=11005].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Karta Tożsamości — nazwa z tytułem] 싱클레어
   źródło: Personalities.json :: dataList[id=11005].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Karta Tożsamości — opis] 싱클레어의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=11005].desc
   limit: do 120 znaków
   EN: Sinclair’s 5th Identity
   PL:
304. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 내몰린 심판
   źródło: Skills.json :: dataList[id=1100501].levelList[level=1].name ; dataList[id=1100501].levelList[level=2].name ; dataList[id=1100501].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 8 · monety: 2 (−2)
   limit: do 40 znaków
   EN: Coerced Judgement
   PL:
305. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — opis] [WhenUse] 정신력 7 감소
   źródło: Skills.json :: dataList[id=1100501].levelList[level=1].desc ; dataList[id=1100501].levelList[level=2].desc ; dataList[id=1100501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Lose 7 SP
   PL:
306. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackTail] 화상 2 부여
   źródło: Skills.json :: dataList[id=1100501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 2 Burn
   PL:
307. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackTail] 다음 턴에 광신 1을 얻음
   źródło: Skills.json :: dataList[id=1100501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1100501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Gain 1 Fanatic next turn
   PL:
308. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills.json :: dataList[id=1100501].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Burn
   PL:
309. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 화상 3 부여
   źródło: Skills.json :: dataList[id=1100501].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Burn
   PL:
310. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 판단을 멈춘 집행
   źródło: Skills.json :: dataList[id=1100502].levelList[level=1].name ; dataList[id=1100502].levelList[level=2].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 16 · monety: 4 (−4)
   limit: do 40 znaków
   EN: Amoral Enactment
   PL:
311. [Umiejętność 2 (×2) (ulepszenie 1) — opis] - [WhenUse] 정신력 10 감소\n- 자신에게 광신 이 있을 때 피해량 +5%
   źródło: Skills.json :: dataList[id=1100502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Lose 10 SP\nIf this unit is Fanatic, deal +5% damage
   PL:
312. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackTail] 화상 1 부여
   źródło: Skills.json :: dataList[id=1100502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 1 Burn
   PL:
313. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackTail] 화상 1 부여
   źródło: Skills.json :: dataList[id=1100502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1100502].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL:
315. [Umiejętność 2 (×2) (ulepszenie 2) — opis] - [WhenUse] 정신력 10 감소\n- 자신에게 광신 이 있을 때 피해량 +10%
   źródło: Skills.json :: dataList[id=1100502].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Lose 10 SP\nIf this unit is Fanatic, deal +10% damage
   PL:
316. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttackTail] 화상 2 부여
   źródło: Skills.json :: dataList[id=1100502].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 306 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1100502].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Burn
   PL:
318. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttackTail] 화상 2 부여
   źródło: Skills.json :: dataList[id=1100502].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 306 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1100502].levelList[level=2].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 317 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 4, efekt 1 — opis] [OnSucceedAttackTail] 화상 횟수 1 증가
   źródło: Skills.json :: dataList[id=1100502].levelList[level=2].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict +1 Burn Count
   PL:
321. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1100502].levelList[level=2].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 자멸적 정화
   źródło: Skills.json :: dataList[id=1100503].levelList[level=3].name ; dataList[id=1100503].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 30 · monety: 3 (−12)
   limit: do 40 znaków
   EN: Self-destructive Purge
   PL:
323. [Umiejętność 3 (×1) (ulepszenie 3) — opis] - [WhenUse] 정신력 15 감소\n- 자신에게 광신 이 있을 때 피해량 +15%\n- 대상이 <기계 융화 생명체>면 피해량 +10%
   źródło: Skills.json :: dataList[id=1100503].levelList[level=3].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Lose 15 SP\nIf this unit is Fanatic, deal +15% damage\nIf target is a <Mechanical Amalgam>, deal +10% damage
   PL:
324. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 흐트러짐 손상을 입힘
   źródło: Skills.json :: dataList[id=1100503].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1100503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 50% of damage dealt
   PL:
325. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈 이 5 이상 있으면, 화상 5 부여
   źródło: Skills.json :: dataList[id=1100503].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ Bleed, inflict 5 Burn
   PL:
326. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [EnemyKill] 다음 턴에 타격 위력 증가 1을 얻음
   źródło: Skills.json :: dataList[id=1100503].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1100503].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Gain 1 Blunt Power Up next turn
   PL:
327. [Umiejętność 3 (×1) (ulepszenie 4) — opis] - [WhenUse] 정신력 15 감소\n- 자신에게 광신 이 있을 때 피해량 +15%\n- 대상이 <기계 융화 생명체>면 피해량 +10%
   źródło: Skills.json :: dataList[id=1100503].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: - [WhenUse] Lose 15 SP\n- If this unit is Fanatic, deal +15% damage\n- If target is a <Mechanical Amalgam>, deal +10% damage
   PL:
328. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈 이 5 이상 있으면, 화상 7 부여
   źródło: Skills.json :: dataList[id=1100503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ Bleed, inflict 7 Burn
   PL:
329. [Obrona (ulepszenie 1) — nazwa] 그만...
   źródło: Skills.json :: dataList[id=1100504].levelList[level=1].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 17 · monety: 1 (−7)
   limit: do 40 znaków
   EN: Enough…
   PL:
330. [Obrona (ulepszenie 1) — opis] [StartBattle] 자신의 정신력 5 ~ 10 회복
   źródło: Skills.json :: dataList[id=1100504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Heal 5~10 SP
   PL:
331. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Wrath) — nazwa] 광염
   źródło: Passives.json :: dataList[id=1100501].name
   limit: do 40 znaków
   EN: Mad Flame
   PL:
332. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Wrath) — opis] 합 승리, 적 처치 시 회복하는 정신력 50% 감소
   źródło: Passives.json :: dataList[id=1100501].desc
   limit: do 120 znaków
   EN: Heal 50% less SP from winning a clash or defeating an enemy.
   PL:
333. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Wrath) — nazwa] 몰린
   źródło: Passives.json :: dataList[id=1100521].name
   limit: do 40 znaków
   EN: Cornering
   PL:
334. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Wrath) — opis] 정신력이 가장 낮은 아군 1명의 타격 피해량 +10%\n해당 효과를 받는 대상의 정신력이 0 미만이면 정신력이 낮아질수록 타격 피해량 추가 증가 (최대 10%)
   źródło: Passives.json :: dataList[id=1100521].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 1 ally with the least SP deals +10% Blunt damage.\nIf said ally is below 0 SP, further boost their Blunt damage the lower their SP is. (Max 10%)
   PL:
335. [Kwestia głosowa [get_11005_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=get_11005_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Kwestia głosowa [get_11005_1] (Identity Acquisition)] 전부, 불태울 거야… 역겨운 내 삶까지도.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=get_11005_1].dlg
   limit: do 120 znaków
   EN: Everything—I’ll burn it all… and my whole disgusting life, too.
   PL:
337. [Kwestia głosowa [lobby_morning_11005_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=lobby_morning_11005_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Kwestia głosowa [lobby_morning_11005_1] (Morning Greeting)] 당신이군요. 잠은 제대로 주무셨나요? 저는… 잠이 오질 않아서요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=lobby_morning_11005_1].dlg
   limit: do 120 znaków
   EN: So it’s you. Have you slept well? As for me… sleep wouldn’t come.
   PL:
339. [Kwestia głosowa [lobby_noon_11005_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=lobby_noon_11005_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Kwestia głosowa [lobby_noon_11005_1] (Afternoon Greeting)] 입맛이 없네요. 당신이라도 가면을 벗고 제대로 챙겨 드시길.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=lobby_noon_11005_1].dlg
   limit: do 120 znaków
   EN: I don’t feel like eating. You should take off your mask and have a nice meal.
   PL:
341. [Kwestia głosowa [lobby_night_11005_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=lobby_night_11005_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Kwestia głosowa [lobby_night_11005_1] (Evening Greeting)] 꿈을 꾸는 것이 두려웠던 적은 없나요? …부럽네요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=lobby_night_11005_1].dlg
   limit: do 120 znaków
   EN: Have you ever been afraid of dreaming? …I wish I were like you.
   PL:
343. [Kwestia głosowa [smalltalk_11005_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=smalltalk_11005_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Kwestia głosowa [smalltalk_11005_1] (Chatter #1)] 역겨운 것들과 삶을 포개왔었다는 걸 깨달은 후 부터, 지난 나날들이 전부 악몽으로 되돌아오네요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=smalltalk_11005_1].dlg
   limit: do 170 znaków
   EN: Ever since I realized that my life had been intertwined with disgusting beings, my every memory haunts me as its own nightmare.
   PL:
345. [Kwestia głosowa [smalltalk_11005_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=smalltalk_11005_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Kwestia głosowa [smalltalk_11005_2] (Chatter #2)] 불태우고 불태워서… 이미 눈 앞에서 잿더미가 된 것들인데도, 자꾸 저를 괴롭히네요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=smalltalk_11005_2].dlg
   limit: do 130 znaków
   EN: I burned and scorched them away… I saw them turn to ashes before my eyes, yet they still torment me.
   PL:
347. [Kwestia głosowa [smalltalk_11005_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=smalltalk_11005_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Kwestia głosowa [smalltalk_11005_3] (Chatter #3)] …역시, 그녀의 말이 맞아요. 더 많은 정화를 이루어 내야만… 제 정신 속의 정화도 이루어 질테니까.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=smalltalk_11005_3].dlg
   limit: do 130 znaków
   EN: …She is right—I must carry out more purification… That will then purify my mind with certainty.
   PL:
349. [Kwestia głosowa [smalltalk_11005_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=smalltalk_11005_4].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Kwestia głosowa [smalltalk_11005_4] (Post-Uptie Chat 1)] 오늘은 열 여섯을 꿰뚫어 불태웠죠. 내일은 곱절의 이단을 못질하고 태울 거예요. 후훗… 이것도 하다보니 즐겁지 않나요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=smalltalk_11005_4].dlg
   limit: do 160 znaków
   EN: I skewered sixteen today. Tomorrow, I will nail and cremate twice as many. Huhu… It gets fun as you keep at it, doesn’t it?
   PL:
351. [Kwestia głosowa [smalltalk_11005_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=smalltalk_11005_5].desc
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Kwestia głosowa [smalltalk_11005_5] (Post-Uptie Chat 2)] 불로서 오물을 정화하는 힘… 역시, 그녀의 말을 듣길 잘했어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=smalltalk_11005_5].dlg
   limit: do 120 znaków
   EN: The power to cleanse filth with fire… Indeed, it was certainly a good idea to listen to her.
   PL:
353. [Kwestia głosowa [neglect_11005_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=neglect_11005_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Kwestia głosowa [neglect_11005_1] (Idle)] …하실 말씀이 없다면, 그녀에게 가보아도 되나요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=neglect_11005_1].dlg
   limit: do 120 znaków
   EN: …If you have nothing to say, then may I go see her now?
   PL:
355. [Kwestia głosowa [gacksung_11005_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=gacksung_11005_1].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Kwestia głosowa [gacksung_11005_1] (Uptying)] 특별한 기분은 아니네요. 저는… 자질이 있는… 선택받은 자였으니까.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=gacksung_11005_1].dlg
   limit: do 120 znaków
   EN: This doesn’t really feel special. I have… always had talent… as the chosen one.
   PL:
357. [Kwestia głosowa [formation_11005_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=formation_11005_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Kwestia głosowa [formation_11005_1] (Deployment)] 말뚝을 쑤셔넣어 주죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=formation_11005_1].dlg
   limit: do 120 znaków
   EN: I’ll wrest them upon stakes.
   PL:
359. [Kwestia głosowa [battleentry_11005_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battleentry_11005_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Kwestia głosowa [battleentry_11005_1] (Stage Entry)] 불로 정화하고, 깨끗한 세계를 세우러.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battleentry_11005_1].dlg
   limit: do 120 znaków
   EN: To purge the grounds with fire, and build anew a clean world.
   PL:
361. [Kwestia głosowa [battle_select_11005_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_select_11005_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Kwestia głosowa [battle_select_11005_1] (Viewed in Battle)] 지금은 바빠요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_select_11005_1].dlg
   limit: do 120 znaków
   EN: I’m busy right now.
   PL:
363. [Kwestia głosowa [battle_endcommand_11005_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_endcommand_11005_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Kwestia głosowa [battle_endcommand_11005_1] (Commencing Attack)] 불길 속으로.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_endcommand_11005_1].dlg
   limit: do 120 znaków
   EN: Unto the fire.
   PL:
365. [Kwestia głosowa [battle_enemy_break_11005_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_enemy_break_11005_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Kwestia głosowa [battle_enemy_break_11005_1] (Enemy Stagger)] …좋아.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_enemy_break_11005_1].dlg
   limit: do 120 znaków
   EN: …Good.
   PL:
367. [Kwestia głosowa [battle_break_11005_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_break_11005_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Kwestia głosowa [battle_break_11005_1] (Staggered)] 큭!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_break_11005_1].dlg
   limit: do 120 znaków
   EN: Huch!
   PL:
369. [Kwestia głosowa [battle_kill_11005_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_kill_11005_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Kwestia głosowa [battle_kill_11005_1] (Enemy Killed)] …타 죽어라.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_kill_11005_1].dlg
   limit: do 120 znaków
   EN: …Go down in flames.
   PL:
371. [Kwestia głosowa [battle_dead_11005_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_dead_11005_1].desc
   limit: do 120 znaków
   EN: Death
   PL:
372. [Kwestia głosowa [battle_dead_11005_1] (Death)] 이게… 답이 아니었다고…?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_dead_11005_1].dlg
   limit: do 120 znaków
   EN: Was this… not the answer…?
   PL:
373. [Kwestia głosowa [choice_success_p_11005_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=choice_success_p_11005_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Kwestia głosowa [choice_success_p_11005_1] (Check Passed)] 어려울 것도 없네요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=choice_success_p_11005_1].dlg
   limit: do 120 znaków
   EN: That wasn’t troublesome at all.
   PL:
375. [Kwestia głosowa [choice_fail_n_11005_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=choice_fail_n_11005_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Kwestia głosowa [choice_fail_n_11005_1] (Check Failed)] 쯧, 안 될 줄 알았는데.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=choice_fail_n_11005_1].dlg
   limit: do 120 znaków
   EN: Tsk, I knew that wouldn’t work.
   PL:
377. [Kwestia głosowa [battle_clear_11005_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_clear_11005_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Kwestia głosowa [battle_clear_11005_1] (Victory Cry)] 이 정도면… 그녀에게도 인정 받겠어.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_clear_11005_1].dlg
   limit: do 120 znaków
   EN: I think… I did well enough to be acknowledged by her.
   PL:
379. [Kwestia głosowa [battle_clear_ex_11005_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_clear_ex_11005_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Kwestia głosowa [battle_clear_ex_11005_1] (Extra Conditions Fulfilled)] 당연한 결과죠. 저는, 선택 받았으니까… 그렇겠죠?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_clear_ex_11005_1].dlg
   limit: do 120 znaków
   EN: It’s only natural. Because I… am the chosen one… Isn’t that right?
   PL:
381. [Kwestia głosowa [battle_defeat_11005_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_defeat_11005_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Kwestia głosowa [battle_defeat_11005_1] (Defeat Wail)] 젠장, 어째서? 으드득…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ncorp_11005.json :: dataList[id=battle_defeat_11005_1].dlg
   limit: do 120 znaków
   EN: Scheiße, just how did—? Grrmgh…
   PL:

## [00] Lobotomy E.G.O::Red Sheet — Sinclair — 로보토미 E.G.O:: 홍적
- ID Tożsamości: `11006` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 2 · HP bazowe: 76 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture

383. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n홍적
   źródło: Personalities.json :: dataList[id=11006].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::Red Sheet
   PL:
384. [Karta Tożsamości — nazwa] 싱클레어
   źródło: Personalities.json :: dataList[id=11006].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Karta Tożsamości — nazwa z tytułem] 싱클레어
   źródło: Personalities.json :: dataList[id=11006].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Karta Tożsamości — opis] 싱클레어의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=11006].desc
   limit: do 120 znaków
   EN: Sinclair’s 6th Identity
   PL:
387. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 상처 부각
   źródło: Skills.json :: dataList[id=1100601].levelList[level=1].name ; dataList[id=1100601].levelList[level=2].name ; dataList[id=1100601].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 5 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Magnify Wound
   PL:
388. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1100601].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1100601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1100601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 대상의 [Burst]이 5 이상이면, 부적 1 얻음
   źródło: Skills.json :: dataList[id=1100601].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] If target has 5+ [Burst], gain 1 Talisman
   PL:
390. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]이 5 이상이면, 부적 1 얻음
   źródło: Skills.json :: dataList[id=1100601].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has 5+ [Burst], gain 1 Talisman
   PL:
391. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 늘어나는 부적
   źródło: Skills.json :: dataList[id=1100602].levelList[level=1].name ; dataList[id=1100602].levelList[level=2].name ; dataList[id=1100602].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Proliferating Talismans
   PL:
392. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 부적 1 얻음
   źródło: Skills.json :: dataList[id=1100602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain 1 Talisman
   PL:
393. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 부적 1 얻음
   źródło: Skills.json :: dataList[id=1100602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 392 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 부적 1 얻음
   źródło: Skills.json :: dataList[id=1100602].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1100602].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1100602].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Talisman
   PL:
395. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 부적 1 얻음
   źródło: Skills.json :: dataList[id=1100602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1100602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 부적 1 얻음
   źródło: Skills.json :: dataList[id=1100602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1100602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]이 3 이상이면, 부적 1 얻음
   źródło: Skills.json :: dataList[id=1100602].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has 3+ [Burst], gain 1 Talisman
   PL:
398. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Burst]이 있으면 부적 1 얻음
   źródło: Skills.json :: dataList[id=1100602].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has [Burst], gain 1 Talisman
   PL:
399. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Burst]이 있으면 부적 1 얻음
   źródło: Skills.json :: dataList[id=1100602].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Burst]이 있으면 부적 1 얻음
   źródło: Skills.json :: dataList[id=1100602].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 파열부
   źródło: Skills.json :: dataList[id=1100603].levelList[level=3].name ; dataList[id=1100603].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 5 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Rupturing Talisman
   PL:
402. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 부적 5 소모. 부적 5 부여
   źródło: Skills.json :: dataList[id=1100603].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1100603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 5 Talisman on self; Give 5 Talisman
   PL:
403. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Talisman]이 있으면 파열 횟수 1 증가
   źródło: Skills.json :: dataList[id=1100603].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Talisman], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Talisman] = 부적 / Talisman; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has [Talisman], inflict +1 [Burst] Count
   PL:
404. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Talisman]이 있으면 파열 횟수 3 증가
   źródło: Skills.json :: dataList[id=1100603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Talisman], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Talisman] = 부적 / Talisman; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has [Talisman], inflict +3 [Burst] Count
   PL:
405. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1100604].levelList[level=1].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Obrona (ulepszenie 1) — opis] [WhenUse] 부적 1 얻음
   źródło: Skills.json :: dataList[id=1100604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Talisman
   PL:
407. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — nazwa] 부적 떼기
   źródło: Passives.json :: dataList[id=1100601].name
   limit: do 40 znaków
   EN: Unfixing Talismans
   PL:
408. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — opis] 공격 적중 시 대상에게 [Burst]이 있으면 부적 1을 얻음
   źródło: Passives.json :: dataList[id=1100601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: On hit, if the target had [Burst], gain 1 Talisman.
   PL:
409. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 기원부
   źródło: Passives.json :: dataList[id=1100621].name
   limit: do 40 znaków
   EN: Wishing Talisman
   PL:
410. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 현재 체력이 가장 높은 아군 1명이 공격, 반격 스킬로 부여하는 파열 위력 부여 값 +1
   źródło: Passives.json :: dataList[id=1100621].desc
   limit: do 130 znaków
   EN: 1 ally with the highest current HP inflicts +1 more Rupture Potency with Attack and Counter Skills
   PL:
411. [Kwestia głosowa [get_11006_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=get_11006_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Kwestia głosowa [get_11006_1] (Identity Acquisition)] 아… 기어코… 저를 찾으셨군요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=get_11006_1].dlg
   limit: do 120 znaków
   EN: Ah... You've done it, you've... found me.
   PL:
413. [Kwestia głosowa [lobby_morning_11006_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=lobby_morning_11006_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Kwestia głosowa [lobby_morning_11006_1] (Morning Greeting)] 바라는 것이 있나요. 오셔서… 저와 함께 이걸 써보시는 건 어떨까요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=lobby_morning_11006_1].dlg
   limit: do 120 znaków
   EN: Is there anything you wish? Why don't you come over... and try this with me?
   PL:
415. [Kwestia głosowa [lobby_noon_11006_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=lobby_noon_11006_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Kwestia głosowa [lobby_noon_11006_1] (Afternoon Greeting)] 비스듬히 새어들어오는 햇빛을 보아하니… 정오인가요. 그런 시간이 되었군요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=lobby_noon_11006_1].dlg
   limit: do 130 znaków
   EN: Judging from the slanted ray of sunlight seeping in... Now must be noon. That's what time it is.
   PL:
417. [Kwestia głosowa [lobby_night_11006_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=lobby_night_11006_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Kwestia głosowa [lobby_night_11006_1] (Evening Greeting)] 초를 좀 더 밝혀야겠네요. 너무 어두우면… 밤눈이 어두워지실테니.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=lobby_night_11006_1].dlg
   limit: do 120 znaków
   EN: I should light more candles. If it's too dark... you won't see well in the night.
   PL:
419. [Kwestia głosowa [smalltalk_11006_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=smalltalk_11006_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Kwestia głosowa [smalltalk_11006_1] (Chatter #1)] 정말 긴 시간이었어요… 이 곳에서 나가지 않고, 벌써 얼마나 시간이 지났던 걸까요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=smalltalk_11006_1].dlg
   limit: do 120 znaków
   EN: It was such a long time... How many hours have passed while we stayed in here?
   PL:
421. [Kwestia głosowa [smalltalk_11006_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=smalltalk_11006_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Kwestia głosowa [smalltalk_11006_2] (Chatter #2)] 부적이… 모자라서는 안 돼요. 그렇다고… 제 몸에 너무 많은 부적이 있어서도… 안 되고요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=smalltalk_11006_2].dlg
   limit: do 140 znaków
   EN: The talismans... shouldn't be too sparse. But... there shouldn't be too many of them on my body, either.
   PL:
423. [Kwestia głosowa [smalltalk_11006_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=smalltalk_11006_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Kwestia głosowa [smalltalk_11006_3] (Chatter #3)] 이 부적은… 누군가의 움직임을 멈추죠. 붙이고, 붙일 수록… 점점 그 저주가 쌓여가는 거예요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=smalltalk_11006_3].dlg
   limit: do 140 znaków
   EN: These talismans... can impede movement. The more of them are attached... the more the curse piles up.
   PL:
425. [Kwestia głosowa [smalltalk_11006_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=smalltalk_11006_4].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Kwestia głosowa [smalltalk_11006_4] (Post-Uptie Chat 1)] 아… 함께 써주시는군요… 고마워요.\n…아! 자, 장난으로라도 제게 붙이시면 안된다고요!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=smalltalk_11006_4].dlg
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ah... You'll use them with me... thank you.\n...Ah! Y-You shouldn't attach them to me, even as a prank!
   PL:
427. [Kwestia głosowa [smalltalk_11006_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=smalltalk_11006_5].desc
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Kwestia głosowa [smalltalk_11006_5] (Post-Uptie Chat 2)] 제 몸에 붙어있는 것들은… 제 스스로 떼어낼 수 없는 것이랍니다.\n그런… 저주니까요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=smalltalk_11006_5].dlg
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The ones on my body... I can't remove on my own.\nIt's... that kind of curse.
   PL:
429. [Kwestia głosowa [neglect_11006_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=neglect_11006_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Kwestia głosowa [neglect_11006_1] (Idle)] 여유로우시다면 불꽃을 바라보고 쉬시는 것도 좋아요. 마음이 차분해지죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=neglect_11006_1].dlg
   limit: do 120 znaków
   EN: If you have the time, I'd suggest resting while watching fire. It calms your mind.
   PL:
431. [Kwestia głosowa [gacksung_11006_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=gacksung_11006_1].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Kwestia głosowa [gacksung_11006_1] (Uptying)] 해방을 위해서는… 설령 저주더라도 받아들이겠어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=gacksung_11006_1].dlg
   limit: do 120 znaków
   EN: For the liberation... I'll bear this, even if it's a curse.
   PL:
433. [Kwestia głosowa [formation_11006_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=formation_11006_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Kwestia głosowa [formation_11006_1] (Deployment)] 저주를 끼얹을 것이 있나보군요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=formation_11006_1].dlg
   limit: do 120 znaków
   EN: So there's something you want cursed.
   PL:
435. [Kwestia głosowa [battleentry_11006_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battleentry_11006_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Kwestia głosowa [battleentry_11006_1] (Stage Entry)] 뒤따르죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battleentry_11006_1].dlg
   limit: do 120 znaków
   EN: I'll follow.
   PL:
437. [Kwestia głosowa [battle_select_11006_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_select_11006_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Kwestia głosowa [battle_select_11006_1] (Viewed in Battle)] 집중… 하세요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_select_11006_1].dlg
   limit: do 120 znaków
   EN: Stay... focused.
   PL:
439. [Kwestia głosowa [battle_endcommand_11006_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_endcommand_11006_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Kwestia głosowa [battle_endcommand_11006_1] (Commencing Attack)] 그대로, 멈춰라.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_endcommand_11006_1].dlg
   limit: do 120 znaków
   EN: Stop there, and stay there.
   PL:
441. [Kwestia głosowa [battle_enemy_break_11006_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_enemy_break_11006_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Kwestia głosowa [battle_enemy_break_11006_1] (Enemy Stagger)] 둔해졌군요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_enemy_break_11006_1].dlg
   limit: do 120 znaków
   EN: They've become sluggish.
   PL:
443. [Kwestia głosowa [battle_break_11006_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_break_11006_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Kwestia głosowa [battle_break_11006_1] (Staggered)] 흣…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_break_11006_1].dlg
   limit: do 120 znaków
   EN: Hkh...
   PL:
445. [Kwestia głosowa [battle_kill_11006_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_kill_11006_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Kwestia głosowa [battle_kill_11006_1] (Enemy Killed)] 저주 속에, 가라앉는군요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_kill_11006_1].dlg
   limit: do 120 znaków
   EN: Into the curse they sink.
   PL:
447. [Kwestia głosowa [battle_dead_11006_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_dead_11006_1].desc
   (powtórzenie elementu 371 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Kwestia głosowa [battle_dead_11006_1] (Death)] 아… 결국엔… 멈추는구나…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_dead_11006_1].dlg
   limit: do 120 znaków
   EN: Ah... So it stops... in the end...
   PL:
449. [Kwestia głosowa [choice_success_p_11006_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=choice_success_p_11006_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Kwestia głosowa [choice_success_p_11006_2] (Check Passed)] 뜻 대로 되었네요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=choice_success_p_11006_2].dlg
   limit: do 120 znaków
   EN: It worked as we wished.
   PL:
451. [Kwestia głosowa [choice_fail_n_11006_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=choice_fail_n_11006_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Kwestia głosowa [choice_fail_n_11006_1] (Check Failed)] 이 또한 저주…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=choice_fail_n_11006_1].dlg
   limit: do 120 znaków
   EN: This, too, is a curse...
   PL:
453. [Kwestia głosowa [battle_clear_11006_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_clear_11006_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Kwestia głosowa [battle_clear_11006_1] (Victory Cry)] 해냈네요. 후… 이걸로 해방에 가까워 질 수 있겠죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_clear_11006_1].dlg
   limit: do 120 znaków
   EN: We did it. Phew... I hope this brings us closer to the liberation.
   PL:
455. [Kwestia głosowa [battle_clear_ex_11006_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_clear_ex_11006_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Kwestia głosowa [battle_clear_ex_11006_1] (Extra Conditions Fulfilled)] 모두를 멈춰세웠군요… 이제, 기술을 해방시켜줄 수 있겠죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_clear_ex_11006_1].dlg
   limit: do 120 znaków
   EN: They have all been stopped... Now, we'll be able to liberate technology.
   PL:
457. [Kwestia głosowa [battle_defeat_11006_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_defeat_11006_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Kwestia głosowa [battle_defeat_11006_1] (Defeat Wail)] 역시… 저주 받은 것은 누군가를 저주할 재목 조차 되지 못하는 걸까…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_LEGO_11006.json :: dataList[id=battle_defeat_11006_1].dlg
   limit: do 120 znaków
   EN: It must be... that the cursed can't so much as curse others...
   PL:

## [00] Molar Boatworks Fixer — Sinclair — 어금니 보트 센터 해결사
- ID Tożsamości: `11007` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 2 · HP bazowe: 69 · szybkość: 3–5 / 3–5 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Tremor

459. [Karta Tożsamości — tytuł] 어금니 보트 센터\n해결사
   źródło: Personalities.json :: dataList[id=11007].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Molar Boatworks\nFixer
   PL:
460. [Karta Tożsamości — nazwa] 싱클레어
   źródło: Personalities.json :: dataList[id=11007].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Karta Tożsamości — nazwa z tytułem] 싱클레어
   źródło: Personalities.json :: dataList[id=11007].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Karta Tożsamości — opis] 싱클레어의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=11007].desc
   limit: do 120 znaków
   EN: Sinclair’s 7th Identity
   PL:
463. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 맹습
   źródło: Skills_personality-10.json :: dataList[id=1100701].levelList[level=1].name ; dataList[id=1100701].levelList[level=2].name ; dataList[id=1100701].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 2 · monety: 4 (+1)
   limit: do 40 znaków
   EN: Fierce Assault
   PL:
464. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1100701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +1 Tremor Count
   PL:
465. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1100701].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] 자신의 진동 횟수가 10 이상이면 코인 위력 +1
   źródło: Skills_personality-10.json :: dataList[id=1100701].levelList[level=2].desc ; dataList[id=1100701].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 10+ Tremor Count, Coin Power +1
   PL:
467. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1100701].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1100701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +2 Tremor Count
   PL:
468. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 진동 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1100701].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Tremor Count
   PL:
469. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1100701].levelList[level=2].coinlist[#3].coindescs[#0].desc ; dataList[id=1100701].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 4, efekt 2 — opis] [OnSucceedAttackHead] 진동 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1100701].levelList[level=2].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1100701].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Tremor Count
   PL:
472. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1100701].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 471 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 침착하게...
   źródło: Skills_personality-10.json :: dataList[id=1100702].levelList[level=1].name ; dataList[id=1100702].levelList[level=2].name ; dataList[id=1100702].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Steady...
   PL:
474. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 진동 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1100702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Tremor Count
   PL:
475. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills_personality-10.json :: dataList[id=1100702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Tremor
   PL:
476. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 진동 횟수 4 증가
   źródło: Skills_personality-10.json :: dataList[id=1100702].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +4 Tremor Count
   PL:
477. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 4 부여
   źródło: Skills_personality-10.json :: dataList[id=1100702].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Tremor
   PL:
478. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 진동 횟수 6 증가
   źródło: Skills_personality-10.json :: dataList[id=1100702].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +6 Tremor Count
   PL:
479. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 6 부여
   źródło: Skills_personality-10.json :: dataList[id=1100702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 6 Tremor
   PL:
480. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 도박수
   źródło: Skills_personality-10.json :: dataList[id=1100703].levelList[level=3].name ; dataList[id=1100703].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Gamble
   PL:
481. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수가 10 이상이면, 진동 횟수를 전부 소모하여 대상에게 동일한 값의 진동 횟수 부여\n[OnSucceedAttack] 자신의 진동 횟수가 10 미만이면, 진동 6을 얻고, 자신에게 진동 폭발 발생\n대상에게 진동 폭발 피해만큼 타격 피해를 입힘
   źródło: Skills_personality-10.json :: dataList[id=1100703].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Tremor Count, consume all Tremor Count on self to inflict the same amount of Tremor Count on target\n[OnSucceedAttack] At less than 10 Tremor Count, gain 6 Tremor and trigger Tremor Burst on self\nDeal Blunt damage equal to Tremor Burst damage
   PL:
482. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 진동 횟수 10 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-10.json :: dataList[id=1100703].levelList[level=4].desc
   limit: do 120 znaków
   EN: Coin Power +1 for every 10 Tremor Count on self (Max 2)
   PL:
483. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수가 10 이상이면, 진동 횟수를 전부 소모하여 대상에게 동일한 값의 진동 횟수 부여\n[OnSucceedAttack] 자신의 진동 횟수가 10 미만이면, 진동 10을 얻고, 자신에게 진동 폭발 발생\n대상에게 진동 폭발 피해만큼 타격 피해를 입힘
   źródło: Skills_personality-10.json :: dataList[id=1100703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Tremor Count, consume all Tremor Count on self to inflict the same amount of Tremor Count on target\n[OnSucceedAttack] At less than 10 Tremor Count, gain 10 Tremor and trigger Tremor Burst on self\nDeal Blunt damage equal to Tremor Burst damage
   PL:
484. [Obrona (ulepszenie 1) — nazwa] 게 딱지 녀석들...!
   źródło: Skills_personality-10.json :: dataList[id=1100704].levelList[level=1].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Crab Bastards...!
   PL:
485. [Obrona (ulepszenie 1) — opis] [WhenUse] 파열 보호 1을 얻음 (턴 당 최대 3)
   źródło: Skills_personality-10.json :: dataList[id=1100704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Rupture Protection (3 times per turn)
   PL:
486. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Gloom) — nazwa] 불안정한 출력
   źródło: Passives.json :: dataList[id=1100701].name
   limit: do 40 znaków
   EN: Unstable Power Output
   PL:
487. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Gloom) — opis] 자신의 진동 횟수가 10 이상일 때 공격 적중 시 앞면이 나온 경우, 코인 효과로 적에게 부여하는 진동 과 진동 횟수 +1
   źródło: Passives.json :: dataList[id=1100701].desc
   limit: do 140 znaków
   EN: On hit with Heads Coins at 10+ Tremor Count on self, Inflict +1 Tremor and Tremor Count with Coin effects.
   PL:
488. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — nazwa] 출력 개조
   źródło: Passives.json :: dataList[id=1100721].name
   limit: do 40 znaków
   EN: Modified Power Output
   PL:
489. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — opis] 최대 체력이 가장 높은 아군 1명이 공격 스킬의 스킬, 코인 효과로 적에게 부여하는 진동 +1
   źródło: Passives.json :: dataList[id=1100721].desc
   limit: do 130 znaków
   EN: 1 ally that has the most Max HP inflicts +1 Tremor with the effects of their Attack Skills/Coins
   PL:
490. [Kwestia głosowa [get_11007_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=get_11007_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Kwestia głosowa [get_11007_1] (Identity Acquisition)] 음… 보트 맡기러 온 고객 분이신가요? 잘 부탁드릴게요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=get_11007_1].dlg
   limit: do 120 znaków
   EN: Mm... Are you here to get your boat fixed up? We'll take good care of it.
   PL:
492. [Kwestia głosowa [lobby_morning_11007_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=lobby_morning_11007_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Kwestia głosowa [lobby_morning_11007_1] (Morning Greeting)] 아직 가게 문은 열지 않았는데요… 아, 대신 의자라도 갖다 드릴테니 앉아서 쉬고 계세요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=lobby_morning_11007_1].dlg
   limit: do 120 znaków
   EN: The shop isn't open yet... Oh, I'll get you a chair so you can sit and rest while you wait.
   PL:
494. [Kwestia głosowa [lobby_noon_11007_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=lobby_noon_11007_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Kwestia głosowa [lobby_noon_11007_1] (Afternoon Greeting)] 우으… 이젠 점심으로 다른 것 좀 먹고 싶어요… 저 비린내 나는 크랲게로 찜, 탕, 구이, 수프… 온갖 종류로 요리를 해봤지만, 어떻게 해도 맛이 없었어요!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=lobby_noon_11007_1].dlg
   limit: do 250 znaków
   EN: Mmgh... I wanna eat something else for once... We've made all kinds of dishes out of those trash crabs—steamed, stewed, roasted, souped, you name it... but none of them ever taste any good!
   PL:
496. [Kwestia głosowa [lobby_night_11007_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=lobby_night_11007_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Kwestia głosowa [lobby_night_11007_1] (Evening Greeting)] 아! 용접 불꽃 때문에 눈이 좀 부시셨나요? 죄송해요… 가게 문 닫고 나서도 틈틈이 작업해놔야 해서요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=lobby_night_11007_1].dlg
   limit: do 170 znaków
   EN: Ah! Did the flash from the welding rod hurt your eyes? Sorry about that... There's work to be done even after the shop's closed.
   PL:
498. [Kwestia głosowa [smalltalk_11007_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=smalltalk_11007_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Kwestia głosowa [smalltalk_11007_1] (Chatter #1)] 처음 여기서 깨어났을 때는 정말 뭐가 뭔지 몰라서… 그저 정처없이 돌아다니다가 굶어 죽을 뻔했었죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=smalltalk_11007_1].dlg
   limit: do 170 znaków
   EN: When I first got up and found myself here, I had no idea what to make of anything... I almost starved to death wandering around.
   PL:
500. [Kwestia głosowa [smalltalk_11007_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=smalltalk_11007_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Kwestia głosowa [smalltalk_11007_2] (Chatter #2)] 기계를 다루는 건 그렇게 익숙하지 않지만… 전에 살던 곳으로 돌아가기 위해서라도 열심히 연습해야죠.\n어쩌면, 이 경험이 돌아갔을 때 도움을 주게 될지도 모르고요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=smalltalk_11007_2].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I'm not all too used to handling machinery...but I've got to practice hard if I want to get back to where I used to live. And who knows, this experience might be pretty handy in the future.
   PL:
502. [Kwestia głosowa [smalltalk_11007_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=smalltalk_11007_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Kwestia głosowa [smalltalk_11007_3] (Chatter #3)] 지금은 일상적으로 쓰고 있긴 하지만, U사의 이 특이점은 처음 볼 때부터 신기했다고 해야할까요… 이걸 통해서 붙여두면, 마치 이 부품이 처음부터 한 몸이었던 것처럼 붙게 되니까요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=smalltalk_11007_3].dlg
   limit: do 240 znaków
   EN: I'm used to it now, but U Corp's Singularity was always so fascinating to me... Attaching parts with this thing melds them together, as though they were made this way from the start.
   PL:
504. [Kwestia głosowa [smalltalk_11007_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=smalltalk_11007_4].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Kwestia głosowa [smalltalk_11007_4] (Post-Uptie Chat 1)] 이 무기도, 여기서 배운 용접이나 기계 지식을 통해서 직접 덧대어 개조, 수리한 거예요. 살짝 조잡해 보이긴 하지만… 그래도 꽤 괜찮죠?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=smalltalk_11007_4].dlg
   limit: do 190 znaków
   EN: This weapon too, was made from mechanical knowledge and welding skills I learned here. It doesn't look very sophisticated, but... Not bad, right?
   PL:
506. [Kwestia głosowa [smalltalk_11007_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=smalltalk_11007_5].desc
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Kwestia głosowa [smalltalk_11007_5] (Post-Uptie Chat 2)] 근처에 계셨던 다른 보트 센터 분들이 도와주신 덕에 여기까지 오게 된 거죠.\n…이젠 안 계시는 분들이지만요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=smalltalk_11007_5].dlg
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We could come this far thanks to all the help from people in other boat shops here.\n...They're no longer around, though.
   PL:
508. [Kwestia głosowa [neglect_11007_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=neglect_11007_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Kwestia głosowa [neglect_11007_1] (Idle)] 음… 이 틈에 정비 책이라도 읽어 둬야겠어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=neglect_11007_1].dlg
   limit: do 120 znaków
   EN: Hmm... I should read more books on maintenance in the meantime.
   PL:
510. [Kwestia głosowa [gacksung_11007_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=gacksung_11007_1].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Kwestia głosowa [gacksung_11007_1] (Uptying)] 개조를 했더니 출력은 나아졌는데… 여전히 게 딱지나 잡고 있다니, 괜히 했나 싶네요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=gacksung_11007_1].dlg
   limit: do 160 znaków
   EN: The upgrade certainly improved the output... but it kinda feels redundant if all I'm doing with it is catching more crabs.
   PL:
512. [Kwestia głosowa [formation_11007_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=formation_11007_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Kwestia głosowa [formation_11007_1] (Deployment)] 장비 시동 걸었습니다.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=formation_11007_1].dlg
   limit: do 120 znaków
   EN: The gears are in motion.
   PL:
514. [Kwestia głosowa [battleentry_11007_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battleentry_11007_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Kwestia głosowa [battleentry_11007_1] (Stage Entry)] 어어어? 출력이 왜 이러지…?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battleentry_11007_1].dlg
   limit: do 120 znaków
   EN: Häää? What's wrong with the power output...?
   PL:
516. [Kwestia głosowa [battle_select_11007_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_select_11007_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Kwestia głosowa [battle_select_11007_1] (Viewed in Battle)] 수리 문의신가요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_select_11007_1].dlg
   limit: do 120 znaków
   EN: Need something repaired?
   PL:
518. [Kwestia głosowa [battle_endcommand_11007_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_endcommand_11007_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Kwestia głosowa [battle_endcommand_11007_1] (Commencing Attack)] 출력 안정화… 됐다!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_endcommand_11007_1].dlg
   limit: do 120 znaków
   EN: Stabilizing output... There!
   PL:
520. [Kwestia głosowa [battle_enemy_break_11007_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_enemy_break_11007_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Kwestia głosowa [battle_enemy_break_11007_1] (Enemy Stagger)] 성능 좋고…!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_enemy_break_11007_1].dlg
   limit: do 120 znaków
   EN: Good going...!
   PL:
522. [Kwestia głosowa [battle_break_11007_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_break_11007_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Kwestia głosowa [battle_break_11007_1] (Staggered)] 윽…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_break_11007_1].dlg
   limit: do 120 znaków
   EN: Ngh…
   PL:
524. [Kwestia głosowa [battle_kill_11007_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_kill_11007_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Kwestia głosowa [battle_kill_11007_1] (Enemy Killed)] 후, 해치웠네요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_kill_11007_1].dlg
   limit: do 120 znaków
   EN: Phew, took care of that one.
   PL:
526. [Kwestia głosowa [battle_dead_11007_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_dead_11007_1].desc
   (powtórzenie elementu 371 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Kwestia głosowa [battle_dead_11007_1] (Death)] 아… 다들… 기다리실… 텐데.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_dead_11007_1].dlg
   limit: do 120 znaków
   EN: No... They're... waiting... for me.
   PL:
528. [Kwestia głosowa [choice_success_p_11007_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=choice_success_p_11007_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Kwestia głosowa [choice_success_p_11007_2] (Check Passed)] 정답이었군요!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=choice_success_p_11007_2].dlg
   limit: do 120 znaków
   EN: That was the right answer!
   PL:
530. [Kwestia głosowa [choice_fail_n_11007_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=choice_fail_n_11007_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Kwestia głosowa [choice_fail_n_11007_1] (Check Failed)] 아… 이게 아닌데.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=choice_fail_n_11007_1].dlg
   limit: do 120 znaków
   EN: This... wasn't quite it.
   PL:
532. [Kwestia głosowa [battle_clear_11007_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_clear_11007_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Kwestia głosowa [battle_clear_11007_1] (Victory Cry)] 이제 돌아가서 밀린 작업이나 마저 해야겠어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_clear_11007_1].dlg
   limit: do 120 znaków
   EN: I should go back and deal with the remaining work.
   PL:
534. [Kwestia głosowa [battle_clear_ex_11007_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_clear_ex_11007_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Kwestia głosowa [battle_clear_ex_11007_1] (Extra Conditions Fulfilled)] 깔끔했죠? 제가 봐도 뿌듯할 정도네요. 어, 근데 무기가… 왜, 왜 이러지?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_clear_ex_11007_1].dlg
   limit: do 170 znaków
   EN: That was clean, wasn't it? I'm pretty proud of it if I do say so myself. Huh, my weapon's going... Wha, what's wrong with it?
   PL:
536. [Kwestia głosowa [battle_defeat_11007_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_defeat_11007_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Kwestia głosowa [battle_defeat_11007_1] (Defeat Wail)] 아니… 이렇게 될 줄은… 뭔가 부족했던 걸까요…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Ucorp_11007.json :: dataList[id=battle_defeat_11007_1].dlg
   limit: do 120 znaków
   EN: Noo... I didn't think it'd go this way... What was I missing...
   PL:

## [000] Cinq Assoc. South Section 4 Director — Sinclair — 남부 섕크 협회 4과 부장
- ID Tożsamości: `11008` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 79 · szybkość: 4–6 / 4–7 / 4–8 / 4–8
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Poise

538. [Karta Tożsamości — tytuł] 남부 섕크 협회\n4과 부장
   źródło: Personalities.json :: dataList[id=11008].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cinq Assoc.\nSouth Section 4 Director
   PL:
539. [Karta Tożsamości — nazwa] 싱클레어
   źródło: Personalities.json :: dataList[id=11008].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Karta Tożsamości — nazwa z tytułem] 싱클레어
   źródło: Personalities.json :: dataList[id=11008].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Karta Tożsamości — opis] 싱클레어의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=11008].desc
   limit: do 120 znaków
   EN: Sinclair’s 8th Identity
   PL:
542. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 르미즈
   źródło: Skills_personality-10.json :: dataList[id=1100801].levelList[level=1].name ; dataList[id=1100801].levelList[level=2].name ; dataList[id=1100801].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Remise
   PL:
543. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1100801].levelList[level=1].desc ; dataList[id=1100801].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL:
544. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_personality-10.json :: dataList[id=1100801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Agility]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttackHead] Gain 1 [Agility] next turn
   PL:
545. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_personality-10.json :: dataList[id=1100801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 544 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_personality-10.json :: dataList[id=1100801].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1100801].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 1 [Agility] next turn
   PL:
547. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_personality-10.json :: dataList[id=1100801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1100801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 속도가 대상보다 2 이상 높으면 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1100801].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[WhenUse] Gain +2 [Breath] Count
   PL:
549. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 앙가즈망
   źródło: Skills_personality-10.json :: dataList[id=1100802].levelList[level=1].name ; dataList[id=1100802].levelList[level=2].name ; dataList[id=1100802].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Engagement
   PL:
550. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1100802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WinDuel] Gain +2 [Breath] Count
   PL:
551. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1100802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain +1 [Breath] Count
   PL:
552. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1100802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 자신의 속도가 대상보다 2 이상 높으면 코인 위력 +1\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1100802].levelList[level=2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[WinDuel] Gain +2 [Breath] Count
   PL:
554. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1100802].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1100802].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL:
555. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1100802].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1100802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 554 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 2)\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1100802].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's, Coin Power +1 for every 2 Speed difference (Max 2)\n[WinDuel] Gain +2 [Breath] Count
   PL:
557. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 꽁트르 아따끄
   źródło: Skills_personality-10.json :: dataList[id=1100803].levelList[level=3].name ; dataList[id=1100803].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Contre Attaque
   PL:
558. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 대상보다 2 이상 높으면 코인 위력 +1 \n[WinDuel] 자신의 [Breath] 횟수 10 소모. 소모한 [Breath] 횟수만큼 [Breath]을 얻음.\n[WinDuel] 적 슬롯의 공격 스킬과 [OneOnOneDuel]을 진행했으면, 적중 시 [Vulnerable] 1 부여 (턴 당 최대 2)
   źródło: Skills_personality-10.json :: dataList[id=1100803].levelList[level=3].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Breath], [OneOnOneDuel], [Vulnerable]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [OneOnOneDuel] = 1대1 대결 / Single Combat; [Vulnerable] = 취약 / Fragile
   EN: If this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[WinDuel] Consume 10 [Breath] Count. Gain [Breath] equal to [Breath] Count consumed.\n[WinDuel] If this unit conducted a [OneOnOneDuel] with the target Slot's Attack Skill, inflict 1 [Vulnerable] On Hit (Twice per turn)
   PL:
559. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DuelDeclaration_Sinclair] 부여
   źródło: Skills_personality-10.json :: dataList[id=1100803].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1100803].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DuelDeclaration_Sinclair]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DuelDeclaration_Sinclair] = 결투 선포 - 싱클레어 / Declared Duel - Sinclair
   EN: [OnSucceedAttack] Inflict [DuelDeclaration_Sinclair]
   PL:
560. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-10.json :: dataList[id=1100803].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: +30% Damage on Critical Hit
   PL:
561. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 3)\n[WinDuel] 자신의 [Breath] 횟수 10 소모. 소모한 [Breath] 횟수만큼 [Breath]을 얻음. 대상이 [DuelDeclaration_Sinclair] 대상인 경우, 대신 (소모한 [Breath] 횟수 X 2)만큼 [Breath]을 얻음\n[WinDuel] 적 슬롯의 공격 스킬과 [OneOnOneDuel]을 진행했으면, 적중 시 [Vulnerable] 1 부여 (턴 당 최대 2)
   źródło: Skills_personality-10.json :: dataList[id=1100803].levelList[level=4].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Breath], [DuelDeclaration_Sinclair], [OneOnOneDuel], [Vulnerable]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [DuelDeclaration_Sinclair] = 결투 선포 - 싱클레어 / Declared Duel - Sinclair; [OneOnOneDuel] = 1대1 대결 / Single Combat; [Vulnerable] = 취약 / Fragile
   EN: If this unit's Speed is faster than the target's, Coin Power +1 for every 2 Speed difference (Max 3)\n[WinDuel] Consume 10 [Breath] Count. Gain [Breath] equal to [Breath] Count consumed. Against targets with [DuelDeclaration_Sinclair], gain [Breath] equal to ([Breath] Count consumed x 2) instead\n[WinDuel] If this unit conducted a [OneOnOneDuel] with the target Slot's Attack Skill, inflict 1 [Vulnerable] On Hit (Twice per turn)
   PL:
562. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +50%
   źródło: Skills_personality-10.json :: dataList[id=1100803].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: +50% Damage on Critical Hit
   PL:
563. [Obrona (ulepszenia 3–4) — nazwa] 데팡시브
   źródło: Skills_personality-10.json :: dataList[id=1100804].levelList[level=3].name ; dataList[id=1100804].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Défensive
   PL:
564. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — nazwa] 잠든 살기
   źródło: Passives.json :: dataList[id=1100801].name
   limit: do 40 znaków
   EN: Slumbering Bloodthirst
   PL:
565. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — opis] 턴 종료 시 [Breath] 횟수 5당 다음 턴 자신의 속도 최대 값 +2 (최대 6)
   źródło: Passives.json :: dataList[id=1100801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Turn End: Gain +2 Max Speed next turn for every 5 [Breath] Count (Max 6)
   PL:
566. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Pride) — nazwa] 잠든 살기
   źródło: Passives.json :: dataList[id=1100811].name
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Pride) — opis] 턴 종료 시 [Breath] 횟수 5당 다음 턴 자신의 속도 최대 값 +2 (최대 6)\n전투 시작 시 모든 아군의 속도가 모든 적보다 높으면, [PenetrateDamageUp] 1을 얻음
   źródło: Passives.json :: dataList[id=1100811].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [PenetrateDamageUp]
   znaczenie tagów: [Breath] = 호흡 / Poise; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: Turn End: Gain +2 Max Speed next turn for every 5 [Breath] Count (Max 6)\nCombat Start: If Speed of all allies is higher than Speed of all enemies, gain 1 [PenetrateDamageUp]
   PL:
568. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — nazwa] 느리시네요
   źródło: Passives.json :: dataList[id=1100821].name
   limit: do 40 znaków
   EN: Too Slow
   PL:
569. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — opis] 속도가 가장 빠른 아군 1명이 회피 성공 시 다음 턴에 [Agility] 1을 얻음 (최대 5회)
   źródło: Passives.json :: dataList[id=1100821].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: The fastest ally, On Evade, gains 1 [Agility] next turn (Max 5)
   PL:
570. [Kwestia głosowa [get_11008_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=get_11008_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Kwestia głosowa [get_11008_1] (Identity Acquisition)] 어, 앗! 죄송해요! 너, 너무 과했나…?!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=get_11008_1].dlg
   limit: do 120 znaków
   EN: O—oh, I'm sorry! W-was I too rough...?!
   PL:
572. [Kwestia głosowa [lobby_morning_11008_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=lobby_morning_11008_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Kwestia głosowa [lobby_morning_11008_1] (Morning Greeting)] 아, 안녕하세요~ 오늘은 상쾌한 아침이신가요? 표정이 좋으시네요!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=lobby_morning_11008_1].dlg
   limit: do 120 znaków
   EN: Ah, hello~ Having a good morning today? You're looking pretty upbeat!
   PL:
574. [Kwestia głosowa [lobby_noon_11008_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=lobby_noon_11008_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Kwestia głosowa [lobby_noon_11008_1] (Afternoon Greeting)] 그럼 오늘은 함께 점심을… 아, 앗… 잠시만요…\n하아, 죄송해요. 오늘도 다른 동료분들이 부르셔서… 거절이 힘드네요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=lobby_noon_11008_1].dlg
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: How about we grab lunch together today— Ah, uh... Give me a second.\nHaah, I'm sorry. My coworkers are calling me over, and I shouldn't refuse them.
   PL:
576. [Kwestia głosowa [lobby_night_11008_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=lobby_night_11008_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Kwestia głosowa [lobby_night_11008_1] (Evening Greeting)] 저는 밤 공기를 맡는게 너무 좋더라고요. 검에만 가장 집중할… 수 있다고 해야할까.\n오로지, 검 끝과. 상대 밖에 보이지 않아서.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=lobby_night_11008_1].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I love breathing in the night air. It helps me focus solely on my sword... All I can see are the tip of my blade and my enemy's throat.
   PL:
578. [Kwestia głosowa [smalltalk_11008_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=smalltalk_11008_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Kwestia głosowa [smalltalk_11008_1] (Chatter #1)] 가끔씩… 제가 검에게 끌려다니는 건 아닌가하는 생각이 들어요. 대련 중에도 정신을 차리고 보면 몸이 너무 앞서 가기도 한다니까요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=smalltalk_11008_1].dlg
   limit: do 200 znaków
   EN: Sometimes... I wonder if the sword is wielding me and not the other way around. I sometimes lose myself and get too aggressive, even during a friendly spar.
   PL:
580. [Kwestia głosowa [smalltalk_11008_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=smalltalk_11008_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Kwestia głosowa [smalltalk_11008_2] (Chatter #2)] 항상 얼렁뚱땅이고, 실수도 잦지만… 동료분들이 너무 친절하게 잘 대해주셔서 지내기 좋은 것 같아요!\n음… 가끔은 저를 보고 무서워하는 표정을 짓기도 하시지만요. 또 실수를 저지를까봐 긴장하시는 걸까요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=smalltalk_11008_2].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I'm a bit all over the place, and I make a lot of mistakes... but I like it here! My coworkers are so nice to me.\nMmm... Sometimes, they give me worried looks, though. I guess they're worried that I might stumble into another blunder?
   PL:
582. [Kwestia głosowa [smalltalk_11008_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=smalltalk_11008_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Kwestia głosowa [smalltalk_11008_3] (Chatter #3)] 어, 그러니까… 팔을 이렇게 해서… 우오옷?! 이거 맞죠…? 이 분이 이렇게 쓰러져버리는 게 맞나요?!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=smalltalk_11008_3].dlg
   limit: do 150 znaków
   EN: So uh... I just need to use my arm to... Woaaah?! Did I do that right...? I can just topple them, just like that?!
   PL:
584. [Kwestia głosowa [smalltalk_11008_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=smalltalk_11008_4].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Kwestia głosowa [smalltalk_11008_4] (Post-Uptie Chat 1)] 검의 끝이 상대의 급소와 맞닿아 있다고 생각하는 거죠. 마치 두 손가락 끝을 마주보게 하고 가까워진다는 상상을 계속하면 어느 순간 닿아 있는 것 처럼.\n자, 보셨죠?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=smalltalk_11008_4].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Imagine that the end of the blade is already touching the enemy's vitals. Did you ever learn about the exercise where you can make your fingers touch just by imagining it really hard? It's just like that.\nSee?
   PL:
586. [Kwestia głosowa [smalltalk_11008_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=smalltalk_11008_5].desc
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Kwestia głosowa [smalltalk_11008_5] (Post-Uptie Chat 2)] 주변은 잘 보이지 않아요. 저 조차도, 잘 보이지 않죠. 준비가 되면… 오로지 어두운 공간 안에 결투의 상대가 놓여있을 뿐이예요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=smalltalk_11008_5].dlg
   limit: do 180 znaków
   EN: When I'm ready to duel, my surroundings fade away. A part of me does, too. There is nothing before me but the enemy in a dark, dark place.
   PL:
588. [Kwestia głosowa [neglect_11008_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=neglect_11008_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Kwestia głosowa [neglect_11008_1] (Idle)] 아! 저, 지금은 조금 한가해 진 것 같아요. 지금이라도 얘기를… 아, 안 계시네?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=neglect_11008_1].dlg
   limit: do 120 znaków
   EN: Ah! I'm finally free from work! Now we can talk... Ah, where are you?
   PL:
590. [Kwestia głosowa [gacksung_11008_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=gacksung_11008_1].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Kwestia głosowa [gacksung_11008_1] (Uptying)] 당신께, 완벽한 집중을 보여줄게요. 비록 제 시야는 보여드릴 수 없지만.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=gacksung_11008_1].dlg
   limit: do 120 znaków
   EN: I'll show you impeccable focus. Though you will never see as I do.
   PL:
592. [Kwestia głosowa [formation_11008_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=formation_11008_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Kwestia głosowa [formation_11008_1] (Deployment)] 일인가요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=formation_11008_1].dlg
   limit: do 120 znaków
   EN: Is it work?
   PL:
594. [Kwestia głosowa [battleentry_11008_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battleentry_11008_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Kwestia głosowa [battleentry_11008_1] (Stage Entry)] 검 끝을… 바라본다…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battleentry_11008_1].dlg
   limit: do 120 znaków
   EN: Focus... on the tip of my blade...
   PL:
596. [Kwestia głosowa [battle_select_11008_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_select_11008_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Kwestia głosowa [battle_select_11008_1] (Viewed in Battle)] …….
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_select_11008_1].dlg
   limit: do 120 znaków
   EN: .......
   PL:
598. [Kwestia głosowa [battle_endcommand_11008_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_endcommand_11008_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Kwestia głosowa [battle_endcommand_11008_1] (Commencing Attack)] 거기구나.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_endcommand_11008_1].dlg
   limit: do 120 znaków
   EN: There it is.
   PL:
600. [Kwestia głosowa [battle_enemy_break_11008_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_enemy_break_11008_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Kwestia głosowa [battle_enemy_break_11008_1] (Enemy Stagger)] 아직 모자라.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_enemy_break_11008_1].dlg
   limit: do 120 znaków
   EN: More.
   PL:
602. [Kwestia głosowa [battle_break_11008_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_break_11008_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Kwestia głosowa [battle_break_11008_1] (Staggered)] 핫?!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_break_11008_1].dlg
   limit: do 120 znaków
   EN: Hah?!
   PL:
604. [Kwestia głosowa [battle_kill_11008_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_kill_11008_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Kwestia głosowa [battle_kill_11008_1] (Enemy Killed)] 급소가 전부 꿰뚫렸네.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_kill_11008_1].dlg
   limit: do 120 znaków
   EN: I've hit all of your vital areas.
   PL:
606. [Kwestia głosowa [battle_dead_11008_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_dead_11008_1].desc
   (powtórzenie elementu 371 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Kwestia głosowa [battle_dead_11008_1] (Death)] 어? 어라… 분명히 잘 싸우고… 있었… 는데.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_dead_11008_1].dlg
   limit: do 120 znaków
   EN: Huh? No... I thought... the duel was... going well...
   PL:
608. [Kwestia głosowa [choice_success_p_11008_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=choice_success_p_11008_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Kwestia głosowa [choice_success_p_11008_2] (Check Passed)] 흥… 어라, 해결됐네요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=choice_success_p_11008_2].dlg
   limit: do 120 znaków
   EN: Hmph... Huh? That worked?
   PL:
610. [Kwestia głosowa [choice_fail_n_11008_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=choice_fail_n_11008_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Kwestia głosowa [choice_fail_n_11008_1] (Check Failed)] 이게 아니라고? 그럼 여기, 아니. 여기를!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=choice_fail_n_11008_1].dlg
   limit: do 120 znaków
   EN: That didn't work? Then how about here? No, here?!
   PL:
612. [Kwestia głosowa [battle_clear_11008_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_clear_11008_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Kwestia głosowa [battle_clear_11008_1] (Victory Cry)] 어떻게… 잘 마무리 했네요! 어휴, 이번에는 실수를 안했나?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_clear_11008_1].dlg
   limit: do 120 znaków
   EN: Well, that worked out... somehow! Whew, I guess I didn't make any mistakes this time.
   PL:
614. [Kwestia głosowa [battle_clear_ex_11008_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_clear_ex_11008_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Kwestia głosowa [battle_clear_ex_11008_1] (Extra Conditions Fulfilled)] 아직 모자라… 앗, 여러분들! 어…? 왜 그렇게 뒷걸음질을 하시는 건가요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_clear_ex_11008_1].dlg
   limit: do 120 znaków
   EN: More... Oh hey, guys! Uh... why are you backing away?
   PL:
616. [Kwestia głosowa [battle_defeat_11008_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_defeat_11008_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Kwestia głosowa [battle_defeat_11008_1] (Defeat Wail)] 이렇게 끝날 리 없어. 아직, 아직 더 잘해볼 수 있는데!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Cinq_11008.json :: dataList[id=battle_defeat_11008_1].dlg
   limit: do 120 znaków
   EN: It can't end like this. I have—I know I can do better!
   PL:

## [000] Dawn Office Fixer — Sinclair — 새벽 사무소 해결사
- ID Tożsamości: `11009` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9103 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Burn

618. [Karta Tożsamości — tytuł] 새벽 사무소\n해결사
   źródło: Personalities.json :: dataList[id=11009].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Dawn Office\nFixer
   PL:
619. [Karta Tożsamości — nazwa] 싱클레어
   źródło: Personalities.json :: dataList[id=11009].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Karta Tożsamości — nazwa z tytułem] 싱클레어
   źródło: Personalities.json :: dataList[id=11009].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Karta Tożsamości — opis] 싱클레어의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=11009].desc
   limit: do 120 znaków
   EN: Sinclair's 9th Identity
   PL:
622. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 맹렬한 돌진
   źródło: Skills_personality-10.json :: dataList[id=1100901].levelList[level=1].name ; dataList[id=1100901].levelList[level=2].name ; dataList[id=1100901].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 3 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Fierce Charge
   PL:
623. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-10.json :: dataList[id=1100901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL:
624. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신이 불안정 E.G.O 상태면, 코인 재사용 (스킬당 최대 1회 발동)
   źródło: Skills_personality-10.json :: dataList[id=1100901].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1100901].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1100901].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] When in a Volatile E.G.O state, Reuse Coin (once per Skill)
   PL:
625. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 2 — podsumowanie] [OnSucceedAttackHead] 자신이 불안정 E.G.O 상태면, 코인 재사용
   źródło: Skills_personality-10.json :: dataList[id=1100901].levelList[level=1].coinlist[#0].coindescs[#1].summary ; dataList[id=1100901].levelList[level=2].coinlist[#0].coindescs[#1].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] When in a Volatile E.G.O state, Reuse Coin
   PL:
626. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-10.json :: dataList[id=1100901].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1100901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL:
627. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — podsumowanie] [OnSucceedAttackHead] 자신이 불안정 E.G.O 상태면, 코인 재사용
   źródło: Skills_personality-10.json :: dataList[id=1100901].levelList[level=4].coinlist[#0].coindescs[#1].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] When in a Volatile E.G.O state, Reuse this Coin
   PL:
628. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 노을빛 검
   źródło: Skills_personality-10.json :: dataList[id=1100902].levelList[level=1].name ; dataList[id=1100902].levelList[level=2].name ; dataList[id=1100902].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Sunset Blade
   PL:
629. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신이 불안정 E.G.O 상태면, 정신력 5 소모\n[BeforeAttack] 자신이 불안정 E.G.O 상태면, 공격 가중치 +1\n[EndSkill] 자신이 불안정 E.G.O 상태면, 정신력 5 소모
   źródło: Skills_personality-10.json :: dataList[id=1100902].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BeforeAttack], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] When in a Volatile E.G.O state, consume 5 SP\n[BeforeAttack] When in a Volatile E.G.O state, Atk Weight +1\n[EndSkill] When in a Volatile E.G.O state, consume 5 SP
   PL:
630. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1100902].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1100902].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1100902].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count
   PL:
631. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1100902].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1100902].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1100902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1100902].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1100902].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1100902].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">대상의 [Combustion]이 4 이상이면, 합 위력 +1</style>\n[WhenUse] 자신이 불안정 E.G.O 상태면, 정신력 5 소모\n[BeforeAttack] 자신이 불안정 E.G.O 상태면, 공격 가중치 +1\n[EndSkill] 자신이 불안정 E.G.O 상태면, 정신력 5 소모
   źródło: Skills_personality-10.json :: dataList[id=1100902].levelList[level=2].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [WhenUse], [BeforeAttack], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">If target has 4+ [Combustion], Clash Power +1</style>\n[WhenUse] When in a Volatile E.G.O state, consume 5 SP\n[BeforeAttack] When in a Volatile E.G.O state, Atk Weight +1\n[EndSkill] When in a Volatile E.G.O state, consume 5 SP
   PL:
634. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Combustion]이 4 이상이면, 합 위력 +1\n[WhenUse] 자신이 불안정 E.G.O 상태면, 정신력 5 소모\n[BeforeAttack] 자신이 불안정 E.G.O 상태면, 공격 가중치 +1\n<style="highlight">- 자신의 정신력이 45면, 대신 공격 가중치 +2</style>\n[EndSkill] 자신이 불안정 E.G.O 상태면, 정신력 5 소모
   źródło: Skills_personality-10.json :: dataList[id=1100902].levelList[level=4].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [WhenUse], [BeforeAttack], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If target has 4+ [Combustion], Clash Power +1\n[WhenUse] When in a Volatile E.G.O state, consume 5 SP\n[BeforeAttack] When in a Volatile E.G.O state, Atk Weight +1\n<style="highlight">- At 45 SP, Atk Weight +2 instead</style>\n[EndSkill] When in a Volatile E.G.O state, consume 5 SP
   PL:
635. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 낙인
   źródło: Skills_personality-10.json :: dataList[id=1100903].levelList[level=3].name ; dataList[id=1100903].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 2 (+7)
   limit: do 40 znaków
   EN: Stigmatize
   PL:
636. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Combustion]이 10 이상이면, 코인 위력 +1\n자신이 불안정 E.G.O 상태면, 타오르는 일격으로 발동됨\n[WinDuel] 정신력 10 회복\n[DefeatDuel] 정신력 10 감소
   źródło: Skills_personality-10.json :: dataList[id=1100903].levelList[level=3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [WinDuel], [DefeatDuel], [TabExplain]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has 10+ [Combustion], Coin Power +1\nWhen in a Volatile E.G.O State, activate Blazing[TabExplain] Strike instead\n[WinDuel] Heal 10 SP\n[DefeatDuel] Lose 10 SP
   PL:
637. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-10.json :: dataList[id=1100903].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1100903].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]
   PL:
638. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-10.json :: dataList[id=1100903].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1100903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 637 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">대상의 [Combustion] 7 당 코인 위력 +1 (최대 2)</style>\n자신이 불안정 E.G.O 상태면, 타오르는 일격으로 발동됨\n[WinDuel] 정신력 10 회복\n[DefeatDuel] 정신력 10 감소
   źródło: Skills_personality-10.json :: dataList[id=1100903].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [WinDuel], [DefeatDuel], [TabExplain]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: <style="highlight">Coin Power +1 for every 7 [Combustion] on target (max 2)</style>\nWhen in a Volatile E.G.O state, activate Blazing[TabExplain] Strike instead\n[WinDuel] Heal 10 SP\n[DefeatDuel] Lose 10 SP
   PL:
640. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 타오르는 일격
   źródło: Skills_personality-10.json :: dataList[id=1100905].levelList[level=3].name ; dataList[id=1100905].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 13 · monety: 1 (+15)
   limit: do 40 znaków
   EN: Blazing Strike
   PL:
641. [Umiejętność 4 (×0) (ulepszenie 3) — opis] 적 전체 [Combustion] 위력의 합 4 당 코인 위력 +1 (최대 8)\n[WinDuel] 정신력 10 회복\n[DefeatDuel] 정신력 30감소\n분노 공명당 피해량 5% 증가 (최대 30%)\n[EndSkill] 정신력 15 감소
   źródło: Skills_personality-10.json :: dataList[id=1100905].levelList[level=3].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [WinDuel], [DefeatDuel], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Coin Power +1 for every 4 (sum of [Combustion] Potency on all enemies) (max 8)\n[WinDuel] Heal 10 SP\n[DefeatDuel] Lose 30 SP\nDeal +5% damage for every Wrath Reson. (max 30%)\n[EndSkill] Lose 15 SP
   PL:
642. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] 대상의 [Combustion] 1당 피해량 +2.5% (최대 100%)
   źródło: Skills_personality-10.json :: dataList[id=1100905].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal +2.5% damage for every 1 [Combustion] on target (max 100%)
   PL:
643. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — podsumowanie] 대상의 [Combustion] 비례 피해량이 증가
   źródło: Skills_personality-10.json :: dataList[id=1100905].levelList[level=3].coinlist[#0].coindescs[#0].summary ; dataList[id=1100905].levelList[level=4].coinlist[#0].coindescs[#0].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal more damage based on [Combustion] on target
   PL:
644. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Combustion]이 10 이상 있으면, 무작위 적 (가장 높은 공명 수)명에게 [Combustion] 2 부여
   źródło: Skills_personality-10.json :: dataList[id=1100905].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 10+ [Combustion], inflict 2 [Combustion] against (# of highest Reson.) random enemies
   PL:
645. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 2 — podsumowanie] [OnSucceedAttack] 공명 비례 [Combustion] 부여
   źródło: Skills_personality-10.json :: dataList[id=1100905].levelList[level=3].coinlist[#0].coindescs[#1].summary ; dataList[id=1100905].levelList[level=4].coinlist[#0].coindescs[#1].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict [Combustion] based on Reson.
   PL:
646. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 10 부여
   źródło: Skills_personality-10.json :: dataList[id=1100905].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=1100905].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 10 [Combustion]
   PL:
647. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 4 — opis] [EnemyKill] 처치한 대상의 [Combustion] 위력을 무작위 적에게 나눠서 부여 (최대 10. 집중 전투인 경우 부위로 판정)
   źródło: Skills_personality-10.json :: dataList[id=1100905].levelList[level=3].coinlist[#0].coindescs[#3].desc ; dataList[id=1100905].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Combustion]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Combustion] = 화상 / Burn
   EN: [EnemyKill] Randomly inflict [Combustion] Potency of the defeated target between all enemies (max 10. In Focused Encounters, between all Parts)
   PL:
648. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 4 — podsumowanie] [EnemyKill] 무작위 적에게 [Combustion] 부여
   źródło: Skills_personality-10.json :: dataList[id=1100905].levelList[level=3].coinlist[#0].coindescs[#3].summary ; dataList[id=1100905].levelList[level=4].coinlist[#0].coindescs[#3].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Combustion]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Combustion] = 화상 / Burn
   EN: [EnemyKill] Inflict [Combustion] to random enemies
   PL:
649. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 적 전체 [Combustion] 위력의 합 4 당 코인 위력 +<style="highlight">2</style> (최대 8)\n[WinDuel] 정신력 10 회복\n[DefeatDuel] 정신력 30 감소\n분노 공명당 피해량 <style="highlight">10</style>% 증가 (최대 <style="highlight">60</style>%)\n<style="highlight">- 최대 분노 완전 공명 수가 4 이상이면, 대신 20% 증가 (최대 120%)</style>\n[EndSkill] 정신력 15 감소
   źródło: Skills_personality-10.json :: dataList[id=1100905].levelList[level=4].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [WinDuel], [DefeatDuel], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Coin Power +<style="highlight">2</style> for every 4 (sum of [Combustion] Potency on all enemies) (max 8)\n[WinDuel] Heal 10 SP\n[DefeatDuel] Lose 30 SP\nDeal +<style="highlight">10</style>% damage for every Wrath Reson. (max <style="highlight">60</style>%)\n<style="highlight">If at 4+ highest Wrath A-Reson., deal +20% damage for every Wrath Reson. instead (max 120%)</style>\n[EndSkill] Lose 15 SP
   PL:
650. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] 대상의 [Combustion] 1당 피해량 +<style="highlight">4</style>% (최대 <style="highlight">120</style>%)
   źródło: Skills_personality-10.json :: dataList[id=1100905].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal +<style="highlight">4</style>% damage for every 1 [Combustion] on target (max <style="highlight">120</style>%)
   PL:
651. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Combustion]이 10 이상 있으면, 무작위 적 (가장 높은 공명 수)명에게 [Combustion] 2 부여\n<style="highlight">- 해당 공명이 분노 공명이면, [Combustion] 횟수 1 추가 부여</style>
   źródło: Skills_personality-10.json :: dataList[id=1100905].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 10+ [Combustion], inflict 2 [Combustion] against (# of highest Reson.) random enemies\n<style="highlight">- If the above Reson. was a Wrath Reson., inflict +1 [Combustion] Count as well</style>
   PL:
652. [Obrona (ulepszenia 3–4) — nazwa] 후회
   źródło: Skills_personality-10.json :: dataList[id=1100904].levelList[level=3].name ; dataList[id=1100904].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Rue
   PL:
653. [Obrona (ulepszenie 3) — opis] 자신이 불안정 E.G.O 상태면, 대상의 [Combustion] 2 당 기본 위력 +1 (최대 10)
   źródło: Skills_personality-10.json :: dataList[id=1100904].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When in a Volatile E.G.O state, Base Power +1 for every 2 [Combustion] on target (max 10)
   PL:
654. [Obrona (ulepszenie 4) — opis] 자신이 불안정 E.G.O 상태면, 대상의 [Combustion] 2 당 기본 위력 +1 (최대 <style="highlight">20</style>)
   źródło: Skills_personality-10.json :: dataList[id=1100904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When in a Volatile E.G.O state, Base Power +1 for every 2 [Combustion] on target (max <style="highlight">20</style>)
   PL:
655. [Umiejętność powiązana 1100906 (ulepszenie 3) — nazwa] 다시 타오르는 일격
   źródło: Skills_personality-10.json :: dataList[id=1100906].levelList[level=3].name
   limit: do 40 znaków
   EN: Rekindled Strike
   PL:
656. [Pasywka bojowa (od ulepszenia 1) — nazwa] 불안정한 자아의 껍질
   źródło: Passives.json :: dataList[id=1100902].name
   limit: do 40 znaków
   EN: Unstable Shell of Ego
   PL:
657. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 시작 시 정신력이 40 이상이면, 정신력을 20 소모하여 불안정 E.G.O::밀랍날개 상태가 됨. (이후 턴 시작 시 효과가 추가로 발동되지 않음)\n또는 한 턴에 아군이 2명 이상 사망했을 때, 턴 종료 시 정신력이 -45가 아니면, 정신력을 20으로 변경한 후 불안정 E.G.O::밀랍날개 상태가 됨. (두 조건이 동시에 발생한 경우, 정신력 결과 값은 높은 쪽으로 결정됨.)\n\n불안정 E.G.O 상태가 될 때, 피해나 흐트러짐 손상으로 흐트러짐 상태가 된 경우, 흐트러짐 상태를 해제함. 해제할 수 없는 흐트러짐 상태인 경우, 불안정 E.G.O 상태가 될 수 없음.\n\n불안정 E.G.O 상태동안 [UnstableFeeling]을 얻음.\n\n턴 시작 시 정신력이 0 이하면, 불안정 E.G.O 상태가 해제됨.
   źródło: Passives.json :: dataList[id=1100902].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: \n, [UnstableFeeling]
   znaczenie tagów: [UnstableFeeling] = 불안정한 격정 / Volatile Passion
   EN: Turn Start: At 40+ SP, consume 20 SP to enter the Volatile E.G.O::Waxen Pinion state. (this 'Turn Start' effect does not activate repeatedly)\n\nIf 2+ allies are defeated in a single turn, and if this unit's SP isn't at -45 at Turn End, reset SP to 20; then, enter the Volatile E.G.O::Waxen Pinion state. (if both conditions are met at the same time, whichever condition that results in a higher SP goes into effect)\n\nIf this unit gets Staggered due to damage or raised Stagger Threshold when entering the Volatile E.G.O state, recover from Stagger. If the Stagger is something that cannot be naturally recovered from, this unit does not enter the Volatile E.G.O state.\n\nGain [UnstableFeeling] while in the Volatile E.G.O state.\n\nTurn Start: At 0 or less SP, exit the Volatile E.G.O::Waxen Pinion state.
   PL:
658. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Wrath) — nazwa] 스티그마 공방 무기 / 격정
   źródło: Passives.json :: dataList[id=1100901].name
   limit: do 50 znaków
   EN: Stigma Workshop Weaponry / Passion
   PL:
659. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Wrath) — opis] 자신이 스킬로 부여하는 [Combustion] 위력 +1 (턴 당 최대 6회 발동)\n자신이 불안정 E.G.O 상태이고, 정신력이 0 이상이면, (자신의 정신력/20)만큼 코인 위력이 증가함. 자신의 정신력이 45면, 대신 코인 위력 +3
   źródło: Passives.json :: dataList[id=1100901].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: This unit inflicts +1 more [Combustion] Potency with its Skills (Activates 6 times per turn)\nWhen in a Volatile E.G.O state, and at 0+ SP, gain Coin Power +(SP/20). At 45 SP, gain Coin Power +3 instead.
   PL:
660. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Wrath) — podsumowanie] 스킬로 부여하는 [Combustion] 위력 +1\n정신력에 비례하여 코인 위력이 증가
   źródło: Passives.json :: dataList[id=1100901].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Inflict +1 more [Combustion] Potency with Skills\nGain Coin Power based on SP
   PL:
661. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Wrath) — nazwa] 스티그마 공방 무기 / 격정
   źródło: Passives.json :: dataList[id=1100911].name
   (powtórzenie elementu 658 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Wrath) — opis] 자신이 스킬로 부여하는 [Combustion] 위력<style="highlight">과 횟수 +1</style> (턴 당 최대 6회 발동)\n자신이 불안정 E.G.O 상태이고, 정신력이 0 이상이면, (자신의 정신력/20)만큼 코인 위력이 증가함. 자신의 정신력이 45면, 대신 코인 위력 +3
   źródło: Passives.json :: dataList[id=1100911].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: This unit inflicts +1 more [Combustion] Potency <style="highlight">and Count</style> with its Skills (Activates 6 times per turn)\nWhen in a Volatile E.G.O state, and at 0+ SP, gain Coin Power +(SP/20). At 45 SP, gain Coin Power +3 instead.
   PL:
663. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Wrath) — podsumowanie] 스킬로 부여하는 [Combustion] 위력, 횟수 +1\n정신력에 비례하여 코인 위력이 증가
   źródło: Passives.json :: dataList[id=1100911].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Inflict +1 more [Combustion] Potency and Count with Skills\nGain Coin Power based on SP
   PL:
664. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 이글거리는 검
   źródło: Passives.json :: dataList[id=1100921].name
   limit: do 40 znaków
   EN: Flaring Brand
   PL:
665. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 편성 순서 1번인 아군이 앞면 적중 시 [Combustion] 횟수 1 부여 (턴 당 최대 4회 발동)
   źródło: Passives.json :: dataList[id=1100921].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When the #1 Sinner to be Deployed Heads Hits, inflict +1 [Combustion] Count (4 times per turn)
   PL:
666. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — podsumowanie] 앞면 적중 시 [Combustion] 횟수 1 부여
   źródło: Passives.json :: dataList[id=1100921].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: On Heads Hit, inflict +1 [Combustion] Count
   PL:
667. [Kwestia głosowa [get_11009_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=get_11009_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Kwestia głosowa [get_11009_1] (Identity Acquisition)] 손이 가끔씩 떨릴 때가 있는데, 겁쟁이처럼 보이지 않았으면 좋겠네요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=get_11009_1].dlg
   limit: do 120 znaków
   EN: Sometimes I get hand tremors... I hope that doesn't make me look like a coward.
   PL:
669. [Kwestia głosowa [lobby_morning_11009_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=lobby_morning_11009_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Kwestia głosowa [lobby_morning_11009_1] (Morning Greeting)] 아! 일찍 오셨네요. 오늘 들어온 의뢰서는 평소처럼 책상 위에 올려뒀어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=lobby_morning_11009_1].dlg
   limit: do 140 znaków
   EN: Oh! You're back early. As always, I placed any and all contract requests we received today on your desk.
   PL:
671. [Kwestia głosowa [lobby_noon_11009_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=lobby_noon_11009_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Kwestia głosowa [lobby_noon_11009_1] (Afternoon Greeting)] 슬슬 일하러 가지 않으면 사무소 월세가 위험할지도 몰라요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=lobby_noon_11009_1].dlg
   limit: do 120 znaków
   EN: We should get to work soon. Or our Office might not make our next month's rent.
   PL:
673. [Kwestia głosowa [lobby_night_11009_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=lobby_night_11009_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Kwestia głosowa [lobby_night_11009_1] (Evening Greeting)] 밤공기가 차네요. 따뜻한 쌍화차라도 한 잔 타드릴까요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=lobby_night_11009_1].dlg
   limit: do 120 znaków
   EN: It's pretty cold tonight. How about a warm cup of ssanghwa-cha?
   PL:
675. [Kwestia głosowa [smalltalk_11009_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=smalltalk_11009_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Kwestia głosowa [smalltalk_11009_1] (Chatter #1)] 음악 좋아하세요? 저는 첼로 연주를 듣는 게 좋더라고요.\n언젠가 배워보고 싶네요. 직접 연주하는 음악은 또 다를 테니까.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=smalltalk_11009_1].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Do you listen to music from time to time? I enjoy the sound of cello myself.\nOne day, I hope to have a chance to try my hand at learning it. I'm sure creating music with my own hands feels different.
   PL:
677. [Kwestia głosowa [smalltalk_11009_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=smalltalk_11009_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Kwestia głosowa [smalltalk_11009_2] (Chatter #2)] 가열된 스티그마 공방의 무기는 상대에게 지워지지 않는 특유의 문양을 화상으로 남기죠. 상대가 살아남더라도 살아가는 동안 그 낙인이 따라다니는 거에요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=smalltalk_11009_2].dlg
   limit: do 240 znaków
   EN: Weapons from Stigma Workshop brand their victims with their unique 'stigma'. Even if they were to survive the fight, they'll have to live with that mark for the rest of their lives.
   PL:
679. [Kwestia głosowa [smalltalk_11009_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=smalltalk_11009_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Kwestia głosowa [smalltalk_11009_3] (Chatter #3)] 아, 쌍화차가 입에 맞으셨나요? 특색 노란쌍화라니… 쌍화차에 들어가는 노른자랑 제 머리카락 색이 비슷한 건 사실이지만… 그런 식으로 놀리는 건 그만해주세요…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=smalltalk_11009_3].dlg
   limit: do 270 znaków
   EN: Oh, did you enjoy the ssanghwa-cha? Huh? They'd call me 'The Yellow Ssanghwa' if I ever became a Color...? I mean, I guess my blonde hair does resemble an egg yolk, but... Come on, don't tease me like that.
   PL:
681. [Kwestia głosowa [smalltalk_11009_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=smalltalk_11009_4].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Kwestia głosowa [smalltalk_11009_4] (Post-Uptie Chat 1)] 도시에 살아가는 사람은… 누군가를 위해 행동하면 안 되는 걸까요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=smalltalk_11009_4].dlg
   limit: do 120 znaków
   EN: Are people of the City... not allowed to do anything on behalf of others?
   PL:
683. [Kwestia głosowa [smalltalk_11009_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=smalltalk_11009_5].desc
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Kwestia głosowa [smalltalk_11009_5] (Post-Uptie Chat 2)] 그들을 위한… 타인을 위한… 누군가를 위한… 저는 그런 이기적인 말로 저를 포장했어요. 당신도 스스로를 무언가로 포장해본 적이 있나요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=smalltalk_11009_5].dlg
   limit: do 240 znaków
   EN: "For them". "For the others". "For someone else's sake"... You know, they were all just... selfish disguises to hide my true self. Have you ever pretended to be something you're not?
   PL:
685. [Kwestia głosowa [neglect_11009_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=neglect_11009_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Kwestia głosowa [neglect_11009_1] (Idle)] 누구나… 생각을 정리할 시간은 필요한 거겠죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=neglect_11009_1].dlg
   limit: do 120 znaków
   EN: Everyone... needs the time to collect their thoughts.
   PL:
687. [Kwestia głosowa [gacksung_11009_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=gacksung_11009_1].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Kwestia głosowa [gacksung_11009_1] (Uptying)] 슬퍼하고 있는 저를 위해 대신 울어줄 사람은 없겠죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=gacksung_11009_1].dlg
   limit: do 120 znaków
   EN: No one's going to shed their tears on behalf of my sorrow.
   PL:
689. [Kwestia głosowa [formation_11009_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=formation_11009_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Kwestia głosowa [formation_11009_1] (Deployment)] 의뢰… 인가요? 먼저 준비하고 있을게요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=formation_11009_1].dlg
   limit: do 120 znaków
   EN: Do we have... a contract? Okay, I'll go get ready.
   PL:
691. [Kwestia głosowa [battleentry_11009_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battleentry_11009_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Kwestia głosowa [battleentry_11009_1] (Stage Entry)] 발목 잡지 않도록, 최선을 다할게요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battleentry_11009_1].dlg
   limit: do 120 znaków
   EN: I'll try my best not to hold you back.
   PL:
693. [Kwestia głosowa [battle_select_11009_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_select_11009_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Kwestia głosowa [battle_select_11009_1] (Viewed in Battle)] 저에게도 무언가에 맞설 용기를…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_select_11009_1].dlg
   limit: do 120 znaków
   EN: Give me the courage to stand up to something...
   PL:
695. [Kwestia głosowa [battle_endcommand_11009_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_endcommand_11009_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Kwestia głosowa [battle_endcommand_11009_1] (Commencing Attack)] 당신의 판단을 따를게요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_endcommand_11009_1].dlg
   limit: do 120 znaków
   EN: I will follow your judgment.
   PL:
697. [Kwestia głosowa [battle_endcommand_11009_2] — sytuacja] 공격 시작 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_endcommand_11009_2].desc
   limit: do 120 znaków
   EN: Commencing Attack 2
   PL:
698. [Kwestia głosowa [battle_endcommand_11009_2] (Commencing Attack 2)] 여전히 무섭고 겁이 나, 그럼에도… 멈추고 싶지 않아.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_endcommand_11009_2].dlg
   limit: do 120 znaków
   EN: I'm just as scared as I was before. But... despite everything, I don't want to stop.
   PL:
699. [Kwestia głosowa [battle_enemy_break_11009_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_enemy_break_11009_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Kwestia głosowa [battle_enemy_break_11009_1] (Enemy Stagger)] 망설이지 말고…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_enemy_break_11009_1].dlg
   limit: do 120 znaków
   EN: I shouldn't hesitate...
   PL:
701. [Kwestia głosowa [battle_break_11009_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_break_11009_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Kwestia głosowa [battle_break_11009_1] (Staggered)] 이래선 걱정만 끼치게 되는 꼴인데…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_break_11009_1].dlg
   limit: do 120 znaków
   EN: I feel like I'm just causing you concern...
   PL:
703. [Kwestia głosowa [battle_kill_11009_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_kill_11009_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Kwestia głosowa [battle_kill_11009_1] (Enemy Killed)] 조금 더 과감하게!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_kill_11009_1].dlg
   limit: do 120 znaków
   EN: ... I have to be bold!
   PL:
705. [Kwestia głosowa [battle_dead_11009_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_dead_11009_1].desc
   (powtórzenie elementu 371 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Kwestia głosowa [battle_dead_11009_1] (Death)] 끝까지… 함께 싸울 수 있을 거라 생각했어요…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_dead_11009_1].dlg
   limit: do 120 znaków
   EN: I thought... I'd be there for you all the way...
   PL:
707. [Kwestia głosowa [choice_success_p_11009_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=choice_success_p_11009_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [Kwestia głosowa [choice_success_p_11009_2] (Check Passed)] 여러분을 위한 일이었어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=choice_success_p_11009_2].dlg
   limit: do 120 znaków
   EN: It was for everyone's sake.
   PL:
709. [Kwestia głosowa [choice_fail_n_11009_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=choice_fail_n_11009_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Kwestia głosowa [choice_fail_n_11009_1] (Check Failed)] 걸림돌이… 되고 싶지 않았는데…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=choice_fail_n_11009_1].dlg
   limit: do 120 znaków
   EN: I didn't want to be a baggage... to you all...
   PL:
711. [Kwestia głosowa [battle_clear_11009_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_clear_11009_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Kwestia głosowa [battle_clear_11009_1] (Victory Cry)] 저희도 손실이 없는 건 아니지만… 결과가 중요한 법이죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_clear_11009_1].dlg
   limit: do 120 znaków
   EN: We did suffer some losses, but... only the outcome matters in the end.
   PL:
713. [Kwestia głosowa [battle_clear_ex_11009_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_clear_ex_11009_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Kwestia głosowa [battle_clear_ex_11009_1] (Extra Conditions Fulfilled)] 확실한 승리였어요. 돌아가면 저번처럼 홈파티라도 할까요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_clear_ex_11009_1].dlg
   limit: do 130 znaków
   EN: That was certainly a perfect victory. How about we throw a house party like we did last time?
   PL:
715. [Kwestia głosowa [battle_defeat_11009_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_defeat_11009_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Kwestia głosowa [battle_defeat_11009_1] (Defeat Wail)] 지금은 때가 아니야… 도움을 청해야만…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Philip_11009.json :: dataList[id=battle_defeat_11009_1].dlg
   limit: do 120 znaków
   EN: Not yet... I've got to, I've got to go ask for help...!
   PL:

## [00] Zwei Assoc. West Section 3 — Sinclair — 서부 츠바이 협회 3과
- ID Tożsamości: `11010` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 5 · HP bazowe: 86 · szybkość: 3–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor

717. [Karta Tożsamości — tytuł] 서부 츠바이 협회\n3과
   źródło: Personalities.json :: dataList[id=11010].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Zwei Assoc.\nWest Section 3
   PL:
718. [Karta Tożsamości — nazwa] 싱클레어
   źródło: Personalities.json :: dataList[id=11010].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Karta Tożsamości — nazwa z tytułem] 싱클레어
   źródło: Personalities.json :: dataList[id=11010].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Karta Tożsamości — opis] 싱클레어의 열번째 인격
   źródło: Personalities.json :: dataList[id=11010].desc
   limit: do 120 znaków
   EN: Sinclair’s 10th Identity
   PL:
721. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 제압합니다.
   źródło: Skills_personality-10.json :: dataList[id=1101001].levelList[level=1].name ; dataList[id=1101001].levelList[level=2].name ; dataList[id=1101001].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Suppressing.
   PL:
722. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n[WhenUse] [DefenseUp] 1 얻음\n[WinDuel] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1101001].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [DefenseUp], [WinDuel], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WinDuel] = [합 승리시] / [Clash Win]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp]\n[WinDuel] Gain +2 [Vibration] Count
   PL:
723. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [WinDuelAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1101001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Vibration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Vibration] = 진동 / Tremor
   EN: [WinDuelAttack] Inflict +1 [Vibration] Count
   PL:
724. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [DefenseUp] 2를 얻음
   źródło: Skills_personality-10.json :: dataList[id=1101001].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1101001].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttackHead] Gain 2 [DefenseUp] next turn
   PL:
725. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n[WhenUse] [DefenseUp] <style="highlight">2</style> 얻음\n<style="highlight">[WhenUse] 대상의 [Vibration] 횟수가 4 이상이면, 합 위력 +1</style>\n[WinDuel] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1101001].levelList[level=2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [DefenseUp], [Vibration], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain <style="highlight">2</style> [DefenseUp]\n<style="highlight">[WhenUse] If target has 4+ [Vibration] Count, Clash Power +1</style>\n[WinDuel] Gain +2 [Vibration] Count
   PL:
726. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [WinDuelAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1101001].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1101001].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Vibration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Vibration] = 진동 / Tremor
   EN: [WinDuelAttack] Inflict +2 [Vibration] Count
   PL:
727. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n[WhenUse] [DefenseUp] 2 얻음\n[WhenUse] 대상의 [Vibration] 횟수가 4 이상이면, 합 위력 +<style="highlight">2</style>\n[WinDuel] 자신의 [Vibration] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-10.json :: dataList[id=1101001].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [DefenseUp], [Vibration], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 2 [DefenseUp]\n[WhenUse] If target has 4+ [Vibration] Count, Clash Power +<style="highlight">2</style>\n[WinDuel] Gain +<style="highlight">3</style> [Vibration] Count
   PL:
728. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 2를 얻음
   źródło: Skills_personality-10.json :: dataList[id=1101001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 2 [DefenseUp] next turn
   PL:
729. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 전투 준비
   źródło: Skills_personality-10.json :: dataList[id=1101002].levelList[level=1].name ; dataList[id=1101002].levelList[level=2].name ; dataList[id=1101002].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Combat Preparation
   PL:
730. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n[WinDuel] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1101002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [WinDuel], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [WinDuel] = [합 승리시] / [Clash Win]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n[WinDuel] Gain +2 [Vibration] Count
   PL:
731. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신을 제외한 [DefenseUp]를 보유한 아군 1명에게 (대상이 보유한 [DefenseUp]/3)만큼 다음 턴에 [AttackUp] 부여 (턴 당 1회. 최대 3 부여)
   źródło: Skills_personality-10.json :: dataList[id=1101002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp], [AttackUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttack] On 1 other ally with [DefenseUp], apply (([DefenseUp] on the ally)/3) [AttackUp] next turn (once per turn, max 3)
   PL:
732. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n<style="highlight">[WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 3)\n[WhenUse] 자신의 [DefenseUp]가 4 이상이면, 코인 위력 +1</style>\n[WinDuel] 자신의 [Vibration] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-10.json :: dataList[id=1101002].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Vibration], [DefenseUp], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n<style="highlight">[WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max 3)\n[WhenUse] At 4+ [DefenseUp], Coin Power +1</style>\n[WinDuel] Gain +<style="highlight">3</style> [Vibration] Count
   PL:
733. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [WinDuelAttack] 자신 제외 현재 체력 비율이 가장 낮은 아군 1명에게 다음 턴에 방어 레벨 증가 2 부여
   źródło: Skills_personality-10.json :: dataList[id=1101002].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]
   EN: [WinDuelAttack] On 1 other ally with the lowest HP percentage, apply 2 Defense Level Up next turn
   PL:
734. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신을 제외한 [DefenseUp]를 보유한 아군 1명에게 (대상이 보유한 [DefenseUp]/<style="highlight">2</style>)만큼 다음 턴에 [AttackUp] 부여 (턴 당 1회. 최대 3 부여)
   źródło: Skills_personality-10.json :: dataList[id=1101002].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DefenseUp], [AttackUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttack] On 1 other ally with [DefenseUp], apply (([DefenseUp] on the ally)/<style="highlight">2</style>) [AttackUp] next turn (once per turn, max 3)
   PL:
735. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n[WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 3)\n[WhenUse] 자신의 [DefenseUp] 4 이상이면, 코인 위력 +1\n[WinDuel] 자신의 [Vibration] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_personality-10.json :: dataList[id=1101002].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Vibration], [DefenseUp], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max 3)\n[WhenUse] At 4+ [DefenseUp], Coin Power +1\n[WinDuel] Gain +3 [Vibration] Count<style="highlight"></style>
   PL:
736. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [WinDuelAttack] 자신 제외 현재 체력 비율이 가장 낮은 아군 <style="highlight">2</style>명에게 다음 턴에 방어 레벨 증가 2 부여
   źródło: Skills_personality-10.json :: dataList[id=1101002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WinDuelAttack]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]
   EN: [WinDuelAttack] On <style="highlight">2 other allies</style> with the lowest HP percentage, apply 2 Defense Level Up next turn
   PL:
737. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신을 제외한 [DefenseUp]를 보유한 아군 <style="highlight">2</style>명에게 (대상이 보유한 [DefenseUp]/2)만큼 다음 턴에 [AttackUp] 부여 (턴 당 1회. 최대 3 부여)
   źródło: Skills_personality-10.json :: dataList[id=1101002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DefenseUp], [AttackUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttack] On <style="highlight">2 other allies</style> with [DefenseUp], apply (([DefenseUp] on the ally)/2) [AttackUp] next turn (once per turn, max 3)
   PL:
738. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 울타리
   źródło: Skills_personality-10.json :: dataList[id=1101003].levelList[level=3].name ; dataList[id=1101003].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Fence
   PL:
739. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 2)\n[WhenUse] 자신의 [DefenseUp] 3 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-10.json :: dataList[id=1101003].levelList[level=3].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max 2)\n[WhenUse] Coin Power +1 for every 3 [DefenseUp] on self (max 2)
   PL:
740. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신 제외 현재 체력 비율이 가장 낮은 아군 1명에게 다음 턴에 [DefenseUp] 3 부여
   źródło: Skills_personality-10.json :: dataList[id=1101003].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] On 1 other ally with the lowest HP percentage, apply 3 [DefenseUp] next turn
   PL:
741. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수를 최대 8 소모하여, 소모한 값만큼 대상의 [Vibration] 횟수 증가
   źródło: Skills_personality-10.json :: dataList[id=1101003].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1101003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Consume up to 8 [Vibration] Count on self, and inflict the same amount of [Vibration] Count on target
   PL:
742. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-10.json :: dataList[id=1101003].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1101003].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
743. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 <style="highlight">4</style>)\n[WhenUse] 자신의 [DefenseUp] 3 당 코인 위력 +1 (최대 <style="highlight">3</style>)
   źródło: Skills_personality-10.json :: dataList[id=1101003].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max <style="highlight">4</style>)\n[WhenUse] Coin Power +1 for every 3 [DefenseUp] on self (max <style="highlight">3</style>)
   PL:
744. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신 제외 현재 체력 비율이 가장 낮은 아군 1명에게 다음 턴에 [DefenseUp] <style="highlight">4</style> 부여
   źródło: Skills_personality-10.json :: dataList[id=1101003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] On 1 other ally with the lowest HP percentage, apply <style="highlight">4</style> [DefenseUp] next turn
   PL:
745. [Obrona (ulepszenia 1,4) — nazwa] 츠바이 기사단 대검술 - 가드
   źródło: Skills_personality-10.json :: dataList[id=1101004].levelList[level=1].name ; dataList[id=1101004].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 2 · monety: 1 (+9)
   limit: do 60 znaków
   EN: Zwei Knight's Greatsword Form - Guard
   PL:
746. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] 다음 턴에 이 스킬 슬롯의 [Aggro] 5 증가\n[WhenUse] 자신의 [Vibration] 횟수 2 증가 (턴 당 1회)\n[WinDuel] [VibrationExplosion]
   źródło: Skills_personality-10.json :: dataList[id=1101004].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [Aggro], [WhenUse], [Vibration], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [Aggro] = 도발치 / Aggro; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [CanDuelGuard]\n[StartBattle] Gain +5 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain +2 [Vibration] Count (once per turn)\n[WinDuel] Trigger [VibrationExplosion]
   PL:
747. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-10.json :: dataList[id=1101004].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1101004].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
748. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[StartBattle] 다음 턴에 이 스킬 슬롯의 [Aggro] 5 증가\n[WhenUse] 자신의 [Vibration] 횟수 <style="highlight">3</style> 증가 (턴 당 1회)\n[WinDuel] [VibrationExplosion]
   źródło: Skills_personality-10.json :: dataList[id=1101004].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [StartBattle], [Aggro], [WhenUse], [Vibration], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [Aggro] = 도발치 / Aggro; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [CanDuelGuard]\n[StartBattle] Gain +5 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain +<style="highlight">3</style> [Vibration] Count (once per turn)\n[WinDuel] Trigger [VibrationExplosion]
   PL:
749. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — nazwa] 보호 임무 시작
   źródło: Passives.json :: dataList[id=1101001].name
   limit: do 40 znaków
   EN: Begin Protection Mission
   PL:
750. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — opis] 전투 시작 시, 자신의 진동 횟수만큼 [DefenseUp] 얻음 (최대 5)
   źródło: Passives.json :: dataList[id=1101001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseUp], [Vibration]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Vibration] = 진동 / Tremor
   EN: At Combat Start, gain [DefenseUp] equal to [Vibration] Count on self (max 5)
   PL:
751. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Sloth) — nazwa] 의뢰 대상 보호
   źródło: Passives.json :: dataList[id=1101021].name
   limit: do 40 znaków
   EN: Contract Target Protection
   PL:
752. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Sloth) — opis] 턴 종료 시 체력 비율이 가장 낮은 아군 1명에게 다음 턴에 [Agility] 1, [DefenseUp] 3 부여
   źródło: Passives.json :: dataList[id=1101021].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Agility], [DefenseUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn End: apply 1 [Agility] and 3 [DefenseUp] to 1 ally with the lowest HP percentage next turn
   PL:
753. [Kwestia głosowa [get_11010_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=get_11010_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Kwestia głosowa [get_11010_1] (Identity Acquisition)] 의뢰하신 생존자는 무사히 데려올테니까… 손가락은 치워주시겠어요…?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=get_11010_1].dlg
   limit: do 130 znaków
   EN: We'll rescue the survivor like you requested, so... can you stop pointing that finger at me...?
   PL:
755. [Kwestia głosowa [lobby_morning_11010_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=lobby_morning_11010_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Kwestia głosowa [lobby_morning_11010_1] (Morning Greeting)] …버, 벌써 아침이에요!? 갑옷입고 아침 조회시간에 맞추려면 지금부터 뛰어야…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=lobby_morning_11010_1].dlg
   limit: do 130 znaków
   EN: ... I-it's morning already?! I gotta run if I wanna suit up and make it to the morning assembly—
   PL:
757. [Kwestia głosowa [lobby_noon_11010_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=lobby_noon_11010_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [Kwestia głosowa [lobby_noon_11010_1] (Afternoon Greeting)] 필요한 서류가 꽤 많네요. 낮 동안 다 받아둬야 할텐데… 서둘러야겠어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=lobby_noon_11010_1].dlg
   limit: do 160 znaków
   EN: There's a lot of paperwork to be done. Hopefully we can take care of this process before the sun goes down... Let's hurry.
   PL:
759. [Kwestia głosowa [lobby_night_11010_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=lobby_night_11010_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [Kwestia głosowa [lobby_night_11010_1] (Evening Greeting)] 야밤의 구출 의뢰는 신중히 받는 편이 좋아요. 저희까지 위험에 빠지는 경우가 많거든요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=lobby_night_11010_1].dlg
   limit: do 140 znaków
   EN: Can't be too careful when taking on late night rescue contracts. It often ends up putting us in danger, too.
   PL:
761. [Kwestia głosowa [smalltalk_11010_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=smalltalk_11010_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Kwestia głosowa [smalltalk_11010_1] (Chatter #1)] 복장이 눈에 띄게 화려한 건 츠바이 기사단의 복식 때문도 있겠지만… 이러면 난전 속에서는 눈에 띄는 갑옷을 입은 저희에게 시선이 더 쏠려서 생존자를 무시한대요.\n망토가 거추장스럽다고 생각했는데… 그런 이유도 있더라고요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=smalltalk_11010_1].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Zwei Knights wear these gaudy armors not only because it's our uniform... but also because it draws attention away from our clients when the battle gets messy.\nAnd here I was, thinking that this cape was bothersome... I guess everything has a reason.
   PL:
763. [Kwestia głosowa [smalltalk_11010_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=smalltalk_11010_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Kwestia głosowa [smalltalk_11010_2] (Chatter #2)] 가끔 다른 협회 분들과 작전을 나가면 느끼는 건데… 대부분 누구를 지키거나 구하는 것에 큰 관심이 없는 것 같아요.\n의뢰비를 주었을 때만 움직이는 건 사실이지만… 저희만큼 의뢰인의 안전을 신경써주는 협회는 드물다는 거죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=smalltalk_11010_2].dlg
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There's something I realized whenever I go on joint operations with other Association Fixers... It's that most people don't care about protecting or saving someone.\nI know that we only move when we're paid to do so, but... our Association's the best when it comes to protecting their clients.
   PL:
765. [Kwestia głosowa [smalltalk_11010_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=smalltalk_11010_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Kwestia głosowa [smalltalk_11010_3] (Chatter #3)] 가끔 무리한 의뢰가 들어올 때가 있어요. 거절하고 싶은 마음은 굴뚝같지만…\n그럼에도 막대한 의뢰비를 준다면, 협회의 의지에 따라 저희 츠바이 해결사들은 의뢰를 거절할 수 없어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=smalltalk_11010_3].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sometimes, we receive contracts that are clearly above our pay grade. I hate taking those contracts, but...\nIf they pay enough, us Zwei Fixers have no choice but to do as our Association tells us to do.
   PL:
767. [Kwestia głosowa [smalltalk_11010_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=smalltalk_11010_4].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [Kwestia głosowa [smalltalk_11010_4] (Post-Uptie Chat 1)] 주변 사람들의 죽음에 점점 익숙해지는 제가 싫어요. 어쩔 수 없다는 걸 알고 있는데도…\n…아냐. 이렇게 약한 마음으로는 그날처럼 아무것도 지키지 못해.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=smalltalk_11010_4].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I hate myself for growing so accustomed to people dying around me. I know, I don't have a choice. But...\n... No. I can't be so weak-willed... I can't protect anything like this. Just like that day...
   PL:
769. [Kwestia głosowa [smalltalk_11010_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=smalltalk_11010_5].desc
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Kwestia głosowa [smalltalk_11010_5] (Post-Uptie Chat 2)] 만인의 안전을 바라는 게 잘못된 건 아니라고 생각해요.\n단지… 모두를 지키는 게 불가능할 뿐이죠. 소중한 사람을 지키는 것조차 어려운 곳이 이 도시잖아요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=smalltalk_11010_5].dlg
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I don't think there's anything wrong with wishing safety for everyone.\nIt's just that it's... impossible. It's the City. We can't even protect the people we love.
   PL:
771. [Kwestia głosowa [neglect_11010_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=neglect_11010_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [Kwestia głosowa [neglect_11010_1] (Idle)] …어? 어어! 혼자 돌아다니시면 위험해요!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=neglect_11010_1].dlg
   limit: do 120 znaków
   EN: ... Huh? O-oh! Please don't go wandering off on your own!
   PL:
773. [Kwestia głosowa [gacksung_11010_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=gacksung_11010_1].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Kwestia głosowa [gacksung_11010_1] (Uptying)] 걱정하지 마세요. 의뢰 대상인 당신만큼은… 반드시 지켜줄테니까요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=gacksung_11010_1].dlg
   limit: do 120 znaków
   EN: Don't worry. You're my target... so I'll protect you no matter what.
   PL:
775. [Kwestia głosowa [formation_11010_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=formation_11010_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [Kwestia głosowa [formation_11010_1] (Deployment)] 퀘스트… 확인했어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=formation_11010_1].dlg
   limit: do 120 znaków
   EN: Quest... confirmed.
   PL:
777. [Kwestia głosowa [battleentry_11010_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battleentry_11010_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Kwestia głosowa [battleentry_11010_1] (Stage Entry)] 이 대검은 당신의 검이자 방패가 되어…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battleentry_11010_1].dlg
   limit: do 120 znaków
   EN: Thus becomes your blade and shield, this greatsword...
   PL:
779. [Kwestia głosowa [battle_select_11010_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_select_11010_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [Kwestia głosowa [battle_select_11010_1] (Viewed in Battle)] 서류는 다 제출했을 텐데… 무슨 일이신가요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_select_11010_1].dlg
   limit: do 120 znaków
   EN: I thought I submitted everything...? What's wrong?
   PL:
781. [Kwestia głosowa [battle_endcommand_11010_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_endcommand_11010_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Kwestia głosowa [battle_endcommand_11010_1] (Commencing Attack)] 신병 확보하겠습니다…!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_endcommand_11010_1].dlg
   limit: do 120 znaków
   EN: Securing personnel...!
   PL:
783. [Kwestia głosowa [battle_enemy_break_11010_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_enemy_break_11010_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Kwestia głosowa [battle_enemy_break_11010_1] (Enemy Stagger)] 이 틈에 제 뒤로…!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_enemy_break_11010_1].dlg
   limit: do 120 znaków
   EN: Get behind me, now...!
   PL:
785. [Kwestia głosowa [battle_break_11010_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_break_11010_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Kwestia głosowa [battle_break_11010_1] (Staggered)] 으윽…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_break_11010_1].dlg
   limit: do 120 znaków
   EN: Nngh...
   PL:
787. [Kwestia głosowa [battle_kill_11010_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_kill_11010_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [Kwestia głosowa [battle_kill_11010_1] (Enemy Killed)] 위험 인물 배제…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_kill_11010_1].dlg
   limit: do 120 znaków
   EN: Excluding high-risk individuals...
   PL:
789. [Kwestia głosowa [battle_dead_11010_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_dead_11010_1].desc
   (powtórzenie elementu 371 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Kwestia głosowa [battle_dead_11010_1] (Death)] 저는 괜찮으니… 지금이라도… 멀리 도망치세요….
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_dead_11010_1].dlg
   limit: do 120 znaków
   EN: I'll be fine... so run... get as far away as you can from here...
   PL:
791. [Kwestia głosowa [choice_success_p_11010_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=choice_success_p_11010_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Kwestia głosowa [choice_success_p_11010_2] (Check Passed)] 한 명 정도는 더… 이번만 도와드리는 거예요. 이 이상은 안돼요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=choice_success_p_11010_2].dlg
   limit: do 120 znaków
   EN: I can protect one more person, yeah... But only this time, okay? I can't do this again.
   PL:
793. [Kwestia głosowa [choice_fail_n_11010_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=choice_fail_n_11010_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [Kwestia głosowa [choice_fail_n_11010_1] (Check Failed)] …죄송하지만, 이건 의뢰에 없던 일이었어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=choice_fail_n_11010_1].dlg
   limit: do 120 znaków
   EN: ... I'm sorry. This was not a part of my contract.
   PL:
795. [Kwestia głosowa [battle_clear_11010_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_clear_11010_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Kwestia głosowa [battle_clear_11010_1] (Victory Cry)] 약간의 희생이 있었지만… 어쩔 수 없는 거겠죠. 모두를 지키는 방패가 될 순 없으니까요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_clear_11010_1].dlg
   limit: do 140 znaków
   EN: We suffered some losses, but... I guess it couldn't be helped. There's only so much a shield can protect.
   PL:
797. [Kwestia głosowa [battle_clear_ex_11010_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_clear_ex_11010_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Kwestia głosowa [battle_clear_ex_11010_1] (Extra Conditions Fulfilled)] 생존자를 모두 구출했어요. 열심히 하다보니 이런 날도… 다 있네요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_clear_ex_11010_1].dlg
   limit: do 120 znaków
   EN: We actually rescued everyone. I guess days of hard work does pay off... sometimes.
   PL:
799. [Kwestia głosowa [battle_defeat_11010_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_defeat_11010_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Kwestia głosowa [battle_defeat_11010_1] (Defeat Wail)] 의뢰는… 실패했어요. 아무도 지키지 못했어… 전멸이야…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_ZweiWest_11010.json :: dataList[id=battle_defeat_11010_1].dlg
   limit: do 120 znaków
   EN: We... failed the contract. I couldn't protect anyone... They're... all dead...
   PL:

## [000] Devyat' Assoc. North Section 3 — Sinclair — 북부 제뱌찌 협회 3과
- ID Tożsamości: `11011` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 73 · szybkość: 2–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Rupture

801. [Karta Tożsamości — tytuł] 북부 제뱌찌 협회\n3과
   źródło: Personalities.json :: dataList[id=11011].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Devyat' Assoc.\nNorth Section 3
   PL:
802. [Karta Tożsamości — nazwa] 싱클레어
   źródło: Personalities.json :: dataList[id=11011].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Karta Tożsamości — nazwa z tytułem] 싱클레어
   źródło: Personalities.json :: dataList[id=11011].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Karta Tożsamości — opis] 싱클레어의 열한번째 인격
   źródło: Personalities.json :: dataList[id=11011].desc
   limit: do 120 znaków
   EN: Sinclair’s 11th Identity
   PL:
805. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 딜리버리 캐리어 - 붕괴 망치
   źródło: Skills_personality-10.json :: dataList[id=1101101].levelList[level=1].name ; dataList[id=1101101].levelList[level=2].name ; dataList[id=1101101].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Courier Trunk - Decay Hammer
   PL:
806. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 적중 시 효과로 [Burst] 횟수를 부여하지 않는 대신, [DefenseDown] 2 부여 (코인 당 1회)
   źródło: Skills_personality-10.json :: dataList[id=1101101].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst], [DefenseDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not inflict [Burst] with this Skill's On Hit effects; instead, it inflicts 2 [DefenseDown] (once per Coin)
   PL:
807. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DevyatDimensionalSackSinclair] 1 얻음\n- [DevyatDimensionalSackSinclair]가 15 미만이면, [DevyatDimensionalSackSinclair] 1 추가로 얻음
   źródło: Skills_personality-10.json :: dataList[id=1101101].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1101101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1101101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: [OnSucceedAttack] Gain 1 [DevyatDimensionalSackSinclair]\n- If this unit has less than 15 [DevyatDimensionalSackSinclair], gain 1 additional [DevyatDimensionalSackSinclair]
   PL:
808. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1101101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL:
809. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [DevyatDimensionalSackSinclair]가 10 이상이거나, 대상의 [Burst]이 6 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 적중 시 효과로 [Burst] 횟수를 부여하지 않는 대신, [DefenseDown] 2 부여 (코인 당 1회)
   źródło: Skills_personality-10.json :: dataList[id=1101101].levelList[level=2].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [DevyatDimensionalSackSinclair], [Burst], [WhenUse], [DefenseDown]
   znaczenie tagów: [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair; [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: At 10+ [DevyatDimensionalSackSinclair], or if target has 6+ [Burst], Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Count with its On Hit effects; instead, it inflicts 2 [DefenseDown] (once per Coin)
   PL:
810. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가\n- [DevyatDimensionalSackSinclair]가 15 이상이면, [Burst] 횟수 1 추가 증가
   źródło: Skills_personality-10.json :: dataList[id=1101101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1101101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Burst], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count\n- At 15+ [DevyatDimensionalSackSinclair], inflict +1 additional [Burst] Count
   PL:
811. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [DevyatDimensionalSackSinclair] 10 또는 대상의 [Burst] 6당 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 적중 시 효과로 [Burst] 횟수를 부여하지 않는 대신, [DefenseDown] 2 부여 (코인 당 1회)
   źródło: Skills_personality-10.json :: dataList[id=1101101].levelList[level=4].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [DevyatDimensionalSackSinclair], [Burst], [WhenUse], [DefenseDown]
   znaczenie tagów: [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair; [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Coin Power +1 for every 10 [DevyatDimensionalSackSinclair] on self or for every 6 [Burst] on target (max 2)\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Count with its On Hit effects; instead, it inflicts 2 [DefenseDown] (once per Coin)
   PL:
812. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 딜리버리 캐리어 - 돌파 가젯
   źródło: Skills_personality-10.json :: dataList[id=1101102].levelList[level=1].name ; dataList[id=1101102].levelList[level=2].name ; dataList[id=1101102].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 50 znaków
   EN: Courier Trunk - Demolition Gadget
   PL:
813. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 적중 시 효과로 [Burst], [Burst] 횟수를 부여하지 않는 대신, [DefenseDown] 2 부여 (코인 당 1회)
   źródło: Skills_personality-10.json :: dataList[id=1101102].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst], [DefenseDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not inflict [Burst] or [Burst] Count with this Skill's On Hit effects; instead, it inflicts 2 [DefenseDown] (once per Coin)
   PL:
814. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DevyatDimensionalSackSinclair] 1 얻음\n- [DevyatDimensionalSackSinclair]가 15 미만이면, [DevyatDimensionalSackSinclair] 2 추가로 얻음
   źródło: Skills_personality-10.json :: dataList[id=1101102].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1101102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1101102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: [OnSucceedAttack] Gain 1 [DevyatDimensionalSackSinclair]\n- If this unit has less than 15 [DevyatDimensionalSackSinclair], gain 2 additional [DevyatDimensionalSackSinclair]
   PL:
815. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-10.json :: dataList[id=1101102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
816. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_personality-10.json :: dataList[id=1101102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL:
817. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [DevyatDimensionalSackSinclair]가 10 이상이거나, 대상의 [Burst]이 6 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 적중 시 효과로 [Burst], [Burst] 횟수를 부여하지 않는 대신, [DefenseDown] 2 부여 (코인 당 1회)\n[WhenUse] [DevyatDimensionalSackSinclair]가 20 이하면, 다음 턴에 [Agility] 1 얻음 (턴 당 최대 1)
   źródło: Skills_personality-10.json :: dataList[id=1101102].levelList[level=2].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [DevyatDimensionalSackSinclair], [Burst], [WhenUse], [DefenseDown], [Agility]
   znaczenie tagów: [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair; [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Agility] = 신속 / Haste
   EN: At 10+ [DevyatDimensionalSackSinclair], or if target has 6+ [Burst], Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] or [Burst] Count with its On Hit effects; instead, it inflicts 2 [DefenseDown] (once per Coin)\n[WhenUse] At 20- [DevyatDimensionalSackSinclair], gain 1 [Agility] next turn (once per turn)
   PL:
818. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여\n- [DevyatDimensionalSackSinclair]가 15 이상이면, [Burst] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1101102].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Burst], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: [OnSucceedAttack] Inflict 2 [Burst]\n- At 15+ [DevyatDimensionalSackSinclair], inflict +1 [Burst] Count
   PL:
819. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여\n- [DevyatDimensionalSackSinclair]가 15 이상이면, [Burst] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1101102].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Burst], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: [OnSucceedAttack] Inflict 3 [Burst]\n- At 15+ [DevyatDimensionalSackSinclair], inflict +1 [Burst] Count
   PL:
820. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [DevyatDimensionalSackSinclair] 10 또는 대상의 [Burst] 6당 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 적중 시 효과로 [Burst], [Burst] 횟수를 부여하지 않는 대신, [DefenseDown] 2 부여 (코인 당 1회)\n[WhenUse] [DevyatDimensionalSackSinclair]가 30 이하면, 다음 턴에 [Agility] 1 얻음 (턴 당 최대 1)
   źródło: Skills_personality-10.json :: dataList[id=1101102].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [DevyatDimensionalSackSinclair], [Burst], [WhenUse], [DefenseDown], [Agility]
   znaczenie tagów: [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair; [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Agility] = 신속 / Haste
   EN: Coin Power +1 for every 10 [DevyatDimensionalSackSinclair] on self or for every 6 [Burst] on target (max 2)\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] or [Burst] Count with its On Hit effects; instead, it inflicts 2 [DefenseDown] (once per Coin)\n[WhenUse] At 30- [DevyatDimensionalSackSinclair], gain 1 [Agility] next turn (once per turn)
   PL:
821. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여\n- [DevyatDimensionalSackSinclair]가 15 이상이면, [Burst] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-10.json :: dataList[id=1101102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Burst], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: [OnSucceedAttack] Inflict 2 [Burst]\n- At 15+ [DevyatDimensionalSackSinclair], inflict +<style="highlight">2</style> [Burst] Count
   PL:
822. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여\n- [DevyatDimensionalSackSinclair]가 15 이상이면, [Burst] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-10.json :: dataList[id=1101102].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Burst], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: [OnSucceedAttack] Inflict 3 [Burst]\n- At 15+ [DevyatDimensionalSackSinclair], inflict +<style="highlight">2</style> [Burst] Count
   PL:
823. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 플루드니차... 부탁해요!
   źródło: Skills_personality-10.json :: dataList[id=1101103].levelList[level=3].name ; dataList[id=1101103].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Poludnitsa... I trust you!
   PL:
824. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [DevyatDimensionalSackSinclair]가 10 이상이거나, 대상의 [Burst]이 6 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 적중 시 효과로 [Burst], [Burst] 횟수를 부여하지 않는 대신, 마지막 코인 위력 +2\n[WhenUse] 대상의 [Burst]이 15 이상이면, [DevyatDimensionalSackSinclair] 1 당 마지막 코인의 피해량 +3% (최대 90%)
   źródło: Skills_personality-10.json :: dataList[id=1101103].levelList[level=3].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [DevyatDimensionalSackSinclair], [Burst], [WhenUse]
   znaczenie tagów: [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair; [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: At 10+ [DevyatDimensionalSackSinclair], or if target has 6+ [Burst], Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] or [Burst] Count with its On Hit effects; instead, the final Coin gains +2 Coin Power\n[WhenUse] If target has 15+ [Burst], deal +3% damage for every [DevyatDimensionalSackSinclair] (max 90%)
   PL:
825. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가\n- [DevyatDimensionalSackSinclair] 10 당 [Burst] 횟수 1 추가로 증가 (최대 2)
   źródło: Skills_personality-10.json :: dataList[id=1101103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Burst], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count\n- Inflict +1 additional [Burst] Count for every 10 [DevyatDimensionalSackSinclair] (max 2)
   PL:
826. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여\n- [DevyatDimensionalSackSinclair] 10 당 [Burst] 1 추가로 부여 (최대 2)
   źródło: Skills_personality-10.json :: dataList[id=1101103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Burst], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: [OnSucceedAttack] Inflict 3 [Burst]\n- Inflict +1 additional [Burst] for every 10 [DevyatDimensionalSackSinclair] (max 2)
   PL:
827. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 이 스킬의 마지막 코인 위력이 증가하는 효과가 발동하지 않았다면, 다음 턴에 [Agility] 1 얻음
   źródło: Skills_personality-10.json :: dataList[id=1101103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] If this Skill failed to increase the final Coin Power, gain 1 [Agility] next turn
   PL:
828. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [DevyatDimensionalSackSinclair] 10 또는 대상의 [Burst] 6당 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 적중 시 효과로 [Burst], [Burst] 횟수를 부여하지 않는 대신, 마지막 코인 위력 +4\n[WhenUse] 대상의 [Burst]이 15 이상이면, [DevyatDimensionalSackSinclair] 1 당 마지막 코인의 피해량 +4% (최대 120%)
   źródło: Skills_personality-10.json :: dataList[id=1101103].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [DevyatDimensionalSackSinclair], [Burst], [WhenUse]
   znaczenie tagów: [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair; [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: Coin Power +1 for every 10 [DevyatDimensionalSackSinclair] on self or for every 6 [Burst] on target (max 2)\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] or [Burst] Count with its On Hit effects; instead, the final Coin gains +4 Coin Power\n[WhenUse] If target has 15+ [Burst], deal +4% damage for every [DevyatDimensionalSackSinclair] (max 120%)
   PL:
829. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가\n- [DevyatDimensionalSackSinclair] 10 당 [Burst] 횟수 1 추가로 증가 (최대 <style="highlight">3</style>)
   źródło: Skills_personality-10.json :: dataList[id=1101103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Burst], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count\n- Inflict +1 additional [Burst] Count for every 10 [DevyatDimensionalSackSinclair] (max <style="highlight">3</style>)
   PL:
830. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여\n- [DevyatDimensionalSackSinclair] <style="highlight">8</style> 당 [Burst] 1 추가로 부여 (최대 <style="highlight">4</style>)
   źródło: Skills_personality-10.json :: dataList[id=1101103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Burst], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: [OnSucceedAttack] Inflict 3 [Burst]\n- Inflict +1 additional [Burst] for every <style="highlight">8</style> [DevyatDimensionalSackSinclair] (max <style="highlight">4</style>)
   PL:
831. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 이 스킬의 마지막 코인 위력이 증가하는 효과가 발동하지 않았다면, 다음 턴에 [Agility] 2 얻음
   źródło: Skills_personality-10.json :: dataList[id=1101103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] If this Skill's effect to raise its final Coin Power did not activate, gain 2 [Agility] next turn
   PL:
832. [Obrona (ulepszenia 1,4) — nazwa] 배달 지원 및 상황 통제 절차
   źródło: Skills_personality-10.json :: dataList[id=1101104].levelList[level=1].name ; dataList[id=1101104].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 9 · monety: 1 (+7)
   limit: do 60 znaków
   EN: Courier Assistance & Crisis Control System
   PL:
833. [Obrona (ulepszenie 1) — opis] [StartBattle] [DevyatDimensionalSackSinclair]가 15 이상이면, '자, 잠깐 정비 좀 할게요...!' 으로 발동함 (턴 당 1회)\n[StartBattle] 이 스킬로 발동 예정인 경우, 자신의 최대 체력의 ([DevyatDimensionalSackSinclair]/2)% 만큼 보호막을 얻음 (최대 15%, 턴 당 1회)
   źródło: Skills_personality-10.json :: dataList[id=1101104].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: [StartBattle] At 15+ [DevyatDimensionalSackSinclair], activate 'W-wait, I need to do some maintenance...!.' instead (once per turn)\n[StartBattle] If this Skill is to be activated, gain ([DevyatDimensionalSackSinclair] / 2)% of this unit's max HP as Shield (max 15%, once per turn)
   PL:
834. [Obrona (ulepszenie 4) — opis] [StartBattle] [DevyatDimensionalSackSinclair]가 15 이상이면, '자, 잠깐 정비 좀 할게요...!' 으로 발동함 (턴 당 1회)\n[StartBattle] 이 스킬로 발동 예정인 경우, 자신의 최대 체력의 <style="highlight">([DevyatDimensionalSackSinclair])</style>% 만큼 보호막을 얻음 (최대 <style="highlight">25</style>%, 턴 당 1회)
   źródło: Skills_personality-10.json :: dataList[id=1101104].levelList[level=4].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: [StartBattle] At 15+ [DevyatDimensionalSackSinclair], activate 'W-wait, I need to do some maintenance...!' instead (once per turn)\n[StartBattle] If this Skill is to be activated, gain <style="highlight">([DevyatDimensionalSackSinclair])%</style> of this unit's max HP as Shield (max <style="highlight">25%</style>, once per turn)
   PL:
835. [Obrona (ulepszenia 1,4) — nazwa] 자, 잠깐 정비 좀 할게요...!
   źródło: Skills_personality-10.json :: dataList[id=1101105].levelList[level=1].name ; dataList[id=1101105].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 9 · monety: 1 (+7)
   limit: do 60 znaków
   EN: W-wait, I need to do some maintenance...!
   PL:
836. [Obrona (ulepszenie 1) — opis] [StartBattle] 이 스킬로 발동 예정인 경우, 자신의 최대 체력의 ([DevyatDimensionalSackSinclair]/2)% 만큼 보호막을 얻음 (최대 15%, 턴 당 1회)\n[EndBattle] [Retreat] 발동
   źródło: Skills_personality-10.json :: dataList[id=1101105].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DevyatDimensionalSackSinclair], [EndBattle], [Retreat]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair; [EndBattle] = [턴 종료 시] / [Turn End]; [Retreat] = 전략적 휴식 복지 모드 / Strategic R&R Mode
   EN: [StartBattle] If this Skill is to be activated, gain ([DevyatDimensionalSackSinclair])% of this unit's max HP as Shield (max 15%, once per turn)\n[EndBattle] Activate [Retreat]
   PL:
837. [Obrona (ulepszenie 4) — opis] [StartBattle] 이 스킬로 발동 예정인 경우, 자신의 최대 체력의 <style="highlight">([DevyatDimensionalSackSinclair])</style>% 만큼 보호막을 얻음 (최대 <style="highlight">25</style>%, 턴 당 1회)\n[EndBattle] [Retreat] 발동
   źródło: Skills_personality-10.json :: dataList[id=1101105].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [DevyatDimensionalSackSinclair], [EndBattle], [Retreat]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair; [EndBattle] = [턴 종료 시] / [Turn End]; [Retreat] = 전략적 휴식 복지 모드 / Strategic R&R Mode
   EN: [StartBattle] If this Skill is to be activated, gain <style="highlight">([DevyatDimensionalSackSinclair])%</style> of this unit's max HP as Shield (max <style="highlight">25%</style>, once per turn)\n[EndBattle] Activate [Retreat]
   PL:
838. [Pasywka bojowa (od ulepszenia 1) — nazwa] 다음에는 제대로 배달할게요...
   źródło: Passives.json :: dataList[id=1101102].name
   limit: do 40 znaków
   EN: I'll do better next time...
   PL:
839. [Pasywka bojowa (od ulepszenia 1) — opis] <연속 전투 전용> '[Retreat]'가 발동하여 퇴각한 다음 다시 전투에 참여할 때, [DevyatDimensionalSackSinclair]가 절반으로 감소 (전투당 1회, 올림하여 처리)
   źródło: Passives.json :: dataList[id=1101102].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [Retreat], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [Retreat] = 전략적 휴식 복지 모드 / Strategic R&R Mode; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: <For Chain Battles> When, after Retreating using '[Retreat]', if this unit rejoins the battle, halve the [DevyatDimensionalSackSinclair] value (once per Encounter, rounded up)
   PL:
840. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — nazwa] 잠시만 부탁드려요...
   źródło: Passives.json :: dataList[id=1101101].name
   limit: do 40 znaków
   EN: A moment, please...
   PL:
841. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — opis] 턴 시작시 속도가 6 이상이거나 [Agility]을 보유하였다면, 자신의 최대 체력의 ([DevyatDimensionalSackSinclair])%만큼 보호막을 얻음 (최대 20%)
   źródło: Passives.json :: dataList[id=1101101].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Agility], [DevyatDimensionalSackSinclair]
   znaczenie tagów: [Agility] = 신속 / Haste; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair
   EN: Turn Start: At 6+ Speed, or if this unit has [Agility], gain ([DevyatDimensionalSackSinclair])% of this unit's max HP as Shield (max 20%)
   PL:
842. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 잠시만 부탁드려요...
   źródło: Passives.json :: dataList[id=1101111].name
   (powtórzenie elementu 840 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — opis] 턴 시작시 속도가 6 이상이거나 [Agility]을 보유하였다면, 자신의 최대 체력의 ([DevyatDimensionalSackSinclair])%만큼 보호막을 얻음 (최대 20%)\n퇴각 시, 다음 턴에 아군 둘에게 [ParryingResultUp] 1 부여 (대기 해제된 인격에게 우선으로 부여되며, 그 다음으로는 편성 순서가 빠른 순으로 적용)\n- [DevyatDimensionalSackSinclair] 15당 유지 턴 수 1 증가 (최대 2턴 증가)
   źródło: Passives.json :: dataList[id=1101111].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [DevyatDimensionalSackSinclair], [ParryingResultUp]
   znaczenie tagów: [Agility] = 신속 / Haste; [DevyatDimensionalSackSinclair] = 딜리버리 캐리어 - 싱클레어 / Courier Trunk - Sinclair; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Turn Start: At 6+ Speed, or if this unit has [Agility], gain ([DevyatDimensionalSackSinclair])% of this unit's max HP as Shield (max 20%)\nUpon Retreat, apply 1 [ParryingResultUp] to 2 allies next turn (prioritizes Substituted units first, then in Deployment order)\n- Lasts for 1 additional turn for every 15 [DevyatDimensionalSackSinclair] (2 more turns max)
   PL:
844. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Glut.) — nazwa] 신속 배달부
   źródło: Passives.json :: dataList[id=1101121].name
   limit: do 40 znaków
   EN: Speedy Courier
   PL:
845. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Glut.) — opis] 속도가 가장 빠른 아군 1명이 [Burst]이 부여된 적에게 공격 적중시 [DefenseDown] 1 부여 (턴 당 적 1명당 최대 3)
   źródło: Passives.json :: dataList[id=1101121].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Burst], [DefenseDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When 1 ally with the fastest Speed hits an enemy with [Burst], inflict 1 [DefenseDown] (3 times per enemy per turn)
   PL:
846. [Kwestia głosowa [get_11011_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=get_11011_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Kwestia głosowa [get_11011_1] (Identity Acquisition)] 이건 이거랑 묶어서 같이 배송하고… 경로 확인한 다음에… 이, 이번 집화처리는 왜 이렇게 복잡한 거예요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=get_11011_1].dlg
   limit: do 190 znaków
   EN: I think I can lump this package with that one, and... let's see where this one's gotta go... W-why is the sorting process so complicated this time?
   PL:
848. [Kwestia głosowa [lobby_morning_11011_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=lobby_morning_11011_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Kwestia głosowa [lobby_morning_11011_1] (Morning Greeting)] 요즘 밤 중에도 배송 의뢰를 자주 배정 받아서… 아침까지 잠을 영 못 잤네요.\n저는… 지금부터라도 조금 자야겠어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=lobby_morning_11011_1].dlg
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I haven't been sleeping well, with the recent surge of late-night delivery contracts...\nI'll try to get some sleep in now.
   PL:
850. [Kwestia głosowa [lobby_noon_11011_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=lobby_noon_11011_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Kwestia głosowa [lobby_noon_11011_1] (Afternoon Greeting)] 도시락 같은 걸 가져오시면 보통 배달하는 중에 얼어버리는 경우가 많아요.\n딜리버리 캐리어에 넣는 해결사 분들도 종종 있지만… 일단은 제뱌찌 협회 규칙에는 어긋나는 행동이라서요…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=lobby_noon_11011_1].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Boxed lunches usually end up freezing solid when we're making deliveries through the cold.\nThat's why some Fixers keep their lunches in the Courier Trunks they've been assigned, but... that's a violation of the Devyat' Association rules...
   PL:
852. [Kwestia głosowa [lobby_night_11011_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=lobby_night_11011_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Kwestia głosowa [lobby_night_11011_1] (Evening Greeting)] 밤길이 위험한 건 알지만… 그래도 가야 해요.\n뒷골목의 밤이 오기 전까지 배달해야 할 물품이 있거든요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=lobby_night_11011_1].dlg
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It's dangerous to travel at night, but... I don't have a choice.\nThere's a package that needs to be delivered before the Night in the Backstreets.
   PL:
854. [Kwestia głosowa [smalltalk_11011_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=smalltalk_11011_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Kwestia głosowa [smalltalk_11011_1] (Chatter #1)] 제뱌찌 협회의 해결사라면 각 구역의 문화는 잘 알아두는 편이 좋아요.\n배달을 빠르게 하는 것도 좋지만, 구역에 있는 날개나 조직의 금기를 어기지 않는 것도 중요하거든요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=smalltalk_11011_1].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It's important for Fixers of the Devyat' Association to keep themselves up-to-date about cultures of each District.\nSpeed is one thing, but we also have to be careful not to accidentally break a Taboo of a Wing or a Syndicate's rule.
   PL:
856. [Kwestia głosowa [smalltalk_11011_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=smalltalk_11011_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Kwestia głosowa [smalltalk_11011_2] (Chatter #2)] 자동차를 타고 배송하면 안 되냐구요? 음… 그런 걸 이용하는 것보다는 플루드니차가 안내해주는 지름길로 가는 게 대체로 빠를 걸요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=smalltalk_11011_2].dlg
   limit: do 220 znaków
   EN: Why don't I just drive there, you ask? Um... I'm pretty sure going on foot and following Poludnitsa's shortcut directions would get me there much faster than driving would.
   PL:
858. [Kwestia głosowa [smalltalk_11011_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=smalltalk_11011_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Kwestia głosowa [smalltalk_11011_3] (Chatter #3)] 대부분의 위기 상황은 플루드니차가 출력 제한을 해제해주면 이겨낼 수 있지만…\n그러면 배달비가 한 푼도 안 남기도 하고… 무엇보다 제 수명이 남아나지 않아서요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=smalltalk_11011_3].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I can survive most risky situations by having Poludnitsa disengage the output threshold.\nBut that'll deduct way too much money from my payout... If it doesn't kill me in the process.
   PL:
860. [Kwestia głosowa [smalltalk_11011_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=smalltalk_11011_4].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Kwestia głosowa [smalltalk_11011_4] (Post-Uptie Chat 1)] <color=#9eada4><size=60%><i>[전방 200m 앞, 조직 간 분쟁 발생. 배송 지연 우려. 경로를 재탐색합니다.]</i></size></color> 오늘따라 길이 자주 바뀌네요… 그럼 왼쪽 길인가?\n<color=#9eada4><size=60%><i>[새로운 경로로 안내합니다]</i></size></color> 건물 위로… 뛰라구요!?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=smalltalk_11011_4].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <color=#9eada4>, <size=60%>, <i>, </i>, </size>, </color>, \n
   EN: <color=#9eada4><size=60%><i>[Possible delivery delay detected: Syndicate altercation 200m ahead. Rerouting.]</i></size></color>\nLots of route adjustments today, huh... Left turn, then?\n<color=#9eada4><size=60%><i>[New route discovered; navigating courier.]</i></size></color> You want me to... <i>scale</i> the building?!
   PL:
862. [Kwestia głosowa [smalltalk_11011_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=smalltalk_11011_5].desc
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Kwestia głosowa [smalltalk_11011_5] (Post-Uptie Chat 2)] 보통 저희를 습격하는 건 차원가방에 대해 아는 게 없는 뒷골목의 하급 조직원들이죠. 딜리버리 캐리어 안에 있는 물건은 보안 모드 때문에 못 가져가는데.\n손가락의 조직원 분들은… 고객으로 만날 때가 더 많죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=smalltalk_11011_5].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Only lower-rung Syndicate henchmen who don't know about these dimensional bags are dumb enough to attack us. Courier Trunks are locked by Protection Mode anyway, so...\nOh, what about members of the Fingers? They're... we usually meet them as our clients.
   PL:
864. [Kwestia głosowa [neglect_11011_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=neglect_11011_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Kwestia głosowa [neglect_11011_1] (Idle)] …플루드니차. 심심한데 노래라도 틀어주면 안돼요? <color=#9eada4><size=60%><i>[플루드니차는 해당 기능을 지원하지 않습니다.]</i></size></color> 어? 저번에 로쟈 씨가… <color=#9eada4><size=60%><i>[정정. 본 AI는 해당 기능을 지원하지 않습니다.]</i></size></color>
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=neglect_11011_1].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#9eada4>, <size=60%>, <i>, </i>, </size>, </color>, \n
   EN: Poludnitsa, I'm bored. Can you play me a song?\n<color=#9eada4><size=60%><i>[Poludnitsa does not support the requested functionality.]</i></size></color>\nHuh? But Miss Rodya said—\n<color=#9eada4><size=60%><i>[Correction. This AI model does not support the requested functionality.]</i></size></color>
   PL:
866. [Kwestia głosowa [gacksung_11011_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=gacksung_11011_1].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
867. [Kwestia głosowa [gacksung_11011_1] (Uptying)] 으… 쓰기 싫었는데… 시간 안에 지나가려면…! 플루드니차, 모드 전환! <color=#9eada4><size=60%><i>[해머 모드 전환. 붕괴입자의 흔들림에 맞춰 강하게 휘두르십시오.]</i></size></color>
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=gacksung_11011_1].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#9eada4>, <size=60%>, <i>, </i>, </size>, </color>, \n
   EN: Ugh, I really hoped it wouldn't have to come to this, but I need to get there in time...! Poludnitsa, engage mode conversion!\n<color=#9eada4><size=60%><i>[Hammer mode engaged. Swing to the undulation of decay particles.]</i></size></color>
   PL:
868. [Kwestia głosowa [formation_11011_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=formation_11011_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Kwestia głosowa [formation_11011_1] (Deployment)] 새로운 배달 의뢰인가요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=formation_11011_1].dlg
   limit: do 120 znaków
   EN: Is it a new delivery order?
   PL:
870. [Kwestia głosowa [battleentry_11011_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battleentry_11011_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Kwestia głosowa [battleentry_11011_1] (Stage Entry)] 다음 배송지는…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battleentry_11011_1].dlg
   limit: do 120 znaków
   EN: My next destination is...
   PL:
872. [Kwestia głosowa [battle_select_11011_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_select_11011_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
873. [Kwestia głosowa [battle_select_11011_1] (Viewed in Battle)] 어… 부르셨어요? 혹시 제뱌찌를 통해 주문한 물품이라도…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_select_11011_1].dlg
   limit: do 120 znaków
   EN: Uh... did you call me? Oh, did you order something through the Devyat'?
   PL:
874. [Kwestia głosowa [battle_endcommand_11011_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_endcommand_11011_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Kwestia głosowa [battle_endcommand_11011_1] (Commencing Attack)] 아직 안 늦었어…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_endcommand_11011_1].dlg
   limit: do 120 znaków
   EN: I still have time...
   PL:
876. [Kwestia głosowa [battle_enemy_break_11011_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_enemy_break_11011_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [Kwestia głosowa [battle_enemy_break_11011_1] (Enemy Stagger)] 비켜주시면 안돼요…?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_enemy_break_11011_1].dlg
   limit: do 120 znaków
   EN: Can you clear the way, please...?
   PL:
878. [Kwestia głosowa [battle_break_11011_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_break_11011_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Kwestia głosowa [battle_break_11011_1] (Staggered)] 으윽…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_break_11011_1].dlg
   (powtórzenie elementu 786 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
880. [Kwestia głosowa [battle_kill_11011_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_kill_11011_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [Kwestia głosowa [battle_kill_11011_1] (Enemy Killed)] …비켜달라고 했잖아요!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_kill_11011_1].dlg
   limit: do 120 znaków
   EN: ... I said move!
   PL:
882. [Kwestia głosowa [battle_dead_11011_1] — sytuacja] 본인 사망 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_dead_11011_1].desc
   limit: do 120 znaków
   EN: Death #1
   PL:
883. [Kwestia głosowa [battle_dead_11011_1] (Death #1)] 플루드니차… 살려주세… <color=#9eada4><size=60%><i>[활로 개척 실패. 담당자가 부재중입니다. 플루드니차, 보안 모드 작동.]</i></size></color>
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_dead_11011_1].dlg
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#9eada4>, <size=60%>, <i>, </i>, </size>, </color>
   EN: Poludnitsa... help... <color=#9eada4><size=60%><i>[Pathfinding failed. Courier absence detected. Poludnitsa, engaging Protection Mode.]</i></size></color>
   PL:
884. [Kwestia głosowa [battle_dead_11011_2] — sytuacja] 본인 사망 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_dead_11011_2].desc
   limit: do 120 znaków
   EN: Death #2
   PL:
885. [Kwestia głosowa [battle_dead_11011_2] (Death #2)] 시, 싫어요! 한 번만 봐주세요! 이때까지 잘… <color=#9eada4><size=60%><i>[통보. 배달 실패. 잠시 후 담당자를 수거합니다. 당신의 노고에 감사드립니다. 플루드니차, 보안 모드 작동.]</i></size></color>
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_dead_11011_2].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#9eada4>, <size=60%>, <i>, </i>, </size>, </color>
   EN: N-no! Please, please give me another chance! I've never been late bef— <color=#9eada4><size=60%><i>[Update. Delivery failed. The courier will be collected shortly. Thank you for your service. Poludnitsa, engaging Protection Mode.]</i></size></color>
   PL:
886. [Kwestia głosowa [choice_success_p_11011_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=choice_success_p_11011_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [Kwestia głosowa [choice_success_p_11011_2] (Check Passed)] …다음엔 이런 심부름은 안 해드릴 거예요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=choice_success_p_11011_2].dlg
   limit: do 120 znaków
   EN: ... I'm not running an errand like this for you again.
   PL:
888. [Kwestia głosowa [choice_fail_n_11011_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=choice_fail_n_11011_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [Kwestia głosowa [choice_fail_n_11011_1] (Check Failed)] 바, 바빠서 어쩔 수 없었어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=choice_fail_n_11011_1].dlg
   limit: do 120 znaków
   EN: I-I'm busy, okay?
   PL:
890. [Kwestia głosowa [battle_clear_11011_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_clear_11011_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
891. [Kwestia głosowa [battle_clear_11011_1] (Victory Cry)] 으아아아! 주문하신 상품 배송 완료했어요! 저, 안 늦었죠? 아직 배송 예정 시간 안 지난 거죠?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_clear_11011_1].dlg
   limit: do 130 znaków
   EN: AAAHHHHH! Your package has been delivered! I'm not late, am I? I'm on time for the delivery, right?
   PL:
892. [Kwestia głosowa [battle_clear_ex_11011_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_clear_ex_11011_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [Kwestia głosowa [battle_clear_ex_11011_1] (Extra Conditions Fulfilled)] 주문하신 상품을 예정된 시간보다 일찍 배송할 수 있겠네요. 의뢰인 분이 좋아하시겠어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_clear_ex_11011_1].dlg
   limit: do 120 znaków
   EN: This package will be delivered earlier than expected. The client will be happy to hear that.
   PL:
894. [Kwestia głosowa [battle_defeat_11011_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_defeat_11011_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
895. [Kwestia głosowa [battle_defeat_11011_1] (Defeat Wail)] 헉… 헉… 거, 거의 다 왔어요, 플루드니차! 조금만 더 가면 된다구요! 5분만 기다려 주시면…!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Devjat_11011.json :: dataList[id=battle_defeat_11011_1].dlg
   limit: do 120 znaków
   EN: Pant... pant... I-I'm almost there, Poludnitsa! I just need five more minutes, please...!
   PL:

## [000] The Middle Little Brother — Sinclair — 중지 작은 아우
- ID Tożsamości: `11012` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 92 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Bleed

896. [Karta Tożsamości — tytuł] 중지\n작은 아우
   źródło: Personalities.json :: dataList[id=11012].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Middle\nLittle Brother
   PL:
897. [Karta Tożsamości — nazwa] 싱클레어
   źródło: Personalities.json :: dataList[id=11012].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Karta Tożsamości — nazwa z tytułem] 싱클레어
   źródło: Personalities.json :: dataList[id=11012].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [Karta Tożsamości — opis] 싱클레어의 열두번째 인격
   źródło: Personalities.json :: dataList[id=11012].desc
   limit: do 120 znaków
   EN: Sinclair’s 12th Identity
   PL:
900. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 네 놈이냐!
   źródło: Skills_personality-10.json :: dataList[id=1101201].levelList[level=1].name ; dataList[id=1101201].levelList[level=2].name ; dataList[id=1101201].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Is it You?!
   PL:
901. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 2를 얻음\n[WhenUse] 자신의 정신력 5 회복
   źródło: Skills_personality-10.json :: dataList[id=1101201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +2 [Aggro] to this Skill Slot next turn\n[WhenUse] Heal 5 SP on self
   PL:
902. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 1 부여
   źródło: Skills_personality-10.json :: dataList[id=1101201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 1 [Laceration]
   PL:
903. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 1 부여
   źródło: Skills_personality-10.json :: dataList[id=1101201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 902 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
904. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">대상의 [Laceration]이 6 이상이면 코인 위력 +1</style>\n[WhenUse] 다음 턴에 이 슬롯이 [Aggro] <style="highlight">3</style>을 얻음\n[WhenUse] 자신의 정신력 5 회복
   źródło: Skills_personality-10.json :: dataList[id=1101201].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [WhenUse], [Aggro]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: <style="highlight">If target has 6+ [Laceration], Coin Power +1</style>\n[WhenUse] Gain +<style="highlight">3</style> [Aggro] to this Skill Slot next turn\n[WhenUse] Heal 5 SP on self
   PL:
905. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack]</style> [Laceration] 1 부여
   źródło: Skills_personality-10.json :: dataList[id=1101201].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack]</style> Inflict 1 [Laceration]
   PL:
906. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack]</style> [Laceration] 1 부여
   źródło: Skills_personality-10.json :: dataList[id=1101201].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 905 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Laceration]이 6 이상이면 코인 위력 +1\n[WhenUse] 다음 턴에 이 슬롯이 [Aggro] <style="highlight">5</style>를 얻음\n[WhenUse] 자신의 정신력 5 회복\n<style="highlight">- 정신력이 최대일 경우, 이 효과 대신 합 위력 +1</style>
   źródło: Skills_personality-10.json :: dataList[id=1101201].levelList[level=4].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [WhenUse], [Aggro]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: If target has 6+ [Laceration], Coin Power +1\n[WhenUse] Gain +<style="highlight">5</style> [Aggro] to this Skill Slot next turn\n[WhenUse] Heal 5 SP on self\n<style="highlight">- At max SP, gain Clash Power +1 instead</style>
   PL:
908. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-10.json :: dataList[id=1101201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]<style="highlight"></style>
   PL:
909. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-10.json :: dataList[id=1101201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 908 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 배로 먹여주마
   źródło: Skills_personality-10.json :: dataList[id=1101202].levelList[level=1].name ; dataList[id=1101202].levelList[level=2].name ; dataList[id=1101202].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Payback with Interest
   PL:
911. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 2를 얻음\n[StartBattle] (가장 높은 공명 수/3)만큼 이 스킬의 공격 레벨이 증가 (최대 2, 소수점 버림)
   źródło: Skills_personality-10.json :: dataList[id=1101202].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [StartBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [WhenUse] Gain +2 [Aggro] to this Skill Slot next turn\n[StartBattle] This Skill gains (highest Reson. / 3) Offense Level (max 2, rounded down)
   PL:
912. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-10.json :: dataList[id=1101202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
913. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] 이 스킬을 포함한 공명이 4 이상이면, 피해량 +10%
   źródło: Skills_personality-10.json :: dataList[id=1101202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: At 4+ Reson. that includes this Skill, deal +10% damage
   PL:
914. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 다음 턴에 이 슬롯이 [Aggro] <style="highlight">3</style>을 얻음\n[StartBattle] (가장 높은 공명 수/<style="highlight">2</style>)만큼 이 스킬의 공격 레벨이 증가 (최대 <style="highlight">3</style>, 소수점 버림)
   źródło: Skills_personality-10.json :: dataList[id=1101202].levelList[level=2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [WhenUse], [Aggro], [StartBattle]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [StartBattle] = [전투 시작시] / [Combat Start]
   EN: <style="highlight">If target has 6+ [Laceration], Coin Power +1</style>\n[WhenUse] Gain +<style="highlight">3</style> [Aggro] to this Skill Slot next turn\n[StartBattle] This Skill gains (highest Reson. / <style="highlight">2</style>) Offense Level (max <style="highlight">3</style>, rounded down)
   PL:
915. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-10.json :: dataList[id=1101202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1101202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]<style="highlight"></style>
   PL:
916. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] 이 스킬을 포함한 공명이 4 이상이면, 피해량 <style="highlight">+15%</style>
   źródło: Skills_personality-10.json :: dataList[id=1101202].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: At 4+ Reson. that includes this Skill, deal <style="highlight">+15%</style> damage
   PL:
917. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WhenUse] 다음 턴에 이 슬롯이 [Aggro] <style="highlight">5</style>를 얻음\n[StartBattle] (가장 높은 공명 수/2)만큼 이 스킬의 공격 레벨이 증가 (최대 3, 소수점 버림)\n<style="highlight">- 해당 공명에 완전 공명이 포함되어 있으면, 위 효과로 증가한 값이 2배로 적용</style>
   źródło: Skills_personality-10.json :: dataList[id=1101202].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [WhenUse], [Aggro], [StartBattle]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [StartBattle] = [전투 시작시] / [Combat Start]
   EN: If target has 6+ [Laceration], Coin Power +1\n[WhenUse] Gain +<style="highlight">5</style> [Aggro] to this Skill Slot next turn\n[StartBattle] This Skill gains (highest Reson. / 2) Offense Level (max 3, rounded down)\n<style="highlight">- If the said Reson. includes an A-Reson., double the Offense Level gained from the above effect</style>
   PL:
918. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] 이 스킬을 포함한 공명이 <style="highlight">3</style> 이상이면, 피해량 <style="highlight">+20%</style>
   źródło: Skills_personality-10.json :: dataList[id=1101202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: At <style="highlight">3</style>+ Reson. that includes this Skill, deal <style="highlight">+20%</style> damage
   PL:
919. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 똑똑히 새겨라
   źródło: Skills_personality-10.json :: dataList[id=1101203].levelList[level=3].name ; dataList[id=1101203].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Write 'em all down
   PL:
920. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [VengeanceBookSinclair] 2당 피해량 +1% (최대 15%)\n대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[StartBattle] (가장 높은 공명 수/2)만큼 이 스킬의 공격 레벨이 증가 (최대 3, 소수점 버림)
   źródło: Skills_personality-10.json :: dataList[id=1101203].levelList[level=3].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [VengeanceBookSinclair], [Laceration], [StartBattle]
   znaczenie tagów: [VengeanceBookSinclair] = 앙갚음 장부 [싱클레어] / Book of Vengeance [Sinclair]; [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]
   EN: Deal +1% damage for every 2 [VengeanceBookSinclair] (max 15%)\nIf target has 6+ [Laceration], Coin Power +1\n[StartBattle] This Skill gains (highest Reson. / 2) Offense Level (max 3, rounded down)
   PL:
921. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-10.json :: dataList[id=1101203].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
922. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 이 스킬을 포함한 공명당 피해량 +2.5% (최대 15%)
   źródło: Skills_personality-10.json :: dataList[id=1101203].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +2.5% damage for every Reson. that includes this Skill (max 15%)
   PL:
923. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [VengeanceBookSinclair] 10당 피해량 +7.5% (최대 22.5%)
   źródło: Skills_personality-10.json :: dataList[id=1101203].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [VengeanceBookSinclair]
   znaczenie tagów: [VengeanceBookSinclair] = 앙갚음 장부 [싱클레어] / Book of Vengeance [Sinclair]
   EN: Deal +7.5% damage for every 10 [VengeanceBookSinclair] (max 22.5%)
   PL:
924. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [VengeanceBookSinclair] <style="highlight">1</style>당 피해량 +1% (최대 <style="highlight">30%</style>)\n<style="highlight">대상의 [Laceration] 6당, 코인 위력 +1 (최대 2)</style>\n[StartBattle] (가장 높은 공명 수/2)만큼 이 스킬의 공격 레벨이 증가 (최대 3, 소수점 버림)\n<style="highlight">- 해당 공명에 완전 공명이 포함되어 있으면, 위 효과로 증가한 값이 2배로 적용</style>
   źródło: Skills_personality-10.json :: dataList[id=1101203].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [VengeanceBookSinclair], [Laceration], [StartBattle]
   znaczenie tagów: [VengeanceBookSinclair] = 앙갚음 장부 [싱클레어] / Book of Vengeance [Sinclair]; [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]
   EN: Deal +1% damage for every <style="highlight">1</style> [VengeanceBookSinclair] (max <style="highlight">30%</style>)\n<style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[StartBattle] This Skill gains (highest Reson. / 2) Offense Level (max 3, rounded down)\n<style="highlight">- If the said Reson. includes an A-Reson., double the Offense Level gained from the above effect</style>
   PL:
925. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">4</style> 부여
   źródło: Skills_personality-10.json :: dataList[id=1101203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">4</style> [Laceration]
   PL:
926. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 이 스킬을 포함한 공명당 피해량 <style="highlight">+5%</style> (최대 <style="highlight">30%</style>)
   źródło: Skills_personality-10.json :: dataList[id=1101203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal <style="highlight">+5%</style> damage for every Reson. that includes this Skill (max <style="highlight">30%</style>)
   PL:
927. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [VengeanceBookSinclair] 10당 피해량 <style="highlight">+15%</style> (최대 <style="highlight">45%</style>)
   źródło: Skills_personality-10.json :: dataList[id=1101203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [VengeanceBookSinclair]
   znaczenie tagów: [VengeanceBookSinclair] = 앙갚음 장부 [싱클레어] / Book of Vengeance [Sinclair]
   EN: Deal <style="highlight">+15%</style> damage for every 10 [VengeanceBookSinclair] (max <style="highlight">45%</style>)
   PL:
928. [Obrona (ulepszenia 1,4) — nazwa] 동부에서 몸 좀 풀어보죠
   źródło: Skills_personality-10.json :: dataList[id=1101204].levelList[level=1].name ; dataList[id=1101204].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Warmup in the East
   PL:
929. [Obrona (ulepszenie 1) — opis] [StartBattle] 잃은 체력의 20%만큼 보호막을 얻음 (턴당 1회)
   źródło: Skills_personality-10.json :: dataList[id=1101204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 20% of missing HP as Shield (once per turn)
   PL:
930. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-10.json :: dataList[id=1101204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
931. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-10.json :: dataList[id=1101204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 930 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
932. [Obrona (ulepszenie 4) — opis] <style="highlight">[StartBattle] 질투 완전 공명 수의 합에 따라 효과가 변경됨\n- 4 이상이면, 반격 시 '배로 먹여주마'를 사용함\n- 6 이상이면, 반격 시 '똑똑히 새겨라'를 사용함\n(조작 패널의 왼쪽 슬롯 스킬부터 발동, 턴당 최대 2회 발동)</style>\n[StartBattle] 잃은 체력의 <style="highlight">30%</style>만큼 보호막을 얻음 (턴당 1회)
   źródło: Skills_personality-10.json :: dataList[id=1101204].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: <style="highlight">[StartBattle] Skill behavior changes based on the sum of Envy A-Reson.:\n- At 4+ sum of A-Reson., use 'Payback with Interest' as Counter\n- At 6+ sum of A-Reson., use 'Write 'em all down' as Counter\n(Activates from the leftmost Skill Slot. Activates 2 times per turn)</style>\n[StartBattle] Gain <style="highlight">30%</style> of missing HP as Shield (once per turn)
   PL:
933. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-10.json :: dataList[id=1101204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 908 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
934. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-10.json :: dataList[id=1101204].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 908 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
935. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 중지는 잊지 않아
   źródło: Passives.json :: dataList[id=1101201].name
   limit: do 40 znaków
   EN: The Middle Never Forgets
   PL:
936. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 자신이 적에게 피격당할 때마다, 공격자(또는 부위)에게 [VendettaMark] 3 부여 (턴당 1회)\n\n자신을 제외한 아군이 적에게 피격당할 때마다, 공격자(또는 부위)에게 [VendettaMark] 2 부여 (인격 별로 턴당 1회)\n\n기본 공격 스킬 또는 반격 스킬 공격 종료 시, 대상의 [VendettaMark]을 전부 소모\n- 적의 [VendettaMark]을 소모할 때마다, 그 수치만큼 [VengeanceBookSinclair] 얻음
   źródło: Passives.json :: dataList[id=1101201].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [VendettaMark], [VengeanceBookSinclair]
   znaczenie tagów: [VendettaMark] = 복수 대상 / Vendetta Mark; [VengeanceBookSinclair] = 앙갚음 장부 [싱클레어] / Book of Vengeance [Sinclair]
   EN: When hit by an enemy, inflict 3 [VendettaMark] against the attacker(or Part) (once per turn)\n\nWhen another ally is hit by an enemy, inflict 2 [VendettaMark] against the attacker(or Part) (once per turn per Identity)\n\nAttack End with Base Attack Skills or Counter Skills: Consume all [VendettaMark] on the target\n- Every time the target consumes [VendettaMark], gain [VengeanceBookSinclair] equal to the amount consumed
   PL:
937. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — nazwa] 중지는 잊지 않아
   źródło: Passives.json :: dataList[id=1101211].name
   (powtórzenie elementu 935 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
938. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — opis] 자신이 적에게 피격당할 때마다, 공격자(또는 부위)에게 [VendettaMark] <style="highlight">5</style> 부여 (턴당 1회)\n\n자신을 제외한 아군이 적에게 피격당할 때마다, 공격자(또는 부위)에게 [VendettaMark] 2 부여 (인격 별로 턴당 1회)\n<style="highlight">- 아군이 중지 소속이면, [VendettaMark] 3 추가로 부여</style>\n\n기본 공격 스킬 또는 반격 스킬 공격 종료 시, 대상의 [VendettaMark]을 전부 소모\n- 적의 [VendettaMark]을 소모할 때마다, 그 수치만큼 [VengeanceBookSinclair] 얻음
   źródło: Passives.json :: dataList[id=1101211].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [VendettaMark], [VengeanceBookSinclair]
   znaczenie tagów: [VendettaMark] = 복수 대상 / Vendetta Mark; [VengeanceBookSinclair] = 앙갚음 장부 [싱클레어] / Book of Vengeance [Sinclair]
   EN: When hit by an enemy, inflict <style="highlight">5</style> [VendettaMark] against the attacker(or Part) (once per turn)\n\nWhen another ally is hit by an enemy, inflict 2 [VendettaMark] against the attacker(or Part) (once per turn per Identity)\n<style="highlight">- If the said ally is from the Middle, inflict 3 additional [VendettaMark]</style>\n\nAttack End with Base Attack Skills or Counter Skills, consume all [VendettaMark] on the target\n- Every time the target consumes [VendettaMark], gain [VengeanceBookSinclair] equal to the amount consumed
   PL:
939. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — nazwa] 빽
   źródło: Passives.json :: dataList[id=1101221].name
   limit: do 40 znaków
   EN: We've Got Your Back
   PL:
940. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — opis] 전투 시작 시, 현재 체력 비율이 가장 낮은 아군 1명이 [DefenseUp] 2 얻음
   źródło: Passives.json :: dataList[id=1101221].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Combat Start: 1 ally with the least current HP percentage gains 2 [DefenseUp]
   PL:
941. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Envy) — nazwa] 빽
   źródło: Passives.json :: dataList[id=1101231].name
   (powtórzenie elementu 939 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
942. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Envy) — opis] 전투 시작 시, 현재 체력 비율이 가장 낮은 아군 1명이 [DefenseUp] 2 얻음\n<style="highlight">- 대상이 중지 소속이면, [AttackUp] 2 추가로 얻음</style>
   źródło: Passives.json :: dataList[id=1101231].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DefenseUp], [AttackUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Combat Start: 1 ally with the least current HP percentage gains 2 [DefenseUp]\n<style="highlight">- If the said ally is from the Middle, also gain 2 [AttackUp]</style>
   PL:
943. [Kwestia głosowa [get_11012_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=get_11012_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
944. [Kwestia głosowa [get_11012_1] (Identity Acquisition)] 처리하기로 했던 것들은 다 줄 그었고… 이제 고대하시던 헤어 쿠폰 도둑놈들을 찾으러 가보자고 형님께 말씀드려야겠어.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=get_11012_1].dlg
   limit: do 190 znaków
   EN: We crossed off everyone on the list for today, and... Alright, time to tell Big Brother we’re all set to chase down those hair coupon thieves.
   PL:
945. [Kwestia głosowa [lobby_morning_11012_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=lobby_morning_11012_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
946. [Kwestia głosowa [lobby_morning_11012_1] (Morning Greeting)] 어어. 좋은 아침. …있잖아, 오늘 식사 때 큰 누님께서 내려오신대. …그렇게 떨지 말고. 나도 도울 테니까.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=lobby_morning_11012_1].dlg
   limit: do 250 znaków
   EN: Uh-huh. Good morning to you, too. ... Hey, just a heads-up, apparently the Great Sister's coming down to join us during mealtime. ... Don't freak out, I'll be right there with you for the prep.
   PL:
947. [Kwestia głosowa [lobby_noon_11012_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=lobby_noon_11012_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
948. [Kwestia głosowa [lobby_noon_11012_1] (Afternoon Greeting)] 미안, 점심은 너희들끼리 먹는 게 나을 것 같아. 동쪽으로 가려면 슬슬 준비해 둬야 할 것 같아서.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=lobby_noon_11012_1].dlg
   limit: do 120 znaków
   EN: Sorry, I won't be joining for lunch today. Gotta start getting ready to head east.
   PL:
949. [Kwestia głosowa [lobby_night_11012_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=lobby_night_11012_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
950. [Kwestia głosowa [lobby_night_11012_1] (Evening Greeting)] 별일 없었지? 후… 벌써 해가 졌네. 큰 아우께선 사업장에 나가신 것 같고… 우리는… 음, 자잘한 명부나 미리 집행해 두는 게 어때. 작은 형님 따라가려면 미리 끝장내 놔야지.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=lobby_night_11012_1].dlg
   limit: do 350 znaków
   EN: All good? Phew... it's sundown already, huh. Looks like the Young Brother's gone out to check on our 'businesses', and... we're... hm. Let's start by taking care of some easier targets in the Book. We'll have to clear our schedule if we want to keep up with the Big Brother.
   PL:
951. [Kwestia głosowa [smalltalk_11012_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=smalltalk_11012_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
952. [Kwestia głosowa [smalltalk_11012_1] (Chatter #1)] H사는… 곧 재적일이잖아? 그럼 뒷골목에 처박혀서 숨어있는 버러지들도 다 튀어나오겠지… 명부의 페이지만 계속 차지하고 있는 더러운 집행유예인들. 이참에 전부 처리하자고.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=smalltalk_11012_1].dlg
   limit: do 330 znaków
   EN: It's one of those Restructuring Days at H Corp. soon, isn't it? That'll get all the vermin hiding in the Backstreets maze to come out crawling... Disgusting fugitives of the Book of Vengeance, wastes of paper... Let's take this chance to clear out the trash.
   PL:
953. [Kwestia głosowa [smalltalk_11012_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=smalltalk_11012_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
954. [Kwestia głosowa [smalltalk_11012_2] (Chatter #2)] 원래 이런 건 동쪽 식구들이 처리하겠지만… 작은 형님께서 친히 벌하고 싶어 하시니 어쩔 수 없지.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=smalltalk_11012_2].dlg
   limit: do 190 znaków
   EN: Normally, this would fall under our eastern family's jurisdiction, but... our Big Brother was dead set on personally handling this specific case.
   PL:
955. [Kwestia głosowa [smalltalk_11012_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=smalltalk_11012_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
956. [Kwestia głosowa [smalltalk_11012_3] (Chatter #3)] 장부에… 8구 식구들이 말했던 원한들이 몇 개 추가 됐네. 자, 이걸 대신 처리해서 지워드리면 우리가 여기서 좀 날뛰는 걸 동쪽 식구들이 봐준다는 거지… 이런 걸 품앗이라고 하던가?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=smalltalk_11012_3].dlg
   limit: do 330 znaków
   EN: Looks like... some District 8 family's Vengeance list has been added to our own. Right, so we take care of these guys, and they'll overlook us starting a ruckus in the east, huh. What was that saying again? We scratch their backs, and they scratch ours, yeah.
   PL:
957. [Kwestia głosowa [smalltalk_11012_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=smalltalk_11012_4].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
958. [Kwestia głosowa [smalltalk_11012_4] (Post-Uptie Chat 1)] 복잡하게 구네. 그냥 집행을 받아들이면 그만인데, 왜 대들어서 이런 난장판을 만드는 걸까.\n장부에 적히면, 어딜 가든 언젠가 반드시 중지가 찾아올 텐데.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=smalltalk_11012_4].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You're making things hard for both of us. Why don't you just accept your punishment instead of fighting back and making a mess?\nYou know that once your name's in the book, the Middle'll stop at nothing to track you down wherever you go, right?
   PL:
959. [Kwestia głosowa [smalltalk_11012_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=smalltalk_11012_5].desc
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
960. [Kwestia głosowa [smalltalk_11012_5] (Post-Uptie Chat 2)] 이런 거 한두 줄 부탁하시는 걸로 우리 작은 형님 부탁을 퉁쳐주신다니, 마음이 넓어도 너무 넓으시네.\n감사의 의미로 귀한 환이라도 몇 개 사드려야…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=smalltalk_11012_5].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: They're really doing us a solid by letting these one or two favors pay for our Big Brother's request. Awfully generous of them.\nWe should gift them some expensive Boluses as thanks, at least...
   PL:
961. [Kwestia głosowa [neglect_11012_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=neglect_11012_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
962. [Kwestia głosowa [neglect_11012_1] (Idle)] …8구에서 가볼 만한 곳을 추천해 드릴까요, 형님?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=neglect_11012_1].dlg
   limit: do 120 znaków
   EN: ... Would you like some recommendations on places to visit in District 8, Big Bro?
   PL:
963. [Kwestia głosowa [gacksung_11012_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=gacksung_11012_1].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
964. [Kwestia głosowa [gacksung_11012_1] (Uptying)] 아… 그래, 그래. 시끄럽게 떠들지 말고 한 명씩 말해. 작은 형님이… 어디를 가신다고?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=gacksung_11012_1].dlg
   limit: do 120 znaków
   EN: Aha... Yeah, yeah. Pipe down, one at a time. Where's Big Brother headed to again?
   PL:
965. [Kwestia głosowa [formation_11012_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=formation_11012_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
966. [Kwestia głosowa [formation_11012_1] (Deployment)] H사와 8구의 안내는 제게 맡기시죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=formation_11012_1].dlg
   limit: do 120 znaków
   EN: You can count on me to guide your way through H Corp. and District 8.
   PL:
967. [Kwestia głosowa [battleentry_11012_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battleentry_11012_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
968. [Kwestia głosowa [battleentry_11012_1] (Stage Entry)] 하나씩 차근차근 그어서 되갚아보죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battleentry_11012_1].dlg
   limit: do 120 znaków
   EN: Let's take care of one Vengeance at a time.
   PL:
969. [Kwestia głosowa [battle_select_11012_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_select_11012_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
970. [Kwestia głosowa [battle_select_11012_1] (Viewed in Battle)] 다른 놈이 끼어들었나?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_select_11012_1].dlg
   limit: do 120 znaków
   EN: Who meddles in our business?
   PL:
971. [Kwestia głosowa [battle_endcommand_11012_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_endcommand_11012_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
972. [Kwestia głosowa [battle_endcommand_11012_1] (Commencing Attack)] 처부숴 줄 테다.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_endcommand_11012_1].dlg
   limit: do 120 znaków
   EN: I'll pummel them to dust.
   PL:
973. [Kwestia głosowa [battle_enemy_break_11012_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_enemy_break_11012_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
974. [Kwestia głosowa [battle_enemy_break_11012_1] (Enemy Stagger)] 반항하지 마.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_enemy_break_11012_1].dlg
   limit: do 120 znaków
   EN: Don't resist.
   PL:
975. [Kwestia głosowa [battle_break_11012_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_break_11012_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
976. [Kwestia głosowa [battle_break_11012_1] (Staggered)] 저… 새끼!
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_break_11012_1].dlg
   limit: do 120 znaków
   EN: You... little... shit!
   PL:
977. [Kwestia głosowa [battle_kill_11012_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_kill_11012_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
978. [Kwestia głosowa [battle_kill_11012_1] (Enemy Killed)] …좋아, 장부에서 삭제.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_kill_11012_1].dlg
   limit: do 120 znaków
   EN: ... Nice, now I can cross that off the book.
   PL:
979. [Kwestia głosowa [battle_dead_11012_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_dead_11012_1].desc
   (powtórzenie elementu 371 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
980. [Kwestia głosowa [battle_dead_11012_1] (Death)] 큭… 큭. 내가 죽어도… 넌 장부에 남는다.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_dead_11012_1].dlg
   limit: do 120 znaków
   EN: Heh... heh. Killing me won't clear your name off the book.
   PL:
981. [Kwestia głosowa [choice_success_p_11012_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=choice_success_p_11012_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
982. [Kwestia głosowa [choice_success_p_11012_2] (Check Passed)] 제 안내가 도움이 되셨다면 다행입니다. 형님.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=choice_success_p_11012_2].dlg
   limit: do 120 znaków
   EN: I am glad you found my guidance helpful, Big Bro.
   PL:
983. [Kwestia głosowa [choice_fail_n_11012_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=choice_fail_n_11012_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
984. [Kwestia głosowa [choice_fail_n_11012_1] (Check Failed)] …그냥 반으로 갈라 버리면 안 되나?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=choice_fail_n_11012_1].dlg
   limit: do 120 znaków
   EN: ... Why don't we just break this thing in half?
   PL:
985. [Kwestia głosowa [battle_clear_11012_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_clear_11012_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
986. [Kwestia głosowa [battle_clear_11012_1] (Victory Cry)] 결국 되갚아냈지만 식구들도 많이 죽었어. 아까 같이 밥 먹은 사람인데… 내가 반드시… 되갚아 줄게.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_clear_11012_1].dlg
   limit: do 220 znaków
   EN: We finally had our vengeance, but many of the family died in the process. Even those that I shared a meal with just a few hours ago... I'll... avenge you, I swear I will.
   PL:
987. [Kwestia głosowa [battle_clear_ex_11012_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_clear_ex_11012_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
988. [Kwestia głosowa [battle_clear_ex_11012_1] (Extra Conditions Fulfilled)] 완벽한 장부 집행으로 다들 고생했다고 작은 형님께서 자라 환을 몇 개 주셨다. 8구에 처음 온 놈들은 운 좋은 거라고. 꽤 귀한 거거든.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_clear_ex_11012_1].dlg
   limit: do 290 znaków
   EN: Big Brother gave us some tortoise Boluses as a reward for a job well done. Here's some info for the Brothers and Sisters who've never been to District 8 before—these things are pretty darn rare. So consider yourselves lucky.
   PL:
989. [Kwestia głosowa [battle_defeat_11012_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_defeat_11012_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
990. [Kwestia głosowa [battle_defeat_11012_1] (Defeat Wail)] …실패는 상관없어. 그건 중지의 실패가 아닌 나의 실패이니. 그리고 중지는 반드시 복수에 성공한다.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_MiddleFinger_11012.json :: dataList[id=battle_defeat_11012_1].dlg
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ... I don't care that we failed. It's my failure, not the Middle's.\nAnd the Middle always pays its debts.
   PL:

## [000] The Thumb East Soldato II — Sinclair — 동부 엄지 솔다토II
- ID Tożsamości: `11013` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 79 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Burn, Tremor

991. [Karta Tożsamości — tytuł] 동부 엄지\n솔다토II
   źródło: Personalities.json :: dataList[id=11013].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Thumb\nEast Soldato II
   PL:
992. [Karta Tożsamości — nazwa] 싱클레어
   źródło: Personalities.json :: dataList[id=11013].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
993. [Karta Tożsamości — nazwa z tytułem] 싱클레어
   źródło: Personalities.json :: dataList[id=11013].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
994. [Karta Tożsamości — opis] 싱클레어의 열세번째 인격
   źródło: Personalities.json :: dataList[id=11013].desc
   limit: do 120 znaków
   EN: Sinclair’s 13th Identity
   PL:
995. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 예에 따라서.
   źródło: Skills_personality-10.json :: dataList[id=1101301].levelList[level=1].name ; dataList[id=1101301].levelList[level=2].name ; dataList[id=1101301].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Adherence to Propriety.
   PL:
996. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1101301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL:
997. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-10.json :: dataList[id=1101301].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1101301].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1101301].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL:
998. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Combustion]과 [Vibration]의 합 6당 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-10.json :: dataList[id=1101301].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Combustion], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[WhenUse] Coin Power +1 for every 6 ([Combustion] + [Vibration]) on target (max 2)</style>
   PL:
999. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-10.json :: dataList[id=1101301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1101301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count<style="highlight"></style>
   PL:
1000. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 6당 코인 위력 +1 (최대 2)\n<style="highlight">[WhenUse] 대상의 [Vibration]이 특수 진동이면, 합 위력 +1</style>
   źródło: Skills_personality-10.json :: dataList[id=1101301].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Combustion], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Coin Power +1 for every 6 ([Combustion] + [Vibration]) on target (max 2)\n<style="highlight">[WhenUse] If target has 'Unique Tremor' as [Vibration], Clash Power +1</style>
   PL:
1001. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 엄지에 존중을.
   źródło: Skills_personality-10.json :: dataList[id=1101302].levelList[level=1].name ; dataList[id=1101302].levelList[level=2].name ; dataList[id=1101302].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Respect the Thumb.
   PL:
1002. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-10.json :: dataList[id=1101302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Combustion], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 6+ ([Combustion] + [Vibration]), Coin Power +1
   PL:
1003. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-10.json :: dataList[id=1101302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 997 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1004. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1101302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 996 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1005. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]이 6 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-10.json :: dataList[id=1101302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 6+ [Vibration], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
1006. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 <style="highlight">합 6당 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-10.json :: dataList[id=1101302].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Combustion], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[WhenUse] Coin Power +1 for every 6 ([Combustion] + [Vibration]) on target (max 2)</style>
   PL:
1007. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-10.json :: dataList[id=1101302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Vibration]
   PL:
1008. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-10.json :: dataList[id=1101302].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1101302].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 999 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1009. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 대상에게 [VibrationIgnition]이 10 이상 있으면, 대상의 [Combustion] 횟수 1 증가</style>
   źródło: Skills_personality-10.json :: dataList[id=1101302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationIgnition], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Combustion] = 화상 / Burn
   EN: <style="highlight">[OnSucceedAttack] If target has 10+ [VibrationIgnition], inflict +1 [Combustion] Count</style>
   PL:
1010. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration]이 6 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-10.json :: dataList[id=1101302].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1101302].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 6+ [Vibration], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL:
1011. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 6당 코인 위력 +1 (최대 2)\n<style="highlight">[WhenUse] 대상의 [Combustion]과 [Vibration]의 합 4당 피해량 +10% (최대 30%)\n[WhenUse] 대상의 특수 진동이 10 이상이면, 기본 위력 +2</style>
   źródło: Skills_personality-10.json :: dataList[id=1101302].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Combustion], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Coin Power +1 for every 6 ([Combustion] + [Vibration]) on target (max 2)\n<style="highlight">[WhenUse] Deal +10% damage for every 4 ([Combustion] + [Vibration]) on target (max 30%)\n[WhenUse] If target has 10+ 'Unique Tremor', Base Power +2</style>
   PL:
1012. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-10.json :: dataList[id=1101302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]<style="highlight"></style>
   PL:
1013. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 [VibrationIgnition]이 10 이상 있으면, 대상의 [Combustion] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-10.json :: dataList[id=1101302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationIgnition], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 10+ [VibrationIgnition], inflict <style="highlight">+2</style> [Combustion] Count
   PL:
1014. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 추력 집중
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].name ; dataList[id=1101303].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Thruster Compression
   PL:
1015. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 8당 코인 위력 +1 (최대 2)\n[WhenUse] [FireBulletPropellant] 3개 이상 보유시, 기본 위력 +1
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [Vibration], [FireBulletPropellant]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [FireBulletPropellant] = 작열 추진탄 / Scorch Propellant Ammo
   EN: [WhenUse] Coin Power +1 for every 8 ([Combustion] + [Vibration]) on target (max 2)\n[WhenUse] At 3+ [FireBulletPropellant], Base Power +1
   PL:
1016. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [FireBulletPropellant] 1 소모
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1101303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [FireBulletPropellant]
   znaczenie tagów: [FireBulletPropellant] = 작열 추진탄 / Scorch Propellant Ammo
   EN: Spend 1 [FireBulletPropellant]
   PL:
1017. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] 이 코인 효과로 [FireBulletPropellant]을 소모하였다면, 피해량 +20%
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [FireBulletPropellant]
   znaczenie tagów: [FireBulletPropellant] = 작열 추진탄 / Scorch Propellant Ammo
   EN: If this unit spent [FireBulletPropellant] due to this Coin's effect, deal +20% damage
   PL:
1018. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=1101303].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 996 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1019. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +2 [Combustion] Count
   PL:
1020. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#0].coindescs[#4].desc ; dataList[id=1101303].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]
   PL:
1021. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [FireBulletPropellant] 1 소모
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1101303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1016 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1022. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] 이 코인 효과로 [FireBulletPropellant]을 소모하였다면, 피해량 +20%
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 1017 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1023. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=1101303].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 996 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1024. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#1].coindescs[#3].desc ; dataList[id=1101303].levelList[level=4].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 637 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1025. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [FireBulletPropellant] 1 소모
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1101303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 1016 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1026. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] 이 코인 효과로 [FireBulletPropellant]을 소모하였다면, 피해량 +20%
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 1017 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1027. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1101303].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 996 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1028. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#2].coindescs[#3].desc ; dataList[id=1101303].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 4 [Combustion]
   PL:
1029. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 5 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#2].coindescs[#4].desc ; dataList[id=1101303].levelList[level=4].coinlist[#2].coindescs[#4].desc
   (powtórzenie elementu 742 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1030. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 6 — opis] [OnSucceedAttack] [FireBulletPropellant]을 소모했으면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=3].coinlist[#2].coindescs[#5].desc ; dataList[id=1101303].levelList[level=4].coinlist[#2].coindescs[#5].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FireBulletPropellant], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FireBulletPropellant] = 작열 추진탄 / Scorch Propellant Ammo; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this unit spent [FireBulletPropellant], trigger [VibrationExplosion]; then, reduce the target's [Vibration] Count by 1
   PL:
1031. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 8당 코인 위력 +1 (최대 2)\n[WhenUse] [FireBulletPropellant] 3개 이상 보유시, <style="highlight">기본 위력 +3, 피해량 +30%, [SuperCoin]으로 변경됨</style>
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Combustion], [Vibration], [FireBulletPropellant], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [FireBulletPropellant] = 작열 추진탄 / Scorch Propellant Ammo; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Coin Power +1 for every 8 ([Combustion] + [Vibration]) on target (max 2)\n[WhenUse] At 3+ [FireBulletPropellant], <style="highlight">Base Power +3, deal +30% damage, and convert the Coins to [SuperCoin]s</style>
   PL:
1032. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] 이 코인 효과로 [FireBulletPropellant]을 소모하였다면, 피해량 <style="highlight">+25%</style>
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [FireBulletPropellant]
   znaczenie tagów: [FireBulletPropellant] = 작열 추진탄 / Scorch Propellant Ammo
   EN: If this unit spent [FireBulletPropellant] due to this Coin's effect, deal <style="highlight">+25%</style> damage
   PL:
1033. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Combustion] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">+3</style> [Combustion] Count
   PL:
1034. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] 이 코인 효과로 [FireBulletPropellant]을 소모하였다면, 피해량 <style="highlight">+25%</style>
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 1032 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1035. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] 이 코인 효과로 [FireBulletPropellant]을 소모하였다면, 피해량 <style="highlight">+25%</style>
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 1032 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1036. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 7 — opis] <style="highlight">[OnSucceedAttack] 이 스킬에서 [FireBulletPropellant]을 3개 소모했으면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_personality-10.json :: dataList[id=1101303].levelList[level=4].coinlist[#2].coindescs[#6].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [FireBulletPropellant], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FireBulletPropellant] = 작열 추진탄 / Scorch Propellant Ammo; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] If this Skill spent 3 [FireBulletPropellant], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL:
1037. [Obrona (ulepszenia 1,4) — nazwa] 철의 방어
   źródło: Skills_personality-10.json :: dataList[id=1101304].levelList[level=1].name ; dataList[id=1101304].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 9 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Ferrous Guard
   PL:
1038. [Obrona (ulepszenie 1) — opis] 보호막이 있는 동안 피격 시, 피격 횟수만큼 공격자에게 [Vibration] 1 부여 (턴 당 3회 발동)
   źródło: Skills_personality-10.json :: dataList[id=1101304].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Inflict 1 [Vibration] against the Attacker when hit as long as this unit has remaining Shield (3 times per turn)
   PL:
1039. [Obrona (ulepszenie 4) — opis] 보호막이 있는 동안 피격 시, 피격 횟수만큼 공격자에게 [Vibration] <style="highlight">2</style> 부여 (턴 당 <style="highlight">4회</style> 발동)
   źródło: Skills_personality-10.json :: dataList[id=1101304].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Inflict <style="highlight">2</style> [Vibration] against the Attacker when hit as long as this unit has remaining Shield (<style="highlight">4</style> times per turn)
   PL:
1040. [Pasywka bojowa (od ulepszenia 2) — nazwa] 총검술
   źródło: Passives.json :: dataList[id=1101312].name
   limit: do 40 znaków
   EN: Bayonets
   PL:
1041. [Pasywka bojowa (od ulepszenia 2) — opis] 상시 적용: [FireBulletPropellant] 15개 보유\n\n스킬이나 패시브로 [FireBulletPropellant]을 소모했다면, 다음 턴에 소모한 만큼 [AttackDmgUp]를 얻음 (최대 3)\n\n[FireBulletPropellant]을 소모하는 코인을 굴릴 때, [FireBulletPropellant]이 없는 경우에도 공격이 취소되지 않는 대신 해당 코인의 적중 시 [Combustion] 부여, [Combustion] 횟수 증가 효과가 발동하지 않음
   źródło: Passives.json :: dataList[id=1101312].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n, [FireBulletPropellant], [AttackDmgUp], [Combustion]
   znaczenie tagów: [FireBulletPropellant] = 작열 추진탄 / Scorch Propellant Ammo; [AttackDmgUp] = 피해량 증가 / Damage Up; [Combustion] = 화상 / Burn
   EN: Always Active: begin Encounters with 15 [FireBulletPropellant]\n\nIf this unit spent [FireBulletPropellant] with Skills or Passives, gain [AttackDmgUp] equal to the amount spent next turn (max 3)\n\nWhen flipping a Coin that spends [FireBulletPropellant]: while not having [FireBulletPropellant] does not cancel this unit's attacks, the Coin's On Hit "inflict [Combustion]" and "inflict [Combustion] Count" effects do not activate
   PL:
1042. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — nazwa] 탄환 상납
   źródło: Passives.json :: dataList[id=1101301].name
   limit: do 40 znaków
   EN: Ammunition Tribute
   PL:
1043. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — opis] [Bullet]을 쓰는 인격 중 편성 순서가 가장 빠른 아군 1명의 공격이 종료 되었을 때, 해당 인격의 현재 보유 [Bullet]이 절반 미만이면 (소수점 올림), 해당 인격이 소모한 [Bullet] 수 만큼 자신의 [FireBulletPropellant]을 소모하고, [FireBulletPropellant]을 소모한 만큼 해당 인격이 사용하는 [Bullet]을 보급함. (최대 소모 값: 3개) (전투당 1회)\n\n- [Bullet]을 보급 받는 인격이 자신보다 계급이 높은 엄지 소속 인격이면, 해당 인격이 사용하는 [Bullet]을 1개 더 보급함\n- 위력, 횟수가 분리된 [Bullet]은 위력, 횟수를 무작위로 보급함\n- 만약 위력 또는 횟수가 최댓값인 경우, 최댓값이 아닌 쪽의 [Bullet]으로 보급함
   źródło: Passives.json :: dataList[id=1101301].desc
   limit: do 910 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [FireBulletPropellant]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [FireBulletPropellant] = 작열 추진탄 / Scorch Propellant Ammo
   EN: When the 1 ally Identity with the earliest Deployment order among those using [Bullet] finishes their attack, if their current [Bullet] count is fewer than half (rounded up), spend [FireBulletPropellant] on self equal to the total [Bullet] count the affected unit spent and supply them with the same amount of [Bullet] as [FireBulletPropellant] this unit just spent. (can spend up to 3 ammunition) (once per Encounter)\n\n- If the [Bullet] receiving Identity is a Thumb Identity of a higher rank, supply 1 additional [Bullet] they use\n- If the [Bullet] receiving Identity has separate values for Potency and Count, they will be supplied at random.\n- If either Potency or Count is maxed out, supply whichever is not maxed.
   PL:
1044. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Pride) — nazwa] 탄환 상납
   źródło: Passives.json :: dataList[id=1101311].name
   (powtórzenie elementu 1042 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1045. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Pride) — opis] [Bullet]을 쓰는 인격 중 편성 순서가 가장 빠른 아군 1명의 공격이 종료 되었을 때, 해당 인격의 현재 보유 [Bullet]이 절반 미만이면 (소수점 올림), 해당 인격이 소모한 [Bullet] 수 만큼 자신의 [FireBulletPropellant]을 소모하고, [FireBulletPropellant]을 소모한 만큼 해당 인격이 사용하는 [Bullet]을 보급함. <style="highlight">(최대 소모 값: 5개)</style> (전투당 1회)\n\n- [Bullet]을 보급 받는 인격이 자신보다 계급이 높은 엄지 소속 인격이면, 해당 인격이 사용하는 [Bullet]을 1개 더 보급함\n- 위력, 횟수가 분리된 [Bullet]은 위력, 횟수를 무작위로 보급함\n- 만약 위력 또는 횟수가 최댓값인 경우, 최댓값이 아닌 쪽의 [Bullet]으로 보급함
   źródło: Passives.json :: dataList[id=1101311].desc
   limit: do 910 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet], [FireBulletPropellant]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [FireBulletPropellant] = 작열 추진탄 / Scorch Propellant Ammo
   EN: When the 1 ally Identity with the earliest Deployment order among those using [Bullet] finishes their attack, if their current [Bullet] count is fewer than half (rounded up), spend [FireBulletPropellant] on self equal to the total [Bullet] count the affected unit spent and supply them with the same amount of [Bullet] as [FireBulletPropellant] this unit just spent. <style="highlight">(can spend up to 5 ammunition)</style> (once per Encounter)\n\n- If the [Bullet] receiving Identity is a Thumb Identity of a higher rank, supply 1 additional [Bullet] they use\n- If the [Bullet] receiving Identity has separate values for Potency and Count, they will be supplied at random.\n- If either Potency or Count is maxed out, supply whichever is not maxed.
   PL:
1046. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Pride) — nazwa] 재장전
   źródło: Passives.json :: dataList[id=1101321].name
   limit: do 40 znaków
   EN: Reloader
   PL:
1047. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Pride) — opis] [Bullet]을 쓰는 인격 중 편성 순서가 가장 빠른 아군 1명의 공격이 종료 되었을 때, 해당 인격의 현재 보유 [Bullet]이 절반 미만이면, [Bullet]을 최대치의 절반만큼 다시 얻음 (소수점 올림, 전투당 1회, 최대 [Bullet] 획득 값 : 5)\n\n- 위력, 횟수가 분리된 [Bullet]은 위력, 횟수를 무작위로 얻음\n- 만약 위력 또는 횟수가 최댓값인 경우, 최댓값이 아닌 쪽의 [Bullet]으로 얻음\n- [Bullet]을 사용하는 인격이 없으면, 이 효과는 발동하지 않음
   źródło: Passives.json :: dataList[id=1101321].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: When the 1 ally Identity with the earliest Deployment order among those using [Bullet] finishes their attack, if their current [Bullet] count is fewer than half (rounded up), regain half of the maximum [Bullet] capacity (rounded up; once per Encounter; max [Bullet] regained: 5)\n\n- If the [Bullet] receiving Identity has separate values for Potency and Count, they will gain them at random\n- If either Potency or Count of [Bullet] is maxed out, gain whichever is not maxed\n- This effect does not activate if there are no Identities that use [Bullet]
   PL:
1048. [Kwestia głosowa [get_11013_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=get_11013_1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1049. [Kwestia głosowa [get_11013_1] (Identity Acquisition)] 명령은 경청하고 있어요. 그저… 감히 상급자와 눈이 맞지 않도록 시선을 아래로 둘 뿐.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=get_11013_1].dlg
   limit: do 180 znaków
   EN: I listen carefully to every order I'm given. I... just look to the ground to not risk staring at my superiors straight in their eyes.
   PL:
1050. [Kwestia głosowa [lobby_morning_11013_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=lobby_morning_11013_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1051. [Kwestia głosowa [lobby_morning_11013_1] (Morning Greeting)] …해가 떴으니, 보호비를 걷으러 가야 해요. 괜히 지체하다가, 윗분들이 행동하게 만드는 건… 엄지로서 실격이죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=lobby_morning_11013_1].dlg
   limit: do 270 znaków
   EN: ... Sun's up. Time to collect some protection fees. If I don't get right on it, my superiors might be compelled to act, and that's... well, I wouldn't deserve to be a member of The Thumb if I let that happen.
   PL:
1052. [Kwestia głosowa [lobby_noon_11013_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=lobby_noon_11013_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1053. [Kwestia głosowa [lobby_noon_11013_1] (Afternoon Greeting)] 점심을 먹으려면 조금 기다려야 해요. 솔다토 테르조, 콰르토 분들이 식사를 마치고 나면 먹어야 하거든요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=lobby_noon_11013_1].dlg
   limit: do 180 znaków
   EN: Lunch is still a while away for me. Soldato Terzo and Quarto, my superiors, have to finish eating their meals first before I eat dinner.
   PL:
1054. [Kwestia głosowa [lobby_night_11013_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=lobby_night_11013_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1055. [Kwestia głosowa [lobby_night_11013_1] (Evening Greeting)] 밤에는 다른 조직에 대해 공부하곤 해요. 새로운 회사나 단체에 대해 연구하고 그들의 계급을 대략적이나마 측정하려 노력하죠.\n그래야만… 예의를 다하지 못하는 일을 줄일 수 있으니까요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=lobby_night_11013_1].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I usually study other Syndicates at night, trying to learn more about companies and organizations' internal structure to gauge their hierarchy.\nI have to... try my best to uphold the perfect manners and etiquette.
   PL:
1056. [Kwestia głosowa [smalltalk_11013_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=smalltalk_11013_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1057. [Kwestia głosowa [smalltalk_11013_1] (Chatter #1)] 음. 탄환을 닦는 건 솔다토 프리모에게 맡기는 편이 좋겠어요.\n저도 이제 솔다토 세칸도인데… 슬슬 탄환 닦는 건 그만두고, 카포 분들에게 탄환을 보급하는 중책으로 넘어가야죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=smalltalk_11013_1].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hm. I think I can leave the ammo-cleaning job for the Soldato Primo juniors.\nI'm a Soldato Secondo, you know...? It's about time I moved away from ammo cleaning duty to something more important, like ammo carrying duty for the esteemed Capos.
   PL:
1058. [Kwestia głosowa [smalltalk_11013_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=smalltalk_11013_2].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1059. [Kwestia głosowa [smalltalk_11013_2] (Chatter #2)] 말하기 전에 생각하는 버릇을 들여두는 편이 좋아요. 말실수로 처벌받은 혀나 턱을 치료하려면 값이 꽤 나가니까요.\n물론…의체로 갈아끼우면 저렴하긴 하죠. 저는… 내키지 않지만요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=smalltalk_11013_2].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It's important to learn how to think before we speak. Treating punished tongues or jaws can get pretty expensive.\nWell... sure, replacing them with prosthetics can be a lot cheaper. I don't like it, though...
   PL:
1060. [Kwestia głosowa [smalltalk_11013_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=smalltalk_11013_3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1061. [Kwestia głosowa [smalltalk_11013_3] (Chatter #3)] …총검술은 엄지의 필수 소양이에요. 탄을 쓸 수 없는 상황에서 날카로운 총검과 튼튼한 개머리판만큼 든든한 게 없거든요.\n게다가 동부 엄지는 평소에도 추진탄을 활용한 총검술을 주로 쓰다보니… 유난히 실력이 좋은 편이죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=smalltalk_11013_3].dlg
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ... Anyone in The Thumb has to know how to wield bayonets. Nothing like the sharp blade and the hard stock of a rifle in situations when we can't use ammunition.\nIt's also something The Thumb's eastern branch specializes in, in combination with the usage of propellant rounds... so we're pretty good at it.
   PL:
1062. [Kwestia głosowa [smalltalk_11013_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=smalltalk_11013_4].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1063. [Kwestia głosowa [smalltalk_11013_4] (Post-Uptie Chat 1)] 엄지는 신사적이에요. 무작위한 지령이나, 잔혹한 미학, 사슬 같은 의리와는 완전히 다르죠.\n상대가 이룬 업적을 인정하고, 이를 높이 사 따르는 건 어렵지 않잖아요?
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=smalltalk_11013_4].dlg
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Thumb is very gentlemanly. We don't subscribe to the patternless Prescripts, vicious philosophies on art, or a sense of brotherhood that's more akin to chains.\nThere's nothing difficult about what we do, right? It's just a recognition of the accomplishments, and giving them the respect they deserve.
   PL:
1064. [Kwestia głosowa [smalltalk_11013_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=smalltalk_11013_5].desc
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1065. [Kwestia głosowa [smalltalk_11013_5] (Post-Uptie Chat 2)] 프리모, 세칸도, 테르조, 콰르토. 같은 계급이라도 그 안에 세부적인 높낮이가 있어요. 그 미세한 차이 덕분에… 저희는 더 신사적이고, 예의 바르게 상대를 대할 수 있죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=smalltalk_11013_5].dlg
   limit: do 270 znaków
   EN: Primo, Secondo, Terzo, Quarto. Even within the same ranks there exists distinctly tiered subdivisions. It's those details that allow us to be more... gentlemanly and courteous toward anyone we come across.
   PL:
1066. [Kwestia głosowa [neglect_11013_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=neglect_11013_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1067. [Kwestia głosowa [neglect_11013_1] (Idle)] …함부로 입을 놀리면 실수라도 실례를 범하는 법.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=neglect_11013_1].dlg
   limit: do 120 znaków
   EN: ... Speaking thoughtlessly is a good way to display bad manners. Even by accident.
   PL:
1068. [Kwestia głosowa [gacksung_11013_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=gacksung_11013_1].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1069. [Kwestia głosowa [gacksung_11013_1] (Uptying)] 무례하네요. 언더보스의 명령을 따르지 않았음에도, 감히 숨을 쉬고 있다니.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=gacksung_11013_1].dlg
   limit: do 140 znaków
   EN: Daring to breathe when you haven't even followed the underboss's command? Now that's quite discourteous.
   PL:
1070. [Kwestia głosowa [formation_11013_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=formation_11013_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1071. [Kwestia głosowa [formation_11013_1] (Deployment)] 명령하실 때까지 자리에서 대기하겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=formation_11013_1].dlg
   limit: do 120 znaków
   EN: I will await your next command at this spot.
   PL:
1072. [Kwestia głosowa [battleentry_11013_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battleentry_11013_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1073. [Kwestia głosowa [battleentry_11013_1] (Stage Entry)] 명 받았습니다.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battleentry_11013_1].dlg
   limit: do 120 znaków
   EN: As you command.
   PL:
1074. [Kwestia głosowa [battle_select_11013_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_select_11013_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1075. [Kwestia głosowa [battle_select_11013_1] (Viewed in Battle)] 현재 말씀하신 임무를 수행 중이에요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_select_11013_1].dlg
   limit: do 120 znaków
   EN: Progressing through the mission as commanded.
   PL:
1076. [Kwestia głosowa [battle_endcommand_11013_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_endcommand_11013_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1077. [Kwestia głosowa [battle_endcommand_11013_1] (Commencing Attack)] 명령에 따르겠습니다.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_endcommand_11013_1].dlg
   limit: do 120 znaków
   EN: I will follow your command.
   PL:
1078. [Kwestia głosowa [battle_enemy_break_11013_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_enemy_break_11013_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1079. [Kwestia głosowa [battle_enemy_break_11013_1] (Enemy Stagger)] 각자의 위치가 있으니…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_enemy_break_11013_1].dlg
   limit: do 120 znaków
   EN: We all have our lots...
   PL:
1080. [Kwestia głosowa [battle_break_11013_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_break_11013_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1081. [Kwestia głosowa [battle_break_11013_1] (Staggered)] 예에 바친 목숨…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_break_11013_1].dlg
   limit: do 120 znaków
   EN: So, in this life dedicated to propriety...
   PL:
1082. [Kwestia głosowa [battle_kill_11013_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_kill_11013_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1083. [Kwestia głosowa [battle_kill_11013_1] (Enemy Killed)] 피차 동정은 필요 없겠죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_kill_11013_1].dlg
   limit: do 120 znaków
   EN: ... there's no need for sympathy, mutual or otherwise.
   PL:
1084. [Kwestia głosowa [battle_dead_11013_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_dead_11013_1].desc
   (powtórzenie elementu 371 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1085. [Kwestia głosowa [battle_dead_11013_1] (Death)] 무례는 범하지 않았을 것이라 생각…
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_dead_11013_1].dlg
   limit: do 120 znaków
   EN: I don't think I was discourteous...
   PL:
1086. [Kwestia głosowa [choice_success_p_11013_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=choice_success_p_11013_2].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1087. [Kwestia głosowa [choice_success_p_11013_2] (Check Passed)] 명령하신 임무를 완료했어요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=choice_success_p_11013_2].dlg
   limit: do 120 znaków
   EN: Mission completed as ordered.
   PL:
1088. [Kwestia głosowa [choice_fail_n_11013_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=choice_fail_n_11013_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1089. [Kwestia głosowa [choice_fail_n_11013_1] (Check Failed)] …책임을 다하지 못했으니, 그에 맞는 벌을.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=choice_fail_n_11013_1].dlg
   limit: do 120 znaków
   EN: ... I failed to complete my duties. This is but a punishment I deserve.
   PL:
1090. [Kwestia głosowa [battle_clear_11013_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_clear_11013_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1091. [Kwestia głosowa [battle_clear_11013_1] (Victory Cry)] 완벽하진 않지만, 하달하신 명령은 모두 지켜냈어요. 모쪼록… 마음에 드셨으면 좋겠네요.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_clear_11013_1].dlg
   limit: do 120 znaków
   EN: That wasn't perfect, but I completed every one of your orders! I hope... you like it.
   PL:
1092. [Kwestia głosowa [battle_clear_ex_11013_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_clear_ex_11013_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1093. [Kwestia głosowa [battle_clear_ex_11013_1] (Extra Conditions Fulfilled)] 완벽한 승리를 보고드릴 수 있어 영광이네요! 분명… 관리자님을 비롯한 상급자 분들의 활약 덕분이겠죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_clear_ex_11013_1].dlg
   limit: do 160 znaków
   EN: I am honored to report that we have achieved a most perfect victory! All credits go to my superiors, including the manager.
   PL:
1094. [Kwestia głosowa [battle_defeat_11013_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_defeat_11013_1].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1095. [Kwestia głosowa [battle_defeat_11013_1] (Defeat Wail)] 탓할 것도 없이 제 몫을 못했으니… 부족함의 대가를 치뤄야죠.
   źródło: PersonalityVoiceDlg/Voice_Sinclair_Thumb_11013.json :: dataList[id=battle_defeat_11013_1].dlg
   limit: do 120 znaków
   EN: I won't blame anyone else or make excuses. ... I must pay for my inadequacies.
   PL:
