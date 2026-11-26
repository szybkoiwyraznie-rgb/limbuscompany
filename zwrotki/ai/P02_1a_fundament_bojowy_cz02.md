# Paczka AI P02 (Fala 1 · 1A) — Fundament bojowy — grzechy, odporności, tagi, Panika i interfejs walki (część 2/2)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P02_1a_fundament_bojowy_cz02.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P02_1a_fundament_bojowy_cz02.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Poczytalność i Panika: PanicInfo-walpu5
- plik gry: `PanicInfo-walpu5.json`

1. [Poczytalność i Panika [1035] — efekt niskiego morale] 전투 중 [Smoke] 혹은 [Smoke] 횟수를 얻을 때, 추가로 1 얻음.\n턴 시작 시 [Vulnerable] 3, [AttackDmgUp] 2, [Endurance] 1 얻음
   źródło: PanicInfo-walpu5.json :: dataList[id=1035].lowMoraleDescription
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Smoke], [Vulnerable], [AttackDmgUp], [Endurance]
   znaczenie tagów: [Smoke] = 연기 / Smoke; [Vulnerable] = 취약 / Fragile; [AttackDmgUp] = 피해량 증가 / Damage Up; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: Gain 1 additional [Smoke] or [Smoke] Count when gaining them.\nTurn Start: gain 3 [Vulnerable], 2 [AttackDmgUp], and 1 [Endurance].
   PL: Zyskując [Smoke] lub Licznik [Smoke] w walce, zyskaj dodatkowo +1.\nPoczątek Tury: zyskaj 3 [Vulnerable], 2 [AttackDmgUp] i 1 [Endurance]
2. [Poczytalność i Panika [1035] — efekt Paniki] 전투 중 [Smoke] 혹은 [Smoke] 횟수를 얻을 때, 추가로 2 얻음.\n턴 시작 시 [Vulnerable] 3, [AttackDmgUp] 4, [Endurance] 2 얻음
   źródło: PanicInfo-walpu5.json :: dataList[id=1035].panicDescription
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Smoke], [Vulnerable], [AttackDmgUp], [Endurance]
   znaczenie tagów: [Smoke] = 연기 / Smoke; [Vulnerable] = 취약 / Fragile; [AttackDmgUp] = 피해량 증가 / Damage Up; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: Gain 2 additional [Smoke] or [Smoke] Count when gaining them.\nTurn Start: gain 3 [Vulnerable], 4 [AttackDmgUp], and 2 [Endurance].
   PL: Zyskując [Smoke] lub Licznik [Smoke] w walce, zyskaj dodatkowo +2.\nPoczątek Tury: zyskaj 3 [Vulnerable], 4 [AttackDmgUp] i 2 [Endurance]

## Poczytalność i Panika: PanicInfo-x1p1c1
- plik gry: `PanicInfo-x1p1c1.json`

3. [Poczytalność i Panika [1089] — nazwa Paniki] 맛있어짐
   źródło: PanicInfo-x1p1c1.json :: dataList[id=1089].panicName
   limit: do 40 znaków
   EN: Yummers
   PL: Pyszności
4. [Poczytalność i Panika [1089] — efekt niskiego morale] 턴 시작시 [Vulnerable] 1 얻음
   źródło: PanicInfo-x1p1c1.json :: dataList[id=1089].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Turn Start: Gain 1 [Vulnerable]
   PL: Początek Tury: zyskaj 1 [Vulnerable]
5. [Poczytalność i Panika [1089] — efekt Paniki] 턴 시작시 [Vulnerable] 2 얻음
   źródło: PanicInfo-x1p1c1.json :: dataList[id=1089].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Turn Start: Gain 2 [Vulnerable]
   PL: Początek Tury: zyskaj 2 [Vulnerable]

## Poczytalność i Panika: PanicInfo
- plik gry: `PanicInfo.json`

6. [Poczytalność i Panika [1001] — nazwa Paniki] 자해
   źródło: PanicInfo.json :: dataList[id=1001].panicName
   limit: do 40 znaków
   EN: Compulsion
   PL: Samookaleczenie
7. [Poczytalność i Panika [1001] — efekt niskiego morale] 턴 시작 시, <sprite name="Agility"><color=#f8c200><u><link="Agility">신속</color></link></u> 2, <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">취약</color></link></u> 2를 얻음
   źródło: PanicInfo.json :: dataList[id=1001].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Agility">, <color=#f8c200>, <u>, <link="Agility">, </color>, </link>, </u>, <sprite name="Vulnerable">, <color=#e30000>, <link="Vulnerable">
   EN: Turn Start: Gain 2 <sprite name="Agility"><color=#f8c200><u><link="Agility">Haste</color></link></u> and 2 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Fragile</color></link></u>
   PL: Początek Tury: zyskaj 2 <sprite name="Agility"><color=#f8c200><u><link="Agility">Pośpiech</link></u></color> oraz 2 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Wrażliwość</link></u></color>
8. [Poczytalność i Panika [1001] — efekt Paniki] 턴 시작 시 자신의 체력 -10
   źródło: PanicInfo.json :: dataList[id=1001].panicDescription
   limit: do 120 znaków
   EN: Turn Start: Lose 10 HP.
   PL: Początek Tury: trać 10 PŻ.
9. [Poczytalność i Panika [1002] — nazwa Paniki] 비난
   źródło: PanicInfo.json :: dataList[id=1002].panicName
   limit: do 40 znaków
   EN: Outlash
   PL: Wybuch Gniewu
10. [Poczytalność i Panika [1002] — efekt niskiego morale] 턴 시작 시, <sprite name="Enhancement"><color=#f8c200><u><link="Enhancement">공격 위력 증가</color></link></u> 2, <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">취약</color></link></u> 2를 얻음
   źródło: PanicInfo.json :: dataList[id=1002].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Enhancement">, <color=#f8c200>, <u>, <link="Enhancement">, </color>, </link>, </u>, <sprite name="Vulnerable">, <color=#e30000>, <link="Vulnerable">
   EN: Turn Start: Gain 2 <sprite name="Enhancement"><color=#f8c200><u><link="Enhancement">Attack Power Up</color></link></u> and 2 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Fragile</color></link></u>
   PL: Początek Tury: zyskaj 2 <sprite name="Enhancement"><color=#f8c200><u><link="Enhancement">Wzrost Mocy Ataku</link></u></color> oraz 2 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Wrażliwość</link></u></color>
11. [Poczytalność i Panika [1002] — efekt Paniki] 자신의 턴 시작 시 무작위 아군의 정신력 - 20
   źródło: PanicInfo.json :: dataList[id=1002].panicDescription
   limit: do 120 znaków
   EN: Turn Start: Random ally loses 20 SP.
   PL: Początek Tury: losowy sojusznik traci 20 SP.
12. [Poczytalność i Panika [1003] — nazwa Paniki] 압도
   źródło: PanicInfo.json :: dataList[id=1003].panicName
   limit: do 40 znaków
   EN: Overwhelmed
   PL: Przytłoczenie
13. [Poczytalność i Panika [1003] — efekt niskiego morale] 턴 시작 시 <sprite name="Reduction"><color=#e30000><u><link="Reduction">공격 위력 감소</color></link></u> 2를 얻음
   źródło: PanicInfo.json :: dataList[id=1003].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Reduction">, <color=#e30000>, <u>, <link="Reduction">, </color>, </link>, </u>
   EN: Turn Start: Gain 2 <sprite name="Reduction"><color=#e30000><u><link="Reduction">Attack Power Down</color></link></u>
   PL: Początek Tury: zyskaj 2 <sprite name="Reduction"><color=#e30000><u><link="Reduction">Spadek Mocy Ataku</link></u></color>
14. [Poczytalność i Panika [1003] — efekt Paniki] 한 턴 동안 행동하지 않음
   źródło: PanicInfo.json :: dataList[id=1003].panicDescription
   limit: do 120 znaków
   EN: Does not act for this turn.
   PL: Nie wykonuje działań w tej turze.
15. [Poczytalność i Panika [1004] — nazwa Paniki] 위축
   źródło: PanicInfo.json :: dataList[id=1004].panicName
   limit: do 40 znaków
   EN: Atrophied
   PL: Skurczenie
16. [Poczytalność i Panika [1004] — efekt niskiego morale] 턴 시작 시 <sprite name="Reduction"><color=#e30000><u><link="Reduction">공격 위력 감소</color></link></u> 2를 얻음
   źródło: PanicInfo.json :: dataList[id=1004].lowMoraleDescription
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [Poczytalność i Panika [1004] — efekt Paniki] 턴 시작 시 <sprite name="Reduction"><color=#e30000><u><link="Reduction">공격 위력 감소</color></link></u> 4를 얻음
   źródło: PanicInfo.json :: dataList[id=1004].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Reduction">, <color=#e30000>, <u>, <link="Reduction">, </color>, </link>, </u>
   EN: Turn Start: Gain 4 <sprite name="Reduction"><color=#e30000><u><link="Reduction">Attack Power Down</color></link></u>
   PL: Początek Tury: zyskaj 4 <sprite name="Reduction"><color=#e30000><u><link="Reduction">Spadek Mocy Ataku</link></u></color>
18. [Poczytalność i Panika [1005] — nazwa Paniki] 분함
   źródło: PanicInfo.json :: dataList[id=1005].panicName
   limit: do 40 znaków
   EN: Agitated
   PL: Wzburzenie
19. [Poczytalność i Panika [1005] — efekt niskiego morale] 턴 시작 시 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">피해량 증가</color></link></u> 1, <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">취약</color></link></u> 2를 얻음
   źródło: PanicInfo.json :: dataList[id=1005].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="AttackDmgUp">, <color=#f8c200>, <u>, <link="AttackDmgUp">, </color>, </link>, </u>, <sprite name="Vulnerable">, <color=#e30000>, <link="Vulnerable">
   EN: Turn Start: Gain 1 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Damage Up</color></link></u> and 2 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Fragile</color></link></u>
   PL: Początek Tury: zyskaj 1 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Wzrost Obrażeń</link></u></color> oraz 2 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Wrażliwość</link></u></color>
20. [Poczytalność i Panika [1005] — efekt Paniki] 턴 시작 시 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">피해량 증가</color></link></u> 2, <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">취약</color></link></u> 5를 얻음
   źródło: PanicInfo.json :: dataList[id=1005].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="AttackDmgUp">, <color=#f8c200>, <u>, <link="AttackDmgUp">, </color>, </link>, </u>, <sprite name="Vulnerable">, <color=#e30000>, <link="Vulnerable">
   EN: Turn Start: Gain 2 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Damage Up</color></link></u> and 5 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Fragile</color></link></u>
   PL: Początek Tury: zyskaj 2 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Wzrost Obrażeń</link></u></color> oraz 5 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Wrażliwość</link></u></color>
21. [Poczytalność i Panika [1006] — nazwa Paniki] 도주
   źródło: PanicInfo.json :: dataList[id=1006].panicName
   limit: do 40 znaków
   EN: Running
   PL: Ucieczka
22. [Poczytalność i Panika [1006] — efekt niskiego morale] 행동하지 않음. 피격 시, 해당 스킬 종료 후 사망
   źródło: PanicInfo.json :: dataList[id=1006].lowMoraleDescription
   limit: do 120 znaków
   EN: Does not act. When hit, this unit is defeated after the skill ends.
   PL: Nie działa. Po otrzymaniu trafienia ginie po zakończeniu umiejętności.
23. [Poczytalność i Panika [1007] — nazwa Paniki] 슬픔
   źródło: PanicInfo.json :: dataList[id=1007].panicName
   limit: do 40 znaków
   EN: Sorrow
   PL: Smutek
24. [Poczytalność i Panika [1007] — efekt niskiego morale] 매 턴마다 <sprite name="AttackDmgDown"><color=#e30000><u><link="AttackDmgDown">피해량 감소</color></link></u> 2를 얻음
   źródło: PanicInfo.json :: dataList[id=1007].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="AttackDmgDown">, <color=#e30000>, <u>, <link="AttackDmgDown">, </color>, </link>, </u>
   EN: Gain 2 <sprite name="AttackDmgDown"><color=#e30000><u><link="AttackDmgDown">Damage Down</color></link></u> each turn
   PL: Co turę zyskaj 2 <sprite name="AttackDmgDown"><color=#e30000><u><link="AttackDmgDown">Spadek Obrażeń</link></u></color>
