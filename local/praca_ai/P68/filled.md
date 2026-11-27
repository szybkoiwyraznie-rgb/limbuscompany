# Paczka AI P68 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 4/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P68_3c_przeciwnicy_i_anomalie_cz04.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P68_3c_przeciwnicy_i_anomalie_cz04.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [a1c10p3] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c10p3
- grupa rozdziału/trybu: `a1c10p3` · plik: `Skills_Abnormality-a1c10p3.json`

1. [Umiejętność wroga [152201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] nakłada 1 [Sinking]
2. [Umiejętność wroga [152201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 1 [Binding] w następnej turze
3. [Umiejętność wroga [152202] (ulepszenie 1) — nazwa] 패턴과 설계
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152202].levelList[level=1].name
   limit: do 40 znaków
   EN: Patterns and Designs
   PL: Patterns and Designs
4. [Umiejętność wroga [152202] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeKhaki] 횟수 3 증가\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152202].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeKhaki], [Breath], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain +3 [ChargeKhaki] Count\n[WhenUse] Gain +2 [Breath] Count\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] zyskuje 3 Licznika [ChargeKhaki]\n[WhenUse] zyskuje 2 Licznika [Breath]\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
5. [Umiejętność wroga [152202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
6. [Umiejętność wroga [152202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 1 Licznika [Sinking]
7. [Umiejętność wroga [152202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
8. [Umiejętność wroga [152202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [AttackDmgDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [AttackDmgDown] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [AttackDmgDown] w następnej turze
9. [Umiejętność wroga [152203] (ulepszenie 1) — nazwa] 시점 고정
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152203].levelList[level=1].name
   limit: do 40 znaków
   EN: Fixed Viewpoint
   PL: Fixed Viewpoint
10. [Umiejętność wroga [152203] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeKhaki] 횟수를 전부 소모하여, 소모한 횟수 3당 피해량 +25% (최대 50%)\n[WhenUse] 자신의 [ChargeKhaki] 횟수 3 증가\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152203].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeKhaki], [Breath], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Consume all [ChargeKhaki] Count on self to deal +25% damage for every 3 [ChargeKhaki] Count consumed (max 50%)\n[WhenUse] Gain +3 [ChargeKhaki] Count\n[WhenUse] Gain +2 [Breath] Count\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] zużywa wszystkie [ChargeKhaki] tej jednostki, zadając +25% obrażeń za każde 3 zużyte Liczniki [ChargeKhaki] (maks. 50%)\n[WhenUse] zyskuje 3 Licznika [ChargeKhaki]\n[WhenUse] zyskuje 2 Licznika [Breath]\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
11. [Umiejętność wroga [152203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
12. [Umiejętność wroga [152203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 이번 턴과 다음 턴에 [PenetrateResistDown] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [PenetrateResistDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [PenetrateResistDown] = 관통 내성 약화 / Pierce Resist Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [PenetrateResistDown] this turn and next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [PenetrateResistDown] w tej turze i następnej
13. [Umiejętność wroga [152203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
14. [Umiejętność wroga [152203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
15. [Umiejętność wroga [152203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
16. [Umiejętność wroga [152203] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152203].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [Umiejętność wroga [152203] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152203].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [Umiejętność wroga [152203] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인 최종 피해량의 (<color=#ff6000><mark color=#ff000040><b><u>대상의 부정적인 효과 종류 갯수</color></mark></b></u> x 15)%만큼 관통 피해 (최대 45%)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152203].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal Pierce damage equal to (<color=#ff6000><mark color=#ff000040><b><u>types of negative effects on target</color></mark></b></u> x 15)% of this Coin's final damage (max 45%)
   PL: [UnBrokenCoinOnSucceedAttack] zadaje obrażenia Przebijające równe (<color=#ff6000><mark color=#ff000040><b><u>liczbie rodzajów negatywnych efektów celu</u></b></mark></color> x 15)% końcowych obrażeń tej Monety (maks. 45%)
19. [Umiejętność wroga [152204] (ulepszenie 1) — nazwa] 관점대로
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152204].levelList[level=1].name
   limit: do 40 znaków
   EN: Within Perspective
   PL: Within Perspective
20. [Umiejętność wroga [152204] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeKhaki] 횟수 2당 최종 위력 +1 (최대 5)\n[OnSucceedEvade] <color=#ff6000><mark color=#ff000040><b><u>자신의 최대 체력의 2%만큼 회복</color></mark></b></u>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152204].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [ChargeKhaki], [OnSucceedEvade]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [WhenUse] Final Power +1 for every 2 [ChargeKhaki] Count on self (max 5)\n[OnSucceedEvade] <color=#ff6000><mark color=#ff000040><b><u>Heal 2% HP</color></mark></b></u>
   PL: [WhenUse] Moc Końcowa +1 za każde 2 Liczniki [ChargeKhaki] tej jednostki (maks. 5)\n[OnSucceedEvade] <color=#ff6000><mark color=#ff000040><b><u>przywraca 2% HP</u></b></mark></color>
21. [Umiejętność wroga [152205] (ulepszenie 1) — nazwa] 포착
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152205].levelList[level=1].name
   limit: do 40 znaków
   EN: Focusing
   PL: Focusing
22. [Umiejętność wroga [152205] (ulepszenie 1) — opis] [CantIdentify]\n[CantDuel] [CantChangeTarget]\n아군 우선 지정\n수비 스킬을 발동시키지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152205].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [CantDuel], [CantChangeTarget]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]
   EN: [CantIdentify]\n[CantDuel] [CantChangeTarget]\nPrioritizes allies\nThis Skill does not trigger Defense Skills
   PL: [CantIdentify]\n[CantDuel] [CantChangeTarget]\npriorytet: sojusznicy\nta Umiejętność nie uruchamia Umiejętności obrony
23. [Umiejętność wroga [152205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 아군이면,
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target is an ally,
   PL: [OnSucceedAttack] jeżeli cel jest sojusznikiem,
24. [Umiejętność wroga [152205] (ulepszenie 1) — moneta 1, efekt 2 — opis] - 대상 처치
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152205].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: - Kill target
   PL: - zabija cel
25. [Umiejętność wroga [152205] (ulepszenie 1) — moneta 1, efekt 3 — opis] - <color=#ff6000><mark color=#ff000040><b><u>[JeanneDesign] 1 얻음</color></mark></b></u>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152205].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, [JeanneDesign]
   znaczenie tagów: [JeanneDesign] = 못 박힘 / Nailed
   EN: - <color=#ff6000><mark color=#ff000040><b><u>Gain 1 [JeanneDesign]</color></mark></b></u>
   PL: - <color=#ff6000><mark color=#ff000040><b><u>zyskuje 1 [JeanneDesign]</u></b></mark></color>
26. [Umiejętność wroga [152301] (ulepszenie 1) — nazwa] 첫번째 스텝
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152301].levelList[level=1].name
   limit: do 40 znaków
   EN: First Step
   PL: First Step
27. [Umiejętność wroga [152301] (ulepszenie 1) — opis] [BeforeUse] 합을 지정한 뫼르소의 스킬이 <color=#ff6000><mark color=#ff000040><b><u>스킬 1</color></mark></b></u>이 아닐 경우, ‘패턴대로 해야지.’로 변경됨\n[WinDuel] 이 스킬을 종료하고 대상에게 ‘우리 같이 카페에서 이야기 나누던 때들이 생각나’ 사용함
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152301].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [BeforeUse], [WinDuel]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [BeforeUse] When Clashing using Meursault's Skills that are not <color=#ff6000><mark color=#ff000040><b><u>Skill 1</color></mark></b></u>, change this Skill to "You've got to keep to the pattern"\n[WinDuel] End this Skill and use "Those times when we chatted together at the café" on the target
   PL: [BeforeUse] jeżeli Umiejętność Meursaulta, który wyznaczył Starcie, nie jest <color=#ff6000><mark color=#ff000040><b><u>Umiejętnością 1</u></b></mark></color>, zmienia tę Umiejętność na „You've got to keep to the pattern”\n[WinDuel] kończy tę Umiejętność i używa „Those times when we chatted together at the café” na celu
28. [Umiejętność wroga [152302] (ulepszenie 1) — nazwa] 두번째 걸음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152302].levelList[level=1].name
   limit: do 40 znaków
   EN: Second Pace
   PL: Second Pace
29. [Umiejętność wroga [152302] (ulepszenie 1) — opis] [BeforeUse] 합을 지정한 뫼르소의 스킬이 <color=#ff6000><mark color=#ff000040><b><u>스킬 2</color></mark></b></u>가 아닐 경우, ‘패턴대로 해야지.’로 변경됨\n[WinDuel] 이 스킬을 종료하고 대상에게 ‘우리 같이 카페에서 이야기 나누던 때들이 생각나’ 사용함
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152302].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [BeforeUse], [WinDuel]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [BeforeUse] When Clashing using Meursault's Skills that are not <color=#ff6000><mark color=#ff000040><b><u>Skill 2</color></mark></b></u>, change this Skill to "You've got to keep to the pattern"\n[WinDuel] End this Skill and use "Those times when we chatted together at the café" on the target
   PL: [BeforeUse] jeżeli Umiejętność Meursaulta, który wyznaczył Starcie, nie jest <color=#ff6000><mark color=#ff000040><b><u>Umiejętnością 2</u></b></mark></color>, zmienia tę Umiejętność na „You've got to keep to the pattern”\n[WinDuel] kończy tę Umiejętność i używa „Those times when we chatted together at the café” na celu
30. [Umiejętność wroga [152303] (ulepszenie 1) — nazwa] 세번째 단계
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152303].levelList[level=1].name
   limit: do 40 znaków
   EN: Third Movement
   PL: Third Movement
31. [Umiejętność wroga [152303] (ulepszenie 1) — opis] [BeforeUse] 합을 지정한 뫼르소의 스킬이 <color=#ff6000><mark color=#ff000040><b><u>스킬 3 또는 E.G.O 스킬</color></mark></b></u>이 아닐 경우, ‘패턴대로 해야지.’로 변경됨\n[WinDuel] 이 스킬을 종료하고 대상에게 ‘우리 같이 카페에서 이야기 나누던 때들이 생각나’ 사용함
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152303].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [BeforeUse], [WinDuel]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [BeforeUse] When Clashing using Meursault's Skills that are not <color=#ff6000><mark color=#ff000040><b><u>Skill 3 or E.G.O Skills</color></mark></b></u>, change this Skill to "You've got to keep to the pattern"\n[WinDuel] End this Skill and use "Those times when we chatted together at the café" on the target
   PL: [BeforeUse] jeżeli Umiejętność Meursaulta, który wyznaczył Starcie, nie jest <color=#ff6000><mark color=#ff000040><b><u>Umiejętnością 3 lub Umiejętnością E.G.O</u></b></mark></color>, zmienia tę Umiejętność na „You've got to keep to the pattern”\n[WinDuel] kończy tę Umiejętność i używa „Those times when we chatted together at the café” na celu
32. [Umiejętność wroga [152304] (ulepszenie 1) — nazwa] 패턴대로 해야지.
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152304].levelList[level=1].name
   limit: do 50 znaków
   EN: You've got to keep to the pattern.
   PL: You've got to keep to the pattern.
33. [Umiejętność wroga [152304] (ulepszenie 1) — opis] 이 스킬은 항상 크리티컬로 발동됨\n[StartDuel] 대상의 <color=#ff6000><mark color=#ff000040><b><u>코인 뒷면 확률 100%로 고정</color></mark></b></u>\n- 빼기 코인일 경우, 앞면으로 고정
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152304].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [StartDuel]
   znaczenie tagów: [StartDuel] = [합 시작 시] / [Clash Start]
   EN: This Skill always hits Critically\n[StartDuel] Target has <color=#ff6000><mark color=#ff000040><b><u>100% chance to flip Tails</color></mark></b></u>\n- Target's Minus Coins have 100% chance to flip Heads
   PL: ta Umiejętność zawsze trafia krytycznie\n[StartDuel] cel ma <color=#ff6000><mark color=#ff000040><b><u>100% szansy na wyrzucenie Reszki</u></b></mark></color>\n- Minusowe Monety celu mają 100% szansy na wyrzucenie Orła
34. [Umiejętność wroga [152304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [JeannePathos] 3 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [JeannePathos]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [JeannePathos] = 파토스 - 데지르 데트르(désir d'être) / Pathos - Désir d'être
   EN: [OnSucceedAttack] Gain 3 [JeannePathos]
   PL: [OnSucceedAttack] zyskuje 3 [JeannePathos]
35. [Umiejętność wroga [152304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [JeannePathos] 3 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
36. [Umiejętność wroga [152305] (ulepszenie 1) — nazwa] 우리 같이 카페에서 이야기 나누던 때들이 생각나
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152305].levelList[level=1].name
   limit: do 70 znaków
   EN: Those times when we chatted together at the café
   PL: Those times when we chatted together at the café
37. [Umiejętność wroga [152305] (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 아래 효과가 적용됨\n- 수비 스킬을 발동시키지 않음\n- 공격이 적중하지 않음\n[WhenUse] 자신과 대상의 [JeannePathos]와 [JeanneLogos]를 각각 5씩 올림
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152305].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [JeannePathos], [JeanneLogos]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [JeannePathos] = 파토스 - 데지르 데트르(désir d'être) / Pathos - Désir d'être; [JeanneLogos] = 로고스 - 망끄 데트르(manque d'être) / Logos - Manque d'être
   EN: [CantDuel]\nThis Skill has the following properties:\n- Does not trigger Defense Skills\n- Its attack does not hit\n[WhenUse] Both this unit and the target gain 5 [JeannePathos] and 5 [JeanneLogos]
   PL: [CantDuel]\nta Umiejętność ma następujące właściwości:\n- nie uruchamia Umiejętności obrony\n- jej atak nie trafia\n[WhenUse] ta jednostka i cel zyskują po 5 [JeannePathos] i 5 [JeanneLogos]
38. [Umiejętność wroga [152306] (ulepszenie 1) — nazwa] 작은 다툼들도 있었지.
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152306].levelList[level=1].name
   limit: do 50 znaków
   EN: We had our little quarrels, yes.
   PL: We had our little quarrels, yes.
39. [Umiejętność wroga [152306] (ulepszenie 1) — opis] [OnSucceedEvade] 자신과 대상의 [JeannePathos]와 [JeanneLogos]를 각각 4씩 올림
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152306].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [JeannePathos], [JeanneLogos]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [JeannePathos] = 파토스 - 데지르 데트르(désir d'être) / Pathos - Désir d'être; [JeanneLogos] = 로고스 - 망끄 데트르(manque d'être) / Logos - Manque d'être
   EN: [OnSucceedEvade] Both this unit and the target gain 4 [JeannePathos] and 4 [JeanneLogos]
   PL: [OnSucceedEvade] ta jednostka i cel zyskują po 4 [JeannePathos] i 4 [JeanneLogos]
40. [Umiejętność wroga [152401] (ulepszenie 1) — nazwa] 권한: 재구축
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152401].levelList[level=1].name
   limit: do 40 znaków
   EN: Rights: Rebuild
   PL: Rights: Rebuild
41. [Umiejętność wroga [152401] (ulepszenie 1) — opis] [CantChangeTarget]\n대상의 수비 스킬 발동하지 않음\n메인 타겟으로 뫼르소를 지정함\n[StartDuel] 자신의 코인 앞면 확률 100% 고정
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152401].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [StartDuel]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [StartDuel] = [합 시작 시] / [Clash Start]
   EN: [CantChangeTarget]\nThis Skill does not trigger the target's Defense Skill\nMainly targets Meursault\n[StartDuel] This unit has 100% chance to flip Heads
   PL: [CantChangeTarget]\nta Umiejętność nie uruchamia Umiejętności obrony celu\ngłównym celem jest Meursault\n[StartDuel] ta jednostka ma 100% szansy na wyrzucenie Orła
42. [Umiejętność wroga [152401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Umiejętność wroga [152401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 타겟 사망
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target dies
   PL: [OnSucceedAttack] cel ginie
44. [Umiejętność wroga [152402] (ulepszenie 1) — nazwa] 권한: 차단
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152402].levelList[level=1].name
   limit: do 40 znaków
   EN: Rights: Ban
   PL: Rights: Ban
45. [Umiejętność wroga [152402] (ulepszenie 1) — opis] <color=#ff6000><mark color=#ff000040><b><u>[EndSkill] 다음 턴에 [JeanneCheat] 1 부여</color></mark></b></u>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, [EndSkill], [JeanneCheat]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [JeanneCheat] = 데제스푸아르(désespoir) / Désespoir
   EN: <color=#ff6000><mark color=#ff000040><b><u>[EndSkill] Inflict 1 [JeanneCheat] next turn</color></mark></b></u>
   PL: <color=#ff6000><mark color=#ff000040><b><u>[EndSkill] nakłada 1 [JeanneCheat] w następnej turze</u></b></mark></color>
46. [Umiejętność wroga [152402] (ulepszenie 1) — tekst klimatyczny] 뫼르. 네가 원한다면, 더 이상 그 사슬로 몸을 감지 않아도 괜찮아. 판단하고, 말해도 괜찮아. 누구의 눈치도 보지 않고, 누구의 생각도 의식하지 않고, 너답게 말이야.
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152402].levelList[level=1].flavor
   limit: do 340 znaków
   EN: Meur. If you want, you don't have to keep binding yourself in those chains anymore. You're allowed to judge for yourself. You should be allowed to speak. No more worrying about anyone's gaze, no more letting anyone else's thoughts weigh on you... Just <i>be</i> yourself.
   PL: Meur. Jeżeli tego chcesz, nie musisz już więcej krępować się tymi łańcuchami. Możesz osądzać na własną rękę. Powinno ci być wolno mówić. Bez oglądania się na czyjś wzrok, bez ulegania czyimś myślom... po prostu <i>bądź</i> sobą.
47. [Umiejętność wroga [152402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [Umiejętność wroga [152402] (ulepszenie 1) — moneta 1, efekt 2 — opis] 파괴되지 않은 코인일 경우, 피해량 +20%
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: If the Coin is not Cracked, deal +20% damage
   PL: jeżeli Moneta nie jest pęknięta, zadaje +20% obrażeń
49. [Umiejętność wroga [152402] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152402].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Vulnerable]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Vulnerable]
50. [Umiejętność wroga [152402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Umiejętność wroga [152402] (ulepszenie 1) — moneta 2, efekt 2 — opis] 파괴되지 않은 코인일 경우, 피해량 +20%
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Umiejętność wroga [152402] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152402].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Vulnerable] w następnej turze
53. [Umiejętność wroga [152403] (ulepszenie 1) — nazwa] 이 무대에서만큼은 모든게 정해져 있어.
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152403].levelList[level=1].name
   limit: do 70 znaków
   EN: At least on this stage, everything's set and fixed.
   PL: At least on this stage, everything's set and fixed.
54. [Umiejętność wroga [152403] (ulepszenie 1) — opis] [BeforeUse] 합을 지정한 대상이 <color=#ff6000><mark color=#ff000040><b><u>뫼르소가 아니거나 이 스킬로 일방 공격할 경우,</color></mark></b></u> ‘의도된 패턴대로 하지 않았잖아.’로 변경됨\n[DefeatDuel] 뫼르소의 [JeanneLogos]가 10 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152403].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [BeforeUse], [DefeatDuel], [JeanneLogos]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [JeanneLogos] = 로고스 - 망끄 데트르(manque d'être) / Logos - Manque d'être
   EN: [BeforeUse] When Clashing against targets <color=#ff6000><mark color=#ff000040><b><u>that are not Meursault, or if this Skill is used as an Unopposed Attack,</color></mark></b></u> change this Skill to "You went off-pattern."\n[DefeatDuel] Meursault gains 10 [JeanneLogos]
   PL: [BeforeUse] jeżeli cel wyznaczony do Starcia <color=#ff6000><mark color=#ff000040><b><u>nie jest Meursaultem albo ta Umiejętność wykonuje atak jednostronny,</u></b></mark></color> zmienia tę Umiejętność na „You went off-pattern.”\n[DefeatDuel] Meursault zyskuje 10 [JeanneLogos]
55. [Umiejętność wroga [152404] (ulepszenie 1) — nazwa] 의도된 패턴대로 하지 않았잖아.
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152404].levelList[level=1].name
   limit: do 40 znaków
   EN: You went off-pattern.
   PL: You went off-pattern.
56. [Umiejętność wroga [152404] (ulepszenie 1) — opis] 이 스킬은 항상 크리티컬로 발동됨\n[StartDuel] <color=#ff6000><mark color=#ff000040><b><u>대상의 코인 뒷면 확률 100%로 고정</color></mark></b></u>\n- 빼기 코인일 경우, 앞면으로 고정\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>최대 체력의 50%만큼 회복함</color></mark></b></u>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152404].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [StartDuel], [EndSkill]
   znaczenie tagów: [StartDuel] = [합 시작 시] / [Clash Start]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: This Skill always hits Critically\n[StartDuel] Target has <color=#ff6000><mark color=#ff000040><b><u>100% chance to flip Tails</color></mark></b></u>\n- Target's Minus Coins have 100% chance to flip Heads\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>Heal 50% HP</color></mark></b></u>
   PL: ta Umiejętność zawsze trafia krytycznie\n[StartDuel] cel ma <color=#ff6000><mark color=#ff000040><b><u>100% szansy na wyrzucenie Reszki</u></b></mark></color>\n- Minusowe Monety celu mają 100% szansy na wyrzucenie Orła\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>przywraca 50% HP</u></b></mark></color>
57. [Umiejętność wroga [152404] (ulepszenie 1) — tekst klimatyczny] 뫼르, 기믹은 잘 수행해야지.
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152404].levelList[level=1].flavor
   limit: do 120 znaków
   EN: Meur, you need to execute the gimmick right.
   PL: Meur, you need to execute the gimmick right.
58. [Umiejętność wroga [152404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Umiejętność wroga [152404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [Umiejętność wroga [152405] (ulepszenie 1) — nazwa] 여기까지 설계야.
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152405].levelList[level=1].name
   limit: do 50 znaków
   EN: The designing was up to this point.
   PL: The designing was up to this point.
61. [Umiejętność wroga [152405] (ulepszenie 1) — opis] [WhenUse] 자신의 특수 [Charge] 횟수 2당 최종 위력 +1 (최대 5)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152405].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Final Power +1 for every 2 Unique [Charge] Count on self (max 5)
   PL: [WhenUse] Moc Końcowa +1 za każde 2 Unikalnych Liczników [Charge] tej jednostki (maks. 5)
62. [Umiejętność wroga [152406] (ulepszenie 1) — nazwa] 권한: 시선
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152406].levelList[level=1].name
   limit: do 40 znaków
   EN: Rights: Gaze
   PL: Rights: Gaze
63. [Umiejętność wroga [152406] (ulepszenie 1) — opis] [WhenUse] 자신의 특수 [Charge] (위력 + 횟수) 합 4당 최종 위력 +1 (최대 3)\n[WhenUse] 모든 대상의 부정적인 효과 종류 합 2개당 피해량 +10% (최대 50%, 대상마다 중복되는 효과는 별개로 취급)\n<color=#ff6000><mark color=#ff000040><b><u>[WinDuel] 다음 턴에 [JeanneCheat] 1 부여</color></mark></b></u>\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152406].levelList[level=1].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Charge], [WinDuel], [JeanneCheat], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [WinDuel] = [합 승리시] / [Clash Win]; [JeanneCheat] = 데제스푸아르(désespoir) / Désespoir; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Final Power +1 for every 4 Unique [Charge] (Potency + Count) on self (max 3)\n[WhenUse] Deal +10% damage for every 2 types of negative effects on all targets (max 50%; overlapping effects between units are counted separately)\n<color=#ff6000><mark color=#ff000040><b><u>[WinDuel] Inflict 1 [JeanneCheat] next turn</color></mark></b></u>\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Końcowa +1 za każde 4 Unikalnego [Charge] (Siła + Licznik) tej jednostki (maks. 3)\n[WhenUse] zadaje +10% obrażeń za każde 2 rodzaje negatywnych efektów na wszystkich celach (maks. 50%; nakładające się efekty między jednostkami rozpatrywane są osobno)\n<color=#ff6000><mark color=#ff000040><b><u>[WinDuel] nakłada 1 [JeanneCheat] w następnej turze</u></b></mark></color>\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
64. [Umiejętność wroga [152406] (ulepszenie 1) — tekst klimatyczny] 너는 네 어머니가 느꼈던 그 불안을 누구보다 잘 알고 있었을 거야.\n하지만 뫼르, 누군가와 같은 공간에 있는 것만으로도 시선은 느껴질 수밖에 없어. 같은 공간에 존재하는 한, 너는 네 어머니에게 바라보아지고, 바라볼 수밖에 없었겠지.\n\n그 죄책감 때문일까?\n너는 자꾸만 네 어머니에게 일어난 일을 자신의 탓으로 미루고 있는 것 같아.
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152406].levelList[level=1].flavor
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You must've understood the anxiety your mother felt better than anyone. But, Meur... simply sharing the same space with someone means becoming aware of their gaze. As long as you were there together, you must've had to bear your mother's gaze. You could hardly help but gaze her in return.\n\nIs that why you feel guilty?\nIt seems to me you're still trying to make what happened to your mother into something that was your fault.
   PL: Musiałeś rozumieć niepokój swojej matki lepiej niż ktokolwiek.\nAle, Meur... samo przebywanie z kimś w tej samej przestrzeni sprawia, że czujesz się obserwowany. Dopóki istniejecie w tej samej przestrzeni, matka musiała na ciebie patrzeć — a ty nie mogłeś nie patrzeć na nią.\n\nCzy dlatego czujesz się winny?\nWydaje mi się, że wciąż próbujesz przedstawić to, co stało się twojej matce, jako twoją własną winę.
65. [Umiejętność wroga [152406] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152406].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Umiejętność wroga [152406] (ulepszenie 1) — moneta 1, efekt 2 — opis] 파괴되지 않은 코인일 경우, 피해량 +50%
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152406].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: If the Coin is not Cracked, deal +50% damage
   PL: jeżeli Moneta nie jest pęknięta, zadaje +50% obrażeń
67. [Umiejętność wroga [152406] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [AttackDmgDown] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152406].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [AttackDmgDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [AttackDmgDown] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [AttackDmgDown] w następnej turze
68. [Umiejętność wroga [152406] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152406].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [Umiejętność wroga [152406] (ulepszenie 1) — moneta 2, efekt 2 — opis] 파괴되지 않은 코인일 경우, 피해량 +50%
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152406].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Umiejętność wroga [152406] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152406].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Binding] w następnej turze
71. [Umiejętność wroga [152501] (ulepszenie 1) — nazwa] 백화점 설계도
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152501].levelList[level=1].name
   limit: do 40 znaków
   EN: Department Store Blueprint
   PL: Department Store Blueprint
72. [Umiejętność wroga [152501] (ulepszenie 1) — opis] [WhenUse] 스킬로 받는 피해량 -90% (턴당 1회)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Take -90% damage from Skills (once per turn)
   PL: [WhenUse] otrzymuje -90% obrażeń od Umiejętności (1 raz na turę)
73. [Umiejętność wroga [152501] (ulepszenie 1) — tekst klimatyczny] 이것은 백화점 설계도가 아니다.
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152501].levelList[level=1].flavor
   limit: do 120 znaków
   EN: This is not a department store blueprint.
   PL: This is not a department store blueprint.
74. [Umiejętność wroga [152601] (ulepszenie 1) — nazwa] 패턴: 욕망하라
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152601].levelList[level=1].name
   limit: do 40 znaków
   EN: Pattern: "Desire."
   PL: Pattern: "Desire."
75. [Umiejętność wroga [152601] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeRouge] 횟수가 최대가 아닐 때, 자신의 체력을 최대 체력의 5% 소모하여, [ChargeRouge] 횟수 10 얻음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152601].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] At fewer than max [ChargeRouge] Count, consume 5% HP to gain 10 [ChargeRouge] Count
   PL: [WhenUse] jeżeli Liczniki [ChargeRouge] tej jednostki nie są na maksimum, zużywa 5% HP, aby zyskać 10 Licznika [ChargeRouge]
76. [Umiejętność wroga [152601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] nakłada 3 [Laceration]
77. [Umiejętność wroga [152602] (ulepszenie 1) — nazwa] 패턴: 걸쳐라
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152602].levelList[level=1].name
   limit: do 40 znaków
   EN: Pattern: "Don."
   PL: Pattern: "Don."
78. [Umiejętność wroga [152602] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeRouge] 횟수가 최대가 아닐 때, 자신의 체력을 최대 체력의 5% 소모하여, [ChargeRouge] 횟수 10 얻음\n[WhenUse] 자신의 [ChargeRouge] 횟수 5 소모하여, 최종 위력 +2
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152602].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] At fewer than max [ChargeRouge] Count, consume 5% HP to gain 10 [ChargeRouge] Count\n[WhenUse] Consume 5 [ChargeRouge] Count to gain Final Power +2
   PL: [WhenUse] jeżeli Liczniki [ChargeRouge] tej jednostki nie są na maksimum, zużywa 5% HP, aby zyskać 10 Licznika [ChargeRouge]\n[WhenUse] zużywa 5 Licznika [ChargeRouge], aby zyskać Moc Końcową +2
79. [Umiejętność wroga [152602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Laceration]
80. [Umiejętność wroga [152602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Umiejętność wroga [152603] (ulepszenie 1) — nazwa] 패턴: 섭취하라
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152603].levelList[level=1].name
   limit: do 40 znaków
   EN: Pattern: "Consume."
   PL: Pattern: "Consume."
82. [Umiejętność wroga [152603] (ulepszenie 1) — opis] [WhenUse] 자신의 잃은 체력 2%당 피해량 +3% (최대 60%)\n[WhenUse] 자신의 [ChargeRouge] 횟수를 전부 소모하여, 소모한 횟수 2당 최종 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152603].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] Deal +3% damage for every 2% missing HP on self (max 60%)\n[WhenUse] Consume all [ChargeRouge] Count on self to gain Final Power +1 for every 2 [ChargeRouge] Count consumed (max 3)
   PL: [WhenUse] zadaje +3% obrażeń za każde 2% utraconego HP tej jednostki (maks. 60%)\n[WhenUse] zużywa wszystkie [ChargeRouge] tej jednostki, aby zyskać Moc Końcową +1 za każde 2 zużyte Liczniki [ChargeRouge] (maks. 3)
83. [Umiejętność wroga [152603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [ScarletTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ScarletTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ScarletTakeDamageUp] = 색욕 취약 / Lust Fragility
   EN: [OnSucceedAttack] Inflict 1 [ScarletTakeDamageUp]
   PL: [OnSucceedAttack] nakłada 1 [ScarletTakeDamageUp]
84. [Umiejętność wroga [152603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 (자신의 잃은 체력 비율)% 만큼 색욕 피해
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal Lust damage equal to (missing HP on self)% of this Coin's final damage
   PL: [OnSucceedAttack] zadaje obrażenia Żądzy równe (procent utraconego HP tej jednostki)% końcowych obrażeń tej Monety
85. [Umiejętność wroga [152604] (ulepszenie 1) — nazwa] 패턴: 긁어모아라
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152604].levelList[level=1].name
   limit: do 50 znaków
   EN: Pattern: "Scrape and gather."
   PL: Pattern: "Scrape and gather."
86. [Umiejętność wroga [152604] (ulepszenie 1) — opis] [WhenUse] 자신의 최대 체력의 25%만큼 회복\n- 자신의 [ChargeRouge]이 2 이상이면, 대신 50%만큼 회복
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] Heal 25% HP\n- At 2+ [ChargeRouge], heal 50% HP instead
   PL: [WhenUse] przywraca 25% HP\n- przy 2+ [ChargeRouge] przywraca zamiast tego 50% HP
87. [Umiejętność wroga [152701] (ulepszenie 1) — nazwa] 재단: 보존하라
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152701].levelList[level=1].name
   limit: do 40 znaków
   EN: Tailoring: "Conserve."
   PL: Tailoring: "Conserve."
88. [Umiejętność wroga [152701] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoir] 횟수 5 증가\n- 대상에게 [Vibration]이 있으면, 추가로 5 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152701].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoir], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +5 [ChargeNoir] Count\n- If target has [Vibration], gain +5 additional [ChargeNoir] Count
   PL: [WhenUse] zyskuje 5 Licznika [ChargeNoir]\n- jeżeli cel ma [Vibration], dodatkowo zyskuje 5 Licznika [ChargeNoir]
89. [Umiejętność wroga [152701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] nakłada 3 [Vibration]
90. [Umiejętność wroga [152702] (ulepszenie 1) — nazwa] 재단: 묵시하라
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152702].levelList[level=1].name
   limit: do 50 znaków
   EN: Tailoring: "Witness in silence."
   PL: Tailoring: "Witness in silence."
91. [Umiejętność wroga [152702] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoir] 횟수 5 증가\n- 대상에게 [Vibration]이 있으면, 추가로 5 증가\n[WhenUse] 자신의 [ChargeNoir] 횟수 2당 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeNoir] 횟수가 10 이상이면, 코인 적중시마다 [Vibration] 위력 5 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152702].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoir], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain 5 [ChargeNoir] Count\n- If target has [Vibration], gain 5 additional [ChargeNoir] Count\n[WhenUse] Final Power +1 for every 2 [ChargeNoir] Count on self (max 2)\n[WhenUse] At 10+ [ChargeNoir] Count, inflict 5 [Vibration] Potency on Coin Hit
   PL: [WhenUse] zyskuje 5 Licznika [ChargeNoir]\n- jeżeli cel ma [Vibration], dodatkowo zyskuje 5 Licznika [ChargeNoir]\n[WhenUse] Moc Końcowa +1 za każde 2 Liczniki [ChargeNoir] tej jednostki (maks. 2)\n[WhenUse] przy 10+ Licznika [ChargeNoir] nakłada 5 Siły [Vibration] przy trafieniu Monetą
92. [Umiejętność wroga [152702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Vibration]
93. [Umiejętność wroga [152702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
94. [Umiejętność wroga [152703] (ulepszenie 1) — nazwa] 재단: 고정하라
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152703].levelList[level=1].name
   limit: do 50 znaków
   EN: Tailoring: "Let all be pinned."
   PL: Tailoring: "Let all be pinned."
95. [Umiejętność wroga [152703] (ulepszenie 1) — opis] 자신의 [ChargeNoir]당 피해량 +4% (최대 20%)\n[WhenUse] 자신의 [ChargeNoir] 횟수를 전부 소모하여, 소모한 횟수 2당 최종 위력 +1 (최대 3)\n- 소모한 값이 10 이상이면, 코인 적중시마다 [Vibration] 위력 5 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152703].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir], [WhenUse], [Vibration]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: Deal +4% damage for every [ChargeNoir] on self (max 20%)\n[WhenUse] Consume all [ChargeNoir] Count on self to gain Final Power +1 for every 2 [ChargeNoir] Count consumed (max 3)\n- If this unit consumed 10+ [ChargeNoir] Count, inflict 5 [Vibration] Potency on Coin Hit
   PL: zadaje +4% obrażeń za każde 1 [ChargeNoir] tej jednostki (maks. 20%)\n[WhenUse] zużywa wszystkie [ChargeNoir] tej jednostki, aby zyskać Moc Końcową +1 za każde 2 zużyte Liczniki [ChargeNoir] (maks. 3)\n- jeżeli zużyła 10+ Liczników [ChargeNoir], przy każdym trafieniu Monetą nakłada 5 Siły [Vibration]
96. [Umiejętność wroga [152703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Umiejętność wroga [152703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 (대상의 [Vibration] 위력)% 만큼 나태 피해
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Deal Sloth damage equal to ([Vibration] Potency on target)% of this Coin's final damage
   PL: [OnSucceedAttack] zadaje obrażenia Lenistwa równe (Siła [Vibration] celu)% końcowych obrażeń tej Monety
98. [Umiejętność wroga [152704] (ulepszenie 1) — nazwa] 재단: 못박히라
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152704].levelList[level=1].name
   limit: do 50 znaków
   EN: Tailoring: "Cometh the nail."
   PL: Tailoring: "Cometh the nail."
99. [Umiejętność wroga [152704] (ulepszenie 1) — opis] [StartBattle] 이번 턴과 다음 턴 동안 보호막을 자신의 최대 체력의 25%만큼 얻음 (최소 1)\n- 자신의 [ChargeNoir]이 2 이상이면, 대신 40% 얻음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152704].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [ChargeNoir]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeNoir] = 보존 / Preservation
   EN: [StartBattle] This turn and next turn, gain Shield equal to 25% of this unit's max HP (min 1)\n- At 2+ [ChargeNoir], gain Shield equal to 40% of this unit's max HP instead
   PL: [StartBattle] w tej turze i następnej zyskuje Tarczę równą 25% Maks. HP tej jednostki (min. 1)\n- przy 2+ [ChargeNoir] zamiast tego zyskuje Tarczę równą 40% Maks. HP tej jednostki
100. [Umiejętność wroga [151701] (ulepszenie 1) — nazwa] 주 멕스퓔스(je m'expulse)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151701].levelList[level=1].name
   limit: do 40 znaków
   EN: Je m'expulse
   PL: Je m'expulse
101. [Umiejętność wroga [151701] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 [Laceration]이 6 이상이면, 코인 위력 +1\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] 메인 타겟에게 [Laceration]이 없다면,</u></b></mark></color> 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151701].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Laceration], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If the main target has 6+ [Laceration], Coin Power +1\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] If the main target does not have [Laceration]</u></b></mark></color>, convert all Coins on this Skill to [SuperCoin]s\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] jeżeli główny cel ma 6+ [Laceration], Moc Monety +1\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] jeżeli główny cel nie ma [Laceration],</u></b></mark></color> wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
102. [Umiejętność wroga [151701] (ulepszenie 1) — tekst klimatyczny] 배출하고.
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151701].levelList[level=1].flavor
   limit: do 120 znaków
   EN: Excrete.
   PL: Excrete.
103. [Umiejętność wroga [151701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Umiejętność wroga [151701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Laceration]
105. [Umiejętność wroga [151702] (ulepszenie 1) — nazwa] 주 므 크라슈(je me crache)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151702].levelList[level=1].name
   limit: do 40 znaków
   EN: Je me crache
   PL: Je me crache
106. [Umiejętność wroga [151702] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 기본 위력 +2\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>자신의 [ChargeRouge] 위력 2당, 가중치 +1</u></b></mark></color> (최대 2)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151702].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Laceration], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] If target has 6+ [Laceration], Base Power +2\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>Gain +1 Atk Weight for every 2 [ChargeRouge] Potency on self</u></b></mark></color> (max 2)
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Bazowa +2\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>zyskuje Wagę Ataku +1 za każde 2 Siły [ChargeRouge] tej jednostki</u></b></mark></color> (maks. 2)
107. [Umiejętność wroga [151702] (ulepszenie 1) — tekst klimatyczny] 뱉어내고.
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151702].levelList[level=1].flavor
   limit: do 120 znaków
   EN: Vomit.
   PL: Vomit.
108. [Umiejętność wroga [151702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] nakłada 2 [Laceration]
109. [Umiejętność wroga [151702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BoneNail] 3 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BoneNail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BoneNail] = 라브젝트(l'abject) / L'Abject
   EN: [OnSucceedAttack] Inflict 3 [BoneNail]
   PL: [OnSucceedAttack] nakłada 3 [BoneNail]
110. [Umiejętność wroga [151703] (ulepszenie 1) — nazwa] 주 마브젝트(je m'abjecte)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151703].levelList[level=1].name
   limit: do 40 znaków
   EN: Je m'abjecte
   PL: Je m'abjecte
111. [Umiejętność wroga [151703] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 [Laceration] 4당, 코인 위력 +1 (최대 2)\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>자신의 [ChargeRouge] 위력 2당, 가중치 +1</u></b></mark></color> (최대 2)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151703].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Laceration], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] Coin Power +1 for every 4 [Laceration] on the main target (max 2)\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>Gain +1 Atk Weight for every 2 [ChargeRouge] Potency on self</u></b></mark></color> (max 2)
   PL: [WhenUse] Moc Monety +1 za każde 4 [Laceration] na głównym celu (maks. 2)\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>zyskuje Wagę Ataku +1 za każde 2 Siły [ChargeRouge] tej jednostki</u></b></mark></color> (maks. 2)
112. [Umiejętność wroga [151703] (ulepszenie 1) — tekst klimatyczny] 내던진다.
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151703].levelList[level=1].flavor
   limit: do 120 znaków
   EN: And cast it to the world.
   PL: And cast it to the world.
113. [Umiejętność wroga [151703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] nakłada 1 [Laceration]
114. [Umiejętność wroga [151703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BoneNail] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BoneNail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BoneNail] = 라브젝트(l'abject) / L'Abject
   EN: [OnSucceedAttack] Inflict 2 [BoneNail]
   PL: [OnSucceedAttack] nakłada 2 [BoneNail]
115. [Umiejętność wroga [151703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Umiejętność wroga [151703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [BoneNail]가 3 이상이면, 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BoneNail], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BoneNail] = 라브젝트(l'abject) / L'Abject; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] If target has 3+ [BoneNail], inflict 2 [Vulnerable] next turn
   PL: [OnSucceedAttack] jeżeli cel ma 3+ [BoneNail], nakłada 2 [Vulnerable] w następnej turze
117. [Umiejętność wroga [151704] (ulepszenie 1) — nazwa] 라 퓔시옹(la pulsion)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151704].levelList[level=1].name
   limit: do 40 znaków
   EN: La Pulsion
   PL: La Pulsion
118. [Umiejętność wroga [151704] (ulepszenie 1) — opis] [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\n르루주 고위 스태프를 타겟으로 지정\n\n[WhenUse] 자신의 [ChargeRouge] 횟수가 10 이상이면, [ChargeRouge] 횟수를 최대 10 소모하고 가중치 +2
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151704].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [SupportAlly], [WhenUse], [ChargeRouge]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [SupportAlly] = 양극성 / Duality; [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\nTargets Le Rouge Senior Staff\n\n[WhenUse] At 10+ [ChargeRouge] Count, consume up to 10 [ChargeRouge] Count and gain +2 Atk Weight
   PL: [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\npriorytet: Le Rouge Senior Staff\n\n[WhenUse] przy 10+ Licznika [ChargeRouge] zużywa do 10 Licznika [ChargeRouge] i zyskuje Wagę Ataku +2
119. [Umiejętność wroga [151704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [EndCoin] 대상의 [ChargeRouge] 횟수 10 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [ChargeRouge]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [ChargeRouge] = 맥동 / Pulsation
   EN: [EndCoin] Apply +10 [ChargeRouge] Count
   PL: [EndCoin] zwiększa Licznik [ChargeRouge] celu o 10
120. [Umiejętność wroga [151704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [EndCoin] 대상의 현재 체력을 50% 감소시키고, <color=#ff6000><mark=#ff000040><b><u>[AttackUp] 5 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [EndCoin], [AttackUp]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [EndCoin] Reduce target's current HP by 50%; <color=#ff6000><mark=#ff000040><b><u>then, apply 5 [AttackUp]</u></b></mark></color>
   PL: [EndCoin] zmniejsza aktualne HP celu o 50%; <color=#ff6000><mark=#ff000040><b><u>następnie nakłada 5 [AttackUp]</u></b></mark></color>
121. [Umiejętność wroga [151704] (ulepszenie 1) — moneta 1, efekt 3 — opis] [EndCoin] <color=#ff6000><mark=#ff000040><b><u>[BuffetRouge] 3 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151704].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [EndCoin], [BuffetRouge]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [BuffetRouge] = 폭주[르 데지르] / Uncontrollable Rampage [Le Désir]
   EN: [EndCoin] <color=#ff6000><mark=#ff000040><b><u>Apply 3 [BuffetRouge]</u></b></mark></color>
   PL: [EndCoin] <color=#ff6000><mark=#ff000040><b><u>nakłada 3 [BuffetRouge]</u></b></mark></color>
122. [Umiejętność wroga [151705] (ulepszenie 1) — nazwa] 르 망카에트르(le manque-à-être)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151705].levelList[level=1].name
   limit: do 40 znaków
   EN: Le Manque-à-être
   PL: Le Manque-à-être
123. [Umiejętność wroga [151705] (ulepszenie 1) — opis] [CantDuel]\n[CantChangeTarget]\n[SupportAlly]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151705].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [SupportAlly]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [SupportAlly] = 양극성 / Duality
   EN: [CantDuel]\n[CantChangeTarget]\n[SupportAlly]
   PL: [CantDuel]\n[CantChangeTarget]\n[SupportAlly]
124. [Umiejętność wroga [151705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [EndCoin] 대상의 흐트러짐 상태 해제
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: [EndCoin] Recover target from Stagger
   PL: [EndCoin] przywraca cel z Oszołamienia
125. [Umiejętność wroga [151705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [EndCoin] 스킬 최종 위력만큼 대상의 체력 회복
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: [EndCoin] Heal HP on target equal to this Skill's Final Power
   PL: [EndCoin] przywraca celowi HP równe Mocy Końcowej tej Umiejętności
126. [Umiejętność wroga [151705] (ulepszenie 1) — moneta 1, efekt 3 — opis] [EndCoin] [BuffetRouge] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151705].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [BuffetRouge]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [BuffetRouge] = 폭주[르 데지르] / Uncontrollable Rampage [Le Désir]
   EN: [EndCoin] Apply 1 [BuffetRouge]
   PL: [EndCoin] nakłada 1 [BuffetRouge]
127. [Umiejętność wroga [151706] (ulepszenie 1) — nazwa] 라 주이상스(la jouissance)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151706].levelList[level=1].name
   limit: do 40 znaków
   EN: La Jouissance
   PL: La Jouissance
128. [Umiejętność wroga [151706] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>전장의 르루주 고위 스태프 1명당, 정신력 15 회복, 합 위력 +2</u></b></mark></color>\n[WhenUse] 르루주 고위 스태프가 <color=#ff6000><mark=#ff000040><b><u>모두 사망한 상태</u></b></mark></color>이면, 합 위력 -3\n[DefeatDuel] <color=#ff6000><mark=#ff000040><b><u>[BuffetDream] 1 얻음.</u></b></mark></color> 피해량 -80%, 이 스킬 피해로 대상이 흐트러지지 않음\n[EndSkill] 메인 타겟의 [BuffetScruple]을 [BuffetResolve]으로 변경
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151706].levelList[level=1].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [DefeatDuel], [BuffetDream], [EndSkill], [BuffetScruple], [BuffetResolve]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BuffetDream] = 뿌이의 기억 / Pwie's Memories; [EndSkill] = [공격 종료시] / [Attack End]; [BuffetScruple] = 뿌이와의 경험 / Shared with Pwie; [BuffetResolve] = 결단 / Decision
   EN: Can Clash with this Skill regardless of Speed\n\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>Heal 15 SP and gain Clash Power +2 for every Le Rouge Senior Staff</u></b></mark></color> on the field\n[WhenUse] If <color=#ff6000><mark=#ff000040><b><u>all Le Rouge Senior Staff are defeated</u></b></mark></color>, Clash Power -3\n[DefeatDuel] \n- <color=#ff6000><mark=#ff000040><b><u>Gain 1 [BuffetDream].</u></b></mark></color>\n- Deal -80% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] Convert [BuffetScruple] on the main target into [BuffetResolve]
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>przywraca 15 SP i zyskuje Moc Starcia +2 za każdego Le Rouge Senior Staff na polu</u></b></mark></color>\n[WhenUse] jeżeli <color=#ff6000><mark=#ff000040><b><u>wszyscy Le Rouge Senior Staff zostali pokonani</u></b></mark></color>, Moc Starcia -3\n[DefeatDuel]\n- <color=#ff6000><mark=#ff000040><b><u>zyskuje 1 [BuffetDream].</u></b></mark></color>\n- zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu\n[EndSkill] zamienia [BuffetScruple] głównego celu w [BuffetResolve]
129. [Umiejętność wroga [151706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Umiejętność wroga [151706] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151706].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Umiejętność wroga [151706] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151706].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Umiejętność wroga [151706] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151706].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Umiejętność wroga [151706] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151706].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Laceration]
134. [Umiejętność wroga [151706] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151706].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Umiejętność wroga [151706] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151706].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Umiejętność wroga [151706] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 3회 발동. 대상의 [Laceration] 횟수 3 감소
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151706].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Activate [Laceration] on target 3 times. Target loses 3 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] uruchamia [Laceration] na celu 3 razy. Cel traci 3 Licznika [Laceration]
137. [Umiejętność wroga [151707] (ulepszenie 1) — nazwa] 라 드망드(la demande)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151707].levelList[level=1].name
   limit: do 40 znaków
   EN: La Demande
   PL: La Demande
138. [Umiejętność wroga [151707] (ulepszenie 1) — opis] [CantDuel]\n[CantChangeTarget]\n이 스킬은 수비 스킬을 발동시키지 않음\n[WhenUse] 메인 타겟의 [BoneNail] 모두 제거\n[WhenUse] 메인 타겟의 [Laceration] 4당, 코인 위력 +1 (최대 2)\n[EndSkill] 메인 타겟의 [BuffetScruple] 제거
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151707].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [WhenUse], [BoneNail], [Laceration], [EndSkill], [BuffetScruple]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [BoneNail] = 라브젝트(l'abject) / L'Abject; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [BuffetScruple] = 뿌이와의 경험 / Shared with Pwie
   EN: [CantDuel]\n[CantChangeTarget]\nThis Skill does not trigger Defense Skills\n[WhenUse] Remove all [BoneNail] on the main target\n[WhenUse] Coin Power +1 for every 4 [Laceration] on the main target (max 2)\n[EndSkill] Remove [BuffetScruple] on the main target
   PL: [CantDuel]\n[CantChangeTarget]\nta Umiejętność nie uruchamia Umiejętności obrony\n[WhenUse] usuwa wszystkie [BoneNail] głównego celu\n[WhenUse] Moc Monety +1 za każde 4 [Laceration] na głównym celu (maks. 2)\n[EndSkill] usuwa [BuffetScruple] głównego celu
139. [Umiejętność wroga [151707] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151707].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Umiejętność wroga [151707] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151707].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Umiejętność wroga [151707] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151707].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on target once. Target loses 1 [Laceration] Count
   PL: [OnSucceedAttack] uruchamia [Laceration] na celu 1 raz. Cel traci 1 Licznika [Laceration]
142. [Umiejętność wroga [151708] (ulepszenie 1) — nazwa] 르 농뒤페르(le Nom-du-Père)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151708].levelList[level=1].name
   limit: do 40 znaków
   EN: Le Nom-du-Père
   PL: Le Nom-du-Père
143. [Umiejętność wroga [151708] (ulepszenie 1) — opis] [StartBattle] <color=#ff6000><mark=#ff000040><b><u>[BuffetRouge]가 있으면</u></b></mark></color>, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 메인 타겟의 [Laceration] 4당, 코인 위력 +1 (최대 2)\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>메인 타겟에게 [BuffetScruple]이 있으면</u></b></mark></color>, 가중치 -2\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] 메인 타겟의 [BuffetScruple] 제거
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151708].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StartBattle], [BuffetRouge], [SuperCoin], [WhenUse], [Laceration], [BuffetScruple], [DefeatDuel], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BuffetRouge] = 폭주[르 데지르] / Uncontrollable Rampage [Le Désir]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BuffetScruple] = 뿌이와의 경험 / Shared with Pwie; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [StartBattle] <color=#ff6000><mark=#ff000040><b><u>If this unit has [BuffetRouge]</u></b></mark></color>, convert all Coins on this Skill to [SuperCoin]s\n[WhenUse] Coin Power +1 for every 4 [Laceration] on the main target (max 2)\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>If the main target has [BuffetScruple], lose 2 Atk Weight</u></b></mark></color>\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] Remove [BuffetScruple] on the main target
   PL: [StartBattle] <color=#ff6000><mark=#ff000040><b><u>jeżeli ta jednostka ma [BuffetRouge],</u></b></mark></color> wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y\n[WhenUse] Moc Monety +1 za każde 4 [Laceration] na głównym celu (maks. 2)\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>jeżeli główny cel ma [BuffetScruple],</u></b></mark></color> traci 2 Wagi Ataku\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu\n[EndSkill] usuwa [BuffetScruple] głównego celu
144. [Umiejętność wroga [151708] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151708].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Umiejętność wroga [151708] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BoneNail] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151708].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Umiejętność wroga [151708] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [BoneNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151708].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [BoneNail]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [BoneNail] = 라브젝트(l'abject) / L'Abject
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [BoneNail]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [BoneNail]
147. [Umiejętność wroga [151708] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151708].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Umiejętność wroga [151708] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [BoneNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151708].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Umiejętność wroga [151708] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151708].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Umiejętność wroga [151708] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [BoneNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151708].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Umiejętność wroga [151709] (ulepszenie 1) — nazwa] 라 카스트라시옹(la castration)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151709].levelList[level=1].name
   limit: do 40 znaków
   EN: La Castration
   PL: La Castration
152. [Umiejętność wroga [151709] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>[BuffetDream]이 5 미만이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>메인 타겟에게 [BuffetScruple]이 있으면</u></b></mark></color>, 코인 위력 -3\n[WhenUse] 메인 타겟의 [Laceration] 4당, 최종 위력 +1 (최대 3)\n[DefeatDuel] 피해량 -95%, 이 스킬 피해로 대상이 흐트러지지 않고 <color=#ff6000><mark=#ff000040><b><u>[BuffetDream] 1 얻음</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151709].levelList[level=1].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [BuffetDream], [SuperCoin], [BuffetScruple], [Laceration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BuffetDream] = 뿌이의 기억 / Pwie's Memories; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BuffetScruple] = 뿌이와의 경험 / Shared with Pwie; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed\nCannot be Staggered before using this Skill\n\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>If this unit has fewer than 5 [BuffetDream], convert all Coins on this Skill to [SuperCoin]</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>If the main target has [BuffetScruple]</u></b></mark></color>, Coin Power -3\n[WhenUse] Final Power +1 for every 4 [Laceration] on the main target (max 3)\n[DefeatDuel] Deal -95% damage, damage dealt by this Skill cannot Stagger the target, <color=#ff6000><mark=#ff000040><b><u>and gain 1 [BuffetDream]</u></b></mark></color>
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>jeżeli ta jednostka ma mniej niż 5 [BuffetDream], wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>jeżeli główny cel ma [BuffetScruple],</u></b></mark></color> Moc Monety -3\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] na głównym celu (maks. 3)\n[DefeatDuel] zadaje -95% obrażeń, obrażenia z tej Umiejętności nie Oszołamiają celu, <color=#ff6000><mark=#ff000040><b><u>a zyskuje 1 [BuffetDream]</u></b></mark></color>
153. [Umiejętność wroga [151709] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151709].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Umiejętność wroga [151709] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151709].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Umiejętność wroga [151709] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151709].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Umiejętność wroga [151709] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151709].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Umiejętność wroga [151709] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151709].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [Umiejętność wroga [151709] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151709].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Activate [Laceration] on target once. Target loses 1 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] uruchamia [Laceration] na celu 1 raz. Cel traci 1 Licznika [Laceration]
159. [Umiejętność wroga [151709] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151709].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Umiejętność wroga [151709] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 2회 발동. 대상의 [Laceration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151709].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Activate [Laceration] on target 2 times. Target loses 2 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] uruchamia [Laceration] na celu 2 razy. Cel traci 2 Licznika [Laceration]
161. [Umiejętność wroga [151710] (ulepszenie 1) — nazwa] 르 트레튀네르(le trait unaire)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151710].levelList[level=1].name
   limit: do 40 znaków
   EN: Le Trait Unaire
   PL: Le Trait Unaire
162. [Umiejętność wroga [151710] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WhenUse] 모든 적이 보유한 <color=#ff6000><mark=#ff000040><b><u>[BoneNail]의 합 5당, 가중치 +1</u></b></mark></color> (최대 3)\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151710].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DuelCounter], [WhenUse], [Laceration], [BoneNail], [DefeatDuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BoneNail] = 라브젝트(l'abject) / L'Abject; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DuelCounter]\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>Gain +1 Atk Weight for every 5 total sum of [BoneNail] on all enemies</u></b></mark></color> (max 3)\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [DuelCounter]\n[WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>zyskuje Wagę Ataku +1 za każde 5 łącznej sumy [BoneNail] wszystkich wrogów</u></b></mark></color> (maks. 3)\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
163. [Umiejętność wroga [151710] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151710].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Umiejętność wroga [151710] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151710].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Umiejętność wroga [151710] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151710].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Umiejętność wroga [151710] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151710].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Umiejętność wroga [151710] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151710].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Umiejętność wroga [151710] (ulepszenie 1) — moneta 3, efekt 2 — opis] <color=#ff6000><mark=#ff000040><b><u>모든 적의 [BoneNail] 소모</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151710].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [BoneNail]
   znaczenie tagów: [BoneNail] = 라브젝트(l'abject) / L'Abject
   EN: <color=#ff6000><mark=#ff000040><b><u>Consume [BoneNail] on all enemies</u></b></mark></color>
   PL: <color=#ff6000><mark=#ff000040><b><u>zużywa [BoneNail] wszystkich wrogów</u></b></mark></color>
169. [Umiejętność wroga [151710] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 이 코인 최종 피해량 (소모한 [BoneNail] 수치x 5)%만큼 대상에게 색욕 피해
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151710].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BoneNail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BoneNail] = 라브젝트(l'abject) / L'Abject
   EN: [OnSucceedAttack] Deal Lust damage equal to ([BoneNail] Stack consumed x 5)% of this Coin's final damage
   PL: [OnSucceedAttack] zadaje obrażenia Żądzy równe (Stosy zużytego [BoneNail] x 5)% końcowych obrażeń tej Monety
170. [Umiejętność wroga [151710] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 소모한 [BoneNail] 4당, [Laceration] 1 횟수 증가 (최대 3)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151710].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BoneNail], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BoneNail] = 라브젝트(l'abject) / L'Abject; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count for every 4 [BoneNail] consumed (max 3)
   PL: [OnSucceedAttack] nakłada 1 Licznika [Laceration] za każde 4 zużyte [BoneNail] (maks. 3)
171. [Umiejętność wroga [151711] (ulepszenie 1) — nazwa] 데가제(Dégagé)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151711].levelList[level=1].name
   limit: do 40 znaków
   EN: Dégagé
   PL: Dégagé
172. [Umiejętność wroga [151711] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 2)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] 대상에게 [Laceration]이 없다면,</u></b></mark></color> 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151711].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Laceration], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] If target does not have [Laceration]</u></b></mark></color>, convert all Coins on this Skill to [SuperCoin]s\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Końcowa +1 za każde 4 [Laceration] celu (maks. 2)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] jeżeli cel nie ma [Laceration],</u></b></mark></color> wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
173. [Umiejętność wroga [151711] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [BoneNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151711].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BoneNail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BoneNail] = 라브젝트(l'abject) / L'Abject
   EN: [OnSucceedAttack] Inflict 1 [BoneNail]
   PL: [OnSucceedAttack] nakłada 1 [BoneNail]
174. [Umiejętność wroga [151711] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151711].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 1 Licznika [Laceration]
175. [Umiejętność wroga [151711] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [BoneNail] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151711].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [BoneNail]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [BoneNail] = 라브젝트(l'abject) / L'Abject
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [BoneNail]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [BoneNail]
176. [Umiejętność wroga [151712] (ulepszenie 1) — nazwa] 르 푸앵 드 카피통(le point de capiton)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151712].levelList[level=1].name
   limit: do 50 znaków
   EN: Le Point de Capiton
   PL: Le Point de Capiton
177. [Umiejętność wroga [151712] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 3)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] 대상에게 [Laceration]이 없다면,</u></b></mark></color> 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151712].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Laceration], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Final Power +1 for every 4 [Laceration] on target (max 3)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] If target does not have [Laceration]</u></b></mark></color>, convert all Coins on this Skill to [SuperCoin]s\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Końcowa +1 za każde 4 [Laceration] celu (maks. 3)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] jeżeli cel nie ma [Laceration],</u></b></mark></color> wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
178. [Umiejętność wroga [151712] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [BoneNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151712].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Umiejętność wroga [151712] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151712].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Umiejętność wroga [151712] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [BoneNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151712].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Umiejętność wroga [151712] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [BoneNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151712].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Umiejętność wroga [151712] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151712].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Umiejętność wroga [151712] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [BoneNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151712].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Umiejętność wroga [151713] (ulepszenie 1) — nazwa] 라 주이상스(la jouissance)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151713].levelList[level=1].name
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Umiejętność wroga [151713] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>메인 타겟에게 [BuffetScruple]이 있으면</u></b></mark></color>, 자신의 정신력 20 감소, 코인 위력 -3\n[DefeatDuel] <color=#ff6000><mark=#ff000040><b><u>[BuffetDream] 1 얻음</u></b></mark></color>. 피해량 -80%, 이 스킬 피해로 대상이 흐트러지지 않음\n[EndSkill] 메인 타겟의 [BuffetScruple]을 [BuffetResolve]으로 변경
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151713].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [BuffetScruple], [DefeatDuel], [BuffetDream], [EndSkill], [BuffetResolve]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BuffetScruple] = 뿌이와의 경험 / Shared with Pwie; [DefeatDuel] = [합 패배] / [Clash Lose]; [BuffetDream] = 뿌이의 기억 / Pwie's Memories; [EndSkill] = [공격 종료시] / [Attack End]; [BuffetResolve] = 결단 / Decision
   EN: Can Clash with this Skill regardless of Speed\n\n[WhenUse] If <color=#ff6000><mark=#ff000040><b><u>the main target has [BuffetScruple]</u></b></mark></color>, lose 20 SP and Coin Power -3\n[DefeatDuel] \n- <color=#ff6000><mark=#ff000040><b><u>Gain 1 [BuffetDream].</u></b></mark></color>\n- Deal -80% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] Convert [BuffetScruple] on the main target into [BuffetResolve]
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n\n[WhenUse] jeżeli <color=#ff6000><mark=#ff000040><b><u>główny cel ma [BuffetScruple]</u></b></mark></color>, traci 20 SP i Moc Monety -3\n[DefeatDuel]\n- <color=#ff6000><mark=#ff000040><b><u>zyskuje 1 [BuffetDream].</u></b></mark></color>\n- zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu\n[EndSkill] zamienia [BuffetScruple] głównego celu w [BuffetResolve]
186. [Umiejętność wroga [151713] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151713].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność wroga [151713] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151713].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Umiejętność wroga [151713] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151713].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Umiejętność wroga [151713] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151713].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Umiejętność wroga [151713] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151713].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Umiejętność wroga [151713] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151713].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [151713] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151713].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność wroga [151713] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 3회 발동. 대상의 [Laceration] 횟수 3 감소
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151713].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Umiejętność wroga [151714] (ulepszenie 1) — nazwa] 라 메타포르 파테르넬(la métaphore paternelle)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151714].levelList[level=1].name
   limit: do 50 znaków
   EN: La Métaphore Paternelle
   PL: La Métaphore Paternelle
195. [Umiejętność wroga [151714] (ulepszenie 1) — opis] [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\n이 스킬은 가장 마지막 순서에 사용\n[EndSkill] 자신의 최대 체력의 25% 만큼 체력 회복
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151714].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [SupportAlly], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [SupportAlly] = 양극성 / Duality; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\nThis Skill is used at the very end of the turn\n[EndSkill] Heal 25% HP
   PL: [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\nta Umiejętność jest używana na samym końcu tury\n[EndSkill] przywraca 25% HP
196. [Umiejętność wroga [151714] (ulepszenie 1) — moneta 1, efekt 1 — opis] [EndCoin] '붉은 신의 뜯긴 살점'을 다음 턴에 '르루주 고위 스태프'로 부활 시킴
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151714].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: [EndCoin] Revive "Ripped Flesh of the Crimson God" as "Le Rouge Senior Staff" next turn
   PL: [EndCoin] ożywia w następnej turze „Ripped Flesh of the Crimson God” jako „Le Rouge Senior Staff”
197. [Umiejętność wroga [151801] (ulepszenie 1) — nazwa] 거두어… 주세요…
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151801].levelList[level=1].name
   limit: do 40 znaków
   EN: Take Us In...
   PL: Take Us In...
198. [Umiejętność wroga [151801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [BuffetRevival] 1 감소
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BuffetRevival]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BuffetRevival] = 붉은 신의 목소리 / Voice of the Crimson God
   EN: [OnSucceedAttack] Lose 1 [BuffetRevival]
   PL: [OnSucceedAttack] traci 1 [BuffetRevival]
199. [Umiejętność wroga [151801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Umiejętność wroga [151802] (ulepszenie 1) — nazwa] 붉은… 목소리여…
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151802].levelList[level=1].name
   limit: do 40 znaków
   EN: Oh... Our Crimson Voice...
   PL: Oh... Our Crimson Voice...
201. [Umiejętność wroga [151802] (ulepszenie 1) — opis] 보호막이 있는 동안 피격 시 대상의 [Laceration] 횟수 1 증가\n[StartBattle] 최대 체력의 25%만큼 보호막을 얻음\n[EndBattle] 보호막이 있으면, 자신의 [BuffetRevival] 1 감소
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=151802].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [StartBattle], [EndBattle], [BuffetRevival]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [EndBattle] = [턴 종료 시] / [Turn End]; [BuffetRevival] = 붉은 신의 목소리 / Voice of the Crimson God
   EN: Inflict +1 [Laceration] Count against the attacker when hit as long as this unit has remaining shield\n[StartBattle] Gain Shield equal to 25% of this unit's max HP\n[EndBattle] If this unit has Shield, lose 1 [BuffetRevival]
   PL: przy trafieniu, dopóki ta jednostka ma Tarczę, nakłada 1 Licznika [Laceration] atakującemu\n[StartBattle] zyskuje Tarczę równą 25% Maks. HP tej jednostki\n[EndBattle] jeżeli ta jednostka ma Tarczę, traci 1 [BuffetRevival]
202. [Umiejętność wroga [152101] (ulepszenie 1) — nazwa] 이 낫으로 답하나이다!
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152101].levelList[level=1].name
   limit: do 60 znaków
   EN: With sickles mine I answer your calling!
   PL: With sickles mine I answer your calling!
203. [Umiejętność wroga [152101] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeRouge] 횟수 6 증가\n[WhenUse] 자신의 [ChargeRouge] 횟수가 10 이상이면, [ChargeRouge] 횟수를 5 소모하여 기본 위력 +2
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152101].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] Gain +6 [ChargeRouge] Count\n[WhenUse] At 10+ [ChargeRouge] Count, consume 5 [ChargeRouge] Count to gain Base Power +2
   PL: [WhenUse] zyskuje 6 Licznika [ChargeRouge]\n[WhenUse] przy 10+ Licznika [ChargeRouge] zużywa 5 Licznika [ChargeRouge], aby zyskać Moc Bazową +2
204. [Umiejętność wroga [152101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeRouge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRouge] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +2 [ChargeRouge] Count
   PL: [OnSucceedAttack] zyskuje 2 Licznika [ChargeRouge]
205. [Umiejętność wroga [152101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Umiejętność wroga [152102] (ulepszenie 1) — nazwa] 이 살을 받으소서!
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152102].levelList[level=1].name
   limit: do 40 znaków
   EN: Accept my offering of flesh!
   PL: Accept my offering of flesh!
207. [Umiejętność wroga [152102] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeRouge] 횟수 4 증가\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [ChargeRouge] 횟수가 10 이상이면, [ChargeRouge] 횟수를 10 소모하여 코인 위력 +1
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152102].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeRouge], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Gain +4 [ChargeRouge] Count\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[WhenUse] At 10+ [ChargeRouge] Count, consume 10 [ChargeRouge] Count to gain Coin Power +1
   PL: [WhenUse] zyskuje 4 Licznika [ChargeRouge]\n[WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1\n[WhenUse] przy 10+ Licznika [ChargeRouge] zużywa 10 Licznika [ChargeRouge], aby zyskać Moc Monety +1
208. [Umiejętność wroga [152102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Umiejętność wroga [152102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Umiejętność wroga [152102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Umiejętność wroga [152102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Umiejętność wroga [152103] (ulepszenie 1) — nazwa] 품에 안아 바치나이다!
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152103].levelList[level=1].name
   limit: do 40 znaków
   EN: An offering from my embrace!
   PL: An offering from my embrace!
213. [Umiejętność wroga [152103] (ulepszenie 1) — opis] [StartBattle] 자신의 현재 체력이 최대 체력의 50% 미만이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [ChargeRouge] 횟수가 10 이상이면, [ChargeRouge] 횟수를 10 소모하여 코인 위력 +1\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152103].levelList[level=1].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SuperCoin], [WhenUse], [Laceration], [ChargeRouge], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeRouge] = 맥동 / Pulsation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] If this unit has less than 50% HP, convert all Coins on this Skill to [SuperCoin]\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[WhenUse] At 10+ [ChargeRouge] Count, consume 10 [ChargeRouge] Count to gain Coin Power +1\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: [StartBattle] przy HP tej jednostki poniżej 50% Maks. HP, wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]\n[WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1\n[WhenUse] przy 10+ Licznika [ChargeRouge] zużywa 10 Licznika [ChargeRouge], aby zyskać Moc Monety +1\n[DefeatDuel] obrażenia z tej Umiejętności nie Oszołamiają celu
214. [Umiejętność wroga [152103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Umiejętność wroga [152103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Umiejętność wroga [152103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Umiejętność wroga [152103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Umiejętność wroga [152103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 Licznika [Laceration]
219. [Umiejętność wroga [152103] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152103].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność wroga [152104] (ulepszenie 1) — nazwa] 남김없이 먹어치우겠나이다!
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152104].levelList[level=1].name
   limit: do 40 znaków
   EN: We shall devour it all!
   PL: We shall devour it all!
221. [Umiejętność wroga [152104] (ulepszenie 1) — opis] [StartBattle] 자신의 현재 체력이 최대 체력의 50% 미만이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [ChargeRouge] 횟수가 10 이상이면, [ChargeRouge] 횟수를 10 소모하여 코인 위력 +1\n[WinDuel] 자신의 [ChargeRouge] 횟수 10 증가\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152104].levelList[level=1].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SuperCoin], [WhenUse], [Laceration], [ChargeRouge], [WinDuel], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeRouge] = 맥동 / Pulsation; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] If this unit has less than 50% HP, convert all Coins on this Skill to [SuperCoin]\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[WhenUse] At 10+ [ChargeRouge] Count, consume 10 [ChargeRouge] Count to gain Coin Power +1\n[WinDuel] Gain +10 [ChargeRouge] Count\n[DefeatDuel] Deal -80% damage; damage dealt by this Skill cannot Stagger the target
   PL: [StartBattle] przy HP tej jednostki poniżej 50% Maks. HP, wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]\n[WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1\n[WhenUse] przy 10+ Licznika [ChargeRouge] zużywa 10 Licznika [ChargeRouge], aby zyskać Moc Monety +1\n[WinDuel] zyskuje 10 Licznika [ChargeRouge]\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
222. [Umiejętność wroga [152104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Laceration]
223. [Umiejętność wroga [152104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [ChargeRouge] 횟수를 최대 5 소모하고, 최종 피해의 (소모한 수치 x 3)%만큼 참격 피해 (최대 15%)\n- 최대 체력의 (소모한 수치)%만큼 체력 회복
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [UnBrokenCoinOnSucceedAttack], [ChargeRouge]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ChargeRouge] = 맥동 / Pulsation
   EN: [UnBrokenCoinOnSucceedAttack] Consume up to 5 [ChargeRouge] Count to deal Slash damage equal to ([ChargeRouge] Count consumed x 3)% of this Coin's final damage (max 15%)\n- Heal ([ChargeRouge] Count consumed)% HP
   PL: [UnBrokenCoinOnSucceedAttack] zużywa do 5 Licznika [ChargeRouge], zadając obrażenia Cięcia równe (zużyte Liczniki [ChargeRouge] x 3)% końcowych obrażeń tej Monety (maks. 15%)\n- przywraca HP równe (zużyte Liczniki [ChargeRouge])%
224. [Umiejętność wroga [152104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Umiejętność wroga [152104] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [ChargeRouge] 횟수를 최대 5 소모하고, 최종 피해의 (소모한 수치 x 3)%만큼 참격 피해 (최대 15%)\n- 최대 체력의 (소모한 수치)%만큼 체력 회복
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152104].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność wroga [152104] (ulepszenie 1) — moneta 3, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152104].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność wroga [152104] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [ChargeRouge] 횟수를 최대 5 소모하고, 최종 피해의 (소모한 수치 x 3)%만큼 참격 피해 (최대 15%)\n- 최대 체력의 (소모한 수치)%만큼 체력 회복
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152104].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
228. [Umiejętność wroga [152104] (ulepszenie 1) — moneta 4, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152104].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Umiejętność wroga [152104] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152104].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Umiejętność wroga [152105] (ulepszenie 1) — nazwa] 아직 눕지 않나이다!
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152105].levelList[level=1].name
   limit: do 50 znaków
   EN: We shan't yet be laid to rest!
   PL: We shan't yet be laid to rest!
231. [Umiejętność wroga [152105] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 자신의 [ChargeRouge] 횟수 5당, 최종 위력 +1 (최대 3)\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152105].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [ChargeRouge], [Laceration]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation; [Laceration] = 출혈 / Bleed
   EN: [DuelCounter]\n[WhenUse] Final Power +1 for every 5 [ChargeRouge] Count on self (max 3)\n[WhenUse] If target has 6+ [Laceration], Coin Power +1
   PL: [DuelCounter]\n[WhenUse] Moc Końcowa +1 za każde 5 Liczników [ChargeRouge] tej jednostki (maks. 3)\n[WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1
232. [Umiejętność wroga [152105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeRouge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRouge] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +3 [ChargeRouge] Count
   PL: [OnSucceedAttack] zyskuje 3 Licznika [ChargeRouge]
233. [Umiejętność wroga [152105] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152105].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Umiejętność wroga [152105] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152105].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność wroga [152106] (ulepszenie 1) — nazwa] 목소리를 향한 예배
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152106].levelList[level=1].name
   limit: do 50 znaków
   EN: Supplication Toward the Voice
   PL: Supplication Toward the Voice
236. [Umiejętność wroga [152106] (ulepszenie 1) — opis] [CantDuel]\n[CantChangeTarget]\n붉은 신을 타겟으로 지정\n\n이 스킬은 아래 효과가 적용됨\n- 수비 스킬을 발동시키지 않음\n- 외부 효과로 재사용할 수 없음\n- 공격이 적중하지 않음\n\n[EndCoin] 대상의 정신력 20 회복
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152106].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [EndCoin]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: [CantDuel]\n[CantChangeTarget]\nTargets The Crimson God\n\nThis Skill has the following properties:\n- Does not trigger Defense Skills\n- External effects cannot trigger this Skill to be Reused\n- Its attack does not hit\n\n[EndCoin] Target heals 20 SP
   PL: [CantDuel]\n[CantChangeTarget]\npriorytet: The Crimson God\n\nta Umiejętność ma następujące właściwości:\n- nie uruchamia Umiejętności obrony\n- zewnętrzne efekty nie mogą wywołać ponownego użycia tej Umiejętności\n- jej atak nie trafia\n\n[EndCoin] przywraca celowi 20 SP

## [a1c10p3] Pasywka wroga: Passives_Abnormality-a1c10p3
- plik gry: `Passives_Abnormality-a1c10p3.json`

237. [[a1c10p3] Pasywka wroga [148511] — nazwa] …불가능하다!
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148511].name
   limit: do 40 znaków
   EN: ... Impossible!
   PL: ... Impossible!
238. [[a1c10p3] Pasywka wroga [148511] — opis] 스테이지 시작 시, 뫼르소가 [MeursaultBuffWarderFirstPhase] 얻음\n\n턴 시작 시, [GoldenHideWarderFirstPhase]과 [GoldenFabricWarderFirstPhase]가 무작위 수감자에게 부여됨
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148511].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [MeursaultBuffWarderFirstPhase], [GoldenHideWarderFirstPhase], [GoldenFabricWarderFirstPhase]
   znaczenie tagów: [MeursaultBuffWarderFirstPhase] = 이방인 / The Stranger; [GoldenHideWarderFirstPhase] = 박동 / Thumping Pulse; [GoldenFabricWarderFirstPhase] = 정지 / Stillness
   EN: Encounter Start: Meursault gains [MeursaultBuffWarderFirstPhase]\n\nTurn Start: Random Sinners gain [GoldenHideWarderFirstPhase] and [GoldenFabricWarderFirstPhase]
   PL: Na początku etapu: Meursault zyskuje [MeursaultBuffWarderFirstPhase]\n\nPoczątek tury: losowi Grzesznicy zyskują [GoldenHideWarderFirstPhase] i [GoldenFabricWarderFirstPhase]
239. [[a1c10p3] Pasywka wroga [148511] — tekst klimatyczny] “그 정지와 변화의 표상은… 신의 권능일 터…!”
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148511].flavor
   limit: do 120 znaków
   EN: "That which betokeneth stillness and change... is reserved for none but God...!!"
   PL: "That which betokeneth stillness and change... is reserved for none but God...!!"
240. [[a1c10p3] Pasywka wroga [148511] — podsumowanie] 뫼르소가 [MeursaultBuffWarderFirstPhase] 얻음\n매 턴 무작위 수감자에게 [GoldenHideWarderFirstPhase], [GoldenFabricWarderFirstPhase] 부여
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148511].summary
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [MeursaultBuffWarderFirstPhase], [GoldenHideWarderFirstPhase], [GoldenFabricWarderFirstPhase]
   znaczenie tagów: [MeursaultBuffWarderFirstPhase] = 이방인 / The Stranger; [GoldenHideWarderFirstPhase] = 박동 / Thumping Pulse; [GoldenFabricWarderFirstPhase] = 정지 / Stillness
   EN: Meursault gains [MeursaultBuffWarderFirstPhase]\nRandom Sinners gain [GoldenHideWarderFirstPhase] and [GoldenFabricWarderFirstPhase] every turn
   PL: Meursault zyskuje [MeursaultBuffWarderFirstPhase]\nco turę losowi Grzesznicy zyskują [GoldenHideWarderFirstPhase] i [GoldenFabricWarderFirstPhase]
241. [[a1c10p3] Pasywka wroga [148501] — nazwa] 신의 대리인
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148501].name
   limit: do 40 znaków
   EN: Vicarius Dei
   PL: Vicarius Dei
242. [[a1c10p3] Pasywka wroga [148501] — opis] [PanicChangeLock] 효과가 적용되며,\n턴 종료 시 패닉 상태면 정신력이 30으로 변경됨\n\n스테이지 시작 시,\n- 체력이 50%인 상태로 시작\n- [UnstableConnection] 2 얻음\n\n세 번째 턴이 되면 강력한 스킬을 사용\n- 해당 턴 동안 수감자에게 피격 시, [ParryingResultDown] 1 얻음 (수감자별 1회)\n\n체력이 1 이하가 되거나 세 번째 턴이 종료되면, 페이즈 변경
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148501].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [PanicChangeLock], [UnstableConnection], [ParryingResultDown]
   znaczenie tagów: [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic; [UnstableConnection] = 불안정한 현현 / Precarious Theophany; [ParryingResultDown] = 합 위력 감소 / Clash Power Down
   EN: Apply the [PanicChangeLock] effect\nTurn End: If this unit is in Panic, change SP to 30\n\nEncounter Start:\n- Begin with 50% HP\n- Gain 2 [UnstableConnection]\n\nOn Turn 3, use a powerful Skill\n- During that turn, when hit by a Sinner, gain 1 [ParryingResultDown] (once per Sinner)\n\nWhen this unit's HP drops to 1 or below, or at the end of the turn 3, enter a new Phase
   PL: stosuje efekt [PanicChangeLock]\nKoniec tury: jeżeli ta jednostka jest w Panice, jej SP wynosi 30\n\nNa początku etapu:\n- rozpoczyna z 50% HP\n- zyskuje 2 [UnstableConnection]\n\nw turze 3 używa potężnej Umiejętności\n- podczas tej tury, przy trafieniu przez Grzesznika, zyskuje 1 [ParryingResultDown] (1 raz na Grzesznika)\n\ngdy HP tej jednostki spadnie do 1 lub poniżej albo po zakończeniu tury 3, zmienia Fazę
243. [[a1c10p3] Pasywka wroga [148501] — tekst klimatyczny] 길에서 벗어난 자들을 단죄하는 검은 신의 대리인.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148501].flavor
   limit: do 120 znaków
   EN: The Vicar of the Obsidian God who visits punishment upon those who have gone astray.
   PL: Namiestnik Obsydianowego Boga, wymierzający karę tym, którzy zeszli z drogi.
244. [[a1c10p3] Pasywka wroga [148501] — podsumowanie] 세 번째 턴에 강력한 스킬 사용\n세 번째 턴 종료 시 페이즈 변경
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148501].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use a powerful Skill on Turn 3\nChange the phase at the end of Turn 3
   PL: używa potężnej Umiejętności w turze 3\nzmienia Fazę po zakończeniu tury 3
245. [[a1c10p3] Pasywka wroga [148502] — nazwa] 신성형벌촛대
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148502].name
   limit: do 50 znaków
   EN: Hallowed Candles of Retribution
   PL: Hallowed Candles of Retribution
246. [[a1c10p3] Pasywka wroga [148502] — opis] 턴 시작 시, <color=#ff6000><mark=#ff000040><b><u>형벌 촛대 둘을 소환함</u></b></mark></color>\n- 턴이 지날 때마다 턴 시작 시 소환하는 <color=#ff6000><mark=#ff000040><b><u>형벌 촛대 수 +1</u></b></mark></color>\n- 형벌 촛대는 전장에 최대 4개까지 존재할 수 있음\n\n전장의 형벌 촛대가 파괴될 때마다 간수가 [Vulnerable] 1 얻음\n\n스킬 사용 시\n- 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>속도가 1</u></b></mark></color>이면, 해당 스킬의 <color=#ff6000><mark=#ff000040><b><u>모든 코인이\n[SuperCoin]으로 변경되고 최종 위력 +2, 피해량 +100%</u></b></mark></color>\n- 전장에 형벌 촛대가 없으면, 합 위력 -1
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148502].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Vulnerable], [SuperCoin]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Turn Start: <color=#ff6000><mark=#ff000040><b><u>Summon 2 Candle of Retribution</u></b></mark></color>\n- Summon <color=#ff6000><mark=#ff000040><b><u>+1 more Candle of Retribution</u></b></mark></color> at Turn Start with every passing turn\n- Up to 4 Candles of Retribution can exist simultaneously on the field\n\nEvery time a Candle of Retribution is destroyed, the Warden gains 1 [Vulnerable]\n\nOn Skill Use:\n- <color=#ff6000><mark=#ff000040><b><u>If the main target has 1 Speed, convert all Coins on this unit's Skill into [SuperCoin]s, gain Final Power +2, and deal +100% damage</u></b></mark></color>\n- If there are no Candles of Retribution on the field, Clash Power -1
   PL: Początek tury: <color=#ff6000><mark=#ff000040><b><u>przywołuje 2 Candle of Retribution</u></b></mark></color>\n- z każdą kolejną turą przywołuje na początku tury <color=#ff6000><mark=#ff000040><b><u>+1 więcej Candle of Retribution</u></b></mark></color>\n- na polu może istnieć maks. 4 Candle of Retribution\n\nza każdym razem, gdy Candle of Retribution zostanie zniszczone, The Warden zyskuje 1 [Vulnerable]\n\nprzy użyciu Umiejętności:\n- jeżeli główny cel ma <color=#ff6000><mark=#ff000040><b><u>Szybkość 1</u></b></mark></color>, wszystkie Monety Umiejętności tej jednostki\nzamieniają się w [SuperCoin]y, Moc Końcowa +2, zadaje +100% obrażeń\n- jeżeli na polu nie ma Candle of Retribution, Moc Starcia -1
247. [[a1c10p3] Pasywka wroga [148502] — tekst klimatyczny] 백화점의 운명을 거스르는 죄인들의 위로 떨어지는 촛대.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148502].flavor
   limit: do 130 znaków
   EN: The candle that smites those sinful ones who dare defy the fate allotted by the department store.
   PL: Świeca, która spada na grzeszników ośmielających się przeciwstawić losowi wyznaczonemu przez dom towarowy.
248. [[a1c10p3] Pasywka wroga [148502] — podsumowanie] 매 턴 형벌 촛대 소환, 파괴 시 [Vulnerable] 얻음\n메인 타겟의 속도가 1이면, 스킬 강화
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148502].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Summon Candle of Retribution every turn, gain [Vulnerable] when Candle is destroyed\nIf the main target has 1 Speed, strengthen the Skill
   PL: przywołuje Candle of Retribution co turę, zyskuje [Vulnerable] gdy Candle zostanie zniszczone\njeżeli główny cel ma Szybkość 1, wzmacnia Umiejętność
249. [[a1c10p3] Pasywka wroga [148503] — nazwa] 눈물은 천을 적시고
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148503].name
   limit: do 40 znaków
   EN: Tears shall soak the cloth
   PL: Tears shall soak the cloth
250. [[a1c10p3] Pasywka wroga [148503] — opis] <color=#ff6000><mark=#ff000040><b><u>[Sinking] 효과로 자신의 정신력이 감소하지 않는 대신</u></b></mark></color>,\n그 수치만큼 우울 피해를 받음\n\n수감자에게 피격 시, 대상 수감자의 [Sinking] 횟수 1 증가\n(수감자별 턴당 최대 2)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148503].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: <color=#ff6000><mark=#ff000040><b><u>This unit does not lose SP from [Sinking] effects</u></b></mark></color>; instead, when [Sinking] effects trigger, this unit takes Gloom damage equal to Sinking Potency\n\nWhen hit by a Sinner, the said Sinner gains +1 [Sinking] Count (2 per turn per Sinner)
   PL: <color=#ff6000><mark=#ff000040><b><u>ta jednostka nie traci SP z powodu efektów [Sinking]</u></b></mark></color>; zamiast tego, gdy efekt [Sinking] się uruchamia, otrzymuje obrażenia Posępności równe Siły Zatonięcia\n\nprzy trafieniu przez Grzesznika, ten Grzesznik zyskuje 1 Licznika [Sinking] (maks. 2 na turę na Grzesznika)
251. [[a1c10p3] Pasywka wroga [148503] — podsumowanie] [Sinking]으로 정신력 감소 대신 우울 피해를 받음\n피격 시 공격자의 [Sinking] 횟수 증가
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148503].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Take Gloom damage from [Sinking] instead of losing SP\nWhen hit, the attacker gains [Sinking] Count
   PL: otrzymuje obrażenia Posępności z [Sinking] zamiast tracić SP\nprzy trafieniu atakujący zyskuje Licznik [Sinking]
252. [[a1c10p3] Pasywka wroga [148504] — nazwa] 완벽 보존
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148504].name
   limit: do 40 znaków
   EN: Perfect Conservation
   PL: Perfect Conservation
253. [[a1c10p3] Pasywka wroga [148504] — opis] 전투 중 누적으로 자신의 [ChargeNoir] 횟수를\n10 소모할 때마다 [ChargeNoir] 위력 1 얻음\n\n턴 시작 시 자신의 [ChargeNoir] 위력이 3, [ChargeNoir] 횟수가 10 미만이면,\n자신의 [ChargeNoir] 횟수 5 증가\n\n[ChargeNoir]의 턴 종료 시 횟수 1이 감소하는 효과가 발동하지 않음
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148504].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: Gain 1 [ChargeNoir] Potency for every 10 cumulative [ChargeNoir] Count this unit consumes in this Encounter\n\nTurn Start: At fewer than 3 [ChargeNoir] Potency and fewer than 10 [ChargeNoir] Count, gain +5 [ChargeNoir] Count\n\nThe "Turn End: Lose 1 Count" effect on [ChargeNoir] does not trigger
   PL: zyskuje 1 Siły [ChargeNoir] za każde 10 łącznie zużytych Liczników [ChargeNoir] tej jednostki w tej walce\n\nPoczątek tury: jeżeli Siła [ChargeNoir] tej jednostki jest niższa niż 3, a Liczniki [ChargeNoir] niższe niż 10, zyskuje 5 Licznika [ChargeNoir]\n\nefekt [ChargeNoir] „Koniec tury: traci 1 Licznika” się nie uruchamia
254. [[a1c10p3] Pasywka wroga [148504] — tekst klimatyczny] 시지프 시스템적으로 이 보존은 완벽하게 보존된다.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148504].flavor
   limit: do 120 znaków
   EN: Within the Sisyphe System, conservation itself is preserved perfectly.
   PL: W Systemie Sisyphe ta konserwacja jest konserwowana w sposób doskonały.
255. [[a1c10p3] Pasywka wroga [148504] — podsumowanie] [ChargeNoir] 횟수를 누적 소모하면 [ChargeNoir] 위력 얻음\n[ChargeNoir] 횟수가 턴 종료 시 감소하지 않음
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148504].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: Gain [ChargeNoir] Potency when consuming [ChargeNoir] Count cumulatively\n[ChargeNoir] Count is not lost at Turn End
   PL: zyskuje Siłę [ChargeNoir] przy łącznym zużyciu Liczników [ChargeNoir]\nLiczniki [ChargeNoir] nie maleją na Koniec tury
256. [[a1c10p3] Pasywka wroga [152001] — nazwa] 형벌적 구속
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152001].name
   limit: do 40 znaków
   EN: Chastening Bonds
   PL: Chastening Bonds
257. [[a1c10p3] Pasywka wroga [152001] — opis] 턴 종료 시 다음 턴에 모든 수감자에게 <color=#ff6000><mark=#ff000040><b><u>[Binding] 2</u></b></mark></color> 부여\n- 페이즈가 넘어가면 이 효과는 적용되지 않음
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152001].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Turn End: Inflict <color=#ff6000><mark=#ff000040><b><u>2 [Binding]</u></b></mark></color> next turn on all Sinners\n- This effect does not trigger after Phase change
   PL: Koniec tury: nakłada w następnej turze <color=#ff6000><mark=#ff000040><b><u>2 [Binding]</u></b></mark></color> na wszystkich Grzeszników\n- ten efekt nie uruchamia się po zmianie Fazy
258. [[a1c10p3] Pasywka wroga [152001] — tekst klimatyczny] 죄인은 묶이라.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152001].flavor
   limit: do 120 znaków
   EN: Let the sinful one be bound.
   PL: Niech grzesznik będzie związany.
259. [[a1c10p3] Pasywka wroga [152001] — podsumowanie] 다음 턴에 모든 수감자에게 [Binding] 부여
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152001].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Inflict [Binding] on all Sinners next turn
   PL: nakłada [Binding] na wszystkich Grzeszników w następnej turze
260. [[a1c10p3] Pasywka wroga [152002] — nazwa] 피어오르는 죄악
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152002].name
   limit: do 40 znaków
   EN: Sin Aflame
   PL: Sin Aflame
261. [[a1c10p3] Pasywka wroga [152002] — opis] 수감자 스킬에 의해 서브 타겟으로 지정되었을 때,\n해당 스킬로 받는 피해량 -50%\n\n사망 시,\n- 모든 속성 E.G.O 자원 +1\n- 자신을 가장 마지막에 공격한 수감자의 정신력을 5만큼 회복\n· 해당 수감자에게 [Binding]이 있으면, 대신 10만큼 회복\n· 효과 적용 대상을 판별할 수 없으면, 대신 정신력이 가장 낮은 수감자에게 효과 발동
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152002].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: When this unit is sub-targeted by a Sinner's Skill, take -50% damage from the said Skill\n\nUpon defeat:\n- Give 1 E.G.O resource for all Affinities\n- The last Sinner to attack this unit heals 5 SP\n  · If the said Sinner has [Binding], heal 10 SP instead\n  · If the "last Sinner" to attack this unit cannot be determined, above effects activate for the Sinner that has the lowest SP
   PL: gdy ta jednostka zostanie wskazana jako cel dodatkowy Umiejętności Grzesznika, otrzymuje -50% obrażeń od tej Umiejętności\n\npo śmierci:\n- daje 1 zasób E.G.O dla wszystkich Afinności\n- ostatni Grzesznik, który zaatakował tę jednostkę, przywraca 5 SP\n  · jeżeli ten Grzesznik ma [Binding], zamiast tego przywraca 10 SP\n  · jeżeli nie można ustalić ostatniego Grzesznika, efekty uruchamiają się na Grzeszniku z najniższym SP
262. [[a1c10p3] Pasywka wroga [152002] — podsumowanie] 서브 타겟일 때 받는 피해량 감소\n사망 시, E.G.O 자원 획득, 공격자 정신력 회복
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152002].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Take less damage when sub-targeted\nOn death, give E.G.O resource; heal attacker's SP
   PL: otrzymuje mniej obrażeń jako cel dodatkowy\npo śmierci daje zasób E.G.O; przywraca SP atakującemu
263. [[a1c10p3] Pasywka wroga [148611] — nazwa] …불가능하다!
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148611].name
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [[a1c10p3] Pasywka wroga [148611] — opis] 턴 시작 시, [GoldenHideWarderSecondPhase]과 [GoldenFabricWarderSecondPhase]가 무작위 수감자에게 부여됨
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148611].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [GoldenHideWarderSecondPhase], [GoldenFabricWarderSecondPhase]
   znaczenie tagów: [GoldenHideWarderSecondPhase] = 박동 / Thumping Pulse; [GoldenFabricWarderSecondPhase] = 정지 / Stillness
   EN: Turn Start: Random Sinners gain [GoldenHideWarderSecondPhase] and [GoldenFabricWarderSecondPhase]
   PL: Początek tury: losowi Grzesznicy zyskują [GoldenHideWarderSecondPhase] i [GoldenFabricWarderSecondPhase]
265. [[a1c10p3] Pasywka wroga [148611] — tekst klimatyczny] “그 정지와 변화의 표상은… 신의 권능일 터…!”
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148611].flavor
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [[a1c10p3] Pasywka wroga [148611] — podsumowanie] 매 턴 무작위 수감자에게 [GoldenHideWarderSecondPhase], [GoldenFabricWarderSecondPhase] 부여
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148611].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [GoldenHideWarderSecondPhase], [GoldenFabricWarderSecondPhase]
   znaczenie tagów: [GoldenHideWarderSecondPhase] = 박동 / Thumping Pulse; [GoldenFabricWarderSecondPhase] = 정지 / Stillness
   EN: Random Sinners gain [GoldenHideWarderSecondPhase] and [GoldenFabricWarderSecondPhase] every turn
   PL: co turę losowi Grzesznicy zyskują [GoldenHideWarderSecondPhase] i [GoldenFabricWarderSecondPhase]
267. [[a1c10p3] Pasywka wroga [148605] — nazwa] 고해 도구
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148605].name
   limit: do 40 znaków
   EN: Implements of Confession
   PL: Implements of Confession
268. [[a1c10p3] Pasywka wroga [148605] — opis] 간수가 자신의 스킬 효과로 수감자에게 [ConfessionSecondPhase]를 부여할 때,\n다음의 효과가 적용됨\n- [RestrainingNailSecondPhase], [ExecutionNailSecondPhase], [CeremonialNail], [MarkingNail]를 아울러 <color=#ff6000><mark=#ff000040><b><u>[ConfessionSecondPhase]로 지칭</u></b></mark></color>함\n- 간수가 수감자에게 못이나 망치 못을 부여할 때, <color=#ff6000><mark=#ff000040><b><u>제일 마지막에 부여한 효과로 적용</u></b></mark></color>시키고 수치는 합산함\n- <color=#ff6000><mark=#ff000040><b><u>망치 못은 못으로 변경되지 않음</u></b></mark></color>\n\n수감자에게 공격 적중 시, 대상 수감자가 보유한 <color=#ff6000><mark=#ff000040><b><u>[ConfessionSecondPhase] 1당\n피해량 +3%</u></b></mark></color> (최대 27%, 대상별로 적용)\n\n턴 시작 시 간수의 <color=#ff6000><mark=#ff000040><b><u>체력이 50% 이하</u></b></mark></color>면,\n스킬로 부여하는 모든 <color=#ff6000><mark=#ff000040><b><u>[ConfessionSecondPhase] 부여량 +1</u></b></mark></color>
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148605].desc
   limit: do 950 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ConfessionSecondPhase], [RestrainingNailSecondPhase], [ExecutionNailSecondPhase], [CeremonialNail], [MarkingNail], [TabExplain]
   znaczenie tagów: [ConfessionSecondPhase] = 고해의 증거 / Proof of Confession; [RestrainingNailSecondPhase] = 망치 못[단죄] / Hammernail [Condemnation]; [ExecutionNailSecondPhase] = 망치 못[심판] / Hammernail [Judgment]; [CeremonialNail] = 못[형벌] / Nail [Punishment]; [MarkingNail] = 못[속죄] / Nail [Penance]
   EN: When the Warden inflicts [ConfessionSecondPhase] on Sinners using its Skill effects, apply the following:\n- The following effects are <color=#ff6000><mark=#ff000040><b><u>collectively referred to as [ConfessionSecondPhase]:</u></b></mark></color>\n  · [RestrainingNailSecondPhase]\n  · [ExecutionNailSecondPhase]\n  · [CeremonialNail]\n  · [MarkingNail]\n- When the Warden inflicts Nail[TabExplain] or Hammernail on the Sinners, <color=#ff6000><mark=#ff000040><b><u>only the effect that is inflicted last remains</u></b></mark></color>; however, Stacks between Nail[TabExplain] and Hammernail accumulate\n- <color=#ff6000><mark=#ff000040><b><u>Hammernail does not convert into Nail[TabExplain]</u></b></mark></color>\n\nOn Hit against a Sinner, <color=#ff6000><mark=#ff000040><b><u>deal +3% damage for every [ConfessionSecondPhase] on target</u></b></mark></color> (max 27%, separately for each target)\n\nTurn Start: <color=#ff6000><mark=#ff000040><b><u>If the Warden has 50% or lower HP</u></b></mark></color>, all Skills inflict <color=#ff6000><mark=#ff000040><b><u>+1 more [ConfessionSecondPhase]</u></b></mark></color>
   PL: gdy The Warden nakłada [ConfessionSecondPhase] na Grzeszników efektami swoich Umiejętności, stosuje się:\n- następujące efekty są <color=#ff6000><mark=#ff000040><b><u>łącznie nazywane [ConfessionSecondPhase]:</u></b></mark></color>\n  · [RestrainingNailSecondPhase]\n  · [ExecutionNailSecondPhase]\n  · [CeremonialNail]\n  · [MarkingNail]\n- gdy The Warden nakłada Nail[TabExplain] lub Hammernail na Grzeszników, <color=#ff6000><mark=#ff000040><b><u>pozostaje wyłącznie ostatnio nałożony efekt</u></b></mark></color>; Stosy między Nail[TabExplain] a Hammernail sumują się\n- <color=#ff6000><mark=#ff000040><b><u>Hammernail nie zamienia się w Nail[TabExplain]</u></b></mark></color>\n\nprzy trafieniu Grzesznika <color=#ff6000><mark=#ff000040><b><u>zadaje +3% obrażeń za każdą 1 [ConfessionSecondPhase] celu</u></b></mark></color> (maks. 27%, osobno dla każdego celu)\n\nPoczątek tury: <color=#ff6000><mark=#ff000040><b><u>jeżeli HP The Warden wynosi 50% lub mniej</u></b></mark></color>, wszystkie Umiejętności nakładają <color=#ff6000><mark=#ff000040><b><u>dodatkowo +1 [ConfessionSecondPhase]</u></b></mark></color>
269. [[a1c10p3] Pasywka wroga [148605] — podsumowanie] 대상의 [ConfessionSecondPhase]에 따라 피해량 증가\n체력 50% 이하면 [ConfessionSecondPhase] 부여량 증가
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148605].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [ConfessionSecondPhase]
   znaczenie tagów: [ConfessionSecondPhase] = 고해의 증거 / Proof of Confession
   EN: Deal more damage based on [ConfessionSecondPhase] on target\nAt 50%- HP, inflict more [ConfessionSecondPhase]
   PL: zadaje więcej obrażeń zależnie od [ConfessionSecondPhase] celu\nprzy HP tej jednostki 50% lub mniej nakłada więcej [ConfessionSecondPhase]
270. [[a1c10p3] Pasywka wroga [148601] — nazwa] 보존의 규율대로
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148601].name
   limit: do 60 znaków
   EN: As Ordained by the Rule of Conservation
   PL: As Ordained by the Rule of Conservation
271. [[a1c10p3] Pasywka wroga [148601] — opis] [PanicChangeLock] 효과가 적용되며,\n턴 종료 시 패닉 상태면 정신력이 30으로 변경됨\n\n등장 이후 첫 턴 시작 시,\n- 정신력이 45로 변경됨\n- [EncompassingVoiceSecondPhase] 0, [LeaderVoiceSecondPhase] 1 얻음\n- 직전 페이즈의 [ChargeNoir] 위력과 횟수가 그대로 유지됨
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148601].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [PanicChangeLock], [EncompassingVoiceSecondPhase], [LeaderVoiceSecondPhase], [ChargeNoir]
   znaczenie tagów: [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic; [EncompassingVoiceSecondPhase] = 검은 신의 목소리 / Voice of the Obsidian God; [LeaderVoiceSecondPhase] = 시지프 형벌의 간수 / Warden of the Sisyphe Penalty; [ChargeNoir] = 보존 / Preservation
   EN: Apply the [PanicChangeLock] effect\nTurn End: If this unit is in Panic, change SP to 30\n\nFirst Turn Start after entry:\n- Change SP to 45\n- Gain 0 [EncompassingVoiceSecondPhase] and 1 [LeaderVoiceSecondPhase]\n- [ChargeNoir] Potency and Count carry over from the preceding Phase
   PL: stosuje efekt [PanicChangeLock]\nKoniec tury: jeżeli ta jednostka jest w Panice, jej SP wynosi 30\n\nna pierwszym Początku tury po pojawieniu się:\n- SP zmienia się na 45\n- zyskuje 0 [EncompassingVoiceSecondPhase] i 1 [LeaderVoiceSecondPhase]\n- Siła i Liczniki [ChargeNoir] dziedziczone z poprzedniej Fazy
272. [[a1c10p3] Pasywka wroga [148601] — podsumowanie] [PanicChangeLock]\n직전 페이즈의 [ChargeNoir] 위력, 횟수 유지
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148601].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [PanicChangeLock], [ChargeNoir]
   znaczenie tagów: [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic; [ChargeNoir] = 보존 / Preservation
   EN: [PanicChangeLock]\n[ChargeNoir] Potency and Count carry over from the preceding Phase
   PL: [PanicChangeLock]\nSiła i Liczniki [ChargeNoir] dziedziczone z poprzedniej Fazy
273. [[a1c10p3] Pasywka wroga [148602] — nazwa] 심판의 날
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148602].name
   limit: do 40 znaków
   EN: Dies Irae
   PL: Dies Irae
274. [[a1c10p3] Pasywka wroga [148602] — opis] 턴 시작 시 [SpreadingVoiceSecondPhase]이 있으면,\n패턴이 변경되고 <color=#ff6000><mark=#ff000040><b><u>강력한 스킬 ‘심판…! 선고…! 단죄…!’</u></b></mark></color>를 사용\n- 해당 턴에 속도 최솟값, 최댓값 +20\n- <color=#ff6000><mark=#ff000040><b><u>이 패턴에서 간수가 합 패배</u></b></mark></color> 시,\n다음 턴에 패턴이 추가로 변경되고 <color=#ff6000><mark=#ff000040><b><u>강력한 스킬 ‘사형 집행’</u></b></mark></color>을 사용\n\n[SpreadingVoiceSecondPhase]/[EncompassingVoiceSecondPhase]가 변경될 때마다\n<color=#ff6000><mark=#ff000040><b><u>정신력이 45만큼 회복</u></b></mark></color>되고 <color=#ff6000><mark=#ff000040><b><u>[LeaderVoiceSecondPhase] 1 얻음</u></b></mark></color>\n\n체력이 50% 이하가 되면,\n해당 턴을 종료(특정 스킬 제외)하고 흐트러짐 상태면 흐트러짐 해제됨\n체력이 1 이하가 되면, 페이즈 변경
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148602].desc
   limit: do 750 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [SpreadingVoiceSecondPhase], [EncompassingVoiceSecondPhase], [LeaderVoiceSecondPhase]
   znaczenie tagów: [SpreadingVoiceSecondPhase] = 검은 신의 권능 / Divinity of the Obsidian God; [EncompassingVoiceSecondPhase] = 검은 신의 목소리 / Voice of the Obsidian God; [LeaderVoiceSecondPhase] = 시지프 형벌의 간수 / Warden of the Sisyphe Penalty
   EN: Turn Start: If this unit has [SpreadingVoiceSecondPhase], gain a new pattern and <color=#ff6000><mark=#ff000040><b><u>use a powerful Skill, "Judgment... Sentencing... Condemnation!"</u></b></mark></color>\n- Min & Max Speed +20 for the turn\n- <color=#ff6000><mark=#ff000040><b><u>If the Warden loses the Clash while in this pattern</u></b></mark></color>, gain a changed pattern next turn, and <color=#ff6000><mark=#ff000040><b><u>use a powerful Skill, "Death Unto the Condemned"</u></b></mark></color>\n\nEvery time [SpreadingVoiceSecondPhase] and [EncompassingVoiceSecondPhase] are converted, <color=#ff6000><mark=#ff000040><b><u>heal 45 SP</u></b></mark></color> and <color=#ff6000><mark=#ff000040><b><u>gain 1 [LeaderVoiceSecondPhase]</u></b></mark></color>\n\nAt 50% or lower HP, end the turn (excluding certain Skills); if Staggered, recover from Stagger\nAt 1 or lower HP, enter a new Phase
   PL: Początek tury: jeżeli ta jednostka ma [SpreadingVoiceSecondPhase], przybiera nowy wzorzec i <color=#ff6000><mark=#ff000040><b><u>używa potężnej Umiejętności „Judgment... Sentencing... Condemnation!”</u></b></mark></color>\n- Szybkość min. i maks. +20 w tej turze\n- gdy <color=#ff6000><mark=#ff000040><b><u>The Warden przegra Starcie w tym wzorcu</u></b></mark></color>, w następnej turze przybiera zmieniony wzorzec i <color=#ff6000><mark=#ff000040><b><u>używa potężnej Umiejętności „Death Unto the Condemned”</u></b></mark></color>\n\nza każdą konwersją [SpreadingVoiceSecondPhase] i [EncompassingVoiceSecondPhase] <color=#ff6000><mark=#ff000040><b><u>przywraca 45 SP</u></b></mark></color> i <color=#ff6000><mark=#ff000040><b><u>zyskuje 1 [LeaderVoiceSecondPhase]</u></b></mark></color>\n\nprzy HP 50% lub mniej, kończy turę (z wyjątkiem pewnych Umiejętności); jeżeli jest Oszołamiona, dochodzi do siebie\nprzy HP 1 lub mniej, zmienia Fazę
275. [[a1c10p3] Pasywka wroga [148602] — tekst klimatyczny] 형벌로도 속죄치 못한 자들은… 심판의 날에 죽으리.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148602].flavor
   limit: do 120 znaków
   EN: They who have failed to atone through punishment shall perish on the Day of Judgment.
   PL: Ci, którzy nie zdołali odkupić się karą… zginą w Dniu Sądu.
276. [[a1c10p3] Pasywka wroga [148602] — podsumowanie] [SpreadingVoiceSecondPhase]이 있으면 강력한 스킬 사용\n이때 합 패배 시 다음 턴에 '사형 집행' 사용
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148602].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [SpreadingVoiceSecondPhase]
   znaczenie tagów: [SpreadingVoiceSecondPhase] = 검은 신의 권능 / Divinity of the Obsidian God
   EN: Use a powerful Skill if this unit has [SpreadingVoiceSecondPhase]\nOn Clash Lose in this pattern, use "Death Unto the Condemned" next turn
   PL: jeżeli ta jednostka ma [SpreadingVoiceSecondPhase], używa potężnej Umiejętności\npo przegranej w Starciu w tym wzorcu używa „Death Unto the Condemned” w następnej turze
277. [[a1c10p3] Pasywka wroga [148603] — nazwa] 눈물은 천을 적시고, 천은 목을 조르며
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148603].name
   limit: do 90 znaków
   EN: Tears shall soak the cloth, cloth shall close about the throat...
   PL: Tears shall soak the cloth, cloth shall close about the throat...
278. [[a1c10p3] Pasywka wroga [148603] — opis] <color=#ff6000><mark=#ff000040><b><u>[Sinking] 효과로 자신의 정신력이 감소하지 않는 대신</u></b></mark></color>,\n그 수치만큼 우울 피해를 받음\n\n수감자에게 피격 시, 대상 수감자의 [Sinking] 횟수 1 증가\n(수감자별 턴당 최대 2)\n\n[Breath] 위력을 20까지만 얻는 대신,\n<color=#ff6000><mark=#ff000040><b><u>이를 초과하여 얻는 [Breath] 위력 수치만큼 정신력 회복</u></b></mark></color>
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148603].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Sinking], [Breath]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [Breath] = 호흡 / Poise
   EN: <color=#ff6000><mark=#ff000040><b><u>This unit does not lose SP from [Sinking] effects</u></b></mark></color>; instead, this unit takes Gloom damage equal to Sinking Potency\n\nWhen hit by a Sinner, the said Sinner gains +1 [Sinking] Count (2 times per turn per Sinner)\n\nThis unit cannot gain [Breath] Potency past 20; <color=#ff6000><mark=#ff000040><b><u>instead, heal SP equal to excess [Breath] Potency gained</u></b></mark></color>
   PL: <color=#ff6000><mark=#ff000040><b><u>ta jednostka nie traci SP z powodu efektów [Sinking]</u></b></mark></color>; zamiast tego otrzymuje obrażenia Posępności równe Siły Zatonięcia\n\nprzy trafieniu przez Grzesznika, ten Grzesznik zyskuje 1 Licznika [Sinking] (2 razy na turę na Grzesznika)\n\nta jednostka nie może zyskać Siły [Breath] powyżej 20; <color=#ff6000><mark=#ff000040><b><u>zamiast tego przywraca SP równe nadmiarowi zyskanej Siły [Breath]</u></b></mark></color>
279. [[a1c10p3] Pasywka wroga [148603] — podsumowanie] [Sinking]으로 정신력 감소 대신 우울 피해를 받음\n피격 시 공격자의 [Sinking] 횟수 증가
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148603].summary
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [[a1c10p3] Pasywka wroga [148604] — nazwa] 완벽 보존
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148604].name
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [[a1c10p3] Pasywka wroga [148604] — opis] 전투 중 누적으로 자신의 [ChargeNoir] 횟수를\n10 소모할 때마다 [ChargeNoir] 위력 1 얻음\n\n턴 시작 시 자신의 [ChargeNoir] 위력이 5, [ChargeNoir] 횟수가 10 미만이면,\n자신의 [ChargeNoir] 횟수 5 증가\n\n[ChargeNoir]의 턴 종료 시 횟수 1이 감소하는 효과가 적용되지 않음\n\n자신의 [ChargeNoir] 위력이 5/10 이상이면, 자신의 [ChargeNoir] 횟수 최대치 +5/+10
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148604].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: Gain 1 [ChargeNoir] Potency for every 10 cumulative [ChargeNoir] Count this unit consumes in this Encounter\n\nTurn Start: At fewer than 5 [ChargeNoir] Potency and fewer than 10 [ChargeNoir] Count, gain +5 [ChargeNoir] Count\n\nThe "Turn End: Lose 1 Count" effect on [ChargeNoir] does not trigger\n\nAt 5+/10+ [ChargeNoir] Potency, [ChargeNoir] Count max cap +5/+10
   PL: zyskuje 1 Siły [ChargeNoir] za każde 10 łącznie zużytych Liczników [ChargeNoir] tej jednostki w tej walce\n\nPoczątek tury: jeżeli Siła [ChargeNoir] tej jednostki jest niższa niż 5, a Liczniki [ChargeNoir] niższe niż 10, zyskuje 5 Licznika [ChargeNoir]\n\nefekt [ChargeNoir] „Koniec tury: traci 1 Licznika” się nie uruchamia\n\nprzy 5+/10+ Siły [ChargeNoir] maks. wartość Liczników [ChargeNoir] +5/+10
282. [[a1c10p3] Pasywka wroga [148604] — tekst klimatyczny] 시지프 시스템적으로 이 보존은 완벽하게 보존된다.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148604].flavor
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [[a1c10p3] Pasywka wroga [148604] — podsumowanie] [ChargeNoir] 횟수를 누적 소모하면 [ChargeNoir] 위력 얻음\n[ChargeNoir] 횟수가 턴 종료 시 감소하지 않음
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148604].summary
   (powtórzenie elementu 255 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [[a1c10p3] Pasywka wroga [148711] — nazwa] 젠장, 그런 글리치는 어떻게 찾아낸 거야.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148711].name
   limit: do 80 znaków
   EN: Goddammit. How did you manage to find a glitch like that?
   PL: Goddammit. How did you manage to find a glitch like that?
285. [[a1c10p3] Pasywka wroga [148711] — opis] 턴 시작 시, [GoldenHideWarderThirdPhase]과 [GoldenFabricWarderThirdPhase]가 무작위 수감자에게 부여됨\n\n<color=#ff6000><mark=#ff000040><b><u>관리자가 특정 행동을 할 경우,\n신부가 무작위 수감자에게 최대 체력 비례 피해를 입히고 [GoldenNail]을 부여</u></b></mark></color>\n\n<color=#ff6000><mark=#ff000040><b><u>체력이 50% 미만이 되면, 신부가 시스템에 간섭하여</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>자신의 체력과 정신력을 최대로 회복하고 부정적인 효과를 전부 제거</u></b></mark></color>
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148711].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [GoldenHideWarderThirdPhase], [GoldenFabricWarderThirdPhase], [GoldenNail]
   znaczenie tagów: [GoldenHideWarderThirdPhase] = 박동 / Thumping Pulse; [GoldenFabricWarderThirdPhase] = 정지 / Stillness; [GoldenNail] = 못[Console] / Nail [Console]
   EN: Turn Start: Random Sinners gain [GoldenHideWarderThirdPhase] and [GoldenFabricWarderThirdPhase]\n\n<color=#ff6000><mark=#ff000040><b><u>When "the Manager" takes a certain action, the Chaplain deals damage to a random Sinner based on the said Sinner's max HP and inflicts [GoldenNail] on them</u></b></mark></color>\n\n<color=#ff6000><mark=#ff000040><b><u>At lower than 50% HP, the Chaplain manipulates his status on a system level</u></b></mark></color> to <color=#ff6000><mark=#ff000040><b><u>heal both HP and SP up to max and remove all negative effects from self</u></b></mark></color>
   PL: Początek tury: losowi Grzesznicy zyskują [GoldenHideWarderThirdPhase] i [GoldenFabricWarderThirdPhase]\n\n<color=#ff6000><mark=#ff000040><b><u>gdy „Zarządca” podejmie określone działanie, The Chaplain zadaje losowemu Grzesznikowi obrażenia proporcjonalne do Maks. HP tego Grzesznika i nakłada na niego [GoldenNail]</u></b></mark></color>\n\n<color=#ff6000><mark=#ff000040><b><u>gdy HP spadnie poniżej 50%, The Chaplain manipuluje swoim statusem na poziomie systemu</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>przywraca HP i SP do maksimum i usuwa wszystkie negatywne efekty z siebie</u></b></mark></color>
286. [[a1c10p3] Pasywka wroga [148711] — tekst klimatyczny] “시스템이 언제나 완벽할 순 없겠다만은, 이 정도의 버그가 생길 줄은 몰랐지. 쯧, 유지보수팀을 불러야겠군.”
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148711].flavor
   limit: do 160 znaków
   EN: "No system's glitch-free all the time, of course, but a bug this bad...? Tsk. Looks like I'll have to call maintenance."
   PL: "No system's glitch-free all the time, of course, but a bug this bad...? Tsk. Looks like I'll have to call maintenance."
287. [[a1c10p3] Pasywka wroga [148711] — podsumowanie] 매 턴 무작위 수감자에게 [GoldenHideWarderThirdPhase], [GoldenFabricWarderThirdPhase] 부여\n체력 50% 미만 시 완전 회복, 부정적인 효과 제거
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148711].summary
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [GoldenHideWarderThirdPhase], [GoldenFabricWarderThirdPhase]
   znaczenie tagów: [GoldenHideWarderThirdPhase] = 박동 / Thumping Pulse; [GoldenFabricWarderThirdPhase] = 정지 / Stillness
   EN: Random Sinners gain [GoldenHideWarderThirdPhase] and [GoldenFabricWarderThirdPhase] every turn\nWhen reaching lower than 50% HP, fully heal and remove negative effects
   PL: co turę losowi Grzesznicy zyskują [GoldenHideWarderThirdPhase] i [GoldenFabricWarderThirdPhase]\nprzy HP poniżej 50% pełne przywrócenie HP i usunięcie negatywnych efektów
288. [[a1c10p3] Pasywka wroga [148705] — nazwa] 시지프 시스템 유지보수 툴
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148705].name
   limit: do 50 znaków
   EN: Sisyphe System Maintenance Tool
   PL: Sisyphe System Maintenance Tool
289. [[a1c10p3] Pasywka wroga [148705] — opis] 신부가 자신의 스킬 효과로 수감자에게 [ConfessionThirdPhase]를 부여할 때,\n다음의 효과가 적용됨\n- [RestrainingNailThirdPhase], [ExecutionNailThirdPhase], [GoldenNail]을 아울러\n<color=#ff6000><mark=#ff000040><b><u>[ConfessionThirdPhase]로 지칭</u></b></mark></color>함\n- 신부가 수감자에게 못을 부여할 때, <color=#ff6000><mark=#ff000040><b><u>제일 마지막에 부여한 효과로 적용</u></b></mark></color>시키고 수치는 합산함\n- <color=#ff6000><mark=#ff000040><b><u>[RestrainingNailThirdPhase], [ExecutionNailThirdPhase]는\n[GoldenNail]로 변경되지 않음</u></b></mark></color>\n\n수감자에게 공격 적중 시, 대상 수감자가 보유한 <color=#ff6000><mark=#ff000040><b><u>[ConfessionThirdPhase] 1당\n피해량 +5%</u></b></mark></color> (최대 45%, 대상별로 적용)\n\n턴 시작 시 신부의 <color=#ff6000><mark=#ff000040><b><u>체력이 50% 이하</u></b></mark></color>면,\n스킬로 부여하는 모든 <color=#ff6000><mark=#ff000040><b><u>[ConfessionThirdPhase]의 부여량 +1</u></b></mark></color>
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148705].desc
   limit: do 930 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ConfessionThirdPhase], [RestrainingNailThirdPhase], [ExecutionNailThirdPhase], [GoldenNail], [TabExplain]
   znaczenie tagów: [ConfessionThirdPhase] = 〜 / 〜; [RestrainingNailThirdPhase] = 못[Exception] / Nail [Exception]; [ExecutionNailThirdPhase] = 못[Breakpoint] / Nail [Breakpoint]; [GoldenNail] = 못[Console] / Nail [Console]
   EN: When the Chaplain inflicts [ConfessionThirdPhase] on Sinners using its Skill effects, apply the following:\n- The following effects are <color=#ff6000><mark=#ff000040><b><u>collectively referred to as [ConfessionThirdPhase]</u></b></mark></color>:\n  · [RestrainingNailThirdPhase]\n  · [ExecutionNailThirdPhase]\n  · [GoldenNail]\n- When the Chaplain inflicts Nail[TabExplain] on the Sinners, <color=#ff6000><mark=#ff000040><b><u>only the effect that is inflicted last remains</u></b></mark></color>; however, Stacks between effects accumulate\n<color=#ff6000><mark=#ff000040><b><u>- [RestrainingNailThirdPhase] and [ExecutionNailThirdPhase] do not convert into [GoldenNail]</u></b></mark></color>\n\nOn Hit against a Sinner, <color=#ff6000><mark=#ff000040><b><u>deal +5% damage for every [ConfessionThirdPhase]</u></b></mark></color> on target (max 45%, separately for each target)\n\nTurn Start: <color=#ff6000><mark=#ff000040><b><u>If the Chaplain has 50% or lower HP</u></b></mark></color>, all Skills inflict <color=#ff6000><mark=#ff000040><b><u>+1 more [ConfessionThirdPhase]</u></b></mark></color>
   PL: gdy The Chaplain nakłada [ConfessionThirdPhase] na Grzeszników efektami swoich Umiejętności, stosuje się:\n- następujące efekty są <color=#ff6000><mark=#ff000040><b><u>łącznie nazywane [ConfessionThirdPhase]</u></b></mark></color>:\n  · [RestrainingNailThirdPhase]\n  · [ExecutionNailThirdPhase]\n  · [GoldenNail]\n- gdy The Chaplain nakłada Nail[TabExplain] na Grzeszników, <color=#ff6000><mark=#ff000040><b><u>pozostaje wyłącznie ostatnio nałożony efekt</u></b></mark></color>; Stosy między efektami sumują się\n<color=#ff6000><mark=#ff000040><b><u>- [RestrainingNailThirdPhase] i [ExecutionNailThirdPhase] nie zamieniają się w [GoldenNail]</u></b></mark></color>\n\nprzy trafieniu Grzesznika <color=#ff6000><mark=#ff000040><b><u>zadaje +5% obrażeń za każdą 1 [ConfessionThirdPhase]</u></b></mark></color> na celu (maks. 45%, osobno dla każdego celu)\n\nPoczątek tury: <color=#ff6000><mark=#ff000040><b><u>jeżeli HP The Chaplain wynosi 50% lub mniej</u></b></mark></color>, wszystkie Umiejętności nakładają <color=#ff6000><mark=#ff000040><b><u>dodatkowo +1 [ConfessionThirdPhase]</u></b></mark></color>
290. [[a1c10p3] Pasywka wroga [148705] — tekst klimatyczny] “매뉴얼에 따르면… 이럴 때는 전부 다시 조정해야 돼. 다 이미 규정된 사항이라고. 여기 매뉴얼에 적혀있는 것만 봐도… 아, 그쪽에선 볼 수가 없겠군.”
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148705].flavor
   limit: do 290 znaków
   EN: "According to the manual... when this happens, everything has to be readjusted. It's all been laid out in the regulations already. You can see it right here in the manual... ah. Right. You can't see this from where you are."
   PL: "According to the manual... when this happens, everything has to be readjusted. It's all been laid out in the regulations already. You can see it right here in the manual... ah. Right. You can't see this from where you are."
291. [[a1c10p3] Pasywka wroga [148705] — podsumowanie] 대상의 [ConfessionThirdPhase]에 따라 피해량 증가\n체력 50% 이하면 [ConfessionThirdPhase] 부여량 증가
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148705].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [ConfessionThirdPhase]
   znaczenie tagów: [ConfessionThirdPhase] = 〜 / 〜
   EN: Deal more damage based on [ConfessionThirdPhase] on target\nAt 50%- HP, inflict more [ConfessionThirdPhase]
   PL: zadaje więcej obrażeń zależnie od [ConfessionThirdPhase] celu\nprzy HP tej jednostki 50% lub mniej nakłada więcej [ConfessionThirdPhase]
292. [[a1c10p3] Pasywka wroga [148701] — nazwa] ‘보존의 규율대로’
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148701].name
   limit: do 60 znaków
   EN: "As Ordained by the Rule of Conservation"
   PL: "As Ordained by the Rule of Conservation"
293. [[a1c10p3] Pasywka wroga [148701] — opis] <color=#ff6000><mark=#ff000040><b><u>합 횟수가 10 이상</u></b></mark></color>이 되면, 해당 스킬의 <color=#ff6000><mark=#ff000040><b><u>합 위력 +(합을 진행한 횟수)</u></b></mark></color>\n\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]의 <color=#ff6000><mark=#ff000040><b><u>위력이 최대 50까지 누적</u></b></mark></color>되고 <color=#ff6000><mark=#ff000040><b><u>횟수는 최대 15까지 누적</u></b></mark></color>됨\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -50%\n\n[PanicChangeLock] 효과가 적용되며,\n<color=#ff6000><mark=#ff000040><b><u>정신력이 0 미만으로 내려가지 않음</u></b></mark></color>\n\n등장 이후 첫 턴 시작 시,\n- 정신력이 45로 변경됨\n- [EncompassingVoiceThirdPhase] 0 얻음, [LeaderVoiceThirdPhase] 1 얻음\n- 직전 페이즈의 [ChargeNoir] 위력과 횟수가 그대로 유지됨
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148701].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [PanicChangeLock], [EncompassingVoiceThirdPhase], [LeaderVoiceThirdPhase], [ChargeNoir]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic; [EncompassingVoiceThirdPhase] = 검은 신의 목소리 / Voice of the Obsidian God; [LeaderVoiceThirdPhase] = 시지프 형벌의 신부 / Chaplain of the Sisyphe Penalty …
   EN: <color=#ff6000><mark=#ff000040><b><u>At 10+ Clashes</u></b></mark></color>, the said Skill <color=#ff6000><mark=#ff000040><b><u>gains Clash Power by (Clash Count)</u></b></mark></color>\n\nFor [Combustion], [Laceration], [Vibration], [Burst], [Sinking]:\n- <color=#ff6000><mark=#ff000040><b><u>Max Potency cap: 50\n- Max Count cap: 15</u></b></mark></color>\n- Take -50% damage from above effects\n\nApply the [PanicChangeLock] effect, and <color=#ff6000><mark=#ff000040><b><u>this unit's SP does not drop below 0</u></b></mark></color>\n\nFirst Turn Start after entry:\n- Change SP to 45\n- Gain 0 [EncompassingVoiceThirdPhase] and 1 [LeaderVoiceThirdPhase]\n- [ChargeNoir] Potency and Count carry over from the preceding Phase
   PL: <color=#ff6000><mark=#ff000040><b><u>przy 10+ Starciach</u></b></mark></color>, ta Umiejętność <color=#ff6000><mark=#ff000040><b><u>zyskuje Moc Starcia równą (liczba stoczonych Starć)</u></b></mark></color>\n\nDla [Combustion], [Laceration], [Vibration], [Burst], [Sinking]:\n- <color=#ff6000><mark=#ff000040><b><u>maks. wartość Siły: 50\n- maks. wartość Liczników: 15</u></b></mark></color>\n- otrzymuje -50% obrażeń od powyższych efektów\n\nstosuje efekt [PanicChangeLock], a <color=#ff6000><mark=#ff000040><b><u>SP tej jednostki nie spada poniżej 0</u></b></mark></color>\n\nna pierwszym Początku tury po pojawieniu się:\n- SP zmienia się na 45\n- zyskuje 0 [EncompassingVoiceThirdPhase] i 1 [LeaderVoiceThirdPhase]\n- Siła i Liczniki [ChargeNoir] dziedziczone z poprzedniej Fazy
294. [[a1c10p3] Pasywka wroga [148701] — podsumowanie] 합 횟수 10 이상이면 합 위력 증가\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 감소
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148701].summary
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: At 10+ Clash Count, gain Clash Power\nTake less damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL: przy 10+ Starciach zyskuje Moc Starcia\notrzymuje mniej obrażeń od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]
295. [[a1c10p3] Pasywka wroga [148702] — nazwa] ‘심판의 날’
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148702].name
   limit: do 40 znaków
   EN: "Dies Irae"
   PL: "Dies Irae"
296. [[a1c10p3] Pasywka wroga [148702] — opis] 턴 시작 시 [SpreadingVoiceThirdPhase]이 있으면, 패턴이 변경되고\n<color=#ff6000><mark=#ff000040><b><u>강력한 스킬 ‘시지프 시스템을 진짜 망가트리려고?’</u></b></mark></color>를 사용\n- 해당 턴에 속도 최솟값, 최댓값 +20\n- <color=#ff6000><mark=#ff000040><b><u>이 패턴에서 신부가 합 패배</u></b></mark></color> 시,\n다음 턴에 패턴이 추가로 변경되고 <color=#ff6000><mark=#ff000040><b><u>강력한 스킬 ‘강제 퇴장’</u></b></mark></color>을 사용\n\n[SpreadingVoiceThirdPhase]/[EncompassingVoiceThirdPhase]가 변경될 때마다\n<color=#ff6000><mark=#ff000040><b><u>정신력이 45만큼 회복</u></b></mark></color>되고 <color=#ff6000><mark=#ff000040><b><u>[LeaderVoiceThirdPhase] 1 얻음</u></b></mark></color>
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148702].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [SpreadingVoiceThirdPhase], [EncompassingVoiceThirdPhase], [LeaderVoiceThirdPhase]
   znaczenie tagów: [SpreadingVoiceThirdPhase] = 검은 신의 권능 / Divinity of the Obsidian God; [EncompassingVoiceThirdPhase] = 검은 신의 목소리 / Voice of the Obsidian God; [LeaderVoiceThirdPhase] = 시지프 형벌의 신부 / Chaplain of the Sisyphe Penalty
   EN: Turn Start: If this unit has [SpreadingVoiceThirdPhase], gain a new pattern and use a <color=#ff6000><mark=#ff000040><b><u>powerful Skill, "Do you seriously mean to break the Sisyphe System?"</u></b></mark></color>\n- Min & Max Speed +20 for the turn\n- <color=#ff6000><mark=#ff000040><b><u>If the Chaplain loses the Clash</u></b></mark></color> while in this pattern, gain a changed pattern next turn, and <color=#ff6000><mark=#ff000040><b><u>use a powerful Skill, "Systemwide Ban"</u></b></mark></color>\n\nEvery time [SpreadingVoiceThirdPhase] and [EncompassingVoiceThirdPhase] are converted, <color=#ff6000><mark=#ff000040><b><u>heal 45 SP</u></b></mark></color> and <color=#ff6000><mark=#ff000040><b><u>gain 1 [LeaderVoiceThirdPhase]</u></b></mark></color>
   PL: Początek tury: jeżeli ta jednostka ma [SpreadingVoiceThirdPhase], przybiera nowy wzorzec i używa <color=#ff6000><mark=#ff000040><b><u>potężnej Umiejętności „Do you seriously mean to break the Sisyphe System?”</u></b></mark></color>\n- Szybkość min. i maks. +20 w tej turze\n- gdy <color=#ff6000><mark=#ff000040><b><u>The Chaplain przegra Starcie</u></b></mark></color> w tym wzorcu, w następnej turze przybiera zmieniony wzorzec i używa <color=#ff6000><mark=#ff000040><b><u>potężnej Umiejętności „Systemwide Ban”</u></b></mark></color>\n\nza każdą konwersją [SpreadingVoiceThirdPhase] i [EncompassingVoiceThirdPhase] <color=#ff6000><mark=#ff000040><b><u>przywraca 45 SP</u></b></mark></color> i <color=#ff6000><mark=#ff000040><b><u>zyskuje 1 [LeaderVoiceThirdPhase]</u></b></mark></color>
297. [[a1c10p3] Pasywka wroga [148702] — tekst klimatyczny] 벌받고도 반성을 안 했으면, 심판받아야지. 죽을 만큼 말이야.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148702].flavor
   limit: do 170 znaków
   EN: If getting punished still wasn't enough to make you reflect, then I guess it's time for judgment. Enough to kill you, that is.
   PL: Skoro kara nie wystarczyła, byś się zrewidował, to czas na sąd. Na taki, który cię zabije.
298. [[a1c10p3] Pasywka wroga [148702] — podsumowanie] [SpreadingVoiceThirdPhase]이 있으면 강력한 스킬 사용\n이때 합 패배 시 다음 턴에 '강제 퇴장' 사용
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148702].summary
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [SpreadingVoiceThirdPhase]
   znaczenie tagów: [SpreadingVoiceThirdPhase] = 검은 신의 권능 / Divinity of the Obsidian God
   EN: Use a powerful Skill if this unit has [SpreadingVoiceThirdPhase]\nOn Clash Lose in this pattern, use "Systemwide Ban" next turn
   PL: jeżeli ta jednostka ma [SpreadingVoiceThirdPhase], używa potężnej Umiejętności\npo przegranej w Starciu w tym wzorcu używa „Systemwide Ban” w następnej turze
299. [[a1c10p3] Pasywka wroga [148703] — nazwa] 눈물은 천을 적시고, 천은 목을 조르며… 말도 안 떠오르네.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148703].name
   limit: do 140 znaków
   EN: Tears shall soak the cloth, cloth shall close about the throat... now I can't even remember what's next.
   PL: Tears shall soak the cloth, cloth shall close about the throat... now I can't even remember what's next.
300. [[a1c10p3] Pasywka wroga [148703] — opis] <color=#ff6000><mark=#ff000040><b><u>[Sinking] 효과로 자신의 정신력이 감소하지 않는 대신</u></b></mark></color>,\n그 수치만큼 우울 피해를 받음\n\n수감자에게 피격 시, 대상 수감자의 [Sinking] 횟수 1 증가\n(수감자별 턴당 최대 2)\n\n[Breath] 위력을 20까지만 얻는 대신,\n<color=#ff6000><mark=#ff000040><b><u>이를 초과하여 얻는 [Breath] 위력만큼 정신력 회복</u></b></mark></color>\n\n수감자에게 [VibrationExplosion] 시 대상 수감자에게 <color=#ff6000><mark=#ff000040><b><u>흐트러짐 선이 없으면</u></b></mark></color>,\n흐트러짐 피해 대신 대상의 [Vibration] 위력 절반만큼 <color=#ff6000><mark=#ff000040><b><u>나태 피해를 입힘</u></b></mark></color> (흐트러진 대상 제외, 대상별로 적용)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148703].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Sinking], [Breath], [VibrationExplosion], [Vibration]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [Breath] = 호흡 / Poise; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: <color=#ff6000><mark=#ff000040><b><u>This unit does not lose SP from [Sinking] effects</u></b></mark></color>; instead, when [Sinking] effects trigger, this unit takes Gloom damage equal to Sinking Potency\n\nWhen hit by a Sinner, the said Sinner gains +1 [Sinking] Count (2 per turn per Sinner)\n\nThis unit cannot gain [Breath] Potency past 20; <color=#ff6000><mark=#ff000040><b><u>instead, heal SP equal to excess [Breath] Potency gained</u></b></mark></color>\n\nWhen triggering [VibrationExplosion] on Sinners, <color=#ff6000><mark=#ff000040><b><u>if the targeted Sinner does not have a Stagger Threshold</u></b></mark></color>, <color=#ff6000><mark=#ff000040><b><u>deal ([Vibration] Potency on target / 2) Sloth damage</u></b></mark></color> (except Staggered targets; calculated separately for each target)
   PL: <color=#ff6000><mark=#ff000040><b><u>ta jednostka nie traci SP z powodu efektów [Sinking]</u></b></mark></color>; zamiast tego, gdy efekt [Sinking] się uruchamia, otrzymuje obrażenia Posępności równe Siły Zatonięcia\n\nprzy trafieniu przez Grzesznika, ten Grzesznik zyskuje 1 Licznika [Sinking] (maks. 2 na turę na Grzesznika)\n\nta jednostka nie może zyskać Siły [Breath] powyżej 20; <color=#ff6000><mark=#ff000040><b><u>zamiast tego przywraca SP równe nadmiarowi zyskanej Siły [Breath]</u></b></mark></color>\n\nprzy wywołaniu [VibrationExplosion] na Grzesznikach, jeżeli <color=#ff6000><mark=#ff000040><b><u>atakowany Grzesznik nie ma Progu Oszołomienia</u></b></mark></color>, zamiast obrażeń Oszołamienia zadaje <color=#ff6000><mark=#ff000040><b><u>obrażenia Lenistwa równe (Siła [Vibration] celu / 2)</u></b></mark></color> (z wyłączeniem oszołamionych celów; rozpatrywane osobno dla każdego celu)
301. [[a1c10p3] Pasywka wroga [148703] — tekst klimatyczny] “정말 ‘기도하기’라도 해야 하지 않겠어?”
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148703].flavor
   limit: do 120 znaków
   EN: “About time you started 'praying,' don't you think?”
   PL: “About time you started 'praying,' don't you think?”
302. [[a1c10p3] Pasywka wroga [148703] — podsumowanie] 피격 시 공격자의 [Sinking] 횟수 증가\n[VibrationExplosion] 시 흐트러짐 선이 없으면 나태 피해
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148703].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [VibrationExplosion]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: When hit, inflict [Sinking] Count on the attacker\nOn [VibrationExplosion], deal Sloth damage if target does not have a Stagger Threshold
   PL: przy trafieniu atakujący zyskuje Licznik [Sinking]\nprzy [VibrationExplosion] zadaje obrażenia Lenistwa, jeżeli cel nie ma Progu Oszołomienia
303. [[a1c10p3] Pasywka wroga [148704] — nazwa] 완벽 보존
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148704].name
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [[a1c10p3] Pasywka wroga [148704] — opis] 전투 중 누적으로 자신의 [ChargeNoir] 횟수를\n10 소모할 때마다 [ChargeNoir] 위력 1 얻음\n\n턴 시작 시 자신의 [ChargeNoir] 위력이 10, [ChargeNoir] 횟수가 10 미만이면,\n자신의 [ChargeNoir] 횟수 5 증가\n\n[ChargeNoir]의 턴 종료 시 횟수 1이 감소하는 효과가 적용되지 않음\n\n자신의 [ChargeNoir] 위력이 5/10 이상이면, 자신의 [ChargeNoir] 횟수 최대치 +5/+10
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148704].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: Gain 1 [ChargeNoir] Potency for every 10 cumulative [ChargeNoir] Count this unit consumes in this Encounter\n\nTurn Start: At fewer than 10 [ChargeNoir] Potency and fewer than 10 [ChargeNoir] Count, gain +5 [ChargeNoir] Count\n\nThe "Turn End: Lose 1 Count" effect on [ChargeNoir] does not trigger\n\nAt 5+/10+ [ChargeNoir] Potency, [ChargeNoir] Count max cap +5/+10
   PL: zyskuje 1 Siły [ChargeNoir] za każde 10 łącznie zużytych Liczników [ChargeNoir] tej jednostki w tej walce\n\nPoczątek tury: jeżeli Siła [ChargeNoir] tej jednostki jest niższa niż 10, a Liczniki [ChargeNoir] niższe niż 10, zyskuje 5 Licznika [ChargeNoir]\n\nefekt [ChargeNoir] „Koniec tury: traci 1 Licznika” się nie uruchamia\n\nprzy 5+/10+ Siły [ChargeNoir] maks. wartość Liczników [ChargeNoir] +5/+10
305. [[a1c10p3] Pasywka wroga [148704] — tekst klimatyczny] 시지프 시스템적으로 이 보존은 완벽하게 보존된다.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148704].flavor
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [[a1c10p3] Pasywka wroga [148704] — podsumowanie] [ChargeNoir] 횟수를 누적 소모하면 [ChargeNoir] 위력 얻음\n[ChargeNoir] 횟수가 턴 종료 시 감소하지 않음
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148704].summary
   (powtórzenie elementu 255 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [[a1c10p3] Pasywka wroga [148706] — nazwa] 자, 이제 퇴근해 볼까
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148706].name
   limit: do 50 znaków
   EN: All right. Time to clock out.
   PL: All right. Time to clock out.
308. [[a1c10p3] Pasywka wroga [148706] — opis] 턴 종료 시 [ChargeNoir] 위력이 10을 초과하면,\n초과한 수치만큼 [ChargeNoir] 위력을 소모하여 소모한 수치만큼\n[Dominion] 얻음\n- 이 패시브 효과로 [Dominion]을 전부 소모한 이후에는 이 효과가 발동하지 않음\n\n자신의 체력이 처음으로 <color=#ff6000><mark=#ff000040><b><u>33% 이하가 되면, 패턴이 변경</u></b></mark></color>됨\n- 보유한 [Dominion]을 전부 소모하여 자신의 <color=#ff6000><mark=#ff000040><b><u>최대 체력의\n(25 + [Dominion] 수치)%만큼 비휘발성 보호막 얻음</u></b></mark></color>\n- 소모한 [Dominion] 수치만큼 방어 레벨이 영구적으로 감소
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148706].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ChargeNoir], [Dominion]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation; [Dominion] = 시지프 시스템 보존 / Sisyphe System Preservation
   EN: Turn End: At more than 10 [ChargeNoir] Potency, consume excess [ChargeNoir] Potency and gain ([ChargeNoir] Potency consumed) [Dominion]\n- This effect does not trigger again after all [Dominion] has been consumed by the effects of this Passive\n\nWhen this unit's HP drops to <color=#ff6000><mark=#ff000040><b><u>33% or lower for the first time in this Encounter, gain a new pattern</u></b></mark></color>\n- Consume all [Dominion] on self and <color=#ff6000><mark=#ff000040><b><u>gain persistent Shield equal to (25 + [Dominion] Stack)% of this unit's max HP</u></b></mark></color>\n- Permanently lose Defense Level equal to [Dominion] Stack consumed
   PL: Koniec tury: gdy Siła [ChargeNoir] przekroczy 10, zużywa nadwyżkę Siły [ChargeNoir] i zyskuje (zużyta Siła [ChargeNoir]) [Dominion]\n- po zużyciu całego [Dominion] efektami tej pasywki ten efekt się nie uruchamia\n\ngdy HP tej jednostki po raz pierwszy w tej walce <color=#ff6000><mark=#ff000040><b><u>spadnie do 33% lub mniej, przybiera nowy wzorzec</u></b></mark></color>\n- zużywa cały [Dominion] tej jednostki i <color=#ff6000><mark=#ff000040><b><u>zyskuje trwałą Tarczę równą (25 + Stosy [Dominion])% Maks. HP tej jednostki</u></b></mark></color>\n- traci trwale Poziom Obrony równy zużytym Stosom [Dominion]
309. [[a1c10p3] Pasywka wroga [148706] — tekst klimatyczny] “이러니저러니 해도 시지프 시스템은 N사에 반드시 필요해. 이 시스템이 무너지면… 다시 야만의 시대로 돌아가야 한다고.”\n\n“그러니까 매뉴얼대로, 너희는 이 백화점에서 나갈 수 없어. 예외는 없다는 거지.”
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148706].flavor
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Say what you want, the Sisyphe System is something N Corp. absolutely needs. If this system goes down... we're back to barbarism."\n\n"So, just like the manual says, you don't get to leave this department store. No exceptions."
   PL: „Mówcie, co chcecie — System Sisyphe jest czymś, czego N Corp. bezwzględnie potrzebuje. Jeżeli ten system się zawali... wrócimy do barbarzyństwa.”\n\n„A zatem, jak głosi instrukcja — nie wyjdziecie z tego domu towarowego. Wyjątków nie ma.”
310. [[a1c10p3] Pasywka wroga [148706] — podsumowanie] [ChargeNoir] 위력 10 초과분이 [Dominion]이 됨\n체력 33% 이하 시 패턴 변경, 보호막 얻음
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=148706].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir], [Dominion]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation; [Dominion] = 시지프 시스템 보존 / Sisyphe System Preservation
   EN: Convert 10 surplus [ChargeNoir] Potency into [Dominion]\nAt 33% or lower HP, change the pattern and gain Shield
   PL: nadwyżka Siły [ChargeNoir] powyżej 10 zamienia się w [Dominion]\nprzy HP 33% lub mniej zmienia wzorzec i zyskuje Tarczę
311. [[a1c10p3] Pasywka wroga [152201] — nazwa] 모베즈 푸아(mauvaise foi)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152201].name
   limit: do 40 znaków
   EN: Mauvaise Foi
   PL: Mauvaise Foi
312. [[a1c10p3] Pasywka wroga [152201] — opis] 전투 중 누적으로 자신의 [ChargeKhaki] 횟수를 10 소모할 때마다 [ChargeKhaki] 위력 1 얻음\n- 턴 종료시 [ChargeKhaki] 횟수 감소하는 효과가 발동하지 않음\n\n자신의 [ChargeKhaki] 횟수만큼 턴 종료 시 [Breath] 위력 얻음 (최대 10)\n자신의 [ChargeKhaki] 위력만큼 턴 종료 시 [Breath] 횟수 얻음 (최대 5)\n\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -60%\n- [Vibration]으로 받는 흐트러짐 피해량 -60%\n\n동일한 대상과의 합 진행 시 10합 당, 자신의 합 위력 +1
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152201].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeKhaki], [Breath], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: Gain 1 [ChargeKhaki] Potency for every 10 cumulative [ChargeKhaki] Count this unit consumes in this Encounter\n- The "Turn End: Lose 1 Count" effect on [ChargeKhaki] does not trigger\n\nTurn End: Gain [Breath] Potency equal to [ChargeKhaki] Count on self (max 10)\nTurn End: Gain [Breath] Count equal to [ChargeKhaki] Potency on self (max 5)\n\nTake -60% damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]\n- Stagger Threshold raised from [Vibration] -60%\n\nAt 10+ Clashes against the same target, gain Clash Power by (Clash Count / 10)
   PL: zyskuje 1 Siły [ChargeKhaki] za każde 10 łącznie zużytych Liczników [ChargeKhaki] tej jednostki w tej walce\n- efekt [ChargeKhaki] „Koniec tury: traci 1 Licznika” się nie uruchamia\n\nKoniec tury: zyskuje Siłę [Breath] równą Licznikom [ChargeKhaki] tej jednostki (maks. 10)\nKoniec tury: zyskuje Licznik [Breath] równy Sile [ChargeKhaki] tej jednostki (maks. 5)\n\notrzymuje -60% obrażeń od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]\n- podniesienie Progu Oszołomienia przez [Vibration] zmniejsza się o 60%\n\nprzy 10+ Starciach z tym samym celem zyskuje Moc Starcia równą (liczba Starć / 10)
313. [[a1c10p3] Pasywka wroga [152201] — tekst klimatyczny] 자기기만.\n세계로부터 도망친다. 두려움과 불안의 세계, 그곳을 피해 도망치고, 또 도망친다.\n\n스스로 자리에 못 박음으로써 무대 위로 도망간다. 무대에 올라선 배우는 역할에 완전히 몰입한다. 자신을 속이고 기만한다.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152201].flavor
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Bad faith.\n\nA flight from the world—from a world of fear and anxiety. Escape is sought again and again. \n\nOne escapes onto the stage by nailing oneself firmly into place. Like an actor upon a stage, the role is inhabited completely. Total immersion gives way to deception, and deception to self-deception.
   PL: Samooszukiwanie.\n\nUcieczka od świata — od świata strachu i niepokoju. Ucieczki szuka się znów i znów.\n\nWbiega na scenę, przybijając się na dobre do miejsca. Jak aktor na scenie, wciela się w rolę całkowicie. Całkowite zanurzenie przechodzi w oszustwo, a oszustwo w samooszukiwanie.
314. [[a1c10p3] Pasywka wroga [152202] — nazwa] 왈츠의 박자, 기억해?
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152202].name
   limit: do 50 znaków
   EN: Remember the rhythm of the waltz?
   PL: Remember the rhythm of the waltz?
315. [[a1c10p3] Pasywka wroga [152202] — opis] 한번의 합에서 합 횟수가 4번 이상이면, 합 횟수 4당 3번째 합의 승리한 대상의 피해량 +15% (최대 3회)\n- 해당 합에서 승리한 스킬이 1번째 합에서도 승리했으면, 최종 위력 +1
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152202].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 4+ Clashes in the same Clash:\n- From the 3rd Clash, the winner of the 3rd Clash deals +15% damage for every 4th Clash won (3 times max)\n- If the Skill that won the Clash won the first Clash, Final Power +1
   PL: przy 4+ Starciach w jednym Starciu:\n- od 3. Starcia zwycięzca 3. Starcia zadaje +15% obrażeń za każde wygrane 4. Starcie (maks. 3 razy)\n- jeżeli Umiejętność, która wygrała Starcie, wygrała też pierwsze Starcie, Moc Końcowa +1
316. [[a1c10p3] Pasywka wroga [152202] — tekst klimatyczny] 함께 경험했잖아.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152202].flavor
   limit: do 120 znaków
   EN: It was a shared experience, wasn't it?
   PL: It was a shared experience, wasn't it?
317. [[a1c10p3] Pasywka wroga [152203] — nazwa] 사르트르
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152203].name
   limit: do 40 znaków
   EN: Sartre
   PL: Sartre
