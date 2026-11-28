# Paczka AI P80 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 16/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P80_3c_przeciwnicy_i_anomalie_cz16.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P80_3c_przeciwnicy_i_anomalie_cz16.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [podstawowe] Umiejętności wrogów / Anomalii — Skills_Abnormality_Mirror7-extreme
- grupa rozdziału/trybu: `podstawowe` · plik: `Skills_Abnormality_Mirror7-extreme.json`

1. [Umiejętność wroga [140403] (ulepszenie 1) — opis] 파괴된 팔의 수만큼 기본 위력 -1\n[WhenUse] 대상에게 부정적인 효과가 2개 이상 있으면, 합 위력 +2
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140403].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: Base Power -1 for every broken Arm\n[WhenUse] If target has 2+ types of negative effect, Clash Power +2
   PL: Moc Bazowa -1 za każde zniszczone ramię\n[WhenUse] jeżeli cel ma 2+ rodzaje negatywnych efektów, Moc Starcia +2
2. [Umiejętność wroga [140403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] nakłada 3 [Laceration]
3. [Umiejętność wroga [140403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis] next turn
   PL: [OnSucceedAttack] nakłada 2 [Paralysis] w następnej turze
4. [Umiejętność wroga [140403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
5. [Umiejętność wroga [140404] (ulepszenie 1) — nazwa] 양팔 후려치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140404].levelList[level=1].name
   limit: do 40 znaków
   EN: Thrashing Arms
   PL: Thrashing Arms
6. [Umiejętność wroga [140404] (ulepszenie 1) — opis] [WhenUse] 대상에게 부정적인 효과가 2개 이상 있으면, 기본 위력 +2\n[DefeatDuel] [Aggressive] 1 잃음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140404].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Aggressive]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Aggressive] = 본능 / Instincts
   EN: [WhenUse] If target has 2+ types of negative effect, Base Power +2\n[DefeatDuel] Lose 1 [Aggressive]
   PL: [WhenUse] jeżeli cel ma 2+ rodzaje negatywnych efektów, Moc Bazowa +2\n[DefeatDuel] traci 1 [Aggressive]
7. [Umiejętność wroga [140404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 손상 10
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 10
   PL: [OnSucceedAttack] podnosi Próg Oszołomienia o 10
8. [Umiejętność wroga [140404] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140404].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 5 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 5 [Binding] w następnej turze
9. [Umiejętność wroga [140405] (ulepszenie 1) — nazwa] 숨죽이기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140405].levelList[level=1].name
   limit: do 40 znaków
   EN: Held Breath
   PL: Held Breath
10. [Umiejętność wroga [140405] (ulepszenie 1) — opis] [StartBattle] [Aggressive] 5 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140405].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Aggressive]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Aggressive] = 본능 / Instincts
   EN: [StartBattle] Gain 5 [Aggressive]
   PL: [StartBattle] zyskuje 5 [Aggressive]
11. [Umiejętność wroga [140406] (ulepszenie 1) — nazwa] 고통의 몸부림
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140406].levelList[level=1].name
   limit: do 40 znaków
   EN: Pained Writhing
   PL: Pained Writhing
12. [Umiejętność wroga [140406] (ulepszenie 1) — opis] [WhenUse] 대상에게 부정적인 효과가 있으면, 기본 위력 +3\n[WhenUse] 체력 12 소모. 다음 턴에 [Laceration] 5를 얻음\n[DefeatDuel] 기본 위력 -5\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140406].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If target has a negative effect, Base Power +3\n[WhenUse] Lose 12 HP; gain 5 [Laceration] next turn\n[DefeatDuel] Base Power -5\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] jeżeli cel ma negatywny efekt, Moc Bazowa +3\n[WhenUse] traci 12 HP; zyskuje 5 [Laceration] w następnej turze\n[DefeatDuel] Moc Bazowa -5\n[DefeatDuel] zadaje o 80% mniej obrażeń, a te obrażenia nie Oszołamują celu
13. [Umiejętność wroga [140406] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140406].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
14. [Umiejętność wroga [140406] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 독 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140406].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Poison
   PL: [OnSucceedAttack] nakłada 3 Zatrucia
15. [Umiejętność wroga [140406] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140406].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
16. [Umiejętność wroga [140406] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 독 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140406].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [Umiejętność wroga [140406] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140406].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [Umiejętność wroga [140406] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 독 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140406].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
19. [Umiejętność wroga [140407] (ulepszenie 1) — nazwa] 고통의 발악
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140407].levelList[level=1].name
   limit: do 40 znaków
   EN: Pained Struggle
   PL: Pained Struggle
20. [Umiejętność wroga [140407] (ulepszenie 1) — opis] [WhenUse] 대상에게 부정적인 효과가 있으면, 기본 위력 +4\n[WhenUse] 체력 12 소모. 다음 턴에 자신의 [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140407].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has a negative effect, Base Power +4\n[WhenUse] Lose 12 HP; gain +3 [Laceration] Count next turn
   PL: [WhenUse] jeżeli cel ma negatywny efekt, Moc Bazowa +4\n[WhenUse] traci 12 HP; w następnej turze zwiększa Licznik [Laceration] o 3
21. [Umiejętność wroga [140407] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140407].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis] next turn
   PL: [OnSucceedAttack] nakłada 3 [Paralysis] w następnej turze
22. [Umiejętność wroga [140407] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140407].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 3 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 3 [Binding] w następnej turze
23. [Umiejętność wroga [140501] (ulepszenie 1) — nazwa] 조아려라
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140501].levelList[level=1].name
   limit: do 40 znaków
   EN: Grovel Before Me
   PL: Grovel Before Me
24. [Umiejętność wroga [140501] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 4 이상이면, 합 위력 +1
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 4+ [Laceration], Clash Power +1
   PL: [WhenUse] jeżeli cel ma 4+ [Laceration], Moc Starcia +1
25. [Umiejętność wroga [140501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] nakłada 4 [Laceration]
26. [Umiejętność wroga [140502] (ulepszenie 1) — nazwa] 하찮은 것
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140502].levelList[level=1].name
   limit: do 40 znaków
   EN: Pathetic One
   PL: Pathetic One
27. [Umiejętność wroga [140502] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 4 이상이면, 합 위력 +1
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140502].levelList[level=1].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
28. [Umiejętność wroga [140502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Laceration] o 2
29. [Umiejętność wroga [140503] (ulepszenie 1) — nazwa] 저리 가... 저리 가...!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140503].levelList[level=1].name
   limit: do 40 znaków
   EN: Go... Go Away...!
   PL: Go... Go Away...!
30. [Umiejętność wroga [140503] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 4 이상이면, 합 위력 +1\n[WhenUse] 대상의 [Laceration] 횟수당, 피해량 +5% (최대 20%)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140503].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 4+ [Laceration], Clash Power +1\n[WhenUse] Deal +5% damage for every [Laceration] Count on the target (max 20%)
   PL: [WhenUse] jeżeli cel ma 4+ [Laceration], Moc Starcia +1\n[WhenUse] zadaje +5% obrażeń za każdy Licznik [Laceration] celu (maks. 20%)
31. [Umiejętność wroga [140503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 8 부여. [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 8 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 8 [Laceration] i zwiększa Licznik [Laceration] o 2
32. [Umiejętność wroga [140504] (ulepszenie 1) — nazwa] 퍼레이드의 왕자
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140504].levelList[level=1].name
   limit: do 40 znaków
   EN: The Parade's Prince
   PL: The Parade's Prince
33. [Umiejętność wroga [140504] (ulepszenie 1) — opis] [StartBattle] [Laceration]을 가진 대상만큼 가중치 증가 (최대 5)\n[WhenUse] 메인 타겟의 [Laceration]이 4 이상이면, 기본 위력 +1\n[WhenUse] 메인 타겟의 [Laceration] 횟수가 3 이상이면, 코인 위력 +1\n[DefeatDuel] [KeptBlood] 1 감소
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140504].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Laceration], [WhenUse], [DefeatDuel], [KeptBlood]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [KeptBlood] = 머금은 피 / Stored Blood
   EN: [StartBattle] Gain Atk Weight equal to the number of targets that have [Laceration] (max 5)\n[WhenUse] If the main target has 4+ [Laceration], Base Power +1\n[WhenUse] If the main target has 3+ [Laceration] Count, Coin Power +1\n[DefeatDuel] Lose 1 [KeptBlood]
   PL: [StartBattle] zyskuje Wagę Ataku równą liczbie celów z [Laceration] (maks. 5)\n[WhenUse] jeżeli główny cel ma 4+ [Laceration], Moc Bazowa +1\n[WhenUse] jeżeli główny cel ma 3+ Liczników [Laceration], Moc Monet +1\n[DefeatDuel] traci 1 [KeptBlood]
34. [Umiejętność wroga [140504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
35. [Umiejętność wroga [140504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
36. [Umiejętność wroga [140504] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140504].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
37. [Umiejętność wroga [140504] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140504].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Umiejętność wroga [140504] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [KeptBlood] 1 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140504].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [KeptBlood]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KeptBlood] = 머금은 피 / Stored Blood
   EN: [OnSucceedAttack] Gain 1 [KeptBlood]
   PL: [OnSucceedAttack] zyskuje 1 [KeptBlood]
39. [Umiejętność wroga [140505] (ulepszenie 1) — nazwa] 피... 피... 피...!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140505].levelList[level=1].name
   limit: do 40 znaków
   EN: Blood... Blood... Blood...!
   PL: Blood... Blood... Blood...!
40. [Umiejętność wroga [140505] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 8 이상이면, 코인 위력 +1\n[DefeatDuel] [KeptBlood] 1 감소
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140505].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DefeatDuel], [KeptBlood]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [KeptBlood] = 머금은 피 / Stored Blood
   EN: [WhenUse] If target has 8+ [Laceration], Coin Power +1\n[DefeatDuel] Lose 1 [KeptBlood]
   PL: [WhenUse] jeżeli cel ma 8+ [Laceration], Moc Monet +1\n[DefeatDuel] traci 1 [KeptBlood]
41. [Umiejętność wroga [140505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 5 [Laceration] i zwiększa Licznik [Laceration] o 3
42. [Umiejętność wroga [140505] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10 이상이면, 다음 코인 피해량 +20%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140505].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 10+ [Laceration], the next Coin deals +20% damage
   PL: [OnSucceedAttack] jeżeli cel ma 10+ [Laceration], następna Moneta zadaje +20% obrażeń
43. [Umiejętność wroga [140505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [KeptBlood] 1 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Umiejętność wroga [140505] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140505].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 1 [Binding] w następnej turze
45. [Umiejętność wroga [140506] (ulepszenie 1) — nazwa] 날 내버려둬...!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140506].levelList[level=1].name
   limit: do 40 znaków
   EN: Leave Me Alone...!
   PL: Leave Me Alone...!
46. [Umiejętność wroga [140506] (ulepszenie 1) — opis] [WhenUseEvade] 대상의 [Laceration] 횟수당 기본 위력 +1 (최대 4)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140506].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUseEvade], [Laceration]
   znaczenie tagów: [WhenUseEvade] = [회피 사용시] / [On Evade Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUseEvade] Base Power +1 for every [Laceration] Count on the target (max 4)
   PL: [WhenUseEvade] Moc Bazowa +1 za każdy Licznik [Laceration] celu (maks. 4)
47. [Umiejętność wroga [140507] (ulepszenie 1) — nazwa] 나는... 이 행진의... 왕자이다...!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140507].levelList[level=1].name
   limit: do 60 znaków
   EN: I Am... The Prince... of the Parade...!
   PL: I Am... The Prince... of the Parade...!
48. [Umiejętność wroga [140507] (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] [Paralysis] 4 얻음\n[WhenUse] <noparse>경혈식 글레이브</noparse>의 회복 효과가 2배로 적용됨\n[WhenUse] 정신력이 0이 됨\n[EndSkill] [KeptBlood] 10 얻음\n이번 턴 동안 흐트러짐 상태가 되지 않고 이 스킬 사용 후 턴 종료함
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140507].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [CantDuel], [WhenUse], [Paralysis], [EndSkill], [KeptBlood], [TabExplain]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Paralysis] = 마비 / Paralyze; [EndSkill] = [공격 종료시] / [Attack End]; [KeptBlood] = 머금은 피 / Stored Blood
   EN: [CantDuel]\n[WhenUse] Gain 4 [Paralysis]\n[WhenUse] Double Hardblood[TabExplain] Glaive's heal effect\n[WhenUse] Reset SP to 0\n[EndSkill] Gain [KeptBlood] 10\nDoes not get Staggered this turn; ends turn after using this Skill.
   PL: [CantDuel]\n[WhenUse] zyskuje 4 [Paralysis]\n[WhenUse] podwaja efekt przywracania przez Hardblood[TabExplain] Glaive\n[WhenUse] SP wraca do 0\n[EndSkill] zyskuje 10 [KeptBlood]\nW tej turze nie przechodzi w stan Oszołamienia; po użyciu tej Umiejętności kończy turę.
49. [Umiejętność wroga [140507] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140507].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +1 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 [Laceration] i zwiększa Licznik [Laceration] o 1
50. [Umiejętność wroga [140507] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140507].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Umiejętność wroga [140507] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140507].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Umiejętność wroga [140507] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140507].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [Umiejętność wroga [140508] (ulepszenie 1) — nazwa] 절대... 돌아가지 않아...!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140508].levelList[level=1].name
   limit: do 50 znaków
   EN: I'm... Never... Going Back...!
   PL: I'm... Never... Going Back...!
54. [Umiejętność wroga [140508] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 [Laceration] 5당, 합 위력 +1 (최대 3)\n[WhenUse] 메인 타겟의 [Laceration] 횟수 4 이상이면, 코인 위력 +1\n[WhenUse] 메인 타겟의 [Laceration] 횟수당, 피해량 +5% (최대 20%)\n[WinDuel] <noparse>경혈식 글레이브</noparse>의 회복 효과가 2배로 적용됨\n[DefeatDuel] <noparse>경혈식 글레이브</noparse>의 회복 효과가 발동하지 않음\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] [KeptBlood] 10 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140508].levelList[level=1].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [WhenUse], [Laceration], [WinDuel], [DefeatDuel], [EndSkill], [KeptBlood], [TabExplain]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [KeptBlood] = 머금은 피 / Stored Blood
   EN: [WhenUse] Clash Power +1 for every 5 [Laceration] on the main target (max 3)\n[WhenUse] At 4+ [Laceration] Count on the main target, Coin Power +1\n[WhenUse] Deal +5% damage for every [Laceration] Count on the main target (max 20%)\n[WinDuel] Double Hardblood[TabExplain] Glaive's heal effect\n[DefeatDuel] Hardblood[TabExplain] Glaive's heal effect does not activate\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] Gain [KeptBlood] 10
   PL: [WhenUse] Moc Starcia +1 za każde 5 [Laceration] głównego celu (maks. 3)\n[WhenUse] przy 4+ Licznikach [Laceration] głównego celu, Moc Monet +1\n[WhenUse] zadaje +5% obrażeń za każdy Licznik [Laceration] głównego celu (maks. 20%)\n[WinDuel] podwaja efekt przywracania przez Hardblood[TabExplain] Glaive\n[DefeatDuel] efekt przywracania przez Hardblood[TabExplain] Glaive nie uaktywnia się\n[DefeatDuel] zadaje o 80% mniej obrażeń, a te obrażenia nie Oszołamują celu\n[EndSkill] zyskuje 10 [KeptBlood]
55. [Umiejętność wroga [140508] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140508].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +1 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 [Laceration] i zwiększa Licznik [Laceration] o 1
56. [Umiejętność wroga [140508] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140508].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Umiejętność wroga [140508] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140508].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [Umiejętność wroga [140508] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140508].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Umiejętność wroga [140508] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140508].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration] and +1 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Laceration] i zwiększa Licznik [Laceration] o 1
60. [Umiejętność wroga [140601] (ulepszenie 1) — nazwa] 의체 가동
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140601].levelList[level=1].name
   limit: do 40 znaków
   EN: Activate Prosthesis
   PL: Activate Prosthesis
61. [Umiejętność wroga [140601] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 10 이상이면, [Charge] 횟수 3을 소모하여 코인 위력 +1\n[WhenUse] [Charge] 횟수가 15 이상이면, [Charge] 횟수 3을 추가로 소모하여 피해량 + 20%\n[WhenUse] [Charge] 횟수가 5 미만이면, 최대 체력의 10%만큼 체력이 감소하고 [Charge] 횟수 9 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140601].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 10+ [Charge] Count, consume 3 [Charge] Count to gain Coin Power +1\n[WhenUse] At 15+ [Charge] Count, consume 3 additional [Charge] Count to deal +20% damage\n[WhenUse] At less than 5 [Charge] Count, lose 10% HP and gain +9 [Charge] Count
   PL: [WhenUse] przy 10+ Licznikach [Charge], zużywa 3 Liczniki [Charge], by zyskać Moc Monet +1\n[WhenUse] przy 15+ Licznikach [Charge], zużywa dodatkowo 3 Liczniki [Charge], by zadać +20% obrażeń\n[WhenUse] przy mniej niż 5 Licznikach [Charge], traci 10% HP i zyskuje +9 Liczników [Charge]
62. [Umiejętność wroga [140601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [Umiejętność wroga [140601] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140601].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [Umiejętność wroga [140602] (ulepszenie 1) — nazwa] 경혈식 혈액 역류
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140602].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Reflux
   PL: Hardblood Reflux
65. [Umiejętność wroga [140602] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 10 이상이면, [Charge] 횟수 3을 소모하여 코인 위력 +1\n[WhenUse] [Charge] 횟수가 15 이상이면, [Charge] 횟수 3을 추가로 소모하여 피해량 + 20%\n[WhenUse] [Charge] 횟수가 5 미만이면, 최대 체력의 10%만큼 체력이 감소하고 [Charge] 횟수 9 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140602].levelList[level=1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Umiejętność wroga [140602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [Umiejętność wroga [140602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis]
   PL: [OnSucceedAttack] nakłada 2 [Paralysis]
68. [Umiejętność wroga [140602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] nakłada 2 [Laceration]
69. [Umiejętność wroga [140602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Laceration] o 1
70. [Umiejętność wroga [140602] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140602].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
71. [Umiejętność wroga [140602] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140602].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Umiejętność wroga [140603] (ulepszenie 1) — nazwa] 생체 에너지 전환식 충전
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140603].levelList[level=1].name
   limit: do 40 znaków
   EN: Bioenergy Conversion Charge
   PL: Bioenergy Conversion Charge
73. [Umiejętność wroga [140603] (ulepszenie 1) — opis] [WhenUse] 자신의 체력을 최대 체력의 10% 만큼 소모하여 [Charge] 횟수 15 증가\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140603].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Consume 10% HP on self to gain +15 [Charge] Count\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] zużywa 10% swojego HP, by zyskać +15 Liczników [Charge]\n[DefeatDuel] zadaje o 50% mniej obrażeń, a te obrażenia nie Oszołamują celu
74. [Umiejętność wroga [140603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [Umiejętność wroga [140603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 4 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 4 [Laceration]
76. [Umiejętność wroga [140603] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140603].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 Licznika [Laceration]
77. [Umiejętność wroga [140603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [Umiejętność wroga [140603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 6 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 6 [Laceration]
79. [Umiejętność wroga [140603] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140603].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 Licznika [Laceration]
80. [Umiejętność wroga [140603] (ulepszenie 1) — moneta 2, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [AttackDown] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140603].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [AttackDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [AttackDown]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [AttackDown]
81. [Umiejętność wroga [140604] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140604].levelList[level=1].name
   limit: do 40 znaków
   EN: Guard
   PL: Garda
82. [Umiejętność wroga [140604] (ulepszenie 1) — opis] [WhenUse] 자신의 [Laceration] 횟수 3당, 기본 위력 +1 (최대 2)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Base Power +1 for every 3 [Laceration] Count on self (max 2)
   PL: [WhenUse] Moc Bazowa +1 za każde 3 Liczników [Laceration] jednostki (maks. 2)
83. [Umiejętność wroga [140605] (ulepszenie 1) — nazwa] 경혈식 혈액 이전
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140605].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Transfusion
   PL: Hardblood Transfusion
84. [Umiejętność wroga [140605] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 10 이상이면, [Charge] 횟수 3을 소모하여 코인 위력 +1\n[WhenUse] [Charge] 횟수가 15 이상이면, [Charge] 횟수 3을 추가로 소모하여 피해량 + 20%\n[WhenUse] [Charge] 횟수가 5 미만이면, 최대 체력의 10%만큼 체력이 감소하고 [Charge] 횟수 9 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140605].levelList[level=1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Umiejętność wroga [140605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Umiejętność wroga [140605] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140605].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność wroga [140605] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140605].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Umiejętność wroga [140606] (ulepszenie 1) — nazwa] 생체 에너지 전환식 재충전
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140606].levelList[level=1].name
   limit: do 50 znaków
   EN: Bioenergy Conversion Recharge
   PL: Bioenergy Conversion Recharge
89. [Umiejętność wroga [140606] (ulepszenie 1) — opis] [WhenUse] 자신의 체력을 최대 체력의 10% 만큼 소모하여 [Charge] 횟수 15 증가\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140606].levelList[level=1].desc
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Umiejętność wroga [140606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Umiejętność wroga [140606] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140606].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Umiejętność wroga [140606] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140606].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Vulnerable]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Vulnerable]
93. [Umiejętność wroga [140606] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140606].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Umiejętność wroga [140606] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140606].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Umiejętność wroga [140606] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가.
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140606].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada +1 Licznika [Laceration].
96. [Umiejętność wroga [140606] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140606].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Umiejętność wroga [140606] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140606].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Umiejętność wroga [140606] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가.
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140606].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] zwiększa Licznik [Laceration] o 2.
99. [Umiejętność wroga [140606] (ulepszenie 1) — moneta 3, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [AttackDown] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140606].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Umiejętność wroga [140701] (ulepszenie 1) — nazwa] 걸려든 미끼
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140701].levelList[level=1].name
   limit: do 40 znaków
   EN: Snagged Lure
   PL: Snagged Lure
101. [Umiejętność wroga [140701] (ulepszenie 1) — opis] [CantDuel]\n요정이 살아있는 턴만큼 공격 가중치가 증가함.\n[FairyCharm]에 걸린 인격 우선 공격
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140701].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [FairyCharm]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [FairyCharm] = 매혹 / Charmed
   EN: [CantDuel] \nGain +1 Atk Weight for every turn Fairy is alive\nPrioritizes Identities that have [FairyCharm]
   PL: [CantDuel] \nZyskuje +1 Wagi Ataku za każdą turę, w której Wróżka żyje\npriorytet: Tożsamości z [FairyCharm]
102. [Umiejętność wroga [140701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Burst]
103. [Umiejętność wroga [140701] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140701].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Umiejętność wroga [140701] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 본체, 몸통 체력 15 회복
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140701].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Core and Body heal 15 HP
   PL: [OnSucceedAttack] przywraca 15 HP Korpusowi i Części Korpusu
105. [Umiejętność wroga [140702] (ulepszenie 1) — nazwa] 파고드는 뿌리
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140702].levelList[level=1].name
   limit: do 40 znaków
   EN: Burrowing Roots
   PL: Burrowing Roots
106. [Umiejętność wroga [140702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Burst]
107. [Umiejętność wroga [140702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Laceration] o 3
108. [Umiejętność wroga [140703] (ulepszenie 1) — nazwa] 확산하는 뿌리
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140703].levelList[level=1].name
   limit: do 40 znaków
   EN: Expanding Roots
   PL: Expanding Roots
109. [Umiejętność wroga [140703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]
   PL: [OnSucceedAttack] nakłada 5 [Burst]
110. [Umiejętność wroga [140703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL: [OnSucceedAttack] nakłada 5 [Laceration]
111. [Umiejętność wroga [140704] (ulepszenie 1) — nazwa] 잠식하는 줄기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140704].levelList[level=1].name
   limit: do 40 znaków
   EN: Encroaching Stems
   PL: Encroaching Stems
112. [Umiejętność wroga [140704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Burst] 수치당 피해량 +5%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Deal +5% damage for every [Burst] on target
   PL: [OnSucceedAttack] zadaje +5% obrażeń za każdy [Burst] celu
113. [Umiejętność wroga [140705] (ulepszenie 1) — nazwa] 드러난 심연
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140705].levelList[level=1].name
   limit: do 40 znaków
   EN: Uncovered Abyss
   PL: Uncovered Abyss
114. [Umiejętność wroga [140705] (ulepszenie 1) — opis] 대상에게 [Burst]이 5이상 있다면 피해량 +100%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140705].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 5+ [Burst], deal +100% damage
   PL: jeżeli cel ma 5+ [Burst], zadaje +100% obrażeń
115. [Umiejętność wroga [140801] (ulepszenie 1) — nazwa] 상처 훑기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140801].levelList[level=1].name
   limit: do 40 znaków
   EN: Skim Wounds
   PL: Brush Wounds
116. [Umiejętność wroga [140801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 [Laceration]을 가지고 있다면, [Paralysis] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] If target has [Laceration], inflict 1 [Paralysis]
   PL: [OnSucceedAttack] jeżeli cel ma [Laceration], nakłada 1 [Paralysis]
117. [Umiejętność wroga [140801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Umiejętność wroga [140801] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수가 2 이상이면 [Laceration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140801].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 2+ [Laceration] Count, inflict 5 [Laceration]
   PL: [OnSucceedAttack] jeżeli cel ma 2+ Liczników [Laceration], nakłada 5 [Laceration]
119. [Umiejętność wroga [140802] (ulepszenie 1) — nazwa] 옭아매인 상처
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140802].levelList[level=1].name
   limit: do 40 znaków
   EN: Entangled Injury
   PL: Entangled Injury
120. [Umiejętność wroga [140802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 [Laceration]을 가지고 있다면, [Binding] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] If target has [Laceration], inflict 1 [Binding]
   PL: [OnSucceedAttack] jeżeli cel ma [Laceration], nakłada 1 [Binding]
121. [Umiejętność wroga [140802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Umiejętność wroga [140803] (ulepszenie 1) — nazwa] 묻어오는 살점
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140803].levelList[level=1].name
   limit: do 40 znaków
   EN: Smeared Flesh
   PL: Smeared Flesh
123. [Umiejętność wroga [140803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Umiejętność wroga [140803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 [Laceration]을 가지고 있다면, 체력 20 회복
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has [Laceration], heal 20 HP
   PL: [OnSucceedAttack] jeżeli cel ma [Laceration], przywraca 20 HP
125. [Umiejętność wroga [140803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 횟수가 2 이상이면 [Laceration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Umiejętność wroga [140804] (ulepszenie 1) — nazwa] 드리우는 그늘
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140804].levelList[level=1].name
   limit: do 40 znaków
   EN: Casting Shade
   PL: Casting Shade
127. [Umiejętność wroga [140804] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 거대 클로버 생성\n[DefeatDuel] 거대 클로버의 체력이 70%인 상태로 생성됨
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Spawn a Giant Clover next turn\n[DefeatDuel] The Giant Clover spawns with 70% HP
   PL: [WhenUse] przywołuje Giant Clover w następnej turze\n[DefeatDuel] Giant Clover powstaje z 70% HP
128. [Umiejętność wroga [140804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 전부 소모
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Remove all [Laceration] Count
   PL: [OnSucceedAttack] usuwa wszystkie Liczniki [Laceration]
129. [Umiejętność wroga [140805] (ulepszenie 1) — nazwa] 소화
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140805].levelList[level=1].name
   limit: do 40 znaków
   EN: Churning
   PL: Trawienie
130. [Umiejętność wroga [140805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 3당 자신의 전체 체력의 1%만큼 회복 (최대 30%). [Laceration] 횟수 전부 소모
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Heal 1% HP for every 3 [Laceration] on target (max 30%); remove all [Laceration] Count
   PL: [OnSucceedAttack] przywraca 1% HP za każde 3 [Laceration] celu (maks. 30%); usuwa wszystkie Liczniki [Laceration]
131. [Umiejętność wroga [140901] (ulepszenie 1) — nazwa] 취하고 싶나?
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140901].levelList[level=1].name
   limit: do 40 znaków
   EN: Wanna Get Drunk?
   PL: Wanna Get Drunk?
132. [Umiejętność wroga [140901] (ulepszenie 1) — opis] 합 진행 시 [Exalted] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Exalted]
   znaczenie tagów: [Exalted] = 고양 / Morale Boost
   EN: In a Clash, apply 1 [Exalted]
   PL: podczas Starcia nakłada 1 [Exalted]
133. [Umiejętność wroga [140901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 5 [Vibration] i +2 Licznika [Vibration]
134. [Umiejętność wroga [140902] (ulepszenie 1) — nazwa] 나눠 마시자!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140902].levelList[level=1].name
   limit: do 40 znaków
   EN: Let's Share the Drink!
   PL: Let's Share the Drink!
135. [Umiejętność wroga [140902] (ulepszenie 1) — opis] 합 진행 시 [Exalted] 2 부여\n[WhenUse] 체력 5% 회복
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Exalted], [WhenUse]
   znaczenie tagów: [Exalted] = 고양 / Morale Boost; [WhenUse] = [사용시] / [On Use]
   EN: In a Clash, apply 2 [Exalted]\n[WhenUse] Heal 5% HP
   PL: podczas Starcia nakłada 2 [Exalted]\n[WhenUse] przywraca 5% HP
136. [Umiejętność wroga [140902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 2 [Binding] w następnej turze
137. [Umiejętność wroga [140903] (ulepszenie 1) — nazwa] 남은건 이것 뿐이네!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140903].levelList[level=1].name
   limit: do 40 znaków
   EN: This is All I Got!
   PL: This is All I Got!
138. [Umiejętność wroga [140903] (ulepszenie 1) — opis] 합 진행 시 [Exalted] 2 부여\n[Vibration]을 가진 대상 우선 공격
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140903].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Exalted], [Vibration]
   znaczenie tagów: [Exalted] = 고양 / Morale Boost; [Vibration] = 진동 / Tremor
   EN: In a Clash, apply 2 [Exalted]\nPrioritizes targets that have the most [Vibration]
   PL: podczas Starcia nakłada 2 [Exalted]\npriorytet: cele z największą liczbą [Vibration]
139. [Umiejętność wroga [140903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수만큼 [VibrationExplosion]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] equal to [Vibration] Count on target
   PL: [OnSucceedAttack] uruchamia tyle [VibrationExplosion], ile wynosi Licznik [Vibration] celu
140. [Umiejętność wroga [140904] (ulepszenie 1) — nazwa] 이건 내가 먹어야지!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140904].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Have This!
   PL: I'll Have This!
141. [Umiejętność wroga [140904] (ulepszenie 1) — opis] [CantDuel]\n[CantChangeTarget]\n[Exalted]을 가진 대상 우선 공격\n대상에게 [Tipsiness]가 없다면, 합 위력 +5
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140904].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [Exalted], [Tipsiness]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [Exalted] = 고양 / Morale Boost; [Tipsiness] = 취기 / Tipsy
   EN: [CantDuel]\n[CantChangeTarget]\nPrioritizes targets that have [Exalted]\nIf target has no [Tipsiness], Clash Power +5
   PL: [CantDuel]\n[CantChangeTarget]\npriorytet: cele z [Exalted]\njeżeli cel nie ma [Tipsiness], Moc Starcia +5
142. [Umiejętność wroga [140904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 [Exalted]을 가지고 있다면, [Exalted]만큼 피해량 +10%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Exalted]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Exalted] = 고양 / Morale Boost
   EN: [OnSucceedAttack] If target has [Exalted], deal +10% damage for every [Exalted]
   PL: [OnSucceedAttack] jeżeli cel ma [Exalted], zadaje +10% obrażeń za każdy [Exalted]
143. [Umiejętność wroga [140904] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 [Tipsiness]를 가지고 있다면, 주는 피해가 0이 되고 자신의 체력 -50
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140904].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Tipsiness]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Tipsiness] = 취기 / Tipsy
   EN: [OnSucceedAttack] If target has [Tipsiness], deal 0 damage, and this unit loses 50 HP
   PL: [OnSucceedAttack] jeżeli cel ma [Tipsiness], zadaje 0 obrażeń, a ta jednostka traci 50 HP
144. [Umiejętność wroga [140904] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 [Exalted] 혹은 [Tipsiness] 전부 소모
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140904].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Exalted], [Tipsiness]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Exalted] = 고양 / Morale Boost; [Tipsiness] = 취기 / Tipsy
   EN: [OnSucceedAttack] Remove all [Exalted] or [Tipsiness] on target
   PL: [OnSucceedAttack] usuwa cały [Exalted] lub [Tipsiness] celu
145. [Umiejętność wroga [140905] (ulepszenie 1) — nazwa] 이건 내가 먹어야지!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140905].levelList[level=1].name
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Umiejętność wroga [140905] (ulepszenie 1) — opis] [Exalted]을 가진 대상 우선 공격\n대상에게 [Tipsiness]가 없다면, 합 위력 +5
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140905].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Exalted], [Tipsiness]
   znaczenie tagów: [Exalted] = 고양 / Morale Boost; [Tipsiness] = 취기 / Tipsy
   EN: Prioritizes targets that have [Exalted]\nIf target has no [Tipsiness], Clash Power +5
   PL: priorytet: cele z [Exalted]\njeżeli cel nie ma [Tipsiness], Moc Starcia +5
147. [Umiejętność wroga [140905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 [Exalted]을 가지고 있다면, [Exalted]만큼 피해량 +100%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Exalted]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Exalted] = 고양 / Morale Boost
   EN: [OnSucceedAttack] If target has [Exalted], deal +100% damage for every [Exalted]
   PL: [OnSucceedAttack] jeżeli cel ma [Exalted], zadaje +100% obrażeń za każdy [Exalted]
148. [Umiejętność wroga [140905] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 [Tipsiness]를 가지고 있다면, 주는 피해가 0이 되고 자신의 체력 -50
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140905].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Umiejętność wroga [140905] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 [Exalted] 혹은 [Tipsiness] 전부 소모
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140905].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Umiejętność wroga [140906] (ulepszenie 1) — nazwa] 이번에는 안돼!
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140906].levelList[level=1].name
   limit: do 40 znaków
   EN: Not This Time!
   PL: Not This Time!
151. [Umiejętność wroga [140906] (ulepszenie 1) — opis] 요정주 우선 대상 공격
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140906].levelList[level=1].desc
   limit: do 120 znaków
   EN: Prioritizes Fairy Wine
   PL: priorytet: Fairy Wine
152. [Umiejętność wroga [140906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 요정주를 공격했다면, 다음 턴에 체력 10% 회복, [Enhancement] 2, [Agility] 2, [Protection] 2를 얻음.
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Enhancement], [Agility], [Protection]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Agility] = 신속 / Haste; [Protection] = 보호 / Protection
   EN: [OnSucceedAttack] If this unit attacked Fairy Wine, apply the following effects next turn:\n- Heal 10% HP\n- Gain 2 [Enhancement]\n- Gain 2 [Agility]\n- Gain 2 [Protection]
   PL: [OnSucceedAttack] jeżeli ta jednostka zaatakowała Fairy Wine, w następnej turze stosuje następujące efekty:\n- przywraca 10% HP\n- zyskuje 2 [Enhancement]\n- zyskuje 2 [Agility]\n- zyskuje 2 [Protection]
153. [Umiejętność wroga [140907] (ulepszenie 1) — nazwa] 이 요정주가 좋나?
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140907].levelList[level=1].name
   limit: do 40 znaków
   EN: You Like This Brew?
   PL: You Like This Brew?
154. [Umiejętność wroga [140907] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Binding] 1 얻음
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=140907].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Binding]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Binding] = 속박 / Bind
   EN: [WhenUse] Gain 1 [Binding] next turn
   PL: [WhenUse] Zyskuje 1 [Binding] w następnej turze
155. [Umiejętność wroga [141001] (ulepszenie 1) — nazwa] 손뼉치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141001].levelList[level=1].name
   limit: do 40 znaków
   EN: Clap
   PL: Clap
156. [Umiejętność wroga [141001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [Reduction]
157. [Umiejętność wroga [141002] (ulepszenie 1) — nazwa] 강한 손뼉치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141002].levelList[level=1].name
   limit: do 40 znaków
   EN: Powerful Clap
   PL: Powerful Clap
158. [Umiejętność wroga [141002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 3 [Reduction] next turn
   PL: [OnSucceedAttack] nakłada 3 [Reduction] w następnej turze
159. [Umiejętność wroga [141003] (ulepszenie 1) — nazwa] 꼬리치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141003].levelList[level=1].name
   limit: do 40 znaków
   EN: Tail Whip
   PL: Tail Whip
160. [Umiejętność wroga [141003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 1 [Vulnerable] w następnej turze
161. [Umiejętność wroga [141003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 3 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 3 [Vulnerable] w następnej turze
162. [Umiejętność wroga [141004] (ulepszenie 1) — nazwa] 주머니 압박
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141004].levelList[level=1].name
   limit: do 40 znaków
   EN: Pressing Sac
   PL: Pressing Sac
163. [Umiejętność wroga [141004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Umiejętność wroga [141005] (ulepszenie 1) — nazwa] 혈사포
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141005].levelList[level=1].name
   limit: do 40 znaków
   EN: Blood Cannon
   PL: Blood Cannon
165. [Umiejętność wroga [141005] (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상에게 부정적인 효과가 있으면, 피해량 +50%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: If target has a negative effect, deal +50% damage
   PL: jeżeli cel ma negatywny efekt, zadaje +50% obrażeń
166. [Umiejętność wroga [141005] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 20 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141005].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 20 [Laceration]
   PL: [OnSucceedAttack] nakłada 20 [Laceration]
167. [Umiejętność wroga [141006] (ulepszenie 1) — nazwa] 종혈
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141006].levelList[level=1].name
   limit: do 40 znaków
   EN: Clotting
   PL: Clotting
168. [Umiejętność wroga [141006] (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상에게 부정적인 효과가 있으면, 피해량 +100%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: If target has a negative effect, deal +100% damage
   PL: jeżeli cel ma negatywny efekt, zadaje +100% obrażeń
169. [Umiejętność wroga [141006] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 30 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141006].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 30 [Laceration]
   PL: [OnSucceedAttack] nakłada 30 [Laceration]
170. [Umiejętność wroga [141101] (ulepszenie 1) — nazwa] 손뼉치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141101].levelList[level=1].name
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Umiejętność wroga [141101] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration], [Vibration], [Sinking]의 합 5당 합 위력 +1 (최대 4)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141101].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration], [Vibration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Clash Power +1 for every 5 ([Laceration] + [Vibration] + [Sinking]) on target (max 4)
   PL: [WhenUse] Moc Starcia +1 za każde 5 (suma [Laceration] + [Vibration] + [Sinking]) celu (maks. 4)
172. [Umiejętność wroga [141101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Umiejętność wroga [141101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Umiejętność wroga [141102] (ulepszenie 1) — nazwa] 강한 손뼉치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141102].levelList[level=1].name
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Umiejętność wroga [141102] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration], [Vibration], [Sinking]의 합 5당 합 위력 +1 (최대 4)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141102].levelList[level=1].desc
   (powtórzenie elementu 171 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Umiejętność wroga [141102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3, [Vibration] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and 3 [Vibration]
   PL: [OnSucceedAttack] nakłada 3 [Laceration] i 3 [Vibration]
177. [Umiejętność wroga [141102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Umiejętność wroga [141103] (ulepszenie 1) — nazwa] 꼬리치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141103].levelList[level=1].name
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Umiejętność wroga [141103] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration], [Vibration], [Sinking]의 합 5당 기본 위력 +1 (최대 3)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141103].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration], [Vibration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Base Power +1 for every 5 ([Laceration] + [Vibration] + [Sinking]) on target (max 3)
   PL: [WhenUse] Moc Bazowa +1 za każde 5 (suma [Laceration] + [Vibration] + [Sinking]) celu (maks. 3)
180. [Umiejętność wroga [141103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3, [Vibration] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Sinking] and 3 [Vibration]
   PL: [OnSucceedAttack] nakłada 3 [Sinking] i 3 [Vibration]
181. [Umiejętność wroga [141103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Umiejętność wroga [141103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Sinking] o 2
183. [Umiejętność wroga [141103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Umiejętność wroga [141104] (ulepszenie 1) — nazwa] 주머니 압박
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141104].levelList[level=1].name
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Umiejętność wroga [141104] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration], [Vibration], [Sinking]의 합 5당 기본 위력 +1 (최대 3)
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141104].levelList[level=1].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Umiejętność wroga [141104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] uruchamia [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
187. [Umiejętność wroga [141104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Umiejętność wroga [141105] (ulepszenie 1) — nazwa] 혈사포
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141105].levelList[level=1].name
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Umiejętność wroga [141105] (ulepszenie 1) — opis] [WhenUse] 메인 타겟에게 부정적인 효과가 있으면, 합 위력 +5\n- 부정적인 효과가 없으면, 대신 합 위력 -5
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141105].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If the main target has a negative effect, Clash Power +5\n- If the main target has no negative effect, Clash Power -5 instead
   PL: [WhenUse] jeżeli główny cel ma negatywny efekt, Moc Starcia +5\n- jeżeli główny cel nie ma negatywnego efektu, zamiast tego Moc Starcia -5
190. [Umiejętność wroga [141105] (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상에게 부정적인 효과가 있으면, 피해량 +50%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Umiejętność wroga [141105] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 20 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [141105] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1회 발동. [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141105].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on target once (target loses 1 [Laceration] Count)
   PL: [OnSucceedAttack] aktywuje [Laceration] celu 1 raz (cel traci 1 Licznik [Laceration])
193. [Umiejętność wroga [141106] (ulepszenie 1) — nazwa] 종혈
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141106].levelList[level=1].name
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Umiejętność wroga [141106] (ulepszenie 1) — opis] [WhenUse] 메인 타겟에게 부정적인 효과가 있으면, 합 위력 +5\n- 부정적인 효과가 없으면, 대신 합 위력 -5
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141106].levelList[level=1].desc
   (powtórzenie elementu 189 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Umiejętność wroga [141106] (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상에게 부정적인 효과가 있으면, 피해량 +100%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Umiejętność wroga [141106] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 30 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141106].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Umiejętność wroga [141106] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1회 발동. [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141106].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 192 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Umiejętność wroga [141201] (ulepszenie 1) — nazwa] 손뼉치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141201].levelList[level=1].name
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Umiejętność wroga [141201] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration], [Vibration], [Sinking]의 합 5당 기본 위력 +2 (최대 6)\n[WhenUse] 대상에게 [PlayingWithWaterTogetherMirror]이 있으면, 합 위력 -3
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141201].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [Vibration], [Sinking], [PlayingWithWaterTogetherMirror]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking; [PlayingWithWaterTogetherMirror] = 찰박찰박 / Splish Splash
   EN: [WhenUse] Base Power +2 for every 5 ([Laceration] + [Vibration] + [Sinking]) on target (max 6)\n[WhenUse] If target has [PlayingWithWaterTogetherMirror], Clash Power -3
   PL: [WhenUse] Moc Bazowa +2 za każde 5 (suma [Laceration] + [Vibration] + [Sinking]) celu (maks. 6)\n[WhenUse] jeżeli cel ma [PlayingWithWaterTogetherMirror], Moc Starcia -3
200. [Umiejętność wroga [141201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Vibration] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and 3 [Vibration]
   PL: [OnSucceedAttack] nakłada 3 [Laceration] i 3 [Vibration]
201. [Umiejętność wroga [141201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Umiejętność wroga [141202] (ulepszenie 1) — nazwa] 강한 손뼉치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141202].levelList[level=1].name
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Umiejętność wroga [141202] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration], [Vibration], [Sinking]의 합 5당 기본 위력 +2 (최대 6)\n[WhenUse] 대상에게 [PlayingWithWaterTogetherMirror]이 있으면, 합 위력 -3
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141202].levelList[level=1].desc
   (powtórzenie elementu 199 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Umiejętność wroga [141202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5, [Vibration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and 5 [Vibration]
   PL: [OnSucceedAttack] nakłada 5 [Laceration] i 5 [Vibration]
205. [Umiejętność wroga [141202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationBleeding]로 [Switch_Vibration]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationBleeding], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationBleeding] = 진동 - 과다출혈 / Tremor - Hemorrhage; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationBleeding]
   PL: [OnSucceedAttack] Wywołuje [Switch_Vibration] do [VibrationBleeding]
206. [Umiejętność wroga [141202] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141202].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Umiejętność wroga [141203] (ulepszenie 1) — nazwa] 꼬리치기
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141203].levelList[level=1].name
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Umiejętność wroga [141203] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration], [Vibration], [Sinking]의 합 5당 코인 위력 +1 (최대 3)\n[WhenUse] 대상에게 [PlayingWithWaterTogetherMirror]이 있으면, 합 위력 -2
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141203].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [Vibration], [Sinking], [PlayingWithWaterTogetherMirror]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking; [PlayingWithWaterTogetherMirror] = 찰박찰박 / Splish Splash
   EN: [WhenUse] Coin Power +1 for every 5 ([Laceration] + [Vibration] + [Sinking]) on target (max 3)\n[WhenUse] If target has [PlayingWithWaterTogetherMirror], Clash Power -2
   PL: [WhenUse] Moc Monet +1 za każde 5 (suma [Laceration] + [Vibration] + [Sinking]) celu (maks. 3)\n[WhenUse] jeżeli cel ma [PlayingWithWaterTogetherMirror], Moc Starcia -2
209. [Umiejętność wroga [141203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5, [Vibration] 5 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Sinking] and 5 [Vibration]
   PL: [OnSucceedAttack] nakłada 5 [Sinking] i 5 [Vibration]
210. [Umiejętność wroga [141203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Umiejętność wroga [141203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 4 증가
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +4 [Sinking] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] celu o 4
212. [Umiejętność wroga [141203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Umiejętność wroga [141204] (ulepszenie 1) — nazwa] 주머니 압박
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141204].levelList[level=1].name
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Umiejętność wroga [141204] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration], [Vibration], [Sinking]의 합 5당 기본 위력 +2 (최대 6)\n[WhenUse] 대상에게 [PlayingWithWaterTogetherMirror]이 있으면, 합 위력 -2
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141204].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [Vibration], [Sinking], [PlayingWithWaterTogetherMirror]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking; [PlayingWithWaterTogetherMirror] = 찰박찰박 / Splish Splash
   EN: [WhenUse] Base Power +2 for every 5 ([Laceration] + [Vibration] + [Sinking]) on target (max 6)\n[WhenUse] If target has [PlayingWithWaterTogetherMirror], Clash Power -2
   PL: [WhenUse] Moc Bazowa +2 za każde 5 (suma [Laceration] + [Vibration] + [Sinking]) celu (maks. 6)\n[WhenUse] jeżeli cel ma [PlayingWithWaterTogetherMirror], Moc Starcia -2
215. [Umiejętność wroga [141204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VibrationBleeding]로 [Switch_Vibration]
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Umiejętność wroga [141204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Umiejętność wroga [141204] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141204].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Umiejętność wroga [141205] (ulepszenie 1) — nazwa] 혈사포
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141205].levelList[level=1].name
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Umiejętność wroga [141205] (ulepszenie 1) — opis] [WhenUse] 메인 타겟에게 부정적인 효과가 있으면, 합 위력 +10\n- 부정적인 효과가 없으면, 대신 합 위력 -10
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141205].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If the main target has a negative effect, Clash Power +10\n- If the main target has no negative effect, Clash Power -10 instead
   PL: [WhenUse] jeżeli główny cel ma negatywny efekt, Moc Starcia +10\n- jeżeli główny cel nie ma negatywnego efektu, zamiast tego Moc Starcia -10
220. [Umiejętność wroga [141205] (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상에게 부정적인 효과가 있으면, 피해량 +50%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność wroga [141205] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 20 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141205].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Umiejętność wroga [141205] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1회 발동. [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141205].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 192 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Umiejętność wroga [141206] (ulepszenie 1) — nazwa] 종혈
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141206].levelList[level=1].name
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [Umiejętność wroga [141206] (ulepszenie 1) — opis] [WhenUse] 메인 타겟에게 부정적인 효과가 있으면, 합 위력 +10\n- 부정적인 효과가 없으면, 대신 합 위력 -10
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141206].levelList[level=1].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Umiejętność wroga [141206] (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상에게 부정적인 효과가 있으면, 피해량 +100%
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność wroga [141206] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 30 부여
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141206].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność wroga [141206] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 3회 발동. [Laceration] 횟수 3 감소
   źródło: Skills_Abnormality_Mirror7-extreme.json :: dataList[id=141206].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on target 3 times (target loses 3 [Laceration] Count)
   PL: [OnSucceedAttack] aktywuje [Laceration] celu 3 razy (cel traci 3 Liczniki [Laceration])

