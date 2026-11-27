# Paczka AI P50 (Fala 3 · 3A) — Grzesznik 08 — Ishmael

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P50_3a_08_ishmael.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P50_3a_08_ishmael.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Grzesznik #08: Ishmael (이스마엘)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 이스마엘
   źródło: Characters.json :: dataList[id=8].name
   limit: do 40 znaków
   EN: Ishmael
   PL: Ishmael
2. [Akta więźnia — nazwa] 이스마엘
   źródło: IntroduceCharacter.json :: dataList[id=이스마엘].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [0] LCB Sinner — Ishmael — LCB 수감자
- ID Tożsamości: `10801` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 78 · szybkość: 5–6 / 5–7 / 5–8 / 5–8
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor

3. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10801].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL: LCB\nGrzesznik
4. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10801].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
5. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10801].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — opis] 이스마엘의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10801].desc
   limit: do 120 znaków
   EN: Ishmael’s 1st Identity
   PL: Pierwsza Tożsamość Ishmael
7. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 강타
   źródło: Skills.json :: dataList[id=1080101].levelList[level=1].name ; dataList[id=1080101].levelList[level=2].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Loggerhead
   PL: Hak
8. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttackHead] Nakłada +1 Licznika Wstrząsu
9. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]
10. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 슬라이딩
   źródło: Skills.json :: dataList[id=1080102].levelList[level=1].name ; dataList[id=1080102].levelList[level=2].name ; dataList[id=1080102].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 6 · monety: 1 (+9)
   limit: do 40 znaków
   EN: Slide
   PL: Ślizg
11. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 수비 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1080102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Inflict 1 Defense Power Down
   PL: [WinDuel] Nakłada 1 Spadek Mocy Obrony
12. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WinDuel] 수비 위력 감소 3 부여
   źródło: Skills.json :: dataList[id=1080102].levelList[level=2].desc ; dataList[id=1080102].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Inflict 3 Defense Power Down
   PL: [WinDuel] Nakłada 3 Spadek Mocy Obrony
13. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills.json :: dataList[id=1080102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] Nakłada 3 [Vibration]
14. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 방어
   źródło: Skills.json :: dataList[id=1080103].levelList[level=3].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 8 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Shield Bash
   PL: Garda
15. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발. 타격 취약 1 부여
   źródło: Skills.json :: dataList[id=1080103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; Inflict 1 Blunt Fragility
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Nakłada 1 Wrażliwości na Uderzenie
16. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1080104].levelList[level=1].name
   kontekst: grzech: Wrath · typ: obrona: blok · moc bazowa: 7 · monety: 1 (+3)
   limit: do 40 znaków
   EN: Guard
   PL: Blok
17. [Pasywka bojowa (od ulepszenia 1, posiadane 3× Wrath) — nazwa] 발악
   źródło: Passives.json :: dataList[id=1080101].name
   limit: do 40 znaków
   EN: Last-ditch Struggle
   PL: Ostatnie Zrywy
18. [Pasywka bojowa (od ulepszenia 1, posiadane 3× Wrath) — opis] 합 진행 시 자신의 체력이 25% 미만이면 합 위력 +1
   źródło: Passives.json :: dataList[id=1080101].desc
   limit: do 120 znaków
   EN: At less than 25% HP, gain +1 clash Power in a clash.
   PL: Przy HP poniżej 25% zyskuje Moc Starcia +1 w starciu
19. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Wrath) — nazwa] 살아남고 말것이라는 마음
   źródło: Passives.json :: dataList[id=1080121].name
   limit: do 40 znaków
   EN: Determination to Survive
   PL: Postanowienie Przetrwania
20. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Wrath) — opis] 현재 체력이 가장 낮은 아군 1명 체력이 50% 미만이면 합 진행 시 합 위력 +1
   źródło: Passives.json :: dataList[id=1080121].desc
   limit: do 120 znaków
   EN: 1 ally with the least HP and less than 50% of Max HP gains +1 Clash Power in a clash.
   PL: Sojusznik z najniższym HP poniżej 50% Maks. HP zyskuje Moc Starcia +1 w starciu

## [000] R Corp. 4th Pack Reindeer — Ishmael — R사 제 4무리 순록팀
- ID Tożsamości: `10802` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 79 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Charge, Sinking

21. [Karta Tożsamości — tytuł] R사 제 4무리\n순록팀
   źródło: Personalities.json :: dataList[id=10802].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: R Corp. 4th Pack\nReindeer
   PL: R Corp. 4 Pack\nZespół Reniferów
22. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10802].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
23. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10802].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
24. [Karta Tożsamości — opis] 이스마엘의 두번째 인격
   źródło: Personalities.json :: dataList[id=10802].desc
   limit: do 120 znaków
   EN: Ishmael’s 2nd Identity
   PL: Druga Tożsamość Ishmael
25. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 정신 가격
   źródło: Skills.json :: dataList[id=1080201].levelList[level=1].name ; dataList[id=1080201].levelList[level=2].name ; dataList[id=1080201].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Mind Strike
   PL: Cios w Umysł
26. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 1 [Sinking]
   PL: [OnSucceedAttackHead] Nakłada 1 Zatonięcia
27. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
28. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] Nakłada 1 Zatonięcia
29. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080201].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +2 Charge Count
   PL: [OnSucceedAttackHead] Zyskuje +2 Licznika Ładowania
30. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
31. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080201].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
32. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080201].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Charge Count
   PL: [WhenUse] Zyskuje +2 Licznika Ładowania
33. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080201].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +2 Charge Count
   PL: [OnSucceedAttack] Zyskuje +2 Licznika Ładowania
34. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
35. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 지져내기
   źródło: Skills.json :: dataList[id=1080202].levelList[level=1].name ; dataList[id=1080202].levelList[level=2].name ; dataList[id=1080202].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 6 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Flaying Surge
   PL: Przezdzieranie
36. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 횟수 3 증가
   źródło: Skills.json :: dataList[id=1080202].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttackHead] Nakłada +3 Licznika Zatonięcia
37. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 충전 횟수 5 증가
   źródło: Skills.json :: dataList[id=1080202].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +5 Charge Count
   PL: [WhenUse] Zyskuje +5 Licznika Ładowania
38. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 7 증가
   źródło: Skills.json :: dataList[id=1080202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +7 Charge Count
   PL: [WhenUse] Zwiększa własny Licznik Ładowania o 7
39. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 3 증가
   źródło: Skills.json :: dataList[id=1080202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika Zatonięcia
40. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 정신 채찍
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].name ; dataList[id=1080203].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 2 · monety: 4 (+6)
   limit: do 40 znaków
   EN: Mind Whip
   PL: Bicz na Umysł
41. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] 충전 횟수 전부 소모.\n전투 시작 시 충전 횟수가 10 미만이면 무작위 대상 일방 공격
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Spend all Charge Count\nIf at less than 10 Charge Count at Combat Start, target a random unit for an unopposed attack
   PL: [StartBattle] Zużywa cały Licznik Ładowania.\nJeżeli na początku walki ma mniej niż 10 Licznika Ładowania, atakuje nieoparciego losowego celu
42. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1080203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 40%만큼 흐트러짐 손상을 입힘
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1080203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 40% of damage dealt
   PL: [OnSucceedAttack] Podnosi Próg Oszołomienia o 40% zadanych obrażeń
44. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1080203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량의 30%만큼 흐트러짐 손상을 입힘
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1080203].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 30% of damage dealt
   PL: [OnSucceedAttack] Podnosi Próg Oszołomienia o 30% zadanych obrażeń
46. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1080203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상을 입힘
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1080203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 20% of damage dealt
   PL: [OnSucceedAttack] Podnosi Próg Oszołomienia o 20% zadanych obrażeń
48. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1080203].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상을 입힘
   źródło: Skills.json :: dataList[id=1080203].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1080203].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 10% of damage dealt
   PL: [OnSucceedAttack] Podnosi Próg Oszołomienia o 10% zadanych obrażeń
50. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [StartBattle] 충전 횟수 8 소모.\n전투 시작 시 충전 횟수가 8 미만이면 무작위 대상 일방 공격
   źródło: Skills.json :: dataList[id=1080203].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Spend 8 Charge Count\nIf at less than 8 Charge Count at Combat Start, target a random unit for an unopposed attack
   PL: [StartBattle] Zużywa 8 Licznika Ładowania.\nJeżeli na początku walki ma mniej niż 8 Licznika Ładowania, atakuje nieoparciego losowego celu
51. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1080204].levelList[level=1].name ; dataList[id=1080204].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL: Unik
52. [Obrona (ulepszenie 4) — opis] [OnSucceedEvade] 자신의 충전 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080204].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Gain +1 Charge Count
   PL: [OnSucceedEvade] Zwiększa własny Licznik Ładowania o 1
53. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — nazwa] 뇌파집속
   źródło: Passives.json :: dataList[id=1080201].name
   limit: do 40 znaków
   EN: Brainwave Focus
   PL: Skupienie Fal Mózgowych
54. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — opis] 전투 시작 시 정신력 -15.\n다음 턴 시작 시 공격 위력 증가를 (우울 공명 수/3)만큼 얻음
   źródło: Passives.json :: dataList[id=1080201].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the combat phase, lose 15 SP.\nGain (Gloom Res / 3) Attack Power Up next turn.
   PL: Na początku walki traci 15 Poczytalności.\nNa początku następnej tury zyskuje Wzrost Mocy Ataku równy (Rezonans Posępności/3)
55. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — nazwa] 집념
   źródło: Passives.json :: dataList[id=1080221].name
   limit: do 40 znaków
   EN: Tenacity
   PL: Upór
56. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — opis] 정신력이 가장 낮은 아군 1명 타격 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1080221].desc
   limit: do 120 znaków
   EN: 1 ally with the least SP deals +10% Blunt damage.
   PL: 1 Sojusznik z najniższą Poczytalnością zadaje +10% obrażeń Uderzenia.

## [00] Shi Assoc. South Section 5 — Ishmael — 남부 시 협회 5과
- ID Tożsamości: `10803` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Poise

57. [Karta Tożsamości — tytuł] 남부 시 협회\n5과
   źródło: Personalities.json :: dataList[id=10803].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Shi Assoc.\nSouth Section 5
   PL: Południowe Stowarzyszenie Shi\nSekcja 5
58. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10803].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10803].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [Karta Tożsamości — opis] 이스마엘의 세번째 인격
   źródło: Personalities.json :: dataList[id=10803].desc
   limit: do 120 znaków
   EN: Ishmael’s 3rd Identity
   PL: Trzecia Tożsamość Ishmael
61. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 비검
   źródło: Skills.json :: dataList[id=1080301].levelList[level=1].name ; dataList[id=1080301].levelList[level=2].name ; dataList[id=1080301].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Flying Sword
   PL: Latający Miecz
62. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1080301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 2 [Breath]
   PL: [OnSucceedAttackHead] Zyskuje 2 Oddechu
63. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 자신의 체력이 50%미만일 때 이 스킬로 얻는 호흡 +1
   źródło: Skills.json :: dataList[id=1080301].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At less than 50% HP, this skill gives 1 additional [Breath]
   PL: Przy HP poniżej 50% zyskuje o 1 więcej Oddechu z tej Umiejętności
64. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1080301].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080301].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL: [OnSucceedAttack] Zyskuje 2 Oddechu
65. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 체력이 50%미만일 때 이 스킬로 얻는 호흡 +3
   źródło: Skills.json :: dataList[id=1080301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At less than 50% HP, this skill gives 3 additional [Breath]
   PL: Przy HP poniżej 50% zyskuje o 3 więcej Oddechu z tej Umiejętności
66. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 섬격
   źródło: Skills.json :: dataList[id=1080302].levelList[level=1].name ; dataList[id=1080302].levelList[level=2].name ; dataList[id=1080302].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Flashing Strike
   PL: Błyskawiczne Uderzenie
67. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain +1 [Breath] Count
   PL: [OnSucceedAttackHead] Zwiększa własny Licznik Oddechu o 1
68. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WhenUse] 자신의 체력이 50%미만일 때, 스킬의 1, 2코인이 추가됨
   źródło: Skills.json :: dataList[id=1080302].levelList[level=2].desc ; dataList[id=1080302].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At less than 50% HP, use Coin 1 and 2 an additional time
   PL: [WhenUse] Przy HP poniżej 50% monety 1 i 2 są używane dodatkowo
70. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik Oddechu o 1
71. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +2 Licznika Oddechu
73. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 호흡 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 숨고르기
   źródło: Skills.json :: dataList[id=1080303].levelList[level=3].name ; dataList[id=1080303].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 6 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Catch Breath
   PL: Wyrównanie Oddechu
75. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1080303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1080303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] 체력이 25%미만일 때, 피해량의 100%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1080303].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1080303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] At less than 25% HP, heal 100% of damage dealt
   PL: [CriticalOnSucceedAttack] Przy HP poniżej 25% odzyskuje HP równe 100% zadanych obrażeń
77. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 호흡 횟수가 5 이상이면, 크리티컬 피해량 +50%
   źródło: Skills.json :: dataList[id=1080303].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 5+ [Breath] Count, +50% Critical Damage
   PL: Przy 5+ Liczniku Oddechu zadaje +50% obrażeń przy trafieniu krytycznym
78. [Obrona (ulepszenia 1,4) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1080304].levelList[level=1].name ; dataList[id=1080304].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 8 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Counter
   PL: Kontra
79. [Obrona (ulepszenie 4) — opis] 자신의 호흡 횟수가 5 이상이면, 크리티컬 피해량 +50%
   źródło: Skills.json :: dataList[id=1080304].levelList[level=4].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL: [OnSucceedAttack] Zwiększa Licznik Oddechu o 1
81. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Envy) — nazwa] 사선발악
   źródło: Passives.json :: dataList[id=1080301].name
   limit: do 40 znaków
   EN: Walking the Line of Death
   PL: Balansowanie na Linii Śmierci
82. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Envy) — opis] 자신의 체력이 50%미만일 때 스킬 효과로 얻는 호흡 +1
   źródło: Passives.json :: dataList[id=1080301].desc
   limit: do 120 znaków
   EN: At less than 50% HP, gain 1 additional Poise from skills.
   PL: Przy HP poniżej 50% zyskuje o 1 więcej Oddechu z efektów Umiejętności
83. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Envy) — nazwa] 투쟁
   źródło: Passives.json :: dataList[id=1080321].name
   limit: do 40 znaków
   EN: Strife
   PL: Zmagania
84. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Envy) — opis] 현재 체력이 가장 낮은 아군 1명 반격 스킬의 최종 위력 +2
   źródło: Passives.json :: dataList[id=1080321].desc
   limit: do 120 znaków
   EN: 1 ally with the least HP gains +2 counter skill final Power.
   PL: 1 Sojusznik z najniższym HP: Moc Końcowa Umiejętności Kontry +2

## [00] LCCB Assistant Manager — Ishmael — LCCB 대리
- ID Tożsamości: `10804` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 1 · HP bazowe: 82 · szybkość: 1–5 / 1–5 / 2–6 / 2–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor, Rupture

85. [Karta Tożsamości — tytuł] LCCB\n대리
   źródło: Personalities.json :: dataList[id=10804].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCCB\nAssistant Manager
   PL: LCCB\nZastępca Kierownika
86. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10804].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10804].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Karta Tożsamości — opis] 이스마엘의 네번째 인격
   źródło: Personalities.json :: dataList[id=10804].desc
   limit: do 120 znaków
   EN: Ishmael’s 4th Identity
   PL: Czwarta Tożsamość Ishmael
89. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 밀쳐내기
   źródło: Skills.json :: dataList[id=1080401].levelList[level=1].name ; dataList[id=1080401].levelList[level=2].name ; dataList[id=1080401].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 4 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Shove
   PL: Odepchnięcie
90. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마비 1 부여
   źródło: Skills.json :: dataList[id=1080401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Paralyze
   PL: [OnSucceedAttackHead] Nakłada 1 Paraliżu
91. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills.json :: dataList[id=1080401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze
   PL: [OnSucceedAttack] Nakłada 3 Paraliżu
92. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n대상의 [Vibration]이 8 이상이면, 스킬 위력 +2
   źródło: Skills.json :: dataList[id=1080401].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn\nIf target has 8+ [Vibration], Skill Power +2
   PL: [WhenUse] Zwiększa Prowokację tego slotu Umiejętności o 4 w następnej turze\nJeżeli cel ma 8+ [Vibration], Moc Umiejętności +2
93. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 진동탄
   źródło: Skills.json :: dataList[id=1080402].levelList[level=1].name ; dataList[id=1080402].levelList[level=2].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Quake Rounds
   PL: Pociski Wstrząsu
94. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1080402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Attack Power Down
   PL: [OnSucceedAttackHead] Nakłada 1 Spadek Mocy Ataku
95. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 진동 4 부여
   źródło: Skills.json :: dataList[id=1080402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: Spend 1 Ammo\n[OnSucceedAttack] Inflict 4 [Vibration]
   PL: Zużywa 1 amunicji.\n[OnSucceedAttack] Nakłada 4 Wstrząsu
96. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 진동 4 부여
   źródło: Skills.json :: dataList[id=1080402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1080402].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Attack Power Down
   PL: [OnSucceedAttack] Nakłada 1 Spadek Mocy Ataku
98. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 진동 8 부여. 진동 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080402].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: Spend 1 Ammo\n[OnSucceedAttack] Inflict 8 [Vibration]; Inflict +2 [Vibration] Count
   PL: Zużywa 1 amunicji.\n[OnSucceedAttack] Nakłada 8 Wstrząsu i zwiększa Licznik Wstrząsu o 2
99. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 진동 8 부여. 진동 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080402].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 제압
   źródło: Skills.json :: dataList[id=1080403].levelList[level=3].name ; dataList[id=1080403].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Suppress
   PL: Powstrzymanie
101. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills.json :: dataList[id=1080403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1080403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL: [OnSucceedAttack] Wybuch Wstrząsu
102. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 파열 4 부여. 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080403].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1080403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: Spend 1 Ammo\n[OnSucceedAttack] Inflict 4 Rupture; Inflict +2 Rupture Count
   PL: Zużywa 1 amunicji.\n[OnSucceedAttack] Nakłada 4 Rozdarcia i zwiększa Licznik Rozdarcia o 2
103. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 파열 4 부여. 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080403].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1080403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 취약 5 부여.
   źródło: Skills.json :: dataList[id=1080403].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1080403].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: Spend 1 Ammo\n[OnSucceedAttack] Inflict 5 Fragile
   PL: Zużywa 1 amunicji.\n[OnSucceedAttack] Nakłada 5 Wrażliwości
105. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 진동 횟수가 5 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1080403].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 5+ [Vibration] Count, Coin Power +1
   PL: Jeżeli cel ma 5+ Licznika Wstrząsu, Moc Monet +1
106. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1080404].levelList[level=1].name ; dataList[id=1080404].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+8)
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n탄환이 0일 때, 도발치 추가 2 증가
   źródło: Skills.json :: dataList[id=1080404].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn\nAt 0 Ammo, gain 2 more Aggro
   PL: [WhenUse] Zwiększa Prowokację tego slotu o 4 w następnej turze\nPrzy 0 amunicji zwiększa ją dodatkowo o 2
108. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — nazwa] 약점포착
   źródło: Passives.json :: dataList[id=1080401].name
   limit: do 40 znaków
   EN: Eye for Weakness
   PL: Wyczuwanie Słabości
109. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — opis] 합 승리 후 공격 적중 시마다 진동 1 부여
   źródło: Passives.json :: dataList[id=1080401].desc
   limit: do 120 znaków
   EN: Attacks inflict 1 Tremor in a won clash.
   PL: Po wygranej w starciu każde trafienie nakłada 1 Wstrząsu
110. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Glut.) — nazwa] 매뉴얼대로
   źródło: Passives.json :: dataList[id=1080421].name
   limit: do 40 znaków
   EN: By the Manual
   PL: Zgodnie z Instrukcją
111. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Glut.) — opis] 속도가 가장 낮은 아군 1명 가드 스킬의 최종 위력 +2
   źródło: Passives.json :: dataList[id=1080421].desc
   limit: do 120 znaków
   EN: 1 ally with the slowest Speed gains +2 guard skill final Power.
   PL: 1 Sojusznik z najniższą Szybkością: Moc Końcowa Umiejętności Gardy +2

## [00] Lobotomy E.G.O::Sloshing — Ishmael — 로보토미 E.G.O:: 출렁임
- ID Tożsamości: `10805` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 2 · HP bazowe: 90 · szybkość: 1–6 / 2–6 / 2–7 / 2–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Tremor, Rupture

112. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n출렁임
   źródło: Personalities.json :: dataList[id=10805].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::Sloshing
   PL: Lobotomy E.G.O::\nChlupot
113. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10805].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10805].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Karta Tożsamości — opis] 이스마엘의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10805].desc
   limit: do 120 znaków
   EN: Ishmael’s 5th Identity
   PL: Piąta Tożsamość Ishmael
116. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 무거워...!
   źródło: Skills.json :: dataList[id=1080501].levelList[level=1].name ; dataList[id=1080501].levelList[level=2].name ; dataList[id=1080501].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 1 (+6)
   limit: do 40 znaków
   EN: It's Heavy...!
   PL: Ciężkie...!
117. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1080501].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 1 [Vibration]
   PL: [OnSucceedAttackHead] Nakłada 1 [Vibration]
119. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080501].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1080501].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n[DefeatDuel] 진동 2, 파열 2 부여
   źródło: Skills.json :: dataList[id=1080501].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn\n[DefeatDuel] Inflict 2 [Vibration] and 2 Rupture
   PL: [WhenUse] Zwiększa Prowokację tego slotu Umiejętności o 4 w następnej turze\n[DefeatDuel] Nakłada 2 Wstrząsu i 2 Rozdarcia
121. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 울렁거려...!
   źródło: Skills.json :: dataList[id=1080502].levelList[level=1].name ; dataList[id=1080502].levelList[level=2].name ; dataList[id=1080502].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: It's Churning...!
   PL: Coś się burzy...!
122. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1080502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills.json :: dataList[id=1080502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 2 [Vibration]
   PL: [OnSucceedAttackHead] Nakłada 2 [Vibration]
124. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills.json :: dataList[id=1080502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]
125. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills.json :: dataList[id=1080502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
126. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n[DefeatDuel] 진동 3, 파열 3 부여
   źródło: Skills.json :: dataList[id=1080502].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn\n[DefeatDuel] Inflict 3 [Vibration] and 3 Rupture
   PL: [WhenUse] Zwiększa Prowokację tego slotu Umiejętności o 4 w następnej turze\n[DefeatDuel] Nakłada 3 Wstrząsu i 3 Rozdarcia
127. [Umiejętność 3 (×1) (ulepszenia 1,4) — nazwa] 부식성 점액 타격
   źródło: Skills.json :: dataList[id=1080503].levelList[level=1].name ; dataList[id=1080503].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 6 · monety: 1 (+16)
   limit: do 40 znaków
   EN: Corrosive Splash
   PL: Cios Żrącego Śluzu
128. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발\n진동 폭발 시 진동 횟수 4 감소. 파열 5 부여
   źródło: Skills.json :: dataList[id=1080503].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]\nAfter triggering [VibrationExplosion], reduce [Vibration] Count by 4. Inflict 5 Rupture
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]\nPo wywołaniu [VibrationExplosion] zmniejsza Licznik Wstrząsu o 4. Nakłada 5 Rozdarcia
129. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n[DefeatDuel] 진동 5, 파열 5 부여
   źródło: Skills.json :: dataList[id=1080503].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn\n[DefeatDuel] Inflict 5 [Vibration] and 5 Rupture
   PL: [WhenUse] Zwiększa Prowokację tego slotu Umiejętności o 4 w następnej turze\n[DefeatDuel] Nakłada 5 Wstrząsu i 5 Rozdarcia
130. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1080504].levelList[level=1].name ; dataList[id=1080504].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가
   źródło: Skills.json :: dataList[id=1080504].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn
   PL: [WhenUse] Zwiększa Prowokację tego slotu Umiejętności o 4 w następnej turze
132. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Gloom) — nazwa] 차오르는 액체
   źródło: Passives.json :: dataList[id=1080501].name
   limit: do 40 znaków
   EN: Filling Fluid
   PL: Nabierający Płyn
133. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Gloom) — opis] 공격 스킬로 대상의 체력에 피해를 주지 못한 경우, 다음 턴에 최대 체력의 5%만큼 보호막을 얻음 (최대 30)
   źródło: Passives.json :: dataList[id=1080501].desc
   limit: do 160 znaków
   EN: If this unit fails to deal HP damage using attack skills in a turn, gain a Shield equal to 5% of Max HP next turn. (Max 30)
   PL: Jeżeli w turze nie zada obrażeń HP Umiejętnością ataku, zyskuje w następnej turze Tarczę równą 5% Maks. HP (maks. 30)
134. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — nazwa] 부식 점액
   źródło: Passives.json :: dataList[id=1080521].name
   limit: do 40 znaków
   EN: Corrosive Slime
   PL: Żrący Śluz
135. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — opis] 속도가 가장 빠른 아군 1명이 진동 폭발 발동 시 파열 2 부여
   źródło: Passives.json :: dataList[id=1080521].desc
   limit: do 120 znaków
   EN: When 1 ally with the fastest Speed triggers Tremor Burst, they inflict 2 Rupture.
   PL: Gdy 1 Sojusznik z najwyższą Szybkością wywołuje [VibrationExplosion], nakłada 2 Rozdarcia

## [000] Liu Assoc. South Section 4 — Ishmael — 남부 리우 협회 4과
- ID Tożsamości: `10806` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 79 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Burn

136. [Karta Tożsamości — tytuł] 남부 리우 협회\n4과
   źródło: Personalities.json :: dataList[id=10806].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Liu Assoc.\nSouth Section 4
   PL: Południowe Stowarzyszenie Liu\nSekcja 4
137. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10806].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10806].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Karta Tożsamości — opis] 이스마엘의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10806].desc
   limit: do 120 znaków
   EN: Ishmael’s 6th Identity
   PL: Szósta Tożsamość Ishmael
140. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 단각
   źródło: Skills.json :: dataList[id=1080601].levelList[level=1].name ; dataList[id=1080601].levelList[level=2].name ; dataList[id=1080601].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Red Kick
   PL: Czerwony Kopniak
141. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1080601].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Burn
   PL: [OnSucceedAttack] Nakłada 1 Podpalenia
142. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1080601].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Combustion]이 3 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1080601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 3+ [Combustion], Coin Power +1
   PL: Jeżeli cel ma 3+ [Combustion], Moc Monet +1
144. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 화상 3당, 코인 위력 +1 (최대 2)
   źródło: Skills.json :: dataList[id=1080601].levelList[level=4].desc
   limit: do 120 znaków
   EN: Coin Power +1 for every 3 Burn on target (Max 2)
   PL: Moc Monet +1 za każde 3 Podpalenia celu (maks. 2)
145. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 정면 돌파
   źródło: Skills.json :: dataList[id=1080602].levelList[level=1].name ; dataList[id=1080602].levelList[level=2].name ; dataList[id=1080602].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Frontal Assault
   PL: Atak Czołowy
146. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1080602].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1080602].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 화상 횟수 2 부여
   źródło: Skills.json :: dataList[id=1080602].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1080602].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1080602].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], inflict 2 Burn Count
   PL: [OnSucceedAttack] Jeżeli cel ma 6+ [Combustion], nakłada 2 Licznika Podpalenia
149. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Combustion]이 6 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1080602].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Coin Power +1
   PL: Jeżeli cel ma 6+ [Combustion], Moc Monet +1
150. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 화상 6 당, 코인 위력 +1 (최대 2)
   źródło: Skills.json :: dataList[id=1080602].levelList[level=4].desc
   limit: do 120 znaków
   EN: Coin Power +1 for every 6 Burn on target (Max 2)
   PL: Moc Monet +1 za każde 6 Podpalenia celu (maks. 2)
151. [Umiejętność 3 (×1) (ulepszenia 1,4) — nazwa] 이문정주
   źródło: Skills.json :: dataList[id=1080603].levelList[level=1].name ; dataList[id=1080603].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 3 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Inner Gate Elbow Strike
   PL: Łokieć Wewnętrznej Bramy
152. [Umiejętność 3 (×1) (ulepszenie 1) — opis] 대상의 화상과 화상 횟수가 6 이상이면, 피해량 +30%
   źródło: Skills.json :: dataList[id=1080603].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target has 6+ Burn and Burn Count, deal +30% damage
   PL: Przy 6+ (suma Podpalenia i Licznika Podpalenia celu) zadaje +30% obrażeń
153. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1080603].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1080603].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 2 증가
   źródło: Skills.json :: dataList[id=1080603].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1080603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Burn Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika Podpalenia
156. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 4, efekt 1 — opis] [EndSkill] 대상이 흐트러짐 상태가 되거나 사망하면, 다음 턴에 더하기 코인 강화 1을 얻음
   źródło: Skills.json :: dataList[id=1080603].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=1080603].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] If target is Staggered or defeated, gain 1 Plus Coin Boost next turn
   PL: [EndSkill] Jeżeli cel zostaje Ogłuszony albo ginie, zyskuje 1 Wzmocnienie Monet Plus w następnej turze
157. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 화상과 화상 횟수가 6 이상이면, 피해량 +50%
   źródło: Skills.json :: dataList[id=1080603].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target has 6+ Burn and Burn Count, deal +50% damage
   PL: Przy 6+ (suma Podpalenia i Licznika Podpalenia celu) zadaje +50% obrażeń
158. [Obrona (ulepszenie 1) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1080604].levelList[level=1].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 9 · monety: 1 (+7)
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 1 증가
   źródło: Skills.json :: dataList[id=1080604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Burn Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika Podpalenia
160. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — nazwa] 격화
   źródło: Passives.json :: dataList[id=1080601].name
   limit: do 40 znaków
   EN: Intense Blaze
   PL: Gwałtowny Żar
161. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — opis] 대상의 화상 횟수 3 당 타격 피해량 +10% (최대 30%)
   źródło: Passives.json :: dataList[id=1080601].desc
   limit: do 120 znaków
   EN: Deal +10% Blunt damage for every 3 Burn Count on target. (Max 30%)
   PL: Zadaje +10% obrażeń Uderzenia za każde 3 Licznika Podpalenia celu (maks. 30%)
162. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Wrath) — nazwa] 격화
   źródło: Passives.json :: dataList[id=1080621].name
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Wrath) — opis] 속도가 가장 느린 아군 1명이 공격 적중 시 대상의 화상 횟수 3 당 타격 피해량 +5% (최대 15%)
   źródło: Passives.json :: dataList[id=1080621].desc
   limit: do 130 znaków
   EN: 1 ally with the slowest Speed deals +5% Blunt damage for every 3 Burn Count on target. (Max 15%)
   PL: 1 Sojusznik z najniższą Szybkością zadaje +5% obrażeń Uderzenia za każde 3 Licznika Podpalenia celu (maks. 15%)

## [000] Molar Boatworks Fixer — Ishmael — 어금니 보트 센터 해결사
- ID Tożsamości: `10807` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 2 · HP bazowe: 70 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Sinking, Tremor

164. [Karta Tożsamości — tytuł] 어금니 보트 센터\n해결사
   źródło: Personalities.json :: dataList[id=10807].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Molar Boatworks\nFixer
   PL: Centrum Łodzi Trzonowca\nFikser
165. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10807].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10807].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Karta Tożsamości — opis] 이스마엘의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10807].desc
   limit: do 120 znaków
   EN: Ishmael’s 7th Identity
   PL: Siódma Tożsamość Ishmael
168. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 파쇄 준비
   źródło: Skills_personality-08.json :: dataList[id=1080701].levelList[level=1].name ; dataList[id=1080701].levelList[level=2].name ; dataList[id=1080701].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Ready to Crush
   PL: Gotów do Miażdżenia
169. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 진동 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1080701].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080701].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +3 Tremor Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik Wstrząsu o 3
170. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 침잠 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080701].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080701].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +2 Sinking Count
   PL: [OnSucceedAttackHead] Nakłada +2 Licznika Zatonięcia
171. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] [WhenUse] 자신의 진동 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1080701].levelList[level=2].desc ; dataList[id=1080701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +3 Tremor Count
   PL: [WhenUse] Zwiększa własny Licznik Wstrząsu o 3
172. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Sinking Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika Zatonięcia
173. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 작렬
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=1].name ; dataList[id=1080702].levelList[level=2].name ; dataList[id=1080702].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 5 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Explosive Blast
   PL: Wybuchowe Uderzenie
174. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Tremor Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika Wstrząsu
175. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 6 부여
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 6 Sinking
   PL: [OnSucceedAttack] Nakłada 6 Zatonięcia
176. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 방어 레벨 감소 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Defense Level Down next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze 2 Spadki Poziomu Obrony
177. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] 자신의 진동 횟수가 5 이상이면, 코인 위력 +1
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=2].desc ; dataList[id=1080702].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 5+ Tremor Count, Coin Power +1
   PL: Przy 5+ Liczniku Wstrząsu Moc Monet +1
178. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Tremor Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika Wstrząsu
179. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 진동 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1080702].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +2 Tremor Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik Wstrząsu o 2
180. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 감소 3 부여
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Defense Level Down next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 3 Spadku Poziomu Obrony
181. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 감소 4 부여
   źródło: Skills_personality-08.json :: dataList[id=1080702].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Defense Level Down next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 4 Spadki Poziomu Obrony
182. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 과격한 판단
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].name ; dataList[id=1080703].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 3 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Risky Judgement
   PL: Ryzykowny Osąd
183. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 진동 횟수가 5 이상이면, 코인 위력 +1\n대상의 침잠이 6 이상이면, 피해량 +20%
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 5+ Tremor Count, Coin Power +1\nIf target has 6+ Sinking, deal +20% damage
   PL: Przy 5+ Liczniku Wstrząsu Moc Monet +1\nJeżeli cel ma 6+ Zatonięcia, zadaje +20% obrażeń
184. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 횟수 5 증가
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1080703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +5 Sinking Count
   PL: [OnSucceedAttack] Nakłada +5 Licznika Zatonięcia
185. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1080703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Sinking
   PL: [OnSucceedAttack] Nakłada 3 Zatonięcia
186. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 진동 횟수 5를 소모하여 다음 턴에 취약 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1080703].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 5 Tremor Count to inflict 1 Fragile next turn
   PL: [OnSucceedAttack] Zużywa 5 Licznika Wstrząsu, aby nakładać w następnej turze 1 Wrażliwość
187. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 침잠 3 부여
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1080703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 진동 횟수 5를 소모하여 다음 턴에 취약 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1080703].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 5 Tremor Count to inflict 2 Fragile next turn
   PL: [OnSucceedAttack] Zużywa 5 Licznika Wstrząsu, aby nakładać w następnej turze 2 Wrażliwości
189. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 진동 횟수가 5 당, 코인 위력 +1(최대 2)\n대상의 침잠이 6 이상이면, 피해량 +40%
   źródło: Skills_personality-08.json :: dataList[id=1080703].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Coin Power +1 for every 5 Tremor Count on self (Max 2)\nIf target has 6+ Sinking, deal +40% damage
   PL: Moc Monet +1 za każde 5 Licznika Wstrząsu (maks. 2)\nJeżeli cel ma 6+ Zatonięcia, zadaje +40% obrażeń
190. [Obrona (ulepszenie 1) — nazwa] 신속 보법
   źródło: Skills_personality-08.json :: dataList[id=1080704].levelList[level=1].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Nimble Steps
   PL: Zwinne Kroki
191. [Obrona (ulepszenie 1) — opis] [WhenUse] 파열 보호 2를 얻음 (턴 당 최대 6)
   źródło: Skills_personality-08.json :: dataList[id=1080704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Rupture Protection (6 times per turn)
   PL: [WhenUse] Zyskuje 2 Ochrony przed Rozdarciami (maks. 6 na turę)
192. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — nazwa] 크랲 파쇄
   źródło: Passives.json :: dataList[id=1080701].name
   limit: do 40 znaków
   EN: Crushin' Crabs
   PL: Miażdżące Kraby
193. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — opis] [Vibration]이 있는 대상에게 공격 적중 시 침잠 횟수 1 증가
   źródło: Passives.json :: dataList[id=1080701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: On Hit against a target that has [Vibration], inflict +1 Sinking Count
   PL: Przy trafieniu celu z [Vibration] nakłada +1 Licznika Zatonięcia
194. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — nazwa] 크랲 드라이버
   źródło: Passives.json :: dataList[id=1080721].name
   limit: do 40 znaków
   EN: Crab Driver
   PL: Atak Kraba
195. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — opis] 최대 체력이 가장 낮은 아군이 공격 적중 시 앞면이 나온 경우, 코인 효과로 진동 횟수를 적에게 부여할 때 침잠 횟수 1 부여
   źródło: Passives.json :: dataList[id=1080721].desc
   limit: do 200 znaków
   EN: When an ally that has the lowest Max HP hits with Heads Coins, they inflict +1 Sinking Count when inflicting Tremor Count on their target with Coin effects.
   PL: Gdy Sojusznik z najniższym Maks. HP trafi awersem i efektem monety nakłada Licznik Wstrząsu wrogowi, nakłada dodatkowo 1 Licznika Zatonięcia

## [000] The Pequod Captain — Ishmael — 피쿼드호 선장
- ID Tożsamości: `10808` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 3 · HP bazowe: 68 · szybkość: 4–5 / 4–6 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Burn, Poise

196. [Karta Tożsamości — tytuł] 피쿼드호\n선장
   źródło: Personalities.json :: dataList[id=10808].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Pequod\nCaptain
   PL: Pequod\nKapitan
197. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10808].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10808].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Karta Tożsamości — opis] 이스마엘의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10808].desc
   limit: do 120 znaków
   EN: Ishmael’s 8th Identity
   PL: Ósma Tożsamość Ishmael
200. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 내 주위에 서라!
   źródło: Skills_personality-08.json :: dataList[id=1080801].levelList[level=1].name ; dataList[id=1080801].levelList[level=2].name ; dataList[id=1080801].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: To Me!
   PL: Do mnie!
201. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 자신을 제외하고 최대 체력이 가장 높은 아군 1명의 가장 왼쪽 슬롯의 [Aggro]가 (가장 높은 공명 수) 만큼 증가 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1080801].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Next turn, the leftmost Skill Slot of 1 other ally with the highest Max HP gains +(highest Reson.) [Aggro] (Once per turn)
   PL: [WhenUse] Lewy skrajny slot 1 Sojusznika z najwyższym Maks. HP (bez tej jednostki) zyskuje w nast. turze [Aggro] równy (najwyższemu Rezonansowi) (1 raz na turę)
202. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed
   PL: [OnSucceedAttackHead] Nakłada 2 Krwawienia
203. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 자신을 제외하고 최대 체력이 가장 높은 아군 1명의 가장 왼쪽 슬롯의 [Aggro]가 (가장 높은 공명 수) 만큼 증가 (턴 당 1회)\n- 가장 높은 완전 공명의 합이 4 이상이면, 효과 발동 시 다음 턴에 보호 1 부여 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1080801].levelList[level=2].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Next turn, the leftmost Skill Slot of 1 other ally with the highest Max HP gains +(highest Reson.) [Aggro] (Once per turn)\n- At 4+ highest A-Reson., apply 1 Protection to the ally next turn when they gain Aggro (Once per turn)
   PL: [WhenUse] Lewy skrajny slot 1 Sojusznika z najwyższym Maks. HP (bez tej jednostki) zyskuje w nast. turze [Aggro] równy (najwyższemu Rezonansowi) (1 raz na turę)\n- Przy 4+ sumie najwyższego Pełnego Rezonansu, przy wywołaniu efektu nakłada 1 [Protection] w następnej turze (1 raz na turę)
204. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL: [OnSucceedAttack] Nakłada 2 Krwawienia
205. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">[StartBattle] 조작 패널에서 자신의 양 옆의 아군에게 방어 레벨 증가 2 부여</style>\n[WhenUse] 다음 턴에 자신을 제외하고 최대 체력이 가장 높은 아군 1명의 가장 왼쪽 슬롯의 [Aggro]가 (가장 높은 공명 수) 만큼 증가 (턴 당 1회)\n- 가장 높은 완전 공명의 합이 4 이상이면, 효과 발동 시 다음 턴에 보호 1 부여 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1080801].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [WhenUse], [Aggro]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: <style="highlight">[StartBattle] Apply 2 Defense Level Up to 2 allies adjacent to this unit on the Dashboard</style>\n[WhenUse] Next turn, the leftmost Skill Slot of 1 other ally with the highest Max HP gains +(highest Reson.) [Aggro] (Once per turn)\n- At 4+ highest A-Reson., apply 1 Protection to the ally next turn when they gain Aggro (Once per turn)
   PL: <style="highlight">[StartBattle] Nakłada 2 Wzrostu Poziomu Obrony na sojuszników przylegających do tej jednostki na panelu</style>\n[WhenUse] Lewy skrajny slot 1 Sojusznika z najwyższym Maks. HP (bez tej jednostki) zyskuje w nast. turze [Aggro] równy (najwyższemu Rezonansowi) (1 raz na turę)\n- Przy 4+ sumie najwyższego Pełnego Rezonansu, przy wywołaniu efektu nakłada 1 [Protection] w następnej turze (1 raz na turę)
206. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 끝까지 추적한다!
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=1].name ; dataList[id=1080802].levelList[level=2].name ; dataList[id=1080802].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Pursue Them to the End!
   PL: Ścigam was do końca!
207. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 가장 높은 공명의 공명 당 10% 확률로 조작 패널에서 자신의 우측에 위치한 아군에게 이번 턴에 [CoverAttack]을 명령함.
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [CoverAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [CoverAttack] = 원호 공격 / Assist Attack
   EN: [WhenUse] Every Reson. of the highest Reson. adds 10% chance that this unit orders the ally on its immediate right(on the Dashboard) to use [CoverAttack] this turn.
   PL: [WhenUse] Każdy Rezonans najwyższego Rezonansu daje 10% szansy, że ta jednostka rozkaże sojusznikowi na swojej prawej stronie (na panelu) użyć [CoverAttack] w tej turze.
208. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL: [OnSucceedAttackHead] Nakłada 1 Krwawienia
209. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Burn
   PL: [OnSucceedAttackHead] Nakłada 1 Podpalenia
210. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 가장 높은 공명의 공명 당 15% 확률로 조작 패널에서 자신의 우측에 위치한 아군에게 이번 턴에 [CoverAttack]을 명령함.\n- 가장 높은 완전 공명의 합이 4 이상이면, 대상에게 피해량 증가 1 부여\n- 오만 완전 공명의 합이 4 이상이면, 오만 위력 증가 1 추가 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=2].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [CoverAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [CoverAttack] = 원호 공격 / Assist Attack
   EN: [WhenUse] Every Reson. of the highest Reson. adds 15% chance that this unit orders the ally on its immediate right(on the Dashboard) to use [CoverAttack] this turn.\n- At 4+ highest A-Reson., apply 1 Damage Up to the ally\n- At 4+ Pride A-Reson., apply 1 additional Pride Power Up
   PL: [WhenUse] Każdy Rezonans najwyższego Rezonansu daje 15% szansy, że ta jednostka rozkaże sojusznikowi na swojej prawej stronie (na panelu) użyć [CoverAttack] w tej turze.\n- Przy 4+ sumie najwyższego Pełnego Rezonansu, nakłada 1 Wzrost Obrażeń celowi\n- Przy 4+ sumie Pełnego Rezonansu Pychy, dodatkowo nakłada 1 Wzrost Mocy Pychy
211. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL: [OnSucceedAttack] Nakłada 1 Krwawienia
212. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1080802].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [StartBattle] 조작 패널에서 자신의 양 옆의 아군에게 공격 레벨 증가 3 부여\n[WhenUse] 가장 높은 공명의 공명 당 20% 확률로 조작 패널에서 자신의 우측에 위치한 아군에게 이번 턴에 [CoverAttack]을 명령함.\n- 가장 높은 완전 공명의 합이 4 이상이면, 대상에게 피해량 증가 2 부여\n- 오만 완전 공명의 합이 4 이상이면, 오만 위력 증가 2 추가 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=4].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [CoverAttack]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [CoverAttack] = 원호 공격 / Assist Attack
   EN: [StartBattle] Apply 3 Offense Level Up to 2 allies adjacent to this unit on the Dashboard\n[WhenUse] Every Reson. of the highest Reson. adds 20% chance that this unit orders the ally on its immediate right(on the Dashboard) to use [CoverAttack] this turn.\n- At 4+ highest A-Reson., apply 2 Damage Up to the ally\n- At 4+ Pride A-Reson., apply 2 additional Pride Power Up
   PL: [StartBattle] Nakłada 3 Wzrostu Poziomu Ataku na sojuszników przylegających do tej jednostki na panelu\n[WhenUse] Każdy Rezonans najwyższego Rezonansu daje 20% szansy, że ta jednostka rozkaże sojusznikowi na swojej prawej stronie (na panelu) użyć [CoverAttack] w tej turze.\n- Przy 4+ sumie najwyższego Pełnego Rezonansu, nakłada 2 Wzrosty Obrażeń celowi\n- Przy 4+ sumie Pełnego Rezonansu Pychy, dodatkowo nakłada 2 Wzrosty Mocy Pychy
214. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 집착의 작살
   źródło: Skills_personality-08.json :: dataList[id=1080803].levelList[level=3].name ; dataList[id=1080803].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Harpoon of Obsession
   PL: Harpun Obsesji
216. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 잃은 체력 1% 당 피해량 +0.2% (최대 20%)\n[EndSkill] 적이 흐트러짐 상태가 되거나 사망하면, 정신력이 가장 낮은 아군 1 + (가장 높은 완전 공명 수/2)명의 정신력 10 회복, 호흡 2 호흡 횟수 4 부여 (최대 2회. 최대 회복 인원 수: 4명)
   źródło: Skills_personality-08.json :: dataList[id=1080803].levelList[level=3].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal more damage based on target's missing HP (+0.2% damage per 1% missing HP, max +20%)\n[EndSkill] If target is Staggered or defeated, (1+(highest A-Reson./2)) allies with the least SP heal 10 SP, gain 2 Poise, and +4 Poise Count. (2 times max. Max # of allies that can be healed: 4)
   PL: Zadaje +0.2% obrażeń za każde 1% brakującego HP celu (maks. 20%)\n[EndSkill] Jeżeli wróg zostaje Ogłuszony albo ginie, 1 + (najwyższy Pełny Rezonans/2) Sojuszników z najniższą Poczytalnością odzyskuje 10 Poczytalności, zyskuje 2 Oddechu i +4 Licznika Oddechu (maks. 2 razy. Maks. liczba leczonych sojuszników: 4)
217. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1080803].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1080803].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Bleed Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika Krwawienia
218. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080803].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1080803].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1080803].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1080803].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 잃은 체력 1% 당 피해량 +0.3% (최대 30%)\n대상의 [Laceration] 5 당 코인 위력 +1 (최대 2)\n[EndSkill] 적이 흐트러짐 상태가 되거나 사망하면, 정신력이 가장 낮은 아군 1 + (가장 높은 완전 공명 수/2)명의 정신력 10 회복, 호흡 2 호흡 횟수 4 부여 (최대 4회. 최대 회복 인원 수: 4명)
   źródło: Skills_personality-08.json :: dataList[id=1080803].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [EndSkill]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal more damage based on target's missing HP (+0.3% damage per 1% missing HP, max +30%)\nCoin Power +1 for every 5 [Laceration] on target (Max 2)\n[EndSkill] If target is Staggered or defeated, (1+(highest A-Reson./2)) allies with the least SP heal 10 SP, gain 2 Poise, and gain +4 Poise Count. (4 times max. Max # of allies that can be healed: 4)
   PL: Zadaje +0.3% obrażeń za każde 1% brakującego HP celu (maks. 30%)\nMoc Monet +1 za każde 5 [Laceration] celu (maks. 2)\n[EndSkill] Jeżeli wróg zostaje Ogłuszony albo ginie, 1 + (najwyższy Pełny Rezonans/2) Sojuszników z najniższą Poczytalnością odzyskuje 10 Poczytalności, zyskuje 2 Oddechu i +4 Licznika Oddechu (maks. 4 razy. Maks. liczba leczonych sojuszników: 4)
221. [Obrona (ulepszenia 1,4) — nazwa] 공포를 날려주지
   źródło: Skills_personality-08.json :: dataList[id=1080804].levelList[level=1].name ; dataList[id=1080804].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Do Not Fear
   PL: Rozpraszam Strach
222. [Obrona (ulepszenie 1) — opis] [WhenUse] 조작 패널에서 자신의 양 옆의 아군 정신력 3 회복 (최대 2회)
   źródło: Skills_personality-08.json :: dataList[id=1080804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 3 SP for 2 allies adjacent to this unit on the Dashboard (2 times max)
   PL: [WhenUse] Odzyskuje 3 Poczytalności dla sojuszników przylegających do tej jednostki na panelu (maks. 2 razy)
223. [Obrona (ulepszenie 4) — opis] [WhenUse] 조작 패널에서 자신의 양 옆의 아군 정신력 5 회복 (최대 2회)
   źródło: Skills_personality-08.json :: dataList[id=1080804].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 5 SP for 2 allies adjacent to this unit on the Dashboard (2 times max)
   PL: [WhenUse] Odzyskuje 5 Poczytalności dla sojuszników przylegających do tej jednostki na panelu (maks. 2 razy)
224. [Pasywka bojowa (od ulepszenia 1) — nazwa] 사냥 시간
   źródło: Passives.json :: dataList[id=1080802].name
   limit: do 40 znaków
   EN: Hour of the Hunt
   PL: Czas Polowania
225. [Pasywka bojowa (od ulepszenia 1) — opis] 대상이 <호수의 존재>면 피해량 +10%
   źródło: Passives.json :: dataList[id=1080802].desc
   limit: do 120 znaków
   EN: If the target is a <Lake Entity>, deal +10% damage
   PL: Jeżeli cel to <Istota z Jeziora>, zadaje +10% obrażeń
226. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — nazwa] 피쿼드호의 선장
   źródło: Passives.json :: dataList[id=1080801].name
   limit: do 40 znaków
   EN: Captain of the Pequod
   PL: Kapitan Pequod
227. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — opis] 자신의 공격 종료 시 대상이 사망했으면,\n- 다음 턴에 [HeatedGasHarpoon] 상태가 됨.\n- 자신을 제외한 정신력이 가장 낮은 아군 1명의 정신력 7 회복.\n- 대상이 피쿼드호 소속이면, 정신력 5 추가 회복.
   źródło: Passives.json :: dataList[id=1080801].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [HeatedGasHarpoon]
   znaczenie tagów: [HeatedGasHarpoon] = 가열된 가스 작살 / Heated Gas Harpoon
   EN: Attack End: If the enemy is defeated after this unit's attack,\n- gain [HeatedGasHarpoon] next turn.\n- 1 other ally with the least SP heals 7 SP.\n- If the ally is from The Pequod, heal an additional 5 SP.
   PL: Na koniec ataku, jeżeli cel ginie:\n- W następnej turze wchodzi w stan [HeatedGasHarpoon].\n- 1 Sojusznik z najniższą Poczytalnością (poza tą jednostką) odzyskuje 7 Poczytalności.\n- Jeżeli cel jest z Pequod, dodatkowo odzyskuje 5 Poczytalności.
228. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Pride) — nazwa] 피쿼드호의 선장
   źródło: Passives.json :: dataList[id=1080811].name
   (powtórzenie elementu 226 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Pride) — opis] 자신의 공격 종료 시 대상이 사망했으면,\n<style="highlight">- 호흡 4, 호흡 횟수 2를 얻고, 다음 턴에 [OverHeatedGasHarpoon] 상태가 됨.</style>\n- 자신을 제외한 정신력이 가장 낮은 아군 <style="highlight">2명의 정신력 7 회복, 호흡 4 부여.</style>\n- 대상이 피쿼드호 소속이면, 정신력 5 추가 회복, <style="highlight">턴 당 1회 다음 턴에 관통 위력 증가 1 부여.</style>
   źródło: Passives.json :: dataList[id=1080811].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OverHeatedGasHarpoon]
   znaczenie tagów: [OverHeatedGasHarpoon] = 과열된 가스 작살 / Overheated Gas Harpoon
   EN: - Attack End: If the enemy is defeated after this unit's attack,\n<style="highlight">- gain 4 Poise, +2 Poise Count. Then, gain [OverHeatedGasHarpoon] next turn.</style>\n<style="highlight">- 2 other allies with the least SP heal 7 SP and gain 4 Poise.</style>\n- If the allies are from The Pequod, heal an additional 5 SP. <style="highlight">Then, once per turn, apply 1 Pierce Power Up next turn.</style>
   PL: Na koniec ataku, jeżeli cel ginie:\n<style="highlight">- Zyskuje 4 Oddechu i +2 Licznika Oddechu, a w następnej turze wchodzi w stan [OverHeatedGasHarpoon].</style>\n- <style="highlight">2 Sojuszników z najniższą Poczytalnością odzyskuje 7 Poczytalności i zyskuje 4 Oddechu.</style> (poza tą jednostką)\n- Jeżeli cel jest z Pequod, dodatkowo odzyskuje 5 Poczytalności, <style="highlight">a w następnej turze 1 raz na turę nakłada 1 Wzrost Mocy Przebicia</style>.
230. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — nazwa] 선장의 명령
   źródło: Passives.json :: dataList[id=1080821].name
   limit: do 40 znaków
   EN: Captain's Orders
   PL: Rozkazy Kapitana
231. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — opis] 정신력이 가장 높은 아군 1명이 자신의 공격 종료 시 대상이 사망했으면, 호흡 2 얻음 (턴 당 2회)
   źródło: Passives.json :: dataList[id=1080821].desc
   limit: do 150 znaków
   EN: 1 ally with the highest SP gains 2 Poise when the target is defeated after that unit's attack (2 times per turn)
   PL: Gdy 1 Sojusznik z najwyższą Poczytalnością zabił cel swoim atakiem, zyskuje 2 Oddechu (2 razy na turę)
232. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Pride) — nazwa] 선장의 명령
   źródło: Passives.json :: dataList[id=1080831].name
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Pride) — opis] 정신력이 가장 높은 아군 1명이 자신의 공격 종료 시 대상이 사망했으면, 호흡 2, <style="highlight">호흡 횟수 2</style> 얻음 (턴 당 2회)
   źródło: Passives.json :: dataList[id=1080831].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Attack End: 1 ally with the highest SP gains 2 Poise and <style="highlight">+2 Poise Count</style> when the target is defeated after that unit's attack (2 times per turn)
   PL: Gdy 1 Sojusznik z najwyższą Poczytalnością zabił cel swoim atakiem, zyskuje 2 Oddechu i <style="highlight">+2 Licznika Oddechu</style> (2 razy na turę)

## [00] Edgar Family Butler — Ishmael — 에드가 가문 버틀러
- ID Tożsamości: `10809` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 4 · HP bazowe: 73 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Poise, Sinking

234. [Karta Tożsamości — tytuł] 에드가 가문\n버틀러
   źródło: Personalities.json :: dataList[id=10809].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Edgar Family\nButler
   PL: Rod Edgara\nKamerdyner
235. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10809].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10809].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Karta Tożsamości — opis] 이스마엘의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10809].desc
   limit: do 120 znaków
   EN: Ishmael’s 9th Identity
   PL: Dziewiąta Tożsamość Ishmael
238. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 빗겨쳐내기
   źródło: Skills_personality-08.json :: dataList[id=1080901].levelList[level=1].name ; dataList[id=1080901].levelList[level=2].name ; dataList[id=1080901].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Sweeping Redirection
   PL: Odbicie Zamiataniem
239. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080901].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080901].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL: [OnSucceedAttack] Zyskuje 2 [Breath]
240. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080901].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] Nakłada 2 [Sinking]
241. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] [Breath] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080901].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2
242. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 속도가 자신보다 느리면 코인 위력 +1\n[WhenUse] [Breath] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080901].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's, Coin Power +1\n[WhenUse] Gain +2 [Breath] Count
   PL: Jeżeli Szybkość celu jest niższa od własnej, Moc Monet +1\n[WhenUse] Zwiększa Licznik [Breath] o 2
243. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080901].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Agility]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Agility] = 신속 / Haste
   EN: [CriticalOnSucceedAttack] Gain 1 [Agility] next turn
   PL: [CriticalOnSucceedAttack] Zyskuje 1 [Agility] w następnej turze
244. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 정리정돈
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=1].name ; dataList[id=1080902].levelList[level=2].name ; dataList[id=1080902].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Housekeeping
   PL: Porządek i Czystość
245. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [Breath] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=1].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1080902].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1080902].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 1 [Agility] next turn
   PL: [OnSucceedAttack] Zyskuje 1 [Agility] w następnej turze
247. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1080902].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown]
   PL: [OnSucceedAttack] Nakłada 2 [DefenseDown]
248. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1080902].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1080902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL: [OnSucceedAttack] Nakłada 4 [Sinking]
249. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] [Breath] 횟수 2 증가\n[WinDuel] [Breath] 2 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +2 [Breath] Count\n[WinDuel] Gain 2 [Breath]
   PL: [WhenUse] Zwiększa Licznik [Breath] o 2\n[WinDuel] Zyskuje 2 [Breath]
250. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 속도가 자신보다 느리면 코인 위력 +1\n[WhenUse] [Breath] 횟수 2 증가\n[WinDuel] [Breath] 2 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, Coin Power +1\n[WhenUse] Gain +2 [Breath] Count\n[WinDuel] Gain 2 [Breath]
   PL: Jeżeli Szybkość celu jest niższa od własnej, Moc Monet +1\n[WhenUse] Zwiększa Licznik [Breath] o 2\n[WinDuel] Zyskuje 2 [Breath]
251. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] 다음 턴에 [Binding] 1 부여</style>
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Binding]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Binding] = 속박 / Bind
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict 1 [Binding] next turn</style>
   PL: <style="highlight">[CriticalOnSucceedAttack] Nakłada 1 [Binding] w następnej turze</style>
252. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [DefenseDown] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080902].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 247 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 동체 속박술
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].name ; dataList[id=1080903].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Restraining Technique
   PL: Technika Spętania
254. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] [Breath] 6 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 6 [Breath]
   PL: [WhenUse] Zyskuje 6 [Breath]
255. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1080903].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Sinking]
256. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1080903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1080903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [Binding]
259. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [SlashTakeDamageUp] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1080903].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttack] Inflict 1 [SlashTakeDamageUp] next turn
   PL: [OnSucceedAttack] Nakłada 1 [SlashTakeDamageUp] w następnej turze
260. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 속도가 자신보다 느리면 코인 위력 +1\n[WhenUse] [Breath] 6 얻음
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's, Coin Power +1\n[WhenUse] Gain 6 [Breath]
   PL: Jeżeli Szybkość celu jest niższa od własnej, Moc Monet +1\n[WhenUse] Zyskuje 6 [Breath]
261. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1080903].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 2 [Binding]
262. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills_personality-08.json :: dataList[id=1080904].levelList[level=1].name ; dataList[id=1080904].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 3 · monety: 1 (+10)
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Obrona (ulepszenie 4) — opis] [OnSucceedEvade] 정신력 5 회복 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1080904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Heal 5 SP (once per turn)
   PL: [OnSucceedEvade] Odzyskuje 5 Poczytalności (1 raz na turę)
264. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Gloom) — nazwa] 묵은 먼지 털기
   źródło: Passives.json :: dataList[id=1080901].name
   limit: do 40 znaków
   EN: Deep Cleaning
   PL: Głębokie Sprzątanie
265. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Gloom) — opis] 속도가 자신보다 느린 대상에게 크리티컬 적중 시 자신이 스킬로 부여하는 부정적인 효과의 위력이 1 추가 부여됨 (턴 당 최대 3회)
   źródło: Passives.json :: dataList[id=1080901].desc
   limit: do 220 znaków
   EN: If this unit Critically Hits against targets with Slower Speed than this unit's, inflict 1 additional Potency for negative effects using its Skills (3 times per turn)
   PL: Przy trafieniu krytycznym celu z niższą Szybkością, efekty negatywne nakładane jej Umiejętnościami zyskują +1 Mocy (maks. 3 razy na turę)
266. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — nazwa] 충실한 보조
   źródło: Passives.json :: dataList[id=1080921].name
   limit: do 40 znaków
   EN: Loyal Supporter
   PL: Wierny Pomocnik
267. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — opis] 속도가 가장 빠른 아군 1명이 [Sinking]이 있는 대상 공격 시 대상의 [Sinking] 1당 피해량 0.5% (최대 10%)
   źródło: Passives.json :: dataList[id=1080921].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When 1 ally with the fastest Speed attacks a target that has [Sinking], deal +0.5% damage for every 1 [Sinking] on target (max 10%)
   PL: Gdy 1 Sojusznik z najwyższą Szybkością atakuje cel z [Sinking], zadaje +0.5% obrażeń za każde 1 [Sinking] celu (maks. 10%)
268. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Gloom) — nazwa] 충실한 보조
   źródło: Passives.json :: dataList[id=1080931].name
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Gloom) — opis] 속도가 가장 빠른 아군 1명이 [Sinking]이 있는 대상 공격 시 대상의 [Sinking] 1당 피해량 1% (최대 20%)
   źródło: Passives.json :: dataList[id=1080931].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When 1 ally with the fastest Speed attacks a target that has [Sinking], deal +1% damage for every 1 [Sinking] on target (max 20%)
   PL: Gdy 1 Sojusznik z najwyższą Szybkością atakuje cel z [Sinking], zadaje +1% obrażeń za każde 1 [Sinking] celu (maks. 20%)

## [000] Zwei Assoc. West Section 3 — Ishmael — 서부 츠바이 협회 3과
- ID Tożsamości: `10810` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 93 · szybkość: 3–5 / 3–5 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor

270. [Karta Tożsamości — tytuł] 서부 츠바이 협회\n3과
   źródło: Personalities.json :: dataList[id=10810].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Zwei Assoc.\nWest Section 3
   PL: Zachodnie Stowarzyszenie Zwei\nSekcja 3
271. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10810].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10810].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Karta Tożsamości — opis] 이스마엘의 열번째 인격
   źródło: Personalities.json :: dataList[id=10810].desc
   limit: do 120 znaków
   EN: Ishmael's 10th Identity
   PL: Dziesiąta Tożsamość Ishmael
274. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 츠바이 기사단 대검술
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=1].name ; dataList[id=1081001].levelList[level=2].name ; dataList[id=1081001].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 50 znaków
   EN: Zwei Knight's Greatsword Form
   PL: Szermierka Wielkim Mieczem Rycerzy Zwei
275. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 2 증가\n[WhenUse] 자신의 [Vibration] 횟수 4 당, [DefenseUp] 1 얻음 (최대 2)
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Vibration], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain +2 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp] for every 4 [Vibration] Count on self (max 2)
   PL: [WhenUse] Zwiększa [Aggro] tego slotu Umiejętności o 2 w następnej turze\n[WhenUse] Zyskuje 1 [DefenseUp] za każde 4 Licznika [Vibration] (maks. 2)
276. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081001].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081001].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]
277. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 1을 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 1 [DefenseUp] next turn
   PL: [OnSucceedAttack] Zyskuje 1 [DefenseUp] w następnej turze
278. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081001].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 1을 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] <style="highlight">3</style> 증가\n[WhenUse] 자신의 [Vibration] 횟수 <style="highlight">3</style> 당, [DefenseUp] 1 얻음 (최대 2)\n<style="highlight">[WhenUse] 자신의 [DefenseUp] 4 이상이면, 기본 위력 +1</style>
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Vibration], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain +<style="highlight">3</style> [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp] for every <style="highlight">3</style> [Vibration] Count on self (max 2)\n<style="highlight">[WhenUse] At 4+ [DefenseUp], Base Power +1</style>
   PL: [WhenUse] Zwiększa [Aggro] tego slotu Umiejętności o <style="highlight">3</style> w następnej turze\n[WhenUse] Zyskuje 1 [DefenseUp] za każde <style="highlight">3</style> Licznika [Vibration] (maks. 2)\n<style="highlight">[WhenUse] Przy 4+ [DefenseUp] Moc Bazowa +1</style>
281. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] <style="highlight">2</style>를 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain <style="highlight">2</style> [DefenseUp] next turn
   PL: [OnSucceedAttack] Zyskuje <style="highlight">2</style> [DefenseUp] w następnej turze
282. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] <style="highlight">2</style>를 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n[WhenUse] 자신의 [Vibration] 횟수 <style="highlight">2</style> 당 [DefenseUp] 1 얻음 (최대 <style="highlight">3</style>)\n[WhenUse] 자신의 [DefenseUp] <style="highlight">4 당</style>, 기본 위력 +1 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=4].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Vibration], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp] for every <style="highlight">2</style> [Vibration] Count on self (max <style="highlight">3</style>)\n[WhenUse] <style="highlight">Base Power +1 for every 4 [DefenseUp] (max 2)</style>
   PL: [WhenUse] Zwiększa [Aggro] tego slotu Umiejętności o 3 w następnej turze\n[WhenUse] Zyskuje 1 [DefenseUp] za każde <style="highlight">2</style> Licznika [Vibration] (maks. <style="highlight">3</style>)\n[WhenUse] <style="highlight">Moc Bazowa +1 za każde 4 [DefenseUp] (maks. 2)</style>
284. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 2를 얻음<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 2 [DefenseUp] next turn<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 2 [DefenseUp] w następnej turze<style="highlight"></style>
285. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 2를 얻음<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081001].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 못 지나갑니다.
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=1].name ; dataList[id=1081002].levelList[level=2].name ; dataList[id=1081002].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Can't Let You Through.
   PL: Nie przepuścimy.
287. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n[WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 3)\n[WinDuel] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Aggro], [Vibration], [DefenseUp], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max 3)\n[WinDuel] Gain +3 [Vibration] Count
   PL: [WhenUse] Zwiększa [Aggro] tego slotu Umiejętności o 3 w następnej turze\n[WhenUse] Zyskuje 1 [DefenseUp] za każde 2 Licznika [Vibration] (maks. 3)\n[WinDuel] Zwiększa własny Licznik [Vibration] o 3
288. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
289. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 3을 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081002].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 3 [DefenseUp] next turn
   PL: [OnSucceedAttack] Zyskuje 3 [DefenseUp] w następnej turze
290. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] (자신의 [Vibration] 횟수/2)만큼 [Vibration] 부여 (최대 2)
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict [Vibration] equal to (([Vibration] Count on self)/2) (max 2)
   PL: [OnSucceedAttack] Nakłada [Vibration] równy wartości (własny Licznik [Vibration]/2) (maks. 2)
291. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [DefenseUp]가 10 이상이면 대상에게 [Reduction] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1081002].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] At 10+ [DefenseUp], inflict 1 [Reduction]
   PL: [OnSucceedAttack] Przy 10+ własnym [DefenseUp] nakłada 1 [Reduction] na cel
292. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 3 증가\n[WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 <style="highlight">4</style>)\n<style="highlight">[WhenUse] 자신의 [DefenseUp]가 5 이상이면, 코인 위력 +1</style>\n[WinDuel] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Vibration], [DefenseUp], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +3 [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max <style="highlight">4</style>)\n<style="highlight">[WhenUse] At 5+ [DefenseUp], Coin Power +1</style>\n[WinDuel] Gain +3 [Vibration] Count
   PL: [WhenUse] Zwiększa [Aggro] tego slotu Umiejętności o 3 w następnej turze\n[WhenUse] Zyskuje 1 [DefenseUp] za każde 2 Licznika [Vibration] (maks. <style="highlight">4</style>)\n<style="highlight">[WhenUse] Przy 5+ własnym [DefenseUp] Moc Monet +1</style>\n[WinDuel] Zwiększa własny Licznik [Vibration] o 3
293. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Vibration]
294. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] (자신의 [Vibration] 횟수/2)만큼 [Vibration] 부여 (최대 <style="highlight">3</style>)
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict [Vibration] equal to (([Vibration] Count on self)/2) (max <style="highlight">3</style>)
   PL: [OnSucceedAttack] Nakłada [Vibration] równy wartości (własny Licznik [Vibration]/2) (maks. <style="highlight">3</style>)
295. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] <style="highlight">5</style> 증가\n[WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 <style="highlight">5</style>)\n[WhenUse] 자신의 [DefenseUp] <style="highlight">4</style> 이상이면, 코인 위력 +1\n[WinDuel] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Aggro], [Vibration], [DefenseUp], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +<style="highlight">5</style> [Aggro] to this Skill Slot next turn\n[WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max <style="highlight">5</style>)\n[WhenUse] At <style="highlight">4</style>+ [DefenseUp], Coin Power +1\n[WinDuel] Gain +3 [Vibration] Count
   PL: [WhenUse] Zwiększa [Aggro] tego slotu Umiejętności o <style="highlight">5</style> w następnej turze\n[WhenUse] Zyskuje 1 [DefenseUp] za każde 2 Licznika [Vibration] (maks. <style="highlight">5</style>)\n[WhenUse] Przy <style="highlight">4</style>+ własnym [DefenseUp] Moc Monet +1\n[WinDuel] Zwiększa własny Licznik [Vibration] o 3
296. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">4</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">4</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">4</style> [Vibration]
297. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] <style="highlight">4</style>를 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain <style="highlight">4</style> [DefenseUp] next turn
   PL: [OnSucceedAttack] Zyskuje <style="highlight">4</style> [DefenseUp] w następnej turze
298. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] (자신의 [Vibration] 횟수/2)만큼 [Vibration] 부여 (최대 <style="highlight">4</style>)
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict [Vibration] equal to (([Vibration] Count on self)/2) (max <style="highlight">4</style>)
   PL: [OnSucceedAttack] Nakłada [Vibration] równy wartości (własny Licznik [Vibration]/2) (maks. <style="highlight">4</style>)
299. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [DefenseUp]가 <style="highlight">8</style> 이상이면 대상에게 [Reduction] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081002].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DefenseUp], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] At <style="highlight">8</style>+ [DefenseUp], inflict 1 [Reduction]
   PL: [OnSucceedAttack] Przy <style="highlight">8</style>+ własnym [DefenseUp] nakłada 1 [Reduction] na cel
300. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 수호
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].name ; dataList[id=1081003].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Ward
   PL: Straż
301. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 3)\n[WhenUse] 자신에게 [DefensiveStance]가 있으면, 피해량 +50%\n[WhenUse] 자신의 [DefenseUp] 4 당 코인 위력 +1 (최대 2)\n[WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] 8 증가\n[WinDuel] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [DefenseUp], [DefensiveStance], [Aggro], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [DefensiveStance] = 방어 태세 / Defensive Stance; [Aggro] = 도발치 / Aggro; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max 3)\n[WhenUse] If this unit is in [DefensiveStance], deal +50% damage\n[WhenUse] Coin Power +1 for every 4 [DefenseUp] on self (max 2)\n[WhenUse] Gain +8 [Aggro] to this Skill Slot next turn\n[WinDuel] Gain +3 [Vibration] Count
   PL: [WhenUse] Zyskuje 1 [DefenseUp] za każde 2 Licznika [Vibration] (maks. 3)\n[WhenUse] Jeżeli jest w [DefensiveStance], zadaje +50% obrażeń\n[WhenUse] Moc Monet +1 za każde 4 [DefenseUp] (maks. 2)\n[WhenUse] Zwiększa [Aggro] tego slotu Umiejętności o 8 w następnej turze\n[WinDuel] Zwiększa własny Licznik [Vibration] o 3
302. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1081003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1081003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수를 전부 소모하여, 소모한 값만큼 [Vibration] 부여. (최대 10)\n- (초과한 [Vibration] x 1.5)%만큼 피해량이 증가 (최대 30%)
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Consume all [Vibration] Count on self, and inflict the value of the Count consumed as [Vibration] on target. (max 10)\n- Deal +(excess [Vibration] x 1.5)% damage (max 30%)
   PL: [OnSucceedAttack] Zużywa cały własny Licznik [Vibration], nakłada [Vibration] równy zużytej wartości. (maks. 10)\n- Zadaje +(1.5 x nadmiarowe [Vibration])% obrażeń (maks. 30%)
305. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1081003].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
306. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [DefensiveStance]면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1081003].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefensiveStance], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefensiveStance] = 방어 태세 / Defensive Stance; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this unit is in [DefensiveStance], trigger [VibrationExplosion]; then, reduce the target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Jeżeli jest w [DefensiveStance], wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
307. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 당 [DefenseUp] 1 얻음 (최대 <style="highlight">5</style>)\n[WhenUse] 자신에게 [DefensiveStance]가 있으면, 피해량 +<style="highlight">70</style>%\n[WhenUse] 자신의 [DefenseUp] 4 당 코인 위력 +1 (최대 <style="highlight">4</style>)\n[WhenUse] 다음 턴에 이 스킬 슬롯의 [Aggro] <style="highlight">10</style> 증가\n[WinDuel] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration], [DefenseUp], [DefensiveStance], [Aggro], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [DefensiveStance] = 방어 태세 / Defensive Stance; [Aggro] = 도발치 / Aggro; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain 1 [DefenseUp] for every 2 [Vibration] Count on self (max <style="highlight">5</style>)\n[WhenUse] If this unit is in [DefensiveStance], deal +<style="highlight">70</style>% damage\n[WhenUse] Coin Power +1 for every 4 [DefenseUp] on self (max <style="highlight">4</style>)\n[WhenUse] Gain +<style="highlight">10</style> [Aggro] to this Skill Slot next turn\n[WinDuel] Gain +3 [Vibration] Count
   PL: [WhenUse] Zyskuje 1 [DefenseUp] za każde 2 Licznika [Vibration] (maks. <style="highlight">5</style>)\n[WhenUse] Jeżeli jest w [DefensiveStance], zadaje +<style="highlight">70</style>% obrażeń\n[WhenUse] Moc Monet +1 za każde 4 [DefenseUp] (maks. <style="highlight">4</style>)\n[WhenUse] Zwiększa [Aggro] tego slotu Umiejętności o <style="highlight">10</style> w następnej turze\n[WinDuel] Zwiększa własny Licznik [Vibration] o 3
308. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수를 전부 소모하여, 소모한 값만큼 [Vibration] 부여. (최대 <style="highlight">20</style>)\n- (초과한 [Vibration] x <style="highlight">5</style>)%만큼 피해량이 증가 (최대 <style="highlight">50</style>%)
   źródło: Skills_personality-08.json :: dataList[id=1081003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Consume all [Vibration] Count on self, and inflict the value of the Count consumed as [Vibration] on target. (max <style="highlight">20</style>)\n- Deal +(excess [Vibration] x <style="highlight">5</style>)% damage (max <style="highlight">50</style>%)
   PL: [OnSucceedAttack] Zużywa cały własny Licznik [Vibration], nakłada [Vibration] równy zużytej wartości. (maks. <style="highlight">20</style>)\n- Zadaje+(<style="highlight">5</style> x nadmiarowe [Vibration])% obrażeń (maks. <style="highlight">50</style>%)
309. [Obrona (ulepszenia 1,4) — nazwa] 당신의 방패
   źródło: Skills_personality-08.json :: dataList[id=1081004].levelList[level=1].name ; dataList[id=1081004].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 3 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Your Shield
   PL: Twoja Tarcza
310. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] [DefensiveStance] 2 얻음. (턴 당 1회)\n[WhenUse] 자신의 [Vibration] 횟수 10 증가 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081004].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [DefensiveStance], [WhenUse], [Vibration]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [DefensiveStance] = 방어 태세 / Defensive Stance; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [CanDuelGuard]\n[StartBattle] Gain 2 [DefensiveStance]. (once per turn)\n[WhenUse] Gain +10 [Vibration] Count (once per turn)
   PL: [CanDuelGuard]\n[StartBattle] Zyskuje 2 [DefensiveStance]. (1 raz na turę)\n[WhenUse] Zwiększa własny Licznik [Vibration] o 10 (1 raz na turę)
311. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-08.json :: dataList[id=1081004].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081004].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
312. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[StartBattle] [DefensiveStance] 2 얻음. (턴 당 1회)\n[WhenUse] 자신의 [Vibration] 횟수 10 증가 (턴 당 1회)\n<style="highlight">[WinDuel] [VibrationExplosion]</style>
   źródło: Skills_personality-08.json :: dataList[id=1081004].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [StartBattle], [DefensiveStance], [WhenUse], [Vibration], [WinDuel], [VibrationExplosion]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [DefensiveStance] = 방어 태세 / Defensive Stance; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [CanDuelGuard]\n[StartBattle] Gain 2 [DefensiveStance]. (once per turn)\n[WhenUse] Gain +10 [Vibration] Count (once per turn)\n<style="highlight">[WinDuel] Trigger [VibrationExplosion]</style>
   PL: [CanDuelGuard]\n[StartBattle] Zyskuje 2 [DefensiveStance]. (1 raz na turę)\n[WhenUse] Zwiększa własny Licznik [Vibration] o 10 (1 raz na turę)\n<style="highlight">[WinDuel] Wywołuje [VibrationExplosion]</style>
313. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — nazwa] 충격상쇄 그레이트소드
   źródło: Passives.json :: dataList[id=1081001].name
   limit: do 40 znaków
   EN: Shock-nullifying Greatsword
   PL: Wielki Miecz Niwelujący Wstrząsy
314. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — opis] 전투 시작 시, 자신의 [Vibration] 횟수만큼 [DefenseUp]를 얻음 (최대 5)
   źródło: Passives.json :: dataList[id=1081001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration], [DefenseUp]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: At Combat Start, gain [DefenseUp] equal to [Vibration] Count on self (max 5)
   PL: Na początku walki zyskuje [DefenseUp] równy własnemu Licznikowi [Vibration] (maks. 5)
315. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Pride) — nazwa] 충격상쇄 그레이트소드
   źródło: Passives.json :: dataList[id=1081011].name
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Pride) — opis] 전투 시작 시, 자신의 [Vibration] 횟수만큼 [DefenseUp]를 얻음 (최대 5)\n-[DefensiveStance]가 있으면 위 효과로 얻는 [DefenseUp]가 2배가 됨.
   źródło: Passives.json :: dataList[id=1081011].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [DefenseUp], [DefensiveStance]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [DefensiveStance] = 방어 태세 / Defensive Stance
   EN: At Combat Start, gain [DefenseUp] equal to [Vibration] Count on self (max 5)\n- If this unit is in [DefensiveStance], double the amount of [DefenseUp] gained from the above effect.
   PL: Na początku walki zyskuje [DefenseUp] równy własnemu Licznikowi [Vibration] (maks. 5)\n- Jeżeli jest w [DefensiveStance], [DefenseUp] zyskany powyższym efektem jest podwojony (x2).
317. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — nazwa] 긴급수호
   źródło: Passives.json :: dataList[id=1081021].name
   limit: do 40 znaków
   EN: Emergency Protection
   PL: Awaryjna Ochrona
318. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — opis] 전투 시작 시 체력이 감소하여 이전 턴 시작과 체력 비율이 가장 차이가 많이 나는 인격에게 [DefenseUp] 2 부여
   źródło: Passives.json :: dataList[id=1081021].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: At Combat Start, compare each Identity's current HP to their HP at the start of the previous turn. Then, apply 2 [DefenseUp] to the Identity that has the greatest disparity of HP values between turns.
   PL: Na początku walki nakłada 2 [DefenseUp] na Tożsamość, której HP najbardziej odbiega od stanu z początku poprzedniej tury

## [000] Kurokumo Clan Captain — Ishmael — 흑운회 부조장
- ID Tożsamości: `10811` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 93 · szybkość: 3–4 / 3–5 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed

319. [Karta Tożsamości — tytuł] 흑운회\n부조장
   źródło: Personalities.json :: dataList[id=10811].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Kurokumo Clan\nCaptain
   PL: Klan Kurokumo\nKapitan
320. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10811].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10811].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [Karta Tożsamości — opis] 이스마엘의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10811].desc
   limit: do 120 znaków
   EN: Ishmael's 11th Identity
   PL: Jedenasta Tożsamość Ishmael
323. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 뒷처리
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=1].name ; dataList[id=1081101].levelList[level=2].name ; dataList[id=1081101].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Clean Up
   PL: Posprzątanie
324. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]
325. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]
326. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AttackDown] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown]
   PL: [OnSucceedAttack] Nakłada 1 [AttackDown]
327. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: <style="highlight">If target has 6+ [Laceration], Coin Power +1</style>
   PL: <style="highlight">Jeżeli cel ma 6+ [Laceration], Moc Monet +1</style>
328. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]<style="highlight"></style>
329. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]<style="highlight"></style>
330. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AttackDown] 1 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1081101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [AttackDown]<style="highlight"></style>
331. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)\n대상이 보유한 부정적인 효과 1개당 피해량 +10% (최대 30%)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081101].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)\nDeal +10% damage for every type of negative effect on target (max 30%)</style>
   PL: <style="highlight">Moc Monet +1 za każde 6 [Laceration] celu (maks. 2)\nZadaje +10% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 30%)</style>
332. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 날카로운 칼날
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=1].name ; dataList[id=1081102].levelList[level=2].name ; dataList[id=1081102].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Sharpened Blade
   PL: Naostrzone Ostrze
333. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [StartBattle] 자신을 제외하고 속도가 가장 빠른 아군 흑운회 소속 인격 2명에게 [AttackDmgUp] 1 부여 (턴 당 1회)\n- 자신 포함 흑운회 소속이 6명 이상이면 대신 5명에게 [AttackDmgUp] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [AttackDmgUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [StartBattle] On 2 other allied Kurokumo Clan Identities with the fastest Speed: apply 1 [AttackDmgUp] (once per turn)\n- If there are 6+ Kurokumo Clan allies, including this unit, apply 2 [AttackDmgUp] to 5 allies instead
   PL: [StartBattle] Nakłada 1 [AttackDmgUp] na 2 Sojuszników Klanu Kurokumo z najwyższą Szybkością (poza tą jednostką) (1 raz na turę)\n- Jeżeli Klanu Kurokumo (łącznie z tą jednostką) jest 6 lub więcej, zamiast tego nakłada 2 [AttackDmgUp] na 5 Sojuszników
334. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 2
336. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>\n[StartBattle] 자신을 제외하고 속도가 가장 빠른 아군 흑운회 소속 인격 2명에게 [AttackDmgUp] <style="highlight">2</style> 부여 (턴 당 1회)\n- 자신 포함 흑운회 소속이 6명 이상이면 대신 5명에게 [AttackDmgUp] <style="highlight">3</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=2].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [StartBattle], [AttackDmgUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: <style="highlight">If target has 6+ [Laceration], Coin Power +1</style>\n[StartBattle] On 2 other allied Kurokumo Clan Identities with the fastest Speed: apply <style="highlight">2</style> [AttackDmgUp] (once per turn)\n- If there are 6+ Kurokumo Clan units, including this unit, apply <style="highlight">3</style> [AttackDmgUp] to 5 allies instead
   PL: <style="highlight">Jeżeli cel ma 6+ [Laceration], Moc Monet +1</style>\n[StartBattle] Nakłada <style="highlight">2</style> [AttackDmgUp] na 2 Sojuszników Klanu Kurokumo z najwyższą Szybkością (poza tą jednostką) (1 raz na turę)\n- Jeżeli Klanu Kurokumo (łącznie z tą jednostką) jest 6 lub więcej, zamiast tego nakłada <style="highlight">3</style> [AttackDmgUp] na 5 Sojuszników
337. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 329 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [SlashTakeDamageUp] 1 부여 (턴 당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: <style="highlight">[OnSucceedAttackHead] Inflict 1 [SlashTakeDamageUp] (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttackHead] Nakłada 1 [SlashTakeDamageUp] (1 raz na turę)</style>
339. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 2<style="highlight"></style>
340. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [SlashResultUp] 1 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SlashResultUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResultUp] = 참격 위력 증가 / Slash Power Up
   EN: <style="highlight">[OnSucceedAttack] Gain 1 [SlashResultUp] next turn (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttack] Zyskuje 1 [SlashResultUp] w następnej turze (1 raz na turę)</style>
341. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)\n대상이 보유한 부정적인 효과 1개당 피해량 +10% (최대 50%)</style>\n[StartBattle] 자신을 제외하고 속도가 가장 빠른 아군 흑운회 소속 인격 2명에게 [AttackDmgUp] 2 부여 (턴 당 1회)\n- 자신 포함 흑운회 소속이 6명 이상이면 대신 5명에게 [AttackDmgUp] 4 부여
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [StartBattle], [AttackDmgUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)\nDeal +10% damage for every type of negative effect on target (max 50%)</style>\n[StartBattle] On 2 other allied Kurokumo Clan Identities with the fastest Speed: apply 2 [AttackDmgUp] (once per turn)\n- If there are 6+ Kurokumo Clan units, including this unit, apply 4 [AttackDmgUp] to 5 allies instead
   PL: <style="highlight">Moc Monet +1 za każde 6 [Laceration] celu (maks. 2)\nZadaje +10% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 50%)</style>\n[StartBattle] Nakłada 2 [AttackDmgUp] na 2 Sojuszników Klanu Kurokumo z najwyższą Szybkością (poza tą jednostką) (1 raz na turę)\n- Jeżeli Klanu Kurokumo (łącznie z tą jednostką) jest 6 lub więcej, zamiast tego nakłada 4 [AttackDmgUp] na 5 Sojuszników
342. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [SlashTakeDamageUp] 1 부여 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttackHead] Inflict 1 [SlashTakeDamageUp] (once per turn)<style="highlight"></style>
   PL: [OnSucceedAttackHead] Nakłada 1 [SlashTakeDamageUp] (1 raz na turę)<style="highlight"></style>
343. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 3 — opis] <style="highlight">- 자신 포함 흑운회 소속이 6명 이상이면, 대신 [Vulnerable] 2 부여</style>
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: <style="highlight">- If there are 6+ Kurokumo Clan units, including this unit, inflict 2 [Vulnerable] instead</style>
   PL: <style="highlight">- Jeżeli Klanu Kurokumo (łącznie z tą jednostką) jest 6 lub więcej, zamiast tego nakłada 2 [Vulnerable]</style>
344. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [SlashResultUp] 1 얻음 (턴 당 <style="highlight">2</style>회)
   źródło: Skills_personality-08.json :: dataList[id=1081102].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SlashResultUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResultUp] = 참격 위력 증가 / Slash Power Up
   EN: [OnSucceedAttack] Gain 1 [SlashResultUp] next turn (<style="highlight">2 times</style> per turn)
   PL: [OnSucceedAttack] Zyskuje 1 [SlashResultUp] w następnej turze (<style="highlight">2 razy</style> na turę)
345. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 먹칠
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=3].name ; dataList[id=1081103].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Ink Over
   PL: Zamazywanie
346. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 6+ [Laceration], Coin Power +1
   PL: Jeżeli cel ma 6+ [Laceration], Moc Monet +1
347. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] Nakłada 3 [Laceration]
349. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Laceration] 3회 발동. 대상의 출혈 횟수 3 감소
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on target 3 times; then, reduce their [Laceration] Count by 3
   PL: [OnSucceedAttack] Uruchamia [Laceration] celu 3 razy. Zmniejsza Licznik Krwawienia celu o 3
350. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)\n[EnemyKill] 다음 턴에 [SlashResultUp] 2 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [EnemyKill], [SlashResultUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [EnemyKill] = [적 처치 시] / [On Kill]; [SlashResultUp] = 참격 위력 증가 / Slash Power Up
   EN: <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)\n[EnemyKill] Gain 2 [SlashResultUp] next turn (once per turn)</style>
   PL: <style="highlight">Moc Monet +1 za każde 6 [Laceration] celu (maks. 2)\n[EnemyKill] Zyskuje 2 [SlashResultUp] w następnej turze (1 raz na turę)</style>
351. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Laceration]<style="highlight"></style>
353. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">대상이 보유한 부정적인 효과 1개당 피해량 +10% (최대 100%)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">Deal +10% damage for every type of negative effect on target (max 100%)</style>
   PL: <style="highlight">Zadaje +10% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 100%)</style>
354. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 3회 발동. 대상의 출혈 횟수 3 감소<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081103].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on target 3 times; then, reduce their [Laceration] Count by 3<style="highlight"></style>
   PL: [OnSucceedAttack] Uruchamia [Laceration] celu 3 razy. Zmniejsza Licznik Krwawienia celu o 3<style="highlight"></style>
355. [Obrona (ulepszenia 1,4) — nazwa] 흩어지는 검격
   źródło: Skills_personality-08.json :: dataList[id=1081104].levelList[level=1].name ; dataList[id=1081104].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Scattering Slash
   PL: Rozproszony Cios
356. [Obrona (ulepszenie 1) — opis] [StartBattle] [Protection] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Protection]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection
   EN: [StartBattle] Gain 1 [Protection] (once per turn)
   PL: [StartBattle] Zyskuje 1 [Protection] (1 raz na turę)
357. [Obrona (ulepszenie 4) — opis] [StartBattle] [Protection] 1 얻음 (턴 당 1회)\n<style="highlight">[StartBattle] 자신을 포함하여 속도가 가장 빠른 아군 흑운회 소속 인격 (2 + 최대 공명 수)명에게 [Endurance] 2 부여 (턴 당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081104].levelList[level=4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [Protection], [Endurance]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: [StartBattle] Gain 1 [Protection] (once per turn)\n<style="highlight">[StartBattle] On (2 + highest Reson.) allied Kurokumo Clan Identities, including this unit, with the fastest Speed: apply 2 [Endurance] (once per turn)</style>
   PL: [StartBattle] Zyskuje 1 [Protection] (1 raz na turę)\n<style="highlight">[StartBattle] Nakłada 2 [Endurance] na (2 + najwyższy Rezonans) Sojuszników Klanu Kurokumo z najwyższą Szybkością (łącznie z tą jednostką) (1 raz na turę)</style>
358. [Pasywka bojowa (od ulepszenia 1) — nazwa] 임전
   źródło: Passives.json :: dataList[id=1081102].name
   limit: do 40 znaków
   EN: Battle Ready
   PL: Gotowość Bojowa
359. [Pasywka bojowa (od ulepszenia 1) — opis] 흑운회 소속 아군이 사망하면, 이번 전투 동안 [SlashResultUp] 1 얻음\n\n흑운회 소속 아군이 3명 이상 사망하면 이번 전투 동안 [EngageToBattle]을 얻음
   źródło: Passives.json :: dataList[id=1081102].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [SlashResultUp], [EngageToBattle]
   znaczenie tagów: [SlashResultUp] = 참격 위력 증가 / Slash Power Up; [EngageToBattle] = 임전 / Battle Ready
   EN: When a Kurokumo Clan ally dies, gain 1 [SlashResultUp] for this Encounter\n\nWhen 3 or more Kurokumo Clan allies are defeated, gain [EngageToBattle] for this Encounter
   PL: Gdy sojusznik Klanu Kurokumo ginie, zyskuje 1 [SlashResultUp] w tym spotkaniu\n\nGdy zginie 3 lub więcej sojuszników Klanu Kurokumo, zyskuje [EngageToBattle] w tym spotkaniu
360. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — nazwa] 몰려드는 검은 구름
   źródło: Passives.json :: dataList[id=1081101].name
   limit: do 40 znaków
   EN: Gathering Dark Clouds
   PL: Nadciągające Czarne Chmury
361. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — opis] 전투 시작시 자신을 포함해 전투에 참여한 아군 흑운회 소속 인격이 2명 이상이면, [BlackCloudBlade] 1 얻음\n\n전투 시작시 조작 패널에서 자신의 양 옆의 흑운회 소속 인격에게 [BlackCloud] 1 부여
   źródło: Passives.json :: dataList[id=1081101].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [BlackCloudBlade], [BlackCloud]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade; [BlackCloud] = 검은 구름 / Dark Cloud
   EN: Combat Start: if there are 2+ allied Kurokumo Clan Identities in this Encounter, including this unit, gain 1 [BlackCloudBlade]\n\nCombat Start: apply 1 [BlackCloud] to Kurokumo Clan Identities adjacent to this unit on the Dashboard
   PL: Na początku walki, jeżeli 2 lub więcej Tożsamości Klanu Kurokumo (łącznie z tą jednostką) uczestniczy w walce, zyskuje 1 [BlackCloudBlade]\n\nNa początku walki nakłada 1 [BlackCloud] na Tożsamości Klanu Kurokumo przylegające do tej jednostki na panelu
362. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — podsumowanie] [BlackCloudBlade] 얻음, 아군 흑운회 소속 인격에게 [BlackCloud] 부여
   źródło: Passives.json :: dataList[id=1081101].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BlackCloudBlade], [BlackCloud]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade; [BlackCloud] = 검은 구름 / Dark Cloud
   EN: Gain [BlackCloudBlade]; apply [BlackCloud] to allied Kurokumo Clan Identities
   PL: Zyskuje [BlackCloudBlade], nakłada [BlackCloud] na Tożsamości sojuszników Klanu Kurokumo
363. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — nazwa] 몰려드는 검은 구름
   źródło: Passives.json :: dataList[id=1081111].name
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — opis] 전투 시작시 자신을 포함해 전투에 참여한 아군 흑운회 소속 인격이 2명 이상이면, [BlackCloudBlade] 1 얻음\n\n전투 시작시 조작 패널에서 자신의 양 옆의 흑운회 소속 인격에게 [BlackCloud] 1 부여\n<style="highlight">- 색욕 공명이 4 이상이면, 자신을 제외한 모든 흑운회 소속 아군에게 [BlackCloud] 1 부여</style>
   źródło: Passives.json :: dataList[id=1081111].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BlackCloudBlade], [BlackCloud]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade; [BlackCloud] = 검은 구름 / Dark Cloud
   EN: Combat Start: if there are 2+ allied Kurokumo Clan Identities in this Encounter, including this unit, gain 1 [BlackCloudBlade]\n\nCombat Start: apply 1 [BlackCloud] to Kurokumo Clan Identities adjacent to this unit on the Dashboard\n<style="highlight">- At 4+ Lust Reson., apply 1 [BlackCloud] to all other Kurokumo Clan allies</style>
   PL: Na początku walki, jeżeli 2 lub więcej Tożsamości Klanu Kurokumo (łącznie z tą jednostką) uczestniczy w walce, zyskuje 1 [BlackCloudBlade]\n\nNa początku walki nakłada 1 [BlackCloud] na Tożsamości Klanu Kurokumo przylegające do tej jednostki na panelu\n<style="highlight">- Przy 4+ Rezonansie Żądzy, nakłada 1 [BlackCloud] na wszystkich pozostałych sojuszników Klanu Kurokumo</style>
365. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — podsumowanie] [BlackCloudBlade] 얻음, 아군 흑운회 소속 인격에게 [BlackCloud] 부여
   źródło: Passives.json :: dataList[id=1081111].summary
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — nazwa] 구름 공방 칼날
   źródło: Passives.json :: dataList[id=1081121].name
   limit: do 40 znaków
   EN: Cloud Workshop Blade
   PL: Ostrze Warsztatu Chmur
367. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — opis] 속도가 가장 빠른 아군 1명이 적에게 스킬 효과, 코인 효과로 부여하는 [Laceration] 위력 또는 횟수 부여 값 +1
   źródło: Passives.json :: dataList[id=1081121].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: 1 ally with the fastest Speed inflicts +1 more [Laceration] Potency or Count with Skill and Coin effects against enemies
   PL: 1 Sojusznik z najwyższą Szybkością nakłada o 1 więcej Mocy lub Licznika [Laceration] efektami Umiejętności i monet wrogom

## [000] Family Hierarch Candidate — Ishmael — 가주 후보
- ID Tożsamości: `10812` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 70 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Rupture, Poise

368. [Karta Tożsamości — tytuł] 가주 후보
   źródło: Personalities.json :: dataList[id=10812].title
   limit: do 40 znaków
   EN: Family Hierarch Candidate
   PL: Kandydat na Głowę Rodu
369. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10812].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10812].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Karta Tożsamości — opis] 이스마엘의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10812].desc
   limit: do 120 znaków
   EN: Ishmael's 12th Identity
   PL: Dwunasta Tożsamość Ishmael
372. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 적격
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=1].name ; dataList[id=1081201].levelList[level=2].name ; dataList[id=1081201].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Crimson Strike
   PL: Szkarłatny Cios
373. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 합 위력 +1\n[WinDuel] [Breath] 1 얻음, 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WinDuel], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WhenUse] If target has 5+ types of negative effects, Clash Power +1\n[WinDuel] Gain 1 [Breath] and +1 [Breath] Count
   PL: [WhenUse] Przy 5+ rodzajach negatywnych efektów celu Moc Starcia +1\n[WinDuel] Zyskuje 1 [Breath] i zwiększa własny Licznik [Breath] o 1
374. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]
375. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] Nakłada 2 [Burst]
376. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [AttackUp] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1081201].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [AttackUp]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CriticalOnSucceedAttack] Gain 1 [AttackUp] next turn (once per turn)
   PL: [CriticalOnSucceedAttack] Zyskuje 1 [AttackUp] w następnej turze (1 raz na turę)
377. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 합 위력 +1\n<style="highlight">[WhenUse] 대상의 [Burst] 3 이상이면, 코인 위력 +1</style>\n[WinDuel] [Breath] 2 얻음, 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WhenUse] If target has 5+ types of negative effects, Clash Power +1\n<style="highlight">[WhenUse] If target has 3+ [Burst], Coin Power +1</style>\n[WinDuel] Gain 2 [Breath] and +1 [Breath] Count
   PL: [WhenUse] Przy 5+ rodzajach negatywnych efektów celu Moc Starcia +1\n<style="highlight">[WhenUse] Jeżeli cel ma 3+ [Burst], Moc Monet +1</style>\n[WinDuel] Zyskuje 2 [Breath] i zwiększa własny Licznik [Breath] o 1
378. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 합 위력 +1\n[WhenUse] 대상의 [Burst] <style="highlight">3당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WinDuel] [Breath] <style="highlight">3</style> 얻음, 자신의 [Breath] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WhenUse] If target has 5+ types of negative effects, Clash Power +1\n[WhenUse] <style="highlight">Coin Power +1 for every 3 [Burst] on target (max 2)</style>\n[WinDuel] Gain <style="highlight">3</style> [Breath] and +<style="highlight">2</style> [Breath] Count
   PL: [WhenUse] Przy 5+ rodzajach negatywnych efektów celu Moc Starcia +1\n[WhenUse] <style="highlight">Moc Monet +1 za każde 3 [Burst] celu (maks. 2)</style>\n[WinDuel] Zyskuje <style="highlight">3</style> [Breath] i zwiększa własny Licznik [Breath] o <style="highlight">2</style>
379. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [AttackUp] 1 얻음 (턴 당 <style="highlight">2</style>회)
   źródło: Skills_personality-08.json :: dataList[id=1081201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [AttackUp]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CriticalOnSucceedAttack] Gain 1 [AttackUp] next turn (<style="highlight">2 times</style> per turn)
   PL: [CriticalOnSucceedAttack] Zyskuje 1 [AttackUp] w następnej turze (<style="highlight">2 razy</style> na turę)
380. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 적봉
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].name ; dataList[id=1081202].levelList[level=2].name ; dataList[id=1081202].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 2 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Crimson Phoenix
   PL: Szkarłatny Feniks
381. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 코인 위력 +1
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].desc ; dataList[id=1081202].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If target has 5+ types of negative effects, Coin Power +1
   PL: [WhenUse] Przy 5+ rodzajach negatywnych efektów celu Moc Monet +1
382. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 374 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 374 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Burst]만큼 [Breath] 얻음 (최대 5)
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1081202].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1081202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain [Breath] equal to [Burst] on target (max 5)
   PL: [OnSucceedAttack] Zyskuje [Breath] równy wartości [Burst] celu (maks. 5)
385. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 대상의 [Burst] 횟수만큼 [Breath] 횟수 증가 (최대 3)
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1081202].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1081202].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain [Breath] Count equal to [Burst] Count on target (max 3)
   PL: [OnSucceedAttackHead] Zwiększa Licznik [Breath] o wartość Licznika [Burst] celu (maks. 3)
386. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 4, efekt 1 — opis] 크리티컬 피해량 +(20 + 자신의 [Breath] + 대상의 [Burst])% (최대 50%)
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=1081202].levelList[level=2].coinlist[#3].coindescs[#0].desc ; dataList[id=1081202].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath], [Burst]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: Deal +(20 + [Breath] on self + [Burst] on target)% damage on Critical Hit (max 50%)
   PL: Zadaje +(20 + własne [Breath] + [Burst] celu)% obrażeń przy trafieniu krytycznym (maks. 50%)
387. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [DefenseDown] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [DefenseDown]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [CriticalOnSucceedAttack] Inflict 1 [DefenseDown] next turn
   PL: [CriticalOnSucceedAttack] Nakłada 1 [DefenseDown] w następnej turze
388. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [DefenseDown] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 4, efekt 2 — opis] [CriticalEnemyTargetKill] 다음 턴에 [AttackUp] 3 얻음 (턴 당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=2].coinlist[#3].coindescs[#1].desc ; dataList[id=1081202].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalEnemyTargetKill], [AttackUp]
   znaczenie tagów: [CriticalEnemyTargetKill] = [크리티컬 적 처치 시] / [On Crit Kill Against Enemy]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CriticalEnemyTargetKill] Gain 3 [AttackUp] next turn (once per turn)
   PL: [CriticalEnemyTargetKill] Zyskuje 3 [AttackUp] w następnej turze (1 raz na turę)
390. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 부정적인 효과가 5개 이상이면, 코인 위력 +1\n<style="highlight">[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 5+ types of negative effects, Coin Power +1\n<style="highlight">[WhenUse] If target has 4+ [Burst], Coin Power +1</style>
   PL: [WhenUse] Przy 5+ rodzajach negatywnych efektów celu Moc Monet +1\n<style="highlight">[WhenUse] Jeżeli cel ma 4+ [Burst], Moc Monet +1</style>
391. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [DefenseDown] <style="highlight">2</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [DefenseDown]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [CriticalOnSucceedAttack] Inflict <style="highlight">2</style> [DefenseDown] next turn
   PL: [CriticalOnSucceedAttack] Nakłada <style="highlight">2</style> [DefenseDown] w następnej turze
392. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [DefenseDown] <style="highlight">2</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 적춘
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].name ; dataList[id=1081203].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 8 · monety: 1 (+14)
   limit: do 40 znaków
   EN: Crimson Spring
   PL: Szkarłatna Wiosna
394. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [BeforeAttack] 메인 타겟의 부정적인 효과가 6개 이상이면 공격 가중치 +1\n[WhenUse] 메인 타겟의 부정적인 효과 3개당, 코인 위력+2 (최대 4)\n[WhenUse] 메인 타겟의 ([Burst] + [Burst] 횟수)의 합 7당, 코인 위력 +1 (최대 3)\n[WinDuel] [Breath] 4 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [WhenUse], [Burst], [WinDuel], [Breath]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [BeforeAttack] If main target has 6+ types of negative effects, Atk Weight +1\n[WhenUse] Coin Power +2 for every 3 types of negative effect on the main target (max 4)\n[WhenUse] Coin Power +1 for every 7 ([Burst] + [Burst] Count) on the main target (max 3)\n[WinDuel] Gain 4 [Breath]
   PL: [BeforeAttack] Przy 6+ rodzajach negatywnych efektów głównego celu Waga ataku +1\n[WhenUse] Moc Monet +2 za każde 3 rodzaje negatywnych efektów głównego celu (maks. 4)\n[WhenUse] Moc Monet +1 za każde 7 (suma [Burst] i Licznika [Burst] głównego celu) (maks. 3)\n[WinDuel] Zyskuje 4 [Breath]
395. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] 피해량 +(20 + 자신의 [Breath] + 메인 타겟의 [Burst])% (최대 40%)
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath], [Burst]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: Deal +(20 + [Breath] on self + [Burst] on the main target)% damage (max 40%)
   PL: Zadaje +(20 + własne [Breath] + [Burst] głównego celu)% obrażeń (maks. 40%)
397. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] 크리티컬 피해량 +(45 + 자신의 [Breath] + 메인 타겟의 [Burst])% (최대 65%)
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath], [Burst]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: Deal +(45 + [Breath] on self + [Burst] on the main target)% damage on Critical Hit (max 65%)
   PL: Zadaje +(45 + własne [Breath] + [Burst] głównego celu)% obrażeń przy trafieniu krytycznym (maks. 65%)
398. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 4 — opis] 자신의 [StartXichun]당 크리티컬 피해량 +5% (최대 30%)
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartXichun]
   znaczenie tagów: [StartXichun] = 시[始] / Launcher [始]
   EN: +5% Damage on Critical Hit for every [StartXichun] on self (max 30%)
   PL: Zadaje +5% obrażeń przy trafieniu krytycznym za każdy 1 [StartXichun] (maks. 30%)
399. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]
   PL: [OnSucceedAttack] Nakłada 5 [Burst]
400. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 6 — opis] [CriticalOnSucceedAttack] [Breath] 2 얻음. [Breath] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain 2 [Breath] and +1 [Breath] Count
   PL: [CriticalOnSucceedAttack] Zyskuje 2 [Breath] i zwiększa Licznik [Breath] o 1
401. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 7 — opis] [CriticalEnemyTargetKill] [Breath] 횟수 2 증가 (턴 당 3회)
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=3].coinlist[#0].coindescs[#6].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalEnemyTargetKill], [Breath]
   znaczenie tagów: [CriticalEnemyTargetKill] = [크리티컬 적 처치 시] / [On Crit Kill Against Enemy]; [Breath] = 호흡 / Poise
   EN: [CriticalEnemyTargetKill] Gain +2 [Breath] Count (3 times per turn)
   PL: [CriticalEnemyTargetKill] Zwiększa własny Licznik [Breath] o 2 (3 razy na turę)
402. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [BeforeAttack] 메인 타겟의 부정적인 효과가 5개 이상이면, 공격 가중치 +1\n<style="highlight">[BeforeAttack] 자신의 [StartXichun]가 3 이상이면, 공격 가중치 +1</style>\n[WhenUse] 메인 타겟의 부정적인 효과 3개당, 코인 위력+2 (최대 <style="highlight">6</style>)\n[WhenUse] 메인 타겟의 ([Burst] + [Burst] 횟수)의 합 7당, 코인 위력 +1 (최대 <style="highlight">5</style>)\n[WinDuel] [Breath] 4 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [StartXichun], [WhenUse], [Burst], [WinDuel], [Breath]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [StartXichun] = 시[始] / Launcher [始]; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [BeforeAttack] If main target has 5+ types of negative effects, Atk Weight +1\n<style="highlight">[BeforeAttack] At 3+ [StartXichun], Atk Weight +1</style>\n[WhenUse] Coin Power +2 for every 3 types of negative effect on the main target (max <style="highlight">6</style>)\n[WhenUse] Coin Power +1 for every 7 ([Burst] + [Burst] Count) on the main target (max <style="highlight">5</style>)\n[WinDuel] Gain 4 [Breath]
   PL: [BeforeAttack] Przy 5+ rodzajach negatywnych efektów głównego celu Waga ataku +1\n<style="highlight">[BeforeAttack] Przy 3+ własnym [StartXichun] Waga ataku +1</style>\n[WhenUse] Moc Monet +2 za każde 3 rodzaje negatywnych efektów głównego celu (maks. <style="highlight">6</style>)\n[WhenUse] Moc Monet +1 za każde 7 (suma [Burst] i Licznika [Burst] głównego celu) (maks. <style="highlight">5</style>)\n[WinDuel] Zyskuje 4 [Breath]
403. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] 피해량 +(<style="highlight">50</style> + 자신의 [Breath] + 메인 타겟의 [Burst])% (최대 <style="highlight">75</style>%)
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Breath], [Burst]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: Deal +(<style="highlight">50</style> + [Breath] on self + [Burst] on the main target)% damage (max <style="highlight">75</style>%)
   PL: Zadaje +(<style="highlight">50</style> + własne [Breath] + [Burst] głównego celu)% obrażeń (maks. <style="highlight">75</style>%)
404. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] 크리티컬 피해량 +(<style="highlight">80</style> + 자신의 [Breath] + 메인 타겟의 [Burst])% (최대 <style="highlight">105</style>%)
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Breath], [Burst]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: Deal +(<style="highlight">80</style> + [Breath] on self + [Burst] on the main target)% damage on Critical Hit (max <style="highlight">105</style>%)
   PL: Zadaje +(<style="highlight">80</style> + własne [Breath] + [Burst] głównego celu)% obrażeń przy trafieniu krytycznym (maks. <style="highlight">105</style>%)
405. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] 자신의 [StartXichun]당 크리티컬 피해량 +5% (최대 30%)<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [StartXichun]
   znaczenie tagów: [StartXichun] = 시[始] / Launcher [始]
   EN: +5% Damage on Critical Hit for every [StartXichun] on self (max 30%)<style="highlight"></style>
   PL: Zadaje +5% obrażeń przy trafieniu krytycznym za każdy 1 [StartXichun] (maks. 30%)<style="highlight"></style>
406. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [Burst] 5 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 5 [Burst]<style="highlight"></style>
407. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 6 — opis] <style="highlight">[CriticalOnSucceedAttack] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict +1 [Burst] Count</style>
   PL: <style="highlight">[CriticalOnSucceedAttack] Zwiększa Licznik [Burst] o 1</style>
408. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 7 — opis] [CriticalOnSucceedAttack] [Breath] 2 얻음. [Breath] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#6].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain 2 [Breath] and +1 [Breath] Count<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Zyskuje 2 [Breath] i zwiększa Licznik [Breath] o 1<style="highlight"></style>
409. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 8 — opis] [CriticalEnemyTargetKill] [Breath] 횟수 2 증가 (턴 당 3회)<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081203].levelList[level=4].coinlist[#0].coindescs[#7].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalEnemyTargetKill], [Breath]
   znaczenie tagów: [CriticalEnemyTargetKill] = [크리티컬 적 처치 시] / [On Crit Kill Against Enemy]; [Breath] = 호흡 / Poise
   EN: [CriticalEnemyTargetKill] Gain +2 [Breath] Count (3 times per turn)<style="highlight"></style>
   PL: [CriticalEnemyTargetKill] Zwiększa własny Licznik [Breath] o 2 (3 razy na turę)<style="highlight"></style>
410. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — nazwa] 적격 - 시[始]
   źródło: Skills_personality-08.json :: dataList[id=1081205].levelList[level=1].name ; dataList[id=1081205].levelList[level=2].name ; dataList[id=1081205].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 2 · monety: 2 (+2)
   limit: do 50 znaków
   EN: Crimson Strike - Launcher [始]
   PL: Szkarłatny Cios - Wyrzutnia [始]
411. [Umiejętność 4 (×0) (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] [Breath] 5 얻음, 자신의 [Breath] 횟수 2 증가\n[BeforeAttack] 자신의 [WaitingXichun]를 전부 소모하여, (자신의 [WaitingXichun] X 2)만큼 가중치 증가 (최대 5)
   źródło: Skills_personality-08.json :: dataList[id=1081205].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [Breath], [BeforeAttack], [WaitingXichun]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WaitingXichun] = 대[待] / Ready [待]
   EN: [CantDuel]\n[WhenUse] Gain 5 [Breath] and +2 [Breath] Count\n[BeforeAttack] Consume all [WaitingXichun] on self to gain +([WaitingXichun] on self x 2) Atk Weight (max 5)
   PL: [CantDuel]\n[WhenUse] Zyskuje 5 [Breath] i zwiększa własny Licznik [Breath] o 2\n[BeforeAttack] Zużywa całe własne [WaitingXichun], aby zyskać Waga ataku +([WaitingXichun] x 2) (maks. 5)
412. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081205].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081205].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081205].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL: [OnSucceedAttack] Nakłada 1 [Burst]
413. [Umiejętność 4 (×0) (ulepszenie 2) — opis] [CantDuel]\n[WhenUse] [Breath] 5 얻음, 자신의 [Breath] 횟수 2 증가\n<style="highlight">[WhenUse] 자신의 [WaitingXichun]가 3 이상이면, 코인 위력 +1</style>\n[BeforeAttack] 자신의 [WaitingXichun]를 전부 소모하여, (자신의 [WaitingXichun] X 2)만큼 가중치 증가 (최대 5)
   źródło: Skills_personality-08.json :: dataList[id=1081205].levelList[level=2].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [WhenUse], [Breath], [WaitingXichun], [BeforeAttack]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WaitingXichun] = 대[待] / Ready [待]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantDuel]\n[WhenUse] Gain 5 [Breath] and +2 [Breath] Count\n<style="highlight">[WhenUse] At 3+ [WaitingXichun], Coin Power +1</style>\n[BeforeAttack] Consume all [WaitingXichun] on self to gain +([WaitingXichun] on self x 2) Atk Weight (max 5)
   PL: [CantDuel]\n[WhenUse] Zyskuje 5 [Breath] i zwiększa własny Licznik [Breath] o 2\n<style="highlight">[WhenUse] Przy 3+ [WaitingXichun] Moc Monet +1</style>\n[BeforeAttack] Zużywa całe własne [WaitingXichun], aby zyskać Waga ataku +([WaitingXichun] x 2) (maks. 5)
414. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [CantDuel]\n[WhenUse] [Breath] 5 얻음, 자신의 [Breath] 횟수 2 증가\n[WhenUse] 자신의 [WaitingXichun]가 3 이상이면, 코인 위력 +<style="highlight">2</style>\n[BeforeAttack] 자신의 [WaitingXichun]를 전부 소모하여, (자신의 [WaitingXichun] X 2)만큼 가중치 증가 (최대 5)
   źródło: Skills_personality-08.json :: dataList[id=1081205].levelList[level=4].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [WhenUse], [Breath], [WaitingXichun], [BeforeAttack]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WaitingXichun] = 대[待] / Ready [待]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [CantDuel]\n[WhenUse] Gain 5 [Breath] and +2 [Breath] Count\n[WhenUse] At 3+ [WaitingXichun], Coin Power +<style="highlight">2</style>\n[BeforeAttack] Consume all [WaitingXichun] on self to gain +([WaitingXichun] on self x 2) Atk Weight (max 5)
   PL: [CantDuel]\n[WhenUse] Zyskuje 5 [Breath] i zwiększa własny Licznik [Breath] o 2\n[WhenUse] Przy 3+ [WaitingXichun] Moc Monet +<style="highlight">2</style>\n[BeforeAttack] Zużywa całe własne [WaitingXichun], aby zyskać Waga ataku +([WaitingXichun] x 2) (maks. 5)
415. [Obrona (ulepszenia 1,4) — nazwa] 수회
   źródło: Skills_personality-08.json :: dataList[id=1081204].levelList[level=1].name ; dataList[id=1081204].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Adept Evasion
   PL: Mistrzowskie Uniki
416. [Obrona (ulepszenie 1) — opis] [StartBattle] 자신의 [StartXichun]가 3 이상이면, 턴 종료 시 [RetreatForCommon]함.\n- 퇴각 시 대기 순서 1번이 됨 (대기 인원의 대기 해제보다 우선적으로 복귀함)\n[OnSucceedEvade] [Breath] 2 얻음. (턴 당 최대 2회)
   źródło: Skills_personality-08.json :: dataList[id=1081204].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [StartXichun], [RetreatForCommon], [OnSucceedEvade], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [StartXichun] = 시[始] / Launcher [始]; [RetreatForCommon] = 전장 퇴각 / Battlefield Retreat; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [StartBattle] At 3+ [StartXichun], perform a [RetreatForCommon] at Turn End.\n- Upon Retreat, move to the frontmost place in the Backup units' Deployment order (Returns first before the other Backup units Substitute in)\n[OnSucceedEvade] Gain 2 [Breath] (2 times per turn)
   PL: [StartBattle] Przy 3+ [StartXichun] wycofuje się [RetreatForCommon] na koniec tury.\n- Przy Odwrócie staje na 1. miejscu kolejki jednostek w rezerwie (Powrót przed innymi jednostkami w rezerwie)\n[OnSucceedEvade] Zyskuje 2 [Breath]. (maks. 2 razy na turę)
417. [Obrona (ulepszenie 4) — opis] [StartBattle] 자신의 [StartXichun]가 3 이상이면, 턴 종료 시 [RetreatForCommon]함.\n- 퇴각 시 대기 순서 1번이 됨 (대기 인원의 대기 해제보다 우선적으로 복귀함)\n<style="highlight">[WhenUse] [Breath] 횟수 1 증가 (턴 당 최대 2회)</style>\n[OnSucceedEvade] [Breath] 2 얻음. (턴 당 최대 2회)
   źródło: Skills_personality-08.json :: dataList[id=1081204].levelList[level=4].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [StartXichun], [RetreatForCommon], [WhenUse], [Breath], [OnSucceedEvade]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [StartXichun] = 시[始] / Launcher [始]; [RetreatForCommon] = 전장 퇴각 / Battlefield Retreat; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [StartBattle] At 3+ [StartXichun], perform a [RetreatForCommon] at Turn End.\n- Upon Retreat, move to the frontmost place in the Backup units' Deployment order (Returns first before the other Backup units Substitute in)\n<style="highlight">[WhenUse] Gain +1 [Breath] Count (2 times per turn)</style>\n[OnSucceedEvade] Gain 2 [Breath] (2 times per turn)
   PL: [StartBattle] Przy 3+ [StartXichun] wycofuje się [RetreatForCommon] na koniec tury.\n- Przy Odwrócie staje na 1. miejscu kolejki jednostek w rezerwie (Powrót przed innymi jednostkami w rezerwie)\n<style="highlight">[WhenUse] Zwiększa własny Licznik [Breath] o 1 (maks. 2 razy na turę)</style>\n[OnSucceedEvade] Zyskuje 2 [Breath]. (maks. 2 razy na turę)
418. [Pasywka bojowa (od ulepszenia 1) — nazwa] 시동[始動]
   źródło: Passives.json :: dataList[id=1081202].name
   limit: do 40 znaków
   EN: Launching Maneuver [始動]
   PL: Manewr Startowy [始動]
419. [Pasywka bojowa (od ulepszenia 1) — opis] 전투에서 퇴각할 때, 아군에게 편성 순서 순으로 다음 턴에 공격 레벨 증가 1 부여\n- 부여 대상 수 : 자신의 [StartXichun] 수치\n- 부여 대상이 "가씨 가문"이면, 대신 다음 턴에 공격 레벨 증가 2 부여\n- 다음 턴에 복귀, 대기 해제되는 인격에게는 부여되지 않음\n\n대기 해제 또는 복귀로 등장한 턴에 자신이 [WaitingXichun]를 얻고, 전투 시작시 스킬 순서상 가장 먼저 '적격 - 시【始】'를 무작위 대상에게 사용함
   źródło: Passives.json :: dataList[id=1081202].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n, [StartXichun], [WaitingXichun]
   znaczenie tagów: [StartXichun] = 시[始] / Launcher [始]; [WaitingXichun] = 대[待] / Ready [待]
   EN: Upon Retreat: apply 1 Offense Level Up next turn to allies in their Deployment order\n- Number of affected allies = [StartXichun] Stack on self\n- If the affected ally is a "Jia Family" unit, apply 2 Offense Level Up next turn instead\n- Does not affect allies that either Return or Substitute next turn\n\nOn the turn this unit Substituted or Returned to the field, gain [WaitingXichun]; then, at Combat Start, as the very first Skill in the Skill order, use 'Crimson Strike - Launcher【始】' against a random target.
   PL: Przy Odwrócie z walki nakłada 1 Wzrost Poziomu Ataku w następnej turze sojusznikom w kolejności przydziału\n- Liczba objętych sojuszników: liczba stosów [StartXichun]\n- Jeżeli objętym sojusznikiem jest jednostka „Rodu Jia”, zamiast tego nakłada 2 Wzrostu Poziomu Ataku w następnej turze\n- Nie dotyczy sojuszników, którzy w następnej turze Powracają albo Wchodzą z rezerwy\n\nW turze Wejścia z rezerwy albo Powrotu zyskuje [WaitingXichun], a na początku walki, jako pierwsza Umiejętność w kolejce, używa „Szkarłatny Cios - Wyrzutnia【始】” na losowym celu
420. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 대기 해제 혹은 복귀로 등장한 턴에 전투 시작시, 스킬 순서상 가장 먼저 "적격 - 시(始)"을 무작위 대상에게 사용함
   źródło: Passives.json :: dataList[id=1081202].summary
   limit: do 250 znaków
   EN: In the turn this unit entered the battle via Substitution or Return: at Combat Start, as the very first Skill in the Skill order, use 'Crimson Strike - Launcher (始)' against a random target
   PL: Na początku walki w turze Wejścia z rezerwy albo Powrotu, jako pierwsza Umiejętność w kolejce, używa "Szkarłatny Cios - Wyrzutnia(始)" na losowym celu
421. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — nazwa] 파흡자환[破吸自桓]
   źródło: Passives.json :: dataList[id=1081201].name
   limit: do 50 znaków
   EN: Rupture-breathing Resolve [破吸自桓]
   PL: Rozrywający Oddech [破吸自桓]
422. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — opis] 자신의 공격 스킬로 대상 처치 시 대상의 [Burst]만큼 [Breath]을 얻음 (적 1명당 최대 3, 턴 당 최대 1회)\n- 위 효과로 [Breath]을 3까지 얻었다면, 대상의 [Burst] 횟수만큼 자신의 [Breath] 횟수 증가 (적 1명당 최대 2, 턴 당 최대 1회)\n\n합 진행 시 합을 진행하는 적보다 공격 레벨이 높으면, 합 위력 +1\n\n합 진행 시 합을 진행하는 적보다 공격 레벨이 높으면, 기본 공격 스킬로 부여하는 [Burst] 위력 또는 [Burst] 횟수 +1 (턴 당 2회 발동)
   źródło: Passives.json :: dataList[id=1081201].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Breath]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: When killing the target with this unit's Attack Skills, gain [Breath] equal to [Burst] on target (3 per 1 enemy; once per turn)\n- If this unit gained 3 [Breath] with the above effect, gain [Breath] Count equal to [Burst] Count on target (2 per 1 enemy; once per turn)\n\nIn a Clash, if this unit's Offense Level is higher than the target's, Clash Power +1\n\nIn a Clash, if this unit's Offense Level is higher than the target's, inflict +1 more [Burst] Potency or [Burst] Count with this unit's Base Attack Skills (2 times per turn)
   PL: Gdy zabija cel Umiejętnością ataku, zyskuje [Breath] równy wartości [Burst] celu (maks. 3 na 1 wroga, maks. 1 raz na turę)\n- Jeżeli zyskał tak 3 [Breath], zwiększa własny Licznik [Breath] o wartość Licznika [Burst] celu (maks. 2 na 1 wroga, maks. 1 raz na turę)\n\nW starciu, jeżeli Poziom Ataku jest wyższy niż wroga prowadzącego starcie, Moc Starcia +1\n\nW starciu, jeżeli Poziom Ataku jest wyższy niż wroga prowadzącego starcie, podstawowe Umiejętności ataku nakładają o 1 więcej Mocy lub Licznika [Burst] (2 razy na turę)
423. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — podsumowanie] 합을 할 때, 공격 대상보다 공격 레벨이 높을 경우, 합 위력 +1\n기본 공격 스킬로 부여하는 [Burst] 위력 혹은 [Burst] 횟수 +1
   źródło: Passives.json :: dataList[id=1081201].summary
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: In a Clash, if this unit's Offense Level is higher than the target's, Clash Power +1\nInflict +1 more [Burst] Potency and [Burst] Count with this unit's Base Attack Skills
   PL: W starciu, jeżeli Poziom Ataku jest wyższy niż celu, Moc Starcia +1\nPodstawowe Umiejętności ataku nakładają o 1 więcej Mocy i Licznika [Burst]
424. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — nazwa] 여환[餘桓]
   źródło: Passives.json :: dataList[id=1081221].name
   limit: do 40 znaków
   EN: Lingering Resolve [餘桓]
   PL: Przedłużone Postanowienie [餘桓]
425. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — opis] 전투 중 자신이 사망했으면, 자신 다음 턴에 대기해제 되는 인격(대기 편성 순서상 가장 빠른 인격)에게 전투 시작 시 [CheerUpXichun] 부여\n\n연속 전투에서 자신이 퇴각 혹은 대기 상태일 때, 아래의 효과 발동\n전투 시작 시 체력이 최대 체력의 50% 이하이고, 수비 스킬을 사용한 인격 중 편성 순서가 가장 빠른 인격이 턴 종료 시 피해로 인한 흐트러짐을 해제하고  [RetreatForCommon]함 (전투당 2회 발동)
   źródło: Passives.json :: dataList[id=1081221].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n, [CheerUpXichun], [RetreatForCommon]
   znaczenie tagów: [CheerUpXichun] = 원[援] / Assist [援]; [RetreatForCommon] = 전장 퇴각 / Battlefield Retreat
   EN: If this unit is defeated in an Encounter, apply [CheerUpXichun] to the subsequently Substituting Identity (the fastest Backup Unit in the Deployment Order) next turn\n\nIn Chain Battles, if this unit is a Backup unit or has Retreated, activate the following:\n- Combat Start: Among the Identities who 1) are at 50% HP or lower, and 2) used a Defense Skill, choose the Identity with the earliest Deployment order. At Turn End, that Identity recovers from Stagger due to damage and performs a [RetreatForCommon] (2 times per Encounter)
   PL: Jeżeli ta jednostka ginie podczas walki, nakłada [CheerUpXichun] na początku walki Tożsamości, która Wejdzie z rezerwy w następnej turze (najwcześniej przydzielona jednostka w rezerwie)\n\nW walkach łańcuchowych, gdy ta jednostka jest w rezerwie albo się wycofała, uruchamia poniższy efekt:\nNa początku walki Tożsamość z HP równym 50% Maks. HP lub niższym, która użyła Umiejętności obrony i ma najwcześniejszy przydział, na koniec tury dochodzi z Ogłuszenia od obrażeń i wycofuje się [RetreatForCommon] (2 razy na spotkanie)
426. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — podsumowanie] 전투 시작 시 체력이 50%이하이고 수비 스킬을 사용한 인격을 턴 종료 시, 퇴각 시킴
   źródło: Passives.json :: dataList[id=1081221].summary
   limit: do 150 znaków
   EN: Turn End: Retreat the Identity that, at Combat Start, has 50% or less HP and has used a Defense Skill this turn
   PL: Na koniec tury wycofuje Tożsamość, która na początku walki ma 50% HP lub mniej i użyła w tej turze Umiejętności obrony

## [000] Jeong's Office Rep — Ishmael — 정사무소 대표
- ID Tożsamości: `10813` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9107 · HP bazowe: 88 · szybkość: 2–6 / 2–6 / 3–7 / 3–8
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Tremor, Sinking

427. [Karta Tożsamości — tytuł] 정사무소\n대표
   źródło: Personalities.json :: dataList[id=10813].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Jeong's Office Rep
   PL: Biuro Jeonga\nRep
428. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10813].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10813].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Karta Tożsamości — opis] 이스마엘의 열세번째 인격
   źródło: Personalities.json :: dataList[id=10813].desc
   limit: do 120 znaków
   EN: Ishmael's 13th Identity
   PL: Trzynasta Tożsamość Ishmael
431. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 츠루기리[鶴斬り]
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=1].name ; dataList[id=1081301].levelList[level=2].name ; dataList[id=1081301].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Tsuru-giri [鶴斬り]
   PL: Tsuru-giri [鶴斬り]
432. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Discard]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard
   EN: [WhenUse] If the other Skill in the same Skill Slot is a different Skill, [Discard] that Skill
   PL: [WhenUse] Jeżeli druga Umiejętność w tym slocie jest inna niż ta, [Discard] ją
433. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] celu o 1
434. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]\n<style="highlight">[WhenUse] 대상의 [Vibration]과 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Discard], [Vibration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If the other Skill in the same Skill Slot is a different Skill, [Discard] that Skill\n<style="highlight">[WhenUse] If target has 6+ ([Vibration] + [Sinking]), Coin Power +1</style>
   PL: [WhenUse] Jeżeli druga Umiejętność w tym slocie jest inna niż ta, [Discard] ją\n<style="highlight">[WhenUse] Przy 6+ (suma [Vibration] i [Sinking] celu) Moc Monet +1</style>
436. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] celu o 1<style="highlight"></style>
437. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [Sinking] 횟수 1 증가</style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[OnSucceedAttackHead] Inflict +1 [Sinking] Count</style>
   PL: <style="highlight">[OnSucceedAttackHead] Zwiększa Licznik [Sinking] o 1</style>
438. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081301].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]<style="highlight"></style>
439. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [Vibration] 횟수 1 증가</style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttackHead] Inflict +1 [Vibration] Count</style>
   PL: <style="highlight">[OnSucceedAttackHead] Zwiększa Licznik [Vibration] o 1</style>
440. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]\n<style="highlight">[WhenUse] 대상의 [Vibration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Discard], [Vibration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If the other Skill in the same Skill Slot is a different Skill, [Discard] that Skill\n<style="highlight">[WhenUse] Coin Power +1 for every 6 ([Vibration] + [Sinking]) on target (max 2)</style>
   PL: [WhenUse] Jeżeli druga Umiejętność w tym slocie jest inna niż ta, [Discard] ją\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 (suma [Vibration] i [Sinking] celu) (maks. 2)</style>
441. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +1 [Sinking] Count<style="highlight"></style>
   PL: [OnSucceedAttackHead] Zwiększa Licznik [Sinking] o 1<style="highlight"></style>
442. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081301].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict +1 [Vibration] Count<style="highlight"></style>
   PL: [OnSucceedAttackHead] Zwiększa Licznik [Vibration] o 1<style="highlight"></style>
443. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 억새 흘리기
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=1].name ; dataList[id=1081302].levelList[level=2].name ; dataList[id=1081302].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Susuki Misdirection
   PL: Zmylenie Susuki
444. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=1].desc
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]\n<style="highlight">[WhenUse] 대상의 [Vibration]과 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=2].desc
   (powtórzenie elementu 435 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Sinking]<style="highlight"></style>
449. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [Sinking] 1 부여</style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[OnSucceedAttackHead] Inflict 1 [Sinking]</style>
   PL: <style="highlight">[OnSucceedAttackHead] Nakłada 1 [Sinking]</style>
450. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]<style="highlight"></style>
451. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [Vibration] 1 부여</style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttackHead] Inflict 1 [Vibration]</style>
   PL: <style="highlight">[OnSucceedAttackHead] Nakłada 1 [Vibration]</style>
452. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]\n<style="highlight">[WhenUse] 대상의 [Vibration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=4].desc
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 1 [Sinking]<style="highlight"></style>
   PL: [OnSucceedAttackHead] Nakłada 1 [Sinking]<style="highlight"></style>
454. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 1 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttackHead] Nakłada 1 [Vibration]<style="highlight"></style>
455. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 정신력 5 회복</style>
   źródło: Skills_personality-08.json :: dataList[id=1081302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] Heal 5 SP</style>
   PL: <style="highlight">[OnSucceedAttack] Odzyskuje 5 Poczytalności</style>
456. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 사쿠라센[桜閃]
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].name ; dataList[id=1081303].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Sakura-sen [桜閃]
   PL: Sakura-sen [桜閃]
457. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 [HanafudaCombo] 위력 1당 피해량 +5%\n[WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]\n[WhenUse] 대상의 [Vibration]과 [Sinking]의 합이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [HanafudaCombo], [WhenUse], [Discard], [Vibration], [Sinking]
   znaczenie tagów: [HanafudaCombo] = 광【光】 / Bright【光】; [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: Deal +5% damage for every [HanafudaCombo] Potency on self\n[WhenUse] If the other Skill in the same Skill Slot is a different Skill, [Discard] that Skill\n[WhenUse] If target has 6+ ([Vibration] + [Sinking]), Coin Power +1
   PL: Zadaje +5% obrażeń za każdą 1 Moc [HanafudaCombo]\n[WhenUse] Jeżeli druga Umiejętność w tym slocie jest inna niż ta, [Discard] ją\n[WhenUse] Przy 6+ (suma [Vibration] i [Sinking] celu) Moc Monet +1
458. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Vibration]
459. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Sinking]
460. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] [Sinking] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +1 [Sinking] Count
   PL: [OnSucceedAttackHead] Zwiększa Licznik [Sinking] celu o 1
461. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] Nakłada 3 [Vibration]
462. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL: [OnSucceedAttack] Nakłada 3 [Sinking]
463. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttackHead] [Vibration] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttackHead] Nakłada +1 Licznika [Vibration]
464. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상이 [Switch_Vibration] 상태가 아니면, [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Switch_Vibration], [VibrationCollapse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay
   EN: [OnSucceedAttack] If target isn't in an [Switch_Vibration] state, trigger [Switch_Vibration] into [VibrationCollapse]
   PL: [OnSucceedAttack] Jeżeli cel nie jest w stanie [Switch_Vibration], wywołuje [Switch_Vibration] do [VibrationCollapse]
465. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 [HanafudaCombo] 위력 1당 피해량 <style="highlight">+10%</style>\n[WhenUse] 이 스킬 슬롯의 장착하지 않은 스킬이 이 스킬과 다르면 [Discard]\n<style="highlight">[WhenUse] 대상의 [Vibration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 3)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [HanafudaCombo], [WhenUse], [Discard], [Vibration], [Sinking]
   znaczenie tagów: [HanafudaCombo] = 광【光】 / Bright【光】; [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: Deal +<style="highlight">10</style>% damage for every [HanafudaCombo] Potency on self\n[WhenUse] If the other Skill in the same Skill Slot is a different Skill, [Discard] that Skill\n<style="highlight">[WhenUse] Coin Power +1 for every 6 ([Vibration] + [Sinking]), on target (max 3)</style>
   PL: Zadaje <style="highlight">+10%</style> obrażeń za każdą 1 Moc [HanafudaCombo]\n[WhenUse] Jeżeli druga Umiejętność w tym slocie jest inna niż ta, [Discard] ją\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 (suma [Vibration] i [Sinking] celu) (maks. 3)</style>
466. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Vibration]<style="highlight"></style>
467. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] celu o 2<style="highlight"></style>
468. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 441 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Vibration]<style="highlight"></style>
470. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 3 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Sinking]<style="highlight"></style>
471. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttackHead] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">대상이 [Switch_Vibration] 이나 [FusionVibration] 상태면, 이 코인 피해량 +48%</style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Switch_Vibration], [FusionVibration]
   znaczenie tagów: [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: <style="highlight"> If target is in either [Switch_Vibration] or [FusionVibration] states, this Coin deals +48% damage</style>
   PL: <style="highlight"> Jeżeli cel jest w stanie [Switch_Vibration] albo [FusionVibration], ta moneta zadaje +48% obrażeń</style>
473. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상이 [Switch_Vibration] 상태가 아니면, [VibrationCollapse]로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081303].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Switch_Vibration], [VibrationCollapse]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay
   EN: [OnSucceedAttack] If target isn't in an [Switch_Vibration] state, trigger [Switch_Vibration] into [VibrationCollapse]<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli cel nie jest w stanie [Switch_Vibration], wywołuje [Switch_Vibration] do [VibrationCollapse]<style="highlight"></style>
474. [Umiejętność 4 (×0) (ulepszenia 1,4) — nazwa] 코오쟌[光斬]
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=1].name ; dataList[id=1081305].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Kōzan [光斬]
   PL: Kōzan [光斬]
475. [Umiejętność 4 (×0) (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않으며, 외부 효과로 재사용이 불가능함\n\n[WhenUse] 자신의 [HanafudaCombo] 위력이 3 미만이면, 스킬이 취소되고 다음 턴에 [Enhancement] 2 얻음\n[WhenUse] 자신의 [HanafudaCombo] 위력이 3 이상이면, 위력당 아래 효과 적용\n- 1당 이 스킬 피해량 +10%\n- 4 이상이면, 기본 위력 +1\n- 5면, 마지막 재사용 코인 적중시 [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 1 감소\n[EndSkillAll] 자신의 [HanafudaCombo] 소멸\n[EndSkillAll] 다음 턴에 ‘짝패’를 자신이 보유한 기본 공격 스킬에 대응되는 무작위 ‘짝패’로 변경 (턴당 1회)\n[EndSkillAll] 사용하지 못한 코인 갯수만큼 다음 턴에 [HanafudaCombo] 위력 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=1].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [HanafudaCombo], [Enhancement], [VibrationExplosion], [Vibration], [EndSkillAll]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [HanafudaCombo] = 광【光】 / Bright【光】; [Enhancement] = 공격 위력 증가 / Attack Power Up; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [EndSkillAll] = [스킬 종료시] / [Skill End]
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills, and external effects cannot trigger this Skill to be Reused\n\n[WhenUse] At less than 3 [HanafudaCombo] Potency, cancel the Skill and gain 2 [Enhancement] next turn\n[WhenUse] At 3+ [HanafudaCombo] Potency, gain the following effects based on Potency:\n- Per 1 Potency: this Skill deals +10% damage\n- At 4+ Potency: Base Power +1\n- At 5 Potency: On Hit with the final Reuse Coin, trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 1\n[EndSkillAll] Lose [HanafudaCombo] on self\n[EndSkillAll] Next turn, convert the Suit in this unit's Hand to a random Suit that corresponds to one of this unit's Base Attack Skills (once per turn)\n[EndSkillAll] Gain [HanafudaCombo] Potency next turn equal to the # of Coins that weren't used
   PL: [CantDuel]\nTa Umiejętność nie uruchamia Umiejętności obrony, a zewnętrzne efekty nie mogą jej ponownie użyć\n\n[WhenUse] Przy mniej niż 3 Mocy [HanafudaCombo], anuluje Umiejętność i zyskuje 2 [Enhancement] w następnej turze\n[WhenUse] Przy 3+ Mocy [HanafudaCombo], stosuje poniższe efekty w zależności od Mocy:\n- Za każdą 1 Moc ta Umiejętność zadaje +10% obrażeń\n- Przy 4+ Mocy Moc Bazowa +1\n- Przy 5 Mocy, przy trafieniu ostatnią ponownie użytą monetą wywołuje [VibrationExplosion] 2 razy. Zmniejsza Licznik [Vibration] celu o 1\n[EndSkillAll] Traci [HanafudaCombo]\n[EndSkillAll] W następnej turze zamienia „kolor” na losowy „kolor” odpowiadający jednej z własnych podstawowych Umiejętności ataku (1 raz na turę)\n[EndSkillAll] Zyskuje w następnej turze Moc [HanafudaCombo] równą liczbie nieużytych monet
476. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] 자신의 ([HanafudaCombo] 위력 - 1)만큼 이 코인 재사용 (최대 4회)
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [HanafudaCombo]
   znaczenie tagów: [HanafudaCombo] = 광【光】 / Bright【光】
   EN: Reuse this Coin ([HanafudaCombo] Potency - 1) times (4 times max)
   PL: Ponownie używa tę monetę (Moc [HanafudaCombo] - 1) razy (maks. 4)
477. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않으며, 외부 효과로 재사용이 불가능함\n\n[WhenUse] 자신의 [HanafudaCombo] 위력이 3 미만이면, 스킬이 취소되고 다음 턴에 [Enhancement] 2 얻음\n[WhenUse] 자신의 [HanafudaCombo] 위력이 3 이상이면, 위력당 아래 효과 적용\n- 1당 이 스킬 피해량 +10%\n- 4 이상이면, 기본 위력 +1\n- 5면, 마지막 재사용 코인 적중시 [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 1 감소\n[EndSkillAll] 자신의 [HanafudaCombo] 소멸\n[EndSkillAll] 다음 턴에 ‘짝패’를 자신이 보유한 기본 공격 스킬에 대응되는 무작위 ‘짝패’로 변경 (턴당 1회)\n[EndSkillAll] 사용하지 못한 코인 갯수만큼 다음 턴에 [HanafudaCombo] 위력 얻음<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=4].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [WhenUse], [HanafudaCombo], [Enhancement], [VibrationExplosion], [Vibration], [EndSkillAll]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [HanafudaCombo] = 광【光】 / Bright【光】; [Enhancement] = 공격 위력 증가 / Attack Power Up; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [EndSkillAll] = [스킬 종료시] / [Skill End]
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills, and external effects cannot trigger this Skill to be Reused\n\n[WhenUse] At less than 3 [HanafudaCombo] Potency, cancel the Skill and gain 2 [Enhancement] next turn\n[WhenUse] At 3+ [HanafudaCombo] Potency, gain the following effects based on Potency:\n- Per 1 Potency: this Skill deals +10% damage\n- At 4+ Potency: Base Power +1\n- At 5 Potency: On Hit with the final Reuse Coin, trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 1\n[EndSkillAll] Lose [HanafudaCombo] on self\n[EndSkillAll] Next turn, convert the Suit in this unit's Hand to a random Suit that corresponds to one of this unit's Base Attack Skills (once per turn)\n[EndSkillAll] Gain [HanafudaCombo] Potency next turn equal to the # of Coins that weren't used<style="highlight"></style>
   PL: [CantDuel]\nTa Umiejętność nie uruchamia Umiejętności obrony, a zewnętrzne efekty nie mogą jej ponownie użyć\n\n[WhenUse] Przy mniej niż 3 Mocy [HanafudaCombo], anuluje Umiejętność i zyskuje 2 [Enhancement] w następnej turze\n[WhenUse] Przy 3+ Mocy [HanafudaCombo], stosuje poniższe efekty w zależności od Mocy:\n- Za każdą 1 Moc ta Umiejętność zadaje +10% obrażeń\n- Przy 4+ Mocy Moc Bazowa +1\n- Przy 5 Mocy, przy trafieniu ostatnią ponownie użytą monetą wywołuje [VibrationExplosion] 2 razy. Zmniejsza Licznik [Vibration] celu o 1\n[EndSkillAll] Traci [HanafudaCombo]\n[EndSkillAll] W następnej turze zamienia „kolor” na losowy „kolor” odpowiadający jednej z własnych podstawowych Umiejętności ataku (1 raz na turę)\n[EndSkillAll] Zyskuje w następnej turze Moc [HanafudaCombo] równą liczbie nieużytych monet<style="highlight"></style>
480. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] 자신의 ([HanafudaCombo] 위력 - 1)만큼 이 코인 재사용 (최대 4회)<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [HanafudaCombo]
   znaczenie tagów: [HanafudaCombo] = 광【光】 / Bright【光】
   EN: Reuse this Coin ([HanafudaCombo] Potency - 1) times (4 times max)<style="highlight"></style>
   PL: Ponownie używa tę monetę (Moc [HanafudaCombo] - 1) razy (maks. 4)<style="highlight"></style>
481. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 4 — opis] <style="highlight">[OnSucceedAttackHead] [DefenseDown] 1 부여</style>
   źródło: Skills_personality-08.json :: dataList[id=1081305].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: <style="highlight">[OnSucceedAttackHead] Inflict 1 [DefenseDown]</style>
   PL: <style="highlight">[OnSucceedAttackHead] Nakłada 1 [DefenseDown]</style>
484. [Obrona (ulepszenia 1,4) — nazwa] 화투패 섞기
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=1].name ; dataList[id=1081304].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Shuffle Hands - Floral Deck
   PL: Tasowanie Ręki - Talia Kwiatów
485. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 2개를 [Discard] (턴당 1회)\n[StartBattle] 자신의 가장 왼쪽 슬롯에 장착했으면, 다음 턴에 ‘짝패’를 자신이 보유한 기본 공격 스킬에 대응되는 무작위 ‘짝패’로 변경 (턴당 1회. 보유한 ‘짝패’와 동일한 ‘짝패’ 제외)
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [Discard]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [Discard] = 버림 / Discard
   EN: [DuelCounter]\n[StartBattle] [Discard] 2 Skills of the lowest rank in all of this unit's Skill Slots (once per turn)\n[StartBattle] If this Skill was equipped on this unit's leftmost Skill Slot, convert the Suit in this unit's Hand to a random Suit that corresponds to one of this unit's Base Attack Skills next turn. (once per turn; excluding the Suit already in this unit's Hand)
   PL: [DuelCounter]\n[StartBattle] [Discard] 2 Umiejętności o najniższej randze ze wszystkich slotów Umiejętności (1 raz na turę)\n[StartBattle] Jeżeli wyposażona w najbardziej lewym slocie, zamienia w następnej turze „kolor” na losowy „kolor” odpowiadający jednej z własnych podstawowych Umiejętności ataku (1 raz na turę; z wyłączeniem „koloru” już posiadanego)
486. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[StartBattle] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 2개를 [Discard] (턴당 1회)\n[StartBattle] 자신의 가장 왼쪽 슬롯에 장착했으면, 다음 턴에 ‘짝패’를 자신이 보유한 기본 공격 스킬에 대응되는 무작위 ‘짝패’로 변경 (턴당 1회. 보유한 ‘짝패’와 동일한 ‘짝패’ 제외)\n<style="highlight">[StartBattle] 50% 확률로 [HanafudaCombo] 위력 1 얻음 (턴당 1회)</style>\n<style="highlight">[WhenUse] 자신의 [HanafudaCombo] 위력 2당 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=4].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [Discard], [HanafudaCombo], [WhenUse]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [Discard] = 버림 / Discard; [HanafudaCombo] = 광【光】 / Bright【光】; [WhenUse] = [사용시] / [On Use]
   EN: [DuelCounter]\n[StartBattle] [Discard] 2 Skills of the lowest rank in all of this unit's Skill Slots (once per turn)\n[StartBattle] If this Skill was equipped on this unit's leftmost Skill Slot, convert the Suit in this unit's Hand to a random Suit that corresponds to one of this unit's Base Attack Skills next turn. (once per turn; excluding the Suit already in this unit's Hand)\n<style="highlight">[StartBattle] 50% chance to gain 1 [HanafudaCombo] Potency (once per turn)</style>\n<style="highlight">[WhenUse] Coin Power +1 for every 2 [HanafudaCombo] Potency on self (max 2)</style>
   PL: [DuelCounter]\n[StartBattle] [Discard] 2 Umiejętności o najniższej randze ze wszystkich slotów Umiejętności (1 raz na turę)\n[StartBattle] Jeżeli wyposażona w najbardziej lewym slocie, zamienia w następnej turze „kolor” na losowy „kolor” odpowiadający jednej z własnych podstawowych Umiejętności ataku (1 raz na turę; z wyłączeniem „koloru” już posiadanego)\n<style="highlight">[StartBattle] 50% szansy na zyskanie 1 Mocy [HanafudaCombo] (1 raz na turę)</style>\n<style="highlight">[WhenUse] Moc Monet +1 za każde 2 Mocy [HanafudaCombo] (maks. 2)</style>
489. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081304].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Pasywka bojowa (od ulepszenia 1) — nazwa] 코이코이[こいこい]
   źródło: Passives.json :: dataList[id=1081302].name
   limit: do 40 znaków
   EN: Koi-Koi [こいこい]
   PL: Koi-Koi [こいこい]
492. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 시작시 [HanafudaCombo]이 없으면, [HanafudaCombo] 위력 0, 횟수 3 얻음\n\n턴 시작시 ‘짝패’가 없으면, [HanafudaOne], [HanafudaTwo], [HanafudaThree] 중 자신의 가장 왼쪽 슬롯의 기본 공격 스킬에 대응되는 무작위 ‘짝패’ 얻음\n\n전투 시작시 자신의 가장 왼쪽 슬롯에 장착한 기본 공격 스킬 또는 E.G.O 스킬이 사용될 때 아래 효과 적용 (턴당 1회)\n- 다음 턴에 해당 스킬에 대응되는 ‘짝패’로 변경\n- '사쿠라센' 또는 E.G.O 스킬이면, [HanafudaCombo] 위력 1 얻음\n- 해당 스킬 속성이 ‘짝패’와 일치하면, 아래 효과 적용\n  · [HanafudaCombo] 위력 1 얻음\n  · 이전 턴과 연속으로 ‘짝패’가 일치했으면, [HanafudaCombo] 위력 1 얻음\n  · 해당 스킬 적중 시 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n  · 25% 확률로 해당 스킬 속성의 E.G.O 자원 1 얻음\n- 해당 스킬 종료 시 [HanafudaCombo] 위력이 5거나, 횟수가 0이면, '코오쟌' 발동
   źródło: Passives.json :: dataList[id=1081302].desc
   limit: do 1500 znaków
   tokeny: zachowaj dokładnie: \n, [HanafudaCombo], [HanafudaOne], [HanafudaTwo], [HanafudaThree], [VibrationExplosion], [Vibration]
   znaczenie tagów: [HanafudaCombo] = 광【光】 / Bright【光】; [HanafudaOne] = 짝패 - 송학 / Hand - Pine Crane Suit; [HanafudaTwo] = 짝패 - 억새 / Hand - Susuki Grass Suit; [HanafudaThree] = 짝패 - 청벚꽃 / Hand - Blue Sakura Suit; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: Turn Start: if this unit does not have [HanafudaCombo], gain 0 [HanafudaCombo] Potency and 3 [HanafudaCombo] Count\n\nTurn Start: if this unit does not have a Suit in Hand, gain a random Suit([HanafudaOne], [HanafudaTwo], or [HanafudaThree]) that corresponds to a Base Attack Skill on this unit's leftmost Skill Slot\n\nCombat Start: when this unit uses a Base Attack Skill or an E.G.O Skill equipped on its leftmost Skill Slot, activate the following (once per turn):\n- Next turn, convert the Hand on self to the one corresponding to the used Skill's Affinity\n- If the Skill was either "Sakura-sen" or an E.G.O Skill, gain 1 [HanafudaCombo] Potency\n- If the Skill's Affinity matches the Affinity on the current Hand's description(thus "forming a Hand"), activate the following:\n  · Gain 1 [HanafudaCombo] Potency\n  · If this unit formed a Hand last turn and this turn in succession, gain 1 [HanafudaCombo] Potency\n  · On Hit with the said Skill: trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n  · 25% chance to gain 1 E.G.O Resource corresponding to the Skill's Affinity\n- At the Skill's Skill End: at 5 [HanafudaCombo] Potency, or at 0 [HanafudaCombo] Count, use "Kōzan"
   PL: Na początku tury, jeżeli nie ma [HanafudaCombo], zyskuje 0 Mocy [HanafudaCombo] i 3 Licznika [HanafudaCombo]\n\nNa początku tury, jeżeli nie ma „koloru”, zyskuje losowy „kolor” ([HanafudaOne], [HanafudaTwo] lub [HanafudaThree]) odpowiadający podstawowej Umiejętności ataku w najbardziej lewym slocie\n\nNa początku walki, przy użyciu podstawowej Umiejętności ataku albo Umiejętności E.G.O wyposażonej w najbardziej lewym slocie, stosuje poniższe efekty (1 raz na turę)\n- W następnej turze zamienia „kolor” na ten odpowiadający atrybutowi użytej Umiejętności\n- Jeżeli Umiejętnością jest „Sakura-sen” albo Umiejętność E.G.O, zyskuje 1 Moc [HanafudaCombo]\n- Jeżeli atrybut Umiejętności zgadza się z „kolorem”, stosuje poniższe efekty:\n  · Zyskuje 1 Moc [HanafudaCombo]\n  · Jeżeli „kolor” pasował też w poprzedniej turze, zyskuje 1 Moc [HanafudaCombo]\n  · Przy trafieniu tą Umiejętnością wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1\n  · 25% szansy na zyskanie 1 zasobu E.G.O atrybutu Umiejętności\n- Na koniec Umiejętności, przy 5 Mocy [HanafudaCombo] albo 0 Licznika [HanafudaCombo], stosuje „Kōzan”
493. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 짝패를 맞추면, [HanafudaCombo] 얻음. 진동 폭발.
   źródło: Passives.json :: dataList[id=1081302].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [HanafudaCombo]
   znaczenie tagów: [HanafudaCombo] = 광【光】 / Bright【光】
   EN: When forming a Hand, gain [HanafudaCombo]. Trigger Tremor Burst.
   PL: Przy dopasowaniu „koloru” zyskuje [HanafudaCombo]. Wywołuje [VibrationExplosion].
494. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Sloth, posiadane 2× Gloom) — nazwa] 낱장치기
   źródło: Passives.json :: dataList[id=1081301].name
   limit: do 40 znaków
   EN: Stacking the Deck
   PL: Przekładanie Kart
495. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Sloth, posiadane 2× Gloom) — opis] 뒷면 적중 시 정신력 5 회복 (턴 당 1회)\n사기 저하 또는 패닉 상태인 적에게 가하는 피해량 +10%
   źródło: Passives.json :: dataList[id=1081301].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Tails Hit, heal 5 SP (once per turn)\nDeal +10% damage against targets in either Low Morale or Panic states
   PL: Przy trafieniu rewersem odzyskuje 5 Poczytalności (1 raz na turę)\nZadaje +10% obrażeń celom w stanie Niskiego Moralu albo Paniki
496. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Sloth, posiadane 2× Gloom) — podsumowanie] 정신력 회복\n사기 저하, 패닉 대상에게 가하는 피해량 증가
   źródło: Passives.json :: dataList[id=1081301].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heal SP\nDeal more damage against Low Morale or Panicked targets
   PL: Odzyskuje Poczytalność\nZadaje więcej obrażeń celom z Niskim Moralami albo w Panice
497. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth, posiadane 3× Gloom) — nazwa] 중계
   źródło: Passives.json :: dataList[id=1081321].name
   limit: do 40 znaków
   EN: Relay
   PL: Przekaźnik
498. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth, posiadane 3× Gloom) — opis] 전투 시작시 정신력이 가장 낮은 아군 1명이 기본 공격 스킬로 앞면 적중시 해당 아군 정신력 5 회복 (턴당 2회, 정신력이 -40 이하인 아군 제외)
   źródło: Passives.json :: dataList[id=1081321].desc
   limit: do 200 znaków
   EN: Combat Start: when 1 ally that has the least SP uses a Base Attack Skill to Heads Hit, it heals 5 SP (2 times per turn; excluding allies at -40 or lower SP)
   PL: Na początku walki, gdy 1 Sojusznik z najniższą Poczytalnością trafi awersem podstawową Umiejętnością ataku, odzyskuje 5 Poczytalności (2 razy na turę; bez sojuszników z Poczytalnością -40 lub niższą)
499. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth, posiadane 3× Gloom) — podsumowanie] 정신력 회복
   źródło: Passives.json :: dataList[id=1081321].summary
   limit: do 120 znaków
   EN: Heal SP
   PL: Odzyskiwanie Poczytalności

## [000] The House of Spiders: The Middle Apprentice — Ishmael — 거미집 중지 제자
- ID Tożsamości: `10814` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 7 · HP bazowe: 92 · szybkość: 2–6 / 3–6 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Bleed, Burn

500. [Karta Tożsamości — tytuł] 거미집\n중지 제자
   źródło: Personalities.json :: dataList[id=10814].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The House of Spiders:\nThe Middle Apprentice
   PL: Dom Pajęczyn:\nUczeń Środkowego
501. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10814].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10814].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Karta Tożsamości — opis] 이스마엘의 열네번째 인격
   źródło: Personalities.json :: dataList[id=10814].desc
   limit: do 120 znaków
   EN: Ishmael's 14th Identity
   PL: Czternasta Tożsamość Ishmael
504. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 욜라 패기
   źródło: Skills_personality-08.json :: dataList[id=1081401].levelList[level=1].name ; dataList[id=1081401].levelList[level=2].name ; dataList[id=1081401].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Totally Badass Ass-kicking
   PL: Totalny Sznyt
505. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 정신력 5 회복
   źródło: Skills_personality-08.json :: dataList[id=1081401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 5 SP
   PL: [WhenUse] Odzyskuje 5 Poczytalności
506. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">대상의 [Combustion]과 [Laceration]의 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 정신력 5 회복
   źródło: Skills_personality-08.json :: dataList[id=1081401].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [Laceration], [WhenUse]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">If target has 6+ ([Combustion] + [Laceration]), Coin Power +1</style>\n[WhenUse] Heal 5 SP
   PL: <style="highlight">Przy 6+ (suma [Combustion] i [Laceration] celu) Moc Monet +1</style>\n[WhenUse] Odzyskuje 5 Poczytalności
508. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081401].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Laceration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Laceration]
509. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 추가 타격 피해 5</style>
   źródło: Skills_personality-08.json :: dataList[id=1081401].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] Deal 5 Blunt bonus damage</style>
   PL: <style="highlight">[OnSucceedAttack] Zadaje 5 dodatkowych obrażeń Uderzenia</style>
510. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Combustion]과 [Laceration]의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 정신력 5 회복<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081401].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [Laceration], [WhenUse]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]
   EN: If target has 6+ ([Combustion] + [Laceration]), Coin Power +1\n[WhenUse] Heal 5 SP<style="highlight"></style>
   PL: Przy 6+ (suma [Combustion] i [Laceration] celu) Moc Monet +1\n[WhenUse] Odzyskuje 5 Poczytalności<style="highlight"></style>
511. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 329 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 5<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 Blunt bonus damage<style="highlight"></style>
   PL: [OnSucceedAttack] Zadaje 5 dodatkowych obrażeń Uderzenia<style="highlight"></style>
513. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [ReinforcedTattooIshmael]이 있으면, [Laceration] 횟수 1 증가</style>
   źródło: Skills_personality-08.json :: dataList[id=1081401].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ReinforcedTattooIshmael], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ReinforcedTattooIshmael] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack] If this unit has [ReinforcedTattooIshmael], inflict +1 [Laceration] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli ma [ReinforcedTattooIshmael], zwiększa Licznik [Laceration] o 1</style>
514. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 십자난무
   źródło: Skills_personality-08.json :: dataList[id=1081402].levelList[level=1].name ; dataList[id=1081402].levelList[level=2].name ; dataList[id=1081402].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Crossing Dervish
   PL: Krzyżowy Derwisz
515. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [StartBattle] (가장 높은 공명 수/2)만큼 이 스킬의 공격 레벨이 증가 (최대 3, 소수점 버림)\n[WhenUse] 다음 턴에 이 슬롯이 [Aggro] 5를 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081402].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Aggro]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [StartBattle] This Skill gains Offense Level by (highest Reson./2) (max 3; rounded down)\n[WhenUse] Gain +5 [Aggro] to this Slot next turn
   PL: [StartBattle] Umiejętność ta zyskuje Wzrost Poziomu Ataku równy (najwyższy Rezonans/2) (maks. 3, zaokrąglone w dół)\n[WhenUse] Zwiększa [Aggro] tego slotu o 5 w następnej turze
516. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Laceration]
518. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">대상의 [Combustion]과 [Laceration]의 합이 6 이상이면, 코인 위력 +1</style>\n[StartBattle] (가장 높은 공명 수/2)만큼 이 스킬의 공격 레벨이 증가 (최대 3, 소수점 버림)\n[WhenUse] 다음 턴에 이 슬롯이 [Aggro] 5를 얻음\n<style="highlight">[WhenUse] 자신에게 [HeatingWireIshmael]이 있으면, 1, 2 코인 적중시 스킬에서 기본으로 부여하는 [Laceration] 만큼 [Combustion] 부여</style>
   źródło: Skills_personality-08.json :: dataList[id=1081402].levelList[level=2].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [Laceration], [StartBattle], [WhenUse], [Aggro], [HeatingWireIshmael]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [HeatingWireIshmael] = 열선 / Thermal Blades
   EN: <style="highlight">If target has 6+ ([Combustion] + [Laceration]), Coin Power +1</style>\n[StartBattle] This Skill gains Offense Level by (highest Reson. / 2) (max 3; rounded down)\n[WhenUse] Gain +5 [Aggro] to this Slot next turn\n<style="highlight">[WhenUse] If this unit has [HeatingWireIshmael], On Hit with 1st and 2nd Coins, inflict [Combustion] by the base amount of [Laceration] the Skill inflicts</style>
   PL: <style="highlight">Przy 6+ (suma [Combustion] i [Laceration] celu) Moc Monet +1</style>\n[StartBattle] Umiejętność ta zyskuje Wzrost Poziomu Ataku równy (najwyższy Rezonans/2) (maks. 3, zaokrąglone w dół)\n[WhenUse] Zwiększa [Aggro] tego slotu o 5 w następnej turze\n<style="highlight">[WhenUse] Jeżeli ma [HeatingWireIshmael], przy trafieniach monetami 1 i 2 nakłada [Combustion] równy bazowej wartości [Laceration] nakładanej tą Umiejętnością</style>
519. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081402].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 1<style="highlight"></style>
521. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 추가 타격 피해 5</style>
   źródło: Skills_personality-08.json :: dataList[id=1081402].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 509 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Combustion]과 [Laceration]의 합이 6 이상이면, 코인 위력 +1\n[StartBattle] (가장 높은 공명 수/2)만큼 이 스킬의 공격 레벨이 증가 (최대 3, 소수점 버림)\n<style="highlight">- 해당 공명에 완전 공명이 포함되어 있으면, 위 효과로 증가한 값이 2배로 적용</style>\n[WhenUse] 다음 턴에 이 슬롯이 [Aggro] 5를 얻음\n[WhenUse] 자신에게 [HeatingWireIshmael]이 있으면, 1, 2 코인 적중시 스킬에서 기본으로 부여하는 [Laceration] 만큼 [Combustion] 부여
   źródło: Skills_personality-08.json :: dataList[id=1081402].levelList[level=4].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [Laceration], [StartBattle], [WhenUse], [Aggro], [HeatingWireIshmael]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro; [HeatingWireIshmael] = 열선 / Thermal Blades
   EN: If target has 6+ ([Combustion] + [Laceration]), Coin Power +1\n[StartBattle] This Skill gains Offense Level by (highest Reson. / 2) (max 3; rounded down)\n<style="highlight">- If there was an A-Reson. in the Reson. chain, double the amount of Offense Level gained from the above effect</style>\n[WhenUse] Gain +5 [Aggro] to this Slot next turn\n[WhenUse] If this unit has [HeatingWireIshmael], On Hit with 1st and 2nd Coins, inflict [Combustion] by the base amount of [Laceration] the Skill inflicts
   PL: Przy 6+ (suma [Combustion] i [Laceration] celu) Moc Monet +1\n[StartBattle] Umiejętność ta zyskuje Wzrost Poziomu Ataku równy (najwyższy Rezonans/2) (maks. 3, zaokrąglone w dół)\n<style="highlight">- Jeżeli w tym Rezonansie jest Pełny Rezonans, wartość zyskana powyższym efektem jest podwojona</style>\n[WhenUse] Zwiększa [Aggro] tego slotu o 5 w następnej turze\n[WhenUse] Jeżeli ma [HeatingWireIshmael], przy trafieniach monetami 1 i 2 nakłada [Combustion] równy bazowej wartości [Laceration] nakładanej tą Umiejętnością
523. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 329 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 5<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [ReinforcedTattooIshmael]이 있으면, 다음 턴에 [Paralysis] 1, [Binding] 1 부여 (턴당 2회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081402].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ReinforcedTattooIshmael], [Paralysis], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ReinforcedTattooIshmael] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos; [Paralysis] = 마비 / Paralyze; [Binding] = 속박 / Bind
   EN: <style="highlight">[OnSucceedAttack] If this unit has [ReinforcedTattooIshmael], inflict 1 [Paralysis] and 1 [Binding] next turn (2 times per turn)</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli ma [ReinforcedTattooIshmael], nakłada w następnej turze 1 [Paralysis] i 1 [Binding] (2 razy na turę)</style>
526. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 바이올렛 브레이크 슬램
   źródło: Skills_personality-08.json :: dataList[id=1081403].levelList[level=3].name ; dataList[id=1081403].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Violet~ Breaking Slam
   PL: Fioletowe~ Rozbicie
527. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Combustion]과 [Laceration]의 합이 6 이상이면, 코인 위력 +1\n[StartBattle] (가장 높은 공명 수/2)만큼 이 스킬의 공격 레벨이 증가 (최대 3, 소수점 버림)\n[WhenUse] 자신에게 [HeatingWireIshmael]이 있으면, 1, 2, 4 코인 적중시 스킬에서 기본으로 부여하는 [Laceration] 만큼 [Combustion] 부여\n[WhenUse] 자신의 [ResentmentIshmael]이 5 이상이면, 최종 위력 +1\n[EndSkill] 자신의 [ResentmentIshmael] 전부 소모
   źródło: Skills_personality-08.json :: dataList[id=1081403].levelList[level=3].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [StartBattle], [WhenUse], [HeatingWireIshmael], [ResentmentIshmael], [EndSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [HeatingWireIshmael] = 열선 / Thermal Blades; [ResentmentIshmael] = 중지 - 원한 / The Middle - Grudge; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If target has 6+ ([Combustion] + [Laceration]), Coin Power +1\n[StartBattle] This Skill gains Offense Level by (highest Reson. / 2) (max 3; rounded down)\n[WhenUse] If this unit has [HeatingWireIshmael], On Hit with 1st, 2nd, and 4th Coins, inflict [Combustion] by the base amount of [Laceration] this Skill inflicts\n[WhenUse] At 5+ [ResentmentIshmael], Final Power +1\n[EndSkill] Consume all [ResentmentIshmael] on self
   PL: Przy 6+ (suma [Combustion] i [Laceration] celu) Moc Monet +1\n[StartBattle] Umiejętność ta zyskuje Wzrost Poziomu Ataku równy (najwyższy Rezonans/2) (maks. 3, zaokrąglone w dół)\n[WhenUse] Jeżeli ma [HeatingWireIshmael], przy trafieniach monetami 1, 2 i 4 nakłada [Combustion] równy bazowej wartości [Laceration] nakładanej tą Umiejętnością\n[WhenUse] Przy 5+ [ResentmentIshmael] Moc Końcowa +1\n[EndSkill] Zużywa całe [ResentmentIshmael]
528. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081403].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081403].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 517 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 (질투 공명 수 x 5)% 만큼 추가 참격 피해 (최대 30%)
   źródło: Skills_personality-08.json :: dataList[id=1081403].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal (Envy Reson. x 5)% of this Coin's final damage as Slash bonus damage (max 30%)
   PL: [OnSucceedAttack] Zadaje dodatkowe obrażenia Sieczne równe (Rezonans Zazdrości x 5)% końcowych obrażeń tej monety (maks. 30%)
531. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081403].levelList[level=3].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Combustion]과 [Laceration]의 합이 6 이상이면, 코인 위력 +1\n[StartBattle] (가장 높은 공명 수/2)만큼 이 스킬의 공격 레벨이 증가 (최대3, 소수점 버림)\n<style="highlight">- 해당 공명에 완전 공명이 포함되어 있으면, 위 효과로 증가한 값이 2배로 적용</style>\n[WhenUse] 자신에게 [HeatingWireIshmael]이 있으면, 1, 2, 4 코인 적중시 스킬에서 기본으로 부여하는 [Laceration] 만큼 [Combustion] 부여\n[WhenUse] 자신의 [ResentmentIshmael] 5<style="highlight">당 최종 위력 +1 (최대 3)</style>\n[EndSkill] 자신의 [ResentmentIshmael] 전부 소모\n<style="highlight">[EndSkill] 이 스킬을 반격 스킬로 발동했으면, 다음 턴에 [HitDamageUp] 1 얻음 (턴당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081403].levelList[level=4].desc
   limit: do 830 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [Laceration], [StartBattle], [WhenUse], [HeatingWireIshmael], [ResentmentIshmael], [EndSkill], [HitDamageUp]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [HeatingWireIshmael] = 열선 / Thermal Blades; [ResentmentIshmael] = 중지 - 원한 / The Middle - Grudge; [EndSkill] = [공격 종료시] / [Attack End]; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up
   EN: If target has 6+ ([Combustion] + [Laceration]), Coin Power +1\n[StartBattle] This Skill gains Offense Level by (highest Reson. / 2) (max 3; rounded down)\n<style="highlight">- If there was an A-Reson. in the Reson. chain, double the amount of Offense Level gained from the above effect</style>\n[WhenUse] If this unit has [HeatingWireIshmael], On Hit with 1st, 2nd, and 4th Coins, inflict [Combustion] by the base amount of [Laceration] this Skill inflicts\n[WhenUse] <style="highlight">Final Power +1 for every 5 [ResentmentIshmael] on self (max 3)</style>\n[EndSkill] Consume all [ResentmentIshmael] on self\n<style="highlight">[EndSkill] If this Skill was activated as a Counter Skill, gain 1 [HitDamageUp] next turn (once per turn)</style>
   PL: Przy 6+ (suma [Combustion] i [Laceration] celu) Moc Monet +1\n[StartBattle] Umiejętność ta zyskuje Wzrost Poziomu Ataku równy (najwyższy Rezonans/2) (maks. 3, zaokrąglone w dół)\n<style="highlight">- Jeżeli w tym Rezonansie jest Pełny Rezonans, wartość zyskana powyższym efektem jest podwojona</style>\n[WhenUse] Jeżeli ma [HeatingWireIshmael], przy trafieniach monetami 1, 2 i 4 nakłada [Combustion] równy bazowej wartości [Laceration] nakładanej tą Umiejętnością\n[WhenUse] Moc Końcowa +1 za każde 5 [ResentmentIshmael]<style="highlight"> (maks. 3)</style>\n[EndSkill] Zużywa całe [ResentmentIshmael]\n<style="highlight">[EndSkill] Jeżeli ta Umiejętność została użyta jako Kontra, zyskuje 1 [HitDamageUp] w następnej turze (1 raz na turę)</style>
533. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-08.json :: dataList[id=1081403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o <style="highlight">2</style>
535. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 (질투 공명 수 x 5)% 만큼 추가 참격 피해 (최대 30%)<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081403].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal (Envy Reson. x 5)% of this Coin's final damage as Slash bonus damage (max 30%)<style="highlight"></style>
   PL: [OnSucceedAttack] Zadaje dodatkowe obrażenia Sieczne równe (Rezonans Zazdrości x 5)% końcowych obrażeń tej monety (maks. 30%)<style="highlight"></style>
536. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081403].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 328 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Obrona (ulepszenia 1,4) — nazwa] 가만 안둬요
   źródło: Skills_personality-08.json :: dataList[id=1081404].levelList[level=1].name ; dataList[id=1081404].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 4 · monety: 2 (+5)
   limit: do 50 znaków
   EN: I'll Get You Back for This, Man
   PL: Tego wam nie odpuszczę
538. [Obrona (ulepszenie 1) — opis] [StartBattle] 잃은 체력의 25%만큼 보호막을 얻음 (턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 25% of missing HP as Shield (once per turn)
   PL: [StartBattle] Zyskuje Tarczę równą 25% brakującego HP (1 raz na turę)
539. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 6 회복
   źródło: Skills_personality-08.json :: dataList[id=1081404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 6
   PL: [OnSucceedAttack] Obniża Próg Oszołomienia o 6
540. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Obrona (ulepszenie 4) — opis] <style="highlight">[StartBattle] 질투 완전 공명 수의 합이 6 이상이면, 반격 시 ‘바이올렛 브레이크 슬램’ 사용함\n(조작 패널의 왼쪽 슬롯부터 발동. 턴당 최대 2회 발동)</style>\n[StartBattle] 잃은 체력의 25%만큼 보호막을 얻음 (턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081404].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: <style="highlight">[StartBattle] At 6+ sum of Envy A-Reson., use 'Violet~ Breaking Slam' as Counter\n(Activates from the leftmost Skill Slot. Activates 2 times per turn)</style>\n[StartBattle] Gain 25% of missing HP as Shield (once per turn)
   PL: <style="highlight">[StartBattle] Przy 6+ sumie Pełnych Rezonansów Zazdrości odpowiada Kontrą „Fioletowe~ Rozbicie”\n(uruchamia od najbardziej lewego slotu na panelu; maks. 2 razy na turę)</style>\n[StartBattle] Zyskuje Tarczę równą 25% brakującego HP (1 raz na turę)
542. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 6 회복<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081404].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 6<style="highlight"></style>
   PL: [OnSucceedAttack] Obniża Próg Oszołomienia o 6<style="highlight"></style>
543. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081404].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 328 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Pasywka bojowa (od ulepszenia 2) — nazwa] 열선 무기
   źródło: Passives.json :: dataList[id=1081402].name
   limit: do 40 znaków
   EN: Thermal Weapon
   PL: Broń Termiczna
545. [Pasywka bojowa (od ulepszenia 2) — opis] 이 인격은 [Combustion], [Laceration]을 부여하는 인격으로 취급됨.\n[HeatingWireIshmael] 효과를 보유하고 있을 시, [Laceration]을 부여하는 스킬이 이 효과로 인해서 [Combustion]과 [Laceration]을 부여하는 스킬로 취급됨.
   źródło: Passives.json :: dataList[id=1081402].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [HeatingWireIshmael]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [HeatingWireIshmael] = 열선 / Thermal Blades
   EN: This unit is considered as an "Identity that inflicts [Combustion] and [Laceration]"\nIf this unit has [HeatingWireIshmael], Skills that inflict [Laceration] are considered as Skills that inflict both [Combustion] and [Laceration]
   PL: Ta Tożsamość traktowana jest jako Tożsamość nakładająca [Combustion] i [Laceration].\nPrzy posiadaniu efektu [HeatingWireIshmael], Umiejętności nakładające [Laceration] traktowane są jako nakładające zarówno [Combustion], jak i [Laceration].
546. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 중지는 잊지 않는다구요
   źródło: Passives.json :: dataList[id=1081401].name
   limit: do 50 znaków
   EN: The Middle Never Forgets, Y'know?
   PL: Środkowy nigdy nie zapomina
547. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 턴 종료시 해당 턴에 아군에게 스킬로 가장 많이 피해를 준 적 1명에게 [RetaliationBook]을 부여\n\n자신이 적에게 피격당할 때마다, [ResentmentIshmael] 2 얻음 (턴당 2회)\n자신을 제외한 중지 소속 아군이 적에게 피격당할 때마다, [ResentmentIshmael] 1 얻음 (인격 별로 턴당 1회)\n\n자신이 [ResentmentIshmael]을 5 소모할 때마다 [ReinforcedTattooIshmael] 1 얻음 (턴당 2회)\n\n전투 시작시 자신에게 [HeatingWireIshmael]이 없으면, 질투 공명 수의 합이 3 이상일 때, 다음 턴에 [HeatingWireIshmael] 2 얻음\n전투 시작시 자신에게 [HeatingWireIshmael]이 있으면, 턴 종료시 (질투 공명 수 / 3)만큼 [HeatingWireIshmael] 얻음 (최대 2)
   źródło: Passives.json :: dataList[id=1081401].desc
   limit: do 820 znaków
   tokeny: zachowaj dokładnie: \n, [RetaliationBook], [ResentmentIshmael], [ReinforcedTattooIshmael], [HeatingWireIshmael]
   znaczenie tagów: [RetaliationBook] = 앙갚음 대상 / Vengeance Mark; [ResentmentIshmael] = 중지 - 원한 / The Middle - Grudge; [ReinforcedTattooIshmael] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos; [HeatingWireIshmael] = 열선 / Thermal Blades
   EN: Turn End: Inflict [RetaliationBook] to the enemy that dealt the most Skill damage to an ally this turn\n\nEvery time this unit is hit by an enemy, gain 2 [ResentmentIshmael] (2 times per turn)\nWhen another The Middle-faction ally is hit by an enemy, gain 1 [ResentmentIshmael] (once per turn per Identity)\n\nGain 1 [ReinforcedTattooIshmael] every time this unit consumes 5 [ResentmentIshmael] (2 times per turn)\n\nCombat Start: If this unit does not have [HeatingWireIshmael], and at 3+ Envy Reson., gain 2 [HeatingWireIshmael] next turn\nCombat Start: If this unit has [HeatingWireIshmael], gain (Envy Reson. / 3) [HeatingWireIshmael] at Turn End (max 2)
   PL: Na koniec tury nakłada [RetaliationBook] na wroga, który w tej turze zadał sojusznikom najwięcej obrażeń Umiejętnościami\n\nZa każdym razem, gdy ta jednostka zostaje trafiona przez wroga, zyskuje 2 [ResentmentIshmael] (2 razy na turę)\nZa każdym razem, gdy sojusznik frakcji Środkowego (poza tą jednostką) zostaje trafiony przez wroga, zyskuje 1 [ResentmentIshmael] (1 raz na turę na Tożsamość)\n\nZa każde zużycie 5 [ResentmentIshmael] zyskuje 1 [ReinforcedTattooIshmael] (2 razy na turę)\n\nNa początku walki, jeżeli nie ma [HeatingWireIshmael], przy 3+ sumie Rezonansów Zazdrości zyskuje 2 [HeatingWireIshmael] w następnej turze\nNa początku walki, jeżeli ma [HeatingWireIshmael], na koniec tury zyskuje [HeatingWireIshmael] równy wartości (suma Rezonansów Zazdrości / 3) (maks. 2)
548. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — nazwa] 중지는 잊지 않는다구요
   źródło: Passives.json :: dataList[id=1081411].name
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — opis] 턴 종료시 해당 턴에 아군에게 스킬로 가장 많이 피해를 준 적 1명에게 [RetaliationBook]을 부여\n\n자신이 적에게 피격당할 때마다, [ResentmentIshmael] 2 얻음 (턴당 2회)\n자신을 제외한 중지 소속 아군이 적에게 피격당할 때마다, [ResentmentIshmael] 1 얻음 (인격 별로 턴당 1회)\n<style="highlight">- 자신이나 아군을 공격한 대상이 [RetaliationBook]이면, 추가로 1 얻음\n- 전투 시작시 질투 완전 공명이 있으면, 이번 턴에 [ResentmentIshmael]을 2배로 얻음</style>\n\n자신이 [ResentmentIshmael]을 5 소모할 때마다 [ReinforcedTattooIshmael] 1 얻음 (턴당 2회)\n\n전투 시작시 자신에게 [HeatingWireIshmael]이 없으면, 질투 공명 수의 합이 3 이상일 때, 다음 턴에 [HeatingWireIshmael] 2 얻음\n전투 시작시 자신에게 [HeatingWireIshmael]이 있으면, 턴 종료시 (질투 공명 수 / 3)만큼 [HeatingWireIshmael] 얻음 (최대 2)
   źródło: Passives.json :: dataList[id=1081411].desc
   limit: do 1090 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RetaliationBook], [ResentmentIshmael], [ReinforcedTattooIshmael], [HeatingWireIshmael]
   znaczenie tagów: [RetaliationBook] = 앙갚음 대상 / Vengeance Mark; [ResentmentIshmael] = 중지 - 원한 / The Middle - Grudge; [ReinforcedTattooIshmael] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos; [HeatingWireIshmael] = 열선 / Thermal Blades
   EN: Turn End: Inflict [RetaliationBook] to the enemy that dealt the most Skill damage to an ally this turn\n\nEvery time this unit is hit by an enemy, gain 2 [ResentmentIshmael] (2 times per turn)\nWhen another The Middle-faction ally is hit by an enemy, gain 1 [ResentmentIshmael] (once per turn per Identity)\n<style="highlight">- If the target that attacked this unit or an ally has [RetaliationBook], gain 1 more [ResentmentIshmael]\n- Combat Start: If the Dashboard has Envy A-Reson., double the amount of [ResentmentIshmael] gained this turn</style>\n\nGain 1 [ReinforcedTattooIshmael] every time this unit consumes 5 [ResentmentIshmael] (2 times per turn)\n\nCombat Start: If this unit does not have [HeatingWireIshmael], and at 3+ Envy Reson., gain 2 [HeatingWireIshmael] next turn\nCombat Start: If this unit has [HeatingWireIshmael], gain (Envy Reson. / 3) [HeatingWireIshmael] at Turn End (max 2)
   PL: Na koniec tury nakłada [RetaliationBook] na wroga, który w tej turze zadał sojusznikom najwięcej obrażeń Umiejętnościami\n\nZa każdym razem, gdy ta jednostka zostaje trafiona przez wroga, zyskuje 2 [ResentmentIshmael] (2 razy na turę)\nZa każdym razem, gdy sojusznik frakcji Środkowego (poza tą jednostką) zostaje trafiony przez wroga, zyskuje 1 [ResentmentIshmael] (1 raz na turę na Tożsamość)\n<style="highlight">- Jeżeli atakujący cel ma [RetaliationBook], dodatkowo zyskuje 1 [ResentmentIshmael]\n- Na początku walki, przy Pełnym Rezonansie Zazdrości, zyskuje w tej turze 2x więcej [ResentmentIshmael]</style>\n\nZa każde zużycie 5 [ResentmentIshmael] zyskuje 1 [ReinforcedTattooIshmael] (2 razy na turę)\n\nNa początku walki, jeżeli nie ma [HeatingWireIshmael], przy 3+ sumie Rezonansów Zazdrości zyskuje 2 [HeatingWireIshmael] w następnej turze\nNa początku walki, jeżeli ma [HeatingWireIshmael], na koniec tury zyskuje [HeatingWireIshmael] równy wartości (suma Rezonansów Zazdrości / 3) (maks. 2)
550. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — nazwa] 당신… 해결사 좋아해요?
   źródło: Passives.json :: dataList[id=1081421].name
   limit: do 50 znaków
   EN: Hey, Are Ya Into Fixers, Too?
   PL: Hej, to ty lubisz Fikserów?
551. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — opis] 편성 순서 1번의 기본 공격 스킬의 합 위력 +1 (턴당 1회)\n질투 공명이 완전 공명이면, 편성 순서 1번의 기본 스킬 피해량 +10%
   źródło: Passives.json :: dataList[id=1081421].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clash Power +1 for #1 Deployed Identity's Base Attack Skills (once per turn)\nIf the Dashboard has Envy A-Reson., #1 Deployed Identity deals +10% damage with Base Skills
   PL: Moc Starcia +1 podstawowych Umiejętności ataku Tożsamości przydzielonej na 1. pozycji (1 raz na turę)\nPrzy Pełnym Rezonansie Zazdrości, podstawowe Umiejętności Tożsamości przydzielonej na 1. pozycji zadają +10% obrażeń
552. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — podsumowanie] 기본 공격 스킬의 합 위력 +1\n질투 완전 공명이면, 기본 스킬 피해량 +10%
   źródło: Passives.json :: dataList[id=1081421].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clash Power +1 for Base Attack Skills\nIf the Dashboard has Envy A-Reson., deal +10% damage with Base Skills
   PL: Moc Starcia +1 podstawowych Umiejętności ataku\nPrzy Pełnym Rezonansie Zazdrości podstawowe Umiejętności zadają +10% obrażeń

## [000] LCD OSIR Team — Ishmael — LCD 현장추리팀
- ID Tożsamości: `10815` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 7 · HP bazowe: 85 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Poise

553. [Karta Tożsamości — tytuł] LCD\n현장추리팀
   źródło: Personalities.json :: dataList[id=10815].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCD OSIR Team
   PL: LCD\nZespół Śledczy OSIR
554. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10815].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10815].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Karta Tożsamości — opis] 이스마엘의 열다섯번째 인격
   źródło: Personalities.json :: dataList[id=10815].desc
   limit: do 120 znaków
   EN: Ishmael's 15th Identity
   PL: Piętnasta Tożsamość Ishmael
557. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 세법
   źródło: Skills_personality-08.json :: dataList[id=1081501].levelList[level=1].name ; dataList[id=1081501].levelList[level=2].name ; dataList[id=1081501].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Rending Arts
   PL: Sztuka Rozdzierania
558. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가\n[EndSkill] 자신에게 [Agility]이 있다면, [WindBladeIshmael] 1 얻음 (턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081501].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [EndSkill], [Agility], [WindBladeIshmael]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [Agility] = 신속 / Haste; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: [WhenUse] Gain +2 [Breath] Count\n[EndSkill] If this unit has [Agility], gain 1 [WindBladeIshmael] (once per turn)
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2\n[EndSkill] Jeżeli ma [Agility], zyskuje 1 [WindBladeIshmael] (1 raz na turę)
559. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081501].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081501].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081501].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL: [OnSucceedAttack] Zyskuje 1 [Breath]
561. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081501].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1081501].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1081501].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Agility]이 3 이상이면, 합 위력 +1</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[EndSkill] 자신에게 [Agility]이 있다면, [WindBladeIshmael] 1 얻음 (턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081501].levelList[level=2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Agility], [Breath], [EndSkill], [WindBladeIshmael]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: <style="highlight">[WhenUse] At 3+ [Agility], Clash Power +1</style>\n[WhenUse] Gain +2 [Breath] Count\n[EndSkill] If this unit has [Agility], gain 1 [WindBladeIshmael] (once per turn)
   PL: <style="highlight">[WhenUse] Przy 3+ [Agility] Moc Starcia +1</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2\n[EndSkill] Jeżeli ma [Agility], zyskuje 1 [WindBladeIshmael] (1 raz na turę)
563. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 자신의 [Breath]이 5 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration] 5당, 합 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Agility]이 3 이상이면, 합 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[EndSkill] 자신에게 [Agility]이 있다면, [WindBladeIshmael] 1 얻음 (턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081501].levelList[level=4].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Laceration], [Agility], [EndSkill], [WindBladeIshmael]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [Agility] = 신속 / Haste; [EndSkill] = [공격 종료시] / [Attack End]; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: <style="highlight">[WhenUse] At 5+ [Breath], Coin Power +1\n[WhenUse] Clash Power +1 for every 5 [Laceration] on target (max 2)</style>\n[WhenUse] At 3+ [Agility], Clash Power +1\n[WhenUse] Gain +2 [Breath] Count\n[EndSkill] If this unit has [Agility], gain 1 [WindBladeIshmael] (once per turn)
   PL: <style="highlight">[WhenUse] Przy 5+ [Breath] Moc Monet +1\n[WhenUse] Moc Starcia +1 za każde 5 [Laceration] celu (maks. 2)</style>\n[WhenUse] Przy 3+ [Agility] Moc Starcia +1\n[WhenUse] Zwiększa własny Licznik [Breath] o 2\n[EndSkill] Jeżeli ma [Agility], zyskuje 1 [WindBladeIshmael] (1 raz na turę)
564. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 3 — opis] <style="highlight">[OnSucceedAttack] [AengduNewArmIshmael]을 보유한 상태로 자신의 [Agility]이 3 이상이면, 이 코인 재사용 (턴당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081501].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [AengduNewArmIshmael], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AengduNewArmIshmael] = 도깨비팔 / Dokkaebi Arms; [Agility] = 신속 / Haste
   EN: <style="highlight">[OnSucceedAttack] If this unit has [AengduNewArmIshmael] and 3+ [Agility], Reuse this Coin (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli ma [AengduNewArmIshmael] i 3+ [Agility], ponownie używa tej monety (1 raz na turę)</style>
565. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 자법
   źródło: Skills_personality-08.json :: dataList[id=1081502].levelList[level=1].name ; dataList[id=1081502].levelList[level=2].name ; dataList[id=1081502].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 3 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Acupuncture
   PL: Akupunktura
566. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 3 증가\n[EndSkill] 자신의 [Agility] 1당, [WindBladeIshmael] 1 얻음 (최대 2, 턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081502].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [EndSkill], [Agility], [WindBladeIshmael]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [Agility] = 신속 / Haste; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: [WhenUse] Gain +3 [Breath] Count\n[EndSkill] Gain 1 [WindBladeIshmael] for every [Agility] on self (max 2, once per turn)
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 3\n[EndSkill] Zyskuje 1 [WindBladeIshmael] za każdą 1 [Agility] (maks. 2, 1 raz na turę)
567. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081502].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081502].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1081502].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1081502].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081502].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081502].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1081502].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1081502].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-08.json :: dataList[id=1081502].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1081502].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1081502].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 517 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [Agility] 2 얻음 (턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081502].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1081502].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Agility]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Agility] = 신속 / Haste
   EN: [CriticalOnSucceedAttack] Gain 2 [Agility] next turn (once per turn)
   PL: [CriticalOnSucceedAttack] Zyskuje 2 [Agility] w następnej turze (1 raz na turę)
573. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Agility]이 3 이상이면, 합 위력 +2</style>\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n[EndSkill] 자신의 [Agility] 1당, [WindBladeIshmael] 1 얻음 (최대 2, 턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081502].levelList[level=2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Agility], [Breath], [EndSkill], [WindBladeIshmael]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: <style="highlight">[WhenUse] At 3+ [Agility], Clash Power +2</style>\n[WhenUse] Gain +3 [Breath] Count\n[EndSkill] Gain 1 [WindBladeIshmael] for every [Agility] on self (max 2, once per turn)
   PL: <style="highlight">[WhenUse] Przy 3+ [Agility] Moc Starcia +2</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 3\n[EndSkill] Zyskuje 1 [WindBladeIshmael] za każdą 1 [Agility] (maks. 2, 1 raz na turę)
574. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 자신의 [Breath]이 5 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration] 5당, 합 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Agility]이 3 이상이면, 합 위력 +2\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n[EndSkill] 자신의 [Agility] 1당, [WindBladeIshmael] 1 얻음 (최대 2, 턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081502].levelList[level=4].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Laceration], [Agility], [EndSkill], [WindBladeIshmael]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [Agility] = 신속 / Haste; [EndSkill] = [공격 종료시] / [Attack End]; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: <style="highlight">[WhenUse] At 5+ [Breath], Coin Power +1\n[WhenUse] Clash Power +1 for every 5 [Laceration] on target (max 2)</style>\n[WhenUse] At 3+ [Agility], Clash Power +2\n[WhenUse] Gain +3 [Breath] Count\n[EndSkill] Gain 1 [WindBladeIshmael] for every [Agility] on self (max 2, once per turn)
   PL: <style="highlight">[WhenUse] Przy 5+ [Breath] Moc Monet +1\n[WhenUse] Moc Starcia +1 za każde 5 [Laceration] celu (maks. 2)</style>\n[WhenUse] Przy 3+ [Agility] Moc Starcia +2\n[WhenUse] Zwiększa własny Licznik [Breath] o 3\n[EndSkill] Zyskuje 1 [WindBladeIshmael] za każdą 1 [Agility] (maks. 2, 1 raz na turę)
575. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [AengduNewArmIshmael]을 보유한 상태로 자신의 [Agility]이 3 이상이면, 이 코인 재사용 (턴당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081502].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] 다음 턴에 [Agility] 2 얻음 (턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081502].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 572 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Umiejętność 3 (×1) (ulepszenia 1,4) — nazwa] 청린화
   źródło: Skills_personality-08.json :: dataList[id=1081503].levelList[level=1].name ; dataList[id=1081503].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Lucent Rippling Flame
   PL: Błękitny Falujący Płomień
578. [Umiejętność 3 (×1) (ulepszenie 1) — opis] 자신의 [Breath] 1당, 크리티컬 피해량 +1.5% (최대 30%)\n[WhenUse] 자신의 [Agility] 2당, 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [WindBladeIshmael] 수치가 10 이상이면, 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] [Breath] 3 얻음\n[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴당 1회)\n[EndSkill] 자신의 [Agility] 1당, [WindBladeIshmael] 1 얻음 (최대 3, 턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081503].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [WhenUse], [Agility], [WindBladeIshmael], [SuperCoin], [EndSkill]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +1.5% damage on Critical Hit for every [Breath] on self (max 30%)\n[WhenUse] Final Power +1 for every 2 [Agility] on self (max 2)\n[WhenUse] At 10+ [WindBladeIshmael], convert all Coins into [SuperCoin]s\n[WhenUse] Gain 3 [Breath]\n[WhenUse] Gain 2 [Agility] next turn (once per turn)\n[EndSkill] Gain 1 [WindBladeIshmael] for every [Agility] on self (max 3, once per turn)
   PL: Zadaje +1.5% obrażeń przy trafieniu krytycznym za każde 1 [Breath] (maks. 30%)\n[WhenUse] Moc Końcowa +1 za każde 2 [Agility] (maks. 2)\n[WhenUse] Przy 10+ stosach [WindBladeIshmael] wszystkie monety stają się [SuperCoin]ami\n[WhenUse] Zyskuje 3 [Breath]\n[WhenUse] Zyskuje 2 [Agility] w następnej turze (1 raz na turę)\n[EndSkill] Zyskuje 1 [WindBladeIshmael] za każdą 1 [Agility] (maks. 3, 1 raz na turę)
579. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_personality-08.json :: dataList[id=1081503].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +3 [Breath] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Breath] o 3
580. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081503].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 3, efekt 1 — opis] 자신의 [WindBladeIshmael] 수치 1당, 크리티컬 피해량 +2% (최대 20%)
   źródło: Skills_personality-08.json :: dataList[id=1081503].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1081503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WindBladeIshmael]
   znaczenie tagów: [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: Deal +2% damage on Critical Hit for every [WindBladeIshmael] on self (max 20%)
   PL: Zadaje +2% obrażeń przy trafieniu krytycznym za każdy 1 stos [WindBladeIshmael] (maks. 20%)
582. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081503].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1081503].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [SlashTakeDamageUp] 1 부여 (턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081503].levelList[level=1].coinlist[#2].coindescs[#2].desc ; dataList[id=1081503].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttack] Inflict 1 [SlashTakeDamageUp] (once per turn)
   PL: [OnSucceedAttack] Nakłada 1 [SlashTakeDamageUp] (1 raz na turę)
584. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 [Breath] 1당, 크리티컬 피해량 +1.5% (최대 30%)\n[WhenUse] 자신의 [Agility] 2당, 최종 위력 +1 (최대 2)\n<style="highlight">[WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6 당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [WindBladeIshmael] 수치가 10 이상이면, 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] [Breath] 3 얻음\n[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴당 1회)\n[EndSkill] 자신의 [Agility] 1당, [WindBladeIshmael] 1 얻음 (최대 3, 턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081503].levelList[level=4].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [WhenUse], [Agility], [Laceration], [WindBladeIshmael], [SuperCoin], [EndSkill]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [Laceration] = 출혈 / Bleed; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +1.5% damage on Critical Hit for every [Breath] on self (max 30%)\n[WhenUse] Final Power +1 for every 2 [Agility] on self (max 2)\n<style="highlight">[WhenUse] Coin Power +1 for every 6 ([Breath] on self + [Laceration] on target) (max 2)</style>\n[WhenUse] At 10+ [WindBladeIshmael], convert all Coins into [SuperCoin]s\n[WhenUse] Gain 3 [Breath]\n[WhenUse] Gain 2 [Agility] next turn (once per turn)\n[EndSkill] Gain 1 [WindBladeIshmael] for every [Agility] on self (max 3, once per turn)
   PL: Zadaje +1.5% obrażeń przy trafieniu krytycznym za każde 1 [Breath] (maks. 30%)\n[WhenUse] Moc Końcowa +1 za każde 2 [Agility] (maks. 2)\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 (suma własnego [Breath] i [Laceration] celu) (maks. 2)</style>\n[WhenUse] Przy 10+ stosach [WindBladeIshmael] wszystkie monety stają się [SuperCoin]ami\n[WhenUse] Zyskuje 3 [Breath]\n[WhenUse] Zyskuje 2 [Agility] w następnej turze (1 raz na turę)\n[EndSkill] Zyskuje 1 [WindBladeIshmael] za każdą 1 [Agility] (maks. 3, 1 raz na turę)
585. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] [WindBladeIshmael] 1 얻음</style>
   źródło: Skills_personality-08.json :: dataList[id=1081503].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [WindBladeIshmael]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: <style="highlight">[CriticalOnSucceedAttack] Gain 1 [WindBladeIshmael]</style>
   PL: <style="highlight">[CriticalOnSucceedAttack] Zyskuje 1 [WindBladeIshmael]</style>
586. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] [WindBladeIshmael] 1 얻음</style>
   źródło: Skills_personality-08.json :: dataList[id=1081503].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] <style="highlight">[CriticalOnSucceedAttack] [WindBladeIshmael] 1 얻음</style>
   źródło: Skills_personality-08.json :: dataList[id=1081503].levelList[level=4].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — nazwa] 골단
   źródło: Skills_personality-08.json :: dataList[id=1081505].levelList[level=1].name ; dataList[id=1081505].levelList[level=2].name ; dataList[id=1081505].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: To Claim Their Bones
   PL: Łamanie Kości