318. [[a1c10p3] Pasywka wroga [152203] — opis] <color=#ff6000><mark color=#ff000040><b><u>3턴마다 시지프 백화점 설계도를 3명 소환</color></mark></b></u>하고 보호막을 자신의 최대 체력만큼 얻음\n- 해당 턴 동안 흐트러짐 상태시 흐트러짐을 해제하고 흐트러짐 상태가 되지 않음\n\n<color=#ff6000><mark color=#ff000040><b><u>시지프 백화점 설계도를 ‘포착’으로 죽였으면, [JeanneDesign]을 얻음</color></mark></b></u>\n\n<color=#ff6000><mark color=#ff000040><b><u>자신의 [JeanneDesign]이 3이면, [JeanneManager]으로 변경됨</color></mark></b></u>\n시지프 백화점 설계도를 <color=#ff6000><mark color=#ff000040><b><u>자신의 ‘포착’으로 한명도 죽이지 못했으면,</color></mark></b></u> 다음 턴에 [Vulnerable] 1 얻음
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152203].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [JeanneDesign], [JeanneManager], [Vulnerable]
   znaczenie tagów: [JeanneDesign] = 못 박힘 / Nailed; [JeanneManager] = 앙가즈망(engagement) / Engagement; [Vulnerable] = 취약 / Fragile
   EN: <color=#ff6000><mark color=#ff000040><b><u>Summon 3 "Grand Magasin Sisyphe Blueprint" every 3 turns</color></mark></b></u> and gain Shield equal to this unit's max HP\n- For that turn, when Staggered, recover from Stagger and cannot be Staggered again for the rest of the turn\n\n<color=#ff6000><mark color=#ff000040><b><u>After killing a "Grand Magasin Sisyphe Blueprint" with the "Focusing" Skill, gain [JeanneDesign]</color></mark></b></u>\n\n<color=#ff6000><mark color=#ff000040><b><u>At 3 [JeanneDesign], convert [JeanneDesign] into [JeanneManager]</color></mark></b></u>\n<color=#ff6000><mark color=#ff000040><b><u>If this unit failed to kill a single "Grand Magasin Sisyphe Blueprint" with its "Focusing" Skill</color></mark></b></u>, gain 1 [Vulnerable] next turn
   PL: <color=#ff6000><mark color=#ff000040><b><u>co 3 tury przywołuje 3 „Grand Magasin Sisyphe Blueprint”</u></b></mark></color> i zyskuje Tarczę równą Maks. HP tej jednostki\n- w tej turze, gdy przechodzi w Oszołamienie, dochodzi do siebie i nie może ponownie przejść w Oszołamienie przez resztę tej tury\n\n<color=#ff6000><mark color=#ff000040><b><u>po zabiciu „Grand Magasin Sisyphe Blueprint” Umiejętnością „Focusing” zyskuje [JeanneDesign]</u></b></mark></color>\n\n<color=#ff6000><mark color=#ff000040><b><u>przy 3 [JeanneDesign] zamienia [JeanneDesign] w [JeanneManager]</u></b></mark></color>\n<color=#ff6000><mark color=#ff000040><b><u>jeżeli nie zabiła ani jednego „Grand Magasin Sisyphe Blueprint” swoją Umiejętnością „Focusing”</u></b></mark></color>, zyskuje 1 [Vulnerable] w następnej turze
319. [[a1c10p3] Pasywka wroga [152203] — tekst klimatyczny] 시지프탑 네 명의 거인 중 하나.\n\n그중 시지프 시스템의 설계를 맡은 건축가이자, 재단사. 자신의 관점대로 쌓아 올리는 역할, 직업, 혹은 그 무언가.\n\n잔느에게 구토감을 일으키지 않는, 사르토리얼적으로 재단하여 못 박고, 꿰매어 쌓아 올린 장소.\n\n시지프 백화점.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152203].flavor
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One of the four Giants of Sisyphe Tower.\n\nAmong them, she is the architect of the Sisyphe System—a tailor, a designer, the executor of the role, or a job, or something... that builds the world up according to a viewpoint of her own.\n\nCut to her measure, nailed into place, stitched together piece by piece—this is a sartorial world shaped so that she might look upon it without being nauseated.\n\nThis is Grand Magasin Sisyphe.
   PL: Jeden z czterech Gigantów Wieży Sisyphe.\n\nSpośród nich jest architektką Systemu Sisyphe — krawcową, projektantką; wykonawczynią roli, zawodu albo czegokolwiek, co wznosi świat zgodnie z jej własnym punktem widzenia.\n\nWykrojone na jej miarę, przybite na miejscu, uszyte kawałek po kawałku — to sartorialny świat ukształtowany tak, by mogła spojrzeć na niego bez mdłości.\n\nTo jest Grand Magasin Sisyphe.
320. [[a1c10p3] Pasywka wroga [152204] — nazwa] 난 말이야…
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152204].name
   limit: do 40 znaków
   EN: You know, I...
   PL: You know, I...
321. [[a1c10p3] Pasywka wroga [152204] — opis] 스테이지 시작 시 정신력 45로 시작함\n\n뫼르소가 사망하면, 수감자가 전투 패배함\n\n<color=#ff6000><mark color=#ff000040><b><u>체력이 50% 이하면,</color></mark></b></u> 피해를 받지 않고, 페이즈 변경\n- 페이즈 변경 시 보유한 부정적인 효과 중 해제 가능한 효과를 제거함
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152204].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: Start this Encounter with 45 SP\n\nWhen Meursault is defeated, the Sinners lose the Encounter\n\n<color=#ff6000><mark color=#ff000040><b><u>At 50%- HP</color></mark></b></u>, stop taking any damage and enter a new Phase\n- When entering a new Phase, remove all removable negative effects on self
   PL: rozpoczyna tę walkę z 45 SP\n\ngdy Meursault zostanie pokonany, Grzesznicy przegrywają tę walkę\n\n<color=#ff6000><mark color=#ff000040><b><u>przy HP 50% lub mniej</u></b></mark></color>, przestaje otrzymywać obrażenia i zmienia Fazę\n- przy zmianie Fazy usuwa wszystkie usuwalne negatywne efekty z siebie
322. [[a1c10p3] Pasywka wroga [152204] — tekst klimatyczny] 당신이 바깥으로 나가지 않았으면 좋겠어.\n\n마 퓌스, 나와 함께 다음 무대로 가자.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152204].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I don't want you going back outside.\n\nCome with me onto the next stage instead, ma puce.
   PL: Nie chcę, żebyś wychodził na zewnątrz.\n\nChodź raczej ze mną na następną scenę, ma puce.
323. [[a1c10p3] Pasywka wroga [152301] — nazwa] 왈츠의 경험. 기억해?
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152301].name
   limit: do 60 znaków
   EN: Remember the experience of the waltz?
   PL: Remember the experience of the waltz?
324. [[a1c10p3] Pasywka wroga [152301] — opis] 이번 페이즈동안 피해를 받지 않음\n\n턴 시작시, 자신이 [JeannePartnerTwo] 1, [JeannePathos] 1을, 뫼르소가 [JeannePartner] 1, [JeanneLogos] 1을 얻음 (전투당 1회)\n\n일방공격을 당하거나 합 패배 시 ‘작은 다툼들도 있었지.’ 스킬 발동\n<color=#ff6000><mark color=#ff000040><b><u>뫼르소의 위 슬롯에 특정 스킬을 생성함</color></mark></b></u>
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152301].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [JeannePartnerTwo], [JeannePathos], [JeannePartner], [JeanneLogos]
   znaczenie tagów: [JeannePartnerTwo] = 에트르 뿌르 수아(être-pour-soi) / Être-pour-soi; [JeannePathos] = 파토스 - 데지르 데트르(désir d'être) / Pathos - Désir d'être; [JeannePartner] = 에트르 뿌르 오트뤼(être-pour-autrui) / Être-pour-autrui; [JeanneLogos] = 로고스 - 망끄 데트르(manque d'être) / Logos - Manque d'être
   EN: Does not take any damage for this Phase\n\nTurn Start (once per Encounter): \n- Jeanne gains 1 [JeannePartnerTwo] and 1 [JeannePathos]\n- Meursault gains 1 [JeannePartner] and 1 [JeanneLogos]\n\nWhen attacked by Unopposed Attacks, or when losing a Clash, activate the "We had our little quarrels, yes." Skill\n<color=#ff6000><mark color=#ff000040><b><u>Generate a unique Skill in Meursault's upper Skill Slot</color></mark></b></u>
   PL: nie otrzymuje żadnych obrażeń w tej Fazie\n\nPoczątek tury (1 raz na walkę):\n- Jeanne zyskuje 1 [JeannePartnerTwo] i 1 [JeannePathos]\n- Meursault zyskuje 1 [JeannePartner] i 1 [JeanneLogos]\n\nprzy otrzymaniu ataku jednostronnego albo przegranej w Starciu uruchamia Umiejętność „We had our little quarrels, yes.”\n<color=#ff6000><mark color=#ff000040><b><u>generuje unikalną Umiejętność w górnym slocie Umiejętności Meursaulta</u></b></mark></color>
325. [[a1c10p3] Pasywka wroga [152301] — tekst klimatyczny] 기억 속 왈츠, 다시 경험하는 거야.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152301].flavor
   limit: do 120 znaków
   EN: That waltz in your memory—let's re-experience it.
   PL: That waltz in your memory—let's re-experience it.
326. [[a1c10p3] Pasywka wroga [152302] — nazwa] 라 노제(la nausée)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152302].name
   limit: do 40 znaków
   EN: La Nausée
   PL: La Nausée
327. [[a1c10p3] Pasywka wroga [152302] — opis] 뫼르소가 사망하면, 수감자가 전투 패배함\n\n<color=#ff6000><mark color=#ff000040><b><u>자신의 [JeannePathos]가 100이면,</color></mark></b></u> 사용하고 있는 스킬 종료 시 페이즈 변경\n- 페이즈 변경 시 보유한 부정적인 효과 중 해제 가능한 효과를 제거함
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152302].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [JeannePathos]
   znaczenie tagów: [JeannePathos] = 파토스 - 데지르 데트르(désir d'être) / Pathos - Désir d'être
   EN: When Meursault is defeated, the Sinners lose the Encounter\n\nCurrent Skill End: <color=#ff6000><mark color=#ff000040><b><u>At 100 [JeannePathos]</color></mark></b></u>, enter a new Phase\n- When entering a new Phase, remove all removable negative effects on self
   PL: gdy Meursault zostanie pokonany, Grzesznicy przegrywają tę walkę\n\nKoniec aktualnej Umiejętności: <color=#ff6000><mark color=#ff000040><b><u>przy 100 [JeannePathos]</u></b></mark></color>, zmienia Fazę\n- przy zmianie Fazy usuwa wszystkie usuwalne negatywne efekty z siebie
328. [[a1c10p3] Pasywka wroga [152302] — tekst klimatyczny] 어지럽지? 하지만 절정은 이 다음이야.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152302].flavor
   limit: do 120 znaków
   EN: Feeling dizzy? But the climax comes next.
   PL: Feeling dizzy? But the climax comes next.
329. [[a1c10p3] Pasywka wroga [152401] — nazwa] 랑페르 쎄 레조트르(L'enfer, c'est les autres)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152401].name
   limit: do 60 znaków
   EN: L'enfer, c'est les autres
   PL: L'enfer, c'est les autres
330. [[a1c10p3] Pasywka wroga [152401] — opis] 잔느의 체력이 10% 이하가 된다면...
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152401].desc
   limit: do 120 znaków
   EN: When Jeanne's HP drops to 10% or below...
   PL: gdy HP Jeanne spadnie do 10% lub mniej...
331. [[a1c10p3] Pasywka wroga [152401] — tekst klimatyczny] 우리는 늘 타인의 시선에 못 박히는 지옥 속에서 살아가고 있어. 그러니… 네 감정을 모두 말해봐, 뫼르. 판단은 그다음에 내려도 되잖아?
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152401].flavor
   limit: do 240 znaków
   EN: We live in a hell where we're forever nailed beneath the gaze of others. So... tell me everything you're feeling, Meur. You can always decide what to make of it afterward, can't you?
   PL: Żyjemy w piekle, gdzie na zawsze jesteśmy przybici pod spojrzeniem innych. Więc... powiedz mi wszystko, co czujesz, Meur. Wyrok możesz wydać dopiero później, prawda?
332. [[a1c10p3] Pasywka wroga [152402] — nazwa] 시선: 시지프 백화점
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152402].name
   limit: do 40 znaków
   EN: Gaze: Grand Magasin Sisyphe
   PL: Gaze: Grand Magasin Sisyphe
333. [[a1c10p3] Pasywka wroga [152402] — opis] 정신력이 45로 고정됨\n\n턴 시작 시 시지프 시스템 설계도 - 르루주와 시지프 시스템 설계도 - 르누아르가 각각 2명이 되도록 소환함\n\n페이즈 변경 후 2턴째 부터 설계도 1명을 재단사 잔느 사르트르 형태로 변경함\n- [Vulnerable]이 없는 설계도 우선 변경됨\n- 이전 턴에 재단사 잔느 사르트르 상태가 된 설계도를 제외함\n- 흐트러짐 상태이면, 흐트러짐을 해제함\n\n재단사 잔느 사르트르 상태가 되었을 경우, ‘이 무대에서만큼은 모든게 정해져 있어.’ 스킬을 사용함\n- ‘이 무대에서만큼은 모든게 정해져 있어.’과의 합에서 뫼르소의 스킬이 승리했을 경우, 다음 턴 부터 해당 설계도가 매턴 [Vulnerable] 5 얻음\n\n재단사 잔느 사르트르 형태가 해제될 때마다, 다음 턴부터 설계도 중 1명이 잔느의 ‘권한: 차단’ 스킬을 장착함\n- 잔느의 스킬을 장착하는 설계도는 누적하여 1명씩 증가함\n\n설계도 사망 시, 아래 효과 적용\n- 잔느의 체력이 5% 감소함\n- 다른 설계도들이 [JeanneBlueprint] 1 얻음\n- 다음 턴에 설계도 중 1명이 잔느의 ‘권한: 차단’ 스킬 대신 ‘권한: 시선’ 스킬을 장착함
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152402].desc
   limit: do 1530 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable], [JeanneBlueprint]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [JeanneBlueprint] = 델레스망(délaissement) / Délaissement
   EN: This unit's SP is fixed at 45 \n\nTurn Start: Summon "Sisyphe System Blueprint - Le Rouge" and "Sisyphe System Blueprint - Le Noir" until there are 2 of each on the field\n\n2nd turn after Phase change: Convert 1 Blueprint unit into "Jeanne Sartre, the Sartorial Tailor" form\n- Prioritize the Blueprint unit that does not have [Vulnerable]\n- Exclude the Blueprint unit that entered the "Jeanne Sartre, the Sartorial Tailor" state on the previous turn\n- If Staggered, recover from Stagger\n\nWhen entering the "Jeanne Sartre, the Sartorial Tailor" state, use the "At least on this stage, everything's set and fixed." Skill\n- If Meursault's Skill wins the Clash against "At least on this stage, everything's set and fixed.", the said Blueprint unit gains 5 [Vulnerable] every turn starting from the next turn\n\nEvery time "Jeanne Sartre, the Sartorial Tailor" state is disabled, 1 Blueprint unit equips Jeanne's "Rights: Ban" Skill next turn\n- The number of Blueprint units that equip Jeanne's Skills increases cumulatively by 1\n\nWhen a Blueprint unit is defeated,\n- Jeanne loses 5% HP\n- All other Blueprint units gain 1 [JeanneBlueprint]\n- 1 Blueprint unit equips Jeanne's "Rights: Gaze" Skill instead of "Rights: Ban" next turn
   PL: SP tej jednostki jest stałe i wynosi 45\n\nPoczątek tury: przywołuje „Sisyphe System Blueprint - Le Rouge” i „Sisyphe System Blueprint - Le Noir” tak, by na polu było po 2 z każdego\n\nod 2. tury po zmianie Fazy zamienia 1 jednostkę Blueprint w postać „Jeanne Sartre, the Sartorial Tailor”\n- priorytet: jednostki Blueprint bez [Vulnerable]\n- z wyłączeniem jednostki Blueprint, która przeszła w stan „Jeanne Sartre, the Sartorial Tailor” w poprzedniej turze\n- jeżeli jest Oszołamiona, dochodzi do siebie\n\npo wejściu w stan „Jeanne Sartre, the Sartorial Tailor” używa Umiejętności „At least on this stage, everything's set and fixed.”\n- jeżeli Umiejętność Meursaulta wygra Starcie z „At least on this stage, everything's set and fixed.”, ta jednostka Blueprint od następnej tury zyskuje 5 [Vulnerable] co turę\n\nza każdym razem, gdy stan „Jeanne Sartre, the Sartorial Tailor” zostanie zdeaktywowany, od następnej tury 1 jednostka Blueprint wyposaża Umiejętność Jeanne „Rights: Ban”\n- liczba jednostek Blueprint wyposażających Umiejętności Jeanne rośnie łącznie o 1\n\npokonanie jednostki Blueprint uruchamia następujące efekty:\n- Jeanne traci 5% HP\n- wszystkie pozostałe jednostki Blueprint zyskują 1 [JeanneBlueprint]\n- od następnej tury 1 jednostka Blueprint wyposaża Umiejętność Jeanne „Rights: Gaze” zamiast „Rights: Ban”
334. [[a1c10p3] Pasywka wroga [152402] — tekst klimatyczny] 잔느에게는 백화점이야말로 자신이 가장 편하게 인식할 수 있는 세계였어.\n\n중립적이어야 하는 르카키의 업무를 배정받았지만, 지금 보이는 것처럼… 사실 누구보다 화려하게 피어나서, 무대 위에서 정열적으로 뫼르, 너와 춤을 추고 싶었던 거야.\n\n하지만… 잔느는 수많은 시선과 눈치라는 사슬에 얽매여서, 화려하게 피어나지 못했어. 피어나고자 하는 마음조차 드러내지 못했지.\n\n나는 잔느의 구토감을 없애줄 수는 없지만… 내던져진 이 세상에서 누구의 눈치도 보지 않고 피어나도록, 나다울 수 있도록 도와줄 거야. 열중하는 동안, 잠시 어지러움을 잊을 수 있게 말이지.\n\n그리고 이건… 잔느뿐만 아니라, 도시의 모든 사람에게 필요한 일이야. 설령 거절하더라도, 반드시 주어져야 하는 기회라고 생각해.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152402].flavor
   limit: do 1350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To Jeanne, the department store was the world she could perceive most comfortably.\n\nShe was given the office chair of Le Kaki's Giant, a role that was supposed to remain neutral. But as you can see for yourself... She wanted to bloom in all those brilliant colors more than anybody else. She wanted to burn with passion, Meur, to stand on that stage and dance with you.\n\nIt's unfortunate that she couldn't let herself do so. There were too many gazes to mind, too many expectations to satisfy... until they wound themselves around her like chains. She couldn't blossom vibrantly as she wanted. Even the budding wish had to be hidden away.\n\nI can't make Jeanne's nausea disappear, but I can give her the chance to be herself, to bloom as herself without worrying about anyone's gaze in this world she was thrown into. Perhaps, if she's deep in that passion, she'll get to forget the nausea for a little while.\n\nAnd... I don't think Jeanne is the only one who needs that. Everyone in the City does. They might refuse, but I do believe that everyone deserves the same chance.
   PL: Dla Jeanne dom towarowy był światem, który mogła postrzegać najwygodniej.\n\nOtrzymała biurko Giganta Le Kaki — rolę, która miała pozostać neutralna. Ale jak sam możesz zobaczyć... chciała rozkwitać we wszystkich tych wspaniałych barwach bardziej niż ktokolwiek. Chciała płonąć pasją, Meur, stać na scenie i tańczyć z tobą.\n\nNiestety nie mogła sobie na to pozwolić. Zbyt wiele spojrzeń, zbyt wiele oczekiwań... aż owinęły się wokół niej jak łańcuchy. Nie mogła rozkwitnąć tak, jak pragnęła. Nawet kiełkujące pragnienie musiała ukryć.\n\nNie mogę usunąć mdłości Jeanne, ale mogę dać jej szansę na bycie sobą — na rozkwitanie bez oglądania się na czyjś wzrok, w tym świecie, w który ją wrzucono. Może, gdy zanurzy się w tej pasji, na chwilę zapomni o mdłościach.\n\nI... nie sądzę, żeby tylko Jeanne tego potrzebowała. Wszyscy w Mieście. Mogą odmówić, ale wierzę, że każdy zasługuje na tę samą szansę.
335. [[a1c10p3] Pasywka wroga [152501] — nazwa] 의상 설계도
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152501].name
   limit: do 40 znaków
   EN: Outfit Ensemble Blueprint
   PL: Outfit Ensemble Blueprint
336. [[a1c10p3] Pasywka wroga [152501] — opis] 전투 중 <color=#ff6000><mark color=#ff000040><b><u>처음으로 피격</color></mark></b></u>받기 전, 자신의 타겟팅과 상관없이 <color=#ff6000><mark color=#ff000040><b><u>장착한 ‘백화점 설계도’를 사용함</color></mark></b></u> (턴당 1회)\n\n기본 스킬로 받는 피해량 -50%\n\n<color=#ff6000><mark color=#ff000040><b><u>E.G.O 스킬로 받는 피해량 +100%</color></mark></b></u>\n\n재단사 잔느 사르트르의 ‘포착’ 스킬 피격 시 사망함
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152501].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: During the Encounter, <color=#ff6000><mark color=#ff000040><b><u>immediately before taking a hit for the first time</color></mark></b></u>, <color=#ff6000><mark color=#ff000040><b><u>use the equipped "Department Store Blueprint"</color></mark></b></u> regardless of how this unit's Skills are Chained (once per turn)\n\nTake -50% damage from Base Skills\n\n<color=#ff6000><mark color=#ff000040><b><u>Take +100% damage from E.G.O Skills</color></mark></b></u>\n\nThis unit is defeated when hit by the "Focusing" Skill of "Jeanne Sartre, the Sartorial Tailor"
   PL: w trakcie walki <color=#ff6000><mark color=#ff000040><b><u>bezpośrednio przed pierwszym otrzymanym trafieniem</u></b></mark></color> <color=#ff6000><mark color=#ff000040><b><u>używa wyposażonego „Department Store Blueprint”</u></b></mark></color> niezależnie od tego, jak Umiejętności tej jednostki są Łączone (1 raz na turę)\n\notrzymuje -50% obrażeń od podstawowych Umiejętności\n\n<color=#ff6000><mark color=#ff000040><b><u>otrzymuje +100% obrażeń od Umiejętności E.G.O</u></b></mark></color>\n\nta jednostka zostaje pokonana, gdy zostanie trafiona Umiejętnością „Focusing” „Jeanne Sartre, the Sartorial Tailor”
337. [[a1c10p3] Pasywka wroga [152501] — tekst klimatyczny] 이것이 백화점의 설계도.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152501].flavor
   limit: do 120 znaków
   EN: This is the department store's blueprint.
   PL: This is the department store's blueprint.
338. [[a1c10p3] Pasywka wroga [152502] — nazwa] 자아 설계도
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152502].name
   limit: do 40 znaków
   EN: Blueprint of the Self
   PL: Blueprint of the Self
339. [[a1c10p3] Pasywka wroga [152502] — opis] 수감자의 스킬로 사망 시 가장 수량이 적은 E.G.O 자원 속성의 자원을 1개씩, 총 5개 지급\n(가장 적은 자원이 2개 이상일 경우, 무작위로 지급)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152502].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When killed by a Sinner's Skill, give 1 E.G.O resource each from 5 of the E.G.O Affinities with the least amount of resources (if 2 or more least-owned Affinities share the resource quantity, it is distributed randomly)
   PL: gdy zostaje pokonany Umiejętnością Grzesznika, daje po 1 zasobie E.G.O z 5 Afinności E.G.O z najmniejszą ilością zasobów (łącznie 5 zasobów)\n(jeżeli 2 lub więcej Afinności ma tyle samo zasobów, rozdzielane losowo)
340. [[a1c10p3] Pasywka wroga [152502] — tekst klimatyczny] 설계되지 않은 설계.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152502].flavor
   limit: do 120 znaków
   EN: Undesigned design.
   PL: Undesigned design.
341. [[a1c10p3] Pasywka wroga [152601] — nazwa] 패턴: 시지프 백화점
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152601].name
   limit: do 50 znaków
   EN: Pattern: Grand Magasin Sisyphe
   PL: Pattern: Grand Magasin Sisyphe
342. [[a1c10p3] Pasywka wroga [152601] — opis] 동일한 대상과의 합 진행 시 10합 당, 자신의 합 위력 1 증가\n\n등장 후 1턴 뒤 부터, 설계도 중 1명이 <color=#ff6000><mark color=#ff000040><b><u>재단사 잔느 사르트르 상태로 변경됨</color></mark></b></u>\n- [Vulnerable]이 없는 설계도 우선 변경됨\n- 이전 턴에 재단사 잔느 사르트르 상태가 된 설계도를 제외함\n- 흐트러짐 상태이면, 흐트러짐을 해제함\n\n재단사 잔느 사르트르 상태가 되었을 경우, <color=#ff6000><mark color=#ff000040><b><u>‘이 무대에서만큼은 모든게 정해져 있어.’ 스킬</color></mark></b></u>을 사용함\n- ‘이 무대에서만큼은 모든게 정해져 있어.’와의 합에서 <color=#ff6000><mark color=#ff000040><b><u>뫼르소의 스킬이 승리</color></mark></b></u>했을 경우, 다음 턴 부터 해당 설계도가 <color=#ff6000><mark color=#ff000040><b><u>매턴 [Vulnerable] 5 얻음</color></mark></b></u>\n\n설계도 사망 시 아래 효과 적용\n- <color=#ff6000><mark color=#ff000040><b><u>잔느의 체력이 5% 감소함</color></mark></b></u>\n- 다른 설계도들이 [JeanneBlueprint] 1 얻음
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152601].desc
   limit: do 1060 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Vulnerable], [JeanneBlueprint]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [JeanneBlueprint] = 델레스망(délaissement) / Délaissement
   EN: When Clashing against the same target, Clash Power +1 for every 10 Clashes\n\nStarting from the turn after this unit enters the field, 1 Blueprint unit enters the <color=#ff6000><mark color=#ff000040><b><u>"Jeanne Sartre, the Sartorial Tailor" state</color></mark></b></u>\n- Prioritize the Blueprint unit that does not have [Vulnerable]\n- Exclude the Blueprint unit that entered the "Jeanne Sartre, the Sartorial Tailor" state on the previous turn\n- If Staggered, recover from Stagger\n\nWhen entering the "Jeanne Sartre, the Sartorial Tailor" state, use the <color=#ff6000><mark color=#ff000040><b><u>"At least on this stage, everything's set and fixed." Skill</color></mark></b></u>\n- <color=#ff6000><mark color=#ff000040><b><u>If Meursault's Skill wins the Clash</color></mark></b></u> against "At least on this stage, everything's set and fixed.", the said Blueprint unit <color=#ff6000><mark color=#ff000040><b><u>gains 5 [Vulnerable] every turn</color></mark></b></u> starting from the next turn\n\nWhen a Blueprint unit is defeated,\n- <color=#ff6000><mark color=#ff000040><b><u>Jeanne loses 5% HP</color></mark></b></u>\n- All other Blueprint units gain 1 [JeanneBlueprint]
   PL: w Starciach z tym samym celem zyskuje Moc Starcia +1 za każde 10 Starć\n\nod tury po pojawieniu się na polu 1 jednostka Blueprint przechodzi w <color=#ff6000><mark color=#ff000040><b><u>stan „Jeanne Sartre, the Sartorial Tailor”</u></b></mark></color>\n- priorytet: jednostki Blueprint bez [Vulnerable]\n- z wyłączeniem jednostki Blueprint, która przeszła w stan „Jeanne Sartre, the Sartorial Tailor” w poprzedniej turze\n- jeżeli jest Oszołamiona, dochodzi do siebie\n\npo wejściu w stan „Jeanne Sartre, the Sartorial Tailor” używa <color=#ff6000><mark color=#ff000040><b><u>Umiejętności „At least on this stage, everything's set and fixed.”</u></b></mark></color>\n- jeżeli <color=#ff6000><mark color=#ff000040><b><u>Umiejętność Meursaulta wygra Starcie</u></b></mark></color> z „At least on this stage, everything's set and fixed.”, ta jednostka Blueprint <color=#ff6000><mark color=#ff000040><b><u>zyskuje 5 [Vulnerable] co turę</u></b></mark></color> od następnej tury\n\npokonanie jednostki Blueprint uruchamia następujące efekty:\n- <color=#ff6000><mark color=#ff000040><b><u>Jeanne traci 5% HP</u></b></mark></color>\n- wszystkie pozostałe jednostki Blueprint zyskują 1 [JeanneBlueprint]
343. [[a1c10p3] Pasywka wroga [152602] — nazwa] 대사작용
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152602].name
   limit: do 50 znaków
   EN: Metabolic Action and Reaction
   PL: Metabolic Action and Reaction
344. [[a1c10p3] Pasywka wroga [152602] — opis] 전투 중 누적으로 자신의 [ChargeRouge] 횟수를 10 소모할 때마다 [ChargeRouge] 위력 1 얻음\n\n자신의 스킬 효과로 체력이 감소할 때, 1 미만이 되지 않음
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152602].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation
   EN: Gain 1 [ChargeRouge] Potency for every 10 cumulative [ChargeRouge] Count this unit consumes in this Encounter\n\nThis unit's Skill effects cannot drop this unit's HP below 1
   PL: zyskuje 1 Siły [ChargeRouge] za każde 10 łącznie zużytych Liczników [ChargeRouge] tej jednostki w tej walce\n\nefekty Umiejętności tej jednostki nie mogą obniżyć jej HP poniżej 1
345. [[a1c10p3] Pasywka wroga [152602] — tekst klimatyczny] 섭취하고 충전하고 소모하고 다시 섭취한다. 단순한 반복은 갈망에 기인한다.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152602].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Consume, replenish, deplete, then consume again.\nSimple repetitions are born of yearning.
   PL: Spożywa, uzupełnia, zużywa, znów spożywa.\nProste powtórzenia rodzą się z tęsknoty.
346. [[a1c10p3] Pasywka wroga [152701] — nazwa] 보존
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152701].name
   limit: do 40 znaków
   EN: Conservation
   PL: Conservation
347. [[a1c10p3] Pasywka wroga [152701] — opis] 전투 중 누적으로 자신의 [ChargeNoir] 횟수를 10 소모할 때마다 [ChargeNoir] 위력 1 얻음
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152701].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: Gain 1 [ChargeNoir] Potency for every 10 cumulative [ChargeNoir] Count this unit consumes in this Encounter
   PL: zyskuje 1 Siły [ChargeNoir] za każde 10 łącznie zużytych Liczników [ChargeNoir] tej jednostki w tej walce
348. [[a1c10p3] Pasywka wroga [152701] — tekst klimatyczny] 응축하여 힘을 모아 고정한다. 변화시키지 않는 것이 변화시키는 것보다 더 큰 힘이 필요할 때가 있다.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152701].flavor
   limit: do 160 znaków
   EN: Force is compressed, gathered, and fixed in place. Sometimes, it takes more force to prevent change than to cause it.
   PL: Siła jest sprężana, zbierana i umacniana na miejscu. Czasem, żeby zapobiec zmianie, potrzeba większej siły niż by ją wywołać.
349. [[a1c10p3] Pasywka wroga [151701] — nazwa] 라 주이상스 오트르(la jouissance Autre)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151701].name
   limit: do 50 znaków
   EN: La Jouissance Autre
   PL: La Jouissance Autre
350. [[a1c10p3] Pasywka wroga [151701] — opis] 턴 종료 시 [ChargeRouge] 횟수가 감소하지 않음\n전투에서 [Laceration] 피해가 발동할 때마다 자신의 [ChargeRouge] 횟수 1 증가\n턴 시작 시 자신의 [ChargeRouge] 횟수 1당, 정신력 2 회복
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151701].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge], [Laceration]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation; [Laceration] = 출혈 / Bleed
   EN: Turn End: Does not lose [ChargeRouge] Count\nGain +1 [ChargeRouge] Count every time [Laceration] damage is activated in an Encounter\nTurn Start: Heal 2 SP for every [ChargeRouge] Count on self
   PL: Koniec tury: nie traci Liczników [ChargeRouge]\nzyskuje 1 Licznika [ChargeRouge] za każdym razem, gdy obrażenia [Laceration] uruchamiają się w walce\nPoczątek tury: przywraca 2 SP za każdą 1 Licznika [ChargeRouge] tej jednostki
351. [[a1c10p3] Pasywka wroga [151701] — tekst klimatyczny] 온몸으로 느끼지만, 말로 담을 수 없는 고동, 본성. 그 모든 맥동의 총체.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151701].flavor
   limit: do 170 znaków
   EN: A throbbing felt through the whole body, yet beyond the reach of words—the totality of every pulsation born of one's very nature.
   PL: Puls odczuwany całym ciałem, lecz poza zasięgiem słów — suma wszystkich pulsacji rodzących się z samej natury.
352. [[a1c10p3] Pasywka wroga [151701] — podsumowanie] 맥동 횟수 증가
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151701].summary
   limit: do 120 znaków
   EN: Gain Pulsation Count
   PL: zyskuje Licznik Pulsacji
353. [[a1c10p3] Pasywka wroga [151702] — nazwa] 렉스티미테(l'extimité)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151702].name
   limit: do 40 znaków
   EN: L'Extimité
   PL: L'Extimité
354. [[a1c10p3] Pasywka wroga [151702] — opis] 체력이 50% 감소된 채로 전투 시작\n스테이지 시작 시 모든 적에게 [BuffetScruple] 부여 (대기 인원 포함)\n\n스킬 사용 시 대상이 <color=#ff6000><mark=#ff000040><b><u>[BuffetScruple]을 보유</u></b></mark></color>했으면, 정신력 10 감소
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151702].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BuffetScruple]
   znaczenie tagów: [BuffetScruple] = 뿌이와의 경험 / Shared with Pwie
   EN: Start the Encounter with 50% missing HP\nEncounter Start: Apply [BuffetScruple] on all enemies (including Backup Units)\n\nOn Skill Use, <color=#ff6000><mark=#ff000040><b><u>if target has [BuffetScruple]</u></b></mark></color>, lose 10 SP
   PL: rozpoczyna tę walkę z 50% utraconego HP\nNa początku etapu: nakłada [BuffetScruple] na wszystkich wrogów (łącznie z jednostkami w rezerwie)\n\nprzy użyciu Umiejętności, <color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma [BuffetScruple]</u></b></mark></color>, traci 10 SP
355. [[a1c10p3] Pasywka wroga [151702] — tekst klimatyczny] …당신들은 나의 몸 가장 바깥에 있으면서도, 나의 가장 안쪽에 자리 잡고 있어.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151702].flavor
   limit: do 150 znaków
   EN: ... You're there at the very edge of my body, and yet somehow, you are also rooted in the deepest part of me.
   PL: ... Jesteście na samym skraju mojego ciała, a mimo to, jakoś tak, zakorzenieni jesteście także w jego najgłębszej części.
356. [[a1c10p3] Pasywka wroga [151702] — podsumowanie] 정신력 감소
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151702].summary
   limit: do 120 znaków
   EN: Lose SP
   PL: traci SP
357. [[a1c10p3] Pasywka wroga [151703] — nazwa] 르 무아(le moi)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151703].name
   limit: do 40 znaków
   EN: Le Moi
   PL: Le Moi
358. [[a1c10p3] Pasywka wroga [151703] — opis] [BuffetScruple]을 가진 수감자가 특정 스킬과 합 승리 시\n<color=#ff6000><mark=#ff000040><b><u>붉은 신이 [BuffetDream] 1 얻음</u></b></mark></color>\n[BuffetDream]이 5가 되면 패턴이 변경되며, 변경된 패턴의 스킬과 합 승리 시 전투 승리\n\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]의 위력이 최대 50까지 누적되고 횟수는 최대 15까지 누적됨\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 체력, 정신력 피해량 -50%\n패닉 변경 불가\n턴 종료 시 패닉 상태라면 정신력이 0이 됨
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151703].desc
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BuffetScruple], [BuffetDream], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [BuffetScruple] = 뿌이와의 경험 / Shared with Pwie; [BuffetDream] = 뿌이의 기억 / Pwie's Memories; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: When the Sinner who has [BuffetScruple] wins a Clash against a certain Skill, <color=#ff6000><mark=#ff000040><b><u>The Crimson God gains 1 [BuffetDream]</u></b></mark></color>\nWhen The Crimson God reaches 5 [BuffetDream] Stacks, it gains a new pattern; winning the Clash against the Skill in that new pattern will win the Encounter\n\nRaise max Potency and Count cap for [Combustion], [Laceration], [Vibration], [Burst], and [Sinking] to 50 and 15, respectively\n\nTake -50% HP and SP damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]\n- Fixed Panic\n- Turn End: If this unit is in Panic, SP becomes 0
   PL: gdy Grzesznik mający [BuffetScruple] wygra Starcie z określoną Umiejętnością, <color=#ff6000><mark=#ff000040><b><u>The Crimson God zyskuje 1 [BuffetDream]</u></b></mark></color>\ngdy The Crimson God osiągnie 5 Stosów [BuffetDream], przybiera nowy wzorzec; wygranie Starcia z Umiejętnością w tym nowym wzorcu wygrywa walkę\n\npodnosi maks. wartość Siły i Liczników [Combustion], [Laceration], [Vibration], [Burst] i [Sinking] odpowiednio do 50 i 15\n\notrzymuje -50% obrażeń HP i SP od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]\n- Panika zablokowana\n- Koniec tury: jeżeli ta jednostka jest w Panice, jej SP wynosi 0
359. [[a1c10p3] Pasywka wroga [151703] — tekst klimatyczny] 나. 물속에 비친 나의 모습을 봤어. 난 완전한 몸을 지녔어…
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151703].flavor
   limit: do 120 znaków
   EN: I saw my reflection in the water. My body, it's been... completed...
   PL: Zobaczyłem swoje odbicie w wodzie. Moje ciało zostało... ukończone...
360. [[a1c10p3] Pasywka wroga [151704] — nazwa] 푸부아르 드 라 비(Pouvoirs de la vie)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151704].name
   limit: do 50 znaków
   EN: Pouvoirs de la vie
   PL: Pouvoirs de la vie
361. [[a1c10p3] Pasywka wroga [151704] — opis] 아군이 피해로 인한 흐트러짐 상태가 되면,\n<color=#ff6000><mark=#ff000040><b><u>대상 아군의 흐트러짐을 해제하고 원호 공격</u></b></mark></color>을 시키는 '르 망카에트르' 사용 (턴당 1회)\n\n아군이 사망하면, 다음 턴 시작 시 [BuffetRevival] 3을 보유한 붉은 신의 뜯긴 살점 소환
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151704].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BuffetRevival]
   znaczenie tagów: [BuffetRevival] = 붉은 신의 목소리 / Voice of the Crimson God
   EN: If an ally becomes Staggered due to damage, <color=#ff6000><mark=#ff000040><b><u>un-Stagger the ally, then use the "Le Manque-à-être" Skill that activates the said ally's <noparse>Assist Attack</noparse></u></b></mark></color> (once per turn)\n\nIf an ally is defeated, summon a Ripped Flesh of the Crimson God that has 3 [BuffetRevival] at the next Turn Start
   PL: gdy sojusznik przechodzi w Oszołamienie z powodu obrażeń, <color=#ff6000><mark=#ff000040><b><u>przywraca sojusznika z Oszołamienia, po czym używa Umiejętności „Le Manque-à-être” wywołującej <noparse>Atak Wsparcia</noparse> tego sojusznika</u></b></mark></color> (1 raz na turę)\n\npo śmierci sojusznika, na początku następnej tury przywołuje Ripped Flesh of the Crimson God posiadającego 3 [BuffetRevival]
362. [[a1c10p3] Pasywka wroga [151704] — tekst klimatyczny] 태어나게 하는 폭력성. 르루주의 신은 탄생의 권능을 가진다.\n\n죽으면 의식은 어디로 가는가? 태어나기 전, 의식은 어디에서 오는가?\n\n그곳으로 내보내고, 끄집어내는 것은 모두 동일한 폭력적인 권능이다.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151704].flavor
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The violence by which things are brought into being. The God of the Rouges possesses the authority of birth.\n\nWhere does consciousness go when we die? And before we are born, from where does it emerge?\n\nTo send it back to that place, or to tear it forth from there... both are workings of the same violent power.
   PL: Przemoc powodująca, że rzeczy powstają. Bóg Rouge posiada władzę narodzin.\n\nDokąd podąża świadomość, gdy umieramy? A zanim się rodzimy — skąd się bierze?\n\nOdesłanie jej tam i wyrwanie jej stamtąd... to działanie tej samej brutalnej władzy.
363. [[a1c10p3] Pasywka wroga [151705] — nazwa] 라 주이상스 팔리크(la jouissance phallique)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151705].name
   limit: do 50 znaków
   EN: La Jouissance phallique
   PL: La Jouissance phallique
364. [[a1c10p3] Pasywka wroga [151705] — opis] 턴 시작 시 [BuffetRouge] 상태가 아닐 때,\n자신의 [ChargeRouge] 횟수가 15 이상이면,\n[ChargeRouge] 횟수를 모두 소모하여 [BuffetRouge]를 최대로 얻음.\n소모한 [ChargeRouge] 횟수 1당 정신력 2 회복\n\n스킬 사용 시 [BuffetRouge] 상태가 아니고,\n자신의 [ChargeRouge] 횟수가 10 이상이면,\n[ChargeRouge] 횟수를 10 소모하여 코인 위력 +1
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151705].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [BuffetRouge], [ChargeRouge]
   znaczenie tagów: [BuffetRouge] = 폭주[르 데지르] / Uncontrollable Rampage [Le Désir]; [ChargeRouge] = 맥동 / Pulsation
   EN: Turn Start: If this unit does not have [BuffetRouge] and is at 15+ [ChargeRouge] Count, consume all [ChargeRouge] Count and gain up to max [BuffetRouge] Stack; then, heal 2 SP for every [ChargeRouge] Count consumed\n\nOn Skill Use, if this unit does not have [BuffetRouge] and is at 10+ [ChargeRouge] Count, consume 10 [ChargeRouge] Count to gain Coin Power +1
   PL: Początek tury: jeżeli ta jednostka nie ma [BuffetRouge] i ma 15+ Licznika [ChargeRouge], zużywa wszystkie Liczniki [ChargeRouge] i zyskuje Stosy [BuffetRouge] do maksimum; następnie przywraca 2 SP za każdą 1 zużytego Licznika [ChargeRouge]\n\nprzy użyciu Umiejętności, jeżeli ta jednostka nie ma [BuffetRouge] i ma 10+ Licznika [ChargeRouge], zużywa 10 Licznika [ChargeRouge], aby zyskać Moc Monety +1
365. [[a1c10p3] Pasywka wroga [151705] — tekst klimatyczny] 생의 향락을 누리는 것에 조건이 붙는다. 조건이 붙는 이상, 육체적 쾌락은 한계와 끝을 지니고, 필연적으로 실패한다.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151705].flavor
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There are conditions to tasting the pleasures of life, and as it is with all things conditional, this carnal pleasure is fated to fail.\n\nThe stipulated limits and end have deemed it so.
   PL: Smakowanie rozkoszy życia podlega warunkom. A skoro podlega warunkom, cielesna rozkosz ma granice i kres — i z konieczności kończy się fiaskiem.\n\nWyznaczone limity i kres przesądziły o tym.
366. [[a1c10p3] Pasywka wroga [151705] — podsumowanie] 맥동 횟수를 소모하여, 코인 위력 증가
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151705].summary
   limit: do 120 znaków
   EN: Consume Pulsation Count to gain Coin Power
   PL: zużywa Licznik Pulsacji, aby zyskać Moc Monety
367. [[a1c10p3] Pasywka wroga [151706] — nazwa] 라 무아송(la moisson)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151706].name
   limit: do 40 znaków
   EN: La Moisson
   PL: La Moisson
368. [[a1c10p3] Pasywka wroga [151706] — opis] 공격 종료 시 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>[BoneNail]가 5 이상</u></b></mark></color>이면,\n공격한 메인 타겟에게 <color=#ff6000><mark=#ff000040><b><u>'강력한 스킬'</u></b></mark></color> 사용 (턴당 1회)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151706].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BoneNail]
   znaczenie tagów: [BoneNail] = 라브젝트(l'abject) / L'Abject
   EN: Attack End: If the main target has <color=#ff6000><mark=#ff000040><b><u>5+ [BoneNail]</u></b></mark></color>, use <color=#ff6000><mark=#ff000040><b><u>a powerful Skill</u></b></mark></color> against the main target this unit attacked (once per turn)
   PL: po zakończeniu ataku, jeżeli główny cel ma <color=#ff6000><mark=#ff000040><b><u>5+ [BoneNail]</u></b></mark></color>,\nużywa <color=#ff6000><mark=#ff000040><b><u>potężnej Umiejętności</u></b></mark></color> przeciwko zaatakowanemu głównemu celowi (1 raz na turę)
369. [[a1c10p3] Pasywka wroga [151706] — tekst klimatyczny] 밀어내어진 부속기관은 타인에게 박혀, 경계 밖에서 계속 나를 부른다.\n\n태어난 곳으로 되돌아가고 싶은 충동은 죽음의 충동인가, 혹은 삶의 충동인가.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151706].flavor
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The jutting appendage is thrust into another, calling me from beyond the periphery.\n\nIs this compulsion to return to my birthplace an impulse for death, or impulse for life?
   PL: Wypchnięty narząd zostaje wbity w innego i woła mnie spoza granicy.\n\nCzy ten przymus powrotu do miejsca narodzin to popęd śmierci, czy popęd życia?
370. [[a1c10p3] Pasywka wroga [151707] — nazwa] 르 브주앵(le besoin)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151707].name
   limit: do 40 znaków
   EN: Le Besoin
   PL: Le Besoin
371. [[a1c10p3] Pasywka wroga [151707] — opis] [ChargeRouge] 횟수를 누적해서 10 소모할 때마다 맥동 위력 1 증가\n\n자신의 [ChargeRouge] 위력에 따라, 다음 효과를 전부 얻음\n- 1 : 자신보다 느린 대상에게 가하는 피해량 +([ChargeRouge] 위력 x 20)%\n- 2 : 스킬의 최종 위력 +1\n- 3 : 스킬로 부여하는 [Laceration] 위력 부여량 +1\n- 4 : 스킬의 코인 위력 +1\n- 5 : 자신의 [BuffetRouge]가 감소하지 않음
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151707].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge], [Laceration], [BuffetRouge]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation; [Laceration] = 출혈 / Bleed; [BuffetRouge] = 폭주[르 데지르] / Uncontrollable Rampage [Le Désir]
   EN: Gain 1 Pulsation Potency for every 10 cumulative [ChargeRouge] Count this unit consumes in this Encounter\n\nGain all of the following effects based on [ChargeRouge] Potency on self:\n- 1+: Deal +([ChargeRouge] Potency x 20)% damage if this unit's Speed is faster than the target's\n- 2+: Skill Final Power +1\n- 3+: Skills inflict +1 more [Laceration] Potency\n- 4+: Skill Coin Power +1\n- 5+: Do not lose [BuffetRouge] Stack on self
   PL: zyskuje 1 Siły Pulsacji za każde 10 łącznie zużytych Liczników [ChargeRouge] tej jednostki w tej walce\n\nzyskuje wszystkie poniższe efekty zależnie od Siły [ChargeRouge] tej jednostki:\n- 1+: zadaje +(Siła [ChargeRouge] x 20)% obrażeń, jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu\n- 2+: Moc Końcowa Umiejętności +1\n- 3+: Umiejętności nakładają dodatkowo +1 Siły [Laceration]\n- 4+: Moc Monety Umiejętności +1\n- 5+: nie traci Stosów [BuffetRouge]
372. [[a1c10p3] Pasywka wroga [151707] — tekst klimatyczny] 살아있기 때문에. 태어나 버렸기 때문에.\n저주와도 같이 찾아오는 육체적인, 필연적인, 그렇기에 운명적인 욕망.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151707].flavor
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The destined and inevitable desire of those who live, those who are birthed.\nA curselike need, its inescapability threaded by fate.
   PL: Przeznaczona i nieunikniona pożądliwość żyjących, tych, którzy przyszli na świat.\nPotrzeba jak przekleństwo, której nieuchronność przeplata się z losem.
373. [[a1c10p3] Pasywka wroga [151707] — podsumowanie] 맥동 위력에 따라 스킬 강화
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151707].summary
   limit: do 120 znaków
   EN: Enhance Skills based on Pulsation Potency
   PL: wzmacnia Umiejętności zależnie od Siły Pulsacji
374. [[a1c10p3] Pasywka wroga [151708] — nazwa] 답을 주어야 할 때
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151708].name
   limit: do 40 znaków
   EN: Time to Answer
   PL: Time to Answer
375. [[a1c10p3] Pasywka wroga [151708] — opis] 다음 조건 중 1개를 만족하면 패턴이 변경됨\n- <color=#ff6000><mark=#ff000040><b><u>[BuffetDream] 3 보유</u></b></mark></color>\n- 현재 체력이 최대 체력의 25% 미만으로 내려감
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151708].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BuffetDream]
   znaczenie tagów: [BuffetDream] = 뿌이의 기억 / Pwie's Memories
   EN: If any of the following conditions are met, change the pattern:\n- <color=#ff6000><mark=#ff000040><b><u>[BuffetDream] is at 3 Stacks</u></b></mark></color>\n- Current HP falls below 25% of max HP
   PL: jeżeli spełniony jest 1 z poniższych warunków, przybiera nowy wzorzec:\n- <color=#ff6000><mark=#ff000040><b><u>posiada 3 Stosy [BuffetDream]</u></b></mark></color>\n- aktualne HP spada poniżej 25% Maks. HP
376. [[a1c10p3] Pasywka wroga [151708] — tekst klimatyczny] 내게 알려줘… 데려가 줘…
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151708].flavor
   limit: do 120 znaków
   EN: Keep teaching me things... I wanna go with you...
   PL: Keep teaching me things... I wanna go with you...
377. [[a1c10p3] Pasywka wroga [152101] — nazwa] 비울수록 채워지리라
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152101].name
   limit: do 40 znaków
   EN: Emptiness Begets Satiation
   PL: Emptiness Begets Satiation
378. [[a1c10p3] Pasywka wroga [152101] — opis] 전투 중 누적으로 자신의 [ChargeRouge] 횟수를 10 소모할 때마다 [ChargeRouge] 위력 1 얻음\n스킬 사용 시 [ChargeRouge] 위력 3 이상이면, 코인 위력 +1\n\n잃은 체력 20%당, 공격 레벨 1 증가(최대 3), 가하는 피해량 +20%(최대 60%)
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152101].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation
   EN: Gain 1 [ChargeRouge] Potency for every 10 cumulative [ChargeRouge] Count this unit consumes in this Encounter\n\nOn Skill Use, at 3+ [ChargeRouge] Potency, Coin Power +1\n\nGain 1 Offense Level (max 3) and deal +20% damage (max 60%) for every 20% missing HP
   PL: zyskuje 1 Siły [ChargeRouge] za każde 10 łącznie zużytych Liczników [ChargeRouge] tej jednostki w tej walce\nprzy użyciu Umiejętności, przy 3+ Siły [ChargeRouge], Moc Monety +1\n\nzyskuje Poziom Ataku +1 (maks. 3) i zadaje +20% obrażeń (maks. 60%) za każde 20% utraconego HP
379. [[a1c10p3] Pasywka wroga [152101] — podsumowanie] 코인 위력 증가
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152101].summary
   limit: do 120 znaków
   EN: Gain Coin Power
   PL: zyskuje Moc Monety
380. [[a1c10p3] Pasywka wroga [152102] — nazwa] 느린 목을 노리는 낫
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152102].name
   limit: do 40 znaków
   EN: The Sickle Seeks the Slow
   PL: The Sickle Seeks the Slow
381. [[a1c10p3] Pasywka wroga [152102] — opis] 자신보다 속도가 느린 대상을 우선으로 지정\n스킬 사용 시 대상보다 속도가 빠르면, 대상과 자신의 속도 차이만큼 공격 레벨 증가\n턴 시작 시 자신의 [ChargeRouge] 위력이 3 이상이면, 강력한 스킬을 사용
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152102].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation
   EN: Prioritize targets with slower Speed than self\n\nOn Skill Use, if this unit's Speed is faster than the target's gain Offense Level equal to the Speed difference\n\nTurn Start: At 3+ [ChargeRouge] Potency, use a powerful Skill
   PL: priorytet: cele o Szybkości niższej niż własna\n\nprzy użyciu Umiejętności, jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, zyskuje Poziom Ataku równy różnicy Szybkości\n\nPoczątek tury: przy 3+ Siły [ChargeRouge] używa potężnej Umiejętności
382. [[a1c10p3] Pasywka wroga [152102] — tekst klimatyczny] 맥동하는 포식자는 느린 목을 노리고, 그 차이만큼 치명적인 피해를 가한다.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152102].flavor
   limit: do 180 znaków
   EN: Pulsating predators pursue the slow prey, seeking to sink their fangs into the neck. Their fatality is determined by the speed differential.
   PL: Pulsujący drapieżcy polują na powolne karki, a ich śmiertelność zależy od różnicy prędkości.
383. [[a1c10p3] Pasywka wroga [152103] — nazwa] 그분 곁에서 식지 않는 맥동
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152103].name
   limit: do 70 znaków
   EN: Persistent Pulsation Beside The Cherished One
   PL: Persistent Pulsation Beside The Cherished One
384. [[a1c10p3] Pasywka wroga [152103] — opis] 전장에 붉은 신이 있으면, 턴 종료 시 자신의 [ChargeRouge] 횟수가 감소하지 않음\n\n피격으로 인해 흐트러짐 상태가 되었을 때, 붉은 신의 스킬로 흐트러짐 상태에서 해제되면, 자신을 공격했던 대상에게 스킬'이 낫으로 답하나이다!'로 일방공격
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152103].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation
   EN: When The Crimson God is on the field, this unit does not lose [ChargeRouge] Count at Turn End\n\nWhen Staggered due to getting hit: When this unit recovers from Stagger due to The Crimson God's Skill, use "With sickles mine I answer your calling!" as Unopposed Attack against the attacker
   PL: gdy The Crimson God jest na polu, ta jednostka nie traci Liczników [ChargeRouge] na Koniec tury\n\ngdy przechodzi w Oszołamienie od trafienia: gdy ta jednostka dochodzi do siebie po Oszołamieniu dzięki Umiejętności The Crimson God, używa „With sickles mine I answer your calling!” jako atak jednostronny na atakującego
385. [[a1c10p3] Pasywka wroga [152103] — tekst klimatyczny] 숨이, 박동이 멈추지 않는다. 멈추고 싶다 해도, 멈추지 않는다.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152103].flavor
   limit: do 120 znaków
   EN: Against their wishes, neither breathing nor the thumping pulse in their hearts would stop.
   PL: Oddech i tętno nie ustają. Nawet jeśli chcą się zatrzymać — nie ustają.
386. [[a1c10p3] Pasywka wroga [152104] — nazwa] 삶의 흔적
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152104].name
   limit: do 40 znaków
   EN: Traces of Life
   PL: Traces of Life
387. [[a1c10p3] Pasywka wroga [152104] — opis] 사망 시 적 진영에 수량이 가장 적은 E.G.O 자원 중 무작위 속성 자원 2개 지급
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152104].desc
   limit: do 120 znaków
   EN: Upon death, grant 2 E.G.O Resource of a random Affinity among least-owned Affinities
   PL: po śmierci daje 2 zasoby E.G.O losowej Afinności spośród Afinności z najmniejszą liczbą zasobów
388. [[a1c10p3] Pasywka wroga [152104] — tekst klimatyczny] 누군가 살아가는, 살아갔던 흔적.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152104].flavor
   limit: do 120 znaków
   EN: Traces left behind by those who live, those who lived.
   PL: Ślady czyjegoś życia — tego, kto żyje, i tego, który żył.
389. [[a1c10p3] Pasywka wroga [152105] — nazwa] 살에 내리는 은총
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152105].name
   limit: do 40 znaków
   EN: Blessings Upon the Flesh
   PL: Blessings Upon the Flesh
390. [[a1c10p3] Pasywka wroga [152105] — opis] <color=#ff6000><mark=#ff000040><b><u>[BuffetRouge]가 있으면</u></b></mark></color> 다음 효과 발동\n- 스킬로 받는 피해량 -50%\n- 턴 시작 시 정신력이 최대치로 증가, [ChargeRouge] 1 얻음. 자신의 [ChargeRouge] 횟수 5 증가
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152105].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BuffetRouge], [ChargeRouge]
   znaczenie tagów: [BuffetRouge] = 폭주[르 데지르] / Uncontrollable Rampage [Le Désir]; [ChargeRouge] = 맥동 / Pulsation
   EN: <color=#ff6000><mark=#ff000040><b><u>If this unit has [BuffetRouge]</u></b></mark></color>, apply the following effects:\n- Take -50% damage from Skills\n- Turn Start: Heal SP to max and gain 1 [ChargeRouge]; gain +5 [ChargeRouge] Count
   PL: <color=#ff6000><mark=#ff000040><b><u>jeżeli ta jednostka ma [BuffetRouge]</u></b></mark></color>, uruchamia następujące efekty:\n- otrzymuje -50% obrażeń od Umiejętności\n- Początek tury: przywraca SP do maksimum i zyskuje 1 [ChargeRouge]; zyskuje 5 Licznika [ChargeRouge]
391. [[a1c10p3] Pasywka wroga [152105] — tekst klimatyczny] 온몸으로 그 권능을 받아낸다.
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=152105].flavor
   limit: do 120 znaków
   EN: To receive that divinity whole with one's body.
   PL: Przyjmuje tę władzę całym ciałem.
392. [[a1c10p3] Pasywka wroga [151801] — nazwa] 다시 살아지는 육체
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151801].name
   limit: do 40 znaków
   EN: Body Forced to Live Again
   PL: Body Forced to Live Again
393. [[a1c10p3] Pasywka wroga [151801] — opis] [BuffetRevival] 소멸 시 본래의 모습(르루주 고위 스태프)으로 돌아가며, 붉은 신의 뜯긴 살점 상태에서 남아있던 체력 10 당, 정신력 5 회복. [ChargeRouge] 횟수 2 얻음\n- 얻은 [ChargeRouge] 횟수가 10 이상이면, [ChargeRouge] 횟수를 모두 소모하고 소모한 수치 5당, 다음 턴에 [BuffetRouge] 1 얻음
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151801].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [BuffetRevival], [ChargeRouge], [BuffetRouge]
   znaczenie tagów: [BuffetRevival] = 붉은 신의 목소리 / Voice of the Crimson God; [ChargeRouge] = 맥동 / Pulsation; [BuffetRouge] = 폭주[르 데지르] / Uncontrollable Rampage [Le Désir]
   EN: When [BuffetRevival] expires, return to Le Rouge Senior Staff form; heal 5 SP for every 10 HP that remained while this unit was in Ripped Flesh of the Crimson God form; gain +2 [ChargeRouge] Count\n- If this unit gained 10+ [ChargeRouge] Count, consume all [ChargeRouge] Count; then, gain 1 [BuffetRouge] next turn for every 5 Stacks consumed
   PL: gdy [BuffetRevival] wygasa, wraca do postaci Le Rouge Senior Staff; przywraca 5 SP za każde 10 HP, które pozostały tej jednostce w postaci Ripped Flesh of the Crimson God; zyskuje 2 Licznika [ChargeRouge]\n- jeżeli zyskane Liczniki [ChargeRouge] osiągnęły 10+, zużywa wszystkie Liczniki [ChargeRouge]; następnie zyskuje 1 [BuffetRouge] w następnej turze za każde 5 zużytych Stosów
394. [[a1c10p3] Pasywka wroga [151802] — nazwa] 땅에 눌어붙은 살점
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151802].name
   limit: do 40 znaków
   EN: Flesh Gummed to the Ground
   PL: Flesh Gummed to the Ground
395. [[a1c10p3] Pasywka wroga [151802] — opis] 수감자들이 타겟으로 지정할 수 없음
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151802].desc
   limit: do 120 znaków
   EN: Sinners cannot target this unit
   PL: Grzesznicy nie mogą wskazać tej jednostki jako celu
396. [[a1c10p3] Pasywka wroga [151709] — nazwa] 밀어내지도, 쥐어내지도 못한 손
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151709].name
   limit: do 70 znaków
   EN: The hand they could neither push away nor hold
   PL: The hand they could neither push away nor hold
397. [[a1c10p3] Pasywka wroga [151709] — opis] 턴 시작 시 전장의 르루주 고위 스태프 1명당, [Protection] 2 얻음\n- 르루주 고위 스태프가 사망할 때마다 [Protection] 2 감소\n\n<color=#ff6000><mark=#ff000040><b><u>르루주 고위 스태프가 모두 사망한 상태</u></b></mark></color>이면, 다음 효과 적용\n- [Vulnerable] 2 얻음\n- 스킬 사용 시 대상이 <color=#ff6000><mark=#ff000040><b><u>[BuffetScruple]을 보유했으면, 코인 위력 -1</u></b></mark></color>
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151709].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Protection], [Vulnerable], [BuffetScruple]
   znaczenie tagów: [Protection] = 보호 / Protection; [Vulnerable] = 취약 / Fragile; [BuffetScruple] = 뿌이와의 경험 / Shared with Pwie
   EN: Turn Start: Gain 2 [Protection] for every Le Rouge Senior Staff on the field\n- Lose 2 [Protection] every time a Le Rouge Senior Staff is defeated\n\n<color=#ff6000><mark=#ff000040><b><u>If all Le Rouge Senior Staff are defeated</u></b></mark></color>, apply the following effects:\n- Gain 2 [Vulnerable]\n- On Skill Use, <color=#ff6000><mark=#ff000040><b><u>if target has [BuffetScruple], Coin Power -1</u></b></mark></color>
   PL: Początek tury: zyskuje 2 [Protection] za każdego Le Rouge Senior Staff na polu\n- traci 2 [Protection] za każdym razem, gdy Le Rouge Senior Staff zostanie pokonany\n\njeżeli <color=#ff6000><mark=#ff000040><b><u>wszyscy Le Rouge Senior Staff zostali pokonani</u></b></mark></color>, stosuje następujące efekty:\n- zyskuje 2 [Vulnerable]\n- przy użyciu Umiejętności, jeżeli cel <color=#ff6000><mark=#ff000040><b><u>ma [BuffetScruple], Moc Monety -1</u></b></mark></color>
398. [[a1c10p3] Pasywka wroga [151709] — tekst klimatyczny] 손… 아직 잡아줄 거야…?
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151709].flavor
   limit: do 120 znaków
   EN: Will you still... hold my hand?
   PL: Will you still... hold my hand?
399. [[a1c10p3] Pasywka wroga [151709] — podsumowanie] 코인 위력 감소
   źródło: Passives_Abnormality-a1c10p3.json :: dataList[id=151709].summary
   limit: do 120 znaków
   EN: Lose Coin Power
   PL: traci Moc Monety

## [a1c5p1] Wróg / część: Enemies-a1c5p1
- plik gry: `Enemies-a1c5p1.json`

400. [[a1c5p1] Wróg / część [90083] — nazwa] 구멍 손바닥 고래 인어
   źródło: Enemies-a1c5p1.json :: dataList[id=90083].name
   limit: do 50 znaków
   EN: Whale of the Porous Hand Mermaid
   PL: Whale of the Porous Hand Mermaid
401. [[a1c5p1] Wróg / część [90083] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=90083].desc
   limit: do 120 znaków
   EN: Core
   PL: Core
402. [[a1c5p1] Wróg / część [90084] — nazwa] 쌍갈고리 해적단 콧수염 조직원
   źródło: Enemies-a1c5p1.json :: dataList[id=90084].name
   limit: do 50 znaków
   EN: Moustachioed Twinhooks Pirate
   PL: Moustachioed Twinhooks Pirate
403. [[a1c5p1] Wróg / część [90084] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=90084].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [[a1c5p1] Wróg / część [90085] — nazwa] 쌍갈고리 해적단 반다나 조직원
   źródło: Enemies-a1c5p1.json :: dataList[id=90085].name
   limit: do 50 znaków
   EN: Bandana-wearing Twinhooks Pirate
   PL: Bandana-wearing Twinhooks Pirate
405. [[a1c5p1] Wróg / część [90085] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=90085].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [[a1c5p1] Wróg / część [90086] — nazwa] 쌍갈고리 해적단 날렵한 조직원
   źródło: Enemies-a1c5p1.json :: dataList[id=90086].name
   limit: do 40 znaków
   EN: Agile Twinhooks Pirate
   PL: Agile Twinhooks Pirate
407. [[a1c5p1] Wróg / część [90086] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=90086].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [[a1c5p1] Wróg / część [90087] — nazwa] 쌍갈고리 해적단 든든한 조직원
   źródło: Enemies-a1c5p1.json :: dataList[id=90087].name
   limit: do 40 znaków
   EN: Tough Twinhooks Pirate
   PL: Tough Twinhooks Pirate
409. [[a1c5p1] Wróg / część [90087] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=90087].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [[a1c5p1] Wróg / część [91011] — nazwa] 구멍 손바닥 고래 병정 인어
   źródło: Enemies-a1c5p1.json :: dataList[id=91011].name
   limit: do 60 znaków
   EN: Whale of the Porous Hand Soldier Mermaid
   PL: Whale of the Porous Hand Soldier Mermaid
411. [[a1c5p1] Wróg / część [91011] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=91011].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [[a1c5p1] Wróg / część [91012] — nazwa] 쌍갈고리 해적단 부선장 스미
   źródło: Enemies-a1c5p1.json :: dataList[id=91012].name
   limit: do 50 znaków
   EN: Twinhook Pirates First Mate Smee
   PL: Twinhook Pirates First Mate Smee
413. [[a1c5p1] Wróg / część [91012] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=91012].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [[a1c5p1] Wróg / część [97401] — nazwa] 두려워하는 K사 검문소 요원
   źródło: Enemies-a1c5p1.json :: dataList[id=97401].name
   limit: do 60 znaków
   EN: Terrified K Corp. Checkpoint Security
   PL: Terrified K Corp. Checkpoint Security
415. [[a1c5p1] Wróg / część [97401] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=97401].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [[a1c5p1] Wróg / część [97402] — nazwa] 굳어있는 K사 검문소 요원
   źródło: Enemies-a1c5p1.json :: dataList[id=97402].name
   limit: do 60 znaków
   EN: Stiffened K Corp. Checkpoint Security
   PL: Stiffened K Corp. Checkpoint Security
417. [[a1c5p1] Wróg / część [97402] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=97402].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [[a1c5p1] Wróg / część [97403] — nazwa] 위협받는 K사 1등급 직원
   źródło: Enemies-a1c5p1.json :: dataList[id=97403].name
   limit: do 50 znaków
   EN: Threatened K Corp. Class 1 Staff
   PL: Threatened K Corp. Class 1 Staff
419. [[a1c5p1] Wróg / część [97403] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=97403].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [[a1c5p1] Wróg / część [97404] — nazwa] 불안한 K사 1등급 직원
   źródło: Enemies-a1c5p1.json :: dataList[id=97404].name
   limit: do 50 znaków
   EN: Unnerved K Corp. Class 1 Staff
   PL: Unnerved K Corp. Class 1 Staff
421. [[a1c5p1] Wróg / część [97404] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=97404].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [[a1c5p1] Wróg / część [97405] — nazwa] 해킹된 K사 재생 드론
   źródło: Enemies-a1c5p1.json :: dataList[id=97405].name
   limit: do 40 znaków
   EN: Hacked K Corp. Regen Drone
   PL: Hacked K Corp. Regen Drone
423. [[a1c5p1] Wróg / część [97405] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=97405].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [[a1c5p1] Wróg / część [97406] — nazwa] 되살아난 K사 검문소 요원
   źródło: Enemies-a1c5p1.json :: dataList[id=97406].name
   limit: do 40 znaków
   EN: Revived K Corp. Security
   PL: Revived K Corp. Security
425. [[a1c5p1] Wróg / część [97406] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=97406].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [[a1c5p1] Wróg / część [97407] — nazwa] 되살아난 K사 검문소 요원
   źródło: Enemies-a1c5p1.json :: dataList[id=97407].name
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [[a1c5p1] Wróg / część [97407] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=97407].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [[a1c5p1] Wróg / część [97408] — nazwa] 되살아난 K사 1등급 직원
   źródło: Enemies-a1c5p1.json :: dataList[id=97408].name
   limit: do 50 znaków
   EN: Revived K Corp. Class 1 Staff
   PL: Revived K Corp. Class 1 Staff
429. [[a1c5p1] Wróg / część [97408] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=97408].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [[a1c5p1] Wróg / część [97409] — nazwa] 되살아난 K사 1등급 직원
   źródło: Enemies-a1c5p1.json :: dataList[id=97409].name
   (powtórzenie elementu 428 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [[a1c5p1] Wróg / część [97409] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=97409].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [[a1c5p1] Wróg / część [97410] — nazwa] 되살아난 K사 3등급 직원 - 강화
   źródło: Enemies-a1c5p1.json :: dataList[id=97410].name
   limit: do 60 znaków
   EN: Revived K Corp. Class 3 Empowered Staff
   PL: Revived K Corp. Class 3 Empowered Staff
433. [[a1c5p1] Wróg / część [97410] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=97410].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [[a1c5p1] Wróg / część [8741] — nazwa] 누구도 울지 않도록
   źródło: Enemies-a1c5p1.json :: dataList[id=8741].name
   limit: do 40 znaków
   EN: So That No One Will Cry
   PL: So That No One Will Cry
435. [[a1c5p1] Wróg / część [8741] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=8741].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [[a1c5p1] Wróg / część [874101] — nazwa] 몸통
   źródło: Enemies-a1c5p1.json :: dataList[id=874101].name
   limit: do 40 znaków
   EN: Body
   PL: Korpus
437. [[a1c5p1] Wróg / część [874101] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874101].desc
   limit: do 120 znaków
   EN: Part
   PL: Część
438. [[a1c5p1] Wróg / część [874102] — nazwa] 오른팔
   źródło: Enemies-a1c5p1.json :: dataList[id=874102].name
   limit: do 40 znaków
   EN: Right Arm
   PL: Right Arm
439. [[a1c5p1] Wróg / część [874102] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874102].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [[a1c5p1] Wróg / część [8742] — nazwa] 떠돌이 여우
   źródło: Enemies-a1c5p1.json :: dataList[id=8742].name
   limit: do 40 znaków
   EN: Drifting Fox
   PL: Drifting Fox
441. [[a1c5p1] Wróg / część [8742] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=8742].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [[a1c5p1] Wróg / część [874201] — nazwa] 몸통
   źródło: Enemies-a1c5p1.json :: dataList[id=874201].name
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [[a1c5p1] Wróg / część [874201] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874201].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [[a1c5p1] Wróg / część [874202] — nazwa] 머리
   źródło: Enemies-a1c5p1.json :: dataList[id=874202].name
   limit: do 40 znaków
   EN: Head
   PL: Head
445. [[a1c5p1] Wróg / część [874202] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874202].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [[a1c5p1] Wróg / część [8743] — nazwa] 낡은 우산
   źródło: Enemies-a1c5p1.json :: dataList[id=8743].name
   limit: do 40 znaków
   EN: Old Umbrella
   PL: Old Umbrella
447. [[a1c5p1] Wróg / część [8743] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=8743].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [[a1c5p1] Wróg / część [874301] — nazwa] 우산
   źródło: Enemies-a1c5p1.json :: dataList[id=874301].name
   limit: do 40 znaków
   EN: Umbrella
   PL: Umbrella
449. [[a1c5p1] Wróg / część [874301] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874301].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [[a1c5p1] Wróg / część [8744] — nazwa] 신사 요정
   źródło: Enemies-a1c5p1.json :: dataList[id=8744].name
   limit: do 40 znaków
   EN: Fairy Gentleman
   PL: Fairy Gentleman
451. [[a1c5p1] Wróg / część [8744] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=8744].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [[a1c5p1] Wróg / część [874401] — nazwa] 몸통
   źródło: Enemies-a1c5p1.json :: dataList[id=874401].name
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [[a1c5p1] Wróg / część [874401] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874401].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [[a1c5p1] Wróg / część [874402] — nazwa] 왼팔
   źródło: Enemies-a1c5p1.json :: dataList[id=874402].name
   limit: do 40 znaków
   EN: Left Arm
   PL: Left Arm
455. [[a1c5p1] Wróg / część [874402] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874402].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [[a1c5p1] Wróg / część [8745] — nazwa] 요정주
   źródło: Enemies-a1c5p1.json :: dataList[id=8745].name
   limit: do 40 znaków
   EN: Fairy Wine
   PL: Fairy Wine
457. [[a1c5p1] Wróg / część [8745] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=8745].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [[a1c5p1] Wróg / część [874501] — nazwa] 술통
   źródło: Enemies-a1c5p1.json :: dataList[id=874501].name
   limit: do 40 znaków
   EN: Wine Barrel
   PL: Wine Barrel
459. [[a1c5p1] Wróg / część [874501] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874501].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [[a1c5p1] Wróg / część [8746] — nazwa] 키다리 요정
   źródło: Enemies-a1c5p1.json :: dataList[id=8746].name
   limit: do 40 znaków
   EN: Fairy-Long-Legs
   PL: Fairy-Long-Legs
461. [[a1c5p1] Wróg / część [8746] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=8746].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [[a1c5p1] Wróg / część [874601] — nazwa] 몸통
   źródło: Enemies-a1c5p1.json :: dataList[id=874601].name
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [[a1c5p1] Wróg / część [874601] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874601].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [[a1c5p1] Wróg / część [874602] — nazwa] 왼팔
   źródło: Enemies-a1c5p1.json :: dataList[id=874602].name
   (powtórzenie elementu 454 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [[a1c5p1] Wróg / część [874602] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874602].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [[a1c5p1] Wróg / część [874603] — nazwa] 머리
   źródło: Enemies-a1c5p1.json :: dataList[id=874603].name
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [[a1c5p1] Wróg / część [874603] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874603].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [[a1c5p1] Wróg / część [8747] — nazwa] 거대한 잎사귀
   źródło: Enemies-a1c5p1.json :: dataList[id=8747].name
   limit: do 40 znaków
   EN: Giant Leaf
   PL: Giant Leaf
469. [[a1c5p1] Wróg / część [8747] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=8747].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [[a1c5p1] Wróg / część [874701] — nazwa] 몸통
   źródło: Enemies-a1c5p1.json :: dataList[id=874701].name
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [[a1c5p1] Wróg / część [874701] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874701].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [[a1c5p1] Wróg / część [8748] — nazwa] 놋쇠 황소 - 눈물 흘리는
   źródło: Enemies-a1c5p1.json :: dataList[id=8748].name
   limit: do 40 znaków
   EN: Brazen Bull - Tearful
   PL: Brazen Bull - Tearful
473. [[a1c5p1] Wróg / część [8748] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=8748].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [[a1c5p1] Wróg / część [874801] — nazwa] 몸통
   źródło: Enemies-a1c5p1.json :: dataList[id=874801].name
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [[a1c5p1] Wróg / część [874801] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874801].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [[a1c5p1] Wróg / część [874802] — nazwa] 머리
   źródło: Enemies-a1c5p1.json :: dataList[id=874802].name
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [[a1c5p1] Wróg / część [874802] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874802].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [[a1c5p1] Wróg / część [8749] — nazwa] kqe-1j-23
   źródło: Enemies-a1c5p1.json :: dataList[id=8749].name
   limit: do 40 znaków
   EN: kqe-1j-23
   PL: kqe-1j-23
479. [[a1c5p1] Wróg / część [8749] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=8749].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [[a1c5p1] Wróg / część [874901] — nazwa] 몸통
   źródło: Enemies-a1c5p1.json :: dataList[id=874901].name
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [[a1c5p1] Wróg / część [874901] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=874901].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [[a1c5p1] Wróg / część [8750] — nazwa] 마을 주민의 심장
   źródło: Enemies-a1c5p1.json :: dataList[id=8750].name
   limit: do 40 znaków
   EN: Heart of the Townsfolk
   PL: Heart of the Townsfolk
483. [[a1c5p1] Wróg / część [8750] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=8750].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [[a1c5p1] Wróg / część [875001] — nazwa] 심장
   źródło: Enemies-a1c5p1.json :: dataList[id=875001].name
   limit: do 40 znaków
   EN: Heart
   PL: Heart
485. [[a1c5p1] Wróg / część [875001] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=875001].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [[a1c5p1] Wróg / część [8751] — nazwa] 울음 두꺼비
   źródło: Enemies-a1c5p1.json :: dataList[id=8751].name
   limit: do 40 znaków
   EN: Blubbering Toad
   PL: Blubbering Toad
487. [[a1c5p1] Wróg / część [8751] — opis] 본체
   źródło: Enemies-a1c5p1.json :: dataList[id=8751].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [[a1c5p1] Wróg / część [875101] — nazwa] 몸통
   źródło: Enemies-a1c5p1.json :: dataList[id=875101].name
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [[a1c5p1] Wróg / część [875101] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=875101].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [[a1c5p1] Wróg / część [875102] — nazwa] 왼쪽 눈
   źródło: Enemies-a1c5p1.json :: dataList[id=875102].name
   limit: do 40 znaków
   EN: Left Eye
   PL: Left Eye
491. [[a1c5p1] Wróg / część [875102] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=875102].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [[a1c5p1] Wróg / część [875103] — nazwa] 오른쪽 눈
   źródło: Enemies-a1c5p1.json :: dataList[id=875103].name
   limit: do 40 znaków
   EN: Right Eye
   PL: Right Eye
493. [[a1c5p1] Wróg / część [875103] — opis] 부위
   źródło: Enemies-a1c5p1.json :: dataList[id=875103].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c5p1] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c5p1
- grupa rozdziału/trybu: `a1c5p1` · plik: `Skills_Enemy-a1c5p1.json`

494. [Umiejętność wroga [9008301] (ulepszenie 1) — nazwa] 물거품 토하기
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008301].levelList[level=1].name
   limit: do 40 znaków
   EN: Vomit Froth
   PL: Vomit Froth
495. [Umiejętność wroga [9008301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 2 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Sinking
   PL: [OnSucceedAttackHead] nakłada 2 Zatonięcia
496. [Umiejętność wroga [9008301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 침잠 2 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Umiejętność wroga [9008302] (ulepszenie 1) — nazwa] 할퀴기
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008302].levelList[level=1].name
   limit: do 40 znaków
   EN: Claw
   PL: Claw
498. [Umiejętność wroga [9008302] (ulepszenie 1) — opis] 대상의 <sprite name="Sinking"><color=#e30000><u><link="Sinking">침잠</link></u></color>이 5 이상이면 피해량 +20%
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Sinking">, <color=#e30000>, <u>, <link="Sinking">, </link>, </u>, </color>
   EN: If target has 5+ <sprite name="Sinking"><color=#e30000><u><link="Sinking">Sinking</link></u></color>, deal +20% damage.
   PL: jeżeli cel ma 5+ <sprite name="Sinking"><color=#e30000><u><link="Sinking">Zatonięcie</link></u></color>, zadaje +20% obrażeń.
499. [Umiejętność wroga [9008302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 30%만큼 체력 회복
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal by 30% of damage dealt
   PL: [OnSucceedAttack] przywraca HP równe 30% zadanych obrażeń
500. [Umiejętność wroga [9008302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 30%만큼 체력 회복
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Umiejętność wroga [9008303] (ulepszenie 1) — nazwa] 살수
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008303].levelList[level=1].name
   limit: do 40 znaków
   EN: Water Jet
   PL: Water Jet
502. [Umiejętność wroga [9008303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 5 증가
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +5 Sinking Count
   PL: [OnSucceedAttack] nakłada 5 Licznika Zatonięcia
503. [Umiejętność wroga [9008304] (ulepszenie 1) — nazwa] 미끌거리는 피부
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008304].levelList[level=1].name
   limit: do 40 znaków
   EN: Mucous Skin
   PL: Mucous Skin
504. [Umiejętność wroga [9008304] (ulepszenie 1) — opis] 보호막이 있는동안 피격 시 대상에게 침잠 1 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008304].levelList[level=1].desc
   limit: do 120 znaków
   EN: If attacked while Shielded, inflict 1 Sinking on the attacker
   PL: przy trafieniu, gdy ta jednostka ma Tarczę, nakłada 1 Zatonięcia na atakującego
505. [Umiejętność wroga [9008401] (ulepszenie 1) — nazwa] 갈고리 베기
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008401].levelList[level=1].name
   limit: do 40 znaków
   EN: Hook Slice
   PL: Hook Slice
506. [Umiejętność wroga [9008401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 3 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Bleed
   PL: [OnSucceedAttackHead] nakłada 3 Krwawienia
507. [Umiejętność wroga [9008402] (ulepszenie 1) — nazwa] 연속 갈고리 베기
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008402].levelList[level=1].name
   limit: do 40 znaków
   EN: Consecutive Hook Slice
   PL: Consecutive Hook Slice
508. [Umiejętność wroga [9008402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 2 증가
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Bleed Count
   PL: [OnSucceedAttack] nakłada 2 Licznika Krwawienia
509. [Umiejętność wroga [9008402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 5 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Bleed
   PL: [OnSucceedAttack] nakłada 5 Krwawień
510. [Umiejętność wroga [9008403] (ulepszenie 1) — nazwa] 전투의 함성
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008403].levelList[level=1].name
   limit: do 40 znaków
   EN: Battle Cry
   PL: Battle Cry
511. [Umiejętność wroga [9008403] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 호흡 2 얻음.\n턴 종료시 보호막만큼 체력을 회복함.
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008403].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Poise next turn.\nTurn End: Heal HP equal to the Shield HP.
   PL: [WhenUse] zyskuje 2 Oddechu w następnej turze.\nKoniec tury: przywraca HP równe HP Tarczy.
512. [Umiejętność wroga [9008404] (ulepszenie 1) — nazwa] 빈틈 후리기
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008404].levelList[level=1].name
   limit: do 40 znaków
   EN: Tear the Gap
   PL: Tear the Gap
513. [Umiejętność wroga [9008404] (ulepszenie 1) — opis] <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</link></u></color>이 있을 때 코인 효과가 발동한다.
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </link>, </u>, </color>
   EN: Coin effects activate when this unit has <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</link></u></color>.
   PL: efekty Monety uruchamiają się, gdy ta jednostka ma <sprite name="Breath"><color=#f8c200><u><link="Breath">Oddech</link></u></color>.
514. [Umiejętność wroga [9008404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 가하는 피해량 +30%
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Deal +30% damage
   PL: [OnSucceedAttackTail] zadaje +30% obrażeń
515. [Umiejętność wroga [9008404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackTail] 가하는 피해량 +30%
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Umiejętność wroga [9008501] (ulepszenie 1) — nazwa] 갈고리 걸기
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008501].levelList[level=1].name
   limit: do 40 znaków
   EN: Hook Snag
   PL: Hook Snag
517. [Umiejętność wroga [9008501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 2 증가
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +2 Bleed Count
   PL: [OnSucceedAttackHead] nakłada 2 Licznika Krwawienia
518. [Umiejętność wroga [9008502] (ulepszenie 1) — nazwa] 갈고리 훅
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008502].levelList[level=1].name
   limit: do 40 znaków
   EN: Hook Punch
   PL: Hook Punch
519. [Umiejętność wroga [9008502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL: [OnSucceedAttack] nakłada 2 Krwawienia
520. [Umiejętność wroga [9008502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Bleed Count
   PL: [OnSucceedAttack] nakłada 3 Licznika Krwawienia
521. [Umiejętność wroga [9008503] (ulepszenie 1) — nazwa] 전투의 함성
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008503].levelList[level=1].name
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Umiejętność wroga [9008503] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 호흡 2 얻음.\n턴 종료시 보호막만큼 체력을 회복함.
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008503].levelList[level=1].desc
   (powtórzenie elementu 511 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Umiejętność wroga [9008504] (ulepszenie 1) — nazwa] 빈틈 후리기
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008504].levelList[level=1].name
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Umiejętność wroga [9008504] (ulepszenie 1) — opis] <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</link></u></color>이 있을 때 코인 효과가 발동한다.
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008504].levelList[level=1].desc
   (powtórzenie elementu 513 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Umiejętność wroga [9008504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 가하는 피해량 +30%
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Umiejętność wroga [9008504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackTail] 가하는 피해량 +30%
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Umiejętność wroga [9008601] (ulepszenie 1) — nazwa] 피부 찢기
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008601].levelList[level=1].name
   limit: do 40 znaków
   EN: Tear the Flesh
   PL: Tear the Flesh
528. [Umiejętność wroga [9008601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 2 증가
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Umiejętność wroga [9008601] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 출혈 3 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008601].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 506 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Umiejętność wroga [9008602] (ulepszenie 1) — nazwa] 침투한다
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008602].levelList[level=1].name
   limit: do 40 znaków
   EN: Going In
   PL: Going In
531. [Umiejętność wroga [9008602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 4 부여, 출혈 횟수 3 증가
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Bleed and +3 Bleed Count
   PL: [OnSucceedAttack] nakłada 4 Krwawienia i 3 Licznika Krwawienia
532. [Umiejętność wroga [9008603] (ulepszenie 1) — nazwa] 더 빠르게
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008603].levelList[level=1].name
   limit: do 40 znaków
   EN: Faster
   PL: Faster
533. [Umiejętność wroga [9008603] (ulepszenie 1) — opis] [EndSkill] 다음 턴에 피해량 증가 1 얻음
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] Gain 1 Damage Up next turn
   PL: [EndSkill] zyskuje 1 Wzrost Obrażeń w następnej turze
534. [Umiejętność wroga [9008603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 4 얻음
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 4 Poise next turn
   PL: [OnSucceedAttack] zyskuje 4 Oddechu w następnej turze
535. [Umiejętność wroga [9008603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 2 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Fragile next turn
   PL: [OnSucceedAttack] nakłada 2 Kruchości w następnej turze
536. [Umiejętność wroga [9008604] (ulepszenie 1) — nazwa] 전투의 함성
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008604].levelList[level=1].name
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Umiejętność wroga [9008604] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 호흡 2 얻음.\n턴 종료시 보호막만큼 체력을 회복함.
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008604].levelList[level=1].desc
   (powtórzenie elementu 511 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Umiejętność wroga [9008605] (ulepszenie 1) — nazwa] 노획
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008605].levelList[level=1].name
   limit: do 40 znaków
   EN: Looting
   PL: Looting
539. [Umiejętność wroga [9008605] (ulepszenie 1) — opis] [WinDuel] 대상의 1~3등급 스킬의 코인 위력, 갯수를 가져와 사용함
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008605].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Copies the target's 1~3 Skill Coin Power and Coin Count and uses them as its own
   PL: [WinDuel] przejmuje Moc Monet i Liczniki Monet Umiejętności celu o rangach 1–3 i używa ich jako własnych
540. [Umiejętność wroga [9008701] (ulepszenie 1) — nazwa] 더 때려봐
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008701].levelList[level=1].name
   limit: do 40 znaków
   EN: Hit Me Harder
   PL: Hit Me Harder
541. [Umiejętność wroga [9008701] (ulepszenie 1) — opis] [WhenUse] 대상에게 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>이 있다면, 보호 1 얻음
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target has <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u>, gain 1 Protection
   PL: [WhenUse] jeżeli cel ma <sprite name="Laceration"><color=#e30000><u><link="Laceration">Krwawienie</link></u></color>, zyskuje 1 Ochrony
542. [Umiejętność wroga [9008701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind next turn
   PL: [OnSucceedAttack] nakłada 2 Wiązania w następnej turze
543. [Umiejętność wroga [9008701] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008701].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Umiejętność wroga [9008702] (ulepszenie 1) — nazwa] 여기를 때리는거다
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008702].levelList[level=1].name
   limit: do 40 znaków
   EN: Hit Me Right here
   PL: Hit Me Right here
545. [Umiejętność wroga [9008702] (ulepszenie 1) — opis] [WhenUse] 대상에게 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>이 있다면, 보호 1 얻음
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008702].levelList[level=1].desc
   (powtórzenie elementu 541 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Umiejętność wroga [9008702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Paralyze next turn
   PL: [OnSucceedAttack] nakłada 1 Paraliżu w następnej turze
547. [Umiejętność wroga [9008702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Umiejętność wroga [9008702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 피해량 감소 2 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Damage Down next turn
   PL: [OnSucceedAttack] nakłada 2 Spadek Obrażeń w następnej turze
549. [Umiejętność wroga [9008702] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Umiejętność wroga [9008703] (ulepszenie 1) — nazwa] 더욱 단단하게
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008703].levelList[level=1].name
   limit: do 40 znaków
   EN: Even Harder
   PL: Even Harder
551. [Umiejętność wroga [9008703] (ulepszenie 1) — opis] [EndSkill] 다음 턴에 피해량 증가 1 얻음
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008703].levelList[level=1].desc
   (powtórzenie elementu 533 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Umiejętność wroga [9008703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 보호 2 얻음
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 Protection
   PL: [OnSucceedAttack] zyskuje 2 Ochrony
553. [Umiejętność wroga [9008703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 보호 2 얻음
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 Protection next turn
   PL: [OnSucceedAttack] zyskuje 2 Ochrony w następnej turze
554. [Umiejętność wroga [9008703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 호흡 4 얻음
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 534 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Umiejętność wroga [9008704] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008704].levelList[level=1].name
   limit: do 40 znaków
   EN: Defend
   PL: Defend
556. [Umiejętność wroga [9008704] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 호흡 2 얻음.\n턴 종료시 보호막만큼 체력을 회복함.
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008704].levelList[level=1].desc
   (powtórzenie elementu 511 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Umiejętność wroga [9008705] (ulepszenie 1) — nazwa] 노획
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008705].levelList[level=1].name
   (powtórzenie elementu 538 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Umiejętność wroga [9008705] (ulepszenie 1) — opis] [WinDuel] 대상의 1~3등급 스킬의 코인 위력, 갯수를 가져와 사용함
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9008705].levelList[level=1].desc
   (powtórzenie elementu 539 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Umiejętność wroga [9101101] (ulepszenie 1) — nazwa] 살수
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101101].levelList[level=1].name
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Umiejętność wroga [9101101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Sinking
   PL: [OnSucceedAttack] nakłada 3 Zatonięcia
561. [Umiejętność wroga [9101101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Umiejętność wroga [9101102] (ulepszenie 1) — nazwa] 축축한 일격
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101102].levelList[level=1].name
   limit: do 40 znaków
   EN: Damp Strike
   PL: Damp Strike
563. [Umiejętność wroga [9101102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 취약 2 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Sinking Fragility
   PL: [OnSucceedAttack] nakłada 2 Kruchości Zatonięcia
564. [Umiejętność wroga [9101102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 520 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Umiejętność wroga [9101102] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 50%만큼 체력 회복
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101102].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal by 50% of damage dealt
   PL: [OnSucceedAttack] przywraca HP równe 50% zadanych obrażeń
566. [Umiejętność wroga [9101103] (ulepszenie 1) — nazwa] 파도의 손아귀
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101103].levelList[level=1].name
   limit: do 40 znaków
   EN: Clutch of the Waves
   PL: Clutch of the Waves
567. [Umiejętność wroga [9101103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 2 증가
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Sinking Count
   PL: [OnSucceedAttack] nakłada 2 Licznika Zatonięcia
568. [Umiejętność wroga [9101103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed
   PL: [OnSucceedAttackHead] nakłada 2 Krwawienia
569. [Umiejętność wroga [9101103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 2 증가
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Umiejętność wroga [9101103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 568 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Umiejętność wroga [9101104] (ulepszenie 1) — nazwa] 울부짖는 물결
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101104].levelList[level=1].name
   limit: do 40 znaków
   EN: Shrieking Waves
   PL: Shrieking Waves
572. [Umiejętność wroga [9101104] (ulepszenie 1) — opis] 대상의 침잠 위력 5당 피해량 +20%\n대상의 정신력이 0 미만이면 피해량 +10%
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Damage +20% per 5 Sinking Potency on target\nIf target's SP is below 0, deal +10% damage
   PL: zadaje +20% obrażeń za każde 5 Siły Zatonięcia celu\njeżeli SP celu jest poniżej 0, zadaje +10% obrażeń
573. [Umiejętność wroga [9101104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠쇄도
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Sinking Deluge
   PL: [OnSucceedAttack] Zatonięcie: Powódź
574. [Umiejętność wroga [9101105] (ulepszenie 1) — nazwa] 미끌거리는 피부
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101105].levelList[level=1].name
   (powtórzenie elementu 503 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Umiejętność wroga [9101105] (ulepszenie 1) — opis] 보호막이 있는동안 피격 시 대상에게 침잠 1 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101105].levelList[level=1].desc
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Umiejętność wroga [9101201] (ulepszenie 1) — nazwa] 저기 저기봐
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101201].levelList[level=1].name
   limit: do 40 znaków
   EN: There, There They Are
   PL: There, There They Are
577. [Umiejętność wroga [9101201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL: [OnSucceedAttack] nakłada 3 Krwawień
578. [Umiejętność wroga [9101202] (ulepszenie 1) — nazwa] 얘들아 손님이다
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101202].levelList[level=1].name
   limit: do 40 znaków
   EN: We've Got Company, Boys
   PL: We've Got Company, Boys
579. [Umiejętność wroga [9101202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 2 증가
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Umiejętność wroga [9101202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 568 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność wroga [9101202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Bleed Count
   PL: [OnSucceedAttack] nakłada 1 Licznika Krwawienia
582. [Umiejętność wroga [9101202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead]  출혈 4 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 4 Bleed
   PL: [OnSucceedAttackHead] nakłada 4 Krwawień
583. [Umiejętność wroga [9101203] (ulepszenie 1) — nazwa] 전투 지휘
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101203].levelList[level=1].name
   limit: do 40 znaków
   EN: Battle Command
   PL: Battle Command
584. [Umiejętność wroga [9101203] (ulepszenie 1) — opis] [WhenUse] 이번 턴에 호흡 5 얻음
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101203].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 5 Poise this turn
   PL: [WhenUse] zyskuje 5 Oddechu w tej turze
585. [Umiejętność wroga [9101203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신을 제외한 모든 아군에게 다음 턴에 보호 2, 공격 위력 증가 1 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Apply 2 Protection, 1 Attack Power Up to all other allies next turn
   PL: [OnSucceedAttack] nakłada 2 Ochrony i 1 Wzrost Mocy Ataku wszystkim pozostałym sojusznikom w następnej turze
586. [Umiejętność wroga [9101204] (ulepszenie 1) — nazwa] 헛점 발견! 격발!
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101204].levelList[level=1].name
   limit: do 40 znaków
   EN: Weakness Spotted! Fire!
   PL: Weakness Spotted! Fire!
587. [Umiejętność wroga [9101204] (ulepszenie 1) — opis] 대상의 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>이 5이상일 때, 합 위력 +2
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>
   EN: If target has 5+ <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u>, Clash Power +2
   PL: jeżeli cel ma 5+ <sprite name="Laceration"><color=#e30000><u><link="Laceration">Krwawienie</link></u></color>, Moc Starcia +2
588. [Umiejętność wroga [9101204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 4 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Bleed
   PL: [OnSucceedAttack] nakłada 4 Krwawień
589. [Umiejętność wroga [9101204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 출혈 4 부여
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 4 Bleed
   PL: [OnSucceedAttackHead] nakłada 4 Krwawień
590. [Umiejętność wroga [9101204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 3 부여\n대상의 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>만큼 추가 피해
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>, \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed Count\nDeal bonus damage equal to <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u> on target
   PL: [OnSucceedAttack] nakłada 3 Licznika Krwawienia\nzadaje dodatkowe obrażenia równe <sprite name="Laceration"><color=#e30000><u><link="Laceration">Krwawieniu</link></u></color> celu
591. [Umiejętność wroga [9101204] (ulepszenie 1) — moneta 2, efekt 2 — opis] 탄환 1 소모
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101204].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   EN: Spend 1 Ammo
   PL: zużywa 1 Amunicji
592. [Umiejętność wroga [9101205] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101205].levelList[level=1].name
   limit: do 40 znaków
   EN: Evade
   PL: Evade
593. [Umiejętność wroga [9101205] (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 호흡 5 얻음.\n[OnSucceedEvade]다음 턴에 모든 아군에게 호흡 2 부여.
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101205].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Gain 5 Poise next turn.\n[OnSucceedEvade] Apply 2 Poise to all allies next turn.
   PL: [OnSucceedEvade] zyskuje 5 Oddechu w następnej turze.\n[OnSucceedEvade] nakłada 2 Oddechu wszystkim sojusznikom w następnej turze.
594. [Umiejętność wroga [9101206] (ulepszenie 1) — nazwa] 노획
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101206].levelList[level=1].name
   (powtórzenie elementu 538 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Umiejętność wroga [9101206] (ulepszenie 1) — opis] [WinDuel] 대상의 3등급 스킬의 코인 위력, 갯수를 가져와 사용함
   źródło: Skills_Enemy-a1c5p1.json :: dataList[id=9101206].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Copies the target's Skill 3 Coin Power and Coin Count and uses them as its own
   PL: [WinDuel] przejmuje Moc Monet i Liczniki Monet Umiejętności 3 celu i używa ich jako własnych

## [a1c5p1] Pasywka wroga: Passives_Enemy-a1c5p1
- plik gry: `Passives_Enemy-a1c5p1.json`

596. [[a1c5p1] Pasywka wroga [9008301] — nazwa] 고래와의 연결
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008301].name
   limit: do 40 znaków
   EN: Cetacean Strand
   PL: Cetacean Strand
597. [[a1c5p1] Pasywka wroga [9008301] — opis] 이 캐릭터가 사망하면 구멍 손바닥 고래에게 피해를 준다.
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008301].desc
   limit: do 120 znaków
   EN: Whale of the Porous Hand takes damage when this unit is defeated.
   PL: gdy ta jednostka zostaje pokonana, zadaje obrażenia Whale of the Porous Hand
598. [[a1c5p1] Pasywka wroga [9008302] — nazwa] 연결된 아픔
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008302].name
   limit: do 40 znaków
   EN: Connected Pain
   PL: Connected Pain
599. [[a1c5p1] Pasywka wroga [9008302] — opis] 사망한다면, 연결된 인어들에게 체력 10의 피해를 주고 다음 턴에 피해량 증가 2를 부여.\n연결된 인어들은 해당 피해로 체력이 1이하로 떨어지지 않음.
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008302].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upon death, deal 10 damage to connected Mermaids. Then, apply 2 Damage Up next turn.\nThis effect cannot drop the connected Mermaids' HP below 1.
   PL: po śmierci zadaje połączonym Syrenom 10 obrażeń i nakłada im 2 Wzrost Obrażeń w następnej turze.\npowiązane Syreny nie mogą stracić przez te obrażenia więcej HP niż do 1.
600. [[a1c5p1] Pasywka wroga [9008401] — nazwa] 여유로운 호흡
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008401].name
   limit: do 40 znaków
   EN: Easy Breathing
   PL: Easy Breathing
601. [[a1c5p1] Pasywka wroga [9008401] — opis] <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>이 있을 때, 합 승리 시 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>을 5 얻음.
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008401].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>
   EN: If this unit has <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u>, gain 5 <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u> upon Clash Win.
   PL: gdy ta jednostka ma <sprite name="Breath"><color=#f8c200><u><link="Breath">Oddech</link></u></color>, przy wygranej Starciu zyskuje 5 <sprite name="Breath"><color=#f8c200><u><link="Breath">Oddechu</link></u></color>.
602. [[a1c5p1] Pasywka wroga [9008402] — nazwa] 동전의 양면
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008402].name
   limit: do 40 znaków
   EN: Two Sides Of a Coin
   PL: Two Sides Of a Coin
603. [[a1c5p1] Pasywka wroga [9008402] — opis] 매 턴마다 첫번째 코인 적중시 앞면이면 다음 턴에 피해량 증가 1을 얻음.\n첫번째 코인 적중시 뒷면이면 다음 턴에 피해량 감소 1을 얻음
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008402].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Every turn, if the first Coin 'Heads Hits', gain 1 Damage Up next turn.\nIf the first Coin 'Tails Hits', gain 1 Damage Down next turn.
   PL: w każdej turze, gdy pierwsza Moneta trafia Awersem, zyskuje 1 Wzrost Obrażeń w następnej turze.\ngdy pierwsza Moneta trafia Rewersem, zyskuje 1 Spadek Obrażeń w następnej turze
604. [[a1c5p1] Pasywka wroga [9008601] — nazwa] 거기 따끔하지 않아?
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008601].name
   limit: do 40 znaków
   EN: Ain't That a Prick?
   PL: Ain't That a Prick?
605. [[a1c5p1] Pasywka wroga [9008601] — opis] 적중시 대상에게 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>이 있다면, 대상의 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>만큼 정신력 회복
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>
   EN: On Hit, if target has <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u>, regain SP equal to <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u> on target
   PL: przy trafieniu, jeżeli cel ma <sprite name="Laceration"><color=#e30000><u><link="Laceration">Krwawienie</link></u></color>, przywraca SP równe <sprite name="Laceration"><color=#e30000><u><link="Laceration">Krwawieniu</link></u></color> celu
606. [[a1c5p1] Pasywka wroga [9008701] — nazwa] 최전선으로!!
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008701].name
   limit: do 40 znaków
   EN: To the Front Lines!!
   PL: To the Front Lines!!
607. [[a1c5p1] Pasywka wroga [9008701] — opis] 속도가 1일 때, <sprite name="Protection"><color=#f8c200><u><link="Protection">보호</color></link></u>를 얻으면 1 추가로 얻음.
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Protection">, <color=#f8c200>, <u>, <link="Protection">, </color>, </link>, </u>
   EN: When gaining Protection, gain 1 additional <sprite name="Protection"><color=#f8c200><u><link="Protection">Protection</color></link></u> if this unit's Speed is at 1
   PL: zyskując <sprite name="Protection"><color=#f8c200><u><link="Protection">Ochronę</link></u></color>, przy Szybkości 1 zyskuje dodatkowo 1 <sprite name="Protection"><color=#f8c200><u><link="Protection">Ochrony</link></u></color>.
608. [[a1c5p1] Pasywka wroga [9008702] — nazwa] 거기 따끔하지 않아?
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008702].name
   (powtórzenie elementu 604 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [[a1c5p1] Pasywka wroga [9008702] — opis] 적중시 대상에게 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>이 있다면, 대상의 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>만큼 정신력 회복
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9008702].desc
   (powtórzenie elementu 605 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [[a1c5p1] Pasywka wroga [9101201] — nazwa] 동전의 양면
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9101201].name
   (powtórzenie elementu 602 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [[a1c5p1] Pasywka wroga [9101201] — opis] 매 턴마다 첫번째 코인이 앞면이면 다음 턴에 피해량 증가 2, 공격 위력 증가 1을 얻음.\n첫번째 코인이 뒷면이면 다음 턴에 피해량 감소 2, 공격 위력 감소 1을 얻음
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9101201].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Every turn, if the first Coin 'Heads Hits', gain 2 Damage Up and 1 Attack Power Up next turn.\nIf the first Coin 'Tails Hits', gain 2 Damage Down and 1 Attack Power Down next turn.
   PL: w każdej turze, gdy pierwsza Moneta trafia Awersem, zyskuje 2 Wzrost Obrażeń i 1 Wzrost Mocy Ataku w następnej turze.\ngdy pierwsza Moneta trafia Rewersem, zyskuje 2 Spadek Obrażeń i 1 Spadek Mocy Ataku w następnej turze
612. [[a1c5p1] Pasywka wroga [9101202] — nazwa] 잠깐… 다가오지마!
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9101202].name
   limit: do 40 znaków
   EN: No... Get Away From Me!
   PL: No... Get Away From Me!
613. [[a1c5p1] Pasywka wroga [9101202] — opis] 합 패배시, 호흡 4, 호흡 횟수 3 증가.
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9101202].desc
   limit: do 120 znaków
   EN: Upon Clash Lose, gain 4 Poise and 3 Poise Count.
   PL: po przegranej w Starciu zyskuje 4 Oddechu i 3 Licznika Oddechu.
614. [[a1c5p1] Pasywka wroga [9101203] — nazwa] 환호하라!
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9101203].name
   limit: do 40 znaków
   EN: Huzzah, Men!
   PL: Huzzah, Men!
615. [[a1c5p1] Pasywka wroga [9101203] — opis] 크리티컬 적중시 다음 턴에 더하기 코인 강화 1를 얻음.\n자신의 정신력 15 회복.\n자신을 제외한 모든 아군의 정신력 10 회복\n(매 턴마다 한 번 발동)
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9101203].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Critical Hit, gain 1 Plus Coin Boost next turn.\nHeal 15 SP on self.\nAll other allies heal 10 SP.\n(Activates once per turn)
   PL: przy trafieniu krytycznym zyskuje 1 Wzmocnienia Monet Plus w następnej turze.\nprzywraca 15 SP sobie.\npozostali sojusznicy przywracają 10 SP\n(1 raz na turę)
616. [[a1c5p1] Pasywka wroga [9101204] — nazwa] 뭣들 하는 거야?
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9101204].name
   limit: do 40 znaków
   EN: What Are You Doing?!
   PL: What Are You Doing?!
617. [[a1c5p1] Pasywka wroga [9101204] — opis] 전투에서 붙잡혔을 때, 모든 아군의 정신력 -30
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9101204].desc
   limit: do 120 znaków
   EN: Being captured in this encounter causes all allies to lose 30 SP
   PL: pojmanie w tej walce powoduje utratę 30 SP przez wszystkich sojuszników
618. [[a1c5p1] Pasywka wroga [9101205] — nazwa] 거기 따끔하지 않아?
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9101205].name
   (powtórzenie elementu 604 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [[a1c5p1] Pasywka wroga [9101205] — opis] 적중시 대상에게 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>이 있다면, 대상의 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>만큼 정신력 회복
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9101205].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>
   EN: If target has <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u> On Hit, regain SP equal to <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u> on target
   PL: przy trafieniu, jeżeli cel ma <sprite name="Laceration"><color=#e30000><u><link="Laceration">Krwawienie</link></u></color>, przywraca SP równe <sprite name="Laceration"><color=#e30000><u><link="Laceration">Krwawieniu</link></u></color> celu
620. [[a1c5p1] Pasywka wroga [9101101] — nazwa] 고래와의 연결
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9101101].name
   (powtórzenie elementu 596 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [[a1c5p1] Pasywka wroga [9101101] — opis] 이 캐릭터가 사망하면 구멍 손바닥 고래에게 피해를 준다.
   źródło: Passives_Enemy-a1c5p1.json :: dataList[id=9101101].desc
   (powtórzenie elementu 597 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c5p2] Wróg / część: Enemies-a1c5p2
- plik gry: `Enemies-a1c5p2.json`

622. [[a1c5p2] Wróg / część [90088] — nazwa] 천가닥 줄기 고래 인어
   źródło: Enemies-a1c5p2.json :: dataList[id=90088].name
   limit: do 60 znaków
   EN: Whale of the Thousand Strands Mermaid
   PL: Whale of the Thousand Strands Mermaid
623. [[a1c5p2] Wróg / część [90088] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=90088].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [[a1c5p2] Wróg / część [90089] — nazwa] 창백한 흰색 인어
   źródło: Enemies-a1c5p2.json :: dataList[id=90089].name
   limit: do 40 znaków
   EN: Pallid White Mermaid
   PL: Pallid White Mermaid
625. [[a1c5p2] Wróg / część [90089] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=90089].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [[a1c5p2] Wróg / część [90090] — nazwa] 창백한 푸른 인어
   źródło: Enemies-a1c5p2.json :: dataList[id=90090].name
   limit: do 40 znaków
   EN: Pallid Blue Mermaid
   PL: Pallid Blue Mermaid
627. [[a1c5p2] Wróg / część [90090] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=90090].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [[a1c5p2] Wróg / część [90091] — nazwa] 창백한 얽힌 인어
   źródło: Enemies-a1c5p2.json :: dataList[id=90091].name
   limit: do 40 znaków
   EN: Pallid Entwined Mermaid
   PL: Pallid Entwined Mermaid
629. [[a1c5p2] Wróg / część [90091] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=90091].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [[a1c5p2] Wróg / część [90092] — nazwa] 창백해진 것-방패
   źródło: Enemies-a1c5p2.json :: dataList[id=90092].name
   limit: do 40 znaków
   EN: Pallidified Thing-Shield
   PL: Pallidified Thing-Shield
631. [[a1c5p2] Wróg / część [90092] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=90092].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [[a1c5p2] Wróg / część [90093] — nazwa] 창백해진 것-곤봉
   źródło: Enemies-a1c5p2.json :: dataList[id=90093].name
   limit: do 40 znaków
   EN: Pallidified Thing-Club
   PL: Pallidified Thing-Club
633. [[a1c5p2] Wróg / część [90093] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=90093].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [[a1c5p2] Wróg / część [90094] — nazwa] 창백해진 것-해적
   źródło: Enemies-a1c5p2.json :: dataList[id=90094].name
   limit: do 40 znaków
   EN: Pallidified Thing-Pirate
   PL: Pallidified Thing-Pirate
635. [[a1c5p2] Wróg / część [90094] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=90094].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [[a1c5p2] Wróg / część [90095] — nazwa] 창백해진 것-갈고리
   źródło: Enemies-a1c5p2.json :: dataList[id=90095].name
   limit: do 40 znaków
   EN: Pallidified Thing-Hook
   PL: Pallidified Thing-Hook
637. [[a1c5p2] Wróg / część [90095] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=90095].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [[a1c5p2] Wróg / część [90096] — nazwa] 든든한 중지 작은 아우
   źródło: Enemies-a1c5p2.json :: dataList[id=90096].name
   limit: do 50 znaków
   EN: Sturdy Little Brother of the Middle
   PL: Sturdy Little Brother of the Middle
639. [[a1c5p2] Wróg / część [90096] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=90096].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [[a1c5p2] Wróg / część [90097] — nazwa] 엄격한 중지 작은 아우
   źródło: Enemies-a1c5p2.json :: dataList[id=90097].name
   limit: do 50 znaków
   EN: Stern Little Brother of the Middle
   PL: Stern Little Brother of the Middle
641. [[a1c5p2] Wróg / część [90097] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=90097].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [[a1c5p2] Wróg / część [8097] — nazwa] 든든한 중지 작은 아우
   źródło: Enemies-a1c5p2.json :: dataList[id=8097].name
   (powtórzenie elementu 638 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [[a1c5p2] Wróg / część [8097] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=8097].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [[a1c5p2] Wróg / część [809701] — nazwa] 몸통
   źródło: Enemies-a1c5p2.json :: dataList[id=809701].name
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [[a1c5p2] Wróg / część [809701] — opis] 부위
   źródło: Enemies-a1c5p2.json :: dataList[id=809701].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [[a1c5p2] Wróg / część [8098] — nazwa] 엄격한 중지 작은 아우
   źródło: Enemies-a1c5p2.json :: dataList[id=8098].name
   (powtórzenie elementu 640 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [[a1c5p2] Wróg / część [8098] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=8098].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [[a1c5p2] Wróg / część [809801] — nazwa] 몸통
   źródło: Enemies-a1c5p2.json :: dataList[id=809801].name
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [[a1c5p2] Wróg / część [809801] — opis] 부위
   źródło: Enemies-a1c5p2.json :: dataList[id=809801].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [[a1c5p2] Wróg / część [8099] — nazwa] 리카르도
   źródło: Enemies-a1c5p2.json :: dataList[id=8099].name
   limit: do 40 znaków
   EN: Ricardo
   PL: Ricardo
651. [[a1c5p2] Wróg / część [8099] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=8099].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [[a1c5p2] Wróg / część [809901] — nazwa] 몸통
   źródło: Enemies-a1c5p2.json :: dataList[id=809901].name
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [[a1c5p2] Wróg / część [809901] — opis] 부위
   źródło: Enemies-a1c5p2.json :: dataList[id=809901].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [[a1c5p2] Wróg / część [90100] — nazwa] 창백하고도 푸른 인어
   źródło: Enemies-a1c5p2.json :: dataList[id=90100].name
   limit: do 40 znaków
   EN: Pallid and Blue Mermaid
   PL: Pallid and Blue Mermaid
655. [[a1c5p2] Wróg / część [90100] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=90100].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [[a1c5p2] Wróg / część [97501] — nazwa] 창백해진 것-곤봉
   źródło: Enemies-a1c5p2.json :: dataList[id=97501].name
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [[a1c5p2] Wróg / część [97501] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=97501].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [[a1c5p2] Wróg / część [97502] — nazwa] 창백해진 것-방패
   źródło: Enemies-a1c5p2.json :: dataList[id=97502].name
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [[a1c5p2] Wróg / część [97502] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=97502].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [[a1c5p2] Wróg / część [97503] — nazwa] 창백해진 것-갈고리
   źródło: Enemies-a1c5p2.json :: dataList[id=97503].name
   (powtórzenie elementu 636 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [[a1c5p2] Wróg / część [97503] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=97503].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [[a1c5p2] Wróg / część [97504] — nazwa] 창백해진 것-해적
   źródło: Enemies-a1c5p2.json :: dataList[id=97504].name
   (powtórzenie elementu 634 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [[a1c5p2] Wróg / część [97504] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=97504].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [[a1c5p2] Wróg / część [97505] — nazwa] 창백한 흰색 인어
   źródło: Enemies-a1c5p2.json :: dataList[id=97505].name
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [[a1c5p2] Wróg / część [97505] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=97505].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [[a1c5p2] Wróg / część [97506] — nazwa] 창백한 푸른 인어
   źródło: Enemies-a1c5p2.json :: dataList[id=97506].name
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [[a1c5p2] Wróg / część [97506] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=97506].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [[a1c5p2] Wróg / część [97507] — nazwa] 창백한 얽힌 인어
   źródło: Enemies-a1c5p2.json :: dataList[id=97507].name
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [[a1c5p2] Wróg / część [97507] — opis] 본체
   źródło: Enemies-a1c5p2.json :: dataList[id=97507].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c5p2] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c5p2
- grupa rozdziału/trybu: `a1c5p2` · plik: `Skills_Abnormality-a1c5p2.json`

670. [Umiejętność wroga [809901] (ulepszenie 1) — nazwa] 주먹질
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809901].levelList[level=1].name
   limit: do 40 znaków
   EN: Punching
   PL: Punching
671. [Umiejętność wroga [809901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 타격 추가 피해 3
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 3 Blunt bonus damage
   PL: [OnSucceedAttack] zadaje 3 dodatkowych obrażeń Uderzeniem
672. [Umiejętność wroga [809901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 타격 추가 피해 3
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 671 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Umiejętność wroga [809901] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809901].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze
   PL: [OnSucceedAttack] nakłada 3 Paraliżu
674. [Umiejętność wroga [809902] (ulepszenie 1) — nazwa] 발길질
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809902].levelList[level=1].name
   limit: do 40 znaków
   EN: Kicking
   PL: Kicking
675. [Umiejętność wroga [809902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 타격 추가 피해 5
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 Blunt bonus damage
   PL: [OnSucceedAttack] zadaje 5 dodatkowych obrażeń Uderzeniem
676. [Umiejętność wroga [809902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 타격 추가 피해 5
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Umiejętność wroga [809902] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 3 부여
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze next turn
   PL: [OnSucceedAttack] nakłada 3 Paraliżu w następnej turze
678. [Umiejętność wroga [809903] (ulepszenie 1) — nazwa] 되갚기
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809903].levelList[level=1].name
   limit: do 40 znaków
   EN: Payback
   PL: Payback
679. [Umiejętność wroga [809903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력 5 감소
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 5 SP
   PL: [OnSucceedAttack] cel traci 5 SP
680. [Umiejętność wroga [809904] (ulepszenie 1) — nazwa] 위압
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809904].levelList[level=1].name
   limit: do 40 znaków
   EN: Domineer
   PL: Domineer
681. [Umiejętność wroga [809904] (ulepszenie 1) — opis] [StartBattle] 모든 아군에게 공격 위력 증가 1 부여\n[StartBattle] 정신력이 가장 낮은 적 2명에게 공격 위력 감소 2 부여
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809904].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Apply 1 Attack Power Up to all allies\n[StartBattle] Inflict 2 Attack Power Down to 2 enemies with the least SP
   PL: [StartBattle] nakłada 1 Wzrost Mocy Ataku wszystkim sojusznikom\n[StartBattle] nakłada 2 Spadek Mocy Ataku 2 wrogom z najniższym SP
682. [Umiejętność wroga [809905] (ulepszenie 1) — nazwa] 내 몸에 새겨봐라
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809905].levelList[level=1].name
   limit: do 40 znaków
   EN: Make this Memorable
   PL: Make this Memorable
683. [Umiejętność wroga [809905] (ulepszenie 1) — opis] [StartBattle] [AaCePbBi] 2를 얻음. 다음 턴에 속박 5를 얻음.
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809905].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [AaCePbBi]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AaCePbBi] = 형님의 시험 / Test of the Big Brother
   EN: [StartBattle] Gain 2 [AaCePbBi]. Gain 5 Bind next turn.
   PL: [StartBattle] zyskuje 2 [AaCePbBi]. Zyskuje 5 Wiązania w następnej turze.
684. [Umiejętność wroga [809906] (ulepszenie 1) — nazwa] 뒤통수 조심!
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809906].levelList[level=1].name
   limit: do 40 znaków
   EN: Watch Your Back!
   PL: Watch Your Back!
685. [Umiejętność wroga [809906] (ulepszenie 1) — opis] 대상의 정신력이 0 미만인 경우, 코인 위력 +3
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809906].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target has less than 0 SP, Coin Power +3
   PL: jeżeli SP celu jest poniżej 0, Moc Monety +3
686. [Umiejętność wroga [809906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 정신력 10 회복
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 10 SP on self
   PL: [OnSucceedAttack] przywraca 10 SP sobie
687. [Umiejętność wroga [809906] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 2, 공격 위력 감소 2 부여
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809906].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind and 2 Attack Power Down next turn
   PL: [OnSucceedAttack] nakłada 2 Wiązania i 2 Spadek Mocy Ataku w następnej turze
688. [Umiejętność wroga [809906] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력 20 감소
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809906].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 20 SP
   PL: [OnSucceedAttack] cel traci 20 SP
689. [Umiejętność wroga [809907] (ulepszenie 1) — nazwa] 다들 집합
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809907].levelList[level=1].name
   limit: do 40 znaków
   EN: Assemble
   PL: Assemble
690. [Umiejętność wroga [809907] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 아군 2명 소환
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809907].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Summon 2 allies next turn
   PL: [StartBattle] przywołuje 2 sojuszników w następnej turze
691. [Umiejętność wroga [809908] (ulepszenie 1) — nazwa] 원한 곱씹기
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809908].levelList[level=1].name
   limit: do 40 znaków
   EN: Swear Vengeance
   PL: Swear Vengeance
692. [Umiejętność wroga [809908] (ulepszenie 1) — opis] [StartBattle] [AaCePbBi] 2를 얻음. 다음 턴에 속박 5, 피해량 증가 5를 얻음.
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809908].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [AaCePbBi]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AaCePbBi] = 형님의 시험 / Test of the Big Brother
   EN: [StartBattle] Gain 2 [AaCePbBi]. Gain 5 Bind and 5 Damage Up next turn.
   PL: [StartBattle] zyskuje 2 [AaCePbBi]. Zyskuje 5 Wiązania i 5 Wzrost Obrażeń w następnej turze.
693. [Umiejętność wroga [809909] (ulepszenie 1) — nazwa] 내 헤어쿠포오오오온!!!
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809909].levelList[level=1].name
   limit: do 40 znaków
   EN: MY HAIR COUPOOOOOOOOOOONS!!!
   PL: MY HAIR COUPOOOOOOOOOOONS!!!
694. [Umiejętność wroga [809909] (ulepszenie 1) — opis] 메인 공격 대상의 정신력이 0 미만인 경우, 최종 위력 +5
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809909].levelList[level=1].desc
   limit: do 120 znaków
   EN: If the main target has less than 0 SP, Final Power +5
   PL: jeżeli SP głównego celu jest poniżej 0, Moc Końcowa +5
695. [Umiejętność wroga [809909] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 손상 30
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809909].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 30
   PL: [OnSucceedAttack] podnosi Próg Oszołomienia o 30
696. [Umiejętność wroga [809909] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality-a1c5p2.json :: dataList[id=809909].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c5p2] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c5p2
- grupa rozdziału/trybu: `a1c5p2` · plik: `Skills_Enemy-a1c5p2.json`

697. [Umiejętność wroga [9008801] (ulepszenie 1) — nazwa] 두려움 심기
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008801].levelList[level=1].name
   limit: do 40 znaków
   EN: Sow Fear
   PL: Sow Fear
698. [Umiejętność wroga [9008801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 대상의 정신력 피해 2
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Deal 2 SP damage
   PL: [OnSucceedAttackTail] zadaje 2 obrażeń SP
699. [Umiejętność wroga [9008801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackTail] 대상의 정신력 피해 2
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 698 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Umiejętność wroga [9008802] (ulepszenie 1) — nazwa] 공포 새기기
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008802].levelList[level=1].name
   limit: do 40 znaków
   EN: Engrave Horror
   PL: Engrave Horror
701. [Umiejętność wroga [9008802] (ulepszenie 1) — opis] [WinDuel] 대상의 정신력 피해 5, 자신의 체력 10만큼 회복
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Deal 10 SP damage to target; this unit heals 10 HP
   PL: [WinDuel] zadaje 10 obrażeń SP celowi; ta jednostka przywraca 10 HP
702. [Umiejętność wroga [9008802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bind next turn
   PL: [OnSucceedAttack] nakłada 1 Wiązania w następnej turze
703. [Umiejętność wroga [9008803] (ulepszenie 1) — nazwa] 공포 수확
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008803].levelList[level=1].name
   limit: do 40 znaków
   EN: Reap Horror
   PL: Reap Horror
704. [Umiejętność wroga [9008803] (ulepszenie 1) — opis] 대상의 정신력이 20미만이면, 이 공격의 체력 회복량 20% 추가 회복
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008803].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target’s SP is below 20, heal 20% more HP from this attack
   PL: jeżeli SP celu jest poniżej 20, ten atak przywraca o 20% więcej HP
705. [Umiejętność wroga [9008803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 대상의 정신력 피해 3
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Deal 3 SP damage
   PL: [OnSucceedAttackTail] zadaje 3 obrażeń SP
706. [Umiejętność wroga [9008803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 30%만큼 체력 회복
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Umiejętność wroga [9008803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackTail] 대상의 정신력 피해 3
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 705 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [Umiejętność wroga [9008803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량의 30%만큼 체력 회복
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Umiejętność wroga [9008804] (ulepszenie 1) — nazwa] 정신 마비
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008804].levelList[level=1].name
   limit: do 40 znaków
   EN: Paralyze Mind
   PL: Paralyze Mind
710. [Umiejętność wroga [9008804] (ulepszenie 1) — opis] 대상의 정신력이 -15미만이면, 피해량 +50%
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008804].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target's SP is below -15, deal +50% damage
   PL: jeżeli SP celu jest poniżej -15, zadaje +50% obrażeń
711. [Umiejętność wroga [9008804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Paralyze next turn
   PL: [OnSucceedAttack] nakłada 2 Paraliżu w następnej turze
712. [Umiejętność wroga [9008804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 711 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Umiejętność wroga [9008901] (ulepszenie 1) — nazwa] -... - ..-
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008901].levelList[level=1].name
   limit: do 40 znaków
   EN: -... - ..-
   PL: -... - ..-
714. [Umiejętność wroga [9008901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Umiejętność wroga [9008901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Umiejętność wroga [9008902] (ulepszenie 1) — nazwa] -- ... -.-
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008902].levelList[level=1].name
   limit: do 40 znaków
   EN: -- ... -.-
   PL: -- ... -.-
717. [Umiejętność wroga [9008902] (ulepszenie 1) — opis] [WinDuel] 창백한 소음 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Inflict 1 Pallid Noise
   PL: [WinDuel] nakłada 1 Bladego Szumu
718. [Umiejętność wroga [9008902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Umiejętność wroga [9008902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 침잠 횟수 3 증가
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +3 Sinking Count
   PL: [OnSucceedAttackHead] nakłada 3 Licznika Zatonięcia
720. [Umiejętność wroga [9008903] (ulepszenie 1) — nazwa] ...- .
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008903].levelList[level=1].name
   limit: do 40 znaków
   EN: ...- .
   PL: ...- .
721. [Umiejętność wroga [9008903] (ulepszenie 1) — opis] 자신을 제외한 살아있는 백화 상태의 아군이 있다면, 아군당 최종 위력 +1
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008903].levelList[level=1].desc
   limit: do 120 znaków
   EN: Final Power +1 for each surviving Pallidified ally (not counting this unit)
   PL: Moc Końcowa +1 za każdego żyjącego Zbielałego sojusznika (nie licząc tej jednostki)
722. [Umiejętność wroga [9008903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 40%만큼 체력 회복
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal by 40% of damage dealt
   PL: [OnSucceedAttack] przywraca HP równe 40% zadanych obrażeń
723. [Umiejętność wroga [9008903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 가지고있는 버프 하나를 다음 턴에 자신이 얻음.\n(공격 위력 증가, 신속, 피해량 증가, <sprite name="Protection"><color=#f8c200><u><link="Protection">보호</link></u></color>에 한함)
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <sprite name="Protection">, <color=#f8c200>, <u>, <link="Protection">, </link>, </u>, </color>, \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Copy one of the buffs currently applied to the target. Gain the copied buff next turn.\n(Limited to: Attack Power Up, Haste, Damage Up, and <sprite name="Protection"><color=#f8c200><u><link="Protection">Protection</link></u></color>)
   PL: [OnSucceedAttack] kopiuje 1 z Efektów należących obecnie do celu; zyskuje skopiowany Efekt w następnej turze.\n(ograniczone do: Wzrost Mocy Ataku, Haste, Wzrost Obrażeń i <sprite name="Protection"><color=#f8c200><u><link="Protection">Ochrony</link></u></color>)
724. [Umiejętność wroga [9008903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 40%만큼 체력 회복
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9008903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Umiejętność wroga [9009001] (ulepszenie 1) — nazwa] ..-. .
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009001].levelList[level=1].name
   limit: do 40 znaków
   EN: ..-. .
   PL: ..-. .
726. [Umiejętność wroga [9009001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 2 증가
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Umiejętność wroga [9009001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 2 증가
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Umiejętność wroga [9009002] (ulepszenie 1) — nazwa] ..-. . --
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009002].levelList[level=1].name
   limit: do 40 znaków
   EN: ..-. . --
   PL: ..-. . --
729. [Umiejętność wroga [9009002] (ulepszenie 1) — opis] [WinDuel] 창백한 소음 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009002].levelList[level=1].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Umiejętność wroga [9009002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 2 증가
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność wroga [9009002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 침잠 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Umiejętność wroga [9009003] (ulepszenie 1) — nazwa] .-.. -
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009003].levelList[level=1].name
   limit: do 40 znaków
   EN: .-.. -
   PL: .-.. -
733. [Umiejętność wroga [9009003] (ulepszenie 1) — opis] [WinDuel] 자신을 제외한 살아있는 백화 상태의 아군 수당 대상의 정신력 피해 1
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009003].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Deal 1 SP damage to target for each surviving Pallidified ally (not counting this unit)
   PL: [WinDuel] zadaje 1 obrażeń SP celowi za każdego żyjącego Zbielałego sojusznika (nie licząc tej jednostki)
734. [Umiejętność wroga [9009003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 40%만큼 체력 회복
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Umiejętność wroga [9009003] (ulepszenie 1) — moneta 1, efekt 2 — opis] 대상이 가지고있는 버프 하나를 다음 턴에 자신이 얻음.\n(공격 위력 증가, 신속, 피해량 증가, <sprite name="Protection"><color=#f8c200><u><link="Protection">보호</link></u></color>에 한함)
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <sprite name="Protection">, <color=#f8c200>, <u>, <link="Protection">, </link>, </u>, </color>, \n
   EN: Copy one of the buffs currently applied to the target. Gain the copied buff next turn.\n(Limited to: Attack Power Up, Haste, Damage Up, and <sprite name="Protection"><color=#f8c200><u><link="Protection">Protection</link></u></color>)
   PL: kopiuje 1 z Efektów należących obecnie do celu; zyskuje skopiowany Efekt w następnej turze.\n(ograniczone do: Wzrost Mocy Ataku, Haste, Wzrost Obrażeń i <sprite name="Protection"><color=#f8c200><u><link="Protection">Ochrony</link></u></color>)
736. [Umiejętność wroga [9009003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 40%만큼 체력 회복
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Umiejętność wroga [9009101] (ulepszenie 1) — nazwa] -... .…
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009101].levelList[level=1].name
   limit: do 40 znaków
   EN: -... .…
   PL: -... .…
738. [Umiejętność wroga [9009101] (ulepszenie 1) — opis] 대상에게 <sprite name="Sinking"><color=#e30000><u><link="Sinking">침잠</link></u></color>이 있다면, 체력 회복 효과가 체력이 가장 낮은 백화 상태의 아군 1명에게 같이 적용됨
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009101].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <sprite name="Sinking">, <color=#e30000>, <u>, <link="Sinking">, </link>, </u>, </color>
   EN: If target has <sprite name="Sinking"><color=#e30000><u><link="Sinking">Sinking</link></u></color>, the HP heal effect also applies to 1 other Pallidified ally with the lowest SP
   PL: jeżeli cel ma <sprite name="Sinking"><color=#e30000><u><link="Sinking">Zatonięcie</link></u></color>, efekt przywracania HP dotyczy także 1 innego Zbielałego sojusznika z najniższym SP
739. [Umiejętność wroga [9009101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 30%만큼 체력 회복
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
740. [Umiejętność wroga [9009101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 침잠 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Sinking
   PL: [OnSucceedAttackHead] nakłada 1 Zatonięcia
741. [Umiejętność wroga [9009101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 30%만큼 체력 회복
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Umiejętność wroga [9009101] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 침잠 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 740 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [Umiejętność wroga [9009102] (ulepszenie 1) — nazwa] .--- .
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009102].levelList[level=1].name
   limit: do 40 znaków
   EN: .--- .
   PL: .--- .
744. [Umiejętność wroga [9009102] (ulepszenie 1) — opis] 대상에게 <sprite name="Sinking"><color=#e30000><u><link="Sinking">침잠</link></u></color>이 있다면, 체력 회복 효과가 체력이 가장 낮은 백화 상태의 아군 1명에게 같이 적용됨
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009102].levelList[level=1].desc
   (powtórzenie elementu 738 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Umiejętność wroga [9009102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 체력 회복
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
746. [Umiejętność wroga [9009102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 창백한 소음 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Pallid Noise
   PL: [OnSucceedAttack] nakłada 2 Bladego Szumu
747. [Umiejętność wroga [9009103] (ulepszenie 1) — nazwa] -. .…
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009103].levelList[level=1].name
   limit: do 40 znaków
   EN: -. .…
   PL: -. .…
748. [Umiejętność wroga [9009103] (ulepszenie 1) — opis] [WhenUse] 대상에게 <sprite name="AaCePbBa"><color=#e30000><u><link="AaCePbBa">창백한 소음</link></u></color>이 있을 때, 자신을 제외한 체력이 가장 낮은 백화 상태의 아군 체력 30 회복
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009103].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="AaCePbBa">, <color=#e30000>, <u>, <link="AaCePbBa">, </link>, </u>, </color>, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target has <sprite name="AaCePbBa"><color=#e30000><u><link="AaCePbBa">Pallid Noise</link></u></color>, all other Pallidified allies heal 30 HP
   PL: [WhenUse] jeżeli cel ma <sprite name="AaCePbBa"><color=#e30000><u><link="AaCePbBa">Blady Szum</link></u></color>, wszyscy pozostali Zbielali sojusznicy przywracają 30 HP
749. [Umiejętność wroga [9009103] (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상이 가지고있는 버프 하나를 다음 턴에 자신이 얻음.\n(공격 위력 증가, 신속, 피해량 증가, <sprite name="Protection"><color=#f8c200><u><link="Protection">보호</link></u></color>에 한함)
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 735 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [Umiejętność wroga [9009103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 체력 20 회복
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 20 HP on self
   PL: [OnSucceedAttack] przywraca 20 HP sobie
751. [Umiejętność wroga [9009201] (ulepszenie 1) — nazwa] -- . -.-
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009201].levelList[level=1].name
   limit: do 40 znaków
   EN: -- . -.-
   PL: -- . -.-
752. [Umiejętność wroga [9009201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Tremor
   PL: [OnSucceedAttack] nakłada 3 Wstrząsu
753. [Umiejętność wroga [9009201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 752 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Umiejętność wroga [9009202] (ulepszenie 1) — nazwa] -... .-
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009202].levelList[level=1].name
   limit: do 40 znaków
   EN: -... .-
   PL: -... .-
755. [Umiejętność wroga [9009202] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 자신을 제외한 무작위 아군 1명에게 보호 1 부여. 대상이 백화 상태면 추가로 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009202].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Apply 1 Protection to 1 other random ally next turn. If the ally is a Pallidified ally, apply 1 additional Protection.
   PL: [WhenUse] nakłada 1 Ochrony na 1 losowego innego sojusznika w następnej turze. Jeżeli sojusznik jest Zbielały, nakłada dodatkowo 1 Ochrony.
756. [Umiejętność wroga [9009202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 4 증가
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +4 Tremor Count
   PL: [OnSucceedAttack] nakłada 4 Licznika Wstrząsu
757. [Umiejętność wroga [9009203] (ulepszenie 1) — nazwa] -.-. ..-
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009203].levelList[level=1].name
   limit: do 40 znaków
   EN: -.-. ..-
   PL: -.-. ..-
758. [Umiejętność wroga [9009203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Trigger Tremor Burst
   PL: [OnSucceedAttack] uruchamia Wyładowanie Wstrząsu
759. [Umiejętność wroga [9009203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 횟수 2 감소
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Reduce Tremor Count by 2
   PL: [OnSucceedAttack] zmniejsza Licznik Wstrząsu o 2
760. [Umiejętność wroga [9009203] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 창백한 소음 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009203].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Pallid Noise
   PL: [OnSucceedAttack] nakłada 1 Bladego Szumu
761. [Umiejętność wroga [9009203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 10 부여, 파열 횟수 4 증가
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 10 Rupture and +4 Rupture Count
   PL: [OnSucceedAttack] nakłada 10 Rozdarcia i 4 Licznika Rozdarcia
762. [Umiejętność wroga [9009204] (ulepszenie 1) — nazwa] .--. .
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009204].levelList[level=1].name
   limit: do 40 znaków
   EN: .--. .
   PL: .--. .
763. [Umiejętność wroga [9009204] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 자신을 제외한 백화 상태의 아군 2명당 보호 1 얻음\n보호막이 있는 동안 피격 시 공격자에게 진동 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009204].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 1 Protection for every 2 Pallidified ally (not counting this unit)\nWhen attacked while this unit has Shield, inflict 1 Tremor to the attacker
   PL: [StartBattle] zyskuje 1 Ochrony za każde 2 Zbielałych sojuszników (nie licząc tej jednostki)\nprzy trafieniu, gdy ta jednostka ma Tarczę, nakłada 1 Wstrząsu na atakującego
764. [Umiejętność wroga [9009301] (ulepszenie 1) — nazwa] ..-. .
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009301].levelList[level=1].name
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Umiejętność wroga [9009301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 방어 레벨 감소 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Defense Level Down
   PL: [OnSucceedAttack] nakłada 2 Spadek Poziomu Obrony
766. [Umiejętność wroga [9009302] (ulepszenie 1) — nazwa] .-.. .
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009302].levelList[level=1].name
   limit: do 40 znaków
   EN: .-.. .
   PL: .-.. .
767. [Umiejętność wroga [9009302] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 자신을 제외한 무작위 백화 상태의 아군 1명에게 피해량 증가 1을 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Apply 1 Damage Up to 1 other random Pallidified ally next turn
   PL: [WhenUse] nakłada 1 Wzrost Obrażeń na 1 losowego innego Zbielałego sojusznika w następnej turze
768. [Umiejętność wroga [9009302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마비 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Paralyze
   PL: [OnSucceedAttack] nakłada 2 Paraliżu
769. [Umiejętność wroga [9009302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 창백한 소음 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Pallid Noise
   PL: [OnSucceedAttackHead] nakłada 1 Bladego Szumu
770. [Umiejętność wroga [9009303] (ulepszenie 1) — nazwa] .-.. .-
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009303].levelList[level=1].name
   limit: do 40 znaków
   EN: .-.. .-
   PL: .-.. .-
771. [Umiejętność wroga [9009303] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 자신을 포함한 백화 상태의 무작위 아군 1명에게 공격 위력 증가 1을 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Apply 1 Damage Up to 1 random Pallidified ally next turn
   PL: [WhenUse] nakłada 1 Wzrost Obrażeń na 1 losowego Zbielałego sojusznika w następnej turze
772. [Umiejętność wroga [9009303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 방어 레벨 감소 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Umiejętność wroga [9009303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 창백한 소음 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 760 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Umiejętność wroga [9009303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 방어 레벨 감소 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Umiejętność wroga [9009401] (ulepszenie 1) — nazwa] --. . ...-
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009401].levelList[level=1].name
   limit: do 40 znaków
   EN: --. . ...-
   PL: --. . ...-
776. [Umiejętność wroga [9009401] (ulepszenie 1) — opis] 대상에게 <sprite name="AaCePbBa"><color=#e30000><u><link="AaCePbBa">창백한 소음</link></u></color>이 있을 때, 자신을 제외한 살아있는 아군당 대상의 정신력 피해 1
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="AaCePbBa">, <color=#e30000>, <u>, <link="AaCePbBa">, </link>, </u>, </color>
   EN: If target has <sprite name="AaCePbBa"><color=#e30000><u><link="AaCePbBa">Pallid Noise</link></u></color>, deal 1 SP damage to target for every other surviving ally
   PL: jeżeli cel ma <sprite name="AaCePbBa"><color=#e30000><u><link="AaCePbBa">Blady Szum</link></u></color>, zadaje 1 obrażeń SP celowi za każdego innego żyjącego sojusznika
777. [Umiejętność wroga [9009401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 2 증가
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Umiejętność wroga [9009401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 출혈 3 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 506 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Umiejętność wroga [9009402] (ulepszenie 1) — nazwa] ...- …
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009402].levelList[level=1].name
   limit: do 40 znaków
   EN: ...- …
   PL: ...- …
780. [Umiejętność wroga [9009402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 창백한 소음 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 760 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Umiejętność wroga [9009402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 520 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Umiejętność wroga [9009402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Umiejętność wroga [9009403] (ulepszenie 1) — nazwa] .--. .... -
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009403].levelList[level=1].name
   limit: do 40 znaków
   EN: .--. .... -
   PL: .--. .... -
784. [Umiejętność wroga [9009403] (ulepszenie 1) — opis] [WinDuel] 창백한 소음 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009403].levelList[level=1].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Umiejętność wroga [9009403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 4 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Bleed next turn
   PL: [OnSucceedAttack] nakłada 4 Krwawienia w następnej turze
786. [Umiejętność wroga [9009403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 535 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Umiejętność wroga [9009404] (ulepszenie 1) — nazwa] -.- -
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009404].levelList[level=1].name
   limit: do 40 znaków
   EN: -.- -
   PL: -.- -
788. [Umiejętność wroga [9009404] (ulepszenie 1) — opis] 보호막이 남았을 때 피격 시 대상에게 창백한 소음 1 부여\n[EndBattle] 보호막이 남았을 때, 다음 턴에 호흡 3을 얻음.
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009404].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [EndBattle]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]
   EN: When attacked while this unit has Shield, inflict 1 Pallid Noise to the target\n[EndBattle] If this unit has Shield, gain 3 Poise next turn
   PL: przy trafieniu, gdy ta jednostka ma Tarczę, nakłada 1 Bladego Szumu na cel\n[EndBattle] jeżeli ta jednostka ma Tarczę, zyskuje 3 Oddechu w następnej turze
789. [Umiejętność wroga [9009501] (ulepszenie 1) — nazwa] .--. -
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009501].levelList[level=1].name
   limit: do 40 znaków
   EN: .--. -
   PL: .--. -
790. [Umiejętność wroga [9009501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Umiejętność wroga [9009501] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009501].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Umiejętność wroga [9009502] (ulepszenie 1) — nazwa] .-.. - ..-
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009502].levelList[level=1].name
   limit: do 40 znaków
   EN: .-.. - ..-
   PL: .-.. - ..-
793. [Umiejętność wroga [9009502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [Umiejętność wroga [9009502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Umiejętność wroga [9009502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 피해량 감소 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Umiejętność wroga [9009502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Umiejętność wroga [9009503] (ulepszenie 1) — nazwa] -- .... -
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009503].levelList[level=1].name
   limit: do 40 znaków
   EN: -- .... -
   PL: -- .... -
798. [Umiejętność wroga [9009503] (ulepszenie 1) — opis] [WhenUse] 아군이 살아있다면, 1명당 보호 1을 얻음. (최대 3)
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Protection for every surviving ally. (Max 3)
   PL: [WhenUse] zyskuje 1 Ochrony za każdego żyjącego sojusznika. (maks. 3)
799. [Umiejętność wroga [9009503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 보호 2 얻음
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 552 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Umiejętność wroga [9009503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 창백한 소음 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 769 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Umiejętność wroga [9009503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 보호 2 얻음
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 553 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Umiejętność wroga [9009503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 출혈 4 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 4 Bleed next turn
   PL: [OnSucceedAttackHead] nakłada 4 Krwawienia w następnej turze
803. [Umiejętność wroga [9009504] (ulepszenie 1) — nazwa] -.- ..
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009504].levelList[level=1].name
   limit: do 40 znaków
   EN: -.- ..
   PL: -.- ..
804. [Umiejętność wroga [9009504] (ulepszenie 1) — opis] [WhenUse] 보호 2 얻음\n보호막이 남았을 때 피격 시 대상에게 창백한 소음 1 부여\n[EndBattle] 자신의 체력을 남은 보호막의 2배만큼 회복함.
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009504].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [WhenUse] Gain 2 Protection\nWhen attacked while this unit has Shield, inflict 1 Pallid Noise to the target\n[EndBattle] Heal HP by x2 of the remaining Shield HP.
   PL: [WhenUse] zyskuje 2 Ochrony\nprzy trafieniu, gdy ta jednostka ma Tarczę, nakłada 1 Bladego Szumu na cel\n[EndBattle] przywraca HP równe (pozostałe HP Tarczy x 2).
805. [Umiejętność wroga [9009601] (ulepszenie 1) — nazwa] 명치 후리기
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009601].levelList[level=1].name
   limit: do 40 znaków
   EN: Right in the Solar Plexus
   PL: Right in the Solar Plexus
806. [Umiejętność wroga [9009601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 마비 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Paralyze next turn
   PL: [OnSucceedAttackHead] nakłada 1 Paraliżu w następnej turze
807. [Umiejętność wroga [9009602] (ulepszenie 1) — nazwa] 기억한다!
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009602].levelList[level=1].name
   limit: do 40 znaków
   EN: We Remember!
   PL: We Remember!
808. [Umiejętność wroga [9009602] (ulepszenie 1) — opis] [DefeatDuel] 다음 턴에 피해량 증가 1 얻음
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Gain 1 Damage Up next turn
   PL: [DefeatDuel] zyskuje 1 Wzrost Obrażeń w następnej turze
809. [Umiejętność wroga [9009602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Umiejętność wroga [9009602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 웨이브동안 죽은 중지 소속 아군 수만큼 추가 고정 피해
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal additional fixed damage equal to the number of the Middle allies killed during this wave
   PL: [OnSucceedAttack] zadaje dodatkowe stałe obrażenia równe liczbie sojuszników Środkowego pokonanych podczas tej fali
811. [Umiejętność wroga [9009603] (ulepszenie 1) — nazwa] 머리 으깨기
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009603].levelList[level=1].name
   limit: do 40 znaków
   EN: Skull Crushing
   PL: Skull Crushing
812. [Umiejętność wroga [9009603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Attack Power Down next turn
   PL: [OnSucceedAttackHead] nakłada 1 Spadek Mocy Ataku w następnej turze
813. [Umiejętność wroga [9009603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 711 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Umiejętność wroga [9009604] (ulepszenie 1) — nazwa] 새길 준비
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009604].levelList[level=1].name
   limit: do 40 znaków
   EN: Ready to Write
   PL: Ready to Write
815. [Umiejętność wroga [9009604] (ulepszenie 1) — opis] [EndBattle] 보호막이 남아있으면 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndBattle]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [EndBattle] If this unit has Shield, gain 1 Attack Power Up next turn
   PL: [EndBattle] jeżeli ta jednostka ma Tarczę, zyskuje 1 Wzrost Mocy Ataku w następnej turze
816. [Umiejętność wroga [9009605] (ulepszenie 1) — nazwa] 앙갚음
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009605].levelList[level=1].name
   limit: do 40 znaków
   EN: Vengeance
   PL: Vengeance
817. [Umiejętność wroga [9009605] (ulepszenie 1) — opis] [DefeatDuel] 다음 턴에 피해량 증가 1 얻음
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009605].levelList[level=1].desc
   (powtórzenie elementu 808 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Umiejętność wroga [9009605] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009605].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 711 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Umiejętność wroga [9009605] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackTail] 8만큼 흐트러짐 손상
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009605].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Raise Stagger Threshold by 8
   PL: [OnSucceedAttackTail] podnosi Próg Oszołomienia o 8
820. [Umiejętność wroga [9009606] (ulepszenie 1) — nazwa] 배로 갚기
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009606].levelList[level=1].name
   limit: do 40 znaków
   EN: Multifold Retribution
   PL: Multifold Retribution
821. [Umiejętność wroga [9009606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 30만큼 흐트러짐 손상
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 30
   PL: [OnSucceedAttack] podnosi Próg Oszołomienia o 30
822. [Umiejętność wroga [9009606] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 20만큼 고정 체력 피해
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009606].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 20 fixed HP damage
   PL: [OnSucceedAttack] zadaje 20 stałych obrażeń HP
823. [Umiejętność wroga [9009606] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 다음 턴에 마비 3 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009606].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Paralyze next turn
   PL: [OnSucceedAttackHead] nakłada 3 Paraliżu w następnej turze
824. [Umiejętność wroga [9009701] (ulepszenie 1) — nazwa] 명치 후리기
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009701].levelList[level=1].name
   (powtórzenie elementu 805 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Umiejętność wroga [9009701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 마비 1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 806 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Umiejętność wroga [9009702] (ulepszenie 1) — nazwa] 새겨라!
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009702].levelList[level=1].name
   limit: do 40 znaków
   EN: Write Their Sins!
   PL: Write Their Sins!
827. [Umiejętność wroga [9009702] (ulepszenie 1) — opis] [DefeatDuel] 다음 턴에 피해량 증가 1 얻음
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009702].levelList[level=1].desc
   (powtórzenie elementu 808 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [Umiejętność wroga [9009702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 피해량 감소 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Umiejętność wroga [9009702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 웨이브동안 죽은 중지 소속 아군 수만큼 추가 고정 피해
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 810 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [Umiejętność wroga [9009703] (ulepszenie 1) — nazwa] 머리 터트리기
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009703].levelList[level=1].name
   limit: do 40 znaków
   EN: Skull Bursting
   PL: Skull Bursting
831. [Umiejętność wroga [9009703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 더하기 코인 약화1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Plus Coin Drop next turn
   PL: [OnSucceedAttackHead] nakłada 1 Osłabienia Monet Plus w następnej turze
832. [Umiejętność wroga [9009703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 더하기 코인 약화1 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Plus Coin Drop next turn
   PL: [OnSucceedAttack] nakłada 1 Osłabienia Monet Plus w następnej turze
833. [Umiejętność wroga [9009704] (ulepszenie 1) — nazwa] 새길 준비
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009704].levelList[level=1].name
   (powtórzenie elementu 814 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Umiejętność wroga [9009704] (ulepszenie 1) — opis] 보호막이 전부 소진되면, 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009704].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this unit's Shield is fully depleted, gain 1 Attack Power Up next turn
   PL: jeżeli Tarcza tej jednostki została całkowicie wyczerpana, zyskuje 1 Wzrost Mocy Ataku w następnej turze
835. [Umiejętność wroga [9009705] (ulepszenie 1) — nazwa] 앙갚음
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009705].levelList[level=1].name
   (powtórzenie elementu 816 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [Umiejętność wroga [9009705] (ulepszenie 1) — opis] [DefeatDuel] 다음 턴에 피해량 증가 1 얻음
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009705].levelList[level=1].desc
   (powtórzenie elementu 808 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Umiejętność wroga [9009705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 2 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 711 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Umiejętność wroga [9009705] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackTail] 8만큼 흐트러짐 손상
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009705].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 819 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Umiejętność wroga [9009706] (ulepszenie 1) — nazwa] 배로 갚기
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009706].levelList[level=1].name
   (powtórzenie elementu 820 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Umiejętność wroga [9009706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 30만큼 흐트러짐 손상
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [Umiejętność wroga [9009706] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 20만큼 고정 체력 피해
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009706].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
842. [Umiejętność wroga [9009706] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 마비 3 부여
   źródło: Skills_Enemy-a1c5p2.json :: dataList[id=9009706].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 677 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c5p2] Pasywka wroga: Passives_Enemy-a1c5p2
- plik gry: `Passives_Enemy-a1c5p2.json`

843. [[a1c5p2] Pasywka wroga [9008801] — nazwa] 형용할 수 없는 형체
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9008801].name
   limit: do 40 znaków
   EN: Ineffable Shape
   PL: Ineffable Shape
844. [[a1c5p2] Pasywka wroga [9008801] — opis] 교전 중 사망시 자신을 마지막으로 공격한 인격의 정신력 피해 10
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9008801].desc
   limit: do 120 znaków
   EN: When killed in combat, deal 10 SP damage to the unit that attacked it last
   PL: gdy zostaje pokonana w walce, zadaje 10 obrażeń SP jednostce, która atakowała ją jako ostatnia