25. [Poczytalność i Panika [1007] — efekt Paniki] 매 턴마다 <sprite name="AttackDmgDown"><color=#e30000><u><link="AttackDmgDown">피해량 감소</color></link></u> 5, <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">취약</color></link></u> 2를 얻음
   źródło: PanicInfo.json :: dataList[id=1007].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="AttackDmgDown">, <color=#e30000>, <u>, <link="AttackDmgDown">, </color>, </link>, </u>, <sprite name="Vulnerable">, <link="Vulnerable">
   EN: Gain 5 <sprite name="AttackDmgDown"><color=#e30000><u><link="AttackDmgDown">Damage Down</color></link></u> and 2 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Fragile</color></link></u> each turn
   PL: Co turę zyskaj 5 <sprite name="AttackDmgDown"><color=#e30000><u><link="AttackDmgDown">Spadek Obrażeń</link></u></color> oraz 2 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Wrażliwość</link></u></color>
26. [Poczytalność i Panika [1008] — nazwa Paniki] 광인
   źródło: PanicInfo.json :: dataList[id=1008].panicName
   limit: do 40 znaków
   EN: Maddened
   PL: Obłęd
27. [Poczytalność i Panika [1008] — efekt niskiego morale] 첫 사기저하일 때, 피아식별 불가상태
   źródło: PanicInfo.json :: dataList[id=1008].lowMoraleDescription
   limit: do 120 znaków
   EN: When at low morale for the first time, targets units indiscriminately
   PL: Przy pierwszym wejściu w Niskie Morale atakuje cele bez rozróżnienia
28. [Poczytalność i Panika [1008] — efekt Paniki] 피아식별 불가상태, 합 위력 +1, <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">피해량 증가</color></link></u> 2 얻음
   źródło: PanicInfo.json :: dataList[id=1008].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="AttackDmgUp">, <color=#f8c200>, <u>, <link="AttackDmgUp">, </color>, </link>, </u>
   EN: Targets indiscriminately; Clash Power +1, and gain 2 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Damage Up</color></link></u>
   PL: Atakuje bez rozróżnienia; Moc Starcia +1 oraz zyskaj 2 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Wzrost Obrażeń</link></u></color>
29. [Poczytalność i Panika [1009] — nazwa Paniki] 자살
   źródło: PanicInfo.json :: dataList[id=1009].panicName
   limit: do 40 znaków
   EN: Suicidal
   PL: Samobójczy Pęd
30. [Poczytalność i Panika [1009] — efekt niskiego morale] 첫 사기저하 상태였을 때, 행동 불가 상태
   źródło: PanicInfo.json :: dataList[id=1009].lowMoraleDescription
   limit: do 120 znaków
   EN: When at low morale for the first time, become unable to act
   PL: Przy pierwszym wejściu w Niskie Morale nie może działać
31. [Poczytalność i Panika [1009] — efekt Paniki] 3턴 간 행동불가 상태. 3턴 경과 후 턴 시작 시 사망. 사망 시 모든 아군 정신력 감소 조건에 10 추가 감소
   źródło: PanicInfo.json :: dataList[id=1009].panicDescription
   limit: do 170 znaków
   EN: Cannot act for 3 turns. After 3 turns, unit dies at turn start; all its allies lose additional 10 SP with every SP loss condition
   PL: Nie może działać przez 3 tury. Po 3 turach ginie na początku tury; po śmierci wszyscy sojusznicy tracą dodatkowo 10 SP przy każdym warunku utraty SP
32. [Poczytalność i Panika [1010] — nazwa Paniki] 배회
   źródło: PanicInfo.json :: dataList[id=1010].panicName
   limit: do 40 znaków
   EN: Wandering
   PL: Błądzenie
33. [Poczytalność i Panika [1010] — efekt niskiego morale] 턴 종료 시 아군에게 정신력 2 피해
   źródło: PanicInfo.json :: dataList[id=1010].lowMoraleDescription
   limit: do 120 znaków
   EN: Turn End: Deal 2 SP damage to allies
   PL: Koniec Tury: zadaj 2 obrażeń SP sojusznikom
34. [Poczytalność i Panika [1010] — efekt Paniki] 3턴 간 턴 종료 시 아군에게 정신력 5 피해\n3턴 종료 시 도주함
   źródło: PanicInfo.json :: dataList[id=1010].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Deal 5 SP damage to allies. Flees from battle after 3 turns have passed
   PL: Koniec Tury: przez 3 tury zadaje 5 obrażeń SP sojusznikom\nPo zakończeniu 3. tury ucieka z walki
35. [Poczytalność i Panika [1011] — nazwa Paniki] 불안정
   źródło: PanicInfo.json :: dataList[id=1011].panicName
   limit: do 40 znaków
   EN: Unstable
   PL: Niestabilność
36. [Poczytalność i Panika [1011] — efekt niskiego morale] 턴 시작 시 <sprite name="Enhancement"><color=#f8c200><u><link="Enhancement">공격 위력 증가</color></link></u> 2, <sprite name="Binding"><color=#e30000><u><link="Binding">속박</color></link></u> 3 얻음
   źródło: PanicInfo.json :: dataList[id=1011].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Enhancement">, <color=#f8c200>, <u>, <link="Enhancement">, </color>, </link>, </u>, <sprite name="Binding">, <color=#e30000>, <link="Binding">
   EN: Turn Start: Gain 2 <sprite name="Enhancement"><color=#f8c200><u><link="Enhancement">Attack Power Up</color></link></u> and 3 <sprite name="Binding"><color=#e30000><u><link="Binding">Bind</color></link></u>
   PL: Początek Tury: zyskaj 2 <sprite name="Enhancement"><color=#f8c200><u><link="Enhancement">Wzrost Mocy Ataku</link></u></color> oraz 3 <sprite name="Binding"><color=#e30000><u><link="Binding">Spętanie</link></u></color>
37. [Poczytalność i Panika [1011] — efekt Paniki] 턴 시작 시 흐트러짐
   źródło: PanicInfo.json :: dataList[id=1011].panicDescription
   limit: do 120 znaków
   EN: Turn Start: Become staggered
   PL: Początek Tury: wpada w Oszołomienie
38. [Poczytalność i Panika [1012] — nazwa Paniki] 슬픔
   źródło: PanicInfo.json :: dataList[id=1012].panicName
   limit: do 40 znaków
   EN: Dejection
   PL: Przygnębienie
39. [Poczytalność i Panika [1012] — efekt niskiego morale] <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">취약</color></link></u> 1 얻음. 합 중 코인이 한 번이라도 뒷면이라면, 해당 합 동안 합 위력 -1.
   źródło: PanicInfo.json :: dataList[id=1012].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Vulnerable">, <color=#e30000>, <u>, <link="Vulnerable">, </color>, </link>, </u>
   EN: Gain 1 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Fragile</color></link></u>; In a clash, if any Coin lands tails, Clash Power -1 for the clash.
   PL: Zyskaj 1 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Wrażliwość</link></u></color>. Jeśli w Starciu choć jedna Moneta wypadnie Rewersem, Moc Starcia -1 w tym Starciu.
40. [Poczytalność i Panika [1012] — efekt Paniki] <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">취약</color></link></u> 3 얻음. 합 중 코인이 한 번이라도 뒷면이라면, 해당 합 동안 합 위력 -3.
   źródło: PanicInfo.json :: dataList[id=1012].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Vulnerable">, <color=#e30000>, <u>, <link="Vulnerable">, </color>, </link>, </u>
   EN: Gain 3 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Fragile</color></link></u>; In a clash, if any Coin lands tails, Clash Power -3 for the clash.
   PL: Zyskaj 3 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Wrażliwość</link></u></color>. Jeśli w Starciu choć jedna Moneta wypadnie Rewersem, Moc Starcia -3 w tym Starciu.
41. [Poczytalność i Panika [9999] — nazwa Paniki] 패닉
   źródło: PanicInfo.json :: dataList[id=9999].panicName
   limit: do 40 znaków
   EN: Panic
   PL: Panika
42. [Poczytalność i Panika [9999] — efekt Paniki] 한 턴 동안 행동하지 않음
   źródło: PanicInfo.json :: dataList[id=9999].panicDescription
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Poczytalność i Panika [1013] — nazwa Paniki] 불순
   źródło: PanicInfo.json :: dataList[id=1013].panicName
   limit: do 40 znaków
   EN: Impurity
   PL: Skaza
44. [Poczytalność i Panika [1013] — efekt niskiego morale] <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">취약</color></link></u> 1을 얻음. 합 패배시 대상의 정신력 -2
   źródło: PanicInfo.json :: dataList[id=1013].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Vulnerable">, <color=#e30000>, <u>, <link="Vulnerable">, </color>, </link>, </u>
   EN: Gain 1 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Fragile</color></link></u>. Target loses 2 SP if this unit loses the clash
   PL: Zyskaj 1 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Wrażliwość</link></u></color>. Po przegranym Starciu cel traci 2 SP
45. [Poczytalność i Panika [1013] — efekt Paniki] <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">취약</color></link></u> 2를 얻음. 합 패배시 대상의 정신력 -5
   źródło: PanicInfo.json :: dataList[id=1013].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Vulnerable">, <color=#e30000>, <u>, <link="Vulnerable">, </color>, </link>, </u>
   EN: Gain 1 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Fragile</color></link></u>. Target loses 5 SP if this unit loses the clash
   PL: Zyskaj 2 <sprite name="Vulnerable"><color=#e30000><u><link="Vulnerable">Wrażliwość</link></u></color>. Po przegranym Starciu cel traci 5 SP
46. [Poczytalność i Panika [1014] — nazwa Paniki] 앙갚음
   źródło: PanicInfo.json :: dataList[id=1014].panicName
   limit: do 40 znaków
   EN: Vengeance
   PL: Odwet
47. [Poczytalność i Panika [1014] — efekt niskiego morale] 턴 시작 시 <sprite name="Enhancement"><color=#f8c200><u><link="Enhancement">공격 위력 증가</color></link></u> 1, <sprite name="DefenseDown"><color=#e30000><u><link="DefenseDown">방어 레벨 감소</color></link></u> 3을 얻고, 이전 턴에 받은 누적 피해량에 비례하여 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">피해량 증가</color></link></u>를 얻음\n(최대 체력의 3%당 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">피해량 증가</color></link></u> 1을 얻음)
   źródło: PanicInfo.json :: dataList[id=1014].lowMoraleDescription
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <sprite name="Enhancement">, <color=#f8c200>, <u>, <link="Enhancement">, </color>, </link>, </u>, <sprite name="DefenseDown">, <color=#e30000>, <link="DefenseDown">, <sprite name="AttackDmgUp">, <link="AttackDmgUp">, \n
   EN: Turn Start: Gain 1 <sprite name="Enhancement"><color=#f8c200><u><link="Enhancement">Attack Power Up</color></link></u> and 3 <sprite name="DefenseDown"><color=#e30000><u><link="DefenseDown">Defense Level Down</color></link></u>. Gain <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Damage Up</color></link></u> based on the amount of damage taken last turn (1 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Damage Up</color></link></u> for every 3% of Max HP lost)
   PL: Początek Tury: zyskaj 1 <sprite name="Enhancement"><color=#f8c200><u><link="Enhancement">Wzrost Mocy Ataku</link></u></color> i 3 <sprite name="DefenseDown"><color=#e30000><u><link="DefenseDown">Spadek Poziomu Obrony</link></u></color> oraz zyskaj <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Wzrost Obrażeń</link></u></color> zależnie od obrażeń otrzymanych w poprzedniej turze\n(1 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Wzrost Obrażeń</link></u></color> za każde 3% Maks. PŻ)
48. [Poczytalność i Panika [1014] — efekt Paniki] 턴 시작 시 <sprite name="Enhancement"><color=#f8c200><u><link="Enhancement">공격 위력 증가</color></link></u> 2, <sprite name="DefenseDown"><color=#e30000><u><link="DefenseDown">방어 레벨 감소</color></link></u> 6을 얻고, 이전 턴에 받은 누적 피해량에 비례하여 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">피해량 증가</color></link></u>를 얻음\n(최대 체력의 3%당 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">피해량 증가</color></link></u> 1을 얻음)
   źródło: PanicInfo.json :: dataList[id=1014].panicDescription
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <sprite name="Enhancement">, <color=#f8c200>, <u>, <link="Enhancement">, </color>, </link>, </u>, <sprite name="DefenseDown">, <color=#e30000>, <link="DefenseDown">, <sprite name="AttackDmgUp">, <link="AttackDmgUp">, \n
   EN: Turn Start: Gain 2 <sprite name="Enhancement"><color=#f8c200><u><link="Enhancement">Attack Power Up</color></link></u> and 6 <sprite name="DefenseDown"><color=#e30000><u><link="DefenseDown">Defense Level Down</color></link></u>. Gain <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Damage Up</color></link></u> based on the amount of damage taken last turn (1 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Damage Up</color></link></u> for every 3% of Max HP lost)
   PL: Początek Tury: zyskaj 2 <sprite name="Enhancement"><color=#f8c200><u><link="Enhancement">Wzrost Mocy Ataku</link></u></color> i 6 <sprite name="DefenseDown"><color=#e30000><u><link="DefenseDown">Spadek Poziomu Obrony</link></u></color> oraz zyskaj <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Wzrost Obrażeń</link></u></color> zależnie od obrażeń otrzymanych w poprzedniej turze\n(1 <sprite name="AttackDmgUp"><color=#f8c200><u><link="AttackDmgUp">Wzrost Obrażeń</link></u></color> za każde 3% Maks. PŻ)
49. [Poczytalność i Panika [1015] — nazwa Paniki] 하얀 공황
   źródło: PanicInfo.json :: dataList[id=1015].panicName
   limit: do 40 znaków
   EN: Pallid Panic
   PL: Blada Panika
50. [Poczytalność i Panika [1015] — efekt niskiego morale] [MentalSystemResultDecrease_Typo] +2
   źródło: PanicInfo.json :: dataList[id=1015].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MentalSystemResultDecrease_Typo]
   znaczenie tagów: [MentalSystemResultDecrease_Typo] = 정신력 감소 효율 / SP Loss Efficiency
   EN: [MentalSystemResultDecrease_Typo] +2
   PL: [MentalSystemResultDecrease_Typo] +2
51. [Poczytalność i Panika [1015] — efekt Paniki] 매 턴 종료 시 다음 턴에 <sprite name="Binding"><color=#f8c200><u><link="Binding">속박</color></link></u> 2를 얻음.\n자신이 사용하는 모든 코인이 뒷면이 나옴.
   źródło: PanicInfo.json :: dataList[id=1015].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Binding">, <color=#f8c200>, <u>, <link="Binding">, </color>, </link>, </u>, \n
   EN: Every Turn End: Gain 2 <sprite name="Binding"><color=#f8c200><u><link="Binding">Bind</color></link></u>.\nEvery Coin this unit flips lands on tails.
   PL: Co Koniec Tury: w następnej turze zyskaj 2 <sprite name="Binding"><color=#f8c200><u><link="Binding">Spętanie</link></u></color>.\nWszystkie rzucane przez tę jednostkę Monety wypadają Rewersem.
52. [Poczytalność i Panika [1016] — nazwa Paniki] 원한
   źródło: PanicInfo.json :: dataList[id=1016].panicName
   limit: do 40 znaków
   EN: Resentment
   PL: Zadrza
53. [Poczytalność i Panika [1016] — efekt niskiego morale] 턴 시작 시 [AttackDmgUp] 2, [DefenseDown] 3을 얻음
   źródło: PanicInfo.json :: dataList[id=1016].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp], [DefenseDown]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: gain 2 [AttackDmgUp] and 3 [DefenseDown]
   PL: Początek Tury: zyskaj 2 [AttackDmgUp] i 3 [DefenseDown]
54. [Poczytalność i Panika [1016] — efekt Paniki] 턴 시작 시 [Enhancement] 1, [DefenseDown] 5를 얻음
   źródło: PanicInfo.json :: dataList[id=1016].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [DefenseDown]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: gain 1 [Enhancement] and 5 [DefenseDown]
   PL: Początek Tury: zyskaj 1 [Enhancement] i 5 [DefenseDown]
55. [Poczytalność i Panika [1026] — nazwa Paniki] 파탄
   źródło: PanicInfo.json :: dataList[id=1026].panicName
   limit: do 40 znaków
   EN: Ruin
   PL: Zatrata
56. [Poczytalność i Panika [1026] — efekt niskiego morale] 매 턴 종료 시 [Sinking] 3 얻음, 자신의 합 위력 -1
   źródło: PanicInfo.json :: dataList[id=1026].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Gain 3 [Sinking] at every Turn End; Clash Power -1
   PL: Co Koniec Tury: zyskaj 3 [Sinking]; Moc Starcia -1
57. [Poczytalność i Panika [1026] — efekt Paniki] 매 턴 종료 시 [Sinking] 5 얻음, [Sinking] 횟수 3 증가, 자신의 합 위력 -2
   źródło: PanicInfo.json :: dataList[id=1026].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Gain 5 [Sinking] and +3 [Sinking] Count at every Turn End; Clash Power -2
   PL: Co Koniec Tury: zyskaj 5 [Sinking] i +3 Licznika [Sinking]; Moc Starcia -2
58. [Poczytalność i Panika [9994] — nazwa Paniki] 사랑과 증오
   źródło: PanicInfo.json :: dataList[id=9994].panicName
   limit: do 40 znaków
   EN: Love and Hate
   PL: Miłość i Nienawiść
59. [Poczytalność i Panika [9994] — efekt Paniki] 한 턴 동안 행동하지 않음
   źródło: PanicInfo.json :: dataList[id=9994].panicDescription
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [Poczytalność i Panika [1065] — nazwa Paniki] 파쇄흔
   źródło: PanicInfo.json :: dataList[id=1065].panicName
   limit: do 40 znaków
   EN: Shattermark
   PL: Ślad Roztrzaskania
61. [Poczytalność i Panika [1065] — efekt niskiego morale] 자신의 합 위력 -1, 방어 레벨 -2
   źródło: PanicInfo.json :: dataList[id=1065].lowMoraleDescription
   limit: do 120 znaków
   EN: Clash Power -1, Defense Level -2
   PL: Moc Starcia -1, Poziom Obrony -2
62. [Poczytalność i Panika [1065] — efekt Paniki] 자신의 합 위력 -2, 방어 레벨 -3
   źródło: PanicInfo.json :: dataList[id=1065].panicDescription
   limit: do 120 znaków
   EN: Clash Power -2, Defense Level -3
   PL: Moc Starcia -2, Poziom Obrony -3
63. [Poczytalność i Panika [1085] — nazwa Paniki] 푸른 모래
   źródło: PanicInfo.json :: dataList[id=1085].panicName
   limit: do 40 znaków
   EN: Blue Sand
   PL: Błękitny Piasek
64. [Poczytalność i Panika [1085] — efekt niskiego morale] 자신의 합 위력 -1\n속도 최솟값, 최댓값 -1
   źródło: PanicInfo.json :: dataList[id=1085].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clash Power -1\nMin & Max Speed -1
   PL: Moc Starcia -1\nMin. i Maks. Szybkość -1
65. [Poczytalność i Panika [1085] — efekt Paniki] 자신의 합 위력 -2\n속도 최솟값, 최댓값 -1
   źródło: PanicInfo.json :: dataList[id=1085].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clash Power -2\nMin & Max Speed -1
   PL: Moc Starcia -2\nMin. i Maks. Szybkość -1
66. [Poczytalność i Panika [1086] — nazwa Paniki] 현혹
   źródło: PanicInfo.json :: dataList[id=1086].panicName
   limit: do 40 znaków
   EN: Dazzle
   PL: Olśnienie
67. [Poczytalność i Panika [1086] — efekt niskiego morale] 턴 종료 시 다음 턴에 [Binding] 1, [AttackDown] 2 얻음
   źródło: PanicInfo.json :: dataList[id=1086].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding], [AttackDown]
   znaczenie tagów: [Binding] = 속박 / Bind; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: Turn End: Gain 1 [Binding] and 2 [AttackDown] next turn
   PL: Koniec Tury: zyskaj 1 [Binding] i 2 [AttackDown] w następnej turze
68. [Poczytalność i Panika [1086] — efekt Paniki] 턴 종료 시 다음 턴에 [Binding] 1, [AttackDown] 4 얻음
   źródło: PanicInfo.json :: dataList[id=1086].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding], [AttackDown]
   znaczenie tagów: [Binding] = 속박 / Bind; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: Turn End: Gain 1 [Binding] and 4 [AttackDown] next turn
   PL: Koniec Tury: zyskaj 1 [Binding] i 4 [AttackDown] w następnej turze
69. [Poczytalność i Panika [1087] — nazwa Paniki] 고독
   źródło: PanicInfo.json :: dataList[id=1087].panicName
   limit: do 40 znaków
   EN: Solitude
   PL: Samotność
70. [Poczytalność i Panika [1087] — efekt niskiego morale] 턴 종료시 [Sinking] 횟수 2 증가
   źródło: PanicInfo.json :: dataList[id=1087].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Turn End: Gain +2 [Sinking] Count
   PL: Koniec Tury: zyskaj +2 Licznika [Sinking]
71. [Poczytalność i Panika [1087] — efekt Paniki] 턴 종료시 [Sinking] 횟수 3 증가
   źródło: PanicInfo.json :: dataList[id=1087].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Turn End: Gain +3 [Sinking] Count
   PL: Koniec Tury: zyskaj +3 Licznika [Sinking]
72. [Poczytalność i Panika [1091] — nazwa Paniki] 굴절된 애증
   źródło: PanicInfo.json :: dataList[id=1091].panicName
   limit: do 50 znaków
   EN: Refracted Affection and Resentment
   PL: Załamana Miłość i Urąganie
73. [Poczytalność i Panika [1091] — efekt niskiego morale] 가하는 피해량과 받는 피해량 +10%
   źródło: PanicInfo.json :: dataList[id=1091].lowMoraleDescription
   limit: do 120 znaków
   EN: Deal and take +10% damage
   PL: Zadawane i otrzymywane obrażenia +10%
74. [Poczytalność i Panika [1091] — efekt Paniki] 가하는 피해량과 받는 피해량 +20%
   źródło: PanicInfo.json :: dataList[id=1091].panicDescription
   limit: do 120 znaków
   EN: Deal and take +20% damage
   PL: Zadawane i otrzymywane obrażenia +20%
75. [Poczytalność i Panika [1097] — nazwa Paniki] 모조된 아비
   źródło: PanicInfo.json :: dataList[id=1097].panicName
   limit: do 40 znaków
   EN: Imitation of a Father
   PL: Imitacja Ojca
76. [Poczytalność i Panika [1097] — efekt niskiego morale] - 턴 시작 시, [Combustion] 5, [Laceration] 5 얻음
   źródło: PanicInfo.json :: dataList[id=1097].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Laceration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: - Turn Start: Gain 5 [Combustion] and 5 [Laceration]
   PL: - Początek Tury: zyskaj 5 [Combustion] i 5 [Laceration]
77. [Poczytalność i Panika [1097] — efekt Paniki] - 턴 시작 시, [Combustion] 5, [Combustion] 횟수 3, [Laceration] 5, [Laceration] 횟수 3 얻음
   źródło: PanicInfo.json :: dataList[id=1097].panicDescription
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Laceration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: - Turn Start: Gain 5 [Combustion], +3 [Combustion] Count, 5 [Laceration], and +3 [Laceration] Count
   PL: - Początek Tury: zyskaj 5 [Combustion], +3 Licznika [Combustion], 5 [Laceration] i +3 Licznika [Laceration]

## Interfejs i ustawienia: BattleUIText
- plik gry: `BattleUIText.json`

78. [Interfejs i ustawienia [battle_battleunit_guard] — tekst] 방어
   źródło: BattleUIText.json :: dataList[id=battle_battleunit_guard].content
   limit: do 120 znaków
   EN: Guard
   PL: Garda
