# Paczka AI P74 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 10/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P74_3c_przeciwnicy_i_anomalie_cz10.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P74_3c_przeciwnicy_i_anomalie_cz10.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [a1c971] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c971
- grupa rozdziału/trybu: `a1c971` · plik: `Skills_Abnormality-a1c971.json`

1. [Umiejętność wroga [108101] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 5+ [Sinking], Coin Power +1
   PL: [WhenUse] jeżeli cel ma 5+ [Sinking], Moc Monety +1
2. [Umiejętność wroga [108101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
3. [Umiejętność wroga [108101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] and +2 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 2 [Sinking] i 2 Licznika [Sinking]
4. [Umiejętność wroga [108102] (ulepszenie 1) — nazwa] 물벼락
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108102].levelList[level=1].name
   limit: do 40 znaków
   EN: Torrent
   PL: Torrent
5. [Umiejętność wroga [108102] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Sinking]이 있으면, 기본 위력 +2
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has [Sinking], Base Power +2
   PL: [WhenUse] jeżeli cel ma [Sinking], Moc Bazowa +2
6. [Umiejętność wroga [108102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 8부여, [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 8 [Sinking] and +2 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 8 [Sinking] i 2 Licznika [Sinking]
7. [Umiejętność wroga [108102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 무작위 대상 2명 에게 [Sinking] 4 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking] and +2 [Sinking] Count against 2 random targets
   PL: [OnSucceedAttack] nakłada 4 [Sinking] i 2 Licznika [Sinking] 2 losowym celom
8. [Umiejętność wroga [108103] (ulepszenie 1) — nazwa] 쏟아지는 우울
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108103].levelList[level=1].name
   limit: do 40 znaków
   EN: Cascading Gloom
   PL: Cascading Gloom
9. [Umiejętność wroga [108103] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 3 당, 코인 위력 +1 (최대 3)\n[WinDuel] 대상의 [Sinking] 5 당, 이 스킬의 공격 가중치 +1 (최대 2)
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108103].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Coin Power +1 for every 3 [Sinking] on target (max 3)\n[WinDuel] This Skill gains Atk Weight +1 for every 5 [Sinking] on the target (max 2)
   PL: [WhenUse] Moc Monety +1 za każde 3 [Sinking] celu (maks. 3)\n[WinDuel] ta Umiejętność zyskuje Wagę Ataku +1 za każde 5 [Sinking] celu (maks. 2)
10. [Umiejętność wroga [108103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5 부여, [Sinking] 횟수 4 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking] and +4 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 5 [Sinking] i 4 Licznika [Sinking]
11. [Umiejętność wroga [108103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Sinking] 3 당, 다음 코인 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Next Coin Power +1 for every 3 [Sinking] on the target (3 times max)
   PL: [OnSucceedAttack] Moc następnej Monety +1 za każde 3 [Sinking] celu (do 3 razy)
12. [Umiejętność wroga [108103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
13. [Umiejętność wroga [108103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [SinkingSurge]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [SinkingSurge]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [SinkingSurge] = 침잠쇄도 / Sinking Deluge
   EN: [UnBrokenCoinOnSucceedAttack] Cause [SinkingSurge]
   PL: [UnBrokenCoinOnSucceedAttack] powoduje [SinkingSurge]
14. [Umiejętność wroga [108104] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108104].levelList[level=1].name
   limit: do 40 znaków
   EN: Evade
   PL: Evade
15. [Umiejętność wroga [108104] (ulepszenie 1) — opis] [OnSucceedEvade] 대상의 정신력 5 감소
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Target loses 5 SP
   PL: [OnSucceedEvade] cel traci 5 SP
16. [Umiejętność wroga [107901] (ulepszenie 1) — nazwa] 무너뜨리기
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107901].levelList[level=1].name
   limit: do 40 znaków
   EN: Topple
   PL: Topple
17. [Umiejętność wroga [107901] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 20 소모하여, [BloodDinner] 10당 [BloodArmor] 1 얻음.\n[WhenUse] [BloodArmor] 10당, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Laceration] 10당, 코인 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107901].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodArmor], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmor] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Consume 20 [BloodDinner]: gain 1 [BloodArmor] for every 10 [BloodDinner] consumed\n[WhenUse] Coin Power +1 for every 10 [BloodArmor] (max 2)\n[WhenUse] Coin Power +1 for every 15 [Laceration] on self (max 3)
   PL: [WhenUse] zużywa 20 [BloodDinner]: zyskuje 1 [BloodArmor] za każde 10 zużytego [BloodDinner].\n[WhenUse] Moc Monety +1 za każde 10 [BloodArmor] (maks. 2)\n[WhenUse] Moc Monety +1 za każde 10 [Laceration] jednostki (maks. 3)
18. [Umiejętność wroga [107901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL: [OnSucceedAttack] nakłada 5 [Laceration]
19. [Umiejętność wroga [107901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
20. [Umiejętność wroga [107902] (ulepszenie 1) — nazwa] 상처내기
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107902].levelList[level=1].name
   limit: do 40 znaków
   EN: Wound
   PL: Wound
21. [Umiejętność wroga [107902] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 20 소모하여, [BloodDinner] 10당 [BloodArmor] 1 얻음.\n[WhenUse] [BloodArmor] 10당, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Laceration] 10당, 코인 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107902].levelList[level=1].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
22. [Umiejętność wroga [107902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Laceration]
23. [Umiejętność wroga [107902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
24. [Umiejętność wroga [107903] (ulepszenie 1) — nazwa] 돈키호테류 경혈 4식 - 도려내기
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107903].levelList[level=1].name
   limit: do 60 znaków
   EN: Don Quixote Hardblood Arts 4 - Sundering
   PL: Don Quixote Hardblood Arts 4 - Sundering
25. [Umiejętność wroga [107903] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WinDuel] [BloodArmor] 단계에 따라, 이 스킬의 피해량 +20% (최대 60%)\n[DefeatDuel] [BloodArmor] 4 소모
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107903].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [WinDuel], [BloodArmor], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [BloodArmor] = 경혈 / Hardblood; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If target has 6+ [Laceration], Coin Power +1\n[WinDuel] With this Skill, deal +20% damage with every Stage of [BloodArmor] (max 60%)\n[DefeatDuel] Consume 4 [BloodArmor]
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1\n[WinDuel] ta Umiejętność zadaje +20% obrażeń za każdy Etap [BloodArmor] (maks. 60%)\n[DefeatDuel] zużywa 4 [BloodArmor]
26. [Umiejętność wroga [107903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
27. [Umiejętność wroga [107903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
28. [Umiejętność wroga [107904] (ulepszenie 1) — nazwa] 돈키호테류 경혈11식 - 후벼파기
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107904].levelList[level=1].name
   limit: do 60 znaków
   EN: Don Quixote Hardblood Arts 11 - Impaling
   PL: Don Quixote Hardblood Arts 11 - Impaling
29. [Umiejętność wroga [107904] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 3당, 기본 위력 +1 (최대 3)\n[WinDuel] [BloodArmor] 단계에 따라, 이 스킬의 피해량 +20% (최대 60%)\n[DefeatDuel] [BloodArmor] 4 소모
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107904].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [WinDuel], [BloodArmor], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [BloodArmor] = 경혈 / Hardblood; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] For every 3 [Laceration] on the target, Base Power +1 (max 3)\n[WinDuel] With this Skill, deal +20% damage with every Stage of [BloodArmor] (max 60%)\n[DefeatDuel] Consume 4 [BloodArmor]
   PL: [WhenUse] Moc Bazowa +1 za każde 3 [Laceration] celu (maks. 3)\n[WinDuel] ta Umiejętność zadaje +20% obrażeń za każdy Etap [BloodArmor] (maks. 60%)\n[DefeatDuel] zużywa 4 [BloodArmor]
30. [Umiejętność wroga [107904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
31. [Umiejętność wroga [107904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
32. [Umiejętność wroga [107904] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]을 횟수만큼 발동시킴. 대상의 [Laceration] 횟수를 1까지 소모시킴
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107904].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on the target equal to its Count. Use up the target's [Laceration] Count down to 1
   PL: [OnSucceedAttack] uruchamia [Laceration] celu tyle razy, ile wynosi jego Licznik. zużywa Licznik [Laceration] celu do 1
33. [Umiejętność wroga [107905] (ulepszenie 1) — nazwa] 돈키호테 아류 산초 4식 - 추적
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107905].levelList[level=1].name
   limit: do 70 znaków
   EN: Variant Don Quixote Style: Sancho Arts 4 - Track
   PL: Variant Don Quixote Style: Sancho Arts 4 - Track
34. [Umiejętność wroga [107905] (ulepszenie 1) — opis] [Laceration]이 가장 많은 대상 우선 공격\n[BeforeAttack] 자신의 [BloodArmor] 10 당 공격 가중치 +1 (최대 3)\n[WhenUse] 대상의 [Laceration] 5 당, 합 위력 +1 (최대 3)\n[WhenUse] [BloodDinner]을 최대 30 소모하여, 소모한 [BloodDinner] 15당 [BloodArmor] 1 얻음. 코인 위력 +1 (최대 2)\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻고 발동시킴. [Laceration] 횟수 1 감소\n[EndSkill] 이 스킬로 입히는 피해량만큼 [BloodDinner] 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107905].levelList[level=1].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BeforeAttack], [BloodArmor], [WhenUse], [BloodDinner], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BloodArmor] = 경혈 / Hardblood; [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Prioritizes targets with the most [Laceration]\n[BeforeAttack] Atk Weight +1 for every 10 [BloodArmor] on self (max 3)\n[WhenUse] Clash Power +1 for every 5 [Laceration] on the target (max 3)\n[WhenUse] Consume up to 30 [BloodDinner]: gain 1 [BloodArmor] and Coin Power +1 for every 15 [BloodDinner] consumed (max 2)\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration], and activate [Laceration] immediately. Lose 1 [Laceration] Count\n[EndSkill] Increase [BloodDinner] equal to the damage this Skill dealt
   PL: priorytet: cele z największą liczbą [Laceration]\n[BeforeAttack] Waga Ataku +1 za każde 10 [BloodArmor] jednostki (maks. 3)\n[WhenUse] Moc Starcia +1 za każde 5 [Laceration] celu (maks. 3)\n[WhenUse] zużywa do 30 [BloodDinner]: zyskuje 1 [BloodArmor] i Moc Monety +1 za każde 15 zużytego [BloodDinner] (maks. 2)\n- jeżeli nie udało się zużyć [BloodDinner], zyskuje 10 [Laceration] i natychmiast uruchamia [Laceration]. traci 1 Licznika [Laceration]\n[EndSkill] zwiększa [BloodDinner] o wartość obrażeń zadanych tą Umiejętnością
35. [Umiejętność wroga [107905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 8 [Laceration]
   PL: [OnSucceedAttack] nakłada 8 [Laceration]
36. [Umiejętność wroga [107905] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여\n- 이 스킬에서 [BloodDinner]을 30 소모했다면, [Binding] 2 추가 부여
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107905].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Binding], [BloodDinner]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [BloodDinner] = 혈찬 / Bloodfeast
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn\n- If this Skill consumed 30 [BloodDinner], inflict 2 additional [Binding]
   PL: [OnSucceedAttack] nakłada 1 [Binding] w następnej turze\n- jeżeli ta Umiejętność zużyła 30 [BloodDinner], nakłada dodatkowe 2 [Binding]
37. [Umiejętność wroga [107906] (ulepszenie 1) — nazwa] 돈키호테 아류 산초 3식 - 기습
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107906].levelList[level=1].name
   limit: do 70 znaków
   EN: Variant Don Quixote Style: Sancho Arts 3 - Ambush
   PL: Variant Don Quixote Style: Sancho Arts 3 - Ambush
38. [Umiejętność wroga [107906] (ulepszenie 1) — opis] [Laceration]이 가장 많은 대상 우선 공격\n[BeforeAttack] 대상의 [Laceration] 10당 공격 가중치 +1 (최대 2)\n[WhenUse] 대상의 [Laceration] 5 당, 합 위력 +1 (최대 3)\n[WhenUse] [BloodDinner]을 최대 30 소모하여, 소모한 [BloodDinner] 15당 [BloodArmor] 1 얻음. 코인 위력 +1 (최대 2)\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻고 발동시킴. [Laceration] 횟수 1 감소\n[EndSkill] 이 스킬로 입히는 피해량만큼 [BloodDinner] 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107906].levelList[level=1].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BeforeAttack], [WhenUse], [BloodDinner], [BloodArmor], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmor] = 경혈 / Hardblood; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Prioritizes targets with the most [Laceration]\n[BeforeAttack] Atk Weight +1 for every 10 [BloodArmor] on self (max 2)\n[WhenUse] Clash Power +1 for every 5 [Laceration] on the target (max 3)\n[WhenUse] Consume up to 30 [BloodDinner]: gain 1 [BloodArmor] and Coin Power +1 for every 15 [BloodDinner] consumed (max 2)\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration], and activate [Laceration] immediately. Lose 1 [Laceration] Count\n[EndSkill] Increase [BloodDinner] equal to the damage this Skill dealt
   PL: priorytet: cele z największą liczbą [Laceration]\n[BeforeAttack] Waga Ataku +1 za każde 10 [BloodArmor] jednostki (maks. 2)\n[WhenUse] Moc Starcia +1 za każde 5 [Laceration] celu (maks. 3)\n[WhenUse] zużywa do 30 [BloodDinner]: zyskuje 1 [BloodArmor] i Moc Monety +1 za każde 15 zużytego [BloodDinner] (maks. 2)\n- jeżeli nie udało się zużyć [BloodDinner], zyskuje 10 [Laceration] i natychmiast uruchamia [Laceration]. traci 1 Licznika [Laceration]\n[EndSkill] zwiększa [BloodDinner] o wartość obrażeń zadanych tą Umiejętnością
39. [Umiejętność wroga [107906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
40. [Umiejętność wroga [107906] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107906].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
41. [Umiejętność wroga [107906] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여\n- 이 스킬에서 [BloodDinner]을 50 소모했다면, [Paralysis] 2 추가 부여
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107906].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Paralysis], [BloodDinner]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze; [BloodDinner] = 혈찬 / Bloodfeast
   EN: [OnSucceedAttack] Inflict 1 [Paralysis] next turn\n- If this Skill consumed 50 [BloodDinner], inflict 2 additional [Paralysis]
   PL: [OnSucceedAttack] nakłada 1 [Paralysis] w następnej turze\n- jeżeli ta Umiejętność zużyła 50 [BloodDinner], nakłada dodatkowe 2 [Paralysis]
42. [Umiejętność wroga [107907] (ulepszenie 1) — nazwa] 돈키호테류 경혈 2식 - 경혈
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107907].levelList[level=1].name
   limit: do 60 znaków
   EN: Don Quixote Hardblood Arts 2 - Hardblood
   PL: Don Quixote Hardblood Arts 2 - Hardblood
43. [Umiejętność wroga [107907] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[StartBattle] [SwirlingBlood]를 1 얻음\n[StartBattle] [BloodDinner]을 100 소모하여, 소모한 [BloodDinner] 10당 [BloodArmor] 1, 보호막 체력 20을얻음.\n- [BloodDinner]이 부족할 경우, [Laceration] 50을 얻고 발동시킴. [Laceration] 횟수 2 감소. 200만큼 보호막 체력을 얻음 (이 피해로 체력이 1미만이 되지 않음)\n[DefeatDuel] 이 스킬로 얻은 보호막 효과가 있는 동안 [Vulnerable]을 3 얻음\n[DefeatDuel] 이 스킬로 입히는 피해량 -50%\n[EndSkill] 전투 종료
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107907].levelList[level=1].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SwirlingBlood], [BloodDinner], [BloodArmor], [Laceration], [DefeatDuel], [Vulnerable], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SwirlingBlood] = 일렁임【혈귀】 / Shimmering【Bloodfiend】; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmor] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Can Clash with this Skill regardless of Speed\n[StartBattle] Gain 1 [SwirlingBlood]\n[StartBattle] Consume 100 [BloodDinner]; gain 1 [BloodArmor] and 20 Shield HP for every 10 [BloodDinner] consumed\n- If this unit doesn't have enough [BloodDinner], gain 50 [Laceration], and activate it immediately. Lose 2 [Laceration] Count. Gain 200 Shield HP (this damage does not reduce this unit's HP to 0)\n[DefeatDuel] As long as the Shield HP from this Skill remains, gain 3 [Vulnerable]\n[DefeatDuel] This Skill deals -50% damage\n[EndSkill] End Combat Phase
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[StartBattle] zyskuje 1 [SwirlingBlood]\n[StartBattle] zużywa 100 [BloodDinner]; zyskuje 1 [BloodArmor] i 20 HP Tarczy za każde 10 zużytego [BloodDinner]\n- jeżeli jednostka nie ma wystarczającego [BloodDinner], zyskuje 50 [Laceration] i natychmiast je uruchamia. traci 2 Licznika [Laceration]. zyskuje 200 HP Tarczy (te obrażenia nie obniżają HP jednostki poniżej 1)\n[DefeatDuel] dopóki trwa efekt Tarczy z tej Umiejętności, zyskuje 3 [Vulnerable]\n[DefeatDuel] ta Umiejętność zadaje o 50% mniej obrażeń\n[EndSkill] kończy Fazę walki
44. [Umiejętność wroga [107907] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107907].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Umiejętność wroga [107907] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107907].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
46. [Umiejętność wroga [107907] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107907].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Umiejętność wroga [107907] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107907].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [Umiejętność wroga [107907] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107907].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 5 [Laceration] i 3 Licznika [Laceration]
49. [Umiejętność wroga [107908] (ulepszenie 1) — nazwa] 라 어벤투라 아 테르미나도
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107908].levelList[level=1].name
   limit: do 40 znaków
   EN: La Aventura Ha Terminado
   PL: La Aventura Ha Terminado
50. [Umiejętność wroga [107908] (ulepszenie 1) — opis] 대상의 [Laceration]당, 피해량 +10% (최대 200%)\n[BloodArmor] 3 당 피해량 +10% (최대 100%)\n[StartBattle] [BloodDinner]을 (45 - 현재 정신력)만큼 소모하여 정신력을 45까지 회복\n- [BloodDinner]이 부족할 경우, [Laceration] 20을 얻고, 정신력을 45까지 회복\n- 남은 [BloodDinner]만큼 보호막 체력을 얻음 (최대 100)\n[WinDuel] 대상에게 [Laceration] 10 부여\n[EndSkill] 대상에게 가한 체력 피해량만큼 [BloodDinner] 증가\n[EndSkill] 대상이 사망했으면, 대상의 최대 체력만큼 [BloodDinner] 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107908].levelList[level=1].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodArmor], [StartBattle], [BloodDinner], [WinDuel], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodArmor] = 경혈 / Hardblood; [StartBattle] = [전투 시작시] / [Combat Start]; [BloodDinner] = 혈찬 / Bloodfeast; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +10% damage for every [Laceration] on the target (max 200%)\nDeal +10% damage for every 3 [BloodArmor] (max 100%)\n[StartBattle] Consume (45 - current SP) [BloodDinner] and heal up to 45 SP\n- If there isn't enough [BloodDinner], gain 20 [Laceration] and heal up to 45 SP\n- Gain Shield HP equal to remaining [BloodDinner] (max 100)\n[WinDuel] Inflict 10 [Laceration]\n[EndSkill] Increase [BloodDinner] by HP damage dealt against the target\n[EndSkill] If the target is defeated, increase [BloodDinner] by the target's max HP
   PL: zadaje +10% obrażeń za każdy [Laceration] celu (maks. 200%)\nzadaje +10% obrażeń za każde 3 [BloodArmor] (maks. 100%)\n[StartBattle] zużywa (45 - aktualne SP) [BloodDinner] i przywraca SP do 45\n- jeżeli brakuje [BloodDinner], zyskuje 20 [Laceration] i przywraca SP do 45\n- zyskuje HP Tarczy równe pozostałemu [BloodDinner] (maks. 100)\n[WinDuel] nakłada 10 [Laceration]\n[EndSkill] zwiększa [BloodDinner] o wartość obrażeń HP zadanych celowi\n[EndSkill] jeżeli cel ginie, zwiększa [BloodDinner] o Maks. HP celu
51. [Umiejętność wroga [107908] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107908].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Umiejętność wroga [107908] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 10 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107908].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 10 [Laceration] and +3 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 10 [Laceration] i 3 Licznika [Laceration]
53. [Umiejętność wroga [107908] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상을 제외한 모든 적들에게 [Laceration] 5 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107908].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +3 [Laceration] Count to all enemies except for the target
   PL: [OnSucceedAttack] nakłada 5 [Laceration] i 3 Licznika [Laceration] wszystkim wrogom poza celem
54. [Umiejętność wroga [107909] (ulepszenie 1) — nazwa] 라 어벤투라 아 테르미나도...
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107909].levelList[level=1].name
   limit: do 40 znaków
   EN: La Aventura Ha Terminado...
   PL: La Aventura Ha Terminado...
55. [Umiejętność wroga [107909] (ulepszenie 1) — opis] 모든 대상의 [Laceration] 합산 10당, 피해량 +40% (최대 200%)\n자신의 누적 소모 [BloodDinner]당 피해량 +10% (최대 100%)\n[StartBattle] [BloodDinner]을 (45 - 현재 정신력)만큼 소모하여 정신력을 45까지 회복\n- [BloodDinner]이 부족할 경우, [Laceration] 20을 얻고, 정신력을 45까지 회복\n- 남은 [BloodDinner]만큼 보호막 체력을 얻음 (최대 100)\n[WinDuel] 대상에게 [Laceration] 10 부여\n[EndSkill] 대상에게 가한 체력 피해량만큼 [BloodDinner] 증가\n[EndSkill] 대상이 사망했으면, 대상의 최대 체력만큼 [BloodDinner] 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107909].levelList[level=1].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner], [StartBattle], [WinDuel], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [StartBattle] = [전투 시작시] / [Combat Start]; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +40% damage for every 10 (sum of [Laceration] on all targets]) (max 200%)\nDeal +10% damage for every cumulative [BloodDinner] this unit consumed (max 100%)\n[StartBattle] Consume (45 - current SP) [BloodDinner] and heal up to 45 SP\n- If there isn't enough [BloodDinner], gain 20 [Laceration] and heal up to 45 SP\n- Gain Shield HP equal to remaining [BloodDinner] (max 100)\n[WinDuel] Inflict 10 [Laceration]\n[EndSkill] Increase [BloodDinner] by HP damage dealt against the target\n[EndSkill] If the target is defeated, increase [BloodDinner] by the target's max HP
   PL: zadaje +40% obrażeń za każde 10 łącznie ([Laceration] wszystkich celów) (maks. 200%)\nzadaje +10% obrażeń za każde łącznie zużyte [BloodDinner] jednostki (maks. 100%)\n[StartBattle] zużywa (45 - aktualne SP) [BloodDinner] i przywraca SP do 45\n- jeżeli brakuje [BloodDinner], zyskuje 20 [Laceration] i przywraca SP do 45\n- zyskuje HP Tarczy równe pozostałemu [BloodDinner] (maks. 100)\n[WinDuel] nakłada 10 [Laceration]\n[EndSkill] zwiększa [BloodDinner] o wartość obrażeń HP zadanych celowi\n[EndSkill] jeżeli cel ginie, zwiększa [BloodDinner] o Maks. HP celu
56. [Umiejętność wroga [107909] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107909].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Umiejętność wroga [107909] (ulepszenie 1) — moneta 1, efekt 2 — opis] [Laceration] 10 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=107909].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Inflict 10 [Laceration] and +3 [Laceration] Count
   PL: nakłada 10 [Laceration] i 3 Licznika [Laceration]
58. [Umiejętność wroga [108201] (ulepszenie 1) — nazwa] 압착
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108201].levelList[level=1].name
   limit: do 40 znaków
   EN: Compression
   PL: Compression
59. [Umiejętność wroga [108201] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력 5당 최종 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Final Power +1 for every 5 [Breath] Potency on self (max 3)
   PL: [WhenUse] Moc Końcowa +1 za każde 5 Siły [Breath] jednostki (maks. 3)
60. [Umiejętność wroga [108201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 위력 2 부여
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] Potency
   PL: [OnSucceedAttack] nakłada 2 Siły [Vibration]
61. [Umiejętność wroga [108201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Vibration] 위력 3 부여, 대상의 [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Vibration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Vibration] = 진동 / Tremor
   EN: [CriticalOnSucceedAttack] Inflict 3 [Vibration] Potency and +2 [Vibration] Count
   PL: [CriticalOnSucceedAttack] nakłada 3 Siły [Vibration] i 2 Licznika [Vibration]
62. [Umiejętność wroga [108202] (ulepszenie 1) — nazwa] 분해
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108202].levelList[level=1].name
   limit: do 40 znaków
   EN: Dismantle
   PL: Dismantle
63. [Umiejętność wroga [108202] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력 3당 최종 위력 +1 (최대 5)
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Final Power +1 for every 3 [Breath] Potency on self (max 5)
   PL: [WhenUse] Moc Końcowa +1 za każde 3 Siły [Breath] jednostki (maks. 5)
64. [Umiejętność wroga [108202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 위력 3 부여
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] Potency
   PL: [OnSucceedAttack] nakłada 3 Siły [Vibration]
65. [Umiejętność wroga [108202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [WinDuelAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Vibration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Vibration] = 진동 / Tremor
   EN: [WinDuelAttack] Inflict +3 [Vibration] Count
   PL: [WinDuelAttack] nakłada 3 Licznika [Vibration]
66. [Umiejętność wroga [108202] (ulepszenie 1) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] [VibrationExplosion] 1회. 대상이 [VibrationExplosion] 시, 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108202].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [CriticalOnSucceedAttack] Trigger [VibrationExplosion]. When [VibrationExplosion] is triggered on the target, reduce target's [Vibration] Count by 1
   PL: [CriticalOnSucceedAttack] uruchamia [VibrationExplosion] raz. gdy [VibrationExplosion] uruchamia się na celu, zmniejsza Licznik [Vibration] celu o 1
67. [Umiejętność wroga [108203] (ulepszenie 1) — nazwa] 분석 시행
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108203].levelList[level=1].name
   limit: do 40 znaków
   EN: Conduct Analysis
   PL: Conduct Analysis
68. [Umiejętność wroga [108203] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력이 10 이상이면, [Breath] 위력을 소모하여 소모한 [Breath] 위력 3당 최종 위력 +2 (최대 4). 위력이 증가 시, 증가한 위력 1당 [Breath] 3 추가로 소모
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108203].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] At 10+ [Breath] Potency, consume [Breath] Potency to gain +2 Final Power for every 3 [Breath] Potency consumed (max 4). Consume 3 additional [Breath] for every Final Power gained due to this effect
   PL: [WhenUse] przy 10+ Siły [Breath], zużywa Siłę [Breath], by zyskać +2 Mocy Końcowej za każde 3 zużytej Siły [Breath] (maks. 4). zużywa dodatkowo 3 [Breath] za każdą zyskaną dzięki temu efektowi Moc Końcową
69. [Umiejętność wroga [108203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Umiejętność wroga [108203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 5 이상이면 [VibrationExplosion]. 대상이 [VibrationExplosion] 시, 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 5+ [Vibration] Count, trigger [VibrationExplosion]. When [VibrationExplosion] is triggered on the target, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] jeżeli cel ma 5+ Licznika [Vibration], uruchamia [VibrationExplosion]. gdy [VibrationExplosion] uruchamia się na celu, zmniejsza Licznik [Vibration] celu o 1
71. [Umiejętność wroga [108203] (ulepszenie 1) — moneta 1, efekt 3 — opis] [WinDuelAttack] [Vibration] 위력 5 부여, [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108203].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Vibration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Vibration] = 진동 / Tremor
   EN: [WinDuelAttack] Inflict 5 [Vibration] Potency and +3 [Vibration] Count
   PL: [WinDuelAttack] nakłada 5 Siły [Vibration] i 3 Licznika [Vibration]
72. [Umiejętność wroga [108203] (ulepszenie 1) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] [VibrationExplosion] 2회. 대상이 [VibrationExplosion] 시, 대상의 [Vibration] 횟수 1 감소 (합에서 승리했다면 감소 효과 1회 무효)
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108203].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [CriticalOnSucceedAttack] Trigger [VibrationExplosion] twice. When [VibrationExplosion] is triggered on the target, reduce target's [Vibration] Count by 1 (nullify 1 instance of [Vibration] Count reduction if this unit won the Clash)
   PL: [CriticalOnSucceedAttack] uruchamia [VibrationExplosion] 2 razy. gdy [VibrationExplosion] uruchamia się na celu, zmniejsza Licznik [Vibration] celu o 1 (unieważnia 1 zmniejszenie Licznika [Vibration], jeżeli jednostka wygrała Starcie)
73. [Umiejętność wroga [108204] (ulepszenie 1) — nazwa] 소멸 시퀀스 가동
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108204].levelList[level=1].name
   limit: do 40 znaków
   EN: Trigger Extinction Sequence
   PL: Trigger Extinction Sequence
74. [Umiejętność wroga [108204] (ulepszenie 1) — opis] [WhenUse] [Breath] 위력과 [Breath] 횟수를 절반만큼 소모\n- (소모한 [Breath] 위력과 [Breath] 횟수의 합/2)만큼 최종 위력이 증가 (최대 20)\n- (소모한 [Breath] 위력 x 2)%만큼 피해량이 증가 (최대 50%)\n- (소모한 [Breath] 횟수 x 4)%만큼 크리티컬 피해량이 증가 (최대 100%)\n[DefeatDuel] 남은 [Breath] 횟수가 절반으로 감소
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108204].levelList[level=1].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Consume half of [Breath] Potency and Count on self\n- Gain (sum of consumed [Breath] Potency and Count / 2) Final Power (max 20)\n- Deal +(sum of consumed [Breath] Potency and Count x 2)% damage (max 50%)\n- +(sum of consumed [Breath] Potency and Count x 4)% damage on Critical Hit (max 100%)\n[DefeatDuel] Reduce remaining [Breath] Count by half
   PL: [WhenUse] zużywa połowę Siły i Licznika [Breath] jednostki\n- zyskuje (suma zużytej Siły [Breath] i Licznika [Breath] / 2) Mocy Końcowej (maks. 20)\n- zadaje +(suma zużytej Siły [Breath] i Licznika [Breath] x 2)% obrażeń (maks. 50%)\n- +(suma zużytej Siły [Breath] i Licznika [Breath] x 4)% obrażeń przy trafieniu krytycznym (maks. 100%)\n[DefeatDuel] zmniejsza pozostały Licznik [Breath] o połowę
75. [Umiejętność wroga [108204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Umiejętność wroga [108204] (ulepszenie 1) — moneta 1, efekt 2 — opis] 직전 턴에 체력 피해를 받지 않았다면, 크리티컬로 적중
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: If user took no HP damage last turn, guarantee a Crit
   PL: jeżeli użytkownik nie otrzymał obrażeń HP w poprzedniej turze, gwarantuje trafienie krytyczne
77. [Umiejętność wroga [108204] (ulepszenie 1) — moneta 1, efekt 3 — opis] 직전 턴에 체력 피해를 받았다면, 크리티컬로 적중하지 않고 피해량이 80%만큼 감소
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108204].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   EN: If user took HP damage last turn, does not Crit; instead, deal -80% damage
   PL: jeżeli ta jednostka otrzymała obrażenia HP w poprzedniej turze, bez trafienia krytycznego zadaje o 80% mniej obrażeń
78. [Umiejętność wroga [108204] (ulepszenie 1) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] [VibrationExplosion] 3회. 대상이 [VibrationExplosion] 시, [VibrationExplosion] 1회당 대상의 [Vibration] 횟수 3 감소 (최대 9 감소)
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108204].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [CriticalOnSucceedAttack] Trigger [VibrationExplosion] thrice. When [VibrationExplosion] is triggered on the target, reduce target's [Vibration] Count by 3 (max 9 [Vibration] Count reduction)
   PL: [CriticalOnSucceedAttack] uruchamia [VibrationExplosion] 3 razy. gdy [VibrationExplosion] uruchamia się na celu, zmniejsza Licznik [Vibration] celu o 3 za każde [VibrationExplosion] (maks. zmniejszenie o 9 Licznika [Vibration])
79. [Umiejętność wroga [108205] (ulepszenie 1) — nazwa] 고찰
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108205].levelList[level=1].name
   limit: do 40 znaków
   EN: Contemplation
   PL: Contemplation
80. [Umiejętność wroga [108205] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력 3당 최종 위력 +1 (최대 5)\n[WhenUse] [Breath] 위력 4 얻음\n- 보호막이 있으면, [Breath] 횟수 2 추가로 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108205].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Final Power +1 for [Breath] Potency on self (max 5)\n[WhenUse] Gain 4 [Breath] Potency\n- If this unit has Shield, gain +2 [Breath] Count as well
   PL: [WhenUse] Moc Końcowa +1 za każde 3 Siły [Breath] jednostki (maks. 5)\n[WhenUse] zyskuje 4 Siły [Breath]\n- jeżeli jednostka ma Tarczę, zyskuje dodatkowo 2 Licznika [Breath]
81. [Umiejętność wroga [137801] (ulepszenie 1) — nazwa] 압착
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137801].levelList[level=1].name
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Umiejętność wroga [137801] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력 5당 최종 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137801].levelList[level=1].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność wroga [137801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 위력 2 부여
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Umiejętność wroga [137801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Vibration] 위력 3 부여, 대상의 [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Umiejętność wroga [137802] (ulepszenie 1) — nazwa] 분해
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137802].levelList[level=1].name
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Umiejętność wroga [137802] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력 3당 최종 위력 +1 (최대 5)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] 대상의 [ObservedPerson]가 20 이상이면, 이 스킬의 코인이 [SuperCoin]으로 변경됨</u></b></mark></color>
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137802].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [Breath], [ObservedPerson], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [ObservedPerson] = 피관찰자 / Subject of Observation; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Final Power +1 for every 3 [Breath] Potency on self (max 5)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] If the target has 20+ [ObservedPerson], convert all Coins on this Skill to [SuperCoin]s</u></b></mark></color>
   PL: [WhenUse] Moc Końcowa +1 za każde 3 Siły [Breath] jednostki (maks. 5)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] jeżeli cel ma 20+ [ObservedPerson], zmienia Monety tej Umiejętności w [SuperCoin]y</u></b></mark></color>
87. [Umiejętność wroga [137802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 위력 3 부여
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Umiejętność wroga [137802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [WinDuelAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Umiejętność wroga [137802] (ulepszenie 1) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] [VibrationExplosion] 1회. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137802].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [CriticalOnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [CriticalOnSucceedAttack] uruchamia [VibrationExplosion] raz; następnie zmniejsza Licznik [Vibration] celu o 1
90. [Umiejętność wroga [137803] (ulepszenie 1) — nazwa] 분석 시행
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137803].levelList[level=1].name
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Umiejętność wroga [137803] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력이 10 이상이면, [Breath] 위력을 소모하여 소모한 [Breath] 위력 3당 최종 위력 +2 (최대 4)
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137803].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] At 10+ [Breath] Potency, consume [Breath] Potency to gain +2 Final Power for every 3 [Breath] Potency consumed (max 4)
   PL: [WhenUse] przy 10+ Siły [Breath], zużywa Siłę [Breath], by zyskać +2 Mocy Końcowej za każde 3 zużytej Siły [Breath] (maks. 4)
92. [Umiejętność wroga [137803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [Umiejętność wroga [137803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 5 이상이면 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 5+ [Vibration] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] jeżeli cel ma 5+ Licznika [Vibration], uruchamia [VibrationExplosion]; następnie zmniejsza Licznik [Vibration] celu o 1
94. [Umiejętność wroga [137803] (ulepszenie 1) — moneta 1, efekt 3 — opis] [WinDuelAttack] [Vibration] 위력 5 부여, [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137803].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Umiejętność wroga [137803] (ulepszenie 1) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137803].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [CriticalOnSucceedAttack] Trigger [VibrationExplosion] twice; then, reduce target's [Vibration] Count by 2
   PL: [CriticalOnSucceedAttack] uruchamia [VibrationExplosion] 2 razy; następnie zmniejsza Licznik [Vibration] celu o 2
96. [Umiejętność wroga [137804] (ulepszenie 1) — nazwa] 소멸 시퀀스 가동
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137804].levelList[level=1].name
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Umiejętność wroga [137804] (ulepszenie 1) — opis] [WhenUse] [Breath] 위력과 [Breath] 횟수를 절반만큼 소모\n- (소모한 [Breath] 위력과 [Breath] 횟수의 합/2)만큼 최종 위력이 증가 (최대 20)\n- (소모한 [Breath] 위력 x 2)%만큼 피해량이 증가 (최대 50%)\n- (소모한 [Breath] 횟수 x 4)%만큼 크리티컬 피해량이 증가 (최대 100%)\n[DefeatDuel] 남은 [Breath] 횟수가 절반으로 감소
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137804].levelList[level=1].desc
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Umiejętność wroga [137804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Umiejętność wroga [137804] (ulepszenie 1) — moneta 1, efekt 2 — opis] 직전 턴에 체력 피해를 받지 않았다면, 크리티컬로 적중
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137804].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Umiejętność wroga [137804] (ulepszenie 1) — moneta 1, efekt 3 — opis] 직전 턴에 체력 피해를 받았다면, 크리티컬로 적중하지 않고 피해량이 80%만큼 감소
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137804].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Umiejętność wroga [137804] (ulepszenie 1) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] [VibrationExplosion] 3회. 대상의 [Vibration] 횟수 3 감소
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137804].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [CriticalOnSucceedAttack] Trigger [VibrationExplosion] thrice; then, reduce target's [Vibration] Count by 3
   PL: [CriticalOnSucceedAttack] uruchamia [VibrationExplosion] 3 razy; następnie zmniejsza Licznik [Vibration] celu o 3
102. [Umiejętność wroga [137805] (ulepszenie 1) — nazwa] 고찰
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137805].levelList[level=1].name
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Umiejętność wroga [137805] (ulepszenie 1) — opis] [CanDuelGuard]\n[WhenUse] 자신의 [Breath] 위력 3당 최종 위력 +1 (최대 5)\n[WhenUse] [Breath] 위력 4 얻음\n- 보호막이 있으면, [Breath] 횟수 2 추가로 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137805].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WhenUse], [Breath]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [CanDuelGuard]\n[WhenUse] Final Power +1 for every 3 [Breath] Potency on self (max 5)\n[WhenUse] Gain 4 [Breath] Potency\n- If this unit has Shield, gain +2 [Breath] Count as well
   PL: [CanDuelGuard]\n[WhenUse] Moc Końcowa +1 za każde 3 Siły [Breath] jednostki (maks. 5)\n[WhenUse] zyskuje 4 Siły [Breath]\n- jeżeli jednostka ma Tarczę, zyskuje dodatkowo 2 Licznika [Breath]
104. [Umiejętność wroga [137805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=137805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c971] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c971
- grupa rozdziału/trybu: `a1c971` · plik: `Skills_Enemy-a1c971.json`

105. [Umiejętność wroga [9018101] (ulepszenie 1) — nazwa] ■■라
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018101].levelList[level=1].name
   limit: do 40 znaków
   EN: ■■ew
   PL: ■■ew
106. [Umiejętność wroga [9018101] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Burst]이 없다면, 합 위력 +1
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If the target does not have [Burst], Clash Power +1
   PL: [WhenUse] jeżeli cel nie ma [Burst], Moc Starcia +1
107. [Umiejętność wroga [9018101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL: [OnSucceedAttack] nakłada 3 [Burst]
108. [Umiejętność wroga [9018101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 2 피해
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 2 SP damage
   PL: [OnSucceedAttack] zadaje 2 obrażeń SP
109. [Umiejętność wroga [9018102] (ulepszenie 1) — nazwa] ■어 ■■자
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018102].levelList[level=1].name
   limit: do 40 znaków
   EN: Le■'■ ■■t
   PL: Le■'■ ■■t
110. [Umiejętność wroga [9018102] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 5+ [Burst], Coin Power +1
   PL: [WhenUse] jeżeli cel ma 5+ [Burst], Moc Monety +1
111. [Umiejętność wroga [9018102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Burst]
112. [Umiejętność wroga [9018102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 3 피해
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 3 SP damage
   PL: [OnSucceedAttack] zadaje 3 obrażeń SP
113. [Umiejętność wroga [9018102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Umiejętność wroga [9018102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 입힌 체력 피해량만큼 체력 회복 (최대 20)
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal HP equal to damage dealt (Max 20)
   PL: [OnSucceedAttack] przywraca HP równe zadanym obrażeniom HP (maks. 20)
115. [Umiejętność wroga [9018102] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 정신력 5 피해
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018102].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 SP damage
   PL: [OnSucceedAttack] zadaje 5 obrażeń SP
116. [Umiejętność wroga [9018103] (ulepszenie 1) — nazwa] 이■엔 ■야!!
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018103].levelList[level=1].name
   limit: do 40 znaków
   EN: I■'s Y■■r ■■rn N■■!!
   PL: I■'s Y■■r ■■rn N■■!!
117. [Umiejętność wroga [9018103] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 3 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018103].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Coin Power +1 for every 3 [Burst] on target (max 2)
   PL: [WhenUse] Moc Monety +1 za każde 3 [Burst] celu (maks. 2)
118. [Umiejętność wroga [9018103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Burst]
119. [Umiejętność wroga [9018103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Umiejętność wroga [9018103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량만큼 체력 회복 (최대 20)
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal HP equal to damage dealt (Max 20)
   PL: [OnSucceedAttack] przywraca HP równe zadanym obrażeniom (maks. 20)
121. [Umiejętność wroga [9018103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 50% 미만이면, 코인 1회 재사용
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At less than 50% HP, Reuse Coin once
   PL: [OnSucceedAttack] przy HP niższym niż 50% Maks. HP, używa Monety ponownie raz
122. [Umiejętność wroga [9018103] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018103].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Umiejętność wroga [9018103] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 정신력 10 피해
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018103].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 10 SP damage
   PL: [OnSucceedAttack] zadaje 10 obrażeń SP
124. [Umiejętność wroga [9018103] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 피해량만큼 체력 회복 (최대 20)
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018103].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Umiejętność wroga [9018104] (ulepszenie 1) — nazwa] 가■
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018104].levelList[level=1].name
   limit: do 40 znaków
   EN: Gua■■
   PL: Gua■■
126. [Umiejętność wroga [9018104] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]당 5의 보호막 체력 얻음\n[EndBattle] 남은 보호막 수치만큼 체력 회복
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018104].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [WhenUse] Gain Shield HP for every 5 [Burst] on the target\n[EndBattle] Heal HP equal to the remaining Shield HP
   PL: [WhenUse] zyskuje HP Tarczy za każde 5 [Burst] celu\n[EndBattle] przywraca HP równe pozostałej Tarczy
127. [Umiejętność wroga [9018201] (ulepszenie 1) — nazwa] 으■■하
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018201].levelList[level=1].name
   limit: do 40 znaków
   EN: Wa■■■■ha
   PL: Wa■■■■ha
128. [Umiejętność wroga [9018201] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Burst]이 없다면, 합 위력 +1
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018201].levelList[level=1].desc
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Umiejętność wroga [9018201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Umiejętność wroga [9018201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 2 피해
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Umiejętność wroga [9018202] (ulepszenie 1) — nazwa] ■■자
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018202].levelList[level=1].name
   limit: do 40 znaków
   EN: C■■an
   PL: C■■an
132. [Umiejętność wroga [9018202] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018202].levelList[level=1].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Umiejętność wroga [9018202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Umiejętność wroga [9018202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 3 피해
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Umiejętność wroga [9018202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Burst]
   PL: [OnSucceedAttack] nakłada 4 [Burst]
136. [Umiejętność wroga [9018202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 입힌 체력 피해량만큼 체력 회복 (최대 20)
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Umiejętność wroga [9018202] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 정신력 5 피해
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018202].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Umiejętność wroga [9018203] (ulepszenie 1) — nazwa] 식■ ■간이다!
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018203].levelList[level=1].name
   limit: do 40 znaków
   EN: Ti■■ to E■■!
   PL: Ti■■ to E■■!
139. [Umiejętność wroga [9018203] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 3 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018203].levelList[level=1].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Umiejętność wroga [9018203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Umiejętność wroga [9018203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [Umiejętność wroga [9018203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량만큼 체력 회복 (최대 20)
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność wroga [9018203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 50% 미만이면, 코인 1회 재사용
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Umiejętność wroga [9018203] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018203].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Umiejętność wroga [9018203] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 정신력 10 피해
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018203].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Umiejętność wroga [9018203] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 피해량만큼 체력 회복 (최대 20)
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018203].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Umiejętność wroga [9018204] (ulepszenie 1) — nazwa] ■드
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018204].levelList[level=1].name
   limit: do 40 znaków
   EN: ■■■rd
   PL: ■■■rd
148. [Umiejętność wroga [9018204] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]당 5의 보호막 체력 얻음\n[EndBattle] 남은 보호막 수치만큼 체력 회복
   źródło: Skills_Enemy-a1c971.json :: dataList[id=9018204].levelList[level=1].desc
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c9p1] Wróg / część: Enemies-a1c9p1
- plik gry: `Enemies-a1c9p1.json`

149. [[a1c9p1] Wróg / część [91036] — nazwa] 약지 신체파 자동인형- 연구원
   źródło: Enemies-a1c9p1.json :: dataList[id=91036].name
   limit: do 60 znaków
   EN: The Ring Corporist Automanikin - Researcher
   PL: The Ring Corporist Automanikin - Researcher
150. [[a1c9p1] Wróg / część [91037] — nazwa] 약지 신체파 자동인형- 전투원
   źródło: Enemies-a1c9p1.json :: dataList[id=91037].name
   limit: do 60 znaków
   EN: The Ring Corporist Automanikin - Combatant
   PL: The Ring Corporist Automanikin - Combatant
151. [[a1c9p1] Wróg / część [91038] — nazwa] 약지 신체파 자동인형- 분홍욕망 침식
   źródło: Enemies-a1c9p1.json :: dataList[id=91038].name
   limit: do 80 znaków
   EN: The Ring Corporist Automanikin - Roseate Desire Corrosion
   PL: The Ring Corporist Automanikin - Roseate Desire Corrosion
152. [[a1c9p1] Wróg / część [1306] — nazwa] 엄지 제자 - 루치오
   źródło: Enemies-a1c9p1.json :: dataList[id=1306].name
   limit: do 40 znaków
   EN: The Thumb Apprentice - Lucio
   PL: The Thumb Apprentice - Lucio
153. [[a1c9p1] Wróg / część [130601] — nazwa] 몸통
   źródło: Enemies-a1c9p1.json :: dataList[id=130601].name
   limit: do 40 znaków
   EN: Body
   PL: Korpus
154. [[a1c9p1] Wróg / część [130601] — opis] 부위
   źródło: Enemies-a1c9p1.json :: dataList[id=130601].desc
   limit: do 120 znaków
   EN: Part
   PL: Część
155. [[a1c9p1] Wróg / część [1315] — nazwa] 약지 신체파 자동인형- 연구원
   źródło: Enemies-a1c9p1.json :: dataList[id=1315].name
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [[a1c9p1] Wróg / część [131501] — nazwa] 몸통
   źródło: Enemies-a1c9p1.json :: dataList[id=131501].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [[a1c9p1] Wróg / część [131501] — opis] 부위
   źródło: Enemies-a1c9p1.json :: dataList[id=131501].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [[a1c9p1] Wróg / część [1316] — nazwa] 약지 신체파 자동인형- 전투원
   źródło: Enemies-a1c9p1.json :: dataList[id=1316].name
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [[a1c9p1] Wróg / część [131601] — nazwa] 몸통
   źródło: Enemies-a1c9p1.json :: dataList[id=131601].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [[a1c9p1] Wróg / część [131601] — opis] 부위
   źródło: Enemies-a1c9p1.json :: dataList[id=131601].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [[a1c9p1] Wróg / część [1317] — nazwa] 약지 신체파 자동인형- 분홍욕망 침식
   źródło: Enemies-a1c9p1.json :: dataList[id=1317].name
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [[a1c9p1] Wróg / część [131701] — nazwa] 몸통
   źródło: Enemies-a1c9p1.json :: dataList[id=131701].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [[a1c9p1] Wróg / część [131701] — opis] 부위
   źródło: Enemies-a1c9p1.json :: dataList[id=131701].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [[a1c9p1] Wróg / część [1318] — nazwa] 소지 제자 - 렌
   źródło: Enemies-a1c9p1.json :: dataList[id=1318].name
   limit: do 40 znaków
   EN: The Pinky Apprentice - Ren
   PL: The Pinky Apprentice - Ren
165. [[a1c9p1] Wróg / część [131801] — nazwa] 몸통
   źródło: Enemies-a1c9p1.json :: dataList[id=131801].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [[a1c9p1] Wróg / część [131801] — opis] 부위
   źródło: Enemies-a1c9p1.json :: dataList[id=131801].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [[a1c9p1] Wróg / część [1319] — nazwa] 약지 제자 - 알비나
   źródło: Enemies-a1c9p1.json :: dataList[id=1319].name
   limit: do 40 znaków
   EN: The Ring Apprentice - Albina
   PL: The Ring Apprentice - Albina
168. [[a1c9p1] Wróg / część [131901] — nazwa] 몸통
   źródło: Enemies-a1c9p1.json :: dataList[id=131901].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [[a1c9p1] Wróg / część [131901] — opis] 부위
   źródło: Enemies-a1c9p1.json :: dataList[id=131901].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c9p1] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c9p1
- grupa rozdziału/trybu: `a1c9p1` · plik: `Skills_Abnormality-a1c9p1.json`

170. [Umiejętność wroga [130601] (ulepszenie 1) — nazwa] 팔레르모 스파다
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130601].levelList[level=1].name
   limit: do 40 znaków
   EN: La Spada di Palermo
   PL: La Spada di Palermo
171. [Umiejętność wroga [130601] (ulepszenie 1) — opis] 대상의 [Vibration]이 6 이상이면, 합 위력 + 1
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 6+ [Vibration], Clash Power +1
   PL: jeżeli cel ma 6+ [Vibration], Moc Starcia +1
172. [Umiejętność wroga [130601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] nakłada 2 [Vibration]
173. [Umiejętność wroga [130601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Umiejętność wroga [130602] (ulepszenie 1) — nazwa] 콜피 소타니
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130602].levelList[level=1].name
   limit: do 40 znaków
   EN: Colpi Sottani
   PL: Colpi Sottani
175. [Umiejętność wroga [130602] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Vibration]의 합 4당, 기본 위력 + 1 (최대 2)
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: Base Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 2)
   PL: Moc Bazowa +1 za każde 4 łącznie ([Combustion] + [Vibration]) celu (maks. 2)
176. [Umiejętność wroga [130602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가.
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Vibration].
177. [Umiejętność wroga [130602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion] and +2 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 2 [Combustion] i 2 Licznika [Combustion]
178. [Umiejętność wroga [130602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 2 [Vibration] i 2 Licznika [Vibration]
179. [Umiejętność wroga [130602] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130602].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Umiejętność wroga [130602] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130602].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] uruchamia [VibrationExplosion]; następnie zmniejsza Licznik [Vibration] celu o 1
181. [Umiejętność wroga [130603] (ulepszenie 1) — nazwa] 카치아토레
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130603].levelList[level=1].name
   limit: do 40 znaków
   EN: Il Cacciatore
   PL: Il Cacciatore
182. [Umiejętność wroga [130603] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Vibration]의 합 4당, 코인 위력 + 1 (최대 2)\n\n[WhenUse] 대상에게 [DuelEdge]가 있다면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130603].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Vibration], [WhenUse], [DuelEdge], [SuperCoin]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [WhenUse] = [사용시] / [On Use]; [DuelEdge] = 결투 고조 / The Duel Escalates; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Coin Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 2)\n\n[WhenUse] If target has [DuelEdge], convert all Coins on this Skill to [SuperCoin]s
   PL: Moc Monety +1 za każde 4 łącznie ([Combustion] + [Vibration]) celu (maks. 2)\n\n[WhenUse] jeżeli cel ma [DuelEdge], zmienia wszystkie Monety tej Umiejętności w [SuperCoin]y
183. [Umiejętność wroga [130603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Umiejętność wroga [130603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Umiejętność wroga [130603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationIgnition]로 [FusionVibration]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationIgnition], [FusionVibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: [OnSucceedAttack] Trigger [FusionVibration] into [VibrationIgnition]
   PL: [OnSucceedAttack] uruchamia [FusionVibration], przekształcając je w [VibrationIgnition]
186. [Umiejętność wroga [130603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność wroga [130603] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Agility] 2 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130603].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Agility]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttackHead] Gain 2 [Agility] next turn
   PL: [OnSucceedAttackHead] zyskuje 2 [Agility] w następnej turze
188. [Umiejętność wroga [130604] (ulepszenie 1) — nazwa] 세치오나투라 디 체르보
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130604].levelList[level=1].name
   limit: do 40 znaków
   EN: Sezionatura di Cervo
   PL: Sezionatura di Cervo
189. [Umiejętność wroga [130604] (ulepszenie 1) — opis] [CantChangeTarget]\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n\n이번 턴동안 <color=#ff6000><mark color=#ff000040><b><u>합 패배한 공격 스킬</color></mark></b></u> 1당, 최종 위력 -2, 가중치 -1\n(가중치 최소 1 이하로 내려가지 않음)\n\n[DefeatDuel] 피해량 90% 감소, 해당 피해로 흐트러짐이 발생하지 않음\n[DefeatDuel] 정신력 15 감소, 다음 턴 공격 레벨 감소 6 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130604].levelList[level=1].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [CantChangeTarget], [DefeatDuel]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [CantChangeTarget]\nCannot be Staggered before using this Skill\n\nFor <color=#ff6000><mark color=#ff000040><b><u>every Attack Skill of this unit that lost a Clash this turn</color></mark></b></u>, Final Power -2 and Atk Weight -1\n(Min. Atk Weight: 1)\n\n[DefeatDuel] Deal -90% damage and damage dealt by this Skill cannot Stagger the target\n[DefeatDuel] Lose 15 SP; next turn, gain 6 Offense Level Down
   PL: [CantChangeTarget]\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n\nza każdą w tej turze <color=#ff6000><mark color=#ff000040><b><u>Umiejętność ataku, która przegrała Starcie</u></b></mark></color>, Moc Końcowa -2 i Waga Ataku -1\n(Waga Ataku nie spada poniżej 1)\n\n[DefeatDuel] zadaje o 90% mniej obrażeń, a zadawane obrażenia nie powodują Oszołamienia\n[DefeatDuel] traci 15 SP; w następnej turze zyskuje 6 Spadku Poziomu Ataku
190. [Umiejętność wroga [130604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Umiejętność wroga [130604] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130604].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [130604] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130604].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność wroga [130604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Umiejętność wroga [130604] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130604].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Umiejętność wroga [130604] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130604].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Umiejętność wroga [130604] (ulepszenie 1) — moneta 2, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [FusionVibration]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130604].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationIgnition], [FusionVibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [FusionVibration] into [VibrationIgnition]
   PL: [UnBrokenCoinOnSucceedAttack] uruchamia [FusionVibration], przekształcając je w [VibrationIgnition]
197. [Umiejętność wroga [130604] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130604].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Umiejętność wroga [130604] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130604].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2
   PL: [UnBrokenCoinOnSucceedAttack] uruchamia [VibrationExplosion] 2 razy; następnie zmniejsza Licznik [Vibration] celu o 2
199. [Umiejętność wroga [130604] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130604].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Umiejętność wroga [130604] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130604].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 198 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Umiejętność wroga [130605] (ulepszenie 1) — nazwa] 검끝 재기
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130605].levelList[level=1].name
   limit: do 40 znaków
   EN: Measuring Blade Reach
   PL: Measuring Blade Reach
202. [Umiejętność wroga [130605] (ulepszenie 1) — opis] [DuelCounter]\n대상의 [DuelEdge]가 2 이상이면 피해량 +30%\n\n[WinDuel] 대상에게 [DuelEdge] 1 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130605].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [DuelEdge], [WinDuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [DuelEdge] = 결투 고조 / The Duel Escalates; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [DuelCounter]\nIf target has 2+ [DuelEdge], deal +30% damage\n\n[WinDuel] Inflict 1 [DuelEdge]
   PL: [DuelCounter]\njeżeli cel ma 2+ [DuelEdge], zadaje +30% obrażeń\n\n[WinDuel] nakłada 1 [DuelEdge]
203. [Umiejętność wroga [130605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Umiejętność wroga [130605] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130605].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Umiejętność wroga [130701] (ulepszenie 1) — nazwa] 허무의 열매
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130701].levelList[level=1].name
   limit: do 40 znaków
   EN: Vain Fruit
   PL: Vain Fruit
206. [Umiejętność wroga [130701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] nakłada 4 [Laceration]
207. [Umiejętność wroga [130702] (ulepszenie 1) — nazwa] 백설을 데려와라.
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130702].levelList[level=1].name
   limit: do 40 znaków
   EN: Bring Me Snow White.
   PL: Bring Me Snow White.
208. [Umiejętność wroga [130702] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Burst]의 합이 5 이상이면 기본 위력 +5\n[WhenUse] 자신이 [HowDareYouApple]를 보유 중이면, 공격 가중치 +2
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130702].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [Burst], [HowDareYouApple]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [HowDareYouApple] = 감히…! / The Audacity...!
   EN: [WhenUse] At 5+ ([Laceration] + [Burst]) on target, Base Power +5\n[WhenUse] If this unit has [HowDareYouApple], gain +2 Atk Weight
   PL: [WhenUse] przy 5+ łącznie ([Laceration] + [Burst]) celu, Moc Bazowa +5\n[WhenUse] jeżeli ta jednostka ma [HowDareYouApple], zyskuje Wagę Ataku +2
209. [Umiejętność wroga [130702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 정신 피해 10
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 10 SP damage
   PL: [OnSucceedAttack] zadaje 10 obrażeń SP
210. [Umiejętność wroga [130703] (ulepszenie 1) — nazwa] 감히 무엄하구나!
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130703].levelList[level=1].name
   limit: do 40 znaków
   EN: Such Insolence!
   PL: Such Insolence!
211. [Umiejętność wroga [130703] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Burst]의 합 4당 코인 위력 +2 (최대 4)\n[WhenUse] 자신이 [HowDareYouApple]를 보유 중이면, 공격 가중치 +2\n[DefeatDuel] 아래 효과 적용\n- [Paralysis] 2 얻음\n- 피해량이 80%만큼 감소함\n- 이 스킬로 대상이 흐트러지지 않음\n- 대상의 [Burst] 효과를 발동시키지 않음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130703].levelList[level=1].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [Burst], [HowDareYouApple], [DefeatDuel], [Paralysis]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [HowDareYouApple] = 감히…! / The Audacity...!; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze
   EN: [WhenUse] Coin Power +2 for every 4 ([Laceration] + [Burst]) on target (max 4)\n[WhenUse] If this unit has [HowDareYouApple], gain +2 Atk Weight\n[DefeatDuel] Gain the following effects:\n- Gain 2 [Paralysis]\n- Deal -80% damage\n- This Skill cannot Stagger the target\n- Does not activate [Burst] on target
   PL: [WhenUse] Moc Monety +2 za każde 4 łącznie ([Laceration] + [Burst]) celu (maks. 4)\n[WhenUse] jeżeli ta jednostka ma [HowDareYouApple], zyskuje Wagę Ataku +2\n[DefeatDuel] zyskuje następujące efekty:\n- zyskuje 2 [Paralysis]\n- zadaje o 80% mniej obrażeń\n- ta Umiejętność nie może Oszołomić celu\n- nie uruchamia [Burst] celu
212. [Umiejętność wroga [130703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Umiejętność wroga [130703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 정신 피해 5
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 SP damage
   PL: [OnSucceedAttack] zadaje 5 obrażeń SP
214. [Umiejętność wroga [130703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Umiejętność wroga [130703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 정신 피해 5
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 213 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Umiejętność wroga [130704] (ulepszenie 1) — nazwa] 조금만 더...
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130704].levelList[level=1].name
   limit: do 40 znaków
   EN: Just a Little More...
   PL: Just a Little More...
217. [Umiejętność wroga [130705] (ulepszenie 1) — nazwa] 불신
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130705].levelList[level=1].name
   limit: do 40 znaków
   EN: Distrust
   PL: Distrust
218. [Umiejętność wroga [130705] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Burst]의 합 3당 코인 위력 +2 (최대 4)
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130705].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [WhenUse] Coin Power +2 for every 3 ([Laceration] + [Burst]) on target (max 4)
   PL: [WhenUse] Moc Monety +2 za każde 3 łącznie ([Laceration] + [Burst]) celu (maks. 4)
219. [Umiejętność wroga [130705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Laceration]
220. [Umiejętność wroga [130705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność wroga [130705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] nakłada 3 [Laceration]
222. [Umiejętność wroga [130705] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130705].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Umiejętność wroga [130706] (ulepszenie 1) — nazwa] 빛바랜 줄기
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130706].levelList[level=1].name
   limit: do 40 znaków
   EN: Pale Stem
   PL: Pale Stem
224. [Umiejętność wroga [130706] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Burst]의 합 4당 최종 위력 +3 (최대 6)
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130706].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [WhenUse] Final Power +3 for every 4 ([Laceration] + [Burst]) on target (max 6)
   PL: [WhenUse] Moc Końcowa +3 za każde 4 łącznie ([Laceration] + [Burst]) celu (maks. 6)
225. [Umiejętność wroga [130706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność wroga [130706] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130706].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność wroga [130707] (ulepszenie 1) — nazwa] 가시 줄기
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130707].levelList[level=1].name
   limit: do 40 znaków
   EN: Thorny Stem
   PL: Thorny Stem
228. [Umiejętność wroga [130707] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Burst]의 합 4당 최종 위력 +3 (최대 6)
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130707].levelList[level=1].desc
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Umiejętność wroga [130707] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130707].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Umiejętność wroga [130707] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130707].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Umiejętność wroga [130708] (ulepszenie 1) — nazwa] 모두의 아픔
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130708].levelList[level=1].name
   limit: do 40 znaków
   EN: Shared Pain
   PL: Shared Pain
232. [Umiejętność wroga [130708] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Burst]의 합 4당 최종 위력 +3 (최대 6)
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130708].levelList[level=1].desc
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Umiejętność wroga [130708] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130708].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Umiejętność wroga [130708] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Vulnerable] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130708].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Vulnerable] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Vulnerable] w następnej turze
235. [Umiejętność wroga [130709] (ulepszenie 1) — nazwa] 뿌리 가시
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130709].levelList[level=1].name
   limit: do 40 znaków
   EN: Root Spike
   PL: Root Spike
236. [Umiejętność wroga [130709] (ulepszenie 1) — opis] [DefeatDuel] 아래 효과 적용\n- [Paralysis] 1 얻음\n- 피해량이 80%만큼 감소함\n- 이 스킬로 대상이 흐트러지지 않음\n- 대상의 [Burst] 효과를 발동시키지 않음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130709].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel], [Paralysis], [Burst]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze; [Burst] = 파열 / Rupture
   EN: [DefeatDuel] Gain the following effects:\n- Gain 1 [Paralysis]\n- Deal -80% damage\n- This Skill cannot Stagger the target\n- Does not activate [Burst] on target
   PL: [DefeatDuel] zyskuje następujące efekty:\n- zyskuje 1 [Paralysis]\n- zadaje o 80% mniej obrażeń\n- ta Umiejętność nie może Oszołomić celu\n- nie uruchamia [Burst] celu
237. [Umiejętność wroga [130709] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130709].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [Umiejętność wroga [130709] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Laceration] 횟수 5 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130709].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +5 [Laceration] Count next turn
   PL: [OnSucceedAttack] nakłada 5 Licznika [Laceration] w następnej turze
239. [Umiejętność wroga [130709] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 부정적인 효과 위력의 합 만큼 [Laceration] 혹은 [Burst] 부여 (최대 부여량 30)
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130709].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict (sum of potency from all negative effects on target) [Laceration] or [Burst] (max 30)
   PL: [UnBrokenCoinOnSucceedAttack] nakłada [Laceration] albo [Burst] równe sumie Siły negatywnych efektów celu (maks. nakład 30)
240. [Umiejętność wroga [130711] (ulepszenie 1) — nazwa] 질투하는 뿌리
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130711].levelList[level=1].name
   limit: do 40 znaków
   EN: Envying Roots
   PL: Envying Roots
241. [Umiejętność wroga [130711] (ulepszenie 1) — opis] 이 스킬은 피해를 주지 않음\n[WhenUse] 자신의 [HowDareYouApple]를 전부 소모하여, 소모한만큼 코인을 재사용함 (최대 4회)\n[DefeatDuel] 이 스킬로 [Burst] 효과를 발동하지 않음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130711].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [HowDareYouApple], [DefeatDuel], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [HowDareYouApple] = 감히…! / The Audacity...!; [DefeatDuel] = [합 패배] / [Clash Lose]; [Burst] = 파열 / Rupture
   EN: This Skill does not deal damage\n[WhenUse] Consume all [HowDareYouApple] on self and Reuse its Coins by [HowDareYouApple] Stack consumed (max 4)\n[DefeatDuel] This Skill does not activate [Burst] on target
   PL: ta Umiejętność nie zadaje obrażeń\n[WhenUse] zużywa wszystkie [HowDareYouApple] jednostki i używa Monety ponownie tyle razy, ile zużyto Liczników [HowDareYouApple] (do 4 razy)\n[DefeatDuel] ta Umiejętność nie uruchamia [Burst] celu
242. [Umiejętność wroga [130711] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130711].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Umiejętność wroga [130711] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130711].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 [Laceration] i 2 Licznika [Laceration]
244. [Umiejętność wroga [130711] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Burst] 3 부여, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130711].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst] and +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 3 [Burst] i 2 Licznika [Burst]
245. [Umiejętność wroga [130712] (ulepszenie 1) — nazwa] 파고드는 뿌리
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130712].levelList[level=1].name
   limit: do 40 znaków
   EN: Burrowing Roots
   PL: Burrowing Roots
246. [Umiejętność wroga [130712] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Burst]의 합 4당 합 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130712].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [WhenUse] Clash Power +1 for every 4 ([Laceration] + [Burst]) on target (max 2)
   PL: [WhenUse] Moc Starcia +1 za każde 4 łącznie ([Laceration] + [Burst]) celu (maks. 2)
247. [Umiejętność wroga [130712] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130712].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [Umiejętność wroga [130713] (ulepszenie 1) — nazwa] 허무의 열매
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130713].levelList[level=1].name
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Umiejętność wroga [131901] (ulepszenie 1) — nazwa] 도축 - 갈비뼈
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131901].levelList[level=1].name
   limit: do 40 znaków
   EN: Butcher - Ribs
   PL: Butcher - Ribs
250. [Umiejętność wroga [131901] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 6+ [Laceration], Coin Power +1
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1
251. [Umiejętność wroga [131901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Umiejętność wroga [131901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 1 [Vulnerable] w następnej turze
253. [Umiejętność wroga [131901] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131901].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Protection]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Protection] = 보호 / Protection
   EN: [OnSucceedAttack] Gain 1 [Protection] next turn
   PL: [OnSucceedAttack] zyskuje 1 [Protection] w następnej turze
254. [Umiejętność wroga [131902] (ulepszenie 1) — nazwa] 회전분쇄
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131902].levelList[level=1].name
   limit: do 40 znaków
   EN: Rotator Crush
   PL: Rotator Crush
255. [Umiejętność wroga [131902] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131902].levelList[level=1].desc
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Umiejętność wroga [131902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Umiejętność wroga [131902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 1 [Binding] w następnej turze
258. [Umiejętność wroga [131902] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 1 [Agility] next turn
   PL: [OnSucceedAttack] zyskuje 1 [Agility] w następnej turze
259. [Umiejętność wroga [131903] (ulepszenie 1) — nazwa] 힘줄파열
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131903].levelList[level=1].name
   limit: do 40 znaków
   EN: Tendon Tear
   PL: Tendon Tear
260. [Umiejętność wroga [131903] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131903].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Coin Power +1 for every 4 [Laceration] on target (max 2)
   PL: [WhenUse] Moc Monety +1 za każde 4 [Laceration] celu (maks. 2)
261. [Umiejętność wroga [131903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]
   PL: [OnSucceedAttack] nakłada 6 [Laceration]
262. [Umiejętność wroga [131903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 1 Licznika [Laceration]
263. [Umiejętność wroga [131903] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [ResultReduction] 1 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131903].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ResultReduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ResultReduction] = 위력 감소 / Power Down
   EN: [OnSucceedAttack] Inflict 1 [ResultReduction] next turn
   PL: [OnSucceedAttack] nakłada 1 [ResultReduction] w następnej turze
264. [Umiejętność wroga [131903] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ResultEnhancement] 1 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131903].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ResultEnhancement]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ResultEnhancement] = 위력 증가 / Power Up
   EN: [OnSucceedAttack] Gain 1 [ResultEnhancement] next turn
   PL: [OnSucceedAttack] zyskuje 1 [ResultEnhancement] w następnej turze
265. [Umiejętność wroga [131904] (ulepszenie 1) — nazwa] 파시아가 굶주렸어
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131904].levelList[level=1].name
   limit: do 40 znaków
   EN: Fascia Hungers
   PL: Fascia Hungers
266. [Umiejętność wroga [131904] (ulepszenie 1) — opis] [DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
267. [Umiejętność wroga [131904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Umiejętność wroga [131904] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 10 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131904].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 10 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 10 [Laceration]
269. [Umiejętność wroga [131904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [Umiejętność wroga [131904] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131904].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 Licznika [Laceration]
271. [Umiejętność wroga [131904] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131904].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Umiejętność wroga [131904] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 정신력 피해 5
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131904].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 5 SP damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje 5 obrażeń SP
273. [Umiejętność wroga [131904] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력 5 회복
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131904].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 5 SP on self
   PL: [OnSucceedAttack] przywraca 5 SP jednostki
274. [Umiejętność wroga [131904] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [HumanFleshTheRings] 1 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131904].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [HumanFleshTheRings]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HumanFleshTheRings] = 생체 재료 / Corpus Ingredient
   EN: [OnSucceedAttack] Gain 1 [HumanFleshTheRings]
   PL: [OnSucceedAttack] zyskuje 1 [HumanFleshTheRings]
275. [Umiejętność wroga [131905] (ulepszenie 1) — nazwa] 억압당한 육체
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].name
   limit: do 40 znaków
   EN: Repressed Flesh
   PL: Repressed Flesh
276. [Umiejętność wroga [131905] (ulepszenie 1) — opis] 이 스킬을 장착한 턴에 아래의 효과가 적용됨\n- 이 스킬 사용 전까지 <color=#ff6000><mark=#ff000040><b><u>공격 스킬로 피격 시</u></b></mark></color>, [UnsteadyTheRings] 1 얻음 (적 스킬당 1회, E.G.O 스킬 포함)\n- ‘아이언메이든[TabExplain]- 가시’ 효과가 발동되지 않음\n- 이 스킬 사용 전까지 흐트러짐 상태가 되지 않음\n\n이 스킬로 대상 처치 시, 정신력 15 회복\n[WhenUse] 대상의 [Laceration] 4당 코인 위력 +1 (최대 4)\n[WhenUse] 대상의 [Laceration] 2당 피해량 +10% (최대 100%)\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] [BoneBladeTheRings] 소멸
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [UnsteadyTheRings], [TabExplain], [WhenUse], [Laceration], [DefeatDuel], [EndSkill], [BoneBladeTheRings]
   znaczenie tagów: [UnsteadyTheRings] = 심하게 울리는 갑주 / Impact-rattled Armor; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [BoneBladeTheRings] = 작품명: 파시아 / Artwork: Fascia
   EN: During the turn this unit has this Skill equipped, gain the following effects:\n- <color=#ff6000><mark=#ff000040><b><u>When hit by Attack Skills</u></b></mark></color> before using this Skill, gain 1 [UnsteadyTheRings] (once per enemy Skill; including E.G.O Skills)\n- Does not trigger the effects of "Iron Maiden[TabExplain] - Spikes" Passive\n- This unit cannot be Staggered before using this Skill\n\nOn Kill with this Skill: heal 15 SP\n[WhenUse] Coin Power +1 for every 4 [Laceration] on target (max 4)\n[WhenUse] Deal +10% damage for every 2 [Laceration] on target (max 100%)\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[EndSkill] Lose [BoneBladeTheRings]
   PL: w turze, w której ta jednostka ma wyposażoną tę Umiejętność, obowiązują następujące efekty:\n- przed użyciem tej Umiejętności, <color=#ff6000><mark=#ff000040><b><u>przy otrzymaniu trafienia od Umiejętności ataku</u></b></mark></color>, zyskuje 1 [UnsteadyTheRings] (1 raz na wrogą Umiejętność, włącznie z Umiejętnościami E.G.O)\n- nie uruchamia efektu Pasywu „Iron Maiden[TabExplain] - Spikes”\n- ta jednostka nie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n\nprzy pokonaniu celu tą Umiejętnością przywraca 15 SP\n[WhenUse] Moc Monety +1 za każde 4 [Laceration] celu (maks. 4)\n[WhenUse] zadaje +10% obrażeń za każde 2 [Laceration] celu (maks. 100%)\n[DefeatDuel] obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[EndSkill] traci [BoneBladeTheRings]
277. [Umiejętność wroga [131905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Umiejętność wroga [131905] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 정신력 피해 5
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Umiejętność wroga [131905] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력 5 회복
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Umiejętność wroga [131905] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Umiejętność wroga [131905] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Vulnerable] w następnej turze
282. [Umiejętność wroga [131905] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność wroga [131905] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Umiejętność wroga [131905] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [AttackDmgDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [AttackDmgDown] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [AttackDmgDown] w następnej turze
285. [Umiejętność wroga [131905] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp] 1 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [OnSucceedAttack] Gain 1 [AttackDmgUp] next turn
   PL: [OnSucceedAttack] zyskuje 1 [AttackDmgUp] w następnej turze
286. [Umiejętność wroga [131905] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Umiejętność wroga [131905] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Binding] w następnej turze
288. [Umiejętność wroga [131905] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131905].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 258 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Umiejętność wroga [131906] (ulepszenie 1) — nazwa] 전시회 준비
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131906].levelList[level=1].name
   limit: do 40 znaków
   EN: Exhibition Arrangements
   PL: Exhibition Arrangements
290. [Umiejętność wroga [131906] (ulepszenie 1) — opis] [StartBattle] 공격 스킬로 피격시, 공격자의 [Laceration] 횟수 1 증가 (E.G.O 스킬 포함)
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131906].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Laceration] = 출혈 / Bleed
   EN: [StartBattle] When hit by Attack Skills, inflict +1 [Laceration] Count on the attacker (including E.G.O Skills)
   PL: [StartBattle] przy otrzymaniu trafienia od Umiejętności ataku, nakłada 1 Licznika [Laceration] atakującemu (włącznie z Umiejętnościami E.G.O)
291. [Umiejętność wroga [131907] (ulepszenie 1) — nazwa] 철의 장막
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131907].levelList[level=1].name
   limit: do 40 znaków
   EN: Iron Curtain
   PL: Iron Curtain
292. [Umiejętność wroga [131907] (ulepszenie 1) — opis] 이번 턴에 ‘아이언메이든[TabExplain]- 가시’ 효과로 <color=#ff6000><mark=#ff000040><b><u>적에게 주는 피해량 20배 증가</u></b></mark></color> (이 효과는 상쇄로 인하여 해제되지 않음)\n[StartBattle] 공격 스킬로 피격시, 공격자의 [Laceration] 횟수 1 증가 (E.G.O 스킬 포함)
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131907].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [TabExplain], [StartBattle], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Laceration] = 출혈 / Bleed
   EN: <color=#ff6000><mark=#ff000040><b><u>Multiply the damage from the "Iron Maiden[TabExplain] - Spikes" Passive by 20</u></b></mark></color> (this effect cannot be disabled by Offsetting this Skill)\n[StartBattle] When hit by Attack Skills, inflict +1 [Laceration] Count against the attacker (including E.G.O Skills)
   PL: <color=#ff6000><mark=#ff000040><b><u>zwiększa 20-krotnie obrażenia z Pasywu „Iron Maiden[TabExplain] - Spikes”</u></b></mark></color> (ten efekt nie może zostać wyłączony przez Zrównoważenie tej Umiejętności)\n[StartBattle] przy otrzymaniu trafienia od Umiejętności ataku, nakłada 1 Licznika [Laceration] atakującemu (włącznie z Umiejętnościami E.G.O)
293. [Umiejętność wroga [131801] (ulepszenie 1) — nazwa] 회[回]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131801].levelList[level=1].name
   limit: do 40 znaków
   EN: Swerve [回]
   PL: Swerve [回]
294. [Umiejętność wroga [131801] (ulepszenie 1) — opis] [StartBattle] [Breath] 8 얻음\n- 이 스킬을 사용하는 슬롯에 메인 타겟으로 지정된 공격 스킬이 있으면 이 효과로 얻는 [Breath] 위력 4 감소\n\n[OnSucceedEvade] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131801].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Breath], [OnSucceedEvade]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [StartBattle] Gain 8 [Breath]\n- If the Skill Slot using this Skill is a main target of an Attack Skill, gain 4 fewer [Breath] Potency from this effect\n\n[OnSucceedEvade] Gain 1 [Breath]
   PL: [StartBattle] zyskuje 8 [Breath]\n- jeżeli w slocie tej Umiejętności wskazany jest cel główny Umiejętności ataku, ten efekt daje o 4 mniej Siły [Breath]\n\n[OnSucceedEvade] zyskuje 1 [Breath]
295. [Umiejętność wroga [131802] (ulepszenie 1) — nazwa] 수[守]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131802].levelList[level=1].name
   limit: do 40 znaków
   EN: Defend [守]
   PL: Defend [守]
296. [Umiejętność wroga [131802] (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] 자신의 [Breath] 횟수 4 증가\n- 이 스킬을 사용하는 슬롯에 메인 타겟으로 지정된 공격 스킬이 있으면 이 효과로 얻는 [Breath] 횟수 2 감소\n\n[WinDuel] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131802].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [Breath], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n[StartBattle] Gain +4 [Breath] Count\n- If the Skill Slot using this Skill is a main target of an Attack Skill, gain 2 fewer [Breath] Count from this effect\n\n[WinDuel] Gain +1 [Breath] Count
   PL: [CanDuelGuard]\n[StartBattle] zyskuje 4 Licznika [Breath]\n- jeżeli w slocie tej Umiejętności wskazany jest cel główny Umiejętności ataku, ten efekt daje o 2 mniej Licznika [Breath]\n\n[WinDuel] zyskuje 1 Licznika [Breath]
297. [Umiejętność wroga [131802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Umiejętność wroga [131803] (ulepszenie 1) — nazwa] 반[反]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131803].levelList[level=1].name
   limit: do 40 znaków
   EN: Reflect [反]
   PL: Reflect [反]
299. [Umiejętność wroga [131803] (ulepszenie 1) — opis] [DuelCounter]\n[DefeatDuel] 자신의 [Breath] 횟수 1 감소
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131803].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [DefeatDuel], [Breath]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Breath] = 호흡 / Poise
   EN: [DuelCounter]\n[DefeatDuel] Lose 1 [Breath] Count
   PL: [DuelCounter]\n[DefeatDuel] traci 1 Licznika [Breath]
300. [Umiejętność wroga [131803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL: [OnSucceedAttack] zyskuje 2 Licznika [Breath]
301. [Umiejętność wroga [131804] (ulepszenie 1) — nazwa] 무명섬[無名閃]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131804].levelList[level=1].name
   limit: do 40 znaków
   EN: Unnamed Cut [無名閃]
   PL: Unnamed Cut [無名閃]
302. [Umiejętność wroga [131804] (ulepszenie 1) — moneta 1, efekt 1 — opis] 크리티컬 피해량 +50%
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +50% Damage on Critical Hit
   PL: zadaje +50% obrażeń przy trafieniu krytycznym
303. [Umiejętność wroga [131805] (ulepszenie 1) — nazwa] 연쇄참[連鎖斬]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131805].levelList[level=1].name
   limit: do 40 znaków
   EN: Chainslash [連鎖斬]
   PL: Chainslash [連鎖斬]
304. [Umiejętność wroga [131805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [SlashTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttack] Inflict 1 [SlashTakeDamageUp] next turn
   PL: [OnSucceedAttack] nakłada 1 [SlashTakeDamageUp] w następnej turze
305. [Umiejętność wroga [131807] (ulepszenie 1) — nazwa] 낙성일살[落星一殺]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131807].levelList[level=1].name
   limit: do 40 znaków
   EN: Fallstar Slayer [落星一殺]
   PL: Fallstar Slayer [落星一殺]
306. [Umiejętność wroga [131807] (ulepszenie 1) — opis] 속도에 관계없이 이 스킬과 합을 할 수 있음\n자신의 [DicipleLittleFinger] 1 당 피해량 +1%\n[WhenUse] 자신의 [DicipleLittleFinger] 10 당 코인 위력 +1\n[DefeatDuel] 피해량이 80% 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131807].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [DicipleLittleFinger], [WhenUse], [DefeatDuel]
   znaczenie tagów: [DicipleLittleFinger] = 월하청도 / Moonlit Azure Blade; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed\nDeal +1% damage for every [DicipleLittleFinger] on self\n[WhenUse] Coin Power +1 for every 10 [DicipleLittleFinger] on self\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\nzadaje +1% obrażeń za każdy [DicipleLittleFinger] jednostki\n[WhenUse] Moc Monety +1 za każde 10 [DicipleLittleFinger] jednostki\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
307. [Umiejętność wroga [131807] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131807].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Umiejętność wroga [131807] (ulepszenie 1) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +50%
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131807].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 302 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Umiejętność wroga [131807] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 이 코인 최종 피해량만큼 참격 피해
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131807].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal Slash damage equal to this Coin's final damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje obrażenia Cięcia równe końcowym obrażeniom tej Monety
310. [Umiejętność wroga [131808] (ulepszenie 1) — nazwa] 수세[收勢]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131808].levelList[level=1].name
   limit: do 40 znaków
   EN: Retreat Form [收勢]
   PL: Retreat Form [收勢]
311. [Umiejętność wroga [131808] (ulepszenie 1) — opis] [StartBattle] (자신의 [DicipleLittleFinger] x 10)만큼 보호막 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131808].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [DicipleLittleFinger]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DicipleLittleFinger] = 월하청도 / Moonlit Azure Blade
   EN: [StartBattle] Gain 10 x ([DicipleLittleFinger] Count on self) Shield HP
   PL: [StartBattle] zyskuje 10 x (Licznik [DicipleLittleFinger] jednostki) HP Tarczy
312. [Umiejętność wroga [131809] (ulepszenie 1) — nazwa] 이격[二擊]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131809].levelList[level=1].name
   limit: do 40 znaków
   EN: Twinstrike [二擊]
   PL: Twinstrike [二擊]
313. [Umiejętność wroga [131809] (ulepszenie 1) — opis] [WinDuel] [DicipleLittleFinger] 1 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131809].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [DicipleLittleFinger]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [DicipleLittleFinger] = 월하청도 / Moonlit Azure Blade
   EN: [WinDuel] Gain 1 [DicipleLittleFinger]
   PL: [WinDuel] zyskuje 1 [DicipleLittleFinger]
314. [Umiejętność wroga [131809] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131809].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL: [OnSucceedAttack] zyskuje 1 Licznika [Breath]
315. [Umiejętność wroga [131809] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131809].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL: [OnSucceedAttack] zyskuje 2 [Breath]
316. [Umiejętność wroga [131810] (ulepszenie 1) — nazwa] 삼격[三擊]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131810].levelList[level=1].name
   limit: do 40 znaków
   EN: Triplestrike [三擊]
   PL: Triplestrike [三擊]
317. [Umiejętność wroga [131810] (ulepszenie 1) — opis] [WinDuel] [DicipleLittleFinger] 1 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131810].levelList[level=1].desc
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Umiejętność wroga [131810] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131810].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [Umiejętność wroga [131810] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131810].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL: [OnSucceedAttack] zyskuje 1 [Breath]
320. [Umiejętność wroga [131810] (ulepszenie 1) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131810].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +30% Damage on Critical Hit
   PL: zadaje +30% obrażeń przy trafieniu krytycznym
321. [Umiejętność wroga [130801] (ulepszenie 1) — nazwa] 걸려든 미끼
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130801].levelList[level=1].name
   limit: do 40 znaków
   EN: Snagged Lure
   PL: Snagged Lure
322. [Umiejętność wroga [130801] (ulepszenie 1) — opis] [CantDuel]\n[FairyCharm]에 걸린 수감자를 우선으로 지정\n공격 가중치가 [FairyCharm]에 걸린 수감자 수만큼 적용됨
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130801].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [FairyCharm]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [FairyCharm] = 매혹 / Charmed
   EN: [CantDuel]\nPrioritizes Sinners who are [FairyCharm]\nThis Skill's Atk Weight = Number of Sinners who are [FairyCharm]
   PL: [CantDuel]\npriorytet: Grzesznicy z [FairyCharm]\nWaga Ataku tej Umiejętności = liczba Grzeszników z [FairyCharm]
323. [Umiejętność wroga [130801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Umiejętność wroga [130801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Umiejętność wroga [130801] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 본체, 몸통 체력 15 회복
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130801].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Core, Body heals 15 HP
   PL: [OnSucceedAttack] przywraca 15 HP Korpusowi i Części Korpusu
326. [Umiejętność wroga [130802] (ulepszenie 1) — nazwa] 파고드는 뿌리
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130802].levelList[level=1].name
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Umiejętność wroga [130802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Umiejętność wroga [130802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Umiejętność wroga [130803] (ulepszenie 1) — nazwa] 확산하는 뿌리
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130803].levelList[level=1].name
   limit: do 40 znaków
   EN: Expanding Roots
   PL: Expanding Roots
330. [Umiejętność wroga [130803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]
   PL: [OnSucceedAttack] nakłada 5 [Burst]
331. [Umiejętność wroga [130803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Umiejętność wroga [130804] (ulepszenie 1) — nazwa] 침식하는 줄기
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130804].levelList[level=1].name
   limit: do 40 znaków
   EN: Infusing Stems
   PL: Infusing Stems
333. [Umiejętność wroga [130804] (ulepszenie 1) — opis] [DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130804].levelList[level=1].desc
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Umiejętność wroga [130804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]\n[OnSucceedAttack] 대상의 [Burst] 수치당 피해량 +5% (최대 100%)
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [SuperCoin], [OnSucceedAttack], [Burst]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [SuperCoin]\n[OnSucceedAttack] Deal +5% damage for every [Burst] on target (max 100%)
   PL: [SuperCoin]\n[OnSucceedAttack] zadaje +5% obrażeń za każdy [Burst] celu (maks. 100%)
335. [Umiejętność wroga [130805] (ulepszenie 1) — nazwa] 드러난 심연
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130805].levelList[level=1].name
   limit: do 40 znaków
   EN: Uncovered Abyss
   PL: Uncovered Abyss
336. [Umiejętność wroga [130805] (ulepszenie 1) — opis] 대상의 [Burst]이 5이상이면, 피해량 +100%\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130805].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [DefeatDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has 5+ [Burst], deal +100% damage\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: jeżeli cel ma 5+ [Burst], zadaje +100% obrażeń\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
337. [Umiejętność wroga [130805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Umiejętność wroga [130806] (ulepszenie 1) — nazwa] 매혹된 자아
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130806].levelList[level=1].name
   limit: do 40 znaków
   EN: Charmed Consciousness
   PL: Charmed Consciousness
339. [Umiejętność wroga [130806] (ulepszenie 1) — opis] 요정 초롱을 공격할 때 피해가 0으로 적용됨
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130806].levelList[level=1].desc
   limit: do 120 znaków
   EN: Attacking Faelantern deals 0 damage
   PL: atakowanie Faelantern zadaje 0 obrażeń
340. [Umiejętność wroga [130807] (ulepszenie 1) — nazwa] 걸려든 미끼
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130807].levelList[level=1].name
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Umiejętność wroga [130807] (ulepszenie 1) — opis] [CantDuel]\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[FairyCharm]에 걸린 수감자를 우선으로 지정\n공격 가중치가 [FairyCharm]에 걸린 수감자 수만큼 적용됨
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130807].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [FairyCharm]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [FairyCharm] = 매혹 / Charmed
   EN: [CantDuel]\nCannot be Staggered before using this Skill\nPrioritizes Sinners who are [FairyCharm]\nThis Skill's Atk Weight = Number of Sinners who are [FairyCharm]
   PL: [CantDuel]\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\npriorytet: Grzesznicy z [FairyCharm]\nWaga Ataku tej Umiejętności = liczba Grzeszników z [FairyCharm]
342. [Umiejętność wroga [130807] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여, [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130807].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst] and +3 [Burst] Count
   PL: [OnSucceedAttack] nakłada 3 [Burst] i 3 Licznika [Burst]
343. [Umiejętność wroga [130807] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130807].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 [Laceration] i 3 Licznika [Laceration]
344. [Umiejętność wroga [130807] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 본체, 몸통 체력 30 회복
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130807].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Core and Body heal 30 HP
   PL: [OnSucceedAttack] przywraca 30 HP Korpusowi i Części Korpusu
345. [Umiejętność wroga [130901] (ulepszenie 1) — nazwa] 차원 베기
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130901].levelList[level=1].name
   limit: do 40 znaków
   EN: Dimensional Slice
   PL: Dimensional Slice
346. [Umiejętność wroga [130901] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 3 증가\n[DefeatDuel] 자신의 [Charge] 횟수 2 소모
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain +3 [Charge] Count\n[DefeatDuel] Consume 2 [Charge] Count
   PL: [WhenUse] zyskuje 3 Licznika [Charge]\n[DefeatDuel] zużywa 2 Licznika [Charge]
347. [Umiejętność wroga [130901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Umiejętność wroga [130902] (ulepszenie 1) — nazwa] 연속 차원 베기
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130902].levelList[level=1].name
   limit: do 50 znaków
   EN: Consecutive Dimensional Slice
   PL: Consecutive Dimensional Slice
349. [Umiejętność wroga [130902] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 3 증가\n[DefeatDuel] 자신의 [Charge] 횟수 2 소모
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130902].levelList[level=1].desc
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Umiejętność wroga [130902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DimensionRift] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DimensionRift]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [OnSucceedAttack] Inflict 3 [DimensionRift]
   PL: [OnSucceedAttack] nakłada 3 [DimensionRift]
351. [Umiejętność wroga [130902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [DimensionRift] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Umiejętność wroga [130903] (ulepszenie 1) — nazwa] 부산물 뱉기
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130903].levelList[level=1].name
   limit: do 40 znaków
   EN: Discharge Byproducts
   PL: Discharge Byproducts
353. [Umiejętność wroga [130903] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 4 증가\n[DefeatDuel] 자신의 [Charge] 횟수 2 소모
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130903].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain +4 [Charge] Count\n[DefeatDuel] Consume 2 [Charge] Count
   PL: [WhenUse] zyskuje 4 Licznika [Charge]\n[DefeatDuel] zużywa 2 Licznika [Charge]
354. [Umiejętność wroga [130903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 330 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Umiejętność wroga [130904] (ulepszenie 1) — nazwa] 공간 절단
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130904].levelList[level=1].name
   limit: do 40 znaków
   EN: Rip Space
   PL: Rip Space
356. [Umiejętność wroga [130904] (ulepszenie 1) — opis] [Charge] 횟수가 10 이상이면, [Charge] 횟수 10을 소모하고 합 위력 +5, 피해량 +100%\n[Charge] 횟수가 10 미만이면, 본체 체력 100을 소모함. 피해량 +80%\n이 스킬의 효과로 자신의 체력이 0이 되지 않음.\n[DefeatDuel] 아래 효과 적용\n- [Paralysis] 2 얻음\n- 피해량이 80%만큼 감소함\n- 이 스킬로 대상이 흐트러지지 않음\n- 대상의 [Burst] 효과를 발동시키지 않음
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130904].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [DefeatDuel], [Paralysis], [Burst]
   znaczenie tagów: [Charge] = 충전 / Charge; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze; [Burst] = 파열 / Rupture
   EN: At 10+ [Charge] Count, consume 10 [Charge] Count to gain Clash Power +5 and deal +100% damage\nAt less than 10 [Charge] Count, consume 100 Core HP. Deal +80% damage\nThis unit's HP cannot drop to 0 due to this Skill's effect\n[DefeatDuel] Gain the following effects:\n- Gain 2 [Paralysis]\n- Deal -80% damage\n- This Skill cannot Stagger the target\n- Does not activate [Burst] on target
   PL: przy 10+ Licznika [Charge], zużywa 10 Licznika [Charge], by zyskać Moc Starcia +5 i zadać +100% obrażeń\nprzy mniej niż 10 Licznika [Charge], zużywa 100 HP Korpusu. zadaje +80% obrażeń\ndzięki efektowi tej Umiejętności HP jednostki nie spada do 0.\n[DefeatDuel] zyskuje następujące efekty:\n- zyskuje 2 [Paralysis]\n- zadaje o 80% mniej obrażeń\n- ta Umiejętność nie może Oszołomić celu\n- nie uruchamia [Burst] celu
357. [Umiejętność wroga [130904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Umiejętność wroga [130904] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130904].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Charge]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttackHead] Gain +2 [Charge] Count
   PL: [OnSucceedAttackHead] zyskuje 2 Licznika [Charge]
359. [Umiejętność wroga [130904] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [DimensionRift] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130904].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [DimensionRift]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [DimensionRift]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [DimensionRift]
360. [Umiejętność wroga [130904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Umiejętność wroga [130904] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130904].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 358 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Umiejętność wroga [130904] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [DimensionRift] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130904].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 359 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Umiejętność wroga [130905] (ulepszenie 1) — nazwa] 준비된 반격
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130905].levelList[level=1].name
   limit: do 40 znaków
   EN: Prepared Retribution
   PL: Prepared Retribution
364. [Umiejętność wroga [130905] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130905].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +1 [Charge] Count
   PL: [WhenUse] zyskuje 1 Licznika [Charge]
365. [Umiejętność wroga [130905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Umiejętność wroga [130905] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130905].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] nakłada 2 [Burst]
367. [Umiejętność wroga [130906] (ulepszenie 1) — nazwa] 부산물 토하기
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130906].levelList[level=1].name
   limit: do 40 znaków
   EN: Vomit Byproducts
   PL: Vomit Byproducts
368. [Umiejętność wroga [130906] (ulepszenie 1) — opis] [WhenUse] 메인 타겟에게 [DimensionRift]이 있다면, 피해량 +10%\n[DefeatDuel] 자신의 [Charge] 횟수 2 소모
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130906].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DimensionRift], [DefeatDuel], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DimensionRift] = 차원 균열 / Dimensional Rift; [DefeatDuel] = [합 패배] / [Clash Lose]; [Charge] = 충전 / Charge
   EN: [WhenUse] If the main target has [DimensionRift], deal +10% damage\n[DefeatDuel] Consume 2 [Charge] Count
   PL: [WhenUse] jeżeli główny cel ma [DimensionRift], zadaje +10% obrażeń\n[DefeatDuel] zużywa 2 Licznika [Charge]
369. [Umiejętność wroga [130906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Umiejętność wroga [130906] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [DimensionRift] 5 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130906].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [DimensionRift]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [DimensionRift]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 5 [DimensionRift]
371. [Umiejętność wroga [130907] (ulepszenie 1) — nazwa] 고속 공간 절단
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130907].levelList[level=1].name
   limit: do 40 znaków
   EN: High-speed Rip Space
   PL: High-speed Rip Space
372. [Umiejętność wroga [130907] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[DefeatDuel]\n- [ResultReduction] 2, [Paralysis] 1 얻음\n- 피해량이 90%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n가장 많이 가지고 있는 포탈 효과만큼 합 위력 증가\n자신이 가지고 있는 포탈 효과만큼 피해량 +10%
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130907].levelList[level=1].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel], [ResultReduction], [Paralysis]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [ResultReduction] = 위력 감소 / Power Down; [Paralysis] = 마비 / Paralyze
   EN: Can Clash with this Skill regardless of Speed; cannot be Staggered before using this Skill\n[DefeatDuel]\n- Gain 2 [ResultReduction] and 1 [Paralysis]\n- Deal -90% damage and damage dealt by this Skill cannot Stagger the target\nGain 1 Clash Power for every Dimension effect on self\nDeal +10% for every Dimension effect on self
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości; nie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n[DefeatDuel]\n- zyskuje 2 [ResultReduction] i 1 [Paralysis]\n- zadaje o 90% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\nzyskuje Moc Starcia +1 za każdy posiadany efekt Wymiaru\nzadaje +10% obrażeń za każdy posiadany efekt Wymiaru
373. [Umiejętność wroga [130907] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130907].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Umiejętność wroga [130907] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130907].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Burst]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Burst]
375. [Umiejętność wroga [130908] (ulepszenie 1) — nazwa] 기회 포착
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130908].levelList[level=1].name
   limit: do 40 znaków
   EN: Opportunity Spotted
   PL: Opportunity Spotted
376. [Umiejętność wroga [130908] (ulepszenie 1) — opis] [WhenUse] 대상에게 [DimensionRift]이 있다면, 피해량 +20%
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130908].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [DimensionRift]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [WhenUse] If target has [DimensionRift], deal +20% damage
   PL: [WhenUse] jeżeli cel ma [DimensionRift], zadaje +20% obrażeń
377. [Umiejętność wroga [130908] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DimensionRift] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130908].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Umiejętność wroga [130909] (ulepszenie 1) — nazwa] 틈새 공격
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130909].levelList[level=1].name
   limit: do 40 znaków
   EN: Rift Attack
   PL: Rift Attack
379. [Umiejętność wroga [130909] (ulepszenie 1) — opis] [WhenUse] 대상에게 [DimensionRift]이 있다면, 피해량 +10%
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130909].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [DimensionRift]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DimensionRift] = 차원 균열 / Dimensional Rift
   EN: [WhenUse] If target has [DimensionRift], deal +10% damage
   PL: [WhenUse] jeżeli cel ma [DimensionRift], zadaje +10% obrażeń
380. [Umiejętność wroga [130909] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DimensionRift] 3 부여
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=130909].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [Umiejętność wroga [131001] (ulepszenie 1) — nazwa] 차원 이동
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131001].levelList[level=1].name
   limit: do 40 znaków
   EN: Dimensional Leap
   PL: Dimensional Leap
382. [Umiejętność wroga [131001] (ulepszenie 1) — opis] 이 차원이 남아있다면, 피해량이 10% 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131001].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this 'Dimensional Rift' remains, deal +10% damage
   PL: jeżeli ten „Dimensional Rift” nadal trwa, zadaje +10% obrażeń
383. [Umiejętność wroga [131101] (ulepszenie 1) — nazwa] 차원 이동
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131101].levelList[level=1].name
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Umiejętność wroga [131101] (ulepszenie 1) — opis] 이 차원이 남아있다면, 최대 체력이 20% 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131101].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this 'Dimensional Rift' remains, max HP +20%
   PL: jeżeli ten „Dimensional Rift” nadal trwa, Maks. HP +20%
385. [Umiejętność wroga [131201] (ulepszenie 1) — nazwa] 차원 이동
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131201].levelList[level=1].name
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Umiejętność wroga [131201] (ulepszenie 1) — opis] 이 차원이 남아있다면, 속도 1 증가
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131201].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this 'Dimensional Rift' remains, gain 1 Speed
   PL: jeżeli ten „Dimensional Rift” nadal trwa, zyskuje 1 Szybkości
387. [Umiejętność wroga [131301] (ulepszenie 1) — nazwa] 차원 이동
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131301].levelList[level=1].name
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Umiejętność wroga [131301] (ulepszenie 1) — opis] 이 차원이 남아있다면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c9p1.json :: dataList[id=131301].levelList[level=1].desc
   limit: do 120 znaków
   EN: If this 'Dimensional Rift' remains, Coin Power +1
   PL: jeżeli ten „Dimensional Rift” nadal trwa, Moc Monety +1

## [a1c9p1] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c9p1
- grupa rozdziału/trybu: `a1c9p1` · plik: `Skills_Enemy-a1c9p1.json`

389. [Umiejętność wroga [9103601] (ulepszenie 1) — nazwa] 관통
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103601].levelList[level=1].name
   limit: do 40 znaków
   EN: Pierce
   PL: Pierce
390. [Umiejętność wroga [9103601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Umiejętność wroga [9103602] (ulepszenie 1) — nazwa] 살찢기
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103602].levelList[level=1].name
   limit: do 40 znaków
   EN: Flesh Rip
   PL: Flesh Rip
392. [Umiejętność wroga [9103602] (ulepszenie 1) — opis] 대상의 [Laceration]이 5 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 5+ [Laceration], Base Power +1
   PL: jeżeli cel ma 5+ [Laceration], Moc Bazowa +1
393. [Umiejętność wroga [9103602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가\n대상에게 부정적인 효과가 3개 이상이면, 추가 1 증가
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count\nIf target has 3+ types of negative effects, inflict +1 additional [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Laceration]\njeżeli cel ma 3+ typy negatywnych efektów, nakłada dodatkowe 1 Licznika [Laceration]
394. [Umiejętność wroga [9103602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttackHead] Inflict 2 [DefenseDown] next turn
   PL: [OnSucceedAttackHead] nakłada 2 [DefenseDown] w następnej turze
395. [Umiejętność wroga [9103602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가\n대상에게 부정적인 효과가 3개 이상이면, 추가 1 증가
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność wroga [9103602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Umiejętność wroga [9103603] (ulepszenie 1) — nazwa] 작품명: 심장박동 주기에 따른 뼈의 해방
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103603].levelList[level=1].name
   limit: do 80 znaków
   EN: Artwork: Liberation of Bones Contingent on Cardiac Rhythm
   PL: Artwork: Liberation of Bones Contingent on Cardiac Rhythm
398. [Umiejętność wroga [9103603] (ulepszenie 1) — opis] 자신의 잃은 본체 체력 20% 당, 기본 위력 + 1 (최대 4)\n대상의 [Laceration] 3 당, 코인 위력 +1 (최대 2)\n[WinDuel] 대상의 [Vibration] 횟수 2 증가\n[DefeatDuel] 다음 턴에 [Paralysis] 1 얻음
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103603].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WinDuel], [Vibration], [DefeatDuel], [Paralysis]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze
   EN: Base Power +1 for every 20% missing HP percentage on this unit's Core (max 4)\nCoin Power +1 for every 3 [Laceration] on target (max 2)\n[WinDuel] Inflict +2 [Vibration] Count\n[DefeatDuel] Gain 1 [Paralysis] next turn
   PL: Moc Bazowa +1 za każde 20% brakującego HP Korpusu jednostki (maks. 4)\nMoc Monety +1 za każde 3 [Laceration] celu (maks. 2)\n[WinDuel] nakłada 2 Licznika [Vibration]\n[DefeatDuel] zyskuje 1 [Paralysis] w następnej turze
399. [Umiejętność wroga [9103603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Umiejętność wroga [9103603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] nakłada 3 [Vibration]
401. [Umiejętność wroga [9103603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Umiejętność wroga [9103603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Umiejętność wroga [9103603] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnStartCoin] 현재 본체 체력의 30%만큼 체력 감소 (이 효과로 흐트러짐 상태가 되지 않음, 소수점 버림)
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103603].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]
   EN: [OnStartCoin] Lose 30% of this unit's current Core HP (does not get Staggered due to this effect; rounded down)
   PL: [OnStartCoin] traci 30% aktualnego HP Korpusu (nie przechodzi w Oszołamienie dzięki temu efektowi; zaokrąglając w dół)
404. [Umiejętność wroga [9103603] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Laceration] 5 얻음
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103603].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Gain 5 [Laceration]
   PL: [OnSucceedAttack] zyskuje 5 [Laceration]
405. [Umiejętność wroga [9103603] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103603].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Umiejętność wroga [9103603] (ulepszenie 1) — moneta 3, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationBleeding]로 [Switch_Vibration]
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103603].levelList[level=1].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationBleeding], [Switch_Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationBleeding] = 진동 - 과다출혈 / Tremor - Hemorrhage; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [Switch_Vibration] into [VibrationBleeding]
   PL: [UnBrokenCoinOnSucceedAttack] uruchamia [Switch_Vibration], przekształcając je w [VibrationBleeding]
407. [Umiejętność wroga [9103603] (ulepszenie 1) — moneta 3, efekt 6 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103603].levelList[level=1].coinlist[#2].coindescs[#5].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [UnBrokenCoinOnSucceedAttack] uruchamia [VibrationExplosion]; następnie zmniejsza Licznik [Vibration] celu o 1
408. [Umiejętność wroga [9103605] (ulepszenie 1) — nazwa] 근육 수축
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103605].levelList[level=1].name
   limit: do 40 znaków
   EN: Muscular Contraction
   PL: Muscular Contraction
409. [Umiejętność wroga [9103605] (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] 다음 턴에 [MuscleContraction] 1 얻음. 피격 시 추가로 1 얻음. (턴 당 1회)
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103605].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [MuscleContraction]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [MuscleContraction] = 근섬유의 기계적 수축과 이완 / Automated Myofiber Activity
   EN: [CanDuelGuard]\n[StartBattle] Gain 1 [MuscleContraction] next turn. When hit, gain 1 additional [MuscleContraction] (once per turn)
   PL: [CanDuelGuard]\n[StartBattle] zyskuje 1 [MuscleContraction] w następnej turze. przy otrzymaniu trafienia zyskuje dodatkowe 1 [MuscleContraction] (1 raz na turę)
410. [Umiejętność wroga [9103605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Umiejętność wroga [9103701] (ulepszenie 1) — nazwa] 꽂기
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103701].levelList[level=1].name
   limit: do 40 znaków
   EN: Jab
   PL: Jab
412. [Umiejętność wroga [9103701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Umiejętność wroga [9103702] (ulepszenie 1) — nazwa] 혈관찢기
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103702].levelList[level=1].name
   limit: do 40 znaków
   EN: Vascular Tear
   PL: Vascular Tear
414. [Umiejętność wroga [9103702] (ulepszenie 1) — opis] 대상의 [Laceration]이 5 이상이면, 기본 위력 +1\n대상에게 부정적인 효과가 3개 이상이면 피해량 +30%
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103702].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 5+ [Laceration], Base Power +1\nIf target has 3+ types of negative effects, deal +30% damage
   PL: jeżeli cel ma 5+ [Laceration], Moc Bazowa +1\njeżeli cel ma 3+ typy negatywnych efektów, zadaje +30% obrażeń
415. [Umiejętność wroga [9103702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Umiejętność wroga [9103702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Umiejętność wroga [9103703] (ulepszenie 1) — nazwa] 작품명: 심장박동 주기에 따른 뼈의 해방
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103703].levelList[level=1].name
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Umiejętność wroga [9103703] (ulepszenie 1) — opis] 자신의 잃은 본체 체력 20% 당, 기본 위력 + 1 (최대 4)\n대상의 [Laceration] 3 당, 코인 위력 +1 (최대 2)\n[WinDuel] 대상의 [Vibration] 횟수 2 증가\n[DefeatDuel] 다음 턴에 [Paralysis] 1 얻음
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103703].levelList[level=1].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Umiejętność wroga [9103703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Umiejętność wroga [9103703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Umiejętność wroga [9103703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Umiejętność wroga [9103703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Umiejętność wroga [9103703] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnStartCoin] 현재 본체 체력의 30%만큼 체력 감소 (이 효과로 흐트러짐 상태가 되지 않음, 소수점 버림)
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103703].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Umiejętność wroga [9103703] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Laceration] 5 얻음
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103703].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 404 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Umiejętność wroga [9103703] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103703].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Umiejętność wroga [9103703] (ulepszenie 1) — moneta 3, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationBleeding]로 [Switch_Vibration]
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103703].levelList[level=1].coinlist[#2].coindescs[#4].desc
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Umiejętność wroga [9103703] (ulepszenie 1) — moneta 3, efekt 6 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103703].levelList[level=1].coinlist[#2].coindescs[#5].desc
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Umiejętność wroga [9103705] (ulepszenie 1) — nazwa] 근육 수축
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103705].levelList[level=1].name
   (powtórzenie elementu 408 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Umiejętność wroga [9103705] (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] 다음 턴에 [MuscleContraction] 1 얻음. 피격 시 추가로 1 얻음. (턴 당 1회)
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103705].levelList[level=1].desc
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Umiejętność wroga [9103705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Umiejętność wroga [9103801] (ulepszenie 1) — nazwa] 묶인 근육
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103801].levelList[level=1].name
   limit: do 40 znaków
   EN: Bound Muscles
   PL: Bound Muscles
432. [Umiejętność wroga [9103801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Umiejętność wroga [9103801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Desire] 1 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Desire]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Desire] = 욕망 / Urge
   EN: [OnSucceedAttackHead] Inflict 1 [Desire] next turn
   PL: [OnSucceedAttackHead] nakłada 1 [Desire] w następnej turze
434. [Umiejętność wroga [9103802] (ulepszenie 1) — nazwa] 당겨서 찢기
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103802].levelList[level=1].name
   limit: do 40 znaków
   EN: Tear and Rip
   PL: Tear and Rip
435. [Umiejętność wroga [9103802] (ulepszenie 1) — opis] 대상의 [Laceration]이 5 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103802].levelList[level=1].desc
   (powtórzenie elementu 392 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Umiejętność wroga [9103802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가\n대상에게 부정적인 효과가 3개 이상이면, 추가 1 증가
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Umiejętność wroga [9103802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Desire] 1 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Umiejętność wroga [9103802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가\n대상에게 부정적인 효과가 3개 이상이면, 추가 1 증가
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Umiejętność wroga [9103802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Desire] 1 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Umiejętność wroga [9103803] (ulepszenie 1) — nazwa] 욕망으로 꾸며진 작품
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103803].levelList[level=1].name
   limit: do 40 znaków
   EN: Artwork Adorned by Desire
   PL: Artwork Adorned by Desire
441. [Umiejętność wroga [9103803] (ulepszenie 1) — opis] 자신의 잃은 본체 체력 20% 당, 기본 위력 + 1 (최대 4)\n대상의 [Laceration] 3 당, 코인 위력 +1 (최대 2)\n[WinDuel] 대상의 [Vibration] 횟수 2 증가\n[DefeatDuel] 다음 턴에 [Paralysis] 1 얻음
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103803].levelList[level=1].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Umiejętność wroga [9103803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Umiejętność wroga [9103803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Umiejętność wroga [9103803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Umiejętność wroga [9103803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Umiejętność wroga [9103803] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnStartCoin] 현재 본체 체력의 30%만큼 체력 감소 (이 효과로 흐트러짐 상태가 되지 않음, 소수점 버림)
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103803].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Umiejętność wroga [9103803] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Laceration] 5 얻음
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103803].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 404 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Umiejętność wroga [9103803] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [Desire] 2 부여
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103803].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Desire]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Desire] = 욕망 / Urge
   EN: [OnSucceedAttack] Inflict 2 [Desire] next turn
   PL: [OnSucceedAttack] nakłada 2 [Desire] w następnej turze
449. [Umiejętność wroga [9103803] (ulepszenie 1) — moneta 3, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationBleeding]로 [Switch_Vibration]
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103803].levelList[level=1].coinlist[#2].coindescs[#4].desc
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Umiejętność wroga [9103803] (ulepszenie 1) — moneta 3, efekt 6 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103803].levelList[level=1].coinlist[#2].coindescs[#5].desc
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Umiejętność wroga [9103805] (ulepszenie 1) — nazwa] 압박하는 리본
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103805].levelList[level=1].name
   limit: do 40 znaków
   EN: Tightening Ribbons
   PL: Tightening Ribbons
452. [Umiejętność wroga [9103805] (ulepszenie 1) — opis] [CanDuelGuard]\n피격 시 대상에게 [PinkRibbon_Ishmael] 1 부여 (스킬당 1회)\n[StartBattle] 다음 턴에 [MuscleContraction] 1 얻음. 피격 시 추가로 1 얻음. (턴 당 1회)
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103805].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [PinkRibbon_Ishmael], [StartBattle], [MuscleContraction]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [PinkRibbon_Ishmael] = 분홍 리본 / Pink Ribbons; [StartBattle] = [전투 시작시] / [Combat Start]; [MuscleContraction] = 근섬유의 기계적 수축과 이완 / Automated Myofiber Activity
   EN: [CanDuelGuard]\nWhen hit, inflict 1 [PinkRibbon_Ishmael] against the attacker (once per Skill)\n[StartBattle] Gain 1 [MuscleContraction] next turn. When hit, gain 1 additional [MuscleContraction] (once per turn)
   PL: [CanDuelGuard]\nprzy otrzymaniu trafienia nakłada 1 [PinkRibbon_Ishmael] atakującemu (1 raz na Umiejętność)\n[StartBattle] zyskuje 1 [MuscleContraction] w następnej turze. przy otrzymaniu trafienia zyskuje dodatkowe 1 [MuscleContraction] (1 raz na turę)
453. [Umiejętność wroga [9103805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9p1.json :: dataList[id=9103805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c9p1] Pasywka wroga: Passives_Abnormality-a1c9p1
- plik gry: `Passives_Abnormality-a1c9p1.json`

454. [[a1c9p1] Pasywka wroga [130601] — nazwa] 듀엘로
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130601].name
   limit: do 40 znaków
   EN: Duello
   PL: Duello
455. [[a1c9p1] Pasywka wroga [130601] — opis] 합 종료 시 합을 진행한 대상에게 [DuelEdge] 1 부여\n[DuelEdge]를 가진 대상과 합 진행 시 대상의 [DuelEdge] 수치 1당, 정신력 3 회복 (최대 15)
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130601].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [DuelEdge]
   znaczenie tagów: [DuelEdge] = 결투 고조 / The Duel Escalates
   EN: After Clashing, inflict 1 [DuelEdge] against the target this unit Clashed against\nIn a Clash against targets with [DuelEdge], heal 3 SP for every [DuelEdge] Stack on target (max 15)
   PL: po rozegraniu Starcia nakłada 1 [DuelEdge] celowi, z którym stoczyło Starcie\npodczas Starcia z celami posiadającymi [DuelEdge], przywraca 3 SP za każdy Licznik [DuelEdge] celu (maks. 15)
456. [[a1c9p1] Pasywka wroga [130602] — nazwa] 팔레르모 검술
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130602].name
   limit: do 40 znaków
   EN: Palermitan Style
   PL: Palermitan Style
457. [[a1c9p1] Pasywka wroga [130602] — opis] [DuelEdge] 수치에 따라 다음 효과를 얻음 (중복 적용)\n- 수치 1당 부여된 대상에게 가하는 피해량 +5%, 받는 피해량 -5% \n- 1 이상이면, 부여된 대상과 합 진행 시 합 위력 +1\n- 2 이상이면, 부여된 대상과 합 진행 시 기본 위력 +1\n- 3 이상이면, 부여된 대상과 합 진행 시 코인 위력 +1, 대상에게 공격 적중 시 [SeveredTendon] 3 부여\n- 4 이상이면, 부여된 대상과 합 진행 시 최종 위력 +1
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130602].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n, [DuelEdge], [SeveredTendon]
   znaczenie tagów: [DuelEdge] = 결투 고조 / The Duel Escalates; [SeveredTendon] = 힘줄 절단 / Severed Tendon
   EN: Gain the following effects based on the target's [DuelEdge] Stack\n- For every Stack, deal +5% damage against and take -5% damage from the target with [DuelEdge]\n- At 1+ Stack, in a Clash against targets with [DuelEdge], gain Clash Power +1\n- At 2+ Stack, in a Clash against targets with [DuelEdge], gain Base Power +1\n- At 3+ Stack, in a Clash against targets with [DuelEdge], gain Coin Power +1 and inflict 3 [SeveredTendon] On Hit\n- At 4+ Stack, in a Clash against targets with [DuelEdge], gain Final Power +1
   PL: zyskuje następujące efekty w zależności od Licznika [DuelEdge] celu\n- za każdy Licznik zadaje +5% obrażeń i otrzymuje o 5% mniej obrażeń od celu z [DuelEdge]\n- przy 1+ Liczniku, podczas Starcia z celami posiadającymi [DuelEdge], zyskuje Moc Starcia +1\n- przy 2+ Licznikach, podczas Starcia z celami posiadającymi [DuelEdge], zyskuje Moc Bazowa +1\n- przy 3+ Licznikach, podczas Starcia z celami posiadającymi [DuelEdge], zyskuje Moc Monety +1 i nakłada 3 [SeveredTendon] przy trafieniu\n- przy 4+ Licznikach, podczas Starcia z celami posiadającymi [DuelEdge], zyskuje Moc Końcowa +1
458. [[a1c9p1] Pasywka wroga [130603] — nazwa] 팔레르모식 레이피어 / 절참도
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130603].name
   limit: do 60 znaków
   EN: Palermitan Rapier / The Cleaving Blade
   PL: Palermitan Rapier / The Cleaving Blade
459. [[a1c9p1] Pasywka wroga [130603] — opis] 자신의 스킬 효과로 [VibrationExplosion]이 발동되었다면, 다음 턴 [AttackUp] 2 얻음 (턴 당 3회)
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130603].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion], [AttackUp]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: If this unit's Skill effects triggered [VibrationExplosion], gain 2 [AttackUp] next turn (3 times per turn)
   PL: jeżeli efekty Umiejętności tej jednostki uruchomiły [VibrationExplosion], zyskuje 2 [AttackUp] w następnej turze (3 razy na turę)
460. [[a1c9p1] Pasywka wroga [130604] — nazwa] 사냥 표식
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130604].name
   limit: do 40 znaków
   EN: Hunter's Mark
   PL: Hunter's Mark
461. [[a1c9p1] Pasywka wroga [130604] — opis] 3턴마다 료슈를 제외한 나머지 적들을 우선으로 무작위 1명을 지정하여, 속도를 1로 만들고 모든 스킬의 타겟으로 지정한다\n(흐트러짐으로 발동되지 못한 경우, 다음 턴에 발동한다)
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130604].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Every 3 turns, select a random enemy (except Ryōshū), reduce their Speed to 1, and target it with all of this unit's Skills\n(If this effect could not be activated due to Stagger, activate it next turn)
   PL: co 3 tury wskazuje losowego wroga (poza Ryōshū) jako priorytet, ustala jego Szybkość na 1 i wskazuje go celom wszystkich Umiejętności\n(jeżeli efekt nie mógł się uruchomić z powodu Oszołamienia, uruchamia się w następnej turze)
462. [[a1c9p1] Pasywka wroga [130605] — nazwa] 하나만을 위해 만들어진 교본
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130605].name
   limit: do 50 znaków
   EN: A Textbook with a Singular Purpose
   PL: A Textbook with a Singular Purpose
463. [[a1c9p1] Pasywka wroga [130605] — opis] 스테이지 시작 시 [TeachersCommand] 얻음\n료슈와 합 진행 시 합 위력 -3, 기본 공격 스킬이 [SuperCoin]으로 변경되며,\n합 패배시 피해량이 80% 감소하고, 적중시 효과가 발동하지 않음
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130605].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [TeachersCommand], [SuperCoin]
   znaczenie tagów: [TeachersCommand] = 엄지 아비의 명령 / The Thumb Nursefather's Command; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Encounter Start: gain [TeachersCommand]\nIn a Clash against Ryōshū, Clash Power -3 and convert the Coins on this unit's Base Attack Skills into [SuperCoin]s.\nAlso, on Clash Lose, deal -80% damage and any "On Hit" effects do not activate
   PL: Początek walki: zyskuje [TeachersCommand]\npodczas Starcia z Ryōshū Moc Starcia -3, a Monety bazowych Umiejętności ataku tej jednostki zmieniają się w [SuperCoin]y.\npoza tym po przegranej w Starciu zadaje o 80% mniej obrażeń, a efekty „przy trafieniu” nie uruchamiają się
464. [[a1c9p1] Pasywka wroga [130701] — nazwa] 무언가 찾는 팔 - 억지력 부분해제
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130701].name
   limit: do 60 znaków
   EN: Searching Arm - Partial Deterrence Release
   PL: Searching Arm - Partial Deterrence Release
465. [[a1c9p1] Pasywka wroga [130701] — opis] 다른 팔 부위가 파괴되었으면 남은 팔 부위의 모든 스킬이 [SuperCoin]이 되고, 공격 가중치 +1\n- 이 효과가 적용된 스킬 사용 시, [RapidGrowthApple] 1 얻음
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130701].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [SuperCoin], [RapidGrowthApple]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [RapidGrowthApple] = 급한 성장 / Rapid Growth
   EN: If an Arm is Part Broken, convert the Coins on the remaining Arm's Skills to [SuperCoin]s, and they gain +1 Atk Weight\n- When using a Skill affected by this effect, gain 1 [RapidGrowthApple]
   PL: jeżeli inna Część Ręki została zniszczona, Monety Umiejętności pozostałej Ręki zmieniają się w [SuperCoin]y, a te zyskują Wagę Ataku +1\n- przy użyciu Umiejętności objętej tym efektem zyskuje 1 [RapidGrowthApple]
466. [[a1c9p1] Pasywka wroga [130702] — nazwa] 흑단 여왕 - 억지력 부분해제
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130702].name
   limit: do 60 znaków
   EN: Ebony Queen - Partial Deterrence Release
   PL: Ebony Queen - Partial Deterrence Release
467. [[a1c9p1] Pasywka wroga [130702] — opis] 뿌리 부위가 있다면, 열매 부위 피격 후 [HowDareYouApple]를 1 획득함\n\n자신의 [HowDareYouApple]가 4라면 강력한 부정적인 효과 스킬을 사용함\n\n뿌리 부위가 없다면 [HowDareYouApple]를 획득하지 않고 소모하지 않음\n이후 열매 부위가 파괴되면 [HowDareYouApple]를 제거함
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130702].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [HowDareYouApple]
   znaczenie tagów: [HowDareYouApple] = 감히…! / The Audacity...!
   EN: If this unit has Roots, gain 1 [HowDareYouApple] after its Fruit Part is hit\n\nAt 4 [HowDareYouApple], use a powerful Skill that inflicts powerful negative effects\n\nIf this unit does not have Roots, neither gain nor lose [HowDareYouApple]\nWhen the Fruit Part gets broken, lose [HowDareYouApple]
   PL: jeżeli ta jednostka ma Korzenie, zyskuje 1 [HowDareYouApple] po otrzymaniu trafienia na Części Owocu\n\nprzy 4 [HowDareYouApple] używa potężnej Umiejętności nakładającej silne negatywne efekty\n\njeżeli ta jednostka nie ma Korzeni, nie zyskuje i nie zużywa [HowDareYouApple]\ngdy Część Owocu zostaje zniszczona, traci [HowDareYouApple]
468. [[a1c9p1] Pasywka wroga [130703] — nazwa] 휘감는 뿌리
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130703].name
   limit: do 40 znaków
   EN: Entangling Roots
   PL: Entangling Roots
469. [[a1c9p1] Pasywka wroga [130703] — opis] 뿌리가 파괴되기 전까지 턴 시작 시 모든 적에게 [Binding] 2 부여함
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130703].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Turn Start: inflict 2 [Binding] on all enemies\nThis lasts until the Roots are broken
   PL: na Początku tury nakłada 2 [Binding] wszystkim wrogom\ndotyczy to do czasu zniszczenia Korzeni
470. [[a1c9p1] Pasywka wroga [130704] — nazwa] 단 하나의 뿌리
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130704].name
   limit: do 40 znaków
   EN: One Sole Root
   PL: One Sole Root
471. [[a1c9p1] Pasywka wroga [130704] — opis] 파괴되지 않은 팔의 수만큼 뿌리가 [Enhancement] 3 얻음\n뿌리 부위가 파괴된 상태라면 얻지 않음
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130704].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: The Roots Part gains 3 [Enhancement] for every unbroken Arm Part\nDoes not gain this effect if the Roots are broken
   PL: Część Korzeni zyskuje 3 [Enhancement] za każdą niezniszczoną Część Ręki\nnie zyskuje tego efektu, jeżeli Korzenie są zniszczone
472. [[a1c9p1] Pasywka wroga [131901] — nazwa] 보호와 억제를 위한 갑주
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131901].name
   limit: do 50 znaków
   EN: Armor of Protection & Repression
   PL: Armor of Protection & Repression
473. [[a1c9p1] Pasywka wroga [131901] — opis] 턴 시작 시, 자신이 흐트러짐 상태가 아니면 [Protection] 2, [DefenseUp] 10 얻고 보호막을 현재 체력의 10%만큼 얻음\n\n이번 전투에서 ‘억압당한 육체’ 사용 횟수 1당, 위 효과로 얻는 [Protection] 1, [DefenseUp] 5, 보호막 수치 5% 감소
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131901].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Protection], [DefenseUp]
   znaczenie tagów: [Protection] = 보호 / Protection; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: if this unit isn't Staggered, gain 2 [Protection], 10 [DefenseUp], and Shield HP equal to 10% of this unit's current HP\n\nEvery time this unit uses "Repressed Flesh" Skill in this Encounter, gain 1 fewer [Protection], 5 fewer [DefenseUp], and reduce the percentage mentioned above by 5%
   PL: na Początku tury, jeżeli ta jednostka nie jest w Oszołamieniu, zyskuje 2 [Protection], 10 [DefenseUp] i HP Tarczy równe 10% aktualnego HP jednostki\n\nza każde użycie Umiejętności „Repressed Flesh” w tej walce ten efekt daje o 1 mniej [Protection], o 5 mniej [DefenseUp] i zmniejsza wspomniany procent o 5%
474. [[a1c9p1] Pasywka wroga [131902] — nazwa] 아이언메이든- 가시
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131902].name
   limit: do 40 znaków
   EN: Iron Maiden - Spikes
   PL: Iron Maiden - Spikes
475. [[a1c9p1] Pasywka wroga [131902] — opis] 자신이 흐트러짐 상태가 아닐 때, 공격자의 마지막 코인으로 피격 시 효과 발동\n- 공격자에게 해당 코인으로 받은 피해량의 20%만큼 관통 피해를 입히고 출혈 2 부여 (스킬당 최대 피해 100)\n- 이 효과의 피해로 대상이 흐트러지지 않음
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131902].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If this unit isn't Staggered, when hit by the last Coin of an attacker, activate the following:\n- Deal Pierce damage by 20% of the said Coin's damage and inflict 2 [Laceration] (max damage per Skill: 100)\n- Damage from this effect cannot Stagger the target
   PL: jeżeli ta jednostka nie jest w Oszołamieniu, przy otrzymaniu trafienia ostatnią Monetą atakującego uruchamia następujący efekt:\n- zadaje atakującemu obrażenia Przebiciem równe 20% obrażeń otrzymanych tą Monetą i nakłada 2 [Laceration] (maks. obrażeń na Umiejętność: 100)\nobrażenia z tego efektu nie mogą Oszołomić celu
476. [[a1c9p1] Pasywka wroga [131903] — nazwa] 아이언메이든- 재세동
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131903].name
   limit: do 40 znaków
   EN: Iron Maiden - Defibrillation
   PL: Iron Maiden - Defibrillation
477. [[a1c9p1] Pasywka wroga [131903] — opis] 등장 시 정신력 30 회복\n\n자신의 체력이 60% 남았을 때, 흐트러짐 상태를 해제하고 이번 턴을 종료함 (전투당 1회)
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131903].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upon entry, heal 30 SP\n\nAt 60% HP, recover from Stagger and end the turn (once per Encounter)
   PL: przy pojawieniu się przywraca 30 SP\n\nprzy 60% HP dochodzi do siebie z Oszołamienia i kończy tę turę (1 raz na walkę)
478. [[a1c9p1] Pasywka wroga [131904] — nazwa] 이미 재료로 사용된 육체
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131904].name
   limit: do 40 znaków
   EN: Corpus Spent as Material
   PL: Corpus Spent as Material
479. [[a1c9p1] Pasywka wroga [131904] — opis] [Combustion], [Vibration], [Burst], [Sinking]으로 받는 체력, 정신력, 흐트러짐 손상 피해량 -30%\n[Laceration]로 받는 피해량 -50%
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131904].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Vibration], [Burst], [Sinking], [Laceration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [Laceration] = 출혈 / Bleed
   EN: Take -30% HP, SP damage from [Combustion], [Burst], [Sinking]; -30% to Stagger Threshold raised by [Vibration]\nTake -50% damage from [Laceration]
   PL: otrzymuje o 30% mniej obrażeń HP i SP od [Combustion], [Burst] i [Sinking]; otrzymuje o 30% mniej wzrostu Próg Oszołomienia od [Vibration]\notrzymuje o 50% mniej obrażeń od [Laceration]
480. [[a1c9p1] Pasywka wroga [131905] — nazwa] 소중한 작품 파시아
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131905].name
   limit: do 40 znaków
   EN: Fascia, My Precious Artwork
   PL: Fascia, My Precious Artwork
481. [[a1c9p1] Pasywka wroga [131905] — opis] 턴 종료 시 [HumanFleshTheRings]가 2면, 다음 턴에 [HumanFleshTheRings] 소멸 후 [BoneBladeTheRings] 얻음\n\n턴 시작 시 [BoneBladeTheRings]가 있으면, 이번 턴에 강력한 공격 사용\n\n강력한 공격 사용 전에 공격 스킬로 피격 시, [UnsteadyTheRings] 1 얻음
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131905].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [HumanFleshTheRings], [BoneBladeTheRings], [UnsteadyTheRings]
   znaczenie tagów: [HumanFleshTheRings] = 생체 재료 / Corpus Ingredient; [BoneBladeTheRings] = 작품명: 파시아 / Artwork: Fascia; [UnsteadyTheRings] = 심하게 울리는 갑주 / Impact-rattled Armor
   EN: Turn End: at 2 [HumanFleshTheRings], [HumanFleshTheRings] expires next turn; then, gain [BoneBladeTheRings]\n\nTurn Start: if this unit has [BoneBladeTheRings], use a powerful attack this turn\n\nIf this unit is hit by an Attack Skill before using the powerful attack, gain 1 [UnsteadyTheRings]
   PL: na koniec tury przy 2 [HumanFleshTheRings], w następnej turze [HumanFleshTheRings] wygasają; następnie zyskuje [BoneBladeTheRings]\n\nna Początku tury, jeżeli ta jednostka ma [BoneBladeTheRings], używa w tej turze potężnego ataku\n\njeżeli przed użyciem potężnego ataku otrzyma trafienie od Umiejętności ataku, zyskuje 1 [UnsteadyTheRings]
482. [[a1c9p1] Pasywka wroga [131801] — nazwa] 별의 이름을 받기 위한 수행
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131801].name
   limit: do 60 znaków
   EN: Training to Inherit the Name of a Star
   PL: Training to Inherit the Name of a Star
483. [[a1c9p1] Pasywka wroga [131801] — opis] 공격 스킬 종료시, 각 대상에게 (크리티컬로 적중한 참격 코인 개수 x 10)만큼 참격 피해 (해당 피해로는 흐트러지지 않음)
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131801].desc
   limit: do 180 znaków
   EN: Attack Skill End: Deal (# of Slash Coins that hit Critically x 10) Slash damage against each target (cannot be Staggered due to this damage)
   PL: koniec Umiejętności ataku: zadaje każdemu celowi obrażenia Cięcia równe (liczba Monet Cięcia trafiających krytycznie x 10) (te obrażenia nie powodują Oszołamienia)
484. [[a1c9p1] Pasywka wroga [131802] — nazwa] 정신일도
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131802].name
   limit: do 40 znaków
   EN: Singular Focus of the Mind
   PL: Singular Focus of the Mind
485. [[a1c9p1] Pasywka wroga [131802] — opis] [Breath] 위력이 최대 25로 제한됨\n25를 초과하여 얻는 [Breath] 위력은 [DicipleLittleFinger]로 전환됨
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131802].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [DicipleLittleFinger]
   znaczenie tagów: [Breath] = 호흡 / Poise; [DicipleLittleFinger] = 월하청도 / Moonlit Azure Blade
   EN: This unit's [Breath] Potency is capped at 25\nAny excess [Breath] Potency gained past 25 will be converted to [DicipleLittleFinger]
   PL: Siła [Breath] tej jednostki jest ograniczona do 25\nnadmierna Siła [Breath] uzyskana ponad 25 jest przekształcana w [DicipleLittleFinger]
486. [[a1c9p1] Pasywka wroga [131803] — nazwa] 정검[整劍]
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131803].name
   limit: do 40 znaków
   EN: The Orthodox Blade [整劍]
   PL: The Orthodox Blade [整劍]
487. [[a1c9p1] Pasywka wroga [131803] — opis] 스테이지 시작시 [DicipleLittleFinger] 50을 얻음
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131803].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DicipleLittleFinger]
   znaczenie tagów: [DicipleLittleFinger] = 월하청도 / Moonlit Azure Blade
   EN: Encounter Start: gain 50 [DicipleLittleFinger]
   PL: Początek walki: zyskuje 50 [DicipleLittleFinger]
488. [[a1c9p1] Pasywka wroga [131804] — nazwa] 정념[靜念]
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131804].name
   limit: do 40 znaków
   EN: Tranquility [靜念]
   PL: Tranquility [靜念]
489. [[a1c9p1] Pasywka wroga [131804] — opis] 자신에게 [DicipleLittleFinger]가 있으면 아래 효과 적용\n- 정신력이 0 미만으로 감소하지 않음. 0 미만이었으면 0이 됨\n- 받는 정신력 피해가 우울 피해로 전환됨 (기본 정신력 증감조건 제외)
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131804].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [DicipleLittleFinger]
   znaczenie tagów: [DicipleLittleFinger] = 월하청도 / Moonlit Azure Blade
   EN: If this unit has [DicipleLittleFinger], gain the following effects:\n- SP does not drop below 0; if it was below 0, recover to 0\n- Convert any SP damage taken into Gloom damage (save for SP changes due to "Base factors increasing/decreasing Sanity")
   PL: jeżeli ta jednostka ma [DicipleLittleFinger], obowiązują następujące efekty:\n- SP nie spada poniżej 0; jeżeli było niższe niż 0, wraca do 0\n- otrzymywane obrażenia SP są przekształcane w obrażenia Zauły (poza zmianami SP wynikającymi z „bazowych warunków zmiany Poczucia”)
490. [[a1c9p1] Pasywka wroga [131805] — nazwa] 은혜
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131805].name
   limit: do 40 znaków
   EN: Grace
   PL: Grace
491. [[a1c9p1] Pasywka wroga [131805] — opis] 료슈 외 대상과 합을 진행할 때, 합 위력 -2\n료슈 외 대상에게 받는 피해량 -20%
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131805].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In a Clash against targets that aren't Ryōshū, Clash Power -2\nTake -20% damage from targets other than Ryōshū
   PL: podczas Starcia z celami innymi niż Ryōshū Moc Starcia -2\notrzymuje o 20% mniej obrażeń od celów innych niż Ryōshū
492. [[a1c9p1] Pasywka wroga [130801] — nazwa] 매혹
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130801].name
   limit: do 40 znaków
   EN: Charmed
   PL: Charmed
493. [[a1c9p1] Pasywka wroga [130801] — opis] 턴 시작 시 전투 참여 인원 수에 비례하여, 속도가 낮은 수감자들에게 [FairyCharm] 부여\n요정 부위가 재생될 때마다 [FairyCharm] 인원이 증가
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130801].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [FairyCharm]
   znaczenie tagów: [FairyCharm] = 매혹 / Charmed
   EN: Turn Start: based on the number of units in the Encounter, inflict [FairyCharm] on Sinners with the slowest Speed\nNumber of [FairyCharm] units increases every time the Fairy Part is restored
   PL: na Początku tury, proporcjonalnie do liczby uczestników walki, nakłada [FairyCharm] Grzesznikom z najniższą Szybkością\nliczba jednostek z [FairyCharm] rośnie przy każdym odtworzeniu Części Wróżki
494. [[a1c9p1] Pasywka wroga [130802] — nazwa] 드러난 심연
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130802].name
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [[a1c9p1] Pasywka wroga [130802] — opis] 요정 부위를 파괴하면 몸통이 드러남\n몸통을 다시 숨길 때, 가지고 있는 버프 및 디버프 효과 전부 제거
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130802].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reveal body when the Fairy Part is broken\nAll Buffs and Debuffs expire when the Body hides again
   PL: odsłania Korpus, gdy Część Wróżki zostaje zniszczona\nprzy ponownym ukryciu Korpusu usuwa wszystkie posiadane bonusy i debuffy
496. [[a1c9p1] Pasywka wroga [130803] — nazwa] 앞선 미끼
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130803].name
   limit: do 40 znaków
   EN: Leading Lure
   PL: Leading Lure
497. [[a1c9p1] Pasywka wroga [130803] — opis] 요정 부위를 공격당하여도 본체 체력이 소모되지 않음\n[FairyCharm]된 인원 수에 따라 특정 스킬의 공격 가중치가 증가
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130803].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [FairyCharm]
   znaczenie tagów: [FairyCharm] = 매혹 / Charmed
   EN: Cannot damage Core HP by damaging the Fairy\nA certain Skill gains Atk Weight based on the number of [FairyCharm] units
   PL: atakowanie Części Wróżki nie zużywa HP Korpusu\nokreślona Umiejętność zyskuje Wagę Ataku zależnie od liczby jednostek z [FairyCharm]
498. [[a1c9p1] Pasywka wroga [130804] — nazwa] 파괴된 밑동
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130804].name
   limit: do 40 znaków
   EN: Broken Stump
   PL: Broken Stump
499. [[a1c9p1] Pasywka wroga [130804] — opis] 몸통 부위 파괴 시,\n- 요정이 재생될 때 체력이 60%인 상태로 적용됨\n- 스킬로 본체 체력을 회복할 때, 회복량 +20
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130804].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the Body is broken:\n- Fairy will have 60% of its max HP upon restoration\n- Core heals +20 more HP with Skill effects
   PL: gdy Korpus zostaje zniszczony:\n- Wróżka odtwarza się z HP równym 60% swojego Maks. HP\n- przywracając HP Korpusu efektami Umiejętności, przywraca o 20 więcej HP
500. [[a1c9p1] Pasywka wroga [130805] — nazwa] 진화하는 미끼
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130805].name
   limit: do 40 znaków
   EN: Evolving Lure
   PL: Evolving Lure
501. [[a1c9p1] Pasywka wroga [130805] — opis] 요정 부위가 재생될 때마다 최대 체력 30% 증가
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130805].desc
   limit: do 120 znaków
   EN: Fairy gains 30% increased max HP with each restoration
   PL: przy każdym odtworzeniu Części Wróżki jej Maks. HP rośnie o 30%
502. [[a1c9p1] Pasywka wroga [130806] — nazwa] 요정 가루
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130806].name
   limit: do 40 znaków
   EN: Fairy Dust
   PL: Fairy Dust
503. [[a1c9p1] Pasywka wroga [130806] — opis] 요정이 죽었을 때, 모든 인격이 다음 턴에 [Breath] 5, [Breath] 횟수 2 얻음
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130806].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: When the Fairy is killed, all Identities gain 5 [Breath] and +2 [Breath] Count next turn
   PL: gdy Wróżka ginie, wszystkie Osobowości zyskują 5 [Breath] i 2 Licznika [Breath] w następnej turze
504. [[a1c9p1] Pasywka wroga [130807] — nazwa] 공격성 강화 - 억지력 부분해제
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130807].name
   limit: do 70 znaków
   EN: Increased Aggression - Partial Deterrence Release
   PL: Increased Aggression - Partial Deterrence Release
505. [[a1c9p1] Pasywka wroga [130807] — opis] 요정이 2번 드러난 이후부터 한층 강화된 스킬을 사용
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130807].desc
   limit: do 120 znaków
   EN: Use more powerful Skills after the Fairy is restored for the second time
   PL: po drugim odtworzeniu Wróżki używa jeszcze potężniejszych Umiejętności
506. [[a1c9p1] Pasywka wroga [130901] — nazwa] 차원 도주
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130901].name
   limit: do 40 znaków
   EN: Dimensional Escape
   PL: Dimensional Escape
507. [[a1c9p1] Pasywka wroga [130901] — opis] 두 번째 턴부터 일정 턴마다 4개의 무작위 차원을 소환하여 몸을 숨김.\n- 모든 부위가 흐트러짐 상태이면, 다음 턴에 발동\n- 차원으로 몸을 숨긴 상태에서는 흐트러짐 상태가 되지 않음.
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130901].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Starting from turn 2, this unit summons 4 random Dimensions and hides\n- When all Parts are Staggered, this effect activates next turn\n- Cannot be Staggered while hidden inside a 'Dimensional Rift'.
   PL: od 2. tury, co kilka tur przywołuje 4 losowe Wymiary i się ukrywa.\n- jeżeli wszystkie Części są w Oszołamieniu, efekt uruchamia się w następnej turze\n- ukryta wewnątrz „Dimensional Rift” nie może przejść w Oszołamienie.
508. [[a1c9p1] Pasywka wroga [130902] — nazwa] 갇혀버린 차원 탈출
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130902].name
   limit: do 40 znaków
   EN: Trapped Dimensional Escape
   PL: Trapped Dimensional Escape
509. [[a1c9p1] Pasywka wroga [130902] — opis] 차원이 모두 파괴되면, 다음 턴에 차원에서 빠져나와 자신을 드러냄\n이후 [Charge] 횟수 5를 잃고, 모든 부위가 흐트러짐 손상 30을 입음
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130902].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: When all 'Dimensional Rifts' are broken, this unit voluntarily emerges from a 'Dimensional Rift' next turn\nAfterward, this unit loses 5 [Charge] Count and all of its Parts' Stagger Thresholds are raised by 30
   PL: gdy wszystkie Wymiary zostaną zniszczone, ta jednostka dobrowolnie wydostaje się z „Dimensional Rift” w następnej turze i się ujawnia\nnastępnie traci 5 Licznika [Charge], a wszystkie jej Części otrzymują 30 obrażeń Próg Oszołomienia
510. [[a1c9p1] Pasywka wroga [130903] — nazwa] 차원 굴절 칼날 수복
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130903].name
   limit: do 60 znaków
   EN: Regenerate Dimensional Refraction Blade
   PL: Regenerate Dimensional Refraction Blade
511. [[a1c9p1] Pasywka wroga [130903] — opis] 칼날 부위가 파괴되면, [Charge] 횟수 5를 잃음\n다음 턴 종료 시 [Charge] 횟수 2를 소모하여 파괴된 칼날 부위를 회복함.\n\n칼날 부위가 파괴된 상태면, 매 턴 시작 시 [AttackDown] 2를 얻음.
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130903].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [AttackDown]
   znaczenie tagów: [Charge] = 충전 / Charge; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: When the Blade Part is broken, lose 5 [Charge] Count\nAt the next Turn End, consume 2 [Charge] Count to restore the broken Blade.\n\nWhile the Blade Part is broken, gain 2 [AttackDown] at every Turn Start.
   PL: gdy Część Ostrza zostaje zniszczona, traci 5 Licznika [Charge]\nna koniec następnej tury zużywa 2 Licznika [Charge], by odtworzyć zniszczoną Część Ostrza.\n\ndopóki Część Ostrza jest zniszczona, na każdym Początku tury zyskuje 2 [AttackDown].
512. [[a1c9p1] Pasywka wroga [130904] — nazwa] 차원 강제 개방 시도 - 억지력 부분해제
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130904].name
   limit: do 90 znaków
   EN: Forced Dimensional Breach Attempt - Partial Deterrence Release
   PL: Forced Dimensional Breach Attempt - Partial Deterrence Release
513. [[a1c9p1] Pasywka wroga [130904] — opis] 본체 체력이 60% 이하가 되면, 턴이 종료되고 패턴이 변경됨\n- '차원 도주' 패시브 비활성화\n- '갇혀버린 차원 탈출' 패시브 비활성화\n- 양팔이 파괴되지 않은 상태면, 일정 턴마다 강력한 스킬을 사용
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=130904].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 60% or less Core HP, end turn and gain a new pattern\n- Deactivate "Dimensional Escape" Passive\n- Deactivate "Trapped Dimensional Escape" Passive\n- If neither of its Arms are broken, use a powerful Skill every few turns
   PL: gdy HP Korpusu spadnie do 60% lub mniej, tur się kończy, a jednostka przybiera nowy wzorzec\n- wyłącza Pasyw „Dimensional Escape”\n- wyłącza Pasyw „Trapped Dimensional Escape”\n- jeżeli żadna z Rąk nie została zniszczona, co kilka tur używa potężnej Umiejętności
514. [[a1c9p1] Pasywka wroga [131001] — nazwa] 피가 흐르는 차원
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131001].name
   limit: do 40 znaków
   EN: Hemorrhaging Dimension
   PL: Hemorrhaging Dimension
515. [[a1c9p1] Pasywka wroga [131001] — opis] 피가 흐르는 차원을 통과했다면, 피해량 +10%
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Deal +10% damage after passing through the Hemorrhaging Dimension[TabExplain]
   PL: jeżeli przeszła przez Hemorrhaging Dimension[TabExplain], zadaje +10% obrażeń
516. [[a1c9p1] Pasywka wroga [131101] — nazwa] 독이 들끓는 차원
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131101].name
   limit: do 40 znaków
   EN: Poisonous Dimension
   PL: Poisonous Dimension
517. [[a1c9p1] Pasywka wroga [131101] — opis] 독이 들끓는 차원을 통과했다면, 기본 본체 최대 체력 +20%
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Core gains +20% max HP after passing through the Poisonous Dimension[TabExplain]
   PL: jeżeli przeszła przez Poisonous Dimension[TabExplain], Korpus zyskuje +20% Maks. HP
518. [[a1c9p1] Pasywka wroga [131201] — nazwa] 끊임없이 진동하는 차원
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131201].name
   limit: do 40 znaków
   EN: Tremoring Dimension
   PL: Tremoring Dimension
519. [[a1c9p1] Pasywka wroga [131201] — opis] 끊임없이 진동하는 차원을 통과했다면, 속도 1 증가
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Gain 1 Speed after passing through the Tremoring Dimension[TabExplain]
   PL: jeżeli przeszła przez Tremoring Dimension[TabExplain], zyskuje 1 Szybkości
520. [[a1c9p1] Pasywka wroga [131301] — nazwa] 전류를 뿜어내는 차원
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131301].name
   limit: do 40 znaków
   EN: Electrifying Dimension
   PL: Electrifying Dimension
521. [[a1c9p1] Pasywka wroga [131301] — opis] 전류를 뿜어내는 차원을 통과했다면, 코인 위력 +1
   źródło: Passives_Abnormality-a1c9p1.json :: dataList[id=131301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Gain +1 Coin Power after passing through the Electrifying Dimension[TabExplain]
   PL: jeżeli przeszła przez Electrifying Dimension[TabExplain], zyskuje Moc Monety +1

## [a1c9p1] Pasywka wroga: Passives_Enemy-a1c9p1
- plik gry: `Passives_Enemy-a1c9p1.json`

522. [[a1c9p1] Pasywka wroga [9103601] — nazwa] 약지 아비의 작품
   źródło: Passives_Enemy-a1c9p1.json :: dataList[id=9103601].name
   limit: do 50 znaków
   EN: The Ring Nursefather's Artwork
   PL: The Ring Nursefather's Artwork
523. [[a1c9p1] Pasywka wroga [9103601] — opis] 메인 타겟에게 부정적인 효과가 3개 이상이면, 최종 위력 +1
   źródło: Passives_Enemy-a1c9p1.json :: dataList[id=9103601].desc
   limit: do 120 znaków
   EN: If the main target has 3+ types of negative effects, Final Power +1
   PL: jeżeli główny cel ma 3+ typy negatywnych efektów, Moc Końcowa +1
524. [[a1c9p1] Pasywka wroga [9103801] — nazwa] 뼈대에 묶인 매듭
   źródło: Passives_Enemy-a1c9p1.json :: dataList[id=9103801].name
   limit: do 40 znaków
   EN: Bonebound Knot
   PL: Bonebound Knot
525. [[a1c9p1] Pasywka wroga [9103801] — opis] 흐트러졌을 경우 다음 턴에 흐트러짐을 해제하고 [Binding] 2 얻음\n이후 매 턴 시작 시 [Vulnerable] 2 , [Enhancement] 1 얻음
   źródło: Passives_Enemy-a1c9p1.json :: dataList[id=9103801].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Binding], [Vulnerable], [Enhancement]
   znaczenie tagów: [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: When Staggered, recover from Stagger next turn and gain 2 [Binding]\nEvery subsequent Turn Start: gain 2 [Vulnerable] and 1 [Enhancement]
   PL: przy Oszołamieniu dochodzi do siebie z Oszołamienia w następnej turze i zyskuje 2 [Binding]\nnastępnie na każdym Początku tury zyskuje 2 [Vulnerable] i 1 [Enhancement]
526. [[a1c9p1] Pasywka wroga [9103802] — nazwa] 분홍 리본
   źródło: Passives_Enemy-a1c9p1.json :: dataList[id=9103802].name
   limit: do 40 znaków
   EN: Pink Ribbons
   PL: Pink Ribbons
527. [[a1c9p1] Pasywka wroga [9103802] — opis] 합 승리시 [PinkRibbon_Ishmael] 1 부여
   źródło: Passives_Enemy-a1c9p1.json :: dataList[id=9103802].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PinkRibbon_Ishmael]
   znaczenie tagów: [PinkRibbon_Ishmael] = 분홍 리본 / Pink Ribbons
   EN: Clash Win: inflict 1 [PinkRibbon_Ishmael]
   PL: po wygranej w Starciu: nakłada 1 [PinkRibbon_Ishmael]

## [a1c9p2] Wróg / część: Enemies-a1c9p2
- plik gry: `Enemies-a1c9p2.json`

528. [[a1c9p2] Wróg / część [1325] — nazwa] 검지 제자 - 소라
   źródło: Enemies-a1c9p2.json :: dataList[id=1325].name
   limit: do 40 znaków
   EN: The Index Apprentice - Sora
   PL: The Index Apprentice - Sora
529. [[a1c9p2] Wróg / część [132501] — nazwa] 몸통
   źródło: Enemies-a1c9p2.json :: dataList[id=132501].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [[a1c9p2] Wróg / część [132501] — opis] 부위
   źródło: Enemies-a1c9p2.json :: dataList[id=132501].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [[a1c9p2] Wróg / część [1322] — nazwa] 소지 아비 - 시오미 요루
   źródło: Enemies-a1c9p2.json :: dataList[id=1322].name
   limit: do 50 znaków
   EN: The Pinky Nursefather - Shiomi Yoru
   PL: The Pinky Nursefather - Shiomi Yoru
532. [[a1c9p2] Wróg / część [132201] — nazwa] 몸통
   źródło: Enemies-a1c9p2.json :: dataList[id=132201].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [[a1c9p2] Wróg / część [132201] — opis] 부위
   źródło: Enemies-a1c9p2.json :: dataList[id=132201].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c9p2] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c9p2
- grupa rozdziału/trybu: `a1c9p2` · plik: `Skills_Abnormality-a1c9p2.json`

534. [Umiejętność wroga [132001] (ulepszenie 1) — nazwa] 화염 강타
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132001].levelList[level=1].name
   limit: do 40 znaków
   EN: Flame Strike
   PL: Flame Strike
535. [Umiejętność wroga [132001] (ulepszenie 1) — opis] [WhenUse] [MRcAiBa] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [MRcAiBa]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [MRcAiBa] = 불씨 / Ember
   EN: [WhenUse] Gain 1 [MRcAiBa]
   PL: [WhenUse] zyskuje 1 [MRcAiBa]
536. [Umiejętność wroga [132001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 5 부여, [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion] and +3 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 5 [Combustion] i 3 Licznika [Combustion]
537. [Umiejętność wroga [132002] (ulepszenie 1) — nazwa] 홍염익
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132002].levelList[level=1].name
   limit: do 40 znaków
   EN: Ardor Blossom Pinions
   PL: Ardor Blossom Pinions
538. [Umiejętność wroga [132002] (ulepszenie 1) — opis] [WhenUse] [MRcAiBa] 2 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [MRcAiBa]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [MRcAiBa] = 불씨 / Ember
   EN: [WhenUse] Gain 2 [MRcAiBa]
   PL: [WhenUse] zyskuje 2 [MRcAiBa]
539. [Umiejętność wroga [132002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [CrimsonResistDown] 2 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [CrimsonResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CrimsonResistDown] = 분노 내성 약화 / Wrath Resist Down
   EN: [OnSucceedAttack] Inflict 2 [CrimsonResistDown] next turn
   PL: [OnSucceedAttack] nakłada 2 [CrimsonResistDown] w następnej turze
540. [Umiejętność wroga [132003] (ulepszenie 1) — nazwa] 점화
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132003].levelList[level=1].name
   limit: do 40 znaków
   EN: Spark
   PL: Spark
541. [Umiejętność wroga [132003] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion] 횟수 2 증가\n[WinDuel] 대상의 [Combustion]만큼 [Combustion] 부여\n[DefeatDuel] 아래 효과 적용\n- 이 스킬의 피해로 대상이 흐트러지지 않음\n- 이 스킬이 분노 속성 스킬이면, 대상의 [Combustion] 제거\n- [Combustion], [Combustion] 횟수 부여량이 절반으로 감소함
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132003].levelList[level=1].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [WinDuel], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Inflict +2 [Combustion] Count\n[WinDuel] Inflict [Combustion] equal to [Combustion] on target\n[DefeatDuel] Gain the following effects:\n- Damage dealt by this Skill cannot Stagger the target\n- If this is a Wrath Skill, remove [Combustion] on the target\n- Halve the amount of [Combustion] and [Combustion] Count this Skill inflicts
   PL: [WhenUse] nakłada 2 Licznika [Combustion]\n[WinDuel] nakłada [Combustion] równy [Combustion] celu\n[DefeatDuel] zyskuje następujące efekty:\n- obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n- jeżeli to Umiejętność Gniewu, usuwa [Combustion] celu\n- ilość nakładanych [Combustion] i Liczników [Combustion] maleje o połowę
542. [Umiejętność wroga [132003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Umiejętność wroga [132003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [MRcAiBb]가 3 이상이면,\n- [Combustion] 10 부여\n- [Combustion] 횟수 2 증가\n- [MRcAiBc] 2 부여\n- [MRcAiBb] 전부 감소
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [UnBrokenCoinOnSucceedAttack], [MRcAiBb], [Combustion], [MRcAiBc]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [MRcAiBb] = 아른거리는 불씨 / Shimmering Ember; [Combustion] = 화상 / Burn; [MRcAiBc] = 점화 / Spark
   EN: [UnBrokenCoinOnSucceedAttack] If target has 3+ [MRcAiBb]...\n- Inflict 10 [Combustion]\n- Inflict +2 [Combustion] Count\n- Inflict 2 [MRcAiBc]\n- [MRcAiBb] expires completely
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli cel ma 3+ [MRcAiBb]...\n- nakłada 10 [Combustion]\n- nakłada 2 Licznika [Combustion]\n- nakłada 2 [MRcAiBc]\n- [MRcAiBb] wygasają całkowicie
544. [Umiejętność wroga [132003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Umiejętność wroga [132003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 6 부여, [Combustion] 횟수 4 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 6 [Combustion] and +4 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 6 [Combustion] i 4 Licznika [Combustion]
546. [Umiejętność wroga [132003] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [CrimsonResistDown] 2 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132003].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 539 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [Umiejętność wroga [132004] (ulepszenie 1) — nazwa] 분진 폭발
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132004].levelList[level=1].name
   limit: do 40 znaków
   EN: Dust Explosion
   PL: Dust Explosion
548. [Umiejętność wroga [132004] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion]이 5이상이면, 이 스킬의 합 위력 +2
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: [WhenUse] If target has 5+ [Combustion], this Skill gains Clash Power +2
   PL: [WhenUse] jeżeli cel ma 5+ [Combustion], ta Umiejętność zyskuje Moc Starcia +2
549. [Umiejętność wroga [132004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이번 턴에 홍염 나방이 사용할 분노 스킬 수만큼 [Combustion] 횟수 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict [Combustion] Count equal to the number of Wrath Skills that the Ardor Blossom Moth will use this turn
   PL: [OnSucceedAttack] nakłada Licznika [Combustion] równy liczbie Umiejętności Gniewu, których Ardor Blossom Moth użyje w tej turze
550. [Umiejętność wroga [132004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 가장 느린 적에게 홍염 나방이 사용하는 분노 스킬 수만큼 [Combustion] 횟수 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Against the enemy with the slowest Speed, inflict [Combustion] Count equal to the number of Wrath Skills that the Ardor Blossom Moth will use this turn
   PL: [OnSucceedAttackHead] wrogowi z najniższą Szybkością nakłada Licznika [Combustion] równy liczbie Umiejętności Gniewu, których Ardor Blossom Moth użyje w tej turze
551. [Umiejętność wroga [132004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 이번 턴에 홍염 나방이 사용할 분노 스킬 수만큼 [Combustion] 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict [Combustion] equal to the number of Wrath Skills that the Ardor Blossom Moth will use this turn
   PL: [OnSucceedAttack] nakłada [Combustion] równy liczbie Umiejętności Gniewu, których Ardor Blossom Moth użyje w tej turze
552. [Umiejętność wroga [132004] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 가장 느린 적에게 홍염 나방이 사용하는 분노 스킬 수만큼 [Combustion] 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132004].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Against the enemy with the lowest Speed, inflict [Combustion] equal to the number of Wrath Skills that the Ardor Blossom Moth will use this turn
   PL: [OnSucceedAttackHead] wrogowi z najniższą Szybkością nakłada [Combustion] równy liczbie Umiejętności Gniewu, których Ardor Blossom Moth użyje w tej turze
553. [Umiejętność wroga [132005] (ulepszenie 1) — nazwa] 홍염살
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132005].levelList[level=1].name
   limit: do 40 znaków
   EN: Ardor Blossom Star
   PL: Ardor Blossom Star
554. [Umiejętność wroga [132005] (ulepszenie 1) — opis] (이번 턴에 홍염 나방이 사용할 분노 스킬 수 x 2)만큼 합 위력 증가\n[WhenUse] 모든 적에게 (홍염 나방이 사용하는 분노 스킬 수 x 2)만큼 [Combustion] 부여\n[DefeatDuel] 아래 효과 적용\n- 이 공격 스킬이 가하는 피해는 0이 됨\n- 모든 대상의 [Combustion] 제거\n- 이 스킬의 [Combustion], [Combustion] 횟수 부여량이 절반으로 감소함
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132005].levelList[level=1].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Gain Clash Power equal to (# of Wrath Skills that the Ardor Blossom Moth will use this turn x2)\n[WhenUse] Inflict (# of Wrath Skills that the Ardor Blossom Moth will use this turn x2) [Combustion] to all enemies\n[DefeatDuel] Gain the following effects:\n- This Attack Skill deals 0 damage\n- Remove [Combustion] from all targets\n- Halve the amount of [Combustion] and [Combustion] Count this Skill inflicts
   PL: zyskuje Moc Starcia równą (liczba Umiejętności Gniewu, których Ardor Blossom Moth użyje w tej turze x 2)\n[WhenUse] nakłada (# Umiejętności Gniewu, których Ardor Blossom Moth użyje w tej turze x 2) [Combustion] wszystkim wrogom\n[DefeatDuel] zyskuje następujące efekty:\n- ta Umiejętność ataku zadaje 0 obrażeń\n- usuwa [Combustion] wszystkich celów\n- ilość nakładanych przez tę Umiejętność [Combustion] i Liczników [Combustion] maleje o połowę
555. [Umiejętność wroga [132005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Umiejętność wroga [132005] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 이번 턴에 홍염 나방이 사용할 분노 스킬 수만큼 [Combustion] 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132005].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Umiejętność wroga [132005] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 가장 느린 적에게 이번 턴에 홍염 나방이 사용할 분노 스킬 수만큼 [Combustion] 부여, [Combustion] 횟수 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132005].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Against the enemy with the slowest Speed, Inflict [Combustion] and [Combustion] Count equal to the number of Wrath Skills that the Ardor Blossom Moth will use this turn
   PL: [UnBrokenCoinOnSucceedAttack] wrogowi z najniższą Szybkością nakłada [Combustion] i Licznik [Combustion] równy liczbie Umiejętności Gniewu, których Ardor Blossom Moth użyje w tej turze
558. [Umiejętność wroga [132005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Umiejętność wroga [132005] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 이번 턴에 홍염 나방이 사용할 분노 스킬 수만큼 [Combustion] 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132005].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Umiejętność wroga [132005] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 가장 느린 적에게 이번 턴에 홍염 나방이 사용할 분노 스킬 수만큼 [Combustion] 부여, [Combustion] 횟수 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132005].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Umiejętność wroga [132005] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132005].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Umiejętność wroga [132005] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 피해량의 70%만큼 흐트러짐 손상 입힘
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132005].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Raise the target's Stagger Threshold by 70% of damage dealt
   PL: [UnBrokenCoinOnSucceedAttack] podnosi Próg Oszołomienia celu o 70% zadanych obrażeń
563. [Umiejętność wroga [132005] (ulepszenie 1) — moneta 3, efekt 3 — opis] - 이 피해로 흐트러짐 상태가 된 적에게 [Combustion] 10 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132005].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: - Inflict 10 [Combustion] against targets that have been Staggered by this
   PL: - nakłada 10 [Combustion] wrogom, którzy przeszli w Oszołamienie od tych obrażeń
564. [Umiejętność wroga [132006] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132006].levelList[level=1].name
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Umiejętność wroga [132006] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion] 4당 기본 위력 +1 (최대 3)\n[WhenUse] 대상에게 [Combustion] 4 부여\n[OnSucceedEvade] 다음 턴에 [MRcAiBa] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132006].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [OnSucceedEvade], [MRcAiBa]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [MRcAiBa] = 불씨 / Ember
   EN: [WhenUse] Base Power +1 for every 4 [Combustion] on target (max 3)\n[WhenUse] Inflict 4 [Combustion]\n[OnSucceedEvade] Gain 1 [MRcAiBa] next turn
   PL: [WhenUse] Moc Bazowa +1 za każde 4 [Combustion] celu (maks. 3)\n[WhenUse] nakłada 4 [Combustion]\n[OnSucceedEvade] zyskuje 1 [MRcAiBa] w następnej turze
566. [Umiejętność wroga [132007] (ulepszenie 1) — nazwa] 불씨 지피기
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132007].levelList[level=1].name
   limit: do 40 znaków
   EN: Stoke the Flames
   PL: Stoke the Flames
567. [Umiejętność wroga [132007] (ulepszenie 1) — opis] [CantDuel] [CantChangeTarget]\n이 공격 스킬이 가하는 피해는 0이 됨
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132007].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]
   EN: [CantDuel] [CantChangeTarget]\nDamage dealt by this Attack Skill is fixed to 0
   PL: [CantDuel] [CantChangeTarget]\nta Umiejętność ataku zadaje 0 obrażeń
568. [Umiejętność wroga [132007] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [MRcAiBb] 2 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132007].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MRcAiBb]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MRcAiBb] = 아른거리는 불씨 / Shimmering Ember
   EN: [OnSucceedAttack] Inflict 2 [MRcAiBb] next turn
   PL: [OnSucceedAttack] nakłada 2 [MRcAiBb] w następnej turze
569. [Umiejętność wroga [132101] (ulepszenie 1) — nazwa] 물어뜯기
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132101].levelList[level=1].name
   limit: do 40 znaków
   EN: Bite
   PL: Bite
570. [Umiejętność wroga [132101] (ulepszenie 1) — opis] [StartBattle] [SelfCharge] 2 얻음\n[WhenUse] 자신의 [SelfCharge]이 5 이상이면, 기본 위력 +2\n[DefeatDuel] [SelfCharge] 1 소모
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132101].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SelfCharge], [WhenUse], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SelfCharge] = 자가 충전 / Self-charge; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 2 [SelfCharge]\n[WhenUse] At 5+ [SelfCharge], Base Power +2\n[DefeatDuel] Lose 1 [SelfCharge]
   PL: [StartBattle] zyskuje 2 [SelfCharge]\n[WhenUse] przy 5+ [SelfCharge], Moc Bazowa +2\n[DefeatDuel] traci 1 [SelfCharge]
571. [Umiejętność wroga [132101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Umiejętność wroga [132102] (ulepszenie 1) — nazwa] 꼬리찌르기
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132102].levelList[level=1].name
   limit: do 40 znaków
   EN: Tail Poke
   PL: Tail Poke
573. [Umiejętność wroga [132102] (ulepszenie 1) — opis] [StartBattle] [SelfCharge] 2 얻음\n[WhenUse] 자신의 [SelfCharge]이 5 이상이면, 코인 위력 +1\n[DefeatDuel] [SelfCharge] 1 소모
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132102].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SelfCharge], [WhenUse], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SelfCharge] = 자가 충전 / Self-charge; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 2 [SelfCharge]\n[WhenUse] At 5+ [SelfCharge], Coin Power +1\n[DefeatDuel] Lose 1 [SelfCharge]
   PL: [StartBattle] zyskuje 2 [SelfCharge]\n[WhenUse] przy 5+ [SelfCharge], Moc Monety +1\n[DefeatDuel] traci 1 [SelfCharge]
574. [Umiejętność wroga [132102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Umiejętność wroga [132102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 2 [Binding] w następnej turze
576. [Umiejętność wroga [132103] (ulepszenie 1) — nazwa] 감아 조이기
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132103].levelList[level=1].name
   limit: do 40 znaków
   EN: Wrapping Coil
   PL: Wrapping Coil
577. [Umiejętność wroga [132103] (ulepszenie 1) — opis] [StartBattle] [SelfCharge] 3 얻음\n[WhenUse] 자신의 [SelfCharge]이 5 이상이면, 기본 위력 +2\n[DefeatDuel] [SelfCharge] 1 소모
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132103].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SelfCharge], [WhenUse], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SelfCharge] = 자가 충전 / Self-charge; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 3 [SelfCharge]\n[WhenUse] At 5+ [SelfCharge], Base Power +2\n[DefeatDuel] Lose 1 [SelfCharge]
   PL: [StartBattle] zyskuje 3 [SelfCharge]\n[WhenUse] przy 5+ [SelfCharge], Moc Bazowa +2\n[DefeatDuel] traci 1 [SelfCharge]
578. [Umiejętność wroga [132103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Umiejętność wroga [132103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 2 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable]
   PL: [OnSucceedAttack] nakłada 2 [Vulnerable]
580. [Umiejętność wroga [132103] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132103].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Binding] w następnej turze
581. [Umiejętność wroga [132104] (ulepszenie 1) — nazwa] 전류 주입
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132104].levelList[level=1].name
   limit: do 40 znaków
   EN: Electric Load
   PL: Electric Load
582. [Umiejętność wroga [132104] (ulepszenie 1) — opis] [StartBattle] [SelfCharge] 1 얻음\n[WhenUse] 자신의 [SelfCharge]이 5 이상이면, 코인 위력 +1\n대상에게 [Paralysis]가 있다면 피해량 +30%\n[DefeatDuel] [SelfCharge] 2 소모
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132104].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SelfCharge], [WhenUse], [Paralysis], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SelfCharge] = 자가 충전 / Self-charge; [WhenUse] = [사용시] / [On Use]; [Paralysis] = 마비 / Paralyze; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 1 [SelfCharge]\n[WhenUse] At 5+ [SelfCharge], Coin Power +1\nIf target has [Paralysis], deal +30% damage\n[DefeatDuel] Lose 2 [SelfCharge]
   PL: [StartBattle] zyskuje 1 [SelfCharge]\n[WhenUse] przy 5+ [SelfCharge], Moc Monety +1\njeżeli cel ma [Paralysis], zadaje +30% obrażeń\n[DefeatDuel] traci 2 [SelfCharge]
583. [Umiejętność wroga [132104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 261 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Umiejętność wroga [132104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis]
   PL: [OnSucceedAttack] nakłada 3 [Paralysis]
585. [Umiejętność wroga [132105] (ulepszenie 1) — nazwa] 전기 방류
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132105].levelList[level=1].name
   limit: do 40 znaków
   EN: Electric Release
   PL: Electric Release
586. [Umiejętność wroga [132105] (ulepszenie 1) — opis] [StartBattle] [SelfCharge] 1 얻음\n[WhenUse] 자신의 [SelfCharge]이 5 이상이면, 코인 위력 +1\n대상에게 [Paralysis]가 있다면 피해량 +30%\n[DefeatDuel] [SelfCharge] 3 소모
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132105].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SelfCharge], [WhenUse], [Paralysis], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SelfCharge] = 자가 충전 / Self-charge; [WhenUse] = [사용시] / [On Use]; [Paralysis] = 마비 / Paralyze; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Gain 1 [SelfCharge]\n[WhenUse] At 5+ [SelfCharge], Coin Power +1\nIf target has [Paralysis], deal +30% damage\n[DefeatDuel] Lose 3 [SelfCharge]
   PL: [StartBattle] zyskuje 1 [SelfCharge]\n[WhenUse] przy 5+ [SelfCharge], Moc Monety +1\njeżeli cel ma [Paralysis], zadaje +30% obrażeń\n[DefeatDuel] traci 3 [SelfCharge]
587. [Umiejętność wroga [132105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Umiejętność wroga [132105] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132105].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Umiejętność wroga [132105] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132105].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Umiejętność wroga [132106] (ulepszenie 1) — nazwa] 전기 방출
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132106].levelList[level=1].name
   limit: do 40 znaków
   EN: Electric Discharge
   PL: Electric Discharge
591. [Umiejętność wroga [132106] (ulepszenie 1) — opis] [StartBattle] [SelfCharge] 1 얻음\n대상에게 [Paralysis]가 있다면 피해량 +30%
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132106].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SelfCharge], [Paralysis]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SelfCharge] = 자가 충전 / Self-charge; [Paralysis] = 마비 / Paralyze
   EN: [StartBattle] Gain 1 [SelfCharge]\nIf target has [Paralysis], deal +30% damage
   PL: [StartBattle] zyskuje 1 [SelfCharge]\njeżeli cel ma [Paralysis], zadaje +30% obrażeń
592. [Umiejętność wroga [132106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 2 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Umiejętność wroga [132106] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 5 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132106].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 5 [Paralysis]
   PL: [OnSucceedAttack] nakłada 5 [Paralysis]
594. [Umiejętność wroga [132107] (ulepszenie 1) — nazwa] 초고압 전기 방출
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132107].levelList[level=1].name
   limit: do 50 znaków
   EN: High-voltage Electric Discharge
   PL: High-voltage Electric Discharge
595. [Umiejętność wroga [132107] (ulepszenie 1) — opis] [WhenUse] 가지고 있는 [SelfCharge] 전부 소모하고, 소모한 [SelfCharge]이 10 이상이면, 합 위력 +5\n[DefeatDuel] 이 공격 스킬이 가하는 피해는 0이 됨
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132107].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [SelfCharge], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SelfCharge] = 자가 충전 / Self-charge; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Lose all [SelfCharge] on self; if this unit lost 10+ [SelfCharge], gain Clash Power +5\n[DefeatDuel] This Attack Skill deals 0 damage
   PL: [WhenUse] traci wszystkie [SelfCharge] jednostki; jeżeli straciła 10+ [SelfCharge], zyskuje Moc Starcia +5\n[DefeatDuel] ta Umiejętność ataku zadaje 0 obrażeń
596. [Umiejętność wroga [132107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Umiejętność wroga [132107] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 메인 대상에게 [Vulnerable] 2 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132107].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Vulnerable] on the main target
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Vulnerable] głównemu celowi
598. [Umiejętność wroga [132107] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132107].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Umiejętność wroga [132107] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [ElectricStorage] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132107].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ElectricStorage]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ElectricStorage] = 축전 / Capacitor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [ElectricStorage]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [ElectricStorage]
600. [Umiejętność wroga [132107] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 메인 대상에게 [Paralysis] 3 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132107].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Paralysis] on the main target
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Paralysis] głównemu celowi
601. [Umiejętność wroga [132107] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] 대상이 [ElectricStorage] 상태일 때, 최종 피해량의 40%만큼 고정 피해
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132107].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ElectricStorage]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ElectricStorage] = 축전 / Capacitor
   EN: [OnSucceedAttack] If target has [ElectricStorage], deal 40% of final damage dealt as fixed damage
   PL: [OnSucceedAttack] jeżeli cel ma [ElectricStorage], zadaje stałe obrażenia równe 40% końcowych zadanych obrażeń
602. [Umiejętność wroga [132108] (ulepszenie 1) — nazwa] 똬리틀기
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132108].levelList[level=1].name
   limit: do 40 znaków
   EN: Coil Up
   PL: Coil Up
603. [Umiejętność wroga [132108] (ulepszenie 1) — opis] [StartBattle] 머리 부위 현재 체력만큼 보호막 얻음\n[EndBattle] 머리 부위에 보호막이 있으면, 다음 턴에 [SelfCharge] 10 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132108].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [EndBattle], [SelfCharge]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [EndBattle] = [턴 종료 시] / [Turn End]; [SelfCharge] = 자가 충전 / Self-charge
   EN: [StartBattle] The Head Part gains Shield by its current HP\n[EndBattle] If the Head Part has Shield, gain 10 [SelfCharge] next turn
   PL: [StartBattle] Część Głowy zyskuje Tarczę równą swojemu aktualnemu HP\n[EndBattle] jeżeli Część Głowy ma Tarczę, zyskuje 10 [SelfCharge] w następnej turze
604. [Umiejętność wroga [132109] (ulepszenie 1) — nazwa] 꿈틀거리는 머리
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132109].levelList[level=1].name
   limit: do 40 znaków
   EN: Wriggling Head
   PL: Wriggling Head
605. [Umiejętność wroga [132109] (ulepszenie 1) — opis] 체력이 가장 낮은 적 우선 공격\n대상에게 [Paralysis]가 있다면 피해량 +50%\n<color=#ff6000><mark color=#ff000040><b><u>대상이 수비 스킬을 사용했으면 피해량 -100%</color></mark></b></u>\n[SelfCharge] 1당 기본 위력 +1\n[WhenUse] [SelfCharge] 1 소모\n[EndSkill] 일방 공격이었으면, [SelfCharge] 1 소모\n- 공격한 대상이 수비 스킬을 사용했으면, [SelfCharge] 1 추가 소모
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132109].levelList[level=1].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Paralysis], [SelfCharge], [WhenUse], [EndSkill]
   znaczenie tagów: [Paralysis] = 마비 / Paralyze; [SelfCharge] = 자가 충전 / Self-charge; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Prioritizes targets with the least HP\nIf target has [Paralysis], deal +50% damage\n<color=#ff6000><mark color=#ff000040><b><u>If target has used a Defense Skill, deal -100% damage</color></mark></b></u>\nBase Power +1 for every [SelfCharge]\n[WhenUse] Lose 1 [SelfCharge]\n[EndSkill] If it was an Unopposed Attack, lose 1 [SelfCharge]\n- If the target attacked by this Skill used a Defense Skill, lose 1 more [SelfCharge]
   PL: priorytet: wrogowie z najmniejszym HP\njeżeli cel ma [Paralysis], zadaje +50% obrażeń\n<color=#ff6000><mark color=#ff000040><b><u>jeżeli cel użył Umiejętności obrony, zadaje o 100% mniej obrażeń</u></b></mark></color>\nMoc Bazowa +1 za każde [SelfCharge]\n[WhenUse] traci 1 [SelfCharge]\n[EndSkill] jeżeli był to nieprzeciwstawiany atak, traci 1 [SelfCharge]\n- jeżeli zaatakowany cel użył Umiejętności obrony, traci dodatkowe 1 [SelfCharge]
606. [Umiejętność wroga [132109] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132109].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Umiejętność wroga [132109] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132109].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Umiejętność wroga [132110] (ulepszenie 1) — nazwa] 꿈틀거리는 꼬리
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132110].levelList[level=1].name
   limit: do 40 znaków
   EN: Wriggling Tail
   PL: Wriggling Tail
609. [Umiejętność wroga [132110] (ulepszenie 1) — opis] 체력이 가장 낮은 적 우선 공격\n대상에게 [Paralysis]가 있다면 피해량 +50%\n<color=#ff6000><mark color=#ff000040><b><u>대상이 수비 스킬을 사용했으면 피해량 -100%</color></mark></b></u>\n[SelfCharge] 1당 기본 위력 +1\n[WhenUse] [SelfCharge] 1 소모\n[EndSkill] 일방 공격이었으면, [SelfCharge] 1 소모\n- 공격한 대상이 수비 스킬을 사용했으면, [SelfCharge] 1 추가 소모
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132110].levelList[level=1].desc
   (powtórzenie elementu 605 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Umiejętność wroga [132110] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132110].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] nakłada 2 [Laceration]
611. [Umiejętność wroga [132110] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132110].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 610 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Umiejętność wroga [132110] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132110].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność wroga [132201] (ulepszenie 1) — nazwa] 이연[二連]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132201].levelList[level=1].name
   limit: do 40 znaków
   EN: Twinslash [二連]
   PL: Twinslash [二連]
614. [Umiejętność wroga [132201] (ulepszenie 1) — opis] [WhenUse] [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] zyskuje 2 Licznika [Breath]
615. [Umiejętność wroga [132201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Umiejętność wroga [132201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Umiejętność wroga [132202] (ulepszenie 1) — nazwa] 삼연[三連]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132202].levelList[level=1].name
   limit: do 40 znaków
   EN: Tripleslash [三連]
   PL: Tripleslash [三連]
618. [Umiejętność wroga [132202] (ulepszenie 1) — opis] [WhenUse] [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +3 [Breath] Count
   PL: [WhenUse] zyskuje 3 Licznika [Breath]
619. [Umiejętność wroga [132202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Umiejętność wroga [132202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Umiejętność wroga [132202] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Umiejętność wroga [132203] (ulepszenie 1) — nazwa] 쾌섬[快閃]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132203].levelList[level=1].name
   limit: do 40 znaków
   EN: Swift Glimmer [快閃]
   PL: Swift Glimmer [快閃]
623. [Umiejętność wroga [132203] (ulepszenie 1) — opis] [OnDirectAttack] [Breath] 5 얻음\n[DefeatDuel] 가중치 -2
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132203].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnDirectAttack], [Breath], [DefeatDuel]
   znaczenie tagów: [OnDirectAttack] = [일방 공격 시] / [On Unopposed Attack]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [OnDirectAttack] Gain 5 [Breath]\n[DefeatDuel] -2 Atk Weight
   PL: [OnDirectAttack] zyskuje 5 [Breath]\n[DefeatDuel] Waga Ataku -2
624. [Umiejętność wroga [132203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Umiejętność wroga [132203] (ulepszenie 1) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: +30% Damage on Critical Hit
   PL: +30% obrażeń przy trafieniu krytycznym
626. [Umiejętność wroga [132203] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132203].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Umiejętność wroga [132203] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [PhantomIncision] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132203].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PhantomIncision]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PhantomIncision] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [OnSucceedAttack] Inflict 1 [PhantomIncision]
   PL: [OnSucceedAttack] nakłada 1 [PhantomIncision]
628. [Umiejętność wroga [132203] (ulepszenie 1) — moneta 1, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [PhantomIncision] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132203].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [PhantomIncision]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [PhantomIncision] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [PhantomIncision]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [PhantomIncision]
629. [Umiejętność wroga [132204] (ulepszenie 1) — nazwa] 무형참[無形斬]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132204].levelList[level=1].name
   limit: do 40 znaków
   EN: Formless Cut [無形斬]
   PL: Formless Cut [無形斬]
630. [Umiejętność wroga [132204] (ulepszenie 1) — opis] [WideAreaRampage]\n속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬 종료시까지 흐트러짐 상태가 되지 않음\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132204].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [DefeatDuel]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WideAreaRampage]\nCan Clash with this Skill regardless of Speed; cannot be Staggered until this Skill ends\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WideAreaRampage]\nmoże stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości; nie przechodzi w Oszołamienie do końca tej Umiejętności\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
631. [Umiejętność wroga [132204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność wroga [132204] (ulepszenie 1) — moneta 1, efekt 2 — opis] 이 코인 재사용 (최대 4회)
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: Reuse this Coin (4 times max)
   PL: używa Monety ponownie (do 4 razy)
633. [Umiejętność wroga [132204] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132204].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Umiejętność wroga [132204] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [PhantomIncision] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132204].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 627 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Umiejętność wroga [132204] (ulepszenie 1) — moneta 1, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [PhantomIncision] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132204].levelList[level=1].coinlist[#0].coindescs[#4].desc
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Umiejętność wroga [132205] (ulepszenie 1) — nazwa] 공간참[空間斬]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132205].levelList[level=1].name
   limit: do 40 znaków
   EN: Rend Space [空間斬]
   PL: Rend Space [空間斬]
637. [Umiejętność wroga [132205] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬 종료시까지 흐트러짐 상태가 되지 않음\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132205].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel], [EndSkill]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Can Clash with this Skill regardless of Speed; cannot be Staggered until this Skill ends\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] End this turn
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości; nie przechodzi w Oszołamienie do końca tej Umiejętności\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[EndSkill] kończy tę turę
638. [Umiejętność wroga [132205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Umiejętność wroga [132205] (ulepszenie 1) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +100%
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132205].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: +100% Damage on Critical Hit
   PL: +100% obrażeń przy trafieniu krytycznym
640. [Umiejętność wroga [132205] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[PhantomIncision]을 모두 소모</u></b></mark></color>하여, 각 대상 최대 체력의 (소모값)% 만큼 체력 피해
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132205].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [PhantomIncision]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PhantomIncision] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Consume all [PhantomIncision] on target</u></b></mark></color> and deal ([PhantomIncision] consumed)% HP damage against each target, respectively
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>zużywa wszystkie [PhantomIncision] celu</u></b></mark></color> i zadaje każdemu celowi obrażenia HP równe (zużyte [PhantomIncision])% Maks. HP
641. [Umiejętność wroga [132206] (ulepszenie 1) — nazwa] 잔상보[殘像步]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132206].levelList[level=1].name
   limit: do 40 znaków
   EN: Phantom Step [殘像步]
   PL: Phantom Step [殘像步]
642. [Umiejętność wroga [132206] (ulepszenie 1) — opis] [DefeatDuel] 대상의 <color=#ff6000><mark=#ff000040><b><u>[PhantomIncision]이 절반으로 감소</u></b></mark></color> (소수점 버림)
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132206].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [DefeatDuel], [PhantomIncision]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [PhantomIncision] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [DefeatDuel] <color=#ff6000><mark=#ff000040><b><u>Halve the [PhantomIncision] Stack on target</u></b></mark></color> (rounded down)
   PL: [DefeatDuel] <color=#ff6000><mark=#ff000040><b><u>zmniejsza Licznik [PhantomIncision] celu o połowę</u></b></mark></color> (zaokrąglając w dół)
643. [Umiejętność wroga [132207] (ulepszenie 1) — nazwa] 관망
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132207].levelList[level=1].name
   limit: do 40 znaków
   EN: Silent Regard
   PL: Silent Regard
644. [Umiejętność wroga [132207] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] [Reduction] 2 얻음</u></b></mark></color>\n[DefeatDuel] 대상의 정신력 5 회복
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132207].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuel], [Reduction]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: <color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] Gain 2 [Reduction]</u></b></mark></color>\n[DefeatDuel] Target heals 5 SP
   PL: <color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] zyskuje 2 [Reduction]</u></b></mark></color>\n[DefeatDuel] cel przywraca 5 SP
645. [Umiejętność wroga [132207] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132207].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Umiejętność wroga [132208] (ulepszenie 1) — nazwa] 절명[絶命]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132208].levelList[level=1].name
   limit: do 40 znaków
   EN: Deathedge [絶命]
   PL: Deathedge [絶命]
647. [Umiejętność wroga [132208] (ulepszenie 1) — opis] 이 스킬은 대상의 수비 스킬을 발동시키지 않음\n현재 체력 비율이 가장 낮은 대상 공격\n- 료슈 외 수감자를 우선 공격
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132208].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This Skill does not trigger the target's Defense Skill\nPrioritizes the target with the least HP percentage\n- Prioritizes targets that aren't Ryōshū
   PL: ta Umiejętność nie uruchamia Umiejętności obrony celu\npriorytet: cel z najniższym procentem HP\n- priorytet: Grzesznicy inni niż Ryōshū
648. [Umiejętność wroga [132208] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 잃은 체력 1%당 [PhantomIncision] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132208].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PhantomIncision]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PhantomIncision] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [OnSucceedAttack] Inflict 1 [PhantomIncision] for every 1% missing HP on target
   PL: [OnSucceedAttack] nakłada 1 [PhantomIncision] za każde 1% brakującego HP celu
649. [Umiejętność wroga [132208] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[PhantomIncision]을 모두 소모</u></b></mark></color>하여, 대상 최대 체력의 (소모값)% 만큼 체력 피해
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132208].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [PhantomIncision]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PhantomIncision] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Consume all [PhantomIncision] on target</u></b></mark></color> and deal ([PhantomIncision] consumed)% HP damage
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>zużywa wszystkie [PhantomIncision] celu</u></b></mark></color> i zadaje obrażenia HP równe (zużyte [PhantomIncision])% Maks. HP celu
650. [Umiejętność wroga [132209] (ulepszenie 1) — nazwa] 공간참-연[空間斬-緣]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132209].levelList[level=1].name
   limit: do 60 znaków
   EN: Rend Space - String Connection [空間斬-緣]
   PL: Rend Space - String Connection [空間斬-緣]
651. [Umiejętność wroga [132209] (ulepszenie 1) — opis] [WhenUse] 자신의 정신력이 10 이상이면 망을 1개 생성. 최종 위력 +5\n속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] 이 스킬에서 망을 생성했으면, 정신력 -10\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132209].levelList[level=1].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] At 10+ SP, generate 1 Mang. Final Power +5\nCan Clash with this Skill regardless of Speed; cannot be Staggered until this Skill ends\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] If this skill generated 1 Mang, lose 10 SP\n[EndSkill] End this turn
   PL: [WhenUse] przy SP równym 10 lub więcej tworzy 1 Mang. Moc Końcowa +5\nmoże stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości; nie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[EndSkill] jeżeli ta Umiejętność utworzyła 1 Mang, traci 10 SP\n[EndSkill] kończy tę turę
652. [Umiejętność wroga [132209] (ulepszenie 1) — tekst klimatyczny] 공간을 베는 기술. 공간참. 공간을 베고자하는 마음은 검사들의 숙원이었고 다양한 방식으로 그 숙원에 도달했다.
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132209].levelList[level=1].flavor
   limit: do 240 znaków
   EN: A technique that cuts through space itself. Sundering the fabric of space has long been the ambition of those who live by the sword—a hard-won feat reached through divergent disciplines.
   PL: Technika przecinająca samoł przestrzeń. Rend Space. Pragnienie przecięcia przestrzeni było odwiecznym dążeniem szermierzy, a do tego celu dochodzono na wiele rozmaitych sposobów.
653. [Umiejętność wroga [132209] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132209].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [Umiejętność wroga [132209] (ulepszenie 1) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +100%
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132209].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Umiejętność wroga [132209] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[PhantomIncision]을 모두 소모</u></b></mark></color>하여, 각 대상 최대 체력의 (소모값)% 만큼 체력 피해
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132209].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 640 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Umiejętność wroga [132209] (ulepszenie 1) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132209].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain 1 [Breath]
   PL: [CriticalOnSucceedAttack] zyskuje 1 [Breath]
657. [Umiejętność wroga [132501] (ulepszenie 1) — nazwa] 머리 으깨기
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132501].levelList[level=1].name
   limit: do 40 znaków
   EN: Skull Crushing
   PL: Skull Crushing
658. [Umiejętność wroga [132501] (ulepszenie 1) — opis] 자신의 [Breath]과 대상의 [Sinking]의 합 6당, 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132501].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Sinking], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]
   EN: Final Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)\n[WhenUse] Gain +2 [Breath] Count
   PL: Moc Końcowa +1 za każde 6 łącznie ([Breath] jednostki + [Sinking] celu) (maks. 2)\n[WhenUse] zyskuje 2 Licznika [Breath]
659. [Umiejętność wroga [132501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] nakłada 1 [Sinking]
660. [Umiejętność wroga [132501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Umiejętność wroga [132502] (ulepszenie 1) — nazwa] 앗, 조용히 해주세요
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132502].levelList[level=1].name
   limit: do 40 znaków
   EN: Ah, Please be Quiet
   PL: Ah, Please be Quiet
662. [Umiejętność wroga [132502] (ulepszenie 1) — opis] 자신의 [Breath]과 대상의 [Sinking]의 합 6당, 최종 위력 +1 (최대 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>[PressureOfPrescript]이 있거나, [IndexPrescriptTargetToPersonality]이면,</u></b></mark></color> 마지막 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 피해량 -50%, 적중시 대상을 흐트러뜨리지 않고 [Sinking] 효과를 발동하지 않음\n[WhenUse] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132502].levelList[level=1].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Breath], [Sinking], [StartBattle], [PressureOfPrescript], [IndexPrescriptTargetToPersonality], [SuperCoin], [DefeatDuel], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [PressureOfPrescript] = 압박감 / Onus; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]; [WhenUse] = [사용시] / [On Use]
   EN: Final Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>If this unit has [PressureOfPrescript], or if target has [IndexPrescriptTargetToPersonality]</u></b></mark></color>, convert the final Coin to [SuperCoin]\n[DefeatDuel] Deal -50% damage; On Hit, does not Stagger the target; On Hit, does not activate [Sinking] on target\n[WhenUse] Gain 2 [Breath]
   PL: Moc Końcowa +1 za każde 6 łącznie ([Breath] jednostki + [Sinking] celu) (maks. 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>jeżeli jednostka ma [PressureOfPrescript] albo cel ma [IndexPrescriptTargetToPersonality]</u></b></mark></color>, ostatnia Moneta zmienia się w [SuperCoin]\n[DefeatDuel] zadaje o 50% mniej obrażeń; przy trafieniu nie Oszołomi celu i nie uruchamia [Sinking] celu\n[WhenUse] zyskuje 2 [Breath]
663. [Umiejętność wroga [132502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [Umiejętność wroga [132502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Umiejętność wroga [132502] (ulepszenie 1) — moneta 3, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Sinking] and +1 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Sinking] i 1 Licznika [Sinking]
666. [Umiejętność wroga [132503] (ulepszenie 1) — nazwa] 빠,빨리 지령을 수행해야만…
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132503].levelList[level=1].name
   limit: do 60 znaków
   EN: I-I Have to Execute the Prescript Soon...!
   PL: I-I Have to Execute the Prescript Soon...!
667. [Umiejętność wroga [132503] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>[PressureOfPrescript]이 2이면, 대상 변경 불가</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>수비 스킬 발동 불가</u></b></mark></color>\n자신의 [Breath]과 대상의 [Sinking]의 합 6당, 최종 위력 +1 (최대 3)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>[PressureOfPrescript]이 있거나, [IndexPrescriptTargetToPersonality]이면,</u></b></mark></color> 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 피해량 -80%, 적중시 대상을 흐트러뜨리지 않고 [Sinking] 효과를 발동하지 않음\n[WhenUse] [Breath] 2 얻음, 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132503].levelList[level=1].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [PressureOfPrescript], [Breath], [Sinking], [StartBattle], [IndexPrescriptTargetToPersonality], [SuperCoin], [DefeatDuel], [WhenUse]
   znaczenie tagów: [PressureOfPrescript] = 압박감 / Onus; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]; [WhenUse] = [사용시] / [On Use]
   EN: <color=#ff6000><mark=#ff000040><b><u>At 2 [PressureOfPrescript], cannot change target</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>Does not trigger Defense Skills</u></b></mark></color>\nFinal Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 3)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>If this unit has [PressureOfPrescript], or if target has [IndexPrescriptTargetToPersonality]</u></b></mark></color>, convert all Coins to [SuperCoin]s\n[DefeatDuel] Deal -80% damage; On Hit, does not Stagger the target; On Hit, does not activate [Sinking] on target\n[WhenUse] Gain 2 [Breath] and +2 [Breath] Count
   PL: <color=#ff6000><mark=#ff000040><b><u>przy 2 [PressureOfPrescript] nie może zmienić celu</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>nie uruchamia Umiejętności obrony</u></b></mark></color>\nMoc Końcowa +1 za każde 6 łącznie ([Breath] jednostki + [Sinking] celu) (maks. 3)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>jeżeli jednostka ma [PressureOfPrescript] albo cel ma [IndexPrescriptTargetToPersonality]</u></b></mark></color>, wszystkie Monety zmieniają się w [SuperCoin]y\n[DefeatDuel] zadaje o 80% mniej obrażeń; przy trafieniu nie Oszołomi celu i nie uruchamia [Sinking] celu\n[WhenUse] zyskuje 2 [Breath] i 2 Licznika [Breath]
668. [Umiejętność wroga [132503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Sinking]
669. [Umiejętność wroga [132503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Umiejętność wroga [132503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 Licznika [Sinking]
671. [Umiejętność wroga [132503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 피해량 +20%
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Deal +20% damage
   PL: [CriticalOnSucceedAttack] zadaje +20% obrażeń
672. [Umiejętność wroga [132504] (ulepszenie 1) — nazwa] 얌전히 으깨져주세요
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132504].levelList[level=1].name
   limit: do 70 znaków
   EN: Please Don't Resist and just be Crushed to Death
   PL: Please Don't Resist and just be Crushed to Death
673. [Umiejętność wroga [132504] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>속도와 상관없이 이 스킬과 합을 할 수 있음</u></b></mark></color>\n[DefeatDuel] [ResultReduction] 3, [Paralysis] 4 얻음\n[DefeatDuel] 피해량 -90%, 적중시 대상을 흐트러뜨리지 않고 [Sinking] 효과를 발동하지 않음\n[EndSkill] [PressureOfPrescript] 전부 소모
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132504].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuel], [ResultReduction], [Paralysis], [Sinking], [EndSkill], [PressureOfPrescript]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [ResultReduction] = 위력 감소 / Power Down; [Paralysis] = 마비 / Paralyze; [Sinking] = 침잠 / Sinking; [EndSkill] = [공격 종료시] / [Attack End]; [PressureOfPrescript] = 압박감 / Onus
   EN: <color=#ff6000><mark=#ff000040><b><u>Can Clash with this Skill regardless of Speed</u></b></mark></color>\n[DefeatDuel] Gain 3 [ResultReduction] and 4 [Paralysis]\n[DefeatDuel] Deal -90% damage; On Hit, does not Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] Consume all [PressureOfPrescript]
   PL: <color=#ff6000><mark=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\n[DefeatDuel] zyskuje 3 [ResultReduction] i 4 [Paralysis]\n[DefeatDuel] zadaje o 90% mniej obrażeń; przy trafieniu nie Oszołomi celu i nie uruchamia [Sinking] celu\n[EndSkill] zużywa wszystkie [PressureOfPrescript]
674. [Umiejętność wroga [132504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Umiejętność wroga [132504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain 1 [Breath]
   PL: [UnBrokenCoinOnSucceedAttack] zyskuje 1 [Breath]
676. [Umiejętność wroga [132504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Umiejętność wroga [132504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Umiejętność wroga [132504] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132504].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Umiejętność wroga [132504] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132504].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Umiejętność wroga [132504] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132504].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Umiejętność wroga [132504] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132504].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Umiejętność wroga [132505] (ulepszenie 1) — nazwa] 이 손으로 대신…
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132505].levelList[level=1].name
   limit: do 50 znaków
   EN: Let These Hands be the Proxy...
   PL: Let These Hands be the Proxy...
683. [Umiejętność wroga [132505] (ulepszenie 1) — opis] 자신의 [Breath]과 대상의 [Sinking]의 합 6당, 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[EndSkill] 정신력 3 감소
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132505].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Sinking], [WhenUse], [EndSkill]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Final Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)\n[WhenUse] Gain +2 [Breath] Count\n[EndSkill] Lose 3 SP
   PL: Moc Końcowa +1 za każde 6 łącznie ([Breath] jednostki + [Sinking] celu) (maks. 2)\n[WhenUse] zyskuje 2 Licznika [Breath]\n[EndSkill] traci 3 SP
684. [Umiejętność wroga [132505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] nakłada 2 [Sinking]
685. [Umiejętność wroga [132505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Sinking]
686. [Umiejętność wroga [132506] (ulepszenie 1) — nazwa] 파헤치고, 파헤치겠어요
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132506].levelList[level=1].name
   limit: do 40 znaków
   EN: Disembowel, Eviscerate...
   PL: Disembowel, Eviscerate...
687. [Umiejętność wroga [132506] (ulepszenie 1) — opis] 자신의 [Breath]과 대상의 [Sinking]의 합 6당, 최종 위력 +1 (최대 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>[PressureOfPrescript]이 있거나, [IndexPrescriptTargetToPersonality]이면,</u></b></mark></color> 마지막 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 피해량 -50%, 적중시 대상을 흐트러뜨리지 않고 [Sinking] 효과를 발동하지 않음\n[WhenUse] [Breath] 2 얻음\n[EndSkill] 정신력 3 감소
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132506].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Breath], [Sinking], [StartBattle], [PressureOfPrescript], [IndexPrescriptTargetToPersonality], [SuperCoin], [DefeatDuel], [WhenUse], [EndSkill]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [PressureOfPrescript] = 압박감 / Onus; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]; [WhenUse] = [사용시] / [On Use] …
   EN: Final Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>If this unit has [PressureOfPrescript], or if target has [IndexPrescriptTargetToPersonality]</u></b></mark></color>, convert the final Coin to [SuperCoin]\n[DefeatDuel] Deal -50% damage; On Hit, does not Stagger the target; On Hit, does not activate [Sinking] on target\n[WhenUse] Gain 2 [Breath]\n[EndSkill] Lose 3 SP
   PL: Moc Końcowa +1 za każde 6 łącznie ([Breath] jednostki + [Sinking] celu) (maks. 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>jeżeli jednostka ma [PressureOfPrescript] albo cel ma [IndexPrescriptTargetToPersonality]</u></b></mark></color>, ostatnia Moneta zmienia się w [SuperCoin]\n[DefeatDuel] zadaje o 50% mniej obrażeń; przy trafieniu nie Oszołomi celu i nie uruchamia [Sinking] celu\n[WhenUse] zyskuje 2 [Breath]\n[EndSkill] traci 3 SP
688. [Umiejętność wroga [132506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Umiejętność wroga [132506] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132506].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Umiejętność wroga [132506] (ulepszenie 1) — moneta 3, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132506].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 670 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Umiejętność wroga [132507] (ulepszenie 1) — nazwa] 대행: 새기기
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132507].levelList[level=1].name
   limit: do 40 znaków
   EN: Procuration: Engrave
   PL: Procuration: Engrave
692. [Umiejętność wroga [132507] (ulepszenie 1) — opis] 자신의 [Breath]과 대상의 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>[PressureOfPrescript]이 있거나, [IndexPrescriptTargetToPersonality]이면,</u></b></mark></color> 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>[IndexPrescriptTargetToPersonality]이면, 피해량 +50%</u></b></mark></color>\n[WhenUse] [Breath] 3 얻음, 자신의 [Breath] 횟수 3 증가\n[DefeatDuel] 피해량 -80%, 적중시 대상을 흐트러뜨리지 않고 [Sinking] 효과를 발동하지 않음\n[EndSkill] 정신력 6 감소
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132507].levelList[level=1].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Breath], [Sinking], [StartBattle], [PressureOfPrescript], [IndexPrescriptTargetToPersonality], [SuperCoin], [WhenUse], [DefeatDuel], [EndSkill]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [PressureOfPrescript] = 압박감 / Onus; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose] …
   EN: Coin Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>If this unit has [PressureOfPrescript], or if target has [IndexPrescriptTargetToPersonality]</u></b></mark></color>, convert all Coins on this Skill to [SuperCoin]s\n[WhenUse]<color=#ff6000><mark=#ff000040><b><u>If the target has [IndexPrescriptTargetToPersonality], deal +50% damage</u></b></mark></color>\n[WhenUse] Gain 3 [Breath] and +3 [Breath] Count\n[DefeatDuel] Deal -80% damage; On Hit, does not Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] Lose 6 SP
   PL: Moc Monety +1 za każde 6 łącznie ([Breath] jednostki + [Sinking] celu) (maks. 2)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>jeżeli jednostka ma [PressureOfPrescript] albo cel ma [IndexPrescriptTargetToPersonality]</u></b></mark></color>, wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin]y\n[WhenUse]<color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma [IndexPrescriptTargetToPersonality], zadaje +50% obrażeń</u></b></mark></color>\n[WhenUse] zyskuje 3 [Breath] i 3 Licznika [Breath]\n[DefeatDuel] zadaje o 80% mniej obrażeń; przy trafieniu nie Oszołomi celu i nie uruchamia [Sinking] celu\n[EndSkill] traci 6 SP
693. [Umiejętność wroga [132507] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132507].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Sinking]
694. [Umiejętność wroga [132507] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132507].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 Licznika [Sinking]
695. [Umiejętność wroga [132508] (ulepszenie 1) — nazwa] 대행: 말살
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132508].levelList[level=1].name
   limit: do 40 znaków
   EN: Procuration: Annihilate
   PL: Procuration: Annihilate
696. [Umiejętność wroga [132508] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>속도와 상관없이 이 스킬과 합을 할 수 있음</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>[IndexPrescriptTargetToPersonality]이면, 피해량 +100%</u></b></mark></color>\n[DefeatDuel] [ResultReduction] 3, [Paralysis] 4 얻음\n[DefeatDuel] 피해량 -90%, 적중시 대상을 흐트러뜨리지 않고 [Sinking] 효과를 발동하지 않음\n[EndSkill] 정신력 15 감소\n[EndSkill] [PressureOfPrescript] 전부 소모
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132508].levelList[level=1].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [IndexPrescriptTargetToPersonality], [DefeatDuel], [ResultReduction], [Paralysis], [Sinking], [EndSkill], [PressureOfPrescript]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [DefeatDuel] = [합 패배] / [Clash Lose]; [ResultReduction] = 위력 감소 / Power Down; [Paralysis] = 마비 / Paralyze; [Sinking] = 침잠 / Sinking; [EndSkill] = [공격 종료시] / [Attack End]; [PressureOfPrescript] = 압박감 / Onus
   EN: <color=#ff6000><mark=#ff000040><b><u>Can Clash with this Skill regardless of Speed</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>If the target has [IndexPrescriptTargetToPersonality], deal +100% damage</u></b></mark></color>\n[DefeatDuel] Gain 3 [ResultReduction] and 4 [Paralysis]\n[DefeatDuel] Deal -90% damage; On Hit, does not Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] Lose 15 SP\n[EndSkill] Consume all [PressureOfPrescript]
   PL: <color=#ff6000><mark=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma [IndexPrescriptTargetToPersonality], zadaje +100% obrażeń</u></b></mark></color>\n[DefeatDuel] zyskuje 3 [ResultReduction] i 4 [Paralysis]\n[DefeatDuel] zadaje o 90% mniej obrażeń; przy trafieniu nie Oszołomi celu i nie uruchamia [Sinking] celu\n[EndSkill] traci 15 SP\n[EndSkill] zużywa wszystkie [PressureOfPrescript]
697. [Umiejętność wroga [132508] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132508].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Umiejętność wroga [132508] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132508].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 668 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Umiejętność wroga [132508] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132508].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Umiejętność wroga [132508] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132508].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 668 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Umiejętność wroga [132508] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132508].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Umiejętność wroga [132508] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132508].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 668 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Umiejętność wroga [132508] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132508].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Umiejętność wroga [132508] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132508].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 668 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Umiejętność wroga [132509] (ulepszenie 1) — nazwa] 대행: 말살 - 본망[本望]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132509].levelList[level=1].name
   limit: do 80 znaków
   EN: Procuration: Annihilation - Mang of Immanent Yearning [本望]
   PL: Procuration: Annihilation - Mang of Immanent Yearning [本望]
706. [Umiejętność wroga [132509] (ulepszenie 1) — opis] [WhenUse] <color=#ff6000><mark=#ff000040><b><u>정신력이 0 이상이면, 망 1개 생성</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>피해량 +20%, 최종 위력과 코인 위력 각각 +2</u></b></mark></color>\n[EndSkill] 정신력 15 감소\n[EndSkill] 망을 생성했으면, 정신력 20 소모\n[EndSkill] [PressureOfPrescript] 전부 소모, 이번 턴 종료
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132509].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [EndSkill], [PressureOfPrescript]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]; [PressureOfPrescript] = 압박감 / Onus
   EN: [WhenUse] <color=#ff6000><mark=#ff000040><b><u>At 0+ SP, generate 1 Mang</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>Deal +20% damage, Final Power +2, Coin Power +2</u></b></mark></color>\n[EndSkill] Lose 15 SP\n[EndSkill] If this Skill generated Mang, lose 20 SP\n[EndSkill] Consume all [PressureOfPrescript] and end this turn
   PL: [WhenUse] <color=#ff6000><mark=#ff000040><b><u>przy SP równym 0 lub więcej tworzy 1 Mang</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>zadaje +20% obrażeń, Moc Końcowa +2 i Moc Monety +2</u></b></mark></color>\n[EndSkill] traci 15 SP\n[EndSkill] jeżeli ta Umiejętność utworzyła Mang, traci 20 SP\n[EndSkill] zużywa wszystkie [PressureOfPrescript] i kończy tę turę
707. [Umiejętność wroga [132509] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132509].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [Umiejętność wroga [132509] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132509].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Umiejętność wroga [132509] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132509].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Umiejętność wroga [132509] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132509].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Umiejętność wroga [132509] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132509].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Umiejętność wroga [132509] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132509].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Umiejętność wroga [132509] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132509].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Umiejętność wroga [132509] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132509].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Umiejętność wroga [132509] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132509].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Umiejętność wroga [132509] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=132509].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Umiejętność wroga [877311] (ulepszenie 1) — nazwa] 질투하는 뿌리
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877311].levelList[level=1].name
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [Umiejętność wroga [877311] (ulepszenie 1) — opis] 이 스킬은 피해를 주지 않음\n[WhenUse] 자신의 [HowDareYouApple]를 전부 소모하여, 소모한만큼 코인을 재사용함 (최대 4회)\n[DefeatDuel] 이 스킬로 [Burst] 효과를 발동하지 않음
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877311].levelList[level=1].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Umiejętność wroga [877311] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877311].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Umiejętność wroga [877205] (ulepszenie 1) — nazwa] 홍염살
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877205].levelList[level=1].name
   (powtórzenie elementu 553 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Umiejętność wroga [877205] (ulepszenie 1) — opis] (이번 턴에 홍염 나방이 사용할 분노 스킬 수 x 2)만큼 합 위력 증가\n[WhenUse] 모든 적에게 (홍염 나방이 사용하는 분노 스킬 수 x 2)만큼 [Combustion] 부여\n[DefeatDuel] 아래 효과 적용\n- 이 공격 스킬이 가하는 피해는 0이 됨\n- 모든 대상의 [Combustion] 제거\n- 이 스킬의 [Combustion], [Combustion] 횟수 부여량이 절반으로 감소함
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877205].levelList[level=1].desc
   (powtórzenie elementu 554 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Umiejętność wroga [877205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Umiejętność wroga [877205] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 이번 턴에 홍염 나방이 사용할 분노 스킬 수만큼 [Combustion] 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877205].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [Umiejętność wroga [877205] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 가장 느린 적에게 이번 턴에 홍염 나방이 사용할 분노 스킬 수만큼 [Combustion] 부여, [Combustion] 횟수 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877205].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 557 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Umiejętność wroga [877205] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877205].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Umiejętność wroga [877205] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 이번 턴에 홍염 나방이 사용할 분노 스킬 수만큼 [Combustion] 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877205].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Umiejętność wroga [877205] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 가장 느린 적에게 이번 턴에 홍염 나방이 사용할 분노 스킬 수만큼 [Combustion] 부여, [Combustion] 횟수 증가
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877205].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] Against the enemy with the slowest Speed, inflict [Combustion] and [Combustion] Count equal to the number of Wrath Skills that the Ardor Blossom Moth will use this turn
   PL: [UnBrokenCoinOnSucceedAttack] wrogowi z najniższą Szybkością nakłada [Combustion] i Licznik [Combustion] równy liczbie Umiejętności Gniewu, których Ardor Blossom Moth użyje w tej turze
728. [Umiejętność wroga [877205] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877205].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Umiejętność wroga [877205] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 피해량의 70%만큼 흐트러짐 손상 입힘
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877205].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Umiejętność wroga [877205] (ulepszenie 1) — moneta 3, efekt 3 — opis] - 이 피해로 흐트러짐 상태가 된 적에게 [Combustion] 10 부여
   źródło: Skills_Abnormality-a1c9p2.json :: dataList[id=877205].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 563 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c9p2] Pasywka wroga: Passives_Abnormality-a1c9p2
- plik gry: `Passives_Abnormality-a1c9p2.json`

731. [[a1c9p2] Pasywka wroga [132203] — nazwa] 중첩된 잔상
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132203].name
   limit: do 40 znaków
   EN: Superposed Afterimage
   PL: Superposed Afterimage
732. [[a1c9p2] Pasywka wroga [132203] — opis] 스테이지 시작시, [TimeEntangleFour] 얻음\n패턴의 첫 턴 시작시 [TimeGapAb]를 ([TimeEntangleDesc] 단계 x 400)만큼 얻음\n([TimeEntangleDesc] 단계 당 1회)\n\n[TimeEntangleDesc] 3, 4단계에서 <color=#ff6000><mark=#ff000040><b><u>[TimeGapAb]를 모두 잃으면 패턴이 변경되고, 다음 턴 동안 흐트러짐</u></b></mark></color>\n\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 체력, 정신력, 흐트러짐 손상 피해량 -30%
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132203].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [TimeEntangleFour], [TimeGapAb], [TimeEntangleDesc], [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [TimeEntangleFour] = 4중 잔상 얽힘 / Fourfold Afterimage Entanglement; [TimeGapAb] = 괴리 / Disjunction; [TimeEntangleDesc] = 잔상 얽힘 / Afterimage Entanglement; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: Encounter Start: Gain [TimeEntangleFour]\nAt the start of the first turn of each pattern, gain [TimeGapAb] equal to ([TimeEntangleDesc] stage x 400) (once per [TimeEntangleDesc] stage)\n\nAt stage 3 and 4 [TimeEntangleDesc], <color=#ff6000><mark=#ff000040><b><u>if this unit loses all [TimeGapAb], the pattern changes and become Staggered for the next turn</u></b></mark></color>\n\nTake -30% HP, SP damage from [Combustion], [Laceration], [Burst], and [Sinking]; -30% to Stagger Threshold raised by [Vibration]
   PL: Początek walki: zyskuje [TimeEntangleFour]\nna Początku pierwszej tury każdego wzorca zyskuje [TimeGapAb] równy (Etap [TimeEntangleDesc] x 400) (1 raz na Etap [TimeEntangleDesc])\n\nna Etapie 3 i 4 [TimeEntangleDesc], <color=#ff6000><mark=#ff000040><b><u>jeżeli jednostka straci wszystkie [TimeGapAb], wzorzec się zmienia, a ona przechodzi w Oszołamienie na następną turę</u></b></mark></color>\n\notrzymuje o 30% mniej obrażeń HP i SP od [Combustion], [Laceration], [Burst] i [Sinking]; otrzymuje o 30% mniej wzrostu Próg Oszołomienia od [Vibration]
733. [[a1c9p2] Pasywka wroga [132204] — nazwa] 잔상 반향
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132204].name
   limit: do 40 znaków
   EN: Afterimage Reverberation
   PL: Afterimage Reverberation
734. [[a1c9p2] Pasywka wroga [132204] — opis] 자신의 코인 적중 시, (해당 코인 최종 피해량 / 10)만큼 참격 피해 (자신의 [TimeEntangleDesc] 단계만큼 발동. 이 피해로 흐트러지지 않음)
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132204].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [TimeEntangleDesc]
   znaczenie tagów: [TimeEntangleDesc] = 잔상 얽힘 / Afterimage Entanglement
   EN: On hit with this unit's Coin, deal Slash damage equal to (the Coin's final damage / 10)\n- This effect activates ([TimeEntangleDesc] stage) times; damage from this effect cannot Stagger target
   PL: przy trafieniu Monetą tej jednostki zadaje obrażenia Cięcia równe (końcowe obrażenia tej Monety / 10)\n- ten efekt uruchamia się tyle razy, ile wynosi Etap [TimeEntangleDesc]; obrażenia z tego efektu nie mogą Oszołomić celu
735. [[a1c9p2] Pasywka wroga [132204] — podsumowanie] 참격 추가 피해
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132204].summary
   limit: do 120 znaków
   EN: Deal Slash bonus damage
   PL: zadaje dodatkowe obrażenia Cięcia
736. [[a1c9p2] Pasywka wroga [132205] — nazwa] 여러 시간에서 베여오는 잔상
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132205].name
   limit: do 60 znaków
   EN: Lacerating Afterimages from Myriad Moments
   PL: Lacerating Afterimages from Myriad Moments
737. [[a1c9p2] Pasywka wroga [132205] — opis] 공격 스킬 종료시, 각 대상에게 (크리티컬로 적중한 참격 코인 개수 x 10)만큼 참격 피해 (이 피해로 흐트러지지 않음)\n\n공격 스킬 종료시, 자신이 보유한 20을 초과하는 [Breath]을 전부 소모하여 소모값만큼 대상에게 [PhantomIncision] 부여
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132205].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [PhantomIncision]
   znaczenie tagów: [Breath] = 호흡 / Poise; [PhantomIncision] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: Attack Skill End: Deal (# of Slash Coins that hit Critically x 10) Slash damage against each target) (damage from this effect cannot Stagger target)\n\nAttack Skill End: Consume every surplus [Breath] Potency past 20 on self and inflict [PhantomIncision] to target by [Breath] Potency consumed
   PL: koniec Umiejętności ataku: zadaje każdemu celowi obrażenia Cięcia równe (liczba Monet Cięcia trafiających krytycznie x 10) (obrażenia z tego efektu nie mogą Oszołomić celu)\n\nkoniec Umiejętności ataku: zużywa całą nadwyżkę Siły [Breath] ponad 20 i nakłada tyle [PhantomIncision] celowi, ile zużyto Siły [Breath]
738. [[a1c9p2] Pasywka wroga [132208] — nazwa] 지혜성도 발도
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132208].name
   limit: do 50 znaków
   EN: Unsheathing Dihui Star's Blade
   PL: Unsheathing Dihui Star's Blade
739. [[a1c9p2] Pasywka wroga [132208] — opis] 4턴마다 강력한 스킬 사용\n- 자신의 [PhantomIncisionTotal] 수치가 50 이상이면 사용하는 스킬이 강화됨
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132208].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [PhantomIncisionTotal]
   znaczenie tagów: [PhantomIncisionTotal] = 지혜성도 / Dihui Star's Blade
   EN: Use a powerful attack pattern every 4 turns\n- At 50+ [PhantomIncisionTotal], the pattern above becomes empowered
   PL: używa potężnego wzorca ataku co 4 tury\n- przy 50+ [PhantomIncisionTotal] powyższy wzorzec zostaje wzmocniony
740. [[a1c9p2] Pasywka wroga [132208] — tekst klimatyczny] ‘…지긋지긋한 낙인과도 같은 검.’
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132208].flavor
   limit: do 120 znaków
   EN: '... I'm weary of this stigma of a blade.'
   PL: '... I'm weary of this stigma of a blade.'
741. [[a1c9p2] Pasywka wroga [132216] — nazwa] ‘적당히 겨뤄주마’
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132216].name
   limit: do 50 znaków
   EN: 'I Shall Give You Some Quarter'
   PL: 'I Shall Give You Some Quarter'
742. [[a1c9p2] Pasywka wroga [132216] — opis] 수비 스킬을 사용한 대상에게 가하는 자신의 스킬 최종 피해량 -50%\n\n4턴마다 턴 종료시, 이번 전투 동안 [Vulnerable] 2, [AttackDmgUp] 2 얻음 (전투 당 최대 2회 누적)
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132216].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable], [AttackDmgUp]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Deal -50% final damage with this unit's Skill against targets that used Defense Skill\n\nTurn End: Gain 2 [Vulnerable] and 2 [AttackDmgUp] every 4 turn in this Encounter (applies cumulatively; max 2 times per Encounter)
   PL: Umiejętności tej jednostki zadają o 50% mniej końcowych obrażeń celom, które użyły Umiejętności obrony\n\nna koniec tury co 4 tury w tej walce zyskuje 2 [Vulnerable] i 2 [AttackDmgUp] (kumuluje się; maks. 2 razy na walkę)
743. [[a1c9p2] Pasywka wroga [132101] — nazwa] 살아있는 신경 - 억지력 부분해제
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132101].name
   limit: do 60 znaków
   EN: Living Nerves - Partial Deterrence Release
   PL: Living Nerves - Partial Deterrence Release
744. [[a1c9p2] Pasywka wroga [132101] — opis] 죽음을 맞이하면 해당 턴 스킬 전부 취소\n위 효과 발동 시 [SelfCharge] 10 얻음
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132101].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [SelfCharge]
   znaczenie tagów: [SelfCharge] = 자가 충전 / Self-charge
   EN: Upon death, all Skills are cancelled for the turn\nGain 10 [SelfCharge] when the effect above activates
   PL: przy śmierci wszystkie Umiejętności w tej turze zostają anulowane\nzyskuje 10 [SelfCharge], gdy ten efekt się uruchomi
745. [[a1c9p2] Pasywka wroga [132102] — nazwa] 끈질긴 생명력
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132102].name
   limit: do 40 znaków
   EN: Undying Persistence
   PL: Undying Persistence
746. [[a1c9p2] Pasywka wroga [132102] — opis] 5턴마다 머리 부위 체력만큼 보호막을 얻음
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132102].desc
   limit: do 120 znaków
   EN: Every 5 turns, gains a Shield equal to the head's HP
   PL: co 5 tur zyskuje Tarczę równą HP głowy
747. [[a1c9p2] Pasywka wroga [132103] — nazwa] 끊겨버린 생명력
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132103].name
   limit: do 40 znaków
   EN: Terminated Persistence
   PL: Terminated Persistence
748. [[a1c9p2] Pasywka wroga [132103] — opis] 똬리 틀기 사용 후 보호막을 전부 소모할 시 [SelfCharge] 전부 소모\n모든 부위가 다음 턴에 흐트러짐 상태가 됨
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132103].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [SelfCharge]
   znaczenie tagów: [SelfCharge] = 자가 충전 / Self-charge
   EN: After using 'Coil Up', if the Shield is exhausted, spend all [SelfCharge]\nAll parts become Staggered next turn
   PL: po użyciu „Coil Up”, jeżeli Tarcza została zużyta, zużywa wszystkie [SelfCharge]\nwszystkie Części przechodzą w Oszołamienie w następnej turze
749. [[a1c9p2] Pasywka wroga [132001] — nazwa] 마지막 불씨
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132001].name
   limit: do 40 znaków
   EN: The Last Ember
   PL: The Last Ember
750. [[a1c9p2] Pasywka wroga [132001] — opis] 체력이 30% 이하가 되었을 때, 얻는 [MRcAiBa] +1
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MRcAiBa]
   znaczenie tagów: [MRcAiBa] = 불씨 / Ember
   EN: At 30%- HP, gain +1 more [MRcAiBa]
   PL: przy 30% HP lub mniej, zyskuje o 1 więcej [MRcAiBa]
751. [[a1c9p2] Pasywka wroga [132002] — nazwa] 불씨 지피기
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132002].name
   (powtórzenie elementu 566 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [[a1c9p2] Pasywka wroga [132002] — opis] 날개 부위 파괴 시, 마지막 공격자에게 자신의 [MRcAiBa]만큼\n[MRcAiBb]를 부여하고, 자신의 [MRcAiBa]를 소멸함\n\n‘홍염살’을 사용할 때, [MRcAiBa]가 0개면 ‘불씨[TabExplain] 지피기’를 추가로 사용함
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132002].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [MRcAiBa], [MRcAiBb], [TabExplain]
   znaczenie tagów: [MRcAiBa] = 불씨 / Ember; [MRcAiBb] = 아른거리는 불씨 / Shimmering Ember
   EN: When the Wings Part is broken, inflict [MRcAiBb] equal to [MRcAiBa] Stack to the last attacker; then, all [MRcAiBa] on self expires.\n\nWhen using 'Ardor Blossom Star' at 0 [MRcAiBa], use 'Stoke the Flames' as well
   PL: gdy Część Skrzydeł zostaje zniszczona, nakłada ostatniemu atakującemu [MRcAiBb] równy Licznikowi [MRcAiBa], po czym wszystkie [MRcAiBa] tej jednostki wygasają.\n\nprzy użyciu „Ardor Blossom Star” z liczbą [MRcAiBa] równą 0, dodatkowo używa „Stoke the Flames”
753. [[a1c9p2] Pasywka wroga [132003] — nazwa] 타오르는 불씨
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132003].name
   limit: do 40 znaków
   EN: Flaming Ember
   PL: Flaming Ember
754. [[a1c9p2] Pasywka wroga [132003] — opis] [MRcAiBa] 수만큼 다른 속성의 스킬을 분노 속성으로 변경함
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132003].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MRcAiBa]
   znaczenie tagów: [MRcAiBa] = 불씨 / Ember
   EN: Convert a number of non-Wrath Skills equal to [MRcAiBa] Stack into Wrath Skills
   PL: przekształca liczbę Umiejętności innych Gniewu równą Licznikowi [MRcAiBa] w Umiejętności Gniewu
755. [[a1c9p2] Pasywka wroga [132004] — nazwa] 맞물리는 홍염
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132004].name
   limit: do 40 znaków
   EN: Interlocking Ardor Blossom
   PL: Interlocking Ardor Blossom
756. [[a1c9p2] Pasywka wroga [132004] — opis] 자신에게 [MRcAiBa]가 있으면, 분노 속성이 아닌 스킬이 수치만큼 분노 속성이 됨\n\n이번 턴에 홍염 나방이 사용할 분노 스킬 수만큼 스킬 적중시 [Combustion]을 부여함\n\n스킬 적중시 (이번 턴에 홍염 나방이 사용할 분노 스킬 수 x 2)만큼 체력을 회복함
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132004].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [MRcAiBa], [Combustion]
   znaczenie tagów: [MRcAiBa] = 불씨 / Ember; [Combustion] = 화상 / Burn
   EN: If this unit has [MRcAiBa], convert a number of non-Wrath Skills equal to [MRcAiBa] Stack into Wrath Skills\n\nOn Hit, inflict [Combustion] equal to (# of Wrath Skills that the Ardor Blossom Moth will use this turn)\n\nOn Hit, heal HP equal to (# of Wrath Skills that the Ardor Blossom Moth will use this turn x 2)
   PL: jeżeli ta jednostka ma [MRcAiBa], przekształca liczbę Umiejętności niebędących Gniewem równą Licznikowi [MRcAiBa] w Umiejętności Gniewu\n\nprzy trafieniu nakłada [Combustion] równy (liczba Umiejętności Gniewu, których Ardor Blossom Moth użyje w tej turze)\n\nprzy trafieniu przywraca HP równe (liczba Umiejętności Gniewu, których Ardor Blossom Moth użyje w tej turze x 2)
757. [[a1c9p2] Pasywka wroga [132005] — nazwa] 자원 보급
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132005].name
   limit: do 40 znaków
   EN: Supply Resources
   PL: Supply Resources
758. [[a1c9p2] Pasywka wroga [132005] — opis] 날개 부위 파괴 시 모든 속성의 E.G.O 자원 +2, 모든 수감자 정신력 15 회복
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132005].desc
   limit: do 130 znaków
   EN: When the Wings Part is broken, gain 2 E.G.O Resource of all Affinity and heal all Sinners' SP by 15
   PL: gdy Część Skrzydeł zostaje zniszczona, zyskuje po 2 zasobów E.G.O każdej Afinności i przywraca 15 SP wszystkim Grzesznikom
759. [[a1c9p2] Pasywka wroga [132006] — nazwa] 불타는 날개 - 억지력 부분해제
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132006].name
   limit: do 60 znaków
   EN: Flaming Wings - Partial Deterrence Release
   PL: Flaming Wings - Partial Deterrence Release
760. [[a1c9p2] Pasywka wroga [132006] — opis] [Combustion]으로 인한 피해를 받지 않음\n\n턴 종료시 자신이 보유한 [Combustion] x 5 만큼 본체 체력 회복
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132006].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Does not take [Combustion] damage\n\nTurn End: Heal Core by ([Combustion] on self x 5)
   PL: nie otrzymuje obrażeń od [Combustion]\n\nna koniec tury przywraca Korpusowi HP równe (Licznik [Combustion] jednostki x 5)
761. [[a1c9p2] Pasywka wroga [132501] — nazwa] 단말기로 전해진 지령
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132501].name
   limit: do 50 znaków
   EN: Prescript Delivered on a Device
   PL: Prescript Delivered on a Device
762. [[a1c9p2] Pasywka wroga [132501] — opis] 스테이지 시작 시, 최대 체력의 20%만큼 보호막 얻음 (이번 전투 동안 유지)\n\n턴 시작 시\n- [UnlockBuff_Base] 단계에 따라 [IndexPrescript_Base_2nd] 얻음\n- <color=#ff6000><mark=#ff000040><b><u>무작위 적에게 [IndexPrescriptTargetToPersonality]을 부여하고, 우선 공격함</u></b></mark></color> (특정 패턴 제외)\n\n[BlessingOfIndexPrescriptEnemy]당 [IndexPrescriptTargetToPersonality]에게 가하는 피해량 +2.5% (최대 20%)\n- [BlessingOfIndexPrescriptEnemy]가 9면, 대신 모든 대상에게 가하는 피해량 +30%
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132501].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [UnlockBuff_Base], [IndexPrescript_Base_2nd], [IndexPrescriptTargetToPersonality], [BlessingOfIndexPrescriptEnemy]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [IndexPrescript_Base_2nd] = 지령 / Prescript; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript
   EN: Encounter Start: Gain Shield equal to 20% of max HP (remains throughout this Encounter)\n\nTurn Start:\n- Gain [IndexPrescript_Base_2nd] based on [UnlockBuff_Base] stage on self\n- <color=#ff6000><mark=#ff000040><b><u>Inflict [IndexPrescriptTargetToPersonality] to a random enemy and prioritize attacking that enemy</u></b></mark></color> (excluding certain pattern)\n\nDeal +2.5% damage to [IndexPrescriptTargetToPersonality] for every [BlessingOfIndexPrescriptEnemy] (max 20%)\n- At 9 [BlessingOfIndexPrescriptEnemy], deal +30% damage to all targets instead
   PL: Początek walki: zyskuje Tarczę równą 20% Maks. HP (utrzymuje się przez tę walkę)\n\nna Początku tury:\n- zyskuje [IndexPrescript_Base_2nd] zależnie od Etapu [UnlockBuff_Base] jednostki\n- <color=#ff6000><mark=#ff000040><b><u>nakłada [IndexPrescriptTargetToPersonality] losowemu wrogowi i priorytet: atakowanie tego wroga</u></b></mark></color> (poza określonym wzorcem)\n\nzadaje +2.5% obrażeń [IndexPrescriptTargetToPersonality] za każdy [BlessingOfIndexPrescriptEnemy] (maks. 20%)\n- przy 9 [BlessingOfIndexPrescriptEnemy], zamiast tego zadaje +30% obrażeń wszystkim celom
763. [[a1c9p2] Pasywka wroga [132502] — nazwa] 지령의 뜻
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132502].name
   limit: do 40 znaków
   EN: Will of the Prescript
   PL: Will of the Prescript
764. [[a1c9p2] Pasywka wroga [132502] — opis] 이번 턴에 <color=#ff6000><mark=#ff000040><b><u>[IndexPrescript_Base_2nd]을 수행했으면,</u></b></mark></color>\n턴 종료 시 정신력 15 회복, ([UnlockBuff_Base] 단계+1)만큼 [BlessingOfIndexPrescriptEnemy] 얻음(턴당 1회)\n\n이번 턴에 <color=#ff6000><mark=#ff000040><b><u>[IndexPrescript_Base_2nd]을 수행하지 못했으면,</u></b></mark></color>\n턴 종료 시 [PressureOfPrescript] 1, [KarmaOfIndexStudent] 5 얻음\n- [UnlockBuff_Base]이 없으면, 턴 종료 시 [BlessingOfIndexPrescriptEnemy] 1 얻음\n- [BlessingOfIndexPrescriptEnemy]가 9면, [KarmaOfIndexStudent]를 얻지 않음\n- 개화[TabExplain] E.G.O::대행 상태면, 얻는 [KarmaOfIndexStudent] 2배 증가
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132502].desc
   limit: do 750 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [IndexPrescript_Base_2nd], [UnlockBuff_Base], [BlessingOfIndexPrescriptEnemy], [PressureOfPrescript], [KarmaOfIndexStudent], [TabExplain]
   znaczenie tagów: [IndexPrescript_Base_2nd] = 지령 / Prescript; [UnlockBuff_Base] = 해금 / Unlock; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [PressureOfPrescript] = 압박감 / Onus; [KarmaOfIndexStudent] = 카르마 / Karmic Consequence
   EN: Turn End: <color=#ff6000><mark=#ff000040><b><u>If [IndexPrescript_Base_2nd] was executed this turn,</u></b></mark></color> heal 15 SP and gain [BlessingOfIndexPrescriptEnemy] by ([UnlockBuff_Base] stage + 1) (once per turn)\n\nTurn End: <color=#ff6000><mark=#ff000040><b><u>If [IndexPrescript_Base_2nd] was not executed this turn</u></b></mark></color>, gain 1 [PressureOfPrescript] and 5 [KarmaOfIndexStudent]\n- If this unit does not have [UnlockBuff_Base], gain 1 [BlessingOfIndexPrescriptEnemy] at Turn End\n- At 9 [BlessingOfIndexPrescriptEnemy], does not gain [KarmaOfIndexStudent]\n- If this unit is under the effect of Effloresced[TabExplain] E.G.O::Procuration, double [KarmaOfIndexStudent] this unit will gain
   PL: na koniec tury: <color=#ff6000><mark=#ff000040><b><u>jeżeli w tej turze wykonano [IndexPrescript_Base_2nd]</u></b></mark></color>, przywraca 15 SP i zyskuje (Etap [UnlockBuff_Base] + 1) [BlessingOfIndexPrescriptEnemy] (1 raz na turę)\n\nna koniec tury: <color=#ff6000><mark=#ff000040><b><u>jeżeli w tej turze nie wykonano [IndexPrescript_Base_2nd]</u></b></mark></color>, zyskuje 1 [PressureOfPrescript] i 5 [KarmaOfIndexStudent]\n- jeżeli jednostka nie ma [UnlockBuff_Base], na koniec tury zyskuje 1 [BlessingOfIndexPrescriptEnemy]\n- przy 9 [BlessingOfIndexPrescriptEnemy] nie zyskuje [KarmaOfIndexStudent]\n- jeżeli ta jednostka jest w stanie Effloresced[TabExplain] E.G.O::Procuration, zyskiwane [KarmaOfIndexStudent] jest podwójne
765. [[a1c9p2] Pasywka wroga [132503] — nazwa] 해금
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132503].name
   limit: do 40 znaków
   EN: Unlock
   PL: Unlock
766. [[a1c9p2] Pasywka wroga [132503] — opis] 턴 종료 시 [BlessingOfIndexPrescriptEnemy]가 3/6/9거나 체력이 90%/75%/60% 이하면,\n- [UnlockBuff_1]/[UnlockBuff_2]/[UnlockBuff_3] 얻음\n- 정신력이 45로 증가\n- <color=#ff6000><mark=#ff000040><b><u>보유한 [PressureOfPrescript] 전부 소모</u></b></mark></color>, 흐트러짐 해제\n- 처음으로 [UnlockBuff_Base] 획득한 다음 턴에 [BlessingOfIndexPrescriptEnemy] 1 얻음\n\n체력 조건으로 [UnlockBuff_Base] 획득 시\n- (증가한 정신력/15)만큼 [KarmaOfIndexStudent] 얻음\n- [BlessingOfIndexPrescriptEnemy]가 3/6/9 미만이면, 3/6/9로 변경,\n증가한 수치 1당 다음 턴 시작 시 [DefenseDown] 1, [KarmaOfIndexStudent] 2 얻음\n\n강력한 공격을 사용하는 턴의 속도 최솟값, 최댓값 +10
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132503].desc
   limit: do 920 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BlessingOfIndexPrescriptEnemy], [UnlockBuff_1], [UnlockBuff_2], [UnlockBuff_3], [PressureOfPrescript], [UnlockBuff_Base], [KarmaOfIndexStudent], [DefenseDown]
   znaczenie tagów: [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [UnlockBuff_1] = 해금 - I / Unlock - I; [UnlockBuff_2] = 해금 - II / Unlock - II; [UnlockBuff_3] = 해금 - III / Unlock - III; [PressureOfPrescript] = 압박감 / Onus; [UnlockBuff_Base] = 해금 / Unlock; [KarmaOfIndexStudent] = 카르마 / Karmic Consequence; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn End: At 3/6/9 [BlessingOfIndexPrescriptEnemy] or at 90%-/75%-/60%- HP,\n- Gain [UnlockBuff_1]/[UnlockBuff_2]/[UnlockBuff_3]\n- Heal to 45 SP\n- <color=#ff6000><mark=#ff000040><b><u>Consume all [PressureOfPrescript]</u></b></mark></color> and recover from Stagger\n- Gain 1 [BlessingOfIndexPrescriptEnemy] in the turn after [UnlockBuff_Base] was gained for the first time\n\nIf [UnlockBuff_Base] was gained based on HP conditional above,\n- Gain [KarmaOfIndexStudent] by (sum of healed SP / 15)\n- Increase [BlessingOfIndexPrescriptEnemy] to 3/6/9 if this unit had less than 3/6/9 [BlessingOfIndexPrescriptEnemy]; gain 1 [DefenseDown] and 2 [KarmaOfIndexStudent] next turn for every [BlessingOfIndexPrescriptEnemy] Stack gained\n\nMin & Max Speed +10 in the turn this unit uses its powerful attack
   PL: na koniec tury, przy 3/6/9 [BlessingOfIndexPrescriptEnemy] albo przy HP równym 90%/75%/60% lub mniej:\n- zyskuje [UnlockBuff_1]/[UnlockBuff_2]/[UnlockBuff_3]\n- przywraca SP do 45\n- <color=#ff6000><mark=#ff000040><b><u>zużywa wszystkie [PressureOfPrescript]</u></b></mark></color> i dochodzi do siebie z Oszołamienia\n- w turze po pierwszym uzyskaniu [UnlockBuff_Base] zyskuje 1 [BlessingOfIndexPrescriptEnemy]\n\njeżeli [UnlockBuff_Base] zostało uzyskane dzięki warunkowi HP opisanemu powyżej:\n- zyskuje (przywrócone SP / 15) [KarmaOfIndexStudent]\n- jeżeli jednostka miała mniej niż 3/6/9 [BlessingOfIndexPrescriptEnemy], zwiększa [BlessingOfIndexPrescriptEnemy] do 3/6/9; za każdy zyskany Licznik [BlessingOfIndexPrescriptEnemy] zyskuje 1 [DefenseDown] i 2 [KarmaOfIndexStudent] w następnej turze\n\nMin. i Maks. Szybkość +10 w turze użycia potężnego ataku
767. [[a1c9p2] Pasywka wroga [132503] — tekst klimatyczny] “지령이 전해주는 검과 천은 지령이 수행될 때 비로소 그 힘이 해금되며 발현된다고 하더군.”
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132503].flavor
   limit: do 160 znaków
   EN: "It is said that the blade and fabric granted by the Prescript unlock their power only when the Prescript is executed."
   PL: \u201eMówi się, że ostrze i tkanina ofiarowane przez Prescript uwalniają swoją moc dopiero wtedy, gdy Prescript zostaje wykonany.\u201d
768. [[a1c9p2] Pasywka wroga [132504] — nazwa] 개화 E.G.O::대행
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132504].name
   limit: do 50 znaków
   EN: Effloresced E.G.O::Procuration
   PL: Effloresced E.G.O::Procuration
769. [[a1c9p2] Pasywka wroga [132504] — opis] 턴 시작 시 [UnlockBuff_Base]이 있고, 정신력이 25 이상이면,\n정신력을 15 소모하여 개화[TabExplain] E.G.O::대행 상태가 되고, 흐트러짐 해제\n- 해당 상태 동안 내성 변경, [Blandishment_Enemy] 얻음\n- 턴 시작 시 정신력이 0 이하면, 개화[TabExplain] E.G.O::대행 상태 해제
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132504].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_Base], [TabExplain], [Blandishment_Enemy]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [Blandishment_Enemy] = 당연한 믿음 / Faith Beyond Question
   EN: Turn Start: if this unit has [UnlockBuff_Base] and is at 25+ SP, consume 15 SP to enter Effloresced[TabExplain] E.G.O::Procuration state and recover from Stagger\n- Gain [Blandishment_Enemy] and a different set of Resistance values while in this state\n- Turn Start: at 0 or less SP, exit Effloresced[TabExplain] E.G.O::Procuration state
   PL: na Początku tury, jeżeli ta jednostka ma [UnlockBuff_Base] i SP równe 25 lub więcej, zużywa 15 SP, by wejść w stan Effloresced[TabExplain] E.G.O::Procuration, i dochodzi do siebie z Oszołamienia\n- w tym stanie zyskuje [Blandishment_Enemy] i inny zestaw wartości Odporności\n- na Początku tury przy SP równym 0 lub mniej wychodzi ze stanu Effloresced[TabExplain] E.G.O::Procuration
770. [[a1c9p2] Pasywka wroga [132505] — nazwa] 말살 태세
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132505].name
   limit: do 40 znaków
   EN: Annihilation Form
   PL: Annihilation Form
771. [[a1c9p2] Pasywka wroga [132505] — opis] 전장에 베스파 등장 시,\n- 특정 턴이 되어 등장 시 [UnlockBuff_Base] 단계가 2 미만이면, [UnlockBuff_3] 얻고, 정신력을 45까지 회복, 흐트러짐 해제\n- [Blandishment_Shin_Enemy], 최대 체력의 50%만큼 보호막 얻음 (이번 전투 동안 유지)\n- '해금[TabExplain]' 패시브의 [PressureOfPrescript] 소모 효과 비활성화\n- [PressureOfPrescript]이 [PressureOfPrescript_2nd]으로 변경되고, 최대로 증가\n- 턴 시작 시 [PressureOfPrescript_2nd] 1 얻음\n- 이후 정신력이 0 미만으로 감소하지 않음\n\n체력이 20% 이하가 될 때, [PressureOfPrescript_2nd]이 최대로 증가
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132505].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_Base], [UnlockBuff_3], [Blandishment_Shin_Enemy], [TabExplain], [PressureOfPrescript], [PressureOfPrescript_2nd]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [UnlockBuff_3] = 해금 - III / Unlock - III; [Blandishment_Shin_Enemy] = 신(心) - 소라 / Shin (心) - Sora; [PressureOfPrescript] = 압박감 / Onus; [PressureOfPrescript_2nd] = 극심한 압박감 / Extreme Onus
   EN: When Vespa enters the battlefield:\n- If [UnlockBuff_Base] is below stage II, gain [UnlockBuff_3], heal SP to 45, and recover from Stagger\n- Gain 1 [Blandishment_Shin_Enemy] and gain Shield equal to 50% of max HP (lasts for the rest of this Encounter)\n- Disable the [PressureOfPrescript] cost of activating the 'Unlock[TabExplain]' Passive\n- Intensify [PressureOfPrescript] to [PressureOfPrescript_2nd] and max out its Stack\n- Turn Start: Gain 1 [PressureOfPrescript_2nd]\n- Then, this unit's SP does not drop below 0\n\nAt 20% or less HP, max out [PressureOfPrescript_2nd] Stack
   PL: gdy Vespa pojawia się na polu bitwy:\n- jeżeli pojawia się w określonej turze z [UnlockBuff_Base] poniżej Etapu II, zyskuje [UnlockBuff_3], przywraca SP do 45 i dochodzi do siebie z Oszołamienia\n- zyskuje 1 [Blandishment_Shin_Enemy] i Tarczę równą 50% Maks. HP (utrzymuje się przez tę walkę)\n- wyłącza koszt [PressureOfPrescript] aktywacji Pasywu „Unlock[TabExplain]”\n- [PressureOfPrescript] zmienia się w [PressureOfPrescript_2nd] i osiąga maksimum\n- na Początku tury zyskuje 1 [PressureOfPrescript_2nd]\n- od tej pory SP tej jednostki nie spada poniżej 0\n\nprzy HP równym 20% lub mniej, [PressureOfPrescript_2nd] osiąga maksimum
772. [[a1c9p2] Pasywka wroga [132505] — tekst klimatyczny] ‘위, 위험한 사람... 지령이 수행되지 모, 못할 수도 있겠어요.’
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132505].flavor
   limit: do 120 znaków
   EN: 'W-what a dangerous person... The Prescript could go unfulfilled at this rate.'
   PL: 'W-w niebezpieczna to osoba... Pr-escript może nie zostać wykonany, j-jeśli tak dalej pójdzie.'
773. [[a1c9p2] Pasywka wroga [132230] — nazwa] 패닉 회복
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132230].name
   limit: do 40 znaków
   EN: Panic Recovery
   PL: Panic Recovery
774. [[a1c9p2] Pasywka wroga [132230] — opis] 턴 종료 시 패닉 상태라면 정신력이 30이 됨.
   źródło: Passives_Abnormality-a1c9p2.json :: dataList[id=132230].desc
   limit: do 120 znaków
   EN: Turn End: if in Panic, reset SP to 30.
   PL: Koniec tury: jeżeli jest w Panice, SP wraca do 30.

## [a1c9p3] Wróg / część: Enemies-a1c9p3
- plik gry: `Enemies-a1c9p3.json`

775. [[a1c9p3] Wróg / część [1314] — nazwa] 엄지 아비 - 발렌치나
   źródło: Enemies-a1c9p3.json :: dataList[id=1314].name
   limit: do 50 znaków
   EN: The Thumb Nursefather - Valencina
   PL: The Thumb Nursefather - Valencina
776. [[a1c9p3] Wróg / część [1314] — opis] 엄지 아비
   źródło: Enemies-a1c9p3.json :: dataList[id=1314].desc
   limit: do 120 znaków
   EN: The Thumb Nursefather
   PL: The Thumb Nursefather
777. [[a1c9p3] Wróg / część [131401] — nazwa] 몸통
   źródło: Enemies-a1c9p3.json :: dataList[id=131401].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [[a1c9p3] Wróg / część [131401] — opis] 부위
   źródło: Enemies-a1c9p3.json :: dataList[id=131401].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [[a1c9p3] Wróg / część [1327] — nazwa] 중지 아비 - 마티아스
   źródło: Enemies-a1c9p3.json :: dataList[id=1327].name
   limit: do 50 znaków
   EN: The Middle Nursefather - Matthias
   PL: The Middle Nursefather - Matthias
780. [[a1c9p3] Wróg / część [1327] — opis] 중지 아비
   źródło: Enemies-a1c9p3.json :: dataList[id=1327].desc
   limit: do 120 znaków
   EN: The Middle Nursefather
   PL: The Middle Nursefather
781. [[a1c9p3] Wróg / część [132701] — nazwa] 몸통
   źródło: Enemies-a1c9p3.json :: dataList[id=132701].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [[a1c9p3] Wróg / część [132701] — opis] 중지 아비 부위
   źródło: Enemies-a1c9p3.json :: dataList[id=132701].desc
   limit: do 120 znaków
   EN: The Middle Nursefather Part
   PL: The Middle Nursefather Part
783. [[a1c9p3] Wróg / część [1328] — nazwa] 중지 제자 - 키라
   źródło: Enemies-a1c9p3.json :: dataList[id=1328].name
   limit: do 40 znaków
   EN: The Middle Apprentice - Kira
   PL: The Middle Apprentice - Kira
784. [[a1c9p3] Wróg / część [1328] — opis] 중지 제자
   źródło: Enemies-a1c9p3.json :: dataList[id=1328].desc
   limit: do 120 znaków
   EN: The Middle Apprentice
   PL: The Middle Apprentice
785. [[a1c9p3] Wróg / część [132801] — nazwa] 몸통
   źródło: Enemies-a1c9p3.json :: dataList[id=132801].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [[a1c9p3] Wróg / część [132801] — opis] 중지 제자 부위
   źródło: Enemies-a1c9p3.json :: dataList[id=132801].desc
   limit: do 120 znaków
   EN: The Middle Apprentice Part
   PL: The Middle Apprentice Part
787. [[a1c9p3] Wróg / część [1347] — nazwa] 검지 아비 - 뤼엔
   źródło: Enemies-a1c9p3.json :: dataList[id=1347].name
   limit: do 40 znaków
   EN: The Index Nursefather - Rien
   PL: The Index Nursefather - Rien
788. [[a1c9p3] Wróg / część [1347] — opis] 검지 아비
   źródło: Enemies-a1c9p3.json :: dataList[id=1347].desc
   limit: do 120 znaków
   EN: The Index Nursefather
   PL: The Index Nursefather
789. [[a1c9p3] Wróg / część [134701] — nazwa] 몸통
   źródło: Enemies-a1c9p3.json :: dataList[id=134701].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [[a1c9p3] Wróg / część [134701] — opis] 부위
   źródło: Enemies-a1c9p3.json :: dataList[id=134701].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [[a1c9p3] Wróg / część [1348] — nazwa] 검지 아비 - 뤼엔
   źródło: Enemies-a1c9p3.json :: dataList[id=1348].name
   (powtórzenie elementu 787 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [[a1c9p3] Wróg / część [1348] — opis] 검지 아비
   źródło: Enemies-a1c9p3.json :: dataList[id=1348].desc
   (powtórzenie elementu 788 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [[a1c9p3] Wróg / część [134801] — nazwa] 몸통
   źródło: Enemies-a1c9p3.json :: dataList[id=134801].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [[a1c9p3] Wróg / część [134801] — opis] 부위
   źródło: Enemies-a1c9p3.json :: dataList[id=134801].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [[a1c9p3] Wróg / część [1331] — nazwa] 약지 아비 - 칼리스토
   źródło: Enemies-a1c9p3.json :: dataList[id=1331].name
   limit: do 50 znaków
   EN: The Ring Nursefather - Callisto
   PL: The Ring Nursefather - Callisto
796. [[a1c9p3] Wróg / część [1331] — opis] 약지 아비
   źródło: Enemies-a1c9p3.json :: dataList[id=1331].desc
   limit: do 120 znaków
   EN: The Ring Nursefather
   PL: The Ring Nursefather
797. [[a1c9p3] Wróg / część [133101] — nazwa] 몸통
   źródło: Enemies-a1c9p3.json :: dataList[id=133101].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [[a1c9p3] Wróg / część [133101] — opis] 부위
   źródło: Enemies-a1c9p3.json :: dataList[id=133101].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [[a1c9p3] Wróg / część [1332] — nazwa] 신체관극
   źródło: Enemies-a1c9p3.json :: dataList[id=1332].name
   limit: do 40 znaków
   EN: Corpus Theater
   PL: Corpus Theater
800. [[a1c9p3] Wróg / część [1332] — opis] 약지 아비 스킬로 생성되는 유닛
   źródło: Enemies-a1c9p3.json :: dataList[id=1332].desc
   limit: do 120 znaków
   EN: Unit spawned by The Ring Nursefather's Skill
   PL: jednostka tworzona przez Umiejętność The Ring Nursefather
801. [[a1c9p3] Wróg / część [133201] — nazwa] 몸통
   źródło: Enemies-a1c9p3.json :: dataList[id=133201].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [[a1c9p3] Wróg / część [133201] — opis] 부위
   źródło: Enemies-a1c9p3.json :: dataList[id=133201].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [[a1c9p3] Wróg / część [1339] — nazwa] 바퀴 황제
   źródło: Enemies-a1c9p3.json :: dataList[id=1339].name
   limit: do 40 znaków
   EN: The Roach Emperor
   PL: The Roach Emperor
804. [[a1c9p3] Wróg / część [1339] — opis] G사의 무기
   źródło: Enemies-a1c9p3.json :: dataList[id=1339].desc
   limit: do 120 znaków
   EN: G Corp. Weapon
   PL: broń G Corp.
805. [[a1c9p3] Wróg / część [133901] — nazwa] 몸통
   źródło: Enemies-a1c9p3.json :: dataList[id=133901].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [[a1c9p3] Wróg / część [133901] — opis] 부위
   źródło: Enemies-a1c9p3.json :: dataList[id=133901].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [[a1c9p3] Wróg / część [1323] — nazwa] 소지 아비 - 시오미 요루
   źródło: Enemies-a1c9p3.json :: dataList[id=1323].name
   (powtórzenie elementu 531 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [[a1c9p3] Wróg / część [1323] — opis] 소지 아비
   źródło: Enemies-a1c9p3.json :: dataList[id=1323].desc
   limit: do 120 znaków
   EN: The Pinky Nursefather
   PL: The Pinky Nursefather
809. [[a1c9p3] Wróg / część [1324] — nazwa] 소지 아비 - ???
   źródło: Enemies-a1c9p3.json :: dataList[id=1324].name
   limit: do 40 znaków
   EN: The Pinky Nursefather - ???
   PL: The Pinky Nursefather - ???
810. [[a1c9p3] Wróg / część [1324] — opis] 소지 아비
   źródło: Enemies-a1c9p3.json :: dataList[id=1324].desc
   (powtórzenie elementu 808 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [[a1c9p3] Wróg / część [1343] — nazwa] 료슈
   źródło: Enemies-a1c9p3.json :: dataList[id=1343].name
   limit: do 40 znaków
   EN: Ryōshū
   PL: Ryōshū
812. [[a1c9p3] Wróg / część [1343] — opis] 료슈
   źródło: Enemies-a1c9p3.json :: dataList[id=1343].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [[a1c9p3] Wróg / część [134301] — nazwa] 몸통
   źródło: Enemies-a1c9p3.json :: dataList[id=134301].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [[a1c9p3] Wróg / część [134301] — opis] 부위
   źródło: Enemies-a1c9p3.json :: dataList[id=134301].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [[a1c9p3] Wróg / część [1337] — nazwa] 검지 제자 - 소라
   źródło: Enemies-a1c9p3.json :: dataList[id=1337].name
   (powtórzenie elementu 528 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [[a1c9p3] Wróg / część [1337] — opis] 료슈
   źródło: Enemies-a1c9p3.json :: dataList[id=1337].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [[a1c9p3] Wróg / część [133701] — nazwa] 몸통
   źródło: Enemies-a1c9p3.json :: dataList[id=133701].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [[a1c9p3] Wróg / część [133701] — opis] 부위
   źródło: Enemies-a1c9p3.json :: dataList[id=133701].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [[a1c9p3] Wróg / część [1338] — nazwa] 소지 제자 - 렌
   źródło: Enemies-a1c9p3.json :: dataList[id=1338].name
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [[a1c9p3] Wróg / część [1338] — opis] 료슈
   źródło: Enemies-a1c9p3.json :: dataList[id=1338].desc
   (powtórzenie elementu 811 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
821. [[a1c9p3] Wróg / część [133801] — nazwa] 몸통
   źródło: Enemies-a1c9p3.json :: dataList[id=133801].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
822. [[a1c9p3] Wróg / część [133801] — opis] 부위
   źródło: Enemies-a1c9p3.json :: dataList[id=133801].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [[a1c9p3] Wróg / część [1378] — nazwa] 뒤틀린 호엔하임
   źródło: Enemies-a1c9p3.json :: dataList[id=1378].name
   limit: do 40 znaków
   EN: Distorted Hohenheim
   PL: Distorted Hohenheim
824. [[a1c9p3] Wróg / część [1378] — opis] 본체
   źródło: Enemies-a1c9p3.json :: dataList[id=1378].desc
   limit: do 120 znaków
   EN: Core
   PL: Korpus
825. [[a1c9p3] Wróg / część [137801] — nazwa] 몸통
   źródło: Enemies-a1c9p3.json :: dataList[id=137801].name
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [[a1c9p3] Wróg / część [137801] — opis] 부위
   źródło: Enemies-a1c9p3.json :: dataList[id=137801].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c9p3] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c9p3
- grupa rozdziału/trybu: `a1c9p3` · plik: `Skills_Abnormality-a1c9p3.json`

827. [Umiejętność wroga [131401] (ulepszenie 1) — nazwa] 콜피 디 탈리오
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131401].levelList[level=1].name
   limit: do 40 znaków
   EN: Colpi di Taglio
   PL: Colpi di Taglio
828. [Umiejętność wroga [131401] (ulepszenie 1) — opis] 자신의 [Breath]이 6 이상이면, 코인 위력 + 1\n대상의 [Vibration]이 6 이상이면, 합 위력 + 1
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Vibration]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor
   EN: At 6+ [Breath], Coin Power +1\nIf target has 6+ [Vibration], Clash Power +1
   PL: przy 6+ [Breath], Moc Monety +1\njeżeli cel ma 6+ [Vibration], Moc Starcia +1
829. [Umiejętność wroga [131401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [Umiejętność wroga [131401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Umiejętność wroga [131401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL: [OnSucceedAttack] nakłada 2 [Combustion]
832. [Umiejętność wroga [131401] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131401].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Umiejętność wroga [131401] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상의 [Combustion] 위력만큼 분노 속성 피해를 줌.
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131401].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict Wrath damage equal to [Combustion] on target
   PL: [OnSucceedAttack] zadaje obrażenia Gniewu równe [Combustion] celu.
834. [Umiejętność wroga [131402] (ulepszenie 1) — nazwa] 코포 디 푼토
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131402].levelList[level=1].name
   limit: do 40 znaków
   EN: Colpo di Punta
   PL: Colpo di Punta
835. [Umiejętność wroga [131402] (ulepszenie 1) — opis] 자신의 [Breath]이 6 이상이면, 코인 위력 + 1\n[WhenUse] 대상의 [Combustion]과 [Vibration]의 합 4당, 기본 위력 + 1 (최대 2)\n[WhenUse] [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131402].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [WhenUse], [Combustion], [Vibration]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: At 6+ [Breath], Coin Power +1\n[WhenUse] Base Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 2)\n[WhenUse] Gain +2 [Breath] Count
   PL: przy 6+ [Breath], Moc Monety +1\n[WhenUse] Moc Bazowa +1 za każde 4 łącznie ([Combustion] + [Vibration]) celu (maks. 2)\n[WhenUse] zyskuje 2 Licznika [Breath]
836. [Umiejętność wroga [131402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [AccelBullet] 소모
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AccelBullet]
   znaczenie tagów: [AccelBullet] = 가속탄 / Acceleration Round
   EN: Spend [AccelBullet]
   PL: zużywa [AccelBullet]
837. [Umiejętność wroga [131402] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Umiejętność wroga [131402] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131402].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Umiejętność wroga [131402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [AccelBullet] 소모
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 836 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Umiejętność wroga [131402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [Umiejętność wroga [131402] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131402].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
842. [Umiejętność wroga [131403] (ulepszenie 1) — nazwa] 세치오나투라 디 코닐리오
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131403].levelList[level=1].name
   limit: do 40 znaków
   EN: Sezionatura di Coniglio
   PL: Sezionatura di Coniglio
843. [Umiejętność wroga [131403] (ulepszenie 1) — opis] 자신의 [Breath]이 6 이상이면, 코인 위력 + 1\n[WhenUse] 대상의 [Combustion]과 [Vibration]의 합 4당, 기본 위력 + 1 (최대 2)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131403].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [WhenUse], [Combustion], [Vibration]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: At 6+ [Breath], Coin Power +1\n[WhenUse] Base Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 2)
   PL: przy 6+ [Breath], Moc Monety +1\n[WhenUse] Moc Bazowa +1 za każde 4 łącznie ([Combustion] + [Vibration]) celu (maks. 2)
844. [Umiejętność wroga [131403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여, [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion] and +3 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 3 [Combustion] i 3 Licznika [Combustion]
845. [Umiejętność wroga [131403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여, [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and +3 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 3 [Vibration] i 3 Licznika [Vibration]
846. [Umiejętność wroga [131403] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131403].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]
   PL: [OnSucceedAttack] uruchamia [Switch_Vibration], przekształcając je w [VibrationIgnition]
847. [Umiejętność wroga [131403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion] 위력만큼 분노 속성 피해를 줌.
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 833 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Umiejętność wroga [131403] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131403].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Umiejętność wroga [131404] (ulepszenie 1) — nazwa] 세치오나투라 디 체르보
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131404].levelList[level=1].name
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
850. [Umiejętność wroga [131404] (ulepszenie 1) — opis] 자신의 [Breath]이 6 이상이면, 코인 위력 + 1\n대상의 [Combustion]과 [Vibration]의 합 4당, 코인 위력 + 1 (최대 2)\n[WhenUse] 정신력이 0 이상이면, 망(望) 하나를 생성함\n- 기본 위력 + 4\n[WhenUse] [Breath] 횟수 3 증가\n[WinDuel] [Breath] 5 얻음\n[EndSkill] 망을 생성했으면, 정신력 10만큼 소모
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131404].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Combustion], [Vibration], [WhenUse], [WinDuel], [EndSkill]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: At 6+ [Breath], Coin Power +1\nCoin Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 2)\n[WhenUse] At 0+ SP, generate 1 Mang (望)\n- Base Power +4\n[WhenUse] Gain +3 [Breath] Count\n[WinDuel] Gain 5 [Breath]\n[EndSkill] If this Skill generated Mang, lose 10 SP
   PL: przy 6+ [Breath], Moc Monety +1\nMoc Monety +1 za każde 4 łącznie ([Combustion] + [Vibration]) celu (maks. 2)\n[WhenUse] przy SP równym 0 lub więcej tworzy 1 Mang (望)\n- Moc Bazowa +4\n[WhenUse] zyskuje 3 Licznika [Breath]\n[WinDuel] zyskuje 5 [Breath]\n[EndSkill] jeżeli ta Umiejętność utworzyła Mang, traci 10 SP
851. [Umiejętność wroga [131404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]
   PL: [OnSucceedAttack] nakłada 3 [Combustion]
852. [Umiejętność wroga [131404] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131404].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Umiejętność wroga [131404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여, [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 845 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [Umiejętność wroga [131404] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131404].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Umiejętność wroga [131404] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131404].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] twice; then, reduce target's [Vibration] Count by 2
   PL: [OnSucceedAttack] uruchamia [VibrationExplosion] 2 razy; następnie zmniejsza Licznik [Vibration] celu o 2
856. [Umiejętność wroga [131404] (ulepszenie 1) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] [VibrationExplosion] 1회. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131404].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Umiejętność wroga [131405] (ulepszenie 1) — nazwa] 기꺼이 이 탄환으로 꿰뚫어주지
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131405].levelList[level=1].name
   limit: do 50 znaków
   EN: I'll Gladly Blast a Hole Through You
   PL: I'll Gladly Blast a Hole Through You
858. [Umiejętność wroga [131405] (ulepszenie 1) — opis] 자신의 [Breath]이 6 이상이면, 코인 위력 + 1\n대상의 [Combustion]과 [Vibration]의 합 4당, 코인 위력 + 1 (최대 2)\n[WhenUse] [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131405].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Combustion], [Vibration], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [WhenUse] = [사용시] / [On Use]
   EN: At 6+ [Breath], Coin Power +1\nCoin Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 2)\n[WhenUse] Gain +3 [Breath] Count
   PL: przy 6+ [Breath], Moc Monety +1\nMoc Monety +1 za każde 4 łącznie ([Combustion] + [Vibration]) celu (maks. 2)\n[WhenUse] zyskuje 3 Licznika [Breath]
859. [Umiejętność wroga [131405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [AccelBullet] 소모
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 836 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [Umiejętność wroga [131405] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131405].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Umiejętność wroga [131405] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131405].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
862. [Umiejętność wroga [131405] (ulepszenie 1) — moneta 2, efekt 1 — opis] [AccelBullet] 소모
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131405].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 836 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Umiejętność wroga [131405] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131405].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
864. [Umiejętność wroga [131405] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131405].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Umiejętność wroga [131405] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion] 위력만큼 분노 속성 피해를 줌.
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131405].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 833 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
866. [Umiejętność wroga [131405] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131405].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
867. [Umiejętność wroga [131405] (ulepszenie 1) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131405].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [CriticalOnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [CriticalOnSucceedAttack] uruchamia [VibrationExplosion]; następnie zmniejsza Licznik [Vibration] celu o 1
868. [Umiejętność wroga [131406] (ulepszenie 1) — nazwa] 세치오나투라 디 엘레판테
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].name
   limit: do 40 znaków
   EN: Sezionatura di Elefante
   PL: Sezionatura di Elefante
869. [Umiejętność wroga [131406] (ulepszenie 1) — opis] 자신의 [Breath]이 6 이상이면, 코인 위력 + 1\n대상의 [Combustion]과 [Vibration]의 합 4당, 코인 위력 + 1 (최대 2)\n[WhenUse] [Breath] 횟수 3 증가\n[DefeatDuel] 최종 피해량이 50%만큼 감소하고, 크리티컬이 발동하지 않음.\n이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Combustion], [Vibration], [WhenUse], [DefeatDuel]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: At 6+ [Breath], Coin Power +1\nCoin Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 2)\n[WhenUse] Gain +3 [Breath] Count\n[DefeatDuel] Deal -50% final damage and does not hit Critically.\nDamage dealt by this Skill cannot Stagger the target
   PL: przy 6+ [Breath], Moc Monety +1\nMoc Monety +1 za każde 4 łącznie ([Combustion] + [Vibration]) celu (maks. 2)\n[WhenUse] zyskuje 3 Licznika [Breath]\n[DefeatDuel] zadaje o 50% mniej końcowych obrażeń i nie zadaje trafienia krytycznego.\nobrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
870. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 1, efekt 2 — opis] [AccelBullet] 소모
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 836 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
872. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 4 [Combustion]
   PL: [OnSucceedAttack] nakłada 4 [Combustion]
873. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Vibration] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]
   PL: [OnSucceedAttack] nakłada 4 [Vibration]
874. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 2, efekt 2 — opis] [AccelBullet] 소모
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 836 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
876. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 4 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +4 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 4 Licznika [Combustion]
877. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [Vibration] 횟수 4 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +4 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 4 Licznika [Vibration]
878. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 3, efekt 2 — opis] [AccelBullet] 소모
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 836 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
880. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]
   PL: [UnBrokenCoinOnSucceedAttack] uruchamia [Switch_Vibration], przekształcając je w [VibrationIgnition]
881. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
882. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion] 위력만큼 분노 속성 피해를 줌.
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 833 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 855 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
884. [Umiejętność wroga [131406] (ulepszenie 1) — moneta 4, efekt 4 — opis] [CriticalOnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131406].levelList[level=1].coinlist[#3].coindescs[#3].desc
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
885. [Umiejętność wroga [131407] (ulepszenie 1) — nazwa] 처분
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].name
   limit: do 40 znaków
   EN: Disposal
   PL: Disposal
886. [Umiejętność wroga [131407] (ulepszenie 1) — opis] [CantChangeTarget]\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n<color=#ff6000><mark color=#ff000040><b><u>[FutureEyeOn] 수치 1당, 기본 위력 + 1, 피해량 + 10%</color></mark></b></u>\n[WhenUse] 대상의 현재 체력이 50% 이하면, 피해량 + 100%\n[WhenUse] 정신력이 0 이상이면, 망(望) 하나를 생성함\n- 기본 위력 + 4\n[WhenUse] [Breath] 횟수 3 증가\n[WinDuel] [Breath] 5 얻음\n[DefeatDuel] 최종 피해량이 50%만큼 감소하고, 크리티컬이 발동하지 않음.\n이 스킬의 피해로 대상이 흐트러지지 않음\n[EnemyKill] 다음 턴에 무작위 수감자 1명에게 [TeachersPrey] 부여\n[EndSkill] [FullReload] (턴당 1회)\n[EndSkill] 망을 생성했으면, 정신력 10만큼 소모
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [CantChangeTarget], [FutureEyeOn], [WhenUse], [Breath], [WinDuel], [DefeatDuel], [EnemyKill], [TeachersPrey], [EndSkill], [FullReload]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [FutureEyeOn] = 예지안 / Eye of Precognition; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EnemyKill] = [적 처치 시] / [On Kill]; [TeachersPrey] = 사냥 표적 / Game Target …
   EN: [CantChangeTarget]\nCannot be Staggered before using this Skill\n<color=#ff6000><mark color=#ff000040><b><u>Base Power +1 and deal +10% damage for every [FutureEyeOn] Stack</color></mark></b></u>\n[WhenUse] If target has 50% or less HP, deal +100% damage\n[WhenUse] At 0+ SP, generate 1 Mang (望)\n- Base Power +4\n[WhenUse] Gain +3 [Breath] Count\n[WinDuel] Gain 5 [Breath]\n[DefeatDuel] Deal -50% final damage and does not hit Critically.\nDamage dealt by this Skill cannot Stagger the target\n[EnemyKill] Inflict [TeachersPrey] against a random Sinner next turn\n[EndSkill] [FullReload] (once per turn)\n[EndSkill] If this Skill generated Mang, lose 10 SP
   PL: [CantChangeTarget]\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n<color=#ff6000><mark color=#ff000040><b><u>Moc Bazowa +1 i zadaje +10% obrażeń za każdy Licznik [FutureEyeOn]</u></b></mark></color>\n[WhenUse] jeżeli aktualne HP celu wynosi 50% lub mniej, zadaje +100% obrażeń\n[WhenUse] przy SP równym 0 lub więcej tworzy 1 Mang (望)\n- Moc Bazowa +4\n[WhenUse] zyskuje 3 Licznika [Breath]\n[WinDuel] zyskuje 5 [Breath]\n[DefeatDuel] zadaje o 50% mniej końcowych obrażeń i nie zadaje trafienia krytycznego.\nobrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n[EnemyKill] nakłada [TeachersPrey] losowemu Grzesznikowi w następnej turze\n[EndSkill] [FullReload] (1 raz na turę)\n[EndSkill] jeżeli ta Umiejętność utworzyła Mang, traci 10 SP
887. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
888. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
890. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
891. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
892. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
894. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 6 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +6 [Combustion] Count
   PL: [OnSucceedAttack] nakłada 6 Licznika [Combustion]
895. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 6 증가
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +6 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 6 Licznika [Vibration]
896. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
897. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 880 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 5, efekt 2 — opis] [AccelBullet] 전부 소모
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#4].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AccelBullet]
   znaczenie tagów: [AccelBullet] = 가속탄 / Acceleration Round
   EN: Spend all [AccelBullet]
   PL: zużywa wszystkie [AccelBullet]
900. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 5, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 3회. 대상의 [Vibration] 횟수 3 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#4].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] 3 times; then, reduce target's [Vibration] Count by 3
   PL: [UnBrokenCoinOnSucceedAttack] uruchamia [VibrationExplosion] 3 razy; następnie zmniejsza Licznik [Vibration] celu o 3
901. [Umiejętność wroga [131407] (ulepszenie 1) — moneta 5, efekt 4 — opis] [CriticalOnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131407].levelList[level=1].coinlist[#4].coindescs[#3].desc
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [Umiejętność wroga [131408] (ulepszenie 1) — nazwa] 예지
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131408].levelList[level=1].name
   limit: do 40 znaków
   EN: Precognition
   PL: Precognition
903. [Umiejętność wroga [131408] (ulepszenie 1) — opis] 스킬의 모든 코인을 회피 성공할 시, 공격한 대상에게 ‘세치오나투라 디 코닐리오’으로 일방 공격함\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>[FutureEyeOn] 수치 2당, 기본 위력 +1</u></b></mark></color>\n[WhenUse] [FullReload] (턴당 1회)\n[OnSucceedEvade] [Breath] 3 얻음 (턴당 2회)\n[OnSucceedEvade] 정신력 2 회복 (턴당 5회)\n[OnDefeatEvade] 정신력 5 감소
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=131408].levelList[level=1].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [FutureEyeOn], [FullReload], [OnSucceedEvade], [Breath], [OnDefeatEvade]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FutureEyeOn] = 예지안 / Eye of Precognition; [FullReload] = 재장전 / Reload; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise; [OnDefeatEvade] = [회피 실패시] / [Failed Evade]
   EN: Upon successfully evading all Coins on a Skill, use "Sezionatura di Coniglio" as an Unopposed Attack against the attacker\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>Base Power +1 for every 2 [FutureEyeOn] Stack</u></b></mark></color>\n[WhenUse] [FullReload] (once per turn)\n[OnSucceedEvade] Gain 3 [Breath] (2 times per turn)\n[OnSucceedEvade] Heal 2 SP (5 times per turn)\n[OnDefeatEvade] Lose 5 SP
   PL: po udanym uniku wszystkich Monet Umiejętności wykonuje nieprzeciwstawiany atak „Sezionatura di Coniglio” przeciwko atakującemu\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>Moc Bazowa +1 za każde 2 Licznika [FutureEyeOn]</u></b></mark></color>\n[WhenUse] [FullReload] (1 raz na turę)\n[OnSucceedEvade] zyskuje 3 [Breath] (2 razy na turę)\n[OnSucceedEvade] przywraca 2 SP (5 razy na turę)\n[OnDefeatEvade] traci 5 SP
904. [Umiejętność wroga [130606] (ulepszenie 1) — nazwa] 지키겠습니다.
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=130606].levelList[level=1].name
   limit: do 40 znaków
   EN: I Will Protect.
   PL: I Will Protect.
905. [Umiejętność wroga [130606] (ulepszenie 1) — opis] [CanDuelGuard]\n[SupportProtect]전용 스킬\n[SupportProtect] 수치 1당, 받는 피해량 20% 감소\n[WhenUse] 아군의 정신력 8 증가\n[DefeatDuel] 다음 턴에 [Vulnerable] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=130606].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [SupportProtect], [WhenUse], [DefeatDuel], [Vulnerable]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile
   EN: [CanDuelGuard]\n[SupportProtect] Exclusive Skill\nTake -20% damage for every [SupportProtect] Stack\n[WhenUse] Heal allies by 8 SP\n[DefeatDuel] Gain 1 [Vulnerable] next turn
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [SupportProtect]\notrzymuje o 20% mniej obrażeń za każdy Licznik [SupportProtect]\n[WhenUse] przywraca sojusznikom 8 SP\n[DefeatDuel] zyskuje 1 [Vulnerable] w następnej turze
906. [Umiejętność wroga [130606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=130606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [Umiejętność wroga [133101] (ulepszenie 1) — nazwa] 설치 미술 제 3호 ‘간이늑골’
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133101].levelList[level=1].name
   limit: do 60 znaków
   EN: Installation Art no. 3: Improvised Ribcage
   PL: Installation Art no. 3: Improvised Ribcage
908. [Umiejętność wroga [133101] (ulepszenie 1) — opis] [CantDuel] [CantChangeTarget]\n레벨이 높은 적 우선 지정\n이 스킬은 수비 스킬을 발동시키지 않음\n[WhenUse] 대상의 [Laceration] 8당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133101].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [WhenUse], [Laceration]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [CantDuel] [CantChangeTarget]\nPrioritizes enemy with the highest level\nThis Skill does not trigger Defense Skills\n[WhenUse] Coin Power +1 for every 8 [Laceration] on target (max 2)
   PL: [CantDuel] [CantChangeTarget]\npriorytet: wróg z najwyższym poziomem\nta Umiejętność nie uruchamia Umiejętności obrony\n[WhenUse] Moc Monety +1 za każde 8 [Laceration] celu (maks. 2)
909. [Umiejętność wroga [133101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 체력 피해 대신 정신력 피해를 입힘
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal SP damage instead of HP damage
   PL: [OnSucceedAttack] zadaje obrażenia SP zamiast obrażeń HP
910. [Umiejętność wroga [133101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 정신력 15 회복
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 15 SP on self
   PL: [OnSucceedAttack] przywraca 15 SP jednostce
911. [Umiejętność wroga [133101] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>흐트러짐 상태로 만들고 다음 턴에 [LivingSpecimenTheRings]으로 만듦</u></b></mark></color>
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133101].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [OnSucceedAttack], [LivingSpecimenTheRings]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LivingSpecimenTheRings] = 신체관극 / Corpus Theater
   EN: [OnSucceedAttack]\n<color=#ff6000><mark=#ff000040><b><u>Stagger target and turn target into [LivingSpecimenTheRings] next turn</u></b></mark></color>
   PL: [OnSucceedAttack]\n<color=#ff6000><mark=#ff000040><b><u>Oszołomi cel i przekształci go w [LivingSpecimenTheRings] w następnej turze</u></b></mark></color>
912. [Umiejętność wroga [133102] (ulepszenie 1) — nazwa] 해체
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133102].levelList[level=1].name
   limit: do 40 znaków
   EN: Anatomize
   PL: Anatomize
913. [Umiejętność wroga [133102] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133102].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If target has 6+ [Laceration], Coin Power +1\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
914. [Umiejętność wroga [133102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
915. [Umiejętność wroga [133102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 4 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 4 [Laceration]
916. [Umiejętność wroga [133102] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133102].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
917. [Umiejętność wroga [133102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
918. [Umiejętność wroga [133102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
919. [Umiejętność wroga [133102] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음
   źródło: Skills_Abnormality-a1c9p3.json :: dataList[id=133102].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
