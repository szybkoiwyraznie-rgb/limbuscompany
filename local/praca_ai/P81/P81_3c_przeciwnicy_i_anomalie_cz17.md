# Paczka AI P81 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 17/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P81_3c_przeciwnicy_i_anomalie_cz17.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P81_3c_przeciwnicy_i_anomalie_cz17.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [podstawowe] Umiejętności wrogów / Anomalii — Skills_Enemy
- grupa rozdziału/trybu: `podstawowe` · plik: `Skills_Enemy.json`

1. [Umiejętność wroga [9007003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 가지고 있는 충전 횟수가 5 이상이면, 충전 횟수만큼 가하는 피해량 +10%. 전부 소모.
   źródło: Skills_Enemy.json :: dataList[id=9007003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 5+ Charge Count, spend all Charge Count to deal +10% damage for each Count
   PL:
2. [Umiejętność wroga [9007003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 맞물리는 시간 1 부여
   źródło: Skills_Enemy.json :: dataList[id=9007003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Interlocking Time
   PL:
3. [Umiejętność wroga [9007004] (ulepszenie 1) — nazwa] 시간 대여
   źródło: Skills_Enemy.json :: dataList[id=9007004].levelList[level=1].name
   limit: do 40 znaków
   EN: Borrow Time
   PL:
4. [Umiejętność wroga [9007004] (ulepszenie 1) — opis] [StartBattle] [TimeRental] 3 얻음. 자신의 충전 횟수 1 얻음
   źródło: Skills_Enemy.json :: dataList[id=9007004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [TimeRental]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [TimeRental] = 심상 속 시간 대여 / Borrowed Time of the Fathoms
   EN: [StartBattle] Gain 3 [TimeRental] and +1 Charge Count
   PL:
5. [Umiejętność wroga [9007101] (ulepszenie 1) — nazwa] 근접 촬영 시작
   źródło: Skills_Enemy.json :: dataList[id=9007101].levelList[level=1].name
   limit: do 40 znaków
   EN: Proximity Shooting
   PL:
6. [Umiejętność wroga [9007102] (ulepszenie 1) — nazwa] 후퇴 후퇴
   źródło: Skills_Enemy.json :: dataList[id=9007102].levelList[level=1].name
   limit: do 40 znaków
   EN: Retreat; Retreat;
   PL:
7. [Umiejętność wroga [9007103] (ulepszenie 1) — nazwa] 섬광 섬광
   źródło: Skills_Enemy.json :: dataList[id=9007103].levelList[level=1].name
   limit: do 40 znaków
   EN: Flash; Flash;
   PL:
8. [Umiejętność wroga [9007103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력 -5
   źródło: Skills_Enemy.json :: dataList[id=9007103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 5 SP
   PL:
9. [Umiejętność wroga [9007103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 대상의 정신력 -5
   źródło: Skills_Enemy.json :: dataList[id=9007103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Target loses 5 SP
   PL:
10. [Umiejętność wroga [9007104] (ulepszenie 1) — nazwa] 구속합니다.
   źródło: Skills_Enemy.json :: dataList[id=9007104].levelList[level=1].name
   limit: do 40 znaków
   EN: Arresting.
   PL:
11. [Umiejętność wroga [9007104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2, 마비 3 부여.
   źródło: Skills_Enemy.json :: dataList[id=9007104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind and 3 Paralyze next turn.
   PL:
12. [Umiejętność wroga [9008201] (ulepszenie 1) — nazwa] 거수자 발견
   źródło: Skills_Enemy.json :: dataList[id=9008201].levelList[level=1].name
   limit: do 40 znaków
   EN: Suspicious Individuals
   PL:
13. [Umiejętność wroga [9008201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9008201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Rupture
   PL:
14. [Umiejętność wroga [9008202] (ulepszenie 1) — nazwa] 제압
   źródło: Skills_Enemy.json :: dataList[id=9008202].levelList[level=1].name
   limit: do 40 znaków
   EN: Restrain
   PL:
15. [Umiejętność wroga [9008202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Enemy.json :: dataList[id=9008202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
16. [Umiejętność wroga [9008203] (ulepszenie 1) — nazwa] 거수자 차단
   źródło: Skills_Enemy.json :: dataList[id=9008203].levelList[level=1].name
   limit: do 40 znaków
   EN: No Trespassing
   PL:
17. [Umiejętność wroga [9008203] (ulepszenie 1) — opis] 체력이 가장 높은 대상 우선 공격
   źródło: Skills_Enemy.json :: dataList[id=9008203].levelList[level=1].desc
   limit: do 120 znaków
   EN: Targets the unit with the most HP
   PL:
18. [Umiejętność wroga [9008203] (ulepszenie 1) — moneta 2, efekt 1 — opis] 1코인이 앞면이라면 피해량 +10%
   źródło: Skills_Enemy.json :: dataList[id=9008203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   EN: If Coin 1 lands Heads, +10% Damage
   PL:
19. [Umiejętność wroga [9008203] (ulepszenie 1) — moneta 3, efekt 1 — opis] 2코인이 앞면이라면 피해량 +10%
   źródło: Skills_Enemy.json :: dataList[id=9008203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: If Coin 2 lands Heads, +10% Damage
   PL:
20. [Umiejętność wroga [9008203] (ulepszenie 1) — moneta 4, efekt 1 — opis] 2, 3코인이 앞면이라면 피해량 +30%
   źródło: Skills_Enemy.json :: dataList[id=9008203].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: If Coins 2 & 3 land Heads, +30% Damage
   PL:

## [podstawowe] Umiejętności wrogów / Anomalii — Skills_Enemy91-4
- grupa rozdziału/trybu: `podstawowe` · plik: `Skills_Enemy91-4.json`

21. [Umiejętność wroga [9007701] (ulepszenie 1) — nazwa] 꾸악
   źródło: Skills_Enemy91-4.json :: dataList[id=9007701].levelList[level=1].name
   limit: do 40 znaków
   EN: Gwah
   PL:
22. [Umiejętność wroga [9007701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
23. [Umiejętność wroga [9007701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
24. [Umiejętność wroga [9007702] (ulepszenie 1) — nazwa] 등딱지 태클!
   źródło: Skills_Enemy91-4.json :: dataList[id=9007702].levelList[level=1].name
   limit: do 40 znaków
   EN: Shell Tackle!
   PL:
25. [Umiejętność wroga [9007702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 횟수 2 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9007702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Rupture Count next turn
   PL:
26. [Umiejętność wroga [9007702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 참격 취약 1 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Slash Fragility next turn
   PL:
27. [Umiejętność wroga [9007703] (ulepszenie 1) — nazwa] 꾸아악!
   źródło: Skills_Enemy91-4.json :: dataList[id=9007703].levelList[level=1].name
   limit: do 40 znaków
   EN: Gwaaah!
   PL:
28. [Umiejętność wroga [9007703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture
   PL:
29. [Umiejętność wroga [9007703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
30. [Umiejętność wroga [9007703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
31. [Umiejętność wroga [9007704] (ulepszenie 1) — nazwa] 게거품
   źródło: Skills_Enemy91-4.json :: dataList[id=9007704].levelList[level=1].name
   limit: do 40 znaków
   EN: Foaming
   PL:
32. [Umiejętność wroga [9007704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 5 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9007704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +5 Rupture Count
   PL:
33. [Umiejętność wroga [9007705] (ulepszenie 1) — nazwa] 게 눈 감추기
   źródło: Skills_Enemy91-4.json :: dataList[id=9007705].levelList[level=1].name
   limit: do 40 znaków
   EN: Hermit Crab
   PL:
34. [Umiejętność wroga [9007705] (ulepszenie 1) — opis] [StartBattle] 이번 턴동안 보호막 체력이 있는 상태에서 피격 시 참격 피해 4 반사
   źródło: Skills_Enemy91-4.json :: dataList[id=9007705].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] When attacked while this unit has Shield HP, deal 4 Slash damage to the attacker
   PL:
35. [Umiejętność wroga [9007801] (ulepszenie 1) — nazwa] 꾸악
   źródło: Skills_Enemy91-4.json :: dataList[id=9007801].levelList[level=1].name
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
36. [Umiejętność wroga [9007801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
37. [Umiejętność wroga [9007801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Umiejętność wroga [9007802] (ulepszenie 1) — nazwa] 등딱지 태클!
   źródło: Skills_Enemy91-4.json :: dataList[id=9007802].levelList[level=1].name
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
39. [Umiejętność wroga [9007802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 횟수 2 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9007802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
40. [Umiejętność wroga [9007802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 관통 취약 1 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Pierce Fragility next turn
   PL:
41. [Umiejętność wroga [9007803] (ulepszenie 1) — nazwa] 꾸아악!
   źródło: Skills_Enemy91-4.json :: dataList[id=9007803].levelList[level=1].name
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
42. [Umiejętność wroga [9007803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Umiejętność wroga [9007803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Umiejętność wroga [9007803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Umiejętność wroga [9007804] (ulepszenie 1) — nazwa] 게거품
   źródło: Skills_Enemy91-4.json :: dataList[id=9007804].levelList[level=1].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
46. [Umiejętność wroga [9007804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 5 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9007804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Umiejętność wroga [9007805] (ulepszenie 1) — nazwa] 게 눈 감추기
   źródło: Skills_Enemy91-4.json :: dataList[id=9007805].levelList[level=1].name
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [Umiejętność wroga [9007805] (ulepszenie 1) — opis] [StartBattle] 이번 턴동안 보호막 체력이 있는 상태에서 피격 시 관통 피해 4 반사
   źródło: Skills_Enemy91-4.json :: dataList[id=9007805].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] When attacked while this unit has Shield HP, deal 4 Pierce damage to the attacker
   PL:
49. [Umiejętność wroga [9007901] (ulepszenie 1) — nazwa] 꾸악
   źródło: Skills_Enemy91-4.json :: dataList[id=9007901].levelList[level=1].name
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
50. [Umiejętność wroga [9007901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Umiejętność wroga [9007901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Umiejętność wroga [9007902] (ulepszenie 1) — nazwa] 등딱지 태클!
   źródło: Skills_Enemy91-4.json :: dataList[id=9007902].levelList[level=1].name
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [Umiejętność wroga [9007902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 파열 횟수 2 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9007902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
54. [Umiejętność wroga [9007902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 타격 취약 1 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Blunt Fragility next turn
   PL:
55. [Umiejętność wroga [9007903] (ulepszenie 1) — nazwa] 꾸아악!
   źródło: Skills_Enemy91-4.json :: dataList[id=9007903].levelList[level=1].name
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Umiejętność wroga [9007903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Umiejętność wroga [9007903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [Umiejętność wroga [9007903] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9007903].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Umiejętność wroga [9007904] (ulepszenie 1) — nazwa] 게거품
   źródło: Skills_Enemy91-4.json :: dataList[id=9007904].levelList[level=1].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [Umiejętność wroga [9007904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 5 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9007904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Umiejętność wroga [9007905] (ulepszenie 1) — nazwa] 게 눈 감추기
   źródło: Skills_Enemy91-4.json :: dataList[id=9007905].levelList[level=1].name
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [Umiejętność wroga [9007905] (ulepszenie 1) — opis] [StartBattle] 이번 턴동안 보호막 체력이 있는 상태에서 피격 시 타격 피해 4 반사
   źródło: Skills_Enemy91-4.json :: dataList[id=9007905].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] When attacked while this unit has Shield HP, deal 4 Blunt damage to the attacker
   PL:
63. [Umiejętność wroga [9008001] (ulepszenie 1) — nazwa] 찍기
   źródło: Skills_Enemy91-4.json :: dataList[id=9008001].levelList[level=1].name
   limit: do 40 znaków
   EN: Thwack
   PL:
64. [Umiejętność wroga [9008001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9008001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Rupture
   PL:
65. [Umiejętność wroga [9008002] (ulepszenie 1) — nazwa] 마구 찍기
   źródło: Skills_Enemy91-4.json :: dataList[id=9008002].levelList[level=1].name
   limit: do 40 znaków
   EN: Thwack Thwack Thwack
   PL:
66. [Umiejętność wroga [9008002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9008002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Rupture Count
   PL:
67. [Umiejętność wroga [9008002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9008002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [Umiejętność wroga [9008002] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9008002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [Umiejętność wroga [9008003] (ulepszenie 1) — nazwa] 게거품
   źródło: Skills_Enemy91-4.json :: dataList[id=9008003].levelList[level=1].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Umiejętność wroga [9008003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 5 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9008003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
71. [Umiejętność wroga [9008003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 5 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9008003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Umiejętność wroga [9008004] (ulepszenie 1) — nazwa] 게장 발사!
   źródło: Skills_Enemy91-4.json :: dataList[id=9008004].levelList[level=1].name
   limit: do 40 znaków
   EN: Delicious Crab Guts!
   PL:
73. [Umiejętność wroga [9008004] (ulepszenie 1) — opis] [CantIdentify]\n대상의 파열 위력 5 마다 피해량 +15%\n[EndSkill] 최대 체력의 8%만큼 본체 체력 감소
   źródło: Skills_Enemy91-4.json :: dataList[id=9008004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify] \nDeal +15% damage per 5 Rupture on target\n[EndSkill] Lose HP by 8% of Max HP
   PL:
74. [Umiejętność wroga [9008004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 10 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9008004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 10 Rupture
   PL:
75. [Umiejętność wroga [9008005] (ulepszenie 1) — nazwa] 꾸오!
   źródło: Skills_Enemy91-4.json :: dataList[id=9008005].levelList[level=1].name
   limit: do 40 znaków
   EN: GUOH!
   PL:
76. [Umiejętność wroga [9008005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9008005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL:
77. [Umiejętność wroga [9008005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9008005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [Umiejętność wroga [9008005] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9008005].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Umiejętność wroga [9008101] (ulepszenie 1) — nazwa] 찍기
   źródło: Skills_Enemy91-4.json :: dataList[id=9008101].levelList[level=1].name
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [Umiejętność wroga [9008101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9008101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Umiejętność wroga [9008102] (ulepszenie 1) — nazwa] 마구 찍기
   źródło: Skills_Enemy91-4.json :: dataList[id=9008102].levelList[level=1].name
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Umiejętność wroga [9008102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9008102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność wroga [9008102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9008102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Umiejętność wroga [9008102] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9008102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Umiejętność wroga [9008103] (ulepszenie 1) — nazwa] 게거품
   źródło: Skills_Enemy91-4.json :: dataList[id=9008103].levelList[level=1].name
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Umiejętność wroga [9008103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 5 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9008103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność wroga [9008103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 5 증가
   źródło: Skills_Enemy91-4.json :: dataList[id=9008103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Umiejętność wroga [9008104] (ulepszenie 1) — nazwa] 등딱지 태클!!!
   źródło: Skills_Enemy91-4.json :: dataList[id=9008104].levelList[level=1].name
   limit: do 40 znaków
   EN: Shell Tackle!!!
   PL:
89. [Umiejętność wroga [9008104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 관통 취약 3 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9008104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Pierce Fragility next turn
   PL:
90. [Umiejętność wroga [9008105] (ulepszenie 1) — nazwa] 오래된 게딱지 탄 발사
   źródło: Skills_Enemy91-4.json :: dataList[id=9008105].levelList[level=1].name
   limit: do 40 znaków
   EN: Firing Molted Shell Shot
   PL:
91. [Umiejętność wroga [9008105] (ulepszenie 1) — opis] [CantIdentify]\n대상의 파열 위력 5마다 피해량 +15%
   źródło: Skills_Enemy91-4.json :: dataList[id=9008105].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: [CantIdentify]\nDeal +15% damage per 5 Rupture on target
   PL:
92. [Umiejętność wroga [9008105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 오래된 게딱지 탄 1 소모
   źródło: Skills_Enemy91-4.json :: dataList[id=9008105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 1 Molted Shell Shot
   PL:
93. [Umiejętność wroga [9008106] (ulepszenie 1) — nazwa] 꾸오!
   źródło: Skills_Enemy91-4.json :: dataList[id=9008106].levelList[level=1].name
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Umiejętność wroga [9008106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9008106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Umiejętność wroga [9008106] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9008106].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Umiejętność wroga [9008106] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills_Enemy91-4.json :: dataList[id=9008106].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [podstawowe] Umiejętności wrogów / Anomalii — Skills_Enemy_Mirror7-extreme
- grupa rozdziału/trybu: `podstawowe` · plik: `Skills_Enemy_Mirror7-extreme.json`

97. [Umiejętność wroga [7104701] (ulepszenie 1) — nazwa] 돌격
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104701].levelList[level=1].name
   limit: do 40 znaków
   EN: Raid
   PL:
98. [Umiejętność wroga [7104701] (ulepszenie 1) — opis] [WhenUse] 대상의 [Vibration]이 3 이상이면, 코인 위력 +1
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 3+ [Vibration], Coin Power +1
   PL:
99. [Umiejętność wroga [7104701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
100. [Umiejętność wroga [7104701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Umiejętność wroga [7104701] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104701].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [Umiejętność wroga [7104702] (ulepszenie 1) — nazwa] 표적 무력화
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104702].levelList[level=1].name
   limit: do 40 znaków
   EN: Neutralize Target
   PL:
103. [Umiejętność wroga [7104702] (ulepszenie 1) — opis] [WhenUse] 대상의 [Vibration]이 3 이상이면, 코인 위력 +1
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104702].levelList[level=1].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Umiejętność wroga [7104702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL:
105. [Umiejętność wroga [7104702] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
106. [Umiejętność wroga [7104703] (ulepszenie 1) — nazwa] HP탄 활성화
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104703].levelList[level=1].name
   limit: do 40 znaków
   EN: Activate HP Bullet
   PL:
107. [Umiejętność wroga [7104703] (ulepszenie 1) — opis] [WhenUse] 체력 20 회복
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104703].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 20 HP
   PL:
108. [Umiejętność wroga [7104704] (ulepszenie 1) — nazwa] 진압
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104704].levelList[level=1].name
   limit: do 40 znaków
   EN: Takedown
   PL:
109. [Umiejętność wroga [7104704] (ulepszenie 1) — opis] [WhenUse] 대상의 [Vibration]이 4 이상이면, 기본 위력 +2
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 4+ [Vibration], Base Power +2
   PL:
110. [Umiejętność wroga [7104704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
111. [Umiejętność wroga [7104801] (ulepszenie 1) — nazwa] HP탄 활성화
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104801].levelList[level=1].name
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [Umiejętność wroga [7104801] (ulepszenie 1) — opis] [WhenUse] 체력 20 회복
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104801].levelList[level=1].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Umiejętność wroga [7104802] (ulepszenie 1) — nazwa] 방호
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104802].levelList[level=1].name
   limit: do 40 znaków
   EN: Shelter
   PL:
114. [Umiejętność wroga [7104802] (ulepszenie 1) — opis] [WinDuel] 무작위 아군 2명에게 다음 턴에 [ResultEnhancement] 1 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [ResultEnhancement]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [ResultEnhancement] = 위력 증가 / Power Up
   EN: [WinDuel] Apply 1 [ResultEnhancement] to 2 random allies next turn
   PL:
115. [Umiejętność wroga [7104803] (ulepszenie 1) — nazwa] 엄호
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104803].levelList[level=1].name
   limit: do 40 znaków
   EN: Cover
   PL:
116. [Umiejętność wroga [7104803] (ulepszenie 1) — opis] [WhenUse] 자신을 제외한 무작위 아군 2명에게 다음 턴에 [Protection] 2 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104803].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Protection]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection
   EN: [WhenUse] Apply 2 [Protection] to 2 random other allies next turn
   PL:
117. [Umiejętność wroga [7104803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable]
   PL:
118. [Umiejętność wroga [7104901] (ulepszenie 1) — nazwa] 출입 금지
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104901].levelList[level=1].name
   limit: do 40 znaków
   EN: Do Not Enter
   PL:
119. [Umiejętność wroga [7104901] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 4 이상이면, 기본 위력 +2
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 4+ [Burst], Base Power +2
   PL:
120. [Umiejętność wroga [7104901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]
   PL:
121. [Umiejętność wroga [7104902] (ulepszenie 1) — nazwa] 진압
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104902].levelList[level=1].name
   limit: do 40 znaków
   EN: Subdue
   PL:
122. [Umiejętność wroga [7104902] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 3당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Coin Power +1 for every 3 [Burst] on target (max 2)
   PL:
123. [Umiejętność wroga [7104902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL:
124. [Umiejętność wroga [7104902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL:
125. [Umiejętność wroga [7104903] (ulepszenie 1) — nazwa] 출입 차단
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104903].levelList[level=1].name
   limit: do 40 znaków
   EN: Forbid Entry
   PL:
126. [Umiejętność wroga [7104903] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 3당, 코인 위력 +1 (최대 2)\n[DefeatDuel] 체력 10 회복
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104903].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Coin Power +1 for every 3 [Burst] on target (max 2)\n[DefeatDuel] Heal 10 HP
   PL:
127. [Umiejętność wroga [7104903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL:
128. [Umiejętność wroga [7104903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] x [Burst] 횟수만큼 체력 피해. 대상의 [Burst] 전부 소모
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7104903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Deal ([Burst] x [Burst] Count) HP damage, then consume all [Burst] on target
   PL:
129. [Umiejętność wroga [7105001] (ulepszenie 1) — nazwa] 거수자 발견
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105001].levelList[level=1].name
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Umiejętność wroga [7105001] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 3 이상이면, 기본 위력 +2
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 3+ [Burst], Base Power +2
   PL:
131. [Umiejętność wroga [7105001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Umiejętność wroga [7105002] (ulepszenie 1) — nazwa] 제압
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105002].levelList[level=1].name
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Umiejętność wroga [7105002] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 3 이상이면, 기본 위력 +2
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105002].levelList[level=1].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Umiejętność wroga [7105002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Umiejętność wroga [7105002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Umiejętność wroga [7105003] (ulepszenie 1) — nazwa] 거수자 차단
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105003].levelList[level=1].name
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Umiejętność wroga [7105003] (ulepszenie 1) — opis] [Burst]이 가장 많은 대상 우선 공격\n[WhenUse] 대상에게 [Burst]이 있다면, 코인 위력 +1
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105003].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: Prioritizes targets that have the most [Burst]\n[WhenUse] If target has [Burst], Coin Power +1
   PL:
138. [Umiejętność wroga [7105003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Umiejętność wroga [7105003] (ulepszenie 1) — moneta 2, efekt 1 — opis] 1코인이 앞면이면 피해량 +10%
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   EN: If Coin 1 lands Heads, deal +10% damage
   PL:
140. [Umiejętność wroga [7105003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
141. [Umiejętność wroga [7105003] (ulepszenie 1) — moneta 3, efekt 1 — opis] 2코인이 앞면이면 피해량 +10%
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: If Coin 2 lands Heads, deal +10% damage
   PL:
142. [Umiejętność wroga [7105003] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105003].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność wroga [7105003] (ulepszenie 1) — moneta 4, efekt 1 — opis] 2, 3코인이 앞면이면 피해량 +30%
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105003].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: If Coins 2 & 3 land Heads, deal +30% damage
   PL:
144. [Umiejętność wroga [7105003] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Burst] x [Burst] 횟수만큼 체력 피해. 대상의 [Burst] 전부 소모
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105003].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Umiejętność wroga [7105101] (ulepszenie 1) — nazwa] 기이
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105101].levelList[level=1].name
   limit: do 40 znaków
   EN: Kii
   PL:
146. [Umiejętność wroga [7105101] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Clash Power +2 for every type of negative effect on target (max 6)
   PL:
147. [Umiejętność wroga [7105101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 5 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +5 [Burst] Count
   PL:
148. [Umiejętność wroga [7105102] (ulepszenie 1) — nazwa] 기이익
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105102].levelList[level=1].name
   limit: do 40 znaków
   EN: Kiih
   PL:
149. [Umiejętność wroga [7105102] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105102].levelList[level=1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Umiejętność wroga [7105102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Umiejętność wroga [7105102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Umiejętność wroga [7105103] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105103].levelList[level=1].name
   limit: do 40 znaków
   EN: Guard
   PL:
153. [Umiejętność wroga [7105103] (ulepszenie 1) — opis] [StartBattle] 이번 턴 동안 (자신의 잃은 체력 / 10) 만큼 보호막 얻음
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105103].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] For this turn, gain (missing HP on self / 10) Shield
   PL:
154. [Umiejętność wroga [7105201] (ulepszenie 1) — nazwa] 기이익
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105201].levelList[level=1].name
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Umiejętność wroga [7105201] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105201].levelList[level=1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Umiejętność wroga [7105201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 6 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 6 [Burst]
   PL:
157. [Umiejętność wroga [7105202] (ulepszenie 1) — nazwa] 기이이익
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105202].levelList[level=1].name
   limit: do 40 znaków
   EN: Kiieeh
   PL:
158. [Umiejętność wroga [7105202] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105202].levelList[level=1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Umiejętność wroga [7105202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Umiejętność wroga [7105202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Umiejętność wroga [7105203] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105203].levelList[level=1].name
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [Umiejętność wroga [7105203] (ulepszenie 1) — opis] [StartBattle] 이번 턴 동안 (자신의 잃은 체력 / 10) 만큼 보호막 얻음
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105203].levelList[level=1].desc
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Umiejętność wroga [7105301] (ulepszenie 1) — nazwa] 기긱!
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105301].levelList[level=1].name
   limit: do 40 znaków
   EN: Kigik!
   PL:
164. [Umiejętność wroga [7105301] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105301].levelList[level=1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Umiejętność wroga [7105301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL:
166. [Umiejętność wroga [7105302] (ulepszenie 1) — nazwa] 기익!
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105302].levelList[level=1].name
   limit: do 40 znaków
   EN: Kieek!
   PL:
167. [Umiejętność wroga [7105302] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105302].levelList[level=1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Umiejętność wroga [7105302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL:
169. [Umiejętność wroga [7105302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 2 부여, [Laceration] 횟수 5 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown] and +5 [Laceration] Count
   PL:
170. [Umiejętność wroga [7105303] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105303].levelList[level=1].name
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Umiejętność wroga [7105303] (ulepszenie 1) — opis] [StartBattle] 이번 턴 동안 (자신의 잃은 체력 / 10) 만큼 보호막 얻음
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105303].levelList[level=1].desc
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Umiejętność wroga [7105401] (ulepszenie 1) — nazwa] 기긱이긱
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105401].levelList[level=1].name
   limit: do 40 znaków
   EN: Kigigiik
   PL:
173. [Umiejętność wroga [7105401] (ulepszenie 1) — opis] 이전 턴에 피해를 받지 않은 경우 코인 위력 +1\n[WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105401].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: If this unit did not take damage in the previous turn, Coin Power +1\n[WhenUse] Clash Power +2 for every type of negative effect on target (max 6)
   PL:
174. [Umiejętność wroga [7105401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]
   PL:
175. [Umiejętność wroga [7105401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL:
176. [Umiejętność wroga [7105402] (ulepszenie 1) — nazwa] 기긱이긱
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105402].levelList[level=1].name
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Umiejętność wroga [7105402] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105402].levelList[level=1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Umiejętność wroga [7105402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Umiejętność wroga [7105402] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1, [DefenseDown] 2 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [Binding] and 2 [DefenseDown] next turn
   PL:
180. [Umiejętność wroga [7105403] (ulepszenie 1) — nazwa] 기이긱기
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105403].levelList[level=1].name
   limit: do 40 znaków
   EN: Kieegikhik
   PL:
181. [Umiejętność wroga [7105403] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)\n[WhenUse] [Protection] 2 얻음\n[WinDuel] [Vibration] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105403].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Protection], [WinDuel], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection; [WinDuel] = [합 승리시] / [Clash Win]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Clash Power +2 for every type of negative effect on target (max 6)\n[WhenUse] Gain 2 [Protection]\n[WinDuel] Inflict 5 [Vibration]
   PL:
182. [Umiejętność wroga [7105403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
183. [Umiejętność wroga [7105403] (ulepszenie 1) — moneta 1, efekt 2 — opis] - [VibrationExplosion]이 적중했으면, [Laceration], [Vibration], [Burst] 위력 중 무작위로 10 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion], [Laceration], [Vibration], [Burst]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture
   EN: - If [VibrationExplosion] is triggered, inflict 10 Potency of a random status effect, chosen from [Laceration], [Vibration], and [Burst]
   PL:
184. [Umiejętność wroga [7105404] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105404].levelList[level=1].name
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Umiejętność wroga [7105404] (ulepszenie 1) — opis] [StartBattle] 이번 턴 동안 (자신의 잃은 체력 / 10) 만큼 보호막 얻음
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105404].levelList[level=1].desc
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Umiejętność wroga [7105501] (ulepszenie 1) — nazwa] 돌격
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105501].levelList[level=1].name
   (powtórzenie elementu 97 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność wroga [7105501] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105501].levelList[level=1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Umiejętność wroga [7105501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL:
189. [Umiejętność wroga [7105501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL:
190. [Umiejętność wroga [7105501] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105501].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Umiejętność wroga [7105502] (ulepszenie 1) — nazwa] 표적 무력화
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105502].levelList[level=1].name
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [7105502] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105502].levelList[level=1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność wroga [7105502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Umiejętność wroga [7105502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 189 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Umiejętność wroga [7105502] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]이 10 이상이면, [Sinking] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target has 10+ [Sinking], inflict 5 [Sinking] next turn
   PL:
196. [Umiejętność wroga [7105503] (ulepszenie 1) — nazwa] HP탄 활성화
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105503].levelList[level=1].name
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Umiejętność wroga [7105503] (ulepszenie 1) — opis] [WhenUse] 잃은 체력의 5%만큼 회복 (최대 150, 턴당 1회)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 5% of missing HP (once per turn; max 150)
   PL:
198. [Umiejętność wroga [7105601] (ulepszenie 1) — nazwa] 방호
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105601].levelList[level=1].name
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Umiejętność wroga [7105601] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)\n[WhenUse] 무작위 아군 2명에게 다음 턴에 [Protection] 2 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105601].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Protection]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection
   EN: [WhenUse] Clash Power +2 for every type of negative effect on target (max 6)\n[WhenUse] Apply 2 [Protection] to 2 random allies next turn
   PL:
200. [Umiejętność wroga [7105601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 5 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +5 [Sinking] Count
   PL:
201. [Umiejętność wroga [7105602] (ulepszenie 1) — nazwa] 저지
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105602].levelList[level=1].name
   limit: do 40 znaków
   EN: Blockade
   PL:
202. [Umiejętność wroga [7105602] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105602].levelList[level=1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Umiejętność wroga [7105602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Umiejętność wroga [7105602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Umiejętność wroga [7105603] (ulepszenie 1) — nazwa] 엄호
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105603].levelList[level=1].name
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Umiejętność wroga [7105603] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)\n[WinDuel] 자신을 제외한 무작위 아군 1명에게 다음 턴에 [AmberDamageUp] 1, [ShamrockDamageUp] 1 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105603].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WinDuel], [AmberDamageUp], [ShamrockDamageUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [AmberDamageUp] = 나태 피해량 증가 / Sloth DMG Up; [ShamrockDamageUp] = 탐식 피해량 증가 / Gluttony DMG Up
   EN: [WhenUse] Clash Power +2 for every type of negative effect on target (max 6)\n[WinDuel] Apply 1 [AmberDamageUp] and 1 [ShamrockDamageUp] to a random other ally next turn
   PL:
207. [Umiejętność wroga [7105603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking]
   PL:
208. [Umiejętność wroga [7105701] (ulepszenie 1) — nazwa] 출입 금지
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105701].levelList[level=1].name
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Umiejętność wroga [7105701] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105701].levelList[level=1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Umiejętność wroga [7105701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Umiejętność wroga [7105702] (ulepszenie 1) — nazwa] 진압
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105702].levelList[level=1].name
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Umiejętność wroga [7105702] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105702].levelList[level=1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Umiejętność wroga [7105702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Umiejętność wroga [7105702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 5 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Umiejętność wroga [7105703] (ulepszenie 1) — nazwa] 출입 차단
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105703].levelList[level=1].name
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Umiejętność wroga [7105703] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)\n[DefeatDuel] 잃은 체력의 5%만큼 회복 (최대 100, 턴당 1회)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105703].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Clash Power +2 for every type of negative effect on target (max 6)\n[DefeatDuel] Heal 5% of missing HP (once per turn; max 100)
   PL:
217. [Umiejętność wroga [7105703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 5 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Umiejętność wroga [7105703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking] 위력만큼 우울 피해. 대상의 [Sinking] 횟수 1 감소
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Deal Gloom damage equal to [Sinking] Potency on target and reduce target's [Sinking] Count by 1
   PL:
219. [Umiejętność wroga [7105801] (ulepszenie 1) — nazwa] 거수자 발견
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105801].levelList[level=1].name
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność wroga [7105801] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105801].levelList[level=1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność wroga [7105801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 5 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Umiejętność wroga [7105802] (ulepszenie 1) — nazwa] 제압
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105802].levelList[level=1].name
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Umiejętność wroga [7105802] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105802].levelList[level=1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [Umiejętność wroga [7105802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 5 증가
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Umiejętność wroga [7105802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność wroga [7105803] (ulepszenie 1) — nazwa] 거수자 차단
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105803].levelList[level=1].name
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność wroga [7105803] (ulepszenie 1) — opis] [Sinking]이 가장 많은 대상 우선 공격\n[WhenUse] 대상에게 [Sinking]이 있다면, 기본 위력 +2\n[WhenUse] 대상의 부정적인 효과 종류 당 합 위력 +2 (최대 6)\n[DefeatDuel] 잃은 체력의 5%만큼 회복 (최대 100, 턴당 1회)
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105803].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [WhenUse], [DefeatDuel]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Targets the unit that has the most [Sinking]\n[WhenUse] If target has [Sinking], Base Power +2\n[WhenUse] Clash Power +2 for every type of negative effect on target (max 6)\n[DefeatDuel] Heal 5% of missing HP (once per turn; max 100)
   PL:
228. [Umiejętność wroga [7105803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Umiejętność wroga [7105803] (ulepszenie 1) — moneta 2, efekt 1 — opis] 1코인이 앞면이면 피해량 +10%
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 139 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Umiejętność wroga [7105803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Umiejętność wroga [7105803] (ulepszenie 1) — moneta 3, efekt 1 — opis] 2코인이 앞면이면 피해량 +10%
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Umiejętność wroga [7105803] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105803].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Umiejętność wroga [7105803] (ulepszenie 1) — moneta 4, efekt 1 — opis] 2, 3코인이 앞면이면 피해량 +30%
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105803].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Umiejętność wroga [7105803] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Sinking] 위력 x [Sinking] 횟수만큼 우울 피해. 대상의 [Sinking] 횟수 1 감소
   źródło: Skills_Enemy_Mirror7-extreme.json :: dataList[id=7105803].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Deal Gloom damage equal to ([Sinking] Potency x [Sinking] Count) on target and reduce target's [Sinking] Count by 1
   PL:

## [podstawowe] Umiejętności wrogów / Anomalii — Skills_Tutorial
- grupa rozdziału/trybu: `podstawowe` · plik: `Skills_Tutorial.json`

235. [Umiejętność wroga [9900401] (ulepszenie 1) — nazwa] 싱거운 타격
   źródło: Skills_Tutorial.json :: dataList[id=9900401].levelList[level=1].name
   limit: do 40 znaków
   EN: Weak Blow
   PL:
236. [Umiejętność wroga [9900501] (ulepszenie 1) — nazwa] 어설픈 베기
   źródło: Skills_Tutorial.json :: dataList[id=9900501].levelList[level=1].name
   limit: do 40 znaków
   EN: Clumsy Chop
   PL:
237. [Umiejętność wroga [9900601] (ulepszenie 1) — nazwa] 서투른 찌르기
   źródło: Skills_Tutorial.json :: dataList[id=9900601].levelList[level=1].name
   limit: do 40 znaków
   EN: Clunky Stab
   PL:
238. [Umiejętność wroga [9900701] (ulepszenie 1) — nazwa] 어설픈 베기
   źródło: Skills_Tutorial.json :: dataList[id=9900701].levelList[level=1].name
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [Umiejętność wroga [9900801] (ulepszenie 1) — nazwa] 서투른 찌르기
   źródło: Skills_Tutorial.json :: dataList[id=9900801].levelList[level=1].name
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Umiejętność wroga [9900901] (ulepszenie 1) — nazwa] 싱거운 타격
   źródło: Skills_Tutorial.json :: dataList[id=9900901].levelList[level=1].name
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
241. [Umiejętność wroga [9901001] (ulepszenie 1) — nazwa] 어설픈 베기
   źródło: Skills_Tutorial.json :: dataList[id=9901001].levelList[level=1].name
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [Umiejętność wroga [9901101] (ulepszenie 1) — nazwa] 서투른 찌르기
   źródło: Skills_Tutorial.json :: dataList[id=9901101].levelList[level=1].name
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Umiejętność wroga [9901201] (ulepszenie 1) — nazwa] 어설픈 베기
   źródło: Skills_Tutorial.json :: dataList[id=9901201].levelList[level=1].name
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [Umiejętność wroga [9901301] (ulepszenie 1) — nazwa] 서투른 찌르기
   źródło: Skills_Tutorial.json :: dataList[id=9901301].levelList[level=1].name
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Umiejętność wroga [9901401] (ulepszenie 1) — nazwa] 어설픈 베기
   źródło: Skills_Tutorial.json :: dataList[id=9901401].levelList[level=1].name
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Umiejętność wroga [9901501] (ulepszenie 1) — nazwa] 싱거운 타격
   źródło: Skills_Tutorial.json :: dataList[id=9901501].levelList[level=1].name
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność wroga [9901601] (ulepszenie 1) — nazwa] 어설픈 베기
   źródło: Skills_Tutorial.json :: dataList[id=9901601].levelList[level=1].name
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [Umiejętność wroga [9901701] (ulepszenie 1) — nazwa] 싱거운 타격
   źródło: Skills_Tutorial.json :: dataList[id=9901701].levelList[level=1].name
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Umiejętność wroga [9901801] (ulepszenie 1) — nazwa] 타격
   źródło: Skills_Tutorial.json :: dataList[id=9901801].levelList[level=1].name
   limit: do 40 znaków
   EN: Hit
   PL:
250. [Umiejętność wroga [9901802] (ulepszenie 1) — nazwa] 묵직한 일격
   źródło: Skills_Tutorial.json :: dataList[id=9901802].levelList[level=1].name
   limit: do 40 znaków
   EN: Heavy Strike
   PL:
251. [Umiejętność wroga [9901803] (ulepszenie 1) — nazwa] 막기
   źródło: Skills_Tutorial.json :: dataList[id=9901803].levelList[level=1].name
   limit: do 40 znaków
   EN: Block
   PL:
252. [Umiejętność wroga [9901901] (ulepszenie 1) — nazwa] 어설픈 베기
   źródło: Skills_Tutorial.json :: dataList[id=9901901].levelList[level=1].name
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Umiejętność wroga [9902001] (ulepszenie 1) — nazwa] 싱거운 타격
   źródło: Skills_Tutorial.json :: dataList[id=9902001].levelList[level=1].name
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Umiejętność wroga [9902101] (ulepszenie 1) — nazwa] 서투른 찌르기
   źródło: Skills_Tutorial.json :: dataList[id=9902101].levelList[level=1].name
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Umiejętność wroga [9902201] (ulepszenie 1) — nazwa] 어설픈 베기
   źródło: Skills_Tutorial.json :: dataList[id=9902201].levelList[level=1].name
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Umiejętność wroga [9902301] (ulepszenie 1) — nazwa] 서투른 찌르기
   źródło: Skills_Tutorial.json :: dataList[id=9902301].levelList[level=1].name
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Umiejętność wroga [9902401] (ulepszenie 1) — nazwa] 묵직한 타격
   źródło: Skills_Tutorial.json :: dataList[id=9902401].levelList[level=1].name
   limit: do 40 znaków
   EN: Heavy Hit
   PL:
258. [Umiejętność wroga [9902501] (ulepszenie 1) — nazwa] 타격
   źródło: Skills_Tutorial.json :: dataList[id=9902501].levelList[level=1].name
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Umiejętność wroga [9902601] (ulepszenie 1) — nazwa] 싱거운 타격
   źródło: Skills_Tutorial.json :: dataList[id=9902601].levelList[level=1].name
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [podstawowe] Pasywka wroga: Passives_Abnormality-mr7-extreme
- plik gry: `Passives_Abnormality-mr7-extreme.json`

260. [[podstawowe] Pasywka wroga [139001] — nazwa] 피의 축제 개막
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139001].name
   limit: do 40 znaków
   EN: Let the Blood Festival Flow
   PL:
261. [[podstawowe] Pasywka wroga [139001] — opis] 종말 토우를 전부 잡으면 페이즈가 변경됨
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139001].desc
   limit: do 120 znaków
   EN: The battle proceeds to the next phase after all the Clay Dolls are defeated
   PL:
262. [[podstawowe] Pasywka wroga [139003] — nazwa] 불의 축제 개막
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139003].name
   limit: do 40 znaków
   EN: Let the Fire Festival Ignite
   PL:
263. [[podstawowe] Pasywka wroga [139003] — opis] 팔이 전부 파괴되거나, 본체의 체력이 70% 이하로 내려가면 페이즈가 변경됨
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139003].desc
   limit: do 140 znaków
   EN: If both Arms are destroyed or the main body’s HP is brought to 70%, the battle proceeds to the next phase
   PL:
264. [[podstawowe] Pasywka wroga [139004] — nazwa] 열기
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139004].name
   limit: do 40 znaków
   EN: Frenzy
   PL:
265. [[podstawowe] Pasywka wroga [139004] — opis] 3페이즈 동안 매 턴마다 모든 적에게 [Combustion] 7을 부여함
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139004].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: During phase 3, inflict 7 [Combustion] on all enemies every turn
   PL:
266. [[podstawowe] Pasywka wroga [139006] — nazwa] 별의 축제 개막
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139006].name
   limit: do 40 znaków
   EN: Let the Star Festival Fall
   PL:
267. [[podstawowe] Pasywka wroga [139006] — opis] 본체의 체력이 25% 이하가 되면 페이즈가 변경됨
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139006].desc
   limit: do 120 znaków
   EN: When the Core HP is brought to 25% or lower, the battle proceeds to the next phase
   PL:
268. [[podstawowe] Pasywka wroga [139101] — nazwa] 우상 숭배
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139101].name
   limit: do 40 znaków
   EN: Idolatry
   PL:
269. [[podstawowe] Pasywka wroga [139101] — opis] 체력이 0이 되면 사망하지 않고, 행동, 타겟팅 불가 상태가 됨\n종말 달력 제압 시 함께 제압됨
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139101].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Does not die at 0 HP; instead, remains on the stage as an immobile and untargetable unit.\nSuppressed when the Doomsday Calendar is suppressed
   PL:
270. [[podstawowe] Pasywka wroga [139301] — nazwa] 돌아오는 과거
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139301].name
   limit: do 40 znaków
   EN: Returning Past
   PL:
271. [[podstawowe] Pasywka wroga [139301] — opis] [AccumulatedPastMirror]가 50 이상이면, 본체 체력이 80% 이하일 때 턴 종료 시 [AccumulatedPastMirror]를 50 소모하여 본체 체력을 200 회복함
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139301].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [AccumulatedPastMirror]
   znaczenie tagów: [AccumulatedPastMirror] = 축적된 과거 / Accumulated Past
   EN: At 50+ [AccumulatedPastMirror], and if Core HP is at 80%-, the Core heals 200 HP by consuming 50 [AccumulatedPastMirror] at Turn End
   PL:
272. [[podstawowe] Pasywka wroga [139302] — nazwa] 소실된 과거
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139302].name
   limit: do 40 znaków
   EN: Misplaced Past
   PL:
273. [[podstawowe] Pasywka wroga [139302] — opis] 몸통 부위 파괴 시, [AccumulatedPastMirror] 전부 소모\n몸통 부위 파괴 시, 다음 턴부터 이번 전투동안 몸통 부위가 모든 속성과 공격 유형에 대하여 내성(0.5)이 됨
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139302].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [AccumulatedPastMirror]
   znaczenie tagów: [AccumulatedPastMirror] = 축적된 과거 / Accumulated Past
   EN: When the Body is broken, consume all [AccumulatedPastMirror]\nWhen the Body is broken, starting next turn, all Attack Types and Affinities become Ineffective(0.5) for the rest of the Encounter
   PL:
274. [[podstawowe] Pasywka wroga [139303] — nazwa] 파괴된 배연 기관
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139303].name
   limit: do 40 znaków
   EN: Broken Exhaust Port
   PL:
275. [[podstawowe] Pasywka wroga [139303] — opis] 증기총 부위 파괴 시, 모든 부위의 [Breath] 전부 소모\n증기총 부위가 파괴된 이후, [Breath]을 얻을 때마다 [Vulnerable]을 [Breath]만큼 얻음.\n증기총 부위가 파괴된 이후, 매 공격 스킬 사용 시 [Breath] 1을 잃음
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139303].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Vulnerable]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Vulnerable] = 취약 / Fragile
   EN: When Steam Blaster is broken, completely lose [Breath] on all parts\nOnce Steam Blaster is broken, every time this unit gains [Breath], gain [Vulnerable] for every [Breath] gained\nOnce Steam Blaster is broken, lose 1 [Breath] On Use of an Attack Skill
   PL:
276. [[podstawowe] Pasywka wroga [139304] — nazwa] 새어나오는 증기
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139304].name
   limit: do 40 znaków
   EN: Leaking Steam
   PL:
277. [[podstawowe] Pasywka wroga [139304] — opis] 증기총 부위 피격 시, [Breath]과 [Breath] 횟수 1 감소
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139304].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: When Steam Blaster is hit, lose 1 [Breath] and 1 [Breath] Count
   PL:
278. [[podstawowe] Pasywka wroga [139305] — nazwa] 메트로놈
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139305].name
   limit: do 40 znaków
   EN: Metronome
   PL:
279. [[podstawowe] Pasywka wroga [139305] — opis] [AccumulatedPastMirror]가 홀수이면 [Vulnerable]과 [AttackDmgUp]를 3 얻음\n짝수이면, [Protection]와 [AttackDmgDown]를 3 얻음
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139305].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [AccumulatedPastMirror], [Vulnerable], [AttackDmgUp], [Protection], [AttackDmgDown]
   znaczenie tagów: [AccumulatedPastMirror] = 축적된 과거 / Accumulated Past; [Vulnerable] = 취약 / Fragile; [AttackDmgUp] = 피해량 증가 / Damage Up; [Protection] = 보호 / Protection; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: If the [AccumulatedPastMirror] is an odd number, gain 3 [Vulnerable] and [AttackDmgUp]\nIf it is an even number, gain 3 [Protection] and [AttackDmgDown]
   PL:
280. [[podstawowe] Pasywka wroga [139401] — nazwa] 행복해진 닭
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139401].name
   limit: do 40 znaków
   EN: Vigorous Volaille
   PL:
281. [[podstawowe] Pasywka wroga [139401] — opis] 턴 종료 시, 전투에 참여중인 (생닭 수 x 5)만큼 체력 회복
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139401].desc
   limit: do 120 znaków
   EN: Turn End: Heal 5 HP for every Raw Chicken on the field
   PL:
282. [[podstawowe] Pasywka wroga [139402] — nazwa] 우울해진 닭
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139402].name
   limit: do 40 znaków
   EN: Gloomy Gallus
   PL:
283. [[podstawowe] Pasywka wroga [139402] — opis] 턴 종료 시, 전투에 참여중인 (생닭 수 x 5)만큼 모든 적에게 정신력 피해
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139402].desc
   limit: do 120 znaków
   EN: Turn End: Deal 5 SP damage to all enemies for every Raw Chicken on the field
   PL:
284. [[podstawowe] Pasywka wroga [139403] — nazwa] 취약해진 닭
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139403].name
   limit: do 40 znaków
   EN: Fragile Fowl
   PL:
285. [[podstawowe] Pasywka wroga [139403] — opis] 부위 파괴 시, 매 턴마다 부위 파괴 턴까지 죽은 생닭 수만큼 [Vulnerable]을 얻음
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139403].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: When a Part breaks, gain 1 [Vulnerable] every turn for every Raw Chicken that died before that Part was broken
   PL:
286. [[podstawowe] Pasywka wroga [139404] — nazwa] 강해진 닭
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139404].name
   limit: do 40 znaków
   EN: Powerful Poussin
   PL:
287. [[podstawowe] Pasywka wroga [139404] — opis] 부위 파괴 상태가 아니라면, 매 턴마다 살아있는 닭만큼 [AttackDmgUp]를 얻음
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139404].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: If the Part isn’t broken, gain 1 [AttackDmgUp] every turn for every surviving Raw Chicken
   PL:
288. [[podstawowe] Pasywka wroga [139501] — nazwa] 걸어다니는 봉이닭
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139501].name
   limit: do 40 znaków
   EN: Bongy Chicken Struts
   PL:
289. [[podstawowe] Pasywka wroga [139501] — opis] 턴 종료 시, 무작위 적 1명에게 3만큼 정신력 피해
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139501].desc
   limit: do 120 znaków
   EN: Turn End: Deal 3 SP damage to a random enemy
   PL:
290. [[podstawowe] Pasywka wroga [139701] — nazwa] 힘이 쑥쑥 봉이닭
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139701].name
   limit: do 40 znaków
   EN: Bongy Chicken Beefs Up
   PL:
291. [[podstawowe] Pasywka wroga [139701] — opis] 턴 종료 시, 다음 턴에 자신 포함 모든 아군에게 [AttackDmgUp] 2, [Protection] 2 부여
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=139701].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp], [Protection]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [Protection] = 보호 / Protection
   EN: Turn End: Apply 2 [AttackDmgUp] and 2 [Protection] to all allies next turn, including this unit
   PL:
292. [[podstawowe] Pasywka wroga [141001] — nazwa] 피주머니
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141001].name
   limit: do 40 znaków
   EN: Blood Sac
   PL:
293. [[podstawowe] Pasywka wroga [141001] — opis] [BloodPocket]가 있으면, 몸통의 분노 내성 -50%, 우울 내성 +50%
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141001].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [BloodPocket]
   znaczenie tagów: [BloodPocket] = 피주머니 / Blood Sac
   EN: If this unit has [BloodPocket]:\n- The Body's Wrath Resist. -50%\n- The Body's Gloom Resist. +50%
   PL:
294. [[podstawowe] Pasywka wroga [141002] — nazwa] 물주머니
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141002].name
   limit: do 40 znaków
   EN: Fluid Sac
   PL:
295. [[podstawowe] Pasywka wroga [141002] — opis] [WaterPocket]가 있으면, (수치 x 20)만큼 본체 체력 회복
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141002].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WaterPocket]
   znaczenie tagów: [WaterPocket] = 물주머니 / Fluid Sac
   EN: If this unit has [WaterPocket], heal its Core by (Stack x 20)
   PL:
296. [[podstawowe] Pasywka wroga [141003] — nazwa] 찢어진 피주머니
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141003].name
   limit: do 40 znaków
   EN: Ruptured Blood Sac
   PL:
297. [[podstawowe] Pasywka wroga [141003] — opis] 몸통 부위가 파괴되었으면, 이후 합 승리 시 적의 [Laceration]을 1회 발동시키고, [Laceration] 횟수 1 감소
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141003].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Once the Body is broken, on Clash Win, activate the enemy's [Laceration] once and reduce [Laceration] Count by 1
   PL:
298. [[podstawowe] Pasywka wroga [141004] — nazwa] 찰박거림
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141004].name
   limit: do 40 znaków
   EN: Splash Around
   PL:
299. [[podstawowe] Pasywka wroga [141004] — opis] 같은 물리 속성의 스킬로 합을 진행한 대상에게 [PlayingWithWaterTogetherMirror]을 1 부여함 (스킬당 1회, 턴당 3회)\n- 해당 스킬이 타격일 경우 대신 [PlayingWithWaterTogetherMirror]을 2 부여함
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141004].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [PlayingWithWaterTogetherMirror]
   znaczenie tagów: [PlayingWithWaterTogetherMirror] = 찰박찰박 / Splish Splash
   EN: Apply 1 [PlayingWithWaterTogetherMirror] on the target that Clashed against this unit's Skill using a Skill that has the same Attack Type as this unit's (once per Skill, 3 times per turn)\n- If it was a Blunt Skill, apply 2 [PlayingWithWaterTogetherMirror] instead
   PL:
300. [[podstawowe] Pasywka wroga [141101] — nazwa] 물주머니
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141101].name
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [[podstawowe] Pasywka wroga [141101] — opis] [WaterPocket]가 있으면, (수치 x 30)만큼 본체 체력 회복
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WaterPocket]
   znaczenie tagów: [WaterPocket] = 물주머니 / Fluid Sac
   EN: If this unit has [WaterPocket], heal its Core by (Stack x 30)
   PL:
302. [[podstawowe] Pasywka wroga [141102] — nazwa] 찢어진 피주머니
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141102].name
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [[podstawowe] Pasywka wroga [141102] — opis] 몸통 부위가 파괴되었으면, 이후 합 승리 시 적의 [Laceration]을 2회 발동시키고, [Laceration] 횟수 2 감소
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141102].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Once the Body is broken, on Clash Win, activate the enemy's [Laceration] twice and reduce [Laceration] Count by 2
   PL:
304. [[podstawowe] Pasywka wroga [141201] — nazwa] 피주머니
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141201].name
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [[podstawowe] Pasywka wroga [141201] — opis] [BloodPocket]가 있으면, 몸통의 분노 내성 -35%, 우울 내성 +35%
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141201].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [BloodPocket]
   znaczenie tagów: [BloodPocket] = 피주머니 / Blood Sac
   EN: If this unit has [BloodPocket]:\n- The Body's Wrath Resist. -35%\n- The Body's Gloom Resist. +35%
   PL:
306. [[podstawowe] Pasywka wroga [141202] — nazwa] 물주머니
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141202].name
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [[podstawowe] Pasywka wroga [141202] — opis] [WaterPocket]가 있으면, (수치 x 35)만큼 본체 체력 회복
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141202].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WaterPocket]
   znaczenie tagów: [WaterPocket] = 물주머니 / Fluid Sac
   EN: If this unit has [WaterPocket], heal its Core by (Stack x 35)
   PL:
308. [[podstawowe] Pasywka wroga [141203] — nazwa] 찢어진 피주머니
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141203].name
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [[podstawowe] Pasywka wroga [141203] — opis] 몸통 부위가 파괴되었으면, 이후 합 승리 시 적의 [Laceration]을 3회 발동시키고, [Laceration] 횟수 3 감소
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141203].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Once the Body is broken, on Clash Win, activate the enemy's [Laceration] thrice and reduce [Laceration] Count by 3
   PL:
310. [[podstawowe] Pasywka wroga [141204] — nazwa] 찰박찰박찰박
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141204].name
   limit: do 40 znaków
   EN: SplishSplashSplish
   PL:
311. [[podstawowe] Pasywka wroga [141204] — opis] 대상에게 [PlayingWithWaterTogetherMirror]이 없으면, 아래 효과 적용\n- 가하는 피해량 +80%\n- 자신의 스킬 중 마지막 코인 적중시 [VibrationExplosion] 1회. [Vibration] 횟수 1 감소\n\n대상에게 [PlayingWithWaterTogetherMirror]이 있으면, 아래 효과 적용\n- 가하는 피해량 -50%\n- 대상의 [PlayingWithWaterTogetherMirror] 당 받는 피해량 +10% (최대 100%)\n\n[PlayingWithWaterTogetherMirror]을 보유한 대상이 없다면, 아래 효과 적용\n- 자신의 스킬 적중시 [Laceration] 5 부여\n- 자신의 스킬 중 마지막 코인 적중시 대상의 [Laceration] 1회 발동. [Laceration] 횟수 1 감소
   źródło: Passives_Abnormality-mr7-extreme.json :: dataList[id=141204].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: \n, [PlayingWithWaterTogetherMirror], [VibrationExplosion], [Vibration], [Laceration]
   znaczenie tagów: [PlayingWithWaterTogetherMirror] = 찰박찰박 / Splish Splash; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [Laceration] = 출혈 / Bleed
   EN: If target does not have [PlayingWithWaterTogetherMirror], gain the following effects:\n- Deal +80% damage\n- On Hit using a Skill's final Coin, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n\nIf target has [PlayingWithWaterTogetherMirror], gain the following effects:\n- Deal -50% damage\n- Take +10% damage for every [PlayingWithWaterTogetherMirror] Stack on target (max 100%)\n\nIf no one has [PlayingWithWaterTogetherMirror], gain the following effects:\n- On Hit using a Skill, inflict 5 [Laceration]\n- On Hit using a Skill's final Coin, activate [Laceration] once; then, reduce target's [Laceration] Count by 1
   PL:

## [podstawowe] Pasywka wroga: Passives_Abnormality
- plik gry: `Passives_Abnormality.json`

312. [[podstawowe] Pasywka wroga [800101] — nazwa] 사과의 황홀기
   źródło: Passives_Abnormality.json :: dataList[id=800101].name
   limit: do 40 znaków
   EN: An Apple’s Twilight
   PL:
313. [[podstawowe] Pasywka wroga [800101] — opis] 열매가 파괴되면 모든 부위가 취약 2를 얻음.\n파괴된 열매는 1턴 후 재생됨.
   źródło: Passives_Abnormality.json :: dataList[id=800101].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the Fruit is destroyed, all parts are inflicted with 2 Fragile.\nThe Fruit regenerates after 1 turn.
   PL:
314. [[podstawowe] Pasywka wroga [800101] — podsumowanie] 열매가 파괴되면 모든 부위가 취약 2를 얻음
   źródło: Passives_Abnormality.json :: dataList[id=800101].summary
   limit: do 120 znaków
   EN: When the Fruit is destroyed, apply 2 Fragile to all parts
   PL:
315. [[podstawowe] Pasywka wroga [800102] — nazwa] 나오면 안되는 패시브1
   źródło: Passives_Abnormality.json :: dataList[id=800102].name
   limit: do 40 znaków
   EN: NOT FOR DISPLAY1
   PL:
316. [[podstawowe] Pasywka wroga [800102] — opis] 머리가 한 번 재생된 후, 머리의 체력을 50% 미만으로 만들면 선택지가 등장한다.
   źródło: Passives_Abnormality.json :: dataList[id=800102].desc
   limit: do 120 znaków
   EN: After the head regenerates once, bringing the head’s HP to 50% initiates a choice prompt.
   PL:
317. [[podstawowe] Pasywka wroga [800103] — nazwa] 나오면 안되는 패시브2
   źródło: Passives_Abnormality.json :: dataList[id=800103].name
   limit: do 40 znaków
   EN: NOT FOR DISPLAY2
   PL:
318. [[podstawowe] Pasywka wroga [800103] — opis] 3턴 시작 시 녹색 줄기 효과를 제거할 수 있는 선택지가 등장한다.
   źródło: Passives_Abnormality.json :: dataList[id=800103].desc
   limit: do 130 znaków
   EN: At the start of Turn 3, a choice prompt where you can remove the Green Stem effect is initiated.
   PL:
319. [[podstawowe] Pasywka wroga [800104] — nazwa] 휘감는 뿌리
   źródło: Passives_Abnormality.json :: dataList[id=800104].name
   limit: do 40 znaków
   EN: Entangling Roots
   PL:
320. [[podstawowe] Pasywka wroga [800104] — opis] 뿌리가 파괴되기 전까지 턴 시작 시 모든 적에게 속박 1을 부여함.
   źródło: Passives_Abnormality.json :: dataList[id=800104].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the turn, inflict 1 Bind on all enemies.\nThis lasts until the Roots have been broken.
   PL:
321. [[podstawowe] Pasywka wroga [800104] — podsumowanie] 뿌리가 파괴되기 전까지 모든 적에게 속박 1을 부여
   źródło: Passives_Abnormality.json :: dataList[id=800104].summary
   limit: do 120 znaków
   EN: Inflict 1 Bind on all enemies until Roots are broken
   PL:
322. [[podstawowe] Pasywka wroga [800105] — nazwa] 단 하나의 뿌리
   źródło: Passives_Abnormality.json :: dataList[id=800105].name
   limit: do 40 znaków
   EN: One Sole Root
   PL:
323. [[podstawowe] Pasywka wroga [800105] — opis] 파괴되지 않은 팔의 수만큼 뿌리가 공격 위력 증가 2를 얻는다.
   źródło: Passives_Abnormality.json :: dataList[id=800105].desc
   limit: do 120 znaków
   EN: The Roots gain 2 Attack Power Up for each intact Arm.
   PL:
324. [[podstawowe] Pasywka wroga [800201] — nazwa] 피의 축제 개막
   źródło: Passives_Abnormality.json :: dataList[id=800201].name
   (powtórzenie elementu 260 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [[podstawowe] Pasywka wroga [800201] — opis] 종말 토우를 전부 잡으면 페이즈가 변경된다.
   źródło: Passives_Abnormality.json :: dataList[id=800201].desc
   limit: do 120 znaków
   EN: The battle proceeds to the next phase after all the Clay Dolls are defeated.
   PL:
326. [[podstawowe] Pasywka wroga [800202] — nazwa] 나오면 안됨
   źródło: Passives_Abnormality.json :: dataList[id=800202].name
   limit: do 40 znaków
   EN: DON'T LET THE KIDS READ THIS
   PL:
327. [[podstawowe] Pasywka wroga [800202] — opis] 2페이즈 2턴 시작 시 선택지 1 등장
   źródło: Passives_Abnormality.json :: dataList[id=800202].desc
   limit: do 120 znaków
   EN: At the start of turn 2 in phase 2, choice prompt 1 is initiated.
   PL:
328. [[podstawowe] Pasywka wroga [800203] — nazwa] 불의 축제 개막
   źródło: Passives_Abnormality.json :: dataList[id=800203].name
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [[podstawowe] Pasywka wroga [800203] — opis] 팔이 전부 파괴되거나, 본체의 체력이 70% 이하로 내려가면 페이즈가 변경된다.
   źródło: Passives_Abnormality.json :: dataList[id=800203].desc
   limit: do 140 znaków
   EN: If both Arms are destroyed or the main body’s HP is brought to 70%, the battle proceeds to the next phase.
   PL:
330. [[podstawowe] Pasywka wroga [800204] — nazwa] 열기
   źródło: Passives_Abnormality.json :: dataList[id=800204].name
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [[podstawowe] Pasywka wroga [800204] — opis] 3페이즈동안 매 턴마다 모든 적에게 화상 3을 부여한다.
   źródło: Passives_Abnormality.json :: dataList[id=800204].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During Phase 3\nAt the start of the turn, inflict 3 Burn on all enemies.
   PL:
332. [[podstawowe] Pasywka wroga [800205] — nazwa] 나오면 안됨
   źródło: Passives_Abnormality.json :: dataList[id=800205].name
   limit: do 40 znaków
   EN: NOT FOR DISPLAY
   PL:
333. [[podstawowe] Pasywka wroga [800205] — opis] 체력이 최대 체력의 60% 이하가 되면 선택지 2 등장
   źródło: Passives_Abnormality.json :: dataList[id=800205].desc
   limit: do 120 znaków
   EN: When HP is brought to 60%, choice prompt 2 is initiated.
   PL:
334. [[podstawowe] Pasywka wroga [800206] — nazwa] 별의 축제 개막
   źródło: Passives_Abnormality.json :: dataList[id=800206].name
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [[podstawowe] Pasywka wroga [800206] — opis] 본체의 체력이 25% 이하가 되면 페이즈가 변경된다.
   źródło: Passives_Abnormality.json :: dataList[id=800206].desc
   limit: do 120 znaków
   EN: When HP is brought to 25%, the battle proceeds to the next phase.
   PL:
336. [[podstawowe] Pasywka wroga [800207] — nazwa] 나오면 안됨
   źródło: Passives_Abnormality.json :: dataList[id=800207].name
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [[podstawowe] Pasywka wroga [800207] — opis] 4페이즈 2번째 턴에 선택지 3 등장
   źródło: Passives_Abnormality.json :: dataList[id=800207].desc
   limit: do 120 znaków
   EN: At the start of turn 2 in phase 4, choice prompt 3 is initiated.
   PL:
338. [[podstawowe] Pasywka wroga [800301] — nazwa] 우상 숭배
   źródło: Passives_Abnormality.json :: dataList[id=800301].name
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [[podstawowe] Pasywka wroga [800301] — opis] 체력이 0이 되면 사망하지 않고, 행동, 타겟팅 불가 상태가 된다.\n종말 달력 제압 시 함께 제압된다.
   źródło: Passives_Abnormality.json :: dataList[id=800301].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Does not die at 0 HP; instead, remains on the stage as an immobile and untargetable unit.\nSuppressed when the Doomsday Calendar is suppressed.
   PL:
340. [[podstawowe] Pasywka wroga [800801] — nazwa] 조각난 황금
   źródło: Passives_Abnormality.json :: dataList[id=800801].name
   limit: do 40 znaków
   EN: Cracked Gold
   PL:
341. [[podstawowe] Pasywka wroga [800801] — opis] 매 턴마다 황금빛 수치에 비례하여 체력을 회복한다.
   źródło: Passives_Abnormality.json :: dataList[id=800801].desc
   limit: do 120 znaków
   EN: Heals HP every turn based on the amount of Golden Sheen.
   PL:
342. [[podstawowe] Pasywka wroga [800902] — nazwa] 파괴된 중추
   źródło: Passives_Abnormality.json :: dataList[id=800902].name
   limit: do 40 znaków
   EN: Frail Core
   PL:
343. [[podstawowe] Pasywka wroga [800902] — opis] 머리가 파괴 당하면 다음 턴 동안 모든 부위가 행동하지 않는다. 파괴된 머리는 1턴 후 재생된다.
   źródło: Passives_Abnormality.json :: dataList[id=800902].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the Head is destroyed, all parts are inflicted with Immobilize next turn.\nThe Head regenerates after 1 turn.
   PL:
344. [[podstawowe] Pasywka wroga [800903] — nazwa] 허물어진 사과
   źródło: Passives_Abnormality.json :: dataList[id=800903].name
   limit: do 40 znaków
   EN: Rotting Apple
   PL:
345. [[podstawowe] Pasywka wroga [800903] — opis] 몸통이 파괴 당하면 다음 턴 부터 모든 부위가 공격 위력 감소 2를 얻는다.
   źródło: Passives_Abnormality.json :: dataList[id=800903].desc
   limit: do 120 znaków
   EN: After the body is destroyed, all parts are inflicted with 2 Attack Power Down every turn.
   PL:
346. [[podstawowe] Pasywka wroga [800904] — nazwa] 나오면 안되는 텍스트
   źródło: Passives_Abnormality.json :: dataList[id=800904].name
   limit: do 40 znaków
   EN: NOT FOR DISPLAY
   PL:
347. [[podstawowe] Pasywka wroga [800904] — opis] 나오면 안되는 텍스트
   źródło: Passives_Abnormality.json :: dataList[id=800904].desc
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [[podstawowe] Pasywka wroga [801001] — nazwa] 강화 공장 가동
   źródło: Passives_Abnormality.json :: dataList[id=801001].name
   limit: do 40 znaków
   EN: Upgrade Factory at Work
   PL:
349. [[podstawowe] Pasywka wroga [801001] — opis] 사망 시 다음 턴에 시술을 1 얻고, 부활한다.
   źródło: Passives_Abnormality.json :: dataList[id=801001].desc
   limit: do 120 znaków
   EN: When this unit is defeated, it revives the next turn and gains 1 Surgery.
   PL:
350. [[podstawowe] Pasywka wroga [801002] — nazwa] 당신은 강해져야합니다
   źródło: Passives_Abnormality.json :: dataList[id=801002].name
   limit: do 40 znaków
   EN: You Must Become Strong
   PL:
351. [[podstawowe] Pasywka wroga [801002] — opis] 매 턴마다 보호 1을 얻는다.
   źródło: Passives_Abnormality.json :: dataList[id=801002].desc
   limit: do 120 znaków
   EN: At the start of the turn, gain 1 Protection.
   PL:
352. [[podstawowe] Pasywka wroga [801201] — nazwa] 당신은 강해져야합니다
   źródło: Passives_Abnormality.json :: dataList[id=801201].name
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [[podstawowe] Pasywka wroga [801201] — opis] 매 턴마다 보호 2를 얻는다.
   źródło: Passives_Abnormality.json :: dataList[id=801201].desc
   limit: do 120 znaków
   EN: At the start of the turn, gain 2 Protection.
   PL:
354. [[podstawowe] Pasywka wroga [801301] — nazwa] 흔들리는 욕망
   źródło: Passives_Abnormality.json :: dataList[id=801301].name
   limit: do 40 znaków
   EN: Wavering Desires
   PL:
355. [[podstawowe] Pasywka wroga [801301] — opis] 탐욕 상태가 되면 취약 2, 속박 10를 얻고, 스킬 슬롯이 1 증가하며, 스킬 패턴이 변경됨.
   źródło: Passives_Abnormality.json :: dataList[id=801301].desc
   limit: do 130 znaków
   EN: While Desirous, the unit gains 2 Fragile and 10 Bind, gains 1 skill slot, and changes behavior.
   PL:
356. [[podstawowe] Pasywka wroga [801302] — nazwa] 옭아매는 욕망
   źródło: Passives_Abnormality.json :: dataList[id=801302].name
   limit: do 40 znaków
   EN: Ensnaring Desires
   PL:
357. [[podstawowe] Pasywka wroga [801302] — opis] 체력이 30% 감소할 때마다 탐욕 상태가 됨.
   źródło: Passives_Abnormality.json :: dataList[id=801302].desc
   limit: do 120 znaków
   EN: The unit becomes Desirous every time it loses 30% of its HP.
   PL:
358. [[podstawowe] Pasywka wroga [801904] — nazwa] 살갗을 에는 두려움
   źródło: Passives_Abnormality.json :: dataList[id=801904].name
   limit: do 40 znaków
   EN: Shuddering Terror
   PL:
359. [[podstawowe] Pasywka wroga [801904] — opis] 이번 웨이브동안 사망한 아군 수만큼 보호를 얻는다. (최대 5)
   źródło: Passives_Abnormality.json :: dataList[id=801904].desc
   limit: do 120 znaków
   EN: Gain 1 Protection for every ally that died this wave. (Max 5.)
   PL:
360. [[podstawowe] Pasywka wroga [802401] — nazwa] 맥동하는 팔
   źródło: Passives_Abnormality.json :: dataList[id=802401].name
   limit: do 40 znaków
   EN: Pulsating Arms
   PL:
361. [[podstawowe] Pasywka wroga [802401] — opis] 턴 시작 시 본능만큼 공격 위력 증가와 보호를 얻는다.
   źródło: Passives_Abnormality.json :: dataList[id=802401].desc
   limit: do 120 znaków
   EN: At the start of the turn, gain Attack Power Up and Protection by the Count of Instincts.
   PL:
362. [[podstawowe] Pasywka wroga [802402] — nazwa] 훼손당한 팔
   źródło: Passives_Abnormality.json :: dataList[id=802402].name
   limit: do 40 znaków
   EN: Damaged Arms
   PL:
363. [[podstawowe] Pasywka wroga [802402] — opis] 공격으로 피해를 1 이상 받으면 본능을 1 잃는다.
   źródło: Passives_Abnormality.json :: dataList[id=802402].desc
   limit: do 120 znaków
   EN: Lose 1 Instincts whenever the unit takes damage from attacks.
   PL:
364. [[podstawowe] Pasywka wroga [802403] — nazwa] 껍데기 회복
   źródło: Passives_Abnormality.json :: dataList[id=802403].name
   limit: do 40 znaków
   EN: Regenerating Shell
   PL:
365. [[podstawowe] Pasywka wroga [802403] — opis] 한 턴동안 공격으로 피해를 받지 않으면, 턴 종료 시 체력을 5% 회복하고, 본능을 1 얻는다.
   źródło: Passives_Abnormality.json :: dataList[id=802403].desc
   limit: do 160 znaków
   EN: At the end of the turn, if the unit didn’t take any damage from attacks during the turn, heal 5% HP and gain 1 Instincts.
   PL:
366. [[podstawowe] Pasywka wroga [802404] — nazwa] 광기에 찬 눈동자
   źródło: Passives_Abnormality.json :: dataList[id=802404].name
   limit: do 40 znaków
   EN: Frantic Eyes
   PL:
367. [[podstawowe] Pasywka wroga [802404] — opis] 본능이 4 이상이면 공격적으로, 4 미만이면 방어적으로 스킬 패턴이 변경된다.
   źródło: Passives_Abnormality.json :: dataList[id=802404].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Behavior depends on the Count of Instincts.\nUses aggressive skills at +4 Instincts, and becomes defensive at 3 or less.
   PL:
368. [[podstawowe] Pasywka wroga [802501] — nazwa] 팽창된 공격성
   źródło: Passives_Abnormality.json :: dataList[id=802501].name
   limit: do 40 znaków
   EN: Amplified Aggression
   PL:
369. [[podstawowe] Pasywka wroga [802501] — opis] 피격 시 본능 1을 얻는다. 턴 종료 시 본능이 4 이상이면 광란 상태가 된다.
   źródło: Passives_Abnormality.json :: dataList[id=802501].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When hit by an attack, gain 1 Instincts.\nIf the unit has +4 Instincts at the end of the turn, enter a state of Frenzy.
   PL:
370. [[podstawowe] Pasywka wroga [802502] — nazwa] 광란
   źródło: Passives_Abnormality.json :: dataList[id=802502].name
   limit: do 40 znaków
   EN: Frenzy
   PL:
371. [[podstawowe] Pasywka wroga [802502] — opis] 광란 상태가 되면 공격 위력 증가, 취약 3을 얻고, 스킬 패턴이 변경되며, 피격 시 본능을 얻지 않는다.
   źródło: Passives_Abnormality.json :: dataList[id=802502].desc
   limit: do 180 znaków
   EN: In the Frenzy state, the unit gains 3 Attack Power Up and 3 Fragile, changes behavior, and does not gain Instincts from being attacked.
   PL:
372. [[podstawowe] Pasywka wroga [802503] — nazwa] 일렁이는 분노
   źródło: Passives_Abnormality.json :: dataList[id=802503].name
   limit: do 40 znaków
   EN: Shimmering Rage
   PL:
373. [[podstawowe] Pasywka wroga [802503] — opis] 체력이 50% 미만이면 매 턴마다 광란 상태가 된다.
   źródło: Passives_Abnormality.json :: dataList[id=802503].desc
   limit: do 120 znaków
   EN: At less than 50% HP, enters Frenzy every turn.
   PL:
374. [[podstawowe] Pasywka wroga [802701] — nazwa] 팽창된 공격성
   źródło: Passives_Abnormality.json :: dataList[id=802701].name
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [[podstawowe] Pasywka wroga [802701] — opis] 피격 시 본능 1을 얻는다. 턴 종료 시 본능이 4 이상이면 광란 상태가 된다.
   źródło: Passives_Abnormality.json :: dataList[id=802701].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [[podstawowe] Pasywka wroga [802702] — nazwa] 광란
   źródło: Passives_Abnormality.json :: dataList[id=802702].name
   (powtórzenie elementu 370 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [[podstawowe] Pasywka wroga [802702] — opis] 광란 상태가 되면 공격 위력 증가, 취약 3을 얻고, 스킬 패턴이 변경되며, 피격 시 본능을 얻지 않는다.
   źródło: Passives_Abnormality.json :: dataList[id=802702].desc
   (powtórzenie elementu 371 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [[podstawowe] Pasywka wroga [802801] — nazwa] 썩어가는 피부
   źródło: Passives_Abnormality.json :: dataList[id=802801].name
   limit: do 40 znaków
   EN: Rotting Skin
   PL:
379. [[podstawowe] Pasywka wroga [802801] — opis] 턴 시작 시 체력이 50% 미만이면, 피격 시 공격자에게 독 3을 부여한다.
   źródło: Passives_Abnormality.json :: dataList[id=802801].desc
   limit: do 120 znaków
   EN: At the start of the turn, if at less than 50% HP, inflict 3 Poison when attacked.
   PL:
380. [[podstawowe] Pasywka wroga [802802] — nazwa] 허물 벗기
   źródło: Passives_Abnormality.json :: dataList[id=802802].name
   limit: do 40 znaków
   EN: Molt
   PL:
381. [[podstawowe] Pasywka wroga [802802] — opis] 파괴 후 1턴 뒤 다른 팔이 파괴되지 않았으면, 해당 팔과 동일한 체력으로 팔이 재생된다.
   źródło: Passives_Abnormality.json :: dataList[id=802802].desc
   limit: do 180 znaków
   EN: After this part is broken, if the other arm is not broken at the end of the following turn, this part regenerates with the same HP as it.
   PL:
382. [[podstawowe] Pasywka wroga [802803] — nazwa] 고통의 몸부림
   źródło: Passives_Abnormality.json :: dataList[id=802803].name
   limit: do 40 znaków
   EN: Pained Writhing
   PL:
383. [[podstawowe] Pasywka wroga [802803] — opis] 양 팔이 파괴되면 매 턴마다 취약 5를 얻고, 모든 적에게 독 10을 부여한다.
   źródło: Passives_Abnormality.json :: dataList[id=802803].desc
   limit: do 140 znaków
   EN: When both arms are broken, the unit gains 5 Fragile and inflicts 10 Poison on all enemies every turn.
   PL:
384. [[podstawowe] Pasywka wroga [802804] — nazwa] 꿈틀거리는 본능
   źródło: Passives_Abnormality.json :: dataList[id=802804].name
   limit: do 40 znaków
   EN: Wriggling Instincts
   PL:
385. [[podstawowe] Pasywka wroga [802804] — opis] 본능 수치가 4 이상이면 공격적으로, 0이면 방어적으로 스킬 패턴이 변경된다.
   źródło: Passives_Abnormality.json :: dataList[id=802804].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Behavior depends on the Count of Instincts.\nUses aggressive skills at +4 Instincts, and becomes defensive at 0.
   PL:
386. [[podstawowe] Pasywka wroga [803302] — nazwa] 잘려나간 팔
   źródło: Passives_Abnormality.json :: dataList[id=803302].name
   limit: do 40 znaków
   EN: Severed Arm
   PL:
387. [[podstawowe] Pasywka wroga [803302] — opis] 팔이 파괴되면 매 턴 시작 시 취약 5를 얻는다.
   źródło: Passives_Abnormality.json :: dataList[id=803302].desc
   limit: do 120 znaków
   EN: When the arm is broken, the unit gains 5 Fragile every turn.
   PL:
388. [[podstawowe] Pasywka wroga [802901] — nazwa] 휘파람의 공포
   źródło: Passives_Abnormality.json :: dataList[id=802901].name
   limit: do 40 znaków
   EN: Fearsome Whistles
   PL:
389. [[podstawowe] Pasywka wroga [802901] — opis] 어느 표지가 3 미만이면 싱클레어가 매 턴마다 속박 1, 마비 1을 얻는다.
   źródło: Passives_Abnormality.json :: dataList[id=802901].desc
   limit: do 140 znaków
   EN: If you have collected less than 3 of A Sign, Sinclair is inflicted with 1 Bind and Paralyze every turn.
   PL:
390. [[podstawowe] Pasywka wroga [802902] — nazwa] 공포를 이기는 용기
   źródło: Passives_Abnormality.json :: dataList[id=802902].name
   limit: do 40 znaków
   EN: Courage to Triumph Fear
   PL:
391. [[podstawowe] Pasywka wroga [802902] — opis] 어느 표지가 3 이상이면 싱클레어가 매 턴마다 공격 위력 증가 1, 보호 2를 얻는다.
   źródło: Passives_Abnormality.json :: dataList[id=802902].desc
   limit: do 140 znaków
   EN: If you have collected 3 or more of A Sign, Sinclair gains 1 Attack Power Up and 2 Protection every turn.
   PL:
392. [[podstawowe] Pasywka wroga [802903] — nazwa] 고통을 받아들여야 해!
   źródło: Passives_Abnormality.json :: dataList[id=802903].name
   limit: do 40 znaków
   EN: You Must Accept the Pain!
   PL:
393. [[podstawowe] Pasywka wroga [802903] — opis] 턴 시작 시 파괴되지 않은 부위가 출혈 또는 화상 상태면, 최대 체력의 15%만큼 체력을 회복하고, 공격 위력 증가 3을 얻는다. 어느 표지의 개수에 비례하여 회복량과 위력 증가 값이 최대 0까지 감소한다.
   źródło: Passives_Abnormality.json :: dataList[id=802903].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the turn, if the unbroken part has Bleed or Burn, heal 15% of Max HP and gain 3 Attack Power Up.\nThe healing and status effects gained are decreased based on the number of A Sign, down to 0.
   PL:
394. [[podstawowe] Pasywka wroga [802904] — nazwa] 처단의 환희
   źródło: Passives_Abnormality.json :: dataList[id=802904].name
   limit: do 40 znaków
   EN: Bliss of Execution
   PL:
395. [[podstawowe] Pasywka wroga [802904] — opis] 적을 처치하면 다음 턴 시작 시 신속 2, 피해량 증가 5를 얻는다.
   źródło: Passives_Abnormality.json :: dataList[id=802904].desc
   limit: do 120 znaków
   EN: After defeating an enemy, gain 2 Haste and 5 Damage Up next turn.
   PL:
396. [[podstawowe] Pasywka wroga [803001] — nazwa] 넘치는 희열
   źródło: Passives_Abnormality.json :: dataList[id=803001].name
   limit: do 40 znaków
   EN: Overflowing Ecstasy
   PL:
397. [[podstawowe] Pasywka wroga [803001] — opis] 3턴부터 2턴마다 희열 상태가 된다.
   źródło: Passives_Abnormality.json :: dataList[id=803001].desc
   limit: do 120 znaków
   EN: Starting with Turn 3, becomes Ecstatic every 2 turns.
   PL:
398. [[podstawowe] Pasywka wroga [803002] — nazwa] 피어난 순수
   źródło: Passives_Abnormality.json :: dataList[id=803002].name
   limit: do 40 znaków
   EN: Blooming Purity
   PL:
399. [[podstawowe] Pasywka wroga [803002] — opis] 크로머의 본체 체력이 50% 미만이 되면 남은 턴동안 순수 상태가 된다.
   źródło: Passives_Abnormality.json :: dataList[id=803002].desc
   limit: do 120 znaków
   EN: If Kromer’s main body is brought to 50% HP, she gains Purity for the remaining turns.
   PL:
400. [[podstawowe] Pasywka wroga [803003] — nazwa] 무결한 육체
   źródło: Passives_Abnormality.json :: dataList[id=803003].name
   limit: do 40 znaków
   EN: Flawless Flesh
   PL:
401. [[podstawowe] Pasywka wroga [803003] — opis] 팔 파괴 시 해당 부위가 공격 위력 감소 2를 얻는다.
   źródło: Passives_Abnormality.json :: dataList[id=803003].desc
   limit: do 120 znaków
   EN: When the arm is broken, the part is inflicted with 2 Attack Power Down.
   PL:
402. [[podstawowe] Pasywka wroga [803101] — nazwa] 피주머니
   źródło: Passives_Abnormality.json :: dataList[id=803101].name
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [[podstawowe] Pasywka wroga [803101] — opis] 분노 내성이 상승한다.\n우울 내성이 하락한다.
   źródło: Passives_Abnormality.json :: dataList[id=803101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Wrath Resistance increases.\nGloom Resistance decreases.
   PL:
404. [[podstawowe] Pasywka wroga [803102] — nazwa] 물주머니
   źródło: Passives_Abnormality.json :: dataList[id=803102].name
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [[podstawowe] Pasywka wroga [803102] — opis] 물주머니가 지속될수록 본체 체력을 (수치 * 20) 만큼 회복한다.
   źródło: Passives_Abnormality.json :: dataList[id=803102].desc
   limit: do 120 znaków
   EN: While the Fluid Sac status is active, the Core heals (20 * Fluid Sac Count) HP.
   PL:
406. [[podstawowe] Pasywka wroga [803103] — nazwa] 끓어오르는 피
   źródło: Passives_Abnormality.json :: dataList[id=803103].name
   limit: do 40 znaków
   EN: Boiling Blood
   PL:
407. [[podstawowe] Pasywka wroga [803103] — opis] 피주머니 상태에서, 몸통 부위 파괴당하면 모든 적에게 20의 고정 피해를 준다.
   źródło: Passives_Abnormality.json :: dataList[id=803103].desc
   limit: do 120 znaków
   EN: If the body is broken while Blood Sac is active, all enemies take 20 fixed damage.
   PL:
408. [[podstawowe] Pasywka wroga [803201] — nazwa] 피뢰침
   źródło: Passives_Abnormality.json :: dataList[id=803201].name
   limit: do 40 znaków
   EN: Lightning Rod
   PL:
409. [[podstawowe] Pasywka wroga [803201] — opis] 전봇대 피격 시, 이번 턴에 감전 2 부여.\n가지고 있는 번개가 5 이상이면, 다음 턴부터 부위마다 피격 시 이번 턴에 감전 3 부여.\n(번개가 0이 되기전까지 지속)\n나태 속성 공격에 피격 시 상대에게 원래 감전 부여가 절반으로 감소. (올림)
   źródło: Passives_Abnormality.json :: dataList[id=803201].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the Telephone Pole is hit, inflict 2 Shock on the attacker this turn.\nAt 5+ Lightning, all Parts will inflict 3 Shock on the attacker, starting next turn.\n(Lasts until Lightning reaches 0.)\nWhen hit by a Sloth attack, the amount of Shock inflicted is halved. (Rounded up.)
   PL:
410. [[podstawowe] Pasywka wroga [803202] — nazwa] 번개
   źródło: Passives_Abnormality.json :: dataList[id=803202].name
   limit: do 40 znaków
   EN: Lightning
   PL:
411. [[podstawowe] Pasywka wroga [803202] — opis] 전봇대가 부숴지지 않았을 때, 공격 종료 시 번개 1 얻는다. 전봇대 피격 시마다, 번개 1 소모.
   źródło: Passives_Abnormality.json :: dataList[id=803202].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: While the telephone pole isn’t broken, gain 1 Lightning after an attack.\nWhenever the telephone pole is hit by an attack, lose 1 Lightning.
   PL:
412. [[podstawowe] Pasywka wroga [803203] — nazwa] 부서지는 파편
   źródło: Passives_Abnormality.json :: dataList[id=803203].name
   limit: do 40 znaków
   EN: Breaking Pieces
   PL:
413. [[podstawowe] Pasywka wroga [803203] — opis] 전봇대가 흐트러지거나 부위 파괴되었을 때, 번개가 0이 됨. 해당 턴동안 골목파수견의 공격 스킬이 전부 취소된다.
   źródło: Passives_Abnormality.json :: dataList[id=803203].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the telephone pole is Staggered or Broken, lose all Lightning.\nAll attacks of Alleyway Watchdog will then be canceled for the turn.
   PL:
414. [[podstawowe] Pasywka wroga [803401] — nazwa] 걸어다니는 봉이닭
   źródło: Passives_Abnormality.json :: dataList[id=803401].name
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [[podstawowe] Pasywka wroga [803401] — opis] 턴 종료 시, 무작위 적 1명에게 3만큼 정신력 피해.
   źródło: Passives_Abnormality.json :: dataList[id=803401].desc
   limit: do 120 znaków
   EN: At the end of the turn, deal 3 SP damage to a random enemy.
   PL:
416. [[podstawowe] Pasywka wroga [803701] — nazwa] 힘이 쑥쑥 봉이닭
   źródło: Passives_Abnormality.json :: dataList[id=803701].name
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [[podstawowe] Pasywka wroga [803701] — opis] 턴 종료 시, 다음 턴에 자신 포함 모든 아군에게 피해량 증가 2, 보호 2 부여.
   źródło: Passives_Abnormality.json :: dataList[id=803701].desc
   limit: do 120 znaków
   EN: At the end of the turn, apply 2 Damage Up and 2 Protection to all allies next turn.
   PL:
418. [[podstawowe] Pasywka wroga [803901] — nazwa] 행복해진 닭
   źródło: Passives_Abnormality.json :: dataList[id=803901].name
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [[podstawowe] Pasywka wroga [803901] — opis] 턴 종료 시, 전투에 참여중인 (생닭 수 * 5)만큼 체력 회복.
   źródło: Passives_Abnormality.json :: dataList[id=803901].desc
   limit: do 120 znaków
   EN: At the end of the turn, heal 5 HP for each Raw Chicken in battle.
   PL:
420. [[podstawowe] Pasywka wroga [803902] — nazwa] 우울해진 닭
   źródło: Passives_Abnormality.json :: dataList[id=803902].name
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [[podstawowe] Pasywka wroga [803902] — opis] 턴 종료 시, 전투에 참여중인 (생닭 수 * 5)만큼 모든 적에게 정신력 피해.
   źródło: Passives_Abnormality.json :: dataList[id=803902].desc
   limit: do 120 znaków
   EN: At the end of the turn, deal 5 SP damage to all enemies for each Raw Chicken in battle.
   PL:
422. [[podstawowe] Pasywka wroga [803903] — nazwa] 취약해진 닭
   źródło: Passives_Abnormality.json :: dataList[id=803903].name
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [[podstawowe] Pasywka wroga [803903] — opis] 부위 파괴 시, 매 턴마다 부위 파괴 턴까지 죽은 생닭 수만큼 취약을 얻음.
   źródło: Passives_Abnormality.json :: dataList[id=803903].desc
   limit: do 140 znaków
   EN: When a Part breaks, gain 1 Fragile every turn for each Raw Chicken that died before the Part was broken.
   PL:
424. [[podstawowe] Pasywka wroga [803904] — nazwa] 강해진 닭
   źródło: Passives_Abnormality.json :: dataList[id=803904].name
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [[podstawowe] Pasywka wroga [803904] — opis] 부위 파괴 상태가 아니라면, 매 턴마다 살아있는 닭만큼 피해량 증가를 얻음.
   źródło: Passives_Abnormality.json :: dataList[id=803904].desc
   limit: do 120 znaków
   EN: If the Part isn’t broken, gain 1 Damage Up for each living Raw Chicken.
   PL:
426. [[podstawowe] Pasywka wroga [804101] — nazwa] 팽창하는 슬픔
   źródło: Passives_Abnormality.json :: dataList[id=804101].name
   limit: do 40 znaków
   EN: Expanding Sorrow
   PL:
427. [[podstawowe] Pasywka wroga [804101] — opis] 턴 종료 시 해소되지 않은 슬픔 이 3 이상 있으면, 다음 턴에 머리가 생성되고 스킬 패턴이 변경된다.
   źródło: Passives_Abnormality.json :: dataList[id=804101].desc
   limit: do 150 znaków
   EN: At the end of the turn, if the unit has 3+ Unresolved Sorrow, generates a head next turn and changes behavior.
   PL:
428. [[podstawowe] Pasywka wroga [804102] — nazwa] 헤어나올 수 없는 슬픔
   źródło: Passives_Abnormality.json :: dataList[id=804102].name
   limit: do 40 znaków
   EN: Inconsolable Sorrow
   PL:
429. [[podstawowe] Pasywka wroga [804102] — opis] 턴 종료 시 해소되지 않은 슬픔 이 3 이상 있을 때, 머리가 파괴되어 있는 경우, 다음 턴에 흐트러짐 상태가 된다.
   źródło: Passives_Abnormality.json :: dataList[id=804102].desc
   limit: do 150 znaków
   EN: At the end of the turn, if the unit has 3+ Unresolved Sorrow and the head is broken, becomes staggered next turn.
   PL:
430. [[podstawowe] Pasywka wroga [804103] — nazwa] 무력화
   źródło: Passives_Abnormality.json :: dataList[id=804103].name
   limit: do 40 znaków
   EN: Taken by the Horns
   PL:
431. [[podstawowe] Pasywka wroga [804103] — opis] 머리가 흐트러짐 상태가 되면, 다음 턴에 모든 부위가 흐트러짐 상태가 된다.
   źródło: Passives_Abnormality.json :: dataList[id=804103].desc
   limit: do 120 znaków
   EN: When the head is staggered, all parts become staggered next turn.
   PL:
432. [[podstawowe] Pasywka wroga [804104] — nazwa] 완전 무력화
   źródło: Passives_Abnormality.json :: dataList[id=804104].name
   limit: do 40 znaków
   EN: Downed by the Horns
   PL:
433. [[podstawowe] Pasywka wroga [804104] — opis] 머리가 파괴되면 다음 턴에 모든 부위가 흐트러짐 상태가 된다. 이후 이번 전투 동안 모든 부위가 공격 위력 감소 3을 얻는다.
   źródło: Passives_Abnormality.json :: dataList[id=804104].desc
   limit: do 190 znaków
   EN: When the head is broken, all parts become staggered next turn. Afterwards, all parts have 3 Attack Power Down for the duration of the battle.
   PL:
434. [[podstawowe] Pasywka wroga [804501] — nazwa] 살아있는 신경
   źródło: Passives_Abnormality.json :: dataList[id=804501].name
   limit: do 40 znaków
   EN: Living Nerves
   PL:
435. [[podstawowe] Pasywka wroga [804501] — opis] 죽음을 맞이하면 해당 턴 스킬 전부 취소.\n보유한 자가 충전 2배로 늘어남.
   źródło: Passives_Abnormality.json :: dataList[id=804501].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upon death, all Skills are cancelled for the turn.\nDoubles currently owned Self-charge.
   PL:
436. [[podstawowe] Pasywka wroga [804502] — nazwa] 움직이는 신경
   źródło: Passives_Abnormality.json :: dataList[id=804502].name
   limit: do 40 znaków
   EN: Motioning Nerves
   PL:
437. [[podstawowe] Pasywka wroga [804502] — opis] 죽음을 맞이한 후 공격 스킬당 자가 충전 1 소모.\n가지고 있는 자가 충전을 전부 소모하기 전까지 적을 공격함.
   źródło: Passives_Abnormality.json :: dataList[id=804502].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: After dying, attack skills spend 1 Self-charge.\nAttacks enemies until Self-charge runs out.
   PL:
438. [[podstawowe] Pasywka wroga [804503] — nazwa] 끈질긴 생명력
   źródło: Passives_Abnormality.json :: dataList[id=804503].name
   limit: do 40 znaków
   EN: Undying Persistence
   PL:
439. [[podstawowe] Pasywka wroga [804503] — opis] 5턴마다 머리 부위 체력만큼 보호막을 얻음.
   źródło: Passives_Abnormality.json :: dataList[id=804503].desc
   limit: do 120 znaków
   EN: Every 5 turns, gains a Shield equal to the head's HP.
   PL:
440. [[podstawowe] Pasywka wroga [804504] — nazwa] 끊겨버린 생명력
   źródło: Passives_Abnormality.json :: dataList[id=804504].name
   limit: do 40 znaków
   EN: Terminated Persistence
   PL:
441. [[podstawowe] Pasywka wroga [804504] — opis] 똬리틀기 사용 후 보호막을 전부 소모할 시 자가 충전 소모.\n모든 부위가 다음 턴에 흐트러짐 상태가 됨.
   źródło: Passives_Abnormality.json :: dataList[id=804504].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: After using 'Coil Up', if the Shield is exhausted, spend Self-charge.\nAll parts become staggered next turn.
   PL:
442. [[podstawowe] Pasywka wroga [804601] — nazwa] 부서진 우산
   źródło: Passives_Abnormality.json :: dataList[id=804601].name
   limit: do 40 znaków
   EN: Broken Umbrella
   PL:
443. [[podstawowe] Pasywka wroga [804601] — opis] 등 부위 파괴 시, 매 턴마다 취약 3 얻음. 파열 2 추가 부여
   źródło: Passives_Abnormality.json :: dataList[id=804601].desc
   limit: do 120 znaków
   EN: After the back is broken, gain 3 Fragile every turn. Inflict +2 Rupture.
   PL:
444. [[podstawowe] Pasywka wroga [804602] — nazwa] 다해진 우산
   źródło: Passives_Abnormality.json :: dataList[id=804602].name
   limit: do 40 znaków
   EN: Ragged Umbrella
   PL:
445. [[podstawowe] Pasywka wroga [804602] — opis] 머리 우산 부위 파괴 시, 매 턴마다 공격 레벨 감소 5 얻음, 침잠 2 추가 부여
   źródło: Passives_Abnormality.json :: dataList[id=804602].desc
   limit: do 120 znaków
   EN: After the head umbrella is broken, gain 5 Offense Level Down every turn. Inflict +2 Sinking.
   PL:
446. [[podstawowe] Pasywka wroga [804603] — nazwa] 마지막 발버둥
   źródło: Passives_Abnormality.json :: dataList[id=804603].name
   limit: do 40 znaków
   EN: Last Struggle
   PL:
447. [[podstawowe] Pasywka wroga [804603] — opis] 전체 체력의 15%만큼 남았다면, 매 턴마다 속도 1로 고정. 공격 위력 감소 1 얻음\n새로 소환된 낡은 우산 체력 30% 증가. 매 턴마다 무언가를 찾는 울음소리 사용
   źródło: Passives_Abnormality.json :: dataList[id=804603].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 15% HP, the unit's Speed is fixed at 1, and gains 1 Attack Power Down.\nNewly spawned Old Umbrellas have 30% more HP. Uses 'Cries Seeking Something' every turn.
   PL:
448. [[podstawowe] Pasywka wroga [804701] — nazwa] 옮겨붙는 불씨
   źródło: Passives_Abnormality.json :: dataList[id=804701].name
   limit: do 40 znaków
   EN: Spreading Ember
   PL:
449. [[podstawowe] Pasywka wroga [804701] — opis] 턴 종료 시 자신에게 화상이 있다면, 얽혀온 저주 부적을 가지고 있는 모든 대상에게 가지고 있는 화상만큼 다음 턴에 화상 부여
   źródło: Passives_Abnormality.json :: dataList[id=804701].desc
   limit: do 160 znaków
   EN: At the end of the turn, if this unit has Burn, inflict the same amount to all units with Entangled Curse Talisman next turn
   PL:
450. [[podstawowe] Pasywka wroga [804702] — nazwa] 부서진 수단
   źródło: Passives_Abnormality.json :: dataList[id=804702].name
   limit: do 40 znaków
   EN: Broken Means
   PL:
451. [[podstawowe] Pasywka wroga [804702] — opis] 팔 부위 파괴 시, 팔이 가하는 피해량 - 20%
   źródło: Passives_Abnormality.json :: dataList[id=804702].desc
   limit: do 120 znaków
   EN: When the arm is broken, it deals -20% damage
   PL:
452. [[podstawowe] Pasywka wroga [804801] — nazwa] 취기가 딸꾹!
   źródło: Passives_Abnormality.json :: dataList[id=804801].name
   limit: do 40 znaków
   EN: Booze Makes You Hicc!
   PL:
453. [[podstawowe] Pasywka wroga [804801] — opis] 취기 5이상인 적에게 "이건 내가 먹어야지!"를 적중시켰다면, 흐트러짐 상태가 됨.
   źródło: Passives_Abnormality.json :: dataList[id=804801].desc
   limit: do 150 znaków
   EN: After using 'I'll Have This!' on enemies with 5+ Tipsy and successfully landing the attack, become staggered.
   PL:
454. [[podstawowe] Pasywka wroga [804802] — nazwa] 고양되는 내음이죠?
   źródło: Passives_Abnormality.json :: dataList[id=804802].name
   limit: do 40 znaków
   EN: Stimulating Smell, Isn't It?
   PL:
455. [[podstawowe] Pasywka wroga [804802] — opis] 내부에서 나는 알 수 없는 내음으로 고양감이 생김.\n웨이브 시작 시 무작위 수감자 한 명에게 고양 5 부여.
   źródło: Passives_Abnormality.json :: dataList[id=804802].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A mysterious smell from within boosts the spirit.\nA random Sinner gains 5 Morale Boost at the start of the wave.
   PL:
456. [[podstawowe] Pasywka wroga [805201] — nazwa] 버려진 낡은 우산
   źródło: Passives_Abnormality.json :: dataList[id=805201].name
   limit: do 40 znaków
   EN: Old and Abandoned
   PL:
457. [[podstawowe] Pasywka wroga [805201] — opis] 자신이 처치되면 다음 턴에 처치한 수감자 신속 2 얻음.\n떠돌이 여우의 모든 부위에 속박 2 부여. 우산 파편 1 부여.
   źródło: Passives_Abnormality.json :: dataList[id=805201].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When this unit is defeated, the Sinner that defeated it gains 2 Haste next turn.\nAll parts of Drifting Fox are inflicted with 2 Bind and 1 Umbrella Splinters.
   PL:
458. [[podstawowe] Pasywka wroga [804301] — nazwa] 위태로운 정신
   źródło: Passives_Abnormality.json :: dataList[id=804301].name
   limit: do 40 znaków
   EN: Perilous Mind
   PL:
459. [[podstawowe] Pasywka wroga [804301] — opis] 매 턴 종료 시 정신력이 10 감소
   źródło: Passives_Abnormality.json :: dataList[id=804301].desc
   limit: do 120 znaków
   EN: At the end of each turn, lose 10 SP.
   PL:
460. [[podstawowe] Pasywka wroga [804302] — nazwa] 위태로운 마음
   źródło: Passives_Abnormality.json :: dataList[id=804302].name
   limit: do 40 znaków
   EN: Perilous Heart
   PL:
461. [[podstawowe] Pasywka wroga [804302] — opis] 사기 저하 상태면 공격 위력 증가 2 , 속박 3을 얻음
   źródło: Passives_Abnormality.json :: dataList[id=804302].desc
   limit: do 120 znaków
   EN: While in low morale, gain 2 Attack Power Up and 3 Bind.
   PL:
462. [[podstawowe] Pasywka wroga [804303] — nazwa] 흐트러진 마음
   źródło: Passives_Abnormality.json :: dataList[id=804303].name
   limit: do 40 znaków
   EN: Faltering Heart
   PL:
463. [[podstawowe] Pasywka wroga [804303] — opis] 패닉 상태면 흐트러짐 상태가 됨
   źródło: Passives_Abnormality.json :: dataList[id=804303].desc
   limit: do 120 znaków
   EN: In panic, become staggered.
   PL:
464. [[podstawowe] Pasywka wroga [804304] — nazwa] 결의
   źródło: Passives_Abnormality.json :: dataList[id=804304].name
   limit: do 40 znaków
   EN: Determination
   PL:
465. [[podstawowe] Pasywka wroga [804304] — opis] 패닉 상태에서 돌아온 경우, 정신력을 최대로 회복하고, 신속 2, 공격 위력 증가 2를 얻음
   źródło: Passives_Abnormality.json :: dataList[id=804304].desc
   limit: do 120 znaków
   EN: When recovering from panic, fully heal SP, and gain 2 Haste and 2 Attack Power Up.
   PL:
466. [[podstawowe] Pasywka wroga [804305] — nazwa] 로보토미 E.G.O
   źródło: Passives_Abnormality.json :: dataList[id=804305].name
   limit: do 40 znaków
   EN: Lobotomy E.G.O
   PL:
467. [[podstawowe] Pasywka wroga [804305] — opis] 보호막 체력 1200을 가지고 전투 시작
   źródło: Passives_Abnormality.json :: dataList[id=804305].desc
   limit: do 120 znaków
   EN: Starts the battle with 1200 Shield HP
   PL:
468. [[podstawowe] Pasywka wroga [805301] — nazwa] 마음의 벽
   źródło: Passives_Abnormality.json :: dataList[id=805301].name
   limit: do 40 znaków
   EN: Walled Heart
   PL:
469. [[podstawowe] Pasywka wroga [805301] — opis] 이 유닛이 파괴될 때마다 동백의 침잠 횟수가 5 증가하고, 모든 수감자의 침잠 2 감소, 모든 수감자가 다음 턴에 보호 1, 공격 위력 증가 2를 얻음
   źródło: Passives_Abnormality.json :: dataList[id=805301].desc
   limit: do 230 znaków
   EN: Whenever this unit is broken, Dongbaek is inflicted with +5 Sinking Count, and all Sinners lose 2 Sinking Count; all Sinners gain 1 Protection and 2 Attack Power Up next turn.
   PL:
470. [[podstawowe] Pasywka wroga [804401] — nazwa] 만발
   źródło: Passives_Abnormality.json :: dataList[id=804401].name
   limit: do 40 znaków
   EN: Into Full Bloom
   PL:
471. [[podstawowe] Pasywka wroga [804401] — opis] 5턴 시작 시 성장 3을 보유한 곧 피어날 꽃 4개 생성
   źródło: Passives_Abnormality.json :: dataList[id=804401].desc
   limit: do 120 znaków
   EN: At the start of Turn 5, spawn 4 Soon-to-bloom Flowers with 3 Growing
   PL:
472. [[podstawowe] Pasywka wroga [804402] — nazwa] 흐드러지는 마음
   źródło: Passives_Abnormality.json :: dataList[id=804402].name
   limit: do 40 znaków
   EN: Flowering Mind
   PL:
473. [[podstawowe] Pasywka wroga [804402] — opis] 체력이 50% 이하가 되면 2페이즈로 넘어감. 2페이즈 전까지 체력이 50% 미만으로 감소하지 않음
   źródło: Passives_Abnormality.json :: dataList[id=804402].desc
   limit: do 130 znaków
   EN: When HP drops to 50%, proceeds to the next phase. HP does not go below 50% until the phase changes.
   PL:
474. [[podstawowe] Pasywka wroga [804403] — nazwa] 대결
   źródło: Passives_Abnormality.json :: dataList[id=804403].name
   limit: do 40 znaków
   EN: Dueling
   PL:
475. [[podstawowe] Pasywka wroga [804403] — opis] 체력이 50% 이하가 되면 특정 1명을 지정하는 특수 스킬 사용\n해당 턴 부터 다음 2턴 동안 흐트러짐, 패닉 상태가 되지 않음.\n대결 효과를 보유한 캐릭터가 이상이면, 동백이 공격 위력 증가 1을 얻음\n이상이 대결에서 승리한 경우, 다음 턴에 모든 아군이 피해량 증가 3을 얻음.\n동백이 대결에서 승리한 경우, 정신력을 최대로 회복함.
   źródło: Passives_Abnormality.json :: dataList[id=804403].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When HP falls below 50%, uses a special skill to target 1 unit, then becomes immune to Stagger and Panic for the next 2 turns.\nIf Yi Sang has 'Dueling', Dongbaek gains 1 Attack Power Up.\nIf Yi Sang wins the duel, all allies gain 3 Damage Up next turn.\nIf Dongbaek wins the duel, Dongbaek fully heals SP.
   PL:
476. [[podstawowe] Pasywka wroga [804404] — nazwa] 피어남의 대가
   źródło: Passives_Abnormality.json :: dataList[id=804404].name
   limit: do 40 znaków
   EN: Cost of Blooming
   PL:
477. [[podstawowe] Pasywka wroga [804404] — opis] 찬란한 봄바람 스킬의 합 패배 시 정신력 -10
   źródło: Passives_Abnormality.json :: dataList[id=804404].desc
   limit: do 120 znaków
   EN: If 'Magnificent Spring Breeze' loses in a clash, lose 10 SP
   PL:
478. [[podstawowe] Pasywka wroga [805401] — nazwa] 자라나는 꽃
   źródło: Passives_Abnormality.json :: dataList[id=805401].name
   limit: do 40 znaków
   EN: Growing Flower
   PL:
479. [[podstawowe] Pasywka wroga [805401] — opis] 성장 1을 보유하고 생성됨
   źródło: Passives_Abnormality.json :: dataList[id=805401].desc
   limit: do 120 znaków
   EN: Spawns with 1 Growing
   PL:
480. [[podstawowe] Pasywka wroga [804903] — nazwa] 자기 파괴
   źródło: Passives_Abnormality.json :: dataList[id=804903].name
   limit: do 40 znaków
   EN: Self Destruction
   PL:
481. [[podstawowe] Pasywka wroga [804903] — opis] 모든 스킬을 피아식별 없이 사용. 스킬 사용 시마다 최대 체력의 2%만큼 체력을 잃음
   źródło: Passives_Abnormality.json :: dataList[id=804903].desc
   limit: do 120 znaków
   EN: All skills target indiscriminately. With each skill used, this unit loses 2% of Max HP.
   PL:
482. [[podstawowe] Pasywka wroga [804904] — nazwa] 자기 구제
   źródło: Passives_Abnormality.json :: dataList[id=804904].name
   limit: do 40 znaków
   EN: Self Salvation
   PL:
483. [[podstawowe] Pasywka wroga [804904] — opis] 체력 회복 효과가 2배로 적용된다.
   źródło: Passives_Abnormality.json :: dataList[id=804904].desc
   limit: do 120 znaków
   EN: HP healing effects heal twice as much.
   PL:
484. [[podstawowe] Pasywka wroga [805601] — nazwa] 빛나는 허영
   źródło: Passives_Abnormality.json :: dataList[id=805601].name
   limit: do 40 znaków
   EN: Radiant Vanity
   PL:
485. [[podstawowe] Pasywka wroga [805601] — opis] 이 유닛이 살아있으면 턴 시작 시 동랑에게 보호 1, 공격 위력 증가 1을 부여함
   źródło: Passives_Abnormality.json :: dataList[id=805601].desc
   limit: do 140 znaków
   EN: While this unit is present, Dongrang gains 1 Protection and 1 Attack Power Up at the start of each turn.
   PL:
486. [[podstawowe] Pasywka wroga [805602] — nazwa] 간절한 성과
   źródło: Passives_Abnormality.json :: dataList[id=805602].name
   limit: do 40 znaków
   EN: Earnest Accomplishment
   PL:
487. [[podstawowe] Pasywka wroga [805602] — opis] 이 유닛에 간절한 성과 가 있을 때 아래의 효과가 적용된다.\n- 동랑의 공격으로만 처치 가능.\n- 수감자가 이 유닛의 체력을 1로 만들면, 수감자가 체력을 회복하고 이 유닛이 공허한 영예 를 얻음\n- 동랑이 이 유닛을 처치하면, 동랑이 체력을 회복한 뒤 다음 턴에 강화됨
   źródło: Passives_Abnormality.json :: dataList[id=805602].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: While this unit has Earnest Accomplishment, the following effects apply:\n- Can only be defeated with Dongrang's attacks.\n- If a Sinner drops this unit's HP to 1, the Sinner heals HP, and this unit gains Empty Honor.\n- If Dongrang defeats this unit, Dongrang heals HP and powers up next turn.
   PL:
488. [[podstawowe] Pasywka wroga [805603] — nazwa] 공허한 영예
   źródło: Passives_Abnormality.json :: dataList[id=805603].name
   limit: do 40 znaków
   EN: Empty Honor
   PL:
489. [[podstawowe] Pasywka wroga [805603] — opis] 이 유닛에 공허한 영예 가 있을 때 아래의 효과가 적용된다.\n- 동랑의 공격으로만 처치 가능.\n- 동랑이 처치하면, 동랑이 체력을 잃은 뒤 공허함 1을 얻고 다음 턴에 약화됨
   źródło: Passives_Abnormality.json :: dataList[id=805603].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: While this unit has Empty Honor, the following effects apply:\n- Can only be defeated with Dongrang's attacks.\n- If Dongrang defeats this unit, Dongrang loses HP, gains 1 Emptiness, and is weakened next turn
   PL:
490. [[podstawowe] Pasywka wroga [805701] — nazwa] 맺힌 결실
   źródło: Passives_Abnormality.json :: dataList[id=805701].name
   limit: do 40 znaków
   EN: Borne Fruition
   PL:
491. [[podstawowe] Pasywka wroga [805701] — opis] 이 유닛을 처치한 대상은 체력을 최대 체력의 5%만큼 회복하고, 다음 턴에 신속 1, 공격 위력 증가 1을 얻음
   źródło: Passives_Abnormality.json :: dataList[id=805701].desc
   limit: do 140 znaków
   EN: The unit that defeated this unit heals by 5% of Max HP, and gains 1 Haste and 1 Attack Power Up next turn
   PL:
492. [[podstawowe] Pasywka wroga [805001] — nazwa] 이상을 항하여
   źródło: Passives_Abnormality.json :: dataList[id=805001].name
   limit: do 40 znaków
   EN: Toward the Ideal
   PL:
493. [[podstawowe] Pasywka wroga [805001] — opis] 현재 체력이 최대 체력의 85%, 50%가 될 때마다 욕망의 나무 2개를 생성하고, 스킬 패턴이 변경됨
   źródło: Passives_Abnormality.json :: dataList[id=805001].desc
   limit: do 150 znaków
   EN: When the HP is brought to 85% and 50% of Max HP, respectively, spawns 2 Trees of Desires and changes behavior.
   PL:
494. [[podstawowe] Pasywka wroga [806001] — nazwa] 빛나는 욕망
   źródło: Passives_Abnormality.json :: dataList[id=806001].name
   limit: do 40 znaków
   EN: Radiant Desire
   PL:
495. [[podstawowe] Pasywka wroga [806001] — opis] 이 유닛이 살아있으면 동랑이 턴 시작 시 피해량 증가, 보호 1을 얻음
   źródło: Passives_Abnormality.json :: dataList[id=806001].desc
   limit: do 130 znaków
   EN: While this unit is present, Dongrang gains 1 Damage Up and 1 Protection at the start of each turn.
   PL:
496. [[podstawowe] Pasywka wroga [805004] — nazwa] 등돌림의 대가
   źródło: Passives_Abnormality.json :: dataList[id=805004].name
   limit: do 40 znaków
   EN: Price of Neglect
   PL:
497. [[podstawowe] Pasywka wroga [805004] — opis] 수확의 시간 스킬의 합 패배 시 정신력 -5
   źródło: Passives_Abnormality.json :: dataList[id=805004].desc
   limit: do 120 znaków
   EN: If 'Time of Harvest' loses in a clash, lose 5 SP
   PL:
498. [[podstawowe] Pasywka wroga [805005] — nazwa] 비릿한 웃음
   źródło: Passives_Abnormality.json :: dataList[id=805005].name
   limit: do 40 znaków
   EN: Bitter Smile
   PL:
499. [[podstawowe] Pasywka wroga [805005] — opis] 패닉 상태가 되면, 다음 턴 시작 시 보호 2를 얻고 정신력이 0으로 돌아옴
   źródło: Passives_Abnormality.json :: dataList[id=805005].desc
   limit: do 120 znaków
   EN: When in panic, gain 2 Protection and reset SP to 0 at the start of the next turn.
   PL:
500. [[podstawowe] Pasywka wroga [805006] — nazwa] 비효율적인 판단
   źródło: Passives_Abnormality.json :: dataList[id=805006].name
   limit: do 40 znaków
   EN: Inefficient Judgement
   PL:
501. [[podstawowe] Pasywka wroga [805006] — opis] 흐트러짐 상태에서 돌아올 때 공격 위력 증가 1을 얻음
   źródło: Passives_Abnormality.json :: dataList[id=805006].desc
   limit: do 120 znaków
   EN: When recovering from stagger, gain 1 Attack Power Up.
   PL:
502. [[podstawowe] Pasywka wroga [805007] — nazwa] 체력 소모
   źródło: Passives_Abnormality.json :: dataList[id=805007].name
   limit: do 40 znaków
   EN: Exhausting Endeavor
   PL:
503. [[podstawowe] Pasywka wroga [805007] — opis] 양분이 되어주세요 스킬을 3번 사용하면 다음 턴에 흐트러짐 상태가 됨
   źródło: Passives_Abnormality.json :: dataList[id=805007].desc
   limit: do 120 znaków
   EN: After using the skill Please Be My Nutrient 3 times, become staggered next turn.
   PL:
504. [[podstawowe] Pasywka wroga [805002] — nazwa] 이상을 항하여
   źródło: Passives_Abnormality.json :: dataList[id=805002].name
   (powtórzenie elementu 492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [[podstawowe] Pasywka wroga [805002] — opis] 현재 체력이 최대 체력의 85%가 되면 욕망의 나무 2개를 생성하고, 스킬 패턴이 변경됨
   źródło: Passives_Abnormality.json :: dataList[id=805002].desc
   limit: do 120 znaków
   EN: When the HP is brought to 85% of Max HP, spawns 2 Trees of Desires and changes behavior.
   PL:
506. [[podstawowe] Pasywka wroga [805003] — nazwa] 이상을 항하여
   źródło: Passives_Abnormality.json :: dataList[id=805003].name
   (powtórzenie elementu 492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [[podstawowe] Pasywka wroga [805003] — opis] 현재 체력이 최대 체력의 50%가 되면 욕망의 나무 2개를 생성하고, 스킬 패턴이 변경됨
   źródło: Passives_Abnormality.json :: dataList[id=805003].desc
   limit: do 120 znaków
   EN: When the HP is brought to 50% of Max HP, spawns 2 Trees of Desires and changes behavior.
   PL:
508. [[podstawowe] Pasywka wroga [805801] — nazwa] 미끼 요정
   źródło: Passives_Abnormality.json :: dataList[id=805801].name
   limit: do 40 znaków
   EN: Fairy Lure
   PL:
509. [[podstawowe] Pasywka wroga [805801] — opis] 요정 공격 시, 해당 부위 체력만 감소함.
   źródło: Passives_Abnormality.json :: dataList[id=805801].desc
   limit: do 120 znaków
   EN: When the fairy is attacked, only that part loses HP.
   PL:
510. [[podstawowe] Pasywka wroga [805802] — nazwa] 드러난 밑동
   źródło: Passives_Abnormality.json :: dataList[id=805802].name
   limit: do 40 znaków
   EN: Exposed Base
   PL:
511. [[podstawowe] Pasywka wroga [805802] — opis] 요정 부위 파괴 시, 다음 턴에 뿌리 공격 가능 상태가 됨.\n모든 부위에 다음 턴에 공격 위력 증가 1, 속박 2, 취약 3을 얻음.
   źródło: Passives_Abnormality.json :: dataList[id=805802].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the fairy part is broken, the roots can be attacked next turn.\nAll parts gain 1 Attack Power Up, 2 Bind, and 3 Fragile next turn.
   PL:
512. [[podstawowe] Pasywka wroga [805803] — nazwa] 여분의 미끼
   źródło: Passives_Abnormality.json :: dataList[id=805803].name
   limit: do 40 znaków
   EN: Spare Lure
   PL:
513. [[podstawowe] Pasywka wroga [805803] — opis] 뿌리가 드러난 다음 턴에 요정 다시 생성. (최대 1번)\n뿌리가 3번 드러나거나 파괴된다면 광폭화 상태가 됨.
   źródło: Passives_Abnormality.json :: dataList[id=805803].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The fairy regenerates the turn after the roots are exposed. (One time only)\nAfter the roots are exposed 3 times or destroyed, the unit is enraged.
   PL:
514. [[podstawowe] Pasywka wroga [805804] — nazwa] 발견되는 취약점
   źródło: Passives_Abnormality.json :: dataList[id=805804].name
   limit: do 40 znaków
   EN: Discovered Weakness
   PL:
515. [[podstawowe] Pasywka wroga [805804] — opis] 요정이 진동을 가지고 있다면, 위력만큼 턴 종료 시 요정이 피해를 입음 (최대 20)
   źródło: Passives_Abnormality.json :: dataList[id=805804].desc
   limit: do 120 znaków
   EN: If the fairy has Tremor, it takes damage by its Potency at the end of the turn. (Max 20)
   PL:
516. [[podstawowe] Pasywka wroga [805805] — nazwa] 이어지는 취약점
   źródło: Passives_Abnormality.json :: dataList[id=805805].name
   limit: do 40 znaków
   EN: Connected Weakness
   PL:
517. [[podstawowe] Pasywka wroga [805805] — opis] 부위에 화상을 가지고 있다면 위력만큼 받는 피해량 증가 (최대 +15%)
   źródło: Passives_Abnormality.json :: dataList[id=805805].desc
   limit: do 120 znaków
   EN: If the part has Burn, it takes more damage based on its Potency. (Max +15%)
   PL:
518. [[podstawowe] Pasywka wroga [805901] — nazwa] 만들어진 휴식
   źródło: Passives_Abnormality.json :: dataList[id=805901].name
   limit: do 40 znaków
   EN: Manufactured Respite
   PL:
519. [[podstawowe] Pasywka wroga [805901] — opis] 거대 클로버가 살아있다면, 턴 종료 시 자신의 체력 30 회복
   źródło: Passives_Abnormality.json :: dataList[id=805901].desc
   limit: do 120 znaków
   EN: If the giant clover is present, this unit heals 30 HP at the end of the turn.
   PL:
520. [[podstawowe] Pasywka wroga [805902] — nazwa] 잃어버린 수단
   źródło: Passives_Abnormality.json :: dataList[id=805902].name
   limit: do 40 znaków
   EN: Lost Means
   PL:
521. [[podstawowe] Pasywka wroga [805902] — opis] 팔 부위 파괴 시, 매 턴마다 공격 위력 감소 2 얻음
   źródło: Passives_Abnormality.json :: dataList[id=805902].desc
   limit: do 120 znaków
   EN: When the arm is broken, the unit gains 2 Attack Power Down every turn.
   PL:
522. [[podstawowe] Pasywka wroga [805903] — nazwa] 훼손된 그늘
   źródło: Passives_Abnormality.json :: dataList[id=805903].name
   limit: do 40 znaków
   EN: Damaged Shade
   PL:
523. [[podstawowe] Pasywka wroga [805903] — opis] 머리 부위 파괴 시, 매 턴마다 방어 레벨 감소 4, 취약 1 얻음
   źródło: Passives_Abnormality.json :: dataList[id=805903].desc
   limit: do 120 znaków
   EN: When the head is broken, the unit gains 4 Defense Level Down and 1 Fragile every turn.
   PL:
524. [[podstawowe] Pasywka wroga [806201] — nazwa] 오염시키는 잎사귀
   źródło: Passives_Abnormality.json :: dataList[id=806201].name
   limit: do 40 znaków
   EN: Contaminating Leaf
   PL:
525. [[podstawowe] Pasywka wroga [806201] — opis] 매 턴 시작시 키다리 요정에게 회복량 증가 1, 공격 위력 1 증가를 부여함.
   źródło: Passives_Abnormality.json :: dataList[id=806201].desc
   limit: do 120 znaków
   EN: At the start of the turn, give 1 HP Healing Boost and 1 Attack Power Up to Fairy-Long-Legs.
   PL:
526. [[podstawowe] Pasywka wroga [80620101] — nazwa] 오염시키는 잎사귀
   źródło: Passives_Abnormality.json :: dataList[id=80620101].name
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [[podstawowe] Pasywka wroga [80620101] — opis] 매 턴 시작시 키다리 요정에게 회복량 증가 1, 공격 위력 1 증가를 부여함.
   źródło: Passives_Abnormality.json :: dataList[id=80620101].desc
   (powtórzenie elementu 525 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [[podstawowe] Pasywka wroga [826301] — nazwa] 잠깐의 배부름
   źródło: Passives_Abnormality.json :: dataList[id=826301].name
   limit: do 40 znaków
   EN: Momentary Satiation
   PL:
529. [[podstawowe] Pasywka wroga [826301] — opis] 턴 종료 시 [PreparedMeat]가 부여된 아군의 체력이 1이면, 해당 캐릭터를 처치하고 다음 턴에 모든 부위가 [Vulnerable] 5, [Reduction], [Disarming] 5를 얻음.
   źródło: Passives_Abnormality.json :: dataList[id=826301].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [PreparedMeat], [Vulnerable], [Reduction], [Disarming]
   znaczenie tagów: [PreparedMeat] = 준비된 고기 / Prepared Meat; [Vulnerable] = 취약 / Fragile; [Reduction] = 공격 위력 감소 / Attack Power Down; [Disarming] = 수비 위력 감소 / Defense Power Down
   EN: Turn End: If the ally with [PreparedMeat] is at 1 HP, kill the ally; then, all Parts gain 5 [Vulnerable], [Reduction], and [Disarming].
   PL:
530. [[podstawowe] Pasywka wroga [826302] — nazwa] 광포한 굶주림
   źródło: Passives_Abnormality.json :: dataList[id=826302].name
   limit: do 40 znaków
   EN: Ravening Hunger
   PL:
531. [[podstawowe] Pasywka wroga [826302] — opis] 턴 시작 시 체력이 25% 이하일 때 아군이 살아있으면, 모든 아군 처치.\n최대 체력의 (처치한 아군 수 x 5)% 만큼 본체의 체력 회복.\n아군이 없는 상태이면, 턴 종료 시 다음 턴에 [Enhancement] 20 얻음.
   źródło: Passives_Abnormality.json :: dataList[id=826302].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Turn Start: If there are surviving allies at 25%- HP, kill all allies.\nHeal (# of allies killed x 5)% of max Core HP.\nTurn End: If there are no surviving allies, gain 20 [Enhancement] next turn.
   PL:
532. [[podstawowe] Pasywka wroga [826303] — nazwa] 찢겨진 팔
   źródło: Passives_Abnormality.json :: dataList[id=826303].name
   limit: do 40 znaków
   EN: Torn Arm
   PL:
533. [[podstawowe] Pasywka wroga [826303] — opis] 팔 부위가 파괴되면, 매 턴 시작 시 몸통 부위가 출혈 5 얻음.
   źródło: Passives_Abnormality.json :: dataList[id=826303].desc
   limit: do 120 znaków
   EN: When an Arm is broken, the Body gains 5 Bleed at every Turn Start.
   PL:
534. [[podstawowe] Pasywka wroga [826304] — nazwa] 식사 접대
   źródło: Passives_Abnormality.json :: dataList[id=826304].name
   limit: do 40 znaków
   EN: Invitation to a Meal
   PL:
535. [[podstawowe] Pasywka wroga [826304] — opis] 턴 종료 시 모든 수감자의 정신력 10 회복, 모든 속성의 EGO 자원 +1
   źródło: Passives_Abnormality.json :: dataList[id=826304].desc
   limit: do 120 znaków
   EN: Turn End: All Sinners heal 10 SP, and gain +1 E.G.O resource for all Affinities
   PL:
536. [[podstawowe] Pasywka wroga [826501] — nazwa] 텅 빈 배
   źródło: Passives_Abnormality.json :: dataList[id=826501].name
   limit: do 40 znaków
   EN: Empty Belly
   PL:
537. [[podstawowe] Pasywka wroga [826501] — opis] 턴 종료 시 [PreparedMeat]가 부여된 아군이 흐트러짐 상태면, 해당 캐릭터를 처치함.
   źródło: Passives_Abnormality.json :: dataList[id=826501].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PreparedMeat]
   znaczenie tagów: [PreparedMeat] = 준비된 고기 / Prepared Meat
   EN: Turn End: If the ally with [PreparedMeat] is Staggered, kill the ally.
   PL:
538. [[podstawowe] Pasywka wroga [826502] — nazwa] 채워지지 않는 허기
   źródło: Passives_Abnormality.json :: dataList[id=826502].name
   limit: do 40 znaków
   EN: Bottomless Hunger
   PL:
539. [[podstawowe] Pasywka wroga [826502] — opis] 아군 처치 시 본체의 체력 20 회복, 다음 턴에 [Vulnerable] 1 얻음.
   źródło: Passives_Abnormality.json :: dataList[id=826502].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: After defeating an ally, heal 20 Core HP; then, gain 1 [Vulnerable] next turn.
   PL:
540. [[podstawowe] Pasywka wroga [826503] — nazwa] 굶주림
   źródło: Passives_Abnormality.json :: dataList[id=826503].name
   limit: do 40 znaków
   EN: Hunger
   PL:
541. [[podstawowe] Pasywka wroga [826503] — opis] 턴 종료 시 준비된 고기가 부여된 아군을 처치하지 못했으면 [Hunger] 1 증가. 체력이 75% 미만이면, 2 증가, 체력이 50% 미만이면, 3 증가.\n턴 시작 시 [PreparedMeat]가 부여된 아군을 처치했으면, [Hunger] 1 감소.
   źródło: Passives_Abnormality.json :: dataList[id=826503].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Hunger], [PreparedMeat]
   znaczenie tagów: [Hunger] = 굶주림 / Hunger; [PreparedMeat] = 준비된 고기 / Prepared Meat
   EN: Turn End: If this unit failed to defeat an ally with Prepared Meat, gain 1 [Hunger]. At 75%- HP, gain 2. At 50%- HP, gain 3.\nTurn Start: If this unit defeated an ally with Prepared Meat, lose 1 [Hunger].
   PL:
542. [[podstawowe] Pasywka wroga [826504] — nazwa] 잠깐의 배부름
   źródło: Passives_Abnormality.json :: dataList[id=826504].name
   (powtórzenie elementu 528 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [[podstawowe] Pasywka wroga [826504] — opis] 턴 종료 시 [Hunger]이 0이면, 다음 턴에 [AttackDown], [DefenseDown]를 (이번 턴에 처치한 아군 수 x 3)만큼 얻음.
   źródło: Passives_Abnormality.json :: dataList[id=826504].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Hunger], [AttackDown], [DefenseDown]
   znaczenie tagów: [Hunger] = 굶주림 / Hunger; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn End: At 0 [Hunger], gain (allies defeated this turn x 3) [AttackDown] and [DefenseDown].
   PL:
544. [[podstawowe] Pasywka wroga [826505] — nazwa] 광포한 굶주림
   źródło: Passives_Abnormality.json :: dataList[id=826505].name
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [[podstawowe] Pasywka wroga [826505] — opis] 턴 종료 시 [Hunger]이 4이면, 다음 턴에 강한 스킬 패턴으로 변경됨.
   źródło: Passives_Abnormality.json :: dataList[id=826505].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Hunger]
   znaczenie tagów: [Hunger] = 굶주림 / Hunger
   EN: Turn End: At 4 [Hunger], gain a stronger pattern.
   PL:
546. [[podstawowe] Pasywka wroga [811801] — nazwa] 돌아오는 과거
   źródło: Passives_Abnormality.json :: dataList[id=811801].name
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [[podstawowe] Pasywka wroga [811801] — opis] [AccumulatedPastMirror]가 50 이상이면, 본체 체력이 80% 이하일 때 턴 종료 시 [AccumulatedPastMirror]를 소모하여 본체 체력을 200 회복함.
   źródło: Passives_Abnormality.json :: dataList[id=811801].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [AccumulatedPastMirror]
   znaczenie tagów: [AccumulatedPastMirror] = 축적된 과거 / Accumulated Past
   EN: If at 50+ [AccumulatedPastMirror], and if Core's HP is less than or equal to 80%, Core gains 200 HP by spending 50 [AccumulatedPastMirror] at Turn End
   PL:
548. [[podstawowe] Pasywka wroga [811802] — nazwa] 소실된 과거
   źródło: Passives_Abnormality.json :: dataList[id=811802].name
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [[podstawowe] Pasywka wroga [811802] — opis] 몸통 부위 파괴 시, 축적된 과거 전부 소모.\n몸통 부위 파괴 시, 다음 턴부터 이번 전투동안 몸통 부위가 모든 속성과 공격 유형에 대하여 내성(0.5)이 됨.
   źródło: Passives_Abnormality.json :: dataList[id=811802].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the body is broken, spend all Accumulated Past.\nWhen the body is broken, all Attack Types and Affinities become ineffective(0.5) against the body starting next turn until the end of this encounter.
   PL:
550. [[podstawowe] Pasywka wroga [811808] — nazwa] 메트로놈
   źródło: Passives_Abnormality.json :: dataList[id=811808].name
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [[podstawowe] Pasywka wroga [811808] — opis] [AccumulatedPastMirror]가 홀수이면 [Vulnerable]과 [AttackDmgUp]를 3 얻음\n짝수이면, [Protection]와 [AttackDmgDown]를 3 얻음
   źródło: Passives_Abnormality.json :: dataList[id=811808].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [[podstawowe] Pasywka wroga [826401] — nazwa] 보살핌
   źródło: Passives_Abnormality.json :: dataList[id=826401].name
   limit: do 40 znaków
   EN: Care
   PL:
553. [[podstawowe] Pasywka wroga [826401] — opis] 턴 시작 시 최대 체력의 15%만큼 체력 회복
   źródło: Passives_Abnormality.json :: dataList[id=826401].desc
   limit: do 120 znaków
   EN: Turn Start: Heal 15% of max HP
   PL:
554. [[podstawowe] Pasywka wroga [826402] — nazwa] 신선도 유지
   źródło: Passives_Abnormality.json :: dataList[id=826402].name
   limit: do 40 znaków
   EN: Keep It Fresh
   PL:
555. [[podstawowe] Pasywka wroga [826402] — opis] 체력이 1 미만으로 감소하지 않음
   źródło: Passives_Abnormality.json :: dataList[id=826402].desc
   limit: do 120 znaków
   EN: HP does not drop below 1
   PL:
556. [[podstawowe] Pasywka wroga [124501] — nazwa] 여왕 호위
   źródło: Passives_Abnormality.json :: dataList[id=124501].name
   limit: do 40 znaków
   EN: The Queen's Defenders
   PL:
557. [[podstawowe] Pasywka wroga [124501] — opis] 자신이 공격을 받을 때 스킬 피해의 70% 만큼 받지 않고 스킬당 랜덤 아군 한명을 지정하여 아군에게 해당 수치만큼 피해를 입힘\n([PreparedMeat]가 있는 아군 우선 적용, 아군이 없을 때 발동하지 않음, 이 피해로 아군이 사망하지 않음)
   źródło: Passives_Abnormality.json :: dataList[id=124501].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [PreparedMeat]
   znaczenie tagów: [PreparedMeat] = 준비된 고기 / Prepared Meat
   EN: When this unit gets attacked, take -70% Skill damage, and transfer that Skill's damage to a random ally.\n(Prioritizes allies with [PreparedMeat]; does not activate if there are no allies; this damage does not kill the affected allies)
   PL:

## [podstawowe] Pasywka wroga: Passives_Abnormality91-4
- plik gry: `Passives_Abnormality91-4.json`

558. [[podstawowe] Pasywka wroga [806301] — nazwa] 흉포한 산성 갑각
   źródło: Passives_Abnormality91-4.json :: dataList[id=806301].name
   limit: do 40 znaków
   EN: Ferocious Acidic Crust
   PL:
559. [[podstawowe] Pasywka wroga [806301] — opis] 머리 부위 파괴 시 부위 스킬 최종 위력 -2
   źródło: Passives_Abnormality91-4.json :: dataList[id=806301].desc
   limit: do 120 znaków
   EN: When the head is broken, the part has -2 Skill Final Power
   PL:
560. [[podstawowe] Pasywka wroga [806302] — nazwa] 탈취한 파열성 소라
   źródło: Passives_Abnormality91-4.json :: dataList[id=806302].name
   limit: do 40 znaków
   EN: Stolen Rupturing Shell
   PL:
561. [[podstawowe] Pasywka wroga [806302] — opis] 소라 부위 파괴 시 부위 스킬의 최종 위력 -2
   źródło: Passives_Abnormality91-4.json :: dataList[id=806302].desc
   limit: do 120 znaków
   EN: When the shell is broken, the part has -2 Skill Final Power
   PL:
562. [[podstawowe] Pasywka wroga [806303] — nazwa] 긴급 영양 보급
   źródło: Passives_Abnormality91-4.json :: dataList[id=806303].name
   limit: do 40 znaków
   EN: Emergency Nutrient Supply
   PL:
563. [[podstawowe] Pasywka wroga [806303] — opis] 자신의 공격으로 아군 처치 시 체력을 최대 체력의 5%만큼 회복\n턴 종료 시, 이 효과로 체력을 최대 체력의 15%만큼 회복한 경우, 다음 턴에 소라 부위 재생.
   źródło: Passives_Abnormality91-4.json :: dataList[id=806303].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: After this unit defeats its ally, heal by 5% of Max HP.\nAt the end of the turn, if this unit has healed 15% of Max HP with the above effect, restore the shell.
   PL:
564. [[podstawowe] Pasywka wroga [806304] — nazwa] 게판
   źródło: Passives_Abnormality91-4.json :: dataList[id=806304].name
   limit: do 40 znaków
   EN: A Crab-eat-crab World
   PL:
565. [[podstawowe] Pasywka wroga [806304] — opis] 자신이 체력이 70% 미만이면, 마구 마구 찍기, 세게! 찍기, 게거품 스킬이 현재 체력이 자신을 제외하고 가장 낮은 아군을 지정함\n아군 공격 시 피해량만큼 체력 회복.\n아군 처치 시 피해량의 2배만큼 체력 회복.
   źródło: Passives_Abnormality91-4.json :: dataList[id=806304].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At less than 70% HP, Brutal Pummelling, Powerful! Pummel, and Foaming skills target another ally with the least current HP.\nWhen attacking an ally, heals HP by the damage dealt.\nWhen defeating an ally, heals HP by double the damage dealt.
   PL:
566. [[podstawowe] Pasywka wroga [806305] — nazwa] 거대한 위용
   źródło: Passives_Abnormality91-4.json :: dataList[id=806305].name
   limit: do 40 znaków
   EN: Looming Presence
   PL:
567. [[podstawowe] Pasywka wroga [806305] — opis] 턴 시작 시 모든 적의 정신력 -10
   źródło: Passives_Abnormality91-4.json :: dataList[id=806305].desc
   limit: do 120 znaków
   EN: Turn Start: All enemies lose 10 SP
   PL:

## [podstawowe] Pasywka wroga: Passives_Enemy-mr7-extreme
- plik gry: `Passives_Enemy-mr7-extreme.json`

568. [[podstawowe] Pasywka wroga [7104701] — nazwa] HP탄
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7104701].name
   limit: do 40 znaków
   EN: HP Bullets
   PL:
569. [[podstawowe] Pasywka wroga [7104701] — opis] 턴 시작 시 체력 3% 회복\n체력이 50% 미만이면 체력 5% 추가 회복
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7104701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: heal 3% HP\nAt less than 50% HP, heal 5% additional HP
   PL:
570. [[podstawowe] Pasywka wroga [7105001] — nazwa] 과부하 HP탄
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105001].name
   limit: do 40 znaków
   EN: Overloaded HP Bullet
   PL:
571. [[podstawowe] Pasywka wroga [7105001] — opis] 턴 시작 시, [AttackDmgUp] 2, [Vulnerable] 2 얻음.
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: Gain 2 [AttackDmgUp] and 2 [Vulnerable].
   PL:
572. [[podstawowe] Pasywka wroga [7105002] — nazwa] HP 앰플 주입
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105002].name
   limit: do 40 znaków
   EN: HP Ampule Injection
   PL:
573. [[podstawowe] Pasywka wroga [7105002] — opis] 턴 시작 시, 체력이 소모되어 있다면 전체 체력의 25% 회복 (최대 3회)
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105002].desc
   limit: do 120 znaków
   EN: Turn Start: if this unit's HP is not at full, heal 25% HP (3 times max)
   PL:
574. [[podstawowe] Pasywka wroga [7105101] — nazwa] HP탄
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105101].name
   (powtórzenie elementu 568 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [[podstawowe] Pasywka wroga [7105101] — opis] 턴 시작 시 체력 3% 회복\n체력이 50% 미만이면 체력 5% 추가 회복
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105101].desc
   (powtórzenie elementu 569 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [[podstawowe] Pasywka wroga [7105102] — nazwa] 탱고 양념장
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105102].name
   limit: do 40 znaków
   EN: Tango Marinade
   PL:
577. [[podstawowe] Pasywka wroga [7105102] — opis] 대상보다 체력이 높다면, 합 위력 (대상과의 체력 차이 / 50) 만큼 추가 (최대 3)\n합 위력 증가[TabExplain] 효과를 받았으면, 공격 종료 후 [Vulnerable] 1 얻음
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105102].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain], [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: If this unit has more HP than the target, gain Clash Power +(HP difference / 50) (max 3)\nIf this unit gained Clash Power from the above effect, gain 1 [Vulnerable] after Attack End
   PL:
578. [[podstawowe] Pasywka wroga [7105501] — nazwa] HP탄
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105501].name
   (powtórzenie elementu 568 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [[podstawowe] Pasywka wroga [7105501] — opis] 턴 시작 시 체력 3% 회복\n체력이 50% 미만이면 체력 5% 추가 회복
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105501].desc
   (powtórzenie elementu 569 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [[podstawowe] Pasywka wroga [7105502] — nazwa] 흘러오는 우울
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105502].name
   limit: do 40 znaków
   EN: Floods of Sorrow
   PL:
581. [[podstawowe] Pasywka wroga [7105502] — opis] 뒷면 적중 시 [Sinking] 3 부여
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105502].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: On Tails Hit, inflict 3 [Sinking]
   PL:
582. [[podstawowe] Pasywka wroga [7105503] — nazwa] 넘쳐흐르는 슬픔
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105503].name
   limit: do 40 znaków
   EN: Overflowing Sorrow
   PL:
583. [[podstawowe] Pasywka wroga [7105503] — opis] 턴 종료 시, 자신의 정신력 5 감소
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105503].desc
   limit: do 120 znaków
   EN: Turn End: Lose 5 SP
   PL:
584. [[podstawowe] Pasywka wroga [7105701] — nazwa] 회복 앰플 주입
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105701].name
   limit: do 40 znaków
   EN: Healing Ampule Injection
   PL:
585. [[podstawowe] Pasywka wroga [7105701] — opis] 턴 시작 시 체력 5% 회복
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105701].desc
   limit: do 120 znaków
   EN: Turn Start: Heal 5% HP.
   PL:
586. [[podstawowe] Pasywka wroga [7105801] — nazwa] 과부하 HP탄
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105801].name
   (powtórzenie elementu 570 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [[podstawowe] Pasywka wroga [7105801] — opis] 턴 시작시, [AttackDmgUp]2, [Vulnerable] 2 얻음
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: Gain 2 [AttackDmgUp] and 2 [Vulnerable]
   PL:
588. [[podstawowe] Pasywka wroga [7105802] — nazwa] 긴급 앰플 투약
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105802].name
   limit: do 50 znaków
   EN: Emergency Ampule Administration
   PL:
589. [[podstawowe] Pasywka wroga [7105802] — opis] 체력이 25% 미만이면 전체 체력의 40%까지 회복 (최대 1회)
   źródło: Passives_Enemy-mr7-extreme.json :: dataList[id=7105802].desc
   limit: do 120 znaków
   EN: At less than 25% HP, heal up to 40% of max HP (1 time max)
   PL:

## [podstawowe] Pasywka wroga: Passives_Enemy-schema
- plik gry: `Passives_Enemy-schema.json`

590. [[podstawowe] Pasywka wroga [600201] — nazwa] 도상구축
   źródło: Passives_Enemy-schema.json :: dataList[id=600201].name
   limit: do 40 znaków
   EN: Schemacraft
   PL:
591. [[podstawowe] Pasywka wroga [600201] — opis] [PanicChangeLock] 효과가 적용되며,\n정신력이 0 미만으로 내려가지 않음\n\n이번 전투에서 흑운회 제3조장 미네에게 다음 효과 적용\n- <color=#ff6000><mark=#ff000040><b><u>참격 속성 E.G.O 스킬과 합 진행 시, 합 위력 -5</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>참격 속성 E.G.O 스킬로 받는 피해량 +(150/코인 수)%</u></b></mark></color>
   źródło: Passives_Enemy-schema.json :: dataList[id=600201].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [PanicChangeLock]
   znaczenie tagów: [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic
   EN: Apply the [PanicChangeLock] effect\n\nSP does not drop below 0\n\nIn this Encounter, apply the following effects on Mine, Patriarch of the Kurokumo Clan's Third Family:\n- <color=#ff6000><mark=#ff000040><b><u>In a Clash against Slash E.G.O Skills, Clash Power -5</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>Take +(150 / # of Coins)% damage from Slash E.G.O Skills</u></b></mark></color>
   PL:
592. [[podstawowe] Pasywka wroga [600201] — tekst klimatyczny] “도상적으로 구축된 표상. 이 훈련을 통해 많은 걸 체험해볼 수 있을 거야. 특히 관리자, 당신은 유독 이 훈련에 잘 맞거든.”\n“시지프 탑이 건재했다면, 당신의 시스템은 어떤 모습이었을까?”
   źródło: Passives_Enemy-schema.json :: dataList[id=600201].flavor
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "A series of representations, crafted in groupings of schema. There's a great deal you can experience through this training, so.. bon courage, Manager. You in particular, well... I must say this suits you especially well."\n\n"If Sisyphe Tower were still standing, I wonder what form your iteration of the system would've taken?"
   PL:
593. [[podstawowe] Pasywka wroga [600202] — nazwa] 발도술[쿠로쿠모]
   źródło: Passives_Enemy-schema.json :: dataList[id=600202].name
   limit: do 40 znaków
   EN: Battōjutsu [Kurokumo]
   PL:
594. [[podstawowe] Pasywka wroga [600202] — opis] 세 번째 턴 시작 시, 스킬 슬롯에 ‘발도 자세’를 장착하고 이번 턴 동안 반복하여 사용\n- 해당 턴 시작 시, (25 + 자신의 잃은 체력 비율/2)만큼 [SharpSensibility] 얻음 (소수점 버림)\n- 해당 턴 동안 <color=#ff6000><mark=#ff000040><b><u>수감자의 기본 공격 가중치가 1인 E.G.O 스킬에 1회 피격되면, ‘발도 자세’가 취소되고</u></b></mark></color> 다음 효과 적용\n(피격 판정은 스킬당 1회)\n· [SharpSensibility]가 0으로 변경됨\n· 모든 E.G.O 자원 +1\n· 다음 턴 동안 [Vulnerable] 5 얻고 ‘쿠모기리’와 ‘공간참’의 합 위력 -5\n- 이후 두 턴마다 반복하며, <color=#ff6000><mark=#ff000040><b><u>패턴을 반복할 때마다 취소에 필요한 피격 횟수 +1 (최대 +3)</u></b></mark></color>\n\n‘발도 자세’를 장착한 턴 종료 이후 다음 턴 시작 시, ‘쿠모기리’ 사용\n\n이번 전투에서 처음으로 체력이 50% 이하가 되었을 때 턴이 즉시 종료되고,\n자신과 쥰을 제외한 자신 진영 흑운회 소속이 다섯 미만이면, 능숙한 흑운회 조직원, 나른한 흑운회 조직원을 합하여 다섯 명까지 불러옴 (새롭게 등장한 적들은 정신력이 30인 상태로 등장)\n\n패턴 변경 이후로는 다음의 효과가 적용됨\n- 가하는 피해량 +(자신의 잃은 체력 비율)% (최대 100%)\n- ‘쿠모기리’가 ‘공간참’으로 변경됨
   źródło: Passives_Enemy-schema.json :: dataList[id=600202].desc
   limit: do 1590 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [SharpSensibility], [Vulnerable]
   znaczenie tagów: [SharpSensibility] = 칼질의 재미 / Delightful Swordbutchery; [Vulnerable] = 취약 / Fragile
   EN: Turn 3 Start: This unit equips "Battō Shisei" in its Skill Slots and uses it repeatedly during this turn\n- Said Turn Start: Gain (25 + (missing HP percentage on self) / 2)[SharpSensibility] (rounded down)\n- During said turn, <color=#ff6000><mark=#ff000040><b><u>when hit once by a Sinner's E.G.O Skill with 1 base Atk Weight, cancel "Ready to Draw"</u></b></mark></color> and activate the following effects (each Skill only counts as hitting once):\n  · Change [SharpSensibility] to 0\n  · Gain +1 for all E.G.O Resource\n  · Gain 5 [Vulnerable] for the next turn; Clash Power -5 for "Kumogiri" and "Rend Space"\n- Repeat the above every 2 turns. <color=#ff6000><mark=#ff000040><b><u>Every time this unit enters this pattern, +1 to the number of hits required to cancel "Ready to Draw" (max +3)</u></b></mark></color>\n\nTurn Start: If this unit had "Battō Shisei" equipped at last Turn End, use "Kumogiri"\n\nWhen this unit's HP drops to 50% or below for the first time in this Encounter, immediately end the turn; then, if there are fewer than 5 "Kurokumo Clan" allies other than this unit and Jun, summon up to 5 allies comprised of Adept Kurokumo Henchwoman and Tired Kurokumo Henchwoman.\n(above units are summoned at 30 SP)\n\nAfter entering a different pattern, gain the following effects:\n- Deal +(missing HP percentage on self)% damage (max 100%)\n- Replace "Kumogiri" with "Rend Space"
   PL:
595. [[podstawowe] Pasywka wroga [600202] — podsumowanie] 두 턴마다 ‘발도 자세’ 후 ‘쿠모기리’ 사용\n‘발도 자세’는 E.G.O 스킬에 피격되면 취소\n체력 50% 이하 시 조직원 소환, 가하는 피해량이 증가
   źródło: Passives_Enemy-schema.json :: dataList[id=600202].summary
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Every 2 turns, use "Battō Shisei" followed by "Kumogiri"\n"Battō Shisei" Skill is canceled when hit by E.G.O Skills\nAt 50%- HP, summon allies and deal more damage
   PL:
596. [[podstawowe] Pasywka wroga [600202] — tekst klimatyczny] 흑운회의 초대 조장이 창시한 흑운회 고유의 발도술. 검은 구름 속에서 번개가 번쩍이듯, 언제 어디에서 검격이 날아들지 알 수 없다.
   źródło: Passives_Enemy-schema.json :: dataList[id=600202].flavor
   limit: do 310 znaków
   EN: The Kurokumo Clan owes its signature sword-drawing technique to its very first Patriarch. Keep a wary eye on the bank of black clouds all you like, but you will never predict where the flash of the lightning-fast sword will strike, or when.
   PL:
597. [[podstawowe] Pasywka wroga [600203] — nazwa] 흑운회 제3조장
   źródło: Passives_Enemy-schema.json :: dataList[id=600203].name
   limit: do 80 znaków
   EN: Patriarch of the Third Family, a Kurokumo Clan Subsidiary
   PL:
598. [[podstawowe] Pasywka wroga [600203] — opis] 자신을 포함하여 자신과 동일한 진영의 흑운회 소속이 이번 전투 동안 [BlackCloudBladeEnemy] 1 얻음\n- 효과 적용 대상의 체력이 전투에서 처음으로 50% 이하가 되면, [EngageToBattleEnemy] 1을 추가로 얻음\n\n<color=#ff6000><mark=#ff000040><b><u>자신과 동일한 진영의 흑운회 소속이 사망할 때마다 흑운회 제3조장 미네의 속도 최솟값, 최댓값 +1 (각각 최대 5)</u></b></mark></color>
   źródło: Passives_Enemy-schema.json :: dataList[id=600203].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BlackCloudBladeEnemy], [EngageToBattleEnemy]
   znaczenie tagów: [BlackCloudBladeEnemy] = 흑운도 / Dark Cloud Blade; [EngageToBattleEnemy] = 임전 / Battle Ready
   EN: Allied "Kurokumo Clan" units, including this unit, gain 1 [BlackCloudBladeEnemy] for the Encounter\n- When an affected unit's HP drops 50% or below for the first time in this Encounter, additionally gain 1 [EngageToBattleEnemy]\n\n<color=#ff6000><mark=#ff000040><b><u>Whenever an allied "Kurokumo Clan" unit is defeated, Min & Max Speed +1 for Mine, Patriarch of the Kurokumo Clan's Third Family (max +5 each)</u></b></mark></color>
   PL:
599. [[podstawowe] Pasywka wroga [600203] — tekst klimatyczny] 남부에서 동부까지 세력을 뻗친 흑운회는 여러 조로 구성되어 있다. 그중 하나의 집단으로서 의미를 갖는 것은 제1조부터 제4조까지다. 이들은 각 조장에 따라 같은 조직임에도 서로 다른 면모를 갖는다.\n\n제1조장은 흑운회를 다스리고, 제2조장은 흑운회의 가장 날카로운 검이 되었으며, 제3조장은 칼싸움과 살육을 즐겨 싸움판을 찾아다닌다. 반면 제4조장은 어느 날 실종되어 그 행방이 묘연하다.
   źródło: Passives_Enemy-schema.json :: dataList[id=600203].flavor
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Kurokumo Clan's reach extends from the South of the City all the way to the East. Its subsidiaries are many, but only the First through the Fourth have each acquired an identity of their own. In the character of each, one may recognize the hand of its Patriarch.\n\nThe First rules the Clan. The Second became its keenest blade. The Third enjoys a good battle of blades and the slaughter that comes with it, going wherever there's plenty of both. As for the Fourth... one day the Fourth simply vanished. To where, no one can say.
   PL:
600. [[podstawowe] Pasywka wroga [601305] — nazwa] 도상구축
   źródło: Passives_Enemy-schema.json :: dataList[id=601305].name
   (powtórzenie elementu 590 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [[podstawowe] Pasywka wroga [601305] — opis] 이번 전투에서 흑운회 부조장 쥰에게 다음 효과 적용\n- 최대 체력 +75%, 흐트러짐 선 하나 제거 (30%)\n- <color=#ff6000><mark=#ff000040><b><u>참격 속성 스킬로 받는 피해량 +50% (E.G.O 스킬일 경우, 대신 100%)</u></b></mark></color>
   źródło: Passives_Enemy-schema.json :: dataList[id=601305].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: In this Encounter, apply the following effects on Kurokumo Clan Captain Jun:\n- Max HP +75%, remove one Stagger Threshold (30%)\n- <color=#ff6000><mark=#ff000040><b><u>Take +50% damage from Slash Skills (for E.G.O Skills, take +100% damage instead)</u></b></mark></color>
   PL:
602. [[podstawowe] Pasywka wroga [601305] — tekst klimatyczny] “도상적으로 구축된 표상. 이 훈련을 통해 많은 걸 체험해볼 수 있을 거야. 특히 관리자, 당신은 유독 이 훈련에 잘 맞거든.”\n“시지프 탑이 건재했다면, 당신의 시스템은 어떤 모습이었을까?”
   źródło: Passives_Enemy-schema.json :: dataList[id=601305].flavor
   (powtórzenie elementu 592 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [[podstawowe] Pasywka wroga [600405] — nazwa] 도상구축
   źródło: Passives_Enemy-schema.json :: dataList[id=600405].name
   (powtórzenie elementu 590 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [[podstawowe] Pasywka wroga [600405] — opis] 이번 전투에서 흑운회 부조장 쥰에게 다음 효과 적용\n- 최대 체력 +75%, 흐트러짐 선 하나 제거 (30%)\n- <color=#ff6000><mark=#ff000040><b><u>참격 속성 스킬로 받는 피해량 +50% (E.G.O 스킬일 경우, 대신 100%)</u></b></mark></color>\n- 자신의 체력이 처음으로 50% 이하가 되었을 때 턴이 즉시 종료되고,\n자신을 제외한 자신 진영 흑운회 소속이 다섯 미만이면 결연한 흑운회 조직원, 긴장한 흑운회 조직원을 합하여 다섯 명까지 불러옴 (새롭게 등장한 적들은 정신력이 30인 상태로 등장)
   źródło: Passives_Enemy-schema.json :: dataList[id=600405].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: In this Encounter, apply the following effects on Kurokumo Clan Captain Jun:\n- Max HP +75%, Remove one Stagger Threshold (30%)\n- <color=#ff6000><mark=#ff000040><b><u>Take +50% damage from Slash Skills (for E.G.O Skills, take +100% damage instead)</u></b></mark></color>\n- If this unit's HP has dropped to 50% or below for the first time, the turn ends immediately;\nIf this unit has fewer than 5 "Kurokumo Clan" allies on the field (excluding this unit), summon up to 5 allies (combining <noparse>Determined</noparse> Kurokumo Henchmen and Tense Kurokumo Henchmen; newly-summoned units enter the field with 30 SP)
   PL:
605. [[podstawowe] Pasywka wroga [600405] — tekst klimatyczny] “도상적으로 구축된 표상. 이 훈련을 통해 많은 걸 체험해볼 수 있을 거야. 특히 관리자, 당신은 유독 이 훈련에 잘 맞거든.”\n“시지프 탑이 건재했다면, 당신의 시스템은 어떤 모습이었을까?”
   źródło: Passives_Enemy-schema.json :: dataList[id=600405].flavor
   (powtórzenie elementu 592 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [[podstawowe] Pasywka wroga [600508] — nazwa] 도상구축
   źródło: Passives_Enemy-schema.json :: dataList[id=600508].name
   (powtórzenie elementu 590 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [[podstawowe] Pasywka wroga [600508] — opis] 이번 전투에서 리카르도에게 다음 효과 적용\n- 최대 체력 +25%, 흐트러짐 선 하나 제거(25%)\n- <color=#ff6000><mark=#ff000040><b><u>타격 속성 스킬로 받는 피해량 +50% (E.G.O 스킬일 경우, 대신 100%)</u></b></mark></color>\n- 정신력이 0 미만으로 내려가지 않음\n- 자신과 동일한 진영의 중지 소속이 사망할 때마다 리카르도의 속도 최솟값, 최댓값 +1 (각각 최대 3)\n- ‘다들 집합’ 사용 시, 아군 2명을 추가로 소환
   źródło: Passives_Enemy-schema.json :: dataList[id=600508].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: In this Encounter, apply the following effects on Ricardo:\n- Max HP +25%, Remove one Stagger Threshold (25%)\n- <color=#ff6000><mark=#ff000040><b><u>Take +50% damage from Blunt Skills (for E.G.O Skills, take +100% damage instead)</u></b></mark></color>\n- SP does not drop below 0\n- Min & Max Speed +1 every time this unit's ally from "The Middle" is killed (max 3 each)\n- Upon using the "Assemble" Skill, summon 2 more allies
   PL:
608. [[podstawowe] Pasywka wroga [600508] — tekst klimatyczny] “도상적으로 구축된 표상. 이 훈련을 통해 많은 걸 체험해볼 수 있을 거야. 특히 관리자, 당신은 유독 이 훈련에 잘 맞거든.”\n“시지프 탑이 건재했다면, 당신의 시스템은 어떤 모습이었을까?”
   źródło: Passives_Enemy-schema.json :: dataList[id=600508].flavor
   (powtórzenie elementu 592 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [[podstawowe] Pasywka wroga [600605] — nazwa] 도상구축
   źródło: Passives_Enemy-schema.json :: dataList[id=600605].name
   (powtórzenie elementu 590 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [[podstawowe] Pasywka wroga [600605] — opis] 이번 전투에서 작은 아우 베르너에게 다음 효과 적용\n- 최대 체력 +25%\n- <color=#ff6000><mark=#ff000040><b><u>타격 속성 스킬로 받는 피해량 +50% (E.G.O 스킬일 경우, 대신 100%)</u></b></mark></color>
   źródło: Passives_Enemy-schema.json :: dataList[id=600605].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: In this Encounter, apply the following effects on Little Brother Werner:\n- <color=#ff6000><mark=#ff000040><b><u>Take +25% damage from Blunt Skills (for E.G.O Skills, take +100% damage instead)</u></b></mark></color>
   PL:
611. [[podstawowe] Pasywka wroga [600605] — tekst klimatyczny] “도상적으로 구축된 표상. 이 훈련을 통해 많은 걸 체험해볼 수 있을 거야. 특히 관리자, 당신은 유독 이 훈련에 잘 맞거든.”\n“시지프 탑이 건재했다면, 당신의 시스템은 어떤 모습이었을까?”
   źródło: Passives_Enemy-schema.json :: dataList[id=600605].flavor
   (powtórzenie elementu 592 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [[podstawowe] Pasywka wroga [601101] — nazwa] 반짝
   źródło: Passives_Enemy-schema.json :: dataList[id=601101].name
   limit: do 40 znaków
   EN: Sparkle
   PL:
613. [[podstawowe] Pasywka wroga [601101] — opis] 특정 턴마다, 전봇대 부위가 [ElectricPolePower] 10 얻음\n[ElectricPolePower]의 효과로 0이 되어 소멸하면, 전봇대 부위가 파괴됨\n턴 종료 시까지 [ElectricPolePower]이 남아 있으면, 다음 턴에 강력한 스킬 사용
   źródło: Passives_Enemy-schema.json :: dataList[id=601101].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [ElectricPolePower]
   znaczenie tagów: [ElectricPolePower] = 고압 방전 / High-voltage Discharge
   EN: The "Telepole" Part gains 10 [ElectricPolePower] every specific turn\nIf [ElectricPolePower] is reduced to 0 due to its effects, the "Telepole" Part will be destroyed\nIf [ElectricPolePower] remains until Turn End, this unit uses a powerful Skill next turn
   PL:
614. [[podstawowe] Pasywka wroga [601102] — nazwa] 피뢰침
   źródło: Passives_Enemy-schema.json :: dataList[id=601102].name
   (powtórzenie elementu 408 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [[podstawowe] Pasywka wroga [601102] — opis] 자신의 [DogThunder]가 5 이상이면, 다음 턴부터 부위마다 피격 시 이번 턴에 [ElectricShock] 3 부여 ([DogThunder]가 0이 되기전까지 지속)\n나태 속성 공격에 피격 시 [ElectricShock] 부여량이 절반으로 감소 (소수점올림)
   źródło: Passives_Enemy-schema.json :: dataList[id=601102].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [DogThunder], [ElectricShock]
   znaczenie tagów: [DogThunder] = 번개 / Lightning; [ElectricShock] = 감전 / Shock
   EN: At 5+ [DogThunder], all Parts will inflict 3 [ElectricShock] on the attacker when hit, starting from the next turn (lasts until [DogThunder] reaches 0)\nWhen hit by a Sloth attack, the amount of [ElectricShock] inflicted is halved (rounded up)
   PL:
616. [[podstawowe] Pasywka wroga [601103] — nazwa] 번개
   źródło: Passives_Enemy-schema.json :: dataList[id=601103].name
   (powtórzenie elementu 410 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [[podstawowe] Pasywka wroga [601103] — opis] 전봇대가 파괴되지 않았으면 공격 종료 시, [DogThunder] 1 얻음\n전봇대 피격 시, [DogThunder] 1 소모
   źródło: Passives_Enemy-schema.json :: dataList[id=601103].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [DogThunder]
   znaczenie tagów: [DogThunder] = 번개 / Lightning
   EN: While the Telepole isn’t broken, gain 1 [DogThunder] after an attack\nWhenever the Telepole is hit by an attack, lose 1 [DogThunder]
   PL:
618. [[podstawowe] Pasywka wroga [601104] — nazwa] 부서지는 파편
   źródło: Passives_Enemy-schema.json :: dataList[id=601104].name
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [[podstawowe] Pasywka wroga [601104] — opis] 전봇대가 흐트러짐 상태거나 부위 파괴되었으면, [DogThunder]가 0이 되고 이번 턴에 골목파수견의 공격 스킬이 전부 취소됨
   źródło: Passives_Enemy-schema.json :: dataList[id=601104].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [DogThunder]
   znaczenie tagów: [DogThunder] = 번개 / Lightning
   EN: When Telepole is Staggered or Broken, lose all [DogThunder];\nAll Attack Skills of the Alleyway Watchdog will then be canceled for the turn
   PL:

## [podstawowe] Pasywka wroga: Passives_Enemy
- plik gry: `Passives_Enemy.json`

620. [[podstawowe] Pasywka wroga [90001] — nazwa] 벌레 육체
   źródło: Passives_Enemy.json :: dataList[id=90001].name
   limit: do 40 znaków
   EN: Verminous Body
   PL:
621. [[podstawowe] Pasywka wroga [90001] — opis] 턴 종료 시 체력 5 회복
   źródło: Passives_Enemy.json :: dataList[id=90001].desc
   limit: do 120 znaków
   EN: At the end of the turn, heal 5 HP.
   PL:
622. [[podstawowe] Pasywka wroga [90002] — nazwa] 영양분 보충
   źródło: Passives_Enemy.json :: dataList[id=90002].name
   limit: do 40 znaków
   EN: Nutritive Reinforcements
   PL:
623. [[podstawowe] Pasywka wroga [90002] — opis] 적 처치 시 체력 20 회복, 다음 턴에 수비 위력 증가 5를 얻음
   źródło: Passives_Enemy.json :: dataList[id=90002].desc
   limit: do 120 znaków
   EN: After defeating an enemy, heal 20 HP, and gain 5 Defense Power Up next turn.
   PL:
624. [[podstawowe] Pasywka wroga [90003] — nazwa] 날카로운 칼
   źródło: Passives_Enemy.json :: dataList[id=90003].name
   limit: do 40 znaków
   EN: Sharp Edge
   PL:
625. [[podstawowe] Pasywka wroga [90003] — opis] 공격 적중 시 출혈 1-2 부여\n턴 시작 시 표적이 있는 캐릭터가 있으면, 해당 캐릭터를 공격함
   źródło: Passives_Enemy.json :: dataList[id=90003].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On hit, inflict 1-2 Bleed.\nIf a unit is Marked, attack them first.
   PL:
626. [[podstawowe] Pasywka wroga [90004] — nazwa] 사기 하락
   źródło: Passives_Enemy.json :: dataList[id=90004].name
   limit: do 40 znaków
   EN: Weak Morale
   PL:
627. [[podstawowe] Pasywka wroga [90004] — opis] 아군이 사망할 때마다 영구적으로 취약 1을 얻음
   źródło: Passives_Enemy.json :: dataList[id=90004].desc
   limit: do 120 znaków
   EN: Whenever an ally dies, permanently gain 1 Fragile.
   PL:
628. [[podstawowe] Pasywka wroga [90005] — nazwa] 응징
   źródło: Passives_Enemy.json :: dataList[id=90005].name
   limit: do 40 znaków
   EN: Retribution
   PL:
629. [[podstawowe] Pasywka wroga [90005] — opis] 체력이 50% 이하가 되면 다음 턴에 공격 위력 증가 5를 얻음
   źródło: Passives_Enemy.json :: dataList[id=90005].desc
   limit: do 120 znaków
   EN: When HP drops below 50%, gain 5 Attack Power Up next turn.
   PL:
630. [[podstawowe] Pasywka wroga [90006] — nazwa] 정신 파동
   źródło: Passives_Enemy.json :: dataList[id=90006].name
   limit: do 40 znaków
   EN: Mind Wave
   PL:
631. [[podstawowe] Pasywka wroga [90006] — opis] 공격 적중 시 대상의 정신력 -10
   źródło: Passives_Enemy.json :: dataList[id=90006].desc
   limit: do 120 znaków
   EN: On hit, target loses 10 SP.
   PL:
632. [[podstawowe] Pasywka wroga [9000101] — nazwa] 부상당한 강화 육체
   źródło: Passives_Enemy.json :: dataList[id=9000101].name
   limit: do 40 znaków
   EN: Injured Augmentation
   PL:
633. [[podstawowe] Pasywka wroga [9000101] — opis] 체력이 50% 미만일 때 턴 시작 시 체력 1 회복
   źródło: Passives_Enemy.json :: dataList[id=9000101].desc
   limit: do 120 znaków
   EN: At the start of the turn, if at less than 50% HP, heal 1 HP.
   PL:
634. [[podstawowe] Pasywka wroga [9000102] — nazwa] 강화 육체
   źródło: Passives_Enemy.json :: dataList[id=9000102].name
   limit: do 40 znaków
   EN: Augmented Body
   PL:
635. [[podstawowe] Pasywka wroga [9000102] — opis] 체력이 50% 미만일 때 턴 시작 시 체력 2 회복
   źródło: Passives_Enemy.json :: dataList[id=9000102].desc
   limit: do 120 znaków
   EN: At the start of the turn, if at less than 50% HP, heal 2 HP.
   PL:
636. [[podstawowe] Pasywka wroga [9000103] — nazwa] 침식된 강화 육체
   źródło: Passives_Enemy.json :: dataList[id=9000103].name
   limit: do 40 znaków
   EN: Corroded Augmentation
   PL:
637. [[podstawowe] Pasywka wroga [9000103] — opis] 체력이 50% 미만일 때 턴 시작 시 체력 4 회복
   źródło: Passives_Enemy.json :: dataList[id=9000103].desc
   limit: do 120 znaków
   EN: At the start of the turn, if at less than 50% HP, heal 4 HP.
   PL:
638. [[podstawowe] Pasywka wroga [9100301] — nazwa] 큰형님
   źródło: Passives_Enemy.json :: dataList[id=9100301].name
   limit: do 40 znaków
   EN: Big Boss
   PL:
639. [[podstawowe] Pasywka wroga [9100301] — opis] 이 캐릭터가 사망하면 모든 아군 정신력 -45
   źródło: Passives_Enemy.json :: dataList[id=9100301].desc
   limit: do 120 znaków
   EN: When this unit is defeated, all its allies lose 45 SP.
   PL:
640. [[podstawowe] Pasywka wroga [9100302] — nazwa] 아그들아!
   źródło: Passives_Enemy.json :: dataList[id=9100302].name
   limit: do 40 znaków
   EN: Not Me Boys!
   PL:
641. [[podstawowe] Pasywka wroga [9100302] — opis] 아군이 사망할 때마다 이 캐릭터의 정신력 -15
   źródło: Passives_Enemy.json :: dataList[id=9100302].desc
   limit: do 120 znaków
   EN: This unit loses 15 SP whenever an ally is defeated.
   PL:
642. [[podstawowe] Pasywka wroga [9100401] — nazwa] 파티 타임
   źródło: Passives_Enemy.json :: dataList[id=9100401].name
   limit: do 40 znaków
   EN: Hora de Fiesta
   PL:
643. [[podstawowe] Pasywka wroga [9100401] — opis] 매 턴마다 자신 포함 모든 아군 정신력 10 회복\n자신의 정신력 20 이상이면 턴 시작 시 공격 위력 증가, 수비 위력 증가 1 얻음
   źródło: Passives_Enemy.json :: dataList[id=9100401].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the turn, all allies heal 10 SP.\nAt 20+ SP, gain 1 Attack Power Up and 1 Defense Power Up at turn start.
   PL:
644. [[podstawowe] Pasywka wroga [9100402] — nazwa] 파티 종료
   źródło: Passives_Enemy.json :: dataList[id=9100402].name
   limit: do 40 znaków
   EN: Se Acabó la Fiesta
   PL:
645. [[podstawowe] Pasywka wroga [9100402] — opis] 이 캐릭터가 사망하면 모든 아군 정신력 -45
   źródło: Passives_Enemy.json :: dataList[id=9100402].desc
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [[podstawowe] Pasywka wroga [9002801] — nazwa] HP탄
   źródło: Passives_Enemy.json :: dataList[id=9002801].name
   (powtórzenie elementu 568 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [[podstawowe] Pasywka wroga [9002801] — opis] 턴 시작 시 체력 15 회복\n체력이 50%미만이면 체력 15 추가 회복
   źródło: Passives_Enemy.json :: dataList[id=9002801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the turn, heal 15 HP.\nAt less than 50% HP, heal 15 additional HP.
   PL:
648. [[podstawowe] Pasywka wroga [9003201] — nazwa] 고귀한 희생있도다
   źródło: Passives_Enemy.json :: dataList[id=9003201].name
   limit: do 40 znaków
   EN: Noble be Thy Sacrifice
   PL:
649. [[podstawowe] Pasywka wroga [9003201] — opis] 아군이 사망하면 다음 턴 시작 시 공격 위력 증가 1을 얻는다.
   źródło: Passives_Enemy.json :: dataList[id=9003201].desc
   limit: do 120 znaków
   EN: When an ally is defeated, gain 1 Attack Power Up next turn.
   PL:
650. [[podstawowe] Pasywka wroga [9003801] — nazwa] 처단의 기쁨
   źródło: Passives_Enemy.json :: dataList[id=9003801].name
   limit: do 40 znaków
   EN: Joy of Execution
   PL:
651. [[podstawowe] Pasywka wroga [9003801] — opis] 적을 처치하면 다음 턴 시작 시 피해량 증가 2를 얻는다.
   źródło: Passives_Enemy.json :: dataList[id=9003801].desc
   limit: do 120 znaków
   EN: After defeating an enemy, gain 2 Damage Up next turn.
   PL:
652. [[podstawowe] Pasywka wroga [9100501] — nazwa] 쥐는 자의 망치
   źródło: Passives_Enemy.json :: dataList[id=9100501].name
   limit: do 40 znaków
   EN: Hammer of the One Who Grips
   PL:
653. [[podstawowe] Pasywka wroga [9100501] — opis] 이 캐릭터가 살아있는동안 모든 아군이 턴 시작 시 정신력 10 회복\n이 캐릭터가 사망하면 모든 아군 정신력 -45
   źródło: Passives_Enemy.json :: dataList[id=9100501].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the turn, all allies heal 10 SP.\nWhen this unit is defeated, all its allies lose 45 SP.
   PL:
654. [[podstawowe] Pasywka wroga [9100601] — nazwa] 집념
   źródło: Passives_Enemy.json :: dataList[id=9100601].name
   limit: do 40 znaków
   EN: Persistence
   PL:
655. [[podstawowe] Pasywka wroga [9100601] — opis] 체력이 50% 미만이 되면, 다음 턴 시작 시 자신에게 부여된 부정적인 효과를 제거하고, 매 턴마다 광신 4, 공격 위력 증가 1, 수비 위력 증가 1을 얻는다.
   źródło: Passives_Enemy.json :: dataList[id=9100601].desc
   limit: do 190 znaków
   EN: When HP drops below 50%, remove all negative status effects next turn, and gain 4 Fanatic, 1 Attack Power Up, and 1 Defense Power Up each turn.
   PL:
656. [[podstawowe] Pasywka wroga [9100502] — nazwa] 두드릴지라
   źródło: Passives_Enemy.json :: dataList[id=9100502].name
   limit: do 40 znaków
   EN: Thou Shalt Hammer
   PL:
657. [[podstawowe] Pasywka wroga [9100502] — opis] 자신에게 광신이 있을 때 피해량 +50%
   źródło: Passives_Enemy.json :: dataList[id=9100502].desc
   limit: do 120 znaków
   EN: If this unit is Fanatic, deal +50% damage.
   PL:
658. [[podstawowe] Pasywka wroga [9004601] — nazwa] 기계 정신
   źródło: Passives_Enemy.json :: dataList[id=9004601].name
   limit: do 40 znaków
   EN: Mechanical Mentality
   PL:
659. [[podstawowe] Pasywka wroga [9004601] — opis] 정신력이 0에 고정됨.
   źródło: Passives_Enemy.json :: dataList[id=9004601].desc
   limit: do 120 znaków
   EN: Sanity is fixed at 0.
   PL:
660. [[podstawowe] Pasywka wroga [9004602] — nazwa] 단단한 외피
   źródło: Passives_Enemy.json :: dataList[id=9004602].name
   limit: do 40 znaków
   EN: Solid Exterior
   PL:
661. [[podstawowe] Pasywka wroga [9004602] — opis] <sprite name="Laceration"><color=#f8c200><u><link="Laceration">출혈</color></link></u>과 <sprite name="Combustion"><color=#f8c200><u><link="Combustion">화상</color></link></u>에 입는 피해 반감.
   źródło: Passives_Enemy.json :: dataList[id=9004602].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#f8c200>, <u>, <link="Laceration">, </color>, </link>, </u>, <sprite name="Combustion">, <link="Combustion">
   EN: Take half as much damage from <sprite name="Laceration"><color=#f8c200><u><link="Laceration">Bleed</color></link></u> and <sprite name="Combustion"><color=#f8c200><u><link="Combustion">Burn</color></link></u>.
   PL:
662. [[podstawowe] Pasywka wroga [9004603] — nazwa] 흔들림 주의
   źródło: Passives_Enemy.json :: dataList[id=9004603].name
   limit: do 40 znaków
   EN: Caution: Unsteady
   PL:
663. [[podstawowe] Pasywka wroga [9004603] — opis] 자신이 받는 진동 폭발에 의한 흐트러짐 손상 +50%
   źródło: Passives_Enemy.json :: dataList[id=9004603].desc
   limit: do 120 znaków
   EN: This unit's stagger threshold rises by 50% more when affected by Tremor Burst
   PL:
664. [[podstawowe] Pasywka wroga [9004604] — nazwa] 파손 주의
   źródło: Passives_Enemy.json :: dataList[id=9004604].name
   limit: do 40 znaków
   EN: Caution: Delicate
   PL:
665. [[podstawowe] Pasywka wroga [9004604] — opis] 자신이 받는 <sprite name="Burst"><color=#f8c200><u><link="Burst">파열</color></link></u>에 의한 피해 +30% (소수점 버림)
   źródło: Passives_Enemy.json :: dataList[id=9004604].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#f8c200>, <u>, <link="Burst">, </color>, </link>, </u>
   EN: Take +30% damage from <sprite name="Burst"><color=#f8c200><u><link="Burst">Rupture</color></link></u> (Rounded down)
   PL:
666. [[podstawowe] Pasywka wroga [9004901] — nazwa] 파손 기능 손상
   źródło: Passives_Enemy.json :: dataList[id=9004901].name
   limit: do 40 znaków
   EN: Damageable Disuniter
   PL:
667. [[podstawowe] Pasywka wroga [9004901] — opis] 흐트러짐 상태가 된다면, 이후로 부여하는 파열, 파열 횟수 1 감소
   źródło: Passives_Enemy.json :: dataList[id=9004901].desc
   limit: do 120 znaków
   EN: After being staggered, inflict 1 less Rupture and Rupture Count
   PL:
668. [[podstawowe] Pasywka wroga [9005001] — nazwa] 흔들림 기능 손상
   źródło: Passives_Enemy.json :: dataList[id=9005001].name
   limit: do 40 znaków
   EN: Damageable Thumper
   PL:
669. [[podstawowe] Pasywka wroga [9005001] — opis] 흐트러짐 상태가 된다면, 이후로 부여하는 진동, 진동 횟수 1 감소
   źródło: Passives_Enemy.json :: dataList[id=9005001].desc
   limit: do 120 znaków
   EN: After being staggered, inflict 1 less Tremor and Tremor Count
   PL:
670. [[podstawowe] Pasywka wroga [9100701] — nazwa] 공격 기능 과열
   źródło: Passives_Enemy.json :: dataList[id=9100701].name
   limit: do 40 znaków
   EN: Overheating Attack Function
   PL:
671. [[podstawowe] Pasywka wroga [9100701] — opis] 자신의 공격으로 흐트러짐 상태를 만들었다면, 다음 턴에 피해량 증가 3 얻음
   źródło: Passives_Enemy.json :: dataList[id=9100701].desc
   limit: do 120 znaków
   EN: When staggering a unit with an attack, gain 3 Damage Up next turn.
   PL:
672. [[podstawowe] Pasywka wroga [9100702] — nazwa] 파손 기능 완전 손상
   źródło: Passives_Enemy.json :: dataList[id=9100702].name
   limit: do 40 znaków
   EN: Breakable Disuniter
   PL:
673. [[podstawowe] Pasywka wroga [9100702] — opis] 흐트러짐 상태가 된다면, 이후로 부여하는 파열, 파열 횟수 3 감소
   źródło: Passives_Enemy.json :: dataList[id=9100702].desc
   limit: do 120 znaków
   EN: After being staggered, inflict 3 less Rupture and Rupture Count
   PL:
674. [[podstawowe] Pasywka wroga [9100703] — nazwa] 흔들림 기능 완전 손상
   źródło: Passives_Enemy.json :: dataList[id=9100703].name
   limit: do 40 znaków
   EN: Breakable Thumper
   PL:
675. [[podstawowe] Pasywka wroga [9100703] — opis] 흐트러짐 상태가 된다면, 이후로 부여하는 진동, 진동 횟수 3 감소
   źródło: Passives_Enemy.json :: dataList[id=9100703].desc
   limit: do 120 znaków
   EN: After being staggered, inflict 3 less Tremor and Tremor Count
   PL:
676. [[podstawowe] Pasywka wroga [9100801] — nazwa] 스패너 가동
   źródło: Passives_Enemy.json :: dataList[id=9100801].name
   limit: do 40 znaków
   EN: Spanner Up
   PL:
677. [[podstawowe] Pasywka wroga [9100801] — opis] 턴동안 앞면 적중한 코인 수만큼 공진을 얻음. (최대 10)
   źródło: Passives_Enemy.json :: dataList[id=9100801].desc
   limit: do 120 znaków
   EN: Gain Resonant by the number of heads Coins that successfully hit during a turn. (Max 10)
   PL:
678. [[podstawowe] Pasywka wroga [9100802] — nazwa] 장미스패너 공방 대표
   źródło: Passives_Enemy.json :: dataList[id=9100802].name
   limit: do 40 znaków
   EN: Rosespanner Workshop Rep
   PL:
679. [[podstawowe] Pasywka wroga [9100802] — opis] 웨이브동안 죽은 아군 수만큼 진동을 추가 부여
   źródło: Passives_Enemy.json :: dataList[id=9100802].desc
   limit: do 120 znaków
   EN: Inflict more Tremor by the number of allies that have died this wave
   PL:
680. [[podstawowe] Pasywka wroga [9100803] — nazwa] 마지막인건가요
   źródło: Passives_Enemy.json :: dataList[id=9100803].name
   limit: do 40 znaków
   EN: Guess I'm the Last
   PL:
681. [[podstawowe] Pasywka wroga [9100803] — opis] 혼자 남으면 매 턴마다 공진 1, 진동 동화 1 얻음.
   źródło: Passives_Enemy.json :: dataList[id=9100803].desc
   limit: do 120 znaków
   EN: When alone, gain 1 Resonant and 1 Tremor Sync every turn.
   PL:
682. [[podstawowe] Pasywka wroga [9100804] — nazwa] 어쩔 수 없네요
   źródło: Passives_Enemy.json :: dataList[id=9100804].name
   limit: do 40 znaków
   EN: I've Got No Choice
   PL:
683. [[podstawowe] Pasywka wroga [9100804] — opis] 혼자 남았을 때, 자신을 마지막으로 공격한 사람을 다음 턴에 지정함.
   źródło: Passives_Enemy.json :: dataList[id=9100804].desc
   limit: do 120 znaków
   EN: When alone, marks the last unit that attacked this character as a target next turn.
   PL:
684. [[podstawowe] Pasywka wroga [9100901] — nazwa] 얽혀오는 저주 부적
   źródło: Passives_Enemy.json :: dataList[id=9100901].name
   limit: do 40 znaków
   EN: Entangling Curse Talisman
   PL:
685. [[podstawowe] Pasywka wroga [9100901] — opis] 턴동안 진행한 합만큼 얽혀온 저주 부적을 얻음.
   źródło: Passives_Enemy.json :: dataList[id=9100901].desc
   limit: do 120 znaków
   EN: Gain Entangled Curse Talismans by the number of clashes the unit engaged in during a turn.
   PL:
686. [[podstawowe] Pasywka wroga [9100902] — nazwa] 옭아매인 저주 부적
   źródło: Passives_Enemy.json :: dataList[id=9100902].name
   limit: do 40 znaków
   EN: Strangling Curse Talisman
   PL:
687. [[podstawowe] Pasywka wroga [9100902] — opis] 얽혀온 저주 부적이 10이라면, 10만큼 흐트러짐 손상. 전부 소멸.
   źródło: Passives_Enemy.json :: dataList[id=9100902].desc
   limit: do 120 znaków
   EN: At 10 Entangled Curse Talismans, raise stagger threshold by 10, then remove the status.
   PL:
688. [[podstawowe] Pasywka wroga [9100903] — nazwa] 증식하는 저주 부적
   źródło: Passives_Enemy.json :: dataList[id=9100903].name
   limit: do 40 znaków
   EN: Multiplying Curse Talisman
   PL:
689. [[podstawowe] Pasywka wroga [9100903] — opis] 체력이 30%이하일 때, 부여하는 다시 붙여진 저주 부적 +1
   źródło: Passives_Enemy.json :: dataList[id=9100903].desc
   limit: do 120 znaków
   EN: At 30% or less HP, inflict +1 Reattached Curse Talisman
   PL:
690. [[podstawowe] Pasywka wroga [9100904] — nazwa] 침식하는 저주 부적
   źródło: Passives_Enemy.json :: dataList[id=9100904].name
   limit: do 40 znaków
   EN: Encroaching Curse Talisman
   PL:
691. [[podstawowe] Pasywka wroga [9100904] — opis] 체력이 30%이하일 때, 공격 종료 시 대상에게 다시 붙여진 저주 부적이 5이상이라면 다음 턴에 마비 2 부여
   źródło: Passives_Enemy.json :: dataList[id=9100904].desc
   limit: do 160 znaków
   EN: At 30% or less HP, if the target has 5+ Reattached Curse Talisman after an attack is finished, inflict 2 Paralyze next turn.
   PL:
692. [[podstawowe] Pasywka wroga [9006201] — nazwa] 흘러오는 우울
   źródło: Passives_Enemy.json :: dataList[id=9006201].name
   (powtórzenie elementu 580 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [[podstawowe] Pasywka wroga [9006201] — opis] 뒷면 적중 시 침잠 2 부여
   źródło: Passives_Enemy.json :: dataList[id=9006201].desc
   limit: do 120 znaków
   EN: Tails Coins inflict 2 Sinking
   PL:
694. [[podstawowe] Pasywka wroga [9006202] — nazwa] 넘쳐흐르는 슬픔
   źródło: Passives_Enemy.json :: dataList[id=9006202].name
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [[podstawowe] Pasywka wroga [9006202] — opis] 턴 종료 시, 자신의 정신력 5 감소
   źródło: Passives_Enemy.json :: dataList[id=9006202].desc
   limit: do 120 znaków
   EN: At the end of the turn, lose 5 SP
   PL:
696. [[podstawowe] Pasywka wroga [9006101] — nazwa] 취기
   źródło: Passives_Enemy.json :: dataList[id=9006101].name
   limit: do 40 znaków
   EN: Intoxication
   PL:
697. [[podstawowe] Pasywka wroga [9006101] — opis] 가지고 있는 고양이 5일 때, 취기를 5 얻음.
   źródło: Passives_Enemy.json :: dataList[id=9006101].desc
   limit: do 120 znaków
   EN: At 5 Morale Boost, gain 5 Tipsy.
   PL:
698. [[podstawowe] Pasywka wroga [9006102] — nazwa] 숙취 해소
   źródło: Passives_Enemy.json :: dataList[id=9006102].name
   limit: do 40 znaków
   EN: Hangover Cure
   PL:
699. [[podstawowe] Pasywka wroga [9006102] — opis] 가지고 있는 취기가 5일 때, 수비 스킬을 사용함.
   źródło: Passives_Enemy.json :: dataList[id=9006102].desc
   limit: do 120 znaków
   EN: At 5 Tipsy, uses a defense skill.
   PL:
700. [[podstawowe] Pasywka wroga [9006801] — nazwa] 회복 앰플 주입
   źródło: Passives_Enemy.json :: dataList[id=9006801].name
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [[podstawowe] Pasywka wroga [9006801] — opis] 턴 시작 시 체력 20 회복
   źródło: Passives_Enemy.json :: dataList[id=9006801].desc
   limit: do 120 znaków
   EN: At the start of the turn, heal 20 HP.
   PL:
702. [[podstawowe] Pasywka wroga [9006802] — nazwa] 긴급 앰플 투약
   źródło: Passives_Enemy.json :: dataList[id=9006802].name
   (powtórzenie elementu 588 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [[podstawowe] Pasywka wroga [9006802] — opis] 체력이 25%미만이면 전체 체력의 40%까지 회복 (최대 1회)
   źródło: Passives_Enemy.json :: dataList[id=9006802].desc
   limit: do 120 znaków
   EN: At less than 25% HP, heal up to 40% of Max HP (One-time only)
   PL:
704. [[podstawowe] Pasywka wroga [9007001] — nazwa] 황금 시간
   źródło: Passives_Enemy.json :: dataList[id=9007001].name
   limit: do 40 znaków
   EN: Golden Time
   PL:
705. [[podstawowe] Pasywka wroga [9007001] — opis] 턴 종료 시 체력이 12% ~ 24%사이로 남았을 때, 전체 체력의 65%만큼 즉시 회복. 흐트러짐 상태 해제. (최대 1회)
   źródło: Passives_Enemy.json :: dataList[id=9007001].desc
   limit: do 180 znaków
   EN: At the end of the turn, if the HP is between 12% and 24%, instantly heal up to 65% of Max HP, and recover from stagger. (One-time only)
   PL:
706. [[podstawowe] Pasywka wroga [9007002] — nazwa] 시간 역행 반동
   źródło: Passives_Enemy.json :: dataList[id=9007002].name
   limit: do 40 znaków
   EN: Time Reversion Retroaction
   PL:
707. [[podstawowe] Pasywka wroga [9007002] — opis] 황금 시간 발동 이후, 턴 종료 시 취약 3 얻음
   źródło: Passives_Enemy.json :: dataList[id=9007002].desc
   limit: do 120 znaków
   EN: After activating Golden Time, gain 3 Fragile at turn end.
   PL:
708. [[podstawowe] Pasywka wroga [9005401] — nazwa] 공포 장치
   źródło: Passives_Enemy.json :: dataList[id=9005401].name
   limit: do 40 znaków
   EN: Terror Device
   PL:
709. [[podstawowe] Pasywka wroga [9005401] — opis] 아군이 아군에게 공격할 때, 정신력 3 피해
   źródło: Passives_Enemy.json :: dataList[id=9005401].desc
   limit: do 120 znaków
   EN: When an ally attacks another ally, deal 3 SP damage
   PL:
710. [[podstawowe] Pasywka wroga [9006901] — nazwa] 회복 앰플 주입
   źródło: Passives_Enemy.json :: dataList[id=9006901].name
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [[podstawowe] Pasywka wroga [9006901] — opis] 턴 시작 시 체력 20 회복
   źródło: Passives_Enemy.json :: dataList[id=9006901].desc
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [[podstawowe] Pasywka wroga [9006902] — nazwa] 긴급 앰플 투약
   źródło: Passives_Enemy.json :: dataList[id=9006902].name
   (powtórzenie elementu 588 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [[podstawowe] Pasywka wroga [9006902] — opis] 체력이 25%미만이면 전체 체력의 40%까지 회복 (최대 1회)
   źródło: Passives_Enemy.json :: dataList[id=9006902].desc
   (powtórzenie elementu 703 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [[podstawowe] Pasywka wroga [9006803] — nazwa] 긴급 앰플 과부하
   źródło: Passives_Enemy.json :: dataList[id=9006803].name
   limit: do 40 znaków
   EN: Emergency Ampule Overdose
   PL:
715. [[podstawowe] Pasywka wroga [9006803] — opis] 체력이 1 이하로 떨어지지 않음.\n턴 시작 시 체력이 60 이하라면, 강화 상태가 된다.
   źródło: Passives_Enemy.json :: dataList[id=9006803].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: HP does not drop below 1;\nIf at 60- HP at the start of the turn, enter a powered-up state.
   PL:

## [podstawowe] Pasywka wroga: Passives_Enemy91-4
- plik gry: `Passives_Enemy91-4.json`

716. [[podstawowe] Pasywka wroga [9007701] — nazwa] 게판
   źródło: Passives_Enemy91-4.json :: dataList[id=9007701].name
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [[podstawowe] Pasywka wroga [9007701] — opis] 자신이 체력이 70% 미만이면, 현재 체력이 자신을 제외하고 가장 낮은 아군을 지정함\n아군 공격 시 피해량만큼 체력 회복.\n아군 처치 시 피해량의 2배만큼 체력 회복.
   źródło: Passives_Enemy91-4.json :: dataList[id=9007701].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At less than 70% HP, targets another ally with the least current HP.\nWhen attacking an ally, heals HP by the damage dealt.\nWhen defeating an ally, heals HP by double the damage dealt.
   PL:
718. [[podstawowe] Pasywka wroga [9007801] — nazwa] 게판
   źródło: Passives_Enemy91-4.json :: dataList[id=9007801].name
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [[podstawowe] Pasywka wroga [9007801] — opis] 자신이 체력이 70% 미만이면, 현재 체력이 자신을 제외하고 가장 낮은 아군을 지정함\n아군 공격 시 피해량만큼 체력 회복.\n아군 처치 시 피해량의 2배만큼 체력 회복.
   źródło: Passives_Enemy91-4.json :: dataList[id=9007801].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [[podstawowe] Pasywka wroga [9007901] — nazwa] 게판
   źródło: Passives_Enemy91-4.json :: dataList[id=9007901].name
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [[podstawowe] Pasywka wroga [9007901] — opis] 자신이 체력이 70% 미만이면, 현재 체력이 자신을 제외하고 가장 낮은 아군을 지정함\n아군 공격 시 피해량만큼 체력 회복.\n아군 처치 시 피해량의 2배만큼 체력 회복.
   źródło: Passives_Enemy91-4.json :: dataList[id=9007901].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [[podstawowe] Pasywka wroga [9008001] — nazwa] 게판
   źródło: Passives_Enemy91-4.json :: dataList[id=9008001].name
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [[podstawowe] Pasywka wroga [9008001] — opis] 자신이 체력이 70% 미만이면, 현재 체력이 자신을 제외하고 가장 낮은 아군을 지정함\n아군 공격 시 피해량만큼 체력 회복.\n아군 처치 시 피해량의 2배만큼 체력 회복.
   źródło: Passives_Enemy91-4.json :: dataList[id=9008001].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [[podstawowe] Pasywka wroga [9008101] — nazwa] 게판
   źródło: Passives_Enemy91-4.json :: dataList[id=9008101].name
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [[podstawowe] Pasywka wroga [9008101] — opis] 자신이 체력이 70% 미만이면, 현재 체력이 자신을 제외하고 가장 낮은 아군을 지정함\n아군 공격 시 피해량만큼 체력 회복.\n아군 처치 시 피해량의 2배만큼 체력 회복.
   źródło: Passives_Enemy91-4.json :: dataList[id=9008101].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [[podstawowe] Pasywka wroga [9008102] — nazwa] 오래된 게딱지 탄
   źródło: Passives_Enemy91-4.json :: dataList[id=9008102].name
   limit: do 40 znaków
   EN: Molted Shell Shot
   PL:
727. [[podstawowe] Pasywka wroga [9008102] — opis] 스테이지 시작 시, 오래된 게딱지 탄을 1 얻음
   źródło: Passives_Enemy91-4.json :: dataList[id=9008102].desc
   limit: do 120 znaków
   EN: Encounter Start: Gain 1 Molted Shell Shot
   PL:

## [podstawowe] Pasywka wroga: Passives_check4
- plik gry: `Passives_check4.json`

728. [[podstawowe] Pasywka wroga [1010311] — nazwa] 냉정
   źródło: Passives_check4.json :: dataList[id=1010311].name
   limit: do 40 znaków
   EN: Poised
   PL:
729. [[podstawowe] Pasywka wroga [1010311] — opis] 합 승리 시 호흡 횟수 1 증가\n호흡 횟수 5당 코인 위력 +1 (최대 3)
   źródło: Passives_check4.json :: dataList[id=1010311].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: On Clash Win, gain +1 [Breath] Count\nCoin Power +1 for every 5 [Breath] Count (max 3)
   PL:
730. [[podstawowe] Pasywka wroga [1020211] — nazwa] 자가충전
   źródło: Passives_check4.json :: dataList[id=1020211].name
   limit: do 40 znaków
   EN: Self-charging
   PL:
731. [[podstawowe] Pasywka wroga [1020211] — opis] 공격 종료 시 충전 횟수 1 증가\n공격 종료 시 무작위 아군의 충전 횟수 1 증가
   źródło: Passives_check4.json :: dataList[id=1020211].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain +1 [Charge] Count at Attack End\nA random ally gains +1 [Charge] Count at Attack End
   PL:
732. [[podstawowe] Pasywka wroga [1050311] — nazwa] 견뎌내기
   źródło: Passives_check4.json :: dataList[id=1050311].name
   limit: do 40 znaków
   EN: Enduring Spirit
   PL:
733. [[podstawowe] Pasywka wroga [1050311] — opis] 피격 시 충전 횟수 1 증가 (최대 6회)\n합 패배 시 충전 횟수 1 증가 (최대 6회, 피격 시 조건과 별도로 판정)
   źródło: Passives_check4.json :: dataList[id=1050311].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When attacked, gain +1 Charge Count. (Up to 6 times)\nAfter losing a clash, gain +1 Charge Count. (Up 6 times, counted independently of hits taken)
   PL:
734. [[podstawowe] Pasywka wroga [1070411] — nazwa] 젠장...
   źródło: Passives_check4.json :: dataList[id=1070411].name
   limit: do 40 znaków
   EN: Bugger…
   PL:
735. [[podstawowe] Pasywka wroga [1070411] — opis] 아군이 사망하면 다음 턴 시작 시 정신력이 10 감소하고, 타격 위력 증가 1을 얻음\n생존한 N사 광신도가 파티에 자신 포함 4명 이상 있을 때 코인 위력 +1
   źródło: Passives_check4.json :: dataList[id=1070411].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When an ally is defeated, lose 10 SP and gain 1 Blunt Power Up next turn.\nIf 4 or more surviving units in the team, including this unit, are 'N Corp. Fanatics', Coin Power +1.
   PL:
736. [[podstawowe] Pasywka wroga [1100211] — nazwa] 살수
   źródło: Passives_check4.json :: dataList[id=1100211].name
   limit: do 40 znaków
   EN: Slayer
   PL:
737. [[podstawowe] Pasywka wroga [1100211] — opis] 연결한 죄 중 마지막 죄의 마지막 코인의 피해량 +20%\n자신을 제외한 아군의 스킬로 호흡 횟수가 증가할 때 50% 확률로 자신의 호흡 횟수 1 증가
   źródło: Passives_check4.json :: dataList[id=1100211].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The last Coin on the last skill in the chain deals +20% damage.\nWhenever an ally other than this unit gains Poise Count, this unit gains +1 Poise Count at a 50% chance.
   PL:
738. [[podstawowe] Pasywka wroga [1100211] — podsumowanie] 연결한 죄 중 마지막 죄의 마지막 코인의 피해량 +20%. 호흡 횟수 추가 증가
   źródło: Passives_check4.json :: dataList[id=1100211].summary
   limit: do 120 znaków
   EN: The last Coin on the last Skill in the chain deals +20% damage. Gain additional Poise Count
   PL:
739. [[podstawowe] Pasywka wroga [1020411] — nazwa] 휘파람
   źródło: Passives_check4.json :: dataList[id=1020411].name
   limit: do 40 znaków
   EN: Whistles
   PL:
740. [[podstawowe] Pasywka wroga [1020411] — opis] 전투 시작 시 정신력이 가장 낮은 아군 2명의 정신력 15 회복.\n대상이 N사 광신도면 광신 2 부여
   źródło: Passives_check4.json :: dataList[id=1020411].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [AssemblePersonality]
   znaczenie tagów: [AssemblePersonality] = 광신 / Fanatic
   EN: Combat Start: Heal 15 SP for 2 allies that have the lowest SP\nIf the ally is an "N Corp. Fanatic", also apply 2 [AssemblePersonality]
   PL:
741. [[podstawowe] Pasywka wroga [1020431] — nazwa] 속삭임
   źródło: Passives_check4.json :: dataList[id=1020431].name
   limit: do 40 znaków
   EN: Whispers
   PL:
742. [[podstawowe] Pasywka wroga [1020431] — opis] 전투 시작 시 정신력이 가장 낮은 아군 1명의 정신력 15 회복.\n대상이 N사 광신도면 광신 2 부여
   źródło: Passives_check4.json :: dataList[id=1020431].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [AssemblePersonality]
   znaczenie tagów: [AssemblePersonality] = 광신 / Fanatic
   EN: Combat Start: Heal 15 SP for 1 ally that has the lowest SP\nIf the ally is an "N Corp. Fanatic", also apply 2 [AssemblePersonality]
   PL:
743. [[podstawowe] Pasywka wroga [1100511] — nazwa] 광염
   źródło: Passives_check4.json :: dataList[id=1100511].name
   limit: do 40 znaków
   EN: Mad Flame
   PL:
744. [[podstawowe] Pasywka wroga [1100511] — opis] 합 승리, 적 처치 시 회복하는 정신력 50% 감소\n생존한 N사 광신도가 자신을 포함하여 5명 이상 있을 때, N사 광신도들의 피해량 +10%
   źródło: Passives_check4.json :: dataList[id=1100511].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heal 50% less SP from winning a clash or defeating an enemy.\nIf 5 or more surviving units, including this unit, are 'N Corp. Fanatics', they deal +10% damage.
   PL:
745. [[podstawowe] Pasywka wroga [1070311] — nazwa] 풀 뜯을 준비
   źródło: Passives_check4.json :: dataList[id=1070311].name
   limit: do 40 znaków
   EN: Raring to Graze
   PL:
746. [[podstawowe] Pasywka wroga [1070311] — opis] 다음 턴 시작 시 (분노 공명 수)만큼 충전 횟수 증가.\n충전 횟수가 5 이상이면 신속 1, 공격 위력 증가 1을 얻음\n상시 발동: 스테이지 시작 시 탄환 +3
   źródło: Passives_check4.json :: dataList[id=1070311].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain (Wrath Reson.) Charge Count next turn.\nAt 5+ Charge Count, gain 1 Haste and Attack Power Up.\nAlways Activate: At the start of the stage, gain +3 Ammo.
   PL:
747. [[podstawowe] Pasywka wroga [1050611] — nazwa] rrR-#4 슈트 가압 가동
   źródło: Passives_check4.json :: dataList[id=1050611].name
   limit: do 50 znaków
   EN: Activate rrR-#4 Suit Pressurization
   PL:
748. [[podstawowe] Pasywka wroga [1050611] — opis] 턴 종료 시 충전 횟수 5당 다음 턴의 속도 최대 값 +2 (최대 6)\n턴 시작 시 충전 횟수가 5 이상 있으면 자신의 가장 오른쪽 슬롯 1개에 도발치 3 상승.
   źródło: Passives_check4.json :: dataList[id=1050611].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the end of the turn, gain +2 Max Speed per 5 Charge Count next turn. (Max 6)\nAt the start of the turn, if at 5+ Charge Count, gain 3 Aggro to this unit's rightmost slot.
   PL:
749. [[podstawowe] Pasywka wroga [1080511] — nazwa] 차오르는 액체
   źródło: Passives_check4.json :: dataList[id=1080511].name
   limit: do 40 znaków
   EN: Filling Fluid
   PL:
750. [[podstawowe] Pasywka wroga [1080511] — opis] 공격 스킬로 대상의 체력에 피해를 주지 못한 경우, 다음 턴에 최대 체력의 10%만큼 보호막을 얻음 (최대 30)
   źródło: Passives_check4.json :: dataList[id=1080511].desc
   limit: do 160 znaków
   EN: If this unit fails to deal HP damage using attack skills in a turn, gain a Shield equal to 10% of Max HP next turn. (Max 30)
   PL:
751. [[podstawowe] Pasywka wroga [1080211] — nazwa] 뇌파집속
   źródło: Passives_check4.json :: dataList[id=1080211].name
   limit: do 40 znaków
   EN: Brainwave Focus
   PL:
752. [[podstawowe] Pasywka wroga [1080211] — opis] 전투 시작 시 공격 위력 증가를 (우울 공명 수/3)만큼 얻음\n턴 종료 시 이번 턴에 피해를 주지 못한 경우 정신력 -15
   źródło: Passives_check4.json :: dataList[id=1080211].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the combat phase, gain (Gloom Reson. / 3) Attack Power Up.\nIf this unit fails to deal damage this turn, lose 15 SP at the end of the turn.
   PL:
753. [[podstawowe] Pasywka wroga [1040511] — nazwa] 차원 마검
   źródło: Passives_check4.json :: dataList[id=1040511].name
   limit: do 40 znaków
   EN: Dimensional Demon Edge
   PL:
754. [[podstawowe] Pasywka wroga [1040511] — opis] 적 처치 시 충전 횟수 3 증가 (턴 당 최대 3회 발동)
   źródło: Passives_check4.json :: dataList[id=1040511].desc
   limit: do 120 znaków
   EN: Upon defeating an enemy, gain +3 Charge Count (3 times per turn)
   PL:
755. [[podstawowe] Pasywka wroga [1040531] — nazwa] 차원 굴절 칼날 - Type: Blade Mk7
   źródło: Passives_check4.json :: dataList[id=1040531].name
   limit: do 70 znaków
   EN: Dimensional Refraction Edge - Type: Blade Mk7
   PL:
756. [[podstawowe] Pasywka wroga [1040531] — opis] 최대 체력이 가장 낮은 아군 1명이 적 처치 시 충전 횟수 3 증가 (턴 당 최대 1회 발동)
   źródło: Passives_check4.json :: dataList[id=1040531].desc
   limit: do 130 znaków
   EN: When an ally with the lowest Max HP defeats an enemy, they gain +3 Charge Count (Once per turn)
   PL:
757. [[podstawowe] Pasywka wroga [1060611] — nazwa] 익숙해진 정리 업무
   źródło: Passives_check4.json :: dataList[id=1060611].name
   limit: do 40 znaków
   EN: Cleanup Mastery
   PL:
758. [[podstawowe] Pasywka wroga [1060611] — opis] 전투 시작 시 충전 횟수가 5 이상 있으면, 다음 턴에 신속 2를 얻음.<style="highlight">충전 횟수가 10 이상 있으면, 신속 1을 추가로 얻음.</style>
   źródło: Passives_check4.json :: dataList[id=1060611].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: If at 5+ Charge Count at the start of the combat phase, gain 2 Haste. <style="highlight">At 10+ Charge Count, gain 1 additional Haste.</style>
   PL:

## [refraction] Wróg / część: Enemies_Refraction
- plik gry: `Enemies_Refraction.json`

759. [[refraction] Wróg / część [8501] — nazwa] 기억속 어긋난 패잔병
   źródło: Enemies_Refraction.json :: dataList[id=8501].name
   limit: do 40 znaków
   EN: Recollected Awry Soldier
   PL:
760. [[refraction] Wróg / część [8501] — opis] 본체
   źródło: Enemies_Refraction.json :: dataList[id=8501].desc
   limit: do 120 znaków
   EN: Core
   PL:
761. [[refraction] Wróg / część [850101] — nazwa] 몸통
   źródło: Enemies_Refraction.json :: dataList[id=850101].name
   limit: do 40 znaków
   EN: Body
   PL:
762. [[refraction] Wróg / część [850101] — opis] 부위
   źródło: Enemies_Refraction.json :: dataList[id=850101].desc
   limit: do 120 znaków
   EN: Part
   PL:
763. [[refraction] Wróg / część [8502] — nazwa] 기억속 절망하는 패잔병
   źródło: Enemies_Refraction.json :: dataList[id=8502].name
   limit: do 50 znaków
   EN: Recollected Wallowing Soldier
   PL:
764. [[refraction] Wróg / część [8502] — opis] 본체
   źródło: Enemies_Refraction.json :: dataList[id=8502].desc
   (powtórzenie elementu 760 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [[refraction] Wróg / część [850201] — nazwa] 몸통
   źródło: Enemies_Refraction.json :: dataList[id=850201].name
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [[refraction] Wróg / część [850201] — opis] 부위
   źródło: Enemies_Refraction.json :: dataList[id=850201].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [[refraction] Wróg / część [8503] — nazwa] 기억속 침식된 패잔병
   źródło: Enemies_Refraction.json :: dataList[id=8503].name
   limit: do 50 znaków
   EN: Recollected Overtaken Soldier
   PL:
768. [[refraction] Wróg / część [8503] — opis] 본체
   źródło: Enemies_Refraction.json :: dataList[id=8503].desc
   (powtórzenie elementu 760 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [[refraction] Wróg / część [850301] — nazwa] 몸통
   źródło: Enemies_Refraction.json :: dataList[id=850301].name
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [[refraction] Wróg / część [850301] — opis] 부위
   źródło: Enemies_Refraction.json :: dataList[id=850301].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [[refraction] Wróg / część [8504] — nazwa] 기억속 짓물린 G사 부장
   źródło: Enemies_Refraction.json :: dataList[id=8504].name
   limit: do 60 znaków
   EN: Recollected Festered G Corp. H. Manager
   PL:
772. [[refraction] Wróg / część [8504] — opis] 본체
   źródło: Enemies_Refraction.json :: dataList[id=8504].desc
   (powtórzenie elementu 760 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [[refraction] Wróg / część [850401] — nazwa] 몸통
   źródło: Enemies_Refraction.json :: dataList[id=850401].name
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [[refraction] Wróg / część [850401] — opis] 부위
   źródło: Enemies_Refraction.json :: dataList[id=850401].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [[refraction] Wróg / część [8505] — nazwa] 흥겨운 마리아치 조직원
   źródło: Enemies_Refraction.json :: dataList[id=8505].name
   limit: do 40 znaków
   EN: Mariachi Alegre
   PL:
776. [[refraction] Wróg / część [8505] — opis] 본체
   źródło: Enemies_Refraction.json :: dataList[id=8505].desc
   (powtórzenie elementu 760 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [[refraction] Wróg / część [850501] — nazwa] 몸통
   źródło: Enemies_Refraction.json :: dataList[id=850501].name
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [[refraction] Wróg / część [850501] — opis] 부위
   źródło: Enemies_Refraction.json :: dataList[id=850501].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [[refraction] Wróg / część [8506] — nazwa] 경쾌한 마리아치 조직원
   źródło: Enemies_Refraction.json :: dataList[id=8506].name
   limit: do 40 znaków
   EN: Mariachi Vivaz
   PL:
780. [[refraction] Wróg / część [8506] — opis] 본체
   źródło: Enemies_Refraction.json :: dataList[id=8506].desc
   (powtórzenie elementu 760 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [[refraction] Wróg / część [850601] — nazwa] 몸통
   źródło: Enemies_Refraction.json :: dataList[id=850601].name
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [[refraction] Wróg / część [850601] — opis] 부위
   źródło: Enemies_Refraction.json :: dataList[id=850601].desc
   (powtórzenie elementu 762 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