79. [Interfejs i ustawienia [popup_message_ego_seat_lack] — tekst] 에고를 사용할 수 없는 상태입니다. 자리를 확인해주세요.
   źródło: BattleUIText.json :: dataList[id=popup_message_ego_seat_lack].content
   limit: do 120 znaków
   EN: Cannot use this E.G.O. Please check available space.
   PL: Nie można użyć tego E.G.O. Sprawdź dostępne miejsce.
80. [Interfejs i ustawienia [popup_message_ego_resources_lack] — tekst] 에고를 사용할 수 없는 상태입니다. 문양을 확인해주세요.
   źródło: BattleUIText.json :: dataList[id=popup_message_ego_resources_lack].content
   limit: do 120 znaków
   EN: Cannot use this E.G.O. Please check your resources.
   PL: Nie można użyć tego E.G.O. Sprawdź posiadane zasoby.
81. [Interfejs i ustawienia [option_title] — tekst] 설정
   źródło: BattleUIText.json :: dataList[id=option_title].content
   limit: do 120 znaków
   EN: Settings
   PL: Ustawienia
82. [Interfejs i ustawienia [option_btn_exit] — tekst] 스테이지 나가기
   źródło: BattleUIText.json :: dataList[id=option_btn_exit].content
   limit: do 120 znaków
   EN: Exit Stage
   PL: Opuść Etap
83. [Interfejs i ustawienia [option_btn_statistical] — tekst] 전투 통계
   źródło: BattleUIText.json :: dataList[id=option_btn_statistical].content
   limit: do 120 znaków
   EN: Battle Data
   PL: Statystyki Walki
84. [Interfejs i ustawienia [creature_destroy_notice] — tekst] 부위파괴
   źródło: BattleUIText.json :: dataList[id=creature_destroy_notice].content
   limit: do 120 znaków
   EN: Part Broken
   PL: Część Zniszczona
85. [Interfejs i ustawienia [oneside_attack] — tekst] 일방공격
   źródło: BattleUIText.json :: dataList[id=oneside_attack].content
   limit: do 120 znaków
   EN: Unopposed
   PL: Jednostronny
86. [Interfejs i ustawienia [guard] — tekst] 방어
   źródło: BattleUIText.json :: dataList[id=guard].content
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Interfejs i ustawienia [power] — tekst] 위력
   źródło: BattleUIText.json :: dataList[id=power].content
   limit: do 120 znaków
   EN: Potency
   PL: Siła
88. [Interfejs i ustawienia [require] — tekst] 필요
   źródło: BattleUIText.json :: dataList[id=require].content
   limit: do 120 znaków
   EN: Req.
   PL: Wym.
89. [Interfejs i ustawienia [battle_log_atk_hp] — tekst] {0}가(이) {1}에게 {2}의 피해!
   źródło: BattleUIText.json :: dataList[id=battle_log_atk_hp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0} deals {2} damage to {1}!
   PL: {0} zadaje {2} obrażeń celowi {1}!
90. [Interfejs i ustawienia [battle_log_atk_mp] — tekst] {0}가(이) {1}에게 {2}의 정신력 피해!
   źródło: BattleUIText.json :: dataList[id=battle_log_atk_mp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0} deals {2} damage to {1}’s sanity!
   PL: {0} zadaje {2} obrażeń Poczytalności celowi {1}!
91. [Interfejs i ustawienia [battle_log_recover_hp] — tekst] {0}가(이) {1}을 사용하여 체력{2} 회복
   źródło: BattleUIText.json :: dataList[id=battle_log_recover_hp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0} healed {2} HP using {1}.
   PL: {0} odzyskuje {2} PŻ dzięki {1}.
92. [Interfejs i ustawienia [battle_log_guard] — tekst] {0} 방어 사용
   źródło: BattleUIText.json :: dataList[id=battle_log_guard].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} raised their guard.
   PL: {0} używa Gardy.
93. [Interfejs i ustawienia [battle_log_buf_to_other] — tekst] {0}가(이) {1}에게 {2}를(을) {3} 부여
   źródło: BattleUIText.json :: dataList[id=battle_log_buf_to_other].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: {0} applied {3} {2} to {1}.
   PL: {0} nakłada {3} {2} na {1}.
94. [Interfejs i ustawienia [battle_log_buf_to_self] — tekst] {0}가(이) 자신에게 {1}를(을) {2} 부여
   źródło: BattleUIText.json :: dataList[id=battle_log_buf_to_self].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0} applied {2} {1} to themself.
   PL: {0} nakłada na siebie {2} {1}.
95. [Interfejs i ustawienia [battle_log_use_ego] — tekst] {0}의 E.G.O:{1} 각성!!
   źródło: BattleUIText.json :: dataList[id=battle_log_use_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} awakens {1}!!
   PL: {0} — Przebudzenie E.G.O: {1}!!
96. [Interfejs i ustawienia [battle_log_use_ego_corrosion] — tekst] {0}의 E.G.O:{1} 침식!!
   źródło: BattleUIText.json :: dataList[id=battle_log_use_ego_corrosion].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {1} corrodes {0}!!
   PL: {0} — Korozja E.G.O: {1}!!
97. [Interfejs i ustawienia [battle_log_personality_corrosion] — tekst] {0}의 정신붕괴!!
   źródło: BattleUIText.json :: dataList[id=battle_log_personality_corrosion].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} has a breakdown!!
   PL: {0} ulega załamaniu psychicznemu!!
98. [Interfejs i ustawienia [battle_log_low_morale] — tekst] {0}의 사기 저하!
   źródło: BattleUIText.json :: dataList[id=battle_log_low_morale].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}’s morale is low!
   PL: {0} ma Niskie Morale!
99. [Interfejs i ustawienia [battle_log_panic] — tekst] {0}의 패닉!!
   źródło: BattleUIText.json :: dataList[id=battle_log_panic].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} is panicking!!
   PL: {0} wpada w Panikę!!
100. [Interfejs i ustawienia [choice_result_success] — tekst] 판정 성공
   źródło: BattleUIText.json :: dataList[id=choice_result_success].content
   limit: do 120 znaków
   EN: Check Passed
   PL: Test Zdany
101. [Interfejs i ustawienia [choice_result_fail] — tekst] 판정 실패
   źródło: BattleUIText.json :: dataList[id=choice_result_fail].content
   limit: do 120 znaków
   EN: Check Failed
   PL: Test Nieudany
102. [Interfejs i ustawienia [choice_result_skip] — tekst] 판정 넘김
   źródło: BattleUIText.json :: dataList[id=choice_result_skip].content
   limit: do 120 znaków
   EN: Check Skipped
   PL: Test Pominięty
103. [Interfejs i ustawienia [info_button_detailinfo] — tekst] 상세 정보
   źródło: BattleUIText.json :: dataList[id=info_button_detailinfo].content
   limit: do 120 znaków
   EN: Details
   PL: Szczegóły
104. [Interfejs i ustawienia [info_button_skill] — tekst] 스킬
   źródło: BattleUIText.json :: dataList[id=info_button_skill].content
   limit: do 120 znaków
   EN: Skill
   PL: Umiejętność
105. [Interfejs i ustawienia [info_button_awakenskill] — tekst] 각성 스킬
   źródło: BattleUIText.json :: dataList[id=info_button_awakenskill].content
   limit: do 120 znaków
   EN: Awakening
   PL: Przebudzenie
106. [Interfejs i ustawienia [info_button_erosionskill] — tekst] 침식 스킬
   źródło: BattleUIText.json :: dataList[id=info_button_erosionskill].content
   limit: do 120 znaków
   EN: Corrosion
   PL: Korozja
107. [Interfejs i ustawienia [resonance] — tekst] 공명
   źródło: BattleUIText.json :: dataList[id=resonance].content
   limit: do 120 znaków
   EN: Res
   PL: Rez.
108. [Interfejs i ustawienia [perfect_resonance] — tekst] 완전공명
   źródło: BattleUIText.json :: dataList[id=perfect_resonance].content
   limit: do 120 znaków
   EN: A-Res
   PL: Rez. Abs.
109. [Interfejs i ustawienia [break] — tekst] 흐트러짐
   źródło: BattleUIText.json :: dataList[id=break].content
   limit: do 120 znaków
   EN: STAGGER
   PL: OSZOŁOMIENIE
110. [Interfejs i ustawienia [mental_break] — tekst] 정신붕괴
   źródło: BattleUIText.json :: dataList[id=mental_break].content
   limit: do 120 znaków
   EN: BREAKDOWN
   PL: ZAŁAMANIE
111. [Interfejs i ustawienia [low_morale] — tekst] 사기저하
   źródło: BattleUIText.json :: dataList[id=low_morale].content
   limit: do 120 znaków
   EN: Low Morale
   PL: Niskie Morale
112. [Interfejs i ustawienia [panic] — tekst] 패닉
   źródło: BattleUIText.json :: dataList[id=panic].content
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Interfejs i ustawienia [status] — tekst] 스테이터스
   źródło: BattleUIText.json :: dataList[id=status].content
   limit: do 120 znaków
   EN: Status
   PL: Status
114. [Interfejs i ustawienia [status_abnormal] — tekst] 상태이상
   źródło: BattleUIText.json :: dataList[id=status_abnormal].content
   limit: do 120 znaków
   EN: Effects
   PL: Efekty
115. [Interfejs i ustawienia [immunity_information] — tekst] 내성 정보
   źródło: BattleUIText.json :: dataList[id=immunity_information].content
   limit: do 120 znaków
   EN: Resistances
   PL: Odporności
116. [Interfejs i ustawienia [awaken_ego_skill] — tekst] 각성 스킬
   źródło: BattleUIText.json :: dataList[id=awaken_ego_skill].content
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Interfejs i ustawienia [erosion_ego_skill] — tekst] 침식 스킬
   źródło: BattleUIText.json :: dataList[id=erosion_ego_skill].content
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Interfejs i ustawienia [turnplace_test_name] — tekst] 남겨진 로보토미 지부 어딘가
   źródło: BattleUIText.json :: dataList[id=turnplace_test_name].content
   limit: do 120 znaków
   EN: An Abandoned LC Branch
   PL: Opuszczony Oddział Lobotomy Corp.
119. [Interfejs i ustawienia [death] — tekst] 사망
   źródło: BattleUIText.json :: dataList[id=death].content
   limit: do 120 znaków
   EN: DEAD
   PL: MARTWY
120. [Interfejs i ustawienia [slash] — tekst] 참격
   źródło: BattleUIText.json :: dataList[id=slash].content
   limit: do 120 znaków
   EN: Slash
   PL: Cięcie
121. [Interfejs i ustawienia [penetrate] — tekst] 관통
   źródło: BattleUIText.json :: dataList[id=penetrate].content
   limit: do 120 znaków
   EN: Pierce
   PL: Kłucie
122. [Interfejs i ustawienia [hit] — tekst] 타격
   źródło: BattleUIText.json :: dataList[id=hit].content
   limit: do 120 znaków
   EN: Blunt
   PL: Obuch
123. [Interfejs i ustawienia [action_disable] — tekst] 행동불가
   źródło: BattleUIText.json :: dataList[id=action_disable].content
   limit: do 120 znaków
   EN: Immobile
   PL: Niezdatny do Ruchu
124. [Interfejs i ustawienia [ab_event_select_character] — tekst] 수감자 선택
   źródło: BattleUIText.json :: dataList[id=ab_event_select_character].content
   limit: do 120 znaków
   EN: Select Sinner
   PL: Wybierz Grzesznika
125. [Interfejs i ustawienia [ab_event_select_desc] — tekst] 선택 내용
   źródło: BattleUIText.json :: dataList[id=ab_event_select_desc].content
   limit: do 120 znaków
   EN: Info
   PL: Wybór
126. [Interfejs i ustawienia [ab_event_rate] — tekst] 성공 확률
   źródło: BattleUIText.json :: dataList[id=ab_event_rate].content
   limit: do 120 znaków
   EN: Success Rate
   PL: Szansa Powodzenia
127. [Interfejs i ustawienia [formet_event_rate] — tekst] 성공 확률 : {0}
   źródło: BattleUIText.json :: dataList[id=formet_event_rate].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Success Rate: {0}
   PL: Szansa Powodzenia: {0}
128. [Interfejs i ustawienia [ab_event_decision] — tekst] 판정 시작
   źródło: BattleUIText.json :: dataList[id=ab_event_decision].content
   limit: do 120 znaków
   EN: Commence
   PL: Rozpocznij Test
129. [Interfejs i ustawienia [ab_event_need] — tekst] 필요
   źródło: BattleUIText.json :: dataList[id=ab_event_need].content
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Interfejs i ustawienia [ab_battle_resume] — tekst] 전투 재개
   źródło: BattleUIText.json :: dataList[id=ab_battle_resume].content
   limit: do 120 znaków
   EN: Resume Battle
   PL: Wznów Walkę
131. [Interfejs i ustawienia [info_button_choice_log] — tekst] 선택지 로그
   źródło: BattleUIText.json :: dataList[id=info_button_choice_log].content
   limit: do 120 znaków
   EN: Decision Log
   PL: Dziennik Wyborów
132. [Interfejs i ustawienia [info_button_story] — tekst] 스토리
   źródło: BattleUIText.json :: dataList[id=info_button_story].content
   limit: do 120 znaków
   EN: Story
   PL: Historia
133. [Interfejs i ustawienia [info_button_ego] — tekst] E.G.O
   źródło: BattleUIText.json :: dataList[id=info_button_ego].content
   limit: do 120 znaków
   EN: E.G.O
   PL: E.G.O
134. [Interfejs i ustawienia [dungeon_encounter_start] — tekst] 시작점
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_start].content
   limit: do 120 znaków
   EN: Start
   PL: Start
135. [Interfejs i ustawienia [dungeon_encounter_battle] — tekst] 일반 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_battle].content
   limit: do 120 znaków
   EN: Regular Encounter
   PL: Zwykłe Starcie
136. [Interfejs i ustawienia [dungeon_encounter_ab_battle] — tekst] 집중 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_ab_battle].content
   limit: do 120 znaków
   EN: Focused Encounter
   PL: Starcie Skupione
137. [Interfejs i ustawienia [dungeon_encounter_hard_battle] — tekst] 위험 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_hard_battle].content
   limit: do 120 znaków
   EN: Risky Encounter
   PL: Ryzykowne Starcie
138. [Interfejs i ustawienia [dungeon_encounter_event] — tekst] 이벤트
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_event].content
   limit: do 120 znaków
   EN: Event
   PL: Zdarzenie
139. [Interfejs i ustawienia [dungeon_encounter_save] — tekst] 세이브 포인트
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_save].content
   limit: do 120 znaków
   EN: Checkpoint
   PL: Punkt Kontrolny
140. [Interfejs i ustawienia [dungeon_encounter_boss] — tekst] 층 보스
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_boss].content
   limit: do 120 znaków
   EN: Floor Boss
   PL: Boss Piętra
141. [Interfejs i ustawienia [bottom_winrate] — tekst] 승률
   źródło: BattleUIText.json :: dataList[id=bottom_winrate].content
   limit: do 120 znaków
   EN: Win Rate
   PL: Szansa
142. [Interfejs i ustawienia [bottom_dmg] — tekst] 피해량
   źródło: BattleUIText.json :: dataList[id=bottom_dmg].content
   limit: do 120 znaków
   EN: Damage
   PL: Obrażenia
143. [Interfejs i ustawienia [ab_event_next] — tekst] 다음으로
   źródło: BattleUIText.json :: dataList[id=ab_event_next].content
   limit: do 120 znaków
   EN: Proceed
   PL: Dalej
144. [Interfejs i ustawienia [explanatory] — tekst] 범례
   źródło: BattleUIText.json :: dataList[id=explanatory].content
   limit: do 120 znaków
   EN: Legend
   PL: Legenda
145. [Interfejs i ustawienia [get_ego_gift] — tekst] E.G.O 기프트 획득
   źródło: BattleUIText.json :: dataList[id=get_ego_gift].content
   limit: do 120 znaków
   EN: E.G.O Gift GET
   PL: Zdobyto Dar E.G.O
146. [Interfejs i ustawienia [get_ego_gift_desc] — tekst] E.G.O 기프트를 획득했습니다.
   źródło: BattleUIText.json :: dataList[id=get_ego_gift_desc].content
   limit: do 120 znaków
   EN: E.G.O Gift GET!
   PL: Zdobyto Dar E.G.O!
147. [Interfejs i ustawienia [selection] — tekst] 선택지
   źródło: BattleUIText.json :: dataList[id=selection].content
   limit: do 120 znaków
   EN: Choices
   PL: Opcje
148. [Interfejs i ustawienia [result] — tekst] 결과
   źródło: BattleUIText.json :: dataList[id=result].content
   limit: do 120 znaków
   EN: Result
   PL: Wynik
149. [Interfejs i ustawienia [choice_total_rate] — tekst] 총 성공 확률
   źródło: BattleUIText.json :: dataList[id=choice_total_rate].content
   limit: do 120 znaków
   EN: Total Success Rate
   PL: Łączna Szansa Powodzenia
150. [Interfejs i ustawienia [enter] — tekst] 입장
   źródło: BattleUIText.json :: dataList[id=enter].content
   limit: do 120 znaków
   EN: Enter
   PL: Wejdź
151. [Interfejs i ustawienia [recommend_level] — tekst] 추천 레벨
   źródło: BattleUIText.json :: dataList[id=recommend_level].content
   limit: do 120 znaków
   EN: Ideal LVL
   PL: Zalec. Poz.
152. [Interfejs i ustawienia [enemy_info] — tekst] 적 정보
   źródło: BattleUIText.json :: dataList[id=enemy_info].content
   limit: do 120 znaków
   EN: Enemy Info
   PL: Dane Wrogów
153. [Interfejs i ustawienia [enter_clear_requirement] — tekst] EX 클리어 조건
   źródło: BattleUIText.json :: dataList[id=enter_clear_requirement].content
   limit: do 120 znaków
   EN: Extra Objective
   PL: Warunek EX
154. [Interfejs i ustawienia [choice_event_resume] — tekst] 돌아가기
   źródło: BattleUIText.json :: dataList[id=choice_event_resume].content
   limit: do 120 znaków
   EN: Continue
   PL: Wróć
155. [Interfejs i ustawienia [crime_state_judgment] — tekst] {0} 판정
   źródło: BattleUIText.json :: dataList[id=crime_state_judgment].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Check
   PL: Test: {0}
156. [Interfejs i ustawienia [choice_personality] — tekst] 판정을 진행할 인격을 선택하세요
   źródło: BattleUIText.json :: dataList[id=choice_personality].content
   limit: do 120 znaków
   EN: Choose a character to perform the check with:
   PL: Wybierz Tożsamość, która wykona test:
157. [Interfejs i ustawienia [success_result] — tekst] 성공 값
   źródło: BattleUIText.json :: dataList[id=success_result].content
   limit: do 120 znaków
   EN: Threshold
   PL: Próg Sukcesu
158. [Interfejs i ustawienia [expectation_result] — tekst] 예상 값
   źródło: BattleUIText.json :: dataList[id=expectation_result].content
   limit: do 120 znaków
   EN: Predicted
   PL: Prognoza
159. [Interfejs i ustawienia [outcome_result] — tekst] 결과 값
   źródło: BattleUIText.json :: dataList[id=outcome_result].content
   limit: do 120 znaków
   EN: Outcome
   PL: Wynik Końcowy
160. [Interfejs i ustawienia [choice_event_percent] — tekst] 예상 확률
   źródło: BattleUIText.json :: dataList[id=choice_event_percent].content
   limit: do 120 znaków
   EN: Odds
   PL: Szansa
161. [Interfejs i ustawienia [skill_expectition_value] — tekst] 스킬 예상 값 {0}-{1}
   źródło: BattleUIText.json :: dataList[id=skill_expectition_value].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Predicted Range: {0}-{1}
   PL: Przewidywany zakres: {0}-{1}
162. [Interfejs i ustawienia [skill_expectition_or_value] — tekst] 스킬 예상 값 {0}or{1}
   źródło: BattleUIText.json :: dataList[id=skill_expectition_or_value].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Predicted Value: {0} / {1}
   PL: Przewidywana wartość: {0} / {1}
163. [Interfejs i ustawienia [skill_correction_value] — tekst] {0} 보정 값 {1}
   źródło: BattleUIText.json :: dataList[id=skill_correction_value].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} Modifier: {1}
   PL: Modyfikator ({0}): {1}
164. [Interfejs i ustawienia [correction_based_on_association] — tekst] {0} 소속 보정 값 {1}(, )
   źródło: BattleUIText.json :: dataList[id=correction_based_on_association].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} Faction Modifier: {1}(, )
   PL: Modyfikator przynależności ({0}): {1}(, )
165. [Interfejs i ustawienia [action_choice_event_result_example_battle] — tekst] 전투 발생
   źródło: BattleUIText.json :: dataList[id=action_choice_event_result_example_battle].content
   limit: do 120 znaków
   EN: Combat Encounter
   PL: Wybuch Walki
166. [Interfejs i ustawienia [action_choice_event_result_example_event] — tekst] 이벤트
   źródło: BattleUIText.json :: dataList[id=action_choice_event_result_example_event].content
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Interfejs i ustawienia [action_choice_event_result_example_resume] — tekst] 돌아가기
   źródło: BattleUIText.json :: dataList[id=action_choice_event_result_example_resume].content
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Interfejs i ustawienia [areaatk_attack] — tekst] 광역 스킬
   źródło: BattleUIText.json :: dataList[id=areaatk_attack].content
   limit: do 120 znaków
   EN: AoE Skills
   PL: Umiej. Obszarowe
169. [Interfejs i ustawienia [enter_battle] — tekst] 전투 시작
   źródło: BattleUIText.json :: dataList[id=enter_battle].content
   limit: do 120 znaków
   EN: Commence Battle
   PL: Rozpocznij Walkę
170. [Interfejs i ustawienia [choice_event_five_percent] — tekst] 5% 확률로 성공
   źródło: BattleUIText.json :: dataList[id=choice_event_five_percent].content
   limit: do 120 znaków
   EN: 5% Chance
   PL: 5% Szansy
171. [Interfejs i ustawienia [choice_event_five_percent_success] — tekst] 5% 확률로 판정 성공
   źródło: BattleUIText.json :: dataList[id=choice_event_five_percent_success].content
   limit: do 120 znaków
   EN: 5% Chance of Success
   PL: 5% Szansy na Sukces
172. [Interfejs i ustawienia [skillinfo_passivetitle] — tekst] 지속 효과
   źródło: BattleUIText.json :: dataList[id=skillinfo_passivetitle].content
   limit: do 120 znaków
   EN: Passives
   PL: Pasywki
173. [Interfejs i ustawienia [skillinfo_coinabilitytitle] — tekst] 스킬 효과
   źródło: BattleUIText.json :: dataList[id=skillinfo_coinabilitytitle].content
   limit: do 120 znaków
   EN: Skill Effects
   PL: Efekty Umiejętności
174. [Interfejs i ustawienia [dungeon_save_desc] — tekst] 세이브 포인트 도달.\n던전 진행 상황이 저장되었습니다.\n모든 수감자가 회복됩니다.
   źródło: BattleUIText.json :: dataList[id=dungeon_save_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Checkpoint reached.\nDungeon progress has been saved.\nAll Sinners have been healed.
   PL: Osiągnięto Punkt Kontrolny.\nPostępy w lochu zostały zapisane.\nWszyscy Grzesznicy zostali uleczeni.
175. [Interfejs i ustawienia [battle_battleunit_evade] — tekst] 회피
   źródło: BattleUIText.json :: dataList[id=battle_battleunit_evade].content
   limit: do 120 znaków
   EN: Evade
   PL: Unik
176. [Interfejs i ustawienia [battle_battleunit_counter] — tekst] 반격
   źródło: BattleUIText.json :: dataList[id=battle_battleunit_counter].content
   limit: do 120 znaków
   EN: Counter
   PL: Kontra
177. [Interfejs i ustawienia [battle_operation_defence] — tekst] 수비
   źródło: BattleUIText.json :: dataList[id=battle_operation_defence].content
   limit: do 120 znaków
   EN: Defense
   PL: Obrona
178. [Interfejs i ustawienia [battle_increase_mp] — tekst] 정신력 증가
   źródło: BattleUIText.json :: dataList[id=battle_increase_mp].content
   limit: do 120 znaków
   EN: Sanity Up
   PL: Wzrost Poczytalności
179. [Interfejs i ustawienia [battle_decrease_mp] — tekst] 정신력 감소
   źródło: BattleUIText.json :: dataList[id=battle_decrease_mp].content
   limit: do 120 znaków
   EN: Sanity Down
   PL: Spadek Poczytalności
180. [Interfejs i ustawienia [dungeon_encounter_type_start] — tekst] 시작
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_start].content
   limit: do 120 znaków
   EN: Start
   PL: Start
181. [Interfejs i ustawienia [dungeon_encounter_type_battle] — tekst] 일반 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_battle].content
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Interfejs i ustawienia [dungeon_encounter_type_ab_battle] — tekst] 집중 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_ab_battle].content
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Interfejs i ustawienia [dungeon_encounter_type_hard_battle] — tekst] 위험 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_hard_battle].content
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Interfejs i ustawienia [dungeon_encounter_type_event] — tekst] 이벤트
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_event].content
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Interfejs i ustawienia [dungeon_encounter_type_save] — tekst] 세이브룸
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_save].content
   limit: do 120 znaków
   EN: Saferoom
   PL: Bezpieczny Pokój
186. [Interfejs i ustawienia [dungeon_encounter_type_boss] — tekst] 보스 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_boss].content
   limit: do 120 znaków
   EN: Boss Encounter
   PL: Walka z Bossem
187. [Interfejs i ustawienia [battle_mp] — tekst] 정신력
   źródło: BattleUIText.json :: dataList[id=battle_mp].content
   limit: do 120 znaków
   EN: Sanity
   PL: Poczytalność
188. [Interfejs i ustawienia [abnormality_part_hp] — tekst] 부위 체력
   źródło: BattleUIText.json :: dataList[id=abnormality_part_hp].content
   limit: do 120 znaków
   EN: Part HP
   PL: PŻ Części
189. [Interfejs i ustawienia [abnormality_research_level] — tekst] 관찰 단계
   źródło: BattleUIText.json :: dataList[id=abnormality_research_level].content
   limit: do 120 znaków
   EN: Obs. Level
   PL: Poz. Obserwacji
190. [Interfejs i ustawienia [abnormality_no_research_level] — tekst] 관찰 단계 없음
   źródło: BattleUIText.json :: dataList[id=abnormality_no_research_level].content
   limit: do 120 znaków
   EN: Lacking Data
   PL: Brak Danych
191. [Interfejs i ustawienia [Insufficient_conditions] — tekst] 조건 불충족
   źródło: BattleUIText.json :: dataList[id=Insufficient_conditions].content
   limit: do 120 znaków
   EN: Conditions Unmet
   PL: Warunki Niespełnione
192. [Interfejs i ustawienia [skillinfo_keyword] — tekst] 키워드
   źródło: BattleUIText.json :: dataList[id=skillinfo_keyword].content
   limit: do 120 znaków
   EN: Keywords
   PL: Słowa Kluczowe
193. [Interfejs i ustawienia [ability_turn] — tekst] 횟수
   źródło: BattleUIText.json :: dataList[id=ability_turn].content
   limit: do 120 znaków
   EN: Count
   PL: Licznik
194. [Interfejs i ustawienia [ego_erosion] — tekst] E.G.O 침식
   źródło: BattleUIText.json :: dataList[id=ego_erosion].content
   limit: do 120 znaków
   EN: E.G.O Corrosion
   PL: Korozja E.G.O
195. [Interfejs i ustawienia [continuous_turn] — tekst] 지속 턴
   źródło: BattleUIText.json :: dataList[id=continuous_turn].content
   limit: do 120 znaków
   EN: Turns
   PL: Tury
196. [Interfejs i ustawienia [status_buff_list] — tekst] 효과 목록
   źródło: BattleUIText.json :: dataList[id=status_buff_list].content
   limit: do 120 znaków
   EN: Effects
   PL: Lista Efektów
197. [Interfejs i ustawienia [stack] — tekst] 스택
   źródło: BattleUIText.json :: dataList[id=stack].content
   limit: do 120 znaków
   EN: Stack
   PL: Ładunki
198. [Interfejs i ustawienia [slash_resistance] — tekst] 참격 내성
   źródło: BattleUIText.json :: dataList[id=slash_resistance].content
   limit: do 120 znaków
   EN: Slash Res.
   PL: Odp. na Cięcie
199. [Interfejs i ustawienia [penetrate_resistance] — tekst] 관통 내성
   źródło: BattleUIText.json :: dataList[id=penetrate_resistance].content
   limit: do 120 znaków
   EN: Pierce Res.
   PL: Odp. na Kłucie
200. [Interfejs i ustawienia [hit_resistance] — tekst] 타격 내성
   źródło: BattleUIText.json :: dataList[id=hit_resistance].content
   limit: do 120 znaków
   EN: Blunt Res.
   PL: Odp. na Obuch
201. [Interfejs i ustawienia [Lack_Buff] — tekst] !{0} 부족!
   źródło: BattleUIText.json :: dataList[id=Lack_Buff].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: No {0}!
   PL: Brak: {0}!
202. [Interfejs i ustawienia [received_the_golden_bough] — tekst] 황금가지 수복
   źródło: BattleUIText.json :: dataList[id=received_the_golden_bough].content
   limit: do 120 znaków
   EN: Golden Bough Recovered
   PL: Odzyskano Złotą Gałąź
203. [Interfejs i ustawienia [destroyable] — tekst] 파괴 가능
   źródło: BattleUIText.json :: dataList[id=destroyable].content
   limit: do 120 znaków
   EN: Destructible
   PL: Zniszczalna
204. [Interfejs i ustawienia [resumption] — tekst] 게임 재개
   źródło: BattleUIText.json :: dataList[id=resumption].content
   limit: do 120 znaków
   EN: Resume
   PL: Wznów Grę
205. [Interfejs i ustawienia [stage_GiveUp] — tekst] 스테이지 포기
   źródło: BattleUIText.json :: dataList[id=stage_GiveUp].content
   limit: do 120 znaków
   EN: Give Up
   PL: Poddaj Etap
206. [Interfejs i ustawienia [show_skillTool] — tekst] 스킬 툴 표시
   źródło: BattleUIText.json :: dataList[id=show_skillTool].content
   limit: do 120 znaków
   EN: Show Skill Tools
   PL: Pokaż Narzędzia Umiej.
207. [Interfejs i ustawienia [auto_coinToss] — tekst] 코인 토스 자동
   źródło: BattleUIText.json :: dataList[id=auto_coinToss].content
   limit: do 120 znaków
   EN: Auto Cointoss
   PL: Auto-rzut Monetą
208. [Interfejs i ustawienia [babayaga_alert] — tekst] {0}번의 기회가 남았어.
   źródło: BattleUIText.json :: dataList[id=babayaga_alert].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You have {0} chances left.
   PL: Pozostało ci szans: {0}.
209. [Interfejs i ustawienia [battle_operation_offset] — tekst] 상쇄
   źródło: BattleUIText.json :: dataList[id=battle_operation_offset].content
   limit: do 120 znaków
   EN: Offset
   PL: Zbicie
210. [Interfejs i ustawienia [oneside_defense] — tekst] 일방방어
   źródło: BattleUIText.json :: dataList[id=oneside_defense].content
   limit: do 120 znaków
   EN: One-sided Guard
   PL: Garda Jednostronna
211. [Interfejs i ustawienia [cantIdentify] — tekst] <color=#ff0000>[피아식별불가]</color>
   źródło: BattleUIText.json :: dataList[id=cantIdentify].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>
   EN: <color=#ff0000>[Indiscriminate]</color>
   PL: <color=#ff0000>[Bez Rozróżnienia]</color>
212. [Interfejs i ustawienia [popup_message_ego_irrevocable] — tekst] 이전 턴에 생성한 E.G.O 스킬은 취소할 수 없습니다.
   źródło: BattleUIText.json :: dataList[id=popup_message_ego_irrevocable].content
   limit: do 120 znaków
   EN: E.G.O Skills generated on previous turns cannot be canceled.
   PL: Nie można anulować umiejętności E.G.O wygenerowanych w poprzednich turach.
213. [Interfejs i ustawienia [stock] — tekst] 보유
   źródło: BattleUIText.json :: dataList[id=stock].content
   limit: do 120 znaków
   EN: Owned
   PL: Posiadane
214. [Interfejs i ustawienia [stable] — tekst] 안정
   źródło: BattleUIText.json :: dataList[id=stable].content
   limit: do 120 znaków
   EN: Stable
   PL: Stabilny
215. [Interfejs i ustawienia [un_stable] — tekst] 불안정
   źródło: BattleUIText.json :: dataList[id=un_stable].content
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Interfejs i ustawienia [vibration_explosion] — tekst] 진동 폭발!
   źródło: BattleUIText.json :: dataList[id=vibration_explosion].content
   limit: do 120 znaków
   EN: Tremor Burst!
   PL: Wyładowanie Wstrząsu!
217. [Interfejs i ustawienia [sinking_surge] — tekst] 침잠쇄도!
   źródło: BattleUIText.json :: dataList[id=sinking_surge].content
   limit: do 120 znaków
   EN: Sinking Deluge!
   PL: Potop Zatonięcia!
218. [Interfejs i ustawienia [targetSlotWeight] — tekst] 공격 가중치
   źródło: BattleUIText.json :: dataList[id=targetSlotWeight].content
   limit: do 120 znaków
   EN: Atk Weight
   PL: Waga Ataku
219. [Interfejs i ustawienia [EGO_ErodeProbability] — tekst] 침식확률
   źródło: BattleUIText.json :: dataList[id=EGO_ErodeProbability].content
   limit: do 120 znaków
   EN: To Corrode
   PL: Szansa Korozji
220. [Interfejs i ustawienia [EGOSelectUI_resources_lack] — tekst] 자원이 부족합니다.\n문양을 확인해 주세요.
   źródło: BattleUIText.json :: dataList[id=EGOSelectUI_resources_lack].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You lack sufficient resources.\nPlease check the symbols.
   PL: Niewystarczające zasoby.\nSprawdź posiadane symbole.
221. [Interfejs i ustawienia [EGOSelectUI_DetailInfo] — tekst] 상세 정보
   źródło: BattleUIText.json :: dataList[id=EGOSelectUI_DetailInfo].content
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Interfejs i ustawienia [ab_part_destroyable] — tekst] 파괴 가능
   źródło: BattleUIText.json :: dataList[id=ab_part_destroyable].content
   (powtórzenie elementu 203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Interfejs i ustawienia [ab_part_destroyable_and_can_vanish] — tekst] 파괴 및 적출 가능
   źródło: BattleUIText.json :: dataList[id=ab_part_destroyable_and_can_vanish].content
   limit: do 120 znaków
   EN: Destr. & Severable
   PL: Zniszcz. i Odcięcie
224. [Interfejs i ustawienia [ab_guidebook_view] — tekst] 도감 보기
   źródło: BattleUIText.json :: dataList[id=ab_guidebook_view].content
   limit: do 120 znaków
   EN: View Logs
   PL: Dziennik
225. [Interfejs i ustawienia [show_BattleAblityUI] — tekst] 전투 중 상세 정보 UI 표시
   źródło: BattleUIText.json :: dataList[id=show_BattleAblityUI].content
   limit: do 120 znaków
   EN: Display detailed info UI in Combat Phase
   PL: Pokaż szczegółowy interfejs w Fazie Walki
226. [Interfejs i ustawienia [Ahab_NotTarget_Onece] — tekst] 내가 진짜 노려야하는건…
   źródło: BattleUIText.json :: dataList[id=Ahab_NotTarget_Onece].content
   limit: do 120 znaków
   EN: Where my Harpoon must strike...
   PL: To, w co naprawdę muszę wymierzyć harpun…
227. [Interfejs i ustawienia [Ahab_NotTarget_Twice] — tekst] 늘 앞만 뚫어지게 바라봐야만하는게 아니야...
   źródło: BattleUIText.json :: dataList[id=Ahab_NotTarget_Twice].content
   limit: do 120 znaków
   EN: ... Sometimes, the answer isn't right before me.
   PL: …Nie zawsze trzeba wpatrywać się wyłącznie przed siebie.
228. [Interfejs i ustawienia [Ahab_NotTarget_Thrice] — tekst] 나아가려면 내 옆에 있던 것들\n바라봐야할 때도 있는거야…
   źródło: BattleUIText.json :: dataList[id=Ahab_NotTarget_Thrice].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sometimes, to move forward...\n... I have to turn and look beside me.
   PL: Czasem, by ruszyć naprzód…\n…trzeba spojrzeć na tych u swego boku.
229. [Interfejs i ustawienia [show_BattleUnitAblityUI] — tekst] 전투 중 효과 UI 표시
   źródło: BattleUIText.json :: dataList[id=show_BattleUnitAblityUI].content
   limit: do 120 znaków
   EN: Show active effects UI in Combat Phase
   PL: Pokaż interfejs aktywnych efektów w Fazie Walki
230. [Interfejs i ustawienia [LobotomyStartTypo_Title_1] — tekst] 녹빛 여명의 시련
   źródło: BattleUIText.json :: dataList[id=LobotomyStartTypo_Title_1].content
   limit: do 120 znaków
   EN: The Dawn of Green
   PL: Próba Zielonego Świtu
231. [Interfejs i ustawienia [LobotomyStartTypo_Name_1] — tekst] 의문
   źródło: BattleUIText.json :: dataList[id=LobotomyStartTypo_Name_1].content
   limit: do 120 znaków
   EN: Doubt
   PL: Wątpliwość
232. [Interfejs i ustawienia [LobotomyStartTypo_Desc_1] — tekst] 어느날 의문이 생겼다. 우리는 어디서 왔는가. 누군가에게 생명을 받고 무책임하게 놓여졌다.
   źródło: BattleUIText.json :: dataList[id=LobotomyStartTypo_Desc_1].content
   limit: do 180 znaków
   EN: One day, a question crossed through my mind. Where do we come from? We were given life and left in this world against our own volition.
   PL: Pewnego dnia zrodziło się pytanie. Skąd pochodzimy? Otrzymaliśmy życie i porzucono nas na tym świecie wbrew naszej woli.
233. [Interfejs i ustawienia [LobotomyStartTypo_KillCountTitle_1] — tekst] 제압 현황
   źródło: BattleUIText.json :: dataList[id=LobotomyStartTypo_KillCountTitle_1].content
   limit: do 120 znaków
   EN: Suppression Status
   PL: Stan Tłumienia
234. [Interfejs i ustawienia [LobotomyClearTypo_Title_1] — tekst] 녹빛 여명의 시련
   źródło: BattleUIText.json :: dataList[id=LobotomyClearTypo_Title_1].content
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Interfejs i ustawienia [LobotomyClearTypo_Name_1] — tekst] 의문
   źródło: BattleUIText.json :: dataList[id=LobotomyClearTypo_Name_1].content
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [Interfejs i ustawienia [LobotomyClearTypo_Desc_1] — tekst] 살아간다는 것은 고통이었다.
   źródło: BattleUIText.json :: dataList[id=LobotomyClearTypo_Desc_1].content
   limit: do 120 znaków
   EN: To live was a process full of pain.
   PL: Życie było pasmem cierpienia.
237. [Interfejs i ustawienia [LobotomyEndTypo_Title] — tekst] 제압 시간 만료
   źródło: BattleUIText.json :: dataList[id=LobotomyEndTypo_Title].content
   limit: do 120 znaków
   EN: Time Limit Reached
   PL: Upłynął Limit Czasu
238. [Interfejs i ustawienia [LobotomyEndTypo_Desc] — tekst] 남은 시련 개체: {0}
   źródło: BattleUIText.json :: dataList[id=LobotomyEndTypo_Desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Remaining Ordeal Entities: {0}
   PL: Pozostałe Bytności Próby: {0}
239. [Interfejs i ustawienia [abnormality_all_part] — tekst] 전체 부위
   źródło: BattleUIText.json :: dataList[id=abnormality_all_part].content
   limit: do 120 znaków
   EN: All Parts
   PL: Wszystkie Części
240. [Interfejs i ustawienia [applying_buff_format] — tekst] {0} 적용중
   źródło: BattleUIText.json :: dataList[id=applying_buff_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Activated
   PL: {0} — Aktywne
241. [Interfejs i ustawienia [level_number_UNDEF] — tekst] 미정
   źródło: BattleUIText.json :: dataList[id=level_number_UNDEF].content
   limit: do 120 znaków
   EN: Undef.
   PL: Nieokr.
242. [Interfejs i ustawienia [level_number_HYPHEN] — tekst] -
   źródło: BattleUIText.json :: dataList[id=level_number_HYPHEN].content
   limit: do 120 znaków
   EN: -
   PL: -
243. [Interfejs i ustawienia [received_the_golden_bough_undecided] — tekst] ?
   źródło: BattleUIText.json :: dataList[id=received_the_golden_bough_undecided].content
   limit: do 120 znaków
   EN: ?
   PL: ?
244. [Interfejs i ustawienia [vibration_fusion] — tekst] 진폭 얽힘!
   źródło: BattleUIText.json :: dataList[id=vibration_fusion].content
   limit: do 120 znaków
   EN: Amplitude Entanglement!
   PL: Splątanie Amplitudy!
245. [Interfejs i ustawienia [BatonPassUIText] — tekst] 대기해제
   źródło: BattleUIText.json :: dataList[id=BatonPassUIText].content
   limit: do 120 znaków
   EN: Substitute
   PL: Wejście Rezerwy
246. [Interfejs i ustawienia [perfect] — tekst] 완전
   źródło: BattleUIText.json :: dataList[id=perfect].content
   limit: do 120 znaków
   EN: A-Res
   PL: Abs.
247. [Interfejs i ustawienia [ab_part_destroyed] — tekst] 파괴 완료
   źródło: BattleUIText.json :: dataList[id=ab_part_destroyed].content
   limit: do 120 znaków
   EN: Destroyed
   PL: Zniszczona
248. [Interfejs i ustawienia [ab_part_vanished] — tekst] 파괴 및 적출 완료
   źródło: BattleUIText.json :: dataList[id=ab_part_vanished].content
   limit: do 120 znaków
   EN: Destr. & Severed
   PL: Zniszcz. i Odcięta
249. [Interfejs i ustawienia [ab_part_cannot_destroy_and_vanish] — tekst] 파괴 및 적출 불가
   źródło: BattleUIText.json :: dataList[id=ab_part_cannot_destroy_and_vanish].content
   limit: do 120 znaków
   EN: Indestr. & Unsever.
   PL: Niezniszcz. i Nieodcin.
250. [Interfejs i ustawienia [current_hp] — tekst] 현재 체력
   źródło: BattleUIText.json :: dataList[id=current_hp].content
   limit: do 120 znaków
   EN: Current HP
   PL: Aktualne PŻ
251. [Interfejs i ustawienia [break_section_format] — tekst] 흐트러짐 [{0}]
   źródło: BattleUIText.json :: dataList[id=break_section_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Stagger [{0}]
   PL: Oszołomienie [{0}]
252. [Interfejs i ustawienia [no_break_section] — tekst] 흐트러짐 없음
   źródło: BattleUIText.json :: dataList[id=no_break_section].content
   limit: do 120 znaków
   EN: No Stagger Threshold
   PL: Brak Progu Oszołomienia
253. [Interfejs i ustawienia [correction_based_on_unit_keyword] — tekst] {0} 인격 보정 값 {1}(, )
   źródło: BattleUIText.json :: dataList[id=correction_based_on_unit_keyword].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} Identity Modifier: {1}(, )
   PL: Modyfikator Tożsamości ({0}): {1}(, )
254. [Interfejs i ustawienia [battle_operation_counter] — tekst] 강화 반격
   źródło: BattleUIText.json :: dataList[id=battle_operation_counter].content
   limit: do 120 znaków
   EN: Power Counter
   PL: Wzmocniona Kontra
255. [Interfejs i ustawienia [LOBOTOMY_ORDEAL_TIME_TYPE_0] — tekst] 여명
   źródło: BattleUIText.json :: dataList[id=LOBOTOMY_ORDEAL_TIME_TYPE_0].content
   limit: do 120 znaków
   EN: Dawn
   PL: Świt
256. [Interfejs i ustawienia [LOBOTOMY_ORDEAL_TIME_TYPE_1] — tekst] 정오
   źródło: BattleUIText.json :: dataList[id=LOBOTOMY_ORDEAL_TIME_TYPE_1].content
   limit: do 120 znaków
   EN: Noon
   PL: Południe
257. [Interfejs i ustawienia [LOBOTOMY_ORDEAL_TIME_TYPE_2] — tekst] 어스름
   źródło: BattleUIText.json :: dataList[id=LOBOTOMY_ORDEAL_TIME_TYPE_2].content
   limit: do 120 znaków
   EN: Dusk
   PL: Zmierzch
258. [Interfejs i ustawienia [LOBOTOMY_ORDEAL_TIME_TYPE_3] — tekst] 자정
   źródło: BattleUIText.json :: dataList[id=LOBOTOMY_ORDEAL_TIME_TYPE_3].content
   limit: do 120 znaków
   EN: Midnight
   PL: Północ
259. [Interfejs i ustawienia [LobotomyOrdealTypo_QliphothLevel] — tekst] 클리포트 폭주 - {0}단계
   źródło: BattleUIText.json :: dataList[id=LobotomyOrdealTypo_QliphothLevel].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Qliphoth Meltdown - Level {0}
   PL: Przeciążenie Klifot — Poziom {0}
260. [Interfejs i ustawienia [SinkingWhite_stack] — tekst] 산나비
   źródło: BattleUIText.json :: dataList[id=SinkingWhite_stack].content
   limit: do 120 znaków
   EN: The Living
   PL: Żywe
261. [Interfejs i ustawienia [SinkingWhite_turn] — tekst] 죽은나비
   źródło: BattleUIText.json :: dataList[id=SinkingWhite_turn].content
   limit: do 120 znaków
   EN: The Departed
   PL: Zmarłe
262. [Interfejs i ustawienia [BulletLament_stack] — tekst] 산나비(탄환)
   źródło: BattleUIText.json :: dataList[id=BulletLament_stack].content
   limit: do 120 znaków
   EN: The Living(Ammo)
   PL: Żywe (Amunicja)
263. [Interfejs i ustawienia [BulletLament_turn] — tekst] 죽은나비(탄환)
   źródło: BattleUIText.json :: dataList[id=BulletLament_turn].content
   limit: do 120 znaków
   EN: The Departed(Ammo)
   PL: Zmarłe (Amunicja)
264. [Interfejs i ustawienia [Retreat_TextAlarm] — tekst] !퇴각!
   źródło: BattleUIText.json :: dataList[id=Retreat_TextAlarm].content
   limit: do 120 znaków
   EN: !Retreat!
   PL: !Odwrót!
265. [Interfejs i ustawienia [Retreat_TextPassive] — tekst] 퇴각 중
   źródło: BattleUIText.json :: dataList[id=Retreat_TextPassive].content
   limit: do 120 znaków
   EN: Retreating
   PL: W Odwrocie
266. [Interfejs i ustawienia [battle_operation_defense] — tekst] 강화 방어
   źródło: BattleUIText.json :: dataList[id=battle_operation_defense].content
   limit: do 120 znaków
   EN: Power Guard
   PL: Wzmocniona Garda
267. [Interfejs i ustawienia [battle_operation_defense_TextTypo] — tekst] 위력 경감!
   źródło: BattleUIText.json :: dataList[id=battle_operation_defense_TextTypo].content
   limit: do 120 znaków
   EN: Depowered!
   PL: Osłabienie Mocy!
268. [Interfejs i ustawienia [battle_StageBuffUI_Stackdesc] — tekst] (현재 수치: {0})
   źródło: BattleUIText.json :: dataList[id=battle_StageBuffUI_Stackdesc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: (Current Value: {0})
   PL: (Obecna wartość: {0})
269. [Interfejs i ustawienia [EGOSelectUI_not_allow] — tekst] 현재 장착이 불가능한 에고입니다.
   źródło: BattleUIText.json :: dataList[id=EGOSelectUI_not_allow].content
   limit: do 120 znaków
   EN: This E.G.O cannot be equipped at the moment.
   PL: Tego E.G.O nie można obecnie wyposażyć.
270. [Interfejs i ustawienia [laceration_surge] — tekst] 출혈쇄도!
   źródło: BattleUIText.json :: dataList[id=laceration_surge].content
   limit: do 120 znaków
   EN: Bleed Deluge!
   PL: Potop Krwawienia!
271. [Interfejs i ustawienia [QTE_Notice] — tekst] 같이 달려나가는 거야!
   źródło: BattleUIText.json :: dataList[id=QTE_Notice].content
   limit: do 120 znaków
   EN: GALLOP ON, TOGETHER!
   PL: GALOPUJMY RAZEM!
272. [Interfejs i ustawienia [septempeccata_classification] — tekst] {0}형
   źródło: BattleUIText.json :: dataList[id=septempeccata_classification].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Class {0}
   PL: Typ {0}
273. [Interfejs i ustawienia [run_forBattlePortraitStateText] — tekst] 후퇴
   źródło: BattleUIText.json :: dataList[id=run_forBattlePortraitStateText].content
   limit: do 120 znaków
   EN: FLED
   PL: UCIECZKA
274. [Interfejs i ustawienia [ReturnPassUIText] — tekst] 복귀
   źródło: BattleUIText.json :: dataList[id=ReturnPassUIText].content
   limit: do 120 znaków
   EN: Return
   PL: Powrót
275. [Interfejs i ustawienia [NoHavePassive] — tekst] 동기화 단계 낮음\n서포트 패시브 비활성화 상태
   źródło: BattleUIText.json :: dataList[id=NoHavePassive].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Support Passive Locked\nUptie to Unlock
   PL: Pasywka Wsparcia Zablokowana\nZwiększ Synchronizację
276. [Interfejs i ustawienia [LocalSetButtonTitle_ImportanceLevel] — tekst] 중요도
   źródło: BattleUIText.json :: dataList[id=LocalSetButtonTitle_ImportanceLevel].content
   limit: do 120 znaków
   EN: Hints
   PL: Priorytet
277. [Interfejs i ustawienia [Retreat_Command_TextAlarm] — tekst] !퇴각 명령!
   źródło: BattleUIText.json :: dataList[id=Retreat_Command_TextAlarm].content
   limit: do 120 znaków
   EN: !Retreat Order!
   PL: !Rozkaz Odwrotu!
278. [Interfejs i ustawienia [Retreat_Quit_TextAlarm] — tekst] !전장 이탈!
   źródło: BattleUIText.json :: dataList[id=Retreat_Quit_TextAlarm].content
   limit: do 120 znaków
   EN: !Escape Battlefield!
   PL: !Ucieczka z Pola Bitwy!
279. [Interfejs i ustawienia [ab_part_gadget_activated] — tekst] 활성화
   źródło: BattleUIText.json :: dataList[id=ab_part_gadget_activated].content
   limit: do 120 znaków
   EN: On
   PL: Wł.
280. [Interfejs i ustawienia [ab_part_gadget_deactivated] — tekst] 비활성화
   źródło: BattleUIText.json :: dataList[id=ab_part_gadget_deactivated].content
   limit: do 120 znaków
   EN: Off
   PL: Wył.
281. [Interfejs i ustawienia [UpperSkillInfo_Player_ImportanceLevel_1_Desc] — tekst] !대응 중요도: 중간!
   źródło: BattleUIText.json :: dataList[id=UpperSkillInfo_Player_ImportanceLevel_1_Desc].content
   limit: do 120 znaków
   EN: !Priority:Med.!
   PL: !Priorytet: Średni!
282. [Interfejs i ustawienia [UpperSkillInfo_Player_ImportanceLevel_2_Desc] — tekst] !대응 중요도: 높음!
   źródło: BattleUIText.json :: dataList[id=UpperSkillInfo_Player_ImportanceLevel_2_Desc].content
   limit: do 120 znaków
   EN: !Priority:High!
   PL: !Priorytet: Wysoki!
283. [Interfejs i ustawienia [UpperSkillInfo_Player_ImportanceLevel_3_Desc] — tekst] !대응 중요도: 매우 높음!
   źródło: BattleUIText.json :: dataList[id=UpperSkillInfo_Player_ImportanceLevel_3_Desc].content
   limit: do 120 znaków
   EN: !Priority:V.High!
   PL: !Priorytet: B. Wysoki!
284. [Interfejs i ustawienia [UpperSkillInfo_Enemy_ImportanceLevel_1_Desc] — tekst] !대응 중요도: 중간!
   źródło: BattleUIText.json :: dataList[id=UpperSkillInfo_Enemy_ImportanceLevel_1_Desc].content
   limit: do 120 znaków
   EN: !Priority: Med.!
   PL: !Priorytet: Średni!
285. [Interfejs i ustawienia [UpperSkillInfo_Enemy_ImportanceLevel_2_Desc] — tekst] !대응 중요도: 높음!
   źródło: BattleUIText.json :: dataList[id=UpperSkillInfo_Enemy_ImportanceLevel_2_Desc].content
   limit: do 120 znaków
   EN: !Priority: High!
   PL: !Priorytet: Wysoki!
286. [Interfejs i ustawienia [UpperSkillInfo_Enemy_ImportanceLevel_3_Desc] — tekst] !대응 중요도: 매우 높음!
   źródło: BattleUIText.json :: dataList[id=UpperSkillInfo_Enemy_ImportanceLevel_3_Desc].content
   limit: do 120 znaków
   EN: !Priority: Very High!
   PL: !Priorytet: Bardzo Wysoki!
287. [Interfejs i ustawienia [EgoGiftListPopupTabType_CANDIDATE] — tekst] 조건부 발동
   źródło: BattleUIText.json :: dataList[id=EgoGiftListPopupTabType_CANDIDATE].content
   limit: do 120 znaków
   EN: Conditional
   PL: Warunkowe
288. [Interfejs i ustawienia [EgoGiftListPopupTabType_EXCLUDE_CANDIDATE] — tekst] 상시 발동
   źródło: BattleUIText.json :: dataList[id=EgoGiftListPopupTabType_EXCLUDE_CANDIDATE].content
   limit: do 120 znaków
   EN: Always Active
   PL: Zawsze Aktywne
289. [Interfejs i ustawienia [EgoGiftListPopupTabType_active] — tekst] 발동 중
   źródło: BattleUIText.json :: dataList[id=EgoGiftListPopupTabType_active].content
   limit: do 120 znaków
   EN: Activated
   PL: Aktywne
290. [Interfejs i ustawienia [UnitInformation_emptySkillList] — tekst] 스킬이 없습니다.
   źródło: BattleUIText.json :: dataList[id=UnitInformation_emptySkillList].content
   limit: do 120 znaków
   EN: No Skills in this category.
   PL: Brak umiejętności w tej kategorii.
291. [Interfejs i ustawienia [retire_forBattlePortraitStateText] — tekst] 전투 불능
   źródło: BattleUIText.json :: dataList[id=retire_forBattlePortraitStateText].content
   limit: do 120 znaków
   EN: Incapacitated
   PL: Niezdatny do Walki
292. [Interfejs i ustawienia [KAA1C9ActivateEffect] — tekst] 사용된 K사 앰플
   źródło: BattleUIText.json :: dataList[id=KAA1C9ActivateEffect].content
   limit: do 120 znaków
   EN: Used K Corp. Ampule
   PL: Zużyta Ampułka Korp. K
293. [Interfejs i ustawienia [contMineInfo_Title] — tekst] 현재 진행 중인 회차
   źródło: BattleUIText.json :: dataList[id=contMineInfo_Title].content
   limit: do 120 znaków
   EN: Progress:
   PL: Bieżący przebieg:
294. [Interfejs i ustawienia [contMineInfo_Desc_Valid_Reward] — tekst] ※ 스테이지 포기 시 모듈 {0}개 소모 및 보상 획득
   źródło: BattleUIText.json :: dataList[id=contMineInfo_Desc_Valid_Reward].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ※ Forfeiting the Stage now will cost {0} Enkephalin Modules and yield rewards based on Modules used
   PL: ※ Poddanie etapu zużyje Moduły Enkefaliny ({0}) i przyzna nagrody odpowiednie do zużycia
295. [Interfejs i ustawienia [contMineInfo_Desc_Invalid_Reward] — tekst] ※ 스테이지 포기 시 모듈 소모·보상 획득 없음
   źródło: BattleUIText.json :: dataList[id=contMineInfo_Desc_Invalid_Reward].content
   limit: do 120 znaków
   EN: ※ Forfeiting the Stage now will not cost Enkephalin Modules and will not yield rewards
   PL: ※ Poddanie etapu nie zużyje Modułów Enkefaliny i nie przyzna nagród
296. [Interfejs i ustawienia [battle_operation_player_support] — tekst] 서포트
   źródło: BattleUIText.json :: dataList[id=battle_operation_player_support].content
   limit: do 120 znaków
   EN: Support
   PL: Wsparcie
297. [Interfejs i ustawienia [PassiveSynergyConditionCount] — tekst] {0}
   źródło: BattleUIText.json :: dataList[id=PassiveSynergyConditionCount].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}
   PL: {0}

## Samouczek i wskazówki: SuccessRate
- plik gry: `SuccessRate.json`

298. [Samouczek i wskazówki [very-high] — tekst] 매우 우세
   źródło: SuccessRate.json :: dataList[id=very-high].content
   limit: do 120 znaków
   EN: Dominating
   PL: Dominująca
299. [Samouczek i wskazówki [high] — tekst] 우세
   źródło: SuccessRate.json :: dataList[id=high].content
   limit: do 120 znaków
   EN: Favored
   PL: Korzystna
300. [Samouczek i wskazówki [normal] — tekst] 균형
   źródło: SuccessRate.json :: dataList[id=normal].content
   limit: do 120 znaków
   EN: Neutral
   PL: Równa
301. [Samouczek i wskazówki [low] — tekst] 불리
   źródło: SuccessRate.json :: dataList[id=low].content
   limit: do 120 znaków
   EN: Struggling
   PL: Niekorzystna
302. [Samouczek i wskazówki [very-low] — tekst] 매우 불리
   źródło: SuccessRate.json :: dataList[id=very-low].content
   limit: do 120 znaków
   EN: Hopeless
   PL: Beznadziejna
303. [Samouczek i wskazówki [impossible] — tekst] 선택 불가
   źródło: SuccessRate.json :: dataList[id=impossible].content
   limit: do 120 znaków
   EN: Unselectable
   PL: Niedostępne
304. [Samouczek i wskazówki [event-very-high] — tekst] 매우 높음
   źródło: SuccessRate.json :: dataList[id=event-very-high].content
   limit: do 120 znaków
   EN: Very High
   PL: Bardzo Wysoka
305. [Samouczek i wskazówki [event-high] — tekst] 높음
   źródło: SuccessRate.json :: dataList[id=event-high].content
   limit: do 120 znaków
   EN: High
   PL: Wysoka
306. [Samouczek i wskazówki [event-normal] — tekst] 보통
   źródło: SuccessRate.json :: dataList[id=event-normal].content
   limit: do 120 znaków
   EN: Normal
   PL: Średnia
307. [Samouczek i wskazówki [event-low] — tekst] 낮음
   źródło: SuccessRate.json :: dataList[id=event-low].content
   limit: do 120 znaków
   EN: Low
   PL: Niska
308. [Samouczek i wskazówki [event-very-low] — tekst] 매우 낮음
   źródło: SuccessRate.json :: dataList[id=event-very-low].content
   limit: do 120 znaków
   EN: Very Low
   PL: Bardzo Niska
309. [Samouczek i wskazówki [event-impossible] — tekst] 선택 불가
   źródło: SuccessRate.json :: dataList[id=event-impossible].content
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