589. [Umiejętność 4 (×0) (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않음\n자신의 잃은 체력 1%당 피해량 +0.5% (최대 20%)\n자신의 [Agility] 1당, 크리티컬 피해량 +3% (최대 15%)
   źródło: Skills_personality-08.json :: dataList[id=1081505].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [Agility]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [Agility] = 신속 / Haste
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills\nDeal +0.5% damage for every 1% missing HP on self (max 20%)\nDeal +3% damage on Critical Hit for every [Agility] on self (max 15%)
   PL: [CantDuel]\nTa Umiejętność nie uruchamia Umiejętności obrony\nZadaje +0.5% obrażeń za każde 1% brakującego HP (maks. 20%)\nZadaje +3% obrażeń przy trafieniu krytycznym za każdą 1 [Agility] (maks. 15%)
590. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081505].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081505].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1081505].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL: [OnSucceedAttack] Zyskuje 3 [Breath]
591. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [SlashTakeDamageUp] 1 부여 (턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081505].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1081505].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1081505].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081505].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081505].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081505].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Umiejętność 4 (×0) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081505].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1081505].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1081505].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 1 [Paralysis] next turn
   PL: [OnSucceedAttack] Nakłada 1 [Paralysis] w następnej turze
594. [Umiejętność 4 (×0) (ulepszenie 2) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않음\n자신의 잃은 체력 1%당 피해량 +0.5% (최대 20%)\n자신의 [Agility] 1당, 크리티컬 피해량 +3% (최대 15%)\n<style="highlight">[WhenUse] 자신의 [WindBladeIshmael] 수치 1당, 피해량 +1% (최대 15%)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081505].levelList[level=2].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [Agility], [WhenUse], [WindBladeIshmael]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [Agility] = 신속 / Haste; [WhenUse] = [사용시] / [On Use]; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills\nDeal +0.5% damage for every 1% missing HP on self (max 20%)\nDeal +3% damage on Critical Hit for every [Agility] on self (max 15%)\n<style="highlight">[WhenUse] Deal +1% damage for every [WindBladeIshmael] on self (max 15%)</style>
   PL: [CantDuel]\nTa Umiejętność nie uruchamia Umiejętności obrony\nZadaje +0.5% obrażeń za każde 1% brakującego HP (maks. 20%)\nZadaje +3% obrażeń przy trafieniu krytycznym za każdą 1 [Agility] (maks. 15%)\n<style="highlight">[WhenUse] Zadaje +1% obrażeń za każdy 1 stos [WindBladeIshmael] (maks. 15%)</style>
595. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않음\n자신의 잃은 체력 1%당 피해량 +0.5% (최대 20%)\n자신의 [Agility] 1당, 크리티컬 피해량 +3% (최대 15%)\n[WhenUse] 자신의 [WindBladeIshmael] 수치 1당, 피해량 +1% (최대 15%)\n<style="highlight">[WhenUse] 자신의 [Breath] 1당, 크리티컬 피해량 +1.5% (최대 30%)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081505].levelList[level=4].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [Agility], [WhenUse], [WindBladeIshmael], [Breath]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [Agility] = 신속 / Haste; [WhenUse] = [사용시] / [On Use]; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire; [Breath] = 호흡 / Poise
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills\nDeal +0.5% damage for every 1% missing HP on self (max 20%)\nDeal +3% damage on Critical Hit for every [Agility] on self (max 15%)\n[WhenUse] Deal +1% damage for every [WindBladeIshmael] on self (max 15%)\n<style="highlight">[WhenUse] Deal +1.5% damage on Critical Hit for every [Breath] on self (max 30%)</style>
   PL: [CantDuel]\nTa Umiejętność nie uruchamia Umiejętności obrony\nZadaje +0.5% obrażeń za każde 1% brakującego HP (maks. 20%)\nZadaje +3% obrażeń przy trafieniu krytycznym za każdą 1 [Agility] (maks. 15%)\n[WhenUse] Zadaje +1% obrażeń za każdy 1 stos [WindBladeIshmael] (maks. 15%)\n<style="highlight">[WhenUse] Zadaje +1.5% obrażeń przy trafieniu krytycznym za każde 1 [Breath] (maks. 30%)</style>
596. [Umiejętność 5 (×0) (ulepszenia 1,4) — nazwa] 상전 청린화
   źródło: Skills_personality-08.json :: dataList[id=1081506].levelList[level=1].name ; dataList[id=1081506].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 5 · monety: 4 (+3)
   limit: do 60 znaków
   EN: Even the Balance - Lucent Rippling Flame
   PL: Rozliczenie - Błękitny Falujący Płomień
597. [Umiejętność 5 (×0) (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않음\n자신의 [Breath] 1당, 크리티컬 피해량 +1.5% (최대 30%)\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n[EndSkill] 자신의 [WindBladeIshmael] 모두 소모
   źródło: Skills_personality-08.json :: dataList[id=1081506].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [Breath], [WhenUse], [EndSkill], [WindBladeIshmael]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills\nDeal +1.5% damage on Critical Hit for every [Breath] on self (max 30%)\n[WhenUse] Gain +3 [Breath] Count\n[EndSkill] Consume all [WindBladeIshmael] on self
   PL: [CantDuel]\nTa Umiejętność nie uruchamia Umiejętności obrony\nZadaje +1.5% obrażeń przy trafieniu krytycznym za każde 1 [Breath] (maks. 30%)\n[WhenUse] Zwiększa własny Licznik [Breath] o 3\n[EndSkill] Zużywa całe [WindBladeIshmael]
598. [Umiejętność 5 (×0) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081506].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081506].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 590 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Umiejętność 5 (×0) (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081506].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081506].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Umiejętność 5 (×0) (ulepszenia 1,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081506].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1081506].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Umiejętność 5 (×0) (ulepszenia 1,4) — moneta 4, efekt 1 — opis] 자신의 [WindBladeIshmael] 수치가 15를 초과했으면, 초과된 수치 1당, 크리티컬 피해량 +5% (최대 25%)
   źródło: Skills_personality-08.json :: dataList[id=1081506].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=1081506].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WindBladeIshmael]
   znaczenie tagów: [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: At more than 15 [WindBladeIshmael], deal +5% damage on Critical Hit for every excess Stack (max 25%)
   PL: Ponad 15 stosów [WindBladeIshmael]: zadaje +5% obrażeń przy trafieniu krytycznym za każdy 1 nadmiarowego stosu (maks. 25%)
602. [Umiejętność 5 (×0) (ulepszenia 1,4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-08.json :: dataList[id=1081506].levelList[level=1].coinlist[#3].coindescs[#1].desc ; dataList[id=1081506].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Umiejętność 5 (×0) (ulepszenia 1,4) — moneta 4, efekt 3 — opis] [CriticalOnSucceedAttack] 자신의 [Agility]이 5 이상이면, 이 코인 재사용 (스킬당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081506].levelList[level=1].coinlist[#3].coindescs[#2].desc ; dataList[id=1081506].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Agility]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Agility] = 신속 / Haste
   EN: [CriticalOnSucceedAttack] At 5+ [Agility], Reuse this Coin (once per Skill)
   PL: [CriticalOnSucceedAttack] Przy 5+ [Agility] ponownie używa tej monety (1 raz na Umiejętność)
604. [Umiejętność 5 (×0) (ulepszenie 4) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않음\n자신의 [Breath] 1당, 크리티컬 피해량 +1.5% (최대 30%)\n<style="highlight">자신의 [Agility] 1당, 크리티컬 피해량 +5% (최대 25%)</style>\n[WhenUse] [Breath] 횟수 3 증가\n[EndSkill] 자신의 [WindBladeIshmael] 모두 소모
   źródło: Skills_personality-08.json :: dataList[id=1081506].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CantDuel], [Breath], [Agility], [WhenUse], [EndSkill], [WindBladeIshmael]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills\nDeal +1.5% damage on Critical Hit for every [Breath] on self (max 30%)\n<style="highlight">Deal +5% damage on Critical Hit for every [Agility] on self (max 25%)</style>\n[WhenUse] Gain +3 [Breath] Count\n[EndSkill] Consume all [WindBladeIshmael] on self
   PL: [CantDuel]\nTa Umiejętność nie uruchamia Umiejętności obrony\nZadaje +1.5% obrażeń przy trafieniu krytycznym za każde 1 [Breath] (maks. 30%)\n<style="highlight">Zadaje +5% obrażeń przy trafieniu krytycznym za każdą 1 [Agility] (maks. 25%)</style>\n[WhenUse] Zwiększa Licznik [Breath] o 3\n[EndSkill] Zużywa całe [WindBladeIshmael]
605. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] [WindBladeIshmael] 1 얻음</style>
   źródło: Skills_personality-08.json :: dataList[id=1081506].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] [WindBladeIshmael] 1 얻음</style>
   źródło: Skills_personality-08.json :: dataList[id=1081506].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[CriticalOnSucceedAttack] [WindBladeIshmael] 1 얻음</style>
   źródło: Skills_personality-08.json :: dataList[id=1081506].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Obrona (ulepszenia 1,4) — nazwa] 앞길을 밝힐게요
   źródło: Skills_personality-08.json :: dataList[id=1081504].levelList[level=1].name ; dataList[id=1081504].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 5 · monety: 1 (+8)
   limit: do 40 znaków
   EN: I'll Light the Path Forward
   PL: Oświetlę drogę naprzód
609. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] [SupportProtect] 1 얻음 (턴당 1회)\n[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴당 1회)\n[WhenUse] 자신의 [Breath] 횟수 2 증가 (턴당 1회)\n[WinDuel] [Breath] 3 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081504].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [SupportProtect], [WhenUse], [Agility], [Breath], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n[StartBattle] Gain 1 [SupportProtect] (once per turn)\n[WhenUse] Gain 2 [Agility] next turn (once per turn)\n[WhenUse] Gain +2 [Breath] Count (once per turn)\n[WinDuel] Gain 3 [Breath]
   PL: [CanDuelGuard]\n[StartBattle] Zyskuje 1 [SupportProtect] (1 raz na turę)\n[WhenUse] Zyskuje 2 [Agility] w następnej turze (1 raz na turę)\n[WhenUse] Zwiększa własny Licznik [Breath] o 2 (1 raz na turę)\n[WinDuel] Zyskuje 3 [Breath]
610. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-08.json :: dataList[id=1081504].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081504].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[StartBattle] [SupportProtect] 1 얻음 (턴당 1회)\n[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴당 1회)\n[WhenUse] 자신의 [Breath] 횟수 2 증가 (턴당 1회)\n[WinDuel] [Breath] 3 얻음\n<style="highlight">[EndSkillAll] 자신에게 [Agility]이 있다면, [WindBladeIshmael] 2 얻음 (턴당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081504].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [StartBattle], [SupportProtect], [WhenUse], [Agility], [Breath], [WinDuel], [EndSkillAll], [WindBladeIshmael]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkillAll] = [스킬 종료시] / [Skill End] …
   EN: [CanDuelGuard]\n[StartBattle] Gain 1 [SupportProtect] (once per turn)\n[WhenUse] Gain 2 [Agility] next turn (once per turn)\n[WhenUse] Gain +2 [Breath] Count (once per turn)\n[WinDuel] Gain 3 [Breath]\n<style="highlight">[EndSkillAll] If this unit has [Agility], gain 2 [WindBladeIshmael] (once per turn)</style>
   PL: [CanDuelGuard]\n[StartBattle] Zyskuje 1 [SupportProtect] (1 raz na turę)\n[WhenUse] Zyskuje 2 [Agility] w następnej turze (1 raz na turę)\n[WhenUse] Zwiększa własny Licznik [Breath] o 2 (1 raz na turę)\n[WinDuel] Zyskuje 3 [Breath]\n<style="highlight">[EndSkillAll] Jeżeli ma [Agility], zyskuje 2 [WindBladeIshmael] (1 raz na turę)</style>
612. [Obrona (ulepszenia 1,4) — nazwa] 형세 읽기
   źródło: Skills_personality-08.json :: dataList[id=1081507].levelList[level=1].name ; dataList[id=1081507].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 4 · monety: 1 (+9)
   limit: do 50 znaków
   EN: Observing the Stones on the Board
   PL: Czytanie Kamieni na Płycie
613. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081507].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [SupportProtect], [WhenUse], [Breath]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [CanDuelGuard]\n[SupportProtect] Exclusive Skill\n\n[WhenUse] Gain 3 [Breath]
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [SupportProtect]\n\n[WhenUse] Zyskuje 3 [Breath]
614. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-08.json :: dataList[id=1081507].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081507].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n<style="highlight">[WhenUse] [SupportProtect]로 보호[TabExplain]한 대상의 정신력 5 회복</style>\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081507].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [SupportProtect], [WhenUse], [TabExplain], [Breath]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [CanDuelGuard]\n[SupportProtect] Exclusive Skill\n<style="highlight">[WhenUse] Heal 5 SP on target this unit guarded using [SupportProtect]</style>\n[WhenUse] Gain 3 [Breath]
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [SupportProtect]\n<style="highlight">[WhenUse] Odzyskuje 5 Poczytalności dla jednostki chronionej [TabExplain] przez [SupportProtect]</style>\n[WhenUse] Zyskuje 3 [Breath]
616. [Pasywka bojowa (od ulepszenia 1) — nazwa] 귀화요격
   źródło: Passives.json :: dataList[id=1081503].name
   limit: do 40 znaków
   EN: Demonfire Spinecleaver
   PL: Przechwyt Demonognia
617. [Pasywka bojowa (od ulepszenia 1) — opis] 수비 스킬 합 패배 시 [Agility]이 3 이상이면, 수비 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않으며, 피격 후 ‘골단’ 발동 (턴당 2회, 강제 흐트러짐 제외)
   źródło: Passives.json :: dataList[id=1081503].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: On Defense Skill Clash Lose, if this unit has 3+ [Agility], this unit cannot be Staggered from taking damage until Defense Skill End, and activate "To Claim Their Bones" after being hit (2 times per turn, excluding forced Staggers)
   PL: Przy przegranej w starciu Umiejętności obrony, przy 3+ [Agility], do końca Umiejętności obrony nie może zostać Ogłuszona obrażeniami, a po trafieniu stosuje „Odbieranie Kości” (2 razy na turę, z wyłączeniem wymuszonego Ogłuszenia)
618. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 조건 만족 시 추가 스킬 발동
   źródło: Passives.json :: dataList[id=1081503].summary
   limit: do 120 znaków
   EN: Activate additional Skill when conditions are met
   PL: Uruchamia dodatkową Umiejętność przy spełnieniu warunków
619. [Pasywka bojowa (od ulepszenia 1) — nazwa] 돌아가야 할 곳
   źródło: Passives.json :: dataList[id=1081502].name
   limit: do 40 znaków
   EN: To Where I Must Return
   PL: Tam, Dokąd Muszę Wrócić
620. [Pasywka bojowa (od ulepszenia 1) — opis] 스테이지 첫 등장 시 자신을 제외한 전장에 있는 검계 소속 아군 인격의 수 1명당, [BladelineagePride] 얻음 (최대 3)\n\n이번 전투에서 자신을 제외한 검계 소속 아군 인격이 3명 이상 사망한 경우\n- 스킬 사용 전 자신에게 [SwordPlayOfTheHomeland]이 없다면, [SwordPlayOfTheHomeland] 얻음\n- 자신의 스킬, 코인 효과로 [Breath] 위력, 횟수를 얻을 때, [Breath] 위력, 횟수 1 추가 증가\n- 검계 소속 아군 인격이 5명 이상 사망한 경우, 대신 2 증가
   źródło: Passives.json :: dataList[id=1081502].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: \n, [BladelineagePride], [SwordPlayOfTheHomeland], [Breath]
   znaczenie tagów: [BladelineagePride] = 살수본위 / Bearing of a Salsu; [SwordPlayOfTheHomeland] = 본국검술 / Swordplay of the Homeland; [Breath] = 호흡 / Poise
   EN: Upon entering the Encounter for the first time, this unit gains [BladelineagePride] for every Blade Lineage Identity on the field excluding this unit (max 3)\n\nIf 3 or more Blade Lineage Identities, excluding this unit, are defeated in this Encounter:\n- Before Skill Use, if this unit did not have [SwordPlayOfTheHomeland], gain [SwordPlayOfTheHomeland]\n- When this unit gains [Breath] Potency and [Breath] Count with its Skill or Coin effects, gain 1 additional [Breath] Potency and [Breath] Count\n- If 5 or more Blade Lineage Identities are defeated, gain 2 additional [Breath] Potency and [Breath] Count instead
   PL: Przy pierwszym wejściu na pole spotkania zyskuje [BladelineagePride] za każdą 1 Tożsamość Ród Ostrza na polu (poza tą jednostką) (maks. 3)\n\nJeżeli w tym spotkaniu ginie 3 lub więcej Tożsamości Ród Ostrza (poza tą jednostką):\n- Przed użyciem Umiejętności, jeżeli nie ma [SwordPlayOfTheHomeland], zyskuje [SwordPlayOfTheHomeland]\n- Gdy zyskuje Moc lub Licznik [Breath] efektami Umiejętności albo monet, zyskuje o 1 więcej Mocy i Licznika [Breath]\n- Jeżeli ginie 5 lub więcej Tożsamości Ród Ostrza, zamiast tego zyskuje o 2 więcej Mocy i Licznika [Breath]
621. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — nazwa] 림버스 컴퍼니 제작 특수 의체 시제품 mk5 - 도깨비팔
   źródło: Passives.json :: dataList[id=1081501].name
   limit: do 100 znaków
   EN: Limbus Company Specialized Custom Prosthetic Prototype mk5 - Dokkaebi Arms
   PL: Specjalna Prototypowa Proteza mk5 Limbus Company - Ramię Dokkaebi
622. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — opis] 전투 시작 시 [AengduNewArmIshmael]을 얻으며, 자신을 제외한 검계 소속 아군 인격의 정신력을 (오만 공명 수)만큼 회복\n\n전투 시작 시 자신을 제외한 현재 체력이 최대 체력의 50% 미만인 아군 인격이 있다면, [SupportProtect] 1 얻음 (턴당 1회)\n\n스킬 종료 시 자신의 [Breath] 위력 3당, [WindBladeIshmael] 1 얻음 (최대 5, 턴당 2회)
   źródło: Passives.json :: dataList[id=1081501].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [AengduNewArmIshmael], [SupportProtect], [Breath], [WindBladeIshmael]
   znaczenie tagów: [AengduNewArmIshmael] = 도깨비팔 / Dokkaebi Arms; [SupportProtect] = 원호 방어 / Assist Defense; [Breath] = 호흡 / Poise; [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   EN: Combat Start: Gain [AengduNewArmIshmael] and heal (Pride Reson.) SP for Blade Lineage allied Identities excluding this unit\n\nCombat Start: If there is an allied Identity at less than 50% HP on the field excluding this unit, gain 1 [SupportProtect] (once per turn)\n\nSkill End: Gain 1 [WindBladeIshmael] for every 3 [Breath] Potency on self (max 5, 2 times per turn)
   PL: Na początku walki zyskuje [AengduNewArmIshmael] i odzyskuje (Rezonans Pychy) Poczytalności dla Tożsamości sojuszników Ród Ostrza (poza tą jednostką)\n\nNa początku walki, jeżeli na polu jest Tożsamość sojusznika (poza tą jednostką) z HP poniżej 50%, zyskuje 1 [SupportProtect] (1 raz na turę)\n\nNa koniec Umiejętności zyskuje 1 [WindBladeIshmael] za każde 3 Mocy [Breath] (maks. 5, 2 razy na turę)
623. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — podsumowanie] [AengduNewArmIshmael] 얻음
   źródło: Passives.json :: dataList[id=1081501].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AengduNewArmIshmael]
   znaczenie tagów: [AengduNewArmIshmael] = 도깨비팔 / Dokkaebi Arms
   EN: Gain [AengduNewArmIshmael]
   PL: Zyskuje [AengduNewArmIshmael]
624. [Pasywka bojowa (od ulepszenia 3) — nazwa] 귀화요격
   źródło: Passives.json :: dataList[id=1081513].name
   (powtórzenie elementu 616 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Pasywka bojowa (od ulepszenia 3) — opis] <style="highlight">기본 공격 스킬 종료 시 자신의 [WindBladeIshmael]이 15 이상이면, ‘상전 청린화’ 발동 (턴당 1회)</style>\n\n수비 스킬 합 패배 시 [Agility]이 3 이상이면, 수비 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않으며, 피격 후 ‘골단’ 발동 (턴당 2회, 강제 흐트러짐 제외)
   źródło: Passives.json :: dataList[id=1081513].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WindBladeIshmael], [Agility]
   znaczenie tagów: [WindBladeIshmael] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire; [Agility] = 신속 / Haste
   EN: <style="highlight">On Base Attack Skill End, if this unit has 15+ [WindBladeIshmael], activate "Even the Balance - Lucent Rippling Flame" (once per turn)</style>\n\nOn Defense Skill Clash Lose, if this unit has 3+ [Agility], this unit cannot be Staggered from taking damage until Defense Skill End, and activate "To Claim Their Bones" after being hit (2 times per turn, excluding forced Staggers)
   PL: <style="highlight">Na koniec podstawowej Umiejętności ataku, przy 15+ stosach [WindBladeIshmael], stosuje „Rozliczenie - Błękitny Falujący Płomień” (1 raz na turę)</style>\n\nPrzy przegranej w starciu Umiejętności obrony, przy 3+ [Agility], do końca Umiejętności obrony nie może zostać Ogłuszona obrażeniami, a po trafieniu stosuje „Odbieranie Kości” (2 razy na turę, z wyłączeniem wymuszonego Ogłuszenia)
626. [Pasywka bojowa (od ulepszenia 3) — podsumowanie] 조건 만족 시 추가 스킬 발동
   źródło: Passives.json :: dataList[id=1081513].summary
   (powtórzenie elementu 618 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — nazwa] 베고, 죽일 뿐
   źródło: Passives.json :: dataList[id=1081521].name
   limit: do 40 znaków
   EN: Cut Down What Must Be Felled
   PL: Tylko Ciąć i Zabijać
628. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — opis] 속도가 가장 빠른 아군 1명이 가하는 참격 스킬 피해량 +10%\n- 해당 아군에게 [Agility]이 있으면, 대신 참격 스킬 피해량 +15%
   źródło: Passives.json :: dataList[id=1081521].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: 1 ally with the fastest Speed deals +10% damage using Slash Skills\n- If the said ally has [Agility], deal +15% damage using Slash Skills instead
   PL: 1 Sojusznik z najwyższą Szybkością zadaje +10% obrażeń Umiejętnościami Siecznymi\n- Jeżeli ten sojusznik ma [Agility], zamiast tego zadaje +15% obrażeń Umiejętnościami Siecznymi

## [000] Haute Couture:: Boutique du Rouge — Ishmael — 오트쿠튀르:: 르루주 부티크
- ID Tożsamości: `10816` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 8 · HP bazowe: 85 · szybkość: 2–5 / 2–5 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Charge

629. [Karta Tożsamości — tytuł] 오트쿠튀르::\n르루주 부티크
   źródło: Personalities.json :: dataList[id=10816].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Haute Couture::\nBoutique du Rouge
   PL: Haute Couture::\nButik Le Rouge
630. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities.json :: dataList[id=10816].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities.json :: dataList[id=10816].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Karta Tożsamości — opis] 이스마엘의 열여섯번째 인격
   źródło: Personalities.json :: dataList[id=10816].desc
   limit: do 120 znaków
   EN: Ishmael's 16th Identity
   PL: Szesnasta Tożsamość Ishmael
633. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 아아 당신한테는 들리지 않나보죠?
   źródło: Skills_personality-08.json :: dataList[id=1081601].levelList[level=1].name ; dataList[id=1081601].levelList[level=2].name ; dataList[id=1081601].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 50 znaków
   EN: Ahh... You Can't Hear It, Can You?
   PL: Ahh... Nie słyszysz tego, prawda?
634. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 현재 체력이 80% 이상이면, [ChargeRougeAlly] 횟수 3 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ChargeRougeAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [WhenUse] At 80%+ HP, gain +3 [ChargeRougeAlly] Count
   PL: [WhenUse] Przy 80%+ HP zyskuje 3 Licznika [ChargeRougeAlly]
635. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1081601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +2 [ChargeRougeAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeRougeAlly] o 2
636. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1081601].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">자신의 [ChargeRougeAlly]이 2 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 현재 체력이 80% 이상이면, [ChargeRougeAlly] 횟수 3 얻음
   źródło: Skills_personality-08.json :: dataList[id=1081601].levelList[level=2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeRougeAlly], [WhenUse]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 2+ [ChargeRougeAlly], Coin Power +1</style>\n[WhenUse] At 80%+ HP, gain +3 [ChargeRougeAlly] Count
   PL: <style="highlight">Przy 2+ [ChargeRougeAlly] Moc Monet +1</style>\n[WhenUse] Przy 80%+ HP zyskuje 3 Licznika [ChargeRougeAlly]
638. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-08.json :: dataList[id=1081601].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +<style="highlight">3</style> [ChargeRougeAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeRougeAlly] o <style="highlight">3</style>
639. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 [ChargeRougeAlly]이 2 이상이면, 코인 위력 +1\n[WhenUse] 자신의 현재 체력이 80% 이상이면, [ChargeRougeAlly] 횟수 <style="highlight">5</style> 얻음\n<style="highlight">[WhenUse] 대상의 [Laceration] 3당 합 위력 +1 (최대 2)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081601].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeRougeAlly], [WhenUse], [Laceration]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: At 2+ [ChargeRougeAlly], Coin Power +1\n[WhenUse] At 80%+ HP, gain +<style="highlight">5</style> [ChargeRougeAlly] Count\n<style="highlight">[WhenUse] Clash Power +1 for every 3 [Laceration] on target (max 2)</style>
   PL: Przy 2+ [ChargeRougeAlly] Moc Monet +1\n[WhenUse] Przy 80%+ HP zyskuje <style="highlight">5</style> Licznika [ChargeRougeAlly]\n<style="highlight">[WhenUse] Moc Starcia +1 za każde 3 [Laceration] celu (maks. 2)</style>
640. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +3 [ChargeRougeAlly] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeRougeAlly] o 3<style="highlight"></style>
641. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 목소리가 들리지 않았다해서 부재했던것이 아니었음을!
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=1].name ; dataList[id=1081602].levelList[level=2].name ; dataList[id=1081602].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 90 znaków
   EN: Indeed, the Silence of the Voice Did Not Signify Its Absence!
   PL: Nieobecność Głosu Nie Znaczyła Jego Nieobecności!
642. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 635 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1081602].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1081602].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] 자신에게 [RougeIshmaelEclose]이 있으면, 이 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1081602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RougeIshmaelEclose]
   znaczenie tagów: [RougeIshmaelEclose] = 새단장 / Full Makeover
   EN: If this unit has [RougeIshmaelEclose], Reuse this Coin once (once per Skill)
   PL: Jeżeli ma [RougeIshmaelEclose], ponownie używa tę monetę 1 raz (1 raz na Umiejętność)
645. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1081602].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1081602].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 3 — opis] [ReUseOnSucceedAttack] 최대 체력의 ([ChargeRougeAlly] 위력 x 2)%만큼 체력 회복 (최대 10%)
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [ReUseOnSucceedAttack] Heal ([ChargeRougeAlly] Potency x 2)% HP (max 10%)
   PL: [ReUseOnSucceedAttack] Odzyskuje HP równe (2 x Moc [ChargeRougeAlly])% Maks. HP (maks. 10%)
647. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">자신의 [ChargeRougeAlly] 2당 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수가 10 미만이면, 최대 체력의 3 x (10 - 현재 [ChargeRougeAlly] 횟수)%만큼 체력을 소모하여 [ChargeRougeAlly] 횟수가 10으로 증가\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수를 10 소모하여 코인 위력 +1\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[BeforeAttack] 자신에게 [RougeIshmaelEclose]이 있으면, 피해량 +20%\n- [RougeIshmaelEclose]이 없으면, 자신의 체력을 최대 체력의 20%만큼 소모 후 발동</style>
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=2].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeRougeAlly], [WhenUse], [Laceration], [BeforeAttack], [RougeIshmaelEclose]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [RougeIshmaelEclose] = 새단장 / Full Makeover
   EN: <style="highlight">Final Power +1 for every 2 [ChargeRougeAlly] (max 2)\n[WhenUse] At fewer than 10 [ChargeRougeAlly] Count, consume 3(10 - current [ChargeRougeAlly] Count)% HP to raise [ChargeRougeAlly] Count to 10\n[WhenUse] Consume 10 [ChargeRougeAlly] Count to gain Coin Power +1\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[BeforeAttack] If this unit has [RougeIshmaelEclose], deal +20% damage\n- If this unit does not have [RougeIshmaelEclose], consume 20% HP on self to activate the above effect</style>
   PL: <style="highlight">Moc Końcowa +1 za każde 2 [ChargeRougeAlly] (maks. 2)\n[WhenUse] Przy mniej niż 10 Licznika [ChargeRougeAlly] zużywa HP równe 3 x (10 - Licznik [ChargeRougeAlly])% Maks. HP, aby zwiększyć Licznik [ChargeRougeAlly] do 10\n[WhenUse] Zużywa 10 Licznika [ChargeRougeAlly], aby zyskać Moc Monet +1\n[WhenUse] Jeżeli cel ma 6+ [Laceration], Moc Monet +1\n[BeforeAttack] Jeżeli ma [RougeIshmaelEclose], zadaje +20% obrażeń\n- Jeżeli nie ma [RougeIshmaelEclose], zużywa 20% HP, aby uruchomić powyższy efekt</style>
648. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +<style="highlight">4</style> [ChargeRougeAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeRougeAlly] o <style="highlight">4</style>
649. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 자신의 [ChargeRougeAlly]이 3 이상이면, 다음 턴에 [ScarletTakeDamageUp] 1 부여 (턴당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=2].coinlist[#1].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeRougeAlly], [ScarletTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation; [ScarletTakeDamageUp] = 색욕 취약 / Lust Fragility
   EN: <style="highlight">[OnSucceedAttack] At 3+ [ChargeRougeAlly], inflict 1 [ScarletTakeDamageUp] next turn (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttack] Przy 3+ [ChargeRougeAlly] nakłada 1 [ScarletTakeDamageUp] w następnej turze (1 raz na turę)</style>
650. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 4 — opis] [ReUseOnSucceedAttack] 최대 체력의 ([ChargeRougeAlly] 위력 x <style="highlight">3</style>)%만큼 체력 회복 (최대 <style="highlight">15%</style>)
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=2].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [ReUseOnSucceedAttack] Heal ([ChargeRougeAlly] Potency x <style="highlight">3</style>)% HP (max <style="highlight">15</style>%)
   PL: [ReUseOnSucceedAttack] Odzyskuje HP równe (<style="highlight">3</style> x Moc [ChargeRougeAlly])% Maks. HP (maks. <style="highlight">15</style>%)
651. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 [ChargeRougeAlly] 2당 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수가 10 미만이면, 최대 체력의 3 x (10 - 현재 [ChargeRougeAlly] 횟수)%만큼 체력을 소모하여 [ChargeRougeAlly] 횟수가 10으로 증가\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수를 10 소모하여 코인 위력 +1\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[BeforeAttack] 자신에게 [RougeIshmaelEclose]이 있으면, 피해량 +<style="highlight">40%</style>\n- [RougeIshmaelEclose]이 없으면, 자신의 체력을 최대 체력의 20%만큼 소모 후 발동
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=4].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeRougeAlly], [WhenUse], [Laceration], [BeforeAttack], [RougeIshmaelEclose]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [RougeIshmaelEclose] = 새단장 / Full Makeover
   EN: Final Power +1 for every 2 [ChargeRougeAlly] (max 2)\n[WhenUse] At fewer than 10 [ChargeRougeAlly] Count, consume 3(10 - current [ChargeRougeAlly] Count)% HP to raise [ChargeRougeAlly] Count to 10\n[WhenUse] Consume 10 [ChargeRougeAlly] Count to gain Coin Power +1\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[BeforeAttack] If this unit has [RougeIshmaelEclose], deal +<style="highlight">40</style>% damage\n- If this unit does not have [RougeIshmaelEclose], consume 20% HP on self to activate the above effect
   PL: Moc Końcowa +1 za każde 2 [ChargeRougeAlly] (maks. 2)\n[WhenUse] Przy mniej niż 10 Licznika [ChargeRougeAlly] zużywa HP równe 3 x (10 - Licznik [ChargeRougeAlly])% Maks. HP, aby zwiększyć Licznik [ChargeRougeAlly] do 10\n[WhenUse] Zużywa 10 Licznika [ChargeRougeAlly], aby zyskać Moc Monet +1\n[WhenUse] Jeżeli cel ma 6+ [Laceration], Moc Monet +1\n[BeforeAttack] Jeżeli ma [RougeIshmaelEclose], zadaje +<style="highlight">40%</style> obrażeń\n- Jeżeli nie ma [RougeIshmaelEclose], zużywa 20% HP, aby uruchomić powyższy efekt
652. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 4 증가<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +4 [ChargeRougeAlly] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeRougeAlly] o 4<style="highlight"></style>
653. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly]이 <style="highlight">2</style> 이상이면, 다음 턴에 [ScarletTakeDamageUp] 1 부여 (턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeRougeAlly], [ScarletTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation; [ScarletTakeDamageUp] = 색욕 취약 / Lust Fragility
   EN: [OnSucceedAttack] At <style="highlight">2</style>+ [ChargeRougeAlly], inflict 1 [ScarletTakeDamageUp] next turn (once per turn)
   PL: [OnSucceedAttack] Przy <style="highlight">2</style>+ [ChargeRougeAlly] nakłada 1 [ScarletTakeDamageUp] w następnej turze (1 raz na turę)
654. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 4 — opis] [ReUseOnSucceedAttack] 최대 체력의 ([ChargeRougeAlly] 위력 x 3)%만큼 체력 회복 (최대 15%)<style="highlight"></style>
   źródło: Skills_personality-08.json :: dataList[id=1081602].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [ReUseOnSucceedAttack] Heal ([ChargeRougeAlly] Potency x 3)% HP (max 15%)<style="highlight"></style>
   PL: [ReUseOnSucceedAttack] Odzyskuje HP równe (3 x Moc [ChargeRougeAlly])% Maks. HP (maks. 15%)<style="highlight"></style>
655. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 긁어내고, 뜯어내고, 못 박으라!
   źródło: Skills_personality-08.json :: dataList[id=1081603].levelList[level=3].name ; dataList[id=1081603].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 5 · monety: 3 (+3)
   limit: do 60 znaków
   EN: Scrape It Out, Rip It Off, and Nail It Down!
   PL: Wyskrobać, Rozdarć i Przybić!
656. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 [ChargeRougeAlly] 1당 피해량 +5% (최대 25%)\n[StartBattle] 자신의 현재 체력이 최대 체력의 50% 미만이거나 자신에게 [RougeIshmaelEclose]이 있으면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수가 15 미만이면, 최대 체력의 3 x (15 - 현재 [ChargeRougeAlly] 횟수)%만큼 체력을 소모하여 [ChargeRougeAlly] 횟수가 15로 증가\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수를 15 소모하여 코인 위력 +3\n[WhenUse] 대상의 [Laceration] 6당 코인 위력 +1 (최대 2)\n[BeforeAttack] 자신에게 [RougeIshmaelEclose]이 있으면, 피해량 +40%\n- [RougeIshmaelEclose]이 없으면, 자신의 체력을 최대 체력의 20%만큼 소모 후 발동
   źródło: Skills_personality-08.json :: dataList[id=1081603].levelList[level=3].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRougeAlly], [StartBattle], [RougeIshmaelEclose], [SuperCoin], [WhenUse], [Laceration], [BeforeAttack]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [StartBattle] = [전투 시작시] / [Combat Start]; [RougeIshmaelEclose] = 새단장 / Full Makeover; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: Deal +5% damage for every [ChargeRougeAlly] (max 25%)\n[StartBattle] At lower than 50% HP, or if this unit has [RougeIshmaelEclose], convert all Coins on this Skill to [SuperCoin]s\n[WhenUse] At fewer than 15 [ChargeRougeAlly] Count, consume 3(15 - current [ChargeRougeAlly] Count)% HP to raise [ChargeRougeAlly] Count to 15\n[WhenUse] Consume 15 [ChargeRougeAlly] Count to gain Coin Power +3\n[WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)\n[BeforeAttack] If this unit has [RougeIshmaelEclose], deal +40% damage\n- If this unit does not have [RougeIshmaelEclose], consume 20% HP on self to activate the above effect
   PL: Zadaje +5% obrażeń za każde 1 [ChargeRougeAlly] (maks. 25%)\n[StartBattle] Jeżeli ma mniej niż 50% HP albo ma [RougeIshmaelEclose], wszystkie monety tej Umiejętności stają się [SuperCoin]ami\n[WhenUse] Przy mniej niż 15 Licznika [ChargeRougeAlly] zużywa HP równe 3 x (15 - Licznik [ChargeRougeAlly])% Maks. HP, aby zwiększyć Licznik [ChargeRougeAlly] do 15\n[WhenUse] Zużywa 15 Licznika [ChargeRougeAlly], aby zyskać Moc Monet +3\n[WhenUse] Moc Monet +1 za każde 6 [Laceration] celu (maks. 2)\n[BeforeAttack] Jeżeli ma [RougeIshmaelEclose], zadaje +40% obrażeń\n- Jeżeli nie ma [RougeIshmaelEclose], zużywa 20% HP, aby uruchomić powyższy efekt
657. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-08.json :: dataList[id=1081603].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1081603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081603].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] 자신에게 [RougeIshmaelEclose]이 있으면, 이 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081603].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1081603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 644 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 (자신의 [ChargeRougeAlly] 위력 x 10)% 만큼 색욕 피해 (최대 30%)
   źródło: Skills_personality-08.json :: dataList[id=1081603].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1081603].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Deal Lust damage equal to ([ChargeRougeAlly] Potency on self x 10)% of this Coin's final damage (max 30%)
   PL: [OnSucceedAttack] Zadaje obrażenia Żądzy równe (10 x Moc własnego [ChargeRougeAlly])% końcowych obrażeń tej monety (maks. 30%)
661. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [ReUseOnSucceedAttack] 최대 체력의 ([ChargeRougeAlly] 위력 x 4)%만큼 체력 회복 (최대 20%)
   źródło: Skills_personality-08.json :: dataList[id=1081603].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1081603].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [ReUseOnSucceedAttack] Heal ([ChargeRougeAlly] Potency x 4)% HP (max 20%)
   PL: [ReUseOnSucceedAttack] Odzyskuje HP równe (4 x Moc [ChargeRougeAlly])% Maks. HP (maks. 20%)
662. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 [ChargeRougeAlly] 1당 피해량 +<style="highlight">10%</style> (최대 <style="highlight">50%</style>)\n[StartBattle] 자신의 현재 체력이 최대 체력의 50% 미만이거나 자신에게 [RougeIshmaelEclose]이 있으면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수가 15 미만이면, 최대 체력의 3 x (15 - 현재 [ChargeRougeAlly] 횟수)%만큼 체력을 소모하여 [ChargeRougeAlly] 횟수가 15로 증가\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수를 15 소모하여 코인 위력 +3\n[WhenUse] 대상의 [Laceration] 6당 코인 위력 +1 (최대 2)\n[BeforeAttack] 자신에게 [RougeIshmaelEclose]이 있으면, 피해량 +40%\n- [RougeIshmaelEclose]이 없으면, 자신의 체력을 최대 체력의 20%만큼 소모 후 발동
   źródło: Skills_personality-08.json :: dataList[id=1081603].levelList[level=4].desc
   limit: do 810 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeRougeAlly], [StartBattle], [RougeIshmaelEclose], [SuperCoin], [WhenUse], [Laceration], [BeforeAttack]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [StartBattle] = [전투 시작시] / [Combat Start]; [RougeIshmaelEclose] = 새단장 / Full Makeover; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: Deal +<style="highlight">10</style>% damage for every [ChargeRougeAlly] on self (max <style="highlight">50</style>%)\n[StartBattle] At lower than 50% HP, or if this unit has [RougeIshmaelEclose], convert all Coins on this Skill to [SuperCoin]s\n[WhenUse] At fewer than 15 [ChargeRougeAlly] Count, consume 3(15 - current [ChargeRougeAlly] Count)% HP to raise [ChargeRougeAlly] Count to 15\n[WhenUse] Consume 15 [ChargeRougeAlly] Count to gain Coin Power +3\n[WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)\n[BeforeAttack] If this unit has [RougeIshmaelEclose], deal +40% damage\n- If this unit does not have [RougeIshmaelEclose], consume 20% HP on self to activate the above effect
   PL: Zadaje +<style="highlight">10%</style> obrażeń za każde 1 [ChargeRougeAlly] (maks. <style="highlight">50%</style>)\n[StartBattle] Jeżeli ma mniej niż 50% HP albo ma [RougeIshmaelEclose], wszystkie monety tej Umiejętności stają się [SuperCoin]ami\n[WhenUse] Przy mniej niż 15 Licznika [ChargeRougeAlly] zużywa HP równe 3 x (15 - Licznik [ChargeRougeAlly])% Maks. HP, aby zwiększyć Licznik [ChargeRougeAlly] do 15\n[WhenUse] Zużywa 15 Licznika [ChargeRougeAlly], aby zyskać Moc Monet +3\n[WhenUse] Moc Monet +1 za każde 6 [Laceration] celu (maks. 2)\n[BeforeAttack] Jeżeli ma [RougeIshmaelEclose], zadaje +40% obrażeń\n- Jeżeli nie ma [RougeIshmaelEclose], zużywa 20% HP, aby uruchomić powyższy efekt
663. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">4</style> 부여
   źródło: Skills_personality-08.json :: dataList[id=1081603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">4</style> [Laceration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">4</style> [Laceration]
664. [Obrona (ulepszenia 1,4) — nazwa] 역시.. 이 세상에 의미는 있던 거죠?
   źródło: Skills_personality-08.json :: dataList[id=1081604].levelList[level=1].name ; dataList[id=1081604].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 4 · monety: 2 (+5)
   limit: do 80 znaków
   EN: Of Course... There was Meaning to this World After All
   PL: Z pewnością.. świat ten miał jednak sens?
665. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] 자신의 현재 체력이 최대 체력의 10% 이하면, [RougeIshmaelCocoon] 2를 얻고 [RougeIshmaelCocoon] 상태가 됨 (전투당 1회)\n[StartBattle] 자신에게 [RougeIshmaelEclose]이 없으면, 자신의 체력을 최대 체력의 20%만큼 소모하고 다음 턴에 이 슬롯의 [Aggro] 10 증가 (턴당 1회)
   źródło: Skills_personality-08.json :: dataList[id=1081604].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [RougeIshmaelCocoon], [RougeIshmaelEclose], [Aggro]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [RougeIshmaelCocoon] = 탈의실 / Changing Room; [RougeIshmaelEclose] = 새단장 / Full Makeover; [Aggro] = 도발치 / Aggro
   EN: [DuelCounter]\n[StartBattle] At 10% or lower HP, gain 2 [RougeIshmaelCocoon] and enter [RougeIshmaelCocoon] (once per Encounter)\n[StartBattle] If this unit does not have [RougeIshmaelEclose], consume 20% HP on self and gain +10 [Aggro] to this Skill Slot next turn (once per turn)
   PL: [DuelCounter]\n[StartBattle] Przy HP równym 10% Maks. HP lub niższym, zyskuje 2 [RougeIshmaelCocoon] i wchodzi w stan [RougeIshmaelCocoon] (1 raz na spotkanie)\n[StartBattle] Jeżeli nie ma [RougeIshmaelEclose], zużywa 20% HP i zwiększa [Aggro] tego slotu Umiejętności o 10 w następnej turze (1 raz na turę)
666. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 4 증가
   źródło: Skills_personality-08.json :: dataList[id=1081604].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081604].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +4 [ChargeRougeAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeRougeAlly] o 4
667. [Obrona (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-08.json :: dataList[id=1081604].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1081604].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[StartBattle] 자신의 현재 체력이 최대 체력의 10% 이하면, [RougeIshmaelCocoon] 2를 얻고 [RougeIshmaelCocoon] 상태가 됨 (전투당 1회)\n[StartBattle] 자신에게 [RougeIshmaelEclose]이 없으면, 자신의 체력을 최대 체력의 20%만큼 소모하고 다음 턴에 이 슬롯의 [Aggro] 10 증가 (턴당 1회)\n<style="highlight">[WhenUse] 자신의 [ChargeRougeAlly] 위력 2당 최종 위력 +1 (최대 2)\n[WhenUse] 대상의 [Laceration] 4당 피해량 +10% (최대 40%)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081604].levelList[level=4].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [RougeIshmaelCocoon], [RougeIshmaelEclose], [Aggro], [WhenUse], [ChargeRougeAlly], [Laceration]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [RougeIshmaelCocoon] = 탈의실 / Changing Room; [RougeIshmaelEclose] = 새단장 / Full Makeover; [Aggro] = 도발치 / Aggro; [WhenUse] = [사용시] / [On Use]; [ChargeRougeAlly] = 맥동 / Pulsation; [Laceration] = 출혈 / Bleed
   EN: [DuelCounter]\n[StartBattle] At 10% or lower HP, gain 2 [RougeIshmaelCocoon] and enter [RougeIshmaelCocoon] (once per Encounter)\n[StartBattle] If this unit does not have [RougeIshmaelEclose], consume 20% HP on self and gain +10 [Aggro] to this Skill Slot next turn (once per turn)\n<style="highlight">[WhenUse] Final Power +1 for every 2 [ChargeRougeAlly] Potency (max 2)\n[WhenUse] Deal +10% damage for every 4 [Laceration] on target (max 40%)</style>
   PL: [DuelCounter]\n[StartBattle] Przy HP równym 10% Maks. HP lub niższym, zyskuje 2 [RougeIshmaelCocoon] i wchodzi w stan [RougeIshmaelCocoon] (1 raz na spotkanie)\n[StartBattle] Jeżeli nie ma [RougeIshmaelEclose], zużywa 20% HP i zwiększa [Aggro] tego slotu Umiejętności o 10 w następnej turze (1 raz na turę)\n<style="highlight">[WhenUse] Moc Końcowa +1 za każde 2 Mocy [ChargeRougeAlly] (maks. 2)\n[WhenUse] Zadaje +10% obrażeń za każde 4 [Laceration] celu (maks. 40%)</style>
669. [Obrona (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신에게 [RougeIshmaelEclose]이 있으면, 최대 체력의 10%만큼 체력 회복 (턴당 1회)</style>
   źródło: Skills_personality-08.json :: dataList[id=1081604].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [RougeIshmaelEclose]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RougeIshmaelEclose] = 새단장 / Full Makeover
   EN: <style="highlight">[OnSucceedAttack] If this unit has [RougeIshmaelEclose], heal 10% HP (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli ma [RougeIshmaelEclose], odzyskuje 10% HP (1 raz na turę)</style>
670. [Obrona (ulepszenia 1,4) — nazwa] 목소리에 따라 기꺼이 나의 안으로
   źródło: Skills_personality-08.json :: dataList[id=1081605].levelList[level=1].name ; dataList[id=1081605].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 6 · monety: 1 (+9)
   limit: do 70 znaków
   EN: As the Voice Says, I Gladly Withdraw into Myself
   PL: Na Głos Chętnie Wycofuję się do Siebie
671. [Obrona (ulepszenie 1) — opis] [RougeIshmaelCocoon] 전용 스킬\n[CanDuelGuard]\n[StartBattle] 자신의 [ChargeRougeAlly] 횟수가 10 이상이면, 10 소모하여 다음 턴에 편성 순서가 가장 빠른 아군 2명에게 [ResultEnhancement] 1 부여 (턴당 1회)\n[StartBattle] 자신의 최대 체력의 50%만큼 체력 회복 (턴당 1회)\n[WinDuel] 자신의 [ChargeRougeAlly] 횟수 5 증가 (턴당 4회)
   źródło: Skills_personality-08.json :: dataList[id=1081605].levelList[level=1].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [RougeIshmaelCocoon], [CanDuelGuard], [StartBattle], [ChargeRougeAlly], [ResultEnhancement], [WinDuel]
   znaczenie tagów: [RougeIshmaelCocoon] = 탈의실 / Changing Room; [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeRougeAlly] = 맥동 / Pulsation; [ResultEnhancement] = 위력 증가 / Power Up; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [RougeIshmaelCocoon] exclusive Skill\n[CanDuelGuard]\n[StartBattle] At 10+ [ChargeRougeAlly] Count, consume 10 [ChargeRougeAlly] Count to apply 1 [ResultEnhancement] next turn to 2 allies with the earliest Deployment orders (once per turn)\n[StartBattle] Heal 50% HP (once per turn)\n[WinDuel] Gain +5 [ChargeRougeAlly] Count (4 times per turn)
   PL: [RougeIshmaelCocoon] Umiejętność wyłącznie dla tego stanu\n[CanDuelGuard]\n[StartBattle] Przy 10+ Licznika [ChargeRougeAlly] zużywa 10 Licznika [ChargeRougeAlly], aby nałożyć 1 [ResultEnhancement] w następnej turze na 2 Sojuszników przydzielonych najwcześniej na pozycjach (1 raz na turę)\n[StartBattle] Odzyskuje 50% HP (1 raz na turę)\n[WinDuel] Zwiększa własny Licznik [ChargeRougeAlly] o 5 (4 razy na turę)
672. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-08.json :: dataList[id=1081605].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1081605].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Obrona (ulepszenie 4) — opis] [RougeIshmaelCocoon] 전용 스킬\n[CanDuelGuard]\n[StartBattle] 자신의 [ChargeRougeAlly] 횟수가 10 이상이면, 10 소모하여 다음 턴에 편성 순서가 가장 빠른 아군 2명에게 [ResultEnhancement] 1 부여 (턴당 1회)\n<style="highlight">- 대상이 르루주 소속이면, 다음 턴에 자신의 [ChargeRougeAlly] 횟수가 5 증가하고, 대상에게 [AttackDmgUp] 1 추가 부여</style>\n[StartBattle] 자신의 최대 체력의 <style="highlight">100%</style>만큼 체력 회복 (턴당 1회)\n<style="highlight">[WinDuel] 자신에게 부여된 해제 가능한 부정적인 효과 중 무작위 1개 제거 (턴당 1회)</style>\n[WinDuel] 자신의 [ChargeRougeAlly] 횟수 5 증가 (턴당 4회)
   źródło: Skills_personality-08.json :: dataList[id=1081605].levelList[level=4].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RougeIshmaelCocoon], [CanDuelGuard], [StartBattle], [ChargeRougeAlly], [ResultEnhancement], [AttackDmgUp], [WinDuel]
   znaczenie tagów: [RougeIshmaelCocoon] = 탈의실 / Changing Room; [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeRougeAlly] = 맥동 / Pulsation; [ResultEnhancement] = 위력 증가 / Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [RougeIshmaelCocoon] exclusive Skill\n[CanDuelGuard]\n[StartBattle] At 10+ [ChargeRougeAlly] Count, consume 10 [ChargeRougeAlly] Count to apply 1 [ResultEnhancement] next turn to 2 allies with the earliest Deployment orders (once per turn)\n<style="highlight">- If the affected ally is a Rouge Identity, gain +5 [ChargeRougeAlly] Count next turn and additionally apply 1 [AttackDmgUp] on the said ally</style>\n[StartBattle] Heal <style="highlight">100</style>% HP (once per turn)\n<style="highlight">[WinDuel] Remove 1 random removable negative effect applied to self (once per turn)</style>\n[WinDuel] Gain +5 [ChargeRougeAlly] Count (4 times per turn)
   PL: [RougeIshmaelCocoon] Umiejętność wyłącznie dla tego stanu\n[CanDuelGuard]\n[StartBattle] Przy 10+ Licznika [ChargeRougeAlly] zużywa 10 Licznika [ChargeRougeAlly], aby nałożyć 1 [ResultEnhancement] w następnej turze na 2 Sojuszników przydzielonych najwcześniej na pozycjach (1 raz na turę)\n<style="highlight">- Jeżeli objęty sojusznik należy do frakcji Le Rouge, zyskuje 5 Licznika [ChargeRougeAlly] w następnej turze i dodatkowo nakłada 1 [AttackDmgUp] na tego sojusznika</style>\n[StartBattle] Odzyskuje <style="highlight">100%</style> HP (1 raz na turę)\n<style="highlight">[WinDuel] Usuwa 1 losowy usuwalny negatywny efekt nałożony na siebie (1 raz na turę)</style>\n[WinDuel] Zwiększa własny Licznik [ChargeRougeAlly] o 5 (4 razy na turę)
674. [Pasywka bojowa (od ulepszenia 1) — nazwa] 탈의실 속으로…
   źródło: Passives.json :: dataList[id=1081602].name
   limit: do 40 znaków
   EN: Into the Changing Room...
   PL: Do Kabiny Przebieralni...
675. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 중 누적으로 자신의 [ChargeRougeAlly] 횟수 10을 소모할 때마다 [ChargeRougeAlly] 1 얻음\n\n자신의 기본 스킬의 체력 감소 효과로 흐트러지거나 체력이 1 미만으로 감소하지 않음\n(체력이 1인 경우, 기본 스킬 효과 중 체력 소모로 발동되는 효과를 적용 받을 수 있음)\n\n이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고, 즉시 [RougeIshmaelCocoon] 2를 얻고 [RougeIshmaelCocoon] 상태가 됨 (전투당 1회)\n- 수비 스킬 효과로 [RougeIshmaelCocoon] 상태가 되었으면, 해당 효과는 이번 전투 동안 발동하지 않음\n\n[RougeIshmaelCocoon] 상태가 될 때 자신의 최대 체력만큼 보호막을 얻음\n- 이 효과로 얻은 보호막은 턴 종료시에도 사라지지 않음\n- [RougeIshmaelCocoon] 상태가 해제될 때 위 효과에서 얻은 보호막은 사라짐\n\n[RougeIshmaelCocoon] 상태일 때, ‘목소리에 따라 기꺼이 나의 안으로’만 사용 가능함 (E.G.O 스킬 사용 불가)\n\n턴 종료시 [RougeIshmaelCocoon]이 0이면, [RougeIshmaelCocoon] 상태가 해제 되며 [RougeIshmaelEclose] 상태가 되고, [ChargeRougeAlly] 횟수 5 얻음
   źródło: Passives.json :: dataList[id=1081602].desc
   limit: do 1500 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRougeAlly], [RougeIshmaelCocoon], [RougeIshmaelEclose]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [RougeIshmaelCocoon] = 탈의실 / Changing Room; [RougeIshmaelEclose] = 새단장 / Full Makeover
   EN: Gain 1 [ChargeRougeAlly] for every 10 cumulative [ChargeRougeAlly] Count this unit consumes in this Encounter\n\nHP consumption effects from this unit's Base Skills do not Stagger or reduce this unit's HP below 1\n(At 1 HP, Base Skill effects that consume HP will be activated for free)\n\nIn this Encounter, when this unit takes damage that brings its HP down to 0, nullify that damage; then, immediately gain 2 [RougeIshmaelCocoon] and enter the [RougeIshmaelCocoon] state (once per Encounter)\n- If this unit entered [RougeIshmaelCocoon] state via its Defense Skill effects, the above effect will not trigger for the rest of the Encounter\n\nWhen entering [RougeIshmaelCocoon] state, gain Shield equal to this unit's max HP\n- Shield gained from this effect does not expire at Turn End\n- When [RougeIshmaelCocoon] state expires, Shield gained from the above effect expires\n\n- While in the [RougeIshmaelCocoon] state, aside from its exclusive Skill "As the Voice Says, I Gladly Withdraw into Myself", cannot equip Defense Skills or E.G.O Skills\n\nTurn End: At 0 [RougeIshmaelCocoon] Stack, leave [RougeIshmaelCocoon] state and enter [RougeIshmaelEclose] state; then, gain +5 [ChargeRougeAlly] Count
   PL: Za każde łączne zużycie 10 własnego Licznika [ChargeRougeAlly] podczas walki zyskuje 1 [ChargeRougeAlly]\n\nEfekty zużycia HP własnych podstawowych Umiejętności nie Ogłuszają ani nie obniżają HP tej jednostki poniżej 1\n(Przy 1 HP efekty zużycia HP podstawowych Umiejętności uruchamiane są bezpłatnie)\n\nW tym spotkaniu, gdy ta jednostka otrzymuje obrażenia redukujące HP do 0, unieważnia te obrażenia; natychmiast zyskuje 2 [RougeIshmaelCocoon] i wchodzi w stan [RougeIshmaelCocoon] (1 raz na spotkanie)\n- Jeżeli weszła w stan [RougeIshmaelCocoon] przez efekty Umiejętności obrony, powyższy efekt nie uruchamia się do końca spotkania\n\nWchodząc w stan [RougeIshmaelCocoon], zyskuje Tarczę równą własnemu Maks. HP\n- Tarcza zyskana tym efektem nie wygasa na koniec tury\n- Gdy stan [RougeIshmaelCocoon] wygasa, Tarcza zyskana powyższym efektem wygasa\n\nW stanie [RougeIshmaelCocoon] dostępna jest wyłącznie Umiejętność „Na Głos Chętnie Wycofuję się do Siebie” (Umiejętności E.G.O niedostępne)\n\nNa koniec tury, przy 0 stosów [RougeIshmaelCocoon], stan [RougeIshmaelCocoon] wygasa, jednostka wchodzi w stan [RougeIshmaelEclose] i zyskuje 5 Licznika [ChargeRougeAlly]
676. [Pasywka bojowa (od ulepszenia 1) — tekst klimatyczny] 옷을 갈아입을 거에요. 더 나다운 모습으로!
   źródło: Passives.json :: dataList[id=1081602].flavor
   limit: do 120 znaków
   EN: I'm going to get myself a makeover! So I can get nearer to my true self!
   PL: Przebiorę się. Bliżej prawdziwej wersji siebie!
677. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Wrath, posiadane 1× Lust, posiadane 2× Envy) — nazwa] 변화의 요람
   źródło: Passives.json :: dataList[id=1081601].name
   limit: do 40 znaków
   EN: Cradle of Change
   PL: Kolebka Zmiany
678. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Wrath, posiadane 1× Lust, posiadane 2× Envy) — opis] 기본 스킬 사용 시 자신의 [ChargeRougeAlly] 횟수가 10 미만이면, 합 위력 +2\n\n자신이 [RougeIshmaelEclose] 상태면, 기본 스킬 적중시 최대 체력의 8%만큼 체력 회복 (턴당 5회)
   źródło: Passives.json :: dataList[id=1081601].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRougeAlly], [RougeIshmaelEclose]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [RougeIshmaelEclose] = 새단장 / Full Makeover
   EN: On Base Skill Use, at fewer than 10 [ChargeRougeAlly] Count, Clash Power +2\n\nIf this unit is in [RougeIshmaelEclose] state, heal 8% HP On Hit using Base Skills (5 times per turn)
   PL: Przy użyciu podstawowej Umiejętności, przy mniej niż 10 Licznika [ChargeRougeAlly], Moc Starcia +2\n\nW stanie [RougeIshmaelEclose], przy trafieniu podstawową Umiejętnością odzyskuje 8% HP (5 razy na turę)
679. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Wrath, posiadane 1× Lust, posiadane 2× Envy) — tekst klimatyczny] 탈의실이라고도 부르지만, 밖에서는 이것을 번데기나 알이라고 부르는 편이 더 알맞을 거야.\n안에서 자신의 몸을 녹이거나 으깨가면서 변화하고, 때가 되었을 때 껍질을 깨고 밖으로 나오겠지.\n하지만 아직 준비되지 않은 것을 밖에서 찢어버리면, 슬프게도 망가지고 말아.\n그래서 이 시기가 가장 취약하고, 어느 때보다 보살핌이 필요해.
   źródło: Passives.json :: dataList[id=1081601].flavor
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n
   EN: While some might call this a "changing room," it would be more appropriate for those on the other side to call it a "pupa" or an "egg."\nShe melts and tears herself apart, metamorphosing... Until, when the time is right, she will shatter the shells and emerge into the world outside.\nBut if someone from the outside rips into the shell before she is ready... sadly, they will end up breaking her.\nThis is her most vulnerable moment, and therefore must be nurtured and looked after.
   PL: Choć nazywane bywa „kabiną przebieralni”, z zewnątrz właściwiej byłoby mówić o „poczwarkach” albo „jajach”.\nW środku rozpuszcza i rozcina własne ciało, metamorfozując... Aż gdy przyjdzie czas, rozbije skorupę i wyłoni się na zewnątrz.\nLecz gdy ktoś z zewnątrz rozedrze skorupę, zanim będzie gotowa... niestety, zostanie złamana.\nTo jej najbardziej wrażliwy moment, dlatego wymaga opieki bardziej niż kiedykolwiek.
680. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — nazwa] [르루주 오트쿠튀르 악트리스] - 로브
   źródło: Passives.json :: dataList[id=1081621].name
   limit: do 60 znaków
   EN: [Actrice Haute Couture du Rouge] - Robes
   PL: [Actrice Haute Couture du Rouge] - Roba
681. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — opis] 편성 순서 1번과 2번 인격이 패시브, 스킬, 코인의 효과로 회복하는 체력 회복량 +20%\n\n색욕 공명이 완전 공명이면, 이번 턴에 편성 순서 1번과 2번의 스킬로 받는 피해량 -10%
   źródło: Passives.json :: dataList[id=1081621].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: #1 and #2 Deployed allies heal +20% more HP from Passive, Skill, and Coin effects\n\nOn Lust A-Reson., #1 and #2 allies take -10% damage from Skills for the turn
   PL: Tożsamości przydzielone na 1. i 2. pozycji odzyskują +20% więcej HP efektami pasywek, Umiejętności i monet\n\nPrzy Pełnym Rezonansie Żądzy otrzymują w tej turze -10% obrażeń od Umiejętności
682. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — tekst klimatyczny] 거울세계의 인격을 원본 그대로 덮어쓰기 어려울 때, 배우만을 위해 맞춰진 형태로 옷이 만들어지고, 입혀진다.\n오트쿠튀르는 일종의 시네마적인 재구성이다. 있었던 존재를 옷으로 치환하여 덮어쓰고, 배우는 그 존재에 이입하고 몰입하여 연기한다. 영화를 보는 사람은 그것이 연기가 아닌 실재라는 거짓말을 받아들이고, 배우는 그 이야기 안에서만큼은 그 존재가 되어 원본을 재현한다.
   źródło: Passives.json :: dataList[id=1081621].flavor
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When it isn't feasible to overwrite the subject with the exact form of the Mirrored Identity, a "costume" fitted for each actor is designed and worn.\n\nHaute Couture is a form of cinematic reinterpretation; it replaces an existent being with an outfit, and the actor, now overwritten, dutifully performs the given role in full immersion. \n\nThis deception of reality is readily accepted by the audience at the theater while the actor, at least within the confines of the narrative, embodies the original existence in earnest recreation.
   PL: Gdy nie da się nadpisać Tożsamości ze Świata Lustra jej oryginalną postacią, „kostium” szyty na miarę każdego aktora zostaje zaprojektowany i założony.\nHaute Couture to forma kinowej reinterpretacji; zamienia istniejące istnienie w ubiór, a aktor, teraz nadpisany, gorliwie odgrywa powierzoną rolę w pełnym zanurzeniu.\nTo oszustwo rzeczywistości chętnie akceptuje widownia w teatrze, podczas gdy aktor, przynajmniej w granicach narracji, ucieleśnia oryginalne istnienie z prawdziwym oddaniem.

## [?] Cheery Chickies Sinnerling — Ishmael — 병아리반 수감생
- ID Tożsamości: `400032` (plik: `Personalities-x1p1c1.json`)

683. [Karta Tożsamości — tytuł] 병아리반 수감생
   źródło: Personalities-x1p1c1.json :: dataList[id=400032].title
   limit: do 40 znaków
   EN: Cheery Chickies Sinnerling
   PL: Grzeszniczek Grupy Pisklaków
684. [Karta Tożsamości — nazwa] 이스마엘
   źródło: Personalities-x1p1c1.json :: dataList[id=400032].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Karta Tożsamości — nazwa z tytułem] 이스마엘
   źródło: Personalities-x1p1c1.json :: dataList[id=400032].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Karta Tożsamości — opis] 이스마엘의 ??? 인격
   źródło: Personalities-x1p1c1.json :: dataList[id=400032].desc
   limit: do 120 znaków
   EN: Ishmael's ??? Identity
   PL: ??? Tożsamość Ishmael
687. [Pasywka bojowa [40003201] — nazwa] 빨악
   źródło: Passives-x1p1c1.json :: dataList[id=40003201].name
   limit: do 40 znaków
   EN: Las-ditch Stwuggle
   PL: — nazwa] Ostatnie Zrywy
688. [Pasywka bojowa [40003201] — opis] 합 진행 시 자신의 체력이 25% 미만이면 합 위력 +1
   źródło: Passives-x1p1c1.json :: dataList[id=40003201].desc
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Pasywka bojowa [40003202] — nazwa] 쌀아남고 말껏이라는 마음
   źródło: Passives-x1p1c1.json :: dataList[id=40003202].name
   limit: do 40 znaków
   EN: Detewminashun to Suwiwe
   PL: — nazwa] Postanowienie Przetrwania
690. [Pasywka bojowa [40003202] — opis] 현재 체력이 가장 낮은 아군 1명 체력이 50% 미만이면 합 진행 시 합 위력 +1
   źródło: Passives-x1p1c1.json :: dataList[id=40003202].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
