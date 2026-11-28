# Grzesznik #01: Yi Sang — Tożsamości, umiejętności, pasywki i głos (część a) — Limbus Company

Kompletny zestaw kart Tożsamości postaci **Yi Sang** (이상) wraz z umiejętnościami na ulepszeniach 1–4, efektami monet, pasywkami i kwestiami głosowymi.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Grzesznik #01: Yi Sang (이상)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 이상
   źródło: Characters.json :: dataList[id=1].name
   limit: do 40 znaków
   EN: Yi Sang
   PL:
2. [Akta więźnia — nazwa] 이상
   źródło: IntroduceCharacter.json :: dataList[id=이상].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
3. [Akta więźnia — opis] [보안 검열] 날개 소속 최연소 수석 연구원 출신으로 타 수감자들에 비해\n우수한 지능을 가지고 있습니다. 일상적인 소통은 아마 우리가 뽑은\n관리자님의 수준에선 힘들 것으로 판단됩니다. 그렇다고 노골적으로\n대화를 피하는 것 또한 불안 요소가 있습니다. 간혹 본 수감자의\n침묵 상태가 길더라도 일련의 사고들을 뇌 속에서 처리 중이므로\n너그럽게 기다려 주시는 걸 권장합니다.
   źródło: IntroduceCharacter.json :: dataList[id=이상].description
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Formerly the youngest chief researcher at the [REDACTED] Wing,\nthis Sinner possesses higher intelligence compared to most others.\nWe estimate that everyday conversation with this Sinner will prove difficult\nfor managers selected by our current screening process.\nAvoiding communication altogether will pose a risk on its own, however.\nIf the Sinner remains silent for a long time, that means he is currently processing a line of deliberate thought;\nwe recommend waiting patiently for him.
   PL: [UTAJNIONO] Były najmłodszy główny badacz w Skrzydle; pod względem inteligencji\nprzewyższa pozostałych Grzeszników. Oceniamy, że codzienna rozmowa z nim\nprzekroczy zapewne możliwości Kierownika, którego wybraliśmy. Z drugiej strony\notwarte unikanie kontaktu również niesie ryzyko. Jeśli Grzesznik milczy\nzbyt długo, oznacza to, że przetwarza w głowie ciąg myśli;\nzalecamy wyrozumiałość i cierpliwe czekanie.

## [0] LCB Sinner — Yi Sang — LCB 수감자
- ID Tożsamości: `10101` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 72 · szybkość: 4–6 / 4–7 / 4–8 / 4–8
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Sinking

4. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10101].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL:
5. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10101].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10101].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Karta Tożsamości — opis] 이상의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10101].desc
   limit: do 120 znaków
   EN: Yi Sang’s 1st Identity
   PL:
8. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 쳐내기
   źródło: Skills.json :: dataList[id=1010101].levelList[level=1].name ; dataList[id=1010101].levelList[level=2].name ; dataList[id=1010101].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Deflect
   PL:
9. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1010101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 1 [Sinking]
   PL:
10. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 2 [Sinking]
   PL:
11. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL:
12. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 밀어 찌르기
   źródło: Skills.json :: dataList[id=1010102].levelList[level=1].name ; dataList[id=1010102].levelList[level=2].name ; dataList[id=1010102].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: End-stop Stab
   PL:
13. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +1 [Sinking] Count
   PL:
14. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여. 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010102].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking] and +1 [Sinking] Count
   PL:
15. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여. 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] and +1 [Sinking] Count
   PL:
16. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 연격
   źródło: Skills.json :: dataList[id=1010103].levelList[level=3].name ; dataList[id=1010103].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 6 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Enjamb
   PL:
17. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력이 0미만이면 다음 턴에 취약 1 부여
   źródło: Skills.json :: dataList[id=1010103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] If target’s SP is below 0, inflict 1 [Vulnerable] next turn
   PL:
18. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
19. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1010103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL:
20. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력이 0미만이면 다음 턴에 취약 1 부여
   źródło: Skills.json :: dataList[id=1010103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] If target has less than 0 SP, inflict 1 [Vulnerable] next turn
   PL:
21. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1010104].levelList[level=1].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 7 · monety: 1 (+3)
   limit: do 40 znaków
   EN: Guard
   PL:
22. [Pasywka bojowa (od ulepszenia 1, rezonans 4× Gloom) — nazwa] 정보전달
   źródło: Passives.json :: dataList[id=1010101].name
   limit: do 40 znaków
   EN: Information Relay
   PL:
23. [Pasywka bojowa (od ulepszenia 1, rezonans 4× Gloom) — opis] 조작 패널에서 자신의 뒤에 있는 아군 2명에게 피해량 증가 1 부여
   źródło: Passives.json :: dataList[id=1010101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Apply 1 [AttackDmgUp] to 2 allies placed after this unit on the Dashboard
   PL:
24. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — nazwa] 정보중화
   źródło: Passives.json :: dataList[id=1010121].name
   limit: do 40 znaków
   EN: Information Neutralization
   PL:
25. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — opis] 정신력이 가장 낮은 아군 1명 이번 턴에 정신력이 감소한 경우 턴 종료 시 정신력 10 회복
   źródło: Passives.json :: dataList[id=1010121].desc
   limit: do 120 znaków
   EN: Turn End: If 1 ally that has the lowest SP lost SP this turn, heal 10 SP for the said ally
   PL:
26. [Kwestia głosowa [get_10101_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=get_10101_1].desc
   limit: do 120 znaków
   EN: Identity Acquisition
   PL:
27. [Kwestia głosowa [get_10101_1] (Identity Acquisition)] 이상이라고 하오. 소개는 이상이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=get_10101_1].dlg
   limit: do 120 znaków
   EN: I am Yi Sang. My name is all I have to say.
   PL:
28. [Kwestia głosowa [lobby_morning_10101_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=lobby_morning_10101_1].desc
   limit: do 120 znaków
   EN: Morning Greeting
   PL:
29. [Kwestia głosowa [lobby_morning_10101_1] (Morning Greeting)] 아침은 무사하오? 간밤 동안 잊어버린 것 하나 없이 모든 게 돌아온 것이오?
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=lobby_morning_10101_1].dlg
   limit: do 150 znaków
   EN: Are you sound this morning? Have you returned to the waking world without leaving any memories behind in the night?
   PL:
30. [Kwestia głosowa [lobby_noon_10101_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=lobby_noon_10101_1].desc
   limit: do 120 znaków
   EN: Afternoon Greeting
   PL:
31. [Kwestia głosowa [lobby_noon_10101_1] (Afternoon Greeting)] 해가 내 얼굴을 물끄러미 바라보고 있소. 눈을 감아도 마찬가지오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=lobby_noon_10101_1].dlg
   limit: do 120 znaków
   EN: The sun stares into my face. I can feel its glare even when my eyes are closed.
   PL:
32. [Kwestia głosowa [lobby_night_10101_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=lobby_night_10101_1].desc
   limit: do 120 znaków
   EN: Evening Greeting
   PL:
33. [Kwestia głosowa [lobby_night_10101_1] (Evening Greeting)] 하루가 저물어 가는 동안 나는 그저 서 있을 뿐이었소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=lobby_night_10101_1].dlg
   limit: do 120 znaków
   EN: I have been merely standing here as the day has faded.
   PL:
34. [Kwestia głosowa [smalltalk_10101_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=smalltalk_10101_1].desc
   limit: do 120 znaków
   EN: Chatter #1
   PL:
35. [Kwestia głosowa [smalltalk_10101_1] (Chatter #1)] 그대는 과거로 돌아가는 법을 알아낸 것이오, 아니면 미래를 물러가게 하는 법을 알아낸 것이오?
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=smalltalk_10101_1].dlg
   limit: do 120 znaków
   EN: Have you discovered a way to return to the past, or a way to repel the future?
   PL:
36. [Kwestia głosowa [smalltalk_10101_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=smalltalk_10101_2].desc
   limit: do 120 znaków
   EN: Chatter #2
   PL:
37. [Kwestia głosowa [smalltalk_10101_2] (Chatter #2)] 어느 순간 나는 그저 달리는 걸 멈췄고, 스스로를 이 버스에 유폐시켰소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=smalltalk_10101_2].dlg
   limit: do 120 znaków
   EN: One moment, I stopped my sprint, and confined myself to this bus.
   PL:
38. [Kwestia głosowa [smalltalk_10101_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=smalltalk_10101_3].desc
   limit: do 120 znaków
   EN: Chatter #3
   PL:
39. [Kwestia głosowa [smalltalk_10101_3] (Chatter #3)] 그대의 시계는 멈추는 법이 없군. 포기를 모르고 나를 계속 귀향시키오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=smalltalk_10101_3].dlg
   limit: do 130 znaków
   EN: Your clock doesn’t seem to ever stop. It never ceases to bring me back to home each time I perish.
   PL:
40. [Kwestia głosowa [neglect_10101_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=neglect_10101_1].desc
   limit: do 120 znaków
   EN: Idle
   PL:
41. [Kwestia głosowa [neglect_10101_1] (Idle)] 그대, 드디어 목적지를 찾은 것이오?
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=neglect_10101_1].dlg
   limit: do 120 znaków
   EN: Have you finally located your destination?
   PL:
42. [Kwestia głosowa [formation_10101_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=formation_10101_1].desc
   limit: do 120 znaków
   EN: Deployment
   PL:
43. [Kwestia głosowa [formation_10101_1] (Deployment)] 앞장서시오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=formation_10101_1].dlg
   limit: do 120 znaków
   EN: Lead the way.
   PL:
44. [Kwestia głosowa [battleentry_10101_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battleentry_10101_1].desc
   limit: do 120 znaków
   EN: Stage Entry
   PL:
45. [Kwestia głosowa [battleentry_10101_1] (Stage Entry)] 목적지는 혹이 많소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battleentry_10101_1].dlg
   limit: do 120 znaków
   EN: Our destination has many a bump.
   PL:
46. [Kwestia głosowa [battle_select_10101_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_select_10101_1].desc
   limit: do 120 znaków
   EN: Viewed in Battle
   PL:
47. [Kwestia głosowa [battle_select_10101_1] (Viewed in Battle)] 원하는 것은 찾으셨소?
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_select_10101_1].dlg
   limit: do 120 znaków
   EN: Have you found what you seek?
   PL:
48. [Kwestia głosowa [battle_endcommand_10101_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_endcommand_10101_1].desc
   limit: do 120 znaków
   EN: Commencing Attack
   PL:
49. [Kwestia głosowa [battle_endcommand_10101_1] (Commencing Attack)] 혹들을 제거하겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_endcommand_10101_1].dlg
   limit: do 120 znaków
   EN: I shall remove the bumps.
   PL:
50. [Kwestia głosowa [battle_enemy_break_10101_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_enemy_break_10101_1].desc
   limit: do 120 znaków
   EN: Enemy Stagger
   PL:
51. [Kwestia głosowa [battle_enemy_break_10101_1] (Enemy Stagger)] 저치는 낙역하오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_enemy_break_10101_1].dlg
   limit: do 120 znaków
   EN: Such is the fate of a frequent target.
   PL:
52. [Kwestia głosowa [battle_break_10101_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_break_10101_1].desc
   limit: do 120 znaków
   EN: Staggered
   PL:
53. [Kwestia głosowa [battle_break_10101_1] (Staggered)] 읍…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_break_10101_1].dlg
   limit: do 120 znaków
   EN: Hnf…
   PL:
54. [Kwestia głosowa [battle_kill_10101_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_kill_10101_1].desc
   limit: do 120 znaków
   EN: Enemy Killed
   PL:
55. [Kwestia głosowa [battle_kill_10101_1] (Enemy Killed)] 혹의 거울은 깨졌소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_kill_10101_1].dlg
   limit: do 120 znaków
   EN: The mirror of this bump has shattered.
   PL:
56. [Kwestia głosowa [battle_allydead_10101_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_allydead_10101_1].desc
   limit: do 120 znaków
   EN: Ally Death
   PL:
57. [Kwestia głosowa [battle_allydead_10101_1] (Ally Death)] 그대의 시계가 움직여야겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_allydead_10101_1].dlg
   limit: do 120 znaków
   EN: Your clock shall have to wind.
   PL:
58. [Kwestia głosowa [choice_success_p_10101_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=choice_success_p_10101_1].desc
   limit: do 120 znaków
   EN: Check Passed
   PL:
59. [Kwestia głosowa [choice_success_p_10101_1] (Check Passed)] 유쾌를 맞이했소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=choice_success_p_10101_1].dlg
   limit: do 120 znaków
   EN: I was met with mirth.
   PL:
60. [Kwestia głosowa [choice_fail_n_10101_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=choice_fail_n_10101_1].desc
   limit: do 120 znaków
   EN: Check Failed
   PL:
61. [Kwestia głosowa [choice_fail_n_10101_1] (Check Failed)] 사람은 절망하라.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=choice_fail_n_10101_1].dlg
   limit: do 120 znaków
   EN: Man will despair.
   PL:
62. [Kwestia głosowa [battle_clear_10101_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_clear_10101_1].desc
   limit: do 120 znaków
   EN: Victory Cry
   PL:
63. [Kwestia głosowa [battle_clear_10101_1] (Victory Cry)] 이 또한 영원하지는 않을 것이오. 그렇기에 나는 담담하오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_clear_10101_1].dlg
   limit: do 120 znaków
   EN: I’m certain this shan’t last forever. I am therefore apathetic.
   PL:
64. [Kwestia głosowa [battle_clear_ex_10101_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_clear_ex_10101_1].desc
   limit: do 120 znaków
   EN: Extra Conditions Fulfilled
   PL:
65. [Kwestia głosowa [battle_clear_ex_10101_1] (Extra Conditions Fulfilled)] 혹사에 대한 대가구료. 시들어가는 것 같소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_clear_ex_10101_1].dlg
   limit: do 120 znaków
   EN: The fruits of arduous labor. I feel as though I’m withering.
   PL:
66. [Kwestia głosowa [battle_defeat_10101_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_defeat_10101_1].desc
   limit: do 120 znaków
   EN: Defeat Wail
   PL:
67. [Kwestia głosowa [battle_defeat_10101_1] (Defeat Wail)] 아스라히, 바래지는구료…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCB_10101.json :: dataList[id=battle_defeat_10101_1].dlg
   limit: do 120 znaków
   EN: Thus, in a haze, it pales…
   PL:

## [00] Seven Assoc. South Section 6 — Yi Sang — 남부 세븐 협회 6과
- ID Tożsamości: `10102` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 5–6 / 5–7 / 5–8 / 5–8
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Rupture

68. [Karta Tożsamości — tytuł] 남부 세븐 협회\n6과
   źródło: Personalities.json :: dataList[id=10102].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Seven Assoc.\nSouth Section 6
   PL:
69. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10102].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10102].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
71. [Karta Tożsamości — opis] 이상의 두번째 인격
   źródło: Personalities.json :: dataList[id=10102].desc
   limit: do 120 znaków
   EN: Yi Sang’s 2nd Identity
   PL:
72. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 플레쉬
   źródło: Skills.json :: dataList[id=1010201].levelList[level=1].name ; dataList[id=1010201].levelList[level=2].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Flèche
   PL:
73. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1010201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 1 [Burst]
   PL:
74. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1010201].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 2 [Burst]
   PL:
75. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 리포스트
   źródło: Skills.json :: dataList[id=1010203].levelList[level=1].name ; dataList[id=1010203].levelList[level=2].name ; dataList[id=1010203].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Riposte
   PL:
76. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [WinDuel] 다음 턴에 마비 3 부여
   źródło: Skills.json :: dataList[id=1010203].levelList[level=1].desc ; dataList[id=1010203].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Paralysis]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Paralysis] = 마비 / Paralyze
   EN: [WinDuel] Inflict 3 [Paralysis] next turn
   PL:
77. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills.json :: dataList[id=1010203].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL:
78. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WinDuel] 다음 턴에 마비 3 부여\n[WinDuel] 파열 횟수 1 부여
   źródło: Skills.json :: dataList[id=1010203].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Paralysis], [Burst]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Paralysis] = 마비 / Paralyze; [Burst] = 파열 / Rupture
   EN: [WinDuel] Inflict 3 [Paralysis] next turn\n[WinDuel] Inflict +1 [Burst] Count
   PL:
79. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1010203].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
80. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 물리네
   źródło: Skills.json :: dataList[id=1010202].levelList[level=3].name ; dataList[id=1010202].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Moulinet
   PL:
81. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마지막 코인의 효과 부여 값 + 1
   źródło: Skills.json :: dataList[id=1010202].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Final Coin inflicts +1 more Stack of its effect
   PL:
82. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 마지막 코인의 효과 부여 값 + 1
   źródło: Skills.json :: dataList[id=1010202].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 관통 취약 1 부여
   źródło: Skills.json :: dataList[id=1010202].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1010202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [OnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] next turn
   PL:
84. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마지막 코인의 효과 부여 값 + 1
   źródło: Skills.json :: dataList[id=1010202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Final Coin inflicts +1 more Stack of its effects
   PL:
85. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 마지막 코인의 효과 부여 값 + 1
   źródło: Skills.json :: dataList[id=1010202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1010202].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1010204].levelList[level=1].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 9 · monety: 1 (+3)
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Glut.) — nazwa] 관찰
   źródło: Passives.json :: dataList[id=1010201].name
   limit: do 40 znaków
   EN: Acute Studies
   PL:
89. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Glut.) — opis] 합 진행 시 대상의 합 위력 -2
   źródło: Passives.json :: dataList[id=1010201].desc
   limit: do 120 znaków
   EN: In a Clash, the opponent has Clash Power -2
   PL:
90. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — nazwa] 분석
   źródło: Passives.json :: dataList[id=1010221].name
   limit: do 40 znaków
   EN: Observational Eye
   PL:
91. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — opis] 최대 체력이 가장 높은 아군 1명 합 진행 시 합 위력 +1
   źródło: Passives.json :: dataList[id=1010221].desc
   limit: do 120 znaków
   EN: 1 ally that has the highest max HP gains Clash Power +1 in a Clash
   PL:
92. [Kwestia głosowa [get_10102_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=get_10102_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [Kwestia głosowa [get_10102_1] (Identity Acquisition)] 내게는 어떤 것도 감출 필요가 없소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=get_10102_1].dlg
   limit: do 120 znaków
   EN: You need not hide any secrets from me.
   PL:
94. [Kwestia głosowa [lobby_morning_10102_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=lobby_morning_10102_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Kwestia głosowa [lobby_morning_10102_1] (Morning Greeting)] 어제를 반추하시오. 그걸로 오늘을 구할 수 있을 테니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=lobby_morning_10102_1].dlg
   limit: do 120 znaków
   EN: Ruminate on your yesterday. It shall prove useful for extricating the present from woe.
   PL:
96. [Kwestia głosowa [lobby_noon_10102_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=lobby_noon_10102_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Kwestia głosowa [lobby_noon_10102_1] (Afternoon Greeting)] 태양광선 속에는 무수한 스펙트럼이 있소. 이 세상도 마찬가지로 무수한 비밀들에 둘러싸여 있지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=lobby_noon_10102_1].dlg
   limit: do 150 znaków
   EN: An infinite spectrum comprises the rays of light cast by the sun. Likewise, this world hides countless secrets.
   PL:
98. [Kwestia głosowa [lobby_night_10102_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=lobby_night_10102_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Kwestia głosowa [lobby_night_10102_1] (Evening Greeting)] 어둠 속에 선 밀어들이 속삭이지, 항상 귀를 기울이고 있어야 하오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=lobby_night_10102_1].dlg
   limit: do 120 znaków
   EN: Furtive words are whispered in the dark. You must always have your ear to the ground.
   PL:
100. [Kwestia głosowa [smalltalk_10102_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=smalltalk_10102_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Kwestia głosowa [smalltalk_10102_1] (Chatter #1)] 언젠가 기회가 된다면 내 그대의 머리를 탐구해보고 싶소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=smalltalk_10102_1].dlg
   limit: do 120 znaków
   EN: I would like to study your head if I get the chance one day.
   PL:
102. [Kwestia głosowa [smalltalk_10102_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=smalltalk_10102_2].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Kwestia głosowa [smalltalk_10102_2] (Chatter #2)] 약점이 없는 인간은 없지. 제아무리 화려하고 위험한 기술이더라도 내 앞에선 의미가 없는 까닭이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=smalltalk_10102_2].dlg
   limit: do 150 znaków
   EN: No man is without weakness. It is why no amount of extravagance and intimidation a move poses can threaten me.
   PL:
104. [Kwestia głosowa [smalltalk_10102_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=smalltalk_10102_3].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [Kwestia głosowa [smalltalk_10102_3] (Chatter #3)] 조금만 주의를 기울인다면 많은 정보를 알아낼 수 있소. 가령, 지금 히스클리프 군에게 말을 걸면 좋지 않을 거라는 것 따위 말이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=smalltalk_10102_3].dlg
   limit: do 180 znaków
   EN: A little bit of attention can bring in much information. For instance, you will know that now is not a good time to speak with Heathcliff.
   PL:
106. [Kwestia głosowa [smalltalk_10102_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=smalltalk_10102_4].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 1
   PL:
107. [Kwestia głosowa [smalltalk_10102_4] (Post-Uptie Chat 1)] 혹여나, 그대의 과거가 궁금하다면 내게 의뢰하시오. …사양한다라… 단테, 그대는 볼수록 참 기이하고 흥미롭군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=smalltalk_10102_4].dlg
   limit: do 180 znaków
   EN: If you ever yearn to know your past, merely give me a request. …You’d rather not, I see… Dante, you are such a bizarre and curious specimen.
   PL:
108. [Kwestia głosowa [smalltalk_10102_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=smalltalk_10102_5].desc
   limit: do 120 znaków
   EN: Post-Uptie Chat 2
   PL:
109. [Kwestia głosowa [smalltalk_10102_5] (Post-Uptie Chat 2)] 아직까지는 이곳에 흥미로운 게 많소. 발견의 기쁨은 내 공복을 진정시켜 주지. 그대도 마찬가지요.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=smalltalk_10102_5].dlg
   limit: do 150 znaków
   EN: So far, I have yet to run out of curiosities to find here. The joy of discovery sates my hunger, and so do you.
   PL:
110. [Kwestia głosowa [neglect_10102_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=neglect_10102_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [Kwestia głosowa [neglect_10102_1] (Idle)] 흠… 침묵도 좋은 정보 중 하나지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=neglect_10102_1].dlg
   limit: do 120 znaków
   EN: Hmm… Silence can speak much, in a way.
   PL:
112. [Kwestia głosowa [gacksung_10102_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=gacksung_10102_1].desc
   limit: do 120 znaków
   EN: Uptying
   PL:
113. [Kwestia głosowa [gacksung_10102_1] (Uptying)] 예측하고 있던 사항이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=gacksung_10102_1].dlg
   limit: do 120 znaków
   EN: It was as I expected.
   PL:
114. [Kwestia głosowa [formation_10102_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=formation_10102_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Kwestia głosowa [formation_10102_1] (Deployment)] 지식이 축적될 시간이군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=formation_10102_1].dlg
   limit: do 120 znaków
   EN: It is time to enrich my knowledge.
   PL:
116. [Kwestia głosowa [battleentry_10102_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battleentry_10102_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Kwestia głosowa [battleentry_10102_1] (Stage Entry)] 탐구할 것은 무엇이오?
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battleentry_10102_1].dlg
   limit: do 120 znaków
   EN: What am I to study this time?
   PL:
118. [Kwestia głosowa [battle_select_10102_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_select_10102_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Kwestia głosowa [battle_select_10102_1] (Viewed in Battle)] 저치를 탐구하는 것은 어떻소?
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_select_10102_1].dlg
   limit: do 120 znaków
   EN: How about you examine that one?
   PL:
120. [Kwestia głosowa [battle_endcommand_10102_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_endcommand_10102_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Kwestia głosowa [battle_endcommand_10102_1] (Commencing Attack)] 탐구는 끝났소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_endcommand_10102_1].dlg
   limit: do 120 znaków
   EN: I have finished my studies.
   PL:
122. [Kwestia głosowa [battle_enemy_break_10102_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_enemy_break_10102_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Kwestia głosowa [battle_enemy_break_10102_1] (Enemy Stagger)] 저치의 약점이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_enemy_break_10102_1].dlg
   limit: do 120 znaków
   EN: That one has become vulnerable.
   PL:
124. [Kwestia głosowa [battle_break_10102_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_break_10102_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Kwestia głosowa [battle_break_10102_1] (Staggered)] 앗…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_break_10102_1].dlg
   limit: do 120 znaków
   EN: Oh…
   PL:
126. [Kwestia głosowa [battle_kill_10102_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_kill_10102_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Kwestia głosowa [battle_kill_10102_1] (Enemy Killed)] 침묵했소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_kill_10102_1].dlg
   limit: do 120 znaków
   EN: Fallen into silence.
   PL:
128. [Kwestia głosowa [battle_allydead_10102_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_allydead_10102_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Kwestia głosowa [battle_allydead_10102_1] (Ally Death)] 용태가 썩 보기 좋지 않소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_allydead_10102_1].dlg
   limit: do 120 znaków
   EN: Not the most flattering situation.
   PL:
130. [Kwestia głosowa [choice_success_p_10102_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=choice_success_p_10102_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Kwestia głosowa [choice_success_p_10102_1] (Check Passed)] 예측과도 같소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=choice_success_p_10102_1].dlg
   limit: do 120 znaków
   EN: It is as predicted.
   PL:
132. [Kwestia głosowa [choice_fail_n_10102_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=choice_fail_n_10102_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Kwestia głosowa [choice_fail_n_10102_1] (Check Failed)] 예측 외의 일이오…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=choice_fail_n_10102_1].dlg
   limit: do 120 znaków
   EN: This was unexpected…
   PL:
134. [Kwestia głosowa [battle_clear_10102_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_clear_10102_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Kwestia głosowa [battle_clear_10102_1] (Victory Cry)] 적들의 공격 방식을 분석하는 데 성공했소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_clear_10102_1].dlg
   limit: do 120 znaków
   EN: I’ve successfully analyzed the enemy’s behavior.
   PL:
136. [Kwestia głosowa [battle_clear_ex_10102_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_clear_ex_10102_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Kwestia głosowa [battle_clear_ex_10102_1] (Extra Conditions Fulfilled)] 모두의 약점을 효율적으로 간파했소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_clear_ex_10102_1].dlg
   limit: do 120 znaków
   EN: That was an effective exploitation of their weaknesses.
   PL:
138. [Kwestia głosowa [battle_defeat_10102_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_defeat_10102_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Kwestia głosowa [battle_defeat_10102_1] (Defeat Wail)] 다른 방법을 탐색해봐야겠소…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Seven6_10102.json :: dataList[id=battle_defeat_10102_1].dlg
   limit: do 120 znaków
   EN: We ought to explore other modes…
   PL:

## [000] Blade Lineage Salsu — Yi Sang — 검계 살수
- ID Tożsamości: `10103` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Poise

140. [Karta Tożsamości — tytuł] 검계\n살수
   źródło: Personalities.json :: dataList[id=10103].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Blade Lineage\nSalsu
   PL:
141. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10103].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10103].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Karta Tożsamości — opis] 이상의 세번째 인격
   źródło: Personalities.json :: dataList[id=10103].desc
   limit: do 120 znaków
   EN: Yi Sang’s 3rd Identity
   PL:
144. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 격세
   źródło: Skills.json :: dataList[id=1010301].levelList[level=1].name ; dataList[id=1010301].levelList[level=2].name ; dataList[id=1010301].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 6 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Striker’s Stance
   PL:
145. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1010301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath] next turn
   PL:
146. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 3 얻음
   źródło: Skills.json :: dataList[id=1010301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1010301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath] next turn
   PL:
147. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 호흡 횟수 2 얻음
   źródło: Skills.json :: dataList[id=1010301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL:
148. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 두의틀기
   źródło: Skills.json :: dataList[id=1010302].levelList[level=1].name ; dataList[id=1010302].levelList[level=2].name ; dataList[id=1010302].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 7 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Heel Turn
   PL:
149. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 다음 턴에 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WinDuel] Gain +1 [Breath] Count next turn
   PL:
150. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WinDuel] 다음 턴에 자신의 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1010302].levelList[level=2].desc ; dataList[id=1010302].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WinDuel] Gain +2 [Breath] Count next turn
   PL:
151. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 이면찬자
   źródło: Skills.json :: dataList[id=1010303].levelList[level=3].name ; dataList[id=1010303].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 8 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Flank Thrust
   PL:
152. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1010303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1010303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath] next turn
   PL:
153. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +50%
   źródło: Skills.json :: dataList[id=1010303].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +50% damage on Critical Hit
   PL:
154. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1010303].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 2 [Breath]
   PL:
155. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +70%
   źródło: Skills.json :: dataList[id=1010303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +70% damage on Critical Hit
   PL:
156. [Obrona (ulepszenia 1,4) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1010304].levelList[level=1].name ; dataList[id=1010304].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 10 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Counter
   PL:
157. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] 크리티컬 피해량 +70%
   źródło: Skills.json :: dataList[id=1010304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — nazwa] 냉정
   źródło: Passives.json :: dataList[id=1010301].name
   limit: do 40 znaków
   EN: Poised
   PL:
159. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — opis] 합 승리 시 호흡 횟수 1 증가
   źródło: Passives.json :: dataList[id=1010301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: On Clash Win, gain +1 [Breath] Count
   PL:
160. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — nazwa] 사사
   źródło: Passives.json :: dataList[id=1010321].name
   limit: do 40 znaków
   EN: Bestow
   PL:
161. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — opis] 정신력이 가장 높은 아군 1명 스킬의 효과로 얻는 호흡 횟수 +1
   źródło: Passives.json :: dataList[id=1010321].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: 1 ally that has the highest SP gains +1 more [Breath] Count from Skill effects
   PL:
162. [Kwestia głosowa [get_10103_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=get_10103_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Kwestia głosowa [get_10103_1] (Identity Acquisition)] 나는 유려하면서도 비범하게 심장을 베는 법을 알고 있소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=get_10103_1].dlg
   limit: do 120 znaków
   EN: I know of the ways to cut through a heart with elegance and eccentricity.
   PL:
164. [Kwestia głosowa [lobby_morning_10103_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=lobby_morning_10103_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Kwestia głosowa [lobby_morning_10103_1] (Morning Greeting)] 검의 향연을 이룰 시간이 돌아왔소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=lobby_morning_10103_1].dlg
   limit: do 120 znaków
   EN: It’s time again for a banquet of swordplay.
   PL:
166. [Kwestia głosowa [lobby_noon_10103_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=lobby_noon_10103_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Kwestia głosowa [lobby_noon_10103_1] (Afternoon Greeting)] 웃음이 많은 자들을 조심하시오. 그 허풍 같은 웃음 속엔 칼이 숨어 있소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=lobby_noon_10103_1].dlg
   limit: do 150 znaków
   EN: Be wary of those with plenty of laughs and smiles to show. A sharp edge lurks beneath that deceptive expression.
   PL:
168. [Kwestia głosowa [lobby_night_10103_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=lobby_night_10103_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Kwestia głosowa [lobby_night_10103_1] (Evening Greeting)] 달빛은 마음에 들지 않소. 비추면 안 될 것을 구태여 환히 돋보이게 만들기만 하니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=lobby_night_10103_1].dlg
   limit: do 120 znaków
   EN: I do not enjoy the moonlight much. All it does is shed a gleam on what should be left unlit.
   PL:
170. [Kwestia głosowa [smalltalk_10103_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=smalltalk_10103_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Kwestia głosowa [smalltalk_10103_1] (Chatter #1)] 이 흉터들 말이오? 이제 아물었소. 그보다는… 이 흉터를 만들어낸 이들이 어떻게 되었는지 물어봐야 하는 것이 아니오?
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=smalltalk_10103_1].dlg
   limit: do 160 znaków
   EN: These scars? They are healed up now. Rather than that… shouldn’t you be asking what became of those who left them on me?
   PL:
172. [Kwestia głosowa [smalltalk_10103_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=smalltalk_10103_2].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Kwestia głosowa [smalltalk_10103_2] (Chatter #2)] 제아무리 잘 벼려진 검이라도 아니 든다면 무용에 불과하지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=smalltalk_10103_2].dlg
   limit: do 120 znaków
   EN: The sharpest blade has no meaning if it lies unused.
   PL:
174. [Kwestia głosowa [smalltalk_10103_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=smalltalk_10103_3].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Kwestia głosowa [smalltalk_10103_3] (Chatter #3)] 내 옛날을 묻는 것이오? 그러한 것들은… 옛적에 모두 베어버렸소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=smalltalk_10103_3].dlg
   limit: do 120 znaków
   EN: Are you curious of my past? Such things… have all been cut off long ago.
   PL:
176. [Kwestia głosowa [smalltalk_10103_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=smalltalk_10103_4].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Kwestia głosowa [smalltalk_10103_4] (Post-Uptie Chat 1)] 비밀을 하나 말해주자면 난 눈과 귀를 막고도 적을 벨 수 있소. …농이오. 단테, 그대는 참으로 순진하군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=smalltalk_10103_4].dlg
   limit: do 160 znaków
   EN: To tell you a secret, I can slay a foe with both my eyes and ears closed. …I was in jest. Dante, you truly are credulous.
   PL:
178. [Kwestia głosowa [smalltalk_10103_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=smalltalk_10103_5].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Kwestia głosowa [smalltalk_10103_5] (Post-Uptie Chat 2)] 지금까지 시계는 내게 그저 무용한 것에 불과했는데 말이오. 단테, 그대의 시계는 참으로 매혹적일 만큼 이상스러워.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=smalltalk_10103_5].dlg
   limit: do 160 znaków
   EN: Until now, a clock was nothing more than a useless thing to me. Yours, however, has such a peculiar charm to it, Dante.
   PL:
180. [Kwestia głosowa [neglect_10103_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=neglect_10103_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Kwestia głosowa [neglect_10103_1] (Idle)] 그대, 대화가 끝났다고 바로 돌아서다니, 퍽 냉정하군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=neglect_10103_1].dlg
   limit: do 120 znaków
   EN: You’re rather cold, turning away the moment a conversation dies down.
   PL:
182. [Kwestia głosowa [gacksung_10103_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=gacksung_10103_1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Kwestia głosowa [gacksung_10103_1] (Uptying)] 검이 부러질 때까지 함께 하겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=gacksung_10103_1].dlg
   limit: do 120 znaków
   EN: I shall stay by your side until my sword breaks.
   PL:
184. [Kwestia głosowa [formation_10103_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=formation_10103_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Kwestia głosowa [formation_10103_1] (Deployment)] 피가 범람할 시간이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=formation_10103_1].dlg
   limit: do 120 znaków
   EN: It’s time to raise a deluge of blood.
   PL:
186. [Kwestia głosowa [battleentry_10103_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battleentry_10103_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Kwestia głosowa [battleentry_10103_1] (Stage Entry)] 그대, 이 검이 필요하오?
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battleentry_10103_1].dlg
   limit: do 120 znaków
   EN: Are you in need of this blade?
   PL:
188. [Kwestia głosowa [battle_select_10103_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_select_10103_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Kwestia głosowa [battle_select_10103_1] (Viewed in Battle)] 검은 아직 벼려있소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_select_10103_1].dlg
   limit: do 120 znaków
   EN: The sword is still sharp.
   PL:
190. [Kwestia głosowa [battle_endcommand_10103_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_endcommand_10103_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Kwestia głosowa [battle_endcommand_10103_1] (Commencing Attack)] 죄를 새겨주겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_endcommand_10103_1].dlg
   limit: do 120 znaków
   EN: I shall carve the sin unto you.
   PL:
192. [Kwestia głosowa [battle_enemy_break_10103_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_enemy_break_10103_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Kwestia głosowa [battle_enemy_break_10103_1] (Enemy Stagger)] 혈이 낭자하오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_enemy_break_10103_1].dlg
   limit: do 120 znaków
   EN: It’s bloodshed.
   PL:
194. [Kwestia głosowa [battle_break_10103_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_break_10103_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Kwestia głosowa [battle_break_10103_1] (Staggered)] 흠…
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_break_10103_1].dlg
   limit: do 120 znaków
   EN: Hmh…
   PL:
196. [Kwestia głosowa [battle_kill_10103_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_kill_10103_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Kwestia głosowa [battle_kill_10103_1] (Enemy Killed)] 흉터의 결과요.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_kill_10103_1].dlg
   limit: do 120 znaków
   EN: A consequence of the scars.
   PL:
198. [Kwestia głosowa [battle_allydead_10103_1] — sytuacja] 아군 사망
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_allydead_10103_1].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Kwestia głosowa [battle_allydead_10103_1] (Ally Death)] 흉터는 남지 않을 것이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_allydead_10103_1].dlg
   limit: do 120 znaków
   EN: This will leave a scar not.
   PL:
200. [Kwestia głosowa [choice_success_p_10103_1] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=choice_success_p_10103_1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Kwestia głosowa [choice_success_p_10103_1] (Check Passed)] 흉터는 경험이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=choice_success_p_10103_1].dlg
   limit: do 120 znaków
   EN: Scars signify experience.
   PL:
202. [Kwestia głosowa [choice_fail_n_10103_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=choice_fail_n_10103_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Kwestia głosowa [choice_fail_n_10103_1] (Check Failed)] 묘혈을 판 것 같소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=choice_fail_n_10103_1].dlg
   limit: do 120 znaków
   EN: It would seem that I dug a grave.
   PL:
204. [Kwestia głosowa [battle_clear_10103_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_clear_10103_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Kwestia głosowa [battle_clear_10103_1] (Victory Cry)] 저들이 순응을 아는 자들이기에 다행이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_clear_10103_1].dlg
   limit: do 120 znaków
   EN: I am relieved to see that they know to comply.
   PL:
206. [Kwestia głosowa [battle_clear_ex_10103_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_clear_ex_10103_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Kwestia głosowa [battle_clear_ex_10103_1] (Extra Conditions Fulfilled)] 갈가리 베어버렸소. 이보다 정신이 맑을 때가 없군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_clear_ex_10103_1].dlg
   limit: do 120 znaków
   EN: I shred them to pieces. My mind is now clearer than ever.
   PL:
208. [Kwestia głosowa [battle_defeat_10103_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_defeat_10103_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Kwestia głosowa [battle_defeat_10103_1] (Defeat Wail)] 내 검은 만족할 만큼 베어냈소. 그러니 미련은 없지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_SwordGroup_10103.json :: dataList[id=battle_defeat_10103_1].dlg
   limit: do 120 znaków
   EN: My sword has cut its fair share. Nothing stops me from accepting this result.
   PL:

## [000] Effloresced E.G.O::Spicebush — Yi Sang — 개화 E.G.O:: 동백
- ID Tożsamości: `10104` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 2 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Tremor, Sinking

210. [Karta Tożsamości — tytuł] 개화 E.G.O::\n동백
   źródło: Personalities.json :: dataList[id=10104].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Effloresced E.G.O::Spicebush
   PL:
211. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10104].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10104].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Karta Tożsamości — opis] 이상의 네번째 인격
   źródło: Personalities.json :: dataList[id=10104].desc
   limit: do 120 znaków
   EN: Yi Sang’s 4th Identity
   PL:
214. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 움트는 봉우리
   źródło: Skills.json :: dataList[id=1010401].levelList[level=1].name ; dataList[id=1010401].levelList[level=2].name ; dataList[id=1010401].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 3 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Sprouting Bud
   PL:
215. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 진동 횟수 2를 얻음
   źródło: Skills.json :: dataList[id=1010401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count
   PL:
216. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +1 [Sinking] Count next turn
   PL:
217. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010401].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] [WhenUse] 진동 횟수 3을 얻음
   źródło: Skills.json :: dataList[id=1010401].levelList[level=2].desc ; dataList[id=1010401].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count
   PL:
219. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count next turn
   PL:
220. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010401].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 침잠 횟수 2 증가
   źródło: Skills.json :: dataList[id=1010401].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count next turn
   PL:
222. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 찰나의 꽃바람
   źródło: Skills.json :: dataList[id=1010402].levelList[level=1].name ; dataList[id=1010402].levelList[level=2].name ; dataList[id=1010402].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Moment's Floral Breeze
   PL:
223. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [StartBattle] 자신의 진동 횟수를 6 소모하여 공격 가중치 3 스킬로 변경
   źródło: Skills.json :: dataList[id=1010402].levelList[level=1].desc ; dataList[id=1010402].levelList[level=2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] Consume 6 [Vibration] Count on self to turn this into an AoE skill with 3 Atk Weight
   PL:
224. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 2 [Sinking] next turn
   PL:
225. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1010402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] next turn
   PL:
228. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 침잠 2 부여
   źródło: Skills.json :: dataList[id=1010402].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1010402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [StartBattle] 자신의 진동 횟수를 6 소모하여 공격 가중치 3 스킬로 변경\n메인 타겟의 침잠 횟수가 6 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1010402].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Vibration], [Sinking]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: [StartBattle] Consume 6 [Vibration] Count on self to turn this into an AoE skill with 3 Atk Weight\nIf main target has 6+ [Sinking] Count, Coin Power +1
   PL:
231. [Umiejętność 3 (×1) (ulepszenia 1,4) — nazwa] 피를 머금은 향기
   źródło: Skills.json :: dataList[id=1010403].levelList[level=1].name ; dataList[id=1010403].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 6 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Bloodsteeped Scent
   PL:
232. [Umiejętność 3 (×1) (ulepszenia 1,4) — opis] [DefeatDuel] 정신력 20 감소\n[WhenUse] 진동 횟수 6을 얻음
   źródło: Skills.json :: dataList[id=1010403].levelList[level=1].desc ; dataList[id=1010403].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel], [WhenUse], [Vibration]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [DefeatDuel] Lose 20 SP\n[WhenUse] Gain +6 [Vibration] Count
   PL:
233. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010403].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1010403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count
   PL:
234. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1010403].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1010403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]이 6 이상이면, 침잠쇄도
   źródło: Skills.json :: dataList[id=1010403].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1010403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [SinkingSurge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [SinkingSurge] = 침잠쇄도 / Sinking Deluge
   EN: [OnSucceedAttack] If target has 6+ [Sinking], cause [SinkingSurge]
   PL:
236. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 진동 횟수가 10 이상이면, 피해량의 30%만큼 추가 피해
   źródło: Skills.json :: dataList[id=1010403].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this unit has 10+ [Vibration] Count, deal 30% of damage dealt as bonus damage
   PL:
237. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 진동 횟수가 10 이상이면, 피해량의 40%만큼 추가 피해
   źródło: Skills.json :: dataList[id=1010403].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this unit has 10+ [Vibration] Count, deal 40% of damage dealt as bonus damage
   PL:
238. [Obrona (ulepszenie 1) — nazwa] 흩날리는 잔향
   źródło: Skills.json :: dataList[id=1010404].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Scattering Aroma
   PL:
239. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1010404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Sinking]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedEvade] Inflict 1 [Sinking]
   PL:
240. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Sloth) — nazwa] 만개
   źródło: Passives.json :: dataList[id=1010401].name
   limit: do 40 znaków
   EN: Full Bloom
   PL:
241. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Sloth) — opis] 2명 이상을 공격할 때 피해량 +30%
   źródło: Passives.json :: dataList[id=1010401].desc
   limit: do 120 znaków
   EN: When attacking 2 or more targets at once, deal +30% damage
   PL:
242. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — nazwa] 알싸한 봄바람
   źródło: Passives.json :: dataList[id=1010421].name
   limit: do 40 znaków
   EN: Pungent Spring Breeze
   PL:
243. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — opis] 정신력이 가장 낮은 아군 1명이 2명 이상을 공격할 때 피해량 +10%
   źródło: Passives.json :: dataList[id=1010421].desc
   limit: do 120 znaków
   EN: 1 ally that has the lowest SP deals +10% damage when attacking 2 or more targets at once
   PL:
244. [Kwestia głosowa [get_10104_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=get_10104_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Kwestia głosowa [get_10104_1] (Identity Acquisition)] 어서 오시게. 내 마음이… 마음에 드오?
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=get_10104_1].dlg
   limit: do 120 znaków
   EN: Welcome. Now what does your heart say... about what you see of my heart?
   PL:
246. [Kwestia głosowa [lobby_morning_10104_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=lobby_morning_10104_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Kwestia głosowa [lobby_morning_10104_1] (Morning Greeting)] 장지는 그대로 열어두게. 볕이… 간만에 따스하니까.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=lobby_morning_10104_1].dlg
   limit: do 120 znaków
   EN: Keep the door ajar. The sunbeam... is warm for once.
   PL:
248. [Kwestia głosowa [lobby_noon_10104_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=lobby_noon_10104_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Kwestia głosowa [lobby_noon_10104_1] (Afternoon Greeting)] 식사는 하셨는가. 어디… 감자는 어떻소? 점심에 퍽 어울리오.\n…싹은 나지 않았으니, 걱정마시게.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=lobby_noon_10104_1].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I wonder if you have dined. Let's see... How about potatoes? They are quite fitting as luncheon.\n...Worry not, for they have not sprouted.
   PL:
250. [Kwestia głosowa [lobby_night_10104_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=lobby_night_10104_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Kwestia głosowa [lobby_night_10104_1] (Evening Greeting)] 밤은 익숙치 않소… 한치 앞이 보이지 아니하기 때문이요.\n스러져간 새 동료들을 떠올리면… 또 다시 적적함 속에 삼켜질까봐 두렵기도 하오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=lobby_night_10104_1].dlg
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I am not quite used to the night... It's thanks to the dark that prevents me from seeing further than my nose.\nThinking of my new colleagues who have perished... this solitude brings me fear that I will soon be consumed by another.
   PL:
252. [Kwestia głosowa [smalltalk_10104_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=smalltalk_10104_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Kwestia głosowa [smalltalk_10104_1] (Chatter #1)] K사의 그자 말인가. 이제는 벗도 뭣도 아니며, 그저 더러운 사상을 갖고 기술을 능욕하는… 아니, 굳이 입까지 더럽힐 필요는 없지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=smalltalk_10104_1].dlg
   limit: do 290 znaków
   EN: You wish to hear my thoughts on that man in K Corp. He is no longer a companion or anyone worth mentioning; he is no more than a worm with wretched ideas, humiliating technology with... nay, there is no need to sully my tongue.
   PL:
254. [Kwestia głosowa [smalltalk_10104_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=smalltalk_10104_2].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Kwestia głosowa [smalltalk_10104_2] (Chatter #2)] …가끔 그렇게 생각하지 않소? 대단히 빼어난 것을 보고나서, 차라리 이것을 더 나누고 싶다고.\n처음 그것을 보았던 순간을, 누가 되었던 다시 겪게 하고 싶은 것이지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=smalltalk_10104_2].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ...Does it sometimes occur to you when you see a remarkable thing that you want to share the wonderment with others?\nThat you would like anyone to experience the same moment when you first saw it.
   PL:
256. [Kwestia głosowa [smalltalk_10104_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=smalltalk_10104_3].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Kwestia głosowa [smalltalk_10104_3] (Chatter #3)] 닭들이 싸우는 것을 본 적이 있소. 덩치가 작은 놈이 항상 머리를 쪼이기 일쑤 였지.\n여직 우리도 그러했으나… 어디, 언제까지 그럴지. 곧 알게 되지 않겠는가.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=smalltalk_10104_3].dlg
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I have seen chickens fight. The smaller one was always being pecked on its head.\nWe have been similar until now... but will that last? It will come to light soon enough.
   PL:
258. [Kwestia głosowa [smalltalk_10104_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=smalltalk_10104_4].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Kwestia głosowa [smalltalk_10104_4] (Post-Uptie Chat 1)] 알싸한 향이 나지 않는가. 땅에 고꾸라질 정도로 정신이 아찔해지는… 짙고도 향긋한 향이지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=smalltalk_10104_4].dlg
   limit: do 200 znaków
   EN: It makes a pungent smell, does it not? It strikes your senses so intensely, you might almost fall to the ground... Such a deep and fragrant scent, it is.
   PL:
260. [Kwestia głosowa [smalltalk_10104_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=smalltalk_10104_5].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Kwestia głosowa [smalltalk_10104_5] (Post-Uptie Chat 2)] 어찌, 사람 얼굴을 그리 뚫어지게 쳐다보오. 그래… 잠시 넋이라도 나갔었나보오?
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=smalltalk_10104_5].dlg
   limit: do 140 znaków
   EN: Pray, for what reason do you stare so intently into my face? I see... Were you enraptured for a moment?
   PL:
262. [Kwestia głosowa [neglect_10104_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=neglect_10104_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Kwestia głosowa [neglect_10104_1] (Idle)] 그래, 그대도 하던 일 마저 보시게.\n피차, 서로의 목표가 더 중요한 법이지 않겠나.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=neglect_10104_1].dlg
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: RIght, then. Go back to tending to your business if you insist.\nAfter all, nothing matters more to us than our goals.
   PL:
264. [Kwestia głosowa [gacksung_10104_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=gacksung_10104_1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Kwestia głosowa [gacksung_10104_1] (Uptying)] 자… 보시게. 흐드러지게 피어나지 않았는가.\n이 꽃 모두를 붉게 물들이면… 비로소, '나'또한 피어날테요.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=gacksung_10104_1].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Now... Behold. These flowers are in full glory.\nOnce all these flowers have been stained red... that shall be when 'I' bloom as well.
   PL:
266. [Kwestia głosowa [formation_10104_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=formation_10104_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Kwestia głosowa [formation_10104_1] (Deployment)] 재촉치 마시오. 어련히 가겠지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=formation_10104_1].dlg
   limit: do 120 znaków
   EN: Press me not. I'll be on my way when I need to.
   PL:
268. [Kwestia głosowa [battleentry_10104_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battleentry_10104_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Kwestia głosowa [battleentry_10104_1] (Stage Entry)] …순수했던 나날로.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battleentry_10104_1].dlg
   limit: do 120 znaków
   EN: ...To the innocent times.
   PL:
270. [Kwestia głosowa [battle_select_10104_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_select_10104_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Kwestia głosowa [battle_select_10104_1] (Viewed in Battle)] 불렀는가?
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_select_10104_1].dlg
   limit: do 120 znaków
   EN: Did you call me?
   PL:
272. [Kwestia głosowa [battle_endcommand_10104_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_endcommand_10104_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Kwestia głosowa [battle_endcommand_10104_1] (Commencing Attack)] 피워보지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_endcommand_10104_1].dlg
   limit: do 120 znaków
   EN: Let's make it bloom.
   PL:
274. [Kwestia głosowa [battle_enemy_break_10104_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_enemy_break_10104_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Kwestia głosowa [battle_enemy_break_10104_1] (Enemy Stagger)] 흐드러졌구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_enemy_break_10104_1].dlg
   limit: do 120 znaków
   EN: So did they bloom.
   PL:
276. [Kwestia głosowa [battle_break_10104_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_break_10104_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Kwestia głosowa [battle_break_10104_1] (Staggered)] 아아… 이런.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_break_10104_1].dlg
   limit: do 120 znaków
   EN: Ahh... Dear.
   PL:
278. [Kwestia głosowa [battle_kill_10104_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_kill_10104_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Kwestia głosowa [battle_kill_10104_1] (Enemy Killed)] 다시 못살게 구는 일은 없을 것이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_kill_10104_1].dlg
   limit: do 120 znaków
   EN: They will not be tormenting anyone any longer.
   PL:
280. [Kwestia głosowa [battle_dead_10104_1] — sytuacja] 본인 사망 시
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_dead_10104_1].desc
   limit: do 120 znaków
   EN: Death
   PL:
281. [Kwestia głosowa [battle_dead_10104_1] (Death)] 때가… 되면… 시들 수 밖에 없는 운명…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_dead_10104_1].dlg
   limit: do 120 znaków
   EN: When... the time comes... I would have to wilt...
   PL:
282. [Kwestia głosowa [choice_success_p_10104_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=choice_success_p_10104_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Kwestia głosowa [choice_success_p_10104_2] (Check Passed)] 고맙소, 이런 순간을 보여주어.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=choice_success_p_10104_2].dlg
   limit: do 120 znaków
   EN: Thank you for showing me such a moment.
   PL:
284. [Kwestia głosowa [choice_fail_n_10104_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=choice_fail_n_10104_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Kwestia głosowa [choice_fail_n_10104_1] (Check Failed)] …흙을 덮어두는게 어떻겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=choice_fail_n_10104_1].dlg
   limit: do 120 znaków
   EN: ...Let's cover this moment with dirt, shall we.
   PL:
286. [Kwestia głosowa [battle_clear_10104_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_clear_10104_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Kwestia głosowa [battle_clear_10104_1] (Victory Cry)] 봉오리가 폈구료. 결실을 맺은게로지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_clear_10104_1].dlg
   limit: do 120 znaków
   EN: The bud has risen. Effort has borne fruit.
   PL:
288. [Kwestia głosowa [battle_clear_ex_10104_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_clear_ex_10104_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Kwestia głosowa [battle_clear_ex_10104_1] (Extra Conditions Fulfilled)] 개화하였구료… 이 순간을 어딘가에 담고 싶군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_clear_ex_10104_1].dlg
   limit: do 120 znaków
   EN: So it has bloomed... I would like to capture this moment somewhere.
   PL:
290. [Kwestia głosowa [battle_defeat_10104_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_defeat_10104_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Kwestia głosowa [battle_defeat_10104_1] (Defeat Wail)] 여직 운이 좋았던 것 뿐이지… 그저, 지금껏 우리가 판 땅이 비옥했던 것 뿐…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LEGO_10104.json :: dataList[id=battle_defeat_10104_1].dlg
   limit: do 130 znaków
   EN: We were simply in fortune's favor until now... It was only the land we tilled that was fertile...
   PL:

## [00] Molar Office Fixer — Yi Sang — 어금니 사무소 해결사
- ID Tożsamości: `10105` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 2 · HP bazowe: 73 · szybkość: 3–6 / 4–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Tremor

292. [Karta Tożsamości — tytuł] 어금니 사무소\n해결사
   źródło: Personalities.json :: dataList[id=10105].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Molar Office\nFixer
   PL:
293. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10105].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10105].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Karta Tożsamości — opis] 이상의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10105].desc
   limit: do 120 znaków
   EN: Yi Sang's 5th Identity
   PL:
296. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 침착하게
   źródło: Skills_personality-01.json :: dataList[id=1010501].levelList[level=1].name ; dataList[id=1010501].levelList[level=2].name ; dataList[id=1010501].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Stay Calm
   PL:
297. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 이 스킬이 버려지면 자신의 진동 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1010501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If this Skill is Discarded, gain +3 [Vibration] Count
   PL:
298. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict +2 [Vibration] Count
   PL:
299. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 이 스킬이 버려지면 자신의 진동 횟수 4 증가\n[WhenUse] 자신의 진동 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010501].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: If this Skill is Discarded, gain +4 [Vibration] Count\n[WhenUse] Gain +2 [Vibration] Count
   PL:
300. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
301. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 이 스킬이 버려지면 자신의 진동 횟수 4 증가\n[WhenUse] 자신의 진동 횟수 2 증가\n자신의 진동 횟수가 5 이상일 때 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010501].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: If this Skill is Discarded, gain +4 [Vibration] Count\n[WhenUse] Gain +2 [Vibration] Count\nAt 5+ [Vibration] Count, gain Coin Power +1
   PL:
302. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 도박수
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=1].name ; dataList[id=1010502].levelList[level=2].name ; dataList[id=1010502].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Gamble
   PL:
303. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 이 스킬이 버려지면 자신의 진동 횟수 3 증가\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: If this Skill is Discarded, gain +3 [Vibration] Count\n[WhenUse] Discard 1 Skill of the lowest rank in all of this unit's Skill Slots
   PL:
304. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수가 5 이상일 때, 진동 폭발. 대상의 진동 횟수 2 감소
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] At 5+ [Vibration] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 2
   PL:
305. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] 이 스킬이 버려지면 자신의 진동 횟수 4 증가\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=2].desc ; dataList[id=1010502].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: If this Skill is Discarded, gain +4 [Vibration] Count\n[WhenUse] Discard 1 Skill of the lowest rank in all of this unit's Skill Slots
   PL:
306. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 300 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 진동 횟수가 5 이상일 때, 진동 폭발. 대상의 진동 횟수 2 감소
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1010502].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1010502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL:
309. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 어금니 갈기
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=3].name ; dataList[id=1010503].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Grinding the Molars
   PL:
310. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림.\n[WhenUse] 자신의 진동 횟수 10을 소모하여 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Discard 1 Skill of the lowest rank in all of this unit's Skill Slots\n[WhenUse] Consume 10 [Vibration] Count on self to gain Coin Power +1
   PL:
311. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 4 부여
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1010503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]
   PL:
312. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 스킬 사용 시 진동 횟수를 소모했으면, 진동 폭발
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1010503].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If the Skill consumed [Vibration] Count, trigger [VibrationExplosion]
   PL:
313. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 방어 레벨 감소 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttackHead] Inflict 2 [DefenseDown]
   PL:
314. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 스킬 사용 시 진동 횟수를 소모했으면, 진동 폭발
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1010503].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림.\n[WhenUse] 자신의 진동 횟수 10을 소모하여 코인 위력 +2
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Discard 1 Skill of the lowest rank in all of this unit's Skill Slots\n[WhenUse] Consume 10 [Vibration] Count on self to gain Coin Power +2
   PL:
316. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 방어 레벨 감소 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown]
   PL:
317. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-01.json :: dataList[id=1010504].levelList[level=1].name ; dataList[id=1010504].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+5)
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Obrona (ulepszenia 1,4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림
   źródło: Skills_personality-01.json :: dataList[id=1010504].levelList[level=1].desc ; dataList[id=1010504].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Discard 1 Skill of the lowest rank in all of this unit's Skill Slots
   PL:
319. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — nazwa] 이럴 때 일수록...
   źródło: Passives.json :: dataList[id=1010501].name
   limit: do 40 znaków
   EN: In Times Like These...
   PL:
320. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — opis] 적에게 진동 폭발 시 입히는 흐트러짐 손상 4 당 [DefenseDown] 1 부여 (턴마다 적 1명당 최대 5)
   źródło: Passives.json :: dataList[id=1010501].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [DefenseDown], [VibrationExplosion]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: Upon triggering [VibrationExplosion] on an enemy, inflict 1 [DefenseDown] for every 4 Stagger Threshold raised (max 5 [DefenseDown] per enemy per turn)
   PL:
321. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — nazwa] 벌려진 일 수습
   źródło: Passives.json :: dataList[id=1010521].name
   limit: do 40 znaków
   EN: Cleaning Up the Mess
   PL:
322. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — opis] 최대 체력이 가장 낮은 아군 1명이 적에게 진동 폭발 시 입히는 흐트러짐 손상 4 당 다음 턴에 [DefenseDown] 1 부여 (턴마다 적 1명당 최대 3)
   źródło: Passives.json :: dataList[id=1010521].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [DefenseDown], [VibrationExplosion]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: 1 ally that has the lowest max HP: For every 4 Stagger Threshold raised by triggering [VibrationExplosion] on an enemy, inflict 1 [DefenseDown] next turn (max 3 [DefenseDown] per enemy per turn)
   PL:
323. [Kwestia głosowa [get_10105_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=get_10105_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Kwestia głosowa [get_10105_1] (Identity Acquisition)] 결국, 우리가 나서서 처리해야겠구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=get_10105_1].dlg
   limit: do 120 znaków
   EN: Alas, it appears that we must involve ourselves in this matter.
   PL:
325. [Kwestia głosowa [lobby_morning_10105_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=lobby_morning_10105_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [Kwestia głosowa [lobby_morning_10105_1] (Morning Greeting)] 더 없이 평소와 같은, 평범한 아침이구료. 의뢰 관련이라면, 사무실 안쪽으로 들어오시오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=lobby_morning_10105_1].dlg
   limit: do 210 znaków
   EN: Thus it is a morning like any other, its patterns forever unchanging. If you have a matter concerning a contract, please make yourself comfortable in our office.
   PL:
327. [Kwestia głosowa [lobby_noon_10105_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=lobby_noon_10105_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Kwestia głosowa [lobby_noon_10105_1] (Afternoon Greeting)] 음… 하루의 절반이 지나갔군. 그대는 안녕하오?
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=lobby_noon_10105_1].dlg
   limit: do 120 znaków
   EN: Hmm... Half a day remains. How do you fare?
   PL:
329. [Kwestia głosowa [lobby_night_10105_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=lobby_night_10105_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Kwestia głosowa [lobby_night_10105_1] (Evening Greeting)] 야밤에 퇴근하지 못하는 것이 불행해보일 수는 있으나… 그것도 처리해야 할 일이 있다는 뜻이니 나쁜 것만은 아니오.\n의뢰 하나 없는 사무소도 도시에 한 가득이니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=lobby_night_10105_1].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Though it may appear pitiable that I am working so late into the night... it is not entirely unideal, as it signifies that there is work to be done.\nMany Offices in this city oft go days with nary a proper contract.
   PL:
331. [Kwestia głosowa [smalltalk_10105_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=smalltalk_10105_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Kwestia głosowa [smalltalk_10105_1] (Chatter #1)] 의뢰를 받아 일을 처리하겠다면, 공식적으로 계약서를 작성해야 하오.\n뭐… 말이 거창할 뿐, 그저 서로에 대한 약속을 하겠다는 것 뿐이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=smalltalk_10105_1].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: An official contract must first be drafted and signed, if we are to accept a request.\nWell... there is no need to be intimidated. It is but a simple covenant betwixt two entities.
   PL:
333. [Kwestia głosowa [smalltalk_10105_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=smalltalk_10105_2].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Kwestia głosowa [smalltalk_10105_2] (Chatter #2)] 누님께서는… 바깥 일을 나가셨소. 전할 말이 있다면 대신 전해 주겠소.\n…연락처를 부탁하는 건 적절치 않아 보이오. 틀림 없이 대화가 통할 상태는 아닐테니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=smalltalk_10105_2].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Big Sister is... occupied with an outside business at the moment. If there are any words you must pass on to her, you may say them unto me.\n... Asking for her contact information... may be unwise. I can speak with certitude that she is not in an ideal state to engage in dialogue.
   PL:
335. [Kwestia głosowa [smalltalk_10105_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=smalltalk_10105_3].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Kwestia głosowa [smalltalk_10105_3] (Chatter #3)] 이 무기를 말하는 것이오? 당연히 공방을 통해 만들어진 제품이오.\n개조…? 허어, 그럴 필요는 없지 않겠소? 내가 그럴 일도 없을 것이라보오만.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=smalltalk_10105_3].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You ask of this weapon? It is a handicraft of a workshop, indeed.\nModifications...? Hmm, why would there be a need for modifications? I do not see myself tampering with its build, either.
   PL:
337. [Kwestia głosowa [smalltalk_10105_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=smalltalk_10105_4].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Kwestia głosowa [smalltalk_10105_4] (Post-Uptie Chat 1)] 협회에서 오는 의뢰와 날개에서 오는 의뢰는 그 무게가 다르오. 날개가 일개 사무소에 의뢰를 맡긴다는건 그만한 인정을 받았다는 것일테니.\n이번 R사의 의뢰도 그런 의미에서 아주 무거운… 의뢰지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=smalltalk_10105_4].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Contracts from Associations and contracts from Wings carry entirely different levels of significance. To be contracted by a Wing is to have our competency acknowledged.\nThus, this contract from R Corp. is also... something of grave importance.
   PL:
339. [Kwestia głosowa [smalltalk_10105_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=smalltalk_10105_5].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Kwestia głosowa [smalltalk_10105_5] (Post-Uptie Chat 2)] 한편으로는 걱정이 되는 것도 사실이나… 또 어마어마한 기회임을 십분 알고 있기에.\n누님만 잘 보필하면, 해결할 수 있을 거라 믿소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=smalltalk_10105_5].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: While I do have my reservations... I also understand that it may be a marvelous opportunity.\nI am hopeful that we should be able to fulfill this contract as long as I prove to be a sufficient support for Big Sister.
   PL:
341. [Kwestia głosowa [neglect_10105_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=neglect_10105_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Kwestia głosowa [neglect_10105_1] (Idle)] 남는 시간은 서류 정리를 해두는 게 좋겠군. 이럴 때일수록… 늘어지면 안 되오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=neglect_10105_1].dlg
   limit: do 130 znaków
   EN: I shall use this downtime to catalogue our documents. One must not idle... in times such as these.
   PL:
343. [Kwestia głosowa [gacksung_10105_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=gacksung_10105_1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Kwestia głosowa [gacksung_10105_1] (Uptying)] 흠. 무거운 신뢰를 받게 되었구료. 기대에 보답하게 노력하겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=gacksung_10105_1].dlg
   limit: do 120 znaków
   EN: Hm. This is quite the responsibility. I shall try my best to live up to your expectations.
   PL:
345. [Kwestia głosowa [formation_10105_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=formation_10105_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Kwestia głosowa [formation_10105_1] (Deployment)] 출발하는가, 따라 가겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=formation_10105_1].dlg
   limit: do 120 znaków
   EN: Departure, is it? Allow me to accompany you.
   PL:
347. [Kwestia głosowa [battleentry_10105_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battleentry_10105_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Kwestia głosowa [battleentry_10105_1] (Stage Entry)] 좋은 경험이 되기를.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battleentry_10105_1].dlg
   limit: do 120 znaków
   EN: Let this be a positive experience for us all.
   PL:
349. [Kwestia głosowa [battle_select_10105_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_select_10105_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Kwestia głosowa [battle_select_10105_1] (Viewed in Battle)] 아직은 이상, 없소만.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_select_10105_1].dlg
   limit: do 120 znaków
   EN: The situation has hitherto been quite... ideal.
   PL:
351. [Kwestia głosowa [battle_endcommand_10105_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_endcommand_10105_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Kwestia głosowa [battle_endcommand_10105_1] (Commencing Attack)] 침착하게.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_endcommand_10105_1].dlg
   limit: do 120 znaków
   EN: Stay calm.
   PL:
353. [Kwestia głosowa [battle_enemy_break_10105_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_enemy_break_10105_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Kwestia głosowa [battle_enemy_break_10105_1] (Enemy Stagger)] 기회가 왔군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_enemy_break_10105_1].dlg
   limit: do 120 znaków
   EN: This is an opportunity.
   PL:
355. [Kwestia głosowa [battle_break_10105_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_break_10105_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Kwestia głosowa [battle_break_10105_1] (Staggered)] 큭…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_break_10105_1].dlg
   limit: do 120 znaków
   EN: Ach...
   PL:
357. [Kwestia głosowa [battle_kill_10105_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_kill_10105_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Kwestia głosowa [battle_kill_10105_1] (Enemy Killed)] 어려울 것도 없었소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_kill_10105_1].dlg
   limit: do 120 znaków
   EN: There was naught to worry.
   PL:
359. [Kwestia głosowa [battle_dead_10105_1] — sytuacja] 본인 사망 시
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_dead_10105_1].desc
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Kwestia głosowa [battle_dead_10105_1] (Death)] …역시, 해내지 못하는 것인가.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_dead_10105_1].dlg
   limit: do 120 znaków
   EN: ...I expected as little from myself.
   PL:
361. [Kwestia głosowa [choice_success_p_10105_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=choice_success_p_10105_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Kwestia głosowa [choice_success_p_10105_2] (Check Passed)] 도박수였소만. 잘 되었군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=choice_success_p_10105_2].dlg
   limit: do 120 znaków
   EN: It appears that my gamble bore fruit.
   PL:
363. [Kwestia głosowa [choice_fail_n_10105_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=choice_fail_n_10105_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Kwestia głosowa [choice_fail_n_10105_1] (Check Failed)] …너무 도박수였구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=choice_fail_n_10105_1].dlg
   limit: do 120 znaków
   EN: ... I have miscalculated the risks of this gamble.
   PL:
365. [Kwestia głosowa [battle_clear_10105_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_clear_10105_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Kwestia głosowa [battle_clear_10105_1] (Victory Cry)] …의뢰는 해결했소. 더 복잡한 일이 생기기 전에 서둘러 이곳을 나가지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_clear_10105_1].dlg
   limit: do 120 znaków
   EN: ... The contract is fulfilled. Let us make ourselves scarce before further trouble finds us.
   PL:
367. [Kwestia głosowa [battle_clear_ex_10105_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_clear_ex_10105_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Kwestia głosowa [battle_clear_ex_10105_1] (Extra Conditions Fulfilled)] 침착하게만 해나간다면, 이 정도 의뢰는 완박하게 해결해보일 수 있소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_clear_ex_10105_1].dlg
   limit: do 120 znaków
   EN: Presuming that we remain steady, a contract of such caliber should pose no difficulty to us.
   PL:
369. [Kwestia głosowa [battle_defeat_10105_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_defeat_10105_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Kwestia głosowa [battle_defeat_10105_1] (Defeat Wail)] 실수가 너무 많았나… 도움이 되지 못했군. 미안하오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Molar_10105.json :: dataList[id=battle_defeat_10105_1].dlg
   limit: do 120 znaków
   EN: I've made far too many mistakes... I apologize. I was of no help to you.
   PL:

## [000] W Corp. L3 Cleanup Agent — Yi Sang — W사 3등급 정리 요원
- ID Tożsamości: `10106` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 79 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Charge, Rupture

371. [Karta Tożsamości — tytuł] W사 3등급\n정리 요원
   źródło: Personalities.json :: dataList[id=10106].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L3\nCleanup Agent
   PL:
372. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10106].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10106].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Karta Tożsamości — opis] 이상의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10106].desc
   limit: do 120 znaków
   EN: Yi Sang's 6th Identity
   PL:
375. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 차원 긋기
   źródło: Skills_personality-01.json :: dataList[id=1010601].levelList[level=1].name ; dataList[id=1010601].levelList[level=2].name ; dataList[id=1010601].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Dimensional Slit
   PL:
376. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 충전 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010601].levelList[level=1].desc ; dataList[id=1010601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +2 [Charge] Count
   PL:
377. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010601].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1010601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1010601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count
   PL:
378. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010601].levelList[level=2].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 2 증가\n충전 횟수가 10 이상이면, 코인 위력 +2
   źródło: Skills_personality-01.json :: dataList[id=1010601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +2 [Charge] Count\nAt 10+ [Charge] Count, Coin Power +2
   PL:
380. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010601].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
381. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 에너지 순환
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=1].name ; dataList[id=1010602].levelList[level=2].name ; dataList[id=1010602].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 5 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Energy Cycle
   PL:
382. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 5 증가
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +5 [Charge] Count
   PL:
383. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Binding]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttackHead] Inflict 1 [Binding] next turn
   PL:
384. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1010602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL:
385. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 충전 횟수 6 증가\n충전 횟수가 10 이상이면, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +6 [Charge] Count\nAt 10+ [Charge] Count, Coin Power +1
   PL:
386. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1010602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL:
387. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 충전 횟수가 10 이상이면, 파열 3 부여
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 10+ [Charge] Count, inflict 3 [Burst]
   PL:
388. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 7 증가\n충전 횟수가 10 이상이면, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +7 [Charge] Count\nAt 10+ [Charge] Count, Coin Power +1
   PL:
389. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 충전 횟수가 10 이상이면,  파열 3 부여, 파열 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010602].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 10+ [Charge] Count, inflict 3 [Burst] and +2 [Burst] Count
   PL:
390. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 차원의 틈
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].name ; dataList[id=1010603].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Dimensional Rift
   PL:
391. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 충전 횟수가 15 미만이면, 충전 횟수를 10 소모하여 코인 위력 +1\n[WhenUse] 충전 횟수를 15 소모하여 코인 위력 +2
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At less than 15 [Charge] Count, consume 10 [Charge] Count to gain Coin Power +1\n[WhenUse] Consume 15 [Charge] Count to gain Coin Power +2
   PL:
392. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1010603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1010603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 스킬 사용시 소모한 충전 횟수 5 당 파열 2 부여 (최대 6)
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Inflict 2 [Burst] for every 5 [Charge] Count consumed by the Skill (max 6)
   PL:
395. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 스킬 사용시 충전 횟수를 15 소모하였으면, 차원 균열 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1010603].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] If the Skill consumed 15 [Charge] Count upon use, inflict 2 [DimensionRift]
   PL:
396. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [EnemyKill] 충전 역장 3 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [ChargeForceField]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: [EnemyKill] Gain 3 [ChargeForceField]
   PL:
397. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 충전 횟수가 15 미만이면, 충전 횟수를 10 소모하여 코인 위력 +1\n[WhenUse] 충전 횟수를 15 소모하여 코인 위력 +2\n[BeforeAttack] 충전 횟수를 15 소모했다면, 파열 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BeforeAttack], [Charge], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: [WhenUse] At less than 15 [Charge] Count, consume 10 [Charge] Count to gain Coin Power +1\n[WhenUse] Consume 15 [Charge] Count to gain Coin Power +2\n[BeforeAttack] If 15 [Charge] Count has been consumed, inflict +3 [Burst] Count
   PL:
398. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 스킬 사용시 소모한 충전 횟수 5 당 파열 3 부여 (최대 9)
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Inflict 3 [Burst] for every 5 [Charge] Count consumed by the Skill (max 9)
   PL:
399. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [EnemyKill] 충전 역장 5 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010603].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [ChargeForceField]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: [EnemyKill] Gain 5 [ChargeForceField]
   PL:
400. [Obrona (ulepszenia 1,4) — nazwa] 텅 빈 차원
   źródło: Skills_personality-01.json :: dataList[id=1010604].levelList[level=1].name ; dataList[id=1010604].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Hollow Dimension
   PL:
401. [Obrona (ulepszenie 1) — opis] 충전 횟수 5당 기본 위력 +1 (최대 2)
   źródło: Skills_personality-01.json :: dataList[id=1010604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Base Power +1 for every 5 [Charge] Count (max 2)
   PL:
402. [Obrona (ulepszenie 4) — opis] 충전 횟수 5당 기본 위력 +1 (최대 2)\n[OnSucceedEvade] 다음 턴에 처음으로 스킬로 부여하는 파열 +1 (턴 당 최대 증가량 : 3)
   źródło: Skills_personality-01.json :: dataList[id=1010604].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedEvade], [Charge], [Burst]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: Base Power +1 for every 5 [Charge] Count (max 2)\n[OnSucceedEvade] Next turn, when inflicting [Burst] with a Skill for the first time, inflict +1 more [Burst] (max +3 per turn)
   PL:
403. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — nazwa] 비워낸 생각
   źródło: Passives.json :: dataList[id=1010601].name
   limit: do 40 znaków
   EN: Emptied Thought
   PL:
404. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — opis] - 턴 종료 시 자신의 충전 횟수 5 당 다음 턴에 신속 1을 얻음. (최대 2)\n- 자신이 스킬로 충전 횟수를 소모할 때, 현재 체력 비율이 가장 낮은 아군 1명에게 충전 역장 3 부여
   źródło: Passives.json :: dataList[id=1010601].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [Charge], [ChargeForceField]
   znaczenie tagów: [Agility] = 신속 / Haste; [Charge] = 충전 / Charge; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: - Turn End: Gain 1 [Agility] next turn for every 5 [Charge] Count on self (max 2)\n- If this unit's Skill consumed [Charge] Count, apply 3 [ChargeForceField] on 1 ally that has the lowest current HP percentage
   PL:
405. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 비워낸 생각
   źródło: Passives.json :: dataList[id=1010611].name
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — opis] - 턴 종료 시 자신의 충전 횟수 5 당 다음 턴에 신속 1을 얻음. (최대 3)\n- 자신이 스킬로 충전 횟수를 소모할 때, 현재 체력 비율이 가장 낮은 아군 1명에게 충전 역장 3 부여
   źródło: Passives.json :: dataList[id=1010611].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [Charge], [ChargeForceField]
   znaczenie tagów: [Agility] = 신속 / Haste; [Charge] = 충전 / Charge; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: - Turn End: Gain 1 [Agility] next turn for every 5 [Charge] Count on self (max 3)\n- If this unit's Skill consumed [Charge] Count, apply 3 [ChargeForceField] on 1 ally that has the lowest current HP percentage
   PL:
407. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 정리 시범 교육
   źródło: Passives.json :: dataList[id=1010621].name
   limit: do 40 znaków
   EN: Cleanup Demonstration
   PL:
408. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 충전 횟수가 가장 높은 아군 1명이 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>이 있는 대상에게 가하는 피해량이 대상의 파열 에 비례하여 증가 (파열 1 당 1.5%. 최대 15%)
   źródło: Passives.json :: dataList[id=1010621].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: 1 ally that has the highest [Charge] Count deals more damage against targets that have <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u> based on Rupture on target (+1.5% per Rupture, max +15% damage)
   PL:
409. [Kwestia głosowa [get_10106_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=get_10106_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Kwestia głosowa [get_10106_1] (Identity Acquisition)] 출근 중에는 되도록 건드리지 않았으면 하오만… 무엇이오?
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=get_10106_1].dlg
   limit: do 120 znaków
   EN: I prefer to not be disturbed during my morning commute... What is it?
   PL:
411. [Kwestia głosowa [lobby_morning_10106_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=lobby_morning_10106_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Kwestia głosowa [lobby_morning_10106_1] (Morning Greeting)] 이 시간에 앉아서 갈 수 있다는 것만으로 작지 않은 행운이오. 조금… 잘 수… 있겠군…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=lobby_morning_10106_1].dlg
   limit: do 210 znaków
   EN: It is no small fortune that I was able to procure myself a seat on the way to work at this time of day. Perhaps... today... I may be permitted a small... nap...
   PL:
413. [Kwestia głosowa [lobby_noon_10106_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=lobby_noon_10106_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Kwestia głosowa [lobby_noon_10106_1] (Afternoon Greeting)] 이제 반절 지나갔는가… 하지만, 또 반절이 두 번 지나면 이 곳에서 다시 일하고 있겠지.\n끊어낼 방법조차 보이지 않는 굴레구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=lobby_noon_10106_1].dlg
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This day is now half spent... Yet, after two more halfs of a day I shall return to this exact spot to do selfsame, unchanging work. I see no way of freeing myself from this cyclical yoke.
   PL:
415. [Kwestia głosowa [lobby_night_10106_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=lobby_night_10106_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Kwestia głosowa [lobby_night_10106_1] (Evening Greeting)] 밤이 되면 달도 없는 그믐 칠야에… 새까맣게, 아무런 것들이 보이지가 않소. 나는 이런 시간이 퍽 좋소.\n사람이 침소로 들어가듯… 생각도 어둠 속으로 아주 없어져 버리니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=lobby_night_10106_1].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When a moonless, tenebrous night of the month-end descends, all is obscured with naught manifest before me. I regard such hours with fondness.\nThoughts fade into oblivion... as consciousness is claimed by slumber.
   PL:
417. [Kwestia głosowa [smalltalk_10106_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=smalltalk_10106_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Kwestia głosowa [smalltalk_10106_1] (Chatter #1)] 특별히 무얼 생각하지 않소. 무언가를 생각지 않게 노력한다고 하는 것이 바를 지도 모르겠군.\n이대로 잠에 들면… 조금은 편해질 지도 모르겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=smalltalk_10106_1].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I do not think of anything in particular. Perhaps it would be more accurate to say that I try to not think of anything.\nPerchance I may claim myself a marginally restful night... were I to drift off in this state.
   PL:
419. [Kwestia głosowa [smalltalk_10106_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=smalltalk_10106_2].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Kwestia głosowa [smalltalk_10106_2] (Chatter #2)] 그런 열차에서 일하면서 또 다른 열차에 몸을 싣고 어디론가로 간다는 것은 퍽 우스꽝스럽지.\n그대도 그렇게 생각하지 않는가?
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=smalltalk_10106_2].dlg
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There is ironic humor in taking a train to go clean a different train of such... peculiar nature, wouldn't you agree?
   PL:
421. [Kwestia głosowa [smalltalk_10106_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=smalltalk_10106_3].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Kwestia głosowa [smalltalk_10106_3] (Chatter #3)] 근래에는 새로 입사한 사우들에게 우리 회사를 가르치는 일을 부탁받았소. 제법 즐거웠지, 열차를 정리하는 것보다 더욱.\n어쩌면 나는 누군가를 가르치는데에 재능이 있었을지도 모르오. 혹은 흥미라던가.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=smalltalk_10106_3].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I have been assigned the task of training our new fellow employees as of late. It is quite enjoyable. Much more so than cleaning up the trains.\nPerhaps I've a talent for education. Or an interest, at least.
   PL:
423. [Kwestia głosowa [smalltalk_10106_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=smalltalk_10106_4].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Kwestia głosowa [smalltalk_10106_4] (Post-Uptie Chat 1)] 이러한 일을 할 때 특별히 무얼 생각하지 않소. 아니, 무언가를 생각지 않게…\n아, 언젠가 말했던 적이 있던가. 이해해주게. 무너지기 전에 다잡는 중이니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=smalltalk_10106_4].dlg
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When doing work of this nature, I do not think of anything in particular. Perhaps it would be more accurate to say that—\nAh, so these words have been uttered before. Please do understand. I simply seek to collect myself afore I am broken.
   PL:
425. [Kwestia głosowa [smalltalk_10106_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=smalltalk_10106_5].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Kwestia głosowa [smalltalk_10106_5] (Post-Uptie Chat 2)] 함께 사우를 가르치는 일에 발령받은 사우께선 그 일이 마음에 들지 않은가 보오.\n차라리 나의 일만큼 그 자가 가져가 주면 좋으련만. 물론, 회사가 그리 두지는 않겠지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=smalltalk_10106_5].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: My fellow employee, who was assigned the same task of educating our new recruits, appear averse to doing such work.\nI would rather have her take over my portion of the... other work. Yet, I have scant faith that the company would allow such reassignment.
   PL:
427. [Kwestia głosowa [neglect_10106_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=neglect_10106_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Kwestia głosowa [neglect_10106_1] (Idle)] 하… 언제쯤 끝이 날지…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=neglect_10106_1].dlg
   limit: do 120 znaków
   EN: Haah... When will this cycle be broken?
   PL:
429. [Kwestia głosowa [gacksung_10106_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=gacksung_10106_1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Kwestia głosowa [gacksung_10106_1] (Uptying)] 내가 능력이 있다는거요? …그렇구료. 가르치는 쪽의 능력도 봐주었으면 하네만.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=gacksung_10106_1].dlg
   limit: do 180 znaków
   EN: You insinuate that I am rather capable? ... Very well. ...I would appreciate it if you would take note of my teaching abilities also.
   PL:
431. [Kwestia głosowa [formation_10106_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=formation_10106_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Kwestia głosowa [formation_10106_1] (Deployment)] 출근하겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=formation_10106_1].dlg
   limit: do 120 znaków
   EN: Commuting to work.
   PL:
433. [Kwestia głosowa [battleentry_10106_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battleentry_10106_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Kwestia głosowa [battleentry_10106_1] (Stage Entry)] 정리를 시작하겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battleentry_10106_1].dlg
   limit: do 120 znaków
   EN: Commencing cleanup.
   PL:
435. [Kwestia głosowa [battle_select_10106_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_select_10106_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Kwestia głosowa [battle_select_10106_1] (Viewed in Battle)] 다른 일이 있는가?
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_select_10106_1].dlg
   limit: do 120 znaków
   EN: Is there aught else?
   PL:
437. [Kwestia głosowa [battle_endcommand_10106_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_endcommand_10106_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Kwestia głosowa [battle_endcommand_10106_1] (Commencing Attack)] …….
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_endcommand_10106_1].dlg
   limit: do 120 znaków
   EN: .......
   PL:
439. [Kwestia głosowa [battle_enemy_break_10106_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_enemy_break_10106_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Kwestia głosowa [battle_enemy_break_10106_1] (Enemy Stagger)] 이제…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_enemy_break_10106_1].dlg
   limit: do 120 znaków
   EN: Now...
   PL:
441. [Kwestia głosowa [battle_break_10106_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_break_10106_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Kwestia głosowa [battle_break_10106_1] (Staggered)] 아…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_break_10106_1].dlg
   limit: do 120 znaków
   EN: Ah...
   PL:
443. [Kwestia głosowa [battle_kill_10106_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_kill_10106_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Kwestia głosowa [battle_kill_10106_1] (Enemy Killed)] 쉬시게.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_kill_10106_1].dlg
   limit: do 120 znaków
   EN: You may rest.
   PL:
445. [Kwestia głosowa [battle_dead_10106_1] — sytuacja] 본인 사망 시
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_dead_10106_1].desc
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Kwestia głosowa [battle_dead_10106_1] (Death)] 마침내… 굴레를 벗는… 가?
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_dead_10106_1].dlg
   limit: do 120 znaków
   EN: Am I freed at last... from the yoke?
   PL:
447. [Kwestia głosowa [choice_success_p_10106_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=choice_success_p_10106_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Kwestia głosowa [choice_success_p_10106_2] (Check Passed)] 해결했군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=choice_success_p_10106_2].dlg
   limit: do 120 znaków
   EN: It has been addressed.
   PL:
449. [Kwestia głosowa [choice_fail_n_10106_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=choice_fail_n_10106_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Kwestia głosowa [choice_fail_n_10106_1] (Check Failed)] …이번엔 해결하지 못했소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=choice_fail_n_10106_1].dlg
   limit: do 120 znaków
   EN: ... It could not be addressed.
   PL:
451. [Kwestia głosowa [battle_clear_10106_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_clear_10106_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Kwestia głosowa [battle_clear_10106_1] (Victory Cry)] 정리는 끝났소. 다음 정리까지는 좀 잠들고 싶군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_clear_10106_1].dlg
   limit: do 120 znaków
   EN: This cleanup is complete. Allow me to nap until our next assignment.
   PL:
453. [Kwestia głosowa [battle_clear_ex_10106_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_clear_ex_10106_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Kwestia głosowa [battle_clear_ex_10106_1] (Extra Conditions Fulfilled)] 아무래도 다른 사우들의 몫까지 해결해 버린 모양이구료. 보상은 없는가, 잠시 다른 일을 하는 것이어도 좋으니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_clear_ex_10106_1].dlg
   limit: do 260 znaków
   EN: It appears that I have resolved my fellow employees' share of responsibilities as well. Will there be a reward for this performance? I would appreciate even a reassignment to a different line of work.
   PL:
455. [Kwestia głosowa [battle_defeat_10106_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_defeat_10106_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Kwestia głosowa [battle_defeat_10106_1] (Defeat Wail)] …이 보시오. 나는 이 일이 맞지 않는 것 같소. 나에 대한 평가가 잘못되지는 않았는지, 재고를…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Wcorp_10106.json :: dataList[id=battle_defeat_10106_1].dlg
   limit: do 190 znaków
   EN: ... Please, take heed. I no longer believe that I am appropriate for this line of work. Revisit your assessment of my aptitude, if you will...
   PL:

## [00] The Pequod First Mate — Yi Sang — 피쿼드호 일등 항해사
- ID Tożsamości: `10107` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 3 · HP bazowe: 69 · szybkość: 3–6 / 3–6 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Bleed, Poise

457. [Karta Tożsamości — tytuł] 피쿼드호\n일등 항해사
   źródło: Personalities.json :: dataList[id=10107].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Pequod\nFirst Mate
   PL:
458. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10107].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10107].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Karta Tożsamości — opis] 이상의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10107].desc
   limit: do 120 znaków
   EN: Yi Sang's 7th Identity
   PL:
461. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 후벼파기
   źródło: Skills_personality-01.json :: dataList[id=1010701].levelList[level=1].name ; dataList[id=1010701].levelList[level=2].name ; dataList[id=1010701].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Impale
   PL:
462. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — opis] [WhenUse] 자신의 호흡 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010701].levelList[level=1].desc ; dataList[id=1010701].levelList[level=2].desc ; dataList[id=1010701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL:
463. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 2 [Laceration]
   PL:
464. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010701].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 383 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010701].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1010701].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
466. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 쑤시고 쑤시기
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=1].name ; dataList[id=1010702].levelList[level=2].name ; dataList[id=1010702].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Relentless Stabbing
   PL:
468. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [WhenUse] 자신의 호흡 횟수 2 증가\n자신의 호흡 이 5 이상이면, 합 위력 +2
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=1].desc ; dataList[id=1010702].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count\nAt 5+ [Breath], Clash Power +2
   PL:
469. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 호흡 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1010702].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath]
   PL:
470. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1010702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
471. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 이 코인 재사용 (최대 1회)
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Reuse this Coin (1 time max)
   PL:
472. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 호흡 횟수 2 증가\n자신의 호흡 이 5 이상이면, 합 위력 +3
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count\nAt 5+ [Breath], Clash Power +3
   PL:
473. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
474. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 이 코인 재사용 (최대 3회)
   źródło: Skills_personality-01.json :: dataList[id=1010702].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Reuse this Coin (3 times max)
   PL:
475. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 급습
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=3].name ; dataList[id=1010703].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Ambush
   PL:
476. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 호흡 5 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 5 [Breath]
   PL:
477. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 호흡 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain +2 [Breath] Count
   PL:
478. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 4 부여
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1010703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL:
479. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 출혈 횟수 4 증가
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict +4 [Laceration] Count
   PL:
480. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 호흡 5 얻음\n자신의 호흡 이 7 이상이면, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 5 [Breath]\nAt 7+ [Breath], Coin Power +1
   PL:
481. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL:
482. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 출혈 횟수 6 증가
   źródło: Skills_personality-01.json :: dataList[id=1010703].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict +6 [Laceration] Count
   PL:
483. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills_personality-01.json :: dataList[id=1010704].levelList[level=1].name ; dataList[id=1010704].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 3 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL:
484. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — nazwa] 일등 항해사의 작살
   źródło: Passives.json :: dataList[id=1010701].name
   limit: do 40 znaków
   EN: The First Mate's Harpoon
   PL:
485. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — opis] 크리티컬 적중 시 스킬로 부여하는 출혈 위력 +2 (턴 당 최대 6회)
   źródło: Passives.json :: dataList[id=1010701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: On Crit, this unit inflicts +2 more [Laceration] Potency using its Skills (6 times per turn)
   PL:
486. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — nazwa] 일등 항해사의 노련함
   źródło: Passives.json :: dataList[id=1010721].name
   limit: do 40 znaków
   EN: The First Mate's Acumen
   PL:
487. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — opis] [Breath]을 가장 많이 보유한 아군 1명이 크리티컬 적중 시 스킬로 부여하는 출혈 위력 +2 (턴 당 최대 6회)
   źródło: Passives.json :: dataList[id=1010721].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Breath], [Laceration]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: On Crit, 1 ally that has the highest [Breath] inflicts +2 more [Laceration] Potency using its Skills (6 times per turn)
   PL:
488. [Kwestia głosowa [get_10107_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=get_10107_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Kwestia głosowa [get_10107_1] (Identity Acquisition)] 이상이라 부르게. 피쿼드호의 일등 항해사를 맡고 있지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=get_10107_1].dlg
   limit: do 120 znaków
   EN: You may call me Yi Sang. I am the first mate of the Pequod.
   PL:
490. [Kwestia głosowa [lobby_morning_10107_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=lobby_morning_10107_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Kwestia głosowa [lobby_morning_10107_1] (Morning Greeting)] 밤새 안녕하셨는가. 오늘 호수는 제법 잔잔한 편일세. 바깥의 경치를 좀 즐기는 것은 어떤가 하네만.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=lobby_morning_10107_1].dlg
   limit: do 210 znaków
   EN: I pray that the waves did not keep you up at night. The Lake remains tranquil today... Perhaps we may be availed a brief moment to savor its sights for once.
   PL:
492. [Kwestia głosowa [lobby_noon_10107_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=lobby_noon_10107_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Kwestia głosowa [lobby_noon_10107_1] (Afternoon Greeting)] 흐음… 이 말라 비틀어진 지느러미살을 먹는 것도 좀 지치는구료. 그대는 좀 먹을 만한가?
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=lobby_noon_10107_1].dlg
   limit: do 120 znaków
   EN: Hm... I grow weary of this diet of desiccated fins. How do you fare?
   PL:
494. [Kwestia głosowa [lobby_night_10107_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=lobby_night_10107_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Kwestia głosowa [lobby_night_10107_1] (Evening Greeting)] 야간 항해를 너무 길게 하는 건 좋지 않소. 안전을 따진다면 그건 상식일테요. 그대는 좀 들어가 쉬시게.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=lobby_night_10107_1].dlg
   limit: do 190 znaków
   EN: Do not sail overlong under the night sky. It is common wisdom that such practice invites peril to a journey. Please, do get yourself some rest.
   PL:
496. [Kwestia głosowa [smalltalk_10107_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=smalltalk_10107_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Kwestia głosowa [smalltalk_10107_1] (Chatter #1)] 자, 고래의 이 부분을 공격하는 것이오. 묵직한 한 방을 내기 어렵다면… 한 곳을 빠르게 여러번 쑤셔서 이런 효과를 갖는게지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=smalltalk_10107_1].dlg
   limit: do 260 znaków
   EN: See, this is the part of a Whale that you must assail. If a singular, powerful strike is difficult to execute, apply multiple strikes to a single point. Then you should be able to perform effectively.
   PL:
498. [Kwestia głosowa [smalltalk_10107_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=smalltalk_10107_2].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Kwestia głosowa [smalltalk_10107_2] (Chatter #2)] 갑판! 노닥거리지 말고 위치로 가서 일하게! …아, 그대 듣기는 조금 시끄러웠겠구료. 내 사과하지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=smalltalk_10107_2].dlg
   limit: do 170 znaków
   EN: Deckhands! Cease your loitering and return to your stations! ... Ah, apologies. That may have been quite loud for you. I apologize.
   PL:
500. [Kwestia głosowa [smalltalk_10107_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=smalltalk_10107_3].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Kwestia głosowa [smalltalk_10107_3] (Chatter #3)] 항해사 일은… 뭐, 나쁘지는 않네만. 그래도 나는, 이 항해를 끝내면 카페를 하나 내고 싶소. 급박한 일보다는 이제는 느긋한 일을 꿈꾸게 되어가는군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=smalltalk_10107_3].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The life of a sailor is... Quite all right. Once this endeavor is complete, however, I wish to start a café of my own.\nI have begun dreaming of a leisurely life, free from urgency.
   PL:
502. [Kwestia głosowa [smalltalk_10107_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=smalltalk_10107_4].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Kwestia głosowa [smalltalk_10107_4] (Post-Uptie Chat 1)] 밧줄을 놓치지 마시오! 작살을 든 손을 미끄러트리면 죽소! 현명하게… 대담하게 임하시오!
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=smalltalk_10107_4].dlg
   limit: do 130 znaków
   EN: Do not let go of the rope! To release the rope is to release your hold on life! Be wise... yet bold!
   PL:
504. [Kwestia głosowa [smalltalk_10107_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=smalltalk_10107_5].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Kwestia głosowa [smalltalk_10107_5] (Post-Uptie Chat 2)] 이스마엘 선장께서는 그대들의 죽음을 명하지 않았소! 우리 모두… 저것을 잡아내고 각자가 있을 곳으로 돌아가야 하오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=smalltalk_10107_5].dlg
   limit: do 150 znaków
   EN: Captain Ishmael has not ordered you to your deaths! We must... All of us must kill it and return to where we belong!
   PL:
506. [Kwestia głosowa [neglect_10107_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=neglect_10107_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Kwestia głosowa [neglect_10107_1] (Idle)] 흠… 물을 가르는 소리만 남은 것도 제법 운치가 있구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=neglect_10107_1].dlg
   limit: do 140 znaków
   EN: Hm... All is silent, save for the sound of the vessel hewing across the waters. This is also quite pleasant.
   PL:
508. [Kwestia głosowa [gacksung_10107_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=gacksung_10107_1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Kwestia głosowa [gacksung_10107_1] (Uptying)] 기어이 나까지 나서야 하는 것인가…! 좋소, 내 작살을 들도록 하지!
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=gacksung_10107_1].dlg
   limit: do 120 znaków
   EN: Thus I must step up to the occasion, then...! Very well. Wield the harpoon I shall!
   PL:
510. [Kwestia głosowa [formation_10107_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=formation_10107_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Kwestia głosowa [formation_10107_1] (Deployment)] 키만 잡고 있을 때가 아니구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=formation_10107_1].dlg
   limit: do 120 znaków
   EN: It appears that I must let go of the helm and join the fray.
   PL:
512. [Kwestia głosowa [battleentry_10107_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battleentry_10107_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Kwestia głosowa [battleentry_10107_1] (Stage Entry)] 작살, 놓치지 말게.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battleentry_10107_1].dlg
   limit: do 120 znaków
   EN: Do not let go of the harpoon.
   PL:
514. [Kwestia głosowa [battle_select_10107_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_select_10107_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Kwestia głosowa [battle_select_10107_1] (Viewed in Battle)] 선장이 위험한가?
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_select_10107_1].dlg
   limit: do 120 znaków
   EN: Is the Captain in danger?
   PL:
516. [Kwestia głosowa [battle_endcommand_10107_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_endcommand_10107_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Kwestia głosowa [battle_endcommand_10107_1] (Commencing Attack)] 내가 시범을 보이지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_endcommand_10107_1].dlg
   limit: do 120 znaków
   EN: Please, allow me to demonstrate.
   PL:
518. [Kwestia głosowa [battle_enemy_break_10107_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_enemy_break_10107_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Kwestia głosowa [battle_enemy_break_10107_1] (Enemy Stagger)] 흠! 제법 지쳤나보오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_enemy_break_10107_1].dlg
   limit: do 120 znaków
   EN: Hm! They appear to be quite spent.
   PL:
520. [Kwestia głosowa [battle_break_10107_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_break_10107_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Kwestia głosowa [battle_break_10107_1] (Staggered)] 하앗…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_break_10107_1].dlg
   limit: do 120 znaków
   EN: Haah...
   PL:
522. [Kwestia głosowa [battle_kill_10107_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_kill_10107_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Kwestia głosowa [battle_kill_10107_1] (Enemy Killed)] 쳇, 기름도 나오지 않는 놈이구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_kill_10107_1].dlg
   limit: do 120 znaków
   EN: Tsk. There is no oil to be gleaned from this fellow.
   PL:
524. [Kwestia głosowa [battle_dead_10107_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_dead_10107_1].desc
   limit: do 120 znaków
   EN: Death
   PL:
525. [Kwestia głosowa [battle_dead_10107_1] (Death)] 하하… 내 항해가… 여기서… 끝나는 건가…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_dead_10107_1].dlg
   limit: do 120 znaków
   EN: Ha ha ha... Thus does my... voyage... end...
   PL:
526. [Kwestia głosowa [choice_success_p_10107_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=choice_success_p_10107_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Kwestia głosowa [choice_success_p_10107_2] (Check Passed)] 이 정도 일은 우습소. 삼등 항해사도 능히 해내겠군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=choice_success_p_10107_2].dlg
   limit: do 130 znaków
   EN: This was a trivial endeavor. Even a third mate should have little trouble accomplishing this task.
   PL:
528. [Kwestia głosowa [choice_fail_n_10107_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=choice_fail_n_10107_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Kwestia głosowa [choice_fail_n_10107_1] (Check Failed)] 으흠… 내 평생 배에만 있어서. 크흠.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=choice_fail_n_10107_1].dlg
   limit: do 120 znaków
   EN: Ahem... I have very seldom set my foot outside the ship... Do understand.
   PL:
530. [Kwestia głosowa [battle_clear_10107_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_clear_10107_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Kwestia głosowa [battle_clear_10107_1] (Victory Cry)] 자, 이제 항해의 끝이 얼마 남지 않았네. 좀 더 나아가보세!
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_clear_10107_1].dlg
   limit: do 120 znaków
   EN: The end of this voyage rises upon the horizon. Let us persevere but for a little longer!
   PL:
532. [Kwestia głosowa [battle_clear_ex_10107_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_clear_ex_10107_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Kwestia głosowa [battle_clear_ex_10107_1] (Extra Conditions Fulfilled)] 해냈소! 이제 이 배를 쉽게 넘볼 해적도 고래도 몇 없을테지. 흐흠, 흡족하군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_clear_ex_10107_1].dlg
   limit: do 170 znaków
   EN: We have done it! Not many pirates or Whales shall dare attack this vessel again. Hm hm, this was quite the satisfactory outcome.
   PL:
534. [Kwestia głosowa [battle_defeat_10107_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_defeat_10107_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Kwestia głosowa [battle_defeat_10107_1] (Defeat Wail)] …선체에 파손된 부위가 너무 많소… 정박하고, 수리하세. …그리고 다시 호수로 떠나면 될 것이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Starb_10107.json :: dataList[id=battle_defeat_10107_1].dlg
   limit: do 170 znaków
   EN: ... Our vessel is far too damaged to continue... Let us anchor and repair. ... Then we shall set sail to the Lake once again.
   PL:

## [00] Dieci Assoc. South Section 4 — Yi Sang — 남부 디에치 협회 4과
- ID Tożsamości: `10108` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Sinking

536. [Karta Tożsamości — tytuł] 남부 디에치 협회\n4과
   źródło: Personalities.json :: dataList[id=10108].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Dieci Assoc.\nSouth Section 4
   PL:
537. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10108].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10108].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Karta Tożsamości — opis] 이상의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10108].desc
   limit: do 120 znaków
   EN: Yi Sang's 8th Identity
   PL:
540. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 지식 소모
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=1].name ; dataList[id=1010801].levelList[level=2].name ; dataList[id=1010801].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Expend Knowledge
   PL:
541. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 2%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]
   EN: Gain ([KnowledgeExplored] x 2% of max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots
   PL:
542. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [KnowledgeExplored]만큼 흐트러짐 회복
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [KnowledgeExplored]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [OnSucceedAttackHead] Lower user’s Stagger Threshold by [KnowledgeExplored]
   PL:
543. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [KnowledgeExplored]만큼 흐트러짐 회복
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 3%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]
   EN: Gain ([KnowledgeExplored] x 3% of max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots
   PL:
545. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [KnowledgeExplored]만큼 흐트러짐 회복
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1010801].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [KnowledgeExplored]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by [KnowledgeExplored]
   PL:
546. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [KnowledgeExplored]만큼 흐트러짐 회복
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 3%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림\n[WhenUse] 대상의 [Sinking]이 5 이상이면 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010801].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Sinking]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: Gain ([KnowledgeExplored] x 3% of max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots\n[WhenUse] If target has 5+ [Sinking], Coin Power +1
   PL:
548. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 잠궈닫기
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=1].name ; dataList[id=1010802].levelList[level=2].name ; dataList[id=1010802].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Seal Shut
   PL:
549. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 4%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]
   EN: Gain ([KnowledgeExplored] x 4% of max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots
   PL:
550. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [KnowledgeExplored]만큼 [Sinking] 부여
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1010802].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict [Sinking] equal to [KnowledgeExplored]
   PL:
551. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] [KnowledgeExplored]만큼 [Sinking] 부여
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1010802].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 5%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림\n[WhenUse] 다음 턴에 이 슬롯이 도발치 3 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Aggro]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: Gain ([KnowledgeExplored] x 5% of max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots\n[WhenUse] Gain +3 [Aggro] to this Skill Slot next turn
   PL:
553. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 6%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림\n[WhenUse] 대상의 [Sinking]이 5 이상이면 코인 위력 +1\n[WhenUse] 다음 턴에 이 슬롯이 도발치 3 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=4].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Sinking], [Aggro]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Aggro] = 도발치 / Aggro
   EN: Gain ([KnowledgeExplored] x 6% of max HP) Shield if this Skill is Discarded\n[WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots\n[WhenUse] If target has 5+ [Sinking], Coin Power +1\n[WhenUse] Gain +3 [Aggro] to this Skill Slot next turn
   PL:
554. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [KnowledgeExplored]만큼 [Sinking] 부여
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict [Sinking] equal to [KnowledgeExplored]
   PL:
555. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [KnowledgeExplored]만큼 [Sinking] 부여
   źródło: Skills_personality-01.json :: dataList[id=1010802].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 554 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 지식의 가호
   źródło: Skills_personality-01.json :: dataList[id=1010803].levelList[level=3].name ; dataList[id=1010803].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Grace of Knowledge
   PL:
557. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 9%)만큼 보호막을 얻음\n[WhenUse] 다음 턴에 이 슬롯이 도발치 8 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010803].levelList[level=3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Aggro]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: Gain ([KnowledgeExplored] x 9% of max HP) Shield if this Skill is Discarded\n[WhenUse] Gain +8 [Aggro] to this Skill Slot next turn
   PL:
558. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010803].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL:
559. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] × 최대 체력의 12%)만큼 보호막을 얻음\n[WhenUse] 다음 턴에 이 슬롯이 도발치 10 얻음\n[WhenUse] 자신의 체력이 50% 미만이면 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010803].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Aggro]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: Gain ([KnowledgeExplored] x 12% of max HP) Shield if this Skill is Discarded\n[WhenUse] Gain +10 [Aggro] to this Skill Slot next turn\n[WhenUse] At less than 50% HP, Coin Power +1
   PL:
560. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1010803].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
561. [Obrona (ulepszenia 1,4) — nazwa] 탐구 몰입
   źródło: Skills_personality-01.json :: dataList[id=1010804].levelList[level=1].name ; dataList[id=1010804].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Fixated Study
   PL:
562. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 무작위 스킬 2개를 등급이 낮은 순으로 버림\n[WhenUse] 다음 턴에 이 슬롯이 도발치 3 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010804].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Randomly Discard 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots\n[WhenUse] Gain +3 [Aggro] to this Skill Slot next turn
   PL:
563. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 무작위 스킬 2개를 등급이 낮은 순으로 버림\n[WhenUse] 다음 턴에 이 슬롯이 도발치 5 얻음
   źródło: Skills_personality-01.json :: dataList[id=1010804].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Randomly Discard 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots\n[WhenUse] Gain +5 [Aggro] to this Skill Slot next turn
   PL:
564. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — nazwa] 가라앉는 지식
   źródło: Passives.json :: dataList[id=1010801].name
   limit: do 40 znaków
   EN: Sinking Knowledge
   PL:
565. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — opis] 피격 시 공격자에게 침잠 1 부여 (최대 4회)
   źródło: Passives.json :: dataList[id=1010801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When hit, inflict 1 [Sinking] on the attacker (max 4 times)
   PL:
566. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Sloth) — nazwa] 가라앉는 지식
   źródło: Passives.json :: dataList[id=1010811].name
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Sloth) — opis] 피격 시 공격자에게 침잠 1 부여. 보호막이 있는 동안 피격 시 침잠 1 추가 부여 (최대 4회)
   źródło: Passives.json :: dataList[id=1010811].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When hit, inflict 1 [Sinking] on the attacker. When hit while Shielded, inflict 1 additional [Sinking] on the attacker (max 4 times)
   PL:
568. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Sloth) — nazwa] 반복 지식
   źródło: Passives.json :: dataList[id=1010821].name
   limit: do 40 znaków
   EN: Reviewed Knowledge
   PL:
569. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Sloth) — opis] 속도가 가장 빠른 아군 1명이 스킬을 버릴 때, 해당 캐릭터 최대 체력의 (3 x 버린 스킬의 등급) % 만큼 보호막을 얻음 (턴 당 최대 1회)
   źródło: Passives.json :: dataList[id=1010821].desc
   limit: do 170 znaków
   EN: When 1 ally with the fastest Speed Discards a Skill, gain (3 x Discarded Skill rank)% of the max HP as Shield (once per turn)
   PL:
570. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Sloth) — nazwa] 반복 지식
   źródło: Passives.json :: dataList[id=1010831].name
   (powtórzenie elementu 568 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Sloth) — opis] 속도가 가장 빠른 아군 1명이 스킬을 버릴 때, 해당 캐릭터 최대 체력의 (5 x 버린 스킬의 등급) % 만큼 보호막을 얻음 (턴 당 최대 2회)
   źródło: Passives.json :: dataList[id=1010831].desc
   limit: do 170 znaków
   EN: When 1 ally with the fastest Speed Discards a Skill, gain (5 x Discarded Skill rank)% of the max HP as Shield (2 times per turn)
   PL:
572. [Kwestia głosowa [get_10108_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=get_10108_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Kwestia głosowa [get_10108_1] (Identity Acquisition)] 이상이오. 조금 조용히 하도록 하지, 이곳은 지식의 성전이니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=get_10108_1].dlg
   limit: do 120 znaków
   EN: I am Yi Sang. Please remain silent, as you find yourself at the temple of knowledge.
   PL:
574. [Kwestia głosowa [lobby_morning_10108_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=lobby_morning_10108_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Kwestia głosowa [lobby_morning_10108_1] (Morning Greeting)] 아, 해가 떴는가. 으으음… 그 말을 들으니 피로가 조금 몰려오는 것 같군. 그만 쉬어야겠어…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=lobby_morning_10108_1].dlg
   limit: do 130 znaków
   EN: Ah, so the sun has risen... Mmhm. I feel a scintilla of fatigue setting in. I must rest a little...
   PL:
576. [Kwestia głosowa [lobby_noon_10108_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=lobby_noon_10108_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Kwestia głosowa [lobby_noon_10108_1] (Afternoon Greeting)] 식사…? 아, 이곳 안에서는 식사가 금지되어 있소. 배가 고프다면, 저기 보이는 출구로 나가 오른쪽으로 꺾어보게. 거기 식당이 있을 것이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=lobby_noon_10108_1].dlg
   limit: do 240 znaków
   EN: You seek sustenance...? Consuming a meal within these premises is prohibited. If you find yourself growing peckish, turn right at that exit over yonder. There, you shall find a cafeteria.
   PL:
578. [Kwestia głosowa [lobby_night_10108_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=lobby_night_10108_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Kwestia głosowa [lobby_night_10108_1] (Evening Greeting)] 음, 오면서 보았소. 해가 떨어졌더군. 야음 속에서 읽는 활자가 훨씬 더 눈에 들어오는 법. 이제 차분히 책을 읽을까 하오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=lobby_night_10108_1].dlg
   limit: do 250 znaków
   EN: Mm. Indeed, I noticed on my stroll here that the sun had sunk beyond the horizon. Yet, it is said that erudition comes more naturally under the pale moonlight. I suppose I shall read now, then.
   PL:
580. [Kwestia głosowa [smalltalk_10108_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=smalltalk_10108_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Kwestia głosowa [smalltalk_10108_1] (Chatter #1)] 지식은 쌓아둘 수 있을 때 최대한 쌓아두어야만 하오. 언제 어디서 휘발될 지 모르기에.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=smalltalk_10108_1].dlg
   limit: do 190 znaków
   EN: Knowledge must always be amassed to the full capacity. Occasions in which they may have to be burned for strength... arise with nary a forewarning.
   PL:
582. [Kwestia głosowa [smalltalk_10108_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=smalltalk_10108_2].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Kwestia głosowa [smalltalk_10108_2] (Chatter #2)] 이곳에는 만세의 지식이 수납되어 있소. 새로운 것을 깊게 파고들기에 이곳보다 뛰어난 곳이 있겠는가. 과장을 조금 보태, 이 공간에만 무한히 있고 싶구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=smalltalk_10108_2].dlg
   limit: do 280 znaków
   EN: A decem millennium of knowledge is stored here. What better place to delve deep into an unfamiliar subject? If you would allow me to speak in hyperbole... I would like nothing more than to spend an eternity in here.
   PL:
584. [Kwestia głosowa [smalltalk_10108_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=smalltalk_10108_3].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Kwestia głosowa [smalltalk_10108_3] (Chatter #3)] 이곳은 갈 곳 없는 이를 돌봐주는 일도 하고 있지. 그렇게 또 한 명, 지식을 음미하고 쌓는 자가 생기면 모두에게 기쁜 일이 아니겠는가.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=smalltalk_10108_3].dlg
   limit: do 270 znaków
   EN: This Association also takes in those without places to go. One by one, the number of knowledge-seekers grows. Is it not a boon to all, to have more of those who simply enjoy the act of learning and understanding?
   PL:
586. [Kwestia głosowa [smalltalk_10108_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=smalltalk_10108_4].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Kwestia głosowa [smalltalk_10108_4] (Post-Uptie Chat 1)] 본인과 주먹파가 어울리지 않는다라… 흠, 글쎄. 지식은 직접 나의 손으로 써내려가며 얻는 것. 그 손을 써 상대를 제압함에 무슨 차이가 있는지 모르겠구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=smalltalk_10108_4].dlg
   limit: do 330 znaków
   EN: I seem out of place as a member of the Fists, you say? Hm, one may wonder. Yet I maintain that there is a direct correlation—to learn is to write with my hands. To neutralize my enemies is to smite them with my hands. The distinction is paper-thin, indeed.
   PL:
588. [Kwestia głosowa [smalltalk_10108_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=smalltalk_10108_5].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Kwestia głosowa [smalltalk_10108_5] (Post-Uptie Chat 2)] 지식이 조금씩 닳아도 상관 없네. 알고 있는가? 복습은 앎을 쌓는 과정에 있어 가장 즐거운 일이라는 걸.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=smalltalk_10108_5].dlg
   limit: do 200 znaków
   EN: To use my powers is to burn my amassed knowledge... yet I care not. Are you aware that reviewing is the most engrossing part of the learning process?
   PL:
590. [Kwestia głosowa [neglect_10108_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=neglect_10108_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Kwestia głosowa [neglect_10108_1] (Idle)] 흠…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=neglect_10108_1].dlg
   limit: do 120 znaków
   EN: Hmm...
   PL:
592. [Kwestia głosowa [gacksung_10108_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=gacksung_10108_1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Kwestia głosowa [gacksung_10108_1] (Uptying)] 그런가. 공부를 더욱 게을리 하지 말아야 하겠군. 정진하겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=gacksung_10108_1].dlg
   limit: do 120 znaków
   EN: Is that so... Then I must not grow complacent with my studies. I shall persevere.
   PL:
594. [Kwestia głosowa [formation_10108_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=formation_10108_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Kwestia głosowa [formation_10108_1] (Deployment)] 출발하지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=formation_10108_1].dlg
   limit: do 120 znaków
   EN: Let us take our leave.
   PL:
596. [Kwestia głosowa [battleentry_10108_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battleentry_10108_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Kwestia głosowa [battleentry_10108_1] (Stage Entry)] 앎을 깨치기 위함이라.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battleentry_10108_1].dlg
   limit: do 120 znaków
   EN: To reach the understanding of knowledge.
   PL:
598. [Kwestia głosowa [battle_select_10108_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_select_10108_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Kwestia głosowa [battle_select_10108_1] (Viewed in Battle)] 궁금한 것이라도 있는가.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_select_10108_1].dlg
   limit: do 120 znaków
   EN: Is there aught you would like to ask?
   PL:
600. [Kwestia głosowa [battle_endcommand_10108_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_endcommand_10108_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Kwestia głosowa [battle_endcommand_10108_1] (Commencing Attack)] 앎은 고통스러운 법!
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_endcommand_10108_1].dlg
   limit: do 120 znaków
   EN: Pain paves the road to understanding!
   PL:
602. [Kwestia głosowa [battle_enemy_break_10108_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_enemy_break_10108_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Kwestia głosowa [battle_enemy_break_10108_1] (Enemy Stagger)] 깨달음은 괴롭지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_enemy_break_10108_1].dlg
   limit: do 120 znaków
   EN: The path to enlightenment is an excruciating one.
   PL:
604. [Kwestia głosowa [battle_break_10108_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_break_10108_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Kwestia głosowa [battle_break_10108_1] (Staggered)] 크흠…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_break_10108_1].dlg
   limit: do 120 znaków
   EN: Ahm...
   PL:
606. [Kwestia głosowa [battle_kill_10108_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_kill_10108_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Kwestia głosowa [battle_kill_10108_1] (Enemy Killed)] 이제 끝내지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_kill_10108_1].dlg
   limit: do 120 znaków
   EN: Let us finish this.
   PL:
608. [Kwestia głosowa [battle_dead_10108_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_dead_10108_1].desc
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Kwestia głosowa [battle_dead_10108_1] (Death)] 아… 죽음을 피할 지식은… 잊었던 건가…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_dead_10108_1].dlg
   limit: do 120 znaków
   EN: I must have forgotten... the knowledge that would have been my salvation from death...
   PL:
610. [Kwestia głosowa [choice_success_p_10108_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=choice_success_p_10108_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Kwestia głosowa [choice_success_p_10108_2] (Check Passed)] 책에 적힌 대로구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=choice_success_p_10108_2].dlg
   limit: do 120 znaków
   EN: As I have read in my books.
   PL:
612. [Kwestia głosowa [choice_fail_n_10108_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=choice_fail_n_10108_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Kwestia głosowa [choice_fail_n_10108_1] (Check Failed)] 음… 복습이 필요하겠군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=choice_fail_n_10108_1].dlg
   limit: do 120 znaków
   EN: Hm... I must review my materials.
   PL:
614. [Kwestia głosowa [battle_clear_10108_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_clear_10108_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Kwestia głosowa [battle_clear_10108_1] (Victory Cry)] 우리의 승리였소. 하지만 이것 저것… 머릿 속에 빈 낱말들이 신경 쓰이는구료. 가서 복습이라도 해야 하겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_clear_10108_1].dlg
   limit: do 150 znaków
   EN: We were victorious. Yet... these new gaps in my knowledge are rather vexing. I must return and review my materials.
   PL:
616. [Kwestia głosowa [battle_clear_ex_10108_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_clear_ex_10108_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Kwestia głosowa [battle_clear_ex_10108_1] (Extra Conditions Fulfilled)] 손이 열쇠보다 강하다. 그것을 분명하게 깨우치게 했소. 그리고… 흠, 무슨 말을 더 붙이려 했었던지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_clear_ex_10108_1].dlg
   limit: do 210 znaków
   EN: The hand is mightier than the key. I am certain that I have smote that understanding into them. And... Hm. I do not recall what I had planned to say hereafter.
   PL:
618. [Kwestia głosowa [battle_defeat_10108_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_defeat_10108_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Kwestia głosowa [battle_defeat_10108_1] (Defeat Wail)] 실망을 했겠소. 아무래도 나의 공부가 부족한 것만 같소. 더욱 면학에 힘을 써야만…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Dieci_10108.json :: dataList[id=battle_defeat_10108_1].dlg
   limit: do 140 znaków
   EN: You must be disappointed. It appears that my studies were not enough... I must delve deeper in my erudition.
   PL:

## [000] The Ring Pointillist Student — Yi Sang — 약지 점묘파 스튜던트
- ID Tożsamości: `10109` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 70 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed

620. [Karta Tożsamości — tytuł] 약지 점묘파\n스튜던트
   źródło: Personalities.json :: dataList[id=10109].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Ring Pointillist\nStudent
   PL:
621. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10109].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10109].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Karta Tożsamości — opis] 이상의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10109].desc
   limit: do 120 znaków
   EN: Yi Sang's 9th Identity
   PL:
624. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 덧칠
   źródło: Skills_personality-01.json :: dataList[id=1010901].levelList[level=1].name ; dataList[id=1010901].levelList[level=2].name ; dataList[id=1010901].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 2 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Paint Over
   PL:
625. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과의 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010901].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1010901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1010901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +2 Count of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL:
626. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010901].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 2 [Laceration]
   PL:
627. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010901].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1010901].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
628. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Laceration]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010901].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration], Clash Power +1
   PL:
629. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 혈점묘화
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=1].name ; dataList[id=1010902].levelList[level=2].name ; dataList[id=1010902].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 8 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Sanguine Pointillism
   PL:
630. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 20% 확률로 코인 1회 재사용. 대상이 보유한 부정적인 효과 1개당 재사용 확률 +20%
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1010902].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] 20% chance to Reuse Coin once. +20% more chance to Reuse Coin for every type of negative effect on target
   PL:
631. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1010902].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1010902].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
632. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과의 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 Count of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL:
633. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Laceration]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=2].desc
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과의 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=2].coinlist[#0].coindescs[#2].desc ; dataList[id=1010902].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 Count of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL:
635. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Laceration] 3 당 합 위력 +1 (최대 2)\n대상의 [Laceration] 횟수 3 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Clash Power +1 for every 3 [Laceration] on target (max 2)\nCoin Power +1 for every 3 [Laceration] Count on target (max 2)
   PL:
636. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 40% 확률로 코인 재사용. 대상이 보유한 부정적인 효과 1개당 재사용 확률 +20%. (스킬당 최대 2회 재사용 가능)
   źródło: Skills_personality-01.json :: dataList[id=1010902].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] 40% chance to Reuse Coin. +20% more chance to Reuse Coin for every type of negative effect on target (2 times max per Skill)
   PL:
637. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 핏방울 채색
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].name ; dataList[id=1010903].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 3 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Hematic Coloring
   PL:
638. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Laceration]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].desc
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가. 대상이 보유한 부정적인 효과가 4개 이상이면, 추가 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count. If target has 4+ types of negative effects, inflict +2 additional [Laceration] Count
   PL:
640. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과의 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1010903].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 634 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여. 대상이 보유한 부정적인 효과가 4개 이상이면, 추가 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]. If target has 4+ types of negative effects, inflict 2 additional [Laceration]
   PL:
642. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과의 위력 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1010903].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 Potency of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL:
643. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] 대상이 보유한 부정적인 효과 1개당 피해량 +15% (최대 75%)
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +15% damage for every type of negative effect on target (max 75%)
   PL:
644. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 2 — opis] [EndSkill] 대상이 흐트러졌거나 사망했으면, 부정적인 효과를 가장 적게 보유한 적 1명에게 [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [EndSkill] If target is Staggered or Defeated, inflict 2 Potency of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking], on 1 enemy that has the fewest types of negative effects
   PL:
645. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Laceration] 3 당 합 위력 +1 (최대 2)\n대상의 [Laceration] 횟수 3 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=4].desc
   (powtórzenie elementu 635 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가. 대상이 보유한 부정적인 효과가 3개 이상이면, 추가 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count. If target has 3+ types of negative effects, inflict +2 additional [Laceration] Count
   PL:
647. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여. 대상이 보유한 부정적인 효과가 3개 이상이면, 추가 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]. If target has 3+ types of negative effects, inflict 2 additional [Laceration]
   PL:
648. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] 대상이 보유한 부정적인 효과 1개당 피해량 +25% (최대 125%)
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +25% damage for every type of negative effect on target (max 125%)
   PL:
649. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] [EndSkill] 대상이 흐트러졌거나 사망했으면, 부정적인 효과를 가장 적게 보유한 적 2명에게 [Combustion], [Laceration], [Vibration], [Burst], [Sinking] 중 무작위 1개 효과 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1010903].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: [EndSkill] If target is Staggered or Defeated, inflict 2 Potency of a random status, chosen from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking], on 2 enemies that have the fewest types of negative effects
   PL:
650. [Obrona (ulepszenia 1,4) — nazwa] 붓 털기
   źródło: Skills_personality-01.json :: dataList[id=1010904].levelList[level=1].name ; dataList[id=1010904].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Beat the Brush
   PL:
651. [Obrona (ulepszenie 1) — opis] 대상의 [Laceration]이 6 이상이면, 기본 위력 +5
   źródło: Skills_personality-01.json :: dataList[id=1010904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration], Base Power +5
   PL:
652. [Obrona (ulepszenie 4) — opis] 대상의 [Laceration] 1당 기본 위력 +1 (최대 10)
   źródło: Skills_personality-01.json :: dataList[id=1010904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Base Power +1 for every 1 [Laceration] on target (max 10)
   PL:
653. [Pasywka bojowa (od ulepszenia 1) — nazwa] 혈점묘파
   źródło: Passives.json :: dataList[id=1010902].name
   limit: do 40 znaków
   EN: Sanguine Pointillist
   PL:
654. [Pasywka bojowa (od ulepszenia 1) — opis] 이 인격은 [Laceration]을 부여하는 인격으로만 취급됨. 랜덤으로 [Combustion], [Laceration], [Vibration], [Burst], [Sinking]을 부여하는 스킬이 이 효과로 인해서 해당 키워드를 부여하는 스킬로 취급되지 않음.
   źródło: Passives.json :: dataList[id=1010902].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: [Laceration], [Combustion], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: This Identity only counts as an "Identity that inflicts [Laceration]". This Identity's Skills that randomly inflict [Combustion], [Laceration], [Vibration], [Burst], and [Sinking] do not count as Skills that inflict each respective Keyword
   PL:
655. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — nazwa] 과제평가
   źródło: Passives.json :: dataList[id=1010901].name
   limit: do 40 znaków
   EN: Assignment Evaluation
   PL:
656. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — opis] 적중시 대상에게 [Laceration]이 6 이상 있으면 정신력 2 회복.\n대상이 보유한 부정적인 효과 1개당 정신력 1 추가 회복.(최대 3)\n이 효과로 정신력 회복 시 자신의 정신력이 최대면, 다음 턴에 [AttackUp] 1 얻음.\n(턴 당 패시브 최대 발동 횟수 : 4회)
   źródło: Passives.json :: dataList[id=1010901].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [AttackUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: On Hit, if the target has 6+ [Laceration], heal 2 SP\nHeal 1 additional SP for every type of negative effect on the target (max 3)\nIf this unit's SP is at max, gain 1 [AttackUp] next turn when this unit heals SP with this effect\n(This Passive activates 4 times max per turn)
   PL:
657. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — podsumowanie] 적중시 조건에 따라 정신력 회복. 정신력이 최대면, 다음 턴에 [AttackUp] 1 얻음
   źródło: Passives.json :: dataList[id=1010901].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Conditional SP Heal On Hit. At max SP, gain 1 [AttackUp] next turn
   PL:
658. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — nazwa] 과제평가
   źródło: Passives.json :: dataList[id=1010911].name
   (powtórzenie elementu 655 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — opis] 적중시 대상에게 [Laceration]이 <style="highlight">4</style> 이상 있으면 정신력 2 회복.\n대상이 보유한 부정적인 효과 1개당 정신력 1 추가 회복.(최대 3)\n이 효과로 정신력 회복 시 자신의 정신력이 최대면, 다음 턴에 [AttackUp] <style="highlight">2</style> 얻음.\n(턴 당 패시브 최대 발동 횟수 : 4회)
   źródło: Passives.json :: dataList[id=1010911].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [AttackUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: On Hit, if target has <style="highlight">4</style>+ [Laceration], heal 2 SP\nHeal 1 additional SP for every type of negative effect on the target (max 3)\nIf this unit's SP is at max, gain <style="highlight">2</style> [AttackUp] next turn when this unit heals SP with this effect\n(This Passive activates 4 times max per turn)
   PL:
660. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — podsumowanie] 적중시 조건에 따라 정신력 회복. 정신력이 최대면, 다음 턴에 [AttackUp] 2 얻음
   źródło: Passives.json :: dataList[id=1010911].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Conditional SP Heal On Hit. At max SP, gain 2 [AttackUp] next turn
   PL:
661. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 미학견습
   źródło: Passives.json :: dataList[id=1010921].name
   limit: do 40 znaków
   EN: Practices on Aesthetics
   PL:
662. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 정신력이 가장 낮은 아군이 공격 적중 시 대상이 보유한 부정적인 효과 1개당 정신력 2 회복.(최대 6)\n(턴 당 패시브 최대 발동 횟수 : 2회)
   źródło: Passives.json :: dataList[id=1010921].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 1 ally that has the lowest SP heals 2 SP On Hit for every type of negative effect on the target (max 6)\n(This Passive activates 2 times max per turn)
   PL:
663. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — podsumowanie] 적중시 대상이 보유한 부정적인 효과 수에 비례하여 정신력 회복
   źródło: Passives.json :: dataList[id=1010921].summary
   limit: do 120 znaków
   EN: On Hit, heal SP based on the number of negative effect types on the target
   PL:
664. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Lust) — nazwa] 미학견습
   źródło: Passives.json :: dataList[id=1010931].name
   (powtórzenie elementu 661 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Lust) — opis] 정신력이 가장 낮은 아군이 공격 적중 시 대상이 보유한 부정적인 효과 1개당 정신력 2 회복.(최대 6)\n<style="highlight">대상에게 [Laceration]이 있으면 추가 3 회복.</style>\n(턴 당 패시브 최대 발동 횟수 : 2회)
   źródło: Passives.json :: dataList[id=1010931].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: 1 ally that has the lowest SP heals 2 SP On Hit for every type of negative effect on the target (max 6)\n<style="highlight">If the target has [Laceration], heal 3 additional SP</style>\n(This Passive activates 2 times max per turn)
   PL:
666. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Lust) — podsumowanie] 적중시 대상이 보유한 부정적인 효과 수에 비례하여 정신력 회복
   źródło: Passives.json :: dataList[id=1010931].summary
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Kwestia głosowa [get_10109_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=get_10109_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Kwestia głosowa [get_10109_1] (Identity Acquisition)] 그대께서 새로운 영감을 불러와주시겠는가. 그렇지 않다면… 특별히 흥미가 생기진 않네만.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=get_10109_1].dlg
   limit: do 140 znaków
   EN: Will you rekindle the inspiration within me anew? If not... then I can't say that I am terribly interested.
   PL:
669. [Kwestia głosowa [lobby_morning_10109_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=lobby_morning_10109_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Kwestia głosowa [lobby_morning_10109_1] (Morning Greeting)] 커튼은 걷지 말게. 갑작스러운 아침 햇살에 방금까지 집중하고 있던 이 점의 밀도를 잃기 싫으니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=lobby_morning_10109_1].dlg
   limit: do 170 znaków
   EN: Open not the curtains; I fear that a sudden light of dawn may disturb the density of this dot I have been pouring my focus in.
   PL:
671. [Kwestia głosowa [lobby_noon_10109_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=lobby_noon_10109_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Kwestia głosowa [lobby_noon_10109_1] (Afternoon Greeting)] 5초 안에 영양을 공급받을 수 있는 식사가 있으면 참 좋겠구료. 하루의 절반을 가르는 이 순간에, 식사라는 보잘것없는 행위로 작품을 만들 시간을 해친다니…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=lobby_noon_10109_1].dlg
   limit: do 280 znaków
   EN: Oh, how I wish there was a meal that could be consumed in five seconds. To waste so much time I could have used to create... on something so pointless yet vital at the exact bisection of a full day... How regrettable.
   PL:
673. [Kwestia głosowa [lobby_night_10109_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=lobby_night_10109_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Kwestia głosowa [lobby_night_10109_1] (Evening Greeting)] 잠은 죽어서 자는 것이오. 생명이 정지하면 그 순간 작품을 만들 기회도 흩어지니. 그러니 순간순간을 오롯이 작품에 투자해야만 하오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=lobby_night_10109_1].dlg
   limit: do 310 znaków
   EN: Sleep shall claim me only when it knocks with death as its companion. Understand that cessation of life is, in turn, a complete elimination of any potential to create. Thus every waking moment must be fully devoted to the creation of art.
   PL:
675. [Kwestia głosowa [smalltalk_10109_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=smalltalk_10109_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Kwestia głosowa [smalltalk_10109_1] (Chatter #1)] 비록 반지 한 바퀴짜리의 수습생이라 한들, 제법 챙겨야 할 일은 많소.\n마에스트로께서 내려주시는 과제를 충실히 해내고, 주민들이 내놓는 실없는 작품을 평가해야만 하지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=smalltalk_10109_1].dlg
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Though I am but an apprentice with a single coil of a ring, there is much that requires my attention.\nThe Maestro's assignments to be completed, the civilians' drab 'artwork' to be evaluated...
   PL:
677. [Kwestia głosowa [smalltalk_10109_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=smalltalk_10109_2].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Kwestia głosowa [smalltalk_10109_2] (Chatter #2)] 불만… 이라. 붓을 자유로이 놀릴 수 있는 것과는 달리, 그다지 동의할 수 없는 도슨트들의 작품성에도 마음에 없는 칭찬이 강제된다는 점은 다소 불만이 있소.\n하지만, 자그마한 티끌과도 같은 단점일 뿐이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=smalltalk_10109_2].dlg
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Any disgruntlements, you ask...? Mm, I do find it regrettable that my freedom in wielding the brush extends not to critiquing the artistic merit of works created by Docents. Oft am I compelled to compliment their pieces, when no such sentiment could be found in my heart.\nThis is but a very, very miniscule disgruntlement, mind.
   PL:
679. [Kwestia głosowa [smalltalk_10109_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=smalltalk_10109_3].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Kwestia głosowa [smalltalk_10109_3] (Chatter #3)] 과거는 그다지 돌볼 필요가 없소. 작품과 통찰은 계속해서 발전해 나가기 때문이오.\n아, 뭐… 과거의 작품을 재해석하여 만드는 것은 상당히 흥미로울 수 있겠구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=smalltalk_10109_3].dlg
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The past deserves very little care. The art and the surrounding insight must always remain in a constant state of transformative improvement; capricious like quicksilver, if you will.\nOh, hm... Reinterpreting past works to remake them could prove interesting, indeed.
   PL:
681. [Kwestia głosowa [smalltalk_10109_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=smalltalk_10109_4].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Kwestia głosowa [smalltalk_10109_4] (Post-Uptie Chat 1)] 이것도 낙제, 흠… 이것도 낙제. …아! 자네, B+. 이 구정물 속에서 유일하게 빛나는 연꽃이구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=smalltalk_10109_4].dlg
   limit: do 190 znaków
   EN: F. Hm... another F. ... Ah! B+ for you, my friend; your work is like a solitary lotus, blooming its budded beauty in a mud pit of mediocrity.
   PL:
683. [Kwestia głosowa [smalltalk_10109_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=smalltalk_10109_5].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Kwestia głosowa [smalltalk_10109_5] (Post-Uptie Chat 2)] 내 자네의 작품이나, 영감을 떠올리는 모습이 제법 마음에 들었소. 이번엔 친히 부족한 부분을 내가 다시 그려줄테니… 다음 번엔 더욱 나를 놀라게 할 만한 것을 가져와 보시게.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=smalltalk_10109_5].dlg
   limit: do 290 znaków
   EN: I find your entire artistic process—from conceptualization to production—quite satisfactory. Please surprise me further with another creation of yours. I shall do my best to complement your work, should aught need touching up.
   PL:
685. [Kwestia głosowa [neglect_10109_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=neglect_10109_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Kwestia głosowa [neglect_10109_1] (Idle)] 흐음. 구상의 시간을 방해치는 않겠소. 그것이 귀중하다는 건 내 잘 알고 있으니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=neglect_10109_1].dlg
   limit: do 150 znaków
   EN: Hm. I shall not disturb you as you meditate on your next project. Well do I understand the import of such hours.
   PL:
687. [Kwestia głosowa [gacksung_10109_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=gacksung_10109_1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Kwestia głosowa [gacksung_10109_1] (Uptying)] 아하, 그대도 평가의 순간이 궁금했소? 이리 와보시게. 볼만한 것들을 몇 개 짚어드리지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=gacksung_10109_1].dlg
   limit: do 150 znaków
   EN: Aha, you wished to watch as I evaluated them? Come hither; allow me to guide you to those that are worth viewing.
   PL:
689. [Kwestia głosowa [formation_10109_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=formation_10109_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Kwestia głosowa [formation_10109_1] (Deployment)] 소재가 준비됐소?
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=formation_10109_1].dlg
   limit: do 120 znaków
   EN: I suppose the ingredients are ready?
   PL:
691. [Kwestia głosowa [battleentry_10109_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battleentry_10109_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Kwestia głosowa [battleentry_10109_1] (Stage Entry)] 이것 참, 설레는구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battleentry_10109_1].dlg
   limit: do 120 znaków
   EN: My, this is quite exciting.
   PL:
693. [Kwestia głosowa [battle_select_10109_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_select_10109_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Kwestia głosowa [battle_select_10109_1] (Viewed in Battle)] 내 작품에 의견이라도 있소?
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_select_10109_1].dlg
   limit: do 120 znaków
   EN: Have you aught to say about my work?
   PL:
695. [Kwestia głosowa [battle_endcommand_10109_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_endcommand_10109_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Kwestia głosowa [battle_endcommand_10109_1] (Commencing Attack)] 점찍었네!
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_endcommand_10109_1].dlg
   limit: do 120 znaków
   EN: Quite the pointed critique!
   PL:
697. [Kwestia głosowa [battle_enemy_break_10109_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_enemy_break_10109_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Kwestia głosowa [battle_enemy_break_10109_1] (Enemy Stagger)] 비뚤어졌구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_enemy_break_10109_1].dlg
   limit: do 120 znaków
   EN: Mm, this piece is off-balance.
   PL:
699. [Kwestia głosowa [battle_break_10109_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_break_10109_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Kwestia głosowa [battle_break_10109_1] (Staggered)] 큭…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_break_10109_1].dlg
   limit: do 120 znaków
   EN: Kngh...
   PL:
701. [Kwestia głosowa [battle_kill_10109_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_kill_10109_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Kwestia głosowa [battle_kill_10109_1] (Enemy Killed)] 이제야, 완성되었나.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_kill_10109_1].dlg
   limit: do 120 znaków
   EN: Finally... it is complete.
   PL:
703. [Kwestia głosowa [battle_dead_10109_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_dead_10109_1].desc
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Kwestia głosowa [battle_dead_10109_1] (Death)] 작품을 만들다 죽을 수 있다니… 그야말로… 이상… 적…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_dead_10109_1].dlg
   limit: do 130 znaków
   EN: To perish in the process of artistic creation... Truly, there is no... death... more ideal...
   PL:
705. [Kwestia głosowa [choice_success_p_10109_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=choice_success_p_10109_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Kwestia głosowa [choice_success_p_10109_2] (Check Passed)] 합격점이구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=choice_success_p_10109_2].dlg
   limit: do 120 znaków
   EN: That is a passing grade.
   PL:
707. [Kwestia głosowa [choice_fail_n_10109_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=choice_fail_n_10109_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [Kwestia głosowa [choice_fail_n_10109_1] (Check Failed)] 음… 낙제점인가…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=choice_fail_n_10109_1].dlg
   limit: do 120 znaków
   EN: Mm... that may be a failing grade.
   PL:
709. [Kwestia głosowa [battle_clear_10109_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_clear_10109_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Kwestia głosowa [battle_clear_10109_1] (Victory Cry)] 나쁘지는 않았구료. 붓을 몇 번 더 놀릴 기회만 있었어도 좋았을 것 같지만…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_clear_10109_1].dlg
   limit: do 130 znaków
   EN: It is... passable. Though I very much wish that I had more opportunity to wield this brush...
   PL:
711. [Kwestia głosowa [battle_clear_ex_10109_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_clear_ex_10109_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Kwestia głosowa [battle_clear_ex_10109_1] (Extra Conditions Fulfilled)] 걸작을 자아냈나… 후우, 마에스트로 님이 어떤 평가를 내려주실지, 흥분이 가시지 않는구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_clear_ex_10109_1].dlg
   limit: do 190 znaków
   EN: Quite the artistic tour de force we have produced... Ah, I cannot help but be overcome with anticipation for the Maestro's critique of this piece.
   PL:
713. [Kwestia głosowa [battle_defeat_10109_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_defeat_10109_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Kwestia głosowa [battle_defeat_10109_1] (Defeat Wail)] 최악이오… 소재는 망가졌고, 영감은 이미 떠난지 오래지. 이리도 굴욕적인 기분은 참으로 오랜만이군…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Rings_10109.json :: dataList[id=battle_defeat_10109_1].dlg
   limit: do 170 znaków
   EN: How dreadful... The ingredients lay broken, and not an ounce of inspiration remains. I have not felt such shame in a long time.
   PL:

## [000] Lobotomy E.G.O:: Solemn Lament — Yi Sang — 로보토미 E.G.O:: 엄숙한 애도
- ID Tożsamości: `10110` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9104 · HP bazowe: 66 · szybkość: 3–6 / 3–7 / 3–8 / 3–8
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Sinking

715. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n엄숙한 애도
   źródło: Personalities.json :: dataList[id=10110].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::\nSolemn Lament
   PL:
716. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10110].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10110].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [Karta Tożsamości — opis] 이상의 열번째 인격
   źródło: Personalities.json :: dataList[id=10110].desc
   limit: do 120 znaków
   EN: Yi Sang's 10th Identity
   PL:
719. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 떠난이에게 축하를
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=1].name ; dataList[id=1011001].levelList[level=2].name ; dataList[id=1011001].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Celebration for the Departed
   PL:
720. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [BulletLament] 1 소모
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011001].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011001].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: Spend 1 [BulletLament]
   PL:
721. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1011001].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1011001].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BulletLament], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [SinkingWhite] = 나비 / Butterfly
   EN: [OnSucceedAttack] Inflict [SinkingWhite] equal to [BulletLament] spent
   PL:
722. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [BulletLament] 1 소모
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1011001].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 720 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1011001].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1011001].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Sinking]과 모든 [SinkingWhite]의 합이 6 이상이면, 코인 위력 +1\n[WinDuel] [Sinking] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [SinkingWhite], [WinDuel]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [SinkingWhite] = 나비 / Butterfly; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If the sum of the target's [Sinking] and both [SinkingWhite] is 6 or higher, Coin Power +1\n[WinDuel] Inflict +2 [Sinking] Count
   PL:
725. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">보유한 [BulletLament]가 10 이상이면, 합 위력 +1</style>\n대상의 [Sinking]과 모든 [SinkingWhite]의 합이 6 이상이면, 코인 위력 +1\n[WinDuel] [Sinking] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011001].levelList[level=4].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BulletLament], [Sinking], [SinkingWhite], [WinDuel]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [Sinking] = 침잠 / Sinking; [SinkingWhite] = 나비 / Butterfly; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">At 10+ [BulletLament], Clash Power +1</style>\nIf the sum of the target's [Sinking] and both [SinkingWhite] is 6 or higher, Coin Power +1\n[WinDuel] Inflict +2 [Sinking] Count
   PL:
726. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 남은자에게 엄숙한 애도를
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=1].name ; dataList[id=1011002].levelList[level=2].name ; dataList[id=1011002].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Solemn Lament for the Living
   PL:
727. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [BulletLament] 5 소모
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011002].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: Spend 5 [BulletLament]
   PL:
728. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1011002].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1011002].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [BulletLament] 1 소모
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1011002].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 720 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1011002].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1011002].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Sinking]과 모든 [SinkingWhite]의 합이 6 이상이면, 코인 위력 +1\n[WinDuel] [Sinking] 횟수 1 증가\n[EndSkill] 최대 공명 수만큼 [BulletLament]를 얻음 (최대 6)\n- 해당 공명이 완전 공명이면, (최대 공명 수 x 2)만큼 얻음 (최대 12)
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=2].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [SinkingWhite], [WinDuel], [EndSkill], [BulletLament]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [SinkingWhite] = 나비 / Butterfly; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]; [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: If the sum of the target's [Sinking] and both [SinkingWhite] is 6 or higher, Coin Power +1\n[WinDuel] Inflict +1 [Sinking] Count\n[EndSkill] Gain (highest Reson.) of [BulletLament] (max 6)\n- If the said Reson. was an A-Reson., gain (highest Reson. x 2) of [BulletLament] (max 12)
   PL:
732. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 보유한 [BulletLament]가 10 이상이면, 합 위력 +1\n대상의 [Sinking]과 모든 [SinkingWhite]의 <style="highlight">합 6 당, 코인 위력 +1(최대 2)</style>\n[WinDuel] [Sinking] 횟수 1 증가\n[EndSkill] 최대 공명 수만큼 [BulletLament]를 얻음 (최대 6)\n- 해당 공명이 완전 공명이면, (최대 공명 수 x 2)만큼 얻음 (최대 12)\n<style="highlight"> - 해당 공명이 완전 공명 4 이상이면, 대신 [ReloadLament]</style>
   źródło: Skills_personality-01.json :: dataList[id=1011002].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BulletLament], [Sinking], [SinkingWhite], [WinDuel], [EndSkill], [ReloadLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [Sinking] = 침잠 / Sinking; [SinkingWhite] = 나비 / Butterfly; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]; [ReloadLament] = 재장전 / Reload
   EN: At 10+ [BulletLament], Clash Power +1\n<style="highlight">Coin Power +1 for every 6 value</style> of the sum of the target's [Sinking] and both [SinkingWhite] <style="highlight">(max 2)</style>\n[WinDuel] Inflict +1 [Sinking] Count\n[EndSkill] Gain (highest Reson.) of [BulletLament] (max 6)\n- If the said Reson. was an A-Reson., gain (highest Reson. x 2) of [BulletLament] (max 12)\n<style="highlight"> - If the said Reson. was at 4+ A-Reson., [ReloadLament] instead</style>
   PL:
733. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 이상으로 장례는 이상이오
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].name ; dataList[id=1011003].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Goodbye Now, a Sorrow in You
   PL:
734. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 보유한 [BulletLament] 10마다, 기본 위력 +1 (최대 2)\n[WinDuel] [Sinking] 횟수 3 증가\n[EndSkill] [ReloadLament]
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [BulletLament], [WinDuel], [Sinking], [EndSkill], [ReloadLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [WinDuel] = [합 승리시] / [Clash Win]; [Sinking] = 침잠 / Sinking; [EndSkill] = [공격 종료시] / [Attack End]; [ReloadLament] = 재장전 / Reload
   EN: Base Power +1 for every 10 value of [BulletLament] (max 2)\n[WinDuel] Inflict +3 [Sinking] Count\n[EndSkill] [ReloadLament]
   PL:
735. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [BulletLament] 1 소모
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1011003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 720 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
736. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1011003].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [BulletLament] 6 소모
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1011003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: Spend 6 [BulletLament]
   PL:
738. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1011003].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] 보유한 [BulletLament] 전부 소모
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1011003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: Spend all of [BulletLament] on self
   PL:
740. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 소모한 [BulletLament]만큼 [SinkingWhite] 부여
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1011003].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
741. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 이 스킬에서 소모한 [BulletLament] 1당 피해량 +2%
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BulletLament]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: [OnSucceedAttack] Deal +2% damage for every value of [BulletLament] spent by this Skill
   PL:
742. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 모든 [SinkingWhite]만큼 우울 피해\n- 산나비와 죽은나비의 합으로 계산
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1011003].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [SinkingWhite]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SinkingWhite] = 나비 / Butterfly
   EN: [OnSucceedAttack] Inflict Gloom damage equal to "All" [SinkingWhite] on target\n- "All" = the sum of both The Living and The Departed on target
   PL:
743. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 보유한 [BulletLament] <style="highlight">5</style> 마다 기본 위력 +1 <style="highlight">(최대 4)</style>\n대상의 [Sinking]과 모든 [SinkingWhite]의 합 6당, 코인 위력 +1 (최대 2)\n[WinDuel] [Sinking] 횟수 3 증가\n[EndSkill] [ReloadLament]
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BulletLament], [Sinking], [SinkingWhite], [WinDuel], [EndSkill], [ReloadLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [Sinking] = 침잠 / Sinking; [SinkingWhite] = 나비 / Butterfly; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]; [ReloadLament] = 재장전 / Reload
   EN: Base Power +1 for every <style="highlight">5</style> value of [BulletLament] <style="highlight">(max 4)</style>\nCoin Power +1 for every 6 value of the sum of the target's [Sinking] and both [SinkingWhite] (max 2)\n[WinDuel] Inflict +3 [Sinking] Count\n[EndSkill] [ReloadLament]
   PL:
744. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 이 스킬에서 소모한 [BulletLament] 1당 피해량 +4%
   źródło: Skills_personality-01.json :: dataList[id=1011003].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BulletLament]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BulletLament] = 산나비·죽은나비 / The Living & The Departed
   EN: [OnSucceedAttack] Deal +4% damage for every value of [BulletLament] spent by this Skill
   PL:
745. [Obrona (ulepszenia 1,4) — nazwa] 관에서나비가날아오리라
   źródło: Skills_personality-01.json :: dataList[id=1011004].levelList[level=1].name ; dataList[id=1011004].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 50 znaków
   EN: FromTheCoffinAButterflyTakesFlight
   PL:
746. [Obrona (ulepszenie 1) — opis] [StartBattle] [ReloadLament] (턴 당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [ReloadLament]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ReloadLament] = 재장전 / Reload
   EN: [StartBattle] [ReloadLament] (once per turn)
   PL:
747. [Obrona (ulepszenie 4) — opis] [StartBattle] [ReloadLament] (턴 당 1회)\n[StartBattle] 최대 체력의 (지정한 대상의 모든 [SinkingWhite])% 만큼 보호막을 얻음. (턴 당 최대 20%)
   źródło: Skills_personality-01.json :: dataList[id=1011004].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [ReloadLament], [SinkingWhite]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ReloadLament] = 재장전 / Reload; [SinkingWhite] = 나비 / Butterfly
   EN: [StartBattle] [ReloadLament] (once per turn)\n[StartBattle] Gain Shield equal to (the sum of both [SinkingWhite] on the selected target)% HP (max 20% per turn)
   PL:
748. [Pasywka bojowa (od ulepszenia 1) — nazwa] 죽어가는나비를본다.
   źródło: Passives.json :: dataList[id=1011002].name
   limit: do 40 znaków
   EN: ISeeTheDyingButterfly.
   PL:
749. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 시작 시 [BulletLament]를 각각 10씩 보유함.\n\n [BulletLament]를 소모할 때, 해당 효과의 산나비(위력)와 죽은나비(횟수)를 무작위로 소모.\n\n[SinkingWhite]를 부여할 때, 해당 코인에서 소모한 [BulletLament]에 따라 부여.\n- 산나비를 소모했으면, 소모한 값만큼 산나비를 부여.\n- 죽은나비를 소모했으면, 소모한 값만큼 죽은나비를 부여.\n\n스킬 사용 중 [BulletLament]가 부족하면, 다음 코인을 모두 취소하고 [ReloadLament]\n\n[ReloadLament]을 하거나 [BulletLament]를 얻을 때, 현재 정신력에 따라 얻는 나비가 정해짐.\n- 정신력이 0 이상이면, 30% 확률로 산나비를, 70% 확률로 죽은나비를 얻음.\n- 정신력이 0 미만이면, 70% 확률로 산나비를, 30% 확률로 죽은나비를 얻음.\n- 확률은 각 탄환마다 개별적으로 적용됨.
   źródło: Passives.json :: dataList[id=1011002].desc
   limit: do 1110 znaków
   tokeny: zachowaj dokładnie: \n, [BulletLament], [SinkingWhite], [ReloadLament]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [SinkingWhite] = 나비 / Butterfly; [ReloadLament] = 재장전 / Reload
   EN: Begin encounters with 10 of each of [BulletLament]\n\nWhen spending [BulletLament], select randomly between The Living(Potency) and The Departed(Count) for each [BulletLament] value\n\nWhen inflicting [SinkingWhite], inflict the same amount of The Living and The Departed as they were consumed. Example below:\n- If this unit spent X Living, inflict X Living\n- If this unit spent Y Departed, inflict Y Departed\n\nIf this unit runs out of [BulletLament] midway through Skill use, cancel all subsequent Coins and [ReloadLament]\n\nWhen [ReloadLament]ing, or when gaining [BulletLament], gain either The Living or The Departed based on this unit's current SP\n- At 0 or higher SP: 30% chance to gain The Living; 70% chance to gain The Departed\n- At less than 0 SP: 70% chance to gain The Living; 30% chance to gain The Departed\n- The probabilities are calculated separately for each ammo spent
   PL:
750. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 스킬 사용 중 탄환이 부족하면 재장전
   źródło: Passives.json :: dataList[id=1011002].summary
   limit: do 120 znaków
   EN: Reloads if this unit runs out of Ammo midway through Skill use
   PL:
751. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — nazwa] 쏘아라.쏘으리로다.
   źródło: Passives.json :: dataList[id=1011001].name
   limit: do 40 znaków
   EN: Fire.IShallFire.
   PL:
752. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — opis] [BulletLament]를 얻으면, 다음 턴에 [Agility] 2 얻음 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1011001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletLament], [Agility]
   znaczenie tagów: [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [Agility] = 신속 / Haste
   EN: When this unit gains [BulletLament], gain 2 [Agility] next turn (once per turn)
   PL:
753. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — podsumowanie] 탄환을 얻으면, 다음 턴에 신속을 얻음
   źródło: Passives.json :: dataList[id=1011001].summary
   limit: do 120 znaków
   EN: When this unit gains Ammo, gain Agility next turn
   PL:
754. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — nazwa] 쏘아라.쏘으리로다.
   źródło: Passives.json :: dataList[id=1011011].name
   (powtórzenie elementu 751 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — opis] 공격 종료시 자신의 스킬에 의해 대상이 사망했으면, [ReloadLament]\n[BulletLament]를 얻으면, 다음 턴에 [Agility] 2 얻음 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1011011].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [ReloadLament], [BulletLament], [Agility]
   znaczenie tagów: [ReloadLament] = 재장전 / Reload; [BulletLament] = 산나비·죽은나비 / The Living & The Departed; [Agility] = 신속 / Haste
   EN: Attack End: If this unit killed the target with its Skill, [ReloadLament]\nWhen this unit gains [BulletLament], gain 2 [Agility] next turn (once per turn)
   PL:
756. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — podsumowanie] 탄환을 얻으면, 다음 턴에 신속을 얻음. 대상 처치시, 재장전
   źródło: Passives.json :: dataList[id=1011011].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: When this unit gains Ammo, gain [Agility] next turn. On Kill, Reload
   PL:
757. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Gloom) — nazwa] 구원의 손
   źródło: Passives.json :: dataList[id=1011021].name
   limit: do 40 znaków
   EN: Hand of Salvation
   PL:
758. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Gloom) — opis] 아군의 스킬 적중 시 대상의 [Sinking]을 2 소모하여 [SinkingWhite] 1 부여 (턴 당 3회)
   źródło: Passives.json :: dataList[id=1011021].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Sinking], [SinkingWhite]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [SinkingWhite] = 나비 / Butterfly
   EN: When an ally hits with a Skill, consume 2 [Sinking] on the target to inflict them with 1 [SinkingWhite] (3 times per turn)
   PL:
759. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Gloom) — podsumowanie] 대상의 침잠을 나비로 전환
   źródło: Passives.json :: dataList[id=1011021].summary
   limit: do 120 znaków
   EN: Convert target's Sinking into Butterfly
   PL:
760. [Kwestia głosowa [get_10110_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=get_10110_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Kwestia głosowa [get_10110_1] (Identity Acquisition)] 죽음에 관한 그대의 의견은 잘 알았소. 잠시, 충동적인 마음은 접어두고 좀 더 대화해보지 않겠는가.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=get_10110_1].dlg
   limit: do 170 znaków
   EN: Well do I understand your sentiment on death. Why not lay rest to the impulses in your heart for a moment and converse with me more?
   PL:
762. [Kwestia głosowa [lobby_morning_10110_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=lobby_morning_10110_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Kwestia głosowa [lobby_morning_10110_1] (Morning Greeting)] 이른 아침부터 그대를 귀찮게 한 것은 미안하게 여기고 있소. 그대의 꿈을 깨우지는 않았는가 하여.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=lobby_morning_10110_1].dlg
   limit: do 140 znaków
   EN: I apologize for bothering you in such early hours of the morning. I hope I did not wrest you from a dream.
   PL:
764. [Kwestia głosowa [lobby_noon_10110_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=lobby_noon_10110_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Kwestia głosowa [lobby_noon_10110_1] (Afternoon Greeting)] 점심 식사를 하고 오지는 않았소. 그대와 나눈 이야기가 사색에 잠기기 워낙 좋은 주제인지라.\n그대도 누군가를 애도할 때는 응당 그러했겠지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=lobby_noon_10110_1].dlg
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I did not lunch, for my contemplation upon our earlier conversation consumed most of the noon away.\nI suppose you had done the same as you mourned for others, and rightly so.
   PL:
766. [Kwestia głosowa [lobby_night_10110_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=lobby_night_10110_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Kwestia głosowa [lobby_night_10110_1] (Evening Greeting)] 금일의 관리는 지금이 마지막일 예정이오. 그대도 고단하리라 보오만, 씁씁한 고찰은 잠시 내려두고 단잠을 청해보는 것이 어떠한가.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=lobby_night_10110_1].dlg
   limit: do 220 znaków
   EN: This will be the last management work of the day. You appear rather spent yourself; why not leave behind the bitter ruminations and seek the sweetness of a brief slumber?
   PL:
768. [Kwestia głosowa [smalltalk_10110_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=smalltalk_10110_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Kwestia głosowa [smalltalk_10110_1] (Chatter #1)] 사람이 죽으면 어디로 가는가. 과연 고찰함직한 화두로구료. 내 언젠가 삶의 끝에 대한 생각을 기록으로 남겼던 적이 있었소만, 차후에는 그것과 함께 담소를 나누어보지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=smalltalk_10110_1].dlg
   limit: do 250 znaków
   EN: Where do humans go upon the final egress from life? You ask a rather stimulating question. I have once written my reflections on the end of life; perhaps we may have a chance to discuss it later.
   PL:
770. [Kwestia głosowa [smalltalk_10110_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=smalltalk_10110_2].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Kwestia głosowa [smalltalk_10110_2] (Chatter #2)] 유서를 열세 벌이나 적어내려갔었음에도, 나는 나의 죽음을 애도할 자가 있지는 않을 것이라는 생각이 들었소.\n그런 자들이 있었다면 좋았을 것이오. 이곳에는 떠난 자를 추억할 여유 하나 없는 자들 뿐이니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=smalltalk_10110_2].dlg
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Even as I wrote my thirteen wills, I could not help but believe that no one would mourn me upon the event of my death.\nIt would have been nice to have those who would lament my passing, yet the remembrance of the dead has no place in the hearts of those who live here.
   PL:
772. [Kwestia głosowa [smalltalk_10110_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=smalltalk_10110_3].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Kwestia głosowa [smalltalk_10110_3] (Chatter #3)] 총구에서 나비의 탄환이 발사되는 것이 아니오, 총이 향한 좌표에 산 나비와 죽은 나비들이 피어날 따름이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=smalltalk_10110_3].dlg
   limit: do 190 znaków
   EN: The barrel of the gun does not fire bullets of butterflies; it is merely that butterflies, both living and dead, bloom from where the gun points.
   PL:
774. [Kwestia głosowa [smalltalk_10110_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=smalltalk_10110_4].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Kwestia głosowa [smalltalk_10110_4] (Post-Uptie Chat 1)] 그대가 선물이라 말하며 지워준 이 관은 제법 무겁소. 또한 그대가 사유하던 나비들이 내게 깃든 것 또한 가볍게 쏘아내기 어렵구료.\n애도의 마음에 불현듯한 경박함 한오라기라도 잘못 씌워질까 나는 두렵기만 하오. …그러니 엄숙한 마음으로 방아쇠를 당겨야만 하겠지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=smalltalk_10110_4].dlg
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This coffin, this gift you have given me to shoulder—it carries quite the weight. The butterflies that have nested in me, those that have been once yours, are also not to be fired with a light heart.\nI fear letting even the lightest wisp of frivolity upon this lament. ... Thus, it is only right that I wreath solemness upon my heart as I pull their triggers.
   PL:
776. [Kwestia głosowa [smalltalk_10110_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=smalltalk_10110_5].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Kwestia głosowa [smalltalk_10110_5] (Post-Uptie Chat 2)] 애도에 미사여구는 필요치 않겠소. 혹자 말하길 이 관을 맨 애도자가 비로소 구원의 사자라고 하더마는…\n본인 또한 날개에 꽂힌 단순한 깃털일 뿐, 그 외의 가치는 하등 없소. 나도 언젠가 꽃가루를 찾지 않는 나비가 될 테니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=smalltalk_10110_5].dlg
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There is no need for showy, purple prose in expressing condolences. Some say that the mourner shouldering this coffin is the long-awaited savior to all, yet...\n... I am but a feather stuck upon a Wing; the worth of my being, otherwise, nil; for I am also fluttering the path to becoming a butterfly that pollinates no more.
   PL:
778. [Kwestia głosowa [neglect_10110_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=neglect_10110_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Kwestia głosowa [neglect_10110_1] (Idle)] 내가 죽는다면, 유리창 저 너머의 통화구는 꼭 막으며 죽으려 하오. 그리해야 내게 앉았던 나비도 날아갈테니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=neglect_10110_1].dlg
   limit: do 190 znaków
   EN: I intend to shut the speech-hole beyond the window tight if I were to meet my demise. Only then will the butterfly who rests upon me flutter away.
   PL:
780. [Kwestia głosowa [gacksung_10110_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=gacksung_10110_1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Kwestia głosowa [gacksung_10110_1] (Uptying)] 과분한 선물을 등에 졌소. 갈 곳 잃은 영혼들은 두 손에 꽉 쥐었소.\n이제 우리는 어디로 나아가야 하겠소?
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=gacksung_10110_1].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It is a heavy gift that I shoulder; a twain of wayward souls in each of my palms, fingers held ever-closer.\nWhere lies our destination now?
   PL:
782. [Kwestia głosowa [formation_10110_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=formation_10110_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Kwestia głosowa [formation_10110_1] (Deployment)] 관리인가, 아니면 애도인가?
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=formation_10110_1].dlg
   limit: do 120 znaków
   EN: Is it management or lamentation?
   PL:
784. [Kwestia głosowa [battleentry_10110_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battleentry_10110_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Kwestia głosowa [battleentry_10110_1] (Stage Entry)] 죽음충동 억제, 관념 봉인.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battleentry_10110_1].dlg
   limit: do 120 znaków
   EN: Death urges suppressed; concept sealed.
   PL:
786. [Kwestia głosowa [battle_select_10110_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_select_10110_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Kwestia głosowa [battle_select_10110_1] (Viewed in Battle)] 애도에 잡담이 끼어드는 것은 좋지 않소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_select_10110_1].dlg
   limit: do 120 znaków
   EN: Idle chatter is ill-advised in mourning.
   PL:
788. [Kwestia głosowa [battle_endcommand_10110_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_endcommand_10110_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Kwestia głosowa [battle_endcommand_10110_1] (Commencing Attack)] 나아가주게.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_endcommand_10110_1].dlg
   limit: do 120 znaków
   EN: Please, step forth.
   PL:
790. [Kwestia głosowa [battle_enemy_break_10110_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_enemy_break_10110_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Kwestia głosowa [battle_enemy_break_10110_1] (Enemy Stagger)] 그대 또한 잠들게.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_enemy_break_10110_1].dlg
   limit: do 120 znaków
   EN: Go into the night without worry.
   PL:
792. [Kwestia głosowa [battle_break_10110_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_break_10110_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Kwestia głosowa [battle_break_10110_1] (Staggered)] 음…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_break_10110_1].dlg
   limit: do 120 znaków
   EN: Mm...
   PL:
794. [Kwestia głosowa [battle_kill_10110_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_kill_10110_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Kwestia głosowa [battle_kill_10110_1] (Enemy Killed)] 내 잠든 그대를 기릴테니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_kill_10110_1].dlg
   limit: do 120 znaków
   EN: For your remembrance shall be mine as you sleep.
   PL:
796. [Kwestia głosowa [battle_dead_10110_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_dead_10110_1].desc
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Kwestia głosowa [battle_dead_10110_1] (Death)] 작은 나비의 날개라 해도… 이곳을… 벗어날 수 있… 었을지…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_dead_10110_1].dlg
   limit: do 120 znaków
   EN: Could the small wings... of a butterfly have... fluttered away from this... place...?
   PL:
798. [Kwestia głosowa [choice_success_p_10110_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=choice_success_p_10110_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Kwestia głosowa [choice_success_p_10110_2] (Check Passed)] 억압 작업이 성공했소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=choice_success_p_10110_2].dlg
   limit: do 120 znaków
   EN: Repression work yielded a more preferable result.
   PL:
800. [Kwestia głosowa [choice_fail_n_10110_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=choice_fail_n_10110_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Kwestia głosowa [choice_fail_n_10110_1] (Check Failed)] 애착 작업은 옳지 않았소…
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=choice_fail_n_10110_1].dlg
   limit: do 120 znaków
   EN: Attachment work was quite... the incongruent choice.
   PL:
802. [Kwestia głosowa [battle_clear_10110_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_clear_10110_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Kwestia głosowa [battle_clear_10110_1] (Victory Cry)] 잠든 자들에게는 기꺼이 꽃 한 송이를 놓겠소. 나비가 그들에게 피어날 수 있도록.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_clear_10110_1].dlg
   limit: do 120 znaków
   EN: A willing flower, for those who slumber. May they bloom the butterflies within.
   PL:
804. [Kwestia głosowa [battle_clear_ex_10110_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_clear_ex_10110_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Kwestia głosowa [battle_clear_ex_10110_1] (Extra Conditions Fulfilled)] 한 자루는 죽어 떠난 자에 대한 축하를, 한 자루는 목숨에 묶여 살아갈 자에 대한 엄숙한 애도를. 장례는 이상으로 끝내겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_clear_ex_10110_1].dlg
   limit: do 220 znaków
   EN: One handgun, a congratulation for the departed dead; the other, a lamentation for the life-bound in living stead. Thus yield into solemnity, all; now grieve them nevermore.
   PL:
806. [Kwestia głosowa [battle_defeat_10110_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_defeat_10110_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Kwestia głosowa [battle_defeat_10110_1] (Defeat Wail)] 깨어진 거울 가운데에 죽어가는 나비를 보고 있소. 애도의 임무가 내게 있으나 정작 떠도는 나비를 피워내지 못하니, 애석할 따름이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_Funeral_10110.json :: dataList[id=battle_defeat_10110_1].dlg
   limit: do 230 znaków
   EN: At the heart of a broken mirror, I see the fading butterfly. A wandering butterfly I cannot bloom, yet the duty of lamentation is mine; thus, it is also mine, this melancholy.
   PL:

## [00] LCE E.G.O:: Lantern — Yi Sang — LCE E.G.O:: 초롱
- ID Tożsamości: `10111` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 5 · HP bazowe: 73 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Rupture

808. [Karta Tożsamości — tytuł] LCE E.G.O::\n초롱
   źródło: Personalities.json :: dataList[id=10111].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCE E.G.O::\nLantern
   PL:
809. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10111].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10111].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Karta Tożsamości — opis] 이상의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10111].desc
   limit: do 120 znaków
   EN: Yi Sang's 11th Identity
   PL:
812. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] E.G.O는 제식 장비라 할지라도,
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=1].name ; dataList[id=1011101].levelList[level=2].name ; dataList[id=1011101].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 2 (+3)
   limit: do 100 znaków
   EN: Though it must be prefaced that E.G.O gears are standardized equipment,
   PL:
813. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Aggro] 2 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst]을 부여하지 않음.
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture
   EN: [WhenUse] Gain +2 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] with its effects
   PL:
814. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
815. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1011101].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1011101].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
816. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1011101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 814 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1011101].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1011101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 815 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [StartBattle] 자신을 타겟팅 한 스킬의 수만큼 합 패배 시 최종 위력이 증가 (최대 2)\n[WhenUse] 다음 턴에 [Aggro] 3 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst]을 부여하지 않음.\n[DefeatDuel] 이 스킬에서 부여하는 [Burst] 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=2].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Aggro], [Burst], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] On Clash Lose, gain Final Power equal to the number of Skills targeting this unit (max 2)\n[WhenUse] Gain +3 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] with its effects\n[DefeatDuel] [Burst] Potency inflicted by this Skill +1
   PL:
819. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [StartBattle] 자신을 타겟팅 한 스킬의 수만큼 합 패배 시 최종 위력이 증가 (최대 3)\n[WhenUse] 다음 턴에 [Aggro] 3 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst]을 부여하지 않음.\n[DefeatDuel] 이 스킬에서 부여하는 [Burst] 위력 +2
   źródło: Skills_personality-01.json :: dataList[id=1011101].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Aggro], [Burst], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] On Clash Lose, gain Final Power equal to the number of Skills targeting this unit (max 3)\n[WhenUse] Gain +3 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] with its effects\n[DefeatDuel] [Burst] Potency inflicted by this Skill +2
   PL:
820. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 로보토미때의 E.G.O보다 환상체와의 감응 정도에 따라
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=1].name ; dataList[id=1011102].levelList[level=2].name ; dataList[id=1011102].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 8 · monety: 1 (+6)
   limit: do 140 znaków
   EN: when juxtaposed with E.G.O gear from L Corp., depending on the degree of attunement to the Abnormality,
   PL:
821. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Aggro] 2 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 횟수를 부여하지 않음.
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture
   EN: [WhenUse] Gain +2 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Count with its effects
   PL:
822. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 814 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL:
824. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [StartBattle] 자신을 타겟팅 한 스킬의 수 만큼 합 패배 시 최종 위력이 증가 (최대 3)\n[WhenUse] 다음 턴에 [Aggro] 3 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 횟수를 부여하지 않음.\n[DefeatDuel] 이 스킬에서 부여하는 [Burst] 횟수 +1
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=2].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Aggro], [Burst], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] On Clash Lose, gain Final Power equal to the number of Skills targeting this unit (max 3)\n[WhenUse] Gain +3 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Count with its effects\n[DefeatDuel] [Burst] Count inflicted by this Skill +1
   PL:
825. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1011102].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL:
826. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [StartBattle] <style="highlight">(자신을 타겟팅 한 스킬의 수 X 2) 만큼 합 패배 시 최종 위력이 증가 (최대 6)</style>\n[WhenUse] 다음 턴에 [Aggro] 4 얻음\n[WhenUse] 대상의 [Burst] 위력이 15, 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 횟수를 부여하지 않음\n[DefeatDuel] 이 스킬에서 부여하는 [Burst] 횟수 +2
   źródło: Skills_personality-01.json :: dataList[id=1011102].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [WhenUse], [Aggro], [Burst], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] <style="highlight">On Clash Lose, gain (# of Skills targeting this unit x 2) Final Power (max 6)</style>\n[WhenUse] Gain +4 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Count with its effects\n[DefeatDuel] [Burst] Count inflicted by this Skill +2
   PL:
827. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 본체의 특징을 더 유연하게 활용 가능하오
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=3].name ; dataList[id=1011103].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 16 · monety: 3 (−5)
   limit: do 100 znaków
   EN: the idiosyncrasies of the source may be utilized with greater flexibility
   PL:
828. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 잃은 체력 1%당 피해량 0.5% 증가\n[StartBattle] 자신을 타겟팅 한 스킬의 수 만큼 기본 위력 +1 (최대 2)\n[WhenUse] [GlowingLantern] 2 얻음 (턴 당 1회)\n[WhenUse] 다음 턴에 [Aggro] 6 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 위력과 횟수를 부여하지 않고, 기본 위력 +1\n[EndSkill] 정신력 30 회복
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=3].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [GlowingLantern], [Aggro], [Burst], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [GlowingLantern] = 미끼 요정 / Fairy Lure; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +0.5% damage for every 1% missing HP on self\n[StartBattle] Base Power +1 for every Skill that targets this unit (max 2)\n[WhenUse] Gain 2 [GlowingLantern] (once per turn)\n[WhenUse] Gain +6 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Potency or Count with its effects; instead, gain Base Power +1\n[EndSkill] Heal 30 SP
   PL:
829. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 825 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL:
831. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1011103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 815 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1011103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 815 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 잃은 체력 1%당 피해량 0.8% 증가\n[StartBattle] 자신을 타겟팅 한 스킬의 수 만큼 기본 위력 +1 (최대 3)\n[WhenUse] [GlowingLantern] 3 얻음 (턴 당 1회)\n[WhenUse] 다음 턴에 [Aggro] 8 얻음\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 위력과 횟수를 부여하지 않고, 기본 위력 +1\n[EndSkill] 정신력 30 회복
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [GlowingLantern], [Aggro], [Burst], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [GlowingLantern] = 미끼 요정 / Fairy Lure; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +0.8% damage for every 1% missing HP on self\n[StartBattle] Base Power +1 for every Skill that targets this unit (max 3)\n[WhenUse] Gain 3 [GlowingLantern] (once per turn)\n[WhenUse] Gain +8 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Potency or Count with its effects; instead, gain Base Power +1\n[EndSkill] Heal 30 SP
   PL:
834. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL:
835. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011103].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL:
836. [Obrona (ulepszenia 1,4) — nazwa] 다만 그 감응과 동기화 정도에 따라 잡아먹힐 수 있소
   źródło: Skills_personality-01.json :: dataList[id=1011104].levelList[level=1].name ; dataList[id=1011104].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 10 · monety: 1 (+5)
   limit: do 160 znaków
   EN: Yet, the degree to which that attunement and synchronization are achieved may resultantly allow the user to be devoured
   PL:
837. [Obrona (ulepszenie 1) — opis] [StartBattle] [GlowingLantern] 2 얻음 (턴 당 1회)\n[WhenUse] 다음 턴에 [Aggro] 6 얻음\n[WhenUse] 대상의 [Burst] 위력이 15, 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 횟수를 부여하지 않고, 기본 위력 +3
   źródło: Skills_personality-01.json :: dataList[id=1011104].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [GlowingLantern], [WhenUse], [Aggro], [Burst]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [GlowingLantern] = 미끼 요정 / Fairy Lure; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture
   EN: [StartBattle] Gain 2 [GlowingLantern] (once per turn)\n[WhenUse] Gain +6 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Count with its effects; instead, gain Base Power +3
   PL:
838. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011104].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011104].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 825 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Obrona (ulepszenie 4) — opis] [StartBattle] [GlowingLantern] 3 얻음 (턴 당 1회)\n[WhenUse] 다음 턴에 [Aggro] 8 얻음\n[WhenUse] 대상의 [Burst] 위력이 15, 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 횟수를 부여하지 않고, 기본 위력 +3
   źródło: Skills_personality-01.json :: dataList[id=1011104].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [GlowingLantern], [WhenUse], [Aggro], [Burst]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [GlowingLantern] = 미끼 요정 / Fairy Lure; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture
   EN: [StartBattle] Gain 3 [GlowingLantern] (once per turn)\n[WhenUse] Gain +8 [Aggro] next turn\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Count with its effects; instead, gain Base Power +3
   PL:
840. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — nazwa] 외형 또한 이전 L사의 E.G.O에 비해, 환상체와 가깝게 추출할 수 있소
   źródło: Passives.json :: dataList[id=1011101].name
   limit: do 160 znaków
   EN: This is reflected in their appearance, more closely resembling the source Abnormality than E.G.O of the former L Corp. do
   PL:
841. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — opis] 사망 시 자신을 가장 마지막으로 공격한 대상에게 [Burst] 4, [Burst] 횟수 2를 부여하고, 가장 부족한 속성의 E.G.O 자원 4종을 2개씩 얻음.\n- 공격자가 없거나 아군에게 사망한 경우, 현재 [Burst] 횟수가 가장 적은 적에게 [Burst] 4, [Burst] 횟수 2 부여
   źródło: Passives.json :: dataList[id=1011101].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: On death, inflict 4 [Burst] and +2 [Burst] Count against the target that attacked this unit last; then, gain 2 E.G.O resources for 4 least-owned Affinities\n- If no one attacked this unit, or if an ally killed this unit, inflict 4 [Burst] and +2 [Burst] Count against the enemy that has the least [Burst] Count
   PL:
842. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Glut.) — nazwa] 외형 또한 이전 L사의 E.G.O에 비해, 환상체와 가깝게 추출할 수 있소
   źródło: Passives.json :: dataList[id=1011111].name
   (powtórzenie elementu 840 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Glut.) — opis] 사망 시 자신을 가장 마지막으로 공격한 대상에게 [Burst] <style="highlight">5</style>, [Burst] 횟수 <style="highlight">3</style>을 부여하고, 가장 부족한 속성의 E.G.O 자원 4종을 2개씩 얻음.\n- 공격자가 없거나 아군에게 사망한 경우, 현재 [Burst] 횟수가 가장 적은 적에게 [Burst] 5, [Burst] 횟수 3 부여\n- 자신이 [GlowingLantern] 상태인 경우, 이 효과로 부여하는 [Burst] 위력이 2배로 적용됨.
   źródło: Passives.json :: dataList[id=1011111].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [GlowingLantern]
   znaczenie tagów: [Burst] = 파열 / Rupture; [GlowingLantern] = 미끼 요정 / Fairy Lure
   EN: On death, inflict <style="highlight">5</style> [Burst] and +<style="highlight">3</style> [Burst] Count against the target that attacked this unit last; then, gain 2 E.G.O resources for 4 least-owned Affinities\n- If no one attacked this unit, or if an ally killed this unit, inflict 5 [Burst] and +3 [Burst] Count against the enemy that has the least [Burst] Count\n- If this unit is in a [GlowingLantern] state, inflict double the [Burst] Potency with this effect
   PL:
844. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — nazwa] E.G.O가 붕괴될 때 거름과 같이 분해되오
   źródło: Passives.json :: dataList[id=1011121].name
   limit: do 80 znaków
   EN: E.G.O disintegration is not unlike decomposition of compost
   PL:
845. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — opis] 현재 체력이 가장 낮은 아군 1명이 사망 시 가장 부족한 속성의 E.G.O 자원 2종을 2개씩 얻음.
   źródło: Passives.json :: dataList[id=1011121].desc
   limit: do 140 znaków
   EN: When 1 ally that has the lowest current HP is killed, gain 2 E.G.O resources for 2 least-owned Affinities
   PL:
846. [Kwestia głosowa [get_10111_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=get_10111_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Kwestia głosowa [get_10111_1] (Identity Acquisition)] 아, 그대. 잠시 쉬고 가지 않겠나. …그리고 온 김에,\n이 실험 결과 정리를 도와주게. 끝내기 전까지는 돌아갈 수 없으니 도망은 포기하시고.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=get_10111_1].dlg
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ah, rest awhile here, dear fellow. ... And now that you are indeed here, will you assist me in organizing this experiment data?\nAh! Abscond from here you will not, for there is no escape until this work is complete.
   PL:
848. [Kwestia głosowa [lobby_morning_10111_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=lobby_morning_10111_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Kwestia głosowa [lobby_morning_10111_1] (Morning Greeting)] 이 엔케팔린 부서에서 일하는 것에 불만은 크게 없네만… 아침 햇볕을 받을 수 있는 작달막한 테라스라도 있으면 좋겠다는 바램은 있소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=lobby_morning_10111_1].dlg
   limit: do 230 znaków
   EN: I have no significant misgivings about working for the department of Enkephalin... yet a small wish I do maintain, that a tiny terrace to enjoy the morning sun may be built.
   PL:
850. [Kwestia głosowa [lobby_noon_10111_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=lobby_noon_10111_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Kwestia głosowa [lobby_noon_10111_1] (Afternoon Greeting)] 점심은 간단히 때웠소. 격리실에 새로운 환상체가 들어왔다는 소식에 이것저것 시험해보느라 바쁘기도 하고…\n사실, 배고픔을 느끼기엔 이미 이 신선한 실험자료에게서 오는 자극만으로도…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=lobby_noon_10111_1].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I partook in a rather simple lunch today, for I am quite busy with experiments with the news of a new Abnormality's arrival in the containment chamber.\nTo be truthful, any amount of hunger I once had has long been quashed by the stimulation from fresh experimentation subjects...
   PL:
852. [Kwestia głosowa [lobby_night_10111_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=lobby_night_10111_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Kwestia głosowa [lobby_night_10111_1] (Evening Greeting)] 구 L사의 본사나 지부는 꽤 빈번한 야근이 자행되었다 들었소만… 우리 엔케팔린 부서는 무조건적인 정시 퇴근을 지향하고 있소.\n아… 나를 포함한 저 연구원들이 남아 있는 건 단순히 실험에 대한 흥분이 가시질 않아 일을 그만두질 못하고 있는 것 뿐이오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=lobby_night_10111_1].dlg
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Indeed, it is said that the former L Corp. Headquarters and Branches oft engaged in late shifts... but the Enkephalin department prides itself on unconditional adherence to the official office closing hour schedules.\nAh... yet, the researchers, including myself, remain here still at such late an hour. We are, however, bound not by policy but by our very own passions for experimentation.
   PL:
854. [Kwestia głosowa [smalltalk_10111_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=smalltalk_10111_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Kwestia głosowa [smalltalk_10111_1] (Chatter #1)] 나는 구 L사에서 근무해 본 적은 없지만, LCE에 입사한 연구원 중 몇몇은 지부 출신이라고 하더구료.\n그들이 겪었다는 온갖 기이한 이야기를 듣고 있노라면, …으음. 만감이 교차하는 기분이 든다 하겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=smalltalk_10111_1].dlg
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I had not the experience of laboring for the former L Corp., yet I hear that some researchers employed here at LCE were employed there, once.\nThe bizarre tales of their employment are quite... Mm, they certainly do conjure all kinds of peculiar emotions.
   PL:
856. [Kwestia głosowa [smalltalk_10111_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=smalltalk_10111_2].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Kwestia głosowa [smalltalk_10111_2] (Chatter #2)] 아, 이 장비 말씀이신가. 이번에 새로이 E.G.O 추출을 진행한 결과요. 구 L사의 기록에서도 찾을 수 없었던 환상체의 추출이라 제법 난도가 있었지만… 보다시피 나쁘지 않은 성과를 냈소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=smalltalk_10111_2].dlg
   limit: do 420 znaków
   EN: Ah, you would like to know more of this gear? It is the product of our most recent E.G.O extraction efforts. There were some difficulties in the extraction process, given that this Abnormality was not once observed even within the records of former L Corp., but... as it is plain to see, we have yielded a rather promising result.
   PL:
858. [Kwestia głosowa [smalltalk_10111_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=smalltalk_10111_3].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Kwestia głosowa [smalltalk_10111_3] (Chatter #3)] 추출된 장비를 입고 있을 때 다소의 감정 동요가 발생하는 점은 아직 해결을 위한 연구중이오.\n다만… 나도 함정을 파두고 연구원들을 골려먹는 재미를 느끼게 되었다는 점에서, 그 연구는 조금 천천히 진행되도 좋지 않나 싶구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=smalltalk_10111_3].dlg
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The research to resolve the emergence of emotional instability when equipped with an extracted gear is currently underway.\nYet... given that I have acquired quite the taste for entrapping the fellow researchers in jokes of practical nature, perhaps this research need not take precedence over the others.
   PL:
860. [Kwestia głosowa [smalltalk_10111_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=smalltalk_10111_4].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Kwestia głosowa [smalltalk_10111_4] (Post-Uptie Chat 1)] …환상체의 탈출은 아무래도 제법 흔한 편이오. 구 L사처럼 환상체를 단순한 에너지 생산에만 쓰질 않으니, 어쩌면 그 때보다 더 심할지도 모르겠구료.\n그나마 뒤틀림 개체는 작게나마 인간으로 돌아올 여지가 있어서인지, 대화가 진행되어 감에 따라 안정되는 경향을 보이곤 하오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=smalltalk_10111_4].dlg
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ... Abnormality containment breaches are a rather commonplace occurrence here. It may perhaps be more frequent than it was at the former L Corp., given that the application for Abnormalities here is more for tasks rather than simple energy generation.\nDistortion subjects, however, may exhibit signs of calming upon engagement in dialogues. Perhaps this is an indicator that they may indeed be reverted to their human forms—no matter how slim the chance may be.
   PL:
862. [Kwestia głosowa [smalltalk_10111_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=smalltalk_10111_5].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Kwestia głosowa [smalltalk_10111_5] (Post-Uptie Chat 2)] 이 장비의 꼬리 같은 부분을 따라다니는 저 영체… 역시 환상체, 뒤틀림을 가리지 않고 대상을 '유인'하는 능력을 가진듯하구료.\n분명 본체는… 다른 것이지만, 저리 홀려대는 모습을 보면 흡사 저것이 진짜인 것만도 같소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=smalltalk_10111_5].dlg
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The apparition by the tail-like apparatus of this gear... Indeed, it appears to exhibit the ability to 'lure' the target, regardless of whether it is an Abnormality or a Distortion that they choose.\nThe core lies elsewhere, indubitably... yet, its bewitching form may lead one to the delusion that the apparition is, indeed, the core.
   PL:
864. [Kwestia głosowa [neglect_10111_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=neglect_10111_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Kwestia głosowa [neglect_10111_1] (Idle)] 눈이 마주친 김에 여기 앉으시게. 잠시 담소라도 나누지. …아. 이번엔 함정이 아니라, 진짜요.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=neglect_10111_1].dlg
   limit: do 180 znaków
   EN: Ah, this chance meeting is quite the fortunate one. Come, take a seat. ... Ah, worry not, for there is no trap waiting for you this time.
   PL:
866. [Kwestia głosowa [gacksung_10111_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=gacksung_10111_1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
867. [Kwestia głosowa [gacksung_10111_1] (Uptying)] 아, 나를 못 본 척 하고 있어주게. 곧 탈출한 환상체가 이쪽에 관심을 보이면… 내가 이 망치로 한 번에 제압할테니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=gacksung_10111_1].dlg
   limit: do 270 znaków
   EN: Ah, may I ask you to continue this pretense that you are yet to spy my location? The escaped Abnormality will soon find interest in me and approach... and I shall smite it with a single swing of this hammer.
   PL:
868. [Kwestia głosowa [formation_10111_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=formation_10111_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Kwestia głosowa [formation_10111_1] (Deployment)] 연구 보고회인가. 아니면… 탈출인가?
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=formation_10111_1].dlg
   limit: do 120 znaków
   EN: Is this a research briefing session, or... has there been a containment breach?
   PL:
870. [Kwestia głosowa [battleentry_10111_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battleentry_10111_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Kwestia głosowa [battleentry_10111_1] (Stage Entry)] 시험해 볼 기회구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battleentry_10111_1].dlg
   limit: do 120 znaków
   EN: A chance to test its merits.
   PL:
872. [Kwestia głosowa [battle_select_10111_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_select_10111_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
873. [Kwestia głosowa [battle_select_10111_1] (Viewed in Battle)] …예외처리하라는 말은 하지마시게…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_select_10111_1].dlg
   limit: do 120 znaków
   EN: … It would be deeply appreciated if the exclusion category were not to be necessitated here…
   PL:
874. [Kwestia głosowa [battle_endcommand_10111_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_endcommand_10111_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Kwestia głosowa [battle_endcommand_10111_1] (Commencing Attack)] 개체 제압.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_endcommand_10111_1].dlg
   limit: do 120 znaków
   EN: Subject suppressed.
   PL:
876. [Kwestia głosowa [battle_enemy_break_10111_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_enemy_break_10111_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [Kwestia głosowa [battle_enemy_break_10111_1] (Enemy Stagger)] 흠, 이 약점을 기록해두지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_enemy_break_10111_1].dlg
   limit: do 120 znaków
   EN: Hm. Thus I leave a recording of this weakness.
   PL:
878. [Kwestia głosowa [battle_break_10111_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_break_10111_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Kwestia głosowa [battle_break_10111_1] (Staggered)] 으윽…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_break_10111_1].dlg
   limit: do 120 znaków
   EN: Ngh...
   PL:
880. [Kwestia głosowa [battle_kill_10111_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_kill_10111_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [Kwestia głosowa [battle_kill_10111_1] (Enemy Killed)] 제압 완료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_kill_10111_1].dlg
   limit: do 120 znaków
   EN: Suppression complete.
   PL:
882. [Kwestia głosowa [battle_dead_10111_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_dead_10111_1].desc
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [Kwestia głosowa [battle_dead_10111_1] (Death)] 하아… 아직, 세상엔… 궁금한 것이…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_dead_10111_1].dlg
   limit: do 120 znaków
   EN: Haah... yet... there is so much of the unknown... in this world... to be learned...
   PL:
884. [Kwestia głosowa [choice_success_p_10111_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=choice_success_p_10111_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
885. [Kwestia głosowa [choice_success_p_10111_2] (Check Passed)] 명료한 해결책이 보였소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=choice_success_p_10111_2].dlg
   limit: do 120 znaków
   EN: A clear, crisp vision of a solution appeared before me.
   PL:
886. [Kwestia głosowa [choice_fail_n_10111_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=choice_fail_n_10111_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [Kwestia głosowa [choice_fail_n_10111_1] (Check Failed)] 이건 장기 연구 과제로 두는 것이…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=choice_fail_n_10111_1].dlg
   limit: do 120 znaków
   EN: Perchance this issue may be set aside as a long-term research goal...?
   PL:
888. [Kwestia głosowa [battle_clear_10111_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_clear_10111_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [Kwestia głosowa [battle_clear_10111_1] (Victory Cry)] 제압되었구료. 다만 좀 지체된 감이 있군… 보고서 제출 마감 기한까지 남은 시간이 제법 적소만… 아, 또 한 번 동료들에게 미끼를 던질 시기인가.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_clear_10111_1].dlg
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Thus completed is the suppression. Yet this effort has caused us quite the delay... We are not availed much time until the deadline for this report.\n... Ah, ha ha. Perhaps I must cast another lure to my fellow colleagues.
   PL:
890. [Kwestia głosowa [battle_clear_ex_10111_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_clear_ex_10111_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
891. [Kwestia głosowa [battle_clear_ex_10111_1] (Extra Conditions Fulfilled)] 훌륭한 성과라고 기록해야겠소. 장착한 장비와의 협응도 뛰어났고, 또… 음, 이곳엔 여백이 부족하여 다른 곳에 제대로 작성하지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_clear_ex_10111_1].dlg
   limit: do 300 znaków
   EN: Let the records state that this was a resounding success. Exceptional coordination with the equipment, and... Mm, this report must be completed elsewhere, for there isn't much room here to write the full chronicling of the events.
   PL:
892. [Kwestia głosowa [battle_defeat_10111_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_defeat_10111_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [Kwestia głosowa [battle_defeat_10111_1] (Defeat Wail)] 괜찮소. 실패라는 건 연구원에겐 그림자와 같이 따라붙는 것. 단 한 번의 성공을 할 수만 있다면 실패는 얼마든지 받아들일 수 있소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LCE_10111.json :: dataList[id=battle_defeat_10111_1].dlg
   limit: do 270 znaków
   EN: Worry not. To researchers, failure is like a shadow—one may not exist without it. Thus, all manner of failures are acceptable as long as they are used as building blocks to forge a path to a singular success.
   PL:

## [000] Liu Assoc. South Section 3 — Yi Sang — 남부 리우 협회 3과
- ID Tożsamości: `10112` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Burn

894. [Karta Tożsamości — tytuł] 남부 리우 협회\n3과
   źródło: Personalities.json :: dataList[id=10112].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Liu Assoc.\nSouth Section 3
   PL:
895. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10112].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
896. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10112].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
897. [Karta Tożsamości — opis] 이상의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10112].desc
   limit: do 120 znaków
   EN: Yi Sang's 12th Identity
   PL:
898. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 염참
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=1].name ; dataList[id=1011201].levelList[level=2].name ; dataList[id=1011201].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Flame Hew
   PL:
899. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 대상의 [Combustion] 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Coin Power +1
   PL:
900. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Inflict 1 [Combustion]
   PL:
901. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 900 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Combustion] <style="highlight">3</style> 이상이면, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has <style="highlight">3</style>+ [Combustion], Coin Power +1
   PL:
903. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL:
904. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 903 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Combustion] <style="highlight">3 당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n<style="highlight">대상의 [Combustion] 10 당, 피해량 +10% (최대 30%)</style>
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: <style="highlight">Coin Power +1 for every 3 [Combustion] on target (max 2)</style>\n<style="highlight">Deal +10% damage for every 10 [Combustion] on target (max 30%)</style>
   PL:
906. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 900 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 900 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 정면돌파
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=1].name ; dataList[id=1011202].levelList[level=2].name ; dataList[id=1011202].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Frontal Assault
   PL:
909. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 대상의 [Combustion] 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=1].desc
   (powtórzenie elementu 899 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL:
911. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1011202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 910 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, [Combustion] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], inflict +2 [Combustion] Count on target
   PL:
913. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] 대상의 [Combustion] 6 당, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=2].desc ; dataList[id=1011202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Coin Power +1 for every 6 [Combustion] on target (max 2)
   PL:
914. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] 대상의 [Combustion]당, 피해량 +2.5% (최대 30%)
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal +2.5% damage for every [Combustion] on target (max 30%)
   PL:
915. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, [Combustion] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1011202].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], inflict +2 [Combustion] Count on target<style="highlight"></style>
   PL:
916. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] 대상의 [Combustion]당, 피해량 +<style="highlight">5</style>% (최대  <style="highlight">60</style>%)
   źródło: Skills_personality-01.json :: dataList[id=1011202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal +<style="highlight">5</style>% damage for every [Combustion] on target (max <style="highlight">60</style>%)
   PL:
917. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 검의 흐름
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].name ; dataList[id=1011203].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Flow of the Sword
   PL:
918. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Combustion] 6 이상이면, 코인 위력 +1\n대상의 [Combustion] 6 당, 피해량 +10% (최대 30%)\n[EndSkill] 자신을 제외한 정신력이 가장 낮은 아군 1명 정신력 10 회복\n- 공격 대상을 처치했거나 공격 대상의 [Combustion]이 10 이상이면, 인원 1명 추가
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If target has 6+ [Combustion], Coin Power +1\nDeal +10% damage for every 6 [Combustion] on target (max 30%)\n[EndSkill] Heal 10 SP for 1 other ally that has the lowest SP\n- If this attack killed the target, or if target had 10+ [Combustion], heal 1 more ally
   PL:
919. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1011203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 903 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
920. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1011203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 903 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
921. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1011203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 910 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] 대상의 [Combustion]당, 피해량 +2% (최대 60%)
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1011203].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Deal +2% damage for every [Combustion] on target (max 60%)
   PL:
923. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion] 위력만큼 분노 속성 피해를 줌 (최대 30). 대상의 [Combustion] 횟수 2 감소
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1011203].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Deal Wrath damage equal to [Combustion] Potency on target (max 30). Reduce target's [Combustion] Count by 2
   PL:
924. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Combustion] 6 <style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n대상의 [Combustion] 6 당, 피해량 +10% (최대 30%)\n[EndSkill] 자신을 제외한 정신력이 가장 낮은 아군 1명 정신력 <style="highlight">15</style> 회복\n- 공격 대상을 처치했거나 공격 대상의 [Combustion]이 10 이상이면, 인원 1명 추가
   źródło: Skills_personality-01.json :: dataList[id=1011203].levelList[level=4].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">Coin Power +1 for every 6 [Combustion] on target (max 2)</style>\nDeal +10% damage for every 6 [Combustion] on target (max 30%)\n[EndSkill] Heal <style="highlight">15</style> SP for 1 other ally that has the lowest SP\n- If this attack killed the target, or if target had 10+ [Combustion], heal 1 more ally
   PL:
925. [Obrona (ulepszenia 1,4) — nazwa] 염반
   źródło: Skills_personality-01.json :: dataList[id=1011204].levelList[level=1].name ; dataList[id=1011204].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Flame Counter
   PL:
926. [Obrona (ulepszenie 1) — opis] [BeforeHit] 대상의 [Combustion]만큼 보호막을 얻음 (최대 10, 턴 당 1회)
   źródło: Skills_personality-01.json :: dataList[id=1011204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeHit], [Combustion]
   znaczenie tagów: [BeforeHit] = [피격 직전] / [Before Getting Hit]; [Combustion] = 화상 / Burn
   EN: [BeforeHit] Gain Shield equal to [Combustion] on target (max 10, once per turn)
   PL:
927. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여\n- 자신에게 보호막이 있으면, [Combustion] 1 추가 부여
   źródło: Skills_personality-01.json :: dataList[id=1011204].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Inflict 1 [Combustion]\n- If this unit has Shield, inflict 1 additional [Combustion]
   PL:
928. [Obrona (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여\n- 자신에게 보호막이 있으면, [Combustion] 1 추가 부여
   źródło: Skills_personality-01.json :: dataList[id=1011204].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1011204].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 927 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
929. [Obrona (ulepszenie 4) — opis] [BeforeHit] 대상의 [Combustion]만큼 보호막을 얻음 (최대 15, 턴 당 1회)\n[WhenUse] 대상의 [Combustion]이 10 이상이면, 피해량 +10%
   źródło: Skills_personality-01.json :: dataList[id=1011204].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeHit], [Combustion], [WhenUse]
   znaczenie tagów: [BeforeHit] = [피격 직전] / [Before Getting Hit]; [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]
   EN: [BeforeHit] Gain Shield equal to [Combustion] on target (max 15, once per turn)\n[WhenUse] If target has 10+ [Combustion], deal +10% damage
   PL:
930. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — nazwa] 내면의 열혈
   źródło: Passives.json :: dataList[id=1011201].name
   limit: do 40 znaków
   EN: Inner Ardor
   PL:
931. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — opis] 턴 종료 시 현재 정신력이 가장 낮은 아군 1명의 정신력을 5 + (최대 공명 수)만큼 회복시킴. (최대 10) (자신 또는 패닉, E.G.O 침식 상태인 아군 제외)\n- 회복 대상이 [Combustion] 위력이나 횟수를 부여하는 기본 스킬을 보유하고 있으면, 정신력 5 추가 회복
   źródło: Passives.json :: dataList[id=1011201].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Turn End: Heal 1 ally that has the lowest SP by (5 + highest Reson.) (max 10) (excludes: self and Panicked or E.G.O Corroded allies)\n- If the said ally has Base Skills that inflict [Combustion] Potency or Count, heal 5 additional SP to them
   PL:
932. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Wrath) — nazwa] 내면의 열혈
   źródło: Passives.json :: dataList[id=1011211].name
   (powtórzenie elementu 930 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
933. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Wrath) — opis] 턴 종료 시 현재 정신력이 가장 낮은 아군 1명의 정신력을 5 + (최대 공명 수)만큼 회복시킴. (최대 10) (자신 또는 패닉, E.G.O 침식 상태인 아군 제외)\n- 회복 대상이 [Combustion] 위력이나 횟수를 부여하는 기본 스킬을 보유하고 있으면, 정신력 5 추가 회복\n- 분노 공명 4 이상이면, 회복 대상 1명 추가
   źródło: Passives.json :: dataList[id=1011211].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Turn End: Heal 1 ally that has the lowest SP by (5 + highest Reson.) (max 10) (excludes: self and Panicked or E.G.O Corroded allies)\n- If the said ally has Base Skills that inflict [Combustion] Potency or Count, heal 5 additional SP to them\n- At 4+ Wrath Reson., heal 1 additional ally
   PL:
934. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 리우 방진
   źródło: Passives.json :: dataList[id=1011221].name
   limit: do 40 znaków
   EN: Liu Defensive Square
   PL:
935. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 정신력이 가장 낮은 아군 2명이 이번 턴에 정신력이 감소한 경우 턴 종료 시 정신력 5 회복
   źródło: Passives.json :: dataList[id=1011221].desc
   limit: do 120 znaków
   EN: For 2 allies that have the lowest SP: If they lost SP this turn, heal 5 SP at Turn End
   PL:
936. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Wrath) — nazwa] 리우 방진
   źródło: Passives.json :: dataList[id=1011231].name
   (powtórzenie elementu 934 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
937. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Wrath) — opis] 정신력이 가장 낮은 아군 2명이 이번 턴에 정신력이 감소한 경우 턴 종료 시 정신력 5 회복\n- 회복 대상이 [Combustion] 위력이나 횟수를 부여하는 기본 스킬을 보유하고 있으면, 대신 5 - 10 회복
   źródło: Passives.json :: dataList[id=1011231].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: For 2 allies that have the lowest SP: If they lost SP this turn, heal 5 SP at Turn End\n- If the said allies have Base Skills that inflict [Combustion] Potency or Count, heal 5~10 SP instead
   PL:
938. [Kwestia głosowa [get_10112_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=get_10112_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
939. [Kwestia głosowa [get_10112_1] (Identity Acquisition)] 여전히도, 참으로 북적스런 공간이 아닐 수 없구료…\n하아, 동료들은 어찌 나를 방 안에 내버려두질 않는 것인지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=get_10112_1].dlg
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Such bustle and busyness this place harbors... Haah, why is it that my fellows find it to be of great difficulty to leave me be in my room?
   PL:
940. [Kwestia głosowa [lobby_morning_10112_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=lobby_morning_10112_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
941. [Kwestia głosowa [lobby_morning_10112_1] (Morning Greeting)] 이리 일찍 일어나는 사람들이 거리에 즐비하다니, 다들 부지런히도 사시는구료.\n흠… 비록 인위적으로 만들어진 맑은 하늘이라 하여도, 서관에만 박혀 있다가 나와보니 퍽 생경하기는 하오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=lobby_morning_10112_1].dlg
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To walk the streets and find so many pedestrians at such an early hour... quite the busy lives they must lead.\nHm... though the blue sky under which I amble is but a facsimile, to behold it after long hours in the archives makes it a rather... unfamiliar activity.
   PL:
942. [Kwestia głosowa [lobby_noon_10112_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=lobby_noon_10112_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
943. [Kwestia głosowa [lobby_noon_10112_1] (Afternoon Greeting)] 낮에는… 간단한 식사와 협회 동료의 안부를 묻곤 하오. 다만, 우리 협회의 사람들은 대화의 흐름이 끼어들기 힘들만큼 불타오르는지라, …음. 익숙해지기 위해 노력하고 있소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=lobby_noon_10112_1].dlg
   limit: do 310 znaków
   EN: At noon... I partake in a simple meal and ask how my Association fellows are faring. Yet the flow of their dialogue oft burns too rapidly for me to find the room to utter a word, it is... mm. It is my intent to familiarize myself further.
   PL:
944. [Kwestia głosowa [lobby_night_10112_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=lobby_night_10112_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [Kwestia głosowa [lobby_night_10112_1] (Evening Greeting)] 야간 정도는 훈련장에서 습득한 정보를 직접 시험해보는 것이 좋을 것이오. 눈으로 읽어내린 활자만으론 리우의 기술을 체화하긴 어려운 법이니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=lobby_night_10112_1].dlg
   limit: do 230 znaków
   EN: At night, information obtained from the training grounds should be put to the test. Merely reading the texts is but a poor method by which one may learn the techniques of the Liu.
   PL:
946. [Kwestia głosowa [smalltalk_10112_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=smalltalk_10112_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
947. [Kwestia głosowa [smalltalk_10112_1] (Chatter #1)] 3과에 오르고 협회의 서관에 있는 책자를 벌써 세 번은 돌려읽은 것 같소만… 흠… 다른 과의 책이 있다면 마치 책장을 들춰본 적도 없던 것처럼 깨끗하고 티나지 않게 읽고 돌려줄 수도 있겠소만… 크흠, 아니. 잊으시오…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=smalltalk_10112_1].dlg
   limit: do 370 znaków
   EN: Since I made the ascent the third Section, Thrice have I perused the books of the Association's archives. Were I to be granted volumes of other Sections, I may return them there following my perusal, pristine as though they had not once been removed from their rightful... Ahem. Worry not.
   PL:
948. [Kwestia głosowa [smalltalk_10112_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=smalltalk_10112_2].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
949. [Kwestia głosowa [smalltalk_10112_2] (Chatter #2)] 아무래도 줄곧 권(拳)과 각(脚)을 써오다보니 지금처럼 검을 쓰는 건 다소 신선하오. 지금 생각해보니 4과에서 지내며 배운 수도(手刀)가 이 과정을 익숙하게 하기 위한 발판은 아니었나 생각이 드는구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=smalltalk_10112_2].dlg
   limit: do 330 znaków
   EN: The sword feels quite unfamiliar in my hand, as thus far I have primarily utilized punches(拳) and kicks(脚) as the means of battle. Knifehand(手刀) techniques learned in Section 4 may have been instrumental steps to familiarize oneself with the blade, one thinks.
   PL:
950. [Kwestia głosowa [smalltalk_10112_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=smalltalk_10112_3].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
951. [Kwestia głosowa [smalltalk_10112_3] (Chatter #3)] 흠… 동부로 파견될 것 같은데, 이 참에 그 곳의 훈련이나 전투방식을 배워보는 것도 흥미롭겠소.\n…아, 협회의 동료들에게는 비밀로 해주겠소? 그들은 어째 상처를 받을 것만 같아서…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=smalltalk_10112_3].dlg
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hm... it seems that my dispatch would find me eastward; perhaps this should be an opportune time to learn of their training methods and combat techniques.\nAh, please, do not speak of this to my Association fellows. I prefer not to hurt their feelings, be it not my intention or otherwise.
   PL:
952. [Kwestia głosowa [smalltalk_10112_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=smalltalk_10112_4].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
953. [Kwestia głosowa [smalltalk_10112_4] (Post-Uptie Chat 1)] 검격으로 공간을 불사르는 것을 통해 대규모의 적들을 상대한다라… 직접 해보기 전만 해도, 검술이란 단일의 상대에나 효과가 있을 거라고 생각했는데 다소 미숙한 발상이었군.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=smalltalk_10112_4].dlg
   limit: do 270 znaków
   EN: To put a crowd of enemies at bay by setting alight the air with the sword... Much doubt did I have in the abilities of the sword beyond dueling a single enemy; clearly, my thoughts were yet to have matured then.
   PL:
954. [Kwestia głosowa [smalltalk_10112_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=smalltalk_10112_5].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
955. [Kwestia głosowa [smalltalk_10112_5] (Post-Uptie Chat 2)] 기왕 전선에 설 것이라면 선두에. 최전선이 좋겠소. 새로이 배운 기술을 활용할 기회도 늘 것이요, 불씨를 틔워놓는다면 뒤이어 따라 올 동료들의 전투 또한 수월할테지.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=smalltalk_10112_5].dlg
   limit: do 320 znaków
   EN: It would be best to be in the vanguard, should I find myself on a battlefield. There, I shall have opportunities aplenty to make use of the techniques I have learned; I could be of great assistance to those who follow as I set the embers alight.
   PL:
956. [Kwestia głosowa [neglect_10112_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=neglect_10112_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [Kwestia głosowa [neglect_10112_1] (Idle)] 으음… 이것이 리우 남부 3과 검법의 초식인가. 다른 지부의 무구와 초식들도 궁금해지는구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=neglect_10112_1].dlg
   limit: do 180 znaków
   EN: Hm... so these are the fundamental forms of Liu South Section 3. I wonder what the weapons and forms of other branches have to offer?
   PL:
958. [Kwestia głosowa [gacksung_10112_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=gacksung_10112_1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
959. [Kwestia głosowa [gacksung_10112_1] (Uptying)] 북적한 공간에 소음이 끼는 것은 유쾌하지 못한 일이오.\n차라리 이 참에 한적하게 만들어 보이리다.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=gacksung_10112_1].dlg
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It is unpleasant business to have noise compounded with bustle; I shall bring calm and silence to my presence.
   PL:
960. [Kwestia głosowa [formation_10112_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=formation_10112_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
961. [Kwestia głosowa [formation_10112_1] (Deployment)] 시험해 볼 기회구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=formation_10112_1].dlg
   limit: do 120 znaków
   EN: An opportunity to test my sword.
   PL:
962. [Kwestia głosowa [battleentry_10112_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battleentry_10112_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
963. [Kwestia głosowa [battleentry_10112_1] (Stage Entry)] 불꽃을 벼리겠소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battleentry_10112_1].dlg
   limit: do 120 znaków
   EN: To forge the flame itself.
   PL:
964. [Kwestia głosowa [battle_select_10112_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_select_10112_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
965. [Kwestia głosowa [battle_select_10112_1] (Viewed in Battle)] 아, 잔불에 주의하시오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_select_10112_1].dlg
   limit: do 120 znaków
   EN: Ah, be wary of the embers.
   PL:
966. [Kwestia głosowa [battle_endcommand_10112_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_endcommand_10112_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
967. [Kwestia głosowa [battle_endcommand_10112_1] (Commencing Attack)] 화격검.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_endcommand_10112_1].dlg
   limit: do 120 znaków
   EN: Flamestrike sword.
   PL:
968. [Kwestia głosowa [battle_enemy_break_10112_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_enemy_break_10112_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
969. [Kwestia głosowa [battle_enemy_break_10112_1] (Enemy Stagger)] 흐드러지게.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_enemy_break_10112_1].dlg
   limit: do 120 znaków
   EN: Cremation...
   PL:
970. [Kwestia głosowa [battle_break_10112_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_break_10112_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
971. [Kwestia głosowa [battle_break_10112_1] (Staggered)] 음…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_break_10112_1].dlg
   (powtórzenie elementu 793 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
972. [Kwestia głosowa [battle_kill_10112_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_kill_10112_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
973. [Kwestia głosowa [battle_kill_10112_1] (Enemy Killed)] 타오르시게.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_kill_10112_1].dlg
   limit: do 120 znaków
   EN: ... like a blossom.
   PL:
974. [Kwestia głosowa [battle_dead_10112_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_dead_10112_1].desc
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
975. [Kwestia głosowa [battle_dead_10112_1] (Death)] 더 배우지 못하고 가는 것이… 그저… 못마땅, 하군…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_dead_10112_1].dlg
   limit: do 130 znaków
   EN: What a shame it is... that I... must depart this world... with the void of knowledge... so vast...
   PL:
976. [Kwestia głosowa [choice_success_p_10112_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=choice_success_p_10112_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
977. [Kwestia głosowa [choice_success_p_10112_2] (Check Passed)] 이것이 옳은 점화식이었소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=choice_success_p_10112_2].dlg
   limit: do 120 znaków
   EN: Thus reignited was the spark of resolution to this riddle.
   PL:
978. [Kwestia głosowa [choice_fail_n_10112_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=choice_fail_n_10112_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
979. [Kwestia głosowa [choice_fail_n_10112_1] (Check Failed)] 으음, 분명 쓸데없는 것이었을테요…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=choice_fail_n_10112_1].dlg
   limit: do 120 znaków
   EN: Mm. This task must not have been of any critical significance...
   PL:
980. [Kwestia głosowa [battle_clear_10112_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_clear_10112_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
981. [Kwestia głosowa [battle_clear_10112_1] (Victory Cry)] 해봄직한 일을 그럴듯하게 풀어냈소. 단지, 새로이 불씨를 틔워볼 기회가 적어서 아쉽기는 하구료.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_clear_10112_1].dlg
   limit: do 190 znaków
   EN: A manageable task, handled in the most practicable fashion. Yet, it is regrettable that it did not allow for much chance to spark new flames.
   PL:
982. [Kwestia głosowa [battle_clear_ex_10112_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_clear_ex_10112_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
983. [Kwestia głosowa [battle_clear_ex_10112_1] (Extra Conditions Fulfilled)] 앞에 나선 보람이 있었구료. 그 어느 때보다 뜨겁게 타올랐소. 이 검법도 제법 손에 익은 듯 하오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_clear_ex_10112_1].dlg
   limit: do 210 znaków
   EN: I regret not, the choice of taking the forefront of the assault; I have burned hotter than I ever have. This blade-form feels more familiar in the hand as well.
   PL:
984. [Kwestia głosowa [battle_defeat_10112_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_defeat_10112_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
985. [Kwestia głosowa [battle_defeat_10112_1] (Defeat Wail)] 아… 최근엔 너무 활자에만 기대었던가. 훈련의 양을 늘리는 것이 좋겠소. 이러다간 2과는 커녕, 다른 지역에 파견도 꿈꾸기 어려울테니…
   źródło: PersonalityVoiceDlg/Voice_Yisang_LiuAssoc_10112.json :: dataList[id=battle_defeat_10112_1].dlg
   limit: do 270 znaków
   EN: Ah... an overreliance on text over practice, is it? I must expand my trainings. Should such failures continue, I shan't be selected for dispatches to different regions, let alone claim promotion to Section 2...
   PL:

## [000] N Corp. E.G.O:: Fell Bullet — Yi Sang — N사 E.G.O:: 흉탄
- ID Tożsamości: `10113` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Poise

986. [Karta Tożsamości — tytuł] N사 E.G.O::\n흉탄
   źródło: Personalities.json :: dataList[id=10113].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: N Corp. E.G.O::\nFell Bullet
   PL:
987. [Karta Tożsamości — nazwa] 이상
   źródło: Personalities.json :: dataList[id=10113].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
988. [Karta Tożsamości — nazwa z tytułem] 이상
   źródło: Personalities.json :: dataList[id=10113].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
989. [Karta Tożsamości — opis] 이상의 열세번째 인격
   źródło: Personalities.json :: dataList[id=10113].desc
   limit: do 120 znaków
   EN: Yi Sang's 13th Identity
   PL:
990. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 헛점 파악
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=1].name ; dataList[id=1011301].levelList[level=2].name ; dataList[id=1011301].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: See Through Defenses
   PL:
991. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 자신의 [BoseProjektil]당 피해량 +7% (최대 49%)\n[WhenUse] [BoseProjektil] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [BoseProjektil], [WhenUse]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]
   EN: Deal +7% damage for every [BoseProjektil] on self (max 49%)\n[WhenUse] Gain 1 [BoseProjektil]
   PL:
992. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL:
993. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 자신의 [BoseProjektil]당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">70</style>%)\n<style="highlight">[WhenUse] 자신의 [Breath]이 5 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 이상이면, 기본 위력 +1</style>\n[WhenUse] <style="highlight">자신의 [Breath] 횟수 1 증가,</style> [BoseProjektil] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=2].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BoseProjektil], [WhenUse], [Breath]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Deal +<style="highlight">10</style>% damage for every [BoseProjektil] on self (max <style="highlight">70</style>%)\n<style="highlight">[WhenUse] At 5+ [Breath], Coin Power +1\n[WhenUse] At 3+ [Breath] Count, Base Power +1 </style>\n[WhenUse] Gain <style="highlight">+1 [Breath] Count and</style> 1 [BoseProjektil]
   PL:
994. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count<style="highlight"></style>
   PL:
995. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttackHead] [Laceration] 횟수 1 증가</style>
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttackHead], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttackHead] = [크리티컬 앞면 적중 시] / [On Crit - Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[CriticalOnSucceedAttackHead] Inflict +1 [Laceration] Count</style>
   PL:
996. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 3 — opis] <style="highlight">[CriticalOnSucceedAttackHead] [BoseProjektil] 1 얻음</style>
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=2].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttackHead], [BoseProjektil]
   znaczenie tagów: [CriticalOnSucceedAttackHead] = [크리티컬 앞면 적중 시] / [On Crit - Heads Hit]; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: <style="highlight">[CriticalOnSucceedAttackHead] Gain 1 [BoseProjektil]</style>
   PL:
997. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 [BoseProjektil]당 피해량 +<style="highlight">15</style>% (최대 <style="highlight">105</style>%)\n[WhenUse] 자신의 [Breath] 5 <style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 3 <style="highlight">당</style>, 기본 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">2</style> 증가, [BoseProjektil] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=4].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BoseProjektil], [WhenUse], [Breath]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Deal +<style="highlight">15</style>% damage for every [BoseProjektil] on self (max <style="highlight">105</style>%)\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Breath] on self (max 2)</style>\n[WhenUse] <style="highlight">Base Power +1 for every 3 [Breath] Count on self (max 2)</style>\n[WhenUse] Gain +<style="highlight">2</style> [Breath] Count and 1 [BoseProjektil]
   PL:
998. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack]</style> [Laceration] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[CriticalOnSucceedAttack]</style> Inflict +1 [Laceration] Count
   PL:
999. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 3 — opis] <style="highlight">[CriticalOnSucceedAttack]</style> [BoseProjektil] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011301].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [BoseProjektil]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: <style="highlight">[CriticalOnSucceedAttack]</style> Gain 1 [BoseProjektil]
   PL:
1000. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 꿰뚫으리라
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].name ; dataList[id=1011302].levelList[level=2].name ; dataList[id=1011302].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Punch Through
   PL:
1001. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [BoseProjektil]당 피해량 +10% (최대 70%)\n[WhenUse] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BoseProjektil], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [Breath] = 호흡 / Poise
   EN: [WhenUse] Deal +10% damage for every [BoseProjektil] on self (max 70%)\n[WhenUse] Gain 2 [Breath]
   PL:
1002. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
1003. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 814 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1004. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 1002 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1005. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BoseProjektil] 1 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BoseProjektil]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: [OnSucceedAttack] Gain 1 [BoseProjektil]
   PL:
1006. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 4 — opis] [CriticalOnSucceedAttack] [BoseProjektil] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [BoseProjektil]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: [CriticalOnSucceedAttack] Gain 2 [BoseProjektil]
   PL:
1007. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 [BoseProjektil]당 피해량 +10% (최대 70%)\n<style="highlight">[WhenUse] 자신의 [Breath]이 5 이상이면, 코인 위력 +1</style>\n[WhenUse] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BoseProjektil], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [Breath] = 호흡 / Poise
   EN: [WhenUse] Deal +10% damage for every [BoseProjektil] on self (max 70%)\n<style="highlight">[WhenUse] At 5+ [Breath], Coin Power +1</style>\n[WhenUse] Gain 2 [Breath]
   PL:
1008. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1011302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]<style="highlight"></style>
   PL:
1009. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttackHead] [Laceration] 2 부여</style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttackHead], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttackHead] = [크리티컬 앞면 적중 시] / [On Crit - Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[CriticalOnSucceedAttackHead] Inflict 2 [Laceration]</style>
   PL:
1010. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1011302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL:
1011. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1011302].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 1008 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1012. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BoseProjektil] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#1].coindescs[#2].desc ; dataList[id=1011302].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BoseProjektil]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: [OnSucceedAttack] Gain 1 [BoseProjektil]<style="highlight"></style>
   PL:
1013. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 4 — opis] <style="highlight">[CriticalOnSucceedAttack] [Laceration] 1 부여</style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict 1 [Laceration]</style>
   PL:
1014. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 5 — opis] [CriticalOnSucceedAttack] [BoseProjektil] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=2].coinlist[#1].coindescs[#4].desc ; dataList[id=1011302].levelList[level=4].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [BoseProjektil]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: [CriticalOnSucceedAttack] Gain 2 [BoseProjektil]<style="highlight"></style>
   PL:
1015. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 [BoseProjektil]당 피해량 +<style="highlight">15</style>% (최대 <style="highlight">105</style>%)\n[WhenUse] 자신의 [Breath] 5 <style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BoseProjektil], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [Breath] = 호흡 / Poise
   EN: [WhenUse] Deal +<style="highlight">15</style>% damage for every [BoseProjektil] on self (max <style="highlight">105</style>%)\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Breath] on self (max 2)</style>\n[WhenUse] Gain 2 [Breath]
   PL:
1016. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack]</style> [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[CriticalOnSucceedAttack]</style> Inflict 2 [Laceration]<style="highlight"></style>
   PL:
1017. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 4 — opis] [CriticalOnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011302].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict <style="highlight">2</style> [Laceration]
   PL:
1018. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 대상 조정 사격
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].name ; dataList[id=1011303].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 2 (+7)
   limit: do 40 znaków
   EN: Target Readjustment Fire
   PL:
1019. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] 체력이 가장 낮은 대상 우선 공격\n- 자신의 [BoseProjektil]이 7이면, 메인 타겟을 아군 우선 지정\n[StartBattle] 자신의 [BoseProjektil] 3당, 공격 가중치 +1 (최대 2)\n[WhenUse] 자신의 [Breath]이 5 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [BoseProjektil]당, [Breath] 1 얻음 (최대 7)\n[EndSkill] 자신의 ([BoseProjektil] X 2) 만큼 정신력 감소 (최대 14 감소)\n[EndSkill] 전투 시작 시 자신의 [BoseProjektil]이 7이면, 전부 소모\n- 전부 소모했고 아군이 사망했으면, 자신의 정신력 20 회복
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [BoseProjektil], [WhenUse], [Breath], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [StartBattle] Targets the unit that has the lowest HP\n- At 7 [BoseProjektil], primarily targets among allies as the main target\n[StartBattle] Gain +1 Atk Weight for every 3 [BoseProjektil] on self (max 2)\n[WhenUse] At 5+ [Breath], Coin Power +1\n[WhenUse] At 3+ [Breath] Count, Base Power +1\n[WhenUse] Gain 1 [Breath] for every [BoseProjektil] on self (max 7)\n[EndSkill] Lose ([BoseProjektil] on self x 2) SP (max 14)\n[EndSkill] If this unit has 7 [BoseProjektil] at Combat Start, lose them all\n- If this unit lost all [BoseProjektil], and if an ally is killed, heal 20 SP on self
   PL:
1020. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1011303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 814 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1021. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] 이 코인에는 메인 타겟만 피해를 입음
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1011303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin deals damage only against the main target
   PL:
1022. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 3 — opis] 메인 타겟이 아군이면, 아래 효과가 적용됨\n- 이 공격에 한해 관통 속성 내성을 취약으로 변경함
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=1011303].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If the main target is an ally, activate the following effects:\n- The main target's Pierce Resistance becomes Fatal against this attack
   PL:
1023. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 4 — opis] - 자신의 [BoseProjektil]당 피해량 +5% (최대 35%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: - Deal +5% damage for every [BoseProjektil] on self (max 35%)
   PL:
1024. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 5 — opis] - 자신의 [Breath]당 크리티컬 피해량 +2% (최대 40%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: - +2% Damage on Critical Hit for every [Breath] on self (max 40%)
   PL:
1025. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 814 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1026. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] 이 코인에는 서브 타겟만 피해를 입음
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin deals damage only against the sub-targets
   PL:
1027. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 3 — opis] - 메인 타겟이 적이였을 경우, 메인 타겟에게 피해를 입힘
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   EN: - However, if the main target was an enemy, deal damage against the main target
   PL:
1028. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 4 — opis] - 첫번째 코인에서 아군을 처치하지 못했으면, 서브 타겟 중 무작위 1명이 피해를 입음
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#3].desc ; dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If the first Coin failed to kill an ally, 1 random sub-target takes damage
   PL:
1029. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 5 — opis] 자신의 [BoseProjektil]당, 피해량 +15% (최대 105%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: Deal +15% damage for every [BoseProjektil] on self (max 105%)
   PL:
1030. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 6 — opis] - 첫번째 코인에서 아군을 처치했으면, 대신하여 자신의 [BoseProjektil]당 피해량 +30% (최대 210%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#5].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: - If the first Coin killed an ally, deal +30% damage for every [BoseProjektil] on self instead (max 210%)
   PL:
1031. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 7 — opis] [Breath] 위력당, 크리티컬 피해량 +2.5% (최대 25%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#6].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: +2.5% Damage on Critical Hit for every [Breath] Potency (max 25%)
   PL:
1032. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 8 — opis] 자신의 [BoseProjektil]당, 크리티컬 피해량 +7% (최대 49%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#7].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: +7% Damage on Critical Hit for every [BoseProjektil] on self (max 49%)
   PL:
1033. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 9 — opis] 첫번째 코인으로 메인 타겟에게 가한 피해 비율(최대 체력 기준)만큼 피해량이 증가 (최대 100%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#8].desc ; dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#8].desc
   limit: do 120 znaków
   EN: Deal +(HP percentage the first Coin removed from the main target)% damage (max 100%)
   PL:
1034. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 10 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#9].desc
   (powtórzenie elementu 627 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1035. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 11 — opis] - 첫번째 코인에서 아군을 처치했으면, 대신하여 [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=3].coinlist[#1].coindescs[#10].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: - If the first Coin killed an ally, inflict 3 [Laceration] and +1 [Laceration] Count instead
   PL:
1036. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [StartBattle] 체력이 가장 낮은 대상 우선 공격\n- 자신의 [BoseProjektil]이 7이면, 메인 타겟을 아군 우선 지정\n[StartBattle] 자신의 [BoseProjektil] 3당, 공격 가중치 +1 (최대 2)\n[WhenUse] 자신의 [Breath] 5 <style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 3 <style="highlight">당</style>, 기본 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [BoseProjektil]당, [Breath] 1 얻음 (최대 7)\n[EndSkill] 자신의 ([BoseProjektil] X 2) 만큼 정신력 감소 (최대 14 감소)\n[EndSkill] 전투 시작 시 자신의 [BoseProjektil]이 7이면, 전부 소모\n- 전부 소모했고 아군이 사망했으면, 자신의 정신력 20 회복
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [BoseProjektil], [WhenUse], [Breath], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [StartBattle] Targets the unit that has the lowest HP\n- At 7 [BoseProjektil], primarily targets among allies as the main target\n[StartBattle] Gain +1 Atk Weight for every 3 [BoseProjektil] on self (max 2)\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Breath] on self (max 2)</style>\n[WhenUse] <style="highlight">Base Power +1 for every 3 [Breath] Count on self (max 2)</style>\n[WhenUse] Gain 1 [Breath] for every [BoseProjektil] on self (max 7)\n[EndSkill] Lose ([BoseProjektil] on self x 2) SP (max 14)\n[EndSkill] If this unit has 7 [BoseProjektil] at Combat Start, lose them all\n- If this unit lost all [BoseProjektil], and if an ally is killed, heal 20 SP on self
   PL:
1037. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] - 자신의 [BoseProjektil]당 피해량 +7% (최대 49%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: - Deal +7% damage for every [BoseProjektil] on self (max 49%)
   PL:
1038. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 5 — opis] - 자신의 [Breath]당 크리티컬 피해량 +3% (최대 60%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: - +3% Damage on Critical Hit for every [Breath] on self (max 60%)
   PL:
1039. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 5 — opis] 자신의 [BoseProjektil]당, 피해량 +<style="highlight">20</style>% (최대 <style="highlight">140</style>%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: Deal +<style="highlight">20</style>% damage for every [BoseProjektil] on self (max <style="highlight">140</style>%)
   PL:
1040. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 6 — opis] - 첫번째 코인에서 아군을 처치했으면, 대신하여 자신의 [BoseProjektil]당 피해량 +<style="highlight">40</style>% (최대 <style="highlight">280</style>%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#5].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: - If the first Coin killed an ally, deal +<style="highlight">40</style>% damage for every [BoseProjektil] on self instead (max <style="highlight">280</style>%)
   PL:
1041. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 7 — opis] [Breath] 위력당, 크리티컬 피해량 +<style="highlight">5</style>% (최대 <style="highlight">50</style>%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#6].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: +<style="highlight">5</style>% Damage on Critical Hit for every [Breath] Potency (max <style="highlight">50</style>%)
   PL:
1042. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 8 — opis] 자신의 [BoseProjektil]당, 크리티컬 피해량 +<style="highlight">10</style>% (최대 <style="highlight">70</style>%)
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#7].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: +<style="highlight">10</style>% Damage on Critical Hit for every [BoseProjektil] on self (max <style="highlight">70</style>%)
   PL:
1043. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 10 — opis] [OnSucceedAttack] [Laceration] <style="highlight">3</style> 부여
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#9].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Laceration]
   PL:
1044. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 11 — opis] - 첫번째 코인에서 아군을 처치했으면, 대신하여 [Laceration] <style="highlight">5</style> 부여, [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-01.json :: dataList[id=1011303].levelList[level=4].coinlist[#1].coindescs[#10].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: - If the first Coin killed an ally, inflict <style="highlight">5</style> [Laceration] and +<style="highlight">2</style> [Laceration] Count instead
   PL:
1045. [Obrona (ulepszenia 1,4) — nazwa] 전방 지원
   źródło: Skills_personality-01.json :: dataList[id=1011304].levelList[level=1].name ; dataList[id=1011304].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 5 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Front Line Support
   PL:
1046. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 자신의 [Breath] 2 당, 코인 위력 +1 (최대 2)\n[WhenUse] [BoseProjektil] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011304].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Breath], [BoseProjektil]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: [DuelCounter]\n[WhenUse] Coin Power +1 for every 2 [Breath] on self (max 2)\n[WhenUse] Gain 2 [BoseProjektil]
   PL:
1047. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011304].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1011304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1002 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1048. [Obrona (ulepszenia 1,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-01.json :: dataList[id=1011304].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1011304].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL:
1049. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[WhenUse] 자신의 [Breath] 2 당, 코인 위력 +1 (최대 3)\n[WhenUse] [BoseProjektil] 2 얻음
   źródło: Skills_personality-01.json :: dataList[id=1011304].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Breath], [BoseProjektil]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: [DuelCounter]\n[WhenUse] Coin Power +1 for every 2 [Breath] on self (max 3)\n[WhenUse] Gain 2 [BoseProjektil]
   PL:
1050. [Pasywka bojowa (od ulepszenia 1) — nazwa] 휘발된 추억
   źródło: Passives.json :: dataList[id=1011302].name
   limit: do 40 znaków
   EN: Volatilized Memory
   PL:
1051. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 종료 시 자신의 [BoseProjektil]을 전부 제거하고 다음 턴에 제거한 수치만큼 [BoseProjektil]을 얻음
   źródło: Passives.json :: dataList[id=1011302].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: Turn End: Lose all [BoseProjektil] on self. Next turn, gain [BoseProjektil] equal to the amount lost
   PL:
1052. [Pasywka bojowa (od ulepszenia 2, posiadane 6× Pride) — nazwa] 흉탄
   źródło: Passives.json :: dataList[id=1011301].name
   limit: do 40 znaków
   EN: Fell Bullet
   PL:
1053. [Pasywka bojowa (od ulepszenia 2, posiadane 6× Pride) — opis] 전투 중 자신의 공격으로 아군을 사망시켰으면, 다음 턴동안 [FellBulletPersonality]을 얻음 (자신의 E.G.O 침식 및 아군 공격 포함)\n자신의 E.G.O 흉탄을 사용하여, [BoseProjektil]이 소모되면, 턴 종료 시 소모한만큼 다음 턴에 [BoseProjektil]을 얻음
   źródło: Passives.json :: dataList[id=1011301].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [FellBulletPersonality], [BoseProjektil]
   znaczenie tagów: [FellBulletPersonality] = 흉탄 / Fell Bullet; [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: If this unit killed an allied unit using its attack, gain [FellBulletPersonality] for the next turn (including using this unit's 'E.G.O Corrosion' and attacks against allies)\nIf this unit uses its E.G.O 'Fell Bullet' and consumes [BoseProjektil]: Next turn, gain [BoseProjektil] equal to the amount of it consumed by the end of the last turn
   PL:
1054. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Pride) — nazwa] 대상 지정
   źródło: Passives.json :: dataList[id=1011321].name
   limit: do 40 znaków
   EN: Designate Target
   PL:
1055. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Pride) — opis] 속도가 가장 느린 아군이 아군을 공격했다면 공격 종료 시, 다음 턴에 [AttackDmgUp]를 1 얻음 (턴 당 최대 2)\n- 이 때, 아군이 사망했으면, 위 효과를 대신하여 이번 전투 동안 [AttackDmgUp]를 1 얻음 (스테이지 및 인격당 최대 2)\n- 위 효과들로 얻는 [AttackDmgUp]는 최대 2까지만 얻어짐.
   źródło: Passives.json :: dataList[id=1011321].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: When the ally with the slowest Speed attacked an ally, Attack End: Gain 1 [AttackDmgUp] next turn (2 times per turn)\n- If the attacked ally is killed by this attack, gain 1 [AttackDmgUp] for the whole Encounter instead (max 2 per Stage per Identity)\n- Can gain only up to 2 [AttackDmgUp] from the above effect
   PL:
1056. [Kwestia głosowa [get_10113_1] — sytuacja] 인격 획득
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=get_10113_1].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1057. [Kwestia głosowa [get_10113_1] (Identity Acquisition)] 친우의 피로 점철한 넝마를 보고 손가락질하는가. 어리석은 자들이로다. 지상 최고의 비극은 오직 나만이 통감할 수 있는 것을.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=get_10113_1].dlg
   limit: do 200 znaków
   EN: They would point and jeer at the rags splattered with the blood of fellowship. The fools; only I can grasp the highest degree of tragedy upon this earth.
   PL:
1058. [Kwestia głosowa [lobby_morning_10113_1] — sytuacja] 아침 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=lobby_morning_10113_1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1059. [Kwestia głosowa [lobby_morning_10113_1] (Morning Greeting)] 부상한 태양의 빛이 내게는 제법 따갑구료. 나는 오히려 달이 좋소. 반사되어 저감하는 빛이어야 내게 알맞소. 동료를 꿰어 탄환을 내보내는 나와 제법 어울리지 않는가.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=lobby_morning_10113_1].dlg
   limit: do 250 znaków
   EN: Rays of the risen sun prickle my skin. I prefer the moon, the light of which is but a reflection softened. Quite the fitting preference for me, who rains fire by striking my comrades, is it not?
   PL:
1060. [Kwestia głosowa [lobby_noon_10113_1] — sytuacja] 점심 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=lobby_noon_10113_1].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1061. [Kwestia głosowa [lobby_noon_10113_1] (Afternoon Greeting)] 점심 식사는 즐기지 않소. 잠시 거르는 것으로 크게 영향을 받지도 않을 뿐더러, 들러붙은 쩐득한 혈향이 제법 고약하기에.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=lobby_noon_10113_1].dlg
   limit: do 180 znaków
   EN: I do not partake in midday meals. Its absence does not affect me much, and the bloodsteeped scent, I must say, makes it rather unsavory.
   PL:
1062. [Kwestia głosowa [lobby_night_10113_1] — sytuacja] 저녁 인사
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=lobby_night_10113_1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1063. [Kwestia głosowa [lobby_night_10113_1] (Evening Greeting)] …들켰는가. 모른척 하고 지나가 주시게. 이사님이 내게 이고(E.G.O)의 연구를 허락하지 않아, 야음을 틈타 연구자료라도 뒤져보려는 셈이었으니.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=lobby_night_10113_1].dlg
   limit: do 290 znaków
   EN: ... Ah, you've seen me. Pretend you have seen nothing here, and pass on by. The Director has disallowed me from partaking in studies regarding E.G.O; I thought to use the nocturnal umbra to sift through their research material.
   PL:
1064. [Kwestia głosowa [smalltalk_10113_1] — sytuacja] 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=smalltalk_10113_1].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1065. [Kwestia głosowa [smalltalk_10113_1] (Chatter #1)] 하아… 과거의 아픔을 물으시는가. 구태여 떠올리려 하지 않아 기억이 흩어졌소만. 음, 분명 나의 친우들은 하나를 제외하고 모두 돌아서… 나의 가치를 담을 수 있는 기술을 알아보는 N사와 이 신구인회를 옹립했지.\n…무언가 이상하오?
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=smalltalk_10113_1].dlg
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ahh... you would like to know more of my old wounds? Yet my memories have all but scattered away now, for I have not deigned to recall it in some time. My fellows have, save for one, all turned from—\nThus, I have worked with N Corp. to establish this new League of the Nine, for they understand the technology that deserves to harbor my value.\n... Is aught odd about this assessment?
   PL:
1066. [Kwestia głosowa [smalltalk_10113_2] — sytuacja] 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=smalltalk_10113_2].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1067. [Kwestia głosowa [smalltalk_10113_2] (Chatter #2)] 이 이고(E.G.O)는 이사님께 부여받았을 뿐이오. 내게 선택권이 있지도 않았지. 나라고 하여 동료를 관통해 쏘는 일을 좋아서 받아들였을 거라 보는가?\n…그리 보였다고? 그렇다면 그건… 침식, 일 거요.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=smalltalk_10113_2].dlg
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This E.G.O was simply bestowed upon me by the Director, the choice hardly mine. Does your reason truly dictate that I would have readily accepted the manner of occupation that has me shooting my own comrades to fire at our foes?\n... It does? Then it must have been... but a Corrosion.
   PL:
1068. [Kwestia głosowa [smalltalk_10113_3] — sytuacja] 대화 3
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=smalltalk_10113_3].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1069. [Kwestia głosowa [smalltalk_10113_3] (Chatter #3)] 죽어가는 자들을 보고 아쉬워 할 것은 없소. …찾게 되면, 어차피 …것인데.\n나와 친우가 그를 위해 분투하고 있으니 곧 내게 꿰뚫린 동료들도…
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=smalltalk_10113_3].dlg
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One needn't lament for those who are dying. Once we discover the... it shall all... in the end.\nMy fellow and I are toiling incessantly for it; thus, even the comrades whom I have pierced shall soon...
   PL:
1070. [Kwestia głosowa [smalltalk_10113_4] — sytuacja] 동기화 후 대화 1
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=smalltalk_10113_4].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1071. [Kwestia głosowa [smalltalk_10113_4] (Post-Uptie Chat 1)] 새까만 핏조각이 땡그랑 소리 내며 깨어지리라. 관통한 탄환은 여러 갈래가 되어 저들 모두를 파고들터. 이로서 동료들의 희생은 가치로워졌소, 아니… 처음부터 동료였던지도 이젠 흐릿하군!
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=smalltalk_10113_4].dlg
   limit: do 330 znaków
   EN: Obsidian shards of blood shatter with echoes of glass; the perforating bullet scatters to a thousand pellets to bore into them all. Thus worthy has it become, the sacrifice of my comrades... no, I can scarcely recall if they were comrades of mine at all!
   PL:
1072. [Kwestia głosowa [smalltalk_10113_5] — sytuacja] 동기화 후 대화 2
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=smalltalk_10113_5].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1073. [Kwestia głosowa [smalltalk_10113_5] (Post-Uptie Chat 2)] 이 총인지, 아니면 이 넝마인지… 이것들이 내게 계속해서 속삭이고 있소. 적을 노리는 것이 아니다, 사랑을 기억하는 이를 노리라. 그것을 파괴하라, 쏘아라, 쏘으…\n …내가 어디까지 이야기했소?
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=smalltalk_10113_5].dlg
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It whispers to me incessantly, the voice of the rifle, or the ragged cloak... that I am to aim not for my enemies, but for those who still remember love. Destroy it, fire, I shall fi—\n... Remind me, where was I?
   PL:
1074. [Kwestia głosowa [neglect_10113_1] — sytuacja] 방치
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=neglect_10113_1].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1075. [Kwestia głosowa [neglect_10113_1] (Idle)] 팬던트를 꺼내어 보나, 나는 기어코 열지 않으려 하오. 친우가 그랬소. 늦었다고, 늦었다고…
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=neglect_10113_1].dlg
   limit: do 170 znaków
   EN: Hold the pendant in sight I may, but I shan't ever peer into it. A fellow of mine has once spoken thusly to me—<i>too late, too late</i>...
   PL:
1076. [Kwestia głosowa [gacksung_10113_1] — sytuacja] 동기화 진행
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=gacksung_10113_1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1077. [Kwestia głosowa [gacksung_10113_1] (Uptying)] 임무에 나서는가. 함께하는 동료의 숫자는 몇이나 되는가. 음, 총알의 갯수를 세어보아야 하여 묻소.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=gacksung_10113_1].dlg
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Are we to embark on a mission? How many shall accompany us?\nMm. I ask, for I must count my bullets ere it begins.
   PL:
1078. [Kwestia głosowa [formation_10113_1] — sytuacja] 인격 편성
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=formation_10113_1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1079. [Kwestia głosowa [formation_10113_1] (Deployment)] 내 바쁘오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=formation_10113_1].dlg
   limit: do 120 znaków
   EN: I am preoccupied.
   PL:
1080. [Kwestia głosowa [battleentry_10113_1] — sytuacja] 입장
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battleentry_10113_1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1081. [Kwestia głosowa [battleentry_10113_1] (Stage Entry)] 저들은 전율하리라.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battleentry_10113_1].dlg
   limit: do 120 znaków
   EN: They will shiver with frisson.
   PL:
1082. [Kwestia głosowa [battle_select_10113_1] — sytuacja] 전투 중 인격 선택
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_select_10113_1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1083. [Kwestia głosowa [battle_select_10113_1] (Viewed in Battle)] 후후… 음, 웃음은 잊으시오. 어떤 일인가.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_select_10113_1].dlg
   limit: do 120 znaków
   EN: Heh heh... mm. Forget you heard the laughter. What is your business here?
   PL:
1084. [Kwestia głosowa [battle_endcommand_10113_1] — sytuacja] 공격 시작
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_endcommand_10113_1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1085. [Kwestia głosowa [battle_endcommand_10113_1] (Commencing Attack)] 꿰뚫어 퍼지리.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_endcommand_10113_1].dlg
   limit: do 120 znaków
   EN: To pierce and scatter.
   PL:
1086. [Kwestia głosowa [battle_enemy_break_10113_1] — sytuacja] 적 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_enemy_break_10113_1].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1087. [Kwestia głosowa [battle_enemy_break_10113_1] (Enemy Stagger)] 구멍 투성이가 되어-
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_enemy_break_10113_1].dlg
   limit: do 120 znaków
   EN: Become a porous thing—
   PL:
1088. [Kwestia głosowa [battle_break_10113_1] — sytuacja] 흐트러질 시 대사
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_break_10113_1].desc
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1089. [Kwestia głosowa [battle_break_10113_1] (Staggered)] …이런.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_break_10113_1].dlg
   limit: do 120 znaków
   EN: ... Oh.
   PL:
1090. [Kwestia głosowa [battle_kill_10113_1] — sytuacja] 적 처치
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_kill_10113_1].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1091. [Kwestia głosowa [battle_kill_10113_1] (Enemy Killed)] 마침내, 깊은 수면에 빠지시는가.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_kill_10113_1].dlg
   limit: do 120 znaków
   EN: Thus, you sink into a bottomless slumber.
   PL:
1092. [Kwestia głosowa [battle_dead_10113_1] — sytuacja] 본인 사망
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_dead_10113_1].desc
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1093. [Kwestia głosowa [battle_dead_10113_1] (Death)] 죽고 싶던 마음이… 드디어 칼을 찾았는가.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_dead_10113_1].dlg
   limit: do 120 znaków
   EN: The heart that wished to die... has finally found a knife.
   PL:
1094. [Kwestia głosowa [choice_success_p_10113_2] — sytuacja] 선택지 성공
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=choice_success_p_10113_2].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1095. [Kwestia głosowa [choice_success_p_10113_2] (Check Passed)] 보시게, 내 계획했던 대로 되지 않았나.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=choice_success_p_10113_2].dlg
   limit: do 120 znaków
   EN: Behold, for it has transpired exactly as I had planned.
   PL:
1096. [Kwestia głosowa [choice_fail_n_10113_1] — sytuacja] 선택지 실패
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=choice_fail_n_10113_1].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1097. [Kwestia głosowa [choice_fail_n_10113_1] (Check Failed)] …엄밀히 말해, 나의 전문분야가 아니오.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=choice_fail_n_10113_1].dlg
   limit: do 120 znaków
   EN: ... In my defense, this is not my area of expertise.
   PL:
1098. [Kwestia głosowa [battle_clear_10113_1] — sytuacja] 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_clear_10113_1].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1099. [Kwestia głosowa [battle_clear_10113_1] (Victory Cry)] 흠, 이만하면 됐구료. 소기의 목적은 달성한 모양이니. 돌아가는 길이 북적이지 않아 제법 쾌적하겠소. 그리 생각치 않는가?
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_clear_10113_1].dlg
   limit: do 230 znaków
   EN: Hm, the desired purpose has been accomplished; this will suffice. Our return journey should be quite comfortable, given the reduced population of our team. Wouldn't you agree?
   PL:
1100. [Kwestia głosowa [battle_clear_ex_10113_1] — sytuacja] EX CLEAR 전투 승리
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_clear_ex_10113_1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1101. [Kwestia głosowa [battle_clear_ex_10113_1] (Extra Conditions Fulfilled)] 입 안에 짠 맛이 도는군…  아, 무엇인가 했더니 터져버린 동료의 피가 튀었던 모양이군. 허… 이런, 맛이던가.
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_clear_ex_10113_1].dlg
   limit: do 150 znaków
   EN: This taste of salt—ah, blood of my departed comrade must have splattered there. Hmh... so, this is how it tastes.
   PL:
1102. [Kwestia głosowa [battle_defeat_10113_1] — sytuacja] 전투 패배
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_defeat_10113_1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1103. [Kwestia głosowa [battle_defeat_10113_1] (Defeat Wail)] 쳇… 빨리 도망쳐야겠구료. 음, 마침 퇴각을 도울 자들이 도착했나. 자, 따라오게!
   źródło: PersonalityVoiceDlg/Voice_Yisang_NEGO_10113.json :: dataList[id=battle_defeat_10113_1].dlg
   limit: do 160 znaków
   EN: Tsk... we must make ourselves scarce with haste. Those who would assist in our extraction have arrived; now, with me!
   PL:
