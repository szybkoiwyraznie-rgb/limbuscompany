# Paczka AI P77 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 13/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P77_3c_przeciwnicy_i_anomalie_cz13.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P77_3c_przeciwnicy_i_anomalie_cz13.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [mirror] Umiejętności wrogów / Anomalii — Skills_Abnormality_Mirror
- grupa rozdziału/trybu: `mirror` · plik: `Skills_Abnormality_Mirror.json`

1. [Umiejętność wroga [809005] (ulepszenie 1) — opis] 고양을 가진 대상 우선 공격\n대상에게 취기 가 없다면, 합 위력 +5
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809005].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Prioritizes enemies with Morale Boost\nIf target has no Tipsy, Clash Power +5
   PL:
2. [Umiejętność wroga [809005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 고양 을 가지고 있다면, 고양 만큼 피해량 +100%
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Morale Boost, deal +100% damage for each Count
   PL:
3. [Umiejętność wroga [809005] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 취기 를 가지고 있다면, 주는 피해가 0이 되고 자신의 체력 -50
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809005].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Tipsy, deal 0 damage, and user loses 50 HP
   PL:
4. [Umiejętność wroga [809005] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 고양 혹은 취기 전부 소모 시킴
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809005].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Remove all Morale Boost or Tipsy
   PL:
5. [Umiejętność wroga [809006] (ulepszenie 1) — nazwa] 이번에는 안돼!
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809006].levelList[level=1].name
   limit: do 40 znaków
   EN: Not This Time!
   PL:
6. [Umiejętność wroga [809006] (ulepszenie 1) — opis] 요정주 우선 대상 공격
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809006].levelList[level=1].desc
   limit: do 120 znaków
   EN: Prioritizes Fairy Wine
   PL:
7. [Umiejętność wroga [809006] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 요정주를 공격했다면, 다음 턴에 체력 10% 회복, 공격 위력 증가 2, 신속 2, 보호 2를 얻음.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If this attacks Fairy Wine, heal 10% HP next turn, and gain 2 Attack Power Up, 2 Haste, and 2 Protection
   PL:
8. [Umiejętność wroga [809007] (ulepszenie 1) — nazwa] 이 요정주가 좋나?
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809007].levelList[level=1].name
   limit: do 40 znaków
   EN: You Like This Brew?
   PL:
9. [Umiejętność wroga [809007] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 속박 1 얻음
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809007].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Bind next turn
   PL:
10. [Umiejętność wroga [809101] (ulepszenie 1) — nazwa] 요정주
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809101].levelList[level=1].name
   limit: do 40 znaków
   EN: Fairy Wine
   PL:
11. [Umiejętność wroga [809101] (ulepszenie 1) — opis] [WhenUse] 상대의 고양을 수치만큼 취기로 변환
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Convert opponent's Morale Boost into Tipsy
   PL:
12. [Umiejętność wroga [809201] (ulepszenie 1) — nazwa] 상처 훑기
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809201].levelList[level=1].name
   limit: do 40 znaków
   EN: Skim Wounds
   PL:
13. [Umiejętność wroga [809201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 출혈을 가지고 있다면, 마비 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed, inflict 1 Paralyze
   PL:
14. [Umiejętność wroga [809201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Bleed Count
   PL:
15. [Umiejętność wroga [809201] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 출혈 횟수가 2 이상이면 출혈 5 부여.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809201].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 2+ Bleed Count, inflict 5 Bleed
   PL:
16. [Umiejętność wroga [809202] (ulepszenie 1) — nazwa] 옭아매인 상처
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809202].levelList[level=1].name
   limit: do 40 znaków
   EN: Entangled Injury
   PL:
17. [Umiejętność wroga [809202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 출혈을 가지고 있다면, 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed, inflict 1 Bind next turn
   PL:
18. [Umiejętność wroga [809202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL:
19. [Umiejętność wroga [809203] (ulepszenie 1) — nazwa] 묻어오는 살점
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809203].levelList[level=1].name
   limit: do 40 znaków
   EN: Smeared Flesh
   PL:
20. [Umiejętność wroga [809203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
21. [Umiejętność wroga [809203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 출혈을 가지고 있다면, 체력 20 회복
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed, heal 20 HP
   PL:
22. [Umiejętność wroga [809203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 출혈 횟수가 2 이상이면 출혈 5 부여.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
23. [Umiejętność wroga [809204] (ulepszenie 1) — nazwa] 드리우는 그늘
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809204].levelList[level=1].name
   limit: do 40 znaków
   EN: Casting Shade
   PL:
24. [Umiejętność wroga [809204] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 거대 클로버 생성\n[DefeatDuel] 거대 클로버의 체력이 70%인 상태로 생성됨.
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Spawn a Giant Clover next turn\n[DefeatDuel] The Giant Clover spawns with 70% HP
   PL:
25. [Umiejętność wroga [809204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 전부 소모
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Remove all Bleed Count
   PL:
26. [Umiejętność wroga [809205] (ulepszenie 1) — nazwa] 소화
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809205].levelList[level=1].name
   limit: do 40 znaków
   EN: Churning
   PL:
27. [Umiejętność wroga [809205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 출혈당 자신의 전체 체력의 1%만큼 회복\n출혈 횟수 전부 소모
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal by 1% of Max HP per target's Bleed\nRemove all Bleed Count
   PL:
28. [Umiejętność wroga [809401] (ulepszenie 1) — nazwa] 발아
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809401].levelList[level=1].name
   limit: do 40 znaków
   EN: Sprout
   PL:
29. [Umiejętność wroga [809402] (ulepszenie 1) — nazwa] 황금 과실
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809402].levelList[level=1].name
   limit: do 40 znaków
   EN: Golden Fruit
   PL:
30. [Umiejętność wroga [809402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [DefeatDuel] 자신에게 피해 20
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Take 20 damage
   PL:
31. [Umiejętność wroga [809402] (ulepszenie 1) — moneta 1, efekt 2 — opis] [DefeatDuel] 황금빛 1 잃음
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Lose 1 Golden Sheen
   PL:
32. [Umiejętność wroga [809403] (ulepszenie 1) — nazwa] 단단한 황금
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809403].levelList[level=1].name
   limit: do 40 znaków
   EN: Solid Gold
   PL:
33. [Umiejętność wroga [809501] (ulepszenie 1) — nazwa] 영양분 흡수
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809501].levelList[level=1].name
   limit: do 40 znaków
   EN: Absorb Nutrients
   PL:
34. [Umiejętność wroga [809501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 본체의 체력 3 회복
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Core heals 3 HP
   PL:
35. [Umiejętność wroga [809502] (ulepszenie 1) — nazwa] 허물어지는 과육
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809502].levelList[level=1].name
   limit: do 40 znaków
   EN: Deteriorating Flesh
   PL:
36. [Umiejętność wroga [809502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 횟수 3 증가
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Bleed Count next turn
   PL:
37. [Umiejętność wroga [809502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 취약 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Fragile next turn
   PL:
38. [Umiejętność wroga [809503] (ulepszenie 1) — nazwa] 포획
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809503].levelList[level=1].name
   limit: do 40 znaków
   EN: Entangle
   PL:
39. [Umiejętność wroga [809503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 본체의 체력 10 회복
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Core heals 10 HP
   PL:
40. [Umiejętność wroga [809503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 출혈 5 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Bleed next turn
   PL:
41. [Umiejętność wroga [809601] (ulepszenie 1) — nazwa] 들이받기
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809601].levelList[level=1].name
   limit: do 40 znaków
   EN: Ram
   PL:
42. [Umiejętność wroga [809601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Burn
   PL:
43. [Umiejętność wroga [809601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 3 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Umiejętność wroga [809602] (ulepszenie 1) — nazwa] 찍어누르기
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809602].levelList[level=1].name
   limit: do 40 znaków
   EN: Pin Down
   PL:
45. [Umiejętność wroga [809602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 3 증가
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Burn Count
   PL:
46. [Umiejętność wroga [809603] (ulepszenie 1) — nazwa] 돌진
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809603].levelList[level=1].name
   limit: do 40 znaków
   EN: Charge In
   PL:
47. [Umiejętność wroga [809603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Burn
   PL:
48. [Umiejętność wroga [809603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 20% of damage dealt
   PL:
49. [Umiejętność wroga [809603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
50. [Umiejętność wroga [809603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Umiejętność wroga [809603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Umiejętność wroga [809603] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809603].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [Umiejętność wroga [809604] (ulepszenie 1) — nazwa] 넘쳐흐르는 슬픔
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809604].levelList[level=1].name
   limit: do 40 znaków
   EN: Overflowing Sorrow
   PL:
54. [Umiejętność wroga [809604] (ulepszenie 1) — opis] [DefeatDuel] 해소되지 않은 슬픔 1을 얻음
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Gain 1 Unresolved Sorrow
   PL:
55. [Umiejętność wroga [809604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력 15 감소
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 15 SP
   PL:
56. [Umiejętność wroga [809604] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 50%만큼 대상의 흐트러짐 손상
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809604].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 50% of damage dealt
   PL:
57. [Umiejętność wroga [809605] (ulepszenie 1) — nazwa] 뜨거운 울음소리
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809605].levelList[level=1].name
   limit: do 40 znaków
   EN: Heated Cries
   PL:
58. [Umiejętność wroga [809605] (ulepszenie 1) — opis] [WinDuel] 다음 턴에 신속, 공격 위력 증가 1을 얻음
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809605].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 1 Haste and 1 Attack Power Up next turn
   PL:
59. [Umiejętność wroga [809605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 울렁이는 감정 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Wavering Emotions
   PL:
60. [Umiejętność wroga [809605] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 침잠 횟수 3 증가
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809605].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Sinking Count
   PL:
61. [Umiejętność wroga [809606] (ulepszenie 1) — nazwa] 뜨거운 비명소리
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809606].levelList[level=1].name
   limit: do 40 znaków
   EN: Heated Screams
   PL:
62. [Umiejętność wroga [809606] (ulepszenie 1) — opis] [WinDuel] 다음 턴에 신속, 공격 위력 증가 1을 얻음
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809606].levelList[level=1].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [Umiejętność wroga [809606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 울렁이는 감정 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [Umiejętność wroga [809606] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809606].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Sinking
   PL:
65. [Umiejętność wroga [809606] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 울렁이는 감정 1 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809606].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Umiejętność wroga [809606] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills_Abnormality_Mirror.json :: dataList[id=809606].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [mirror4] Wróg / część: Enemies-mirror4
- plik gry: `Enemies-mirror4.json`

67. [[mirror4] Wróg / część [8175] — nazwa] 분노를 머금은 장미
   źródło: Enemies-mirror4.json :: dataList[id=8175].name
   limit: do 40 znaków
   EN: Wrath-drenched Rose
   PL:
68. [[mirror4] Wróg / część [8175] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8175].desc
   limit: do 120 znaków
   EN: Core
   PL:
69. [[mirror4] Wróg / część [8176] — nazwa] 색욕을 머금은 장미
   źródło: Enemies-mirror4.json :: dataList[id=8176].name
   limit: do 40 znaków
   EN: Lust-drenched Rose
   PL:
70. [[mirror4] Wróg / część [8176] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8176].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
71. [[mirror4] Wróg / część [8177] — nazwa] 나태를 머금은 장미
   źródło: Enemies-mirror4.json :: dataList[id=8177].name
   limit: do 40 znaków
   EN: Sloth-drenched Rose
   PL:
72. [[mirror4] Wróg / część [8177] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8177].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [[mirror4] Wróg / część [8178] — nazwa] 탐식을 머금은 장미
   źródło: Enemies-mirror4.json :: dataList[id=8178].name
   limit: do 40 znaków
   EN: Gluttony-drenched Rose
   PL:
74. [[mirror4] Wróg / część [8178] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8178].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [[mirror4] Wróg / część [8179] — nazwa] 우울을 머금은 장미
   źródło: Enemies-mirror4.json :: dataList[id=8179].name
   limit: do 40 znaków
   EN: Gloom-drenched Rose
   PL:
76. [[mirror4] Wróg / część [8179] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8179].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [[mirror4] Wróg / część [8180] — nazwa] 오만을 머금은 장미
   źródło: Enemies-mirror4.json :: dataList[id=8180].name
   limit: do 40 znaków
   EN: Pride-drenched Rose
   PL:
78. [[mirror4] Wróg / część [8180] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8180].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [[mirror4] Wróg / część [8181] — nazwa] 질투를 머금은 장미
   źródło: Enemies-mirror4.json :: dataList[id=8181].name
   limit: do 40 znaków
   EN: Envy-drenched Rose
   PL:
80. [[mirror4] Wróg / część [8181] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8181].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [[mirror4] Wróg / część [8182] — nazwa] 개화 E.G.O::마름
   źródło: Enemies-mirror4.json :: dataList[id=8182].name
   limit: do 40 znaków
   EN: Effloresced E.G.O::Farmwatch
   PL:
82. [[mirror4] Wróg / część [8182] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8182].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [[mirror4] Wróg / część [8183] — nazwa] 욕망의 나무
   źródło: Enemies-mirror4.json :: dataList[id=8183].name
   limit: do 40 znaków
   EN: Tree of Desires
   PL:
84. [[mirror4] Wróg / część [8183] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8183].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [[mirror4] Wróg / część [8184] — nazwa] 흡수하는 나무
   źródło: Enemies-mirror4.json :: dataList[id=8184].name
   limit: do 40 znaków
   EN: Absorbing Tree
   PL:
86. [[mirror4] Wróg / część [8184] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8184].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [[mirror4] Wróg / część [8197] — nazwa] 홍염나방
   źródło: Enemies-mirror4.json :: dataList[id=8197].name
   limit: do 40 znaków
   EN: Ardor Blossom Moth
   PL:
88. [[mirror4] Wróg / część [8197] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8197].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [[mirror4] Wróg / część [8198] — nazwa] 머금은 목화
   źródło: Enemies-mirror4.json :: dataList[id=8198].name
   limit: do 40 znaków
   EN: Drenched Gossypium
   PL:
90. [[mirror4] Wróg / część [8198] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8198].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [[mirror4] Wróg / część [8199] — nazwa] 경멸의 나선
   źródło: Enemies-mirror4.json :: dataList[id=8199].name
   limit: do 40 znaków
   EN: Spiral of Contempt
   PL:
92. [[mirror4] Wróg / część [8199] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8199].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [[mirror4] Wróg / część [8200] — nazwa] 손아귀
   źródło: Enemies-mirror4.json :: dataList[id=8200].name
   limit: do 40 znaków
   EN: Grasp
   PL:
94. [[mirror4] Wróg / część [8200] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8200].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [[mirror4] Wróg / część [8201] — nazwa] 장미 표지판
   źródło: Enemies-mirror4.json :: dataList[id=8201].name
   limit: do 40 znaków
   EN: Sign of Roses
   PL:
96. [[mirror4] Wróg / część [8201] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8201].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [[mirror4] Wróg / część [8118] — nazwa] 증기 운반 기계
   źródło: Enemies-mirror4.json :: dataList[id=8118].name
   limit: do 40 znaków
   EN: Steam Transport Machine
   PL:
98. [[mirror4] Wróg / część [8118] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8118].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [[mirror4] Wróg / część [8119] — nazwa] 길 잃은 승객
   źródło: Enemies-mirror4.json :: dataList[id=8119].name
   limit: do 40 znaków
   EN: Wayward Passenger
   PL:
100. [[mirror4] Wróg / część [8119] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8119].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [[mirror4] Wróg / część [8120] — nazwa] 피가 흐르는 차원
   źródło: Enemies-mirror4.json :: dataList[id=8120].name
   limit: do 40 znaków
   EN: Hemorrhaging Dimension
   PL:
102. [[mirror4] Wróg / część [8120] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8120].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [[mirror4] Wróg / część [8121] — nazwa] 독이 들끓는 차원
   źródło: Enemies-mirror4.json :: dataList[id=8121].name
   limit: do 40 znaków
   EN: Poisonous Dimension
   PL:
104. [[mirror4] Wróg / część [8121] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8121].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [[mirror4] Wróg / część [8122] — nazwa] 끊임없이 진동하는 차원
   źródło: Enemies-mirror4.json :: dataList[id=8122].name
   limit: do 40 znaków
   EN: Tremoring Dimension
   PL:
106. [[mirror4] Wróg / część [8122] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8122].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [[mirror4] Wróg / część [8123] — nazwa] 전류를 뿜어내는 차원
   źródło: Enemies-mirror4.json :: dataList[id=8123].name
   limit: do 40 znaków
   EN: Electrifying Dimension
   PL:
108. [[mirror4] Wróg / część [8123] — opis] 본체
   źródło: Enemies-mirror4.json :: dataList[id=8123].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [mirror6] Umiejętności wrogów / Anomalii — Skills_Abnormality_Mirror6
- grupa rozdziału/trybu: `mirror6` · plik: `Skills_Abnormality_Mirror6.json`

109. [Umiejętność wroga [123901] (ulepszenie 1) — nazwa] 끝나지 않는 축제
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=123901].levelList[level=1].name
   limit: do 40 znaków
   EN: The Infinite Parade
   PL:
110. [Umiejętność wroga [123901] (ulepszenie 1) — opis] [CantDuel]\n대상이 수비 스킬을 사용했으면 피해를 받지 않음\n[WhenUse] 다음 턴에 곤돌라 1개를 생성
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=123901].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]
   EN: [CantDuel]\nIf the target used a Defense Skill, the target does not take damage\n[WhenUse] Generate 1 Gondola next turn
   PL:
111. [Umiejętność wroga [123902] (ulepszenie 1) — nazwa] 영원한 축제
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=123902].levelList[level=1].name
   limit: do 40 znaków
   EN: The Eternal Festival
   PL:
112. [Umiejętność wroga [123902] (ulepszenie 1) — opis] [CantDuel]\n대상이 수비 스킬을 사용했으면 피해를 받지 않음\n[WhenUse] 다음 턴에 곤돌라 4개를 생성
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=123902].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]
   EN: [CantDuel]\nIf the target used a Defense Skill, the target does not take damage\n[WhenUse] Generate 4 Gondola next turn
   PL:
113. [Umiejętność wroga [124001] (ulepszenie 1) — nazwa] 타는 갈증
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124001].levelList[level=1].name
   limit: do 40 znaków
   EN: Burning Thirst
   PL:
114. [Umiejętność wroga [124001] (ulepszenie 1) — opis] 자신이 소모한 [BloodDinner] 100당 최종 위력 +1 (최대 5)\n[WhenUse] 대상의 [Laceration] 5당 기본 위력 +1 (최대 3)\n[WhenUse] [BloodDinner]을 최대 30 소모하여 소모한 [BloodDinner] 10당 [RegainedStrength] 1 얻음\n[DefeatDuel] 정신력 3 감소
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124001].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [WhenUse], [Laceration], [RegainedStrength], [DefeatDuel]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Final Power +1 for every 100 [BloodDinner] this unit consumed (max 5)\n[WhenUse] Base Power +1 for every 5 [Laceration] on the target (max 3)\n[WhenUse] Consume up to 30 [BloodDinner]: gain 1 [RegainedStrength] for every 10 [BloodDinner] consumed\n[DefeatDuel] Lose 3 SP
   PL:
115. [Umiejętność wroga [124001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +2 [Laceration] Count
   PL:
116. [Umiejętność wroga [124001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
117. [Umiejętność wroga [124002] (ulepszenie 1) — nazwa] 꿰뚫려라
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124002].levelList[level=1].name
   limit: do 40 znaków
   EN: Be Impaled
   PL:
118. [Umiejętność wroga [124002] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 40 소모하여 소모한 [BloodDinner] 10당 [RegainedStrength] 1 얻고 정신력 3 회복\n\n[DefeatDuel] 정신력 3 감소
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124002].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [RegainedStrength], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Consume up to 40 [BloodDinner]: gain 1 [RegainedStrength] and heal 3 SP for every 10 [BloodDinner] consumed\n\n[DefeatDuel] Lose 3 SP
   PL:
119. [Umiejętność wroga [124002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 최대 체력의 20%만큼 색욕 피해를 줌
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal Lust damage equal to 20% of the target's max HP
   PL:
120. [Umiejętność wroga [124002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 최대 체력의 20%만큼 색욕 피해를 줌
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Umiejętność wroga [124003] (ulepszenie 1) — nazwa] 돈키호테류 경혈 2식 - 말뚝
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124003].levelList[level=1].name
   limit: do 50 znaków
   EN: Don Quixote Hardblood Arts 2 - Stake
   PL:
122. [Umiejętność wroga [124003] (ulepszenie 1) — opis] [Laceration]이 가장 많이 부여된 대상 공격\n자신이 소모한 [BloodDinner] 100당 최종 위력 +1 (최대 5)\n[WhenUse] 대상의 [Laceration] 5당 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124003].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner], [WhenUse]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [WhenUse] = [사용시] / [On Use]
   EN: Attacks the target with the most [Laceration]\nFinal Power +1 for every 100 [BloodDinner] this unit consumed (max 5)\n[WhenUse] Coin Power +1 for every 5 [Laceration] on target (max 2)
   PL:
123. [Umiejętność wroga [124003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +2 [Laceration] Count
   PL:
124. [Umiejętność wroga [124003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
125. [Umiejętność wroga [124003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
126. [Umiejętność wroga [124003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Umiejętność wroga [124003] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] (대상의 [Laceration] 위력 X 횟수)만큼 색욕 피해를 줌
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Deal Lust damage equal to ([Laceration] Potency x Count)
   PL:
128. [Umiejętność wroga [124004] (ulepszenie 1) — nazwa] 경혈식 쐐기
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124004].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Wedge
   PL:
129. [Umiejętność wroga [124004] (ulepszenie 1) — opis] 자신이 소모한 [BloodDinner] 100당 최종 위력 +1 (최대 5)\n[StartBattle] 자신의 [RegainedStrength] 3당 가중치 +1 (최대 2)\n[EndSkill] [RegainedStrength] 3 소모\n[DefeatDuel] 최종 피해량 -80%
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124004].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [StartBattle], [RegainedStrength], [EndSkill], [DefeatDuel]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [StartBattle] = [전투 시작시] / [Combat Start]; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [EndSkill] = [공격 종료시] / [Attack End]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Final Power +1 for every 100 [BloodDinner] this unit consumed (max 5)\n[StartBattle] Atk Weight +1 for every 3 [RegainedStrength] on self (max 2)\n[EndSkill] Consume 3 [RegainedStrength]\n[DefeatDuel] Deal -80% final damage
   PL:
130. [Umiejętność wroga [124004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
131. [Umiejętność wroga [124004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +3 [Laceration] Count
   PL:
132. [Umiejętność wroga [124004] (ulepszenie 1) — moneta 1, efekt 3 — opis] [WinDuelAttack] [Burst] 3 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124004].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [Burst]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [Burst] = 파열 / Rupture
   EN: [WinDuelAttack] Inflict 3 [Burst]
   PL:
133. [Umiejętność wroga [124004] (ulepszenie 1) — moneta 1, efekt 4 — opis] [DefeatDuelAttack] [RegainedStrength] 1 소모
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124004].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuelAttack], [RegainedStrength]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust
   EN: [DefeatDuelAttack] Consume 1 [RegainedStrength]
   PL:
134. [Umiejętność wroga [124004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Umiejętność wroga [124004] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124004].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
136. [Umiejętność wroga [124004] (ulepszenie 1) — moneta 2, efekt 3 — opis] [WinDuelAttack] [Burst] 3 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124004].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 132 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Umiejętność wroga [124004] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124004].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Umiejętność wroga [124005] (ulepszenie 1) — nazwa] 피의 욕망
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124005].levelList[level=1].name
   limit: do 40 znaków
   EN: Desire for Blood
   PL:
139. [Umiejętność wroga [124005] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 40 소모하여 소모한 [BloodDinner] 10당 [RegainedStrength] 1 얻고 정신력 5 회복\n[WhenUse] [RegainedStrength] 5당 부여하는 [Laceration] 횟수 1증가 (최대 2)\n[DefeatDuel] 최종 피해량 -80%
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124005].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [RegainedStrength], [Laceration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Consume up to 40 [BloodDinner]: gain 1 [RegainedStrength] and heal 5 SP for every 10 [BloodDinner] consumed\n[WhenUse] Inflict +1 more [Laceration] Count for every 5 [RegainedStrength] (max 2)\n[DefeatDuel] Deal -80% final damage
   PL:
140. [Umiejętność wroga [124005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Umiejętność wroga [124005] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124005].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
142. [Umiejętność wroga [124005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność wroga [124005] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124005].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Umiejętność wroga [124005] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124005].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Umiejętność wroga [124005] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124005].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Umiejętność wroga [124005] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124005].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Umiejętność wroga [124005] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124005].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL:
148. [Umiejętność wroga [124006] (ulepszenie 1) — nazwa] 혈찬의 시간
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124006].levelList[level=1].name
   limit: do 40 znaków
   EN: Moment of Bloodfeast
   PL:
149. [Umiejętność wroga [124006] (ulepszenie 1) — opis] [CantIdentify]\n[WhenUse] [BloodDinner]을 최대 300 소모하여 소모한 [BloodDinner] 10당 [RegainedStrength] 1 얻고 정신력 3 회복\n[WhenUse] [BloodDinner]을 소모했으면 정신력 30 회복\n[DefeatDuel] 최종 피해량 -80%
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124006].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WhenUse], [BloodDinner], [RegainedStrength], [DefeatDuel]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [CantIdentify]\n[WhenUse] Consume up to 300 [BloodDinner]: gain 1 [RegainedStrength] and heal 3 SP for every 10 [BloodDinner] consumed\n[WhenUse] If this unit consumed [BloodDinner], heal 30 SP\n[DefeatDuel] Deal -80% final damage
   PL:
150. [Umiejętność wroga [124006] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Umiejętność wroga [124007] (ulepszenie 1) — nazwa] 돈키호테류 경혈 4식 - 도려내기
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124007].levelList[level=1].name
   limit: do 60 znaków
   EN: Don Quixote Hardblood Arts 4 - Sundering
   PL:
152. [Umiejętność wroga [124007] (ulepszenie 1) — opis] 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음.\n[WhenUse] [BloodDinner]을 최대 100 소모하여 소모한 [BloodDinner] 10당 [RegainedStrength] 1 얻고 정신력 15 회복\n[WhenUse] 자신의 [BloodDinner_Accumulation] 수치 30당 합 위력 +1 (최대 15)\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음.\n[EndSkill] 증가한 합 위력만큼 이번 턴과 다음 턴에 [AttackDown], [DefenseDown]를 얻음. (최대 15)\n[DefeatDuel] 최종 피해량 -80%
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124007].levelList[level=1].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [RegainedStrength], [BloodDinner_Accumulation], [DefeatDuel], [EndSkill], [AttackDown], [DefenseDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Cannot be Staggered until he uses this Skill.\n[WhenUse] Consume up to 100 [BloodDinner]: gain 1 [RegainedStrength] and heal 15 SP for every 10 [BloodDinner] consumed\n[WhenUse] Clash Power +1 for every 30 [BloodDinner_Accumulation] by this unit (max 15)\n[DefeatDuel] Deal -50% damage, and the damage from this Skill does not Stagger the target.\n[EndSkill] For this turn and next turn, gain [AttackDown] and [DefenseDown] equal to the Clash Power gained with this Skill. (max 15)\n[DefeatDuel] Deal -80% final damage
   PL:
153. [Umiejętność wroga [124007] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124007].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Umiejętność wroga [124007] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124007].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 8 [Laceration]
   PL:
155. [Umiejętność wroga [124007] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [RegainedStrength] 2 소모
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124007].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RegainedStrength]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust
   EN: [OnSucceedAttack] Consume 2 [RegainedStrength]
   PL:
156. [Umiejętność wroga [124008] (ulepszenie 1) — nazwa] 돈키호테류 경혈 14식 망토
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124008].levelList[level=1].name
   limit: do 60 znaków
   EN: Don Quixote Hardblood Arts 14: Mantle
   PL:
157. [Umiejętność wroga [124008] (ulepszenie 1) — opis] 자신이 소모한 [BloodDinner] 100당 기본 위력 +1 (최대 10)\n[DuelGuard]\n[WinDuel] 대상에게 [Laceration] 4, [Burst] 4 부여\n[DefeatDuel] [RegainedStrength] 2 소모
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124008].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [DuelGuard], [WinDuel], [Laceration], [Burst], [DefeatDuel], [RegainedStrength]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [DuelGuard] = [합 가능 가드] / [Clashable Guard]; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust
   EN: Base Power +1 for every 100 [BloodDinner] this unit consumed (max 10)\n[DuelGuard]\n[WinDuel] Inflict 4 [Laceration] and [Burst]\n[DefeatDuel] Consume 2 [RegainedStrength]
   PL:
158. [Umiejętność wroga [124008] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124008].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Umiejętność wroga [124009] (ulepszenie 1) — nazwa] 약하디 약하구나
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124009].levelList[level=1].name
   limit: do 40 znaków
   EN: Frail, So Frail
   PL:
160. [Umiejętność wroga [124009] (ulepszenie 1) — opis] [DuelCounter]\n[RegainedStrength] 5당 기본 위력 +1\n대상의 [Laceration] 5당 코인 위력 +1 (최대 2)\n[DefeatDuel] 정신력 3 감소
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124009].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [RegainedStrength], [Laceration], [DefeatDuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DuelCounter]\nBase Power +1 for every 5 [RegainedStrength]\nCoin Power +1 for every 5 [Laceration] on the target (max 2)\n[DefeatDuel] Lose 3 SP
   PL:
161. [Umiejętność wroga [124009] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124009].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [Umiejętność wroga [124009] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124009].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Umiejętność wroga [124010] (ulepszenie 1) — nazwa] 블러디 메리 고 라운드
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124010].levelList[level=1].name
   limit: do 40 znaków
   EN: Bloody-Merry-Go-Round
   PL:
164. [Umiejętność wroga [124010] (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] 적에게 피해를 주지 않으며, 다음 턴에 굳어진 꿈을 생성함\n[WhenUse] [RegainedStrength] 5당 부여하는 [Laceration] 횟수 1증가 (최대 2)
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124010].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [RegainedStrength], [Laceration]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [Laceration] = 출혈 / Bleed
   EN: [CantDuel]\n[WhenUse] Does not deal any damage against enemies; generate Coagulated Dream units next turn\n[WhenUse] For every 5 [RegainedStrength], inflict +1 more [Laceration] Count (max 2)
   PL:
165. [Umiejętność wroga [124010] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124010].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Umiejętność wroga [124010] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124010].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Umiejętność wroga [124010] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124010].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Umiejętność wroga [124010] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124010].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Umiejętność wroga [124011] (ulepszenie 1) — nazwa] 꿰어져라
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124011].levelList[level=1].name
   limit: do 40 znaków
   EN: Be Impaled
   PL:
170. [Umiejętność wroga [124011] (ulepszenie 1) — opis] [DefeatDuel] 정신력 3 감소\n[DefeatDuel] 최종 피해량 -50%
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124011].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Lose 3 SP\n[DefeatDuel] Deal -50% final damage
   PL:
171. [Umiejętność wroga [124011] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124011].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Umiejętność wroga [124011] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 흐트러짐 상태가 되고, 다음 턴에 [Penetration] 상태가 됨
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124011].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Penetration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Penetration] = 굳어가는 피 / Congealing Blood
   EN: [OnSucceedAttack] The target becomes staggered, then becomes [Penetration] next turn
   PL:
173. [Umiejętność wroga [124011] (ulepszenie 1) — moneta 2, efekt 3 — opis] [EndCoin] 대상의 [Laceration] 위력 25 감소. 해당 수치만큼 [Laceration]을 얻고, [BloodDinner] 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124011].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [Laceration], [BloodDinner]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: [EndCoin] The target loses 25 [Laceration] Potency. Gain [Laceration] and increase [BloodDinner] equal to that value
   PL:
174. [Umiejętność wroga [124012] (ulepszenie 1) — nazwa] 돈키호테류 경혈 오의 - 구
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124012].levelList[level=1].name
   limit: do 70 znaków
   EN: Ascendant Don Quixote Hardblood Arts - The Sphere
   PL:
175. [Umiejętność wroga [124012] (ulepszenie 1) — opis] 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음.\n[BloodDinner_Common_Accumulation]만큼 피해량이 증가함.(최대 300%)\n[WhenUse] 정신력 30 회복\n[WhenUse] [RegainedStrength] 10당 합 위력 +1\n[EndSkill] [RegainedStrength] 모두 소모. 이번 턴과 다음 턴에 [Vulnerable] 5 얻음. 다음 턴에 [Binding] 2 얻음.\n[DefeatDuel] 최종 피해량 -80%
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124012].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner_Common_Accumulation], [WhenUse], [RegainedStrength], [EndSkill], [Vulnerable], [Binding], [DefeatDuel]
   znaczenie tagów: [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [WhenUse] = [사용시] / [On Use]; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [EndSkill] = [공격 종료시] / [Attack End]; [Vulnerable] = 취약 / Fragile; [Binding] = 속박 / Bind; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Cannot be Staggered until he uses this Skill.\nDeal more damage equal to [BloodDinner_Common_Accumulation]. (max 300%)\n[WhenUse] Heal 30 SP\n[WhenUse] Clash Power +1 for every 10 [RegainedStrength]\n[EndSkill] Consume all [RegainedStrength]. Gain 5 [Vulnerable] this turn and next turn. Gain 2 [Binding] next turn.\n[DefeatDuel] Deal -80% final damage
   PL:
176. [Umiejętność wroga [124012] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124012].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Umiejętność wroga [124012] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124012].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Umiejętność wroga [117501] (ulepszenie 1) — nazwa] 집요한 상처내기
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117501].levelList[level=1].name
   limit: do 40 znaków
   EN: Tenacious Wound
   PL:
179. [Umiejętność wroga [117501] (ulepszenie 1) — opis] 대상의 [Laceration] 위력이 6 이상이면, 코인 위력 +1, 이 스킬에서 부여하는 [Laceration] 위력과 횟수의 값 +1
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117501].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration] Potency, gain Coin Power +1 and gain +1 to [Laceration] Potency and Count inflicted by this Skill
   PL:
180. [Umiejętność wroga [117501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Umiejętność wroga [117501] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117501].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Umiejętność wroga [117501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Umiejętność wroga [117501] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117501].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Umiejętność wroga [117502] (ulepszenie 1) — nazwa] 상처내기
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117502].levelList[level=1].name
   limit: do 40 znaków
   EN: Wound
   PL:
185. [Umiejętność wroga [117502] (ulepszenie 1) — opis] 대상의 [Laceration] 위력이 6 이상이면, 코인 위력 +1, 이 스킬에서 부여하는 [Laceration] 위력과 횟수의 값 +1
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117502].levelList[level=1].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Umiejętność wroga [117502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność wroga [117502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Umiejętność wroga [117503] (ulepszenie 1) — nazwa] 죄어오는 가시덩굴
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117503].levelList[level=1].name
   limit: do 40 znaków
   EN: Brambles that Constrict
   PL:
189. [Umiejętność wroga [117503] (ulepszenie 1) — opis] 대상의 [Laceration] 위력이 6 이상이면, 이 스킬에서 부여하는 [Laceration] 위력의 값 +1\n대상의 ([Laceration] 위력 + [Laceration] 횟수)가 15이상이면, 공격 가중치 +2
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117503].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration] Potency, this Skill inflicts +1 more [Laceration] Potency\nIf target has 15+ ([Laceration] + [Laceration] Count), gain +2 Atk Weight
   PL:
190. [Umiejętność wroga [117503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Umiejętność wroga [117503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [117503] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117503].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration] and +2 [Laceration] Count
   PL:
193. [Umiejętność wroga [117511] (ulepszenie 1) — nazwa] 목마른 꽃잎
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117511].levelList[level=1].name
   limit: do 40 znaków
   EN: Polydipsic Petals
   PL:
194. [Umiejętność wroga [117511] (ulepszenie 1) — opis] [Laceration] 위력과 횟수의 합이 가장 높은 대상에게 시전\n[WhenUse] 대상의 [Laceration] 위력이 6 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117511].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: Attacks the target with the highest sum of [Laceration] Potency + Count\n[WhenUse] Coin Power +1 for every 6 [Laceration] Potency on target (max 2)
   PL:
195. [Umiejętność wroga [117511] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [ScarletTakeDamageUp] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117511].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ScarletTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ScarletTakeDamageUp] = 색욕 취약 / Lust Fragility
   EN: [OnSucceedAttack] Inflict 2 [ScarletTakeDamageUp]
   PL:
196. [Umiejętność wroga [117511] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동 ([Laceration] 횟수 1 감소)
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117511].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on the target once (reduce [Laceration] Count by 1)
   PL:
197. [Umiejętność wroga [117512] (ulepszenie 1) — nazwa] 폭발하는 꽃잎
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117512].levelList[level=1].name
   limit: do 40 znaków
   EN: Bursting Petals
   PL:
198. [Umiejętność wroga [117512] (ulepszenie 1) — opis] [Laceration] 위력과 횟수의 합이 가장 높은 대상에게 시전\n[WhenUse] 대상의 [Laceration] 위력이 6 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117512].levelList[level=1].desc
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Umiejętność wroga [117512] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [ScarletTakeDamageUp] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117512].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 195 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Umiejętność wroga [117512] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 모두 발동 ([Laceration] 횟수 모두 감소)
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117512].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate all [Laceration] on the target (completely reduce [Laceration] Count)
   PL:
201. [Umiejętność wroga [117513] (ulepszenie 1) — nazwa] 가시 폭풍
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117513].levelList[level=1].name
   limit: do 40 znaków
   EN: Storm of Spikes
   PL:
202. [Umiejętność wroga [117513] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 위력이 6 이상이면, 최종 위력 +2
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117513].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 6+ [Laceration] Potency, Final Power +2
   PL:
203. [Umiejętność wroga [117513] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동 ([Laceration] 횟수 1회 감소)
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117513].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on the target once (reduce [Laceration] Count by 1)
   PL:
204. [Umiejętność wroga [117514] (ulepszenie 1) — nazwa] 목마른 가시
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117514].levelList[level=1].name
   limit: do 40 znaków
   EN: Polydipsic Thorn
   PL:
205. [Umiejętność wroga [117514] (ulepszenie 1) — opis] [StartBattle] [AttackDmgUp] 3, [Vulnerable] 2 얻음
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117514].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: [StartBattle] Gain 3 [AttackDmgUp] and 2 [Vulnerable]
   PL:
206. [Umiejętność wroga [117514] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117514].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Umiejętność wroga [117514] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117514].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Umiejętność wroga [117514] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117514].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
209. [Umiejętność wroga [117514] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117514].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Umiejętność wroga [117514] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117514].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Umiejętność wroga [117514] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117514].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 208 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Umiejętność wroga [117514] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117514].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Umiejętność wroga [117514] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117514].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Umiejętność wroga [117514] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117514].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 208 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Umiejętność wroga [117515] (ulepszenie 1) — nazwa] 멈추지 않는 피
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117515].levelList[level=1].name
   limit: do 40 znaków
   EN: Endless Spring of Blood
   PL:
216. [Umiejętność wroga [117515] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 이 스킬과 합을 하는 대상은 합을 진행하는 동안 [Laceration] 횟수가 감소하지 않음
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117515].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Laceration]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [DuelCounter]\n[WhenUse] Targets that clash against this Skill do not lose [Laceration] Count while clashing
   PL:
217. [Umiejętność wroga [117515] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117515].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Umiejętność wroga [117515] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]을 1회 발동시키고, 해당 [Laceration] 피해로 생성된 [BloodDinner]을 즉시 소모함
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117515].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [BloodDinner]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: [OnSucceedAttack] Activate [Laceration] on the target once, and immediately consume [BloodDinner] generated by the [Laceration] damage
   PL:
219. [Umiejętność wroga [117515] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117515].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność wroga [117515] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]을 1회 발동시키고, 해당 [Laceration] 피해로 생성된 [BloodDinner]을 즉시 소모함
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117515].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność wroga [117515] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117515].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Umiejętność wroga [117515] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]을 1회 발동시키고, 해당 [Laceration] 피해로 생성된 [BloodDinner]을 즉시 소모함
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117515].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Umiejętność wroga [117516] (ulepszenie 1) — nazwa] 양분 탐닉
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117516].levelList[level=1].name
   limit: do 40 znaków
   EN: Nutrient Craving
   PL:
224. [Umiejętność wroga [117516] (ulepszenie 1) — opis] [BloodDinner]이 100 이상이면 사용\n[EndBattle] [BloodDinner]을 최대 100 소모하여 아래 효과 적용\n- 소모한 [BloodDinner]만큼 본체와 몸통 부위 체력 회복\n- 소모한 [BloodDinner] 20 당 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117516].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [EndBattle], [AttackUp]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [EndBattle] = [턴 종료 시] / [Turn End]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Activates at 100+ [BloodDinner]\n[EndBattle] Consume up to 100 [BloodDinner] to activate the following effects:\n- Heal the Core and the Body Parts' HP by [BloodDinner] consumed\n- Gain 1 [AttackUp] next turn for every 20 [BloodDinner] consumed
   PL:
225. [Umiejętność wroga [117517] (ulepszenie 1) — nazwa] 갈망하는 가시덩굴
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117517].levelList[level=1].name
   limit: do 40 znaków
   EN: Brambles that Yearn
   PL:
226. [Umiejętność wroga [117517] (ulepszenie 1) — opis] [WhenUse] [BloodDinner]을 최대 100 소모하여 아래 효과 적용\n- 소모한 [BloodDinner]만큼 본체와 몸통 부위 체력 회복\n- 소모한 [BloodDinner] 20 당 이 스킬의 최종 위력 +1\n[EndSkill] 이 스킬로 소모한 [BloodDinner]이 30 미만이면, 다음 턴에 [Vulnerable] 2 얻음
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=117517].levelList[level=1].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [EndSkill], [Vulnerable]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [EndSkill] = [공격 종료시] / [Attack End]; [Vulnerable] = 취약 / Fragile
   EN: [WhenUse] Consume up to 100 [BloodDinner] to activate the following effects:\n- Heal the Core and the Body Parts' HP by [BloodDinner] consumed\n- This Skill gains Final Power +1 for every 20 [BloodDinner] consumed\n[EndSkill] If this Skill consumed less than 30 [BloodDinner], gain 2 [Vulnerable] next turn
   PL:
227. [Umiejętność wroga [118308] (ulepszenie 1) — nazwa] 답하라, 가보옥
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118308].levelList[level=1].name
   limit: do 40 znaków
   EN: Answer Me, Jia Baoyu
   PL:
228. [Umiejętność wroga [118308] (ulepszenie 1) — opis] [CantChangeTarget]\n편성 순서가 가장 빠른 대상 우선 공격\n[WinDuel] [Burst] 횟수 4 증가\n[DefeatDuel] 대상의 편성 순서가 가장 빠르면, [Teaching] 1 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118308].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [WinDuel], [Burst], [DefeatDuel], [Teaching]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture; [DefeatDuel] = [합 패배] / [Clash Lose]; [Teaching] = 문답 / Dialogues
   EN: [CantChangeTarget]\nPrioritizes the target with the earliest Deployment order\n[WinDuel] Inflict +4 [Burst] Count\n[DefeatDuel] If the target has the earliest Deployment order, inflict 1 [Teaching]
   PL:
229. [Umiejętność wroga [118308] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118308].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Umiejętność wroga [118308] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118308].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Burst]
   PL:
231. [Umiejętność wroga [118308] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118308].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Umiejętność wroga [118308] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118308].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Umiejętność wroga [118308] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118308].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Umiejętność wroga [118308] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118308].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność wroga [118308] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118308].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [Umiejętność wroga [118308] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118308].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Umiejętność wroga [118309] (ulepszenie 1) — nazwa] 천강성 - 격(格)
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118309].levelList[level=1].name
   limit: do 40 znaków
   EN: Tiangang Star - Form (格)
   PL:
238. [Umiejętność wroga [118309] (ulepszenie 1) — opis] 편성 순서가 가장 빠른 대상 우선 공격\n대상의 [Teaching]당, 코인 위력 -2\n[DefeatDuel] 이 공격으로 흐트러짐 상태가 되지 않음. 이번 전투동안 [DefenseDown] 24 얻음\n[DefeatDuel] 피해량이 50%만큼 감소함
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118309].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Teaching], [DefeatDuel], [DefenseDown]
   znaczenie tagów: [Teaching] = 문답 / Dialogues; [DefeatDuel] = [합 패배] / [Clash Lose]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Prioritizes the target with the earliest Deployment order\nCoin Power -2 for every [Teaching] on target\n[DefeatDuel] Cannot Stagger with this attack. Gain 24 [DefenseDown] for this Encounter\n[DefeatDuel] Deal -50% damage
   PL:
239. [Umiejętność wroga [118309] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118309].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Umiejętność wroga [118309] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118309].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
241. [Umiejętność wroga [118309] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118309].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [Umiejętność wroga [118309] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118309].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Umiejętność wroga [118309] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118309].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [Umiejętność wroga [118309] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118309].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Umiejętność wroga [118309] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118309].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Umiejętność wroga [118309] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 ([Burst] 위력 + [Burst] 횟수 + 보유한 주살 종류)당 피해량 +5% (최대 100%)
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118309].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Deal +5% damage for every ([Burst] Potency on target + [Burst] Count on target + number of Deathrite types on target) (max 100%)
   PL:
247. [Umiejętność wroga [118701] (ulepszenie 1) — nazwa] 보옥요람[寶玉搖籃]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118701].levelList[level=1].name
   limit: do 50 znaków
   EN: Precious Jade's Cradle [寶玉搖籃]
   PL:
248. [Umiejętność wroga [118701] (ulepszenie 1) — opis] [CantChangeTarget]\n편성 순서가 가장 빠른 대상 우선 공격\n대상이 편성 순서가 빠른 대상이면 피해량이 0으로 고정됨\n[EndSkill] 대상이 편성 순서가 빠른 대상이면, 흐트러짐 상태로 만들고 다음 턴에 [ExpensiveJade]으로 만듦. 이후 턴 종료
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118701].levelList[level=1].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [EndSkill], [ExpensiveJade]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [EndSkill] = [공격 종료시] / [Attack End]; [ExpensiveJade] = 보옥요람 / Precious Jade's Cradle
   EN: [CantChangeTarget]\nPrioritizes the target with the earliest Deployment order\nWhen this Skill targets the target with the earliest Deployment order, deal 0 damage\n[EndSkill] When this Skill targets the unit with the earliest Deployment order, Stagger them, then turn them into [ExpensiveJade] next turn; then, end the turn
   PL:
249. [Umiejętność wroga [118701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Umiejętność wroga [118310] (ulepszenie 1) — nazwa] 휩쓸고 몰아쳐라
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118310].levelList[level=1].name
   limit: do 40 znaków
   EN: Like a Roaring Storm
   PL:
251. [Umiejętność wroga [118310] (ulepszenie 1) — opis] [CantDuel]\n[CantChangeTarget]\n이 스킬은 편성 순서가 가장 빠른 대상 인격을 제외한 인원을 공격함\n다음 턴에 편성 순서가 가장 빠른 대상 인격을 제외한 다른 인격들을 흑수 - 묘를 이용해 흐트러짐 상태로 만듦, 자신의 흐트러짐 상태를 해제함\n[EndSkill] 턴이 종료함
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118310].levelList[level=1].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantDuel]\n[CantChangeTarget]\nThis Skill attacks targets that are not the earliest in the Deployment order\nUses the Heishou Pack - Mao Branch to Stagger every Identity except for the Identity with the earliest Deployment order next turn; this unit recovers from Stagger\n[EndSkill] Ends turn
   PL:
252. [Umiejętność wroga [118310] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118310].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL:
253. [Umiejętność wroga [118703] (ulepszenie 1) — nazwa] 너희는 그 눈의 힘과 특별함을 아직도 한참을 모르고 있구나
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118703].levelList[level=1].name
   limit: do 90 znaków
   EN: You do not know the fathoms of the eye's powers, its special nature
   PL:
254. [Umiejętność wroga [118703] (ulepszenie 1) — opis] 편성 순서가 가장 빠른 대상 우선 공격\n[WhenUse] 보옥이 있으면, 이 스킬의 모든 코인이 [SuperCoin]이 됨\n[WhenUse] 대상의 [Laceration]과 [Burst]의 합 5당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118703].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [SuperCoin], [Laceration], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: Prioritizes the target with the earliest Deployment Order\n[WhenUse] When there is Baoyu, the Precious Jade, convert all Coins on this Skill to [SuperCoin]s\n[WhenUse] Coin Power +1 for every 5 ([Laceration] + [Burst]) on target (max 2)
   PL:
255. [Umiejętność wroga [118703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3, [Burst] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count and +3 [Burst] Count
   PL:
256. [Umiejętność wroga [118703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1, [Burst] 1 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Laceration] and 1 [Burst]
   PL:
257. [Umiejętność wroga [118703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1, [Burst] 1 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Umiejętność wroga [118704] (ulepszenie 1) — nazwa] 선인님들 지켜봐주세요...!
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118704].levelList[level=1].name
   limit: do 50 znaków
   EN: Please Watch me, O Xianren...!
   PL:
259. [Umiejętność wroga [118704] (ulepszenie 1) — opis] 편성 순서가 가장 빠른 대상 우선 공격\n[WinDuel] [Breath] 5 얻음, [Breath] 횟수 2 증가\n[DefeatDuel] 다음 턴에 [AttackUp] 2, [DefenseDown] 2 얻음
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118704].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Breath], [DefeatDuel], [AttackUp], [DefenseDown]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Prioritizes the target with the earliest Deployment Order\n[WinDuel] Gain 5 [Breath] and +2 [Breath] Count\n[DefeatDuel] Gain 2 [AttackUp] and 2 [DefenseDown] next turn
   PL:
260. [Umiejętność wroga [118704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2, [Vulnerable] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Binding] and 2 [Vulnerable] next turn
   PL:
261. [Umiejętność wroga [118704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count and +2 [Burst] Count
   PL:
262. [Umiejętność wroga [118707] (ulepszenie 1) — nazwa] 너는 여전히 아무것도 할 수 없단다
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118707].levelList[level=1].name
   limit: do 40 znaków
   EN: Still, you can do nothing
   PL:
263. [Umiejętność wroga [118707] (ulepszenie 1) — opis] [WhenUse] 정신력 8 회복\n[WhenUse] 메인 타겟의 체력이 50% 미만이거나, 메인 타겟의 [Burst]과 [Laceration]의 합이 10 이상이면 [SuperCoin]이 됨\n[DefeatDuel] [Vulnerable] 1 얻음\n- 홍루에게 합 패배 시 대신 2 얻음
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118707].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Laceration], [SuperCoin], [DefeatDuel], [Vulnerable]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile
   EN: [WhenUse] Heal 8 SP\n[WhenUse] If the main target has less than 50% HP, or if the main target has 10+ ([Burst] + [Laceration]), convert this Skill's Coins to [SuperCoin]s\n[DefeatDuel] Gain 1 [Vulnerable]\n- When losing a clash against Hong Lu, gain 2 [Vulnerable] instead
   PL:
264. [Umiejętność wroga [118707] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4, [Burst] 4 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118707].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and 4 [Burst]
   PL:
265. [Umiejętność wroga [118707] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118707].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 252 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Umiejętność wroga [118707] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 정신력 피해 10, 피해량의 50%만큼 흐트러짐 손상
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118707].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 10 SP damage and raise target's Stagger Threshold by 50% of damage dealt
   PL:
267. [Umiejętność wroga [118707] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118707].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL:
268. [Umiejętność wroga [118707] (ulepszenie 1) — moneta 1, efekt 5 — opis] [OnSucceedAttack] 정신력 8 회복
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=118707].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 8 SP
   PL:
269. [Umiejętność wroga [124105] (ulepszenie 1) — nazwa] 폭쇄참 [爆碎斬]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].name
   limit: do 40 znaków
   EN: Blasting Shatterslash [爆碎斬]
   PL:
270. [Umiejętność wroga [124105] (ulepszenie 1) — opis] [Prey]을 보유한 대상을 우선으로 지정\n속도에 상관없이 이 스킬과 합을 할 수 있음\n대상의 [Combustion]과 [Vibration]의 합 6당 코인 위력 +1 (최대 3)\n[DefeatDuel] 최종 피해량 -50%
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Prey], [Combustion], [Vibration], [DefeatDuel]
   znaczenie tagów: [Prey] = 사냥감 / Prey; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets with [Prey]\nCan clash with this Skill regardless of Speed\nCoin Power +1 for every 6 ([Combustion] + [Vibration]) on target (max 3)\n[DefeatDuel] Deal -50% final damage
   PL:
271. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 1, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellant]
   znaczenie tagów: [BulletPropellant] = 호표탄 / Tigermark Round
   EN: Spend 1 [BulletPropellant]
   PL:
273. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]
   PL:
274. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL:
275. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 1, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 4 부여, [Vibration] 횟수 4 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 4 [Vibration] and +4 [Vibration] Count
   PL:
276. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 2, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +3 [Combustion] Count
   PL:
279. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL:
280. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 2, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]
   PL:
281. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 3, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 3, efekt 3 — opis] 이 코인 효과로 [BulletPropellant]을 소모하였다면, 피해량 +50%
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellant]
   znaczenie tagów: [BulletPropellant] = 호표탄 / Tigermark Round
   EN: If this unit spent [BulletPropellant] due to this Coin's effect, deal +50% damage
   PL:
284. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [Combustion] 3 부여, [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion] and +3 [Combustion] Count
   PL:
285. [Umiejętność wroga [124105] (ulepszenie 1) — moneta 3, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124105].levelList[level=1].coinlist[#2].coindescs[#4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] twice; then, reduce target's [Vibration] Count by 2
   PL:
286. [Umiejętność wroga [124106] (ulepszenie 1) — nazwa] 쾌도난마 [快刀亂麻]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124106].levelList[level=1].name
   limit: do 40 znaków
   EN: Tanglecleaver [快刀亂麻]
   PL:
287. [Umiejętność wroga [124106] (ulepszenie 1) — opis] [Prey]을 보유한 대상을 우선으로 지정\n속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[WhenUse] [BattleSense]을 전부 소모. 소모한 수치가\n- 10 이상이면, 10당 공격 가중치 +1 (최대 2)\n- 25일 경우, 메인 타겟의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 5)\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않으며, [Combustion] 위력과 횟수, [Vibration] 위력과 횟수 부여량이 절반으로 감소 (다른 효과로 증가되는 수치 제외)\n[EndSkill] [FullReload] (턴당 1회)\n- [BulletPropellantSpecial]을 보유하였다면, 대신 [ReloadKeepAmmo] (턴당 1회)\n[DefeatDuel] 최종 피해량 -50%\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124106].levelList[level=1].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: \n, [Prey], [WhenUse], [BattleSense], [Combustion], [Vibration], [DefeatDuel], [EndSkill], [FullReload], [BulletPropellantSpecial], [ReloadKeepAmmo]
   znaczenie tagów: [Prey] = 사냥감 / Prey; [WhenUse] = [사용시] / [On Use]; [BattleSense] = 저력 [底力] / Inner Strength [底力]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [FullReload] = 재장전 / Reload …
   EN: Prioritizes targets with [Prey]\nCan Clash with this Skill regardless of Speed; this unit does not become Staggered before it uses this Skill\n[WhenUse] Consume all [BattleSense] Stack on self. If this unit consumed...\n- ... 10+ Stack , gain Atk Weight +1 for every 10 Stack consumed (max 2)\n- ... 25 Stack, Final Power +1 for every 4 (sum of [Combustion] and [Vibration] on the main target) (max 5)\n[DefeatDuel] Deal -80% damage; this Skill's damage cannot Stagger the target; inflict only half the Potency and Count for both [Combustion] and [Vibration] inflicted by this Skill (unless raised by other effects)\n[EndSkill] [FullReload] (once per turn)\n- If this unit has [BulletPropellantSpecial], [ReloadKeepAmmo] instead (once per turn)\n[DefeatDuel] Deal -50% final damage\n[EndSkill] Ends this turn
   PL:
288. [Umiejętność wroga [124106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Umiejętność wroga [124106] (ulepszenie 1) — moneta 1, efekt 2 — opis] [BulletPropellant] 전부 소모
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124106].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellant]
   znaczenie tagów: [BulletPropellant] = 호표탄 / Tigermark Round
   EN: Spend all [BulletPropellant]
   PL:
290. [Umiejętność wroga [124106] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 소모한 [BulletPropellant]만큼 [Combustion] 부여, [Combustion] 횟수 증가, [Vibration] 부여, [Vibration] 횟수 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124106].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BulletPropellant], [Combustion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BulletPropellant] = 호표탄 / Tigermark Round; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict [Combustion], [Combustion] Count, [Vibration], and [Vibration] Count by [BulletPropellant] spent
   PL:
291. [Umiejętność wroga [124106] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124106].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Umiejętność wroga [124106] (ulepszenie 1) — moneta 1, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 3회. 대상의 [Vibration] 횟수 3 감소
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124106].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] 3 times; then, reduce target's [Vibration] Count by 3
   PL:
293. [Umiejętność wroga [124107] (ulepszenie 1) — nazwa] 초절맹호살격난참 [超絕猛虎殺擊亂斬]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].name
   limit: do 80 znaków
   EN: Savage Tigerslayer's Perfected Flurry of Blades [超絕猛虎殺擊亂斬]
   PL:
294. [Umiejętność wroga [124107] (ulepszenie 1) — opis] [Prey]을 보유한 대상을 우선으로 지정\n속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[WhenUse] [BattleSense]을 전부 소모. 소모한 수치가\n- 10 이상이면, 10당 공격 가중치 +1 (최대 4)\n- 25 이상이면, 메인 타겟의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 6)\n- 50일 경우, 코인 위력 +1, 피해량 +50%\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않으며, [Combustion] 위력과 횟수, [Vibration] 위력과 횟수 부여량이 절반으로 감소 (다른 효과로 증가되는 수치 제외)\n[EndSkill] [FullReload] (턴당 1회)\n- [BulletPropellantSpecial]을 보유하였다면, 대신 [ReloadKeepAmmo] (턴당 1회)\n[DefeatDuel] 최종 피해량 -50%\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].desc
   limit: do 1070 znaków
   tokeny: zachowaj dokładnie: \n, [Prey], [WhenUse], [BattleSense], [Combustion], [Vibration], [DefeatDuel], [EndSkill], [FullReload], [BulletPropellantSpecial], [ReloadKeepAmmo]
   znaczenie tagów: [Prey] = 사냥감 / Prey; [WhenUse] = [사용시] / [On Use]; [BattleSense] = 저력 [底力] / Inner Strength [底力]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [FullReload] = 재장전 / Reload …
   EN: Prioritizes targets with [Prey]\nCan Clash with this Skill regardless of Speed; this unit does not become Staggered before it uses this Skill\n[WhenUse] Consume all [BattleSense] Stack on self. If this unit consumed...\n- ... 10+ Stack , gain Atk Weight +1 for every 10 Stack consumed (max 4)\n- ... 25 Stack, Final Power +1 for every 4 (sum of [Combustion] and [Vibration] on the main target) (max 6)\n- ... 50 Stack, Coin Power +1 and deal +50% damage\n[DefeatDuel] Deal -80% damage; this Skill's damage cannot Stagger the target; inflict only half the Potency and Count for both [Combustion] and [Vibration] inflicted by this Skill (unless raised by other effects)\n[EndSkill] [FullReload] (once per turn)\n- If this unit has [BulletPropellantSpecial], [ReloadKeepAmmo] instead (once per turn)\n[DefeatDuel] Deal -50% final damage\n[EndSkill] Ends this turn
   PL:
295. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 1, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 6 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 6 [Combustion]
   PL:
298. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 2, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 6 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +6 [Combustion] Count
   PL:
301. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 3, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Vibration] 6 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 6 [Vibration]
   PL:
304. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 4, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 6 증가
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +6 [Vibration] Count
   PL:
307. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 5, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 5, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#4].coindescs[#2].desc
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 6, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#5].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 6, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#5].coindescs[#1].desc
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [Umiejętność wroga [124107] (ulepszenie 1) — moneta 6, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 5회. 대상의 [Vibration] 횟수 5 감소
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124107].levelList[level=1].coinlist[#5].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] 5 times; then, reduce target's [Vibration] Count by 5
   PL:
313. [Umiejętność wroga [124108] (ulepszenie 1) — nazwa] 천퇴성도 장전
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124108].levelList[level=1].name
   limit: do 50 znaków
   EN: Reloading Tiantui Star's Blade
   PL:
314. [Umiejętność wroga [124108] (ulepszenie 1) — opis] [WhenUse] 정신력 10 회복\n- 정신력이 0 미만이면, 정신력 5 추가로 회복\n[DuelCounter]\n[DefeatDuel] [BulletPropellant] 1 감소\n[EndSkill] [FullReload] (턴당 1회)\n- [BulletPropellantSpecial]을 보유하였다면, 대신 [ReloadKeepAmmo] (턴당 1회)
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124108].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DuelCounter], [DefeatDuel], [BulletPropellant], [EndSkill], [FullReload], [BulletPropellantSpecial], [ReloadKeepAmmo]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BulletPropellant] = 호표탄 / Tigermark Round; [EndSkill] = [공격 종료시] / [Attack End]; [FullReload] = 재장전 / Reload; [BulletPropellantSpecial] = 맹호표탄 / Savage Tigermark Round; [ReloadKeepAmmo] = 재장전 - 잔탄 유지 / Reload - Tactical
   EN: [WhenUse] Heal 10 SP\n- At less than 0 SP, heal 5 additional SP\n[DuelCounter]\n[DefeatDuel] Lose 1 [BulletPropellant]\n[EndSkill] [FullReload] (once per turn)\n- If this unit has [BulletPropellantSpecial], [ReloadKeepAmmo] instead (once per turn)
   PL:
315. [Umiejętność wroga [124301] (ulepszenie 1) — nazwa] 사탕 줘.
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124301].levelList[level=1].name
   limit: do 40 znaków
   EN: Gimme Candy.
   PL:
316. [Umiejętność wroga [124301] (ulepszenie 1) — opis] [GiveMeCandy]을 가진 대상 우선 공격\n[WhenUse] 대상의 [GiveMeCandy] 1당 코인 위력 +1 (최대 5)\n[DefeatDuel] 최종 피해량 -50%
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124301].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [GiveMeCandy], [WhenUse], [DefeatDuel]
   znaczenie tagów: [GiveMeCandy] = 사탕 / Candy; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets with [GiveMeCandy]\n[WhenUse] Coin Power +1 for every [GiveMeCandy] on target (max 5)\n[DefeatDuel] Deal -50% final damage
   PL:
317. [Umiejętność wroga [124301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Umiejętność wroga [124301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [WinDuelAttack] 대상에게 [GiveMeCandy]이 있으면, 대상은 다음 턴 흐트러짐 상태가 됨.
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack], [GiveMeCandy]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]; [GiveMeCandy] = 사탕 / Candy
   EN: [WinDuelAttack] If target has [GiveMeCandy], the target becomes Staggered next turn.
   PL:
319. [Umiejętność wroga [124301] (ulepszenie 1) — moneta 1, efekt 3 — opis] [DefeatDuel] 대상의 [GiveMeCandy] 만큼 포만감 얻음.
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124301].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel], [GiveMeCandy]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [GiveMeCandy] = 사탕 / Candy
   EN: [DefeatDuel] Gain Indulged equal to [GiveMeCandy] on target.
   PL:
320. [Umiejętność wroga [124301] (ulepszenie 1) — moneta 1, efekt 4 — opis] [EndSkill] 합을 진행한 대상의 [GiveMeCandy] 모두 제거
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124301].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [GiveMeCandy]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [GiveMeCandy] = 사탕 / Candy
   EN: [EndSkill] Completely remove [GiveMeCandy] from the target this unit clashed against
   PL:
321. [Umiejętność wroga [124302] (ulepszenie 1) — nazwa] 없어. 사탕.
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124302].levelList[level=1].name
   limit: do 40 znaków
   EN: No Candy.
   PL:
322. [Umiejętność wroga [124302] (ulepszenie 1) — opis] [BeforeAttack] [GiveMeCandy]을 가진 인격 수만큼 공격 가중치 증가 (최대 3)\n[WhenUse] [GiveMeCandy]을 가진 인격 수만큼 피해량 +10% (최대 50%)\n[WhenUse] 메인 타겟이 보유한 [GiveMeCandy] 1당 코인 위력 +1 (최대 5)
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124302].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [GiveMeCandy], [WhenUse]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [GiveMeCandy] = 사탕 / Candy; [WhenUse] = [사용시] / [On Use]
   EN: [BeforeAttack] Gain +(# of Identities with [GiveMeCandy]) Atk Weight (max 3)\n[WhenUse] Deal +10% damage for every Identity with [GiveMeCandy] (max 50%)\n[WhenUse] Coin Power +1 for every [GiveMeCandy] on the main target (max 5)
   PL:
323. [Umiejętność wroga [124303] (ulepszenie 1) — nazwa] 너희들…
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124303].levelList[level=1].name
   limit: do 40 znaków
   EN: All of you...
   PL:
324. [Umiejętność wroga [124303] (ulepszenie 1) — opis] [WhenUse] 대상의 [GiveMeCandy] 1당 코인 위력 +1 (최대 5)\n[DefeatDuel] 최종 피해량 -50%
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124303].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [GiveMeCandy], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [GiveMeCandy] = 사탕 / Candy; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Coin Power +1 for every [GiveMeCandy] on target (max 5)\n[DefeatDuel] Deal -50% final damage
   PL:
325. [Umiejętność wroga [124303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [Umiejętność wroga [124303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Umiejętność wroga [124304] (ulepszenie 1) — nazwa] 부릉부릉
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124304].levelList[level=1].name
   limit: do 40 znaków
   EN: Vroom-Vroom
   PL:
328. [Umiejętność wroga [124304] (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] [GiveMeCandy]을 가진 인격 수만큼 피해량 +20% (최대 100%)
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [GiveMeCandy]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [GiveMeCandy] = 사탕 / Candy
   EN: [CantDuel]\n[WhenUse] Deal +20% damage for every Identity with [GiveMeCandy] (max 100%)
   PL:
329. [Umiejętność wroga [124305] (ulepszenie 1) — nazwa] 나눠. 먹어.
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124305].levelList[level=1].name
   limit: do 40 znaków
   EN: Eat. Together.
   PL:
330. [Umiejętność wroga [124305] (ulepszenie 1) — opis] [WhenUse] 무작위 적 2명([GiveMeCandy]이 없는 적 우선 순위)에게 [GiveMeCandy]을 1부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124305].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [GiveMeCandy]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [GiveMeCandy] = 사탕 / Candy
   EN: [WhenUse] Apply 1 [GiveMeCandy] to 2 random enemies(prioritizes enemies without [GiveMeCandy])
   PL:
331. [Umiejętność wroga [124306] (ulepszenie 1) — nazwa] …꼬미가, 화났어.
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124306].levelList[level=1].name
   limit: do 40 znaków
   EN: ... Kkomi's angry.
   PL:
332. [Umiejętność wroga [124306] (ulepszenie 1) — opis] [BeforeAttack] [GiveMeCandy]을 가진 인격 수만큼 공격 가중치 증가\n[WhenUse] [GiveMeCandy]을 가진 인격 수만큼 피해량 +10% (최대 50%)\n[WhenUse] [GiveMeCandy]을 가진 인격 수만큼 합 위력 증가 (최대 5)\n[DefeatDuel] 최종 피해량 -80%
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124306].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [GiveMeCandy], [WhenUse], [DefeatDuel]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [GiveMeCandy] = 사탕 / Candy; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [BeforeAttack] Gain +(# of Identities with [GiveMeCandy]) Atk Weight\n[WhenUse] Deal +10% damage for every Identity with [GiveMeCandy] (max 50%)\n[WhenUse] Gain Clash Power equal to the number of Identities with [GiveMeCandy] (max 5)\n[DefeatDuel] Deal -80% final damage
   PL:
333. [Umiejętność wroga [124306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Umiejętność wroga [124306] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124306].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Umiejętność wroga [124307] (ulepszenie 1) — nazwa] 때렸어. 꼬미를
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124307].levelList[level=1].name
   limit: do 40 znaków
   EN: You hit Kkomi.
   PL:
336. [Umiejętność wroga [124307] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 다음 턴에 모든 부위 합 위력 증가 2 얻음\n[WhenUse] 다음 턴에 모든 부위 신속 2 얻음
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124307].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]
   EN: [DuelCounter]\n[WhenUse] All Parts gain 2 Clash Power Up next turn\n[WhenUse] All Parts gain 2 Haste next turn
   PL:
337. [Umiejętność wroga [124201] (ulepszenie 1) — nazwa] 주먹질
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124201].levelList[level=1].name
   limit: do 40 znaków
   EN: Punching
   PL:
338. [Umiejętność wroga [124201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 타격 추가 피해 3
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 3 Blunt bonus damage
   PL:
339. [Umiejętność wroga [124201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 타격 추가 피해 3
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Umiejętność wroga [124201] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124201].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze
   PL:
341. [Umiejętność wroga [124202] (ulepszenie 1) — nazwa] 발길질
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124202].levelList[level=1].name
   limit: do 40 znaków
   EN: Kicking
   PL:
342. [Umiejętność wroga [124202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 타격 추가 피해 5
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 Blunt bonus damage
   PL:
343. [Umiejętność wroga [124202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 타격 추가 피해 5
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Umiejętność wroga [124202] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 마비 3 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze next turn
   PL:
345. [Umiejętność wroga [124203] (ulepszenie 1) — nazwa] 되갚기
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124203].levelList[level=1].name
   limit: do 40 znaków
   EN: Payback
   PL:
346. [Umiejętność wroga [124203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력 5 감소
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 5 SP
   PL:
347. [Umiejętność wroga [124204] (ulepszenie 1) — nazwa] 뒤통수 조심!
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124204].levelList[level=1].name
   limit: do 40 znaków
   EN: Watch Your Back!
   PL:
348. [Umiejętność wroga [124204] (ulepszenie 1) — opis] 대상의 정신력이 0 미만인 경우, 코인 위력 +3
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124204].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target has less than 0 SP, Coin Power +3
   PL:
349. [Umiejętność wroga [124204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 정신력 10 회복
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 10 SP on self
   PL:
350. [Umiejętność wroga [124204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 2, 공격 위력 감소 2 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind and 2 Attack Power Down next turn
   PL:
351. [Umiejętność wroga [124204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 정신력 20 감소
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 20 SP
   PL:
352. [Umiejętność wroga [124205] (ulepszenie 1) — nazwa] 다들 집합
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124205].levelList[level=1].name
   limit: do 40 znaków
   EN: Assemble
   PL:
353. [Umiejętność wroga [124205] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 아군 2명 소환
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124205].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Summon 2 allies next turn
   PL:
354. [Umiejętność wroga [124206] (ulepszenie 1) — nazwa] 시험은 끝났다
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124206].levelList[level=1].name
   limit: do 40 znaków
   EN: No More Tests
   PL:
355. [Umiejętność wroga [124206] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [HitDamageUp] 3 얻음\n[WhenUse] 메인 타겟의 [MiddleFingerBook] 수치가 3 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 메인 타겟이 보유한 [MiddleFingerBook]이 5 이상인 경우, 가중치 +1\n[DefeatDuel] 최종 피해량 -80%
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124206].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [HitDamageUp], [MiddleFingerBook], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up; [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain 3 [HitDamageUp] next turn\n[WhenUse] If the main target has 3+ [MiddleFingerBook], convert all Coins on this Skill to [SuperCoin]s\n[WhenUse] If the main target has 5+ [MiddleFingerBook], gain +1 Atk Weight\n[DefeatDuel] Deal -80% final damage
   PL:
356. [Umiejętność wroga [124206] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124206].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL:
357. [Umiejętność wroga [124207] (ulepszenie 1) — nazwa] 고통 새기기
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124207].levelList[level=1].name
   limit: do 40 znaków
   EN: Promised Suffering
   PL:
358. [Umiejętność wroga [124207] (ulepszenie 1) — opis] [MiddleFingerBook] 수치가 가장 높은 대상을 우선 지정\n[WhenUse] 대상의 [MiddleFingerBook] 수치가 3 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[DefeatDuel] 최종 피해량 -50%
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124207].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [MiddleFingerBook], [WhenUse], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark; [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets with the highest [MiddleFingerBook] Stack\n[WhenUse] If target has 3+ [MiddleFingerBook], convert all Coins on this Skill to [SuperCoin]s\n[DefeatDuel] Deal -50% final damage
   PL:
359. [Umiejętność wroga [124207] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124207].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] this turn and next turn
   PL:
360. [Umiejętność wroga [124207] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124207].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 359 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Umiejętność wroga [124207] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] (대상의 [MiddleFingerBook] 수치 x 3)만큼 타격 추가 피해
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124207].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MiddleFingerBook]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark
   EN: [OnSucceedAttack] Inflict ([MiddleFingerBook] on the target x 3) Blunt bonus damage
   PL:
362. [Umiejętność wroga [124207] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 모든 [MiddleFingerBook] 제거
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124207].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MiddleFingerBook]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark
   EN: [OnSucceedAttack] Remove all [MiddleFingerBook] on the target
   PL:
363. [Umiejętność wroga [124208] (ulepszenie 1) — nazwa] 장난이 길었군
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124208].levelList[level=1].name
   limit: do 40 znaków
   EN: Enough games
   PL:
364. [Umiejętność wroga [124208] (ulepszenie 1) — opis] [StartBattle] 모든 아군의 정신력 10 회복\n[EndBattle] 패닉 상태인 아군이 있으면, 다음 턴 시작 시 패닉 상태를 해제하고, 정신력을 0으로 초기화함\n[EndBattle] 다음 턴에 자신을 포함한 모든 아군에게 [HitResultUp] 1 부여
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124208].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [EndBattle], [HitResultUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [EndBattle] = [턴 종료 시] / [Turn End]; [HitResultUp] = 타격 위력 증가 / Blunt Power Up
   EN: [StartBattle] Heal all allies' SP by 10\n[EndBattle] If there are Panicked allies, recover them from Panic at the next Turn Start and reset their SP to 0\n[EndBattle] Apply 1 [HitResultUp] to all allies, including this unit
   PL:
365. [Umiejętność wroga [124209] (ulepszenie 1) — nazwa] 전원, 처형이다!!!
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124209].levelList[level=1].name
   limit: do 50 znaków
   EN: COMPLETE AND TOTAL EXTERMINATION!!!
   PL:
366. [Umiejętność wroga [124209] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n메인 타겟의 [MiddleFingerBook] 수치가 5 이상이면, 최종 위력 +5\n[DefeatDuel] 최종 피해량 -80%\n[EndSkill] 공격 당한 모든 대상의 [MiddleFingerBook] 제거
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124209].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [MiddleFingerBook], [DefeatDuel], [EndSkill]
   znaczenie tagów: [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Can Clash with this Skill regardless of Speed\nIf the main target has 5+ [MiddleFingerBook], Final Power +5\n[DefeatDuel] Deal -80% final damage\n[EndSkill] Remove [MiddleFingerBook] from all targets that were hit
   PL:
367. [Umiejętność wroga [124209] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124209].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Umiejętność wroga [124209] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] (대상의 [MiddleFingerBook] 수치 x 10)만큼 타격 추가 피해
   źródło: Skills_Abnormality_Mirror6.json :: dataList[id=124209].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MiddleFingerBook]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark
   EN: [OnSucceedAttack] Inflict ([MiddleFingerBook] on the target x 10) Blunt bonus damage
   PL:

## [mirror7] Wróg / część: Enemies-mirror7
- plik gry: `Enemies-mirror7.json`

369. [[mirror7] Wróg / część [1355] — nazwa] ???
   źródło: Enemies-mirror7.json :: dataList[id=1355].name
   limit: do 40 znaków
   EN: ???
   PL:
370. [[mirror7] Wróg / część [1355] — opis] 본체
   źródło: Enemies-mirror7.json :: dataList[id=1355].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [[mirror7] Wróg / część [1353] — nazwa] ???
   źródło: Enemies-mirror7.json :: dataList[id=1353].name
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [[mirror7] Wróg / część [1353] — opis] 본체
   źródło: Enemies-mirror7.json :: dataList[id=1353].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [mirror7] Umiejętności wrogów / Anomalii — Skills_Abnormality_Mirror7
- grupa rozdziału/trybu: `mirror7` · plik: `Skills_Abnormality_Mirror7.json`

373. [Umiejętność wroga [136401] (ulepszenie 1) — nazwa] 꿈틀거리는 머리
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=136401].levelList[level=1].name
   limit: do 40 znaków
   EN: Wriggling Head
   PL:
374. [Umiejętność wroga [136401] (ulepszenie 1) — opis] 체력이 가장 낮은 적 우선 공격\n대상에게 [Paralysis]가 있다면 피해량 +50%\n<color=#ff6000><mark color=#ff000040><b><u>대상이 수비 스킬을 사용했으면 피해량 -200%</color></mark></b></u>\n[SelfCharge] 1당 기본 위력 +1\n[WhenUse] [SelfCharge] 1 소모\n[DefeatDuel] [SelfCharge] 1 소모\n[EndSkill] 일방 공격이었으면, [SelfCharge] 1 소모\n- 공격한 대상이 수비 스킬을 사용했으면, [SelfCharge] 1 추가 소모
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=136401].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Paralysis], [SelfCharge], [WhenUse], [DefeatDuel], [EndSkill]
   znaczenie tagów: [Paralysis] = 마비 / Paralyze; [SelfCharge] = 자가 충전 / Self-charge; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Prioritizes targets with the least HP\nIf target has [Paralysis], deal +50% damage\n<color=#ff6000><mark color=#ff000040><b><u>If target has used a Defense Skill, deal -200% damage</color></mark></b></u>\nBase Power +1 for every [SelfCharge]\n[WhenUse] Lose 1 [SelfCharge]\n[DefeatDuel] Lose 1 [SelfCharge]\n[EndSkill] If it was an Unopposed Attack, lose 1 [SelfCharge]\n- If the target attacked by this Skill used a Defense Skill, lose 1 more [SelfCharge]
   PL:
375. [Umiejętność wroga [136401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=136401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Umiejętność wroga [136401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=136401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis]
   PL:
377. [Umiejętność wroga [136402] (ulepszenie 1) — nazwa] 꿈틀거리는 꼬리
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=136402].levelList[level=1].name
   limit: do 40 znaków
   EN: Wriggling Tail
   PL:
378. [Umiejętność wroga [136402] (ulepszenie 1) — opis] 체력이 가장 낮은 적 우선 공격\n대상에게 [Paralysis]가 있다면 피해량 +50%\n<color=#ff6000><mark color=#ff000040><b><u>대상이 수비 스킬을 사용했으면 피해량 -200%</color></mark></b></u>\n[SelfCharge] 1당 기본 위력 +1\n[WhenUse] [SelfCharge] 1 소모\n[DefeatDuel] [SelfCharge] 1 소모\n[EndSkill] 일방 공격이었으면, [SelfCharge] 1 소모\n- 공격한 대상이 수비 스킬을 사용했으면, [SelfCharge] 1 추가 소모
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=136402].levelList[level=1].desc
   (powtórzenie elementu 374 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Umiejętność wroga [136402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=136402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Umiejętność wroga [136402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=136402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [Umiejętność wroga [136402] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=136402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Umiejętność wroga [135509] (ulepszenie 1) — nazwa] 대행: 말살 - 본망[本望]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=135509].levelList[level=1].name
   limit: do 80 znaków
   EN: Procuration: Annihilation - Mang of Immanent Yearning [本望]
   PL:
383. [Umiejętność wroga [135509] (ulepszenie 1) — opis] [WhenUse] <color=#ff6000><mark=#ff000040><b><u>정신력이 0 이상이면, 망 1개 생성</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>피해량 +20%, 최종 위력 +3</u></b></mark></color>\n[EndSkill] 정신력 15 감소\n[EndSkill] 망을 생성했으면, 정신력 20 소모\n[EndSkill] [PressureOfPrescript] 전부 소모, 이번 턴 종료
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=135509].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [EndSkill], [PressureOfPrescript]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]; [PressureOfPrescript] = 압박감 / Onus
   EN: [WhenUse] <color=#ff6000><mark=#ff000040><b><u>At 0+ SP, generate 1 Mang</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>Deal +20% damage, Final Power +3</u></b></mark></color>\n[EndSkill] Lose 15 SP\n[EndSkill] If this Skill generated Mang, lose 20 SP\n[EndSkill] Consume all [PressureOfPrescript] and end this turn
   PL:
384. [Umiejętność wroga [135509] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=135509].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Umiejętność wroga [135509] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=135509].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL:
386. [Umiejętność wroga [135509] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=135509].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Umiejętność wroga [135509] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=135509].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Umiejętność wroga [135509] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=135509].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność wroga [135509] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=135509].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Umiejętność wroga [135509] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=135509].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Umiejętność wroga [135509] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=135509].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Umiejętność wroga [135509] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=135509].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Umiejętność wroga [135509] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=135509].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Umiejętność wroga [138201] (ulepszenie 1) — nazwa] 짓밟기
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138201].levelList[level=1].name
   limit: do 40 znaków
   EN: Stomping
   PL:
395. [Umiejętność wroga [138201] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면 코인 위력 +1\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138201].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has 4+ [Laceration], Coin Power +1\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL:
396. [Umiejętność wroga [138201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Umiejętność wroga [138201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Umiejętność wroga [138201] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Umiejętność wroga [138201] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138201].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ReinforcedTattooSpider], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] If this unit has [ReinforcedTattooSpider], inflict 2 [Paralysis]
   PL:
400. [Umiejętność wroga [138203] (ulepszenie 1) — nazwa] 원한 스탬핑
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138203].levelList[level=1].name
   limit: do 40 znaków
   EN: Stamp of Vengeance
   PL:
401. [Umiejętność wroga [138203] (ulepszenie 1) — opis] 대상의 [Laceration] 3당 기본 위력 +1 (최대 3)\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[EndSkill] 자신의 [ResentmentSpider]을 전부 소모하고, [DaughterEducationSpider] 1 얻음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138203].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [DefeatDuel], [EndSkill], [ResentmentSpider], [DaughterEducationSpider]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [ResentmentSpider] = 중지 - 원한 / The Middle - Grudge; [DaughterEducationSpider] = 잘 봐둬라 딸! / Check This Out, Kiddo!
   EN: Base Power +1 for every 3 [Laceration] on target (max 3)\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[EndSkill] Consume all [ResentmentSpider] on self and gain 1 [DaughterEducationSpider]
   PL:
402. [Umiejętność wroga [138203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Umiejętność wroga [138203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Umiejętność wroga [138203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Umiejętność wroga [138203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Umiejętność wroga [138203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Umiejętność wroga [138203] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138203].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration]
   PL:
408. [Umiejętność wroga [138203] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138203].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Umiejętność wroga [138203] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138203].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
410. [Umiejętność wroga [138203] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138203].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Umiejętność wroga [138204] (ulepszenie 1) — nazwa] 고작 이거에 부서지지 말라고!
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138204].levelList[level=1].name
   limit: do 60 znaków
   EN: Don't Let Somethin' Like This Break Ya!
   PL:
412. [Umiejętność wroga [138204] (ulepszenie 1) — opis] [WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 파괴되지 않은 코인 적중시 추가 타격 피해 5\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138204].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ReinforcedTattooSpider], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If this unit has [ReinforcedTattooSpider], deal 5 Blunt bonus damage On Hit with Unbroken Coin\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL:
413. [Umiejętność wroga [138204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Umiejętność wroga [138204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 267 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Umiejętność wroga [138204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Umiejętność wroga [138204] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138204].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 10 Blunt bonus damage
   PL:
417. [Umiejętność wroga [138204] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138204].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Umiejętność wroga [138204] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138204].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Paralysis]
   PL:
419. [Umiejętność wroga [138206] (ulepszenie 1) — nazwa] 포장 하나 뜯는다!
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138206].levelList[level=1].name
   limit: do 50 znaków
   EN: Gonna Unbox a Layer of Packaging!
   PL:
420. [Umiejętność wroga [138206] (ulepszenie 1) — opis] [WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 파괴되지 않은 코인 적중시 추가 타격 피해 10\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[EndSkill] [MiddleFatherSwordOne]이 [MiddleFatherSwordTwo] 상태가 됨
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138206].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ReinforcedTattooSpider], [DefeatDuel], [EndSkill], [MiddleFatherSwordOne], [MiddleFatherSwordTwo]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [MiddleFatherSwordOne] = 봉인된 검 / Sealed Sword; [MiddleFatherSwordTwo] = 1단계 봉인 해제 / First Seal Removed
   EN: [WhenUse] If this unit has [ReinforcedTattooSpider], deal 10 Blunt bonus damage On Hit with Unbroken Coin\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[EndSkill] [MiddleFatherSwordOne] becomes [MiddleFatherSwordTwo]
   PL:
421. [Umiejętność wroga [138206] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Umiejętność wroga [138206] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138206].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Umiejętność wroga [138206] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138206].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Umiejętność wroga [138206] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138206].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Umiejętność wroga [138206] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138206].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Umiejętność wroga [138206] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138206].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Umiejętność wroga [138207] (ulepszenie 1) — nazwa] 짓밟기
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138207].levelList[level=1].name
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Umiejętność wroga [138207] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면 코인 위력 +1\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 [Laceration] 1 추가 부여\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[DefeatDuel] 다음 턴에 [ParryingResultUp] 1 얻음 (턴당 2회)
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138207].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [ReinforcedTattooSpider], [DefeatDuel], [ParryingResultUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [DefeatDuel] = [합 패배] / [Clash Lose]; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: If target has 4+ [Laceration], Coin Power +1\n[WhenUse] If this unit has [ReinforcedTattooSpider], inflict 1 [Laceration] On Coin Hit\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[DefeatDuel] Gain 1 [ParryingResultUp] next turn (2 times per turn)
   PL:
429. [Umiejętność wroga [138207] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138207].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Umiejętność wroga [138207] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138207].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Umiejętność wroga [138207] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138207].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Umiejętność wroga [138207] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138207].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Umiejętność wroga [138209] (ulepszenie 1) — nazwa] 원한 스탬핑
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138209].levelList[level=1].name
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Umiejętność wroga [138209] (ulepszenie 1) — opis] 대상의 [Laceration] 3당 기본 위력 +1 (최대 3)\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 [Laceration] 1 추가 부여\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[EndSkill] 자신의 [ResentmentSpider]을 전부 소모하고, [DaughterEducationSpider] 1 얻음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138209].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [ReinforcedTattooSpider], [DefeatDuel], [EndSkill], [ResentmentSpider], [DaughterEducationSpider]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [ResentmentSpider] = 중지 - 원한 / The Middle - Grudge; [DaughterEducationSpider] = 잘 봐둬라 딸! / Check This Out, Kiddo!
   EN: Base Power +1 for every 3 [Laceration] on target (max 3)\n[WhenUse] If this unit has [ReinforcedTattooSpider], inflict 1 [Laceration] On Coin Hit\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[EndSkill] Consume all [ResentmentSpider] on self and gain 1 [DaughterEducationSpider]
   PL:
435. [Umiejętność wroga [138209] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138209].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Umiejętność wroga [138209] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138209].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Umiejętność wroga [138209] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138209].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Umiejętność wroga [138209] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138209].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Umiejętność wroga [138209] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138209].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Umiejętność wroga [138209] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138209].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 4 [Laceration]
   PL:
441. [Umiejętność wroga [138209] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138209].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Umiejętność wroga [138209] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138209].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Umiejętność wroga [138209] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138209].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Umiejętność wroga [138210] (ulepszenie 1) — nazwa] 후끈해지지 않나?!
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138210].levelList[level=1].name
   limit: do 40 znaków
   EN: Are Ya Feelin' the Heat?!
   PL:
445. [Umiejętność wroga [138210] (ulepszenie 1) — opis] [WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 파괴되지 않은 코인 적중시 추가 타격 피해 10\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[BeforeAttack] 자신의 체력이 50% 이하일 때, 피해량 +40%
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138210].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ReinforcedTattooSpider], [DefeatDuel], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [WhenUse] If this unit has [ReinforcedTattooSpider], deal 10 Blunt bonus damage On Hit with Unbroken Coin\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[BeforeAttack] At 50%- HP, deal +40% damage
   PL:
446. [Umiejętność wroga [138210] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138210].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Umiejętność wroga [138210] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138210].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL:
448. [Umiejętność wroga [138210] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138210].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 267 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Umiejętność wroga [138210] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138210].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Umiejętność wroga [138210] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138210].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Umiejętność wroga [138210] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 15
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138210].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 15 Blunt bonus damage
   PL:
452. [Umiejętność wroga [138210] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138210].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Umiejętność wroga [138210] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138210].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Umiejętność wroga [138210] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138210].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Paralysis]
   PL:
455. [Umiejętność wroga [138212] (ulepszenie 1) — nazwa] 두번째 포장지까지 벗기게 되는군.
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138212].levelList[level=1].name
   limit: do 70 znaków
   EN: Looks Like I Gotta Unbox the Second Layer, too.
   PL:
456. [Umiejętność wroga [138212] (ulepszenie 1) — opis] [WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 파괴되지 않은 코인 적중시 추가 타격 피해 10\n[EndSkill] [MiddleFatherSwordTwo] 상태가 [MiddleFatherSwordThree] 상태가 됨
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138212].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ReinforcedTattooSpider], [EndSkill], [MiddleFatherSwordTwo], [MiddleFatherSwordThree]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [EndSkill] = [공격 종료시] / [Attack End]; [MiddleFatherSwordTwo] = 1단계 봉인 해제 / First Seal Removed; [MiddleFatherSwordThree] = 2단계 봉인 해제 / Second Seal Removed
   EN: [WhenUse] If this unit has [ReinforcedTattooSpider], deal 10 Blunt bonus damage On Hit with Unbroken Coin\n[EndSkill] [MiddleFatherSwordTwo] becomes [MiddleFatherSwordThree]
   PL:
457. [Umiejętność wroga [138212] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138212].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Umiejętność wroga [138212] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138212].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Umiejętność wroga [138212] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138212].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Umiejętność wroga [138212] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138212].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Umiejętność wroga [138212] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138212].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Umiejętność wroga [138212] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138212].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Umiejętność wroga [138212] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138212].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Umiejętność wroga [138212] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 5 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138212].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 5 [Vulnerable]
   PL:
465. [Umiejętność wroga [138213] (ulepszenie 1) — nazwa] 짓밟기!
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138213].levelList[level=1].name
   limit: do 40 znaków
   EN: Stomping!
   PL:
466. [Umiejętność wroga [138213] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면 코인 위력 +1\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 [Laceration] 1 추가 부여\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[DefeatDuel] 다음 턴에 [SkillPowerUp] 1 얻음 (턴당 2회)
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138213].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [ReinforcedTattooSpider], [DefeatDuel], [SkillPowerUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [DefeatDuel] = [합 패배] / [Clash Lose]; [SkillPowerUp] = 기본 위력 증가 / Base Power Up
   EN: If target has 4+ [Laceration], Coin Power +1\n[WhenUse] If this unit has [ReinforcedTattooSpider], inflict 1 [Laceration] On Coin Hit\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[DefeatDuel] Gain 1 [SkillPowerUp] next turn (2 times per turn)
   PL:
467. [Umiejętność wroga [138213] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138213].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL:
468. [Umiejętność wroga [138213] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138213].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Umiejętność wroga [138213] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138213].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
470. [Umiejętność wroga [138213] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138213].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Umiejętność wroga [138215] (ulepszenie 1) — nazwa] 즉결 처형 스탬핑!
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138215].levelList[level=1].name
   limit: do 60 znaków
   EN: Stamp of Complete and Total Extermination!
   PL:
472. [Umiejętność wroga [138215] (ulepszenie 1) — opis] 대상의 [Laceration] 3당 기본 위력 +1 (최대 3)\n[WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 코인 적중시 [Laceration] 1 추가 부여\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[EndSkill] 자신의 [ResentmentSpider]을 전부 소모하고, [DaughterEducationSpider] 1 얻음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138215].levelList[level=1].desc
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Umiejętność wroga [138215] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138215].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Umiejętność wroga [138215] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138215].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Umiejętność wroga [138215] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138215].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Umiejętność wroga [138215] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138215].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Umiejętność wroga [138215] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138215].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Umiejętność wroga [138215] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138215].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [Laceration]
   PL:
479. [Umiejętność wroga [138215] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138215].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Umiejętność wroga [138215] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138215].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
481. [Umiejętność wroga [138215] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpider]이 있으면, [Paralysis] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138215].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Umiejętność wroga [138216] (ulepszenie 1) — nazwa] 슬슬 녹아 죽을 차례다
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138216].levelList[level=1].name
   limit: do 40 znaków
   EN: Time to Melt Away and Die
   PL:
483. [Umiejętność wroga [138216] (ulepszenie 1) — opis] [WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 파괴되지 않은 코인 적중시 추가 참격 피해 10\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[BeforeAttack] 자신의 체력이 50% 이하일 때, 피해량 +40%
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138216].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ReinforcedTattooSpider], [DefeatDuel], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [WhenUse] If this unit has [ReinforcedTattooSpider], deal 10 Slash bonus damage On Hit with Unbroken Coin\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[BeforeAttack] At 50%- HP, deal +40% damage
   PL:
484. [Umiejętność wroga [138216] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138216].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Umiejętność wroga [138216] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138216].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 4 [Combustion]
   PL:
486. [Umiejętność wroga [138216] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138216].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 267 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Umiejętność wroga [138216] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138216].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Umiejętność wroga [138216] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138216].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 485 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Umiejętność wroga [138216] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 추가 참격 피해 15
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138216].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 15 Slash bonus damage
   PL:
490. [Umiejętność wroga [138216] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138216].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Umiejętność wroga [138216] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138216].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 485 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Umiejętność wroga [138216] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Paralysis] 3 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138216].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 454 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Umiejętność wroga [138218] (ulepszenie 1) — nazwa] 레바테인 - 여기까지 꺼내는 것도 오랜만이군!
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138218].levelList[level=1].name
   limit: do 90 znaków
   EN: Lævateinn - Been a While Since I Had to Unbox the Whole Thing!
   PL:
494. [Umiejętność wroga [138218] (ulepszenie 1) — opis] [WhenUse] 자신에게 [ReinforcedTattooSpider]이 있으면, 파괴되지 않고 코인 적중시 추가 참격 피해 10\n[EndSkill] [MiddleFatherSwordThree] 상태가 [MiddleFatherSwordFour]이 됨
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138218].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ReinforcedTattooSpider], [EndSkill], [MiddleFatherSwordThree], [MiddleFatherSwordFour]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [EndSkill] = [공격 종료시] / [Attack End]; [MiddleFatherSwordThree] = 2단계 봉인 해제 / Second Seal Removed; [MiddleFatherSwordFour] = 레바테인 / Lævateinn
   EN: [WhenUse] If this unit has [ReinforcedTattooSpider], deal 10 Slash bonus damage On Hit with Unbroken Coin\n[EndSkill] [MiddleFatherSwordThree] becomes [MiddleFatherSwordFour]
   PL:
495. [Umiejętność wroga [138218] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138218].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Umiejętność wroga [138218] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 참격 피해 10
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138218].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 10 Slash bonus damage
   PL:
497. [Umiejętność wroga [138218] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138218].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Umiejętność wroga [138218] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 참격 피해 10
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138218].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Umiejętność wroga [138218] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138218].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Umiejętność wroga [138218] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 참격 피해 10
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138218].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Umiejętność wroga [138218] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138218].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Umiejętność wroga [138218] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Vulnerable] 10 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138218].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 10 [Vulnerable]
   PL:
503. [Umiejętność wroga [138220] (ulepszenie 1) — nazwa] 칼빵 [레바테인]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138220].levelList[level=1].name
   limit: do 40 znaków
   EN: Gut Stab [Lævateinn]
   PL:
504. [Umiejętność wroga [138220] (ulepszenie 1) — opis] [BeforeUse] 자신의 정신력 10 감소\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음\n[BeforeAttack] 자신의 체력이 50% 이하일 때, 피해량 +40%\n[BeforeAttack] (이 스킬의 코인 수 x 2)만큼 [Combustion] 얻음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138220].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [DefeatDuel], [BeforeAttack], [Combustion]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Combustion] = 화상 / Burn
   EN: [BeforeUse] Lose 10 SP\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target\n[BeforeAttack] At 50%- HP, deal +40% damage\n[BeforeAttack] Gain (# of Coins in this Skill x 2) [Combustion]
   PL:
505. [Umiejętność wroga [138220] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138220].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Umiejętność wroga [138220] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138220].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Umiejętność wroga [138220] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138220].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Umiejętność wroga [138220] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 10
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138220].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Umiejętność wroga [138220] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138220].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Umiejętność wroga [138220] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 10 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138220].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 10 [Combustion]
   PL:
511. [Umiejętność wroga [138220] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138220].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Umiejętność wroga [138220] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 4 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138220].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +4 [Combustion] Count
   PL:
513. [Umiejętność wroga [138220] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138220].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Umiejętność wroga [138220] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] [Combustion] 10 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138220].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Umiejętność wroga [138801] (ulepszenie 1) — nazwa] 몸 좀 풀어볼까?
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138801].levelList[level=1].name
   limit: do 40 znaków
   EN: Time for Some Warm-up!
   PL:
516. [Umiejętność wroga [138801] (ulepszenie 1) — opis] 대상의 [Laceration]이 5 이상이면 기본 위력 +2\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138801].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [DefeatDuel]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has 5+ [Laceration], Base Power +2\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL:
517. [Umiejętność wroga [138801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 3
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 3 Blunt bonus damage
   PL:
518. [Umiejętność wroga [138801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 3
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 517 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Umiejętność wroga [138801] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138801].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Umiejętność wroga [138801] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 3
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138801].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 3 Blunt bonus damage
   PL:
521. [Umiejętność wroga [138801] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpiderDaughter]이 있으면, 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138801].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ReinforcedTattooSpiderDaughter], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ReinforcedTattooSpiderDaughter] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] If this unit has [ReinforcedTattooSpiderDaughter], inflict 2 [Binding] next turn
   PL:
522. [Umiejętność wroga [138804] (ulepszenie 1) — nazwa] 십자난무!
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138804].levelList[level=1].name
   limit: do 40 znaków
   EN: Crossing Dervish!
   PL:
523. [Umiejętność wroga [138804] (ulepszenie 1) — opis] 이 스킬은 [HeatingWireOnSpider] 상태일 때 열선 효과가 적용됨\n대상의 [Laceration]이 4 이상이면 코인 위력 +1\n[WhenUse] 자신에게 [ReinforcedTattooSpiderDaughter]이 있으면, 코인 적중시 대상의 [Laceration] 횟수 1 증가\n[DefeatDuel] 이 스킬 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138804].levelList[level=1].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [HeatingWireOnSpider], [Laceration], [WhenUse], [ReinforcedTattooSpiderDaughter], [DefeatDuel]
   znaczenie tagów: [HeatingWireOnSpider] = 열선 ON / Thermal Blades ON; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [ReinforcedTattooSpiderDaughter] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Thermal Blade Skill. \nWhen in [HeatingWireOnSpider] state, this Skill activates its Thermal Blade effects\nIf target has 4+ [Laceration], Coin Power +1\n[WhenUse] If this unit has [ReinforcedTattooSpiderDaughter], inflict +1 [Laceration] Count On Coin Hit\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL:
524. [Umiejętność wroga [138804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Umiejętność wroga [138804] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138804].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Umiejętność wroga [138804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Umiejętność wroga [138804] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138804].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Umiejętność wroga [138804] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138804].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Umiejętność wroga [138804] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138804].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Umiejętność wroga [138804] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138804].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Umiejętność wroga [138804] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 추가 타격 피해 5
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138804].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 5 Blunt bonus damage
   PL:
532. [Umiejętność wroga [138804] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신에게 [ReinforcedTattooSpiderDaughter]이 있으면, 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138804].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 521 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Umiejętność wroga [138107] (ulepszenie 1) — nazwa] 소리를 부수고, 생각을 납작하게 짓이겨라
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138107].levelList[level=1].name
   limit: do 60 znaków
   EN: Destroy the Sound, Crush Flat the Thought
   PL:
534. [Umiejętność wroga [138107] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[BlackNightmare]이 있으면,\n- 모든 코인이 [SuperCoin]으로 변경됨\n- <color=#ff6000><mark=#ff000040><b><u>합을 지정한 대상이 타격 스킬이 아니면</u></b></mark></color>, 코인 위력 +2, 피해량 +50%\n- 타격 스킬에게 합 패배 시, 코인 위력 -2, 피해량 -50%, 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n\n타격 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 타격 무기일 경우, 피해량 +60%\n- 타격 무기가 아닐 경우, 피해량 -30%\n[WhenUse] [Breath] 3 얻음, [Breath] 횟수 2 증가\n[WinDuel] 25만큼 흐트러짐 피해\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 발동하지 않음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138107].levelList[level=1].desc
   limit: do 1100 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BlackNightmare], [SuperCoin], [Sinking], [KarmaOfIndexRien_2Phase], [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [BlackNightmare] = 지령 탐닉 / Indulgence in Prescripts; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Sinking] = 침잠 / Sinking; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Can Clash with this Skill regardless of Speed\nIf this unit has [BlackNightmare]:\n- Convert all Coins to [SuperCoin]s\n- <color=#ff6000><mark=#ff000040><b><u>When clashing against a non-Blunt Skill</u></b></mark></color>, Coin Power +2 and deal +50% damage\n- On Clash Lose against a Blunt Skill:\n  - Coin Power -2 and deal -50% damage\n  - Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n\nBlunt weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Blunt weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Blunt weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Blunt weapons deal +60% damage\n- Non-Blunt weapons deal -30% damage\n[WhenUse] Gain 3 [Breath] and +2 [Breath] Count\n[WinDuel] Raise target's Stagger Threshold by 25\n- At 150+ [KarmaOfIndexRien_2Phase], this effect does not activate
   PL:
535. [Umiejętność wroga [138107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Sinking]
   PL:
536. [Umiejętność wroga [138107] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138107].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Sinking] Count
   PL:
537. [Umiejętność wroga [138107] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138107].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Umiejętność wroga [138107] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138107].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain 2 [Breath]
   PL:
539. [Umiejętność wroga [138107] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138107].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Umiejętność wroga [138107] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138107].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain +2 [Breath] Count
   PL:
541. [Umiejętność wroga [138108] (ulepszenie 1) — nazwa] 고요의 중심을 찌르고, 기억을 꿰뚫어라
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138108].levelList[level=1].name
   limit: do 70 znaków
   EN: Stab the Heart of Silence, Penetrate the Memory
   PL:
542. [Umiejętność wroga [138108] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[BlackNightmare]이 있으면,\n- 모든 코인이 [SuperCoin]으로 변경됨\n- <color=#ff6000><mark=#ff000040><b><u>합을 지정한 대상이 관통 스킬이 아니면</u></b></mark></color>, 코인 위력 +2, 피해량 +50%\n- 관통 스킬에게 합 패배 시, 코인 위력 -2, 피해량 -50%, 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n\n관통 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 관통 무기일 경우, 피해량 +60%\n- 관통 무기가 아닐 경우, 피해량 -30%\n[WhenUse] [Breath] 3 얻음, [Breath] 횟수 2 증가\n[WinDuel] 다음 턴에 [AttackDmgUp] 2 얻음\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 발동하지 않음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138108].levelList[level=1].desc
   limit: do 1090 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BlackNightmare], [SuperCoin], [Sinking], [KarmaOfIndexRien_2Phase], [WhenUse], [Breath], [WinDuel], [AttackDmgUp]
   znaczenie tagów: [BlackNightmare] = 지령 탐닉 / Indulgence in Prescripts; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Sinking] = 침잠 / Sinking; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Can Clash with this Skill regardless of Speed\nIf this unit has [BlackNightmare]:\n- Convert all Coins to [SuperCoin]s\n- <color=#ff6000><mark=#ff000040><b><u>When clashing against a non-Pierce Skill</u></b></mark></color>, Coin Power +2 and deal +50% damage\n- On Clash Lose against a Pierce Skill:\n  - Coin Power -2 and deal -50% damage\n  - Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n\nPierce weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Pierce weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Pierce weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Pierce weapons deal +60% damage\n- Non-Pierce weapons deal -30% damage\n[WhenUse] Gain 3 [Breath] and +2 [Breath] Count\n[WinDuel] Gain 2 [AttackDmgUp] next turn\n- At 150+ [KarmaOfIndexRien_2Phase], this effect does not activate
   PL:
543. [Umiejętność wroga [138108] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138108].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 535 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Umiejętność wroga [138108] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138108].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain 3 [Breath]
   PL:
545. [Umiejętność wroga [138108] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138108].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Umiejętność wroga [138108] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138108].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 536 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [Umiejętność wroga [138108] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138108].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Umiejętność wroga [138108] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138108].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Umiejętność wroga [138109] (ulepszenie 1) — nazwa] 날카롭게 벼린 비밀로, 형태를 베어내라
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138109].levelList[level=1].name
   limit: do 50 znaków
   EN: With Tempered Secret, Sever the Form
   PL:
550. [Umiejętność wroga [138109] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[BlackNightmare]이 있으면,\n- 모든 코인이 [SuperCoin]으로 변경됨\n- <color=#ff6000><mark=#ff000040><b><u>합을 지정한 대상이 참격 스킬이 아니면,</u></b></mark></color> 코인 위력 +2, 피해량 +50%\n- 참격 스킬에게 합 패배 시, 코인 위력 -2, 피해량 -50%, 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n\n참격 무기가 더욱 자주 등장\n- [KarmaOfIndexRien_2Phase]가 75 이상이면, 등장 확률 감소\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 등장 확률 추가로 감소\n사용하는 무기의 공격 유형에 따라 효과 적용\n- 참격 무기일 경우, 피해량 +60%\n- 참격 무기가 아닐 경우, 피해량 -30%\n[WhenUse] [Breath] 3 얻음, [Breath] 횟수 2 증가\n[WinDuel] 최종 위력 +3\n- [KarmaOfIndexRien_2Phase]가 150 이상이면, 발동하지 않음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138109].levelList[level=1].desc
   limit: do 1070 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BlackNightmare], [SuperCoin], [Sinking], [KarmaOfIndexRien_2Phase], [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [BlackNightmare] = 지령 탐닉 / Indulgence in Prescripts; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Sinking] = 침잠 / Sinking; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Can Clash with this Skill regardless of Speed\nIf this unit has [BlackNightmare]:\n- Convert all Coins to [SuperCoin]s\n- <color=#ff6000><mark=#ff000040><b><u>When clashing against a non-Slash Skill</u></b></mark></color>, Coin Power +2 and deal +50% damage\n- On Clash Lose against a Slash Skill:\n  - Coin Power -2 and deal -50% damage\n  - Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n\nSlash weapons appear more frequently\n- At 75+ [KarmaOfIndexRien_2Phase], Slash weapons appear less frequently\n- At 150+ [KarmaOfIndexRien_2Phase], Slash weapons appear even less frequently\nThe following effects activate depending on the weapon's Attack Type\n- Slash weapons deal +60% damage\n- Non-Slash weapons deal -30% damage\n[WhenUse] Gain 3 [Breath] and +2 [Breath] Count\n[WinDuel] Final Power +3\n- At 150+ [KarmaOfIndexRien_2Phase], this effect does not activate
   PL:
551. [Umiejętność wroga [138109] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138109].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 544 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Umiejętność wroga [138109] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138109].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Breath]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Breath] = 호흡 / Poise
   EN: [UnBrokenCoinOnSucceedAttack] Gain +3 [Breath] Count
   PL:
553. [Umiejętność wroga [138109] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138109].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Umiejętność wroga [138109] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138109].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL:
555. [Umiejętność wroga [138109] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138109].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Umiejętność wroga [138109] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138109].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 536 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Umiejętność wroga [138010] (ulepszenie 1) — nazwa] Furioso-Replica
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138010].levelList[level=1].name
   limit: do 40 znaków
   EN: Furioso-Replica
   PL:
558. [Umiejętność wroga [138010] (ulepszenie 1) — opis] [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>이 스킬은 대상의 수비 스킬을 발동시키지 않음</u></b></mark></color>\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- [Breath] 3 얻음, 자신의 [Breath] 횟수 3 증가\n- 합 위력 +5 (<color=#ff6000><mark=#ff000040><b><u>자신의 [KarmaOfIndexRien] 5당 1씩 감소, 최소 0</u></b></mark></color>)\n[WhenUse] 정신력이 0 이상이면, 망 1개 생성\n- 피해량이 20%만큼 증가하고 최종 위력 +3\n[WinDuel] \n- [Breath] 3 얻음, 자신의 [Breath] 횟수 3 증가\n- 공격 종료 시 공격이 적중한 모든 대상에게 다음 턴에 [Laceration] 3, [Binding] 1, [Vulnerable] 1 부여\n[DefeatDuel]\n- 최종 피해량이 80%만큼 감소\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n[EndSkill] 망을 생성했으면, 정신력 20만큼 감소\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138010].levelList[level=1].desc
   limit: do 910 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WideAreaRampage], [WhenUse], [Breath], [KarmaOfIndexRien], [WinDuel], [Laceration], [Binding], [Vulnerable], [DefeatDuel], [Sinking], [EndSkill]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [KarmaOfIndexRien] = 카르마 / Karmic Consequence; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile …
   EN: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>This Skill does not trigger the target's Defense Skills</u></b></mark></color>\nCan Clash with this Skill regardless of Speed\n[WhenUse]\n- Gain 3 [Breath] and +3 [Breath] Count\n- Clash Power +5 (<color=#ff6000><mark=#ff000040><b><u>Clash Power gained is reduced by 1 for every 5 [KarmaOfIndexRien] on self, down to 0</u></b></mark></color>)\n[WhenUse] At 0+ SP, generate 1 Mang\n- Deal +20% damage; Final Power +3\n\n[WinDuel]\n- Gain 3 [Breath] and +3 [Breath] Count\n- Attack End: Inflict 3 [Laceration], 1 [Binding], and 1 [Vulnerable] next turn to all targets this unit hit\n[DefeatDuel]\n- Deal -80% final damage\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] If this Skill generated Mang, lose 20 SP\n[EndSkill] End this turn
   PL:
559. [Umiejętność wroga [138010] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138010].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Umiejętność wroga [138010] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138010].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Umiejętność wroga [138010] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>이 코인 재사용 (최대 7회)</u></b></mark></color>
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138010].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Reuse this Coin (7 times max)</u></b></mark></color>
   PL:
562. [Umiejętność wroga [138010] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138010].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Sinking]
   PL:
563. [Umiejętność wroga [138110] (ulepszenie 1) — nazwa] Furioso [Crescendo]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138110].levelList[level=1].name
   limit: do 40 znaków
   EN: Furioso [Crescendo]
   PL:
564. [Umiejętność wroga [138110] (ulepszenie 1) — opis] [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>이 스킬은 대상의 수비 스킬을 발동시키지 않음</u></b></mark></color>\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- [Breath] 6 얻음, 자신의 [Breath] 횟수 6 증가\n- 합 위력 +10 (<color=#ff6000><mark=#ff000040><b><u>자신의 [KarmaOfIndexRien_2Phase] 5당 1씩 감소</u></b></mark></color>)\n[WhenUse] 정신력이 0 이상이면, 망 2개 생성\n- 피해량이 40%만큼 증가하고 최종 위력 +5\n[WinDuel]\n- 공격 종료 시 공격이 적중한 모든 대상에게 다음 턴에 [Laceration] 4, [Binding] 2, [Vulnerable] 2 부여\n[DefeatDuel]\n- 최종 피해량이 80%만큼 감소\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n[EndSkill] 망을 생성했으면, 정신력 25만큼 감소\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138110].levelList[level=1].desc
   limit: do 860 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WideAreaRampage], [WhenUse], [Breath], [KarmaOfIndexRien_2Phase], [WinDuel], [Laceration], [Binding], [Vulnerable], [DefeatDuel], [Sinking], [EndSkill]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile …
   EN: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>This Skill does not trigger the target's Defense Skills</u></b></mark></color>\nCan Clash with this Skill regardless of Speed\n[WhenUse]\n- Gain 6 [Breath] and +6 [Breath] Count\n- Clash Power +10 (<color=#ff6000><mark=#ff000040><b><u>Clash Power gained is reduced by 1 for every 5 [KarmaOfIndexRien_2Phase] on self</u></b></mark></color>)\n[WhenUse] At 0+ SP, generate 2 Mangs\n- Deal +40% damage; Final Power +5\n\n[WinDuel]\n- Attack End: Inflict 4 [Laceration], 2 [Binding], and 2 [Vulnerable] next turn to all targets this unit hit\n[DefeatDuel]\n- Deal -80% final damage\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] If this Skill generated Mang, lose 25 SP\n[EndSkill] End this turn
   PL:
565. [Umiejętność wroga [138110] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138110].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Umiejętność wroga [138110] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138110].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Umiejętność wroga [138110] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>이 코인 재사용 (최대 7회)</u></b></mark></color>
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138110].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Umiejętność wroga [138110] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138110].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Umiejętność wroga [138111] (ulepszenie 1) — nazwa] Furioso [Lacrimosa-Crescendo]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138111].levelList[level=1].name
   limit: do 50 znaków
   EN: Furioso [Lacrimosa-Crescendo]
   PL:
570. [Umiejętność wroga [138111] (ulepszenie 1) — opis] [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>이 스킬은 대상의 수비 스킬을 발동시키지 않음</u></b></mark></color>\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- [Breath] 9 얻음, 자신의 [Breath] 횟수 9 증가\n- 합 위력 +15 (자신의 [KarmaOfIndexRien_2Phase] 5당 1씩 감소)\n[WhenUse] 정신력이 0 이상이면, 망 3개 생성\n- 피해량이 60%만큼 증가하고 최종 위력 +8\n[WinDuel]\n- 공격 종료 시 공격이 적중한 모든 대상에게 다음 턴에 [Laceration] 5, [Binding] 3, [Vulnerable] 3 부여\n[DefeatDuel]\n- 최종 피해량이 80%만큼 감소\n- 이 스킬의 피해로 대상이 흐트러지지 않고 적중 시 대상의 [Sinking] 효과가 발동하지 않음\n[EndSkill] 망을 생성했으면, 정신력 30만큼 감소\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138111].levelList[level=1].desc
   limit: do 860 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WideAreaRampage], [WhenUse], [Breath], [KarmaOfIndexRien_2Phase], [WinDuel], [Laceration], [Binding], [Vulnerable], [DefeatDuel], [Sinking], [EndSkill]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed; [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile …
   EN: [WideAreaRampage]\n<color=#ff6000><mark=#ff000040><b><u>This Skill does not trigger the target's Defense Skills</u></b></mark></color>\nCan Clash with this Skill regardless of Speed\n[WhenUse]\n- Gain 9 [Breath] and +9 [Breath] Count\n- Clash Power +15 (Clash Power gained is reduced by 1 for every 5 [KarmaOfIndexRien_2Phase] on self)\n[WhenUse] At 0+ SP, generate 3 Mangs\n- Deal +60% damage; Final Power +8\n\n[WinDuel]\n- Attack End: Inflict 5 [Laceration], 3 [Binding], and 3 [Vulnerable] next turn to all targets this unit hit\n[DefeatDuel]\n- Deal -80% final damage\n- Damage dealt by this Skill cannot Stagger the target; On Hit, does not activate [Sinking] on target\n[EndSkill] If this Skill generated Mang, lose 30 SP\n[EndSkill] End this turn
   PL:
571. [Umiejętność wroga [138111] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138111].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Umiejętność wroga [138111] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138111].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Umiejętność wroga [138111] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>이 코인 재사용 (최대 7회)</u></b></mark></color>
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138111].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Umiejętność wroga [138111] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138111].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Umiejętność wroga [138301] (ulepszenie 1) — nazwa] 설치 미술 제 3호 ‘간이늑골’
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138301].levelList[level=1].name
   limit: do 60 znaków
   EN: Installation Art no. 3: Improvised Ribcage
   PL:
576. [Umiejętność wroga [138301] (ulepszenie 1) — opis] [CantDuel] [CantChangeTarget]\n레벨이 높은 적 우선 지정\n이 스킬은 수비 스킬을 발동시키지 않음\n[WhenUse] 대상의 [Laceration] 8당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138301].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [WhenUse], [Laceration]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [CantDuel] [CantChangeTarget]\nPrioritizes enemy with the highest level\nThis Skill does not trigger Defense Skills\n[WhenUse] Coin Power +1 for every 8 [Laceration] on target (max 2)
   PL:
577. [Umiejętność wroga [138301] (ulepszenie 1) — moneta 1, efekt 1 — opis] 이 코인은 체력 피해를 입히지 않음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: This Coin does not deal HP damage
   PL:
578. [Umiejętność wroga [138301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 정신력 15 회복
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 15 SP on self
   PL:
579. [Umiejętność wroga [138301] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>흐트러짐 상태로 만들고 다음 턴에 [LivingSpecimenTheRings]으로 만듦</u></b></mark></color>
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138301].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [OnSucceedAttack], [LivingSpecimenTheRings]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LivingSpecimenTheRings] = 신체관극 / Corpus Theater
   EN: [OnSucceedAttack]\n<color=#ff6000><mark=#ff000040><b><u>Stagger target and turn target into [LivingSpecimenTheRings] next turn</u></b></mark></color>
   PL:
580. [Umiejętność wroga [138302] (ulepszenie 1) — nazwa] 해체
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138302].levelList[level=1].name
   limit: do 40 znaków
   EN: Anatomize
   PL:
581. [Umiejętność wroga [138302] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[DefeatDuel] 최종 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138302].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] If target has 6+ [Laceration], Coin Power +1\n[DefeatDuel] Deal -80% final damage and damage dealt by this Skill cannot Stagger the target
   PL:
582. [Umiejętność wroga [138302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Umiejętność wroga [138302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Umiejętność wroga [138302] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138302].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Umiejętność wroga [138302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Umiejętność wroga [138302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL:
587. [Umiejętność wroga [138302] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138302].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Protection]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Protection] = 보호 / Protection
   EN: [OnSucceedAttack] Gain 1 [Protection] next turn
   PL:
588. [Umiejętność wroga [138303] (ulepszenie 1) — nazwa] 재료획득 - 피로 목욕하는 오브제
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138303].levelList[level=1].name
   limit: do 60 znaków
   EN: Gather Ingredient - Blood-bathed Objet
   PL:
589. [Umiejętność wroga [138303] (ulepszenie 1) — opis] 신체관극을 대상으로 우선 지정함\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[DefeatDuel] 최종 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138303].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes Corpus Theaters\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[DefeatDuel] Deal -80% final damage and damage dealt by this Skill cannot Stagger the target
   PL:
590. [Umiejętność wroga [138303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Umiejętność wroga [138303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 208 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność wroga [138303] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138303].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Umiejętność wroga [138303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Umiejętność wroga [138303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ResultReduction] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ResultReduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ResultReduction] = 위력 감소 / Power Down
   EN: [OnSucceedAttack] Inflict 1 [ResultReduction] next turn
   PL:
595. [Umiejętność wroga [138303] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [ResultEnhancement] 1 얻음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138303].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ResultEnhancement]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ResultEnhancement] = 위력 증가 / Power Up
   EN: [OnSucceedAttack] Gain 1 [ResultEnhancement] next turn
   PL:
596. [Umiejętność wroga [138304] (ulepszenie 1) — nazwa] 티비아의 멜로디 - 해체된 것이 해체되지 않은 것을 해체하는 것
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138304].levelList[level=1].name
   limit: do 90 znaków
   EN: Tibia's Melody - Anatomization of the Unanatomized by the Anatomized
   PL:
597. [Umiejętność wroga [138304] (ulepszenie 1) — opis] 이 스킬을 장착한 턴에 <color=#ff6000><mark=#ff000040><b><u>공격 스킬로 피격 시</u></b></mark></color>, [PlusCoinValueDown] 1, [ResultReduction] 1 얻음 (스킬당 1회. 턴당 최대 3회)\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n이 스킬로 처치한 대상 하나당 정신력 15 회복\n[StartBattle] [Protection] 4 얻음\n[WhenUse] 메인 타겟과 서브 타겟의 [Laceration]의 합 6당, 피해량 +3% (최대 30%)\n[DefeatDuel] 최종 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] [MineTheRings] 소멸
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138304].levelList[level=1].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [PlusCoinValueDown], [ResultReduction], [StartBattle], [Protection], [WhenUse], [Laceration], [DefeatDuel], [EndSkill], [MineTheRings]
   znaczenie tagów: [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop; [ResultReduction] = 위력 감소 / Power Down; [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: During the turn this unit has this Skill equipped, gain 1 [PlusCoinValueDown] and 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>when hit by Attack Skills</u></b></mark></color> (once per Skill; max 3 times per turn)\nCannot be Staggered before using this Skill\nOn Kill with this Skill: heal 15 SP for every target killed\n[StartBattle] Gain 4 [Protection]\n[WhenUse] Deal +3% damage for every 6 ([Laceration] on main target + [Laceration] on sub-target) (max 30%)\n[DefeatDuel] Deal -80% final damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] [MineTheRings] expires
   PL:
598. [Umiejętność wroga [138304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Umiejętność wroga [138304] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 정신력 피해 5
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 5 SP damage
   PL:
600. [Umiejętność wroga [138304] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력 5 회복 (스킬당 1회)
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138304].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 5 SP (once per Skill)
   PL:
601. [Umiejętność wroga [138304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Umiejętność wroga [138304] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138304].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL:
603. [Umiejętność wroga [138304] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138304].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Protection]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Protection] = 보호 / Protection
   EN: [OnSucceedAttack] Gain 1 [Protection] next turn (once per Skill)
   PL:
604. [Umiejętność wroga [138304] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138304].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Umiejętność wroga [138304] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138304].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [AttackDmgDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [AttackDmgDown] next turn
   PL:
606. [Umiejętność wroga [138304] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138304].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [OnSucceedAttack] Gain 1 [AttackDmgUp] next turn (once per Skill)
   PL:
607. [Umiejętność wroga [138304] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138304].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Umiejętność wroga [138304] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138304].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Umiejętność wroga [138305] (ulepszenie 1) — nazwa] 우린 피와 살을 사랑해요
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138305].levelList[level=1].name
   limit: do 60 znaków
   EN: Oh, How We Love the Flesh and the Blood
   PL:
610. [Umiejętność wroga [138305] (ulepszenie 1) — opis] 약지 제자 - 알비나를 대상으로 우선 지정함\n[DefeatDuel] <color=#ff6000><mark=#ff000040><b><u>[AttackDmgDown] 8 얻음</u></b></mark></color>
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138305].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuel], [AttackDmgDown]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: Prioritizes The Ring Apprentice - Albina\n[DefeatDuel] Gain <color=#ff6000><mark=#ff000040><b><u>8 [AttackDmgDown]</u></b></mark></color>
   PL:
611. [Umiejętność wroga [138305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Umiejętność wroga [138305] (ulepszenie 1) — moneta 1, efekt 2 — opis] 이 코인은 체력 피해를 입히지 않음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność wroga [138305] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138305].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Umiejętność wroga [138305] (ulepszenie 1) — moneta 1, efekt 4 — opis] - 대상이 아군이면 이 효과를 대신하여 다음 턴까지 [AttackUp] 6 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138305].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: - If target is an ally, apply 6 [AttackUp] instead of the effect above
   PL:
615. [Umiejętność wroga [138306] (ulepszenie 1) — nazwa] 전시회 주최
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138306].levelList[level=1].name
   limit: do 40 znaków
   EN: Curating the Exhibition
   PL:
616. [Umiejętność wroga [138306] (ulepszenie 1) — opis] [StartBattle] <color=#ff6000><mark=#ff000040><b><u>[SupportProtect] 3 얻음</u></b></mark></color>\n[WhenUse] 공격자의 공격 종료 전까지 공격자가 보유한 [Laceration] 횟수가 감소하지 않음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138306].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StartBattle], [SupportProtect], [WhenUse], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [StartBattle] <color=#ff6000><mark=#ff000040><b><u>Gain 3 [SupportProtect]</u></b></mark></color>\n[WhenUse] The attacker does not lose [Laceration] Count before Attack End
   PL:
617. [Umiejętność wroga [138307] (ulepszenie 1) — nazwa] 반달리즘은 사절이랍니다
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138307].levelList[level=1].name
   limit: do 50 znaków
   EN: Please. Vandalism is Prohibited.
   PL:
618. [Umiejętność wroga [138307] (ulepszenie 1) — opis] [DuelCounter]\n[SupportProtect] 전용 스킬\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[WhenUse] [Protection] 1 얻음\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138307].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [SupportProtect], [WhenUse], [Protection], [Laceration]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection; [Laceration] = 출혈 / Bleed
   EN: [DuelCounter]\n[SupportProtect] exclusive Skill\nCannot be Staggered before using this Skill\n[WhenUse] Gain 1 [Protection]\n[WhenUse] If target has 6+ [Laceration], Coin Power +1
   PL:
619. [Umiejętność wroga [138307] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138307].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Umiejętność wroga [138307] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138307].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Umiejętność wroga [138307] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [ResultReduction] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138307].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 594 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Umiejętność wroga [138307] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [ResultEnhancement] 1 얻음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=138307].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 595 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Umiejętność wroga [141704] (ulepszenie 1) — nazwa] 파시아 식사 시간이야
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141704].levelList[level=1].name
   limit: do 40 znaków
   EN: Time to Eat, Fascia
   PL:
624. [Umiejętność wroga [141704] (ulepszenie 1) — opis] [DefeatDuel] 최종 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Deal -80% final damage and damage dealt by this Skill cannot Stagger the target
   PL:
625. [Umiejętność wroga [141704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Umiejętność wroga [141704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 10 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 10 [Laceration]
   PL:
627. [Umiejętność wroga [141704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Umiejętność wroga [141704] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141704].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Umiejętność wroga [141704] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141704].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Umiejętność wroga [141704] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 정신력 피해 5
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141704].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 SP damage
   PL:
631. [Umiejętność wroga [141704] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력 10 회복
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141704].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność wroga [141704] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [HumanFleshTheRings] 1 얻음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141704].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [HumanFleshTheRings]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [HumanFleshTheRings] = 생체 재료 / Corpus Ingredient
   EN: [OnSucceedAttack] Gain 1 [HumanFleshTheRings]
   PL:
633. [Umiejętność wroga [141705] (ulepszenie 1) — nazwa] 억압당한 육체의 해방
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141705].levelList[level=1].name
   limit: do 50 znaków
   EN: Liberation of the Repressed Flesh
   PL:
634. [Umiejętność wroga [141705] (ulepszenie 1) — opis] 이 스킬을 장착한 턴에 <color=#ff6000><mark=#ff000040><b><u>공격 스킬로 피격 시</u></b></mark></color>, [PlusCoinValueDown] 1, [ResultReduction] 1 얻음 (스킬당 1회. 턴당 최대 3회)\n이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n이 스킬로 처치한 대상 하나당 정신력 15 회복\n[StartBattle] [Protection] 4 얻음\n[WhenUse] 메인 타겟과 서브 타겟의 [Laceration]의 합 6당, 피해량 +3% (최대 30%)\n[DefeatDuel] 최종 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] [BoneBladeTheRings] 소멸
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141705].levelList[level=1].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [PlusCoinValueDown], [ResultReduction], [StartBattle], [Protection], [WhenUse], [Laceration], [DefeatDuel], [EndSkill], [BoneBladeTheRings]
   znaczenie tagów: [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop; [ResultReduction] = 위력 감소 / Power Down; [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: During the turn this unit has this Skill equipped, gain 1 [PlusCoinValueDown] and 1 [ResultReduction] <color=#ff6000><mark=#ff000040><b><u>when hit by Attack Skills</u></b></mark></color> (once per Skill; max 3 times per turn)\nCannot be Staggered before using this Skill\nOn Kill with this Skill: heal 15 SP for every target killed\n[StartBattle] Gain 4 [Protection]\n[WhenUse] Deal +3% damage for every 6 ([Laceration] on main target + [Laceration] on sub-target) (max 30%)\n[DefeatDuel] Deal -80% final damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] [BoneBladeTheRings] expires
   PL:
635. [Umiejętność wroga [141705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Umiejętność wroga [141705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 정신력 피해 5
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 599 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Umiejętność wroga [141705] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력 5 회복 (스킬당 1회)
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141705].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 600 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [Umiejętność wroga [141705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Umiejętność wroga [141705] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141705].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 602 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Umiejętność wroga [141705] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Protection] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141705].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 603 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Umiejętność wroga [141705] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141705].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Umiejętność wroga [141705] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141705].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 605 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność wroga [141705] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgUp] 1 얻음 (스킬당 1회)
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141705].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Umiejętność wroga [141705] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141705].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Umiejętność wroga [141705] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141705].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Umiejętność wroga [141706] (ulepszenie 1) — nazwa] 시작된 전시회
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141706].levelList[level=1].name
   limit: do 40 znaków
   EN: The Exhibition Begins
   PL:
647. [Umiejętność wroga [141706] (ulepszenie 1) — opis] [StartBattle] <color=#ff6000><mark=#ff000040><b><u>[SupportProtect] 2 얻음</u></b></mark></color>\n[StartBattle] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=141706].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StartBattle], [SupportProtect], [Agility]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [Agility] = 신속 / Haste
   EN: [StartBattle] <color=#ff6000><mark=#ff000040><b><u> Gain 2 [SupportProtect]</u></b></mark></color>\n[StartBattle] Gain 1 [Agility] next turn
   PL:
648. [Umiejętność wroga [137903] (ulepszenie 1) — nazwa] 세치오나투라 디 코닐리오
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=137903].levelList[level=1].name
   limit: do 40 znaków
   EN: Sezionatura di Coniglio
   PL:
649. [Umiejętność wroga [137903] (ulepszenie 1) — opis] 자신의 [Breath]이 6 이상이면, 코인 위력 + 1\n[WhenUse] 대상의 [Combustion]과 [Vibration]의 합 4당, 기본 위력 + 1 (최대 2)
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=137903].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [WhenUse], [Combustion], [Vibration]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: At 6+ [Breath], Coin Power +1\n[WhenUse] Base Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 2)
   PL:
650. [Umiejętność wroga [137903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여, [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=137903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Umiejętność wroga [137903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여, [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=137903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and +3 [Vibration] Count
   PL:
652. [Umiejętność wroga [137903] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=137903].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]
   PL:
653. [Umiejętność wroga [137903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=137903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
654. [Umiejętność wroga [137908] (ulepszenie 1) — nazwa] 예지
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=137908].levelList[level=1].name
   limit: do 40 znaków
   EN: Precognition
   PL:
655. [Umiejętność wroga [137908] (ulepszenie 1) — opis] 스킬의 모든 코인을 회피 성공할 시, 공격한 대상에게 ‘세치오나투라 디 코닐리오’으로 일방 공격함\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>[FutureEyeOn] 수치 3당, 기본 위력 +1</u></b></mark></color>\n[WhenUse] [FullReload] (턴당 1회)\n[OnSucceedEvade] [Breath] 3 얻음 (턴당 2회)\n[OnDefeatEvade] 정신력 5 감소
   źródło: Skills_Abnormality_Mirror7.json :: dataList[id=137908].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [FutureEyeOn], [FullReload], [OnSucceedEvade], [Breath], [OnDefeatEvade]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [FutureEyeOn] = 예지안 / Eye of Precognition; [FullReload] = 재장전 / Reload; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise; [OnDefeatEvade] = [회피 실패시] / [Failed Evade]
   EN: Upon successfully evading all Coins on a Skill, use "Sezionatura di Coniglio" as an Unopposed Attack against the attacker\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>Base Power +1 for every 3 [FutureEyeOn] Stack</u></b></mark></color>\n[WhenUse] [FullReload] (once per turn)\n[OnSucceedEvade] Gain 3 [Breath] (2 times per turn)\n[OnDefeatEvade] Lose 5 SP
   PL:

## [mowe] Wróg / część: Enemies-mowe
- plik gry: `Enemies-mowe.json`

656. [[mowe] Wróg / część [90145] — nazwa] 갈구하는 피주머니 승객
   źródło: Enemies-mowe.json :: dataList[id=90145].name
   limit: do 40 znaków
   EN: Craving Bloodbag Passenger
   PL:
657. [[mowe] Wróg / część [90145] — opis] 본체
   źródło: Enemies-mowe.json :: dataList[id=90145].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [[mowe] Wróg / część [90146] — nazwa] 난폭한 피주머니 승객
   źródło: Enemies-mowe.json :: dataList[id=90146].name
   limit: do 40 znaków
   EN: Violent Bloodbag Passenger
   PL:
659. [[mowe] Wróg / część [90146] — opis] 본체
   źródło: Enemies-mowe.json :: dataList[id=90146].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [[mowe] Wróg / część [90147] — nazwa] 저돌적인 피주머니 승객
   źródło: Enemies-mowe.json :: dataList[id=90147].name
   limit: do 50 znaków
   EN: Aggressive Bloodbag Passenger
   PL:
661. [[mowe] Wróg / część [90147] — opis] 본체
   źródło: Enemies-mowe.json :: dataList[id=90147].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [[mowe] Wróg / część [90148] — nazwa] 무자비한 피주머니 정리 요원
   źródło: Enemies-mowe.json :: dataList[id=90148].name
   limit: do 50 znaków
   EN: Merciless Bloodbag Cleanup Agent
   PL:
663. [[mowe] Wróg / część [90148] — opis] 본체
   źródło: Enemies-mowe.json :: dataList[id=90148].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [[mowe] Wróg / część [90149] — nazwa] 맹렬한 피주머니 정리 요원
   źródło: Enemies-mowe.json :: dataList[id=90149].name
   limit: do 40 znaków
   EN: Feral Bloodbag Cleanup Agent
   PL:
665. [[mowe] Wróg / część [90149] — opis] 본체
   źródło: Enemies-mowe.json :: dataList[id=90149].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [[mowe] Wróg / część [90150] — nazwa] 굶주린 피주머니 정리 요원
   źródło: Enemies-mowe.json :: dataList[id=90150].name
   limit: do 50 znaków
   EN: Hungering Bloodbag Cleanup Agent
   PL:
667. [[mowe] Wróg / część [90150] — opis] 본체
   źródło: Enemies-mowe.json :: dataList[id=90150].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [[mowe] Wróg / część [90151] — nazwa] 피주머니 의체 해결사
   źródło: Enemies-mowe.json :: dataList[id=90151].name
   limit: do 40 znaków
   EN: Bloodbag Prosthetic Fixer
   PL:
669. [[mowe] Wróg / część [90151] — opis] 본체
   źródło: Enemies-mowe.json :: dataList[id=90151].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [[mowe] Wróg / część [91018] — nazwa] 사샤
   źródło: Enemies-mowe.json :: dataList[id=91018].name
   limit: do 40 znaków
   EN: Sasha
   PL:
671. [[mowe] Wróg / część [91018] — opis] 본체
   źródło: Enemies-mowe.json :: dataList[id=91018].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [[mowe] Wróg / część [8350] — nazwa] 카세티
   źródło: Enemies-mowe.json :: dataList[id=8350].name
   limit: do 40 znaków
   EN: Cassetti
   PL:
673. [[mowe] Wróg / część [8350] — opis] 본체
   źródło: Enemies-mowe.json :: dataList[id=8350].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [[mowe] Wróg / część [835001] — nazwa] 몸통
   źródło: Enemies-mowe.json :: dataList[id=835001].name
   limit: do 40 znaków
   EN: Body
   PL:
675. [[mowe] Wróg / część [835001] — opis] 본체
   źródło: Enemies-mowe.json :: dataList[id=835001].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [mowe] Umiejętności wrogów / Anomalii — Skills_Abnormality-mowe
- grupa rozdziału/trybu: `mowe` · plik: `Skills_Abnormality-mowe.json`

676. [Umiejętność wroga [835001] (ulepszenie 1) — nazwa] 조아려라
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835001].levelList[level=1].name
   limit: do 40 znaków
   EN: Grovel Before Me
   PL:
677. [Umiejętność wroga [835001] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 4 이상이면, 합 위력 +1
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 4+ [Laceration], Clash Power +1
   PL:
678. [Umiejętność wroga [835001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Umiejętność wroga [835002] (ulepszenie 1) — nazwa] 하찮은 것
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835002].levelList[level=1].name
   limit: do 40 znaków
   EN: Pathetic One
   PL:
680. [Umiejętność wroga [835002] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 4 이상이면, 합 위력 +1
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835002].levelList[level=1].desc
   (powtórzenie elementu 677 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Umiejętność wroga [835002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Umiejętność wroga [835003] (ulepszenie 1) — nazwa] 저리 가... 저리 가...!
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835003].levelList[level=1].name
   limit: do 40 znaków
   EN: Go... Go Away...!
   PL:
683. [Umiejętność wroga [835003] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 4 이상이면, 합 위력 +1\n[WhenUse] 대상의 [Laceration] 횟수당, 피해량 +5% (최대 20%)
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835003].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 4+ [Laceration], Clash Power +1\n[WhenUse] Deal +5% damage for every [Laceration] Count on the target (max 20%)
   PL:
684. [Umiejętność wroga [835003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 8 부여. [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 8 [Laceration] and +2 [Laceration] Count
   PL:
685. [Umiejętność wroga [835004] (ulepszenie 1) — nazwa] 퍼레이드의 왕자
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835004].levelList[level=1].name
   limit: do 40 znaków
   EN: The Parade's Prince
   PL:
686. [Umiejętność wroga [835004] (ulepszenie 1) — opis] [StartBattle] [Laceration]을 가진 대상만큼 가중치 증가 (최대 5)\n[WhenUse] 대상의 [Laceration]이 4 이상이면, 기본 위력 +1\n[WhenUse] 대상의 [Laceration] 횟수가 3 이상이면, 코인 위력 +1\n[DefeatDuel] [KeptBlood] 1 감소
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835004].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Laceration], [WhenUse], [DefeatDuel], [KeptBlood]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [KeptBlood] = 머금은 피 / Stored Blood
   EN: [StartBattle] Gain Atk Weight equal to the number of targets with [Laceration] (max 5)\n[WhenUse] If target has 4+ [Laceration], Base Power +1\n[WhenUse] If target has 3+ [Laceration] Count, Coin Power +1\n[DefeatDuel] Lose 1 [KeptBlood]
   PL:
687. [Umiejętność wroga [835004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Umiejętność wroga [835004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Umiejętność wroga [835004] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835004].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Umiejętność wroga [835004] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835004].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Umiejętność wroga [835005] (ulepszenie 1) — nazwa] 피... 피... 피...!
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835005].levelList[level=1].name
   limit: do 40 znaków
   EN: Blood... Blood... Blood...!
   PL:
692. [Umiejętność wroga [835005] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 8 이상이면, 코인 위력 +1\n[DefeatDuel] [KeptBlood] 1 감소
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835005].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [DefeatDuel], [KeptBlood]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [KeptBlood] = 머금은 피 / Stored Blood
   EN: [WhenUse] If target has 8+ [Laceration], Coin Power +1\n[DefeatDuel] Lose 1 [KeptBlood]
   PL:
693. [Umiejętność wroga [835005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +3 [Laceration] Count
   PL:
694. [Umiejętność wroga [835005] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration]이 10 이상이면, 다음 코인 피해량 +20%
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835005].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 10+ [Laceration], the next Coin deals +20% damage
   PL:
695. [Umiejętność wroga [835005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [KeptBlood] 1 얻음
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [KeptBlood]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KeptBlood] = 머금은 피 / Stored Blood
   EN: [OnSucceedAttack] Gain 1 [KeptBlood]
   PL:
696. [Umiejętność wroga [835005] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835005].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Umiejętność wroga [835006] (ulepszenie 1) — nazwa] 날 내버려둬...!
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835006].levelList[level=1].name
   limit: do 40 znaków
   EN: Leave Me Alone...!
   PL:
698. [Umiejętność wroga [835006] (ulepszenie 1) — opis] [WhenUseEvade] 대상의 [Laceration] 횟수당 기본 위력 +1 (최대 4)
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835006].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUseEvade], [Laceration]
   znaczenie tagów: [WhenUseEvade] = [회피 사용시] / [On Evade Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUseEvade] Base Power +1 for every [Laceration] Count on the target (max 4)
   PL:
699. [Umiejętność wroga [835007] (ulepszenie 1) — nazwa] 나는... 이 행진의... 왕자이다...!
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835007].levelList[level=1].name
   limit: do 60 znaków
   EN: I Am... The Prince... of the Parade...!
   PL:
700. [Umiejętność wroga [835007] (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] 경혈[TabExplain]식 글레이브의 회복 효과가 2배로 적용됨\n[WhenUse] 정신력이 0이 됨\n[EndSkill] [KeptBlood] 10 얻음\n이번 턴동안 흐트러짐 상태가 되지 않고 이 스킬 사용 후 턴 종료함.
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835007].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [TabExplain], [EndSkill], [KeptBlood]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]; [KeptBlood] = 머금은 피 / Stored Blood
   EN: [CantDuel]\n[WhenUse] Double the amount healed by Hardblood[TabExplain] Glaive\n[WhenUse] Reset SP to 0\n[EndSkill] Gain 10 [KeptBlood]\nDoes not get Staggered this turn; ends turn after using this Skill.
   PL:
701. [Umiejętność wroga [835007] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835007].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +1 [Laceration] Count
   PL:
702. [Umiejętność wroga [835007] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835007].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Umiejętność wroga [835007] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835007].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Umiejętność wroga [835007] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835007].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Umiejętność wroga [835008] (ulepszenie 1) — nazwa] 절대... 돌아가지 않아...!
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835008].levelList[level=1].name
   limit: do 50 znaków
   EN: I'm... Never... Going Back...!
   PL:
706. [Umiejętność wroga [835008] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 [Laceration] 5당, 합 위력 +1 (최대 3)\n[WhenUse] 메인 타겟의 [Laceration] 횟수 4 이상이면, 코인 위력 +1\n[WhenUse] 메인 타겟의 [Laceration] 횟수당, 피해량 +5% (최대 20%)\n[WhenUse] 경혈[TabExplain]식 글레이브의 회복 효과가 2배로 적용됨\n[EndSkill] [KeptBlood] 10 얻음
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835008].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [TabExplain], [EndSkill], [KeptBlood]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [KeptBlood] = 머금은 피 / Stored Blood
   EN: [WhenUse] Clash Power +1 for every 5 [Laceration] on the main target (max 3)\n[WhenUse] If the main target has 4+ [Laceration], Coin Power +1\n[WhenUse] Deal +5% damage for every [Laceration] on the main target (max 20%)\n[WhenUse] Double the amount healed by Hardblood[TabExplain] Glaive\n[EndSkill] Gain 10 [KeptBlood]
   PL:
707. [Umiejętność wroga [835008] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835008].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +1 [Laceration] Count
   PL:
708. [Umiejętność wroga [835008] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835008].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Umiejętność wroga [835008] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835008].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Umiejętność wroga [835008] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe.json :: dataList[id=835008].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [mowe] Umiejętności wrogów / Anomalii — Skills_Enemy-mowe
- grupa rozdziału/trybu: `mowe` · plik: `Skills_Enemy-mowe.json`

711. [Umiejętność wroga [9014501] (ulepszenie 1) — nazwa] 경화된 팔
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014501].levelList[level=1].name
   limit: do 40 znaków
   EN: Coagulated Arm
   PL:
712. [Umiejętność wroga [9014501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Umiejętność wroga [9014502] (ulepszenie 1) — nazwa] 경혈식 강화 찌르기
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014502].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Jag
   PL:
714. [Umiejętność wroga [9014502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Umiejętność wroga [9014502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Umiejętność wroga [9014503] (ulepszenie 1) — nazwa] 혈액 수집
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014503].levelList[level=1].name
   limit: do 40 znaków
   EN: Collecting Blood
   PL:
717. [Umiejętność wroga [9014503] (ulepszenie 1) — opis] 대상의 [Laceration]이 10 이상이면, 피해량 +20%
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 10+ [Laceration], deal +20% damage
   PL:
718. [Umiejętność wroga [9014503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Umiejętność wroga [9014503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Umiejętność wroga [9014503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력을 최대 10까지 흡수하여 최대 체력의 (흡수한 [Laceration] 위력 x 2)%만큼 체력 회복 ([Laceration] 위력은 1 미만으로 감소하지 않음)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Absorb up to 10 [Laceration] Potency from the target and heal ([Laceration] Potency absorbed x 2)% HP (this effect does not lower the target's [Laceration] Potency under 1)
   PL:
721. [Umiejętność wroga [9014503] (ulepszenie 1) — moneta 3, efekt 1 — podsumowanie] [OnSucceedAttack] 대상의 [Laceration]을 흡수하여 체력 회복
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014503].levelList[level=1].coinlist[#2].coindescs[#0].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Absorb [Laceration] on target to heal
   PL:
722. [Umiejętność wroga [9014504] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014504].levelList[level=1].name
   limit: do 40 znaków
   EN: Counter
   PL:
723. [Umiejętność wroga [9014504] (ulepszenie 1) — opis] [WhenUse] 자신의 [Laceration] 횟수 3당, 기본 위력 +1 (최대 2)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Base Power +1 for every 3 [Laceration] Count on self (max 2)
   PL:
724. [Umiejętność wroga [9014504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Umiejętność wroga [9014601] (ulepszenie 1) — nazwa] 경화된 팔
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014601].levelList[level=1].name
   (powtórzenie elementu 711 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Umiejętność wroga [9014601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Umiejętność wroga [9014602] (ulepszenie 1) — nazwa] 경혈식 강화 베기
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014602].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Slice
   PL:
728. [Umiejętność wroga [9014602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Umiejętność wroga [9014602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Umiejętność wroga [9014603] (ulepszenie 1) — nazwa] 혈액 수집
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014603].levelList[level=1].name
   (powtórzenie elementu 716 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność wroga [9014603] (ulepszenie 1) — opis] 대상의 [Laceration]이 10 이상이면, 피해량 +20%
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014603].levelList[level=1].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Umiejętność wroga [9014603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Umiejętność wroga [9014603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Umiejętność wroga [9014603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력을 최대 10까지 흡수하여 최대 체력의 (흡수한 [Laceration] 위력 x 2)%만큼 체력 회복 ([Laceration] 위력은 1 미만으로 감소하지 않음)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 720 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Umiejętność wroga [9014603] (ulepszenie 1) — moneta 3, efekt 1 — podsumowanie] [OnSucceedAttack] 대상의 [Laceration]을 흡수하여 체력 회복
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014603].levelList[level=1].coinlist[#2].coindescs[#0].summary
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
736. [Umiejętność wroga [9014604] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014604].levelList[level=1].name
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Umiejętność wroga [9014604] (ulepszenie 1) — opis] [WhenUse] 자신의 [Laceration] 횟수 3당, 기본 위력 +1 (최대 2)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014604].levelList[level=1].desc
   (powtórzenie elementu 723 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [Umiejętność wroga [9014604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Umiejętność wroga [9014701] (ulepszenie 1) — nazwa] 경화된 팔
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014701].levelList[level=1].name
   (powtórzenie elementu 711 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
740. [Umiejętność wroga [9014701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
741. [Umiejętność wroga [9014701] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014701].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Umiejętność wroga [9014702] (ulepszenie 1) — nazwa] 경혈식 강화 타격
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014702].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Strike
   PL:
743. [Umiejętność wroga [9014702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [Umiejętność wroga [9014702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Umiejętność wroga [9014703] (ulepszenie 1) — nazwa] 혈액 수집
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014703].levelList[level=1].name
   (powtórzenie elementu 716 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
746. [Umiejętność wroga [9014703] (ulepszenie 1) — opis] 대상의 [Laceration]이 10 이상이면, 피해량 +20%
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014703].levelList[level=1].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Umiejętność wroga [9014703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
748. [Umiejętność wroga [9014703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [Umiejętność wroga [9014703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력을 최대 10까지 흡수하여 최대 체력의 (흡수한 [Laceration] 위력 x 2)%만큼 체력 회복 ([Laceration] 위력은 1 미만으로 감소하지 않음)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 720 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [Umiejętność wroga [9014703] (ulepszenie 1) — moneta 3, efekt 1 — podsumowanie] [OnSucceedAttack] 대상의 [Laceration]을 흡수하여 체력 회복
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014703].levelList[level=1].coinlist[#2].coindescs[#0].summary
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Umiejętność wroga [9014704] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014704].levelList[level=1].name
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [Umiejętność wroga [9014704] (ulepszenie 1) — opis] [WhenUse] 자신의 [Laceration] 횟수 3당, 기본 위력 +1 (최대 2)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014704].levelList[level=1].desc
   (powtórzenie elementu 723 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Umiejętność wroga [9014704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Umiejętność wroga [9014801] (ulepszenie 1) — nazwa] 절단
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014801].levelList[level=1].name
   limit: do 40 znaków
   EN: Rip
   PL:
755. [Umiejętność wroga [9014801] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +2 [Charge] Count
   PL:
756. [Umiejętność wroga [9014801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count
   PL:
757. [Umiejętność wroga [9014801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [Umiejętność wroga [9014802] (ulepszenie 1) — nazwa] 찍어내리기
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014802].levelList[level=1].name
   limit: do 40 znaków
   EN: Stab Down
   PL:
759. [Umiejętność wroga [9014802] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +5 [Charge] Count
   PL:
760. [Umiejętność wroga [9014802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 756 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Umiejętność wroga [9014802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Umiejętność wroga [9014802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 756 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Umiejętność wroga [9014802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Umiejętność wroga [9014803] (ulepszenie 1) — nazwa] 경혈식 무기 강화
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014803].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Weapon
   PL:
765. [Umiejętność wroga [9014803] (ulepszenie 1) — opis] [WhenUse] 보유한 [Charge] 횟수를 전부 소모하고, 최대 체력의 2 x (15 - 소모한 [Charge] 횟수)% 만큼 체력을 소모하여 코인 위력 +2
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014803].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume all [Charge] Count on self and consume 2(15 - [Charge] Count consumed)% HP to gain Coin Power +2
   PL:
766. [Umiejętność wroga [9014803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]
   PL:
767. [Umiejętność wroga [9014803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 6 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 6 [DefenseDown]
   PL:
768. [Umiejętność wroga [9014803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력을 최대 10까지 흡수하여 최대 체력의 (흡수한 [Laceration] 위력 x 2)%만큼 체력 회복 ([Laceration] 위력은 1 미만으로 감소하지 않음)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 720 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Umiejętność wroga [9014803] (ulepszenie 1) — moneta 2, efekt 2 — podsumowanie] [OnSucceedAttack] 대상의 [Laceration]을 흡수하여 체력 회복
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014803].levelList[level=1].coinlist[#1].coindescs[#1].summary
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Umiejętność wroga [9014804] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014804].levelList[level=1].name
   limit: do 40 znaków
   EN: Guard
   PL:
771. [Umiejętność wroga [9014804] (ulepszenie 1) — opis] [WhenUse] 자신의 [Laceration] 횟수 3당, 기본 위력 +1 (최대 2)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014804].levelList[level=1].desc
   (powtórzenie elementu 723 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [Umiejętność wroga [9014901] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014901].levelList[level=1].name
   limit: do 40 znaków
   EN: Thrust
   PL:
773. [Umiejętność wroga [9014901] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014901].levelList[level=1].desc
   (powtórzenie elementu 755 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Umiejętność wroga [9014901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 756 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Umiejętność wroga [9014901] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014901].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [Umiejętność wroga [9014902] (ulepszenie 1) — nazwa] 베어가르기
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014902].levelList[level=1].name
   limit: do 40 znaków
   EN: Cleave
   PL:
777. [Umiejętność wroga [9014902] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014902].levelList[level=1].desc
   (powtórzenie elementu 759 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Umiejętność wroga [9014902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 756 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Umiejętność wroga [9014902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [Umiejętność wroga [9014902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 756 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Umiejętność wroga [9014902] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Umiejętność wroga [9014903] (ulepszenie 1) — nazwa] 경혈식 무기 강화
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014903].levelList[level=1].name
   (powtórzenie elementu 764 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Umiejętność wroga [9014903] (ulepszenie 1) — opis] [WhenUse] 보유한 [Charge] 횟수를 전부 소모하고, 최대 체력의 2 x (15 - 소모한 [Charge] 횟수)% 만큼 체력을 소모하여 코인 위력 +2
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014903].levelList[level=1].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Umiejętność wroga [9014903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 766 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Umiejętność wroga [9014903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable]
   PL:
786. [Umiejętność wroga [9014903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력을 최대 10까지 흡수하여 최대 체력의 (흡수한 [Laceration] 위력 x 2)%만큼 체력 회복 ([Laceration] 위력은 1 미만으로 감소하지 않음)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 720 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Umiejętność wroga [9014903] (ulepszenie 1) — moneta 2, efekt 1 — podsumowanie] [OnSucceedAttack] 대상의 [Laceration]을 흡수하여 체력 회복
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014903].levelList[level=1].coinlist[#1].coindescs[#0].summary
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [Umiejętność wroga [9014904] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014904].levelList[level=1].name
   limit: do 40 znaków
   EN: Evade
   PL:
789. [Umiejętność wroga [9014904] (ulepszenie 1) — opis] [WhenUse] 자신의 [Laceration] 횟수 3당, 기본 위력 +1 (최대 2)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9014904].levelList[level=1].desc
   (powtórzenie elementu 723 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Umiejętność wroga [9015001] (ulepszenie 1) — nazwa] 창 휘두르기
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015001].levelList[level=1].name
   limit: do 40 znaków
   EN: Spear Swing
   PL:
791. [Umiejętność wroga [9015001] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015001].levelList[level=1].desc
   (powtórzenie elementu 755 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Umiejętność wroga [9015001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 756 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Umiejętność wroga [9015001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [Umiejętność wroga [9015001] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015001].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Umiejętność wroga [9015002] (ulepszenie 1) — nazwa] 상처 헤집기
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015002].levelList[level=1].name
   limit: do 40 znaków
   EN: Tear Up Wound
   PL:
796. [Umiejętność wroga [9015002] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015002].levelList[level=1].desc
   (powtórzenie elementu 759 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Umiejętność wroga [9015002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 756 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Umiejętność wroga [9015002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL:
799. [Umiejętność wroga [9015002] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015002].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Umiejętność wroga [9015002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 756 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Umiejętność wroga [9015002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Umiejętność wroga [9015002] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015002].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Umiejętność wroga [9015003] (ulepszenie 1) — nazwa] 경혈식 무기 강화
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015003].levelList[level=1].name
   (powtórzenie elementu 764 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Umiejętność wroga [9015003] (ulepszenie 1) — opis] [WhenUse] 보유한 [Charge] 횟수를 전부 소모하고, 최대 체력의 2 x (15 - 소모한 [Charge] 횟수)% 만큼 체력을 소모하여 코인 위력 +2
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015003].levelList[level=1].desc
   (powtórzenie elementu 765 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Umiejętność wroga [9015003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 766 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [Umiejętność wroga [9015003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Umiejętność wroga [9015003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [AttackDown] 3 부여.
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 3 [AttackDown]
   PL:
808. [Umiejętność wroga [9015003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력을 최대 10까지 흡수하여 최대 체력의 (흡수한 [Laceration] 위력 x 2)%만큼 체력 회복 ([Laceration] 위력은 1 미만으로 감소하지 않음)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 720 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Umiejętność wroga [9015003] (ulepszenie 1) — moneta 2, efekt 2 — podsumowanie] [OnSucceedAttack] 대상의 [Laceration]을 흡수하여 체력 회복
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015003].levelList[level=1].coinlist[#1].coindescs[#1].summary
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Umiejętność wroga [9015004] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015004].levelList[level=1].name
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Umiejętność wroga [9015004] (ulepszenie 1) — opis] [WhenUse] 자신의 [Laceration] 횟수 3당, 기본 위력 +1 (최대 2)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015004].levelList[level=1].desc
   (powtórzenie elementu 723 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
812. [Umiejętność wroga [9015101] (ulepszenie 1) — nazwa] 의체 가동
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015101].levelList[level=1].name
   limit: do 40 znaków
   EN: Activate Prosthesis
   PL:
813. [Umiejętność wroga [9015101] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 10 이상이면, [Charge] 횟수를 5 소모하여 [AttackUp] 3을 얻음
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge], [AttackUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [WhenUse] At 10+ [Charge] Count, consume 5 [Charge] Count to gain 3 [AttackUp]
   PL:
814. [Umiejętność wroga [9015101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Umiejętność wroga [9015102] (ulepszenie 1) — nazwa] 작살 표식
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015102].levelList[level=1].name
   limit: do 40 znaków
   EN: Harpoon Mark
   PL:
816. [Umiejętność wroga [9015102] (ulepszenie 1) — opis] [StartBattle] 자신의 [Charge] 횟수가 5 미만이면, 자신의 [Charge] 횟수 5, [Laceration] 횟수 3 증가하고, [Vulnerable] 1을 얻음\n[WhenUse] [Charge] 횟수가 10 이상이면, [Charge] 횟수를 5 소모하여 [AttackUp] 3을 얻음
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015102].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Charge], [Laceration], [Vulnerable], [WhenUse], [AttackUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Charge] = 충전 / Charge; [Laceration] = 출혈 / Bleed; [Vulnerable] = 취약 / Fragile; [WhenUse] = [사용시] / [On Use]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [StartBattle] At 5- [Charge] Count, gain 5 [Charge] Count, 3 [Laceration] Count, and 1 [Vulnerable]\n[WhenUse] At 10+ [Charge] Count, consume 5 [Charge] Count to gain 3 [AttackUp]
   PL:
817. [Umiejętność wroga [9015102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Umiejętność wroga [9015102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Umiejętność wroga [9015102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 267 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [Umiejętność wroga [9015103] (ulepszenie 1) — nazwa] 경혈식 강화 작살
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015103].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Harpoon
   PL:
821. [Umiejętność wroga [9015103] (ulepszenie 1) — opis] [WhenUse] 자신의 체력을 최대 체력의 10% 만큼 소모하여 [Charge] 횟수 10 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015103].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 10% HP on self to gain +10 [Charge] Count
   PL:
822. [Umiejętność wroga [9015103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [Umiejętność wroga [9015103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여.
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]
   PL:
824. [Umiejętność wroga [9015103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가.
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count.
   PL:
825. [Umiejętność wroga [9015103] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015103].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis]
   PL:
826. [Umiejętność wroga [9015104] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015104].levelList[level=1].name
   (powtórzenie elementu 722 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Umiejętność wroga [9015104] (ulepszenie 1) — opis] [WhenUse] 자신의 [Laceration] 횟수 3당, 기본 위력 +1 (최대 2)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9015104].levelList[level=1].desc
   (powtórzenie elementu 723 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [Umiejętność wroga [9101801] (ulepszenie 1) — nazwa] 의체 가동
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101801].levelList[level=1].name
   (powtórzenie elementu 812 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Umiejętność wroga [9101801] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 10 이상이면, [Charge] 횟수 3을 소모하여 코인 위력 +1\n[WhenUse] [Charge] 횟수가 15 이상이면, [Charge] 횟수 3을 추가로 소모하여 피해량 + 20%\n[WhenUse] [Charge] 횟수가 5 미만이면, 최대 체력의 10%만큼 체력이 감소하고 [Charge] 횟수 5 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101801].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 10+ [Charge] Count, consume 3 [Charge] Count to gain Coin Power +1\n[WhenUse] At 15+ [Charge] Count, consume 3 additional [Charge] Count to deal +20% damage\n[WhenUse] At 5- [Charge] Count, lose 10% HP and gain +5 [Charge] Count
   PL:
830. [Umiejętność wroga [9101801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Umiejętność wroga [9101801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [Umiejętność wroga [9101802] (ulepszenie 1) — nazwa] 경혈식 혈액 역류
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101802].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Reflux
   PL:
833. [Umiejętność wroga [9101802] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 10 이상이면, [Charge] 횟수 3을 소모하여 코인 위력 +1\n[WhenUse] [Charge] 횟수가 15 이상이면, [Charge] 횟수 3을 추가로 소모하여 피해량 + 20%\n[WhenUse] [Charge] 횟수가 5 미만이면, 최대 체력의 10%만큼 체력이 감소하고 [Charge] 횟수 5 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101802].levelList[level=1].desc
   (powtórzenie elementu 829 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Umiejętność wroga [9101802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
835. [Umiejętność wroga [9101802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 825 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [Umiejętność wroga [9101802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Umiejętność wroga [9101802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Umiejętność wroga [9101802] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Umiejętność wroga [9101802] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101802].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Umiejętność wroga [9101803] (ulepszenie 1) — nazwa] 생체 에너지 전환식 충전
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101803].levelList[level=1].name
   limit: do 40 znaków
   EN: Bioenergy Conversion Charge
   PL:
841. [Umiejętność wroga [9101803] (ulepszenie 1) — opis] [WhenUse] 자신의 체력을 최대 체력의 10% 만큼 소모하여 [Charge] 횟수 15 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101803].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 10% HP on self to gain +15 [Charge] Count
   PL:
842. [Umiejętność wroga [9101803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Umiejętność wroga [9101803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Umiejętność wroga [9101803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 766 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Umiejętność wroga [9101803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
846. [Umiejętność wroga [9101803] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [AttackDown] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101803].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 2 [AttackDown]
   PL:
847. [Umiejętność wroga [9101804] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101804].levelList[level=1].name
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Umiejętność wroga [9101804] (ulepszenie 1) — opis] [WhenUse] 자신의 [Laceration] 횟수 3당, 기본 위력 +1 (최대 2)
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101804].levelList[level=1].desc
   (powtórzenie elementu 723 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Umiejętność wroga [9101805] (ulepszenie 1) — nazwa] 경혈식 혈액 이전
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101805].levelList[level=1].name
   limit: do 40 znaków
   EN: Hardblood Transfusion
   PL:
850. [Umiejętność wroga [9101805] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 10 이상이면, [Charge] 횟수 3을 소모하여 코인 위력 +1\n[WhenUse] [Charge] 횟수가 15 이상이면, [Charge] 횟수 3을 추가로 소모하여 피해량 + 20%\n[WhenUse] [Charge] 횟수가 5 미만이면, 최대 체력의 10%만큼 체력이 감소하고 [Charge] 횟수 5 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101805].levelList[level=1].desc
   (powtórzenie elementu 829 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Umiejętność wroga [9101805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
852. [Umiejętność wroga [9101805] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101805].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Umiejętność wroga [9101805] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101805].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [Umiejętność wroga [9101806] (ulepszenie 1) — nazwa] 생체 에너지 전환식 재충전
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101806].levelList[level=1].name
   limit: do 50 znaków
   EN: Bioenergy Conversion Recharge
   PL:
855. [Umiejętność wroga [9101806] (ulepszenie 1) — opis] [WhenUse] 자신의 체력을 최대 체력의 10% 만큼 소모하여 [Charge] 횟수 15 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101806].levelList[level=1].desc
   (powtórzenie elementu 841 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
856. [Umiejętność wroga [9101806] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101806].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Umiejętność wroga [9101806] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101806].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable]
   PL:
858. [Umiejętność wroga [9101806] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101806].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Umiejętność wroga [9101806] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101806].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [Umiejętność wroga [9101806] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101806].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 766 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Umiejętność wroga [9101806] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101806].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
862. [Umiejętność wroga [9101806] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [AttackDown] 2 부여
   źródło: Skills_Enemy-mowe.json :: dataList[id=9101806].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [mowe] Pasywka wroga: Passives_Abnormality-mowe
- plik gry: `Passives_Abnormality-mowe.json`

863. [[mowe] Pasywka wroga [835001] — nazwa] 머금은 피
   źródło: Passives_Abnormality-mowe.json :: dataList[id=835001].name
   limit: do 40 znaków
   EN: Stored Blood
   PL:
864. [[mowe] Pasywka wroga [835001] — opis] 턴 종료 시 [KeptBlood] 수치에 따라\n- 5 이하라면, 매 턴마다 (6 - 수치)만큼 다음 턴에 [Binding] 1, [Vulnerable] 1, [AttackDown] 1씩 얻음\n- 5 초과라면, 매 턴마다 (수치 - 5)만큼 다음 턴에 [AttackUp] 2, [DefenseUp] 2씩 얻음
   źródło: Passives_Abnormality-mowe.json :: dataList[id=835001].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [KeptBlood], [Binding], [Vulnerable], [AttackDown], [AttackUp], [DefenseUp]
   znaczenie tagów: [KeptBlood] = 머금은 피 / Stored Blood; [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: At Turn End, depending on the [KeptBlood] Stack on self:\n- At 5 or fewer Stack: gain 1 [Binding], 1 [Vulnerable], and 1 [AttackDown] next turn for every (6 - Stack)\n- At more than 5 Stack: gain 2 [AttackUp] and 2 [DefenseUp] next turn for every (Stack - 5)
   PL:
865. [[mowe] Pasywka wroga [835002] — nazwa] 피가 떨어져서는 안 돼
   źródło: Passives_Abnormality-mowe.json :: dataList[id=835002].name
   limit: do 40 znaków
   EN: Must Retain Blood
   PL:
866. [[mowe] Pasywka wroga [835002] — opis] [KeptBlood]가 처음으로 0이 되었을 때 패턴 변경\n나는... 이 행진의... 왕자이다...!를 사용할 때, 속도가 10으로 고정됨
   źródło: Passives_Abnormality-mowe.json :: dataList[id=835002].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [KeptBlood]
   znaczenie tagów: [KeptBlood] = 머금은 피 / Stored Blood
   EN: Gains a new pattern when [KeptBlood] reaches 0 for the first time\nFix this unit's speed to 10 when using the Skill 'I Am... The Prince... of the Parade...!'
   PL:
867. [[mowe] Pasywka wroga [835003] — nazwa] 왕자의 발악
   źródło: Passives_Abnormality-mowe.json :: dataList[id=835003].name
   limit: do 40 znaków
   EN: The Prince's Frenzy
   PL:
868. [[mowe] Pasywka wroga [835003] — opis] 현재 체력이 최대 체력의 30%가 되었을 때, [BloodyCrave]를 얻음
   źródło: Passives_Abnormality-mowe.json :: dataList[id=835003].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BloodyCrave]
   znaczenie tagów: [BloodyCrave] = 핏빛 갈구 / Bloodtinged Craving
   EN: When this unit reaches 30% HP, gain [BloodyCrave]
   PL:
869. [[mowe] Pasywka wroga [835004] — nazwa] 경혈식 글레이브
   źródło: Passives_Abnormality-mowe.json :: dataList[id=835004].name
   limit: do 40 znaków
   EN: Hardblood Glaive
   PL:
870. [[mowe] Pasywka wroga [835004] — opis] [Laceration] 위력과 횟수의 합이 가장 높은 대상 우선 공격\n공격 적중시 대상에게 [Laceration]이 있으면, 최대 체력의 2%만큼 체력 회복
   źródło: Passives_Abnormality-mowe.json :: dataList[id=835004].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Prioritizes targets with the highest sum of [Laceration] Potency and Count\nOn Hit, if the target has [Laceration], heal 2% HP
   PL:
871. [[mowe] Pasywka wroga [835005] — nazwa] 혈식 - 경화
   źródło: Passives_Abnormality-mowe.json :: dataList[id=835005].name
   limit: do 40 znaków
   EN: Sanguivore - Coagulation
   PL:
872. [[mowe] Pasywka wroga [835005] — opis] 자신에게 [Laceration]이 있을 때,\n- [Laceration] 5당 공격 레벨 증가 1, 방어 레벨 증가 1을 얻음 (최대 10)\n- [Laceration] 10당 합 위력 증가 1을 얻음 (최대 5)\n- 자신이 받는 [Laceration] 피해 50% 감소 (소수점 버림)
   źródło: Passives_Abnormality-mowe.json :: dataList[id=835005].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: When this unit has [Laceration]:\n- Gain 1 Offense Level Up and 1 Defense Level Up for every 5 [Laceration] (max 10)\n- Gain 1 Clash Power Up for every 10 [Laceration] (max 5)\n- Damage taken from [Laceration] -50% (rounded down)
   PL:
873. [[mowe] Pasywka wroga [9014501] — nazwa] 혈액 경화
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9014501].name
   limit: do 40 znaków
   EN: Blood Coagulation
   PL:
874. [[mowe] Pasywka wroga [9014501] — opis] 자신이 피격당할 때마다 [Laceration] 횟수 1 을 얻음\n턴 종료 시, 자신의 [Laceration] 횟수를 3 소모하여 [HardenedBlood] 1 얻음
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9014501].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [HardenedBlood]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [HardenedBlood] = 경화 혈액 / Coagulated Blood
   EN: Gain +1 [Laceration] Count every time this unit is hit\nTurn End: consume 3 [Laceration] Count on self to gain 1 [HardenedBlood]
   PL:
875. [[mowe] Pasywka wroga [9014502] — nazwa] 피의 갈증
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9014502].name
   limit: do 40 znaków
   EN: Thirst for Blood
   PL:
876. [[mowe] Pasywka wroga [9014502] — opis] [Laceration]이 부여된 대상을 우선적으로 공격\n턴 종료 시 이번 턴에 피해를 주지 못한 경우, 다음 턴에 [Vulnerable] 2, [AttackUp] 2를 얻음
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9014502].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Vulnerable], [AttackUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Vulnerable] = 취약 / Fragile; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Prioritizes targets with [Laceration]\nTurn End: if this unit failed to deal any damage this turn, gain 2 [Vulnerable] and 2 [AttackUp] next turn
   PL:
877. [[mowe] Pasywka wroga [9014503] — nazwa] 흡혈
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9014503].name
   limit: do 40 znaków
   EN: Bloodsucking
   PL:
878. [[mowe] Pasywka wroga [9014503] — opis] 자신이 받는 [Laceration] 피해 10% 감소 (소수점 버림)\n공격 적중시 대상에게 [Laceration]이 있으면, 피해량의 10%만큼 체력 회복
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9014503].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Damage taken from [Laceration] -10% (rounded down)\nOn Hit, if the target has [Laceration], heal 10% of the damage dealt
   PL:
879. [[mowe] Pasywka wroga [9014801] — nazwa] 억센 흡혈
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9014801].name
   limit: do 40 znaków
   EN: Rough Bloodsucking
   PL:
880. [[mowe] Pasywka wroga [9014801] — opis] 자신이 받는 [Laceration] 피해 20% 감소 (소수점 버림)\n공격 적중시 대상에게 [Laceration]이 있으면, 피해량의 15%만큼 체력 회복
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9014801].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Damage taken from [Laceration] -20% (rounded down)\nOn Hit, if the target has [Laceration], heal 15% of the damage dealt
   PL:
881. [[mowe] Pasywka wroga [9014802] — nazwa] 누전
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9014802].name
   limit: do 40 znaków
   EN: Power Leakage
   PL:
882. [[mowe] Pasywka wroga [9014802] — opis] 자신이 피격당할 때마다 공격자가 [Charge]을 얻는 스킬을 사용했으면, [Charge] 횟수 1을 공격자에게 옮긴다. \n(스킬 당 1회, 피격자가 [Charge]이 없으면 발동하지 않음)
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9014802].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Every time this unit is hit, if the attacker used a Skill that gains [Charge], the attacker steals 1 [Charge] Count from this unit.\n(Once per Skill. Does not activate if this unit does not have [Charge])
   PL:
883. [[mowe] Pasywka wroga [9015101] — nazwa] 피를 뇌로 보내기
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9015101].name
   limit: do 40 znaków
   EN: Blood to Brain
   PL:
884. [[mowe] Pasywka wroga [9015101] — opis] 자신이 받는 [Laceration] 피해 30% 감소 (소수점 버림)\n공격 적중시 대상에게 [Laceration]이 있으면, 피해량의 15%만큼 체력 회복
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9015101].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Damage taken from [Laceration] -30% (rounded down)\nOn Hit, if the target has [Laceration], heal 15% of the damage dealt
   PL:
885. [[mowe] Pasywka wroga [9015102] — nazwa] 의체 모델 - L37
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9015102].name
   limit: do 40 znaków
   EN: Prosthesis Model - L37
   PL:
886. [[mowe] Pasywka wroga [9015102] — opis] 턴 시작 시 [Charge] 횟수가 5 미만이면 자신에게 [Reduction] 1 부여\n턴 시작 시 [Charge] 횟수가 5 이상이면 [ParryingResultUp] 2 얻음
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9015102].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [Reduction], [ParryingResultUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [Reduction] = 공격 위력 감소 / Attack Power Down; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Turn Start: At less than 5 [Charge] Count, gain 1 [Reduction]\nTurn Start: At 5+ [Charge] Count, gain 2 [ParryingResultUp]
   PL:
887. [[mowe] Pasywka wroga [9015201] — nazwa] 어린 권속
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9015201].name
   limit: do 40 znaków
   EN: A Young Kindred
   PL:
888. [[mowe] Pasywka wroga [9015201] — opis] 자신이 받는 [Laceration] 피해 30% 감소 (소수점 버림)\n공격 적중시 대상에게 [Laceration]이 있으면, 피해량의 25%만큼 체력 회복
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9015201].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Damage taken from [Laceration] -30% (rounded down)\nOn Hit, if the target has [Laceration], heal 25% of the damage dealt
   PL:
889. [[mowe] Pasywka wroga [9014803] — nazwa] 끈질김
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9014803].name
   limit: do 40 znaków
   EN: Tenacious
   PL:
890. [[mowe] Pasywka wroga [9014803] — opis] 자신의 스킬로 인해 받는 피해로 체력이 1 미만으로 감소하지 않음
   źródło: Passives_Abnormality-mowe.json :: dataList[id=9014803].desc
   limit: do 120 znaków
   EN: Self-inflicted damage due to this unit's Skills does not reduce this unit's HP under 1
   PL:
891. [[mowe] Pasywka wroga [834801] — nazwa] 터진 피주머니
   źródło: Passives_Abnormality-mowe.json :: dataList[id=834801].name
   limit: do 40 znaków
   EN: Burst Bloodbag
   PL:
892. [[mowe] Pasywka wroga [834801] — opis] 전투 시작시 체력이 전체 체력의 절반인 상태로 전투함
   źródło: Passives_Abnormality-mowe.json :: dataList[id=834801].desc
   limit: do 120 znaków
   EN: Combat Start: starts the Encounter only with half of max HP
   PL:
893. [[mowe] Pasywka wroga [834802] — nazwa] 제 7의 권속
   źródło: Passives_Abnormality-mowe.json :: dataList[id=834802].name
   limit: do 40 znaków
   EN: The Seventh Kindred
   PL:
894. [[mowe] Pasywka wroga [834802] — opis] 체력 1이 된 아군 수에 따라, 슬롯 +1 (최대 2회)
   źródło: Passives_Abnormality-mowe.json :: dataList[id=834802].desc
   limit: do 120 znaków
   EN: Gain +1 Slot for every ally at 1 HP (2 times max)
   PL:

## [mowe-re] Umiejętności wrogów / Anomalii — Skills_Abnormality-mowe-re
- grupa rozdziału/trybu: `mowe-re` · plik: `Skills_Abnormality-mowe-re.json`

895. [Umiejętność wroga [130501] (ulepszenie 1) — nazwa] 의체 가동
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130501].levelList[level=1].name
   (powtórzenie elementu 812 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
896. [Umiejętność wroga [130501] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 10 이상이면, [Charge] 횟수 3을 소모하여 코인 위력 +1\n[WhenUse] [Charge] 횟수가 15 이상이면, [Charge] 횟수 3을 추가로 소모하여 피해량 + 20%\n[WhenUse] [Charge] 횟수가 5 미만이면, 최대 체력의 10%만큼 체력이 감소하고 [Charge] 횟수 9 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130501].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 10+ [Charge] Count, consume 3 [Charge] Count to gain Coin Power +1\n[WhenUse] At 15+ [Charge] Count, consume 3 additional [Charge] Count to deal +20% damage\n[WhenUse] At less than 5 [Charge] Count, lose 10% HP and gain +9 [Charge] Count
   PL:
897. [Umiejętność wroga [130501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Umiejętność wroga [130501] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130501].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [Umiejętność wroga [130502] (ulepszenie 1) — nazwa] 경혈식 혈액 역류
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130502].levelList[level=1].name
   (powtórzenie elementu 832 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
900. [Umiejętność wroga [130502] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 10 이상이면, [Charge] 횟수 3을 소모하여 코인 위력 +1\n[WhenUse] [Charge] 횟수가 15 이상이면, [Charge] 횟수 3을 추가로 소모하여 피해량 + 20%\n[WhenUse] [Charge] 횟수가 5 미만이면, 최대 체력의 10%만큼 체력이 감소하고 [Charge] 횟수 9 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130502].levelList[level=1].desc
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
901. [Umiejętność wroga [130502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [Umiejętność wroga [130502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 825 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
903. [Umiejętność wroga [130502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
904. [Umiejętność wroga [130502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [Umiejętność wroga [130502] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
906. [Umiejętność wroga [130502] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130502].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [Umiejętność wroga [130503] (ulepszenie 1) — nazwa] 생체 에너지 전환식 충전
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130503].levelList[level=1].name
   (powtórzenie elementu 840 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Umiejętność wroga [130503] (ulepszenie 1) — opis] [WhenUse] 자신의 체력을 최대 체력의 10% 만큼 소모하여 [Charge] 횟수 15 증가\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130503].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Consume 10% HP on self to gain +15 [Charge] Count\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL:
909. [Umiejętność wroga [130503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Umiejętność wroga [130503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
911. [Umiejętność wroga [130503] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130503].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 208 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [Umiejętność wroga [130503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
913. [Umiejętność wroga [130503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 6 [Laceration]
   PL:
914. [Umiejętność wroga [130503] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130503].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
915. [Umiejętność wroga [130503] (ulepszenie 1) — moneta 2, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [AttackDown] 2 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130503].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [AttackDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [AttackDown]
   PL:
916. [Umiejętność wroga [130504] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130504].levelList[level=1].name
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
917. [Umiejętność wroga [130504] (ulepszenie 1) — opis] [WhenUse] 자신의 [Laceration] 횟수 3당, 기본 위력 +1 (최대 2)
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130504].levelList[level=1].desc
   (powtórzenie elementu 723 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
918. [Umiejętność wroga [130505] (ulepszenie 1) — nazwa] 경혈식 혈액 이전
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130505].levelList[level=1].name
   (powtórzenie elementu 849 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
919. [Umiejętność wroga [130505] (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 10 이상이면, [Charge] 횟수 3을 소모하여 코인 위력 +1\n[WhenUse] [Charge] 횟수가 15 이상이면, [Charge] 횟수 3을 추가로 소모하여 피해량 + 20%\n[WhenUse] [Charge] 횟수가 5 미만이면, 최대 체력의 10%만큼 체력이 감소하고 [Charge] 횟수 9 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130505].levelList[level=1].desc
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
920. [Umiejętność wroga [130505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
921. [Umiejętność wroga [130505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [Umiejętność wroga [130505] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130505].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
923. [Umiejętność wroga [130506] (ulepszenie 1) — nazwa] 생체 에너지 전환식 재충전
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130506].levelList[level=1].name
   (powtórzenie elementu 854 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
924. [Umiejętność wroga [130506] (ulepszenie 1) — opis] [WhenUse] 자신의 체력을 최대 체력의 10% 만큼 소모하여 [Charge] 횟수 15 증가\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130506].levelList[level=1].desc
   (powtórzenie elementu 908 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
925. [Umiejętność wroga [130506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [Umiejętność wroga [130506] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130506].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
927. [Umiejętność wroga [130506] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130506].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Vulnerable]
   PL:
928. [Umiejętność wroga [130506] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130506].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
929. [Umiejętność wroga [130506] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130506].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
930. [Umiejętność wroga [130506] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가.
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130506].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
931. [Umiejętność wroga [130506] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130506].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
932. [Umiejętność wroga [130506] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130506].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 913 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
933. [Umiejętność wroga [130506] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 2 증가.
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130506].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
934. [Umiejętność wroga [130506] (ulepszenie 1) — moneta 3, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [AttackDown] 2 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=130506].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 915 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
935. [Umiejętność wroga [123804] (ulepszenie 1) — nazwa] 퍼레이드의 왕자
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123804].levelList[level=1].name
   (powtórzenie elementu 685 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
936. [Umiejętność wroga [123804] (ulepszenie 1) — opis] [StartBattle] [Laceration]을 가진 대상만큼 가중치 증가 (최대 5)\n[WhenUse] 메인 타겟의 [Laceration]이 4 이상이면, 기본 위력 +1\n[WhenUse] 메인 타겟의 [Laceration] 횟수가 3 이상이면, 코인 위력 +1\n[DefeatDuel] [KeptBlood] 1 감소
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123804].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Laceration], [WhenUse], [DefeatDuel], [KeptBlood]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [KeptBlood] = 머금은 피 / Stored Blood
   EN: [StartBattle] Gain Atk Weight equal to the number of targets with [Laceration] (max 5)\n[WhenUse] If the main target has 4+ [Laceration], Base Power +1\n[WhenUse] If the main target has 3+ [Laceration] Count, Coin Power +1\n[DefeatDuel] Lose 1 [KeptBlood]
   PL:
937. [Umiejętność wroga [123804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
938. [Umiejętność wroga [123804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
939. [Umiejętność wroga [123804] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123804].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
940. [Umiejętność wroga [123804] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123804].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
941. [Umiejętność wroga [123804] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [KeptBlood] 1 얻음
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123804].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 695 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
942. [Umiejętność wroga [123807] (ulepszenie 1) — nazwa] 나는... 이 행진의... 왕자이다...!
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123807].levelList[level=1].name
   (powtórzenie elementu 699 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
943. [Umiejętność wroga [123807] (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] [Paralysis] 4 얻음\n[WhenUse] <noparse>경혈식 글레이브</noparse>의 회복 효과가 2배로 적용됨\n[WhenUse] 정신력이 0이 됨\n[EndSkill] [KeptBlood] 10 얻음\n이번 턴 동안 흐트러짐 상태가 되지 않고 이 스킬 사용 후 턴 종료함
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123807].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [CantDuel], [WhenUse], [Paralysis], [EndSkill], [KeptBlood], [TabExplain]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Paralysis] = 마비 / Paralyze; [EndSkill] = [공격 종료시] / [Attack End]; [KeptBlood] = 머금은 피 / Stored Blood
   EN: [CantDuel]\n[WhenUse] Gain 4 [Paralysis]\n[WhenUse] Double Hardblood[TabExplain] Glaive's heal effect\n[WhenUse] Reset SP to 0\n[EndSkill] Gain [KeptBlood] 10\nDoes not get Staggered this turn; ends turn after using this Skill.
   PL:
944. [Umiejętność wroga [123807] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123807].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [Umiejętność wroga [123807] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123807].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
946. [Umiejętność wroga [123807] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123807].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
947. [Umiejętność wroga [123807] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123807].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
948. [Umiejętność wroga [123808] (ulepszenie 1) — nazwa] 절대... 돌아가지 않아...!
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123808].levelList[level=1].name
   (powtórzenie elementu 705 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
949. [Umiejętność wroga [123808] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 [Laceration] 5당, 합 위력 +1 (최대 3)\n[WhenUse] 메인 타겟의 [Laceration] 횟수 4 이상이면, 코인 위력 +1\n[WhenUse] 메인 타겟의 [Laceration] 횟수당, 피해량 +5% (최대 20%)\n[WinDuel] <noparse>경혈식 글레이브</noparse>의 회복 효과가 2배로 적용됨\n[DefeatDuel] <noparse>경혈식 글레이브</noparse>의 회복 효과가 발동하지 않음\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] [KeptBlood] 10 얻음
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123808].levelList[level=1].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [WhenUse], [Laceration], [WinDuel], [DefeatDuel], [EndSkill], [KeptBlood], [TabExplain]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [KeptBlood] = 머금은 피 / Stored Blood
   EN: [WhenUse] Clash Power +1 for every 5 [Laceration] on the main target (max 3)\n[WhenUse] At 4+ [Laceration] Count on the main target, Coin Power +1\n[WhenUse] Deal +5% damage for every [Laceration] Count on the main target (max 20%)\n[WinDuel] Double Hardblood[TabExplain] Glaive's heal effect\n[DefeatDuel] Hardblood[TabExplain] Glaive's heal effect does not activate\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] Gain [KeptBlood] 10
   PL:
950. [Umiejętność wroga [123808] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123808].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
951. [Umiejętność wroga [123808] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123808].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
952. [Umiejętność wroga [123808] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123808].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
953. [Umiejętność wroga [123808] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123808].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
954. [Umiejętność wroga [123808] (ulepszenie 1) — moneta 4, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-mowe-re.json :: dataList[id=123808].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration] and +1 [Laceration] Count
   PL:

## [mowe-re] Pasywka wroga: Passives_Abnormality-mowe-re
- plik gry: `Passives_Abnormality-mowe-re.json`

955. [[mowe-re] Pasywka wroga [123806] — nazwa] 라만차랜드의 악몽
   źródło: Passives_Abnormality-mowe-re.json :: dataList[id=123806].name
   limit: do 40 znaków
   EN: Nightmare of La Manchaland
   PL:
956. [[mowe-re] Pasywka wroga [123806] — opis] 적 중 라만차랜드 소속 혈귀가 있으면, 아래 효과 얻음\n- 라만차랜드 소속 혈귀와 합 진행 시, 합 위력 4 감소\n- 라만차랜드 소속 혈귀에게 공격 시, 정신력 5 감소 (스킬당 최대 1회. 턴당 최대 2회)\n- 라만차랜드 소속 혈귀에게 스킬로 가하는 피해량 20% 감소
   źródło: Passives_Abnormality-mowe-re.json :: dataList[id=123806].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If there are La Manchaland Bloodfiends among the enemies, gain the following effects:\n- In a Clash against La Manchaland Bloodfiends, lose 4 Clash Power\n- When attacking La Manchaland Bloodfiends, lose 5 SP (once per Skill; 2 times per turn)\n- Deal -20% Skill damage against La Manchaland Bloodfiends
   PL:
957. [[mowe-re] Pasywka wroga [123801] — nazwa] 머금은 피
   źródło: Passives_Abnormality-mowe-re.json :: dataList[id=123801].name
   (powtórzenie elementu 863 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
958. [[mowe-re] Pasywka wroga [123801] — opis] 턴 종료 시 [KeptBlood] 수치에 따라\n- 다음 턴에 1 당 [Laceration] 2, [Laceration] 횟수 1 얻음\n- 5 이하라면, 매 턴마다 (6 - 수치)만큼 다음 턴에 [Binding] 1, [Vulnerable] 1, [AttackDown] 1씩 얻고 정신력 5씩 감소 (이 효과로 인하여 정신력이 -20 미만으로 내려가지 않음)\n- 5 초과라면, 매 턴마다 (수치 - 5)만큼 다음 턴에 [AttackUp] 1, [DefenseUp] 1씩 얻고 정신력 8씩 회복 (이 효과로 인하여 정신력이 30 초과로 올라가지 않음)
   źródło: Passives_Abnormality-mowe-re.json :: dataList[id=123801].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n, [KeptBlood], [Laceration], [Binding], [Vulnerable], [AttackDown], [AttackUp], [DefenseUp]
   znaczenie tagów: [KeptBlood] = 머금은 피 / Stored Blood; [Laceration] = 출혈 / Bleed; [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: At Turn End, depending on the [KeptBlood] Stack on self:\n- Inflict +2 [Laceration] and +1 [Laceration] Count on self for every Stack\n- At 5 or fewer Stack: gain 1 [Binding], 1 [Vulnerable], 1 [AttackDown] and lose 5 SP next turn for every (6 - Stack) (this effect cannot reduce this unit's SP below -20)\n- At more than 5 Stack: gain 1 [AttackUp], 1 [DefenseUp], and heal 8 SP next turn for every (Stack - 5) (this effect cannot increase this unit's SP higher than 30)
   PL:
959. [[mowe-re] Pasywka wroga [123805] — nazwa] 혈식 - 경화
   źródło: Passives_Abnormality-mowe-re.json :: dataList[id=123805].name
   (powtórzenie elementu 871 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
960. [[mowe-re] Pasywka wroga [123805] — opis] 등장 시 정신력 30 회복\n턴 시작 시 자신에게 [Laceration]이 있을 때,\n- [Laceration] 5 당 [AttackUp] 1, [DefenseUp] 1을 얻음 (최대 5)\n- [Laceration] 10 당 [ParryingResultUp] 1을 얻음 (최대 2)\n자신이 받는 [Laceration] 피해 50% 감소 (소수점 버림)
   źródło: Passives_Abnormality-mowe-re.json :: dataList[id=123805].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [AttackUp], [DefenseUp], [ParryingResultUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Upon entry, heal 30 SP\nTurn Start: if this unit has [Laceration],\n- Gain 1 [AttackUp] and 1 [DefenseUp] for every 5 [Laceration] (max 5)\n- Gain 1 [ParryingResultUp] for every 10 [Laceration] (max 2)\nTake -50% [Laceration] damage (rounded down)
   PL:
961. [[mowe-re] Pasywka wroga [130502] — nazwa] 의체 모델 - L37
   źródło: Passives_Abnormality-mowe-re.json :: dataList[id=130502].name
   (powtórzenie elementu 885 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
962. [[mowe-re] Pasywka wroga [130502] — opis] 등장 시 정신력 20 회복\n턴 시작 시 [Charge] 횟수 1당, 정신력 1 회복 (최대 15)\n턴 시작 시 [Charge] 횟수가 5 미만이면 자신에게 [Reduction] 1 부여\n턴 시작 시 [Charge] 횟수가 5 이상이면 [ParryingResultUp] 2 얻음\n턴 시작 시 [Charge] 횟수가 10 이상이면 [PlusCoinValueUp] 1 얻음\n턴 시작 시 [Charge] 횟수가 15 이상이면 기본 공격 스킬의 피해량이 (자신의 [Charge] 횟수 x 2)%만큼 추가로 증가
   źródło: Passives_Abnormality-mowe-re.json :: dataList[id=130502].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [Reduction], [ParryingResultUp], [PlusCoinValueUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [Reduction] = 공격 위력 감소 / Attack Power Down; [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost
   EN: Upon entry, heal 20 SP\nTurn Start: For every 1 [Charge] Count, heal 1 SP (max 15)\nTurn Start: At less than 5 [Charge] Count, inflict 1 [Reduction] on self\nTurn Start: At 5+ [Charge] Count, gain 2 [ParryingResultUp]\nTurn Start: At 10+ [Charge] Count, gain 1 [PlusCoinValueUp]\nTurn Start: At 15+ [Charge] Count, deal +([Charge] Count on self x 2)% damage with Base Attack Skills
   PL:

## [mr6] Pasywka wroga: Passives_Abnormality-mr6
- plik gry: `Passives_Abnormality-mr6.json`

963. [[mr6] Pasywka wroga [814201] — nazwa] 대결
   źródło: Passives_Abnormality-mr6.json :: dataList[id=814201].name
   limit: do 40 znaków
   EN: Dueling
   PL:
964. [[mr6] Pasywka wroga [814201] — opis] 체력이 50% 이하가 되면 특정 1명을 지정하는 특수 스킬 사용\n해당 턴 부터 다음 2턴 동안 흐트러짐, 패닉 상태가 되지 않음.\n대결 효과를 보유한 캐릭터가 이상이면, 동백이 공격 위력 증가 1을 얻음\n이상이 대결에서 승리한 경우, 다음 턴에 모든 아군이 피해량 증가 3을 얻음.\n동백이 대결에서 승리한 경우, 정신력을 최대로 회복함.
   źródło: Passives_Abnormality-mr6.json :: dataList[id=814201].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When HP falls below 50%, uses a special skill to target 1 unit, then becomes immune to Stagger and Panic for the next 2 turns.\nIf Yi Sang has 'Dueling', Dongbaek gains 1 Attack Power Up.\nIf Yi Sang wins the duel, all allies gain 3 Damage Up next turn.\nIf Dongbaek wins the duel, Dongbaek fully heals SP.
   PL:
965. [[mr6] Pasywka wroga [118301] — nazwa] 나는 아직 듣지 못했다.
   źródło: Passives_Abnormality-mr6.json :: dataList[id=118301].name
   limit: do 50 znaków
   EN: I am yet to hear your answer.
   PL:
966. [[mr6] Pasywka wroga [118301] — opis] 매 턴 시작 시, 본체와 부위에 보호막 900을 얻음.\n- 편성 순서가 가장 빠른 대상에게 [Teaching]이 있으면, 수치당 300을 감소해서 얻음\n- 편성 순서가 가장 빠른 대상에게 [Teaching] 3 이상있으면, 이후 전투동안 보호막을 얻지 않음
   źródło: Passives_Abnormality-mr6.json :: dataList[id=118301].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Teaching]
   znaczenie tagów: [Teaching] = 문답 / Dialogues
   EN: Every Turn Start: Core and Part gain 900 Shield.\n- When the unit with the earliest Deployment order has [Teaching], lose 300 Shield per Stack\n- When the unit with the earliest Deployment order has 3+ [Teaching], this unit does not gain Shield for the rest of the Encounter
   PL:
967. [[mr6] Pasywka wroga [118701] — nazwa] 소녀를 지켜봐주세요…!
   źródło: Passives_Abnormality-mr6.json :: dataList[id=118701].name
   limit: do 40 znaków
   EN: Watch this little girl...!
   PL:
968. [[mr6] Pasywka wroga [118701] — opis] 턴 시작 시 자신이 소환한 유닛이 있으면 정신력 10 회복
   źródło: Passives_Abnormality-mr6.json :: dataList[id=118701].desc
   limit: do 120 znaków
   EN: If there are this unit's summoned units at Turn Start, heal 10 SP
   PL:
969. [[mr6] Pasywka wroga [124105] — nazwa] 호표탄 장전
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124105].name
   limit: do 40 znaków
   EN: Tigermark Round Reload
   PL:
970. [[mr6] Pasywka wroga [124105] — opis] 턴 종료 시점에 체력이 90% 이하가 되었거나 2번째 턴 종료 시, [BulletPropellant]을 장전하고 다음 턴에 패턴이 변경됨\n- 흐트러짐 상태면, 흐트러짐 해제
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124105].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [BulletPropellant]
   znaczenie tagów: [BulletPropellant] = 호표탄 / Tigermark Round
   EN: Turn End: at 90% or less HP, or at the end of the 2nd turn, reload [BulletPropellant] and gain a new pattern next turn\n- If this unit is Staggered, recover from Stagger
   PL:
971. [[mr6] Pasywka wroga [124106] — nazwa] 뇌횡 [雷橫]
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124106].name
   limit: do 40 znaków
   EN: Lei Heng [雷橫]
   PL:
972. [[mr6] Pasywka wroga [124106] — opis] 턴 종료 시점에 체력이 80% 이하가 되었거나 4번째 턴 종료 시, 다음 턴에 패턴이 변경됨\n- 강력한 공격('쾌도난마')을 사용하며, 3번째 턴마다 반복함. 이 스킬을 사용하는 턴의 속도 최솟값, 최댓값 +10\n- 해당 턴 시작 시, [BattleSense] 25 얻음\n- 흐트러짐 상태면, 흐트러짐 해제
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124106].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [BattleSense]
   znaczenie tagów: [BattleSense] = 저력 [底力] / Inner Strength [底力]
   EN: Turn End: at 80% or less HP, or at the end of the 4th turn, gain a new pattern next turn\n- Use a powerful attack ('Tanglecleaver'), repeat every 3rd turn. +10 to Min & Max Speed for turns in which this unit uses this Skill\n- At the start of that turn, gain 25 [BattleSense]\n- If this unit is Staggered, recover from Stagger
   PL:
973. [[mr6] Pasywka wroga [124107] — nazwa] 천퇴성 [天退星]
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124107].name
   limit: do 40 znaków
   EN: Tiantui Star [天退星]
   PL:
974. [[mr6] Pasywka wroga [124107] — opis] 턴 종료 시점에 체력이 60% 이하가 되었거나 다음 턴에 강력한 공격('쾌도난마')을 이번 전투에서 두 번째로 사용할 예정이면, 다음 턴에 패턴이 변경됨\n- 해당 턴 시작 시, [Irritation] 1 얻음\n- 해당 턴 시작 시, [BulletPropellantSpecial] 18 얻고 즉시 장전\n· [BulletPropellantSpecial]을 전부 소모할 경우, 해당 효과가 [BulletPropellant]으로 변경되고 다음 턴에 엄격한 엄지 솔다토 2명을 소환하여 [BulletPropellantSpecial]을 보급받음\n- 흐트러짐 상태면, 흐트러짐 해제
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124107].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n, [Irritation], [BulletPropellantSpecial], [BulletPropellant]
   znaczenie tagów: [Irritation] = 천퇴성[天退星] / Tiantui Star [天退星]; [BulletPropellantSpecial] = 맹호표탄 / Savage Tigermark Round; [BulletPropellant] = 호표탄 / Tigermark Round
   EN: If this unit's HP dropped to 60% or below at Turn End, or if this unit is set to use a powerful attack ('Tanglecleaver') next turn for the second time this Encounter, gain a new pattern next turn\n- When that turn starts, gain 1 [Irritation]\n- When that turn starts, gain 18 [BulletPropellantSpecial] and reload immediately\n· If this unit spends all [BulletPropellantSpecial], convert the effect to [BulletPropellant] and summon 2 of "Stern Soldato of the Thumb" units next turn and have them supply this unit with [BulletPropellantSpecial]\n- When Staggered, recover from Stagger
   PL:
975. [[mr6] Pasywka wroga [124108] — nazwa] 소지 천퇴성 뇌횡
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124108].name
   limit: do 50 znaków
   EN: Lei Heng, The Pinky's Tiantui Star
   PL:
976. [[mr6] Pasywka wroga [124108] — opis] 턴 종료 시점에 체력이 40% 이하가 되었거나 다음 턴에 강력한 공격('쾌도난마')을 이번 전투에서 세 번째로 사용할 예정이면, 다음 턴에 패턴이 변경됨\n- 강력한 공격 '쾌도난마'가 '초절맹호살격난참'으로 변경됨. 이 스킬을 사용하는 턴의 속도 최솟값, 최댓값 +15\n- [BattleSense]이 [RestoredBattleSense]으로 변경\n- [Irritation]가 [DerivativeHugeIrritation]으로 변경\n- 흐트러짐 상태면, 흐트러짐 해제
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124108].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n, [BattleSense], [RestoredBattleSense], [Irritation], [DerivativeHugeIrritation]
   znaczenie tagów: [BattleSense] = 저력 [底力] / Inner Strength [底力]; [RestoredBattleSense] = 극력 [極力] / Extreme Strength [極力]; [Irritation] = 천퇴성[天退星] / Tiantui Star [天退星]; [DerivativeHugeIrritation] = 신(心) - 천퇴성[天退星] / Shin (心) - Tiantui Star [天退星]
   EN: Turn End: at 40% or less HP, or if this unit is set to use a powerful attack ('Tanglecleaver') next turn for the third time this Encounter, gain a new pattern next turn\n- Replace the powerful attack 'Tanglecleaver' with 'Savage Tigerslayer's Perfected Flurry of Blades'. +15 to Min & Max Speed for turns in which this unit uses this Skill\n- Convert [BattleSense] to [RestoredBattleSense]\n- Convert [Irritation] to [DerivativeHugeIrritation]\n- If this unit is Staggered, recover from Stagger
   PL:
977. [[mr6] Pasywka wroga [124112] — nazwa] 천퇴성도 오버히트
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124112].name
   limit: do 50 znaków
   EN: Tiantui Star's Blade - Overheat
   PL:
978. [[mr6] Pasywka wroga [124112] — opis] 강력한 공격('쾌도난마', '초절맹호살격난참')을 사용하였다면, 이번 전투 동안 강력한 공격을 사용한 횟수만큼 다음 턴에 [Complacency] 얻음 (최대 5)
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124112].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [Complacency]
   znaczenie tagów: [Complacency] = 오버히트 / Overheat
   EN: If this unit used a powerful attack ('Tanglecleaver' or 'Savage Tigerslayer's Perfected Flurry of Blades'), gain [Complacency] next turn equal to the number of times those skills were used (max 5)
   PL:
979. [[mr6] Pasywka wroga [124301] — nazwa] 더는 못 먹어
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124301].name
   limit: do 40 znaków
   EN: I'm Stuffed
   PL:
980. [[mr6] Pasywka wroga [124301] — opis] [FullCharon]이 10이상 일 때\n- 턴 시작 시 강제 흐트러짐 발생(1턴 동안)\n- 턴이 종료되면 [HungryCharon], [FullCharon] 모두 제거
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124301].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [FullCharon], [HungryCharon]
   znaczenie tagów: [FullCharon] = 포만감 / Indulged; [HungryCharon] = 배고픔-분노 / Hunger-Rage
   EN: At 10+ [FullCharon]...\n- Turn Start: enter a forced Stagger State (for a turn)\n- Turn End: remove [HungryCharon] and [FullCharon] completely
   PL:
981. [[mr6] Pasywka wroga [124302] — nazwa] 부릉부릉. 화났어
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124302].name
   limit: do 40 znaków
   EN: Vroom-vroom. Angry now
   PL:
982. [[mr6] Pasywka wroga [124302] — opis] 전투 시작 시, 베르길리우스가 [HungryCharon]를 1얻음\n[HungryCharon]가 3에 도달하면 강력한 공격('부릉부릉')을 사용\n※[FullCharon]으로 발생한 흐트러짐에서는 전투 시작 시 발동하지 않음
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124302].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [HungryCharon], [FullCharon]
   znaczenie tagów: [HungryCharon] = 배고픔-분노 / Hunger-Rage; [FullCharon] = 포만감 / Indulged
   EN: Combat Start: Vergilius gains 1 [HungryCharon]\nAt 3 [HungryCharon], uses a devastating attack ("Vroom-Vroom")\n※ Does not activate at "Combat Start" if this unit is Staggered due to [FullCharon]
   PL:
983. [[mr6] Pasywka wroga [124303] — nazwa] 사탕 있어?
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124303].name
   limit: do 40 znaków
   EN: Got Candy?
   PL:
984. [[mr6] Pasywka wroga [124303] — opis] 편성 순서가 가장 빠른 인격 순서로 [GiveMeCandy]이 없는 적 1명에게 턴 시작 시 [GiveMeCandy] 1을 부여함
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124303].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [GiveMeCandy]
   znaczenie tagów: [GiveMeCandy] = 사탕 / Candy
   EN: Turn Start: in Deployment Order, inflict 1 [GiveMeCandy] against 1 enemy without [GiveMeCandy]
   PL:
985. [[mr6] Pasywka wroga [124304] — nazwa] 꼬미 때려도 사탕 안나와
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124304].name
   limit: do 40 znaków
   EN: Kkomi's not a Piñata
   PL:
986. [[mr6] Pasywka wroga [124304] — opis] 꼬미를 공격한 대상에게 [GiveMeCandy] 1 부여
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124304].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [GiveMeCandy]
   znaczenie tagów: [GiveMeCandy] = 사탕 / Candy
   EN: Inflict 1 [GiveMeCandy] to the target who attacked Kkomi
   PL:
987. [[mr6] Pasywka wroga [124001] — nazwa] 깨져 흩날리는 경혈
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124001].name
   limit: do 50 znaków
   EN: Shattering, Scattering Hardblood
   PL:
988. [[mr6] Pasywka wroga [124001] — opis] 적의 공격, 상태이상 피해로 사망 시 [BloodDinner] 30 증가. 스스로 제거된 경우 발동되지 않음.
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124001].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [BloodDinner]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast
   EN: When this unit is killed due to enemy attack or Status effect damage, increase [BloodDinner] by 30. Does not activate if this unit killed itself.
   PL:
989. [[mr6] Pasywka wroga [124002] — nazwa] 지나온 모험의 기억들
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124002].name
   limit: do 50 znaków
   EN: Memories of the Journeys Past
   PL:
990. [[mr6] Pasywka wroga [124002] — opis] 모든 아군에게 특수한 효과 부여
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124002].desc
   limit: do 120 znaków
   EN: Apply special effect to all allies
   PL:
991. [[mr6] Pasywka wroga [124003] — nazwa] 지나온 모험의 기억들
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124003].name
   (powtórzenie elementu 989 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
992. [[mr6] Pasywka wroga [124003] — opis] 턴 시작 시 모든 적에게 [Laceration] 3부여, [Laceration] 횟수 1 증가
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124003].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Turn Start: Inflict 3 [Laceration] and +1 [Laceration] Count against all enemies
   PL:
993. [[mr6] Pasywka wroga [124004] — nazwa] 지나온 모험의 기억들
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124004].name
   (powtórzenie elementu 989 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
994. [[mr6] Pasywka wroga [124004] — opis] 턴 종료 시 돈키호테에게  [RegainedStrength] 1 부여
   źródło: Passives_Abnormality-mr6.json :: dataList[id=124004].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RegainedStrength]
   znaczenie tagów: [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust
   EN: Turn End: Apply 1 [RegainedStrength] on Don Quixote
   PL:

## [mr7] Pasywka wroga: Passives_Abnormality-mr7
- plik gry: `Passives_Abnormality-mr7.json`

995. [[mr7] Pasywka wroga [131911] — nazwa] 아이언메이든 - 재세동
   źródło: Passives_Abnormality-mr7.json :: dataList[id=131911].name
   limit: do 40 znaków
   EN: Iron Maiden - Defibrillation
   PL:
996. [[mr7] Pasywka wroga [131911] — opis] 등장 시 정신력 30 회복
   źródło: Passives_Abnormality-mr7.json :: dataList[id=131911].desc
   limit: do 120 znaków
   EN: Upon entry, heal 30 SP
   PL:
997. [[mr7] Pasywka wroga [135201] — nazwa] 사냥 표식
   źródło: Passives_Abnormality-mr7.json :: dataList[id=135201].name
   limit: do 40 znaków
   EN: Hunter's Mark
   PL:
998. [[mr7] Pasywka wroga [135201] — opis] 3턴마다 무작위 1명을 지정하여, 속도를 1로 만들고 모든 스킬의 타겟으로 지정함\n(흐트러짐으로 발동되지 못한 경우, 다음 턴에 발동함)
   źródło: Passives_Abnormality-mr7.json :: dataList[id=135201].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Every 3 turns, select a random enemy, reduce their Speed to 1, and target it with all of this unit's Skills\n(If this effect could not be activated due to Stagger, activate it next turn)
   PL:
999. [[mr7] Pasywka wroga [135501] — nazwa] 단말기로 전해진 지령
   źródło: Passives_Abnormality-mr7.json :: dataList[id=135501].name
   limit: do 50 znaków
   EN: Prescript Delivered on a Device
   PL:
1000. [[mr7] Pasywka wroga [135501] — opis] 스테이지 시작 시, 최대 체력의 20%만큼 보호막 얻음 (이번 전투 동안 유지)\n\n턴 시작 시\n- [UnlockBuff_Base] 단계에 따라 [IndexPrescript_Base_2nd] 얻음\n- <color=#ff6000><mark=#ff000040><b><u>무작위 적에게 [IndexPrescriptTargetToPersonality]을 부여하고, 우선 공격함</u></b></mark></color>\n\n[BlessingOfIndexPrescriptEnemy]당 [IndexPrescriptTargetToPersonality]에게 가하는 피해량 +2.5% (최대 20%)\n- [BlessingOfIndexPrescriptEnemy]가 9면, 대신 모든 대상에게 가하는 피해량 +30%
   źródło: Passives_Abnormality-mr7.json :: dataList[id=135501].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [UnlockBuff_Base], [IndexPrescript_Base_2nd], [IndexPrescriptTargetToPersonality], [BlessingOfIndexPrescriptEnemy]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [IndexPrescript_Base_2nd] = 지령 / Prescript; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript
   EN: Encounter Start: Gain Shield equal to 20% of max HP (remains throughout this Encounter)\n\nTurn Start:\n- Gain [IndexPrescript_Base_2nd] based on [UnlockBuff_Base] stage on self\n- <color=#ff6000><mark=#ff000040><b><u>Inflict [IndexPrescriptTargetToPersonality] to a random enemy and prioritize attacking that enemy</u></b></mark></color>\n\nDeal +2.5% damage to [IndexPrescriptTargetToPersonality] for every [BlessingOfIndexPrescriptEnemy] (max 20%)\n- At 9 [BlessingOfIndexPrescriptEnemy], deal +30% damage to all targets instead
   PL:
1001. [[mr7] Pasywka wroga [135503] — nazwa] 해금
   źródło: Passives_Abnormality-mr7.json :: dataList[id=135503].name
   limit: do 40 znaków
   EN: Unlock
   PL:
1002. [[mr7] Pasywka wroga [135503] — opis] 턴 종료 시 [BlessingOfIndexPrescriptEnemy]가 3/6/9거나 체력이 90%/70%/50% 이하면,\n- [UnlockBuff_1]/[UnlockBuff_2]/[UnlockBuff_3] 얻음\n- 정신력이 45로 증가\n- 보유한 [PressureOfPrescript] 전부 소모, 흐트러짐 해제\n- 처음으로 [UnlockBuff_Base] 획득한 다음 턴에 [BlessingOfIndexPrescriptEnemy] 1 얻음\n\n체력 조건으로 [UnlockBuff_Base] 획득 시\n- (증가한 정신력/15)만큼 [KarmaOfIndexStudent] 얻음\n- [BlessingOfIndexPrescriptEnemy]가 3/6/9 미만이면, 3/6/9로 변경,\n증가한 수치 1당 다음 턴 시작 시 [DefenseDown] 1, [KarmaOfIndexStudent] 2 얻음
   źródło: Passives_Abnormality-mr7.json :: dataList[id=135503].desc
   limit: do 840 znaków
   tokeny: zachowaj dokładnie: \n, [BlessingOfIndexPrescriptEnemy], [UnlockBuff_1], [UnlockBuff_2], [UnlockBuff_3], [PressureOfPrescript], [UnlockBuff_Base], [KarmaOfIndexStudent], [DefenseDown]
   znaczenie tagów: [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [UnlockBuff_1] = 해금 - I / Unlock - I; [UnlockBuff_2] = 해금 - II / Unlock - II; [UnlockBuff_3] = 해금 - III / Unlock - III; [PressureOfPrescript] = 압박감 / Onus; [UnlockBuff_Base] = 해금 / Unlock; [KarmaOfIndexStudent] = 카르마 / Karmic Consequence; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn End: At 3/6/9 [BlessingOfIndexPrescriptEnemy] or at 90%-/70%-/50%- HP,\n- Gain [UnlockBuff_1]/[UnlockBuff_2]/[UnlockBuff_3]\n- Heal to 45 SP\n- Consume all [PressureOfPrescript] and recover from Stagger\n- Gain 1 [BlessingOfIndexPrescriptEnemy] in the turn after [UnlockBuff_Base] was gained for the first time\n\nIf [UnlockBuff_Base] was gained based on HP conditional above,\n- Gain [KarmaOfIndexStudent] by (sum of healed SP / 15)\n- Increase [BlessingOfIndexPrescriptEnemy] to 3/6/9 if this unit had less than 3/6/9 [BlessingOfIndexPrescriptEnemy]; gain 1 [DefenseDown] and 2 [KarmaOfIndexStudent] next turn for every [BlessingOfIndexPrescriptEnemy] Stack gained
   PL:
1003. [[mr7] Pasywka wroga [135505] — nazwa] 몰입
   źródło: Passives_Abnormality-mr7.json :: dataList[id=135505].name
   limit: do 40 znaków
   EN: Concentration
   PL:
1004. [[mr7] Pasywka wroga [135505] — opis] [UnlockBuff_3]을 얻으면 다음 효과 적용\n- [BlandishmentShinEnemyDelete], 최대 체력의 50%만큼 보호막 얻음 (이번 전투 동안 유지)\n- [PressureOfPrescript]이 [PressureOfPrescript_2nd]으로 변경되고, 최대로 증가\n- 턴 시작 시 [PressureOfPrescript_2nd] 1 얻음
   źródło: Passives_Abnormality-mr7.json :: dataList[id=135505].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_3], [BlandishmentShinEnemyDelete], [PressureOfPrescript], [PressureOfPrescript_2nd]
   znaczenie tagów: [UnlockBuff_3] = 해금 - III / Unlock - III; [BlandishmentShinEnemyDelete] = 신(心) - ??? / Shin (心) - ???; [PressureOfPrescript] = 압박감 / Onus; [PressureOfPrescript_2nd] = 극심한 압박감 / Extreme Onus
   EN: At [UnlockBuff_3], apply the following effects:\n- [BlandishmentShinEnemyDelete], gain Shield equal to 50% of max HP (lasts for the rest of this Encounter)\n- Intensify [PressureOfPrescript] to [PressureOfPrescript_2nd] and max out its Stack\n- Turn Start: Gain 1 [PressureOfPrescript_2nd]
   PL:
1005. [[mr7] Pasywka wroga [141801] — nazwa] 필사의 분전
   źródło: Passives_Abnormality-mr7.json :: dataList[id=141801].name
   limit: do 40 znaków
   EN: Desperate Struggle
   PL:
1006. [[mr7] Pasywka wroga [141801] — opis] - 턴 시작 시 [SupportProtect] 3 얻음\n- 엄지 아비가 합에서 승리하면, 해당 공격 종료 시 '콜피 소타니'로 일방 공격 (턴당 2회)
   źródło: Passives_Abnormality-mr7.json :: dataList[id=141801].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [SupportProtect]
   znaczenie tagów: [SupportProtect] = 원호 방어 / Assist Defense
   EN: - Turn Start: Gain 3 [SupportProtect]\n- When the Thumb Nursefather wins a Clash, and uses an Attack against the target, follow up with "Colpi Sottani" as an Unopposed Attack against the same target (2 times per turn)
   PL:
1007. [[mr7] Pasywka wroga [141801] — tekst klimatyczny] ‘지금이라면, 죽일 수 있지 않을까.’\n\n잠에 든 스승을 보며, 루치오는 항상 같은 상념에 빠졌다.\n그 생각을 행동으로 옮기지 않는 것은, 이미 학습된 공포와 뒷골목에서 자신을 데려와 준 은혜 때문이었다.\n하지만 쌓여버린 원한이 너무나 깊다. 진심을 다해 명령을 따르겠다 말하면서도 루치오는 다짐했다.\n이 전투가 끝나면 반드시 죽이자. 남은 눈 하나까지 베고 찔러 죽여버리자.\n온몸에 멍이 든 소년의 눈에 처음으로 생기가 돌기 시작했다.
   źródło: Passives_Abnormality-mr7.json :: dataList[id=141801].flavor
   limit: do 860 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'Maybe I can kill her now. Maybe this is my chance.'\n\nOnce again, the same contemplation comes to seize Lucio as he looms over his master, who lies fast asleep.\nBut this impulse remains an unactioned thought, for he had both fear born from experience and gratitude for his deliverance from the Backstreets.\nYet, his resentment runs too deep. Lucio makes a promise with himself, even as he swears utter fealty without a trace of deception:\n'Once this battle is behind us, I will kill her. I will gouge out her other eye and stab and slash at her, again and again, until she no longer moves.'\nFor the first time, fire burns in the eyes of the boy whose body is covered in bruises.
   PL:
1008. [[mr7] Pasywka wroga [137901] — nazwa] 위신 유지
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137901].name
   limit: do 40 znaków
   EN: Authority Unbroken
   PL:
1009. [[mr7] Pasywka wroga [137901] — opis] 전투 내 ‘엄지 제자 - 루치오’가 있는 동안 받는 최종 피해량 -50%
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137901].desc
   limit: do 120 znaków
   EN: Take -50% final damage if "The Thumb Apprentice - Lucio" is on the field
   PL:
1010. [[mr7] Pasywka wroga [137911] — nazwa] 예지안
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137911].name
   limit: do 40 znaków
   EN: The Eye of Precognition
   PL:
1011. [[mr7] Pasywka wroga [137911] — opis] 스테이지 등장 시, [FutureEyeOnMirror] 30 얻음\n[FutureEyeOnMirror] 수치가 0이 되면, [FutureEyeOnMirror]이 [FutureEyeOffMirror]로 변경됨
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137911].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [FutureEyeOnMirror], [FutureEyeOffMirror]
   znaczenie tagów: [FutureEyeOnMirror] = 예지안 / Eye of Precognition; [FutureEyeOffMirror] = 예지안 과열 / Eye of Precognition - Overheat
   EN: When this unit enters the Encounter, gain 30 [FutureEyeOnMirror]\nAt 0 [FutureEyeOnMirror] Stack, convert [FutureEyeOnMirror] to [FutureEyeOffMirror]
   PL:
1012. [[mr7] Pasywka wroga [137911] — tekst klimatyczny] 오딘의 눈이라 불린 이 유물은, 사실 세 갈래로 쪼개진 어떤 유물의 파편 중 하나다.
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137911].flavor
   limit: do 140 znaków
   EN: This Relic, known as the Eye of Odin, is but a third of a whole Relic that was broken into three parts.
   PL:
1013. [[mr7] Pasywka wroga [137902] — nazwa] 가속하는 미래
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137902].name
   limit: do 40 znaków
   EN: Accelerating Future
   PL:
1014. [[mr7] Pasywka wroga [137902] — opis] 합 진행 시 <color=#ff6000><mark=#ff000040><b><u>매 합마다 자신에게 [LookingFuture] 1 부여</u></b></mark></color>\n[LookingFuture]는 턴당 (턴 시작 시 보유한 [FutureEyeOnMirror]/3)까지 얻을 수 있음\n[FutureEyeOnMirror]이 있을 때, <color=#ff6000><mark=#ff000040><b><u>일방공격을 당하거나 합 패배 시 ‘예지’ 스킬 발동</u></b></mark></color>
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137902].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [LookingFuture], [FutureEyeOnMirror]
   znaczenie tagów: [LookingFuture] = 가속하는 미래 / Accelerating Future; [FutureEyeOnMirror] = 예지안 / Eye of Precognition
   EN: In a Clash, <color=#ff6000><mark=#ff000040><b><u>gain 1 [LookingFuture] with every Clash</u></b></mark></color>\nCan gain up to ([FutureEyeOnMirror] Stack at Turn Start / 3) [LookingFuture] per turn\nWhile this unit has [FutureEyeOnMirror], <color=#ff6000><mark=#ff000040><b><u>getting attacked by Unopposed Attacks or losing a Clash activates the "Precognition" Skill</u></b></mark></color>
   PL:
1015. [[mr7] Pasywka wroga [137902] — tekst klimatyczny] “맞대고 부딪힐수록 이 검은 가열되고, 내가 본 미래에 도달할 때까지 가속할 거다.”
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137902].flavor
   limit: do 140 znaków
   EN: "The more we clash, the hotter my sword will become... and accelerate to bring us to the future I foresaw."
   PL:
1016. [[mr7] Pasywka wroga [137908] — nazwa] 과부하
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137908].name
   limit: do 40 znaków
   EN: Overloaded
   PL:
1017. [[mr7] Pasywka wroga [137908] — opis] 다음 조건에 따라 [FutureEyeOnMirror] 감소\n- [LookingFuture]를 얻지 못하면, 매 합마다 [FutureEyeOnMirror] 1 감소\n- 일방 공격을 당할 시 [FutureEyeOnMirror] 1 감소\n- 합 패배 시 [FutureEyeOnMirror] 3 감소
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137908].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [FutureEyeOnMirror], [LookingFuture]
   znaczenie tagów: [FutureEyeOnMirror] = 예지안 / Eye of Precognition; [LookingFuture] = 가속하는 미래 / Accelerating Future
   EN: The following causes this unit to lose [FutureEyeOnMirror] Stack:\n- If this unit fails to gain [LookingFuture], lose 1 [FutureEyeOnMirror] with every Clash\n- When this unit is attacked by an Unopposed Attack, lose 1 [FutureEyeOnMirror]\n- On Clash Lose, lose 3 [FutureEyeOnMirror]
   PL:
1018. [[mr7] Pasywka wroga [137908] — tekst klimatyczny] ‘눈이 지끈거리며 뜨거워지고, 시야가 붉어진다’
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137908].flavor
   limit: do 120 znaków
   EN: 'The eye's heating up, its socket is starting to ache, and my vision is turning red.'
   PL:
1019. [[mr7] Pasywka wroga [137905] — nazwa] 팔레르모 스파다
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137905].name
   limit: do 40 znaków
   EN: La Spada di Palermo
   PL:
1020. [[mr7] Pasywka wroga [137905] — opis] 메인 타겟의 화상 1당, 보호막에 입히는 피해량 15% 증가 (최대 300%)\n스킬 사용 시 대상의 공격 스킬이 참격 혹은 관통 속성이면, 합 위력 +1\n자신의 스킬 효과로 [VibrationExplosion]이 발동되었다면, 다음 턴 [AttackDmgUp] 2 얻음 (턴당 3회)\n자신의 스킬 효과로 크리티컬이 발동되었다면, 정신력 5 회복
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137905].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationExplosion], [AttackDmgUp]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Deal +15% more damage against Shields for every Burn on the main target (max 300%)\nOn Skill Use, if target's Attack Skill is either a Slash or a Pierce Skill, Clash Power +1\nIf this unit's Skill effects triggered [VibrationExplosion], gain 2 [AttackDmgUp] next turn (3 times per turn)\nIf this unit hit Critically with its Skill effects, heal 5 SP
   PL:
1021. [[mr7] Pasywka wroga [137904] — nazwa] 보냐텔리 가문의 수치
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137904].name
   limit: do 50 znaków
   EN: The Shame of Famiglia Bognatelli
   PL:
1022. [[mr7] Pasywka wroga [137904] — opis] [Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 체력, 정신력, 흐트러짐 손상 피해량 -30%\n[AccelBullet]이 1 이상이면, [AccelBullet]을 소모하는 스킬의 피해량 +30%, 보호막에 입히는 피해량 +150%\n[AccelBullet] 소모한 수치 1당, [Breath] 4 얻음\n[AccelBullet]을 소모하는 코인을 굴릴 때, 가속탄이 없는 경우에도 공격을 취소하지 않음
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137904].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [AccelBullet], [Breath]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [AccelBullet] = 가속탄 / Acceleration Round; [Breath] = 호흡 / Poise
   EN: Take -30% HP, SP damage from [Combustion], [Laceration], [Burst], [Sinking]; -30% to Stagger Threshold raised by [Vibration]\nAt 1+ [AccelBullet], Skills that spend [AccelBullet] deal +30% damage and deal +150% damage against Shields\nGain 4 [Breath] for every [AccelBullet] spent\nWhen flipping a Coin that spends [AccelBullet], does not cancel the attack even if this unit does not have Acceleration Round
   PL:
1023. [[mr7] Pasywka wroga [137904] — tekst klimatyczny] “팔레르모를 전수 받고, 가보까지 계승 받았음에도 이런 추태를 보이다니.”\n“네가 물려 받은 유물과 검은, 네 불명예스러운 잔향이 배어 있으니 회수하지 않겠다.”\n“언더보스로 승격한지 사흘 만에 파면 당한 건 발렌치나, 네가 유일할 테지.”\n“너는 가문의 수치다. 보냐텔리는 너에게서 사랑을 거두겠다.”
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137904].flavor
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "You were an inheritor of the Palermitan style and a wielder of our family heirloom—you had every privilege one could ever hope for. How dare you embarrass yourself like this?"\n"We'll let you keep the Relic and the sword, for they have been defiled by your dishonorable stench."\n"To be promoted to the station of a Sottocapo, an Underboss... only to be ousted in a mere 3 days. No one else has suffered such pathetic humiliation apart from you, Valencina."\n"You are the shame of our family. La Famiglia Bognatelli withdraws its love from you."
   PL:
1024. [[mr7] Pasywka wroga [137909] — nazwa] 신(心) - 발렌치나
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137909].name
   limit: do 40 znaków
   EN: Shin (心) - Valencina
   PL:
1025. [[mr7] Pasywka wroga [137909] — opis] 피격 시 혹은 ‘엄지 제자 - 루치오’가 전투 불능이 되면, 다음 턴에 [ObsessionAndGreed] 얻음
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137909].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [ObsessionAndGreed]
   znaczenie tagów: [ObsessionAndGreed] = 신(心) - 발렌치나 / Shin (心) - Valencina
   EN: When hit, or when "The Thumb Apprentice - Lucio" is defeated, gain [ObsessionAndGreed] next turn
   PL:
1026. [[mr7] Pasywka wroga [137909] — tekst klimatyczny] “후… 결국 그 광신도 놈이 짜 놓은 작전대로 들어가서 깽판을 치면 된다는 건데… 이런다고 진짜 티켓이 돌아오는 거 맞아?”
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137909].flavor
   limit: do 230 znaków
   EN: "*sigh* Okay. So, you're saying we can get Ticket back by going in and wrecking the place according to that fanatic's plan... Is this really going to bring Ticket back to us?"
   PL:
1027. [[mr7] Pasywka wroga [137906] — nazwa] 루치오. 이 쓸모없는 것
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137906].name
   limit: do 50 znaków
   EN: Lucio, you useless little shit!
   PL:
1028. [[mr7] Pasywka wroga [137906] — opis] ‘엄지 제자 - 루치오’가 전투 불능이 되면, 패시브 ‘사냥 시간’이 발동
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137906].desc
   limit: do 120 znaków
   EN: When "The Thumb Apprentice - Lucio" is defeated, activate "Time to Hunt" Passive
   PL:
1029. [[mr7] Pasywka wroga [137910] — nazwa] 사냥 시간
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137910].name
   limit: do 40 znaków
   EN: Time to Hunt
   PL:
1030. [[mr7] Pasywka wroga [137910] — opis] 턴 시작 시 흐트러짐 상태면 흐트러짐을 해제\n\n무작위 수감자 1명을 지정하여, [TeachersPrey]을 부여\n- 이후 4턴마다 1번씩 발동\n- 스킬 ‘처분’으로 대상을 처치할 시 다음 턴에 다시 발동
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137910].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [TeachersPrey]
   znaczenie tagów: [TeachersPrey] = 사냥 표적 / Game Target
   EN: Turn Start: If this unit is Staggered, recover from Stagger\n\nSelect a random Sinner and inflict [TeachersPrey]\n- Activates every 4 turns after the initial activation\n- If this unit kills the target with the Skill "Disposal," activate it again next turn
   PL:
1031. [[mr7] Pasywka wroga [137910] — tekst klimatyczny] 팔레르모는 보냐텔리 가문의 성향을 그대로 빼닮은 검술이다.\n하나의 사냥감을 집요하게 노려, 사냥하고 해체한다. 은밀함은 배제한다. 명예롭고 당당하게, 모두의 시선 앞에서 상대를 죽인다.\n그 화려한 검술은 수많은 영예를 낳았고, 보냐텔리 가문을 뒷골목의 7대 명문가로 만들었다.\n팔레르모를 완전히 터득한 발렌치나는 연기전쟁에서 수많은 장교와 베테랑 병사들의 목을 떨구며 연기전쟁의 영웅 중 한 명이 되었다.\n하지만 누가 예상이나 했을까. 그 명성이 그녀의 발목을 잡을 줄이야.
   źródło: Passives_Abnormality-mr7.json :: dataList[id=137910].flavor
   limit: do 1070 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Palermitan Style has much in common with the originator of the sword technique—La Famiglia Bognatelli.\nBoth the Famiglia and the sword style are renowned for relentlessly focusing on a single prey during a hunt, which is concluded with a Coup de Grâce that may as well be called a dissection. These executions are not carried out in the shadows, but instead, proudly put on display for all to behold.\nThe spectacular and formidable sword style has granted the Famiglia much honor and prestige, eventually securing them a place among the Sette Famiglie of the Backstreets.\nValencina, a master of the Palermitan Style, used it to hunt and execute many officers and so-called battle-hardened soldiers during the Smoke War, becoming a veritable "War Hero."\nIronically, no one could have imagined her fall would sink as low as her fame once soared.
   PL:
1032. [[mr7] Pasywka wroga [138201] — nazwa] 원한 문신 [<s>큰 형님</s>]
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138201].name
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: Vengeance Tattoos [<s>Great Brother</s>]
   PL:
