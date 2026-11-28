# Paczka AI P71 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 7/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P71_3c_przeciwnicy_i_anomalie_cz07.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P71_3c_przeciwnicy_i_anomalie_cz07.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [a1c7p1] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c7p1
- grupa rozdziału/trybu: `a1c7p1` · plik: `Skills_Enemy-a1c7p1.json`

1. [Umiejętność wroga [9015403] (ulepszenie 1) — nazwa] 이벤트가 남아있어!
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015403].levelList[level=1].name
   limit: do 40 znaków
   EN: We've an Event for You!
   PL: We've an Event for You!
2. [Umiejętność wroga [9015403] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10당 [BloodScissor] 1 얻음\n[WhenUse] 이 스킬에서 [BloodDinner]을 소모하지 못했으면, [Laceration] 5, [HardenedBlood]을 1 얻음.\n[WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015403].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodScissor], [Laceration], [HardenedBlood]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [WhenUse] Consume up to 50 [BloodDinner]; gain 1 [BloodScissor] for every 10 [BloodDinner] consumed\n[WhenUse] If this unit failed to consume [BloodDinner] with this Skill, gain 5 [Laceration] and 1 [HardenedBlood].\n[WhenUse] If target has 5+ [Laceration], Coin Power +1
   PL: [WhenUse] zużywa do 50 [BloodDinner]; zyskuje 1 [BloodScissor] za każde 10 zużytych [BloodDinner]\n[WhenUse] jeżeli ta Umiejętność nie zużyła [BloodDinner], zyskuje 5 [Laceration] i 1 [HardenedBlood].\n[WhenUse] jeżeli cel ma 5+ [Laceration], Moc Monety +1
3. [Umiejętność wroga [9015403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] nakłada 3 [Laceration]
4. [Umiejętność wroga [9015403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
5. [Umiejętność wroga [9015404] (ulepszenie 1) — nazwa] 재촉하지마
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015404].levelList[level=1].name
   limit: do 40 znaków
   EN: Don't Rush Me
   PL: Don't Rush Me
6. [Umiejętność wroga [9015404] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1\n[WhenUse] [BloodScissor]에 비례해서, 합 위력 +1 (최대 3)\n[HardenedBlood]당 피해량 +7% (최대 35%)\n[EndSkill] [HardenedBlood] 전부 소모
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015404].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BloodScissor], [HardenedBlood], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] If target has 5+ [Laceration], Coin Power +1\n[WhenUse] Clash Power +1 for every [BloodScissor] (max 3)\nDeal +7% damage for every [HardenedBlood] (max 35%)\n[EndSkill] Consume all [HardenedBlood]
   PL: [WhenUse] jeżeli cel ma 5+ [Laceration], Moc Monety +1\n[WhenUse] Moc Starcia +1 za każde [BloodScissor] (maks. 3)\nzadaje +7% obrażeń za każde [HardenedBlood] (maks. 35%)\n[EndSkill] zużywa całe [HardenedBlood]
7. [Umiejętność wroga [9015404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
8. [Umiejętność wroga [9015404] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 8 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015404].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 8 [Laceration]
   PL: [OnSucceedAttackHead] nakłada 8 [Laceration]
9. [Umiejętność wroga [9015404] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [BloodScissor]를 최대 5 소모하여 피해량 (20 * 소모한 [BloodScissor])% 증가 (최대 100%)
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015404].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloodScissor]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades
   EN: [OnSucceedAttack] Consume up to 5 [BloodScissor] and deal +(20 * consumed [BloodScissor])% damage (max 100%)
   PL: [OnSucceedAttack] zużywa do 5 [BloodScissor] i zadaje +(20 * zużytych [BloodScissor])% obrażeń (maks. 100%)
10. [Umiejętność wroga [9015404] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 최대 체력의 (대상의 [Laceration] 위력)%만큼 체력 회복 (최대 30%)
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015404].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Heal ([Laceration] Potency on target)% HP (max 30%)
   PL: [OnSucceedAttack] przywraca HP równe (Siły [Laceration] celu)% Maks. HP (maks. 30%)
11. [Umiejętność wroga [9015405] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015405].levelList[level=1].name
   limit: do 40 znaków
   EN: Counter
   PL: Counter
12. [Umiejętność wroga [9015405] (ulepszenie 1) — opis] [WhenUse] [BloodScissor] 1 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [HardenedBlood] 3 이상이면 코인 위력 +1
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015405].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodScissor], [HardenedBlood]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [WhenUse] At 1+ [BloodScissor], Base Power +1\n[WhenUse] At 3+ [HardenedBlood], Coin Power +1
   PL: [WhenUse] przy 1+ [BloodScissor], Moc Bazowa +1\n[WhenUse] przy 3+ [HardenedBlood], Moc Monety +1
13. [Umiejętność wroga [9015405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] nakłada 2 [Laceration]
14. [Umiejętność wroga [9015501] (ulepszenie 1) — nazwa] 더 많이 와줘
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015501].levelList[level=1].name
   limit: do 40 znaków
   EN: More, More!
   PL: More, More!
15. [Umiejętność wroga [9015501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Laceration]
16. [Umiejętność wroga [9015501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [Umiejętność wroga [9015502] (ulepszenie 1) — nazwa] 조금 더 먹을래
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015502].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Have Some More
   PL: I'll Have Some More
18. [Umiejętność wroga [9015502] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 4 이상이면, 피해량 +10%
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 4+ [Laceration], deal +10% damage
   PL: [WhenUse] jeżeli cel ma 4+ [Laceration], zadaje +10% obrażeń
19. [Umiejętność wroga [9015502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] nakłada 4 [Laceration]
20. [Umiejętność wroga [9015502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 5 이상이면, [HardenedBlood]을 1 얻음
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [HardenedBlood]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [OnSucceedAttack] If target has 5+ [Laceration], gain 1 [HardenedBlood]
   PL: [OnSucceedAttack] jeżeli cel ma 5+ [Laceration], zyskuje 1 [HardenedBlood]
21. [Umiejętność wroga [9015503] (ulepszenie 1) — nazwa] 맛이 기가 막힐거야!
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015503].levelList[level=1].name
   limit: do 40 znaków
   EN: What Heavenly Taste!
   PL: What Heavenly Taste!
22. [Umiejętność wroga [9015503] (ulepszenie 1) — opis] [WhenUse] 혈찬을 최대 50 소모하여 소모한 혈찬 10당 [BloodScissor] 1 얻음.\n[WhenUse] 이 스킬에서 [BloodDinner]을 소모하지 못했으면, [Laceration] 5, [HardenedBlood]을 1 얻음.\n[WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015503].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodScissor], [BloodDinner], [Laceration], [HardenedBlood]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades; [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [WhenUse] Consume up to 50 [BloodDinner]; gain 1 [BloodScissor] for every 10 [BloodDinner] consumed\n[WhenUse] If this unit failed to consume [BloodDinner] with this Skill, gain 5 [Laceration] and 1 [HardenedBlood].\n[WhenUse] If target has 5+ [Laceration], Coin Power +1
   PL: [WhenUse] zużywa do 50 [BloodDinner]; zyskuje 1 [BloodScissor] za każde 10 zużytych [BloodDinner].\n[WhenUse] jeżeli ta Umiejętność nie zużyła [BloodDinner], zyskuje 5 [Laceration] i 1 [HardenedBlood].\n[WhenUse] jeżeli cel ma 5+ [Laceration], Moc Monety +1
23. [Umiejętność wroga [9015503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
24. [Umiejętność wroga [9015503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
25. [Umiejętność wroga [9015504] (ulepszenie 1) — nazwa] 쥐새끼 같은 꼴이구나!
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015504].levelList[level=1].name
   limit: do 40 znaków
   EN: You Rat Bastard!
   PL: You Rat Bastard!
26. [Umiejętność wroga [9015504] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1\n[WhenUse] [BloodScissor]에 비례해서, 합 위력 +1 (최대 3)\n[HardenedBlood]당 피해량 +7% (최대 35%)\n[EndSkill] [HardenedBlood] 전부 소모
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015504].levelList[level=1].desc
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
27. [Umiejętność wroga [9015504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
28. [Umiejętność wroga [9015504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 8 [Laceration]
   PL: [OnSucceedAttack] nakłada 8 [Laceration]
29. [Umiejętność wroga [9015504] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [BloodScissor]를 최대 5 소모하여 피해량 (20 * 소모한 [BloodScissor])% 증가 (최대 100%)
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015504].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
30. [Umiejętność wroga [9015504] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 최대 체력의 (대상의 [Laceration] 위력)%만큼 체력 회복 (최대 30%)
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015504].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
31. [Umiejętność wroga [9015505] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015505].levelList[level=1].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
32. [Umiejętność wroga [9015505] (ulepszenie 1) — opis] [WhenUse] [BloodScissor] 1 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [HardenedBlood] 3 이상이면 코인 위력 +1
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015505].levelList[level=1].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
33. [Umiejętność wroga [9015505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
34. [Umiejętność wroga [9015601] (ulepszenie 1) — nazwa] 내려치기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015601].levelList[level=1].name
   limit: do 40 znaków
   EN: Slam
   PL: Slam
35. [Umiejętność wroga [9015601] (ulepszenie 1) — opis] 대상의 [Burst]이 5 이상이면, 피해량 +10%
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 5+ [Burst], deal +10% damage
   PL: jeżeli cel ma 5+ [Burst], zadaje +10% obrażeń
36. [Umiejętność wroga [9015601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL: [OnSucceedAttack] nakłada 3 [Burst]
37. [Umiejętność wroga [9015601] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015601].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown]
   PL: [OnSucceedAttack] nakłada 1 [DefenseDown]
38. [Umiejętność wroga [9015602] (ulepszenie 1) — nazwa] 상처 짓이기기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015602].levelList[level=1].name
   limit: do 40 znaków
   EN: Crush Wounds
   PL: Crush Wounds
39. [Umiejętność wroga [9015602] (ulepszenie 1) — opis] 대상의 [Burst]이 5 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 5+ [Burst], Base Power +1
   PL: jeżeli cel ma 5+ [Burst], Moc Bazowa +1
40. [Umiejętność wroga [9015602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL: [OnSucceedAttack] nakłada 1 [Burst]
41. [Umiejętność wroga [9015602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [TakeHpHealReduce] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TakeHpHealReduce]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down
   EN: [OnSucceedAttack] Inflict 1 [TakeHpHealReduce]
   PL: [OnSucceedAttack] nakłada 1 [TakeHpHealReduce]
42. [Umiejętność wroga [9015602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]이 5 이상이면, 추가로 [TakeHpHealReduce] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [TakeHpHealReduce]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down
   EN: [OnSucceedAttack] If target has 5+ [Burst], inflict 1 [TakeHpHealReduce] as well
   PL: [OnSucceedAttack] jeżeli cel ma 5+ [Burst], dodatkowo nakłada 1 [TakeHpHealReduce]
43. [Umiejętność wroga [9015603] (ulepszenie 1) — nazwa] 과격한 내려찍기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015603].levelList[level=1].name
   limit: do 40 znaków
   EN: Wild Swinging
   PL: Wild Swinging
44. [Umiejętność wroga [9015603] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 10 이상이면, 이 스킬로 적중 시 [Burst] 횟수를 소모하지 않음
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015603].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 10+ [Burst] Count: this Skill does not consume target's [Burst] Count On Hit
   PL: [WhenUse] jeżeli cel ma 10+ Licznika [Burst]: ta Umiejętność nie zużywa Licznika [Burst] celu przy trafieniu
45. [Umiejętność wroga [9015603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL: [OnSucceedAttack] nakłada 1 Licznika [Burst]
46. [Umiejętność wroga [9015603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable]
   PL: [OnSucceedAttack] nakłada 1 [Vulnerable]
47. [Umiejętność wroga [9015603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Burst]
   PL: [OnSucceedAttack] nakłada 4 [Burst]
48. [Umiejętność wroga [9015603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]이 10 이상이면, 피해량 +30%
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has 10+ [Burst], deal +30% damage
   PL: [OnSucceedAttack] jeżeli cel ma 10+ [Burst], zadaje +30% obrażeń
49. [Umiejętność wroga [9015604] (ulepszenie 1) — nazwa] 지혈
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015604].levelList[level=1].name
   limit: do 40 znaków
   EN: Hemostasis
   PL: Hemostasis
50. [Umiejętność wroga [9015604] (ulepszenie 1) — opis] [WhenUse] 자신에게 [Laceration]이 있다면, 자신의 [Laceration] 2 감소 (1 미만으로는 감소하지 않음)
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If this unit has [Laceration], lose 2 [Laceration] (does not drop below 1)
   PL: [WhenUse] jeżeli ta jednostka ma [Laceration], traci 2 [Laceration] (nie spadnie poniżej 1)
51. [Umiejętność wroga [9015701] (ulepszenie 1) — nazwa] 내려치기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015701].levelList[level=1].name
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Umiejętność wroga [9015701] (ulepszenie 1) — opis] 대상의 [Burst] 횟수가 3 이상이면, 피해량 +10%
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 3+ [Burst] Count, deal +10% damage
   PL: jeżeli cel ma 3+ Licznika [Burst], zadaje +10% obrażeń
53. [Umiejętność wroga [9015701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Burst]
54. [Umiejętność wroga [9015701] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015701].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [Umiejętność wroga [9015702] (ulepszenie 1) — nazwa] 상처 짓이기기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015702].levelList[level=1].name
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Umiejętność wroga [9015702] (ulepszenie 1) — opis] 대상의 [Burst] 횟수가 3 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 3+ [Burst] Count, Base Power +1
   PL: jeżeli cel ma 3+ Licznika [Burst], Moc Bazowa +1
57. [Umiejętność wroga [9015702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [Umiejętność wroga [9015702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [TakeHpHealReduce] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Umiejętność wroga [9015702] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]이 5 이상이면, 추가로 [TakeHpHealReduce] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [Umiejętność wroga [9015703] (ulepszenie 1) — nazwa] 과격한 내려찍기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015703].levelList[level=1].name
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Umiejętność wroga [9015703] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 10 이상이면, 이 스킬로 적중 시 [Burst] 횟수를 소모하지 않음
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015703].levelList[level=1].desc
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [Umiejętność wroga [9015703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [Umiejętność wroga [9015703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [Umiejętność wroga [9015703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
65. [Umiejętność wroga [9015703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]이 10 이상이면, 피해량 +30%
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Umiejętność wroga [9015704] (ulepszenie 1) — nazwa] 지혈
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015704].levelList[level=1].name
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [Umiejętność wroga [9015704] (ulepszenie 1) — opis] [WhenUse] 자신에게 [Laceration]이 있다면, 자신의 [Laceration] 2 감소(1 미만으로는 감소하지 않음)
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9015704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If this unit has [Laceration], lose 2 [Laceration] (does not drop below 1)
   PL: [WhenUse] jeżeli ta jednostka ma [Laceration], traci 2 [Laceration] (nie spadnie poniżej 1)
68. [Umiejętność wroga [9016001] (ulepszenie 1) — nazwa] 행패부리기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016001].levelList[level=1].name
   limit: do 40 znaków
   EN: Plain Villainy
   PL: Plain Villainy
69. [Umiejętność wroga [9016001] (ulepszenie 1) — opis] [WhenUse] [Breath] 2 얻음
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 2 [Breath]
   PL: [WhenUse] zyskuje 2 [Breath]
70. [Umiejętność wroga [9016001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] nakłada 1 [Laceration]
71. [Umiejętność wroga [9016001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 1 [Paralysis]
   PL: [OnSucceedAttack] nakłada 1 [Paralysis]
72. [Umiejętność wroga [9016001] (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 피해량 20% 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016001].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Deal +20% damage
   PL: [CriticalOnSucceedAttack] zadaje +20% obrażeń
73. [Umiejętność wroga [9016002] (ulepszenie 1) — nazwa] 핍박하기
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016002].levelList[level=1].name
   limit: do 40 znaków
   EN: Bullying
   PL: Bullying
74. [Umiejętność wroga [9016002] (ulepszenie 1) — opis] [WhenUse] [Breath] 2 얻음
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016002].levelList[level=1].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [Umiejętność wroga [9016002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Umiejętność wroga [9016002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [Umiejętność wroga [9016002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 대상이 [TrulyWeak] 디버프를 가지고 있으면, 피해량 30% 증가
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [TrulyWeak]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [TrulyWeak] = 약자 / The Weak
   EN: [CriticalOnSucceedAttack] If target has [TrulyWeak], deal +30% damage
   PL: [CriticalOnSucceedAttack] jeżeli cel ma debuff [TrulyWeak], zadaje +30% obrażeń
78. [Umiejętność wroga [9016101] (ulepszenie 1) — nazwa] "으르렁.."
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016101].levelList[level=1].name
   limit: do 40 znaków
   EN: "Grrr..."
   PL: "Grrr..."
79. [Umiejętność wroga [9016101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] nakłada 2 [Burst]
80. [Umiejętność wroga [9016102] (ulepszenie 1) — nazwa] "크르렁.."
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016102].levelList[level=1].name
   limit: do 40 znaków
   EN: "Krrr..."
   PL: "Krrr..."
81. [Umiejętność wroga [9016102] (ulepszenie 1) — opis] 대상에게 [Laceration]이 5 이상 있으면, 피해량 +10%
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 5+ [Laceration], deal +10% damage
   PL: jeżeli cel ma 5+ [Laceration], zadaje +10% obrażeń
82. [Umiejętność wroga [9016102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność wroga [9016102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Umiejętność wroga [9016103] (ulepszenie 1) — nazwa] 아니, 그러니까.."으르렁"
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016103].levelList[level=1].name
   limit: do 50 znaków
   EN: Listen, you sod. It's— "Grrrr."
   PL: Listen, you sod. It's— "Grrrr."
85. [Umiejętność wroga [9016103] (ulepszenie 1) — opis] 대상에게 [Laceration]이 5 이상 있으면, 코인 위력 +1
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016103].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 5+ [Laceration], Coin Power +1
   PL: jeżeli cel ma 5+ [Laceration], Moc Monety +1
86. [Umiejętność wroga [9016103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność wroga [9016103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Umiejętność wroga [9016103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Umiejętność wroga [9016104] (ulepszenie 1) — nazwa] ...
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016104].levelList[level=1].name
   limit: do 40 znaków
   EN: ...
   PL: ...
90. [Umiejętność wroga [9016104] (ulepszenie 1) — opis] [WhenUse] [Protection] 1 얻음
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Protection]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection
   EN: [WhenUse] Gain 1 [Protection]
   PL: [WhenUse] zyskuje 1 [Protection]
91. [Umiejętność wroga [9016105] (ulepszenie 1) — nazwa] 야, 나 이거 계속 해야돼?
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016105].levelList[level=1].name
   limit: do 40 znaków
   EN: Oi, can we stop now?
   PL: Oi, can we stop now?
92. [Umiejętność wroga [9016105] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_Enemy-a1c7p1.json :: dataList[id=9016105].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Enhancement]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [WhenUse] Gain 1 [Enhancement] next turn
   PL: [WhenUse] zyskuje 1 [Enhancement] w następnej turze

## [a1c7p1] Pasywka wroga: Passives_Abnormality-a1c7p1
- plik gry: `Passives_Abnormality-a1c7p1.json`

93. [[a1c7p1] Pasywka wroga [837101] — nazwa] 여유로운 기회
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837101].name
   limit: do 40 znaków
   EN: Casual Opportunity
   PL: Casual Opportunity
94. [[a1c7p1] Pasywka wroga [837101] — opis] 턴 시작 시 자신의 속도가 적보다 높으면, [PenetrateDamageUp] 1 얻음
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PenetrateDamageUp]
   znaczenie tagów: [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: Turn Start: if this unit's Speed is faster than the target's, gain 1 [PenetrateDamageUp]
   PL: Początek tury: jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, zyskuje 1 [PenetrateDamageUp]
95. [[a1c7p1] Pasywka wroga [837102] — nazwa] 느긋한 숨고르기
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837102].name
   limit: do 40 znaków
   EN: Leisurely Breathing
   PL: Leisurely Breathing
96. [[a1c7p1] Pasywka wroga [837102] — opis] 턴 종료 시 정신력 7 회복\n턴 종료 시 (자신의 [Breath] / 4)만큼 다음 턴에 [Agility] 얻음 (최대 3)
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837102].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Agility]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: Turn End: Heal 7 SP\nTurn End: Gain [Agility] equal to ([Breath] on self/4) next turn (max 3)
   PL: Koniec tury: przywraca 7 SP\nKoniec tury: zyskuje [Agility] w następnej turze równe ([Breath] tej jednostki/4) (maks. 3)
97. [[a1c7p1] Pasywka wroga [837103] — nazwa] 1:1 대결
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837103].name
   limit: do 40 znaków
   EN: Single Combat
   PL: Single Combat
98. [[a1c7p1] Pasywka wroga [837103] — opis] 대상이 흐트러짐 상태일 때, '살뤼'를 사용함
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837103].desc
   limit: do 120 znaków
   EN: Use Salut if the target is Staggered
   PL: używa „Salut”, gdy cel jest w Oszołamieniu
99. [[a1c7p1] Pasywka wroga [837104] — nazwa] 집중 공격
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837104].name
   limit: do 40 znaków
   EN: Focused Attack
   PL: Focused Attack
100. [[a1c7p1] Pasywka wroga [837104] — opis] 이전 턴에 공격 성공한 슬롯에 스킬 사용시 누적된 공격 성공 턴 수에 따라 다음과 같은 효과를 얻음.\n이전 턴에 공격하지 못했을 때, 초기화됨.\n- 공격 성공 누적 1턴: 합 위력 +1\n- 공격 성공 누적 2턴: 기본 위력 + 1\n- 공격 성공 누적 3턴: 기본 위력 + 1, 코인 위력 + 1
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837104].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When using a Skill against the same Slot this unit successfully hit last turn, gain the following effects based on the number of consecutive turns it successfully hit the Slot\nResets if this unit failed to attack last turn.\n- 1 Consecutive hit: Clash Power +1\n- 2 Consecutive hits: Base Power +1\n- 3 Consecutive hits: Base Power +1, Coin Power +1
   PL: przy użyciu Umiejętności przeciwko Slotowi, w który ta jednostka trafiła w poprzedniej turze, zyskuje następujące efekty w zależności od liczby kolejnych tur trafień\nresetuje się, jeżeli jednostka nie zaatakowała w poprzedniej turze.\n- 1 trafienie z rzędu: Moc Starcia +1\n- 2 trafienia z rzędu: Moc Bazowa +1\n- 3 trafienia z rzędu: Moc Bazowa +1, Moc Monety +1
101. [[a1c7p1] Pasywka wroga [837201] — nazwa] 너부터 오려줄게!
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837201].name
   limit: do 40 znaków
   EN: I'll Cut You First!
   PL: I'll Cut You First!
102. [[a1c7p1] Pasywka wroga [837201] — opis] [LineCutting]을 우선 공격함.
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [LineCutting]
   znaczenie tagów: [LineCutting] = 재봉 대상 / Sewing Target
   EN: Prioritizes [LineCutting].
   PL: priorytet: [LineCutting].
103. [[a1c7p1] Pasywka wroga [837202] — nazwa] 경혈식 가위
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837202].name
   limit: do 40 znaków
   EN: Hardblood Scissor
   PL: Hardblood Scissor
104. [[a1c7p1] Pasywka wroga [837202] — opis] 합 승리 시 대상에게 [Laceration]이 있으면, 입힌 체력 피해량의 40%만큼 부위와 본체 체력 회복\n공격 종료 시 체력을 100만큼 회복한 경우, 정신력 10 회복\n파괴 불가 코인의 경우 합 패배 후 적중 시 이 효과는 발동되지 않음.
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837202].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: On Clash Win, if the target has [Laceration], heal this unit's Part & Core by 40% of the HP damage dealt.\nAttack End: If this unit healed at least 100 HP, heal 10 SP\nThis effect does not activate On Hit with an Unbreakable Coin Skill if it loses the Clash.
   PL: wygrana w Starciu: jeżeli cel ma [Laceration], przywraca Części i Korpusowi HP równe 40% zadanych obrażeń HP.\npo zakończeniu Ataku: jeżeli jednostka przywróciła co najmniej 100 HP, przywraca 10 SP\nten efekt nie uruchamia się przy trafieniu Umiejętnością z Niezniszczalną Monetą po przegranej w Starciu.
105. [[a1c7p1] Pasywka wroga [837202] — podsumowanie] 출혈 상태인 적 공격시 체력 회복. 체력을 100 회복했으면 정신력도 회복.
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837202].summary
   limit: do 120 znaków
   EN: Heal when attacking enemies with Bleed. When this unit heals 100 HP, heal SP as well.
   PL: przywraca HP atakując wrogów z Krwawieniem. gdy jednostka przywróci 100 HP, przywraca również SP.
106. [[a1c7p1] Pasywka wroga [837203] — nazwa] 아름답지 않은 건 필요없어!!
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837203].name
   limit: do 40 znaków
   EN: I Don't Need Ugly Things!!
   PL: I Don't Need Ugly Things!!
107. [[a1c7p1] Pasywka wroga [837203] — opis] 적 중에서 전체 체력의 30%만큼 남은 적이 있다면, '아름답지 않은 건 필요없어!!'스킬을 사용함.
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837203].desc
   limit: do 120 znaków
   EN: If there are any enemies with 30% or less HP, use 'I Don't Need Ugly Things!!' Skill.
   PL: jeżeli istnieją wrogowie z HP równym 30% lub mniej, używa Umiejętności „I Don't Need Ugly Things!!”.
108. [[a1c7p1] Pasywka wroga [837204] — nazwa] 아직 끝나지 않았어
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837204].name
   limit: do 40 znaków
   EN: It's Not Over Yet
   PL: It's Not Over Yet
109. [[a1c7p1] Pasywka wroga [837204] — opis] 자신의 전체 체력의 40%가 남았을 때, 패턴 변경\n패턴 변경 시, 매 턴마다 [Laceration] 10, [BloodScissor] 2를 얻음.
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837204].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodScissor]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades
   EN: Gains a new pattern at 40% of this unit's max HP\nUpon pattern change, gain 10 [Laceration] and 2 [BloodScissor].
   PL: przybiera nowy wzorzec przy 40% Maks. HP tej jednostki\npo zmianie wzorca zyskuje co turę 10 [Laceration] i 2 [BloodScissor].
110. [[a1c7p1] Pasywka wroga [837205] — nazwa] 혈찬
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837205].name
   limit: do 40 znaków
   EN: Bloodfeast
   PL: Bloodfeast
111. [[a1c7p1] Pasywka wroga [837205] — opis] 이 캐릭터가 전투에 등장해 있거나, 등장할 적 리스트에 포함되어 있으면, 1턴부터 모든 캐릭터가 받은 [Laceration] 피해만큼 [BloodDinner]이 증가함.\n이 캐릭터가 전투에 등장할 때 전장에 흩뿌려진 잠재된 피가 더욱 드러난다.
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837205].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: If this unit is on field, or is one of the units that can appear on this Stage, increase [BloodDinner] value by the amount of [Laceration] damage collectively received by every unit. \nWhen this unit enters the field, the sleeping blood drenching the battlefield will rise above the surface.
   PL: jeżeli ta jednostka jest na polu bitwy lub znajduje się na liście wrogów mogących się pojawić w tej walce, od 1. tury [BloodDinner] rośnie o łączną wartość obrażeń [Laceration] otrzymanych przez wszystkie jednostki.\ngdy ta jednostka pojawia się na polu bitwy, uśpiona krew przesiąkająca pole bitwy wypływa na powierzchnię.
112. [[a1c7p1] Pasywka wroga [837206] — nazwa] 피를 머금은 가위
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837206].name
   limit: do 40 znaków
   EN: Bloodsteeped Scissors
   PL: Bloodsteeped Scissors
113. [[a1c7p1] Pasywka wroga [837206] — opis] 전투 시작 시, [BloodScissor]을 10 얻음\n- [BloodScissor]이 1 미만으로 감소하지 않음\n- [BloodScissor]이 10 이상이면, [BloodScissorTwo] 로 전환됨.\n- [BloodScissor]이 20 이상이면, [BloodScissorThree] 로 전환됨\n[BloodScissor]이 소모되어, 부족해지면 이전 단계가 됨
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837206].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [BloodScissor], [BloodScissorTwo], [BloodScissorThree]
   znaczenie tagów: [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades; [BloodScissorTwo] = 핏빛 가위날 II / Blood-tinged Scissorblades II; [BloodScissorThree] = 핏빛 가위날 III / Blood-tinged Scissorblades III
   EN: Combat Start: gain 10 [BloodScissor]\n- [BloodScissor] cannot drop below 1\n- At 10+ [BloodScissor], convert them to [BloodScissorTwo].\n- At 20+ [BloodScissor], convert them to [BloodScissorThree].\nIf this unit consumes [BloodScissor] and drops below the above thresholds, convert them accordingly.
   PL: Początek walki: zyskuje 10 [BloodScissor]\n- [BloodScissor] nie spadnie poniżej 1\n- przy 10+ [BloodScissor], przekształca je w [BloodScissorTwo].\n- przy 20+ [BloodScissor], przekształca je w [BloodScissorThree].\njeżeli jednostka zużyje [BloodScissor] i spadnie poniżej powyższych progów, przekształca je odpowiednio.
114. [[a1c7p1] Pasywka wroga [837207] — nazwa] 굶주림과 노쇠
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837207].name
   limit: do 40 znaków
   EN: Starved and Withered
   PL: Starved and Withered
115. [[a1c7p1] Pasywka wroga [837207] — opis] 전투 시작 시, [StarvingBarberTwo] 얻음
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837207].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StarvingBarberTwo]
   znaczenie tagów: [StarvingBarberTwo] = 노쇠 / Withered
   EN: Combat Start: gain [StarvingBarberTwo]
   PL: Początek walki: zyskuje [StarvingBarberTwo]
116. [[a1c7p1] Pasywka wroga [837208] — nazwa] 피... 피... 피...!
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837208].name
   limit: do 40 znaków
   EN: Blood... Blood... Blood...!
   PL: Blood... Blood... Blood...!
117. [[a1c7p1] Pasywka wroga [837208] — opis] 턴 종료 시 패닉 상태면, 다음 턴 시작 시 패닉 상태를 해제하고, 정신력이 0으로 초기화 됨.\n패닉 상태가 해제될 때\n- [BloodDinner]을 30 소모하여 다음 턴에 [Enhancement] 2,  [BloodScissor]을 1 얻고, 정신력 20 회복.\n- [BloodDinner]을 소모하지 못했으면, [Laceration]을 30 얻고, [Laceration]로 인한 피해를 즉시 발동시킨 후, [Laceration] 횟수가 3 감소함. 이후 다음 턴에 [Enhancement] 2, [AttackDmgUp] 2를 얻고, 정신력 20 회복.
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=837208].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [Enhancement], [BloodScissor], [Laceration], [AttackDmgUp]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [Enhancement] = 공격 위력 증가 / Attack Power Up; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades; [Laceration] = 출혈 / Bleed; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn End: If Panicked, recover from Panic at the next Turn Start and reset SP to 0.\nWhen recovering from Panic:\n- Consume 30 [BloodDinner] to gain 2 [Enhancement] and 1 [BloodScissor] next turn, and heal 20 SP.\n- If this unit failed to consume [BloodDinner], gain 30 [Laceration], immediately take the damage from [Laceration], then lose 3 [Laceration] Count. Then, gain 2 [Enhancement], 2 [AttackDmgUp], and heal 20 SP next turn.
   PL: Koniec tury: jeżeli jest w Panice, na początku następnej tury dochodzi do siebie z Paniki, a SP wraca do 0.\nprzy dochodzeniu do siebie z Paniki:\n- zużywa 30 [BloodDinner], by zyskać 2 [Enhancement] i 1 [BloodScissor] w następnej turze, oraz przywraca 20 SP.\n- jeżeli nie udało się zużyć [BloodDinner], zyskuje 30 [Laceration], natychmiast uruchamia obrażenia od [Laceration], po czym traci 3 Licznika [Laceration]. Następnie w następnej turze zyskuje 2 [Enhancement], 2 [AttackDmgUp] i przywraca 20 SP.
118. [[a1c7p1] Pasywka wroga [9999997] — nazwa] 패닉 회복
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=9999997].name
   limit: do 40 znaków
   EN: Panic Recovery
   PL: Panic Recovery
119. [[a1c7p1] Pasywka wroga [9999997] — opis] 턴 종료 시 패닉 상태라면 정신력이 0이됨.
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=9999997].desc
   limit: do 120 znaków
   EN: Turn End: if in Panic, reset SP to 0.
   PL: Koniec tury: jeżeli jest w Panice, SP wraca do 0.
120. [[a1c7p1] Pasywka wroga [9999996] — nazwa] 패닉 변경 불가
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=9999996].name
   limit: do 40 znaków
   EN: Fixed Panic
   PL: Panika zablokowana
121. [[a1c7p1] Pasywka wroga [9999996] — opis] 패닉 유형을 변경하는 버프 획득 시, 패닉 유형이 변경되지 않음. 대신 정신력이 없는 대상에게 부여되는 효과가 부여됨
   źródło: Passives_Abnormality-a1c7p1.json :: dataList[id=9999996].desc
   limit: do 240 znaków
   EN: This unit's Panic Type does not change when inflicted with an effect that changes Panic Types. Instead, this unit is inflicted with an effect that is inflicted against Non-SP Units.
   PL: gdy ta jednostka zyskuje Efekt zmieniający typ Paniki, typ Paniki się nie zmienia. Zamiast tego nakładany jest efekt nakładany na jednostki bez SP.

## [a1c7p1] Pasywka wroga: Passives_Enemy-a1c7p1
- plik gry: `Passives_Enemy-a1c7p1.json`

122. [[a1c7p1] Pasywka wroga [9015206] — nazwa] 굶주림과 노쇠
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015206].name
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [[a1c7p1] Pasywka wroga [9015206] — opis] 전투 시작 시, [StarvingBarberOne] 얻음
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015206].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StarvingBarberOne]
   znaczenie tagów: [StarvingBarberOne] = 노쇠 / Withered
   EN: Gain [StarvingBarberOne] at the start of the Encounter
   PL: Początek walki: zyskuje [StarvingBarberOne]
124. [[a1c7p1] Pasywka wroga [9015202] — nazwa] 노쇠
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015202].name
   limit: do 40 znaków
   EN: Withered
   PL: Withered
125. [[a1c7p1] Pasywka wroga [9015202] — opis] 턴 시작 시 [Laceration]이 있는 대상이 없으면, 속도 최댓값 -2 (아군, 적군 전부 포함)
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015202].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Turn Start: if no one has [Laceration], Min Speed -2 (checks both allies & enemies)
   PL: Początek tury: jeżeli nikt nie ma [Laceration], Maks. Szybkość -2 (dotyczy sojuszników i wrogów)
126. [[a1c7p1] Pasywka wroga [9015203] — nazwa] 흡혈
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015203].name
   limit: do 40 znaków
   EN: Bloodsucking
   PL: Bloodsucking
127. [[a1c7p1] Pasywka wroga [9015203] — opis] 공격 적중시 대상에게 [Laceration]이 있으면, 피해량의 15%만큼 체력 회복
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015203].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: On Hit, if the target has [Laceration], heal by 15% of damage dealt
   PL: przy trafieniu, jeżeli cel ma [Laceration], przywraca HP równe 15% zadanych obrażeń
128. [[a1c7p1] Pasywka wroga [9015204] — nazwa] 혈액 경화
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015204].name
   limit: do 40 znaków
   EN: Blood Coagulation
   PL: Blood Coagulation
129. [[a1c7p1] Pasywka wroga [9015204] — opis] 공격 종료시 대상의 [Laceration]이 8 이상이면, [HardenedBlood] 1 얻음
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015204].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration], [HardenedBlood]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: Attack End: If the target has 8+ [Laceration], gain 1 [HardenedBlood]
   PL: po zakończeniu Ataku: jeżeli cel ma 8+ [Laceration], zyskuje 1 [HardenedBlood]
130. [[a1c7p1] Pasywka wroga [9015205] — nazwa] 핏빛 가위날
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015205].name
   limit: do 40 znaków
   EN: Blood-tinged Scissorblades
   PL: Blood-tinged Scissorblades
131. [[a1c7p1] Pasywka wroga [9015205] — opis] [BloodScissor]이 1 이상이면, 가위의 날이 강화됨.
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015205].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BloodScissor]
   znaczenie tagów: [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades
   EN: At 1+ [BloodScissor], enhance the blades of the scissor.
   PL: przy 1+ [BloodScissor], ostrza nożyc są wzmocnione.
132. [[a1c7p1] Pasywka wroga [9015207] — nazwa] 피주머니
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015207].name
   limit: do 40 znaków
   EN: Bloodbag
   PL: Bloodbag
133. [[a1c7p1] Pasywka wroga [9015207] — opis] 피격 시 자신의 [Laceration] 횟수 1 증가.\n체력이 20% 감소할 때마다 [HardenedBlood] 1 얻음.\n아군 또는 적에 혈귀가 있는 경우, 사망 시, [BloodDinner]이 30만큼 증가
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015207].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [HardenedBlood], [BloodDinner]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [BloodDinner] = 혈찬 / Bloodfeast
   EN: When hit, gain +1 [Laceration] Count.\nGain 1 [HardenedBlood] every time this unit loses 20% HP.\nIf there is a Bloodfiend on the field, regardless of whether it is an ally or an enemy, increase [BloodDinner] by 30
   PL: przy otrzymaniu trafienia zyskuje 1 Licznika [Laceration].\nzyskuje 1 [HardenedBlood] za każdym razem, gdy traci 20% HP.\njeżeli na polu bitwy znajduje się Bloodfiend — sojusznik lub wróg — przy śmierci zwiększa [BloodDinner] o 30
134. [[a1c7p1] Pasywka wroga [9015401] — nazwa] 흡혈
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015401].name
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [[a1c7p1] Pasywka wroga [9015401] — opis] 공격 적중시 대상에게 [Laceration]이 있으면, 피해량의 20%만큼 체력 회복
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015401].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: On Hit, if the target has [Laceration], heal by 20% of damage dealt
   PL: przy trafieniu, jeżeli cel ma [Laceration], przywraca HP równe 20% zadanych obrażeń
136. [[a1c7p1] Pasywka wroga [9015402] — nazwa] 혈액 경화
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015402].name
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [[a1c7p1] Pasywka wroga [9015402] — opis] 공격 종료시 대상의 [Laceration]이 5 이상이면, [HardenedBlood] 1 얻음
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015402].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration], [HardenedBlood]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: Attack End: If the target has 5+ [Laceration], gain 1 [HardenedBlood]
   PL: po zakończeniu Ataku: jeżeli cel ma 5+ [Laceration], zyskuje 1 [HardenedBlood]
138. [[a1c7p1] Pasywka wroga [9015403] — nazwa] 피의 갈증
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015403].name
   limit: do 40 znaków
   EN: Thirst for Blood
   PL: Thirst for Blood
139. [[a1c7p1] Pasywka wroga [9015403] — opis] - [Laceration]이 부여된 대상을 우선적으로 공격\n- 턴 종료 시 이번 턴에 피해를 주지 못한 경우, 다음 턴에 취약 2, 공격 레벨 증가 2를 얻음\n- 턴 종료 시 이번 턴에 피해를 줬다면,정신력 5 회복
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015403].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Vulnerable]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Vulnerable] = 취약 / Fragile
   EN: - Prioritizes targets with [Laceration]\nTurn End: if this unit failed to deal any damage this turn, gain 2 [Vulnerable] and 2 Offense Level Up next turn\n- Turn End: if this unit dealt damage this turn, heal 5 SP
   PL: - priorytet: cele z [Laceration]\n- Koniec tury: jeżeli nie zadała żadnych obrażeń w tej turze, zyskuje 2 [Vulnerable] i 2 Wzrost Poziomu Ataku w następnej turze\n- Koniec tury: jeżeli zadała obrażenia w tej turze, przywraca 5 SP
140. [[a1c7p1] Pasywka wroga [9015404] — nazwa] 혈찬
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015404].name
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [[a1c7p1] Pasywka wroga [9015404] — opis] 이 캐릭터가 전투에 등장해 있거나, 등장할 적 리스트에 포함되어 있으면, 1턴부터 모든 캐릭터가 받은 [Laceration] 피해만큼 [BloodDinner]이 증가함.\n이 캐릭터가 전투에 등장할 때 전장에 흩뿌려진 잠재된 피를 드러낸다.
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015404].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: If this unit is on field, or is one of the units that can appear on this Stage, increase [BloodDinner] value by the amount of [Laceration] damage collectively received by every unit. \nWhen this unit enters the field, the sleeping blood drenching the battlefield will surface.
   PL: jeżeli ta jednostka jest na polu bitwy lub znajduje się na liście wrogów mogących się pojawić w tej walce, od 1. tury [BloodDinner] rośnie o łączną wartość obrażeń [Laceration] otrzymanych przez wszystkie jednostki.\ngdy ta jednostka pojawia się na polu bitwy, uśpiona krew przesiąkająca pole bitwy wynurza się na powierzchnię.
142. [[a1c7p1] Pasywka wroga [9015405] — nazwa] 핏빛 가위날
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015405].name
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [[a1c7p1] Pasywka wroga [9015405] — opis] [BloodScissor]이 2 이상이면, 가위의 날이 강화됨.
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015405].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BloodScissor]
   znaczenie tagów: [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades
   EN: At 2+ [BloodScissor], enhance the blades of the scissor.
   PL: przy 2+ [BloodScissor], ostrza nożyc są wzmocnione.
144. [[a1c7p1] Pasywka wroga [9015601] — nazwa] 혈귀 사냥꾼
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015601].name
   limit: do 40 znaków
   EN: Bloodfiend Hunter
   PL: Bloodfiend Hunter
145. [[a1c7p1] Pasywka wroga [9015601] — opis] 대상이 <혈귀>, <피주머니>면 피해량 +10%
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015601].desc
   limit: do 120 znaków
   EN: If the target is a <Bloodfiend> or a <Bloodbag>, deal +10% damage
   PL: jeżeli cel to <Bloodfiend> lub <Bloodbag>, zadaje +10% obrażeń
146. [[a1c7p1] Pasywka wroga [9015602] — nazwa] 과격한 사냥법
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015602].name
   limit: do 50 znaków
   EN: Aggressive Hunting Techniques
   PL: Aggressive Hunting Techniques
147. [[a1c7p1] Pasywka wroga [9015602] — opis] 적에게 공격 스킬 적중 시 10% 확률로 [Burst] 횟수 2 증가
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015602].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: When hitting an enemy with an Attack Skill, 10% chance to inflict +2 [Burst] Count
   PL: przy trafieniu wroga Umiejętnością ataku 10% szans na nałożenie 2 Licznika [Burst]
148. [[a1c7p1] Pasywka wroga [9015603] — nazwa] 대 혈귀전용 망치
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015603].name
   limit: do 40 znaków
   EN: Anti-Bloodfiend Hammer
   PL: Anti-Bloodfiend Hammer
149. [[a1c7p1] Pasywka wroga [9015603] — opis] 스킬 사용 시, 대상의 [Burst]이 10 이상이면, 스킬에서 [Burst]을 부여하는 대신 피해량이 30% 증가
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015603].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: On Skill use, if the target has 10+ [Burst], deal +30% damage instead of inflicting [Burst] with this unit's Skills
   PL: przy użyciu Umiejętności, jeżeli cel ma 10+ [Burst], zamiast nakładać [Burst] zadaje +30% obrażeń
150. [[a1c7p1] Pasywka wroga [9015604] — nazwa] 지혈제
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015604].name
   limit: do 40 znaków
   EN: Styptics
   PL: Styptics
151. [[a1c7p1] Pasywka wroga [9015604] — opis] 턴 종료시, 자신에게 [Laceration]이 있으면 [Laceration] 횟수 1 감소
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9015604].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Turn End: if this unit has [Laceration], lose 1 [Laceration] Count
   PL: Koniec tury: jeżeli ta jednostka ma [Laceration], traci 1 Licznika [Laceration]
152. [[a1c7p1] Pasywka wroga [9016001] — nazwa] 약자 표식
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9016001].name
   limit: do 40 znaków
   EN: Weakling Mark
   PL: Weakling Mark
153. [[a1c7p1] Pasywka wroga [9016001] — opis] 합 승리시, 대상에게 [TrulyWeak] 디버프를 부여함
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9016001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TrulyWeak]
   znaczenie tagów: [TrulyWeak] = 약자 / The Weak
   EN: On Clash Win, inflict [TrulyWeak]
   PL: wygrana w Starciu: nakłada debuff [TrulyWeak] na cel
154. [[a1c7p1] Pasywka wroga [9016002] — nazwa] 악의 무리
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9016002].name
   limit: do 40 znaków
   EN: The Wicked Caitiffs
   PL: The Wicked Caitiffs
155. [[a1c7p1] Pasywka wroga [9016002] — opis] 약자를 괴롭히는 것을 좋아함
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9016002].desc
   limit: do 120 znaków
   EN: Loves bullying the weak
   PL: uwielbia znęcać się nad słabszymi
156. [[a1c7p1] Pasywka wroga [9016003] — nazwa] 비열함
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9016003].name
   limit: do 40 znaków
   EN: Bullies
   PL: Bullies
157. [[a1c7p1] Pasywka wroga [9016003] — opis] [TrulyWeak] 디버프를 가진 적을 공격할 때, 합 위력 1 증가
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9016003].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TrulyWeak]
   znaczenie tagów: [TrulyWeak] = 약자 / The Weak
   EN: Clash Power +1 when attacking an enemy with [TrulyWeak]
   PL: Moc Starcia +1 przy atakowaniu wroga z debuffem [TrulyWeak]
158. [[a1c7p1] Pasywka wroga [9016101] — nazwa] 시시하지 않은 전투
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9016101].name
   limit: do 50 znaków
   EN: An Encounter of Moderate Difficulty
   PL: An Encounter of Moderate Difficulty
159. [[a1c7p1] Pasywka wroga [9016101] — opis] 이 캐릭터가 가하는 피해량 +15%
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9016101].desc
   limit: do 120 znaków
   EN: Deals +15% damage
   PL: zadaje +15% obrażeń
160. [[a1c7p1] Pasywka wroga [9016102] — nazwa] 사람까지 잡아먹는 곰
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9016102].name
   limit: do 40 znaków
   EN: The Man-eating Bear
   PL: The Man-eating Bear
161. [[a1c7p1] Pasywka wroga [9016102] — opis] 현재 체력이 최대 체력의 50% 이하인 대상에게 가하는 피해량 +25%
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9016102].desc
   limit: do 120 znaków
   EN: Deal +25% damage against targets with 50%- HP
   PL: zadaje +25% obrażeń celom z 50% HP lub mniej
162. [[a1c7p1] Pasywka wroga [9016103] — nazwa] 무시무시함
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9016103].name
   limit: do 40 znaków
   EN: Big & Scary
   PL: Big & Scary
163. [[a1c7p1] Pasywka wroga [9016103] — opis] 합 진행 시 대상의 정신력이 1 감소할 수도 있음
   źródło: Passives_Enemy-a1c7p1.json :: dataList[id=9016103].desc
   limit: do 120 znaków
   EN: In a Clash, the opponent just might lose 1 SP, maybe
   PL: podczas Starcia przeciwnik czasem traci 1 SP — może

## [a1c7p2] Wróg / część: Enemies-a1c7p2
- plik gry: `Enemies-a1c7p2.json`

164. [[a1c7p2] Wróg / część [90173] — nazwa] 괴로운 행렬의 피주머니
   źródło: Enemies-a1c7p2.json :: dataList[id=90173].name
   limit: do 50 znaków
   EN: Bloodbag of the Painful Parade
   PL: Bloodbag of the Painful Parade
165. [[a1c7p2] Wróg / część [90173] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=90173].desc
   limit: do 120 znaków
   EN: Unit
   PL: jednostka
166. [[a1c7p2] Wróg / część [90174] — nazwa] 뒤따르는 행렬의 피주머니
   źródło: Enemies-a1c7p2.json :: dataList[id=90174].name
   limit: do 40 znaków
   EN: Bloodbag of the Rear Parade
   PL: Bloodbag of the Rear Parade
167. [[a1c7p2] Wróg / część [90174] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=90174].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [[a1c7p2] Wróg / część [90175] — nazwa] 행복한 행렬의 혈귀
   źródło: Enemies-a1c7p2.json :: dataList[id=90175].name
   limit: do 50 znaków
   EN: Bloodfiend of the Happy Parade
   PL: Bloodfiend of the Happy Parade
169. [[a1c7p2] Wróg / część [90175] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=90175].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [[a1c7p2] Wróg / część [90176] — nazwa] 즐거운 행렬의 혈귀
   źródło: Enemies-a1c7p2.json :: dataList[id=90176].name
   limit: do 50 znaków
   EN: Bloodfiend of the Joyful Parade
   PL: Bloodfiend of the Joyful Parade
171. [[a1c7p2] Wróg / część [90176] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=90176].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [[a1c7p2] Wróg / część [8381] — nazwa] 돌시네아
   źródło: Enemies-a1c7p2.json :: dataList[id=8381].name
   limit: do 40 znaków
   EN: Dulcinea
   PL: Dulcinea
173. [[a1c7p2] Wróg / część [8381] — opis] 보스
   źródło: Enemies-a1c7p2.json :: dataList[id=8381].desc
   limit: do 120 znaków
   EN: Boss
   PL: Boss
174. [[a1c7p2] Wróg / część [90158] — nazwa] 전락한 피주머니
   źródło: Enemies-a1c7p2.json :: dataList[id=90158].name
   limit: do 40 znaków
   EN: Disgraced Bloodbag
   PL: Disgraced Bloodbag
175. [[a1c7p2] Wróg / część [90158] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=90158].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [[a1c7p2] Wróg / część [90159] — nazwa] 절망하는 피주머니
   źródło: Enemies-a1c7p2.json :: dataList[id=90159].name
   limit: do 40 znaków
   EN: Despairing Bloodbag
   PL: Despairing Bloodbag
177. [[a1c7p2] Wróg / część [90159] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=90159].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [[a1c7p2] Wróg / część [8384] — nazwa] 괴로운 행렬의 피주머니
   źródło: Enemies-a1c7p2.json :: dataList[id=8384].name
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [[a1c7p2] Wróg / część [8384] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=8384].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [[a1c7p2] Wróg / część [8385] — nazwa] 뒤따르는 행렬의 피주머니
   źródło: Enemies-a1c7p2.json :: dataList[id=8385].name
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [[a1c7p2] Wróg / część [8385] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=8385].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [[a1c7p2] Wróg / część [8386] — nazwa] 행복한 행렬의 혈귀
   źródło: Enemies-a1c7p2.json :: dataList[id=8386].name
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [[a1c7p2] Wróg / część [8386] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=8386].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [[a1c7p2] Wróg / część [8387] — nazwa] 즐거운 행렬의 혈귀
   źródło: Enemies-a1c7p2.json :: dataList[id=8387].name
   (powtórzenie elementu 170 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [[a1c7p2] Wróg / część [8387] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=8387].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [[a1c7p2] Wróg / część [8382] — nazwa] 전락한 피주머니
   źródło: Enemies-a1c7p2.json :: dataList[id=8382].name
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [[a1c7p2] Wróg / część [8382] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=8382].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [[a1c7p2] Wróg / część [8383] — nazwa] 절망하는 피주머니
   źródło: Enemies-a1c7p2.json :: dataList[id=8383].name
   (powtórzenie elementu 176 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [[a1c7p2] Wróg / część [8383] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=8383].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [[a1c7p2] Wróg / część [90169] — nazwa] 으스스한 피주머니
   źródło: Enemies-a1c7p2.json :: dataList[id=90169].name
   limit: do 40 znaków
   EN: Eerie Bloodbag
   PL: Eerie Bloodbag
191. [[a1c7p2] Wróg / część [90169] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=90169].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [[a1c7p2] Wróg / część [90170] — nazwa] 섬뜩한 피주머니
   źródło: Enemies-a1c7p2.json :: dataList[id=90170].name
   limit: do 40 znaków
   EN: Sinister Bloodbag
   PL: Sinister Bloodbag
193. [[a1c7p2] Wróg / część [90170] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=90170].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [[a1c7p2] Wróg / część [90171] — nazwa] 회개 못한 유령 역할 혈귀
   źródło: Enemies-a1c7p2.json :: dataList[id=90171].name
   limit: do 60 znaków
   EN: "Ghost" Bloodfiend of Failed Penitence
   PL: "Ghost" Bloodfiend of Failed Penitence
195. [[a1c7p2] Wróg / część [90171] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=90171].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [[a1c7p2] Wróg / część [90172] — nazwa] 기도하는 유령 역할 혈귀
   źródło: Enemies-a1c7p2.json :: dataList[id=90172].name
   limit: do 50 znaków
   EN: "Ghost" Bloodfiend of Prayers
   PL: "Ghost" Bloodfiend of Prayers
197. [[a1c7p2] Wróg / część [90172] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=90172].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [[a1c7p2] Wróg / część [8389] — nazwa] 하얀 달의 기사
   źródło: Enemies-a1c7p2.json :: dataList[id=8389].name
   limit: do 40 znaków
   EN: The Knight of the White Moon
   PL: The Knight of the White Moon
199. [[a1c7p2] Wróg / część [8389] — opis] 잡몹
   źródło: Enemies-a1c7p2.json :: dataList[id=8389].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c7p2] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c7p2
- grupa rozdziału/trybu: `a1c7p2` · plik: `Skills_Abnormality-a1c7p2.json`

200. [Umiejętność wroga [838101] (ulepszenie 1) — nazwa] 걸음은 우아하게...
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838101].levelList[level=1].name
   limit: do 40 znaków
   EN: Walk With Grace...
   PL: Walk With Grace...
201. [Umiejętność wroga [838101] (ulepszenie 1) — opis] 흐트러지지 않은 아군을 우선으로 지정하며, 대상이 아군이면 합 위력 +10, 피해량이 항상 0으로 고정\n대상의 [Laceration] 3당 합 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838101].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Prioritize an unstaggered ally. If the target is an ally, gain Clash Power +10, and fix the damage to 0 at all times\nClash Power +1 for every 3 [Laceration] on the target (max 3)
   PL: priorytet: sojusznik niebędący w Oszołamieniu; jeżeli celem jest sojusznik, Moc Starcia +10, a obrażenia są zawsze zerowe\nMoc Starcia +1 za każde 3 [Laceration] celu (maks. 3)
202. [Umiejętność wroga [838101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여\n- 대상이 아군이면 이 효과를 대신하여 다음 턴까지 [AttackUp] 3 부여
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Laceration], [AttackUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttack] Inflict 3 [Laceration]\n- If the target is an ally, replace this effect with 3 [AttackUp] until next turn
   PL: [OnSucceedAttack] nakłada 3 [Laceration]\n- jeżeli celem jest sojusznik, zamiast tego nakłada 3 [AttackUp] do następnej tury
203. [Umiejętność wroga [838102] (ulepszenie 1) — nazwa] 몸짓은 아름답게...
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838102].levelList[level=1].name
   limit: do 40 znaków
   EN: Move With Beauty...
   PL: Move With Beauty...
204. [Umiejętność wroga [838102] (ulepszenie 1) — opis] 흐트러지지 않은 아군을 우선으로 지정하며, 대상이 아군이면 합 위력 +10, 피해량이 항상 0으로 고정\n대상의 [Laceration] 3당 합 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838102].levelList[level=1].desc
   (powtórzenie elementu 201 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Umiejętność wroga [838102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가\n- 대상이 아군이면 이 효과를 대신하여 다음 턴까지 [DefenseUp] 3 부여
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Laceration], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count\n- If the target is an ally, replace this effect with 3 [DefenseUp] until next turn
   PL: [OnSucceedAttack] nakłada 3 Licznika [Laceration]\n- jeżeli celem jest sojusznik, zamiast tego nakłada 3 [DefenseUp] do następnej tury
206. [Umiejętność wroga [838103] (ulepszenie 1) — nazwa] 관객을 향해 손짓해...
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838103].levelList[level=1].name
   limit: do 50 znaków
   EN: Beckon the Audience Hither...
   PL: Beckon the Audience Hither...
207. [Umiejętność wroga [838103] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever] 5 또는 대상의 [Laceration] 6당 최종 위력 +1 (최대 4)\n[WhenUse] [BloodDinner]이 15 미만이면, [Laceration] 15를 얻은 다음 즉시 1회 발동시키고 [Laceration] 횟수 1 감소 (체력이 10% 미만이면 [Laceration], [Laceration] 횟수를 얻는 효과만 발동)\n[EndSkill] [BloodDinner] 15 소모
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838103].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [FestivalFever], [Laceration], [BloodDinner], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FestivalFever] = 축제의 열기 / Festive Fever; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Final Power +1 for every 5 [FestivalFever] on self or every 6 [Laceration] on the target (max 4)\n[WhenUse] At less than 15 [BloodDinner], gain 15 [Laceration] and immediately trigger it once, then reduce [Laceration] Count by 1 (at less than 10% HP, activate only the part of this effect where this unit gains [Laceration] Potency and Count)\n[EndSkill] Consume 15 [BloodDinner]
   PL: [WhenUse] Moc Końcowa +1 za każde 5 [FestivalFever] tej jednostki lub 6 [Laceration] celu (maks. 4)\n[WhenUse] przy mniej niż 15 [BloodDinner], zyskuje 15 [Laceration], natychmiast uruchamia je raz, po czym traci 1 Licznika [Laceration] (poniżej 10% HP uruchamia jedynie część efektu zyskującą Siłę i Licznik [Laceration])\n[EndSkill] zużywa 15 [BloodDinner]
208. [Umiejętność wroga [838103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 6당 [AttackUp] 1, [DefenseUp] 1 얻음 (각각 최대 3)
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [AttackUp], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 1 [AttackUp] and 1 [DefenseUp] for every 6 [Laceration] on the target (max 3 of each)
   PL: [OnSucceedAttack] zyskuje 1 [AttackUp] i 1 [DefenseUp] za każde 6 [Laceration] celu (po 3 maks.)
209. [Umiejętność wroga [838103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Umiejętność wroga [838103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [WinDuelAttack] [Laceration] 횟수 5 증가
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Laceration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuelAttack] Inflict +5 [Laceration] Count
   PL: [WinDuelAttack] nakłada 5 Licznika [Laceration]
211. [Umiejętność wroga [838103] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BloomingThorns] 3 얻음
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838103].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloomingThorns]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloomingThorns] = 피어나는 가시 / Blooming Thorn
   EN: [OnSucceedAttack] Gain 3 [BloomingThorns]
   PL: [OnSucceedAttack] zyskuje 3 [BloomingThorns]
212. [Umiejętność wroga [838104] (ulepszenie 1) — nazwa] 환상의 퍼레이드
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838104].levelList[level=1].name
   limit: do 40 znaków
   EN: Parade of Wonders
   PL: Parade of Wonders
213. [Umiejętność wroga [838104] (ulepszenie 1) — opis] [CantIdentify]\n메인 타겟은 적, 서브 타겟은 아군을 우선으로 지정하며, 대상이 아군이면 합 위력 +10, 피해량이 항상 0으로 고정\n[WhenUse] 자신의 [BloodDinner_Accumulation] 20당 합 위력 +1 (최대 10)\n[WhenUse] [BloodDinner]이 25 미만이면, [Laceration] 25를 얻은 다음 즉시 1회 발동시키고 [Laceration] 횟수 1 감소 (체력이 10% 미만이면 [Laceration], [Laceration] 횟수를 얻는 효과만 발동)\n[EndSkill] [BloodDinner] 25 소모\n[EndBattle] [FestivalFever]를 전부 소모
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838104].levelList[level=1].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WhenUse], [BloodDinner_Accumulation], [BloodDinner], [Laceration], [EndSkill], [EndBattle], [FestivalFever]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed; [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [EndBattle] = [턴 종료 시] / [Turn End]; [FestivalFever] = 축제의 열기 / Festive Fever
   EN: [CantIdentify]\nPrioritizes enemies for its main target, and prioritizes allies for its sub-targets. If the target is an ally, Clash Power +10 and always fix the damage to 0.\n[WhenUse] Clash Power +1 for every 20 [BloodDinner_Accumulation] by this unit (max 10)\n[WhenUse] At less than 25 [BloodDinner], gain 25 [Laceration], immediately trigger it once, then lose 1 [Laceration] Count (at less than 10% HP, activate only the part of this effect where this unit gains [Laceration] Potency and Count)\n[EndSkill] Consume 25 [BloodDinner]\n[EndBattle] Consume all [FestivalFever]
   PL: [CantIdentify]\npriorytet: wrogowie jako cel główny, sojusznicy jako cele poboczne; jeżeli celem jest sojusznik, Moc Starcia +10, a obrażenia są zawsze zerowe\n[WhenUse] Moc Starcia +1 za każde 20 [BloodDinner_Accumulation] tej jednostki (maks. 10)\n[WhenUse] przy mniej niż 25 [BloodDinner], zyskuje 25 [Laceration], natychmiast uruchamia je raz, po czym traci 1 Licznika [Laceration] (poniżej 10% HP uruchamia jedynie część efektu zyskującą Siłę i Licznik [Laceration])\n[EndSkill] zużywa 25 [BloodDinner]\n[EndBattle] zużywa całe [FestivalFever]
214. [Umiejętność wroga [838104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [FestivalFever]에 비례하여 다음 턴까지 [AttackUp] 1, [DefenseUp] 1 부여 ([FestivalFever] 3당 1 부여, 각각 최대 3)
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FestivalFever], [AttackUp], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FestivalFever] = 축제의 열기 / Festive Fever; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Inflict 1 [AttackUp] and [DefenseUp] until next turn based on [FestivalFever] (1 per 3 [FestivalFever], max 3 of each)
   PL: [OnSucceedAttack] nakłada 1 [AttackUp] i [DefenseUp] do następnej tury według [FestivalFever] (1 za każde 3 [FestivalFever], po 3 maks.)
215. [Umiejętność wroga [838104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Umiejętność wroga [838104] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가\n- 대상이 아군이면 이 효과를 대신하여 [BloomingThorns] 5 부여
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838104].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Laceration], [BloomingThorns]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [BloomingThorns] = 피어나는 가시 / Blooming Thorn
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count\n- If the target is an ally, replace this effect with 5 [BloomingThorns]
   PL: [OnSucceedAttack] nakłada 3 Licznika [Laceration]\n- jeżeli celem jest sojusznik, zamiast tego nakłada 5 [BloomingThorns]
217. [Umiejętność wroga [838105] (ulepszenie 1) — nazwa] 퍼레이드는 영원히 반복될거야
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838105].levelList[level=1].name
   limit: do 50 znaków
   EN: The Parade Repeats for Eternity
   PL: The Parade Repeats for Eternity
218. [Umiejętność wroga [838105] (ulepszenie 1) — opis] [WhenUse] 자신의 [BloodDinner_Accumulation] 20당 합 위력 +1 (최대 10)\n[WhenUse] [BloodDinner]이 50 미만이면, [Laceration] 25, [Laceration] 횟수 2를 얻은 다음 즉시 2회 발동시키고 [Laceration] 횟수 2 감소 (체력이 10% 미만이면 [Laceration], [Laceration] 횟수를 얻는 효과만 발동)\n[WhenUse] [BloodDinner]을 절반만큼 소모\n[EndBattle] [IncompleteParade]를 전부 소모\n[EndBattle] [FestivalFever] 10 얻음
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838105].levelList[level=1].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner_Accumulation], [BloodDinner], [Laceration], [EndBattle], [IncompleteParade], [FestivalFever]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed; [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed; [EndBattle] = [턴 종료 시] / [Turn End]; [IncompleteParade] = 불완전한 퍼레이드 / Imperfect Parade; [FestivalFever] = 축제의 열기 / Festive Fever
   EN: [WhenUse] Clash Power +1 for every 20 [BloodDinner_Accumulation] by this unit (max 10)\n[WhenUse] At less than 50 [BloodDinner], gain 25 [Laceration], +2 [Laceration] Count, immediately trigger it twice, then reduce [Laceration] Count by 2 (at less than 10% HP, activate only the part of this effect where this unit gains [Laceration] Potency and Count)\n[WhenUse] Consume half of [BloodDinner]\n[EndBattle] Consume all [IncompleteParade]\n[EndBattle] Gain 10 [FestivalFever]
   PL: [WhenUse] Moc Starcia +1 za każde 20 [BloodDinner_Accumulation] tej jednostki (maks. 10)\n[WhenUse] przy mniej niż 50 [BloodDinner], zyskuje 25 [Laceration] i 2 Licznika [Laceration], natychmiast uruchamia je 2 razy, po czym traci 2 Licznika [Laceration] (poniżej 10% HP uruchamia jedynie część efektu zyskującą Siłę i Licznik [Laceration])\n[WhenUse] zużywa połowę [BloodDinner]\n[EndBattle] zużywa całe [IncompleteParade]\n[EndBattle] zyskuje 10 [FestivalFever]
219. [Umiejętność wroga [838105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 입힌 피해량의 25%만큼 체력 회복
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal by 25% of damage dealt
   PL: [OnSucceedAttack] przywraca HP równe 25% zadanych obrażeń
220. [Umiejętność wroga [838105] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 입힌 피해량의 25%만큼 체력 회복
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838105].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność wroga [838105] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838105].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Umiejętność wroga [838105] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 입힌 피해량의 50%만큼 체력 회복
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838105].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal by 50% of damage dealt
   PL: [OnSucceedAttack] przywraca HP równe 50% zadanych obrażeń
223. [Umiejętność wroga [838105] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Laceration] 5, [Burst] 5 부여
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838105].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and 5 [Burst]
   PL: [OnSucceedAttack] nakłada 5 [Laceration] i 5 [Burst]
224. [Umiejętność wroga [838105] (ulepszenie 1) — moneta 3, efekt 4 — opis] [EndCoin] 이 스킬로 소모한 [BloodDinner] 10당 [BloomingThorns] 1 얻음 (최대 10)
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838105].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [BloodDinner], [BloomingThorns]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [BloodDinner] = 혈찬 / Bloodfeast; [BloomingThorns] = 피어나는 가시 / Blooming Thorn
   EN: [EndCoin] Gain 1 [BloomingThorns] for every 10 [BloodDinner] consumed by this Skill (max 10)
   PL: [EndCoin] zyskuje 1 [BloomingThorns] za każde 10 [BloodDinner] zużytych przez tę Umiejętność (maks. 10)
225. [Umiejętność wroga [838106] (ulepszenie 1) — nazwa] 그걸 반복할 뿐...
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838106].levelList[level=1].name
   limit: do 40 znaków
   EN: And that's all it does...
   PL: And that's all it does...
226. [Umiejętność wroga [838106] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 자신의 [FestivalFever]가 5 이상이면 합 위력 +3\n[StartBattle] [BloomingThorns] 5 얻음\n[DefeatDuel] [BloomingThorns] 5 잃음
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838106].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [FestivalFever], [StartBattle], [BloomingThorns], [DefeatDuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [FestivalFever] = 축제의 열기 / Festive Fever; [StartBattle] = [전투 시작시] / [Combat Start]; [BloomingThorns] = 피어나는 가시 / Blooming Thorn; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DuelCounter]\n[WhenUse] At 5+ [FestivalFever], Clash Power +3\n[StartBattle] Gain 5 [BloomingThorns]\n[DefeatDuel] Lose 5 [BloomingThorns]
   PL: [DuelCounter]\n[WhenUse] przy 5+ [FestivalFever], Moc Starcia +3\n[StartBattle] zyskuje 5 [BloomingThorns]\n[DefeatDuel] traci 5 [BloomingThorns]
227. [Umiejętność wroga [838106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
228. [Umiejętność wroga [838106] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838106].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Umiejętność wroga [838107] (ulepszenie 1) — nazwa] 피날레
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838107].levelList[level=1].name
   limit: do 40 znaków
   EN: The Finale
   PL: The Finale
230. [Umiejętność wroga [838107] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 절반만큼 소모\n[WinDuel] 피해량이 (이 스킬로 소모한 [BloodDinner])%만큼 증가 (최대 150%)\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] 정신력 -45로 감소
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838107].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [WinDuel], [DefeatDuel], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Consume half of [BloodDinner]\n[WinDuel] Deal +([BloodDinner] consumed by this Skill)% damage (max 150%)\n[DefeatDuel] Deal -50% damage, and the damage from this Skill does not Stagger the target\n[EndSkill] This unit's SP drops to -45
   PL: [WhenUse] zużywa połowę [BloodDinner]\n[WinDuel] zadaje +([BloodDinner] zużyte przez tę Umiejętność)% obrażeń (maks. 150%)\n[DefeatDuel] zadaje -50% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu\n[EndSkill] SP tej jednostki spada do -45
231. [Umiejętność wroga [838107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Umiejętność wroga [838107] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838107].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]
   PL: [OnSucceedAttack] nakłada 6 [Laceration]
233. [Umiejętność wroga [838107] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 6 증가
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838107].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +6 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 6 Licznika [Laceration]
234. [Umiejętność wroga [838107] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838107].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność wroga [838107] (ulepszenie 1) — moneta 2, efekt 2 — opis] [WinDuelAttack] [Burst] 6 부여
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838107].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Burst]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Burst] = 파열 / Rupture
   EN: [WinDuelAttack] Inflict 6 [Burst]
   PL: [WinDuelAttack] nakłada 6 [Burst]
236. [Umiejętność wroga [838107] (ulepszenie 1) — moneta 2, efekt 3 — opis] [WinDuelAttack] [Burst] 횟수 6 증가
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838107].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Burst]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Burst] = 파열 / Rupture
   EN: [WinDuelAttack] Inflict +6 [Burst] Count
   PL: [WinDuelAttack] nakłada 6 Licznika [Burst]
237. [Umiejętność wroga [838107] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838107].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [Umiejętność wroga [838107] (ulepszenie 1) — moneta 3, efekt 2 — opis] [EndCoin] 이 스킬로 소모한 [BloodDinner] 10당 [BloomingThorns] 1 얻음 (최대 10)
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838107].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [Umiejętność wroga [838901] (ulepszenie 1) — nazwa] 샘의 용
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838901].levelList[level=1].name
   limit: do 40 znaków
   EN: Dragon of the Spring
   PL: Dragon of the Spring
240. [Umiejętność wroga [838901] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility] 2 얻음
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste
   EN: [WhenUse] Gain 2 [Agility] next turn
   PL: [WhenUse] zyskuje 2 [Agility] w następnej turze
241. [Umiejętność wroga [838901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 1 [Agility] next turn
   PL: [OnSucceedAttack] zyskuje 1 [Agility] w następnej turze
242. [Umiejętność wroga [838901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 2 [Vulnerable] w następnej turze
243. [Umiejętność wroga [838902] (ulepszenie 1) — nazwa] 가을 연꽃
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838902].levelList[level=1].name
   limit: do 40 znaków
   EN: Lotus in Autumn
   PL: Lotus in Autumn
244. [Umiejętność wroga [838902] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility] 2 얻음
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838902].levelList[level=1].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Umiejętność wroga [838902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Umiejętność wroga [838902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 242 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność wroga [838903] (ulepszenie 1) — nazwa] 흐릿한 궤적
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838903].levelList[level=1].name
   limit: do 40 znaków
   EN: Faint Trace
   PL: Faint Trace
248. [Umiejętność wroga [838903] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility] 3 얻음
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838903].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste
   EN: [WhenUse] Gain 3 [Agility] next turn
   PL: [WhenUse] zyskuje 3 [Agility] w następnej turze
249. [Umiejętność wroga [838903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Umiejętność wroga [838903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [SlashTakeDamageUp] 3 부여
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttack] Inflict 3 [SlashTakeDamageUp]
   PL: [OnSucceedAttack] nakłada 3 [SlashTakeDamageUp]
251. [Umiejętność wroga [838904] (ulepszenie 1) — nazwa] 창백한 궤적
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838904].levelList[level=1].name
   limit: do 40 znaków
   EN: Pallid Trace
   PL: Pallid Trace
252. [Umiejętność wroga [838904] (ulepszenie 1) — opis] 대상보다 속도가 5 이상 빠르면, 합 위력 +5
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838904].levelList[level=1].desc
   limit: do 120 znaków
   EN: If user's Speed is faster than target's by 5+, Clash Power +5
   PL: jeżeli Szybkość tej jednostki jest wyższa od Szybkości celu o 5 lub więcej, Moc Starcia +5
253. [Umiejętność wroga [838904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Umiejętność wroga [838904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 추가 피해 100
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 100 Bonus Damage
   PL: [OnSucceedAttack] zadaje 100 dodatkowych obrażeń
255. [Umiejętność wroga [838905] (ulepszenie 1) — nazwa] 붉은살
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838905].levelList[level=1].name
   limit: do 40 znaków
   EN: Red Arwe
   PL: Red Arwe
256. [Umiejętność wroga [838905] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility] 2 얻음
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838905].levelList[level=1].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Umiejętność wroga [838905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 추가 피해 50
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 50 Bonus Damage
   PL: [OnSucceedAttack] zadaje 50 dodatkowych obrażeń
258. [Umiejętność wroga [838905] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 추가 피해 50
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838905].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 257 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Umiejętność wroga [838906] (ulepszenie 1) — nazwa] 검은살
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838906].levelList[level=1].name
   limit: do 40 znaków
   EN: Blak Arwe
   PL: Blak Arwe
260. [Umiejętność wroga [838906] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility] 2 얻음
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838906].levelList[level=1].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Umiejętność wroga [838906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [MentalCrack] 2 부여
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MentalCrack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MentalCrack] = 정신 균열 / Mental Fracture
   EN: [OnSucceedAttack] Inflict 2 [MentalCrack]
   PL: [OnSucceedAttack] nakłada 2 [MentalCrack]
262. [Umiejętność wroga [838906] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MentalCrack] 2 부여
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838906].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 261 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Umiejętność wroga [838907] (ulepszenie 1) — nazwa] 물의 거울
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838907].levelList[level=1].name
   limit: do 40 znaków
   EN: Mirror of Water
   PL: Mirror of Water
264. [Umiejętność wroga [838907] (ulepszenie 1) — opis] [CanDuelGuard]\n[WhenUse] [Protection] 3 얻음\n[WinDuel] 이 스킬의 마지막 합 위력만큼 체력 피해를 입힘
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838907].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WhenUse], [Protection], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n[WhenUse] Gain 3 [Protection]\n[WinDuel] Deal HP damage equal to the final Clash Power of this Skill
   PL: [CanDuelGuard]\n[WhenUse] zyskuje 3 [Protection]\n[WinDuel] zadaje obrażenia HP równe końcowej Mocy Starcia tej Umiejętności
265. [Umiejętność wroga [838907] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838907].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Umiejętność wroga [838908] (ulepszenie 1) — nazwa] 전자가속 레일 활성화
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838908].levelList[level=1].name
   limit: do 50 znaków
   EN: Electron Accelerator Rail Activation
   PL: Electron Accelerator Rail Activation
267. [Umiejętność wroga [838908] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 [Enhancement] 10, [Agility] 10 얻음
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838908].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Enhancement], [Agility]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Agility] = 신속 / Haste
   EN: [StartBattle] Gain 10 [Enhancement] and [Agility] next turn
   PL: [StartBattle] zyskuje 10 [Enhancement] i 10 [Agility] w następnej turze
268. [Umiejętność wroga [838909] (ulepszenie 1) — nazwa] 살
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838909].levelList[level=1].name
   limit: do 40 znaków
   EN: Arwe
   PL: Arwe
269. [Umiejętność wroga [838909] (ulepszenie 1) — opis] [WhenUse] [PenetrateDamageUp] 5 얻음
   źródło: Skills_Abnormality-a1c7p2.json :: dataList[id=838909].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [PenetrateDamageUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: [WhenUse] Gain 5 [PenetrateDamageUp]
   PL: [WhenUse] zyskuje 5 [PenetrateDamageUp]

## [a1c7p2] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c7p2
- grupa rozdziału/trybu: `a1c7p2` · plik: `Skills_Enemy-a1c7p2.json`

270. [Umiejętność wroga [9015801] (ulepszenie 1) — nazwa] 경혈식 내려치기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015801].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Slam
   PL: Hardblood Slam
271. [Umiejętność wroga [9015801] (ulepszenie 1) — opis] [WhenUse] 자신에게 [HardenedBlood]이 있고 이 스킬의 코인에 [Burst]을 부여하는 효과가 있으면, 추가로 [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015801].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [HardenedBlood], [Burst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [Burst] = 파열 / Rupture; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If this unit has [HardenedBlood], and if this Skill's Coin effect inflicts [Burst], inflict +1 [Laceration] Count as well
   PL: [WhenUse] jeżeli ta jednostka ma [HardenedBlood] i efekt Monety tej Umiejętności nakłada [Burst], dodatkowo nakłada 1 Licznika [Laceration]
272. [Umiejętność wroga [9015801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Umiejętność wroga [9015801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Umiejętność wroga [9015802] (ulepszenie 1) — nazwa] 목적 잃은 분노
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015802].levelList[level=1].name
   limit: do 40 znaków
   EN: Aimless Wrath
   PL: Aimless Wrath
275. [Umiejętność wroga [9015802] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1\n[WhenUse] 자신에게 [HardenedBlood]이 3 이상 있고 이 스킬의 코인에 [Burst]을 부여하는 효과가 있으면, 추가로 [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015802].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [HardenedBlood], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 5+ [Laceration], Coin Power +1\n[WhenUse] If this unit has 3+ [HardenedBlood], and if this Skill's Coin effect inflicts [Burst], inflict 2 [Laceration] as well
   PL: [WhenUse] jeżeli cel ma 5+ [Laceration], Moc Monety +1\n[WhenUse] jeżeli ta jednostka ma 3+ [HardenedBlood] i efekt Monety tej Umiejętności nakłada [Burst], dodatkowo nakłada 2 [Laceration]
276. [Umiejętność wroga [9015802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Umiejętność wroga [9015802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Umiejętność wroga [9015802] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Umiejętność wroga [9015802] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있으면, [HardenedBlood] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015802].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [HardenedBlood]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [OnSucceedAttack] If target has [Laceration], gain 1 [HardenedBlood]
   PL: [OnSucceedAttack] jeżeli cel ma [Laceration], zyskuje 1 [HardenedBlood]
280. [Umiejętność wroga [9015803] (ulepszenie 1) — nazwa] 무절제한 내려찍기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015803].levelList[level=1].name
   limit: do 40 znaków
   EN: Unbridled Smite
   PL: Unbridled Smite
281. [Umiejętność wroga [9015803] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015803].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 5+ [Laceration], Coin Power +1
   PL: [WhenUse] jeżeli cel ma 5+ [Laceration], Moc Monety +1
282. [Umiejętność wroga [9015803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność wroga [9015803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Umiejętność wroga [9015803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Umiejętność wroga [9015803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Umiejętność wroga [9015803] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015803].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Umiejętność wroga [9015803] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10 이상이면, 피해량 +20%
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015803].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 10+ [Laceration], deal +20% damage
   PL: [OnSucceedAttack] jeżeli cel ma 10+ [Laceration], zadaje +20% obrażeń
288. [Umiejętność wroga [9015804] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015804].levelList[level=1].name
   limit: do 40 znaków
   EN: Guard
   PL: Guard
289. [Umiejętność wroga [9015804] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Laceration]이 있다면, [HardenedBlood] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration], [HardenedBlood]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [WhenUse] If target has [Laceration], gain 1 [HardenedBlood]
   PL: [WhenUse] jeżeli cel ma [Laceration], zyskuje 1 [HardenedBlood]
290. [Umiejętność wroga [9015901] (ulepszenie 1) — nazwa] 경혈식 내려치기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015901].levelList[level=1].name
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Umiejętność wroga [9015901] (ulepszenie 1) — opis] [WhenUse] 자신에게 [HardenedBlood]이 있고 이 스킬의 코인에 [Burst]을 부여하는 효과가 있으면, 추가로 [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015901].levelList[level=1].desc
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Umiejętność wroga [9015901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Umiejętność wroga [9015901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 1 Licznika [Laceration]
294. [Umiejętność wroga [9015902] (ulepszenie 1) — nazwa] 목적 잃은 분노
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015902].levelList[level=1].name
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Umiejętność wroga [9015902] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1\n[WhenUse] 자신에게 [HardenedBlood]이 3 이상 있고 이 스킬의 코인에 [Burst]을 부여하는 효과가 있으면, 추가로 [Laceration] 1 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015902].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [HardenedBlood], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 5+ [Laceration], Coin Power +1\n[WhenUse] If this unit has 3+ [HardenedBlood], and if this Skill's Coin effect inflicts [Burst], inflict +1 [Laceration] Count as well
   PL: [WhenUse] jeżeli cel ma 5+ [Laceration], Moc Monety +1\n[WhenUse] jeżeli ta jednostka ma 3+ [HardenedBlood] i efekt Monety tej Umiejętności nakłada [Burst], dodatkowo nakłada 1 Licznika [Laceration]
296. [Umiejętność wroga [9015902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Umiejętność wroga [9015902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Umiejętność wroga [9015902] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność wroga [9015902] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Laceration]이 있으면, [HardenedBlood] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015902].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Umiejętność wroga [9015903] (ulepszenie 1) — nazwa] 무절제한 내려찍기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015903].levelList[level=1].name
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [Umiejętność wroga [9015903] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015903].levelList[level=1].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Umiejętność wroga [9015903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Umiejętność wroga [9015903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Umiejętność wroga [9015903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Umiejętność wroga [9015903] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015903].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Umiejętność wroga [9015903] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015903].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Umiejętność wroga [9015903] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10 이상이면, 피해량 +20%
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015903].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 287 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Umiejętność wroga [9015904] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015904].levelList[level=1].name
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Umiejętność wroga [9015904] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Laceration]이 있다면, [HardenedBlood] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9015904].levelList[level=1].desc
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Umiejętność wroga [9016901] (ulepszenie 1) — nazwa] 경혈식 후려치기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016901].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Thrash
   PL: Hardblood Thrash
311. [Umiejętność wroga [9016901] (ulepszenie 1) — opis] [DefeatDuel] [Laceration] 10, [Laceration] 횟수 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel], [Laceration]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [Laceration] = 출혈 / Bleed
   EN: [DefeatDuel] Gain 10 [Laceration] and +1 [Laceration] Count
   PL: [DefeatDuel] zyskuje 10 [Laceration] i 1 Licznika [Laceration]
312. [Umiejętność wroga [9016901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [Umiejętność wroga [9016901] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 10 과 [BloodyHand] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016901].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [BloodyHand]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [BloodyHand] = 피로 물든 손 / Bloodied Hand
   EN: [OnSucceedAttack] Gain 10 [Laceration] and 1 [BloodyHand]
   PL: [OnSucceedAttack] zyskuje 10 [Laceration] i 1 [BloodyHand]
314. [Umiejętność wroga [9016902] (ulepszenie 1) — nazwa] 경혈식 휘두르기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016902].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Lash
   PL: Hardblood Lash
315. [Umiejętność wroga [9016902] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 8 이상이면, 피해량 +20%
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 8+ [Laceration], deal +20% damage
   PL: [WhenUse] jeżeli cel ma 8+ [Laceration], zadaje +20% obrażeń
316. [Umiejętność wroga [9016902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Umiejętność wroga [9016902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Umiejętność wroga [9016902] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 6 이상이면, [HardenedBlood] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [HardenedBlood]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [OnSucceedAttack] If target has 6+ [Laceration], gain 1 [HardenedBlood]
   PL: [OnSucceedAttack] jeżeli cel ma 6+ [Laceration], zyskuje 1 [HardenedBlood]
319. [Umiejętność wroga [9016902] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Umiejętność wroga [9016902] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 20과 [BloodyHand] 2 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016902].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [BloodyHand]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [BloodyHand] = 피로 물든 손 / Bloodied Hand
   EN: [OnSucceedAttack] Gain 20 [Laceration] and 2 [BloodyHand]
   PL: [OnSucceedAttack] zyskuje 20 [Laceration] i 2 [BloodyHand]
321. [Umiejętność wroga [9016903] (ulepszenie 1) — nazwa] 경혈식 강화 타격
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016903].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Strike
   PL: Hardblood Strike
322. [Umiejętność wroga [9016903] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 기본 위력 +1\n[WhenUse] 이 스킬로 대상에게 [Laceration]을 부여할 때, 자신의 [HardenedBlood] 만큼 [Burst]을 추가로 부여\n[EndSkill] [HardenedBlood], [BloodyHand] 전부 소모
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016903].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [HardenedBlood], [Burst], [EndSkill], [BloodyHand]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [Burst] = 파열 / Rupture; [EndSkill] = [공격 종료시] / [Attack End]; [BloodyHand] = 피로 물든 손 / Bloodied Hand
   EN: [WhenUse] If target has 6+ [Laceration], Base Power +1\n[WhenUse] When inflicting [Laceration] with this Skill, inflict [Burst] equal to [HardenedBlood] on self as well\n[EndSkill] Consume all [HardenedBlood] and [BloodyHand]
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Bazowa +1\n[WhenUse] nakładając [Laceration] tą Umiejętnością, dodatkowo nakłada na siebie [Burst] w wysokości własnego [HardenedBlood]\n[EndSkill] zużywa całe [HardenedBlood] i [BloodyHand]
323. [Umiejętność wroga [9016903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Umiejętność wroga [9016903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Umiejętność wroga [9016903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 (대상의 [Laceration])% 만큼 체력 회복 (최대 20%)
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Heal ([Laceration] on target)% HP (max 20%)
   PL: [OnSucceedAttack] przywraca HP równe ([Laceration] celu)% Maks. HP (maks. 20%)
326. [Umiejętność wroga [9016904] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016904].levelList[level=1].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Umiejętność wroga [9016904] (ulepszenie 1) — opis] [WhenUse] 자신의 [HardenedBlood] 1 당, 기본 위력 +1
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [HardenedBlood]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [WhenUse] Base Power +1 for every [HardenedBlood] on self
   PL: [WhenUse] Moc Bazowa +1 za każde [HardenedBlood] tej jednostki
328. [Umiejętność wroga [9016904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9016904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 2 [Laceration]
   PL: [OnSucceedAttackHead] nakłada 2 [Laceration]
329. [Umiejętność wroga [9017001] (ulepszenie 1) — nazwa] 경혈식 후려치기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017001].levelList[level=1].name
   (powtórzenie elementu 310 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Umiejętność wroga [9017001] (ulepszenie 1) — opis] [DefeatDuel] [Laceration] 10, [Laceration] 횟수 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017001].levelList[level=1].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Umiejętność wroga [9017001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Umiejętność wroga [9017001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 10과 [BloodyHand] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [BloodyHand]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [BloodyHand] = 피로 물든 손 / Bloodied Hand
   EN: [OnSucceedAttack] Gain 10 [Laceration] and 1 [BloodyHand]
   PL: [OnSucceedAttack] zyskuje 10 [Laceration] i 1 [BloodyHand]
333. [Umiejętność wroga [9017002] (ulepszenie 1) — nazwa] 경혈식 휘두르기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017002].levelList[level=1].name
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Umiejętność wroga [9017002] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 4 이상이면, 피해량 +10%
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017002].levelList[level=1].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Umiejętność wroga [9017002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Umiejętność wroga [9017002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Umiejętność wroga [9017002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 6 이상이면, [HardenedBlood] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Umiejętność wroga [9017002] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Umiejętność wroga [9017002] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 20과 [BloodyHand] 2 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017002].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Umiejętność wroga [9017003] (ulepszenie 1) — nazwa] 경혈식 강화 타격
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017003].levelList[level=1].name
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Umiejętność wroga [9017003] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 기본 위력 +1\n[WhenUse] 이 스킬로 대상에게 [Laceration]을 부여할 때, 자신의 [HardenedBlood] 만큼 [Burst]을 추가로 부여\n[EndSkill] [HardenedBlood], [BloodyHand] 전부 소모
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017003].levelList[level=1].desc
   (powtórzenie elementu 322 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Umiejętność wroga [9017003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Umiejętność wroga [9017003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Umiejętność wroga [9017003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 (대상의 [Laceration])% 만큼 체력 회복 (최대 20%)
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Umiejętność wroga [9017004] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017004].levelList[level=1].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Umiejętność wroga [9017004] (ulepszenie 1) — opis] [WhenUse] 자신의 [HardenedBlood] 1 당, 기본 위력 +1
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017004].levelList[level=1].desc
   (powtórzenie elementu 327 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [Umiejętność wroga [9017004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 328 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Umiejętność wroga [9017101] (ulepszenie 1) — nazwa] 질문에 답을 해 주세요.
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017101].levelList[level=1].name
   limit: do 40 znaków
   EN: Please answer the survey.
   PL: Please answer the survey.
349. [Umiejętność wroga [9017101] (ulepszenie 1) — opis] [WhenUse] [Laceration] 5, [Laceration] 횟수 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Gain 5 [Laceration] and +1 [Laceration] Count
   PL: [WhenUse] zyskuje 5 [Laceration] i 1 Licznika [Laceration]
350. [Umiejętność wroga [9017101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Umiejętność wroga [9017101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Umiejętność wroga [9017102] (ulepszenie 1) — nazwa] 말 끊지 마세요!
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017102].levelList[level=1].name
   limit: do 40 znaków
   EN: Don't! Don't Cut Me Off!
   PL: Don't! Don't Cut Me Off!
353. [Umiejętność wroga [9017102] (ulepszenie 1) — opis] [WhenUse] [Laceration] 5, [Laceration] 횟수 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017102].levelList[level=1].desc
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Umiejętność wroga [9017102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Umiejętność wroga [9017102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 5 이상이면, [BloodyHand] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [BloodyHand]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [BloodyHand] = 피로 물든 손 / Bloodied Hand
   EN: [OnSucceedAttack] If target has 5+ [Laceration], gain 1 [BloodyHand]
   PL: [OnSucceedAttack] jeżeli cel ma 5+ [Laceration], zyskuje 1 [BloodyHand]
356. [Umiejętność wroga [9017103] (ulepszenie 1) — nazwa] 빛바랜 인내
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017103].levelList[level=1].name
   limit: do 40 znaków
   EN: Faded Patience
   PL: Faded Patience
357. [Umiejętność wroga [9017103] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10 당 [BloodyHand] 1 얻음\n[WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017103].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodyHand], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodyHand] = 피로 물든 손 / Bloodied Hand; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Consume up to 50 [BloodDinner]; gain 1 [BloodyHand] for every 10 [BloodDinner] consumed\n[WhenUse] If target has 5+ [Laceration], Coin Power +1
   PL: [WhenUse] zużywa do 50 [BloodDinner]; zyskuje 1 [BloodyHand] za każde 10 zużytych [BloodDinner]\n[WhenUse] jeżeli cel ma 5+ [Laceration], Moc Monety +1
358. [Umiejętność wroga [9017103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Umiejętność wroga [9017103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [EndSkill] 이 스킬에서 [BloodDinner]을 소모하지 못했으면, [Laceration] 10, [BloodyHand] 1 얻음.
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [BloodDinner], [Laceration], [BloodyHand]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed; [BloodyHand] = 피로 물든 손 / Bloodied Hand
   EN: [EndSkill] If this unit failed to consume [BloodDinner] with this Skill, gain 10 [Laceration] and 1 [BloodyHand].
   PL: [EndSkill] jeżeli ta Umiejętność nie zużyła [BloodDinner], zyskuje 10 [Laceration] i 1 [BloodyHand].
360. [Umiejętność wroga [9017104] (ulepszenie 1) — nazwa] 끝없는 고해
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017104].levelList[level=1].name
   limit: do 40 znaków
   EN: Endless Atonement
   PL: Endless Atonement
361. [Umiejętność wroga [9017104] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [HardenedBlood] 1 당, 합 위력 +1\n[DefeatDuel] [BloodyHand] 2 감소
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017104].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [HardenedBlood], [DefeatDuel], [BloodyHand]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [DefeatDuel] = [합 패배] / [Clash Lose]; [BloodyHand] = 피로 물든 손 / Bloodied Hand
   EN: [WhenUse] If target has 5+ [Laceration], Coin Power +1\n[WhenUse] Clash Power +1 for every [HardenedBlood] on self\n[DefeatDuel] Lose 2 [BloodyHand]
   PL: [WhenUse] jeżeli cel ma 5+ [Laceration], Moc Monety +1\n[WhenUse] Moc Starcia +1 za każde [HardenedBlood] tej jednostki\n[DefeatDuel] traci 2 [BloodyHand]
362. [Umiejętność wroga [9017104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Umiejętność wroga [9017104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Umiejętność wroga [9017104] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [BloodyHand]을 전부 소모하여, 대상의 [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017104].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloodyHand], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodyHand] = 피로 물든 손 / Bloodied Hand; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Consume all [BloodyHand] to inflict +3 [Laceration]
   PL: [OnSucceedAttack] zużywa całe [BloodyHand], by nałożyć 3 Licznika [Laceration]
365. [Umiejętność wroga [9017104] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [HardenedBlood]을 모두 소모하여, (소모한 [HardenedBlood] x 3) 만큼 [BloodDinner]이 증가하고, [Laceration] 5 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017104].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [HardenedBlood], [BloodDinner], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Consume all [HardenedBlood] on self to increase [BloodDinner] by (consumed [HardenedBlood] x 3) and gain 5 [Laceration]
   PL: [OnSucceedAttack] zużywa całe własne [HardenedBlood], zwiększa [BloodDinner] o (zużyte [HardenedBlood] x 3) i zyskuje 5 [Laceration]
366. [Umiejętność wroga [9017104] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 최대 체력의 (대상의 [Laceration])% 만큼 체력 회복 (최대 30%)
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017104].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Heal ([Laceration] on target)% HP (max 30%)
   PL: [OnSucceedAttack] przywraca HP równe ([Laceration] celu)% Maks. HP (maks. 30%)
367. [Umiejętność wroga [9017105] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017105].levelList[level=1].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Umiejętność wroga [9017105] (ulepszenie 1) — opis] [WhenUse] [BloodyHand]이 1 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [HardenedBlood]이 3 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017105].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodyHand], [HardenedBlood]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodyHand] = 피로 물든 손 / Bloodied Hand; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [WhenUse] At 1+ [BloodyHand], Base Power +1\n[WhenUse] At 3+ [HardenedBlood], Coin Power +1
   PL: [WhenUse] przy 1+ [BloodyHand], Moc Bazowa +1\n[WhenUse] przy 3+ [HardenedBlood], Moc Monety +1
369. [Umiejętność wroga [9017105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Umiejętność wroga [9017201] (ulepszenie 1) — nazwa] 질문에 답을 해 주세요.
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017201].levelList[level=1].name
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Umiejętność wroga [9017201] (ulepszenie 1) — opis] [WhenUse] [Laceration] 5, [Laceration] 횟수 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017201].levelList[level=1].desc
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Umiejętność wroga [9017201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Umiejętność wroga [9017201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Umiejętność wroga [9017202] (ulepszenie 1) — nazwa] 말 끊지 마세요!
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017202].levelList[level=1].name
   (powtórzenie elementu 352 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [Umiejętność wroga [9017202] (ulepszenie 1) — opis] [WhenUse] [Laceration] 5, [Laceration] 횟수 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017202].levelList[level=1].desc
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Umiejętność wroga [9017202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Laceration]
377. [Umiejętność wroga [9017202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 5 이상이면, [BloodyHand] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Umiejętność wroga [9017203] (ulepszenie 1) — nazwa] 빛바랜 인내
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017203].levelList[level=1].name
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Umiejętność wroga [9017203] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10 당 [BloodyHand] 1 얻음\n[WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017203].levelList[level=1].desc
   (powtórzenie elementu 357 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Umiejętność wroga [9017203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [Umiejętność wroga [9017203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [EndSkill] 이 스킬에서 [BloodDinner]을 소모하지 못했으면, [Laceration] 10, [BloodyHand] 1 얻음.
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 359 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Umiejętność wroga [9017204] (ulepszenie 1) — nazwa] 끝없는 고해
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017204].levelList[level=1].name
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Umiejętność wroga [9017204] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [HardenedBlood] 1 당, 합 위력 +1\n[DefeatDuel] [BloodyHand] 2 감소
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017204].levelList[level=1].desc
   (powtórzenie elementu 361 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Umiejętność wroga [9017204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Umiejętność wroga [9017204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Umiejętność wroga [9017204] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [BloodyHand]을 전부 소모하여, 대상의 [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017204].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Umiejętność wroga [9017204] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [HardenedBlood]을 모두 소모하여, (소모한 [HardenedBlood] x 3) 만큼 [BloodDinner]이 증가하고, [Laceration] 5 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017204].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 365 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Umiejętność wroga [9017204] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 최대 체력의 (대상의 [Laceration])% 만큼 체력 회복 (최대 30%)
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017204].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność wroga [9017205] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017205].levelList[level=1].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Umiejętność wroga [9017205] (ulepszenie 1) — opis] [WhenUse] [BloodyHand]이 1 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [HardenedBlood]이 3 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017205].levelList[level=1].desc
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Umiejętność wroga [9017205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Umiejętność wroga [9017301] (ulepszenie 1) — nazwa] 경혈식 내려베기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017301].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Downward Cut
   PL: Hardblood Downward Cut
393. [Umiejętność wroga [9017301] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever]가 5 이상이면, 최종 위력 +1
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [FestivalFever]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FestivalFever] = 축제의 열기 / Festive Fever
   EN: [WhenUse] At 5+ [FestivalFever], Final Power +1
   PL: [WhenUse] przy 5+ [FestivalFever], Moc Końcowa +1
394. [Umiejętność wroga [9017301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 [Laceration] i 2 Licznika [Laceration]
395. [Umiejętność wroga [9017301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Burst] 2 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 2 [Burst]
   PL: [OnSucceedAttackHead] nakłada 2 [Burst]
396. [Umiejętność wroga [9017302] (ulepszenie 1) — nazwa] 경혈식 깎아내기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017302].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Carve
   PL: Hardblood Carve
397. [Umiejętność wroga [9017302] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever] 5 또는 대상의 [Laceration] 6당 최종 위력 +1 (최대 2)\n[WhenUse] [Laceration] 15를 얻은 다음 즉시 1회 발동시키고 [Laceration] 횟수 1 감소
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017302].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [FestivalFever], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FestivalFever] = 축제의 열기 / Festive Fever; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Final Power +1 for every 5 [FestivalFever] on self or every 6 [Laceration] on the target (max 2)\n[WhenUse] Gain 15 [Laceration], immediately trigger it once, and reduce [Laceration] Count by 1
   PL: [WhenUse] Moc Końcowa +1 za każde 5 [FestivalFever] tej jednostki lub 6 [Laceration] celu (maks. 2)\n[WhenUse] zyskuje 15 [Laceration], natychmiast uruchamia je raz i traci 1 Licznika [Laceration]
398. [Umiejętność wroga [9017302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 6 이상이면, [HardenedBlood] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Umiejętność wroga [9017302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 [Laceration] i 2 Licznika [Laceration]
400. [Umiejętność wroga [9017302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloomingThorns] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloomingThorns]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloomingThorns] = 피어나는 가시 / Blooming Thorn
   EN: [OnSucceedAttack] Gain 1 [BloomingThorns]
   PL: [OnSucceedAttack] zyskuje 1 [BloomingThorns]
401. [Umiejętność wroga [9017303] (ulepszenie 1) — nazwa] 경혈식 강화 펼치기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017303].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Power Unfurling
   PL: Hardblood Power Unfurling
402. [Umiejętność wroga [9017303] (ulepszenie 1) — opis] [WhenUse] [Laceration] 15, [Laceration] 횟수 2를 얻음 다음 즉시 2회 발동시키고 [Laceration] 횟수 2 감소\n[EndBattle] [HardenedBlood], [FestivalFever] 전부 소모
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017303].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [EndBattle], [HardenedBlood], [FestivalFever]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [EndBattle] = [턴 종료 시] / [Turn End]; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [FestivalFever] = 축제의 열기 / Festive Fever
   EN: [WhenUse] Gain 15 [Laceration] and +2 [Laceration] Count, immediately trigger it twice, then reduce [Laceration] Count by 2\n[EndBattle] Consume all [HardenedBlood] and [FestivalFever]
   PL: [WhenUse] zyskuje 15 [Laceration] i 2 Licznika [Laceration], natychmiast uruchamia je 2 razy, po czym traci 2 Licznika [Laceration]\n[EndBattle] zużywa całe [HardenedBlood] i [FestivalFever]
403. [Umiejętność wroga [9017303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [HardenedBlood]만큼 [Laceration], [Burst] 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [HardenedBlood], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict [Laceration] and [Burst] equal to [HardenedBlood] on self
   PL: [OnSucceedAttack] nakłada na siebie [Laceration] i [Burst] w wysokości własnego [HardenedBlood]
404. [Umiejętność wroga [9017303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 ([FestivalFever] x 2.5)%만큼 체력 회복 (최대 20%)
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FestivalFever]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FestivalFever] = 축제의 열기 / Festive Fever
   EN: [OnSucceedAttack] Heal ([FestivalFever] x 2.5)% HP (max 20%)
   PL: [OnSucceedAttack] przywraca HP równe ([FestivalFever] x 2.5)% Maks. HP (maks. 20%)
405. [Umiejętność wroga [9017303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [FestivalFever] 2 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FestivalFever]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FestivalFever] = 축제의 열기 / Festive Fever
   EN: [OnSucceedAttack] Gain 2 [FestivalFever]
   PL: [OnSucceedAttack] zyskuje 2 [FestivalFever]
406. [Umiejętność wroga [9017304] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017304].levelList[level=1].name
   limit: do 40 znaków
   EN: Evade
   PL: Evade
407. [Umiejętność wroga [9017304] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever]가 5 이상이면, 최종 위력 +1\n[StartBattle] [FestivalFever] 2 얻음\n[OnDefeatEvade] [FestivalFever] 2 잃음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017304].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [FestivalFever], [StartBattle], [OnDefeatEvade]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FestivalFever] = 축제의 열기 / Festive Fever; [StartBattle] = [전투 시작시] / [Combat Start]; [OnDefeatEvade] = [회피 실패시] / [Failed Evade]
   EN: [WhenUse] At 5+ [FestivalFever], Final Power +1\n[StartBattle] Gain 2 [FestivalFever]\n[OnDefeatEvade] Lose 2 [FestivalFever]
   PL: [WhenUse] przy 5+ [FestivalFever], Moc Końcowa +1\n[StartBattle] zyskuje 2 [FestivalFever]\n[OnDefeatEvade] traci 2 [FestivalFever]
408. [Umiejętność wroga [9017401] (ulepszenie 1) — nazwa] 경혈식 휘두르기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017401].levelList[level=1].name
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Umiejętność wroga [9017401] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever]가 5 이상이면, 최종 위력 +1
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017401].levelList[level=1].desc
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Umiejętność wroga [9017401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Umiejętność wroga [9017401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Burst] 2 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 395 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Umiejętność wroga [9017402] (ulepszenie 1) — nazwa] 경혈식 마구 찌르기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017402].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Wild Jag
   PL: Hardblood Wild Jag
413. [Umiejętność wroga [9017402] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever] 5 또는 대상의 [Laceration] 6당 최종 위력 +1 (최대 2)\n[WhenUse] [Laceration] 15를 얻은 다음 즉시 1회 발동시키고 [Laceration] 횟수 1 감소
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017402].levelList[level=1].desc
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Umiejętność wroga [9017402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]이 6 이상이면, [HardenedBlood] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Umiejętność wroga [9017402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Umiejętność wroga [9017402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloomingThorns] 1 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Umiejętność wroga [9017403] (ulepszenie 1) — nazwa] 경혈식 강화 펼치기
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017403].levelList[level=1].name
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Umiejętność wroga [9017403] (ulepszenie 1) — opis] [WhenUse] [Laceration] 15, [Laceration] 횟수 2를 얻음 다음 즉시 2회 발동시키고 [Laceration] 횟수 2 감소\n[EndBattle] [HardenedBlood], [FestivalFever] 전부 소모
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017403].levelList[level=1].desc
   (powtórzenie elementu 402 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Umiejętność wroga [9017403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [HardenedBlood]만큼 [Laceration], [Burst] 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Umiejętność wroga [9017403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 ([FestivalFever] x 2.5)%만큼 체력 회복 (최대 20%)
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 404 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Umiejętność wroga [9017403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [FestivalFever] 2 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Umiejętność wroga [9017404] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017404].levelList[level=1].name
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Umiejętność wroga [9017404] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever]가 5 이상이면, 최종 위력 +1\n[StartBattle] [FestivalFever] 2 얻음\n[OnDefeatEvade] [FestivalFever] 2 잃음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017404].levelList[level=1].desc
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Umiejętność wroga [9017501] (ulepszenie 1) — nazwa] 환상의 축제로 오세요!
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017501].levelList[level=1].name
   limit: do 50 znaków
   EN: Welcome to the Festival of Wonders!
   PL: Welcome to the Festival of Wonders!
425. [Umiejętność wroga [9017501] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever]가 5 이상이면, 최종 위력 +2
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [FestivalFever]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FestivalFever] = 축제의 열기 / Festive Fever
   EN: [WhenUse] At 5+ [FestivalFever], Final Power +2
   PL: [WhenUse] przy 5+ [FestivalFever], Moc Końcowa +2
426. [Umiejętność wroga [9017501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Umiejętność wroga [9017501] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Burst] 3 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017501].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 3 [Burst]
   PL: [OnSucceedAttackHead] nakłada 3 [Burst]
428. [Umiejętność wroga [9017502] (ulepszenie 1) — nazwa] 즐거운 행렬에 함께 해요!
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017502].levelList[level=1].name
   limit: do 40 znaków
   EN: Join the Joyful Parade!
   PL: Join the Joyful Parade!
429. [Umiejętność wroga [9017502] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever] 5 또는 대상의 [Laceration] 6당 최종 위력 +1 (최대 3)\n[WhenUse] [BloodDinner]이 20 미만이면, [Laceration] 20을 얻은 다음 즉시 1회 발동시키고 [Laceration] 횟수 1 감소\n[EndSkill] [BloodDinner] 20 소모
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017502].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [FestivalFever], [Laceration], [BloodDinner], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FestivalFever] = 축제의 열기 / Festive Fever; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Final Power +1 for every 5 [FestivalFever] on self or every 6 [Laceration] on the target (max 3)\n[WhenUse] At less than 20 [BloodDinner], gain 20 [Laceration] and immediately trigger it once, then reduce [Laceration] Count by 1\n[EndSkill] Consume 20 [BloodDinner]
   PL: [WhenUse] Moc Końcowa +1 za każde 5 [FestivalFever] tej jednostki lub 6 [Laceration] celu (maks. 3)\n[WhenUse] przy mniej niż 20 [BloodDinner], zyskuje 20 [Laceration], natychmiast uruchamia je raz, po czym traci 1 Licznika [Laceration]\n[EndSkill] zużywa 20 [BloodDinner]
430. [Umiejętność wroga [9017502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 6당 [HardenedBlood] 1 얻음 (최대 2)
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [HardenedBlood]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [OnSucceedAttack] Gain 1 [HardenedBlood] for every 6 [Laceration] on the target (max 2)
   PL: [OnSucceedAttack] zyskuje 1 [HardenedBlood] za każde 6 [Laceration] celu (maks. 2)
431. [Umiejętność wroga [9017502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Umiejętność wroga [9017502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [WinDuelAttack] [Laceration] 4 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Laceration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuelAttack] Inflict 4 [Laceration] and +3 [Laceration] Count
   PL: [WinDuelAttack] nakłada 4 [Laceration] i 3 Licznika [Laceration]
433. [Umiejętność wroga [9017502] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BloomingThorns] 2 ~ 3 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017502].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloomingThorns]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloomingThorns] = 피어나는 가시 / Blooming Thorn
   EN: [OnSucceedAttack] Gain 2~3 [BloomingThorns]
   PL: [OnSucceedAttack] zyskuje 2~3 [BloomingThorns]
434. [Umiejętność wroga [9017503] (ulepszenie 1) — nazwa] 기쁨의 미소를 꽃피워요!
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017503].levelList[level=1].name
   limit: do 40 znaków
   EN: Blossom your Smiles of Joy!
   PL: Blossom your Smiles of Joy!
435. [Umiejętność wroga [9017503] (ulepszenie 1) — opis] [WhenUse] [FestivalFever]가 5 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 합 위력 +1
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017503].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [FestivalFever], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FestivalFever] = 축제의 열기 / Festive Fever; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] At 5+ [FestivalFever], Coin Power +1\n[WhenUse] If target has 6+ [Laceration], Clash Power +1
   PL: [WhenUse] przy 5+ [FestivalFever], Moc Monety +1\n[WhenUse] jeżeli cel ma 6+ [Laceration], Moc Starcia +1
436. [Umiejętność wroga [9017503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Umiejętność wroga [9017503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [WinDuelAttack] [FestivalFever] 2 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [FestivalFever]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [FestivalFever] = 축제의 열기 / Festive Fever
   EN: [WinDuelAttack] Gain 2 [FestivalFever]
   PL: [WinDuelAttack] zyskuje 2 [FestivalFever]
438. [Umiejętność wroga [9017504] (ulepszenie 1) — nazwa] 영원한 행복의 왕국 라만차랜드!
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017504].levelList[level=1].name
   limit: do 60 znaków
   EN: Eternal Kingdom of Happiness, La Manchaland!
   PL: Eternal Kingdom of Happiness, La Manchaland!
439. [Umiejętność wroga [9017504] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]이 40 미만이면, [Laceration] 20, [Laceration] 횟수 2를 얻은 다음 즉시 2회 발동시키고 [Laceration] 횟수 2 감소\n[EndSkill] [BloodDinner] 40 소모\n[EndBattle] [HardenedBlood], [FestivalFever] 전부 소모
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017504].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [Laceration], [EndSkill], [EndBattle], [HardenedBlood], [FestivalFever]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [EndBattle] = [턴 종료 시] / [Turn End]; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [FestivalFever] = 축제의 열기 / Festive Fever
   EN: [WhenUse] At less than 40 [BloodDinner], gain 20 [Laceration] and +2 [Laceration] Count, immediately trigger it twice, then reduce [Laceration] Count by 2\n[EndSkill] Consume 40 [BloodDinner]\n[EndBattle] Consume all [HardenedBlood] and [FestivalFever]
   PL: [WhenUse] przy mniej niż 40 [BloodDinner], zyskuje 20 [Laceration] i 2 Licznika [Laceration], natychmiast uruchamia je 2 razy, po czym traci 2 Licznika [Laceration]\n[EndSkill] zużywa 40 [BloodDinner]\n[EndBattle] zużywa całe [HardenedBlood] i [FestivalFever]
440. [Umiejętność wroga [9017504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [HardenedBlood]만큼 [Laceration], [Burst] 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Umiejętność wroga [9017504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 최대 체력의 ([FestivalFever] x 4)%만큼 체력 회복 (최대 40%)
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [FestivalFever]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [FestivalFever] = 축제의 열기 / Festive Fever
   EN: [OnSucceedAttack] Heal ([FestivalFever] x 4)% HP (max 40%)
   PL: [OnSucceedAttack] przywraca HP równe ([FestivalFever] x 4)% Maks. HP (maks. 40%)
442. [Umiejętność wroga [9017504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Umiejętność wroga [9017504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloomingThorns] 5 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloomingThorns]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloomingThorns] = 피어나는 가시 / Blooming Thorn
   EN: [OnSucceedAttack] Gain 5 [BloomingThorns]
   PL: [OnSucceedAttack] zyskuje 5 [BloomingThorns]
444. [Umiejętność wroga [9017505] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017505].levelList[level=1].name
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Umiejętność wroga [9017505] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever]가 5 이상이면 최종 위력 +2\n[StartBattle] [FestivalFever] 3 얻음\n[OnDefeatEvade] [FestivalFever] 3 잃음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017505].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [FestivalFever], [StartBattle], [OnDefeatEvade]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FestivalFever] = 축제의 열기 / Festive Fever; [StartBattle] = [전투 시작시] / [Combat Start]; [OnDefeatEvade] = [회피 실패시] / [Failed Evade]
   EN: [WhenUse] At 5+ [FestivalFever], Final Power +2\n[StartBattle] Gain 3 [FestivalFever]\n[OnDefeatEvade] Lose 3 [FestivalFever]
   PL: [WhenUse] przy 5+ [FestivalFever], Moc Końcowa +2\n[StartBattle] zyskuje 3 [FestivalFever]\n[OnDefeatEvade] traci 3 [FestivalFever]
446. [Umiejętność wroga [9017601] (ulepszenie 1) — nazwa] 환상의 축제로 오세요!
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017601].levelList[level=1].name
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Umiejętność wroga [9017601] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever]가 5 이상이면, 최종 위력 +2
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017601].levelList[level=1].desc
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Umiejętność wroga [9017601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 [Laceration] i 3 Licznika [Laceration]
449. [Umiejętność wroga [9017601] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Burst] 3 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017601].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 427 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Umiejętność wroga [9017602] (ulepszenie 1) — nazwa] 모두 발 맞추어 춤을 춰요!
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017602].levelList[level=1].name
   limit: do 50 znaków
   EN: Let's All Match Our Steps, Dance!
   PL: Let's All Match Our Steps, Dance!
451. [Umiejętność wroga [9017602] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever] 5 또는 대상의 [Laceration] 6당 최종 위력 +1 (최대 3)\n[WhenUse] [BloodDinner]이 20 미만이면, [Laceration] 20을 얻은 다음 즉시 1회 발동시키고 [Laceration] 횟수 1 감소\n[EndSkill] [BloodDinner] 20 소모
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017602].levelList[level=1].desc
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Umiejętność wroga [9017602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 6당 [HardenedBlood] 1 얻음 (최대 2)
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 430 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Umiejętność wroga [9017602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Umiejętność wroga [9017602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [WinDuelAttack] [Laceration] 4 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Umiejętność wroga [9017602] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BloomingThorns] 2 ~ 3 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017602].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Umiejętność wroga [9017603] (ulepszenie 1) — nazwa] 신나게 노래를 불러봐요!
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017603].levelList[level=1].name
   limit: do 50 znaków
   EN: Lose Yourself in the Singing!
   PL: Lose Yourself in the Singing!
457. [Umiejętność wroga [9017603] (ulepszenie 1) — opis] [WhenUse] [FestivalFever]가 5 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 합 위력 +1
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017603].levelList[level=1].desc
   (powtórzenie elementu 435 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Umiejętność wroga [9017603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Umiejętność wroga [9017603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [WinDuelAttack] [FestivalFever] 2 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Umiejętność wroga [9017604] (ulepszenie 1) — nazwa] 영원한 행복의 왕국 라만차랜드!
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017604].levelList[level=1].name
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Umiejętność wroga [9017604] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]이 40 미만이면, [Laceration] 20, [Laceration] 횟수 2를 얻은 다음 즉시 2회 발동시키고 [Laceration] 횟수 2 감소\n[EndSkill] [BloodDinner] 40 소모\n[EndBattle] [HardenedBlood], [FestivalFever] 전부 소모
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017604].levelList[level=1].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Umiejętność wroga [9017604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [HardenedBlood]만큼 [Laceration], [Burst] 부여
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Umiejętność wroga [9017604] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 최대 체력의 ([FestivalFever] x 4)%만큼 체력 회복 (최대 40%)
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017604].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Umiejętność wroga [9017604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Umiejętność wroga [9017604] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloomingThorns] 5 얻음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017604].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Umiejętność wroga [9017605] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017605].levelList[level=1].name
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Umiejętność wroga [9017605] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever]가 5 이상이면 최종 위력 +2\n[StartBattle] [FestivalFever] 3 얻음\n[OnDefeatEvade] [FestivalFever] 3 잃음
   źródło: Skills_Enemy-a1c7p2.json :: dataList[id=9017605].levelList[level=1].desc
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c7p2] Pasywka wroga: Passives_Abnormality-a1c7p2
- plik gry: `Passives_Abnormality-a1c7p2.json`

468. [[a1c7p2] Pasywka wroga [838101] — nazwa] 환상의 축제
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838101].name
   limit: do 40 znaków
   EN: Festival of Wonders
   PL: Festival of Wonders
469. [[a1c7p2] Pasywka wroga [838101] — opis] 다른 아군에게 스킬 효과로 긍정적 버프를 부여할 때마다 [FestivalFever] 1 얻음 (종류 별로 1회)\n\n턴 시작 시, 자신을 제외한 다른 아군의 수만큼 [FestivalFever]를 얻음 (최대 3)\n턴 종료 시, 자신의 [FestivalFever]만큼 정신력을 회복 (정신력이 -45일 때는 발동하지 않음)\n\n턴 종료 시 [FestivalFever]가 10이면 다음 턴에 강력한 스킬을 사용 (단, '퍼레이드는 영원히 반복될거야' 효과가 활성화되면 발동하지 않음)
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838101].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [FestivalFever]
   znaczenie tagów: [FestivalFever] = 축제의 열기 / Festive Fever
   EN: Gain 1 [FestivalFever] every time this unit applies a positive buff to other allies with its Skill effects (once per type of buff)\n\nTurn Start: gain [FestivalFever] equal to the number of other allies (max 3)\nTurn End: heal SP equal to [FestivalFever] on self (does not activate at -45 SP)\n\nTurn End: at 10+ [FestivalFever], use a powerful Skill next turn (however, if 'The Parade Repeats for Eternity' is active, this effect does not activate)
   PL: zyskuje 1 [FestivalFever] za każdym razem, gdy efekty Umiejętności nakładają pozytywny Efekt na innych sojuszników (1 raz na typ Efektu)\n\nPoczątek tury: zyskuje [FestivalFever] równe liczbie innych sojuszników (maks. 3)\nKoniec tury: przywraca SP równe własnego [FestivalFever] (nie uruchamia się przy SP równym -45)\n\nKoniec tury: przy 10+ [FestivalFever] używa w następnej turze potężnej Umiejętności (jednak jeżeli aktywny jest efekt „The Parade Repeats for Eternity”, ten efekt się nie uruchamia)
470. [[a1c7p2] Pasywka wroga [838102] — nazwa] 퍼레이드의 주인공
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838102].name
   limit: do 40 znaków
   EN: The Parade's Lady
   PL: The Parade's Lady
471. [[a1c7p2] Pasywka wroga [838102] — opis] 턴 시작 시, [Protection] 8 얻음\n- 아군이 사망할 때마다 턴 시작 시 획득하는 수치가 1씩 감소\n턴 종료 시 이번 턴에 체력 피해를 받지 않았다면 다음 턴에 [Agility] 2 얻음
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838102].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Protection], [Agility]
   znaczenie tagów: [Protection] = 보호 / Protection; [Agility] = 신속 / Haste
   EN: Turn Start: gain 8 [Protection]\n- With every ally death, gain 1 less [Protection] at Turn Start\nTurn End: If this unit did not take any HP damage this turn, gain 2 [Agility] next turn
   PL: Początek tury: zyskuje 8 [Protection]\n- za każdą śmierć sojusznika zyskuje o 1 mniej [Protection] na Początku tury\nKoniec tury: jeżeli ta jednostka nie otrzymała obrażeń HP w tej turze, zyskuje 2 [Agility] w następnej turze
472. [[a1c7p2] Pasywka wroga [838103] — nazwa] 퍼레이드는 영원히 반복될거야
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838103].name
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [[a1c7p2] Pasywka wroga [838103] — opis] 턴 종료 시 [IncompleteParade]의 수치가 5 이상이면, 다음 턴에 강력한 스킬을 사용
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838103].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [IncompleteParade]
   znaczenie tagów: [IncompleteParade] = 불완전한 퍼레이드 / Imperfect Parade
   EN: Turn End: if at 5+ [IncompleteParade], use a powerful Skill next turn
   PL: Koniec tury: przy 5+ [IncompleteParade], używa w następnej turze potężnej Umiejętności
474. [[a1c7p2] Pasywka wroga [838104] — nazwa] 행복의 퍼레이드
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838104].name
   limit: do 40 znaków
   EN: Parade of Happiness
   PL: Parade of Happiness
475. [[a1c7p2] Pasywka wroga [838104] — opis] 자신의 체력이 처음으로 최대 체력의 66% 이하가 되었을 때 패턴이 강화됨\n\n패턴 변경 시\n- 속도 최솟값, 최댓값 1 증가\n- 자신의 [BloomingThorns] 효과가 [BloomingThorns_2nd]로 변경됨\n- 매 턴마다 모든 아군이 [FestivalFever] 3, [BloomingThorns] 3 얻음
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838104].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [BloomingThorns], [BloomingThorns_2nd], [FestivalFever]
   znaczenie tagów: [BloomingThorns] = 피어나는 가시 / Blooming Thorn; [BloomingThorns_2nd] = 피를 엮은 가시 / Bloodwoven Thorn; [FestivalFever] = 축제의 열기 / Festive Fever
   EN: Gains a new pattern when this unit's HP drops to 66% or less for the first time\n\nUpon pattern change,\n- Raise Min & Max Speed values by 1\n- Convert [BloomingThorns] on self to [BloomingThorns_2nd]\n- All allies gain 3 [FestivalFever] and 3 [BloomingThorns] at every turn
   PL: przybiera nowy wzorzec, gdy HP tej jednostki po raz pierwszy spada do 66% lub mniej\n\npo zmianie wzorca:\n- Min. i Maks. Szybkość +1\n- zmienia własne [BloomingThorns] w [BloomingThorns_2nd]\n- co turę wszyscy sojusznicy zyskują 3 [FestivalFever] i 3 [BloomingThorns]
476. [[a1c7p2] Pasywka wroga [838105] — nazwa] 영원한 행복의 퍼레이드
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838105].name
   limit: do 40 znaków
   EN: Eternal Parade of Happiness
   PL: Eternal Parade of Happiness
477. [[a1c7p2] Pasywka wroga [838105] — opis] 자신의 체력이 처음으로 최대 체력의 33% 이하가 되었을 때 패턴이 강화됨\n\n패턴 변경 시\n- 속도 최솟값, 최댓값 2 증가\n- 강력한 스킬을 사용하며, 그 후 참격, 관통, 타격의 내성이 약화(+0.5)됨\n- 자신의 [BloomingThorns], [BloomingThorns_2nd] 효과가 [BloomingThorns_3rd]로 변경됨\n- 매 턴마다 모든 아군이 [FestivalFever] 5, [BloomingThorns] 5 얻음
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838105].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [BloomingThorns], [BloomingThorns_2nd], [BloomingThorns_3rd], [FestivalFever]
   znaczenie tagów: [BloomingThorns] = 피어나는 가시 / Blooming Thorn; [BloomingThorns_2nd] = 피를 엮은 가시 / Bloodwoven Thorn; [BloomingThorns_3rd] = 피로 빚은 가시 / Bloodmolded Thorn; [FestivalFever] = 축제의 열기 / Festive Fever
   EN: Gains a new pattern when this unit's HP drops to 33% or less for the first time\n\nUpon pattern change,\n- Raise Min & Max Speed values by 2\n- Uses a powerful Skill; then weakens Resistances against Slash, Pierce, and Blunt (+0.5)\n- Convert [BloomingThorns] and [BloomingThorns_2nd] on self to [BloomingThorns_3rd]\n- All allies gain 5 [FestivalFever] and 5 [BloomingThorns] at every turn
   PL: przybiera nowy wzorzec, gdy HP tej jednostki po raz pierwszy spada do 33% lub mniej\n\npo zmianie wzorca:\n- Min. i Maks. Szybkość +2\n- używa potężnej Umiejętności, po czym Osłabia Odporność na Cięcia, Przebicie i Uderzenie (+0.5)\n- zmienia własne [BloomingThorns] i [BloomingThorns_2nd] w [BloomingThorns_3rd]\n- co turę wszyscy sojusznicy zyskują 5 [FestivalFever] i 5 [BloomingThorns]
478. [[a1c7p2] Pasywka wroga [838106] — nazwa] 이렇게 끝나서는 안 돼
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838106].name
   limit: do 40 znaków
   EN: This isn't how it ends
   PL: This isn't how it ends
479. [[a1c7p2] Pasywka wroga [838106] — opis] 턴 종료 시 살아있는 아군이 없고 추가로 등장할 수 있는 아군도 없는 경우, 다음 턴에 [FestivalFever], [IncompleteParade]를 전부 소모하고 흐트러짐 상태가 됨 (턴 시작 시 살아있는 아군이 없는 경우에는 즉시 발동)\n\n흐트러진 다음 턴에 권속 혈귀 2명을 소환함
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838106].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [FestivalFever], [IncompleteParade]
   znaczenie tagów: [FestivalFever] = 축제의 열기 / Festive Fever; [IncompleteParade] = 불완전한 퍼레이드 / Imperfect Parade
   EN: Turn End: If there are no surviving allies nor Backup allies, consume all [FestivalFever] and [IncompleteParade] next turn and become Staggered (activates immediately if there are no surviving allies at Turn Start)\n\nIn the turn after this unit is Staggered, summon 2 Kindred Bloodfiends
   PL: Koniec tury: jeżeli nie ma żyjących sojuszników ani sojuszników rezerwowych, w następnej turze zużywa całe [FestivalFever] i [IncompleteParade] i przechodzi w Oszołamienie (uruchamia się natychmiast, jeżeli na Początku tury nie ma żyjących sojuszników)\n\nw turze po Oszołamieniu przywołuje 2 Kindred Bloodfiends
480. [[a1c7p2] Pasywka wroga [838107] — nazwa] 혈찬
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838107].name
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [[a1c7p2] Pasywka wroga [838107] — opis] 이 캐릭터가 전투에 등장해 있거나, 등장할 적 리스트에 포함되어 있으면, 1턴부터 모든 캐릭터가 받은 [Laceration] 피해만큼 [BloodDinner]이 증가함. 이 캐릭터가 전투에 등장할 때 전장에 흩뿌려진 잠재된 피가 더욱 크게 드러난다.
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838107].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: If this unit is on field, or is one of the units that can appear on this Stage, increase [BloodDinner] value by the amount of [Laceration] damage collectively received by every unit. \nWhen this unit enters the field, the sleeping blood drenching the battlefield will fill the surface.
   PL: jeżeli ta jednostka jest na polu bitwy lub znajduje się na liście wrogów mogących się pojawić w tej walce, od 1. tury [BloodDinner] rośnie o łączną wartość obrażeń [Laceration] otrzymanych przez wszystkie jednostki. gdy ta jednostka pojawia się na polu bitwy, uśpiona krew przesiąkająca pole bitwy wypełnia powierzchnię.
482. [[a1c7p2] Pasywka wroga [838108] — nazwa] 굶주림과 노쇠
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838108].name
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [[a1c7p2] Pasywka wroga [838108] — opis] 전투 시작 시, [StarvingDolcineaOne] 얻음
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838108].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StarvingDolcineaOne]
   znaczenie tagów: [StarvingDolcineaOne] = 노쇠 / Withered
   EN: Gain [StarvingDolcineaOne] at the start of the Encounter
   PL: Początek walki: zyskuje [StarvingDolcineaOne]
484. [[a1c7p2] Pasywka wroga [838901] — nazwa] 하얀 달의 기사
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838901].name
   (powtórzenie elementu 198 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [[a1c7p2] Pasywka wroga [838901] — opis] 받는 피해량 -20%\n합 패배시 [Enhancement] 3 얻음
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838901].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Damage Taken -20%\nGain 3 [Enhancement] on Clash Lose
   PL: otrzymuje o 20% mniej obrażeń\npo przegranej w Starciu zyskuje 3 [Enhancement]
486. [[a1c7p2] Pasywka wroga [838902] — nazwa] 아슬아슬한 승부
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838902].name
   limit: do 40 znaków
   EN: A Close Match
   PL: A Close Match
487. [[a1c7p2] Pasywka wroga [838902] — opis] 동일한 대상과의 합이 10합 이상이면, 합 판정 시 합 위력이 현재 (합 횟수 / 10)만큼 랜덤하게 증가 또는 감소함. (소수점 버림)
   źródło: Passives_Abnormality-a1c7p2.json :: dataList[id=838902].desc
   limit: do 160 znaków
   EN: At 10+ Clashes against the same enemy, randomly gain or lose Clash Power by (Clash Count / 10) in a Clash. (rounded down)
   PL: po 10+ Starciach z tym samym wrogiem, podczas rozstrzygania Starcia Moc Starcia losowo rośnie lub maleje o (Liczba Starć / 10). (zaokrąglone w dół)

## [a1c7p2] Pasywka wroga: Passives_Enemy-a1c7p2
- plik gry: `Passives_Enemy-a1c7p2.json`

488. [[a1c7p2] Pasywka wroga [9015801] — nazwa] 어설픈 흡혈
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9015801].name
   limit: do 40 znaków
   EN: Clumsy Bloodsucking
   PL: Clumsy Bloodsucking
489. [[a1c7p2] Pasywka wroga [9015801] — opis] 공격 적중시 대상에게 [Laceration]이 있으면, 피해량의 5 ~ 10% 만큼 체력 회복
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9015801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: On Hit, if the target has [Laceration], heal by 5~10% of damage dealt
   PL: przy trafieniu, jeżeli cel ma [Laceration], przywraca HP równe 5~10% zadanych obrażeń
490. [[a1c7p2] Pasywka wroga [9017501] — nazwa] 축제 분위기
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017501].name
   limit: do 40 znaków
   EN: Festive Mood
   PL: Festive Mood
491. [[a1c7p2] Pasywka wroga [9017501] — opis] 스킬 효과로 긍정적 버프 효과를 얻을 때마다 [FestivalFever] 1 얻음 (종류 별로 1회)\n\n턴 시작 시, 자신을 제외한 다른 아군의 수만큼 [FestivalFever]를 얻음 (최대 3)\n턴 종료 시, 이번 턴에 사망한 아군의 수만큼 [FestivalFever]를 잃음\n턴 종료 시, 자신의 [FestivalFever]만큼 정신력을 회복 (정신력이 -45일 때는 발동하지 않음)\n\n턴 종료 시 [FestivalFever]가 8 이상이면 다음 턴에 강력한 스킬을 사용
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017501].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [FestivalFever]
   znaczenie tagów: [FestivalFever] = 축제의 열기 / Festive Fever
   EN: Gain 1 [FestivalFever] every time this unit gains positive buff with Skill effects (once per type of buff)\n\nTurn Start: gain [FestivalFever] equal to the number of other allies (max 3)\nTurn End: lose [FestivalFever] equal to the number of allies that were killed this turn\nTurn End: heal SP equal to [FestivalFever] on self (does not activate at -45 SP)\n\nTurn End: at 8+ [FestivalFever], use a powerful Skill next turn
   PL: zyskuje 1 [FestivalFever] za każdym razem, gdy efekty Umiejętności nakładają na jednostkę pozytywny Efekt (1 raz na typ Efektu)\n\nPoczątek tury: zyskuje [FestivalFever] równe liczbie innych sojuszników (maks. 3)\nKoniec tury: traci [FestivalFever] równe liczbie sojuszników poległych w tej turze\nKoniec tury: przywraca SP równe własnego [FestivalFever] (nie uruchamia się przy SP równym -45)\n\nKoniec tury: przy 8+ [FestivalFever] używa w następnej turze potężnej Umiejętności
492. [[a1c7p2] Pasywka wroga [9017502] — nazwa] 흡혈
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017502].name
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [[a1c7p2] Pasywka wroga [9017502] — opis] 공격 적중시 대상에게 [Laceration]이 있으면, 피해량의 20%만큼 체력 회복
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017502].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [[a1c7p2] Pasywka wroga [9017503] — nazwa] 혈액 경화
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017503].name
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [[a1c7p2] Pasywka wroga [9017503] — opis] 공격 종료시 대상의 [Laceration]이 5 이상이면, [HardenedBlood] 1 얻음
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017503].desc
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [[a1c7p2] Pasywka wroga [9017504] — nazwa] 피의 갈증
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017504].name
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [[a1c7p2] Pasywka wroga [9017504] — opis] - [Laceration]이 부여된 대상을 우선적으로 공격\n- 턴 종료 시 이번 턴에 피해를 입히지 못한 경우, 다음 턴에 취약 2, 공격 레벨 증가 2를 얻음\n- 턴 종료 시 이번 턴에 피해를 입혔다면, 정신력 5 회복
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017504].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Vulnerable]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Vulnerable] = 취약 / Fragile
   EN: - Prioritizes targets with [Laceration]\nTurn End: if this unit failed to deal any damage this turn, gain 2 [Vulnerable] and 2 Offense Level Up next turn\n- Turn End: if this unit dealt damage this turn, heal 5 SP
   PL: - priorytet: cele z [Laceration]\n- Koniec tury: jeżeli nie zadała żadnych obrażeń w tej turze, zyskuje 2 [Vulnerable] i 2 Wzrost Poziomu Ataku w następnej turze\n- Koniec tury: jeżeli zadała obrażenia w tej turze, przywraca 5 SP
498. [[a1c7p2] Pasywka wroga [9017505] — nazwa] 혈찬
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017505].name
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [[a1c7p2] Pasywka wroga [9017505] — opis] 이 캐릭터가 전투에 등장해 있거나, 등장할 적 리스트에 포함되어 있으면, 1턴부터 모든 캐릭터가 받은 [Laceration] 피해만큼 [BloodDinner]이 증가함.\n이 캐릭터가 전투에 등장할 때 전장에 흩뿌려진 잠재된 피를 드러낸다.
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017505].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [[a1c7p2] Pasywka wroga [9017506] — nazwa] 굶주림과 노쇠
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017506].name
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [[a1c7p2] Pasywka wroga [9017506] — opis] 전투 시작 시, [StarvingDolcineaServant] 얻음
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017506].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StarvingDolcineaServant]
   znaczenie tagów: [StarvingDolcineaServant] = 노쇠 / Withered
   EN: Gain [StarvingDolcineaServant] at the start of the Encounter
   PL: Początek walki: zyskuje [StarvingDolcineaServant]
502. [[a1c7p2] Pasywka wroga [9017301] — nazwa] 축제 소리
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017301].name
   limit: do 40 znaków
   EN: Festive Sounds
   PL: Festive Sounds
503. [[a1c7p2] Pasywka wroga [9017301] — opis] 스킬 효과로 긍정적 버프 효과를 얻을 때마다 [FestivalFever] 1 얻음 (종류 별로 1회)\n\n턴 시작 시, 자신을 제외한 다른 아군의 수만큼 [FestivalFever]를 얻음 (최대 3)\n턴 종료 시, 이번 턴에 사망한 아군의 수만큼 [FestivalFever]를 잃음\n\n[FestivalFever]가 8 이상이면 강력한 스킬을 사용
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017301].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [FestivalFever]
   znaczenie tagów: [FestivalFever] = 축제의 열기 / Festive Fever
   EN: Gain 1 [FestivalFever] every time this unit gains positive buff with Skill effects (once per type of buff)\n\nTurn Start: gain [FestivalFever] equal to the number of other allies (max 3)\nTurn End: lose [FestivalFever] equal to the number of allies that were killed this turn\n\nTurn End: at 8+ [FestivalFever], use a powerful Skill next turn
   PL: zyskuje 1 [FestivalFever] za każdym razem, gdy efekty Umiejętności nakładają na jednostkę pozytywny Efekt (1 raz na typ Efektu)\n\nPoczątek tury: zyskuje [FestivalFever] równe liczbie innych sojuszników (maks. 3)\nKoniec tury: traci [FestivalFever] równe liczbie sojuszników poległych w tej turze\n\nKoniec tury: przy 8+ [FestivalFever] używa w następnej turze potężnej Umiejętności
504. [[a1c7p2] Pasywka wroga [9017302] — nazwa] 흡혈
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017302].name
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [[a1c7p2] Pasywka wroga [9017302] — opis] 공격 적중시 대상에게 [Laceration]이 있으면, 피해량의 15%만큼 체력 회복
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017302].desc
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [[a1c7p2] Pasywka wroga [9017303] — nazwa] 혈액 경화
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017303].name
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [[a1c7p2] Pasywka wroga [9017303] — opis] 공격 종료시 대상의 [Laceration]이 8 이상이면, [HardenedBlood] 1 얻음
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017303].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [[a1c7p2] Pasywka wroga [9017304] — nazwa] 피의 갈증
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017304].name
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [[a1c7p2] Pasywka wroga [9017304] — opis] [Laceration]이 부여된 대상을 우선적으로 공격\n턴 종료 시 이번 턴에 피해를 입히지 못한 경우, 다음 턴에 [Vulnerable] 2, [AttackUp] 2를 얻음
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017304].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Vulnerable], [AttackUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Vulnerable] = 취약 / Fragile; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Prioritizes targets with [Laceration]\nTurn End: if this unit failed to deal any damage this turn, gain 2 [Vulnerable] and 2 [AttackUp] next turn
   PL: priorytet: cele z [Laceration]\nKoniec tury: jeżeli nie zadała żadnych obrażeń w tej turze, zyskuje 2 [Vulnerable] i 2 [AttackUp] w następnej turze
510. [[a1c7p2] Pasywka wroga [9017305] — nazwa] 피주머니
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017305].name
   (powtórzenie elementu 132 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [[a1c7p2] Pasywka wroga [9017305] — opis] 피격 시 자신의 [Laceration] 횟수 1 증가\n체력이 20% 감소할 때마다 [HardenedBlood] 1, [BloomingThorns] 2 얻음.\n아군 또는 적에 혈귀가 있는 경우, 사망 시, [BloodDinner]이 30만큼 증가
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017305].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [HardenedBlood], [BloomingThorns], [BloodDinner]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [BloomingThorns] = 피어나는 가시 / Blooming Thorn; [BloodDinner] = 혈찬 / Bloodfeast
   EN: When hit, gain +1 [Laceration] Count.\nGain 1 [HardenedBlood] and 2 [BloomingThorns] every time this unit loses 20% HP.\nIf there is a Bloodfiend on the field, regardless of whether it is an ally or an enemy, increase [BloodDinner] by 30 upon death
   PL: przy otrzymaniu trafienia zyskuje 1 Licznika [Laceration].\nzyskuje 1 [HardenedBlood] i 2 [BloomingThorns] za każdym razem, gdy traci 20% HP.\njeżeli na polu bitwy znajduje się Bloodfiend — sojusznik lub wróg — przy śmierci zwiększa [BloodDinner] o 30
512. [[a1c7p2] Pasywka wroga [9017101] — nazwa] 굶주림과 노쇠
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017101].name
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [[a1c7p2] Pasywka wroga [9017101] — opis] 전투 시작 시, [StarvingPriestOne] 얻음
   źródło: Passives_Enemy-a1c7p2.json :: dataList[id=9017101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StarvingPriestOne]
   znaczenie tagów: [StarvingPriestOne] = 노쇠 / Withered
   EN: Gain [StarvingPriestOne] at the start of the Encounter
   PL: Początek walki: zyskuje [StarvingPriestOne]

## [a1c7p3] Wróg / część: Enemies-a1c7p3
- plik gry: `Enemies-a1c7p3.json`

514. [[a1c7p3] Wróg / część [90162] — nazwa] 움튼 피주머니
   źródło: Enemies-a1c7p3.json :: dataList[id=90162].name
   limit: do 40 znaków
   EN: Budding Bloodbag
   PL: Budding Bloodbag
515. [[a1c7p3] Wróg / część [90162] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=90162].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [[a1c7p3] Wróg / część [8394] — nazwa] 움튼 츠바이 해결사
   źródło: Enemies-a1c7p3.json :: dataList[id=8394].name
   limit: do 40 znaków
   EN: Budding Zwei Fixer
   PL: Budding Zwei Fixer
517. [[a1c7p3] Wróg / część [8394] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8394].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [[a1c7p3] Wróg / część [90166] — nazwa] 피어난 혈귀
   źródło: Enemies-a1c7p3.json :: dataList[id=90166].name
   limit: do 40 znaków
   EN: Budding Bloodfiend
   PL: Budding Bloodfiend
519. [[a1c7p3] Wróg / część [90166] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=90166].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [[a1c7p3] Wróg / część [90167] — nazwa] 만발한 혈귀
   źródło: Enemies-a1c7p3.json :: dataList[id=90167].name
   limit: do 40 znaków
   EN: Blossomed Bloodfiend
   PL: Blossomed Bloodfiend
521. [[a1c7p3] Wróg / część [90167] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=90167].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [[a1c7p3] Wróg / część [90168] — nazwa] 만개한 혈귀
   źródło: Enemies-a1c7p3.json :: dataList[id=90168].name
   limit: do 40 znaków
   EN: Bloomed Bloodfiend
   PL: Bloomed Bloodfiend
523. [[a1c7p3] Wróg / część [90168] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=90168].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [[a1c7p3] Wróg / część [8373] — nazwa] 색욕 죄종?
   źródło: Enemies-a1c7p3.json :: dataList[id=8373].name
   limit: do 40 znaków
   EN: Peccatulum Luxuriae?
   PL: Peccatulum Luxuriae?
525. [[a1c7p3] Wróg / część [8373] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8373].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [[a1c7p3] Wróg / część [8374] — nazwa] 오만 죄종?
   źródło: Enemies-a1c7p3.json :: dataList[id=8374].name
   limit: do 40 znaków
   EN: Peccatulum Superbiae?
   PL: Peccatulum Superbiae?
527. [[a1c7p3] Wróg / część [8374] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8374].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [[a1c7p3] Wróg / część [8375] — nazwa] 움튼 서부 섕크 해결사
   źródło: Enemies-a1c7p3.json :: dataList[id=8375].name
   limit: do 40 znaków
   EN: Budding Cinq West Fixer
   PL: Budding Cinq West Fixer
529. [[a1c7p3] Wróg / część [8375] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8375].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [[a1c7p3] Wróg / część [8376] — nazwa] 장미 사냥꾼
   źródło: Enemies-a1c7p3.json :: dataList[id=8376].name
   limit: do 40 znaków
   EN: Rose Hunter
   PL: Rose Hunter
531. [[a1c7p3] Wróg / część [8376] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8376].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [[a1c7p3] Wróg / część [8377] — nazwa] 가시 올가미
   źródło: Enemies-a1c7p3.json :: dataList[id=8377].name
   limit: do 40 znaków
   EN: Barbed Lasso
   PL: Barbed Lasso
533. [[a1c7p3] Wróg / część [8377] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8377].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [[a1c7p3] Wróg / część [8378] — nazwa] 신부
   źródło: Enemies-a1c7p3.json :: dataList[id=8378].name
   limit: do 40 znaków
   EN: The Priest
   PL: The Priest
535. [[a1c7p3] Wróg / część [8378] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8378].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [[a1c7p3] Wróg / część [8379] — nazwa] 아파하는 테디
   źródło: Enemies-a1c7p3.json :: dataList[id=8379].name
   limit: do 40 znaków
   EN: Hurting Teddy Bear
   PL: Hurting Teddy Bear
537. [[a1c7p3] Wróg / część [8379] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8379].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [[a1c7p3] Wróg / część [8380] — nazwa] 산초
   źródło: Enemies-a1c7p3.json :: dataList[id=8380].name
   limit: do 40 znaków
   EN: Sancho
   PL: Sancho
539. [[a1c7p3] Wróg / część [8380] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8380].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [[a1c7p3] Wróg / część [8395] — nazwa] 이발사
   źródło: Enemies-a1c7p3.json :: dataList[id=8395].name
   limit: do 40 znaków
   EN: The Barber
   PL: The Barber
541. [[a1c7p3] Wróg / część [8395] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8395].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [[a1c7p3] Wróg / część [8396] — nazwa] 돌시네아
   źródło: Enemies-a1c7p3.json :: dataList[id=8396].name
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [[a1c7p3] Wróg / część [8396] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8396].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [[a1c7p3] Wróg / część [8403] — nazwa] 곤돌라
   źródło: Enemies-a1c7p3.json :: dataList[id=8403].name
   limit: do 40 znaków
   EN: Gondola
   PL: Gondola
545. [[a1c7p3] Wróg / część [8403] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8403].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [[a1c7p3] Wróg / część [8411] — nazwa] 굳어진 꿈
   źródło: Enemies-a1c7p3.json :: dataList[id=8411].name
   limit: do 40 znaków
   EN: Coagulated Dream
   PL: Coagulated Dream
547. [[a1c7p3] Wróg / część [8411] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8411].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [[a1c7p3] Wróg / część [8412] — nazwa] 꿰뚫은 창
   źródło: Enemies-a1c7p3.json :: dataList[id=8412].name
   limit: do 40 znaków
   EN: Impaling Spear
   PL: Impaling Spear
549. [[a1c7p3] Wróg / część [8412] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8412].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [[a1c7p3] Wróg / część [90165] — nazwa] 움튼 서부 츠바이 해결사
   źródło: Enemies-a1c7p3.json :: dataList[id=90165].name
   limit: do 40 znaków
   EN: Budding Zwei West Fixer
   PL: Budding Zwei West Fixer
551. [[a1c7p3] Wróg / część [90165] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=90165].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [[a1c7p3] Wróg / część [8410] — nazwa] 돈키호테
   źródło: Enemies-a1c7p3.json :: dataList[id=8410].name
   limit: do 40 znaków
   EN: Don Quixote
   PL: Don Quixote
553. [[a1c7p3] Wróg / część [8410] — opis] 보스
   źródło: Enemies-a1c7p3.json :: dataList[id=8410].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [[a1c7p3] Wróg / część [8413] — nazwa] 꿈꾸는 모험의 기억
   źródło: Enemies-a1c7p3.json :: dataList[id=8413].name
   limit: do 50 znaków
   EN: Memories of the Dreaming Adventure
   PL: Memories of the Dreaming Adventure
555. [[a1c7p3] Wróg / część [8413] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=8413].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [[a1c7p3] Wróg / część [8390] — nazwa] 돈키호테
   źródło: Enemies-a1c7p3.json :: dataList[id=8390].name
   (powtórzenie elementu 552 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [[a1c7p3] Wróg / część [8390] — opis] 보스
   źródło: Enemies-a1c7p3.json :: dataList[id=8390].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [[a1c7p3] Wróg / część [839001] — nazwa] 대관람차
   źródło: Enemies-a1c7p3.json :: dataList[id=839001].name
   limit: do 40 znaków
   EN: The Wheel of La Manchaland
   PL: The Wheel of La Manchaland
559. [[a1c7p3] Wróg / część [839001] — opis] 보스
   źródło: Enemies-a1c7p3.json :: dataList[id=839001].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [[a1c7p3] Wróg / część [840301] — nazwa] 곤돌라
   źródło: Enemies-a1c7p3.json :: dataList[id=840301].name
   (powtórzenie elementu 544 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [[a1c7p3] Wróg / część [840301] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=840301].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [[a1c7p3] Wróg / część [841101] — nazwa] 꿈 조각
   źródło: Enemies-a1c7p3.json :: dataList[id=841101].name
   limit: do 40 znaków
   EN: Dreamshard
   PL: Dreamshard
563. [[a1c7p3] Wróg / część [841101] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=841101].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [[a1c7p3] Wróg / część [841201] — nazwa] 경혈 조각
   źródło: Enemies-a1c7p3.json :: dataList[id=841201].name
   limit: do 40 znaków
   EN: Hardblood Fragment
   PL: Hardblood Fragment
565. [[a1c7p3] Wróg / część [841201] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=841201].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [[a1c7p3] Wróg / część [841301] — nazwa] 모험의 기억
   źródło: Enemies-a1c7p3.json :: dataList[id=841301].name
   limit: do 40 znaków
   EN: Memories of the Adventure
   PL: Memories of the Adventure
567. [[a1c7p3] Wróg / część [841301] — opis] 잡몹
   źródło: Enemies-a1c7p3.json :: dataList[id=841301].desc
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c7p3] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c7p3
- grupa rozdziału/trybu: `a1c7p3` · plik: `Skills_Abnormality-a1c7p3.json`

568. [Umiejętność wroga [837801] (ulepszenie 1) — nazwa] 씻을 수 없는 죄를...
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837801].levelList[level=1].name
   limit: do 40 znaków
   EN: This Unforgivable Sin...
   PL: This Unforgivable Sin...
569. [Umiejętność wroga [837801] (ulepszenie 1) — opis] [WhenUse] 자신에게 [Laceration] 20 부여, 자신의 [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Gain 20 [Laceration] and +1 [Laceration] Count
   PL: [WhenUse] nakłada na siebie 20 [Laceration] i 1 Licznika [Laceration]
570. [Umiejętność wroga [837801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Umiejętność wroga [837802] (ulepszenie 1) — nazwa] 마땅한 벌을...
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837802].levelList[level=1].name
   limit: do 40 znaków
   EN: The Deserved Penance...
   PL: The Deserved Penance...
572. [Umiejętność wroga [837802] (ulepszenie 1) — opis] [WhenUse] 자신에게 [Laceration] 20 부여, 자신의 [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837802].levelList[level=1].desc
   (powtórzenie elementu 569 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Umiejętność wroga [837802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Umiejętność wroga [837802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Umiejętność wroga [837803] (ulepszenie 1) — nazwa] 오늘 피에 대한 생각을 했나?
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837803].levelList[level=1].name
   limit: do 50 znaków
   EN: Did you think about blood today?
   PL: Did you think about blood today?
576. [Umiejętność wroga [837803] (ulepszenie 1) — opis] [WhenUse] 자신에게 [Laceration] 10 부여\n[WhenUse] [BloodDinner]을 최대 30까지 소모하여 체력이 가장 낮은 아군의 (본체와 부위의) 체력을 (소모한 [BloodDinner]x2) 만큼 회복 (본인 제외. 소수점 버림)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837803].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BloodDinner]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: [WhenUse] Gain 10 [Laceration]\n[WhenUse] Consume up to 30 [BloodDinner]: heal the Core and the Part of the ally with the least HP by ([BloodDinner] consumed x 2). (excludes self; rounded down)
   PL: [WhenUse] nakłada na siebie 10 [Laceration]\n[WhenUse] zużywa do 30 [BloodDinner]: przywraca Korpusowi i Części sojusznika z najniższym HP HP równe (zużyte [BloodDinner] x 2). (poza jednostką; zaokrąglone w dół)
577. [Umiejętność wroga [837803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Umiejętność wroga [837803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [WornHeart]과 [BloodyHand] 2 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [WornHeart], [BloodyHand]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [WornHeart] = 닳아버린 마음 / Ailing Heart; [BloodyHand] = 피로 물든 손 / Bloodied Hand
   EN: [OnSucceedAttack] Gain 2 [WornHeart] and [BloodyHand]
   PL: [OnSucceedAttack] zyskuje 2 [WornHeart] i [BloodyHand]
579. [Umiejętność wroga [837804] (ulepszenie 1) — nazwa] 여전히 피가 생각 나나?
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837804].levelList[level=1].name
   limit: do 50 znaków
   EN: Are you still thinking about blood?
   PL: Are you still thinking about blood?
580. [Umiejętność wroga [837804] (ulepszenie 1) — opis] [WhenUse] 자신에게 [Laceration] 10 부여\n[WhenUse] [BloodDinner]을 최대 20까지 소모하여 자신과 체력이 가장 낮은 아군의 (본체와 부위의) 체력을 (소모한 [BloodDinner] x2) 만큼 회복\n- 아군이 존재하지 않으면, 대신 자신의 체력을 회복량만큼 추가로 회복
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837804].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BloodDinner]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: [WhenUse] Gain 10 [Laceration]\n[WhenUse] Consume up to 20 [BloodDinner]: heal self and the ally(the Core and the Part) with the least HP by ([BloodDinner] consumed x 2).\n- If there are no remaining allies, double the healing on self
   PL: [WhenUse] nakłada na siebie 10 [Laceration]\n[WhenUse] zużywa do 20 [BloodDinner]: przywraca Korpusowi i Części tej jednostki oraz sojusznika z najniższym HP HP równe (zużyte [BloodDinner] x 2)\n- jeżeli nie ma sojuszników, zamiast tego przywraca sobie podwójną wartość leczenia
581. [Umiejętność wroga [837804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Umiejętność wroga [837804] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837804].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Umiejętność wroga [837804] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 현재 체력이 최대 체력의 50% 이상이면, 자신의 [Laceration]을 발동시킴. 자신의 [Laceration] 횟수 1 소모
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837804].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] At 50%+ HP, activate [Laceration] on self. Lose 1 [Laceration] Count on self
   PL: [OnSucceedAttack] przy 50%+ HP uruchamia własne [Laceration]. traci 1 Licznika [Laceration]
584. [Umiejętność wroga [837804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [WornHeart]과 [BloodyHand] 3 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [WornHeart], [BloodyHand]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [WornHeart] = 닳아버린 마음 / Ailing Heart; [BloodyHand] = 피로 물든 손 / Bloodied Hand
   EN: [OnSucceedAttack] Gain 3 [WornHeart] and [BloodyHand]
   PL: [OnSucceedAttack] zyskuje 3 [WornHeart] i [BloodyHand]
585. [Umiejętność wroga [837804] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [WornHeart]이 10이면, [BloodyHand]을 추가로 3 얻고 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837804].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [WornHeart], [BloodyHand], [AttackUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [WornHeart] = 닳아버린 마음 / Ailing Heart; [BloodyHand] = 피로 물든 손 / Bloodied Hand; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttack] At 10 [WornHeart], gain 3 additional [BloodyHand] and gain 1 [AttackUp] next turn
   PL: [OnSucceedAttack] przy 10 [WornHeart], zyskuje dodatkowo 3 [BloodyHand] i 1 [AttackUp] w następnej turze
586. [Umiejętność wroga [837805] (ulepszenie 1) — nazwa] 더 많은 피를...!
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837805].levelList[level=1].name
   limit: do 40 znaków
   EN: More, more blood...!
   PL: More, more blood...!
587. [Umiejętność wroga [837805] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10당 [BloodyHand] 1 얻음\n[WhenUse] 자신에게 [Laceration]을 10 부여\n[WhenUse] [BloodyHand] 3 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837805].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodyHand], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodyHand] = 피로 물든 손 / Bloodied Hand; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodyHand] for every 10 [BloodDinner] consumed\n[WhenUse] Gain 10 [Laceration]\n[WhenUse] Gain 3 [BloodyHand]
   PL: [WhenUse] zużywa do 50 [BloodDinner] i zyskuje 1 [BloodyHand] za każde 10 zużytych [BloodDinner]\n[WhenUse] nakłada na siebie 10 [Laceration]\n[WhenUse] zyskuje 3 [BloodyHand]
588. [Umiejętność wroga [837805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 5 당, [BloodyHand] 1 얻음 (최대 5)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [BloodyHand]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [BloodyHand] = 피로 물든 손 / Bloodied Hand
   EN: [OnSucceedAttack] Gain 1 [BloodyHand] for every 5 [Laceration] on the target (max 5)
   PL: [OnSucceedAttack] zyskuje 1 [BloodyHand] za każde 5 [Laceration] celu (maks. 5)
589. [Umiejętność wroga [837806] (ulepszenie 1) — nazwa] 이토록 풍요로울 수가...
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837806].levelList[level=1].name
   limit: do 40 znaków
   EN: How Bountiful...
   PL: How Bountiful...
590. [Umiejętność wroga [837806] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WhenUse] [BloodDinner]을 최대 30 소모하여, 소모한 [BloodDinner] 10당 코인 위력 +1 (첫번째 코인의 공격 종료시 효과 소멸)\n[DefeatDuel] 다음 턴에 [Vulnerable] 1 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837806].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BloodDinner], [DefeatDuel], [Vulnerable]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile
   EN: [WhenUse] If target has 6+ [Laceration], Coin Power +1\n[WhenUse] Consume up to 30 [BloodDinner]: gain Coin Power +1 for every 10 [BloodDinner] consumed (effect expires after the first Coin attack)\n[DefeatDuel] Gain 1 [Vulnerable] next turn
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1\n[WhenUse] zużywa do 30 [BloodDinner]: Moc Monety +1 za każde 10 zużytych [BloodDinner] (efekt wygasa po ataku pierwszej Monety)\n[DefeatDuel] zyskuje 1 [Vulnerable] w następnej turze
591. [Umiejętność wroga [837806] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837806].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność wroga [837806] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837806].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Umiejętność wroga [837806] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837806].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Umiejętność wroga [837806] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 피해량만큼 체력 회복 (최대 30)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837806].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal HP equal to damage dealt (Max 30)
   PL: [OnSucceedAttack] przywraca HP równe zadanym obrażeniom (maks. 30)
595. [Umiejętność wroga [837806] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 이 스킬에서 [BloodDinner]을 30 소모했고, [BloodyHand_3rd]이 30이면 이 코인 1회 재사용
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837806].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloodDinner], [BloodyHand_3rd]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodyHand_3rd] = 피로 물든 손 III / Bloodied Hand III
   EN: [OnSucceedAttack] If this Skill consumed 30 [BloodDinner], and if this unit is at 30+ [BloodyHand_3rd], Reuse this Coin once
   PL: [OnSucceedAttack] jeżeli ta Umiejętność zużyła 30 [BloodDinner] i jednostka ma 30+ [BloodyHand_3rd], używa Monety ponownie raz
596. [Umiejętność wroga [837806] (ulepszenie 1) — moneta 3, efekt 3 — opis] - 이 스킬에서 [BloodDinner]을 소모하지 못했으면, 자신에게 [Laceration] 20 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837806].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BloodDinner], [Laceration]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed
   EN: - If this unit failed to consume [BloodDinner] with this Skill, gain 20 [Laceration]
   PL: - jeżeli ta Umiejętność nie zużyła [BloodDinner], nakłada na siebie 20 [Laceration]
597. [Umiejętność wroga [837807] (ulepszenie 1) — nazwa] 가족을 위한 헌신
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837807].levelList[level=1].name
   limit: do 40 znaków
   EN: Sacrifice for the Family
   PL: Sacrifice for the Family
598. [Umiejętność wroga [837807] (ulepszenie 1) — opis] [StartBattle] 자신의 현재 체력이 최대 체력의 50% 이상이면, 자신의 [Laceration]을 발동시킴 (최대 3회. 발동된 횟수만큼 출혈 횟수 감소. 이 피해로 흐트러지지 않음)\n[StartBattle] 모든 아군의 정신력 5 회복 (자신 포함)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837807].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Laceration] = 출혈 / Bleed
   EN: [StartBattle] At 50%+ HP, activate [Laceration] on self (max 3 times; reduce Bleed Count every time it is activated; cannot be Staggered from this damage)\n[StartBattle] All allies heal 5 SP (including self)
   PL: [StartBattle] przy 50%+ HP uruchamia własne [Laceration] (do 3 razy; za każdym uruchomieniem traci Licznik Krwawienia; nie Oszołamia się od tych obrażeń)\n[StartBattle] wszyscy sojusznicy (łącznie z tą jednostką) przywracają 5 SP
599. [Umiejętność wroga [837808] (ulepszenie 1) — nazwa] 피를...
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837808].levelList[level=1].name
   limit: do 40 znaków
   EN: Blood...
   PL: Blood...
600. [Umiejętność wroga [837808] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Laceration]이 6 이상 있으면 피해량 +20%
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837808].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 6+ [Laceration], deal +20% damage
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], zadaje +20% obrażeń
601. [Umiejętność wroga [837808] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837808].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Umiejętność wroga [837808] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837808].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Umiejętność wroga [837901] (ulepszenie 1) — nazwa] 애정표현
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837901].levelList[level=1].name
   limit: do 40 znaków
   EN: Expression of Love
   PL: Expression of Love
604. [Umiejętność wroga [837901] (ulepszenie 1) — opis] 부정적인 효과가 적은 대상을 우선으로 지정\n[WhenUse] 대상에게 부정적인 효과가 없으면, 다음 턴에 '거친 애정표현'을 사용\n\n[WhenUse] 대상이 보유한 부정적 효과의 종류 수가 자신의 [FaintMemory] 보다 많으면, 다음 턴에 '서글픈 포옹'을 사용
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837901].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [FaintMemory]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FaintMemory] = 아련한 기억 / Faint Memories
   EN: Prioritizes targets with the least number of negative effects\n[WhenUse] If the target does not have any negative effects, use 'Rough Expression of Love' next turn\n\n[WhenUse] If target has more negative effects than [FaintMemory] on self, use 'A Sad Embrace' next turn
   PL: priorytet: cele z najmniejszą liczbą negatywnych efektów\n[WhenUse] jeżeli cel nie ma żadnych negatywnych efektów, używa w następnej turze „Rough Expression of Love”\n\n[WhenUse] jeżeli liczba typów negatywnych efektów celu przekracza [FaintMemory] tej jednostki, używa w następnej turze „A Sad Embrace”
605. [Umiejętność wroga [837901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Umiejętność wroga [837901] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [AffectionTeddy] 4 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837901].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AffectionTeddy]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AffectionTeddy] = 애착 / Attachment
   EN: [OnSucceedAttack] Inflict 4 [AffectionTeddy]
   PL: [OnSucceedAttack] nakłada 4 [AffectionTeddy]
607. [Umiejętność wroga [837901] (ulepszenie 1) — moneta 1, efekt 3 — opis] [WinDuelAttack] 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837901].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Vulnerable]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Vulnerable] = 취약 / Fragile
   EN: [WinDuelAttack] Inflict 2 [Vulnerable] next turn
   PL: [WinDuelAttack] nakłada 2 [Vulnerable] w następnej turze
608. [Umiejętność wroga [837902] (ulepszenie 1) — nazwa] 할퀴기
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837902].levelList[level=1].name
   limit: do 40 znaków
   EN: Clawing
   PL: Clawing
609. [Umiejętność wroga [837902] (ulepszenie 1) — opis] 부정적인 효과가 적은 대상을 우선으로 지정\n[WinDuel] 다음 턴에 [AffectionTeddy] 3 부여\n[DefeatDuel] 다음 턴에 [AffectionTeddy] 1 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837902].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [AffectionTeddy], [DefeatDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [AffectionTeddy] = 애착 / Attachment; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets with the least number of negative effects\n[WinDuel] Inflict 3 [AffectionTeddy] next turn\n[DefeatDuel] Inflict 1 [AffectionTeddy] next turn
   PL: priorytet: cele z najmniejszą liczbą negatywnych efektów\n[WinDuel] nakłada 3 [AffectionTeddy] w następnej turze\n[DefeatDuel] nakłada 1 [AffectionTeddy] w następnej turze
610. [Umiejętność wroga [837902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Umiejętność wroga [837902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NailPersonality] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 2 [NailPersonality]
   PL: [OnSucceedAttack] nakłada 2 [NailPersonality]
612. [Umiejętność wroga [837903] (ulepszenie 1) — nazwa] 마구 할퀴기
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837903].levelList[level=1].name
   limit: do 40 znaków
   EN: Violent Clawing
   PL: Violent Clawing
613. [Umiejętność wroga [837903] (ulepszenie 1) — opis] 부정적인 효과가 적은 대상을 우선으로 지정\n[WinDuel] 다음 턴에 [AffectionTeddy] 3 부여\n[DefeatDuel] 다음 턴에 [AffectionTeddy] 1 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837903].levelList[level=1].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Umiejętność wroga [837903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Umiejętność wroga [837903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Curse] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Curse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse
   EN: [OnSucceedAttack] Inflict 3 [Curse]
   PL: [OnSucceedAttack] nakłada 3 [Curse]
616. [Umiejętność wroga [837904] (ulepszenie 1) — nazwa] 소심한 애정 표현
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837904].levelList[level=1].name
   limit: do 40 znaków
   EN: Timid Expression of Love
   PL: Timid Expression of Love
617. [Umiejętność wroga [837904] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 다음 턴에 [Disarming] 2 부여\n[WhenUse] [Curse] 1 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Disarming], [Curse]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Disarming] = 수비 위력 감소 / Defense Power Down; [Curse] = 저주 / Curse
   EN: [DuelCounter]\n[WhenUse] Inflict 2 [Disarming] next turn\n[WhenUse] Inflict 1 [Curse]
   PL: [DuelCounter]\n[WhenUse] nakłada 2 [Disarming] w następnej turze\n[WhenUse] nakłada 1 [Curse]
618. [Umiejętność wroga [837904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Umiejętność wroga [837904] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [AffectionTeddy]이 있으면, [AffectionTeddy]을 소모하여 그 수치만큼 [Curse]와 [NailPersonality] 부여 (최대 4 소모)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837904].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AffectionTeddy], [Curse], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AffectionTeddy] = 애착 / Attachment; [Curse] = 저주 / Curse; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] If target has [AffectionTeddy], consume [AffectionTeddy] and inflict [Curse] and [NailPersonality] equal to the value of [AffectionTeddy] consumed (consumes up to 4)
   PL: [OnSucceedAttack] jeżeli cel ma [AffectionTeddy], zużywa [AffectionTeddy] i nakłada [Curse] oraz [NailPersonality] w wysokości zużytego [AffectionTeddy] (zużywa do 4)
620. [Umiejętność wroga [837904] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 [Curse]가 4 이상이면, 대상의 [Curse] 4를 소모하여 [CursePackage] 1 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837904].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Curse], [CursePackage]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse; [CursePackage] = 저주 꾸러미 / Box of Curses
   EN: [OnSucceedAttack] If target has 4+ [Curse], consume 4 [Curse] on the target and inflict 1 [CursePackage]
   PL: [OnSucceedAttack] jeżeli cel ma 4+ [Curse], zużywa 4 [Curse] celu i nakłada 1 [CursePackage]
621. [Umiejętność wroga [837905] (ulepszenie 1) — nazwa] 거친 애정표현
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837905].levelList[level=1].name
   limit: do 40 znaków
   EN: Rough Expression of Love
   PL: Rough Expression of Love
622. [Umiejętność wroga [837905] (ulepszenie 1) — opis] [CantChangeTarget]\n직전 턴에 '애정 표현'으로 합을 한 대상을 지정
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837905].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]
   EN: [CantChangeTarget]\nTargets the target this unit Clashed with 'Expression of Love' last turn
   PL: [CantChangeTarget]\nwskazuje cel ze Starcia „Expression of Love” z poprzedniej tury
623. [Umiejętność wroga [837905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Umiejętność wroga [837905] (ulepszenie 1) — moneta 1, efekt 2 — opis] 대상에게 부정적인 효과가 없으면 피해량 +100%
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837905].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: If the target does not have any negative effects, deal +100% damage
   PL: jeżeli cel nie ma żadnych negatywnych efektów, zadaje +100% obrażeń
625. [Umiejętność wroga [837905] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Curse] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837905].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 615 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Umiejętność wroga [837905] (ulepszenie 1) — moneta 1, efekt 4 — opis] [WinDuelAttack] [NailPersonality] 6 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837905].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [NailPersonality]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [NailPersonality] = 못 / Nails
   EN: [WinDuelAttack] Inflict 6 [NailPersonality]
   PL: [WinDuelAttack] nakłada 6 [NailPersonality]
627. [Umiejętność wroga [837906] (ulepszenie 1) — nazwa] 서글픈 포옹
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837906].levelList[level=1].name
   limit: do 40 znaków
   EN: A Sad Embrace
   PL: A Sad Embrace
628. [Umiejętność wroga [837906] (ulepszenie 1) — opis] [CantChangeTarget]\n직전 턴에 '애정 표현'으로 합을 한 대상을 지정\n대상에게 입히는 피해량이 0으로 고정\n[StartBattle] 다음 턴까지 [Vulnerable] 2 얻음\n[EndBattle] 흐트러짐
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837906].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [StartBattle], [Vulnerable], [EndBattle]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [StartBattle] = [전투 시작시] / [Combat Start]; [Vulnerable] = 취약 / Fragile; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [CantChangeTarget]\nTargets the target this unit Clashed with 'Expression of Love' last turn\nFix the damage dealt against that target to 0\n[StartBattle] Gain 2 [Vulnerable] until next turn\n[EndBattle] Enter Staggered state
   PL: [CantChangeTarget]\nwskazuje cel ze Starcia „Expression of Love” z poprzedniej tury\nobrażenia zadawane temu celowi są zerowe\n[StartBattle] zyskuje 2 [Vulnerable] do następnej tury\n[EndBattle] przechodzi w Oszołamienie
629. [Umiejętność wroga [837906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Umiejętność wroga [837906] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 정신력을 최대로 회복
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837906].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Fully heals the target's SP
   PL: [OnSucceedAttack] przywraca celowi SP do maksimum
631. [Umiejętność wroga [837907] (ulepszenie 1) — nazwa] 그리웠던 옛날의 포옹
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837907].levelList[level=1].name
   limit: do 40 znaków
   EN: An Old, Nostalgic Embrace
   PL: An Old, Nostalgic Embrace
632. [Umiejętność wroga [837907] (ulepszenie 1) — opis] [DefeatDuel] 이 스킬로 적에게 입히는 피해량이 절반으로 감소
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837907].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Deal only half damage against the enemy with this Skill
   PL: [DefeatDuel] zadaje wrogowi jedynie połowę obrażeń tą Umiejętnością
633. [Umiejętność wroga [837907] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Curse] 4 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837907].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Curse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Curse] = 저주 / Curse
   EN: [OnSucceedAttack] Inflict 4 [Curse]
   PL: [OnSucceedAttack] nakłada 4 [Curse]
634. [Umiejętność wroga [837907] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837907].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Umiejętność wroga [837907] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NailPersonality] 4 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837907].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NailPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NailPersonality] = 못 / Nails
   EN: [OnSucceedAttack] Inflict 4 [NailPersonality]
   PL: [OnSucceedAttack] nakłada 4 [NailPersonality]
636. [Umiejętność wroga [837907] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상의 [AffectionTeddy]을 전부 소모\n- 합에서 승리하였다면 (소모한 [AffectionTeddy] x 10)만큼 흐트러짐 피해를 입힘
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837907].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [AffectionTeddy]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AffectionTeddy] = 애착 / Attachment
   EN: [OnSucceedAttack] Consume all [AffectionTeddy] on the target\n- If this unit won the Clash, raise the target's Stagger Threshold by ([AffectionTeddy] consumed x 10)
   PL: [OnSucceedAttack] zużywa całe [AffectionTeddy] celu\n- jeżeli jednostka wygrała Starcie, podnosi Próg Oszołomienia celu o (zużyte [AffectionTeddy] x 10)
637. [Umiejętność wroga [837301] (ulepszenie 1) — nazwa] 찍어누르기
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837301].levelList[level=1].name
   limit: do 40 znaków
   EN: Pin Down
   PL: Pin Down
638. [Umiejętność wroga [837301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 4 [Laceration] i 2 Licznika [Laceration]
639. [Umiejętność wroga [837302] (ulepszenie 1) — nazwa] 꿰뚫린 욕망
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837302].levelList[level=1].name
   limit: do 40 znaków
   EN: Impaled Desire
   PL: Impaled Desire
640. [Umiejętność wroga [837302] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 4 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 4+ [Laceration], Coin Power +1
   PL: [WhenUse] jeżeli cel ma 4+ [Laceration], Moc Monety +1
641. [Umiejętność wroga [837302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Umiejętność wroga [837302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność wroga [837303] (ulepszenie 1) — nazwa] 억누른 욕망
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837303].levelList[level=1].name
   limit: do 40 znaków
   EN: Repressed Desire
   PL: Repressed Desire
644. [Umiejętność wroga [837303] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 4 이상이면, 기본 위력 +2
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 4+ [Laceration], Base Power +2
   PL: [WhenUse] jeżeli cel ma 4+ [Laceration], Moc Bazowa +2
645. [Umiejętność wroga [837303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [WinDuelAttack] 대상이 합동안 잃은 [Laceration] 횟수만큼 [Laceration] 횟수 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Laceration]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuelAttack] Inflict [Laceration] Count equal to the [Laceration] Count the target lost during the Clash
   PL: [WinDuelAttack] nakłada Licznika [Laceration] w wysokości Licznika [Laceration] utraconego przez cel podczas Starcia
646. [Umiejętność wroga [837303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 10 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 10 [Laceration]
   PL: [OnSucceedAttack] nakłada 10 [Laceration]
647. [Umiejętność wroga [837303] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ScarletTakeDamageUp] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837303].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ScarletTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ScarletTakeDamageUp] = 색욕 취약 / Lust Fragility
   EN: [OnSucceedAttack] Inflict 2 [ScarletTakeDamageUp] next turn
   PL: [OnSucceedAttack] nakłada 2 [ScarletTakeDamageUp] w następnej turze
648. [Umiejętność wroga [837304] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837304].levelList[level=1].name
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Umiejętność wroga [837304] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당 보호막 체력 +10 (최대 30)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Shield HP +10 for every 4 [Laceration] on the target (max 30)
   PL: [WhenUse] HP Tarczy +10 za każde 4 [Laceration] celu (maks. 30)
650. [Umiejętność wroga [837401] (ulepszenie 1) — nazwa] 갈아내기
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837401].levelList[level=1].name
   limit: do 40 znaków
   EN: Grinding
   PL: Grinding
651. [Umiejętność wroga [837401] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] zyskuje 2 Licznika [Breath]
652. [Umiejętność wroga [837401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL: [OnSucceedAttack] zyskuje 3 [Breath]
653. [Umiejętność wroga [837401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 652 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [Umiejętność wroga [837401] (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837401].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Vulnerable] = 취약 / Fragile
   EN: [CriticalOnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [CriticalOnSucceedAttack] nakłada 1 [Vulnerable] w następnej turze
655. [Umiejętność wroga [837402] (ulepszenie 1) — nazwa] 분쇄
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837402].levelList[level=1].name
   limit: do 40 znaków
   EN: Crush
   PL: Crush
656. [Umiejętność wroga [837402] (ulepszenie 1) — opis] [WhenUse] [Breath] 5 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 5 [Breath]
   PL: [WhenUse] zyskuje 5 [Breath]
657. [Umiejętność wroga [837402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL: [OnSucceedAttack] zyskuje 2 Licznika [Breath]
658. [Umiejętność wroga [837402] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [IndigoTakeDamageUp] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [IndigoTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [IndigoTakeDamageUp] = 오만 취약 / Pride Fragility
   EN: [OnSucceedAttack] Inflict 2 [IndigoTakeDamageUp] next turn
   PL: [OnSucceedAttack] nakłada 2 [IndigoTakeDamageUp] w następnej turze
659. [Umiejętność wroga [837402] (ulepszenie 1) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837402].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 654 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Umiejętność wroga [837403] (ulepszenie 1) — nazwa] 오만한 분쇄
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837403].levelList[level=1].name
   limit: do 40 znaków
   EN: Prideful Crush
   PL: Prideful Crush
661. [Umiejętność wroga [837403] (ulepszenie 1) — opis] [WhenUse] [Breath]이 5 이상이면, 코인 위력 +2
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837403].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] At 5+ [Breath], Coin Power +2
   PL: [WhenUse] przy 5+ [Breath], Moc Monety +2
662. [Umiejętność wroga [837403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음, [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 4 [Breath] and +3 [Breath] Count
   PL: [OnSucceedAttack] zyskuje 4 [Breath] i 3 Licznika [Breath]
663. [Umiejętność wroga [837403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 피해량 +100%
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Deal +100% damage
   PL: [CriticalOnSucceedAttack] zadaje +100% obrażeń
664. [Umiejętność wroga [837404] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837404].levelList[level=1].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Umiejętność wroga [837404] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 6 이상이면, 코인 위력 +2
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] At 6+ [Breath], Coin Power +2
   PL: [WhenUse] przy 6+ [Breath], Moc Monety +2
666. [Umiejętność wroga [837404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count next turn
   PL: [OnSucceedAttack] zyskuje 2 Licznika [Breath] w następnej turze
667. [Umiejętność wroga [838001] (ulepszenie 1) — nazwa] 무너뜨리기
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838001].levelList[level=1].name
   limit: do 40 znaków
   EN: Topple
   PL: Topple
668. [Umiejętność wroga [838001] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 10 소모하여, [BloodArmor] 1 얻음\n[WhenUse] [BloodArmor] 10 당 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Laceration] 15 당, 코인 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838001].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodArmor], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmor] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Consume 10 [BloodDinner]: gain 1 [BloodArmor]\n[WhenUse] Coin Power +1 for every 10 [BloodArmor] (max 2)\n[WhenUse] Coin Power +1 for every 15 [Laceration] on self (max 3)
   PL: [WhenUse] zużywa 10 [BloodDinner]: zyskuje 1 [BloodArmor]\n[WhenUse] Moc Monety +1 za każde 10 [BloodArmor] (maks. 2)\n[WhenUse] Moc Monety +1 za każde 15 [Laceration] tej jednostki (maks. 3)
669. [Umiejętność wroga [838001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Umiejętność wroga [838001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Umiejętność wroga [838002] (ulepszenie 1) — nazwa] 상처내기
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838002].levelList[level=1].name
   limit: do 40 znaków
   EN: Wound
   PL: Wound
672. [Umiejętność wroga [838002] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 20 소모하여, 소모한 [BloodDinner] 10당 [BloodArmor] 1 얻음\n[WhenUse] [BloodArmor] 10 당 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Laceration] 15 당, 코인 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838002].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodArmor], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmor] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Consume up to 20 [BloodDinner]: gain 1 [BloodArmor] for every 10 [BloodDinner] consumed\n[WhenUse] Coin Power +1 for every 10 [BloodArmor] (max 2)\n[WhenUse] Coin Power +1 for every 15 [Laceration] on self (max 3)
   PL: [WhenUse] zużywa do 20 [BloodDinner]: zyskuje 1 [BloodArmor] za każde 10 zużytych [BloodDinner]\n[WhenUse] Moc Monety +1 za każde 10 [BloodArmor] (maks. 2)\n[WhenUse] Moc Monety +1 za każde 15 [Laceration] tej jednostki (maks. 3)
673. [Umiejętność wroga [838002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Umiejętność wroga [838002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Umiejętność wroga [838003] (ulepszenie 1) — nazwa] 혈희
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838003].levelList[level=1].name
   limit: do 40 znaków
   EN: Sanguine Joy
   PL: Sanguine Joy
676. [Umiejętność wroga [838003] (ulepszenie 1) — opis] [WhenUse] [BloodArmor] 4 소모하여, 정신력 10 회복\n[WhenUse] [BloodDinner]을 10 소모하여, [BloodArmor] 1 얻음, 정신력 10 회복\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 3 얻음.
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838003].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodArmor], [BloodDinner], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodArmor] = 경혈 / Hardblood; [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Consume 4 [BloodArmor] to heal 10 SP\n[WhenUse] Consume 10 [BloodDinner] to gain 1 [BloodArmor] and heal 10 SP\n- If this unit failed to consume [BloodDinner], gain 3 [Laceration].
   PL: [WhenUse] zużywa 4 [BloodArmor], by przywrócić 10 SP\n[WhenUse] zużywa 10 [BloodDinner], by zyskać 1 [BloodArmor] i przywrócić 10 SP\n- jeżeli nie udało się zużyć [BloodDinner], zyskuje 3 [Laceration].
677. [Umiejętność wroga [838003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]당, 피해량 +10% (최대 100%)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Deal +10% damage for every [Laceration] on the target (max 100%)
   PL: [OnSucceedAttack] zadaje +10% obrażeń za każde [Laceration] celu (maks. 100%)
678. [Umiejętność wroga [838003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Umiejętność wroga [838004] (ulepszenie 1) — nazwa] 피의 환희
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838004].levelList[level=1].name
   limit: do 40 znaków
   EN: Ecstasy of Blood
   PL: Ecstasy of Blood
680. [Umiejętność wroga [838004] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[StartBattle] 적 중 [Laceration]을 가진 적이 있다면, 모든 적의 [Laceration]을 발동시킴. [Laceration] 횟수 2 감소\n[WhenUse] 전투 시작 시 효과가 발동하지 않았다면, [Laceration] 30 얻음.\n[WinDuel] [BloodDinner]을 최대 40 소모하여, 소모한 [BloodDinner] 10당, [BloodArmor] 1 얻고 피해량 +25% (최대 100%)\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻고 발동시킴. [Laceration] 횟수 2 감소\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838004].levelList[level=1].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Laceration], [WhenUse], [WinDuel], [BloodDinner], [BloodArmor], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmor] = 경혈 / Hardblood; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Can Clash with this Skill regardless of Speed\n[StartBattle] If there are enemies with [Laceration], activate [Laceration] on all enemies. All enemies lose 2 [Laceration] Count\n[WhenUse] If this effect did not activate at Combat Start, gain 30 [Laceration].\n[WinDuel] Consume up to 40 [BloodDinner]: for every 10 [BloodDinner] consumed, gain 1 [BloodArmor] and deal +25% damage (max 100%)\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration], and activate [Laceration] immediately. Lose 2 [Laceration] Count\n[EndSkill] Ends this turn
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[StartBattle] jeżeli istnieją wrogowie z [Laceration], uruchamia [Laceration] u wszystkich wrogów. wszyscy wrogowie tracą 2 Licznika [Laceration]\n[WhenUse] jeżeli ten efekt nie uruchomił się na Początku walki, zyskuje 30 [Laceration].\n[WinDuel] zużywa do 40 [BloodDinner]: za każde 10 zużytych [BloodDinner] zyskuje 1 [BloodArmor] i zadaje +25% obrażeń (maks. 100%)\n- jeżeli nie udało się zużyć [BloodDinner], zyskuje 5 [Laceration] i natychmiast uruchamia [Laceration]. traci 2 Licznika [Laceration]\n[EndSkill] kończy tę turę
681. [Umiejętność wroga [838004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Umiejętność wroga [838004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 5 [Laceration] i 2 Licznika [Laceration]
683. [Umiejętność wroga [838004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Umiejętność wroga [838004] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838004].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Umiejętność wroga [838004] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838004].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Umiejętność wroga [838005] (ulepszenie 1) — nazwa] 돈키호테류 경혈 4식 - 도려내기
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838005].levelList[level=1].name
   limit: do 60 znaków
   EN: Don Quixote Hardblood Arts 4 - Sundering
   PL: Don Quixote Hardblood Arts 4 - Sundering
687. [Umiejętność wroga [838005] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WinDuel] [BloodArmor] 단계에 따라, 이 스킬의 피해량 +20% (최대 60%)\n[DefeatDuel] [BloodArmor] 4 소모하여, 보호막 체력 20 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838005].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [WinDuel], [BloodArmor], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [BloodArmor] = 경혈 / Hardblood; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If target has 6+ [Laceration], Coin Power +1\n[WinDuel] With this Skill, deal +20% damage with every Stage of [BloodArmor] (max 60%)\n[DefeatDuel] Consume 4 [BloodArmor] to gain 20 Shield HP
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1\n[WinDuel] tą Umiejętnością zadaje +20% obrażeń za każdy Etap [BloodArmor] (maks. 60%)\n[DefeatDuel] zużywa 4 [BloodArmor], by zyskać 20 HP Tarczy
688. [Umiejętność wroga [838005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL: [OnSucceedAttack] nakłada 5 [Laceration]
689. [Umiejętność wroga [838005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 688 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Umiejętność wroga [838006] (ulepszenie 1) — nazwa] 돈키호테류 경혈11식 - 후벼파기
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838006].levelList[level=1].name
   limit: do 60 znaków
   EN: Don Quixote Hardblood Arts 11 - Impaling
   PL: Don Quixote Hardblood Arts 11 - Impaling
691. [Umiejętność wroga [838006] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 3당, 기본 위력 +1 (최대 3)\n[WinDuel] [BloodArmor] 단계에 따라, 이 스킬의 피해량 +20% (최대 60%)\n[DefeatDuel] [BloodArmor] 4 소모하여, 보호막 체력 20 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838006].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [WinDuel], [BloodArmor], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [BloodArmor] = 경혈 / Hardblood; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Base Power +1 for every 3 [Laceration] on the target (max 3)\n[WinDuel] With this Skill, deal +20% damage with every Stage of [BloodArmor] (max 60%)\n[DefeatDuel] Consume 4 [BloodArmor] to gain 20 Shield HP
   PL: [WhenUse] Moc Bazowa +1 za każde 3 [Laceration] celu (maks. 3)\n[WinDuel] tą Umiejętnością zadaje +20% obrażeń za każdy Etap [BloodArmor] (maks. 60%)\n[DefeatDuel] zużywa 4 [BloodArmor], by zyskać 20 HP Tarczy
692. [Umiejętność wroga [838006] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Umiejętność wroga [838006] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838006].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Umiejętność wroga [838006] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration]을 횟수만큼 발동시킴. 대상의 [Laceration] 횟수를 1까지 소모시킴
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838006].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on the target equal to its Count. Use up the target's [Laceration] Count down to 1
   PL: [OnSucceedAttack] uruchamia [Laceration] celu tyle razy, ile wynosi jego Licznik. zużywa Licznik [Laceration] celu do 1
695. [Umiejętność wroga [838007] (ulepszenie 1) — nazwa] 돈키호테류 경혈 2식 - 경혈
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838007].levelList[level=1].name
   limit: do 60 znaków
   EN: Don Quixote Hardblood Arts 2 - Hardblood
   PL: Don Quixote Hardblood Arts 2 - Hardblood
696. [Umiejętność wroga [838007] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[StartBattle] [BloodDinner]을 200 소모하여, 500만큼 보호막 체력 얻고 [BloodArmor] 5, [SwirlingBlood] 1 얻음\n- [BloodDinner]이 부족할 경우, [Laceration] 50을 얻고 발동시킴. [Laceration] 횟수 2 감소. 500만큼 보호막 체력을 얻고 [BloodArmor] 5, [SwirlingBlood] 1 얻음 (이 피해로 체력이 1미만이 되지 않음)\n[WinDuel] 200만큼 보호막 체력을 얻음\n[DefeatDuel] 이 스킬로 얻은 보호막 효과가 있는 동안 [Vulnerable]을 3 얻음\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838007].levelList[level=1].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [BloodDinner], [BloodArmor], [SwirlingBlood], [Laceration], [WinDuel], [DefeatDuel], [Vulnerable], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmor] = 경혈 / Hardblood; [SwirlingBlood] = 일렁임【혈귀】 / Shimmering【Bloodfiend】; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile …
   EN: Can Clash with this Skill regardless of Speed\n[StartBattle] Consume 200 [BloodDinner], gain 500 Shield HP, 5 [BloodArmor], and 1 [SwirlingBlood]\n- If this unit doesn't have enough [BloodDinner], gain 50 [Laceration], and activate [Laceration] immediately. Lose 2 [Laceration] Count. Gain 500 Shield HP and 1 [SwirlingBlood] (this damage does not reduce this unit's HP to 1)\n[WinDuel] Gain 200 Shield HP\n[DefeatDuel] Gain 3 [Vulnerable] as long as the Shield gained due to this Skill is active\n[DefeatDuel] Deal -50% damage, and the damage from this Skill does not Stagger the target\n[EndSkill] Ends this turn
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[StartBattle] zużywa 200 [BloodDinner], zyskuje 500 HP Tarczy, 5 [BloodArmor] i 1 [SwirlingBlood]\n- jeżeli brakuje [BloodDinner], zyskuje 50 [Laceration] i natychmiast uruchamia [Laceration]. traci 2 Licznika [Laceration]. zyskuje 500 HP Tarczy oraz 5 [BloodArmor] i 1 [SwirlingBlood] (te obrażenia nie obniżają HP jednostki poniżej 1)\n[WinDuel] zyskuje 200 HP Tarczy\n[DefeatDuel] zyskuje 3 [Vulnerable], dopóki aktywna jest Tarcza zdobyta dzięki tej Umiejętności\n[DefeatDuel] zadaje -50% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu\n[EndSkill] kończy tę turę
697. [Umiejętność wroga [838007] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838007].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Umiejętność wroga [838007] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838007].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Umiejętność wroga [838007] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838007].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Umiejętność wroga [838007] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838007].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Umiejętność wroga [838007] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838007].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 5 [Laceration] i 3 Licznika [Laceration]
702. [Umiejętność wroga [838008] (ulepszenie 1) — nazwa] 돈키호테 아류 산초 4식 - 추적
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838008].levelList[level=1].name
   limit: do 70 znaków
   EN: Variant Don Quixote Style: Sancho Arts 4 - Track
   PL: Variant Don Quixote Style: Sancho Arts 4 - Track
703. [Umiejętność wroga [838008] (ulepszenie 1) — opis] [Laceration]이 가장 많은 대상 우선 공격\n[BeforeAttack] [Laceration]이 가장 많은 대상이면, 공격 가중치 +2, 합 위력 +3\n[WhenUse] [BloodDinner]을 최대 30 소모하여, 소모한 [BloodDinner] 15당 [BloodArmor] 1 얻음. 코인 위력 +1 (최대 2)\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻고 발동시킴. [Laceration] 횟수 1 감소\n[EndSkill] 이 스킬로 입히는 피해량만큼 [BloodDinner] 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838008].levelList[level=1].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BeforeAttack], [WhenUse], [BloodDinner], [BloodArmor], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmor] = 경혈 / Hardblood; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Prioritizes targets with the most [Laceration]\n[BeforeAttack] If the target is the one with the most [Laceration], gain Atk Weight +2 and Clash Power +3\n[WhenUse] Consume up to 30 [BloodDinner]: gain 1 [BloodArmor] and Coin Power +1 for every 15 [BloodDinner] consumed (max 2)\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration], and activate [Laceration] immediately. Lose 2 [Laceration] Count\n[EndSkill] Increase [BloodDinner] equal to the damage this Skill dealt
   PL: priorytet: cel z największą liczbą [Laceration]\n[BeforeAttack] jeżeli celem jest jednostka z największą liczbą [Laceration], Waga Ataku +2 i Moc Starcia +3\n[WhenUse] zużywa do 30 [BloodDinner]: zyskuje 1 [BloodArmor] i Moc Monety +1 za każde 15 zużytych [BloodDinner] (maks. 2)\n- jeżeli nie udało się zużyć [BloodDinner], zyskuje 10 [Laceration] i natychmiast uruchamia [Laceration]. traci 1 Licznika [Laceration]\n[EndSkill] zwiększa [BloodDinner] o wartość obrażeń zadanych tą Umiejętnością
704. [Umiejętność wroga [838008] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838008].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Umiejętność wroga [838008] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여\n- 이 스킬에서 [BloodDinner]을 30 소모했다면, [Binding] 2 추가 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838008].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Binding], [BloodDinner]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [BloodDinner] = 혈찬 / Bloodfeast
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn\n- If this Skill consumed 30 [BloodDinner], inflict 2 additional [Binding]
   PL: [OnSucceedAttack] nakłada 1 [Binding] w następnej turze\n- jeżeli ta Umiejętność zużyła 30 [BloodDinner], nakłada dodatkowo 2 [Binding]
706. [Umiejętność wroga [838009] (ulepszenie 1) — nazwa] 돈키호테 아류 산초 3식 - 기습
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838009].levelList[level=1].name
   limit: do 70 znaków
   EN: Variant Don Quixote Style: Sancho Arts 3 - Ambush
   PL: Variant Don Quixote Style: Sancho Arts 3 - Ambush
707. [Umiejętność wroga [838009] (ulepszenie 1) — opis] [Laceration]이 가장 많은 대상 우선 공격\n[BeforeAttack] [Laceration]이 가장 많은 대상이면, 공격 가중치 +2, 합 위력 +3\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10당 [BloodArmor] 1 얻음. 기본 위력 +1 (최대 5)\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻고 발동시킴. [Laceration] 횟수 1 감소\n[EndSkill] 이 스킬로 입히는 피해량만큼 [BloodDinner] 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838009].levelList[level=1].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BeforeAttack], [WhenUse], [BloodDinner], [BloodArmor], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmor] = 경혈 / Hardblood; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Prioritizes targets with the most [Laceration]\n[BeforeAttack] If the target is the one with the most [Laceration], gain Atk Weight +2 and Clash Power +3\n[WhenUse] Consume up to 50 [BloodDinner]: gain 1 [BloodArmor] and Base Power +1 for every 10 [BloodDinner] consumed (max 5)\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration], and activate [Laceration] immediately. Lose 1 [Laceration] Count\n[EndSkill] Increase [BloodDinner] equal to the damage this Skill dealt
   PL: priorytet: cel z największą liczbą [Laceration]\n[BeforeAttack] jeżeli celem jest jednostka z największą liczbą [Laceration], Waga Ataku +2 i Moc Starcia +3\n[WhenUse] zużywa do 50 [BloodDinner]: zyskuje 1 [BloodArmor] i Moc Bazowa +1 za każde 10 zużytych [BloodDinner] (maks. 5)\n- jeżeli nie udało się zużyć [BloodDinner], zyskuje 10 [Laceration] i natychmiast uruchamia [Laceration]. traci 1 Licznika [Laceration]\n[EndSkill] zwiększa [BloodDinner] o wartość obrażeń zadanych tą Umiejętnością
708. [Umiejętność wroga [838009] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838009].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Umiejętność wroga [838009] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838009].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Umiejętność wroga [838009] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여\n- 이 스킬에서 [BloodDinner]을 50 소모했다면, [Paralysis] 2 추가 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838009].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Paralysis], [BloodDinner]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze; [BloodDinner] = 혈찬 / Bloodfeast
   EN: [OnSucceedAttack] Inflict 1 [Paralysis] next turn\n- If this Skill consumed 50 [BloodDinner], inflict 2 additional [Paralysis]
   PL: [OnSucceedAttack] nakłada 1 [Paralysis] w następnej turze\n- jeżeli ta Umiejętność zużyła 50 [BloodDinner], nakłada dodatkowo 2 [Paralysis]
711. [Umiejętność wroga [838010] (ulepszenie 1) — nazwa] 돈키호테 아류 산초 2식 - 라 샹그레
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838010].levelList[level=1].name
   limit: do 70 znaków
   EN: Variant Don Quixote Style: Sancho Arts 2 - La Sangre
   PL: Variant Don Quixote Style: Sancho Arts 2 - La Sangre
712. [Umiejętność wroga [838010] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse] [BloodDinner]을 50 소모하여, 대상과 자신에게 [Paralysis] 1 부여\n[WhenUse] [BloodDinner]을 100 소모하여, 합 위력 +5\n- [BloodDinner]이 부족할 경우, 자신의 체력을 100 소모하여 합 위력 +5\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838010].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [Paralysis], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [Paralysis] = 마비 / Paralyze; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse] Consume 50 [BloodDinner] to inflict 1 [Paralysis] against the target and self\n[WhenUse] Consume 100 [BloodDinner] to gain Clash Power +5\n- If there isn't enough [BloodDinner], consume 100 HP from this unit to gain Clash Power +5\n[EndSkill] Ends this turn
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse] zużywa 50 [BloodDinner], by nakładać 1 [Paralysis] na cel i siebie\n[WhenUse] zużywa 100 [BloodDinner], by zyskać Moc Starcia +5\n- jeżeli brakuje [BloodDinner], zużywa 100 własnego HP, by zyskać Moc Starcia +5\n[EndSkill] kończy tę turę
713. [Umiejętność wroga [838010] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838010].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Umiejętność wroga [838010] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 8 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838010].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Umiejętność wroga [838010] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 피해량만큼 체력 회복
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838010].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal by damage dealt
   PL: [OnSucceedAttackHead] przywraca HP równe zadanym obrażeniom
716. [Umiejętność wroga [838011] (ulepszenie 1) — nazwa] 라 어벤투라 아 테르미나도
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838011].levelList[level=1].name
   limit: do 40 znaków
   EN: La Aventura Ha Terminado
   PL: La Aventura Ha Terminado
717. [Umiejętność wroga [838011] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 (45 - 현재 정신력)만큼 소모하여 정신력을 45까지 회복\n- [BloodDinner]이 부족할 경우, 자신의 체력을 (45 - 현재 정신력)만큼 소모하여 정신력을 45까지 회복 (이 피해로 체력이 1미만이 되지 않음)\n- 남은 [BloodDinner]만큼 보호막 체력을 얻음 (최대 100)\n[WinDuel] 대상에게 [Laceration] 10 부여\n[DefeatDuel] [BloodDinner] 100 소모\n[EndSkill] 피해량만큼 [BloodDinner] 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838011].levelList[level=1].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [WinDuel], [Laceration], [DefeatDuel], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Consume (45 - current SP) [BloodDinner] to heal up to 45 SP\n- If there isn't enough [BloodDinner], consume up to (45 - current SP) HP to heal up to 45 SP (this damage does not lower this unit's HP below 1)\n- Gain Shield HP equal to the remaining [BloodDinner] (max 100)\n[WinDuel] Inflict 10 [Laceration]\n[DefeatDuel] Consume 100 [BloodDinner]\n[EndSkill] Increase [BloodDinner] equal to the damage dealt
   PL: [WhenUse] zużywa (45 - aktualne SP) [BloodDinner], by przywrócić SP do 45\n- jeżeli brakuje [BloodDinner], zużywa tyle własnego HP, ile wynosi (45 - aktualne SP), by przywrócić SP do 45 (te obrażenia nie obniżają HP jednostki poniżej 1)\n- zyskuje HP Tarczy równe pozostałemu [BloodDinner] (maks. 100)\n[WinDuel] nakłada 10 [Laceration]\n[DefeatDuel] zużywa 100 [BloodDinner]\n[EndSkill] zwiększa [BloodDinner] o wartość zadanych obrażeń
718. [Umiejętność wroga [838011] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838011].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Umiejętność wroga [838011] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]당, 피해량 +10% (최대 200%)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838011].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Deal +10% damage for every [Laceration] on the target (max 200%)
   PL: [OnSucceedAttack] zadaje +10% obrażeń za każde [Laceration] celu (maks. 200%)
720. [Umiejętność wroga [838011] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [BloodDinner]당 피해량 +10% (최대 100%)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838011].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloodDinner]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodDinner] = 혈찬 / Bloodfeast
   EN: [OnSucceedAttack] Deal +10% damage for every [BloodDinner] (max 100%)
   PL: [OnSucceedAttack] zadaje +10% obrażeń za każde [BloodDinner] (maks. 100%)
721. [Umiejętność wroga [838011] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=838011].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Umiejętność wroga [839401] (ulepszenie 1) — nazwa] 키기기이긱
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839401].levelList[level=1].name
   limit: do 40 znaków
   EN: Keeehhhhnnhhh
   PL: Keeehhhhnnhhh
723. [Umiejętność wroga [839401] (ulepszenie 1) — opis] [WhenUse] [DefenseUp] 3을 얻음\n[DefeatDuel] [DefenseUp] 3을 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefenseUp], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain 3 [DefenseUp]\n[DefeatDuel] Gain 3 [DefenseUp]
   PL: [WhenUse] zyskuje 3 [DefenseUp]\n[DefeatDuel] zyskuje 3 [DefenseUp]
724. [Umiejętność wroga [839401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 2를 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 2 [DefenseUp] next turn
   PL: [OnSucceedAttack] zyskuje 2 [DefenseUp] w następnej turze
725. [Umiejętność wroga [839401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 2를 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 724 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Umiejętność wroga [839402] (ulepszenie 1) — nazwa] 키이 이익
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839402].levelList[level=1].name
   limit: do 40 znaków
   EN: Knnhgh nhhnnh
   PL: Knnhgh nhhnnh
727. [Umiejętność wroga [839402] (ulepszenie 1) — opis] [WinDuel] 다음 턴에 [Binding] 1 부여\n[WhenUse] 자신의 [DefenseUp] 4 당, 기본 위력 +1 (최대 2)\n[WhenUse] [DefenseUp] 3을 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839402].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Binding], [WhenUse], [DefenseUp]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Binding] = 속박 / Bind; [WhenUse] = [사용시] / [On Use]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WinDuel] Inflict 1 [Binding] next turn\n[WhenUse] Base Power +1 for every 4 [DefenseUp] on self (max 2)\n[WhenUse] Gain 3 [DefenseUp]
   PL: [WinDuel] nakłada 1 [Binding] w następnej turze\n[WhenUse] Moc Bazowa +1 za każde 4 [DefenseUp] tej jednostki (maks. 2)\n[WhenUse] zyskuje 3 [DefenseUp]
728. [Umiejętność wroga [839402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 2 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 2 [DefenseUp] next turn
   PL: [OnSucceedAttack] zyskuje 2 [DefenseUp] w następnej turze
729. [Umiejętność wroga [839402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 2 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 728 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Umiejętność wroga [839402] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 2 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 728 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność wroga [839403] (ulepszenie 1) — nazwa] 키이익
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839403].levelList[level=1].name
   limit: do 40 znaków
   EN: Knngghh
   PL: Knngghh
732. [Umiejętność wroga [839403] (ulepszenie 1) — opis] [StartBattle] 자신을 포함한 체력 비율이 가장 적은 아군 1명 [DefenseUp] 3 부여\n[WhenUse] 자신의 [DefenseUp] 5 당 기본 위력 +1 (최대 4)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839403].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefenseUp], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Apply 3 [DefenseUp] to 1 ally, including this unit, with the least HP percentage\n[WhenUse] Base Power +1 for every 5 [DefenseUp] on self (max 4)
   PL: [StartBattle] nakłada 3 [DefenseUp] na 1 sojusznika (łącznie z tą jednostką) z najniższym procentem HP\n[WhenUse] Moc Bazowa +1 za każde 5 [DefenseUp] tej jednostki (maks. 4)
733. [Umiejętność wroga [839403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp]만큼 공격 레벨 증가 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain Offense Level Up equal to [DefenseUp] next turn
   PL: [OnSucceedAttack] zyskuje Wzrost Poziomu Ataku w następnej turze równy [DefenseUp]
734. [Umiejętność wroga [839404] (ulepszenie 1) — nazwa] 키긱
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839404].levelList[level=1].name
   limit: do 40 znaków
   EN: Knnh
   PL: Knnh
735. [Umiejętność wroga [839404] (ulepszenie 1) — opis] [StartBattle] (자신의 [DefenseUp] X 2)만큼 보호막을 얻음 (최대 20, 턴 당 2회)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [DefenseUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [StartBattle] Gain 2 x ([DefenseUp] on self) Shield HP (max 20, 2 times per turn)
   PL: [StartBattle] zyskuje Tarczę równą (2 x [DefenseUp] tej jednostki) HP Tarczy (maks. 20, 2 razy na turę)
736. [Umiejętność wroga [837601] (ulepszenie 1) — nazwa] 가시 채찍
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837601].levelList[level=1].name
   limit: do 40 znaków
   EN: Spiked Whip
   PL: Spiked Whip
737. [Umiejętność wroga [837601] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 6 이상이면, 합 위력 +1
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 6+ [Burst], Clash Power +1
   PL: [WhenUse] jeżeli cel ma 6+ [Burst], Moc Starcia +1
738. [Umiejętność wroga [837601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Umiejętność wroga [837602] (ulepszenie 1) — nazwa] 채찍 휘두르기
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837602].levelList[level=1].name
   limit: do 40 znaków
   EN: Whip Crack
   PL: Whip Crack
740. [Umiejętność wroga [837602] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 6 이상이면, 코인 위력 +1\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has 6+ [Burst], Coin Power +1\n[WinDuel] Inflict +2 [Burst] Count
   PL: [WhenUse] jeżeli cel ma 6+ [Burst], Moc Monety +1\n[WinDuel] nakłada 2 Licznika [Burst]
741. [Umiejętność wroga [837602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Burst] 횟수가 5 미만이면, [Burst] 횟수 2 증가\n- 5 이상이면, 대신하여 [Burst] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has less than 5 [Burst] Count, inflict +2 [Burst] Count\n- At 5+ [Burst] Count, inflict 2 [Burst] instead
   PL: [OnSucceedAttack] jeżeli cel ma mniej niż 5 Licznika [Burst], nakłada 2 Licznika [Burst]\n- przy 5+ Licznika [Burst], zamiast tego nakłada 2 [Burst]
742. [Umiejętność wroga [837602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Burst] 횟수가 5 미만이면, [Burst] 횟수 2 증가\n- 5 이상이면, 대신하여 [Burst] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 741 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [Umiejętność wroga [837603] (ulepszenie 1) — nazwa] 옭아매는 가시관
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837603].levelList[level=1].name
   limit: do 40 znaków
   EN: Strangling Crown of Thorns
   PL: Strangling Crown of Thorns
744. [Umiejętność wroga [837603] (ulepszenie 1) — opis] 정신력이 가장 낮은 대상 우선 공격\n[WhenUse] 대상의 정신력이 0 이하라면, 합 위력 +3\n[WhenUse] 대상의 [Burst] 4당, 코인 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837603].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: Prioritizes targets with the lowest SP\n[WhenUse] If target has 0- SP, Clash Power +3\n[WhenUse] Coin Power +1 for every 4 [Burst] on the target (max 3)
   PL: priorytet: cel z najniższym SP\n[WhenUse] jeżeli SP celu wynosi 0 lub mniej, Moc Starcia +3\n[WhenUse] Moc Monety +1 za każde 4 [Burst] celu (maks. 3)
745. [Umiejętność wroga [837603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력 10 피해\n- 대상의 정신력이 0 이하라면, 대신하여 정신력 20 피해
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 10 SP damage\n- If target has 0- SP, deal 20 SP damage instead
   PL: [OnSucceedAttack] zadaje 10 obrażeń SP\n- jeżeli SP celu wynosi 0 lub mniej, zamiast tego zadaje 20 obrażeń SP
746. [Umiejętność wroga [837604] (ulepszenie 1) — nazwa] 채찍 거두기
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837604].levelList[level=1].name
   limit: do 40 znaków
   EN: Withdraw Whip
   PL: Withdraw Whip
747. [Umiejętność wroga [837604] (ulepszenie 1) — opis] [ThornNoose]를 가진 대상 우선 공격\n[ThornNoose]가 없는 대상일 경우, 피해량이 50% 감소
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837604].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [ThornNoose]
   znaczenie tagów: [ThornNoose] = 가시 올가미 / Barbed Lasso
   EN: Prioritizes targets with [ThornNoose]\nIf the target does not have [ThornNoose], deal -50% damage
   PL: priorytet: cele z [ThornNoose]\njeżeli cel nie ma [ThornNoose], zadaje o 50% mniej obrażeń
748. [Umiejętność wroga [837604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [ThornNoose]가 있으면, [Burst] 2 부여\n- 대상의 [Burst]이 10이상이면, 대신하여 [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [ThornNoose], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThornNoose] = 가시 올가미 / Barbed Lasso; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If the target has [ThornNoose], inflict 2 [Burst]\n- If the target has 10+ [Burst], inflict +2 [Burst] Count instead
   PL: [OnSucceedAttack] jeżeli cel ma [ThornNoose], nakłada 2 [Burst]\n- jeżeli cel ma 10+ [Burst], zamiast tego nakłada 2 Licznika [Burst]
749. [Umiejętność wroga [837604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [ThornNoose]가 있으면, [Burst] 2 부여\n- 대상의 [Burst]이 10이상이면, 대신하여 [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 748 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [Umiejętność wroga [837604] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [ThornNoose]가 있으면, [Burst] 2 부여\n- 대상의 [Burst]이 10이상이면, 대신하여 [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837604].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 748 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Umiejętność wroga [837604] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837604].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [Umiejętność wroga [837604] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [ThornNoose]가 있으면, 피해량 +50%
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837604].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ThornNoose]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThornNoose] = 가시 올가미 / Barbed Lasso
   EN: [OnSucceedAttack] If target has [ThornNoose], deal +50% damage
   PL: [OnSucceedAttack] jeżeli cel ma [ThornNoose], zadaje +50% obrażeń
753. [Umiejętność wroga [837605] (ulepszenie 1) — nazwa] 가시 올가미
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837605].levelList[level=1].name
   (powtórzenie elementu 532 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Umiejętność wroga [837605] (ulepszenie 1) — opis] [WhenUse] 대상의 속도보다 자신의 속도가 빠르다면, 합 위력 +5\n[WhenUse] 대상의 [Burst] 4당, 코인 위력 +1 (최대 2)\n[WhenUse] [ThornNoose]를 가지고 있는 대상만큼 기본 위력이 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837605].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [ThornNoose]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [ThornNoose] = 가시 올가미 / Barbed Lasso
   EN: [WhenUse] If this unit's Speed is faster than the target's, Clash Power +5\n[WhenUse] Coin Power +1 for every 4 [Burst] on the target (max 2)\n[WhenUse] Gain Base Power by the number of targets with [ThornNoose]
   PL: [WhenUse] jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Starcia +5\n[WhenUse] Moc Monety +1 za każde 4 [Burst] celu (maks. 2)\n[WhenUse] Moc Bazowa rośnie o liczbę celów z [ThornNoose]
755. [Umiejętność wroga [837605] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837605].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Umiejętność wroga [837605] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Burst] 4, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837605].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Burst] and +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 4 [Burst] i 2 Licznika [Burst]
757. [Umiejętność wroga [837605] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 대상이 흐트러짐 상태이거나 [ThornNoose]가 있으면, 피해량 +30%
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837605].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ThornNoose]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThornNoose] = 가시 올가미 / Barbed Lasso
   EN: [OnSucceedAttack] If target is Staggered or has [ThornNoose], deal +30% damage
   PL: [OnSucceedAttack] jeżeli cel jest w Oszołamieniu lub ma [ThornNoose], zadaje +30% obrażeń
758. [Umiejętność wroga [837605] (ulepszenie 1) — moneta 4, efekt 4 — opis] [EnemyKill] (대상의 [Burst] 횟수 * 2)만큼 모든 적에게 [Burst] 부여 (최대 10)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837605].levelList[level=1].coinlist[#3].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Burst]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Burst] = 파열 / Rupture
   EN: [EnemyKill] Inflict ([Burst] Count on the target x 2) [Burst] against all enemies (max 10)
   PL: [EnemyKill] nakłada [Burst] w wysokości (Licznik [Burst] celu x 2) wszystkim wrogom (maks. 10)
759. [Umiejętność wroga [837606] (ulepszenie 1) — nazwa] 채찍 두르기
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837606].levelList[level=1].name
   limit: do 40 znaków
   EN: Whip Wreath
   PL: Whip Wreath
760. [Umiejętność wroga [837606] (ulepszenie 1) — opis] [StartBattle] 현재 체력의 ([ThornNoose]를 가진 적 수)%만큼 보호막을 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837606].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [ThornNoose]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ThornNoose] = 가시 올가미 / Barbed Lasso
   EN: [StartBattle] Gain (number of enemies with [ThornNoose])% of HP as Shield
   PL: [StartBattle] zyskuje Tarczę równą (liczba wrogów z [ThornNoose])% aktualnego HP
761. [Umiejętność wroga [837607] (ulepszenie 1) — nazwa] 부여잡는 올가미
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837607].levelList[level=1].name
   limit: do 40 znaków
   EN: Snaring Lasso
   PL: Snaring Lasso
762. [Umiejętność wroga [837607] (ulepszenie 1) — opis] [StartBattle] [ThornNoose]를 가진 적이 3명 이하라면, [ThornNoose] 1 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837607].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [ThornNoose]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ThornNoose] = 가시 올가미 / Barbed Lasso
   EN: [StartBattle] If there are 3- enemies with [ThornNoose], inflict 1 [ThornNoose]
   PL: [StartBattle] jeżeli jest 3 lub mniej wrogów z [ThornNoose], nakłada 1 [ThornNoose]
763. [Umiejętność wroga [837607] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837607].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Umiejętność wroga [837607] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837607].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Umiejętność wroga [837701] (ulepszenie 1) — nazwa] 가시
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837701].levelList[level=1].name
   limit: do 40 znaków
   EN: Thorns
   PL: Thorns
766. [Umiejętność wroga [837701] (ulepszenie 1) — opis] [CantChangeTarget]\n가시 올가미를 가진 대상 우선 공격
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]
   EN: [CantChangeTarget]\nPrioritizes targets with Barbed Lasso
   PL: [CantChangeTarget]\npriorytet: cele z Barbed Lasso
767. [Umiejętność wroga [837701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Burst] and +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 4 [Burst] i 2 Licznika [Burst]
768. [Umiejętność wroga [839601] (ulepszenie 1) — nazwa] 고귀하게...
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839601].levelList[level=1].name
   limit: do 40 znaków
   EN: Gracefully...
   PL: Gracefully...
769. [Umiejętność wroga [839601] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 6+ [Laceration], Coin Power +1
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Monety +1
770. [Umiejętność wroga [839601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Umiejętność wroga [839601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [Umiejętność wroga [839001] (ulepszenie 1) — nazwa] 끝나지 않는 축제
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839001].levelList[level=1].name
   limit: do 40 znaków
   EN: The Infinite Parade
   PL: The Infinite Parade
773. [Umiejętność wroga [839001] (ulepszenie 1) — opis] [CantDuel]\n대상이 수비 스킬을 사용했으면 피해량 -100%\n[WhenUse] 다음 턴에 곤돌라 1개를 생성
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839001].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]
   EN: [CantDuel]\nIf the target used a Defense Skill, deal -100% damage\n[WhenUse] Generate 1 Gondola next turn
   PL: [CantDuel]\njeżeli cel użył Umiejętności obrony, zadaje -100% obrażeń\n[WhenUse] generuje 1 Gondolę w następnej turze
774. [Umiejętność wroga [839002] (ulepszenie 1) — nazwa] 영원한 축제
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839002].levelList[level=1].name
   limit: do 40 znaków
   EN: The Eternal Festival
   PL: The Eternal Festival
775. [Umiejętność wroga [839002] (ulepszenie 1) — opis] [CantDuel]\n대상이 수비 스킬을 사용했으면 피해량 -100%\n[WhenUse] 다음 턴에 곤돌라 4개를 생성
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=839002].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]
   EN: [CantDuel]\nIf the target used a Defense Skill, deal -100% damage\n[WhenUse] Generate 4 Gondola next turn
   PL: [CantDuel]\njeżeli cel użył Umiejętności obrony, zadaje -100% obrażeń\n[WhenUse] generuje 4 Gondole w następnej turze
776. [Umiejętność wroga [840301] (ulepszenie 1) — nazwa] 내보내주세요!!! 내보내주세요!!!
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=840301].levelList[level=1].name
   limit: do 40 znaków
   EN: LETMEOUT!!!LETMEOUT!!!
   PL: LETMEOUT!!!LETMEOUT!!!
777. [Umiejętność wroga [840301] (ulepszenie 1) — opis] 다음 턴에 폭발하는 스킬을 사용함.
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=840301].levelList[level=1].desc
   limit: do 120 znaków
   EN: Uses a self-detonating Skill next turn.
   PL: w następnej turze używa samodetonującej Umiejętności.
778. [Umiejętność wroga [840302] (ulepszenie 1) — nazwa] 터진다!! 터진다!!!!
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=840302].levelList[level=1].name
   limit: do 40 znaków
   EN: IT'S ABOUT TO BLOW!!!!!
   PL: IT'S ABOUT TO BLOW!!!!!
779. [Umiejętność wroga [840302] (ulepszenie 1) — opis] [CantDuel]\n[StartBattle] 취약 3 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=840302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [StartBattle]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [CantDuel]\n[StartBattle] Gain 3 Fragile
   PL: [CantDuel]\n[StartBattle] zyskuje 3 Fragile
780. [Umiejętność wroga [840302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [EndCoin] 대상에게 10의 색욕 피해를 주고 제거됨.
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=840302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: [EndCoin] Deal 10 Lust damage against the target, then expires
   PL: [EndCoin] zadaje celowi 10 obrażeń Żądzy, po czym znika.
781. [Umiejętność wroga [840303] (ulepszenie 1) — nazwa] 팡파레!
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=840303].levelList[level=1].name
   limit: do 40 znaków
   EN: The Fanfare!
   PL: The Fanfare!
782. [Umiejętność wroga [840303] (ulepszenie 1) — opis] [CantDuel]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=840303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel]
   PL: [CantDuel]
783. [Umiejętność wroga [840303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [EndCoin] 대상에게 10의 색욕 피해를 주고 사망함.
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=840303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: [EndCoin] Deal 10 Lust damage against the target, then dies.
   PL: [EndCoin] zadaje celowi 10 obrażeń Żądzy, po czym ginie.
784. [Umiejętność wroga [841001] (ulepszenie 1) — nazwa] 타는 갈증
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841001].levelList[level=1].name
   limit: do 40 znaków
   EN: Burning Thirst
   PL: Burning Thirst
785. [Umiejętność wroga [841001] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 5당 기본 위력 +1 (최대 3)\n[WhenUse] [BloodDinner]을 최대 30 소모하여 소모한 [BloodDinner] 10당 [RegainedStrength] 1 얻음\n[DefeatDuel] 정신력 3 감소
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841001].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BloodDinner], [RegainedStrength], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Base Power +1 for every 5 [Laceration] on the target (max 3)\n[WhenUse] Consume up to 30 [BloodDinner]: gain 1 [RegainedStrength] for every 10 [BloodDinner] consumed\n[DefeatDuel] Lose 3 SP
   PL: [WhenUse] Moc Bazowa +1 za każde 5 [Laceration] celu (maks. 3)\n[WhenUse] zużywa do 30 [BloodDinner]: zyskuje 1 [RegainedStrength] za każde 10 zużytych [BloodDinner]\n[DefeatDuel] traci 3 SP
786. [Umiejętność wroga [841001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Umiejętność wroga [841001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [Umiejętność wroga [841002] (ulepszenie 1) — nazwa] 꿰뚫려라
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841002].levelList[level=1].name
   limit: do 40 znaków
   EN: Be Impaled
   PL: Be Impaled
789. [Umiejętność wroga [841002] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 40 소모하여 소모한 [BloodDinner] 10당 [RegainedStrength] 1 얻고 정신력 3 회복\n\n[DefeatDuel] 정신력 3 감소\n[DefeatDuel] [RegainedStrength] 3 소모. 다음 턴에 [DefenseDown] 3 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841002].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [RegainedStrength], [DefeatDuel], [DefenseDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [DefeatDuel] = [합 패배] / [Clash Lose]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [WhenUse] Consume up to 40 [BloodDinner]: gain 1 [RegainedStrength] and heal 3 SP for every 10 [BloodDinner] consumed\n\n[DefeatDuel] Lose 3 SP\n[DefeatDuel] Consume 3 [RegainedStrength]. Gain 3 [DefenseDown] next turn
   PL: [WhenUse] zużywa do 40 [BloodDinner]: zyskuje 1 [RegainedStrength] i przywraca 3 SP za każde 10 zużytych [BloodDinner]\n\n[DefeatDuel] traci 3 SP\n[DefeatDuel] zużywa 3 [RegainedStrength]. zyskuje 3 [DefenseDown] w następnej turze
790. [Umiejętność wroga [841002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 최대 체력의 20%만큼 색욕 피해를 줌
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal Lust damage equal to 20% of the target's max HP
   PL: [OnSucceedAttack] zadaje Żądzą obrażenia równe 20% Maks. HP celu
791. [Umiejętność wroga [841002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 최대 체력의 20%만큼 색욕 피해를 줌
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 790 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Umiejętność wroga [841003] (ulepszenie 1) — nazwa] 돈키호테류 경혈 2식 - 말뚝
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841003].levelList[level=1].name
   limit: do 50 znaków
   EN: Don Quixote Hardblood Arts 2 - Stake
   PL: Don Quixote Hardblood Arts 2 - Stake
793. [Umiejętność wroga [841003] (ulepszenie 1) — opis] [Laceration]이 가장 많이 부여된 대상 공격\n[WhenUse] 대상의 [Laceration] 5당 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841003].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: Attacks the target with the most [Laceration]\n[WhenUse] Coin Power +1 for every 5 [Laceration] on the target (max 2)
   PL: atakuje cel z największą liczbą [Laceration]\n[WhenUse] Moc Monety +1 za każde 5 [Laceration] celu (maks. 2)
794. [Umiejętność wroga [841003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Umiejętność wroga [841003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Umiejętność wroga [841003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Umiejętność wroga [841003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Umiejętność wroga [841003] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] (대상의 [Laceration] 위력 X 횟수)만큼 색욕 피해를 줌
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Deal Lust damage equal to ([Laceration] Potency x Count)
   PL: [OnSucceedAttack] zadaje Żądzą obrażenia równe (Siła [Laceration] celu x Licznik [Laceration] celu)
799. [Umiejętność wroga [841004] (ulepszenie 1) — nazwa] 경혈식 쐐기
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841004].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Wedge
   PL: Hardblood Wedge
800. [Umiejętność wroga [841004] (ulepszenie 1) — opis] [StartBattle] 자신의 [RegainedStrength] 3당 가중치 +1 (최대 2)\n[EndSkill] [RegainedStrength] 3 소모
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841004].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [RegainedStrength], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [StartBattle] Gain Atk Weight +1 for every 3 [RegainedStrength] on self (max 2)\n[EndSkill] Consume 3 [RegainedStrength]
   PL: [StartBattle] Waga Ataku +1 za każde 3 [RegainedStrength] tej jednostki (maks. 2)\n[EndSkill] zużywa 3 [RegainedStrength]
801. [Umiejętność wroga [841004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Umiejętność wroga [841004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Umiejętność wroga [841004] (ulepszenie 1) — moneta 1, efekt 3 — opis] [WinDuelAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841004].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Burst]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Burst] = 파열 / Rupture
   EN: [WinDuelAttack] Inflict 3 [Burst]
   PL: [WinDuelAttack] nakłada 3 [Burst]
804. [Umiejętność wroga [841004] (ulepszenie 1) — moneta 1, efekt 4 — opis] [DefeatDuelAttack] [RegainedStrength] 1 소모
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841004].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuelAttack], [RegainedStrength]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust
   EN: [DefeatDuelAttack] Consume 1 [RegainedStrength]
   PL: [DefeatDuelAttack] zużywa 1 [RegainedStrength]
805. [Umiejętność wroga [841004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [Umiejętność wroga [841004] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841004].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Umiejętność wroga [841004] (ulepszenie 1) — moneta 2, efekt 3 — opis] [WinDuelAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841004].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 803 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Umiejętność wroga [841004] (ulepszenie 1) — moneta 2, efekt 4 — opis] [DefeatDuelAttack] [RegainedStrength] 1 소모
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841004].levelList[level=1].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 804 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Umiejętność wroga [841004] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841004].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Umiejętność wroga [841005] (ulepszenie 1) — nazwa] 피의 욕망
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841005].levelList[level=1].name
   limit: do 40 znaków
   EN: Desire for Blood
   PL: Desire for Blood
811. [Umiejętność wroga [841005] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 40 소모하여 소모한 [BloodDinner] 10당 [RegainedStrength] 1 얻고 정신력 5 회복
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841005].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [BloodDinner], [RegainedStrength]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust
   EN: [WhenUse] Consume up to 40 [BloodDinner]: gain 1 [RegainedStrength] for every 10 [BloodDinner] consumed
   PL: [WhenUse] zużywa do 40 [BloodDinner]: zyskuje 1 [RegainedStrength] i przywraca 5 SP za każde 10 zużytych [BloodDinner]
812. [Umiejętność wroga [841005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [Umiejętność wroga [841005] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841005].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Umiejętność wroga [841005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Umiejętność wroga [841005] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841005].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [Umiejętność wroga [841005] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841005].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Umiejętność wroga [841005] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841005].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Umiejętność wroga [841005] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841005].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Umiejętność wroga [841005] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841005].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [Umiejętność wroga [841006] (ulepszenie 1) — nazwa] 혈찬의 시간
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841006].levelList[level=1].name
   limit: do 40 znaków
   EN: Moment of Bloodfeast
   PL: Moment of Bloodfeast
821. [Umiejętność wroga [841006] (ulepszenie 1) — opis] [CantIdentify]\n[WhenUse] [BloodDinner]을 최대 300 소모하여 소모한 [BloodDinner] 10당 [RegainedStrength] 1 얻고 정신력 3 회복\n[WhenUse] [BloodDinner]을 소모했으면 정신력 30 회복
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841006].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WhenUse], [BloodDinner], [RegainedStrength]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust
   EN: [CantIdentify]\n[WhenUse] Consume up to 300 [BloodDinner]: gain 1 [RegainedStrength] and heal 3 SP for every 10 [BloodDinner] consumed\n[WhenUse] If this unit consumed [BloodDinner], heal 30 SP
   PL: [CantIdentify]\n[WhenUse] zużywa do 300 [BloodDinner]: zyskuje 1 [RegainedStrength] i przywraca 3 SP za każde 10 zużytych [BloodDinner]\n[WhenUse] jeżeli jednostka zużyła [BloodDinner], przywraca 30 SP
822. [Umiejętność wroga [841006] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [Umiejętność wroga [841007] (ulepszenie 1) — nazwa] 돈키호테류 경혈 4식 - 도려내기
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841007].levelList[level=1].name
   (powtórzenie elementu 686 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
824. [Umiejętność wroga [841007] (ulepszenie 1) — opis] 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음.\n[WhenUse] [BloodDinner]을 최대 100 소모하여 소모한 [BloodDinner] 10당 [RegainedStrength] 1 얻고 정신력 15 회복\n[WhenUse] 자신의 [BloodDinner_Accumulation] 수치 30당 합 위력 +1 (최대 15)\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음.\n[EndSkill] 증가한 합 위력만큼 이번 턴과 다음 턴에 [AttackDown], [DefenseDown]를 얻음. (최대 15)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841007].levelList[level=1].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [RegainedStrength], [BloodDinner_Accumulation], [DefeatDuel], [EndSkill], [AttackDown], [DefenseDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Cannot be Staggered until he uses this Skill.\n[WhenUse] Consume up to 100 [BloodDinner]: gain 1 [RegainedStrength] and heal 15 SP for every 10 [BloodDinner] consumed\n[WhenUse] Clash Power +1 for every [BloodDinner_Accumulation] by this unit (max 15)\n[DefeatDuel] Deal -50% damage, and the damage from this Skill does not Stagger the target.\n[EndSkill] For this turn and next turn, gain [AttackDown] and [DefenseDown] equal to the Clash Power gained with this Skill. (max 15)
   PL: nie może przejść w Oszołamienie, dopóki nie użyje tej Umiejętności.\n[WhenUse] zużywa do 100 [BloodDinner]: zyskuje 1 [RegainedStrength] i przywraca 15 SP za każde 10 zużytych [BloodDinner]\n[WhenUse] Moc Starcia +1 za każde 30 [BloodDinner_Accumulation] tej jednostki (maks. 15)\n[DefeatDuel] zadaje -50% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu.\n[EndSkill] w tej turze i następnej zyskuje [AttackDown] i [DefenseDown] równe zdobytej Mocy Starcia. (maks. 15)
825. [Umiejętność wroga [841007] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841007].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Umiejętność wroga [841007] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841007].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Umiejętność wroga [841007] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [RegainedStrength] 2 소모
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841007].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RegainedStrength]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust
   EN: [OnSucceedAttack] Consume 2 [RegainedStrength]
   PL: [OnSucceedAttack] zużywa 2 [RegainedStrength]
828. [Umiejętność wroga [841008] (ulepszenie 1) — nazwa] 돈키호테류 경혈 14식 망토
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841008].levelList[level=1].name
   limit: do 60 znaków
   EN: Don Quixote Hardblood Arts 14: Mantle
   PL: Don Quixote Hardblood Arts 14: Mantle
829. [Umiejętność wroga [841008] (ulepszenie 1) — opis] [DuelGuard]\n[WinDuel] 대상에게 [Laceration] 4, [Burst] 4 부여\n[DefeatDuel] [RegainedStrength] 2 소모
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841008].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [DuelGuard], [WinDuel], [Laceration], [Burst], [DefeatDuel], [RegainedStrength]
   znaczenie tagów: [DuelGuard] = [합 가능 가드] / [Clashable Guard]; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust
   EN: [DuelGuard]\n[WinDuel] Inflict 4 [Laceration] and [Burst]\n[DefeatDuel] Consume 2 [RegainedStrength]
   PL: [DuelGuard]\n[WinDuel] nakłada 4 [Laceration] i 4 [Burst]\n[DefeatDuel] zużywa 2 [RegainedStrength]
830. [Umiejętność wroga [841008] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841008].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Umiejętność wroga [841009] (ulepszenie 1) — nazwa] 약하디 약하구나
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841009].levelList[level=1].name
   limit: do 40 znaków
   EN: Frail, So Frail
   PL: Frail, So Frail
832. [Umiejętność wroga [841009] (ulepszenie 1) — opis] [DuelCounter]\n[RegainedStrength] 10당 기본 위력 +1\n대상의 [Laceration] 5당 코인 위력 +1 (최대 2)\n[DefeatDuel] 정신력 3 감소
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841009].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [RegainedStrength], [Laceration], [DefeatDuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DuelCounter]\nBase Power +1 for every 10 [RegainedStrength]\nCoin Power +1 for every 5 [Laceration] on the target (max 2)\n[DefeatDuel] Lose 3 SP
   PL: [DuelCounter]\nMoc Bazowa +1 za każde 10 [RegainedStrength]\nMoc Monety +1 za każde 5 [Laceration] celu (maks. 2)\n[DefeatDuel] traci 3 SP
833. [Umiejętność wroga [841009] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841009].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Umiejętność wroga [841009] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841009].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
835. [Umiejętność wroga [841010] (ulepszenie 1) — nazwa] 블러디 메리 고 라운드
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841010].levelList[level=1].name
   limit: do 40 znaków
   EN: Bloody-Merry-Go-Round
   PL: Bloody-Merry-Go-Round
836. [Umiejętność wroga [841010] (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] 다음 턴에 굳어진 꿈을 생성함
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841010].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]
   EN: [CantDuel]\n[WhenUse] Generate Coagulated Dream next turn
   PL: [CantDuel]\n[WhenUse] tworzy Coagulated Dream w następnej turze
837. [Umiejętność wroga [841010] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841010].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Umiejętność wroga [841010] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841010].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Umiejętność wroga [841010] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841010].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Umiejętność wroga [841010] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841010].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [Umiejętność wroga [841011] (ulepszenie 1) — nazwa] 꿰어져라
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841011].levelList[level=1].name
   limit: do 40 znaków
   EN: Be Impaled
   PL: Be Impaled
842. [Umiejętność wroga [841011] (ulepszenie 1) — opis] [DefeatDuel] 정신력 3 감소
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841011].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Lose 3 SP
   PL: [DefeatDuel] traci 3 SP
843. [Umiejętność wroga [841011] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841011].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Umiejętność wroga [841011] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 흐트러짐 상태가 되고, 다음 턴에 [Penetration] 상태가 됨
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841011].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Penetration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Penetration] = 굳어가는 피 / Congealing Blood
   EN: [OnSucceedAttack] The target becomes staggered, then becomes [Penetration] next turn
   PL: [OnSucceedAttack] cel przechodzi w Oszołamienie, a w następnej turze w stan [Penetration]
845. [Umiejętność wroga [841011] (ulepszenie 1) — moneta 2, efekt 3 — opis] [EndCoin] 대상의 [Laceration] 위력 25 감소. 해당 수치만큼 [Laceration]을 얻고, [BloodDinner] 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841011].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [Laceration], [BloodDinner]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: [EndCoin] The target loses 25 [Laceration] Potency. Gain [Laceration] and increase [BloodDinner] equal to that value
   PL: [EndCoin] Siła [Laceration] celu maleje o 25. zyskuje [Laceration] i zwiększa [BloodDinner] o tę wartość
846. [Umiejętność wroga [841012] (ulepszenie 1) — nazwa] 돈키호테류 경혈 오의 - 구
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841012].levelList[level=1].name
   limit: do 70 znaków
   EN: Ascendant Don Quixote Hardblood Arts - The Sphere
   PL: Ascendant Don Quixote Hardblood Arts - The Sphere
847. [Umiejętność wroga [841012] (ulepszenie 1) — opis] 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음.\n[BloodDinner_Common_Accumulation]만큼 피해량이 증가함.(최대 300%)\n[WhenUse] 정신력 30 회복\n[WhenUse] [RegainedStrength] 10당 합 위력 +1\n[EndSkill] [RegainedStrength] 모두 소모. 이번 턴과 다음 턴에 [Vulnerable] 5 얻음. 다음 턴에 [Binding] 2 얻음.
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841012].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner_Common_Accumulation], [WhenUse], [RegainedStrength], [EndSkill], [Vulnerable], [Binding]
   znaczenie tagów: [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [WhenUse] = [사용시] / [On Use]; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [EndSkill] = [공격 종료시] / [Attack End]; [Vulnerable] = 취약 / Fragile; [Binding] = 속박 / Bind
   EN: Cannot be Staggered until he uses this Skill.\nDeal more damage equal to [BloodDinner_Common_Accumulation]. (max 300%)\n[WhenUse] Heal 30 SP\n[WhenUse] Clash Power +1 for every 10 [RegainedStrength]\n[EndSkill] Consume all [RegainedStrength]. Gain 5 [Vulnerable] this turn and next turn. Gain 2 [Binding] next turn.
   PL: nie może przejść w Oszołamienie, dopóki nie użyje tej Umiejętności.\nzadaje więcej obrażeń równe [BloodDinner_Common_Accumulation]. (maks. 300%)\n[WhenUse] przywraca 30 SP\n[WhenUse] Moc Starcia +1 za każde 10 [RegainedStrength]\n[EndSkill] zużywa całe [RegainedStrength]. zyskuje 5 [Vulnerable] w tej turze i następnej. zyskuje 2 [Binding] w następnej turze.
848. [Umiejętność wroga [841012] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841012].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Umiejętność wroga [841012] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841012].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
850. [Umiejętność wroga [837501] (ulepszenie 1) — nazwa] 키익
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837501].levelList[level=1].name
   limit: do 40 znaków
   EN: Ksssh
   PL: Ksssh
851. [Umiejętność wroga [837501] (ulepszenie 1) — opis] [WhenUse] [DuelDeclaration_Camille] 부여\n[WhenUse] 자신의 [Breath] 5 얻음\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837501].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DuelDeclaration_Camille], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DuelDeclaration_Camille] = 결투 선포 - 까미유 / Declared Duel - Camille; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Inflict [DuelDeclaration_Camille]\n[WhenUse] Gain 5 [Breath]\n[WinDuel] Gain +2 [Breath] Count
   PL: [WhenUse] nakłada [DuelDeclaration_Camille]\n[WhenUse] zyskuje 5 [Breath]\n[WinDuel] zyskuje 2 Licznika [Breath]
852. [Umiejętność wroga [837502] (ulepszenie 1) — nazwa] 키이이익
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837502].levelList[level=1].name
   limit: do 40 znaków
   EN: Hnnnhhhhhh
   PL: Hnnnhhhhhh
853. [Umiejętność wroga [837502] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 2 [Breath]
   PL: [WhenUse] zyskuje 2 [Breath]
854. [Umiejętność wroga [837502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Umiejętność wroga [837502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 7+ Speed, inflict 3 [Burst]
   PL: [OnSucceedAttack] przy Szybkości 7 lub wyższej, nakłada 3 [Burst]
856. [Umiejętność wroga [837502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 3 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL: [OnSucceedAttack] zyskuje 3 [Breath]
857. [Umiejętność wroga [837502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 3 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 855 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
858. [Umiejętność wroga [837503] (ulepszenie 1) — nazwa] 키이
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837503].levelList[level=1].name
   limit: do 40 znaków
   EN: Kihh
   PL: Kihh
859. [Umiejętność wroga [837503] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath]이 7 이상이면, 코인 위력 +2\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] At 7+ [Breath], Coin Power +2\n[WinDuel] Gain +2 [Breath] Count
   PL: [WhenUse] przy 7+ [Breath], Moc Monety +2\n[WinDuel] zyskuje 2 Licznika [Breath]
860. [Umiejętność wroga [837503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 3 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 856 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Umiejętność wroga [837503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 7+ Speed, inflict 3 [Burst] Count
   PL: [OnSucceedAttack] przy Szybkości 7 lub wyższej, nakłada 3 Licznika [Burst]
862. [Umiejętność wroga [837503] (ulepszenie 1) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 크리티컬 피해량 +50%
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837503].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] +50% Damage on Critical Hit
   PL: [CriticalOnSucceedAttack] +50% obrażeń przy trafieniu krytycznym
863. [Umiejętność wroga [837504] (ulepszenie 1) — nazwa] 키익
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837504].levelList[level=1].name
   (powtórzenie elementu 850 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
864. [Umiejętność wroga [837504] (ulepszenie 1) — opis] [WhenUse] 자신의 속도가 공격자보다 높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 3)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837504].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If this unit's Speed is faster than the target's, Coin Power +1 (Coin Power +1 for every 2 Speed difference; max 3)
   PL: [WhenUse] jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Monety +1 (Moc Monety +1 za każde 2 punkty różnicy Szybkości; maks. 3)
865. [Umiejętność wroga [837504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 4 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +4 [Breath] Count
   PL: [OnSucceedAttack] zyskuje 4 Licznika [Breath]
866. [Umiejętność wroga [837504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 3 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 7+ Speed, inflict 3 [Burst] and +1 [Burst] Count
   PL: [OnSucceedAttack] przy Szybkości 7 lub wyższej, nakłada 3 [Burst] i 1 Licznika [Burst]
867. [Umiejętność wroga [837504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 5 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 5 [Breath]
   PL: [OnSucceedAttack] zyskuje 5 [Breath]
868. [Umiejętność wroga [837504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 3 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 866 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Umiejętność wroga [837504] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 5 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837504].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 867 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [Umiejętność wroga [837504] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 3 부여, [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837504].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 866 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Umiejętność wroga [837504] (ulepszenie 1) — moneta 4, efekt 1 — opis] [CriticalOnSucceedAttack] 크리티컬 피해량 +100%
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837504].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] +100% Damage on Critical Hit
   PL: [CriticalOnSucceedAttack] +100% obrażeń przy trafieniu krytycznym
872. [Umiejętność wroga [837504] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]당 피해량 +5% (최대 50%)
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837504].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Deal +5% damage for every [Burst] on the target (Max 50%)
   PL: [OnSucceedAttack] zadaje +5% obrażeń za każde [Burst] celu (maks. 50%)
873. [Umiejętność wroga [837505] (ulepszenie 1) — nazwa] 키긱
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837505].levelList[level=1].name
   (powtórzenie elementu 734 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
874. [Umiejętność wroga [837505] (ulepszenie 1) — opis] [WinDuel] 합 횟수에 비례하여 피해량이 증가 (합 횟수 1당 +10%. 최대 50%)\n[WinDuel] 다음 턴에 [Agility] 2 얻음\n[DefeatDuel] 다음 턴에 [Binding] 2 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837505].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Agility], [DefeatDuel], [Binding]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Agility] = 신속 / Haste; [DefeatDuel] = [합 패배] / [Clash Lose]; [Binding] = 속박 / Bind
   EN: [WinDuel] Deal more damage based on number of Clashes (+10% damage for every Clash, max 50%)\n[WinDuel] Gain 2 [Agility] next turn\n[DefeatDuel] Gain 2 [Binding] next turn
   PL: [WinDuel] zadaje więcej obrażeń w zależności od liczby Starć (+10% obrażeń za każde Starcie, maks. 50%)\n[WinDuel] zyskuje 2 [Agility] w następnej turze\n[DefeatDuel] zyskuje 2 [Binding] w następnej turze
875. [Umiejętność wroga [837505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 1 [Vulnerable] w następnej turze
876. [Umiejętność wroga [837506] (ulepszenie 1) — nazwa] 키기기긱
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837506].levelList[level=1].name
   limit: do 40 znaków
   EN: Knhhh
   PL: Knhhh
877. [Umiejętność wroga [837506] (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=837506].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Agility]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Agility] = 신속 / Haste
   EN: [OnSucceedEvade] Gain 1 [Agility] next turn
   PL: [OnSucceedEvade] zyskuje 1 [Agility] w następnej turze
878. [Umiejętność wroga [841013] (ulepszenie 1) — nazwa] 돈키호테류 경혈 오의 - 라 샹그레
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841013].levelList[level=1].name
   limit: do 70 znaków
   EN: Ascendant Don Quixote Hardblood Arts - La Sangre
   PL: Ascendant Don Quixote Hardblood Arts - La Sangre
879. [Umiejętność wroga [841301] (ulepszenie 1) — nazwa] 빛나는 모험의 기억
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841301].levelList[level=1].name
   limit: do 50 znaków
   EN: Shining Memories of the Adventure
   PL: Shining Memories of the Adventure
880. [Umiejętność wroga [841301] (ulepszenie 1) — opis] [StartBattle] 무작위 수감자 1명에게 [ParryingResultUp] 1, [AttackDmgUp] 1 부여\n[StartBattle] 돈키호테와 굳어진 꿈에게 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c7p3.json :: dataList[id=841301].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [ParryingResultUp], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: [StartBattle] Apply 1 [ParryingResultUp] and 1 [AttackDmgUp] to a random Sinner\n[StartBattle] Inflict 1 [Vulnerable] against both Don Quixote and his Coagulated Dream
   PL: [StartBattle] nakłada 1 [ParryingResultUp] i 1 [AttackDmgUp] losowemu Grzesznikowi\n[StartBattle] nakłada 1 [Vulnerable] na Don Quixote i jego Coagulated Dream

## [a1c7p3] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c7p3
- grupa rozdziału/trybu: `a1c7p3` · plik: `Skills_Enemy-a1c7p3.json`

881. [Umiejętność wroga [9016201] (ulepszenie 1) — nazwa] 경혈식 찌르기
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016201].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Stab
   PL: Hardblood Stab
882. [Umiejętność wroga [9016201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [Umiejętność wroga [9016202] (ulepszenie 1) — nazwa] 경혈식 베어내기
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016202].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Cleave
   PL: Hardblood Cleave
884. [Umiejętność wroga [9016202] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 8 이상이면, 피해량 +20%
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016202].levelList[level=1].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
885. [Umiejętność wroga [9016202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
886. [Umiejętność wroga [9016202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [Umiejętność wroga [9016202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration]이 6 이상이면 [HardenedBlood]을 1 얻음
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [HardenedBlood]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [OnSucceedAttack] At 6+ [Laceration], gain 1 [HardenedBlood]
   PL: [OnSucceedAttack] przy 6+ [Laceration], zyskuje 1 [HardenedBlood]
888. [Umiejętność wroga [9016202] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [Umiejętność wroga [9016202] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 8, [BloodScissor] 1 얻음.
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016202].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [BloodScissor]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades
   EN: [OnSucceedAttack] Gain 8 [Laceration] and 1 [BloodScissor]
   PL: [OnSucceedAttack] zyskuje 8 [Laceration] i 1 [BloodScissor].
890. [Umiejętność wroga [9016203] (ulepszenie 1) — nazwa] 경혈식 강화 베어내기
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016203].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Powercleave
   PL: Hardblood Powercleave
891. [Umiejętność wroga [9016203] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 기본 위력 +1\n[HardenedBlood]당 피해량 +5% (최대 25%)\n[EndSkill] [HardenedBlood], [BloodScissor] 전부 소모
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016203].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [HardenedBlood], [EndSkill], [BloodScissor]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood; [EndSkill] = [공격 종료시] / [Attack End]; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades
   EN: [WhenUse] If target has 6+ [Laceration], Base Power +1\nDeal +5% damage for every [HardenedBlood] (max 25%)\n[EndSkill] Consume all [HardenedBlood] and [BloodScissor]
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], Moc Bazowa +1\nzadaje +5% obrażeń za każde [HardenedBlood] (maks. 25%)\n[EndSkill] zużywa całe [HardenedBlood] i [BloodScissor]
892. [Umiejętność wroga [9016203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [Umiejętność wroga [9016203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 (대상의 [Laceration])%만큼 체력 회복 (최대 20%)
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Heal ([Laceration] on target)% HP (max 20%)
   PL: [OnSucceedAttack] przywraca HP równe ([Laceration] celu)% Maks. HP (maks. 20%)
894. [Umiejętność wroga [9016204] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016204].levelList[level=1].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
895. [Umiejętność wroga [9016204] (ulepszenie 1) — opis] [WhenUse] 자신의 [HardenedBlood] 1당, 기본 위력 +1
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [HardenedBlood]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [WhenUse] Base Power +1 for every [HardenedBlood] on self
   PL: [WhenUse] Moc Bazowa +1 za każde [HardenedBlood] tej jednostki
896. [Umiejętność wroga [9016204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 328 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
897. [Umiejętność wroga [9016601] (ulepszenie 1) — nazwa] 축제야 축제!
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016601].levelList[level=1].name
   limit: do 40 znaków
   EN: It's a Festival, a Festival!
   PL: It's a Festival, a Festival!
898. [Umiejętność wroga [9016601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [Umiejętność wroga [9016601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
900. [Umiejętność wroga [9016602] (ulepszenie 1) — nazwa] 옷 입혀줄게
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016602].levelList[level=1].name
   limit: do 40 znaków
   EN: Let's Dress Up
   PL: Let's Dress Up
901. [Umiejętność wroga [9016602] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 피해량 +20%
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 6+ [Laceration], deal +20% damage
   PL: [WhenUse] jeżeli cel ma 6+ [Laceration], zadaje +20% obrażeń
902. [Umiejętność wroga [9016602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
903. [Umiejętność wroga [9016602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 5 이상이면, [HardenedBlood]을 1 얻음
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
904. [Umiejętność wroga [9016603] (ulepszenie 1) — nazwa] 이벤트가 남아있어!
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016603].levelList[level=1].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [Umiejętność wroga [9016603] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10당 [BloodScissor] 1 얻음\n[WhenUse] 이 스킬에서 [BloodDinner]을 소모하지 못했으면, [Laceration] 5, [HardenedBlood]을 1 얻음.\n[WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016603].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodScissor], [Laceration], [HardenedBlood]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodScissor] = 핏빛 가위날 / Blood-tinged Scissorblades; [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: [WhenUse] Consume up to 50 [BloodDinner]; gain 1 [BloodScissor] and heal 3 SP for every 10 [BloodDinner] consumed\n[WhenUse] If this unit failed to consume [BloodDinner] with this Skill, gain 5 [Laceration] and 1 [HardenedBlood].\n[WhenUse] If target has 5+ [Laceration], Coin Power +1
   PL: [WhenUse] zużywa do 50 [BloodDinner]; zyskuje 1 [BloodScissor] i przywraca 3 SP za każde 10 zużytych [BloodDinner]\n[WhenUse] jeżeli ta Umiejętność nie zużyła [BloodDinner], zyskuje 5 [Laceration] i 1 [HardenedBlood].\n[WhenUse] jeżeli cel ma 5+ [Laceration], Moc Monety +1
906. [Umiejętność wroga [9016603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [Umiejętność wroga [9016603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Umiejętność wroga [9016604] (ulepszenie 1) — nazwa] 재촉하지마
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016604].levelList[level=1].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
909. [Umiejętność wroga [9016604] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1\n[WhenUse] [BloodScissor]에 비례해서, 합 위력 +1 (최대 3)\n[HardenedBlood]당 피해량 +7% (최대 35%)\n[EndSkill] [HardenedBlood] 전부 소모
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016604].levelList[level=1].desc
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Umiejętność wroga [9016604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
911. [Umiejętność wroga [9016604] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 8 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016604].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [Umiejętność wroga [9016604] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [BloodScissor]를 최대 5 소모하여 피해량 (20 * 소모한 [BloodScissor])% 증가 (최대 100%)
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016604].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
913. [Umiejętność wroga [9016604] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 최대 체력의 (대상의 [Laceration] 위력)%만큼 체력 회복 (최대 30%)
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016604].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
914. [Umiejętność wroga [9016605] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016605].levelList[level=1].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
915. [Umiejętność wroga [9016605] (ulepszenie 1) — opis] [WhenUse] [BloodScissor] 1 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [HardenedBlood] 3 이상이면 코인 위력 +1
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016605].levelList[level=1].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
916. [Umiejętność wroga [9016605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
917. [Umiejętność wroga [9016701] (ulepszenie 1) — nazwa] 질문에 답을 해 주세요.
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016701].levelList[level=1].name
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
918. [Umiejętność wroga [9016701] (ulepszenie 1) — opis] [WhenUse] [Laceration] 5, [Laceration] 횟수 1 얻음
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016701].levelList[level=1].desc
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
919. [Umiejętność wroga [9016701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
920. [Umiejętność wroga [9016701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
921. [Umiejętność wroga [9016702] (ulepszenie 1) — nazwa] 말 끊지 마세요!
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016702].levelList[level=1].name
   (powtórzenie elementu 352 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [Umiejętność wroga [9016702] (ulepszenie 1) — opis] [WhenUse] [Laceration] 5, [Laceration] 횟수 1 얻음
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016702].levelList[level=1].desc
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
923. [Umiejętność wroga [9016702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
924. [Umiejętność wroga [9016702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 5 이상이면, [BloodyHand] 1 얻음
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
925. [Umiejętność wroga [9016703] (ulepszenie 1) — nazwa] 빛바랜 인내
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016703].levelList[level=1].name
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [Umiejętność wroga [9016703] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10 당 [BloodyHand] 1 얻음\n[WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016703].levelList[level=1].desc
   (powtórzenie elementu 357 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
927. [Umiejętność wroga [9016703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
928. [Umiejętność wroga [9016703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [EndSkill] 이 스킬에서 [BloodDinner]을 소모하지 못했으면, [Laceration] 10, [BloodyHand] 1 얻음.
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 359 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
929. [Umiejętność wroga [9016704] (ulepszenie 1) — nazwa] 끝없는 고해
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016704].levelList[level=1].name
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
930. [Umiejętność wroga [9016704] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [HardenedBlood] 1 당, 합 위력 +1\n[DefeatDuel] [BloodyHand] 2 감소
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016704].levelList[level=1].desc
   (powtórzenie elementu 361 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
931. [Umiejętność wroga [9016704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
932. [Umiejętność wroga [9016704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
933. [Umiejętność wroga [9016704] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [BloodyHand]을 전부 소모하여, 대상의 [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016704].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
934. [Umiejętność wroga [9016704] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [HardenedBlood]을 모두 소모하여, (소모한 [HardenedBlood] x 3) 만큼 [BloodDinner]이 증가하고, [Laceration] 5 얻음
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016704].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 365 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
935. [Umiejętność wroga [9016704] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 최대 체력의 (대상의 [Laceration])% 만큼 체력 회복 (최대 30%)
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016704].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
936. [Umiejętność wroga [9016705] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016705].levelList[level=1].name
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
937. [Umiejętność wroga [9016705] (ulepszenie 1) — opis] [WhenUse] [BloodyHand]이 1 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [HardenedBlood]이 3 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016705].levelList[level=1].desc
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
938. [Umiejętność wroga [9016705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
939. [Umiejętność wroga [9016801] (ulepszenie 1) — nazwa] 환상의 축제로 오세요!
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016801].levelList[level=1].name
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
940. [Umiejętność wroga [9016801] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever]가 5 이상이면, 최종 위력 +2
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016801].levelList[level=1].desc
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
941. [Umiejętność wroga [9016801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
942. [Umiejętność wroga [9016801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Burst] 3 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 427 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
943. [Umiejętność wroga [9016802] (ulepszenie 1) — nazwa] 즐거운 행렬에 함께 해요!
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016802].levelList[level=1].name
   (powtórzenie elementu 428 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
944. [Umiejętność wroga [9016802] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever] 5 또는 대상의 [Laceration] 6당 최종 위력 +1 (최대 3)\n[WhenUse] [BloodDinner]이 20 미만이면, [Laceration] 20을 얻은 다음 즉시 1회 발동시키고 [Laceration] 횟수 1 감소\n[EndSkill] [BloodDinner] 20 소모
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016802].levelList[level=1].desc
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [Umiejętność wroga [9016802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 6당 [HardenedBlood] 1 얻음 (최대 2)
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 430 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
946. [Umiejętność wroga [9016802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
947. [Umiejętność wroga [9016802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [WinDuelAttack] [Laceration] 4 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
948. [Umiejętność wroga [9016802] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BloomingThorns] 2 ~ 3 얻음
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016802].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
949. [Umiejętność wroga [9016803] (ulepszenie 1) — nazwa] 기쁨의 미소를 꽃피워요!
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016803].levelList[level=1].name
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
950. [Umiejętność wroga [9016803] (ulepszenie 1) — opis] [WhenUse] [FestivalFever]가 5 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 합 위력 +1
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016803].levelList[level=1].desc
   (powtórzenie elementu 435 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
951. [Umiejętność wroga [9016803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
952. [Umiejętność wroga [9016803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [WinDuelAttack] [FestivalFever] 2 얻음
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
953. [Umiejętność wroga [9016804] (ulepszenie 1) — nazwa] 영원한 행복의 왕국 라만차랜드!
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016804].levelList[level=1].name
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
954. [Umiejętność wroga [9016804] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]이 40 미만이면, [Laceration] 20, [Laceration] 횟수 2를 얻은 다음 즉시 2회 발동시키고 [Laceration] 횟수 2 감소\n[EndSkill] [BloodDinner] 40 소모\n[EndBattle] [HardenedBlood], [FestivalFever] 전부 소모
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016804].levelList[level=1].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
955. [Umiejętność wroga [9016804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [HardenedBlood]만큼 [Laceration], [Burst] 부여
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
956. [Umiejętność wroga [9016804] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 최대 체력의 ([FestivalFever] x 4)%만큼 체력 회복 (최대 40%)
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016804].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [Umiejętność wroga [9016804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
958. [Umiejętność wroga [9016804] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloomingThorns] 5 얻음
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016804].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
959. [Umiejętność wroga [9016805] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016805].levelList[level=1].name
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
960. [Umiejętność wroga [9016805] (ulepszenie 1) — opis] [WhenUse] 자신의 [FestivalFever]가 5 이상이면 최종 위력 +2\n[StartBattle] [FestivalFever] 3 얻음\n[OnDefeatEvade] [FestivalFever] 3 잃음
   źródło: Skills_Enemy-a1c7p3.json :: dataList[id=9016805].levelList[level=1].desc
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c7p3] Pasywka wroga: Passives_Abnormality-a1c7p3
- plik gry: `Passives_Abnormality-a1c7p3.json`

961. [[a1c7p3] Pasywka wroga [837804] — nazwa] 굶주림과 노쇠
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837804].name
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
962. [[a1c7p3] Pasywka wroga [837804] — opis] 전투 시작시, [StarvingPriestTwo] 얻음
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837804].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StarvingPriestTwo]
   znaczenie tagów: [StarvingPriestTwo] = 노쇠 / Withered
   EN: Gain [StarvingPriestTwo] at the start of the Encounter
   PL: Początek walki: zyskuje [StarvingPriestTwo]
963. [[a1c7p3] Pasywka wroga [837801] — nazwa] 종부성사
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837801].name
   limit: do 40 znaków
   EN: Unctio Extrema
   PL: Unctio Extrema
964. [[a1c7p3] Pasywka wroga [837801] — opis] 턴 종료시, 자신의 [Laceration]을 발동시킴 (최대 50. 자신의 [Laceration] 횟수 1 소모). 가장 체력이 낮은 아군 혈귀의 (본체와 부위의) 체력을 50 회복시킴 (피해를 입은 아군이 없으면 발동하지 않음)
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837801].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Turn End: activate [Laceration] on self. (max 50; consume 1 [Laceration] Count on self) Heal 50 HP to Core and Part of an allied Bloodfiend with the least HP (does not activate if all allies are at full HP)
   PL: Koniec tury: uruchamia własne [Laceration] (do 50; zużywa 1 Licznika [Laceration]). przywraca 50 HP Korpusowi i Części sojuszniczego Bloodfienda z najniższym HP (nie uruchamia się, jeżeli żaden sojusznik nie otrzymał obrażeń)
965. [[a1c7p3] Pasywka wroga [837802] — nazwa] 고백성사
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837802].name
   limit: do 40 znaków
   EN: Sacramentum Paenitentiae
   PL: Sacramentum Paenitentiae
966. [[a1c7p3] Pasywka wroga [837802] — opis] 턴 종료시, 자신의 정신력이 5 감소하고 가장 정신력이 낮은 아군 혈귀의 정신력 10 회복 (정신력이 있는 대상이 없으면 발동하지 않음)
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837802].desc
   limit: do 170 znaków
   EN: Turn End: lose 5 SP and heal 10 SP for an allied Bloodfiend with the least SP (does not activate if there aren't any allies with SP)
   PL: Koniec tury: traci 5 SP i przywraca 10 SP sojuszniczemu Bloodfiendowi z najniższym SP (nie uruchamia się, jeżeli nie ma sojuszników z SP)
967. [[a1c7p3] Pasywka wroga [837803] — nazwa] 닳아버린 마음
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837803].name
   limit: do 40 znaków
   EN: Ailing Heart
   PL: Ailing Heart
968. [[a1c7p3] Pasywka wroga [837803] — opis] 자신의 [WornHeart]의 수치에 따라 패턴이 변경됨\n턴 종료시, [WornHeart] 1 얻음
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837803].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WornHeart]
   znaczenie tagów: [WornHeart] = 닳아버린 마음 / Ailing Heart
   EN: Gains new patterns based on [WornHeart] value on self\nTurn End: gain 1 [WornHeart]
   PL: przybiera nowe wzorce w zależności od wartości [WornHeart] tej jednostki\nKoniec tury: zyskuje 1 [WornHeart]
969. [[a1c7p3] Pasywka wroga [837805] — nazwa] 피로 물든 손
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837805].name
   limit: do 40 znaków
   EN: Bloodied Hand
   PL: Bloodied Hand
970. [[a1c7p3] Pasywka wroga [837805] — opis] - [BloodyHand]이 10 이상이면, [BloodyHand_2nd] 로 전환됨.\n- [BloodyHand_2nd]이 20 이상이면, [BloodyHand_3rd] 으로 전환됨.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837805].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [BloodyHand], [BloodyHand_2nd], [BloodyHand_3rd]
   znaczenie tagów: [BloodyHand] = 피로 물든 손 / Bloodied Hand; [BloodyHand_2nd] = 피로 물든 손 II / Bloodied Hand II; [BloodyHand_3rd] = 피로 물든 손 III / Bloodied Hand III
   EN: - At 10+ [BloodyHand], convert them to [BloodyHand_2nd].\n- At 20+ [BloodyHand_2nd], convert them to [BloodyHand_3rd].
   PL: - przy 10+ [BloodyHand], przekształca je w [BloodyHand_2nd].\n- przy 20+ [BloodyHand_2nd], przekształca je w [BloodyHand_3rd].
971. [[a1c7p3] Pasywka wroga [837901] — nazwa] 사랑했던 이들
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837901].name
   limit: do 40 znaków
   EN: The Once-loved Ones
   PL: The Once-loved Ones
972. [[a1c7p3] Pasywka wroga [837901] — opis] 턴 시작 시 모든 적이 [AffectionTeddy]을 보유하였다면, 강력한 스킬을 사용
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837901].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AffectionTeddy]
   znaczenie tagów: [AffectionTeddy] = 애착 / Attachment
   EN: Turn Start: if all enemies have [AffectionTeddy], use a powerful Skill
   PL: Początek tury: jeżeli wszyscy wrogowie mają [AffectionTeddy], używa potężnej Umiejętności
973. [[a1c7p3] Pasywka wroga [837902] — nazwa] 늘어붙은 쇠말뚝
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837902].name
   limit: do 40 znaków
   EN: Grimy Iron Stake
   PL: Grimy Iron Stake
974. [[a1c7p3] Pasywka wroga [837902] — opis] 단일 코인 스킬을 사용하여 적에게 적중 시, 대상에게 [Laceration] 위력 3을 부여하고 다음 턴까지 [DefenseDown] 2 부여\n대상이 [Laceration] 상태일 경우, 효과가 강화되어 [Laceration] 위력 5 부여
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837902].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [DefenseDown]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When hitting an enemy using a single-Coin Skill, inflict 3 [Laceration] Potency. Inflict 2 [DefenseDown] until the end of the next turn.\nIf the target already has [Laceration], inflict 5 [Laceration] Potency instead
   PL: przy trafieniu wroga Umiejętnością z jedną Monetą nakłada 3 Siły [Laceration] i 2 [DefenseDown] do końca następnej tury\njeżeli cel ma już [Laceration], zamiast tego nakłada 5 Siły [Laceration]
975. [[a1c7p3] Pasywka wroga [837903] — nazwa] 기억하기
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837903].name
   limit: do 40 znaków
   EN: To Remember
   PL: To Remember
976. [[a1c7p3] Pasywka wroga [837903] — opis] 이번 턴에 서글픈 포옹의 턴 종료 시 효과로 흐트러졌다면, 다음 턴 시작 시 [FaintMemory] 10 얻음
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837903].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [FaintMemory]
   znaczenie tagów: [FaintMemory] = 아련한 기억 / Faint Memories
   EN: If this unit was Staggered due to the Turn End effect of A Sad Embrace, gain 10 [FaintMemory] at the next Turn Start
   PL: jeżeli Oszołamienie nastąpiło przez efekt końca tury „A Sad Embrace”, na Początku następnej tury zyskuje 10 [FaintMemory]
977. [[a1c7p3] Pasywka wroga [837904] — nazwa] 사랑 베풀기
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837904].name
   limit: do 40 znaków
   EN: To Love
   PL: To Love
978. [[a1c7p3] Pasywka wroga [837904] — opis] 턴 종료 시 체력이 30% 이하인 상태라면 모든 적에게 [AffectionTeddy] 3을 부여하는 대신 다음 턴에 [AttackDown] 15 얻음 (전투당 1회)
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837904].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [AffectionTeddy], [AttackDown]
   znaczenie tagów: [AffectionTeddy] = 애착 / Attachment; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: If at less than or equal to 30% HP at Turn End: instead of inflicting 3 [AffectionTeddy] to all enemies, gain 15 [AttackDown] next turn (once per Encounter)
   PL: jeżeli na koniec tury HP wynosi 30% lub mniej: zamiast nakładać 3 [AffectionTeddy] wszystkim wrogom, zyskuje 15 [AttackDown] w następnej turze (1 raz na walkę)
979. [[a1c7p3] Pasywka wroga [837905] — nazwa] 아프지 않기를
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837905].name
   limit: do 40 znaków
   EN: Please Don't be Sick
   PL: Please Don't be Sick
980. [[a1c7p3] Pasywka wroga [837905] — opis] 대상이 보유한 부정적 효과의 종류 수 3개당 기본 위력 1 감소 (최대 3)
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837905].desc
   limit: do 120 znaków
   EN: Base Power -1 for every 3 types of negative effects on the target (max 3)
   PL: Moc Bazowa -1 za każde 3 typy negatywnych efektów celu (maks. 3)
981. [[a1c7p3] Pasywka wroga [837301] — nazwa] 죄악 저항
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837301].name
   limit: do 40 znaków
   EN: Sin Resistance
   PL: Sin Resistance
982. [[a1c7p3] Pasywka wroga [837301] — opis] 흐트러짐 상태, 부위 파괴 상태가 아니라면 자신이 받는 [Laceration] 피해 50% 감소
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Unless this unit is Staggered or Part Broken, take 50% less [Laceration] damage
   PL: o ile ta jednostka nie jest w Oszołamieniu i nie ma zniszczonej Części, otrzymuje o 50% mniej obrażeń [Laceration]
983. [[a1c7p3] Pasywka wroga [837401] — nazwa] 죄악 저항
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837401].name
   (powtórzenie elementu 981 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
984. [[a1c7p3] Pasywka wroga [837401] — opis] 흐트러짐 상태, 부위 파괴 상태가 아니라면 크리티컬 피해를 받을 때 크리티컬 피해량의 절반만큼 받음.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837401].desc
   limit: do 120 znaków
   EN: Unless this unit is Staggered or Part Broken, take only half of Critical Damage.
   PL: o ile ta jednostka nie jest w Oszołamieniu i nie ma zniszczonej Części, otrzymuje tylko połowę obrażeń krytycznych.
985. [[a1c7p3] Pasywka wroga [837501] — nazwa] 카르밀라
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837501].name
   limit: do 40 znaków
   EN: Carmilla
   PL: Carmilla
986. [[a1c7p3] Pasywka wroga [837501] — opis] 턴 시작 시, 무작위 적 1명의 최대 체력 5%만큼 고정 피해를 입힘.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837501].desc
   limit: do 120 znaków
   EN: Turn Start: to a random enemy, deal fixed damage equal to 5% of their HP.
   PL: Początek tury: zadaje losowemu wrogowi stałe obrażenia równe 5% jego HP.
987. [[a1c7p3] Pasywka wroga [837502] — nazwa] 한 방울의 양분
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837502].name
   limit: do 40 znaków
   EN: A Drop of Nourishment
   PL: A Drop of Nourishment
988. [[a1c7p3] Pasywka wroga [837502] — opis] 공격 종료 시 자신의 공격 스킬로 입힌 피해량의 절반만큼 본체, 부위 체력 회복\n- 자신의 체력이 100%라면, 다음 턴에 [AttackUp] 2 얻음. (최대 2회)\n회복한 체력 비율에 따라 다음의 효과를 누적으로 받음\n- 수치 1 이상: 매 턴 시작 시 방어 레벨 증가 3 얻음\n- 수치 2 이상: 매 턴 시작 시 [AttackUp] 3 얻음\n- 수치 3 이상: 매 턴 시작 시 속도 최솟값 +2, 최댓값 +2\n- 수치 5 이상: 매 턴 시작 시 [Enhancement] 3 얻음
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837502].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [Enhancement]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Attack End: Heal Core and Part equal to 50% of the damage this unit dealt with its Attack Skill\n- At 100% HP, gain 2 [AttackUp] next turn. (2 times max)\nBased on the percentage of HP healed, gain the following effects (cumulative)\n- At 1+ Stack: Gain 3 Defense Level Up at every Turn Start\n- At 2+ Stack: Gain 3 [AttackUp] at every Turn Start\n- At 3+ Stack: Gain +2 Min & Max Speed\n- At 5+ Stack: Gain 3 [Enhancement] at every Turn Start
   PL: po zakończeniu Ataku: przywraca Korpusowi i Części HP równe połowę obrażeń zadanych własnymi Umiejętnościami ataku\n- przy 100% HP zyskuje 2 [AttackUp] w następnej turze. (do 2 razy)\nw zależności od procentu przywróconego HP kumuluje następujące efekty:\n- przy wartości 1+: zyskuje 3 Wzrost Poziomu Obrony na każdym Początku tury\n- przy wartości 2+: zyskuje 3 [AttackUp] na każdym Początku tury\n- przy wartości 3+: Min. i Maks. Szybkość +2\n- przy wartości 5+: zyskuje 3 [Enhancement] na każdym Początku tury
989. [[a1c7p3] Pasywka wroga [837503] — nazwa] 옭아매는 한 송이
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837503].name
   limit: do 40 znaków
   EN: A Single Strangling Flower
   PL: A Single Strangling Flower
990. [[a1c7p3] Pasywka wroga [837503] — opis] 공격 종료 시 [TinyCarmilla] 1을 부여함\n[Laceration]이 있는 대상일 경우, 공격 종료 시 [TinyCarmilla] 1 추가 부여
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837503].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [TinyCarmilla], [Laceration]
   znaczenie tagów: [TinyCarmilla] = 작은 카르밀라 / Little Carmilla; [Laceration] = 출혈 / Bleed
   EN: Attack End: Inflict 1 [TinyCarmilla]\nIf the target has [Laceration], inflict 1 additional [TinyCarmilla] at Attack End
   PL: po zakończeniu Ataku nakłada 1 [TinyCarmilla]\njeżeli cel ma [Laceration], po zakończeniu Ataku nakłada dodatkowo 1 [TinyCarmilla]
991. [[a1c7p3] Pasywka wroga [837601] — nazwa] 가시 채찍
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837601].name
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
992. [[a1c7p3] Pasywka wroga [837601] — opis] 공격 직전 대상에게 [Burst]이 있으면, 20%확률로 [Burst] 횟수 1 증가\n대상에게 [ThornNoose]를 부여할 때, 가시 올가미를 생성함.
   źródło: Passives_Abnormality-a1c7p3.json :: dataList[id=837601].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [ThornNoose]
   znaczenie tagów: [Burst] = 파열 / Rupture; [ThornNoose] = 가시 올가미 / Barbed Lasso
   EN: If the target has [Burst] immediately before attack, 20% chance to inflict +1 [Burst] Count\nWhen inflicting [ThornNoose], generate a 'Barbed Lasso' Unit.
   PL: jeżeli cel ma [Burst] bezpośrednio przed atakiem, 20% szans na nałożenie 1 Licznika [Burst]\nprzy nakładaniu [ThornNoose] tworzy jednostkę „Barbed Lasso”.
