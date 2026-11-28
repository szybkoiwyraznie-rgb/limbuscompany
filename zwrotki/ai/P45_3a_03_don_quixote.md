# Paczka AI P45 (Fala 3 · 3A) — Grzesznik 03 — Don Quixote

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P45_3a_03_don_quixote.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P45_3a_03_don_quixote.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Grzesznik #03: Don Quixote (돈키호테)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 돈키호테
   źródło: Characters.json :: dataList[id=3].name
   limit: do 40 znaków
   EN: Don Quixote
   PL: Don Quixote
2. [Akta więźnia — nazwa] 돈키호테
   źródło: IntroduceCharacter.json :: dataList[id=돈키호테].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [0] LCB Sinner — Don Quixote — LCB 수감자
- ID Tożsamości: `10301` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 66 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed

3. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10301].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL: LCB\nGrzesznik
4. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10301].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
5. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10301].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — opis] 돈키호테의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10301].desc
   limit: do 120 znaków
   EN: Don Quixote’s 1st Identity
   PL: Pierwsza Tożsamość Don Quixote
7. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 찌르기
   źródło: Skills.json :: dataList[id=1030101].levelList[level=1].name ; dataList[id=1030101].levelList[level=2].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Joust
   PL: Pchnięcie
8. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WinDuel] 다음 턴에 신속 1 얻음
   źródło: Skills.json :: dataList[id=1030101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 1 Haste next turn
   PL: [WinDuel] Zyskuje w następnej turze 1 Pośpiechu
9. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WinDuel] 다음 턴에 신속 2 얻음
   źródło: Skills.json :: dataList[id=1030101].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 2 Haste next turn
   PL: [WinDuel] Zyskuje w następnej turze 2 Pośpiechu
10. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 모아 찌르기
   źródło: Skills.json :: dataList[id=1030102].levelList[level=1].name ; dataList[id=1030102].levelList[level=2].name ; dataList[id=1030102].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Galloping Tilt
   PL: Pchnięcie z Rozbiegu
11. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills.json :: dataList[id=1030102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 1 Attack Power Up next turn
   PL: [WinDuel] Zyskuje w następnej turze 1 Wzrost Mocy Ataku
12. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WinDuel] 다음 턴에 공격 위력 증가 2 얻음
   źródło: Skills.json :: dataList[id=1030102].levelList[level=2].desc ; dataList[id=1030102].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 2 Attack Power Up next turn
   PL: [WinDuel] Zyskuje w następnej turze 2 Wzrosty Mocy Ataku
13. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1030102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed
   PL: [OnSucceedAttackHead] Nakłada 2 Krwawienia
14. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 정의를 위해!
   źródło: Skills.json :: dataList[id=1030103].levelList[level=3].name ; dataList[id=1030103].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 3 · monety: 3 (+3)
   limit: do 40 znaków
   EN: For Justice!
   PL: Dla Sprawiedliwości!
15. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] 속도가 10 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1030103].levelList[level=3].desc ; dataList[id=1030103].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 10+ Speed, Coin Power +2
   PL: Przy 10+ Szybkości Moc Monet +2
16. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1030103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL: [OnSucceedAttackHead] Nakłada 1 Krwawienia
17. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1030103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 2 부여
   źródło: Skills.json :: dataList[id=1030103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Bleed count
   PL: [OnSucceedAttack] Nakłada +2 Licznika Krwawienia
19. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1030104].levelList[level=1].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 2 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL: Unik
20. [Pasywka bojowa (od ulepszenia 1, rezonans 3× Lust) — nazwa] 정의의 응징
   źródło: Passives.json :: dataList[id=1030101].name
   limit: do 40 znaków
   EN: Righteous Retribution
   PL: Sprawiedliwy Odwet
21. [Pasywka bojowa (od ulepszenia 1, rezonans 3× Lust) — opis] 합 승리 시 해당 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1030101].desc
   limit: do 120 znaków
   EN: Skills deal +10% damage in a won clash.
   PL: Po wygranym Starciu zadaje +10% obrażeń tą Umiejętnością
22. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — nazwa] 응원
   źródło: Passives.json :: dataList[id=1030121].name
   limit: do 40 znaków
   EN: Support
   PL: Wsparcie
23. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — opis] 정신력이 가장 높은 아군 1명 관통 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1030121].desc
   limit: do 120 znaków
   EN: 1 ally with the most SP deals +10% Pierce damage.
   PL: 1 Sojusznik z najwyższą Poczytalnością: Umiejętności Kłucia zadają +10% obrażeń

## [000] W Corp. L3 Cleanup Agent — Don Quixote — W사 3등급 정리 요원
- ID Tożsamości: `10302` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 73 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Charge, Rupture

24. [Karta Tożsamości — tytuł] W사 3등급\n정리 요원
   źródło: Personalities.json :: dataList[id=10302].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L3\nCleanup Agent
   PL: W Corp. L3\nAgentka Oczyszczania
25. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10302].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
26. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10302].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
27. [Karta Tożsamości — opis] 돈키호테의 두번째 인격
   źródło: Personalities.json :: dataList[id=10302].desc
   limit: do 120 znaków
   EN: Don Quixote’s 2nd Identity
   PL: Druga Tożsamość Don Quixote
28. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 절단
   źródło: Skills.json :: dataList[id=1030201].levelList[level=1].name ; dataList[id=1030201].levelList[level=2].name ; dataList[id=1030201].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Rip
   PL: Przecięcie
29. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1030201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Rupture
   PL: [OnSucceedAttackHead] Nakłada 1 Rozdarcia
30. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1030201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Rupture
   PL: [OnSucceedAttack] Nakłada 1 Rozdarcia
31. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1030201].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +2 Charge Count
   PL: [OnSucceedAttackHead] Zyskuje +2 Licznika Ładowania
32. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 충전 횟수가 5 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1030201].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 5+ Charge Count, Coin Power +2
   PL: Przy 5+ Licznikach Ładowania Moc Monet +2
33. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 4 증가
   źródło: Skills.json :: dataList[id=1030201].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +4 Charge Count
   PL: [OnSucceedAttackHead] Zyskuje +4 Licznika Ładowania
34. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 도약
   źródło: Skills.json :: dataList[id=1030202].levelList[level=1].name ; dataList[id=1030202].levelList[level=2].name ; dataList[id=1030202].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Leap
   PL: Skok
35. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 취약 1 부여
   źródło: Skills.json :: dataList[id=1030202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Fragile
   PL: [OnSucceedAttackHead] Nakłada 1 Wrażliwości
36. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 4 증가
   źródło: Skills.json :: dataList[id=1030202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +4 Charge Count
   PL: [OnSucceedAttack] Zyskuje +4 Licznika Ładowania
37. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 4 증가
   źródło: Skills.json :: dataList[id=1030202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1030202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 취약 2 부여
   źródło: Skills.json :: dataList[id=1030202].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1030202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Fragile
   PL: [OnSucceedAttackHead] Nakłada 2 Wrażliwości
39. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 충전 횟수가 7 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1030202].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 7+ Charge Count, Coin Power +1
   PL: Przy 7+ Licznikach Ładowania Moc Monet +1
40. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 공간 절단
   źródło: Skills.json :: dataList[id=1030203].levelList[level=3].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 1 · monety: 5 (+2)
   limit: do 40 znaków
   EN: Rip Space
   PL: Rozcięcie Przestrzeni
41. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 충전 횟수 10을 소모하여 코인 위력 +4\n충전 횟수가 10미만인 경우 체력 20% 감소
   źródło: Skills.json :: dataList[id=1030203].levelList[level=3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Spend 10 Charge Count to gain +4 Coin Power\nAt less than 10 Charge Count, lose 20% HP
   PL: [WhenUse] Zużywa 10 Licznika Ładowania, aby zyskać Moc Monet +4\nJeżeli Licznik Ładowania jest poniżej 10, traci 20% HP
42. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 5, efekt 1 — opis] [OnSucceedAttackHead] 파열 5 부여
   źródło: Skills.json :: dataList[id=1030203].levelList[level=3].coinlist[#4].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 5 Rupture
   PL: [OnSucceedAttackHead] Nakłada 5 Rozdarcia
43. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1030204].levelList[level=1].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — nazwa] 급속충전
   źródło: Passives.json :: dataList[id=1030201].name
   limit: do 40 znaków
   EN: Quick Recharge
   PL: Szybkie Ładowanie
45. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — opis] 전투 시작 시 이번 턴에 충전 횟수 (우울 공명 수/3)만큼 증가
   źródło: Passives.json :: dataList[id=1030201].desc
   limit: do 120 znaków
   EN: At the start of the combat phase, gain Charge Count by (Gloom Reson. / 3).
   PL: Na początku walki zwiększa w tej turze Licznik Ładowania o (Rezonans Posępności / 3)
46. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — nazwa] 꺾인 마음
   źródło: Passives.json :: dataList[id=1030221].name
   limit: do 40 znaków
   EN: Broken Spirit
   PL: Załamany Duch
47. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — opis] 속도가 가장 높은 아군 1명 첫번째 스킬의 최종 위력 +1
   źródło: Passives.json :: dataList[id=1030221].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed gains +1 final Power for their first skill.
   PL: 1 Sojusznik z najwyższą Szybkością: Moc Końcowa pierwszej Umiejętności +1

## [00] Shi Assoc. South Section 5 Director — Don Quixote — 남부 시 협회 5과 부장
- ID Tożsamości: `10303` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 69 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Poise

48. [Karta Tożsamości — tytuł] 남부 시 협회\n5과 부장
   źródło: Personalities.json :: dataList[id=10303].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Shi Assoc.\nSouth Section 5 Director
   PL: Południowe Stowarzyszenie Shi\nDyrektorka Sekcji 5
49. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10303].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
50. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10303].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Karta Tożsamości — opis] 돈키호테의 세번째 인격
   źródło: Personalities.json :: dataList[id=10303].desc
   limit: do 120 znaków
   EN: Don Quixote’s 3rd Identity
   PL: Trzecia Tożsamość Don Quixote
52. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 숨고르기
   źródło: Skills.json :: dataList[id=1030301].levelList[level=1].name ; dataList[id=1030301].levelList[level=2].name ; dataList[id=1030301].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Catch Breath
   PL: Wyrównanie Oddechu
53. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1030301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath] next turn
   PL: [OnSucceedAttackHead] Zyskuje w następnej turze 2 Oddechu
54. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1030301].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath] next turn
   PL: [OnSucceedAttack] Zyskuje w następnej turze 2 [Breath]
55. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 신속 2 얻음
   źródło: Skills.json :: dataList[id=1030301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Haste next turn
   PL: [WhenUse] Zyskuje w następnej turze 2 Pośpiechu
56. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 3 얻음
   źródło: Skills.json :: dataList[id=1030301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath] next turn
   PL: [OnSucceedAttack] Zyskuje w następnej turze 3 Oddechu
57. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 이격
   źródło: Skills.json :: dataList[id=1030302].levelList[level=1].name ; dataList[id=1030302].levelList[level=2].name ; dataList[id=1030302].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Dual Strike
   PL: Rozdzielenie
58. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath] next turn
   PL: [OnSucceedAttackHead] Zyskuje w następnej turze 1 Oddechu
59. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 신속 2 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1030302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 Haste next turn
   PL: [OnSucceedAttack] Zyskuje w następnej turze 2 Pośpiechu
60. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 체력이 최대 체력의 50%미만일 때 다음 턴에 신속 2 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At less than 50% HP, gain 2 Haste next turn
   PL: [WhenUse] Jeżeli HP jest poniżej 50% Maks. HP, zyskuje w następnej turze 2 Pośpiechu
61. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath] next turn
   PL: [OnSucceedAttack] Zyskuje 1 Oddech w następnej turze
62. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 체력이 최대 체력의 50%미만일 때 다음 턴에 신속 4 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At less than 50% HP, gain 4 Haste next turn
   PL: [WhenUse] Jeżeli HP jest poniżej 50% Maks. HP, zyskuje w następnej turze 4 Pośpiechu
63. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 신속 3 얻음
   źródło: Skills.json :: dataList[id=1030302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 3 Haste next turn
   PL: [OnSucceedAttack] Zyskuje w następnej turze 3 Pośpiechu
65. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 과호흡
   źródło: Skills.json :: dataList[id=1030303].levelList[level=3].name ; dataList[id=1030303].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 1 (+21)
   limit: do 40 znaków
   EN: Overbreathe
   PL: Hiperwentylacja
66. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 속도가 10 이상이면, 스킬 위력 +3
   źródło: Skills.json :: dataList[id=1030303].levelList[level=3].desc
   limit: do 120 znaków
   EN: At 10+ Speed, Skill Power +3
   PL: Przy 10+ Szybkości Moc Umiejętności +3
67. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 속도가 10 이상이면, 스킬 위력 +5
   źródło: Skills.json :: dataList[id=1030303].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 10+ Speed, Skill Power +5
   PL: Przy 10+ Szybkości Moc Umiejętności +5
68. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1030304].levelList[level=1].name
   kontekst: grzech: Wrath · typ: obrona: unik · moc bazowa: 3 · monety: 1 (+10)
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — nazwa] 마음가짐
   źródło: Passives.json :: dataList[id=1030301].name
   limit: do 40 znaków
   EN: Prepared Mind
   PL: Postawa
70. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — opis] 다음 턴에 [Agility]을 (분노 공명 수/3)만큼 얻음
   źródło: Passives.json :: dataList[id=1030301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Gain [Agility] by (Wrath Reson. / 3) next turn.
   PL: Zyskuje w następnej turze [Agility] w liczbie (Rezonans Gniewu / 3)
71. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — nazwa] 양단
   źródło: Passives.json :: dataList[id=1030321].name
   limit: do 40 znaków
   EN: Divide in Two
   PL: Rozłupanie na Pół
72. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — opis] 속도가 가장 높은 아군 1명 참격 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1030321].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed deals +10% Slash damage.
   PL: 1 Sojusznik z najwyższą Szybkością: Umiejętności Cięcia zadają +10% obrażeń

## [00] N Corp. Mittelhammer — Don Quixote — N사 중간 망치
- ID Tożsamości: `10304` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 1 · HP bazowe: 82 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Tremor, Bleed

73. [Karta Tożsamości — tytuł] N사\n중간 망치
   źródło: Personalities.json :: dataList[id=10304].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: N Corp.\nMittelhammer
   PL: Korporacja N\nMittelhammer
74. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10304].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10304].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Karta Tożsamości — opis] 돈키호테의 네번째 인격
   źródło: Personalities.json :: dataList[id=10304].desc
   limit: do 120 znaków
   EN: Don Quixote’s 4th Identity
   PL: Czwarta Tożsamość Don Quixote
77. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 올곧은 정화
   źródło: Skills.json :: dataList[id=1030401].levelList[level=1].name ; dataList[id=1030401].levelList[level=2].name ; dataList[id=1030401].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Rightful Purge
   PL: Słuszne Oczyszczenie
78. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 못 1 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1030401].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Nails
   PL: [OnSucceedAttackHead] Nakłada 1 Gwoździa
79. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 1 [Vibration]
   PL: [OnSucceedAttackHead] Nakłada 1 [Vibration]
80. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1030401].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]
82. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 못 2 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Nails
   PL: [OnSucceedAttackHead] Nakłada 2 Gwoździ
84. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills.json :: dataList[id=1030401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
85. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 집행!
   źródło: Skills.json :: dataList[id=1030402].levelList[level=1].name ; dataList[id=1030402].levelList[level=2].name ; dataList[id=1030402].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 4 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Enactment!
   PL: Wykonanie!
86. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills.json :: dataList[id=1030402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1030402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL: [OnSucceedAttack] Wybuch Wstrząsu
87. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] 대상에게 못 이 5 이상 있으면, 피해량 +20%
   źródło: Skills.json :: dataList[id=1030402].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: +20% Damage to targets that have 5+ Nails
   PL: Jeżeli cel ma 5+ Gwoździ, zadaje +20% obrażeń
88. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] 대상에게 못 이 5 이상 있으면, 피해량 +30%
   źródło: Skills.json :: dataList[id=1030402].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: +30% damage to targets that have 5+ Nails
   PL: Jeżeli cel ma 5+ Gwoździ, zadaje +30% obrażeń
89. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 광적인 심판
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].name ; dataList[id=1030403].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Fanatical Judgement
   PL: Fanatyczny Wyrok
90. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 못 1 부여
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Nails
   PL: [OnSucceedAttack] Nakłada 1 Gwoździa
91. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 못 1 부여
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1030403].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]
93. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 대상에게 못 이 5 이상 있으면, 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1030403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] If target has 5+ Nails, inflict 1 Attack Power Down next turn
   PL: [OnSucceedAttackHead] Jeżeli cel ma 5+ Gwoździ, nakłada w następnej turze 1 Spadku Mocy Ataku
94. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 대상에게 못 이 5 이상 있으면, 다음 턴에 마비 2 부여
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1030403].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] If target has 5+ Nails, inflict 2 Paralyze next turn
   PL: [OnSucceedAttackHead] Jeżeli cel ma 5+ Gwoździ, nakłada w następnej turze 2 Paraliżu
95. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1030403].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1030403].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 못 2 부여
   źródło: Skills.json :: dataList[id=1030403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Nails
   PL: [OnSucceedAttack] Nakłada 2 Gwoździ
97. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 못 2 부여
   źródło: Skills.json :: dataList[id=1030403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1030404].levelList[level=1].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Guard
   PL: Garda
99. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust) — nazwa] 두드릴지라!
   źródło: Passives.json :: dataList[id=1030401].name
   limit: do 40 znaków
   EN: Thou Shalt Hammer!
   PL: Bijcie Młotem!
100. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust) — opis] 못 이 있는 대상에게 부여하는 진동 횟수 +1\n자신에게 광신 이 있으면 부여하는 못 +1
   źródło: Passives.json :: dataList[id=1030401].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If the target has Nails, inflict +1 Tremor Count.\nIf this unit is Fanatic, inflict +1 Nails.
   PL: Nakłada o 1 więcej Licznika Wstrząsu na cele z Gwoździami\nJeżeli ta jednostka ma Fanatyzm, nakłada o 1 więcej Gwoździ
101. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 맹목의 망치
   źródło: Passives.json :: dataList[id=1030421].name
   limit: do 40 znaków
   EN: Hammer of Zealotry
   PL: Młot Ślepej Wiary
102. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 광신 이 있는 아군 중 정신력이 가장 낮은 아군의 피해량 +10%
   źródło: Passives.json :: dataList[id=1030421].desc
   limit: do 120 znaków
   EN: 1 Fanatic ally that has the least SP deals +10% damage
   PL: Sojusznik z najniższą Poczytalnością wśród posiadających Fanatyzm zadaje +10% obrażeń

## [000] Cinq Assoc. South Section 5 Director — Don Quixote — 남부 섕크 협회 5과 부장
- ID Tożsamości: `10305` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 72 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: —

103. [Karta Tożsamości — tytuł] 남부 섕크 협회\n5과 부장
   źródło: Personalities.json :: dataList[id=10305].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cinq Assoc.\nSouth Section 5 Director
   PL: Południowe Stowarzyszenie Cinq\nDyrektorka Sekcji 5
104. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10305].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10305].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Karta Tożsamości — opis] 돈키호테의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10305].desc
   limit: do 120 znaków
   EN: Don Quixote’s 5th Identity
   PL: Piąta Tożsamość Don Quixote
107. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 르미즈
   źródło: Skills.json :: dataList[id=1030501].levelList[level=1].name ; dataList[id=1030501].levelList[level=2].name ; dataList[id=1030501].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Remise
   PL: Remise
108. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 자신의 속도가 7 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1030501].levelList[level=1].desc
   limit: do 120 znaków
   EN: At 7+ Speed, Coin Power +1
   PL: Przy 7+ Szybkości Moc Monet +1
109. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [WinDuelAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills.json :: dataList[id=1030501].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1030501].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttackHead]
   znaczenie tagów: [WinDuelAttackHead] = [합 승리 후 앞면 적중시] / [Heads Hit after Clash Win]
   EN: [WinDuelAttackHead] Inflict 1 Bind next turn
   PL: [WinDuelAttackHead] Nakłada w następnej turze 1 Spętania
110. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 자신의 속도가 7 이상이면, 코인 위력 +1\n[WinDuel] 다음 턴에 신속 1을 얻음
   źródło: Skills.json :: dataList[id=1030501].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: At 7+ Speed, Coin Power +1\n[WinDuel] Gain 1 Haste next turn
   PL: Przy 7+ Szybkości Moc Monet +1\n[WinDuel] Zyskuje w następnej turze 1 Pośpiechu
111. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 속도가 7 이상이면, 코인 위력 +2\n[WinDuel] 다음 턴에 신속 1을 얻음
   źródło: Skills.json :: dataList[id=1030501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: At 7+ Speed, Coin Power +2\n[WinDuel] Gain 1 Haste next turn
   PL: Przy 7+ Szybkości Moc Monet +2\n[WinDuel] Zyskuje w następnej turze 1 Pośpiechu
112. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [WinDuelAttack] 다음 턴에 속박 1 부여
   źródło: Skills.json :: dataList[id=1030501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]
   EN: [WinDuelAttack] Inflict 1 Bind next turn
   PL: [WinDuelAttack] Nakłada w następnej turze 1 Spętania
113. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 플레쉬
   źródło: Skills.json :: dataList[id=1030502].levelList[level=1].name ; dataList[id=1030502].levelList[level=2].name ; dataList[id=1030502].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Flèche
   PL: Flèche
114. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 신속 1을 얻음
   źródło: Skills.json :: dataList[id=1030502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Haste next turn
   PL: [WhenUse] Zyskuje w następnej turze 1 Pośpiechu
115. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 1 부여
   źródło: Skills.json :: dataList[id=1030502].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1030502].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bind next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze 1 Spętania
116. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 신속 2를 얻음
   źródło: Skills.json :: dataList[id=1030502].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Haste next turn
   PL: [WhenUse] Zyskuje w następnej turze 2 Pośpiechu
117. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 신속 2를 얻음\n[WinDuel] 합 횟수에 비례하여 피해량 증가(합 횟수 1 당 +5%. 최대 50%)
   źródło: Skills.json :: dataList[id=1030502].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain 2 Haste next turn\n[WinDuel] Deal more damage based on Clash count (+5% per Clash count, Max 50%)
   PL: [WhenUse] Zyskuje w następnej turze 2 Pośpiechu\n[WinDuel] Zadaje więcej obrażeń zależnie od liczby Starć (+5% za każde 1 Starcie; maks. 50%)
118. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills.json :: dataList[id=1030502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bind next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Spętania
119. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 살뤼!
   źródło: Skills.json :: dataList[id=1030503].levelList[level=3].name ; dataList[id=1030503].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 6 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Salut!
   PL: Salut!
120. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 10 이상이면, 코인 위력 +2\n[WinDuel] 합 횟수에 비례하여 피해량 증가(합 횟수 1 당 +5%. 최대 50%)
   źródło: Skills.json :: dataList[id=1030503].levelList[level=3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: At 10+ Speed, Coin Power +2\n[WinDuel] Deal more damage based on Clash count (+5% per Clash count, Max 50%)
   PL: Przy 10+ Szybkości Moc Monet +2\n[WinDuel] Zadaje więcej obrażeń zależnie od liczby Starć (+5% za każde 1 Starcie; maks. 50%)
121. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [DuelDeclaration_DonQuixote] 부여
   źródło: Skills.json :: dataList[id=1030503].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1030503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DuelDeclaration_DonQuixote]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DuelDeclaration_DonQuixote] = 결투 선포 - 돈키호테 / Declared Duel - Don Quixote
   EN: [OnSucceedAttack] Inflict [DuelDeclaration_DonQuixote]
   PL: [OnSucceedAttack] Nakłada [DuelDeclaration_DonQuixote]
122. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 속도가 10 이상이면, 코인 위력 +3\n[WinDuel] 합 횟수에 비례하여 피해량 증가(합 횟수 1 당 +10%. 최대 100%)
   źródło: Skills.json :: dataList[id=1030503].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: At 10+ Speed, Coin Power +3\n[WinDuel] Deal more damage based on Clash count (+10% per Clash count, Max 100%)
   PL: Przy 10+ Szybkości Moc Monet +3\n[WinDuel] Zadaje więcej obrażeń zależnie od liczby Starć (+10% za każde 1 Starcie; maks. 100%)
123. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [EnemyKill] 자신의 정신력 15 회복
   źródło: Skills.json :: dataList[id=1030503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Heal 15 SP
   PL: [EnemyKill] Odzyskuje 15 Poczytalności
124. [Obrona (ulepszenia 1,4) — nazwa] 데팡시브
   źródło: Skills.json :: dataList[id=1030504].levelList[level=1].name ; dataList[id=1030504].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Défensive
   PL: Défensive
125. [Obrona (ulepszenia 1,4) — opis] [OnSucceedEvade] 대상의 정신력 3 감소
   źródło: Skills.json :: dataList[id=1030504].levelList[level=1].desc ; dataList[id=1030504].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Target loses 3 SP
   PL: [OnSucceedEvade] Cel traci 3 Poczytalności
126. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — nazwa] 고귀한 결투
   źródło: Passives.json :: dataList[id=1030501].name
   limit: do 40 znaków
   EN: A Noble Duel
   PL: Szlachetny Pojedynek
127. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — opis] 모든 아군의 속도가 모든 적보다 높으면, 자신의 피해량이 속도가 가장 느린 적과의 속도 차이에 비례하여 증가 (속도 차이 1 당 6%. 최대 30%)
   źródło: Passives.json :: dataList[id=1030501].desc
   limit: do 280 znaków
   EN: If the Speed of all allies is faster than the Speed of all enemies, this unit deals more damage based on the Speed difference between itself and the slowest enemy (+6% for every point of Speed difference; max 30%)
   PL: Jeżeli Szybkość wszystkich sojuszników przewyższa Szybkość wszystkich wrogów, ta jednostka zadaje obrażenia proporcjonalnie do różnicy Szybkości względem najwolniejszego wroga (+6% za każde 1 różnicy Szybkości; maks. 30%)
128. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — nazwa] 결투 의뢰
   źródło: Passives.json :: dataList[id=1030521].name
   limit: do 40 znaków
   EN: Dueling Request
   PL: Wyzwanie na Pojedynek
129. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — opis] 모든 아군의 속도가 모든 적보다 높으면, 속도가 가장 빠른 아군의 피해량이 속도가 가장 느린 적과의 속도 차이에 비례하여 증가 (속도 차이 1 당 3%. 최대 15%)
   źródło: Passives.json :: dataList[id=1030521].desc
   limit: do 280 znaków
   EN: If the Speed of all allies is faster than the Speed of all enemies, the fastest ally deals more damage based on the Speed difference between itself and the slowest enemy (+3% for every point of Speed difference; max 15%)
   PL: Jeżeli Szybkość wszystkich sojuszników przewyższa Szybkość wszystkich wrogów, najszybszy sojusznik zadaje obrażenia proporcjonalnie do różnicy Szybkości względem najwolniejszego wroga (+3% za każde 1 różnicy Szybkości; maks. 15%)

## [000] The Middle Little Sister — Don Quixote — 중지 작은 아우
- ID Tożsamości: `10306` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 3 · HP bazowe: 86 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Bleed

130. [Karta Tożsamości — tytuł] 중지\n작은 아우
   źródło: Personalities.json :: dataList[id=10306].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Middle\nLittle Sister
   PL: Środkowego\nMłodsza Siostra
131. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10306].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10306].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Karta Tożsamości — opis] 돈키호테의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10306].desc
   limit: do 120 znaków
   EN: Don Quixote’s 6th Identity
   PL: Szósta Tożsamość Don Quixote
134. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 장부 확인
   źródło: Skills_personality-03.json :: dataList[id=1030601].levelList[level=1].name ; dataList[id=1030601].levelList[level=2].name ; dataList[id=1030601].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Checking the Book
   PL: Przegląd Księgi
135. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] [WhenUse] 자신의 정신력 5 회복
   źródło: Skills_personality-03.json :: dataList[id=1030601].levelList[level=2].desc ; dataList[id=1030601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 5 SP on self
   PL: [WhenUse] Odzyskuje 5 Poczytalności
138. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL: [OnSucceedAttack] Nakłada 1 Krwawienia
139. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1030601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1030601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL: [OnSucceedAttack] Nakłada 2 Krwawienia
140. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 의리 증명
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=1].name ; dataList[id=1030602].levelList[level=2].name ; dataList[id=1030602].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Proof of Loyalty
   PL: Dowód Lojalności
141. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [StartBattle] (가장 높은 완전 공명 수/3)만큼 이 스킬의 공격 레벨이 1 증가 (최대 4)
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] This Skill gains 1 Offense Level by (highest A-Reson./3) (Max 4)
   PL: [StartBattle] Ta Umiejętność zyskuje +1 Poziomu Ataku za każde (najwyższy Pełny Rezonans / 3) (maks. 4)
142. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1030602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1030602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL: [OnSucceedAttack] Nakłada 3 Krwawienia
143. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 피해량 감소 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1030602].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Damage Down
   PL: [OnSucceedAttackHead] Nakłada 1 Spadku Obrażeń
144. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [StartBattle] (가장 높은 완전 공명 수/3)만큼 이 스킬의 공격 레벨이 1 증가 (최대 4)\n해당 공명이 질투 완전 공명이면, 위 효과로 증가한 값의 50%만큼 공격 레벨이 추가 증가 (소수점 버림)
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=2].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] This Skill gains 1 Offense Level by (highest A-Reson./3) (Max 4)\nIf the highest A-Reson is Envy A-Reson, Gain 50% additional Offense Level to the Offense Level gained by the above effect (rounded down)
   PL: [StartBattle] Ta Umiejętność zyskuje +1 Poziomu Ataku za każde (najwyższy Pełny Rezonans / 3) (maks. 4)\nJeżeli tym Rezonansem jest Pełny Rezonans Zazdrości, zwiększa o 50% wartość Poziomu Ataku uzyskanego powyższym efektem (zaokrąglone w dół)
145. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [StartBattle] (가장 높은 완전 공명 수/2)만큼 이 스킬의 공격 레벨이 1 증가 (최대 6)\n해당 공명이 질투 완전 공명이면, 위 효과로 증가한 값의 50%만큼 공격 레벨이 추가 증가 (소수점 버림)\n전투 참가 가능 수가 7인 이하인 집중 전투에서는 증가하는 공격 레벨이 2배로 적용됨.
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] This Skill gains 1 Offense Level by (highest A-Reson./2) (Max 6)\nIf the highest A-Reson is Envy A-Reson., boost the Offense Level gained by the above effect by 50% (rounded down)\nGain double the Offense Level from the above effects in Focused Encounters with 7 or fewer Participant Limits.
   PL: [StartBattle] Ta Umiejętność zyskuje +1 Poziomu Ataku za każde (najwyższy Pełny Rezonans / 2) (maks. 6)\nJeżeli tym Rezonansem jest Pełny Rezonans Zazdrości, zwiększa o 50% wartość Poziomu Ataku uzyskanego powyższym efektem (zaokrąglone w dół)\nW walkach skupionych z liczbą uczestników 7 lub mniejszą zyskany Poziom Ataku podwaja się.
146. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량 감소 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030602].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Damage Down
   PL: [OnSucceedAttack] Nakłada 1 Spadku Obrażeń
147. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 정의로운 앙갚음
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=3].name ; dataList[id=1030603].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: A Just Vengeance
   PL: Sprawiedliwa Zemsta
148. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] (가장 높은 완전 공명 수/3)만큼 이 스킬의 공격 레벨이 1 증가 (최대 4)\n해당 공명이 질투 완전 공명이면, 위 효과로 증가한 값의 50%만큼 공격 레벨이 추가 증가 (소수점 버림)
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=3].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] This Skill gains 1 Offense Level by (highest A-Reson./3) (Max 4)\nIf the highest A-Reson is Envy A-Reson, Gain 50% additional 'Offense Level' to the 'Offense Level' gained by the above effect (rounded down)
   PL: [StartBattle] Ta Umiejętność zyskuje +1 Poziomu Ataku za każde (najwyższy Pełny Rezonans / 3) (maks. 4)\nJeżeli tym Rezonansem jest Pełny Rezonans Zazdrości, zwiększa o 50% wartość Poziomu Ataku uzyskanego powyższym efektem (zaokrąglone w dół)
149. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1030603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1030603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1030603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [EndSkill] 대상이 사망하면 정신력이 가장 낮은 아군 1명의 정신력 6 회복
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1030603].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] If target is defeated, 1 ally with the least SP heals 6 SP
   PL: [EndSkill] Jeżeli cel ginie, 1 Sojusznik z najniższą Poczytalnością odzyskuje 6 Poczytalności
153. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [StartBattle] (가장 높은 완전 공명 수/2)만큼 이 스킬의 공격 레벨이 1 증가 (최대 6)\n해당 공명이 질투 완전 공명이면, 위 효과로 증가한 값의 50%만큼 공격 레벨이 추가 증가 (소수점 버림)\n전투 참가 가능 수가 7인 이하인 집중 전투에서는 증가하는 공격 레벨이 2배로 적용됨.
   źródło: Skills_personality-03.json :: dataList[id=1030603].levelList[level=4].desc
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Obrona (ulepszenia 1,4) — nazwa] 배로 갚기
   źródło: Skills_personality-03.json :: dataList[id=1030604].levelList[level=1].name ; dataList[id=1030604].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Multifold Retribution
   PL: Wielokrotna Zemsta
155. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 3 회복
   źródło: Skills_personality-03.json :: dataList[id=1030604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 3
   PL: [OnSucceedAttack] Odzyskuje 3 Ogłuszenia
156. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 3 회복
   źródło: Skills_personality-03.json :: dataList[id=1030604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Obrona (ulepszenie 4) — opis] [StartBattle] 질투 완전 공명 수의 합이 6 이상이면, 반격 시 '정의로운 앙갚음' 스킬을 사용함.\n변경 시 해당 스킬의 속성이 질투로 변경됨.\n(조작 패널의 왼쪽 슬롯 스킬부터 발동. 턴 당 최대 2회 발동)
   źródło: Skills_personality-03.json :: dataList[id=1030604].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] At 6+ sum of Envy A-Reson., use 'A Just Vengeance' as Counter.\nUpon activating the above effect, the Skill's affinity is changed to Envy.\n(Leftmost 'Multifold Retribution' is activated first. Activates 2 times per turn)
   PL: [StartBattle] Jeżeli suma Pełnych Rezonansów Zazdrości wynosi 6 lub więcej, w Kontrze używa Umiejętności „Sprawiedliwa Zemsta”.\nPrzy uruchomieniu tego efektu atrybut tej Umiejętności zmienia się na Zazdrość.\n(Uruchamia od skrajnie lewej Umiejętności w Panelu Sterowania. Maks. 2 razy na turę)
158. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 5 회복
   źródło: Skills_personality-03.json :: dataList[id=1030604].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 5
   PL: [OnSucceedAttack] Odzyskuje 5 Ogłuszenia
159. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 5 회복
   źródło: Skills_personality-03.json :: dataList[id=1030604].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Obrona (ulepszenia 3–4) — nazwa] 정의로운 앙갚음
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=3].name ; dataList[id=1030605].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 4 · monety: 4 (+3)
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Obrona (ulepszenie 3) — opis] [StartBattle] (가장 높은 완전 공명 수/3)만큼 이 스킬의 공격 레벨이 1 증가 (최대 4)\n해당 공명이 질투 완전 공명이면, 위 효과로 증가한 값의 50%만큼 공격 레벨이 추가 증가 (소수점 버림)
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=3].desc
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [Obrona (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1030605].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Obrona (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1030605].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Obrona (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1030605].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Obrona (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [EndSkill] 대상이 사망하면 정신력이 가장 낮은 아군 1명의 정신력 6 회복
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1030605].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Obrona (ulepszenie 4) — opis] [StartBattle] (가장 높은 완전 공명 수/2)만큼 이 스킬의 공격 레벨이 1 증가 (최대 6)\n해당 공명이 질투 완전 공명이면, 위 효과로 증가한 값의 50%만큼 공격 레벨이 추가 증가 (소수점 버림)\n전투 참가 가능 수가 6인 이하인 전투에서는 증가하는 공격 레벨이 2배로 적용됨.
   źródło: Skills_personality-03.json :: dataList[id=1030605].levelList[level=4].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] This Skill gains 1 Offense Level by (highest A-Reson./2) (Max 6)\nIf the highest A-Reson is Envy A-Reson, Gain 50% additional Offense Level to the Offense Level gained by the above effect (rounded down)\nGain double the Offense Level from above effects in encounters with 6 or fewer Participant Limits.
   PL: [StartBattle] Ta Umiejętność zyskuje +1 Poziomu Ataku za każde (najwyższy Pełny Rezonans / 2) (maks. 6)\nJeżeli tym Rezonansem jest Pełny Rezonans Zazdrości, zwiększa o 50% wartość Poziomu Ataku uzyskanego powyższym efektem (zaokrąglone w dół)\nW walkach z liczbą uczestników 6 lub mniejszą zyskany Poziom Ataku podwaja się.
167. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Envy) — nazwa] 원한 문신
   źródło: Passives.json :: dataList[id=1030601].name
   limit: do 40 znaków
   EN: Vengeance Tattoo
   PL: Tatuaż Zemsty
168. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Envy) — opis] - 자신을 포함한 아군이 3번 피격당할 때마다 다음 턴에 질투 피해량 증가 1을 얻음. (최대 5)\n- 턴 종료 시 해당 턴에 아군에게 스킬로 가장 많이 피해를 준 적 1명에게 <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">앙갚음 대상</color></link></u>을 부여.\n- 공격 시 메인 공격 대상이 앙갚음 대상 인 경우 최종 위력 1 증가
   źródło: Passives.json :: dataList[id=1030601].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <sprite name="RetaliationBook">, <color=#e30000>, <u>, <link="RetaliationBook">, </color>, </link>, </u>, \n
   EN: - Gain 1 Envy DMG Up next turn every time the enemies strike an ally(including this unit) 3 times. (Max 5)\n- Apply <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">Vengeance Mark</color></link></u> to the unit that dealt the most Skill damage to an ally.\n- If the main target has Vengeance Mark, Final Power +1
   PL: - Za każde 3 trafienia sojuszników (łącznie z tą jednostką), zyskuje w następnej turze 1 Wzrost Obrażeń Zazdrości. (maks. 5)\n- Na koniec tury nakłada <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">Cel Odwetu</link></u></color> na wroga, który w tej turze zadał sojusznikom najwięcej obrażeń Umiejętnościami.\n- Gdy głównym celem ataku jest Cel Odwetu, Moc Końcowa +1
169. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Envy) — nazwa] 원한 문신
   źródło: Passives.json :: dataList[id=1030611].name
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Envy) — opis] - 자신을 포함한 아군이 3번 피격당할 때마다 다음 턴에 질투 피해량 증가 1을 얻음. (최대 5)\n- 턴 종료 시 해당 턴에 아군에게 스킬로 가장 많이 피해를 준 적 1명에게 <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">앙갚음 대상</color></link></u>을 부여.\n- 공격 시 메인 공격 대상이 앙갚음 대상 인 경우 코인 위력 1 증가
   źródło: Passives.json :: dataList[id=1030611].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <sprite name="RetaliationBook">, <color=#e30000>, <u>, <link="RetaliationBook">, </color>, </link>, </u>, \n
   EN: - Gain 1 Envy DMG Up next turn every time the enemies strike an ally(including this unit) 3 times. (Max 5)\n- Apply <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">Vengeance Mark</color></link></u> to the unit that dealt the most Skill damage to an ally.\n- If the main target has Vengeance Mark, Coin Power +1
   PL: - Za każde 3 trafienia sojuszników (łącznie z tą jednostką), zyskuje w następnej turze 1 Wzrost Obrażeń Zazdrości. (maks. 5)\n- Na koniec tury nakłada <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">Cel Odwetu</link></u></color> na wroga, który w tej turze zadał sojusznikom najwięcej obrażeń Umiejętnościami.\n- Gdy głównym celem ataku jest Cel Odwetu, Moc Monet +1
171. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — nazwa] 편 가르기
   źródło: Passives.json :: dataList[id=1030621].name
   limit: do 40 znaków
   EN: Favoritism
   PL: Faworyzowanie
172. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — opis] 최대 체력이 가장 낮은 아군 1명이 자신을 제외한 아군의 피격 횟수 6회마다 다음 턴에 타격 피해량 증가 1을 얻음. (최대 2)
   źródło: Passives.json :: dataList[id=1030621].desc
   limit: do 180 znaków
   EN: 1 ally with the lowest Max HP gains 1 Blunt DMG Up next turn every time the enemies strike an ally(not including this unit) 6 times. (Max 2)
   PL: 1 Sojusznik z najniższym Maks. HP zyskuje w następnej turze 1 Wzrost Obrażeń Uderzenia za każde 6 trafień sojuszników (nie licząc tej jednostki). (maks. 2)

## [00] Lobotomy E.G.O::Lantern — Don Quixote — 로보토미 E.G.O:: 초롱
- ID Tożsamości: `10307` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: wydarzenie 9102 · HP bazowe: 82 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Rupture

173. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n초롱
   źródło: Personalities.json :: dataList[id=10307].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::Lantern
   PL: Lobotomy E.G.O::\nLatarnia
174. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10307].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10307].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Karta Tożsamości — opis] 돈키호테의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10307].desc
   limit: do 120 znaków
   EN: Don Quixote’s 7th Identity
   PL: Siódma Tożsamość Don Quixote
177. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 씹어주겠네!
   źródło: Skills_personality-03.json :: dataList[id=1030701].levelList[level=1].name ; dataList[id=1030701].levelList[level=2].name ; dataList[id=1030701].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 1 (+7)
   limit: do 40 znaków
   EN: I Shall Nibble Thee!
   PL: Przekąsię Cię!
178. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict +2 [Burst] Count
   PL: [OnSucceedAttackHead] Nakłada +2 Licznika [Burst]
179. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 1을 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030701].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +1 [Aggro] to this Skill Slot next turn
   PL: [WhenUse] W następnej turze ten slot zyskuje 1 [Aggro]
180. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030701].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Burst]
181. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 3를 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn
   PL: [WhenUse] W następnej turze ten slot zyskuje 3 [Aggro]
182. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 발광 미끼
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=1].name ; dataList[id=1030702].levelList[level=2].name ; dataList[id=1030702].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Flashing Lure
   PL: Błyskająca Przynęta
183. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 1 [Burst]
   PL: [OnSucceedAttackHead] Nakłada 1 [Burst]
184. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 2 [Burst]
   PL: [OnSucceedAttackHead] Nakłada 2 [Burst]
186. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 2를 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +2 [Aggro] to this Skill Slot next turn
   PL: [WhenUse] W następnej turze ten slot zyskuje 2 [Aggro]
187. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL: [OnSucceedAttack] Nakłada 1 [Burst]
188. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1030702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1030702].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] Nakłada 2 [Burst]
190. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst] 횟수가 2 이하면, [Burst] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has 2 or less [Burst] Count, inflict +2 [Burst] Count
   PL: [OnSucceedAttack] Jeżeli Licznik [Burst] celu wynosi 2 lub mniej, zwiększa Licznik [Burst] celu o 2
191. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 4를 얻음\n[WhenUse] 대상의 [Burst]이 6 이상이면 코인 위력 +1
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture
   EN: [WhenUse] Gain +4 [Aggro] to this Skill Slot next turn\n[WhenUse] If target has 6+ [Burst], Coin Power +1
   PL: [WhenUse] W następnej turze ten slot zyskuje 4 [Aggro]\n[WhenUse] Jeżeli cel ma 6+ [Burst], Moc Monet +1
192. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst] 횟수가 2 이하면, [Burst] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1030702].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has 2 or less [Burst] Count, inflict +3 [Burst] Count
   PL: [OnSucceedAttack] Jeżeli Licznik [Burst] celu wynosi 2 lub mniej, zwiększa Licznik [Burst] celu o 3
193. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 빙글빙글 냠냠냠!
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=3].name ; dataList[id=1030703].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Whirlwind Om-Nom-Nom!
   PL: Om-Nom-Nom w Wirze!
194. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 3를 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=3].desc
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1030703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Burst]
196. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 체력 10 회복.
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 10 HP.
   PL: [OnSucceedAttack] Odzyskuje 10 HP.
197. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]만큼 체력 추가 회복 ([Burst] 1 당 체력 1 회복. 최대 20)
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Heal additional HP based on [Burst] on target (1 HP healed per 1 [Burst]. Max 20)
   PL: [OnSucceedAttack] Odzyskuje dodatkowo HP równe [Burst] celu (1 HP za każde 1 [Burst]; maks. 20)
198. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] 자신의 체력이 최대 체력의 50% 미만이면 코인 1회 재사용
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1030703].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   EN: At 50%- HP, reuse Coin once
   PL: Przy HP poniżej 50% Maks. HP używa tej monety ponownie (1 raz)
199. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 슬롯이 [Aggro] 5를 얻음\n[WhenUse] 대상의 [Burst]이 6 이상이면 코인 위력 +1
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Burst] = 파열 / Rupture
   EN: [WhenUse] Gain +5 [Aggro] to this Skill Slot next turn\n[WhenUse] If target has 6+ [Burst], Coin Power +1
   PL: [WhenUse] W następnej turze ten slot zyskuje 5 [Aggro]\n[WhenUse] Jeżeli cel ma 6+ [Burst], Moc Monet +1
200. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 체력 15 회복. 코인 재사용 시 체력 회복량 50% 증가.
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 15 HP. Heal by +50% more HP when reusing Coin.
   PL: [OnSucceedAttack] Odzyskuje 15 HP. Przy ponownym użyciu monety odzyskuje o 50% więcej HP.
201. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]만큼 체력 추가 회복 ([Burst] 1 당 체력 2 회복. 최대 40)
   źródło: Skills_personality-03.json :: dataList[id=1030703].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Heal additional HP based on [Burst] on target (2 HP healed per 1 [Burst]. Max 40)
   PL: [OnSucceedAttack] Odzyskuje dodatkowo HP równe 2 x [Burst] celu (2 HP za każde 1 [Burst]; maks. 40)
202. [Obrona (ulepszenia 1,4) — nazwa] 들썩이는 이빨
   źródło: Skills_personality-03.json :: dataList[id=1030704].levelList[level=1].name ; dataList[id=1030704].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Chattering Teeth
   PL: Szczękające Zęby
203. [Obrona (ulepszenie 1) — opis] [EndBattle] 남은 보호막 수치만큼 체력 회복 (턴 당 1회. 최대 회복량: 최대 체력의 10%)
   źródło: Skills_personality-03.json :: dataList[id=1030704].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [EndBattle]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [EndBattle] Heal HP equal to remaining Shield HP (Once per turn. Max Heal amount: 10% of Max HP)
   PL: [EndBattle] Odzyskuje HP równe pozostałej wartości Tarczy (1 raz na turę; maks. 10% Maks. HP)
204. [Obrona (ulepszenie 4) — opis] [WhenUse] 대상의 [Burst]이 6 이상이면 최종 위력 +3\n[EndBattle] 남은 보호막 수치만큼 체력 회복 (턴 당 1회. 최대 회복량: 최대 체력의 10%)
   źródło: Skills_personality-03.json :: dataList[id=1030704].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [WhenUse] If target has 6+ [Burst], Final Power +3\n[EndBattle] Heal HP equal to remaining Shield HP (Once per turn. Max Heal amount: 10% of Max HP)
   PL: [WhenUse] Jeżeli cel ma 6+ [Burst], Moc Końcowa +3\n[EndBattle] Odzyskuje HP równe pozostałej wartości Tarczy (1 raz na turę; maks. 10% Maks. HP)
205. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — nazwa] 잘근잘근 냠냠
   źródło: Passives.json :: dataList[id=1030701].name
   limit: do 40 znaków
   EN: Om Nom Nom
   PL: Om Nom Nom
206. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — opis] 자신의 스킬 슬롯에 [Aggro]가 있을 때 합 위력 +1\n명령 페이즈에서 자신을 공격 스킬의 타겟으로 삼은 적에게 공격을 적중할 때마다 체력 4 회복 (환상체인 경우 부위로 판정)
   źródło: Passives.json :: dataList[id=1030701].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Aggro]
   znaczenie tagów: [Aggro] = 도발치 / Aggro
   EN: If this unit's Skill Slot has [Aggro], Clash Power +1\nHeal 4 HP every time this unit hits enemies that targeted this unit with an Attack Skill in the Chaining Phase (For Abnormalities, the Parts that targeted this unit with an Attack Skill)
   PL: Gdy slot Umiejętności tej jednostki ma [Aggro], Moc Starcia +1\nOdzyskuje 4 HP za każde trafienie wroga, który w fazie rozkazów namierzył tę jednostkę Umiejętnością ataku (w przypadku Abnormalności: liczy się części ciała)
207. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 잘근잘근 냠냠
   źródło: Passives.json :: dataList[id=1030711].name
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — opis] 자신의 스킬 슬롯에 [Aggro]가 있을 때 합 위력 +1\n명령 페이즈에서 자신을 공격 스킬의 타겟으로 삼은 적에게 공격을 적중할 때마다 체력 6 회복 (환상체인 경우 부위로 판정)
   źródło: Passives.json :: dataList[id=1030711].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Aggro]
   znaczenie tagów: [Aggro] = 도발치 / Aggro
   EN: If this unit's Skill Slot has [Aggro], Clash Power +1\nHeal 6 HP every time this unit hits enemies that targeted this unit with an Attack Skill in the Chaining Phase (For Abnormalities, each Part is calculated separately)
   PL: Gdy slot Umiejętności tej jednostki ma [Aggro], Moc Starcia +1\nOdzyskuje 6 HP za każde trafienie wroga, który w fazie rozkazów namierzył tę jednostkę Umiejętnością ataku (w przypadku Abnormalności: liczy się części ciała)
209. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — nazwa] 초롱초롱
   źródło: Passives.json :: dataList[id=1030721].name
   limit: do 40 znaków
   EN: Illumilantern
   PL: Rozświetlona Latarnia
210. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — opis] [Aggro]가 가장 높은 슬롯을 보유한 아군 1명이 자신을 타겟으로 삼은 적에게 공격을 적중할 때마다 체력 2 회복 ([Aggro]가 없으면 적용되지 않음.)
   źródło: Passives.json :: dataList[id=1030721].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [Aggro]
   znaczenie tagów: [Aggro] = 도발치 / Aggro
   EN: The ally with the highest [Aggro] Skill Slot heals 2 HP every time they hit an enemy that targets this unit (Does not apply to units without [Aggro])
   PL: 1 Sojusznik ze slotem o najwyższym [Aggro] odzyskuje 2 HP za każde trafienie wroga namierzającego tę jednostkę (nie działa przy braku [Aggro].)
211. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Glut.) — nazwa] 초롱초롱
   źródło: Passives.json :: dataList[id=1030731].name
   (powtórzenie elementu 209 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Glut.) — opis] [Aggro]가 가장 높은 슬롯을 보유한 아군 1명이 자신을 타겟으로 삼은 적에게 공격을 적중할 때마다 체력 4 회복 ([Aggro]가 없으면 적용되지 않음.)
   źródło: Passives.json :: dataList[id=1030731].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [Aggro]
   znaczenie tagów: [Aggro] = 도발치 / Aggro
   EN: The ally with the highest [Aggro] Skill Slot heals 4 HP every time they hit an enemy that targets this unit (Does not apply to units without [Aggro])
   PL: 1 Sojusznik ze slotem o najwyższym [Aggro] odzyskuje 4 HP za każde trafienie wroga namierzającego tę jednostkę (nie działa przy braku [Aggro].)

## [00] Blade Lineage Salsu — Don Quixote — 검계 살수
- ID Tożsamości: `10308` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 3 · HP bazowe: 73 · szybkość: 4–6 / 4–7 / 4–8 / 4–8
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Poise

213. [Karta Tożsamości — tytuł] 검계\n살수
   źródło: Personalities.json :: dataList[id=10308].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Blade Lineage\nSalsu
   PL: Ród Ostrza\nSalsu
214. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10308].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10308].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Karta Tożsamości — opis] 돈키호테의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10308].desc
   limit: do 120 znaków
   EN: Don Quixote’s 8th Identity
   PL: Ósma Tożsamość Don Quixote
217. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 발검
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=1].name ; dataList[id=1030801].levelList[level=2].name ; dataList[id=1030801].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Draw of the Sword
   PL: Dobycie Ostrza
218. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=1].desc ; dataList[id=1030801].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2
219. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1030801].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath]
   PL: [OnSucceedAttackHead] Zyskuje 1 [Breath]
220. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1030801].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 5 이상이면 코인 위력 +1\n</style>[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 5+ [Breath] on self, Coin Power +1\n</style>[WhenUse] Gain +2 [Breath] Count
   PL: <style="highlight">Przy 5+ [Breath] Moc Monet +1\n</style>[WhenUse] Zwiększa własny Licznik [Breath] o 2
222. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL: [OnSucceedAttack] Zyskuje 1 [Breath]
223. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 검궤
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=1].name ; dataList[id=1030802].levelList[level=2].name ; dataList[id=1030802].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Blade Arc
   PL: Krąg Ostrza
225. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=1].desc ; dataList[id=1030802].levelList[level=2].desc
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 2 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath]
   PL: [OnSucceedAttackHead] Zyskuje 2 [Breath]
227. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] [Breath]이 없거나 [Breath] 위력을 가장 적게 보유한 아군 1명에게 [Breath] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1030802].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] To 1 ally that either has no [Breath] or has the least [Breath] Potency, apply 2 [Breath]
   PL: [CriticalOnSucceedAttack] Nakłada 2 [Breath] na 1 Sojusznika bez [Breath] lub z najmniejszą Mocą [Breath]
228. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1030802].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL: [OnSucceedAttack] Zyskuje 2 [Breath]
229. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 7 이상이면 코인 위력 +1\n</style>[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 7+ [Breath] on self, Coin Power +1\n</style>[WhenUse] Gain +2 [Breath] Count
   PL: <style="highlight">Przy 7+ [Breath] Moc Monet +1\n</style>[WhenUse] Zwiększa własny Licznik [Breath] o 2
230. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] [Breath]이 없거나 [Breath] 위력을 가장 적게 보유한 아군 1명에게 [Breath] 2 부여\n<style="highlight">대상이 검계 조직원이면 호흡 2 추가 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1030802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] To 1 ally that either has no [Breath] or has the least [Breath] Potency, apply 2 [Breath]\n<style="highlight">If the affected ally is from the Blade Lineage, apply 2 additional [Breath]</style>
   PL: [CriticalOnSucceedAttack] Nakłada 2 [Breath] na 1 Sojusznika bez [Breath] lub z najmniejszą Mocą [Breath]\n<style="highlight">Jeżeli takim sojusznikiem jest członek Rodu Ostrza, nakłada dodatkowo 2 [Breath]</style>
231. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 잘가시게!
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=3].name ; dataList[id=1030803].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Fare Thee Well!
   PL: Szczęśliwej Drogi!
232. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] [Breath] 5 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 5 [Breath]
   PL: [WhenUse] Zyskuje 5 [Breath]
233. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1030803].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] The final Coin deals +10% damage
   PL: [OnSucceedAttackHead] Ostatnia Moneta zadaje +10% obrażeń
234. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1030803].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] [Breath]이 없거나 [Breath] 횟수를 가장 적게 보유한 아군 2명의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] To 2 allies that either have no [Breath] or have the least [Breath] Count, apply +2 [Breath] Count
   PL: [CriticalOnSucceedAttack] Nakłada +2 Licznika [Breath] na 2 Sojuszników bez [Breath] lub z najmniejszym Licznikiem [Breath]
236. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [EndSkill] 대상이 사망했으면, 다음 턴에 [SlashDamageUp] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [SlashDamageUp]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: [EndSkill] If target is defeated, gain 1 [SlashDamageUp] next turn
   PL: [EndSkill] Jeżeli cel ginie, zyskuje w następnej turze 1 [SlashDamageUp]
237. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 10 이상이면 코인 위력 +1\n</style>[WhenUse] [Breath] 5 얻음
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 10+ [Breath] on self, Coin Power +1\n</style>[WhenUse] Gain 5 [Breath]
   PL: <style="highlight">Przy 10+ [Breath] Moc Monet +1\n</style>[WhenUse] Zyskuje 5 [Breath]
238. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   EN: +30% Damage on Critical Hit
   PL: Zadaje +30% obrażeń przy trafieniu krytycznym
239. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] [Breath]이 없거나 [Breath] 횟수를 가장 적게 보유한 아군 2명의 [Breath] 횟수 2 증가.\n<style="highlight">대상이 검계 조직원이면 [Breath] 횟수 2 추가 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] To 2 allies that either have no [Breath] or have the least [Breath] Count, apply +2 [Breath] Count\n<style="highlight">If the affected ally is from the Blade Lineage, apply 2 additional [Breath] Count</style>
   PL: [CriticalOnSucceedAttack] Nakłada +2 Licznika [Breath] na 2 Sojuszników bez [Breath] lub z najmniejszym Licznikiem [Breath].\n<style="highlight">Jeżeli takim sojusznikiem jest członek Rodu Ostrza, zwiększa Licznik dodatkowo o 2</style>
240. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] [EndSkill] 대상이 사망했으면, <style="highlight">자신과 무작위 아군 1명에게 다음 턴에 [SlashDamageUp] 1 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1030803].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkill], [SlashDamageUp]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: [EndSkill] If target is defeated, <style="highlight">apply 1 [SlashDamageUp] to self and 1 random other ally next turn</style>
   PL: [EndSkill] Jeżeli cel ginie, <style="highlight">nakłada w następnej turze 1 [SlashDamageUp] na siebie i 1 losowego sojusznika</style>
241. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills_personality-03.json :: dataList[id=1030804].levelList[level=1].name ; dataList[id=1030804].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 3 · monety: 1 (+10)
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Pride) — nazwa] 함께 쉬는 숨
   źródło: Passives.json :: dataList[id=1030801].name
   limit: do 40 znaków
   EN: Collective Breathing
   PL: Wspólny Oddech
243. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Pride) — opis] 자신의 스킬, 코인 효과로 [Breath] 위력을 얻을 때, [Breath]이 없거나 [Breath] 위력이 가장 낮은 아군 1명에게 [Breath] 1 부여 (최대 3회)
   źródło: Passives.json :: dataList[id=1030801].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: When this unit gains [Breath] Potency using its own Skill or Coin effects: Apply 1 [Breath] Potency to 1 ally that either has no [Breath] or has the least [Breath] Potency (max 3 times)
   PL: Gdy ta jednostka zyskuje Moc [Breath] efektem własnej Umiejętności lub Monety, nakłada 1 [Breath] na 1 Sojusznika bez [Breath] lub z najniższą Mocą [Breath] (maks. 3 razy)
244. [Pasywka bojowa (od ulepszenia 4, rezonans 2× Pride) — nazwa] 함께 쉬는 숨
   źródło: Passives.json :: dataList[id=1030811].name
   (powtórzenie elementu 242 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Pasywka bojowa (od ulepszenia 4, rezonans 2× Pride) — opis] 자신의 스킬, 코인 효과로 [Breath] 위력을 얻을 때, [Breath]이 없거나 [Breath] 위력이 가장 낮은 아군 1명에게 [Breath] 1 부여 (최대 5회)
   źródło: Passives.json :: dataList[id=1030811].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: When this unit gains [Breath] Potency using its own Skill or Coin effects: Give 1 [Breath] Potency to 1 ally that either has no [Breath] or has the least [Breath] Potency (max 5 times)
   PL: Gdy ta jednostka zyskuje Moc [Breath] efektem własnej Umiejętności lub Monety, nakłada 1 [Breath] na 1 Sojusznika bez [Breath] lub z najniższą Mocą [Breath] (maks. 5 razy)
246. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — nazwa] 밤 산책
   źródło: Passives.json :: dataList[id=1030821].name
   limit: do 40 znaków
   EN: Nightly Stroll
   PL: Nocny Spacer
247. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — opis] [Breath]을 가장 적게 보유한 아군 1명이 자신의 스킬, 코인 효과로 [Breath] 위력을 얻을 때 얻는 [Breath] 위력 +1 (최대 2회. [Breath]이 없는 대상에게는 적용되지 않음)
   źródło: Passives.json :: dataList[id=1030821].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: 1 ally that has the least [Breath] gains 1 more [Breath] Potency when gaining [Breath] Potency using its own Skill or Coin effects (max 2 times; does not apply to allies that do not have [Breath])
   PL: Sojusznik z najmniejszym [Breath] zyskuje o 1 więcej Mocy [Breath], gdy sam zyskuje Moc [Breath] efektem własnej Umiejętności lub Monety (maks. 2 razy; nie dotyczy sojuszników bez [Breath])
248. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Pride) — nazwa] 밤 산책
   źródło: Passives.json :: dataList[id=1030831].name
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Pride) — opis] [Breath]을 가장 적게 보유한 아군 1명이 자신의 스킬, 코인 효과로 [Breath] 위력을 얻을 때 얻는 [Breath] 위력 +2 (최대 2회. [Breath]이 없는 대상에게는 적용되지 않음)
   źródło: Passives.json :: dataList[id=1030831].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: 1 ally that has the least [Breath] gains 2 more [Breath] Potency when gaining [Breath] Potency using its own Skill or Coin effects (max 2 times; does not apply to allies that do not have [Breath])
   PL: 1 Sojusznik z najmniejszym [Breath] zyskuje o 2 więcej Mocy [Breath], gdy sam zyskuje Moc [Breath] efektem własnej Umiejętności lub Monety (maks. 2 razy; nie dotyczy sojuszników bez [Breath])

## [000] T Corp. Class 3 Collection Staff — Don Quixote — T사 3등급 징수직 직원
- ID Tożsamości: `10309` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 95 · szybkość: 3–6 / 3–6 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor

250. [Karta Tożsamości — tytuł] T사 3등급\n징수직 직원
   źródło: Personalities.json :: dataList[id=10309].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: T Corp. Class 3\nCollection Staff
   PL: Korporacja T 3. klasy\nPersonel Poboru
251. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10309].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10309].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Karta Tożsamości — opis] 돈키호테의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10309].desc
   limit: do 120 znaków
   EN: Don Quixote’s 9th Identity
   PL: Dziewiąta Tożsamość Don Quixote
254. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 징수 준비를 하지
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=1].name ; dataList[id=1030901].levelList[level=2].name ; dataList[id=1030901].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Let Us Prepare To Collect
   PL: Przygotujmy Się do Poboru
255. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 2
256. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]
257. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">[WhenUse] 대상의 [Vibration]이 6 이상이면, 합 위력 +1\n[WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=2].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +2 [Vibration] Count\n<style="highlight">[WhenUse] If target has 6+ [Vibration], Clash Power +1\n[WhenUse] Gain +3 [Aggro] to this Skill Slot next turn</style>
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 2\n<style="highlight">[WhenUse] Jeżeli cel ma 6+ [Vibration], Moc Starcia +1\n[WhenUse] W następnej turze [Aggro] tego slotu Umiejętności rośnie o 3</style>
258. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1030901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Vibration]
259. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">[WhenUse] 대상의 [Vibration] 6 당 합 위력 +1 (최대 2)</style>\n[WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +2 [Vibration] Count\n<style="highlight">[WhenUse] Gain Clash Power +1 for every 6 [Vibration] on target (max 2)</style>\n[WhenUse] Gain +3 [Aggro] to this Skill Slot next turn
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 2\n<style="highlight">[WhenUse] Moc Starcia +1 za każde 6 [Vibration] na celu (maks. 2)</style>\n[WhenUse] W następnej turze [Aggro] tego slotu Umiejętności rośnie o 3
260. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 이 스킬 슬롯의 [Aggro] 4 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1030901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Aggro]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Aggro] = 도발치 / Aggro
   EN: <style="highlight">[OnSucceedAttack] Gain +4 [Aggro] to this Skill Slot next turn</style>
   PL: <style="highlight">[OnSucceedAttack] W następnej turze [Aggro] tego slotu Umiejętności rośnie o 4</style>
261. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] T사제 가속 절단기
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=1].name ; dataList[id=1030902].levelList[level=2].name ; dataList[id=1030902].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 50 znaków
   EN: T Corp. Accelerated Amputator
   PL: Przyspieszony Amputator Korporacji T
262. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 3
263. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]을 최대 3 소모\n소모한 [Vibration]만큼 자신의 [Vibration] 횟수 증가
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1030902].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Consume up to 3 [Vibration] on target, and gain the same amount of [Vibration] Count on self
   PL: [OnSucceedAttack] Zużywa do 3 [Vibration] celu\ni zwiększa własny Licznik [Vibration] o zużytą ilość
264. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
265. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 [Vibration] 횟수 3 증가\n<style="highlight">[WhenUse] 대상의 [Vibration]이 6 이상이면, 합 위력 +1</style>
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count\n<style="highlight">[WhenUse] If target has 6+ [Vibration], Clash Power +1</style>
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 3\n<style="highlight">[WhenUse] Jeżeli cel ma 6+ [Vibration], Moc Starcia +1</style>
266. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Vibration]
267. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 이 스킬의 코인 효과로 대상의 [Vibration]을 소모했다면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: <style="highlight">[OnSucceedAttack] If this Skill's Coin effects consumed [Vibration] on target, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli efekty monet tej Umiejętności zużyły [Vibration] celu, [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1</style>
268. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 3 증가\n[WhenUse] 대상의 [Vibration] <style="highlight">6 당 합 위력 +1 (최대 2)</style>
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count\n[WhenUse] <style="highlight">Clash Power +1 for every 6 [Vibration] on target (max 2)</style>
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 3\n[WhenUse] <style="highlight">Moc Starcia +1 za każde 6 [Vibration] na celu (maks. 2)</style>
269. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]을 최대 3 소모\n(소모한 [Vibration]<style="highlight">x2</style>)만큼 자신의 [Vibration] 횟수 증가\n<style="highlight">다음 턴에 (소모한 [Vibration]-1)만큼 [Binding] 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Vibration], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Consume up to 3 [Vibration] on target, and gain <style="highlight">double the amount consumed</style> as [Vibration] Count on self\n<style="highlight">Inflict ([Vibration] consumed - 1) [Binding] next turn</style>
   PL: [OnSucceedAttack] Zużywa do 3 [Vibration] celu i zwiększa własny Licznik [Vibration] o <style="highlight">zużytą ilość x 2</style>\n<style="highlight">Nakłada w następnej turze ([Vibration] zużyte - 1) [Binding]</style>
270. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Vibration]<style="highlight"></style>
271. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 이 스킬의 코인 효과로 대상의 [Vibration]을 소모했다면 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1030902].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If this Skill's Coin effects consumed [Vibration] on target, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli efekty monet tej Umiejętności zużyły [Vibration] celu, [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1<style="highlight"></style>
272. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 거기 멈추도록!
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=3].name ; dataList[id=1030903].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: I Command Thee, Halt!
   PL: Rozkażam Ci stanąć!
273. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 [Vibration]이 6 이상이면, 합 위력 +1\n[WhenUse] 자신의 [Vibration] 횟수를 10 소모하여 코인 위력 +2
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 6+ [Vibration], Clash Power +1\n[WhenUse] Consume 10 [Vibration] Count on self to gain Coin Power +2
   PL: [WhenUse] Jeżeli cel ma 6+ [Vibration], Moc Starcia +1\n[WhenUse] Zużywa 10 Licznika [Vibration], aby zyskać Moc Monet +2
274. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1030903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]이 10 이상이면, 대상의 [Vibration]을 10 소모하여 [TimeSuspend] 2 부여\n- 자신이 [TimeRentalTwoPersonality] 상태면, 대상의 [Vibration]을 소모하지 않음
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Vibration], [TimeSuspend], [TimeRentalTwoPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [TimeSuspend] = 시간 유예 / Time Moratorium; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time
   EN: [OnSucceedAttack] If target has 10+ [Vibration], consume 10 [Vibration] on target and inflict 2 [TimeSuspend]\n- If this unit is in a [TimeRentalTwoPersonality] state, this effect does not consume the target's [Vibration]
   PL: [OnSucceedAttack] Jeżeli cel ma 10+ [Vibration], zużywa 10 [Vibration] celu i nakłada 2 [TimeSuspend]\n- Jeżeli ta jednostka jest w stanie [TimeRentalTwoPersonality], ten efekt nie zużywa [Vibration] celu
276. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 속도가 자신보다 낮다면, [VibrationChainPersonality]로 [Switch_Vibration]
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationChainPersonality], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationChainPersonality] = 진동 - 사슬 / Tremor - Chain; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] If target's Speed is slower than this unit's, trigger [Switch_Vibration] into [VibrationChainPersonality]
   PL: [OnSucceedAttack] Jeżeli Szybkość celu jest niższa od tej jednostki, wywołuje [Switch_Vibration] do [VibrationChainPersonality]
277. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 대상의 [Vibration] <style="highlight">6 당 합 위력 +1 (최대 2)</style>\n<style="highlight">[WhenUse] 대상이 [Binding] 상태면, 합 위력 +1</style>\n[WhenUse] 자신의 [Vibration] 횟수를 10 소모하여 코인 위력 +2
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [Binding]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Binding] = 속박 / Bind
   EN: [WhenUse] <style="highlight">Clash Power +1 for every 6 [Vibration] on target (max 2)</style>\n<style="highlight">[WhenUse] If target has [Binding], gain Clash Power +1</style>\n[WhenUse] Consume 10 [Vibration] Count on self to gain Coin Power +2
   PL: [WhenUse] <style="highlight">Moc Starcia +1 za każde 6 [Vibration] na celu (maks. 2)</style>\n<style="highlight">[WhenUse] Jeżeli cel ma [Binding], Moc Starcia +1</style>\n[WhenUse] Zużywa 10 Licznika [Vibration], aby zyskać Moc Monet +2
278. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Vibration] 3 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] Inflict 3 [Vibration]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 3 [Vibration]</style>
279. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]이 10 이상이면, 대상의 [Vibration]을 10 소모하여 [TimeSuspend] 2 부여\n- 자신이 [TimeRentalTwoPersonality] 상태면, 대상의 [Vibration]을 소모하지 않음<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Vibration], [TimeSuspend], [TimeRentalTwoPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [TimeSuspend] = 시간 유예 / Time Moratorium; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time
   EN: [OnSucceedAttack] If target has 10+ [Vibration], consume 10 [Vibration] on target and inflict 2 [TimeSuspend]\n- If this unit is in a [TimeRentalTwoPersonality] state, this effect does not consume the target's [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli cel ma 10+ [Vibration], zużywa 10 [Vibration] celu i nakłada 2 [TimeSuspend]\n- Jeżeli ta jednostka jest w stanie [TimeRentalTwoPersonality], ten efekt nie zużywa [Vibration] celu<style="highlight"></style>
280. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL: <style="highlight">[OnSucceedAttack] [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1</style>
281. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 대상의 속도가 자신보다 낮다면, [VibrationChainPersonality]로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1030903].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationChainPersonality], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationChainPersonality] = 진동 - 사슬 / Tremor - Chain; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] If target's Speed is slower than this unit's, trigger [Switch_Vibration] into [VibrationChainPersonality]<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli Szybkość celu jest niższa od tej jednostki, wywołuje [Switch_Vibration] do [VibrationChainPersonality]<style="highlight"></style>
282. [Obrona (ulepszenia 1,4) — nazwa] 시간을 끌어와보도록 하지
   źródło: Skills_personality-03.json :: dataList[id=1030904].levelList[level=1].name ; dataList[id=1030904].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   limit: do 40 znaków
   EN: I Shall Summon the Time
   PL: Przywołam Czas
283. [Obrona (ulepszenie 1) — opis] [StartBattle] [TimeRentalTwoPersonality] 상태가 아니면, 턴 종료 시 [TimeRentalTwoPersonality] 4 얻음 (턴 당 1회)\n[WhenUse] 이번 턴 동안 적에게 피격 시, 다음 턴에 대상에게 [Vibration] 2 부여 (턴 당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1030904].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [TimeRentalTwoPersonality], [WhenUse], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] If this unit is not in a [TimeRentalTwoPersonality] state, gain 4 [TimeRentalTwoPersonality] at Turn End (once per turn)\n[WhenUse] For this turn: when hit by an enemy, inflict 2 [Vibration] on target next turn (2 times per turn)
   PL: [StartBattle] Jeżeli ta jednostka nie jest w stanie [TimeRentalTwoPersonality], zyskuje 4 [TimeRentalTwoPersonality] na koniec tury (1 raz na turę)\n[WhenUse] W tej turze: gdy zostanie trafiona przez wroga, nakłada w następnej turze 2 [Vibration] na celu (2 razy na turę)
284. [Obrona (ulepszenie 4) — opis] [StartBattle] [TimeRentalTwoPersonality] 상태가 아니면, 턴 종료 시 [TimeRentalTwoPersonality] 4 얻음 (턴 당 1회)\n[WhenUse] 이번 턴 동안 적에게 피격 시, 다음 턴에 대상에게 [Vibration] <style="highlight">3</style> 부여 (턴 당 <style="highlight">6</style>회)
   źródło: Skills_personality-03.json :: dataList[id=1030904].levelList[level=4].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [TimeRentalTwoPersonality], [WhenUse], [Vibration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [StartBattle] If this unit is not in a [TimeRentalTwoPersonality] state, gain 4 [TimeRentalTwoPersonality] at Turn End (once per turn)\n[WhenUse] For this turn: when hit by an enemy, inflict <style="highlight">3</style> [Vibration] on target next turn (<style="highlight">6 times</style> per turn)
   PL: [StartBattle] Jeżeli ta jednostka nie jest w stanie [TimeRentalTwoPersonality], zyskuje 4 [TimeRentalTwoPersonality] na koniec tury (1 raz na turę)\n[WhenUse] W tej turze: gdy zostanie trafiona przez wroga, nakłada w następnej turze <style="highlight">3</style> [Vibration] na celu (<style="highlight">6 razy</style> na turę)
285. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — nazwa] 황금 시간 - 받아내기
   źródło: Passives.json :: dataList[id=1030901].name
   limit: do 40 znaków
   EN: Golden Time - Extracting
   PL: Złota Godzina - Pobór
286. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Sloth) — opis] 턴 종료 시 체력이 10% ~ 20% 사이로 남았을 때, 전체 체력의 80%만큼 즉시 회복. 흐트러짐 상태 해제 (전투 당 1회)\n\n[TimeRentalTwoPersonality]가 해제될 경우, 다음 턴에 보유 중인 스킬 슬롯 중 하나의 [Aggro] 8 증가
   źródło: Passives.json :: dataList[id=1030901].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [TimeRentalTwoPersonality], [Aggro]
   znaczenie tagów: [TimeRentalTwoPersonality] = 시간 대여 / Borrowed Time; [Aggro] = 도발치 / Aggro
   EN: Turn End: If this unit's HP is between 10% ~ 20%, instantly heal 80% of this unit's max HP, and recover from Stagger. (once per Encounter)\n\nWhen this unit loses [TimeRentalTwoPersonality], gain +8 [Aggro] to one of this unit's Skill Slots next turn
   PL: Na koniec tury, jeżeli HP wynosi od 10% do 20%, natychmiast odzyskuje 80% Maks. HP i dochodzi do siebie z Ogłuszenia. (1 raz na spotkanie)\n\nGdy ta jednostka traci [TimeRentalTwoPersonality], w następnej turze [Aggro] jednego z jej slotów Umiejętności rośnie o 8
287. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — nazwa] T사식 물리왜곡장
   źródło: Passives.json :: dataList[id=1030921].name
   limit: do 50 znaków
   EN: T Corp. Physics Distortion Field
   PL: Pole Zniekształcenia Fizyki Korporacji T
288. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — opis] 속도가 가장 느린 아군 1명이 [Vibration]이 부여된 적에게 피해를 받을 때, 받는 피해량 -10%
   źródło: Passives.json :: dataList[id=1030921].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: When 1 ally with the slowest Speed takes damage from enemies that have [Vibration], take -10% damage
   PL: Gdy 1 Sojusznik z najniższą Szybkością otrzymuje obrażenia od wrogów z [Vibration], otrzymuje -10% obrażeń

## [000] The Manager of La Manchaland — Don Quixote — 라만차랜드 실장
- ID Tożsamości: `10310` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 63 · szybkość: 4–6 / 4–7 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Bleed

289. [Karta Tożsamości — tytuł] 라만차랜드\n실장
   źródło: Personalities.json :: dataList[id=10310].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Manager\nof La Manchaland
   PL: Zarząd\nLa Manchaland
290. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10310].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10310].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Karta Tożsamości — opis] 돈키호테의 열번째 인격
   źródło: Personalities.json :: dataList[id=10310].desc
   limit: do 120 znaków
   EN: Don Quixote’s 10th Identity
   PL: Dziesiąta Tożsamość Don Quixote
293. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 참는 것은 끝이다
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=1].name ; dataList[id=1031001].levelList[level=2].name ; dataList[id=1031001].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Enough is Enough
   PL: Dość Tolerowania
294. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 5 당, [BloodArmorPersonalityFirst] 1얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 5 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 30% zadanych obrażeń HP (maks. 10)\n[WhenUse] Zużywa do 50 [BloodDinner] i zyskuje 1 [BloodArmorPersonalityFirst] za każde 5 zużytego [BloodDinner]\n- Jeżeli nie udało się zużyć [BloodDinner], zyskuje 5 [Laceration]
295. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]
296. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 5 당, [BloodArmorPersonalityFirst] 1얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n<style="highlight">[WhenUse] 대상의 [Laceration] 6 이상이면 코인 위력 +1</style>
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=2].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 5 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 30% zadanych obrażeń HP (maks. 10)\n[WhenUse] Zużywa do 50 [BloodDinner] i zyskuje 1 [BloodArmorPersonalityFirst] za każde 5 zużytego [BloodDinner]\n- Jeżeli nie udało się zużyć [BloodDinner], zyskuje 5 [Laceration]\n<style="highlight">[WhenUse] Jeżeli cel ma 6+ [Laceration], Moc Monet +1</style>
297. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1031001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]
298. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 5 당, [BloodArmorPersonalityFirst] 1얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n[WhenUse] 대상의 [Laceration] <style="highlight">6 당</style> 코인 위력 +1 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 5 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n[WhenUse] <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 30% zadanych obrażeń HP (maks. 10)\n[WhenUse] Zużywa do 50 [BloodDinner] i zyskuje 1 [BloodArmorPersonalityFirst] za każde 5 zużytego [BloodDinner]\n- Jeżeli nie udało się zużyć [BloodDinner], zyskuje 5 [Laceration]\n[WhenUse] Moc Monet +1 za każde <style="highlight">6</style> [Laceration] celu <style="highlight">(maks. 2)</style>
299. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031001].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 원하는대로 펼쳐라
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=1].name ; dataList[id=1031002].levelList[level=2].name ; dataList[id=1031002].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Let All Blossom Free
   PL: Niech Wszystko Rozkwitnie
301. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10 당, [BloodArmorPersonalityFirst] 1얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n[BeforeAttack] [BloodArmorPersonalityFirst] 10 이상이면, 공격 가중치 +1
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=1].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n[BeforeAttack] At 10+ [BloodArmorPersonalityFirst], Atk Weight +1
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 30% zadanych obrażeń HP (maks. 10)\n[WhenUse] Zużywa do 50 [BloodDinner] i zyskuje 1 [BloodArmorPersonalityFirst] za każde 10 zużytego [BloodDinner]\n- Jeżeli nie udało się zużyć [BloodDinner], zyskuje 5 [Laceration]\n[BeforeAttack] Przy 10+ [BloodArmorPersonalityFirst] Waga ataku +1
302. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1031002].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1031002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] 대상의 [Laceration]당 피해량 +2.5% (최대 25%)
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1031002].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1031002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Deal +2.5% damage for every [Laceration] on target (max 25%)
   PL: Zadaje +2.5% obrażeń za każde 1 [Laceration] na celu (maks. 25%)
304. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] 자신의 [BloodDinner_Accumulation] 100당 피해량 +5% (최대 25%)
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BloodDinner_Accumulation]
   znaczenie tagów: [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed
   EN: Deal +5% damage for every 100 [BloodDinner_Accumulation] by self (max 25%)
   PL: Zadaje +5% obrażeń za każde 100 własnego [BloodDinner_Accumulation] (maks. 25%)
305. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10 당, [BloodArmorPersonalityFirst] 1얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n<style="highlight">[WhenUse] 대상의 [Laceration] 6 이상이면, 코인 위력 +1</style>\n[BeforeAttack] [BloodArmorPersonalityFirst] <style="highlight">10 당</style> 공격 가중치 1 증가 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=2].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>\n[BeforeAttack] <style="highlight">Atk Weight +1 for every 10 [BloodArmorPersonalityFirst] on self (max 2)</style>
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 30% zadanych obrażeń HP (maks. 10)\n[WhenUse] Zużywa do 50 [BloodDinner] i zyskuje 1 [BloodArmorPersonalityFirst] za każde 10 zużytego [BloodDinner]\n- Jeżeli nie udało się zużyć [BloodDinner], zyskuje 5 [Laceration]\n<style="highlight">[WhenUse] Jeżeli cel ma 6+ [Laceration], Moc Monet +1</style>\n[BeforeAttack] Waga ataku +1 za każde <style="highlight">10</style> [BloodArmorPersonalityFirst] <style="highlight">(maks. 2)</style>
306. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] 자신의 [BloodDinner_Accumulation] 100당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">50</style>%)
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BloodDinner_Accumulation]
   znaczenie tagów: [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed
   EN: Deal +<style="highlight">10</style>% damage for every 100 [BloodDinner_Accumulation] by self (max <style="highlight">50</style>%)
   PL: Zadaje +<style="highlight">10</style>% obrażeń za każde 100 własnego [BloodDinner_Accumulation] (maks. <style="highlight">50</style>%)
307. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10 당, [BloodArmorPersonalityFirst] 1얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 5 얻음\n[WhenUse] 대상의 [Laceration] <style="highlight">6 당</style> 코인 위력 +1 <style="highlight">(최대 2)</style>\n[BeforeAttack] [BloodArmorPersonalityFirst] 10 당 공격 가중치 1 증가 (최대 2)
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=4].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner] this unit consumed\n- If this unit failed to consume [BloodDinner], gain 5 [Laceration]\n[WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[BeforeAttack] Atk Weight +1 for every 10 [BloodArmorPersonalityFirst] on self (max 2)
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 30% zadanych obrażeń HP (maks. 10)\n[WhenUse] Zużywa do 50 [BloodDinner] i zyskuje 1 [BloodArmorPersonalityFirst] za każde 10 zużytego [BloodDinner]\n- Jeżeli nie udało się zużyć [BloodDinner], zyskuje 5 [Laceration]\n[WhenUse] Moc Monet +1 za każde <style="highlight">6</style> [Laceration] celu <style="highlight">(maks. 2)</style>\n[BeforeAttack] Waga ataku +1 za każde 10 [BloodArmorPersonalityFirst] (maks. 2)
308. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] 자신의 [BloodDinner_Accumulation] 100당 피해량 +<style="highlight">15</style>% (최대 <style="highlight">75</style>%)
   źródło: Skills_personality-03.json :: dataList[id=1031002].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BloodDinner_Accumulation]
   znaczenie tagów: [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed
   EN: Deal +<style="highlight">15</style>% damage for every 100 [BloodDinner_Accumulation] by self (max <style="highlight">75</style>%)
   PL: Zadaje +<style="highlight">15</style>% obrażeń za każde 100 własnego [BloodDinner_Accumulation] (maks. <style="highlight">75</style>%)
309. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 꿰뚫겠습니다
   źródło: Skills_personality-03.json :: dataList[id=1031003].levelList[level=3].name ; dataList[id=1031003].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: I Shall Impale
   PL: Przebiję Cię
310. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 10 회복)\n[WhenUse] 자신의 [BloodArmorPersonalityFirst] 10 당, 합 위력 +1 (최대 2)\n[WhenUse] 대상의 [Laceration] 10 이상이면, 코인 위력 +1\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10 당, [BloodArmorPersonalityFirst] 1 얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음\n대상의 [Laceration]당 피해량 +5% (최대 50%)\n자신의 [BloodDinner_Accumulation] 100 당 피해량 +10% (최대 50%)\n[EndSkill] 대상이 사망한 경우 [BloodDinner] 30 증가. [BloodArmorPersonalityFirst] 10 얻음 (턴 당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031003].levelList[level=3].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodArmorPersonalityFirst], [Laceration], [BloodDinner], [BloodDinner_Accumulation], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: heal 50% of the HP damage dealt (max 10)\n[WhenUse] Clash Power +1 for every 10 [BloodArmorPersonalityFirst] (max 2)\n[WhenUse] If target has 10+ [Laceration], Coin Power +1\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner] consumed\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]\nDeal +5% damage for every [Laceration] on target (max 50%)\nDeal +10% damage for every 100 [BloodDinner_Accumulation] by self (max 50%)\n[EndSkill] If target is defeated, increase [BloodDinner] by 30; gain 10 [BloodArmorPersonalityFirst] (once per turn)
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 50% zadanych obrażeń HP (maks. 10)\n[WhenUse] Moc Starcia +1 za każde 10 [BloodArmorPersonalityFirst] (maks. 2)\n[WhenUse] Jeżeli cel ma 10+ [Laceration], Moc Monet +1\n[WhenUse] Zużywa do 50 [BloodDinner] i zyskuje 1 [BloodArmorPersonalityFirst] za każde 10 zużytego [BloodDinner]\n- Jeżeli nie udało się zużyć [BloodDinner], zyskuje 10 [Laceration]\nZadaje +5% obrażeń za każde 1 [Laceration] na celu (maks. 50%)\nZadaje +10% obrażeń za każde 100 własnego [BloodDinner_Accumulation] (maks. 50%)\n[EndSkill] Jeżeli cel ginie, zwiększa [BloodDinner] o 30 i zyskuje 10 [BloodArmorPersonalityFirst] (1 raz na turę)
311. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-03.json :: dataList[id=1031003].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1031003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] Nakłada 3 [Laceration]
312. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 10 회복)\n[WhenUse] 자신의 [BloodArmorPersonalityFirst] 10 당, 합 위력 +1 (최대 2)\n[WhenUse] 대상의 [Laceration] <style="highlight">5 당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] [BloodDinner]을 최대 50 소모하여, 소모한 [BloodDinner] 10 당, [BloodArmorPersonalityFirst] 1 얻음\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음\n대상의 [Laceration]당 피해량 +5% (최대 50%)\n자신의 [BloodDinner_Accumulation] 100 당 피해량 +<style="highlight">20</style>% (최대 <style="highlight">100</style>%)\n[EndSkill] 대상이 사망한 경우 [BloodDinner] <style="highlight">60</style> 증가. [BloodArmorPersonalityFirst] 10 얻음 (턴 당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031003].levelList[level=4].desc
   limit: do 820 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodArmorPersonalityFirst], [Laceration], [BloodDinner], [BloodDinner_Accumulation], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast; [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: heal 50% of the HP damage dealt (max 10)\n[WhenUse] Clash Power +1 for every 10 [BloodArmorPersonalityFirst] (max 2)\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Laceration] on target (max 2)</style>\n[WhenUse] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner] consumed\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]\nDeal +5% damage for every [Laceration] on target (max 50%)\nDeal +<style="highlight">20</style>% damage for every 100 [BloodDinner_Accumulation] by self (max <style="highlight">100</style>%)\n[EndSkill] If target is defeated, increase [BloodDinner] by <style="highlight">60</style>; gain 10 [BloodArmorPersonalityFirst] (once per turn)
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 50% zadanych obrażeń HP (maks. 10)\n[WhenUse] Moc Starcia +1 za każde 10 [BloodArmorPersonalityFirst] (maks. 2)\n[WhenUse] Moc Monet +1 za każde <style="highlight">5</style> [Laceration] celu <style="highlight">(maks. 2)</style>\n[WhenUse] Zużywa do 50 [BloodDinner] i zyskuje 1 [BloodArmorPersonalityFirst] za każde 10 zużytego [BloodDinner]\n- Jeżeli nie udało się zużyć [BloodDinner], zyskuje 10 [Laceration]\nZadaje +5% obrażeń za każde 1 [Laceration] na celu (maks. 50%)\nZadaje +<style="highlight">20</style>% obrażeń za każde 100 własnego [BloodDinner_Accumulation] (maks. <style="highlight">100</style>%)\n[EndSkill] Jeżeli cel ginie, zwiększa [BloodDinner] o <style="highlight">60</style> i zyskuje 10 [BloodArmorPersonalityFirst] (1 raz na turę)
313. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — nazwa] 아류 산초 경혈 6식 - 채찍
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=1].name ; dataList[id=1031005].levelList[level=2].name ; dataList[id=1031005].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 60 znaków
   EN: Variant Sancho Hardblood Arts 6 - Whip
   PL: Wariantowy Sancho Twardokrwisty Styl 6 - Bicz
314. [Umiejętność 4 (×0) (ulepszenie 1) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 20 회복)\n[WhenUse] [Laceration] 20 얻음\n[WhenUse] [BloodArmorPersonalityFirst] 10 당 적중시 부여하는 [Laceration] +1 (최대 2). 공격 종료 시 [BloodArmorPersonalityFirst] 10 소모
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BloodArmorPersonalityFirst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodArmorPersonalityFirst] = 경혈 / Hardblood
   EN: On Hit with this Skill: Heal 50% of the HP damage dealt (max 20)\n[WhenUse] Gain 20 [Laceration]\n[WhenUse] Inflict +1 more [Laceration] On Hit for every 10 [BloodArmorPersonalityFirst]. (max 2) Attack End: Consume 10 [BloodArmorPersonalityFirst]
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 50% zadanych obrażeń HP (maks. 20)\n[WhenUse] Zyskuje 20 [Laceration]\n[WhenUse] Nakłada o 1 więcej [Laceration] przy trafieniu za każde 10 [BloodArmorPersonalityFirst]. (maks. 2) Na koniec ataku zużywa 10 [BloodArmorPersonalityFirst]
315. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1031005].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1031005].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
316. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1031005].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1031005].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1031005].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1031005].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1031005].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1031005].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [Umiejętność 4 (×0) (ulepszenie 2) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 20 회복)\n<style="highlight">[WhenUse] 대상의 [Laceration] 6 이상이면, 코인 위력 +1</style>\n[WhenUse] [Laceration] 20 얻음\n[WhenUse] [BloodArmorPersonalityFirst] 10 당 적중시 부여하는 [Laceration] +1 (최대 2). 공격 종료 시 [BloodArmorPersonalityFirst] 10 소모
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=2].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [BloodArmorPersonalityFirst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodArmorPersonalityFirst] = 경혈 / Hardblood
   EN: On Hit with this Skill: Heal 50% of the HP damage dealt (max 20)\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>\n[WhenUse] Gain 20 [Laceration]\n[WhenUse] Inflict +1 more [Laceration] On Hit for every 10 [BloodArmorPersonalityFirst]. (max 2) Attack End: Consume 10 [BloodArmorPersonalityFirst]
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 50% zadanych obrażeń HP (maks. 20)\n<style="highlight">[WhenUse] Jeżeli cel ma 6+ [Laceration], Moc Monet +1</style>\n[WhenUse] Zyskuje 20 [Laceration]\n[WhenUse] Nakłada o 1 więcej [Laceration] przy trafieniu za każde 10 [BloodArmorPersonalityFirst]. (maks. 2) Na koniec ataku zużywa 10 [BloodArmorPersonalityFirst]
320. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 20 회복)\n[WhenUse] 대상의 [Laceration] <style="highlight">6 당</style> 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] [Laceration] 20 얻음\n[WhenUse] [BloodArmorPersonalityFirst] 10당 적중시 부여하는 [Laceration] +1 (최대 2). 공격 종료 시 [BloodArmorPersonalityFirst] 10 소모
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=4].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [BloodArmorPersonalityFirst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodArmorPersonalityFirst] = 경혈 / Hardblood
   EN: On Hit with this Skill: Heal 50% of the HP damage dealt (max 20)\n[WhenUse] <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[WhenUse] Gain 20 [Laceration]\n[WhenUse] Inflict +1 more [Laceration] On Hit for every 10 [BloodArmorPersonalityFirst]. (max 2) Attack End: Consume 10 [BloodArmorPersonalityFirst]
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 50% zadanych obrażeń HP (maks. 20)\n[WhenUse] Moc Monet +1 za każde <style="highlight">6</style> [Laceration] celu <style="highlight">(maks. 2)</style>\n[WhenUse] Zyskuje 20 [Laceration]\n[WhenUse] Nakłada o 1 więcej [Laceration] przy trafieniu za każde 10 [BloodArmorPersonalityFirst]. (maks. 2) Na koniec ataku zużywa 10 [BloodArmorPersonalityFirst]
321. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 대상의 [Laceration]을 1회 발동 시킴. 대상의 [Laceration] 횟수 1 감소</style>
   źródło: Skills_personality-03.json :: dataList[id=1031005].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack] Activate [Laceration] on target once (target loses 1 [Laceration] Count)</style>
   PL: <style="highlight">[OnSucceedAttack] Uruchamia 1 [Laceration] celu (cel traci 1 Licznika [Laceration])</style>
322. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — nazwa] 아류 산초 경혈 8식 - 갈라지도록
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].name ; dataList[id=1031006].levelList[level=2].name ; dataList[id=1031006].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 70 znaków
   EN: Variant Sancho Hardblood Arts 8 - Split Apart
   PL: Wariantowy Sancho Twardokrwisty Styl 8 - Rozszczepienie
323. [Umiejętność 5 (×0) (ulepszenie 1) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] 대상의 [Laceration] 6 이상이면, 코인 위력 +1\n[BeforeAttack] [BloodArmorPersonalityFirst] 10 이상이면, 공격 가중치 +1\n[EndSkill] 공격 가중치가 증가했다면, [BloodArmorPersonalityFirst] 10 소모
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BeforeAttack], [BloodArmorPersonalityFirst], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[BeforeAttack] At 10+ [BloodArmorPersonalityFirst], Atk Weight +1\n[EndSkill] If this Skill had an increased Atk Weight, consume 10 [BloodArmorPersonalityFirst]
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 30% zadanych obrażeń HP (maks. 10)\n[WhenUse] Jeżeli cel ma 6+ [Laceration], Moc Monet +1\n[BeforeAttack] Przy 10+ [BloodArmorPersonalityFirst] Waga ataku +1\n[EndSkill] Jeżeli Waga ataku została zwiększona, zużywa 10 [BloodArmorPersonalityFirst]
324. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1031006].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1031006].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1031006].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1031006].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1031006].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1031006].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — moneta 3, efekt 2 — opis] 대상의 [Laceration]당 피해량 +2.5% (최대 25%)
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1031006].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1031006].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 3, efekt 3 — opis] [BloodDinner_Common_Accumulation] 100당 피해량 +5% (최대 25%)
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BloodDinner_Common_Accumulation]
   znaczenie tagów: [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared)
   EN: Deal +5% damage for every 100 [BloodDinner_Common_Accumulation] (max 25%)
   PL: Zadaje +5% obrażeń za każde 100 [BloodDinner_Common_Accumulation] (maks. 25%)
329. [Umiejętność 5 (×0) (ulepszenie 2) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] 대상의 [Laceration] <style="highlight">6 당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[BeforeAttack] [BloodArmorPersonalityFirst] <style="highlight">10 당</style> 공격 가중치 증가 <style="highlight">(최대 2)</style>\n[EndSkill] 증가한 가중치당 [BloodArmorPersonalityFirst] 10 소모
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=2].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [BeforeAttack], [BloodArmorPersonalityFirst], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[BeforeAttack] <style="highlight">Gain Atk Weight +1 for every 10 [BloodArmorPersonalityFirst] (max 2)</style>\n[EndSkill] Consume 10 [BloodArmorPersonalityFirst] for every Atk Weight gained
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 30% zadanych obrażeń HP (maks. 10)\n[WhenUse] Moc Monet +1 za każde <style="highlight">6</style> [Laceration] celu <style="highlight">(maks. 2)</style>\n[BeforeAttack] <style="highlight">Zyskuje Wagę ataku +1 za każde 10 [BloodArmorPersonalityFirst] (maks. 2)</style>\n[EndSkill] Zużywa 10 [BloodArmorPersonalityFirst] za każdą zwiększoną Wagę ataku
330. [Umiejętność 5 (×0) (ulepszenie 2) — moneta 3, efekt 3 — opis] [BloodDinner_Common_Accumulation] 100당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">50</style>%)
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=2].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BloodDinner_Common_Accumulation]
   znaczenie tagów: [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared)
   EN: Deal +<style="highlight">10</style>% damage for every 100 [BloodDinner_Common_Accumulation] (max <style="highlight">50</style>%)
   PL: Zadaje +<style="highlight">10</style>% obrażeń za każde 100 [BloodDinner_Common_Accumulation] (maks. <style="highlight">50</style>%)
331. [Umiejętność 5 (×0) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복 (최대 10 회복)\n[WhenUse] 대상의 [Laceration] 6 당 코인 위력 +1 (최대 2)\n[BeforeAttack] [BloodArmorPersonalityFirst] 10당 공격 가중치 증가 (최대 2)\n[EndSkill] 증가한 가중치당 [BloodArmorPersonalityFirst] 10 소모<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [BeforeAttack], [BloodArmorPersonalityFirst], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: heal 30% of the HP damage dealt (max 10)\n[WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)\n[BeforeAttack] Gain Atk Weight +1 for every 10 [BloodArmorPersonalityFirst] (max 2)\n[EndSkill] Consume 10 [BloodArmorPersonalityFirst] for every Atk Weight gained<style="highlight"></style>
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 30% zadanych obrażeń HP (maks. 10)\n[WhenUse] Moc Monet +1 za każde 6 [Laceration] na celu (maks. 2)\n[BeforeAttack] Zyskuje Wagę ataku +1 za każde 10 [BloodArmorPersonalityFirst] (maks. 2)\n[EndSkill] Zużywa 10 [BloodArmorPersonalityFirst] za każdą zwiększoną Wagę ataku<style="highlight"></style>
332. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] [BloodDinner_Common_Accumulation] 100당 피해량 +<style="highlight">15</style>% (최대 <style="highlight">75</style>%)
   źródło: Skills_personality-03.json :: dataList[id=1031006].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BloodDinner_Common_Accumulation]
   znaczenie tagów: [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared)
   EN: Deal +<style="highlight">15</style>% damage for every 100 [BloodDinner_Common_Accumulation] (max <style="highlight">75</style>%)
   PL: Zadaje +<style="highlight">15</style>% obrażeń za każde 100 [BloodDinner_Common_Accumulation] (maks. <style="highlight">75</style>%)
333. [Umiejętność 6 (×0) (ulepszenia 3–4) — nazwa] 산초류 경혈 오의 - 라 샹그레
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].name ; dataList[id=1031007].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 5 · monety: 4 (+5)
   limit: do 60 znaków
   EN: Ascendant Sancho Hardblood Arts - La Sangre
   PL: Najwyższy Sancho Twardokrwisty Styl - La Sangre
334. [Umiejętność 6 (×0) (ulepszenie 3) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 20 회복)\n[WhenUse] 자신의 [BloodArmorPersonalityFirst] 10 당, 기본 위력 +1 (최대 2)\n[WhenUse] 대상의 [Laceration] 10 이상이면, 코인 위력 +1\n대상의 [Laceration]당 피해량 +5% (최대 50%)\n[WhenUse] [BloodDinner_Common_Accumulation] 100당 피해량 +20% (최대 100%)\n[EndSkill] [BloodArmorPersonalityFirst] 10 당, [BloodArmorPersonalityFirst] 10 소모\n[EndSkill] 대상이 사망했으면 [BloodDinner] 50 증가. 이 스킬에서 소모한 [BloodArmorPersonalityFirst]을 절반 돌려 받음 (턴 당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodArmorPersonalityFirst], [Laceration], [BloodDinner_Common_Accumulation], [EndSkill], [BloodDinner]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [EndSkill] = [공격 종료시] / [Attack End]; [BloodDinner] = 혈찬 / Bloodfeast
   EN: On Hit with this Skill: heal 50% of the HP damage dealt (max 20)\n[WhenUse] Base Power +1 for every 10 [BloodArmorPersonalityFirst] on self (max 2)\n[WhenUse] If target has 10+ [Laceration], Coin Power +1\nDeal +5% damage for every [Laceration] on target (max 50%)\n[WhenUse] Deal +20% damage for every 100 [BloodDinner_Common_Accumulation] (max 100%)\n[EndSkill] Consume 10 [BloodArmorPersonalityFirst] for every 10 [BloodArmorPersonalityFirst]\n[EndSkill] If target is defeated, increase [BloodDinner] by 50. Regain half of [BloodArmorPersonalityFirst] consumed by this Skill (once per turn)
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 50% zadanych obrażeń HP (maks. 20)\n[WhenUse] Moc Bazowa +1 za każde 10 [BloodArmorPersonalityFirst] (maks. 2)\n[WhenUse] Jeżeli cel ma 10+ [Laceration], Moc Monet +1\nZadaje +5% obrażeń za każde 1 [Laceration] na celu (maks. 50%)\n[WhenUse] Zadaje +20% obrażeń za każde 100 [BloodDinner_Common_Accumulation] (maks. 100%)\n[EndSkill] Zużywa 10 [BloodArmorPersonalityFirst] za każde 10 [BloodArmorPersonalityFirst]\n[EndSkill] Jeżeli cel ginie, zwiększa [BloodDinner] o 50 i odzyskuje połowę [BloodArmorPersonalityFirst] zużytych przez tę Umiejętność (1 raz na turę)
335. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1031007].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1031007].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1031007].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1031007].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 4 증가
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and +4 [Laceration] Count
   PL: [OnSucceedAttack] Nakłada 4 [Laceration] i zwiększa Licznik [Laceration] o 4
340. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 4, efekt 3 — opis] [EndSkill] 대상이 사망했으면, 모든 적에게 [Laceration] 5 부여, [Laceration] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=3].coinlist[#3].coindescs[#2].desc ; dataList[id=1031007].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [Laceration]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [Laceration] = 출혈 / Bleed
   EN: [EndSkill] If target is defeated, inflict 5 [Laceration] and +1 [Laceration] Count against all enemies
   PL: [EndSkill] Jeżeli cel ginie, nakłada 5 [Laceration] i zwiększa Licznik [Laceration] o 1 na wszystkich wrogach
341. [Umiejętność 6 (×0) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (최대 20 회복)\n[WhenUse] 자신의 [BloodArmorPersonalityFirst] 10 당 기본 위력 +1 (최대 <style="highlight">3</style>)\n[WhenUse] 대상의 [Laceration] <style="highlight">5 당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n대상의 [Laceration]당 피해량 +5% (최대 50%)\n[WhenUse] [BloodDinner_Common_Accumulation] 100당 피해량 +20% (최대 100%)\n[EndSkill] [BloodArmorPersonalityFirst] 10 당, [BloodArmorPersonalityFirst] 10 소모\n[EndSkill] 대상이 사망했으면 [BloodDinner] <style="highlight">100</style> 증가. 이 스킬에서 소모한 [BloodArmorPersonalityFirst]을 절반 돌려 받음 (턴 당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=4].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodArmorPersonalityFirst], [Laceration], [BloodDinner_Common_Accumulation], [EndSkill], [BloodDinner]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [EndSkill] = [공격 종료시] / [Attack End]; [BloodDinner] = 혈찬 / Bloodfeast
   EN: On Hit with this Skill: heal 50% of the HP damage dealt (max 20)\n[WhenUse] Base Power +1 for every 10 [BloodArmorPersonalityFirst] on self (max <style="highlight">3</style>)\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Laceration] on target (max 2)</style>\nDeal +5% damage for every [Laceration] on target (max 50%)\n[WhenUse] Deal +20% damage for every 100 [BloodDinner_Common_Accumulation] (max 100%)\n[EndSkill] Consume 10 [BloodArmorPersonalityFirst] for every 10 [BloodArmorPersonalityFirst]\n[EndSkill] If target is defeated, increase [BloodDinner] by <style="highlight">100</style>. Regain half of [BloodArmorPersonalityFirst] consumed by this Skill (once per turn)
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 50% zadanych obrażeń HP (maks. 20)\n[WhenUse] Moc Bazowa +1 za każde 10 [BloodArmorPersonalityFirst] (maks. <style="highlight">3</style>)\n[WhenUse] Moc Monet +1 za każde <style="highlight">5</style> [Laceration] celu <style="highlight">(maks. 2)</style>\nZadaje +5% obrażeń za każde 1 [Laceration] na celu (maks. 50%)\n[WhenUse] Zadaje +20% obrażeń za każde 100 [BloodDinner_Common_Accumulation] (maks. 100%)\n[EndSkill] Zużywa 10 [BloodArmorPersonalityFirst] za każde 10 [BloodArmorPersonalityFirst]\n[EndSkill] Jeżeli cel ginie, zwiększa [BloodDinner] o <style="highlight">100</style> i odzyskuje połowę [BloodArmorPersonalityFirst] zużytych przez tę Umiejętność (1 raz na turę)
342. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] <style="highlight">8</style> 부여, 출혈 횟수 4 증가
   źródło: Skills_personality-03.json :: dataList[id=1031007].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">8</style> [Laceration] and +4 [Laceration] Count
   PL: [OnSucceedAttack] Nakłada <style="highlight">8</style> [Laceration] i zwiększa Licznik [Laceration] o 4
343. [Obrona (ulepszenia 1,4) — nazwa] 웃음소리는 사그라들 것이다
   źródło: Skills_personality-03.json :: dataList[id=1031004].levelList[level=1].name ; dataList[id=1031004].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Laughters Shall Subside
   PL: Śmiech Ucichnie
344. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] [BloodDinner]을 최대 50 소모하여 [BloodDinner] 10 당 [BloodArmorPersonalityFirst] 1얻음.\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음\n[StartBattle] [BloodDinner_Common_Accumulation] 50 당 체력이 가장 적은 아군 1명에게 [SwirlingBloodPersonality] 1 부여 (최대 10, 턴 당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031004].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration], [BloodDinner_Common_Accumulation], [SwirlingBloodPersonality]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [SwirlingBloodPersonality] = 일렁임【혈귀】 / Shimmering【Bloodfiend】
   EN: [DuelCounter]\n[StartBattle] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner]\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]\n[StartBattle] To 1 ally with the least HP: apply 1 [SwirlingBloodPersonality] for every 50 [BloodDinner_Common_Accumulation] (max 10, once per turn)
   PL: [DuelCounter]\n[StartBattle] Zużywa do 50 [BloodDinner] i zyskuje 1 [BloodArmorPersonalityFirst] za każde 10 [BloodDinner]\n- Jeżeli nie udało się zużyć [BloodDinner], zyskuje 10 [Laceration]\n[StartBattle] Nakłada 1 [SwirlingBloodPersonality] na 1 Sojusznika z najmniejszym HP za każde 50 [BloodDinner_Common_Accumulation] (maks. 10, 1 raz na turę)
345. [Obrona (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031004].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1031004].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 2
346. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[StartBattle] [BloodDinner]을 최대 50 소모하여 [BloodDinner] 10 당 [BloodArmorPersonalityFirst] 1얻음.\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음\n[StartBattle] [BloodDinner_Common_Accumulation] 50 당 체력이 가장 적은 아군 1명에게 [SwirlingBloodPersonality] 1 부여 (최대 <style="highlight">15</style>, 턴 당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031004].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [BloodDinner], [BloodArmorPersonalityFirst], [Laceration], [BloodDinner_Common_Accumulation], [SwirlingBloodPersonality]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [Laceration] = 출혈 / Bleed; [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [SwirlingBloodPersonality] = 일렁임【혈귀】 / Shimmering【Bloodfiend】
   EN: [DuelCounter]\n[StartBattle] Consume up to 50 [BloodDinner] and gain 1 [BloodArmorPersonalityFirst] for every 10 [BloodDinner]\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]\n[StartBattle] To 1 ally with the least HP: apply 1 [SwirlingBloodPersonality] for every 50 [BloodDinner_Common_Accumulation] (max <style="highlight">15</style>, once per turn)
   PL: [DuelCounter]\n[StartBattle] Zużywa do 50 [BloodDinner] i zyskuje 1 [BloodArmorPersonalityFirst] za każde 10 [BloodDinner]\n- Jeżeli nie udało się zużyć [BloodDinner], zyskuje 10 [Laceration]\n[StartBattle] Nakłada 1 [SwirlingBloodPersonality] na 1 Sojusznika z najmniejszym HP za każde 50 [BloodDinner_Common_Accumulation] (maks. <style="highlight">15</style>, 1 raz na turę)
347. [Obrona (ulepszenia 1,4) — nazwa] 아류 산초 경혈 15식 - 피날레 준비
   źródło: Skills_personality-03.json :: dataList[id=1031008].levelList[level=1].name ; dataList[id=1031008].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 6 · monety: 2 (+5)
   limit: do 70 znaków
   EN: Variant Sancho Hardblood Arts 15 - Buildup to Finale
   PL: Wariantowy Sancho Twardokrwisty Styl 15 - Przygotowanie Finału
348. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] 체력이 가장 적은 아군 (3 + 가장 높은 공명 수 / 2)명에게 [BloodDinner_Common_Accumulation] 40 당 [SwirlingBloodPersonality]를 (1 + [BloodArmorPersonalityFirst]/15)만큼 부여하고, 보유한 [BloodArmorPersonalityFirst] 절반 소모. (아군 1명당 최대 1회 부여, 소수점 버림)
   źródło: Skills_personality-03.json :: dataList[id=1031008].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [BloodDinner_Common_Accumulation], [SwirlingBloodPersonality], [BloodArmorPersonalityFirst]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [SwirlingBloodPersonality] = 일렁임【혈귀】 / Shimmering【Bloodfiend】; [BloodArmorPersonalityFirst] = 경혈 / Hardblood
   EN: [DuelCounter]\n[StartBattle] To (3 + (highest Reson. / 2)) allies with the least HP: apply (1 + ([BloodArmorPersonalityFirst] / 15)) [SwirlingBloodPersonality] for every 40 [BloodDinner_Common_Accumulation], then consume half of [BloodArmorPersonalityFirst] on self. (once per ally; rounded down)
   PL: [DuelCounter]\n[StartBattle] Nakłada (1 + [BloodArmorPersonalityFirst]/15) [SwirlingBloodPersonality] na (3 + najwyższy Rezonans / 2) Sojuszników z najmniejszym HP za każde 40 [BloodDinner_Common_Accumulation], po czym zużywa połowę własnego [BloodArmorPersonalityFirst]. (1 raz na sojusznika; zaokrąglone w dół)
349. [Obrona (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031008].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1031008].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Obrona (ulepszenia 1,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031008].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1031008].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 3
351. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[StartBattle] 체력이 가장 적은 아군 (3 + 가장 높은 공명 수 / 2)명에게 [BloodDinner_Common_Accumulation] 40 당 [SwirlingBloodPersonality]를 (1 + [BloodArmorPersonalityFirst]/<style="highlight">10</style>)만큼 부여하고, 보유한 [BloodArmorPersonalityFirst] 절반 소모. (아군 1명당 최대 1회 부여, 소수점 버림)
   źródło: Skills_personality-03.json :: dataList[id=1031008].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [BloodDinner_Common_Accumulation], [SwirlingBloodPersonality], [BloodArmorPersonalityFirst]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [BloodDinner_Common_Accumulation] = 공용 누적 소모 혈찬 / Bloodfeast Consumed (shared); [SwirlingBloodPersonality] = 일렁임【혈귀】 / Shimmering【Bloodfiend】; [BloodArmorPersonalityFirst] = 경혈 / Hardblood
   EN: [DuelCounter]\n[StartBattle] To (3 + (highest Reson. / 2)) allies with the least HP: apply (1 + ([BloodArmorPersonalityFirst] / <style="highlight">10</style>)) [SwirlingBloodPersonality] for every 40 [BloodDinner_Common_Accumulation], then consume half of [BloodArmorPersonalityFirst] on self. (once per ally; rounded down)
   PL: [DuelCounter]\n[StartBattle] Nakłada (1 + [BloodArmorPersonalityFirst]/<style="highlight">10</style>) [SwirlingBloodPersonality] na (3 + najwyższy Rezonans / 2) Sojuszników z najmniejszym HP za każde 40 [BloodDinner_Common_Accumulation], po czym zużywa połowę własnego [BloodArmorPersonalityFirst]. (1 raz na sojusznika; zaokrąglone w dół)
352. [Pasywka bojowa (od ulepszenia 1) — nazwa] 혈찬
   źródło: Passives.json :: dataList[id=1031001].name
   limit: do 40 znaków
   EN: Bloodfeast
   PL: Krwawa Uczta
353. [Pasywka bojowa (od ulepszenia 1) — opis] 이 캐릭터가 전투에 등장해 있거나, 등장할 리스트에 포함되어 있으면, 1턴부터 모든 캐릭터가 받은 [Laceration] 피해만큼 [BloodDinner]이 증가함.\n이 캐릭터가 전투에 등장할 때 전장에 흩뿌려진 잠재된 피가 더욱 크게 드러난다.\n\n[BloodDinner]을 소모할 때, <라만차랜드[TabExplain]> 소속 중에서 자신과 같은 권속이 있으면, 자신이 먼저 [BloodDinner]을 소모함.\n\n'아류 산초 경혈[TabExplain] 6식 - 채찍'를 사용하는 동안 출혈 피해로 체력이 1 미만이 되지 않음.
   źródło: Passives.json :: dataList[id=1031001].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner], [TabExplain]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: If this unit is on field, or is one of the units that can appear on this Stage, increase Bloodfeast value by the amount of [Laceration] damage collectively received by every unit.\nWhen this unit enters the field, the sleeping blood drenching the battlefield will fill the surface.\n\nWhen consuming [BloodDinner], if there are <La Manchaland[TabExplain]> Kindreds of the same generation as this unit, this unit takes precedence.\n\nWhen using 'Variant Sancho Hardblood[TabExplain] Arts 6 - Whip', HP cannot drop below 1 due to Bleed damage.
   PL: Jeżeli ta jednostka jest na polu albo jest jedną z jednostek, które mogą się pojawić na tej scenie, od 1 tury [BloodDinner] rośnie o sumę obrażeń [Laceration] otrzymanych przez wszystkie jednostki.\nGdy ta jednostka wchodzi na pole, uśpiona krwią przesiąkające pole bitwy wypełnia jego powierzchnię.\n\nGdy zużywa [BloodDinner], jeżeli wśród <La Manchaland[TabExplain]> jest Rodzeństwo tej samej generacji co ta jednostka, ta jednostka zużywa je jako pierwsza.\n\nPodczas używania „Wariantowego Sancho Twardokrwistego Stylu 6 - Bicz”[TabExplain] HP nie może spaść poniżej 1 od obrażeń Krwawienia.
354. [Pasywka bojowa (od ulepszenia 1) — nazwa] 아류 산초 경혈식
   źródło: Passives.json :: dataList[id=1031002].name
   limit: do 50 znaków
   EN: Variant Sancho Hardblood Arts
   PL: Wariantowy Sancho Twardokrwisty Styl
355. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 시작 시, [BloodArmorPersonalityFirst] 15 이상이고 다음의 인격이 전투에 참가 중이거나 사망했으면, 자신의 가장 왼쪽 슬롯의 스킬이 강화됨.\n- 라만차랜드[TabExplain] 신부 그레고르: 스킬 1 강화\n- 라만차랜드[TabExplain] 이발사 오티스: 스킬 2 강화\n- 자신: 스킬 3 강화\n- 라만차랜드[TabExplain] 공주 로쟈: 수비 스킬[TabExplain] 강화\n\n자신을 제외한 아군이 출혈 피해를 받거나 [BloodDinner]을 소모할 때, [BloodArmorPersonalityFirst] 2 얻음 (턴 당 3회)
   źródło: Passives.json :: dataList[id=1031002].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n, [BloodArmorPersonalityFirst], [TabExplain], [BloodDinner], [Laceration]
   znaczenie tagów: [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed
   EN: Turn Start: At 15+ [BloodArmorPersonalityFirst], if each following unit is either defeated or participating in the Encounter, empower this unit's leftmost Slot.\nThe Priest of La Manchaland[TabExplain] Gregor: Empower Skill 1\nThe Barber of La Manchaland[TabExplain] Outis: Empower Skill 2\nThis Unit: Empower Skill 3\nThe Princess of La Manchaland[TabExplain] Rodion: Empower Defense Skill[TabExplain]\n\nWhen other units among allies take [Laceration] damage or consume [BloodDinner], gain 2 [BloodArmorPersonalityFirst] on self (3 times per turn)
   PL: Na początku tury, przy 15+ [BloodArmorPersonalityFirst], jeżeli każdy z poniższych jest pokonany albo uczestniczy w walce, umiejętność w skrajnie lewym slocie tej jednostki zostaje wzmocniona.\n- Ksiądz La Manchaland[TabExplain] Gregor: wzmacnia Umiejętność 1\n- Fryzjer La Manchaland[TabExplain] Outis: wzmacnia Umiejętność 2\n- Ta jednostka: wzmacnia Umiejętność 3\n- Księżniczka La Manchaland[TabExplain] Rodion: wzmacnia Umiejętność obrony[TabExplain]\n\nGdy inni sojusznicy otrzymają obrażenia [Laceration] albo zużyją [BloodDinner], zyskuje 2 [BloodArmorPersonalityFirst] (3 razy na turę)
356. [Pasywka bojowa (od ulepszenia 1) — nazwa] 혈족을 책임지게 된 자
   źródło: Passives.json :: dataList[id=1031003].name
   limit: do 40 znaków
   EN: Bearer of the Blood Kin
   PL: Stróż Rodziny Krwi
357. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 동안 자신을 제외한 아군 중 <라만차랜드[TabExplain]> 소속이 사망한 경우\n- 자신의 기본 공격 스킬로 [BloodArmorPersonalityFirst]을 얻을 때, [BloodArmorPersonalityFirst]을 1 추가로 얻음\n- 자신을 제외한 아군 중 <라만차랜드[TabExplain]> 소속이 3명 이상 사망한 경우, 대신 [BloodArmorPersonalityFirst] 3을 추가로 얻고 턴 시작 시, [SadLamanchaland] 1 얻음
   źródło: Passives.json :: dataList[id=1031003].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain], [BloodArmorPersonalityFirst], [SadLamanchaland]
   znaczenie tagów: [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [SadLamanchaland] = 책임감 / Responsibility
   EN: In an Encounter, if another allied <La Manchaland[TabExplain]> unit is defeated:\n- Gain 1 more [BloodArmorPersonalityFirst] when gaining [BloodArmorPersonalityFirst] from this unit's Base Attack Skills\n- When 3+ other allied <La Manchaland[TabExplain]> units are defeated: gain 3 additional [BloodArmorPersonalityFirst]; at Turn Start, gain 1 [SadLamanchaland]
   PL: Podczas walki, jeżeli pokonano innego sojusznika <La Manchaland[TabExplain]>:\n- Zyskuje o 1 więcej [BloodArmorPersonalityFirst], gdy zyskuje [BloodArmorPersonalityFirst] od własnych podstawowych Umiejętności ataku\n- Jeżeli pokonano 3 lub więcej innych sojuszników <La Manchaland[TabExplain]>, zamiast tego zyskuje dodatkowo 3 [BloodArmorPersonalityFirst], a na początku tury zyskuje 1 [SadLamanchaland]
358. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — nazwa] 혈갑
   źródło: Passives.json :: dataList[id=1031004].name
   limit: do 40 znaków
   EN: Armadura de Sangre
   PL: Armadura de Sangre
359. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — opis] 자신의 공격 종료 시 적이 사망했다면, 대상의 최대 체력 10%만큼 [BloodDinner] 생성 (턴 당 최대 100, 집중 전투인 경우 부위로 판정)\n턴 종료 시 잃은 체력 15%당 다음 턴에 [AttackDmgUp] 1 얻음. (최대 3)\n전투 중 아군이 출혈 피해로 사망하려 할 때, 해당 턴동안 출혈 피해로는 사망하지 않음. (전투 당 인격 1명당 1회 발동)
   źródło: Passives.json :: dataList[id=1031004].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [AttackDmgUp], [Laceration]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [AttackDmgUp] = 피해량 증가 / Damage Up; [Laceration] = 출혈 / Bleed
   EN: Attack End: If the enemy is defeated, increase [BloodDinner] by 10% of the target's max HP (100 per turn; for Focused Encounters, if the Part is broken)\nGain 1 [AttackDmgUp] next turn for every 15% missing HP at Turn End (max 3)\nIf an ally is about to be defeated from [Laceration] damage, prevent them from being defeated from Bleed damage for the turn (once per Encounter for each Identity)
   PL: Na koniec ataku tej jednostki, jeżeli wróg ginie, tworzy [BloodDinner] równe 10% Maks. HP celu (maks. 100 na turę; w walce skupionej liczy się rozbicie części ciała)\nNa koniec tury zyskuje w następnej turze 1 [AttackDmgUp] za każde 15% brakującego HP. (maks. 3)\nGdy sojusznik ma zginąć od obrażeń Krwawienia podczas walki, w tej turze nie zginie od obrażeń Krwawienia. (1 raz na spotkanie na każdą Tożsamość)
360. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — nazwa] ‘가족들이여 억눌러온 허기를 채워라’
   źródło: Passives.json :: dataList[id=1031021].name
   limit: do 60 znaków
   EN: ‘Feed your repressed hunger, my Family’
   PL: „Nakarmcie stłumiony głód, moja Rodzino”
361. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — opis] 전투 시작 시 체력이 가장 적은 아군이 잃은 체력 20%당 [AttackDmgUp] 1 얻음. (최대 3)\n- 대상 아군이 <혈귀>면, 효과를 대신하여 잃은 체력 15%당 [AttackDmgUp] 1 얻음. (최대 3)
   źródło: Passives.json :: dataList[id=1031021].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Combat Start: 1 ally with the least HP gains 1 [AttackDmgUp] for every 20% missing HP (max 3)\n- If the said ally is a <Bloodfiend>, gain 1 [AttackDmgUp] for every 15% missing HP instead (max 3)
   PL: Na początku walki 1 Sojusznik z najmniejszym HP zyskuje 1 [AttackDmgUp] za każde 20% brakującego HP. (maks. 3)\n- Jeżeli tym sojusznikiem jest <Wampir>, zamiast tego zyskuje 1 [AttackDmgUp] za każde 15% brakującego HP. (maks. 3)

## [000] Cinq Assoc. East Section 3 — Don Quixote — 동부 섕크 협회 3과
- ID Tożsamości: `10311` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: — · HP bazowe: 82 · szybkość: 2–5 / 3–7 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Poise, Burn

362. [Karta Tożsamości — tytuł] 동부 섕크 협회\n3과
   źródło: Personalities.json :: dataList[id=10311].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cinq Assoc.\nEast Section 3
   PL: Wschodnie Stowarzyszenie Cinq\nSekcja 3
363. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10311].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10311].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
365. [Karta Tożsamości — opis] 돈키호테의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10311].desc
   limit: do 120 znaków
   EN: Don Quixote's 11th Identity
   PL: Jedenasta Tożsamość Don Quixote
366. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 발경
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=1].name ; dataList[id=1031101].levelList[level=2].name ; dataList[id=1031101].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Fa Jin
   PL: Jin
367. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 자신의 속도가 대상보다 3 이상 높으면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by 3 or more, Coin Power +1\n[WhenUse] Gain +2 [Breath] Count
   PL: Jeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, Moc Monet +1\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
368. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Inflict 1 [Combustion]
   PL: [OnSucceedAttackHead] Nakłada 1 [Combustion]
369. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 자신의 속도가 대상보다 <style="highlight">2</style> 이상 높으면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by <style="highlight">2</style> or more, Coin Power +1\n[WhenUse] Gain +2 [Breath] Count
   PL: Jeżeli Szybkość tej jednostki jest większa od celu o <style="highlight">2</style> lub więcej, Moc Monet +1\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
371. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack]</style> [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[OnSucceedAttack]</style> Inflict 1 [Combustion]
   PL: <style="highlight">[OnSucceedAttack]</style> Nakłada 1 [Combustion]
372. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack]</style> [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 371 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2당 코인 위력 +1. 최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: <style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)</style>\n[WhenUse] Gain +<style="highlight">3</style> [Breath] Count
   PL: <style="highlight">Zyskuje Moc Monet zależnie od przewagi Szybkości (Moc Monet +1 za każde 2 różnicy Szybkości; maks. 2)</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o <style="highlight">3</style>
374. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]<style="highlight"></style>
375. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 374 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] [Combustion] 횟수 1 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1031101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Combustion]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict +1 [Combustion] Count</style>
   PL: <style="highlight">[CriticalOnSucceedAttack] Zwiększa Licznik [Combustion] o 1</style>
377. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 초염장
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=1].name ; dataList[id=1031102].levelList[level=2].name ; dataList[id=1031102].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Virescent Flame Palm
   PL: Wierzbowa Dłoń Płomienia
378. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 자신의 속도가 대상보다 3 이상 높으면, 코인 위력 +1\n[WinDuel] [Breath] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by 3 or more, Coin Power +1\n[WinDuel] Gain 3 [Breath]
   PL: Jeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, Moc Monet +1\n[WinDuel] Zyskuje 3 [Breath]
379. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain +2 [Breath] Count
   PL: [OnSucceedAttackHead] Zwiększa własny Licznik [Breath] o 2
380. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL: [OnSucceedAttack] Nakłada 2 [Combustion]
382. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion] 6당 [DefenseDown] 1 부여 (최대 2, 턴당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown] for every 6 [Combustion] on target (max 2, once per turn)
   PL: [OnSucceedAttack] Nakłada 1 [DefenseDown] za każde 6 [Combustion] na celu (maks. 2, 1 raz na turę)
383. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 자신의 속도가 대상보다 <style="highlight">2</style> 이상 높으면, 코인 위력 +1\n[WinDuel] [Breath] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by <style="highlight">2</style> or more, Coin Power +1\n[WinDuel] Gain 3 [Breath]
   PL: Jeżeli Szybkość tej jednostki jest większa od celu o <style="highlight">2</style> lub więcej, Moc Monet +1\n[WinDuel] Zyskuje 3 [Breath]
384. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack]</style> 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: <style="highlight">[OnSucceedAttack]</style> Gain +2 [Breath] Count
   PL: <style="highlight">[OnSucceedAttack]</style> Zwiększa własny Licznik [Breath] o 2
385. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack]</style> [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 371 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1031102].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Combustion]<style="highlight"></style>
387. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion] 6당 [DefenseDown] 1 부여 (최대 <style="highlight">3</style>, 턴당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown] for every 6 [Combustion] on target (max <style="highlight">3</style>, once per turn)
   PL: [OnSucceedAttack] Nakłada 1 [DefenseDown] za każde 6 [Combustion] na celu (maks. <style="highlight">3</style>, 1 raz na turę)
388. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2당 코인 위력 +1. 최대 2)</style>\n[WinDuel] [Breath] 3 얻음\n<style="highlight">- 대상의 [DianxueDonQuixote]만큼 추가로 [Breath] 횟수 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=4].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WinDuel], [Breath], [DianxueDonQuixote]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote
   EN: <style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)</style>\n[WinDuel] Gain 3 [Breath]\n<style="highlight">- Gain additional [Breath] Count equal to [DianxueDonQuixote] on target</style>
   PL: <style="highlight">Zyskuje Moc Monet zależnie od przewagi Szybkości (Moc Monet +1 za każde 2 różnicy Szybkości; maks. 2)</style>\n[WinDuel] Zyskuje 3 [Breath]\n<style="highlight">- Zwiększa Licznik [Breath] dodatkowo o wartość [DianxueDonQuixote] celu</style>
389. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Breath] o 2<style="highlight"></style>
390. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Combustion]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Combustion]
391. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion] 6당 [DefenseDown] 1 부여 (최대 <style="highlight">5</style>, 턴당 1회)\n<style="highlight">- 대상의 [DianxueDonQuixote]만큼 [DefenseDown] 추가로 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1031102].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Combustion], [DefenseDown], [DianxueDonQuixote]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown] for every 6 [Combustion] on target (max <style="highlight">5</style>, once per turn)\n<style="highlight">- Inflict additional [DefenseDown] equal to [DianxueDonQuixote] on target</style>
   PL: [OnSucceedAttack] Nakłada 1 [DefenseDown] za każde 6 [Combustion] na celu (maks. <style="highlight">5</style>, 1 raz na turę)\n<style="highlight">- Nakłada dodatkowo [DefenseDown] równy [DianxueDonQuixote] celu</style>
392. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 한 수 부탁드리겠네
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=3].name ; dataList[id=1031103].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 4 (+3)
   limit: do 60 znaków
   EN: Prithee, let this be an enlightening bout
   PL: Proszę o pouczające starcie
393. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [DianxueDonQuixote] 1당 피해량 +10% (최대 30%)\n자신의 속도가 대상보다 2 이상 높으면, 코인 위력 +1\n[WinDuel] [Breath] 5 얻음\n- 대상에게 [DianxueDonQuixote]가 있으면 추가로 [Breath] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=3].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [DianxueDonQuixote], [WinDuel], [Breath]
   znaczenie tagów: [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: Deal +10% damage for every 1 [DianxueDonQuixote] on target (max 30%)\nIf this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[WinDuel] Gain 5 [Breath]\n- If target has [DianxueDonQuixote], gain 3 additional [Breath]
   PL: Zadaje +10% obrażeń za każde 1 [DianxueDonQuixote] na celu (maks. 30%)\nJeżeli Szybkość tej jednostki jest większa od celu o 2 lub więcej, Moc Monet +1\n[WinDuel] Zyskuje 5 [Breath]\n- Jeżeli cel ma [DianxueDonQuixote], zyskuje dodatkowo 3 [Breath]
394. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]
395. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] 크리티컬 피해량 +(자신의 [Breath] + 대상의 [Combustion])% (최대 30%)
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath], [Combustion]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn
   EN: Deal +([Breath] on self + [Combustion] on target)% damage on Critical Hit (max 30%)
   PL: Zadaje +(własna [Breath] + [Combustion] celu)% obrażeń przy trafieniu krytycznym (maks. 30%)
398. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [DianxueDonQuixote] 1당 피해량 <style="highlight">+15%</style> (최대 <style="highlight">45%</style>)\n<style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2당 코인 위력 +1. 최대 2)</style>\n[WinDuel] [Breath] 5 얻음\n- 대상에게 [DianxueDonQuixote]가 있으면 추가로 [Breath] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DianxueDonQuixote], [WinDuel], [Breath]
   znaczenie tagów: [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: Deal <style="highlight">+15%</style> damage for every 1 [DianxueDonQuixote] on target (max <style="highlight">45%</style>)\n<style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)</style>\n[WinDuel] Gain 5 [Breath]\n- If target has [DianxueDonQuixote], gain 3 additional [Breath]
   PL: Zadaje <style="highlight">+15%</style> obrażeń za każde 1 [DianxueDonQuixote] na celu (maks. <style="highlight">45%</style>)\n<style="highlight">Zyskuje Moc Monet zależnie od przewagi Szybkości (Moc Monet +1 za każde 2 różnicy Szybkości; maks. 2)</style>\n[WinDuel] Zyskuje 5 [Breath]\n- Jeżeli cel ma [DianxueDonQuixote], zyskuje dodatkowo 3 [Breath]
399. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 374 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 374 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] 크리티컬 피해량 +(자신의 [Breath] + 대상의 [Combustion])% (최대 <style="highlight">50%</style>)
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Breath], [Combustion]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn
   EN: Deal +([Breath] on self + [Combustion] on target)% damage on Critical Hit (max <style="highlight">50%</style>)
   PL: Zadaje +(własna [Breath] + [Combustion] celu)% obrażeń przy trafieniu krytycznym (maks. <style="highlight">50%</style>)
403. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 대상에게 [DianxueDonQuixote]가 있으면 [DefenseDown] 3 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1031103].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DianxueDonQuixote], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: <style="highlight">[OnSucceedAttack] If target has [DianxueDonQuixote], inflict 3 [DefenseDown]</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli cel ma [DianxueDonQuixote], nakłada 3 [DefenseDown]</style>
404. [Obrona (ulepszenia 1,4) — nazwa] 밥상머리 예절부터 배우시게!
   źródło: Skills_personality-03.json :: dataList[id=1031104].levelList[level=1].name ; dataList[id=1031104].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 70 znaków
   EN: Thou'rt in dire need of a lesson in table manners!
   PL: Potrzebujesz pilnej lekcji savoir-vivre'u!
405. [Obrona (ulepszenie 4) — opis] <style="highlight">자신의 속도가 공격자보다 높으면, 속도 차이 2당 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-03.json :: dataList[id=1031104].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">If this unit's Speed is faster than the target's, gain +1 Coin Power for every 2 Speed difference (max 2)</style>
   PL: <style="highlight">Jeżeli Szybkość tej jednostki jest większa niż atakującego, Moc Monet +1 za każde 2 różnicy Szybkości (maks. 2)</style>
406. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Wrath, posiadane 2× Pride) — nazwa] 초염옥구
   źródło: Passives.json :: dataList[id=1031101].name
   limit: do 40 znaków
   EN: Virescent Pyrojade
   PL: Wierzbowy Jadeit Piro
407. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Wrath, posiadane 2× Pride) — opis] 턴 종료 시 자신의 [Breath] 위력 5당, 다음 턴에 [Agility] 1 얻음 (최대 2)\n\n기본 공격 스킬로 마지막에 적중한 대상(또는 부위)에게 다음 턴에 [DianxueDonQuixote] 부여 (턴당 1회)\n\n크리티컬 피해량 +(대상의 [Combustion] 위력)% (최대 15%)
   źródło: Passives.json :: dataList[id=1031101].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Agility], [DianxueDonQuixote], [Combustion]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote; [Combustion] = 화상 / Burn
   EN: Turn End: gain 1 [Agility] next turn for every 5 [Breath] Potency on self (max 2)\n\nAgainst the target(or the Part) a Base Attack Skill hit last, inflict [DianxueDonQuixote] next turn (once per turn)\n\nDeal +([Combustion] Potency on the target)% damage on Critical Hit (max 15%)
   PL: Na koniec tury zyskuje w następnej turze 1 [Agility] za każde 5 Mocy [Breath] (maks. 2)\n\nNakłada w następnej turze [DianxueDonQuixote] na cel (lub część ciała), który został trafiony ostatni podstawową Umiejętnością ataku (1 raz na turę)\n\nZadaje +(Moc [Combustion] celu)% obrażeń przy trafieniu krytycznym (maks. 15%)
408. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Wrath, posiadane 2× Pride) — nazwa] 초염옥구
   źródło: Passives.json :: dataList[id=1031111].name
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Wrath, posiadane 2× Pride) — opis] 턴 종료 시 자신의 [Breath] 위력 <style="highlight">3</style>당, 다음 턴에 [Agility] 1 얻음 (최대 2)\n\n기본 공격 스킬로 마지막에 적중한 대상(또는 부위)에게 다음 턴에 [DianxueDonQuixote] 부여 (턴당 1회)\n\n크리티컬 피해량 +(대상의 [Combustion] 위력)% (최대 15%)\n<style="highlight">- 대상의 [DianxueDonQuixote] 1당 최댓값 5% 증가</style>
   źródło: Passives.json :: dataList[id=1031111].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [Agility], [DianxueDonQuixote], [Combustion]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [DianxueDonQuixote] = 점혈 - 돈키호테 / Nerve Strike - Don Quixote; [Combustion] = 화상 / Burn
   EN: Turn End: gain 1 [Agility] next turn for every <style="highlight">3</style> [Breath] Potency on self (max 2)\n\nAgainst the target(or the Part) a Base Attack Skill hit last, inflict [DianxueDonQuixote] next turn (once per turn)\n\nDeal +([Combustion] Potency on the target)% damage on Critical Hit (max 15%)\n<style="highlight">- Increase max cap by 5% for every 1 [DianxueDonQuixote] on the target</style>
   PL: Na koniec tury zyskuje w następnej turze 1 [Agility] za każde <style="highlight">3</style> Mocy [Breath] (maks. 2)\n\nNakłada w następnej turze [DianxueDonQuixote] na cel (lub część ciała), który został trafiony ostatni podstawową Umiejętnością ataku (1 raz na turę)\n\nZadaje +(Moc [Combustion] celu)% obrażeń przy trafieniu krytycznym (maks. 15%)\n<style="highlight">- Zwiększa maksimum o 5% za każde 1 [DianxueDonQuixote] celu</style>
410. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 경신법
   źródło: Passives.json :: dataList[id=1031121].name
   limit: do 40 znaków
   EN: Featherstride Technique
   PL: Technika Piórkowego Kroku
411. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 속도가 가장 빠른 아군 1명이 [Combustion] 또는 특수 화상을 보유한 적에게 합 승리 시, 다음 턴에 [Agility] 1을 얻음 (턴당 1회)
   źródło: Passives.json :: dataList[id=1031121].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Agility]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Agility] = 신속 / Haste
   EN: 1 ally with the fastest Speed : On Clash Win against enemies with [Combustion] or 'Unique Burn', gain 1 [Agility] next turn (once per turn)
   PL: 1 Sojusznik z najwyższą Szybkością: po wygranym Starciu z wrogiem mającym [Combustion] lub Specjalne Podpalenie, zyskuje w następnej turze 1 [Agility] (1 raz na turę)
412. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Wrath) — nazwa] 경신법
   źródło: Passives.json :: dataList[id=1031131].name
   (powtórzenie elementu 410 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Wrath) — opis] 속도가 가장 빠른 아군 1명이 [Combustion] 또는 특수 화상을 보유한 적에게 합 승리 시, 다음 턴에 [Agility] 1을 얻음 (턴당 1회)\n<style="highlight">- 대상의 [Combustion] 위력이 20 이상이면, 신속 1을 추가로 얻음</style>
   źródło: Passives.json :: dataList[id=1031131].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [Agility]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Agility] = 신속 / Haste
   EN: 1 ally with the fastest Speed : On Clash Win against enemies with [Combustion] or 'Unique Burn', gain 1 [Agility] next turn (once per turn)\n<style="highlight">- If the target has 20+ [Combustion] Potency, gain 1 additional [Agility]</style>
   PL: 1 Sojusznik z najwyższą Szybkością: po wygranym Starciu z wrogiem mającym [Combustion] lub Specjalne Podpalenie, zyskuje w następnej turze 1 [Agility] (1 raz na turę)\n<style="highlight">- Jeżeli cel ma 20+ Mocy [Combustion], zyskuje dodatkowo 1 [Agility]</style>

## [000] Lobotomy E.G.O:: In the Name of Love and Hate — Don Quixote — 로보토미 E.G.O:: 사랑과 증오의 이름으로
- ID Tożsamości: `10312` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9106 · HP bazowe: 69 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Charge, Rupture, Sinking

414. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n사랑과 증오의 이름으로
   źródło: Personalities.json :: dataList[id=10312].title
   limit: do 70 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::\nIn the Name of\nLove and Hate
   PL: Lobotomy E.G.O::\nW Imię\nMiłości i Nienawiści
415. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10312].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10312].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Karta Tożsamości — opis] 돈키호테의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10312].desc
   limit: do 120 znaków
   EN: Don Quixote's 12th Identity
   PL: Dwunasta Tożsamość Don Quixote
418. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 관리자 나리의 명에 따라 등장!
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=1].name ; dataList[id=1031201].levelList[level=2].name ; dataList[id=1031201].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 60 znaków
   EN: By Manager Esquire's Orders, I Am Here!
   PL: Rozkazem Zarządcy Wsassp, stawiam się!
419. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [WhenUse] Gain +2 [ThePowerOfLoveAndHate] Count
   PL: [WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 2
420. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +2 [ThePowerOfLoveAndHate] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 2
421. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 5 소모하여, 코인 위력 +1</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: <style="highlight">[WhenUse] Consume 5 [ThePowerOfLoveAndHate] Count on self to gain Coin Power +1</style>\n[WhenUse] Gain +<style="highlight">3</style> [ThePowerOfLoveAndHate] Count
   PL: <style="highlight">[WhenUse] Zużywa 5 Licznika [ThePowerOfLoveAndHate], aby zyskać Moc Monet +1</style>\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o <style="highlight">3</style>
423. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +2 [ThePowerOfLoveAndHate] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 2<style="highlight"></style>
424. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Burst]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Burst]
425. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 5 소모하여, 코인 위력 +1\n<style="highlight">[WhenUse] 자신의 [ThePowerOfLoveAndHate] 2당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [WhenUse] Consume 5 [ThePowerOfLoveAndHate] Count on self to gain Coin Power +1\n<style="highlight">[WhenUse] Coin Power +1 for every 2 [ThePowerOfLoveAndHate] (max 2)</style>\n[WhenUse] Gain +3 [ThePowerOfLoveAndHate] Count
   PL: [WhenUse] Zużywa 5 Licznika [ThePowerOfLoveAndHate], aby zyskać Moc Monet +1\n<style="highlight">[WhenUse] Moc Monet +1 za każde 2 [ThePowerOfLoveAndHate] (maks. 2)</style>\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 3
426. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +<style="highlight">3</style> [ThePowerOfLoveAndHate] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o <style="highlight">3</style>
427. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] <style="highlight">3</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Burst]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Burst]
428. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 사랑으로! 욥!
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=1].name ; dataList[id=1031202].levelList[level=2].name ; dataList[id=1031202].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 6 · monety: 2 (+5)
   limit: do 40 znaków
   EN: With Love! Hyah!
   PL: Z Miłością! Hyah!
429. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [WhenUse] Gain +3 [ThePowerOfLoveAndHate] Count
   PL: [WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 3
430. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +3 [ThePowerOfLoveAndHate] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 3
431. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">자신의 [ThePowerOfLoveAndHate]당 피해량 +7.5% (최대 30%)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 6 소모하여, 코인 위력 +1</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=2].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ThePowerOfLoveAndHate], [WhenUse]
   znaczenie tagów: [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">Deal +7.5% damage for every [ThePowerOfLoveAndHate] on self (max 30%)\n[WhenUse] Consume 6 [ThePowerOfLoveAndHate] Count on self to gain Coin Power +1</style>\n[WhenUse] Gain +3 [ThePowerOfLoveAndHate] Count
   PL: <style="highlight">Zadaje +7.5% obrażeń za każde 1 [ThePowerOfLoveAndHate] (maks. 30%)\n[WhenUse] Zużywa 6 Licznika [ThePowerOfLoveAndHate], aby zyskać Moc Monet +1</style>\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 3
433. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +<style="highlight">4</style> [ThePowerOfLoveAndHate] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o <style="highlight">4</style>
434. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] 다음 턴에 메인 타겟에게 [VillainMark] 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [VillainMark]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [VillainMark] = 악당 표식 / Mark of Villainy
   EN: <style="highlight">[OnSucceedAttackHead] Inflict [VillainMark] against the main target next turn</style>
   PL: <style="highlight">[OnSucceedAttackHead] Nakłada w następnej turze [VillainMark] na główny cel</style>
436. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 [ThePowerOfLoveAndHate]당 피해량 +<style="highlight">12.5</style>% (최대 <style="highlight">75</style>%)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 6 소모하여, 코인 위력 +1\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">5</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ThePowerOfLoveAndHate], [WhenUse]
   znaczenie tagów: [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [WhenUse] = [사용시] / [On Use]
   EN: Deal +<style="highlight">12.5</style>% damage for every [ThePowerOfLoveAndHate] on self (max <style="highlight">75</style>%)\n[WhenUse] Consume 6 [ThePowerOfLoveAndHate] Count on self to gain Coin Power +1\n[WhenUse] Gain +<style="highlight">5</style> [ThePowerOfLoveAndHate] Count
   PL: Zadaje +<style="highlight">12.5</style>% obrażeń za każde 1 [ThePowerOfLoveAndHate] (maks. <style="highlight">75</style>%)\n[WhenUse] Zużywa 6 Licznika [ThePowerOfLoveAndHate], aby zyskać Moc Monet +1\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o <style="highlight">5</style>
437. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 4 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +4 [ThePowerOfLoveAndHate] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 4<style="highlight"></style>
438. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Burst]<style="highlight"></style>
439. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack]</style> 다음 턴에 메인 타겟에게 [VillainMark] 부여
   źródło: Skills_personality-03.json :: dataList[id=1031202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VillainMark]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VillainMark] = 악당 표식 / Mark of Villainy
   EN: <style="highlight">[OnSucceedAttack]</style> Inflict [VillainMark] against the main target next turn
   PL: <style="highlight">[OnSucceedAttack]</style> Nakłada w następnej turze [VillainMark] na główny cel
440. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 아르카나 비트!! / 마이너 아르카나 슬레이브!!!
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].name ; dataList[id=1031203].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 60 znaków
   EN: Arcana Beats!! / Minor Arcana Slave!!!
   PL: Uderzenia Arkan!! / Sługa Mniejszych Arkan!!!
441. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 [ArcanaQueenOfHate]당, 피해량 +15% (최대 45%)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate]가 2 이상이면, ([ThePowerOfLoveAndHate] X 20)%만큼 피해량이 증가 (최대 80%)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate]가 2 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 5씩 소모하여, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 6 증가\n[EndSkill] [ArcanaQueenOfHate] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [ArcanaQueenOfHate], [WhenUse], [ThePowerOfLoveAndHate], [EndSkill]
   znaczenie tagów: [ArcanaQueenOfHate] = 매지컬 아르카나 / Magical Arcana; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +15% damage for every [ArcanaQueenOfHate] on self (max 45%)\n[WhenUse] At 2+ [ThePowerOfLoveAndHate], deal +([ThePowerOfLoveAndHate] x 20)% damage (max 80%)\n[WhenUse] At 2+ [ThePowerOfLoveAndHate], Base Power +1\n[WhenUse] Consume [ThePowerOfLoveAndHate] Count to gain Coin Power (Coin Power +1 for every 5 Count consumed, max 2)\n[WhenUse] Gain +6 [ThePowerOfLoveAndHate] Count\n[EndSkill] Gain 1 [ArcanaQueenOfHate]
   PL: Zadaje +15% obrażeń za każde 1 [ArcanaQueenOfHate] (maks. 45%)\n[WhenUse] Przy 2+ [ThePowerOfLoveAndHate] zadaje ([ThePowerOfLoveAndHate] x 20)% więcej obrażeń (maks. 80%)\n[WhenUse] Przy 2+ [ThePowerOfLoveAndHate] Moc Bazowa +1\n[WhenUse] Zużywa po 5 Licznika [ThePowerOfLoveAndHate], aby zyskać Moc Monet +1 (maks. 2)\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 6\n[EndSkill] Zyskuje 1 [ArcanaQueenOfHate]
442. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1031203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1031203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1031203].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Burst]
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada 2 [Burst]
445. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1031203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1031203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 [ArcanaQueenOfHate]당 피해량 +<style="highlight">30</style>% (최대 <style="highlight">90</style>%)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate]가 2 이상이면, ([ThePowerOfLoveAndHate] X <style="highlight">25</style>)%만큼 피해량이 증가 <style="highlight">(최대 125%)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate]가 2 이상이면, 기본 위력 +<style="highlight">2</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 5씩 소모하여, 코인 위력 +1 <style="highlight">(최대 4)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 6 증가\n[EndSkill] [ArcanaQueenOfHate] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031203].levelList[level=4].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ArcanaQueenOfHate], [WhenUse], [ThePowerOfLoveAndHate], [EndSkill]
   znaczenie tagów: [ArcanaQueenOfHate] = 매지컬 아르카나 / Magical Arcana; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +<style="highlight">30</style>% damage for every [ArcanaQueenOfHate] on self (max <style="highlight">90</style>%)\n[WhenUse] At 2+ [ThePowerOfLoveAndHate], deal +([ThePowerOfLoveAndHate] x <style="highlight">25</style>)% damage <style="highlight">(max 125%)</style>\n[WhenUse] At 2+ [ThePowerOfLoveAndHate], Base Power +<style="highlight">2</style>\n[WhenUse] Consume [ThePowerOfLoveAndHate] Count to gain Coin Power (Coin Power +1 for every 5 Count consumed, max <style="highlight">4</style>)\n[WhenUse] Gain +6 [ThePowerOfLoveAndHate] Count\n[EndSkill] Gain 1 [ArcanaQueenOfHate]
   PL: Zadaje +<style="highlight">30</style>% obrażeń za każde 1 [ArcanaQueenOfHate] (maks. <style="highlight">90</style>%)\n[WhenUse] Przy 2+ [ThePowerOfLoveAndHate] zadaje ([ThePowerOfLoveAndHate] x <style="highlight">25</style>)% więcej obrażeń <style="highlight">(maks. 125%)</style>\n[WhenUse] Przy 2+ [ThePowerOfLoveAndHate] Moc Bazowa +<style="highlight">2</style>\n[WhenUse] Zużywa po 5 Licznika [ThePowerOfLoveAndHate], aby zyskać Moc Monet +1 <style="highlight">(maks. 4)</style>\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 6\n[EndSkill] Zyskuje 1 [ArcanaQueenOfHate]
448. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — nazwa] 악당은... 어디있어....?
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=1].name ; dataList[id=1031205].levelList[level=2].name ; dataList[id=1031205].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 12 · monety: 2 (−4)
   limit: do 50 znaków
   EN: Where are... the villains...?
   PL: Gdzie są... łotrzy...?
449. [Umiejętność 4 (×0) (ulepszenie 1) — opis] 자신의 [HystericGauge]당 피해량 +3% (최대 9%)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가\n[WhenUse] 정신력 5 감소
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [HystericGauge], [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [HystericGauge] = 히스테리 / Hysteria; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: Deal +3% damage for every [HystericGauge] on self (max 9%)\n[WhenUse] Gain +2 [ThePowerOfLoveAndHate] Count\n[WhenUse] Lose 5 SP
   PL: Zadaje +3% obrażeń za każde 1 [HystericGauge] (maks. 9%)\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 2\n[WhenUse] Traci 5 Poczytalności
450. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] Nakłada 1 [Sinking]
452. [Umiejętność 4 (×0) (ulepszenie 2) — opis] 자신의 [HystericGauge]당 피해량 <style="highlight">+4% (최대 12%)</style>\n<style="highlight">[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 5 소모하여, 기본 위력 +1</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">3</style> 증가\n[WhenUse] 정신력 5 감소
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [HystericGauge], [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [HystericGauge] = 히스테리 / Hysteria; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: Deal <style="highlight">+4%</style> damage for every [HystericGauge] on self <style="highlight">(max 12%)</style>\n<style="highlight">[WhenUse] Consume 5 [ThePowerOfLoveAndHate] Count on self to gain Base Power +1</style>\n[WhenUse] Gain <style="highlight">+3</style> [ThePowerOfLoveAndHate] Count\n[WhenUse] Lose 5 SP
   PL: Zadaje <style="highlight">+4%</style> obrażeń za każde 1 [HystericGauge] <style="highlight">(maks. 12%)</style>\n<style="highlight">[WhenUse] Zużywa 5 Licznika [ThePowerOfLoveAndHate], aby zyskać Moc Bazową +1</style>\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o <style="highlight">3</style>\n[WhenUse] Traci 5 Poczytalności
453. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 423 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Sinking]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Sinking]
455. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 자신의 [HystericGauge]당 피해량 <style="highlight">+5% (최대 15%)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 5 소모하여, 기본 위력 +1\n<style="highlight">[WhenUse] 자신의 [ThePowerOfLoveAndHate] 2당, 기본 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가\n[WhenUse] 정신력 5 감소
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [HystericGauge], [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [HystericGauge] = 히스테리 / Hysteria; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: Deal <style="highlight">+5%</style> damage for every [HystericGauge] on self <style="highlight">(max 15%)</style>\n<style="highlight">[WhenUse] Consume 5 [ThePowerOfLoveAndHate] Count on self to gain Base Power +1</style>\n<style="highlight">[WhenUse] Base Power +1 for every 2 [ThePowerOfLoveAndHate] on self (max 2)</style>\n[WhenUse] Gain +3 [ThePowerOfLoveAndHate] Count\n[WhenUse] Lose 5 SP
   PL: Zadaje <style="highlight">+5%</style> obrażeń za każde 1 [HystericGauge] <style="highlight">(maks. 15%)</style>\n[WhenUse] Zużywa 5 Licznika [ThePowerOfLoveAndHate], aby zyskać Moc Bazową +1\n<style="highlight">[WhenUse] Moc Bazowa +1 za każde 2 [ThePowerOfLoveAndHate] (maks. 2)</style>\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 3\n[WhenUse] Traci 5 Poczytalności
456. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
457. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] <style="highlight">3</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031205].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Sinking]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Sinking]
458. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — nazwa] 내 머릿속에서 나가줘...
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=1].name ; dataList[id=1031206].levelList[level=2].name ; dataList[id=1031206].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 15 · monety: 2 (−6)
   limit: do 40 znaków
   EN: Get out of my head...
   PL: Wyjdź mi z głowy...
459. [Umiejętność 5 (×0) (ulepszenie 1) — opis] 자신의 [HystericGauge]가 있으면, 합 위력 +1\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가\n[WhenUse] 정신력 8 감소
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [HystericGauge], [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [HystericGauge] = 히스테리 / Hysteria; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: If this unit has [HystericGauge], Clash Power +1\n[WhenUse] Gain +3 [ThePowerOfLoveAndHate] Count\n[WhenUse] Lose 8 SP
   PL: Jeżeli ta jednostka ma [HystericGauge], Moc Starcia +1\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 3\n[WhenUse] Traci 8 Poczytalności
460. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 430 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Umiejętność 5 (×0) (ulepszenie 2) — opis] 자신의 [HystericGauge]가 있으면, <style="highlight">기본 위력 +1</style>\n<style="highlight">[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 6 소모하여, 기본 위력 +1</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가\n[WhenUse] 정신력 8 감소
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=2].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [HystericGauge], [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [HystericGauge] = 히스테리 / Hysteria; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: If this unit has [HystericGauge], <style="highlight">Base Power +1</style>\n<style="highlight">[WhenUse] Consume 6 [ThePowerOfLoveAndHate] Count on self to gain Base Power +1</style>\n[WhenUse] Gain +3 [ThePowerOfLoveAndHate] Count\n[WhenUse] Lose 8 SP
   PL: Jeżeli ta jednostka ma [HystericGauge], <style="highlight">Moc Bazowa +1</style>\n<style="highlight">[WhenUse] Zużywa 6 Licznika [ThePowerOfLoveAndHate], aby zyskać Moc Bazową +1</style>\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 3\n[WhenUse] Traci 8 Poczytalności
463. [Umiejętność 5 (×0) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ThePowerOfLoveAndHate] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1031206].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ThePowerOfLoveAndHate]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [OnSucceedAttack] Gain +3 [ThePowerOfLoveAndHate] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 3<style="highlight"></style>
464. [Umiejętność 5 (×0) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 454 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Umiejętność 5 (×0) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttackTail] 다음 턴에 메인 타겟에게 [VillainMark] 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackTail], [VillainMark]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [VillainMark] = 악당 표식 / Mark of Villainy
   EN: <style="highlight">[OnSucceedAttackTail] Inflict [VillainMark] against the main target next turn</style>
   PL: <style="highlight">[OnSucceedAttackTail] Nakłada w następnej turze [VillainMark] na główny cel</style>
466. [Umiejętność 5 (×0) (ulepszenie 4) — opis] <style="highlight">자신의 [HystericGauge]당 기본 위력 +1(최대 2)\n- [HystericGauge]가 3이면, 공격 가중치 +1\n- 서브 타겟에게 가하는 피해량 -50%</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 6 소모하여, 기본 위력 +1\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">5</style> 증가\n[WhenUse] 정신력 8 감소
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=4].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [HystericGauge], [WhenUse], [ThePowerOfLoveAndHate]
   znaczenie tagów: [HystericGauge] = 히스테리 / Hysteria; [WhenUse] = [사용시] / [On Use]; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: <style="highlight">Base Power +1 for every [HystericGauge] on self (max 2)\n- At 3 [HystericGauge], gain +1 Atk Weight\n- Deal -50% damage against sub-targets</style>\n[WhenUse] Consume 6 [ThePowerOfLoveAndHate] Count on self to gain Base Power +1\n[WhenUse] Gain +<style="highlight">5</style> [ThePowerOfLoveAndHate] Count\n[WhenUse] Lose 8 SP
   PL: <style="highlight">Moc Bazowa +1 za każde 1 [HystericGauge] (maks. 2)\n- Przy 3 [HystericGauge] Waga ataku +1\n- Zadaje -50% obrażeń celom drugorzędnym</style>\n[WhenUse] Zużywa 6 Licznika [ThePowerOfLoveAndHate], aby zyskać Moc Bazową +1\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o <style="highlight">5</style>\n[WhenUse] Traci 8 Poczytalności
467. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Sinking]<style="highlight"></style>
468. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack]</style> 다음 턴에 메인 타겟에게 [VillainMark] 부여
   źródło: Skills_personality-03.json :: dataList[id=1031206].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Umiejętność 6 (×0) (ulepszenia 3–4) — nazwa] 리버스드 비트 / 리버스드 아르카나 슬레이브
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].name ; dataList[id=1031207].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 20 · monety: 3 (−6)
   limit: do 60 znaków
   EN: Reversed Beats / Reversed Arcana Slave
   PL: Odwrócone Uderzenia / Odwrócona Sługa Arkan
470. [Umiejętność 6 (×0) (ulepszenie 3) — opis] 이 스킬로 서브 타겟에게 가하는 피해량 -50%\n\n[WhenUse] [HystericGauge]를 전부 소모하여, 합 위력 +1\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 8씩 소모하여, 합 위력 +1 (최대 2)\n자신의 [ThePowerOfLoveAndHate]당 피해량 +15%(최대 60%)\n[BeforeAttack] 자신의 [ArcanaQueenOfHate]를 전부 소모하여, 공격 가중치 +1\n[BeforeAttack] 공격 대상이 한 명(집중 전투일 경우, 부위로 판정)일 때, 공격 가중치가 2 이상이면 피해량 +20%\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -6 (최대 -18)\n[EndBattle] 정신력이 -45가 아니고 정신력이 0 미만이면, 정신력 10 회복. 정신력이 0보다 낮을수록 회복량 증가 (차이 1당 2회복, 최대 50)\n[WhenUse] 정신력 10 감소
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].desc
   limit: do 970 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [HystericGauge], [ThePowerOfLoveAndHate], [BeforeAttack], [ArcanaQueenOfHate], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [HystericGauge] = 히스테리 / Hysteria; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [ArcanaQueenOfHate] = 매지컬 아르카나 / Magical Arcana; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: This Skill deals -50% damage against sub-targets\n\n[WhenUse] Consume all [HystericGauge] to gain Clash Power +1\n[WhenUse] Consume [ThePowerOfLoveAndHate] Count to gain Clash Power (Clash Power +1 for every 8 Count consumed, max 2)\nDeal +15% damage for every [ThePowerOfLoveAndHate] on self (max 60%)\n[BeforeAttack] Consume all [ArcanaQueenOfHate] on self to gain +1 Atk Weight\n[BeforeAttack] If this Skill only has a single target(for Focused Encounters, a Part), but has 2+ Atk Weight, deal +20% damage\n[BeforeAttack] Base Power -6 for every Cracked Coin (max -18)\n[EndBattle] If this unit isn't at -45 SP, and is at less than 0 SP, heal 10 SP. Heal more SP the further this unit's SP value is from 0 (2 SP healed for every missing SP, max 50 SP)\n[WhenUse] Lose 10 SP
   PL: Ta Umiejętność zadaje -50% obrażeń celom drugorzędnym\n\n[WhenUse] Zużywa całe [HystericGauge], aby zyskać Moc Starcia +1\n[WhenUse] Zużywa po 8 Licznika [ThePowerOfLoveAndHate], aby zyskać Moc Starcia +1 (maks. 2)\nZadaje +15% obrażeń za każde 1 [ThePowerOfLoveAndHate] (maks. 60%)\n[BeforeAttack] Zużywa całe [ArcanaQueenOfHate], aby zyskać Wagę ataku +1\n[BeforeAttack] Jeżeli ta Umiejętność ma tylko 1 cel (w walce skupionej: część ciała), przy 2+ Wadze ataku zadaje +20% obrażeń\n[BeforeAttack] Moc Bazowa -6 za każdą Rozbitą monetę (maks. -18)\n[EndBattle] Jeżeli Poczytalność nie wynosi -45 i jest poniżej 0, odzyskuje 10 Poczytalności. Im niższa jest Poczytalność, tym większy odzysk (2 Poczytalności za każde 1 różnicy; maks. 50)\n[WhenUse] Traci 10 Poczytalności
471. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada 2 [Sinking]
474. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 473 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Umiejętność 6 (×0) (ulepszenie 4) — opis] 이 스킬로 서브 타겟에게 가하는 피해량 -50%\n\n[WhenUse] [HystericGauge]를 전부 소모하여<style="highlight">, 소모한 수치당 합 위력 +1 (최대 3)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수를 <style="highlight">5씩</style> 소모하여, 합 위력 +1 <style="highlight">(최대 4)</style>\n자신의 [ThePowerOfLoveAndHate]당 피해량 +<style="highlight">30</style>%(최대 <style="highlight">150</style>%)\n[BeforeAttack] 자신의 [ArcanaQueenOfHate]를 전부 소모하여, <style="highlight">소모한 수치당 공격 가중치 +1 (최대 3)\n- 이 스킬로 소모한 [HystericGauge]가 3이면, 공격 가중치 +1</style>\n[BeforeAttack] 공격 대상이 한 명(집중 전투일 경우, 부위로 판정)일 때, <style="highlight">(공격 가중치 - 1)만큼 피해량이 증가 (수치당 20%, 최대 80%)</style>\n[BeforeAttack] 파괴된 코인 수당 기본 위력 -6 (최대 -18)\n[EndBattle] 정신력이 -45가 아니고 정신력이 0 미만이면, 정신력 10회복. 정신력이 0보다 낮을수록 회복량 증가 (차이 1당 2회복, 최대 50)\n[WhenUse] 정신력 10 감소
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=4].desc
   limit: do 1130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [HystericGauge], [ThePowerOfLoveAndHate], [BeforeAttack], [ArcanaQueenOfHate], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [HystericGauge] = 히스테리 / Hysteria; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [ArcanaQueenOfHate] = 매지컬 아르카나 / Magical Arcana; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: This Skill deals -50% damage against sub-targets\n\n[WhenUse] Consume all [HystericGauge]; <style="highlight">Clash Power +1 for every Stack consumed (max 3)</style>\n[WhenUse] Consume [ThePowerOfLoveAndHate] Count to gain Clash Power (Clash Power +1 for every <style="highlight">5</style> Count consumed, max <style="highlight">4</style>)\nDeal +<style="highlight">30</style>% damage for every [ThePowerOfLoveAndHate] on self (max <style="highlight">150</style>%)\n[BeforeAttack] Consume all [ArcanaQueenOfHate] on self; <style="highlight">gain +1 Atk Weight for every Stack consumed (max 3)\n- If this Skill consumed 3 [HystericGauge], gain +1 Atk Weight</style>\n[BeforeAttack] If this Skill only has a single target(for Focused Encounters, a Part), <style="highlight">deal +(20 x (Atk Weight - 1))% damage (max 80%)</style>\n[BeforeAttack] Base Power -6 for every Cracked Coin (max -18)\n[EndBattle] If this unit isn't at -45 SP, and is at less than 0 SP, heal 10 SP. Heal more SP the further this unit's SP value is from 0 (2 SP healed for every missing SP, max 50 SP)\n[WhenUse] Lose 10 SP
   PL: Ta Umiejętność zadaje -50% obrażeń celom drugorzędnym\n\n[WhenUse] Zużywa całe [HystericGauge]<style="highlight">; Moc Starcia +1 za każdy 1 zużyty stos (maks. 3)</style>\n[WhenUse] Zużywa po <style="highlight">5</style> Licznika [ThePowerOfLoveAndHate], aby zyskać Moc Starcia +1 <style="highlight">(maks. 4)</style>\nZadaje +<style="highlight">30</style>% obrażeń za każde 1 [ThePowerOfLoveAndHate] (maks. <style="highlight">150</style>%)\n[BeforeAttack] Zużywa całe [ArcanaQueenOfHate]; <style="highlight">Waga ataku +1 za każdy 1 zużyty stos (maks. 3)\n- Jeżeli ta Umiejętność zużyła 3 [HystericGauge], Waga ataku +1</style>\n[BeforeAttack] Jeżeli ta Umiejętność ma tylko 1 cel (w walce skupionej: część ciała), <style="highlight">zadaje +(20 x (Waga ataku - 1))% obrażeń (maks. 80%)</style>\n[BeforeAttack] Moc Bazowa -6 za każdą Rozbitą monetę (maks. -18)\n[EndBattle] Jeżeli Poczytalność nie wynosi -45 i jest poniżej 0, odzyskuje 10 Poczytalności. Im niższa jest Poczytalność, tym większy odzysk (2 Poczytalności za każde 1 różnicy; maks. 50)\n[WhenUse] Traci 10 Poczytalności
477. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL: [SuperCoin]<style="highlight"></style>
478. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Sinking]<style="highlight"></style>
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada 2 [Sinking]<style="highlight"></style>
480. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031207].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 479 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Obrona (ulepszenia 1,4) — nazwa] 단기 영창
   źródło: Skills_personality-03.json :: dataList[id=1031204].levelList[level=1].name ; dataList[id=1031204].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 2 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Rapid Chant
   PL: Rozkaz Szybki
483. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[WhenUse] 자신의 [HystericGauge]당, 기본 위력 +1 (최대 2)\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 2 증가 (턴 당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1031204].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WhenUse], [HystericGauge], [ThePowerOfLoveAndHate]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [HystericGauge] = 히스테리 / Hysteria; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [CanDuelGuard]\n[WhenUse] Base Power +1 for every [HystericGauge] (max 2)\n[WhenUse] Gain +2 [ThePowerOfLoveAndHate] Count (2 times per turn)
   PL: [CanDuelGuard]\n[WhenUse] Moc Bazowa +1 za każde 1 [HystericGauge] (maks. 2)\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o 2 (2 razy na turę)
484. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031204].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1031204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[WhenUse] 자신의 [HystericGauge]당, 기본 위력 +1 <style="highlight">(최대 3)</style>\n[WhenUse] 자신의 [ThePowerOfLoveAndHate] 횟수 <style="highlight">4</style> 증가 (턴 당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1031204].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [WhenUse], [HystericGauge], [ThePowerOfLoveAndHate]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [HystericGauge] = 히스테리 / Hysteria; [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: [CanDuelGuard]\n[WhenUse] Base Power +1 for every [HystericGauge] <style="highlight">(max 3)</style>\n[WhenUse] Gain +<style="highlight">4</style> [ThePowerOfLoveAndHate] Count (2 times per turn)
   PL: [CanDuelGuard]\n[WhenUse] Moc Bazowa +1 za każde 1 [HystericGauge] <style="highlight">(maks. 3)</style>\n[WhenUse] Zwiększa własny Licznik [ThePowerOfLoveAndHate] o <style="highlight">4</style> (2 razy na turę)
486. [Pasywka bojowa (od ulepszenia 1) — nazwa] 사랑과 증오의 이름으로 - !E.G.O 장비 동기화율 초과주의!
   źródło: Passives.json :: dataList[id=1031202].name
   limit: do 100 znaków
   EN: In the Name of Love and Hate - !ALERT: E.G.O GEAR SYNC THRESHOLD EXCEEDED!
   PL: W Imię Miłości i Nienawiści - !UWAGA: E.G.O przekroczyło próg synchronizacji!
487. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 중 누적으로 자신의 [ThePowerOfLoveAndHate] 횟수 10을 소모할 때마다, [ThePowerOfLoveAndHate] 1 얻음\n\n스테이지 시작시 [HystericGauge]가 없다면, [HystericGauge] 효과를 얻음\n\n스테이지 시작시 [ThePowerOfLoveAndHate]가 없다면, [ThePowerOfLoveAndHate] 효과를 얻음\n\n턴 시작시\n- 정신력이 0 이상이면, [MagicalGirlAppear] 얻음, [NoVillain] 제거\n- 정신력이 0 미만이면, [NoVillain] 얻음, [MagicalGirlAppear] 제거\n\n자신의 기본 공격 스킬의 정신력 소모 효과에 의해서 정신력이 -40 미만으로 내려가지 않음
   źródło: Passives.json :: dataList[id=1031202].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: \n, [ThePowerOfLoveAndHate], [HystericGauge], [MagicalGirlAppear], [NoVillain]
   znaczenie tagów: [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [HystericGauge] = 히스테리 / Hysteria; [MagicalGirlAppear] = 마법소녀 등장! / Here Comes Magical Girl!; [NoVillain] = 역변-리버스드 / Regressive Transformation - Reversed
   EN: Gain 1 [ThePowerOfLoveAndHate] every time this unit consumes 10 cumulative [ThePowerOfLoveAndHate] Count in this Encounter\n\nEncounter Start: if this unit does not have [HystericGauge], gain [HystericGauge]\n\nEncounter Start: if this unit does not have [ThePowerOfLoveAndHate], gain [ThePowerOfLoveAndHate]\n\nTurn Start:\n- At 0 or higher SP, gain [MagicalGirlAppear] and lose [NoVillain]\n- At less than 0 SP, gain [NoVillain] and lose [MagicalGirlAppear]\n\nThis unit's SP cannot drop below -40 due to the SP loss effects from this unit's Base Attack Skills
   PL: Za każde łączne zużycie 10 własnego Licznika [ThePowerOfLoveAndHate] podczas walki zyskuje 1 [ThePowerOfLoveAndHate]\n\nNa początku spotkania: jeżeli ta jednostka nie ma [HystericGauge], zyskuje [HystericGauge]\n\nNa początku spotkania: jeżeli ta jednostka nie ma [ThePowerOfLoveAndHate], zyskuje [ThePowerOfLoveAndHate]\n\nNa początku tury\n- Przy Poczytalności 0 lub wyższej zyskuje [MagicalGirlAppear] i traci [NoVillain]\n- Przy Poczytalności poniżej 0 zyskuje [NoVillain] i traci [MagicalGirlAppear]\n\nPoczytalność tej jednostki nie może spaść poniżej -40 wskutek efektów zużycia Poczytalności jej podstawowych Umiejętności ataku
488. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Envy) — nazwa] 사랑의 마법소녀 / 증오의 여왕
   źródło: Passives.json :: dataList[id=1031201].name
   limit: do 60 znaków
   EN: Magical Girl of Love / Queen of Hatred
   PL: Czarodziejka Miłości / Królowa Nienawiści
489. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Envy) — opis] [ThePowerOfLoveAndHate]당, 피해량 +2% (최대 10%)
   źródło: Passives.json :: dataList[id=1031201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ThePowerOfLoveAndHate]
   znaczenie tagów: [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate
   EN: Deal +2% damage for every [ThePowerOfLoveAndHate] (max 10%)
   PL: Zadaje +2% obrażeń za każde 1 [ThePowerOfLoveAndHate] (maks. 10%)
490. [Pasywka bojowa (od ulepszenia 3, rezonans 4× Envy) — nazwa] 사랑의 마법소녀 / 증오의 여왕
   źródło: Passives.json :: dataList[id=1031211].name
   (powtórzenie elementu 488 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Pasywka bojowa (od ulepszenia 3, rezonans 4× Envy) — opis] [ThePowerOfLoveAndHate]당, 피해량 +2% (최대 10%)\n전투 시작 시, [ArcanaQueenOfHate] 1 얻음
   źródło: Passives.json :: dataList[id=1031211].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [ThePowerOfLoveAndHate], [ArcanaQueenOfHate]
   znaczenie tagów: [ThePowerOfLoveAndHate] = 사랑/증오 / Love/Hate; [ArcanaQueenOfHate] = 매지컬 아르카나 / Magical Arcana
   EN: Deal +2% damage for every [ThePowerOfLoveAndHate] (max 10%)\nCombat Start: gain 1 [ArcanaQueenOfHate]
   PL: Zadaje +2% obrażeń za każde 1 [ThePowerOfLoveAndHate] (maks. 10%)\nNa początku walki zyskuje 1 [ArcanaQueenOfHate]
492. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — nazwa] 매지컬 파워 차징 서포트
   źródło: Passives.json :: dataList[id=1031221].name
   limit: do 50 znaków
   EN: Magical Power Charging Support
   PL: Wspierające Ładowanie Mocy Magicznej
493. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — opis] 기본 공격 스킬에서 [Charge] 횟수를 획득하는 아군 중 [Charge] 횟수가 가장 적은 1명이 [Charge] 횟수를 획득하는 기본 공격 스킬 사용 시, [Charge] 횟수 +2 (턴 당 2회 발동)\n- 정신력이 0 이상이면, 체력을 (대상의 [Charge] X 2)만큼 회복 (최대 10, 턴 당 최대 20 회복)\n- 정신력이 0 미만이면, 정신력을 대상의 [Charge]만큼 회복 (최대 5, 턴 당 최대 10 회복)
   źródło: Passives.json :: dataList[id=1031221].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: If, among allies that gain [Charge] Count using their Base Attack Skills, 1 ally that has the least [Charge] Count uses a Base Attack Skill that gains [Charge] Count, the said ally gains +2 [Charge] Count (2 times per turn)\n- At 0 or higher SP: heal ([Charge] on target x 2) HP (max 10; heals up to 20 per turn)\n- At less than 0 SP: heal ([Charge] on target) SP (max 5; heals up to 10 per turn)
   PL: Gdy 1 Sojusznik z najmniejszym Licznikiem [Charge] wśród zyskujących Licznik [Charge] podstawowymi Umiejętnościami ataku użyje podstawowej Umiejętności ataku zyskującej Licznik [Charge], ten sojusznik zyskuje +2 Licznika [Charge] (2 razy na turę)\n- Przy Poczytalności 0 lub wyższej: odzyskuje HP równe (2 x [Charge] celu) (maks. 10, maks. 20 na turę)\n- Przy Poczytalności poniżej 0: odzyskuje Poczytalność równą [Charge] celu (maks. 5, maks. 10 na turę)
494. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — podsumowanie] [Charge] 횟수 증가\n- 정신력에 따라, [Charge]에 비례하여 체력이나 정신력 회복
   źródło: Passives.json :: dataList[id=1031221].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain [Charge] Count\n- Depending on this unit's SP, Heal HP or SP based on [Charge]
   PL: Zwiększa Licznik [Charge]\n- Zależnie od Poczytalności, odzyskuje HP lub Poczytalność proporcjonalnie do [Charge]

## [000] Heishou Pack - Wei Branch — Don Quixote — 흑수 - 미
- ID Tożsamości: `10313` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 82 · szybkość: 2–5 / 3–7 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Rupture, Sinking

495. [Karta Tożsamości — tytuł] 흑수 - 미
   źródło: Personalities.json :: dataList[id=10313].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heishou Pack -\nWei Branch
   PL: Wataha Heishou - Gałąź Wei
496. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10313].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10313].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Karta Tożsamości — opis] 돈키호테의 열세번째 인격
   źródło: Personalities.json :: dataList[id=10313].desc
   limit: do 120 znaków
   EN: Don Quixote's 13th Identity
   PL: Trzynasta Tożsamość Don Quixote
499. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 돌파
   źródło: Skills_personality-03.json :: dataList[id=1031301].levelList[level=1].name ; dataList[id=1031301].levelList[level=2].name ; dataList[id=1031301].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Breakthrough
   PL: Przełom
500. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]
501. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] celu o 1
502. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031301].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">대상의 [Burst]과 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-03.json :: dataList[id=1031301].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Burst], [Sinking]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">If target has 6+ ([Burst] + [Sinking]), Coin Power +1</style>
   PL: <style="highlight">Jeżeli cel ma 6+ (suma [Burst] i [Sinking]), Moc Monet +1</style>
505. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1031301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]<style="highlight"></style>
506. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031301].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1031301].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] celu o 1<style="highlight"></style>
507. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031301].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1031301].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Burst]<style="highlight"></style>
508. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031301].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1031301].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Sinking]<style="highlight"></style>
509. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">대상에게 [CrushMarks]이 있으면, 피해량 +25%</style>\n대상의 [Burst]과 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-03.json :: dataList[id=1031301].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CrushMarks], [Burst], [Sinking]
   znaczenie tagów: [CrushMarks] = 파쇄흔 / Shattermark; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">If target has [CrushMarks], deal +25% damage</style>\n<style="highlight">Coin Power +1 for every 6 ([Burst] + [Sinking]) on target (max 2)</style>
   PL: <style="highlight">Jeżeli cel ma [CrushMarks], zadaje +25% obrażeń</style>\nMoc Monet +1 za każde <style="highlight">6</style> (suma [Burst] i [Sinking] celu) <style="highlight">(maks. 2)</style>
510. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 파죽지세
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=1].name ; dataList[id=1031302].levelList[level=2].name ; dataList[id=1031302].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 50 znaków
   EN: Seize the Momentum, Shatter the Wall
   PL: Niepowstrzymany Rozmach
511. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">대상의 [Burst]과 [Sinking]의 합이 6 이상이면, 코인 위력 +1\n[StartBattle] 자신에게 [GrownHorns]이 있으면, 이 스킬의 마지막 코인이 [SuperCoin]으로 변경됨</style>
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [Sinking], [StartBattle], [GrownHorns], [SuperCoin]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [GrownHorns] = 발각[發角] / Burgeoning of Horns [發角]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: <style="highlight">If target has 6+ ([Burst] + [Sinking]), Coin Power +1\n[StartBattle] If this unit has [GrownHorns], convert the last Coin of this Skill into [SuperCoin]</style>
   PL: <style="highlight">Jeżeli cel ma 6+ (suma [Burst] i [Sinking]), Moc Monet +1\n[StartBattle] Jeżeli ta jednostka ma [GrownHorns], ostatnia Moneta tej Umiejętności zmienia się w [SuperCoin]</style>
516. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1031302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1031302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 506 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 507 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=2].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 자신에게 [GrownHorns]이 있으면, 수치 1당 이 코인 최종 피해량의 5%만큼 참격 피해 (최대 15%)</style>
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=2].coinlist[#2].coindescs[#2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [GrownHorns]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GrownHorns] = 발각[發角] / Burgeoning of Horns [發角]
   EN: <style="highlight">[OnSucceedAttack] Deal Slash damage equal to 5% of this Coin's final damage for every [GrownHorns] Stack on this unit (max 15%)</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli ta jednostka ma [GrownHorns], zadaje obrażenia Cięcia równe 5% końcowych obrażeń tej monety za każdy 1 stos [GrownHorns] (maks. 15%)</style>
521. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Burst]과 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[StartBattle] 자신에게 [GrownHorns]이 있으면, 이 스킬의 마지막 코인이 [SuperCoin]으로 변경되고 <style="highlight">수치 1당 마지막 코인의 피해량 +5% (최대 15%)</style>
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=4].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [Sinking], [StartBattle], [GrownHorns], [SuperCoin]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [GrownHorns] = 발각[發角] / Burgeoning of Horns [發角]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: <style="highlight">Coin Power +1 for every 6 ([Burst] + [Sinking]) on target (max 2)</style>\n[StartBattle] If this unit has [GrownHorns], convert the last Coin of this Skill into [SuperCoin]; <style="highlight">the last Coin deals +5% damage for every [GrownHorns] Stack on this unit (max 15%)</style>
   PL: Moc Monet +1 za każde <style="highlight">6</style> (suma [Burst] i [Sinking] celu) <style="highlight">(maks. 2)</style>\n[StartBattle] Jeżeli ta jednostka ma [GrownHorns], ostatnia Moneta tej Umiejętności zmienia się w [SuperCoin] i <style="highlight">zadaje +5% obrażeń za każdy 1 stos [GrownHorns] (maks. 15%)</style>
522. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 454 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신에게 [GrownHorns]이 있으면, 수치 1당 이 코인 최종 피해량의 <style="highlight">10%</style>만큼 참격 피해 (최대 <style="highlight">30%</style>)
   źródło: Skills_personality-03.json :: dataList[id=1031302].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [GrownHorns]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GrownHorns] = 발각[發角] / Burgeoning of Horns [發角]
   EN: [OnSucceedAttack] Deal Slash damage equal to <style="highlight">10%</style> of this Coin's final damage for every [GrownHorns] Stack on this unit (max <style="highlight">30%</style>)
   PL: [OnSucceedAttack] Jeżeli ta jednostka ma [GrownHorns], zadaje obrażenia Cięcia równe <style="highlight">10%</style> końcowych obrażeń tej monety za każdy 1 stos [GrownHorns] (maks. <style="highlight">30%</style>)
525. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 파쇄각 [破碎角]
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=3].name ; dataList[id=1031303].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Crushing Horns [破碎角]
   PL: Roztrzaskane Rogi [破碎角]
526. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Burst]과 [Sinking]의 합이 6 이상이면, 코인 위력 +1\n[StartBattle] 자신에게 [GrownHorns]이 있으면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] [GrownHorns] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=3].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Sinking], [StartBattle], [GrownHorns], [SuperCoin], [WhenUse]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [GrownHorns] = 발각[發角] / Burgeoning of Horns [發角]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]
   EN: If target has 6+ ([Burst] + [Sinking]), Coin Power +1\n[StartBattle] If this unit has [GrownHorns], convert all Coins of this Skill into [SuperCoin]\n[WhenUse] Gain 3 [GrownHorns]
   PL: Jeżeli cel ma 6+ (suma [Burst] i [Sinking]), Moc Monet +1\n[StartBattle] Jeżeli ta jednostka ma [GrownHorns], wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin]\n[WhenUse] Zyskuje 3 [GrownHorns]
527. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 189 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] Nakłada 2 [Sinking]
531. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] 대상에게 패닉 타입 변경 효과가 있으면, 수치 1당 피해량 +5% (최대 15%)
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: - If target has any of the Panic type changing effects, +5% damage for every Stack (max 15%)
   PL: - Jeżeli cel ma efekt zmieniający typ Paniki, zadaje +5% obrażeń za każdy 1 stos (maks. 15%)
532. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 25%만큼 참격 피해
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal (25% of this Coin's final damage) Slash damage
   PL: [OnSucceedAttack] Zadaje obrażenia Cięcia równe 25% końcowych obrażeń tej monety
533. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [CrushMarks] 3 부여
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=3].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [CrushMarks]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CrushMarks] = 파쇄흔 / Shattermark
   EN: [OnSucceedAttack] Inflict 3 [CrushMarks] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 3 [CrushMarks]
534. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Burst]과 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[StartBattle] 자신에게 [GrownHorns]이 있으면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경되고 <style="highlight">수치 1당 피해량 +10% (최대 30%)</style>\n[WhenUse] [GrownHorns] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=4].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [Sinking], [StartBattle], [GrownHorns], [SuperCoin], [WhenUse]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [GrownHorns] = 발각[發角] / Burgeoning of Horns [發角]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">Coin Power +1 for every 6 ([Burst] + [Sinking]) on target (max 2)</style>\n[StartBattle] If this unit has [GrownHorns], convert all Coins of this Skill into [SuperCoin] and <style="highlight">deal +10% damage for every [GrownHorns] Stack on this unit (max 30%)</style>\n[WhenUse] Gain 3 [GrownHorns]
   PL: Moc Monet +1 za każde <style="highlight">6</style> (suma [Burst] i [Sinking] celu) <style="highlight">(maks. 2)</style>\n[StartBattle] Jeżeli ta jednostka ma [GrownHorns], wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin] i <style="highlight">zadaje +10% obrażeń za każdy 1 stos [GrownHorns] (maks. 30%)</style>\n[WhenUse] Zyskuje 3 [GrownHorns]
535. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">+2</style> [Burst] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Burst] celu o <style="highlight">2</style>
536. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">+2</style> [Sinking] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] celu o <style="highlight">2</style>
537. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] 대상에게 패닉 타입 변경 효과가 있으면, 수치 1당 피해량 <style="highlight">+10%</style> (최대 <style="highlight">30%</style>)
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: - If target has any of the Panic type changing effects, <style="highlight">+10%</style> damage for every Stack (max <style="highlight">30%</style>)
   PL: - Jeżeli cel ma efekt zmieniający typ Paniki, zadaje <style="highlight">+10%</style> obrażeń za każdy 1 stos (maks. <style="highlight">30%</style>)
540. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 25%만큼 참격 피해\n<style="highlight">- 대상에게 [CrushMarks]이 있으면 효과가 강화되어, 대신 50%만큼 참격 피해</style>
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [CrushMarks]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CrushMarks] = 파쇄흔 / Shattermark
   EN: [OnSucceedAttack] Deal (25% of this Coin's final damage) Slash damage\n<style="highlight">- If target has [CrushMarks], strengthen this effect and deal (50% of this Coin's final damage) Slash damage instead
   PL: [OnSucceedAttack] Zadaje obrażenia Cięcia równe 25% końcowych obrażeń tej monety\n<style="highlight">- Jeżeli cel ma [CrushMarks], efekt się wzmacnia: zadaje zamiast tego obrażenia Cięcia równe 50% końcowych obrażeń tej monety</style>
541. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [CrushMarks] 3 부여\n<style="highlight">- 대상에게 패닉 타입 변경 효과가 있으면, 추가로 대상의 [Sinking] 횟수 3 증가 (턴당 1회)</style>
   źródło: Skills_personality-03.json :: dataList[id=1031303].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [CrushMarks], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CrushMarks] = 파쇄흔 / Shattermark; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [CrushMarks] next turn\n<style="highlight">- If target has any of the Panic type changing effects, inflict +3 [Sinking] Count (once per turn)</style>
   PL: [OnSucceedAttack] Nakłada w następnej turze 3 [CrushMarks]\n<style="highlight">- Jeżeli cel ma efekt zmieniający typ Paniki, zwiększa dodatkowo Licznik [Sinking] celu o 3 (1 raz na turę)</style>
542. [Obrona (ulepszenia 1,4) — nazwa] 가로막는 것들을 모조리 박살내주겠네!
   źródło: Skills_personality-03.json :: dataList[id=1031304].levelList[level=1].name ; dataList[id=1031304].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 60 znaków
   EN: I shall crush all that standeth in our way!
   PL: Rozbije wszystko, co stanie nam na drodze!
543. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 다음 턴에 [GrownHorns] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [GrownHorns]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [GrownHorns] = 발각[發角] / Burgeoning of Horns [發角]
   EN: [DuelCounter] \n[WhenUse] Gain 3 [GrownHorns] next turn
   PL: [DuelCounter]\n[WhenUse] Zyskuje w następnej turze 3 [GrownHorns]
544. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n<style="highlight">대상의 [Burst]과 [Sinking]의 합 3당, 최종 위력 +1 (최대 3)</style>\n[WhenUse] 다음 턴에 [GrownHorns] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031304].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [Burst], [Sinking], [WhenUse], [GrownHorns]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [GrownHorns] = 발각[發角] / Burgeoning of Horns [發角]
   EN: [DuelCounter]\n<style="highlight">Final Power +1 for every 3 ([Burst] + [Sinking]) on target (max 3)</style>\n[WhenUse] Gain 3 [GrownHorns] next turn
   PL: [DuelCounter]\nMoc Końcowa +1 za każde <style="highlight">3</style> (suma [Burst] i [Sinking] celu) <style="highlight">(maks. 3)</style>\n[WhenUse] Zyskuje w następnej turze 3 [GrownHorns]
547. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 507 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031304].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Pasywka bojowa (od ulepszenia 1) — nazwa] 망양지탄 [亡羊之嘆]
   źródło: Passives.json :: dataList[id=1031302].name
   limit: do 50 znaków
   EN: Lament of the Lost Sheep [亡羊之嘆]
   PL: Skarga o Zgubionej Owcy [亡羊之嘆]
550. [Pasywka bojowa (od ulepszenia 1) — opis] 홍원 군주 홍루와 [HeishouCombo] 발동 시, 홍원 군주 홍루가 [HeishouComboCountHonglu]으로 아래 효과 얻음\n- 스킬로 [Burst] 위력 또는 횟수 부여 시, [Sinking] 1 부여 (턴당 3회)\n\n대기 해제 또는 복귀로 등장한 턴에 [GrownHorns] 3 얻음
   źródło: Passives.json :: dataList[id=1031302].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [HeishouCombo], [HeishouComboCountHonglu], [Burst], [Sinking], [GrownHorns]
   znaczenie tagów: [HeishouCombo] = 존명 / Exalted Command; [HeishouComboCountHonglu] = 흑수환염[黑獣丸染] / Heishou Bolus Contamination [黑獣丸染]; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [GrownHorns] = 발각[發角] / Burgeoning of Horns [發角]
   EN: When activating [HeishouCombo], The Lord of Hongyuan Hong Lu gains the following effect as the [HeishouComboCountHonglu] effect:\n- Inflict 1 [Sinking] upon inflicting [Burst] Potency or Count by using a Skill (3 times per turn)\n\nOn the turn this unit Substituted or Returned to the field, gain 3 [GrownHorns]
   PL: Gdy Władca Hongyuan Hong Lu uruchomi [HeishouCombo], zyskuje poniższy efekt jako [HeishouComboCountHonglu]:\n- Przy nakładaniu Mocy lub Licznika [Burst] Umiejętnością nakłada 1 [Sinking] (3 razy na turę)\n\nW turze, w której ta jednostka weszła na pole przez Wejście z rezerwy lub Powrót, zyskuje 3 [GrownHorns]
551. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 홍원 군주 홍루가 특수 효과를 얻음
   źródło: Passives.json :: dataList[id=1031302].summary
   limit: do 120 znaków
   EN: The Lord of Hongyuan Hong Lu gains special effect
   PL: Władca Hongyuan Hong Lu zyskuje efekt specjalny
552. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut., posiadane 3× Gloom) — nazwa] 발파각쇄
   źródło: Passives.json :: dataList[id=1031301].name
   limit: do 40 znaków
   EN: Explosive Battering Ram
   PL: Wybuchowy Taran
553. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut., posiadane 3× Gloom) — opis] 대상의 [Burst]과 [Sinking]의 합 2당 피해량 +1% (최대 15%)\n- 정신력이 없는 대상이면, 이 효과와 최댓값이 2배로 증가\n\n자신에게 [GrownHorns]이 있으면, 적을 공격할 때 기본 스킬 마지막 코인의 피해량 +10%\n- 수비 스킬을 장착한 스킬 슬롯 공격 시, 대신 마지막 코인의 피해량 +20%\n- 합 가능 수비 스킬과 합 진행 시, 추가로 합 위력 +1
   źródło: Passives.json :: dataList[id=1031301].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Sinking], [GrownHorns]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [GrownHorns] = 발각[發角] / Burgeoning of Horns [發角]
   EN: Deal +1% damage for every 2 ([Burst] + [Sinking]) on target (max 15%)\n- Double this effect and max value against Non-SP targets\n\nIf this unit has [GrownHorns], the last coin of this unit's Base Skills deals +10% damage\n- When attacking Skill Slots equipped with a Defense Skill, the last Coin deals +20% damage instead\n- When Clashing against a Clashable Guard Skill, Clash Power +1
   PL: Zadaje +1% obrażeń za każde 2 (suma [Burst] i [Sinking] celu) (maks. 15%)\n- Przy celach bez Poczytalności efekt i maksimum podwajają się\n\nJeżeli ta jednostka ma [GrownHorns], ostatnia moneta jej podstawowych Umiejętności zadaje +10% obrażeń\n- Przy ataku na slot wyposażony w Umiejętność obrony ostatnia moneta zadaje zamiast tego +20% obrażeń\n- Przy Starciu z Umiejętnością Gardy zdolną do Starcia dodatkowo Moc Starcia +1
554. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut., posiadane 3× Gloom) — podsumowanie] 대상의 [Burst], [Sinking]에 비례하여 피해량이 증가\n[GrownHorns]이 있으면, 기본 스킬 마지막 코인 피해량이 증가
   źródło: Passives.json :: dataList[id=1031301].summary
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Sinking], [GrownHorns]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [GrownHorns] = 발각[發角] / Burgeoning of Horns [發角]
   EN: Deal more damage based on [Burst] and [Sinking] on target\nIf this unit has [GrownHorns], the last Coin of this unit's Base Skills deals more damage
   PL: Zadaje więcej obrażeń zależnie od [Burst] i [Sinking] celu\nJeżeli ma [GrownHorns], ostatnia moneta podstawowych Umiejętności zadaje więcej obrażeń
555. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Glut., posiadane 3× Gloom) — nazwa] 발파각쇄
   źródło: Passives.json :: dataList[id=1031311].name
   (powtórzenie elementu 552 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Glut., posiadane 3× Gloom) — opis] <style="highlight">대상의 정신력이 0 미만이면, 피해량이 (-대상의 정신력/3)%만큼 증가 (최대 15%, 소수점 버림)</style>\n\n대상의 [Burst]과 [Sinking]의 합 2당 피해량 +1% (최대 15%)\n- 정신력이 없는 대상이면, 이 효과와 최댓값이 2배로 증가\n\n자신에게 [GrownHorns]이 있으면, 적을 공격할 때 기본 스킬 마지막 코인의 피해량 <style="highlight">+15%</style>\n- 수비 스킬을 장착한 스킬 슬롯 공격 시, 대신 마지막 코인의 피해량 <style="highlight">+30%</style>\n- 합 가능 수비 스킬과 합 진행 시, 추가로 합 위력 <style="highlight">+3</style>
   źródło: Passives.json :: dataList[id=1031311].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [Sinking], [GrownHorns]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [GrownHorns] = 발각[發角] / Burgeoning of Horns [發角]
   EN: <style="highlight">Deal (-Target's SP / 3)% more damage against targets at less than 0 SP (max 15%, rounded down)</style>\n\nDeal +1% damage for every 2 ([Burst] + [Sinking]) on target (max 15%)\n- Double this effect and max value against Non-SP targets\n\nIf this unit has [GrownHorns], the last coin of this unit's Base Skills deals <style="highlight">+15%</style> damage\n- When attacking Skill Slots equipped with a Defense Skill, the last Coin deals <style="highlight">+30%</style> damage instead\n- When Clashing against a Clashable Guard Skill, Clash Power <style="highlight">+3</style>
   PL: <style="highlight">Zadaje (-Poczytalność celu / 3)% więcej obrażeń celom z Poczytalnością poniżej 0 (maks. 15%, zaokrąglone w dół)</style>\n\nZadaje +1% obrażeń za każde 2 (suma [Burst] i [Sinking] celu) (maks. 15%)\n- Przy celach bez Poczytalności efekt i maksimum podwajają się\n\nJeżeli ta jednostka ma [GrownHorns], ostatnia moneta jej podstawowych Umiejętności zadaje <style="highlight">+15%</style> obrażeń\n- Przy ataku na slot wyposażony w Umiejętność obrony ostatnia moneta zadaje zamiast tego <style="highlight">+30%</style> obrażeń\n- Przy Starciu z Umiejętnością Gardy zdolną do Starcia dodatkowo Moc Starcia <style="highlight">+3</style>
557. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Glut., posiadane 3× Gloom) — podsumowanie] 대상의 [Burst], [Sinking]에 비례하여 피해량이 증가\n[GrownHorns]이 있으면, 기본 스킬 마지막 코인 피해량이 증가
   źródło: Passives.json :: dataList[id=1031311].summary
   (powtórzenie elementu 554 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Glut., posiadane 3× Gloom) — nazwa] 살을 뚫고 자라나는 뿔
   źródło: Passives.json :: dataList[id=1031321].name
   limit: do 40 znaków
   EN: Flesh-Rending Horn Growth
   PL: Rośnące Rzujące Rogi
559. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Glut., posiadane 3× Gloom) — opis] 속도가 가장 빠른 아군이 [Burst] 횟수 또는 [Sinking] 횟수를 2 이상 보유한 적에게 기본 공격 스킬 적중 시, [DefenseDown] 1 부여 (턴당 2회)
   źródło: Passives.json :: dataList[id=1031321].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [Burst], [Sinking], [DefenseDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Ally with the fastest Speed: On Hit using a Base Attack Skill against enemies that have 2+ [Burst] Count or [Sinking] Count, inflict 1 [DefenseDown] (2 times per turn)
   PL: Sojusznik z najwyższą Szybkością: przy trafieniu podstawową Umiejętnością ataku wroga z 2+ Licznikiem [Burst] lub [Sinking] nakłada 1 [DefenseDown] (2 razy na turę)
560. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Glut., posiadane 3× Gloom) — podsumowanie] [Burst], [Sinking] 보유한 적에게 기본 공격 스킬 적중 시, [DefenseDown] 1 부여
   źródło: Passives.json :: dataList[id=1031321].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Burst], [Sinking], [DefenseDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: On Hit using a Base Attack Skill against enemies that have [Burst] or [Sinking], inflict 1 [DefenseDown]
   PL: Przy trafieniu podstawową Umiejętnością ataku wroga z [Burst] lub [Sinking] nakłada 1 [DefenseDown]

## [000] The Index Proxy - Effloresced E.G.O:: Procuration — Don Quixote — 검지 대행자 - 개화 E.G.O:: 대행
- ID Tożsamości: `10314` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 7 · HP bazowe: 76 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Poise, Sinking

561. [Karta Tożsamości — tytuł] 검지 대행자 -\n개화 E.G.O::\n대행
   źródło: Personalities.json :: dataList[id=10314].title
   limit: do 70 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Index Proxy - \nEffloresced E.G.O::\nProcuration
   PL: Pełnomocnik Wskazującego -\nRozkwitła E.G.O::\nPełnomocnictwo
562. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10314].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10314].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Karta Tożsamości — opis] 돈키호테의 열네번째 인격
   źródło: Personalities.json :: dataList[id=10314].desc
   limit: do 120 znaków
   EN: Don Quixote's 14th Identity
   PL: Czternasta Tożsamość Don Quixote
565. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 머리 으깨기
   źródło: Skills_personality-03.json :: dataList[id=1031401].levelList[level=1].name ; dataList[id=1031401].levelList[level=2].name ; dataList[id=1031401].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Skull Crushing
   PL: Rozbicie Czaszki
566. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +10%\n[WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031401].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetMarkToEnemy], [WhenUse], [Breath]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +10% damage\n[WhenUse] Gain +1 [Breath] Count
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje +10% obrażeń\n[WhenUse] Zwiększa własny Licznik [Breath] o 1
567. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +10%\n<style="highlight">자신의 [Breath]과 대상의 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031401].levelList[level=2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +10% damage\n<style="highlight">At 6+ ([Breath] on self + [Sinking] on target), Coin Power +1</style>\n[WhenUse] Gain +<style="highlight">2</style> [Breath] Count
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje +10% obrażeń\n<style="highlight">Przy 6+ (suma własnej [Breath] i [Sinking] celu) Moc Monet +1</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o <style="highlight">2</style>
570. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1031401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1031401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 1 [Breath]<style="highlight"></style>
572. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, <style="highlight">최종 위력 +1</style>, 피해량 <style="highlight">+15%</style>\n자신의 [Breath]과 대상의 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031401].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], <style="highlight">Final Power +1</style> and deal <style="highlight">+15%</style> damage\n<style="highlight">Coin Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)</style>\n[WhenUse] Gain +2 [Breath] Count
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], <style="highlight">Moc Końcowa +1</style> i zadaje <style="highlight">+15%</style> obrażeń\nMoc Monet +1 za każde <style="highlight">6</style> (suma własnej [Breath] i [Sinking] celu) (maks. 2)\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
573. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] 자신의 [Breath] 횟수 1 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1031401].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: <style="highlight">[CriticalOnSucceedAttack] Gain +1 [Breath] Count</style>
   PL: <style="highlight">[CriticalOnSucceedAttack] Zwiększa własny Licznik [Breath] o 1</style>
574. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 조,조용히 하시게
   źródło: Skills_personality-03.json :: dataList[id=1031402].levelList[level=1].name ; dataList[id=1031402].levelList[level=2].name ; dataList[id=1031402].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: B-be Thee Silent
   PL: C-cisza!
575. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 합 위력 +1\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031402].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetMarkToEnemy], [WhenUse], [Breath]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], Clash Power +1\n[WhenUse] Gain 3 [Breath]
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], Moc Starcia +1\n[WhenUse] Zyskuje 3 [Breath]
576. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +1 Licznika [Breath]
578. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 합 위력 +1\n<style="highlight">자신의 [Breath]과 대상의 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031402].levelList[level=2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], Clash Power +1\n<style="highlight">At 6+ ([Breath] on self + [Sinking] on target), Coin Power +1</style>\n[WhenUse] Gain 3 [Breath]
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], Moc Starcia +1\n<style="highlight">Przy 6+ (suma własnej [Breath] i [Sinking] celu) Moc Monet +1</style>\n[WhenUse] Zyskuje 3 [Breath]
579. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Sinking] 1 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1031402].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Sinking]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [Sinking]</style>
580. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031402].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031402].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1031402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje +1 Licznika [Breath]<style="highlight"></style>
582. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, <style="highlight">최종 위력 +1</style>\n자신의 [Breath]과 대상의 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031402].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], <style="highlight">Final Power +1</style>\n<style="highlight">Coin Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)</style>\n[WhenUse] Gain 3 [Breath]
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], <style="highlight">Moc Końcowa +1</style>\nMoc Monet +1 za każde <style="highlight">6</style> (suma własnej [Breath] i [Sinking] celu) (maks. 2)\n[WhenUse] Zyskuje 3 [Breath]
583. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 454 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] [Sinking] 횟수 1 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1031402].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Sinking]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict +1 [Sinking] Count</style>
   PL: <style="highlight">[CriticalOnSucceedAttack] Zwiększa Licznik [Sinking] celu o 1</style>
586. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 빠,빨리 지령을 수행해야만…
   źródło: Skills_personality-03.json :: dataList[id=1031403].levelList[level=3].name ; dataList[id=1031403].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 6 · monety: 2 (+6)
   limit: do 60 znaków
   EN: T-the Prescript Must be Fulfilled Anon...
   PL: N-nakaz musi być wypełniony natychmiast...
587. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 크리티컬 피해량 +20%\n자신의 [Breath]과 대상의 [Sinking]의 합 4당, 최종 위력 +1 (최대 2)\n[StartBattle] [UnlockBuff_Base] 단계가 2 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031403].levelList[level=3].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [StartBattle], [UnlockBuff_Base], [SuperCoin], [WhenUse]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [UnlockBuff_Base] = 해금 / Unlock; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +20% damage on Critical Hit\nFinal Power +1 for every 4 ([Breath] on self + [Sinking] on target) (max 2)\n[StartBattle] At 2+ [UnlockBuff_Base] stage, convert all Coins of this Skill to [SuperCoin]s\n[WhenUse] Gain +3 [Breath] Count
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje +20% obrażeń przy trafieniu krytycznym\nMoc Końcowa +1 za każde 4 (suma własnej [Breath] i [Sinking] celu) (maks. 2)\n[StartBattle] Przy 2+ poziomie [UnlockBuff_Base] wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin]\n[WhenUse] Zwiększa własny Licznik [Breath] o 3
588. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031403].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [UnlockBuff_Base] 단계 1당 피해량 +20% (최대 60%)
   źródło: Skills_personality-03.json :: dataList[id=1031403].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnlockBuff_Base]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock
   EN: Deal +20% damage for every [UnlockBuff_Base] stage (max 60%)
   PL: Zadaje +20% obrażeń za każdy 1 poziom [UnlockBuff_Base] (maks. 60%)
590. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031403].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] and +1 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada 2 [Sinking] i zwiększa Licznik [Sinking] o 1
591. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031403].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Sinking]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Sinking] = 침잠 / Sinking
   EN: [CriticalOnSucceedAttack] Inflict 1 [Sinking]
   PL: [CriticalOnSucceedAttack] Nakłada 1 [Sinking]
592. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, <style="highlight">코인 위력 +1</style>, 크리티컬 피해량 <style="highlight">+40%</style>\n자신의 [Breath]과 대상의 [Sinking]의 합 4당, 최종 위력 +1 (최대 <style="highlight">4</style>)\n[StartBattle] [UnlockBuff_Base] 단계가 2 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경되고 <style="highlight">[UnlockBuff_Base] 단계 1당 피해량 +20% (최대 60%)</style>\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n<style="highlight">- [UnlockBuff_Base] 단계만큼 [Breath] 추가로 얻음</style>
   źródło: Skills_personality-03.json :: dataList[id=1031403].levelList[level=4].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [StartBattle], [UnlockBuff_Base], [SuperCoin], [WhenUse]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [UnlockBuff_Base] = 해금 / Unlock; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], <style="highlight">Coin Power +1 and</style> deal +<style="highlight">40</style>% damage on Critical Hit\nFinal Power +1 for every 4 ([Breath] on self + [Sinking] on target) (max <style="highlight">4</style>)\n[StartBattle] At 2+ [UnlockBuff_Base] stage, convert all Coins of this Skill to [SuperCoin]s <style="highlight">and deal +20% damage for every [UnlockBuff_Base] stage (max 60%)</style>\n[WhenUse] Gain +3 [Breath] Count\n<style="highlight">- Gain [Breath] equal to current [UnlockBuff_Base] stage
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], <style="highlight">Moc Monet +1</style> i zadaje <style="highlight">+40</style>% obrażeń przy trafieniu krytycznym\nMoc Końcowa +1 za każde 4 (suma własnej [Breath] i [Sinking] celu) (maks. <style="highlight">4</style>)\n[StartBattle] Przy 2+ poziomie [UnlockBuff_Base] wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin] i <style="highlight">zadaje +20% obrażeń za każdy 1 poziom [UnlockBuff_Base] (maks. 60%)</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 3\n<style="highlight">- Zyskuje dodatkowo [Breath] równy obecnemu poziomowi [UnlockBuff_Base]</style>
593. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 2 [Breath]<style="highlight"></style>
594. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [UnlockBuff_Base] 단계 1당 피해량 <style="highlight">+40%</style> (최대 <style="highlight">120%</style>)
   źródło: Skills_personality-03.json :: dataList[id=1031403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnlockBuff_Base]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock
   EN: Deal <style="highlight">+40%</style> damage for every [UnlockBuff_Base] stage (max <style="highlight">120%</style>)
   PL: Zadaje <style="highlight">+40%</style> obrażeń za każdy 1 poziom [UnlockBuff_Base] (maks. <style="highlight">120%</style>)
595. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031403].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] and +1 [Sinking] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Sinking] i zwiększa Licznik [Sinking] o 1<style="highlight"></style>
596. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] [Sinking] 1 부여, <style="highlight">[Sinking] 횟수 1 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1031403].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Sinking]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Sinking] = 침잠 / Sinking
   EN: [CriticalOnSucceedAttack] Inflict 1 [Sinking] <style="highlight">and +1 [Sinking] Count</style>
   PL: [CriticalOnSucceedAttack] Nakłada 1 [Sinking] <style="highlight">i zwiększa Licznik [Sinking] o 1</style>
597. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — nazwa] 이 손으로 대신…
   źródło: Skills_personality-03.json :: dataList[id=1031405].levelList[level=1].name ; dataList[id=1031405].levelList[level=2].name ; dataList[id=1031405].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 2 (+4)
   limit: do 60 znaków
   EN: Let These Hands be the Proxy with Which...
   PL: Niech te ręce pełnią pełnomocnictwo…
598. [Umiejętność 4 (×0) (ulepszenie 1) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +10%\n[WhenUse] 자신의 [Breath] 횟수 1 증가\n[EndSkill] 정신력 3 감소 (턴당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1031405].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetMarkToEnemy], [WhenUse], [Breath], [EndSkill]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +10% damage\n[WhenUse] Gain +1 [Breath] Count\n[EndSkill] Lose 3 SP (2 times per turn)
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje +10% obrażeń\n[WhenUse] Zwiększa własny Licznik [Breath] o 1\n[EndSkill] Traci 3 Poczytalności (2 razy na turę)
599. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031405].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Umiejętność 4 (×0) (ulepszenie 2) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +10%\n<style="highlight">자신의 [Breath]과 대상의 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">2</style> 증가\n[EndSkill] 정신력 3 감소 (턴당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1031405].levelList[level=2].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse], [EndSkill]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +10% damage\n<style="highlight">At 6+ ([Breath] on self + [Sinking] on target), Coin Power +1</style>\n[WhenUse] Gain +<style="highlight">2</style> [Breath] Count\n[EndSkill] Lose 3 SP (2 times per turn)
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje +10% obrażeń\n<style="highlight">Przy 6+ (suma własnej [Breath] i [Sinking] celu) Moc Monet +1</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o <style="highlight">2</style>\n[EndSkill] Traci 3 Poczytalności (2 razy na turę)
602. [Umiejętność 4 (×0) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031405].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1031405].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Umiejętność 4 (×0) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031405].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1031405].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 506 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 <style="highlight">+15%</style>\n자신의 [Breath]과 대상의 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[EndSkill] 정신력 3 감소 (턴당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1031405].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse], [EndSkill]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +<style="highlight">15</style>% damage\n<style="highlight">Coin Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)</style>\n[WhenUse] Gain +2 [Breath] Count\n[EndSkill] Lose 3 SP (2 times per turn)
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje <style="highlight">+15</style>% obrażeń\nMoc Monet +1 za każde <style="highlight">6</style> (suma własnej [Breath] i [Sinking] celu) (maks. 2)\n[WhenUse] Zwiększa własny Licznik [Breath] o 2\n[EndSkill] Traci 3 Poczytalności (2 razy na turę)
605. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] 자신의 [Breath] 횟수 1 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1031405].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 573 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — nazwa] 대행: 새기기
   źródło: Skills_personality-03.json :: dataList[id=1031406].levelList[level=1].name ; dataList[id=1031406].levelList[level=2].name ; dataList[id=1031406].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Procuration: Engrave
   PL: Pełnomocnictwo: Wyrycie
607. [Umiejętność 5 (×0) (ulepszenie 1) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +5%\n[WhenUse] [Breath] 3 얻음\n[EndSkill] 정신력 6 감소 (턴당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1031406].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetMarkToEnemy], [WhenUse], [Breath], [EndSkill]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +5% damage\n[WhenUse] Gain 3 [Breath]\n[EndSkill] Lose 6 SP (2 times per turn)
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje +5% obrażeń\n[WhenUse] Zyskuje 3 [Breath]\n[EndSkill] Traci 6 Poczytalności (2 razy na turę)
608. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031406].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031406].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Umiejętność 5 (×0) (ulepszenie 2) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +5%\n<style="highlight">자신의 [Breath]과 대상의 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] [Breath] 3 얻음\n[EndSkill] 정신력 6 감소 (턴당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1031406].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse], [EndSkill]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +5% damage\n<style="highlight">At 6+ ([Breath] on self + [Sinking] on target), Coin Power +1</style>\n[WhenUse] Gain 3 [Breath]\n[EndSkill] Lose 6 SP (2 times per turn)
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje +5% obrażeń\n<style="highlight">Przy 6+ (suma własnej [Breath] i [Sinking] celu) Moc Monet +1</style>\n[WhenUse] Zyskuje 3 [Breath]\n[EndSkill] Traci 6 Poczytalności (2 razy na turę)
611. [Umiejętność 5 (×0) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Sinking] 2 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1031406].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[OnSucceedAttack] Inflict 2 [Sinking]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 2 [Sinking]</style>
612. [Umiejętność 5 (×0) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031406].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność 5 (×0) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031406].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1031406].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 581 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Umiejętność 5 (×0) (ulepszenie 4) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 <style="highlight">+10%</style>\n자신의 [Breath]과 대상의 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] [Breath] 3 얻음\n[EndSkill] 정신력 6 감소 (턴당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1031406].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse], [EndSkill]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +<style="highlight">10</style>% damage\n<style="highlight">Coin Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)</style>\n[WhenUse] Gain 3 [Breath]\n[EndSkill] Lose 6 SP (2 times per turn)
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje <style="highlight">+10</style>% obrażeń\nMoc Monet +1 za każde <style="highlight">6</style> (suma własnej [Breath] i [Sinking] celu) (maks. 2)\n[WhenUse] Zyskuje 3 [Breath]\n[EndSkill] Traci 6 Poczytalności (2 razy na turę)
615. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031406].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031406].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 454 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] [Sinking] 횟수 1 증가</style>
   źródło: Skills_personality-03.json :: dataList[id=1031406].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Umiejętność 6 (×0) (ulepszenia 3–4) — nazwa] 대행: 말살
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=3].name ; dataList[id=1031407].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 5 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Procuration: Annihilate
   PL: Pełnomocnictwo: Zaznaczenie
619. [Umiejętność 6 (×0) (ulepszenie 3) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 +15%\n자신의 [Breath]과 대상의 [Sinking]의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n[EndSkill] 정신력 15 감소 (턴당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=3].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse], [EndSkill]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +15% damage\nAt 6+ ([Breath] on self + [Sinking] on target), Coin Power +1\n[WhenUse] Gain +3 [Breath] Count\n[EndSkill] Lose 15 SP (2 times per turn)
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje +15% obrażeń\nPrzy 6+ (suma własnej [Breath] i [Sinking] celu) Moc Monet +1\n[WhenUse] Zwiększa własny Licznik [Breath] o 3\n[EndSkill] Traci 15 Poczytalności (2 razy na turę)
620. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 4, efekt 2 — opis] [UnlockBuff_Base] 단계 1당, 이 코인의 피해량 +20% (최대 60%)
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnlockBuff_Base]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock
   EN: This Coin deals +20% damage for every [UnlockBuff_Base] stage (max 60%)
   PL: Ta moneta zadaje +20% obrażeń za każdy 1 poziom [UnlockBuff_Base] (maks. 60%)
628. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=3].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 4, efekt 4 — opis] [CriticalOnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=3].coinlist[#3].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Sinking]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Sinking] = 침잠 / Sinking
   EN: [CriticalOnSucceedAttack] Inflict +1 [Sinking] Count
   PL: [CriticalOnSucceedAttack] Zwiększa Licznik [Sinking] celu o 1
630. [Umiejętność 6 (×0) (ulepszenie 4) — opis] 이 스킬에 [IndexPrescriptTargetMarkToEnemy]이 새겨졌으면, 피해량 <style="highlight">+25%</style>\n자신의 [Breath]과 대상의 [Sinking]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n<style="highlight">- [UnlockBuff_Base] 단계만큼 [Breath] 추가로 얻음</style>\n[EndSkill] 정신력 15 감소 (턴당 2회)
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=4].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [IndexPrescriptTargetMarkToEnemy], [Breath], [Sinking], [WhenUse], [UnlockBuff_Base], [EndSkill]
   znaczenie tagów: [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [UnlockBuff_Base] = 해금 / Unlock; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If this Skill is marked with [IndexPrescriptTargetMarkToEnemy], deal +<style="highlight">25</style>% damage\n<style="highlight">Coin Power +1 for every 6 ([Breath] on self + [Sinking] on target) (max 2)</style>\n[WhenUse] Gain +3 [Breath] Count\n<style="highlight">- Gain [Breath] equal to current [UnlockBuff_Base] stage</style>\n[EndSkill] Lose 15 SP (2 times per turn)
   PL: Jeżeli ta Umiejętność ma wyryte [IndexPrescriptTargetMarkToEnemy], zadaje <style="highlight">+25</style>% obrażeń\nMoc Monet +1 za każde <style="highlight">6</style> (suma własnej [Breath] i [Sinking] celu) (maks. 2)\n[WhenUse] Zwiększa własny Licznik [Breath] o 3\n<style="highlight">- Zyskuje dodatkowo [Breath] równy obecnemu poziomowi [UnlockBuff_Base]</style>\n[EndSkill] Traci 15 Poczytalności (2 razy na turę)
631. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 4, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 4, efekt 2 — opis] [UnlockBuff_Base] 단계 1당, 이 코인의 <style="highlight">위력 +1</style>, 피해량 <style="highlight">+40%</style> <style="highlight">(각각 최대 3, 최대 120%)</style>
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnlockBuff_Base]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock
   EN: This Coin gains <style="highlight">Power +1</style> and deals +<style="highlight">40</style>% damage for every [UnlockBuff_Base] stage <style="highlight">(max 3; max 120%)</style>
   PL: Ta moneta zyskuje <style="highlight">Moc +1</style> i zadaje +<style="highlight">40</style>% obrażeń za każdy 1 poziom [UnlockBuff_Base] <style="highlight">(maks. odpowiednio 3 i 120%)</style>
639. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=4].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 4, efekt 4 — opis] [CriticalOnSucceedAttack] [Sinking] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031407].levelList[level=4].coinlist[#3].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Sinking]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Sinking] = 침잠 / Sinking
   EN: [CriticalOnSucceedAttack] Inflict +<style="highlight">2</style> [Sinking] Count
   PL: [CriticalOnSucceedAttack] Zwiększa Licznik [Sinking] celu o <style="highlight">2</style>
641. [Obrona (ulepszenia 1,4) — nazwa] 지령이 하사한 지령으로 만들어진 천
   źródło: Skills_personality-03.json :: dataList[id=1031404].levelList[level=1].name ; dataList[id=1031404].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: kontra · moc bazowa: 3 · monety: 3 (+3)
   limit: do 60 znaków
   EN: Prescript-granted, Prescript-woven Fabric
   PL: Tkanina utkana z zesłanego Nakazu
642. [Obrona (ulepszenie 1) — opis] [UnlockBuff_Base] 단계 1당, 최종 위력 +1 (최대 3)\n[StartBattle] 자신의 최대 체력의 10%만큼 보호막 얻음 (턴당 1회)\n- [KarmaOfIndexAlly] 5당 이 효과로 얻는 보호막 수치가 1%씩 감소하여, [KarmaOfIndexAlly] 수치가 50 이상이면 보호막 얻지 않음\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[EndBattle] [UnlockBuff_Base]이 없으면, [UnlockBuffAlly_1] 얻음 (턴당 1회)\n- [BlessingOfIndexPrescriptAlly]가 3으로 변경됨\n- 증가한 [BlessingOfIndexPrescriptAlly] 1당 다음 턴 시작 시 [KarmaOfIndexAlly] 5 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031404].levelList[level=1].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_Base], [StartBattle], [KarmaOfIndexAlly], [WhenUse], [Breath], [EndBattle], [UnlockBuffAlly_1], [BlessingOfIndexPrescriptAlly]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [StartBattle] = [전투 시작시] / [Combat Start]; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndBattle] = [턴 종료 시] / [Turn End]; [UnlockBuffAlly_1] = 해금 - I / Unlock - I; [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript
   EN: Final Power +1 for every [UnlockBuff_Base] stage (max 3)\n[StartBattle] Gain Shield equal to 10% of max HP (once per turn)\n- Reduce Shield gained by 1% for every 5 [KarmaOfIndexAlly]; at 50+ [KarmaOfIndexAlly], does not gain Shield\n[WhenUse] Gain +2 [Breath] Count\n[EndBattle] If this unit does not have [UnlockBuff_Base], gain [UnlockBuffAlly_1] (once per turn)\n- Change [BlessingOfIndexPrescriptAlly] Stack to 3\n- Gain 5 [KarmaOfIndexAlly] at next Turn Start for every [BlessingOfIndexPrescriptAlly] gained
   PL: Moc Końcowa +1 za każdy 1 poziom [UnlockBuff_Base] (maks. 3)\n[StartBattle] Zyskuje Tarczę równą 10% Maks. HP (1 raz na turę)\n- Za każde 5 [KarmaOfIndexAlly] wartość Tarczy uzyskiwanej tym efektem maleje o 1%; przy 50+ [KarmaOfIndexAlly] nie zyskuje Tarczy\n[WhenUse] Zwiększa własny Licznik [Breath] o 2\n[EndBattle] Jeżeli ta jednostka nie ma [UnlockBuff_Base], zyskuje [UnlockBuffAlly_1] (1 raz na turę)\n- Zmienia stos [BlessingOfIndexPrescriptAlly] na 3\n- Na początku następnej tury zyskuje 5 [KarmaOfIndexAlly] za każdy 1 zyskanej [BlessingOfIndexPrescriptAlly]
643. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Obrona (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031404].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Obrona (ulepszenie 4) — opis] [UnlockBuff_Base] 단계 1당, 최종 위력 +1, <style="highlight">피해량 +15%</style> (각각 최대 3, <style="highlight">최대 45%</style>)\n[StartBattle] 자신의 최대 체력의 <style="highlight">15%</style>만큼 보호막 얻음 (턴당 1회)\n- [KarmaOfIndexAlly] 5당 이 효과로 얻는 보호막 수치가 <style="highlight">1.5%</style>씩 감소하여, [KarmaOfIndexAlly] 수치가 50 이상이면 보호막 얻지 않음\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[EndBattle] [UnlockBuff_Base]이 없으면, [UnlockBuffAlly_1] 얻음 (턴당 1회)\n- [BlessingOfIndexPrescriptAlly]가 3으로 변경됨\n- 증가한 [BlessingOfIndexPrescriptAlly] 1당 다음 턴 시작 시 [KarmaOfIndexAlly] 5 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031404].levelList[level=4].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [UnlockBuff_Base], [StartBattle], [KarmaOfIndexAlly], [WhenUse], [Breath], [EndBattle], [UnlockBuffAlly_1], [BlessingOfIndexPrescriptAlly]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [StartBattle] = [전투 시작시] / [Combat Start]; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndBattle] = [턴 종료 시] / [Turn End]; [UnlockBuffAlly_1] = 해금 - I / Unlock - I; [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript
   EN: Final Power +1 <style="highlight">and deal +15% damage</style> for every [UnlockBuff_Base] stage (max 3; <style="highlight">max 45%</style>)\n[StartBattle] Gain Shield equal to <style="highlight">15</style>% of max HP (once per turn)\n- Reduce Shield gained by <style="highlight">1.5</style>% for every 5 [KarmaOfIndexAlly]; at 50+ [KarmaOfIndexAlly], does not gain Shield\n[WhenUse] Gain +2 [Breath] Count\n[EndBattle] If this unit does not have [UnlockBuff_Base], gain [UnlockBuffAlly_1] (once per turn)\n- Change [BlessingOfIndexPrescriptAlly] Stack to 3\n- Gain 5 [KarmaOfIndexAlly] at next Turn Start for every [BlessingOfIndexPrescriptAlly] gained
   PL: Moc Końcowa +1 i <style="highlight">zadaje +15% obrażeń</style> za każdy 1 poziom [UnlockBuff_Base] (maks. 3; <style="highlight">maks. 45%</style>)\n[StartBattle] Zyskuje Tarczę równą <style="highlight">15</style>% Maks. HP (1 raz na turę)\n- Za każde 5 [KarmaOfIndexAlly] wartość Tarczy uzyskiwanej tym efektem maleje o <style="highlight">1.5%</style>; przy 50+ [KarmaOfIndexAlly] nie zyskuje Tarczy\n[WhenUse] Zwiększa własny Licznik [Breath] o 2\n[EndBattle] Jeżeli ta jednostka nie ma [UnlockBuff_Base], zyskuje [UnlockBuffAlly_1] (1 raz na turę)\n- Zmienia stos [BlessingOfIndexPrescriptAlly] na 3\n- Na początku następnej tury zyskuje 5 [KarmaOfIndexAlly] za każdy 1 zyskanej [BlessingOfIndexPrescriptAlly]
646. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031404].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 571 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Sinking] 1 부여</style>
   źródło: Skills_personality-03.json :: dataList[id=1031404].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 579 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Obrona (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031404].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Obrona (ulepszenia 1,4) — nazwa] 강제 해금
   źródło: Skills_personality-03.json :: dataList[id=1031408].levelList[level=1].name ; dataList[id=1031408].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: kontra · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Compulsory Unlock
   PL: Przymusowe Odblokowanie
650. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] [Breath] 3 얻음\n[EndBattle] [UnlockBuff_Base]이 3 미만이면, 다음 효과 발동 (턴당 1회)\n- 자신에게 [UnlockBuff_Base]이 있으면, 단계 1 증가\n- 6/9 미만인 [BlessingOfIndexPrescriptAlly]가 6/9로 변경됨\n- 증가한 [BlessingOfIndexPrescriptAlly] 1당 다음 턴 시작 시 [KarmaOfIndexAlly] 5 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031408].levelList[level=1].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Breath], [EndBattle], [UnlockBuff_Base], [BlessingOfIndexPrescriptAlly], [KarmaOfIndexAlly]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndBattle] = [턴 종료 시] / [Turn End]; [UnlockBuff_Base] = 해금 / Unlock; [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence
   EN: [DuelCounter]\n[WhenUse] Gain 3 [Breath]\n[EndBattle] At lower than stage 3 [UnlockBuff_Base], activate the following (once per turn):\n- If this unit has [UnlockBuff_Base], increase it by 1 stage\n- At less than 6/9 [BlessingOfIndexPrescriptAlly], change its Stack to 6/9\n- Gain 5 [KarmaOfIndexAlly] at next Turn Start for every [BlessingOfIndexPrescriptAlly] gained
   PL: [DuelCounter]\n[WhenUse] Zyskuje 3 [Breath]\n[EndBattle] Poniżej 3 poziomu [UnlockBuff_Base] uruchamia następujące efekty (1 raz na turę):\n- Jeżeli ta jednostka ma [UnlockBuff_Base], zwiększa ją o 1 poziom\n- [BlessingOfIndexPrescriptAlly] poniżej 6/9 zmienia się na 6/9\n- Na początku następnej tury zyskuje 5 [KarmaOfIndexAlly] za każdy 1 zyskanej [BlessingOfIndexPrescriptAlly]
651. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031408].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Obrona (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031408].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n<style="highlight">[UnlockBuff_Base] 단계 1당, 최종 위력 +1 (최대 3)</style>\n[WhenUse] [Breath] 3 얻음\n[EndBattle] [UnlockBuff_Base]이 3 미만이면, 다음 효과 발동 (턴당 1회)\n- 자신에게 [UnlockBuff_Base]이 있으면, 단계 1 증가\n- 6/9 미만인 [BlessingOfIndexPrescriptAlly]가 6/9로 변경됨\n- 증가한 [BlessingOfIndexPrescriptAlly] 1당 다음 턴 시작 시 [KarmaOfIndexAlly] 5 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031408].levelList[level=4].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [UnlockBuff_Base], [WhenUse], [Breath], [EndBattle], [BlessingOfIndexPrescriptAlly], [KarmaOfIndexAlly]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [UnlockBuff_Base] = 해금 / Unlock; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndBattle] = [턴 종료 시] / [Turn End]; [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence
   EN: [DuelCounter]\n<style="highlight">Final Power +1 for every [UnlockBuff_Base] stage (max 3)</style>\n[WhenUse] Gain 3 [Breath]\n[EndBattle] At lower than stage 3 [UnlockBuff_Base], activate the following (once per turn):\n- If this unit has [UnlockBuff_Base], increase it by 1 stage\n- At less than 6/9 [BlessingOfIndexPrescriptAlly], change its Stack to 6/9\n- Gain 5 [KarmaOfIndexAlly] at next Turn Start for every [BlessingOfIndexPrescriptAlly] gained
   PL: [DuelCounter]\n<style="highlight">Moc Końcowa +1 za każdy 1 poziom [UnlockBuff_Base] (maks. 3)</style>\n[WhenUse] Zyskuje 3 [Breath]\n[EndBattle] Poniżej 3 poziomu [UnlockBuff_Base] uruchamia następujące efekty (1 raz na turę):\n- Jeżeli ta jednostka ma [UnlockBuff_Base], zwiększa ją o 1 poziom\n- [BlessingOfIndexPrescriptAlly] poniżej 6/9 zmienia się na 6/9\n- Na początku następnej tury zyskuje 5 [KarmaOfIndexAlly] za każdy 1 zyskanej [BlessingOfIndexPrescriptAlly]
654. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031408].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Obrona (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031408].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Pasywka bojowa (od ulepszenia 1) — nazwa] 단말기로 전해진 지령
   źródło: Passives.json :: dataList[id=1031402].name
   limit: do 50 znaków
   EN: Prescript Delivered on a Device
   PL: Nakaz Przekazany Terminalem
657. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 시작 시\n- 자신의 [UnlockBuff_Base] 단계에 따라 [IndexPrescriptDon_0] / [IndexPrescriptDon_1] / [IndexPrescriptDon_2] / [IndexPrescriptDon_3] 얻음\n- 무작위 적 1명에게 [IndexPrescriptTargetToEnemy] 부여 (집중 전투면, 부위에 부여)\n- 조작 슬롯의 자신의 기본 공격 스킬에 [IndexPrescriptTargetMarkToEnemy] 부여 (슬롯당 1개, 최대 2개 부여)\n· [UnlockBuffAlly_2] 이상이면, 스킬 3에 우선 부여\n- 흐트러짐, 행동 불가[TabExplain], 패닉, E.G.O 침식 상태면, 위의 모든 효과와 [IndexPrescript_Base_2nd] 수행 여부가 적용되지 않음\n\n턴 시작 시 [UnlockBuffAlly_3]이면, [Blandishment_Shin] 얻음
   źródło: Passives.json :: dataList[id=1031402].desc
   limit: do 870 znaków
   tokeny: zachowaj dokładnie: \n, [UnlockBuff_Base], [IndexPrescriptDon_0], [IndexPrescriptDon_1], [IndexPrescriptDon_2], [IndexPrescriptDon_3], [IndexPrescriptTargetToEnemy], [IndexPrescriptTargetMarkToEnemy], [UnlockBuffAlly_2], [TabExplain], [IndexPrescript_Base_2nd], [UnlockBuffAlly_3], [Blandishment_Shin]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [IndexPrescriptDon_0] = 지령[단말기] I / Prescript: [Device] I; [IndexPrescriptDon_1] = 지령[단말기] II / Prescript: [Device] II; [IndexPrescriptDon_2] = 지령[단말기] III / Prescript: [Device] III; [IndexPrescriptDon_3] = 지령[단말기] IV / Prescript: [Device] IV; [IndexPrescriptTargetToEnemy] = 지령 대상 / The Prescript's Target; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [UnlockBuffAlly_2] = 해금 - II / Unlock - II …
   EN: Turn Start:\n- Gain [IndexPrescriptDon_0] / [IndexPrescriptDon_1] / [IndexPrescriptDon_2] / [IndexPrescriptDon_3] based on [UnlockBuff_Base] stage on self\n- Inflict [IndexPrescriptTargetToEnemy] to a random enemy (in Focused Encounters, the Part)\n- Apply [IndexPrescriptTargetMarkToEnemy] to Base Attack Skills on this unit's Dashboard (1 per Slot, max 2 Skills)\n· At [UnlockBuffAlly_2]+, the effect above prioritizes Skill 3\n- All of the effects above and [IndexPrescript_Base_2nd] execution checks do not trigger when this unit is Staggered, Immobilized[TabExplain], in Panic, or in E.G.O Corrosion[TabExplain]\n\nIf this unit has [UnlockBuffAlly_3] at Turn Start, gain [Blandishment_Shin]
   PL: Na początku tury\n- Zyskuje [IndexPrescriptDon_0] / [IndexPrescriptDon_1] / [IndexPrescriptDon_2] / [IndexPrescriptDon_3] zależnie od poziomu [UnlockBuff_Base]\n- Nakłada [IndexPrescriptTargetToEnemy] na 1 losowego wroga (w walce skupionej: na część ciała)\n- Nakłada [IndexPrescriptTargetMarkToEnemy] na własne podstawowe Umiejętności ataku w Panelu Sterowania (1 na slot, maks. 2 Umiejętności)\n· Przy [UnlockBuffAlly_2]+ efekt nakłada najpierw na Umiejętność 3\n- Jeżeli ta jednostka jest Ogłuszona, Niezdolna do działania[TabExplain], w Panice lub w Korozji E.G.O[TabExplain], żaden z powyższych efektów ani warunek wykonania [IndexPrescript_Base_2nd] nie działa\n\nNa początku tury przy [UnlockBuffAlly_3] zyskuje [Blandishment_Shin]
658. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 지령 얻음\n무작위 적에 지령 대상 부여\n자신의 무작위 기본 공격 스킬에 지령 표식 부여
   źródło: Passives.json :: dataList[id=1031402].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Prescript\nInflict The Prescript's Target to random target\nApply Mark of the Prescript on a Base Attack Skill
   PL: Zyskuje Nakaz\nNakłada Cel Nakazu na losowego wroga\nNakłada Znak Nakazu na losową własną podstawową Umiejętność ataku
659. [Pasywka bojowa (od ulepszenia 1) — nazwa] 지령의 뜻
   źródło: Passives.json :: dataList[id=1031403].name
   limit: do 40 znaków
   EN: Will of the Prescript
   PL: Wola Nakazu
660. [Pasywka bojowa (od ulepszenia 1) — opis] 이번 턴에 [IndexPrescript_Base_2nd]을 수행했으면,\n턴 종료 시 정신력 4 회복, [BlessingOfIndexPrescriptAlly] 1 얻음 (턴당 1회)\n- [IndexPrescript_Base_2nd] 수행 시 메인 타겟에게 [IndexPrescriptTargetToEnemy]이 있으면,\n대신 정신력 8 회복, [BlessingOfIndexPrescriptAlly] 3 얻음\n\n이번 턴에 [IndexPrescript_Base_2nd]을 수행하지 못했으면,\n 턴 종료 시 [KarmaOfIndexAlly] 5 얻음\n- [UnlockBuffAlly_3]이면, [KarmaOfIndexAlly]를 얻지 않음\n- 전투 시작 시 [IndexPrescript_Base_2nd] 수행을 시도했으나, 전투 중에 대상을 타겟할 수 없게 되었으면, 턴 종료 시 [KarmaOfIndexAlly]를 얻지 않음
   źródło: Passives.json :: dataList[id=1031403].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescript_Base_2nd], [BlessingOfIndexPrescriptAlly], [IndexPrescriptTargetToEnemy], [KarmaOfIndexAlly], [UnlockBuffAlly_3]
   znaczenie tagów: [IndexPrescript_Base_2nd] = 지령 / Prescript; [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [IndexPrescriptTargetToEnemy] = 지령 대상 / The Prescript's Target; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [UnlockBuffAlly_3] = 해금 - III / Unlock - III
   EN: Turn End: If [IndexPrescript_Base_2nd] was executed this turn, heal 4 SP and gain 1 [BlessingOfIndexPrescriptAlly] (once per turn)\n- When executing [IndexPrescript_Base_2nd], if the main target has [IndexPrescriptTargetToEnemy], heal 8 SP and gain 3 [BlessingOfIndexPrescriptAlly] instead\n\nTurn End: If [IndexPrescript_Base_2nd] was not executed this turn, gain 5 [KarmaOfIndexAlly]\n- At [UnlockBuffAlly_3], does not gain [KarmaOfIndexAlly]\n- If this unit attempted to execute [IndexPrescript_Base_2nd] at Combat Start, but could not target the enemy during the combat phase, does not gain [KarmaOfIndexAlly] at Turn End
   PL: Na koniec tury: jeżeli [IndexPrescript_Base_2nd] został wykonany w tej turze, odzyskuje 4 Poczytalności i zyskuje 1 [BlessingOfIndexPrescriptAlly] (1 raz na turę)\n- Jeżeli przy wykonywaniu [IndexPrescript_Base_2nd] główny cel ma [IndexPrescriptTargetToEnemy], zamiast tego odzyskuje 8 Poczytalności i zyskuje 3 [BlessingOfIndexPrescriptAlly]\n\nNa koniec tury: jeżeli [IndexPrescript_Base_2nd] nie został wykonany w tej turze, zyskuje 5 [KarmaOfIndexAlly]\n- Przy [UnlockBuffAlly_3] nie zyskuje [KarmaOfIndexAlly]\n- Jeżeli ta jednostka próbowała wykonać [IndexPrescript_Base_2nd] na początku walki, ale nie mogła namierzyć celu podczas walki, nie zyskuje [KarmaOfIndexAlly]
661. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 지령 수행 시, 정신력 회복하고 지령의 가호 얻음\n지령 실패 시, 카르마 얻음
   źródło: Passives.json :: dataList[id=1031403].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upon executing Prescript, heal SP and gain Grace of the Prescript\nUpon failing Prescript, gain Karmic Consequence
   PL: Po wykonaniu Nakazu odzyskuje Poczytalność i zyskuje Łaskę Nakazu\nPo nieudanym Nakazie zyskuje Karmę
662. [Pasywka bojowa (od ulepszenia 1) — nazwa] 해금/개화 E.G.O::대행
   źródło: Passives.json :: dataList[id=1031404].name
   limit: do 60 znaków
   EN: Unlock / Effloresced E.G.O::Procuration
   PL: Odblokowanie / Rozkwita E.G.O::Pełnomocnictwo
663. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 종료 시 [BlessingOfIndexPrescriptAlly]가 3/6/9이면, [UnlockBuffAlly_1]/[UnlockBuffAlly_2]/[UnlockBuffAlly_3] 얻음\n\n[UnlockBuffAlly_1]을 얻으면, 정신력을 15 소모하여 <noparse>개화</noparse> E.G.O::대행 상태가 됨\n- 정신력 소모 전 정신력이 25까지 증가하고 (증가한 정신력/5)만큼 [KarmaOfIndexAlly] 얻음 (소수점 올림)\n- 이후 턴 시작 시 [UnlockBuff_Base]이 있고, 정신력이 25 이상이면,\n정신력을 15 소모하여 해당 상태가 됨\n\n<noparse>개화</noparse> E.G.O::대행 상태가 될 때,\n- 해당 턴의 흐트러짐 해제\n(해제할 수 없는 흐트러짐이면 해당 상태가 될 수 없음)\n- 해당 상태일 때, [Blandishment] 얻음\n\n턴 시작 시 정신력이 0 이하면, 해당 상태 해제
   źródło: Passives.json :: dataList[id=1031404].desc
   limit: do 1050 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [BlessingOfIndexPrescriptAlly], [UnlockBuffAlly_1], [UnlockBuffAlly_2], [UnlockBuffAlly_3], [KarmaOfIndexAlly], [UnlockBuff_Base], [Blandishment]
   znaczenie tagów: [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [UnlockBuffAlly_1] = 해금 - I / Unlock - I; [UnlockBuffAlly_2] = 해금 - II / Unlock - II; [UnlockBuffAlly_3] = 해금 - III / Unlock - III; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [UnlockBuff_Base] = 해금 / Unlock; [Blandishment] = 당연한 믿음 / Faith Beyond Question
   EN: Turn End: At 3/6/9 [BlessingOfIndexPrescriptAlly], gain [UnlockBuffAlly_1]/[UnlockBuffAlly_2]/[UnlockBuffAlly_3].\n\nIf this unit gained [UnlockBuffAlly_1], consume 15 SP to enter <noparse>Effloresced</noparse> E.G.O::Procuration state:\n- Before consuming SP to enter this state, heal SP to 25 and gain [KarmaOfIndexAlly] equal to (SP healed / 5) (rounded up)\n- At Turn Start after the above checks, if this unit has [UnlockBuff_Base] and is at 25+ SP, consume 15 SP to enter this state\n\n- If this unit gets Staggered when entering <noparse>Effloresced</noparse> E.G.O::Procuration state, recover from Stagger (if this unit's Stagger cannot be naturally recovered from, does not enter <noparse>Effloresced</noparse> E.G.O::Procuration state)\n- Gain [Blandishment] while in <noparse>Effloresced</noparse> EGO::Procuration state\n\nTurn Start: At 0 or less SP, this unit exits <noparse>Effloresced</noparse> E.G.O::Procuration state
   PL: Na koniec tury przy 3/6/9 [BlessingOfIndexPrescriptAlly] zyskuje [UnlockBuffAlly_1]/[UnlockBuffAlly_2]/[UnlockBuffAlly_3].\n\nGdy ta jednostka zyska [UnlockBuffAlly_1], zużywa 15 Poczytalności, by wejść w stan <noparse>Rozkwita</noparse> E.G.O::Pełnomocnictwo:\n- Przed zużyciem Poczytalności odzyskuje ją do 25 i zyskuje [KarmaOfIndexAlly] równy (odzyskane Poczytalności / 5) (zaokrąglone w górę)\n- Na początku następnej tury, jeżeli ta jednostka ma [UnlockBuff_Base] i ma 25+ Poczytalności, zużywa 15 Poczytalności, by wejść w ten stan\n\nWchodząc w stan <noparse>Rozkwita</noparse> E.G.O::Pełnomocnictwo:\n- Dochodzi do siebie z Ogłuszenia w tej turze\n(jeżeli Ogłuszenia nie da się naturalnie usunąć, ta jednostka nie wchodzi w stan <noparse>Rozkwita</noparse> E.G.O::Pełnomocnictwo)\n- W tym stanie zyskuje [Blandishment]\n\nNa początku tury przy Poczytalności 0 lub niższej ta jednostka wychodzi ze stanu <noparse>Rozkwita</noparse> E.G.O::Pełnomocnictwo
664. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Lust, posiadane 1× Gloom, posiadane 1× Pride) — nazwa] 역시 마법의 삐삐님은 본인이 원하는 걸 알아주시는 군!
   źródło: Passives.json :: dataList[id=1031401].name
   limit: do 60 znaków
   EN: The Great Magicked Beeper Knoweth My Desire!
   PL: Wielka Magiczna Brzęczydzwonko zna moje pragnienia!
665. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Lust, posiadane 1× Gloom, posiadane 1× Pride) — opis] 자신의 [BlessingOfIndexPrescriptAlly] 1당 [IndexPrescriptTargetMarkToEnemy] 스킬 피해량 +2% (최대 16%)\n- [BlessingOfIndexPrescriptAlly]가 9면, 대신 기본 스킬의 피해량 +20%\n\n[IndexPrescriptTargetToEnemy]이 있는 대상에게 기본 스킬 공격 적중 시,\n정신력 3 회복 (스킬당 1회, 턴당 2회)\n- [UnlockBuff_Base] 단계만큼 정신력 추가 회복
   źródło: Passives.json :: dataList[id=1031401].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [BlessingOfIndexPrescriptAlly], [IndexPrescriptTargetMarkToEnemy], [IndexPrescriptTargetToEnemy], [UnlockBuff_Base]
   znaczenie tagów: [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [IndexPrescriptTargetMarkToEnemy] = 지령 표식 / Mark of the Prescript; [IndexPrescriptTargetToEnemy] = 지령 대상 / The Prescript's Target; [UnlockBuff_Base] = 해금 / Unlock
   EN: Deal +2% damage using Skills marked with [IndexPrescriptTargetMarkToEnemy] for every [BlessingOfIndexPrescriptAlly] on self (max 16%)\n- At 9 [BlessingOfIndexPrescriptAlly], deal +20% damage using Base Skills instead\n\nOn hit using Base Skill attacks against targets that have [IndexPrescriptTargetToEnemy], heal 3 SP (once per Skill; 2 times per turn)\n- Heal additional SP based on [UnlockBuff_Base] stage
   PL: Zadaje +2% obrażeń Umiejętnościami z [IndexPrescriptTargetMarkToEnemy] za każdy 1 [BlessingOfIndexPrescriptAlly] (maks. 16%)\n- Przy 9 [BlessingOfIndexPrescriptAlly] zamiast tego zadaje +20% obrażeń podstawowymi Umiejętnościami\n\nPrzy trafieniu podstawową Umiejętnością ataku w cel z [IndexPrescriptTargetToEnemy] odzyskuje 3 Poczytalności (1 raz na Umiejętność, 2 razy na turę)\n- Odzyskuje dodatkowe Poczytalności równe poziomowi [UnlockBuff_Base]
666. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Lust, posiadane 1× Gloom, posiadane 1× Pride) — podsumowanie] 지령 표식이 새겨진 스킬이면, 지령의 가호에 비례하여 피해량이 증가\n적중 시 정신력 회복
   źródło: Passives.json :: dataList[id=1031401].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skills marked with Mark of the Prescript deal more damage based on Grace of the Prescript Stack\nOn Hit, heal SP
   PL: Umiejętności z wyrytym Znakiem Nakazu zadają więcej obrażeń proporcjonalnie do Łaski Nakazu\nPrzy trafieniu odzyskuje Poczytalność
667. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — nazwa] 이 또한 마법의 삐삐님의 은혜일테지
   źródło: Passives.json :: dataList[id=1031421].name
   limit: do 80 znaków
   EN: This, too, is the Grace of the Great Magicked Beeper!
   PL: To również łaska Wielkiej Magicznej Brzęczydzwonko!
668. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — opis] 전투 시작 시, 정신력이 가장 낮은 아군 1명의 정신력 15 회복\n- 더하기 코인을 사용하는 인격에게 우선으로 적용\n- 대상이 검지 소속이면 효과가 강화되어 추가로 [AttackDmgUp] 1 부여\n- 침식, 패닉 등 정신력을 회복할 수 없는 대상에게는 적용되지 않음
   źródło: Passives.json :: dataList[id=1031421].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDmgUp], [TabExplain]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Combat Start: Heal 15 SP for the ally that has the lowest SP\n- This effect prioritizes Plus Coin Identities\n- If the affected unit is in The Index faction, they gain 1 [AttackDmgUp] as well\n- This effect does not apply to units under effects that prevent SP recovery such as E.G.O Corrosion[TabExplain], Panic, etc.
   PL: Na początku walki odzyskuje 15 Poczytalności sojusznika z najniższą Poczytalnością\n- Efekt najpierw dotyczy Tożsamości używających monet Plus\n- Jeżeli taką jednostką jest członek frakcji Wskazującego, efekt się wzmacnia: dodatkowo nakłada 1 [AttackDmgUp]\n- Nie działa na jednostki, które nie mogą odzyskać Poczytalności (np. Korozja E.G.O[TabExplain], Panika)

## [000] Haute Couture:: Le Noir Brand Manager — Don Quixote — 오트쿠튀르:: 르누아르 브랜드 매니저
- ID Tożsamości: `10315` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 8 · HP bazowe: 88 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Charge, Tremor

669. [Karta Tożsamości — tytuł] 오트쿠튀르::\n르누아르\n브랜드 매니저
   źródło: Personalities.json :: dataList[id=10315].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Haute Couture::\nLe Noir\nBrand Manager
   PL: Haute Couture::\nLe Noir\nMenadżerka Marki
670. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10315].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10315].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Karta Tożsamości — opis] 돈키호테의 열다섯번째 인격
   źródło: Personalities.json :: dataList[id=10315].desc
   limit: do 120 znaków
   EN: Don Quixote’s 15th Identity
   PL: Piętnasta Tożsamość Don Quixote
673. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 못 박히라
   źródło: Skills_personality-03.json :: dataList[id=1031501].levelList[level=1].name ; dataList[id=1031501].levelList[level=2].name ; dataList[id=1031501].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Cometh the Nail
   PL: Niech Wbije się Gwóźdź
674. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1\n[WhenUse] 자신과 자신을 제외한 [Charge] 횟수가 가장 적은 르누아르 소속 아군 인격 1명의 [Charge] 횟수 2 증가 (턴당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031501].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoirAlly], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation; [Charge] = 충전 / Charge
   EN: [WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1\n[WhenUse] Apply +2 [Charge] Count on self and 1 other "Le Noir" allied Identity that has the lowest [Charge] Count (once per turn)
   PL: [WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1\n[WhenUse] Nakłada +2 Licznika [Charge] na siebie i 1 inną Tożsamość sojuszniczą „Le Noir” z najmniejszym Licznikiem [Charge] (1 raz na turę)
675. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031501].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1031501].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1031501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Vibration]
676. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 4 증가
   źródło: Skills_personality-03.json :: dataList[id=1031501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +4 [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zyskuje +4 Licznika [ChargeNoirAlly]
677. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Vibration] 위력과 [NoirNailDonQuixote]의 합 4당, 최종 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, <style="highlight">피해량 +20%</style>\n[WhenUse] 자신과 자신을 제외한 [Charge] 횟수가 가장 적은 르누아르 소속 아군 인격 1명의 [Charge] 횟수 <style="highlight">3</style> 증가 (턴당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031501].levelList[level=2].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [NoirNailDonQuixote], [ChargeNoirAlly], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [ChargeNoirAlly] = 보존 / Preservation; [Charge] = 충전 / Charge
   EN: <style="highlight">[WhenUse] Final Power +1 for every 4 ([Vibration] Potency + [NoirNailDonQuixote]) on target (max 2)</style>\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 <style="highlight">and deal +20% damage</style>\n[WhenUse] Apply +<style="highlight">3</style> [Charge] Count on self and 1 other "Le Noir" allied Identity that has the lowest [Charge] Count (once per turn)
   PL: <style="highlight">[WhenUse] Moc Końcowa +1 za każde 4 (suma Mocy [Vibration] i [NoirNailDonQuixote] celu) (maks. 2)</style>\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i <style="highlight">zadaje +20% obrażeń</style>\n[WhenUse] Nakłada +<style="highlight">3</style> Licznika [Charge] na siebie i 1 inną Tożsamość sojuszniczą „Le Noir” z najmniejszym Licznikiem [Charge] (1 raz na turę)
678. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">5</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031501].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +<style="highlight">5</style> [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">5</style>
679. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 [Vibration] 위력과 [NoirNailDonQuixote]의 합 4당, 최종 위력 +1 (최대 <style="highlight">3</style>)\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, 피해량 +<style="highlight">40%</style>\n[WhenUse] 자신과 자신을 제외한 [Charge] 횟수가 가장 적은 르누아르 소속 아군 인격 1명의 [Charge] 횟수 <style="highlight">4</style> 증가 (턴당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031501].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [NoirNailDonQuixote], [ChargeNoirAlly], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [ChargeNoirAlly] = 보존 / Preservation; [Charge] = 충전 / Charge
   EN: [WhenUse] Final Power +1 for every 4 ([Vibration] Potency + [NoirNailDonQuixote]) on target (max <style="highlight">3</style>)\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 and deal +<style="highlight">40</style>% damage\n[WhenUse] Apply +<style="highlight">4</style> [Charge] Count on self and 1 other "Le Noir" allied Identity that has the lowest [Charge] Count (once per turn)
   PL: [WhenUse] Moc Końcowa +1 za każde 4 (suma Mocy [Vibration] i [NoirNailDonQuixote] celu) (maks. <style="highlight">3</style>)\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i zadaje +<style="highlight">40</style>% obrażeń\n[WhenUse] Nakłada +<style="highlight">4</style> Licznika [Charge] na siebie i 1 inną Tożsamość sojuszniczą „Le Noir” z najmniejszym Licznikiem [Charge] (1 raz na turę)
680. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">6</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +<style="highlight">6</style> [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">6</style>
681. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 못 생기라
   źródło: Skills_personality-03.json :: dataList[id=1031502].levelList[level=1].name ; dataList[id=1031502].levelList[level=2].name ; dataList[id=1031502].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 6 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Summoneth the Nail
   PL: Niech Gwóźdź Się Przyzwie
682. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1
   źródło: Skills_personality-03.json :: dataList[id=1031502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ChargeNoirAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1
   PL: [WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1
683. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [NoirNailDonQuixote] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031502].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1031502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1031502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NoirNailDonQuixote]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NoirNailDonQuixote] = 약속된 못 / Promised Nail
   EN: [OnSucceedAttack] Inflict 1 [NoirNailDonQuixote]
   PL: [OnSucceedAttack] Nakłada 1 [NoirNailDonQuixote]
684. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-03.json :: dataList[id=1031502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 6 증가
   źródło: Skills_personality-03.json :: dataList[id=1031502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +6 [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zyskuje +6 Licznika [ChargeNoirAlly]
686. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031502].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1031502].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1031502].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Vibration]
687. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-03.json :: dataList[id=1031502].levelList[level=1].coinlist[#1].coindescs[#2].desc ; dataList[id=1031502].levelList[level=2].coinlist[#1].coindescs[#2].desc ; dataList[id=1031502].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
688. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Vibration] 위력과 [NoirNailDonQuixote]의 합 4당, 최종 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, <style="highlight">피해량 +20%</style>\n<style="highlight">[BeforeAttack] 최대 공명 수 1당, 마지막 코인의 최종 위력 +1 (최대 4)</style>
   źródło: Skills_personality-03.json :: dataList[id=1031502].levelList[level=2].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [NoirNailDonQuixote], [ChargeNoirAlly], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [ChargeNoirAlly] = 보존 / Preservation; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: <style="highlight">[WhenUse] Final Power +1 for every 4 ([Vibration] Potency + [NoirNailDonQuixote]) on target (max 2)</style>\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 <style="highlight">and deal +20% damage</style>\n<style="highlight">[BeforeAttack] The final Coin gains Final Power +1 for every highest Reson. (max 4)</style>
   PL: <style="highlight">[WhenUse] Moc Końcowa +1 za każde 4 (suma Mocy [Vibration] i [NoirNailDonQuixote] celu) (maks. 2)</style>\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i <style="highlight">zadaje +20% obrażeń</style>\n<style="highlight">[BeforeAttack] Moc Końcowa ostatniej monety +1 za każde 1 najwyższego Rezonansu (maks. 4)</style>
689. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031502].levelList[level=2].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">7</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031502].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +<style="highlight">7</style> [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">7</style>
691. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Vibration] 위력과 [NoirNailDonQuixote]의 합 4당, 최종 위력 +1 (최대 <style="highlight">3</style>)\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, 피해량 +<style="highlight">30%</style>\n[BeforeAttack] 최대 공명 수 1당, 마지막 코인의 최종 위력 +1 (최대 4)
   źródło: Skills_personality-03.json :: dataList[id=1031502].levelList[level=4].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [NoirNailDonQuixote], [ChargeNoirAlly], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [ChargeNoirAlly] = 보존 / Preservation; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [WhenUse] Final Power +1 for every 4 ([Vibration] Potency + [NoirNailDonQuixote]) on target (max <style="highlight">3</style>)\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 and deal +<style="highlight">30</style>% damage\n[BeforeAttack] The final Coin gains Final Power +1 for every highest Reson. (max 4)
   PL: [WhenUse] Moc Końcowa +1 za każde 4 (suma Mocy [Vibration] i [NoirNailDonQuixote] celu) (maks. <style="highlight">3</style>)\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i zadaje +<style="highlight">30</style>% obrażeń\n[BeforeAttack] Moc Końcowa ostatniej monety +1 za każde 1 najwyższego Rezonansu (maks. 4)
692. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">4</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031502].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">4</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">4</style> [Vibration]
693. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">8</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +<style="highlight">8</style> [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">8</style>
694. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 탄생을 끊으리라!
   źródło: Skills_personality-03.json :: dataList[id=1031503].levelList[level=3].name ; dataList[id=1031503].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: I Sever Thine Advent!
   PL: Przerwie Twe Narodziny!
695. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] [OathFieldDonQuixote] 3 얻음 (턴당 1회)\n[StartBattle] 자신과 자신을 제외한 속도가 가장 빠른 르누아르 소속 아군 인격 1명에게 [AttackUp] 2, [DefenseUp] 2 부여 (턴당 1회)\n[WhenUse] 대상의 [Vibration] 위력과 [NoirNailDonQuixote]의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, 피해량 +20%\n[BeforeAttack] 최대 공명 수 1당, 마지막 코인의 최종 위력 +1 (최대 4)
   źródło: Skills_personality-03.json :: dataList[id=1031503].levelList[level=3].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [OathFieldDonQuixote], [AttackUp], [DefenseUp], [WhenUse], [Vibration], [NoirNailDonQuixote], [ChargeNoirAlly], [BeforeAttack]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [OathFieldDonQuixote] = 보존 신역 / Sanctum of Conservation; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [ChargeNoirAlly] = 보존 / Preservation …
   EN: [StartBattle] Gain 3 [OathFieldDonQuixote] (once per turn)\n[StartBattle] Apply 2 [AttackUp] and 2 [DefenseUp] on self and 1 other "Le Noir" allied Identity with the fastest Speed (once per turn)\n[WhenUse] If target has 6+ ([Vibration] Potency + [NoirNailDonQuixote]), Coin Power +1\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 and deal +20% damage\n[BeforeAttack] The final Coin gains Final Power +1 for every highest Reson. (max 4)
   PL: [StartBattle] Zyskuje 3 [OathFieldDonQuixote] (1 raz na turę)\n[StartBattle] Nakłada 2 [AttackUp] i 2 [DefenseUp] na siebie i 1 inną Tożsamość sojuszniczą „Le Noir” z najwyższą Szybkością (1 raz na turę)\n[WhenUse] Jeżeli cel ma 6+ (suma Mocy [Vibration] i [NoirNailDonQuixote]), Moc Monet +1\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i zadaje +20% obrażeń\n[BeforeAttack] Moc Końcowa ostatniej monety +1 za każde 1 najwyższego Rezonansu (maks. 4)
696. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [NoirNailDonQuixote] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031503].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1031503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 683 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_personality-03.json :: dataList[id=1031503].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] Nakłada 3 [Vibration]
698. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031503].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1031503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 686 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031503].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +3 [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o 3
700. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationFocusing]으로 [Switch_Vibration]
   źródło: Skills_personality-03.json :: dataList[id=1031503].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1031503].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationFocusing], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationFocusing] = 진동 - 보존 / Tremor - Conservation; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationFocusing]
   PL: [OnSucceedAttack] Wywołuje [Switch_Vibration] do [VibrationFocusing]
701. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-03.json :: dataList[id=1031503].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1031503].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 687 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 대상의 [NoirNailDonQuixote]이 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-03.json :: dataList[id=1031503].levelList[level=3].coinlist[#2].coindescs[#3].desc ; dataList[id=1031503].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NoirNailDonQuixote], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If target has 3+ [NoirNailDonQuixote], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Jeżeli cel ma 3+ [NoirNailDonQuixote], [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
703. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [StartBattle] [OathFieldDonQuixote] 3 얻음 (턴당 1회)\n[StartBattle] 자신과 자신을 제외한 속도가 가장 빠른 르누아르 소속 아군 인격 1명에게 [AttackUp] 2, [DefenseUp] 2 부여 (턴당 1회)\n[WhenUse] 대상의 [Vibration] 위력과 [NoirNailDonQuixote]의 합 <style="highlight">6당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, 피해량 +<style="highlight">40%</style>\n[BeforeAttack] 최대 공명 수 1당, 마지막 코인의 최종 위력 +1 (최대 4)
   źródło: Skills_personality-03.json :: dataList[id=1031503].levelList[level=4].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [OathFieldDonQuixote], [AttackUp], [DefenseUp], [WhenUse], [Vibration], [NoirNailDonQuixote], [ChargeNoirAlly], [BeforeAttack]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [OathFieldDonQuixote] = 보존 신역 / Sanctum of Conservation; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [ChargeNoirAlly] = 보존 / Preservation …
   EN: [StartBattle] Gain 3 [OathFieldDonQuixote] (once per turn)\n[StartBattle] Apply 2 [AttackUp] and 2 [DefenseUp] on self and 1 other "Le Noir" allied Identity with the fastest Speed (once per turn)\n[WhenUse] <style="highlight">Coin Power +1 for every 6 ([Vibration] Potency + [NoirNailDonQuixote]) on target (max 2)</style>\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 and deal +<style="highlight">40</style>% damage\n[BeforeAttack] The final Coin gains Final Power +1 for every highest Reson. (max 4)
   PL: [StartBattle] Zyskuje 3 [OathFieldDonQuixote] (1 raz na turę)\n[StartBattle] Nakłada 2 [AttackUp] i 2 [DefenseUp] na siebie i 1 inną Tożsamość sojuszniczą „Le Noir” z najwyższą Szybkością (1 raz na turę)\n[WhenUse] Moc Monet +1 za każde <style="highlight">6</style> (suma Mocy [Vibration] i [NoirNailDonQuixote] celu) <style="highlight">(maks. 2)</style>\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i zadaje +<style="highlight">40</style>% obrażeń\n[BeforeAttack] Moc Końcowa ostatniej monety +1 za każde 1 najwyższego Rezonansu (maks. 4)
704. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">4</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031503].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 692 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +<style="highlight">4</style> [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">4</style>
706. [Umiejętność 4 (×0) (ulepszenia 1,4) — nazwa] 심판!
   źródło: Skills_personality-03.json :: dataList[id=1031505].levelList[level=1].name ; dataList[id=1031505].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 6 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Judgment!
   PL: Wyrok!
707. [Umiejętność 4 (×0) (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 아래 효과가 적용됨\n- 수비 스킬을 발동시키지 않음\n- 외부 효과로 재사용할 수 없음\n- 이 스킬 종료 시까지 대상의 체력이 1 미만으로 감소하지 않음\n[WhenUse] 대상의 [Vibration] 위력과 [NoirNailDonQuixote]의 합 4당, 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, 피해량 +20%
   źródło: Skills_personality-03.json :: dataList[id=1031505].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [Vibration], [NoirNailDonQuixote], [ChargeNoirAlly]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [ChargeNoirAlly] = 보존 / Preservation
   EN: [CantDuel]\nThis Skill has the following properties:\n- Does not trigger Defense Skills\n- External effects cannot trigger this Skill to be Reused\n- Target's HP cannot be reduced below 1 until this Skill ends\n[WhenUse] Final Power +1 for every 4 ([Vibration] Potency + [NoirNailDonQuixote]) on target (max 2)\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 and deal +20% damage
   PL: [CantDuel]\nTa Umiejętność ma następujące właściwości:\n- Nie uruchamia Umiejętności obrony\n- Zewnętrzne efekty nie mogą ponownie uruchomić tej Umiejętności\n- Do końca działania tej Umiejętności HP celu nie może spaść poniżej 1\n[WhenUse] Moc Końcowa +1 za każde 4 (suma Mocy [Vibration] i [NoirNailDonQuixote] celu) (maks. 2)\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i zadaje +20% obrażeń
708. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [NoirNailDonQuixote] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031505].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1031505].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 683 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_personality-03.json :: dataList[id=1031505].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 697 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [CantDuel]\n이 스킬은 아래 효과가 적용됨\n- 수비 스킬을 발동시키지 않음\n- 외부 효과로 재사용할 수 없음\n- 이 스킬 종료 시까지 대상의 체력이 1 미만으로 감소하지 않음\n[WhenUse] 대상의 [Vibration] 위력과 [NoirNailDonQuixote]의 합 4당, 최종 위력 +1 (최대 <style="highlight">3</style>)\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, 피해량 +<style="highlight">40%</style>
   źródło: Skills_personality-03.json :: dataList[id=1031505].levelList[level=4].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [WhenUse], [Vibration], [NoirNailDonQuixote], [ChargeNoirAlly]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [ChargeNoirAlly] = 보존 / Preservation
   EN: [CantDuel]\nThis Skill has the following properties:\n- Does not trigger Defense Skills\n- External effects cannot trigger this Skill to be Reused\n- Target's HP cannot be reduced below 1 until this Skill ends\n[WhenUse] Final Power +1 for every 4 ([Vibration] Potency + [NoirNailDonQuixote]) on target (max <style="highlight">3</style>)\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 and deal +<style="highlight">40</style>% damage
   PL: [CantDuel]\nTa Umiejętność ma następujące właściwości:\n- Nie uruchamia Umiejętności obrony\n- Zewnętrzne efekty nie mogą ponownie uruchomić tej Umiejętności\n- Do końca działania tej Umiejętności HP celu nie może spaść poniżej 1\n[WhenUse] Moc Końcowa +1 za każde 4 (suma Mocy [Vibration] i [NoirNailDonQuixote] celu) (maks. <style="highlight">3</style>)\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i zadaje +<style="highlight">40</style>% obrażeń
711. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">4</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031505].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 692 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Umiejętność 5 (×0) (ulepszenia 3–4) — nazwa] 거듭 내리쳐, 탄생을 끊으리라!
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=3].name ; dataList[id=1031506].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 6 · monety: 3 (+4)
   limit: do 60 znaków
   EN: With Each Smite, I Sever Thine Advent!
   PL: Każdym Ciosem Przerwie Twe Narodziny!
713. [Umiejętność 5 (×0) (ulepszenie 3) — opis] 이 스킬은 수비 스킬 대신 발동해도 공격 스킬로 취급되어, 수비 위력 변경 효과를 받지 않고, 공격 위력 변경 효과가 적용됨\n[StartBattle] 모든 르누아르 소속 아군 인격에게 [AttackUp] 2, [DefenseUp] 2 부여 (턴당 1회)\n[WhenUse] 모든 공격 대상의 [Vibration] 위력과 [NoirNailDonQuixote]의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1\n[WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당, 피해량 +30% (집중 전투인 경우, 부위로 판정)\n[BeforeAttack] 최대 공명 수 1당, 마지막 코인의 최종 위력 +2 (최대 8)\n[EndSkill] [NoirShieldUpDonQuixote] 전부 소모
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=3].desc
   limit: do 900 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [AttackUp], [DefenseUp], [WhenUse], [Vibration], [NoirNailDonQuixote], [ChargeNoirAlly], [BeforeAttack], [EndSkill], [NoirShieldUpDonQuixote]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [ChargeNoirAlly] = 보존 / Preservation; [BeforeAttack] = [공격 시작 전] / [Before Attack] …
   EN: This Skill counts as an Attack Skill even when it activates instead of a Defense Skill; this Skill is unaffected by Defense Power-changing effects, and is instead affected by Attack Power-changing effects\n[StartBattle] Apply 2 [AttackUp] and 2 [DefenseUp] on all "Le Noir" allied Identities (once per turn)\n[WhenUse] At 6+ total sum of ([Vibration] Potency + [NoirNailDonQuixote]) on all targets, Coin Power +1\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1\n[WhenUse] Deal +30% damage for every excess Atk Weight beyond the # of actual targets (for Focused Encounters, Parts)\n[BeforeAttack] The final Coin gains Final Power +2 for every highest Reson. (max 8)\n[EndSkill] Consume all [NoirShieldUpDonQuixote]
   PL: Ta Umiejętność liczy się jako Umiejętność ataku, nawet gdy uruchamia zamiast Umiejętności obrony; nie podlega efektom zmieniającym Moc Obrony, a podlega efektom zmieniającym Moc Ataku\n[StartBattle] Nakłada 2 [AttackUp] i 2 [DefenseUp] na wszystkie Tożsamości sojusznicze „Le Noir” (1 raz na turę)\n[WhenUse] Jeżeli suma (Mocy [Vibration] i [NoirNailDonQuixote]) wszystkich celów wynosi 6 lub więcej, Moc Monet +1\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1\n[WhenUse] Zadaje +30% obrażeń za każdego 1 nadmiarowego celu ataku ponad wagę ataku tej Umiejętności (w walce skupionej: części ciała)\n[BeforeAttack] Moc Końcowa ostatniej monety +2 za każde 1 najwyższego Rezonansu (maks. 8)\n[EndSkill] Zużywa całe [NoirShieldUpDonQuixote]
714. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [NoirNailDonQuixote] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1031506].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 683 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [NoirNailDonQuixote] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1031506].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 683 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1031506].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 686 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 3 증가 (코인당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +3 [ChargeNoirAlly] Count (once per Coin)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o 3 (1 raz na monetę)
720. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationFocusing]으로 [Switch_Vibration]
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1031506].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 700 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=3].coinlist[#2].coindescs[#3].desc ; dataList[id=1031506].levelList[level=4].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 687 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 3, efekt 5 — opis] [OnSucceedAttack] 대상별로 [NoirNailDonQuixote] 수치에 따라 아래 효과 적용\n- [NoirNailDonQuixote]이 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- 이 코인 최종 피해량의 ([NoirNailDonQuixote] x 1.5)%만큼 나태 피해 (최대 45%)\n- 대상의 [NoirNailDonQuixote] 전부 소모
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=3].coinlist[#2].coindescs[#4].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [NoirNailDonQuixote], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Apply the following effects on target depending on its respective [NoirNailDonQuixote] Stack\n- If target has 3+ [NoirNailDonQuixote], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- Deal Sloth damage equal to ([NoirNailDonQuixote] on target x 1.5)% of this Coin's final damage (max 45%)\n- Consume all [NoirNailDonQuixote] on target
   PL: [OnSucceedAttack] Stosuje na każdym celu poniższe efekty zależnie od jego stosu [NoirNailDonQuixote]\n- Jeżeli cel ma 3+ [NoirNailDonQuixote], [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1\n- Zadaje obrażenia Lenistwa równe ([NoirNailDonQuixote] celu x 1.5)% końcowych obrażeń tej monety (maks. 45%)\n- Zużywa całe [NoirNailDonQuixote] celu
723. [Umiejętność 5 (×0) (ulepszenie 4) — opis] 이 스킬은 수비 스킬 대신 발동해도 공격 스킬로 취급되어, 수비 위력 변경 효과를 받지 않고, 공격 위력 변경 효과가 적용됨\n[StartBattle] 모든 르누아르 소속 아군 인격에게 [AttackUp] 2, [DefenseUp] 2 부여 (턴당 1회)\n[WhenUse] 모든 공격 대상의 [Vibration] 위력과 [NoirNailDonQuixote]의 합 <style="highlight">6당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1\n[WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당, 피해량 +<style="highlight">50%</style> (집중 전투인 경우, 부위로 판정)\n[BeforeAttack] 최대 공명 수 1당, 마지막 코인의 최종 위력 +2 (최대 8)\n[EndSkill] [NoirShieldUpDonQuixote] 전부 소모
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=4].desc
   limit: do 920 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [AttackUp], [DefenseUp], [WhenUse], [Vibration], [NoirNailDonQuixote], [ChargeNoirAlly], [BeforeAttack], [EndSkill], [NoirShieldUpDonQuixote]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [ChargeNoirAlly] = 보존 / Preservation; [BeforeAttack] = [공격 시작 전] / [Before Attack] …
   EN: This Skill counts as an Attack Skill even when it activates instead of a Defense Skill; this Skill is unaffected by Defense Power-changing effects, and is instead affected by Attack Power-changing effects\n[StartBattle] Apply 2 [AttackUp] and 2 [DefenseUp] on all "Le Noir" allied Identities (once per turn)\n[WhenUse] <style="highlight">Coin Power +1 for every 6 total sum of ([Vibration] Potency + [NoirNailDonQuixote]) on all targets (max 2)</style>\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1\n[WhenUse] Deal +<style="highlight">50</style>% damage for every excess Atk Weight beyond the # of actual targets (for Focused Encounters, Parts)\n[BeforeAttack] The final Coin gains Final Power +2 for every highest Reson. (max 8)\n[EndSkill] Consume all [NoirShieldUpDonQuixote]
   PL: Ta Umiejętność liczy się jako Umiejętność ataku, nawet gdy uruchamia zamiast Umiejętności obrony; nie podlega efektom zmieniającym Moc Obrony, a podlega efektom zmieniającym Moc Ataku\n[StartBattle] Nakłada 2 [AttackUp] i 2 [DefenseUp] na wszystkie Tożsamości sojusznicze „Le Noir” (1 raz na turę)\n[WhenUse] Moc Monet +1 za każde <style="highlight">6</style> (suma Mocy [Vibration] i [NoirNailDonQuixote] wszystkich celów) <style="highlight">(maks. 2)</style>\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1\n[WhenUse] Zadaje +<style="highlight">50</style>% obrażeń za każdego 1 nadmiarowego celu ataku ponad wagę ataku tej Umiejętności (w walce skupionej: części ciała)\n[BeforeAttack] Moc Końcowa ostatniej monety +2 za każde 1 najwyższego Rezonansu (maks. 8)\n[EndSkill] Zużywa całe [NoirShieldUpDonQuixote]
724. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 258 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 258 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">4</style> 증가 (코인당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +<style="highlight">4</style> [ChargeNoirAlly] Count (once per Coin)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">4</style> (1 raz na monetę)
727. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 5 — opis] [OnSucceedAttack] 대상별로 [NoirNailDonQuixote] 수치에 따라 아래 효과 적용\n- [NoirNailDonQuixote]이 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- 이 코인 최종 피해량의 ([NoirNailDonQuixote] x <style="highlight">3</style>)%만큼 나태 피해 (최대 <style="highlight">90%</style>)\n- 대상의 [NoirNailDonQuixote] 전부 소모
   źródło: Skills_personality-03.json :: dataList[id=1031506].levelList[level=4].coinlist[#2].coindescs[#4].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [NoirNailDonQuixote], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Apply the following effects on target depending on its respective [NoirNailDonQuixote] Stack\n- If target has 3+ [NoirNailDonQuixote], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- Deal Sloth damage equal to ([NoirNailDonQuixote] on target x <style="highlight">3</style>)% of this Coin's final damage (max <style="highlight">90</style>%)\n- Consume all [NoirNailDonQuixote] on target
   PL: [OnSucceedAttack] Stosuje na każdym celu poniższe efekty zależnie od jego stosu [NoirNailDonQuixote]\n- Jeżeli cel ma 3+ [NoirNailDonQuixote], [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1\n- Zadaje obrażenia Lenistwa równe ([NoirNailDonQuixote] celu x <style="highlight">3</style>)% końcowych obrażeń tej monety (maks. <style="highlight">90</style>%)\n- Zużywa całe [NoirNailDonQuixote] celu
728. [Obrona (ulepszenia 1,3,4) — nazwa] 묵시
   źródło: Skills_personality-03.json :: dataList[id=1031504].levelList[level=1].name ; dataList[id=1031504].levelList[level=3].name ; dataList[id=1031504].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Witness Ye in Silence
   PL: W Świetle Przygładzonego Milczenia
729. [Obrona (ulepszenie 1) — opis] [StartBattle] [OathFieldDonQuixote] 3 얻음 (턴당 1회)\n[StartBattle] 자신과 자신을 제외한 정신력이 가장 낮은 르누아르 소속 아군 인격 1명의 정신력 4 회복 (턴당 1회)\n[StartBattle] 자신의 [ChargeNoirAlly] 횟수 2 증가 (턴당 1회)\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1
   źródło: Skills_personality-03.json :: dataList[id=1031504].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [OathFieldDonQuixote], [ChargeNoirAlly], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [OathFieldDonQuixote] = 보존 신역 / Sanctum of Conservation; [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Gain 3 [OathFieldDonQuixote] (once per turn)\n[StartBattle] Heal 4 SP on self and 1 other "Le Noir" allied Identity that has the lowest SP (once per turn)\n[StartBattle] Gain +2 [ChargeNoirAlly] Count (once per turn)\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1
   PL: [StartBattle] Zyskuje 3 [OathFieldDonQuixote] (1 raz na turę)\n[StartBattle] Odzyskuje 4 Poczytalności na sobie i 1 innej Tożsamości sojuszniczej „Le Noir” z najniższą Poczytalnością (1 raz na turę)\n[StartBattle] Zwiększa własny Licznik [ChargeNoirAlly] o 2 (1 raz na turę)\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1
730. [Obrona (ulepszenia 1,3,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [NoirNailDonQuixote] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031504].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1031504].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1031504].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 683 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Obrona (ulepszenia 1,3,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031504].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1031504].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1031504].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +2 [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o 2
733. [Obrona (ulepszenie 3) — opis] [StartBattle] [OathFieldDonQuixote] 3 얻음 (턴당 1회)\n[StartBattle] 자신과 자신을 제외한 정신력이 가장 낮은 르누아르 소속 아군 인격 1명의 정신력 <style="highlight">5</style> 회복 (턴당 1회)\n<style="highlight">[StartBattle] 자신의 [NoirShieldUpDonQuixote]가</style>\n<style="highlight">- 100이면, 대신 ‘거듭 내리쳐, 탄생을 끊으리라!’로 발동됨 (턴당 1회, 이 효과는 일방 공격에도 발동함)</style>\n<style="highlight">- 100 미만이면, 자신의 최대 체력의 ([NoirShieldUpDonQuixote]/10)%만큼 보호막 얻음 (턴당 1회)</style>\n[StartBattle] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">3</style> 증가 (턴당 1회)\n<style="highlight">[WhenUse] 대상의 [Vibration] 위력과 [NoirNailDonQuixote]의 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, <style="highlight">피해량 +10%</style>
   źródło: Skills_personality-03.json :: dataList[id=1031504].levelList[level=3].desc
   limit: do 960 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [OathFieldDonQuixote], [NoirShieldUpDonQuixote], [ChargeNoirAlly], [WhenUse], [Vibration], [NoirNailDonQuixote]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [OathFieldDonQuixote] = 보존 신역 / Sanctum of Conservation; [NoirShieldUpDonQuixote] = 검은 신의 가호 / Blessing of the Obsidian God; [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [NoirNailDonQuixote] = 약속된 못 / Promised Nail
   EN: [StartBattle] Gain 3 [OathFieldDonQuixote] (once per turn)\n[StartBattle] Heal <style="highlight">5</style> SP on self and 1 other "Le Noir" allied Identity that has the lowest SP (once per turn)\n<style="highlight">[StartBattle] Apply the following effects depending on [NoirShieldUpDonQuixote] on self:\n- At 100 [NoirShieldUpDonQuixote], activate "With Each Smite, I Sever Thine Advent!" instead (once per turn; can activate for Unopposed Attacks)\n- At fewer than 100 [NoirShieldUpDonQuixote], gain Shield equal to ([NoirShieldUpDonQuixote] / 10)% of this unit's max HP (once per turn)</style>\n[StartBattle] Gain +<style="highlight">3</style> [ChargeNoirAlly] Count (once per turn)\n<style="highlight">[WhenUse] If target has 6+ ([Vibration] Potency + [NoirNailDonQuixote]), Coin Power +1</style>\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 <style="highlight">and deal +10% damage</style>
   PL: [StartBattle] Zyskuje 3 [OathFieldDonQuixote] (1 raz na turę)\n[StartBattle] Odzyskuje <style="highlight">5</style> Poczytalności na sobie i 1 innej Tożsamości sojuszniczej „Le Noir” z najniższą Poczytalnością (1 raz na turę)\n<style="highlight">[StartBattle] Zależnie od [NoirShieldUpDonQuixote] stosuje następujące efekty:\n- Przy 100 [NoirShieldUpDonQuixote] zamiast tego uruchamia „Każdym Ciosiem Przerwie Twe Narodziny!” (1 raz na turę; uruchamia się również przy atakach nieopartych)\n- Poniżej 100 [NoirShieldUpDonQuixote] zyskuje Tarczę równą ([NoirShieldUpDonQuixote] / 10)% Maks. HP (1 raz na turę)</style>\n[StartBattle] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">3</style> (1 raz na turę)\n<style="highlight">[WhenUse] Jeżeli cel ma 6+ (suma Mocy [Vibration] i [NoirNailDonQuixote]), Moc Monet +1</style>\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i <style="highlight">zadaje +10% obrażeń</style>
734. [Obrona (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031504].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +<style="highlight">3</style> [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">3</style>
735. [Obrona (ulepszenie 4) — opis] [StartBattle] [OathFieldDonQuixote] 3 얻음 (턴당 1회)\n[StartBattle] 자신과 자신을 제외한 정신력이 가장 낮은 르누아르 소속 아군 인격 1명의 정신력 <style="highlight">6</style> 회복 (턴당 1회)\n[StartBattle] 자신의 [NoirShieldUpDonQuixote]가\n- 100이면, 대신 ‘거듭 내리쳐, 탄생을 끊으리라!’로 발동됨 (턴당 1회, 이 효과는 일방 공격에도 발동함)\n- 100 미만이면, 자신의 최대 체력의 ([NoirShieldUpDonQuixote]/10)%만큼 보호막 얻음 (턴당 1회)\n[StartBattle] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">4</style> 증가 (턴당 1회)\n[WhenUse] 대상의 [Vibration] 위력과 [NoirNailDonQuixote]의 합 <style="highlight">6당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1, 피해량 +<style="highlight">20%</style>
   źródło: Skills_personality-03.json :: dataList[id=1031504].levelList[level=4].desc
   limit: do 980 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [OathFieldDonQuixote], [NoirShieldUpDonQuixote], [ChargeNoirAlly], [WhenUse], [Vibration], [NoirNailDonQuixote]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [OathFieldDonQuixote] = 보존 신역 / Sanctum of Conservation; [NoirShieldUpDonQuixote] = 검은 신의 가호 / Blessing of the Obsidian God; [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [NoirNailDonQuixote] = 약속된 못 / Promised Nail
   EN: [StartBattle] Gain 3 [OathFieldDonQuixote] (once per turn)\n[StartBattle] Heal <style="highlight">6</style> SP on self and 1 other "Le Noir" allied Identity that has the lowest SP (once per turn)\n[StartBattle] Apply the following effects depending on [NoirShieldUpDonQuixote] on self:\n- At 100 [NoirShieldUpDonQuixote], activate "With Each Smite, I Sever Thine Advent!" instead (once per turn; can activate for Unopposed Attacks)\n- At fewer than 100 [NoirShieldUpDonQuixote], gain Shield equal to ([NoirShieldUpDonQuixote] / 10)% of this unit's max HP (once per turn)\n[StartBattle] Gain +<style="highlight">4</style> [ChargeNoirAlly] Count (once per turn)\n[WhenUse] <style="highlight">Coin Power +1 for every 6 ([Vibration] Potency + [NoirNailDonQuixote]) on target (max 2)</style>\n[WhenUse] At 3+ [ChargeNoirAlly] Potency, Coin Power +1 and deal +<style="highlight">20</style>% damage
   PL: [StartBattle] Zyskuje 3 [OathFieldDonQuixote] (1 raz na turę)\n[StartBattle] Odzyskuje <style="highlight">6</style> Poczytalności na sobie i 1 innej Tożsamości sojuszniczej „Le Noir” z najniższą Poczytalnością (1 raz na turę)\n[StartBattle] Zależnie od [NoirShieldUpDonQuixote] stosuje następujące efekty:\n- Przy 100 [NoirShieldUpDonQuixote] zamiast tego uruchamia „Każdym Ciosiem Przerwie Twe Narodziny!” (1 raz na turę; uruchamia się również przy atakach nieopartych)\n- Poniżej 100 [NoirShieldUpDonQuixote] zyskuje Tarczę równą ([NoirShieldUpDonQuixote] / 10)% Maks. HP (1 raz na turę)\n[StartBattle] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">4</style> (1 raz na turę)\n[WhenUse] Moc Monet +1 za każde <style="highlight">6</style> (suma Mocy [Vibration] i [NoirNailDonQuixote] celu) <style="highlight">(maks. 2)</style>\n[WhenUse] Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1 i zadaje +<style="highlight">20</style>% obrażeń
736. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-03.json :: dataList[id=1031504].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 705 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Pasywka bojowa (od ulepszenia 1) — nazwa] 말레우스 프로미시오니스
   źródło: Passives.json :: dataList[id=1031502].name
   limit: do 40 znaków
   EN: Malleus Promissionis
   PL: Malleus Promissionis
738. [Pasywka bojowa (od ulepszenia 1) — opis] 스테이지 첫 등장 시 자신의 [ChargeNoirAlly] 횟수 10 증가하고, 자신을 제외한 르누아르 소속 아군 인격의 [Charge] 횟수 2 증가\n\n스킬 효과로 [NoirNailDonQuixote] 부여 시 자신의 [ChargeNoirAlly] 횟수가\n- 12 이상이면, [NoirNailDonQuixote] 부여량 +1, 자신의 [ChargeNoirAlly] 횟수 4 소모\n- 12 미만이면, 자신의 [ChargeNoirAlly] 횟수 2 소모\n- 부족하면, 대신 [NoirNailDonQuixote]을 부여하지 않음\n- 이 효과로 인해서 [NoirNailDonQuixote]을 부여하는 스킬이 [Charge] 횟수를 소모하는 스킬로 취급됨\n\n전투 중 누적으로 자신의 [ChargeNoirAlly] 횟수를 10 소모할 때마다 [ChargeNoirAlly] 위력 1 얻음
   źródło: Passives.json :: dataList[id=1031502].desc
   limit: do 870 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoirAlly], [Charge], [NoirNailDonQuixote]
   znaczenie tagów: [ChargeNoirAlly] = 보존 / Preservation; [Charge] = 충전 / Charge; [NoirNailDonQuixote] = 약속된 못 / Promised Nail
   EN: Upon entering the Encounter for the first time, gain +10 [ChargeNoirAlly] Count and apply +2 [Charge] Count on other "Le Noir" allied Identities\n\nWhen inflicting [NoirNailDonQuixote] using Skill effects:\n- At 12+ [ChargeNoirAlly] Count, inflict +1 more [NoirNailDonQuixote] and consume 4 [ChargeNoirAlly] Count\n- At fewer than 12 [ChargeNoirAlly] Count, consume 2 [ChargeNoirAlly] Count\n- At insufficient [ChargeNoirAlly] Count, does not inflict [NoirNailDonQuixote]\n- Skills that inflict [NoirNailDonQuixote] due to this effect count as Skills that consume [Charge] Count\n\nGain 1 [ChargeNoirAlly] Potency every time this unit consumes 10 cumulative [ChargeNoirAlly] Count in this Encounter
   PL: Przy pierwszym pojawieniu się na polu zyskuje +10 Licznika [ChargeNoirAlly] i nakłada +2 Licznika [Charge] na inne Tożsamości sojusznicze „Le Noir”\n\nPrzy nakładaniu [NoirNailDonQuixote] efektami Umiejętności:\n- Przy 12+ Liczniku [ChargeNoirAlly] nakłada o 1 więcej [NoirNailDonQuixote] i zużywa 4 Licznika [ChargeNoirAlly]\n- Poniżej 12 Licznika [ChargeNoirAlly] zużywa 2 Licznika [ChargeNoirAlly]\n- Przy niewystarczającym Liczniku [ChargeNoirAlly] nie nakłada [NoirNailDonQuixote]\n- Umiejętności nakładające [NoirNailDonQuixote] wskutek tego efektu liczą się jak Umiejętności zużywające Licznik [Charge]\n\nZa każde łączne zużycie 10 własnego Licznika [ChargeNoirAlly] podczas walki zyskuje 1 Mocy [ChargeNoirAlly]
739. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] [ChargeNoirAlly] 횟수와 르누아르 아군의 [Charge] 횟수 증가\n[NoirNailDonQuixote] 부여 시 [ChargeNoirAlly] 횟수 소모, [ChargeNoirAlly] 횟수가 일정 수치 이상이면 부여량 증가\n[ChargeNoirAlly] 횟수를 누적 소모하면 [ChargeNoirAlly] 위력 얻음
   źródło: Passives.json :: dataList[id=1031502].summary
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoirAlly], [Charge], [NoirNailDonQuixote]
   znaczenie tagów: [ChargeNoirAlly] = 보존 / Preservation; [Charge] = 충전 / Charge; [NoirNailDonQuixote] = 약속된 못 / Promised Nail
   EN: Gain [ChargeNoirAlly] Count; "Le Noir" allies gain [Charge] Count\nConsume [ChargeNoirAlly] Count when inflicting [NoirNailDonQuixote]; inflict more [NoirNailDonQuixote] when at sufficient [ChargeNoirAlly] Count\nGain [ChargeNoirAlly] Potency by consuming [ChargeNoirAlly] Count
   PL: Zwiększa własny Licznik [ChargeNoirAlly] i Liczniki [Charge] sojuszników „Le Noir”\nZużywa Licznik [ChargeNoirAlly] przy nakładaniu [NoirNailDonQuixote]; nakłada więcej [NoirNailDonQuixote] przy wystarczającym Liczniku [ChargeNoirAlly]\nZyskuje Moc [ChargeNoirAlly] za łączne zużycie Licznika [ChargeNoirAlly]
740. [Pasywka bojowa (od ulepszenia 1) — tekst klimatyczny] 망치는 못을 박는다. 망치가 두드리는 것은 못뿐이다. 망치에 맞는 것은 못이다. 그렇게 약속되었다.
   źródło: Passives.json :: dataList[id=1031502].flavor
   limit: do 160 znaków
   EN: A hammer drives nails. This hammer strikes nothing but nails. Whatever it strikes is a nail. That is what was agreed upon.
   PL: Młot wbija gwoździe. Ten młot uderza wyłącznie w gwoździe. Co uderzy, staje się gwoździem. Tak została zawarta ta przysięga.
741. [Pasywka bojowa (od ulepszenia 1) — nazwa] 보존의 사명
   źródło: Passives.json :: dataList[id=1031503].name
   limit: do 40 znaków
   EN: Mission of Conservation
   PL: Misja Konserwacji
742. [Pasywka bojowa (od ulepszenia 1) — opis] 스테이지 첫 등장 시 [NoirShieldUpDonQuixote] 25 얻음\n\n자신의 [ChargeNoirAlly] 횟수를 소모하거나 최대치를 초과하여 얻으면, (해당 수치 x 5)만큼 [NoirShieldUpDonQuixote] 얻음 (턴당 최대 30)\n\n보호막이 있는 아군 인격이 피격 시 자신이 [NoirShieldUpDonQuixote] 2 얻음 (턴당 최대 10)\n- 해당 아군 인격이 [PersonalityCharge]이면, 대신 [NoirShieldUpDonQuixote] 5 얻음
   źródło: Passives.json :: dataList[id=1031503].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: \n, [NoirShieldUpDonQuixote], [ChargeNoirAlly], [PersonalityCharge]
   znaczenie tagów: [NoirShieldUpDonQuixote] = 검은 신의 가호 / Blessing of the Obsidian God; [ChargeNoirAlly] = 보존 / Preservation; [PersonalityCharge] = 충전 인격 / Charge ID
   EN: Upon entering the Encounter for the first time, gain 25 [NoirShieldUpDonQuixote]\n\nWhen consuming [ChargeNoirAlly] Count, or when gaining [ChargeNoirAlly] Count past its max cap, gain ([ChargeNoirAlly] Count consumed or surplus [ChargeNoirAlly] Count x 5) [NoirShieldUpDonQuixote] (max 30 per turn)\n\nWhen an allied Identity that has Shield is hit, this unit gains 2 [NoirShieldUpDonQuixote] (max 10 per turn)\n- If the said allied Identity is a [PersonalityCharge], gain 5 [NoirShieldUpDonQuixote] instead
   PL: Przy pierwszym pojawieniu się na polu zyskuje 25 [NoirShieldUpDonQuixote]\n\nGdy zużywa Licznik [ChargeNoirAlly] albo zyskuje go ponad maksimum, zyskuje (ta wartość x 5) [NoirShieldUpDonQuixote] (maks. 30 na turę)\n\nGdy zostanie trafiona Sojusznia Tożsamość z Tarczą, ta jednostka zyskuje 2 [NoirShieldUpDonQuixote] (maks. 10 na turę)\n- Jeżeli tą Tożsamością jest [PersonalityCharge], zamiast tego zyskuje 5 [NoirShieldUpDonQuixote]
743. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] [NoirShieldUpDonQuixote] 얻음
   źródło: Passives.json :: dataList[id=1031503].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NoirShieldUpDonQuixote]
   znaczenie tagów: [NoirShieldUpDonQuixote] = 검은 신의 가호 / Blessing of the Obsidian God
   EN: Gain [NoirShieldUpDonQuixote]
   PL: Zyskuje [NoirShieldUpDonQuixote]
744. [Pasywka bojowa (od ulepszenia 1) — nazwa] 신의 뜻과 가치가 우리와 함께하리…
   źródło: Passives.json :: dataList[id=1031504].name
   limit: do 60 znaków
   EN: The Lord's Will and Values Be With Us...
   PL: Wola i wartości Pana niech będą z nami…
745. [Pasywka bojowa (od ulepszenia 1) — opis] 자신을 제외한 르누아르 소속 아군 인격이 적에게 공격 스킬, 반격 스킬의 사용 전, 자신이 ‘심판!’으로 메인 타겟을 우선으로 일방 공격함 (턴당 1회)\n\n기본 스킬의 마지막 코인 시작 시 (자신의 [ChargeNoirAlly] 위력 + 대상의 [NoirNailDonQuixote]/2)만큼 해당 코인의 최종 위력이 증가함 (최대 5)\n\n자신에게 [OathFieldDonQuixote]이 있으면, 기본 스킬 1/2/3의 합 위력 +1/+2/+3\n\n[NoirNailDonQuixote]이 있는 대상에게 [VibrationExplosion] 발생 시 자신과 자신을 제외한 [Charge] 횟수가 가장 적은 아군 [PersonalityCharge] 1명의 [Charge] 횟수 2 증가 (턴당 2회)
   źródło: Passives.json :: dataList[id=1031504].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoirAlly], [NoirNailDonQuixote], [OathFieldDonQuixote], [VibrationExplosion], [Charge], [PersonalityCharge]
   znaczenie tagów: [ChargeNoirAlly] = 보존 / Preservation; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [OathFieldDonQuixote] = 보존 신역 / Sanctum of Conservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Charge] = 충전 / Charge; [PersonalityCharge] = 충전 인격 / Charge ID
   EN: Before another "Le Noir" allied Identity uses Attack Skills or Counter Skills on an enemy, this unit uses "Judgment!" Skill as an Unopposed Attack against the main target (once per turn)\n\nOn the final Coin Start of a Base Skill, the said Coin gains Final Power +([ChargeNoirAlly] Potency on self + ([NoirNailDonQuixote] on target / 2)) (max 5)\n\nIf this unit has [OathFieldDonQuixote], Base Skill 1/2/3 gains Clash Power +1/+2/+3\n\nWhen [VibrationExplosion] triggers on a target that has [NoirNailDonQuixote], this unit and 1 other allied [PersonalityCharge] that has the lowest [Charge] Count gain +2 [Charge] Count (2 times per turn)
   PL: Zanim inna Tożsamość sojusznicza „Le Noir” użyje Umiejętności ataku lub Kontry na wrogu, ta jednostka używa Umiejętności „Sąd!” jako ataku nieopartego na głównym celu (1 raz na turę)\n\nNa początku ostatniej monety podstawowej Umiejętności ta moneta zyskuje Moc Końcową równą (własna Moc [ChargeNoirAlly] + [NoirNailDonQuixote] celu / 2) (maks. 5)\n\nJeżeli ta jednostka ma [OathFieldDonQuixote], podstawowe Umiejętności 1/2/3 zyskują Moc Starcia +1/+2/+3\n\nGdy na celu z [NoirNailDonQuixote] wywołany zostanie [VibrationExplosion], ta jednostka i 1 inny sojusznik [PersonalityCharge] z najmniejszym Licznikiem [Charge] zyskują +2 Licznika [Charge] (2 razy na turę)
746. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 르누아르 아군이 공격하기 전 ‘심판!’ 사용\n기본 스킬 마지막 코인 최종 위력 증가[TabExplain]\n[OathFieldDonQuixote]이 있으면 기본 스킬 합 위력 증가[TabExplain]\n[NoirNailDonQuixote]이 있는 대상에게 [VibrationExplosion] 시 [Charge] 횟수 증가
   źródło: Passives.json :: dataList[id=1031504].summary
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain], [OathFieldDonQuixote], [NoirNailDonQuixote], [VibrationExplosion], [Charge]
   znaczenie tagów: [OathFieldDonQuixote] = 보존 신역 / Sanctum of Conservation; [NoirNailDonQuixote] = 약속된 못 / Promised Nail; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Charge] = 충전 / Charge
   EN: Use "Judgment!" Skill before a "Le Noir" ally attacks\nBase Skill final Coins gain Final Power\nIf [OathFieldDonQuixote] is active, Base Skills gain Clash Power\nGain [Charge] Count when triggering [VibrationExplosion] on targets that have [NoirNailDonQuixote]
   PL: Używa „Sądu!” przed atakiem sojusznika „Le Noir”\nOstatnie monety podstawowych Umiejętności zyskują Moc Końcową[TabExplain]\nPrzy aktywnym [OathFieldDonQuixote] podstawowe Umiejętności zyskują Moc Starcia[TabExplain]\nZyskuje Licznik [Charge] przy wywołaniu [VibrationExplosion] na celach z [NoirNailDonQuixote]
747. [Pasywka bojowa (od ulepszenia 1) — tekst klimatyczny] 모든 것이 불확실한 이 세상에서 우리를 인도하시고 지키시는 것은 오직 단 하나, 검은 신의 말씀이니, 그 말씀이 길이 되고 빛이 되어 우리를 비추시매, 비로소 우리에게 의미가 부여되더라.
   źródło: Passives.json :: dataList[id=1031504].flavor
   limit: do 270 znaków
   EN: The Obsidian God's words be our guiding light, our armor and shield in this troubled world of uncertainties; becometh His Voice the shining beam of light upon us, thereby bestowing us with meaning so coveted.
   PL: Słowa Obsydianowego Boga niech będą naszym przewodnim światłem, naszą zbroją i tarczą w tym świecie pełnym niepewności; niech Jego Głos stanie się jaśniejącym promieniem, który nas oświetla, obdarzając nas tym tak pożądanym sensem.
748. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Pride, posiadane 1× Envy, posiadane 1× Sloth) — nazwa] 검은 언약
   źródło: Passives.json :: dataList[id=1031501].name
   limit: do 40 znaków
   EN: Obsidian Covenant
   PL: Obsydianowe Przymierze
749. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Pride, posiadane 1× Envy, posiadane 1× Sloth) — opis] 전투 종료 시 자신에게 [OathFieldDonQuixote]이 있으면, 다음 턴에 [Agility] 1 얻음\n\n자신의 기본 공격 스킬로 메인 타겟에게 가하는 피해량 +(자신의 [ChargeNoirAlly] 위력 x 3)% (최대 15%)
   źródło: Passives.json :: dataList[id=1031501].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [OathFieldDonQuixote], [Agility], [ChargeNoirAlly]
   znaczenie tagów: [OathFieldDonQuixote] = 보존 신역 / Sanctum of Conservation; [Agility] = 신속 / Haste; [ChargeNoirAlly] = 보존 / Preservation
   EN: Combat End: If this unit has [OathFieldDonQuixote], gain 1 [Agility] next turn\n\nThis unit's Base Attack Skills deal +([ChargeNoirAlly] Potency on self x 3)% damage against the main target (max 15%)
   PL: Na koniec walki: jeżeli ta jednostka ma [OathFieldDonQuixote], zyskuje w następnej turze 1 [Agility]\n\nPodstawowe Umiejętności ataku tej jednostki zadają +(własna Moc [ChargeNoirAlly] x 3)% więcej obrażeń głównemu celowi (maks. 15%)
750. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Pride, posiadane 1× Envy, posiadane 1× Sloth) — podsumowanie] [OathFieldDonQuixote]이 있으면 다음 턴에 [Agility] 얻음\n기본 공격 스킬로 메인 타겟에게 가하는 피해량 증가[TabExplain]
   źródło: Passives.json :: dataList[id=1031501].summary
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [OathFieldDonQuixote], [Agility], [TabExplain]
   znaczenie tagów: [OathFieldDonQuixote] = 보존 신역 / Sanctum of Conservation; [Agility] = 신속 / Haste
   EN: If [OathFieldDonQuixote] is active, gain [Agility] next turn\nBase Attack Skills deal more damage against the main target
   PL: Przy aktywnym [OathFieldDonQuixote] zyskuje w następnej turze [Agility]\nPodstawowe Umiejętności ataku zadają więcej obrażeń głównemu celowi[TabExplain]
751. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Pride, posiadane 1× Envy, posiadane 1× Sloth) — tekst klimatyczny] 그분의 목소리를 들었다. 그분께서 약속하시더군, 이 모든 것에는 의미가 있다고.
   źródło: Passives.json :: dataList[id=1031501].flavor
   limit: do 120 znaków
   EN: I heard His voice, His promise: "Everything that exists has meaning."
   PL: Usłyszałem Jego głos, Jego obietnicę: „Wszystko, co istnieje, ma swoje znaczenie”.
752. [Pasywka bojowa (od ulepszenia 4, posiadane 1× Pride, posiadane 1× Envy, posiadane 1× Sloth) — nazwa] 검은 언약
   źródło: Passives.json :: dataList[id=1031511].name
   (powtórzenie elementu 748 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Pasywka bojowa (od ulepszenia 4, posiadane 1× Pride, posiadane 1× Envy, posiadane 1× Sloth) — opis] 전투 종료 시 자신에게 [OathFieldDonQuixote]이 있으면, 다음 턴에 [Agility] 2 얻음\n\n자신의 기본 공격 스킬로 메인 타겟에게 가하는 피해량 +(자신의 [ChargeNoirAlly] 위력 x 6)% (최대 30%)
   źródło: Passives.json :: dataList[id=1031511].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [OathFieldDonQuixote], [Agility], [ChargeNoirAlly]
   znaczenie tagów: [OathFieldDonQuixote] = 보존 신역 / Sanctum of Conservation; [Agility] = 신속 / Haste; [ChargeNoirAlly] = 보존 / Preservation
   EN: Combat End: If this unit has [OathFieldDonQuixote], gain 2 [Agility] next turn\n\nThis unit's Base Attack Skills deal +([ChargeNoirAlly] Potency on self x 6)% damage against the main target (max 30%)
   PL: Na koniec walki: jeżeli ta jednostka ma [OathFieldDonQuixote], zyskuje w następnej turze 2 [Agility]\n\nPodstawowe Umiejętności ataku tej jednostki zadają +(własna Moc [ChargeNoirAlly] x 6)% więcej obrażeń głównemu celowi (maks. 30%)
754. [Pasywka bojowa (od ulepszenia 4, posiadane 1× Pride, posiadane 1× Envy, posiadane 1× Sloth) — podsumowanie] [OathFieldDonQuixote]이 있으면 다음 턴에 [Agility] 얻음\n기본 공격 스킬로 메인 타겟에게 가하는 피해량 증가[TabExplain]
   źródło: Passives.json :: dataList[id=1031511].summary
   (powtórzenie elementu 750 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Pasywka bojowa (od ulepszenia 4, posiadane 1× Pride, posiadane 1× Envy, posiadane 1× Sloth) — tekst klimatyczny] 그분의 목소리를 들었다. 그분께서 약속하시더군, 이 모든 것에는 의미가 있다고.
   źródło: Passives.json :: dataList[id=1031511].flavor
   (powtórzenie elementu 751 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Pasywka wsparcia (od ulepszenia 3, posiadane 2× Envy, posiadane 2× Sloth) — nazwa] 진형 보존
   źródło: Passives.json :: dataList[id=1031521].name
   limit: do 40 znaków
   EN: Formation Conservation
   PL: Konserwacja Szyku
757. [Pasywka wsparcia (od ulepszenia 3, posiadane 2× Envy, posiadane 2× Sloth) — opis] 전투 시작 시 전장에 있는 아군 [PersonalityCharge] 1명당, 이번 턴에 모든 아군 [PersonalityCharge]이 받는 피해량 -2% (최소 -10%)
   źródło: Passives.json :: dataList[id=1031521].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [PersonalityCharge]
   znaczenie tagów: [PersonalityCharge] = 충전 인격 / Charge ID
   EN: All allied [PersonalityCharge]s take -2% damage this turn for every allied [PersonalityCharge] on the field at Combat Start (max -10%)
   PL: Na początku walki za każdego 1 Sojusznika [PersonalityCharge] na polu wszyscy sojuszniczy [PersonalityCharge] otrzymują w tej turze -2% obrażeń (maks. -10%)
758. [Pasywka wsparcia (od ulepszenia 3, posiadane 2× Envy, posiadane 2× Sloth) — podsumowanie] 아군 [PersonalityCharge]이 받는 피해량 감소
   źródło: Passives.json :: dataList[id=1031521].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PersonalityCharge]
   znaczenie tagów: [PersonalityCharge] = 충전 인격 / Charge ID
   EN: Allied [PersonalityCharge]s take less damage
   PL: Sojuszniczy [PersonalityCharge] otrzymują mniej obrażeń

## [000] Wedge Office Fixer — Don Quixote — 쐐기 사무소 해결사
- ID Tożsamości: `10316` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9110 · HP bazowe: 72 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Poise, Tremor

759. [Karta Tożsamości — tytuł] 쐐기 사무소\n해결사
   źródło: Personalities.json :: dataList[id=10316].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Wedge Office\nFixer
   PL: Biuro Klin\nFikser
760. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities.json :: dataList[id=10316].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities.json :: dataList[id=10316].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Karta Tożsamości — opis] 돈키호테의 열여섯번째 인격
   źródło: Personalities.json :: dataList[id=10316].desc
   limit: do 120 znaków
   EN: Don Quixote’s 16th Identity
   PL: Szesnasta Tożsamość Don Quixote
763. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 격돌
   źródło: Skills_personality-03.json :: dataList[id=1031601].levelList[level=1].name ; dataList[id=1031601].levelList[level=2].name ; dataList[id=1031601].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 6 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Collision
   PL: Zderzenie
764. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] [Breath] 3 얻음\n[ComboSkill] : <noparse>쐐기 사무소</noparse> 해결사 싱클레어의 스킬과 공명 시 아래 효과 발동 (턴당 1회)\n- [WhenUse] 합 위력 +1\n- [WhenUse] [BattleFieldKnow] 1 얻음\n- [WhenUse] 마지막 코인 1회 재사용\n[WinDuel] 다음 턴에 [PenetrateDamageUp] 1 얻음 (턴당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031601].levelList[level=1].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [WhenUse], [Breath], [ComboSkill], [BattleFieldKnow], [WinDuel], [PenetrateDamageUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [ComboSkill] = 연 / Joint Combo; [BattleFieldKnow] = 전장 파악 / Field Analysis; [WinDuel] = [합 승리시] / [Clash Win]; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: [WhenUse] Gain 3 [Breath]\n[ComboSkill]: Upon Reson. with <noparse>Wedge Office</noparse> Fixer Sinclair's Skills, gain the following effects (once per turn):\n- [WhenUse] Clash Power +1\n- [WhenUse] Gain 1 [BattleFieldKnow]\n- [WhenUse] Reuse the final Coin once\n[WinDuel] Gain 1 [PenetrateDamageUp] next turn (once per turn)
   PL: [WhenUse] Zyskuje 3 [Breath]\n[ComboSkill]: Przy Rezonansie z Umiejętnościami Fiksera Biura Klin Sinclaira uruchamia następujące efekty (1 raz na turę):\n- [WhenUse] Moc Starcia +1\n- [WhenUse] Zyskuje 1 [BattleFieldKnow]\n- [WhenUse] Używa ostatniej monety ponownie\n[WinDuel] Zyskuje w następnej turze 1 [PenetrateDamageUp] (1 raz na turę)
765. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [ReUseOnSucceedAttack] [WedgeMarkGreen] 1 부여
   źródło: Skills_personality-03.json :: dataList[id=1031601].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1031601].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1031601].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [WedgeMarkGreen]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [WedgeMarkGreen] = 쐐기 - 싱클레어 / Wedge - Sinclair
   EN: [ReUseOnSucceedAttack] Inflict 1 [WedgeMarkGreen]
   PL: [ReUseOnSucceedAttack] Nakłada 1 [WedgeMarkGreen]
767. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합 4당, 최종 위력 +1 (최대 2)</style>\n[WhenUse] [Breath] <style="highlight">4</style> 얻음\n[ComboSkill] : <noparse>쐐기 사무소</noparse> 해결사 싱클레어의 스킬과 공명 시 아래 효과 발동 (턴당 1회)\n- [WhenUse] 합 위력 +<style="highlight">2</style>\n- [WhenUse] [BattleFieldKnow] 1 얻음\n- [WhenUse] 마지막 코인 1회 재사용\n[WinDuel] 다음 턴에 [PenetrateDamageUp] 1 얻음 (턴당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031601].levelList[level=2].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <noparse>, </noparse>, \n, [WhenUse], [Breath], [Vibration], [ComboSkill], [BattleFieldKnow], [WinDuel], [PenetrateDamageUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [ComboSkill] = 연 / Joint Combo; [BattleFieldKnow] = 전장 파악 / Field Analysis; [WinDuel] = [합 승리시] / [Clash Win]; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: <style="highlight">[WhenUse] Final Power +1 for every 4 ([Breath] Potency on self + [Vibration] Potency on target) (max 2)</style>\n[WhenUse] Gain <style="highlight">4</style> [Breath]\n[ComboSkill]: Upon Reson. with <noparse>Wedge Office</noparse> Fixer Sinclair's Skills, gain the following effects (once per turn):\n- [WhenUse] Clash Power +<style="highlight">2</style>\n- [WhenUse] Gain 1 [BattleFieldKnow]\n- [WhenUse] Reuse the final Coin once\n[WinDuel] Gain 1 [PenetrateDamageUp] next turn (once per turn)
   PL: <style="highlight">[WhenUse] Moc Końcowa +1 za każde 4 (suma własnej Mocy [Breath] i Mocy [Vibration] celu) (maks. 2)</style>\n[WhenUse] Zyskuje <style="highlight">4</style> [Breath]\n[ComboSkill]: Przy Rezonansie z Umiejętnościami Fiksera Biura Klin Sinclaira uruchamia następujące efekty (1 raz na turę):\n- [WhenUse] Moc Starcia +<style="highlight">2</style>\n- [WhenUse] Zyskuje 1 [BattleFieldKnow]\n- [WhenUse] Używa ostatniej monety ponownie\n[WinDuel] Zyskuje w następnej turze 1 [PenetrateDamageUp] (1 raz na turę)
768. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-03.json :: dataList[id=1031601].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 258 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합 4당, 최종 위력 +1 (최대 <style="highlight">3</style>)\n[WhenUse] [Breath] 4 얻음\n[ComboSkill] : <noparse>쐐기 사무소</noparse> 해결사 싱클레어의 스킬과 공명 시 아래 효과 발동 (턴당 1회)\n- [WhenUse] 합 위력 +2\n- [WhenUse] [BattleFieldKnow] 1 얻음\n- [WhenUse] 마지막 코인 1회 재사용\n[WinDuel] 다음 턴에 [PenetrateDamageUp] 1 얻음 (턴당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031601].levelList[level=4].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <noparse>, </noparse>, \n, [WhenUse], [Breath], [Vibration], [ComboSkill], [BattleFieldKnow], [WinDuel], [PenetrateDamageUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [ComboSkill] = 연 / Joint Combo; [BattleFieldKnow] = 전장 파악 / Field Analysis; [WinDuel] = [합 승리시] / [Clash Win]; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: [WhenUse] Final Power +1 for every 4 ([Breath] Potency on self + [Vibration] Potency on target) (max <style="highlight">3</style>)\n[WhenUse] Gain 4 [Breath]\n[ComboSkill]: Upon Reson. with <noparse>Wedge Office</noparse> Fixer Sinclair's Skills, gain the following effects (once per turn):\n- [WhenUse] Clash Power +2\n- [WhenUse] Gain 1 [BattleFieldKnow]\n- [WhenUse] Reuse the final Coin once\n[WinDuel] Gain 1 [PenetrateDamageUp] next turn (once per turn)
   PL: [WhenUse] Moc Końcowa +1 za każde 4 (suma własnej Mocy [Breath] i Mocy [Vibration] celu) (maks. <style="highlight">3</style>)\n[WhenUse] Zyskuje 4 [Breath]\n[ComboSkill]: Przy Rezonansie z Umiejętnościami Fiksera Biura Klin Sinclaira uruchamia następujące efekty (1 raz na turę):\n- [WhenUse] Moc Starcia +2\n- [WhenUse] Zyskuje 1 [BattleFieldKnow]\n- [WhenUse] Używa ostatniej monety ponownie\n[WinDuel] Zyskuje w następnej turze 1 [PenetrateDamageUp] (1 raz na turę)
770. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]<style="highlight"></style>
771. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 빈틈 노리기
   źródło: Skills_personality-03.json :: dataList[id=1031602].levelList[level=1].name ; dataList[id=1031602].levelList[level=2].name ; dataList[id=1031602].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 5 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Gap Strike
   PL: Uderzenie w Szczelinę
772. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [Breath] 2 얻음\n[WinDuel] 대상에게 [Vibration] 1 부여하고 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-03.json :: dataList[id=1031602].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel], [Vibration], [VibrationExplosion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [WhenUse] Gain 2 [Breath]\n[WinDuel] Inflict 1 [Vibration], then trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [WhenUse] Zyskuje 2 [Breath]\n[WinDuel] Nakłada 1 [Vibration] na celu i wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
773. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-03.json :: dataList[id=1031602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합 4당, 최종 위력 +1 (최대 2)</style>\n[WhenUse] [Breath] <style="highlight">3</style> 얻음\n[WinDuel] 대상에게 [Vibration] 1 부여하고 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-03.json :: dataList[id=1031602].levelList[level=2].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Vibration], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: <style="highlight">[WhenUse] Final Power +1 for every 4 ([Breath] Potency on self + [Vibration] Potency on target) (max 2)</style>\n[WhenUse] Gain <style="highlight">3</style> [Breath]\n[WinDuel] Inflict 1 [Vibration], then trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: <style="highlight">[WhenUse] Moc Końcowa +1 za każde 4 (suma własnej Mocy [Breath] i Mocy [Vibration] celu) (maks. 2)</style>\n[WhenUse] Zyskuje <style="highlight">3</style> [Breath]\n[WinDuel] Nakłada 1 [Vibration] na celu i wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
776. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] <style="highlight">2</style> 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031602].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain <style="highlight">2</style> [Breath]
   PL: [OnSucceedAttack] Zyskuje <style="highlight">2</style> [Breath]
777. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnStartCoin] 자신의 [BattleFieldKnow] 1당, 이 코인의 최종 위력 +1 (최대 4)</style>
   źródło: Skills_personality-03.json :: dataList[id=1031602].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [BattleFieldKnow]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [BattleFieldKnow] = 전장 파악 / Field Analysis
   EN: <style="highlight">[OnStartCoin] This Coin gains Final Power +1 for every [BattleFieldKnow] on self (max 4)</style>
   PL: <style="highlight">[OnStartCoin] Moc Końcowa tej monety +1 za każde 1 [BattleFieldKnow] (maks. 4)</style>
778. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031602].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1031602].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Vibration]<style="highlight"></style>
779. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합 4당, 최종 위력 +1 (최대 <style="highlight">3</style>)\n[WhenUse] [Breath] 3 얻음\n[WinDuel] 대상에게 [Vibration] 1 부여하고 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-03.json :: dataList[id=1031602].levelList[level=4].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Vibration], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [WhenUse] Final Power +1 for every 4 ([Breath] Potency on self + [Vibration] Potency on target) (max <style="highlight">3</style>)\n[WhenUse] Gain 3 [Breath]\n[WinDuel] Inflict 1 [Vibration], then trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [WhenUse] Moc Końcowa +1 za każde 4 (suma własnej Mocy [Breath] i Mocy [Vibration] celu) (maks. <style="highlight">3</style>)\n[WhenUse] Zyskuje 3 [Breath]\n[WinDuel] Nakłada 1 [Vibration] na celu i wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
780. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 593 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnStartCoin] 자신의 [BattleFieldKnow] 1당, 이 코인의 최종 위력 +1 (최대 4)<style="highlight"></style>
   źródło: Skills_personality-03.json :: dataList[id=1031602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [BattleFieldKnow]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [BattleFieldKnow] = 전장 파악 / Field Analysis
   EN: [OnStartCoin] This Coin gains Final Power +1 for every [BattleFieldKnow] on self (max 4)<style="highlight"></style>
   PL: [OnStartCoin] Moc Końcowa tej monety +1 za każde 1 [BattleFieldKnow] (maks. 4)<style="highlight"></style>
782. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 창 휩쓸기
   źródło: Skills_personality-03.json :: dataList[id=1031603].levelList[level=3].name ; dataList[id=1031603].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Speared Sweep
   PL: Zamieć Włócznią
783. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 2 얻음\n[ComboSkill] : <noparse>쐐기 사무소</noparse> 해결사 싱클레어의 스킬과 공명 시 아래 효과 발동 (턴당 1회)\n- [WhenUse] 합 위력 +1\n- [WhenUse] [BattleFieldKnow] 1 얻음\n- [WhenUse] 피해량 +20%\n[WinDuel] 대상에게 [Vibration] 2 부여하고 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-03.json :: dataList[id=1031603].levelList[level=3].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [WhenUse], [Breath], [Vibration], [ComboSkill], [BattleFieldKnow], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [ComboSkill] = 연 / Joint Combo; [BattleFieldKnow] = 전장 파악 / Field Analysis; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [WhenUse] At 6+ ([Breath] Potency on self + [Vibration] Potency on target), Coin Power +1\n[WhenUse] Gain 2 [Breath]\n[ComboSkill]: Upon Reson. with <noparse>Wedge Office</noparse> Fixer Sinclair's Skills, gain the following effects (once per turn):\n- [WhenUse] Clash Power +1\n- [WhenUse] Gain 1 [BattleFieldKnow]\n- [WhenUse] Deal +20% damage\n[WinDuel] Inflict 2 [Vibration], then trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [WhenUse] Jeżeli cel ma 6+ (suma własnej Mocy [Breath] i Mocy [Vibration] celu), Moc Monet +1\n[WhenUse] Zyskuje 2 [Breath]\n[ComboSkill]: Przy Rezonansie z Umiejętnościami Fiksera Biura Klin Sinclaira uruchamia następujące efekty (1 raz na turę):\n- [WhenUse] Moc Starcia +1\n- [WhenUse] Zyskuje 1 [BattleFieldKnow]\n- [WhenUse] Zadaje +20% obrażeń\n[WinDuel] Nakłada 2 [Vibration] na celu i wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
784. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031603].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1031603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 4 [Breath]
   PL: [OnSucceedAttack] Zyskuje 4 [Breath]
785. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031603].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1031603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 686 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 대상이 [Switch_Vibration]이나 [FusionVibration] 상태면, 피해량 +20%
   źródło: Skills_personality-03.json :: dataList[id=1031603].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Switch_Vibration], [FusionVibration]
   znaczenie tagów: [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: If target is in either [Switch_Vibration] or [FusionVibration] states, deal +20% damage
   PL: Jeżeli cel jest w stanie [Switch_Vibration] lub [FusionVibration], zadaje +20% obrażeń
787. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnStartCoin] 자신의 [BattleFieldKnow] 1당, 이 코인의 최종 위력 +1 (최대 4)
   źródło: Skills_personality-03.json :: dataList[id=1031603].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1031603].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [BattleFieldKnow]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [BattleFieldKnow] = 전장 파악 / Field Analysis
   EN: [OnStartCoin] This Coin gains Final Power +1 for every [BattleFieldKnow] on self (max 4)
   PL: [OnStartCoin] Moc Końcowa tej monety +1 za każde 1 [BattleFieldKnow] (maks. 4)
788. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 대상이 [Switch_Vibration] 상태가 아니면, [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_personality-03.json :: dataList[id=1031603].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1031603].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Switch_Vibration], [VibrationCollapse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay
   EN: [OnSucceedAttack] If target isn't in an [Switch_Vibration] state, trigger [Switch_Vibration] into [VibrationCollapse]
   PL: [OnSucceedAttack] Jeżeli cel nie jest w stanie [Switch_Vibration], wywołuje [Switch_Vibration] do [VibrationCollapse]
789. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-03.json :: dataList[id=1031603].levelList[level=3].coinlist[#2].coindescs[#3].desc ; dataList[id=1031603].levelList[level=4].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 687 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 2 얻음\n[ComboSkill] : <noparse>쐐기 사무소</noparse> 해결사 싱클레어의 스킬과 공명 시 아래 효과 발동 (턴당 1회)\n- [WhenUse] 합 위력 +<style="highlight">3</style>\n- [WhenUse] [BattleFieldKnow] 1 얻음\n- [WhenUse] 피해량 +<style="highlight">40%</style>\n[WinDuel] 대상에게 [Vibration] 2 부여하고 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-03.json :: dataList[id=1031603].levelList[level=4].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, <style="highlight">, </style>, \n, [WhenUse], [Breath], [Vibration], [ComboSkill], [BattleFieldKnow], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [ComboSkill] = 연 / Joint Combo; [BattleFieldKnow] = 전장 파악 / Field Analysis; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [WhenUse] At 6+ ([Breath] Potency on self + [Vibration] Potency on target), Coin Power +1\n[WhenUse] Gain 2 [Breath]\n[ComboSkill]: Upon Reson. with <noparse>Wedge Office</noparse> Fixer Sinclair's Skills, gain the following effects (once per turn):\n- [WhenUse] Clash Power +<style="highlight">3</style>\n- [WhenUse] Gain 1 [BattleFieldKnow]\n- [WhenUse] Deal +<style="highlight">40</style>% damage\n[WinDuel] Inflict 2 [Vibration], then trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [WhenUse] Jeżeli cel ma 6+ (suma własnej Mocy [Breath] i Mocy [Vibration] celu), Moc Monet +1\n[WhenUse] Zyskuje 2 [Breath]\n[ComboSkill]: Przy Rezonansie z Umiejętnościami Fiksera Biura Klin Sinclaira uruchamia następujące efekty (1 raz na turę):\n- [WhenUse] Moc Starcia +<style="highlight">3</style>\n- [WhenUse] Zyskuje 1 [BattleFieldKnow]\n- [WhenUse] Zadaje +<style="highlight">40</style>% obrażeń\n[WinDuel] Nakłada 2 [Vibration] na celu i wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
791. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 대상이 [Switch_Vibration]이나 [FusionVibration] 상태면, 피해량 +<style="highlight">30%</style>
   źródło: Skills_personality-03.json :: dataList[id=1031603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Switch_Vibration], [FusionVibration]
   znaczenie tagów: [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: If target is in either [Switch_Vibration] or [FusionVibration] states, deal +<style="highlight">30</style>% damage
   PL: Jeżeli cel jest w stanie [Switch_Vibration] lub [FusionVibration], zadaje +<style="highlight">30</style>% obrażeń
792. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 빈틈 없이 확실하게 꿰뚫어주지
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].name ; dataList[id=1031605].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 5 · monety: 3 (+5)
   limit: do 50 znaków
   EN: My Spear Shall Puncture Thee True!
   PL: Włócznia Przebi Cię Precyzyjnie!
793. [Umiejętność 4 (×0) (ulepszenie 3) — opis] 이 스킬은 수비 스킬 대신 발동해도 공격 스킬로 취급되어, 수비 위력 변경 효과를 받지 않고, 공격 위력 변경 효과가 적용됨\n대상의 [WedgeMarkGreen] 2당, 합 위력 +1 (최대 4)\n[WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 2 얻음\n[ComboSkill] : <noparse>쐐기 사무소</noparse> 해결사 싱클레어의 스킬과 공명 시 아래 효과 발동 (턴당 1회)\n- [WhenUse] 합 위력 +1\n- [WhenUse] [BattleFieldKnow] 1 얻음\n- [WhenUse] 피해량 +30%\n[WinDuel] 대상에게 [Vibration] 4 부여하고 [VibrationExplosion]\n[EndSkill] 대상의 [WedgeMarkGreen] 전부 소멸\n[EndSkill] 아군 <noparse>쐐기 사무소</noparse> 대표 오티스 인격의 [ComboWedge] 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].desc
   limit: do 980 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [WedgeMarkGreen], [WhenUse], [Breath], [Vibration], [ComboSkill], [BattleFieldKnow], [WinDuel], [VibrationExplosion], [EndSkill], [ComboWedge]
   znaczenie tagów: [WedgeMarkGreen] = 쐐기 - 싱클레어 / Wedge - Sinclair; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [ComboSkill] = 연 / Joint Combo; [BattleFieldKnow] = 전장 파악 / Field Analysis; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst …
   EN: This Skill counts as an Attack Skill even when it activates instead of a Defense Skill; this Skill is unaffected by Defense Power-changing effects, and is instead affected by Attack Power-changing effects\nClash Power +1 for every 2 [WedgeMarkGreen] on target (max 4)\n[WhenUse] At 6+ ([Breath] Potency on self + [Vibration] Potency on target), Coin Power +1\n[WhenUse] Gain 2 [Breath]\n[ComboSkill]: Upon Reson. with <noparse>Wedge Office</noparse> Fixer Sinclair's Skills, gain the following effects (once per turn):\n- [WhenUse] Clash Power +1\n- [WhenUse] Gain 1 [BattleFieldKnow]\n- [WhenUse] Deal +30% damage\n[WinDuel] Inflict 4 [Vibration], then trigger [VibrationExplosion]\n[EndSkill] Remove all [WedgeMarkGreen] on target\n[EndSkill] Allied <noparse>Wedge Office</noparse> Rep Outis Identity gains 3 [ComboWedge]
   PL: Ta Umiejętność liczy się jako Umiejętność ataku, nawet gdy uruchamia zamiast Umiejętności obrony; nie podlega efektom zmieniającym Moc Obrony, a podlega efektom zmieniającym Moc Ataku\nMoc Starcia +1 za każde 2 [WedgeMarkGreen] na celu (maks. 4)\n[WhenUse] Jeżeli cel ma 6+ (suma własnej Mocy [Breath] i Mocy [Vibration] celu), Moc Monet +1\n[WhenUse] Zyskuje 2 [Breath]\n[ComboSkill]: Przy Rezonansie z Umiejętnościami Fiksera Biura Klin Sinclaira uruchamia następujące efekty (1 raz na turę):\n- [WhenUse] Moc Starcia +1\n- [WhenUse] Zyskuje 1 [BattleFieldKnow]\n- [WhenUse] Zadaje +30% obrażeń\n[WinDuel] Nakłada 4 [Vibration] na celu i wywołuje [VibrationExplosion]\n[EndSkill] Całe [WedgeMarkGreen] celu wygasa\n[EndSkill] Tożsamość sojusznicza <noparse>Biura Klin</noparse> — Szefowa Otis zyskuje 3 [ComboWedge]
794. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1031605].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1031605].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 784 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1031605].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1031605].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 686 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +20%
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   EN: Deal +20% damage on Critical Hit
   PL: Zadaje +20% obrażeń przy trafieniu krytycznym
800. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 2 — podsumowanie] 크리티컬 피해량이 증가
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#1].summary ; dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#1].summary
   limit: do 120 znaków
   EN: Deal more damage on Critical Hit
   PL: Zadaje więcej obrażeń przy trafieniu krytycznym
801. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] 피해량 +(40/대상의 관통 내성)% (최대 80%, 소수점 버림)
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   EN: Deal +(40 / target's Pierce Resist.)% damage (max 80%; rounded down)
   PL: Zadaje +(40 / odporność celu na Kłucie)% obrażeń (maks. 80%, zaokrąglone w dół)
802. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 3 — podsumowanie] 대상의 관통 내성이 낮을수록 피해량이 증가
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#2].summary ; dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#2].summary
   limit: do 120 znaków
   EN: Deal more damage the lower the target's Pierce Resist. is
   PL: Zadaje więcej obrażeń im niższa jest odporność celu na Kłucie
803. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 4 — opis] 대상이 [Switch_Vibration]이나 [FusionVibration] 상태면, 피해량 +30%
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#3].desc ; dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Switch_Vibration], [FusionVibration]
   znaczenie tagów: [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: If target is in either [Switch_Vibration] or [FusionVibration] states, deal +30% damage
   PL: Jeżeli cel jest w stanie [Switch_Vibration] lub [FusionVibration], zadaje +30% obrażeń
804. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 4 — podsumowanie] 피해량 +30%
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#3].summary ; dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#3].summary
   limit: do 120 znaków
   EN: Damage +30%
   PL: Zadaje +30% obrażeń
805. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 5 — opis] [OnStartCoin] 자신의 [BattleFieldKnow] 1당, 이 코인의 최종 위력 +2 (최대 8)
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#4].desc ; dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [BattleFieldKnow]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [BattleFieldKnow] = 전장 파악 / Field Analysis
   EN: [OnStartCoin] This Coin gains Final Power +2 for every [BattleFieldKnow] on self (max 8)
   PL: [OnStartCoin] Moc Końcowa tej monety +2 za każde 1 [BattleFieldKnow] (maks. 8)
806. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 5 — podsumowanie] [OnStartCoin] [BattleFieldKnow]에 비례하여 최종 위력이 증가
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#4].summary ; dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#4].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [BattleFieldKnow]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [BattleFieldKnow] = 전장 파악 / Field Analysis
   EN: [OnStartCoin] Gain Final Power based on [BattleFieldKnow]
   PL: [OnStartCoin] Moc Końcowa rośnie proporcjonalnie do [BattleFieldKnow]
807. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 6 — opis] [OnSucceedAttack] 대상이 [Switch_Vibration] 상태가 아니면, [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#5].desc ; dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#5].desc
   (powtórzenie elementu 788 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 6 — podsumowanie] [OnSucceedAttack] [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#5].summary ; dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#5].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationCollapse], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationCollapse]
   PL: [OnSucceedAttack] Wywołuje [Switch_Vibration] do [VibrationCollapse]
809. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 7 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 (대상의 [WedgeMarkGreen] x 7)%만큼 관통 피해 (최대 56%)
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#6].desc ; dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#6].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [WedgeMarkGreen]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [WedgeMarkGreen] = 쐐기 - 싱클레어 / Wedge - Sinclair
   EN: [OnSucceedAttack] Deal Pierce damage equal to ([WedgeMarkGreen] on target x 7)% of this Coin's final damage (max 56%)
   PL: [OnSucceedAttack] Zadaje obrażenia Kłucia równe ([WedgeMarkGreen] celu x 7)% końcowych obrażeń tej monety (maks. 56%)
810. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 7 — podsumowanie] [OnSucceedAttack] 대상의 [WedgeMarkGreen]에 비례하여 관통 피해
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#6].summary ; dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#6].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [WedgeMarkGreen]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [WedgeMarkGreen] = 쐐기 - 싱클레어 / Wedge - Sinclair
   EN: [OnSucceedAttack] Deal Pierce damage based on [WedgeMarkGreen] on target
   PL: [OnSucceedAttack] Zadaje obrażenia Kłucia proporcjonalnie do [WedgeMarkGreen] celu
811. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 8 — opis] [OnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=3].coinlist[#2].coindescs[#7].desc ; dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#7].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion] 2 razy. Zmniejsza Licznik [Vibration] celu o 2
812. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 이 스킬은 수비 스킬 대신 발동해도 공격 스킬로 취급되어, 수비 위력 변경 효과를 받지 않고, 공격 위력 변경 효과가 적용됨\n대상의 [WedgeMarkGreen] 2당, 합 위력 +1 (최대 4)\n[WhenUse] 자신의 [Breath] 위력과 대상의 [Vibration] 위력의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 2 얻음\n[ComboSkill] : <noparse>쐐기 사무소</noparse> 해결사 싱클레어의 스킬과 공명 시 아래 효과 발동 (턴당 1회)\n- [WhenUse] 합 위력 +<style="highlight">3</style>\n- [WhenUse] [BattleFieldKnow] 1 얻음\n- [WhenUse] 피해량 +<style="highlight">50%</style>\n[WinDuel] 대상에게 [Vibration] 4 부여하고 [VibrationExplosion]\n[EndSkill] 대상의 [WedgeMarkGreen] 전부 소멸\n[EndSkill] 아군 <noparse>쐐기 사무소</noparse> 대표 오티스 인격의 [ComboWedge] 3 증가
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=4].desc
   limit: do 980 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, <style="highlight">, </style>, \n, [WedgeMarkGreen], [WhenUse], [Breath], [Vibration], [ComboSkill], [BattleFieldKnow], [WinDuel], [VibrationExplosion], [EndSkill], [ComboWedge]
   znaczenie tagów: [WedgeMarkGreen] = 쐐기 - 싱클레어 / Wedge - Sinclair; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Vibration] = 진동 / Tremor; [ComboSkill] = 연 / Joint Combo; [BattleFieldKnow] = 전장 파악 / Field Analysis; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst …
   EN: This Skill counts as an Attack Skill even when it activates instead of a Defense Skill; this Skill is unaffected by Defense Power-changing effects, and is instead affected by Attack Power-changing effects\nClash Power +1 for every 2 [WedgeMarkGreen] on target (max 4)\n[WhenUse] At 6+ ([Breath] Potency on self + [Vibration] Potency on target), Coin Power +1\n[WhenUse] Gain 2 [Breath]\n[ComboSkill]: Upon Reson. with <noparse>Wedge Office</noparse> Fixer Sinclair's Skills, gain the following effects (once per turn):\n- [WhenUse] Clash Power +<style="highlight">3</style>\n- [WhenUse] Gain 1 [BattleFieldKnow]\n- [WhenUse] Deal +<style="highlight">50</style>% damage\n[WinDuel] Inflict 4 [Vibration], then trigger [VibrationExplosion]\n[EndSkill] Remove all [WedgeMarkGreen] on target\n[EndSkill] Allied <noparse>Wedge Office</noparse> Rep Outis Identity gains 3 [ComboWedge]
   PL: Ta Umiejętność liczy się jako Umiejętność ataku, nawet gdy uruchamia zamiast Umiejętności obrony; nie podlega efektom zmieniającym Moc Obrony, a podlega efektom zmieniającym Moc Ataku\nMoc Starcia +1 za każde 2 [WedgeMarkGreen] na celu (maks. 4)\n[WhenUse] Jeżeli cel ma 6+ (suma własnej Mocy [Breath] i Mocy [Vibration] celu), Moc Monet +1\n[WhenUse] Zyskuje 2 [Breath]\n[ComboSkill]: Przy Rezonansie z Umiejętnościami Fiksera Biura Klin Sinclaira uruchamia następujące efekty (1 raz na turę):\n- [WhenUse] Moc Starcia +<style="highlight">3</style>\n- [WhenUse] Zyskuje 1 [BattleFieldKnow]\n- [WhenUse] Zadaje +<style="highlight">50</style>% obrażeń\n[WinDuel] Nakłada 4 [Vibration] na celu i wywołuje [VibrationExplosion]\n[EndSkill] Całe [WedgeMarkGreen] celu wygasa\n[EndSkill] Tożsamość sojusznicza <noparse>Biura Klin</noparse> — Szefowa Otis zyskuje 3 [ComboWedge]
813. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +<style="highlight">40%</style>
   źródło: Skills_personality-03.json :: dataList[id=1031605].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal +<style="highlight">40</style>% damage on Critical Hit
   PL: Zadaje +<style="highlight">40</style>% obrażeń przy trafieniu krytycznym
814. [Obrona (ulepszenia 1,3,4) — nazwa] 숨 고르기
   źródło: Skills_personality-03.json :: dataList[id=1031604].levelList[level=1].name ; dataList[id=1031604].levelList[level=3].name ; dataList[id=1031604].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Catch Breath
   PL: Wyrównanie Oddechu
815. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 위력이 6 이상이면, 코인 위력 +1\n[OnSucceedEvade] [Breath] 1 얻음 (턴당 3회)\n[OnBattleEnd] 이번 턴에 스킬 효과로 [BattleFieldKnow]을 얻지 못했으면, [BattleFieldKnow] 1 얻음 (턴당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031604].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [OnSucceedEvade], [OnBattleEnd], [BattleFieldKnow]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [OnBattleEnd] = [전투 종료 시] / [Combat End]; [BattleFieldKnow] = 전장 파악 / Field Analysis
   EN: [WhenUse] At 6+ [Breath] Potency, Coin Power +1\n[OnSucceedEvade] Gain 1 [Breath] (3 times per turn)\n[OnBattleEnd] If this unit could not gain [BattleFieldKnow] from Skill effects this turn, gain 1 [BattleFieldKnow] (once per turn)
   PL: [WhenUse] Przy 6+ Mocy [Breath] Moc Monet +1\n[OnSucceedEvade] Zyskuje 1 [Breath] (3 razy na turę)\n[OnBattleEnd] Jeżeli ta jednostka nie zyskała w tej turze [BattleFieldKnow] efektami Umiejętności, zyskuje 1 [BattleFieldKnow] (1 raz na turę)
816. [Obrona (ulepszenie 3) — opis] <style="highlight">[StartBattle] 대상의 [WedgeMarkGreen]가 4 이상이면, 대신 ‘빈틈 없이 확실하게 꿰뚫어주지’로 발동됨 (턴당 1회, 이 효과는 일방 공격에도 발동함)</style>\n[WhenUse] 자신의 [Breath] 위력이 6 이상이면, 코인 위력 +1\n[OnSucceedEvade] [Breath] <style="highlight">2</style> 얻음 (턴당 3회)\n[OnBattleEnd] 이번 턴에 스킬 효과로 [BattleFieldKnow]을 얻지 못했으면, [BattleFieldKnow] 1 얻음 (턴당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031604].levelList[level=3].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [WedgeMarkGreen], [WhenUse], [Breath], [OnSucceedEvade], [OnBattleEnd], [BattleFieldKnow]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WedgeMarkGreen] = 쐐기 - 싱클레어 / Wedge - Sinclair; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [OnBattleEnd] = [전투 종료 시] / [Combat End]; [BattleFieldKnow] = 전장 파악 / Field Analysis
   EN: <style="highlight">[StartBattle] If target has 4+ [WedgeMarkGreen], activate "My Spear Shall Puncture Thee True!" instead (once per turn; can activate for Unopposed Attacks)</style>\n[WhenUse] At 6+ [Breath] Potency, Coin Power +1\n[OnSucceedEvade] Gain <style="highlight">2</style> [Breath] (3 times per turn)\n[OnBattleEnd] If this unit could not gain [BattleFieldKnow] from Skill effects this turn, gain 1 [BattleFieldKnow] (once per turn)
   PL: <style="highlight">[StartBattle] Jeżeli cel ma 4+ [WedgeMarkGreen], zamiast tego uruchamia „Włócznia Przebi Cię Precyzyjnie!” (1 raz na turę; uruchamia się również przy atakach nieopartych)</style>\n[WhenUse] Przy 6+ Mocy [Breath] Moc Monet +1\n[OnSucceedEvade] Zyskuje <style="highlight">2</style> [Breath] (3 razy na turę)\n[OnBattleEnd] Jeżeli ta jednostka nie zyskała w tej turze [BattleFieldKnow] efektami Umiejętności, zyskuje 1 [BattleFieldKnow] (1 raz na turę)
817. [Obrona (ulepszenie 4) — opis] [StartBattle] 대상의 [WedgeMarkGreen]가 4 이상이면, 대신 ‘빈틈 없이 확실하게 꿰뚫어주지’로 발동됨 (턴당 1회, 이 효과는 일방 공격에도 발동함)\n[WhenUse] 자신의 [Breath] 위력이 6 이상이면, 코인 위력 +1\n[OnSucceedEvade] [Breath] 2 얻음 (턴당 3회)\n<style="highlight">[OnSucceedEvade] 다음 턴에 [Agility] 1 얻음 (턴당 1회)</style>\n[OnBattleEnd] 이번 턴에 스킬 효과로 [BattleFieldKnow]을 얻지 못했으면, [BattleFieldKnow] 1 얻음 (턴당 1회)
   źródło: Skills_personality-03.json :: dataList[id=1031604].levelList[level=4].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [WedgeMarkGreen], [WhenUse], [Breath], [OnSucceedEvade], [Agility], [OnBattleEnd], [BattleFieldKnow]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WedgeMarkGreen] = 쐐기 - 싱클레어 / Wedge - Sinclair; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Agility] = 신속 / Haste; [OnBattleEnd] = [전투 종료 시] / [Combat End]; [BattleFieldKnow] = 전장 파악 / Field Analysis
   EN: [StartBattle] If target has 4+ [WedgeMarkGreen], activate "My Spear Shall Puncture Thee True!" instead (once per turn; can activate for Unopposed Attacks)\n[WhenUse] At 6+ [Breath] Potency, Coin Power +1\n[OnSucceedEvade] Gain 2 [Breath] (3 times per turn)\n<style="highlight">[OnSucceedEvade] Gain 1 [Agility] next turn (once per turn)</style>\n[OnBattleEnd] If this unit could not gain [BattleFieldKnow] from Skill effects this turn, gain 1 [BattleFieldKnow] (once per turn)
   PL: [StartBattle] Jeżeli cel ma 4+ [WedgeMarkGreen], zamiast tego uruchamia „Włócznia Przebi Cię Precyzyjnie!” (1 raz na turę; uruchamia się również przy atakach nieopartych)\n[WhenUse] Przy 6+ Mocy [Breath] Moc Monet +1\n[OnSucceedEvade] Zyskuje 2 [Breath] (3 razy na turę)\n<style="highlight">[OnSucceedEvade] Zyskuje w następnej turze 1 [Agility] (1 raz na turę)</style>\n[OnBattleEnd] Jeżeli ta jednostka nie zyskała w tej turze [BattleFieldKnow] efektami Umiejętności, zyskuje 1 [BattleFieldKnow] (1 raz na turę)
818. [Pasywka bojowa (od ulepszenia 1) — nazwa] 싱클레어 군! 내 움직임에 맞추시게!!
   źródło: Passives.json :: dataList[id=1031602].name
   limit: do 60 znaków
   EN: Ho, Young Sinclair! Thou Must Keep Apace!!
   PL: Ho, Młody Sinclairze! Trzymaj Krok!!
819. [Pasywka bojowa (od ulepszenia 1) — opis] 편성창에서\n- <noparse>쐐기 사무소</noparse> 해결사 돈키호테를 편성하면, 자동으로 싱클레어의 인격이 <noparse>쐐기 사무소</noparse> 해결사 싱클레어로 편성됨\n- <noparse>쐐기 사무소</noparse> 해결사 싱클레어가 편성 해제되면, 자동으로 돈키호테의 인격이 <noparse>쐐기 사무소</noparse> 해결사가 아닌 가장 최근 편성했던 인격으로 편성됨 (편성창 진입 시점에 이미 <noparse>쐐기 사무소</noparse> 해결사 인격으로 편성된 상태라면, 편성 해제될 때 LCB 수감자 돈키호테로 편성됨)\n\n턴 시작 시부터 전투 시작 전까지 자신의 속도가 아군 <noparse>쐐기 사무소</noparse> 해결사 싱클레어 인격의 속도보다 느리면, 속도가 같아지도록 자신의 속도가 증가함 (둘 중 하나라도 정신력이 -45이거나 속도 고정 효과가 있으면, 이 효과는 발동하지 않음)
   źródło: Passives.json :: dataList[id=1031602].desc
   limit: do 990 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n
   EN: In the Team Loadout menu:\n- Equipping <noparse>Wedge Office</noparse> Fixer Don Quixote automatically equips Sinclair's Identity as <noparse>Wedge Office</noparse> Fixer Sinclair\n- When <noparse>Wedge Office</noparse> Fixer Sinclair is unequipped, automatically equip the most recently equipped Identity that isn't <noparse>Wedge Office</noparse> Fixer Don Quixote (If <noparse>Wedge Office</noparse> Fixer Don Quixote Identity was already equipped when entering the Team Loadout menu, removing this Identity will automatically equip the LCB Sinner Don Quixote Identity instead)\n\nFrom Turn Start ~ before Combat Start: If this unit's Speed is slower than allied <noparse>Wedge Office</noparse> Fixer Sinclair Identity's Speed, become faster until their Speed values are equal (this effect does not activate if either of the two Identities is at -45 SP, or is under an effect that fixes their Speed)
   PL: W oknie składu drużyny:\n- Przy wybraniu Fiksera Biura Klin Don Quixote Tożsamość Sinclaira zostaje automatycznie ustawiona jako Fikser Biura Klin Sinclair\n- Przy odłożeniu Fiksera Biura Klin Sinclair automatycznie zostaje ustawiona ostatnio wybrana Tożsamość Sinclaira, która nie jest Fikserem Biura Klin Don Quixote (jeżeli w momencie wejścia do okna składu drużyny wybraną Tożsamością był już Fikser Biura Klin Don Quixote, po odłożeniu tej Tożsamości automatycznie ustawia się LCB Grzesznik Don Quixote)\n\nOd początku tury do rozpoczęcia walki: jeżeli Szybkość tej jednostki jest niższa niż Szybkość sojuszniczej Tożsamości Fiksera Biura Klin Sinclair, jej Szybkość rośnie do ich zrównania (efekt nie działa, gdy którakolwiek z tych Tożsamości ma -45 Poczytalności albo jest pod efektem blokującym Szybkość)
820. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 편성 시 싱클레어의 인격이 자동으로 함께 편성됨\n자신의 속도가 싱클레어보다 느리면 속도가 같아지도록 증가
   źródło: Passives.json :: dataList[id=1031602].summary
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When Deployed, automatically Deploy the counterpart Identity for Sinclair\nIf this unit's Speed is slower than Sinclair's, become faster until their Speed values are equal
   PL: Przy przydziale automatycznie przydziela się Tożsamość-parówka Sinclaira\nJeżeli Szybkość tej jednostki jest niższa niż Sinclaira, rośnie do ich zrównania
821. [Pasywka bojowa (od ulepszenia 1) — nazwa] 쐐기 박기
   źródło: Passives.json :: dataList[id=1031603].name
   limit: do 40 znaków
   EN: Wedge Drive
   PL: Wbijanie Klinu
822. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 시작 시 [BattleFieldKnow] 1 얻음\n\n아래 조건 중 하나라도 만족 시, 메인 타겟에게 [WedgeMarkYellow] 1 부여 (턴당 1회)\n- 메인 타겟에게 공격 스킬로 마지막 코인 적중 시\n- 자신의 회피 스킬로 공격자의 스킬의 모든 코인을 회피 성공할 시
   źródło: Passives.json :: dataList[id=1031603].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [BattleFieldKnow], [WedgeMarkYellow]
   znaczenie tagów: [BattleFieldKnow] = 전장 파악 / Field Analysis; [WedgeMarkYellow] = 쐐기 - 돈키호테 / Wedge - Don Quixote
   EN: Turn Start: Gain 1 [BattleFieldKnow]\n\nIf any of the following conditions are met, inflict 1 [WedgeMarkYellow] on the main target (once per turn)\n- On final Coin Hit using an Attack Skill against the main target\n- Upon using this unit's Evade Skill to successfully evade all of the attacker's Coins
   PL: Na początku tury zyskuje 1 [BattleFieldKnow]\n\nJeżeli spełniony jest dowolny z poniższych warunków, nakłada 1 [WedgeMarkYellow] na główny cel (1 raz na turę)\n- Gdy ostatnia moneta Umiejętności ataku trafi główny cel\n- Gdy Umiejętność Uniku pomyślnie uniknie wszystkie monety Umiejętności atakującego
823. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 턴 시작 시 [BattleFieldKnow] 얻음\n조건 만족 시, 메인 타겟에게 [WedgeMarkYellow] 부여
   źródło: Passives.json :: dataList[id=1031603].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [BattleFieldKnow], [WedgeMarkYellow]
   znaczenie tagów: [BattleFieldKnow] = 전장 파악 / Field Analysis; [WedgeMarkYellow] = 쐐기 - 돈키호테 / Wedge - Don Quixote
   EN: Turn Start: Gain [BattleFieldKnow]\nWhen conditions are met, inflict [WedgeMarkYellow] on the main target
   PL: Na początku tury zyskuje [BattleFieldKnow]\nWarunkowo nakłada [WedgeMarkYellow] na główny cel
824. [Pasywka bojowa (od ulepszenia 1) — nazwa] 새벽에 등을 맞대고
   źródło: Passives.json :: dataList[id=1031604].name
   limit: do 50 znaków
   EN: Back-to-back in Dawnbreak's Light
   PL: Ramię w ramię w świetle świtu
825. [Pasywka bojowa (od ulepszenia 1) — opis] 아군 <noparse>새벽 사무소</noparse> 해결사 파우스트 인격이 ‘정오의 해체’ 스킬 사용 시, 해당 스킬의 1코인이 아래 효과 얻음 (턴당 1회)\n- [ComboSkill] : <noparse>쐐기 사무소</noparse> 해결사 돈키호테\n· [OnSucceedAttack] [Combustion] 2 부여, [Combustion] 횟수 2 증가\n· [OnSucceedAttack] [Vibration] 2 부여\n· [OnSucceedAttack] [WedgeMarkYellow] 1 부여\n· [OnSucceedAttack] 아군 <noparse>쐐기 사무소</noparse> 대표 오티스 인격의 [ComboWedgeDawn] 1 증가
   źródło: Passives.json :: dataList[id=1031604].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [ComboSkill], [OnSucceedAttack], [Combustion], [Vibration], [WedgeMarkYellow], [ComboWedgeDawn]
   znaczenie tagów: [ComboSkill] = 연 / Joint Combo; [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [WedgeMarkYellow] = 쐐기 - 돈키호테 / Wedge - Don Quixote; [ComboWedgeDawn] = 새벽의 유대 / Dawn's Camaraderie
   EN: When the allied <noparse>Dawn Office</noparse> Fixer Faust Identity uses the "Dismemberment at High Noon" Skill, the Skill's Coin 1 gains the following effects (once per turn):\n- [ComboSkill]: <noparse>Wedge Office</noparse> Fixer Don Quixote\n  · [OnSucceedAttack] Inflict 2 [Combustion] and +2 [Combustion] Count\n  · [OnSucceedAttack] Inflict 2 [Vibration]\n  · [OnSucceedAttack] Inflict 1 [WedgeMarkYellow]\n  · [OnSucceedAttack] Allied <noparse>Wedge Office</noparse> Rep Outis Identity gains 1 [ComboWedgeDawn]
   PL: Gdy sojusznicza Tożsamość Fikserki Biura Świtu[TabExplain] Faust użyje Umiejętności „Rozczłonkowanie w Południe”, moneta 1 tej Umiejętności zyskuje poniższe efekty (1 raz na turę):\n- [ComboSkill]: Fikser Biura Klin[TabExplain] Don Quixote\n· [OnSucceedAttack] Nakłada 2 [Combustion] i zwiększa Licznik [Combustion] o 2\n· [OnSucceedAttack] Nakłada 2 [Vibration]\n· [OnSucceedAttack] Nakłada 1 [WedgeMarkYellow]\n· [OnSucceedAttack] Tożsamość sojusznicza <noparse>Biura Klin</noparse> — Szefowa Otis zyskuje 1 [ComboWedgeDawn]
826. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 협공 시 ‘정오의 해체’ 1코인 적중 시 [Combustion], [Vibration], [WedgeMarkYellow] 부여, [Combustion] 횟수 증가, 오티스의 [ComboWedgeDawn] 증가
   źródło: Passives.json :: dataList[id=1031604].summary
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Vibration], [WedgeMarkYellow], [ComboWedgeDawn]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [WedgeMarkYellow] = 쐐기 - 돈키호테 / Wedge - Don Quixote; [ComboWedgeDawn] = 새벽의 유대 / Dawn's Camaraderie
   EN: On Combo Attack, On Hit using the "Dismemberment at High Noon" Skill's Coin 1, inflict [Combustion], [Vibration], [WedgeMarkYellow], and [Combustion] Count; Outis gains [ComboWedgeDawn]
   PL: Przy Wsparciu, gdy moneta 1 „Rozczłonkowania w Południe” trafi, nakłada [Combustion], [Vibration], [WedgeMarkYellow], zwiększa Licznik [Combustion], a Otis zyskuje [ComboWedgeDawn]
827. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Sloth, posiadane 2× Pride) — nazwa] 도시의 사냥꾼
   źródło: Passives.json :: dataList[id=1031601].name
   limit: do 40 znaków
   EN: Hunters of the City
   PL: Łowcy Miasta
828. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Sloth, posiadane 2× Pride) — opis] 전투 종료 시 자신의 [Breath] 위력이 10 이상이면, 다음 턴에 [Agility] 1 얻음\n\n자신의 [Breath] 위력이 20을 초과했으면, 기본 스킬로 가하는 크리티컬 피해량 +(초과한 수치)% (최대 15%)
   źródło: Passives.json :: dataList[id=1031601].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Agility]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: Combat End: At 10+ [Breath] Potency, gain 1 [Agility] next turn\n\nAt more than 20 [Breath] Potency, Base Skills deal +(excess Potency)% damage on Critical Hit (max 15%)
   PL: Na koniec walki przy 10+ Mocy [Breath] zyskuje w następnej turze 1 [Agility]\n\nPrzy ponad 20 Mocy [Breath] podstawowe Umiejętności zadają +(nadwyżka)% więcej obrażeń przy trafieniu krytycznym (maks. 15%)
829. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Sloth, posiadane 2× Pride) — podsumowanie] [Breath] 위력이 일정 수치 이상이면 다음 턴에 [Agility] 얻음\n[Breath] 위력이 일정 수치를 초과하면 기본 스킬로 가하는 크리티컬 피해량 증가[TabExplain]
   źródło: Passives.json :: dataList[id=1031601].summary
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Agility], [TabExplain]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: At sufficient [Breath] Potency, gain [Agility] next turn\nAt excess [Breath] Potency, Base Skills deal more damage on Critical Hit
   PL: Przy wystarczającej Mocy [Breath] zyskuje w następnej turze [Agility]\nPrzy nadwyżce Mocy [Breath] podstawowe Umiejętności zadają więcej obrażeń krytycznych[TabExplain]
830. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Sloth, posiadane 2× Pride) — tekst klimatyczny] 도시의 밤거리는 언제나 비열하고 야만적인 것들로 우글거린다.\n인생 역전을 노리는 쥐들부터 복수를 꿈꾸는 뒷골목 주민, 이권을 다투는 조직들과 손가락 그리고 청소부까지.\n그렇기에 밤에 이루어지는 의뢰는 대개 보수가 높음에도 인기가 없다.\n하지만 그런 심야의 의뢰를 기회로 여기는 자들도 있다.\n뛰어난 상황 판단 능력과 우환을 남기지 않는 신속하고 빈틈없는 마무리.\n그 두 가지를 무기로 쐐기 사무소는 매번 살아남아 높은 보수를 챙겨 왔다.
   źródło: Passives.json :: dataList[id=1031601].flavor
   limit: do 1020 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The streets of the City are never short of vile and savage company after dark. Rats desperate to turn their lives around, denizens of the Backstreets harboring dreams of revenge, Syndicates and Fingers embroiled in struggles over their interests... and, of course, the Sweepers.\n\nFor all the fortunes to be made from working after sundown, few Fixers are eager to accept such contracts. There are, however, those who find their greatest opportunities precisely where others dare not tread.\n\nThe discernment to read any situation with remarkable precision. The swiftness and thoroughness to bring a job to its conclusion without inviting further trouble. With these two qualities as its greatest assets, Wedge Office has weathered every contract and walked away with the handsome compensation that follows.
   PL: Nocturne w mieście zawsze roi się od podłych i dzikich istot. Od szczurów dążących do odwrócenia losu, przez mieszkańców Zaułków karmionych marzeniami o zemście, po Syndykaty i Palce spłatające z siebie i na siebie intrygi... i oczywiście Zamiataczy.\n\nMimo że nocne zlecenia zwykle dobrze płacą, niewielu fikserów chce je przyjmować. Są jednak tacy, którzy w nocnych zleceniach widzą swoją największą szansę.\nPrzenikliwość pozwalająca odczytać każdą sytuację ze zdumiewającą precyzją. Szybkość i dokładność, dzięki którym sprawa dobiega końca bez rodzenia kolejnych kłopotów. Z tymi dwoma atutami Biuro Klin przeżyło każdy kontrakt i odchodziło z bogatą rekompensatą, która szła za nimi.
831. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Sloth, posiadane 2× Pride) — nazwa] 도시의 사냥꾼
   źródło: Passives.json :: dataList[id=1031611].name
   (powtórzenie elementu 827 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Sloth, posiadane 2× Pride) — opis] 전투 종료 시 자신의 [Breath] 위력이 10 이상이면, 다음 턴에 [Agility] 1 얻음\n\n자신의 [Breath] 위력이 20을 초과했으면, 기본 스킬로 가하는 크리티컬 피해량 +(초과한 수치)% (최대 25%)
   źródło: Passives.json :: dataList[id=1031611].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Agility]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: Combat End: At 10+ [Breath] Potency, gain 1 [Agility] next turn\n\nAt more than 20 [Breath] Potency, Base Skills deal +(excess Potency)% damage on Critical Hit (max 25%)
   PL: Na koniec walki przy 10+ Mocy [Breath] zyskuje w następnej turze 1 [Agility]\n\nPrzy ponad 20 Mocy [Breath] podstawowe Umiejętności zadają +(nadwyżka)% więcej obrażeń przy trafieniu krytycznym (maks. 25%)
833. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Sloth, posiadane 2× Pride) — podsumowanie] [Breath] 위력이 일정 수치 이상이면 다음 턴에 [Agility] 얻음\n[Breath] 위력이 일정 수치를 초과하면 기본 스킬로 가하는 크리티컬 피해량 증가[TabExplain]
   źródło: Passives.json :: dataList[id=1031611].summary
   (powtórzenie elementu 829 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Sloth, posiadane 2× Pride) — tekst klimatyczny] 도시의 밤거리는 언제나 비열하고 야만적인 것들로 우글거린다.\n인생 역전을 노리는 쥐들부터 복수를 꿈꾸는 뒷골목 주민, 이권을 다투는 조직들과 손가락 그리고 청소부까지.\n그렇기에 밤에 이루어지는 의뢰는 대개 보수가 높음에도 인기가 없다.\n하지만 그런 심야의 의뢰를 기회로 여기는 자들도 있다.\n뛰어난 상황 판단 능력과 우환을 남기지 않는 신속하고 빈틈없는 마무리.\n그 두 가지를 무기로 쐐기 사무소는 매번 살아남아 높은 보수를 챙겨 왔다.
   źródło: Passives.json :: dataList[id=1031611].flavor
   (powtórzenie elementu 830 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
835. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Sloth) — nazwa] 사전 정찰
   źródło: Passives.json :: dataList[id=1031621].name
   limit: do 40 znaków
   EN: Reconnaissance
   PL: Rozpoznanie Pola Bojowego
836. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Sloth) — opis] 속도가 가장 빠른 아군 1명이 합을 진행하는 스킬 사용 시, 합을 하는 대상에게 [Vibration] 위력 3 부여 (턴당 1회, 집중 전투면, 부위로 판정)
   źródło: Passives.json :: dataList[id=1031621].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: When 1 ally with the fastest Speed uses a Skill to Clash, inflict 3 [Vibration] Potency on the target of the Clash (once per turn; for Focused Encounters, the Part)
   PL: Gdy 1 Sojusznik z najwyższą Szybkością użyje Umiejętności do Starcia, nakłada 3 Mocy [Vibration] na przeciwnika w Starciu (1 raz na turę; w walce skupionej: część ciała)
837. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Sloth) — podsumowanie] 속도가 가장 빠른 아군이 합을 진행하는 스킬 사용 시 대상에게 [Vibration] 위력 부여
   źródło: Passives.json :: dataList[id=1031621].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: The fastest ally inflicts [Vibration] Potency against the target it's Clashing against
   PL: Najszybszy sojusznik nakłada Moc [Vibration] na przeciwnika, z którym prowadzi Starcie

## [?] Early Elephants Sinnerling — Don Quixote — 코끼리반 수감생
- ID Tożsamości: `400027` (plik: `Personalities-x1p1c1.json`)

838. [Karta Tożsamości — tytuł] 코끼리반 수감생
   źródło: Personalities-x1p1c1.json :: dataList[id=400027].title
   limit: do 40 znaków
   EN: Early Elephants Sinnerling
   PL: Grzesznik Grupy Słoników
839. [Karta Tożsamości — nazwa] 돈키호테
   źródło: Personalities-x1p1c1.json :: dataList[id=400027].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Karta Tożsamości — nazwa z tytułem] 돈키호테
   źródło: Personalities-x1p1c1.json :: dataList[id=400027].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [Karta Tożsamości — opis] 돈키호테의 ??? 인격
   źródło: Personalities-x1p1c1.json :: dataList[id=400027].desc
   limit: do 120 znaków
   EN: Don Quixote's ??? Identity
   PL: Tożsamość ??? Don Quixote
842. [Pasywka bojowa [40002701] — nazwa] 쩡이의 응징
   źródło: Passives-x1p1c1.json :: dataList[id=40002701].name
   limit: do 40 znaków
   EN: Wicheous Retwibyushun
   PL: Wicheous Retwibyushun
843. [Pasywka bojowa [40002701] — opis] 합 승리 시 해당 스킬의 피해량 +10%
   źródło: Passives-x1p1c1.json :: dataList[id=40002701].desc
   limit: do 120 znaków
   EN: On Clash Win, deal +10% damage with the Skill
   PL: Po wygranym Starciu zadaje +10% obrażeń tą Umiejętnością
844. [Pasywka bojowa [40002702] — nazwa] 응원
   źródło: Passives-x1p1c1.json :: dataList[id=40002702].name
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Pasywka bojowa [40002702] — opis] 정신력이 가장 높은 아군 1명 관통 스킬의 피해량 +10%
   źródło: Passives-x1p1c1.json :: dataList[id=40002702].desc
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
