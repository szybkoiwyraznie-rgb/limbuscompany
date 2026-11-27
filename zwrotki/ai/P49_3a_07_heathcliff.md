# Paczka AI P49 (Fala 3 · 3A) — Grzesznik 07 — Heathcliff

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P49_3a_07_heathcliff.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P49_3a_07_heathcliff.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Grzesznik #07: Heathcliff (히스클리프)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 히스클리프
   źródło: Characters.json :: dataList[id=7].name
   limit: do 40 znaków
   EN: Heathcliff
   PL: Heathcliff
2. [Akta więźnia — nazwa] 히스클리프
   źródło: IntroduceCharacter.json :: dataList[id=히스클리프].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [0] LCB Sinner — Heathcliff — LCB 수감자
- ID Tożsamości: `10701` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 78 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor

3. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10701].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL: LCB\nGrzesznik
4. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10701].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
5. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10701].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — opis] 히스클리프의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10701].desc
   limit: do 120 znaków
   EN: Heathcliff’s 1st Identity
   PL: Pierwsza Tożsamość Heathcliffa
7. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 배트 치기
   źródło: Skills.json :: dataList[id=1070101].levelList[level=1].name ; dataList[id=1070101].levelList[level=2].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Bat Bash
   PL: Uderzenie Kijem
8. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 3 부여
   źródło: Skills.json :: dataList[id=1070101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 3 [Vibration]
   PL: [OnSucceedAttackHead] Nakłada 3 Wstrząsu
9. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills.json :: dataList[id=1070101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] Nakłada 3 Wstrząsu
10. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 내려박기
   źródło: Skills.json :: dataList[id=1070102].levelList[level=1].name ; dataList[id=1070102].levelList[level=2].name ; dataList[id=1070102].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Smackdown
   PL: Roztrzaskanie
11. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills.json :: dataList[id=1070102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Attack Power Up next turn
   PL: [WhenUse] Zyskuje w następnej turze 1 Wzrostu Mocy Ataku
12. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WhenUse] 다음 턴에 공격 위력 증가, 피해량 증가 1 얻음
   źródło: Skills.json :: dataList[id=1070102].levelList[level=2].desc ; dataList[id=1070102].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Attack Power Up and Damage Up next turn
   PL: [WhenUse] Zyskuje w następnej turze 1 Wzrostu Mocy Ataku i 1 Wzrostu Obrażeń
13. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills.json :: dataList[id=1070102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 2 [Vibration]
   PL: [OnSucceedAttackHead] Nakłada 2 Wstrząsu
14. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 분풀기
   źródło: Skills.json :: dataList[id=1070103].levelList[level=3].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 4 · monety: 2 (+8)
   limit: do 40 znaków
   EN: Upheaval
   PL: Zryw
15. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 코인 위력 +2
   źródło: Skills.json :: dataList[id=1070103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Next Coin has +2 Power
   PL: [OnSucceedAttackHead] Następna moneta ma Moc +2
16. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills.json :: dataList[id=1070103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]
17. [Obrona (ulepszenie 1) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1070104].levelList[level=1].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 7 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Counter
   PL: Kontra
18. [Pasywka bojowa (od ulepszenia 1, rezonans 4× Envy) — nazwa] 르쌍티망
   źródło: Passives.json :: dataList[id=1070101].name
   limit: do 40 znaków
   EN: Ressentiment
   PL: Ressentiment
19. [Pasywka bojowa (od ulepszenia 1, rezonans 4× Envy) — opis] 대상이 자신보다 최대 체력이 높으면 피해량 +10%
   źródło: Passives.json :: dataList[id=1070101].desc
   limit: do 120 znaków
   EN: Deal +10% damage to targets that have higher Max HP.
   PL: Jeżeli cel ma wyższe Maks. HP niż ta jednostka, zadaje +10% obrażeń
20. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — nazwa] 악에 받친
   źródło: Passives.json :: dataList[id=1070121].name
   limit: do 40 znaków
   EN: Spite-driven
   PL: Pędzone Złością
21. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — opis] 최대 체력이 가장 낮은 아군 1명 타격 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1070121].desc
   limit: do 120 znaków
   EN: 1 ally that has the lowest Max HP deals +10% Blunt damage.
   PL: 1 Sojusznik z najniższym Maks. HP zadaje +10% obrażeń Umiejętnościami Uderzenia

## [00] Shi Assoc. South Section 5 — Heathcliff — 남부 시 협회 5과
- ID Tożsamości: `10702` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Poise

22. [Karta Tożsamości — tytuł] 남부 시 협회\n5과
   źródło: Personalities.json :: dataList[id=10702].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Shi Assoc.\nSouth Section 5
   PL: Południowe Stowarzyszenie Shi\nSekcja 5
23. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10702].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
24. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10702].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
25. [Karta Tożsamości — opis] 히스클리프의 두번째 인격
   źródło: Personalities.json :: dataList[id=10702].desc
   limit: do 120 znaków
   EN: Heathcliff’s 2nd Identity
   PL: Druga Tożsamość Heathcliffa
26. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 극검
   źródło: Skills.json :: dataList[id=1070201].levelList[level=1].name ; dataList[id=1070201].levelList[level=2].name ; dataList[id=1070201].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Extreme Edge
   PL: Skrajne Ostrze
27. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 자신의 체력이 25%미만일 때 스킬 위력 +1
   źródło: Skills.json :: dataList[id=1070201].levelList[level=1].desc
   limit: do 120 znaków
   EN: At less than 25% HP, +1 Skill Power
   PL: Przy HP poniżej 25% Moc Umiejętności +1
28. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 자신의 체력이 25%미만일 때 스킬 위력 +2
   źródło: Skills.json :: dataList[id=1070201].levelList[level=2].desc
   limit: do 120 znaków
   EN: At less than 25% HP, +2 Skill Power
   PL: Przy HP poniżej 25% Moc Umiejętności +2
29. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 체력이 50%미만일 때 스킬 위력 +2\n[WhenUse] 호흡 횟수 3 얻음
   źródło: Skills.json :: dataList[id=1070201].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: At less than 50% HP, Skill Power +2\n[WhenUse] Gain +3 [Breath] Count
   PL: Przy HP poniżej 50% Moc Umiejętności +2\n[WhenUse] Zyskuje +3 Licznika [Breath]
30. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 비검
   źródło: Skills.json :: dataList[id=1070202].levelList[level=1].name ; dataList[id=1070202].levelList[level=2].name ; dataList[id=1070202].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 5 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Flying Sword
   PL: Latający Miecz
31. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 자신의 체력이 25%미만일 때 스킬 위력 +1
   źródło: Skills.json :: dataList[id=1070202].levelList[level=1].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
32. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 자신의 체력이 25%미만일 때 스킬 위력 +2
   źródło: Skills.json :: dataList[id=1070202].levelList[level=2].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
33. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 체력이 50%미만일 때 스킬 위력 +2\n[WhenUse] 호흡 3 얻음
   źródło: Skills.json :: dataList[id=1070202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: At less than 50% HP, +2 Skill Power\n[WhenUse] Gain 3 [Breath]
   PL: Przy HP poniżej 50% Moc Umiejętności +2\n[WhenUse] Zyskuje 3 [Breath]
34. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 섬격
   źródło: Skills.json :: dataList[id=1070203].levelList[level=3].name ; dataList[id=1070203].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Flashing Strike
   PL: Błyskawiczne Uderzenie
35. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 체력이 25%미만일 때 스킬 위력 +2
   źródło: Skills.json :: dataList[id=1070203].levelList[level=3].desc
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
36. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [BeforeAttack] 자신의 체력 5 감소, 이 코인의 스킬 피해량 +50%
   źródło: Skills.json :: dataList[id=1070203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1070203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] Lose 5 HP; +50% Skill Damage for this Coin
   PL: [BeforeAttack] Traci 5 HP; zadaje +50% obrażeń Umiejętności tą monetą
37. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [BeforeAttack] 자신의 체력 5 감소, 이 코인의 스킬 피해량 +50%
   źródło: Skills.json :: dataList[id=1070203].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1070203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 호흡 횟수가 10 이상이면, 스킬 위력 +2\n자신의 체력이 50%미만일 때, 공격 가중치 +1
   źródło: Skills.json :: dataList[id=1070203].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 10+ [Breath] Count, Skill Power +2\nAt less than 50% HP, Atk Weight +1
   PL: Przy 10+ Liczniku [Breath] Moc Umiejętności +2\nPrzy HP poniżej 50% Waga ataku +1
39. [Obrona (ulepszenia 1,4) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1070204].levelList[level=1].name ; dataList[id=1070204].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 8 · monety: 1 (+5)
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
40. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 체력 5 감소\n자신의 호흡 횟수가 3 이상이면, 피해량 +50%
   źródło: Skills.json :: dataList[id=1070204].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Lose 5 HP\nAt 3+ [Breath] Count, Damage +50%
   PL: [WhenUse] Traci 5 HP\nPrzy 3+ Liczniku [Breath] zadaje +50% obrażeń
41. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — nazwa] 호흡
   źródło: Passives.json :: dataList[id=1070201].name
   limit: do 40 znaków
   EN: Respiration
   PL: Oddech
42. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — opis] 이번 턴에 공격으로 피해를 받으면 피해량 +10%
   źródło: Passives.json :: dataList[id=1070201].desc
   limit: do 120 znaków
   EN: After taking damage from attacks this turn, deal +10% damage.
   PL: Gdy w tej turze otrzyma obrażenia od ataku, zadaje +10% obrażeń.
43. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 자신을 돌보지 않음
   źródło: Passives.json :: dataList[id=1070221].name
   limit: do 40 znaków
   EN: Self-neglect
   PL: Zaniedbanie Siebie
44. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 현재 체력이 가장 낮은 아군 1명 가하는 피해량 +20%, 받는 피해량 +20%
   źródło: Passives.json :: dataList[id=1070221].desc
   limit: do 120 znaków
   EN: 1 ally with the least HP deals and takes +20% damage.
   PL: 1 Sojusznik z najniższym obecnym HP zadaje i otrzymuje +20% obrażeń.

## [000] R Corp. 4th Pack Rabbit — Heathcliff — R사 제 4무리 토끼팀
- ID Tożsamości: `10703` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Charge, Bleed, Rupture

45. [Karta Tożsamości — tytuł] R사 제 4무리\n토끼팀
   źródło: Personalities.json :: dataList[id=10703].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: R Corp. 4th Pack\nRabbit
   PL: R Corp. 4 Pack\nOddział Królików
46. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10703].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10703].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [Karta Tożsamości — opis] 히스클리프의 세번째 인격
   źródło: Personalities.json :: dataList[id=10703].desc
   limit: do 120 znaków
   EN: Heathcliff’s 3rd Identity
   PL: Trzecia Tożsamość Heathcliffa
49. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 풀뜯기
   źródło: Skills.json :: dataList[id=1070301].levelList[level=1].name ; dataList[id=1070301].levelList[level=2].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Graze the Grass
   PL: Pasz się Trawą
50. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] 탄환 1 소모
   źródło: Skills.json :: dataList[id=1070301].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1070301].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: Spend 1 Ammo
   PL: Zużywa 1 amunicji
51. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] 탄환 1 소모
   źródło: Skills.json :: dataList[id=1070301].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1070301].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 1 증가
   źródło: Skills.json :: dataList[id=1070301].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +1 Charge Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik Ładowania o 1
53. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 3 증가
   źródło: Skills.json :: dataList[id=1070301].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +3 Charge Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik Ładowania o 3
54. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 집중 사격
   źródło: Skills.json :: dataList[id=1070302].levelList[level=1].name ; dataList[id=1070302].levelList[level=2].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Concentrated Fire
   PL: Skoncentrowany Ostrzał
55. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070302].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1070302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: Spend 1 Ammo\n[OnSucceedAttack] Inflict 1 Bleed
   PL: Zużywa 1 amunicji\n[OnSucceedAttack] Nakłada 1 Krwawienia
56. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070302].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1070302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070302].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1070302].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 속도가 6 이상이면, 코인 위력 + 1
   źródło: Skills.json :: dataList[id=1070302].levelList[level=2].desc
   limit: do 120 znaków
   EN: Coin Power +1 at 6+ Speed
   PL: Przy 6+ Szybkości Moc Monet +1
59. [Umiejętność 3 (×1) (ulepszenie 1) — nazwa] 신속한 제압
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 3 · monety: 5 (+2)
   limit: do 40 znaków
   EN: Quick Suppression
   PL: Szybka Eliminacja
60. [Umiejętność 3 (×1) (ulepszenie 1) — opis] 속도가 6 이상이면, 코인 위력 + 2
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].desc
   limit: do 120 znaków
   EN: Coin Power +2 at 6+ Speed
   PL: Przy 6+ Szybkości Moc Monet +2
61. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 1, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 취약 2 부여
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: Spend 1 Ammo\n[OnSucceedAttack] Inflict 2 Fragile
   PL: Zużywa 1 amunicji\n[OnSucceedAttack] Nakłada 2 Wrażliwości
62. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 2, efekt 1 — opis] 탄환 1 소모. [OnSucceedAttack] 취약 2 부여
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Rupture
   PL: [OnSucceedAttack] Nakłada 1 Rozdarcia
64. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL: [OnSucceedAttack] Nakłada 2 Rozdarcia
65. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 5, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills.json :: dataList[id=1070303].levelList[level=1].coinlist[#4].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture
   PL: [OnSucceedAttack] Nakłada 3 Rozdarcia
66. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1070304].levelList[level=1].name ; dataList[id=1070304].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL: Unik
67. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 1 증가
   źródło: Skills.json :: dataList[id=1070304].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +1 Charge Count
   PL: [WhenUse] Zwiększa własny Licznik Ładowania o 1
68. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — nazwa] 풀 뜯을 준비
   źródło: Passives.json :: dataList[id=1070301].name
   limit: do 40 znaków
   EN: Raring to Graze
   PL: Gotów do Pasania
69. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Wrath) — opis] 다음 턴 시작 시 (분노 공명 수)만큼 충전 횟수 증가.\n충전 횟수가 5 이상이면 신속 1, 공격 위력 증가 1을 얻음
   źródło: Passives.json :: dataList[id=1070301].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Gain (Wrath Reson.) Charge Count next turn.\nAt 5+ Charge Count, gain 1 [Agility] and Attack Power Up.
   PL: W następnej turze zyskuje Licznik Ładowania równy (Rezonans Gniewu).\nPrzy 5+ Liczniku Ładowania zyskuje 1 [Agility] i Wzrost Mocy Ataku.
70. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — nazwa] 집념
   źródło: Passives.json :: dataList[id=1070321].name
   limit: do 40 znaków
   EN: Doggedness
   PL: Upór
71. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Wrath) — opis] 속도가 가장 높은 아군 1명 관통 스킬의 피해량 +10%
   źródło: Passives.json :: dataList[id=1070321].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed deals +10% Pierce damage.
   PL: 1 Sojusznik z najwyższą Szybkością zadaje +10% obrażeń Umiejętnościami Kłucia

## [00] N Corp. Kleinhammer — Heathcliff — N사 작은 망치
- ID Tożsamości: `10704` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 1 · HP bazowe: 76 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed

72. [Karta Tożsamości — tytuł] N사\n작은 망치
   źródło: Personalities.json :: dataList[id=10704].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: N Corp.\nKleinhammer
   PL: N Corp.\nMały Młot
73. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10704].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10704].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [Karta Tożsamości — opis] 히스클리프의 네번째 인격
   źródło: Personalities.json :: dataList[id=10704].desc
   limit: do 120 znaków
   EN: Heathcliff’s 4th Identity
   PL: Czwarta Tożsamość Heathcliffa
76. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 미숙한 못질
   źródło: Skills.json :: dataList[id=1070401].levelList[level=1].name ; dataList[id=1070401].levelList[level=2].name ; dataList[id=1070401].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Gawky Nailing
   PL: Niezdarny Gwoździk
77. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 1 Bleed
   PL: [OnSucceedAttackTail] Nakłada 1 Krwawienia
78. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL: [OnSucceedAttackHead] Nakłada 1 Krwawienia
79. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 못 1 부여
   źródło: Skills.json :: dataList[id=1070401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1070401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Nails next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze 1 Gwoździa
80. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttackTail] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070401].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1070401].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1070401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL: [OnSucceedAttack] Nakłada 1 Krwawienia
82. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 못 1 부여
   źródło: Skills.json :: dataList[id=1070401].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Nails
   PL: [OnSucceedAttack] Nakłada 1 Gwoździa
83. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 정...화!
   źródło: Skills.json :: dataList[id=1070402].levelList[level=1].name ; dataList[id=1070402].levelList[level=2].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 6 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Puri…fy!
   PL: Pur...yfikacja!
84. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 정신력 3 회복
   źródło: Skills.json :: dataList[id=1070402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Heal 3 SP
   PL: [WinDuel] Odzyskuje 3 Poczytalności
85. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 더하기 코인 약화 1 부여
   źródło: Skills.json :: dataList[id=1070402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Plus Coin Drop next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze 1 Osłabienie Monet Plus
86. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WinDuel] 정신력 5 회복
   źródło: Skills.json :: dataList[id=1070402].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Heal 5 SP
   PL: [WinDuel] Odzyskuje 5 Poczytalności
87. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 더하기 코인 약화 2 부여
   źródło: Skills.json :: dataList[id=1070402].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Plus Coin Drop next turn
   PL: [OnSucceedAttackHead] Nakłada w następnej turze 2 Osłabienia Monet Plus
88. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 미약한 단죄
   źródło: Skills.json :: dataList[id=1070403].levelList[level=3].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Infirm Retribution
   PL: Słaby Odwet
89. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 피해량 10% 만큼 추가 피해
   źródło: Skills.json :: dataList[id=1070403].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Deal bonus damage by 10% of damage dealt
   PL: [OnSucceedAttackHead] Zadaje dodatkowe obrażenia równe 10% zadanych obrażeń
90. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 피해량 10% 만큼 추가 피해
   źródło: Skills.json :: dataList[id=1070403].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 피해량 10% 만큼 추가 피해
   źródło: Skills.json :: dataList[id=1070403].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1070404].levelList[level=1].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Guard
   PL: Blok
93. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Envy) — nazwa] 젠장...
   źródło: Passives.json :: dataList[id=1070401].name
   limit: do 40 znaków
   EN: Bugger…
   PL: Dziadostwo...
94. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Envy) — opis] 아군이 사망하면 다음 턴 시작 시 정신력이 10 감소하고, 타격 위력 증가 1을 얻음
   źródło: Passives.json :: dataList[id=1070401].desc
   limit: do 120 znaków
   EN: When an ally is defeated, lose 10 SP and gain 1 Blunt Power Up next turn.
   PL: Gdy sojusznik ginie, na początku następnej tury traci 10 Poczytalności i zyskuje 1 Wzrostu Mocy Uderzenia.
95. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 독경
   źródło: Passives.json :: dataList[id=1070421].name
   limit: do 40 znaków
   EN: Cantillation
   PL: Recytacja
96. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 속도가 가장 빠른 아군 1명의 못 부여 값 +1
   źródło: Passives.json :: dataList[id=1070421].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed inflicts +1 Nails.
   PL: 1 Sojusznik z najwyższą Szybkością nakłada o 1 więcej Gwoździa.

## [000] Lobotomy E.G.O:: Sunshower — Heathcliff — 로보토미 E.G.O:: 여우비
- ID Tożsamości: `10705` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 2 · HP bazowe: 86 · szybkość: 2–4 / 2–5 / 3–5 / 3–5
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Sinking, Rupture

97. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n여우비
   źródło: Personalities.json :: dataList[id=10705].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::\nSunshower
   PL: Lobotomy E.G.O::\nLisi Deszcz
98. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10705].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10705].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Karta Tożsamości — opis] 히스클리프의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10705].desc
   limit: do 120 znaków
   EN: Heathcliff’s 5th Identity
   PL: Piąta Tożsamość Heathcliffa
101. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 우산후리기
   źródło: Skills.json :: dataList[id=1070501].levelList[level=1].name ; dataList[id=1070501].levelList[level=2].name ; dataList[id=1070501].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 6 · monety: 3 (−2)
   limit: do 40 znaków
   EN: Umbrella Thwack
   PL: Ciach Parasolem
102. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1070501].levelList[level=1].desc ; dataList[id=1070501].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Gain +1 [Sinking] Count
   PL: [WhenUse] Zwiększa własny Licznik [Sinking] o 1
103. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1070501].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] Nakłada 1 Zatonięcia
104. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackTail] 침잠 횟수 1 증가
   źródło: Skills.json :: dataList[id=1070501].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Sinking]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackTail] Inflict +1 [Sinking] Count
   PL: [OnSucceedAttackTail] Zwiększa własny Licznik [Sinking] o 1
105. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1070501].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1070501].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] Nakłada 2 Zatonięcia
106. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttackTail] 침잠 횟수 2 증가
   źródło: Skills.json :: dataList[id=1070501].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1070501].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [Sinking]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackTail] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttackTail] Zwiększa własny Licznik [Sinking] o 2
107. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 침잠 횟수 1 증가\n[DefeatDuel] 침잠 3 얻음
   źródło: Skills.json :: dataList[id=1070501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Gain +1 [Sinking] Count\n[DefeatDuel] Gain 3 [Sinking]
   PL: [WhenUse] Zwiększa własny Licznik [Sinking] o 1\n[DefeatDuel] Zyskuje 3 [Sinking]
108. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 진창다지기
   źródło: Skills.json :: dataList[id=1070502].levelList[level=1].name ; dataList[id=1070502].levelList[level=2].name ; dataList[id=1070502].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 10 · monety: 4 (−3)
   limit: do 40 znaków
   EN: Puddle Stomp
   PL: Udeptanie Bagna
109. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [WhenUse] 자신의 정신력이 -15 미만일 때 최종 위력 +2
   źródło: Skills.json :: dataList[id=1070502].levelList[level=1].desc ; dataList[id=1070502].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] When below -15 SP, Final Power +2
   PL: [WhenUse] Przy Poczytalności niższej niż -15 Moc Końcowa +2
110. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackTail] 파열 2 부여
   źródło: Skills.json :: dataList[id=1070502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 2 Rupture
   PL: [OnSucceedAttackTail] Nakłada 2 Rozdarcia
111. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackTail] 파열 2 부여
   źródło: Skills.json :: dataList[id=1070502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttackTail] 진동 폭발
   źródło: Skills.json :: dataList[id=1070502].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttackTail] Trigger [VibrationExplosion]
   PL: [OnSucceedAttackTail] Wywołuje [VibrationExplosion]
113. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackTail] 파열 3 부여
   źródło: Skills.json :: dataList[id=1070502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 3 Rupture
   PL: [OnSucceedAttackTail] Nakłada 3 Rozdarcia
114. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttackTail] 파열 3 부여
   źródło: Skills.json :: dataList[id=1070502].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1070502].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 4, efekt 1 — opis] 자신의 침잠 5를 소모하여 피해량 +20%
   źródło: Skills.json :: dataList[id=1070502].levelList[level=2].coinlist[#3].coindescs[#0].desc ; dataList[id=1070502].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Spend 5 [Sinking] to deal +20% damage
   PL: Zużywa 5 [Sinking], aby zadać +20% obrażeń
116. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 4, efekt 2 — opis] [OnSucceedAttackTail] 진동 폭발
   źródło: Skills.json :: dataList[id=1070502].levelList[level=2].coinlist[#3].coindescs[#1].desc ; dataList[id=1070502].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 정신력이 -15 미만일 때 최종 위력 +3\n[WhenUse] 자신의 정신력이 -25 미만일 때 최종 위력 +2
   źródło: Skills.json :: dataList[id=1070502].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] When below -15 SP, Final Power +3\n[WhenUse] When below -25 SP, Final Power +2
   PL: [WhenUse] Przy Poczytalności niższej niż -15 Moc Końcowa +3\n[WhenUse] Przy Poczytalności niższej niż -25 Moc Końcowa +2
118. [Umiejętność 3 (×1) (ulepszenie 1) — nazwa] 퍼져라!
   źródło: Skills.json :: dataList[id=1070503].levelList[level=1].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 18 · monety: 3 (−7)
   limit: do 40 znaków
   EN: Spread Out!
   PL: Rozproszcie się!
119. [Umiejętność 3 (×1) (ulepszenie 1) — opis] [WhenUse] 침잠 6을 얻고, 자신의 침잠 횟수 3 증가
   źródło: Skills.json :: dataList[id=1070503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Gain 6 [Sinking] and +3 [Sinking] Count
   PL: [WhenUse] Zyskuje 6 [Sinking] i zwiększa własny Licznik [Sinking] o 3
120. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 다음 턴에 마비 1 부여
   źródło: Skills.json :: dataList[id=1070503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 1 Paralyze next turn
   PL: [OnSucceedAttackTail] Nakłada w następnej turze 1 Paraliżu
121. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills.json :: dataList[id=1070503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Rupture
   PL: [OnSucceedAttack] Nakłada 5 Rozdarcia
122. [Umiejętność 3 (×1) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttackTail] 다음 턴에 취약 1 부여
   źródło: Skills.json :: dataList[id=1070503].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Inflict 1 Fragile next turn
   PL: [OnSucceedAttackTail] Nakłada w następnej turze 1 Wrażliwości
123. [Obrona (ulepszenia 1,4) — nazwa] 경고
   źródło: Skills.json :: dataList[id=1070504].levelList[level=1].name ; dataList[id=1070504].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 10 · monety: 2 (−5)
   limit: do 40 znaków
   EN: Warning
   PL: Ostrzeżenie
124. [Obrona (ulepszenie 1) — opis] [WhenUse] 침잠 3 얻음
   źródło: Skills.json :: dataList[id=1070504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Gain 3 [Sinking]
   PL: [WhenUse] Zyskuje 3 [Sinking]
125. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackTail] 다음 턴에 마비 1을 얻음
   źródło: Skills.json :: dataList[id=1070504].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1070504].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackTail]
   znaczenie tagów: [OnSucceedAttackTail] = [뒷면 적중시] / [Tails Hit]
   EN: [OnSucceedAttackTail] Gain 1 Paralyze next turn
   PL: [OnSucceedAttackTail] Zyskuje w następnej turze 1 Paraliżu
126. [Obrona (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 침잠 5 부여
   źródło: Skills.json :: dataList[id=1070504].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1070504].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking]
   PL: [OnSucceedAttack] Nakłada 5 [Sinking]
127. [Obrona (ulepszenia 1,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills.json :: dataList[id=1070504].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1070504].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Obrona (ulepszenie 4) — opis] [WhenUse] 침잠 5 얻음
   źródło: Skills.json :: dataList[id=1070504].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Gain 5 [Sinking]
   PL: [WhenUse] Zyskuje 5 [Sinking]
129. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 눈물비
   źródło: Passives.json :: dataList[id=1070501].name
   limit: do 40 znaków
   EN: Rain of Tears
   PL: Deszcz Łez
130. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 전투 시작 시 침잠 횟수를 1 소모하여 침잠 만큼 정신력 감소\n피격 전 자신의 침잠 만큼 보호를 얻음.(턴 당 획득 가능한 보호 : 최대 5)\n피격 시 다음 턴에 타격 피해량 증가 1을 얻음 (턴 당 최대 3)
   źródło: Passives.json :: dataList[id=1070501].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the combat phase, spend 1 Sinking Count and lose SP by the current amount of Sinking.\nBefore being hit by an attack, gain Protection equal to this unit's Sinking. (Up to 5 Protection can be gained per turn)\nWhen hit, gain 1 Blunt DMG Up next turn. (3 per turn)
   PL: Na początku walki zużywa 1 Licznika [Sinking] i traci Poczytalność równą Mocy [Sinking]\nPrzy nadchodzącym trafieniu zyskuje Ochronę równą Mocy [Sinking]. (maks. 5 Ochrony na turę)\nPrzy trafieniu zyskuje 1 Wzrostu Obrażeń Uderzenia w następnej turze (maks. 3 razy na turę)
131. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — nazwa] 해진 우산
   źródło: Passives.json :: dataList[id=1070521].name
   limit: do 40 znaków
   EN: Ragged Umbrella
   PL: Zniszczony Parasol
132. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — opis] 정신력이 가장 낮은 아군 1명이 피격 시 정신력 10 감소하고, 다음 턴에 타격 피해량 증가 1을 얻음 (턴 당 1회 발동)
   źródło: Passives.json :: dataList[id=1070521].desc
   limit: do 150 znaków
   EN: 1 ally with the least SP loses 10 SP when hit by an attack and gains 1 Blunt DMG Up next turn. (Once per turn)
   PL: 1 Sojusznik z najniższą Poczytalnością przy trafieniu traci 10 Poczytalności i zyskuje 1 Wzrostu Obrażeń Uderzenia w następnej turze (1 raz na turę)

## [00] Seven Assoc. South Section 4 — Heathcliff — 남부 세븐 협회 4과
- ID Tożsamości: `10706` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 76 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Rupture

133. [Karta Tożsamości — tytuł] 남부 세븐 협회\n4과
   źródło: Personalities.json :: dataList[id=10706].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Seven Assoc.\nSouth Section 4
   PL: Południowe Stowarzyszenie Seven\nSekcja 4
134. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10706].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10706].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Karta Tożsamości — opis] 히스클리프의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10706].desc
   limit: do 120 znaków
   EN: Heathcliff’s 6th Identity
   PL: Szósta Tożsamość Heathcliffa
137. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 직감
   źródło: Skills.json :: dataList[id=1070601].levelList[level=1].name ; dataList[id=1070601].levelList[level=2].name ; dataList[id=1070601].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Intuition
   PL: Intuicja
138. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Rupture
   PL: [OnSucceedAttackHead] Nakłada 1 Rozdarcia
139. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1070601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>이 6  이상일 때 코인 위력 +1
   źródło: Skills.json :: dataList[id=1070601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>
   EN: If target has 6+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u>, Coin Power +1
   PL: Jeżeli cel ma 6+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rozdarcia</link></u></color>, Moc Monet +1
143. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070601].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070601].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 뒷수습
   źródło: Skills.json :: dataList[id=1070602].levelList[level=1].name ; dataList[id=1070602].levelList[level=2].name ; dataList[id=1070602].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 6 · monety: 1 (+10)
   limit: do 40 znaków
   EN: The Wrap-up
   PL: Dokończenie Roboty
146. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1070602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 Rupture Count
   PL: [OnSucceedAttack] Zwiększa Licznik Rozdarcia o 2
147. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WinDuel] 파열 횟수 1 증가
   źródło: Skills.json :: dataList[id=1070602].levelList[level=2].desc ; dataList[id=1070602].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Inflict +1 Rupture Count
   PL: [WinDuel] Zwiększa Licznik Rozdarcia o 1
148. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 감소 1 부여
   źródło: Skills.json :: dataList[id=1070602].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Defense Level Down next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Spadku Poziomu Obrony
149. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1070602].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1070602].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 방어 레벨 감소 3 부여
   źródło: Skills.json :: dataList[id=1070602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Defense Level Down next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 3 Spadku Poziomu Obrony
151. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 현장 자료 분석
   źródło: Skills.json :: dataList[id=1070603].levelList[level=3].name ; dataList[id=1070603].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Forensics
   PL: Analiza Dowodów z Miejsca
152. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 횟수 3 증가
   źródło: Skills.json :: dataList[id=1070603].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1070603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Rupture Count
   PL: [OnSucceedAttack] Zwiększa Licznik Rozdarcia o 3
153. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070603].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1070603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070603].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1070603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1070603].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1070603].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [EnemyKill] 현재 파열 횟수가 가장 낮은 적 1명의 파열 횟수 2 증가
   źródło: Skills.json :: dataList[id=1070603].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1070603].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Inflict +2 Rupture Count against the enemy that has the least Rupture Count
   PL: [EnemyKill] Zwiększa Licznik Rozdarcia o 2 u 1 wroga z najniższym Licznikiem Rozdarcia
157. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 <sprite name="Burst"><color=#e30000><u><link="Burst">파열</color></link></u>이 6 이상일 때 코인 위력 +1
   źródło: Skills.json :: dataList[id=1070603].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Burst">, <color=#e30000>, <u>, <link="Burst">, </color>, </link>, </u>
   EN: If target has 6+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rupture</color></link></u>, Coin Power +1
   PL: Jeżeli cel ma 6+ <sprite name="Burst"><color=#e30000><u><link="Burst">Rozdarcia</link></u></color>, Moc Monet +1
158. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1070604].levelList[level=1].name
   kontekst: grzech: Wrath · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — nazwa] 본능적 간파
   źródło: Passives.json :: dataList[id=1070601].name
   limit: do 40 znaków
   EN: Instinctive Read
   PL: Instynktowne Wyczucie
160. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — opis] 상대의 취약 속성(내성 1.5 초과) 으로 공격 시 스킬로 부여하는 파열 부여 값 +1
   źródło: Passives.json :: dataList[id=1070601].desc
   limit: do 170 znaków
   EN: When attacking a target with a damage type the target is "Fatal" (Resistance>x1.5) to, inflict +1 more Rupture with Skill effects
   PL: Atakując rodzajem obrażeń, na który cel jest Wrażliwy (Odporność powyżej 1.5), nakłada o 1 więcej Rozdarcia efektami Umiejętności
161. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — podsumowanie] 취약 속성으로 공격 시 파열 부여 값 +1
   źródło: Passives.json :: dataList[id=1070601].summary
   limit: do 120 znaków
   EN: When attacking a target with a damage type the target is Fatal to, inflict +1 more Rupture
   PL: Atakując rodzajem obrażeń, na który cel jest Wrażliwy, nakłada o 1 więcej Rozdarcia
162. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 본능적 간파
   źródło: Passives.json :: dataList[id=1070611].name
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — opis] 상대의 취약 속성(내성 1.5 초과) 으로 공격 시 스킬로 부여하는 파열 부여 값 +1\n<style="highlight">전투 시작 시 생존한 아군 세븐 협회 해결사가 자신 포함 4명 이상 있으면, 위 효과의 파열 부여 값 +1</style>
   źródło: Passives.json :: dataList[id=1070611].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n
   EN: When attacking a target with a damage type the target is "Fatal" (Resistance>x1.5) to, inflict +1 more Rupture with Skill effects\n<style="highlight">If 4 or more surviving units, including this unit, are Seven Association Fixers, additional +1 more Rupture</style>
   PL: Atakując rodzajem obrażeń, na który cel jest Wrażliwy (Odporność powyżej 1.5), nakłada o 1 więcej Rozdarcia efektami Umiejętności\n<style="highlight">Na początku walki, jeżeli jest 4 lub więcej ocalałych Fikserów Stowarzyszenia Seven łącznie z tą jednostką, powyższy efekt nakłada o 1 więcej Rozdarcia</style>
164. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — podsumowanie] 취약 속성으로 공격 시 파열 부여 값 +1\n아군 세븐 협회 해결사가 4명 이상이면, 추가로 +1
   źródło: Passives.json :: dataList[id=1070611].summary
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When attacking a target with a damage type the target is Fatal to, inflict +1 more Rupture\nWith 4 or more Seven Association Fixer allies, additional +1 more Rupture
   PL: Atakując rodzajem obrażeń, na który cel jest Wrażliwy, nakłada o 1 więcej Rozdarcia\nPrzy 4+ Fikserach Stowarzyszenia Seven wśród sojuszników nakłada dodatkowo o 1 więcej Rozdarcia
165. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 단서 연결
   źródło: Passives.json :: dataList[id=1070621].name
   limit: do 40 znaków
   EN: Connect The Dots
   PL: Połączenie Poszlak
166. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 최대 체력이 가장 많은 아군 1명이 상대의 취약 속성(내성 1.5 초과)으로 공격 시 스킬로 부여하는 파열 부여 값 +1
   źródło: Passives.json :: dataList[id=1070621].desc
   limit: do 220 znaków
   EN: 1 ally that has the highest Max HP inflicts +1 more Rupture with Skill effects when attacking a target with a damage type that the target is "Fatal"(Resistance>x1.5) to
   PL: 1 Sojusznik z najwyższym Maks. HP, atakując rodzajem obrażeń, na który cel jest Wrażliwy (Odporność powyżej 1.5), nakłada o 1 więcej Rozdarcia efektami Umiejętności
167. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — podsumowanie] 최대 체력이 가장 많은 아군 1명이 취약 속성으로 공격 시 파열 부여 값 +1
   źródło: Passives.json :: dataList[id=1070621].summary
   limit: do 150 znaków
   EN: 1 ally that has the highest Max HP inflicts +1 more Rupture when attacking with a damage type the target is Fatal to
   PL: 1 Sojusznik z najwyższym Maks. HP, atakując rodzajem obrażeń, na który cel jest Wrażliwy, nakłada o 1 więcej Rozdarcia
168. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 단서 연결
   źródło: Passives.json :: dataList[id=1070631].name
   (powtórzenie elementu 165 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Glut.) — opis] 최대 체력이 가장 많은 아군 1명이 상대의 취약 속성(내성 1.5 초과)으로 공격 시 스킬로 부여하는 파열 부여 값 +1\n<style="highlight">효과를 적용받은 대상이 세븐 협회 해결사면, 위 효과의 파열 부여 값 +1</style>
   źródło: Passives.json :: dataList[id=1070631].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n
   EN: 1 ally that has the highest Max HP inflicts +1 more Rupture with Skill effects when attacking a target with a damage type that the target is "Fatal"(Resistance>x1.5) to\n<style="highlight">If the ally is a Seven Association Fixer, additional +1 more Rupture</style>
   PL: 1 Sojusznik z najwyższym Maks. HP, atakując rodzajem obrażeń, na który cel jest Wrażliwy (Odporność powyżej 1.5), nakłada o 1 więcej Rozdarcia efektami Umiejętności\n<style="highlight">Jeżeli takim sojusznikiem jest Fikser Stowarzyszenia Seven, powyższy efekt nakłada o 1 więcej Rozdarcia</style>
170. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Glut.) — podsumowanie] 최대 체력이 가장 많은 아군 1명이 취약 속성으로 공격 시 파열 부여 값 +1\n대상이 세븐 협회 해결사면, 추가로 +1
   źródło: Passives.json :: dataList[id=1070631].summary
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 1 ally that has the highest Max HP inflicts +1 more Rupture when attacking with a damage type the target is Fatal to\nIf the ally is a Seven Association Fixer, additional +1 more Rupture
   PL: 1 Sojusznik z najwyższym Maks. HP, atakując rodzajem obrażeń, na który cel jest Wrażliwy, nakłada o 1 więcej Rozdarcia\nJeżeli takim sojusznikiem jest Fikser Stowarzyszenia Seven, nakłada dodatkowo o 1 więcej Rozdarcia

## [000] The Pequod Harpooneer — Heathcliff — 피쿼드호 작살잡이
- ID Tożsamości: `10707` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 3 · HP bazowe: 99 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Poise, Bleed

171. [Karta Tożsamości — tytuł] 피쿼드호\n작살잡이
   źródło: Personalities.json :: dataList[id=10707].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Pequod\nHarpooneer
   PL: Pequod\nHarpuonier
172. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10707].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10707].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Karta Tożsamości — opis] 히스클리프의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10707].desc
   limit: do 120 znaków
   EN: Heathcliff's 7th Identity
   PL: Siódma Tożsamość Heathcliffa
175. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 사냥감 추적
   źródło: Skills_personality-07.json :: dataList[id=1070701].levelList[level=1].name ; dataList[id=1070701].levelList[level=2].name ; dataList[id=1070701].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Stalk Prey
   PL: Tropienie Zdobyczy
176. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 호흡 횟수 2 증가\n[WhenUse] 다음 턴에 이 슬롯이 도발치 2을 얻음
   źródło: Skills_personality-07.json :: dataList[id=1070701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Poise Count\n[WhenUse] Gain +2 Aggro to this Skill Slot next turn
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2\n[WhenUse] Prowokacja tego slotu Umiejętności +2 w następnej turze
177. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1070701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed
   PL: [OnSucceedAttackHead] Nakłada 2 Krwawienia
178. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 호흡 횟수 3 증가\n[WhenUse] 다음 턴에 이 슬롯이 도발치 3을 얻음
   źródło: Skills_personality-07.json :: dataList[id=1070701].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +3 Poise Count\n[WhenUse] Gain +3 Aggro to this Skill Slot next turn
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 3\n[WhenUse] Prowokacja tego slotu Umiejętności +3 w następnej turze
179. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1070701].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL: [OnSucceedAttack] Nakłada 2 Krwawienia
180. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 호흡 횟수 4 증가\n[WhenUse] 다음 턴에 이 슬롯이 도발치 5를 얻음
   źródło: Skills_personality-07.json :: dataList[id=1070701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +4 Poise Count\n[WhenUse] Gain +5 Aggro to this Skill Slot next turn
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 4\n[WhenUse] Prowokacja tego slotu Umiejętności +5 w następnej turze
181. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 작살박이
   źródło: Skills_personality-07.json :: dataList[id=1070702].levelList[level=1].name ; dataList[id=1070702].levelList[level=2].name ; dataList[id=1070702].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Snagharpoon
   PL: Zaczepiony Harpun
182. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 2를 얻음
   źródło: Skills_personality-07.json :: dataList[id=1070702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Aggro to this Skill Slot next turn
   PL: [WhenUse] Prowokacja tego slotu Umiejętności +2 w następnej turze
183. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] 대상의 출혈 위력의 1/4만큼 대상의 출혈 횟수 증가 (최대 10)
   źródło: Skills_personality-07.json :: dataList[id=1070702].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1070702].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict Bleed Count equal to 1/4 of Bleed Potency on target (Max 10)
   PL: [CriticalOnSucceedAttack] Zwiększa Licznik Krwawienia celu o 1/4 Mocy Krwawienia celu (maks. 10)
184. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 3을 얻음\n[WhenUse] 대상의 출혈 3당 호흡 1 얻음 (최대 10)
   źródło: Skills_personality-07.json :: dataList[id=1070702].levelList[level=2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +3 Aggro to this Skill Slot next turn\n[WhenUse] Gain 1 Poise for every 3 Bleed on target (Max 10)
   PL: [WhenUse] Prowokacja tego slotu Umiejętności +3 w następnej turze\n[WhenUse] Zyskuje 1 [Breath] za każde 3 Krwawienia celu (maks. 10)
185. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 5를 얻음\n[WhenUse] 대상의 출혈 3당 호흡 1 얻음 (최대 10)
   źródło: Skills_personality-07.json :: dataList[id=1070702].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +5 Aggro to this Skill Slot next turn\n[WhenUse] Gain 1 Poise for every 3 Bleed on target (Max 10)
   PL: [WhenUse] Prowokacja tego slotu Umiejętności +5 w następnej turze\n[WhenUse] Zyskuje 1 [Breath] za każde 3 Krwawienia celu (maks. 10)
186. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] 대상의 출혈 위력의 1/3만큼 대상의 출혈 횟수 증가 (최대 10)
   źródło: Skills_personality-07.json :: dataList[id=1070702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict Bleed Count equal to 1/3 of Bleed Potency on target (Max 10)
   PL: [CriticalOnSucceedAttack] Zwiększa Licznik Krwawienia celu o 1/3 Mocy Krwawienia celu (maks. 10)
187. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 매듭 끊기
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].name ; dataList[id=1070703].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Sever Knot
   PL: Przecięcie Węzła
188. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 질투 공명 3 이상이면 합 위력 +1\n질투 공명 4 이상이면 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 3+ Envy Reson., Clash Power +1\nAt 4+ Envy Reson., Coin Power +1
   PL: Przy 3+ Rezonansie Zazdrości Moc Starcia +1\nPrzy 4+ Rezonansie Zazdrości Moc Monet +1
189. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1070703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 50% 미만이면 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 50%- HP, inflict 1 Bleed
   PL: [OnSucceedAttack] Przy HP poniżej 50% Maks. HP nakłada 1 Krwawienia
191. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1070703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 50% 미만이면 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [CriticalOnSucceedAttack] 크리티컬 피해량 +30%
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] +30% Damage on Critical Hit
   PL: [CriticalOnSucceedAttack] Zadaje +30% obrażeń przy trafieniu krytycznym
194. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 질투 공명 3 이상이면 합 위력 +1\n질투 공명 4 이상이면 코인 위력 +1\n질투 완전 공명 6 이상이면 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 3+ Envy Reson., Clash Power +1\nAt 4+ Envy Reson., Coin Power +1\nAt 6+ Envy A-Reson., Coin Power +1
   PL: Przy 3+ Rezonansie Zazdrości Moc Starcia +1\nPrzy 4+ Rezonansie Zazdrości Moc Monet +1\nPrzy 6+ Pełnym Rezonansie Zazdrości Moc Monet +1
195. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 75% 미만이면 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 75%- HP, inflict 1 Bleed
   PL: [OnSucceedAttack] Przy HP poniżej 75% Maks. HP nakłada 1 Krwawienia
196. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 50% 미만이면 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 75% 미만이면 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 195 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 체력이 최대 체력의 50% 미만이면 출혈 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [CriticalOnSucceedAttack] 크리티컬 피해량 +50%
   źródło: Skills_personality-07.json :: dataList[id=1070703].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] +50% Damage on Critical Hit
   PL: [CriticalOnSucceedAttack] Zadaje +50% obrażeń przy trafieniu krytycznym
200. [Obrona (ulepszenia 1,4) — nazwa] 되갚기
   źródło: Skills_personality-07.json :: dataList[id=1070704].levelList[level=1].name ; dataList[id=1070704].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Payback
   PL: Odwet
201. [Obrona (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 2를 얻음\n[StartBattle] 자신의 [Breath]만큼 [DefenseUp]를 얻음. (최대 10)
   źródło: Skills_personality-07.json :: dataList[id=1070704].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [StartBattle], [Breath], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain +2 Aggro to this Skill Slot next turn\n[StartBattle] Gain [DefenseUp] for every [Breath] on self (Max 10)
   PL: [WhenUse] Prowokacja tego slotu Umiejętności +2 w następnej turze\n[StartBattle] Zyskuje [DefenseUp] równy Mocy własnego [Breath]. (maks. 10)
202. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 5를 얻음\n[StartBattle] 자신의 [Breath]만큼 [DefenseUp]를 얻음. (최대 10)
   źródło: Skills_personality-07.json :: dataList[id=1070704].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [StartBattle], [Breath], [DefenseUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [WhenUse] Gain +5 Aggro to this Skill Slot next turn\n[StartBattle] Gain [DefenseUp] for every [Breath] on self (Max 10)
   PL: [WhenUse] Prowokacja tego slotu Umiejętności +5 w następnej turze\n[StartBattle] Zyskuje [DefenseUp] równy Mocy własnego [Breath]. (maks. 10)
203. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — nazwa] 헤집어진 문신
   źródło: Passives.json :: dataList[id=1070701].name
   limit: do 40 znaków
   EN: Mutilated Tattoos
   PL: Powycierane Tatuaże
204. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — opis] 자신을 포함한 아군이 피격당할 때마다 다음 턴에 [AttackUp] 1, [DefenseUp] 1을 얻는다. (최대 6)\n자신의 체력이 낮아질수록 가하는 피해량이 증가한다.\n- 자신의 잃은 체력 1%당 피해량 0.4% 증가
   źródło: Passives.json :: dataList[id=1070701].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Gain 1 [AttackUp] and 1 [DefenseUp] next turn every time an ally (including this unit) is attacked. (Max 6)\nDeal more damage at less HP.\n- Deal +0.4% damage for every 1% missing HP
   PL: Za każde trafienie sojusznika (łącznie z tą jednostką) zyskuje w następnej turze 1 [AttackUp] i 1 [DefenseUp]. (maks. 6)\nZadaje więcej obrażeń w zależności od brakującego HP.\n- Zadaje +0.4% obrażeń za każde 1% brakującego HP
205. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — podsumowanie] 피격당할 때마다 다음 턴에 [AttackUp] 1, [DefenseUp] 1 얻음. 자신의 체력이 낮아질수록 피해량이 증가
   źródło: Passives.json :: dataList[id=1070701].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Gain 1 [AttackUp] and 1 [DefenseUp] every time this unit is attacked. Deal more damage the less HP this unit has.
   PL: Za każde własne trafienie zyskuje w następnej turze 1 [AttackUp] i 1 [DefenseUp]. Zadaje więcej obrażeń w zależności od brakującego HP.
206. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Envy) — nazwa] 헤집어진 문신
   źródło: Passives.json :: dataList[id=1070711].name
   (powtórzenie elementu 203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Envy) — opis] 자신을 포함한 아군이 피격당할 때마다 다음 턴에 [AttackUp] 1, [DefenseUp] 1을 얻는다. 피격 당한 아군이 피쿼드호 소속인 경우, 대신 2를 얻는다. (최대 9)\n자신의 체력이 낮아질수록 가하는 피해량이 증가한다.\n- 자신의 잃은 체력 1%당 피해량 1% 증가
   źródło: Passives.json :: dataList[id=1070711].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Gain 1 [AttackUp] and 1 [DefenseUp] next turn every time an ally (including this unit) is attacked. Gain 2 of each instead if the ally is from The Pequod. (Max 9)\nDeal more damage the less HP this unit has.\n- Deal +1% damage for every 1% missing HP
   PL: Za każde trafienie sojusznika (łącznie z tą jednostką) zyskuje w następnej turze 1 [AttackUp] i 1 [DefenseUp]. Jeżeli trafiony sojusznik jest z Pequoda, zamiast tego zyskuje po 2. (maks. 9)\nZadaje więcej obrażeń w zależności od brakującego HP.\n- Zadaje +1% obrażeń za każde 1% brakującego HP
208. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Envy) — podsumowanie] 피격당할 때마다 다음 턴에 [AttackUp] 1, [DefenseUp] 1 얻음. 자신의 체력이 낮아질수록 피해량이 증가
   źródło: Passives.json :: dataList[id=1070711].summary
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — nazwa] 절박
   źródło: Passives.json :: dataList[id=1070721].name
   limit: do 40 znaków
   EN: Desperation
   PL: Rozpacz
210. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — opis] 최대 체력이 가장 높은 아군 1명이 자신의 체력이 낮아질수록 <noparse>관통 피해량 증가</noparse>\n- 자신의 잃은 체력 1%당 피해량 0.15% 증가 (최대 15%)
   źródło: Passives.json :: dataList[id=1070721].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n
   EN: 1 ally with the highest max HP deals more Pierce Damage at less HP\n- Deal +0.15% damage for every 1% missing HP (Max 15%)
   PL: 1 Sojusznik z najwyższym Maks. HP zadaje więcej obrażeń Kłuciem w zależności od brakującego HP\n- Zadaje +0.15% obrażeń za każde 1% brakującego HP (maks. 15%)
211. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — podsumowanie] 최대 체력이 가장 높은 아군 1명이 자신의 체력이 낮아질수록 <noparse>관통 피해량 증가</noparse>
   źródło: Passives.json :: dataList[id=1070721].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>
   EN: 1 ally with the highest max HP deals more Pierce Damage at less HP
   PL: 1 Sojusznik z najwyższym Maks. HP zadaje więcej obrażeń Kłuciem w zależności od brakującego HP
212. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Envy) — nazwa] 절박
   źródło: Passives.json :: dataList[id=1070731].name
   (powtórzenie elementu 209 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Envy) — opis] 최대 체력이 가장 높은 아군 1명이 자신의 체력이 낮아질수록 <noparse>관통 피해량 증가</noparse>\n- 자신의 잃은 체력 1%당 피해량 0.3% 증가 (최대 30%)
   źródło: Passives.json :: dataList[id=1070731].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n
   EN: 1 ally with the highest max HP deals more Pierce Damage at less HP\n- Deal +0.3% damage for every 1% missing HP (Max 30%)
   PL: 1 Sojusznik z najwyższym Maks. HP zadaje więcej obrażeń Kłuciem w zależności od brakującego HP\n- Zadaje +0.3% obrażeń za każde 1% brakującego HP (maks. 30%)
214. [Pasywka wsparcia (od ulepszenia 4, posiadane 5× Envy) — podsumowanie] 최대 체력이 가장 높은 아군 1명이 자신의 체력이 낮아질수록 <noparse>관통 피해량 증가</noparse>
   źródło: Passives.json :: dataList[id=1070731].summary
   (powtórzenie elementu 211 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [000] Öufi Assoc. South Section 3 — Heathcliff — 남부 외우피 협회 3과
- ID Tożsamości: `10708` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: — · HP bazowe: 79 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Tremor

215. [Karta Tożsamości — tytuł] 남부 외우피 협회\n3과
   źródło: Personalities.json :: dataList[id=10708].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Öufi Assoc.\nSouth Section 3
   PL: Południowe Stowarzyszenie Öufi\nSekcja 3
216. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10708].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10708].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Karta Tożsamości — opis] 히스클리프의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10708].desc
   limit: do 120 znaków
   EN: Heathcliff's 8th Identity
   PL: Ósma Tożsamość Heathcliffa
219. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 이행 권고
   źródło: Skills_personality-07.json :: dataList[id=1070801].levelList[level=1].name ; dataList[id=1070801].levelList[level=2].name ; dataList[id=1070801].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Execution Advised
   PL: Zalecana Egzekucja
220. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1070801].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1070801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Vibration]
221. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Vibration]이 3 이상이면, 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070801].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 3+ [Vibration], Coin Power +1
   PL: Jeżeli cel ma 3+ [Vibration], Moc Monet +1
222. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Vibration] 3 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-07.json :: dataList[id=1070801].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Coin Power +1 for every 3 [Vibration] on target (Max 2)
   PL: Moc Monet +1 za każde 3 [Vibration] celu (maks. 2)
223. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 마지막 경고
   źródło: Skills_personality-07.json :: dataList[id=1070802].levelList[level=1].name ; dataList[id=1070802].levelList[level=2].name ; dataList[id=1070802].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Final Warning
   PL: Ostateczne Ostrzeżenie
224. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1070802].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1070802].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1070802].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
225. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1070802].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1070802].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Vibration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070802].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 6+ [Vibration], Coin Power +1
   PL: Jeżeli cel ma 6+ [Vibration], Moc Monet +1
227. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Vibration] 6 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-07.json :: dataList[id=1070802].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Coin Power +1 for every 6 [Vibration] on target (Max 2)
   PL: Moc Monet +1 za każde 6 [Vibration] celu (maks. 2)
228. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 집행 선고
   źródło: Skills_personality-07.json :: dataList[id=1070803].levelList[level=3].name ; dataList[id=1070803].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Execution Sentencing
   PL: Wyrok Egzekucji
229. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Vibration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070803].levelList[level=3].desc
   (powtórzenie elementu 226 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070803].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1070803].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]
231. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1070803].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1070803].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 위력과 횟수의 합이 20 이상이면, [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_personality-07.json :: dataList[id=1070803].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1070803].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationCollapse], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] If target has 20+ ([Vibration] + [Vibration] Count), trigger [Switch_Vibration] on target, converting [Vibration] to [VibrationCollapse]
   PL: [OnSucceedAttack] Jeżeli suma Mocy [Vibration] i Licznika [Vibration] celu wynosi 20+, wywołuje [Switch_Vibration] na celu, przekształcając [Vibration] w [VibrationCollapse]
233. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Vibration] 6 당 코인 위력 +1 (최대 2)
   źródło: Skills_personality-07.json :: dataList[id=1070803].levelList[level=4].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Obrona (ulepszenia 1,4) — nazwa] 방해는 금지다
   źródło: Skills_personality-07.json :: dataList[id=1070804].levelList[level=1].name ; dataList[id=1070804].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Do Not Obstruct
   PL: Nie Przeszkadzać
235. [Obrona (ulepszenia 1,4) — opis] 보호막이 있는 동안 피격 시 공격자의 [Vibration] 횟수 1 증가 (이 스킬의 효과는 중복되어 적용되지 않음)
   źródło: Skills_personality-07.json :: dataList[id=1070804].levelList[level=1].desc ; dataList[id=1070804].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: When attacked while this unit has Shield, inflict +1 [Vibration] Count on the attacker (this Skill's effect does not stack with multiple uses)
   PL: Przy trafieniu w posiadaniu Tarczy zwiększa Licznik [Vibration] atakującego o 1 (efekt tej Umiejętności nie kumuluje się przy wielokrotnym użyciu)
236. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — nazwa] 엄중한 입회
   źródło: Passives.json :: dataList[id=1070801].name
   limit: do 40 znaków
   EN: Grave Attendance
   PL: Uroczysta Asysta
237. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Pride) — opis] 대상의 [Vibration] 위력 6 당 피해량 +5% (최대 15%)
   źródło: Passives.json :: dataList[id=1070801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Deal +5% damage for every 6 [Vibration] Potency on target (Max 15%)
   PL: Zadaje +5% obrażeń za każde 6 Mocy [Vibration] celu (maks. 15%)
238. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Pride) — nazwa] 엄중한 입회
   źródło: Passives.json :: dataList[id=1070811].name
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Pride) — opis] 대상의 [Vibration] 위력 6 당 피해량 +10% (최대 30%)\n자신의 스킬 효과로 [VibrationCollapse] 변환 시 대상에게 [VibrationExplosion] 발동
   źródło: Passives.json :: dataList[id=1070811].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [VibrationCollapse], [VibrationExplosion]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: Deal +10% damage for every 6 [Vibration] Potency on target (Max 30%)\nWhen converting [Vibration] into [VibrationCollapse] with this unit's Skill effects, trigger [VibrationExplosion] on target
   PL: Zadaje +10% obrażeń za każde 6 Mocy [Vibration] celu (maks. 30%)\nGdy przekształca [Vibration] w [VibrationCollapse] efektami własnych Umiejętności, wywołuje [VibrationExplosion] na celu
240. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Pride) — nazwa] 의무 이행 확인
   źródło: Passives.json :: dataList[id=1070821].name
   limit: do 50 znaków
   EN: Verify Obligation Fulfillment
   PL: Weryfikacja Wykonania Obowiązku
241. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Pride) — opis] 속도가 가장 빠른 아군 1명의 [Vibration] 위력, 횟수를 부여하는 스킬의 합 위력 +1
   źródło: Passives.json :: dataList[id=1070821].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: To 1 ally with the fastest Speed: Clash Power +1 to Skills that apply [Vibration] Potency or Count
   PL: 1 Sojusznik z najwyższą Szybkością: Moc Starcia +1 Umiejętnościom nakładającym [Vibration] Mocy lub Licznika

## [00] MultiCrack Office Fixer — Heathcliff — 멀티크랙 사무소 해결사
- ID Tożsamości: `10709` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 4 · HP bazowe: 71 · szybkość: 3–5 / 3–6 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Charge

242. [Karta Tożsamości — tytuł] 멀티크랙 사무소\n해결사
   źródło: Personalities.json :: dataList[id=10709].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: MultiCrack Office\nFixer
   PL: Biuro MultiCrack\nFikser
243. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10709].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10709].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Karta Tożsamości — opis] 히스클리프의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10709].desc
   limit: do 120 znaków
   EN: Heathcliff's 9th Identity
   PL: Dziewiąta Tożsamość Heathcliffa
246. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 40S-2 가동
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=1].name ; dataList[id=1070901].levelList[level=2].name ; dataList[id=1070901].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: 40S-2 Activation
   PL: Aktywacja 40S-2
247. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수를 5 소모하여 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Coin Power +1
   PL: [WhenUse] Zużywa 5 Licznika [Charge], aby zyskać Moc Monet +1
248. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o 2
249. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] [WhenUse] [Charge] 횟수를 5 소모하여 코인 위력 +1<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=2].desc ; dataList[id=1070901].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Consume 5 [Charge] Count to gain Coin Power +1<style="highlight"></style>
   PL: [WhenUse] Zużywa 5 Licznika [Charge], aby zyskać Moc Monet +1<style="highlight"></style>
250. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 자신의 [Charge] 횟수 2 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: <style="highlight">[OnSucceedAttack] Gain +2 [Charge] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Zwiększa własny Licznik [Charge] o 2</style>
251. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1070901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +2 [Charge] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o 2<style="highlight"></style>
252. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 광전 표식
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=1].name ; dataList[id=1070902].levelList[level=2].name ; dataList[id=1070902].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Photoelectric Mark
   PL: Znak Fotoelektryczny
254. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면, 최대 체력의 2 x (10 - 현재 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수가 10으로 증가\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power +1
   PL: [WhenUse] Jeżeli Licznik [Charge] wynosi od 5 do 9, zużywa HP równe 2 x (10 - Licznik [Charge])% Maks. HP, aby zwiększyć Licznik [Charge] do 10\n[WhenUse] Zużywa 10 Licznika [Charge], aby zyskać Moc Monet +1
255. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge]만큼 [PhotoElectricity] 부여 (최대 2)
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [PhotoElectricity]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [PhotoElectricity] = 광전 / Photoelectricity
   EN: [OnSucceedAttack] Inflict [PhotoElectricity] equal to [Charge] (max 2)
   PL: [OnSucceedAttack] Nakłada [PhotoElectricity] równy wartości [Charge] (maks. 2)
256. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면, 최대 체력의 2 x (10 - 현재 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수가 10으로 증가\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 +1<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power +1<style="highlight"></style>
   PL: [WhenUse] Jeżeli Licznik [Charge] wynosi od 5 do 9, zużywa HP równe 2 x (10 - Licznik [Charge])% Maks. HP, aby zwiększyć Licznik [Charge] do 10\n[WhenUse] Zużywa 10 Licznika [Charge], aby zyskać Moc Monet +1<style="highlight"></style>
257. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Charge] 횟수를 소모했으면, [DefenseDown] 2 부여</style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: <style="highlight">[OnSucceedAttack] If this unit consumed [Charge] Count, inflict 2 [DefenseDown]</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli zużyła Licznik [Charge], nakłada 2 [DefenseDown]</style>
258. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [TakeHpHealReduce] 1 부여</style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [TakeHpHealReduce]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [TakeHpHealReduce]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [TakeHpHealReduce]</style>
259. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge]만큼 [PhotoElectricity] 부여 (최대 <style="highlight">3</style>)
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [PhotoElectricity]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [PhotoElectricity] = 광전 / Photoelectricity
   EN: [OnSucceedAttack] Inflict [PhotoElectricity] equal to [Charge] (max <style="highlight">3</style>)
   PL: [OnSucceedAttack] Nakłada [PhotoElectricity] równy wartości [Charge] (maks. <style="highlight">3</style>)
260. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면, 최대 체력의 2 x (10 - 현재 [Charge] 횟수)%만큼 체력을 소모하여 [Charge] 횟수가 10으로 증가\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 <style="highlight">+2</style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 5~9 [Charge] Count, consume 2(10 - current [Charge] Count)% HP to raise [Charge] Count to 10\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power <style="highlight">+2</style>
   PL: [WhenUse] Jeżeli Licznik [Charge] wynosi od 5 do 9, zużywa HP równe 2 x (10 - Licznik [Charge])% Maks. HP, aby zwiększyć Licznik [Charge] do 10\n[WhenUse] Zużywa 10 Licznika [Charge], aby zyskać Moc Monet <style="highlight">+2</style>
261. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Charge] 횟수를 소모했으면, [DefenseDown] 2 부여</style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 257 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Charge] 횟수를 소모했으면, [DefenseDown] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] If this unit consumed [Charge] Count, inflict 2 [DefenseDown]<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli zużyła Licznik [Charge], nakłada 2 [DefenseDown]<style="highlight"></style>
263. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [TakeHpHealReduce] <style="highlight">2</style> 부여
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [TakeHpHealReduce]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [TakeHpHealReduce]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [TakeHpHealReduce]
264. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge]만큼 [PhotoElectricity] 부여 (최대 3)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070902].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [PhotoElectricity]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [PhotoElectricity] = 광전 / Photoelectricity
   EN: [OnSucceedAttack] Inflict [PhotoElectricity] equal to [Charge] (max 3)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada [PhotoElectricity] równy wartości [Charge] (maks. 3)<style="highlight"></style>
265. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 광전 작살
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=3].name ; dataList[id=1070903].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 5 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Photoelectric Harpoon
   PL: Fotoelektryczny Harpun
266. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [Charge]이 2 이상이면, 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: At 2+ [Charge], Coin Power +1
   PL: Przy 2+ [Charge] Moc Monet +1
267. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +5 [Charge] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o 5
268. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] ([Charge] x 3)만큼 자신의 [Charge] 횟수 증가 (최대 9)
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] x 3) [Charge] Count (max 9)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o wartość ([Charge] x 3) (maks. 9)
269. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge]만큼 [PhotoElectricity] 부여 (최대 3)
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [PhotoElectricity]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [PhotoElectricity] = 광전 / Photoelectricity
   EN: [OnSucceedAttack] Inflict [PhotoElectricity] equal to [Charge] (max 3)
   PL: [OnSucceedAttack] Nakłada [PhotoElectricity] równy wartości [Charge] (maks. 3)
270. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">[Charge] 2당 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: <style="highlight">Coin Power +1 for every 2 [Charge] on self (max 2)</style>
   PL: <style="highlight">Moc Monet +1 za każde 2 [Charge] (maks. 2)</style>
271. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 <style="highlight">7</style> 증가
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +<style="highlight">7</style> [Charge] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o <style="highlight">7</style>
272. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] ([Charge] x 3)만큼 자신의 [Charge] 횟수 증가 (최대 9)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] x 3) [Charge] Count (max 9)<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o wartość ([Charge] x 3) (maks. 9)<style="highlight"></style>
273. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge]만큼 [PhotoElectricity] 부여 (최대 3)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 [Charge] 2당 [HitTakeDamageUp] 1 부여 (최대 2)</style>
   źródło: Skills_personality-07.json :: dataList[id=1070903].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge], [HitTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [HitTakeDamageUp] = 타격 취약 / Blunt Fragility
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [HitTakeDamageUp] for every 2 [Charge] (max 2)</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [HitTakeDamageUp] za każde 2 [Charge] (maks. 2)</style>
275. [Obrona (ulepszenia 1,4) — nazwa] 충전
   źródło: Skills_personality-07.json :: dataList[id=1070904].levelList[level=1].name ; dataList[id=1070904].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Charge
   PL: Ładowanie
276. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 3 증가 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1070904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +3 [Charge] Count (once per turn)
   PL: [WhenUse] Zwiększa własny Licznik [Charge] o 3 (1 raz na turę)
277. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 [Charge] 횟수 3 증가 (턴 당 <style="highlight">2</style>회)
   źródło: Skills_personality-07.json :: dataList[id=1070904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +3 [Charge] Count (<style="highlight">2 times</style> per turn)
   PL: [WhenUse] Zwiększa własny Licznik [Charge] o 3 (maks. <style="highlight">2</style> razy na turę)
278. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 모델 L37 충전
   źródło: Passives.json :: dataList[id=1070901].name
   limit: do 40 znaków
   EN: Charge Model L37
   PL: Ładowanie Modelu L37
279. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음\n\n턴 종료 시 [Charge]이 2 이상이면, 다음 턴에 [Agility] 1 얻음
   źródło: Passives.json :: dataList[id=1070901].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [Agility]
   znaczenie tagów: [Charge] = 충전 / Charge; [Agility] = 신속 / Haste
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\n\nTurn End: At 2+ [Charge], gain 1 [Agility] next turn
   PL: Za każde łączne zużycie 10 własnego Licznika [Charge] podczas walki zyskuje 1 [Charge]\n\nNa koniec tury przy 2+ [Charge] zyskuje 1 [Agility] w następnej turze
280. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — podsumowanie] [Charge] 횟수 10 소모할 때마다 [Charge] 얻음
   źródło: Passives.json :: dataList[id=1070901].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain [Charge] with every 10 [Charge] Count consumption
   PL: Zyskuje [Charge] za każde zużycie 10 Licznika [Charge]
281. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — nazwa] 모델 L37 충전
   źródło: Passives.json :: dataList[id=1070911].name
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음\n턴 종료 시 [Charge]이 2 이상이면, 다음 턴에 [Agility] 1 얻음\n<style="highlight">턴 종료 시 [Charge]이 3 이상이면, 다음 턴에 [Agility] 1, [ParryingResultUp] 1 추가로 얻음</style>
   źródło: Passives.json :: dataList[id=1070911].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [Agility], [ParryingResultUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [Agility] = 신속 / Haste; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\nTurn End: At 2+ [Charge], gain 1 [Agility] next turn\n<style="highlight">Turn End: At 3+ [Charge], gain 1 additional [Agility] and 1 [ParryingResultUp] next turn</style>
   PL: Za każde łączne zużycie 10 własnego Licznika [Charge] podczas walki zyskuje 1 [Charge]\nNa koniec tury przy 2+ [Charge] zyskuje 1 [Agility] w następnej turze\n<style="highlight">Na koniec tury przy 3+ [Charge] zyskuje dodatkowo 1 [Agility] i 1 [ParryingResultUp] w następnej turze</style>
283. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — podsumowanie] [Charge] 횟수 10 소모할 때마다 [Charge] 얻음
   źródło: Passives.json :: dataList[id=1070911].summary
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Pasywka wsparcia (od ulepszenia 3, posiadane 7× Envy) — nazwa] 충전 모듈 추가
   źródło: Passives.json :: dataList[id=1070921].name
   limit: do 40 znaków
   EN: Charging Module Installation
   PL: Montaż Modułu Ładowania
285. [Pasywka wsparcia (od ulepszenia 3, posiadane 7× Envy) — opis] 편성 순서가 1번인 아군의 [Charge] 횟수 최대치 +5\n(조건 충족 시, 다음 턴 시작 전까지 효과 적용)
   źródło: Passives.json :: dataList[id=1070921].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: #1 Deployed ally: Max [Charge] Count +5\n(When conditions are met, this effect will remain activated until the start of the next turn)
   PL: Licznik [Charge] Sojusznika przydzielonego na 1. pozycji +5\n(Po spełnieniu warunków efekt działa do początku następnej tury)

## [000] Wild Hunt — Heathcliff — 와일드헌트
- ID Tożsamości: `10710` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 4 · HP bazowe: 73 · szybkość: 3–5 / 3–6 / 3–8 / 3–8
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Sinking

286. [Karta Tożsamości — tytuł] 와일드헌트
   źródło: Personalities.json :: dataList[id=10710].title
   limit: do 40 znaków
   EN: Wild Hunt
   PL: Dziki Gon
287. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10710].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10710].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Karta Tożsamości — opis] 히스클리프의 열번째 인격
   źródło: Personalities.json :: dataList[id=10710].desc
   limit: do 120 znaków
   EN: Heathcliff’s 10th Identity
   PL: Dziesiąta Tożsamość Heathcliffa
290. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 참수
   źródło: Skills_personality-07.json :: dataList[id=1071001].levelList[level=1].name ; dataList[id=1071001].levelList[level=2].name ; dataList[id=1071001].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Beheading
   PL: Ścięcie
291. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking]이 8 이상이면 합 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1071001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 8+ [Sinking], Clash Power +1
   PL: [WhenUse] Jeżeli cel ma 8+ [Sinking], Moc Starcia +1
292. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071001].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1071001].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] Nakłada 2 [Sinking]
293. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상의 [Sinking]이 6 이상이면 합 위력 +1\n<style="highlight">[WhenUse] 대상의 [Sinking] 횟수 3 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-07.json :: dataList[id=1071001].levelList[level=2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 6+ [Sinking], Clash Power +1\n<style="highlight">[WhenUse] If target has 3+ [Sinking] Count, Coin Power +1</style>
   PL: [WhenUse] Jeżeli cel ma 6+ [Sinking], Moc Starcia +1\n<style="highlight">[WhenUse] Jeżeli cel ma 3+ Licznika [Sinking], Moc Monet +1</style>
294. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking]이 6 이상이면 합 위력 +1\n[WhenUse] 대상의 [Sinking] 횟수 <style="highlight">3 당</style> 코인 위력 +1 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071001].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 6+ [Sinking], Clash Power +1\n[WhenUse] <style="highlight">Coin Power +1 for every 3 [Sinking] Count on target (max 2)</style>
   PL: [WhenUse] Jeżeli cel ma 6+ [Sinking], Moc Starcia +1\n[WhenUse] <style="highlight">Moc Monet +1 za każde 3 Licznika [Sinking] celu (maks. 2)</style>
295. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">3</style> 부여
   źródło: Skills_personality-07.json :: dataList[id=1071001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Sinking]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Sinking]
296. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 추도 행진
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=1].name ; dataList[id=1071002].levelList[level=2].name ; dataList[id=1071002].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Memorial Procession
   PL: Marsz Pogrzebowy
297. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 대상의 [Sinking]이 5 이상이면 코인 위력 +1\n[EndSkill] 자신에게 [NightPathfinding]이 있으면, 정신력 10 감소
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [EndSkill], [NightPathfinding]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [EndSkill] = [공격 종료시] / [Attack End]; [NightPathfinding] = 듀라한 / Dullahan
   EN: [WhenUse] If target has 5+ [Sinking], Coin Power +1\n[EndSkill] If this unit has [NightPathfinding], lose 10 SP
   PL: [WhenUse] Jeżeli cel ma 5+ [Sinking], Moc Monet +1\n[EndSkill] Jeżeli ma [NightPathfinding], traci 10 Poczytalności
298. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1071002].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1071002].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [WanderingFootsteps] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1071002].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1071002].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [WanderingFootsteps]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [WanderingFootsteps] = 다가오는 파탄 / Impending Ruin
   EN: [OnSucceedAttack] Inflict 2 [WanderingFootsteps] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 2 [WanderingFootsteps]
301. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상의 [Sinking]이 5 이상이면 코인 위력 +1\n<style="highlight">[WhenUse] 자신의 [Coffin] 4 이상이면, 공격 가중치 +1\n[WhenUse] 자신에게 [NightPathfinding]이 있으면, 공격 가중치 +1</style>\n[EndSkill] 자신에게 [NightPathfinding]이 있으면, 정신력 10 감소
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Sinking], [Coffin], [NightPathfinding], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Coffin] = 관 / Coffin; [NightPathfinding] = 듀라한 / Dullahan; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] If target has 5+ [Sinking], Coin Power +1\n<style="highlight">[WhenUse] At 4+ [Coffin], Atk Weight +1\n[WhenUse] If this unit has [NightPathfinding], Atk Weight +1</style>\n[EndSkill] If this unit has [NightPathfinding], lose 10 SP
   PL: [WhenUse] Jeżeli cel ma 5+ [Sinking], Moc Monet +1\n<style="highlight">[WhenUse] Przy 4+ [Coffin] Waga ataku +1\n[WhenUse] Jeżeli ma [NightPathfinding], Waga ataku +1</style>\n[EndSkill] Jeżeli ma [NightPathfinding], traci 10 Poczytalności
302. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Sinking] <style="highlight">5 당</style> 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [Coffin] <style="highlight">4당</style> 공격 가중치 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신에게 [NightPathfinding]이 있으면, 공격 가중치 +1\n[EndSkill] 자신에게 [NightPathfinding]이 있으면, 정신력 10 감소
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=4].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Sinking], [Coffin], [NightPathfinding], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Coffin] = 관 / Coffin; [NightPathfinding] = 듀라한 / Dullahan; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] <style="highlight">Coin Power +1 for every 5 Sinking on target (max 2)</style>\n[WhenUse] <style="highlight">Atk Weight +1 for every 4 [Coffin] on self (max 2)</style>\n[WhenUse] If this unit has [NightPathfinding], Atk Weight +1\n[EndSkill] If this unit has [NightPathfinding], lose 10 SP
   PL: [WhenUse] <style="highlight">Moc Monet +1 za każde 5 [Sinking] celu (maks. 2)</style>\n[WhenUse] <style="highlight">Waga ataku +1 za każde 4 [Coffin] (maks. 2)</style>\n[WhenUse] Jeżeli ma [NightPathfinding], Waga ataku +1\n[EndSkill] Jeżeli ma [NightPathfinding], traci 10 Poczytalności
303. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">3</style> 부여
   źródło: Skills_personality-07.json :: dataList[id=1071002].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 레퀴엠
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=3].name ; dataList[id=1071003].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 6 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Requiem
   PL: Requiem
305. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WinDuel] 정신력 10 회복\n[BeforeUse] 자신에게 [NightPathfinding]이 있으면, '비탄하고, 애탄하며, 파탄하라'로 발동됨\n[WhenUse] 대상의 [Sinking] 6 당 코인 위력 +1 (최대 2)\n자신의 [Coffin] 1당 피해량 +7% (최대 70%)\n[WhenUse] [Coffin] 1 얻음\n[EndSkill] 이 스킬 공격으로 대상 처치시 [Coffin] 2 얻음
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=3].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [BeforeUse], [NightPathfinding], [WhenUse], [Sinking], [Coffin], [EndSkill]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [BeforeUse] = [사용전] / [Before Use]; [NightPathfinding] = 듀라한 / Dullahan; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Coffin] = 관 / Coffin; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WinDuel] Heal 10 SP\n[BeforeUse] If this unit has [NightPathfinding], activate 'Lament, Mourn, and Despair' instead\n[WhenUse] Coin Power +1 for every 6 [Sinking] on target (max 2)\nDeal +7% damage for every [Coffin] on self (max 70%)\n[WhenUse] Gain 1 [Coffin]\n[EndSkill] If this Skill attack kills the target, gain 2 [Coffin]
   PL: [WinDuel] Odzyskuje 10 Poczytalności\n[BeforeUse] Jeżeli ma [NightPathfinding], stosuje się jako „Zalujcie, Opłakujcie, Rozpaczajcie”\n[WhenUse] Moc Monet +1 za każde 6 [Sinking] celu (maks. 2)\nZadaje +7% obrażeń za każde 1 [Coffin] (maks. 70%)\n[WhenUse] Zyskuje 1 [Coffin]\n[EndSkill] Jeżeli atak tej Umiejętności zabija cel, zyskuje 2 [Coffin]
306. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Sinking]
307. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [WanderingFootsteps]이 있으면, [Sinking] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1071003].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [WanderingFootsteps], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [WanderingFootsteps] = 다가오는 파탄 / Impending Ruin; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] If target has [WanderingFootsteps], inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] Jeżeli cel ma [WanderingFootsteps], zwiększa Licznik [Sinking] celu o 2
308. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [EnemyKill] 처치한 대상의 ([Sinking] / 3)만큼 무작위 적 2명에게 [Sinking] 부여 (최대 3)
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Sinking]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Sinking] = 침잠 / Sinking
   EN: [EnemyKill] Inflict ([Sinking] on killed target/3) Sinking on 2 random enemies (max 3)
   PL: [EnemyKill] Nakłada [Sinking] równy ([Sinking] zabitego celu / 3) na 2 losowych wrogów (maks. 3)
310. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WinDuel] 정신력 10 회복\n[BeforeUse] 자신에게 [NightPathfinding]이 있으면, '비탄하고, 애탄하며, 파탄하라'로 발동됨\n[WhenUse] 대상의 [Sinking] <style="highlight">3 당</style> 코인 위력 +1 (최대 <style="highlight">4</style>)\n자신의 [Coffin] 1당 피해량 +12% (최대 120%)\n[WhenUse] [Coffin] 1 얻음\n[EndSkill] 이 스킬 공격으로 대상 처치시 [Coffin] 2 얻음
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=4].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WinDuel], [BeforeUse], [NightPathfinding], [WhenUse], [Sinking], [Coffin], [EndSkill]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [BeforeUse] = [사용전] / [Before Use]; [NightPathfinding] = 듀라한 / Dullahan; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Coffin] = 관 / Coffin; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WinDuel] Heal 10 SP\n[BeforeUse] If this unit has [NightPathfinding], activate 'Lament, Mourn, and Despair' instead\n[WhenUse] Coin Power +1 for <style="highlight">every 3</style> [Sinking] on target (max <style="highlight">4</style>)\nDeal +12% damage for every [Coffin] on self (max 120%)\n[WhenUse] Gain 1 [Coffin]\n[EndSkill] If this Skill attack kills the target, gain 2 [Coffin]
   PL: [WinDuel] Odzyskuje 10 Poczytalności\n[BeforeUse] Jeżeli ma [NightPathfinding], stosuje się jako „Zalujcie, Opłakujcie, Rozpaczajcie”\n[WhenUse] Moc Monet +1 za <style="highlight">każde 3</style> [Sinking] celu (maks. <style="highlight">4</style>)\nZadaje +12% obrażeń za każde 1 [Coffin] (maks. 120%)\n[WhenUse] Zyskuje 1 [Coffin]\n[EndSkill] Jeżeli atak tej Umiejętności zabija cel, zyskuje 2 [Coffin]
311. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">+4</style> [Sinking] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] celu o <style="highlight">4</style>
312. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">3</style> 부여
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [EnemyKill] 처치한 대상의 ([Sinking] / <style="highlight">2</style>)만큼 무작위 적 2명에게 [Sinking] 부여 (최대 <style="highlight">5</style>)
   źródło: Skills_personality-07.json :: dataList[id=1071003].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EnemyKill], [Sinking]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Sinking] = 침잠 / Sinking
   EN: [EnemyKill] Inflict ([Sinking] on killed target/<style="highlight">2</style>) Sinking on 2 random enemies (max <style="highlight">5</style>)
   PL: [EnemyKill] Nakłada [Sinking] równy ([Sinking] zabitego celu / <style="highlight">2</style>) na 2 losowych wrogów (maks. <style="highlight">5</style>)
314. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 비탄하고, 애탄하며, 파탄하라
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].name ; dataList[id=1071005].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 31 · monety: 2 (−13)
   limit: do 40 znaków
   EN: Lament, Mourn, and Despair
   PL: Zalujcie, Opłakujcie, Rozpaczajcie
315. [Umiejętność 4 (×0) (ulepszenie 3) — opis] [WhenUse] 정신력 15 감소\n[WhenUse] 대상의 [Sinking] 5 당 기본 위력 +1 (최대 2)\n[WhenUse] 자신의 정신력이 낮을수록 피해량이 증가 (정신력 1당 +0.3%, 최대 21%)\n자신의 [Coffin] 1당 피해량 +7% (최대 70%)\n자신의 [NightPathfinding] 1당 피해량 +10% (최대 30%)\n[WhenUse] [Coffin] 1 얻음\n[EndSkill] 이 스킬 공격으로 대상 처치시 [Coffin] 2 얻음\n[EndSkill] 정신력이 0 미만이면, 정신력 10 회복. 정신력이 0보다 낮을수록 회복량 증가 (차이 1당 1 회복, 최대 25)\n[EndBattle] [NightPathfinding] 제거
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Sinking], [Coffin], [NightPathfinding], [EndSkill], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Coffin] = 관 / Coffin; [NightPathfinding] = 듀라한 / Dullahan; [EndSkill] = [공격 종료시] / [Attack End]; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [WhenUse] Lose 15 SP\n[WhenUse] Base Power +1 for every 5 [Sinking] on target (max 2)\n[WhenUse] Deal more damage the further this unit's SP value is from 45 (+0.3% damage for every missing SP, max 21%)\nDeal +7% damage for every [Coffin] on self (max 70%)\nDeal +10% damage for every [NightPathfinding] on self (max 30%)\n[WhenUse] Gain 1 [Coffin]\n[EndSkill] If this Skill attack kills the target, gain 2 [Coffin]\n[EndSkill] At less than 0 SP, heal 10 SP. When at less than 0 SP, heal more SP the further this unit's SP value is from 0 (heal 1 additional SP for every missing SP; max 25)\n[EndBattle] Lose [NightPathfinding]
   PL: [WhenUse] Traci 15 Poczytalności\n[WhenUse] Moc Bazowa +1 za każde 5 [Sinking] celu (maks. 2)\n[WhenUse] Im niższa Poczytalność, tym więcej obrażeń (+0.3% za każde 1 Poczytalności, maks. 21%)\nZadaje +7% obrażeń za każde 1 [Coffin] (maks. 70%)\nZadaje +10% obrażeń za każde 1 [NightPathfinding] (maks. 30%)\n[WhenUse] Zyskuje 1 [Coffin]\n[EndSkill] Jeżeli atak tej Umiejętności zabija cel, zyskuje 2 [Coffin]\n[EndSkill] Przy Poczytalności niższej niż 0 odzyskuje 10 Poczytalności. Im niższa Poczytalność poniżej 0, tym większy odzysk (1 odzysku za każde 1 różnicy; maks. 25)\n[EndBattle] Traci [NightPathfinding]
316. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여, [Sinking] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking] and +1 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada 3 [Sinking] i zwiększa Licznik [Sinking] o 1
317. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상 입힘
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise the target's Stagger Threshold by 20% of damage dealt
   PL: [OnSucceedAttack] Podnosi Próg Oszołomienia celu o 20% zadanych obrażeń
318. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 우울 속성 피해를 줌 (최대 15)
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict Gloom Affinity damage equal to [Sinking] on target (max 15)
   PL: [OnSucceedAttack] Zadaje obrażenia atrybutu Posępności równe wartości [Sinking] celu (maks. 15)
319. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 2 — opis] [EnemyKill] 처치한 대상의 ([Sinking] / 3)만큼 무작위 적 2명에게 [Sinking] 부여 (최대 4)
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Sinking]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Sinking] = 침잠 / Sinking
   EN: [EnemyKill] Inflict ([Sinking] on killed target/3) Sinking on 2 random enemies (max 4)
   PL: [EnemyKill] Nakłada [Sinking] równy ([Sinking] zabitego celu / 3) na 2 losowych wrogów (maks. 4)
320. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 2, efekt 3 — opis] [EnemyKill] 정신력 15 회복
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=1071005].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Heal 15 SP
   PL: [EnemyKill] Odzyskuje 15 Poczytalności
321. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [WhenUse] 정신력 15 감소\n[WhenUse] 대상의 [Sinking] 5 당 기본 위력 +1 (최대 <style="highlight">4</style>)\n[WhenUse] 자신의 정신력이 낮을수록 피해량이 증가 (정신력 1당 +0.3%, 최대 21%)\n자신의 [Coffin] 1당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">100</style>%)\n자신의 [NightPathfinding] 1당 피해량 +<style="highlight">20</style>% (최대 <style="highlight">60</style>%)\n[WhenUse] [Coffin] <style="highlight">2</style> 얻음\n[EndSkill] 이 스킬 공격으로 대상 처치시 [Coffin] <style="highlight">3</style> 얻음\n[EndSkill] 정신력이 0 미만이면, 정신력 10 회복. 정신력이 0보다 낮을수록 회복량 증가 (차이 1당 <style="highlight">2</style> 회복, 최대 <style="highlight">50</style>)\n[EndBattle] [NightPathfinding] 제거
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=4].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Sinking], [Coffin], [NightPathfinding], [EndSkill], [EndBattle]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [Coffin] = 관 / Coffin; [NightPathfinding] = 듀라한 / Dullahan; [EndSkill] = [공격 종료시] / [Attack End]; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [WhenUse] Lose 15 SP\n[WhenUse] Base Power +1 for every 5 [Sinking] on target (max <style="highlight">4</style>)\n[WhenUse] Deal more damage the further this unit's SP value is from 45 (+0.3% damage for every missing SP, max 21%)\nDeal +<style="highlight">10</style>% damage for every [Coffin] on self (max <style="highlight">100</style>%)\nDeal +<style="highlight">20</style>% damage for every [NightPathfinding] on self (max <style="highlight">60</style>%)\n[WhenUse] Gain <style="highlight">2</style> [Coffin]\n[EndSkill] If this Skill attack kills the target, gain <style="highlight">3</style> [Coffin]\n[EndSkill] At less than 0 SP, heal 10 SP. When at less than 0 SP, heal more SP the further this unit's SP value is from 0 (heal <style="highlight">2</style> additional SP for every missing SP; max <style="highlight">50</style>)\n[EndBattle] Lose [NightPathfinding]
   PL: [WhenUse] Traci 15 Poczytalności\n[WhenUse] Moc Bazowa +1 za każde 5 [Sinking] celu (maks. <style="highlight">4</style>)\n[WhenUse] Im niższa Poczytalność, tym więcej obrażeń (+0.3% za każde 1 Poczytalności, maks. 21%)\nZadaje +<style="highlight">10</style>% obrażeń za każde 1 [Coffin] (maks. <style="highlight">100</style>%)\nZadaje +<style="highlight">20</style>% obrażeń za każde 1 [NightPathfinding] (maks. <style="highlight">60</style>%)\n[WhenUse] Zyskuje <style="highlight">2</style> [Coffin]\n[EndSkill] Jeżeli atak tej Umiejętności zabija cel, zyskuje <style="highlight">3</style> [Coffin]\n[EndSkill] Przy Poczytalności niższej niż 0 odzyskuje 10 Poczytalności. Im niższa Poczytalność poniżej 0, tym większy odzysk (<style="highlight">2</style> odzysku za każde 1 różnicy; maks. <style="highlight">50</style>)\n[EndBattle] Traci [NightPathfinding]
322. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">5</style> 부여, [Sinking] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict <style="highlight">5</style> [Sinking] and +2 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada <style="highlight">5</style> [Sinking] i zwiększa Licznik [Sinking] o 2
323. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 <style="highlight">30</style>%만큼 흐트러짐 손상 입힘
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise the target's Stagger Threshold by <style="highlight">30</style>% of damage dealt
   PL: [OnSucceedAttack] Podnosi Próg Oszołomienia celu o <style="highlight">30</style>% zadanych obrażeń
324. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 우울 속성 피해를 줌 (최대 <style="highlight">30</style>)
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict Gloom Affinity damage equal to [Sinking] on target (max <style="highlight">30</style>)
   PL: [OnSucceedAttack] Zadaje obrażenia atrybutu Posępności równe wartości [Sinking] celu (maks. <style="highlight">30</style>)
325. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [EnemyKill] 처치한 대상의 ([Sinking] / <style="highlight">2</style>)만큼 무작위 적 2명에게 [Sinking] 부여 (최대 <style="highlight">8</style>)
   źródło: Skills_personality-07.json :: dataList[id=1071005].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EnemyKill], [Sinking]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Sinking] = 침잠 / Sinking
   EN: [EnemyKill] Inflict ([Sinking] on killed target/<style="highlight">2</style>) Sinking on 2 random enemies (max <style="highlight">8</style>)
   PL: [EnemyKill] Nakłada [Sinking] równy ([Sinking] zabitego celu / <style="highlight">2</style>) na 2 losowych wrogów (maks. <style="highlight">8</style>)
326. [Obrona (ulepszenia 1,3,4) — nazwa] 듀라한이여...!
   źródło: Skills_personality-07.json :: dataList[id=1071004].levelList[level=1].name ; dataList[id=1071004].levelList[level=3].name ; dataList[id=1071004].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: O Dullahan...!
   PL: O Dullahanie...!
327. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] [NightPathfinding]이 없으면, 다음 턴에 [NightPathfinding]을 1 얻음 (턴 당 1회 발동)\n[EndBattle] [NightPathfinding]이 있으면 제거함
   źródło: Skills_personality-07.json :: dataList[id=1071004].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [NightPathfinding], [EndBattle]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [NightPathfinding] = 듀라한 / Dullahan; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [DuelCounter]\n[StartBattle] If this unit does not have [NightPathfinding], gain 1 [NightPathfinding] next turn (once per turn)\n[EndBattle] If this unit has [NightPathfinding], lose [NightPathfinding]
   PL: [DuelCounter]\n[StartBattle] Jeżeli nie ma [NightPathfinding], zyskuje 1 [NightPathfinding] w następnej turze (1 raz na turę)\n[EndBattle] Jeżeli ma [NightPathfinding], traci [NightPathfinding]
328. [Obrona (ulepszenia 1,3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071004].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1071004].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Obrona (ulepszenie 3) — opis] [DuelCounter]\n<style="highlight">[BeforeUse] [NightPathfinding]이 있고 정신력이 15 이상이면, 비탄하고, 애탄하며, 파탄하라로 반격함 (턴 당 1회 발동)</style>\n[StartBattle] [NightPathfinding]이 없으면, 다음 턴에 [NightPathfinding]을 1 얻음 (턴 당 1회 발동)\n<style="highlight">[WhenUse] 대상의 [Sinking]이 6 이상이면, 코인 위력 +1</style>\n[EndBattle] [NightPathfinding]이 있으면 제거함
   źródło: Skills_personality-07.json :: dataList[id=1071004].levelList[level=3].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [BeforeUse], [NightPathfinding], [StartBattle], [WhenUse], [Sinking], [EndBattle]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [BeforeUse] = [사용전] / [Before Use]; [NightPathfinding] = 듀라한 / Dullahan; [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [DuelCounter]\n<style="highlight">[BeforeUse] If this unit has [NightPathfinding] and has 15+ SP, use 'Lament, Mourn, and Despair' as Counter (once per turn)</style>\n[StartBattle] If this unit does not have [NightPathfinding], gain 1 [NightPathfinding] next turn (once per turn)\n<style="highlight">[WhenUse] If target has 6+ [Sinking], Coin Power +1</style>\n[EndBattle] If this unit has [NightPathfinding], lose [NightPathfinding]
   PL: [DuelCounter]\n<style="highlight">[BeforeUse] Jeżeli ma [NightPathfinding] i 15+ Poczytalności, odpowiada Kontrą „Zalujcie, Opłakujcie, Rozpaczajcie” (1 raz na turę)</style>\n[StartBattle] Jeżeli nie ma [NightPathfinding], zyskuje 1 [NightPathfinding] w następnej turze (1 raz na turę)\n<style="highlight">[WhenUse] Jeżeli cel ma 6+ [Sinking], Moc Monet +1</style>\n[EndBattle] Jeżeli ma [NightPathfinding], traci [NightPathfinding]
330. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[BeforeUse] [NightPathfinding]이 있고 정신력이 15 이상이면, '비탄하고, 애탄하며, 파탄하라'로 반격함 (턴 당 1회 발동)\n[StartBattle] [NightPathfinding]이 없으면, 다음 턴에 [NightPathfinding]을 1 얻음 (턴 당 1회 발동)\n[WhenUse] 대상의 [Sinking] <style="highlight">3 당</style> 코인 위력 +1 <style="highlight">(최대 2)</style>\n<style="highlight">[WinDuel] (합 횟수/ 3)만큼 다음 턴에 [AttackUp]를 얻음 (최대 3, 턴 당 1회 발동)</style>\n[EndBattle] [NightPathfinding]이 있으면 제거함
   źródło: Skills_personality-07.json :: dataList[id=1071004].levelList[level=4].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [BeforeUse], [NightPathfinding], [StartBattle], [WhenUse], [Sinking], [WinDuel], [AttackUp], [EndBattle]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [BeforeUse] = [사용전] / [Before Use]; [NightPathfinding] = 듀라한 / Dullahan; [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [WinDuel] = [합 승리시] / [Clash Win]; [AttackUp] = 공격 레벨 증가 / Offense Level Up …
   EN: [DuelCounter]\n[BeforeUse] If this unit has [NightPathfinding] and has 15+ SP, use 'Lament, Mourn, and Despair' as Counter (once per turn)\n[StartBattle] If this unit does not have [NightPathfinding], gain 1 [NightPathfinding] next turn (once per turn)\n[WhenUse] <style="highlight">Coin Power +1 for every 3 [Sinking] on target (max 2)</style>\n<style="highlight">[WinDuel] Gain [AttackUp] next turn equal to (# of Clashes/3) (max 3, once per turn)</style>\n[EndBattle] If this unit has [NightPathfinding], lose [NightPathfinding]
   PL: [DuelCounter]\n[BeforeUse] Jeżeli ma [NightPathfinding] i 15+ Poczytalności, odpowiada Kontrą „Zalujcie, Opłakujcie, Rozpaczajcie” (1 raz na turę)\n[StartBattle] Jeżeli nie ma [NightPathfinding], zyskuje 1 [NightPathfinding] w następnej turze (1 raz na turę)\n[WhenUse] <style="highlight">Moc Monet +1 za każde 3 [Sinking] celu (maks. 2)</style>\n<style="highlight">[WinDuel] Zyskuje w następnej turze [AttackUp] równy (liczba Starć / 3) (maks. 3, 1 raz na turę)</style>\n[EndBattle] Jeżeli ma [NightPathfinding], traci [NightPathfinding]
331. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여<style="highlight">, 침잠 횟수 1 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071004].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] <style="highlight">and +1 [Sinking] Count</style>
   PL: [OnSucceedAttack] Nakłada 2 [Sinking]<style="highlight"> i zwiększa Licznik [Sinking] o 1</style>
332. [Obrona (ulepszenia 3–4) — nazwa] 비탄하고, 애탄하며, 파탄하라
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].name ; dataList[id=1071006].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: kontra · moc bazowa: 31 · monety: 2 (−13)
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [Obrona (ulepszenie 3) — opis] [WhenUse] 정신력 15 감소\n[WhenUse] 대상의 [Sinking] 5 당 기본 위력 +1 (최대 2)\n[WhenUse] 자신의 정신력이 낮을수록 피해량이 증가 (정신력 1당 +0.3%, 최대 21%)\n자신의 [Coffin] 1당 피해량 +7% (최대 70%)\n자신의 [NightPathfinding] 1당 피해량 +10% (최대 30%)\n[WhenUse] [Coffin] 1 얻음\n[EndSkill] 이 스킬 공격으로 대상 처치시 [Coffin] 2 얻음\n[EndSkill] 정신력이 0 미만이면, 정신력 10 회복. 정신력이 0보다 낮을수록 회복량 증가 (차이 1당 1 회복, 최대 25)\n[EndBattle] [NightPathfinding] 제거
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].desc
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Obrona (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여, [Sinking] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Obrona (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상 입힘
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 317 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Obrona (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 우울 속성 피해를 줌 (최대 15)
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Obrona (ulepszenie 3) — moneta 2, efekt 2 — opis] [EnemyKill] 처치한 대상의 ([Sinking] / 3)만큼 무작위 적 2명에게 [Sinking] 부여 (최대 4)
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 319 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Obrona (ulepszenia 3–4) — moneta 2, efekt 3 — opis] [EnemyKill] 정신력 15 회복
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=1071006].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Obrona (ulepszenie 4) — opis] [WhenUse] 정신력 15 감소\n[WhenUse] 대상의 [Sinking] 5 당 기본 위력 +1 (최대 <style="highlight">4</style>)\n[WhenUse] 자신의 정신력이 낮을수록 피해량이 증가 (정신력 1당 +0.3%, 최대 21%)\n자신의 [Coffin] 1당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">100</style>%)\n자신의 [NightPathfinding] 1당 피해량 +<style="highlight">20</style>% (최대 <style="highlight">60</style>%)\n[WhenUse] [Coffin] <style="highlight">2</style> 얻음\n[EndSkill] 이 스킬 공격으로 대상 처치시 [Coffin] <style="highlight">3</style> 얻음\n[EndSkill] 정신력이 0 미만이면, 정신력 10 회복. 정신력이 0보다 낮을수록 회복량 증가 (차이 1당 <style="highlight">2</style> 회복, 최대 <style="highlight">50</style>)\n[EndBattle] [NightPathfinding] 제거
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=4].desc
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] <style="highlight">5</style> 부여, [Sinking] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 322 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Obrona (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 <style="highlight">30</style>%만큼 흐트러짐 손상 입힘
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 323 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 우울 속성 피해를 줌 (최대 <style="highlight">30</style>)
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Obrona (ulepszenie 4) — moneta 2, efekt 2 — opis] [EnemyKill] 처치한 대상의 ([Sinking] / <style="highlight">2</style>)만큼 무작위 적 2명에게 [Sinking] 부여 (최대 <style="highlight">8</style>)
   źródło: Skills_personality-07.json :: dataList[id=1071006].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Pasywka bojowa (od ulepszenia 1) — nazwa] 듀라한
   źródło: Passives.json :: dataList[id=1071002].name
   limit: do 40 znaków
   EN: Dullahan
   PL: Dullahan
345. [Pasywka bojowa (od ulepszenia 1) — opis] - 턴 시작 시 [NightPathfinding]이 있을 때, [NightPathfinding]에 탑승함\n- [NightPathfinding]에 탑승할 때마다 정신력 5 소모\n- 전투 중 사망한 아군이 3명 이상이면, 다음 턴에 [NightPathfinding]을 얻음. (전투당 1번)\n- [NightPathfinding]에 탑승할 때, 피해나 흐트러짐 손상으로 흐트러짐 상태가 된 경우, 흐트러짐 상태를 해제함. 해제할 수 없는 흐트러짐 상태인 경우, [NightPathfinding]에 탑승할 수 없음.\n- 대상 처치 시 관 1 얻음
   źródło: Passives.json :: dataList[id=1071002].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n, [NightPathfinding]
   znaczenie tagów: [NightPathfinding] = 듀라한 / Dullahan
   EN: - Turn Start: if this unit has [NightPathfinding], mount [NightPathfinding].\n- Lose 5 SP every time this unit mounts [NightPathfinding]\n- If 3+ allies have been defeated in this Encounter, gain [NightPathfinding] next turn. (once per Encounter)\n- If this unit gets Staggered due to damage or raised Stagger Threshold when mounting [NightPathfinding], recover from Stagger. If the Stagger is something that cannot be naturally recovered from, this unit does not mount [NightPathfinding].\n\n- Gain 1 Coffin when killing the target.
   PL: - Na początku tury, jeżeli ma [NightPathfinding], dosiada [NightPathfinding]\n- Za każde dosiadanie [NightPathfinding] traci 5 Poczytalności\n- Jeżeli w tej walce zginęło 3 lub więcej sojuszników, zyskuje [NightPathfinding] w następnej turze. (1 raz na walkę)\n- Jeżeli podczas dosiadania [NightPathfinding] zostanie Ogłuszony przez obrażenia albo Podniesienie Progu Oszołomienia, doszodzi z Ogłuszenia. Jeżeli Ogłuszenie nie może ustąpić naturalnie, nie dosiada [NightPathfinding].\n- Przy zabiciu celu zyskuje 1 Trumny
346. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — nazwa] 마왕의 부름
   źródło: Passives.json :: dataList[id=1071001].name
   limit: do 40 znaków
   EN: Call of the Erlking
   PL: Wołanie Erlkinga
347. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — opis] - 대상의 [Sinking] 1당 피해량 +1% (최대 15%)
   źródło: Passives.json :: dataList[id=1071001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: - Deal +1% damage for every 1 [Sinking] on target (max 15%)
   PL: - Zadaje +1% obrażeń za każde 1 [Sinking] celu (maks. 15%)
348. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — podsumowanie] 대상의 [Sinking]당 피해량이 증가
   źródło: Passives.json :: dataList[id=1071001].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Deal more damage based on [Sinking] on target
   PL: Zadaje więcej obrażeń w zależności od [Sinking] celu
349. [Pasywka bojowa (od ulepszenia 3, posiadane 5× Envy) — nazwa] 마왕의 부름
   źródło: Passives.json :: dataList[id=1071011].name
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Pasywka bojowa (od ulepszenia 3, posiadane 5× Envy) — opis] - 대상의 [Sinking] 1당 피해량 +1% (최대 15%)\n\n<style="highlight">- 전투 중 아군 1명이 사망에 이르는 피해를 받았을 때, 관 2를 소모하여 [WildHunt]를 부여 (턴 당 1회)\n\n- 다음 턴에 [WildHunt]를 부여한 인격에게 [AttackDmgUp] 2 부여\n- 워더링하이츠, 에드가 가문 소속이면, 다음 턴에 [Enhancement] 1 추가 부여</style>
   źródło: Passives.json :: dataList[id=1071011].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Sinking], [WildHunt], [AttackDmgUp], [Enhancement]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [WildHunt] = 와일드헌트 / Wild Hunt; [AttackDmgUp] = 피해량 증가 / Damage Up; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: - Deal +1% damage for every 1 [Sinking] on target (max 15%)\n\n<style="highlight">- When, during combat, 1 ally takes damage that would kill them, consume 2 Coffin to apply [WildHunt] to them (once per turn)\n\n- Apply 2 [AttackDmgUp] next turn to the ally that has [WildHunt]\n- If the said ally is from Wuthering Heights or Edgar Family, apply 1 [Enhancement] next turn as well</style>
   PL: - Zadaje +1% obrażeń za każde 1 [Sinking] celu (maks. 15%)\n\n<style="highlight">- Gdy w trakcie walki sojusznik otrzymuje obrażenia śmiertelne, zużywa 2 Trumny, aby nakładać na niego [WildHunt] (1 raz na turę)\n\n- Nakłada w następnej turze 2 [AttackDmgUp] na Tożsamość z [WildHunt]\n- Jeżeli ta Tożsamość jest z Wuthering Heights albo Rodu Edgar, nakłada dodatkowo w następnej turze 1 [Enhancement]</style>
351. [Pasywka bojowa (od ulepszenia 3, posiadane 5× Envy) — podsumowanie] 대상의 [Sinking]당 피해량이 증가
   źródło: Passives.json :: dataList[id=1071011].summary
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Envy) — nazwa] 마왕의 부름
   źródło: Passives.json :: dataList[id=1071012].name
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Envy) — opis] - 대상의 [Sinking] 1당 피해량 +1% (최대 15%)\n\n- 전투 중 아군 1명이 사망에 이르는 피해를 받았을 때, 관 2를 소모하여 [WildHunt]를 부여 (턴 당 <style="highlight">2</style>회)\n\n- 다음 턴에 [WildHunt]를 부여한 인격에게 [AttackDmgUp] 2 부여\n- 워더링하이츠, 에드가 가문 소속이면, 다음 턴에 [Enhancement] 1 추가 부여
   źródło: Passives.json :: dataList[id=1071012].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Sinking], [WildHunt], [AttackDmgUp], [Enhancement]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [WildHunt] = 와일드헌트 / Wild Hunt; [AttackDmgUp] = 피해량 증가 / Damage Up; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: - Deal +1% damage for every 1 [Sinking] on target (max 15%)\n\n- When, during combat, 1 ally takes damage that would kill them, consume 2 Coffin to apply [WildHunt] to them (<style="highlight">2 times</style> per turn)\n\n- Apply 2 [AttackDmgUp] next turn to the ally that has [WildHunt]\n- If the said ally is from Wuthering Heights or Edgar Family, apply 1 [Enhancement] next turn as well
   PL: - Zadaje +1% obrażeń za każde 1 [Sinking] celu (maks. 15%)\n\n- Gdy w trakcie walki sojusznik otrzymuje obrażenia śmiertelne, zużywa 2 Trumny, aby nakładać na niego [WildHunt] (maks. <style="highlight">2</style> razy na turę)\n\n- Nakłada w następnej turze 2 [AttackDmgUp] na Tożsamość z [WildHunt]\n- Jeżeli ta Tożsamość jest z Wuthering Heights albo Rodu Edgar, nakłada dodatkowo w następnej turze 1 [Enhancement]
354. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Envy) — podsumowanie] 대상의 [Sinking]당 피해량이 증가
   źródło: Passives.json :: dataList[id=1071012].summary
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — nazwa] 울고 또 울어라
   źródło: Passives.json :: dataList[id=1071021].name
   limit: do 40 znaków
   EN: Endless Lamentation
   PL: Płacz i jeszcze raz Płacz
356. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — opis] 정신력이 가장 높은 아군 1명이 정신력이 0 미만인 대상에게 입히는 피해량 +5%\n대상의 정신력이 0보다 낮을수록 입히는 피해량이 증가 (정신력 1당 +0.5%, 최대 20%)\n대상에게 정신력이 없는 경우, 대신 공격 스킬의 스킬, 코인 효과로 부여하는 [Sinking] 위력, 횟수 부여량 +1 (턴 당 최대 2회)
   źródło: Passives.json :: dataList[id=1071021].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: 1 ally that has the highest SP deals +5% damage to targets that have less than 0 SP\nIf the target has less than 0 SP: Deal even more damage the further the target's SP is from 0 (+0.5% damage per SP, max 20%)\nFor targets that are Non-SP Units, the said ally inflicts +1 more [Sinking] Potency and Count using their Skill and Coin Effects of their Attack Skills (2 times per turn)
   PL: 1 Sojusznik z najwyższą Poczytalnością zadaje +5% obrażeń celom z Poczytalnością poniżej 0\nJeżeli Poczytalność celu jest poniżej 0: im niższa Poczytalność celu poniżej 0, tym więcej obrażeń (+0.5% za każde 1 Poczytalności, maks. 20%)\nDla celów bez Poczytalności ten sojusznik nakłada o 1 więcej Mocy i Licznika [Sinking] efektami Umiejętności i monet Umiejętności ataku (maks. 2 razy na turę)
357. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — podsumowanie] 정신력이 0 미만인 대상에게 입히는 피해량이 증가
   źródło: Passives.json :: dataList[id=1071021].summary
   limit: do 120 znaków
   EN: Deal more damage to targets with less than 0 SP
   PL: Zadaje więcej obrażeń celom z Poczytalnością poniżej 0

## [000] Full-Stop Office Fixer — Heathcliff — 마침표 사무소 해결사
- ID Tożsamości: `10711` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9105 · HP bazowe: 70 · szybkość: 3–6 / 3–6 / 3–8 / 3–8
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Poise

358. [Karta Tożsamości — tytuł] 마침표 사무소\n해결사
   źródło: Personalities.json :: dataList[id=10711].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Full-Stop Office\nFixer
   PL: Biuro Kropka\nFikser
359. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10711].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10711].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Karta Tożsamości — opis] 히스클리프의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10711].desc
   limit: do 120 znaków
   EN: Heathcliff’s 11th Identity
   PL: Jedenasta Tożsamość Heathcliffa
362. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 응사
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=1].name ; dataList[id=1071101].levelList[level=2].name ; dataList[id=1071101].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Return Fire
   PL: Odpowiedź Ogniowa
363. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2
364. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend 1 [Bullet]
   PL: Zużywa 1 [Bullet]
365. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가\n<style="highlight">[WhenUse] 다음 턴에 [Agility] 1 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: [WhenUse] Gain +2 [Breath] Count\n<style="highlight">[WhenUse] Gain 1 [Agility] next turn (once per turn)</style>
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2\n<style="highlight">[WhenUse] Zyskuje 1 [Agility] w następnej turze (1 raz na turę)</style>
368. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1071101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend 1 [Bullet]<style="highlight"></style>
   PL: Zużywa 1 [Bullet]<style="highlight"></style>
369. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 [Breath] 횟수 1 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: <style="highlight">[OnSucceedAttack] Gain +1 [Breath] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Zwiększa własny Licznik [Breath] o 1</style>
370. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1071101].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가\n[WhenUse] 다음 턴에 [Agility] <style="highlight">2</style> 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: [WhenUse] Gain +2 [Breath] Count\n[WhenUse] Gain <style="highlight">2</style> [Agility] next turn (once per turn)
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2\n[WhenUse] Zyskuje <style="highlight">2</style> [Agility] w następnej turze (1 raz na turę)
373. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071101].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje +1 Licznika [Breath]<style="highlight"></style>
374. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 헤드샷
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=1].name ; dataList[id=1071102].levelList[level=2].name ; dataList[id=1071102].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 10 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Headshot
   PL: Strzał w Głowę
375. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [Breath] 3 얻음. 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 3 [Breath] and +1 [Breath] Count
   PL: [WhenUse] Zyskuje 3 [Breath] i zwiększa własny Licznik [Breath] o 1
376. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [PenetrateTakeDamageUp] 1 부여 (턴 당 2회)
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [OnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] (2 times per turn)
   PL: [OnSucceedAttack] Nakłada 1 [PenetrateTakeDamageUp] (2 razy na turę)
378. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1 당 피해량 +10% (최대 30%)</style>\n[WhenUse] [Breath] 3 얻음. 자신의 [Breath] 횟수 1 증가\n<style="highlight">[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: <style="highlight">If this unit's Speed is faster than the target's, deal +10% damage for every 1 Speed difference (max 30%)</style>\n[WhenUse] Gain 3 [Breath] and +1 [Breath] Count\n<style="highlight">[WhenUse] Gain 2 [Agility] next turn (once per turn)</style>
   PL: <style="highlight">Jeżeli Szybkość celu jest niższa niż Szybkość tej jednostki, zadaje +10% obrażeń za każde 1 różnicy Szybkości (maks. 30%)</style>\n[WhenUse] Zyskuje 3 [Breath] i zwiększa własny Licznik [Breath] o 1\n<style="highlight">[WhenUse] Zyskuje 2 [Agility] w następnej turze (1 raz na turę)</style>
379. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1071102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">크리티컬 피해량 +30%</style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+30% Damage on Critical Hit</style>
   PL: <style="highlight">Zadaje +30% obrażeń przy trafieniu krytycznym</style>
381. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [PenetrateTakeDamageUp] 1 부여 (턴 당 2회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=2].coinlist[#0].coindescs[#2].desc ; dataList[id=1071102].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [OnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] (2 times per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [PenetrateTakeDamageUp] (2 razy na turę)<style="highlight"></style>
382. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 4 — opis] <style="highlight">[CriticalOnSucceedAttack] 다음 턴에 [PenetrateTakeDamageUp] 1 부여 (턴 당 1회)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=2].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] next turn (once per turn)</style>
   PL: <style="highlight">[CriticalOnSucceedAttack] Nakłada w następnej turze 1 [PenetrateTakeDamageUp] (1 raz na turę)</style>
383. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1 당 피해량 +10% <style="highlight">(최대 50%)</style>\n[WhenUse] [Breath] 3 얻음. 자신의 [Breath] 횟수 <style="highlight">2</style> 증가\n[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: If this unit's Speed is faster than the target's, deal +10% damage for every 1 Speed difference <style="highlight">(max 50%)</style>\n[WhenUse] Gain 3 [Breath] and +<style="highlight">2</style> [Breath] Count\n[WhenUse] Gain 2 [Agility] next turn (once per turn)
   PL: Jeżeli Szybkość celu jest niższa niż Szybkość tej jednostki, zadaje +10% obrażeń za każde 1 różnicy Szybkości <style="highlight">(maks. 50%)</style>\n[WhenUse] Zyskuje 3 [Breath] i zwiększa własny Licznik [Breath] o <style="highlight">2</style>\n[WhenUse] Zyskuje 2 [Agility] w następnej turze (1 raz na turę)
384. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] 크리티컬 피해량 <style="highlight">+50%</style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+50%</style> Damage on Critical Hit
   PL: Zadaje <style="highlight">+50%</style> obrażeń przy trafieniu krytycznym
385. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] 다음 턴에 [PenetrateTakeDamageUp] 1 부여 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071102].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [CriticalOnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] next turn (once per turn)<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Nakłada w następnej turze 1 [PenetrateTakeDamageUp] (1 raz na turę)<style="highlight"></style>
386. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 한 점만 노린다
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=3].name ; dataList[id=1071103].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 12 · monety: 1 (+14)
   limit: do 40 znaków
   EN: Goin' for the Bullseye
   PL: Celuje w Jedno Miejsce
387. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [BeforeUse] 자신에게 [Bullet_LogicAtelier]가 있으면, '로직 아틀리에제 고속분쇄탄'으로 발동\n대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1 당 피해량 +10% (최대 50%)\n[WhenUse] [Breath] 5 얻음\n[WhenUse] [LogicAtelierAM]을 전부 소모하여 (소모한 수치 x 2)만큼 호흡 위력을 얻고, 피해량 +(소모한 수치 x 12.5)%
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=3].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [Bullet_LogicAtelier], [WhenUse], [Breath], [LogicAtelierAM]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [Bullet_LogicAtelier] = 탄환 - 로직 아틀리에 / Ammo - Atelier Logic; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】
   EN: [BeforeUse] If this unit has [Bullet_LogicAtelier], activate 'AL-HV Pulverisation Round' instead\nIf this unit's Speed is faster than the target's, deal +10% damage for every 1 Speed difference (max 50%)\n[WhenUse] Gain 5 [Breath]\n[WhenUse] Consume all [LogicAtelierAM] on self, gain (value consumed x 2) Poise Potency, and deal +(value consumed x 12.5)% damage
   PL: [BeforeUse] Jeżeli ma [Bullet_LogicAtelier], stosuje się jako „Pocisk Rozdrabniający AL-HV”\nJeżeli Szybkość celu jest niższa niż Szybkość tej jednostki, zadaje +10% obrażeń za każde 1 różnicy Szybkości (maks. 50%)\n[WhenUse] Zyskuje 5 [Breath]\n[WhenUse] Zużywa całe [LogicAtelierAM], zyskując Moc [Breath] równą (zużyta wartość x 2) i zadając +(zużyta wartość x 12.5)% obrażeń
388. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +50%
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: +50% Damage on Critical Hit
   PL: Zadaje +50% obrażeń Krytycznych
390. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 자신의 [Breath] 위력이 30을 초과하면, 30을 초과하는 [Breath] 위력을 최대 10까지 소모하여 피해량 +(소모한 [Breath] 위력 x 10)%
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] At more than 30 [Breath] Potency, consume up to 10 of [Breath] Potency over 30 to deal +([Breath] Potency consumed x 10)% damage
   PL: [CriticalOnSucceedAttack] Przy Mocy [Breath] powyżej 30 zużywa do 10 Mocy [Breath] ponad 30, zadając +(zużyta Moc [Breath] x 10)% obrażeń
391. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [BeforeUse] 자신에게 [Bullet_LogicAtelier]가 있으면, '로직 아틀리에제 고속분쇄탄'으로 발동\n대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1 당 피해량 +10% (최대 50%)\n[WhenUse] [Breath] 5 얻음\n[WhenUse] [LogicAtelierAM]을 전부 소모하여 (소모한 수치 x 2)만큼 호흡 위력을 얻고, 피해량 +(소모한 수치 x 12.5)%\n<style="highlight">[EndSkill] 자신의 [Breath] 횟수 2 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=4].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeUse], [Bullet_LogicAtelier], [WhenUse], [Breath], [LogicAtelierAM], [EndSkill]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [Bullet_LogicAtelier] = 탄환 - 로직 아틀리에 / Ammo - Atelier Logic; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeUse] If this unit has [Bullet_LogicAtelier], activate 'AL-HV Pulverisation Round' instead\nIf this unit's Speed is faster than the target's, deal +10% damage for every 1 Speed difference (max 50%)\n[WhenUse] Gain 5 [Breath]\n[WhenUse] Consume all [LogicAtelierAM] on self, gain (value consumed x 2) Poise Potency, and deal +(value consumed x 12.5)% damage\n<style="highlight">[EndSkill] Gain +2 [Breath] Count</style>
   PL: [BeforeUse] Jeżeli ma [Bullet_LogicAtelier], stosuje się jako „Pocisk Rozdrabniający AL-HV”\nJeżeli Szybkość celu jest niższa niż Szybkość tej jednostki, zadaje +10% obrażeń za każde 1 różnicy Szybkości (maks. 50%)\n[WhenUse] Zyskuje 5 [Breath]\n[WhenUse] Zużywa całe [LogicAtelierAM], zyskując Moc [Breath] równą (zużyta wartość x 2) i zadając +(zużyta wartość x 12.5)% obrażeń\n<style="highlight">[EndSkill] Zwiększa własny Licznik [Breath] o 2</style>
392. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] 크리티컬 피해량 <style="highlight">+80%</style>
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+80%</style> Damage on Critical Hit
   PL: Zadaje <style="highlight">+80%</style> obrażeń przy trafieniu krytycznym
394. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] <style="highlight">크리티컬 피해량 +(대상의 관통 내성 x 50)%</style>
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+(target's Pierce Res. x 50)% Damage on Critical Hit</style>
   PL: <style="highlight">Zadaje +(przebiciowa odporność celu x 50)% obrażeń przy trafieniu krytycznym</style>
395. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] 자신의 [Breath] 위력이 30을 초과하면, 30을 초과하는 [Breath] 위력을 최대 10까지 소모하여 피해량 +(소모한 [Breath] 위력 x 10)%<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071103].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] At more than 30 [Breath] Potency, consume up to 10 of [Breath] Potency over 30 to deal +([Breath] Potency consumed x 10)% damage<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Przy Mocy [Breath] powyżej 30 zużywa do 10 Mocy [Breath] ponad 30, zadając +(zużyta Moc [Breath] x 10)% obrażeń<style="highlight"></style>
396. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 로직 아틀리에제 고속분쇄탄
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=3].name ; dataList[id=1071105].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 15 · monety: 1 (+18)
   limit: do 40 znaków
   EN: AL-HV Pulverisation Round
   PL: Pocisk Rozdrabniający AL-HV
397. [Umiejętność 4 (×0) (ulepszenie 3) — opis] 대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1당 피해량 +10% (최대 50%)\n[WhenUse] [Breath] 5 얻음\n[WhenUse] [LogicAtelierAM]을 전부 소모하여, (소모한 수치 x 2)만큼 [Breath] 위력을 얻고, 피해량 +(소모한 수치 x 25)%
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=3].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [LogicAtelierAM]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】
   EN: If this unit's Speed is faster than the target's, deal +10% damage for every 1 Speed difference (max 50%)\n[WhenUse] Gain 5 [Breath]\n[WhenUse] Consume all [LogicAtelierAM] on self, gain (value consumed x 2) [Breath] Potency, and deal +(value consumed x 25)% damage
   PL: Jeżeli Szybkość celu jest niższa niż Szybkość tej jednostki, zadaje +10% obrażeń za każde 1 różnicy Szybkości (maks. 50%)\n[WhenUse] Zyskuje 5 [Breath]\n[WhenUse] Zużywa całe [LogicAtelierAM], zyskując Moc [Breath] równą (zużyta wartość x 2) i zadając +(zużyta wartość x 25)% obrażeń
398. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [Bullet_LogicAtelier] 1 소모
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet_LogicAtelier]
   znaczenie tagów: [Bullet_LogicAtelier] = 탄환 - 로직 아틀리에 / Ammo - Atelier Logic
   EN: Spend 1 [Bullet_LogicAtelier]
   PL: Zużywa 1 [Bullet_LogicAtelier]
399. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +100%
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: +100% Damage on Critical Hit
   PL: Zadaje +100% obrażeń przy trafieniu krytycznym
400. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 자신의 [Breath] 위력이 30을 초과하면, 30을 초과하는 [Breath] 위력을 최대 10까지 소모하여 피해량 +(소모한 [Breath] 위력 x 10)%
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1당 피해량 +10% (최대 50%)\n[WhenUse] [Breath] 5 얻음\n[WhenUse] [LogicAtelierAM]을 전부 소모하여, (소모한 수치 x 2)만큼 [Breath] 위력을 얻고, 피해량 +(소모한 수치 x 25)%\n<style="highlight">[EndSkill] 자신의 [Breath] 횟수 5 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [LogicAtelierAM], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】; [EndSkill] = [공격 종료시] / [Attack End]
   EN: If this unit's Speed is faster than the target's, deal +10% damage for every 1 Speed difference (max 50%)\n[WhenUse] Gain 5 [Breath]\n[WhenUse] Consume all [LogicAtelierAM] on self, gain (value consumed x 2) [Breath] Potency, and deal +(value consumed x 25)% damage\n<style="highlight">[EndSkill] Gain +5 [Breath] Count</style>
   PL: Jeżeli Szybkość celu jest niższa niż Szybkość tej jednostki, zadaje +10% obrażeń za każde 1 różnicy Szybkości (maks. 50%)\n[WhenUse] Zyskuje 5 [Breath]\n[WhenUse] Zużywa całe [LogicAtelierAM], zyskując Moc [Breath] równą (zużyta wartość x 2) i zadając +(zużyta wartość x 25)% obrażeń\n<style="highlight">[EndSkill] Zwiększa własny Licznik [Breath] o 5</style>
402. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [Bullet_LogicAtelier] 1 소모<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet_LogicAtelier]
   znaczenie tagów: [Bullet_LogicAtelier] = 탄환 - 로직 아틀리에 / Ammo - Atelier Logic
   EN: Spend 1 [Bullet_LogicAtelier]<style="highlight"></style>
   PL: Zużywa 1 [Bullet_LogicAtelier]<style="highlight"></style>
403. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] 크리티컬 피해량 <style="highlight">+130%</style>
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+130%</style> Damage on Critical Hit
   PL: Zadaje <style="highlight">+130%</style> obrażeń przy trafieniu krytycznym
404. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] <style="highlight">크리티컬 피해량 +(대상의 관통 내성 x 50)%</style>
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] 자신의 [Breath] 위력이 30을 초과하면, 30을 초과하는 [Breath] 위력을 최대 10까지 소모하여 피해량 +(소모한 [Breath] 위력 x 10)%<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071105].levelList[level=4].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 395 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Obrona (ulepszenia 1,4) — nazwa] 전투 호흡
   źródło: Skills_personality-07.json :: dataList[id=1071104].levelList[level=1].name ; dataList[id=1071104].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Combat Poise
   PL: Bojowa Flegma
407. [Obrona (ulepszenie 1) — opis] 턴 시작시 탄환이 0이면 '엄폐'로 변경됨\n[WhenUse] 마침표 사무소 대표 홍루 인격이 전투에 등장해 있으면, 대상에게 [MeleeCover] 요청 (턴 당 1회)\n[EndBattle] 다음 턴에 [LogicAtelierAM] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071104].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [MeleeCover], [EndBattle], [LogicAtelierAM]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [MeleeCover] = 근접 지원 / Melee Support; [EndBattle] = [턴 종료 시] / [Turn End]; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】
   EN: Turn Start: At 0 Ammo, this Skill activates as 'Taking Cover' instead\n[WhenUse] If Full-Stop Office Rep. Hong Lu is on the field, request [MeleeCover] from that unit (once per turn)\n[EndBattle] Gain 1 [LogicAtelierAM] next turn (once per turn)
   PL: Na początku tury przy 0 amunicji stosuje się jako „Szukanie Osłony”\n[WhenUse] Jeżeli Tożsamość Rep Biura Kropka Hong Lu jest na polu, prosi ją o [MeleeCover] (1 raz na turę)\n[EndBattle] Zyskuje 1 [LogicAtelierAM] w następnej turze (1 raz na turę)
408. [Obrona (ulepszenie 4) — opis] 턴 시작시 탄환이 0이면 '엄폐'로 변경됨\n[WhenUse] 마침표 사무소 대표 홍루 인격이 전투에 등장해 있으면, 대상에게 [MeleeCover] 요청 (턴 당 1회)\n<style="highlight">[OnSucceedEvade] [Breath] 3 얻음 (턴 당 최대 3회)</style>\n[EndBattle] 다음 턴에 [LogicAtelierAM] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071104].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [MeleeCover], [OnSucceedEvade], [Breath], [EndBattle], [LogicAtelierAM]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [MeleeCover] = 근접 지원 / Melee Support; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise; [EndBattle] = [턴 종료 시] / [Turn End]; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】
   EN: Turn Start: At 0 Ammo, this Skill activates as 'Taking Cover' instead\n[WhenUse] If Full-Stop Office Rep. Hong Lu is on the field, request [MeleeCover] from that unit (once per turn)\n<style="highlight">[OnSucceedEvade] Gain 3 [Breath] (3 times per turn)</style>\n[EndBattle] Gain 1 [LogicAtelierAM] next turn (once per turn)
   PL: Na początku tury przy 0 amunicji stosuje się jako „Szukanie Osłony”\n[WhenUse] Jeżeli Tożsamość Rep Biura Kropka Hong Lu jest na polu, prosi ją o [MeleeCover] (1 raz na turę)\n<style="highlight">[OnSucceedEvade] Zyskuje 3 [Breath] (maks. 3 razy na turę)</style>\n[EndBattle] Zyskuje 1 [LogicAtelierAM] w następnej turze (1 raz na turę)
409. [Obrona (ulepszenia 1,4) — nazwa] 엄폐
   źródło: Skills_personality-07.json :: dataList[id=1071106].levelList[level=1].name ; dataList[id=1071106].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 2 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Taking Cover
   PL: Szukanie Osłony
410. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[WhenUse] 마침표 사무소 대표 홍루 인격이 전투에 등장해 있으면, 대상에게 [MeleeCover] 요청 (턴 당 1회)\n[EndBattle] 다음 턴에 [LogicAtelierAM] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071106].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WhenUse], [MeleeCover], [EndBattle], [LogicAtelierAM]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [MeleeCover] = 근접 지원 / Melee Support; [EndBattle] = [턴 종료 시] / [Turn End]; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】
   EN: [CanDuelGuard]\n[WhenUse] If Full-Stop Office Rep. Hong Lu is on the field, request [MeleeCover] from that unit (once per turn)\n[EndBattle] Gain 1 [LogicAtelierAM] next turn (once per turn)
   PL: [CanDuelGuard]\n[WhenUse] Jeżeli Tożsamość Rep Biura Kropka Hong Lu jest na polu, prosi ją o [MeleeCover] (1 raz na turę)\n[EndBattle] Zyskuje 1 [LogicAtelierAM] w następnej turze (1 raz na turę)
411. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071106].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1071106].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL: [SuperCoin]<style="highlight"></style>
412. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[WhenUse] 마침표 사무소 대표 홍루 인격이 전투에 등장해 있으면, 대상에게 [MeleeCover] 요청 (턴 당 1회)\n<style="highlight">[WinDuel] 대상에게 [PenetrateResistDown] 1 부여 (턴 당 1회)</style>\n[EndBattle] 다음 턴에 [LogicAtelierAM] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071106].levelList[level=4].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [WhenUse], [MeleeCover], [WinDuel], [PenetrateResistDown], [EndBattle], [LogicAtelierAM]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [MeleeCover] = 근접 지원 / Melee Support; [WinDuel] = [합 승리시] / [Clash Win]; [PenetrateResistDown] = 관통 내성 약화 / Pierce Resist Down; [EndBattle] = [턴 종료 시] / [Turn End]; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】
   EN: [CanDuelGuard]\n[WhenUse] If Full-Stop Office Rep. Hong Lu is on the field, request [MeleeCover] from that unit (once per turn)\n<style="highlight">[WinDuel] Inflict 1 [PenetrateResistDown] (once per turn)</style>\n[EndBattle] Gain 1 [LogicAtelierAM] next turn (once per turn)
   PL: [CanDuelGuard]\n[WhenUse] Jeżeli Tożsamość Rep Biura Kropka Hong Lu jest na polu, prosi ją o [MeleeCover] (1 raz na turę)\n<style="highlight">[WinDuel] Nakłada 1 [PenetrateResistDown] (1 raz na turę)</style>\n[EndBattle] Zyskuje 1 [LogicAtelierAM] w następnej turze (1 raz na turę)
413. [Pasywka bojowa (od ulepszenia 1) — nazwa] 저격
   źródło: Passives.json :: dataList[id=1071101].name
   limit: do 40 znaków
   EN: Snipe
   PL: Snajperstwo
414. [Pasywka bojowa (od ulepszenia 1) — opis] 스테이지 시작시 [PenetrateResultUp] 3 얻음\n\n턴 종료시 자신의 모든 [Bullet]이 0이면, [Retreat_FullStop] (전투 당 1회)\n\n대기해제되었거나, [Retreat_FullStop] 이후 다시 전투에 참여했을 때, [LogicAtelierAM]이 최대가 되고, [PenetrateResultUp]를 3 얻고, [FullReload] ([Bullet_LogicAtelier] 제외, 전투 당 1회)
   źródło: Passives.json :: dataList[id=1071101].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [PenetrateResultUp], [Bullet], [Retreat_FullStop], [LogicAtelierAM], [FullReload], [Bullet_LogicAtelier]
   znaczenie tagów: [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [Bullet] = 탄환 / Ammo; [Retreat_FullStop] = 후방 지원 배치 / Overwatch Assignment; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】; [FullReload] = 재장전 / Reload; [Bullet_LogicAtelier] = 탄환 - 로직 아틀리에 / Ammo - Atelier Logic
   EN: Encounter Start: gain 3 [PenetrateResultUp]\n\nTurn End: If this unit does not have any remaining [Bullet] of any kind, activate [Retreat_FullStop] (once per Encounter)\n\nIf this unit is Substituted in, or is rejoining battle after [Retreat_FullStop], gain max [LogicAtelierAM], 3 [PenetrateResultUp], and [FullReload] (except [Bullet_LogicAtelier]; once per Encounter)
   PL: Na początku spotkania zyskuje 3 [PenetrateResultUp]\n\nNa koniec tury, jeżeli jej wszystkie [Bullet] wynoszą 0, stosuje [Retreat_FullStop] (1 raz na spotkanie)\n\nPo Wejściu z rezerwy albo po ponownym przystąpieniu do walki po [Retreat_FullStop] uzupełnia [LogicAtelierAM] do maksimum, zyskuje 3 [PenetrateResultUp] i [FullReload] (z wyłączeniem [Bullet_LogicAtelier]; 1 raz na spotkanie)
415. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Pride) — nazwa] 정밀 조준
   źródło: Passives.json :: dataList[id=1071102].name
   limit: do 40 znaków
   EN: Precision Aim
   PL: Celne Wycelowanie
416. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Pride) — opis] 턴 종료시 자신의 [Breath] 10 당, 다음 턴에 [Agility] 1 얻음 (최대 2)\n\n턴 종료 시 이번 턴에 자신이 (E.G.O 스킬 포함, [CoveringFire] 제외) 공격 스킬을 사용하지 않았으면, 다음 턴에 [Breath] 10, [PenetrateResultUp] 1 얻음.
   źródło: Passives.json :: dataList[id=1071102].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Agility], [CoveringFire], [PenetrateResultUp]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [CoveringFire] = 타겟 포착 / Target Spotted; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up
   EN: Turn End: Gain 1 [Agility] next turn for every 10 [Breath] on self (max 2)\n\nTurn End: If this unit is not set to use any Attack Skills (including E.G.O Skills, excluding [CoveringFire]), gain 10 [Breath] and 1 [PenetrateResultUp] next turn.
   PL: Na koniec tury zyskuje 1 [Agility] w następnej turze za każde 10 [Breath] (maks. 2)\n\nNa koniec tury, jeżeli w tej turze nie planuje użyć żadnej Umiejętności ataku (łącznie z Umiejętnościami E.G.O, z wyłączeniem [CoveringFire]), zyskuje 10 [Breath] i 1 [PenetrateResultUp] w następnej turze.
417. [Pasywka bojowa (od ulepszenia 3) — nazwa] 저격
   źródło: Passives.json :: dataList[id=1071103].name
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Pasywka bojowa (od ulepszenia 3) — opis] 스테이지 시작시 [PenetrateResultUp] 3 얻음\n\n<style="highlight">이 캐릭터가 전투에 등장할 때, [Bullet_LogicAtelier] 1 얻음 (전투 당 1회)</style>\n\n턴 종료시 자신의 모든 [Bullet]이 0이면, [Retreat_FullStop] (전투 당 1회)\n\n대기해제되었거나, [Retreat_FullStop] 이후 다시 전투에 참여했을 때, [LogicAtelierAM]이 최대가 되고, [PenetrateResultUp]를 3 얻고, [FullReload]\n([Bullet_LogicAtelier] 제외, 전투 당 1회)
   źródło: Passives.json :: dataList[id=1071103].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [PenetrateResultUp], [Bullet_LogicAtelier], [Bullet], [Retreat_FullStop], [LogicAtelierAM], [FullReload]
   znaczenie tagów: [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [Bullet_LogicAtelier] = 탄환 - 로직 아틀리에 / Ammo - Atelier Logic; [Bullet] = 탄환 / Ammo; [Retreat_FullStop] = 후방 지원 배치 / Overwatch Assignment; [LogicAtelierAM] = 집중【저격】 / Concentration【Sniper】; [FullReload] = 재장전 / Reload
   EN: Encounter Start: gain 3 [PenetrateResultUp]\n\n<style="highlight">When this unit enters the Encounter, gain 1 [Bullet_LogicAtelier] (once per Encounter)</style>\n\nTurn End: If this unit does not have any remaining [Bullet] of any kind, activate [Retreat_FullStop] (once per Encounter)\n\nIf this unit is Substituted in, or is rejoining battle after [Retreat_FullStop], gain max [LogicAtelierAM], 3 [PenetrateResultUp], and [FullReload]\n(Except [Bullet_LogicAtelier]; once per Encounter)
   PL: Na początku spotkania zyskuje 3 [PenetrateResultUp]\n\n<style="highlight">Gdy ta jednostka wchodzi na pole walki, zyskuje 1 [Bullet_LogicAtelier] (1 raz na spotkanie)</style>\n\nNa koniec tury, jeżeli jej wszystkie [Bullet] wynoszą 0, stosuje [Retreat_FullStop] (1 raz na spotkanie)\n\nPo Wejściu z rezerwy albo po ponownym przystąpieniu do walki po [Retreat_FullStop] uzupełnia [LogicAtelierAM] do maksimum, zyskuje 3 [PenetrateResultUp] i [FullReload]\n(z wyłączeniem [Bullet_LogicAtelier]; 1 raz na spotkanie)
419. [Pasywka bojowa (od ulepszenia 4, rezonans 2× Pride) — nazwa] 정밀 조준
   źródło: Passives.json :: dataList[id=1071111].name
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Pasywka bojowa (od ulepszenia 4, rezonans 2× Pride) — opis] 턴 종료시 자신의 [Breath] 10 당, 다음 턴에 [Agility] 1 얻음 (최대 2)\n\n<style="highlight">전투 시작시 자신이 (E.G.O 스킬 포함) 공격 스킬을 사용할 예정이 아니면, 호흡 위력이 가장 낮은 아군 1명에게 [Breath] 3 부여</style>\n\n턴 종료 시 이번 턴에 자신이 (E.G.O 스킬 포함, [CoveringFire] 제외) 공격 스킬을 사용하지 않았으면, 다음 턴에 [Breath] 10, [PenetrateResultUp] 1 얻음
   źródło: Passives.json :: dataList[id=1071111].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [Agility], [CoveringFire], [PenetrateResultUp]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [CoveringFire] = 타겟 포착 / Target Spotted; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up
   EN: Turn End: Gain 1 [Agility] next turn for every 10 [Breath] on self (max 2)\n\n<style="highlight">Combat Start: If this unit is not set to use any Attack Skills (including E.G.O Skills), apply 3 [Breath] to 1 ally that has the least [Breath] Potency</style>\n\nTurn End: If this unit did not use any Attack Skills (including E.G.O Skills, excluding [CoveringFire]), gain 10 [Breath] and 1 [PenetrateResultUp] next turn
   PL: Na koniec tury zyskuje 1 [Agility] w następnej turze za każde 10 [Breath] (maks. 2)\n\n<style="highlight">Na początku walki, jeżeli nie planuje użyć żadnej Umiejętności ataku (łącznie z Umiejętnościami E.G.O), nakłada 3 [Breath] na 1 Sojusznika z najniższą Mocą [Breath]</style>\n\nNa koniec tury, jeżeli w tej turze nie planuje użyć żadnej Umiejętności ataku (łącznie z Umiejętnościami E.G.O, z wyłączeniem [CoveringFire]), zyskuje 10 [Breath] i 1 [PenetrateResultUp] w następnej turze
421. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — nazwa] 감적수
   źródło: Passives.json :: dataList[id=1071121].name
   limit: do 40 znaków
   EN: Spotter
   PL: Obserwator
422. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — opis] [Bullet]을 가장 적게 보유한 아군 1명이 [Bullet]을 소모하는 스킬을 사용할 때, [Breath] 횟수 2 증가\n- 대상이 마침표 사무소 인격이거나, 대상의 [Breath] 횟수가 5 미만이면, 대신 4 증가 (턴 당 1회. [Bullet]이 없는 대상에게는 적용되지 않음)
   źródło: Passives.json :: dataList[id=1071121].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [Breath] = 호흡 / Poise
   EN: 1 ally that has the least [Bullet] gains +2 [Breath] Count when using a Skill that consumes [Bullet].\n- If the said ally is a Full-Stop Office Identity, or if they have less than 5 [Breath] Count, gain +4 [Breath] Count instead (once per turn; does not apply to units without [Bullet])
   PL: Gdy 1 Sojusznik z najmniejszą liczbą [Bullet] używa Umiejętności zużywającej [Bullet], zyskuje +2 Licznika [Breath]\n- Jeżeli tę Tożsamością jest Biuro Kropka albo ma mniej niż 5 Licznika [Breath], zamiast tego zyskuje +4 Licznika [Breath] (1 raz na turę; nie dotyczy jednostek bez [Bullet])

## [000] Kurokumo Clan Wakashu — Heathcliff — 흑운회 와카슈
- ID Tożsamości: `10712` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 70 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed

423. [Karta Tożsamości — tytuł] 흑운회\n와카슈
   źródło: Personalities.json :: dataList[id=10712].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Kurokumo Clan\nWakashu
   PL: Klan Kurokumo\nWakashu
424. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10712].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10712].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Karta Tożsamości — opis] 히스클리프의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10712].desc
   limit: do 120 znaków
   EN: Heathcliff’s 12th Identity
   PL: Dwunasta Tożsamość Heathcliffa
427. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 구름베기
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=1].name ; dataList[id=1071201].levelList[level=2].name ; dataList[id=1071201].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Lenticular Rend
   PL: Cięcie Chmur
428. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Endurance] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Endurance]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: [WhenUse] Gain 1 [Endurance] next turn (once per turn)
   PL: [WhenUse] Zyskuje 1 [Endurance] w następnej turze (1 raz na turę)
429. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]
430. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AttackDown] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown]
   PL: [OnSucceedAttack] Nakłada 1 [AttackDown]
432. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 다음 턴에 [Endurance] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [WhenUse], [Endurance]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: <style="highlight">If target has 6+ [Laceration], Coin Power +1</style>\n[WhenUse] Gain 1 [Endurance] next turn (once per turn)
   PL: <style="highlight">Jeżeli cel ma 6+ [Laceration], Moc Monet +1</style>\n[WhenUse] Zyskuje 1 [Endurance] w następnej turze (1 raz na turę)
433. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1071201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]<style="highlight"></style>
434. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AttackDown] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1071201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [AttackDown]<style="highlight"></style>
436. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 다음 턴에 [Endurance] <style="highlight">2</style> 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071201].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [WhenUse], [Endurance]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[WhenUse] Gain <style="highlight">2</style> [Endurance] next turn (once per turn)
   PL: <style="highlight">Moc Monet +1 za każde 6 [Laceration] celu (maks. 2)</style>\n[WhenUse] Zyskuje <style="highlight">2</style> [Endurance] w następnej turze (1 raz na turę)
437. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 폭풍구름
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=1].name ; dataList[id=1071202].levelList[level=2].name ; dataList[id=1071202].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Stormcloud
   PL: Chmura Burzowa
438. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]
439. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 2
440. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Reduction] 1 부여 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] (once per turn)
   PL: [OnSucceedAttack] Nakłada 1 [Reduction] (1 raz na turę)
441. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: <style="highlight">If target has 6+ [Laceration], Coin Power +1</style>
   PL: <style="highlight">Jeżeli cel ma 6+ [Laceration], Moc Monet +1</style>
442. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1071202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]<style="highlight"></style>
443. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [SlashTakeDamageUp] 1 부여</style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: <style="highlight">[OnSucceedAttackHead] Inflict 1 [SlashTakeDamageUp]</style>
   PL: <style="highlight">[OnSucceedAttackHead] Nakłada 1 [SlashTakeDamageUp]</style>
444. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 2<style="highlight"></style>
445. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Reduction] 1 부여 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] (once per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Reduction] (1 raz na turę)<style="highlight"></style>
446. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)\n[WhenUse] 다음 턴에 [Endurance] 1 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [WhenUse], [Endurance]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)\n[WhenUse] Gain 1 [Endurance] next turn (once per turn)</style>
   PL: <style="highlight">Moc Monet +1 za każde 6 [Laceration] celu (maks. 2)\n[WhenUse] Zyskuje 1 [Endurance] w następnej turze (1 raz na turę)</style>
447. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [SlashTakeDamageUp] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttackHead] Inflict 1 [SlashTakeDamageUp]<style="highlight"></style>
   PL: [OnSucceedAttackHead] Nakłada 1 [SlashTakeDamageUp]<style="highlight"></style>
448. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Reduction] 1 부여 (턴 당 <style="highlight">2</style>회)
   źródło: Skills_personality-07.json :: dataList[id=1071202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] (<style="highlight">2 times</style> per turn)
   PL: [OnSucceedAttack] Nakłada 1 [Reduction] (maks. <style="highlight">2</style> razy na turę)
449. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 천둥베기
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].name ; dataList[id=1071203].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Thundercleave
   PL: Cios Gromu
450. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[StartBattle] 다음 턴에 [CloudWall] 1 얻음\n[WhenUse] 다음 턴에 [Endurance] 1 얻음 (턴 당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [StartBattle], [CloudWall], [WhenUse], [Endurance]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [CloudWall] = 구름 장벽 / Cumulus Wall; [WhenUse] = [사용시] / [On Use]; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: If target has 6+ [Laceration], Coin Power +1\n[StartBattle] Gain 1 [CloudWall] next turn\n[WhenUse] Gain 1 [Endurance] next turn (once per turn)
   PL: Jeżeli cel ma 6+ [Laceration], Moc Monet +1\n[StartBattle] Zyskuje 1 [CloudWall] w następnej turze\n[WhenUse] Zyskuje 1 [Endurance] w następnej turze (1 raz na turę)
451. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] The final Coin deals +10% damage
   PL: [OnSucceedAttack] Ostatnia moneta zadaje +10% obrażeń
453. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [SlashTakeDamageUp] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttack] Inflict 1 [SlashTakeDamageUp]
   PL: [OnSucceedAttack] Nakłada 1 [SlashTakeDamageUp]
454. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 대상이 보유한 부정적인 효과 1개당 피해량 +10% (최대 30%)
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +10% damage for every type of negative effect on target (max 30%)
   PL: Zadaje +10% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 30%)
456. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]
   PL: [OnSucceedAttack] Nakłada 6 [Laceration]
457. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">대상의 [Laceration] 6 당, 코인 위력 +1 (최대 2)</style>\n[StartBattle] 다음 턴에 [CloudWall] 1 얻음\n[WhenUse] 다음 턴에 [Endurance] 1 얻음 (턴 당 1회)\n<style="highlight">[WinDuel] 다음 턴에 [BlackCloudBlade] 1 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Laceration], [StartBattle], [CloudWall], [WhenUse], [Endurance], [WinDuel], [BlackCloudBlade]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [CloudWall] = 구름 장벽 / Cumulus Wall; [WhenUse] = [사용시] / [On Use]; [Endurance] = 수비 위력 증가 / Defense Power Up; [WinDuel] = [합 승리시] / [Clash Win]; [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[StartBattle] Gain 1 [CloudWall] next turn\n[WhenUse] Gain 1 [Endurance] next turn (once per turn)\n<style="highlight">[WinDuel] Gain 1 [BlackCloudBlade] next turn (once per turn)</style>
   PL: <style="highlight">Moc Monet +1 za każde 6 [Laceration] celu (maks. 2)</style>\n[StartBattle] Zyskuje 1 [CloudWall] w następnej turze\n[WhenUse] Zyskuje 1 [Endurance] w następnej turze (1 raz na turę)\n<style="highlight">[WinDuel] Zyskuje 1 [BlackCloudBlade] w następnej turze (1 raz na turę)</style>
458. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 마지막 코인의 피해량 +10%<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] The final Coin deals +10% damage<style="highlight"></style>
   PL: [OnSucceedAttack] Ostatnia moneta zadaje +10% obrażeń<style="highlight"></style>
460. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [SlashTakeDamageUp] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [OnSucceedAttack] Inflict 1 [SlashTakeDamageUp]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [SlashTakeDamageUp]<style="highlight"></style>
461. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 마지막 코인의 피해량 +10%<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 459 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 대상이 보유한 부정적인 효과 1개당 피해량 +10% <style="highlight">(최대 100%)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal +10% damage for every type of negative effect on target <style="highlight">(max 100%)</style>
   PL: Zadaje +10% obrażeń za każdy 1 rodzaj negatywnego efektu na celu <style="highlight">(maks. 100%)</style>
463. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 6 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 6 [Laceration]<style="highlight"></style>
464. [Umiejętność 4 (×0) (ulepszenia 1,4) — nazwa] 뒷골목의 규칙
   źródło: Skills_personality-07.json :: dataList[id=1071205].levelList[level=1].name ; dataList[id=1071205].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Rules of the Backstreets
   PL: Zasady Zauloków
465. [Umiejętność 4 (×0) (ulepszenie 1) — opis] [WhenUse] 자신이 [CloudWall]을 보유하고 있으면, 이 스킬 코인의 재사용 효과를 조건 없이 모두 발동
   źródło: Skills_personality-07.json :: dataList[id=1071205].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [CloudWall]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [CloudWall] = 구름 장벽 / Cumulus Wall
   EN: [WhenUse] If this unit has [CloudWall], unconditionally activate all Reuse effects on this Skill's Coins
   PL: [WhenUse] Jeżeli ma [CloudWall], uruchamia bezwarunkowo wszystkie efekty ponownego użycia monet tej Umiejętności
466. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071205].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1071205].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신에게 [BlackCloudBlade]가 있으면 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071205].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1071205].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BlackCloudBlade]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: [OnSucceedAttack] If this unit has [BlackCloudBlade], Reuse Coin once (once per Skill)
   PL: [OnSucceedAttack] Jeżeli ma [BlackCloudBlade], ponownie używa monety 1 raz (1 raz na Umiejętność)
468. [Umiejętność 4 (×0) (ulepszenia 1,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신에게 [EngageToBattle]이 있으면 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071205].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=1071205].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EngageToBattle]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EngageToBattle] = 임전 / Battle Ready
   EN: [OnSucceedAttack] If this unit has [EngageToBattle], Reuse Coin once (once per Skill)
   PL: [OnSucceedAttack] Jeżeli ma [EngageToBattle], ponownie używa monety 1 raz (1 raz na Umiejętność)
469. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n대상이 보유한 부정적인 효과 1개당 피해량 +10% (최대 100%)\n[WhenUse] 자신이 [CloudWall]을 보유하고 있으면, 이 스킬 코인의 재사용 효과를 조건 없이 모두 발동
   źródło: Skills_personality-07.json :: dataList[id=1071205].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [WhenUse], [CloudWall]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [CloudWall] = 구름 장벽 / Cumulus Wall
   EN: If target has 6+ [Laceration], Coin Power +1\nDeal +10% damage for every type of negative effect on target (max 100%)\n[WhenUse] If this unit has [CloudWall], unconditionally activate all Reuse effects on this Skill's Coins
   PL: Jeżeli cel ma 6+ [Laceration], Moc Monet +1\nZadaje +10% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 100%)\n[WhenUse] Jeżeli ma [CloudWall], uruchamia bezwarunkowo wszystkie efekty ponownego użycia monet tej Umiejętności
470. [Obrona (ulepszenia 1,4) — nazwa] 뒷골목의 규칙
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=1].name ; dataList[id=1071204].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 4 · monety: 1 (+5)
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n흑운회 부조장 이스마엘 인격이 전투에 등장해 있으면, 아래 효과가 적용됨\n- 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n- 합 패배시 이 스킬의 최종 위력 +3\n[WhenUse] 자신이 [CloudWall]을 보유하고 있으면, 이 스킬 코인의 재사용 효과를 조건 없이 모두 발동
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=1].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [SuperCoin], [WhenUse], [CloudWall]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [CloudWall] = 구름 장벽 / Cumulus Wall
   EN: [DuelCounter]\nIf Kurokumo Clan Captain Ishmael is on the field, activate the following:\n- Convert all Coins in this Skill into [SuperCoin]s\n- Final Power +3 to this Skill upon Clash Lose\n[WhenUse] If this unit has [CloudWall], unconditionally activate all Reuse effects on this Skill's Coins
   PL: [DuelCounter]\nJeżeli Kapitan Klanu Kurokumo Ishmael jest na polu, stosują się poniższe efekty:\n- Wszystkie monety tej Umiejętności stają się [SuperCoin]ami\n- Przy przegranej w starciu Moc Końcowa tej Umiejętności +3\n[WhenUse] Jeżeli ma [CloudWall], uruchamia bezwarunkowo wszystkie efekty ponownego użycia monet tej Umiejętności
472. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Obrona (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신에게 [BlackCloudBlade]가 있으면 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Obrona (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신에게 [EngageToBattle]이 있으면 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n흑운회 부조장 이스마엘 인격이 전투에 등장해 있으면, 아래 효과가 적용됨\n- 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n- 합 패배시 이 스킬의 최종 위력 <style="highlight">+4\n대상이 보유한 부정적인 효과 1개당 피해량 +10% (최대 100%)</style>\n[WhenUse] 자신이 [CloudWall]을 보유하고 있으면, 이 스킬 코인의 재사용 효과를 조건 없이 모두 발동
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=4].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [SuperCoin], [WhenUse], [CloudWall]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [CloudWall] = 구름 장벽 / Cumulus Wall
   EN: [DuelCounter]\nIf Kurokumo Clan Captain Ishmael is on the field, activate the following:\n- Convert all Coins in this Skill into [SuperCoin]s\n- Final Power +4 to this Skill upon Clash Lose\n<style="highlight">Deal +10% damage for every type of negative effect on target (max 100%)</style>\n[WhenUse] If this unit has [CloudWall], unconditionally activate all Reuse effects on this Skill's Coins
   PL: [DuelCounter]\nJeżeli Kapitan Klanu Kurokumo Ishmael jest na polu, stosują się poniższe efekty:\n- Wszystkie monety tej Umiejętności stają się [SuperCoin]ami\n- Przy przegranej w starciu Moc Końcowa tej Umiejętności <style="highlight">+4\nZadaje +10% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 100%)</style>\n[WhenUse] Jeżeli ma [CloudWall], uruchamia bezwarunkowo wszystkie efekty ponownego użycia monet tej Umiejętności
476. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Obrona (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신에게 [BlackCloudBlade]가 있으면 코인 1회 재사용 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BlackCloudBlade]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: [OnSucceedAttack] If this unit has [BlackCloudBlade], Reuse Coin once (once per Skill)<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli ma [BlackCloudBlade], ponownie używa monety 1 raz (1 raz na Umiejętność)<style="highlight"></style>
478. [Obrona (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신에게 [EngageToBattle]이 있으면 코인 1회 재사용 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071204].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [EngageToBattle]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EngageToBattle] = 임전 / Battle Ready
   EN: [OnSucceedAttack] If this unit has [EngageToBattle], Reuse Coin once (once per Skill)<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli ma [EngageToBattle], ponownie używa monety 1 raz (1 raz na Umiejętność)<style="highlight"></style>
479. [Pasywka bojowa (od ulepszenia 1) — nazwa] 임전
   źródło: Passives.json :: dataList[id=1071202].name
   limit: do 40 znaków
   EN: Battle Ready
   PL: Gotowość Bojowa
480. [Pasywka bojowa (od ulepszenia 1) — opis] 흑운회 소속 아군이 사망하면, 이번 전투 동안 [SlashResultUp] 1 얻음\n\n흑운회 소속 아군이 3명 이상 사망하면 이번 전투 동안 [EngageToBattle]을 얻음
   źródło: Passives.json :: dataList[id=1071202].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [SlashResultUp], [EngageToBattle]
   znaczenie tagów: [SlashResultUp] = 참격 위력 증가 / Slash Power Up; [EngageToBattle] = 임전 / Battle Ready
   EN: When a Kurokumo Clan ally dies, gain 1 [SlashResultUp] for this Encounter\n\nWhen 3 or more Kurokumo Clan allies are defeated, gain [EngageToBattle] for this Encounter
   PL: Gdy sojusznik Klanu Kurokumo ginie, zyskuje 1 [SlashResultUp] w tym spotkaniu\n\nGdy zginie 3 lub więcej sojuszników Klanu Kurokumo, zyskuje [EngageToBattle] w tym spotkaniu
481. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — nazwa] 흑운도
   źródło: Passives.json :: dataList[id=1071201].name
   limit: do 40 znaków
   EN: Dark Cloud Blade
   PL: Klinga Czarnego Obłoku
482. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — opis] 자신을 포함해 전투에 참여한 아군 흑운회 소속 인격이 2명 이상이면 [BlackCloudBlade] 1 얻음 (최대 1)\n\n이번 턴에 수비 스킬을 사용한 적 또는 공격 시작 전에 최대 체력인 적에게 입히는 피해량 +10%\n\n이번 턴에 적이 자신을 제외한 아군을 스킬로 공격하여 피해를 입혔으면, 공격자를 스킬 1로 일방 공격함 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1071201].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [BlackCloudBlade]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: When there are 2+ allied Kurokumo Clan Identities on the field, including this unit, gain 1 [BlackCloudBlade] (max 1)\n\nAgainst enemies that, in this turn, used Defense Skills or were at max HP before attacking: deal +10% damage\n\nIf an enemy attacked another ally with a Skill and dealt damage this turn: use an Unopposed Attack against the attacker with Skill 1 (once per turn)
   PL: Jeżeli 2 lub więcej Tożsamości Klanu Kurokumo (łącznie z tą jednostką) uczestniczy w walce, zyskuje 1 [BlackCloudBlade] (maks. 1)\n\nZadaje +10% obrażeń wrogom, którzy w tej turze użyli Umiejętności obrony albo mieli Maks. HP przed atakiem\n\nJeżeli wróg w tej turze zaatakował Umiejętnością innego sojusznika (poza tą jednostką) i zadał obrażenia, atakuje nieoparciego agresora Umiejętnością 1 (1 raz na turę)
483. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — podsumowanie] [BlackCloudBlade] 얻음, 최대 체력이거나 수비 스킬을 사용한 적 대상 피해량 증가, 아군이 공격당하면 반격 발동
   źródło: Passives.json :: dataList[id=1071201].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [BlackCloudBlade]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: Gain [BlackCloudBlade]; deal more damage against enemies that were at max HP or used a Defense Skill; counterattack when an ally is attacked
   PL: Zyskuje [BlackCloudBlade]; zadaje więcej obrażeń wrogom z pełnym HP albo po użyciu Umiejętności obrony; odpowiada, gdy sojusznik zostanie zaatakowany
484. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — nazwa] 흑운도
   źródło: Passives.json :: dataList[id=1071211].name
   (powtórzenie elementu 481 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — opis] 자신을 포함해 전투에 참여한 아군 흑운회 소속 인격이 2명 이상이면 [BlackCloudBlade] 1 얻음 (최대 1)\n\n이번 턴에 수비 스킬을 사용한 적 또는 공격 시작 전에 최대 체력인 적에게 입히는 피해량 +10%\n\n적이 자신을 제외한 아군을 스킬로 공격하여 피해를 입혔으면, 공격자를 스킬 1로 일방 공격함 (턴 당 1회)\n\n<style="highlight">적이 자신을 제외한 아군을 처치했거나, 공격 종료후 공격당한 아군의 체력이 25% 미만이면, 공격자를 <뒷골목의 규칙> 으로 일방 공격함 (아군 캐릭터 당 1회, 턴 당 2회. 해당 효과로 발동된 스킬은 공격 스킬로 간주함)</style>
   źródło: Passives.json :: dataList[id=1071211].desc
   limit: do 840 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BlackCloudBlade]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: When there are 2+ allied Kurokumo Clan Identities on the field, including this unit, gain 1 [BlackCloudBlade] (max 1)\n\nAgainst enemies that, in this turn, used Defense Skills or were at max HP before attacking: deal +10% damage\n\nIf an enemy attacked another ally with a Skill and dealt damage this turn: use an Unopposed Attack against the attacker with Skill 1 (once per turn)\n\n<style="highlight">If the enemy killed another ally, or if the said ally's HP is at less than 25% after the enemy's attack, use an Unopposed Attack against the attacker with <Rules of the Backstreets> instead (once per ally; 2 times per turn; the Skill activated with this effect counts as an Attack Skill)</style>
   PL: Jeżeli 2 lub więcej Tożsamości Klanu Kurokumo (łącznie z tą jednostką) uczestniczy w walce, zyskuje 1 [BlackCloudBlade] (maks. 1)\n\nZadaje +10% obrażeń wrogom, którzy w tej turze użyli Umiejętności obrony albo mieli Maks. HP przed atakiem\n\nJeżeli wróg w tej turze zaatakował Umiejętnością innego sojusznika (poza tą jednostką) i zadał obrażenia, atakuje nieoparciego agresora Umiejętnością 1 (1 raz na turę)\n\n<style="highlight">Jeżeli wróg zabił innego sojusznika albo HP zaatakowanego sojusznika jest poniżej 25% po jego ataku, atakuje nieoparciego agresora <Zasady Zauloków> (1 raz na sojusznika; 2 razy na turę; Umiejętność uruchomiona tym efektem liczy się jako Umiejętność ataku)</style>
486. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Lust) — podsumowanie] [BlackCloudBlade] 얻음, 최대 체력이거나 수비 스킬을 사용한 적 대상 피해량이 증가, 아군이 공격당하면 반격 발동
   źródło: Passives.json :: dataList[id=1071211].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [BlackCloudBlade]
   znaczenie tagów: [BlackCloudBlade] = 흑운도 / Dark Cloud Blade
   EN: Gain [BlackCloudBlade]; deal more damage against enemies that were at max HP or used a Defense Skill; counterattack when an ally is attacked
   PL: Zyskuje [BlackCloudBlade], zadaje więcej obrażeń wrogom z pełnym HP albo po użyciu Umiejętności obrony, odpowiada gdy sojusznik zostaje zaatakowany
487. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — nazwa] 후벼파기
   źródło: Passives.json :: dataList[id=1071221].name
   limit: do 40 znaków
   EN: Impale
   PL: Przebicie na Wylot
488. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — opis] 속도가 가장 빠른 아군 1명이 이번 턴에 수비 스킬을 사용했거나, 공격 시작 전에 최대 체력인 적에게 가하는 피해량 +10%
   źródło: Passives.json :: dataList[id=1071221].desc
   limit: do 180 znaków
   EN: 1 ally with the fastest Speed: against enemies that used Defense Skills or were at max HP before attacking this turn: deal +10% damage
   PL: 1 Sojusznik z najwyższą Szybkością zadaje +10% obrażeń wrogom, którzy w tej turze użyli Umiejętności obrony albo mieli Maks. HP przed atakiem

## [000] W Corp. L4 Cleanup Agent - CCA — Heathcliff — W사 4등급 정리 요원 - CCA
- ID Tożsamości: `10713` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 99 · szybkość: 3–5 / 3–5 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Charge, Rupture

489. [Karta Tożsamości — tytuł] W사 4등급\n정리 요원 - CCA
   źródło: Personalities.json :: dataList[id=10713].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L4\nCleanup Agent -\nCCA
   PL: W Corp. L4\nAgentka Oczyszczania - CCA
490. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10713].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10713].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Karta Tożsamości — opis] 히스클리프의 열세번째 인격
   źródło: Personalities.json :: dataList[id=10713].desc
   limit: do 120 znaków
   EN: Heathcliff’s 13th Identity
   PL: Trzynasta Tożsamość Heathcliffa
493. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 혼잡승객 정리
   źródło: Skills_personality-07.json :: dataList[id=1071301].levelList[level=1].name ; dataList[id=1071301].levelList[level=2].name ; dataList[id=1071301].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Congestion Cleanup
   PL: Oczyszczanie Tłoku
494. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 3 증가
   źródło: Skills_personality-07.json :: dataList[id=1071301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +3 [Charge] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o 3
495. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL: [OnSucceedAttack] Nakłada 1 [Burst]
496. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Charge] 횟수가 6 이상이면, 합 위력 +1</style>
   źródło: Skills_personality-07.json :: dataList[id=1071301].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: <style="highlight">[WhenUse] At 6+ [Charge] Count, Clash Power +1</style>
   PL: <style="highlight">[WhenUse] Przy 6+ Liczniku [Charge] Moc Starcia +1</style>
497. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071301].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +3 [Charge] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o 3<style="highlight"></style>
498. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071301].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Burst]<style="highlight"></style>
499. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 자신의 [Charge]이 3 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Charge] 횟수 6당, 합 위력 +1 (최대 2)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071301].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: <style="highlight">[WhenUse] At 3+ [Charge], Coin Power +1\n[WhenUse] Clash Power +1 for every 6 [Charge] Count on self (max 2)</style>
   PL: <style="highlight">[WhenUse] Przy 3+ [Charge] Moc Monet +1\n[WhenUse] Moc Starcia +1 za każde 6 Licznika [Charge] (maks. 2)</style>
500. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-07.json :: dataList[id=1071301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +<style="highlight">4</style> [Charge] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o <style="highlight">4</style>
501. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071301].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] Inflict +1 [Burst] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada +1 Licznika [Burst]</style>
502. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-07.json :: dataList[id=1071301].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Burst]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Burst]
503. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 부스트 엘보 커터
   źródło: Skills_personality-07.json :: dataList[id=1071302].levelList[level=1].name ; dataList[id=1071302].levelList[level=2].name ; dataList[id=1071302].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 5 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Boost: Elbow Blade
   PL: Boost: Ostrze Łokcia
504. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [StartBattle] [ChargeForceField]을 (2 + 자신의 [Charge] 위력)만큼 얻음 (최대 6, 턴당 1회)\n[WhenUse] 자신의 [Charge] 횟수를 6 소모하여, 코인 위력 +1
   źródło: Skills_personality-07.json :: dataList[id=1071302].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [ChargeForceField], [Charge], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeForceField] = 충전 역장 / Charge Barrier; [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Gain [ChargeForceField] equal to (2 + [Charge] Potency on self) (max 6, 1 per turn)\n[WhenUse] Consume 6 [Charge] Count to gain +1 Coin Power
   PL: [StartBattle] Zyskuje [ChargeForceField] równy wartości (2 + Moc własnego [Charge]) (maks. 6, 1 raz na turę)\n[WhenUse] Zużywa 6 Licznika [Charge], aby zyskać Moc Monet +1
505. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 4 증가
   źródło: Skills_personality-07.json :: dataList[id=1071302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +4 [Charge] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o 4
506. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [StartBattle] [ChargeForceField]을 (2 + 자신의 [Charge] 위력)만큼 얻음 (최대 6, 턴당 1회)\n[WhenUse] 자신의 [Charge] 횟수를 6 소모하여, 코인 위력 +1<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071302].levelList[level=2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [ChargeForceField], [Charge], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeForceField] = 충전 역장 / Charge Barrier; [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Gain [ChargeForceField] equal to (2 + [Charge] Potency on self) (max 6, 1 per turn)\n[WhenUse] Consume 6 [Charge] Count to gain +1 Coin Power<style="highlight"></style>
   PL: [StartBattle] Zyskuje [ChargeForceField] równy wartości (2 + Moc własnego [Charge]) (maks. 6, 1 raz na turę)\n[WhenUse] Zużywa 6 Licznika [Charge], aby zyskać Moc Monet +1<style="highlight"></style>
508. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 <style="highlight">5</style> 증가
   źródło: Skills_personality-07.json :: dataList[id=1071302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +<style="highlight">5</style> [Charge] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o <style="highlight">5</style>
509. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071302].levelList[level=2].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-07.json :: dataList[id=1071302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [StartBattle] [ChargeForceField]을 (2 + 자신의 [Charge] 위력)만큼 얻음 (최대 6, 턴당 1회)\n[WhenUse] 자신의 [Charge] 횟수를 6 소모하여, 코인 위력 +1\n<style="highlight">[WhenUse] [Charge]이 3 이상이면 코인 위력 +1</style>
   źródło: Skills_personality-07.json :: dataList[id=1071302].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [ChargeForceField], [Charge], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeForceField] = 충전 역장 / Charge Barrier; [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Gain [ChargeForceField] equal to (2 + [Charge] Potency on self) (max 6, 1 per turn)\n[WhenUse] Consume 6 [Charge] Count to gain +1 Coin Power\n<style="highlight">[WhenUse] At 3+ [Charge], Coin Power +1</style>
   PL: [StartBattle] Zyskuje [ChargeForceField] równy wartości (2 + Moc własnego [Charge]) (maks. 6, 1 raz na turę)\n[WhenUse] Zużywa 6 Licznika [Charge], aby zyskać Moc Monet +1\n<style="highlight">[WhenUse] Przy 3+ [Charge] Moc Monet +1</style>
512. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 <style="highlight">6</style> 증가
   źródło: Skills_personality-07.json :: dataList[id=1071302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +<style="highlight">6</style> [Charge] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o <style="highlight">6</style>
513. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071302].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]<style="highlight"></style>
514. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] <style="highlight">3</style> 부여
   źródło: Skills_personality-07.json :: dataList[id=1071302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Burst]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Burst]
515. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 공간 절단 - CCA 오버드라이브
   źródło: Skills_personality-07.json :: dataList[id=1071303].levelList[level=3].name ; dataList[id=1071303].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 3 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Rip Space - CCA Overdrive
   PL: Rozcięcie Przestrzeni - CCA Overdrive
516. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] 자신의 [Charge] 위력이 3 이상이거나, 현재 체력이 최대 체력의 50% 미만이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n- 이 효과가 발동된 상태에서 합 패배 시, 최종 위력 +3\n[WhenUse] 자신의 [Charge] 횟수가 10 이상이면, [Charge] 횟수를 10 소모하여 코인 위력 +4
   źródło: Skills_personality-07.json :: dataList[id=1071303].levelList[level=3].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Charge], [SuperCoin], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Charge] = 충전 / Charge; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] If this unit has 3+ [Charge] Potency or less than 50% HP, convert all Coins in this Skill into [SuperCoin]\n- If this unit loses a Clash while this effect is active, Final Power +3\n[WhenUse] At 10+ [Charge] Count, consume 10 [Charge] Count to gain +4 Coin Power
   PL: [StartBattle] Jeżeli ma 3+ Mocy [Charge] albo mniej niż 50% HP, wszystkie monety tej Umiejętności stają się [SuperCoin]ami\n- Jeżeli przegra starcie przy aktywnym tym efekcie, Moc Końcowa +3\n[WhenUse] Przy 10+ Liczniku [Charge] zużywa 10 Licznika [Charge], aby zyskać Moc Monet +4
517. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071303].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Charge]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttackHead] Gain +2 [Charge] Count
   PL: [OnSucceedAttackHead] Zwiększa własny Licznik [Charge] o 2
518. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnStartCoin] [Charge] 횟수를 최대 10까지 소모하여, (이 코인에서 소모한 [Charge] 횟수)만큼 이 코인의 위력이 증가
   źródło: Skills_personality-07.json :: dataList[id=1071303].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [Charge]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Charge] = 충전 / Charge
   EN: [OnStartCoin] Consume up to 10 [Charge] Count to gain Coin Power for this Coin equal to ([Charge] Count consumed for this Coin)
   PL: [OnStartCoin] Zużywa do 10 Licznika [Charge], aby zwiększyć Moc tej monety o wartość (Licznik [Charge] zużyty przez tę monetę)
519. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071303].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] Nakłada 2 [Burst]
520. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 ([Charge] 위력 x 5)%만큼 참격 피해 (최대 25%)
   źródło: Skills_personality-07.json :: dataList[id=1071303].levelList[level=3].coinlist[#3].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Deal Slash damage equal to ([Charge] Potency x 5)% of this Coin's final damage (max 25%)
   PL: [OnSucceedAttack] Zadaje obrażenia Sieczne równe (Moc [Charge] x 5)% końcowych obrażeń tej monety (maks. 25%)
521. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [StartBattle] 자신의 [Charge] 위력이 3 이상이거나, 현재 체력이 최대 체력의 50% 미만이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n- 이 효과가 발동된 상태에서 합 패배 시, 최종 위력 +3\n[WhenUse] 자신의 [Charge] 횟수가 10 이상이면, [Charge] 횟수를 10 소모하여 코인 위력 +4\n<style="highlight">[WhenUse] 자신의 [Charge] 위력만큼 합 위력이 증가 (최대 5)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071303].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [Charge], [SuperCoin], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Charge] = 충전 / Charge; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] If this unit has 3+ [Charge] Potency or less than 50% HP, convert all Coins in this Skill into [SuperCoin]\n- If this unit loses a Clash while this effect is active, Final Power +3\n[WhenUse] At 10+ [Charge] Count, consume 10 [Charge] Count to gain +4 Coin Power\n<style="highlight">[WhenUse] Gain Clash Power equal to [Charge] Potency on self (max 5)</style>
   PL: [StartBattle] Jeżeli ma 3+ Mocy [Charge] albo mniej niż 50% HP, wszystkie monety tej Umiejętności stają się [SuperCoin]ami\n- Jeżeli przegra starcie przy aktywnym tym efekcie, Moc Końcowa +3\n[WhenUse] Przy 10+ Liczniku [Charge] zużywa 10 Licznika [Charge], aby zyskać Moc Monet +4\n<style="highlight">[WhenUse] Zyskuje Moc Starcia równą Mocy własnego [Charge] (maks. 5)</style>
522. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttackHead] 자신의 [Charge] 횟수 1 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Charge]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Charge] = 충전 / Charge
   EN: <style="highlight">[OnSucceedAttackHead] Gain +1 [Charge] Count</style>
   PL: <style="highlight">[OnSucceedAttackHead] Zwiększa własny Licznik [Charge] o 1</style>
523. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttackHead] 자신의 [Charge] 횟수 1 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 522 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 자신의 [Charge] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Charge]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttackHead] Gain +2 [Charge] Count<style="highlight"></style>
   PL: [OnSucceedAttackHead] Zwiększa własny Licznik [Charge] o 2<style="highlight"></style>
525. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnStartCoin] [Charge] 횟수를 최대 10까지 소모하여, (이 코인에서 소모한 [Charge] 횟수)만큼 이 코인의 위력이 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071303].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Charge]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Charge] = 충전 / Charge
   EN: [OnStartCoin] Consume up to 10 [Charge] Count to gain Coin Power for this Coin equal to ([Charge] Count consumed for this Coin)<style="highlight"></style>
   PL: [OnStartCoin] Zużywa do 10 Licznika [Charge], aby zwiększyć Moc tej monety o wartość (Licznik [Charge] zużyty przez tę monetę)<style="highlight"></style>
526. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071303].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Burst]<style="highlight"></style>
527. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 ([Charge] 위력 x <style="highlight">10</style>)%만큼 참격 피해 (최대 <style="highlight">50%</style>)
   źródło: Skills_personality-07.json :: dataList[id=1071303].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Deal Slash damage equal to ([Charge] Potency x <style="highlight">10</style>)% of this Coin's final damage (max <style="highlight">50%</style>)
   PL: [OnSucceedAttack] Zadaje obrażenia Sieczne równe (Moc [Charge] x <style="highlight">10</style>)% końcowych obrażeń tej monety (maks. <style="highlight">50%</style>)
528. [Obrona (ulepszenia 1,4) — nazwa] CCA 과충전
   źródło: Skills_personality-07.json :: dataList[id=1071304].levelList[level=1].name ; dataList[id=1071304].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 3 · monety: 1 (+10)
   limit: do 40 znaków
   EN: CCA Overcharge
   PL: CCA Przeładowanie
529. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] 자신의 [Charge] 횟수가 15 미만이면, 아래 효과 발동\n- 다음 턴에 [WOverCharge] 얻음 (턴당 1회)\n- 턴 종료 시 자신의 가장 높은 흐트러짐 구간 1개 제거 (전투당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071304].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [Charge], [WOverCharge]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [Charge] = 충전 / Charge; [WOverCharge] = 과충전 / Overcharge
   EN: [CanDuelGuard]\n[StartBattle] At less than 15 [Charge] Count, gain the following effects:\n- Gain [WOverCharge] next turn (max 1 per turn)\n- Turn End: Remove this unit's first Stagger Threshold (once per Encounter)
   PL: [CanDuelGuard]\n[StartBattle] Przy mniej niż 15 Licznika [Charge] uruchamia poniższe efekty:\n- Zyskuje [WOverCharge] w następnej turze (maks. 1 na turę)\n- Na koniec tury usuwa pierwszy Próg Oszołomienia tej jednostki (1 raz na spotkanie)
530. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-07.json :: dataList[id=1071304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
531. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[StartBattle] 자신의 [Charge] 횟수가 15 미만이면, 아래 효과 발동\n- 다음 턴에 [WOverCharge] 얻음 (턴당 1회)\n- 턴 종료 시 자신의 가장 높은 흐트러짐 구간 1개 제거 (전투 당 1회)\n<style="highlight">- 턴 종료 시 '공간 절단 - CCA 오버드라이브' 1개를 다음 턴에 사용할 스킬 목록에 추가함 (턴당 1회)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071304].levelList[level=4].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [StartBattle], [Charge], [WOverCharge]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [Charge] = 충전 / Charge; [WOverCharge] = 과충전 / Overcharge
   EN: [CanDuelGuard]\n[StartBattle] At less than 15 [Charge] Count, gain the following effects:\n- Gain [WOverCharge] next turn (max 1 per turn)\n- Turn End: Remove this unit's first Stagger Threshold (once per Encounter)\n<style="highlight">- Turn End: Add 1 Rip Space - CCA Overdrive to the list of Skills for the next upcoming turn (once per turn)</style>
   PL: [CanDuelGuard]\n[StartBattle] Przy mniej niż 15 Licznika [Charge] uruchamia poniższe efekty:\n- Zyskuje [WOverCharge] w następnej turze (maks. 1 na turę)\n- Na koniec tury usuwa pierwszy Próg Oszołomienia tej jednostki (1 raz na spotkanie)\n<style="highlight">- Na koniec tury dodaje 1 „Rozcięcie Przestrzeni - CCA Overdrive” do listy Umiejętności na następną turę (1 raz na turę)</style>
532. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Pasywka bojowa (od ulepszenia 1) — nazwa] 방어지향 충전
   źródło: Passives.json :: dataList[id=1071301].name
   limit: do 40 znaków
   EN: Defence-Oriented Charge
   PL: Ładowanie Nastawione na Obronę
534. [Pasywka bojowa (od ulepszenia 1) — opis] - 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다 [Charge] 1 얻음\n- 턴 시작시, 자신의 [Charge] 위력만큼 [DefenseUp] 얻음 (최대 6)
   źródło: Passives.json :: dataList[id=1071301].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [DefenseUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: - Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\n- Turn Start: Gain [DefenseUp] equal to [Charge] Potency on self (max 6)
   PL: - Za każde łączne zużycie 10 własnego Licznika [Charge] podczas walki zyskuje 1 [Charge]\n- Na początku tury zyskuje [DefenseUp] równy Mocy własnego [Charge] (maks. 6)
535. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — nazwa] 컨제스쳔 클리닝 아머
   źródło: Passives.json :: dataList[id=1071311].name
   limit: do 40 znaków
   EN: Congestion Cleaning Armour
   PL: Zbroja Oczyszczania Tłoku
536. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — opis] - 전투 시작시 자신의 체력이 50% 미만이면, ([Charge] 위력 x 5)만큼 보호막 얻음 (최대 25)\n- 피격 직전, (자신의 [Charge] 위력)만큼 보호막 얻음 (최대 5, 턴 당 최대 3회)\n- 자신의 스킬로 [Charge] 횟수 최대치를 초과하여 [Charge] 횟수를 얻으면, 최대치를 초과한 [Charge] 횟수 1 당 해당 스킬 피해량 +3% (최대 15%)
   źródło: Passives.json :: dataList[id=1071311].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: - Combat Start: If this unit has less than 50% HP, gain Shield equal to ([Charge] Potency x 5) (max 25)\n- Immediately before getting hit, gain Shield equal to ([Charge] Potency on self) (max 5, 3 times per turn)\n- If this unit gains [Charge] Count past the Max [Charge] Count Cap by using a Skill, the Skill deals +3% damage for every [Charge] Count that exceeds the Max [Charge] Count Cap (max 15%)
   PL: - Na początku walki, jeżeli ma mniej niż 50% HP, zyskuje Tarczę równą (Moc [Charge] x 5) (maks. 25)\n- Bezpośrednio przed trafieniem zyskuje Tarczę równą (Moc własnego [Charge]) (maks. 5, maks. 3 razy na turę)\n- Jeżeli zyska Licznik [Charge] ponad maksimum Umiejętnością, ta Umiejętność zadaje +3% obrażeń za każde 1 Licznika [Charge] ponad maksimum (maks. 15%)
537. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — nazwa] ‘언젠가 결항 열차용 정리 장비도 노려볼수있겠지’
   źródło: Passives.json :: dataList[id=1071321].name
   limit: do 70 znaków
   EN: One day I'll wear me Armour for Cancelled Trains
   PL: Pewnego dnia nosił będę Zbroję dla Odwołanych Pociągów
538. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — opis] - 전투 시작시 편성 순서가 가장 빠른 아군이 자신의 스킬로 [Charge] 횟수 최대치를 초과하여 [Charge] 횟수를 얻으면, 초과한 [Charge] 횟수 1 당 다음 턴에 [ChargeForceField] 1 얻음 (최대 3. E.G.O 스킬 포함)
   źródło: Passives.json :: dataList[id=1071321].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: [Charge], [ChargeForceField]
   znaczenie tagów: [Charge] = 충전 / Charge; [ChargeForceField] = 충전 역장 / Charge Barrier
   EN: - Combat Start: If the unit with the earliest Deployment Order gains [Charge] Count past the Max [Charge] Count Cap by using a Skill, the unit gains 1 [ChargeForceField] next turn for every [Charge] Count that exceeds the Max [Charge] Count Cap (max 3, including E.G.O Skills)
   PL: - Na początku walki, jeżeli Sojusznik przydzielony najwcześniej na pozycji zyska Umiejętnością Licznik [Charge] ponad maksimum, zyskuje 1 [ChargeForceField] w następnej turze za każde 1 Licznika [Charge] ponad maksimum (maks. 3, łącznie z Umiejętnościami E.G.O)

## [000] Heishou Pack - You Branch Adept — Heathcliff — 흑수 - 유 필두
- ID Tożsamości: `10714` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 92 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture, Burn

539. [Karta Tożsamości — tytuł] 흑수 - 유 필두
   źródło: Personalities.json :: dataList[id=10714].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heishou Pack -\nYou Branch Adept
   PL: Wataha Heishou -\nGałąź You, Adept
540. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10714].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10714].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Karta Tożsamości — opis] 히스클리프의 열네번째 인격
   źródło: Personalities.json :: dataList[id=10714].desc
   limit: do 120 znaków
   EN: Heathcliff’s 14th Identity
   PL: Czternasta Tożsamość Heathcliffa
543. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 쪼아먹는다
   źródło: Skills_personality-07.json :: dataList[id=1071401].levelList[level=1].name ; dataList[id=1071401].levelList[level=2].name ; dataList[id=1071401].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 2 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Peck 'em
   PL: Dziobanie
544. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [StartDuel] 대상과 자신에게 [Combustion] 1 부여, [Combustion] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartDuel], [Combustion]
   znaczenie tagów: [StartDuel] = [합 시작 시] / [Clash Start]; [Combustion] = 화상 / Burn
   EN: [StartDuel] Apply 1 [Combustion] and +1 [Combustion] Count to target and self
   PL: [StartDuel] Nakłada 1 [Combustion] i zwiększa Licznik [Combustion] o 1 na celu i sobie
545. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071401].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1071401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071401].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1071401].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1071401].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]
547. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Combustion]과 [Burst]의 합이 6 이상이면, 코인 위력 +1</style>\n[StartDuel] 대상과 자신에게 [Combustion] 1 부여, [Combustion] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071401].levelList[level=2].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Combustion], [Burst], [StartDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Burst] = 파열 / Rupture; [StartDuel] = [합 시작 시] / [Clash Start]
   EN: <style="highlight">[WhenUse] If target has 6+ ([Combustion] + [Burst]), Coin Power +1</style>\n[StartDuel] Apply 1 [Combustion] and +1 [Combustion] Count to target and self
   PL: <style="highlight">[WhenUse] Przy 6+ (suma [Combustion] i [Burst] celu) Moc Monet +1</style>\n[StartDuel] Nakłada 1 [Combustion] i zwiększa Licznik [Combustion] o 1 na celu i sobie
548. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 [Combustion]과 [Burst]의 합이 6 이상이면, 코인 위력 +1\n<style="highlight">[WhenUse] 자신의 [Combustion] 10당, 합 위력 +1 (최대 2)</style>\n[StartDuel] 대상과 자신에게 [Combustion] 1 부여, [Combustion] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071401].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Combustion], [Burst], [StartDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Burst] = 파열 / Rupture; [StartDuel] = [합 시작 시] / [Clash Start]
   EN: [WhenUse] If target has 6+ ([Combustion] + [Burst]), Coin Power +1\n<style="highlight">[WhenUse] Clash Power +1 for every 10 [Combustion] on self (max 2)</style>\n[StartDuel] Apply 1 [Combustion] and +1 [Combustion] Count to target and self
   PL: [WhenUse] Przy 6+ (suma [Combustion] i [Burst] celu) Moc Monet +1\n<style="highlight">[WhenUse] Moc Starcia +1 za każde 10 [Combustion] (maks. 2)</style>\n[StartDuel] Nakłada 1 [Combustion] i zwiększa Licznik [Combustion] o 1 na celu i sobie
549. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071401].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttackHead] Inflict +1 [Burst] Count</style>
   PL: <style="highlight">[OnSucceedAttackHead] Zwiększa Licznik [Burst] celu o 1</style>
550. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 발톱으로 찢어주지
   źródło: Skills_personality-07.json :: dataList[id=1071402].levelList[level=1].name ; dataList[id=1071402].levelList[level=2].name ; dataList[id=1071402].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Mutilating Talons
   PL: Rozdzieranie Szponami
551. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [StartDuel] 대상과 자신에게 [Combustion] 1 부여, [Combustion] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071402].levelList[level=1].desc
   (powtórzenie elementu 544 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1071402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1071402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071402].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1071402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 얻음, 자신의 [Combustion] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071402].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1071402].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1071402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Gain 3 [Combustion] and +1 [Combustion] Count
   PL: [OnSucceedAttack] Zyskuje 3 [Combustion] i zwiększa własny Licznik [Combustion] o 1
555. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 자신에게 [ChickenStance]이 있거나, 자신의 현재 체력이 최대 체력의 50% 미만이면, 이 코인 재사용 (스킬당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071402].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1071402].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [ChickenStance]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [ChickenStance] = 혈염 [血炎] / Bloodflame [血炎]
   EN: [OnSucceedAttackHead] If this unit has [ChickenStance], or if this unit has less than 50% HP, Reuse this Coin (once per Skill)
   PL: [OnSucceedAttackHead] Jeżeli ma [ChickenStance] albo ma mniej niż 50% HP, ponownie używa tej monety (1 raz na Umiejętność)
556. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Combustion]과 [Burst]의 합이 6 이상이면, 코인 위력 +1</style>\n[StartDuel] 대상과 자신에게 [Combustion] 1 부여, [Combustion] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071402].levelList[level=2].desc
   (powtórzenie elementu 547 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Combustion]과 [Burst]의 합이 6 이상이면, 코인 위력 +1\n<style="highlight">[WhenUse] 자신의 [Combustion] 10당, 합 위력 +1 (최대 2)</style>\n[StartDuel] 대상과 자신에게 [Combustion] 1 부여, [Combustion] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071402].levelList[level=4].desc
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [Combustion] 횟수 1 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071402].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[OnSucceedAttackHead] Inflict +1 [Combustion] Count</style>
   PL: <style="highlight">[OnSucceedAttackHead] Zwiększa własny Licznik [Combustion] o 1</style>
559. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071402].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 이 코인 최종 피해량의 (자신의 [Combustion] x2)% 만큼 분노 피해 (최대 20%)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071402].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[OnSucceedAttack] Deal (([Combustion] on self x 2)% of this Coin's final damage) Wrath damage (max 20%)</style>
   PL: <style="highlight">[OnSucceedAttack] Zadaje obrażenia Gniewu równe (2 x Moc własnego [Combustion])% końcowych obrażeń tej monety (maks. 20%)</style>
561. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttackHead] 자신에게 [ChickenStance]이 있거나, 자신의 현재 체력이 최대 체력의 50% 미만이면, 이 코인 재사용 (스킬당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071402].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 555 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 혈염난무[血炎亂舞]
   źródło: Skills_personality-07.json :: dataList[id=1071403].levelList[level=3].name ; dataList[id=1071403].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Bloodflame Massacre [血炎亂舞]
   PL: Rzeź Krwawego Płomienia [血炎亂舞]
563. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WideAreaRampage]\n[StartBattle] 자신에게 [ChickenStance]이 있거나, 자신의 현재 체력이 최대 체력의 50% 미만이면 모든 코인이 [SuperCoin]으로 변경됨\n[BeforeUse] [ChickenFightlust]이 20이면, '혈천하계무난도'로 발동됨\n[WhenUse] [ChickenStance] 3 얻음\n[EndSkill] 자신의 [Combustion] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071403].levelList[level=3].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [StartBattle], [ChickenStance], [SuperCoin], [BeforeUse], [ChickenFightlust], [WhenUse], [EndSkill], [Combustion]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [StartBattle] = [전투 시작시] / [Combat Start]; [ChickenStance] = 혈염 [血炎] / Bloodflame [血炎]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BeforeUse] = [사용전] / [Before Use]; [ChickenFightlust] = 혈투본능 / Battleblood Instinct; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: [WideAreaRampage]\n[StartBattle] If this unit has [ChickenStance], or if this unit has less than 50% HP, convert all Coins to [SuperCoin]s\n[BeforeUse] At 20 [ChickenFightlust], activate 'Rooster's Rampaging Blades Under the Ensanguined Heaven' instead\n[WhenUse] Gain 3 [ChickenStance]\n[EndSkill] Gain +2 [Combustion] Count
   PL: [WideAreaRampage]\n[StartBattle] Jeżeli ma [ChickenStance] albo ma mniej niż 50% HP, wszystkie monety stają się [SuperCoin]ami\n[BeforeUse] Przy 20 [ChickenFightlust] stosuje się jako „Roześniane Ostrza Koguta pod Zakrwawionym Niebem”\n[WhenUse] Zyskuje 3 [ChickenStance]\n[EndSkill] Zwiększa własny Licznik [Combustion] o 2
564. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상과 자신에게 [Combustion] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1071403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Apply 2 [Combustion] to target and self
   PL: [OnSucceedAttack] Nakłada 2 [Combustion] na cel i siebie
565. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신의 현재 체력이 50% 이상이면, 자신의 [Combustion] 위력만큼 [Combustion] 피해를 받음
   źródło: Skills_personality-07.json :: dataList[id=1071403].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1071403].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] At 50%+ HP, take [Combustion] damage by [Combustion] Potency on self
   PL: [OnSucceedAttackHead] Przy 50%+ HP otrzymuje obrażenia [Combustion] równe Mocy własnego [Combustion]
566. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상과 자신에게 [Combustion] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071403].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1071403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 자신의 현재 체력이 50% 이상이면, 자신의 [Combustion] 위력만큼 [Combustion] 피해를 받음
   źródło: Skills_personality-07.json :: dataList[id=1071403].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1071403].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상과 자신에게 [Combustion] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071403].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1071403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttackHead] 자신의 현재 체력이 50% 이상이면, 자신의 [Combustion] 위력만큼 [Combustion] 피해를 받음
   źródło: Skills_personality-07.json :: dataList[id=1071403].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1071403].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_personality-07.json :: dataList[id=1071403].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1071403].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Burst]
571. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WideAreaRampage]\n<style="highlight">자신의 [Combustion] 1당, 피해량 +1.5% (최대 30%)</style>\n[StartBattle] 자신에게 [ChickenStance]이 있거나, 자신의 현재 체력이 최대 체력의 50% 미만이면 모든 코인이 [SuperCoin]으로 변경됨\n[BeforeUse] [ChickenFightlust]이 20이면, '혈천하계무난도'로 발동됨\n[WhenUse] [ChickenStance] 3 얻음\n<style="highlight">[WhenUse] 메인 타겟의 [Combustion]과 [Burst]의 합 6당 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 잃은 체력 20%당 합 위력 +1 (최대 3)</style>\n[EndSkill] 자신의 [Combustion] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071403].levelList[level=4].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WideAreaRampage], [Combustion], [StartBattle], [ChickenStance], [SuperCoin], [BeforeUse], [ChickenFightlust], [WhenUse], [Burst], [EndSkill]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [Combustion] = 화상 / Burn; [StartBattle] = [전투 시작시] / [Combat Start]; [ChickenStance] = 혈염 [血炎] / Bloodflame [血炎]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BeforeUse] = [사용전] / [Before Use]; [ChickenFightlust] = 혈투본능 / Battleblood Instinct; [WhenUse] = [사용시] / [On Use] …
   EN: [WideAreaRampage]\n<style="highlight">Deal +1.5% damage for every [Combustion] on self (max 30%)</style>\n[StartBattle] If this unit has [ChickenStance], or if this unit has less than 50% HP, convert all Coins to [SuperCoin]s\n[BeforeUse] At 20 [ChickenFightlust], activate 'Rooster's Rampaging Blades Under the Ensanguined Heaven' instead\n[WhenUse] Gain 3 [ChickenStance]\n<style="highlight">[WhenUse] Coin Power +1 for every 6 ([Combustion] + [Burst]) on the main target (max 2)\n[WhenUse] Clash Power +1 for every 20% missing HP on self (max 3)</style>\n[EndSkill] Gain +2 [Combustion] Count
   PL: [WideAreaRampage]\n<style="highlight">Zadaje +1.5% obrażeń za każde 1 [Combustion] (maks. 30%)</style>\n[StartBattle] Jeżeli ma [ChickenStance] albo ma mniej niż 50% HP, wszystkie monety stają się [SuperCoin]ami\n[BeforeUse] Przy 20 [ChickenFightlust] stosuje się jako „Roześniane Ostrza Koguta pod Zakrwawionym Niebem”\n[WhenUse] Zyskuje 3 [ChickenStance]\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 (suma [Combustion] i [Burst] głównego celu) (maks. 2)\n[WhenUse] Moc Starcia +1 za każde 20% brakującego HP (maks. 3)</style>\n[EndSkill] Zwiększa własny Licznik [Combustion] o 2
572. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 이 코인 최종 피해량의 (자신의 [Combustion] + 메인 타겟의 [Combustion])%만큼 모든 공격 대상에게 탐식 피해 (최대 20%)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071403].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[OnSucceedAttack] Deal (([Combustion] on self + [Combustion] on the main target)% of this Coin's final damage) Gluttony damage against all targets (max 20%)</style>
   PL: <style="highlight">[OnSucceedAttack] Zadaje obrażenia Obżarstwa równe (suma Mocy własnego [Combustion] i [Combustion] głównego celu)% końcowych obrażeń tej monety wszystkim celom ataku (maks. 20%)</style>
573. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 혈천하계무난도[血天下鷄舞亂刀]
   źródło: Skills_personality-07.json :: dataList[id=1071405].levelList[level=3].name ; dataList[id=1071405].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 5 · monety: 4 (+3)
   limit: do 90 znaków
   EN: Rooster's Rampaging Blades Under the Ensanguined Heaven [血天下鷄舞亂刀]
   PL: Roześniane Ostrza Koguta pod Zakrwawionym Niebem [血天下鷄舞亂刀]
574. [Umiejętność 4 (×0) (ulepszenie 3) — opis] [WideAreaRampage]\n[WhenUse] [ChickenStance] 3 얻음\n[WinDuel] [Combustion] 10 얻음\n[EndSkill] [ChickenFightlust] 모두 소모\n[EndSkill] 자신의 [Combustion]이 20 초과했으면, 초과한 [Combustion]에서 최대 25 소모하여 최대 체력의 (소모한 [Combustion] x 2)%만큼 체력 회복
   źródło: Skills_personality-07.json :: dataList[id=1071405].levelList[level=3].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [WhenUse], [ChickenStance], [WinDuel], [Combustion], [EndSkill], [ChickenFightlust]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [ChickenStance] = 혈염 [血炎] / Bloodflame [血炎]; [WinDuel] = [합 승리시] / [Clash Win]; [Combustion] = 화상 / Burn; [EndSkill] = [공격 종료시] / [Attack End]; [ChickenFightlust] = 혈투본능 / Battleblood Instinct
   EN: [WideAreaRampage]\n[WhenUse] Gain 3 [ChickenStance]\n[WinDuel] Gain 10 [Combustion]\n[EndSkill] Consume all [ChickenFightlust]\n[EndSkill] At more than 20 [Combustion], consume up to 25 excess [Combustion] and heal ([Combustion] consumed x 2)% HP
   PL: [WideAreaRampage]\n[WhenUse] Zyskuje 3 [ChickenStance]\n[WinDuel] Zyskuje 10 [Combustion]\n[EndSkill] Zużywa całe [ChickenFightlust]\n[EndSkill] Przy ponad 20 [Combustion] zużywa do 25 nadmiarowego [Combustion] i odzyskuje HP równe (2 x zużyte [Combustion])% Maks. HP
575. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-07.json :: dataList[id=1071405].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1071405].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071405].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1071405].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Burst]
577. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-07.json :: dataList[id=1071405].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1071405].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071405].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1071405].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +2 [Combustion] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Combustion] o 2
579. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-07.json :: dataList[id=1071405].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1071405].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071405].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1071405].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-07.json :: dataList[id=1071405].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1071405].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071405].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1071405].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL: [OnSucceedAttack] Nakłada 2 [Combustion]
583. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 자신에게 [Combustion]이 20 이상 있거나, 자신의 현재 체력이 최대 체력의 50% 미만이면, 이 코인 재사용 (스킬당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071405].levelList[level=3].coinlist[#3].coindescs[#2].desc ; dataList[id=1071405].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If this unit has 20+ [Combustion], or if this unit has less than 50% HP, Reuse this Coin (once per Skill)
   PL: [OnSucceedAttack] Jeżeli ma 20+ [Combustion] albo mniej niż 50% HP, ponownie używa tej monety (1 raz na Umiejętność)
584. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [WideAreaRampage]\n<style="highlight">자신의 [Combustion] 1당, 피해량 +3% (최대 60%)\n대상과 자신의 잃은 체력 합 2%당 피해량 +1% (최대 50%)</style>\n[WhenUse] [ChickenStance] 3 얻음\n<style="highlight">[WhenUse] 메인 타겟의 [Combustion]과 [Burst]의 합 6당 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 잃은 체력 20%당 합 위력 +1 (최대 3)</style>\n[WinDuel] [Combustion] 10 얻음\n[EndSkill] [ChickenFightlust] 모두 소모\n[EndSkill] 자신의 [Combustion]이 20 초과했으면, 초과한 [Combustion]에서 최대 25 소모하여 최대 체력의 (소모한 [Combustion] x 2)%만큼 체력 회복
   źródło: Skills_personality-07.json :: dataList[id=1071405].levelList[level=4].desc
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WideAreaRampage], [Combustion], [WhenUse], [ChickenStance], [Burst], [WinDuel], [EndSkill], [ChickenFightlust]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [Combustion] = 화상 / Burn; [WhenUse] = [사용시] / [On Use]; [ChickenStance] = 혈염 [血炎] / Bloodflame [血炎]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [EndSkill] = [공격 종료시] / [Attack End]; [ChickenFightlust] = 혈투본능 / Battleblood Instinct
   EN: [WideAreaRampage]\n<style="highlight">Deal +3% damage for every [Combustion] on self (max 60%)\nDeal +1% damage for every 2% (missing HP percentage on target + missing HP percentage on self) (max 50%)</style>\n[WhenUse] Gain 3 [ChickenStance]\n<style="highlight">[WhenUse] Coin Power +1 for every 6 ([Combustion] + [Burst]) on the main target (max 2)\n[WhenUse] Clash Power +1 for every 20% missing HP on self (max 3)</style>\n[WinDuel] Gain 10 [Combustion]\n[EndSkill] Consume all [ChickenFightlust]\n[EndSkill] At more than 20 [Combustion], consume up to 25 excess [Combustion] and heal ([Combustion] consumed x 2)% HP
   PL: [WideAreaRampage]\n<style="highlight">Zadaje +3% obrażeń za każde 1 [Combustion] (maks. 60%)\nZadaje +1% obrażeń za każde 2% (suma brakującego HP celu i własnego) (maks. 50%)</style>\n[WhenUse] Zyskuje 3 [ChickenStance]\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 (suma [Combustion] i [Burst] głównego celu) (maks. 2)\n[WhenUse] Moc Starcia +1 za każde 20% brakującego HP (maks. 3)</style>\n[WinDuel] Zyskuje 10 [Combustion]\n[EndSkill] Zużywa całe [ChickenFightlust]\n[EndSkill] Przy ponad 20 [Combustion] zużywa do 25 nadmiarowego [Combustion] i odzyskuje HP równe (2 x zużyte [Combustion])% Maks. HP
585. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 4 — opis] <style="highlight">[OnSucceedAttack] 이 코인의 최종 피해량 20%만큼 모든 공격 대상에게 분노 피해를 줌\n- 마지막에 사용하는 코인이면, 해당 피해량만큼 체력 회복</style>
   źródło: Skills_personality-07.json :: dataList[id=1071405].levelList[level=4].coinlist[#3].coindescs[#3].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] Deal (20% of this Coin's final damage) Wrath damage against all targets\n- If this is the final Coin, heal HP by the amount of damage the above effect dealt</style>
   PL: <style="highlight">[OnSucceedAttack] Zadaje obrażenia Gniewu równe 20% końcowych obrażeń tej monety wszystkim celom ataku\n- Jeżeli to ostatnia moneta, odzyskuje HP równe obrażeniom zadanym przez powyższy efekt</style>
586. [Obrona (ulepszenia 1,4) — nazwa] 먹잇감이군
   źródło: Skills_personality-07.json :: dataList[id=1071404].levelList[level=1].name ; dataList[id=1071404].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: More Grub for Us
   PL: Więcej Żarcia dla Nas
587. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 다음 턴에 [ChickenStance] 3 얻음\n[WhenUse] 자신에게 [ChickenStance]이 있으면, 코인 위력 +1\n[StartDuel] 자신의 [Combustion] 횟수 3 증가 (턴당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071404].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [ChickenStance], [StartDuel], [Combustion]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [ChickenStance] = 혈염 [血炎] / Bloodflame [血炎]; [StartDuel] = [합 시작 시] / [Clash Start]; [Combustion] = 화상 / Burn
   EN: [DuelCounter]\n[WhenUse] Gain 3 [ChickenStance] next turn\n[WhenUse] If this unit has [ChickenStance], Coin Power +1\n[StartDuel] Gain +3 [Combustion] Count (once per turn)
   PL: [DuelCounter]\n[WhenUse] Zyskuje 3 [ChickenStance] w następnej turze\n[WhenUse] Jeżeli ma [ChickenStance], Moc Monet +1\n[StartDuel] Zwiększa własny Licznik [Combustion] o 3 (1 raz na turę)
588. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071404].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1071404].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]
589. [Obrona (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071404].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1071404].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[WhenUse] 다음 턴에 [ChickenStance] 3 얻음\n<style="highlight">[WhenUse] 대상의 [Combustion]과 [Burst]의 합이 10 이상이면, 기본 위력 +1</style>\n[WhenUse] 자신에게 [ChickenStance]이 있으면, 코인 위력 +1\n<style="highlight">[WhenUse] 자신이 이번 전투에서 잃은 체력 누적 3%당, 이 스킬 피해량 +1% (최대 30%)</style>\n[StartDuel] 자신의 [Combustion] 횟수 3 증가 (턴당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071404].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [WhenUse], [ChickenStance], [Combustion], [Burst], [StartDuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [ChickenStance] = 혈염 [血炎] / Bloodflame [血炎]; [Combustion] = 화상 / Burn; [Burst] = 파열 / Rupture; [StartDuel] = [합 시작 시] / [Clash Start]
   EN: [DuelCounter]\n[WhenUse] Gain 3 [ChickenStance] next turn\n<style="highlight">[WhenUse] If target has 10+ ([Combustion] + [Burst]), Base Power +1</style>\n[WhenUse] If this unit has [ChickenStance], Coin Power +1\n<style="highlight">[WhenUse] This Skill deals +1% damage for every 3% HP this unit cumulatively lost in this Encounter (max 30%)</style>\n[StartDuel] Gain +3 [Combustion] Count (once per turn)
   PL: [DuelCounter]\n[WhenUse] Zyskuje 3 [ChickenStance] w następnej turze\n<style="highlight">[WhenUse] Przy 10+ (suma [Combustion] i [Burst] celu) Moc Bazowa +1</style>\n[WhenUse] Jeżeli ma [ChickenStance], Moc Monet +1\n<style="highlight">[WhenUse] Ta Umiejętność zadaje +1% obrażeń za każde 3% łącznie straconego HP w tym spotkaniu (maks. 30%)</style>\n[StartDuel] Zwiększa własny Licznik [Combustion] o 3 (1 raz na turę)
591. [Pasywka bojowa (od ulepszenia 1) — nazwa] 투계
   źródło: Passives.json :: dataList[id=1071402].name
   limit: do 40 znaków
   EN: Gamefowl
   PL: Walki Kogutów
592. [Pasywka bojowa (od ulepszenia 1) — opis] 홍원 군주 홍루와 [HeishouCombo] 발동 시, 홍원 군주 홍루가 [HeishouComboCountHonglu]으로 아래 효과 얻음\n- 자신의 기본 스킬로 공격 적중 시 해당 적에게 가한 탐식 피해의 5%만큼 분노 피해를 줌\n\n[Combustion] 피해로 흐트러짐 상태가 되거나 체력이 1 미만으로 감소하지 않음\n\n대기 해제 또는 복귀로 등장한 턴에 [ChickenStance] 3, [Combustion] 횟수 3 얻음
   źródło: Passives.json :: dataList[id=1071402].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [HeishouCombo], [HeishouComboCountHonglu], [Combustion], [ChickenStance]
   znaczenie tagów: [HeishouCombo] = 존명 / Exalted Command; [HeishouComboCountHonglu] = 흑수환염[黑獣丸染] / Heishou Bolus Contamination [黑獣丸染]; [Combustion] = 화상 / Burn; [ChickenStance] = 혈염 [血炎] / Bloodflame [血炎]
   EN: When activating [HeishouCombo], The Lord of Hongyuan Hong Lu gains the following effect as the [HeishouComboCountHonglu] effect:\n- On Hit using this unit's Base Skill: Deal 5% of Gluttony damage dealt as Wrath damage\n\nCannot be Staggered or fall below 1 HP due to [Combustion] damage.\n\nGain 3 [ChickenStance] and +3 [Combustion] Count in the same turn it Substitutes or Returns in.
   PL: Przy uruchomieniu [HeishouCombo] Władca Hongyuan Hong Lu zyskuje poniższy efekt jako efekt [HeishouComboCountHonglu]:\n- Przy trafieniu własną podstawową Umiejętnością ataku zadaje obrażenia Gniewu równe 5% obrażeń Obżarstwa zadanych temu wrogowi\n\nNie może zostać Ogłuszony ani spaść poniżej 1 HP przez obrażenia [Combustion].\n\nW turze Wejścia z rezerwy albo Powrotu zyskuje 3 [ChickenStance] i zwiększa Licznik [Combustion] o 3
593. [Pasywka bojowa (od ulepszenia 1) — nazwa] 염조불사전[炎鳥不死戰]
   źródło: Passives.json :: dataList[id=1071403].name
   limit: do 60 znaków
   EN: Flame Rooster's Death Defiance [炎鳥不死戰]
   PL: Ognisty Kogut Obchodzi Śmierć [炎鳥不死戰]
594. [Pasywka bojowa (od ulepszenia 1) — opis] 이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고, 해당 턴 동안 체력이 1로 유지됨\n이후 다음 턴 시작 시 자신의 최대 체력의 (20 + 자신의 [Combustion])%만큼 체력 회복 후 자신의 [Combustion] 소멸 (최대 49%, 전투 당 1회)
   źródło: Passives.json :: dataList[id=1071403].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: In this Encounter, when this unit takes damage that brings their HP down to 0, nullify that damage; then, this unit's HP cannot drop below 1 for the turn.\nThen, at the next Turn Start, heal (20 + [Combustion] on self)% HP, and remove all [Combustion] on self (max 49%; once per Encounter)
   PL: W tym spotkaniu, gdy ta jednostka otrzymuje obrażenia redukujące HP do 0, unieważnia te obrażenia; jej HP nie spada poniżej 1 w tej turze\nPóźniej, na początku następnej tury odzyskuje HP równe (20 + własne [Combustion])% Maks. HP, po czym jej [Combustion] wygasa (maks. 49%; 1 raz na spotkanie)
595. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 불사 발동
   źródło: Passives.json :: dataList[id=1071403].summary
   limit: do 120 znaków
   EN: Defy death
   PL: Wyzwanie Śmierci
596. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — nazwa] 맞부딪치는 혈투
   źródło: Passives.json :: dataList[id=1071401].name
   limit: do 40 znaków
   EN: Bloody Storm of Blades
   PL: Krwawa Nawałnica Ostrzy
597. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — opis] 전투 시작시 자신의 잃은 체력 20%당 공격 레벨 증가, 방어 레벨 증가 1 얻음 (최대 3)\n\n아래의 조건 만족 시 [ChickenFightlust] 얻음 (턴당 최대 10)\n- 합 시작 시 3 얻음\n- 기본 공격 스킬 적중시 또는 자신이 [Combustion] 피해를 받을 때 1 얻음\n자신의 현재 체력이 50% 미만이면, 추가 1 얻음\n- 적 처치 시 5 얻음
   źródło: Passives.json :: dataList[id=1071401].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [ChickenFightlust], [Combustion]
   znaczenie tagów: [ChickenFightlust] = 혈투본능 / Battleblood Instinct; [Combustion] = 화상 / Burn
   EN: Combat Start: gain 1 Offense Level Up and 1 Defense Level Up for every 20% missing HP on self (max 3)\n\nGain [ChickenFightlust] when meeting one of the following conditions: (10 per turn)\n- Gain 3 at Clash Start\n- Gain 1 when this unit hits with a Base Attack Skill or when this unit takes [Combustion] damage\nAt less than 50% HP, gain 1 more [ChickenFightlust]\n- Gain 5 On Kill
   PL: Na początku walki zyskuje 1 Wzrostu Poziomu Ataku i 1 Wzrostu Poziomu Obrony za każde 20% brakującego HP (maks. 3)\n\nZyskuje [ChickenFightlust] spełniając poniższe warunki (maks. 10 na turę)\n- Zyskuje 3 na początku starcia\n- Zyskuje 1 przy trafieniu podstawową Umiejętnością ataku albo przy otrzymaniu obrażeń [Combustion]\nPrzy HP poniżej 50% zyskuje dodatkowo 1 [ChickenFightlust]\n- Zyskuje 5 przy zabiciu wroga
598. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — podsumowanie] [ChickenFightlust] 얻음.
   źródło: Passives.json :: dataList[id=1071401].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ChickenFightlust]
   znaczenie tagów: [ChickenFightlust] = 혈투본능 / Battleblood Instinct
   EN: Gain [ChickenFightlust]
   PL: Zyskuje [ChickenFightlust].
599. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Wrath, posiadane 3× Glut.) — nazwa] 배수의 진
   źródło: Passives.json :: dataList[id=1071421].name
   limit: do 40 znaków
   EN: Backed Against a River
   PL: Z Plecami nad Rzeką
600. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Wrath, posiadane 3× Glut.) — opis] 턴 종료 시 체력 비율이 가장 낮은 아군 1명의 현재 체력이 최대 체력의 50% 미만이라면, 다음 턴에 [ParryingResultUp] 1 얻음
   źródło: Passives.json :: dataList[id=1071421].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [ParryingResultUp]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Turn End: if an ally with the lowest current HP percentage has less than 50% HP, that unit gains 1 [ParryingResultUp] next turn
   PL: Na koniec tury, jeżeli Sojusznik z najniższym procentem obecnego HP ma mniej niż 50% HP, zyskuje 1 [ParryingResultUp] w następnej turze

## [000] The Middle Big Brother — Heathcliff — 중지 작은 형님
- ID Tożsamości: `10715` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 7 · HP bazowe: 90 · szybkość: 3–5 / 3–5 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Bleed, Burn

601. [Karta Tożsamości — tytuł] 중지\n작은 형님
   źródło: Personalities.json :: dataList[id=10715].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Middle\nBig Brother
   PL: Środkowego\nStarszy Brat
602. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10715].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10715].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Karta Tożsamości — opis] 히스클리프의 열다섯번째 인격
   źródło: Personalities.json :: dataList[id=10715].desc
   limit: do 120 znaków
   EN: Heathcliff’s 15th Identity
   PL: Piętnasta Tożsamość Heathcliffa
605. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 발길질
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=1].name ; dataList[id=1071501].levelList[level=2].name ; dataList[id=1071501].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 2 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Kicking
   PL: Kopniak
606. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 이 슬롯 [Aggro] 3 증가
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Aggro]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [WhenUse] Gain +3 [Aggro] to this Slot next turn
   PL: [WhenUse] Zwiększa [Aggro] tego slotu o 3 w następnej turze
607. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">대상의 [Combustion]과 [Laceration]의 합이 6 이상이면 코인 위력 +1</style>\n[WhenUse] 다음 턴에 이 슬롯 [Aggro] 3 증가
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [Laceration], [WhenUse], [Aggro]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: <style="highlight">If target has 6+ ([Combustion] + [Laceration]), Coin Power +1</style>\n[WhenUse] Gain +3 [Aggro] to this Slot next turn
   PL: <style="highlight">Przy 6+ (suma [Combustion] i [Laceration] celu) Moc Monet +1</style>\n[WhenUse] Zwiększa [Aggro] tego slotu o 3 w następnej turze
612. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 흐트러짐 5 회복</style>
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] Lower user's Stagger Threshold by 5</style>
   PL: <style="highlight">[OnSucceedAttack] Obniża Próg Oszołomienia o 5</style>
613. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1071501].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]<style="highlight"></style>
615. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1071501].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1071501].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Combustion]<style="highlight"></style>
617. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Combustion]과 [Laceration]의 합이 6 이상이면 코인 위력 +1\n<style="highlight">[WhenUse] 대상이 [RetaliationBook]이면, 최종 위력 +1</style>\n[WhenUse] 다음 턴에 이 슬롯 [Aggro] 3 증가
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=4].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [Laceration], [WhenUse], [RetaliationBook], [Aggro]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [WhenUse] = [사용시] / [On Use]; [RetaliationBook] = 앙갚음 대상 / Vengeance Mark; [Aggro] = 도발치 / Aggro
   EN: If target has 6+ ([Combustion] + [Laceration]), Coin Power +1\n<style="highlight">[WhenUse] If target has [RetaliationBook], Final Power +1</style>\n[WhenUse] Gain +3 [Aggro] to this Slot next turn
   PL: Przy 6+ (suma [Combustion] i [Laceration] celu) Moc Monet +1\n<style="highlight">[WhenUse] Jeżeli cel ma [RetaliationBook], Moc Końcowa +1</style>\n[WhenUse] Zwiększa [Aggro] tego slotu o 3 w następnej turze
618. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 흐트러짐 5 회복<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 5<style="highlight"></style>
   PL: [OnSucceedAttack] Obniża Próg Oszołomienia o 5<style="highlight"></style>
619. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">- [RetaliationBook]이면 정신력 3 회복</style>
   źródło: Skills_personality-07.json :: dataList[id=1071501].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [RetaliationBook]
   znaczenie tagów: [RetaliationBook] = 앙갚음 대상 / Vengeance Mark
   EN: <style="highlight">- If target has [RetaliationBook], heal 3 SP</style>
   PL: <style="highlight">- Jeżeli cel ma [RetaliationBook], odzyskuje 3 Poczytalności</style>
620. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 뒤통수 조심!
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=1].name ; dataList[id=1071502].levelList[level=2].name ; dataList[id=1071502].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Watch Your Back!
   PL: Uważaj na Kark!
621. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [StartBattle] 조작 패널의 양 옆의 아군에게 [AttackUp] 2 부여\n[StartBattle] (가장 높은 공명 수 / 2)만큼 이 스킬의 공격 레벨이 증가 (최대 3, 소수점 버림)\n[WhenUse] 다음 턴에 이 슬롯 [Aggro] 5 증가
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [AttackUp], [WhenUse], [Aggro]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: [StartBattle] Apply 2 [AttackUp] on allies adjacent to this unit on the Dashboard\n[StartBattle] This Skill gains (highest Reson. / 2) Offense Level (max 3, rounded down)\n[WhenUse] Gain +5 [Aggro] to this Slot next turn
   PL: [StartBattle] Nakłada 2 [AttackUp] na sojuszników przylegających do tej jednostki na panelu\n[StartBattle] Umiejętność ta zyskuje Wzrost Poziomu Ataku równy (najwyższy Rezonans / 2) (maks. 3, zaokrąglone w dół)\n[WhenUse] Zwiększa [Aggro] tego slotu o 5 w następnej turze
622. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 3
623. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Combustion] o 1
624. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis]
   PL: [OnSucceedAttack] Nakłada 2 [Paralysis]
626. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]
   PL: [OnSucceedAttack] Nakłada 3 [Combustion]
627. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">대상의 [Combustion]과 [Laceration]의 합이 6 이상이면 코인 위력 +1</style>\n[StartBattle] 조작 패널의 양 옆의 아군에게 [AttackUp] 2 부여\n[StartBattle] (가장 높은 공명 수 / 2)만큼 이 스킬의 공격 레벨이 증가 (최대 3, 소수점 버림)\n[WhenUse] 다음 턴에 이 슬롯 [Aggro] 5 증가
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=2].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [Laceration], [StartBattle], [AttackUp], [WhenUse], [Aggro]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [WhenUse] = [사용시] / [On Use]; [Aggro] = 도발치 / Aggro
   EN: <style="highlight">If target has 6+ ([Combustion] + [Laceration]), Coin Power +1</style>\n[StartBattle] Apply 2 [AttackUp] on allies adjacent to this unit on the Dashboard\n[StartBattle] This Skill gains (highest Reson. / 2) Offense Level (max 3, rounded down)\n[WhenUse] Gain +5 [Aggro] to this Slot next turn
   PL: <style="highlight">Przy 6+ (suma [Combustion] i [Laceration] celu) Moc Monet +1</style>\n[StartBattle] Nakłada 2 [AttackUp] na sojuszników przylegających do tej jednostki na panelu\n[StartBattle] Umiejętność ta zyskuje Wzrost Poziomu Ataku równy (najwyższy Rezonans / 2) (maks. 3, zaokrąglone w dół)\n[WhenUse] Zwiększa [Aggro] tego slotu o 5 w następnej turze
628. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1071502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 3<style="highlight"></style>
629. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1071502].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Combustion] o 1<style="highlight"></style>
630. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1071502].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Paralysis]<style="highlight"></style>
632. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1071502].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Combustion]<style="highlight"></style>
633. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Combustion]과 [Laceration]의 합이 6 이상이면 코인 위력 +1\n[StartBattle] 조작 패널의 양 옆의 아군에게 [AttackUp] 2 부여\n[StartBattle] (가장 높은 공명 수 / 2)만큼 이 스킬의 공격 레벨이 증가 (최대 3, 소수점 버림)\n<style="highlight">[WhenUse] 대상이 [RetaliationBook]이면, 최종 위력 +2</style>\n[WhenUse] 다음 턴에 이 슬롯 [Aggro] 5 증가
   źródło: Skills_personality-07.json :: dataList[id=1071502].levelList[level=4].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [Laceration], [StartBattle], [AttackUp], [WhenUse], [RetaliationBook], [Aggro]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [WhenUse] = [사용시] / [On Use]; [RetaliationBook] = 앙갚음 대상 / Vengeance Mark; [Aggro] = 도발치 / Aggro
   EN: If target has 6+ ([Combustion] + [Laceration]), Coin Power +1\n[StartBattle] Apply 2 [AttackUp] on allies adjacent to this unit on the Dashboard\n[StartBattle] This Skill gains (highest Reson. / 2) Offense Level (max 3, rounded down)\n<style="highlight">[WhenUse] If target has [RetaliationBook], Final Power +2</style>\n[WhenUse] Gain +5 [Aggro] to this Slot next turn
   PL: Przy 6+ (suma [Combustion] i [Laceration] celu) Moc Monet +1\n[StartBattle] Nakłada 2 [AttackUp] na sojuszników przylegających do tej jednostki na panelu\n[StartBattle] Umiejętność ta zyskuje Wzrost Poziomu Ataku równy (najwyższy Rezonans / 2) (maks. 3, zaokrąglone w dół)\n<style="highlight">[WhenUse] Jeżeli cel ma [RetaliationBook], Moc Końcowa +2</style>\n[WhenUse] Zwiększa [Aggro] tego slotu o 5 w następnej turze
634. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 내 헤어쿠포오오오온!!!!
   źródło: Skills_personality-07.json :: dataList[id=1071503].levelList[level=3].name ; dataList[id=1071503].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 10 · monety: 1 (+12)
   limit: do 50 znaków
   EN: MY HAIR COUPOOOOOOOOOOONS!!!!
   PL: MOJE KUPONY NA FRYZUROOOOOOO!!!!
635. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 메인 타겟의 [Combustion]과 [Laceration]의 합 4당 최종 위력 +1 (최대 3)\n[StartBattle] (가장 높은 공명 수)만큼 이 스킬의 공격 레벨이 증가 (최대 6)\n[WhenUse] 질투 완전 공명 6 이상이면, 가중치 +1\n[WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당 피해량 +30% (집중 전투의 경우, 부위로 판정)
   źródło: Skills_personality-07.json :: dataList[id=1071503].levelList[level=3].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [StartBattle], [WhenUse]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]
   EN: Final Power +1 for every 4 ([Combustion] + [Laceration]) on the main target (max 3)\n[StartBattle] This Skill gains (highest Reson.) Offense Level (max 6)\n[WhenUse] At 6+ Envy A-Reson., gain +1 Atk Weight\n[WhenUse] Deal +30% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Part)
   PL: Moc Końcowa +1 za każde 4 (suma [Combustion] i [Laceration] głównego celu) (maks. 3)\n[StartBattle] Umiejętność ta zyskuje Wzrost Poziomu Ataku równy najwyższemu Rezonansowi (maks. 6)\n[WhenUse] Przy 6+ Pełnym Rezonansie Zazdrości Waga ataku +1\n[WhenUse] Zadaje +30% obrażeń za każdego nadmiarowego celu ataku poza Wagą ataku tej Umiejętności (w walkach skupionych sądzi się w Partach)
636. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-07.json :: dataList[id=1071503].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_personality-07.json :: dataList[id=1071503].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL: [OnSucceedAttack] Nakłada 5 [Laceration]
638. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 5 부여
   źródło: Skills_personality-07.json :: dataList[id=1071503].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion]
   PL: [OnSucceedAttack] Nakłada 5 [Combustion]
639. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 메인 타겟의 [Combustion]과 [Laceration]의 합 4당 최종 위력 +1 (최대 3)\n질투 공명 2당 최종 위력 +1 (최대 3)\n[StartBattle] (가장 높은 공명 수)만큼 이 스킬의 공격 레벨이 증가 (최대 6)\n<style="highlight">[WhenUse] 메인 타겟이 [RetaliationBook]이면, 최종 위력 +2</style>\n[WhenUse] 질투 완전 공명 6 이상이면, 가중치 +1\n<style="highlight">[WhenUse] 자신의 [VengeanceBookHeathcliff]가 20 이상이면, 가중치 +1</style>\n[WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당 피해량 +<style="highlight">60</style>% (집중 전투의 경우, 부위로 판정)\n<style="highlight">[EnemyKill] 이 스킬로 처치한 적 1명당 원한 문신 2 얻음 (턴당 최대 6)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071503].levelList[level=4].desc
   limit: do 750 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion], [Laceration], [StartBattle], [WhenUse], [RetaliationBook], [VengeanceBookHeathcliff], [EnemyKill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [RetaliationBook] = 앙갚음 대상 / Vengeance Mark; [VengeanceBookHeathcliff] = 앙갚음 장부 [히스클리프] / Book of Vengeance [Heathcliff]; [EnemyKill] = [적 처치 시] / [On Kill]
   EN: Final Power +1 for every 4 ([Combustion] + [Laceration]) on the main target (max 3)\nFinal Power +1 for every 2 Envy Reson. (max 3)\n[StartBattle] This Skill gains (highest Reson.) Offense Level (max 6)\n<style="highlight">[WhenUse] If the main target has [RetaliationBook], Final Power +2</style>\n[WhenUse] At 6+ Envy A-Reson., gain +1 Atk Weight\n<style="highlight">[WhenUse] At 20+ [VengeanceBookHeathcliff], gain +1 Atk Weight</style>\n[WhenUse] Deal +<style="highlight">60</style>% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Part)\n<style="highlight">[EnemyKill] For every enemy killed using this Skill, gain 2 Vengeance Tattoo (max 6 per turn)</style>
   PL: Moc Końcowa +1 za każde 4 (suma [Combustion] i [Laceration] głównego celu) (maks. 3)\nMoc Końcowa +1 za każde 2 Rezonansu Zazdrości (maks. 3)\n[StartBattle] Umiejętność ta zyskuje Wzrost Poziomu Ataku równy najwyższemu Rezonansowi (maks. 6)\n<style="highlight">[WhenUse] Jeżeli główny cel ma [RetaliationBook], Moc Końcowa +2</style>\n[WhenUse] Przy 6+ Pełnym Rezonansie Zazdrości Waga ataku +1\n<style="highlight">[WhenUse] Przy 20+ [VengeanceBookHeathcliff] Waga ataku +1</style>\n[WhenUse] Zadaje +<style="highlight">60</style>% obrażeń za każdego nadmiarowego celu ataku poza Wagą ataku tej Umiejętności (w walkach skupionych sądzi się w Partach)\n<style="highlight">[EnemyKill] Za każdego wroga zabitego tą Umiejętnością zyskuje 2 Tatuaże Zemsty (maks. 6 na turę)</style>
640. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 5 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071503].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 5 [Laceration]<style="highlight"></style>
642. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 5 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071503].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 5 [Combustion]<style="highlight"></style>
643. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] <style="highlight">[OnSucceedAttack] 이 코인 최종 피해량의 (질투 공명 수 x 5)%만큼 타격 피해 (최대 30%)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071503].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] Deal (Envy Reson. x 5)% of this Coin's final damage as Blunt bonus damage (max 30%)</style>
   PL: <style="highlight">[OnSucceedAttack] Zadaje obrażenia Uderzenia równe (Rezonans Zazdrości x 5)% końcowych obrażeń tej monety (maks. 30%)</style>
644. [Umiejętność 4 (×0) (ulepszenie 4) — nazwa] 전원, 처형이다!!
   źródło: Skills_personality-07.json :: dataList[id=1071505].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 16 · monety: 1 (+10)
   limit: do 50 znaków
   EN: COMPLETE AND TOTAL EXTERMINATION!!
   PL: WSZYSCY, EGZEKUCJA!!
645. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 이 스킬은 외부 효과로 재사용할 수 없음\n자신의 잃은 체력 1%당 피해량 1% 증가 (최대 30%)\n메인 타겟의 [Combustion]과 [Laceration]의 합 4당 최종 위력 +1 (최대 5)\n[StartBattle] (가장 높은 공명 수)만큼 이 스킬의 공격 레벨이 증가 (최대 6)\n[WhenUse] 메인 타겟이 [RetaliationBook]이면, 최종 위력 +3\n[WhenUse] 자신의 [VengeanceBookHeathcliff]가 20 이상이면, 가중치 +1\n[WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당 피해량 +60% (집중 전투의 경우, 부위로 판정)\n[EnemyKill] 이 스킬로 처치한 적 수만큼 가장 적게 보유한 무작위 속성 E.G.O 자원 얻음 (최대 4)\n[EndSkill] 자신의 [MiddleFingerTattooID] 15 소모
   źródło: Skills_personality-07.json :: dataList[id=1071505].levelList[level=4].desc
   limit: do 870 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [StartBattle], [WhenUse], [RetaliationBook], [VengeanceBookHeathcliff], [EnemyKill], [EndSkill], [MiddleFingerTattooID]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [RetaliationBook] = 앙갚음 대상 / Vengeance Mark; [VengeanceBookHeathcliff] = 앙갚음 장부 [히스클리프] / Book of Vengeance [Heathcliff]; [EnemyKill] = [적 처치 시] / [On Kill]; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: External effects cannot trigger this Skill to be Reused\nDeal +1% damage for every 1% missing HP on self (max 30%)\nFinal Power +1 for every 4 ([Combustion] + [Laceration]) on the main target (max 5)\n[StartBattle] This Skill gains (highest Reson.) Offense Level (max 6)\n[WhenUse] If the main target has [RetaliationBook], Final Power +3\n[WhenUse] At 20+ [VengeanceBookHeathcliff], gain +1 Atk Weight\n[WhenUse] Deal +60% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Part)\n[EnemyKill] For every enemy killed using this Skill, gain an E.G.O resource of a random least-owned Affinity (max 4)\n[EndSkill] Consume 15 [MiddleFingerTattooID] on self
   PL: Ta Umiejętność nie może być ponownie użyta przez zewnętrzne efekty\nZadaje +1% obrażeń za każde 1% brakującego HP (maks. 30%)\nMoc Końcowa +1 za każde 4 (suma [Combustion] i [Laceration] głównego celu) (maks. 5)\n[StartBattle] Umiejętność ta zyskuje Wzrost Poziomu Ataku równy najwyższemu Rezonansowi (maks. 6)\n[WhenUse] Jeżeli główny cel ma [RetaliationBook], Moc Końcowa +3\n[WhenUse] Przy 20+ [VengeanceBookHeathcliff] Waga ataku +1\n[WhenUse] Zadaje +60% obrażeń za każdego nadmiarowego celu ataku poza Wagą ataku tej Umiejętności (w walkach skupionych sądzi się w Partach)\n[EnemyKill] Za każdego wroga zabitego tą Umiejętnością zyskuje 1 zasób E.G.O losowo wybranego z najmniej posiadanych Atrybutów (maks. 4)\n[EndSkill] Zużywa 15 [MiddleFingerTattooID]
646. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-07.json :: dataList[id=1071505].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] 대상이 흐트러짐 상태면, 피해량 +20%
   źródło: Skills_personality-07.json :: dataList[id=1071505].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: If target is Staggered, deal +20% damage
   PL: Jeżeli cel jest Ogłuszony, zadaje +20% obrażeń
648. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_personality-07.json :: dataList[id=1071505].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 637 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Combustion] 5 부여
   źródło: Skills_personality-07.json :: dataList[id=1071505].levelList[level=4].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 638 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_personality-07.json :: dataList[id=1071505].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]
   PL: [OnSucceedAttack] Nakłada 5 [Vibration]
651. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 6 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_personality-07.json :: dataList[id=1071505].levelList[level=4].coinlist[#0].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
652. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 7 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 (질투 공명 수 x 7)%만큼 타격 피해 (최대 42%)
   źródło: Skills_personality-07.json :: dataList[id=1071505].levelList[level=4].coinlist[#0].coindescs[#6].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal (Envy Reson. x 7)% of this Coin's final damage as Blunt bonus damage (max 42%)
   PL: [OnSucceedAttack] Zadaje obrażenia Uderzenia równe (Rezonans Zazdrości x 7)% końcowych obrażeń tej monety (maks. 42%)
653. [Obrona (ulepszenia 1,4) — nazwa] 되갚기
   źródło: Skills_personality-07.json :: dataList[id=1071504].levelList[level=1].name ; dataList[id=1071504].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [Obrona (ulepszenie 1) — opis] [StartBattle] 잃은 체력의 25%만큼 보호막을 얻음 (턴당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 25% of missing HP as Shield (once per turn)
   PL: [StartBattle] Zyskuje Tarczę równą 25% brakującego HP (1 raz na turę)
655. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [Obrona (ulepszenie 4) — opis] <style="highlight">[StartBattle] 질투 완전 공명 수의 합이 6 이상이면, 반격 시 ‘내 헤어쿠포오오오온!!!!’ 스킬을 사용함. (조작 패널의 왼쪽 슬롯 스킬부터 발동, 턴당 최대 2회 발동)\n[StartBattle] 자신을 포함한 정신력이 가장 낮은 중지 소속 아군 3명의 정신력 (질투 공명 수 + 3)만큼 회복 (턴당 1회, 최대 10. 정신력이 -40 이하인 아군 제외)</style>\n[StartBattle] 잃은 체력의 25%만큼 보호막을 얻음 (턴당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071504].levelList[level=4].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: <style="highlight">[StartBattle] At 6+ sum of Envy A-Reson., use "MY HAIR COUPOOOOOOOOOOONS!!!!" Skill as Counter (Activates from the leftmost Skill Slot. Activates 2 times per turn)\n[StartBattle] Heal (Envy Reson. + 3) SP for 3 of The Middle-faction allies that have the lowest SP (including this unit; once per turn, max 10 SP; excluding allies at -40 or lower SP)</style>\n[StartBattle] Gain 25% of missing HP as Shield (once per turn)
   PL: <style="highlight">[StartBattle] Przy 6+ sumie Pełnych Rezonansów Zazdrości odpowiada Kontrą Umiejętnością „MOJE KUPONY NA FRYZUROOOOOOO!!!!” (uruchamia od Umiejętności lewego slotu na panelu; maks. 2 razy na turę)\n[StartBattle] Odzyskuje (Rezonans Zazdrości + 3) Poczytalności dla 3 Tożsamości frakcji Środkowego z najniższą Poczytalnością (łącznie z tą jednostką; 1 raz na turę, maks. 10 Poczytalności; wyłączając sojuszników z Poczytalnością -40 lub niższą)</style>\n[StartBattle] Zyskuje Tarczę równą 25% brakującego HP (1 raz na turę)
658. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071504].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071504].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Pasywka bojowa (od ulepszenia 1) — nazwa] 앙갚음 장부
   źródło: Passives.json :: dataList[id=1071502].name
   limit: do 40 znaków
   EN: The Book of Vengeance
   PL: Księga Zemsty
661. [Pasywka bojowa (od ulepszenia 1) — opis] 자신 또는 중지 소속의 아군 인격이 적에게 피격 시, 대상에게 [VendettaMark]을 1 부여하고 [VengeanceBookHeathcliff] 1 얻음 (스킬당 1회)\n아군 인격 사망시, [VengeanceBookHeathcliff] 3 얻음
   źródło: Passives.json :: dataList[id=1071502].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [VendettaMark], [VengeanceBookHeathcliff]
   znaczenie tagów: [VendettaMark] = 복수 대상 / Vendetta Mark; [VengeanceBookHeathcliff] = 앙갚음 장부 [히스클리프] / Book of Vengeance [Heathcliff]
   EN: When this unit or any of The Middle-faction allies are hit by an enemy, inflict 1 [VendettaMark] on the said enemy and gain 1 [VengeanceBookHeathcliff] (once per Skill)\nAlly Death: Gain 3 [VengeanceBookHeathcliff]
   PL: Gdy ta jednostka albo sojusznik frakcji Środkowego zostaje trafiony przez wroga, nakłada 1 [VendettaMark] na tego wroga i zyskuje 1 [VengeanceBookHeathcliff] (1 raz na Umiejętność)\nGdy Tożsamość sojusznika ginie, zyskuje 3 [VengeanceBookHeathcliff]
662. [Pasywka bojowa (od ulepszenia 1) — nazwa] 원한 문신 공명
   źródło: Passives.json :: dataList[id=1071503].name
   limit: do 40 znaków
   EN: Vengeance Tattoo Resonance
   PL: Rezonans Tatuażu Zemsty
663. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 시작시 수비 스킬을 장착한 중지 소속 아군 인격이 이번 턴 동안 일방공격으로 받는 피해량 -20%\n\n전투 시작시 질투 공명 4 이상이면, 조작 패널에서 자신의 양 옆의 중지 소속 아군 인격이 사용할 수 있는 반격 스킬이 있는 동안 피해로 인해 흐트러짐 상태가 되지 않음 (강제 흐트러짐 제외)\n- 질투 공명 6 이상이면, 모든 중지 소속 아군 인격에게 적용됨
   źródło: Passives.json :: dataList[id=1071503].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Combat Start: The Middle-faction allies that have equipped Defense Skills take -20% damage from Unopposed Attacks for this turn\n\nCombat Start: At 4+ Envy Reson., The Middle-faction allies adjacent to this unit on the Dashboard cannot be Staggered by damage as long as they have usable Counter Skills equipped in their Slots (excluding Forced Staggers)\n- At 6+ Envy Reson., this effect applies to all of The Middle-faction allies
   PL: Na początku walki Tożsamości frakcji Środkowego z wyposażoną Umiejętnością obrony otrzymują -20% obrażeń z ataków nieopartych w tej turze\n\nNa początku walki przy 4+ Rezonansie Zazdrości Tożsamości frakcji Środkowego przylegające do tej jednostki na panelu nie mogą zostać Ogłuszone obrażeniami, dopóki mają wyposażoną możliwą do użycia Umiejętność Kontry (z wyłączeniem wymuszonego Ogłuszenia)\n- Przy 6+ Rezonansie Zazdrości ten efekt dotyczy wszystkich Tożsamości frakcji Środkowego
664. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Envy) — nazwa] 작은 형님
   źródło: Passives.json :: dataList[id=1071501].name
   limit: do 40 znaków
   EN: The Big Brother
   PL: Starszy Brat
665. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Envy) — opis] 전투 시작시, 질투 공명당 [MiddleFingerTattooID] 1 얻음 (최대 7)\n\n적이 자신을 포함한 중지 소속 아군 인격을 공격했으면, 해당 스킬 공격 종료 시 공격자를 ‘발길질’로 일방 공격함 (턴당 1회)
   źródło: Passives.json :: dataList[id=1071501].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [MiddleFingerTattooID]
   znaczenie tagów: [MiddleFingerTattooID] = 원한 문신 / Vengeance Tattoo
   EN: Combat Start: Gain 1 [MiddleFingerTattooID] for every Envy Reson. (max 7)\n\nIf an enemy attacked any of The Middle-faction allies including this unit, use "Kicking" on the said enemy as an Unopposed Attack at Attack End of the said enemy's Skill (once per turn)
   PL: Na początku walki zyskuje 1 [MiddleFingerTattooID] za każdy Rezonans Zazdrości (maks. 7)\n\nJeżeli wróg zaatakował Tożsamość frakcji Środkowego (łącznie z tą jednostką), na koniec ataku tej Umiejętności atakuje nieoparciego agresora „Kopniakiem” (1 raz na turę)
666. [Pasywka bojowa (od ulepszenia 4) — nazwa] 앙갚음 장부
   źródło: Passives.json :: dataList[id=1071512].name
   (powtórzenie elementu 660 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Pasywka bojowa (od ulepszenia 4) — opis] 자신 또는 중지 소속의 아군 인격이 적에게 피격 시, 대상에게 [VendettaMark]을 1 부여하고 [VengeanceBookHeathcliff] 1 얻음 (스킬당 1회)\n아군 인격 사망시, [VengeanceBookHeathcliff] 3 얻음\n\n<style="highlight">턴 시작시 자신의 [MiddleFingerTattooID]이 15 이상이면 아래 효과 적용\n- 기본 스킬 하나를 ‘전원, 처형이다!!’로 변경 (가장 왼쪽 슬롯의 아래 스킬 우선 적용)\n· 변경된 스킬이 다른 스킬로 변경되어 사용할 수 없게 되면, 위 효과를 다시 발동함\n- 이번 턴이 종료될 때까지 전투 BGM을 변경 (일부 전투 제외)\n\n대기 해제 또는 복귀로 등장한 턴의 전투 시작시, ‘내 헤어쿠포오오오온!!!!'을 무작위 대상에게 사용함\n- 해당 공격 종료 시 모든 아군 중지 인격에게 [AttackUp] 1, [DefenseUp] 1 부여</style>
   źródło: Passives.json :: dataList[id=1071512].desc
   limit: do 1070 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [VendettaMark], [VengeanceBookHeathcliff], [MiddleFingerTattooID], [AttackUp], [DefenseUp]
   znaczenie tagów: [VendettaMark] = 복수 대상 / Vendetta Mark; [VengeanceBookHeathcliff] = 앙갚음 장부 [히스클리프] / Book of Vengeance [Heathcliff]; [MiddleFingerTattooID] = 원한 문신 / Vengeance Tattoo; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: When this unit or any of The Middle-faction allies are hit by an enemy, inflict 1 [VendettaMark] on the said enemy and gain 1 [VengeanceBookHeathcliff] (once per Skill)\nAlly Death: Gain 3 [VengeanceBookHeathcliff]\n\n<style="highlight">Turn Start: At 15+ [MiddleFingerTattooID], apply the following effects:\n- Replace a Base Skill with "COMPLETE AND TOTAL EXTERMINATION!!" (prioritizes the Skill on the leftmost Slot's bottom row on the Dashboard)\n· If the replaced Skill becomes inaccessible due to being replaced by a different Skill, activate the above effect again\n- Change battle music until Turn End (excluding certain Encounters)\n\nCombat Start in the Turn this unit Substituted in or Returned to the field: Use "MY HAIR COUPOOOOOOOOOOONS!!!!" on a random target\n- Attack End of the said Skill: Apply 1 [AttackUp] and 1 [DefenseUp] on all The Middle-faction allies</style>
   PL: Gdy ta jednostka albo sojusznik frakcji Środkowego zostaje trafiony przez wroga, nakłada 1 [VendettaMark] na tego wroga i zyskuje 1 [VengeanceBookHeathcliff] (1 raz na Umiejętność)\nGdy Tożsamość sojusznika ginie, zyskuje 3 [VengeanceBookHeathcliff]\n\n<style="highlight">Na początku tury przy 15+ [MiddleFingerTattooID] stosuje poniższe efekty:\n- Zamienia jedną podstawową Umiejętność na „WSZYSCY, EGZEKUCJA!!” (najpierw Umiejętność lewego dolnego pola slotu po lewej stronie panelu)\n· Jeżeli zamieniona Umiejętność stanie się niedostępna, bo została zamieniona na inną, ponownie uruchamia powyższy efekt\n- Zmienia muzykę walki do końca tury (z wyłączeniem niektórych spotkań)\n\nNa początku walki w turze Wejścia z rezerwy albo Powrotu używa „MOJE KUPONY NA FRYZUROOOOOOO!!!!” na losowym celu\n- Na koniec ataku tej Umiejętności nakłada 1 [AttackUp] i 1 [DefenseUp] na wszystkich sojuszników frakcji Środkowego</style>
668. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Envy) — nazwa] 의리 사슬
   źródło: Passives.json :: dataList[id=1071521].name
   limit: do 40 znaków
   EN: Chains of Loyalty
   PL: Łańcuch Wierności
669. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Envy) — opis] 전투 중 중지 소속 아군 인격이 사망하면 해당 턴과 다음 턴에 모든 중지 소속 아군 인격이 [Enhancement] 1 얻음 (턴당 1회)
   źródło: Passives.json :: dataList[id=1071521].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: If any of The Middle-faction allies are killed during combat this turn, all The Middle-faction allies gain 1 [Enhancement] this turn and next turn (once per turn)
   PL: Gdy Tożsamość sojusznika frakcji Środkowego ginie podczas walki, wszystkie Tożsamości frakcji Środkowego zyskują 1 [Enhancement] w tej turze i następnej (1 raz na turę)

## [000] The House of Spiders: The Thumb Apprentice — Heathcliff — 거미집 엄지 제자
- ID Tożsamości: `10716` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 7 · HP bazowe: 83 · szybkość: 3–5 / 3–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Tremor, Burn

670. [Karta Tożsamości — tytuł] 거미집\n엄지 제자
   źródło: Personalities.json :: dataList[id=10716].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The House of Spiders:\nThe Thumb Apprentice
   PL: Dom Pajęczyn:\nUczeń Kciuka
671. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10716].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10716].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Karta Tożsamości — opis] 히스클리프의 열여섯번째 인격
   źródło: Personalities.json :: dataList[id=10716].desc
   limit: do 120 znaków
   EN: Heathcliff’s 16th Identity
   PL: Szesnasta Tożsamość Heathcliffa
674. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 팔레르모 스파다
   źródło: Skills_personality-07.json :: dataList[id=1071601].levelList[level=1].name ; dataList[id=1071601].levelList[level=2].name ; dataList[id=1071601].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: La Spada di Palermo
   PL: La Spada di Palermo
675. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Combustion]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-07.json :: dataList[id=1071601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Combustion], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[WhenUse] If target has 6+ ([Combustion] + [Vibration]), Coin Power +1</style>
   PL: <style="highlight">[WhenUse] Przy 6+ (suma [Combustion] i [Vibration] celu) Moc Monet +1</style>
678. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071601].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]<style="highlight"></style>
680. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Combustion], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: [WhenUse] <style="highlight">Coin Power +1 for every 6 ([Combustion] + [Vibration]) on target (max 2)</style>
   PL: [WhenUse] <style="highlight">Moc Monet +1 za każde 6 (suma [Combustion] i [Vibration] celu) (maks. 2)</style>
681. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_personality-07.json :: dataList[id=1071601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Combustion]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Combustion]
682. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 콜피 소타니
   źródło: Skills_personality-07.json :: dataList[id=1071602].levelList[level=1].name ; dataList[id=1071602].levelList[level=2].name ; dataList[id=1071602].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Colpi Sottani
   PL: Colpi Sottani
683. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 623 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]
685. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Combustion]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-07.json :: dataList[id=1071602].levelList[level=2].desc
   (powtórzenie elementu 677 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-07.json :: dataList[id=1071602].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Combustion] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Combustion] o <style="highlight">2</style>
687. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-07.json :: dataList[id=1071602].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +<style="highlight">2</style> Licznika [Vibration]
688. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [EvolvingManual]이 있거나 대상에게 [DuelEdgeAlly]가 있으면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_personality-07.json :: dataList[id=1071602].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [EvolvingManual], [DuelEdgeAlly], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook; [DuelEdgeAlly] = 결투 고조 / The Duel Escalates; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] If this unit has [EvolvingManual], or if target has [DuelEdgeAlly], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli ma [EvolvingManual] albo cel ma [DuelEdgeAlly], wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1</style>
689. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)\n[WinDuel] 대상에게 [DuelEdgeAlly]가 있으면, 진동 횟수 1 증가</style>
   źródło: Skills_personality-07.json :: dataList[id=1071602].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Combustion], [Vibration], [WinDuel], [DuelEdgeAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [DuelEdgeAlly] = 결투 고조 / The Duel Escalates
   EN: [WhenUse] <style="highlight">Coin Power +1 for every 6 ([Combustion] + [Vibration]) on target (max 2)\n[WinDuel] If target has [DuelEdgeAlly], inflict +1 [Vibration] Count</style>
   PL: [WhenUse] <style="highlight">Moc Monet +1 za każde 6 (suma [Combustion] i [Vibration] celu) (maks. 2)\n[WinDuel] Jeżeli cel ma [DuelEdgeAlly], zwiększa Licznik [Vibration] celu o 1</style>
690. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] <style="highlight">[Combustion] 2 부여</style>, [Combustion] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">2 [Combustion] and</style> +2 [Combustion] Count
   PL: [OnSucceedAttack] Nakłada <style="highlight">2 [Combustion] i</style> zwiększa Licznik [Combustion] o 2
691. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] <style="highlight">[Vibration] 2 부여</style>, [Vibration] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">2 [Vibration] and</style> +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada <style="highlight">2 [Vibration] i</style> zwiększa Licznik [Vibration] o 2
692. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [EvolvingManual]이 있거나 대상에게 [DuelEdgeAlly]가 있으면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071602].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [EvolvingManual], [DuelEdgeAlly], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook; [DuelEdgeAlly] = 결투 고조 / The Duel Escalates; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this unit has [EvolvingManual], or if target has [DuelEdgeAlly], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli ma [EvolvingManual] albo cel ma [DuelEdgeAlly], wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1<style="highlight"></style>
693. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 카치아토레
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=3].name ; dataList[id=1071603].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Il Cacciatore
   PL: Il Cacciatore
694. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [BeforeUse] 대상의 [DuelEdgeAlly]가 5면, ‘세치오나투라 디 체르보’로 발동됨 (턴당 1회)\n[WhenUse] 대상의 [Combustion]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [DuelEdgeAlly] 수치에 따라 다음 효과 전부 얻음\n- 1 : [Vibration] 위력 부여값 +1\n- 2 : [Vibration] 횟수 부여값 +1\n- 3 : [Combustion] 위력 부여값 +1\n- 4 : [Combustion] 횟수 부여값 +1\n[WhenUse] [EvolvingManual]이 있거나 대상의 [DuelEdgeAlly]가 3 이상이면, 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=3].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [DuelEdgeAlly], [WhenUse], [Combustion], [Vibration], [EvolvingManual], [SuperCoin]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [DuelEdgeAlly] = 결투 고조 / The Duel Escalates; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [BeforeUse] If target has 5 [DuelEdgeAlly], activate "Sezionatura di Cervo" instead (once per turn)\n[WhenUse] If target has 6+ ([Combustion] + [Vibration]), Coin Power +1\n[WhenUse] Gain the following effects based on [DuelEdgeAlly] Stack on target:\n- 1+ [DuelEdgeAlly]: Inflict +1 more [Vibration] Potency\n- 2+ [DuelEdgeAlly]: Inflict +1 more [Vibration] Count\n- 3+ [DuelEdgeAlly]: Inflict +1 more [Combustion] Potency\n- 4+ [DuelEdgeAlly]: Inflict +1 more [Combustion] Count\n[WhenUse] If this unit has [EvolvingManual], or if target has 3+ [DuelEdgeAlly], convert all Coins on this Skill to [SuperCoin]s
   PL: [BeforeUse] Jeżeli cel ma 5 [DuelEdgeAlly], stosuje się jako „Sezionatura di Cervo” (1 raz na turę)\n[WhenUse] Przy 6+ (suma [Combustion] i [Vibration] celu) Moc Monet +1\n[WhenUse] Zyskuje poniższe efekty w zależności od stosów [DuelEdgeAlly] celu:\n- 1+: nakłada o 1 więcej Mocy [Vibration]\n- 2+: nakłada o 1 więcej Licznika [Vibration]\n- 3+: nakłada o 1 więcej Mocy [Combustion]\n- 4+: nakłada o 1 więcej Licznika [Combustion]\n[WhenUse] Jeżeli ma [EvolvingManual] albo cel ma 3+ [DuelEdgeAlly], wszystkie monety tej Umiejętności stają się [SuperCoin]ami
695. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여, [Combustion] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion] and +2 [Combustion] Count
   PL: [OnSucceedAttack] Nakłada 2 [Combustion] i zwiększa Licznik [Combustion] o 2
696. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada 2 [Vibration] i zwiększa Licznik [Vibration] o 2
697. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [EvolvingManual] 1당, 피해량 +10% (최대 30%)
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EvolvingManual]
   znaczenie tagów: [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook
   EN: Deal +10% damage for every [EvolvingManual] on self (max 30%)
   PL: Zadaje +10% obrażeń za każde 1 [EvolvingManual] (maks. 30%)
698. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]
   PL: [OnSucceedAttack] Wywołuje [Switch_Vibration] do [VibrationIgnition]
699. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
700. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [EvolvingManual]이 있거나 대상의 [DuelEdgeAlly]가 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [EvolvingManual], [DuelEdgeAlly], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook; [DuelEdgeAlly] = 결투 고조 / The Duel Escalates; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this unit has [EvolvingManual], or if target has 3+ [DuelEdgeAlly], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Jeżeli ma [EvolvingManual] albo cel ma 3+ [DuelEdgeAlly], wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
701. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [BeforeUse] 대상의 [DuelEdgeAlly]가 5면, ‘세치오나투라 디 체르보’로 발동됨 (턴당 1회)\n[WhenUse] 대상의 [Combustion]과 [Vibration]의 합 <style="highlight">6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 대상의 [DuelEdgeAlly] 수치에 따라 다음 효과 전부 얻음\n<style="highlight">- 수치 1당 피해량 +6% (최대 30%)</style>\n- 1 : [Vibration] 위력 부여값 +1\n- 2 : [Vibration] 횟수 부여값 +1\n- 3 : [Combustion] 위력 부여값 +1\n- 4 : [Combustion] 횟수 부여값 +1\n[WhenUse] [EvolvingManual]이 있거나 대상의 [DuelEdgeAlly]가 3 이상이면, 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=4].desc
   limit: do 830 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeUse], [DuelEdgeAlly], [WhenUse], [Combustion], [Vibration], [EvolvingManual], [SuperCoin]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [DuelEdgeAlly] = 결투 고조 / The Duel Escalates; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [BeforeUse] If target has 5 [DuelEdgeAlly], activate "Sezionatura di Cervo" instead (once per turn)\n[WhenUse] <style="highlight">Coin Power +1 for every 6 ([Combustion] + [Vibration]) on target (max 2)</style>\n[WhenUse] Gain the following effects based on [DuelEdgeAlly] Stack on target:\n- <style="highlight">Deal +6% damage for every Stack (max 30%)</style>\n- 1+ [DuelEdgeAlly]: Inflict +1 more [Vibration] Potency\n- 2+ [DuelEdgeAlly]: Inflict +1 more [Vibration] Count\n- 3+ [DuelEdgeAlly]: Inflict +1 more [Combustion] Potency\n- 4+ [DuelEdgeAlly]: Inflict +1 more [Combustion] Count\n[WhenUse] If this unit has [EvolvingManual], or if target has 3+ [DuelEdgeAlly], convert all Coins on this Skill to [SuperCoin]s
   PL: [BeforeUse] Jeżeli cel ma 5 [DuelEdgeAlly], stosuje się jako „Sezionatura di Cervo” (1 raz na turę)\n[WhenUse] <style="highlight">Moc Monet +1 za każde 6 (suma [Combustion] i [Vibration] celu) (maks. 2)</style>\n[WhenUse] Zyskuje poniższe efekty w zależności od stosów [DuelEdgeAlly] celu:\n- <style="highlight">Zadaje +6% obrażeń za każdy 1 stos (maks. 30%)</style>\n- 1+: nakłada o 1 więcej Mocy [Vibration]\n- 2+: nakłada o 1 więcej Licznika [Vibration]\n- 3+: nakłada o 1 więcej Mocy [Combustion]\n- 4+: nakłada o 1 więcej Licznika [Combustion]\n[WhenUse] Jeżeli ma [EvolvingManual] albo cel ma 3+ [DuelEdgeAlly], wszystkie monety tej Umiejętności stają się [SuperCoin]ami
702. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">3</style> 부여, [Combustion] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Combustion] and +2 [Combustion] Count
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Combustion] i zwiększa Licznik [Combustion] o 2
703. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여, [Vibration] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Vibration] i zwiększa Licznik [Vibration] o 2
704. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [EvolvingManual] 1당, 피해량 <style="highlight">+25%</style> (최대 <style="highlight">75%</style>)
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EvolvingManual]
   znaczenie tagów: [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook
   EN: Deal <style="highlight">+25%</style> damage for every [EvolvingManual] on self (max <style="highlight">75%</style>)
   PL: Zadaje <style="highlight">+25%</style> obrażeń za każde 1 [EvolvingManual] (maks. <style="highlight">75%</style>)
705. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]<style="highlight"></style>
   PL: [OnSucceedAttack] Wywołuje [Switch_Vibration] do [VibrationIgnition]<style="highlight"></style>
706. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1<style="highlight"></style>
707. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [EvolvingManual]이 있거나 대상의 [DuelEdgeAlly]가 3 이상이면, [VibrationExplosion] <style="highlight">2회</style>. 대상의 [Vibration] 횟수 <style="highlight">2</style> 감소
   źródło: Skills_personality-07.json :: dataList[id=1071603].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [EvolvingManual], [DuelEdgeAlly], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook; [DuelEdgeAlly] = 결투 고조 / The Duel Escalates; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this unit has [EvolvingManual], or if target has 3+ [DuelEdgeAlly], trigger [VibrationExplosion] <style="highlight">2 times</style>; then, reduce target's [Vibration] Count by <style="highlight">2</style>
   PL: [OnSucceedAttack] Jeżeli ma [EvolvingManual] albo cel ma 3+ [DuelEdgeAlly], wywołuje [VibrationExplosion] <style="highlight">2 razy</style>. Zmniejsza Licznik [Vibration] celu o <style="highlight">2</style>
708. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 세치오나투라 디 체르보
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=3].name ; dataList[id=1071606].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 5 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Sezionatura di Cervo
   PL: Sezionatura di Cervo
709. [Umiejętność 4 (×0) (ulepszenie 3) — opis] [WhenUse]\n- ([EvolvingManual] - 1)만큼 공격 가중치 증가 (최대 2)\n- 메인 타겟의 [Combustion]과 [Vibration]의 합 6당, 코인 위력 +1 (최대 2)\n- 공격 대상이 1이면, 피해량 +15% (집중 전투인 경우, 부위로 판정)\n- 이 스킬 공격 가중치보다 낮은 공격 대상 1당, 피해량 +15% (집중 전투인 경우, 부위로 판정)\n[EndSkill]\n- 메인 타겟이 보유한 [DuelEdgeAlly] 전부 소모\n- [EvolvingManual] 1 얻음. 메인 타겟 사망 시, 대신 2 얻음
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=3].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [EvolvingManual], [Combustion], [Vibration], [EndSkill], [DuelEdgeAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]; [DuelEdgeAlly] = 결투 고조 / The Duel Escalates
   EN: [WhenUse]\n- Gain +([EvolvingManual] - 1) Atk Weight (max 2)\n- Coin Power +1 for every 6 ([Combustion] + [Vibration]) on the main target (max 2)\n- When attacking just 1 target, deal +15% damage (for Focused Encounters, 1 Part)\n- Deal +15% damage for every excess Atk Weight beyond the # of actual targets (for Focused Encounters, Parts)\n\n[EndSkill]\n- Consume all [DuelEdgeAlly] on the main target\n- Gain 1 [EvolvingManual]. If the main target is defeated, gain 2 [EvolvingManual] instead
   PL: [WhenUse]\n- Zyskuje Waga ataku +([EvolvingManual] - 1) (maks. 2)\n- Moc Monet +1 za każde 6 (suma [Combustion] i [Vibration] głównego celu) (maks. 2)\n- Przy ataku na jednego celu zadaje +15% obrażeń (w walkach skupionych 1 Part)\n- Zadaje +15% obrażeń za każdego nadmiarowego celu ataku poza Wagą ataku tej Umiejętności (w walkach skupionych Party)\n[EndSkill]\n- Zużywa całe [DuelEdgeAlly] głównego celu\n- Zyskuje 1 [EvolvingManual]; jeżeli główny cel ginie, zamiast tego zyskuje 2 [EvolvingManual]
710. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여, [Combustion] 횟수 3 증가
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion] and +3 [Combustion] Count
   PL: [OnSucceedAttack] Nakłada 3 [Combustion] i zwiększa Licznik [Combustion] o 3
712. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여, [Vibration] 횟수 3 증가
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and +3 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada 3 [Vibration] i zwiększa Licznik [Vibration] o 3
714. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnStartCoin] [EvolvingManual] 1당, 이 코인의 위력 +1 (최대 3)
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [EvolvingManual]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook
   EN: [OnStartCoin] This Coin gains Coin Power +1 for every [EvolvingManual] (max 3)
   PL: [OnStartCoin] Ta moneta zyskuje Moc Monet +1 za każde 1 [EvolvingManual] (maks. 3)
717. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=3].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 698 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=3].coinlist[#3].coindescs[#3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion] 2 razy. Zmniejsza Licznik [Vibration] celu o 2
719. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [WhenUse]\n- ([EvolvingManual] - 1)만큼 공격 가중치 증가 (최대 2)\n- 메인 타겟의 [Combustion]과 [Vibration]의 합 6당, 코인 위력 +1 (최대 <style="highlight">3</style>)\n- 공격 대상이 1이면, 피해량 <style="highlight">+25%</style> (집중 전투인 경우, 부위로 판정)\n- 이 스킬 공격 가중치보다 낮은 공격 대상 1당, 피해량 <style="highlight">+25%</style> (집중 전투인 경우, 부위로 판정)\n[EndSkill]\n- 메인 타겟이 보유한 [DuelEdgeAlly] 전부 소모\n- [EvolvingManual] 1 얻음. 메인 타겟 사망 시, 대신 2 얻음
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=4].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [EvolvingManual], [Combustion], [Vibration], [EndSkill], [DuelEdgeAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]; [DuelEdgeAlly] = 결투 고조 / The Duel Escalates
   EN: [WhenUse]\n- Gain +([EvolvingManual] - 1) Atk Weight (max 2)\n- Coin Power +1 for every 6 ([Combustion] + [Vibration]) on the main target (max <style="highlight">3</style>)\n- When attacking just 1 target, deal +<style="highlight">25</style>% damage (for Focused Encounters, 1 Part)\n- Deal +<style="highlight">25</style>% damage for every excess Atk Weight beyond the # of actual targets (for Focused Encounters, Parts)\n\n[EndSkill]\n- Consume all [DuelEdgeAlly] on the main target\n- Gain 1 [EvolvingManual]. If the main target is defeated, gain 2 [EvolvingManual] instead
   PL: [WhenUse]\n- Zyskuje Waga ataku +([EvolvingManual] - 1) (maks. 2)\n- Moc Monet +1 za każde 6 (suma [Combustion] i [Vibration] głównego celu) (maks. <style="highlight">3</style>)\n- Przy ataku na jednego celu zadaje <style="highlight">+25</style>% obrażeń (w walkach skupionych 1 Part)\n- Zadaje <style="highlight">+25</style>% obrażeń za każdego nadmiarowego celu ataku poza Wagą ataku tej Umiejętności (w walkach skupionych Party)\n[EndSkill]\n- Zużywa całe [DuelEdgeAlly] głównego celu\n- Zyskuje 1 [EvolvingManual]; jeżeli główny cel ginie, zamiast tego zyskuje 2 [EvolvingManual]
720. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] <style="highlight">4</style> 부여, [Combustion] 횟수 3 증가
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">4</style> [Combustion] and +3 [Combustion] Count
   PL: [OnSucceedAttack] Nakłada <style="highlight">4</style> [Combustion] i zwiększa Licznik [Combustion] o 3
722. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">4</style> 부여, [Vibration] 횟수 3 증가
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">4</style> [Vibration] and +3 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada <style="highlight">4</style> [Vibration] i zwiększa Licznik [Vibration] o 3
724. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnStartCoin] [EvolvingManual] 1당, 이 코인의 위력 +1 (최대 3)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [EvolvingManual]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook
   EN: [OnStartCoin] This Coin gains Coin Power +1 for every [EvolvingManual] (max 3)<style="highlight"></style>
   PL: [OnStartCoin] Ta moneta zyskuje Moc Monet +1 za każde 1 [EvolvingManual] (maks. 3)<style="highlight"></style>
727. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=4].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 705 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion] <style="highlight">3회</style>. 대상의 [Vibration] 횟수 <style="highlight">3</style> 감소
   źródło: Skills_personality-07.json :: dataList[id=1071606].levelList[level=4].coinlist[#3].coindescs[#3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] <style="highlight">3 times</style>; then, reduce target's [Vibration] Count by <style="highlight">3</style>
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion] <style="highlight">3 razy</style>. Zmniejsza Licznik [Vibration] celu o <style="highlight">3</style>
729. [Obrona (ulepszenia 1,4) — nazwa] 검끝 재기
   źródło: Skills_personality-07.json :: dataList[id=1071604].levelList[level=1].name ; dataList[id=1071604].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Measuring Blade Reach
   PL: Pomiar Zasięgu Ostrza
730. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n대상의 [DuelEdgeAlly] 1당 피해량 +10% (최대 50%)
   źródło: Skills_personality-07.json :: dataList[id=1071604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [DuelEdgeAlly]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [DuelEdgeAlly] = 결투 고조 / The Duel Escalates
   EN: [DuelCounter]\nDeal +10% damage for every [DuelEdgeAlly] on target (max 50%)
   PL: [DuelCounter]\nZadaje +10% obrażeń za każde 1 [DuelEdgeAlly] celu (maks. 50%)
731. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여 (턴당 2회)
   źródło: Skills_personality-07.json :: dataList[id=1071604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion] (2 times per turn)
   PL: [OnSucceedAttack] Nakłada 1 [Combustion] (2 razy na turę)
732. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여 (턴당 2회)
   źródło: Skills_personality-07.json :: dataList[id=1071604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration] (2 times per turn)
   PL: [OnSucceedAttack] Nakłada 1 [Vibration] (2 razy na turę)
733. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n대상의 [DuelEdgeAlly] 1당 피해량 <style="highlight">+20%</style> (최대 <style="highlight">100%</style>)\n<style="highlight">[WhenUse] 대상의 [Combustion]과 [Vibration]의 합 4당, 최종 위력 +1 (최대 2)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071604].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [DuelEdgeAlly], [WhenUse], [Combustion], [Vibration]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [DuelEdgeAlly] = 결투 고조 / The Duel Escalates; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: [DuelCounter]\nDeal +<style="highlight">20</style>% damage for every [DuelEdgeAlly] on target (max <style="highlight">100</style>%)\n<style="highlight">[WhenUse] Final Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 2)</style>
   PL: [DuelCounter]\nZadaje <style="highlight">+20</style>% obrażeń za każde 1 [DuelEdgeAlly] celu (maks. <style="highlight">100</style>%)\n<style="highlight">[WhenUse] Moc Końcowa +1 za każde 4 (suma [Combustion] i [Vibration] celu) (maks. 2)</style>
734. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여 (턴당 2회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071604].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion] (2 times per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Combustion] (2 razy na turę)<style="highlight"></style>
735. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여 (턴당 2회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071604].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration] (2 times per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Vibration] (2 razy na turę)<style="highlight"></style>
736. [Obrona (ulepszenia 1,4) — nazwa] 지키겠습니다.
   źródło: Skills_personality-07.json :: dataList[id=1071605].levelList[level=1].name ; dataList[id=1071605].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 3 · monety: 1 (+10)
   limit: do 40 znaków
   EN: I Will Protect.
   PL: Będę Bronić.
737. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬
   źródło: Skills_personality-07.json :: dataList[id=1071605].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [SupportProtect]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense
   EN: [CanDuelGuard]\n[SupportProtect] exclusive Skill
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [SupportProtect]
738. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-07.json :: dataList[id=1071605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n<style="highlight">[WhenUse]\n- [Protection] 2 얻음 (턴당 1회)\n- [SupportProtect]로 보호한 대상의 정신력 5 회복</style>
   źródło: Skills_personality-07.json :: dataList[id=1071605].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [SupportProtect], [WhenUse], [Protection]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Protection] = 보호 / Protection
   EN: [CanDuelGuard]\n[SupportProtect] exclusive Skill\n<style="highlight">[WhenUse]\n- Gain 2 [Protection] (once per turn)\n- Heal 5 SP for the unit protected by the [SupportProtect]</style>
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [SupportProtect]\n<style="highlight">[WhenUse]\n- Zyskuje 2 [Protection] (1 raz na turę)\n- Odzyskuje 5 Poczytalności dla jednostki chronionej przez [SupportProtect]</style>
740. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071605].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
741. [Pasywka bojowa (od ulepszenia 1) — nazwa] 듀엘로 디스페라토
   źródło: Passives.json :: dataList[id=1071602].name
   limit: do 40 znaków
   EN: Duello Disperato
   PL: Duello Disperato
742. [Pasywka bojowa (od ulepszenia 1) — opis] 적에게 기본 스킬 종료 시,\n- 대상이 (다른 부위를 포함하여) [DuelEdgeAlly]를 보유한 상태로 사망했으면, [EvolvingManual] 1 얻음\n- 메인 타겟이 사망하지 않았으면, 메인 타겟에 [DuelEdgeAlly] 1 부여. 해당 대상과 합을 했으면, 대신 2 부여\n\n[DuelEdgeAlly]를 보유한 대상과 합 시작 시,\n대상의 [DuelEdgeAlly] 수치만큼 정신력 회복 (턴당 최대 5)
   źródło: Passives.json :: dataList[id=1071602].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n, [DuelEdgeAlly], [EvolvingManual]
   znaczenie tagów: [DuelEdgeAlly] = 결투 고조 / The Duel Escalates; [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook
   EN: At Base Skill End against an enemy:\n- If the target is defeated while having [DuelEdgeAlly] (on any of its Parts), gain 1 [EvolvingManual]\n- If the main target isn't defeated, inflict 1 [DuelEdgeAlly] on the main target; if there was a Clash against the said main target using the said Base Skill, inflict 2 [DuelEdgeAlly] on the main target instead\n\nAt Clash Start against a target that has [DuelEdgeAlly], heal SP equal to [DuelEdgeAlly] Stack on target (max 5 per turn)
   PL: Na koniec podstawowej Umiejętności przeciwko wrogowi:\n- Jeżeli cel ginie mając [DuelEdgeAlly] (na dowolnej ze swoich Partów), zyskuje 1 [EvolvingManual]\n- Jeżeli główny cel nie ginie, nakłada 1 [DuelEdgeAlly] na główny cel; jeżeli stoczono z nim starcie tą Umiejętnością, zamiast tego nakłada 2 [DuelEdgeAlly]\n\nNa początku starcia z celem mającym [DuelEdgeAlly], odzyskuje Poczytalność równą stosom [DuelEdgeAlly] celu (maks. 5 na turę)
743. [Pasywka bojowa (od ulepszenia 1) — nazwa] 필사의 분전
   źródło: Passives.json :: dataList[id=1071603].name
   limit: do 40 znaków
   EN: Desperate Struggle
   PL: Desperacki Zryw
744. [Pasywka bojowa (od ulepszenia 1) — opis] 거미집 엄지 아비 로쟈가 전장에 있을 경우, 다음 효과 발동\n(자신이 패닉 또는 흐트러진 턴 제외)\n- 거미집 엄지 아비 로쟈가 [FutureEyeOnRodion]이 있을 때 적에게 기본 스킬 적중 시,\n해당 공격 종료 시점에 대상에게 ‘팔레르모 스파다’로 일방 공격 (턴당 1회)\n- 전투 시작 시 거미집 엄지 아비 로쟈가 [FutureEyeOffRodion]이 있는 상태에서 적으로부터 일방 공격으로 지정된 스킬이 있으면,\n거미집 엄지 제자 히스클리프가 [SupportProtect] 1 얻음\n(이 [SupportProtect]는 거미집 엄지 아비 로쟈를 대상으로만 발동)
   źródło: Passives.json :: dataList[id=1071603].desc
   limit: do 830 znaków
   tokeny: zachowaj dokładnie: \n, [FutureEyeOnRodion], [FutureEyeOffRodion], [SupportProtect]
   znaczenie tagów: [FutureEyeOnRodion] = 예지안 / Eye of Precognition; [FutureEyeOffRodion] = 예지안 과열 / Eye of Precognition - Overheat; [SupportProtect] = 원호 방어 / Assist Defense
   EN: If The House of Spiders: The Thumb Nursefather Rodion is on the field, activate the following:\n(Does not activate in turns where this unit is Panicked or Staggered)\n- When The Thumb Nursefather Rodion (that has [FutureEyeOnRodion]) hits an enemy with a Base Skill, at its Attack End, follow up with "La Spada di Palermo" as an Unopposed Attack against the target (once per turn)\n- Combat Start: When The Thumb Nursefather Rodion (that has [FutureEyeOffRodion]) is targeted by an enemy's Unopposed Skill, The Thumb Apprentice Heathcliff gains 1 [SupportProtect]\n(This [SupportProtect] activates only for The House of Spiders: The Thumb Nursefather Rodion)
   PL: Jeżeli Dom Pajęczyn: Abi Kciuka Rodion jest na polu, uruchamia poniższe efekty:\n(nie aktywuje w turze Paniki albo Ogłuszenia tej jednostki)\n- Gdy Abi Kciuka Rodion (posiadająca [FutureEyeOnRodion]) trafia wroga podstawową Umiejętnością, na koniec tego ataku podąża „La Spada di Palermo” jako atak nieoparty przeciwko celowi (1 raz na turę)\n- Na początku walki, jeżeli Abi Kciuka Rodion (posiadająca [FutureEyeOffRodion]) jest celem ataku nieopartego wroga, Uczeń Kciuka Heathcliff zyskuje 1 [SupportProtect]\n(ten [SupportProtect] uruchamia się wyłącznie dla Dom Pajęczyn: Abi Kciuka Rodion)
745. [Pasywka bojowa (od ulepszenia 1) — nazwa] 재회[再会] - 엄지
   źródło: Passives.json :: dataList[id=1071604].name
   limit: do 40 znaków
   EN: Saikai [再会] - The Thumb
   PL: Saikai [再会] - Kciuk
746. [Pasywka bojowa (od ulepszenia 1) — opis] 스테이지 시작 시 사망한 상태거나 전투 중 사망 시,\n거미집의 검 료슈 인격이 아래 효과 얻음\n- [SojiRyoshuEchoPast] 1 얻음\n- 기본 스킬로 합 승리 시 [Vibration] 2를 부여하고 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소 (턴당 2회)
   źródło: Passives.json :: dataList[id=1071604].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [SojiRyoshuEchoPast], [Vibration], [VibrationExplosion]
   znaczenie tagów: [SojiRyoshuEchoPast] = 얽힘 / Entanglement; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: If this unit is defeated at Encounter Start, or if this unit is defeated during the Encounter, Blade of the House of Spiders Ryōshū gains the following effects:\n- Gain 1 [SojiRyoshuEchoPast]\n- On Clash Win using a Base Skill, inflict 2 [Vibration] and trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1 (2 times per turn)
   PL: Jeżeli ginie na początku spotkania albo podczas walki, Ostrze Domu Pajęczyn Ryōshū zyskuje poniższe efekty:\n- Zyskuje 1 [SojiRyoshuEchoPast]\n- Przy wygranej w starciu podstawową Umiejętnością nakłada 2 [Vibration] i wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1 (2 razy na turę)
747. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Lust, posiadane 2× Sloth) — nazwa] 팔레르모 검술
   źródło: Passives.json :: dataList[id=1071601].name
   limit: do 40 znaków
   EN: Palermitan Style
   PL: Szkoła Palermo
748. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Lust, posiadane 2× Sloth) — opis] 자신의 [EvolvingManual]과 메인 타겟 적의 [DuelEdgeAlly] 수치 합에 따라 다음 효과 전부 얻음\n- 수치 1당, 기본 스킬로 가하는 피해량 +3% (최대 15%)\n- 1 : 합 위력 +1\n- 2 : 기본 스킬의 기본 위력 +1\n- 3 : 기본 스킬 공격 적중 시, 다음 턴에 [SeveredTendonAlly] 1 부여\n- 4 : 기본 스킬의 최종 위력 +1\n- 5 : 기본 스킬의 피해량 +15%\n\n자신의 [EvolvingManual]과 자신을 공격하는 적의 [DuelEdgeAlly] 수치 합 1당, 받는 피해량 -3% (최대 -15%)
   źródło: Passives.json :: dataList[id=1071601].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n, [EvolvingManual], [DuelEdgeAlly], [SeveredTendonAlly]
   znaczenie tagów: [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook; [DuelEdgeAlly] = 결투 고조 / The Duel Escalates; [SeveredTendonAlly] = 힘줄 절단 / Severed Tendon
   EN: Gain the following effects based on ([EvolvingManual] on self + [DuelEdgeAlly] on the main target)\n- Base Skills deal +3% damage for every combined Stack (max 15%)\n- 1+ Stack: Clash Power +1\n- 2+ Stack: Base Skills gain Base Power +1\n- 3+ Stack: On Hit using a Base Skill, inflict 1 [SeveredTendonAlly] next turn\n- 4+ Stack: Base Skills gain Final Power +1\n- 5+ Stack: Base Skills deal +15% damage\n\nTake -3% damage for every ([EvolvingManual] on self + [DuelEdgeAlly] on the enemy attacking this unit) (max -15%)
   PL: Zyskuje poniższe efekty w zależności od sumy (własne [EvolvingManual] + [DuelEdgeAlly] głównego celu):\n- Podstawowe Umiejętności zadają +3% obrażeń za każdy 1 łącznego stosu (maks. 15%)\n- 1+: Moc Starcia +1\n- 2+: Podstawowe Umiejętności zyskują Moc Bazowa +1\n- 3+: Przy trafieniu podstawową Umiejętnością nakłada 1 [SeveredTendonAlly] w następnej turze\n- 4+: Podstawowe Umiejętności zyskują Moc Końcowa +1\n- 5+: Podstawowe Umiejętności zadają +15% obrażeń\n\nOtrzymuje -3% obrażeń za każde 1 (suma własnego [EvolvingManual] i [DuelEdgeAlly] wroga atakującego tę jednostkę) (maks. -15%)
749. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 일대일 결투라면…
   źródło: Passives.json :: dataList[id=1071621].name
   limit: do 40 znaków
   EN: In One-on-one Duels...
   PL: W Pojedynku 1 na 1...
750. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 속도가 가장 빠른 아군 1명이 기본 공격 스킬로 합 승리 시,\n대상 적의 [Combustion] 횟수 1 증가 (턴당 1회)\n- 엄지 소속 인격에게 우선 적용\n- 엄지 소속 인격이면 효과가 강화되어, 대신 대상의 [Combustion] 횟수와 [Vibration] 횟수 1 증가\n- 전투 시작 시 적이 1명만 있으면(환상체일 경우, 본체 기준), 이 패시브 효과로 부여하는 [Combustion] 횟수와 [Vibration] 횟수 +1
   źródło: Passives.json :: dataList[id=1071621].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: 1 ally with the fastest Speed: On Clash Win using Base Attack Skills, inflict +1 [Combustion] Count on target (once per turn)\n- Prioritizes "The Thumb" Identities\n- If the ally is "The Thumb" Identity, inflict +1 [Combustion] Count and [Vibration] Count instead\n- Combat Start: If there is only 1 enemy on the field, (for Abnormalities, a Core), this effect inflicts +1 more [Combustion] Count and [Vibration] Count
   PL: Gdy 1 Sojusznik z najwyższą Szybkością wygrywa starcie podstawową Umiejętnością ataku, zwiększa Licznik [Combustion] celu o 1 (1 raz na turę)\n- Najpierw Tożsamości Kciuka\n- Jeżeli tę Tożsamością jest Kciuk, zamiast tego zwiększa Licznik [Combustion] i Licznik [Vibration] celu o 1\n- Na początku walki, jeżeli na polu jest tylko 1 wróg (dla Abnormalności liczy się Rdzeń), ten pasywny efekt zwiększa Licznik [Combustion] i Licznik [Vibration] o 1 więcej

## [000] Haute Couture:: Le Rouge King of Needleworks — Heathcliff — 오트쿠튀르:: 르루주 바느질의 왕
- ID Tożsamości: `10717` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 8 · HP bazowe: 72 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Bleed, Charge

751. [Karta Tożsamości — tytuł] 오트쿠튀르::\n르루주 바느질의 왕
   źródło: Personalities.json :: dataList[id=10717].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Haute Couture::\nLe Rouge\nKing of\nNeedleworks
   PL: Haute Couture::\nLe Rouge\nKról Obszywek
752. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities.json :: dataList[id=10717].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities.json :: dataList[id=10717].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Karta Tożsamości — opis] 히스클리프의 열일곱번째 인격
   źródło: Personalities.json :: dataList[id=10717].desc
   limit: do 120 znaków
   EN: Heathcliff's 17th Identity
   PL: Siedemnasta Tożsamość Heathcliffa
755. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 경사가 어떻고 위사가 저쨌니
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=1].name ; dataList[id=1071701].levelList[level=2].name ; dataList[id=1071701].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 2 · monety: 3 (+3)
   limit: do 50 znaków
   EN: Bla Bla Warp Bla, Yap Yap Weft Yap
   PL: Bla Bla Osnowa, Ja Ja Wątek
756. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeRougeAlly] 횟수가 5 미만이면, 최대 체력의 2 x (5 - 현재 [ChargeRougeAlly] 횟수)%만큼 체력을 소모하여 [ChargeRougeAlly] 횟수가 5로 증가
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ChargeRougeAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [WhenUse] At fewer than 5 [ChargeRougeAlly] Count, consume (2 x (5 - [ChargeRougeAlly] Count))% HP to raise [ChargeRougeAlly] Count to 5
   PL: [WhenUse] Przy mniej niż 5 Licznika [ChargeRougeAlly] zużywa HP równe 2 x (5 - Licznik [ChargeRougeAlly])% Maks. HP, aby zwiększyć Licznik [ChargeRougeAlly] do 5
757. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 4 증가
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +4 [ChargeRougeAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeRougeAlly] o 4
758. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 622 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">자신의 [ChargeRougeAlly] 위력 2당 최종 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수가 5 미만이면, 최대 체력의 2 x (5 - 현재 [ChargeRougeAlly] 횟수)%만큼 체력을 소모하여 [ChargeRougeAlly] 횟수가 5로 증가
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeRougeAlly], [WhenUse]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">Final Power +1 for every 2 [ChargeRougeAlly] Potency on self (max 2)</style>\n[WhenUse] At fewer than 5 [ChargeRougeAlly] Count, consume (2 x (5 - [ChargeRougeAlly] Count))% HP to raise [ChargeRougeAlly] Count to 5
   PL: <style="highlight">Moc Końcowa +1 za każde 2 Mocy [ChargeRougeAlly] (maks. 2)</style>\n[WhenUse] Przy mniej niż 5 Licznika [ChargeRougeAlly] zużywa HP równe 2 x (5 - Licznik [ChargeRougeAlly])% Maks. HP, aby zwiększyć Licznik [ChargeRougeAlly] do 5
760. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 4 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1071701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +4 [ChargeRougeAlly] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeRougeAlly] o 4<style="highlight"></style>
761. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [NeedlekinAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NeedlekinAlly] = 바늘이 / Needlekin
   EN: <style="highlight">[OnSucceedAttack] Deal Pierce damage equal to 1% of this Coin's final damage for every [NeedlekinAlly] Stack on self (min 1)</style>
   PL: <style="highlight">[OnSucceedAttack] Zadaje obrażenia Kłuciem równe 1% końcowych obrażeń tej monety za każdy 1 stosu [NeedlekinAlly] (min. 1)</style>
762. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [NeedlekinAlly] 수치만큼 [NiddlePinAlly] 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1071701].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [NeedlekinAlly], [NiddlePinAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NeedlekinAlly] = 바늘이 / Needlekin; [NiddlePinAlly] = 바늘못 / Naildle
   EN: [OnSucceedAttack] Inflict [NiddlePinAlly] on target equal to [NeedlekinAlly] Stack on self<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada [NiddlePinAlly] równy liczbie stosów [NeedlekinAlly]<style="highlight"></style>
765. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=2].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 [ChargeRougeAlly] 위력 2당 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수가 5 미만이면, 최대 체력의 2 x (5 - 현재 [ChargeRougeAlly] 횟수)%만큼 체력을 소모하여 [ChargeRougeAlly] 횟수가 5로 증가\n<style="highlight">[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=4].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeRougeAlly], [WhenUse], [Laceration]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: Final Power +1 for every 2 [ChargeRougeAlly] Potency on self (max 2)\n[WhenUse] At fewer than 5 [ChargeRougeAlly] Count, consume (2 x (5 - [ChargeRougeAlly] Count))% HP to raise [ChargeRougeAlly] Count to 5\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>
   PL: Moc Końcowa +1 za każde 2 Mocy [ChargeRougeAlly] (maks. 2)\n[WhenUse] Przy mniej niż 5 Licznika [ChargeRougeAlly] zużywa HP równe 2 x (5 - Licznik [ChargeRougeAlly])% Maks. HP, aby zwiększyć Licznik [ChargeRougeAlly] do 5\n<style="highlight">[WhenUse] Jeżeli cel ma 6+ [Laceration], Moc Monet +1</style>
767. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [NeedlekinAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NeedlekinAlly] = 바늘이 / Needlekin
   EN: [OnSucceedAttack] Deal Pierce damage equal to 1% of this Coin's final damage for every [NeedlekinAlly] Stack on self (min 1)<style="highlight"></style>
   PL: [OnSucceedAttack] Zadaje obrażenia Kłuciem równe 1% końcowych obrażeń tej monety za każdy 1 stosu [NeedlekinAlly] (min. 1)<style="highlight"></style>
768. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 767 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071701].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 767 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 땀수! 땀수! 땀수!
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=1].name ; dataList[id=1071702].levelList[level=2].name ; dataList[id=1071702].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 3 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Stitch! Per! Inch!
   PL: Ścieg! Ścieg! Ścieg!
771. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeRougeAlly] 횟수가 10 미만이면, 최대 체력의 2 x (10- 현재 [ChargeRougeAlly] 횟수)%만큼 체력을 소모하여 [ChargeRougeAlly] 횟수가 10으로 증가\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수를 7 소모하여 최종 위력 +2
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeRougeAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [WhenUse] At fewer than 10 [ChargeRougeAlly] Count, consume (2 x (10 - [ChargeRougeAlly] Count))% HP to raise [ChargeRougeAlly] Count to 10\n[WhenUse] Consume 7 [ChargeRougeAlly] Count on self to gain Final Power +2
   PL: [WhenUse] Przy mniej niż 10 Licznika [ChargeRougeAlly] zużywa HP równe 2 x (10 - Licznik [ChargeRougeAlly])% Maks. HP, aby zwiększyć Licznik [ChargeRougeAlly] do 10\n[WhenUse] Zużywa 7 Licznika [ChargeRougeAlly], aby zyskać Moc Końcowa +2
772. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +2 [ChargeRougeAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeRougeAlly] o 2
773. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 2 증가
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">자신의 [ChargeRougeAlly] 위력 2당 최종 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수가 10 미만이면, 최대 체력의 2 x (10- 현재 [ChargeRougeAlly] 횟수)%만큼 체력을 소모하여 [ChargeRougeAlly] 횟수가 10으로 증가\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수를 7 소모하여 최종 위력 +2
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=2].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeRougeAlly], [WhenUse]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">Final Power +1 for every 2 [ChargeRougeAlly] Potency on self (max 2)</style>\n[WhenUse] At fewer than 10 [ChargeRougeAlly] Count, consume (2 x (10 - [ChargeRougeAlly] Count))% HP to raise [ChargeRougeAlly] Count to 10\n[WhenUse] Consume 7 [ChargeRougeAlly] Count on self to gain Final Power +2
   PL: <style="highlight">Moc Końcowa +1 za każde 2 Mocy [ChargeRougeAlly] (maks. 2)</style>\n[WhenUse] Przy mniej niż 10 Licznika [ChargeRougeAlly] zużywa HP równe 2 x (10 - Licznik [ChargeRougeAlly])% Maks. HP, aby zwiększyć Licznik [ChargeRougeAlly] do 10\n[WhenUse] Zużywa 7 Licznika [ChargeRougeAlly], aby zyskać Moc Końcowa +2
780. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1071702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +2 [ChargeRougeAlly] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeRougeAlly] o 2<style="highlight"></style>
781. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1071702].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=2].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1071702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 780 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1071702].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=2].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1071702].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 780 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1071702].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=2].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=2].coinlist[#3].coindescs[#0].desc ; dataList[id=1071702].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 자신의 [NeedlekinAlly] 수치만큼 [NiddlePinAlly] 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=2].coinlist[#3].coindescs[#1].desc ; dataList[id=1071702].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 764 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 4, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=2].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 761 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 [ChargeRougeAlly] 위력 2당 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수가 10 미만이면, 최대 체력의 2 x (10- 현재 [ChargeRougeAlly] 횟수)%만큼 체력을 소모하여 [ChargeRougeAlly] 횟수가 10으로 증가\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수를 7 소모하여 최종 위력 +2\n<style="highlight">[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=4].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeRougeAlly], [WhenUse], [Laceration]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: Final Power +1 for every 2 [ChargeRougeAlly] Potency on self (max 2)\n[WhenUse] At fewer than 10 [ChargeRougeAlly] Count, consume (2 x (10 - [ChargeRougeAlly] Count))% HP to raise [ChargeRougeAlly] Count to 10\n[WhenUse] Consume 7 [ChargeRougeAlly] Count on self to gain Final Power +2\n<style="highlight">[WhenUse] If target has 6+ [Laceration], Coin Power +1</style>
   PL: Moc Końcowa +1 za każde 2 Mocy [ChargeRougeAlly] (maks. 2)\n[WhenUse] Przy mniej niż 10 Licznika [ChargeRougeAlly] zużywa HP równe 2 x (10 - Licznik [ChargeRougeAlly])% Maks. HP, aby zwiększyć Licznik [ChargeRougeAlly] do 10\n[WhenUse] Zużywa 7 Licznika [ChargeRougeAlly], aby zyskać Moc Końcowa +2\n<style="highlight">[WhenUse] Jeżeli cel ma 6+ [Laceration], Moc Monet +1</style>
793. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 767 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 767 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 767 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] 자신의 [NeedlekinAlly] 수치 1당 이 코인 최종 피해량의 1%만큼 관통 피해 (최소 1)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071702].levelList[level=4].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 767 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 피크스티치 일부러 눈에 띄게 박았냐고?! 그렇게 쳐박아주마!
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=3].name ; dataList[id=1071703].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 90 znaków
   EN: Pick stitch too obvious, you say?! I'll pick-stitch your bum!
   PL: Ścieg pikowy celowo rzuca się w oczy?! Wbiję ci takiego ściega!
798. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 [NiddlePinGather] 15당 공격 가중치 +1 (최대 2)\n[WhenUse] 이 스킬 가중치보다 낮은 대상 1당, 피해량 +30% (집중 전투인 경우, 부위로 판정)\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수를 최대 20까지 소모\n- 소모값 7당 코인 위력 +1 (최대 2)\n- 소모값 1당 이 스킬 피해량 +2%\n[EndSkill] ([NiddlePinGather]로 증가한 공격 가중치 x 15)만큼 자신의 [NiddlePinGather] 소모
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=3].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [NiddlePinGather], [ChargeRougeAlly], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [NiddlePinGather] = 작고 뾰족한 못 / Tiny and Sharp Nails; [ChargeRougeAlly] = 맥동 / Pulsation; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WhenUse] Gain Atk Weight +1 for every 15 [NiddlePinGather] on self (max 2)\n[WhenUse] Deal +30% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Parts)\n[WhenUse] Consume up to 20 [ChargeRougeAlly] Count on self to apply the following effects:\n- Coin Power +1 for every 7 [ChargeRougeAlly] Count consumed (max 2)\n- Deal +2% damage using this Skill for every [ChargeRougeAlly] Count consumed\n[EndSkill] Consume [NiddlePinGather] on self equal to (Atk Weight gained from [NiddlePinGather] x 15)
   PL: [WhenUse] Waga ataku +1 za każde 15 [NiddlePinGather] (maks. 2)\n[WhenUse] Zadaje +30% obrażeń za każdego nadmiarowego celu ataku poza Wagą ataku tej Umiejętności (w walkach skupionych sądzi się w Partach)\n[WhenUse] Zużywa do 20 Licznika [ChargeRougeAlly], aby stosować poniższe efekty:\n- Moc Monet +1 za każde 7 zużytego Licznika [ChargeRougeAlly] (maks. 2)\n- Zadaje +2% obrażeń tą Umiejętnością za każde 1 zużytego Licznika [ChargeRougeAlly]\n[EndSkill] Zużywa [NiddlePinGather] równy wartości (Wzrost Poziomu Ataku zyskany z [NiddlePinGather] x 15)
799. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 3 증가 (스킬당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +3 [ChargeRougeAlly] Count (once per Skill)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeRougeAlly] o 3 (1 raz na Umiejętność)
800. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 3 증가 (스킬당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 799 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [NiddlePinAlly] 3 부여
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NiddlePinAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NiddlePinAlly] = 바늘못 / Naildle
   EN: [OnSucceedAttack] Inflict 3 [NiddlePinAlly]
   PL: [OnSucceedAttack] Nakłada 3 [NiddlePinAlly]
804. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 각 대상의 [NiddlePinAlly]이 5 이상이면, 대상의 [NiddlePinAlly]을 5 소모하여 다음 턴에 해당 대상에게 [NiddlePinnedAlly] 부여
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NiddlePinAlly], [NiddlePinnedAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NiddlePinAlly] = 바늘못 / Naildle; [NiddlePinnedAlly] = 박제 상태 / Taxidermized
   EN: [OnSucceedAttack] If target has 5+ [NiddlePinAlly], consume 5 [NiddlePinAlly] on target to inflict [NiddlePinnedAlly] on the said target next turn (counted per target)
   PL: [OnSucceedAttack] Jeżeli cel ma 5+ [NiddlePinAlly], zużywa 5 [NiddlePinAlly] celu, aby nałożyć [NiddlePinnedAlly] na tego celu w następnej turze
805. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">자신의 [ChargeRougeAlly] 위력 2당 최종 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [NiddlePinGather] 15당 공격 가중치 +1 (최대 2)\n[WhenUse] 이 스킬 가중치보다 낮은 대상 1당, 피해량 +30% (집중 전투인 경우, 부위로 판정)\n[WhenUse] 자신의 [ChargeRougeAlly] 횟수를 최대 20까지 소모\n- 소모값 7당 코인 위력 +1 (최대 2)\n- 소모값 1당 이 스킬 피해량 +2%\n[EndSkill] ([NiddlePinGather]로 증가한 공격 가중치 x 15)만큼 자신의 [NiddlePinGather] 소모
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=4].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeRougeAlly], [WhenUse], [NiddlePinGather], [EndSkill]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [WhenUse] = [사용시] / [On Use]; [NiddlePinGather] = 작고 뾰족한 못 / Tiny and Sharp Nails; [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">Final Power +1 for every 2 [ChargeRougeAlly] Potency on self (max 2)</style>\n[WhenUse] Gain Atk Weight +1 for every 15 [NiddlePinGather] on self (max 2)\n[WhenUse] Deal +30% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Parts)\n[WhenUse] Consume up to 20 [ChargeRougeAlly] Count on self to apply the following effects:\n- Coin Power +1 for every 7 [ChargeRougeAlly] Count consumed (max 2)\n- Deal +2% damage using this Skill for every [ChargeRougeAlly] Count consumed\n[EndSkill] Consume [NiddlePinGather] on self equal to (Atk Weight gained from [NiddlePinGather] x 15)
   PL: <style="highlight">Moc Końcowa +1 za każde 2 Mocy [ChargeRougeAlly] (maks. 2)</style>\n[WhenUse] Waga ataku +1 za każde 15 [NiddlePinGather] (maks. 2)\n[WhenUse] Zadaje +30% obrażeń za każdego nadmiarowego celu ataku poza Wagą ataku tej Umiejętności (w walkach skupionych sądzi się w Partach)\n[WhenUse] Zużywa do 20 Licznika [ChargeRougeAlly], aby stosować poniższe efekty:\n- Moc Monet +1 za każde 7 zużytego Licznika [ChargeRougeAlly] (maks. 2)\n- Zadaje +2% obrażeń tą Umiejętnością za każde 1 zużytego Licznika [ChargeRougeAlly]\n[EndSkill] Zużywa [NiddlePinGather] równy wartości (Wzrost Poziomu Ataku zyskany z [NiddlePinGather] x 15)
806. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 3 증가 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +3 [ChargeRougeAlly] Count (once per Skill)<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeRougeAlly] o 3 (1 raz na Umiejętność)<style="highlight"></style>
807. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 3 증가 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 806 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [NiddlePinAlly] 3 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [NiddlePinAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NiddlePinAlly] = 바늘못 / Naildle
   EN: [OnSucceedAttack] Inflict 3 [NiddlePinAlly]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [NiddlePinAlly]<style="highlight"></style>
811. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [PenetrateTakeDamageUp] 1 부여</style>
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp] next turn</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [PenetrateTakeDamageUp] w następnej turze</style>
812. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 각 대상의 [NiddlePinAlly]이 5 이상이면, 대상의 [NiddlePinAlly]을 5 소모하여 다음 턴에 해당 대상에게 [NiddlePinnedAlly] 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071703].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [NiddlePinAlly], [NiddlePinnedAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NiddlePinAlly] = 바늘못 / Naildle; [NiddlePinnedAlly] = 박제 상태 / Taxidermized
   EN: [OnSucceedAttack] If target has 5+ [NiddlePinAlly], consume 5 [NiddlePinAlly] on target to inflict [NiddlePinnedAlly] on the said target next turn (counted per target)<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli cel ma 5+ [NiddlePinAlly], zużywa 5 [NiddlePinAlly] celu, aby nałożyć [NiddlePinnedAlly] na tego celu w następnej turze<style="highlight"></style>
813. [Umiejętność 4 (×0) (ulepszenie 2) — nazwa] 옆선 바깥에 박음선 두 줄 보이면 더블니들. 탈락!
   źródło: Skills_personality-07.json :: dataList[id=1071705].levelList[level=2].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 12 · monety: 3 (+3)
   limit: do 90 znaków
   EN: Double stitching past the side seam? Double-needle! Rejected!
   PL: Podwójny ścieg za szwem bocznym? Podwójna igła! Odrzucone!
814. [Umiejętność 4 (×0) (ulepszenie 2) — opis] [WideAreaRampage]\n이 스킬에서 적중시, 자신의 최대 체력의 8% 회복\n[WhenUse] 자신의 [NeedlekinAlly]를 모두 소모하여, 다음 턴에 자신과 자신을 제외한 무작위 아군 2명 에게 [PenetrateDamageUp] 1 부여\n- 르루주 소속에게 우선으로 적용됨 (편성 순)
   źródło: Skills_personality-07.json :: dataList[id=1071705].levelList[level=2].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [WhenUse], [NeedlekinAlly], [PenetrateDamageUp]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [NeedlekinAlly] = 바늘이 / Needlekin; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up
   EN: [WideAreaRampage]\nOn Hit using this Skill, heal 8% HP\n[WhenUse] Consume all [NeedlekinAlly] on self to apply 1 [PenetrateDamageUp] to this unit and 2 other random allies next turn\n- Prioritizes "Le Rouge" Identities (in Deployment Order)
   PL: [WideAreaRampage]\nPrzy trafieniu tą Umiejętnością odzyskuje 8% HP\n[WhenUse] Zużywa całe [NeedlekinAlly], aby nałożyć 1 [PenetrateDamageUp] w następnej turze na siebie i 2 innych losowych sojuszników\n- Najpierw Tożsamości Le Rouge (kolejność przydzielania)
815. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071705].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeRougeAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRougeAlly] = 맥동 / Pulsation
   EN: [OnSucceedAttack] Gain +1 [ChargeRougeAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeRougeAlly] o 1
816. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NiddlePinAlly] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071705].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NiddlePinAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NiddlePinAlly] = 바늘못 / Naildle
   EN: [OnSucceedAttack] Inflict 2 [NiddlePinAlly]
   PL: [OnSucceedAttack] Nakłada 2 [NiddlePinAlly]
817. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071705].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 815 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NiddlePinAlly] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071705].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 816 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeRougeAlly] 횟수 1 증가
   źródło: Skills_personality-07.json :: dataList[id=1071705].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 815 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [NiddlePinAlly] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071705].levelList[level=2].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 816 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
821. [Obrona (ulepszenia 1,4) — nazwa] 으드득…
   źródło: Skills_personality-07.json :: dataList[id=1071704].levelList[level=1].name ; dataList[id=1071704].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 7 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Gnnnngh...
   PL: Gnnnngh...
822. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] 자신의 최대 체력의 20%를 소모하여, 다음 턴에 [Enhancement] 1 얻음 (턴당 1회)
   źródło: Skills_personality-07.json :: dataList[id=1071704].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [Enhancement]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [DuelCounter]\n[StartBattle] Consume 20% HP on self to gain 1 [Enhancement] next turn (once per turn)
   PL: [DuelCounter]\n[StartBattle] Zużywa 20% HP, aby zyskać 1 [Enhancement] w następnej turze (1 raz na turę)
823. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [NiddlePinAlly] 2 부여
   źródło: Skills_personality-07.json :: dataList[id=1071704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 816 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
824. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[StartBattle] 자신의 최대 체력의 20%를 소모하여, 다음 턴에 <style="highlight">[Enhancement] 2, [ChargeRougeAlly] 횟수 5</style> 얻음 (턴당 1회)\n<style="highlight">[WhenUse] 자신의 [ChargeRougeAlly] 위력 2당 최종 위력 +1 (최대 2)</style>
   źródło: Skills_personality-07.json :: dataList[id=1071704].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [Enhancement], [ChargeRougeAlly], [WhenUse]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [ChargeRougeAlly] = 맥동 / Pulsation; [WhenUse] = [사용시] / [On Use]
   EN: [DuelCounter]\n[StartBattle] Consume 20% HP on self to gain <style="highlight">2 [Enhancement] and +5 [ChargeRougeAlly] Count</style> next turn (once per turn)\n<style="highlight">[WhenUse] Final Power +1 for every 2 [ChargeRougeAlly] Potency on self (max 2)</style>
   PL: [DuelCounter]\n[StartBattle] Zużywa 20% HP, aby zyskać <style="highlight">2 [Enhancement] i zwiększyć Licznik [ChargeRougeAlly] o 5</style> w następnej turze (1 raz na turę)\n<style="highlight">[WhenUse] Moc Końcowa +1 za każde 2 Mocy [ChargeRougeAlly] (maks. 2)</style>
825. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [NiddlePinAlly] 2 부여<style="highlight"></style>
   źródło: Skills_personality-07.json :: dataList[id=1071704].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [NiddlePinAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NiddlePinAlly] = 바늘못 / Naildle
   EN: [OnSucceedAttack] Inflict 2 [NiddlePinAlly]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [NiddlePinAlly]<style="highlight"></style>
826. [Pasywka bojowa (od ulepszenia 1) — nazwa] 아직도 들리는 것 같은 클레임
   źródło: Passives.json :: dataList[id=1071702].name
   limit: do 60 znaków
   EN: Customer Complaints Haunting the Ears
   PL: Żale Klientów Nawiedzające Ucho
827. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 중 누적으로 자신의 [ChargeRougeAlly] 횟수 10을 소모할 때마다 [ChargeRougeAlly] 위력 1 얻음\n\n턴 시작시 전장에 아군 오트쿠튀르::르루주 붉은 신 싱클레어 인격이 있으면 [HowlingCocoonAlly] 1 증가\n\n턴 시작시 자신의 [HowlingCocoonAlly]이 최대치거나, 아군 오트쿠튀르::르루주 붉은 신 싱클레어 인격이 [TransformSinclair]이 있으면,\n[HowlingCocoonAlly]을 [HowlingCocoonTwoAlly]으로 변경하고 아군 오트쿠튀르::르루주 붉은 신 싱클레어 인격이 아래 효과 얻음\n- [RougeFamilySinclair] 1 얻음\n- '라 드망드(la demande)' 스킬 코인 적중 시 [ChargeRougeAlly] 횟수를 1 얻고, 자신의 최대 체력의 5%만큼 회복
   źródło: Passives.json :: dataList[id=1071702].desc
   limit: do 820 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRougeAlly], [HowlingCocoonAlly], [TransformSinclair], [HowlingCocoonTwoAlly], [RougeFamilySinclair]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [HowlingCocoonAlly] = 고치의 울음소리 - 미약 / Cry of the Cocoon - Frail; [TransformSinclair] = 고귀한 품격 / Noble Dignity; [HowlingCocoonTwoAlly] = 고치의 울음소리 - 악성 / Cry of the Cocoon - Vicious; [RougeFamilySinclair] = 붉은 요람 / Crimson Cradle
   EN: Gain 1 [ChargeRougeAlly] Potency for every 10 cumulative [ChargeRougeAlly] Count this unit consumes in this Encounter\n\nTurn Start: If allied Haute Couture::The Crimson God of Le Rouge Sinclair is on the field, gain 1 [HowlingCocoonAlly]\n\nTurn Start: At max [HowlingCocoonAlly] Stack, or if allied Haute Couture::The Crimson God of Le Rouge Sinclair has [TransformSinclair], convert [HowlingCocoonAlly] into [HowlingCocoonTwoAlly]; then, allied Haute Couture::The Crimson God of Le Rouge Sinclair gains the following effects:\n- Gain 1 [RougeFamilySinclair]\n- On Hit using the "La Demande" Skill's Coins, gain +1 [ChargeRougeAlly] Count and heal 5% HP
   PL: Za każde łączne zużycie 10 własnego Licznika [ChargeRougeAlly] podczas walki zyskuje 1 Mocy [ChargeRougeAlly]\n\nNa początku tury, jeżeli na polu jest sojusznik Haute Couture::Bogini Szkarłatu Le Rouge Sinclair, zwiększa [HowlingCocoonAlly] o 1\n\nNa początku tury, przy maksymalnej liczbie stosów [HowlingCocoonAlly] albo jeżeli sojusznik Haute Couture::Bogini Szkarłatu Le Rouge Sinclair ma [TransformSinclair], zamienia [HowlingCocoonAlly] na [HowlingCocoonTwoAlly], a sojusznik Haute Couture::Bogini Szkarłatu Le Rouge Sinclair zyskuje poniższe efekty:\n- Zyskuje 1 [RougeFamilySinclair]\n- Przy trafieniu monetami Umiejętności „La Demande” zyskuje 1 Licznika [ChargeRougeAlly] i odzyskuje 5% HP
828. [Pasywka bojowa (od ulepszenia 1) — nazwa] 핸드메이드 / 핸드 스티칭하라고!!!
   źródło: Passives.json :: dataList[id=1071703].name
   limit: do 90 znaków
   EN: Handmade? You want me to hand-stitch this?! HAND-STITCH???!!!
   PL: Ręczna robota? Chcesz, żebym szyła ręcznie?! RĘCZNIE-SZYJĄCA???!!!
829. [Pasywka bojowa (od ulepszenia 1) — opis] 자신의 체력이 최대 체력의 3%만큼 감소할 때마다 [ChargeRougeAlly] 횟수 1 얻음 (턴당 최대 20)\n\n자신의 체력이 최대 체력의 1.5%만큼 감소할 때마다 [NiddlePinGather] 1 얻음\n\n자신의 기본 스킬의 체력 감소 효과로 흐트러지거나 체력이 1 미만으로 감소하지 않음 (체력이 1인 경우, 기본 스킬 효과중 체력 소모로 발동되는 효과를 적용 받을 수 있음)
   źródło: Passives.json :: dataList[id=1071703].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRougeAlly], [NiddlePinGather]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [NiddlePinGather] = 작고 뾰족한 못 / Tiny and Sharp Nails
   EN: Every time this unit loses 3% HP, gain +1 [ChargeRougeAlly] Count (max 20 per turn)\n\nEvery time this unit loses 1.5% HP, gain 1 [NiddlePinGather]\n\nHP consumption effects from this unit's Base Skills do not Stagger or reduce this unit's HP below 1 (At 1 HP, Base Skill effects that consume HP will be activated for free)
   PL: Za każde utratę 3% HP zyskuje 1 Licznika [ChargeRougeAlly] (maks. 20 na turę)\n\nZa każde utratę 1.5% HP zyskuje 1 [NiddlePinGather]\n\nEfekty zużycia HP własnych podstawowych Umiejętności nie Ogłuszają ani nie obniżają HP tej jednostki poniżej 1 (przy 1 HP efekty zużycia HP podstawowych Umiejętności uruchamiane są bezpłatnie)
830. [Pasywka bojowa (od ulepszenia 2) — nazwa] 핸드메이드 / 핸드 스티칭하라고!!!
   źródło: Passives.json :: dataList[id=1071713].name
   (powtórzenie elementu 828 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Pasywka bojowa (od ulepszenia 2) — opis] 자신의 체력이 최대 체력의 3%만큼 감소할 때마다 [ChargeRougeAlly] 횟수 1 얻음 (턴당 최대 20)\n\n자신의 체력이 최대 체력의 1.5%만큼 감소할 때마다 [NiddlePinGather] 1 얻음\n\n자신의 기본 스킬의 체력 감소 효과로 흐트러지거나 체력이 1 미만으로 감소하지 않음 (체력이 1인 경우, 기본 스킬 효과중 체력 소모로 발동되는 효과를 적용 받을 수 있음)\n\n자신의 [NeedlekinAlly]가 3일 때 자신의 공격 스킬 종료시, 무작위 적에게 '옆선 바깥에 박음선 두 줄 보이면 더블니들. 탈락!' 스킬 사용
   źródło: Passives.json :: dataList[id=1071713].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRougeAlly], [NiddlePinGather], [NeedlekinAlly]
   znaczenie tagów: [ChargeRougeAlly] = 맥동 / Pulsation; [NiddlePinGather] = 작고 뾰족한 못 / Tiny and Sharp Nails; [NeedlekinAlly] = 바늘이 / Needlekin
   EN: Every time this unit loses 3% HP, gain +1 [ChargeRougeAlly] Count (max 20 per turn)\n\nEvery time this unit loses 1.5% HP, gain 1 [NiddlePinGather]\n\nHP consumption effects from this unit's Base Skills do not Stagger or reduce this unit's HP below 1 (at 1 HP, Base Skill effects that consume HP will be activated for free)\n\nAt 3 [NeedlekinAlly], use the "Double stitching past the side seam? Double-needle! Rejected!" Skill on random enemies at Attack Skill End
   PL: Za każde utratę 3% HP zyskuje 1 Licznika [ChargeRougeAlly] (maks. 20 na turę)\n\nZa każde utratę 1.5% HP zyskuje 1 [NiddlePinGather]\n\nEfekty zużycia HP własnych podstawowych Umiejętności nie Ogłuszają ani nie obniżają HP tej jednostki poniżej 1 (przy 1 HP efekty zużycia HP podstawowych Umiejętności uruchamiane są bezpłatnie)\n\nPrzy 3 [NeedlekinAlly], na koniec Umiejętności ataku używa Umiejętności „Podwójny ścieg za szwem bocznym? Podwójna igła! Odrzucone!” na losowych wrogach
832. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Lust) — nazwa] 스티치가 너무 균일하다고? 손 피크가 아니라고? 집합!!!
   źródło: Passives.json :: dataList[id=1071701].name
   limit: do 80 znaków
   EN: Too even, you say? Not pick-stitching, you say? Assemble!!!
   PL: Za równo? To nie ścieg pikowy? ZBIÓRKA!!!
833. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Lust) — opis] 턴 종료시, [NeedlekinAlly] 1 얻음
   źródło: Passives.json :: dataList[id=1071701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NeedlekinAlly]
   znaczenie tagów: [NeedlekinAlly] = 바늘이 / Needlekin
   EN: Turn End: Gain 1 [NeedlekinAlly]
   PL: Na koniec tury zyskuje 1 [NeedlekinAlly]
834. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Lust) — nazwa] 인치당 땀수 20 이상으로!!!
   źródło: Passives.json :: dataList[id=1071721].name
   limit: do 50 znaków
   EN: 20 stitches an inch, minimum!!!
   PL: 20 ściegów na cal, minimum!!!
835. [Pasywka wsparcia (od ulepszenia 3, rezonans 2× Lust) — opis] 속도가 가장 빠른 아군 1명의 기본 공격 스킬 적중시, [Laceration] 2 부여 (턴당 1회)\n- 해당 아군이 르루주 소속이면, [NiddlePinAlly] 1 추가 부여
   źródło: Passives.json :: dataList[id=1071721].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [NiddlePinAlly]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [NiddlePinAlly] = 바늘못 / Naildle
   EN: 1 ally with the fastest Speed: On Hit using Base Attack Skills, inflict 2 [Laceration] (once per turn)\n- If the said ally is a "Le Rouge" Identity, additionally inflict 1 [NiddlePinAlly]
   PL: Gdy 1 Sojusznik z najwyższą Szybkością trafia podstawową Umiejętnością ataku, nakłada 2 [Laceration] (1 raz na turę)\n- Jeżeli ten sojusznik należy do frakcji Le Rouge, dodatkowo nakłada 1 [NiddlePinAlly]

## [?] Cheery Chickies Sinnerling — Heathcliff — 병아리반 수감생
- ID Tożsamości: `400031` (plik: `Personalities-x1p1c1.json`)

836. [Karta Tożsamości — tytuł] 병아리반 수감생
   źródło: Personalities-x1p1c1.json :: dataList[id=400031].title
   limit: do 40 znaków
   EN: Cheery Chickies Sinnerling
   PL: Grzeszniczek Grupy Pisklaków
837. [Karta Tożsamości — nazwa] 히스클리프
   źródło: Personalities-x1p1c1.json :: dataList[id=400031].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Karta Tożsamości — nazwa z tytułem] 히스클리프
   źródło: Personalities-x1p1c1.json :: dataList[id=400031].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Karta Tożsamości — opis] 히스클리프의 ??? 인격
   źródło: Personalities-x1p1c1.json :: dataList[id=400031].desc
   limit: do 120 znaków
   EN: Heathcliff's ??? Identity
   PL: ??? Tożsamość Heathcliffa
840. [Pasywka bojowa [40003101] — nazwa] 르쌍띠망
   źródło: Passives-x1p1c1.json :: dataList[id=40003101].name
   limit: do 40 znaków
   EN: Reshenshimen
   PL: — nazwa] Reszenszimen
841. [Pasywka bojowa [40003101] — opis] 대상이 자신보다 최대 체력이 높으면 피해량 +10%
   źródło: Passives-x1p1c1.json :: dataList[id=40003101].desc
   limit: do 120 znaków
   EN: Deal +10% damage to targets with higher Max HP.
   PL: — opis] Zadaje +10% obrażeń celom z wyższym Maks. HP.
842. [Pasywka bojowa [40003102] — nazwa] 악에 받찐
   źródło: Passives-x1p1c1.json :: dataList[id=40003102].name
   limit: do 40 znaków
   EN: Spite-dwiven
   PL: — nazwa] Napędzany Złością
843. [Pasywka bojowa [40003102] — opis] 최대 체력이 가장 낮은 아군 1명 타격 스킬의 피해량 +10%
   źródło: Passives-x1p1c1.json :: dataList[id=40003102].desc
   limit: do 120 znaków
   EN: 1 ally with the lowest Max HP deals +10% Blunt damage.
   PL: — opis] 1 Sojusznik z najniższym Maks. HP zadaje +10% obrażeń Uderzenia.
