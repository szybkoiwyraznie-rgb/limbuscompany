# Paczka AI P69 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 5/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P69_3c_przeciwnicy_i_anomalie_cz05.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P69_3c_przeciwnicy_i_anomalie_cz05.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [a1c5p2] Pasywka wroga: Passives_Enemy-a1c5p2
- plik gry: `Passives_Enemy-a1c5p2.json`

1. [[a1c5p2] Pasywka wroga [9008901] — nazwa] 백화
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9008901].name
   limit: do 40 znaków
   EN: Pallidification
   PL: Pallidification
2. [[a1c5p2] Pasywka wroga [9008901] — opis] 매 턴마다 자신을 제외한 살아있는 백화인 아군당 자신의 공격 레벨과 방어 레벨이 2씩 증가한다.
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9008901].desc
   limit: do 130 znaków
   EN: Gain 2 Offense Level and Defense Level for every living Pallidified ally (not counting this unit)
   PL: za każdego żyjącego Zbielałego sojusznika (nie licząc tej jednostki) zyskuje 2 Poziomu Ataku i Poziomu Obrony
3. [[a1c5p2] Pasywka wroga [9008902] — nazwa] 덮쳐오는 부정
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9008902].name
   limit: do 40 znaków
   EN: Crashing Filth
   PL: Crashing Filth
4. [[a1c5p2] Pasywka wroga [9008902] — opis] 전체 체력의 10%만큼 남았을 경우, 적중 시 정신력 피해 20을 입히고 다음 턴에 창백한 소음 1을 부여한 뒤, 사망함.
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9008902].desc
   limit: do 120 znaków
   EN: At 10% of Max HP, inflict 20 SP damage On Hit, inflict 1 Pallid Noise next turn, then dies.
   PL: przy 10% Maks. HP, przy trafieniu zadaje 20 obrażeń SP, nakłada 1 Bladego Szumu w następnej turze, po czym umiera.
5. [[a1c5p2] Pasywka wroga [9008903] — nazwa] 퍼져가는 불결
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9008903].name
   limit: do 40 znaków
   EN: Spreading Flames
   PL: Spreading Flames
6. [[a1c5p2] Pasywka wroga [9008903] — opis] 턴 종료 시 백화 상태의 아군이 있을 때, 자신을 제외한 백화 상태 아군 수만큼 정신력 20이상의 모든 적 정신력 감소
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9008903].desc
   limit: do 210 znaków
   EN: If there are surviving Pallidified allies at Turn End, all enemies with 20 or more SP lose 1 SP for every surviving Pallidified ally (not counting this unit)
   PL: Koniec tury: jeżeli żyją Zbielali sojusznicy, wszyscy wrogowie z 20 lub więcej SP tracą 1 SP za każdego żyjącego Zbielałego sojusznika (nie licząc tej jednostki)
7. [[a1c5p2] Pasywka wroga [9009001] — nazwa] 퍼져가는 불결
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009001].name
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
8. [[a1c5p2] Pasywka wroga [9009001] — opis] 턴 종료 시 백화 상태의 아군이 있을 때, 자신을 제외한 백화 상태 아군 수만큼 정신력 20이상의 모든 적 정신력 감소
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009001].desc
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
9. [[a1c5p2] Pasywka wroga [9009101] — nazwa] 응어리 치유
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009101].name
   limit: do 40 znaków
   EN: Healing Resentment
   PL: Healing Resentment
10. [[a1c5p2] Pasywka wroga [9009101] — opis] 턴 종료 시 백화 상태의 아군이 있을 때, 자신을 제외한 모든 백화 상태 아군을 (자신을 제외한 백화 상태 아군 수 * 3)만큼 체력 회복
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009101].desc
   limit: do 170 znaków
   EN: If there are surviving Pallidified allies at Turn End, all other Pallidified allies heal (# of other Pallidified allies * 3) HP
   PL: Koniec tury: jeżeli żyją Zbielali sojusznicy, wszyscy pozostali Zbielali sojusznicy przywracają (liczba pozostałych Zbielałych sojuszników x 3) HP
11. [[a1c5p2] Pasywka wroga [9009201] — nazwa] 쌓여가는 유기
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009201].name
   limit: do 40 znaków
   EN: Cumulating Organic Material
   PL: Cumulating Organic Material
12. [[a1c5p2] Pasywka wroga [9009201] — opis] 자신을 제외한 살아있는 아군당 자신의 방어 레벨이 1 증가
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009201].desc
   limit: do 120 znaków
   EN: Defense Level +1 for every surviving ally (not counting this unit)
   PL: Poziom Obrony +1 za każdego żyjącego sojusznika (nie licząc tej jednostki)
13. [[a1c5p2] Pasywka wroga [9009202] — nazwa] 붕괴한 무기
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009202].name
   limit: do 50 znaków
   EN: Disintegrating Inorganic Material
   PL: Disintegrating Inorganic Material
14. [[a1c5p2] Pasywka wroga [9009202] — opis] 아군이 죽었다면, 다음 턴에 취약 1 얻음
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009202].desc
   limit: do 120 znaków
   EN: Gain 1 Fragile next turn if an ally dies
   PL: jeżeli ginie sojusznik, zyskuje 1 Kruchości w następnej turze
15. [[a1c5p2] Pasywka wroga [9009301] — nazwa] 얽혀있는 유기
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009301].name
   limit: do 40 znaków
   EN: Intertwined Organic Material
   PL: Intertwined Organic Material
16. [[a1c5p2] Pasywka wroga [9009301] — opis] 자신을 제외한 살아있는 아군당 자신의 공격 레벨이 1 증가
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009301].desc
   limit: do 120 znaków
   EN: Offense Level +1 for every surviving ally (not counting this unit)
   PL: Poziom Ataku +1 za każdego żyjącego sojusznika (nie licząc tej jednostki)
17. [[a1c5p2] Pasywka wroga [9009302] — nazwa] 헤쳐진 무기
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009302].name
   limit: do 40 znaków
   EN: Scattered Inorganic Material
   PL: Scattered Inorganic Material
18. [[a1c5p2] Pasywka wroga [9009302] — opis] 아군이 죽었다면, 다음 턴에 공격 위력 감소 1 얻음
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009302].desc
   limit: do 120 znaków
   EN: Gain 1 Attack Power Down next turn if an ally dies
   PL: jeżeli ginie sojusznik, zyskuje 1 Spadek Mocy Ataku w następnej turze
19. [[a1c5p2] Pasywka wroga [9009401] — nazwa] 유기적인 호흡
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009401].name
   limit: do 40 znaków
   EN: Organic Breathing
   PL: Organic Breathing
20. [[a1c5p2] Pasywka wroga [9009401] — opis] 자신의 공격으로 적을 처치했다면, 다음 턴에 모든 백화 상태의 아군에게 호흡 5 부여. 호흡 횟수 1 증가
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009401].desc
   limit: do 130 znaków
   EN: If this unit dealt the final blow, apply 5 Poise to all Pallidified allies. Apply 1 Poise Count
   PL: jeżeli to ta jednostka zadała cios kończący, nakłada 5 Oddechu wszystkim Zbielałym sojusznikom. Nakłada 1 Licznika Oddechu
21. [[a1c5p2] Pasywka wroga [9009501] — nazwa] 유기적인 경화
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009501].name
   limit: do 40 znaków
   EN: Organic Hardening
   PL: Organic Hardening
22. [[a1c5p2] Pasywka wroga [9009501] — opis] 자신의 공격으로 적을 처치했다면, 다음 턴에 모든 아군에게 보호 1, 방어 레벨 증가 2 부여
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009501].desc
   limit: do 120 znaków
   EN: If this unit dealt the final blow, apply 1 Protection and 2 Defense Level Up to all allies.
   PL: jeżeli to ta jednostka zadała cios kończący, nakłada 1 Ochrony i 2 Wzrost Poziomu Obrony wszystkim sojusznikom.
23. [[a1c5p2] Pasywka wroga [9009601] — nazwa] 원한 문신
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009601].name
   limit: do 40 znaków
   EN: Vengeance Tattoo
   PL: Vengeance Tattoo
24. [[a1c5p2] Pasywka wroga [9009601] — opis] 이번 전투에서 중지 소속 아군이 사망할 때마다 공격 레벨 증가 1을 얻음 (최대 5)
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009601].desc
   limit: do 120 znaków
   EN: Every time a Middle ally is killed in this encounter, gain 1 Offense Level Up (Max 5)
   PL: za każdego sojusznika Środkowego pokonanego w tej walce zyskuje 1 Wzrost Poziomu Ataku (maks. 5)
25. [[a1c5p2] Pasywka wroga [9009602] — nazwa] 사소한 원한
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009602].name
   limit: do 40 znaków
   EN: Little Vengeance
   PL: Little Vengeance
26. [[a1c5p2] Pasywka wroga [9009602] — opis] 합 패배시 다음 턴에 빼기 코인 강화 1얻음 (턴 당 최대 2번)
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009602].desc
   limit: do 120 znaków
   EN: Upon Clash Lose, gain 1 Minus Coin Boost next turn (2 times per turn)
   PL: po przegranej w Starciu zyskuje 1 Wzmocnienia Monet Minus w następnej turze (2 razy na turę)
27. [[a1c5p2] Pasywka wroga [9009603] — nazwa] 배로 갚기
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009603].name
   limit: do 40 znaków
   EN: Multifold Retribution
   PL: Multifold Retribution
28. [[a1c5p2] Pasywka wroga [9009603] — opis] 체력이 20%이하일 때, 배로 갚기를 사용한다. (웨이브당 한 번)
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009603].desc
   limit: do 120 znaków
   EN: Use "Multifold Retribution' at 20% or less HP. (Once per wave)
   PL: używa „Multifold Retribution” przy HP równym 20% lub mniej. (1 raz na falę)
29. [[a1c5p2] Pasywka wroga [9009604] — nazwa] 의리 사슬
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009604].name
   limit: do 40 znaków
   EN: Chains of Loyalty
   PL: Chains of Loyalty
30. [[a1c5p2] Pasywka wroga [9009604] — opis] 중지 소속 아군 사망 시 다음 턴에 더하기 코인 강화 1을 얻음.
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9009604].desc
   limit: do 120 znaków
   EN: When a Middle ally is killed, gain 1 Plus Coin Boost next turn.
   PL: gdy ginie sojusznik Środkowego, zyskuje 1 Wzmocnienia Monet Plus w następnej turze.
31. [[a1c5p2] Pasywka wroga [809901] — nazwa] 작은 형님
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=809901].name
   limit: do 40 znaków
   EN: The Big Brother
   PL: The Big Brother
32. [[a1c5p2] Pasywka wroga [809901] — opis] 턴 시작 시 자신을 포함한 모든 아군의 정신력 10 회복
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=809901].desc
   limit: do 120 znaków
   EN: All allies heal 10 SP at Turn Start
   PL: Początek tury: wszyscy sojusznicy (łącznie z tą jednostką) przywracają 10 SP
33. [[a1c5p2] Pasywka wroga [809902] — nazwa] 의리 사슬
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=809902].name
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
34. [[a1c5p2] Pasywka wroga [809902] — opis] 중지 소속 아군 사망 시 다음 턴에 더하기 코인 강화 1을 얻음. (최대 2)
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=809902].desc
   limit: do 120 znaków
   EN: When an ally from the Middle is killed, gain 1 Plus Coin Boost next turn. (Max 2)
   PL: gdy ginie sojusznik Środkowego, zyskuje 1 Wzmocnienia Monet Plus w następnej turze. (maks. 2)
35. [[a1c5p2] Pasywka wroga [809903] — nazwa] 위압
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=809903].name
   limit: do 40 znaków
   EN: Domineer
   PL: Domineer
36. [[a1c5p2] Pasywka wroga [809903] — opis] 자신을 공격한 대상이 스킬 피해로 자신에게 체력 피해를 12 이상 입히지 못한 경우, 대상의 정신력 10 감소
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=809903].desc
   limit: do 150 znaków
   EN: If an enemy that attacked this unit fails to deal more than 12 HP damage with their Skill, the enemy loses 10 SP
   PL: jeżeli wróg atakujący tę jednostkę nie zada jej ponad 12 obrażeń HP Umiejętnością, traci 10 SP
37. [[a1c5p2] Pasywka wroga [809904] — nazwa] 머리 털기
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=809904].name
   limit: do 40 znaków
   EN: Brush it Off
   PL: Brush it Off
38. [[a1c5p2] Pasywka wroga [809904] — opis] 패닉 상태가 되면, 다음 턴 시작 시 패닉 상태를 해제하고, 정신력이 0으로 초기화 됨.
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=809904].desc
   limit: do 120 znaków
   EN: When in panic, recover from panic at the start of the next turn and reset SP to 0.
   PL: gdy przechodzi w Panikę, na początku następnej tury dochodzi do siebie z Paniki i jej SP wraca do 0.
39. [[a1c5p2] Pasywka wroga [809905] — nazwa] 퍼석해져버린 머리
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=809905].name
   limit: do 40 znaków
   EN: In the World of Bristly
   PL: In the World of Bristly
40. [[a1c5p2] Pasywka wroga [809905] — opis] 합에서 3회 패배하면, 다음 턴에 방어 레벨 감소 6를 얻음
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=809905].desc
   limit: do 120 znaków
   EN: Gain 6 Defense Level Down next turn after losing a Clash 3 times
   PL: po 3 przegranych Starciach zyskuje 6 Spadek Poziomu Obrony w następnej turze
41. [[a1c5p2] Pasywka wroga [9008904] — opis] 정신력이 -20인 상태로 전투에 참전함.
   źródło: Passives_Enemy-a1c5p2.json :: dataList[id=9008904].desc
   limit: do 120 znaków
   EN: Begins encounter with -20 SP.
   PL: rozpoczyna tę walkę z -20 SP.

## [a1c5p3] Wróg / część: Enemies-a1c5p3
- plik gry: `Enemies-a1c5p3.json`

42. [[a1c5p3] Wróg / część [8100] — nazwa] 살갗 예언자
   źródło: Enemies-a1c5p3.json :: dataList[id=8100].name
   limit: do 40 znaków
   EN: Skin Prophet
   PL: Skin Prophet
43. [[a1c5p3] Wróg / część [8100] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=8100].desc
   limit: do 120 znaków
   EN: Core
   PL: Core
44. [[a1c5p3] Wróg / część [810001] — nazwa] 몸통
   źródło: Enemies-a1c5p3.json :: dataList[id=810001].name
   limit: do 40 znaków
   EN: Body
   PL: Korpus
45. [[a1c5p3] Wróg / część [810001] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=810001].desc
   limit: do 120 znaków
   EN: Part
   PL: Część
46. [[a1c5p3] Wróg / część [8107] — nazwa] 촛불
   źródło: Enemies-a1c5p3.json :: dataList[id=8107].name
   limit: do 40 znaków
   EN: Candle
   PL: Candle
47. [[a1c5p3] Wróg / część [8107] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=8107].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [[a1c5p3] Wróg / część [810701] — nazwa] 촛불
   źródło: Enemies-a1c5p3.json :: dataList[id=810701].name
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [[a1c5p3] Wróg / część [810701] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=810701].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
50. [[a1c5p3] Wróg / część [8102] — nazwa] 꿈먹는 탁류
   źródło: Enemies-a1c5p3.json :: dataList[id=8102].name
   limit: do 40 znaków
   EN: Dream-Devouring Siltcurrent
   PL: Dream-Devouring Siltcurrent
51. [[a1c5p3] Wróg / część [8102] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=8102].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [[a1c5p3] Wróg / część [810201] — nazwa] 몸통
   źródło: Enemies-a1c5p3.json :: dataList[id=810201].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [[a1c5p3] Wróg / część [810201] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=810201].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
54. [[a1c5p3] Wróg / część [810202] — nazwa] 형광등
   źródło: Enemies-a1c5p3.json :: dataList[id=810202].name
   limit: do 40 znaków
   EN: Fluorescence
   PL: Fluorescence
55. [[a1c5p3] Wróg / część [810202] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=810202].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [[a1c5p3] Wróg / część [8108] — nazwa] 표류물
   źródło: Enemies-a1c5p3.json :: dataList[id=8108].name
   limit: do 40 znaków
   EN: Flotsam
   PL: Flotsam
57. [[a1c5p3] Wróg / część [8108] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=8108].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [[a1c5p3] Wróg / część [810801] — nazwa] 표류물
   źródło: Enemies-a1c5p3.json :: dataList[id=810801].name
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [[a1c5p3] Wróg / część [810801] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=810801].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [[a1c5p3] Wróg / część [8101] — nazwa] 걷는 진주
   źródło: Enemies-a1c5p3.json :: dataList[id=8101].name
   limit: do 40 znaków
   EN: Ambling Pearl
   PL: Ambling Pearl
61. [[a1c5p3] Wróg / część [8101] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=8101].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [[a1c5p3] Wróg / część [810101] — nazwa] 껍질
   źródło: Enemies-a1c5p3.json :: dataList[id=810101].name
   limit: do 40 znaków
   EN: Shell
   PL: Shell
63. [[a1c5p3] Wróg / część [810101] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=810101].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [[a1c5p3] Wróg / część [810102] — nazwa] 진주
   źródło: Enemies-a1c5p3.json :: dataList[id=810102].name
   limit: do 40 znaków
   EN: Pearl
   PL: Pearl
65. [[a1c5p3] Wróg / część [810102] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=810102].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [[a1c5p3] Wróg / część [8109] — nazwa] 녹색 점액
   źródło: Enemies-a1c5p3.json :: dataList[id=8109].name
   limit: do 40 znaków
   EN: Green Slime
   PL: Green Slime
67. [[a1c5p3] Wróg / część [8109] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=8109].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [[a1c5p3] Wróg / część [810901] — nazwa] 녹색 점액
   źródło: Enemies-a1c5p3.json :: dataList[id=810901].name
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [[a1c5p3] Wróg / część [810901] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=810901].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [[a1c5p3] Wróg / część [8103] — nazwa] ???
   źródło: Enemies-a1c5p3.json :: dataList[id=8103].name
   limit: do 40 znaków
   EN: ???
   PL: ???
71. [[a1c5p3] Wróg / część [8103] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=8103].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [[a1c5p3] Wróg / część [810301] — nazwa] 몸통
   źródło: Enemies-a1c5p3.json :: dataList[id=810301].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [[a1c5p3] Wróg / część [810301] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=810301].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [[a1c5p3] Wróg / część [81032] — nazwa] ???
   źródło: Enemies-a1c5p3.json :: dataList[id=81032].name
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [[a1c5p3] Wróg / część [81032] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=81032].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [[a1c5p3] Wróg / część [8110] — nazwa] 눈이 먼 피쿼드타운 주민
   źródło: Enemies-a1c5p3.json :: dataList[id=8110].name
   limit: do 40 znaków
   EN: Blinded Pequod Town Villager
   PL: Blinded Pequod Town Villager
77. [[a1c5p3] Wróg / część [8110] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=8110].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [[a1c5p3] Wróg / część [811001] — nazwa] 몸통
   źródło: Enemies-a1c5p3.json :: dataList[id=811001].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [[a1c5p3] Wróg / część [811001] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=811001].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [[a1c5p3] Wróg / część [8111] — nazwa] 입이 막힌 피쿼드타운 주민
   źródło: Enemies-a1c5p3.json :: dataList[id=8111].name
   limit: do 40 znaków
   EN: Gagged Pequod Town Villager
   PL: Gagged Pequod Town Villager
81. [[a1c5p3] Wróg / część [8111] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=8111].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [[a1c5p3] Wróg / część [811101] — nazwa] 몸통
   źródło: Enemies-a1c5p3.json :: dataList[id=811101].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [[a1c5p3] Wróg / część [811101] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=811101].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [[a1c5p3] Wróg / część [90098] — nazwa] 눈이 먼 피쿼드타운 주민
   źródło: Enemies-a1c5p3.json :: dataList[id=90098].name
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [[a1c5p3] Wróg / część [90098] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=90098].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [[a1c5p3] Wróg / część [90099] — nazwa] 입이 막힌 피쿼드타운 주민
   źródło: Enemies-a1c5p3.json :: dataList[id=90099].name
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [[a1c5p3] Wróg / część [90099] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=90099].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [[a1c5p3] Wróg / część [8104] — nazwa] 스타벅
   źródło: Enemies-a1c5p3.json :: dataList[id=8104].name
   limit: do 40 znaków
   EN: Starbuck
   PL: Starbuck
89. [[a1c5p3] Wróg / część [8104] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=8104].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [[a1c5p3] Wróg / część [810401] — nazwa] 몸통
   źródło: Enemies-a1c5p3.json :: dataList[id=810401].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [[a1c5p3] Wróg / część [810401] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=810401].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [[a1c5p3] Wróg / część [8105] — nazwa] 에이해브
   źródło: Enemies-a1c5p3.json :: dataList[id=8105].name
   limit: do 40 znaków
   EN: Ahab
   PL: Ahab
93. [[a1c5p3] Wróg / część [8105] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=8105].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [[a1c5p3] Wróg / część [810501] — nazwa] 몸통
   źródło: Enemies-a1c5p3.json :: dataList[id=810501].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [[a1c5p3] Wróg / część [810501] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=810501].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [[a1c5p3] Wróg / część [81052] — nazwa] 에이해브
   źródło: Enemies-a1c5p3.json :: dataList[id=81052].name
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [[a1c5p3] Wróg / część [81052] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=81052].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [[a1c5p3] Wróg / część [8106] — nazwa] 개화 E.G.O::가스하푼
   źródło: Enemies-a1c5p3.json :: dataList[id=8106].name
   limit: do 50 znaków
   EN: Effloresced E.G.O::GasHarpoon
   PL: Effloresced E.G.O::GasHarpoon
99. [[a1c5p3] Wróg / część [8106] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=8106].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [[a1c5p3] Wróg / część [810601] — nazwa] 몸통
   źródło: Enemies-a1c5p3.json :: dataList[id=810601].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [[a1c5p3] Wróg / część [810601] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=810601].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [[a1c5p3] Wróg / część [8112] — nazwa] 퀴케그
   źródło: Enemies-a1c5p3.json :: dataList[id=8112].name
   limit: do 40 znaków
   EN: Queequeg
   PL: Queequeg
103. [[a1c5p3] Wróg / część [8112] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=8112].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [[a1c5p3] Wróg / część [811201] — nazwa] 몸통
   źródło: Enemies-a1c5p3.json :: dataList[id=811201].name
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [[a1c5p3] Wróg / część [811201] — opis] 부위
   źródło: Enemies-a1c5p3.json :: dataList[id=811201].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [[a1c5p3] Wróg / część [81062] — nazwa] 개화 E.G.O::가스하푼
   źródło: Enemies-a1c5p3.json :: dataList[id=81062].name
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [[a1c5p3] Wróg / część [81062] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=81062].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [[a1c5p3] Wróg / część [81063] — nazwa] 개화 E.G.O::가스하푼
   źródło: Enemies-a1c5p3.json :: dataList[id=81063].name
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [[a1c5p3] Wróg / część [81063] — opis] 본체
   źródło: Enemies-a1c5p3.json :: dataList[id=81063].desc
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c5p3] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c5p3
- grupa rozdziału/trybu: `a1c5p3` · plik: `Skills_Abnormality-a1c5p3.json`

110. [Umiejętność wroga [810001] (ulepszenie 1) — nazwa] 분열하리라
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810001].levelList[level=1].name
   limit: do 40 znaków
   EN: All Shall Scatter
   PL: All Shall Scatter
111. [Umiejętność wroga [810001] (ulepszenie 1) — opis] 표식 대상 우선 공격
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810001].levelList[level=1].desc
   limit: do 120 znaków
   EN: Prioritizes enemies with Marked
   PL: priorytet: wrogowie z Oznaczeniem
112. [Umiejętność wroga [810001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 켜진 촛불의 수만큼 정신력 피해
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal SP damage by the number of lit Candles
   PL: [OnSucceedAttack] zadaje obrażeń SP równe liczbie zapalonych Candle
113. [Umiejętność wroga [810001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 켜진 촛불의 수만큼 정신력 피해
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Umiejętność wroga [810002] (ulepszenie 1) — nazwa] 열망하며...
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810002].levelList[level=1].name
   limit: do 40 znaków
   EN: Longing...
   PL: Longing...
115. [Umiejętność wroga [810002] (ulepszenie 1) — opis] 표식 대상 우선 공격
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810002].levelList[level=1].desc
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Umiejętność wroga [810002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 분노 취약 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Wrath Fragility next turn
   PL: [OnSucceedAttack] nakłada 1 Kruchości Gniewu w następnej turze
117. [Umiejętność wroga [810002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Combustion]이 있다면, 화상 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has [Combustion], inflict 4 Burn
   PL: [OnSucceedAttack] jeżeli cel ma [Combustion], nakłada 4 Podpalenia
118. [Umiejętność wroga [810002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 분노 취약 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Umiejętność wroga [810002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [Combustion]이 있다면, 화상 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Umiejętność wroga [810003] (ulepszenie 1) — nazwa] 9장 2절
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810003].levelList[level=1].name
   limit: do 40 znaków
   EN: 9:2
   PL: 9:2
121. [Umiejętność wroga [810003] (ulepszenie 1) — opis] 다음 턴에 모든 촛불을 끔.\n[AaCePcBa]이 있는 대상에게 적중 시 최대 체력의 5%만큼 추가 감소.\n[DefeatDuel] 화상 10 부여. 대상에게 다음 턴에 표식 부여.\n[EndBattle] 모든 촛불 체력 최대치까지 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810003].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [AaCePcBa], [DefeatDuel], [EndBattle]
   znaczenie tagów: [AaCePcBa] = 표식 / Marked; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: Snuffs out all Candles next turn.\nUpon hitting targets with [AaCePcBa], target loses additional 5% of its max HP.\n[DefeatDuel] Inflict 10 Burn. Inflict target with Marked next turn.\n[EndBattle] All Candles heal to max HP.
   PL: gaśnie wszystkie Candle w następnej turze.\nprzy trafieniu celu z [AaCePcBa] odbiera mu dodatkowo 5% Maks. HP.\n[DefeatDuel] nakłada 10 Podpalenia. Nakłada na cel w następnej turze Oznaczenie.\n[EndBattle] przywraca wszystkie Candle do Maks. HP
122. [Umiejętność wroga [810003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 최대 체력을 10%만큼 감소.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target's max HP decreases by 10%.
   PL: [OnSucceedAttack] zmniejsza Maks. HP celu o 10%.
123. [Umiejętność wroga [810003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 화상 5 부여, 화상 횟수 2 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Burn and +2 Burn Count
   PL: [OnSucceedAttack] nakłada 5 Podpalenia i 2 Licznika Podpalenia
124. [Umiejętność wroga [810003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 최대 체력을 10%만큼 감소.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Umiejętność wroga [810003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 화상 5 부여, 화상 횟수 2 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Umiejętność wroga [810004] (ulepszenie 1) — nazwa] 6장 5절
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810004].levelList[level=1].name
   limit: do 40 znaków
   EN: 6:5
   PL: 6:5
127. [Umiejętność wroga [810004] (ulepszenie 1) — opis] [CantDuel][CantChangeTarget]\n대상의 피해를 자신이 받음. 다음 턴에 흐트러짐.\n[AaCePcBa]이 없는 무작위 적에게 다음 턴에 표식 부여.\n[EndBattle] 모든 촛불 체력 최대치까지 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810004].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [AaCePcBa], [EndBattle]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [AaCePcBa] = 표식 / Marked; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [CantDuel][CantChangeTarget]\nTake damage in the target's place. Get staggered next turn.\nInflict Marked on a random enemy without [AaCePcBa].\n[EndBattle] All Candles heal to max HP
   PL: [CantDuel][CantChangeTarget]\nprzyjmuje obrażenia zamiast celu. Przechodzi w Oszołamienie w następnej turze.\nnakłada w następnej turze Oznaczenie na losowego wroga bez [AaCePcBa].\n[EndBattle] przywraca wszystkie Candle do Maks. HP
128. [Umiejętność wroga [810004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 최대 체력을 10%만큼 감소.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] This unit's max HP decreases by 10%.
   PL: [OnSucceedAttack] zmniejsza Maks. HP tej jednostki o 10%.
129. [Umiejętność wroga [810004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신에게 화상 10 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 10 Burn on self
   PL: [OnSucceedAttack] nakłada 10 Podpalenia na siebie
130. [Umiejętność wroga [810004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 최대 체력을 10%만큼 감소.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Umiejętność wroga [810004] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신에게 화상 10 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810004].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Umiejętność wroga [810005] (ulepszenie 1) — nazwa] 드러낼지어다
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810005].levelList[level=1].name
   limit: do 40 znaków
   EN: All Shall be Revealed
   PL: All Shall be Revealed
133. [Umiejętność wroga [810005] (ulepszenie 1) — opis] [CantDuel]
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810005].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel]
   PL: [CantDuel]
134. [Umiejętność wroga [810005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 분노 취약 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Wrath Fragility
   PL: [OnSucceedAttack] nakłada 1 Kruchości Gniewu
135. [Umiejętność wroga [810006] (ulepszenie 1) — nazwa] 타오를지니
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810006].levelList[level=1].name
   limit: do 40 znaków
   EN: All Shall Burn
   PL: All Shall Burn
136. [Umiejętność wroga [810006] (ulepszenie 1) — opis] [CantDuel]
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810006].levelList[level=1].desc
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Umiejętność wroga [810006] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Combustion]이 있다면, 화상 3 부여.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has [Combustion], inflict 3 Burn.
   PL: [OnSucceedAttack] jeżeli cel ma [Combustion], nakłada 3 Podpalenia.
138. [Umiejętność wroga [810701] (ulepszenie 1) — nazwa] 피워진 불씨
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810701].levelList[level=1].name
   limit: do 40 znaków
   EN: Sparked Flame
   PL: Sparked Flame
139. [Umiejętność wroga [810701] (ulepszenie 1) — opis] [AaCePcBa]이 있는 대상 우선 공격
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AaCePcBa]
   znaczenie tagów: [AaCePcBa] = 표식 / Marked
   EN: Prioritizes targets with [AaCePcBa]
   PL: priorytet: cele z [AaCePcBa]
140. [Umiejętność wroga [810701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 6 부여, 화상 횟수 2 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 6 Burn and +2 Burn Count
   PL: [OnSucceedAttack] nakłada 6 Podpalenia i 2 Licznika Podpalenia
141. [Umiejętność wroga [810702] (ulepszenie 1) — nazwa] 꺼지지 않도록
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810702].levelList[level=1].name
   limit: do 40 znaków
   EN: So That It Will Burn
   PL: So That It Will Burn
142. [Umiejętność wroga [810702] (ulepszenie 1) — opis] [StartBattle] 보호막 20을 얻음\n보호막이 모두 소진되면, 다음 턴에 불이 꺼진다.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 20 Shield\nSnuff out the lights next turn when out of Shield
   PL: [StartBattle] zyskuje 20 Tarczy\ngdy Tarcza zostanie całkowicie wyczerpana, światło gaśnie w następnej turze
143. [Umiejętność wroga [810702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 1, 화상 횟수 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Burn and +1 Burn Count
   PL: [OnSucceedAttack] nakłada 1 Podpalenia i 1 Licznika Podpalenia
144. [Umiejętność wroga [810101] (ulepszenie 1) — nazwa] 독성 점액
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810101].levelList[level=1].name
   limit: do 40 znaków
   EN: Toxic Fluid
   PL: Toxic Fluid
145. [Umiejętność wroga [810101] (ulepszenie 1) — opis] [StartBattle] 녹색 점액 1 감소
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Consume 1 Green Slime
   PL: [StartBattle] zużywa 1 Green Slime
146. [Umiejętność wroga [810101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 독 3 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Poison
   PL: [OnSucceedAttack] nakłada 3 Zatrucia
147. [Umiejętność wroga [810101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 독 3 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Umiejętność wroga [810102] (ulepszenie 1) — nazwa] 부식 점액
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810102].levelList[level=1].name
   limit: do 40 znaków
   EN: Corrosive Fluid
   PL: Corrosive Fluid
149. [Umiejętność wroga [810102] (ulepszenie 1) — opis] [StartBattle] 녹색 점액 1 감소
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810102].levelList[level=1].desc
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Umiejętność wroga [810102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Poison]만큼 방어 레벨 감소 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Poison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Poison] = 독 / Poison
   EN: [OnSucceedAttack] Inflict Defense Level Down by [Poison] on target
   PL: [OnSucceedAttack] nakłada na cel Spadek Poziomu Obrony w liczbie [Poison]
151. [Umiejętność wroga [810102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 유충 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Larva
   PL: [OnSucceedAttack] nakłada 1 Larwy
152. [Umiejętność wroga [810102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Poison]만큼 방어 레벨 감소 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
153. [Umiejętność wroga [810102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 유충 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Umiejętność wroga [810103] (ulepszenie 1) — nazwa] 마비 액체
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810103].levelList[level=1].name
   limit: do 40 znaków
   EN: Paralytic Fluid
   PL: Paralytic Fluid
155. [Umiejętność wroga [810103] (ulepszenie 1) — opis] [StartBattle] 녹색 점액 1 감소
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810103].levelList[level=1].desc
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Umiejętność wroga [810103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Poison]이 있다면, 마비 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Poison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Poison] = 독 / Poison
   EN: [OnSucceedAttack] If target has [Poison], inflict 1 Paralyze
   PL: [OnSucceedAttack] jeżeli cel ma [Poison], nakłada 1 Paraliżu
157. [Umiejętność wroga [810103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 유충 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Larva
   PL: [OnSucceedAttack] nakłada 2 Larw
158. [Umiejętność wroga [810103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Poison]이 있다면, 마비 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Umiejętność wroga [810103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 유충 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Umiejętność wroga [810104] (ulepszenie 1) — nazwa] 잠식 액체
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810104].levelList[level=1].name
   limit: do 40 znaków
   EN: Devouring Fluid
   PL: Devouring Fluid
161. [Umiejętność wroga [810104] (ulepszenie 1) — opis] [StartBattle] 녹색 점액 2 감소\n[WhenUse] 유충 3 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Consume 2 Green Slime\n[WhenUse] Inflict 3 Larva
   PL: [StartBattle] zużywa 2 Green Slime\n[WhenUse] nakłada 3 Larw
162. [Umiejętność wroga [810104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 독 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Poison
   PL: [OnSucceedAttack] nakłada 4 Zatrucia
163. [Umiejętność wroga [810104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Paralyze next turn
   PL: [OnSucceedAttackHead] nakłada 1 Paraliżu w następnej turze
164. [Umiejętność wroga [810104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 독 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Umiejętność wroga [810104] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 마비 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810104].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Umiejętność wroga [810105] (ulepszenie 1) — nazwa] 들끓는 녹색 점액
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810105].levelList[level=1].name
   limit: do 40 znaków
   EN: Effervescent Green Slime
   PL: Effervescent Green Slime
167. [Umiejętność wroga [810105] (ulepszenie 1) — opis] [StartBattle] [AaCePcBh]만큼 공격 가중치가 증가\n[StartBattle] [AaCePcBh]을 10 얻음.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810105].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [AaCePcBh]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AaCePcBh] = 녹색 점액 / Green Slime
   EN: [StartBattle] Gain Atk Weight by [AaCePcBh]\n[StartBattle] Gain 10 [AaCePcBh]
   PL: [StartBattle] zyskuje Wagę Ataku równą [AaCePcBh]\n[StartBattle] zyskuje 10 [AaCePcBh].
168. [Umiejętność wroga [810105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 독 10 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 10 Poison
   PL: [OnSucceedAttack] nakłada 10 Zatrucia
169. [Umiejętność wroga [810105] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 7 감소
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lose 7 SP
   PL: [OnSucceedAttack] cel traci 7 SP
170. [Umiejętność wroga [810105] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 유충 3 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810105].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Larva
   PL: [OnSucceedAttack] nakłada 3 Larw
171. [Umiejętność wroga [810105] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttackHead] 다음 턴에 마비 1, 방어 레벨 감소 3 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810105].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Paralyze and 3 Defense Level Down next turn
   PL: [OnSucceedAttackHead] nakłada 1 Paraliżu i 3 Spadek Poziomu Obrony w następnej turze
172. [Umiejętność wroga [810106] (ulepszenie 1) — nazwa] 포식
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810106].levelList[level=1].name
   limit: do 40 znaków
   EN: Predation
   PL: Predation
173. [Umiejętność wroga [810106] (ulepszenie 1) — opis] [CantDuel][CantChangeTarget]\n녹색 점액을 우선 공격\n녹색 점액을 공격 시 처치한다.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810106].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]
   EN: [CantDuel][CantChangeTarget]\nTargets Green Slime primarily\nDefeats Green Slime upon attacking
   PL: [CantDuel][CantChangeTarget]\npriorytet: Green Slime\npokonuje Green Slime przy ataku
174. [Umiejętność wroga [810106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [TargetKill] [AaCePcBh]을 3 얻음.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TargetKill], [AaCePcBh]
   znaczenie tagów: [TargetKill] = [대상 처치 시] / [On Target Kill]; [AaCePcBh] = 녹색 점액 / Green Slime
   EN: [TargetKill] Gain 3 [AaCePcBh].
   PL: [TargetKill] zyskuje 3 [AaCePcBh].
175. [Umiejętność wroga [810107] (ulepszenie 1) — nazwa] 흘러넘친 독
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810107].levelList[level=1].name
   limit: do 40 znaków
   EN: Overflowing Poison
   PL: Overflowing Poison
176. [Umiejętność wroga [810107] (ulepszenie 1) — opis] [OnSucceedEvade] 대상에게 독 5 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810107].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Inflict 5 Poison
   PL: [OnSucceedEvade] nakłada 5 Zatrucia na cel
177. [Umiejętność wroga [810201] (ulepszenie 1) — nazwa] 박치기
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810201].levelList[level=1].name
   limit: do 40 znaków
   EN: Headbutt
   PL: Headbutt
178. [Umiejętność wroga [810201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Sinking
   PL: [OnSucceedAttack] nakłada 4 Zatonięcia
179. [Umiejętność wroga [810202] (ulepszenie 1) — nazwa] 들이박기
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810202].levelList[level=1].name
   limit: do 40 znaków
   EN: Pound
   PL: Pound
180. [Umiejętność wroga [810202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 3 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Sinking Count
   PL: [OnSucceedAttack] nakłada 3 Licznika Zatonięcia
181. [Umiejętność wroga [810202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 3 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Umiejętność wroga [810203] (ulepszenie 1) — nazwa] 짓누르기
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810203].levelList[level=1].name
   limit: do 40 znaków
   EN: Press
   PL: Press
183. [Umiejętność wroga [810203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL: [OnSucceedAttack] nakłada 4 [Sinking]
184. [Umiejętność wroga [810203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [AaCePcBb]이 있다면, 침잠 횟수 2 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AaCePcBb]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AaCePcBb] = 형광등 파편 / Fluorescence Shard
   EN: [OnSucceedAttack] Inflict +2 Sinking Count if target has [AaCePcBb]
   PL: [OnSucceedAttack] jeżeli cel ma [AaCePcBb], nakłada 2 Licznika Zatonięcia
185. [Umiejętność wroga [810203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Umiejętność wroga [810203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [AaCePcBb]이 있다면, 침잠 횟수 2 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność wroga [810204] (ulepszenie 1) — nazwa] 맹목
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810204].levelList[level=1].name
   limit: do 40 znaków
   EN: Blind Obsession
   PL: Blind Obsession
188. [Umiejętność wroga [810204] (ulepszenie 1) — opis] [DefeatDuel] 자신의 형광등 부위가 부위 전체 체력의 34%만큼 감소.\n[DefeatDuel] 맹목 1을 얻음
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810204].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] This unit's Fluorescence Part loses 34% of Max HP.\n[DefeatDuel] Gain 1 Blind Obsession
   PL: [DefeatDuel] część Fluorescence tej jednostki traci 34% Maks. HP tej części.\n[DefeatDuel] zyskuje 1 Blind Obsession
189. [Umiejętność wroga [810204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 3 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Umiejętność wroga [810204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 침잠 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 4 Sinking
   PL: [OnSucceedAttackHead] nakłada 4 Zatonięcia
191. [Umiejętność wroga [810204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 3 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [810204] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 침잠 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810204].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność wroga [810204] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 침잠 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810204].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Umiejętność wroga [810204] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 침잠 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810204].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Umiejętność wroga [810204] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 침잠쇄도
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810204].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Sinking Deluge
   PL: [OnSucceedAttack] Zatonięcie: Powódź
196. [Umiejętność wroga [810205] (ulepszenie 1) — nazwa] 덮쳐오는 탁류
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810205].levelList[level=1].name
   limit: do 40 znaków
   EN: Crashing Siltcurrent
   PL: Crashing Siltcurrent
197. [Umiejętność wroga [810205] (ulepszenie 1) — opis] [CantDuel][StartBattle] 지형을 변화시킴
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810205].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CantDuel], [StartBattle]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [CantDuel][StartBattle] Alters the environment
   PL: [CantDuel][StartBattle] zmienia teren
198. [Umiejętność wroga [810205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여, 침잠 횟수 2 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Sinking and +2 Sinking Count
   PL: [OnSucceedAttack] nakłada 3 Zatonięcia i 2 Licznika Zatonięcia
199. [Umiejętność wroga [810205] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 정신력 감소 효율 -2
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810205].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain -2 SP Loss Efficiency next turn
   PL: [OnSucceedAttackHead] zyskuje -2 Wydajności utraty Poczytalności w następnej turze
200. [Umiejętność wroga [810205] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여, 침잠 횟수 2 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810205].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 198 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Umiejętność wroga [810206] (ulepszenie 1) — nazwa] 길잃은 맹목
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810206].levelList[level=1].name
   limit: do 40 znaków
   EN: Wayward Blind Obsession
   PL: Wayward Blind Obsession
202. [Umiejętność wroga [810206] (ulepszenie 1) — opis] [CantDuel][CantChangeTarget] 파괴된 표류물을 공격\n[EndSkill] 자신의 형광등 부위가 부위 전체 체력의 34%만큼 감소.\n[EndBattle] 맹목 1을 얻음.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810206].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [EndSkill], [EndBattle]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [EndSkill] = [공격 종료시] / [Attack End]; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [CantDuel][CantChangeTarget] Targets destroyed Flotsam\n[EndSkill] Fluorescence Part loses 34% of Max HP.\n[EndBattle] Gain 1 Blind Obsession.
   PL: [CantDuel][CantChangeTarget] atakuje zniszczone Flotsam\n[EndSkill] część Fluorescence tej jednostki traci 34% Maks. HP tej części.\n[EndBattle] zyskuje 1 Blind Obsession.
203. [Umiejętność wroga [810206] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상을 파괴함.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Destroys target.
   PL: [OnSucceedAttack] niszczy cel.
204. [Umiejętność wroga [810207] (ulepszenie 1) — nazwa] 휩쓸기
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810207].levelList[level=1].name
   limit: do 40 znaków
   EN: Sweep
   PL: Sweep
205. [Umiejętność wroga [810207] (ulepszenie 1) — opis] [EndBattle] 표류물을 생성함
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810207].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndBattle]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [EndBattle] Create Flotsam
   PL: [EndBattle] tworzy Flotsam
206. [Umiejętność wroga [810207] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810207].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Umiejętność wroga [810207] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [AaCePcBb]이 있다면, 침잠 횟수 2 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810207].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Umiejętność wroga [810207] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810207].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Umiejętność wroga [810207] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 [AaCePcBb]이 있다면, 침잠 횟수 2 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810207].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Umiejętność wroga [810208] (ulepszenie 1) — nazwa] 몸부림
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810208].levelList[level=1].name
   limit: do 40 znaków
   EN: Wriggle
   PL: Wriggle
211. [Umiejętność wroga [810208] (ulepszenie 1) — opis] [StartBattle] 맹목 전부 소모\n[StartBattle] 모든 표류물과 파괴된 표류물 파괴
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810208].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Spend all Blind Obsession\n[StartBattle] Destroy all Flotsam and destroyed Flotsam
   PL: [StartBattle] zużywa cały Blind Obsession\n[StartBattle] niszczy wszystkie Flotsam i zniszczone Flotsam
212. [Umiejętność wroga [810208] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810208].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Umiejętność wroga [811001] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811001].levelList[level=1].name
   limit: do 40 znaków
   EN: Stab
   PL: Stab
214. [Umiejętność wroga [811001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 4 Bleed
   PL: [OnSucceedAttackHead] nakłada 4 Krwawienia
215. [Umiejętność wroga [811002] (ulepszenie 1) — nazwa] 상처 헤집기
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811002].levelList[level=1].name
   limit: do 40 znaków
   EN: Tear Up Wound
   PL: Tear Up Wound
216. [Umiejętność wroga [811002] (ulepszenie 1) — opis] [WinDuel] 정신력 5 회복.\n대상의 [Laceration]당 피해량 +5%
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Laceration]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Laceration] = 출혈 / Bleed
   EN: [WinDuel] Heal 5 SP.\nDeal +5% damage per [Laceration] on target
   PL: [WinDuel] przywraca 5 SP.\nzadaje +5% obrażeń za każde [Laceration] celu
217. [Umiejętność wroga [811002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL: [OnSucceedAttack] nakłada 2 Krwawienia
218. [Umiejętność wroga [811002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Umiejętność wroga [811002] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność wroga [811003] (ulepszenie 1) — nazwa] 마을을 지켜!
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811003].levelList[level=1].name
   limit: do 40 znaków
   EN: Protect the Town!
   PL: Protect the Town!
221. [Umiejętność wroga [811003] (ulepszenie 1) — opis] [WhenUse] 호흡 5를 얻음
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811003].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 5 Poise
   PL: [WhenUse] zyskuje 5 Oddechu
222. [Umiejętność wroga [811003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +1 Poise Count
   PL: [OnSucceedAttack] zyskuje 1 Licznika Oddechu
223. [Umiejętność wroga [811003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 4 SP
   PL: [OnSucceedAttack] przywraca 4 SP
224. [Umiejętność wroga [811003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Umiejętność wroga [811003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność wroga [811003] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność wroga [811003] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811003].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
228. [Umiejętność wroga [811003] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811003].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Umiejętność wroga [811003] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811003].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Umiejętność wroga [811004] (ulepszenie 1) — nazwa] 결박용 투창
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811004].levelList[level=1].name
   limit: do 40 znaków
   EN: Tangling Javelin
   PL: Tangling Javelin
231. [Umiejętność wroga [811004] (ulepszenie 1) — opis] [WhenUse] 호흡 5, 호흡 횟수 2를 얻음
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 5 Poise and +2 Poise Count
   PL: [WhenUse] zyskuje 5 Oddechu i 2 Licznika Oddechu
232. [Umiejętność wroga [811004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 결박 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Tangle
   PL: [OnSucceedAttack] nakłada Splątanie
233. [Umiejętność wroga [811004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind next turn
   PL: [OnSucceedAttack] nakłada 2 Wiązania w następnej turze
234. [Umiejętność wroga [811005] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811005].levelList[level=1].name
   limit: do 40 znaków
   EN: Guard
   PL: Guard
235. [Umiejętność wroga [811005] (ulepszenie 1) — opis] 보호막이 있는 동안 피격 시, 다음 턴 공격 레벨 증가 1을 얻음.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811005].levelList[level=1].desc
   limit: do 120 znaków
   EN: When attacked while this unit has Shield, gain 1 Offense Level Up next turn
   PL: przy trafieniu, gdy ta jednostka ma Tarczę, zyskuje 1 Wzrost Poziomu Ataku w następnej turze
236. [Umiejętność wroga [811101] (ulepszenie 1) — nazwa] 연속 찌르기
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811101].levelList[level=1].name
   limit: do 40 znaków
   EN: Quick Jabs
   PL: Quick Jabs
237. [Umiejętność wroga [811101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 2 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +2 Bleed Count
   PL: [OnSucceedAttackHead] nakłada 2 Licznika Krwawienia
238. [Umiejętność wroga [811101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Bleed Count
   PL: [OnSucceedAttackHead] nakłada 1 Licznika Krwawienia
239. [Umiejętność wroga [811102] (ulepszenie 1) — nazwa] 상처 파고들기
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811102].levelList[level=1].name
   limit: do 40 znaków
   EN: Carve Wound
   PL: Carve Wound
240. [Umiejętność wroga [811102] (ulepszenie 1) — opis] [WinDuel] 정신력 5 회복.\n대상의 [Laceration]당 피해량 +5%
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811102].levelList[level=1].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
241. [Umiejętność wroga [811102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Bleed Count
   PL: [OnSucceedAttack] nakłada 1 Licznika Krwawienia
242. [Umiejętność wroga [811102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Umiejętność wroga [811102] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [Umiejętność wroga [811102] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811102].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Umiejętność wroga [811103] (ulepszenie 1) — nazwa] 마을을 지켜!
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811103].levelList[level=1].name
   (powtórzenie elementu 220 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Umiejętność wroga [811103] (ulepszenie 1) — opis] [WhenUse] 호흡 5를 얻음
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811103].levelList[level=1].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność wroga [811103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [Umiejętność wroga [811103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Umiejętność wroga [811103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Umiejętność wroga [811103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Umiejętność wroga [811103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Umiejętność wroga [811103] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811103].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Umiejętność wroga [811103] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811103].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Umiejętność wroga [811103] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811103].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Umiejętność wroga [811104] (ulepszenie 1) — nazwa] 포획용 투창
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811104].levelList[level=1].name
   limit: do 40 znaków
   EN: Capturing Javelin
   PL: Capturing Javelin
256. [Umiejętność wroga [811104] (ulepszenie 1) — opis] [WhenUse] 호흡 5, 호흡 횟수 2를 얻음
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811104].levelList[level=1].desc
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Umiejętność wroga [811104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 포획 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Capture
   PL: [OnSucceedAttack] nakłada Pojmanie
258. [Umiejętność wroga [811104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Umiejętność wroga [811105] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811105].levelList[level=1].name
   limit: do 40 znaków
   EN: Evade
   PL: Evade
260. [Umiejętność wroga [811105] (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 공격 레벨 증가 1을 얻음 (최대 3)
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=811105].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Gain 1 Offense Level Up next turn (Max 3)
   PL: [OnSucceedEvade] zyskuje 1 Wzrost Poziomu Ataku w następnej turze (maks. 3)
261. [Umiejętność wroga [810301] (ulepszenie 1) — nazwa] 사냥 시작
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810301].levelList[level=1].name
   limit: do 40 znaków
   EN: Starting Hunt
   PL: Starting Hunt
262. [Umiejętność wroga [810301] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 아군 4명 소환\n[WhenUse] 다음 턴에 대상에게 사냥감의 징표 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Summon 4 allies next turn\n[WhenUse] Apply Prey Mark next turn
   PL: [StartBattle] przywołuje 4 sojuszników w następnej turze\n[WhenUse] nakłada w następnej turze 1 Znak Ofiary
263. [Umiejętność wroga [810301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] nakłada 4 [Laceration]
264. [Umiejętność wroga [810302] (ulepszenie 1) — nazwa] 작살질
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810302].levelList[level=1].name
   limit: do 40 znaków
   EN: Harpooning
   PL: Harpooning
265. [Umiejętność wroga [810302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 263 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Umiejętność wroga [810303] (ulepszenie 1) — nazwa] 꿰뚫는 작살
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810303].levelList[level=1].name
   limit: do 40 znaków
   EN: Piercing Harpoon
   PL: Piercing Harpoon
267. [Umiejętność wroga [810303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 공격 레벨 감소 3 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Offense Level Down
   PL: [OnSucceedAttack] nakłada 3 Spadek Poziomu Ataku
268. [Umiejętność wroga [810303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Umiejętność wroga [810303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 4 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Bleed
   PL: [OnSucceedAttack] nakłada 4 Krwawienia
270. [Umiejętność wroga [810304] (ulepszenie 1) — nazwa] 심호흡
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810304].levelList[level=1].name
   limit: do 40 znaków
   EN: Deep Breath
   PL: Deep Breath
271. [Umiejętność wroga [810304] (ulepszenie 1) — opis] [StartBattle] 호흡 10, 호흡 횟수 5을 얻음.\n이 스킬에서 크리티컬이 발생하면 호흡 횟수가 감소하지 않음.\n턴 종료 시 자신을 제외하고 생존한 아군 수만큼 다음 턴에 [PlusCoinValueUp]를 얻음.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810304].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [PlusCoinValueUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost
   EN: [StartBattle] Gain 10 Poise and +10 Poise Count.\nCritical Hits do not consume Poise Count with this Skill.\nTurn End: Gain [PlusCoinValueUp] next turn by the number of surviving other allies.
   PL: [StartBattle] zyskuje 10 Oddechu i 10 Licznika Oddechu.\nprzy trafieniu krytycznym tą Umiejętnością Licznik Oddechu nie maleje.\nKoniec tury: zyskuje [PlusCoinValueUp] w następnej turze w liczbie równej liczbie pozostałych żyjących sojuszników.
272. [Umiejętność wroga [810305] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810305].levelList[level=1].name
   limit: do 40 znaków
   EN: Counter
   PL: Counter
273. [Umiejętność wroga [810305] (ulepszenie 1) — opis] 이 스킬에서 크리티컬이 발생하면 호흡 횟수가 감소하지 않음
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810305].levelList[level=1].desc
   limit: do 120 znaków
   EN: Critical Hits do not consume Poise Count with this Skill.
   PL: przy trafieniu krytycznym tą Umiejętnością Licznik Oddechu nie maleje
274. [Umiejętność wroga [810305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 2 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Bleed Count
   PL: [OnSucceedAttack] nakłada 2 Licznika Krwawienia
275. [Umiejętność wroga [810306] (ulepszenie 1) — nazwa] 사냥감 추적
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810306].levelList[level=1].name
   limit: do 40 znaków
   EN: Stalk Prey
   PL: Stalk Prey
276. [Umiejętność wroga [810306] (ulepszenie 1) — opis] 크리티컬 시 피해량 +30%
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810306].levelList[level=1].desc
   limit: do 120 znaków
   EN: +30% Damage on Critical Hit
   PL: zadaje +30% obrażeń przy trafieniu krytycznym
277. [Umiejętność wroga [810306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL: [OnSucceedAttack] nakłada 1 Krwawienia
278. [Umiejętność wroga [810306] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810306].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Umiejętność wroga [810306] (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 피해량의 50%만큼 대상의 첫번째 흐트러짐 구간을 손상
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810306].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Raise target's first Stagger Threshold by 50% of damage dealt
   PL: [CriticalOnSucceedAttack] podnosi pierwszy Próg Oszołomienia celu o 50% zadanych obrażeń
280. [Umiejętność wroga [810306] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 5 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810306].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Bleed
   PL: [OnSucceedAttack] nakłada 5 Krwawień
281. [Umiejętność wroga [810307] (ulepszenie 1) — nazwa] 숨통 끊기
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810307].levelList[level=1].name
   limit: do 40 znaków
   EN: Cut Throat
   PL: Cut Throat
282. [Umiejętność wroga [810307] (ulepszenie 1) — opis] 이 스킬에서 크리티컬이 발생하면 호흡 횟수가 감소하지 않음.\n대상의 [Laceration]당 피해량 +5%\n[WhenUse] 자신에게 호흡이 없는 경우, 턴 종료 시 흐트러짐 상태가 됨.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810307].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: This Skill does not consume Poise Count upon Critical Hit.\nDeal +5% damage for every [Laceration] on target\n[WhenUse] Staggered at Turn End if this unit does not have Poise on self.
   PL: przy trafieniu krytycznym tą Umiejętnością Licznik Oddechu nie maleje.\nzadaje +5% obrażeń za każde [Laceration] celu\n[WhenUse] jeżeli ta jednostka nie ma Oddechu, na koniec tury przechodzi w Oszołamienie.
283. [Umiejętność wroga [810307] (ulepszenie 1) — moneta 1, efekt 1 — opis] 크리티컬 시 피해량 50%
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810307].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: +50% Damage on Critical Hit
   PL: zadaje +50% obrażeń przy trafieniu krytycznym
284. [Umiejętność wroga [810307] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 흐트러짐 상태로 만듦
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810307].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Stagger target next turn
   PL: [OnSucceedAttack] powoduje Oszołamienie celu w następnej turze
285. [Umiejętność wroga [810308] (ulepszenie 1) — nazwa] 깊은 호흡
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810308].levelList[level=1].name
   limit: do 40 znaków
   EN: Deep Breathing
   PL: Deep Breathing
286. [Umiejętność wroga [810308] (ulepszenie 1) — opis] [StartBattle] 호흡 3, 호흡 횟수 5를 얻음.\n이번 턴동안 자신의 호흡 위력만큼 최종 위력이 증가함.\n이번 턴동안 피격 시 호흡 횟수 1 잃음.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810308].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 3 Poise and +5 Poise Count.\nFor this turn, gain Final Power equal to Poise Potency on self.\nFor this turn, lose 1 Poise Count when attacked.
   PL: [StartBattle] zyskuje 3 Oddechu i 5 Licznika Oddechu.\nw tej turze zyskuje Moc Końcową równą Sile Oddechu tej jednostki.\nw tej turze traci 1 Licznika Oddechu przy trafieniu.
287. [Umiejętność wroga [810309] (ulepszenie 1) — nazwa] 생존의 오기
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810309].levelList[level=1].name
   limit: do 40 znaków
   EN: To Survive
   PL: To Survive
288. [Umiejętność wroga [810309] (ulepszenie 1) — opis] 크리티컬 시 피해량 +30%
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810309].levelList[level=1].desc
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Umiejętność wroga [810309] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 본체와 부위의 체력을 피해량의 50%만큼 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810309].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal Core and Part HP by 50% of damage dealt
   PL: [OnSucceedAttack] przywraca HP Korpusu i części równe 50% zadanych obrażeń
290. [Umiejętność wroga [810309] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 본체와 부위의 체력을 피해량의 50%만큼 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810309].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Umiejętność wroga [810309] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 본체와 부위의 체력을 피해량의 50%만큼 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810309].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Umiejętność wroga [810310] (ulepszenie 1) — nazwa] 지켜...야해
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810310].levelList[level=1].name
   limit: do 40 znaków
   EN: Must... Protect
   PL: Must... Protect
293. [Umiejętność wroga [810310] (ulepszenie 1) — opis] [TurnStartBattle] 이 스킬을 사용할 때 자신의 원호 방어 보호막 수치가 0보다 크면 원호 방어가 발동함.\n[StartBattle] 최대 체력의 10%만큼 원호 방어 보호막 을 얻음.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810310].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [TurnStartBattle], [StartBattle]
   znaczenie tagów: [TurnStartBattle] = [턴 시작 시] / [Turn Start]; [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [TurnStartBattle] Upon using this Skill, if this unit has more than 0 Assist Barrier, activate Assist Defense.\n[StartBattle] Gain 10% of max HP as Assist Barrier.
   PL: [TurnStartBattle] przy użyciu tej Umiejętności, jeżeli wartość Bariery Wsparcia tej jednostki jest większa niż 0, uruchamia Obronę Wsparcia.\n[StartBattle] zyskuje Bariery Wsparcia równą 10% Maks. HP.
294. [Umiejętność wroga [810311] (ulepszenie 1) — nazwa] 근성의 작살
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810311].levelList[level=1].name
   limit: do 40 znaków
   EN: Persistent Harpoon
   PL: Persistent Harpoon
295. [Umiejętność wroga [810311] (ulepszenie 1) — opis] 스타벅과 동일한 대상 공격 시 최종 위력 +2
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810311].levelList[level=1].desc
   limit: do 120 znaków
   EN: Final Power +1 when attacking the same target as Starbuck
   PL: Moc Końcowa +1 przy atakowaniu tego samego celu co Starbuck
296. [Umiejętność wroga [810311] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 본체와 부위의 체력을 피해량의 50%만큼 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810311].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Umiejętność wroga [810311] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 결박 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810311].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Umiejętność wroga [810311] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 본체와 부위의 체력을 피해량의 50%만큼 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810311].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność wroga [810312] (ulepszenie 1) — nazwa] 사냥... 끝내야해
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810312].levelList[level=1].name
   limit: do 40 znaków
   EN: Must Finish Hunt...
   PL: Must Finish Hunt...
300. [Umiejętność wroga [810312] (ulepszenie 1) — opis] 이 스킬에서 크리티컬이 발생하면 호흡 횟수가 감소하지 않음.\n대상의 [Laceration]당 피해량 +5%
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810312].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Critical Hits do not consume Poise Count with this Skill.\nDeal +5% damage per [Laceration] on target
   PL: przy trafieniu krytycznym tą Umiejętnością Licznik Oddechu nie maleje.\nzadaje +5% obrażeń za każde [Laceration] celu
301. [Umiejętność wroga [810312] (ulepszenie 1) — moneta 1, efekt 1 — opis] 크리티컬 시 피해량 50%
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810312].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 283 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Umiejętność wroga [810312] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 대상을 흐트러짐 상태로 만듦
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810312].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Stagger target next turn
   PL: [OnSucceedAttack] powoduje Oszołamienie celu w następnej turze
303. [Umiejętność wroga [810401] (ulepszenie 1) — nazwa] 후벼파기
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810401].levelList[level=1].name
   limit: do 40 znaków
   EN: Impale
   PL: Impale
304. [Umiejętność wroga [810401] (ulepszenie 1) — opis] [WhenUse] 호흡 횟수 3 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +3 Poise Count
   PL: [WhenUse] zyskuje 3 Licznika Oddechu
305. [Umiejętność wroga [810401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Umiejętność wroga [810401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Umiejętność wroga [810401] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810401].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Umiejętność wroga [810402] (ulepszenie 1) — nazwa] 뚫어내기
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810402].levelList[level=1].name
   limit: do 40 znaków
   EN: Piercing Thrust
   PL: Piercing Thrust
309. [Umiejętność wroga [810402] (ulepszenie 1) — opis] [WhenUse] 호흡 5를 얻음
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810402].levelList[level=1].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Umiejętność wroga [810402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Fragile next turn
   PL: [OnSucceedAttack] nakłada 1 Kruchości w następnej turze
311. [Umiejętność wroga [810402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 감소 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Defense Level Down next turn
   PL: [OnSucceedAttack] nakłada 2 Spadek Poziomu Obrony w następnej turze
312. [Umiejętność wroga [810402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 이 코인 재사용 1회 (최대 3회)
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Reuse this Coin once (Max 3)
   PL: [OnSucceedAttackHead] używa ponownie tę Monetę 1 raz (maks. 3 razy)
313. [Umiejętność wroga [810403] (ulepszenie 1) — nazwa] 명령을 받들어...
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810403].levelList[level=1].name
   limit: do 40 znaków
   EN: I Follow Orders...
   PL: I Follow Orders...
314. [Umiejętność wroga [810403] (ulepszenie 1) — opis] [TurnStartBattle] 퀴케그의 원호 방어 보호막 수치가 0보다 크면 원호 공격 효과가 발동함
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810403].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TurnStartBattle]
   znaczenie tagów: [TurnStartBattle] = [턴 시작 시] / [Turn Start]
   EN: [TurnStartBattle] If Queequeg has more than 0 Assist Barrier, activate Assist Attack
   PL: [TurnStartBattle] jeżeli wartość Bariery Wsparcia Queequeg jest większa niż 0, uruchamia Atak Wsparcia
315. [Umiejętność wroga [810403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Umiejętność wroga [810404] (ulepszenie 1) — nazwa] 급습
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810404].levelList[level=1].name
   limit: do 40 znaków
   EN: Ambush
   PL: Ambush
317. [Umiejętność wroga [810404] (ulepszenie 1) — opis] 크리티컬 시 피해량 50%\n대상의 [Laceration]당 피해량 +5%
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Deal +50% damage with Critical Hit\nDeal +5% damage per [Laceration] on target
   PL: zadaje +50% obrażeń przy trafieniu krytycznym\nzadaje +5% obrażeń za każde [Laceration] celu
318. [Umiejętność wroga [810404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Bleed Count
   PL: [OnSucceedAttack] nakłada 3 Licznika Krwawienia
319. [Umiejętność wroga [810404] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 피해량의 50%만큼 대상의 첫번째 흐트러짐 구간을 손상
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810404].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Umiejętność wroga [810405] (ulepszenie 1) — nazwa] 두려움의 탄식
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810405].levelList[level=1].name
   limit: do 40 znaków
   EN: Fearful Sigh
   PL: Fearful Sigh
321. [Umiejętność wroga [810405] (ulepszenie 1) — opis] [WhenUse] 호흡 횟수 6 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810405].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +6 Poise Count
   PL: [WhenUse] zyskuje 6 Licznika Oddechu
322. [Umiejętność wroga [810405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Umiejętność wroga [810405] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810405].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Umiejętność wroga [810405] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810405].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Umiejętność wroga [810406] (ulepszenie 1) — nazwa] 투지의 작살
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810406].levelList[level=1].name
   limit: do 40 znaków
   EN: Determined Harpoon
   PL: Determined Harpoon
326. [Umiejętność wroga [810406] (ulepszenie 1) — opis] 퀴케그와 동일한 대상 공격 시 최종 위력 +2
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810406].levelList[level=1].desc
   limit: do 120 znaków
   EN: Final Power +2 when attacking the same target as Queequeg
   PL: Moc Końcowa +2 przy atakowaniu tego samego celu co Queequeg
327. [Umiejętność wroga [810406] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 포획 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810406].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 257 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Umiejętność wroga [810406] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 감소 5 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810406].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Defense Level Down next turn
   PL: [OnSucceedAttack] nakłada 5 Spadek Poziomu Obrony w następnej turze
329. [Umiejętność wroga [810406] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810406].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 310 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Umiejętność wroga [810406] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackTail] 이 코인 재사용 1회 (최대 3회)
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810406].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Reuse this Coin once (Max 3)
   PL: [OnSucceedAttackTail] używa ponownie tę Monetę 1 raz (maks. 3 razy)
331. [Umiejętność wroga [810407] (ulepszenie 1) — nazwa] 나가기 위해서라면...
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810407].levelList[level=1].name
   limit: do 40 znaków
   EN: To Escape...
   PL: To Escape...
332. [Umiejętność wroga [810407] (ulepszenie 1) — opis] 크리티컬 시 피해량 100%\n대상의 [Laceration]당 피해량 +5%
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810407].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Deal +100% damage with Critical Hit\nDeal +5% damage per [Laceration] on target
   PL: zadaje +100% obrażeń przy trafieniu krytycznym\nzadaje +5% obrażeń za każde [Laceration] celu
333. [Umiejętność wroga [810407] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810407].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Umiejętność wroga [810407] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 피해량의 50%만큼 대상의 첫번째 흐트러짐 구간을 손상
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810407].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Umiejętność wroga [810501] (ulepszenie 1) — nazwa] 내 지시에 복종해
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810501].levelList[level=1].name
   limit: do 40 znaków
   EN: Obey My Orders
   PL: Obey My Orders
336. [Umiejętność wroga [810501] (ulepszenie 1) — opis] [WhenUse] 자신과 자신을 제외하고 정신력이 가장 낮은 아군 1명의 정신력 10 회복
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 10 SP for self and 1 other ally with the least SP
   PL: [WhenUse] przywraca 10 SP sobie i 1 innemu sojusznikowi z najniższym SP
337. [Umiejętność wroga [810502] (ulepszenie 1) — nazwa] 내 주위에 서라!
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810502].levelList[level=1].name
   limit: do 40 znaków
   EN: To Me!
   PL: To Me!
338. [Umiejętność wroga [810502] (ulepszenie 1) — opis] [StartBattle] 퀴케그에게 다음 턴에 원호 방어 명령을 내림. 자신이 흐트러짐 상태가 되면 명령이 취소됨.
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810502].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Order Queequeg to activate Assist Defense next turn. Order is canceled when this unit is Staggered.
   PL: [StartBattle] wydaje Queequeg rozkaz Obrony Wsparcia na następną turę. Rozkaz jest anulowany, gdy ta jednostka przechodzi w Oszołamienie.
339. [Umiejętność wroga [810503] (ulepszenie 1) — nazwa] 끝까지 추적해!
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810503].levelList[level=1].name
   limit: do 40 znaków
   EN: Track Them to the End!
   PL: Track Them to the End!
340. [Umiejętność wroga [810503] (ulepszenie 1) — opis] [StartBattle] 스타벅에게 다음 턴에 원호 공격 명령을 내림. 자신이 흐트러짐 상태가 되면 명령이 취소됨.\n[WhenUse] 다음 턴에 사냥감의 징표 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810503].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Order Starbuck to activate Assist Attack next turn. Order is canceled when this unit is Staggered.\n[WhenUse] Apply 1 Prey Mark next turn
   PL: [StartBattle] wydaje Starbuck rozkaz uruchomienia Ataku Wsparcia w następnej turze. Rozkaz jest anulowany, gdy ta jednostka przechodzi w Oszołamienie.\n[WhenUse] nakłada w następnej turze 1 Znak Ofiary
341. [Umiejętność wroga [810504] (ulepszenie 1) — nazwa] 노련한 작살질
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810504].levelList[level=1].name
   limit: do 40 znaków
   EN: Veteran's Harpoon
   PL: Veteran's Harpoon
342. [Umiejętność wroga [810504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Umiejętność wroga [810504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Umiejętność wroga [810505] (ulepszenie 1) — nazwa] 불 같은 작살
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810505].levelList[level=1].name
   limit: do 40 znaków
   EN: Burning Harpoon
   PL: Burning Harpoon
345. [Umiejętność wroga [810505] (ulepszenie 1) — opis] 메인 공격 대상이 보유한 부정적인 효과 1개당 최종 위력 +1 (최대 5)\n대상의 [Laceration]당 피해량 +5%
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810505].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Final Power +1 for every negative effect on main target (Max 5)\nDeal +5% damage per [Laceration] on target
   PL: Moc Końcowa +1 za każdy negatywny Efekt głównego celu (maks. 5)\nzadaje +5% obrażeń za każde [Laceration] celu
346. [Umiejętność wroga [810505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL: [OnSucceedAttack] nakłada 3 Krwawienia
347. [Umiejętność wroga [810505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Umiejętność wroga [810505] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 출혈만큼 화상 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810505].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Burn by Bleed on target
   PL: [OnSucceedAttack] nakłada celowi Podpalenie równe Krwawieniu celu
349. [Umiejętność wroga [810506] (ulepszenie 1) — nazwa] 바보 같으니!
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810506].levelList[level=1].name
   limit: do 40 znaków
   EN: Foolishness!
   PL: Foolishness!
350. [Umiejętność wroga [810506] (ulepszenie 1) — opis] [WhenUse] 자신의 정신력 5 회복\n[OnSucceedEvade] 대상의 정신력 5 감소
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810506].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [OnSucceedEvade]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [WhenUse] Heal 5 SP\n[OnSucceedEvade] Target loses 5 SP
   PL: [WhenUse] przywraca 5 SP sobie\n[OnSucceedEvade] cel traci 5 SP
351. [Umiejętność wroga [810507] (ulepszenie 1) — nazwa] 숨결을 토해내라!
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810507].levelList[level=1].name
   limit: do 40 znaków
   EN: Exhale!
   PL: Exhale!
352. [Umiejętność wroga [810507] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 사냥감의 징표 1 부여\n[WinDuel] 호흡 4 얻음
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810507].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Inflict 1 Prey Mark next turn\n[WinDuel] Gain 4 Poise
   PL: [WhenUse] nakłada 1 Znak Ofiary w następnej turze\n[WinDuel] zyskuje 4 Oddechu
353. [Umiejętność wroga [810507] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신을 제외한 아군 2명에게 호흡 4 부여.\n아군이 없는 경우, 대신 호흡 횟수 2 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810507].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Apply 4 Poise to 2 other allies.\nIf there are no other allies, gain 2 Poise Count instead.
   PL: [OnSucceedAttack] nakłada 4 Oddechu 2 innym sojusznikom.\njeżeli nie ma innych sojuszników, zamiast tego zyskuje 2 Licznika Oddechu
354. [Umiejętność wroga [810508] (ulepszenie 1) — nazwa] 마지막 공포를 날려주마!
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810508].levelList[level=1].name
   limit: do 40 znaków
   EN: Be Fearless!
   PL: Be Fearless!
355. [Umiejętność wroga [810508] (ulepszenie 1) — opis] [WhenUse] 자신의 정신력 10 회복. 자신을 제외하고 정신력이 가장 높은 아군 1명의 정신력 10 감소
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810508].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 10 SP on self. 1 other ally with the highest SP loses 10 SP
   PL: [WhenUse] przywraca 10 SP sobie. 1 inny sojusznik z najwyższym SP traci 10 SP
356. [Umiejętność wroga [810508] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810508].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Burn Count
   PL: [OnSucceedAttack] nakłada 1 Licznika Podpalenia
357. [Umiejętność wroga [810508] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 자신을 제외한 무작위 아군 1명에게 마비 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810508].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Apply 1 Paralyze to a random other ally next turn
   PL: [OnSucceedAttack] nakłada w następnej turze 1 Paraliżu losowemu innemu sojusznikowi
358. [Umiejętność wroga [810508] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810508].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Umiejętność wroga [810508] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 자신을 제외한 무작위 아군 1명에게 마비 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810508].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 357 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Umiejętność wroga [810508] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 1 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810508].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Umiejętność wroga [810508] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 자신을 제외한 무작위 아군 1명에게 마비 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810508].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 357 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Umiejętność wroga [810509] (ulepszenie 1) — nazwa] 죽음의 담금질
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810509].levelList[level=1].name
   limit: do 40 znaków
   EN: Tempering of Death
   PL: Tempering of Death
363. [Umiejętność wroga [810509] (ulepszenie 1) — opis] [WhenUse] 정신력이 가장 낮은 아군 1명에게 거역할 수 없는 명령 을 내림\n[DefeatDuel] 정신력이 가장 낮은 아군 1명 흐트러짐 손상 20
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810509].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Apply Undefiable Command to 1 ally with the lowest SP\n[DefeatDuel] Raise Stagger Threshold by 20 for 1 ally with the lowest SP
   PL: [WhenUse] wydaje Rozkaz Bez Dyskusji 1 sojusznikowi z najniższym SP\n[DefeatDuel] podnosi Próg Oszołomienia o 20 u 1 sojusznika z najniższym SP
364. [Umiejętność wroga [810509] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 취약 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810509].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Fragile
   PL: [OnSucceedAttack] nakłada 2 Kruchości
365. [Umiejętność wroga [810601] (ulepszenie 1) — nazwa] 덤벼봐라!
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810601].levelList[level=1].name
   limit: do 40 znaków
   EN: Strike Me Down!
   PL: Strike Me Down!
366. [Umiejętność wroga [810601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Umiejętność wroga [810601] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810601].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Umiejętność wroga [810601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Umiejętność wroga [810601] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810601].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Umiejętność wroga [810602] (ulepszenie 1) — nazwa] 찔러 죽이기
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810602].levelList[level=1].name
   limit: do 40 znaków
   EN: Stab to Kill
   PL: Stab to Kill
371. [Umiejętność wroga [810602] (ulepszenie 1) — opis] 최대 체력이 가장 낮은 대상 공격
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810602].levelList[level=1].desc
   limit: do 120 znaków
   EN: Targets the unit with the least Max HP
   PL: priorytet: jednostka z najniższym Maks. HP
372. [Umiejętność wroga [810602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 공격 레벨 감소 6 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 6 Offense Level Down
   PL: [OnSucceedAttack] nakłada 6 Spadek Poziomu Ataku
373. [Umiejętność wroga [810602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Umiejętność wroga [810603] (ulepszenie 1) — nazwa] 불멸의 영혼
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810603].levelList[level=1].name
   limit: do 40 znaków
   EN: Undying Soul
   PL: Undying Soul
375. [Umiejętność wroga [810603] (ulepszenie 1) — opis] 회피 실패 시에도 재사용 (최대 2회)\n[OnDefeatEvade] 핍의 자아 2 감소
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnDefeatEvade]
   znaczenie tagów: [OnDefeatEvade] = [회피 실패시] / [Failed Evade]
   EN: Re-use Evade upon Evade failure (Up to 2 times)\n[OnDefeatEvade] Lose 2 Pip's Ego
   PL: używa ponownie przy nieudanej Uniku (do 2 razy)\n[OnDefeatEvade] traci 2 Pipy
376. [Umiejętność wroga [810604] (ulepszenie 1) — nazwa] 흐릿한 결백
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810604].levelList[level=1].name
   limit: do 40 znaków
   EN: Murky Innocence
   PL: Murky Innocence
377. [Umiejętność wroga [810604] (ulepszenie 1) — opis] [DefeatDuel] 수비 위력 감소 2 얻음. 자신의 정신력 10 감소
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Gain 2 Defense Power Down. Lose 10 SP on self
   PL: [DefeatDuel] zyskuje 2 Spadek Mocy Obrony. Traci 10 SP.
378. [Umiejętność wroga [810604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 창백한 소음 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Pallid Noise
   PL: [OnSucceedAttackHead] nakłada 1 Bladego Szumu
379. [Umiejętność wroga [810604] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 마비 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810604].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Paralyze
   PL: [OnSucceedAttack] nakłada 1 Paraliżu
380. [Umiejętność wroga [810604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 창백한 소음 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 378 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [Umiejętność wroga [810604] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810604].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bind next turn
   PL: [OnSucceedAttack] nakłada 1 Wiązania w następnej turze
382. [Umiejętność wroga [810605] (ulepszenie 1) — nazwa] 죄책감의 무게
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810605].levelList[level=1].name
   limit: do 40 znaków
   EN: Weight of Guilt
   PL: Weight of Guilt
383. [Umiejętność wroga [810605] (ulepszenie 1) — opis] 최대 체력이 가장 낮은 대상 3명 공격\n[StartBattle] 핍의 자아 5당 기본 위력 +2, 공격 가중치 +1\n[WhenUse] 핍의 자아 3 감소
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810605].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]
   EN: Targets 3 units with the least Max HP\n[StartBattle] Gain Base Power +2 and Atk Weight +1 for every 5 Pip's Ego\n[WhenUse] Lose 3 Pip's Ego
   PL: atakuje 3 jednostki z najniższym Maks. HP\n[StartBattle] zyskuje Moc Bazową +2 i Wagę Ataku +1 za każde 5 Pipów\n[WhenUse] traci 3 Pipy
384. [Umiejętność wroga [810605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 창백한 소음 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Pallid Noise
   PL: [OnSucceedAttack] nakłada 1 Bladego Szumu
385. [Umiejętność wroga [810605] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 흐트러짐 손상 30
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810605].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 30
   PL: [OnSucceedAttack] podnosi Próg Oszołomienia o 30
386. [Umiejętność wroga [810605] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 대상의 정신력 10 감소
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810605].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Target loses 10 SP
   PL: [OnSucceedAttackHead] cel traci 10 SP
387. [Umiejętność wroga [810607] (ulepszenie 1) — nazwa] 뒤덮힌 두려움
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810607].levelList[level=1].name
   limit: do 40 znaków
   EN: Swathed Fear
   PL: Swathed Fear
388. [Umiejętność wroga [810607] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 사냥감의 징표 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810607].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Inflict 1 Prey Mark next turn
   PL: [WhenUse] nakłada 1 Znak Ofiary w następnej turze
389. [Umiejętność wroga [810607] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 창백한 소음 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810607].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 378 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Umiejętność wroga [810607] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 출혈 3 부여, 출혈 횟수 4 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810607].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed and +4 Bleed Count
   PL: [OnSucceedAttack] nakłada 3 Krwawienia i 4 Licznika Krwawienia
391. [Umiejętność wroga [810608] (ulepszenie 1) — nazwa] 꿰뚫린 나약함
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810608].levelList[level=1].name
   limit: do 40 znaków
   EN: Punctured Weakness
   PL: Punctured Weakness
392. [Umiejętność wroga [810608] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 사냥감의 징표 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810608].levelList[level=1].desc
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Umiejętność wroga [810608] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 창백한 소음 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810608].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 378 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Umiejętność wroga [810608] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 공격 레벨 감소 3 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810608].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Offense Level Down next turn
   PL: [OnSucceedAttack] nakłada 3 Spadek Poziomu Ataku w następnej turze
395. [Umiejętność wroga [810609] (ulepszenie 1) — nazwa] 탄식의 메아리
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810609].levelList[level=1].name
   limit: do 40 znaków
   EN: Echoing Cry
   PL: Echoing Cry
396. [Umiejętność wroga [810609] (ulepszenie 1) — opis] 대상의 출혈 1 당 피해량 +5%\n대상에게 사냥감의 징표 가 없으면 코인 위력 +1\n[DefeatDuel] 정신력 5 감소
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810609].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Deal +5% damage for every 1 Bleed on target\nIf target does not have Prey Mark, Coin Power +1\n[DefeatDuel] Lose 5 SP
   PL: zadaje +5% obrażeń za każde 1 Krwawienie celu\njeżeli cel nie ma Znaku Ofiary, Moc Monety +1\n[DefeatDuel] traci 5 SP
397. [Umiejętność wroga [810609] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810609].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Umiejętność wroga [810609] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 무작위 적 3명에게 정신 피해 3
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810609].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 SP damage on 3 random enemies
   PL: [OnSucceedAttack] zadaje 3 obrażeń SP 3 losowym wrogom
399. [Umiejętność wroga [810609] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810609].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Umiejętność wroga [810609] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 무작위 적 3명에게 정신 피해 3
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810609].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Umiejętność wroga [810609] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810609].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Umiejętność wroga [810609] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 무작위 적 3명에게 정신 피해 3
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810609].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Umiejętność wroga [810609] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810609].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Umiejętność wroga [810609] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 무작위 적 3명에게 정신 피해 3
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810609].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Umiejętność wroga [810609] (ulepszenie 1) — moneta 5, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810609].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Umiejętność wroga [810609] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] 무작위 적 3명에게 정신 피해 3
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810609].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Umiejętność wroga [810609] (ulepszenie 1) — moneta 5, efekt 3 — opis] [OnSucceedAttack] 스타벅의 자아 10당 마지막 코인 1회 재사용
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810609].levelList[level=1].coinlist[#4].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Reuse the final Coin once for every 10 Starbuck's Ego
   PL: [OnSucceedAttack] używa ponownie ostatnią Monetę 1 raz za każde 10 Ego Starbuck
408. [Umiejętność wroga [810610] (ulepszenie 1) — nazwa] 혼탁한 궤적
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810610].levelList[level=1].name
   limit: do 40 znaków
   EN: Clouded Path
   PL: Clouded Path
409. [Umiejętność wroga [810610] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 사냥감의 징표 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810610].levelList[level=1].desc
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Umiejętność wroga [810610] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량 감소 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810610].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Damage Down
   PL: [OnSucceedAttack] nakłada 2 Spadek Obrażeń
411. [Umiejętność wroga [810610] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810610].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Umiejętność wroga [810610] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 창백한 소음 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810610].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 378 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Umiejętność wroga [810610] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 출혈 5 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810610].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Umiejętność wroga [810611] (ulepszenie 1) — nazwa] 탈색된 참회
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810611].levelList[level=1].name
   limit: do 40 znaków
   EN: Bleached Atonement
   PL: Bleached Atonement
415. [Umiejętność wroga [810611] (ulepszenie 1) — opis] [WhenUse] 퀴케그의 자아 5 감소\n[WinDuel] 방어 레벨 증가 6 얻음\n[DefeatDuel] 정신력 5 감소
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810611].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WinDuel], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Lose 5 Queequeg's Ego\n[WinDuel] Gain 6 Defense Level Up\n[DefeatDuel] Lose 5 SP
   PL: [WhenUse] traci 5 Ego Queequeg\n[WinDuel] zyskuje 6 Wzrost Poziomu Obrony\n[DefeatDuel] traci 5 SP
416. [Umiejętność wroga [810611] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 창백한 소음 2 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810611].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Pallid Noise
   PL: [OnSucceedAttack] nakłada 2 Bladego Szumu
417. [Umiejętność wroga [810611] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상을 흐트러짐 상태로 만듦
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810611].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Stagger target
   PL: [OnSucceedAttack] powoduje Oszołamienie celu
418. [Umiejętność wroga [810612] (ulepszenie 1) — nazwa] 퍼져나오는 백화
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810612].levelList[level=1].name
   limit: do 40 znaków
   EN: Insidious Pallidification
   PL: Insidious Pallidification
419. [Umiejętność wroga [810612] (ulepszenie 1) — opis] [StartBattle] 최대 체력의 10%만큼 보호막을 얻음. 퀴케그의 자아 1 당 최대 체력의 0.5%만큼 보호막을 추가로 얻음.\n 보호막이 있는동안 피격 시 대상의 정신력 5 감소.\n피격 시 퀴케그의 자아 10당 스킬 1회 재사용
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810612].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 10% of Max HP as Shield. For every Queequeg's Ego, gain additional 0.5% of Max HP as additional Shield.\nWhen attacked while Shielded, attacker loses 5 SP\nWhen attacked, use this Skill once for every 10 Queequeg's Ego
   PL: [StartBattle] zyskuje Tarczę równą 10% Maks. HP; za każde 1 Ego Queequeg zyskuje dodatkowo Tarczę równą 0.5% Maks. HP.\nprzy trafieniu, gdy ta jednostka ma Tarczę, atakujący traci 5 SP\nprzy trafieniu używa ponownie tę Umiejętność 1 raz za każde 10 Ego Queequeg
420. [Umiejętność wroga [810612] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810612].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Umiejętność wroga [810612] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810612].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Umiejętność wroga [810007] (ulepszenie 1) — nazwa] 예언을 멸시치 말라
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810007].levelList[level=1].name
   limit: do 40 znaków
   EN: Scorn Not the Prophecy
   PL: Scorn Not the Prophecy
423. [Umiejętność wroga [810007] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Combustion] 5 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c5p3.json :: dataList[id=810007].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion] and 2 [Combustion] Count on target
   PL: [OnSucceedAttack] nakłada celowi 5 [Combustion] i 2 Licznika [Combustion]

## [a1c5p3] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c5p3
- grupa rozdziału/trybu: `a1c5p3` · plik: `Skills_Enemy-a1c5p3.json`

424. [Umiejętność wroga [9009801] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009801].levelList[level=1].name
   (powtórzenie elementu 213 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Umiejętność wroga [9009801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 4 부여
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 214 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Umiejętność wroga [9009802] (ulepszenie 1) — nazwa] 상처 헤집기
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009802].levelList[level=1].name
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Umiejętność wroga [9009802] (ulepszenie 1) — opis] [WinDuel] 정신력 5 회복.\n대상의 [Laceration]당 피해량 +5%
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009802].levelList[level=1].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Umiejętność wroga [9009802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Umiejętność wroga [9009802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Umiejętność wroga [9009802] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Umiejętność wroga [9009803] (ulepszenie 1) — nazwa] 마을을 지켜!
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009803].levelList[level=1].name
   (powtórzenie elementu 220 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Umiejętność wroga [9009803] (ulepszenie 1) — opis] [WhenUse] 호흡 5를 얻음
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009803].levelList[level=1].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Umiejętność wroga [9009803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Umiejętność wroga [9009803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Umiejętność wroga [9009803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Umiejętność wroga [9009803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Umiejętność wroga [9009803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Umiejętność wroga [9009803] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009803].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Umiejętność wroga [9009803] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009803].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Umiejętność wroga [9009803] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009803].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Umiejętność wroga [9009804] (ulepszenie 1) — nazwa] 투창
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009804].levelList[level=1].name
   limit: do 40 znaków
   EN: Javelin
   PL: Javelin
442. [Umiejętność wroga [9009804] (ulepszenie 1) — opis] [WhenUse] 호흡 5, 호흡 횟수 2를 얻음
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009804].levelList[level=1].desc
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Umiejętność wroga [9009804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2, 피해량 감소 2 부여
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind and 2 Damage Down next turn
   PL: [OnSucceedAttack] nakłada 2 Wiązania i 2 Spadek Obrażeń w następnej turze
444. [Umiejętność wroga [9009805] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009805].levelList[level=1].name
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Umiejętność wroga [9009805] (ulepszenie 1) — opis] 보호막이 있는 동안 피격 시, 다음 턴 공격 레벨 증가 1을 얻음.
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009805].levelList[level=1].desc
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Umiejętność wroga [9009901] (ulepszenie 1) — nazwa] 연속 찌르기
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009901].levelList[level=1].name
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Umiejętność wroga [9009901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 2 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Umiejętność wroga [9009901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Umiejętność wroga [9009902] (ulepszenie 1) — nazwa] 상처 파고들기
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009902].levelList[level=1].name
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Umiejętność wroga [9009902] (ulepszenie 1) — opis] [WinDuel] 정신력 5 회복.\n대상의 [Laceration]당 피해량 +5%
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009902].levelList[level=1].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Umiejętność wroga [9009902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Umiejętność wroga [9009902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Umiejętność wroga [9009902] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Umiejętność wroga [9009902] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009902].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Umiejętność wroga [9009903] (ulepszenie 1) — nazwa] 마을을 지켜!
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009903].levelList[level=1].name
   (powtórzenie elementu 220 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Umiejętność wroga [9009903] (ulepszenie 1) — opis] [WhenUse] 호흡 5를 얻음
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009903].levelList[level=1].desc
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
457. [Umiejętność wroga [9009903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Umiejętność wroga [9009903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Umiejętność wroga [9009903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Umiejętność wroga [9009903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Umiejętność wroga [9009903] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009903].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Umiejętność wroga [9009903] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009903].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Umiejętność wroga [9009903] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009903].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Umiejętność wroga [9009903] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 정신력 4 회복
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009903].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Umiejętność wroga [9009904] (ulepszenie 1) — nazwa] 투창
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009904].levelList[level=1].name
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Umiejętność wroga [9009904] (ulepszenie 1) — opis] [WhenUse] 호흡 5, 호흡 횟수 2를 얻음
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009904].levelList[level=1].desc
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Umiejętność wroga [9009904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 2, 취약 2 부여
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bind and 2 Fragile next turn
   PL: [OnSucceedAttack] nakłada 2 Wiązania i 2 Kruchości w następnej turze
468. [Umiejętność wroga [9009905] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009905].levelList[level=1].name
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Umiejętność wroga [9009905] (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 공격 레벨 증가 1을 얻음 (최대 3)
   źródło: Skills_Enemy-a1c5p3.json :: dataList[id=9009905].levelList[level=1].desc
   (powtórzenie elementu 260 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c5p3] Pasywka wroga: Passives_Abnormality-a1c5p3
- plik gry: `Passives_Abnormality-a1c5p3.json`

470. [[a1c5p3] Pasywka wroga [810001] — nazwa] 모든 것을 밝히는 불빛
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810001].name
   limit: do 40 znaków
   EN: The All-Illuminating Light
   PL: The All-Illuminating Light
471. [[a1c5p3] Pasywka wroga [810001] — opis] 촛불이 꺼지고 촛불 체력이 전부 회복된 상태면, 모든 촛불이 켜지기전까지 내성이 올라감.\n모든 촛불이 켜져있을 때, 내성이 내려감.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810001].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If every Candle is snuffed and at full HP, gain resistance until all Candles are lit again.\nWhen all Candles are lit, lose resistance.
   PL: jeżeli Candle są zgaszone i przywrócone do pełni HP, zyskuje odporność, dopóki wszystkie Candle nie zostaną zapalone ponownie.\ngdy wszystkie Candle są zapalone, traci odporność.
472. [[a1c5p3] Pasywka wroga [810002] — nazwa] 밀려난 어둠
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810002].name
   limit: do 40 znaków
   EN: Darkness Deterred
   PL: Darkness Deterred
473. [[a1c5p3] Pasywka wroga [810002] — opis] 불이 꺼진 이후로 4턴마다 꺼진 촛불이 있다면, 스스로 모든 촛불을 켠다. 모든 촛불의 체력이 1이 된다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810002].desc
   limit: do 120 znaków
   EN: Light all Candles every 4 turns after a Candle is snuffed. All Candles' HP is reduced to 1.
   PL: co 4 tury od zgaszenia światła, jeżeli są zgaszone Candle, zapala je sama. HP wszystkich Candle spada do 1.
474. [[a1c5p3] Pasywka wroga [810701] — nazwa] 피어오르는 불씨
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810701].name
   limit: do 40 znaków
   EN: Burning Embers
   PL: Burning Embers
475. [[a1c5p3] Pasywka wroga [810701] — opis] 체력이 1 이하로 떨어지지 않음.\n체력이 1일 때, 불이 켜지며 공격 스킬을 사용함.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: HP does not drop below 1.\nAt 1 HP, light the Candles and uses an Attack Skill.
   PL: HP nie spada poniżej 1.\nprzy 1 HP zapala Candle i używa Umiejętności ataku.
476. [[a1c5p3] Pasywka wroga [810702] — nazwa] 가라앉는 어둠
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810702].name
   limit: do 40 znaków
   EN: Sinking Darkness
   PL: Sinking Darkness
477. [[a1c5p3] Pasywka wroga [810702] — opis] 모든 촛불이 켜졌을 때, 방어 스킬을 사용한다.\n방어막이 전부 소모되면, 다음 턴에 불이 꺼진다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810702].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When all Candles are lit, use a Defensive Skill.\nSnuff out the Candles next turn when out of Shield.
   PL: gdy wszystkie Candle są zapalone, używa Umiejętności obrony.\ngdy Tarcza się wyczerpie, Candle gasną w następnej turze.
478. [[a1c5p3] Pasywka wroga [810101] — nazwa] 노출된 진주
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810101].name
   limit: do 40 znaków
   EN: Exposed Pearl
   PL: Exposed Pearl
479. [[a1c5p3] Pasywka wroga [810101] — opis] 턴 시작시 자신의 녹색 점액이 0이면, 흐트러짐 상태가 됨. 진주 속성 내성이 0.5씩 감소함.\n흐트러짐이 풀릴 때, 녹색 점액 10을 얻음.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810101].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: If at 0 Green Slime, become Staggered. Pearl loses all Affinity Resistances by 0.5.\nGain 10 Green Slime when recovering from Stagger.
   PL: Początek tury: jeżeli jej Green Slime wynosi 0, przechodzi w Oszołamienie. Odporności Afinności Pearl maleją o 0.5 każda.\ngdy dochodzi do siebie z Oszołamienia, zyskuje 10 Green Slime.
480. [[a1c5p3] Pasywka wroga [810102] — nazwa] 조각난 패각
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810102].name
   limit: do 40 znaków
   EN: Cracked Shell
   PL: Cracked Shell
481. [[a1c5p3] Pasywka wroga [810102] — opis] 본체 체력이 10% 남았을 때, 패턴이 변경됨.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810102].desc
   limit: do 120 znaków
   EN: At 10% Core HP, gains a new pattern.
   PL: przy 10% HP Korpusu przybiera nowy wzorzec.
482. [[a1c5p3] Pasywka wroga [810103] — nazwa] 단단한 패각
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810103].name
   limit: do 40 znaków
   EN: Solid Shell
   PL: Solid Shell
483. [[a1c5p3] Pasywka wroga [810103] — opis] 껍질 부위는 흐트러짐 상태여도 원래 내성을 유지함.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810103].desc
   limit: do 120 znaków
   EN: The Shell Part retains its resistances even during Staggered state.
   PL: część Shell zachowuje swoje odporności nawet w Oszołamieniu.
484. [[a1c5p3] Pasywka wroga [810104] — nazwa] 모여드는 점액
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810104].name
   limit: do 40 znaków
   EN: Gathering Slime
   PL: Gathering Slime
485. [[a1c5p3] Pasywka wroga [810104] — opis] 잠식 액체를 사용하는 턴에 속도가 1이 됨.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810104].desc
   limit: do 120 znaków
   EN: Fix this Part's speed to 1 for a turn when using Devouring Fluid.
   PL: w turze użycia Devouring Fluid Szybkość tej części wynosi 1.
486. [[a1c5p3] Pasywka wroga [810901] — nazwa] 녹색 점액
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810901].name
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [[a1c5p3] Pasywka wroga [810901] — opis] 걷는 진주에게 처치 당하면, 걷는 진주의 녹색 점액 3 증가.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810901].desc
   limit: do 120 znaków
   EN: Apply 3 Green Slime to Ambling Pearl when defeated by Ambling Pearl.
   PL: gdy zostaje pokonana przez Ambling Pearl, Ambling Pearl zyskuje 3 Green Slime.
488. [[a1c5p3] Pasywka wroga [810902] — nazwa] 오염시키는 점액
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810902].name
   limit: do 40 znaków
   EN: Contaminating Slime
   PL: Contaminating Slime
489. [[a1c5p3] Pasywka wroga [810902] — opis] 턴 종료시, 모든 적에게 (2 + 살아있는 녹색 점액)만큼 독 부여.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810902].desc
   limit: do 120 znaków
   EN: Turn End: Apply (2 + Surviving Green Slime) Poison to all enemies.
   PL: Koniec tury: nakłada (2 + liczba żyjących Green Slime) Zatrucia wszystkim wrogom.
490. [[a1c5p3] Pasywka wroga [810201] — nazwa] 확산하는 산소
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810201].name
   limit: do 40 znaków
   EN: Expanding Oxygen
   PL: Expanding Oxygen
491. [[a1c5p3] Pasywka wroga [810201] — opis] 형광등 부위가 파괴되면, 모든 적에게 [AaCePcBb] 부여.\n형광등 부위는 2턴 후에 재생함.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810201].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [AaCePcBb]
   znaczenie tagów: [AaCePcBb] = 형광등 파편 / Fluorescence Shard
   EN: When the Fluorescence Part is broken, inflict [AaCePcBb] on all enemies.\nFluorescence Part regenerates after 2 turns.
   PL: gdy część Fluorescence zostaje zniszczona, nakłada [AaCePcBb] wszystkim wrogom.\nczęść Fluorescence odrasta po 2 turach.
492. [[a1c5p3] Pasywka wroga [810202] — nazwa] 수중 호흡
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810202].name
   limit: do 40 znaków
   EN: Underwater Breathing
   PL: Underwater Breathing
493. [[a1c5p3] Pasywka wroga [810202] — opis] 2턴부터 매 턴마다 형광등 부위가 파괴 상태가 아니라면, 이번 턴에 호흡 8을 얻음.\n호흡 횟수 3 증가.2턴부터 매 턴마다 형광등 부위가 파괴 상태라면, 이번 턴에 마비 2. 피해량 감소 2 얻음.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810202].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Starting from turn 2, gain 8 Poise this turn if the Fluorescence Part isn't broken.\nGain +3 Poise Count. Starting from turn 2, gain 2 Paralyze and 2 Damage Down this turn if the Fluorescence Part is broken.
   PL: od 2. tury, jeżeli część Fluorescence nie jest zniszczona, zyskuje 8 Oddechu w tej turze.\nzwiększa Licznik Oddechu o 3. od 2. tury, jeżeli część Fluorescence jest zniszczona, zyskuje w tej turze 2 Paraliżu i 2 Spadek Obrażeń.
494. [[a1c5p3] Pasywka wroga [810203] — nazwa] 탁류
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810203].name
   limit: do 40 znaków
   EN: Siltcurrent
   PL: Siltcurrent
495. [[a1c5p3] Pasywka wroga [810203] — opis] 2턴부터 매 턴마다 [AaCePcBb]이 없는 인격들에게 속박 1, 마비 1 부여. 정신력 3 감소.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810203].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [AaCePcBb]
   znaczenie tagów: [AaCePcBb] = 형광등 파편 / Fluorescence Shard
   EN: Starting from turn 2, all Identities without [AaCePcBb] are inflicted with 1 Bind and 1 Paralyze; Identities without [AaCePcBb] lose 3 SP.
   PL: od 2. tury nakłada 1 Wiązania i 1 Paraliżu Tożsamościom bez [AaCePcBb]; Tożsamości bez [AaCePcBb] tracą 3 SP.
496. [[a1c5p3] Pasywka wroga [810801] — nazwa] 단단함
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810801].name
   limit: do 40 znaków
   EN: Harden
   PL: Harden
497. [[a1c5p3] Pasywka wroga [810801] — opis] 받은 피해가 최소 12이상이여야 피해를 입음.\n그 이하의 피해는 0으로 받음.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810801].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Can be damaged only with damages equal to or higher than 12.\nAll damage under 12 is nullified.
   PL: otrzymuje obrażenia tylko przy wartości równej lub wyższej niż 12.\nobrażenia poniżej 12 są zerowane.
498. [[a1c5p3] Pasywka wroga [810802] — nazwa] 휩쓸려가는 표류물
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810802].name
   limit: do 40 znaków
   EN: Rolling Flotsam
   PL: Rolling Flotsam
499. [[a1c5p3] Pasywka wroga [810802] — opis] 꿈먹는 탁류가 맹목을 사용하고, 턴 종료시 파괴되지 않았다면 무작위 인격에게 체력 20 피해를 입힘.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810802].desc
   limit: do 190 znaków
   EN: After the Dream-devouring Siltcurrent uses Blind Obsession, and if this unit is not destroyed at Turn End, deal 20 damage to a random Identity.
   PL: gdy Dream-Devouring Siltcurrent użyje Blind Obsession, a ta jednostka nie zostanie zniszczona do końca tury, zadaje 20 obrażeń losowej Tożsamości.
500. [[a1c5p3] Pasywka wroga [810803] — nazwa] 파괴된 표류물
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810803].name
   limit: do 40 znaków
   EN: Destroyed Flotsam
   PL: Destroyed Flotsam
501. [[a1c5p3] Pasywka wroga [810803] — opis] 죽음을 맞이했을 때, 체력이 1 이하로 떨어지지 않음.\n파괴된 표류물이 됨.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810803].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: HP does not drop below 1 upon defeat.\nTurns into a Destroyed Flotsam.
   PL: przy śmierci HP nie spada poniżej 1.\nstaje się Destroyed Flotsam.
502. [[a1c5p3] Pasywka wroga [810301] — nazwa] 선장의 명령
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810301].name
   limit: do 40 znaków
   EN: Captain's Orders
   PL: Captain's Orders
503. [[a1c5p3] Pasywka wroga [810301] — opis] 턴 시작 시 정신력이 -45가 아니면, (자신을 제외한 살아있는 아군 수 x 5)만큼 정신력을 회복한다.\n턴 시작 시 정신력이 -45면, 턴 종료 시 패닉 상태를 해제하고, 정신력을 0으로 초기화한다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810301].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: If not at -45 SP, heal (# of surviving other allies x 5) SP.\nTurn Start: If at -45 SP, recover from panic at Turn End and reset SP to 0.
   PL: Początek tury: przy SP innym niż -45 przywraca (liczba innych żyjących sojuszników x 5) SP.\nPoczątek tury: przy SP równym -45, na koniec tury dochodzi do siebie z Paniki i SP wraca do 0.
504. [[a1c5p3] Pasywka wroga [810302] — nazwa] 헤집어진 문신
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810302].name
   limit: do 40 znaków
   EN: Mutilated Tattoos
   PL: Mutilated Tattoos
505. [[a1c5p3] Pasywka wroga [810302] — opis] 피쿼드타운 소속 아군이 사망할 때마다 호흡 횟수 1 감소, 정신력 10 감소
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810302].desc
   limit: do 120 znaków
   EN: Every time a Pequod Town faction ally is defeated, lose 1 Poise Count and 10 SP.
   PL: za każdym razem, gdy ginie sojusznik frakcji Pequod Town, traci 1 Licznika Oddechu i 10 SP.
506. [[a1c5p3] Pasywka wroga [810303] — nazwa] 불굴의 작살잡이
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810303].name
   limit: do 40 znaków
   EN: The Indomitable Harpooneer
   PL: The Indomitable Harpooneer
507. [[a1c5p3] Pasywka wroga [810303] — opis] 자신의 체력이 낮아질수록 적에게 가하는 스킬의 피해량이 증가한다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810303].desc
   limit: do 120 znaków
   EN: The lower this unit's HP gets, the more damage this unit's Skills deal.
   PL: im niższe HP tej jednostki, tym więcej obrażeń zadają jej Umiejętności.
508. [[a1c5p3] Pasywka wroga [810304] — nazwa] 주입된 증오와 미움
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810304].name
   limit: do 50 znaków
   EN: Injected Hatred and Animosity
   PL: Injected Hatred and Animosity
509. [[a1c5p3] Pasywka wroga [810304] — opis] 턴 종료 시 체력이 최대 체력의 50% 미만이면, 2페이즈로 넘어간다.\n2페이즈 전까지 체력이 1 미만으로 감소하지 않는다.\n2페이즈 시작 시 체력을 최대 체력의 50%까지 회복하고, 아군 4명을 소환한다. 이후 매 턴 시작 시 현재 체력 비율이 가장 낮은 적 1명에게 [AaCePcBj]를 부여한다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810304].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [AaCePcBj]
   znaczenie tagów: [AaCePcBj] = 사냥감의 징표 / Prey Mark
   EN: Turn End: If 50%- of max HP, move on to Phase 2.\nThis unit's HP does not drop below 1 before Phase 2 start.\nPhase 2 Start: Heal HP to 50% of max HP and summon 4 allies. Inflict [AaCePcBj] against 1 enemy with the lowest HP percentage at the start of every turn.
   PL: Koniec tury: przy 50% Maks. HP lub mniej przechodzi do Fazy 2.\ndo rozpoczęcia Fazy 2 jej HP nie spada poniżej 1.\nPoczątek Fazy 2: przywraca HP do 50% Maks. HP i przywołuje 4 sojuszników; na początku każdej tury nakłada [AaCePcBj] na 1 wroga z najniższym procentem aktualnego HP.
510. [[a1c5p3] Pasywka wroga [810305] — nazwa] 새겨지는 증오와 미움
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810305].name
   limit: do 50 znaków
   EN: Engraved Hatred and Animosity
   PL: Engraved Hatred and Animosity
511. [[a1c5p3] Pasywka wroga [810305] — opis] 체력이 1이 될 때,  체력을 최대 체력의 50%까지 회복하고, 다음 턴에 공격 위력 증가 2를 얻는다. (전투 당 1회 발동)
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810305].desc
   limit: do 120 znaków
   EN: At 1 HP, heal up to 50% of max HP and gain 2 Attack Power Up next turn. (Once per encounter)
   PL: przy 1 HP przywraca HP do 50% Maks. HP i zyskuje 2 Wzrost Mocy Ataku w następnej turze. (1 raz na walkę)
512. [[a1c5p3] Pasywka wroga [810306] — nazwa] 혼탁한 정신
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810306].name
   limit: do 40 znaków
   EN: Clouded Mind
   PL: Clouded Mind
513. [[a1c5p3] Pasywka wroga [810306] — opis] 흐트러짐 상태가 되면, 턴 종료 시 정신력이 0 미만인 경우, 정신력을 0으로 초기화한다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810306].desc
   limit: do 120 znaków
   EN: When Staggered and when at less than 0 SP at Turn End, reset SP to 0.
   PL: gdy przechodzi w Oszołamienie i przy SP poniżej 0 na koniec tury, jej SP wraca do 0.
514. [[a1c5p3] Pasywka wroga [810401] — nazwa] 새겨지는 증오와 미움
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810401].name
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [[a1c5p3] Pasywka wroga [810401] — opis] 턴 종료 시 체력이 50% 미만이면, 다음 턴에 신속 2, 공격 위력 증가 2를 얻는다. (전투 당 1회 발동)
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810401].desc
   limit: do 120 znaków
   EN: Turn End: At 50- HP, gain 2 Haste and 2 Attack Power Up next turn. (once per encounter)
   PL: Koniec tury: przy 50% HP lub mniej zyskuje 2 Pośpiechu i 2 Wzrost Mocy Ataku w następnej turze. (1 raz na walkę)
516. [[a1c5p3] Pasywka wroga [810402] — nazwa] 작살 꿰뚫기
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810402].name
   limit: do 40 znaków
   EN: Puncturing Harpoon
   PL: Puncturing Harpoon
517. [[a1c5p3] Pasywka wroga [810402] — opis] 크리티컬 적중 시 스킬로 부여하는 부정적인 효과의 수치가 1 증가한다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810402].desc
   limit: do 120 znaków
   EN: On Critical Hit, inflict 1 additional negative effect with Skill effects.
   PL: przy trafieniu krytycznym nakłada o 1 więcej negatywnych Efektów efektami Umiejętności.
518. [[a1c5p3] Pasywka wroga [810501] — nazwa] 피쿼드 호의 선장
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810501].name
   limit: do 40 znaków
   EN: Captain of the Pequod
   PL: Captain of the Pequod
519. [[a1c5p3] Pasywka wroga [810501] — opis] 턴 시작 시 정신력이 -45가 아니면, 정신력을 15 회복한다.\n턴 종료 시 패닉 상태면, 턴 종료 시 패닉 상태를 해제하고, 정신력을 0으로 초기화한다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810501].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: If not at -45 SP, heal 15 SP.\nTurn End: If panicked, recover from panic. Reset SP to 0.
   PL: Początek tury: przy SP innym niż -45 przywraca 15 SP.\nKoniec tury: jeżeli jest w Panice, dochodzi do siebie i SP wraca do 0.
520. [[a1c5p3] Pasywka wroga [810503] — nazwa] 흐릿해진 명령
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810503].name
   limit: do 40 znaków
   EN: Muddled Orders
   PL: Muddled Orders
521. [[a1c5p3] Pasywka wroga [810503] — opis] 이 캐릭터가 흐트러짐 상태가 되면, 턴 종료 시 자신을 제외한 모든 아군의 정신력이 0 미만인 경우, 정신력을 0으로 초기화한다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810503].desc
   limit: do 150 znaków
   EN: When this unit is Staggered, and when all other allies are at less than 0 SP at Turn End, reset their SP to 0.
   PL: gdy ta jednostka przechodzi w Oszołamienie, na koniec tury, jeżeli SP wszystkich pozostałych sojuszników jest poniżej 0, ich SP wraca do 0.
522. [[a1c5p3] Pasywka wroga [810504] — nazwa] 냉혹한 결단
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810504].name
   limit: do 40 znaków
   EN: Coldhearted Decision
   PL: Coldhearted Decision
523. [[a1c5p3] Pasywka wroga [810504] — opis] 2페이즈가 되면 체력을 최대로 회복하고, 퀴케그, 스타벅이 보유한 선장의 명령 패시브를 발동시키지 않는다. 또한 퀴케그가 턴 종료 시 원호 방어 보호막 수치가 0이어도 흐트러짐 상태가 되지 않는다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810504].desc
   limit: do 250 znaków
   EN: Phase 2 Start: Fully heal HP; Queequeg and Starbuck no longer activate Captain's Orders Passive. Also, Queequeg no longer gets Staggered even when her Assist Defense Shield value reaches 0.
   PL: Początek Fazy 2: przywraca HP do maksimum; Queequeg i Starbuck nie uruchamiają już pasywki Captain's Orders. Ponadto Queequeg nie przechodzi w Oszołamienie, nawet gdy wartość jej Bariery Wsparcia osiągnie 0.
524. [[a1c5p3] Pasywka wroga [810601] — nazwa] 에이해브
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810601].name
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [[a1c5p3] Pasywka wroga [810601] — opis] 턴 시작 시 정신력이 -45가 아니면, 정신력을 15 회복한다.\n턴 종료 시 패닉 상태면, 패닉 상태를 해제하고, 정신력을 0으로 초기화 한 뒤 다음 턴에 공격 위력 증가, 수비 위력 증가 2를 얻는다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810601].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: If not at -45 SP, heal 15 SP.\nTurn End: If panicked, recover from panic. Reset SP to 0 and gain 2 Attack Power Up and 2 Defense Power Up.
   PL: Początek tury: przy SP innym niż -45 przywraca 15 SP.\nKoniec tury: jeżeli jest w Panice, dochodzi do siebie, SP wraca do 0, a w następnej turze zyskuje 2 Wzrost Mocy Ataku i 2 Wzrost Mocy Obrony.
526. [[a1c5p3] Pasywka wroga [810602] — nazwa] 핍의 죄와 결백
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810602].name
   limit: do 40 znaków
   EN: Pip's Sin and Innocence
   PL: Pip's Sin and Innocence
527. [[a1c5p3] Pasywka wroga [810602] — opis] 페이즈 시작 시 핍의 자아 20을 얻는다. \n턴 종료 시 핍의 자아 1당 정신력을 3 회복한다.\n턴 종료 시 [AaCePcBo]가 0이면 다음 턴에 흐트러짐 상태가 된다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810602].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [AaCePcBo]
   znaczenie tagów: [AaCePcBo] = 핍의 자아 / Pip's Ego
   EN: Phase Start: Gain 20 Pip's Ego.\nTurn End: Heal 3 SP for every Pip's Ego.\nTurn End: If [AaCePcBo] is at 0, get Staggered next turn.
   PL: Początek fazy: zyskuje 20 Pipów.\nKoniec tury: przywraca 3 SP za każde 1 Pipy.\nKoniec tury: jeżeli [AaCePcBo] wynosi 0, przechodzi w Oszołamienie w następnej turze.
528. [[a1c5p3] Pasywka wroga [810603] — nazwa] 스타벅의 두려움
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810603].name
   limit: do 40 znaków
   EN: Starbuck's Fears
   PL: Starbuck's Fears
529. [[a1c5p3] Pasywka wroga [810603] — opis] 페이즈 시작 시 스타벅의 자아 20을 얻는다. \n[AaCePcBj]가 있는 대상과의 합 패배 시 합에서 파괴된 코인 수만큼 [AaCePcBp]가 감소한다.\n턴 시작 시 스타벅의 자아 5당 보호 1 을 얻는다.\n턴 종료 시 [AaCePcBp]가 0이면 다음 턴에 흐트러짐 상태가 된다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810603].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [AaCePcBj], [AaCePcBp]
   znaczenie tagów: [AaCePcBj] = 사냥감의 징표 / Prey Mark; [AaCePcBp] = 스타벅의 자아 / Starbuck's Ego
   EN: Phase Start: Gain 20 Starbuck's Ego.\nLose 1 [AaCePcBp] for every Coin destroyed in Clash against targets with [AaCePcBj].\nTurn Start: Gain 1 Protection for every 5 Starbuck's Ego.\nTurn End: If [AaCePcBp] is at 0, get Staggered next turn.
   PL: Początek fazy: zyskuje 20 Ego Starbuck.\npo przegranej w Starciu z celem mającym [AaCePcBj] traci 1 [AaCePcBp] za każdą Monetę zniszczoną w Starciu.\nPoczątek tury: zyskuje 1 Ochrony za każde 5 Ego Starbuck.\nKoniec tury: jeżeli [AaCePcBp] wynosi 0, przechodzi w Oszołamienie w następnej turze.
530. [[a1c5p3] Pasywka wroga [810604] — nazwa] 작살 꿰뚫기
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810604].name
   (powtórzenie elementu 516 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [[a1c5p3] Pasywka wroga [810604] — opis] 이번 페이즈동안 크리티컬 적중 시 스킬로 부여하는 부정적인 효과의 수치가 1 증가한다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810604].desc
   limit: do 120 znaków
   EN: During this Phase, on Critical Hit, inflict 1 additional negative effect with Skill effects.
   PL: w tej fazie, przy trafieniu krytycznym, nakłada o 1 więcej negatywnych Efektów efektami Umiejętności.
532. [[a1c5p3] Pasywka wroga [810605] — nazwa] 퀴케그의 참회
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810605].name
   limit: do 40 znaków
   EN: Queequeg's Atonement
   PL: Queequeg's Atonement
533. [[a1c5p3] Pasywka wroga [810605] — opis] 페이즈 시작 시 퀴케그의 자아 30을 얻는다. \n턴 종료 시 보호막이 남아있으면 퀴케그의 자아를 5 회복하고, 보호막이 없으면 [AaCePcBq]가 10 감소한다.\n턴 종료 시 [AaCePcBq]가 0이면 다음 턴에 흐트러짐 상태가 된다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810605].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [AaCePcBq]
   znaczenie tagów: [AaCePcBq] = 퀴케그의 자아 / Queequeg's Ego
   EN: Phase Start: Gain 30 Queequeg's Ego.\nTurn End: If this unit still has remaining Shield, regain 5 Queequeg's Ego. If this unit does not have remaining Shield, lose 10 [AaCePcBq].\nTurn End: If [AaCePcBq] is at 0, get Staggered next turn.
   PL: Początek fazy: zyskuje 30 Ego Queequeg.\nKoniec tury: jeżeli ta jednostka ma pozostałą Tarczę, odzyskuje 5 Ego Queequeg; jeżeli Tarczy nie ma, traci 10 [AaCePcBq].\nKoniec tury: jeżeli [AaCePcBq] wynosi 0, przechodzi w Oszołamienie w następnej turze.
534. [[a1c5p3] Pasywka wroga [810606] — nazwa] 불굴의 작살잡이
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810606].name
   (powtórzenie elementu 506 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [[a1c5p3] Pasywka wroga [810606] — opis] 이번 페이즈동안 자신의 체력이 낮아질수록 적에게 가하는 스킬의 피해량이 증가한다.\n자신의 잃은 체력 0.75%당 피해량 1% 증가 \n(최대 100%. 체력이 최대 체력의 25%일 때 최대가 됨)
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810606].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The lower this unit's HP gets, the more damage this unit deals with its Skills.\nDeal 1% more HP for every 0.75% missing HP on self\n(Max 100%. Maxes out when this unit is at 25% HP)
   PL: w tej fazie im niższe HP tej jednostki, tym więcej obrażeń zadaje jej Umiejętnościami.\nzadaje o 1% więcej obrażeń za każde 0.75% utraconego HP\n(maks. 100%; maksimum przy 25% HP)
536. [[a1c5p3] Pasywka wroga [810607] — nazwa] 숭고의 대가
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810607].name
   limit: do 40 znaków
   EN: Price of Nobility
   PL: Price of Nobility
537. [[a1c5p3] Pasywka wroga [810607] — opis] 다른 캐릭터의 자아를 얻을 때마다 공격 레벨과 방어 레벨이 증가\n특정 스킬 합 패배 시 정신력 감소
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=810607].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Offense Level and Defense Level every time this unit gains other characters' Ego\nLose SP when losing certain Skill Clashes
   PL: za każdym razem, gdy zyskuje Ego innych postaci, Poziom Ataku i Poziom Obrony rosną\npo przegranej w Starciu z określoną Umiejętnością traci SP
538. [[a1c5p3] Pasywka wroga [814101] — nazwa] 모든 것을 밝히는 불빛
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=814101].name
   (powtórzenie elementu 470 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [[a1c5p3] Pasywka wroga [814101] — opis] 촛불이 꺼지고 촛불 체력이 전부 회복된 상태면, 모든 촛불이 켜지기전까지 내성이 올라감.\n모든 촛불이 켜져있을 때, 내성이 내려감.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=814101].desc
   (powtórzenie elementu 471 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [[a1c5p3] Pasywka wroga [814102] — nazwa] 밀려난 어둠
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=814102].name
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [[a1c5p3] Pasywka wroga [814102] — opis] 불이 꺼진 이후로 4턴마다 꺼진 촛불이 있다면, 스스로 모든 촛불을 켠다. 모든 촛불의 체력이 1이 된다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=814102].desc
   (powtórzenie elementu 473 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [[a1c5p3] Pasywka wroga [813601] — nazwa] 피어오르는 불씨
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813601].name
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [[a1c5p3] Pasywka wroga [813601] — opis] 체력이 1 이하로 떨어지지 않음.\n체력이 1일 때, 불이 켜지며 공격 스킬을 사용함.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813601].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [[a1c5p3] Pasywka wroga [813602] — nazwa] 가라앉는 어둠
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813602].name
   (powtórzenie elementu 476 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [[a1c5p3] Pasywka wroga [813602] — opis] 모든 촛불이 켜졌을 때, 방어 스킬을 사용한다.\n방어막이 전부 소모되면, 다음 턴에 불이 꺼진다.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813602].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [[a1c5p3] Pasywka wroga [813701] — nazwa] 노출된 진주
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813701].name
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [[a1c5p3] Pasywka wroga [813701] — opis] 턴 시작시 자신의 녹색 점액이 0이면, 흐트러짐 상태가 됨. 진주 속성 내성이 0.5씩 감소함.\n흐트러짐이 풀릴 때, 녹색 점액 10을 얻음.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813701].desc
   (powtórzenie elementu 479 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [[a1c5p3] Pasywka wroga [813702] — nazwa] 조각난 패각
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813702].name
   (powtórzenie elementu 480 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [[a1c5p3] Pasywka wroga [813702] — opis] 본체 체력이 10% 남았을 때, 패턴이 변경됨.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813702].desc
   (powtórzenie elementu 481 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [[a1c5p3] Pasywka wroga [813703] — nazwa] 단단한 패각
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813703].name
   (powtórzenie elementu 482 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [[a1c5p3] Pasywka wroga [813703] — opis] 껍질 부위는 흐트러짐 상태여도 원래 내성을 유지함.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813703].desc
   (powtórzenie elementu 483 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [[a1c5p3] Pasywka wroga [813704] — nazwa] 모여드는 점액
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813704].name
   (powtórzenie elementu 484 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [[a1c5p3] Pasywka wroga [813704] — opis] 잠식 액체를 사용하는 턴에 속도가 1이 됨.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813704].desc
   (powtórzenie elementu 485 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [[a1c5p3] Pasywka wroga [813801] — nazwa] 녹색 점액
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813801].name
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [[a1c5p3] Pasywka wroga [813801] — opis] 걷는 진주에게 처치 당하면, 걷는 진주의 녹색 점액 3 증가.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813801].desc
   (powtórzenie elementu 487 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [[a1c5p3] Pasywka wroga [813802] — nazwa] 오염시키는 점액
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813802].name
   (powtórzenie elementu 488 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [[a1c5p3] Pasywka wroga [813802] — opis] 턴 종료시, 모든 적에게 (2 + 살아있는 녹색 점액)만큼 독 부여.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813802].desc
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [[a1c5p3] Pasywka wroga [813901] — nazwa] 확산하는 산소
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813901].name
   (powtórzenie elementu 490 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [[a1c5p3] Pasywka wroga [813901] — opis] 형광등 부위가 파괴되면, 모든 적에게 [AaCePcBb] 부여.\n형광등 부위는 2턴 후에 재생함.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813901].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [[a1c5p3] Pasywka wroga [813902] — nazwa] 수중 호흡
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813902].name
   (powtórzenie elementu 492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [[a1c5p3] Pasywka wroga [813902] — opis] 2턴부터 매 턴마다 형광등 부위가 파괴 상태가 아니라면, 이번 턴에 호흡 8을 얻음.\n호흡 횟수 3 증가.2턴부터 매 턴마다 형광등 부위가 파괴 상태라면, 이번 턴에 마비 2. 피해량 감소 2 얻음.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813902].desc
   (powtórzenie elementu 493 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [[a1c5p3] Pasywka wroga [813903] — nazwa] 탁류
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813903].name
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [[a1c5p3] Pasywka wroga [813903] — opis] 2턴부터 매 턴마다 [AaCePcBb]이 없는 인격들에게 속박 1, 마비 1 부여. 정신력 3 감소.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=813903].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [[a1c5p3] Pasywka wroga [814001] — nazwa] 단단함
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=814001].name
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [[a1c5p3] Pasywka wroga [814001] — opis] 받은 피해가 최소 12이상이여야 피해를 입음.\n그 이하의 피해는 0으로 받음.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=814001].desc
   (powtórzenie elementu 497 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [[a1c5p3] Pasywka wroga [814002] — nazwa] 휩쓸려가는 표류물
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=814002].name
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [[a1c5p3] Pasywka wroga [814002] — opis] 꿈먹는 탁류가 맹목을 사용하고, 턴 종료시 파괴되지 않았다면 무작위 인격에게 체력 20 피해를 입힘.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=814002].desc
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [[a1c5p3] Pasywka wroga [814003] — nazwa] 파괴된 표류물
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=814003].name
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [[a1c5p3] Pasywka wroga [814003] — opis] 죽음을 맞이했을 때, 체력이 1 이하로 떨어지지 않음.\n파괴된 표류물이 됨.
   źródło: Passives_Abnormality-a1c5p3.json :: dataList[id=814003].desc
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c5p3] Pasywka wroga: Passives_Enemy-a1c5p3
- plik gry: `Passives_Enemy-a1c5p3.json`

570. [[a1c5p3] Pasywka wroga [9009801] — nazwa] 억제된 백화
   źródło: Passives_Enemy-a1c5p3.json :: dataList[id=9009801].name
   limit: do 40 znaków
   EN: Suppressed Pallidification
   PL: Suppressed Pallidification
571. [[a1c5p3] Pasywka wroga [9009801] — opis] 턴 시작 시 (자신을 제외한 살아있는 아군 수)만큼 자신의 공격 레벨과 방어 레벨이 증가
   źródło: Passives_Enemy-a1c5p3.json :: dataList[id=9009801].desc
   limit: do 150 znaków
   EN: At Turn Start, gain Offense Level and Defense Level by the number of surviving allies (not including this unit)
   PL: Początek tury: zyskuje Poziom Ataku i Poziom Obrony w liczbie równej liczbie żyjących sojuszników (nie licząc tej jednostki)
572. [[a1c5p3] Pasywka wroga [9009802] — nazwa] 선장님의 명령
   źródło: Passives_Enemy-a1c5p3.json :: dataList[id=9009802].name
   limit: do 40 znaków
   EN: Captain's Orders
   PL: Captain's Orders
573. [[a1c5p3] Pasywka wroga [9009802] — opis] 턴 시작 시 (자신을 제외한 살아있는 아군 수 x 3) 만큼 정신력을 회복한다.
   źródło: Passives_Enemy-a1c5p3.json :: dataList[id=9009802].desc
   limit: do 120 znaków
   EN: At Turn Start, heal SP by (# of other surviving allies x 3)
   PL: Początek tury: przywraca (liczba innych żyjących sojuszników x 3) SP.
574. [[a1c5p3] Pasywka wroga [9009803] — nazwa] 주입된 증오와 미움
   źródło: Passives_Enemy-a1c5p3.json :: dataList[id=9009803].name
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [[a1c5p3] Pasywka wroga [9009803] — opis] 턴 종료 시 체력이 50% 미만이면, 다음 턴에 공격 위력 증가 1을 얻는다. (전투 당 1회 발동)
   źródło: Passives_Enemy-a1c5p3.json :: dataList[id=9009803].desc
   limit: do 120 znaków
   EN: Turn End: At 50%- HP, gain 1 Attack Power Up next turn. (once per encounter)
   PL: Koniec tury: przy 50% HP lub mniej zyskuje 1 Wzrost Mocy Ataku w następnej turze. (1 raz na walkę)
576. [[a1c5p3] Pasywka wroga [9009804] — nazwa] 덮쳐오는 백화
   źródło: Passives_Enemy-a1c5p3.json :: dataList[id=9009804].name
   limit: do 40 znaków
   EN: Crashing Pallidification
   PL: Crashing Pallidification
577. [[a1c5p3] Pasywka wroga [9009804] — opis] 턴 종료 시 정신력이 0 미만이면, 50% 확률로 스킬 패턴이 변경된다.
   źródło: Passives_Enemy-a1c5p3.json :: dataList[id=9009804].desc
   limit: do 120 znaków
   EN: Turn End: At less than 0 SP, 50% chance to change Skill patterns.
   PL: Koniec tury: przy SP poniżej 0, 50% szans na zmianę wzorca Umiejętności.

## [a1c6p1] Wróg / część: Enemies-a1c6p1
- plik gry: `Enemies-a1c6p1.json`

578. [[a1c6p1] Wróg / część [90114] — nazwa] 촉박한 T사 갱단원
   źródło: Enemies-a1c6p1.json :: dataList[id=90114].name
   limit: do 40 znaków
   EN: Urgent T Corp. Gangster
   PL: Urgent T Corp. Gangster
579. [[a1c6p1] Wróg / część [90115] — nazwa] 겁먹은 T사 갱단원
   źródło: Enemies-a1c6p1.json :: dataList[id=90115].name
   limit: do 40 znaków
   EN: Scared T Corp. Gangster
   PL: Scared T Corp. Gangster
580. [[a1c6p1] Wróg / część [90116] — nazwa] 묵직한 데드레빗츠 단원
   źródło: Enemies-a1c6p1.json :: dataList[id=90116].name
   limit: do 40 znaków
   EN: Hefty Dead Rabbits Henchman
   PL: Hefty Dead Rabbits Henchman
581. [[a1c6p1] Wróg / część [90117] — nazwa] 느릿한 데드레빗츠 단원
   źródło: Enemies-a1c6p1.json :: dataList[id=90117].name
   limit: do 40 znaków
   EN: Slow Dead Rabbits Henchman
   PL: Slow Dead Rabbits Henchman
582. [[a1c6p1] Wróg / część [90118] — nazwa] 매서운 데드레빗츠 단원
   źródło: Enemies-a1c6p1.json :: dataList[id=90118].name
   limit: do 40 znaków
   EN: Fierce Dead Rabbits Henchman
   PL: Fierce Dead Rabbits Henchman
583. [[a1c6p1] Wróg / część [90119] — nazwa] 예리한 데드레빗츠 단원
   źródło: Enemies-a1c6p1.json :: dataList[id=90119].name
   limit: do 40 znaków
   EN: Sharp Dead Rabbits Henchman
   PL: Sharp Dead Rabbits Henchman
584. [[a1c6p1] Wróg / część [90120] — nazwa] 날렵한 에드가 가문 버틀러
   źródło: Enemies-a1c6p1.json :: dataList[id=90120].name
   limit: do 40 znaków
   EN: Swift Edgar Family Butler
   PL: Swift Edgar Family Butler
585. [[a1c6p1] Wróg / część [90121] — nazwa] 재빠른 에드가 가문 버틀러
   źródło: Enemies-a1c6p1.json :: dataList[id=90121].name
   limit: do 40 znaków
   EN: Fast Edgar Family Butler
   PL: Fast Edgar Family Butler
586. [[a1c6p1] Wróg / część [90122] — nazwa] 노련한 에드가 가문 버틀러
   źródło: Enemies-a1c6p1.json :: dataList[id=90122].name
   limit: do 40 znaków
   EN: Veteran Edgar Family Butler
   PL: Veteran Edgar Family Butler
587. [[a1c6p1] Wróg / część [90123] — nazwa] 교묘한 에드가 가문 버틀러
   źródło: Enemies-a1c6p1.json :: dataList[id=90123].name
   limit: do 40 znaków
   EN: Shifty Edgar Family Butler
   PL: Shifty Edgar Family Butler
588. [[a1c6p1] Wróg / część [90124] — nazwa] 숙달된 에드가 가문 버틀러
   źródło: Enemies-a1c6p1.json :: dataList[id=90124].name
   limit: do 40 znaków
   EN: Trained Edgar Family Butler
   PL: Trained Edgar Family Butler
589. [[a1c6p1] Wróg / część [90125] — nazwa] 노련한 에드가 가문 버틀러
   źródło: Enemies-a1c6p1.json :: dataList[id=90125].name
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [[a1c6p1] Wróg / część [90126] — nazwa] 험악한 워더링하이츠 버틀러
   źródło: Enemies-a1c6p1.json :: dataList[id=90126].name
   limit: do 50 znaków
   EN: Hostile Wuthering Heights Butler
   PL: Hostile Wuthering Heights Butler
591. [[a1c6p1] Wróg / część [90127] — nazwa] 단련한 워더링하이츠 버틀러
   źródło: Enemies-a1c6p1.json :: dataList[id=90127].name
   limit: do 50 znaków
   EN: Trained Wuthering Heights Butler
   PL: Trained Wuthering Heights Butler
592. [[a1c6p1] Wróg / część [91014] — nazwa] 조세핀
   źródło: Enemies-a1c6p1.json :: dataList[id=91014].name
   limit: do 40 znaków
   EN: Josephine
   PL: Josephine

## [a1c6p1] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c6p1
- grupa rozdziału/trybu: `a1c6p1` · plik: `Skills_Enemy-a1c6p1.json`

593. [Umiejętność wroga [9011401] (ulepszenie 1) — nazwa] 이봐, 이봐
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011401].levelList[level=1].name
   limit: do 40 znaków
   EN: Oi, Oi
   PL: Oi, Oi
594. [Umiejętność wroga [9011401] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Paralysis]가 있다면, 코인 위력 +1
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Paralysis]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Paralysis] = 마비 / Paralyze
   EN: [WhenUse] Coin Power +1 against targets with [Paralysis]
   PL: [WhenUse] Moc Monety +1 przeciwko celom z [Paralysis]
595. [Umiejętność wroga [9011401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여. [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 5 [Vibration]. Zwiększa Licznik [Vibration] o 2
596. [Umiejętność wroga [9011402] (ulepszenie 1) — nazwa] 찌릿할걸!
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011402].levelList[level=1].name
   limit: do 40 znaków
   EN: This'll Sting!
   PL: This'll Sting!
597. [Umiejętność wroga [9011402] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Vibration]이 있다면, 코인 위력 +1
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Coin Power +1 against targets with [Vibration]
   PL: [WhenUse] Moc Monety +1 przeciwko celom z [Vibration]
598. [Umiejętność wroga [9011402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여. [Vibration] 횟수 1 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration] and +1 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 5 [Vibration]. Zwiększa Licznik [Vibration] o 1
599. [Umiejętność wroga [9011402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 1 [Paralysis] next turn
   PL: [OnSucceedAttack] nakłada 1 [Paralysis] w następnej turze
600. [Umiejętność wroga [9011403] (ulepszenie 1) — nazwa] 빈틈 발견!
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011403].levelList[level=1].name
   limit: do 40 znaków
   EN: Found a Gap!
   PL: Found a Gap!
601. [Umiejętność wroga [9011403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL: [OnSucceedAttack] uruchamia [VibrationExplosion]
602. [Umiejętność wroga [9011403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [VibrationExplosion]로 대상이 흐트러졌다면, 코인 재사용
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: If the target is Staggered by [VibrationExplosion], reuse Coin
   PL: jeżeli [VibrationExplosion] oszołomi cel, używa Monety ponownie
603. [Umiejętność wroga [9011501] (ulepszenie 1) — nazwa] 멈추지 말라고
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011501].levelList[level=1].name
   limit: do 40 znaków
   EN: Don't You Stop Now
   PL: Don't You Stop Now
604. [Umiejętność wroga [9011501] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Paralysis]가 있다면, 코인 위력 +1
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011501].levelList[level=1].desc
   (powtórzenie elementu 594 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Umiejętność wroga [9011501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여. [Vibration] 횟수 4 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +4 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 2 [Vibration]. Zwiększa Licznik [Vibration] o 4
606. [Umiejętność wroga [9011502] (ulepszenie 1) — nazwa] 띵해져라!
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011502].levelList[level=1].name
   limit: do 40 znaków
   EN: Dizzy, Eh?!
   PL: Dizzy, Eh?!
607. [Umiejętność wroga [9011502] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Vibration]이 있다면, 코인 위력 +1
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011502].levelList[level=1].desc
   (powtórzenie elementu 597 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Umiejętność wroga [9011502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여. [Vibration] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +3 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 2 [Vibration]. Zwiększa Licznik [Vibration] o 3
609. [Umiejętność wroga [9011502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis] next turn
   PL: [OnSucceedAttack] nakłada 2 [Paralysis] w następnej turze
610. [Umiejętność wroga [9011503] (ulepszenie 1) — nazwa] 어지러워져라!
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011503].levelList[level=1].name
   limit: do 40 znaków
   EN: The Topsy-Turvy!
   PL: The Topsy-Turvy!
611. [Umiejętność wroga [9011503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 601 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Umiejętność wroga [9011503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [VibrationExplosion]로 대상이 흐트러졌다면, 코인 재사용
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 602 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność wroga [9011601] (ulepszenie 1) — nazwa] 사…상처
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011601].levelList[level=1].name
   limit: do 40 znaków
   EN: H-hurt
   PL: H-hurt
614. [Umiejętność wroga [9011601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL: [OnSucceedAttack] nakłada 3 [Burst]
615. [Umiejętność wroga [9011602] (ulepszenie 1) — nazwa] …부수…
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011602].levelList[level=1].name
   limit: do 40 znaków
   EN: ...Brea...
   PL: ...Brea...
616. [Umiejętność wroga [9011602] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 위력이 3이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 3+ [Burst] Potency, Base Power +1
   PL: [WhenUse] jeżeli cel ma 3+ Siły [Burst], Moc Bazowa +1
617. [Umiejętność wroga [9011602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown]
   PL: [OnSucceedAttack] nakłada 1 [DefenseDown]
618. [Umiejętność wroga [9011602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Burst]
619. [Umiejętność wroga [9011602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 617 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Umiejętność wroga [9011602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Umiejętność wroga [9011603] (ulepszenie 1) — nazwa] 약점…
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011603].levelList[level=1].name
   limit: do 40 znaków
   EN: Weakness...
   PL: Weakness...
622. [Umiejętność wroga [9011603] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Burst]이 있다면, [Burst] 위력 3당 기본 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has [Burst], Base Power +1 for every 3 [Burst] Potency on target (max 3)
   PL: [WhenUse] jeżeli cel ma [Burst], Moc Bazowa +1 za każde 3 Siły [Burst] celu (maks. 3)
623. [Umiejętność wroga [9011603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 6 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 6 [Burst]
   PL: [OnSucceedAttack] nakłada 6 [Burst]
624. [Umiejętność wroga [9011603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] nakłada 4 [Laceration]
625. [Umiejętność wroga [9011603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 4 [DefenseDown]
   PL: [OnSucceedAttack] nakłada 4 [DefenseDown]
626. [Umiejętność wroga [9011603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Paralysis]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttackHead] Inflict 2 [Paralysis] next turn
   PL: [OnSucceedAttackHead] nakłada 2 [Paralysis] w następnej turze
627. [Umiejętność wroga [9011604] (ulepszenie 1) — nazwa] 가...
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011604].levelList[level=1].name
   limit: do 40 znaków
   EN: Gua...
   PL: Gua...
628. [Umiejętność wroga [9011604] (ulepszenie 1) — opis] 턴 종료 시 보호막 체력이 남아있다면, 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: If this Unit has remaining Shield HP at Turn End, gain 1 [AttackUp] next turn
   PL: Koniec tury: jeżeli ta jednostka ma pozostałe HP Tarczy, zyskuje 1 [AttackUp] w następnej turze
629. [Umiejętność wroga [9011701] (ulepszenie 1) — nazwa] 늘리…
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011701].levelList[level=1].name
   limit: do 40 znaków
   EN: Exten...
   PL: Exten...
630. [Umiejętność wroga [9011701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Burst]
631. [Umiejętność wroga [9011702] (ulepszenie 1) — nazwa] 가…갑
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011702].levelList[level=1].name
   limit: do 40 znaków
   EN: A-armor Br-
   PL: A-armor Br-
632. [Umiejętność wroga [9011702] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 횟수가 3이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 3+ [Burst] Count, Base Power +1
   PL: [WhenUse] jeżeli cel ma 3+ Licznika [Burst], Moc Bazowa +1
633. [Umiejętność wroga [9011702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [AttackDown] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown]
   PL: [OnSucceedAttack] nakłada 1 [AttackDown]
634. [Umiejętność wroga [9011702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 618 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Umiejętność wroga [9011702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [AttackDown] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 633 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Umiejętność wroga [9011702] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Umiejętność wroga [9011703] (ulepszenie 1) — nazwa] 저미…
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011703].levelList[level=1].name
   limit: do 40 znaków
   EN: Cut You...
   PL: Cut You...
638. [Umiejętność wroga [9011703] (ulepszenie 1) — opis] [WhenUse] 대상에게 [Burst]이 있다면, [Burst] 횟수 2당 기본 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011703].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has [Burst], Base Power +1 for every 2 [Burst] Count on target (max 3)
   PL: [WhenUse] jeżeli cel ma [Burst], Moc Bazowa +1 za każde 2 Licznika [Burst] celu (maks. 3)
639. [Umiejętność wroga [9011703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 4 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +4 [Burst] Count
   PL: [OnSucceedAttack] nakłada 4 Licznika [Burst]
640. [Umiejętność wroga [9011703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Umiejętność wroga [9011703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [AttackDown] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 4 [AttackDown]
   PL: [OnSucceedAttack] nakłada 4 [AttackDown]
642. [Umiejętność wroga [9011703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność wroga [9011704] (ulepszenie 1) — nazwa] 드...
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011704].levelList[level=1].name
   limit: do 40 znaków
   EN: ...rd...
   PL: ...rd...
644. [Umiejętność wroga [9011704] (ulepszenie 1) — moneta 1, efekt 1 — opis] 턴 종료 시 보호막 체력이 남아있다면, 다음 턴에 [AttackUp] 1 얻음
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Umiejętność wroga [9011801] (ulepszenie 1) — nazwa] 처리…
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011801].levelList[level=1].name
   limit: do 40 znaków
   EN: Taking Ca...
   PL: Taking Ca...
646. [Umiejętność wroga [9011801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Burst]
   PL: [OnSucceedAttack] nakłada 4 [Burst]
647. [Umiejętność wroga [9011802] (ulepszenie 1) — nazwa] 치…운…
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011802].levelList[level=1].name
   limit: do 40 znaków
   EN: Remo...ve...
   PL: Remo...ve...
648. [Umiejętność wroga [9011802] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 위력이 3이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011802].levelList[level=1].desc
   (powtórzenie elementu 616 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Umiejętność wroga [9011802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown]
   PL: [OnSucceedAttack] nakłada 2 [DefenseDown]
650. [Umiejętność wroga [9011802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 618 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Umiejętność wroga [9011802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 649 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Umiejętność wroga [9011802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 6 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 623 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Umiejętność wroga [9011803] (ulepszenie 1) — nazwa] 저…지…
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011803].levelList[level=1].name
   limit: do 40 znaków
   EN: Hold... Them Ba...
   PL: Hold... Them Ba...
654. [Umiejętność wroga [9011803] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력 3 피해\n[WhenUse] 대상에게 [Burst]이 있다면, [Burst] 위력 4당 기본 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011803].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Inflict 3 SP damage\n[WhenUse] If target has [Burst], Base Power +1 for every 4 [Burst] Potency on target (max 3)
   PL: [WhenUse] zadaje 3 obrażeń SP\n[WhenUse] jeżeli cel ma [Burst], Moc Bazowa +1 za każde 4 Siły [Burst] celu (maks. 3)
655. [Umiejętność wroga [9011803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 6 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 623 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Umiejętność wroga [9011803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]
   PL: [OnSucceedAttack] nakłada 6 [Laceration]
657. [Umiejętność wroga [9011803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 3 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 3 [DefenseDown]
   PL: [OnSucceedAttack] nakłada 3 [DefenseDown]
658. [Umiejętność wroga [9011803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 599 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Umiejętność wroga [9011804] (ulepszenie 1) — nazwa] 반...
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011804].levelList[level=1].name
   limit: do 40 znaków
   EN: Cou...
   PL: Cou...
660. [Umiejętność wroga [9011804] (ulepszenie 1) — opis] 대상에게 [Burst]이 있다면, 최종 위력+ 1
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has [Burst], Final Power +1
   PL: jeżeli cel ma [Burst], Moc Końcowa +1
661. [Umiejętność wroga [9011804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] nakłada 2 [Laceration]
662. [Umiejętność wroga [9011901] (ulepszenie 1) — nazwa] 비…켜라
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011901].levelList[level=1].name
   limit: do 40 znaków
   EN: M...ove
   PL: M...ove
663. [Umiejętność wroga [9011901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [Umiejętność wroga [9011902] (ulepszenie 1) — nazwa] 막지…라
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011902].levelList[level=1].name
   limit: do 40 znaków
   EN: Get... Out of My...
   PL: Get... Out of My...
665. [Umiejętność wroga [9011902] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 횟수가 3이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011902].levelList[level=1].desc
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Umiejętność wroga [9011902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 2 [AttackDown]
   PL: [OnSucceedAttack] nakłada 2 [AttackDown]
667. [Umiejętność wroga [9011902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Umiejętność wroga [9011902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 666 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Umiejętność wroga [9011902] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 6 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 623 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Umiejętność wroga [9011903] (ulepszenie 1) — nazwa] 돌…파
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011903].levelList[level=1].name
   limit: do 40 znaków
   EN: Break...through
   PL: Break...through
671. [Umiejętność wroga [9011903] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력 3 피해\n[WhenUse] 대상에게 [Burst]이 있다면, [Burst] 횟수 3당 기본 위력 +1 (최대 3)
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011903].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Inflict 3 SP damage\n[WhenUse] If target has [Burst], Base Power +1 for every 3 [Burst] Count on target (max 3)
   PL: [WhenUse] zadaje 3 obrażeń SP\n[WhenUse] jeżeli cel ma [Burst], Moc Bazowa +1 za każde 3 Licznika [Burst] celu (maks. 3)
672. [Umiejętność wroga [9011903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 4 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Umiejętność wroga [9011903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 8 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 8 [Laceration]
   PL: [OnSucceedAttack] nakłada 8 [Laceration]
674. [Umiejętność wroga [9011903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [AttackDown] 3 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 3 [AttackDown]
   PL: [OnSucceedAttack] nakłada 3 [AttackDown]
675. [Umiejętność wroga [9011903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 599 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Umiejętność wroga [9011904] (ulepszenie 1) — nazwa] ...격
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011904].levelList[level=1].name
   limit: do 40 znaków
   EN: ...nter...
   PL: ...nter...
677. [Umiejętność wroga [9011904] (ulepszenie 1) — opis] 대상에게 [Burst]이 있다면, 최종 위력+ 1
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011904].levelList[level=1].desc
   (powtórzenie elementu 660 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Umiejętność wroga [9011904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 661 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Umiejętność wroga [9012001] (ulepszenie 1) — nazwa] 방어 파괴술
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012001].levelList[level=1].name
   limit: do 50 znaków
   EN: Defense Nullification Technique
   PL: Defense Nullification Technique
680. [Umiejętność wroga [9012001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown] next turn
   PL: [OnSucceedAttack] nakłada 2 [DefenseDown] w następnej turze
681. [Umiejętność wroga [9012001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [DefenseDown] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttackHead] Inflict 1 [DefenseDown] next turn
   PL: [OnSucceedAttackHead] nakłada 1 [DefenseDown] w następnej turze
682. [Umiejętność wroga [9012002] (ulepszenie 1) — nazwa] 약점 파악
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012002].levelList[level=1].name
   limit: do 40 znaków
   EN: Grasping Vulnerabilities
   PL: Grasping Vulnerabilities
683. [Umiejętność wroga [9012002] (ulepszenie 1) — opis] [WhenUse] 대상보다 속도가 빠르다면, 자신의 정신력 3 회복
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If this unit's Speed is faster than the target's, heal 3 SP on self
   PL: [WhenUse] jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, przywraca 3 SP
684. [Umiejętność wroga [9012002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 2 [Binding] w następnej turze
685. [Umiejętność wroga [9012002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vulnerable]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttackHead] Inflict 1 [Vulnerable]
   PL: [OnSucceedAttackHead] nakłada 1 [Vulnerable]
686. [Umiejętność wroga [9012002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 680 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Umiejętność wroga [9012002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vulnerable]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttackHead] Inflict 1 [Vulnerable] next turn
   PL: [OnSucceedAttackHead] nakłada 1 [Vulnerable] w następnej turze
688. [Umiejętność wroga [9012003] (ulepszenie 1) — nazwa] 갑주 파쇄
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012003].levelList[level=1].name
   limit: do 40 znaków
   EN: Armor Fracture
   PL: Armor Fracture
689. [Umiejętność wroga [9012003] (ulepszenie 1) — opis] [WhenUse] 대상보다 속도가 빠르다면, [SlashResistDown] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012003].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [SlashResistDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [WhenUse] If this unit's Speed is faster than the target's, inflict 1 [SlashResistDown]
   PL: [WhenUse] jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, nakłada 1 [SlashResistDown]
690. [Umiejętność wroga [9012003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable]
   PL: [OnSucceedAttack] nakłada 1 [Vulnerable]
691. [Umiejętność wroga [9012003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 680 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Umiejętność wroga [9012003] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012003].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 680 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Umiejętność wroga [9012003] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012003].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 687 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Umiejętność wroga [9012004] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012004].levelList[level=1].name
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Umiejętność wroga [9012004] (ulepszenie 1) — opis] [OnSucceedEvade] 자신의 정신력 3 회복
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Heal 3 SP on self
   PL: [OnSucceedEvade] przywraca 3 SP
696. [Umiejętność wroga [9012101] (ulepszenie 1) — nazwa] 맞받아치기
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012101].levelList[level=1].name
   limit: do 40 znaków
   EN: Counterattack
   PL: Counterattack
697. [Umiejętność wroga [9012101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 2 [AttackDown] next turn
   PL: [OnSucceedAttack] nakłada 2 [AttackDown] w następnej turze
698. [Umiejętność wroga [9012101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [AttackDown] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [AttackDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttackHead] Inflict 1 [AttackDown] next turn
   PL: [OnSucceedAttackHead] nakłada 1 [AttackDown] w następnej turze
699. [Umiejętność wroga [9012102] (ulepszenie 1) — nazwa] 제압술
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012102].levelList[level=1].name
   limit: do 40 znaków
   EN: Neutralization Technique
   PL: Neutralization Technique
700. [Umiejętność wroga [9012102] (ulepszenie 1) — opis] [WhenUse] 대상보다 속도가 빠르다면, 자신의 정신력 3 회복
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012102].levelList[level=1].desc
   (powtórzenie elementu 683 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Umiejętność wroga [9012102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 684 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Umiejętność wroga [9012102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Paralysis]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttackHead] Inflict 2 [Paralysis]
   PL: [OnSucceedAttackHead] nakłada 2 [Paralysis]
703. [Umiejętność wroga [9012102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 697 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Umiejętność wroga [9012102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Umiejętność wroga [9012103] (ulepszenie 1) — nazwa] 동작 제압
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012103].levelList[level=1].name
   limit: do 40 znaków
   EN: Immobilisation
   PL: Immobilisation
706. [Umiejętność wroga [9012103] (ulepszenie 1) — opis] [WhenUse] 대상보다 속도가 빠르다면, [SlashResistDown] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012103].levelList[level=1].desc
   (powtórzenie elementu 689 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Umiejętność wroga [9012103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis]
   PL: [OnSucceedAttack] nakłada 2 [Paralysis]
708. [Umiejętność wroga [9012103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 697 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Umiejętność wroga [9012103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 697 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Umiejętność wroga [9012103] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012103].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Umiejętność wroga [9012104] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012104].levelList[level=1].name
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Umiejętność wroga [9012104] (ulepszenie 1) — opis] [OnSucceedEvade] 자신의 정신력 3 회복
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012104].levelList[level=1].desc
   (powtórzenie elementu 695 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Umiejętność wroga [9012201] (ulepszenie 1) — nazwa] 빗겨쳐내기
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012201].levelList[level=1].name
   limit: do 40 znaków
   EN: Parrying
   PL: Parrying
714. [Umiejętność wroga [9012201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 697 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Umiejętność wroga [9012201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttackHead] Inflict 2 [DefenseDown] next turn
   PL: [OnSucceedAttackHead] nakłada 2 [DefenseDown] w następnej turze
716. [Umiejętność wroga [9012202] (ulepszenie 1) — nazwa] 저지술
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012202].levelList[level=1].name
   limit: do 40 znaków
   EN: Suppression
   PL: Suppression
717. [Umiejętność wroga [9012202] (ulepszenie 1) — opis] [WhenUse] 대상보다 속도가 빠르다면, 자신의 정신력 5 회복
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If this unit's Speed is faster than the target's, heal 5 SP on self
   PL: [WhenUse] jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, przywraca 5 SP
718. [Umiejętność wroga [9012202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 2 얻음
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 2 [Agility] next turn
   PL: [OnSucceedAttack] zyskuje 2 [Agility] w następnej turze
719. [Umiejętność wroga [9012202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 707 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Umiejętność wroga [9012202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 680 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Umiejętność wroga [9012202] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Umiejętność wroga [9012203] (ulepszenie 1) — nazwa] 동체 속박술
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012203].levelList[level=1].name
   limit: do 40 znaków
   EN: Restraining Technique
   PL: Restraining Technique
723. [Umiejętność wroga [9012203] (ulepszenie 1) — opis] [WhenUse] 대상보다 속도가 빠르다면, [SlashResistDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012203].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [SlashResistDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [WhenUse] If this unit's Speed is faster than the target's, inflict 2 [SlashResistDown]
   PL: [WhenUse] jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, nakłada 2 [SlashResistDown]
724. [Umiejętność wroga [9012203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable]
   PL: [OnSucceedAttack] nakłada 2 [Vulnerable]
725. [Umiejętność wroga [9012203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [DefenseDown] 3 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttackHead] Inflict 3 [DefenseDown]
   PL: [OnSucceedAttackHead] nakłada 3 [DefenseDown]
726. [Umiejętność wroga [9012203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 697 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Umiejętność wroga [9012203] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012203].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 680 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Umiejętność wroga [9012203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 3 얻음
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 3 [Agility] next turn
   PL: [OnSucceedAttack] zyskuje 3 [Agility] w następnej turze
729. [Umiejętność wroga [9012203] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [SlashResistDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012203].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [OnSucceedAttack] Inflict 2 [SlashResistDown] next turn
   PL: [OnSucceedAttack] nakłada 2 [SlashResistDown] w następnej turze
730. [Umiejętność wroga [9012203] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012203].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność wroga [9012204] (ulepszenie 1) — nazwa] 정리정돈
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012204].levelList[level=1].name
   limit: do 40 znaków
   EN: Housekeeping
   PL: Housekeeping
732. [Umiejętność wroga [9012204] (ulepszenie 1) — opis] [WhenUse] 대상보다 속도가 빠르다면, 합 위력 +3
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If this unit's Speed is faster than the target's, Clash Power +3
   PL: [WhenUse] jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Starcia +3
733. [Umiejętność wroga [9012204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 15 부여, [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 15 [Laceration] and +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 15 [Laceration] i 3 Licznika [Laceration]
734. [Umiejętność wroga [9012204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Umiejętność wroga [9012204] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상보다 속도가 3이상 빠르면, 이 스킬 재사용 (1회)
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012204].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If this unit's Speed is faster than the target's by 3 or more, reuse this Skill (once)
   PL: [OnSucceedAttack] jeżeli Szybkość tej jednostki jest wyższa od Szybkości celu o 3 lub więcej, używa ponownie tę Umiejętność (1 raz)
736. [Umiejętność wroga [9012205] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012205].levelList[level=1].name
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Umiejętność wroga [9012205] (ulepszenie 1) — opis] [OnSucceedEvade] 자신의 정신력 5 회복
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012205].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Heal 5 SP on self
   PL: [OnSucceedEvade] przywraca 5 SP
738. [Umiejętność wroga [9012301] (ulepszenie 1) — nazwa] 쥐잡기
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012301].levelList[level=1].name
   limit: do 40 znaków
   EN: Ratcatching
   PL: Ratcatching
739. [Umiejętność wroga [9012301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] nakłada 3 [Laceration]
740. [Umiejętność wroga [9012301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Laceration]
741. [Umiejętność wroga [9012301] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012301].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Binding]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttackHead] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttackHead] nakłada 1 [Binding] w następnej turze
742. [Umiejętność wroga [9012302] (ulepszenie 1) — nazwa] 비틀기
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012302].levelList[level=1].name
   limit: do 40 znaków
   EN: Twisting
   PL: Twisting
743. [Umiejętność wroga [9012302] (ulepszenie 1) — opis] [WinDuel] 대상의 체력이 100%라면, 피해량 +30%\n[DefeatDuel] [DefenseDown] 3 얻음
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [DefeatDuel], [DefenseDown]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [WinDuel] If the target's HP is at 100%, deal +30% damage\n[DefeatDuel] Gain 3 [DefenseDown]
   PL: [WinDuel] jeżeli HP celu wynosi 100%, zadaje +30% obrażeń\n[DefeatDuel] zyskuje 3 [DefenseDown]
744. [Umiejętność wroga [9012302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Umiejętność wroga [9012302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttackHead] nakłada 2 Licznika [Laceration]
746. [Umiejętność wroga [9012302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력이 5이상이면, 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] If target has 5+ [Laceration] Potency, inflict 1 [Paralysis] next turn
   PL: [OnSucceedAttack] jeżeli cel ma 5+ Siły [Laceration], nakłada 1 [Paralysis] w następnej turze
747. [Umiejętność wroga [9012303] (ulepszenie 1) — nazwa] 상처 비집기
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012303].levelList[level=1].name
   limit: do 40 znaków
   EN: Exacerbate Wound
   PL: Exacerbate Wound
748. [Umiejętność wroga [9012303] (ulepszenie 1) — opis] [WinDuel] [SlashResultUp] 1 얻음
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [SlashResultUp]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [SlashResultUp] = 참격 위력 증가 / Slash Power Up
   EN: [WinDuel] Gain 1 [SlashResultUp]
   PL: [WinDuel] zyskuje 1 [SlashResultUp]
749. [Umiejętność wroga [9012303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 656 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [Umiejętność wroga [9012303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 740 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Umiejętność wroga [9012303] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012303].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Binding]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttackHead] Inflict 2 [Binding] next turn
   PL: [OnSucceedAttackHead] nakłada 2 [Binding] w następnej turze
752. [Umiejętność wroga [9012303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력이 7이상이면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 7+ [Laceration] Potency, deal 20% of damage dealt as bonus damage
   PL: [OnSucceedAttack] jeżeli cel ma 7+ Siły [Laceration], zadaje dodatkowe obrażenia równe 20% zadanych obrażeń
753. [Umiejętność wroga [9012303] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력이 7이상이면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012303].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 752 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Umiejętność wroga [9012304] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012304].levelList[level=1].name
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Umiejętność wroga [9012304] (ulepszenie 1) — opis] [OnSucceedEvade] 자신의 정신력 3 회복
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012304].levelList[level=1].desc
   (powtórzenie elementu 695 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Umiejętność wroga [9012403] (ulepszenie 1) — nazwa] 신경 비집기
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012403].levelList[level=1].name
   limit: do 40 znaków
   EN: Nerve Mutilation
   PL: Nerve Mutilation
757. [Umiejętność wroga [9012403] (ulepszenie 1) — opis] [WinDuel] [SlashResultUp] 1 얻음
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012403].levelList[level=1].desc
   (powtórzenie elementu 748 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [Umiejętność wroga [9012403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 656 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Umiejętność wroga [9012403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 740 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [Umiejętność wroga [9012403] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012403].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Umiejętność wroga [9012403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력이 7이상이면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 752 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Umiejętność wroga [9012403] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력이 7이상이면, 피해량의 20%만큼 추가 피해
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012403].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 752 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Umiejętność wroga [9012501] (ulepszenie 1) — nazwa] 쥐사냥
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012501].levelList[level=1].name
   limit: do 40 znaków
   EN: Rat Hunt
   PL: Rat Hunt
764. [Umiejętność wroga [9012501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL: [OnSucceedAttack] nakłada 5 [Laceration]
765. [Umiejętność wroga [9012501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Laceration]
766. [Umiejętność wroga [9012501] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012501].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 684 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Umiejętność wroga [9012502] (ulepszenie 1) — nazwa] 쥐몰이
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012502].levelList[level=1].name
   limit: do 40 znaków
   EN: Rat Herding
   PL: Rat Herding
768. [Umiejętność wroga [9012502] (ulepszenie 1) — opis] [WinDuel] 대상의 체력이 80%이상이라면, 피해량 +50%\n[DefeatDuel] [DefenseDown] 2 얻음
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [DefeatDuel], [DefenseDown]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [WinDuel] If the target's HP is at 80%+, deal +50% damage\n[DefeatDuel] Gain 2 [DefenseDown]
   PL: [WinDuel] jeżeli HP celu wynosi 80% lub więcej, zadaje +50% obrażeń\n[DefeatDuel] zyskuje 2 [DefenseDown]
769. [Umiejętność wroga [9012502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Umiejętność wroga [9012502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 745 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Umiejętność wroga [9012502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력이 5이상이면, 피해량의 20%만큼 추가 피해 입힘
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] If target has 5+ [Laceration] Potency, deal 20% of damage dealt as bonus damage
   PL: [OnSucceedAttack] jeżeli cel ma 5+ Siły [Laceration], zadaje dodatkowe obrażenia równe 20% zadanych obrażeń
772. [Umiejętność wroga [9012503] (ulepszenie 1) — nazwa] 불청객 처리술
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012503].levelList[level=1].name
   limit: do 40 znaków
   EN: Interloper Banishment
   PL: Interloper Banishment
773. [Umiejętność wroga [9012503] (ulepszenie 1) — opis] [WhenUse] 대상보다 속도가 3이상 빠르면, 이 스킬 재사용 (최대 1)
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If this unit's Speed is faster than target's by 3 or more, reuse this Skill (once)
   PL: [WhenUse] jeżeli Szybkość przewyższa Szybkość celu o 3 lub więcej, używa ponownie tę Umiejętność (1 raz)
774. [Umiejętność wroga [9012503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 10 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 10 [Laceration]
   PL: [OnSucceedAttack] nakłada 10 [Laceration]
775. [Umiejętność wroga [9012503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 685 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [Umiejętność wroga [9012503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력만큼 흐트러짐 손상을 입힘
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Raise target's Stagger Threshold by value equal to [Laceration] on target
   PL: [OnSucceedAttack] podnosi Próg Oszołomienia celu o wartość [Laceration] celu
777. [Umiejętność wroga [9012503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Umiejętność wroga [9012503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력이 12이상이면, [AttackDown] 3 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] If target has 12+ [Laceration], inflict 3 [AttackDown]
   PL: [OnSucceedAttack] jeżeli cel ma 12+ [Laceration], nakłada 3 [AttackDown]
779. [Umiejętność wroga [9012503] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 위력이 15이상이면, 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012503].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] If target has 15+ [Laceration] Potency, inflict 2 [Vulnerable] next turn
   PL: [OnSucceedAttack] jeżeli cel ma 15+ Siły [Laceration], nakłada 2 [Vulnerable] w następnej turze
780. [Umiejętność wroga [9012504] (ulepszenie 1) — nazwa] 상자 수여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012504].levelList[level=1].name
   limit: do 40 znaków
   EN: Box Conferment
   PL: Box Conferment
781. [Umiejętność wroga [9012504] (ulepszenie 1) — opis] [WhenUse] 대상보다 속도가 3이상 빠르면, 합 위력 +2\n[WinDuel] 자신의 정신력 10 회복
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012504].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If this unit's Speed is faster than the target's by 3 or more, Clash Power +2\n[WinDuel] Heal 10 SP on self
   PL: [WhenUse] jeżeli Szybkość tej jednostki jest wyższa od Szybkości celu o 3 lub więcej, Moc Starcia +2\n[WinDuel] przywraca 10 SP
782. [Umiejętność wroga [9012504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DefenseDown] 3 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Umiejętność wroga [9012504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 10 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 774 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Umiejętność wroga [9012504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 10 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 10 [Combustion]
   PL: [OnSucceedAttack] nakłada 10 [Combustion]
785. [Umiejętność wroga [9012505] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012505].levelList[level=1].name
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Umiejętność wroga [9012505] (ulepszenie 1) — opis] [OnSucceedEvade] 자신의 정신력 5 회복
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012505].levelList[level=1].desc
   (powtórzenie elementu 737 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Umiejętność wroga [9012601] (ulepszenie 1) — nazwa] 청소 시작
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012601].levelList[level=1].name
   limit: do 40 znaków
   EN: Housekeeping Start
   PL: Housekeeping Start
788. [Umiejętność wroga [9012601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Umiejętność wroga [9012601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Umiejętność wroga [9012601] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012601].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 741 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Umiejętność wroga [9012602] (ulepszenie 1) — nazwa] 불청객 맞이
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012602].levelList[level=1].name
   limit: do 40 znaków
   EN: Interloper Reception
   PL: Interloper Reception
792. [Umiejętność wroga [9012602] (ulepszenie 1) — opis] [WinDuel] [PlusCoinValueUp] 1 얻음\n[DefeatDuel] [Sinking] 3 얻음
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [PlusCoinValueUp], [DefeatDuel], [Sinking]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost; [DefeatDuel] = [합 패배] / [Clash Lose]; [Sinking] = 침잠 / Sinking
   EN: [WinDuel] Gain 1 [PlusCoinValueUp]\n[DefeatDuel] Gain 3 [Sinking]
   PL: [WinDuel] zyskuje 1 [PlusCoinValueUp]\n[DefeatDuel] zyskuje 3 [Sinking]
793. [Umiejętność wroga [9012602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 8 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 8 [Sinking]
   PL: [OnSucceedAttack] nakłada 8 [Sinking]
794. [Umiejętność wroga [9012602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Sinking]
795. [Umiejętność wroga [9012603] (ulepszenie 1) — nazwa] 접객도 2식 구속
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012603].levelList[level=1].name
   limit: do 40 znaków
   EN: Reception Arts 2: Bind
   PL: Reception Arts 2: Bind
796. [Umiejętność wroga [9012603] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 위력 5당, 기본 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Base Power +1 for every 5 [Sinking] Potency on target (max 2)
   PL: [WhenUse] Moc Bazowa +1 za każde 5 Siły [Sinking] celu (maks. 2)
797. [Umiejętność wroga [9012603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 1 [Binding] w następnej turze
798. [Umiejętność wroga [9012603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 649 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Umiejętność wroga [9012603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 797 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Umiejętność wroga [9012603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 649 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Umiejętność wroga [9012603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking] 위력이 8이상이면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target has 8+ [Sinking] Potency, Reuse this Coin (1 time max)
   PL: [OnSucceedAttack] jeżeli cel ma 8+ Siły [Sinking], używa Monety ponownie (maks. 1 raz)
802. [Umiejętność wroga [9012603] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] [DefenseDown] 4, [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012603].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseDown], [Vulnerable]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttackHead] Inflict 4 [DefenseDown] 4 and 1 [Vulnerable]
   PL: [OnSucceedAttackHead] nakłada 4 [DefenseDown] i 1 [Vulnerable]
803. [Umiejętność wroga [9012604] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012604].levelList[level=1].name
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Umiejętność wroga [9012604] (ulepszenie 1) — opis] 턴 종료 시 보호막이 남아있다면, 10만큼 흐트러짐 회복\n보호막 체력을 전부 소모했다면, 마지막 공격자 정신력 10 회복
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012604].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If this unit has remaining Shield HP at Turn End, lower Stagger threshold by 10\nIf this unit's Shield HP is depleted, the last attacker heals 10 SP
   PL: Koniec tury: jeżeli ta jednostka ma pozostałe HP Tarczy, obniża Próg Oszołomienia o 10\njeżeli HP Tarczy zostało całkowicie zużyte, ostatni atakujący przywraca 10 SP
805. [Umiejętność wroga [9012701] (ulepszenie 1) — nazwa] 청소 개시
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012701].levelList[level=1].name
   limit: do 40 znaków
   EN: Commence Housekeeping
   PL: Commence Housekeeping
806. [Umiejętność wroga [9012701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Umiejętność wroga [9012701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Umiejętność wroga [9012701] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012701].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Paralysis]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttackHead] Inflict 1 [Paralysis] next turn
   PL: [OnSucceedAttackHead] nakłada 1 [Paralysis] w następnej turze
809. [Umiejętność wroga [9012702] (ulepszenie 1) — nazwa] 불청객 응대
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012702].levelList[level=1].name
   limit: do 40 znaków
   EN: Interloper Response
   PL: Interloper Response
810. [Umiejętność wroga [9012702] (ulepszenie 1) — opis] [WinDuel] [PlusCoinValueUp] 1 얻음\n[DefeatDuel] [Sinking] 3 얻음
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012702].levelList[level=1].desc
   (powtórzenie elementu 792 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Umiejętność wroga [9012702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 794 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
812. [Umiejętność wroga [9012702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 794 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [Umiejętność wroga [9012703] (ulepszenie 1) — nazwa] 접객도 2식 탈력
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012703].levelList[level=1].name
   limit: do 40 znaków
   EN: Reception Arts 2: Topple
   PL: Reception Arts 2: Topple
814. [Umiejętność wroga [9012703] (ulepszenie 1) — opis] 대상의 [Sinking] 위력 5당, 기본 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012703].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Base Power +1 for every 5 [Sinking] Potency on target (max 2)
   PL: Moc Bazowa +1 za każde 5 Siły [Sinking] celu (maks. 2)
815. [Umiejętność wroga [9012703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 599 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [Umiejętność wroga [9012703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 666 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Umiejętność wroga [9012703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 599 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Umiejętność wroga [9012703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AttackDown] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 666 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Umiejętność wroga [9012703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking] 횟수 4이상이면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target has 4+ [Sinking] Count, Reuse this Coin (1 time max)
   PL: [OnSucceedAttack] jeżeli cel ma 4+ Licznika [Sinking], używa Monety ponownie (maks. 1 raz)
820. [Umiejętność wroga [9012703] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [AttackDown] 4, [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012703].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [AttackDown], [Paralysis]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttackHead] Inflict 4 [AttackDown] and 1 [Paralysis] next turn
   PL: [OnSucceedAttackHead] nakłada 4 [AttackDown] i 1 [Paralysis] w następnej turze
821. [Umiejętność wroga [9012704] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012704].levelList[level=1].name
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
822. [Umiejętność wroga [9012704] (ulepszenie 1) — opis] 턴 종료 시 보호막이 남아있다면, 10만큼 흐트러짐 회복\n보호막 체력을 전부 소모했다면, 마지막 공격자 정신력 10 회복
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9012704].levelList[level=1].desc
   (powtórzenie elementu 804 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [Umiejętność wroga [9101401] (ulepszenie 1) — nazwa] 노크
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101401].levelList[level=1].name
   limit: do 40 znaków
   EN: Knocking
   PL: Knocking
824. [Umiejętność wroga [9101401] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 위력이 5이상이면, [AttackDown] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking], [AttackDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [WhenUse] If target has 5+ [Sinking] Potency, inflict 1 [AttackDown]
   PL: [WhenUse] jeżeli cel ma 5+ Siły [Sinking], nakłada 1 [AttackDown]
825. [Umiejętność wroga [9101401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Umiejętność wroga [9101401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 797 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Umiejętność wroga [9101401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [Umiejętność wroga [9101401] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101401].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 599 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Umiejętność wroga [9101402] (ulepszenie 1) — nazwa] 청소 시간이다!
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101402].levelList[level=1].name
   limit: do 40 znaków
   EN: Time to Clean!
   PL: Time to Clean!
830. [Umiejętność wroga [9101402] (ulepszenie 1) — opis] [WhenUse] 대상의 정신력이 10이하라면, [AttackDown] 2 부여\n[WinDuel] [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101402].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [AttackDown], [WinDuel], [Vulnerable]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [WinDuel] = [합 승리시] / [Clash Win]; [Vulnerable] = 취약 / Fragile
   EN: [WhenUse] If the target is at 10 or less SP, inflict 2 [AttackDown]\n[WinDuel] Inflict 1 [Vulnerable]
   PL: [WhenUse] jeżeli SP celu wynosi 10 lub mniej, nakłada 2 [AttackDown]\n[WinDuel] nakłada 1 [Vulnerable]
831. [Umiejętność wroga [9101402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 더하기 코인 약화 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Plus Coin Drop next turn
   PL: [OnSucceedAttack] nakłada 1 Osłabienia Monet Plus w następnej turze
832. [Umiejętność wroga [9101402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 794 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Umiejętność wroga [9101402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 2 [Vulnerable] w następnej turze
834. [Umiejętność wroga [9101403] (ulepszenie 1) — nazwa] 마님의 분부대로...!
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101403].levelList[level=1].name
   limit: do 40 znaków
   EN: As Mistress Commands...!
   PL: As Mistress Commands...!
835. [Umiejętność wroga [9101403] (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking] 위력 3당 기본 위력 +1 (최대 3)\n[WinDuel] 모든 아군 정신력 5 회복
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101403].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Base Power +1 for every 3 [Sinking] Potency on target (max 3)\n[WinDuel] All allies heal 5 SP
   PL: [WhenUse] Moc Bazowa +1 za każde 3 Siły [Sinking] celu (maks. 3)\n[WinDuel] wszyscy sojusznicy przywracają 5 SP
836. [Umiejętność wroga [9101403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 8 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 793 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Umiejętność wroga [9101403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttackHead] nakłada 2 Licznika [Sinking]
838. [Umiejętność wroga [9101403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 8 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 793 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Umiejętność wroga [9101403] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101403].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 837 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Umiejętność wroga [9101403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [EchoOfMansion] 2 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EchoOfMansion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EchoOfMansion] = 저택의 메아리 / Echoes of the Manor
   EN: [OnSucceedAttack] Inflict 2 [EchoOfMansion] next turn
   PL: [OnSucceedAttack] nakłada 2 [EchoOfMansion] w następnej turze
841. [Umiejętność wroga [9101403] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 8 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101403].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 793 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
842. [Umiejętność wroga [9101403] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttackHead] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101403].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 837 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Umiejętność wroga [9101404] (ulepszenie 1) — nazwa] 먼지...한 톨 없이!
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101404].levelList[level=1].name
   limit: do 40 znaków
   EN: Not Even a Speck of Dust!
   PL: Not Even a Speck of Dust!
844. [Umiejętność wroga [9101404] (ulepszenie 1) — opis] [StartBattle] 자신을 포함한 모든 아군에게 [AttackUp] 3, 정신력 15 회복\n[StartBattle] 자신을 제외한 모든 아군에게 [Vulnerable] 1 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101404].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [AttackUp], [Vulnerable]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Vulnerable] = 취약 / Fragile
   EN: [StartBattle] Apply 3 [AttackUp] and heal 15 SP for all allies, including this unit\n[StartBattle] Inflict 1 [Vulnerable] to all other allies
   PL: [StartBattle] nakłada 3 [AttackUp] i przywraca 15 SP wszystkim sojusznikom (łącznie z tą jednostką)\n[StartBattle] nakłada 1 [Vulnerable] wszystkim pozostałym sojusznikom
845. [Umiejętność wroga [9101404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking] 위력만큼 우울 속성 추가 피해 입힘. [Sinking] 횟수 1 감소
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict Gloom Affinity bonus damage equal to [Sinking] Potency on target. Reduce [Sinking] Count on target by 1
   PL: [OnSucceedAttack] zadaje celowi dodatkowe obrażenia Posępności równe Siły [Sinking] celu. Zmniejsza Licznik [Sinking] celu o 1
846. [Umiejętność wroga [9101404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking] 위력만큼 우울 속성 추가 피해 입힘. [Sinking] 횟수 1 감소
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 845 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Umiejętność wroga [9101404] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking] 위력만큼 우울 속성 추가 피해 입힘. [Sinking] 횟수 1 감소
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101404].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 845 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Umiejętność wroga [9101404] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101404].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Umiejętność wroga [9101404] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 대상의 [Sinking] 횟수가 3이상이면, 이 코인 재사용. (최대 2회)
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101404].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target has 3+ [Sinking] Count, Reuse this Coin (twice)
   PL: [OnSucceedAttack] jeżeli cel ma 3+ Licznika [Sinking], używa Monety ponownie (do 2 razy)
850. [Umiejętność wroga [9101405] (ulepszenie 1) — nazwa] 쥐새끼 같은 놈!
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101405].levelList[level=1].name
   limit: do 40 znaków
   EN: Slippery Rat!
   PL: Slippery Rat!
851. [Umiejętność wroga [9101405] (ulepszenie 1) — opis] 턴 종료 시 보호막이 남아있다면, 50만큼 흐트러짐 회복\n보호막 체력을 전부 소모했다면, 모든 적의 정신력 10 회복
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9101405].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If this unit has remaining Shield HP at Turn End, lower Stagger threshold by 50\nIf this unit's Shield HP is depleted, all enemies heal 10 SP
   PL: Koniec tury: jeżeli ta jednostka ma pozostałe HP Tarczy, obniża Próg Oszołomienia o 50\njeżeli HP Tarczy zostało całkowicie zużyte, wszyscy wrogowie przywracają 10 SP
852. [Umiejętność wroga [9011404] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c6p1.json :: dataList[id=9011404].levelList[level=1].name
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c6p1] Pasywka wroga: Passives_Enemy-a1c6p1
- plik gry: `Passives_Enemy-a1c6p1.json`

853. [[a1c6p1] Pasywka wroga [9011601] — nazwa] 너로...구
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9011601].name
   limit: do 40 znaków
   EN: It's... you...
   PL: It's... you...
854. [[a1c6p1] Pasywka wroga [9011601] — opis] 전투 시작 시 체력이 가장 낮은 적이라면, 피해량 +10%
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9011601].desc
   limit: do 120 znaków
   EN: Deal +10% damage to targets with the least HP
   PL: zadaje +10% obrażeń celom z najniższym HP
855. [[a1c6p1] Pasywka wroga [9011601] — podsumowanie] 피해량 +10%
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9011601].summary
   limit: do 120 znaków
   EN: Damage +10%
   PL: zadaje +10% obrażeń
856. [[a1c6p1] Pasywka wroga [9011801] — nazwa] ...
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9011801].name
   limit: do 40 znaków
   EN: ...
   PL: ...
857. [[a1c6p1] Pasywka wroga [9011801] — opis] 합 패배시, 대상의 정신력 3 피해
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9011801].desc
   limit: do 120 znaków
   EN: Target takes 3 SP damage if this unit loses the clash
   PL: po przegranej w Starciu cel otrzymuje 3 obrażeń SP
858. [[a1c6p1] Pasywka wroga [9011801] — podsumowanie] 대상의 정신력 3 피해
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9011801].summary
   limit: do 120 znaków
   EN: Target takes 3 SP damage
   PL: cel otrzymuje 3 obrażeń SP
859. [[a1c6p1] Pasywka wroga [9012001] — nazwa] 정돈
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012001].name
   limit: do 40 znaków
   EN: Cleaning
   PL: Cleaning
860. [[a1c6p1] Pasywka wroga [9012001] — opis] 스킬 사용시 대상의 체력이 50%미만일 때, 스킬 위력 +1
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012001].desc
   limit: do 120 znaków
   EN: When using a Skill, if target's HP is below 50%, Skill Power +1
   PL: przy użyciu Umiejętności, jeżeli HP celu jest poniżej 50%, Moc Umiejętności +1
861. [[a1c6p1] Pasywka wroga [9012001] — podsumowanie] 스킬 위력 +1
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012001].summary
   limit: do 120 znaków
   EN: Skill Power +1
   PL: Moc Umiejętności +1
862. [[a1c6p1] Pasywka wroga [9012201] — nazwa] 정리
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012201].name
   limit: do 40 znaków
   EN: Organizing
   PL: Organizing
863. [[a1c6p1] Pasywka wroga [9012201] — opis] 스킬 사용 시 대상의 체력이 50%미만일 때, 피해량 +30%
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012201].desc
   limit: do 120 znaków
   EN: When using a Skill, if target's HP is below 50%, deal +30% damage
   PL: przy użyciu Umiejętności, jeżeli HP celu jest poniżej 50%, zadaje +30% obrażeń
864. [[a1c6p1] Pasywka wroga [9012201] — podsumowanie] 피해량 +30%
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012201].summary
   limit: do 120 znaków
   EN: Damage +30%
   PL: zadaje +30% obrażeń
865. [[a1c6p1] Pasywka wroga [9012301] — nazwa] 독 안에 든 쥐
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012301].name
   limit: do 40 znaków
   EN: Dead End
   PL: Dead End
866. [[a1c6p1] Pasywka wroga [9012301] — opis] 스킬 사용 시 자신의 속도가 대상보다 빠르면, 합 위력 +1
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012301].desc
   limit: do 120 znaków
   EN: When using a Skill, if this unit's Speed is faster than the target's, Clash Power +1
   PL: przy użyciu Umiejętności, jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Starcia +1
867. [[a1c6p1] Pasywka wroga [9012301] — podsumowanie] 합 위력 +1
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012301].summary
   limit: do 120 znaków
   EN: Clash Power +1
   PL: Moc Starcia +1
868. [[a1c6p1] Pasywka wroga [9012501] — nazwa] 쥐사냥
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012501].name
   (powtórzenie elementu 763 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [[a1c6p1] Pasywka wroga [9012501] — opis] 스킬 사용 시 자신의 속도가 대상보다 빠르면, 합 위력 +1, 피해량 +20%
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012501].desc
   limit: do 150 znaków
   EN: When using a Skill, if this unit's Speed is faster than the target's, gain Clash Power +1 and deal +20% damage
   PL: przy użyciu Umiejętności, jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Starcia +1 i zadaje +20% obrażeń
870. [[a1c6p1] Pasywka wroga [9012501] — podsumowanie] 합 위력 +1, 피해량 +20%
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012501].summary
   limit: do 120 znaków
   EN: Clash Power +1, deal +20% damage
   PL: Moc Starcia +1, zadaje +20% obrażeń
871. [[a1c6p1] Pasywka wroga [9012601] — nazwa] 최선을... 다하겠습니다
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012601].name
   limit: do 40 znaków
   EN: I Will... Do My Best
   PL: I Will... Do My Best
872. [[a1c6p1] Pasywka wroga [9012601] — opis] 턴 종료시 흐트러짐 상태가 되었을 때, 정신력 12 회복. 다음 턴에 방어 레벨 감소 2 얻음. (최대 1회)
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012601].desc
   limit: do 120 znaków
   EN: Turn End: if Staggered, heal 12 SP. Gain 2 Defense Level Down next turn. (one time max)
   PL: Koniec tury: jeżeli przechodzi w Oszołamienie, przywraca 12 SP. Zyskuje 2 Spadek Poziomu Obrony (maks. 1).
873. [[a1c6p1] Pasywka wroga [9012602] — nazwa] 죄송합니다...마님!
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012602].name
   limit: do 40 znaków
   EN: Apologies... Mistress!
   PL: Apologies... Mistress!
874. [[a1c6p1] Pasywka wroga [9012602] — opis] 턴 종료 시 패닉 상태에서 벗어났다면, 다음 턴에 공격 위력 증가 1 얻음
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012602].desc
   limit: do 120 znaków
   EN: Turn End: if this unit recovered from Panic, gain 1 Attack Power Up next turn
   PL: Koniec tury: jeżeli dochodzi do siebie z Paniki, zyskuje 1 Wzrost Mocy Ataku w następnej turze
875. [[a1c6p1] Pasywka wroga [9012602] — podsumowanie] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9012602].summary
   limit: do 120 znaków
   EN: Gain 1 Attack Power Up next turn
   PL: zyskuje 1 Wzrost Mocy Ataku w następnej turze
876. [[a1c6p1] Pasywka wroga [9101401] — nazwa] 제대로 치워주지...
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9101401].name
   limit: do 40 znaków
   EN: I'll Clean You Up...
   PL: I'll Clean You Up...
877. [[a1c6p1] Pasywka wroga [9101401] — opis] 턴 종료시 흐트러짐 상태가 되었을 때, 흐트러짐 상태에서 벗어나고 정신력 20 회복. 다음 턴에 공격 레벨 증가 1 얻음. (최대 1)
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9101401].desc
   limit: do 150 znaków
   EN: Turn End: if Staggered, recover from the Staggered state and heal 20 SP. Gain 1 Offense Level Up next turn. (1 max)
   PL: Koniec tury: jeżeli przechodzi w Oszołamienie, dochodzi do siebie i przywraca 20 SP. Zyskuje 1 Wzrost Poziomu Ataku w następnej turze (maks. 1).
878. [[a1c6p1] Pasywka wroga [9101402] — nazwa] 무례한 것!
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9101402].name
   limit: do 40 znaków
   EN: Insolent Fool!
   PL: Insolent Fool!
879. [[a1c6p1] Pasywka wroga [9101402] — opis] 대상이 자신보다 속도가 낮다면, 합 위력 +2
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9101402].desc
   limit: do 120 znaków
   EN: If this unit's Speed is faster than the target's, Clash Power +2
   PL: jeżeli Szybkość tej jednostki jest wyższa niż Szybkość celu, Moc Starcia +2
880. [[a1c6p1] Pasywka wroga [9101402] — podsumowanie] 합 위력 +2
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9101402].summary
   limit: do 120 znaków
   EN: Clash Power +2
   PL: Moc Starcia +2
881. [[a1c6p1] Pasywka wroga [9101403] — nazwa] 마님의 소리가...!
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9101403].name
   limit: do 40 znaków
   EN: The Mistress's Voice...!
   PL: The Mistress's Voice...!
882. [[a1c6p1] Pasywka wroga [9101403] — opis] 한 공격 스킬의 코인이 모두 앞면이라면, 정신력 10 회복
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9101403].desc
   limit: do 120 znaków
   EN: Heal 10 SP when every Coin of an Attack Skill flips heads
   PL: przywraca 10 SP, gdy wszystkie Monety Umiejętności ataku wypadną Awersami
883. [[a1c6p1] Pasywka wroga [9101403] — podsumowanie] 정신력 10 회복
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9101403].summary
   limit: do 120 znaków
   EN: Heal 10 SP
   PL: przywraca 10 SP
884. [[a1c6p1] Pasywka wroga [9101404] — nazwa] 마님, 보고 계신가요?!
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9101404].name
   limit: do 50 znaków
   EN: Will You Witness Me, Mistress?!
   PL: Will You Witness Me, Mistress?!
885. [[a1c6p1] Pasywka wroga [9101404] — opis] 공격시 대상에게 침잠이 있고 대상의 정신력이 -15이하라면, 다음 턴에 공격 레벨 증가 3 얻음. (대상당 한 번)
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9101404].desc
   limit: do 160 znaków
   EN: If the target has Sinking, and if the target has -15 or less SP, gain 3 Offense Level Up next turn. (once per target)
   PL: przy ataku, jeżeli cel ma Zatonięcie i SP celu wynosi -15 lub mniej, zyskuje 3 Wzrost Poziomu Ataku w następnej turze. (1 raz na cel)
886. [[a1c6p1] Pasywka wroga [9999999] — nazwa] 패닉 회복
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9999999].name
   limit: do 40 znaków
   EN: Panic Recovery
   PL: Panic Recovery
887. [[a1c6p1] Pasywka wroga [9999999] — opis] 턴 종료 시 패닉 상태라면 정신력이 0이됨.
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9999999].desc
   limit: do 120 znaków
   EN: Turn End: if in Panic, reset SP to 0.
   PL: Koniec tury: jeżeli jest w Panice, SP wraca do 0.
888. [[a1c6p1] Pasywka wroga [9999998] — nazwa] 패닉 변경 불가
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9999998].name
   limit: do 40 znaków
   EN: Fixed Panic
   PL: Panika zablokowana
889. [[a1c6p1] Pasywka wroga [9999998] — opis] 패닉 유형을 변경하는 버프 획득 시, 패닉 유형이 변경되지 않음. 대신 정신력이 없는 대상에게 부여되는 효과가 부여됨
   źródło: Passives_Enemy-a1c6p1.json :: dataList[id=9999998].desc
   limit: do 240 znaków
   EN: This unit's Panic Type does not change when inflicted with an effect that changes Panic Types. Instead, this unit is inflicted with an effect that is inflicted against Non-SP Units.
   PL: gdy ta jednostka zyskuje Efekt zmieniający typ Paniki, typ Paniki się nie zmienia. Zamiast tego nakładany jest efekt nakładany na jednostki bez SP.

## [a1c6p2] Wróg / część: Enemies-a1c6p2
- plik gry: `Enemies-a1c6p2.json`

890. [[a1c6p2] Wróg / część [90128] — nazwa] 완고한 외우피 해결사
   źródło: Enemies-a1c6p2.json :: dataList[id=90128].name
   limit: do 40 znaków
   EN: Stubborn Öufi Fixer
   PL: Stubborn Öufi Fixer
891. [[a1c6p2] Wróg / część [90129] — nazwa] 철저한 외우피 해결사
   źródło: Enemies-a1c6p2.json :: dataList[id=90129].name
   limit: do 40 znaków
   EN: Precise Öufi Fixer
   PL: Precise Öufi Fixer
892. [[a1c6p2] Wróg / część [90130] — nazwa] 외우피 해결사 부장
   źródło: Enemies-a1c6p2.json :: dataList[id=90130].name
   limit: do 40 znaków
   EN: Öufi Assoc. Director
   PL: Öufi Assoc. Director
893. [[a1c6p2] Wróg / część [90131] — nazwa] 심취한 약지 연구원?
   źródło: Enemies-a1c6p2.json :: dataList[id=90131].name
   limit: do 50 znaków
   EN: Enamored Researcher of the Ring?
   PL: Enamored Researcher of the Ring?
894. [[a1c6p2] Wróg / część [90132] — nazwa] 광적인 약지 연구원?
   źródło: Enemies-a1c6p2.json :: dataList[id=90132].name
   limit: do 40 znaków
   EN: Mad Researcher of the Ring?
   PL: Mad Researcher of the Ring?
895. [[a1c6p2] Wróg / część [90133] — nazwa] 점묘파 약지 연구원?
   źródło: Enemies-a1c6p2.json :: dataList[id=90133].name
   limit: do 50 znaków
   EN: Pointillist Researcher of the Ring?
   PL: Pointillist Researcher of the Ring?
896. [[a1c6p2] Wróg / część [91015] — nazwa] 힌들리
   źródło: Enemies-a1c6p2.json :: dataList[id=91015].name
   limit: do 40 znaków
   EN: Hindley
   PL: Hindley
897. [[a1c6p2] Wróg / część [8204] — nazwa] 데드레빗츠 보스
   źródło: Enemies-a1c6p2.json :: dataList[id=8204].name
   limit: do 40 znaków
   EN: Dead Rabbits Boss
   PL: Dead Rabbits Boss
898. [[a1c6p2] Wróg / część [8159] — nazwa] 나태 죄종?
   źródło: Enemies-a1c6p2.json :: dataList[id=8159].name
   limit: do 40 znaków
   EN: Peccatulum Pigritiae?
   PL: Peccatulum Pigritiae?
899. [[a1c6p2] Wróg / część [8160] — nazwa] 탐식 죄종?
   źródło: Enemies-a1c6p2.json :: dataList[id=8160].name
   limit: do 40 znaków
   EN: Peccatulum Gulae?
   PL: Peccatulum Gulae?
900. [[a1c6p2] Wróg / część [8162] — nazwa] 기묘한 데드레빗츠 단원
   źródło: Enemies-a1c6p2.json :: dataList[id=8162].name
   limit: do 50 znaków
   EN: Bizarre Dead Rabbits Henchman
   PL: Bizarre Dead Rabbits Henchman
901. [[a1c6p2] Wróg / część [8163] — nazwa] 뒤덮인 데드레빗츠 단원
   źródło: Enemies-a1c6p2.json :: dataList[id=8163].name
   limit: do 40 znaków
   EN: Veiled Dead Rabbits Henchman
   PL: Veiled Dead Rabbits Henchman
902. [[a1c6p2] Wróg / część [8164] — nazwa] 히스클리프?
   źródło: Enemies-a1c6p2.json :: dataList[id=8164].name
   limit: do 40 znaków
   EN: Heathcliff?
   PL: Heathcliff?
903. [[a1c6p2] Wróg / część [8165] — nazwa] 빼앗겨 울부짖는 힌들리
   źródło: Enemies-a1c6p2.json :: dataList[id=8165].name
   limit: do 40 znaków
   EN: Hindley, The Reaved Lamenter
   PL: Hindley, The Reaved Lamenter
904. [[a1c6p2] Wróg / część [90134] — nazwa] 기묘한 데드레빗츠 단원
   źródło: Enemies-a1c6p2.json :: dataList[id=90134].name
   (powtórzenie elementu 900 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [[a1c6p2] Wróg / część [90135] — nazwa] 뒤덮인 데드레빗츠 단원
   źródło: Enemies-a1c6p2.json :: dataList[id=90135].name
   (powtórzenie elementu 901 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c6p2] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c6p2
- grupa rozdziału/trybu: `a1c6p2` · plik: `Skills_Abnormality-a1c6p2.json`

906. [Umiejętność wroga [815901] (ulepszenie 1) — nazwa] 손아귀
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815901].levelList[level=1].name
   limit: do 40 znaków
   EN: Grasp
   PL: Grasp
907. [Umiejętność wroga [815901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여. [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 595 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Umiejętność wroga [815901] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815901].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 751 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
909. [Umiejętność wroga [815902] (ulepszenie 1) — nazwa] 돌 쌓기
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815902].levelList[level=1].name
   limit: do 40 znaków
   EN: Piling Rocks
   PL: Piling Rocks
910. [Umiejętność wroga [815902] (ulepszenie 1) — opis] [WhenUse] 대상의 [Vibration]이 5 이상이면, 합 위력 +1
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 5+ [Vibration], Clash Power +1
   PL: [WhenUse] jeżeli cel ma 5+ [Vibration], Moc Starcia +1
911. [Umiejętność wroga [815902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Vibration]
912. [Umiejętność wroga [815902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 599 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
913. [Umiejętność wroga [815902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 8 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 8 [Vibration]
   PL: [OnSucceedAttack] nakłada 8 [Vibration]
914. [Umiejętność wroga [815902] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 697 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
915. [Umiejętność wroga [815903] (ulepszenie 1) — nazwa] 나태한 짓누름
   źródło: Skills_Abnormality-a1c6p2.json :: dataList[id=815903].levelList[level=1].name
   limit: do 40 znaków
   EN: Slothful Press
   PL: Slothful Press
