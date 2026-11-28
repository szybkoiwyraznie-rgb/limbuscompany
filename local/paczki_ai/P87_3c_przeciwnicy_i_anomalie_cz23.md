# Paczka AI P87 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 23/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P87_3c_przeciwnicy_i_anomalie_cz23.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P87_3c_przeciwnicy_i_anomalie_cz23.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [x1p1c1] Umiejętności wrogów / Anomalii — Skills_Abnormality-x1p1c1
- grupa rozdziału/trybu: `x1p1c1` · plik: `Skills_Abnormality-x1p1c1.json`

1. [Umiejętność wroga [138701] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력 5 회복
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Target heals 5 SP
   PL:
2. [Umiejętność wroga [138701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력 5 회복
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target heals 5 SP
   PL:
3. [Umiejętność wroga [138702] (ulepszenie 1) — nazwa] 끄극
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138702].levelList[level=1].name
   limit: do 40 znaków
   EN: Khgh
   PL:
4. [Umiejętność wroga [138702] (ulepszenie 1) — opis] [WideAreaRampage]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WideAreaRampage]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley
   EN: [WideAreaRampage]
   PL:
5. [Umiejętność wroga [138702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
6. [Umiejętność wroga [138702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Umiejętność wroga [138702] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
8. [Umiejętność wroga [138703] (ulepszenie 1) — nazwa] 끄긱
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138703].levelList[level=1].name
   limit: do 40 znaków
   EN: Screecoo!
   PL:
9. [Umiejętność wroga [138703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL:
10. [Umiejętność wroga [138703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
11. [Umiejętność wroga [138704] (ulepszenie 1) — nazwa] 끅
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138704].levelList[level=1].name
   limit: do 40 znaków
   EN: Khk
   PL:
12. [Umiejętność wroga [138704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL:
13. [Umiejętność wroga [138705] (ulepszenie 1) — nazwa] 닭들의 종말
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138705].levelList[level=1].name
   limit: do 40 znaków
   EN: Poultry Apocalypse
   PL:
14. [Umiejętność wroga [138705] (ulepszenie 1) — opis] [CantDuel]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138705].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel]
   PL:
15. [Umiejętność wroga [138705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
16. [Umiejętność wroga [138705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [Umiejętność wroga [138705] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138705].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [Umiejętność wroga [138706] (ulepszenie 1) — nazwa] 끄그극
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138706].levelList[level=1].name
   limit: do 40 znaków
   EN: Keghgh
   PL:
19. [Umiejętność wroga [138706] (ulepszenie 1) — opis] [CanDuelGuard]\n[WinDuel] 대상의 정신력 5 회복
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138706].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n[WinDuel] Target heals 5 SP
   PL:
20. [Umiejętność wroga [138706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-x1p1c1.json :: dataList[id=138706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:

## [x1p1c1] Umiejętności wrogów / Anomalii — Skills_Enemy-x1p1c1
- grupa rozdziału/trybu: `x1p1c1` · plik: `Skills_Enemy-x1p1c1.json`

21. [Umiejętność wroga [9103901] (ulepszenie 1) — nazwa] 꾸옥
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9103901].levelList[level=1].name
   limit: do 40 znaków
   EN: Kwogh
   PL:
22. [Umiejętność wroga [9103902] (ulepszenie 1) — nazwa] 꾸오옥
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9103902].levelList[level=1].name
   limit: do 40 znaków
   EN: Kwaagh
   PL:
23. [Umiejętność wroga [9104001] (ulepszenie 1) — nazwa] 꼬고곡!
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104001].levelList[level=1].name
   limit: do 40 znaków
   EN: Babawbawk!
   PL:
24. [Umiejętność wroga [9104001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bind next turn
   PL:
25. [Umiejętność wroga [9104002] (ulepszenie 1) — nazwa] 꼭꼭!
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104002].levelList[level=1].name
   limit: do 40 znaków
   EN: Cluckcluck!
   PL:
26. [Umiejętność wroga [9104002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 더하기 코인 약화 4 부여
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Plus Coin Drop next turn
   PL:
27. [Umiejętność wroga [9104003] (ulepszenie 1) — nazwa] 꼬오옥!
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104003].levelList[level=1].name
   limit: do 40 znaków
   EN: Cluuuck!
   PL:
28. [Umiejętność wroga [9104003] (ulepszenie 1) — opis] [WinDuel] 스킬 위력 +1
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104003].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Skill Power +1
   PL:
29. [Umiejętność wroga [9104101] (ulepszenie 1) — nazwa] 꼭
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104101].levelList[level=1].name
   limit: do 40 znaków
   EN: Coo
   PL:
30. [Umiejętność wroga [9104101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 진동 1 부여
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Tremor next turn
   PL:
31. [Umiejętność wroga [9104101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 진동 1 부여
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
32. [Umiejętność wroga [9104101] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 진동 1 부여
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104101].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
33. [Umiejętność wroga [9104102] (ulepszenie 1) — nazwa] 고고곡
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104102].levelList[level=1].name
   limit: do 40 znaków
   EN: Gwoghkwogh
   PL:
34. [Umiejętność wroga [9104102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 진동 횟수 1 증가
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Tremor Count next turn
   PL:
35. [Umiejętność wroga [9104103] (ulepszenie 1) — nazwa] 고곡
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104103].levelList[level=1].name
   limit: do 40 znaków
   EN: Bwoghkh
   PL:
36. [Umiejętność wroga [9104103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 진동 3 부여
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Tremor next turn
   PL:
37. [Umiejętność wroga [9104103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Trigger Tremor Burst
   PL:
38. [Umiejętność wroga [9104104] (ulepszenie 1) — nazwa] 꼬곡
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104104].levelList[level=1].name
   limit: do 40 znaków
   EN: Khgwok
   PL:
39. [Umiejętność wroga [9104104] (ulepszenie 1) — opis] [WhenUse] 체력 10 회복
   źródło: Skills_Enemy-x1p1c1.json :: dataList[id=9104104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 10 HP
   PL:

## [x1p1c1] Pasywka wroga: Passives_Abnormality-x1p1c1
- plik gry: `Passives_Abnormality-x1p1c1.json`

40. [[x1p1c1] Pasywka wroga [136501] — nazwa] 뽕.황의 위엄
   źródło: Passives_Abnormality-x1p1c1.json :: dataList[id=136501].name
   limit: do 40 znaków
   EN: Dignity of the B.E.
   PL:
41. [[x1p1c1] Pasywka wroga [136501] — opis] 턴 종료 시, 모든 적에게 5만큼 정신력 피해
   źródło: Passives_Abnormality-x1p1c1.json :: dataList[id=136501].desc
   limit: do 120 znaków
   EN: Turn End: Deal 5 SP damage to all enemies
   PL:
42. [[x1p1c1] Pasywka wroga [136502] — nazwa] 삐져나온닭
   źródło: Passives_Abnormality-x1p1c1.json :: dataList[id=136502].name
   limit: do 40 znaków
   EN: Bulging Chicken
   PL:
43. [[x1p1c1] Pasywka wroga [136502] — opis] 피격 시 [LeakedOutSauce] 1 얻음
   źródło: Passives_Abnormality-x1p1c1.json :: dataList[id=136502].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [LeakedOutSauce]
   znaczenie tagów: [LeakedOutSauce] = 새어나온 양념장 / Leaking Marinade
   EN: When Hit: Gain 1 [LeakedOutSauce]
   PL:
44. [[x1p1c1] Pasywka wroga [136503] — nazwa] 탱고 닭양념장
   źródło: Passives_Abnormality-x1p1c1.json :: dataList[id=136503].name
   limit: do 40 znaków
   EN: Tango Marinade
   PL:
45. [[x1p1c1] Pasywka wroga [136503] — opis] 대상보다 속도가 높다면, 합 위력 (속도 / 3)만큼 추가
   źródło: Passives_Abnormality-x1p1c1.json :: dataList[id=136503].desc
   limit: do 120 znaków
   EN: If this unit's Speed is faster than the target's, Clash Power +(Speed / 3)
   PL:
46. [[x1p1c1] Pasywka wroga [138701] — nazwa] 입에 직접 쑤셔 넣어 주겠어!
   źródło: Passives_Abnormality-x1p1c1.json :: dataList[id=138701].name
   limit: do 50 znaków
   EN: I'll Just Have to Force-feed You!
   PL:
47. [[x1p1c1] Pasywka wroga [138701] — opis] 턴 종료 시, 다음 턴에 모든 적에게 [DeliciousSauce] 1 부여
   źródło: Passives_Abnormality-x1p1c1.json :: dataList[id=138701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DeliciousSauce]
   znaczenie tagów: [DeliciousSauce] = 황금 비법 소스 / Golden Recipe Sauce
   EN: Turn End: Inflict 1 [DeliciousSauce] on all enemies next turn
   PL:
48. [[x1p1c1] Pasywka wroga [138702] — nazwa] 다 함께 요리를 만들어요
   źródło: Passives_Abnormality-x1p1c1.json :: dataList[id=138702].name
   limit: do 40 znaków
   EN: Let's All Cook Together!
   PL:
49. [[x1p1c1] Pasywka wroga [138702] — opis] 턴 종료 시, 전투에 참여 중인 자신을 제외한 모든 적과 아군 정신력 10 회복.
   źródło: Passives_Abnormality-x1p1c1.json :: dataList[id=138702].desc
   limit: do 130 znaków
   EN: Turn End: Heal 10 SP for all allies and enemies participating in this battle (excluding this unit)
   PL:
50. [[x1p1c1] Pasywka wroga [138703] — nazwa] 아이들을 위해서였어요
   źródło: Passives_Abnormality-x1p1c1.json :: dataList[id=138703].name
   limit: do 40 znaków
   EN: It was All... for the Kids.
   PL:
51. [[x1p1c1] Pasywka wroga [138703] — opis] 자신의 공격 적중시, 대상의 잃은 체력 1%당 가하는 피해량 -1%
   źródło: Passives_Abnormality-x1p1c1.json :: dataList[id=138703].desc
   limit: do 120 znaków
   EN: On Attack Hit: Deal -1% damage for every 1% missing HP on target
   PL:

## [x1p1c1] Pasywka wroga: Passives_Enemy-x1p1c1
- plik gry: `Passives_Enemy-x1p1c1.json`

52. [[x1p1c1] Pasywka wroga [9103901] — nazwa] 삐져나온닭
   źródło: Passives_Enemy-x1p1c1.json :: dataList[id=9103901].name
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [[x1p1c1] Pasywka wroga [9103901] — opis] 피격 시 [LeakedOutSauce] 1 얻음 (전투당 6회)
   źródło: Passives_Enemy-x1p1c1.json :: dataList[id=9103901].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [LeakedOutSauce]
   znaczenie tagów: [LeakedOutSauce] = 새어나온 양념장 / Leaking Marinade
   EN: When Hit: Gain 1 [LeakedOutSauce] (6 times per Encounter)
   PL:
54. [[x1p1c1] Pasywka wroga [9103902] — nazwa] 비어버린닭
   źródło: Passives_Enemy-x1p1c1.json :: dataList[id=9103902].name
   limit: do 40 znaków
   EN: Hollowed Chicken
   PL:
55. [[x1p1c1] Pasywka wroga [9103902] — opis] 양념장이 모두 빠져나갔다면, 턴 시작 시 [Vulnerable] 2 얻음
   źródło: Passives_Enemy-x1p1c1.json :: dataList[id=9103902].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Turn Start: Gain 2 [Vulnerable] if this unit has no Marinade
   PL:
56. [[x1p1c1] Pasywka wroga [9104101] — nazwa] HP 앰플
   źródło: Passives_Enemy-x1p1c1.json :: dataList[id=9104101].name
   limit: do 40 znaków
   EN: HP Ampule
   PL:
57. [[x1p1c1] Pasywka wroga [9104101] — opis] 턴 시작시 체력 15 회복\n체력이 50% 미만이면 체력 15 추가 회복
   źródło: Passives_Enemy-x1p1c1.json :: dataList[id=9104101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Heal 15 HP\nAt less than 50% HP, heal 15 additional HP
   PL:

## [ycgd] Wróg / część: Enemies-ycgd
- plik gry: `Enemies-ycgd.json`

58. [[ycgd] Wróg / część [90110] — nazwa] 결연한 흑운회 조직원
   źródło: Enemies-ycgd.json :: dataList[id=90110].name
   limit: do 40 znaków
   EN: Determined Kurokumo Henchman
   PL:
59. [[ycgd] Wróg / część [90110] — opis] 본체
   źródło: Enemies-ycgd.json :: dataList[id=90110].desc
   limit: do 120 znaków
   EN: Core
   PL:
60. [[ycgd] Wróg / część [90111] — nazwa] 긴장한 흑운회 조직원
   źródło: Enemies-ycgd.json :: dataList[id=90111].name
   limit: do 40 znaków
   EN: Tense Kurokumo Henchman
   PL:
61. [[ycgd] Wróg / część [90111] — opis] 본체
   źródło: Enemies-ycgd.json :: dataList[id=90111].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [[ycgd] Wróg / część [90112] — nazwa] 능숙한 흑운회 조직원
   źródło: Enemies-ycgd.json :: dataList[id=90112].name
   limit: do 40 znaków
   EN: Adept Kurokumo Henchwoman
   PL:
63. [[ycgd] Wróg / część [90112] — opis] 본체
   źródło: Enemies-ycgd.json :: dataList[id=90112].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [[ycgd] Wróg / część [90113] — nazwa] 나른한 흑운회 조직원
   źródło: Enemies-ycgd.json :: dataList[id=90113].name
   limit: do 40 znaków
   EN: Tired Kurokumo Henchwoman
   PL:
65. [[ycgd] Wróg / część [90113] — opis] 본체
   źródło: Enemies-ycgd.json :: dataList[id=90113].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [[ycgd] Wróg / część [91013] — nazwa] 흑운회 부조장 쥰
   źródło: Enemies-ycgd.json :: dataList[id=91013].name
   limit: do 40 znaków
   EN: Kurokumo Clan Captain Jun
   PL:
67. [[ycgd] Wróg / część [91013] — opis] 본체
   źródło: Enemies-ycgd.json :: dataList[id=91013].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [[ycgd] Wróg / część [8151] — nazwa] 분노 죄종?
   źródło: Enemies-ycgd.json :: dataList[id=8151].name
   limit: do 40 znaków
   EN: Peccatulum Irae?
   PL:
69. [[ycgd] Wróg / część [8151] — opis] 본체
   źródło: Enemies-ycgd.json :: dataList[id=8151].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [[ycgd] Wróg / część [8152] — nazwa] 우울 죄종?
   źródło: Enemies-ycgd.json :: dataList[id=8152].name
   limit: do 40 znaków
   EN: Peccatulum Morositatis?
   PL:
71. [[ycgd] Wróg / część [8152] — opis] 본체
   źródło: Enemies-ycgd.json :: dataList[id=8152].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [[ycgd] Wróg / część [8153] — nazwa] 뒤틀려가는 김삿갓
   źródło: Enemies-ycgd.json :: dataList[id=8153].name
   limit: do 40 znaków
   EN: Distorting Bamboo-hatted Kim
   PL:
73. [[ycgd] Wróg / część [8153] — opis] 본체
   źródło: Enemies-ycgd.json :: dataList[id=8153].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [[ycgd] Wróg / część [8154] — nazwa] 뒤틀린 김삿갓
   źródło: Enemies-ycgd.json :: dataList[id=8154].name
   limit: do 40 znaków
   EN: Distorted Bamboo-hatted Kim
   PL:
75. [[ycgd] Wróg / część [8154] — opis] 본체
   źródło: Enemies-ycgd.json :: dataList[id=8154].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [ycgd] Umiejętności wrogów / Anomalii — Skills_Abnormality-ycgd
- grupa rozdziału/trybu: `ycgd` · plik: `Skills_Abnormality-ycgd.json`

76. [Umiejętność wroga [815101] (ulepszenie 1) — nazwa] 찔러넣기
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815101].levelList[level=1].name
   limit: do 40 znaków
   EN: Plunge In
   PL:
77. [Umiejętność wroga [815101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 5 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion] and +2 [Combustion] Count
   PL:
78. [Umiejętność wroga [815102] (ulepszenie 1) — nazwa] 꼬리치기
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815102].levelList[level=1].name
   limit: do 40 znaków
   EN: Tail Whisk
   PL:
79. [Umiejętność wroga [815102] (ulepszenie 1) — opis] [WinDuel] 대상에게 [Combustion]이 있을 때, 기본 위력 +2
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Combustion]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Combustion] = 화상 / Burn
   EN: [WinDuel] If target has [Combustion], Base Power +2
   PL:
80. [Umiejętność wroga [815102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 5 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Umiejętność wroga [815103] (ulepszenie 1) — nazwa] 숨결 불어넣기
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815103].levelList[level=1].name
   limit: do 40 znaków
   EN: Blow in Breath
   PL:
82. [Umiejętność wroga [815103] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion]이 5이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815103].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: [WhenUse] If target has 5+ [Combustion], Coin Power +1
   PL:
83. [Umiejętność wroga [815103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +2 [Combustion] Count
   PL:
84. [Umiejętność wroga [815103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [CrimsonTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [CrimsonTakeDamageUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility
   EN: [OnSucceedAttackHead] Inflict 1 [CrimsonTakeDamageUp] next turn
   PL:
85. [Umiejętność wroga [815103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 8 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 8 [Combustion]
   PL:
86. [Umiejętność wroga [815103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [CrimsonTakeDamageUp] 1 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność wroga [815104] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815104].levelList[level=1].name
   limit: do 40 znaków
   EN: Counter
   PL:
88. [Umiejętność wroga [815104] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion]이 5이상이면, 코인 위력 +2
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: [WhenUse] If target has 5+ [Combustion], Coin Power +2
   PL:
89. [Umiejętność wroga [815104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp_Weak] 1 얻음
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgUp_Weak]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgUp_Weak] = 약점 공격 시 피해 증가 / Weak-resist DMG Boost
   EN: [OnSucceedAttack] Gain 1 [AttackDmgUp_Weak] next turn
   PL:
90. [Umiejętność wroga [815201] (ulepszenie 1) — nazwa] 뛰어들기
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815201].levelList[level=1].name
   limit: do 40 znaków
   EN: Leap In
   PL:
91. [Umiejętność wroga [815201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] and +2 [Sinking] Count
   PL:
92. [Umiejętność wroga [815201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [Umiejętność wroga [815202] (ulepszenie 1) — nazwa] 쏘아붙이기
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815202].levelList[level=1].name
   limit: do 40 znaków
   EN: Snap At
   PL:
94. [Umiejętność wroga [815202] (ulepszenie 1) — opis] [WinDuel] 대상에게 [Sinking]이 있을 때, 기본 위력 +2
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Sinking]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Sinking] = 침잠 / Sinking
   EN: [WinDuel] If target has [Sinking], Base Power +2
   PL:
95. [Umiejętność wroga [815202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여, [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking] and +3 [Sinking] Count
   PL:
96. [Umiejętność wroga [815203] (ulepszenie 1) — nazwa] 물폭탄
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815203].levelList[level=1].name
   limit: do 40 znaków
   EN: Water Bomb
   PL:
97. [Umiejętność wroga [815203] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking]이 5이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815203].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 5+ [Sinking], Coin Power +1
   PL:
98. [Umiejętność wroga [815203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 8 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 8 [Sinking]
   PL:
99. [Umiejętność wroga [815203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [AzureTakeDamageUp] 2 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [AzureTakeDamageUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [AzureTakeDamageUp] = 우울 취약 / Gloom Fragility
   EN: [OnSucceedAttackHead] Inflict 2 [AzureTakeDamageUp] next turn
   PL:
100. [Umiejętność wroga [815204] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815204].levelList[level=1].name
   limit: do 40 znaków
   EN: Evade
   PL:
101. [Umiejętność wroga [815204] (ulepszenie 1) — opis] [OnSucceedEvade] 대상에게 [Sinking] 2 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Sinking]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedEvade] Inflict 2 [Sinking]
   PL:
102. [Umiejętność wroga [815301] (ulepszenie 1) — nazwa] 발검
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815301].levelList[level=1].name
   limit: do 40 znaków
   EN: Draw of the Sword
   PL:
103. [Umiejętność wroga [815301] (ulepszenie 1) — opis] [WhenUse] [Breath] 2 얻음
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 2 [Breath]
   PL:
104. [Umiejętność wroga [815301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
105. [Umiejętność wroga [815301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Umiejętność wroga [815302] (ulepszenie 1) — nazwa] 절동
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815302].levelList[level=1].name
   limit: do 40 znaków
   EN: Paralyzer
   PL:
107. [Umiejętność wroga [815302] (ulepszenie 1) — opis] [WhenUse] [Breath] 2 얻음
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815302].levelList[level=1].desc
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Umiejętność wroga [815302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Umiejętność wroga [815302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp] 1 얻음
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [OnSucceedAttack] Gain 1 [AttackDmgUp] next turn
   PL:
110. [Umiejętność wroga [815302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
111. [Umiejętność wroga [815302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 1 [Paralysis] next turn
   PL:
112. [Umiejętność wroga [815302] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Umiejętność wroga [815302] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815302].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Umiejętność wroga [815303] (ulepszenie 1) — nazwa] 처단
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815303].levelList[level=1].name
   limit: do 40 znaków
   EN: Slay
   PL:
115. [Umiejętność wroga [815303] (ulepszenie 1) — opis] [WinDuel] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WinDuel] Gain +1 [Breath] Count
   PL:
116. [Umiejętność wroga [815303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음, [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath] and +1 [Breath] Count
   PL:
117. [Umiejętność wroga [815303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Umiejętność wroga [815303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [SlashDamageUp] 1 얻음
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: [OnSucceedAttack] Gain 1 [SlashDamageUp] next turn
   PL:
119. [Umiejętność wroga [815303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [SlashResistDown] 2 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [OnSucceedAttack] Inflict 2 [SlashResistDown] next turn
   PL:
120. [Umiejętność wroga [815304] (ulepszenie 1) — nazwa] 살주
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815304].levelList[level=1].name
   limit: do 40 znaków
   EN: Overthrow
   PL:
121. [Umiejętność wroga [815304] (ulepszenie 1) — opis] [WinDuel] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WinDuel] Gain +3 [Breath] Count
   PL:
122. [Umiejętność wroga [815304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음, [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath] and +1 [Breath] Count
   PL:
123. [Umiejętność wroga [815304] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
124. [Umiejętność wroga [815304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [SlashDamageUp] 2 얻음
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: [OnSucceedAttack] Gain 2 [SlashDamageUp] next turn
   PL:
125. [Umiejętność wroga [815304] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [SlashResistDown] 2 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815304].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [OnSucceedAttack] Inflict 2 [SlashResistDown]
   PL:
126. [Umiejętność wroga [815304] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815304].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL:
127. [Umiejętność wroga [815304] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815304].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis] next turn
   PL:
128. [Umiejętność wroga [815304] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttackHead] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815304].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict +3 [Laceration] Count
   PL:
129. [Umiejętność wroga [815305] (ulepszenie 1) — nazwa] 골단
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815305].levelList[level=1].name
   limit: do 40 znaków
   EN: To Claim Their Bones
   PL:
130. [Umiejętność wroga [815305] (ulepszenie 1) — opis] [StartBattle] 보호막 50 얻음\n[WhenUse] 보호막이 전부 소모되지 않았다면, 합 위력 +5
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815305].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Gain 50 Shield\n[WhenUse] If the Shield isn't fully depleted, Clash Power +5
   PL:
131. [Umiejętność wroga [815305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [SlashResistDown] 3 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [OnSucceedAttack] Inflict 3 [SlashResistDown]
   PL:
132. [Umiejętność wroga [815305] (ulepszenie 1) — moneta 2, efekt 1 — opis] 크리티컬 피해량 +100%
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815305].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   EN: +100% Damage on Critical Hit
   PL:
133. [Umiejętność wroga [815305] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 10 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815305].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 10 [Laceration] and +2 [Laceration] Count
   PL:
134. [Umiejętność wroga [815305] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 보호막이 전부 소모되지 않았다면, 공격 가중치만큼 [Grudge] 수치를 나눠 고정 피해로 부여함.
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815305].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Grudge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Grudge] = 맺혀가는 응어리 / Growing Resentment
   EN: [OnSucceedAttack] If the Shield isn't fully depleted, divide [Grudge] value by Atk Weight and inflict it as fixed damage.
   PL:
135. [Umiejętność wroga [815306] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815306].levelList[level=1].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Umiejętność wroga [815306] (ulepszenie 1) — opis] [OnSucceedEvade] [Breath] 4 얻음
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815306].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [Breath]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [OnSucceedEvade] Gain 4 [Breath]
   PL:
137. [Umiejętność wroga [815307] (ulepszenie 1) — nazwa] 육참
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815307].levelList[level=1].name
   limit: do 40 znaków
   EN: Yield My Flesh
   PL:
138. [Umiejętność wroga [815307] (ulepszenie 1) — opis] 반격 스킬을 발동시킨 스킬로 받은 피해량만큼 다음 턴에 [Grudge]를 얻음
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815307].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Grudge]
   znaczenie tagów: [Grudge] = 맺혀가는 응어리 / Growing Resentment
   EN: Gain X [Grudge] next turn (X = Damage dealt by the Skill that activated the Counter Skill)
   PL:
139. [Umiejętność wroga [815405] (ulepszenie 1) — nazwa] 골단
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815405].levelList[level=1].name
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Umiejętność wroga [815405] (ulepszenie 1) — opis] [StartBattle] 보호막 200 얻음\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n[WhenUse] 보호막이 전부 소모되지 않았다면, 합 위력 +10
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815405].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [StartBattle] Gain 200 Shield\n[WhenUse] Gain +3 [Breath] Count\n[WhenUse] If the Shield isn't fully depleted, Clash Power +10
   PL:
141. [Umiejętność wroga [815405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [SlashResistDown] 3 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [Umiejętność wroga [815405] (ulepszenie 1) — moneta 2, efekt 1 — opis] 크리티컬 피해량 +100%
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815405].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 132 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność wroga [815405] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 5 부여
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815405].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 5 [Paralysis] next turn
   PL:
144. [Umiejętność wroga [815405] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Laceration] 10 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815405].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Umiejętność wroga [815405] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 보호막이 전부 소모되지 않았다면, 공격 가중치만큼 [Grudge] 수치를 나눠 고정 피해로 부여함.
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815405].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 134 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Umiejętność wroga [815408] (ulepszenie 1) — nazwa] 칼춤
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815408].levelList[level=1].name
   limit: do 40 znaków
   EN: Blade Dance
   PL:
147. [Umiejętność wroga [815408] (ulepszenie 1) — opis] [EnemyKill] 다음 턴에 [AttackUp] 3, [DefenseUp] 3 얻음
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815408].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [AttackUp], [DefenseUp]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [EnemyKill] Gain 3 [AttackUp] and 3 [DefenseUp] next turn
   PL:
148. [Umiejętność wroga [815409] (ulepszenie 1) — nazwa] 골단
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815409].levelList[level=1].name
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Umiejętność wroga [815409] (ulepszenie 1) — opis] [CantChangeTarget]\n체력이 가장 없는 대상 우선 공격\n[EnemyKill] [Grudge]가 2배가 됨.\n[EnemyKill] [Grudge]만큼 체력 회복
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815409].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [EnemyKill], [Grudge]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [EnemyKill] = [적 처치 시] / [On Kill]; [Grudge] = 맺혀가는 응어리 / Growing Resentment
   EN: [CantChangeTarget]\nPrioritizes the unit with the least HP\n[EnemyKill] Double the [Grudge] value.\n[EnemyKill] Heal HP equal to [Grudge] value
   PL:
150. [Umiejętność wroga [815409] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Grudge] 수치만큼 고정 피해.
   źródło: Skills_Abnormality-ycgd.json :: dataList[id=815409].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Grudge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Grudge] = 맺혀가는 응어리 / Growing Resentment
   EN: [OnSucceedAttack] Deal fixed damage equal to [Grudge] value.
   PL:

## [ycgd] Umiejętności wrogów / Anomalii — Skills_Enemy-ycgd
- grupa rozdziału/trybu: `ycgd` · plik: `Skills_Enemy-ycgd.json`

151. [Umiejętność wroga [9011001] (ulepszenie 1) — nazwa] 베어내기
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011001].levelList[level=1].name
   limit: do 40 znaków
   EN: Hack
   PL:
152. [Umiejętność wroga [9011001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
153. [Umiejętność wroga [9011001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Umiejętność wroga [9011002] (ulepszenie 1) — nazwa] 발경
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011002].levelList[level=1].name
   limit: do 40 znaków
   EN: Focus Strike
   PL:
155. [Umiejętność wroga [9011002] (ulepszenie 1) — opis] 대상에게 [Laceration]이 7 이상이면 코인 위력 +1\n[WinDuel] 다음 턴에 [SlashDamageUp] 1을 얻음
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WinDuel], [SlashDamageUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: If target has 7+ [Laceration], Coin Power +1\n[WinDuel] Gain 1 [SlashDamageUp] next turn
   PL:
156. [Umiejętność wroga [9011002] (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상에게 [Laceration]이 있다면, 피해량 +50%
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has [Laceration], deal +50% damage
   PL:
157. [Umiejętność wroga [9011002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
158. [Umiejętność wroga [9011003] (ulepszenie 1) — nazwa] 흩어지는 구름
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011003].levelList[level=1].name
   limit: do 40 znaków
   EN: Lenticular Scatter
   PL:
159. [Umiejętność wroga [9011003] (ulepszenie 1) — opis] 대상에게 [Laceration]이 5 이상이면 코인 위력 +1\n[WinDuel] 다음 턴에 [SlashResultUp] 1을 얻음
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011003].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WinDuel], [SlashResultUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [SlashResultUp] = 참격 위력 증가 / Slash Power Up
   EN: If target has 5+ [Laceration], Coin Power +1\n[WinDuel] Gain 1 [SlashResultUp] next turn
   PL:
160. [Umiejętność wroga [9011003] (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상에게 [Laceration]이 있다면, 피해량 +20%
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has [Laceration], deal +20% damage
   PL:
161. [Umiejętność wroga [9011003] (ulepszenie 1) — moneta 2, efekt 1 — opis] 대상에게 [Laceration]이 있다면, 피해량 +10%
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has [Laceration], deal +10% damage
   PL:
162. [Umiejętność wroga [9011003] (ulepszenie 1) — moneta 3, efekt 1 — opis] 대상에게 [Laceration]이 있다면, 피해량 +40%
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has [Laceration], deal +40% damage
   PL:
163. [Umiejętność wroga [9011004] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011004].levelList[level=1].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Umiejętność wroga [9011004] (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 [SlashDamageUp] 1 얻음 (턴 당 1회)
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [SlashDamageUp]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: [OnSucceedEvade] Gain 1 [SlashDamageUp] next turn (Once per turn)
   PL:
165. [Umiejętność wroga [9011101] (ulepszenie 1) — nazwa] 베기
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011101].levelList[level=1].name
   limit: do 40 znaków
   EN: Swipe
   PL:
166. [Umiejętność wroga [9011101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Umiejętność wroga [9011102] (ulepszenie 1) — nazwa] 가르기
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011102].levelList[level=1].name
   limit: do 40 znaków
   EN: Slice
   PL:
168. [Umiejętność wroga [9011102] (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상에게 [Laceration]이 있다면, 피해량 +30%
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has [Laceration], deal +30% damage
   PL:
169. [Umiejętność wroga [9011102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Umiejętność wroga [9011103] (ulepszenie 1) — nazwa] 날카로운 검격
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011103].levelList[level=1].name
   limit: do 40 znaków
   EN: Keen Slash
   PL:
171. [Umiejętność wroga [9011103] (ulepszenie 1) — opis] [WinDuel] 다음 턴에 [SlashDamageUp] 1을 얻음
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011103].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [SlashDamageUp]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: [WinDuel] Gain 1 [SlashDamageUp] next turn
   PL:
172. [Umiejętność wroga [9011103] (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상에게 [Laceration]이 있다면, 피해량 +10%
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Umiejętność wroga [9011103] (ulepszenie 1) — moneta 2, efekt 1 — opis] 대상에게 [Laceration]이 있다면, 피해량 +10%
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Umiejętność wroga [9011103] (ulepszenie 1) — moneta 3, efekt 1 — opis] 대상에게 [Laceration]이 있다면, 피해량 +20%
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Umiejętność wroga [9011104] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011104].levelList[level=1].name
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Umiejętność wroga [9011104] (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 [SlashDamageUp] 1을 얻음 (턴 당 1회)
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade], [SlashDamageUp]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: [OnSucceedEvade] Gain 1 [SlashDamageUp] next turn (Once per turn)
   PL:
177. [Umiejętność wroga [9011201] (ulepszenie 1) — nazwa] 내려베기
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011201].levelList[level=1].name
   limit: do 40 znaków
   EN: Downward Slash
   PL:
178. [Umiejętność wroga [9011201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Umiejętność wroga [9011201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Umiejętność wroga [9011202] (ulepszenie 1) — nazwa] 돌아베기
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011202].levelList[level=1].name
   limit: do 40 znaków
   EN: Reverse Slash
   PL:
181. [Umiejętność wroga [9011202] (ulepszenie 1) — opis] [WinDuel] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Paralysis]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Paralysis] = 마비 / Paralyze
   EN: [WinDuel] Inflict 1 [Paralysis] next turn
   PL:
182. [Umiejętność wroga [9011202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Umiejętność wroga [9011203] (ulepszenie 1) — nazwa] 발경
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011203].levelList[level=1].name
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Umiejętność wroga [9011203] (ulepszenie 1) — opis] [WinDuel] 다음 턴에 [Protection] 1 얻음
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011203].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Protection]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Protection] = 보호 / Protection
   EN: [WinDuel] Gain 1 [Protection] next turn
   PL:
185. [Umiejętność wroga [9011203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL:
186. [Umiejętność wroga [9011203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność wroga [9011204] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011204].levelList[level=1].name
   limit: do 40 znaków
   EN: Defend
   PL:
188. [Umiejętność wroga [9011204] (ulepszenie 1) — opis] [StartBattle] [Protection] 1 얻음
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Protection]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection
   EN: [StartBattle] Gain 1 [Protection]
   PL:
189. [Umiejętność wroga [9011301] (ulepszenie 1) — nazwa] 후벼베기
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011301].levelList[level=1].name
   limit: do 40 znaków
   EN: Penetrating Slash
   PL:
190. [Umiejętność wroga [9011301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Umiejętność wroga [9011301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [9011301] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011301].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność wroga [9011302] (ulepszenie 1) — nazwa] 예리한 일격
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011302].levelList[level=1].name
   limit: do 40 znaków
   EN: Keen Strike
   PL:
194. [Umiejętność wroga [9011302] (ulepszenie 1) — opis] 대상에게 [Laceration]이 7 이상이면 코인 위력 +1\n[WinDuel] 다음 턴에 [Protection] 1 얻음
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WinDuel], [Protection]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [Protection] = 보호 / Protection
   EN: If target has 7+ [Laceration], Coin Power +1\n[WinDuel] Gain 1 [Protection] next turn
   PL:
195. [Umiejętność wroga [9011302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Umiejętność wroga [9011302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Umiejętność wroga [9011303] (ulepszenie 1) — nazwa] 발경
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011303].levelList[level=1].name
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Umiejętność wroga [9011303] (ulepszenie 1) — opis] 대상에게 [Laceration]이 5 이상이면 코인 위력 +1\n[StartBattle] [Protection] 1 얻음\n[WinDuel] 다음 턴에 [Protection] 1 얻음
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011303].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [StartBattle], [Protection], [WinDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If target has 5+ [Laceration], Coin Power +1\n[StartBattle] Gain 1 [Protection]\n[WinDuel] Gain 1 [Protection] next turn
   PL:
199. [Umiejętność wroga [9011303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Umiejętność wroga [9011303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Umiejętność wroga [9011304] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011304].levelList[level=1].name
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Umiejętność wroga [9011304] (ulepszenie 1) — opis] [StartBattle] [Protection] 2 얻음
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9011304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Protection]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection
   EN: [StartBattle] Gain 2 [Protection]
   PL:
203. [Umiejętność wroga [9101301] (ulepszenie 1) — nazwa] 먹구름
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101301].levelList[level=1].name
   limit: do 40 znaków
   EN: Shadow Cloud
   PL:
204. [Umiejętność wroga [9101301] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 5 이상이면, 피해량 +10%
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has [Laceration], deal +10% damage
   PL:
205. [Umiejętność wroga [9101301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and +1 [Laceration] Count
   PL:
206. [Umiejętność wroga [9101301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Umiejętność wroga [9101302] (ulepszenie 1) — nazwa] 뒷처리
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101302].levelList[level=1].name
   limit: do 40 znaków
   EN: Clean Up
   PL:
208. [Umiejętność wroga [9101302] (ulepszenie 1) — opis] 대상의 [Laceration]이 5 이상이면 코인 위력 +1
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 5+ [Laceration], Coin Power +1
   PL:
209. [Umiejętność wroga [9101302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [SlashTakeDamageUp] 1 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttack] Inflict 1 [SlashTakeDamageUp] next turn
   PL:
210. [Umiejętność wroga [9101302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 1 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 1 [Laceration]
   PL:
211. [Umiejętność wroga [9101302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [SlashTakeDamageUp] 1 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 209 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Umiejętność wroga [9101302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 1 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 210 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Umiejętność wroga [9101303] (ulepszenie 1) — nazwa] 구름 베기
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101303].levelList[level=1].name
   limit: do 40 znaków
   EN: Lenticular Slash
   PL:
214. [Umiejętność wroga [9101303] (ulepszenie 1) — opis] 대상의 [Laceration]이 5 이상이면 코인 위력 +1
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101303].levelList[level=1].desc
   (powtórzenie elementu 208 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Umiejętność wroga [9101303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Umiejętność wroga [9101303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 8 [Laceration]
   PL:
217. [Umiejętność wroga [9101303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Umiejętność wroga [9101304] (ulepszenie 1) — nazwa] 날카로운 칼날
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101304].levelList[level=1].name
   limit: do 40 znaków
   EN: Sharp Edge
   PL:
219. [Umiejętność wroga [9101304] (ulepszenie 1) — opis] [StartBattle] 자신을 포함한 모든 아군에게 [SlashDamageUp] 2 부여\n[StartBattle] [SlashResultUp] 2 얻음
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101304].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SlashDamageUp], [SlashResultUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [SlashResultUp] = 참격 위력 증가 / Slash Power Up
   EN: [StartBattle] Apply 2 [SlashDamageUp] to all allies, including this unit\n[StartBattle] Gain 2 [SlashResultUp]
   PL:
220. [Umiejętność wroga [9101304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność wroga [9101305] (ulepszenie 1) — nazwa] 쾌청 베기
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101305].levelList[level=1].name
   limit: do 40 znaków
   EN: Sky-clearing Cut
   PL:
222. [Umiejętność wroga [9101305] (ulepszenie 1) — opis] [StartBattle] 메인 타겟의 [Laceration]이 10이상이면, 공격 가중치 +1\n[StartBattle] 이번 턴에 사용하는 공격 스킬이 5개라면, 최종 위력 +5\n[WinDuel] 모든 아군 정신력 10 회복\n대상의 [Laceration]이 7 이상이면, 피해량 +30%
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101305].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Laceration], [WinDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [StartBattle] If the main target has 10+ [Laceration], Atk Weight +1\n[StartBattle] If this unit will use 5+ Attack Skills this turn, Final Power +5\n[WinDuel] All allies heal 10 SP\nIf target has 7+ [Laceration], deal +30% damage
   PL:
223. [Umiejętność wroga [9101305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 2 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 2 [Laceration]
   PL:
224. [Umiejętność wroga [9101305] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 3 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101305].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 3 [Laceration]
   PL:
225. [Umiejętność wroga [9101305] (ulepszenie 1) — moneta 3, efekt 1 — opis] 대상의 [Laceration]이 7 이상이면, 피해량 +50%
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101305].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 7+ [Laceration], deal +50% damage
   PL:
226. [Umiejętność wroga [9101305] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 10 부여
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101305].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +10 [Laceration] Count
   PL:
227. [Umiejętność wroga [9101306] (ulepszenie 1) — nazwa] 뒷골목의 규칙
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101306].levelList[level=1].name
   limit: do 40 znaków
   EN: Rules of the Backstreets
   PL:
228. [Umiejętność wroga [9101306] (ulepszenie 1) — opis] [WhenUse] 자신 제외 살아있는 아군 수만큼 1코인 추가 (최대 3)
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101306].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Add 1 more coin per every surviving other ally (Max 3)
   PL:
229. [Umiejętność wroga [9101306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Umiejętność wroga [9101306] (ulepszenie 1) — moneta 1, efekt 2 — opis] [EnemyKill] 모든 아군 정신력 20 회복
   źródło: Skills_Enemy-ycgd.json :: dataList[id=9101306].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] All allies heal 20 SP
   PL:

## [ycgd] Pasywka wroga: Passives_Abnormality-ycgd
- plik gry: `Passives_Abnormality-ycgd.json`

231. [[ycgd] Pasywka wroga [815101] — nazwa] 죄악 저항
   źródło: Passives_Abnormality-ycgd.json :: dataList[id=815101].name
   limit: do 40 znaków
   EN: Sin Resistance
   PL:
232. [[ycgd] Pasywka wroga [815101] — opis] 흐트러짐 상태, 부위 파괴 상태가 아니라면 자신이 받는 [Combustion] 피해 50% 감소.
   źródło: Passives_Abnormality-ycgd.json :: dataList[id=815101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Unless this unit is Staggered or Part Broken, take 50% less [Combustion] damage.
   PL:
233. [[ycgd] Pasywka wroga [815201] — nazwa] 죄악 저항
   źródło: Passives_Abnormality-ycgd.json :: dataList[id=815201].name
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [[ycgd] Pasywka wroga [815201] — opis] 흐트러짐 상태, 부위 파괴 상태가 아니라면 자신이 받는 [Sinking] 피해 50% 감소.
   źródło: Passives_Abnormality-ycgd.json :: dataList[id=815201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Unless this unit is Staggered or Part Broken, take 50% less [Sinking] damage.
   PL:
235. [[ycgd] Pasywka wroga [815301] — nazwa] 한 서린 검집
   źródło: Passives_Abnormality-ycgd.json :: dataList[id=815301].name
   limit: do 40 znaków
   EN: Resentful Scabbard
   PL:
236. [[ycgd] Pasywka wroga [815301] — opis] 골단이 공격 슬롯에 있을 때, 턴 시작 시 [Grudge]를 얻음. 턴 종료 시 [Grudge]를 제거
   źródło: Passives_Abnormality-ycgd.json :: dataList[id=815301].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Grudge]
   znaczenie tagów: [Grudge] = 맺혀가는 응어리 / Growing Resentment
   EN: Gain [Grudge] at Turn Start if 'To Claim Your Bones' is in the Skill Slot. Remove [Grudge] at Turn End
   PL:
237. [[ycgd] Pasywka wroga [815402] — nazwa] 칼춤
   źródło: Passives_Abnormality-ycgd.json :: dataList[id=815402].name
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [[ycgd] Pasywka wroga [815402] — opis] 체력이 20% 남았을 때, 패턴이 변경됨.\n체력이 20% 이하가 될 때, 다음 턴부터 매 턴마다 [Grudge]를 20 얻음. [Grudge]가 제거되지 않음
   źródło: Passives_Abnormality-ycgd.json :: dataList[id=815402].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Grudge]
   znaczenie tagów: [Grudge] = 맺혀가는 응어리 / Growing Resentment
   EN: At 20% HP, gains a new pattern.\nAt 20%- HP, starting next turn, gain 20 [Grudge] every turn. [Grudge] no longer expires
   PL:
239. [[ycgd] Pasywka wroga [815403] — nazwa] 맺혀가는 응어리
   źródło: Passives_Abnormality-ycgd.json :: dataList[id=815403].name
   limit: do 40 znaków
   EN: Growing Resentment
   PL:
240. [[ycgd] Pasywka wroga [815403] — opis] 침잠 피해를 받을 경우, 다음 턴에 방어 레벨 감소 1 얻음. (턴 당 5회)
   źródło: Passives_Abnormality-ycgd.json :: dataList[id=815403].desc
   limit: do 120 znaków
   EN: When taking Sinking damage, gain 1 Defense Level Down next turn. (5 times per turn)
   PL:
