# Paczka AI P66 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 2/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P66_3c_przeciwnicy_i_anomalie_cz02.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P66_3c_przeciwnicy_i_anomalie_cz02.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Umiejętności jednostek wsparcia — Skills_Assist-a1c9p3
- plik gry: `Skills_Assist-a1c9p3.json`

1. [Umiejętność sojusznika [40000705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 10 부여. [Combustion] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 10 [Combustion] and +2 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 10 [Combustion] i zwiększa Licznik [Combustion] o 2
2. [Umiejętność sojusznika [40000801] (ulepszenie 1) — nazwa] 등불과 같은 눈
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000801].levelList[level=1].name
   limit: do 40 znaków
   EN: Eyes Bright Like Lamps
   PL: Eyes Bright Like Lamps
3. [Umiejętność sojusznika [40000801] (ulepszenie 1) — opis] [CanDuelGuard]\n공격자의 속도가 자신의 속도보다 높으면 속도 차이 2당, 코인 위력 +1 (최대 2)\n- 자신의 속도가 1이면, 대신 코인 위력 +2\n[StartBattle] [LanternHohenheimBigBird] 6 얻음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000801].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [LanternHohenheimBigBird]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [LanternHohenheimBigBird] = 램프 / Lamp
   EN: [CanDuelGuard]\nIf the target's Speed is faster than this unit's, Coin Power +1 for every 2 Speed difference (max 2)\n- At 1 Speed, Coin Power +2 instead\n[StartBattle] Gain 6 [LanternHohenheimBigBird]
   PL: [CanDuelGuard]\njeżeli Szybkość celu jest wyższa niż Szybkość tej jednostki, Moc Monety +1 za każde 2 różnicy Szybkości (maks. 2)\n- przy Szybkości 1 zamiast tego Moc Monety +2\n[StartBattle] zyskuje 6 [LanternHohenheimBigBird]
4. [Umiejętność sojusznika [40000802] (ulepszenie 1) — nazwa] 속사
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000802].levelList[level=1].name
   limit: do 40 znaków
   EN: Rapid Fire
   PL: Rapid Fire
5. [Umiejętność sojusznika [40000802] (ulepszenie 1) — opis] 대상의 속도가 자신보다 높으면 속도 차이 2당, 코인 위력 +1 (최대 2)\n- 자신의 속도가 1이면, 대신 코인 위력 +2\n[WhenUse] [LanternHohenheimBigBird] 5 얻음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000802].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [LanternHohenheimBigBird]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [LanternHohenheimBigBird] = 램프 / Lamp
   EN: If the target's Speed is faster than this unit's, Coin Power +1 for every 2 Speed difference (max 2)\n- At 1 Speed, Coin Power +2 instead\n[WhenUse] Gain 5 [LanternHohenheimBigBird]
   PL: [WhenUse] jeżeli Szybkość celu jest wyższa niż Szybkość tej jednostki, Moc Monety +1 za każde 2 różnicy Szybkości (maks. 2)\n- przy Szybkości 1 zamiast tego Moc Monety +2\n[WhenUse] zyskuje 5 [LanternHohenheimBigBird]
6. [Umiejętność sojusznika [40000802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여. [Combustion] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion] and +1 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 2 [Combustion] i zwiększa Licznik [Combustion] o 1
7. [Umiejętność sojusznika [40000802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여. [Sinking] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking] and +1 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 3 [Sinking] i zwiększa Licznik [Sinking] o 1
8. [Umiejętność sojusznika [40000803] (ulepszenie 1) — nazwa] 영거리 주시
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000803].levelList[level=1].name
   limit: do 40 znaków
   EN: Intense Stare: Zero-Range
   PL: Intense Stare: Zero-Range
9. [Umiejętność sojusznika [40000803] (ulepszenie 1) — opis] 대상의 속도가 자신보다 높으면 속도 차이 2당, 코인 위력 +1 (최대 2)\n- 자신의 속도가 1이면, 대신 코인 위력 +2\n[WhenUse] [LanternHohenheimBigBird] 4 얻음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000803].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [LanternHohenheimBigBird]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [LanternHohenheimBigBird] = 램프 / Lamp
   EN: If the target's Speed is faster than this unit's, Coin Power +1 for every 2 Speed difference (max 2)\n- At 1 Speed, Coin Power +2 instead\n[WhenUse] Gain 4 [LanternHohenheimBigBird]
   PL: [WhenUse] jeżeli Szybkość celu jest wyższa niż Szybkość tej jednostki, Moc Monety +1 za każde 2 różnicy Szybkości (maks. 2)\n- przy Szybkości 1 zamiast tego Moc Monety +2\n[WhenUse] zyskuje 4 [LanternHohenheimBigBird]
10. [Umiejętność sojusznika [40000803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]
   PL: [OnSucceedAttack] nakłada 3 [Combustion]
11. [Umiejętność sojusznika [40000803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Combustion] o 1
12. [Umiejętność sojusznika [40000803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5 부여. [Sinking] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking] and +1 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 5 [Sinking] i zwiększa Licznik [Sinking] o 1
13. [Umiejętność sojusznika [40000804] (ulepszenie 1) — nazwa] 등불에 현혹된 것에는 구원을
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000804].levelList[level=1].name
   limit: do 60 znaków
   EN: Salvation for those Enchanted by the Lamp
   PL: Salvation for those Enchanted by the Lamp
14. [Umiejętność sojusznika [40000804] (ulepszenie 1) — opis] 일방 공격 종료시까지 자신은 체력 피해를 입지 않고, 부정적인 효과가 부여되지 않음\n대상의 속도가 자신보다 높으면 속도 차이 1당, 코인 위력 +1 (최대 6)\n- 자신의 속도가 1이면, 대신 코인 위력 +6\n적에게 [DelusionHohenheimBigBird]이 있으면, 공격 종료 전까지 대상의 관통 내성 +0.5\n[EndSkill] 대상의 [DelusionHohenheimBigBird] 제거
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000804].levelList[level=1].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [DelusionHohenheimBigBird], [EndSkill]
   znaczenie tagów: [DelusionHohenheimBigBird] = 현혹 / Dazzle; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Until the end of the Unopposed Attack, this unit does not take HP damage and does not gain negative effects\nIf the target's Speed is faster than this unit's, Coin Power +1 for every 1 Speed difference (max 6)\n- At 1 Speed, Coin Power +6 instead\nIf target has [DelusionHohenheimBigBird], +0.5 to target's Pierce Resist. until Attack End\n[EndSkill] Remove [DelusionHohenheimBigBird] from target
   PL: do końca ataku bez oporu ta jednostka nie otrzymuje obrażeń HP i nie zyskuje negatywnych efektów\njeżeli Szybkość celu jest wyższa niż Szybkość tej jednostki, Moc Monety +1 za każde 1 różnicy Szybkości (maks. 6)\n- przy Szybkości 1 zamiast tego Moc Monety +6\njeżeli cel ma [DelusionHohenheimBigBird], do końca ataku Odporność celu na Kłucie +0.5\n[EndSkill] usuwa [DelusionHohenheimBigBird] z celu
15. [Umiejętność sojusznika [40000804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
16. [Umiejętność sojusznika [40000804] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnStartCoin] [LanternHohenheimBigBird]을 전부 소모하고, 소모한 수치 1당 피해량 +15% (최대 300%)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000804].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [LanternHohenheimBigBird]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [LanternHohenheimBigBird] = 램프 / Lamp
   EN: [OnStartCoin] Consume all [LanternHohenheimBigBird] Stack and deal +15% damage for every Stack consumed (max 300%)
   PL: [OnStartCoin] zużywa wszystkie Stosy [LanternHohenheimBigBird] i zadaje +15% obrażeń za każdy zużyty Stos (maks. 300%)
17. [Umiejętność sojusznika [40000804] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Sinking] 8 부여. [Sinking] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000804].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 8 [Sinking] and +2 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 8 [Sinking] i zwiększa Licznik [Sinking] o 2
18. [Umiejętność sojusznika [40000804] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Combustion] 6 부여. [Combustion] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000804].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 6 [Combustion] and +2 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 6 [Combustion] i zwiększa Licznik [Combustion] o 2
19. [Umiejętność sojusznika [40001201] (ulepszenie 1) — nazwa] 달구어 꿰뚫기
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001201].levelList[level=1].name
   limit: do 40 znaków
   EN: Heated Puncture
   PL: Heated Puncture
20. [Umiejętność sojusznika [40001201] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Laceration]의 합 6당, 코인 위력 + 1 (최대 2)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Laceration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: Coin Power +1 for every 6 ([Combustion] + [Laceration]) on target (max 2)
   PL: Moc Monety +1 za każde 6 ([Combustion] + [Laceration]) celu (maks. 2)
21. [Umiejętność sojusznika [40001201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL: [OnSucceedAttack] nakłada 1 [Combustion]
22. [Umiejętność sojusznika [40001201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +2 [Combustion] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Combustion] o 2
23. [Umiejętność sojusznika [40001201] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001201].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL: [OnSucceedAttack] nakłada 2 [Combustion]
24. [Umiejętność sojusznika [40001202] (ulepszenie 1) — nazwa] 작열절삭
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001202].levelList[level=1].name
   limit: do 40 znaków
   EN: Scorching Incision
   PL: Scorching Incision
25. [Umiejętność sojusznika [40001202] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Laceration]의 합 6당, 코인 위력 + 1 (최대 2)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001202].levelList[level=1].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
26. [Umiejętność sojusznika [40001202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
27. [Umiejętność sojusznika [40001202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
28. [Umiejętność sojusznika [40001202] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
29. [Umiejętność sojusznika [40001203] (ulepszenie 1) — nazwa] 흐름을 따라
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001203].levelList[level=1].name
   limit: do 40 znaków
   EN: Following the Flow
   PL: Following the Flow
30. [Umiejętność sojusznika [40001203] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Laceration]의 합 6당, 코인 위력 + 1 (최대 2)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001203].levelList[level=1].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
31. [Umiejętność sojusznika [40001203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
32. [Umiejętność sojusznika [40001203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable]
   PL: [OnSucceedAttack] nakłada 1 [Vulnerable]
33. [Umiejętność sojusznika [40001203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
34. [Umiejętność sojusznika [40001204] (ulepszenie 1) — nazwa] 길을 열도록 하지
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001204].levelList[level=1].name
   limit: do 40 znaków
   EN: I Shall Open the Path
   PL: I Shall Open the Path
35. [Umiejętność sojusznika [40001204] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Laceration]의 합 6당, 코인 위력 + 1 (최대 3)\n[WhenUse] 정신력이 0 이상이면, 망(望) 하나를 생성함\n- 코인 위력 + 1, 피해량 +30%\n[EndSkill] 망을 생성했으면, 정신력 1만큼 소모
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001204].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [WhenUse], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Coin Power +1 for every 6 ([Combustion] + [Laceration]) on target (max 3)\n[WhenUse] At 0+ SP, generate 1 Mang (望)\n- Coin Power +1 and deal +30% damage\n[EndSkill] If this Skill generated Mang, consume 1 SP
   PL: Moc Monety +1 za każde 6 ([Combustion] + [Laceration]) celu (maks. 3)\n[WhenUse] przy SP 0+ generuje 1 Mang (望)\n- Moc Monety +1, zadaje +30% obrażeń\n[EndSkill] jeżeli ta Umiejętność wygenerowała Mang, zużywa 1 SP
36. [Umiejętność sojusznika [40001204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
37. [Umiejętność sojusznika [40001204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +3 [Combustion] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Combustion] o 3
38. [Umiejętność sojusznika [40001204] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [SlashTakeDamageUp] 1 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001204].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttack] Inflict 1 [SlashTakeDamageUp]
   PL: [OnSucceedAttack] nakłada 1 [SlashTakeDamageUp]
39. [Umiejętność sojusznika [40001204] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001204].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
40. [Umiejętność sojusznika [40001205] (ulepszenie 1) — nazwa] 닥치도록
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001205].levelList[level=1].name
   limit: do 40 znaków
   EN: Silence
   PL: Silence
41. [Umiejętność sojusznika [40001205] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Laceration]의 합 6당, 코인 위력 + 1 (최대 4)\n[WhenUse] 정신력이 0 이상이면, 망(望) 두개를 생성함\n- 코인 위력 + 2, 피해량 +60%\n[EndSkill] 망을 생성했으면, 정신력 3만큼 소모
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001205].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [WhenUse], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Coin Power +1 for every 6 ([Combustion] + [Laceration]) on target (max 4)\n[WhenUse] At 0+ SP, generate 2 Mang (望)\n- Coin Power +2 and deal +60% damage\n[EndSkill] If this Skill generated Mang, consume 3 SP
   PL: Moc Monety +1 za każde 6 ([Combustion] + [Laceration]) celu (maks. 4)\n[WhenUse] przy SP 0+ generuje 2 Mang (望)\n- Moc Monety +2, zadaje +60% obrażeń\n[EndSkill] jeżeli ta Umiejętność wygenerowała Mang, zużywa 3 SP
42. [Umiejętność sojusznika [40001205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Umiejętność sojusznika [40001205] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001205].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Umiejętność sojusznika [40001205] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001205].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Umiejętność sojusznika [40001205] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001205].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
46. [Umiejętność sojusznika [40001206] (ulepszenie 1) — nazwa] 내출혈
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001206].levelList[level=1].name
   limit: do 40 znaków
   EN: Internal Bleeding
   PL: Internal Bleeding
47. [Umiejętność sojusznika [40001206] (ulepszenie 1) — opis] 대상과 자신의 [Laceration]의 합 1당 피해량 + 1% (최대 20%)\n[WhenUse] [Laceration] 3 얻음, 자신의 [Laceration] 횟수 5 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001206].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: Deal +1% damage for every ([Laceration] on self + [Laceration] on target) (max 20%)\n[WhenUse] Gain 3 [Laceration] and +5 [Laceration] Count
   PL: zadaje +1% obrażeń za każde 1 ([Laceration] tej jednostki + [Laceration] celu) (maks. 20%)\n[WhenUse] zyskuje 3 [Laceration] i 5 Licznika [Laceration]
48. [Umiejętność sojusznika [40001206] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [Umiejętność sojusznika [40001206] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001206].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] nakłada 3 [Laceration]
50. [Umiejętność sojusznika [40001206] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001206].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Umiejętność sojusznika [40001206] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001206].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Laceration] o 3
52. [Umiejętność sojusznika [40001206] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001206].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [Umiejętność sojusznika [40001206] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001206].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
54. [Umiejętność sojusznika [40001207] (ulepszenie 1) — nazwa] 망혈참
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001207].levelList[level=1].name
   limit: do 40 znaków
   EN: Blinding Bloodcleaver
   PL: Blinding Bloodcleaver
55. [Umiejętność sojusznika [40001207] (ulepszenie 1) — opis] 대상과 자신의 [Laceration]의 합 1당 피해량 + 1% (최대 20%)\n[WhenUse] [Laceration] 3 얻음, 자신의 [Laceration] 횟수 5 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001207].levelList[level=1].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Umiejętność sojusznika [40001207] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001207].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Umiejętność sojusznika [40001207] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001207].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [Umiejętność sojusznika [40001207] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001207].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] nakłada 4 [Laceration]
59. [Umiejętność sojusznika [40001207] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001207].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [Umiejętność sojusznika [40001207] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001207].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Umiejętność sojusznika [40001208] (ulepszenie 1) — nazwa] 피에 잠겨 익사하도록
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001208].levelList[level=1].name
   limit: do 40 znaków
   EN: Drown in Blood
   PL: Drown in Blood
62. [Umiejętność sojusznika [40001208] (ulepszenie 1) — opis] 대상과 자신의 [Laceration]의 합 1당 피해량 + 1% (최대 30%)\n[WhenUse] [Laceration] 6 얻음, 자신의 [Laceration] 횟수 5 증가\n[WhenUse] 정신력이 0 이상이면, 망(望) 두개를 생성함\n- 코인 위력 + 2, 피해량 +60%\n[EndSkill] 망을 생성했으면, 정신력 5만큼 소모
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001208].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +1% damage for every ([Laceration] on self + [Laceration] on target) (max 30%)\n[WhenUse] Gain 6 [Laceration] and +5 [Laceration] Count\n[WhenUse] At 0+ SP, generate 2 Mang (望)\n- Coin Power +2 and deal +60% damage\n[EndSkill] If this Skill generated Mang, consume 5 SP
   PL: zadaje +1% obrażeń za każde 1 ([Laceration] tej jednostki + [Laceration] celu) (maks. 30%)\n[WhenUse] zyskuje 6 [Laceration] i 5 Licznika [Laceration]\n[WhenUse] przy SP 0+ generuje 2 Mang (望)\n- Moc Monety +2, zadaje +60% obrażeń\n[EndSkill] jeżeli ta Umiejętność wygenerowała Mang, zużywa 5 SP
63. [Umiejętność sojusznika [40001208] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001208].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [Umiejętność sojusznika [40001208] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001208].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
65. [Umiejętność sojusznika [40001208] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001208].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Umiejętność sojusznika [40001208] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 4 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001208].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +4 [Laceration] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Laceration] o 4
67. [Umiejętność sojusznika [40001208] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상과 자신의 [Laceration]의 합 5당, [BloodBranch] 1 부여 (최대3)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001208].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [BloodBranch]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [BloodBranch] = 망혈[盲血] / Blinding Blood [盲血]
   EN: [OnSucceedAttack] Inflict 1 [BloodBranch] for every 5 ([Laceration] on self + [Laceration] on target) (max 3)
   PL: [OnSucceedAttack] nakłada 1 [BloodBranch] za każde 5 ([Laceration] tej jednostki + [Laceration] celu) (maks. 3)
68. [Umiejętność sojusznika [40001208] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001208].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [Umiejętność sojusznika [40001208] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001208].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Umiejętność sojusznika [40001209] (ulepszenie 1) — nazwa] 죽은 혈귀를 위한 장례
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001209].levelList[level=1].name
   limit: do 50 znaków
   EN: Funeral for a Dead Bloodfiend
   PL: Funeral for a Dead Bloodfiend
71. [Umiejętność sojusznika [40001209] (ulepszenie 1) — opis] 대상과 자신의 [Laceration]의 합 1당 피해량 + 1% (최대 50%)\n[WhenUse] [Laceration] 10 얻음, 자신의 [Laceration] 횟수 5 증가\n[WhenUse] 정신력이 0 이상이면, 망(望) 세개를 생성함\n- 코인 위력 + 3, 피해량 +90%\n[EndSkill] 망을 생성했으면, 정신력 3만큼 소모
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001209].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +1% damage for every ([Laceration] on self + [Laceration] on target) (max 50%)\n[WhenUse] Gain 10 [Laceration] and +5 [Laceration] Count\n[WhenUse] At 0+ SP, generate 3 Mang (望)\n- Coin Power +3 and deal +90% damage\n[EndSkill] If this Skill generated Mang, consume 3 SP
   PL: zadaje +1% obrażeń za każde 1 ([Laceration] tej jednostki + [Laceration] celu) (maks. 50%)\n[WhenUse] zyskuje 10 [Laceration] i 5 Licznika [Laceration]\n[WhenUse] przy SP 0+ generuje 3 Mang (望)\n- Moc Monety +3, zadaje +90% obrażeń\n[EndSkill] jeżeli ta Umiejętność wygenerowała Mang, zużywa 3 SP
72. [Umiejętność sojusznika [40001209] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001209].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [Umiejętność sojusznika [40001209] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001209].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Umiejętność sojusznika [40001209] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001209].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL: [OnSucceedAttack] nakłada 5 [Laceration]
75. [Umiejętność sojusznika [40001209] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상과 자신의 [Laceration]의 합 5당, [BloodBranch] 1 부여 (최대5)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001209].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [BloodBranch]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [BloodBranch] = 망혈[盲血] / Blinding Blood [盲血]
   EN: [OnSucceedAttack] Inflict 1 [BloodBranch] for every 5 ([Laceration] on self + [Laceration] on target) (max 5)
   PL: [OnSucceedAttack] nakłada 1 [BloodBranch] za każde 5 ([Laceration] tej jednostki + [Laceration] celu) (maks. 5)
76. [Umiejętność sojusznika [40001209] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001209].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [Umiejętność sojusznika [40001209] (ulepszenie 1) — moneta 5, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001209].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [Umiejętność sojusznika [40001301] (ulepszenie 1) — nazwa] 내려베기
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001301].levelList[level=1].name
   limit: do 40 znaków
   EN: Downward Swing
   PL: Downward Swing
79. [Umiejętność sojusznika [40001301] (ulepszenie 1) — opis] [WhenUse] 자신의 속도가 6 이상이면, 피해량 +20%\n[WhenUse] [Breath] 4 얻음. [Breath] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] At 6+ Speed, deal +20% damage\n[WhenUse] Gain 4 [Breath] and +2 [Breath] Count
   PL: [WhenUse] przy Szybkości 6+ zadaje +20% obrażeń\n[WhenUse] zyskuje 4 [Breath] i 2 Licznika [Breath]
80. [Umiejętność sojusznika [40001301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Burst] o 1
81. [Umiejętność sojusznika [40001301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 8 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 8 [Burst]
   PL: [OnSucceedAttack] nakłada 8 [Burst]
82. [Umiejętność sojusznika [40001301] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001301].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność sojusznika [40001302] (ulepszenie 1) — nazwa] 연속 베기
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001302].levelList[level=1].name
   limit: do 40 znaków
   EN: Halberd Combo
   PL: Halberd Combo
84. [Umiejętność sojusznika [40001302] (ulepszenie 1) — opis] [WhenUse] 자신의 속도가 6 이상이면, 피해량 +30%\n[WhenUse] [Breath] 1 얻음. [Breath] 횟수 3 증가\n[WinDuel] 피해량 +30%
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001302].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] At 6+ Speed, deal +30% damage\n[WhenUse] Gain 1 [Breath] and +3 [Breath] Count\n[WinDuel] Deal +30% damage
   PL: [WhenUse] przy Szybkości 6+ zadaje +30% obrażeń\n[WhenUse] zyskuje 1 [Breath] i 3 Licznika [Breath]\n[WinDuel] zadaje +30% obrażeń
85. [Umiejętność sojusznika [40001302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Burst] o 2
86. [Umiejętność sojusznika [40001302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]
   PL: [OnSucceedAttack] nakłada 5 [Burst]
87. [Umiejętność sojusznika [40001302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]
   PL: [OnSucceedAttack] nakłada 6 [Laceration]
88. [Umiejętność sojusznika [40001303] (ulepszenie 1) — nazwa] 참호전 특화 교전창술
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001303].levelList[level=1].name
   limit: do 50 znaków
   EN: Trench-specialized Spear Combat
   PL: Trench-specialized Spear Combat
89. [Umiejętność sojusznika [40001303] (ulepszenie 1) — opis] [WhenUse] 자신의 속도가 7 이상이면, 피해량 +40%\n[WhenUse] [Breath] 횟수 4 증가\n[WinDuel] [Enhancement] 1 얻음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001303].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel], [Enhancement]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [WhenUse] At 7+ Speed, deal +40% damage\n[WhenUse] Gain +4 [Breath] Count\n[WinDuel] Gain 1 [Enhancement]
   PL: [WhenUse] przy Szybkości 7+ zadaje +40% obrażeń\n[WhenUse] zyskuje 4 Licznika [Breath]\n[WinDuel] zyskuje 1 [Enhancement]
90. [Umiejętność sojusznika [40001303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 6 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 6 [Burst]
   PL: [OnSucceedAttack] nakłada 6 [Burst]
91. [Umiejętność sojusznika [40001303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Umiejętność sojusznika [40001303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Laceration] o 2
93. [Umiejętność sojusznika [40001304] (ulepszenie 1) — nazwa] 진진종참
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001304].levelList[level=1].name
   limit: do 40 znaków
   EN: True Decapitation Deathblow
   PL: True Decapitation Deathblow
94. [Umiejętność sojusznika [40001304] (ulepszenie 1) — opis] 자신에게 [WillAwakenSinclair]가 있으면, 공격 종료 전까지 공격 대상의 참격 내성 +1\n[WhenUse] [Breath] 5당, 기본 위력 +2 (최대 8)\n[WhenUse] 자신의 정신력이 5 이상이면 망을 1개 생성. 기본 위력 +3\n[EndSkill] 이 스킬에서 망을 생성했으면, 정신력 -5
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001304].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WillAwakenSinclair], [WhenUse], [Breath], [EndSkill]
   znaczenie tagów: [WillAwakenSinclair] = 신(心) - 어느 싱클레어 / Shin (心) - A Certain Sinclair; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If this unit has [WillAwakenSinclair], +1 to target's Slash Resist. until Attack End\n[WhenUse] Base Power +2 for every 5 [Breath] (max 8)\n[WhenUse] At 5+ SP, generate 1 Mang; Base Power +3\n[EndSkill] If this Skill generated Mang, lose 5 SP
   PL: jeżeli ta jednostka ma [WillAwakenSinclair], do końca ataku Odporność celu na Cięcie +1\n[WhenUse] Moc Bazowa +2 za każde 5 [Breath] (maks. 8)\n[WhenUse] przy SP 5+ generuje 1 Mang; Moc Bazowa +3\n[EndSkill] jeżeli ta Umiejętność wygenerowała Mang, traci 5 SP
95. [Umiejętność sojusznika [40001304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [ExtractCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ExtractCoin]
   znaczenie tagów: [ExtractCoin] = 적출 코인 / Excision Coin
   EN: [ExtractCoin]
   PL: [ExtractCoin]
96. [Umiejętność sojusznika [40001304] (ulepszenie 1) — moneta 1, efekt 2 — opis] ([Burst] + [Burst] 횟수) 1당 피해량 +1% (최대 100%)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Deal +1% damage for every ([Burst] + [Burst] Count) on the target (max 100%)
   PL: zadaje +1% obrażeń za każde 1 ([Burst] + Licznik [Burst]) celu (maks. 100%)
97. [Umiejętność sojusznika [40001304] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 ([Breath] x 4)만큼 오만 피해를 줌 (최대 80)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001304].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Deal ([Breath] on self x 4) Pride damage (max 80)
   PL: [OnSucceedAttack] zadaje obrażenia Pychy równe (Siła [Breath] tej jednostki x 4) (maks. 80)
98. [Umiejętność sojusznika [40001304] (ulepszenie 1) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] 피해량 +150%
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001304].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Deal +150% damage
   PL: [CriticalOnSucceedAttack] zadaje +150% obrażeń
99. [Umiejętność sojusznika [40001305] (ulepszenie 1) — nazwa] 취수낭랑
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001305].levelList[level=1].name
   limit: do 60 znaków
   EN: Plastered Sleep, Unrestrained Ripples
   PL: Plastered Sleep, Unrestrained Ripples
100. [Umiejętność sojusznika [40001305] (ulepszenie 1) — opis] 자신에게 [WillAwakenSinclair]가 있으면, 공격 종료 전까지 공격 대상의 참격 내성 +1\n속도에 관계없이 공격 대상을 자신으로 변경할 수 있음\n[WhenUse] [Breath] 3당, 기본 위력 +1 (최대 2)\n[WhenUse] 대상의 부정적인 효과 1개당, 기본 위력 +2 (최대 4)\n[WhenUse] 다음 턴에 [Agility] 5 얻음\n[WhenUse] [Breath] 10 얻음. [Breath] 횟수 2 증가\n[WhenUse] 자신의 정신력이 10 이상이면 망을 2개 생성. 기본 위력 +6\n[EndSkill] 이 스킬에서 망을 생성했으면, 정신력 -10
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001305].levelList[level=1].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n, [WillAwakenSinclair], [WhenUse], [Breath], [Agility], [EndSkill]
   znaczenie tagów: [WillAwakenSinclair] = 신(心) - 어느 싱클레어 / Shin (心) - A Certain Sinclair; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If this unit has [WillAwakenSinclair], +1 to target's Slash Resist. until Attack End\nCan draw any attack to this unit regardless of Speed\n[WhenUse] Base Power +1 for every 3 [Breath] (max 2)\n[WhenUse] Base Power +2 for every type of negative effect on target (max 4)\n[WhenUse] Gain 5 [Agility] next turn\n[WhenUse] Gain 10 [Breath] and +2 [Breath] Count\n[WhenUse] At 10+ SP, generate 2 Mang; Base Power +6\n[EndSkill] If this Skill generated Mang, lose 10 SP
   PL: jeżeli ta jednostka ma [WillAwakenSinclair], do końca ataku Odporność celu na Cięcie +1\nmoże przyciągnąć dowolny atak na siebie niezależnie od Szybkości\n[WhenUse] Moc Bazowa +1 za każde 3 [Breath] (maks. 2)\n[WhenUse] Moc Bazowa +2 za każdy rodzaj negatywnego efektu celu (maks. 4)\n[WhenUse] zyskuje 5 [Agility] w następnej turze\n[WhenUse] zyskuje 10 [Breath] i 2 Licznika [Breath]\n[WhenUse] przy SP 10+ generuje 2 Mang; Moc Bazowa +6\n[EndSkill] jeżeli ta Umiejętność wygenerowała Mang, traci 10 SP
101. [Umiejętność sojusznika [40001305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [ExtractCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [Umiejętność sojusznika [40001305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 7 부여. [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 7 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 7 [Laceration] i zwiększa Licznik [Laceration] o 2
103. [Umiejętność sojusznika [40001305] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001305].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 2 [Vulnerable] w następnej turze
104. [Umiejętność sojusznika [40001305] (ulepszenie 1) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] 피해량 +400%
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001305].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Deal +400% damage
   PL: [CriticalOnSucceedAttack] zadaje +400% obrażeń
105. [Umiejętność sojusznika [40001306] (ulepszenie 1) — nazwa] 연기 거두기
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001306].levelList[level=1].name
   limit: do 40 znaków
   EN: Abate the Smoke
   PL: Abate the Smoke
106. [Umiejętność sojusznika [40001306] (ulepszenie 1) — opis] [CantDuel]\n최대 체력이 가장 낮은 적을 우선 지정함\n이 스킬은 수비 스킬을 발동시키지 않음\n[BeforeAttack] 적들의 슬롯 수 합만큼 공격 가중치 증가\n[WhenUse] 자신의 속도가 4 이상이면, 피해량 +50%
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001306].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [BeforeAttack], [WhenUse]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]
   EN: [CantDuel]\nTargets the enemy with the lowest max HP\nThis Skill does not trigger the target's Defense Skill\n[BeforeAttack] Gain +(total number of all enemies' Slots) Atk Weight\n[WhenUse] At 4+ Speed, deal +50% damage
   PL: [CantDuel]\nceluje we wroga z najniższym Maks. HP\nta Umiejętność nie uruchamia Umiejętności obrony celu\n[BeforeAttack] zwiększa Wagę Ataku o łączną liczbę slotów wszystkich wrogów\n[WhenUse] przy Szybkości 4+ zadaje +50% obrażeń
107. [Umiejętność sojusznika [40001306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 이 코인 최종 피해량의 40%만큼 참격 피해
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Deal (40% of this Coin's final damage) Slash damage
   PL: [OnSucceedAttackHead] zadaje obrażenia Sieczne równe 40% końcowych obrażeń tej Monety
108. [Umiejętność sojusznika [40001501] (ulepszenie 1) — nazwa] 베기
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001501].levelList[level=1].name
   limit: do 40 znaków
   EN: Sever
   PL: Sever
109. [Umiejętność sojusznika [40001501] (ulepszenie 1) — opis] 대상 변경 불가능\n자신의 [CutbondRyoshu] 10당, 최종 위력 +1 (최대 3)\n대상의 [Laceration] 6당 최종 위력 +1 (최대 3)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001501].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CutbondRyoshu], [Laceration]
   znaczenie tagów: [CutbondRyoshu] = 무아 [無我] / Muga [無我]; [Laceration] = 출혈 / Bleed
   EN: Cannot change target\nFinal Power +1 for every 10 [CutbondRyoshu] on self (max 3)\nFinal Power +1 for every 6 [Laceration] on target (max 3)
   PL: nie można zmienić celu\nMoc Końcowa +1 za każde 10 [CutbondRyoshu] tej jednostki (maks. 3)\nMoc Końcowa +1 za każde 6 [Laceration] celu (maks. 3)
110. [Umiejętność sojusznika [40001501] (ulepszenie 1) — tekst klimatyczny] ‘아라야는 나와 다른 곳에서 살아야 한다.’
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001501].levelList[level=1].flavor
   limit: do 140 znaków
   EN: 'I cannot let Araya live a life like my own. She must lead a new life away from this place, away from me.'
   PL: ‘Araya nie może żyć tak jak ja — musi prowadzić nowe życie gdzie indziej, z dala od tego miejsca i z dala ode mnie.’
111. [Umiejętność sojusznika [40001501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [Umiejętność sojusznika [40001501] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 1 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001501].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Laceration] and +2 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Laceration] i zwiększa Licznik [Laceration] o 2
113. [Umiejętność sojusznika [40001501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Umiejętność sojusznika [40001501] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001501].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration] and +1 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Laceration] i zwiększa Licznik [Laceration] o 1
115. [Umiejętność sojusznika [40001502] (ulepszenie 1) — nazwa] 칠하기
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001502].levelList[level=1].name
   limit: do 40 znaków
   EN: Paint
   PL: Paint
116. [Umiejętność sojusznika [40001502] (ulepszenie 1) — opis] 대상 변경 불가능\n자신의 [CutbondRyoshu] 10당, 최종 위력 +1 (최대 3)\n대상의 [Laceration] 6당 최종 위력 +1 (최대 3)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001502].levelList[level=1].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Umiejętność sojusznika [40001502] (ulepszenie 1) — tekst klimatyczny] ‘거미집을 탈출한다.’\n\n‘아라야가 사루처럼 되기 전에.’
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001502].levelList[level=1].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'We will escape the House of Spiders...'\n\n'Before Araya meets the same fate as Saru.'
   PL: ‘Wydostaniemy się z Domu Pajęczyn...’\n\n‘Zanim Araya spotka los Saru.’
118. [Umiejętność sojusznika [40001502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Umiejętność sojusznika [40001502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Laceration] and +1 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Laceration] i zwiększa Licznik [Laceration] o 1
120. [Umiejętność sojusznika [40001502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Umiejętność sojusznika [40001502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Laceration] and +2 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Laceration] i zwiększa Licznik [Laceration] o 2
122. [Umiejętność sojusznika [40001503] (ulepszenie 1) — nazwa] 흩뿌리기
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001503].levelList[level=1].name
   limit: do 40 znaków
   EN: Splatter
   PL: Splatter
123. [Umiejętność sojusznika [40001503] (ulepszenie 1) — opis] 대상 변경 불가능\n이 스킬과 합을 진행한 스킬의 가장 빠른 코인이 일정 확률로 소멸\n자신의 [CutbondRyoshu] 10당 최종 위력 +1 (최대 5)\n대상의 [Laceration] 6당 최종 위력 +1 (최대 4)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001503].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [CutbondRyoshu], [Laceration]
   znaczenie tagów: [CutbondRyoshu] = 무아 [無我] / Muga [無我]; [Laceration] = 출혈 / Bleed
   EN: Cannot change target\nRandom chance to delete the earliest Coin on the Skill this unit Clashed with\nFinal Power +1 for every 10 [CutbondRyoshu] on self (max 5)\nFinal Power +1 for every 6 [Laceration] on target (max 4)
   PL: nie można zmienić celu\nz pewnym prawdopodobieństwem niszczy najwcześniejszą Monetę Umiejętności, z którą ta jednostka weszła w Starcie\nMoc Końcowa +1 za każde 10 [CutbondRyoshu] tej jednostki (maks. 5)\nMoc Końcowa +1 za każde 6 [Laceration] celu (maks. 4)
124. [Umiejętność sojusznika [40001503] (ulepszenie 1) — tekst klimatyczny] ‘아비들을 전부 베어내며, 아라야까지 지킬 수는 없다.’
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001503].levelList[level=1].flavor
   limit: do 120 znaków
   EN: 'But I cannot guarantee Araya's safety while fighting off the Nursefathers' pursuit.'
   PL: ‘Odpierając pościg Ojców, nie mogę zagwarantować bezpieczeństwa Arayi.’
125. [Umiejętność sojusznika [40001503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Umiejętność sojusznika [40001503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 1 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Laceration] and +1 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Laceration] i zwiększa Licznik [Laceration] o 1
127. [Umiejętność sojusznika [40001503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Umiejętność sojusznika [40001503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Umiejętność sojusznika [40001503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Umiejętność sojusznika [40001503] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001503].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Laceration] and +3 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Laceration] i zwiększa Licznik [Laceration] o 3
131. [Umiejętność sojusznika [40001504] (ulepszenie 1) — nazwa] 그려내기
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001504].levelList[level=1].name
   limit: do 40 znaków
   EN: Brushstroke
   PL: Brushstroke
132. [Umiejętność sojusznika [40001504] (ulepszenie 1) — opis] 대상 변경 불가능\n이 스킬과 합을 진행한 스킬의 가장 빠른 코인이 일정 확률로 소멸\n자신의 [CutbondRyoshu] 10당 최종 위력 +1 (최대 5)\n대상의 [Laceration] 6당 최종 위력 +1 (최대 4)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001504].levelList[level=1].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Umiejętność sojusznika [40001504] (ulepszenie 1) — tekst klimatyczny] ‘아라야를 숨긴다. 아비들이 자주 드나드는 시간 금고들이 쌓여 있는 방이 있다.’\n\n‘그 방에 있는 금고에 아라야를 대피시킨다. 시간 금고라면 안전하다.’
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001504].levelList[level=1].flavor
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'I will hide her. I will hide her right under their noses—in that room full of Time Vaults where they're always coming and going.'\n\n'Time Vaults are safe. I can put Araya in one of those.'
   PL: ‘Ukryję ją. Tuż pod ich nosem — w pokoju pełnym Skarbców Czasu, do których nieustannie zaglądają.’\n\n‘Skarbce Czasu są bezpieczne. Umieszczę Arayę w jednym z nich.’
134. [Umiejętność sojusznika [40001504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Umiejętność sojusznika [40001504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Umiejętność sojusznika [40001504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Umiejętność sojusznika [40001504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 1 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Umiejętność sojusznika [40001504] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001504].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Umiejętność sojusznika [40001504] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001504].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Umiejętność sojusznika [40001505] (ulepszenie 1) — nazwa] 천살 [天殺]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001505].levelList[level=1].name
   limit: do 50 znaków
   EN: Slay the Heavens - Tiansha [天殺]
   PL: Slay the Heavens - Tiansha [天殺]
141. [Umiejętność sojusznika [40001505] (ulepszenie 1) — opis] 대상 변경 불가능\n이 스킬과 합을 진행한 스킬의 가장 빠른 코인이 일정 확률로 소멸\n자신의 [CutbondRyoshu] 4당, 최종 위력 +1 (최대 12)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001505].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [CutbondRyoshu]
   znaczenie tagów: [CutbondRyoshu] = 무아 [無我] / Muga [無我]
   EN: Cannot change target\nRandom chance to delete the earliest Coin on the Skill this unit Clashed with\nFinal Power +1 for every 4 [CutbondRyoshu] on self (max 12)
   PL: nie można zmienić celu\nz pewnym prawdopodobieństwem niszczy najwcześniejszą Monetę Umiejętności, z którą ta jednostka weszła w Starcie\nMoc Końcowa +1 za każde 4 [CutbondRyoshu] tej jednostki (maks. 12)
142. [Umiejętność sojusznika [40001505] (ulepszenie 1) — tekst klimatyczny] ‘그리고 금고에 내 검으로 검흔을 새겨 놓는다.’\n\n‘내가 다시 돌아왔을 때, 그 검흔이 드러나면 금고가 섞여도 알아낼 수 있을 것이다.’\n\n‘나무를 숨기려면 숲에 숨겨야 한다.’
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001505].levelList[level=1].flavor
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'And then, I will make a small mark on Araya's safe with my blade.'\n\n'That way, when I return, the mark made by my sword will become fresh again and I'll be able to pick out hers even if the Vaults get shuffled around.'\n\n'The best place to hide a tree is in the forest.'
   PL: ‘A potem wygraweruję na jej skarbcu ślad własnym ostrzem.’\n\n‘Gdy do niego wrócę, odnów ten ślad — rozpoznam jej skarbiec nawet po przetasowaniu Skarbców Czasu.’\n\n‘Drzewo najlepiej ukryć w lesie.’
143. [Umiejętność sojusznika [40001505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Umiejętność sojusznika [40001505] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001505].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Umiejętność sojusznika [40001505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Umiejętność sojusznika [40001505] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001505].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Umiejętność sojusznika [40001505] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001505].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Umiejętność sojusznika [40001505] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001505].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] nakłada 2 [Laceration]
149. [Umiejętność sojusznika [40001505] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001505].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Umiejętność sojusznika [40001505] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001505].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Umiejętność sojusznika [40001505] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001505].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Umiejętność sojusznika [40001505] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001505].levelList[level=1].coinlist[#4].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 [Laceration] i zwiększa Licznik [Laceration] o 2
153. [Umiejętność sojusznika [40001506] (ulepszenie 1) — nazwa] ‘나를 지우며, 너를 지운다.’
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001506].levelList[level=1].name
   limit: do 40 znaków
   EN: 'Erasing Me, Erasing You.'
   PL: 'Erasing Me, Erasing You.'
154. [Umiejętność sojusznika [40001506] (ulepszenie 1) — opis] 대상 변경 불가능\n이 스킬과 합을 진행한 스킬의 가장 빠른 코인이 일정 확률로 소멸
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001506].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cannot change target\nRandom chance to delete the earliest Coin on the Skill this unit Clashed with
   PL: nie można zmienić celu\nz pewnym prawdopodobieństwem niszczy najwcześniejszą Monetę Umiejętności, z którą starła się ta jednostka
155. [Umiejętność sojusznika [40001506] (ulepszenie 1) — tekst klimatyczny] ‘오랜 시간이 걸려도, 아라야에게는 찰나 같을 수 있기를.’
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001506].levelList[level=1].flavor
   limit: do 120 znaków
   EN: 'However much time slips by, I hope it feels like only a fleeting moment to her.'
   PL: ‘Nawet gdyby czas płynął wiecznie, niech dla niej będzie to tylko mgnienie oka.’
156. [Umiejętność sojusznika [40001506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Umiejętność sojusznika [40001506] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001506].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [Umiejętność sojusznika [40001506] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001506].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Umiejętność sojusznika [40001506] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001506].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Umiejętność sojusznika [40001506] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001506].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Umiejętności jednostek wsparcia — Skills_Assist-exme
- plik gry: `Skills_Assist-exme.json`

161. [Umiejętność sojusznika [40003801] (ulepszenie 1) — nazwa] 세법
   źródło: Skills_Assist-exme.json :: dataList[id=40003801].levelList[level=1].name
   limit: do 40 znaków
   EN: Rending Arts
   PL: Rending Arts
162. [Umiejętność sojusznika [40003801] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Agility]이 3 이상이면, 기본 위력 +2\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Assist-exme.json :: dataList[id=40003801].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [Agility] = 신속 / Haste
   EN: [WhenUse] Coin Power +1 for every 6 ([Breath] on self + [Laceration] on target) (max 2)\n[WhenUse] At 3+ [Agility], Base Power +2\n[WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Moc Monety +1 za każde 6 ([Breath] tej jednostki + [Laceration] celu) (maks. 2)\n[WhenUse] przy 3+ [Agility] Moc Bazowa +2\n[WhenUse] zyskuje 2 Licznika [Breath]
163. [Umiejętność sojusznika [40003801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40003801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL: [OnSucceedAttack] zyskuje 3 [Breath]
164. [Umiejętność sojusznika [40003801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40003801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Umiejętność sojusznika [40003802] (ulepszenie 1) — nazwa] 자법
   źródło: Skills_Assist-exme.json :: dataList[id=40003802].levelList[level=1].name
   limit: do 40 znaków
   EN: Acupuncture
   PL: Acupuncture
166. [Umiejętność sojusznika [40003802] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Agility]이 3 이상이면, 기본 위력 +2\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Assist-exme.json :: dataList[id=40003802].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration], [Agility], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [Agility] = 신속 / Haste; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Coin Power +1 for every 6 ([Breath] on self + [Laceration] on target) (max 2)\n[WhenUse] At 3+ [Agility], Base Power +2\n[WhenUse] Gain +2 [Breath] Count\n[WinDuel] Gain +2 [Breath] Count
   PL: [WhenUse] Moc Monety +1 za każde 6 ([Breath] tej jednostki + [Laceration] celu) (maks. 2)\n[WhenUse] przy 3+ [Agility] Moc Bazowa +2\n[WhenUse] zyskuje 2 Licznika [Breath]\n[WinDuel] zyskuje 2 Licznika [Breath]
167. [Umiejętność sojusznika [40003802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40003802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL: [OnSucceedAttack] zyskuje 2 [Breath]
168. [Umiejętność sojusznika [40003802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40003802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] nakłada 1 [Laceration]
169. [Umiejętność sojusznika [40003802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40003802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Umiejętność sojusznika [40003802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40003802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Umiejętność sojusznika [40003802] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40003802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Umiejętność sojusznika [40003802] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-exme.json :: dataList[id=40003802].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Umiejętność sojusznika [40003802] (ulepszenie 1) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] 다음 턴에 [Agility] 2 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40003802].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Agility]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Agility] = 신속 / Haste
   EN: [CriticalOnSucceedAttack] Gain 2 [Agility] next turn
   PL: [CriticalOnSucceedAttack] zyskuje 2 [Agility] w następnej turze
174. [Umiejętność sojusznika [40003803] (ulepszenie 1) — nazwa] 청린화
   źródło: Skills_Assist-exme.json :: dataList[id=40003803].levelList[level=1].name
   limit: do 40 znaków
   EN: Lucent Rippling Flame
   PL: Lucent Rippling Flame
175. [Umiejętność sojusznika [40003803] (ulepszenie 1) — opis] 자신의 잃은 체력 1%당 피해량 0.5% 증가 (최대 25%)\n자신의 [Agility] 1당, 크리티컬 피해량 +25% (최대 150%)\n[WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합이 6 이상이면, 코인 위력 +1 (최대 2)\n[WhenUse] [WindBlade] 수치가 5 이상이면, [SuperCoin]으로 변경됨\n[WinDuel] [Breath] 5 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40003803].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [WhenUse], [Breath], [Laceration], [WindBlade], [SuperCoin], [WinDuel]
   znaczenie tagów: [Agility] = 신속 / Haste; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [WindBlade] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Deal +0.5% damage for every 1% missing HP on self (max 25%)\nDeal +25% damage on Critical Hit for every [Agility] on self (max 150%)\n[WhenUse] At 6+ ([Breath] on self + [Laceration] on target), Coin Power +1 (max 2)\n[WhenUse] At 5+ [WindBlade], convert into [SuperCoin]\n[WinDuel] Gain 5 [Breath]
   PL: zadaje +0.5% obrażeń za każde 1% utraconego HP tej jednostki (maks. 25%)\nzadaje +25% obrażeń krytycznych za każde 1 [Agility] tej jednostki (maks. 150%)\n[WhenUse] przy 6+ ([Breath] tej jednostki + [Laceration] celu) Moc Monety +1 (maks. 2)\n[WhenUse] przy 5+ wartości [WindBlade] zamienia się w [SuperCoin]\n[WinDuel] zyskuje 5 [Breath]
176. [Umiejętność sojusznika [40003803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Assist-exme.json :: dataList[id=40003803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +3 [Breath] Count
   PL: [OnSucceedAttack] zyskuje 3 Licznika [Breath]
177. [Umiejętność sojusznika [40003803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [WindBlade] 1 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40003803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [WindBlade]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [WindBlade] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: [CriticalOnSucceedAttack] Gain 1 [WindBlade]
   PL: [CriticalOnSucceedAttack] zyskuje 1 [WindBlade]
178. [Umiejętność sojusznika [40003803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40003803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Umiejętność sojusznika [40003803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [WindBlade] 1 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40003803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Umiejętność sojusznika [40003803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40003803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Umiejętność sojusznika [40003803] (ulepszenie 1) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] [WindBlade] 1 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40003803].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Umiejętność sojusznika [40003804] (ulepszenie 1) — nazwa] 상전 청린화
   źródło: Skills_Assist-exme.json :: dataList[id=40003804].levelList[level=1].name
   limit: do 60 znaków
   EN: Even the Balance - Lucent Rippling Flame
   PL: Even the Balance - Lucent Rippling Flame
183. [Umiejętność sojusznika [40003804] (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않음\n자신의 잃은 체력 1%당 피해량 0.5% 증가 (최대 25%)\n자신의 [Agility] 1당, 크리티컬 피해량 +20% (최대 100%)\n[EndSkill] [WindBlade] 모두 소모
   źródło: Skills_Assist-exme.json :: dataList[id=40003804].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [Agility], [EndSkill], [WindBlade]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [Agility] = 신속 / Haste; [EndSkill] = [공격 종료시] / [Attack End]; [WindBlade] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills\nDeal +0.5% damage for every 1% missing HP on self (max 25%)\nDeal +20% damage on Critical Hit for every [Agility] on self (max 100%)\n[EndSkill] Consume all [WindBlade] on self
   PL: [CantDuel]\nta Umiejętność nie uruchamia Umiejętności obrony celu\nzadaje +0.5% obrażeń za każde 1% utraconego HP tej jednostki (maks. 25%)\nzadaje +20% obrażeń krytycznych za każde 1 [Agility] tej jednostki (maks. 100%)\n[EndSkill] zużywa wszystkie [WindBlade] tej jednostki
184. [Umiejętność sojusznika [40003804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 5 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40003804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 5 [Breath]
   PL: [OnSucceedAttack] zyskuje 5 [Breath]
185. [Umiejętność sojusznika [40003804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40003804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Umiejętność sojusznika [40003804] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40003804].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność sojusznika [40003804] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40003804].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Umiejętność sojusznika [40003804] (ulepszenie 1) — moneta 4, efekt 2 — opis] [CriticalOnSucceedAttack] 자신의 [Agility]이 5 이상이면, 코인 재사용 (스킬당 1회)
   źródło: Skills_Assist-exme.json :: dataList[id=40003804].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Agility]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Agility] = 신속 / Haste
   EN: [CriticalOnSucceedAttack] At 5+ [Agility], Reuse this Coin (once per Skill)
   PL: [CriticalOnSucceedAttack] przy 5+ [Agility] używa tej Monety ponownie (1 raz na Umiejętność)
189. [Umiejętność sojusznika [40003805] (ulepszenie 1) — nazwa] 골단
   źródło: Skills_Assist-exme.json :: dataList[id=40003805].levelList[level=1].name
   limit: do 40 znaków
   EN: To Claim Their Bones
   PL: To Claim Their Bones
190. [Umiejętność sojusznika [40003805] (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않음\n자신의 잃은 체력 1%당 피해량 0.5% 증가 (최대 25%)\n자신의 [Agility] 1당, 크리티컬 피해량 +10% (최대 50%)\n[WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 4당, 기본 위력 +1 (최대 4)
   źródło: Skills_Assist-exme.json :: dataList[id=40003805].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [Agility], [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [Agility] = 신속 / Haste; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills\nDeal +0.5% damage for every 1% missing HP on self (max 25%)\nDeal +10% damage on Critical Hit for every [Agility] on self (max 50%)\n[WhenUse] Base Power +1 for every 4 ([Breath] on self + [Laceration] on target) (max 4)
   PL: [CantDuel]\nta Umiejętność nie uruchamia Umiejętności obrony celu\nzadaje +0.5% obrażeń za każde 1% utraconego HP tej jednostki (maks. 25%)\nzadaje +10% obrażeń krytycznych za każde 1 [Agility] tej jednostki (maks. 50%)\n[WhenUse] Moc Bazowa +1 za każde 4 ([Breath] tej jednostki + [Laceration] celu) (maks. 4)
191. [Umiejętność sojusznika [40003805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40003805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność sojusznika [40003805] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40003805].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność sojusznika [40003805] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40003805].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis] next turn
   PL: [OnSucceedAttack] nakłada 2 [Paralysis] w następnej turze
194. [Umiejętność sojusznika [40003806] (ulepszenie 1) — nazwa] 앞길을 밝힐게요
   źródło: Skills_Assist-exme.json :: dataList[id=40003806].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Light the Path Forward
   PL: I'll Light the Path Forward
195. [Umiejętność sojusznika [40003806] (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] [SupportProtect] 1 얻음\n[WhenUse] [Breath] 5 얻음\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Assist-exme.json :: dataList[id=40003806].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [SupportProtect], [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n[StartBattle] Gain 1 [SupportProtect]\n[WhenUse] Gain 5 [Breath]\n[WinDuel] Gain +2 [Breath] Count
   PL: [CanDuelGuard]\n[StartBattle] zyskuje 1 [SupportProtect]\n[WhenUse] zyskuje 5 [Breath]\n[WinDuel] zyskuje 2 Licznika [Breath]
196. [Umiejętność sojusznika [40003806] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-exme.json :: dataList[id=40003806].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Umiejętność sojusznika [40003807] (ulepszenie 1) — nazwa] 형세 읽기
   źródło: Skills_Assist-exme.json :: dataList[id=40003807].levelList[level=1].name
   limit: do 50 znaków
   EN: Observing the Stones on the Board
   PL: Observing the Stones on the Board
198. [Umiejętność sojusznika [40003807] (ulepszenie 1) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n[WhenUse] [Breath] 5 얻음\n[WhenUse] [Breath]이 25를 초과했으면, [Breath] 5를 소모하여 [WindBlade] 3 얻음\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Assist-exme.json :: dataList[id=40003807].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [SupportProtect], [WhenUse], [Breath], [WindBlade], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WindBlade] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n[SupportProtect] Exclusive Skill\n[WhenUse] Gain 5 [Breath]\n[WhenUse] At more than 25 [Breath], consume 5 [Breath] to gain 3 [WindBlade]\n[WinDuel] Gain +2 [Breath] Count
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [SupportProtect]\n[WhenUse] zyskuje 5 [Breath]\n[WhenUse] przy [Breath] powyżej 25 zużywa 5 [Breath], aby zyskać 3 [WindBlade]\n[WinDuel] zyskuje 2 Licznika [Breath]
199. [Umiejętność sojusznika [40003807] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-exme.json :: dataList[id=40003807].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Umiejętność sojusznika [40004001] (ulepszenie 1) — nazwa] 발검
   źródło: Skills_Assist-exme.json :: dataList[id=40004001].levelList[level=1].name
   limit: do 40 znaków
   EN: Draw of the Sword
   PL: Draw of the Sword
201. [Umiejętność sojusznika [40004001] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 5 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[WinDuel] [Breath] 3 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40004001].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] At 5+ [Breath], Coin Power +1\n[WhenUse] Gain +2 [Breath] Count\n[WinDuel] Gain 3 [Breath]
   PL: [WhenUse] przy 5+ [Breath] Moc Monety +1\n[WhenUse] zyskuje 2 Licznika [Breath]\n[WinDuel] zyskuje 3 [Breath]
202. [Umiejętność sojusznika [40004001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40004001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Umiejętność sojusznika [40004001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40004001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Umiejętność sojusznika [40004001] (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-exme.json :: dataList[id=40004001].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [CriticalOnSucceedAttack] zwiększa Licznik [Laceration] o 2
205. [Umiejętność sojusznika [40004002] (ulepszenie 1) — nazwa] 자법
   źródło: Skills_Assist-exme.json :: dataList[id=40004002].levelList[level=1].name
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Umiejętność sojusznika [40004002] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 7 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n[WinDuel] [Breath] 2 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40004002].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] At 7+ [Breath], Coin Power +1\n[WhenUse] Gain +3 [Breath] Count\n[WinDuel] Gain 2 [Breath]
   PL: [WhenUse] przy 7+ [Breath] Moc Monety +1\n[WhenUse] zyskuje 3 Licznika [Breath]\n[WinDuel] zyskuje 2 [Breath]
207. [Umiejętność sojusznika [40004002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40004002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 4 [Breath]
   PL: [OnSucceedAttack] zyskuje 4 [Breath]
208. [Umiejętność sojusznika [40004002] (ulepszenie 1) — moneta 2, efekt 1 — opis] 크리티컬 피해량 +20%
   źródło: Skills_Assist-exme.json :: dataList[id=40004002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +20% damage on Critical Hit
   PL: +20% obrażeń krytycznych
209. [Umiejętność sojusznika [40004002] (ulepszenie 1) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +40%
   źródło: Skills_Assist-exme.json :: dataList[id=40004002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +40% damage on Critical Hit
   PL: +40% obrażeń krytycznych
210. [Umiejętność sojusznika [40004002] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Assist-exme.json :: dataList[id=40004002].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Umiejętność sojusznika [40004003] (ulepszenie 1) — nazwa] 살주
   źródło: Skills_Assist-exme.json :: dataList[id=40004003].levelList[level=1].name
   limit: do 40 znaków
   EN: Overthrow
   PL: Overthrow
212. [Umiejętność sojusznika [40004003] (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] 이번 턴과 다음 턴에 [SlashDamageUp] 2 얻음\n[WhenUse] 자신의 [Breath]이 8 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n[WinDuel] [Breath] 4 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40004003].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [SlashDamageUp], [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [DuelCounter]\n[StartBattle] Gain 2 [SlashDamageUp] this turn and next turn\n[WhenUse] At 8+ [Breath], Coin Power +1\n[WhenUse] Gain +3 [Breath] Count\n[WinDuel] Gain 4 [Breath]
   PL: [DuelCounter]\n[StartBattle] zyskuje 2 [SlashDamageUp] w tej i w następnej turze\n[WhenUse] przy 8+ [Breath] Moc Monety +1\n[WhenUse] zyskuje 3 Licznika [Breath]\n[WinDuel] zyskuje 4 [Breath]
213. [Umiejętność sojusznika [40004003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 5 얻음
   źródło: Skills_Assist-exme.json :: dataList[id=40004003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Umiejętność sojusznika [40004003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Assist-exme.json :: dataList[id=40004003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL: [OnSucceedAttack] zyskuje 2 Licznika [Breath]
215. [Umiejętność sojusznika [40004003] (ulepszenie 1) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +80%
   źródło: Skills_Assist-exme.json :: dataList[id=40004003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +80% damage on Critical Hit
   PL: +80% obrażeń krytycznych
216. [Umiejętność sojusznika [40004003] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40004003].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 8 [Laceration]
   PL: [OnSucceedAttack] nakłada 8 [Laceration]
217. [Umiejętność sojusznika [40004004] (ulepszenie 1) — nazwa] 육참
   źródło: Skills_Assist-exme.json :: dataList[id=40004004].levelList[level=1].name
   limit: do 40 znaków
   EN: Yield My Flesh
   PL: Yield My Flesh
218. [Umiejętność sojusznika [40004004] (ulepszenie 1) — opis] 최대 위력이 가장 높은 스킬 슬롯을 우선 지정함\n[WhenUse] 이 스킬 종료 시까지\n- 자신의 [Breath] 1당, 공격으로 받는 피해량 -2% (최소 -80%)\n- 자신의 [Breath] 1당, 합 위력 -1 (최소 -30)\n- 피해로 인해 흐트러짐 상태가 되지 않음\n[WinDuel] [Breath] 5 얻음\n[DefeatDuel] 피격 후 ‘골단’ 사용\n[EndBattle] 다음 턴까지 ‘육참’ 사용 불가능
   źródło: Skills_Assist-exme.json :: dataList[id=40004004].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel], [DefeatDuel], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: Targets the Skill Slot that has the highest max Power\n[WhenUse] Until this Skill ends:\n- Take -2% damage from Attacks for every [Breath] on self (min -80%)\n- Clash Power -1 for every [Breath] on self (min -30)\n- Cannot be Staggered from taking damage\n[WinDuel] Gain 5 [Breath]\n[DefeatDuel] Use "To Claim Their Bones" after being hit\n[EndBattle] Cannot use "Yield My Flesh" until next turn
   PL: celuje w Slot Umiejętności z najwyższą maksymalną Mocą\n[WhenUse] do końca tej Umiejętności:\n- otrzymuje o 2% mniej obrażeń z Ataków za każde 1 [Breath] tej jednostki (min. -80%)\n- Moc Starcia -1 za każde 1 [Breath] tej jednostki (min. -30)\n- nie przechodzi w Oszołomienie od otrzymywanych obrażeń\n[WinDuel] zyskuje 5 [Breath]\n[DefeatDuel] po otrzymaniu trafienia używa „To Claim Their Bones”\n[EndBattle] do następnej tury nie może użyć „Yield My Flesh”
219. [Umiejętność sojusznika [40004004] (ulepszenie 1) — moneta 1, efekt 1 — opis] 크리티컬 피해량 +150%
   źródło: Skills_Assist-exme.json :: dataList[id=40004004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +150% damage on Critical Hit
   PL: +150% obrażeń krytycznych
220. [Umiejętność sojusznika [40004004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [SlashResistDown] 2 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40004004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [OnSucceedAttack] Inflict 2 [SlashResistDown] next turn
   PL: [OnSucceedAttack] nakłada 2 [SlashResistDown] w następnej turze
221. [Umiejętność sojusznika [40004004] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 4 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40004004].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 4 [DefenseDown] next turn
   PL: [OnSucceedAttack] nakłada 4 [DefenseDown] w następnej turze
222. [Umiejętność sojusznika [40004005] (ulepszenie 1) — nazwa] 골단
   źródło: Skills_Assist-exme.json :: dataList[id=40004005].levelList[level=1].name
   (powtórzenie elementu 189 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Umiejętność sojusznika [40004005] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 10 이상이면, 코인 위력 +1\n[WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당, 피해량 +40% (집중 전투인 경우, 부위로 판정)\n[WhenUse] 자신의 [Breath] 횟수 4 증가\n[EndSkill] 자신의 [Breath] 전부 소모
   źródło: Skills_Assist-exme.json :: dataList[id=40004005].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] At 10+ [Breath], Coin Power +1\n[WhenUse] Deal +40% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Parts)\n[WhenUse] Gain +4 [Breath] Count\n[EndSkill] Consume all [Breath] on self
   PL: [WhenUse] przy 10+ [Breath] Moc Monety +1\n[WhenUse] zadaje +40% obrażeń za każdą nadwyżkową Wagę Ataku ponad liczbę rzeczywistych celów (w walkach skupionych rozpatrywane per Część)\n[WhenUse] zyskuje 4 Licznika [Breath]\n[EndSkill] zużywa wszystkie [Breath] tej jednostki
224. [Umiejętność sojusznika [40004005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 마지막 코인 위력 +2 (코인당 1회)
   źródło: Skills_Assist-exme.json :: dataList[id=40004005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Coin Power +2 for the final Coin (once per Coin)
   PL: [CriticalOnSucceedAttack] Moc Monety +2 dla ostatniej Monety (1 raz na Monetę)
225. [Umiejętność sojusznika [40004005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] 마지막 코인 위력 +2 (코인당 1회)
   źródło: Skills_Assist-exme.json :: dataList[id=40004005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność sojusznika [40004005] (ulepszenie 1) — moneta 3, efekt 1 — opis] [CriticalOnSucceedAttack] 마지막 코인 위력 +2 (코인당 1회)
   źródło: Skills_Assist-exme.json :: dataList[id=40004005].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność sojusznika [40004005] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 10 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Assist-exme.json :: dataList[id=40004005].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 10 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 10 [Laceration] i zwiększa Licznik [Laceration] o 2
228. [Umiejętność sojusznika [40004005] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40004005].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Umiejętność sojusznika [40003901] (ulepszenie 1) — nazwa] 유리아 공방 - 총공 모드, 마크 17!
   źródło: Skills_Assist-exme.json :: dataList[id=40003901].levelList[level=1].name
   limit: do 60 znaków
   EN: YuRia Atelier - All-out Attack Mode, Mk. 17!
   PL: YuRia Atelier - All-out Attack Mode, Mk. 17!
230. [Umiejętność sojusznika [40003901] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류당, 피해량 +50% (최대 100%)\n[WhenUse] 대상의 [Vibration]이 6 이상이면, 기본 위력 +3
   źródło: Skills_Assist-exme.json :: dataList[id=40003901].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: Deal +50% damage for every type of negative effect on target (max 100%)\n[WhenUse] If target has 6+ [Vibration], Base Power +3
   PL: zadaje +50% obrażeń za każdy rodzaj negatywnego efektu celu (maks. 100%)\n[WhenUse] jeżeli cel ma 6+ [Vibration], Moc Bazowa +3
231. [Umiejętność sojusznika [40003901] (ulepszenie 1) — tekst klimatyczny] 특별 수제작, 골든 리트리버 전용 도끼.
   źródło: Skills_Assist-exme.json :: dataList[id=40003901].levelList[level=1].flavor
   limit: do 120 znaków
   EN: Special Handmade Golden Retriever-Exclusive Axe.
   PL: Special Handmade Golden Retriever-Exclusive Axe.
232. [Umiejętność sojusznika [40003901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-exme.json :: dataList[id=40003901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Umiejętność sojusznika [40003901] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-exme.json :: dataList[id=40003901].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Umiejętność sojusznika [40003901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-exme.json :: dataList[id=40003901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność sojusznika [40003901] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Assist-exme.json :: dataList[id=40003901].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Vibration] o 2
236. [Umiejętność sojusznika [40003901] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-exme.json :: dataList[id=40003901].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Umiejętność sojusznika [40003901] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40003901].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [Umiejętność sojusznika [40003901] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Assist-exme.json :: dataList[id=40003901].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] nakłada 3 [Vibration]
239. [Umiejętność sojusznika [40003901] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-exme.json :: dataList[id=40003901].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Umiejętność sojusznika [40003901] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Assist-exme.json :: dataList[id=40003901].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on target once. Target loses 1 [Laceration] Count
   PL: [OnSucceedAttack] aktywuje [Laceration] na celu 1 raz. Cel traci 1 Licznika [Laceration]
241. [Umiejętność sojusznika [40003901] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Assist-exme.json :: dataList[id=40003901].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
242. [Umiejętność sojusznika [40003902] (ulepszenie 1) — nazwa] 원호해줄게! 뒤로 빠져있어!
   źródło: Skills_Assist-exme.json :: dataList[id=40003902].levelList[level=1].name
   limit: do 50 znaków
   EN: I'll Cover You! Get Behind Me!
   PL: I'll Cover You! Get Behind Me!
243. [Umiejętność sojusznika [40003902] (ulepszenie 1) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n[WinDuel] 아군 정신력 4 회복 (본인 포함)\n- LCD 소속이면, 대신 정신력 8 회복
   źródło: Skills_Assist-exme.json :: dataList[id=40003902].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [SupportProtect], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n[SupportProtect] Exclusive Skill\n[WinDuel] Heal 4 SP for all allies (including this unit)\n- Heal 8 SP instead for LCD Units
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [SupportProtect]\n[WinDuel] przywraca 4 SP wszystkim sojusznikom (wliczając tę jednostkę)\n- dla jednostek LCD zamiast tego przywraca 8 SP
244. [Umiejętność sojusznika [40003902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-exme.json :: dataList[id=40003902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Umiejętności jednostek wsparcia — Skills_Assist-twth
- plik gry: `Skills_Assist-twth.json`

245. [Umiejętność sojusznika [40003701] (ulepszenie 1) — nazwa] 몸 좀 풀어볼까?
   źródło: Skills_Assist-twth.json :: dataList[id=40003701].levelList[level=1].name
   limit: do 40 znaków
   EN: Time for Some Warm-up!
   PL: Time for Some Warm-up!
246. [Umiejętność sojusznika [40003701] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Laceration]의 합이 3 이상이면 최종 위력 +2
   źródło: Skills_Assist-twth.json :: dataList[id=40003701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Laceration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: If target has 3+ ([Combustion] + [Laceration]), Final Power +2
   PL: jeżeli cel ma 3+ ([Combustion] + [Laceration]), Moc Końcowa +2
247. [Umiejętność sojusznika [40003701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 3
   źródło: Skills_Assist-twth.json :: dataList[id=40003701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 3 Blunt bonus damage
   PL: [OnSucceedAttack] zadaje 3 dodatkowych obrażeń Uderzeniem
248. [Umiejętność sojusznika [40003701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 3
   źródło: Skills_Assist-twth.json :: dataList[id=40003701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 247 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Umiejętność sojusznika [40003701] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-twth.json :: dataList[id=40003701].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Umiejętność sojusznika [40003701] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 추가 타격 피해 3
   źródło: Skills_Assist-twth.json :: dataList[id=40003701].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 247 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Umiejętność sojusznika [40003701] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신에게 [ReinforcedTattooSpiderDaughterTwo]이 있으면, 다음 턴에 [Binding] 2 부여
   źródło: Skills_Assist-twth.json :: dataList[id=40003701].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ReinforcedTattooSpiderDaughterTwo], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ReinforcedTattooSpiderDaughterTwo] = 중지식 강화문신 / The Middle Styled Augmentation Tattoos; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] If this unit has [ReinforcedTattooSpiderDaughterTwo], inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] jeżeli ta jednostka ma [ReinforcedTattooSpiderDaughterTwo], nakłada 2 [Binding] w następnej turze
252. [Umiejętność sojusznika [40003702] (ulepszenie 1) — nazwa] 욜라 패기
   źródło: Skills_Assist-twth.json :: dataList[id=40003702].levelList[level=1].name
   limit: do 40 znaków
   EN: Totally Badass Ass-kicking
   PL: Totally Badass Ass-kicking
253. [Umiejętność sojusznika [40003702] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Laceration]의 합이 3 이상이면 최종 위력 +2\n[WhenUse] 자신에게 [ReinforcedTattooSpiderDaughterTwo]이 있으면, 코인 적중시 [Laceration] 2 부여
   źródło: Skills_Assist-twth.json :: dataList[id=40003702].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [WhenUse], [ReinforcedTattooSpiderDaughterTwo]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpiderDaughterTwo] = 중지식 강화문신 / The Middle Styled Augmentation Tattoos
   EN: If target has 3+ ([Combustion] + [Laceration]), Final Power +2\n[WhenUse] If this unit has [ReinforcedTattooSpiderDaughterTwo], inflict 2 [Laceration] On Coin Hit
   PL: jeżeli cel ma 3+ ([Combustion] + [Laceration]), Moc Końcowa +2\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpiderDaughterTwo], nakłada 2 [Laceration] przy trafieniu Monetą
254. [Umiejętność sojusznika [40003702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 5
   źródło: Skills_Assist-twth.json :: dataList[id=40003702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 Blunt bonus damage
   PL: [OnSucceedAttack] zadaje 5 dodatkowych obrażeń Uderzeniem
255. [Umiejętność sojusznika [40003702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 흐트러짐 손상 5
   źródło: Skills_Assist-twth.json :: dataList[id=40003702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 5
   PL: [OnSucceedAttack] podnosi Próg Oszołomienia o 5
256. [Umiejętność sojusznika [40003702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 5
   źródło: Skills_Assist-twth.json :: dataList[id=40003702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Umiejętność sojusznika [40003702] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 흐트러짐 손상 5
   źródło: Skills_Assist-twth.json :: dataList[id=40003702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 255 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Umiejętność sojusznika [40003702] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 [ResentmentSpiderDaughterTwo]이 3 이상이면, 이 코인 3회 재사용
   źródło: Skills_Assist-twth.json :: dataList[id=40003702].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ResentmentSpiderDaughterTwo]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ResentmentSpiderDaughterTwo] = 중지 - 원한 / The Middle - Grudge
   EN: [OnSucceedAttack] At 3+ [ResentmentSpiderDaughterTwo], Reuse this Coin 3 times
   PL: [OnSucceedAttack] przy 3+ [ResentmentSpiderDaughterTwo] używa tej Monety ponownie 3 razy
259. [Umiejętność sojusznika [40003703] (ulepszenie 1) — nazwa] 배 가르기!
   źródło: Skills_Assist-twth.json :: dataList[id=40003703].levelList[level=1].name
   limit: do 40 znaków
   EN: Disemboweling!
   PL: Disemboweling!
260. [Umiejętność sojusznika [40003703] (ulepszenie 1) — opis] 이 스킬은 [HeatingWireOnSpiderTwo] 상태일 때 열선[TabExplain] 효과가 적용됨\n대상의 [Combustion]과 [Laceration]의 합이 3 이상이면 코인 위력 +1\n[WhenUse] 자신에게 [ReinforcedTattooSpiderDaughterTwo]이 있으면, 코인 적중시 대상의 [Laceration] 횟수 1 증가\n[EndSkill] 자신의 [ResentmentSpiderDaughterTwo]이 3 이상이면, 다음 턴에 [VioletDamageUp] 1 얻음
   źródło: Skills_Assist-twth.json :: dataList[id=40003703].levelList[level=1].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [HeatingWireOnSpiderTwo], [TabExplain], [Combustion], [Laceration], [WhenUse], [ReinforcedTattooSpiderDaughterTwo], [EndSkill], [ResentmentSpiderDaughterTwo], [VioletDamageUp]
   znaczenie tagów: [HeatingWireOnSpiderTwo] = 열선 ON / Thermal Blades ON; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpiderDaughterTwo] = 중지식 강화문신 / The Middle Styled Augmentation Tattoos; [EndSkill] = [공격 종료시] / [Attack End]; [ResentmentSpiderDaughterTwo] = 중지 - 원한 / The Middle - Grudge; [VioletDamageUp] = 질투 피해량 증가 / Envy DMG Up
   EN: Thermal Blade Skill. \nWhen in [HeatingWireOnSpiderTwo] state, this Skill activates its Thermal Blade effects\nIf target has 3+ ([Combustion] + [Laceration]), Coin Power +1\n[WhenUse] If this unit has [ReinforcedTattooSpiderDaughterTwo], inflict +1 [Laceration] Count On Coin Hit\n[EndSkill] At 3+ [ResentmentSpiderDaughterTwo], gain 1 [VioletDamageUp] next turn
   PL: Ta Umiejętność aktywuje efekty Termicznego Ostrza[TabExplain], gdy jest w stanie [HeatingWireOnSpiderTwo]\njeżeli cel ma 3+ ([Combustion] + [Laceration]), Moc Monety +1\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpiderDaughterTwo], zwiększa przy trafieniu Monetą Licznik [Laceration] celu o 1\n[EndSkill] przy 3+ [ResentmentSpiderDaughterTwo] zyskuje 1 [VioletDamageUp] w następnej turze
261. [Umiejętność sojusznika [40003703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Assist-twth.json :: dataList[id=40003703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Umiejętność sojusznika [40003703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-twth.json :: dataList[id=40003703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Umiejętność sojusznika [40003704] (ulepszenie 1) — nazwa] 십자난무!
   źródło: Skills_Assist-twth.json :: dataList[id=40003704].levelList[level=1].name
   limit: do 40 znaków
   EN: Crossing Dervish!
   PL: Crossing Dervish!
264. [Umiejętność sojusznika [40003704] (ulepszenie 1) — opis] 이 스킬은 [HeatingWireOnSpiderTwo] 상태일 때 열선[TabExplain] 효과가 적용됨\n대상의 [Combustion]과 [Laceration]의 합이 3 이상이면 코인 위력 +1\n[WhenUse] 자신에게 [ReinforcedTattooSpiderDaughterTwo]이 있으면, 코인 적중시 대상의 [Laceration] 횟수 1 증가
   źródło: Skills_Assist-twth.json :: dataList[id=40003704].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [HeatingWireOnSpiderTwo], [TabExplain], [Combustion], [Laceration], [WhenUse], [ReinforcedTattooSpiderDaughterTwo]
   znaczenie tagów: [HeatingWireOnSpiderTwo] = 열선 ON / Thermal Blades ON; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpiderDaughterTwo] = 중지식 강화문신 / The Middle Styled Augmentation Tattoos
   EN: Thermal Blade Skill. \nWhen in [HeatingWireOnSpiderTwo] state, this Skill activates its Thermal Blade effects\nIf target has 3+ ([Combustion] + [Laceration]), Coin Power +1\n[WhenUse] If this unit has [ReinforcedTattooSpiderDaughterTwo], inflict +1 [Laceration] Count On Coin Hit
   PL: Ta Umiejętność aktywuje efekty Termicznego Ostrza[TabExplain], gdy jest w stanie [HeatingWireOnSpiderTwo]\njeżeli cel ma 3+ ([Combustion] + [Laceration]), Moc Monety +1\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpiderDaughterTwo], zwiększa przy trafieniu Monetą Licznik [Laceration] celu o 1
265. [Umiejętność sojusznika [40003704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-twth.json :: dataList[id=40003704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Umiejętność sojusznika [40003704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Assist-twth.json :: dataList[id=40003704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Umiejętność sojusznika [40003704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-twth.json :: dataList[id=40003704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Umiejętność sojusznika [40003704] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-twth.json :: dataList[id=40003704].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Umiejętność sojusznika [40003704] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-twth.json :: dataList[id=40003704].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [Umiejętność sojusznika [40003704] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-twth.json :: dataList[id=40003704].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Umiejętność sojusznika [40003704] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-twth.json :: dataList[id=40003704].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Umiejętność sojusznika [40003704] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 추가 타격 피해 5
   źródło: Skills_Assist-twth.json :: dataList[id=40003704].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Umiejętność sojusznika [40003704] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 자신에게 [ReinforcedTattooSpiderDaughterTwo]이 있으면, 다음 턴에 [Binding] 2 부여
   źródło: Skills_Assist-twth.json :: dataList[id=40003704].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Umiejętność sojusznika [40003705] (ulepszenie 1) — nazwa] 바이올렛 브레이크 슬램!
   źródło: Skills_Assist-twth.json :: dataList[id=40003705].levelList[level=1].name
   limit: do 40 znaków
   EN: Violet~ Breaking Slam!
   PL: Violet~ Breaking Slam!
275. [Umiejętność sojusznika [40003705] (ulepszenie 1) — opis] 이 스킬은 [HeatingWireOnSpiderTwo] 상태일 때 열선[TabExplain] 효과가 적용됨\n대상의 [Combustion]과 [Laceration]의 합이 3 이상이면 코인 위력 +1\n[WhenUse] 자신에게 [ReinforcedTattooSpiderDaughterTwo]이 있으면, 코인 적중시 대상의 [Laceration] 횟수 1 증가\n[WhenUse] 자신의 체력이 40% 이하거나 [ReinforcedTattooSpiderDaughterTwo]이 2 이상이면, 피해량 +60%\n[WhenUse] 자신의 [ResentmentSpiderDaughterTwo]이 2 이상이면, 코인 적중시 50% 확률로 [Paralysis] 1 부여\n[EndSkill] 자신의 [ResentmentSpiderDaughterTwo]을 전부 소모
   źródło: Skills_Assist-twth.json :: dataList[id=40003705].levelList[level=1].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n, [HeatingWireOnSpiderTwo], [TabExplain], [Combustion], [Laceration], [WhenUse], [ReinforcedTattooSpiderDaughterTwo], [ResentmentSpiderDaughterTwo], [Paralysis], [EndSkill]
   znaczenie tagów: [HeatingWireOnSpiderTwo] = 열선 ON / Thermal Blades ON; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpiderDaughterTwo] = 중지식 강화문신 / The Middle Styled Augmentation Tattoos; [ResentmentSpiderDaughterTwo] = 중지 - 원한 / The Middle - Grudge; [Paralysis] = 마비 / Paralyze; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Thermal Blade Skill. \nWhen in [HeatingWireOnSpiderTwo] state, this Skill activates its Thermal Blade effects\nIf target has 3+ ([Combustion] + [Laceration]), Coin Power +1\n[WhenUse] If this unit has [ReinforcedTattooSpiderDaughterTwo], inflict +1 [Laceration] Count On Coin Hit\n[WhenUse] At 40%- HP or 2+ [ReinforcedTattooSpiderDaughterTwo], deal +60% damage\n[WhenUse] At 2+ [ResentmentSpiderDaughterTwo], 50% chance to inflict 1 [Paralysis] On Coin Hit\n[EndSkill] Consume all [ResentmentSpiderDaughterTwo] on self
   PL: Ta Umiejętność aktywuje efekty Termicznego Ostrza[TabExplain], gdy jest w stanie [HeatingWireOnSpiderTwo]\njeżeli cel ma 3+ ([Combustion] + [Laceration]), Moc Monety +1\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpiderDaughterTwo], zwiększa przy trafieniu Monetą Licznik [Laceration] celu o 1\n[WhenUse] przy HP tej jednostki 40% lub mniej albo przy 2+ [ReinforcedTattooSpiderDaughterTwo] zadaje +60% obrażeń\n[WhenUse] przy 2+ [ResentmentSpiderDaughterTwo] 50% szansy na nałożenie 1 [Paralysis] przy trafieniu Monetą\n[EndSkill] zużywa wszystkie [ResentmentSpiderDaughterTwo] tej jednostki
276. [Umiejętność sojusznika [40003705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-twth.json :: dataList[id=40003705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Umiejętność sojusznika [40003705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Assist-twth.json :: dataList[id=40003705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Umiejętność sojusznika [40003705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-twth.json :: dataList[id=40003705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Umiejętność sojusznika [40003705] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-twth.json :: dataList[id=40003705].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Umiejętność sojusznika [40003705] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-twth.json :: dataList[id=40003705].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Umiejętność sojusznika [40003705] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-twth.json :: dataList[id=40003705].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Umiejętność sojusznika [40003705] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-twth.json :: dataList[id=40003705].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność sojusznika [40003705] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 추가 타격 피해 5
   źródło: Skills_Assist-twth.json :: dataList[id=40003705].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Umiejętność sojusznika [40003705] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 흐트러짐 손상 5
   źródło: Skills_Assist-twth.json :: dataList[id=40003705].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 255 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Umiejętność sojusznika [40003705] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-twth.json :: dataList[id=40003705].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Umiejętność sojusznika [40003705] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Assist-twth.json :: dataList[id=40003705].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Umiejętność sojusznika [40003706] (ulepszenie 1) — nazwa] 가만 안둬
   źródło: Skills_Assist-twth.json :: dataList[id=40003706].levelList[level=1].name
   limit: do 50 znaków
   EN: I'll Get You Back for This...!
   PL: I'll Get You Back for This...!
288. [Umiejętność sojusznika [40003706] (ulepszenie 1) — opis] 이 스킬은 [HeatingWireOnSpiderTwo] 상태일 때 열선[TabExplain] 효과가 적용됨\n피격 시 자신의 [ReinforcedTattooSpiderDaughterTwo] 1당 이 스킬 1회 재사용 (최대 2회)\n[WhenUse] 자신에게 [ReinforcedTattooSpiderDaughterTwo]이 있으면, 코인 적중시 [Laceration] 1 부여\n[WhenUse] 자신의 체력이 40% 이하거나 [ReinforcedTattooSpiderDaughterTwo]이 2 이상이면, 피해량 +40%
   źródło: Skills_Assist-twth.json :: dataList[id=40003706].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [HeatingWireOnSpiderTwo], [TabExplain], [ReinforcedTattooSpiderDaughterTwo], [WhenUse], [Laceration]
   znaczenie tagów: [HeatingWireOnSpiderTwo] = 열선 ON / Thermal Blades ON; [ReinforcedTattooSpiderDaughterTwo] = 중지식 강화문신 / The Middle Styled Augmentation Tattoos; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: Thermal Blade Skill. \nWhen in [HeatingWireOnSpiderTwo] state, this Skill activates its Thermal Blade effects\nWhen hit, Reuse this Skill once for every [ReinforcedTattooSpiderDaughterTwo] on self (max 2 times)\n[WhenUse] If this unit has [ReinforcedTattooSpiderDaughterTwo], inflict 1 [Laceration] On Coin Hit\n[WhenUse] At 40%- HP or 2+ [ReinforcedTattooSpiderDaughterTwo], deal +40% damage
   PL: Ta Umiejętność aktywuje efekty Termicznego Ostrza[TabExplain], gdy jest w stanie [HeatingWireOnSpiderTwo]\nprzy otrzymaniu trafienia używa tej Umiejętności ponownie 1 raz za każde 1 [ReinforcedTattooSpiderDaughterTwo] tej jednostki (maks. 2 razy)\n[WhenUse] jeżeli ta jednostka ma [ReinforcedTattooSpiderDaughterTwo], nakłada 1 [Laceration] przy trafieniu Monetą\n[WhenUse] przy HP tej jednostki 40% lub mniej albo przy 2+ [ReinforcedTattooSpiderDaughterTwo] zadaje +40% obrażeń
289. [Umiejętność sojusznika [40003706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-twth.json :: dataList[id=40003706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Umiejętność sojusznika [40003706] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Assist-twth.json :: dataList[id=40003706].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Umiejętność sojusznika [40003706] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 흐트러짐 회복 10
   źródło: Skills_Assist-twth.json :: dataList[id=40003706].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 10
   PL: [OnSucceedAttack] obniża Próg Oszołomienia użytkownika o 10

## Umiejętności jednostek wsparcia — Skills_Assist-walpu6
- plik gry: `Skills_Assist-walpu6.json`

292. [Umiejętność sojusznika [40000301] (ulepszenie 1) — nazwa] 사랑으로!
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000301].levelList[level=1].name
   limit: do 40 znaków
   EN: With Love!
   PL: With Love!
293. [Umiejętność sojusznika [40000301] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]과 [Sinking]의 합 5 당 기본 위력 +1 (최대 2)\n[WhenUse] 자신의 [PowerOfLoveAndJustice] 횟수 10 증가
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000301].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Sinking], [PowerOfLoveAndJustice]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [PowerOfLoveAndJustice] = 사랑/정의 / Love/Justice
   EN: [WhenUse] Base Power +1 for every 5 ([Burst] + [Sinking]) on target (max 2)\n[WhenUse] Gain +10 [PowerOfLoveAndJustice]
   PL: [WhenUse] Moc Bazowa +1 za każde 5 ([Burst] + [Sinking]) celu (maks. 2)\n[WhenUse] zyskuje 10 Licznika [PowerOfLoveAndJustice]
294. [Umiejętność sojusznika [40000301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL: [OnSucceedAttack] nakłada 1 [Burst]
295. [Umiejętność sojusznika [40000301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Umiejętność sojusznika [40000302] (ulepszenie 1) — nazwa] 정의의 이름으로!
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000302].levelList[level=1].name
   limit: do 40 znaków
   EN: In the Name of Justice!
   PL: In the Name of Justice!
297. [Umiejętność sojusznika [40000302] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]과 [Sinking]의 합 7 당 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [PowerOfLoveAndJustice] 횟수 10 증가
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000302].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Sinking], [PowerOfLoveAndJustice]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [PowerOfLoveAndJustice] = 사랑/정의 / Love/Justice
   EN: [WhenUse] Coin Power +1 for every 7 ([Burst] + [Sinking]) on target (max 2)\n[WhenUse] Gain +10 [PowerOfLoveAndJustice] Count
   PL: [WhenUse] Moc Monety +1 za każde 7 ([Burst] + [Sinking]) celu (maks. 2)\n[WhenUse] zyskuje 10 Licznika [PowerOfLoveAndJustice]
298. [Umiejętność sojusznika [40000302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność sojusznika [40000302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]과 [Sinking]의 합이 10 이상이면, 다음 턴에 [Binding] 1 부여
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [Sinking], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] If target has 10+ ([Burst] + [Sinking]), inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] jeżeli cel ma 10+ ([Burst] + [Sinking]), nakłada 1 [Binding] w następnej turze
300. [Umiejętność sojusznika [40000303] (ulepszenie 1) — nazwa] 아르카나 비트
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000303].levelList[level=1].name
   limit: do 40 znaków
   EN: Arcana Beats
   PL: Arcana Beats
301. [Umiejętność sojusznika [40000303] (ulepszenie 1) — opis] 절망의 기사를 메인 타겟으로 지정함\n[ColdBlackTear]이 가장 많은 아군을 서브 타겟으로 지정함\n- 없을 시, 체력이 가장 적은 아군을 서브 타겟으로 지정함\n아군에게는 피해를 0으로 부여하고, [Sinking] 및 [ColdBlackTear] 효과를 발동하지 않음\n\n[WinDuel] 서브 타겟인 아군의 [ColdBlackTear] 1 제거
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000303].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [ColdBlackTear], [Sinking], [WinDuel]
   znaczenie tagów: [ColdBlackTear] = 차갑고 검은 눈물 / Cold, Black Tears; [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Mainly targets 'The Knight of Despair'\nSub-targets the ally with the most [ColdBlackTear]\n- If there are none, sub-targets the ally with the least HP\nInflicts 0 damage and does not activate the effects of [Sinking] and [ColdBlackTear] against allies\n\n[WinDuel] Remove 1 [ColdBlackTear] from the sub-targeted ally
   PL: głównie celuje w „Rycerza Rozpaczy”\ncele poboczne: sojusznik z największą liczbą [ColdBlackTear]\n- w razie braku — sojusznik z najmniejszym HP\nzadaje sojusznikom 0 obrażeń i nie aktywuje efektów [Sinking] ani [ColdBlackTear]\n\n[WinDuel] usuwa 1 [ColdBlackTear] z sojusznika będącego celem pobocznym
302. [Umiejętność sojusznika [40000303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 적군인 경우, [Burst] 1 부여
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target is an enemy, Inflict 1 [Burst]
   PL: [OnSucceedAttack] jeżeli cel jest wrogiem, nakłada 1 [Burst]
303. [Umiejętność sojusznika [40000303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 아군인 경우, 체력 5 회복
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target is an ally, heal 5 HP
   PL: [OnSucceedAttack] jeżeli cel jest sojusznikiem, przywraca 5 HP
304. [Umiejętność sojusznika [40000303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상이 적군인 경우, [Burst] 1 부여
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 302 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Umiejętność sojusznika [40000303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상이 아군인 경우, 체력 5 회복
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Umiejętność sojusznika [40000303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상이 적군인 경우, [Burst] 1 부여
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 302 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Umiejętność sojusznika [40000303] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상이 아군인 경우, 체력 5 회복
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000303].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Umiejętność sojusznika [40000304] (ulepszenie 1) — nazwa] 그 기술을 사용하는 수 밖에!
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000304].levelList[level=1].name
   limit: do 60 znaków
   EN: Looks Like I'll Have to Use This Power!
   PL: Looks Like I'll Have to Use This Power!
309. [Umiejętność sojusznika [40000304] (ulepszenie 1) — opis] [StartBattle] [ChasingArcana]를 1 얻음\n[StartBattle] 보호막 50 얻음\n[StartBattle] 다음 턴에 [Aggro]를 20 획득함
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000304].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [ChasingArcana], [Aggro]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ChasingArcana] = 영창 - 아르카나 슬레이브 / Chanting - Arcana Slave; [Aggro] = 도발치 / Aggro
   EN: [StartBattle] Gain 1 [ChasingArcana]\n[StartBattle] Gain 50 Shield\n[StartBattle] Gain 20 [Aggro] next turn
   PL: [StartBattle] zyskuje 1 [ChasingArcana]\n[StartBattle] zyskuje 50 Tarczy\n[StartBattle] zyskuje 20 [Aggro] w następnej turze
310. [Umiejętność sojusznika [40000305] (ulepszenie 1) — nazwa] 영창 - 아르카나 슬레이브
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000305].levelList[level=1].name
   limit: do 40 znaków
   EN: Chanting - Arcana Slave
   PL: Chanting - Arcana Slave
311. [Umiejętność sojusznika [40000305] (ulepszenie 1) — opis] [StartBattle] 보호막 50 얻음\n[StartBattle] 다음 턴에 [Aggro]를 20 획득함\n[EndBattle] 남은 보호막 수치가 없다면, 퇴각함
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000305].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Aggro], [EndBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Aggro] = 도발치 / Aggro; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [StartBattle] Gain 50 Shield\n[StartBattle] Gain 20 [Aggro] next turn\n[EndBattle] At 0 Shield HP, Retreats
   PL: [StartBattle] zyskuje 50 Tarczy\n[StartBattle] zyskuje 20 [Aggro] w następnej turze\n[EndBattle] gdy nie ma pozostałej Tarczy, wycofuje się
312. [Umiejętność sojusznika [40000306] (ulepszenie 1) — nazwa] 아르카나 슬레이브
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000306].levelList[level=1].name
   limit: do 40 znaków
   EN: ARCANA SLAVE
   PL: ARCANA SLAVE
313. [Umiejętność sojusznika [40000306] (ulepszenie 1) — opis] [CantDuel]\n잊혀진 기사의 검에게 피해를 주지 않음\n[WornOutKnight]가 있는 적 적중시 턴 종료\n[EndBattle] [UsedTooMuchPower] 얻음
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000306].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WornOutKnight], [EndBattle], [UsedTooMuchPower], [TabExplain]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WornOutKnight] = 닳디 닳은 기사 / Weathered Knight; [EndBattle] = [턴 종료 시] / [Turn End]; [UsedTooMuchPower] = 힘을 너무 많이 썼나봐 / I used too much power
   EN: [CantDuel]\nDoes not deal damage against Sword of a Forgotten Knight[TabExplain]\nEnds Turn when hitting enemies with [WornOutKnight]\n[EndBattle] Gain [UsedTooMuchPower]
   PL: [CantDuel]\nnie zadaje obrażeń Mieczowi Zapomnianego Rycerza[TabExplain]\nkończy turę po trafieniu wroga z [WornOutKnight]\n[EndBattle] zyskuje [UsedTooMuchPower]
314. [Umiejętność sojusznika [40000306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 체력을 현재 체력의 (100 - ([CollapsedPride] 수치 x 33))% 로 만듦
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [CollapsedPride]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CollapsedPride] = 무너져 내린 긍지 / Crumbled Pride
   EN: [OnSucceedAttack] Reduce target's HP to (100 - ([CollapsedPride] Stack x 33))%
   PL: [OnSucceedAttack] ustawia HP celu na (100 - (Stos [CollapsedPride] x 33))% aktualnego HP
315. [Umiejętność sojusznika [40000307] (ulepszenie 1) — nazwa] 아르카나 슬레이브
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000307].levelList[level=1].name
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Umiejętność sojusznika [40000307] (ulepszenie 1) — opis] [CantDuel]\n코인 효과로만 피해를 줌\n마음을 부수는 검, 마음을 찢는 검, 마음을 꿰뚫는 검에게 피해를 주지 않음\n[WornOutKnight]가 있는 체력 600 이하의 적 적중시 턴 종료\n[EndBattle] [UsedTooMuchPower] 얻음
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000307].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WornOutKnight], [EndBattle], [UsedTooMuchPower]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WornOutKnight] = 닳디 닳은 기사 / Weathered Knight; [EndBattle] = [턴 종료 시] / [Turn End]; [UsedTooMuchPower] = 힘을 너무 많이 썼나봐 / I used too much power
   EN: [CantDuel]\nDeals damage only with Coin effects\nDoes not deal damage against Heart-breaking Sword, Heart-tearing Sword, and Heart-piercing Sword\nEnds Turn when hitting enemies that has [WornOutKnight] and 600- HP\n[EndBattle] Gain [UsedTooMuchPower]
   PL: [CantDuel]\nzadaje obrażenia wyłącznie efektami Monet\nnie zadaje obrażeń Mieczowi Łamiącemu Serce, Mieczowi Rozdzierającemu Serce ani Mieczowi Przebijającemu Serce\nkończy turę po trafieniu wroga z [WornOutKnight] i HP 600 lub mniej\n[EndBattle] zyskuje [UsedTooMuchPower]
317. [Umiejętność sojusznika [40000307] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] ([CollapsedPride] 수치 x 200)만큼 고정 피해를 줌
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000307].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [CollapsedPride]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CollapsedPride] = 무너져 내린 긍지 / Crumbled Pride
   EN: [OnSucceedAttack] Deal ([CollapsedPride] x 200) fixed damage
   PL: [OnSucceedAttack] zadaje (Stos [CollapsedPride] x 200) obrażeń stałych
318. [Umiejętność sojusznika [40000308] (ulepszenie 1) — nazwa] 그 기술을 사용하는 수 밖에!
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000308].levelList[level=1].name
   (powtórzenie elementu 308 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [Umiejętność sojusznika [40000308] (ulepszenie 1) — opis] [StartBattle] [ChasingArcanahard]를 1 얻음\n[StartBattle] 보호막 50 얻음\n[StartBattle] 다음 턴에 [Aggro]를 20 획득함
   źródło: Skills_Assist-walpu6.json :: dataList[id=40000308].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [ChasingArcanahard], [Aggro]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ChasingArcanahard] = 영창 - 아르카나 슬레이브 / Chanting - Arcana Slave; [Aggro] = 도발치 / Aggro
   EN: [StartBattle] Gain 1 [ChasingArcanahard]\n[StartBattle] Gain 50 Shield\n[StartBattle] Gain 20 [Aggro] next turn
   PL: [StartBattle] zyskuje 1 [ChasingArcanahard]\n[StartBattle] zyskuje 50 Tarczy\n[StartBattle] zyskuje 20 [Aggro] w następnej turze

## Umiejętności jednostek wsparcia — Skills_Assist
- plik gry: `Skills_Assist.json`

320. [Umiejętność sojusznika [40000101] (ulepszenie 1) — nazwa] 적격
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=1].name
   limit: do 40 znaków
   EN: Crimson Strike
   PL: Crimson Strike
321. [Umiejętność sojusznika [40000101] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 합 위력 +1\n[WhenUse] 대상의 [Burst] 3당, 기본 위력 +1 (최대 2)
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 5+ types of negative effects, Clash Power +1\n[WhenUse] Base Power +1 for every 3 [Burst] on target (max 2)
   PL: [WhenUse] jeżeli cel ma 5+ rodzajów negatywnych efektów, Moc Starcia +1\n[WhenUse] Moc Bazowa +1 za każde 3 [Burst] celu (maks. 2)
322. [Umiejętność sojusznika [40000101] (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=40000101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Umiejętność sojusznika [40000101] (ulepszenia 1–5) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=40000101].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=40000101].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=40000101].levelList[level=4].coinlist[#0].coindescs[#1].desc ; dataList[id=40000101].levelList[level=5].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [AttackUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttackHead] Gain 1 [AttackUp] next turn
   PL: [OnSucceedAttackHead] zyskuje 1 [AttackUp] w następnej turze
324. [Umiejętność sojusznika [40000101] (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=40000101].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Umiejętność sojusznika [40000101] (ulepszenia 1–5) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=40000101].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=40000101].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=40000101].levelList[level=4].coinlist[#1].coindescs[#1].desc ; dataList[id=40000101].levelList[level=5].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 323 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [Umiejętność sojusznika [40000101] (ulepszenie 2) — nazwa] 적격 2형 - 파(破)
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=2].name
   limit: do 60 znaków
   EN: Crimson Strike Second Form - Rupture (破)
   PL: Crimson Strike Second Form - Rupture (破)
327. [Umiejętność sojusznika [40000101] (ulepszenie 2) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 합 위력 +1\n[WhenUse] 대상의 [Burst] 3당, 기본 위력 +1 (최대 2)\n[WhenUse] 대상의 [Burst] 6당, 코인 위력 +1 (최대 2)
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=2].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 5+ types of negative effects, Clash Power +1\n[WhenUse] Base Power +1 for every 3 [Burst] on target (max 2)\n[WhenUse] Coin Power +1 for every 6 [Burst] on target (max 2)
   PL: [WhenUse] jeżeli cel ma 5+ rodzajów negatywnych efektów, Moc Starcia +1\n[WhenUse] Moc Bazowa +1 za każde 3 [Burst] celu (maks. 2)\n[WhenUse] Moc Monety +1 za każde 6 [Burst] celu (maks. 2)
328. [Umiejętność sojusznika [40000101] (ulepszenie 3) — nazwa] 적격 3형 - 강(强)
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=3].name
   limit: do 60 znaków
   EN: Crimson Strike Third Form - Might (强)
   PL: Crimson Strike Third Form - Might (强)
329. [Umiejętność sojusznika [40000101] (ulepszenie 3) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 합 위력 +2\n[WhenUse] 대상의 [Burst] 3당, 기본 위력 +1 (최대 2)\n[WhenUse] 대상의 [Burst] 6당, 코인 위력 +1 (최대 2)
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=3].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 5+ types of negative effects, Clash Power +2\n[WhenUse] Base Power +1 for every 3 [Burst] on target (max 2)\n[WhenUse] Coin Power +1 for every 6 [Burst] on target (max 2)
   PL: [WhenUse] jeżeli cel ma 5+ rodzajów negatywnych efektów, Moc Starcia +2\n[WhenUse] Moc Bazowa +1 za każde 3 [Burst] celu (maks. 2)\n[WhenUse] Moc Monety +1 za każde 6 [Burst] celu (maks. 2)
330. [Umiejętność sojusznika [40000101] (ulepszenia 3–5) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여,[Burst] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=40000101].levelList[level=4].coinlist[#0].coindescs[#0].desc ; dataList[id=40000101].levelList[level=5].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst] and +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 2 [Burst] i zwiększa Licznik [Burst] o 2
331. [Umiejętność sojusznika [40000101] (ulepszenia 3–5) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여,[Burst] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=40000101].levelList[level=4].coinlist[#1].coindescs[#0].desc ; dataList[id=40000101].levelList[level=5].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 330 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Umiejętność sojusznika [40000101] (ulepszenie 4) — nazwa] 적격 4형 - 속(束)
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=4].name
   limit: do 60 znaków
   EN: Crimson Strike Fourth Form - Binding (束)
   PL: Crimson Strike Fourth Form - Binding (束)
333. [Umiejętność sojusznika [40000101] (ulepszenie 4) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 합 위력 +2\n[WhenUse] 대상의 [Burst] 3당, 기본 위력 +1 (최대 2)\n[WhenUse] 대상의 [Burst] 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 다음 턴에 [Agility] 3 얻음 (턴 당 1회)
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=4].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Agility] = 신속 / Haste
   EN: [WhenUse] If target has 5+ types of negative effects, Clash Power +2\n[WhenUse] Base Power +1 for every 3 [Burst] on target (max 2)\n[WhenUse] Coin Power +1 for every 6 [Burst] on target (max 2)\n[WhenUse] Gain 3 [Agility] next turn (once per turn)
   PL: [WhenUse] jeżeli cel ma 5+ rodzajów negatywnych efektów, Moc Starcia +2\n[WhenUse] Moc Bazowa +1 za każde 3 [Burst] celu (maks. 2)\n[WhenUse] Moc Monety +1 za każde 6 [Burst] celu (maks. 2)\n[WhenUse] zyskuje 3 [Agility] w następnej turze (1 raz na turę)
334. [Umiejętność sojusznika [40000101] (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3 부여
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 3 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 3 [Binding] w następnej turze
335. [Umiejętność sojusznika [40000101] (ulepszenie 5) — nazwa] 적격 5형 - 진(進)
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=5].name
   limit: do 60 znaków
   EN: Crimson Strike Fifth Form - March (進)
   PL: Crimson Strike Fifth Form - March (進)
336. [Umiejętność sojusznika [40000101] (ulepszenie 5) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 합 위력 +2\n[WhenUse] 대상의 [Burst] 3당, 기본 위력 +1 (최대 2)\n[WhenUse] 대상의 [Burst] 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 다음 턴에 [Agility] 3 얻음 (턴 당 1회)\n[WhenUse] [Breath] 3 얻음,[Breath] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=5].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Agility], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Agility] = 신속 / Haste; [Breath] = 호흡 / Poise
   EN: [WhenUse] If target has 5+ types of negative effects, Clash Power +2\n[WhenUse] Base Power +1 for every 3 [Burst] on target (max 2)\n[WhenUse] Coin Power +1 for every 6 [Burst] on target (max 2)\n[WhenUse] Gain 3 [Agility] next turn (once per turn)\n[WhenUse] Gain 3 [Breath] aind +2 [Breath] Count
   PL: [WhenUse] jeżeli cel ma 5+ rodzajów negatywnych efektów, Moc Starcia +2\n[WhenUse] Moc Bazowa +1 za każde 3 [Burst] celu (maks. 2)\n[WhenUse] Moc Monety +1 za każde 6 [Burst] celu (maks. 2)\n[WhenUse] zyskuje 3 [Agility] w następnej turze (1 raz na turę)\n[WhenUse] zyskuje 3 [Breath] i 2 Licznika [Breath]
337. [Umiejętność sojusznika [40000101] (ulepszenie 5) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=5].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Burst] = 파열 / Rupture
   EN: [CriticalOnSucceedAttack] Inflict 2 [Burst]
   PL: [CriticalOnSucceedAttack] nakłada 2 [Burst]
338. [Umiejętność sojusznika [40000101] (ulepszenie 5) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Binding] 3 부여
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=5].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 3 [Binding]
   PL: [OnSucceedAttack] nakłada 3 [Binding]
339. [Umiejętność sojusznika [40000101] (ulepszenie 5) — moneta 2, efekt 4 — opis] [CriticalOnSucceedAttack] 이 코인 재사용 (최대 2회)
   źródło: Skills_Assist.json :: dataList[id=40000101].levelList[level=5].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Reuse this Coin (2 times max)
   PL: [CriticalOnSucceedAttack] używa tej Monety ponownie (maks. 2 razy)
340. [Umiejętność sojusznika [40000102] (ulepszenie 1) — nazwa] 적봉
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=1].name
   limit: do 40 znaków
   EN: Crimson Phoenix
   PL: Crimson Phoenix
341. [Umiejętność sojusznika [40000102] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Burst] 6당, 코인 위력 +1 (최대 2)
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 5+ types of negative effects, Coin Power +1\n[WhenUse] Coin Power +1 for every 6 [Burst] on target (max 2)
   PL: [WhenUse] jeżeli cel ma 5+ rodzajów negatywnych efektów, Moc Monety +1\n[WhenUse] Moc Monety +1 za każde 6 [Burst] celu (maks. 2)
342. [Umiejętność sojusznika [40000102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Umiejętność sojusznika [40000102] (ulepszenia 1–2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [DefenseDown] 3 부여
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=40000102].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 3 [DefenseDown]
   PL: [OnSucceedAttack] nakłada 3 [DefenseDown]
344. [Umiejętność sojusznika [40000102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Umiejętność sojusznika [40000102] (ulepszenia 1–2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [AttackUp] 3 얻음
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=40000102].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttack] Gain 3 [AttackUp] next turn
   PL: [OnSucceedAttack] zyskuje 3 [AttackUp] w następnej turze
346. [Umiejętność sojusznika [40000102] (ulepszenia 1–2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 1 증가. 대상의 [Burst]만큼 [Breath] 얻음 (최대 5)
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=40000102].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count. Gain [Breath] equal to [Burst] on target (max 5)
   PL: [OnSucceedAttack] zyskuje 1 Licznika [Breath]. Zyskuje [Breath] równe wartości [Burst] celu (maks. 5)
347. [Umiejętność sojusznika [40000102] (ulepszenia 1–2) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 위력 3 얻음. 대상의 [Burst] 횟수만큼 다음 턴에 [Breath] 횟수 증가 (최대 2)
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=40000102].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 3 [Breath] next turn. Gain [Breath] Count equal to [Burst] Count on target next turn (max 2)
   PL: [OnSucceedAttackHead] zyskuje 3 [Breath] w następnej turze. Zyskuje Licznik [Breath] w następnej turze równy Licznikowi [Burst] celu (maks. 2)
348. [Umiejętność sojusznika [40000102] (ulepszenia 1–5) — moneta 4, efekt 1 — opis] 크리티컬 피해량 +50%
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=40000102].levelList[level=2].coinlist[#3].coindescs[#0].desc ; dataList[id=40000102].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=40000102].levelList[level=4].coinlist[#3].coindescs[#0].desc ; dataList[id=40000102].levelList[level=5].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +50% Damage on Critical Hit
   PL: +50% obrażeń krytycznych
349. [Umiejętność sojusznika [40000102] (ulepszenia 1–5) — moneta 4, efekt 2 — opis] [CriticalEnemyTargetKillFail] [Burst] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=1].coinlist[#3].coindescs[#1].desc ; dataList[id=40000102].levelList[level=2].coinlist[#3].coindescs[#1].desc ; dataList[id=40000102].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=40000102].levelList[level=4].coinlist[#3].coindescs[#1].desc ; dataList[id=40000102].levelList[level=5].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalEnemyTargetKillFail], [Burst]
   znaczenie tagów: [CriticalEnemyTargetKillFail] = [크리티컬 적 처치 실패 시] / [On Crit Kill Fail Against Enemy]; [Burst] = 파열 / Rupture
   EN: [CriticalEnemyTargetKillFail] Inflict +2 [Burst] Count
   PL: [CriticalEnemyTargetKillFail] zwiększa Licznik [Burst] o 2
350. [Umiejętność sojusznika [40000102] (ulepszenia 1–5) — moneta 4, efekt 3 — opis] [CriticalEnemyTargetKill] 다음 턴에 [AttackUp] 3 얻음
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=1].coinlist[#3].coindescs[#2].desc ; dataList[id=40000102].levelList[level=2].coinlist[#3].coindescs[#2].desc ; dataList[id=40000102].levelList[level=3].coinlist[#3].coindescs[#2].desc ; dataList[id=40000102].levelList[level=4].coinlist[#3].coindescs[#2].desc ; dataList[id=40000102].levelList[level=5].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalEnemyTargetKill], [AttackUp]
   znaczenie tagów: [CriticalEnemyTargetKill] = [크리티컬 적 처치 시] / [On Crit Kill Against Enemy]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CriticalEnemyTargetKill] Gain 3 [AttackUp] next turn
   PL: [CriticalEnemyTargetKill] zyskuje 3 [AttackUp] w następnej turze
351. [Umiejętność sojusznika [40000102] (ulepszenie 2) — nazwa] 적봉 제2형 - 파(破)
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=2].name
   limit: do 60 znaków
   EN: Crimson Phoenix Second Form - Rupture (破)
   PL: Crimson Phoenix Second Form - Rupture (破)
352. [Umiejętność sojusznika [40000102] (ulepszenia 2–3) — opis] [WhenUse] 대상의 부정적인 효과가 4개 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Burst] 6당, 코인 위력 +1 (최대 2)
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=2].desc ; dataList[id=40000102].levelList[level=3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 4+ types of negative effects, Coin Power +1\n[WhenUse] Coin Power +1 for every 6 [Burst] on target (max 2)
   PL: [WhenUse] jeżeli cel ma 4+ rodzajów negatywnych efektów, Moc Monety +1\n[WhenUse] Moc Monety +1 za każde 6 [Burst] celu (maks. 2)
353. [Umiejętność sojusznika [40000102] (ulepszenia 2–5) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=40000102].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=40000102].levelList[level=4].coinlist[#0].coindescs[#0].desc ; dataList[id=40000102].levelList[level=5].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Umiejętność sojusznika [40000102] (ulepszenia 2–5) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=40000102].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=40000102].levelList[level=4].coinlist[#1].coindescs[#0].desc ; dataList[id=40000102].levelList[level=5].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Umiejętność sojusznika [40000102] (ulepszenie 3) — nazwa] 적봉 제3형 - 염(炎)
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=3].name
   limit: do 60 znaków
   EN: Crimson Phoenix Third Form - Blaze (炎)
   PL: Crimson Phoenix Third Form - Blaze (炎)
356. [Umiejętność sojusznika [40000102] (ulepszenia 3–5) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=40000102].levelList[level=4].coinlist[#0].coindescs[#1].desc ; dataList[id=40000102].levelList[level=5].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [Umiejętność sojusznika [40000102] (ulepszenia 3–5) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [DefenseDown] 3 부여
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=40000102].levelList[level=4].coinlist[#0].coindescs[#2].desc ; dataList[id=40000102].levelList[level=5].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Umiejętność sojusznika [40000102] (ulepszenia 3–5) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=40000102].levelList[level=4].coinlist[#1].coindescs[#1].desc ; dataList[id=40000102].levelList[level=5].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Umiejętność sojusznika [40000102] (ulepszenia 3–5) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [AttackUp] 3 얻음
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=40000102].levelList[level=4].coinlist[#1].coindescs[#2].desc ; dataList[id=40000102].levelList[level=5].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 345 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Umiejętność sojusznika [40000102] (ulepszenia 3–5) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Burst]과 [Combustion]의 합 만큼 [Breath] 얻음 (최대 10)
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=40000102].levelList[level=4].coinlist[#2].coindescs[#0].desc ; dataList[id=40000102].levelList[level=5].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [Combustion], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Combustion] = 화상 / Burn; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain [Breath] equal to ([Burst] + [Combustion]) on target (max 10)
   PL: [OnSucceedAttack] zyskuje [Breath] równe ([Burst] + [Combustion]) celu (maks. 10)
361. [Umiejętność sojusznika [40000102] (ulepszenia 3–5) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst] 횟수와 [Combustion] 횟수의 합 만큼 [Breath] 횟수 증가 (최대 5)
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=40000102].levelList[level=4].coinlist[#2].coindescs[#1].desc ; dataList[id=40000102].levelList[level=5].coinlist[#2].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [Combustion], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Combustion] = 화상 / Burn; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain [Breath] Count equal to ([Burst] Count + [Combustion] Count) on target (max 5)
   PL: [OnSucceedAttack] zwiększa Licznik [Breath] o liczbę równą (Licznik [Burst] + Licznik [Combustion]) celu (maks. 5)
362. [Umiejętność sojusznika [40000102] (ulepszenie 4) — nazwa] 적봉 제4형 - 기(氣)
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=4].name
   limit: do 50 znaków
   EN: Crimson Phoenix Fourth Form - Qi (氣)
   PL: Crimson Phoenix Fourth Form - Qi (氣)
363. [Umiejętność sojusznika [40000102] (ulepszenia 4–5) — opis] [WhenUse] 대상의 부정적인 효과가 4개 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Burst] 3당, 코인 위력 +1 (최대 2)\n[WhenUse] [Breath] 3 얻음,[Breath] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=4].desc ; dataList[id=40000102].levelList[level=5].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [WhenUse] If target has 4+ types of negative effects, Coin Power +1\n[WhenUse] Coin Power +1 for every 3 [Burst] on target (max 2)\n[WhenUse] Gain 3 [Breath] and +2 [Breath] Count
   PL: [WhenUse] jeżeli cel ma 4+ rodzajów negatywnych efektów, Moc Monety +1\n[WhenUse] Moc Monety +1 za każde 3 [Burst] celu (maks. 2)\n[WhenUse] zyskuje 3 [Breath] i 2 Licznika [Breath]
364. [Umiejętność sojusznika [40000102] (ulepszenia 4–5) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=4].coinlist[#0].coindescs[#3].desc ; dataList[id=40000102].levelList[level=5].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Combustion]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Combustion] = 화상 / Burn
   EN: [CriticalOnSucceedAttack] Inflict 3 [Combustion]
   PL: [CriticalOnSucceedAttack] nakłada 3 [Combustion]
365. [Umiejętność sojusznika [40000102] (ulepszenia 4–5) — moneta 2, efekt 4 — opis] [CriticalOnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=4].coinlist[#1].coindescs[#3].desc ; dataList[id=40000102].levelList[level=5].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Umiejętność sojusznika [40000102] (ulepszenia 4–5) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] [Vulnerable] 2 부여
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=4].coinlist[#2].coindescs[#2].desc ; dataList[id=40000102].levelList[level=5].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Vulnerable] = 취약 / Fragile
   EN: [CriticalOnSucceedAttack] Inflict 2 [Vulnerable]
   PL: [CriticalOnSucceedAttack] nakłada 2 [Vulnerable]
367. [Umiejętność sojusznika [40000102] (ulepszenie 5) — nazwa] 적봉 제5형 - 익(翼)
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=5].name
   limit: do 60 znaków
   EN: Crimson Phoenix Fifth Form - Wings (翼)
   PL: Crimson Phoenix Fifth Form - Wings (翼)
368. [Umiejętność sojusznika [40000102] (ulepszenie 5) — moneta 4, efekt 4 — opis] [CriticalEnemyTargetKillFail] 대상에게 적참 사용
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=5].coinlist[#3].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalEnemyTargetKillFail]
   znaczenie tagów: [CriticalEnemyTargetKillFail] = [크리티컬 적 처치 실패 시] / [On Crit Kill Fail Against Enemy]
   EN: [CriticalEnemyTargetKillFail] Use Crimson Cleave against the target
   PL: [CriticalEnemyTargetKillFail] używa Crimson Cleave na celu
369. [Umiejętność sojusznika [40000102] (ulepszenie 5) — moneta 4, efekt 5 — opis] [CriticalEnemyTargetKill] 무작위 대상에게 적참 사용
   źródło: Skills_Assist.json :: dataList[id=40000102].levelList[level=5].coinlist[#3].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalEnemyTargetKill]
   znaczenie tagów: [CriticalEnemyTargetKill] = [크리티컬 적 처치 시] / [On Crit Kill Against Enemy]
   EN: [CriticalEnemyTargetKill] Use Crimson Cleave against a random enemy
   PL: [CriticalEnemyTargetKill] używa Crimson Cleave na losowym wrogu
370. [Umiejętność sojusznika [40000103] (ulepszenie 1) — nazwa] 적춘
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=1].name
   limit: do 40 znaków
   EN: Crimson Spring
   PL: Crimson Spring
371. [Umiejętność sojusznika [40000103] (ulepszenie 1) — opis] [BeforeAttack] 대상의 부정적인 효과 4개당 공격 가중치 +1 (최대 2)\n[WhenUse] 대상의 부정적인 효과가 5개 이상이면, 기본 위력 +5\n[WhenUse] 대상의 ([Burst] + [Burst] 횟수)의 합이 15 이상이면, 코인 위력 +5\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [BeforeAttack] Gain +1 Atk Weight for every 4 types of negative effects on target (max 2)\n[WhenUse] If target has 5+ types of negative effects, Base Power +5\n[WhenUse] If target has 15+ ([Burst] + [Burst] Count), Coin Power +5\n[WinDuel] Inflict +2 [Burst] Count
   PL: [BeforeAttack] Waga Ataku +1 za każde 4 rodzaje negatywnych efektów celu (maks. 2)\n[WhenUse] jeżeli cel ma 5+ rodzajów negatywnych efektów, Moc Bazowa +5\n[WhenUse] jeżeli cel ma 15+ ([Burst] + Licznik [Burst]), Moc Monety +5\n[WinDuel] zwiększa Licznik [Burst] o 2
372. [Umiejętność sojusznika [40000103] (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 7 부여
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=40000103].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 7 Bleed
   PL: [OnSucceedAttack] nakłada 7 Krwawienia
373. [Umiejętność sojusznika [40000103] (ulepszenia 1–2) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +200%
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=40000103].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: Deal +200% Damage on Critical Hit
   PL: +200% obrażeń krytycznych
374. [Umiejętność sojusznika [40000103] (ulepszenia 1–2) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=40000103].levelList[level=2].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict +3 Bleed Count
   PL: [CriticalOnSucceedAttack] zwiększa Licznik Krwawienia o 3
375. [Umiejętność sojusznika [40000103] (ulepszenia 1–2) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] [Breath] 2 얻음. [Breath] 횟수 1 증가
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=1].coinlist[#0].coindescs[#3].desc ; dataList[id=40000103].levelList[level=2].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain 2 [Breath] and +1 [Breath] Count
   PL: [CriticalOnSucceedAttack] zyskuje 2 [Breath] i 1 Licznika [Breath]
376. [Umiejętność sojusznika [40000103] (ulepszenie 2) — nazwa] 적춘 제2형 - 열(熱)
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=2].name
   limit: do 60 znaków
   EN: Crimson Spring Second Form - Passion (熱)
   PL: Crimson Spring Second Form - Passion (熱)
377. [Umiejętność sojusznika [40000103] (ulepszenia 2–3) — opis] [BeforeAttack] 대상의 부정적인 효과 3개당 공격 가중치 +1 (최대 2)\n[WhenUse] 대상의 부정적인 효과가 5개 이상이면, 기본 위력 +5\n[WhenUse] 대상의 ([Burst] + [Burst] 횟수)의 합 3당, 코인 위력 +1(최대 5)\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=2].desc ; dataList[id=40000103].levelList[level=3].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [BeforeAttack] Gain +1 Atk Weight for every 3 types of negative effects on target (max 2)\n[WhenUse] If target has 5+ types of negative effects, Base Power +5\n[WhenUse] Coin Power +1 for every 3 ([Burst] + [Burst] Count on target) (max 5)\n[WinDuel] Inflict +2 [Burst] Count
   PL: [BeforeAttack] Waga Ataku +1 za każde 3 rodzaje negatywnych efektów celu (maks. 2)\n[WhenUse] jeżeli cel ma 5+ rodzajów negatywnych efektów, Moc Bazowa +5\n[WhenUse] Moc Monety +1 za każde 3 ([Burst] + Licznik [Burst] celu) (maks. 5)\n[WinDuel] zwiększa Licznik [Burst] o 2
378. [Umiejętność sojusznika [40000103] (ulepszenie 3) — nazwa] 적춘 제3형 - 참(斬)
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=3].name
   limit: do 60 znaków
   EN: Crimson Spring Third Form - Decapitation (斬)
   PL: Crimson Spring Third Form - Decapitation (斬)
379. [Umiejętność sojusznika [40000103] (ulepszenia 3–5) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=40000103].levelList[level=4].coinlist[#0].coindescs[#0].desc ; dataList[id=40000103].levelList[level=5].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL: [OnSucceedAttack] nakłada 3 Krwawienia
380. [Umiejętność sojusznika [40000103] (ulepszenia 3–5) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 출혈 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=40000103].levelList[level=4].coinlist[#0].coindescs[#1].desc ; dataList[id=40000103].levelList[level=5].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict +2 Bleed Count
   PL: [CriticalOnSucceedAttack] zwiększa Licznik Krwawienia o 2
381. [Umiejętność sojusznika [40000103] (ulepszenia 3–5) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] [Breath] 2 얻음. [Breath] 횟수 1 증가
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=3].coinlist[#0].coindescs[#2].desc ; dataList[id=40000103].levelList[level=4].coinlist[#0].coindescs[#2].desc ; dataList[id=40000103].levelList[level=5].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Umiejętność sojusznika [40000103] (ulepszenia 3–5) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 7 부여
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=40000103].levelList[level=4].coinlist[#1].coindescs[#0].desc ; dataList[id=40000103].levelList[level=5].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 372 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Umiejętność sojusznika [40000103] (ulepszenia 3–5) — moneta 2, efekt 2 — opis] 크리티컬 피해량 +200%
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=40000103].levelList[level=4].coinlist[#1].coindescs[#1].desc ; dataList[id=40000103].levelList[level=5].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Umiejętność sojusznika [40000103] (ulepszenia 3–5) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=40000103].levelList[level=4].coinlist[#1].coindescs[#2].desc ; dataList[id=40000103].levelList[level=5].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 374 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Umiejętność sojusznika [40000103] (ulepszenia 3–5) — moneta 2, efekt 4 — opis] [CriticalOnSucceedAttack] [Breath] 2 얻음. [Breath] 횟수 1 증가
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=3].coinlist[#1].coindescs[#3].desc ; dataList[id=40000103].levelList[level=4].coinlist[#1].coindescs[#3].desc ; dataList[id=40000103].levelList[level=5].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Umiejętność sojusznika [40000103] (ulepszenie 4) — nazwa] 적춘 제4형 - 순(巡)
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=4].name
   limit: do 60 znaków
   EN: Crimson Spring Fourth Form - Flow (巡)
   PL: Crimson Spring Fourth Form - Flow (巡)
387. [Umiejętność sojusznika [40000103] (ulepszenia 4–5) — opis] [BeforeAttack] 대상의 부정적인 효과 3개당 공격 가중치 +1 (최대 2)\n[WhenUse] 대상의 부정적인 효과가 5개 이상이면, 기본 위력 +5\n[WhenUse] 대상의 ([Burst] + [Burst] 횟수)의 합 3당, 코인 위력 +1(최대 5)\n[WinDuel] [Burst] 횟수 2 증가\n[WhenUse] [Breath] 5 얻음,[Breath] 횟수 2 증가
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=4].desc ; dataList[id=40000103].levelList[level=5].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [WhenUse], [Burst], [WinDuel], [Breath]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [BeforeAttack] Gain +1 Atk Weight for every 3 types of negative effects on target (max 2)\n[WhenUse] If target has 5+ types of negative effects, Base Power +5\n[WhenUse] Coin Power +1 for every 3 ([Burst] + [Burst] Count on target) (max 5)\n[WinDuel] Inflict +2 [Burst] Count\n[WhenUse] Gain 5 [Breath] and +2 [Breath] Count
   PL: [BeforeAttack] Waga Ataku +1 za każde 3 rodzaje negatywnych efektów celu (maks. 2)\n[WhenUse] jeżeli cel ma 5+ rodzajów negatywnych efektów, Moc Bazowa +5\n[WhenUse] Moc Monety +1 za każde 3 ([Burst] + Licznik [Burst] celu) (maks. 5)\n[WinDuel] zwiększa Licznik [Burst] o 2\n[WhenUse] zyskuje 5 [Breath] i 2 Licznika [Breath]
388. [Umiejętność sojusznika [40000103] (ulepszenie 5) — nazwa] 적춘 제5형 - 花(화)
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=5].name
   limit: do 60 znaków
   EN: Crimson Spring Fifth Form - 花 (Blossom)
   PL: Crimson Spring Fifth Form - 花 (Blossom)
389. [Umiejętność sojusznika [40000103] (ulepszenie 5) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 부정적인 효과 1개당 피해량 +10% (최대 50%)
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=5].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal +10% damage for every type of negative effect on target (max 50%)
   PL: [OnSucceedAttack] zadaje +10% obrażeń za każdy rodzaj negatywnego efektu celu (maks. 50%)
390. [Umiejętność sojusznika [40000103] (ulepszenie 5) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +50%
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=5].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Umiejętność sojusznika [40000103] (ulepszenie 5) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 3 얻음 (턴 당 1회)
   źródło: Skills_Assist.json :: dataList[id=40000103].levelList[level=5].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 3 [Agility] next turn (once per turn)
   PL: [OnSucceedAttack] zyskuje 3 [Agility] w następnej turze (1 raz na turę)
392. [Umiejętność sojusznika [40000104] (ulepszenia 1–3) — nazwa] 수회
   źródło: Skills_Assist.json :: dataList[id=40000104].levelList[level=1].name ; dataList[id=40000104].levelList[level=2].name ; dataList[id=40000104].levelList[level=3].name
   limit: do 40 znaków
   EN: Adept Evasion
   PL: Adept Evasion
393. [Umiejętność sojusznika [40000104] (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 [Breath] 1 얻음. (스킬 당 최대 3회)
   źródło: Skills_Assist.json :: dataList[id=40000104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Breath]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [OnSucceedEvade] Gain 1 [Breath] next turn. (3 times per Skill)
   PL: [OnSucceedEvade] zyskuje 1 [Breath] w następnej turze. (maks. 3 razy na Umiejętność)
394. [Umiejętność sojusznika [40000104] (ulepszenie 2) — opis] [OnSucceedEvade] 다음 턴에 [Breath] 3 얻음. (스킬 당 최대 2회)
   źródło: Skills_Assist.json :: dataList[id=40000104].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Breath]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [OnSucceedEvade] Gain 3 [Breath] next turn. (2 times per Skill)
   PL: [OnSucceedEvade] zyskuje 3 [Breath] w następnej turze. (maks. 2 razy na Umiejętność)
395. [Umiejętność sojusznika [40000104] (ulepszenie 3) — opis] [WhenUse] 대상의 부정적인 효과 2개 당 기본 위력 +2 (최대 10)\n[OnSucceedEvade] 다음 턴에 [Breath] 3 얻음. (스킬 당 최대 2회)
   źródło: Skills_Assist.json :: dataList[id=40000104].levelList[level=3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [OnSucceedEvade], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Base Power +2 for every 2 types of negative effect on target (max 10)\n[OnSucceedEvade] Gain 3 [Breath] next turn. (2 times per Skill)
   PL: [WhenUse] Moc Bazowa +2 za każde 2 rodzaje negatywnych efektów celu (maks. 10)\n[OnSucceedEvade] zyskuje 3 [Breath] w następnej turze. (maks. 2 razy na Umiejętność)
396. [Umiejętność sojusznika [40000104] (ulepszenie 4) — nazwa] 수회유환
   źródło: Skills_Assist.json :: dataList[id=40000104].levelList[level=4].name
   limit: do 50 znaków
   EN: Adept Evasion - Redirected Counter
   PL: Adept Evasion - Redirected Counter
397. [Umiejętność sojusznika [40000104] (ulepszenie 4) — opis] [WhenUse] 대상의 부정적인 효과 2개 당 기본 위력 +2 (최대 10)\n[OnSucceedEvade] 다음 턴에 [Breath] 3 얻음. (스킬 당 최대 2회)\n[OnSucceedEvade] 적참을 사용 (턴 당 1회).
   źródło: Skills_Assist.json :: dataList[id=40000104].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [OnSucceedEvade], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Base Power +2 for every 2 types of negative effect on target (max 10)\n[OnSucceedEvade] Gain 3 [Breath] next turn. (2 times per Skill)\n[OnSucceedEvade] Use Crimson Cleave (once per turn)
   PL: [WhenUse] Moc Bazowa +2 za każde 2 rodzaje negatywnych efektów celu (maks. 10)\n[OnSucceedEvade] zyskuje 3 [Breath] w następnej turze. (maks. 2 razy na Umiejętność)\n[OnSucceedEvade] używa Crimson Cleave (1 raz na turę)

## [a1c10p1] Wróg / część: Enemies-a1c10p1
- plik gry: `Enemies-a1c10p1.json`

398. [[a1c10p1] Wróg / część [91059] — nazwa] 목마른 르카키
   źródło: Enemies-a1c10p1.json :: dataList[id=91059].name
   limit: do 40 znaków
   EN: Thirsty Kaki
   PL: Thirsty Kaki
399. [[a1c10p1] Wróg / część [91060] — nazwa] 배고픈 르카키
   źródło: Enemies-a1c10p1.json :: dataList[id=91060].name
   limit: do 40 znaków
   EN: Hungry Kaki
   PL: Hungry Kaki
400. [[a1c10p1] Wróg / część [91060] — opis] 부위
   źródło: Enemies-a1c10p1.json :: dataList[id=91060].desc
   limit: do 120 znaków
   EN: Part
   PL: Część
401. [[a1c10p1] Wróg / część [1465] — nazwa] 르누아르 점원 구스타프
   źródło: Enemies-a1c10p1.json :: dataList[id=1465].name
   limit: do 50 znaków
   EN: Le Noir Sales Associate Gustave
   PL: Le Noir Sales Associate Gustave
402. [[a1c10p1] Wróg / część [1465] — opis] 1층 보스
   źródło: Enemies-a1c10p1.json :: dataList[id=1465].desc
   limit: do 120 znaków
   EN: 1F Boss
   PL: 1F Boss
403. [[a1c10p1] Wróg / część [1494] — nazwa] 르루주 점원 미모사
   źródło: Enemies-a1c10p1.json :: dataList[id=1494].name
   limit: do 50 znaków
   EN: Le Rouge Sales Associate Mimosa
   PL: Le Rouge Sales Associate Mimosa
404. [[a1c10p1] Wróg / część [1494] — opis] 1층 NPC
   źródło: Enemies-a1c10p1.json :: dataList[id=1494].desc
   limit: do 120 znaków
   EN: 1F NPC
   PL: 1F NPC
405. [[a1c10p1] Wróg / część [1480] — nazwa] 가죽 지갑
   źródło: Enemies-a1c10p1.json :: dataList[id=1480].name
   limit: do 40 znaków
   EN: Leather Wallet
   PL: Leather Wallet
406. [[a1c10p1] Wróg / część [1466] — nazwa] 리나모비블
   źródło: Enemies-a1c10p1.json :: dataList[id=1466].name
   limit: do 40 znaków
   EN: L'Inamovible
   PL: L'Inamovible
407. [[a1c10p1] Wróg / część [91066] — nazwa] 르누아르 점원[햇살]
   źródło: Enemies-a1c10p1.json :: dataList[id=91066].name
   limit: do 50 znaków
   EN: Le Noir Sales Associate [Sunshone]
   PL: Le Noir Sales Associate [Sunshone]
408. [[a1c10p1] Wróg / część [1481] — nazwa] 3층 플로어 매니저
   źródło: Enemies-a1c10p1.json :: dataList[id=1481].name
   limit: do 40 znaków
   EN: 3F Floor Manager
   PL: 3F Floor Manager
409. [[a1c10p1] Wróg / część [1484] — nazwa] 붉은 신[미생]
   źródło: Enemies-a1c10p1.json :: dataList[id=1484].name
   limit: do 50 znaków
   EN: The Crimson God [Inchoate Life]
   PL: The Crimson God [Inchoate Life]
410. [[a1c10p1] Wróg / część [148401] — nazwa] 생명줄
   źródło: Enemies-a1c10p1.json :: dataList[id=148401].name
   limit: do 40 znaków
   EN: Lifecord
   PL: Lifecord
411. [[a1c10p1] Wróg / część [148401] — opis] 붉은 신 부위
   źródło: Enemies-a1c10p1.json :: dataList[id=148401].desc
   limit: do 120 znaków
   EN: The Crimson God Part
   PL: The Crimson God Part
412. [[a1c10p1] Wróg / część [91067] — nazwa] 르루주 점원[햇살]
   źródło: Enemies-a1c10p1.json :: dataList[id=91067].name
   limit: do 50 znaków
   EN: Le Rouge Sales Associate [Sunshone]
   PL: Le Rouge Sales Associate [Sunshone]
413. [[a1c10p1] Wróg / część [1474] — nazwa] 수셰프
   źródło: Enemies-a1c10p1.json :: dataList[id=1474].name
   limit: do 40 znaków
   EN: Sous Chef
   PL: Sous Chef
414. [[a1c10p1] Wróg / część [1475] — nazwa] 가죽 지갑
   źródło: Enemies-a1c10p1.json :: dataList[id=1475].name
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [[a1c10p1] Wróg / część [91061] — nazwa] 목마른 르카키
   źródło: Enemies-a1c10p1.json :: dataList[id=91061].name
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [[a1c10p1] Wróg / część [91062] — nazwa] 배고픈 르카키
   źródło: Enemies-a1c10p1.json :: dataList[id=91062].name
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [[a1c10p1] Wróg / część [1482] — nazwa] 포레그
   źródło: Enemies-a1c10p1.json :: dataList[id=1482].name
   limit: do 40 znaków
   EN: Four-legs
   PL: Four-legs
418. [[a1c10p1] Wróg / część [1483] — nazwa] 원레그
   źródło: Enemies-a1c10p1.json :: dataList[id=1483].name
   limit: do 40 znaków
   EN: One-leg
   PL: One-leg
419. [[a1c10p1] Wróg / część [91063] — nazwa] 날실 바늘이
   źródło: Enemies-a1c10p1.json :: dataList[id=91063].name
   limit: do 40 znaków
   EN: Warp Needlekin
   PL: Warp Needlekin
420. [[a1c10p1] Wróg / część [91064] — nazwa] 씨실 바늘이
   źródło: Enemies-a1c10p1.json :: dataList[id=91064].name
   limit: do 40 znaków
   EN: Weft Needlekin
   PL: Weft Needlekin
421. [[a1c10p1] Wróg / część [1496] — nazwa] 바느질의 왕
   źródło: Enemies-a1c10p1.json :: dataList[id=1496].name
   limit: do 40 znaków
   EN: King of Needleworks
   PL: King of Needleworks
422. [[a1c10p1] Wróg / część [1497] — nazwa] 붉은 신의 뜯긴 살점
   źródło: Enemies-a1c10p1.json :: dataList[id=1497].name
   limit: do 50 znaków
   EN: Ripped Flesh of the Crimson God
   PL: Ripped Flesh of the Crimson God
423. [[a1c10p1] Wróg / część [1497] — opis] 붉은 신이 폭주 상태에서 처치한 대상으로 만들어낸 반시체
   źródło: Enemies-a1c10p1.json :: dataList[id=1497].desc
   limit: do 120 znaków
   EN: A half-corpse created from units the Crimson God killed in its rampage
   PL: pół-zwłoki stworzone z jednostek zabitych przez Czerwonego Boga w stanie szału
424. [[a1c10p1] Wróg / część [1498] — nazwa] 날실 바늘이
   źródło: Enemies-a1c10p1.json :: dataList[id=1498].name
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [[a1c10p1] Wróg / część [1499] — nazwa] 씨실 바늘이
   źródło: Enemies-a1c10p1.json :: dataList[id=1499].name
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [[a1c10p1] Wróg / część [1529] — nazwa] 목마른 르카키
   źródło: Enemies-a1c10p1.json :: dataList[id=1529].name
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [[a1c10p1] Wróg / część [1530] — nazwa] 배고픈 르카키
   źródło: Enemies-a1c10p1.json :: dataList[id=1530].name
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c10p1] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c10p1
- grupa rozdziału/trybu: `a1c10p1` · plik: `Skills_Abnormality-a1c10p1.json`

428. [Umiejętność wroga [146501] (ulepszenie 1) — nazwa] 셔츠는 여기에 있습니다.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146501].levelList[level=1].name
   limit: do 50 znaków
   EN: Right this way for the shirts.
   PL: Right this way for the shirts.
429. [Umiejętność wroga [146501] (ulepszenie 1) — opis] [WhenUse] [ChargeNoir] 횟수 7 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ChargeNoir]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation
   EN: [WhenUse] Gain +7 [ChargeNoir] Count
   PL: [WhenUse] zyskuje 7 Licznika [ChargeNoir]
430. [Umiejętność wroga [146501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [ChargeNoir] 횟수 3 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoir]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +3 [ChargeNoir] Count next turn
   PL: [OnSucceedAttack] zyskuje 3 Licznika [ChargeNoir] w następnej turze
431. [Umiejętność wroga [146501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Umiejętność wroga [146501] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146501].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 2 [Binding] w następnej turze
433. [Umiejętność wroga [146502] (ulepszenie 1) — nazwa] 슬랙스는 이곳에 진열되어 있습니다.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146502].levelList[level=1].name
   limit: do 50 znaków
   EN: The slacks display is right here.
   PL: The slacks display is right here.
434. [Umiejętność wroga [146502] (ulepszenie 1) — opis] [WhenUse] [ChargeNoir] 횟수 4 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ChargeNoir]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation
   EN: [WhenUse] Gain +4 [ChargeNoir] Count
   PL: [WhenUse] zyskuje 4 Licznika [ChargeNoir]
435. [Umiejętność wroga [146502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [ChargeNoir] 횟수 3 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 430 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Umiejętność wroga [146502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 4 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]
   PL: [OnSucceedAttack] nakłada 4 [Vibration]
437. [Umiejętność wroga [146502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 2 [Reduction] next turn
   PL: [OnSucceedAttack] nakłada 2 [Reduction] w następnej turze
438. [Umiejętność wroga [146503] (ulepszenie 1) — nazwa] 시착 불가 상품입니다, 고객님.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146503].levelList[level=1].name
   limit: do 80 znaków
   EN: I'm afraid this item cannot be tried on, Dear Customer.
   PL: I'm afraid this item cannot be tried on, Dear Customer.
439. [Umiejętność wroga [146503] (ulepszenie 1) — opis] [CantChangeTarget]\n대상이 <color=#ff6000><mark=#ff000040><b><u>수비 스킬을 장착했으면, 이 스킬이 취소됨</u></b></mark></color>\n[WhenUse] 자신의 [ChargeNoir]당 피해량 +10% (최대 50%)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146503].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantChangeTarget], [WhenUse], [ChargeNoir]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation
   EN: [CantChangeTarget]\n<color=#ff6000><mark=#ff000040><b><u>If target has equipped Defense Skills, cancel this Skill</u></b></mark></color>\n[WhenUse] Deal +10% damage for every [ChargeNoir] on self (max 50%)
   PL: [CantChangeTarget]\n<color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma założoną Umiejętność obrony, ta Umiejętność zostaje anulowana</u></b></mark></color>\n[WhenUse] zadaje +10% obrażeń za każde 1 [ChargeNoir] tej jednostki (maks. 50%)
440. [Umiejętność wroga [146503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [NoirNoComply] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NoirNoComply]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NoirNoComply] = 안내 불이행 / Instruction Incompliance
   EN: [OnSucceedAttack] Inflict 2 [NoirNoComply]
   PL: [OnSucceedAttack] nakłada 2 [NoirNoComply]
441. [Umiejętność wroga [146503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 진동 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
442. [Umiejętność wroga [146503] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [ChargeNoir] 횟수 5를 소모하여 [VibrationExplosion].
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146503].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoir], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Consume 5 [ChargeNoir] Count to trigger [VibrationExplosion]
   PL: [OnSucceedAttack] zużywa 5 Licznika [ChargeNoir], aby wywołać [VibrationExplosion]
443. [Umiejętność wroga [146504] (ulepszenie 1) — nazwa] 뭐라도 편하게 시착해 보시죠, 고객님.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146504].levelList[level=1].name
   limit: do 80 znaków
   EN: Please, feel free to try something on, Dear Customer.
   PL: Please, feel free to try something on, Dear Customer.
444. [Umiejętność wroga [146504] (ulepszenie 1) — opis] [CantChangeTarget]\n[StartBattle] 대상이 <color=#ff6000><mark=#ff000040><b><u>수비 스킬을 장착했으면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경되고 최종 위력 +5</u></b></mark></color>\n[WhenUse] 자신의 [ChargeNoir]당 피해량 +10% (최대 50%)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146504].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantChangeTarget], [StartBattle], [SuperCoin], [WhenUse], [ChargeNoir]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation
   EN: [CantChangeTarget]\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>If target has equipped Defense Skills, convert all Coins in this Skill to [SuperCoin]s and gain Final Power +5</u></b></mark></color>\n[WhenUse] Deal +10% damage for every [ChargeNoir] on self (max 50%)
   PL: [CantChangeTarget]\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma założoną Umiejętność obrony, wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y, a Moc Końcowa +5</u></b></mark></color>\n[WhenUse] zadaje +10% obrażeń za każde 1 [ChargeNoir] tej jednostki (maks. 50%)
445. [Umiejętność wroga [146504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [NoirNoComply] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NoirNoComply]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NoirNoComply] = 안내 불이행 / Instruction Incompliance
   EN: [OnSucceedAttack] Inflict 1 [NoirNoComply]
   PL: [OnSucceedAttack] nakłada 1 [NoirNoComply]
446. [Umiejętność wroga [146504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 진동 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Umiejętność wroga [146504] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [ChargeNoir] 횟수 5를 소모하여 [VibrationExplosion].
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146504].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Umiejętność wroga [146505] (ulepszenie 1) — nazwa] 상품에 손상이 가지 않도록 부탁드립니다.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146505].levelList[level=1].name
   limit: do 70 znaków
   EN: Please take care not to damage the merchandise.
   PL: Please take care not to damage the merchandise.
449. [Umiejętność wroga [146505] (ulepszenie 1) — opis] [CantChangeTarget]\n[StartBattle] 대상이 <color=#ff6000><mark=#ff000040><b><u>공격 스킬을 장착했으면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경되고 최종 위력 +5</u></b></mark></color>\n[WhenUse] 자신의 [ChargeNoir]당 피해량 +10% (최대 50%)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146505].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantChangeTarget], [StartBattle], [SuperCoin], [WhenUse], [ChargeNoir]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation
   EN: [CantChangeTarget]\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>If target has equipped Attack Skills, convert all Coins in this Skill to [SuperCoin]s and gain Final Power +5</u></b></mark></color>\n[WhenUse] Deal +10% damage for every [ChargeNoir] on self (max 50%)
   PL: [CantChangeTarget]\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma założoną Umiejętność ataku, wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y, a Moc Końcowa +5</u></b></mark></color>\n[WhenUse] zadaje +10% obrażeń za każde 1 [ChargeNoir] tej jednostki (maks. 50%)
450. [Umiejętność wroga [146505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 공격 스킬을 장착했으면, [NoirNoComply] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NoirNoComply]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NoirNoComply] = 안내 불이행 / Instruction Incompliance
   EN: [OnSucceedAttack] If target has equipped Attack Skills, inflict 1 [NoirNoComply]
   PL: [OnSucceedAttack] jeżeli cel ma założoną Umiejętność ataku, nakłada 1 [NoirNoComply]
451. [Umiejętność wroga [146505] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 진동 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146505].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Umiejętność wroga [146505] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [ChargeNoir] 횟수 5를 소모하여 [VibrationExplosion].
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146505].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Umiejętność wroga [146506] (ulepszenie 1) — nazwa] 고객님! 상품에 주름이 잡히지 않도록 부탁드립니다!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146506].levelList[level=1].name
   limit: do 70 znaków
   EN: Excuse me! Please try not to wrinkle the clothes!
   PL: Excuse me! Please try not to wrinkle the clothes!
454. [Umiejętność wroga [146506] (ulepszenie 1) — opis] [StartBattle] 수비 스킬을 장착하지 않은 대상에게 가하는 피해량 +(각 대상의 [NoirNoComply] x 100)%
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146506].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [NoirNoComply]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [NoirNoComply] = 안내 불이행 / Instruction Incompliance
   EN: [StartBattle] If target has not equipped Defense Skills, deal +([NoirNoComply] on target x 100)% damage, respectively
   PL: [StartBattle] jeżeli cel nie ma założonej Umiejętności obrony, zadaje +(Wartość [NoirNoComply] każdego celu x 100)% obrażeń
455. [Umiejętność wroga [146506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Umiejętność wroga [146506] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 수비 스킬을 장착했으면, 대상의 [NoirNoComply] 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146506].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NoirNoComply]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NoirNoComply] = 안내 불이행 / Instruction Incompliance
   EN: [OnSucceedAttack] If target has equipped Defense Skills, target loses 1 [NoirNoComply]
   PL: [OnSucceedAttack] jeżeli cel ma założoną Umiejętność obrony, cel traci 1 [NoirNoComply]
457. [Umiejętność wroga [146507] (ulepszenie 1) — nazwa] 해당 상품은 사이즈가 없어서 따로 본사에 재고를 확인해 보겠습니다.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146507].levelList[level=1].name
   limit: do 120 znaków
   EN: We don't have that item in your size. Allow me to check the stocks with the head office.
   PL: We don't have that item in your size. Allow me to check the stocks with the head office.
458. [Umiejętność wroga [146507] (ulepszenie 1) — opis] [StartBattle] 이 스킬을 사용하는 슬롯에 메인 타겟으로 스킬을 3개 이상 지정했으면, [NoirBindArmor] 3 감소, 다음 턴에 [Enhancement] 2 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146507].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [NoirBindArmor], [Enhancement]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [StartBattle] If the Skill Slot using this Skill is a main target of 3 or more Skills, lose 3 [NoirBindArmor] and gain 2 [Enhancement] next turn
   PL: [StartBattle] jeżeli Slot tej Umiejętności jest głównym celem 3 lub więcej Umiejętności, traci 3 [NoirBindArmor] i zyskuje 2 [Enhancement] w następnej turze
459. [Umiejętność wroga [149401] (ulepszenie 1) — nazwa] 스티칭
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149401].levelList[level=1].name
   limit: do 40 znaków
   EN: Stitching
   PL: Stitching
460. [Umiejętność wroga [149401] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeRouge] 횟수 6 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] Gain +6 [ChargeRouge] Count
   PL: [WhenUse] zyskuje 6 Licznika [ChargeRouge]
461. [Umiejętność wroga [149401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeRouge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRouge] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +2 [ChargeRouge] Count
   PL: [OnSucceedAttack] zyskuje 2 Licznika [ChargeRouge]
462. [Umiejętność wroga [149401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Umiejętność wroga [149401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Umiejętność wroga [149402] (ulepszenie 1) — nazwa] 스탬핑
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149402].levelList[level=1].name
   limit: do 40 znaków
   EN: Stamping
   PL: Stamping
465. [Umiejętność wroga [149402] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeRouge] 횟수 4 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] Gain +4 [ChargeRouge] Count
   PL: [WhenUse] zyskuje 4 Licznika [ChargeRouge]
466. [Umiejętność wroga [149402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 461 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Umiejętność wroga [149402] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Laceration] o 1
468. [Umiejętność wroga [149402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Umiejętność wroga [149402] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Umiejętność wroga [149403] (ulepszenie 1) — nazwa] 트리플 스티칭
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149403].levelList[level=1].name
   limit: do 40 znaków
   EN: Triple Stitching
   PL: Triple Stitching
471. [Umiejętność wroga [149403] (ulepszenie 1) — opis] [StartBattle] 자신의 현재 체력이 최대 체력의 50% 미만이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[EndSkill] 자신의 [ChargeRouge] 횟수를 3 소모하여, 체력 30 회복
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149403].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SuperCoin], [DefeatDuel], [EndSkill], [ChargeRouge]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [ChargeRouge] = 맥동 / Pulsation
   EN: [StartBattle] At lower than 50% HP, convert all Coins in this Skill to [SuperCoin]s\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[EndSkill] Consume 3 [ChargeRouge] Count on self to heal 30 HP
   PL: [StartBattle] przy HP tej jednostki poniżej 50% Maks. HP wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y\n[DefeatDuel] obrażenia z tej Umiejętności nie Oszołamiają celu\n[EndSkill] zużywa 3 Licznika [ChargeRouge], aby przywrócić 30 HP
472. [Umiejętność wroga [149403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 4 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 4 [Laceration]
473. [Umiejętność wroga [149403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 461 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Umiejętność wroga [149403] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 이 코인 최종 피해량만큼 자신의 체력 회복
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149403].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal HP on self equal to this Coin's final damage
   PL: [OnSucceedAttack] przywraca tej jednostce HP równe końcowym obrażeniom tej Monety
475. [Umiejętność wroga [149403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Umiejętność wroga [149403] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149403].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 461 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Umiejętność wroga [149403] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 이 코인 최종 피해량만큼 자신의 체력 회복
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149403].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Umiejętność wroga [149403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Umiejętność wroga [149403] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149403].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 461 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Umiejętność wroga [149403] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 이 코인 최종 피해량만큼 자신의 체력 회복
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149403].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Umiejętność wroga [149404] (ulepszenie 1) — nazwa] 공격적 마케팅
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149404].levelList[level=1].name
   limit: do 40 znaków
   EN: Aggressive Marketing
   PL: Aggressive Marketing
482. [Umiejętność wroga [149404] (ulepszenie 1) — opis] [StartBattle] 자신의 현재 체력이 최대 체력의 50% 미만이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경되고, [DefenseDown] 3, [ChargeRouge] 횟수 6 얻음\n[DefeatDuel] 피해량 -80%, 이 스킬 피해로 대상이 흐트러지지 않음\n[WhenUse] 자신의 [ChargeRouge] 1당 이 스킬 피해량 +10% (최대 30%)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149404].levelList[level=1].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SuperCoin], [DefenseDown], [ChargeRouge], [DefeatDuel], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [ChargeRouge] = 맥동 / Pulsation; [DefeatDuel] = [합 패배] / [Clash Lose]; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] At lower than 50% HP, convert all Coins in this Skill to [SuperCoin]s, gain 3 [DefenseDown], and +6 [ChargeRouge] Count\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target\n[WhenUse] This Skill deals +10% damage for every [ChargeRouge] on self (max 30%)
   PL: [StartBattle] przy HP tej jednostki poniżej 50% Maks. HP wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y, zyskuje 3 [DefenseDown] i 6 Licznika [ChargeRouge]\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu\n[WhenUse] ta Umiejętność zadaje +10% obrażeń za każde 1 [ChargeRouge] tej jednostki (maks. 30%)
483. [Umiejętność wroga [149404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 4 [Laceration] and +2 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 4 [Laceration] i zwiększa Licznik [Laceration] o 2
484. [Umiejętność wroga [149404] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인 최종 피해량만큼 자신의 체력 회복 (스킬당 최대 100)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149404].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Heal HP on self equal to this Coin's final damage (max 100 HP per Skill)
   PL: [UnBrokenCoinOnSucceedAttack] przywraca tej jednostce HP równe końcowym obrażeniom tej Monety (maks. 100 HP na Umiejętność)
485. [Umiejętność wroga [149404] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 횟수를 3 소모하여, 이 코인 재사용 (최대 3회)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149404].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeRouge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRouge] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Consume 3 [ChargeRouge] Count on self to Reuse this Coin (max 3 times)
   PL: [OnSucceedAttack] zużywa 3 Licznika [ChargeRouge], aby użyć tej Monety ponownie (maks. 3 razy)
486. [Umiejętność wroga [149404] (ulepszenie 1) — moneta 1, efekt 4 — opis] [ReUseOnSucceedAttack] 대상의 [Laceration] 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149404].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [Laceration]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [Laceration] = 출혈 / Bleed
   EN: [ReUseOnSucceedAttack] Activate [Laceration] on target. Target loses 1 [Laceration] Count
   PL: [ReUseOnSucceedAttack] aktywuje [Laceration] na celu. Cel traci 1 Licznika [Laceration]
487. [Umiejętność wroga [147401] (ulepszenie 1) — nazwa] 써는 거예요
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147401].levelList[level=1].name
   limit: do 50 znaków
   EN: Cutting up the meat, you hear?
   PL: Cutting up the meat, you hear?
488. [Umiejętność wroga [147401] (ulepszenie 1) — opis] [WhenUse] 대상에게 [SapsareeSpices]가 있으면, 최종 위력 +1
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [SapsareeSpices]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SapsareeSpices] = 매콤매콤소스 / Fiery, Tongue-scorching Sauce
   EN: [WhenUse] If target has [SapsareeSpices], Final Power +1
   PL: [WhenUse] jeżeli cel ma [SapsareeSpices], Moc Końcowa +1
489. [Umiejętność wroga [147401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Umiejętność wroga [147401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Umiejętność wroga [147402] (ulepszenie 1) — nazwa] 크게 써는 거예요
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147402].levelList[level=1].name
   limit: do 50 znaków
   EN: Cutting up big chunks, you hear?
   PL: Cutting up big chunks, you hear?
492. [Umiejętność wroga [147402] (ulepszenie 1) — opis] [WhenUse] 대상의 [SapsareeSpices] 1당, 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [SapsareeSpices]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SapsareeSpices] = 매콤매콤소스 / Fiery, Tongue-scorching Sauce
   EN: [WhenUse] Final Power +1 for every [SapsareeSpices] on target (max 2)
   PL: [WhenUse] Moc Końcowa +1 za każde 1 [SapsareeSpices] celu (maks. 2)
493. [Umiejętność wroga [147402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Umiejętność wroga [147402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Umiejętność wroga [147403] (ulepszenie 1) — nazwa] 난도질 하는 거예요
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147403].levelList[level=1].name
   limit: do 40 znaków
   EN: Chop, mince, dice, you hear?
   PL: Chop, mince, dice, you hear?
496. [Umiejętność wroga [147403] (ulepszenie 1) — opis] [WhenUse] 대상에게 [SapsareeSpices]가 있으면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration] 6당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147403].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [SapsareeSpices], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SapsareeSpices] = 매콤매콤소스 / Fiery, Tongue-scorching Sauce; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has [SapsareeSpices], Coin Power +1\n[WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)
   PL: [WhenUse] jeżeli cel ma [SapsareeSpices], Moc Monety +1\n[WhenUse] Moc Monety +1 za każde 6 [Laceration] celu (maks. 2)
497. [Umiejętność wroga [147403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Umiejętność wroga [147403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Umiejętność wroga [147403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Umiejętność wroga [147404] (ulepszenie 1) — nazwa] 제 시그니쳐인 거예요
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147404].levelList[level=1].name
   limit: do 50 znaków
   EN: My signature knife work, you hear?
   PL: My signature knife work, you hear?
501. [Umiejętność wroga [147404] (ulepszenie 1) — opis] [WhenUse] 자신의 [SapsareeYammi] 2당, 코인 위력 +1\n[WhenUse] 메인 타겟에게 [SapsareeSpices]가 있으면, 최종 위력 +3\n[DefeatDuel] 피해량이 80%만큼 감소하고, 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] 보유한 [SapsareeYammi] 모두 소모
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147404].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [SapsareeYammi], [SapsareeSpices], [DefeatDuel], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SapsareeYammi] = 맛있는거 먹고 힘난다는거예요 / Eat yummies and perk up, you hear?; [SapsareeSpices] = 매콤매콤소스 / Fiery, Tongue-scorching Sauce; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Coin Power +1 for every 2 [SapsareeYammi] on self\n[WhenUse] If the main target has [SapsareeSpices], Final Power +3\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] Consume all [SapsareeYammi] on self
   PL: [WhenUse] Moc Monety +1 za każde 2 [SapsareeYammi] tej jednostki\n[WhenUse] jeżeli główny cel ma [SapsareeSpices], Moc Końcowa +3\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu\n[EndSkill] zużywa wszystkie [SapsareeYammi] tej jednostki
502. [Umiejętność wroga [147404] (ulepszenie 1) — tekst klimatyczny] 이 기술을 익혀서 마침내 수셰프로 승급되었다 한다.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147404].levelList[level=1].flavor
   limit: do 120 znaków
   EN: This is the technique that saw her promoted to the position of Sous Chef.
   PL: To ta technika zapewniła jej awans na stanowisko Sous Chef.
503. [Umiejętność wroga [147404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Umiejętność wroga [147404] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147404].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Umiejętność wroga [147404] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147404].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Laceration]
506. [Umiejętność wroga [147404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Umiejętność wroga [147404] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147404].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Umiejętność wroga [147404] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147404].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Umiejętność wroga [147404] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147404].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Umiejętność wroga [147404] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147404].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Umiejętność wroga [147404] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147404].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Umiejętność wroga [147405] (ulepszenie 1) — nazwa] 재료를 얻는 거예요
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147405].levelList[level=1].name
   limit: do 60 znaków
   EN: I'm collecting ingredients, you hear?
   PL: I'm collecting ingredients, you hear?
513. [Umiejętność wroga [147405] (ulepszenie 1) — opis] [CantDuel][CantChangeTarget]\n보유한 효과가 가장 많은 아군을 우선 지정\n이 스킬을 사용하는 동안 아군의 기본 정신력 감소 조건을 비활성화
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147405].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]
   EN: [CantDuel] [CantChangeTarget]\nPrioritizes allies that have the most types of effects\nDeactivates allies' "Base factors decreasing Sanity" while using this Skill
   PL: [CantDuel][CantChangeTarget]\npriorytet: sojusznik z największą liczbą posiadanych efektów\npodczas używania tej Umiejętności dezaktywuje u sojuszników „bazowe warunki spadku Poczytalności”
514. [Umiejętność wroga [147405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>대상 아군 처치</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Kill the targeted ally</u></b>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>zabija wskazanego sojusznika</u></b></mark></color>
515. [Umiejętność wroga [147406] (ulepszenie 1) — nazwa] 다들 모이라는 거예요!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147406].levelList[level=1].name
   limit: do 50 znaków
   EN: Everyone come come, you hear?
   PL: Everyone come come, you hear?
516. [Umiejętność wroga [147406] (ulepszenie 1) — opis] [CanDuelGuard]\n다음 턴에 가죽 지갑을 전장에 가능한 만큼 소환
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147406].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard
   EN: [CanDuelGuard]\nSummon all available Leather Wallets to the field
   PL: [CanDuelGuard]\nw następnej turze przywołuje na pole wszystkie dostępne Leather Wallets
517. [Umiejętność wroga [147406] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147406].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Umiejętność wroga [147407] (ulepszenie 1) — nazwa] 맛있는거 쳐먹으라는 거예요
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147407].levelList[level=1].name
   limit: do 50 znaków
   EN: Yummers! Slurp that up, you hear?
   PL: Yummers! Slurp that up, you hear?
519. [Umiejętność wroga [147407] (ulepszenie 1) — opis] 메인 타겟과 서브 타겟 모두 아군을 지정하는 스킬\n대상이 아군이면 피해량이 항상 0으로 고정
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147407].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This Skill targets allies for both main and sub-targets\nWhen targeting an ally, always deal 0 damage
   PL: ta Umiejętność wskazuje sojuszników jako główny cel i cel poboczny\njeżeli celem jest sojusznik, obrażenia zawsze wynoszą 0
520. [Umiejętność wroga [147407] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 적군일 시, [SapsareeSpices] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147407].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SapsareeSpices]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SapsareeSpices] = 매콤매콤소스 / Fiery, Tongue-scorching Sauce
   EN: [OnSucceedAttack] If target is an enemy, inflict 1 [SapsareeSpices]
   PL: [OnSucceedAttack] jeżeli cel jest wrogiem, nakłada 1 [SapsareeSpices]
521. [Umiejętność wroga [147407] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 아군일 시, 다음 턴에 [AttackUp] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147407].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttack] If target is an ally , apply 2 [AttackUp] next turn
   PL: [OnSucceedAttack] jeżeli cel jest sojusznikiem, nakłada 2 [AttackUp] w następnej turze
522. [Umiejętność wroga [147407] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 적군일 시, [SapsareeSpices] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147407].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 520 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Umiejętność wroga [147407] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 아군일 시, 다음 턴에 [DefenseUp] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147407].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] If target is an ally , apply 2 [DefenseUp] next turn
   PL: [OnSucceedAttack] jeżeli cel jest sojusznikiem, nakłada 2 [DefenseUp] w następnej turze
524. [Umiejętność wroga [147407] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 적군일 시, [SapsareeSpices] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147407].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 520 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Umiejętność wroga [147407] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 아군일 시, 다음 턴에 [ParryingResultUp] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147407].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ParryingResultUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: [OnSucceedAttack] If target is an ally , apply 1 [ParryingResultUp] next turn
   PL: [OnSucceedAttack] jeżeli cel jest sojusznikiem, nakłada 1 [ParryingResultUp] w następnej turze
526. [Umiejętność wroga [147408] (ulepszenie 1) — nazwa] 앗! 제 식사시간인거예요
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147408].levelList[level=1].name
   limit: do 50 znaków
   EN: Aah! I'm on lunch break, you hear?
   PL: Aah! I'm on lunch break, you hear?
527. [Umiejętność wroga [147408] (ulepszenie 1) — opis] [CantIdentify]\n이 스킬은 적중하지 않으며, 피해량이 항상 0으로 고정\n[EndSkill] 자신이 보유한 [SapsareeCooking] 1당, 최대 체력의 1%를 회복하고 [SapsareeYammi] 1 얻음\n[EndSkill] 자신이 보유한 [SapsareeCooking] 1당, 자신을 제외한 모든 아군이 최대 체력의 20%를 회복하고 [SapsareeYammi] 1 얻음\n[EndSkill] [SapsareeCooking] 모두 소모
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147408].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill], [SapsareeCooking], [SapsareeYammi]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [SapsareeCooking] = 토막난 요리재료 / Chopped Ingredients; [SapsareeYammi] = 맛있는거 먹고 힘난다는거예요 / Eat yummies and perk up, you hear?
   EN: [CantIdentify]\nThis Skill does not hit and deals 0 damage\n[EndSkill] For every [SapsareeCooking] on self, heal 1% HP on self and gain 1 [SapsareeYammi]\n[EndSkill] For every [SapsareeCooking] on self, all other allies heal 20% HP and gain 1 [SapsareeYammi]\n[EndSkill] Consume all [SapsareeCooking]
   PL: [CantIdentify]\nta Umiejętność nie trafia i zadaje 0 obrażeń\n[EndSkill] za każde 1 [SapsareeCooking] tej jednostki przywraca 1% Maks. HP i zyskuje 1 [SapsareeYammi]\n[EndSkill] za każde 1 [SapsareeCooking] tej jednostki wszyscy pozostali sojusznicy przywracają 20% Maks. HP i zyskują 1 [SapsareeYammi]\n[EndSkill] zużywa wszystkie [SapsareeCooking]
528. [Umiejętność wroga [147409] (ulepszenie 1) — nazwa] 요리!!! 요리하게 해달라는 거예요!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147409].levelList[level=1].name
   limit: do 60 znaków
   EN: Cooking!! Lemme get cooking, you hear?!
   PL: Cooking!! Lemme get cooking, you hear?!
529. [Umiejętność wroga [147409] (ulepszenie 1) — opis] [CantIdentify]\n다음 턴에 가죽 지갑을 전장에 가능한 만큼 소환\n[EndSkill] [SapsareeHungry]를 모두 소모하며, 이번 턴 동안 [SapsareeHungry]를 얻지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147409].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill], [SapsareeHungry]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]; [SapsareeHungry] = 배고픈 거예요 / Got an appetite, you hear?
   EN: [CantIdentify]\nSummon all available Leather Wallets to the field\n[EndSkill] Consume all [SapsareeHungry]; does not gain [SapsareeHungry] for the rest of this turn
   PL: [CantIdentify]\nw następnej turze przywołuje na pole wszystkie dostępne Leather Wallets\n[EndSkill] zużywa wszystkie [SapsareeHungry] i przez resztę tej tury nie zyskuje [SapsareeHungry]
530. [Umiejętność wroga [147409] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147409].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Umiejętność wroga [147409] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147409].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Umiejętność wroga [147409] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147409].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Umiejętność wroga [147409] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147409].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Umiejętność wroga [147409] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147409].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Umiejętność wroga [147409] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147409].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Umiejętność wroga [147409] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147409].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Umiejętność wroga [147501] (ulepszenie 1) — nazwa] 냠냠
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147501].levelList[level=1].name
   limit: do 40 znaków
   EN: Nom Nom
   PL: Nom Nom
538. [Umiejętność wroga [147501] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)
   PL: [WhenUse] Moc Końcowa +1 za każde 4 [Laceration] celu (maks. 2)
539. [Umiejętność wroga [147501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Umiejętność wroga [147502] (ulepszenie 1) — nazwa] 쩝쩝
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147502].levelList[level=1].name
   limit: do 40 znaków
   EN: Munch Munch
   PL: Munch Munch
541. [Umiejętność wroga [147502] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 6당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)
   PL: [WhenUse] Moc Monety +1 za każde 6 [Laceration] celu (maks. 2)
542. [Umiejętność wroga [147502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Umiejętność wroga [147502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Umiejętność wroga [147503] (ulepszenie 1) — nazwa] 꺼어어억
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147503].levelList[level=1].name
   limit: do 40 znaków
   EN: Buuuurp
   PL: Buuuurp
545. [Umiejętność wroga [147503] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당, 최종 위력 +2 (최대 4)\n[WhenUse] 자신의 [SapsareeYammi]가 3 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 자신의 [SapsareeYammi]가 5 이상이면, 가중치 +2\n[WhenUse] 자신의 [SapsareeYammi] 모두 소모
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147503].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [SapsareeYammi], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [SapsareeYammi] = 맛있는거 먹고 힘난다는거예요 / Eat yummies and perk up, you hear?; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Final Power +2 for every 4 [Laceration] on target (max 4)\n[WhenUse] At 3+ [SapsareeYammi], convert all Coins on this Skill to [SuperCoin]s\n[WhenUse] At 5+ [SapsareeYammi], gain +2 Atk Weight\n[WhenUse] Consume all [SapsareeYammi] on self
   PL: [WhenUse] Moc Końcowa +2 za każde 4 [Laceration] celu (maks. 4)\n[WhenUse] przy 3+ [SapsareeYammi] wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y\n[WhenUse] przy 5+ [SapsareeYammi] Waga Ataku +2\n[WhenUse] zużywa wszystkie [SapsareeYammi] tej jednostki
546. [Umiejętność wroga [147503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 정신력 10 피해
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 10 SP damage
   PL: [OnSucceedAttack] zadaje 10 obrażeń SP
547. [Umiejętność wroga [147503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [SapsareeSpices] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SapsareeSpices]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SapsareeSpices] = 매콤매콤소스 / Fiery, Tongue-scorching Sauce
   EN: [OnSucceedAttack] Inflict 1 [SapsareeSpices]
   PL: [OnSucceedAttack] nakłada 1 [SapsareeSpices]
548. [Umiejętność wroga [147504] (ulepszenie 1) — nazwa] 푸드코트 대기
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147504].levelList[level=1].name
   limit: do 40 znaków
   EN: Standby at the Food Court
   PL: Standby at the Food Court
549. [Umiejętność wroga [147504] (ulepszenie 1) — opis] [StartBattle] <color=#ff6000><mark=#ff000040><b><u>[SapsareeShield] 1 얻음</u></b></mark></color>\n[WhenUse] 대상의 ([Laceration] 위력 x 5)만큼 보호막 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147504].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StartBattle], [SapsareeShield], [WhenUse], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SapsareeShield] = 먹어줘... / Please, eat me...; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [StartBattle] <color=#ff6000><mark=#ff000040><b><u>Gain 1 [SapsareeShield]</u></b></mark></color>\n[WhenUse] Gain ([Laceration] Potency on target x 5) Shield
   PL: [StartBattle] <color=#ff6000><mark=#ff000040><b><u>zyskuje 1 [SapsareeShield]</u></b></mark></color>\n[WhenUse] zyskuje Tarczę równą (Siła [Laceration] celu x 5)
550. [Umiejętność wroga [147505] (ulepszenie 1) — nazwa] 조리되고 싶지 않아.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147505].levelList[level=1].name
   limit: do 40 znaków
   EN: I don't want to be cooked.
   PL: I don't want to be cooked.
551. [Umiejętność wroga [147505] (ulepszenie 1) — opis] [SupportProtect] 전용 스킬\n[DefeatDuel] [Vulnerable] 5 얻음\n<color=#ff6000><mark=#ff000040><b><u>[EndSkillAll] 자신이 살아있다면, 수셰프가 자신에게 '재료를 얻는 거예요' 사용</u></b></mark></color>\n(수셰프가 흐트러짐 상태이면, 발동하지 않음)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147505].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [SupportProtect], [DefeatDuel], [Vulnerable], [EndSkillAll]
   znaczenie tagów: [SupportProtect] = 원호 방어 / Assist Defense; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile; [EndSkillAll] = [스킬 종료시] / [Skill End]
   EN: [SupportProtect] exclusive Skill\n[DefeatDuel] Gain 5 [Vulnerable]\n<color=#ff6000><mark=#ff000040><b><u>[EndSkillAll] If this unit is alive, Sous Chef uses "I'm collecting ingredients, you hear?" on self</u></b></mark></color>\n(Does not trigger if Sous Chef is Staggered)
   PL: Umiejętność wyłącznie dla [SupportProtect]\n[DefeatDuel] zyskuje 5 [Vulnerable]\n<color=#ff6000><mark=#ff000040><b><u>[EndSkillAll] jeżeli ta jednostka żyje, Sous Chef używa „I'm collecting ingredients, you hear?” na tej jednostce</u></b></mark></color>\n(nie uruchamia się, jeżeli Sous Chef jest w stanie Oszołomienia)
552. [Umiejętność wroga [147505] (ulepszenie 1) — tekst klimatyczny] 고기의 역할을 다 할 시간.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147505].levelList[level=1].flavor
   limit: do 120 znaków
   EN: Time for the meat to fulfill its role.
   PL: Czas, by mięso spełniło swoją rolę.
553. [Umiejętność wroga [147505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=147505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Umiejętność wroga [148003] (ulepszenie 1) — nazwa] 공복 꺼억
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148003].levelList[level=1].name
   limit: do 40 znaków
   EN: Buuuurp on Empty Stomach
   PL: Buuuurp on Empty Stomach
555. [Umiejętność wroga [148003] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당, 최종 위력 +2 (최대 4)\n[WhenUse] 자신이 보유한 효과가 3개 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 자신이 보유한 효과가 5개 이상이면, 가중치 +2
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148003].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Final Power +2 for every 4 [Laceration] on target (max 4)\n[WhenUse] At 3+ types of effects, convert all Coins on this Skill to [SuperCoin]s\n[WhenUse] At 5+ types of effects, gain +2 Atk Weight
   PL: [WhenUse] Moc Końcowa +2 za każde 4 [Laceration] celu (maks. 4)\n[WhenUse] przy 3+ rodzajach posiadanych efektów wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y\n[WhenUse] przy 5+ rodzajach posiadanych efektów Waga Ataku +2
556. [Umiejętność wroga [148003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 정신력 10 피해
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Umiejętność wroga [148004] (ulepszenie 1) — nazwa] 밍기적
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148004].levelList[level=1].name
   limit: do 40 znaków
   EN: Dawdle
   PL: Dawdle
558. [Umiejętność wroga [148004] (ulepszenie 1) — opis] [WhenUse] 대상의 ([Laceration] 위력 x 5)만큼 보호막 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Gain ([Laceration] Potency on target x 5) Shield
   PL: [WhenUse] zyskuje Tarczę równą (Siła [Laceration] celu x 5)
559. [Umiejętność wroga [148004] (ulepszenie 1) — tekst klimatyczny] 르카키들은 보통 할 게 없으면 멍하니 있기만 한다.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148004].levelList[level=1].flavor
   limit: do 120 znaków
   EN: Unless there's something to do, most of Le Kaki space out and do nothing.
   PL: Jeśli nie mają nic do roboty, Le Kaki najczęściej bezmyślnie stoje w miejscu.
560. [Umiejętność wroga [148101] (ulepszenie 1) — nazwa] 안내방송
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148101].levelList[level=1].name
   limit: do 40 znaków
   EN: Customer Announcement
   PL: Customer Announcement
561. [Umiejętność wroga [148101] (ulepszenie 1) — opis] 합 가능 수비 스킬과 합 진행 시, 합 위력 +20\n이 스킬은 대상의 수비 스킬을 발동시키지 않음\n이 스킬로 가하는 피해량이 0으로 고정됨\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] 대상에게 [Wariness] 10 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148101].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuel], [Wariness]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [Wariness] = 경계심 / Guarded Caution
   EN: In a Clash against a Clashable Defense Skill, Clash Power +20\nThis Skill does not trigger the target's Defense Skill\nThis Skill deals 0 damage\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] Inflict 10 [Wariness] on target</u></b></mark></color>
   PL: w Starciu z Umiejętnością obrony zdolną do Starcia Moc Starcia +20\nta Umiejętność nie uruchamia Umiejętności obrony celu\nta Umiejętność zadaje 0 obrażeń\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] nakłada 10 [Wariness] na cel</u></b></mark></color>
562. [Umiejętność wroga [148101] (ulepszenie 1) — tekst klimatyczny] 들어라… 목소리를 들어라….
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148101].levelList[level=1].flavor
   limit: do 120 znaków
   EN: Listen... Hear the Voice...
   PL: Słuchaj... Usłysz ten Głos...
563. [Umiejętność wroga [148101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Umiejętność wroga [148101] (ulepszenie 1) — moneta 1, efekt 2 — opis] <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] 대상의 [Wariness]을 전부 제거하고 [ReliefSense] 1 부여 (수감자별 턴당 1회)</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [Wariness], [ReliefSense]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Wariness] = 경계심 / Guarded Caution; [ReliefSense] = 경청에 대한 감사 / Gratitude for Listening
   EN: <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] Remove all [Wariness] on target and apply 1 [ReliefSense] (once per Sinner per turn)</u></b></mark></color>
   PL: <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] usuwa wszystkie [Wariness] celu i nakłada 1 [ReliefSense] (1 raz na turę na Grzesznika)</u></b></mark></color>
565. [Umiejętność wroga [148102] (ulepszenie 1) — nazwa] 경고방송
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148102].levelList[level=1].name
   limit: do 40 znaków
   EN: Warning Announcement
   PL: Warning Announcement
566. [Umiejętność wroga [148102] (ulepszenie 1) — opis] [CantChangeTarget]\n- 지정된 수감자와 [Wariness] 수치가 동일한 수감자일 경우, 속도에 관계 없이 대상 변경 가능\n[Wariness]이 제일 높은 대상을 우선 타겟팅함\n이 스킬은 대상의 수비 스킬을 발동시키지 않음\n[EndSkill] 대상의 [Wariness] 전부 소모
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148102].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [Wariness], [EndSkill]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [Wariness] = 경계심 / Guarded Caution; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantChangeTarget]\n- Any Sinner that has the same [Wariness] Stack as the targeted Sinner can draw this Skill to itself regardless of Speed\nPrioritizes targets that have the highest [Wariness] Stack\nThis Skill does not trigger the target's Defense Skill\n[EndSkill] Consume all [Wariness] on target
   PL: [CantChangeTarget]\n- każdy Grzesznik z taką samą wartością [Wariness] jak wskazany Grzesznik może przyciągnąć tę Umiejętność na siebie niezależnie od Szybkości\npriorytet: cel z najwyższą wartością [Wariness]\nta Umiejętność nie uruchamia Umiejętności obrony celu\n[EndSkill] zużywa całą wartość [Wariness] celu
567. [Umiejętność wroga [148102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Umiejętność wroga [148102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>(대상의 정신력 + 45)만큼 정신력 피해를 입히고, 다음 턴에 [HorribleTerror] 1 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [HorribleTerror]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HorribleTerror] = 끔찍한 반복 재생 / Horribly Infinite Replay
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Deal (target's SP + 45) SP damage; then, inflict 1 [HorribleTerror] next turn</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>zadaje (SP celu + 45) obrażeń SP, po czym nakłada 1 [HorribleTerror] w następnej turze</u></b></mark></color>
569. [Umiejętność wroga [148103] (ulepszenie 1) — nazwa] 들어줘서… 고맙다…
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148103].levelList[level=1].name
   limit: do 50 znaków
   EN: Thank you... for listening...
   PL: Dziękuję... za wysłuchanie...
570. [Umiejętność wroga [148103] (ulepszenie 1) — opis] [CantChangeTarget]\n- 지정된 수감자와 [ReliefSense] 수치가 동일한 수감자일 경우, 속도에 관계 없이 대상 변경 가능\n[ReliefSense]가 제일 높은 대상을 우선 타겟팅함\n[DefeatDuel] 이 스킬과 합을 한 스킬로부터 받는 피해량 +150%\n[EndSkill] 대상의 [ReliefSense]를 전부 제거
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148103].levelList[level=1].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [ReliefSense], [DefeatDuel], [EndSkill]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [ReliefSense] = 경청에 대한 감사 / Gratitude for Listening; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantChangeTarget]\n- Any Sinner that has the same [ReliefSense] Stack as the targeted Sinner can draw this Skill to itself regardless of Speed\nPrioritizes targets that have the highest [ReliefSense] Stack\n[DefeatDuel] Take +150% damage from the Skill that Clashed with this Skill\n[EndSkill] Remove all [ReliefSense] on target
   PL: [CantChangeTarget]\n- każdy Grzesznik z taką samą wartością [ReliefSense] jak wskazany Grzesznik może przyciągnąć tę Umiejętność na siebie niezależnie od Szybkości\npriorytet: cel z najwyższą wartością [ReliefSense]\n[DefeatDuel] otrzymuje +150% obrażeń od Umiejętności, z którą stoczyła Starcie\n[EndSkill] usuwa wszystkie [ReliefSense] celu
571. [Umiejętność wroga [148103] (ulepszenie 1) — tekst klimatyczny] 매혹에는 여러 종류가 있다. 결과도 다르며 과정도 다르다. 하지만 매혹의 상태는 동일하다. 마음이 열렸고 취약해진다는 것.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148103].levelList[level=1].flavor
   limit: do 220 znaków
   EN: Enthrallment takes many forms, with different paths and different endings. Yet the state itself is always the same: the heart opens and, in opening, becomes vulnerable.
   PL: Fascynacja przybiera wiele postaci — różne ścieżki, różne zakończenia. Lecz sam stan jest zawsze ten sam: serce się otwiera i, otwierając się, staje się kruche.
572. [Umiejętność wroga [148103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Umiejętność wroga [148104] (ulepszenie 1) — nazwa] 돌진
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148104].levelList[level=1].name
   limit: do 40 znaków
   EN: Onrush
   PL: Onrush
574. [Umiejętność wroga [148104] (ulepszenie 1) — opis] [WhenUse] 대상의 [Vibration]과 [Sinking]의 합 4당, 최종 위력 +1 (최대 3)\n[WhenUse] 체력이 50% 이하면, 다음 효과가 적용됨\n- 이 스킬로 부여하는 [Vibration] 위력과 횟수 +2\n- 마지막 코인이 [SuperCoin]으로 변경되고 적중 시, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148104].levelList[level=1].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [Sinking], [SuperCoin], [VibrationExplosion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [WhenUse] Final Power +1 for every 4 ([Vibration] + [Sinking]) on target (max 3)\n[WhenUse] At lower than 50% HP, gain the following effects:\n- This Skill inflicts +2 more [Vibration] Potency and Count\n- Convert the final Coin to [SuperCoin]; On Hit, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [WhenUse] Moc Końcowa +1 za każde 4 ([Vibration] + [Sinking]) celu (maks. 3)\n[WhenUse] przy HP 50% lub mniej zyskuje następujące efekty:\n- ta Umiejętność nakłada o 2 więcej Siły i Licznika [Vibration]\n- ostatnia Moneta zamienia się w [SuperCoin]; przy trafieniu wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
575. [Umiejętność wroga [148104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] nakłada 2 [Vibration]
576. [Umiejętność wroga [148104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Vibration] o 1
577. [Umiejętność wroga [148105] (ulepszenie 1) — nazwa] 육중한 돌진
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148105].levelList[level=1].name
   limit: do 40 znaków
   EN: Crushing Onrush
   PL: Crushing Onrush
578. [Umiejętność wroga [148105] (ulepszenie 1) — opis] [WhenUse] 대상의 [Vibration]과 [Sinking]의 합 4당, 최종 위력 +1 (최대 3)\n[WhenUse] 체력이 50% 이하면, 다음 효과가 적용됨\n- 이 스킬로 부여하는 [Vibration] 위력과 횟수 +2\n- 두 번째, 세 번째 코인이 [SuperCoin]으로 변경되고 두 번째 코인 적중 시, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148105].levelList[level=1].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [Sinking], [SuperCoin], [VibrationExplosion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [WhenUse] Final Power +1 for every 4 ([Vibration] + [Sinking]) on target (max 3)\n[WhenUse] At lower than 50% HP, gain the following effects:\n- This Skill inflicts +2 more [Vibration] Potency and Count\n- Convert the second and third Coins to [SuperCoin]s; On Hit using the second Coin, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [WhenUse] Moc Końcowa +1 za każde 4 ([Vibration] + [Sinking]) celu (maks. 3)\n[WhenUse] przy HP 50% lub mniej zyskuje następujące efekty:\n- ta Umiejętność nakłada o 2 więcej Siły i Licznika [Vibration]\n- druga i trzecia Moneta zamieniają się w [SuperCoin]y; przy trafieniu drugą Monetą wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
579. [Umiejętność wroga [148105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] nakłada 1 [Vibration]
580. [Umiejętność wroga [148105] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148105].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność wroga [148105] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148105].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Umiejętność wroga [148106] (ulepszenie 1) — nazwa] 층 울리기
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148106].levelList[level=1].name
   limit: do 40 znaków
   EN: Floorwide Echo
   PL: Floorwide Echo
583. [Umiejętność wroga [148106] (ulepszenie 1) — opis] [CantChangeTarget]\n패닉 상태인 대상을 우선으로 지정\n[ReliefSense]를 보유한 수감자일 경우, 대상 변경 가능\n[WhenUse] 대상에게 [ReliefSense]가 없으면, 공격 가중치 +2\n[WhenUse] 메인 타겟의 [Vibration]과 [Sinking]의 합 4당, 최종 위력 +1 (최대 4)\n[DefeatDuel] 다음 효과가 적용됨\n- 피해량 -50%\n- 이 스킬의 피해로 대상이 흐트러지지 않고, 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148106].levelList[level=1].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [ReliefSense], [WhenUse], [Vibration], [Sinking], [DefeatDuel]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [ReliefSense] = 경청에 대한 감사 / Gratitude for Listening; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [CantChangeTarget]\nPrioritizes targets that are in Panic\nSinners that have [ReliefSense] can draw this Skill to itself\n[WhenUse] If target does not have [ReliefSense], gain +2 Atk Weight\n[WhenUse] Final Power +1 for every 4 ([Vibration] + [Sinking]) on the main target (max 4)\n[DefeatDuel] Gain the Following effects:\n- Deal -50% damage\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] effect on target
   PL: [CantChangeTarget]\npriorytet: cele w Panice\nGrzesznicy z [ReliefSense] mogą przyciągnąć tę Umiejętność na siebie\n[WhenUse] jeżeli cel nie ma [ReliefSense], Waga Ataku +2\n[WhenUse] Moc Końcowa +1 za każde 4 ([Vibration] + [Sinking]) głównego celu (maks. 4)\n[DefeatDuel] zyskuje następujące efekty:\n- zadaje -50% obrażeń\n- obrażenia z tej Umiejętności nie Oszołamiają celu, a przy trafieniu nie aktywuje efektu [Sinking] celu
584. [Umiejętność wroga [148106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Sinking] o 2
585. [Umiejętność wroga [148106] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148106].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Umiejętność wroga [148106] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [UnresolvedFeelings]만큼 [Sinking] 부여 (최대 15)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148106].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [UnresolvedFeelings], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [UnresolvedFeelings] = 다층 레이어 패치워크 / Layered Patchwork; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict [Sinking] equal to [UnresolvedFeelings] (max 15)
   PL: [UnBrokenCoinOnSucceedAttack] nakłada [Sinking] równe wartości [UnresolvedFeelings] (maks. 15)
587. [Umiejętność wroga [148107] (ulepszenie 1) — nazwa] 쾅! 쾅! 콰와앙!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148107].levelList[level=1].name
   limit: do 40 znaków
   EN: WHUMP! THUMP! KRA-KOOM!
   PL: WHUMP! THUMP! KRA-KOOM!
588. [Umiejętność wroga [148107] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[StartBattle] 보호막 100 얻음\n- 잃은 체력 1%당, 보호막 4 추가로 얻음 (최대 200)\n- 공격 시작 전에 보호막이 파괴되지 않았을 때, 남은 보호막 수치 100당 마지막 코인 1회 재사용 (최대 2회)\n[WhenUse] 메인 타겟의 [Vibration]과 [Sinking]의 합 6당, 최종 위력 +1, 코인 위력 +1 (각각 최대 4)\n[DefeatDuel] 다음 효과가 적용됨\n- 피해량 -75%\n- 이 스킬의 피해로 대상이 흐트러지지 않고, 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148107].levelList[level=1].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Vibration], [Sinking], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed\n[StartBattle] Gain 100 Shield\n- Gain 4 more Shield for every 1% missing HP (max 200)\n- Before Attack, if Shield is not broken, Reuse final Coin once for every 100 remaining Shield (max 2 times)\n[WhenUse] Final Power +1 and Coin Power +1 for every 6 ([Vibration] + [Sinking]) on the main target (max 4 each)\n[DefeatDuel] Gain the following effects:\n- Deal -75% damage\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] effect on target
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[StartBattle] zyskuje 100 Tarczy\n- zyskuje 4 dodatkowej Tarczy za każde 1% utraconego HP (maks. 200)\n- przed atakiem, jeżeli Tarcza nie została zniszczona, używa ostatniej Monety ponownie 1 raz za każde 100 pozostałej Tarczy (maks. 2 razy)\n[WhenUse] Moc Końcowa +1 i Moc Monety +1 za każde 6 ([Vibration] + [Sinking]) głównego celu (maks. 4 każdy)\n[DefeatDuel] zyskuje następujące efekty:\n- zadaje -75% obrażeń\n- obrażenia z tej Umiejętności nie Oszołamiają celu, a przy trafieniu nie aktywuje efektu [Sinking] celu
589. [Umiejętność wroga [148107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Umiejętność wroga [148107] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] ([UnresolvedFeelings]/3)만큼 [Sinking] 부여 (최대 10)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148107].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [UnresolvedFeelings], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [UnresolvedFeelings] = 다층 레이어 패치워크 / Layered Patchwork; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict ([UnresolvedFeelings] / 3) [Sinking] (max 10)
   PL: [UnBrokenCoinOnSucceedAttack] nakłada ([UnresolvedFeelings] / 3) [Sinking] (maks. 10)
591. [Umiejętność wroga [148107] (ulepszenie 1) — moneta 1, efekt 3 — opis] [ReUseOnSucceedAttack] 대상에게 [ReliefSense]가 없으면, [Wariness] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148107].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [ReliefSense], [Wariness]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [ReliefSense] = 경청에 대한 감사 / Gratitude for Listening; [Wariness] = 경계심 / Guarded Caution
   EN: [ReUseOnSucceedAttack] If target does not have [ReliefSense], inflict 1 [Wariness]
   PL: [ReUseOnSucceedAttack] jeżeli cel nie ma [ReliefSense], nakłada 1 [Wariness]
592. [Umiejętność wroga [148108] (ulepszenie 1) — nazwa] 층 울리기
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148108].levelList[level=1].name
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Umiejętność wroga [148108] (ulepszenie 1) — opis] [CantChangeTarget]\n패닉 상태인 대상을 우선으로 지정\n[ReliefSense]를 보유한 수감자일 경우, 대상 변경 가능\n이 스킬은 대상의 수비 스킬을 발동시키지 않음\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse] 공격 가중치 +3\n- 메인 타겟의 [ReliefSense] 1당, 증가하는 공격 가중치가 1씩 감소\n[WhenUse] 다음 효과가 적용됨\n- 메인 타겟의 [Vibration]과 [Sinking]의 합 4당, 최종 위력 +1 (최대 4)\n- 메인 타겟의 [Wariness] 3당, 합 위력 +1 (최대 3)\n- 피해량 +(대상의 [Wariness] x 10)% (최대 100%, 타겟별로 적용)\n[DefeatDuel] 다음 효과가 적용됨\n- 피해량 -50%\n- 이 스킬의 피해로 대상이 흐트러지지 않고, 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148108].levelList[level=1].desc
   limit: do 980 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [ReliefSense], [WhenUse], [Vibration], [Sinking], [Wariness], [DefeatDuel]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [ReliefSense] = 경청에 대한 감사 / Gratitude for Listening; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking; [Wariness] = 경계심 / Guarded Caution; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [CantChangeTarget]\nPrioritizes targets that are in Panic\nSinners that have [ReliefSense] can draw this Skill to itself\nThis Skill does not trigger the target's Defense Skill\nCan Clash with this Skill regardless of Speed\n[WhenUse] Gain +3 Atk Weight\n- Reduce Atk Weight gain by 1 for every 1 [ReliefSense] on the main target\n[WhenUse] Gain the following effects:\n- Final Power +1 for every 4 ([Vibration] + [Sinking]) on the main target (max 4)\n- Clash Power +1 for every 3 [Wariness] on the main target (max 3)\n- Deal +([Wariness] on target x 10)% damage (max 100%; calculated separately for each target)\n[DefeatDuel] Gain the following effects:\n- Deal -50% damage\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] effect on target
   PL: [CantChangeTarget]\npriorytet: cele w Panice\nGrzesznicy z [ReliefSense] mogą przyciągnąć tę Umiejętność na siebie\nta Umiejętność nie uruchamia Umiejętności obrony celu\nmoże stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse] Waga Ataku +3\n- za każde 1 [ReliefSense] głównego celu Wzrost Wagi Ataku maleje o 1\n[WhenUse] zyskuje następujące efekty:\n- Moc Końcowa +1 za każde 4 ([Vibration] + [Sinking]) głównego celu (maks. 4)\n- Moc Starcia +1 za każde 3 [Wariness] głównego celu (maks. 3)\n- zadaje +(Wartość [Wariness] celu x 10)% obrażeń (maks. 100%, rozpatrywane osobno dla każdego celu)\n[DefeatDuel] zyskuje następujące efekty:\n- zadaje -50% obrażeń\n- obrażenia z tej Umiejętności nie Oszołamiają celu, a przy trafieniu nie aktywuje efektu [Sinking] celu
594. [Umiejętność wroga [148108] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148108].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Umiejętność wroga [148108] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148108].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] zwiększa Licznik [Sinking] o 3
596. [Umiejętność wroga [148108] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148108].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Umiejętność wroga [148108] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [UnresolvedFeelings]만큼 [Sinking] 부여 (최대 15)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148108].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Umiejętność wroga [148108] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148108].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Umiejętność wroga [148108] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [UnresolvedFeelings]만큼 [Sinking] 부여 (최대 15)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148108].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Umiejętność wroga [148109] (ulepszenie 1) — nazwa] 쾅! 쾅! 콰앙! 콰아아앙!!!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148109].levelList[level=1].name
   limit: do 50 znaków
   EN: WHUMP! THUMP! KRA-KOOM! BOOM-CRACK!
   PL: WHUMP! THUMP! KRA-KOOM! BOOM-CRACK!
601. [Umiejętność wroga [148109] (ulepszenie 1) — opis] 이 스킬은 대상의 수비 스킬을 발동시키지 않음\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[StartBattle] 보호막 100 얻음\n- 잃은 체력 1%당, 보호막 4 추가로 얻음 (최대 400)\n- 공격 시작 전에 보호막이 파괴되지 않았을 때, 남은 보호막 수치 100당 마지막 코인 1회 재사용 (최대 3회)\n[WhenUse] 다음 효과가 적용됨\n- 메인 타겟의 [Vibration]과 [Sinking]의 합 6당, 최종 위력 +1, 코인 위력 +1 (각각 최대 4)\n- 메인 타겟의 [Wariness] 2당, 합 위력 +1 (최대 5)\n- 피해량 +(대상의 [Wariness] x 10)% (최대 100%, 타겟별로 적용)\n[DefeatDuel] 다음 효과가 적용됨\n- 피해량 -75%\n- 이 스킬의 피해로 대상이 흐트러지지 않고, 적중 시 대상의 [Sinking] 효과가 발동하지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148109].levelList[level=1].desc
   limit: do 970 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Vibration], [Sinking], [Wariness], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking; [Wariness] = 경계심 / Guarded Caution; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: This Skill does not trigger the target's Defense Skill\nCan Clash with this Skill regardless of Speed\n[StartBattle] Gain 100 Shield\n- Gain 4 more Shield for every 1% missing HP (max 400)\n- Before Attack, if Shield is not broken, Reuse final Coin once for every 100 remaining Shield (max 3 times)\n[WhenUse] Gain the following effects:\n- Final Power +1 and Coin Power +1 for every 6 ([Vibration] + [Sinking]) on the main target (max 4 each)\n- Clash Power +1 for every 2 [Wariness] on the main target (max 5)\n- Deal +([Wariness] on target x 10)% damage (max 100%; calculated separately for each target)\n[DefeatDuel] Gain the following effects:\n- Deal -75% damage\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] effect on target
   PL: ta Umiejętność nie uruchamia Umiejętności obrony celu\nmoże stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[StartBattle] zyskuje 100 Tarczy\n- zyskuje 4 dodatkowej Tarczy za każde 1% utraconego HP (maks. 400)\n- przed atakiem, jeżeli Tarcza nie została zniszczona, używa ostatniej Monety ponownie 1 raz za każde 100 pozostałej Tarczy (maks. 3 razy)\n[WhenUse] zyskuje następujące efekty:\n- Moc Końcowa +1 i Moc Monety +1 za każde 6 ([Vibration] + [Sinking]) głównego celu (maks. 4 każdy)\n- Moc Starcia +1 za każde 2 [Wariness] głównego celu (maks. 5)\n- zadaje +(Wartość [Wariness] celu x 10)% obrażeń (maks. 100%, rozpatrywane osobno dla każdego celu)\n[DefeatDuel] zyskuje następujące efekty:\n- zadaje -75% obrażeń\n- obrażenia z tej Umiejętności nie Oszołamiają celu, a przy trafieniu nie aktywuje efektu [Sinking] celu
602. [Umiejętność wroga [148109] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148109].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Umiejętność wroga [148109] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] ([UnresolvedFeelings]/2)만큼 [Sinking] 부여 (최대 15)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148109].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [UnresolvedFeelings], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [UnresolvedFeelings] = 다층 레이어 패치워크 / Layered Patchwork; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict ([UnresolvedFeelings] / 2) [Sinking] (max 15)
   PL: [OnSucceedAttack] nakłada ([UnresolvedFeelings] / 2) [Sinking] (maks. 15)
604. [Umiejętność wroga [148109] (ulepszenie 1) — moneta 1, efekt 3 — opis] [ReUseOnSucceedAttack] 대상에게 [ReliefSense]가 없으면, [Wariness] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148109].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 591 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Umiejętność wroga [146601] (ulepszenie 1) — nazwa] 들려! 들린다고!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146601].levelList[level=1].name
   limit: do 40 znaków
   EN: I hear it... I can hear it!
   PL: I hear it... I can hear it!
606. [Umiejętność wroga [146601] (ulepszenie 1) — opis] [WhenUse] [ChargeRouge] 횟수 5 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] Gain +5 [ChargeRouge] Count
   PL: [WhenUse] zyskuje 5 Licznika [ChargeRouge]
607. [Umiejętność wroga [146601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [ChargeRouge] 횟수 2 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeRouge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRouge] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +2 [ChargeRouge] Count
   PL: [OnSucceedAttack] zyskuje 2 Licznika [ChargeRouge]
608. [Umiejętność wroga [146601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [ChargeRouge] 횟수 2 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 607 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Umiejętność wroga [146601] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146601].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Umiejętność wroga [146602] (ulepszenie 1) — nazwa] 한번 더 옷을 갈아입을 수 있었어!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146602].levelList[level=1].name
   limit: do 80 znaków
   EN: I have been granted another chance to change my clothes!
   PL: I have been granted another chance to change my clothes!
611. [Umiejętność wroga [146602] (ulepszenie 1) — opis] [WhenUse] [ChargeRouge] 횟수 5 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146602].levelList[level=1].desc
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Umiejętność wroga [146602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [ChargeRouge] 횟수 2 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 607 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność wroga [146602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [ChargeRouge] 횟수 2 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 607 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Umiejętność wroga [146602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Umiejętność wroga [146603] (ulepszenie 1) — nazwa] 내 믿음이 무의미하지 않았던거야!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146603].levelList[level=1].name
   limit: do 40 znaków
   EN: My faith wasn't in vain!
   PL: My faith wasn't in vain!
616. [Umiejętność wroga [146603] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeRouge] 1당 피해량 +10% (최대 50%)\n[WhenUse] [ChargeRouge] 횟수를 5 소모하여 최종 위력 +2
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146603].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] Deal +10% damage for every [ChargeRouge] on self (max 50%)\n[WhenUse] Consume 5 [ChargeRouge] Count to gain Final Power +2
   PL: [WhenUse] zadaje +10% obrażeń za każde 1 [ChargeRouge] tej jednostki (maks. 50%)\n[WhenUse] zużywa 5 Licznika [ChargeRouge], aby zyskać Moc Końcową +2
617. [Umiejętność wroga [146603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Umiejętność wroga [146603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Umiejętność wroga [146604] (ulepszenie 1) — nazwa] 긁어내! 뜯어내! 벗겨내!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146604].levelList[level=1].name
   limit: do 40 znaków
   EN: Scrape! Flay! Peel!
   PL: Scrape! Flay! Peel!
620. [Umiejętność wroga [146604] (ulepszenie 1) — opis] [StartBattle] 자신의 현재 체력이 최대 체력의 50% 미만이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 자신의 [ChargeRouge] 1당 피해량 +10% (최대 50%)\n[WhenUse] 자신의 [ChargeRouge] 횟수 1당 피해량 +3% (최대 60%)\n\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -2
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146604].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SuperCoin], [WhenUse], [ChargeRouge], [BeforeAttack]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [StartBattle] At lower than 50% HP, convert all Coins in this Skill to [SuperCoin]s\n[WhenUse] Deal +10% damage for every [ChargeRouge] on self (max 50%)\n[WhenUse] Deal +3% damage for every [ChargeRouge] Count on self (max 60%)\n\n[BeforeAttack] Base Power -2 for every Cracked Coin
   PL: [StartBattle] przy HP tej jednostki poniżej 50% Maks. HP wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y\n[WhenUse] zadaje +10% obrażeń za każde 1 [ChargeRouge] tej jednostki (maks. 50%)\n[WhenUse] zadaje +3% obrażeń za każdy 1 Licznik [ChargeRouge] tej jednostki (maks. 60%)\n\n[BeforeAttack] Moc Bazowa -2 za każdą zniszczoną Monetę
621. [Umiejętność wroga [146604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Umiejętność wroga [146604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Umiejętność wroga [146605] (ulepszenie 1) — nazwa] 이 세상에 의미는 있던 거였어!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146605].levelList[level=1].name
   limit: do 60 znaków
   EN: So this world wasn't meaningless after all!
   PL: So this world wasn't meaningless after all!
624. [Umiejętność wroga [146605] (ulepszenie 1) — opis] [StartBattle] 수비 스킬을 장착한 대상 1명당, 이 스킬 피해량 -10%\n[StartBattle] 공격 스킬을 장착한 대상 1명당, 다음 턴에 [DefenseDown] 1 얻음\n\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -1
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146605].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefenseDown], [BeforeAttack]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [StartBattle] This Skill deals -10% damage for every target that has equipped Defense Skills\n[StartBattle] Gain 1 [DefenseDown] next turn for every target that has equipped Attack Skills\n\n[BeforeAttack] Base Power -1 for every Cracked Coin
   PL: [StartBattle] ta Umiejętność zadaje -10% obrażeń za każdy cel z założoną Umiejętnością obrony\n[StartBattle] zyskuje 1 [DefenseDown] w następnej turze za każdy cel z założoną Umiejętnością ataku\n\n[BeforeAttack] Moc Bazowa -1 za każdą zniszczoną Monetę
625. [Umiejętność wroga [146605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Umiejętność wroga [146605] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146605].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Umiejętność wroga [146606] (ulepszenie 1) — nazwa] 확실히 나와 함께하신다!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146606].levelList[level=1].name
   limit: do 50 znaków
   EN: The Voice is with me, this I know!
   PL: The Voice is with me, this I know!
628. [Umiejętność wroga [146606] (ulepszenie 1) — opis] [OnDirectAttack] 이 스킬 피해량 -80%
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146606].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnDirectAttack]
   znaczenie tagów: [OnDirectAttack] = [일방 공격 시] / [On Unopposed Attack]
   EN: [OnDirectAttack] This Skill deals -80% damage
   PL: [OnDirectAttack] ta Umiejętność zadaje -80% obrażeń
629. [Umiejętność wroga [146606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Umiejętność wroga [146606] (ulepszenie 1) — moneta 1, efekt 2 — opis] [DefeatDuelAttack] 이 스킬 최종 피해량만큼 체력 회복
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146606].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuelAttack]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]
   EN: [DefeatDuelAttack] Heal HP equal to this Skill's final damage
   PL: [DefeatDuelAttack] przywraca HP równe końcowym obrażeniom tej Umiejętności
631. [Umiejętność wroga [146607] (ulepszenie 1) — nazwa] 더욱 나답게… 다시 한번 더 나답게…!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146607].levelList[level=1].name
   limit: do 50 znaków
   EN: Be myself... Be utterly myself...!
   PL: Be myself... Be utterly myself...!
632. [Umiejętność wroga [146607] (ulepszenie 1) — opis] [DuelCounter]\n[RougeThreeCocoon] 전용 스킬\n\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 흐트러짐 상태가 되지 않음.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146607].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [RougeThreeCocoon], [DefeatDuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [RougeThreeCocoon] = 탈의실 / Changing Room; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DuelCounter]\n[RougeThreeCocoon] exclusive Skill\n\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [DuelCounter]\n[RougeThreeCocoon] Umiejętność wyłącznie dla tego stanu\n\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
633. [Umiejętność wroga [146607] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146607].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Umiejętność wroga [146607] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146607].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Laceration]
635. [Umiejętność wroga [146607] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>자신의 [RougeThreeCocoonHit]이 10 이상이면, 이 코인 재사용 (스킬당 1회)</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146607].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [RougeThreeCocoonHit]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RougeThreeCocoonHit] = 핍박 / Persecution
   EN: [OnSucceedAttack] At 10+ <color=#ff6000><mark=#ff000040><b><u>[RougeThreeCocoonHit] on self, Reuse this Coin (once per Skill)</u></b></mark></color>
   PL: [OnSucceedAttack] przy 10+ wartości <color=#ff6000><mark=#ff000040><b><u>[RougeThreeCocoonHit] tej jednostki używa tej Monety ponownie (1 raz na Umiejętność)</u></b></mark></color>
636. [Umiejętność wroga [146607] (ulepszenie 1) — moneta 1, efekt 4 — opis] [ReUseOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>자신의 [RougeThreeCocoonHit]이 20 이상이면, 이 코인 재사용 (스킬당 1회)</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146607].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [ReUseOnSucceedAttack], [RougeThreeCocoonHit]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [RougeThreeCocoonHit] = 핍박 / Persecution
   EN: [ReUseOnSucceedAttack]<color=#ff6000><mark=#ff000040><b><u> At 20+ [RougeThreeCocoonHit], Reuse this Coin (once per Skill)</u></b></mark></color>
   PL: [ReUseOnSucceedAttack]<color=#ff6000><mark=#ff000040><b><u> przy 20+ [RougeThreeCocoonHit] tej jednostki używa tej Monety ponownie (1 raz na Umiejętność)</u></b></mark></color>
637. [Umiejętność wroga [146607] (ulepszenie 1) — moneta 1, efekt 5 — opis] [ReUseOnSucceedAttack] [ChargeRouge] 횟수 1 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=146607].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [ChargeRouge]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [ChargeRouge] = 맥동 / Pulsation
   EN: [ReUseOnSucceedAttack] Gain +1 [ChargeRouge] Count
   PL: [ReUseOnSucceedAttack] zyskuje 1 Licznika [ChargeRouge]
638. [Umiejętność wroga [148201] (ulepszenie 1) — nazwa] 다그닥
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148201].levelList[level=1].name
   limit: do 40 znaków
   EN: Clip-clop
   PL: Clip-clop
639. [Umiejętność wroga [148201] (ulepszenie 1) — opis] [WhenUse]\n- 대상의 [Vibration] 4당 최종 위력 +1 (최대 3)\n- 자신의 [ChargeNoir] 횟수가 8 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [ChargeNoir] 횟수가 15 미만이면, [ChargeNoir] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148201].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [ChargeNoir]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [ChargeNoir] = 보존 / Preservation
   EN: [WhenUse]\n- Final Power +1 for every 4 [Vibration] on target (max 3)\n- At 8+ [ChargeNoir] Count, Coin Power +1\n[WhenUse] At fewer than 15 [ChargeNoir] Count, gain +2 [ChargeNoir] Count
   PL: [WhenUse]\n- Moc Końcowa +1 za każde 4 [Vibration] celu (maks. 3)\n- przy 8+ Licznika [ChargeNoir] Moc Monety +1\n[WhenUse] przy mniej niż 15 Licznika [ChargeNoir] zyskuje 2 Licznika [ChargeNoir]
640. [Umiejętność wroga [148201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Umiejętność wroga [148201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoir]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +1 [ChargeNoir] Count
   PL: [OnSucceedAttack] zyskuje 1 Licznika [ChargeNoir]
642. [Umiejętność wroga [148201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność wroga [148201] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 641 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Umiejętność wroga [148202] (ulepszenie 1) — nazwa] 다그닥, 쿵!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148202].levelList[level=1].name
   limit: do 40 znaków
   EN: Clip-clop, Buck!
   PL: Clip-clop, Buck!
645. [Umiejętność wroga [148202] (ulepszenie 1) — opis] [WhenUse]\n- 대상의 [Vibration] 4당 최종 위력 +1 (최대 3)\n- 자신의 [ChargeNoir] 횟수가 8 이상이면, 코인 위력 +1\n[WhenUse]\n- 자신의 [ChargeNoir] 횟수 3 증가\n- 자신의 [ChargeNoir]이 3 이상이면, 마지막 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148202].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [ChargeNoir], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [ChargeNoir] = 보존 / Preservation; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse]\n- Final Power +1 for every 4 [Vibration] on target (max 3)\n- At 8+ [ChargeNoir] Count, Coin Power +1\n[WhenUse]\n- Gain +3 [ChargeNoir] Count\n- At 3+ [ChargeNoir], convert the final coin to [SuperCoin]
   PL: [WhenUse]\n- Moc Końcowa +1 za każde 4 [Vibration] celu (maks. 3)\n- przy 8+ Licznika [ChargeNoir] Moc Monety +1\n[WhenUse]\n- zyskuje 3 Licznika [ChargeNoir]\n- przy 3+ wartości [ChargeNoir] ostatnia Moneta zamienia się w [SuperCoin]
646. [Umiejętność wroga [148202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 3 [Vibration] i zwiększa Licznik [Vibration] o 2
647. [Umiejętność wroga [148202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoir]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +3 [ChargeNoir] Count
   PL: [OnSucceedAttack] zyskuje 3 Licznika [ChargeNoir]
648. [Umiejętność wroga [148202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoir]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +2 [ChargeNoir] Count
   PL: [OnSucceedAttack] zyskuje 2 Licznika [ChargeNoir]
649. [Umiejętność wroga [148202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수가 15 이상이면, [ChargeNoir] 횟수 3을 소모하여 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoir], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 15+ [ChargeNoir] Count, consume 3 [ChargeNoir] Count to trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] przy 15+ Licznika [ChargeNoir] zużywa 3 Licznika [ChargeNoir], aby wywołać [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
650. [Umiejętność wroga [148203] (ulepszenie 1) — nazwa] 잘라주세요! 제발!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148203].levelList[level=1].name
   limit: do 50 znaków
   EN: Please, cut them off! I beg you!
   PL: Please, cut them off! I beg you!
651. [Umiejętność wroga [148203] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- 자신의 [ChargeNoir] 횟수가 10 이상이면, [ChargeNoir] 횟수 10을 소모하여 기본 위력 +1, 코인 위력 +1\n- 자신의 [ChargeNoir] 횟수가 10 미만이면, [ChargeNoir] 횟수 5 증가\n- 자신의 [ChargeNoir]이 3 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148203].levelList[level=1].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoir], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse]\n- At 10+ [ChargeNoir] Count, consume 10 [ChargeNoir] Count to gain Base Power +1 and Coin Power +1\n- At fewer than 10 [ChargeNoir] Count, gain +5 [ChargeNoir] Count\n- At 3+ [ChargeNoir], convert all Coins on this Skill to [SuperCoin]s
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- przy 10+ Licznika [ChargeNoir] zużywa 10 Licznika [ChargeNoir], aby zyskać Moc Bazową +1 i Moc Monety +1\n- przy mniej niż 10 Licznika [ChargeNoir] zyskuje 5 Licznika [ChargeNoir]\n- przy 3+ wartości [ChargeNoir] wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y
652. [Umiejętność wroga [148203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Umiejętność wroga [148203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Vibration] o 3
654. [Umiejętność wroga [148203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Umiejętność wroga [148203] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 이 스킬에서 [ChargeNoir] 횟수를 소모했다면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148203].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoir], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this Skill consumed [ChargeNoir] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] jeżeli ta Umiejętność zużyła Licznik [ChargeNoir], wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
656. [Umiejętność wroga [148204] (ulepszenie 1) — nazwa] 다그닥거리는 이 소리, 끔찍해….
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148204].levelList[level=1].name
   limit: do 60 znaków
   EN: Clippety-clop, what an awful sound...
   PL: Clippety-clop, what an awful sound...
657. [Umiejętność wroga [148204] (ulepszenie 1) — opis] [WideAreaRampage]\n자신의 [ChargeNoir]당 피해량 +3% (최대 15%)\n이 스킬 적중 시마다 대상에게 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n[StartBattle] (자신의 [ChargeNoir] - 2)만큼 [NoirBindArmor] 얻음 (최대 3)\n[WhenUse]\n- 모든 타겟에게 [Vibration] 3 부여, [Vibration] 횟수 3 증가\n- 자신의 [ChargeNoir] 횟수가 10 이상이면, [ChargeNoir] 횟수 10을 소모하여 기본 위력 +2, 코인 위력 +2\n[DefeatDuel]\n- 피해량 -50%\n- 이 스킬의 피해와 효과로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148204].levelList[level=1].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [ChargeNoir], [VibrationExplosion], [Vibration], [StartBattle], [NoirBindArmor], [WhenUse], [DefeatDuel]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [ChargeNoir] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [StartBattle] = [전투 시작시] / [Combat Start]; [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WideAreaRampage]\nDeal +3% damage for every [ChargeNoir] on self (max 15%)\nOn Hit, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count\n[StartBattle] Gain ([ChargeNoir] on self - 2) [NoirBindArmor] (max 3)\n[WhenUse]\n- Inflict 3 [Vibration] and +3 [Vibration] Count on all targets\n- At 10+ [ChargeNoir] Count, consume 10 [ChargeNoir] Count to gain Base Power +2 and Coin Power +2\n[DefeatDuel]\n- Deal -50% damage\n- Damage and effects caused by this Skill cannot Stagger the target
   PL: [WideAreaRampage]\nzadaje +3% obrażeń za każde 1 [ChargeNoir] tej jednostki (maks. 15%)\nprzy każdym trafieniu wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1\n[StartBattle] zyskuje (Licznik [ChargeNoir] tej jednostki - 2) [NoirBindArmor] (maks. 3)\n[WhenUse]\n- nakłada 3 [Vibration] i zwiększa Licznik [Vibration] o 3 na wszystkich celach\n- przy 10+ Licznika [ChargeNoir] zużywa 10 Licznika [ChargeNoir], aby zyskać Moc Bazową +2 i Moc Monety +2\n[DefeatDuel]\n- zadaje -50% obrażeń\n- obrażenia i efekty tej Umiejętności nie Oszołamiają celu
658. [Umiejętność wroga [148204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Umiejętność wroga [148204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Umiejętność wroga [148204] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148204].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Umiejętność wroga [148301] (ulepszenie 1) — nazwa] 불결한 것!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148301].levelList[level=1].name
   limit: do 40 znaków
   EN: Revolting Thing!
   PL: Revolting Thing!
662. [Umiejętność wroga [148301] (ulepszenie 1) — opis] [WhenUse] [NoirSuit]가 50 이상이면, 방어 레벨 증가 1 얻음\n[WhenUse] [Realisation]가 있으면,\n- 피해량 +(자신의 [ChargeNoir] 위력 x 8)% (최대 40%)\n- [Realisation] 4 소모\n[WhenUse] 자신의 [ChargeNoir] 횟수가 12 이상이면,\n[ChargeNoir] 횟수를 2 소모하여 합 위력 +1\n[WhenUse] 자신의 [ChargeNoir] 횟수가 10 미만이면, [ChargeNoir] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148301].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [NoirSuit], [Realisation], [ChargeNoir]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [NoirSuit] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat; [Realisation] = 아르뮈르 에비이예 / Armure Éveillée; [ChargeNoir] = 보존 / Preservation
   EN: [WhenUse] At 50+ [NoirSuit], gain 1 Defense Level Up\n[WhenUse] If this unit has [Realisation]:\n- Deal +([ChargeNoir] Potency on self x 8)% damage (max 40%)\n- Consume 4 [Realisation]\n[WhenUse] At 12+ [ChargeNoir] Count, consume 2 [ChargeNoir] Count to gain Clash Power +1\n[WhenUse] At fewer than 10 [ChargeNoir] Count, gain +2 [ChargeNoir] Count
   PL: [WhenUse] przy 50+ [NoirSuit] zyskuje 1 Wzrost Poziomu Obrony\n[WhenUse] jeżeli ta jednostka ma [Realisation]:\n- zadaje +(Siła [ChargeNoir] tej jednostki x 8)% obrażeń (maks. 40%)\n- zużywa 4 [Realisation]\n[WhenUse] przy 12+ Licznika [ChargeNoir] zużywa 2 Licznika [ChargeNoir], aby zyskać Moc Starcia +1\n[WhenUse] przy mniej niż 10 Licznika [ChargeNoir] zyskuje 2 Licznika [ChargeNoir]
663. [Umiejętność wroga [148301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [Umiejętność wroga [148301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 641 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Umiejętność wroga [148301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여, [Vibration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration] and +1 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 1 [Vibration] i zwiększa Licznik [Vibration] o 1
666. [Umiejętność wroga [148301] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148301].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 641 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Umiejętność wroga [148302] (ulepszenie 1) — nazwa] 다리가 하나가 아닌 게 부끄럽지도 않나?
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148302].levelList[level=1].name
   limit: do 60 znaków
   EN: Aren't you ashamed of that extra leg?
   PL: Aren't you ashamed of that extra leg?
668. [Umiejętność wroga [148302] (ulepszenie 1) — opis] [WhenUse] [NoirSuit]가 있으면,\n수치 40당, [DefenseUp] 1 얻음 (최대 2)\n[WhenUse] [Realisation]가 있으면,\n- 피해량 +(자신의 [ChargeNoir] 위력 x 6)% (최대 30%)\n- [Realisation] 6 소모\n[WhenUse] 자신의 [ChargeNoir] 횟수가 12 이상이면,\n[ChargeNoir] 횟수를 2 소모하여 최종 위력 +1\n[WhenUse] 자신의 [ChargeNoir] 횟수가 15 미만이면, [ChargeNoir] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148302].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [NoirSuit], [DefenseUp], [Realisation], [ChargeNoir]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [NoirSuit] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Realisation] = 아르뮈르 에비이예 / Armure Éveillée; [ChargeNoir] = 보존 / Preservation
   EN: [WhenUse] If this unit has [NoirSuit]:\n- Gain 1 [DefenseUp] for every 40 Stack (max 2)\n[WhenUse] If this unit has [Realisation]:\n- Deal +([ChargeNoir] Potency on self x 6)% damage (max 30%)\n- Consume 6 [Realisation]\n[WhenUse] At 12+ [ChargeNoir] Count, consume 2 [ChargeNoir] Count to gain Final Power +1\n[WhenUse] At fewer than 15 [ChargeNoir] Count, gain +3 [ChargeNoir] Count
   PL: [WhenUse] jeżeli ta jednostka ma [NoirSuit]:\n- zyskuje 1 [DefenseUp] za każde 40 Stosów (maks. 2)\n[WhenUse] jeżeli ta jednostka ma [Realisation]:\n- zadaje +(Siła [ChargeNoir] tej jednostki x 6)% obrażeń (maks. 30%)\n- zużywa 6 [Realisation]\n[WhenUse] przy 12+ Licznika [ChargeNoir] zużywa 2 Licznika [ChargeNoir], aby zyskać Moc Końcową +1\n[WhenUse] przy mniej niż 15 Licznika [ChargeNoir] zyskuje 3 Licznika [ChargeNoir]
669. [Umiejętność wroga [148302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 4 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 4 [Vibration] i zwiększa Licznik [Vibration] o 2
670. [Umiejętność wroga [148302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 648 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Umiejętność wroga [148302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 641 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Umiejętność wroga [148302] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [ChargeNoir] 위력이 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoir], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 3+ [ChargeNoir] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] przy 3+ Siły [ChargeNoir] wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
673. [Umiejętność wroga [148303] (ulepszenie 1) — nazwa] 자비롭게 그 하나 떼어 내 주지.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148303].levelList[level=1].name
   limit: do 70 znaków
   EN: I'll cut that one off You. Consider it a mercy.
   PL: I'll cut that one off You. Consider it a mercy.
674. [Umiejętność wroga [148303] (ulepszenie 1) — tekst klimatyczny] 언젠가 르누아르의 브랜드 매니저를 만났을 때, 이 자가 어떻게 반응할지 궁금하지 않아?
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148303].levelList[level=1].flavor
   limit: do 120 znaków
   EN: Ever wonder how this one would react upon meeting Le Noir's Brand Manager?
   PL: Czy nie ciekawi cię, jak ta istota zareaguje, gdy pozna Menedżera Marki Le Noir?
675. [Umiejętność wroga [148303] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse] [NoirSuit]가 있으면, 수치 30당 합 위력 +1 (최대 3)\n[WhenUse] [Realisation]가 있으면, 수치 2당 피해량 +1% (최대 50%)\n[WhenUse]\n- 자신의 [ChargeNoir] 횟수가 10 이상이면, [ChargeNoir] 횟수 10을 소모하여 코인 위력 +2\n- 자신의 [ChargeNoir] 횟수가 10 미만이면, [ChargeNoir] 횟수 5 증가\n[DefeatDuel]\n- 피해량 -50%\n- 자신의 [DefenseUp] 수치만큼, 자신에게 흐트러짐 피해
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148303].levelList[level=1].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [NoirSuit], [Realisation], [ChargeNoir], [DefeatDuel], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [NoirSuit] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat; [Realisation] = 아르뮈르 에비이예 / Armure Éveillée; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse] If this unit has [NoirSuit], Clash Power +1 for every 30 Stack (max 3)\n[WhenUse] If this unit has [Realisation], deal +1% damage for every 2 Stack (max 50%)\n[WhenUse]\n- At 10+ [ChargeNoir] Count, consume 10 [ChargeNoir] Count to gain Coin Power +2\n- At fewer than 10 [ChargeNoir] Count, gain +5 [ChargeNoir] Count\n[DefeatDuel]\n- Deal -50% damage\n- Raise this unit's Stagger Threshold equal to its [DefenseUp] Stack
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse] jeżeli ta jednostka ma [NoirSuit], Moc Starcia +1 za każde 30 Stosów (maks. 3)\n[WhenUse] jeżeli ta jednostka ma [Realisation], zadaje +1% obrażeń za każde 2 Stosy (maks. 50%)\n[WhenUse]\n- przy 10+ Licznika [ChargeNoir] zużywa 10 Licznika [ChargeNoir], aby zyskać Moc Monety +2\n- przy mniej niż 10 Licznika [ChargeNoir] zyskuje 5 Licznika [ChargeNoir]\n[DefeatDuel]\n- zadaje -50% obrażeń\n- podnosi Próg Oszołomienia tej jednostki o wartość jej Stosów [DefenseUp]
676. [Umiejętność wroga [148303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] nakłada 3 [Vibration]
677. [Umiejętność wroga [148303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] zwiększa Licznik [Vibration] o 3
678. [Umiejętność wroga [148303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Umiejętność wroga [148303] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148303].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [UnBrokenCoinOnSucceedAttack] wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
680. [Umiejętność wroga [148303] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 이 스킬에서 [ChargeNoir] 횟수를 소모했다면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148303].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 655 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Umiejętność wroga [148304] (ulepszenie 1) — nazwa] 원 킥
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148304].levelList[level=1].name
   limit: do 40 znaków
   EN: Single Kick
   PL: Single Kick
682. [Umiejętność wroga [148304] (ulepszenie 1) — opis] [WhenUse] [NoirSuit]가 있으면,\n- 수치 3당, 피해량 +1% (최대 30%)\n- 수치 15당, [DefenseUp] 1 얻음 (최대 5)\n[WhenUse] 자신의 [ChargeNoir] 횟수가 10 이상이면,\n[ChargeNoir] 횟수를 10 소모하여 코인 위력 +2\n- 체력이 50% 이하면, 남은 [ChargeNoir] 횟수를 최대 10까지 추가로 소모하여 피해량 +(추가 소모한 [ChargeNoir] 횟수 x 2.5)% (최대 25%)\n[WhenUse] 자신의 [ChargeNoir] 위력이 3/5 이상이면, 코인 위력 +1/+2\n[DefeatDuel]\n- 피해량 -75%\n- 이 스킬의 피해와 효과로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148304].levelList[level=1].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [NoirSuit], [DefenseUp], [ChargeNoir], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [NoirSuit] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If this unit has [NoirSuit]:\n- Deal +1% damage for every 3 Stack (max 30%)\n- Gain 1 [DefenseUp] for every 15 Stack (max 5)\n[WhenUse] At 10+ [ChargeNoir], consume 10 [ChargeNoir] Count to gain Coin Power +2\n- At 50% or lower HP, additionally consume up to 10 remaining [ChargeNoir] Count and deal +(additionally consumed [ChargeNoir] Count x 2.5)% damage (max 25%)\n[WhenUse] At 3+/5+ [ChargeNoir] Potency, Coin Power +1/+2\n[DefeatDuel]\n- Deal -75% damage\n- Damage and effects caused by this Skill cannot Stagger the target
   PL: [WhenUse] jeżeli ta jednostka ma [NoirSuit]:\n- zadaje +1% obrażeń za każde 3 Stosy (maks. 30%)\n- zyskuje 1 [DefenseUp] za każde 15 Stosów (maks. 5)\n[WhenUse] przy 10+ Licznika [ChargeNoir] zużywa 10 Licznika [ChargeNoir], aby zyskać Moc Monety +2\n- przy HP 50% lub mniej dodatkowo zużywa do 10 pozostałych Liczników [ChargeNoir], zadając +(dodatkowo zużyte Liczniki [ChargeNoir] x 2.5)% obrażeń (maks. 25%)\n[WhenUse] przy 3+/5+ Siły [ChargeNoir] Moc Monety +1/+2\n[DefeatDuel]\n- zadaje -75% obrażeń\n- obrażenia i efekty tej Umiejętności nie Oszołamiają celu
683. [Umiejętność wroga [148304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Umiejętność wroga [148304] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Umiejętność wroga [148304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Umiejętność wroga [148304] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148304].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Umiejętność wroga [148304] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148304].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Umiejętność wroga [148304] (ulepszenie 1) — moneta 3, efekt 2 — opis] 자신의 [DefenseUp] 1당, 피해량 +5% (최대 100%)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148304].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Deal +5% damage for every [DefenseUp] on self (max 100%)
   PL: zadaje +5% obrażeń za każde 1 [DefenseUp] tej jednostki (maks. 100%)
689. [Umiejętność wroga [148304] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148304].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Umiejętność wroga [148304] (ulepszenie 1) — moneta 3, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [ChargeNoir] 위력이 3/5 이상이면, [VibrationExplosion] 1회/2회. 대상의 [Vibration] 횟수 1/2 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148304].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ChargeNoir], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ChargeNoir] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] At 3+/5+ [ChargeNoir] Potency, trigger [VibrationExplosion] once/twice; then, reduce target's [Vibration] Count by 1/2
   PL: [UnBrokenCoinOnSucceedAttack] przy 3+/5+ Siły [ChargeNoir] wywołuje [VibrationExplosion] 1 raz/2 razy, po czym zmniejsza Licznik [Vibration] celu o 1/2
691. [Umiejętność wroga [148305] (ulepszenie 1) — nazwa] 원 킥 - 쿠튀르 뮐티플
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148305].levelList[level=1].name
   limit: do 50 znaków
   EN: Single Kick - Couture Multiple
   PL: Single Kick - Couture Multiple
692. [Umiejętność wroga [148305] (ulepszenie 1) — opis] [WhenUse] [Realisation]가 있으면,\n- 수치 2당, 피해량 +1% (최대 50%)\n- 피해량 +(자신의 [ChargeNoir] 위력 x 6)% (최대 30%)\n- [Realisation] 15 소모\n[WhenUse] 자신의 [ChargeNoir] 횟수가 10 이상이면,\n[ChargeNoir] 횟수를 10 소모하여 최종 위력 +2, 코인 위력 +1\n[WhenUse] 자신의 [ChargeNoir] 위력이 3/5 이상이면, 코인 위력 +1/+2\n[DefeatDuel]\n- 피해량 -75%\n- 이 스킬의 피해와 효과로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148305].levelList[level=1].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Realisation], [ChargeNoir], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Realisation] = 아르뮈르 에비이예 / Armure Éveillée; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If this unit has [Realisation]:\n- Deal +1% damage for every 2 Stack (max 50%)\n- Deal +([ChargeNoir] Potency on self x 6)% damage (max 30%)\n- Consume 15 [Realisation]\n[WhenUse] At 10+ [ChargeNoir] Count, consume 10 [ChargeNoir] Count to gain Final Power +2 and Coin Power +1\n[WhenUse] At 3+/5+ [ChargeNoir] Potency, Coin Power +1/+2\n[DefeatDuel]\n- Deal -75% damage\n- Damage and effects caused by this Skill cannot Stagger the target
   PL: [WhenUse] jeżeli ta jednostka ma [Realisation]:\n- zadaje +1% obrażeń za każde 2 Stosy (maks. 50%)\n- zadaje +(Siła [ChargeNoir] tej jednostki x 6)% obrażeń (maks. 30%)\n- zużywa 15 [Realisation]\n[WhenUse] przy 10+ Licznika [ChargeNoir] zużywa 10 Licznika [ChargeNoir], aby zyskać Moc Końcową +2 i Moc Monety +1\n[WhenUse] przy 3+/5+ Siły [ChargeNoir] Moc Monety +1/+2\n[DefeatDuel]\n- zadaje -75% obrażeń\n- obrażenia i efekty tej Umiejętności nie Oszołamiają celu
693. [Umiejętność wroga [148305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Umiejętność wroga [148305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Umiejętność wroga [148305] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148305].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Umiejętność wroga [148305] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148305].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Umiejętność wroga [148305] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148305].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Umiejętność wroga [148305] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148305].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Umiejętność wroga [148305] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148305].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Umiejętność wroga [148305] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [ChargeNoir] 위력이 3/5 이상이면, [VibrationExplosion] 1회/2회. 대상의 [Vibration] 횟수 1/2 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148305].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 690 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Umiejętność wroga [148305] (ulepszenie 1) — moneta 4, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인 최종 피해량의 20%만큼 관통 피해
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148305].levelList[level=1].coinlist[#3].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal (20% of this Coin's final damage) Pierce damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje obrażenia Kłute równe 20% końcowych obrażeń tej Monety
702. [Umiejętność wroga [149601] (ulepszenie 1) — nazwa] 경사가 어떻고
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149601].levelList[level=1].name
   limit: do 40 znaków
   EN: Bla Bla Warp Bla
   PL: Bla Bla Warp Bla
703. [Umiejętność wroga [149601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Umiejętność wroga [149601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Umiejętność wroga [149602] (ulepszenie 1) — nazwa] 위사가 저쨌니
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149602].levelList[level=1].name
   limit: do 40 znaków
   EN: Yap Yap Weft Yap
   PL: Yap Yap Weft Yap
706. [Umiejętność wroga [149602] (ulepszenie 1) — opis] [WideAreaRampage]\n\n대상의 [NiddlePin] 1당 피해량 +5% (최대 25%)\n\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149602].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [NiddlePin], [DefeatDuel]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [NiddlePin] = 바늘못 / Naildle; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WideAreaRampage]\n\nDeal +5% damage for every [NiddlePin] on target (max 25%)\n\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WideAreaRampage]\n\nzadaje +5% obrażeń za każde 1 [NiddlePin] celu (maks. 25%)\n\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
707. [Umiejętność wroga [149602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [Umiejętność wroga [149602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Umiejętność wroga [149602] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [NiddlePin] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149602].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [NiddlePin]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [NiddlePin] = 바늘못 / Naildle
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [NiddlePin]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [NiddlePin]
710. [Umiejętność wroga [149602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Umiejętność wroga [149602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Umiejętność wroga [149602] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [NiddlePin] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149602].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 709 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Umiejętność wroga [149602] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149602].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Umiejętność wroga [149602] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149602].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Umiejętność wroga [149602] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [NiddlePin] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149602].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 709 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Umiejętność wroga [149603] (ulepszenie 1) — nazwa] 땀수! 땀수! 땀수!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149603].levelList[level=1].name
   limit: do 40 znaków
   EN: Stitch! Per! Inch!
   PL: Stitch! Per! Inch!
717. [Umiejętność wroga [149603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [Umiejętność wroga [149603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NiddlePin] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NiddlePin]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NiddlePin] = 바늘못 / Naildle
   EN: [OnSucceedAttack] Inflict 1 [NiddlePin]
   PL: [OnSucceedAttack] nakłada 1 [NiddlePin]
719. [Umiejętność wroga [149603] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149603].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Umiejętność wroga [149603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Umiejętność wroga [149603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NiddlePin] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 718 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Umiejętność wroga [149603] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149603].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Umiejętność wroga [149603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [Umiejętność wroga [149603] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [NiddlePin] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149603].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 718 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Umiejętność wroga [149603] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149603].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Umiejętność wroga [149603] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149603].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Umiejętność wroga [149603] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [NiddlePin] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149603].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 718 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Umiejętność wroga [149603] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149603].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Umiejętność wroga [149604] (ulepszenie 1) — nazwa] 인치당 땀수 20 이상으로!!!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149604].levelList[level=1].name
   limit: do 50 znaków
   EN: 20 stitches an inch, minimum!!!
   PL: 20 stitches an inch, minimum!!!
730. [Umiejętność wroga [149604] (ulepszenie 1) — opis] [DefeatDuel] 피해량 -80%, 이 스킬의 피해로 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
731. [Umiejętność wroga [149604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Umiejętność wroga [149604] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149604].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Umiejętność wroga [149604] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [NiddlePin] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149604].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 709 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Umiejętność wroga [149605] (ulepszenie 1) — nazwa] 스티치가 너무 균일하다고? 손 피크가 아니라고? 집합!!!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149605].levelList[level=1].name
   limit: do 80 znaków
   EN: Too even, you say? Not pick-stitching, you say? Assemble!!!
   PL: Too even, you say? Not pick-stitching, you say? Assemble!!!
735. [Umiejętność wroga [149605] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 바늘이[TabExplain] 3개 소환
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149605].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [TabExplain]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Summon 3 Needlekin[TabExplain] next turn
   PL: [StartBattle] przywołuje 3 Needlekin[TabExplain] w następnej turze
736. [Umiejętność wroga [149606] (ulepszenie 1) — nazwa] 핸드 스티칭하라고!!!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149606].levelList[level=1].name
   limit: do 70 znaków
   EN: You want me to hand-stitch this?! HAND-STITCH???!!!
   PL: You want me to hand-stitch this?! HAND-STITCH???!!!
737. [Umiejętność wroga [149606] (ulepszenie 1) — opis] 흐트러지지 않은 아군을 우선으로 지정하며, 피해량이 항상 0으로 고정\n대상의 수비 스킬을 발동시키지 않음\n\n[EndSkill] 대상 바늘이가 무작위 공격 스킬 발동 (흐트러짐 무시)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149606].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill], [TabExplain]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: Prioritizes allies that are not Staggered; deals 0 damage\nDoes not trigger the target's Defense Skill\n\n[EndSkill] Targeted Needlekin[TabExplain] activates a random Attack Skill (ignores Stagger)
   PL: priorytet: sojusznicy spoza Oszołomienia; obrażenia zawsze wynoszą 0\nta Umiejętność nie uruchamia Umiejętności obrony celu\n\n[EndSkill] wskazany Needlekin[TabExplain] używa losowej Umiejętności ataku (ignoruje Oszołomienie)
738. [Umiejętność wroga [149606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 공격 위력 증가 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Apply 1 Attack Power Up this turn and next turn
   PL: [OnSucceedAttack] nakłada 1 Wzrost Mocy Ataku w tej i w następnej turze
739. [Umiejętność wroga [149607] (ulepszenie 1) — nazwa] 옆선 바깥에 박음선 두 줄 보이면 더블니들. 탈락!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149607].levelList[level=1].name
   limit: do 90 znaków
   EN: Double stitching past the side seam? Double-needle! Rejected!
   PL: Double stitching past the side seam? Double-needle! Rejected!
740. [Umiejętność wroga [149607] (ulepszenie 1) — opis] [WhenUse] <color=#ff6000><mark=#ff000040><b><u>전장의 바늘이[TabExplain] 1개당 피해량 +50%\n • 전장에 바늘이가 없으면, 스킬이 취소됨</u></b></mark></color>\n\n[EndSkill] 모든 바늘이[TabExplain] 처치\n • 이 효과로 처치한 바늘이[TabExplain] 1개당 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149607].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [TabExplain], [EndSkill], [Enhancement]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [WhenUse] <color=#ff6000><mark=#ff000040><b><u>Deal +50% damage for every Needlekin[TabExplain] on the field\n • If there are no Needlekin[TabExplain] on the field, cancel this Skill</u></b></mark></color>\n\n[EndSkill] Kill every Needlekin[TabExplain]\n • Gain 1 [Enhancement] next turn for every Needlekin[TabExplain] killed by this effect
   PL: [WhenUse] <color=#ff6000><mark=#ff000040><b><u>zadaje +50% obrażeń za każdego Needlekin[TabExplain] na polu\n • jeżeli na polu nie ma Needlekin[TabExplain], Umiejętność zostaje anulowana</u></b></mark></color>\n\n[EndSkill] zabija wszystkie Needlekin[TabExplain]\n • zyskuje 1 [Enhancement] w następnej turze za każdego Needlekin[TabExplain] zabitego tym efektem
741. [Umiejętność wroga [149607] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149607].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Umiejętność wroga [149607] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NiddlePinned]인 대상에게 가하는 피해량 +100%
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149607].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NiddlePinned]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NiddlePinned] = 박제 상태 / Taxidermized
   EN: [OnSucceedAttack] Deal +100% damage against [NiddlePinned] targets
   PL: [OnSucceedAttack] zadaje +100% obrażeń celom z [NiddlePinned]
743. [Umiejętność wroga [149608] (ulepszenie 1) — nazwa] 단추 X자 봉제 아니면 탈락!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149608].levelList[level=1].name
   limit: do 50 znaków
   EN: No cross-stitch buttons? Rejected!
   PL: No cross-stitch buttons? Rejected!
744. [Umiejętność wroga [149608] (ulepszenie 1) — opis] [DefeatDuel] 대상의 [NiddlePin] 2 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149608].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel], [NiddlePin]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [NiddlePin] = 바늘못 / Naildle
   EN: [DefeatDuel] Reduce [NiddlePin] on target by 2
   PL: [DefeatDuel] zmniejsza wartość [NiddlePin] celu o 2
745. [Umiejętność wroga [149608] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [NiddlePin]을 1 소모하여 고정 피해 5
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149608].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NiddlePin]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NiddlePin] = 바늘못 / Naildle
   EN: [OnSucceedAttack] Consume 1 [NiddlePin] on target to deal 5 fixed damage
   PL: [OnSucceedAttack] zużywa 1 [NiddlePin] celu, aby zadać 5 obrażeń stałych
746. [Umiejętność wroga [149608] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [NiddlePin]을 1 소모하여 고정 피해 5
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149608].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 745 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Umiejętność wroga [149609] (ulepszenie 1) — nazwa] 피크스티치 일부러 눈에 띄게 박았냐고?! 그렇게 쳐박아주마!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149609].levelList[level=1].name
   limit: do 90 znaków
   EN: Pick stitch too obvious, you say?! I'll pick-stitch your ass!
   PL: Pick stitch too obvious, you say?! I'll pick-stitch your ass!
748. [Umiejętność wroga [149609] (ulepszenie 1) — opis] [CantDuel]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149609].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel]
   PL: [CantDuel]
749. [Umiejętność wroga [149609] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>[NiddlePin]을 5 이상 보유한 대상에게 [NiddlePinned] 2 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149609].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [NiddlePin], [NiddlePinned]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NiddlePin] = 바늘못 / Naildle; [NiddlePinned] = 박제 상태 / Taxidermized
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Inflict 2 [NiddlePinned] against targets that have 5+ [NiddlePin]</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>nakłada 2 [NiddlePinned] na cele posiadające 5+ [NiddlePin]</u></b></mark></color>
750. [Umiejętność wroga [149610] (ulepszenie 1) — nazwa] 그냥… 쳐먹어!!!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149610].levelList[level=1].name
   limit: do 40 znaków
   EN: Just... Eat!!
   PL: Just... Eat!!
751. [Umiejętność wroga [149610] (ulepszenie 1) — opis] [NiddlePinned] 상태인 적 우선 공격\n- [NiddlePin] 수치가 가장 높은 대상 우선 공격\n[NiddlePin]을 5 이상 보유한 대상은 이 공격의 대상을 변경할 수 없음\n\n대상의 [NiddlePin] 1당 피해량 +10% (최대 50%)
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149610].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [NiddlePinned], [NiddlePin]
   znaczenie tagów: [NiddlePinned] = 박제 상태 / Taxidermized; [NiddlePin] = 바늘못 / Naildle
   EN: Prioritizes [NiddlePinned] enemies\n- Prioritizes targets that have the highest [NiddlePin] Stack\nTargets that have 5+ [NiddlePin] Stack cannot redirect this Skill to itself\n\nDeal +10% damage for every [NiddlePin] on target (max 50%)
   PL: priorytet: wrogowie z [NiddlePinned]\n- priorytet: cel z najwyższą wartością [NiddlePin]\ncele z 5+ wartością [NiddlePin] nie mogą przyciągnąć tej Umiejętności na siebie\n\nzadaje +10% obrażeń za każde 1 [NiddlePin] celu (maks. 50%)
752. [Umiejętność wroga [149610] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149610].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Umiejętność wroga [149610] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>대상이 [NiddlePinned]면 최대 체력의 99%만큼 고정 피해</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149610].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [NiddlePinned]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NiddlePinned] = 박제 상태 / Taxidermized
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>If target is [NiddlePinned], deal fixed damage equal to 99% of target's max HP</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma [NiddlePinned], zadaje obrażenia stałe równe 99% Maks. HP celu</u></b></mark></color>
754. [Umiejętność wroga [149610] (ulepszenie 1) — moneta 1, efekt 3 — opis] [EnemyKill] 자신의 최대 체력의 5%만큼 체력 회복
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149610].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Heal 5% HP on self
   PL: [EnemyKill] przywraca 5% HP tej jednostki
755. [Umiejętność wroga [148401] (ulepszenie 1) — nazwa] 흑…
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148401].levelList[level=1].name
   limit: do 40 znaków
   EN: Hrgh...
   PL: Hrgh...
756. [Umiejętność wroga [148401] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 2)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] 대상에게 [Laceration]이 없다면, 피해량 -80%, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨</u></b></mark></color>\n[WinDuel] 대상의 긍정적인 효과 무작위 1개 제거 (충전, 호흡 제외), 자신이 [Nutrition] 1 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148401].levelList[level=1].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Laceration], [SuperCoin], [WinDuel], [Nutrition]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WinDuel] = [합 승리시] / [Clash Win]; [Nutrition] = 탈취해낸 무언가. / A Seized Something.
   EN: [WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] If target does not have [Laceration], deal -80% damage and convert all Coins on this Skill to [SuperCoin]s</u></b></mark></color>\n[WinDuel] Remove 1 random positive effect on target (excluding Charge and Poise); then, gain 1 [Nutrition]
   PL: [WhenUse] Moc Końcowa +1 za każde 4 [Laceration] celu (maks. 2)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] jeżeli cel nie ma [Laceration], zadaje -80% obrażeń, a wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y</u></b></mark></color>\n[WinDuel] usuwa 1 losowy pozytywny efekt celu (poza Ładowaniem i Równowagą), po czym zyskuje 1 [Nutrition]
757. [Umiejętność wroga [148401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [Umiejętność wroga [148401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BloodyMucus] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloodyMucus]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodyMucus] = 세례[적] / Baptism [Crimson]
   EN: [OnSucceedAttack] Inflict 2 [BloodyMucus]
   PL: [OnSucceedAttack] nakłada 2 [BloodyMucus]
759. [Umiejętność wroga [148402] (ulepszenie 1) — nazwa] 흐윽…
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148402].levelList[level=1].name
   limit: do 40 znaków
   EN: Nngh...
   PL: Nngh...
760. [Umiejętność wroga [148402] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 2)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] 대상에게 [Laceration]이 없다면, 피해량 -80%, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148402].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Laceration], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] If target does not have [Laceration], deal -80% damage and convert all Coins on this Skill to [SuperCoin]s</u></b></mark></color>
   PL: [WhenUse] Moc Końcowa +1 za każde 4 [Laceration] celu (maks. 2)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] jeżeli cel nie ma [Laceration], zadaje -80% obrażeń, a wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y</u></b></mark></color>
761. [Umiejętność wroga [148402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Umiejętność wroga [148402] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloodyMucus]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodyMucus] = 세례[적] / Baptism [Crimson]
   EN: [OnSucceedAttack] Inflict 1 [BloodyMucus]
   PL: [OnSucceedAttack] nakłada 1 [BloodyMucus]
763. [Umiejętność wroga [148402] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 긍정적인 효과 무작위 1개 제거 (충전, 호흡 제외), 자신이 [Nutrition] 1 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148402].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Nutrition]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Nutrition] = 탈취해낸 무언가. / A Seized Something.
   EN: [OnSucceedAttack] Remove 1 random positive effect on target (excluding Charge and Poise) to gain 1 [Nutrition]
   PL: [OnSucceedAttack] usuwa 1 losowy pozytywny efekt celu (poza Ładowaniem i Równowagą), aby zyskać 1 [Nutrition]
764. [Umiejętność wroga [148402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Umiejętność wroga [148402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Umiejętność wroga [148403] (ulepszenie 1) — nazwa] 뿌…페…
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148403].levelList[level=1].name
   limit: do 40 znaków
   EN: Pw... ffeh...
   PL: Pw... ffeh...
767. [Umiejętność wroga [148403] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 [Laceration] 4당, 최종 위력 +1 (최대 3)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] 메인 타겟에게 [Laceration]이 없다면, 피해량 -80%, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148403].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Laceration], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Final Power +1 for every 4 [Laceration] on the main target (max 3)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] If the main target does not have [Laceration], deal -80% damage and convert all Coins on this Skill to [SuperCoin]s</u></b></mark></color>
   PL: [WhenUse] Moc Końcowa +1 za każde 4 [Laceration] głównego celu (maks. 3)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] jeżeli główny cel nie ma [Laceration], zadaje -80% obrażeń, a wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y</u></b></mark></color>
768. [Umiejętność wroga [148403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Umiejętność wroga [148403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Umiejętność wroga [148403] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 긍정적인 효과 무작위 1개 제거 (충전, 호흡 제외), 자신이 [Nutrition] 1 얻음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148403].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 763 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Umiejętność wroga [148403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [Umiejętność wroga [148403] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148403].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Umiejętność wroga [148404] (ulepszenie 1) — nazwa] 추..워…
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148404].levelList[level=1].name
   limit: do 40 znaków
   EN: It's... cold...
   PL: It's... cold...
774. [Umiejętność wroga [148404] (ulepszenie 1) — opis] 체력이 가장 낮은 대상을 우선으로 지정\n대상의 잃은 체력 1%당, 피해량 +5% (최대 250%)\n[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +2 (최대 4)\n[WhenUse] 대상의 현재 체력이 50% 미만이면, 기본 위력 +3\n[WinDuel] 대상의 긍정적인 효과 무작위 1개 제거 (충전, 호흡 제외), 자신이 [Nutrition] 2 얻음\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148404].levelList[level=1].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [WinDuel], [Nutrition], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [Nutrition] = 탈취해낸 무언가. / A Seized Something.; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritize targets that have the lowest current HP\nDeal +5% damage for every 1% missing HP on target (max 250%)\n[WhenUse] Final Power +2 for every 4 [Laceration] on target (max 4)\n[WhenUse] If target has lower than 50% HP, Base Power +3\n[WinDuel] Remove 1 random positive effect on target (excluding Charge and Poise) to gain 2 [Nutrition]\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: priorytet: cel z najniższym aktualnym HP\nzadaje +5% obrażeń za każde 1% utraconego HP celu (maks. 250%)\n[WhenUse] Moc Końcowa +2 za każde 4 [Laceration] celu (maks. 4)\n[WhenUse] jeżeli aktualne HP celu jest niższe niż 50%, Moc Bazowa +3\n[WinDuel] usuwa 1 losowy pozytywny efekt celu (poza Ładowaniem i Równowagą), aby zyskać 2 [Nutrition]\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
775. [Umiejętność wroga [148404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [Umiejętność wroga [148404] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148404].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Umiejętność wroga [148404] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148404].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Umiejętność wroga [148404] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [BloodyMucus] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148404].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [BloodyMucus]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [BloodyMucus] = 세례[적] / Baptism [Crimson]
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [BloodyMucus]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [BloodyMucus]
779. [Umiejętność wroga [148405] (ulepszenie 1) — nazwa] 아파…! 몸이… 제 멋대로…!!!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].name
   limit: do 60 znaków
   EN: It hurts...! My body... won't listen...
   PL: It hurts...! My body... won't listen...
780. [Umiejętność wroga [148405] (ulepszenie 1) — opis] 체력이 가장 낮은 대상을 메인 타겟으로 우선 지정\n대상의 잃은 체력 3%당, 피해량 +5% (최대 50%)\n[WhenUse] 메인 타겟의 [Laceration] 4당, 최종 위력 +2 (최대 4)\n[WhenUse] 메인 타겟의 현재 체력이 50% 미만이면, 기본 위력 +2\n[WinDuel] 메인 타겟의 긍정적인 효과 무작위 1개 제거 (충전, 호흡 제외), 자신이 [Nutrition] 2 얻음\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [WinDuel], [Nutrition], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [Nutrition] = 탈취해낸 무언가. / A Seized Something.; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritize targets that have the lowest current HP as the main target\nDeal +5% damage for every 3% missing HP on target (max 50%)\n[WhenUse] Final Power +2 for every 4 [Laceration] on the main target (max 4)\n[WhenUse] If the main target has lower than 50% HP, Base Power +2\n[WinDuel] Remove 1 random positive effect on the main target (excluding Charge and Poise) to gain 2 [Nutrition]\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: priorytet: cel z najniższym aktualnym HP jako główny cel\nzadaje +5% obrażeń za każde 3% utraconego HP celu (maks. 50%)\n[WhenUse] Moc Końcowa +2 za każde 4 [Laceration] głównego celu (maks. 4)\n[WhenUse] jeżeli aktualne HP głównego celu jest niższe niż 50%, Moc Bazowa +2\n[WinDuel] usuwa 1 losowy pozytywny efekt głównego celu (poza Ładowaniem i Równowagą), aby zyskać 2 [Nutrition]\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
781. [Umiejętność wroga [148405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Umiejętność wroga [148405] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Umiejętność wroga [148405] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Umiejętność wroga [148405] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [BloodyMucus]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [BloodyMucus] = 세례[적] / Baptism [Crimson]
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [BloodyMucus]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [BloodyMucus]
785. [Umiejętność wroga [148405] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Umiejętność wroga [148405] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Umiejętność wroga [148405] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [Umiejętność wroga [148405] (ulepszenie 1) — moneta 2, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 784 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Umiejętność wroga [148405] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Umiejętność wroga [148405] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Umiejętność wroga [148405] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Umiejętność wroga [148405] (ulepszenie 1) — moneta 3, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148405].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 784 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Umiejętność wroga [148406] (ulepszenie 1) — nazwa] 배고파… 추워… 아파…!
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].name
   limit: do 40 znaków
   EN: Hungry... cold... hurts...!
   PL: Hungry... cold... hurts...!
794. [Umiejętność wroga [148406] (ulepszenie 1) — opis] 체력이 가장 낮은 대상을 메인 타겟으로 우선 지정\n대상의 잃은 체력 1%당, 피해량 +1% (최대 30%)\n[WhenUse] 메인 타겟의 [Laceration] 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 메인 타겟의 현재 체력이 50% 미만이면, 기본 위력 +2\n[WhenUse] 자신의 [ChargeRouge] 횟수가 10 이상이면, [ChargeRouge] 횟수를 모두 소모하고 코인 위력 +2, 가중치 +2\n[DefeatDuel] 피해량 -95%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [ChargeRouge], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeRouge] = 맥동 / Pulsation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritize targets that have the lowest current HP as the main target\nDeal +1% damage for every 1% missing HP on target (max 30%)\n[WhenUse] Coin Power +1 for every 6 [Laceration] on the main target (max 2)\n[WhenUse] If the main target has lower than 50% HP, Base Power +2\n[WhenUse] At 10+ [ChargeRouge] Count, consume all [ChargeRouge] on self and gain Coin Power +2 and +2 Atk Weight\n[DefeatDuel] Deal -95% damage and damage dealt by this Skill cannot Stagger the target
   PL: priorytet: cel z najniższym aktualnym HP jako główny cel\nzadaje +1% obrażeń za każde 1% utraconego HP celu (maks. 30%)\n[WhenUse] Moc Monety +1 za każde 6 [Laceration] głównego celu (maks. 2)\n[WhenUse] jeżeli aktualne HP głównego celu jest niższe niż 50%, Moc Bazowa +2\n[WhenUse] przy 10+ Licznika [ChargeRouge] zużywa wszystkie Liczniki [ChargeRouge] i zyskuje Moc Monety +2 oraz Wagę Ataku +2\n[DefeatDuel] zadaje -95% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
795. [Umiejętność wroga [148406] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Umiejętność wroga [148406] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Umiejętność wroga [148406] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 6 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 6 [Laceration]
798. [Umiejętność wroga [148406] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Umiejętność wroga [148406] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 784 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Umiejętność wroga [148406] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Activate [Laceration] on target once. Target loses 1 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] aktywuje [Laceration] na celu 1 raz. Cel traci 1 Licznika [Laceration]
801. [Umiejętność wroga [148406] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Umiejętność wroga [148406] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 784 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Umiejętność wroga [148406] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 800 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Umiejętność wroga [148406] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Umiejętność wroga [148406] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 784 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [Umiejętność wroga [148406] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148406].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 800 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Umiejętność wroga [148407] (ulepszenie 1) — nazwa] 저..리가…
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148407].levelList[level=1].name
   limit: do 40 znaków
   EN: Go... away...
   PL: Go... away...
808. [Umiejętność wroga [148407] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 2)\n[WinDuel] 자신의 [ChargeRouge] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148407].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [WinDuel], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)\n[WinDuel] Gain +3 [ChargeRouge] Count
   PL: [WhenUse] Moc Końcowa +1 za każde 4 [Laceration] celu (maks. 2)\n[WinDuel] zyskuje 3 Licznika [ChargeRouge]
809. [Umiejętność wroga [148407] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148407].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Umiejętność wroga [148407] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148407].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Umiejętność wroga [148408] (ulepszenie 1) — nazwa] 배…고파…
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148408].levelList[level=1].name
   limit: do 40 znaków
   EN: I'm... hungry...
   PL: I'm... hungry...
812. [Umiejętność wroga [148408] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 2)\n[WinDuel] 자신의 [ChargeRouge] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148408].levelList[level=1].desc
   (powtórzenie elementu 808 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [Umiejętność wroga [148408] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148408].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Umiejętność wroga [148408] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148408].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Umiejętność wroga [148408] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148408].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [Umiejętność wroga [148409] (ulepszenie 1) — nazwa] 뭐라도… 먹고…싶어…
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148409].levelList[level=1].name
   limit: do 50 znaków
   EN: Something... to eat... Anything...
   PL: Something... to eat... Anything...
817. [Umiejętność wroga [148409] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 [Laceration] 4당, 최종 위력 +1 (최대 2)\n[WinDuel] 자신의 [ChargeRouge] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148409].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [WinDuel], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] Final Power +1 for every 4 [Laceration] on the main target (max 2)\n[WinDuel] Gain +3 [ChargeRouge] Count
   PL: [WhenUse] Moc Końcowa +1 za każde 4 [Laceration] głównego celu (maks. 2)\n[WinDuel] zyskuje 3 Licznika [ChargeRouge]
818. [Umiejętność wroga [148409] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148409].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Umiejętność wroga [148409] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148409].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [Umiejętność wroga [148410] (ulepszenie 1) — nazwa] 목소리가 들려…
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148410].levelList[level=1].name
   limit: do 40 znaków
   EN: I hear... the Voice...
   PL: I hear... the Voice...
821. [Umiejętność wroga [148410] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 [Laceration] 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeRouge] 횟수가 15 미만이면, 15까지 증가하고 증가한 수치 5당 다음 턴에 [BuffetFailed] 1 얻음\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148410].levelList[level=1].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [ChargeRouge], [BuffetFailed], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeRouge] = 맥동 / Pulsation; [BuffetFailed] = 탈진 / Exhausted; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Coin Power +1 for every 6 [Laceration] on the main target (max 2)\n[WhenUse] At fewer than 15 [ChargeRouge] Count, gain up to 15 [ChargeRouge] Count and gain 1 [BuffetFailed] next turn for every 5 [ChargeRouge] Count gained from this effect\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Monety +1 za każde 6 [Laceration] głównego celu (maks. 2)\n[WhenUse] przy mniej niż 15 Licznika [ChargeRouge] zyskuje Liczniki [ChargeRouge] do 15 i 1 [BuffetFailed] w następnej turze za każde 5 zyskanych Liczników [ChargeRouge] z tego efektu\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
822. [Umiejętność wroga [148410] (ulepszenie 1) — tekst klimatyczny] 백화점에는 여러 목소리가 있다. 누구의 목소리일까.
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148410].levelList[level=1].flavor
   limit: do 120 znaków
   EN: Many Voices inhabit this department store. Whose could this be?
   PL: W domu towarowym mieszka wiele Głosów. Czyj to może być?
823. [Umiejętność wroga [148410] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148410].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
824. [Umiejętność wroga [148410] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148410].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Umiejętność wroga [148410] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148410].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Umiejętność wroga [148410] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148410].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Umiejętność wroga [148410] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148410].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [Umiejętność wroga [148410] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148410].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Umiejętność wroga [148411] (ulepszenie 1) — nazwa] 하..지마…
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148411].levelList[level=1].name
   limit: do 40 znaków
   EN: Don't... do that...
   PL: Don't... do that...
830. [Umiejętność wroga [148411] (ulepszenie 1) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n[WhenUse] 자신의 ([ChargeRouge] 횟수 x 10)만큼 보호막 얻음\n[WinDuel] 자신의 [ChargeRouge] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148411].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [SupportProtect], [WhenUse], [ChargeRouge], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n[SupportProtect] Exclusive Skill\n[WhenUse] Gain ([ChargeRouge] Count on self x 10) Shield\n[WinDuel] Gain +3 [ChargeRouge] Count
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [SupportProtect]\n[WhenUse] zyskuje Tarczę równą (Licznik [ChargeRouge] tej jednostki x 10)\n[WinDuel] zyskuje 3 Licznika [ChargeRouge]
831. [Umiejętność wroga [148411] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148411].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [Umiejętność wroga [148412] (ulepszenie 1) — nazwa] 하…고…싶어
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148412].levelList[level=1].name
   limit: do 40 znaków
   EN: I... wanna...
   PL: I... wanna...
833. [Umiejętność wroga [148412] (ulepszenie 1) — opis] 자신의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WhenUse] 메인 타겟의 [Laceration] 4당, 최종 위력 +2 (최대 4)\n[DefeatDuel] 자신의 [ChargeRouge] 횟수 2 감소\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148412].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [DefeatDuel], [ChargeRouge]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [ChargeRouge] = 맥동 / Pulsation
   EN: At 6+ [Laceration], Coin Power +1\n[WhenUse] Final Power +2 for every 4 [Laceration] on the main target (max 4)\n[DefeatDuel] Lose 2 [ChargeRouge] Count\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: przy 6+ wartości [Laceration] tej jednostki Moc Monety +1\n[WhenUse] Moc Końcowa +2 za każde 4 [Laceration] głównego celu (maks. 4)\n[DefeatDuel] traci 2 Licznika [ChargeRouge]\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
834. [Umiejętność wroga [148412] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148412].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
835. [Umiejętność wroga [148412] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148412].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [Umiejętność wroga [148412] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148412].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Umiejętność wroga [148412] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148412].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Umiejętność wroga [148412] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148412].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Umiejętność wroga [148412] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148412].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Umiejętność wroga [148413] (ulepszenie 1) — nazwa] 난…뭐야…?
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148413].levelList[level=1].name
   limit: do 40 znaków
   EN: What... am I...?
   PL: What... am I...?
841. [Umiejętność wroga [148413] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 [Laceration] 4당, 최종 위력 +1 (최대 3)\n[WhenUse] 자신의 [ChargeRouge] 횟수가 10 이상이면, [ChargeRouge] 횟수를 10 소모하고 코인 위력 +2\n[DefeatDuel] 피해량 -80%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148413].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [ChargeRouge], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeRouge] = 맥동 / Pulsation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Final Power +1 for every 4 [Laceration] on the main target (max 3)\n[WhenUse] At 10+ [ChargeRouge] Count, consume 10 [ChargeRouge] Count to gain Coin Power +2\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Końcowa +1 za każde 4 [Laceration] głównego celu (maks. 3)\n[WhenUse] przy 10+ Licznika [ChargeRouge] zużywa 10 Licznika [ChargeRouge], aby zyskać Moc Monety +2\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
842. [Umiejętność wroga [148413] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148413].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Umiejętność wroga [148413] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148413].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Umiejętność wroga [148413] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148413].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Umiejętność wroga [148413] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148413].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
846. [Umiejętność wroga [148413] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148413].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Umiejętność wroga [148413] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Binding] 4 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=148413].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 4 [Binding] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 4 [Binding] w następnej turze
848. [Umiejętność wroga [149701] (ulepszenie 1) — nazwa] 늘어진 손짓
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149701].levelList[level=1].name
   limit: do 40 znaków
   EN: Feeble Beckoning
   PL: Feeble Beckoning
849. [Umiejętność wroga [149701] (ulepszenie 1) — tekst klimatyczny] …손 잡아줘
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149701].levelList[level=1].flavor
   limit: do 120 znaków
   EN: ... Hold my hand
   PL: ... Hold my hand
850. [Umiejętność wroga [149701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Umiejętność wroga [149701] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149701].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
852. [Umiejętność wroga [149701] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [BloodyMucus] 1 부여
   źródło: Skills_Abnormality-a1c10p1.json :: dataList[id=149701].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 784 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c10p1] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c10p1
- grupa rozdziału/trybu: `a1c10p1` · plik: `Skills_Enemy-a1c10p1.json`

853. [Umiejętność wroga [9105901] (ulepszenie 1) — nazwa] 때리기
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105901].levelList[level=1].name
   limit: do 40 znaków
   EN: Batter
   PL: Batter
854. [Umiejętność wroga [9105901] (ulepszenie 1) — opis] 대상의 [Vibration]이 4 이상이면, 최종 위력 +1
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 4+ [Vibration], Final Power +1
   PL: jeżeli cel ma 4+ [Vibration], Moc Końcowa +1
855. [Umiejętność wroga [9105901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
856. [Umiejętność wroga [9105902] (ulepszenie 1) — nazwa] 몸통 박치기
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105902].levelList[level=1].name
   limit: do 40 znaków
   EN: Body Slam
   PL: Body Slam
857. [Umiejętność wroga [9105902] (ulepszenie 1) — opis] 대상의 [Vibration]이 4 이상이면, 최종 위력 +1
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105902].levelList[level=1].desc
   (powtórzenie elementu 854 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
858. [Umiejętność wroga [9105902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Umiejętność wroga [9105902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [Umiejętność wroga [9105902] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신에게 [Laceration]이 있으면, 수치 위력 절반만큼 대상에게 [Laceration] 횟수 부여 (최대 5, 턴당 1회, 소수점 버림)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If this unit has [Laceration], inflict ([Laceration] Potency on self / 2) [Laceration] Count on target (max 5; once per turn; rounded down)
   PL: [OnSucceedAttack] jeżeli ta jednostka ma [Laceration], nakłada (Siła [Laceration] tej jednostki / 2) Liczników [Laceration] na cel (maks. 5, 1 raz na turę, zaokrąglone w dół)
861. [Umiejętność wroga [9105903] (ulepszenie 1) — nazwa] 내리찍기
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105903].levelList[level=1].name
   limit: do 40 znaków
   EN: Slam Down
   PL: Slam Down
862. [Umiejętność wroga [9105903] (ulepszenie 1) — opis] 대상의 [Vibration]이 4 이상이면, 최종 위력 +1\n[WhenUse] 자신의 [Laceration]당 피해량 +1% (최대 20%)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105903].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [WhenUse], [Laceration]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: If target has 4+ [Vibration], Final Power +1\n[WhenUse] Deal +1% damage for every [Laceration] on self (max 20%)
   PL: jeżeli cel ma 4+ [Vibration], Moc Końcowa +1\n[WhenUse] zadaje +1% obrażeń za każde 1 [Laceration] tej jednostki (maks. 20%)
863. [Umiejętność wroga [9105903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
864. [Umiejętność wroga [9105903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Umiejętność wroga [9105903] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105903].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
866. [Umiejętność wroga [9105903] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [Laceration]이 있으면, 수치 위력만큼 대상에게 [Laceration] 횟수 부여 (최대 8, 턴당 1회)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105903].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] If this unit has [Laceration], inflict ([Laceration] Potency on self) [Laceration] Count on target (max 8; once per turn)
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli ta jednostka ma [Laceration], nakłada Liczniki [Laceration] na cel równe Siły [Laceration] tej jednostki (maks. 8, 1 raz na turę)
867. [Umiejętność wroga [9105903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
868. [Umiejętność wroga [9105903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Umiejętność wroga [9105904] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105904].levelList[level=1].name
   limit: do 40 znaków
   EN: Guard
   PL: Guard
870. [Umiejętność wroga [9105904] (ulepszenie 1) — opis] [StartBattle] 정신력 5 회복\n[StartBattle] 다음 턴에 [ResultEnhancement] 1 얻음
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9105904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [ResultEnhancement]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ResultEnhancement] = 위력 증가 / Power Up
   EN: [StartBattle] Heal 5 SP\n[StartBattle] Gain 1 [ResultEnhancement] next turn
   PL: [StartBattle] przywraca 5 SP\n[StartBattle] zyskuje 1 [ResultEnhancement] w następnej turze
871. [Umiejętność wroga [9106001] (ulepszenie 1) — nazwa] 치기
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106001].levelList[level=1].name
   limit: do 40 znaków
   EN: Strike
   PL: Strike
872. [Umiejętność wroga [9106001] (ulepszenie 1) — opis] 대상의 [Vibration]이 4 이상이면, 최종 위력 +1
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106001].levelList[level=1].desc
   (powtórzenie elementu 854 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
873. [Umiejętność wroga [9106001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
874. [Umiejętność wroga [9106002] (ulepszenie 1) — nazwa] 몸통 밀치기
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106002].levelList[level=1].name
   limit: do 40 znaków
   EN: Body Check
   PL: Body Check
875. [Umiejętność wroga [9106002] (ulepszenie 1) — opis] 대상의 [Vibration]이 4 이상이면, 최종 위력 +1
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106002].levelList[level=1].desc
   (powtórzenie elementu 854 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
876. [Umiejętność wroga [9106002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [Umiejętność wroga [9106002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
878. [Umiejętność wroga [9106002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신에게 [Laceration]이 있으면, 수치 위력 절반만큼 대상에게 [Laceration] 횟수 부여 (최대 5, 턴당 1회, 소수점 버림)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 860 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Umiejętność wroga [9106003] (ulepszenie 1) — nazwa] 내려치기
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106003].levelList[level=1].name
   limit: do 40 znaków
   EN: Slam Down
   PL: Slam Down
880. [Umiejętność wroga [9106003] (ulepszenie 1) — opis] 대상의 [Vibration]이 4 이상이면, 최종 위력 +1\n[WhenUse] 자신의 [Laceration]당 피해량 +1% (최대 20%)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106003].levelList[level=1].desc
   (powtórzenie elementu 862 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [Umiejętność wroga [9106003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
882. [Umiejętność wroga [9106003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [Umiejętność wroga [9106003] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106003].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
884. [Umiejętność wroga [9106003] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [Laceration]이 있으면, 수치 위력만큼 대상에게 [Laceration] 횟수 부여 (최대 8, 턴당 1회)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106003].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 866 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
885. [Umiejętność wroga [9106003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
886. [Umiejętność wroga [9106003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [Umiejętność wroga [9106004] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106004].levelList[level=1].name
   (powtórzenie elementu 869 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
888. [Umiejętność wroga [9106004] (ulepszenie 1) — opis] [StartBattle] 정신력 5 회복\n[StartBattle] 다음 턴에 [ResultEnhancement] 1 얻음
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106004].levelList[level=1].desc
   (powtórzenie elementu 870 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [Umiejętność wroga [9106601] (ulepszenie 1) — nazwa] 건드리지 마…!
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106601].levelList[level=1].name
   limit: do 40 znaków
   EN: Don't touch me...!
   PL: Don't touch me...!
890. [Umiejętność wroga [9106601] (ulepszenie 1) — opis] [WhenUse]\n- 대상의 [Vibration]이 6 이상이면, 코인 위력 +1\n- 자신의 [ChargeNoir] 횟수가 10 이상이면, 코인 위력 +1\n\n[WhenUse] 자신의 [ChargeNoir] 횟수 2 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106601].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [ChargeNoir]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [ChargeNoir] = 보존 / Preservation
   EN: [WhenUse]\n- If target has 6+ [Vibration], Coin Power +1\n- At 10+ [ChargeNoir] Count, Coin Power +1\n\n[WhenUse] Gain +2 [ChargeNoir] Count
   PL: [WhenUse]\n- jeżeli cel ma 6+ [Vibration], Moc Monety +1\n- przy 10+ Licznika [ChargeNoir] Moc Monety +1\n\n[WhenUse] zyskuje 2 Licznika [ChargeNoir]
891. [Umiejętność wroga [9106601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
892. [Umiejętność wroga [9106601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [Umiejętność wroga [9106601] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [ChargeNoir] 횟수 2 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106601].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoir]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +2 [ChargeNoir] Count
   PL: [OnSucceedAttack] zyskuje 2 Licznika [ChargeNoir]
894. [Umiejętność wroga [9106602] (ulepszenie 1) — nazwa] 손대지 마…!
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106602].levelList[level=1].name
   limit: do 40 znaków
   EN: Get your hands off me...!
   PL: Get your hands off me...!
895. [Umiejętność wroga [9106602] (ulepszenie 1) — opis] [WhenUse]\n- 대상의 [Vibration]이 6 이상이면, 코인 위력 +1\n- 자신의 [ChargeNoir] 횟수가 10 이상이면, 코인 위력 +1\n\n[WhenUse] 자신의 [ChargeNoir] 횟수 4 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106602].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [ChargeNoir]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [ChargeNoir] = 보존 / Preservation
   EN: [WhenUse]\n- If target has 6+ [Vibration], Coin Power +1\n- At 10+ [ChargeNoir] Count, Coin Power +1\n\n[WhenUse] Gain +4 [ChargeNoir] Count
   PL: [WhenUse]\n- jeżeli cel ma 6+ [Vibration], Moc Monety +1\n- przy 10+ Licznika [ChargeNoir] Moc Monety +1\n\n[WhenUse] zyskuje 4 Licznika [ChargeNoir]
896. [Umiejętność wroga [9106602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 2 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 648 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
897. [Umiejętność wroga [9106602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Umiejętność wroga [9106602] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106602].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [Umiejętność wroga [9106603] (ulepszenie 1) — nazwa] 아무것도 하면 안 된다고…!
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106603].levelList[level=1].name
   limit: do 50 znaków
   EN: We shouldn't be doing anything...!
   PL: We shouldn't be doing anything...!
900. [Umiejętność wroga [9106603] (ulepszenie 1) — opis] 자신의 [ChargeNoir] 위력당 피해량 +4% (최대 20%)\n\n[WhenUse] 자신의 [ChargeNoir] 횟수가 10 이상이면, [ChargeNoir] 횟수 10을 소모하여 코인 위력 +1, 피해량 +20%
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106603].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir], [WhenUse]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]
   EN: Deal +4% damage for every [ChargeNoir] Potency on self (max 20%)\n\n[WhenUse] At 10+ [ChargeNoir] Count, consume 10 [ChargeNoir] Count to gain Coin Power +1 and deal +20% damage
   PL: zadaje +4% obrażeń za każde 1 Siły [ChargeNoir] tej jednostki (maks. 20%)\n\n[WhenUse] przy 10+ Licznika [ChargeNoir] zużywa 10 Licznika [ChargeNoir], aby zyskać Moc Monety +1 i zadać +20% obrażeń
901. [Umiejętność wroga [9106603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [Umiejętność wroga [9106603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
903. [Umiejętność wroga [9106603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 653 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
904. [Umiejętność wroga [9106603] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106603].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [Umiejętność wroga [9106101] (ulepszenie 1) — nazwa] 뒤지기
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106101].levelList[level=1].name
   limit: do 40 znaków
   EN: Rummage
   PL: Rummage
906. [Umiejętność wroga [9106101] (ulepszenie 1) — opis] 대상의 [Laceration]이 6 이상이면, 최종 위력 +1
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration], Final Power +1
   PL: jeżeli cel ma 6+ [Laceration], Moc Końcowa +1
907. [Umiejętność wroga [9106101] (ulepszenie 1) — tekst klimatyczny] 있을 텐데… 뭔가 있을 텐데…
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106101].levelList[level=1].flavor
   limit: do 120 znaków
   EN: There has to be something here... something worth finding...
   PL: Tu musi być coś... coś, co warto znaleźć...
908. [Umiejętność wroga [9106101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
909. [Umiejętność wroga [9106102] (ulepszenie 1) — nazwa] 잡아뺏기
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106102].levelList[level=1].name
   limit: do 40 znaków
   EN: Snatch Up
   PL: Snatch Up
910. [Umiejętność wroga [9106102] (ulepszenie 1) — opis] 대상의 [Laceration] 3당, 최종 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Final Power +1 for every 3 [Laceration] on target (max 2)
   PL: Moc Końcowa +1 za każde 3 [Laceration] celu (maks. 2)
911. [Umiejętność wroga [9106102] (ulepszenie 1) — tekst klimatyczny] 이건 내 거야!
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106102].levelList[level=1].flavor
   limit: do 120 znaków
   EN: This one's mine!
   PL: This one's mine!
912. [Umiejętność wroga [9106102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
913. [Umiejętność wroga [9106102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
914. [Umiejętność wroga [9106102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict 2 [Laceration]
   PL: [CriticalOnSucceedAttack] nakłada 2 [Laceration]
915. [Umiejętność wroga [9106103] (ulepszenie 1) — nazwa] 찾았다!
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106103].levelList[level=1].name
   limit: do 40 znaków
   EN: Got one!
   PL: Got one!
916. [Umiejętność wroga [9106103] (ulepszenie 1) — opis] 대상의 [Laceration] 3당, 최종 위력 +1 (최대 3)\n[WhenUse] 자신의 체력이 50% 미만이거나, 대상의 [Laceration]이 10 이상이면, 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106103].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [SuperCoin]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Final Power +1 for every 3 [Laceration] on target (max 3)\n[WhenUse] At lower than 50% HP, or if target has 10+ [Laceration], convert all Coins to [SuperCoin]s
   PL: Moc Końcowa +1 za każde 3 [Laceration] celu (maks. 3)\n[WhenUse] przy HP tej jednostki poniżej 50% Maks. HP lub jeżeli cel ma 10+ [Laceration], wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y
917. [Umiejętność wroga [9106103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
918. [Umiejętność wroga [9106103] (ulepszenie 1) — moneta 2, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +30% damage on Critical Hit
   PL: +30% obrażeń krytycznych
919. [Umiejętność wroga [9106103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
920. [Umiejętność wroga [9106103] (ulepszenie 1) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106103].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 914 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
921. [Umiejętność wroga [9106104] (ulepszenie 1) — nazwa] 어딜! 이건 내거야!
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106104].levelList[level=1].name
   limit: do 40 znaków
   EN: Nah, man! That one's mine!
   PL: Nah, man! That one's mine!
922. [Umiejętność wroga [9106104] (ulepszenie 1) — opis] [WhenUse] 대상이 보유한 효과 2개당, [Breath] 2 얻음 (최대 5)\n[WhenUse] 대상이 보유한 효과가 4개 이상이면, 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106104].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 2 [Breath] for every 2 types of effect on target (max 5)\n[WhenUse] If target has 4+ effects, gain +1 [Breath] Count
   PL: [WhenUse] zyskuje 2 [Breath] za każde 2 rodzaje efektów celu (maks. 5)\n[WhenUse] jeżeli cel ma 4+ efektów, zyskuje 1 Licznika [Breath]
923. [Umiejętność wroga [9106104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
924. [Umiejętność wroga [9106104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
925. [Umiejętność wroga [9106201] (ulepszenie 1) — nazwa] 뒤지기
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106201].levelList[level=1].name
   (powtórzenie elementu 905 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [Umiejętność wroga [9106201] (ulepszenie 1) — opis] 대상의 [Laceration]이 6 이상이면, 최종 위력 +1
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106201].levelList[level=1].desc
   (powtórzenie elementu 906 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
927. [Umiejętność wroga [9106201] (ulepszenie 1) — tekst klimatyczny] 있을 텐데… 뭔가 있을 텐데…
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106201].levelList[level=1].flavor
   (powtórzenie elementu 907 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
928. [Umiejętność wroga [9106201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
929. [Umiejętność wroga [9106202] (ulepszenie 1) — nazwa] 잡아뺏기
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106202].levelList[level=1].name
   (powtórzenie elementu 909 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
930. [Umiejętność wroga [9106202] (ulepszenie 1) — opis] 대상의 [Laceration] 3당, 최종 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106202].levelList[level=1].desc
   (powtórzenie elementu 910 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
931. [Umiejętność wroga [9106202] (ulepszenie 1) — tekst klimatyczny] 이건 내 거야!
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106202].levelList[level=1].flavor
   (powtórzenie elementu 911 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
932. [Umiejętność wroga [9106202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
933. [Umiejętność wroga [9106202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
934. [Umiejętność wroga [9106202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 914 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
935. [Umiejętność wroga [9106203] (ulepszenie 1) — nazwa] 찾았다!
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106203].levelList[level=1].name
   (powtórzenie elementu 915 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
936. [Umiejętność wroga [9106203] (ulepszenie 1) — opis] 대상의 [Laceration] 3당, 최종 위력 +1 (최대 3)\n[WhenUse] 자신의 체력이 50% 미만이거나, 대상의 [Laceration]이 10 이상이면, 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106203].levelList[level=1].desc
   (powtórzenie elementu 916 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
937. [Umiejętność wroga [9106203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
938. [Umiejętność wroga [9106203] (ulepszenie 1) — moneta 2, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 918 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
939. [Umiejętność wroga [9106203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
940. [Umiejętność wroga [9106203] (ulepszenie 1) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106203].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 914 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
941. [Umiejętność wroga [9106204] (ulepszenie 1) — nazwa] 어딜! 이건 내거야!
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106204].levelList[level=1].name
   (powtórzenie elementu 921 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
942. [Umiejętność wroga [9106204] (ulepszenie 1) — opis] [WhenUse] 대상이 보유한 효과 2개당, [Breath] 2 얻음 (최대 5)\n[WhenUse] 대상이 보유한 효과가 4개 이상이면, 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106204].levelList[level=1].desc
   (powtórzenie elementu 922 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
943. [Umiejętność wroga [9106204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
944. [Umiejętność wroga [9106204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [Umiejętność wroga [9106301] (ulepszenie 1) — nazwa] 홈질 - 날실
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106301].levelList[level=1].name
   limit: do 40 znaków
   EN: Running Stitch - Warp
   PL: Running Stitch - Warp
946. [Umiejętność wroga [9106301] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면, 최종 위력 +1\n\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 모든 코인이 [SuperCoin]이 됨
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106301].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [SuperCoin]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: If target has 4+ [Laceration], Final Power +1\n\n[WhenUse] If target has 6+ [Laceration], convert all Coins to [SuperCoin]s
   PL: jeżeli cel ma 4+ [Laceration], Moc Końcowa +1\n\n[WhenUse] jeżeli cel ma 6+ [Laceration], wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y
947. [Umiejętność wroga [9106301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
948. [Umiejętność wroga [9106301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [PenetrateResistDown] 1 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenetrateResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateResistDown] = 관통 내성 약화 / Pierce Resist Down
   EN: [OnSucceedAttack] Inflict 1 [PenetrateResistDown] next turn
   PL: [OnSucceedAttack] nakłada 1 [PenetrateResistDown] w następnej turze
949. [Umiejętność wroga [9106302] (ulepszenie 1) — nazwa] 시침질 - 날실
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106302].levelList[level=1].name
   limit: do 40 znaków
   EN: Tacking Stitch - Warp
   PL: Tacking Stitch - Warp
950. [Umiejętność wroga [9106302] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면, 최종 위력 +1
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 4+ [Laceration], Final Power +1
   PL: jeżeli cel ma 4+ [Laceration], Moc Końcowa +1
951. [Umiejętność wroga [9106302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
952. [Umiejętność wroga [9106302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [NiddlePin] 1 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 718 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
953. [Umiejętność wroga [9106302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
954. [Umiejętność wroga [9106303] (ulepszenie 1) — nazwa] 박음질 - 날실
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106303].levelList[level=1].name
   limit: do 40 znaków
   EN: Backstitch - Warp
   PL: Backstitch - Warp
955. [Umiejętność wroga [9106303] (ulepszenie 1) — opis] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n\n[WhenUse] 대상의 [Laceration]당 피해량 +1% (최대 20%)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106303].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: Final Power +1 for every 4 [Laceration] on target (max 2)\n\n[WhenUse] Deal +1% damage for every [Laceration] on target (max 20%)
   PL: Moc Końcowa +1 za każde 4 [Laceration] celu (maks. 2)\n\n[WhenUse] zadaje +1% obrażeń za każde 1 [Laceration] celu (maks. 20%)
956. [Umiejętność wroga [9106303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [Umiejętność wroga [9106303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
958. [Umiejętność wroga [9106303] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106303].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Reuse this Coin once (once per Skill)
   PL: [UnBrokenCoinOnSucceedAttack] używa tej Monety ponownie 1 raz (1 raz na Umiejętność)
959. [Umiejętność wroga [9106303] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 위력만큼 관통 피해 (최대 30)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106303].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Deal Pierce damage equal to [Laceration] Potency on target (max 30)
   PL: [UnBrokenCoinOnSucceedAttack] zadaje obrażenia Kłute równe Siły [Laceration] celu (maks. 30)
960. [Umiejętność wroga [9106303] (ulepszenie 1) — moneta 1, efekt 5 — opis] [ReUseOnSucceedAttack] [NiddlePin] 1 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106303].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [NiddlePin]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [NiddlePin] = 바늘못 / Naildle
   EN: [ReUseOnSucceedAttack] Inflict 1 [NiddlePin]
   PL: [ReUseOnSucceedAttack] nakłada 1 [NiddlePin]
961. [Umiejętność wroga [9106304] (ulepszenie 1) — nazwa] 공그르기 - 날실
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106304].levelList[level=1].name
   limit: do 40 znaków
   EN: Blind Stitch - Warp
   PL: Blind Stitch - Warp
962. [Umiejętność wroga [9106304] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 [PenetrateResultUp] 1 얻음
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [PenetrateResultUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up
   EN: [StartBattle] Gain 1 [PenetrateResultUp] next turn
   PL: [StartBattle] zyskuje 1 [PenetrateResultUp] w następnej turze
963. [Umiejętność wroga [9106401] (ulepszenie 1) — nazwa] 홈질 - 씨실
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106401].levelList[level=1].name
   limit: do 40 znaków
   EN: Running Stitch - Weft
   PL: Running Stitch - Weft
964. [Umiejętność wroga [9106401] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면, 최종 위력 +1\n\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 모든 코인이 [SuperCoin]이 됨
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106401].levelList[level=1].desc
   (powtórzenie elementu 946 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
965. [Umiejętność wroga [9106401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
966. [Umiejętność wroga [9106401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [PenetrateTakeDamageUp] 1 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [OnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] next turn
   PL: [OnSucceedAttack] nakłada 1 [PenetrateTakeDamageUp] w następnej turze
967. [Umiejętność wroga [9106402] (ulepszenie 1) — nazwa] 시침질 - 씨실
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106402].levelList[level=1].name
   limit: do 40 znaków
   EN: Tacking Stitch - Weft
   PL: Tacking Stitch - Weft
968. [Umiejętność wroga [9106402] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면, 최종 위력 +1
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106402].levelList[level=1].desc
   (powtórzenie elementu 950 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
969. [Umiejętność wroga [9106402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
970. [Umiejętność wroga [9106402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [NiddlePin] 1 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 718 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
971. [Umiejętność wroga [9106402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
972. [Umiejętność wroga [9106403] (ulepszenie 1) — nazwa] 박음질 - 씨실
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106403].levelList[level=1].name
   limit: do 40 znaków
   EN: Backstitch - Weft
   PL: Backstitch - Weft
973. [Umiejętność wroga [9106403] (ulepszenie 1) — opis] 대상의 [Laceration] 4당 최종 위력 +1 (최대 2)\n\n[WhenUse] 대상의 [Laceration]당 피해량 +1% (최대 20%)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106403].levelList[level=1].desc
   (powtórzenie elementu 955 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
974. [Umiejętność wroga [9106403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
975. [Umiejętność wroga [9106403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
976. [Umiejętność wroga [9106403] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106403].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 958 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
977. [Umiejętność wroga [9106403] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 위력만큼 관통 피해 (최대 30)
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106403].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 959 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
978. [Umiejętność wroga [9106403] (ulepszenie 1) — moneta 1, efekt 5 — opis] [ReUseOnSucceedAttack] [NiddlePin] 1 부여
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106403].levelList[level=1].coinlist[#0].coindescs[#4].desc
   (powtórzenie elementu 960 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
979. [Umiejętność wroga [9106404] (ulepszenie 1) — nazwa] 공그르기 - 씨실
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106404].levelList[level=1].name
   limit: do 40 znaków
   EN: Blind Stitch - Weft
   PL: Blind Stitch - Weft
980. [Umiejętność wroga [9106404] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 [PenetrateResultUp] 1 얻음
   źródło: Skills_Enemy-a1c10p1.json :: dataList[id=9106404].levelList[level=1].desc
   (powtórzenie elementu 962 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c10p1] Pasywka wroga: Passives_Abnormality-a1c10p1
- plik gry: `Passives_Abnormality-a1c10p1.json`

981. [[a1c10p1] Pasywka wroga [146501] — nazwa] 르누아르 원단
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146501].name
   limit: do 40 znaków
   EN: Le Noir: Fabric
   PL: Le Noir: Fabric
982. [[a1c10p1] Pasywka wroga [146501] — opis] 스테이지 시작시, [NoirBindArmor] 5 얻음\n턴 시작시 자신의 최대 체력의 ([NoirBindArmor] 수치)%만큼 보호막 얻음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146501].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [NoirBindArmor]
   znaczenie tagów: [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted
   EN: Encounter Start: Gain 5 [NoirBindArmor]\nTurn Start: Gain Shield equal to ([NoirBindArmor] Stack)% of this unit's max HP
   PL: Na początku etapu: zyskuje 5 [NoirBindArmor]\nPoczątek tury: zyskuje Tarczę równą (Stosy [NoirBindArmor])% Maks. HP tej jednostki
983. [[a1c10p1] Pasywka wroga [146501] — tekst klimatyczny] 르누아르 원단은 갑옷과 같이 탄탄하고 고정된 실루엣으로 고객의 체형을 보정해준다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146501].flavor
   limit: do 130 znaków
   EN: Le Noir's Worsted holds the body like armor, accentuating it beneath a firm, fixed silhouette.
   PL: Tkanina Le Noir trzyma ciało jak zbroję, eksponując je pod twardą, niezmienną sylwetką.
984. [[a1c10p1] Pasywka wroga [146502] — nazwa] 고객 안내
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146502].name
   limit: do 40 znaków
   EN: Ushering Customers
   PL: Ushering Customers
985. [[a1c10p1] Pasywka wroga [146502] — opis] 대상의 [NoirNoComply] 1당 대상에게 가하는 피해량과 받는 피해량 +10%\n[NoirNoComply]이 3인 대상에게 가하는 피해량 +200%
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146502].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [NoirNoComply]
   znaczenie tagów: [NoirNoComply] = 안내 불이행 / Instruction Incompliance
   EN: Deal +10% damage to and take +10% damage from target for every [NoirNoComply] on target\nDeal +200% damage to targets that have 3 [NoirNoComply]
   PL: zadaje +10% obrażeń i otrzymuje +10% obrażeń od celu za każde 1 [NoirNoComply] celu\nzadaje +200% obrażeń celom mającym 3 [NoirNoComply]
986. [[a1c10p1] Pasywka wroga [146502] — tekst klimatyczny] 르누아르에서는 엄격한 본사 관리 매뉴얼을 통해 고객분들을 응대하고 있습니다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146502].flavor
   limit: do 130 znaków
   EN: Le Noir serves its valued customers in strict accordance with Head Office management protocol.
   PL: Le Noir obsługuje swoich szanowanych klientów w ścisłej zgodzie z podręcznikiem zarządzania Centrali.
987. [[a1c10p1] Pasywka wroga [146503] — nazwa] 보존
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146503].name
   limit: do 40 znaków
   EN: Preservation
   PL: Preservation
988. [[a1c10p1] Pasywka wroga [146503] — opis] 전투 중 누적으로 자신의 [ChargeNoir] 횟수를\n- 3 소모할 때마다 [NoirBindArmor] 1 얻음\n- 10 소모할 때마다 [ChargeNoir] 1 얻음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146503].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir], [NoirBindArmor]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation; [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted
   EN: Gain 1 [NoirBindArmor] for every 3 cumulative [ChargeNoir] Count this unit consumes in this Encounter\nGain 1 [ChargeNoir] for every 10 cumulative [ChargeNoir] Count this unit consumes in this Encounter
   PL: zyskuje 1 [NoirBindArmor] za każde 3 łącznie zużyte Liczniki [ChargeNoir] tej jednostki w tej walce\nzyskuje 1 [ChargeNoir] za każde 10 łącznie zużytych Liczników [ChargeNoir] tej jednostki w tej walce
989. [[a1c10p1] Pasywka wroga [146503] — tekst klimatyczny] 응축하여 힘을 모아 고정한다. 변화시키지 않는 것이 변화시키는 것보다 더 큰 힘이 필요할 때가 있다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146503].flavor
   limit: do 160 znaków
   EN: Force is compressed, gathered, and fixed in place. Sometimes, it takes more force to prevent change than to cause it.
   PL: Siła zostaje sprężona, skupiona i utrwalona. Czasem potrzeba więcej siły, by powstrzymać zmianę, niż ją wywołać.
990. [[a1c10p1] Pasywka wroga [146603] — nazwa] 대사작용
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146603].name
   limit: do 50 znaków
   EN: Metabolic Action and Reaction
   PL: Metabolic Action and Reaction
991. [[a1c10p1] Pasywka wroga [146603] — opis] 전투에 처음으로 등장하면, [ChargeRouge] 횟수 10 얻음\n\n전투 중 누적으로 자신의 [ChargeRouge] 횟수를 10 소모할 때마다 [ChargeRouge] 1 얻음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146603].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation
   EN: Upon entering the Encounter for the first time, gain 10 [ChargeRouge] Count\n\nGain 1 [ChargeRouge] for every 10 cumulative [ChargeRouge] Count this unit consumes in this Encounter
   PL: Przy pierwszym pojawieniu się w walce zyskuje 10 Licznika [ChargeRouge]\n\nzyskuje 1 [ChargeRouge] za każde 10 łącznie zużytych Liczników [ChargeRouge] tej jednostki w tej walce
992. [[a1c10p1] Pasywka wroga [149401] — nazwa] 르루주 자켓
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149401].name
   limit: do 40 znaków
   EN: Le Rouge: Jacket
   PL: Le Rouge: Jacket
993. [[a1c10p1] Pasywka wroga [149401] — opis] 턴 종료시, [ChargeRouge] 횟수를 최대 10까지 얻거나 잃음\n\n자신이 피격당할 때, 공격자가 [Charge]을 얻는 스킬을 사용했으면 [Charge] 횟수 1을 공격자에게 옮김 (공격자 스킬당 1회)\n해당 효과가 발동될 때마다 [AttackUp] 1 얻음\n턴 시작시, 자신의 15를 초과하는 [ChargeRouge] 횟수를 최대 5까지 소모하여 최대 체력의 (소모값)% 회복
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149401].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge], [Charge], [AttackUp]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation; [Charge] = 충전 / Charge; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn End: Gain or lose up to 10 [ChargeRouge] Count\n\nWhen hit, if the attacker used Skills that gain [Charge], transfer 1 [ChargeRouge] Count as [Charge] Count to the attacker (once per the attacker's Skill)\nGain 1 [AttackUp] every time the effect above activates\nTurn Start: Consume up to 5 excess [ChargeRouge] Count beyond 15 on self to heal ([ChargeRouge] Count consumed)% HP
   PL: Koniec tury: zyskuje lub traci do 10 Licznika [ChargeRouge]\n\nPrzy trafieniu, jeżeli atakujący użył Umiejętności zyskujących [Charge], przenosi na atakującego 1 Licznika [ChargeRouge] jako 1 Licznika [Charge] (1 raz na Umiejętność atakującego)\nza każde uruchomienie powyższego efektu zyskuje 1 [AttackUp]\nPoczątek tury: zużywa do 5 nadmiarowych Liczników [ChargeRouge] tej jednostki powyżej 15, aby przywrócić (zużyte Liczniki [ChargeRouge])% HP
994. [[a1c10p1] Pasywka wroga [149402] — nazwa] 근섬유 데님
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149402].name
   limit: do 40 znaków
   EN: Myofiber Denim
   PL: Myofiber Denim