## [podstawowe] Umiejętności wrogów / Anomalii — Skills_Enemy-schema
- grupa rozdziału/trybu: `podstawowe` · plik: `Skills_Enemy-schema.json`

228. [Umiejętność wroga [600201] (ulepszenie 1) — nazwa] 구름 걷기
   źródło: Skills_Enemy-schema.json :: dataList[id=600201].levelList[level=1].name
   limit: do 40 znaków
   EN: Cloudwalking
   PL: Cloudwalking
229. [Umiejętność wroga [600201] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-schema.json :: dataList[id=600201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 6+ [Laceration], Coin Power +1
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1
230. [Umiejętność wroga [600201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-schema.json :: dataList[id=600201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Umiejętność wroga [600201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [AttackDown] 2 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 2 [AttackDown]
   PL: [OnSucceedAttack] nakłada 2 [AttackDown]
232. [Umiejętność wroga [600201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Umiejętność wroga [600201] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여 (스킬당 1회)
   źródło: Skills_Enemy-schema.json :: dataList[id=600201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] (once per Skill)
   PL: [OnSucceedAttack] nakłada 2 [Laceration] (1 raz na Umiejętność)
234. [Umiejętność wroga [600201] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인 재사용 (스킬당 1회)
   źródło: Skills_Enemy-schema.json :: dataList[id=600201].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Reuse this Coin (once per Skill)
   PL: [UnBrokenCoinOnSucceedAttack] używa tej Monety ponownie (1 raz na Umiejętność)
235. [Umiejętność wroga [600202] (ulepszenie 1) — nazwa] 암운
   źródło: Skills_Enemy-schema.json :: dataList[id=600202].levelList[level=1].name
   limit: do 40 znaków
   EN: Gloomcloud
   PL: Gloomcloud
236. [Umiejętność wroga [600202] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-schema.json :: dataList[id=600202].levelList[level=1].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Umiejętność wroga [600202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [Umiejętność wroga [600202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Paralysis] 1 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 1 [Paralysis]
   PL: [OnSucceedAttack] nakłada 1 [Paralysis]
239. [Umiejętność wroga [600202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Umiejętność wroga [600202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가 (스킬당 1회)
   źródło: Skills_Enemy-schema.json :: dataList[id=600202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Gain +2 [Laceration] Count (once per Skill)
   PL: [OnSucceedAttack] zwiększa Licznik [Laceration] o 2 (1 raz na Umiejętność)
241. [Umiejętność wroga [600202] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인 재사용 (스킬당 1회)
   źródło: Skills_Enemy-schema.json :: dataList[id=600202].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [Umiejętność wroga [600203] (ulepszenie 1) — nazwa] 발도 자세
   źródło: Skills_Enemy-schema.json :: dataList[id=600203].levelList[level=1].name
   limit: do 40 znaków
   EN: Battō Shisei
   PL: Battō Shisei
243. [Umiejętność wroga [600203] (ulepszenie 1) — opis] [WhenUse] 자신의 정신력 5 회복\n- 체력이 50% 이하면, 대신 10 회복
   źródło: Skills_Enemy-schema.json :: dataList[id=600203].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 5 SP\n- At 50%- HP, heal 10 SP instead
   PL: [WhenUse] przywraca 5 Poczytalności\n- przy 50%- HP, zamiast tego przywraca 10 Poczytalności
244. [Umiejętność wroga [600203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [SlashTakeDamageUp] 2 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttack] Inflict 2 [SlashTakeDamageUp]
   PL: [OnSucceedAttack] nakłada 2 [SlashTakeDamageUp]
245. [Umiejętność wroga [600203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown]
   PL: [OnSucceedAttack] nakłada 2 [DefenseDown]
246. [Umiejętność wroga [600204] (ulepszenie 1) — nazwa] 쿠모기리
   źródło: Skills_Enemy-schema.json :: dataList[id=600204].levelList[level=1].name
   limit: do 40 znaków
   EN: Kumogiri
   PL: Kumogiri
247. [Umiejętność wroga [600204] (ulepszenie 1) — opis] [Laceration] 위력이 제일 높은 대상을 우선으로 타겟\n[WhenUse]\n- [SharpSensibility] 50당, 공격 가중치 +1, 코인 위력 +1\n- 피해량 +([SharpSensibility] 수치)%\n[WhenUse] 피해량 +(메인 타겟의 [Laceration] 위력)% (최대 50%)\n[DefeatDuel] [Paralysis] 3 얻음, 피해량 -75%, 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkillAll] [SharpSensibility] 전부 소모
   źródło: Skills_Enemy-schema.json :: dataList[id=600204].levelList[level=1].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [SharpSensibility], [DefeatDuel], [Paralysis], [EndSkillAll]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [SharpSensibility] = 칼질의 재미 / Delightful Swordbutchery; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze; [EndSkillAll] = [스킬 종료시] / [Skill End]
   EN: Prioritize the target that has the highest [Laceration] Potency\n[WhenUse]\n- Gain +1 Atk Weight and Coin Power +1 for every 50 [SharpSensibility]\n- Deal +([SharpSensibility] Stack)% damage\n[WhenUse] Deal +([Laceration] Potency on the main target)% damage (max 50%)\n[DefeatDuel] Gain 3 [Paralysis], deal -75% damage, and damage dealt by this Skill cannot Stagger the target\n[EndSkillAll] Consume all [SharpSensibility]
   PL: priorytet: cel z największą Siłą [Laceration]\n[WhenUse]\n- zyskuje +1 Wagi Ataku i Moc Monet +1 za każde 50 [SharpSensibility]\n- zadaje +(Siła [SharpSensibility])% obrażeń\n[WhenUse] zadaje +(Siła [Laceration] głównego celu)% obrażeń (maks. 50%)\n[DefeatDuel] zyskuje 3 [Paralysis], zadaje o 75% mniej obrażeń, a te obrażenia nie Oszołamują celu\n[EndSkillAll] zużywa cały [SharpSensibility]
248. [Umiejętność wroga [600204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Umiejętność wroga [600204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Laceration]
250. [Umiejętność wroga [600204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Umiejętność wroga [600204] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600204].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Umiejętność wroga [600204] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600204].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Umiejętność wroga [600204] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-schema.json :: dataList[id=600204].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Umiejętność wroga [600204] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 횟수가 5 이상이면, [Laceration] 2회 발동. 대상의 [Laceration] 횟수 2 감소
   źródło: Skills_Enemy-schema.json :: dataList[id=600204].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] If target has 5+ [Laceration] Count, activate [Laceration] on target 2 times. Target loses 2 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli cel ma 5+ Liczników [Laceration], aktywuje [Laceration] celu 2 razy. Cel traci 2 Liczniki [Laceration]
255. [Umiejętność wroga [600205] (ulepszenie 1) — nazwa] 아메기리
   źródło: Skills_Enemy-schema.json :: dataList[id=600205].levelList[level=1].name
   limit: do 40 znaków
   EN: Amegiri
   PL: Amegiri
256. [Umiejętność wroga [600205] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-schema.json :: dataList[id=600205].levelList[level=1].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Umiejętność wroga [600205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Umiejętność wroga [600205] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-schema.json :: dataList[id=600205].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Umiejętność wroga [600205] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [AttackDown] 3 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600205].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [AttackDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [AttackDown]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [AttackDown]
260. [Umiejętność wroga [600205] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600205].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Umiejętność wroga [600205] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600205].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Laceration]
262. [Umiejętność wroga [600205] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600205].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Umiejętność wroga [600205] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600205].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Umiejętność wroga [600205] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 횟수가 10 이상이면, [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Enemy-schema.json :: dataList[id=600205].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] If target has 10+ [Laceration] Count, activate [Laceration] on target once. Target loses 1 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli cel ma 10+ Liczników [Laceration], aktywuje [Laceration] celu 1 raz. Cel traci 1 Licznik [Laceration]
265. [Umiejętność wroga [600206] (ulepszenie 1) — nazwa] 쿠로쿠모기리
   źródło: Skills_Enemy-schema.json :: dataList[id=600206].levelList[level=1].name
   limit: do 40 znaków
   EN: Kurokumogiri
   PL: Kurokumogiri
266. [Umiejętność wroga [600206] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-schema.json :: dataList[id=600206].levelList[level=1].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Umiejętność wroga [600206] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Umiejętność wroga [600206] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600206].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Umiejętność wroga [600206] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600206].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Paralysis]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Paralysis]
270. [Umiejętność wroga [600206] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600206].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Umiejętność wroga [600206] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-schema.json :: dataList[id=600206].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Umiejętność wroga [600206] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600206].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Umiejętność wroga [600206] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-schema.json :: dataList[id=600206].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Umiejętność wroga [600206] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 횟수가 10 이상이면, [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Enemy-schema.json :: dataList[id=600206].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Umiejętność wroga [600207] (ulepszenie 1) — nazwa] 공간참[쿠로쿠모]
   źródło: Skills_Enemy-schema.json :: dataList[id=600207].levelList[level=1].name
   limit: do 40 znaków
   EN: Rend Space [Kurokumo]
   PL: Rend Space [Kurokumo]
276. [Umiejętność wroga [600207] (ulepszenie 1) — opis] [Laceration] 위력이 제일 높은 대상을 우선으로 타겟\n[WhenUse]\n- [SharpSensibility] 25당, 공격 가중치 +1\n- [SharpSensibility] 50당, 코인 위력 +1\n- 피해량 +([SharpSensibility] 수치)%\n[WhenUse] 피해량 +(메인 타겟의 [Laceration] 위력과 횟수의 합)% (최대 100%)\n[DefeatDuel] [Paralysis] 4 얻음, 피해량 -75%, 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkillAll] [SharpSensibility] 전부 소모
   źródło: Skills_Enemy-schema.json :: dataList[id=600207].levelList[level=1].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [SharpSensibility], [DefeatDuel], [Paralysis], [EndSkillAll]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [SharpSensibility] = 칼질의 재미 / Delightful Swordbutchery; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze; [EndSkillAll] = [스킬 종료시] / [Skill End]
   EN: Prioritize the target that has the highest [Laceration] Potency\n[WhenUse]\n- Gain +1 Atk Weight for every 25 [SharpSensibility]\n- Coin Power +1 for every 50 [SharpSensibility]\n- Deal +([SharpSensibility] Stack)% damage\n[WhenUse] Deal +([Laceration] Potency + [Laceration] Count on the main target)% damage (max 100%)\n[DefeatDuel] Gain 4 [Paralysis], deal -75% damage, and damage dealt by this Skill cannot Stagger the target\n[EndSkillAll] Consume all [SharpSensibility]
   PL: priorytet: cel z największą Siłą [Laceration]\n[WhenUse]\n- zyskuje +1 Wagi Ataku za każde 25 [SharpSensibility]\n- Moc Monet +1 za każde 50 [SharpSensibility]\n- zadaje +(Siła [SharpSensibility])% obrażeń\n[WhenUse] zadaje +(Siła [Laceration] + Licznik [Laceration] głównego celu)% obrażeń (maks. 100%)\n[DefeatDuel] zyskuje 4 [Paralysis], zadaje o 75% mniej obrażeń, a te obrażenia nie Oszołamują celu\n[EndSkillAll] zużywa cały [SharpSensibility]
277. [Umiejętność wroga [600207] (ulepszenie 1) — tekst klimatyczny] 흑운회 제2조장이 창시한 검술. 불완전한 참격임에도 일순, 공간을 베어낸다.
   źródło: Skills_Enemy-schema.json :: dataList[id=600207].levelList[level=1].flavor
   limit: do 220 znaków
   EN: A sword art devised by the Patriarch of Kurokumo Clan's Second Family. The stroke falls short of perfection, but for one brief instant, it cuts space itself all the same.
   PL: Sztuka miecza stworzona przez Patriarchę Drugiej Rodziny Klanu Kurokumo. Choć cięcie jest niedoskonałe, przez jedną krótką chwilę przecina jednak samą przestrzeń.
278. [Umiejętność wroga [600207] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600207].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Umiejętność wroga [600207] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600207].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 261 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Umiejętność wroga [600207] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600207].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Umiejętność wroga [600207] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-schema.json :: dataList[id=600207].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Umiejętność wroga [600207] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600207].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność wroga [600207] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-schema.json :: dataList[id=600207].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 [Laceration] i zwiększa Licznik [Laceration] o 2
284. [Umiejętność wroga [600207] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600207].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Umiejętność wroga [600207] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 횟수가 5 이상이면, [Laceration] 2회 발동. 대상의 [Laceration] 횟수 2 감소
   źródło: Skills_Enemy-schema.json :: dataList[id=600207].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Umiejętność wroga [601101] (ulepszenie 1) — nazwa] 등압추격
   źródło: Skills_Enemy-schema.json :: dataList[id=601101].levelList[level=1].name
   limit: do 40 znaków
   EN: Electromotive Pursuit
   PL: Electromotive Pursuit
287. [Umiejętność wroga [601101] (ulepszenie 1) — opis] [WhenUse] 자신의 [DogThunder] 1당, 코인 위력 +1 (최대 3)\n[WhenUse] 대상의 [Laceration]과 [Burst]의 합 5당, 피해량 +15% (최대 60%)\n[WhenUse] 대상의 [ElectricShock]이 3 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Enemy-schema.json :: dataList[id=601101].levelList[level=1].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DogThunder], [Laceration], [Burst], [ElectricShock], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DogThunder] = 번개 / Lightning; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [ElectricShock] = 감전 / Shock; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Coin Power +1 for every [DogThunder] on self (max 3)\n[WhenUse] Deal +15% damage for every 5 ([Laceration] + [Burst]) on target (max 60%)\n[WhenUse] If target has 3+ [ElectricShock], convert all Coins on this Skill to [SuperCoin]s\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Monet +1 za każdy [DogThunder] (maks. 3)\n[WhenUse] zadaje +15% obrażeń za każde 5 (suma [Laceration] + [Burst]) celu (maks. 60%)\n[WhenUse] jeżeli cel ma 3+ [ElectricShock], zamienia wszystkie Monety tej Umiejętności w [SuperCoin]y\n[DefeatDuel] zadaje o 50% mniej obrażeń, a te obrażenia nie Oszołamują celu
288. [Umiejętność wroga [601101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Burst] 5 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=601101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst] next turn
   PL: [OnSucceedAttack] nakłada 5 [Burst] w następnej turze
289. [Umiejętność wroga [601101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Burst] 횟수 4 증가
   źródło: Skills_Enemy-schema.json :: dataList[id=601101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +4 [Burst] Count next turn
   PL: [OnSucceedAttack] Zwiększa Licznik [Burst] o 4 w następnej turze
290. [Umiejętność wroga [601102] (ulepszenie 1) — nazwa] 피뢰
   źródło: Skills_Enemy-schema.json :: dataList[id=601102].levelList[level=1].name
   limit: do 40 znaków
   EN: Lightning Rod
   PL: Lightning Rod
291. [Umiejętność wroga [601102] (ulepszenie 1) — opis] [WhenUse] 자신의 [DogThunder] 1당, 코인 위력 +1 (최대 3)\n[WhenUse] 대상의 [Laceration]과 [Burst]의 합 5당, 피해량 +20% (최대 80%)\n[WhenUse] 대상의 [ElectricShock]이 3 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Enemy-schema.json :: dataList[id=601102].levelList[level=1].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DogThunder], [Laceration], [Burst], [ElectricShock], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DogThunder] = 번개 / Lightning; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [ElectricShock] = 감전 / Shock; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Coin Power +1 for every [DogThunder] on self (max 3)\n[WhenUse] Deal +20% damage for every 5 ([Laceration] + [Burst]) on target (max 80%)\n[WhenUse] If target has 3+ [ElectricShock], convert all Coins on this Skill to [SuperCoin]s\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Monet +1 za każdy [DogThunder] (maks. 3)\n[WhenUse] zadaje +20% obrażeń za każde 5 (suma [Laceration] + [Burst]) celu (maks. 80%)\n[WhenUse] jeżeli cel ma 3+ [ElectricShock], zamienia wszystkie Monety tej Umiejętności w [SuperCoin]y\n[DefeatDuel] zadaje o 50% mniej obrażeń, a te obrażenia nie Oszołamują celu
292. [Umiejętność wroga [601102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Burst] 5 부여, [Burst] 횟수 2 증가
   źródło: Skills_Enemy-schema.json :: dataList[id=601102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst] and +2 [Burst] Count next turn
   PL: [OnSucceedAttack] nakłada 5 [Burst] i +2 Licznika [Burst] w następnej turze
293. [Umiejętność wroga [601103] (ulepszenie 1) — nazwa] 적뢰
   źródło: Skills_Enemy-schema.json :: dataList[id=601103].levelList[level=1].name
   limit: do 40 znaków
   EN: Red Bolts
   PL: Red Bolts
294. [Umiejętność wroga [601103] (ulepszenie 1) — opis] [WhenUse] 자신의 [ElectricPolePower] 2당, 공격 가중치 +1 (최대 5)\n[WhenUse] 자신의 [ElectricPolePower] 1당, 최종 위력 +1, 피해량 +10% (최대 10, 100%)\n[WhenUse] 메인 타겟의 [Laceration]과 [Burst]의 합 5당, 피해량 +15% (최대 60%)\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] [ElectricPolePower] 소멸
   źródło: Skills_Enemy-schema.json :: dataList[id=601103].levelList[level=1].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ElectricPolePower], [Laceration], [Burst], [DefeatDuel], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ElectricPolePower] = 고압 방전 / High-voltage Discharge; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Gain +1 Atk Weight for every 2 [ElectricPolePower] on self (max 5)\n[WhenUse] Final Power +1 and deal +10% damage for every [ElectricPolePower] on self (max 10, max 100% respectively)\n[WhenUse] Deal +15% damage for every 5 ([Laceration] + [Burst]) on the main target (max 60%)\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] [ElectricPolePower] expires
   PL: [WhenUse] zyskuje +1 Wagi Ataku za każde 2 [ElectricPolePower] (maks. 5)\n[WhenUse] Moc Końcowa +1 i zadaje +10% obrażeń za każdy [ElectricPolePower] (maks. 10, odpowiednio maks. 100%)\n[WhenUse] zadaje +15% obrażeń za każde 5 (suma [Laceration] + [Burst]) głównego celu (maks. 60%)\n[DefeatDuel] zadaje o 50% mniej obrażeń, a te obrażenia nie Oszołamują celu\n[EndSkill] [ElectricPolePower] wygasa
295. [Umiejętność wroga [601103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=601103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Umiejętność wroga [601103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Burst] 10 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=601103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 10 [Burst] next turn
   PL: [OnSucceedAttack] nakłada 10 [Burst] w następnej turze
297. [Umiejętność wroga [601103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=601103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Umiejętność wroga [601103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Burst] 횟수 2 증가
   źródło: Skills_Enemy-schema.json :: dataList[id=601103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count next turn
   PL: [OnSucceedAttack] Zwiększa Licznik [Burst] o 2 w następnej turze
299. [Umiejętność wroga [600703] (ulepszenie 1) — nazwa] 쓰레기 처리
   źródło: Skills_Enemy-schema.json :: dataList[id=600703].levelList[level=1].name
   limit: do 40 znaków
   EN: Trash Disposal
   PL: Trash Disposal
300. [Umiejętność wroga [600703] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면, 코인 위력 +1\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Enemy-schema.json :: dataList[id=600703].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has 4+ [Laceration], Coin Power +1\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: jeżeli cel ma 4+ [Laceration], Moc Monet +1\n[DefeatDuel] obrażenia tej Umiejętności nie Oszołamują celu
301. [Umiejętność wroga [600703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-schema.json :: dataList[id=600703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Umiejętność wroga [600703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Umiejętność wroga [600703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-schema.json :: dataList[id=600703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Umiejętność wroga [600703] (ulepszenie 1) — moneta 2, efekt 3 — opis] 이 코인에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복
   źródło: Skills_Enemy-schema.json :: dataList[id=600703].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   EN: On Hit using this Coin, heal 30% of the HP damage dealt
   PL: przy trafieniu tą Monetą, przywraca HP równe 30% zadanych obrażeń HP
305. [Umiejętność wroga [600703] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttackHead] 이 코인 재사용 (스킬 당 최대 3회)
   źródło: Skills_Enemy-schema.json :: dataList[id=600703].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Reuse this Coin (3 times per Skill)
   PL: [OnSucceedAttackHead] używa Monety ponownie (do 3 razy na Umiejętność)
306. [Umiejętność wroga [600704] (ulepszenie 1) — nazwa] 333..1973
   źródło: Skills_Enemy-schema.json :: dataList[id=600704].levelList[level=1].name
   limit: do 40 znaków
   EN: 333..1973
   PL: 333..1973
307. [Umiejętność wroga [600704] (ulepszenie 1) — opis] [StartBattle] [Persistent] 4 얻음\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Enemy-schema.json :: dataList[id=600704].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Persistent], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Persistent] = 끈질김 / Persistence; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 4 [Persistent]\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: [StartBattle] zyskuje 4 [Persistent]\n[DefeatDuel] obrażenia tej Umiejętności nie Oszołamują celu
308. [Umiejętność wroga [600704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Umiejętność wroga [600704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 흐트러짐 5 회복
   źródło: Skills_Enemy-schema.json :: dataList[id=600704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 5
   PL: [OnSucceedAttack] obniża Próg Oszołomienia użytkownika o 5
310. [Umiejętność wroga [600704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Umiejętność wroga [600704] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Enemy-schema.json :: dataList[id=600704].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Bleed Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika Krwawienia
312. [Umiejętność wroga [600706] (ulepszenie 1) — nazwa] 뒷골목의 밤
   źródło: Skills_Enemy-schema.json :: dataList[id=600706].levelList[level=1].name
   limit: do 40 znaków
   EN: Night in the Backstreets
   PL: Noc w Zaułkach
313. [Umiejętność wroga [600706] (ulepszenie 1) — opis] 대상의 [Laceration]이 2 이상이면, 코인 위력 +1\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Enemy-schema.json :: dataList[id=600706].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has 2+ [Laceration], Coin Power +1\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: jeżeli cel ma 2+ [Laceration], Moc Monet +1\n[DefeatDuel] obrażenia tej Umiejętności nie Oszołamują celu
314. [Umiejętność wroga [600706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 체력 8 회복
   źródło: Skills_Enemy-schema.json :: dataList[id=600706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 8 HP
   PL: [OnSucceedAttack] przywraca 8 HP
315. [Umiejętność wroga [600706] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-schema.json :: dataList[id=600706].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Umiejętność wroga [600706] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-schema.json :: dataList[id=600706].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Umiejętność wroga [600706] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 체력 8 회복
   źródło: Skills_Enemy-schema.json :: dataList[id=600706].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Umiejętność wroga [600706] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 흐트러짐 8 회복
   źródło: Skills_Enemy-schema.json :: dataList[id=600706].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 8
   PL: [OnSucceedAttack] obniża Próg Oszołomienia użytkownika o 8
319. [Umiejętność wroga [600706] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] 대상의 [Laceration] 1 회 발동 ([Laceration] 횟수 1 감소)
   źródło: Skills_Enemy-schema.json :: dataList[id=600706].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on the target once (reduce [Laceration] Count by 1)
   PL: [OnSucceedAttack] uruchamia [Laceration] celu raz (zmniejsza Licznik [Laceration] o 1)

## [podstawowe] Umiejętności wrogów / Anomalii — Skills_Enemy
- grupa rozdziału/trybu: `podstawowe` · plik: `Skills_Enemy.json`

320. [Umiejętność wroga [9000101] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Enemy.json :: dataList[id=9000101].levelList[level=1].name
   limit: do 40 znaków
   EN: Stab
   PL: Pchnięcie
321. [Umiejętność wroga [9000102] (ulepszenie 1) — nazwa] 무력화
   źródło: Skills_Enemy.json :: dataList[id=9000102].levelList[level=1].name
   limit: do 40 znaków
   EN: Keep Down
   PL: Keep Down
322. [Umiejętność wroga [9000102] (ulepszenie 1) — opis] [OnSucceedAttack] 속박 2 부여. 최대 체력의 5%만큼 체력 회복
   źródło: Skills_Enemy.json :: dataList[id=9000102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind; Heal 5% of Max HP
   PL: [OnSucceedAttack] nakłada 2 Spętania; przywraca HP równe 5% Maks. HP
323. [Umiejętność wroga [9000201] (ulepszenie 1) — nazwa] 비열한 공격
   źródło: Skills_Enemy.json :: dataList[id=9000201].levelList[level=1].name
   limit: do 40 znaków
   EN: Sneaky Attack
   PL: Sneaky Attack
324. [Umiejętność wroga [9000201] (ulepszenie 1) — opis] [OnSucceedAttack] 다음 턴에 공격 위력 증가 1을 얻음
   źródło: Skills_Enemy.json :: dataList[id=9000201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Attack Power Up next turn
   PL: [OnSucceedAttack] zyskuje 1 Wzrost Mocy Ataku w następnej turze
325. [Umiejętność wroga [9000202] (ulepszenie 1) — nazwa] 무차별 공격
   źródło: Skills_Enemy.json :: dataList[id=9000202].levelList[level=1].name
   limit: do 40 znaków
   EN: Wild Swipe
   PL: Wild Swipe
326. [Umiejętność wroga [9000301] (ulepszenie 1) — nazwa] 상처 가르기
   źródło: Skills_Enemy.json :: dataList[id=9000301].levelList[level=1].name
   limit: do 40 znaków
   EN: Open Wound
   PL: Open Wound
327. [Umiejętność wroga [9000301] (ulepszenie 1) — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9000301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Attack Power Down next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Spadku Mocy Ataku
328. [Umiejętność wroga [9000302] (ulepszenie 1) — nazwa] 약점 간파
   źródło: Skills_Enemy.json :: dataList[id=9000302].levelList[level=1].name
   limit: do 40 znaków
   EN: Spot Vulnerability
   PL: Spot Vulnerability
329. [Umiejętność wroga [9000302] (ulepszenie 1) — opis] [OnSucceedAttack] 다음 턴에 취약 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9000302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Fragile next turn
   PL: [OnSucceedAttack] nakłada 3 Wrażliwości w następnej turze
330. [Umiejętność wroga [9100101] (ulepszenie 1) — nazwa] 울리기
   źródło: Skills_Enemy.json :: dataList[id=9100101].levelList[level=1].name
   limit: do 40 znaków
   EN: Crier
   PL: Crier
331. [Umiejętność wroga [9100102] (ulepszenie 1) — nazwa] 공격 명령
   źródło: Skills_Enemy.json :: dataList[id=9100102].levelList[level=1].name
   limit: do 40 znaków
   EN: Onslaught Command
   PL: Rozkaz Natarcia
332. [Umiejętność wroga [9100102] (ulepszenie 1) — opis] [WhenUse] 무작위 아군 1명에게 다음 턴에 공격 위력 증가 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9100102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Apply 1 Attack Power Up to a random ally next turn
   PL: [WhenUse] nakłada 1 Wzrost Mocy Ataku na losowego sojusznika w następnej turze
333. [Umiejętność wroga [9100103] (ulepszenie 1) — nazwa] 방어 명령
   źródło: Skills_Enemy.json :: dataList[id=9100103].levelList[level=1].name
   limit: do 40 znaków
   EN: Rampart Command
   PL: Rampart Command
334. [Umiejętność wroga [9100103] (ulepszenie 1) — opis] [2xPostLine]\n[WhenUse] 무작위 아군 2명에게 다음 턴에 수비 위력 증가 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100103].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [2xPostLine]\n[WhenUse] Give 2 Defense Power Up to 2 random allies next turn
   PL: [2xPostLine]\n[WhenUse] nakłada 2 Wzrost Mocy Obrony na 2 losowych sojuszników w następnej turze
335. [Umiejętność wroga [9100104] (ulepszenie 1) — nazwa] 정신 파동
   źródło: Skills_Enemy.json :: dataList[id=9100104].levelList[level=1].name
   limit: do 40 znaków
   EN: Mind Wave
   PL: Mind Wave
336. [Umiejętność wroga [9100104] (ulepszenie 1) — opis] [5xPostLine]\n[OnSucceedAttack] 대상의 정신력 20 감소
   źródło: Skills_Enemy.json :: dataList[id=9100104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [5xPostLine]\n[OnSucceedAttack] Target loses 20 SP
   PL: [5xPostLine]\n[OnSucceedAttack] cel traci 20 Poczytalności
337. [Umiejętność wroga [9000401] (ulepszenie 1) — nazwa] 어설픈 베기
   źródło: Skills_Enemy.json :: dataList[id=9000401].levelList[level=1].name
   limit: do 40 znaków
   EN: Clumsy Chop
   PL: Clumsy Chop
338. [Umiejętność wroga [9000501] (ulepszenie 1) — nazwa] 서투른 찌르기
   źródło: Skills_Enemy.json :: dataList[id=9000501].levelList[level=1].name
   limit: do 40 znaków
   EN: Clunky Stab
   PL: Clunky Stab
339. [Umiejętność wroga [9000601] (ulepszenie 1) — nazwa] 싱거운 타격
   źródło: Skills_Enemy.json :: dataList[id=9000601].levelList[level=1].name
   limit: do 40 znaków
   EN: Weak Blow
   PL: Weak Blow
340. [Umiejętność wroga [9000701] (ulepszenie 1) — nazwa] 타격
   źródło: Skills_Enemy.json :: dataList[id=9000701].levelList[level=1].name
   limit: do 40 znaków
   EN: Hit
   PL: Obuch
341. [Umiejętność wroga [9000702] (ulepszenie 1) — nazwa] 묵직한 일격
   źródło: Skills_Enemy.json :: dataList[id=9000702].levelList[level=1].name
   limit: do 40 znaków
   EN: Heavy Strike
   PL: Heavy Strike
342. [Umiejętność wroga [9000703] (ulepszenie 1) — nazwa] 막기
   źródło: Skills_Enemy.json :: dataList[id=9000703].levelList[level=1].name
   limit: do 40 znaków
   EN: Block
   PL: Block
343. [Umiejętność wroga [9000801] (ulepszenie 1) — nazwa] 후리기
   źródło: Skills_Enemy.json :: dataList[id=9000801].levelList[level=1].name
   limit: do 40 znaków
   EN: Sweep
   PL: Sweep
344. [Umiejętność wroga [9000802] (ulepszenie 1) — nazwa] 연속 방어
   źródło: Skills_Enemy.json :: dataList[id=9000802].levelList[level=1].name
   limit: do 40 znaków
   EN: Multi-block
   PL: Multi-block
345. [Umiejętność wroga [9000901] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Enemy.json :: dataList[id=9000901].levelList[level=1].name
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Umiejętność wroga [9000902] (ulepszenie 1) — nazwa] 연속 찌르기
   źródło: Skills_Enemy.json :: dataList[id=9000902].levelList[level=1].name
   limit: do 40 znaków
   EN: Quick Jabs
   PL: Quick Jabs
347. [Umiejętność wroga [9001001] (ulepszenie 1) — nazwa] 베기
   źródło: Skills_Enemy.json :: dataList[id=9001001].levelList[level=1].name
   limit: do 40 znaków
   EN: Swipe
   PL: Zamach
348. [Umiejętność wroga [9001002] (ulepszenie 1) — nazwa] 가르기
   źródło: Skills_Enemy.json :: dataList[id=9001002].levelList[level=1].name
   limit: do 40 znaków
   EN: Slice
   PL: Slice
349. [Umiejętność wroga [9001101] (ulepszenie 1) — nazwa] 후리기
   źródło: Skills_Enemy.json :: dataList[id=9001101].levelList[level=1].name
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Umiejętność wroga [9001101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9001101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bind next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze 1 Spętania
351. [Umiejętność wroga [9001102] (ulepszenie 1) — nazwa] 연속 방어
   źródło: Skills_Enemy.json :: dataList[id=9001102].levelList[level=1].name
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Umiejętność wroga [9001201] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Enemy.json :: dataList[id=9001201].levelList[level=1].name
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Umiejętność wroga [9001202] (ulepszenie 1) — nazwa] 연속 찌르기
   źródło: Skills_Enemy.json :: dataList[id=9001202].levelList[level=1].name
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Umiejętność wroga [9001301] (ulepszenie 1) — nazwa] 베기
   źródło: Skills_Enemy.json :: dataList[id=9001301].levelList[level=1].name
   (powtórzenie elementu 347 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Umiejętność wroga [9001302] (ulepszenie 1) — nazwa] 가르기
   źródło: Skills_Enemy.json :: dataList[id=9001302].levelList[level=1].name
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Umiejętność wroga [9001302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 횟수 3 증가
   źródło: Skills_Enemy.json :: dataList[id=9001302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +3 Rupture Count next turn
   PL: [OnSucceedAttackHead] zwiększa Licznik Rozdarcia o 3 w następnej turze
357. [Umiejętność wroga [9000103] (ulepszenie 1) — nazwa] 후리기
   źródło: Skills_Enemy.json :: dataList[id=9000103].levelList[level=1].name
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Umiejętność wroga [9000103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9000103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Umiejętność wroga [9000104] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy.json :: dataList[id=9000104].levelList[level=1].name
   limit: do 40 znaków
   EN: Guard
   PL: Garda
360. [Umiejętność wroga [9000203] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Enemy.json :: dataList[id=9000203].levelList[level=1].name
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Umiejętność wroga [9000204] (ulepszenie 1) — nazwa] 연속 찌르기
   źródło: Skills_Enemy.json :: dataList[id=9000204].levelList[level=1].name
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Umiejętność wroga [9000204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9000204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Bleed Count
   PL: [OnSucceedAttackHead] Nakłada +1 Licznika Krwawienia
363. [Umiejętność wroga [9000204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9000204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Umiejętność wroga [9000204] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9000204].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
365. [Umiejętność wroga [9000303] (ulepszenie 1) — nazwa] 베기
   źródło: Skills_Enemy.json :: dataList[id=9000303].levelList[level=1].name
   (powtórzenie elementu 347 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Umiejętność wroga [9000304] (ulepszenie 1) — nazwa] 가르기
   źródło: Skills_Enemy.json :: dataList[id=9000304].levelList[level=1].name
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Umiejętność wroga [9000304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 횟수 3 증가
   źródło: Skills_Enemy.json :: dataList[id=9000304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Umiejętność wroga [9001401] (ulepszenie 1) — nazwa] 후리기
   źródło: Skills_Enemy.json :: dataList[id=9001401].levelList[level=1].name
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Umiejętność wroga [9001401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9001401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Bind next turn
   PL: [OnSucceedAttackHead] nakłada 3 Spętania w następnej turze
370. [Umiejętność wroga [9001402] (ulepszenie 1) — nazwa] 연속 방어
   źródło: Skills_Enemy.json :: dataList[id=9001402].levelList[level=1].name
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Umiejętność wroga [9001501] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Enemy.json :: dataList[id=9001501].levelList[level=1].name
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Umiejętność wroga [9001502] (ulepszenie 1) — nazwa] 연속 찌르기
   źródło: Skills_Enemy.json :: dataList[id=9001502].levelList[level=1].name
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Umiejętność wroga [9001502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9001502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Umiejętność wroga [9001502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9001502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [Umiejętność wroga [9001502] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9001502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Umiejętność wroga [9001601] (ulepszenie 1) — nazwa] 베기
   źródło: Skills_Enemy.json :: dataList[id=9001601].levelList[level=1].name
   (powtórzenie elementu 347 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [Umiejętność wroga [9001602] (ulepszenie 1) — nazwa] 가르기
   źródło: Skills_Enemy.json :: dataList[id=9001602].levelList[level=1].name
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Umiejętność wroga [9001602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 횟수 3 증가
   źródło: Skills_Enemy.json :: dataList[id=9001602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Umiejętność wroga [9001603] (ulepszenie 1) — nazwa] 연속 방어
   źródło: Skills_Enemy.json :: dataList[id=9001603].levelList[level=1].name
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Umiejętność wroga [9100105] (ulepszenie 1) — nazwa] 울리기
   źródło: Skills_Enemy.json :: dataList[id=9100105].levelList[level=1].name
   (powtórzenie elementu 330 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [Umiejętność wroga [9100106] (ulepszenie 1) — nazwa] 방어 명령
   źródło: Skills_Enemy.json :: dataList[id=9100106].levelList[level=1].name
   (powtórzenie elementu 333 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Umiejętność wroga [9100106] (ulepszenie 1) — opis] [WhenUse] 무작위 아군 2명에게 다음 턴에 보호 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9100106].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Apply 1 Protection to 2 random allies next turn
   PL: [WhenUse] nakłada 1 Ochrony na 2 losowych sojuszników w następnej turze
383. [Umiejętność wroga [9100108] (ulepszenie 1) — nazwa] 단단함
   źródło: Skills_Enemy.json :: dataList[id=9100108].levelList[level=1].name
   limit: do 40 znaków
   EN: Harden
   PL: Wytrzymałość
384. [Umiejętność wroga [9100109] (ulepszenie 1) — nazwa] 공격 명령
   źródło: Skills_Enemy.json :: dataList[id=9100109].levelList[level=1].name
   (powtórzenie elementu 331 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Umiejętność wroga [9100109] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 횟수 5 증가
   źródło: Skills_Enemy.json :: dataList[id=9100109].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +5 Rupture Count next turn
   PL: [OnSucceedAttackHead] zwiększa Licznik Rozdarcia o 5 w następnej turze
386. [Umiejętność wroga [9100201] (ulepszenie 1) — nazwa] 울리기
   źródło: Skills_Enemy.json :: dataList[id=9100201].levelList[level=1].name
   (powtórzenie elementu 330 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Umiejętność wroga [9100201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 대상의 정신력 -5
   źródło: Skills_Enemy.json :: dataList[id=9100201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Target loses 5 SP
   PL: [OnSucceedAttackHead] cel traci 5 Poczytalności
388. [Umiejętność wroga [9100201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 대상의 정신력 -5
   źródło: Skills_Enemy.json :: dataList[id=9100201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność wroga [9100202] (ulepszenie 1) — nazwa] 공격 명령
   źródło: Skills_Enemy.json :: dataList[id=9100202].levelList[level=1].name
   (powtórzenie elementu 331 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Umiejętność wroga [9100202] (ulepszenie 1) — opis] [WhenUse] 무작위 아군 2명에게 다음 턴에 피해량 증가 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9100202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Apply 1 Damage Up to 2 random allies next turn
   PL: [WhenUse] nakłada 1 Wzrost Obrażeń na 2 losowych sojuszników w następnej turze
391. [Umiejętność wroga [9100202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 횟수 5 증가
   źródło: Skills_Enemy.json :: dataList[id=9100202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Umiejętność wroga [9100203] (ulepszenie 1) — nazwa] 정신 파동
   źródło: Skills_Enemy.json :: dataList[id=9100203].levelList[level=1].name
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Umiejętność wroga [9100203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 대상의 정신력 -15
   źródło: Skills_Enemy.json :: dataList[id=9100203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Target loses 15 SP
   PL: [OnSucceedAttackHead] cel traci 15 Poczytalności
394. [Umiejętność wroga [9100204] (ulepszenie 1) — nazwa] 단단함
   źródło: Skills_Enemy.json :: dataList[id=9100204].levelList[level=1].name
   (powtórzenie elementu 383 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Umiejętność wroga [9100205] (ulepszenie 1) — nazwa] 방어 명령
   źródło: Skills_Enemy.json :: dataList[id=9100205].levelList[level=1].name
   (powtórzenie elementu 333 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność wroga [9100205] (ulepszenie 1) — opis] [WhenUse] 무작위 아군 2명에게 다음 턴에 보호 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9100205].levelList[level=1].desc
   (powtórzenie elementu 382 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Umiejętność wroga [9100205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 대상의 정신력 -5
   źródło: Skills_Enemy.json :: dataList[id=9100205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Umiejętność wroga [9001701] (ulepszenie 1) — nazwa] 휘두르기
   źródło: Skills_Enemy.json :: dataList[id=9001701].levelList[level=1].name
   limit: do 40 znaków
   EN: Swipe
   PL: Swipe
399. [Umiejętność wroga [9001702] (ulepszenie 1) — nazwa] 비열한 타격
   źródło: Skills_Enemy.json :: dataList[id=9001702].levelList[level=1].name
   limit: do 40 znaków
   EN: Sneaky Bash
   PL: Sneaky Bash
400. [Umiejętność wroga [9001702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9001702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Umiejętność wroga [9001702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9001702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Umiejętność wroga [9001703] (ulepszenie 1) — nazwa] 작은 소망
   źródło: Skills_Enemy.json :: dataList[id=9001703].levelList[level=1].name
   limit: do 40 znaków
   EN: Wee Wish
   PL: Wee Wish
403. [Umiejętność wroga [9001703] (ulepszenie 1) — opis] [StartBattle] 두번째 슬롯 스킬의 모든 코인이 앞면이 나옴
   źródło: Skills_Enemy.json :: dataList[id=9001703].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Every Coin of the skill in the 2nd slot lands Heads
   PL: [StartBattle] wszystkie Monety Umiejętności na 2. slocie wypadają jako Awers
404. [Umiejętność wroga [9001801] (ulepszenie 1) — nazwa] 내려베기
   źródło: Skills_Enemy.json :: dataList[id=9001801].levelList[level=1].name
   limit: do 40 znaków
   EN: Pipe Down
   PL: Cięcie w Dół
405. [Umiejętność wroga [9001802] (ulepszenie 1) — nazwa] 육중한 참격
   źródło: Skills_Enemy.json :: dataList[id=9001802].levelList[level=1].name
   limit: do 40 znaków
   EN: Heavy Swing
   PL: Heavy Swing
406. [Umiejętność wroga [9001802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9001802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Umiejętność wroga [9001802] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9001802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Umiejętność wroga [9001803] (ulepszenie 1) — nazwa] 작은 소망
   źródło: Skills_Enemy.json :: dataList[id=9001803].levelList[level=1].name
   (powtórzenie elementu 402 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Umiejętność wroga [9001803] (ulepszenie 1) — opis] [StartBattle] 두번째 슬롯 스킬의 모든 코인이 앞면이 나옴
   źródło: Skills_Enemy.json :: dataList[id=9001803].levelList[level=1].desc
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Umiejętność wroga [9001901] (ulepszenie 1) — nazwa] 쑤시기
   źródło: Skills_Enemy.json :: dataList[id=9001901].levelList[level=1].name
   limit: do 40 znaków
   EN: Carve
   PL: Carve
411. [Umiejętność wroga [9001902] (ulepszenie 1) — nazwa] 야비한 찌르기
   źródło: Skills_Enemy.json :: dataList[id=9001902].levelList[level=1].name
   limit: do 40 znaków
   EN: Cunning Stab
   PL: Cunning Stab
412. [Umiejętność wroga [9001902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9001902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL: [OnSucceedAttackHead] Nakłada 2 Rozdarcia
413. [Umiejętność wroga [9001903] (ulepszenie 1) — nazwa] 작은 소망
   źródło: Skills_Enemy.json :: dataList[id=9001903].levelList[level=1].name
   (powtórzenie elementu 402 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Umiejętność wroga [9001903] (ulepszenie 1) — opis] [StartBattle] 두번째 슬롯 스킬의 모든 코인이 앞면이 나옴
   źródło: Skills_Enemy.json :: dataList[id=9001903].levelList[level=1].desc
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Umiejętność wroga [9001904] (ulepszenie 1) — nazwa] 막기
   źródło: Skills_Enemy.json :: dataList[id=9001904].levelList[level=1].name
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Umiejętność wroga [9100301] (ulepszenie 1) — nazwa] 목긋기
   źródło: Skills_Enemy.json :: dataList[id=9100301].levelList[level=1].name
   limit: do 40 znaków
   EN: Throat Slit
   PL: Throat Slit
417. [Umiejętność wroga [9100301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 출혈 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9100301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Bleed next turn
   PL: [OnSucceedAttackHead] nakłada 3 Krwawienia w następnej turze
418. [Umiejętność wroga [9100302] (ulepszenie 1) — nazwa] 후비기
   źródło: Skills_Enemy.json :: dataList[id=9100302].levelList[level=1].name
   limit: do 40 znaków
   EN: Shank
   PL: Dźgnięcie
419. [Umiejętność wroga [9100302] (ulepszenie 1) — opis] [BeforeAttack] 대상의 체력이 50% 미만이면, 스킬의 1,2 코인이 추가됨
   źródło: Skills_Enemy.json :: dataList[id=9100302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] If target has less than 50% HP, use Coin 1 and 2 an additional time
   PL: [BeforeAttack] jeżeli cel ma mniej niż 50% HP, używa Monet 1 i 2 dodatkowy raz
420. [Umiejętność wroga [9100302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture next turn
   PL: [OnSucceedAttackHead] nakłada 2 Rozdarcia w następnej turze
421. [Umiejętność wroga [9100302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 파열 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Umiejętność wroga [9100303] (ulepszenie 1) — nazwa] 난도질
   źródło: Skills_Enemy.json :: dataList[id=9100303].levelList[level=1].name
   limit: do 40 znaków
   EN: Mutilate
   PL: Okaleczenie
423. [Umiejętność wroga [9100303] (ulepszenie 1) — opis] [EnemyKill] 이 스킬 1회 재사용
   źródło: Skills_Enemy.json :: dataList[id=9100303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Use this skill 1 more time
   PL: [EnemyKill] Używa tej Umiejętności dodatkowo 1 raz
424. [Umiejętność wroga [9100303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 대상에게 피해 3
   źródło: Skills_Enemy.json :: dataList[id=9100303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Deal 3 damage
   PL: [OnSucceedAttackHead] zadaje 3 obrażenia
425. [Umiejętność wroga [9100303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 대상에게 피해 3
   źródło: Skills_Enemy.json :: dataList[id=9100303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Umiejętność wroga [9100303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 대상에게 피해 3
   źródło: Skills_Enemy.json :: dataList[id=9100303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Umiejętność wroga [9100304] (ulepszenie 1) — nazwa] 본 때를 보여주마...!
   źródło: Skills_Enemy.json :: dataList[id=9100304].levelList[level=1].name
   limit: do 40 znaków
   EN: I’ll Show You…!
   PL: I’ll Show You…!
428. [Umiejętność wroga [9100304] (ulepszenie 1) — opis] [StartBattle] 공격 위력 증가 1를 얻음
   źródło: Skills_Enemy.json :: dataList[id=9100304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 1 Attack Power Up
   PL: [StartBattle] zyskuje 1 Wzrost Mocy Ataku
429. [Umiejętność wroga [9100305] (ulepszenie 1) — nazwa] 번뜩이는 소망
   źródło: Skills_Enemy.json :: dataList[id=9100305].levelList[level=1].name
   limit: do 40 znaków
   EN: Glinting Wish
   PL: Glinting Wish
430. [Umiejętność wroga [9100305] (ulepszenie 1) — opis] [StartBattle] 이번 턴에 모든 코인이 반드시 앞면이 나옴
   źródło: Skills_Enemy.json :: dataList[id=9100305].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] All Coins land Heads this turn
   PL: [StartBattle] wszystkie Monety wypadają jako Awers w tej turze
431. [Umiejętność wroga [9100306] (ulepszenie 1) — nazwa] 꺼져!
   źródło: Skills_Enemy.json :: dataList[id=9100306].levelList[level=1].name
   limit: do 40 znaków
   EN: Buzz Off!
   PL: Spadaj!
432. [Umiejętność wroga [9002001] (ulepszenie 1) — nazwa] 침입자 발견!
   źródło: Skills_Enemy.json :: dataList[id=9002001].levelList[level=1].name
   limit: do 40 znaków
   EN: Intruder Alert!
   PL: Intruder Alert!
433. [Umiejętność wroga [9002001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9002001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Umiejętność wroga [9002002] (ulepszenie 1) — nazwa] 꼼짝마!
   źródło: Skills_Enemy.json :: dataList[id=9002002].levelList[level=1].name
   limit: do 40 znaków
   EN: Freeze!
   PL: Freeze!
435. [Umiejętność wroga [9002002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 더하기 코인 약화 4 부여
   źródło: Skills_Enemy.json :: dataList[id=9002002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Plus Coin Drop next turn
   PL: [OnSucceedAttack] nakłada 4 Osłabienia Monety Plus w następnej turze
436. [Umiejętność wroga [9002003] (ulepszenie 1) — nazwa] 가만히 있어!
   źródło: Skills_Enemy.json :: dataList[id=9002003].levelList[level=1].name
   limit: do 40 znaków
   EN: Hold It Right There!
   PL: Hold It Right There!
437. [Umiejętność wroga [9002003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 위력 감소 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9002003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Power Down next turn
   PL: [OnSucceedAttack] nakłada 1 Spadek Mocy w następnej turze
438. [Umiejętność wroga [9002003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 위력 감소 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9002003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Umiejętność wroga [9002101] (ulepszenie 1) — nazwa] 아플거다!
   źródło: Skills_Enemy.json :: dataList[id=9002101].levelList[level=1].name
   limit: do 40 znaków
   EN: This’ll Hurt!
   PL: This’ll Hurt!
440. [Umiejętność wroga [9002101] (ulepszenie 1) — opis] [WinDuel] 스킬 위력 +1
   źródło: Skills_Enemy.json :: dataList[id=9002101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Skill Power +1
   PL: [WinDuel] Moc Umiejętności +1
441. [Umiejętność wroga [9002301] (ulepszenie 1) — nazwa] 침입자 포착
   źródło: Skills_Enemy.json :: dataList[id=9002301].levelList[level=1].name
   limit: do 40 znaków
   EN: Interloper Spotted
   PL: Interloper Spotted
442. [Umiejętność wroga [9002301] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9002301].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bind next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 3 Spętania
443. [Umiejętność wroga [9002302] (ulepszenie 1) — nazwa] 견제
   źródło: Skills_Enemy.json :: dataList[id=9002302].levelList[level=1].name
   limit: do 40 znaków
   EN: Wary Move
   PL: Uważne Powstrzymywanie
444. [Umiejętność wroga [9002302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9002302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Paralyze next turn
   PL: [OnSucceedAttack] Nakłada 1 Paraliżu w następnej turze
445. [Umiejętność wroga [9002303] (ulepszenie 1) — nazwa] 무차별 제압
   źródło: Skills_Enemy.json :: dataList[id=9002303].levelList[level=1].name
   limit: do 40 znaków
   EN: Wide Arrest
   PL: Wide Arrest
446. [Umiejętność wroga [9002303] (ulepszenie 1) — opis] [WinDuel] 스킬 위력 + 2
   źródło: Skills_Enemy.json :: dataList[id=9002303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Skill Power +2
   PL: [WinDuel] Moc Umiejętności +2
447. [Umiejętność wroga [9002303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9002303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze next turn
   PL: [OnSucceedAttack] nakłada 3 Paraliżu w następnej turze
448. [Umiejętność wroga [9002304] (ulepszenie 1) — nazwa] 어림 없지
   źródło: Skills_Enemy.json :: dataList[id=9002304].levelList[level=1].name
   limit: do 40 znaków
   EN: Not a Chance
   PL: Not a Chance
449. [Umiejętność wroga [9002401] (ulepszenie 1) — nazwa] 춤을 춥시다~
   źródło: Skills_Enemy.json :: dataList[id=9002401].levelList[level=1].name
   limit: do 40 znaków
   EN: Bailemos~
   PL: Bailemos~
450. [Umiejętność wroga [9002401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 정신력 2 회복
   źródło: Skills_Enemy.json :: dataList[id=9002401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 2 SP
   PL: [OnSucceedAttack] przywraca 2 SP
451. [Umiejętność wroga [9002401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 정신력 2 회복
   źródło: Skills_Enemy.json :: dataList[id=9002401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Umiejętność wroga [9002401] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 정신력 2 회복
   źródło: Skills_Enemy.json :: dataList[id=9002401].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Umiejętność wroga [9002402] (ulepszenie 1) — nazwa] 평화의 춤
   źródło: Skills_Enemy.json :: dataList[id=9002402].levelList[level=1].name
   limit: do 40 znaków
   EN: Danza de Paz
   PL: Danza de Paz
454. [Umiejętność wroga [9002402] (ulepszenie 1) — opis] [WhenUse] 모든 아군에게 다음 턴에 수비 위력 증가 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9002402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Apply 1 Defense Power Up to all allies next turn
   PL: [WhenUse] nakłada 1 Wzrost Mocy Obrony na wszystkich sojuszników w następnej turze
455. [Umiejętność wroga [9002403] (ulepszenie 1) — nazwa] 댄스 대결
   źródło: Skills_Enemy.json :: dataList[id=9002403].levelList[level=1].name
   limit: do 40 znaków
   EN: Duelo de Baile
   PL: Duelo de Baile
456. [Umiejętność wroga [9002403] (ulepszenie 1) — opis] [WinDuel] 대상의 정신력 -5
   źródło: Skills_Enemy.json :: dataList[id=9002403].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Target loses 5 SP
   PL: [WinDuel] cel traci 5 Poczytalności
457. [Umiejętność wroga [9002403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9002403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Attack Power Down next turn
   PL: [OnSucceedAttack] nakłada 2 [Reduction] następnej tury
458. [Umiejętność wroga [9002404] (ulepszenie 1) — nazwa] 흥겨운 찌르기
   źródło: Skills_Enemy.json :: dataList[id=9002404].levelList[level=1].name
   limit: do 40 znaków
   EN: Puñales Joviales
   PL: Puñales Joviales
459. [Umiejętność wroga [9002404] (ulepszenie 1) — opis] 정신력이 0 미만인 대상 공격 시 스킬 위력 +1
   źródło: Skills_Enemy.json :: dataList[id=9002404].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target’s SP is below 0, Skill Power +1
   PL: jeżeli Poczytalność celu jest poniżej 0, Moc Umiejętności +1
460. [Umiejętność wroga [9002405] (ulepszenie 1) — nazwa] 올레!
   źródło: Skills_Enemy.json :: dataList[id=9002405].levelList[level=1].name
   limit: do 40 znaków
   EN: ¡Olé!
   PL: ¡Olé!
461. [Umiejętność wroga [9002405] (ulepszenie 1) — opis] [OnSucceedEvade] 대상의 정신력 -5
   źródło: Skills_Enemy.json :: dataList[id=9002405].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Target loses 5 SP
   PL: [OnSucceedEvade] cel traci 5 Poczytalności
462. [Umiejętność wroga [9002502] (ulepszenie 1) — nazwa] 정열의 춤
   źródło: Skills_Enemy.json :: dataList[id=9002502].levelList[level=1].name
   limit: do 40 znaków
   EN: Danza de Emoción
   PL: Danza de Emoción
463. [Umiejętność wroga [9002502] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 공격 위력 증가 1을 얻음
   źródło: Skills_Enemy.json :: dataList[id=9002502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Attack Power Up next turn
   PL: [WhenUse] zyskuje 1 Wzrost Mocy Ataku w następnej turze
464. [Umiejętność wroga [9100401] (ulepszenie 1) — nazwa] 격정의 춤사위
   źródło: Skills_Enemy.json :: dataList[id=9100401].levelList[level=1].name
   limit: do 40 znaków
   EN: Pasos Pasionales
   PL: Pasos Pasionales
465. [Umiejętność wroga [9100401] (ulepszenie 1) — opis] [WhenUse] 정신력 5 회복
   źródło: Skills_Enemy.json :: dataList[id=9100401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 5 SP
   PL: [WhenUse] przywraca 5 Poczytalności
466. [Umiejętność wroga [9100401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 1 얻음
   źródło: Skills_Enemy.json :: dataList[id=9100401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Poise next turn
   PL: [OnSucceedAttack] Zyskuje 1 Oddech w następnej turze
467. [Umiejętność wroga [9100401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 1 얻음
   źródło: Skills_Enemy.json :: dataList[id=9100401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Umiejętność wroga [9100401] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 1 얻음
   źródło: Skills_Enemy.json :: dataList[id=9100401].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Umiejętność wroga [9100401] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 1 얻음
   źródło: Skills_Enemy.json :: dataList[id=9100401].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Umiejętność wroga [9100402] (ulepszenie 1) — nazwa] 이거 밖에 안돼?
   źródło: Skills_Enemy.json :: dataList[id=9100402].levelList[level=1].name
   limit: do 40 znaków
   EN: ¿Eso es todo?
   PL: ¿Eso es todo?
471. [Umiejętność wroga [9100402] (ulepszenie 1) — opis] [WinDuel] 대상에게 정신 피해 10
   źródło: Skills_Enemy.json :: dataList[id=9100402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Deal 10 SP damage
   PL: [WinDuel] zadaje 10 obrażeń Poczytalności
472. [Umiejętność wroga [9100402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소, 마비 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9100402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Attack Power Down and Paralyze next turn
   PL: [OnSucceedAttack] nakłada 3 Spadku Mocy Ataku i 3 Paraliżu w następnej turze
473. [Umiejętność wroga [9100403] (ulepszenie 1) — nazwa] 날카롭게!
   źródło: Skills_Enemy.json :: dataList[id=9100403].levelList[level=1].name
   limit: do 40 znaków
   EN: ¡Bruscamente!
   PL: ¡Bruscamente!
474. [Umiejętność wroga [9100403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 증가 2를 얻음
   źródło: Skills_Enemy.json :: dataList[id=9100403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 Attack Power Up next turn
   PL: [OnSucceedAttack] zyskuje 2 Wzrost Mocy Ataku w następnej turze
475. [Umiejętność wroga [9100404] (ulepszenie 1) — nazwa] 날렵하게~
   źródło: Skills_Enemy.json :: dataList[id=9100404].levelList[level=1].name
   limit: do 40 znaków
   EN: Rápidamente~
   PL: Rápidamente~
476. [Umiejętność wroga [9100404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 수비 위력 증가 2를 얻음
   źródło: Skills_Enemy.json :: dataList[id=9100404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 Defense Power Up next turn
   PL: [OnSucceedAttack] zyskuje 2 Wzrost Mocy Obrony w następnej turze
477. [Umiejętność wroga [9100405] (ulepszenie 1) — nazwa] 파냐타 파티~!
   źródło: Skills_Enemy.json :: dataList[id=9100405].levelList[level=1].name
   limit: do 40 znaków
   EN: Pañata Party~!
   PL: Pañata Party~!
478. [Umiejętność wroga [9100405] (ulepszenie 1) — opis] [WhenUse] 정신력이 0미만인 적 공격 시 대상의 정신력에 비례하여 크리티컬 발동 확률 증가
   źródło: Skills_Enemy.json :: dataList[id=9100405].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target’s SP is below 0, crit chance increases in proportion to target’s SP
   PL: [WhenUse] jeżeli Poczytalność celu jest poniżej 0, szansa trafienia krytycznego rośnie proporcjonalnie do niej
479. [Umiejętność wroga [9100405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 피해량의 50% 만큼 흐트러짐 회복
   źródło: Skills_Enemy.json :: dataList[id=9100405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Lower user’s Stagger Threshold by 50% of damage dealt
   PL: [OnSucceedAttackHead] obniża swój Próg Oszołomienia o 50% zadanych obrażeń
480. [Umiejętność wroga [9100406] (ulepszenie 1) — nazwa] 엑셀렌떼!
   źródło: Skills_Enemy.json :: dataList[id=9100406].levelList[level=1].name
   limit: do 40 znaków
   EN: ¡Excelente!
   PL: ¡Excelente!
481. [Umiejętność wroga [9100406] (ulepszenie 1) — opis] [OnSucceedEvade] 흐트러짐 회복 5. 대상에게 정신 피해 5
   źródło: Skills_Enemy.json :: dataList[id=9100406].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Lower user’s Stagger Threshold by 5; Deal 5 SP damage
   PL: [OnSucceedEvade] obniża swój Próg Oszołomienia o 5; zadaje 5 obrażeń Poczytalności
482. [Umiejętność wroga [9002601] (ulepszenie 1) — nazwa] 확 찢어불랑게
   źródło: Skills_Enemy.json :: dataList[id=9002601].levelList[level=1].name
   limit: do 40 znaków
   EN: I’ll Tear Ya Apart
   PL: I’ll Tear Ya Apart
483. [Umiejętność wroga [9002601] (ulepszenie 1) — opis] 대상의 정신력이 자신보다 낮으면 스킬 위력 +1
   źródło: Skills_Enemy.json :: dataList[id=9002601].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target’s SP is lower than user’s, Skill Power +1
   PL: jeżeli Poczytalność celu jest niższa niż własna, Moc Umiejętności +1
484. [Umiejętność wroga [9002601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9002601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed next turn
   PL: [OnSucceedAttack] nakłada 3 Krwawienia w następnej turze
485. [Umiejętność wroga [9002601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9002601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 484 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Umiejętność wroga [9002602] (ulepszenie 1) — nazwa] 살벌한 환영인사
   źródło: Skills_Enemy.json :: dataList[id=9002602].levelList[level=1].name
   limit: do 40 znaków
   EN: Gruesome Welcome
   PL: Gruesome Welcome
487. [Umiejętność wroga [9002602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 정신 피해 15
   źródło: Skills_Enemy.json :: dataList[id=9002602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 15 SP damage
   PL: [OnSucceedAttack] zadaje 15 obrażeń Poczytalności
488. [Umiejętność wroga [9002603] (ulepszenie 1) — nazwa] 쏟아지는 욕설
   źródło: Skills_Enemy.json :: dataList[id=9002603].levelList[level=1].name
   limit: do 40 znaków
   EN: Insult Barrage
   PL: Insult Barrage
489. [Umiejętność wroga [9002603] (ulepszenie 1) — opis] [WinDuel] 무작위 아군 1명 정신력 10 회복
   źródło: Skills_Enemy.json :: dataList[id=9002603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Heal 10 SP for a random ally
   PL: [WinDuel] przywraca 10 Poczytalności losowemu sojusznikowi
490. [Umiejętność wroga [9002603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 정신 피해 5
   źródło: Skills_Enemy.json :: dataList[id=9002603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 SP damage
   PL: [OnSucceedAttack] zadaje 5 obrażeń SP
491. [Umiejętność wroga [9002604] (ulepszenie 1) — nazwa] 마!
   źródło: Skills_Enemy.json :: dataList[id=9002604].levelList[level=1].name
   limit: do 40 znaków
   EN: Ey!
   PL: Ey!
492. [Umiejętność wroga [9002604] (ulepszenie 1) — opis] [WinDuel] 대상의 정신력 - 15
   źródło: Skills_Enemy.json :: dataList[id=9002604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Target loses 15 SP
   PL: [WinDuel] cel traci 15 Poczytalności
493. [Umiejętność wroga [9002604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9002604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Umiejętność wroga [9002607] (ulepszenie 1) — nazwa] 눈깔 안 치워잉?
   źródło: Skills_Enemy.json :: dataList[id=9002607].levelList[level=1].name
   limit: do 40 znaków
   EN: What’re Ya Lookin’ At?
   PL: What’re Ya Lookin’ At?
495. [Umiejętność wroga [9002701] (ulepszenie 1) — nazwa] 대그빡을 쪼개불라
   źródło: Skills_Enemy.json :: dataList[id=9002701].levelList[level=1].name
   limit: do 40 znaków
   EN: I’ll Crack Ya Skull
   PL: I’ll Crack Ya Skull
496. [Umiejętność wroga [9002701] (ulepszenie 1) — opis] 대상의 정신력이 자신보다 낮으면 스킬 위력 +1
   źródło: Skills_Enemy.json :: dataList[id=9002701].levelList[level=1].desc
   (powtórzenie elementu 483 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Umiejętność wroga [9002701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 횟수 2 증가
   źródło: Skills_Enemy.json :: dataList[id=9002701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Bleed Count next turn
   PL: [OnSucceedAttack] zwiększa Licznik Krwawienia o 2 w następnej turze
498. [Umiejętność wroga [9002801] (ulepszenie 1) — nazwa] 돌격
   źródło: Skills_Enemy.json :: dataList[id=9002801].levelList[level=1].name
   limit: do 40 znaków
   EN: Raid
   PL: Raid
499. [Umiejętność wroga [9002801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 진동 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9002801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Tremor next turn
   PL: [OnSucceedAttack] nakłada 1 Wstrząsu w następnej turze
500. [Umiejętność wroga [9002801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 진동 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9002801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Umiejętność wroga [9002801] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 진동 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9002801].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Umiejętność wroga [9002802] (ulepszenie 1) — nazwa] 저지
   źródło: Skills_Enemy.json :: dataList[id=9002802].levelList[level=1].name
   limit: do 40 znaków
   EN: Blockade
   PL: Blockade
503. [Umiejętność wroga [9002803] (ulepszenie 1) — nazwa] 표적 무력화
   źródło: Skills_Enemy.json :: dataList[id=9002803].levelList[level=1].name
   limit: do 40 znaków
   EN: Neutralize Target
   PL: Neutralize Target
504. [Umiejętność wroga [9002803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 진동 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9002803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Tremor next turn
   PL: [OnSucceedAttackHead] nakłada 3 Wstrząsu w następnej turze
505. [Umiejętność wroga [9002803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9002803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Trigger Tremor Burst
   PL: [OnSucceedAttack] Wybuch Wstrząsu
506. [Umiejętność wroga [9002804] (ulepszenie 1) — nazwa] HP탄 활성화
   źródło: Skills_Enemy.json :: dataList[id=9002804].levelList[level=1].name
   limit: do 40 znaków
   EN: Activate HP Bullet
   PL: Activate HP Bullet
507. [Umiejętność wroga [9002804] (ulepszenie 1) — opis] [WhenUse] 체력 10 회복
   źródło: Skills_Enemy.json :: dataList[id=9002804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 10 HP
   PL: [WhenUse] przywraca 10 HP
508. [Umiejętność wroga [9002901] (ulepszenie 1) — nazwa] 진압
   źródło: Skills_Enemy.json :: dataList[id=9002901].levelList[level=1].name
   limit: do 40 znaków
   EN: Takedown
   PL: Takedown
509. [Umiejętność wroga [9002901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 진동 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9002901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Tremor Count next turn
   PL: [OnSucceedAttack] zwiększa Licznik Wstrząsu o 1 w następnej turze
510. [Umiejętność wroga [9003001] (ulepszenie 1) — nazwa] 방호
   źródło: Skills_Enemy.json :: dataList[id=9003001].levelList[level=1].name
   limit: do 40 znaków
   EN: Shelter
   PL: Defend
511. [Umiejętność wroga [9003001] (ulepszenie 1) — opis] [WinDuel] 무작위 아군 2명에게 다음 턴에 수비 위력 증가 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9003001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Apply 1 Defense Power Up to 2 random allies next turn
   PL: [WinDuel] nakłada 1 Wzrost Mocy Obrony na 2 losowych sojuszników w następnej turze
512. [Umiejętność wroga [9003002] (ulepszenie 1) — nazwa] 저지
   źródło: Skills_Enemy.json :: dataList[id=9003002].levelList[level=1].name
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Umiejętność wroga [9003002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9003002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Trigger Tremor Burst
   PL: [OnSucceedAttackHead] Wybuch Wstrząsu
514. [Umiejętność wroga [9003101] (ulepszenie 1) — nazwa] 엄호
   źródło: Skills_Enemy.json :: dataList[id=9003101].levelList[level=1].name
   limit: do 40 znaków
   EN: Cover
   PL: Cover
515. [Umiejętność wroga [9003101] (ulepszenie 1) — opis] [WinDuel] 자신을 제외한 무작위 아군 1명에게 다음 턴에 보호 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9003101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Apply 2 Protection to a random other ally next turn
   PL: [WinDuel] nakłada 2 Ochrony na 1 losowego sojusznika poza sobą w następnej turze
516. [Umiejętność wroga [9003201] (ulepszenie 1) — nazwa] 찔러넣기
   źródło: Skills_Enemy.json :: dataList[id=9003201].levelList[level=1].name
   limit: do 40 znaków
   EN: Plunge In
   PL: Plunge In
517. [Umiejętność wroga [9003201] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9003201].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed next turn
   PL: [OnSucceedAttack] nakłada 2 Krwawienia w następnej turze
518. [Umiejętność wroga [9003202] (ulepszenie 1) — nazwa] 못질
   źródło: Skills_Enemy.json :: dataList[id=9003202].levelList[level=1].name
   limit: do 40 znaków
   EN: Nail Pin
   PL: Nail Pin
519. [Umiejętność wroga [9003202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9003202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 N Corp’s Nails next turn
   PL: [OnSucceedAttack] nakłada 1 N Corp's Nails w następnej turze
520. [Umiejętność wroga [9003202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9003202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Umiejętność wroga [9003301] (ulepszenie 1) — nazwa] 두드리기
   źródło: Skills_Enemy.json :: dataList[id=9003301].levelList[level=1].name
   limit: do 40 znaków
   EN: Knock
   PL: Knock
522. [Umiejętność wroga [9003301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비, 수비 위력 감소 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9003301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Paralyze and Defense Power Down next turn
   PL: [OnSucceedAttack] nakłada 1 Paraliżu i 1 Spadek Mocy Obrony w następnej turze
523. [Umiejętność wroga [9003302] (ulepszenie 1) — nazwa] 망치질
   źródło: Skills_Enemy.json :: dataList[id=9003302].levelList[level=1].name
   limit: do 40 znaków
   EN: Hammer
   PL: Hammer
524. [Umiejętność wroga [9003302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9003302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Umiejętność wroga [9003401] (ulepszenie 1) — nazwa] 이단 심판
   źródło: Skills_Enemy.json :: dataList[id=9003401].levelList[level=1].name
   limit: do 40 znaków
   EN: Inquisition
   PL: Inquisition
526. [Umiejętność wroga [9003401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] N사의 못 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9003401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 N Corp’s Nails
   PL: [OnSucceedAttackHead] nakłada 1 N Corp's Nails
527. [Umiejętność wroga [9003401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9003401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 484 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Umiejętność wroga [9003502] (ulepszenie 1) — nazwa] 거친 못질
   źródło: Skills_Enemy.json :: dataList[id=9003502].levelList[level=1].name
   limit: do 40 znaków
   EN: Rough Nailing
   PL: Rough Nailing
529. [Umiejętność wroga [9003502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못, 출혈 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9003502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 N Corp’s Nails and Bleed next turn
   PL: [OnSucceedAttack] nakłada 1 N Corp's Nails i 1 Krwawienia w następnej turze
530. [Umiejętność wroga [9003502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못, 출혈 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9003502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Umiejętność wroga [9003502] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못, 출혈 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9003502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Umiejętność wroga [9003503] (ulepszenie 1) — nazwa] 공격적인 설파
   źródło: Skills_Enemy.json :: dataList[id=9003503].levelList[level=1].name
   limit: do 40 znaków
   EN: Aggressive Preaching
   PL: Aggressive Preaching
533. [Umiejętność wroga [9003503] (ulepszenie 1) — opis] [DefeatDuel] 다음 턴에 취약 2 얻음
   źródło: Skills_Enemy.json :: dataList[id=9003503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Gain 2 Fragile next turn
   PL: [DefeatDuel] zyskuje 2 Wrażliwości w następnej turze
534. [Umiejętność wroga [9003503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9003503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Fragile next turn
   PL: [OnSucceedAttack] nakłada 2 Wrażliwości w następnej turze
535. [Umiejętność wroga [9003504] (ulepszenie 1) — nazwa] 감히!
   źródło: Skills_Enemy.json :: dataList[id=9003504].levelList[level=1].name
   limit: do 40 znaków
   EN: You Dare!
   PL: You Dare!
536. [Umiejętność wroga [9003504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9003504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 N Corp’s Nails next turn
   PL: [OnSucceedAttackHead] nakłada 1 N Corp's Nails w następnej turze
537. [Umiejętność wroga [9003602] (ulepszenie 1) — nazwa] 드센 망치질
   źródło: Skills_Enemy.json :: dataList[id=9003602].levelList[level=1].name
   limit: do 40 znaków
   EN: Vigorous Hammering
   PL: Vigorous Hammering
538. [Umiejętność wroga [9003602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 3, 마비 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9003602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bind and 2 Paralyze next turn
   PL: [OnSucceedAttack] nakłada 3 Spętania i 2 Paraliżu w następnej turze
539. [Umiejętność wroga [9003603] (ulepszenie 1) — nazwa] 압도적인 설파
   źródło: Skills_Enemy.json :: dataList[id=9003603].levelList[level=1].name
   limit: do 40 znaków
   EN: Oppressive Preaching
   PL: Oppressive Preaching
540. [Umiejętność wroga [9003603] (ulepszenie 1) — opis] [DefeatDuel] 다음 턴에 공격 위력 감소 2를 얻음
   źródło: Skills_Enemy.json :: dataList[id=9003603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Gain 2 Attack Power Down next turn
   PL: [DefeatDuel] zyskuje 2 Spadku Mocy Ataku w następnej turze
541. [Umiejętność wroga [9003603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9003603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 457 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Umiejętność wroga [9003701] (ulepszenie 1) — nazwa] 거친 이단 심판
   źródło: Skills_Enemy.json :: dataList[id=9003701].levelList[level=1].name
   limit: do 40 znaków
   EN: Assertive Inquisition
   PL: Assertive Inquisition
543. [Umiejętność wroga [9003701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] N사의 못 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9003701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 526 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Umiejętność wroga [9003701] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 N사의 못이 5 이상 있으면 다음 턴에 속박 10 부여
   źródło: Skills_Enemy.json :: dataList[id=9003701].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ N Corp’s Nails, inflict 10 Bind next turn
   PL: [OnSucceedAttack] jeżeli cel ma 5+ N Corp's Nails, nakłada 10 Spętania w następnej turze
545. [Umiejętność wroga [9003801] (ulepszenie 1) — nazwa] 꿰뚫는 못
   źródło: Skills_Enemy.json :: dataList[id=9003801].levelList[level=1].name
   limit: do 40 znaków
   EN: Thrusting Nail
   PL: Thrusting Nail
546. [Umiejętność wroga [9003801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9003801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 N Corp’s Nails next turn
   PL: [OnSucceedAttack] nakłada 2 N Corp's Nails w następnej turze
547. [Umiejętność wroga [9003803] (ulepszenie 1) — nazwa] 집결
   źródło: Skills_Enemy.json :: dataList[id=9003803].levelList[level=1].name
   limit: do 40 znaków
   EN: Congregate
   PL: Congregate
548. [Umiejętność wroga [9003803] (ulepszenie 1) — opis] [WinDuel] 무작위 아군 2명에게 다음 턴에 광신 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9003803].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Apply 1 Fanatic to 2 random allies next turn
   PL: [WinDuel] nakłada 1 Fanatyzmu na 2 losowych sojuszników w następnej turze
549. [Umiejętność wroga [9003803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9003803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 517 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Umiejętność wroga [9003804] (ulepszenie 1) — nazwa] 단단한 믿음
   źródło: Skills_Enemy.json :: dataList[id=9003804].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardy Faith
   PL: Hardy Faith
551. [Umiejętność wroga [9003804] (ulepszenie 1) — opis] [WhenUse] 보호 1 얻음
   źródło: Skills_Enemy.json :: dataList[id=9003804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Protection
   PL: [WhenUse] Zyskuje 1 [Protection]
552. [Umiejętność wroga [9003901] (ulepszenie 1) — nazwa] 다스리는 망치
   źródło: Skills_Enemy.json :: dataList[id=9003901].levelList[level=1].name
   limit: do 40 znaków
   EN: Ruling Hammer
   PL: Ruling Hammer
553. [Umiejętność wroga [9003901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 3, 공격 위력 감소 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9003901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Bind and 2 Attack Power Down next turn
   PL: [OnSucceedAttackHead] nakłada 3 Spętania i 2 Spadku Mocy Ataku w następnej turze
554. [Umiejętność wroga [9003903] (ulepszenie 1) — nazwa] 단결
   źródło: Skills_Enemy.json :: dataList[id=9003903].levelList[level=1].name
   limit: do 40 znaków
   EN: Unite
   PL: Unite
555. [Umiejętność wroga [9003903] (ulepszenie 1) — opis] [WinDuel] 정신력이 가장 낮은 아군 2명의 정신력 15 회복
   źródło: Skills_Enemy.json :: dataList[id=9003903].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Heal 15 SP for 2 allies with the least SP
   PL: [WinDuel] przywraca 15 Poczytalności 2 sojusznikom z najniższą Poczytalnością
556. [Umiejętność wroga [9003903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9003903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 517 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Umiejętność wroga [9004001] (ulepszenie 1) — nazwa] 육중한 이단 심판
   źródło: Skills_Enemy.json :: dataList[id=9004001].levelList[level=1].name
   limit: do 40 znaków
   EN: Ponderous Inquisition
   PL: Ponderous Inquisition
558. [Umiejętność wroga [9004001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] N사의 못 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9004001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 N Corp’s Nails
   PL: [OnSucceedAttackHead] nakłada 2 N Corp's Nails
559. [Umiejętność wroga [9004001] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 N사의 못이 5 이상 있으면 다음 턴에 공격 위력 감소, 마비 10 부여
   źródło: Skills_Enemy.json :: dataList[id=9004001].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ N Corp’s Nails, inflict 10 Attack Power Down and Paralyze next turn
   PL: [OnSucceedAttack] jeżeli cel ma 5+ N Corp's Nails, nakłada 10 Spadku Mocy Ataku i 10 Paraliżu w następnej turze
560. [Umiejętność wroga [9100501] (ulepszenie 1) — nazwa] 대못 박기
   źródło: Skills_Enemy.json :: dataList[id=9100501].levelList[level=1].name
   limit: do 40 znaków
   EN: Spike Drive
   PL: Spike Drive
561. [Umiejętność wroga [9100501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9100501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Umiejętność wroga [9100501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9100501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Umiejętność wroga [9100501] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100501].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Umiejętność wroga [9100502] (ulepszenie 1) — nazwa] 꿰뚫기
   źródło: Skills_Enemy.json :: dataList[id=9100502].levelList[level=1].name
   limit: do 40 znaków
   EN: Drive
   PL: Pchnięcie
565. [Umiejętność wroga [9100502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 5 , 취약 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Bleed and 2 Fragile next turn
   PL: [OnSucceedAttack] nakłada 5 Krwawień i 2 Wrażliwości w następnej turze
566. [Umiejętność wroga [9100503] (ulepszenie 1) — nazwa] 망치들이여...!
   źródło: Skills_Enemy.json :: dataList[id=9100503].levelList[level=1].name
   limit: do 40 znaków
   EN: Hammers, Heed Me…!
   PL: Hammers, Heed Me…!
567. [Umiejętność wroga [9100503] (ulepszenie 1) — opis] [WinDuel] 모든 아군에게 다음 턴에 광신 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9100503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Apply 1 Fanatic to all allies next turn
   PL: [WinDuel] nakłada 1 Fanatyzmu na wszystkich sojuszników w następnej turze
568. [Umiejętność wroga [9100503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 정신력이 가장 낮은 아군 2명의 정신력 10 회복
   źródło: Skills_Enemy.json :: dataList[id=9100503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 10 SP for 2 allies with the least SP
   PL: [OnSucceedAttack] przywraca 10 Poczytalności 2 sojusznikom z najniższą Poczytalnością
569. [Umiejętność wroga [9100504] (ulepszenie 1) — nazwa] 죄를 씻어내노라
   źródło: Skills_Enemy.json :: dataList[id=9100504].levelList[level=1].name
   limit: do 40 znaków
   EN: You Are Cleansed of Sin
   PL: Zostajesz Oczyszczony z Grzechu
570. [Umiejętność wroga [9100504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] N사의 못 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9100504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 N Corp’s Nails
   PL: [OnSucceedAttackHead] nakłada 3 N Corp's Nails
571. [Umiejętność wroga [9100504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 N사의 못이 5 이상 있으면 흐트러짐 상태로 만듦
   źródło: Skills_Enemy.json :: dataList[id=9100504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ N Corp’s Nails, Stagger them
   PL: [OnSucceedAttack] jeżeli cel ma 5+ N Corp's Nails, Oszołamuje go
572. [Umiejętność wroga [9100505] (ulepszenie 1) — nazwa] 굳센 믿음
   źródło: Skills_Enemy.json :: dataList[id=9100505].levelList[level=1].name
   limit: do 40 znaków
   EN: Stalwart Faith
   PL: Stalwart Faith
573. [Umiejętność wroga [9100505] (ulepszenie 1) — opis] [WhenUse] 보호 2 얻음
   źródło: Skills_Enemy.json :: dataList[id=9100505].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Protection
   PL: [WhenUse] zyskuje 2 Ochrony
574. [Umiejętność wroga [9100601] (ulepszenie 1) — nazwa] 대못 박기
   źródło: Skills_Enemy.json :: dataList[id=9100601].levelList[level=1].name
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Umiejętność wroga [9100601] (ulepszenie 1) — opis] 체력이 50%미만일 때, 부여하는 N사의 못 + 1
   źródło: Skills_Enemy.json :: dataList[id=9100601].levelList[level=1].desc
   limit: do 120 znaków
   EN: At less than 50% HP, inflict +1 N Corp’s Nails
   PL: przy mniej niż 50% HP, nakłada o 1 więcej N Corp's Nails
576. [Umiejętność wroga [9100601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9100601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Umiejętność wroga [9100601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9100601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Umiejętność wroga [9100601] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100601].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Umiejętność wroga [9100602] (ulepszenie 1) — nazwa] 꿰뚫기
   źródło: Skills_Enemy.json :: dataList[id=9100602].levelList[level=1].name
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Umiejętność wroga [9100602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9100602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Bleed next turn
   PL: [OnSucceedAttack] nakłada 5 Krwawienia w następnej turze
581. [Umiejętność wroga [9100603] (ulepszenie 1) — nazwa] 대업을 수행하라...!
   źródło: Skills_Enemy.json :: dataList[id=9100603].levelList[level=1].name
   limit: do 50 znaków
   EN: The Great Task Will Be Done…!
   PL: The Great Task Will Be Done…!
582. [Umiejętność wroga [9100603] (ulepszenie 1) — opis] [WhenUse] 아군 전체에게 다음 턴에 광신 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9100603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Apply 1 Fanatic to all allies next turn
   PL: [WhenUse] nakłada 1 Fanatyzmu na wszystkich sojuszników w następnej turze
583. [Umiejętność wroga [9100604] (ulepszenie 1) — nazwa] 죄를... 씻어내노라!
   źródło: Skills_Enemy.json :: dataList[id=9100604].levelList[level=1].name
   limit: do 40 znaków
   EN: Be Cleansed… of Sin!
   PL: Be Cleansed… of Sin!
584. [Umiejętność wroga [9100604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] N사의 못 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9100604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 N Corp’s Nails
   PL: [OnSucceedAttackHead] nakłada 5 N Corp's Nails
585. [Umiejętność wroga [9100604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 N사의 못이 5 이상 있으면 흐트러짐 상태로 만듦
   źródło: Skills_Enemy.json :: dataList[id=9100604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 571 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Umiejętność wroga [9100605] (ulepszenie 1) — nazwa] 이단 말살
   źródło: Skills_Enemy.json :: dataList[id=9100605].levelList[level=1].name
   limit: do 40 znaków
   EN: Annihilate Heretics
   PL: Zagłada Heretyków
587. [Umiejętność wroga [9100605] (ulepszenie 1) — opis] N사의 못이 있는 대상 공격 시 피해량 +100%
   źródło: Skills_Enemy.json :: dataList[id=9100605].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target has N Corp’s Nails, +100% Damage
   PL: jeżeli cel ma N Corp's Nails, +100% obrażeń
588. [Umiejętność wroga [9100605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 10 부여
   źródło: Skills_Enemy.json :: dataList[id=9100605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 10 Rupture next turn
   PL: [OnSucceedAttack] nakłada 10 Rozdarcia w następnej turze
589. [Umiejętność wroga [9100605] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9100605].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Fragile next turn
   PL: [OnSucceedAttack] nakłada 5 Wrażliwości w następnej turze
590. [Umiejętność wroga [9100606] (ulepszenie 1) — nazwa] 어리석도다...!
   źródło: Skills_Enemy.json :: dataList[id=9100606].levelList[level=1].name
   limit: do 40 znaków
   EN: Foolishness…!
   PL: Głupota...!
591. [Umiejętność wroga [9100606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 N사의 못 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9100606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność wroga [9004101] (ulepszenie 1) — nazwa] 내려찍기
   źródło: Skills_Enemy.json :: dataList[id=9004101].levelList[level=1].name
   limit: do 40 znaków
   EN: Strike Down
   PL: Ściągnięcie
593. [Umiejętność wroga [9004102] (ulepszenie 1) — nazwa] 사선긋기
   źródło: Skills_Enemy.json :: dataList[id=9004102].levelList[level=1].name
   limit: do 40 znaków
   EN: Line of Death
   PL: Line of Death
594. [Umiejętność wroga [9004201] (ulepszenie 1) — nazwa] 기이
   źródło: Skills_Enemy.json :: dataList[id=9004201].levelList[level=1].name
   limit: do 40 znaków
   EN: Kii
   PL: Kii
595. [Umiejętność wroga [9004201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9004201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Rupture
   PL: [OnSucceedAttackHead] Nakłada 3 Rozdarcia
596. [Umiejętność wroga [9004202] (ulepszenie 1) — nazwa] 기이익
   źródło: Skills_Enemy.json :: dataList[id=9004202].levelList[level=1].name
   limit: do 40 znaków
   EN: Kiih
   PL: Kiih
597. [Umiejętność wroga [9004202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 횟수 3 증가
   źródło: Skills_Enemy.json :: dataList[id=9004202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +3 Rupture Count
   PL: [OnSucceedAttackHead] zwiększa Licznik Rozdarcia o 3
598. [Umiejętność wroga [9004202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9004202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Umiejętność wroga [9004203] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy.json :: dataList[id=9004203].levelList[level=1].name
   (powtórzenie elementu 359 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Umiejętność wroga [9004301] (ulepszenie 1) — nazwa] 기이익
   źródło: Skills_Enemy.json :: dataList[id=9004301].levelList[level=1].name
   (powtórzenie elementu 596 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Umiejętność wroga [9004301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9004301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 595 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Umiejętność wroga [9004302] (ulepszenie 1) — nazwa] 기이이익
   źródło: Skills_Enemy.json :: dataList[id=9004302].levelList[level=1].name
   limit: do 40 znaków
   EN: Kiieeh
   PL: Kiieeh
603. [Umiejętność wroga [9004302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9004302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture
   PL: [OnSucceedAttack] Nakłada 3 Rozdarcia
604. [Umiejętność wroga [9004303] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy.json :: dataList[id=9004303].levelList[level=1].name
   (powtórzenie elementu 359 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Umiejętność wroga [9004401] (ulepszenie 1) — nazwa] 기긱!
   źródło: Skills_Enemy.json :: dataList[id=9004401].levelList[level=1].name
   limit: do 40 znaków
   EN: Kigik!
   PL: Kigik!
606. [Umiejętność wroga [9004401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9004401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Bleed
   PL: [OnSucceedAttackHead] Nakłada 3 Krwawienia
607. [Umiejętność wroga [9004402] (ulepszenie 1) — nazwa] 기익!
   źródło: Skills_Enemy.json :: dataList[id=9004402].levelList[level=1].name
   limit: do 40 znaków
   EN: Kieek!
   PL: Kieek!
608. [Umiejętność wroga [9004402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9004402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Umiejętność wroga [9004402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 방어 레벨 2 감소, 출혈 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9004402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Reduce target's Defense Level by 2 and inflict +1 Bleed Count
   PL: [OnSucceedAttackHead] zmniejsza Poziom Obrony celu o 2 i zwiększa Licznik Krwawienia o 1
610. [Umiejętność wroga [9004403] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy.json :: dataList[id=9004403].levelList[level=1].name
   (powtórzenie elementu 359 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Umiejętność wroga [9004501] (ulepszenie 1) — nazwa] 기긱이긱
   źródło: Skills_Enemy.json :: dataList[id=9004501].levelList[level=1].name
   limit: do 40 znaków
   EN: Kigigiik
   PL: Kigigiik
612. [Umiejętność wroga [9004501] (ulepszenie 1) — opis] 이전 턴에 피해를 받지 않은 경우 코인 위력 +1
   źródło: Skills_Enemy.json :: dataList[id=9004501].levelList[level=1].desc
   limit: do 120 znaków
   EN: If user took no damage last turn, Coin Power +1
   PL: Gdy ta jednostka nie otrzymała obrażeń w poprzedniej turze, Moc Monet +1
613. [Umiejętność wroga [9004501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9004501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 Tremor
   PL: [OnSucceedAttackHead] nakłada 5 Wstrząsu
614. [Umiejętność wroga [9004502] (ulepszenie 1) — nazwa] 기긱이긱
   źródło: Skills_Enemy.json :: dataList[id=9004502].levelList[level=1].name
   (powtórzenie elementu 611 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Umiejętność wroga [9004502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1, 방어 레벨 2 감소
   źródło: Skills_Enemy.json :: dataList[id=9004502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bind and reduce target's Defense Level by 2 next turn
   PL: [OnSucceedAttack] nakłada 1 Spętania i zmniejsza Poziom Obrony celu o 2 w następnej turze
616. [Umiejętność wroga [9004503] (ulepszenie 1) — nazwa] 기이긱기
   źródło: Skills_Enemy.json :: dataList[id=9004503].levelList[level=1].name
   limit: do 40 znaków
   EN: Kieegikhik
   PL: Kieegikhik
617. [Umiejętność wroga [9004503] (ulepszenie 1) — opis] [WhenUse] 보호 2 얻음
   źródło: Skills_Enemy.json :: dataList[id=9004503].levelList[level=1].desc
   (powtórzenie elementu 573 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Umiejętność wroga [9004503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9004503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Umiejętność wroga [9004504] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy.json :: dataList[id=9004504].levelList[level=1].name
   (powtórzenie elementu 359 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Umiejętność wroga [9004601] (ulepszenie 1) — nazwa] 근접 촬영 시작
   źródło: Skills_Enemy.json :: dataList[id=9004601].levelList[level=1].name
   limit: do 40 znaków
   EN: Proximity Shooting
   PL: Proximity Shooting
621. [Umiejętność wroga [9004602] (ulepszenie 1) — nazwa] 후퇴 후퇴
   źródło: Skills_Enemy.json :: dataList[id=9004602].levelList[level=1].name
   limit: do 40 znaków
   EN: Retreat; Retreat;
   PL: Retreat; Retreat;
622. [Umiejętność wroga [9004603] (ulepszenie 1) — nazwa] 근접 촬영 시작
   źródło: Skills_Enemy.json :: dataList[id=9004603].levelList[level=1].name
   (powtórzenie elementu 620 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Umiejętność wroga [9004604] (ulepszenie 1) — nazwa] 후퇴 후퇴
   źródło: Skills_Enemy.json :: dataList[id=9004604].levelList[level=1].name
   (powtórzenie elementu 621 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Umiejętność wroga [9004605] (ulepszenie 1) — nazwa] 섬광 섬광
   źródło: Skills_Enemy.json :: dataList[id=9004605].levelList[level=1].name
   limit: do 40 znaków
   EN: Flash; Flash;
   PL: Flash; Flash;
625. [Umiejętność wroga [9004605] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력 -10
   źródło: Skills_Enemy.json :: dataList[id=9004605].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Target loses 10 SP
   PL: [WhenUse] cel traci 10 Poczytalności
626. [Umiejętność wroga [9004606] (ulepszenie 1) — nazwa] 약점을 찾습니다.
   źródło: Skills_Enemy.json :: dataList[id=9004606].levelList[level=1].name
   limit: do 40 znaków
   EN: Scanning for weakness.
   PL: Scanning for weakness.
627. [Umiejętność wroga [9004606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9004606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Fragile next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Wrażliwości
628. [Umiejętność wroga [9004607] (ulepszenie 1) — nazwa] 움직임을 저지합니다.
   źródło: Skills_Enemy.json :: dataList[id=9004607].levelList[level=1].name
   limit: do 40 znaków
   EN: Impeding movement.
   PL: Impeding movement.
629. [Umiejętność wroga [9004607] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9004607].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Umiejętność wroga [9004701] (ulepszenie 1) — nazwa] 썰어냅니다.
   źródło: Skills_Enemy.json :: dataList[id=9004701].levelList[level=1].name
   limit: do 40 znaków
   EN: Cutting up.
   PL: Cutting up.
631. [Umiejętność wroga [9004701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills_Enemy.json :: dataList[id=9004701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Rupture Count
   PL: [OnSucceedAttack] Zwiększa Licznik Rozdarcia o 3
632. [Umiejętność wroga [9004702] (ulepszenie 1) — nazwa] 깎아냅니다.
   źródło: Skills_Enemy.json :: dataList[id=9004702].levelList[level=1].name
   limit: do 40 znaków
   EN: Carving out.
   PL: Carving out.
633. [Umiejętność wroga [9004702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 취약 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9004702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Fragile next turn
   PL: [OnSucceedAttackHead] nakłada 1 Wrażliwości w następnej turze
634. [Umiejętność wroga [9004702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 감소 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9004702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 Defense Level Down next turn
   PL: [OnSucceedAttackHead] nakłada 5 Spadku Poziomu Obrony w następnej turze
635. [Umiejętność wroga [9004801] (ulepszenie 1) — nazwa] 장전...발사
   źródło: Skills_Enemy.json :: dataList[id=9004801].levelList[level=1].name
   limit: do 40 znaków
   EN: Load... And Fire
   PL: Load... And Fire
636. [Umiejętność wroga [9004801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9004801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Tremor
   PL: [OnSucceedAttack] Nakłada 3 [Vibration]
637. [Umiejętność wroga [9004802] (ulepszenie 1) — nazwa] 찍어누릅니다.
   źródło: Skills_Enemy.json :: dataList[id=9004802].levelList[level=1].name
   limit: do 40 znaków
   EN: Pressing down.
   PL: Pressing down.
638. [Umiejętność wroga [9004802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 감소 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9004802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 457 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Umiejętność wroga [9004802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9004802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 513 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Umiejętność wroga [9004901] (ulepszenie 1) — nazwa] 썰어냅니다.
   źródło: Skills_Enemy.json :: dataList[id=9004901].levelList[level=1].name
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Umiejętność wroga [9004901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 5 증가
   źródło: Skills_Enemy.json :: dataList[id=9004901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +5 Rupture Count
   PL: [OnSucceedAttack] Zwiększa Licznik Rozdarcia o 5
642. [Umiejętność wroga [9004901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9004901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 603 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność wroga [9004902] (ulepszenie 1) — nazwa] 깎아냅니다.
   źródło: Skills_Enemy.json :: dataList[id=9004902].levelList[level=1].name
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Umiejętność wroga [9004902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 감소 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9004902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Defense Level Down next turn
   PL: [OnSucceedAttack] nakłada 5 Spadek Poziomu Obrony w następnej turze
645. [Umiejętność wroga [9004902] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 취약 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9004902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Fragile next turn
   PL: [OnSucceedAttackHead] nakłada 2 Wrażliwości w następnej turze
646. [Umiejętność wroga [9004903] (ulepszenie 1) — nazwa] 톱니...찍어내립니다.
   źródło: Skills_Enemy.json :: dataList[id=9004903].levelList[level=1].name
   limit: do 40 znaków
   EN: Sawblade... Slamming down.
   PL: Sawblade... Slamming down.
647. [Umiejętność wroga [9004903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 5 증가
   źródło: Skills_Enemy.json :: dataList[id=9004903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 641 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Umiejętność wroga [9004903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9004903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 Rupture
   PL: [OnSucceedAttackHead] Nakłada 5 Rozdarcia
649. [Umiejętność wroga [9004903] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9004903].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 329 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [Umiejętność wroga [9004904] (ulepszenie 1) — nazwa] 방어 모드 진입
   źródło: Skills_Enemy.json :: dataList[id=9004904].levelList[level=1].name
   limit: do 40 znaków
   EN: Enter Defensive Mode
   PL: Enter Defensive Mode
651. [Umiejętność wroga [9004904] (ulepszenie 1) — opis] [WhenUse] 보호 2 얻음
   źródło: Skills_Enemy.json :: dataList[id=9004904].levelList[level=1].desc
   (powtórzenie elementu 573 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Umiejętność wroga [9005001] (ulepszenie 1) — nazwa] 장전… 발사
   źródło: Skills_Enemy.json :: dataList[id=9005001].levelList[level=1].name
   limit: do 40 znaków
   EN: Load... And Fire
   PL: Load... And Fire
653. [Umiejętność wroga [9005001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9005001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Tremor
   PL: [OnSucceedAttack] Nakłada 5 Wstrząsu
654. [Umiejętność wroga [9005001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 진동 횟수 2 증가
   źródło: Skills_Enemy.json :: dataList[id=9005001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +2 Tremor Count
   PL: [OnSucceedAttackHead] Nakłada +2 Licznika Wstrząsu
655. [Umiejętność wroga [9005002] (ulepszenie 1) — nazwa] 찍어누릅니다.
   źródło: Skills_Enemy.json :: dataList[id=9005002].levelList[level=1].name
   (powtórzenie elementu 637 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Umiejętność wroga [9005002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 레벨 감소 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9005002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Offense Level Down next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 3 Spadku Poziomu Ataku
657. [Umiejętność wroga [9005003] (ulepszenie 1) — nazwa] 흔들림 주의 주의
   źródło: Skills_Enemy.json :: dataList[id=9005003].levelList[level=1].name
   limit: do 40 znaków
   EN: CAUTION, CAUTION: Unsteady
   PL: CAUTION, CAUTION: Unsteady
658. [Umiejętność wroga [9005003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 레벨 감소 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9005003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Offense Level Down next turn
   PL: [OnSucceedAttack] nakłada 5 Spadku Poziomu Ataku w następnej turze
659. [Umiejętność wroga [9005003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9005003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Umiejętność wroga [9005004] (ulepszenie 1) — nazwa] 방어 모드 진입
   źródło: Skills_Enemy.json :: dataList[id=9005004].levelList[level=1].name
   (powtórzenie elementu 650 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Umiejętność wroga [9005004] (ulepszenie 1) — opis] [WhenUse] 보호 2 얻음
   źródło: Skills_Enemy.json :: dataList[id=9005004].levelList[level=1].desc
   (powtórzenie elementu 573 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [Umiejętność wroga [9100701] (ulepszenie 1) — nazwa] 상처냅니다.
   źródło: Skills_Enemy.json :: dataList[id=9100701].levelList[level=1].name
   limit: do 40 znaków
   EN: Wounding.
   PL: Wounding.
663. [Umiejętność wroga [9100701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9100701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Rupture
   PL: [OnSucceedAttack] Nakłada 5 Rozdarcia
664. [Umiejętność wroga [9100701] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 파열 횟수 5 증가
   źródło: Skills_Enemy.json :: dataList[id=9100701].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +5 Rupture Count
   PL: [OnSucceedAttackHead] zwiększa Licznik Rozdarcia o 5
665. [Umiejętność wroga [9100702] (ulepszenie 1) — nazwa] 상처 발견 발견
   źródło: Skills_Enemy.json :: dataList[id=9100702].levelList[level=1].name
   limit: do 40 znaków
   EN: SPOTTED, SPOTTED: Injury
   PL: SPOTTED, SPOTTED: Injury
666. [Umiejętność wroga [9100702] (ulepszenie 1) — opis] 파열이 있는 대상 우선 공격
   źródło: Skills_Enemy.json :: dataList[id=9100702].levelList[level=1].desc
   limit: do 120 znaków
   EN: Prioritizes enemies with Rupture
   PL: priorytet: wrogowie z Rozdarciem
667. [Umiejętność wroga [9100702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수만큼 추가 고정 피해
   źródło: Skills_Enemy.json :: dataList[id=9100702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal fixed damage equal to target's Rupture Count
   PL: [OnSucceedAttack] zadaje stałe obrażenia równe Licznikowi Rozdarcia celu
668. [Umiejętność wroga [9100703] (ulepszenie 1) — nazwa] 흔들림 증폭
   źródło: Skills_Enemy.json :: dataList[id=9100703].levelList[level=1].name
   limit: do 40 znaków
   EN: Amplify Vibration
   PL: Amplify Vibration
669. [Umiejętność wroga [9100703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9100703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Umiejętność wroga [9100703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 진동 횟수 3 증가
   źródło: Skills_Enemy.json :: dataList[id=9100703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +3 Tremor Count
   PL: [OnSucceedAttackHead] zwiększa Licznik Wstrząsu o 3
671. [Umiejętność wroga [9100704] (ulepszenie 1) — nazwa] 무너뜨립니다.
   źródło: Skills_Enemy.json :: dataList[id=9100704].levelList[level=1].name
   limit: do 40 znaków
   EN: Breaking down.
   PL: Breaking down.
672. [Umiejętność wroga [9100704] (ulepszenie 1) — opis] 진동이 있는 대상 우선 공격
   źródło: Skills_Enemy.json :: dataList[id=9100704].levelList[level=1].desc
   limit: do 120 znaków
   EN: Prioritizes enemies with Tremor
   PL: priorytet: wrogowie z Wstrząsem
673. [Umiejętność wroga [9100704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9100704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Umiejętność wroga [9100704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 마비 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9100704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 Paralyze next turn
   PL: [OnSucceedAttackHead] nakłada 5 Paraliżu w następnej turze
675. [Umiejętność wroga [9100705] (ulepszenie 1) — nazwa] 흔들립니다. 주의 주의
   źródło: Skills_Enemy.json :: dataList[id=9100705].levelList[level=1].name
   limit: do 40 znaków
   EN: WARNING, WARNING: Shaking
   PL: WARNING, WARNING: Shaking
676. [Umiejętność wroga [9100705] (ulepszenie 1) — opis] 진동이 있는 대상 우선 공격
   źródło: Skills_Enemy.json :: dataList[id=9100705].levelList[level=1].desc
   (powtórzenie elementu 672 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Umiejętność wroga [9100705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 10 부여
   źródło: Skills_Enemy.json :: dataList[id=9100705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 10 Tremor
   PL: [OnSucceedAttack] nakłada 10 [Vibration]
678. [Umiejętność wroga [9100706] (ulepszenie 1) — nazwa] 헛점 확인
   źródło: Skills_Enemy.json :: dataList[id=9100706].levelList[level=1].name
   limit: do 40 znaków
   EN: Vulnerability Detected
   PL: Vulnerability Detected
679. [Umiejętność wroga [9100706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량 -50%.\n대상을 흐트러짐 상태로 만듦.
   źródło: Skills_Enemy.json :: dataList[id=9100706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Damage -50%\nStagger target
   PL: [OnSucceedAttack] zadaje o 50% mniej obrażeń\nOszołamuje cel
680. [Umiejętność wroga [9100707] (ulepszenie 1) — nazwa] 방어 모드 진입
   źródło: Skills_Enemy.json :: dataList[id=9100707].levelList[level=1].name
   (powtórzenie elementu 650 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Umiejętność wroga [9100707] (ulepszenie 1) — opis] [StartBattle] 보호 3 얻음
   źródło: Skills_Enemy.json :: dataList[id=9100707].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 3 Protection
   PL: [StartBattle] zyskuje 3 Ochrony
682. [Umiejętność wroga [9100708] (ulepszenie 1) — nazwa] 되돌려드립니다.
   źródło: Skills_Enemy.json :: dataList[id=9100708].levelList[level=1].name
   limit: do 40 znaków
   EN: Let me return the favor.
   PL: Let me return the favor.
683. [Umiejętność wroga [9100708] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이전 턴에 맞은 코인 수만큼 진동 부여.
   źródło: Skills_Enemy.json :: dataList[id=9100708].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Tremor by the number of Coins that hit last turn
   PL: [OnSucceedAttack] nakłada Wstrząs w liczbie równej liczbie Monet, które trafiły w poprzedniej turze
684. [Umiejętność wroga [9100708] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9100708].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Umiejętność wroga [9005101] (ulepszenie 1) — nazwa] 어지러울거다
   źródło: Skills_Enemy.json :: dataList[id=9005101].levelList[level=1].name
   limit: do 40 znaków
   EN: This'll Throw You Off
   PL: This'll Throw You Off
686. [Umiejętność wroga [9005101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 3 증가
   źródło: Skills_Enemy.json :: dataList[id=9005101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Tremor Count
   PL: [OnSucceedAttack] zwiększa Licznik [Vibration] o 3
687. [Umiejętność wroga [9005102] (ulepszenie 1) — nazwa] 진동 가속
   źródło: Skills_Enemy.json :: dataList[id=9005102].levelList[level=1].name
   limit: do 40 znaków
   EN: Vibration Acceleration
   PL: Vibration Acceleration
688. [Umiejętność wroga [9005102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 진동 횟수만큼 진동 횟수 증가
   źródło: Skills_Enemy.json :: dataList[id=9005102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Double target’s Tremor Count
   PL: [OnSucceedAttack] podwaja Licznik Wstrząsu celu
689. [Umiejętność wroga [9005103] (ulepszenie 1) — nazwa] 마무리다!
   źródło: Skills_Enemy.json :: dataList[id=9005103].levelList[level=1].name
   limit: do 40 znaków
   EN: This is It!
   PL: This is It!
690. [Umiejętność wroga [9005103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9005103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Umiejętność wroga [9005103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9005103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Umiejętność wroga [9005104] (ulepszenie 1) — nazwa] 시동 걸기
   źródło: Skills_Enemy.json :: dataList[id=9005104].levelList[level=1].name
   limit: do 40 znaków
   EN: Rev Up
   PL: Rozkręcanie
693. [Umiejętność wroga [9005104] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 진동 동화 1 얻음
   źródło: Skills_Enemy.json :: dataList[id=9005104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Tremor Sync next turn
   PL: [WhenUse] zyskuje 1 Synchronizację Wstrząsu w następnej turze
694. [Umiejętność wroga [9005201] (ulepszenie 1) — nazwa] 이거나 먹어라!
   źródło: Skills_Enemy.json :: dataList[id=9005201].levelList[level=1].name
   limit: do 40 znaków
   EN: Eat This!
   PL: Eat This!
695. [Umiejętność wroga [9005201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Tremor
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
696. [Umiejętność wroga [9005202] (ulepszenie 1) — nazwa] 진동 증폭
   źródło: Skills_Enemy.json :: dataList[id=9005202].levelList[level=1].name
   limit: do 40 znaków
   EN: Vibration Amplification
   PL: Vibration Amplification
697. [Umiejętność wroga [9005202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 진동만큼 진동 부여
   źródło: Skills_Enemy.json :: dataList[id=9005202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Tremor by target's Tremor
   PL: [OnSucceedAttack] nakłada Wstrząs w liczbie równej Wstrząsowi celu
698. [Umiejętność wroga [9005203] (ulepszenie 1) — nazwa] 끝이다!
   źródło: Skills_Enemy.json :: dataList[id=9005203].levelList[level=1].name
   limit: do 40 znaków
   EN: It's Over!
   PL: It's Over!
699. [Umiejętność wroga [9005203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Tremor
   PL: [OnSucceedAttackHead] Nakłada 2 [Vibration]
700. [Umiejętność wroga [9005203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 699 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Umiejętność wroga [9005203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9005203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Umiejętność wroga [9005204] (ulepszenie 1) — nazwa] 시동 걸기
   źródło: Skills_Enemy.json :: dataList[id=9005204].levelList[level=1].name
   (powtórzenie elementu 692 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Umiejętność wroga [9005204] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 진동 동화 1 얻음
   źródło: Skills_Enemy.json :: dataList[id=9005204].levelList[level=1].desc
   (powtórzenie elementu 693 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Umiejętność wroga [9005301] (ulepszenie 1) — nazwa] 마찰 가속
   źródło: Skills_Enemy.json :: dataList[id=9005301].levelList[level=1].name
   limit: do 40 znaków
   EN: Friction Escalation
   PL: Friction Escalation
705. [Umiejętność wroga [9005301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9005301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Tremor
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]
706. [Umiejętność wroga [9005301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9005301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Rupture
   PL: [OnSucceedAttackHead] Nakłada 1 Rozdarcia
707. [Umiejętność wroga [9005301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9005301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 705 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [Umiejętność wroga [9005301] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005301].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Umiejętność wroga [9005301] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9005301].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 705 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Umiejętność wroga [9005301] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9005301].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 595 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Umiejętność wroga [9005302] (ulepszenie 1) — nazwa] 갈아내주마!
   źródło: Skills_Enemy.json :: dataList[id=9005302].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Grind You Up!
   PL: I'll Grind You Up!
712. [Umiejętność wroga [9005302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 695 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Umiejętność wroga [9005302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9005302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 595 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Umiejętność wroga [9005303] (ulepszenie 1) — nazwa] 진동진동
   źródło: Skills_Enemy.json :: dataList[id=9005303].levelList[level=1].name
   limit: do 40 znaków
   EN: Quaker Shaker
   PL: Quaker Shaker
715. [Umiejętność wroga [9005303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 코인 1, 2가 앞면이라면, 대상의 진동만큼 진동 부여
   źródło: Skills_Enemy.json :: dataList[id=9005303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If Coins 1 & 2 land Heads, inflict Tremor by target's Tremor
   PL: [OnSucceedAttack] jeżeli Monety 1 i 2 wypadną jako Awers, nakłada Wstrząs w liczbie równej Wstrząsowi celu
716. [Umiejętność wroga [9005303] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 코인 1, 2가 앞면이라면, 스킬의 코인 앞면 수만큼 파열 부여
   źródło: Skills_Enemy.json :: dataList[id=9005303].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If Coins 1 & 2 land Heads, inflict Tremor by the number of Heads this skill lands
   PL: [OnSucceedAttack] jeżeli Monety 1 i 2 wypadną jako Awers, nakłada Wstrząs w liczbie równej liczbie Awersów tej Umiejętności
717. [Umiejętność wroga [9005304] (ulepszenie 1) — nazwa] 시동 걸기
   źródło: Skills_Enemy.json :: dataList[id=9005304].levelList[level=1].name
   (powtórzenie elementu 692 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [Umiejętność wroga [9005304] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 진동 동화 1 얻음
   źródło: Skills_Enemy.json :: dataList[id=9005304].levelList[level=1].desc
   (powtórzenie elementu 693 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Umiejętność wroga [9100801] (ulepszenie 1) — nazwa] 물러나세요!
   źródło: Skills_Enemy.json :: dataList[id=9100801].levelList[level=1].name
   limit: do 40 znaków
   EN: Stand Back!
   PL: Stand Back!
720. [Umiejętność wroga [9100801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 695 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Umiejętność wroga [9100802] (ulepszenie 1) — nazwa] 조금 울릴겁니다!
   źródło: Skills_Enemy.json :: dataList[id=9100802].levelList[level=1].name
   limit: do 40 znaków
   EN: This'll be Wobbly!
   PL: This'll be Wobbly!
722. [Umiejętność wroga [9100802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 695 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Umiejętność wroga [9100802] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 대상이 가지고 있는 진동만큼 마비 부여
   źródło: Skills_Enemy.json :: dataList[id=9100802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict Paralyze by target's Tremor next turn
   PL: [OnSucceedAttackHead] nakłada Paraliż w liczbie równej Wstrząsowi celu w następnej turze
724. [Umiejętność wroga [9100803] (ulepszenie 1) — nazwa] 강력 증폭
   źródło: Skills_Enemy.json :: dataList[id=9100803].levelList[level=1].name
   limit: do 40 znaków
   EN: Turbo Amp
   PL: Turbo Amp
725. [Umiejętność wroga [9100803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 가지고 있는 진동만큼 진동 부여
   źródło: Skills_Enemy.json :: dataList[id=9100803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Tremor by target's Tremor
   PL: [OnSucceedAttack] nakłada Wstrząs w liczbie równej Wstrząsowi celu
726. [Umiejętność wroga [9100804] (ulepszenie 1) — nazwa] 진동 변환
   źródło: Skills_Enemy.json :: dataList[id=9100804].levelList[level=1].name
   limit: do 40 znaków
   EN: Trembling Conversion
   PL: Trembling Conversion
727. [Umiejętność wroga [9100804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 695 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Umiejętność wroga [9100804] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상이 가지고 있는 진동만큼 진동 부여
   źródło: Skills_Enemy.json :: dataList[id=9100804].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Umiejętność wroga [9100804] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 대상이 가지고 있는 진동만큼 마비 부여
   źródło: Skills_Enemy.json :: dataList[id=9100804].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 723 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Umiejętność wroga [9100805] (ulepszenie 1) — nazwa] 진동 압착
   źródło: Skills_Enemy.json :: dataList[id=9100805].levelList[level=1].name
   limit: do 40 znaków
   EN: Vibration Compression
   PL: Vibration Compression
731. [Umiejętność wroga [9100805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 699 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Umiejętność wroga [9100805] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100805].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 699 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Umiejętność wroga [9100805] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9100805].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Umiejętność wroga [9100806] (ulepszenie 1) — nazwa] 한탕 해보죠
   źródło: Skills_Enemy.json :: dataList[id=9100806].levelList[level=1].name
   limit: do 40 znaków
   EN: Let's Sweep the Stakes
   PL: Let's Sweep the Stakes
735. [Umiejętność wroga [9100806] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 10만큼 흐트러짐 손상
   źródło: Skills_Enemy.json :: dataList[id=9100806].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 10
   PL: [OnSucceedAttack] podnosi Próg Oszołomienia o 10
736. [Umiejętność wroga [9100806] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 20만큼 흐트러짐 손상
   źródło: Skills_Enemy.json :: dataList[id=9100806].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Raise Stagger Threshold by 20
   PL: [OnSucceedAttackHead] podnosi Próg Oszołomienia o 20
737. [Umiejętność wroga [9100807] (ulepszenie 1) — nazwa] 마지막 예열
   źródło: Skills_Enemy.json :: dataList[id=9100807].levelList[level=1].name
   limit: do 40 znaków
   EN: Final Warmup
   PL: Final Warmup
738. [Umiejętność wroga [9100807] (ulepszenie 1) — opis] [StartBattle] 보호 4 얻음.\n정신력 15 회복
   źródło: Skills_Enemy.json :: dataList[id=9100807].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 4 Protection\nHeal 15 SP
   PL: [StartBattle] zyskuje 4 Ochrony\nprzywraca 15 Poczytalności
739. [Umiejętność wroga [9005401] (ulepszenie 1) — nazwa] 침입자 저지
   źródło: Skills_Enemy.json :: dataList[id=9005401].levelList[level=1].name
   limit: do 40 znaków
   EN: Stop the Intruder
   PL: Stop the Intruder
740. [Umiejętność wroga [9005401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills_Enemy.json :: dataList[id=9005401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
741. [Umiejętność wroga [9005402] (ulepszenie 1) — nazwa] 출입 금지
   źródło: Skills_Enemy.json :: dataList[id=9005402].levelList[level=1].name
   limit: do 40 znaków
   EN: No Entry
   PL: No Entry
742. [Umiejętność wroga [9005402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL: [OnSucceedAttack] Nakłada 2 Rozdarcia
743. [Umiejętność wroga [9005403] (ulepszenie 1) — nazwa] 출입 차단
   źródło: Skills_Enemy.json :: dataList[id=9005403].levelList[level=1].name
   limit: do 40 znaków
   EN: Forbid Entry
   PL: Forbid Entry
744. [Umiejętność wroga [9005403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 취약 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 645 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Umiejętność wroga [9005404] (ulepszenie 1) — nazwa] 엄폐 엄폐!
   źródło: Skills_Enemy.json :: dataList[id=9005404].levelList[level=1].name
   limit: do 40 znaków
   EN: Cover, Cover!
   PL: Cover, Cover!
746. [Umiejętność wroga [9005404] (ulepszenie 1) — opis] [StartBattle] 전체 체력 5%만큼 체력 회복
   źródło: Skills_Enemy.json :: dataList[id=9005404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Heal 5% of Max HP
   PL: [StartBattle] przywraca HP równe 5% Maks. HP
747. [Umiejętność wroga [9005501] (ulepszenie 1) — nazwa] 일시 정지! 정지!
   źródło: Skills_Enemy.json :: dataList[id=9005501].levelList[level=1].name
   limit: do 40 znaków
   EN: Pause! Halt!
   PL: Pause! Halt!
748. [Umiejętność wroga [9005501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 695 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [Umiejętność wroga [9005502] (ulepszenie 1) — nazwa] 멈추십시오!
   źródło: Skills_Enemy.json :: dataList[id=9005502].levelList[level=1].name
   limit: do 40 znaków
   EN: Stop There, Please!
   PL: Stop There, Please!
750. [Umiejętność wroga [9005502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 695 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Umiejętność wroga [9005502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 진동 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9005502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Tremor
   PL: [OnSucceedAttackHead] Nakłada 3 Wstrząsu
752. [Umiejętność wroga [9005503] (ulepszenie 1) — nazwa] 구속합니다!
   źródło: Skills_Enemy.json :: dataList[id=9005503].levelList[level=1].name
   limit: do 40 znaków
   EN: Arresting!
   PL: Arresting!
753. [Umiejętność wroga [9005503] (ulepszenie 1) — opis] 진동이 있는 대상 우선 공격
   źródło: Skills_Enemy.json :: dataList[id=9005503].levelList[level=1].desc
   (powtórzenie elementu 672 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Umiejętność wroga [9005503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9005503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Umiejętność wroga [9005504] (ulepszenie 1) — nazwa] 엄폐합니다!
   źródło: Skills_Enemy.json :: dataList[id=9005504].levelList[level=1].name
   limit: do 40 znaków
   EN: Taking Cover!
   PL: Taking Cover!
756. [Umiejętność wroga [9005504] (ulepszenie 1) — opis] [StartBattle] 전체 체력 5%만큼 체력 회복
   źródło: Skills_Enemy.json :: dataList[id=9005504].levelList[level=1].desc
   (powtórzenie elementu 746 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Umiejętność wroga [9005601] (ulepszenie 1) — nazwa] HP 앰플 투약합니다.
   źródło: Skills_Enemy.json :: dataList[id=9005601].levelList[level=1].name
   limit: do 40 znaków
   EN: Administering HP Ampule
   PL: Administering HP Ampule
758. [Umiejętność wroga [9005601] (ulepszenie 1) — opis] [CantDuel][WhenUse] 아군을 타겟으로 지정\n피해량만큼 체력 회복.\n피해량은 0이 됨.
   źródło: Skills_Enemy.json :: dataList[id=9005601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]
   EN: [CantDuel][WhenUse] Targets allies\nHeal by damage number\nDeals no damage
   PL: [CantDuel][WhenUse] celuje w sojuszników\nprzywraca HP równe liczbie obrażeń\nnie zadaje obrażeń
759. [Umiejętność wroga [9005602] (ulepszenie 1) — nazwa] 방어 앰플 투약합니다.
   źródło: Skills_Enemy.json :: dataList[id=9005602].levelList[level=1].name
   limit: do 50 znaków
   EN: Administering Resister Ampule
   PL: Administering Resister Ampule
760. [Umiejętność wroga [9005602] (ulepszenie 1) — opis] [CantDuel][WhenUse] 아군을 타겟으로 지정\n무작위 속성 보호를 1 부여.\n피해량은 0이 됨.
   źródło: Skills_Enemy.json :: dataList[id=9005602].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]
   EN: [CantDuel][WhenUse] Targets allies\nGive 1 Protection against a random affinity\nDeals no damage
   PL: [CantDuel][WhenUse] celuje w sojuszników\ndaje 1 Ochronę przed losowym Atrybutem\nnie zadaje obrażeń
761. [Umiejętność wroga [9005603] (ulepszenie 1) — nazwa] 붕괴 앰플 발사 발사
   źródło: Skills_Enemy.json :: dataList[id=9005603].levelList[level=1].name
   limit: do 40 znaków
   EN: Firing Decay Ampule
   PL: Firing Decay Ampule
762. [Umiejętność wroga [9005603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 붕괴 앰플 1 부여.\n다음 턴에 마비 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9005603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Decay Ampule\nInflict 1 Paralyze next turn
   PL: [OnSucceedAttack] nakłada 1 Ampułkę Rozkładu\nnakłada 1 Paraliżu w następnej turze
763. [Umiejętność wroga [9005604] (ulepszenie 1) — nazwa] 회피 기동합니다.
   źródło: Skills_Enemy.json :: dataList[id=9005604].levelList[level=1].name
   limit: do 40 znaków
   EN: Initiating evasive maneuver.
   PL: Initiating evasive maneuver.
764. [Umiejętność wroga [9005701] (ulepszenie 1) — nazwa] 붕괴 앰플 긴급 발사
   źródło: Skills_Enemy.json :: dataList[id=9005701].levelList[level=1].name
   limit: do 40 znaków
   EN: Discharging Decay Ampule
   PL: Discharging Decay Ampule
765. [Umiejętność wroga [9005701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Paralyze next turn
   PL: [OnSucceedAttack] nakłada 2 Paraliżu w następnej turze
766. [Umiejętność wroga [9005701] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 붕괴 앰플 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005701].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Decay Ampule
   PL: [OnSucceedAttackHead] nakłada 2 Ampułki Rozkładu
767. [Umiejętność wroga [9005702] (ulepszenie 1) — nazwa] 약점 약점을 드러냅니다.
   źródło: Skills_Enemy.json :: dataList[id=9005702].levelList[level=1].name
   limit: do 40 znaków
   EN: Exposing weakness.
   PL: Exposing weakness.
768. [Umiejętność wroga [9005702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9005702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 627 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Umiejętność wroga [9005702] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 취약 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 645 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Umiejętność wroga [9005702] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttackHead] 붕괴 앰플 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9005702].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Decay Ampule
   PL: [OnSucceedAttackHead] nakłada 3 Ampułki Rozkładu
771. [Umiejętność wroga [9005703] (ulepszenie 1) — nazwa] 더 맞서 싸우십시오.
   źródło: Skills_Enemy.json :: dataList[id=9005703].levelList[level=1].name
   limit: do 40 znaków
   EN: Continue engaging.
   PL: Continue engaging.
772. [Umiejętność wroga [9005703] (ulepszenie 1) — opis] [CantDuel] 아군을 타겟으로 지정
   źródło: Skills_Enemy.json :: dataList[id=9005703].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel] Targets allies
   PL: [CantDuel] celuje w sojuszników
773. [Umiejętność wroga [9005703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 피해량 증가 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Give 2 Damage Up next turn
   PL: [OnSucceedAttack] nakłada 2 Wzrost Obrażeń w następnej turze
774. [Umiejętność wroga [9005704] (ulepszenie 1) — nazwa] 몸을 아끼지 마십시오.
   źródło: Skills_Enemy.json :: dataList[id=9005704].levelList[level=1].name
   limit: do 50 znaków
   EN: Do not reserve your strength.
   PL: Do not reserve your strength.
775. [Umiejętność wroga [9005704] (ulepszenie 1) — opis] [CantDuel] 아군을 타겟으로 지정
   źródło: Skills_Enemy.json :: dataList[id=9005704].levelList[level=1].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [Umiejętność wroga [9005704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 공격 위력 증가 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Give 2 Attack Power Up next turn
   PL: [OnSucceedAttack] nakłada 2 Wzrost Mocy Ataku w następnej turze
777. [Umiejętność wroga [9005704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 취약 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9005704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 534 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Umiejętność wroga [9005705] (ulepszenie 1) — nazwa] 물러납니다.
   źródło: Skills_Enemy.json :: dataList[id=9005705].levelList[level=1].name
   limit: do 40 znaków
   EN: Retreating.
   PL: Retreating.
779. [Umiejętność wroga [9005901] (ulepszenie 1) — nazwa] 상처 저주
   źródło: Skills_Enemy.json :: dataList[id=9005901].levelList[level=1].name
   limit: do 40 znaków
   EN: Harming Curse
   PL: Harming Curse
780. [Umiejętność wroga [9005901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills_Enemy.json :: dataList[id=9005901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Umiejętność wroga [9005902] (ulepszenie 1) — nazwa] 늘어나는 저주
   źródło: Skills_Enemy.json :: dataList[id=9005902].levelList[level=1].name
   limit: do 40 znaków
   EN: Proliferating Curse
   PL: Proliferating Curse
782. [Umiejętność wroga [9005902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Enemy.json :: dataList[id=9005902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Rupture Count
   PL: [OnSucceedAttack] Zwiększa Licznik Rozdarcia o 2
783. [Umiejętność wroga [9005902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Enemy.json :: dataList[id=9005902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 782 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Umiejętność wroga [9005903] (ulepszenie 1) — nazwa] 벌어진 상처
   źródło: Skills_Enemy.json :: dataList[id=9005903].levelList[level=1].name
   limit: do 40 znaków
   EN: Opened Wound
   PL: Opened Wound
785. [Umiejętność wroga [9005903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9005903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 603 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Umiejętność wroga [9005904] (ulepszenie 1) — nazwa] 방어 부적
   źródło: Skills_Enemy.json :: dataList[id=9005904].levelList[level=1].name
   limit: do 40 znaków
   EN: Defensive Talisman
   PL: Defensive Talisman
787. [Umiejętność wroga [9005801] (ulepszenie 1) — nazwa] 제압 액체
   źródło: Skills_Enemy.json :: dataList[id=9005801].levelList[level=1].name
   limit: do 40 znaków
   EN: Suppressing Fluid
   PL: Suppressing Fluid
788. [Umiejętność wroga [9005801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9005801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bind next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Spętania
789. [Umiejętność wroga [9005802] (ulepszenie 1) — nazwa] 폭발하는 액체
   źródło: Skills_Enemy.json :: dataList[id=9005802].levelList[level=1].name
   limit: do 40 znaków
   EN: Explosive Fluid
   PL: Explosive Fluid
790. [Umiejętność wroga [9005802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9005802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Umiejętność wroga [9005803] (ulepszenie 1) — nazwa] 흔들리는 액체
   źródło: Skills_Enemy.json :: dataList[id=9005803].levelList[level=1].name
   limit: do 40 znaków
   EN: Wobbling Fluid
   PL: Wobbling Fluid
792. [Umiejętność wroga [9005803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9005803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 636 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Umiejętność wroga [9005803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9005803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Tremor Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]
794. [Umiejętność wroga [9005804] (ulepszenie 1) — nazwa] 액체막이
   źródło: Skills_Enemy.json :: dataList[id=9005804].levelList[level=1].name
   limit: do 40 znaków
   EN: Fluid Guard
   PL: Fluid Guard
795. [Umiejętność wroga [9006101] (ulepszenie 1) — nazwa] 상처 저주
   źródło: Skills_Enemy.json :: dataList[id=9006101].levelList[level=1].name
   (powtórzenie elementu 779 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Umiejętność wroga [9006101] (ulepszenie 1) — opis] [WhenUse] 얽혀온 저주 부적 1 얻음
   źródło: Skills_Enemy.json :: dataList[id=9006101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Entangled Curse Talisman
   PL: [WhenUse] zyskuje 1 Splątany Talizman Przekleństwa
797. [Umiejętność wroga [9006101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills_Enemy.json :: dataList[id=9006101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Umiejętność wroga [9006102] (ulepszenie 1) — nazwa] 늘어나는 저주
   źródło: Skills_Enemy.json :: dataList[id=9006102].levelList[level=1].name
   (powtórzenie elementu 781 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Umiejętność wroga [9006102] (ulepszenie 1) — opis] [WhenUse] 얽혀온 저주 부적 2 얻음
   źródło: Skills_Enemy.json :: dataList[id=9006102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Entangled Curse Talisman
   PL: [WhenUse] zyskuje 2 Splątane Talizmany Przekleństwa
800. [Umiejętność wroga [9006102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Enemy.json :: dataList[id=9006102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 782 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Umiejętność wroga [9006102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Enemy.json :: dataList[id=9006102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 782 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Umiejętność wroga [9006103] (ulepszenie 1) — nazwa] 속박 저주
   źródło: Skills_Enemy.json :: dataList[id=9006103].levelList[level=1].name
   limit: do 40 znaków
   EN: Restraining Curse
   PL: Restraining Curse
803. [Umiejętność wroga [9006103] (ulepszenie 1) — opis] [WhenUse] 얽혀온 저주 부적 2 얻음
   źródło: Skills_Enemy.json :: dataList[id=9006103].levelList[level=1].desc
   (powtórzenie elementu 799 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Umiejętność wroga [9006103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9006103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bind next turn
   PL: [OnSucceedAttackHead] nakłada 2 Spętania w następnej turze
805. [Umiejętność wroga [9006104] (ulepszenie 1) — nazwa] 부각된 상처
   źródło: Skills_Enemy.json :: dataList[id=9006104].levelList[level=1].name
   limit: do 40 znaków
   EN: Pronounced Wound
   PL: Pronounced Wound
806. [Umiejętność wroga [9006104] (ulepszenie 1) — opis] [EndBattle] 얽혀온 저주 부적 전부 소멸
   źródło: Skills_Enemy.json :: dataList[id=9006104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndBattle]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [EndBattle] Remove all Entangled Curse Talisman
   PL: [EndBattle] usuwa wszystkie Splątane Talizmany Przekleństwa
807. [Umiejętność wroga [9006104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Enemy.json :: dataList[id=9006104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 782 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Umiejętność wroga [9006104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Enemy.json :: dataList[id=9006104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 782 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Umiejętność wroga [9006104] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9006104].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind next turn
   PL: [OnSucceedAttack] nakłada 2 Spętania w następnej turze
810. [Umiejętność wroga [9006104] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 파열 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9006104].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 648 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Umiejętność wroga [9006105] (ulepszenie 1) — nazwa] 방어 부적
   źródło: Skills_Enemy.json :: dataList[id=9006105].levelList[level=1].name
   (powtórzenie elementu 786 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
812. [Umiejętność wroga [9006001] (ulepszenie 1) — nazwa] 제압 액체
   źródło: Skills_Enemy.json :: dataList[id=9006001].levelList[level=1].name
   (powtórzenie elementu 787 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [Umiejętność wroga [9006001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9006001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 809 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Umiejętność wroga [9006002] (ulepszenie 1) — nazwa] 폭발하는 액체
   źródło: Skills_Enemy.json :: dataList[id=9006002].levelList[level=1].name
   (powtórzenie elementu 789 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Umiejętność wroga [9006002] (ulepszenie 1) — opis] [WhenUse] 고양 1 얻음
   źródło: Skills_Enemy.json :: dataList[id=9006002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Morale Boost
   PL: [WhenUse] zyskuje 1 Uniesienia
816. [Umiejętność wroga [9006002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy.json :: dataList[id=9006002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Umiejętność wroga [9006003] (ulepszenie 1) — nazwa] 흔들리는 액체
   źródło: Skills_Enemy.json :: dataList[id=9006003].levelList[level=1].name
   (powtórzenie elementu 791 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Umiejętność wroga [9006003] (ulepszenie 1) — opis] [WhenUse] 고양 1 얻음
   źródło: Skills_Enemy.json :: dataList[id=9006003].levelList[level=1].desc
   (powtórzenie elementu 815 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Umiejętność wroga [9006003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 4 부여
   źródło: Skills_Enemy.json :: dataList[id=9006003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Tremor
   PL: [OnSucceedAttack] Nakłada 4 Wstrząsu
820. [Umiejętność wroga [9006003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9006003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 793 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
821. [Umiejętność wroga [9006004] (ulepszenie 1) — nazwa] 액체막이
   źródło: Skills_Enemy.json :: dataList[id=9006004].levelList[level=1].name
   (powtórzenie elementu 794 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
822. [Umiejętność wroga [9006004] (ulepszenie 1) — opis] [WhenUse] 전체 체력의 5%만큼 체력 회복.\n다음 턴에 취약 2 얻음.\n[EndBattle] 취기 전부 소멸
   źródło: Skills_Enemy.json :: dataList[id=9006004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [WhenUse] Heal 5% of Max HP\nGain 2 Fragile next turn\n[EndBattle] Remove all Tipsy
   PL: [WhenUse] przywraca HP równe 5% Maks. HP\nzyskuje 2 Wrażliwości w następnej turze\n[EndBattle] usuwa cały Pijacki Nastrój
823. [Umiejętność wroga [9100901] (ulepszenie 1) — nazwa] 속박하는 저주
   źródło: Skills_Enemy.json :: dataList[id=9100901].levelList[level=1].name
   limit: do 40 znaków
   EN: Restraining Curse
   PL: Restraining Curse
824. [Umiejętność wroga [9100901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 809 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Umiejętność wroga [9100902] (ulepszenie 1) — nazwa] 타격 저주
   źródło: Skills_Enemy.json :: dataList[id=9100902].levelList[level=1].name
   limit: do 40 znaków
   EN: Blunt Curse
   PL: Blunt Curse
826. [Umiejętność wroga [9100902] (ulepszenie 1) — opis] [WhenUse] 다시 붙여진 저주 부적 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9100902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict 1 Reattached Curse Talisman
   PL: [WhenUse] nakłada 1 Ponownie Przyklejony Talizman Przekleństwa
827. [Umiejętność wroga [9100902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 타격 취약 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9100902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Blunt Fragility
   PL: [OnSucceedAttack] nakłada 3 Kruchości Uderzenia
828. [Umiejętność wroga [9100903] (ulepszenie 1) — nazwa] 증식하는 부적
   źródło: Skills_Enemy.json :: dataList[id=9100903].levelList[level=1].name
   limit: do 40 znaków
   EN: Multiplying Talismans
   PL: Multiplying Talismans
829. [Umiejętność wroga [9100903] (ulepszenie 1) — opis] 파열이 가장 많은 대상 우선 공격
   źródło: Skills_Enemy.json :: dataList[id=9100903].levelList[level=1].desc
   limit: do 120 znaków
   EN: Targets the enemy with the most Rupture
   PL: priorytet: wrogowie z największą liczbą Rozdarcia
830. [Umiejętność wroga [9100903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다시 붙여진 저주 부적만큼 파열 부여
   źródło: Skills_Enemy.json :: dataList[id=9100903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Rupture by the amount of Reattached Curse Talisman on target
   PL: [OnSucceedAttack] nakłada Rozdarcie w liczbie równej liczbie Ponownie Przyklejonych Talizmanów Przekleństwa celu
831. [Umiejętność wroga [9100904] (ulepszenie 1) — nazwa] 마비되는 저주
   źródło: Skills_Enemy.json :: dataList[id=9100904].levelList[level=1].name
   limit: do 40 znaków
   EN: Paralyzing Curse
   PL: Paralyzing Curse
832. [Umiejętność wroga [9100904] (ulepszenie 1) — opis] [EndBattle] 대상의 다시 붙여진 저주 부적 전부 소멸
   źródło: Skills_Enemy.json :: dataList[id=9100904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndBattle]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [EndBattle] Remove all Reattached Curse Talisman from target
   PL: [EndBattle] usuwa wszystkie Ponownie Przyklejone Talizmany Przekleństwa celu
833. [Umiejętność wroga [9100904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9100904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 603 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Umiejętność wroga [9100904] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다시 붙여진 저주 부적만큼 마비 부여
   źródło: Skills_Enemy.json :: dataList[id=9100904].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Paralyze by the amount of Reattached Curse Talisman on target
   PL: [OnSucceedAttack] nakłada Paraliż w liczbie równej liczbie Ponownie Przyklejonych Talizmanów Przekleństwa celu
835. [Umiejętność wroga [9100905] (ulepszenie 1) — nazwa] 옭아매는 저주 부적
   źródło: Skills_Enemy.json :: dataList[id=9100905].levelList[level=1].name
   limit: do 40 znaków
   EN: Strangling Curse Talisman
   PL: Strangling Curse Talisman
836. [Umiejętność wroga [9100905] (ulepszenie 1) — opis] 다시 붙여진 저주 부적이 가장 많은 대상 우선 공격
   źródło: Skills_Enemy.json :: dataList[id=9100905].levelList[level=1].desc
   limit: do 120 znaków
   EN: Target the enemy with the most Reattached Curse Talismans
   PL: priorytet: wrogowie z największą liczbą Ponownie Przyklejonych Talizmanów Przekleństwa
837. [Umiejętność wroga [9100905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다시 붙여진 저주 부적 5 부여
   źródło: Skills_Enemy.json :: dataList[id=9100905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Reattached Curse Talisman
   PL: [OnSucceedAttack] nakłada 5 Ponownie Przyklejonych Talizmanów Przekleństwa
838. [Umiejętność wroga [9100906] (ulepszenie 1) — nazwa] 소멸되는 저주 부적
   źródło: Skills_Enemy.json :: dataList[id=9100906].levelList[level=1].name
   limit: do 40 znaków
   EN: Expiring Curse Talisman
   PL: Expiring Curse Talisman
839. [Umiejętność wroga [9100906] (ulepszenie 1) — opis] 다시 붙여진 저주 부적이 가장 많은 대상 우선 공격\n[EndBattle] 대상의 다시 붙여진 저주 부적 전부 소멸
   źródło: Skills_Enemy.json :: dataList[id=9100906].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [EndBattle]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]
   EN: Target the enemy with the most Reattached Curse Talismans\n[EndBattle] Remove all Reattached Curse Talisman from target
   PL: priorytet: cel z największą liczbą Ponownie Przyklejonych Talizmanów Przekleństwa\n[EndBattle] usuwa wszystkie Ponownie Przyklejone Talizmany Przekleństwa celu
840. [Umiejętność wroga [9100906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다시 붙여진 저주 부적 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Reattached Curse Talisman
   PL: [OnSucceedAttack] nakłada 2 Ponownie Przyklejone Talizmany Przekleństwa
841. [Umiejętność wroga [9100906] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다시 붙여진 저주 부적이 9이상이라면, 마비 5 부여.\n피해량의 50%만큼 고정 피해
   źródło: Skills_Enemy.json :: dataList[id=9100906].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] If target has 9+ Reattached Curse Talisman, inflict 5 Paralyze\nDeal fixed damage by 50% of damage dealt
   PL: [OnSucceedAttackHead] jeżeli cel ma 9+ Ponownie Przyklejonych Talizmanów Przekleństwa, nakłada 5 Paraliżu\nzadaje stałe obrażenia równe 50% zadanych obrażeń
842. [Umiejętność wroga [9100907] (ulepszenie 1) — nazwa] 옮겨가는 저주 부적
   źródło: Skills_Enemy.json :: dataList[id=9100907].levelList[level=1].name
   limit: do 40 znaków
   EN: Spreading Curse Talisman
   PL: Spreading Curse Talisman
843. [Umiejętność wroga [9100907] (ulepszenie 1) — opis] [WhenUse] 다시 붙여진 저주 부적 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9100907].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict 2 Reattached Curse Talisman
   PL: [WhenUse] nakłada 2 Ponownie Przyklejone Talizmany Przekleństwa
844. [Umiejętność wroga [9101001] (ulepszenie 1) — nazwa] 소멸되는 저주 부적
   źródło: Skills_Enemy.json :: dataList[id=9101001].levelList[level=1].name
   (powtórzenie elementu 838 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Umiejętność wroga [9101001] (ulepszenie 1) — opis] 다시 붙여진 저주 부적이 가장 많은 대상 우선 공격\n[EndBattle] 대상의 다시 붙여진 저주 부적 전부 소멸
   źródło: Skills_Enemy.json :: dataList[id=9101001].levelList[level=1].desc
   (powtórzenie elementu 839 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
846. [Umiejętność wroga [9101001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다시 붙여진 저주 부적 2 부여
   źródło: Skills_Enemy.json :: dataList[id=9101001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 840 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Umiejętność wroga [9101001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackTail] 다시 붙여진 저주 부적이 9이상이라면, 마비 5 부여.\n피해량의 50%만큼 고정 피해
   źródło: Skills_Enemy.json :: dataList[id=9101001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] If target has 9+ Reattached Curse Talisman, inflict 5 Paralyze\nDeal fixed damage by 50% of damage dealt
   PL: [OnSucceedAttackTail] jeżeli cel ma 9+ Ponownie Przyklejonych Talizmanów Przekleństwa, nakłada 5 Paraliżu\nzadaje stałe obrażenia równe 50% zadanych obrażeń
848. [Umiejętność wroga [9006801] (ulepszenie 1) — nazwa] 거수자 발견
   źródło: Skills_Enemy.json :: dataList[id=9006801].levelList[level=1].name
   limit: do 40 znaków
   EN: Suspicious Individuals
   PL: Suspicious Individuals
849. [Umiejętność wroga [9006801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 파열 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9006801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 3 Rupture
   PL: [OnSucceedAttackTail] Nakłada 3 Rozdarcia
850. [Umiejętność wroga [9006802] (ulepszenie 1) — nazwa] 제압
   źródło: Skills_Enemy.json :: dataList[id=9006802].levelList[level=1].name
   limit: do 40 znaków
   EN: Restrain
   PL: Powstrzymanie
851. [Umiejętność wroga [9006802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 파열 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9006802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
852. [Umiejętność wroga [9006803] (ulepszenie 1) — nazwa] 거수자 차단
   źródło: Skills_Enemy.json :: dataList[id=9006803].levelList[level=1].name
   limit: do 40 znaków
   EN: No Trespassing
   PL: No Trespassing
853. [Umiejętność wroga [9006803] (ulepszenie 1) — opis] 체력이 가장 높은 대상 우선 공격
   źródło: Skills_Enemy.json :: dataList[id=9006803].levelList[level=1].desc
   limit: do 120 znaków
   EN: Targets the unit with the most HP
   PL: priorytet: cel z największym HP
854. [Umiejętność wroga [9006803] (ulepszenie 1) — moneta 2, efekt 1 — opis] 1코인이 뒷면이라면 피해량 +10%
   źródło: Skills_Enemy.json :: dataList[id=9006803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   EN: If Coin 1 lands Tails, +10% Damage
   PL: jeżeli Moneta 1 wypadnie jako Rewers, +10% obrażeń
855. [Umiejętność wroga [9006803] (ulepszenie 1) — moneta 3, efekt 1 — opis] 2코인이 뒷면이라면 피해량 +10%
   źródło: Skills_Enemy.json :: dataList[id=9006803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: If Coin 2 lands Tails, +10% Damage
   PL: jeżeli Moneta 2 wypadnie jako Rewers, +10% obrażeń
856. [Umiejętność wroga [9006803] (ulepszenie 1) — moneta 4, efekt 1 — opis] 2, 3코인이 뒷면이라면 피해량 +30%
   źródło: Skills_Enemy.json :: dataList[id=9006803].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: If Coins 2 & 3 land Tails, +30% Damage
   PL: jeżeli Monety 2 i 3 wypadną jako Rewers, +30% obrażeń
857. [Umiejętność wroga [9007001] (ulepszenie 1) — nazwa] 맞물리는 순간
   źródło: Skills_Enemy.json :: dataList[id=9007001].levelList[level=1].name
   limit: do 40 znaków
   EN: Interlocking Moment
   PL: Interlocking Moment
858. [Umiejętność wroga [9007001] (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9007001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +1 Charge Count
   PL: [WhenUse] Zwiększa własny Licznik Ładowania o 1
859. [Umiejętność wroga [9007001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 맞물리는 시간 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9007001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Interlocking Time
   PL: [OnSucceedAttack] nakłada 1 Sprzężonego Czasu
860. [Umiejętność wroga [9007001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 충전 횟수 2 소모 시, 마비 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9007001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 2 Charge Count to inflict 3 Paralyze
   PL: [OnSucceedAttack] zużywa 2 Liczniki Ładowania, by nałożyć 3 Paraliżu
861. [Umiejętność wroga [9007002] (ulepszenie 1) — nazwa] 시간 흡수
   źródło: Skills_Enemy.json :: dataList[id=9007002].levelList[level=1].name
   limit: do 40 znaków
   EN: Siphon Time
   PL: Siphon Time
862. [Umiejętność wroga [9007002] (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 1 증가
   źródło: Skills_Enemy.json :: dataList[id=9007002].levelList[level=1].desc
   (powtórzenie elementu 858 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Umiejętność wroga [9007002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여. 신속 1 얻음
   źródło: Skills_Enemy.json :: dataList[id=9007002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Haste; Inflict 2 Bind next turn
   PL: [OnSucceedAttack] zyskuje 1 Pośpiechu; nakłada 2 Spętania w następnej turze
864. [Umiejętność wroga [9007003] (ulepszenie 1) — nazwa] 가속되는 순간
   źródło: Skills_Enemy.json :: dataList[id=9007003].levelList[level=1].name
   limit: do 40 znaków
   EN: Accelerating Moment
   PL: Accelerating Moment
865. [Umiejętność wroga [9007003] (ulepszenie 1) — opis] [StartBattle] 자신의 충전 횟수 3 증가\n[WhenUse] 충전 횟수가 5이상 이라면, 합 위력+2.\n다음 턴에 행동 불가 상태가 됨.
   źródło: Skills_Enemy.json :: dataList[id=9007003].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Gain +3 Charge Count\n[WhenUse] At 5+ Charge Count, Clash Power +2\nBecome immobilized next turn
   PL: [StartBattle] zyskuje +3 Liczników Ładowania\n[WhenUse] przy 5+ Licznikach Ładowania, Moc Starcia +2\nw następnej turze nie może działać
866. [Umiejętność wroga [9007003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9007003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 788 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
