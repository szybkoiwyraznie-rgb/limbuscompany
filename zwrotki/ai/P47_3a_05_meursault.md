# Paczka AI P47 (Fala 3 · 3A) — Grzesznik 05 — Meursault

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P47_3a_05_meursault.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P47_3a_05_meursault.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Grzesznik #05: Meursault (뫼르소)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 뫼르소
   źródło: Characters.json :: dataList[id=5].name
   limit: do 40 znaków
   EN: Meursault
   PL: Meursault
2. [Akta więźnia — nazwa] 뫼르소
   źródło: IntroduceCharacter.json :: dataList[id=뫼르소].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [0] LCB Sinner — Meursault — LCB 수감자
- ID Tożsamości: `10501` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 90 · szybkość: 1–2 / 1–2 / 2–3 / 2–3
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Tremor

3. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10501].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL: LCB\nGrzesznik
4. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10501].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
5. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10501].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — opis] 뫼르소의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10501].desc
   limit: do 120 znaków
   EN: Meursault’s 1st Identity
   PL: Pierwsza Tożsamość Meursaulta
7. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 원, 투
   źródło: Skills.json :: dataList[id=1050101].levelList[level=1].name ; dataList[id=1050101].levelList[level=2].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Un, Deux
   PL: Un, Deux
8. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 1 [Vibration]
   PL: [OnSucceedAttackHead] Nakłada 1 [Vibration]
9. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
10. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]
11. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050101].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
12. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 주먹꽂기
   źródło: Skills.json :: dataList[id=1050102].levelList[level=1].name ; dataList[id=1050102].levelList[level=2].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 6 · monety: 1 (+9)
   limit: do 40 znaków
   EN: Nailing Fist
   PL: Wbijająca Pięść
13. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills.json :: dataList[id=1050102].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050102].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]
   PL: [OnSucceedAttack] Wybuch Wstrząsu
14. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 수비 위력 증가 3 얻음
   źródło: Skills.json :: dataList[id=1050102].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 3 Defense Power Up next turn
   PL: [WhenUse] Zyskuje w następnej turze 3 Wzrostu Mocy Obrony
15. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 연격
   źródło: Skills.json :: dataList[id=1050103].levelList[level=3].name ; dataList[id=1050103].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Des Coups
   PL: Przerzutnia
16. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] [WhenUse] 다음 턴에 보호 3 얻음
   źródło: Skills.json :: dataList[id=1050103].levelList[level=3].desc ; dataList[id=1050103].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 3 Protection next turn
   PL: [WhenUse] Zyskuje w następnej turze 3 Ochrony
17. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttackHead] 진동 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050103].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttackHead] Nakłada +2 Licznika Wstrząsu
18. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
19. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
20. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
21. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 진동 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050103].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika Wstrząsu
22. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1050104].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+3)
   limit: do 40 znaków
   EN: Guard
   PL: Garda
23. [Pasywka bojowa (od ulepszenia 1, posiadane 2× Sloth) — nazwa] 각오
   źródło: Passives.json :: dataList[id=1050101].name
   limit: do 40 znaków
   EN: Staunchness
   PL: Postanowienie
24. [Pasywka bojowa (od ulepszenia 1, posiadane 2× Sloth) — opis] 전투 시작 시 자신의 체력이 50% 미만이면 보호 1을 얻음
   źródło: Passives.json :: dataList[id=1050101].desc
   limit: do 120 znaków
   EN: At less than 50% HP, gain 1 Protection at the start of the combat phase.
   PL: Na początku walki przy HP poniżej 50% zyskuje 1 Ochrony
25. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — nazwa] 등뒤 받쳐주기
   źródło: Passives.json :: dataList[id=1050121].name
   limit: do 40 znaków
   EN: Backup
   PL: Przykrycie Odwrotu
26. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — opis] 최대 체력이 가장 높은 아군 1명 공격 스킬로 받는 피해량 -10%
   źródło: Passives.json :: dataList[id=1050121].desc
   limit: do 120 znaków
   EN: 1 ally with the highest Max HP takes -10% damage from attack skills.
   PL: 1 Sojusznik z najwyższym Maks. HP otrzymuje -10% obrażeń od Umiejętności ataku.

## [00] Liu Assoc. South Section 6 — Meursault — 남부 리우 협회 6과
- ID Tożsamości: `10502` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 1–4 / 1–5 / 2–5 / 2–5
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Burn

27. [Karta Tożsamości — tytuł] 남부 리우 협회\n6과
   źródło: Personalities.json :: dataList[id=10502].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Liu Assoc.\nSouth Section 6
   PL: Południowe Stowarzyszenie Liu\nSekcja 6
28. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10502].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
29. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10502].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
30. [Karta Tożsamości — opis] 뫼르소의 두번째 인격
   źródło: Personalities.json :: dataList[id=10502].desc
   limit: do 120 znaków
   EN: Meursault’s 2nd Identity
   PL: Druga Tożsamość Meursaulta
31. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 돌파
   źródło: Skills.json :: dataList[id=1050201].levelList[level=1].name ; dataList[id=1050201].levelList[level=2].name ; dataList[id=1050201].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Assault
   PL: Szturm od Frontu
32. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1050201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Burn
   PL: [OnSucceedAttackHead] Nakłada 1 Podpalenia
33. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1050201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
34. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1050201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Burn
   PL: [OnSucceedAttack] Nakłada 1 Podpalenia
35. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1050201].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
36. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills.json :: dataList[id=1050201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Burn
   PL: [OnSucceedAttack] Nakłada 2 Podpalenia
37. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 진각
   źródło: Skills.json :: dataList[id=1050202].levelList[level=1].name ; dataList[id=1050202].levelList[level=2].name ; dataList[id=1050202].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 7 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Stalwart Stance
   PL: Postawa Twarda
38. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 화상 2 부여
   źródło: Skills.json :: dataList[id=1050202].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
39. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 화상 1 부여
   źródło: Skills.json :: dataList[id=1050202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
40. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 무작위 적 2명에게 화상 2 부여
   źródło: Skills.json :: dataList[id=1050202].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], inflict 2 Burn on 2 random enemies
   PL: [OnSucceedAttack] Jeżeli cel ma 6+ [Combustion], nakłada 2 Podpalenia na 2 losowych wrogów
41. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1050202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
42. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 무작위 적 2명에게 화상 3 부여
   źródło: Skills.json :: dataList[id=1050202].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], inflict 3 Burn on 2 random enemies
   PL: [OnSucceedAttack] Jeżeli cel ma 6+ [Combustion], nakłada 3 Podpalenia na 2 losowych wrogów
43. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 연무 붕권
   źródło: Skills.json :: dataList[id=1050203].levelList[level=3].name ; dataList[id=1050203].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Perfected Death Fist
   PL: Mistrzowska Pięść Śmierci
44. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 화상 3 부여
   źródło: Skills.json :: dataList[id=1050203].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Burn
   PL: [OnSucceedAttackHead] Nakłada 3 Podpalenia
45. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 화상 횟수 3 증가
   źródło: Skills.json :: dataList[id=1050203].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1050203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Burn Count
   PL: [OnSucceedAttack] Zwiększa Licznik Podpalenia o 3
46. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 무작위 적 2명에게 화상 3 부여
   źródło: Skills.json :: dataList[id=1050203].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1050203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 화상 위력이 5 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1050203].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target has 5+ Burn, Coin Power +1
   PL: Jeżeli cel ma 5+ Podpalenia, Moc Monet +1
48. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1050204].levelList[level=1].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — nazwa] 태산
   źródło: Passives.json :: dataList[id=1050201].name
   limit: do 40 znaków
   EN: Great Mountain
   PL: Wielka Góra
50. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — opis] 피격 시 무작위 대상에게 화상 1 부여 (최대 4회)
   źródło: Passives.json :: dataList[id=1050201].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When attacked, inflict 1 Burn on a random enemy.\n(Up to 4 times)
   PL: Przy trafieniu nakłada 1 Podpalenia na losowego wroga. (maks. 4 razy)
51. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 마찰 타격점
   źródło: Passives.json :: dataList[id=1050221].name
   limit: do 40 znaków
   EN: Friction Point
   PL: Punkt Tarcia
52. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 속도가 가장 낮은 아군 1명 화상 부여 값 +1
   źródło: Passives.json :: dataList[id=1050221].desc
   limit: do 120 znaków
   EN: 1 ally with the slowest Speed inflicts +1 Burn.
   PL: 1 Sojusznik z najniższą Szybkością nakłada o 1 więcej Podpalenia.

## [000] W Corp. L2 Cleanup Agent — Meursault — W사 2등급 정리 요원
- ID Tożsamości: `10503` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 79 · szybkość: 4–6 / 4–7 / 4–8 / 4–8
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Charge, Rupture

53. [Karta Tożsamości — tytuł] W사 2등급\n정리 요원
   źródło: Personalities.json :: dataList[id=10503].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L2\nCleanup Agent
   PL: W Corp. L2\nAgentka Oczyszczania
54. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10503].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10503].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Karta Tożsamości — opis] 뫼르소의 세번째 인격
   źródło: Personalities.json :: dataList[id=10503].desc
   limit: do 120 znaków
   EN: Meursault’s 3rd Identity
   PL: Trzecia Tożsamość Meursaulta
57. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 절단
   źródło: Skills.json :: dataList[id=1050301].levelList[level=1].name ; dataList[id=1050301].levelList[level=2].name ; dataList[id=1050301].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Rip
   PL: Przecięcie
58. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 참격 보호 1 얻음
   źródło: Skills.json :: dataList[id=1050301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Slash Protection
   PL: [WhenUse] Zyskuje 1 Ochrony przed Cięciem
59. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 참격 보호 2 얻음
   źródło: Skills.json :: dataList[id=1050301].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Slash Protection
   PL: [WhenUse] Zyskuje 2 Ochrony przed Cięciem
60. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 3 증가
   źródło: Skills.json :: dataList[id=1050301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +3 Charge Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik Ładowania o 3
61. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 참격 보호 2 얻음\n자신의 충전 횟수 3 증가
   źródło: Skills.json :: dataList[id=1050301].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Slash Protection\nGain +3 Charge Count
   PL: [WhenUse] Zyskuje 2 Ochrony przed Cięciem\nZwiększa własny Licznik Ładowania o 3
62. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 에너지 순환
   źródło: Skills.json :: dataList[id=1050302].levelList[level=1].name ; dataList[id=1050302].levelList[level=2].name ; dataList[id=1050302].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 5 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Energy Cycle
   PL: Obieg Energii
63. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Rupture
   PL: [OnSucceedAttackHead] Nakłada 1 Rozdarcia
64. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 1 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1050302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
65. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL: [OnSucceedAttack] Nakłada 2 Rozdarcia
66. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1050302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture
   PL: [OnSucceedAttack] Nakłada 3 Rozdarcia
67. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 충전 횟수 3을 소모하여 참격 취약 2 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1050302].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 3 Charge Count to inflict 2 Slash Fragility
   PL: [OnSucceedAttack] Zużywa 3 Licznika Ładowania, aby nakładać 2 Wrażliwości na Cięcie
68. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 충전 횟수가 5 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1050302].levelList[level=4].desc
   limit: do 120 znaków
   EN: If at 5+ Charge Count, Coin Power +1
   PL: Przy 5+ Liczniku Ładowania Moc Monet +1
69. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL: [OnSucceedAttackHead] Nakłada 2 Rozdarcia
70. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1050302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
71. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 에너지 교류
   źródło: Skills.json :: dataList[id=1050303].levelList[level=3].name ; dataList[id=1050303].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Energy Current
   PL: Przepływ Energii
72. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 충전 횟수 2를 소모하여 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1050303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 2 Charge Count to inflict 2 Defense Level Down
   PL: [OnSucceedAttack] Zużywa 2 Licznika Ładowania, aby nakładać 2 Spadku Poziomu Obrony
73. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 충전 횟수 2를 소모하여 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1050303].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1050303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 충전 횟수 2를 소모하여 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1050303].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1050303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 충전 횟수 2를 소모하여 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1050303].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1050303].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 충전 횟수가 5 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1050303].levelList[level=4].desc
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1050304].levelList[level=1].name ; dataList[id=1050304].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+5)
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [Obrona (ulepszenie 4) — opis] [StartBattle] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050304].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain +2 Charge Count
   PL: [StartBattle] Zwiększa własny Licznik Ładowania o 2
79. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 견뎌내기
   źródło: Passives.json :: dataList[id=1050301].name
   limit: do 40 znaków
   EN: Enduring Spirit
   PL: Wytrwałość
80. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 피격 시 충전 횟수 1 증가 (최대 6회)
   źródło: Passives.json :: dataList[id=1050301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When attacked, gain +1 Charge Count.\n(Up to 6 times)
   PL: Przy trafieniu zyskuje +1 Licznika Ładowania. (maks. 6 razy)
81. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Envy) — nazwa] 묵묵함
   źródło: Passives.json :: dataList[id=1050321].name
   limit: do 40 znaków
   EN: Taciturn
   PL: Milczenie
82. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Envy) — opis] 속도가 가장 낮은 아군 1명 파열 부여 값 +1
   źródło: Passives.json :: dataList[id=1050321].desc
   limit: do 120 znaków
   EN: 1 ally with the slowest Speed inflicts +1 Rupture.
   PL: 1 Sojusznik z najniższą Szybkością nakłada o 1 więcej Rozdarcia.

## [000] N Corp. Großhammer — Meursault — N사 큰 망치
- ID Tożsamości: `10504` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 1 · HP bazowe: 99 · szybkość: 2–4 / 2–4 / 3–5 / 3–5
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed

83. [Karta Tożsamości — tytuł] N사\n큰 망치
   źródło: Personalities.json :: dataList[id=10504].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: N Corp.\nGroßhammer
   PL: N Corp.\nWielki Młot
84. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10504].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10504].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Karta Tożsamości — opis] 뫼르소의 네번째 인격
   źródło: Personalities.json :: dataList[id=10504].desc
   limit: do 120 znaków
   EN: Meursault’s 4th Identity
   PL: Czwarta Tożsamość Meursaulta
87. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 꿰뚫기
   źródło: Skills.json :: dataList[id=1050401].levelList[level=1].name ; dataList[id=1050401].levelList[level=2].name ; dataList[id=1050401].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 5 · monety: 2 (+1)
   limit: do 40 znaków
   EN: Drive
   PL: Pchnięcie
88. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 30%만큼 흐트러짐 회복
   źródło: Skills.json :: dataList[id=1050401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user’s Stagger Threshold by 30% of damage dealt
   PL: [OnSucceedAttack] Odzyskuje Ogłuszenie równe 30% zadanych obrażeń
89. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 30%만큼 흐트러짐 회복
   źródło: Skills.json :: dataList[id=1050401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 피해량의 60%만큼 흐트러짐 회복
   źródło: Skills.json :: dataList[id=1050401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user’s Stagger Threshold by 60% of damage dealt
   PL: [OnSucceedAttack] Odzyskuje Ogłuszenie równe 60% zadanych obrażeń
91. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 60%만큼 흐트러짐 회복
   źródło: Skills.json :: dataList[id=1050401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 4 증가\n자신의 체력이 50%미만일 때, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1050401].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +4 Aggro to this Skill Slot next turn\nAt less than 50% HP, Coin Power +2
   PL: [WhenUse] Prowokacja tego slotu Umiejętności +4 w następnej turze\nPrzy HP poniżej 50% Moc Monet +2
93. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 죄를 씻어내노라
   źródło: Skills.json :: dataList[id=1050402].levelList[level=1].name ; dataList[id=1050402].levelList[level=2].name ; dataList[id=1050402].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 6 · monety: 2 (+3)
   limit: do 40 znaków
   EN: You Are Cleansed of Sin
   PL: Zostajesz Oczyszczony z Grzechu
94. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 못 3 부여
   źródło: Skills.json :: dataList[id=1050402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Nails
   PL: [OnSucceedAttack] Nakłada 3 Gwoździ
95. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — podsumowanie] [OnSucceedAttack] 못 3 부여
   źródło: Skills.json :: dataList[id=1050402].levelList[level=1].coinlist[#0].coindescs[#0].summary ; dataList[id=1050402].levelList[level=2].coinlist[#0].coindescs[#0].summary
   (powtórzenie elementu 94 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 3 부여
   źródło: Skills.json :: dataList[id=1050402].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1050402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bind next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 3 Spętania
97. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 못이 5 이상 있으면, 다음 턴에 속박 2, 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1050402].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ Nails, inflict 2 Bind and 1 Attack Power Down next turn
   PL: [OnSucceedAttack] Jeżeli cel ma 5+ Gwoździ, nakłada w następnej turze 2 Spętania i 1 Spadku Mocy Ataku
98. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 6 증가
   źródło: Skills.json :: dataList[id=1050402].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +6 Aggro to this Skill Slot next turn
   PL: [WhenUse] Prowokacja tego slotu Umiejętności +6 w następnej turze
99. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상에게 못이 5 이상 있으면, 다음 턴에 속박 2, 공격 위력 감소 2 부여
   źródło: Skills.json :: dataList[id=1050402].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ Nails, inflict 2 Bind and 2 Attack Power Down next turn
   PL: [OnSucceedAttack] Jeżeli cel ma 5+ Gwoździ, nakłada w następnej turze 2 Spętania i 2 Spadku Mocy Ataku
100. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 이단 말살
   źródło: Skills.json :: dataList[id=1050403].levelList[level=3].name ; dataList[id=1050403].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 8 · monety: 2 (+3)
   limit: do 40 znaków
   EN: Annihilate Heretics
   PL: Zagłada Heretyków
101. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 못 2 부여
   źródło: Skills.json :: dataList[id=1050403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Nails next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 2 Gwoździ
102. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1050403].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 50% of damage dealt
   PL: [OnSucceedAttack] Odzyskuje HP równe 50% zadanych obrażeń
103. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 6 증가
   źródło: Skills.json :: dataList[id=1050403].levelList[level=4].desc
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 피해량의 50%만큼 체력 회복\n 대상의 못 1당 체력 회복량 +3%
   źródło: Skills.json :: dataList[id=1050403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 50% of damage dealt\nHP Heal +3% for each of target's Nails
   PL: [OnSucceedAttack] Odzyskuje HP równe 50% zadanych obrażeń\nOdzysk HP +3% za każde 1 Gwoździ celu
105. [Obrona (ulepszenie 1) — nazwa] 어리석도다...!
   źródło: Skills.json :: dataList[id=1050404].levelList[level=1].name
   kontekst: grzech: Wrath · typ: obrona: kontra · moc bazowa: 15 · monety: 1 (−5)
   limit: do 40 znaków
   EN: Foolishness…!
   PL: Głupota...!
106. [Obrona (ulepszenie 1) — opis] [StartBattle] 보호 1을 얻음\n체력이 50% 미만이면 최종 위력 + 2
   źródło: Skills.json :: dataList[id=1050404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 1 Protection\nAt less than 50% HP, Final Power +2
   PL: [StartBattle] Zyskuje 1 Ochrony\nPrzy HP poniżej 50% Moc Końcowa +2
107. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Wrath) — nazwa] 집념의 망치
   źródło: Passives.json :: dataList[id=1050401].name
   limit: do 40 znaków
   EN: Obsessive Hammer
   PL: Obsesyjny Młot
108. [Pasywka bojowa (od ulepszenia 2, rezonans 4× Wrath) — opis] 전투 시작 시 체력이 50% 미만이면, 자신에게 부여된 부정적인 효과 중 1개를 제거하고, 광신 1, 공격 위력 증가 1, 보호 3을 얻음
   źródło: Passives.json :: dataList[id=1050401].desc
   limit: do 180 znaków
   EN: When below 50% HP, remove 1 negative status effect and gain 1 Fanatic, 1 Attack Power Up, and 3 Protection at the start of the combat phase.
   PL: Na początku walki przy HP poniżej 50% usuwa 1 negatywny efekt i zyskuje 1 Fanatyzmu, 1 Wzrostu Mocy Ataku i 3 Ochrony
109. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 으뜸 영광
   źródło: Passives.json :: dataList[id=1050421].name
   limit: do 40 znaków
   EN: Highest Honor
   PL: Najwyższy Honor
110. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 현재 체력이 가장 낮은 아군 1명이 체력이 50% 미만이면 공격 위력 증가 1, 보호 1을 얻음. 대상이 N사 광신도면 광신 1을 추가로 얻음
   źródło: Passives.json :: dataList[id=1050421].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Apply 1 Attack Power Up and 1 Protection to the ally with the least HP below 50%.\nIf the ally is an 'N Corp. Fanatic', also apply 1 Fanatic.
   PL: 1 Sojusznik z najniższym obecnym HP, jeżeli ma poniżej 50% HP, zyskuje 1 Wzrostu Mocy Ataku i 1 Ochrony. Jeżeli tą jednostką jest Fanatyk Korp. N, zyskuje dodatkowo 1 Fanatyzmu

## [00] Rosespanner Workshop Fixer — Meursault — 장미스패너 공방 해결사
- ID Tożsamości: `10505` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 2 · HP bazowe: 76 · szybkość: 3–6 / 3–7 / 3–8 / 3–8
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Tremor, Charge

111. [Karta Tożsamości — tytuł] 장미스패너 공방\n해결사
   źródło: Personalities.json :: dataList[id=10505].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rosespanner Workshop Fixer
   PL: Warsztat Różanego Klucza\nFikser
112. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10505].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10505].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Karta Tożsamości — opis] 뫼르소의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10505].desc
   limit: do 120 znaków
   EN: Meursault’s 5th Identity
   PL: Piąta Tożsamość Meursaulta
115. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 떠맡은 업무 처리
   źródło: Skills.json :: dataList[id=1050501].levelList[level=1].name ; dataList[id=1050501].levelList[level=2].name ; dataList[id=1050501].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Saddled Tasks
   PL: Powierzone Zlecenia
116. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills.json :: dataList[id=1050501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
117. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills.json :: dataList[id=1050501].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 2 [Vibration]
   PL: [OnSucceedAttackHead] Nakłada 2 [Vibration]
118. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills.json :: dataList[id=1050501].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1050501].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 진동 횟수가 5 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1050501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 5+ [Vibration] Count, Coin Power +2
   PL: Jeżeli cel ma 5+ Licznika [Vibration], Moc Monet +2
120. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 강제 휴식
   źródło: Skills.json :: dataList[id=1050502].levelList[level=1].name ; dataList[id=1050502].levelList[level=2].name ; dataList[id=1050502].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Forced Break
   PL: Przymusowa Pauza
121. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills.json :: dataList[id=1050502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] Nakłada 3 [Vibration]
122. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 [Vibration]이 5 이상 있을 때 다음 턴에 공격 위력 감소 1 부여
   źródło: Skills.json :: dataList[id=1050502].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1050502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If target has 5+ [Vibration], inflict 1 Attack Power Down next turn
   PL: [OnSucceedAttack] Jeżeli cel ma 5+ [Vibration], nakłada w następnej turze 1 Spadku Mocy Ataku
123. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 진동 2 부여
   źródło: Skills.json :: dataList[id=1050502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills.json :: dataList[id=1050502].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1050502].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 진동 횟수가 7 이상이면, 최종 위력 +1
   źródło: Skills.json :: dataList[id=1050502].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 7+ [Vibration] Count, Final Power +1
   PL: Jeżeli cel ma 7+ Licznika [Vibration], Moc Końcowa +1
126. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 마무리 가속
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].name ; dataList[id=1050503].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Finishing Runup
   PL: Rozbieg Finishowy
127. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +1 Charge Count
   PL: [OnSucceedAttackHead] Zwiększa własny Licznik Ładowania o 1
128. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 진동 1 부여
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1050503].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1050503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +2 Charge Count
   PL: [OnSucceedAttackHead] Zwiększa własny Licznik Ładowania o 2
130. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 진동 2 부여
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1050503].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1050503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 진동 3 부여
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1050503].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]\n[VibrationExplosion] 시 진동 횟수 3 감소, 충전 횟수를 전부 소모하여 (소모한 충전 횟수 X 5)% 만큼 [VibrationExplosion]의 흐트러짐 피해량이 증가함 (최대 50%)
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1050503].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]\nWhen triggering [VibrationExplosion], reduce [Vibration] Count by 3, then spend all Charge Count to further raise Stagger Threshold by (Charge Count x 5)% (Max 50%)
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]\nPrzy wywołaniu [VibrationExplosion] zmniejsza Licznik [Vibration] o 3, po czym zużywa całe Ładowanie, dodatkowo podnosząc Próg Oszołomienia o (zużyte Ładowanie x 5)% (maks. 50%)
134. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — podsumowanie] [OnSucceedAttack] [VibrationExplosion]. 진동 횟수 3 감소. 충전 횟수를 소모하여 흐트러짐 피해량이 증가
   źródło: Skills.json :: dataList[id=1050503].levelList[level=3].coinlist[#3].coindescs[#0].summary ; dataList[id=1050503].levelList[level=4].coinlist[#3].coindescs[#0].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion], then reduce [Vibration] Count by 3; Spend Charge Count to further raise Stagger Threshold
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] o 3. Zużywa Ładowanie, aby podnieść Próg Oszołomienia
135. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 진동 횟수가 10 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1050503].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: If target has 10+ [Vibration] Count, Coin Power +1
   PL: Jeżeli cel ma 10+ Licznika [Vibration], Moc Monet +1
136. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1050504].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Gloom) — nazwa] 만성 피로
   źródło: Passives.json :: dataList[id=1050501].name
   limit: do 40 znaków
   EN: Chronic Fatigue
   PL: Przewlekłe Zmęczenie
138. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Gloom) — opis] 대상의 진동 이 5 이상이면 대상의 합 위력 -1\n흐트러짐 상태가 해제될 때 최대 체력의 5%만큼 체력 회복
   źródło: Passives.json :: dataList[id=1050501].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In a clash, the opponent has -1 Clash Power if they have 5+ Tremor.\nWhen recovering from Stagger, heal 5% of Max HP.
   PL: Przy 5+ [Vibration] celu jego Moc Starcia -1\nGdy wydobywa się z Ogłuszenia, odzyskuje 5% Maks. HP.
139. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — nazwa] 권고 휴직
   źródło: Passives.json :: dataList[id=1050521].name
   limit: do 40 znaków
   EN: Leave by Suggestion
   PL: Zwolnienie z Woli Zarządu
140. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Gloom) — opis] 속도가 가장 빠른 아군 1명이 진동 이 부여된 적과 합 진행 시 적의 합 위력 -1
   źródło: Passives.json :: dataList[id=1050521].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed lowers the Clash Power of opponents that have Tremor by 1
   PL: 1 Sojusznik z najwyższą Szybkością obniża Moc Starcia przeciwników z [Vibration] o 1

## [000] R Corp. 4th Pack Rhino — Meursault — R사 제 4무리 코뿔소팀
- ID Tożsamości: `10506` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 95 · szybkość: 2–4 / 2–4 / 3–5 / 3–5
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Charge, Bleed

141. [Karta Tożsamości — tytuł] R사 제 4무리\n코뿔소팀
   źródło: Personalities.json :: dataList[id=10506].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: R Corp. 4th Pack\nRhino
   PL: R Corp. 4 Pack\nOddział Nosorożców
142. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10506].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10506].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Karta Tożsamości — opis] 뫼르소의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10506].desc
   limit: do 120 znaków
   EN: Meursault’s 6th Identity
   PL: Szósta Tożsamość Meursaulta
145. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 육중한 충돌
   źródło: Skills.json :: dataList[id=1050601].levelList[level=1].name ; dataList[id=1050601].levelList[level=2].name ; dataList[id=1050601].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Weighty Bash
   PL: Cieżkie Walnięcie
146. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 충전 횟수가 10 이상이면, 최종 위력 + 1
   źródło: Skills.json :: dataList[id=1050601].levelList[level=1].desc
   limit: do 120 znaków
   EN: At 10+ Charge Count, Final Power +1
   PL: Przy 10+ Liczniku Ładowania Moc Końcowa +1
147. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Gain +2 Charge Count
   PL: [OnSucceedAttackHead] Zwiększa Licznik Ładowania o 2
148. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 충전 횟수가 10 이상이면, 최종 위력 + 1\n속도가 7 이상이면, 피해량 +25%
   źródło: Skills.json :: dataList[id=1050601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 10+ Charge Count, Final Power +1\nAt 7+ Speed, deal +25% Damage
   PL: Przy 10+ Liczniku Ładowania Moc Końcowa +1\nPrzy 7+ Szybkości zadaje +25% obrażeń
149. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +2 Charge Count
   PL: [OnSucceedAttack] Zwiększa Licznik Ładowania o 2
150. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 충전 횟수가 10 이상이면, 최종 위력 + 2\n속도가 7 이상이면, 피해량 +25%\n[WhenUse] 자신의 충전 횟수 2 증가
   źródło: Skills.json :: dataList[id=1050601].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: At 10+ Charge Count, Final Power +2\nAt 7+ Speed, deal +25% Damage\n[WhenUse] Gain +2 Charge Count
   PL: Przy 10+ Liczniku Ładowania Moc Końcowa +2\nPrzy 7+ Szybkości zadaje +25% obrażeń\n[WhenUse] Zwiększa własny Licznik Ładowania o 2
151. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 부수기
   źródło: Skills.json :: dataList[id=1050602].levelList[level=1].name ; dataList[id=1050602].levelList[level=2].name ; dataList[id=1050602].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Demolish
   PL: Rozwalenie
152. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 충전 횟수 4 증가
   źródło: Skills.json :: dataList[id=1050602].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +4 Charge Count
   PL: [OnSucceedAttack] Zwiększa Licznik Ładowania o 4
153. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050602].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1050602].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Bleed Count
   PL: [OnSucceedAttackHead] Zwiększa Licznik Krwawienia o 1
154. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050602].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1050602].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1050602].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Bleed Count
   PL: [OnSucceedAttack] Zwiększa Licznik Krwawienia o 1
155. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 속도가 7 이상이면, 이 스킬에서 증가시키는 출혈 횟수 +1
   źródło: Skills.json :: dataList[id=1050602].levelList[level=2].desc
   limit: do 120 znaków
   EN: At 7+ Speed, inflict +1 Bleed Count with this skill
   PL: Przy 7+ Szybkości ta Umiejętność zwiększa Licznik Krwawienia o 1 więcej
156. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 속도가 7 이상이면, 이 스킬에서 증가시키는 출혈 횟수 +1\n[WhenUse] 자신의 충전 횟수 4 증가
   źródło: Skills.json :: dataList[id=1050602].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: At 7+ Speed, inflict +1 Bleed Count with this Skill\n[WhenUse] Gain +4 Charge Count
   PL: Przy 7+ Szybkości ta Umiejętność zwiększa Licznik Krwawienia o 1 więcej\n[WhenUse] Zwiększa własny Licznik Ładowania o 4
157. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [Umiejętność 3 (×1) (ulepszenia 1,4) — nazwa] 코뿔소 돌진
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].name ; dataList[id=1050603].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 6 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Rhino Ram
   PL: Taran Nosorożca
159. [Umiejętność 3 (×1) (ulepszenie 1) — opis] [WhenUse] 충전 횟수가 10 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At 10+ Charge Count, Coin Power +1
   PL: [WhenUse] Przy 10+ Liczniku Ładowania Moc Monet +1
160. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 충전 횟수 2 소모. 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1050603].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 2 Charge Count; Inflict +1 Bleed Count
   PL: [OnSucceedAttack] Zużywa 2 Licznika Ładowania; Zwiększa Licznik Krwawienia o 1
162. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 충전 횟수 3 소모. 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=1050603].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Spend 3 Charge Count; Inflict +1 Bleed Count
   PL: [OnSucceedAttack] Zużywa 3 Licznika Ładowania; Zwiększa Licznik Krwawienia o 1
163. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1050603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 154 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 충전 횟수 2 소모. 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1050603].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Umiejętność 3 (×1) (ulepszenia 1,4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 충전 횟수 3 소모. 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1050603].levelList[level=1].coinlist[#1].coindescs[#2].desc ; dataList[id=1050603].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 충전 횟수가 10 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1050603].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At 10+ Charge Count, Coin Power +2
   PL: [WhenUse] Przy 10+ Liczniku Ładowania Moc Monet +2
167. [Obrona (ulepszenia 1,4) — nazwa] 생체 전류 감응
   źródło: Skills.json :: dataList[id=1050604].levelList[level=1].name ; dataList[id=1050604].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Bioelectricity Induction
   PL: Indukcja Bioelektryczności
168. [Obrona (ulepszenie 1) — opis] [WhenUse] 보호막이 있는동안 피격 시 충전 횟수 1 증가 (턴 당 최대 10)
   źródło: Skills.json :: dataList[id=1050604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If attacked while shielded, gain +1 Charge Count (Max 10 per turn)
   PL: [WhenUse] Przy trafieniu w posiadaniu Tarczy zyskuje +1 Licznika Ładowania (maks. 10 na turę)
169. [Obrona (ulepszenie 4) — opis] [WhenUse] 보호막이 있는동안 피격 시 충전 횟수 2 증가 (턴 당 최대 10)
   źródło: Skills.json :: dataList[id=1050604].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If attacked while shielded, gain +2 Charge Count (Max 10 per turn)
   PL: [WhenUse] Przy trafieniu w posiadaniu Tarczy zyskuje +2 Licznika Ładowania (maks. 10 na turę)
170. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — nazwa] rrR-#4 슈트 가압 가동
   źródło: Passives.json :: dataList[id=1050601].name
   limit: do 50 znaków
   EN: Activate rrR-#4 Suit Pressurization
   PL: Aktywuj Nadciśnienie Kostiumu rrR-#4
171. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Envy) — opis] 턴 종료 시 충전 횟수 5당 다음 턴의 속도 최대 값 +2 (최대 6)
   źródło: Passives.json :: dataList[id=1050601].desc
   limit: do 120 znaków
   EN: At the end of the turn, Max Speed +2 (Capped at 6) per 5 Charge Count next turn.
   PL: Na koniec tury Maks. Szybkość +2 (maks. 6) w następnej turze za każde 5 Licznika Ładowania.
172. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — nazwa] 기동 훈련
   źródło: Passives.json :: dataList[id=1050621].name
   limit: do 40 znaków
   EN: Maneuver Training
   PL: Trening Manewrowy
173. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Envy) — opis] 턴 종료 시 충전 횟수가 가장 높은 아군 1명이 충전 횟수 5당 다음 턴의 속도 최대 값 +1 (최대 3)
   źródło: Passives.json :: dataList[id=1050621].desc
   limit: do 170 znaków
   EN: At the end of the turn, 1 ally that has the highest Charge Count gains Max Speed +1 (Capped at 3) per 5 Charge Count next turn
   PL: Na koniec tury 1 Sojusznik z najwyższym Licznikiem Ładowania zyskuje Maks. Szybkość +1 (maks. 3) w następnej turze za każde 5 Licznika Ładowania

## [00] The Middle Little Brother — Meursault — 중지 작은 아우
- ID Tożsamości: `10507` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 3 · HP bazowe: 82 · szybkość: 3–5 / 4–5 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Bleed

174. [Karta Tożsamości — tytuł] 중지\n작은 아우
   źródło: Personalities.json :: dataList[id=10507].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Middle\nLittle Brother
   PL: Środkowego\nMłodszy Brat
175. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10507].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10507].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Karta Tożsamości — opis] 뫼르소의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10507].desc
   limit: do 120 znaków
   EN: Meursault’s 7th Identity
   PL: Siódma Tożsamość Meursaulta
178. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 기억한다
   źródło: Skills_personality-05.json :: dataList[id=1050701].levelList[level=1].name ; dataList[id=1050701].levelList[level=2].name ; dataList[id=1050701].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: We Remember
   PL: Pamiętamy
179. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL: [OnSucceedAttackHead] Nakłada 1 Krwawienia
180. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] [DefeatDuel] 다음 턴에 질투 피해량 증가 1 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050701].levelList[level=2].desc ; dataList[id=1050701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Gain 1 Envy DMG Up next turn
   PL: [DefeatDuel] Zyskuje w następnej turze 1 Wzrostu Obrażeń Zazdrości
182. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050701].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL: [OnSucceedAttack] Nakłada 1 Krwawienia
183. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050701].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 의리 사슬
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=1].name ; dataList[id=1050702].levelList[level=2].name ; dataList[id=1050702].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Chains of Loyalty
   PL: Łańcuch Wierności
185. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [StartBattle] 조작 패널에서 자신의 양 옆의 아군에게 질투 위력 증가 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=1].desc ; dataList[id=1050702].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Apply 1 Envy Power Up to 2 allies adjacent to this unit on the Dashboard.
   PL: [StartBattle] Nakłada 1 Wzrostu Mocy Zazdrości na 2 sojuszników sąsiadujących z tą jednostką w Panelu Sterowania.
186. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [StartBattle] 조작 패널에서 자신의 양 옆의 아군에게 질투 위력 증가 1 부여\n해당 슬롯에서 선택한 스킬이 질투 속성이면 추가로 질투 피해량 증가 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050702].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Apply 1 Envy Power Up to 2 allies adjacent to this unit on the Dashboard\nApply 1 Envy DMG Up as well when selecting Envy affinity Skills from the affected Skill Slots
   PL: [StartBattle] Nakłada 1 Wzrostu Mocy Zazdrości na 2 sojuszników sąsiadujących z tą jednostką w Panelu Sterowania\nDodatkowo nakłada 1 Wzrostu Obrażeń Zazdrości przy wyborze Umiejętności Zazdrości z dotkniętych slotów Umiejętności
191. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 새긴다
   źródło: Skills_personality-05.json :: dataList[id=1050703].levelList[level=3].name ; dataList[id=1050703].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Recording
   PL: Zapisuje
192. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 질투 공명이 4 이상이면 코인 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1050703].levelList[level=3].desc
   limit: do 120 znaków
   EN: At 4+ Envy Reson., Coin Power +1
   PL: Przy 4+ Rezonansie Zazdrości Moc Monet +1
193. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 앙갚음 대상 이면, 다음 턴에 더하기 코인 약화 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Vengeance Mark, inflict 1 Plus Coin Drop next turn
   PL: [OnSucceedAttack] Jeżeli cel jest Cel Odwetu, nakłada w następnej turze 1 Osłabienia Monet Plus
194. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상이 앙갚음 대상 이면, 다음 턴에 질투 취약 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050703].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Vengeance Mark, inflict 1 Envy Fragility next turn
   PL: [OnSucceedAttack] Jeżeli cel jest Cel Odwetu, nakłada w następnej turze 1 Wrażliwości na Zazdrość
195. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 질투 공명이 4 이상이면 코인 위력 +1\n질투 완전 공명이 6 이상이면 코인 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1050703].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 4+ Envy Reson., Coin Power +1\nAt 6+ Envy A-Reson., Coin Power +1
   PL: Przy 4+ Rezonansie Zazdrości Moc Monet +1\nPrzy 6+ Pełnym Rezonansie Zazdrości Moc Monet +1
196. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상이 앙갚음 대상 이면, 다음 턴에 질투 취약 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Vengeance Mark, inflict 2 Envy Fragility next turn
   PL: [OnSucceedAttack] Jeżeli cel jest Cel Odwetu, nakłada w następnej turze 2 Wrażliwości na Zazdrość
197. [Obrona (ulepszenia 1,4) — nazwa] 배로 갚기
   źródło: Skills_personality-05.json :: dataList[id=1050704].levelList[level=1].name ; dataList[id=1050704].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Multifold Retribution
   PL: Wielokrotna Zemsta
198. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Obrona (ulepszenie 4) — opis] 질투 공명이 4 이상이면 코인 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1050704].levelList[level=4].desc
   (powtórzenie elementu 192 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050704].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050704].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 의리
   źródło: Passives.json :: dataList[id=1050701].name
   limit: do 40 znaków
   EN: Loyalty
   PL: Braterstwo
204. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] - 턴 종료 시 해당 턴에 아군에게 스킬로 가장 많이 피해를 준 적 1명에게 <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">앙갚음 대상</color></link></u>을 부여.\n- 공격 시 메인 공격 대상이 앙갚음 대상 인 경우 최종 위력 1 증가\n- 자신 이외의 중지 인격이 생존해있으면, 매 턴 종료 시 정신력 6 회복
   źródło: Passives.json :: dataList[id=1050701].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <sprite name="RetaliationBook">, <color=#e30000>, <u>, <link="RetaliationBook">, </color>, </link>, </u>, \n
   EN: - Apply <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">Vengeance Mark</color></link></u> to the unit that dealt the most Skill damage to an ally.\n- If the main target has Vengeance Mark, Final Power +1\n- If there is another surviving ally from the Middle, heal 6 SP at every Turn End
   PL: - Na koniec tury nakłada <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">Cel Odwetu</link></u></color> na wroga, który w tej turze zadał sojusznikom najwięcej obrażeń Umiejętnościami.\n- Przy ataku, gdy głównym celem ataku jest Cel Odwetu, Moc Końcowa +1\n- Jeżeli przeżywa inna Tożsamość Środkowego, odzyskuje 6 Poczytalności na koniec każdej tury
205. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — nazwa] 의리
   źródło: Passives.json :: dataList[id=1050711].name
   (powtórzenie elementu 203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — opis] - 턴 종료 시 해당 턴에 아군에게 스킬로 가장 많이 피해를 준 적 1명에게 <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">앙갚음 대상</color></link></u>을 부여.\n- 공격 시 메인 공격 대상이 앙갚음 대상 인 경우 최종 위력 1 증가\n- 자신 이외의 중지 인격이 생존해있으면, 매 턴 종료 시 자신과 정신력이 가장 낮은 중지 인격 1명의 매 턴 종료 시 정신력 6 회복
   źródło: Passives.json :: dataList[id=1050711].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <sprite name="RetaliationBook">, <color=#e30000>, <u>, <link="RetaliationBook">, </color>, </link>, </u>, \n
   EN: - Apply <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">Vengeance Mark</color></link></u> to the unit that dealt the most Skill damage to an ally.\n- If the main target has Vengeance Mark, Final Power +1\n- If there is another surviving ally from the Middle other than this unit, this unit and the surviving ally from the Middle with the least SP both heal 6 SP at every Turn End
   PL: - Na koniec tury nakłada <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">Cel Odwetu</link></u></color> na wroga, który w tej turze zadał sojusznikom najwięcej obrażeń Umiejętnościami.\n- Przy ataku, gdy głównym celem ataku jest Cel Odwetu, Moc Końcowa +1\n- Jeżeli przeżywa inna Tożsamość Środkowego, ta jednostka i przeżywająca Tożsamość Środkowego z najniższą Poczytalnością odzyskują 6 Poczytalności na koniec każdej tury
207. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — nazwa] 한 식구
   źródło: Passives.json :: dataList[id=1050721].name
   limit: do 40 znaków
   EN: One Family
   PL: Jedna Rodzina
208. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — opis] 정신력이 가장 낮은 아군 1명이 자신과 동일한 소속의 캐릭터가 생존해있는 경우, 턴 종료 시 정신력 10 회복
   źródło: Passives.json :: dataList[id=1050721].desc
   limit: do 130 znaków
   EN: The 1 ally with the least SP heals 10 SP at Turn End if there is another ally from the same Faction
   PL: 1 Sojusznik z najniższą Poczytalnością odzyskuje na koniec tury 10 Poczyt., jeżeli przeżywa ktoś z tej samej frakcji

## [000] Blade Lineage Mentor — Meursault — 검계 우두머리
- ID Tożsamości: `10508` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 3 · HP bazowe: 82 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Poise

209. [Karta Tożsamości — tytuł] 검계\n우두머리
   źródło: Personalities.json :: dataList[id=10508].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Blade Lineage\nMentor
   PL: Ród Ostrza\nMentor
210. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10508].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10508].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Karta Tożsamości — opis] 뫼르소의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10508].desc
   limit: do 120 znaków
   EN: Meursault’s 8th Identity
   PL: Ósma Tożsamość Meursaulta
213. [Umiejętność 1 (×3) (ulepszenia 1–4) — nazwa] 발검
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=1].name ; dataList[id=1050801].levelList[level=2].name ; dataList[id=1050801].levelList[level=3].name ; dataList[id=1050801].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Draw of the Sword
   PL: Dobycie Ostrza
214. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2
215. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 1 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath]
   PL: [OnSucceedAttackHead] Zyskuje 1 [Breath]
216. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 1 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[StartBattle] 자신을 제외한 검계 조직원 (최대 완전 공명 수)명에게 속도가 느린 순으로 [BladeResultUpTier1] 1 부여 (최대 2회)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [BladeResultUpTier1], [WhenUse], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BladeResultUpTier1] = 본국검 - 세법 전수 / Sword of the Homeland - Rending; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: <style="highlight">[StartBattle] Apply 1 [BladeResultUpTier1] to (highest A-Reson.) other Blade Lineage allies in ascending order of Speeds (slowest to fastest, 2 times max)\n</style>[WhenUse] Gain +2 [Breath] Count
   PL: <style="highlight">[StartBattle] Nakłada 1 [BladeResultUpTier1] na (najwyższy Pełny Rezonans / N) innych Tożsamości Rodu Ostrza w kolejności od najniższej Szybkości (maks. 2 razy)</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
218. [Umiejętność 1 (×3) (ulepszenia 2–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050801].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050801].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL: [OnSucceedAttack] Zyskuje 1 [Breath]
219. [Umiejętność 1 (×3) (ulepszenia 2–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050801].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1050801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność 1 (×3) (ulepszenie 3) — opis] [StartBattle_Force] <color=#EBCAA2>자신을 제외한 검계 조직원 (최대 완전 공명 수)명에게 속도가 느린 순으로 [BladeResultUpTier1] 1 부여 (최대 2회)</color>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=3].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#EBCAA2>, </color>, \n, [StartBattle_Force], [BladeResultUpTier1], [WhenUse], [Breath]
   znaczenie tagów: [StartBattle_Force] = [전투 시작시] / [Combat Start]; [BladeResultUpTier1] = 본국검 - 세법 전수 / Sword of the Homeland - Rending; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [StartBattle_Force] <color=#EBCAA2>Apply 1 [BladeResultUpTier1] to (highest A-Reson.) other Blade Lineage allies in ascending order of Speeds (slowest to fastest, 2 times max)</color>\n[WhenUse] Gain +2 [Breath] Count
   PL: [StartBattle_Force] <color=#EBCAA2>Nakłada 1 [BladeResultUpTier1] na (najwyższy Pełny Rezonans / N) innych Tożsamości Rodu Ostrza w kolejności od najniższej Szybkości (maks. 2 razy)</color>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
221. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 5 이상이면 코인 위력 +1</style>\n[StartBattle] 자신을 제외한 검계 조직원 (최대 완전 공명 수)명에게 속도가 느린 순으로 [BladeResultUpTier1] 1 부여 (최대 2회)\n<style="highlight">- 검계 조직원이 6명 이상 전투에 참여했으면, 대신 2 부여</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1050801].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [StartBattle], [BladeResultUpTier1], [WhenUse]
   znaczenie tagów: [Breath] = 호흡 / Poise; [StartBattle] = [전투 시작시] / [Combat Start]; [BladeResultUpTier1] = 본국검 - 세법 전수 / Sword of the Homeland - Rending; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">At 5+ [Breath], Coin Power +1</style>\n[StartBattle] Apply 1 [BladeResultUpTier1] to (highest A-Reson.) other Blade Lineage allies in ascending order of Speeds (slowest to fastest, 2 times max)\n<style="highlight">- If there are 6 or more allied Blade Lineage Identities in the Encounter, apply 2 instead</style>\n[WhenUse] Gain +2 [Breath] Count
   PL: <style="highlight">Przy 5+ [Breath] Moc Monet +1</style>\n[StartBattle] Nakłada 1 [BladeResultUpTier1] na (najwyższy Pełny Rezonans / N) innych Tożsamości Rodu Ostrza w kolejności od najniższej Szybkości (maks. 2 razy)\n<style="highlight">- Jeżeli w spotkaniu uczestniczy 6 lub więcej Tożsamości Rodu Ostrza, zamiast tego nakłada 2</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
222. [Umiejętność 2 (×2) (ulepszenia 1–4) — nazwa] 자법
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=1].name ; dataList[id=1050802].levelList[level=2].name ; dataList[id=1050802].levelList[level=3].name ; dataList[id=1050802].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 3 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Acupuncture
   PL: Akupunktura
223. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가\n[WinDuel] 다음 턴에 참격 위력 증가 1을 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Gain +2 [Breath] Count\n[WinDuel] Gain 1 Slash Power Up next turn
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2\n[WinDuel] Zyskuje w następnej turze 1 Wzrostu Mocy Cięcia
224. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Breath] 3 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 3 [Breath]
   PL: [OnSucceedAttackHead] Zyskuje 3 [Breath]
225. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: +30% Damage on Critical Hit
   PL: Zadaje +30% obrażeń przy trafieniu krytycznym
226. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[StartBattle] 자신을 제외한 검계 조직원 (최대 완전 공명 수)명에게 속도가 느린 순으로 [BladeResultUpTier2] 1 부여 (최대 2회)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[WinDuel] 다음 턴에 참격 위력 증가 1을 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=2].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [BladeResultUpTier2], [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BladeResultUpTier2] = 본국검 - 자법 전수 / Sword of the Homeland - Penetrating; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">[StartBattle] Apply 1 [BladeResultUpTier2] to (highest A-Reson.) other Blade Lineage allies in ascending order of Speeds (slowest to fastest, 2 times max)</style>\n[WhenUse] Gain +2 [Breath] Count\n[WinDuel] Gain 1 Slash Power Up next turn
   PL: <style="highlight">[StartBattle] Nakłada 1 [BladeResultUpTier2] na (najwyższy Pełny Rezonans / N) innych Tożsamości Rodu Ostrza w kolejności od najniższej Szybkości (maks. 2 razy)</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2\n[WinDuel] Zyskuje w następnej turze 1 Wzrostu Mocy Cięcia
227. [Umiejętność 2 (×2) (ulepszenia 2–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050802].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1050802].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL: [OnSucceedAttack] Zyskuje 3 [Breath]
228. [Umiejętność 2 (×2) (ulepszenia 2–3) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +40%
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1050802].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: +40% Damage on Critical Hit
   PL: +40% obrażeń przy trafieniu krytycznym
229. [Umiejętność 2 (×2) (ulepszenie 3) — opis] [StartBattle_Force] <color=#EBCAA2>자신을 제외한 검계 조직원 (최대 완전 공명 수)명에게 속도가 느린 순으로 [BladeResultUpTier2] 1 부여 (최대 2회)</color>\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[WinDuel] 다음 턴에 참격 위력 증가 1을 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=3].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <color=#EBCAA2>, </color>, \n, [StartBattle_Force], [BladeResultUpTier2], [WhenUse], [Breath], [WinDuel]
   znaczenie tagów: [StartBattle_Force] = [전투 시작시] / [Combat Start]; [BladeResultUpTier2] = 본국검 - 자법 전수 / Sword of the Homeland - Penetrating; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [StartBattle_Force] <color=#EBCAA2>Apply 1 [BladeResultUpTier2] to (highest A-Reson.) other Blade Lineage allies in ascending order of Speeds (slowest to fastest, 2 times max)</color>\n[WhenUse] Gain +2 [Breath] Count\n[WinDuel] Gain 1 Slash Power Up next turn
   PL: [StartBattle_Force] <color=#EBCAA2>Nakłada 1 [BladeResultUpTier2] na (najwyższy Pełny Rezonans / N) innych Tożsamości Rodu Ostrza w kolejności od najniższej Szybkości (maks. 2 razy)</color>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2\n[WinDuel] Zyskuje w następnej turze 1 Wzrostu Mocy Cięcia
230. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">자신의 [Breath]이 7 이상이면 코인 위력 +1</style>\n[StartBattle] 자신을 제외한 검계 조직원 (최대 완전 공명 수)명에게 속도가 느린 순으로 [BladeResultUpTier2] 1 부여 (최대 2회)\n<style="highlight">- 검계 조직원이 6명 이상 전투에 참여했으면, 대신 2 부여</style>\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n[WinDuel] 다음 턴에 참격 위력 증가 1을 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=4].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [StartBattle], [BladeResultUpTier2], [WhenUse], [WinDuel]
   znaczenie tagów: [Breath] = 호흡 / Poise; [StartBattle] = [전투 시작시] / [Combat Start]; [BladeResultUpTier2] = 본국검 - 자법 전수 / Sword of the Homeland - Penetrating; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">At 7+ [Breath], Coin Power +1</style>\n[StartBattle] Apply 1 [BladeResultUpTier2] to (highest A-Reson.) other Blade Lineage allies in ascending order of Speeds (slowest to fastest, 2 times max)\n<style="highlight">- If there are 6 or more allied Blade Lineage Identities in the Encounter, apply 2 instead</style>\n[WhenUse] Gain +3 [Breath] Count\n[WinDuel] Gain 1 Slash Power Up next turn
   PL: <style="highlight">Przy 7+ [Breath] Moc Monet +1</style>\n[StartBattle] Nakłada 1 [BladeResultUpTier2] na (najwyższy Pełny Rezonans / N) innych Tożsamości Rodu Ostrza w kolejności od najniższej Szybkości (maks. 2 razy)\n<style="highlight">- Jeżeli w spotkaniu uczestniczy 6 lub więcej Tożsamości Rodu Ostrza, zamiast tego nakłada 2</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 3\n[WinDuel] Zyskuje w następnej turze 1 Wzrostu Mocy Cięcia
231. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +60%
   źródło: Skills_personality-05.json :: dataList[id=1050802].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: +60% Damage on Critical Hit
   PL: +60% obrażeń przy trafieniu krytycznym
232. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 육참
   źródło: Skills_personality-05.json :: dataList[id=1050803].levelList[level=3].name ; dataList[id=1050803].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 20 · monety: 1 (−8)
   limit: do 40 znaków
   EN: Yield My Flesh
   PL: Oddam Ciało
233. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 3 얻음\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WinDuel] [Breath] 5 얻음\n[DefeatDuel] 피격 후 골단 스킬 사용\n[CriticalActivated] 호흡 위력 1당 크리티컬 피해량 +2% (최대 50%)\n크리티컬 피해량 +15%\n 잃은 체력 1%당 피해량 0.5% 증가 (최대 25%)
   źródło: Skills_personality-05.json :: dataList[id=1050803].levelList[level=3].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WinDuel], [Breath], [DefeatDuel], [CriticalActivated]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]; [CriticalActivated] = [크리티컬 발동 시] / [On Crit]
   EN: [WhenUse] Gain +3 Aggro to this Skill Slot next turn\n[WhenUse] Until this Skill ends, this unit cannot be Staggered from taking damage\n[WinDuel] Gain 5 [Breath]\n[DefeatDuel] After getting hit, use 'To Claim Their Bones' Skill\n[CriticalActivated] Deal +2% damage on Critical Hit for every Poise Potency on self (Max 50%)\n+15% Damage on Critical Hit\nDeal +0.5% damage per 1% missing HP on self (Max 25%)
   PL: [WhenUse] Prowokacja tego slotu +3 w następnej turze\n[WhenUse] Do końca działania tej Umiejętności nie może zostać Ogłuszona przez obrażenia\n[WinDuel] Zyskuje 5 [Breath]\n[DefeatDuel] Po otrzymaniu trafienia używa Umiejętności „Łamanie Kości”\n[CriticalActivated] Zadaje +2% obrażeń przy trafieniu krytycznym za każde 1 Mocy Oddechu (maks. 50%)\n+15% obrażeń przy trafieniu krytycznym\nZadaje +0.5% obrażeń za każde 1% brakującego HP (maks. 25%)
234. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 슬롯이 도발치 3 얻음\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WinDuel] [Breath] 5 얻음\n[DefeatDuel] 피격 후 골단 스킬 사용\n[CriticalActivated] 호흡 위력 1당 크리티컬 피해량 +3% (최대 75%)\n크리티컬 피해량 +30%\n 잃은 체력 1%당 피해량 0.5% 증가 (최대 25%)
   źródło: Skills_personality-05.json :: dataList[id=1050803].levelList[level=4].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [WinDuel], [Breath], [DefeatDuel], [CriticalActivated]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]; [CriticalActivated] = [크리티컬 발동 시] / [On Crit]
   EN: [WhenUse] Gain +3 Aggro to this Skill Slot next turn\n[WhenUse] Until this Skill ends, this unit cannot be Staggered from taking damage\n[WinDuel] Gain 5 [Breath]\n[DefeatDuel] After getting hit, use 'To Claim Their Bones' Skill\n[CriticalActivated] Deal +3% damage on Critical Hit for every Poise Potency on self (Max 75%)\n+30% Damage on Critical Hit\nDeal +0.5% damage per 1% missing HP on self (Max 25%)
   PL: [WhenUse] Prowokacja tego slotu +3 w następnej turze\n[WhenUse] Do końca działania tej Umiejętności nie może zostać Ogłuszona przez obrażenia\n[WinDuel] Zyskuje 5 [Breath]\n[DefeatDuel] Po otrzymaniu trafienia używa Umiejętności „Łamanie Kości”\n[CriticalActivated] Zadaje +3% obrażeń przy trafieniu krytycznym za każde 1 Mocy Oddechu (maks. 75%)\n+30% obrażeń przy trafieniu krytycznym\nZadaje +0.5% obrażeń za każde 1% brakującego HP (maks. 25%)
235. [Obrona (ulepszenia 1,4) — nazwa] 살주
   źródło: Skills_personality-05.json :: dataList[id=1050804].levelList[level=1].name ; dataList[id=1050804].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: kontra · moc bazowa: 8 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Overthrow
   PL: Obalenie
236. [Obrona (ulepszenie 1) — opis] [WhenUse] 다음 턴에 참격 위력 증가 1을 얻음 (최대 1회)
   źródło: Skills_personality-05.json :: dataList[id=1050804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Slash Power Up next turn (1 time max)
   PL: [WhenUse] Zyskuje w następnej turze 1 Wzrostu Mocy Cięcia (maks. 1 raz)
237. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-05.json :: dataList[id=1050804].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050804].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL: [OnSucceedAttack] Zyskuje 2 [Breath]
238. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 참격 위력 증가 1을 얻음 (최대 1회)\n<style="highlight">잃은 체력 1% 당 피해량 0.5% 증가 (최대 25%)</style>
   źródło: Skills_personality-05.json :: dataList[id=1050804].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Slash Power Up next turn (1 time max)\n<style="highlight">Deal +0.5% damage for every 1% missing HP on self (Max 25%)</style>
   PL: [WhenUse] Zyskuje w następnej turze 1 Wzrostu Mocy Cięcia (maks. 1 raz)\n<style="highlight">Zadaje +0.5% obrażeń za każde 1% brakującego HP (maks. 25%)</style>
239. [Obrona (ulepszenia 1,4) — nazwa] 골단
   źródło: Skills_personality-05.json :: dataList[id=1050805].levelList[level=1].name ; dataList[id=1050805].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 4 · monety: 4 (+4)
   limit: do 40 znaków
   EN: To Claim Their Bones
   PL: Łamanie Kości
240. [Obrona (ulepszenie 1) — opis] [BeforeAttack] 자신의 [Breath]이 10 이상이면 공격 가중치 +1\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WhenUse] 호흡 위력 1당  크리티컬 피해량 + 2% (최대 50%)\n크리티컬 피해량 +20%\n자신의 잃은 체력 1%당 피해량 0.5% 증가 (최대 25%)
   źródło: Skills_personality-05.json :: dataList[id=1050805].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeAttack], [Breath], [WhenUse]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: [BeforeAttack] At 10+ [Breath], Atk Weight +1\n[WhenUse] Until this Skill ends, this unit cannot be Staggered from taking damage\n[WhenUse] Deal +2% damage on Critical Hit for every Poise Potency on self (Max 50%)\n+20% Damage on Critical Hit\nDeal +0.5% damage per 1% missing HP on self (Max 25%)
   PL: [BeforeAttack] Przy 10+ [Breath] Waga ataku +1\n[WhenUse] Do końca działania tej Umiejętności nie może zostać Ogłuszona przez obrażenia\n[WhenUse] Zadaje +2% obrażeń przy trafieniu krytycznym za każde 1 Mocy Oddechu (maks. 50%)\n+20% obrażeń przy trafieniu krytycznym\nZadaje +0.5% obrażeń za każde 1% własnego brakującego HP (maks. 25%)
241. [Obrona (ulepszenia 1,4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills_personality-05.json :: dataList[id=1050805].levelList[level=1].coinlist[#3].coindescs[#0].desc ; dataList[id=1050805].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL: [OnSucceedAttack] Nakłada 3 Krwawienia
242. [Obrona (ulepszenia 1,4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 마비 5 부여
   źródło: Skills_personality-05.json :: dataList[id=1050805].levelList[level=1].coinlist[#3].coindescs[#1].desc ; dataList[id=1050805].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Paralyze next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 5 Paraliżu
243. [Obrona (ulepszenie 4) — opis] <style="highlight">[BeforeAttack] 자신의 [Breath] 7당 공격 가중치 +1 (최대 2)</style>\n[WhenUse] 이 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않음\n[WhenUse] 호흡 위력 1당  크리티컬 피해량 + 2% (최대 50%)\n크리티컬 피해량 +<style="highlight">30</style>%\n자신의 잃은 체력 1%당 피해량 0.5% 증가 (최대 25%)\n<style="highlight">타겟이 1명이면, 피해량 +100% (집중 전투에서는 부위로 판정)</style>
   źródło: Skills_personality-05.json :: dataList[id=1050805].levelList[level=4].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeAttack], [Breath], [WhenUse]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [Breath] = 호흡 / Poise; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">[BeforeAttack] For every 7 [Breath] on self, Atk Weight +1 (Max +2)</style>\n[WhenUse] Until this Skill ends, this unit cannot be Staggered from taking damage\n[WhenUse] Deal +2% damage on Critical Hit for every Poise Potency on self (Max 50%)\n+<style="highlight">30</style>% Damage on Critical Hit\nDeal +0.5% damage for every 1% missing HP on self (Max 25%)\n<style="highlight">If this Skill targets only a single enemy, deal +100% damage (In Focused Encounters, a single Part)</style>
   PL: <style="highlight">[BeforeAttack] Waga ataku +1 za każde 7 [Breath] (maks. 2)</style>\n[WhenUse] Do końca działania tej Umiejętności nie może zostać Ogłuszona przez obrażenia\n[WhenUse] Zadaje +2% obrażeń przy trafieniu krytycznym za każde 1 Mocy Oddechu (maks. 50%)\n+<style="highlight">30</style>% obrażeń przy trafieniu krytycznym\nZadaje +0.5% obrażeń za każde 1% własnego brakującego HP (maks. 25%)\n<style="highlight">Jeżeli ta Umiejętność namierza tylko 1 wroga, zadaje +100% obrażeń (w walce skupionej: pojedynczą część ciała)</style>
244. [Pasywka bojowa (od ulepszenia 1) — nazwa] 추모
   źródło: Passives.json :: dataList[id=1050802].name
   limit: do 40 znaków
   EN: In Memoriam
   PL: Pamięć
245. [Pasywka bojowa (od ulepszenia 1) — opis] 자신을 제외한 검계 조직원이 3명 이상 사망한 경우\n- 자신의 스킬, 코인 효과로 호흡 위력, 횟수를 얻을 때, 호흡 위력, 횟수 1 추가 증가\n- 검계 조직원이 5명 이상 사망한 경우, 대신 2 증가\n- 전투 시작 시 자신에게 [SwordPlayOfTheHomeland] 부여
   źródło: Passives.json :: dataList[id=1050802].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [SwordPlayOfTheHomeland]
   znaczenie tagów: [SwordPlayOfTheHomeland] = 본국검술 / Swordplay of the Homeland
   EN: When 3 or more other Blade Lineage allies are defeated:\n- When gaining Poise Potency/Count using this unit's own Skills and Coin effects: Gain 1 more of each\n- When 5 or more other Blade Lineage allies are defeated, gain 2 more of each instead\n- Combat Start: Apply [SwordPlayOfTheHomeland] on self
   PL: Gdy 3 lub więcej innych Tożsamości Rodu Ostrza ginie:\n- Zyskując Moc i Licznik Oddechu efektami własnych Umiejętności i monet, zyskuje o 1 więcej jednego i drugiego\n- Gdy ginie 5 lub więcej innych Tożsamości Rodu Ostrza, zamiast tego zyskuje o 2 więcej jednego i drugiego\n- Na początku walki nakłada [SwordPlayOfTheHomeland] na siebie
246. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — nazwa] 본국검술
   źródło: Passives.json :: dataList[id=1050801].name
   limit: do 40 znaków
   EN: Swordplay of the Homeland
   PL: Szermierka Ojczyzny
247. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — opis] 이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고, 해당 턴 동안 체력이 1로 유지됨. (전투 당 1회)\n\n자신의 스킬, 코인 효과로 [Breath] 위력, 횟수를 얻을 때, 자신을 제외한 [Breath]이 없거나, 가장 낮은 검계 인격 2명의 [Breath] 위력, 횟수 1 증가\n- 전투에 참여한 검계 조직원이 6명 이상이면, 대신 2 증가
   źródło: Passives.json :: dataList[id=1050801].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: In this Encounter, when this unit takes damage that brings their HP down to 0, nullify that damage; then, this unit's HP cannot drop below 1 for the turn (once per Encounter)\n\nWhen this unit gains [Breath] Potency/Count using its own Skill or Coin effects: Give 1 [Breath] Potency and +1 [Breath] Count to 2 other Blade Lineage allies that have no [Breath] or have the least [Breath]\n- If there are 6 or more Blade Lineage allies participating in this Encounter, give 2 [Breath] Potency and +2 [Breath] Count instead
   PL: W tym spotkaniu, gdy ta jednostka otrzymuje obrażenia redukujące HP do 0, unieważnia te obrażenia; jej HP nie spada poniżej 1 w tej turze (1 raz na spotkanie)\n\nZyskując [Breath] Moc i Licznik efektami własnych Umiejętności lub monet, daje 1 [Breath] Mocy i +1 [Breath] Licznika 2 innym Tożsamościom Rodu Ostrza bez [Breath] lub z najniższym [Breath]\n- Jeżeli w tym spotkaniu uczestniczy 6 lub więcej Tożsamości Rodu Ostrza, zamiast tego daje 2 [Breath] Mocy i +2 [Breath] Licznika
248. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Pride) — nazwa] 본국검술
   źródło: Passives.json :: dataList[id=1050811].name
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Pride) — opis] 이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고, 해당 턴 동안 체력이 1로 유지됨. (전투 당 1회)\n\n자신의 스킬, 코인 효과로 [Breath] 위력, 횟수를 얻을 때, 자신을 제외한 [Breath]이 없거나, 가장 낮은 검계 인격 2명의 [Breath] 위력, 횟수 1 증가\n- 전투에 참여한 검계 조직원이 6명 이상이면, 대신 2 증가\n\n<style="highlight">전투 시작 시 자신을 제외한 검계 조직원에게 [SwordPlayOfTheHomeland] 부여</style>
   źródło: Passives.json :: dataList[id=1050811].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [SwordPlayOfTheHomeland]
   znaczenie tagów: [Breath] = 호흡 / Poise; [SwordPlayOfTheHomeland] = 본국검술 / Swordplay of the Homeland
   EN: In this Encounter, when this unit takes damage that brings their HP down to 0, nullify that damage; then, this unit's HP cannot drop below 1 for the turn (once per Encounter)\n\nWhen this unit gains [Breath] Potency/Count using its own Skill or Coin effects: Give 1 [Breath] Potency and +1 [Breath] Count to 2 other Blade Lineage allies that have no [Breath] or have the least [Breath]\n- If there are 6 or more Blade Lineage allies participating in this Encounter, give 2 [Breath] Potency and +2 [Breath] Count instead\n\n<style="highlight">Combat Start: Apply [SwordPlayOfTheHomeland] buff to all other Blade Lineage allies</style>
   PL: W tym spotkaniu, gdy ta jednostka otrzymuje obrażenia redukujące HP do 0, unieważnia te obrażenia; jej HP nie spada poniżej 1 w tej turze (1 raz na spotkanie)\n\nZyskując [Breath] Moc i Licznik efektami własnych Umiejętności lub monet, daje 1 [Breath] Mocy i +1 [Breath] Licznika 2 innym Tożsamościom Rodu Ostrza bez [Breath] lub z najniższym [Breath]\n- Jeżeli w tym spotkaniu uczestniczy 6 lub więcej Tożsamości Rodu Ostrza, zamiast tego daje 2 [Breath] Mocy i +2 [Breath] Licznika\n\n<style="highlight">Na początku walki nakłada buff [SwordPlayOfTheHomeland] na wszystkie inne Tożsamości Rodu Ostrza</style>
250. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — nazwa] 본국검술
   źródło: Passives.json :: dataList[id=1050821].name
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — opis] 전투 시작 시 [Breath]을 가장 많이 보유한 아군 1명의 참격 속성 스킬의 크리티컬 피해량 +15%
   źródło: Passives.json :: dataList[id=1050821].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Combat Start: 1 ally that has the most [Breath] deals +15% damage on Critical Hit using Slash Skills
   PL: Na początku walki 1 Sojusznik z największą liczbą [Breath] zadaje +15% obrażeń przy trafieniu krytycznym Umiejętnościami Cięcia

## [00] Dead Rabbits Boss — Meursault — 데드레빗츠 보스
- ID Tożsamości: `10509` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 4 · HP bazowe: 76 · szybkość: 3–6 / 4–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Rupture

252. [Karta Tożsamości — tytuł] 데드레빗츠\n보스
   źródło: Personalities.json :: dataList[id=10509].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Dead Rabbits\nBoss
   PL: Martwe Króliki\nSzef
253. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10509].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10509].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Karta Tożsamości — opis] 뫼르소의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10509].desc
   limit: do 120 znaków
   EN: Meursault’s 9th Identity
   PL: Dziewiąta Tożsamość Meursaulta
256. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 배트치기
   źródło: Skills_personality-05.json :: dataList[id=1050901].levelList[level=1].name ; dataList[id=1050901].levelList[level=2].name ; dataList[id=1050901].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Bat Strike
   PL: Uderzenie Kijem
257. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 2 [Burst]
   PL: [OnSucceedAttackHead] Nakłada 2 [Burst]
258. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Burst]이 5 이상이면 코인 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1050901].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 5+ [Burst], Coin Power +1
   PL: Jeżeli cel ma 5+ [Burst], Moc Monet +1
259. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050901].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1050901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] Nakłada 2 [Burst]
260. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Burst]이 5 이상이면 코인 위력 +<style="highlight">2</style>
   źródło: Skills_personality-05.json :: dataList[id=1050901].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 5+ [Burst], Coin Power +<style="highlight">2</style>
   PL: Jeżeli cel ma 5+ [Burst], Moc Monet +<style="highlight">2</style>
261. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 내려박기
   źródło: Skills_personality-05.json :: dataList[id=1050902].levelList[level=1].name ; dataList[id=1050902].levelList[level=2].name ; dataList[id=1050902].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Smackdown
   PL: Roztrzaskanie
262. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050902].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1050902].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1050902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]이 6 이상이면 [AttackDown] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050902].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1050902].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] If target has 6+ [Burst], inflict 2 [AttackDown]
   PL: [OnSucceedAttack] Jeżeli cel ma 6+ [Burst], nakłada 2 [AttackDown]
264. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1050902].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Burst]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture
   EN: [WinDuel] Inflict +2 [Burst] Count
   PL: [WinDuel] Zwiększa Licznik [Burst] celu o 2
265. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 대상의 [Burst]이 6 이상이면 코인 위력 +1</style>\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1050902].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">[WhenUse] If target has 6+ [Burst], Coin Power +1</style>\n[WinDuel] Inflict +2 [Burst] Count
   PL: <style="highlight">[WhenUse] Jeżeli cel ma 6+ [Burst], Moc Monet +1</style>\n[WinDuel] Zwiększa Licznik [Burst] celu o 2
266. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]이 4 이상이면 [AttackDown] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050902].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] If target has 4+ [Burst], inflict 2 [AttackDown]
   PL: [OnSucceedAttack] Jeżeli cel ma 4+ [Burst], nakłada 2 [AttackDown]
267. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 쏟아내기
   źródło: Skills_personality-05.json :: dataList[id=1050903].levelList[level=3].name ; dataList[id=1050903].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Relentless
   PL: Bezwzględność
268. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 [Burst]이 6 이상이면 코인 위력 +1\n[WinDuel] [AttackDown] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050903].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel], [AttackDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [WhenUse] If target has 6+ [Burst], Coin Power +1\n[WinDuel] Inflict 2 [AttackDown]
   PL: [WhenUse] Jeżeli cel ma 6+ [Burst], Moc Monet +1\n[WinDuel] Nakłada 2 [AttackDown]
269. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_personality-05.json :: dataList[id=1050903].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1050903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Burst]
   PL: [OnSucceedAttack] Nakłada 4 [Burst]
270. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Burst]이 6 이상이면, 다음 턴에 [AttackDown] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050903].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1050903].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] If target has 6+ [Burst], inflict 2 [AttackDown] next turn
   PL: [OnSucceedAttack] Jeżeli cel ma 6+ [Burst], nakłada w następnej turze 2 [AttackDown]
271. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 대상의 [Burst]이 3 이상이면 합 위력 +1</style>\n[WhenUse] 대상의 [Burst]이 6 이상이면 코인 위력 +1\n[WinDuel] [AttackDown] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1050903].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel], [AttackDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: <style="highlight">[WhenUse] If target has 3+ [Burst], Clash Power +1</style>\n[WhenUse] If target has 6+ [Burst], Coin Power +1\n[WinDuel] Inflict 2 [AttackDown]
   PL: <style="highlight">[WhenUse] Jeżeli cel ma 3+ [Burst], Moc Starcia +1</style>\n[WhenUse] Jeżeli cel ma 6+ [Burst], Moc Monet +1\n[WinDuel] Nakłada 2 [AttackDown]
272. [Obrona (ulepszenia 1,4) — nazwa] 반격
   źródło: Skills_personality-05.json :: dataList[id=1050904].levelList[level=1].name ; dataList[id=1050904].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 7 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Counter
   PL: Kontra
273. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1050904].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1050904].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL: [OnSucceedAttack] Nakłada 1 [Burst]
274. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — nazwa] 시간 벌기
   źródło: Passives.json :: dataList[id=1050901].name
   limit: do 40 znaków
   EN: Buy Time
   PL: Zyskiwanie Czasu
275. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — opis] [Burst]이 있는 대상과 합 진행 시 합 위력 +1
   źródło: Passives.json :: dataList[id=1050901].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Clash Power +1 in a Clash against targets that have [Burst]
   PL: Moc Starcia +1 w Starciu z celami z [Burst]
276. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Glut.) — podsumowanie] [Burst]이 있는 대상과 합 진행 시 합 위력 +1
   źródło: Passives.json :: dataList[id=1050901].summary
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Glut.) — nazwa] 시간 벌기
   źródło: Passives.json :: dataList[id=1050911].name
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Glut.) — opis] [Burst]이 있는 대상과 합 진행 시 합 위력 +1\n대상의 [Burst] 횟수가 5 이상이면, 합 위력 +2
   źródło: Passives.json :: dataList[id=1050911].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Clash Power +1 against targets that have [Burst]\nClash Power +2 if the target has 5+ [Burst] Count
   PL: Moc Starcia +1 w Starciu z celami z [Burst]\nPrzy 5+ Liczniku [Burst] celu Moc Starcia +2
279. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — nazwa] 내가 책임진다
   źródło: Passives.json :: dataList[id=1050921].name
   limit: do 40 znaków
   EN: My Responsibility
   PL: To Moja Odpowiedzialność
280. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — opis] 속도가 가장 빠른 아군 1명이 [Burst]이 6 이상 부여된 대상에게 공격 적중 시 [AttackDown] 1 부여 (적 1명 당 턴 당 최대 3)
   źródło: Passives.json :: dataList[id=1050921].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Burst], [AttackDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: When 1 ally with the fastest Speed hits an enemy that has 6+ [Burst], inflict 1 [AttackDown] (3 times per enemy per turn)
   PL: Gdy 1 Sojusznik z najwyższą Szybkością trafi wroga z 6+ [Burst], nakłada 1 [AttackDown] (maks. 3 razy na turę per wróg)
281. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — podsumowanie] [Burst]이 6 이상 부여된 대상에게 공격 적중 시 [AttackDown] 1 부여
   źródło: Passives.json :: dataList[id=1050921].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst], [AttackDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: Inflict 1 [AttackDown] On Hit against targets that have 6+ [Burst]
   PL: Przy trafieniu celów z 6+ [Burst] nakłada 1 [AttackDown]
282. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Glut.) — nazwa] 내가 책임진다
   źródło: Passives.json :: dataList[id=1050931].name
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Glut.) — opis] 속도가 가장 빠른 아군 1명이 [Burst]이 3 이상 부여된 대상에게 공격 적중 시 [AttackDown] 1 부여 (적 1명 당 턴 당 최대 3)
   źródło: Passives.json :: dataList[id=1050931].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Burst], [AttackDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: When 1 ally with the fastest Speed hits an enemy that has 3+ [Burst], inflict 1 [AttackDown] (3 times per enemy per turn)
   PL: Gdy 1 Sojusznik z najwyższą Szybkością trafi wroga z 3+ [Burst], nakłada 1 [AttackDown] (maks. 3 razy na turę per wróg)
284. [Pasywka wsparcia (od ulepszenia 4, rezonans 3× Glut.) — podsumowanie] [Burst]이 3 이상 부여된 대상에게 공격 적중 시 [AttackDown] 1 부여
   źródło: Passives.json :: dataList[id=1050931].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst], [AttackDown]
   znaczenie tagów: [Burst] = 파열 / Rupture; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: Inflict 1 [AttackDown] On Hit against targets that have 3+ [Burst]
   PL: Przy trafieniu celów z 3+ [Burst] nakłada 1 [AttackDown]

## [000] Dieci Assoc. South Section 4 Director — Meursault — 남부 디에치 협회 4과 부장
- ID Tożsamości: `10510` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 82 · szybkość: 3–5 / 4–5 / 4–6 / 4–6
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Sinking

285. [Karta Tożsamości — tytuł] 남부 디에치 협회\n4과 부장
   źródło: Personalities.json :: dataList[id=10510].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Dieci Assoc.\nSouth Section 4 Director
   PL: Południowe Stowarzyszenie Dieci\nDyrektor Sekcji 4
286. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10510].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10510].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Karta Tożsamości — opis] 뫼르소의 열번째 인격
   źródło: Personalities.json :: dataList[id=10510].desc
   limit: do 120 znaków
   EN: Meursault’s 10th Identity
   PL: Dziesiąta Tożsamość Meursaulta
289. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 학업 정진
   źródło: Skills_personality-05.json :: dataList[id=1051001].levelList[level=1].name ; dataList[id=1051001].levelList[level=2].name ; dataList[id=1051001].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Studious Dedication
   PL: Sumienne Uczenie Się
290. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] x 최대 체력의 3%)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 [Discard]
   źródło: Skills_personality-05.json :: dataList[id=1051001].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Discard]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard
   EN: Gain ([KnowledgeExplored] x 3% of Max HP) Shield if this Skill is Discarded\n[WhenUse] [Discard] 1 Skill of the lowest rank in all of this unit's Skill Slots
   PL: Gdy ta Umiejętność zostanie odrzucona, zyskuje Tarczę równą ([KnowledgeExplored] x 3% Maks. HP)\n[WhenUse] [Discard] 1 Umiejętność najniższego poziomu ze wszystkich slotów Umiejętności tej jednostki
291. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Sinking]
292. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] x 최대 체력의 <style="highlight">4%</style>)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 [Discard]\n<style="highlight">[WhenUse] [KnowledgeExplored]이 2 이상이면, 합 위력 +1\n[WinDuel] [KnowledgeTraining] 2 얻음 (턴 당 1회)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051001].levelList[level=2].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KnowledgeExplored], [WhenUse], [Discard], [WinDuel], [KnowledgeTraining]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard; [WinDuel] = [합 승리시] / [Clash Win]; [KnowledgeTraining] = 지식 단련 / Erudition
   EN: Gain ([KnowledgeExplored] x <style="highlight">4%</style> of Max HP) Shield if this Skill is Discarded\n[WhenUse] [Discard] 1 Skill of the lowest rank in all of this unit's Skill Slots\n<style="highlight">[WhenUse] At 2+ [KnowledgeExplored], Clash Power +1\n[WinDuel] Gain 2 [KnowledgeTraining] (once per turn)</style>
   PL: Gdy ta Umiejętność zostanie odrzucona, zyskuje Tarczę równą ([KnowledgeExplored] x <style="highlight">4%</style> Maks. HP)\n[WhenUse] [Discard] 1 Umiejętność najniższego poziomu ze wszystkich slotów Umiejętności tej jednostki\n<style="highlight">[WhenUse] Przy 2+ [KnowledgeExplored] Moc Starcia +1\n[WinDuel] Zyskuje 2 [KnowledgeTraining] (1 raz na turę)</style>
293. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051001].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] celu o 2<style="highlight"></style>
294. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 이 스킬이 버려지면 ([KnowledgeExplored] x 최대 체력의 <style="highlight">5%</style>)만큼 보호막을 얻음\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 [Discard]\n<style="highlight">[WhenUse] ([KnowledgeExplored] - 1)만큼 합 위력이 증가 (최대 2)</style>\n[WinDuel] [KnowledgeTraining] 2 얻음 (턴 당 1회)
   źródło: Skills_personality-05.json :: dataList[id=1051001].levelList[level=4].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KnowledgeExplored], [WhenUse], [Discard], [WinDuel], [KnowledgeTraining]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard; [WinDuel] = [합 승리시] / [Clash Win]; [KnowledgeTraining] = 지식 단련 / Erudition
   EN: Gain ([KnowledgeExplored] x <style="highlight">5%</style> of Max HP) Shield if this Skill is Discarded\n[WhenUse] [Discard] 1 Skill of the lowest rank in all of this unit's Skill Slots\n<style="highlight">[WhenUse] Gain ([KnowledgeExplored] - 1) Clash Power (max 2)</style>\n[WinDuel] Gain 2 [KnowledgeTraining] (once per turn)
   PL: Gdy ta Umiejętność zostanie odrzucona, zyskuje Tarczę równą ([KnowledgeExplored] x <style="highlight">5%</style> Maks. HP)\n[WhenUse] [Discard] 1 Umiejętność najniższego poziomu ze wszystkich slotów Umiejętności tej jednostki\n<style="highlight">[WhenUse] Zyskuje Moc Starcia równą ([KnowledgeExplored] - 1) (maks. 2)</style>\n[WinDuel] Zyskuje 2 [KnowledgeTraining] (1 raz na turę)
295. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 배움의 시간
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=1].name ; dataList[id=1051002].levelList[level=2].name ; dataList[id=1051002].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Moment of Erudition
   PL: Czas Nauki
296. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [StartBattle] 자신에게 [KnowledgeExplored]만큼 [KnowledgeTraining] 부여\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 2개를 등급이 낮은 순으로 [Discard]
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [KnowledgeExplored], [KnowledgeTraining], [WhenUse], [Discard]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [KnowledgeExplored] = 탐구한 지식 / Insight; [KnowledgeTraining] = 지식 단련 / Erudition; [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard
   EN: [StartBattle] Gain [KnowledgeTraining] equal to [KnowledgeExplored] on self\n[WhenUse] [Discard] 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots
   PL: [StartBattle] Nakłada [KnowledgeTraining] równy [KnowledgeExplored] na siebie\n[WhenUse] [Discard] 2 Umiejętności tej jednostki ze wszystkich slotów Umiejętności, w kolejności od najniższego poziomu
297. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [KnowledgeExplored]만큼 [Sinking] 부여
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict [Sinking] equal to [KnowledgeExplored]
   PL: [OnSucceedAttack] Nakłada [Sinking] równe [KnowledgeExplored]
298. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[KnowledgeExplored] 1당 피해량 +3% (최대 9%)</style>\n<style="highlight">[StartBattle] 무작위 아군 하나와</style> 자신에게 [KnowledgeExplored]만큼 [KnowledgeTraining] 부여 <style="highlight">([Discard]을 사용하는 아군 중 [KnowledgeTraining]이 낮은 아군에게 우선 적용)</style>\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 2개를 등급이 낮은 순으로 [Discard]\n<style="highlight">[WhenUse] 대상의 [Sinking]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=2].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KnowledgeExplored], [StartBattle], [KnowledgeTraining], [Discard], [WhenUse], [Sinking]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [StartBattle] = [전투 시작시] / [Combat Start]; [KnowledgeTraining] = 지식 단련 / Erudition; [Discard] = 버림 / Discard; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">Deal +3% damage for every [KnowledgeExplored] on self (max 9%)</style>\n[StartBattle] Apply [KnowledgeTraining] equal to [KnowledgeExplored] on self <style="highlight"> to a random ally</style> and on self <style="highlight">(prioritizes allies with [Discard] that has the least [KnowledgeTraining])</style>\n[WhenUse] [Discard] 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots\n<style="highlight">[WhenUse] If target has 6+ [Sinking], Coin Power +1</style>
   PL: <style="highlight">Zadaje +3% obrażeń za każde 1 [KnowledgeExplored] (maks. 9%)</style>\n<style="highlight">[StartBattle] Nakłada [KnowledgeTraining] równy [KnowledgeExplored]</style> na siebie <style="highlight">i 1 losowego sojusznika</style> <style="highlight">(najpierw sojuszników używających [Discard] z najniższym [KnowledgeTraining])</style>\n[WhenUse] [Discard] 2 Umiejętności tej jednostki ze wszystkich slotów Umiejętności, w kolejności od najniższego poziomu\n<style="highlight">[WhenUse] Jeżeli cel ma 6+ [Sinking], Moc Monet +1</style>
299. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [KnowledgeExplored]만큼 [Sinking] 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict [Sinking] equal to [KnowledgeExplored]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada [Sinking] równy [KnowledgeExplored]<style="highlight"></style>
300. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [KnowledgeExplored] 1당 피해량 <style="highlight">+5%</style> (최대 <style="highlight">15%</style>)\n[StartBattle] 무작위 아군 <style="highlight">둘</style>과 자신에게 [KnowledgeExplored]만큼 [KnowledgeTraining] 부여 ([Discard]을 사용하는 아군 중 [KnowledgeTraining]이 낮은 아군에게 우선 적용)\n[WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 2개를 등급이 낮은 순으로 [Discard]\n<style="highlight">[WhenUse] 대상의 [Sinking] 6당 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=4].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KnowledgeExplored], [StartBattle], [KnowledgeTraining], [Discard], [WhenUse], [Sinking]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [StartBattle] = [전투 시작시] / [Combat Start]; [KnowledgeTraining] = 지식 단련 / Erudition; [Discard] = 버림 / Discard; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking
   EN: Deal <style="highlight">+5%</style> damage for every [KnowledgeExplored] on self (max <style="highlight">15%</style>)\n[StartBattle] Apply [KnowledgeTraining] equal to [KnowledgeExplored] on self <style="highlight">to 2 random allies</style> and on self (prioritizes allies with [Discard] that has the least [KnowledgeTraining])\n[WhenUse] [Discard] 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots\n<style="highlight">[WhenUse] Coin Power +1 for every 6 [Sinking] on target (max 2)</style>
   PL: Zadaje <style="highlight">+5%</style> obrażeń za każde 1 [KnowledgeExplored] (maks. <style="highlight">15%</style>)\n[StartBattle] Nakłada [KnowledgeTraining] równy [KnowledgeExplored] na siebie <style="highlight">i 2 losowych sojuszników</style> (najpierw sojuszników używających [Discard] z najniższym [KnowledgeTraining])\n[WhenUse] [Discard] 2 Umiejętności tej jednostki ze wszystkich slotów Umiejętności, w kolejności od najniższego poziomu\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 [Sinking] celu (maks. 2)</style>
301. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] <style="highlight">([KnowledgeExplored] x 2)</style>만큼 [Sinking] 부여
   źródło: Skills_personality-05.json :: dataList[id=1051002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict [Sinking] equal to <style="highlight">([KnowledgeExplored] x 2)</style>
   PL: [OnSucceedAttack] Nakłada [Sinking] równy <style="highlight">([KnowledgeExplored] x 2)</style>
302. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 지식 전소
   źródło: Skills_personality-05.json :: dataList[id=1051003].levelList[level=3].name ; dataList[id=1051003].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Scorch Knowledge
   PL: Wypalenie Wiedzy
303. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [KnowledgeExplored] 1당 피해량 +3% (최대 18%)\n[WhenUse] 대상의 [Sinking]이 6 이상이면, 코인 위력 +1\n[BeforeAttack] 자신의 [KnowledgeTraining]을 전부 소모하여 그 수치의 절반만큼 [KnowledgeExplored]을 추가로 얻음 (소수점 버림)\n[EndSkill] [KnowledgeExplored]이 4 이상이면, 1로 초기화 (이 스킬로 적 처치 시, 3으로 적용)
   źródło: Skills_personality-05.json :: dataList[id=1051003].levelList[level=3].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored], [WhenUse], [Sinking], [BeforeAttack], [KnowledgeTraining], [EndSkill]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [KnowledgeTraining] = 지식 단련 / Erudition; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +3% damage for every [KnowledgeExplored] on self (max 18%)\n[WhenUse] If target has 6+ [Sinking], Coin Power +1\n[BeforeAttack] Consume all [KnowledgeTraining] on self and gain half of that value as additional [KnowledgeExplored] (rounded down)\n[EndSkill] At 4+ [KnowledgeExplored], reset value to 1 (if this Skill defeats an enemy, reset value to 3 instead)
   PL: Zadaje +3% obrażeń za każde 1 [KnowledgeExplored] (maks. 18%)\n[WhenUse] Jeżeli cel ma 6+ [Sinking], Moc Monet +1\n[BeforeAttack] Zużywa całe [KnowledgeTraining] i zyskuje tyle samo dodatkowego [KnowledgeExplored] (zaokrąglone w dół)\n[EndSkill] Przy 4+ [KnowledgeExplored] resetuje wartość do 1 (jeżeli ta Umiejętność zabija wroga, resetuje wartość do 3)
304. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 위력과 [Sinking] 횟수를 합하여 [KnowledgeExplored]만큼 무작위로 부여
   źródło: Skills_personality-05.json :: dataList[id=1051003].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [KnowledgeExplored]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [OnSucceedAttack] Inflict [Sinking] Potency/Count equal to [KnowledgeExplored] value against the target (how much of that [Sinking] is Potency or Count is randomly determined)
   PL: [OnSucceedAttack] Nakłada [Sinking] Mocy i Licznika łącznie równy [KnowledgeExplored] (rozdzielone losowo)
305. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [KnowledgeExplored] 1당 피해량 <style="highlight">+5%</style> (최대 <style="highlight">45%</style>)\n<style="highlight">[WhenUse] 대상의 [Sinking] 6당, 코인 위력 +1 (최대 2)</style>\n[BeforeAttack] 자신의 [KnowledgeTraining]을 전부 소모하여 그 <style="highlight">수치만큼</style> [KnowledgeExplored]을 추가로 얻음\n[EndSkill] [KnowledgeExplored]이 4 이상이면, 1로 초기화 (이 스킬로 적 처치 시, 3으로 적용)
   źródło: Skills_personality-05.json :: dataList[id=1051003].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [KnowledgeExplored], [WhenUse], [Sinking], [BeforeAttack], [KnowledgeTraining], [EndSkill]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [KnowledgeTraining] = 지식 단련 / Erudition; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal <style="highlight">+5%</style> damage for every [KnowledgeExplored] (max <style="highlight">45%</style>)\n<style="highlight">[WhenUse] Coin Power +1 for every 6 [Sinking] on target (max 2)</style>\n[BeforeAttack] Consume all [KnowledgeTraining] on self and gain <style="highlight">the same value</style> as additional [KnowledgeExplored]\n[EndSkill] At 4+ [KnowledgeExplored], reset value to 1 (if this Skill defeats an enemy, reset value to 3 instead)
   PL: Zadaje <style="highlight">+5%</style> obrażeń za każde 1 [KnowledgeExplored] (maks. <style="highlight">45%</style>)\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 [Sinking] celu (maks. 2)</style>\n[BeforeAttack] Zużywa całe [KnowledgeTraining] i zyskuje <style="highlight">tyle samo</style> dodatkowego [KnowledgeExplored]\n[EndSkill] Przy 4+ [KnowledgeExplored] resetuje wartość do 1 (jeżeli ta Umiejętność zabija wroga, resetuje wartość do 3)
306. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 위력과 [Sinking] 횟수를 합하여 [KnowledgeExplored]만큼 무작위로 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking], [KnowledgeExplored]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [OnSucceedAttack] Inflict [Sinking] Potency/Count equal to [KnowledgeExplored] value against the target (how much of that [Sinking] is Potency or Count is randomly determined)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada [Sinking] Mocy i Licznika łącznie równy [KnowledgeExplored] (rozdzielone losowo)<style="highlight"></style>
307. [Obrona (ulepszenia 1,4) — nazwa] 탐구 몰입
   źródło: Skills_personality-05.json :: dataList[id=1051004].levelList[level=1].name ; dataList[id=1051004].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Fixated Study
   PL: Obsesyjne Badanie
308. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 [Discard]
   źródło: Skills_personality-05.json :: dataList[id=1051004].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Discard]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard
   EN: [WhenUse] [Discard] 1 Skill of the highest rank in all of this unit's Skill Slots
   PL: [WhenUse] [Discard] 1 Umiejętność najwyższego poziomu ze wszystkich slotów Umiejętności tej jednostki
309. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 [Discard]\n<style="highlight">[WhenUse] 다음 턴에 이 슬롯이 도발치 6을 얻음</style>
   źródło: Skills_personality-05.json :: dataList[id=1051004].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Discard]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Discard] = 버림 / Discard
   EN: [WhenUse] [Discard] 1 Skill of the highest rank in all of this unit's Skill Slots\n<style="highlight">[WhenUse] Gain +6 Aggro to this Skill Slot next turn</style>
   PL: [WhenUse] [Discard] 1 Umiejętność najwyższego poziomu ze wszystkich slotów Umiejętności tej jednostki\n<style="highlight">[WhenUse] Prowokacja tego slotu +6 w następnej turze</style>
310. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Gloom) — nazwa] 자율 학습 지시
   źródło: Passives.json :: dataList[id=1051001].name
   limit: do 40 znaków
   EN: Study Hall
   PL: Sala Samodzielnej Nauki
311. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Gloom) — opis] 자신을 제외한 아군이 스킬을 버릴 때마다 대상과 자신에게 [KnowledgeTraining] 1을 부여 (스킬 당 1회, 턴 당 3회)\n턴 종료 시, 자신을 제외하고 스킬을 버린 아군의 수만큼 다음 턴에 관통 피해량 증가, 타격 피해량 증가 얻음 (최대 3)
   źródło: Passives.json :: dataList[id=1051001].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeTraining]
   znaczenie tagów: [KnowledgeTraining] = 지식 단련 / Erudition
   EN: Every time another ally Discards a Skill, apply 1 [KnowledgeTraining] to the ally and self (once per Skill, 3 times per turn)\nTurn End: next turn, gain Pierce DMG Up and Blunt DMG Up equal to the number of other allies that Discarded Skills (max 3)
   PL: Za każdym razem, gdy inny sojusznik odrzuca Umiejętność, nakłada 1 [KnowledgeTraining] jemu i sobie (1 raz na Umiejętność, 3 razy na turę)\nNa koniec tury zyskuje w następnej turze Wzrost Obrażeń Kłucia i Obuchowych równy liczbie innych sojuszników, którzy odrzucili Umiejętności (maks. 3)
312. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — nazwa] 성실한 배움
   źródło: Passives.json :: dataList[id=1051021].name
   limit: do 40 znaków
   EN: Diligent Learning
   PL: Pilna Nauka
313. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Gloom) — opis] 최대 체력이 가장 높은 아군 1명이 스킬을 버릴 때, 해당 인격 최대 체력의 (5 x 버린 스킬의 등급)% 만큼 보호막을 얻음 (턴 당 1회)\n[KnowledgeExplored]이 있는 경우, 보호막 수치가 1.5배로 적용됨
   źródło: Passives.json :: dataList[id=1051021].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [KnowledgeExplored]
   znaczenie tagów: [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: When 1 ally with the highest max HP Discards a Skill, gain (5 x Discarded Skill rank)% of the max HP as Shield (once per turn)\nIf the unit has [KnowledgeExplored], multiply the above Shield value by 1.5
   PL: Gdy 1 Sojusznik z najwyższym Maks. HP odrzuca Umiejętność, zyskuje Tarczę równą (5 x poziom odrzuconej Umiejętności)% Maks. HP (1 raz na turę)\nJeżeli ma [KnowledgeExplored], wartość Tarczy mnoży się x 1.5

## [000] Cinq Assoc. West Section 3 — Meursault — 서부 섕크 협회 3과
- ID Tożsamości: `10511` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 69 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Rupture, Poise

314. [Karta Tożsamości — tytuł] 서부 섕크 협회\n3과
   źródło: Personalities.json :: dataList[id=10511].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cinq Assoc.\nWest Section 3
   PL: Zachodnie Stowarzyszenie Cinq\nSekcja 3
315. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10511].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10511].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Karta Tożsamości — opis] 뫼르소의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10511].desc
   limit: do 120 znaków
   EN: Meursault’s 11th Identity
   PL: Jedenasta Tożsamość Meursaulta
318. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 알레
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=1].name ; dataList[id=1051101].levelList[level=2].name ; dataList[id=1051101].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Allez
   PL: Allez
319. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=1].desc
   (powtórzenie elementu 214 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1051101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1051101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +1 Licznika [Breath]
321. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 자신의 속도가 대상보다 3 이상 높으면 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 위력을 부여하지 않고 적중시 [Burst] 횟수를 소모하지 않음\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=2].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by 3 or more, Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Potency with its effects, but does not consume [Burst] Count On Hit\n[WhenUse] Gain +2 [Breath] Count
   PL: Jeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, Moc Monet +1\n[WhenUse] Jeżeli cel ma 15+ [Burst] Mocy i 3+ Licznika [Burst], ta Umiejętność nie nakłada Mocy [Burst] swoimi efektami, ale nie zużywa Licznika [Burst] przy trafieniu\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
322. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 3 당 코인 위력 +1. 최대 2)\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 위력을 부여하지 않고 적중시 [Burst] 횟수를 소모하지 않음\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=4].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 3 Speed difference; max 2)\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Potency with its effects, but does not consume [Burst] Count On Hit\n[WhenUse] Gain +2 [Breath] Count
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, zyskuje Moc Monet zależnie od różnicy Szybkości (Moc Monet +1 za każde 3 różnicy Szybkości; maks. 2)\n[WhenUse] Jeżeli cel ma 15+ [Burst] Mocy i 3+ Licznika [Burst], ta Umiejętność nie nakłada Mocy [Burst] swoimi efektami, ale nie zużywa Licznika [Burst] przy trafieniu\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
324. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신이 대상보다 속도가 빠르면 대상과의 속도 차이만큼 [Burst] 부여 (최대 3)
   źródło: Skills_personality-05.json :: dataList[id=1051101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If this unit's Speed is faster than the target's, inflict [Burst] equal to their Speed difference (max 3)
   PL: [OnSucceedAttack] Jeżeli Szybkość tej jednostki jest większa niż celu, nakłada [Burst] równy różnicy Szybkości (maks. 3)
325. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 팡트
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=1].name ; dataList[id=1051102].levelList[level=2].name ; dataList[id=1051102].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Fente
   PL: Fente
326. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WinDuel] Gain +2 [Breath] Count
   PL: [WinDuel] Zwiększa własny Licznik [Breath] o 2
327. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1051102].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1051102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 4 부여
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1051102].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] 자신의 속도가 대상보다 3 이상 높으면 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬의 효과로 [Burst] 위력, [Burst] 횟수를 부여하지 않고, 적중 시 [Burst] 횟수를 소모하지 않음\n[WinDuel] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=2].desc ; dataList[id=1051102].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the target's by 3 or more, Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not inflict [Burst] Potency or Count with its effects, but does not consume [Burst] Count On Hit\n[WinDuel] Gain +2 [Breath] Count
   PL: Jeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, Moc Monet +1\n[WhenUse] Jeżeli cel ma 15+ [Burst] Mocy i 3+ Licznika [Burst], ta Umiejętność nie nakłada Mocy ani Licznika [Burst] swoimi efektami, ale nie zużywa Licznika [Burst] przy trafieniu\n[WinDuel] Zwiększa własny Licznik [Breath] o 2
331. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 7+ Speed, inflict +2 [Burst] Count
   PL: [OnSucceedAttack] Przy 7+ Szybkości zwiększa Licznik [Burst] celu o 2
332. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +2 Licznika [Breath]
333. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">[Burst]을 부여하지 않은 경우, 부여하는 [Burst] 위력, 횟수 1 당 크리티컬 피해량 +5%</style>
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: <style="highlight">If this unit does not inflict [Burst], +5% Damage on Critical Hit for every [Burst] Potency and Count it would have inflicted</style>
   PL: <style="highlight">Jeżeli ta jednostka nie nakłada [Burst], zadaje +5% obrażeń przy trafieniu krytycznym za każde 1 Mocy i Licznika [Burst], które nakładałaby</style>
334. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 4 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 4 [Burst]<style="highlight"></style>
335. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 7 이상이면, [Burst] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051102].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 7+ Speed, inflict +2 [Burst] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Przy 7+ Szybkości zwiększa Licznik [Burst] celu o 2<style="highlight"></style>
336. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 살뤼
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=3].name ; dataList[id=1051103].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Salut
   PL: Salut
337. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 대상보다 2 이상 높으면 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 적중 시 [Burst] 횟수를 소모하지 않음\n[WinDuel] [Breath] 5 얻음\n- 대상에게 [ConcentratedAttackMeursault]가 있으면 추가로 호흡 5 얻음
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=3].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel], [Breath], [ConcentratedAttackMeursault]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault
   EN: If this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not consume [Burst] Count On Hit\n[WinDuel] Gain 5 [Breath]\n- If target has [ConcentratedAttackMeursault], gain 5 additional [Breath]
   PL: Jeżeli Szybkość tej jednostki jest większa od celu o 2 lub więcej, Moc Monet +1\n[WhenUse] Jeżeli cel ma 15+ [Burst] Mocy i 3+ Licznika [Burst], ta Umiejętność nie zużywa Licznika [Burst] przy trafieniu\n[WinDuel] Zyskuje 5 [Breath]\n- Jeżeli cel ma [ConcentratedAttackMeursault], zyskuje dodatkowo 5 [Breath]
338. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [WinDuelAttack] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1051103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuelAttack]
   znaczenie tagów: [WinDuelAttack] = [합 승리 후 적중시] / [Hit after Clash Win]
   EN: [WinDuelAttack] The final Coin deals +10% damage
   PL: [WinDuelAttack] Ostatnia moneta zadaje +10% obrażeń
339. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [WinDuelAttack] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1051103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 해당 슬롯의 [ConcentratedAttackMeursault] 1 당 피해량 +10%
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ConcentratedAttackMeursault]
   znaczenie tagów: [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault
   EN: Deal +10% damage for every [ConcentratedAttackMeursault] on the Slot
   PL: Zadaje +10% obrażeń za każde 1 [ConcentratedAttackMeursault] na tym slocie
341. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1051103].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2당 코인 위력 +1. 최대 3)</style>\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 적중 시 [Burst] 횟수를 소모하지 않음\n[WinDuel] [Breath] 5 얻음\n- 대상에게 [ConcentratedAttackMeursault]가 있으면 추가로 호흡 5 얻음
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=4].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel], [Breath], [ConcentratedAttackMeursault]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault
   EN: <style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 3)</style>\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count, this Skill does not consume [Burst] Count On Hit\n[WinDuel] Gain 5 [Breath]\n- If target has [ConcentratedAttackMeursault], gain 5 additional [Breath]
   PL: <style="highlight">Jeżeli Szybkość tej jednostki jest większa niż celu, zyskuje Moc Monet zależnie od różnicy Szybkości (Moc Monet +1 za każde 2 różnicy Szybkości; maks. 3)</style>\n[WhenUse] Jeżeli cel ma 15+ [Burst] Mocy i 3+ Licznika [Burst], ta Umiejętność nie zużywa Licznika [Burst] przy trafieniu\n[WinDuel] Zyskuje 5 [Breath]\n- Jeżeli cel ma [ConcentratedAttackMeursault], zyskuje dodatkowo 5 [Breath]
343. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 해당 슬롯의 [ConcentratedAttackMeursault] 1 당 피해량 <style="highlight">+20%</style>
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ConcentratedAttackMeursault]
   znaczenie tagów: [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault
   EN: Deal <style="highlight">+20%</style> damage for every [ConcentratedAttackMeursault] on the Slot
   PL: Zadaje <style="highlight">+20%</style> obrażeń za każde 1 [ConcentratedAttackMeursault] na tym slocie
344. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] <style="highlight">- 대상의 [Burst] 1 당 크리티컬 피해량 +2% (최대 30%)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: <style="highlight">- Deal +2% Damage on Critical Hit for every [Burst] on target (max 30%)</style>
   PL: <style="highlight">- Zadaje +2% obrażeń przy trafieniu krytycznym za każde 1 [Burst] celu (maks. 30%)</style>
345. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] <style="highlight">[EndSkill] 이 코인으로 대상을 처치하거나 부위를 파괴했으면, 무작위 대상에게 스킬 1회 재사용 (재사용 시 발동하지 않음)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051103].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: <style="highlight">[EndSkill] If this Coin defeated the target or destroyed the Part, Reuse this Skill once against a random target (does not activate on Reuse)</style>
   PL: <style="highlight">[EndSkill] Jeżeli ta moneta pokonała cel albo zniszczyła część ciała, ponownie używa tej Umiejętności 1 raz na losowym celu (nie uruchamia się przy ponownym użyciu)</style>
346. [Obrona (ulepszenia 1,4) — nazwa] 데팡시브
   źródło: Skills_personality-05.json :: dataList[id=1051104].levelList[level=1].name ; dataList[id=1051104].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Défensive
   PL: Défensive
347. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 속도가 공격자보다 3 이상 높으면, 코인 위력 +2
   źródło: Skills_personality-05.json :: dataList[id=1051104].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] If this unit's Speed is faster than the target's by 3 or more, Coin Power +2
   PL: [WhenUse] Jeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, Moc Monet +2
348. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Pride, posiadane 2× Glut.) — nazwa] 결투 생방송
   źródło: Passives.json :: dataList[id=1051101].name
   limit: do 40 znaków
   EN: Duel Livestream
   PL: Transmisja Na Żywo z Pojedynku
349. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Pride, posiadane 2× Glut.) — opis] 턴 종료시 자신의 [Breath] 위력 3 마다, 다음 턴에 [Agility] 1 얻음 (최대 2)\n기본 스킬로 공격 적중 시,  다음 턴에 [ConcentratedAttackMeursault] 부여. (스킬당 1회 부여)
   źródło: Passives.json :: dataList[id=1051101].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Agility], [ConcentratedAttackMeursault]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault
   EN: Gain 1 [Agility] next turn for every 3 [Breath] Potency on self at Turn End (max 2)\nOn Hit using Base Skills: Inflict [ConcentratedAttackMeursault] next turn (once per Skill)
   PL: Na koniec tury zyskuje w następnej turze 1 [Agility] za każde 3 własnej Mocy [Breath] (maks. 2)\nPrzy trafieniu podstawową Umiejętnością nakłada w następnej turze [ConcentratedAttackMeursault]. (1 raz na Umiejętność)
350. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Pride, posiadane 2× Glut.) — podsumowanie] 턴 종료시 자신의 호흡 횟수에 비례해 다음 턴에 신속 얻음. 기본 공격 적중시 다음 턴에 [ConcentratedAttackMeursault] 부여
   źródło: Passives.json :: dataList[id=1051101].summary
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [ConcentratedAttackMeursault], [Agility], [Breath]
   znaczenie tagów: [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault; [Agility] = 신속 / Haste; [Breath] = 호흡 / Poise
   EN: Turn End: Gain [Agility] based on [Breath] Count on self. On Hit using a Base Skill, inflict [ConcentratedAttackMeursault] next turn
   PL: Na koniec tury zyskuje Pośpiech proporc. do Licznika Oddechu w nast. turze. Przy trafieniu podstawowym atakiem nakłada w nast. turze [ConcentratedAttackMeursault]
351. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Pride, posiadane 2× Glut.) — nazwa] 결투 생방송
   źródło: Passives.json :: dataList[id=1051111].name
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Pride, posiadane 2× Glut.) — opis] 턴 종료시 자신의 [Breath] 위력 3 마다, 다음 턴에 [Agility] 1 얻음 (최대 2)\n기본 스킬로 공격 적중 시, 다음 턴에 [ConcentratedAttackMeursault] 부여. (스킬당 1회 부여)\n<style="highlight">[ConcentratedAttackMeursault]가 부여된 슬롯을 공격하여 대상을 처치하거나 부위를 파괴했으면, 정신력 7 회복</style>
   źródło: Passives.json :: dataList[id=1051111].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Breath], [Agility], [ConcentratedAttackMeursault]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault
   EN: Gain 1 [Agility] next turn for every 3 [Breath] Potency on self at Turn End (max 2)\nOn Hit using Base Skills: Inflict [ConcentratedAttackMeursault] next turn (once per Skill)\n<style="highlight">If this unit attacked the Slot that has [ConcentratedAttackMeursault] and defeated its owner or broke the Part, heal 7 SP</style>
   PL: Na koniec tury zyskuje w następnej turze 1 [Agility] za każde 3 własnej Mocy [Breath] (maks. 2)\nPrzy trafieniu podstawową Umiejętnością nakłada w następnej turze [ConcentratedAttackMeursault]. (1 raz na Umiejętność)\n<style="highlight">Jeżeli zaatakowała slot z [ConcentratedAttackMeursault] i pokonała jego właściciela albo zniszczyła część ciała, odzyskuje 7 Poczytalności</style>
353. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Pride, posiadane 2× Glut.) — podsumowanie] 턴 종료시 자신의 호흡 횟수에 비례해 다음 턴에 신속 얻음. 기본 공격 적중시 다음 턴에 [ConcentratedAttackMeursault] 부여. 대상을 처치하면 정신력을 회복함
   źródło: Passives.json :: dataList[id=1051111].summary
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [ConcentratedAttackMeursault], [Agility], [Breath]
   znaczenie tagów: [ConcentratedAttackMeursault] = 집중 공격 - 뫼르소 / Focused Attack - Meursault; [Agility] = 신속 / Haste; [Breath] = 호흡 / Poise
   EN: Turn End: Gain [Agility] based on [Breath] Count on self. On Hit using a Base Skill, inflict [ConcentratedAttackMeursault] next turn. Heals SP On Kill
   PL: Na koniec tury zyskuje Pośpiech proporc. do Licznika Oddechu w nast. turze. Przy trafieniu podstawowym atakiem nakłada w nast. turze [ConcentratedAttackMeursault]. Leczy Poczyt. przy zabiciu
354. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — nazwa] 한 발 더 빠르게
   źródło: Passives.json :: dataList[id=1051121].name
   limit: do 40 znaków
   EN: One Step Ahead
   PL: O Krok przed Resztą
355. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — opis] 속도가 가장 빠른 아군 1명이 합 승리시 다음 턴에 신속 1을 얻음(턴 당 최대 2회)
   źródło: Passives.json :: dataList[id=1051121].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: The fastest ally, on Clash Win, gains 1 [Agility] next turn (2 times per turn)
   PL: Najszybszy sojusznik przy wygranej Starciu zyskuje w następnej turze 1 [Agility] (maks. 2 razy na turę)
356. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — podsumowanie] 속도가 가장 빠른 아군이 합 승리시 다음 턴에 신속 얻음
   źródło: Passives.json :: dataList[id=1051121].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: The fastest ally, on Clash Win, gains 1 [Agility] next turn
   PL: Najszybszy sojusznik przy wygranej Starciu zyskuje w następnej turze Pośpiech

## [000] The Thumb East Capo IIII — Meursault — 동부 엄지 카포IIII
- ID Tożsamości: `10512` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 82 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Burn, Tremor

357. [Karta Tożsamości — tytuł] 동부 엄지\n카포IIII
   źródło: Personalities.json :: dataList[id=10512].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Thumb\nEast Capo IIII
   PL: Kciuk ze Wschodu\nCapo IIII
358. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10512].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10512].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Karta Tożsamości — opis] 뫼르소의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10512].desc
   limit: do 120 znaków
   EN: Meursault’s 12th Identity
   PL: Dwunasta Tożsamość Meursaulta
361. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 이연참-폭[爆]
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=1].name ; dataList[id=1051201].levelList[level=2].name ; dataList[id=1051201].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Double Slash - Blast [爆]
   PL: Podwójne Cięcie - Wybuch [爆]
362. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [BulletPropellantAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellantAlly]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round
   EN: Spend 1 [BulletPropellantAlly]
   PL: Zużywa 1 [BulletPropellantAlly]
363. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]
364. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]
365. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">메인 타겟 대상의 [Combustion]과 [Vibration]의 합 4당, 최종 위력 +1 (최대 2)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: <style="highlight">Final Power +1 for every 4 ([Combustion] + [Vibration]) on the main target (max 2)</style>
   PL: <style="highlight">Moc Końcowa +1 za każde 4 (suma [Combustion] i [Vibration] głównego celu) (maks. 2)</style>
366. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Vibration] 1 부여</style>
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Vibration]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [Vibration]</style>
367. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [BulletPropellantAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BulletPropellantAlly]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round
   EN: Spend 1 [BulletPropellantAlly]<style="highlight"></style>
   PL: Zużywa 1 [BulletPropellantAlly]<style="highlight"></style>
368. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]<style="highlight"></style>
369. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=2].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]<style="highlight"></style>
370. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 메인 타겟 대상의 [Combustion]과 [Vibration]의 합 4당, 최종 위력 +1 (최대 <style="highlight">3</style>)
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: Final Power +1 for every 4 ([Combustion] + [Vibration]) on the main target (max <style="highlight">3</style>)
   PL: Moc Końcowa +1 za każde 4 (suma [Combustion] i [Vibration] głównego celu) (maks. <style="highlight">3</style>)
371. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Vibration]
373. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051201].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Combustion]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Combustion]
374. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 삼연격-폭[爆]
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].name ; dataList[id=1051202].levelList[level=2].name ; dataList[id=1051202].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Triple Slash - Blast [爆]
   PL: Potrójne Cięcie - Wybuch [爆]
375. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [BulletPropellantAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 363 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [BulletPropellantAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]
380. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o 1
381. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">메인 타겟 대상의 [Combustion]과 [Vibration]의 합 4당, 최종 위력 +1 (최대 2)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].desc
   (powtórzenie elementu 365 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Vibration] 1 부여</style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [BulletPropellantAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 367 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [BulletPropellantAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1051202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 367 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]<style="highlight"></style>
388. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o 1<style="highlight"></style>
389. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 4 — opis] <style="highlight">[OnSucceedAttack] 대상의 [Vibration] 횟수가 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=2].coinlist[#2].coindescs[#3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: <style="highlight">[OnSucceedAttack] If target has 3+ [Vibration] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli cel ma 3+ Licznika [Vibration], wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1</style>
390. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 메인 타겟 대상의 [Combustion]과 [Vibration]의 합 4당, 최종 위력 +1 (최대 <style="highlight">4</style>)
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: Final Power +1 for every 4 ([Combustion] + [Vibration]) on the main target (max <style="highlight">4</style>)
   PL: Moc Końcowa +1 za każde 4 (suma [Combustion] i [Vibration] głównego celu) (maks. <style="highlight">4</style>)
391. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 372 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +<style="highlight">2</style> Licznika [Vibration]
395. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">+2</style> [Combustion] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o <style="highlight">2</style>
396. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051202].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 3+ [Vibration] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli cel ma 3+ Licznika [Vibration], wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1<style="highlight"></style>
397. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 쾌도난마 [快刀亂麻]
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].name ; dataList[id=1051203].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Tanglecleaver [快刀亂麻]
   PL: Tanglecleaver [快刀亂麻]
398. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [BulletPropellantSpecialAlly]이 있으면, '초절맹호살격난참'으로 발동됨\n- [BeforeUse] [BulletPropellantSpecialAlly]이 없으면 발동 취소\n메인 타겟 대상의 [Combustion]과 [Vibration]의 합이 8 이상이면, 코인 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [BulletPropellantSpecialAlly], [BeforeUse], [Combustion], [Vibration]
   znaczenie tagów: [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round; [BeforeUse] = [사용전] / [Before Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: If this unit has [BulletPropellantSpecialAlly], activate 'Savage Tigerslayer's Perfected Flurry of Blades' instead\n- [BeforeUse] If this unit does not have [BulletPropellantSpecialAlly], cancel activation\nIf the main target has 8+ ([Combustion] + [Vibration]), Coin Power +1
   PL: Jeżeli ma [BulletPropellantSpecialAlly], uruchamia się jako „Najdziksze Wybuchowe Szaleństwo Rzeźnika Tygrysów”\n- [BeforeUse] Jeżeli nie ma [BulletPropellantSpecialAlly], anuluje aktywację\nJeżeli główny cel ma 8+ (suma [Combustion] i [Vibration]), Moc Monet +1
399. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [BulletPropellantAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
401. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL: [OnSucceedAttack] Nakłada 2 [Combustion]
402. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [BulletPropellantAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Vibration]
404. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +2 [Combustion] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o 2
405. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [BulletPropellantAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] 이 코인 효과로 [BulletPropellantAlly]을 소모하였다면, 피해량 +20%
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellantAlly]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round
   EN: If this unit spent [BulletPropellantAlly] due to this Coin's effect, deal +20% damage
   PL: Jeżeli zużyto [BulletPropellantAlly] efektem tej monety, zadaje +20% obrażeń
407. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]
   PL: [OnSucceedAttack] Wywołuje [Switch_Vibration] do [VibrationIgnition]
408. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- [BulletPropellantAlly] 소모 시, 효과 1회 추가 발동
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [BulletPropellantAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [BulletPropellantAlly] = 호표탄 / Tigermark Round
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When spending [BulletPropellantAlly], activate the above effect once more
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1\n- Zużycie [BulletPropellantAlly] uruchamia ten efekt dodatkowo 1 raz
409. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [BulletPropellantSpecialAlly]이 있으면, '초절맹호살격난참'으로 발동됨\n- [BeforeUse] [BulletPropellantSpecialAlly]이 없으면 발동 취소\n메인 타겟 대상의 [Combustion]과 [Vibration]의 <style="highlight">합 8당, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BulletPropellantSpecialAlly], [BeforeUse], [Combustion], [Vibration]
   znaczenie tagów: [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round; [BeforeUse] = [사용전] / [Before Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: If this unit has [BulletPropellantSpecialAlly], activate 'Savage Tigerslayer's Perfected Flurry of Blades' instead\n- [BeforeUse] If this unit does not have [BulletPropellantSpecialAlly], cancel activation\n<style="highlight">Coin Power +1 for every 8 ([Combustion] + [Vibration]) on the main target, (max 2)</style>
   PL: Jeżeli ma [BulletPropellantSpecialAlly], uruchamia się jako „Najdziksze Wybuchowe Szaleństwo Rzeźnika Tygrysów”\n- [BeforeUse] Jeżeli nie ma [BulletPropellantSpecialAlly], anuluje aktywację\n<style="highlight">Moc Monet +1 za każde 8 (suma [Combustion] i [Vibration] głównego celu), (maks. 2)</style>
410. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [BulletPropellantAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 367 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Vibration]
412. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] <style="highlight">3</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Combustion]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Combustion]
413. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [BulletPropellantAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 367 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">+3</style> [Vibration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Vibration] celu o <style="highlight">3</style>
415. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">+3</style> [Combustion] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o <style="highlight">3</style>
416. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [BulletPropellantAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 367 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] 이 코인 효과로 [BulletPropellantAlly]을 소모하였다면, 피해량 <style="highlight">+50%</style>
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BulletPropellantAlly]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round
   EN: If this unit spent [BulletPropellantAlly] due to this Coin's effect, deal <style="highlight">+50%</style> damage
   PL: Jeżeli zużyto [BulletPropellantAlly] efektem tej monety, zadaje <style="highlight">+50%</style> obrażeń
418. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]<style="highlight"></style>
   PL: [OnSucceedAttack] Wywołuje [Switch_Vibration] do [VibrationIgnition]<style="highlight"></style>
419. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- [BulletPropellantAlly] 소모 시, 효과 <style="highlight">2</style>회 추가 발동
   źródło: Skills_personality-05.json :: dataList[id=1051203].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [BulletPropellantAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [BulletPropellantAlly] = 호표탄 / Tigermark Round
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When spending [BulletPropellantAlly], activate the above effect <style="highlight">2</style> more times
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1\n- Zużycie [BulletPropellantAlly] uruchamia ten efekt dodatkowo <style="highlight">2</style> razy
420. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 초절맹호살격난참 [超絕猛虎殺擊亂斬]
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].name ; dataList[id=1051205].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 3 · monety: 5 (+3)
   limit: do 80 znaków
   EN: Savage Tigerslayer's Perfected Flurry of Blades [超絕猛虎殺擊亂斬]
   PL: Najdziksze Wybuchowe Szaleństwo Rzeźnika Tygrysów [超絕猛虎殺擊亂斬]
421. [Umiejętność 4 (×0) (ulepszenie 3) — opis] 메인 타겟 대상의 [Combustion]과 [Vibration]의 합이 8 이상이면, 코인 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: If the main target has 8+ ([Combustion] + [Vibration]), Coin Power +1
   PL: Jeżeli główny cel ma 8+ (suma [Combustion] i [Vibration]), Moc Monet +1
422. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] [BulletPropellantSpecialAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellantSpecialAlly]
   znaczenie tagów: [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: Spend 1 [BulletPropellantSpecialAlly]
   PL: Zużywa 1 [BulletPropellantSpecialAlly]
425. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 1 — opis] [BulletPropellantSpecialAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 404 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 5, efekt 1 — opis] [BulletPropellantSpecialAlly] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 5, efekt 2 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 5, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- [BulletPropellantSpecialAlly] 소모 시, 효과 1회 추가 발동
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=3].coinlist[#4].coindescs[#2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [BulletPropellantSpecialAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When spending [BulletPropellantSpecialAlly], activate the above effect once more
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1\n- Zużycie [BulletPropellantSpecialAlly] uruchamia ten efekt dodatkowo 1 raz
431. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 메인 타겟 대상의 [Combustion]과 [Vibration]의 <style="highlight">합 8당, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: <style="highlight">Coin Power +1 for every 8 ([Combustion] + [Vibration]) on the main target (max 2)</style>
   PL: <style="highlight">Moc Monet +1 za każde 8 (suma [Combustion] i [Vibration] głównego celu) (maks. 2)</style>
432. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 414 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] [BulletPropellantSpecialAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BulletPropellantSpecialAlly]
   znaczenie tagów: [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: Spend 1 [BulletPropellantSpecialAlly]<style="highlight"></style>
   PL: Zużywa 1 [BulletPropellantSpecialAlly]<style="highlight"></style>
435. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] <style="highlight">3</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 1 — opis] [BulletPropellantSpecialAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 5, efekt 1 — opis] [BulletPropellantSpecialAlly] 1 소모<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 5, efekt 2 — opis] [OnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 418 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 5, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- [BulletPropellantSpecialAlly] 소모 시, 효과 <style="highlight">2</style>회 추가 발동
   źródło: Skills_personality-05.json :: dataList[id=1051205].levelList[level=4].coinlist[#4].coindescs[#2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [BulletPropellantSpecialAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- When spending [BulletPropellantSpecialAlly], activate the above effect <style="highlight">2</style> more times
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1\n- Zużycie [BulletPropellantSpecialAlly] uruchamia ten efekt dodatkowo <style="highlight">2</style> razy
441. [Obrona (ulepszenia 1,4) — nazwa] 끓어오르는군.
   źródło: Skills_personality-05.json :: dataList[id=1051204].levelList[level=1].name ; dataList[id=1051204].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: I'm Burning Up.
   PL: Płonne w Niebie.
442. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n메인 타겟 대상의 [Combustion]과 [Vibration]의 합이 4 이상이면, 최종 위력 +1\n[BulletPropellantAlly] 또는 [BulletPropellantSpecialAlly]이 0이면, 합 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1051204].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [Combustion], [Vibration], [BulletPropellantAlly], [BulletPropellantSpecialAlly]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [BulletPropellantAlly] = 호표탄 / Tigermark Round; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: [DuelCounter]\nIf the main target has 4+ ([Combustion] + [Vibration]), Final Power +1\nIf [BulletPropellantAlly] (or [BulletPropellantSpecialAlly]) is at 0, Clash Power +1
   PL: [DuelCounter]\nJeżeli główny cel ma 4+ (suma [Combustion] i [Vibration]), Moc Końcowa +1\nPrzy 0 [BulletPropellantAlly] lub [BulletPropellantSpecialAlly] Moc Starcia +1
443. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가 (턴당 2회)
   źródło: Skills_personality-05.json :: dataList[id=1051204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count (2 times per turn)
   PL: [OnSucceedAttack] Zwiększa Licznik [Vibration] o 1 (2 razy na turę)
444. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n메인 타겟 대상의 [Combustion]과 [Vibration]의 <style="highlight">합 4당, 최종 위력 +1 (최대 2)</style>\n[BulletPropellantAlly] 또는 [BulletPropellantSpecialAlly]이 0이면, 합 위력 <style="highlight">+2</style>
   źródło: Skills_personality-05.json :: dataList[id=1051204].levelList[level=4].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [Combustion], [Vibration], [BulletPropellantAlly], [BulletPropellantSpecialAlly]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [BulletPropellantAlly] = 호표탄 / Tigermark Round; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: [DuelCounter]\n<style="highlight">Final Power +1 for every 4 ([Combustion] + [Vibration]) on the main target (max 2)</style>\nIf [BulletPropellantAlly] (or [BulletPropellantSpecialAlly]) is at 0, Clash Power <style="highlight">+2</style>
   PL: [DuelCounter]\n<style="highlight">Moc Końcowa +1 za każde 4 (suma [Combustion] i [Vibration] głównego celu) (maks. 2)</style>\nPrzy 0 [BulletPropellantAlly] lub [BulletPropellantSpecialAlly] Moc Starcia <style="highlight">+2</style>
445. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Vibration] 1 부여 (턴당 2회)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Vibration] (2 times per turn)</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [Vibration] (2 razy na turę)</style>
446. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가 (턴당 2회)<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051204].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count (2 times per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Vibration] o 1 (2 razy na turę)<style="highlight"></style>
447. [Pasywka bojowa (od ulepszenia 1) — nazwa] 삽시호 [揷翅虎]
   źródło: Passives.json :: dataList[id=1051202].name
   limit: do 40 znaków
   EN: Chachihu [揷翅虎]
   PL: Chachihu [揷翅虎]
448. [Pasywka bojowa (od ulepszenia 1) — opis] 상시 적용 : [BulletPropellantAlly] 12개 보유\n\n[BulletPropellantAlly], [BulletPropellantSpecialAlly]을 소모하는 코인을 굴릴 때, 해당 특수 탄환이 없는 경우에도 공격을 취소하지 않는 대신 해당 코인의 적중 시 [Combustion] 부여, [Combustion] 횟수 증가 효과가 발동하지 않음\n\n이번 전투에서 처음으로 수비 스킬을 장착하였거나 [BulletPropellantAlly]을 전부 사용, 또는 흐트러졌다면, 해당 턴 종료 시 [BulletPropellantSpecialAlly] 8발을 장전하고 [IrritationAlly] 1 얻음 (전투당 1회)\n- 흐트러짐 상태에서 효과 발동 시, 흐트러짐 상태 해제 (강제 흐트러짐 제외)\n- [BulletPropellantAlly]이 남아있으면 전부 소멸\n- 자신이 소모한 [BulletPropellantAlly]과 [BulletPropellantSpecialAlly]의 합이 8 이상이면, [IrritationAlly]이 [HugeIrritationAlly]으로 변경\n\n[BulletPropellantSpecialAlly]의 마지막 탄환을 소모하는 기본 공격 스킬을 사용할 경우,\n- 공격 시작 전 공격 가중치 +2\n- 다음 턴에 [BeastEyesAlly] 1 얻음
   źródło: Passives.json :: dataList[id=1051202].desc
   limit: do 1390 znaków
   tokeny: zachowaj dokładnie: \n, [BulletPropellantAlly], [BulletPropellantSpecialAlly], [Combustion], [IrritationAlly], [HugeIrritationAlly], [BeastEyesAlly]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round; [Combustion] = 화상 / Burn; [IrritationAlly] = 천퇴성[天退星] / Tiantui Star [天退星]; [HugeIrritationAlly] = 신(心) - 천퇴성[天退星] / Shin (心) - Tiantui Star [天退星]; [BeastEyesAlly] = 오버히트 / Overheat
   EN: Always Active: begin Encounters with 12 [BulletPropellantAlly]\n\nWhen flipping a Coin that consumes [BulletPropellantAlly] or [BulletPropellantSpecialAlly]: while not having those 'Unique Ammo' does not cancel this unit's attacks, the Coin's On Hit "inflict [Combustion]" and "inflict [Combustion] Count" effects do not activate\n\nIf this unit equipped Defense Skills for the first time in this Encounter, or if this unit spent all of his [BulletPropellantAlly], or if this unit is Staggered: at the end of that turn, reload 8 [BulletPropellantSpecialAlly] and gain 1 [IrritationAlly] (once per Encounter)\n- If this effect activates while this unit is Staggered, recover from Stagger (excluding forced Staggers)\n- Remove all [BulletPropellantAlly] if this unit has any leftover [BulletPropellantAlly]\n- At 8+ (sum of [BulletPropellantAlly] and [BulletPropellantSpecialAlly] spent), convert [IrritationAlly] to [HugeIrritationAlly]\n\nWhen this unit uses a Base Attack Skill that spends the final Round of [BulletPropellantSpecialAlly]...\n- Gain Atk Weight +2 before attacking\n- Gain 1 [BeastEyesAlly] next turn
   PL: Zawsze aktywne: rozpoczyna spotkania z 12 [BulletPropellantAlly]\n\nPodczas rzutu monetą zużywającą [BulletPropellantAlly] lub [BulletPropellantSpecialAlly]: w braku tego „specjalnego amunicji” ataki nie zostają anulowane, lecz efekty przy trafieniu tej monety — „nakłada [Combustion]”, „zwiększa Licznik [Combustion]” — nie uruchamiają się\n\nJeżeli ta jednostka wyposażyła Umiejętności obrony po raz pierwszy w tym spotkaniu, zużyła całe [BulletPropellantAlly] albo jest Ogłuszona: na koniec tej tury przeładowuje 8 [BulletPropellantSpecialAlly] i zyskuje 1 [IrritationAlly] (1 raz na spotkanie)\n- Jeżeli efekt uruchomił się w stanie Oszołomienia, wydobywa się z Oszołomienia (z wyłączeniem wymuszonego Oszołomienia)\n- Jeżeli pozostało jej jakiekolwiek [BulletPropellantAlly], usuwa je wszystkie\n- Przy 8+ (suma zużytego [BulletPropellantAlly] i [BulletPropellantSpecialAlly]) zmienia [IrritationAlly] w [HugeIrritationAlly]\n\nGdy ta jednostka użyje podstawowej Umiejętności ataku zużywającej ostatni pocisk [BulletPropellantSpecialAlly],\n- Waga ataku +2 przed atakiem\n- Zyskuje 1 [BeastEyesAlly] w następnej turze
449. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — nazwa] 천퇴성도 [天退星刀]
   źródło: Passives.json :: dataList[id=1051201].name
   limit: do 40 znaków
   EN: Tiantui Star's Blade [天退星刀]
   PL: Ostrze Gwiazdy Tiantui [天退星刀]
450. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Sloth) — opis] [BulletPropellantAlly] 보유 시,\n- 1 이상이면 '쾌도난마'의 모든 코인이 [SuperCoin]으로 변경\n- [BulletPropellantAlly]을 소모하는 스킬 코인 위력 +1 (소모 가능한 만큼만 적용)\n\n[BulletPropellantSpecialAlly] 보유 시,\n- 1 이상이면 기본 공격 스킬의 모든 코인이 [SuperCoin]으로 변경\n- 0 이면 기본 공격 스킬의 특수 탄환을 소모할 수 있는 코인이 [SuperCoin]으로 변경\n- [BulletPropellantSpecialAlly]을 소모하는 스킬 코인 위력 +2 (소모 가능한 만큼만 적용)
   źródło: Passives.json :: dataList[id=1051201].desc
   limit: do 850 znaków
   tokeny: zachowaj dokładnie: \n, [BulletPropellantAlly], [SuperCoin], [BulletPropellantSpecialAlly]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round
   EN: When this unit has [BulletPropellantAlly]:\n- At 1+ [BulletPropellantAlly], convert all Coins of 'Tanglecleaver' into [SuperCoin]s\n- Skill Coins that spend [BulletPropellantAlly] gain +1 Power (activates only as long as the Coin has Rounds left to spend)\n\nWhen this unit has [BulletPropellantSpecialAlly]:\n- At 1+ [BulletPropellantSpecialAlly], convert all Coins of this unit's Base Attack Skills to [SuperCoin]s\n- At 0 [BulletPropellantSpecialAlly], convert all Coins of this unit's Base Attack Skills that spend 'Unique Ammo' to [SuperCoin]s\n- Skill Coins that spend [BulletPropellantSpecialAlly] gain +2 Power (activates only as long as the Coin has Rounds left to spend)
   PL: W posiadaniu [BulletPropellantAlly]:\n- Przy 1+ [BulletPropellantAlly] wszystkie monety „Tanglecleaver” zmieniają się w [SuperCoin]\n- Monety Umiejętności zużywające [BulletPropellantAlly] zyskują +1 Mocy (aktywne tylko, dopóki moneta ma pociski do zużycia)\n\nW posiadaniu [BulletPropellantSpecialAlly]:\n- Przy 1+ [BulletPropellantSpecialAlly] wszystkie monety podstawowych Umiejętności ataku tej jednostki zmieniają się w [SuperCoin]\n- Przy 0 [BulletPropellantSpecialAlly] wszystkie monety podstawowych Umiejętności ataku tej jednostki zużywające „specjalne amunicji” zmieniają się w [SuperCoin]\n- Monety Umiejętności zużywające [BulletPropellantSpecialAlly] zyskują +2 Mocy (aktywne tylko, dopóki moneta ma pociski do zużycia)
451. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Sloth) — nazwa] 천퇴성도 [天退星刀]
   źródło: Passives.json :: dataList[id=1051211].name
   (powtórzenie elementu 449 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Sloth) — opis] [BulletPropellantAlly] 보유 시,\n- 1 이상이면 '쾌도난마'의 모든 코인이 [SuperCoin]으로 변경\n- [BulletPropellantAlly]을 소모하는 스킬 코인 위력 +1, <style="highlight">피해량 +10%</style> (소모 가능한 만큼만 적용)\n\n[BulletPropellantSpecialAlly] 보유 시,\n- 1 이상이면 기본 공격 스킬의 모든 코인이 [SuperCoin]으로 변경\n- 0 이면 기본 공격 스킬의 특수 탄환을 소모할 수 있는 코인이 [SuperCoin]으로 변경\n- [BulletPropellantSpecialAlly]을 소모하는 스킬 코인 위력 +2, <style="highlight">피해량 +30%, 해당 코인으로 적중 시 부여하는 [Combustion] 위력과 [Combustion] 횟수 부여값 +2</style> (소모 가능한 만큼만 적용)
   źródło: Passives.json :: dataList[id=1051211].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BulletPropellantAlly], [SuperCoin], [BulletPropellantSpecialAlly], [Combustion]
   znaczenie tagów: [BulletPropellantAlly] = 호표탄 / Tigermark Round; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BulletPropellantSpecialAlly] = 맹호표탄 / Savage Tigermark Round; [Combustion] = 화상 / Burn
   EN: When this unit has [BulletPropellantAlly]:\n- At 1+ [BulletPropellantAlly], convert all Coins of 'Tanglecleaver' into [SuperCoin]s\n- Skill Coins that spend [BulletPropellantAlly] gain +1 Power <style="highlight">and deal +10% damage</style> (activates only as long as the Coin has Rounds left to spend)\n\nWhen this unit has [BulletPropellantSpecialAlly]:\n- At 1+ [BulletPropellantSpecialAlly], convert all Coins of this unit's Base Attack Skills to [SuperCoin]s\n- At 0 [BulletPropellantSpecialAlly], convert all Coins of this unit's Base Attack Skills that spend 'Unique Ammo' to [SuperCoin]s\n- Skill Coins that spend [BulletPropellantSpecialAlly] gain +2 Power, <style="highlight">deal +30% damage, and inflict +2 more [Combustion] Potency and [Combustion] Count On Hit with those Coins</style> (activates only as long as the Coin has Rounds left to spend)
   PL: W posiadaniu [BulletPropellantAlly]:\n- Przy 1+ [BulletPropellantAlly] wszystkie monety „Tanglecleaver” zmieniają się w [SuperCoin]\n- Monety Umiejętności zużywające [BulletPropellantAlly] zyskują +1 Mocy, <style="highlight">zadają +10% obrażeń</style> (aktywne tylko, dopóki moneta ma pociski do zużycia)\n\nW posiadaniu [BulletPropellantSpecialAlly]:\n- Przy 1+ [BulletPropellantSpecialAlly] wszystkie monety podstawowych Umiejętności ataku tej jednostki zmieniają się w [SuperCoin]\n- Przy 0 [BulletPropellantSpecialAlly] wszystkie monety podstawowych Umiejętności ataku tej jednostki zużywające „specjalne amunicji” zmieniają się w [SuperCoin]\n- Monety Umiejętności zużywające [BulletPropellantSpecialAlly] zyskują +2 Mocy, <style="highlight">zadają +30% obrażeń, a przy trafieniu tymi monetami nakładają o 2 więcej Mocy [Combustion] i Licznika [Combustion]</style> (aktywne tylko, dopóki moneta ma pociski do zużycia)
453. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — nazwa] 맹호의 도약
   źródło: Passives.json :: dataList[id=1051221].name
   limit: do 40 znaków
   EN: Savage Tiger's Lunge
   PL: Skok Savannego Tygrysa
454. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Sloth) — opis] 속도가 가장 빠른 아군 1명이 [Bullet]을 소모하는 스킬 사용 시 대상보다 속도가 3 이상 높다면, 가하는 피해량 +(대상과의 속도 차이 x 2)% (최대 10%)\n([Bullet]이 없으면 적용되지 않음. 단, [Bullet] 버프는 보유하였으나 수치가 0인 경우에는 효과가 적용됨)
   źródło: Passives.json :: dataList[id=1051221].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: When 1 ally with the fastest Speed uses a Skill that spends [Bullet], if their Speed is faster than the target's by 3 or more, deal +(Speed difference × 2)% more damage (max 10%).\n(This effect does not activate if the affected unit lacks the [Bullet] buff entirely. However, it will activate if they have the [Bullet] buff, even if they have 0 rounds left)
   PL: Gdy 1 Sojusznik z najwyższą Szybkością użyje Umiejętności zużywającej [Bullet], jeżeli jego Szybkość jest większa od celu o 3 lub więcej, zadaje +(różnica Szybkości x 2)% więcej obrażeń (maks. 10%).\n(Efekt nie uruchamia się, jeżeli dana jednostka nie ma wcale buffu [Bullet]. Uruchamia się jednak, gdy ją posiada, nawet przy 0 pozostałych pocisków)
455. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Sloth) — nazwa] 맹호의 도약
   źródło: Passives.json :: dataList[id=1051231].name
   (powtórzenie elementu 453 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Sloth) — opis] 속도가 가장 빠른 아군 1명이 [Bullet]을 소모하는 스킬 사용 시 대상보다 속도가 3 이상 높다면, 가하는 피해량 +(대상과의 속도 차이 x <style="highlight">3</style>)% (최대 <style="highlight">15%</style>)\n([Bullet]이 없으면 적용되지 않음. 단, [Bullet] 버프는 보유하였으나 수치가 0인 경우에는 효과가 적용됨)
   źródło: Passives.json :: dataList[id=1051231].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: When 1 ally with the fastest Speed uses a Skill that spends [Bullet], if their Speed is faster than the target's by 3 or more, deal +(Speed difference × <style="highlight">3</style>)% more damage (max <style="highlight">15%</style>).\n(This effect does not activate if the affected unit lacks the [Bullet] buff entirely. However, it will activate if they have the [Bullet] buff, even if they have 0 rounds left)
   PL: Gdy 1 Sojusznik z najwyższą Szybkością użyje Umiejętności zużywającej [Bullet], jeżeli jego Szybkość jest większa od celu o 3 lub więcej, zadaje +(różnica Szybkości x <style="highlight">3</style>)% więcej obrażeń (maks. <style="highlight">15%</style>).\n(Efekt nie uruchamia się, jeżeli dana jednostka nie ma wcale buffu [Bullet]. Uruchamia się jednak, gdy ją posiada, nawet przy 0 pozostałych pocisków)

## [000] The Prince of La Manchaland — Meursault — 라만차랜드 왕자
- ID Tożsamości: `10513` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 88 · szybkość: 2–5 / 3–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Rupture

457. [Karta Tożsamości — tytuł] 라만차랜드\n왕자
   źródło: Personalities.json :: dataList[id=10513].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Prince of La Manchaland
   PL: Książę\nLa Manchalandu
458. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10513].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10513].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Karta Tożsamości — opis] 뫼르소의 열세번째 인격
   źródło: Personalities.json :: dataList[id=10513].desc
   limit: do 120 znaków
   EN: Meursault’s 13th Identity
   PL: Trzynasta Tożsamość Meursaulta
461. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 행진 지휘
   źródło: Skills_personality-05.json :: dataList[id=1051301].levelList[level=1].name ; dataList[id=1051301].levelList[level=2].name ; dataList[id=1051301].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 2 · monety: 3 (+3)
   limit: do 40 znaków
   EN: March Conductor
   PL: Dyrygent Marszu
462. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신과 최대 체력이 가장 낮은 아군 1명에게 [BloodDinner]을 최대 10 소모하여, [BloodDinner] 5당 [BloodArmorMeursault] 1 부여 (턴당 1회, 최댓값인 대상 제외)\n- <라만차랜드>소속, <혈귀>(상위 권속)인 아군에게 우선 부여\n- 부여한 아군이 <라만차랜드>소속이면, [BloodArmorMeursault] 1 추가 부여\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음
   źródło: Skills_personality-05.json :: dataList[id=1051301].levelList[level=1].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodArmorMeursault], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] On self and 1 ally that has the lowest max HP: Consume up to 10 [BloodDinner] and apply 1 [BloodArmorMeursault] for every 5 [BloodDinner] this unit consumed (once per turn; excludes allies that have max Stack)\n- Prioritizes <La Manchaland> and <Bloodfiend>(Higher Kindred) allies\n- If the affected ally is from <La Manchaland>, this unit applies 1 additional [BloodArmorMeursault]\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]
   PL: [WhenUse] Na sobie i 1 Sojuszniku z najniższym Maks. HP zużywa do 10 [BloodDinner], nakładając 1 [BloodArmorMeursault] za każde 5 zużytego [BloodDinner] (1 raz na turę; wyłączając sojuszników z maks. stosem)\n- Namierza najpierw sojuszników z frakcji <La Manchaland> i <Krwiożerca>(Wyższy Pokrewny)\n- Jeżeli dotknięty sojusznik jest z frakcji <La Manchaland>, nakłada dodatkowo 1 [BloodArmorMeursault]\n- Jeżeli nie zdołała zużyć [BloodDinner], zyskuje 10 [Laceration]
463. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051301].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]
465. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신과 최대 체력이 가장 낮은 아군 1명에게 [BloodDinner]을 최대 10 소모하여, [BloodDinner] 5당 [BloodArmorMeursault] 1 부여 (턴당 1회, 최댓값인 대상 제외)\n- <라만차랜드>소속, <혈귀>(상위 권속)인 아군에게 우선 부여\n- 부여한 아군이 <라만차랜드>소속이면, [BloodArmorMeursault] 1 추가 부여\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음\n<style="highlight">[WhenUse] 대상의 [Laceration]이 4 이상이면 코인 위력 +1</style>
   źródło: Skills_personality-05.json :: dataList[id=1051301].levelList[level=2].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodArmorMeursault], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] On self and 1 ally that has the lowest max HP: Consume up to 10 [BloodDinner] and apply 1 [BloodArmorMeursault] for every 5 [BloodDinner] this unit consumed (once per turn; excludes allies that have max Stack)\n- Prioritizes <La Manchaland> and <Bloodfiend>(Higher Kindred) allies\n- If the affected ally is from <La Manchaland>, this unit applies 1 additional [BloodArmorMeursault]\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]\n<style="highlight">[WhenUse] If target has 4+ [Laceration], Coin Power +1</style>
   PL: [WhenUse] Na sobie i 1 Sojuszniku z najniższym Maks. HP zużywa do 10 [BloodDinner], nakładając 1 [BloodArmorMeursault] za każde 5 zużytego [BloodDinner] (1 raz na turę; wyłączając sojuszników z maks. stosem)\n- Namierza najpierw sojuszników z frakcji <La Manchaland> i <Krwiożerca>(Wyższy Pokrewny)\n- Jeżeli dotknięty sojusznik jest z frakcji <La Manchaland>, nakłada dodatkowo 1 [BloodArmorMeursault]\n- Jeżeli nie zdołała zużyć [BloodDinner], zyskuje 10 [Laceration]\n<style="highlight">[WhenUse] Jeżeli cel ma 4+ [Laceration], Moc Monet +1</style>
466. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1051301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Burst]<style="highlight"></style>
467. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Laceration] 횟수 1 증가</style>
   źródło: Skills_personality-05.json :: dataList[id=1051301].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack] Inflict +1 [Laceration] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 1</style>
468. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051301].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]<style="highlight"></style>
469. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신과 최대 체력이 가장 낮은 아군 1명에게 [BloodDinner]을 최대 10 소모하여, [BloodDinner] 5당 [BloodArmorMeursault] 1 부여 (턴당 1회, 최댓값인 대상 제외)\n- <라만차랜드>소속, <혈귀>(상위 권속)인 아군에게 우선 부여\n- 부여한 아군이 <라만차랜드>소속이면, [BloodArmorMeursault] 1 추가 부여\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음\n[WhenUse] 대상의 [Laceration]이 4 이상이면 코인 위력 +1\n<style="highlight">[WhenUse] 대상의 [Laceration] 횟수가 3 이상이면 최종 위력 +1</style>
   źródło: Skills_personality-05.json :: dataList[id=1051301].levelList[level=4].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodArmorMeursault], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] On self and 1 ally that has the lowest max HP: Consume up to 10 [BloodDinner] and apply 1 [BloodArmorMeursault] for every 5 [BloodDinner] this unit consumed (once per turn; excludes allies that have max Stack)\n- Prioritizes <La Manchaland> and <Bloodfiend>(Higher Kindred) allies\n- If the affected ally is from <La Manchaland>, this unit applies 1 additional [BloodArmorMeursault]\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]\n[WhenUse] If target has 4+ [Laceration], Coin Power +1\n<style="highlight">[WhenUse] If target has 3+ [Laceration] Count, Final Power +1</style>
   PL: [WhenUse] Na sobie i 1 Sojuszniku z najniższym Maks. HP zużywa do 10 [BloodDinner], nakładając 1 [BloodArmorMeursault] za każde 5 zużytego [BloodDinner] (1 raz na turę; wyłączając sojuszników z maks. stosem)\n- Namierza najpierw sojuszników z frakcji <La Manchaland> i <Krwiożerca>(Wyższy Pokrewny)\n- Jeżeli dotknięty sojusznik jest z frakcji <La Manchaland>, nakłada dodatkowo 1 [BloodArmorMeursault]\n- Jeżeli nie zdołała zużyć [BloodDinner], zyskuje 10 [Laceration]\n[WhenUse] Jeżeli cel ma 4+ [Laceration], Moc Monet +1\n<style="highlight">[WhenUse] Jeżeli cel ma 3+ Licznika [Laceration], Moc Końcowa +1</style>
470. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051301].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 1<style="highlight"></style>
471. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051301].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Laceration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Laceration]
472. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 재건의 의무
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=1].name ; dataList[id=1051302].levelList[level=2].name ; dataList[id=1051302].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Responsibility to Rebuild
   PL: Obowiązek Odbudowy
473. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신과 최대 체력이 가장 높은 아군 1명에게 [BloodDinner]을 최대 10 소모하여, [BloodDinner] 5당 [BloodArmorMeursault] 1 부여 (턴당 1회, 최댓값인 대상 제외)\n- <라만차랜드>소속, <혈귀>(상위 권속)인 아군에게 우선 부여\n- 부여한 아군이 <라만차랜드>소속이면, [BloodArmorMeursault] 1 추가 부여\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=1].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BloodDinner], [BloodArmorMeursault], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] On self and 1 ally that has the highest max HP: Consume up to 10 [BloodDinner] and apply 1 [BloodArmorMeursault] for every 5 [BloodDinner] this unit consumed (once per turn; excludes allies that have max Stack)\n- Prioritizes <La Manchaland> and <Bloodfiend>(Higher Kindred) allies\n- If the affected ally is from <La Manchaland>, this unit applies 1 additional [BloodArmorMeursault]\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]
   PL: [WhenUse] Na sobie i 1 Sojuszniku z najwyższym Maks. HP zużywa do 10 [BloodDinner], nakładając 1 [BloodArmorMeursault] za każde 5 zużytego [BloodDinner] (1 raz na turę; wyłączając sojuszników z maks. stosem)\n- Namierza najpierw sojuszników z frakcji <La Manchaland> i <Krwiożerca>(Wyższy Pokrewny)\n- Jeżeli dotknięty sojusznik jest z frakcji <La Manchaland>, nakłada dodatkowo 1 [BloodArmorMeursault]\n- Jeżeli nie zdołała zużyć [BloodDinner], zyskuje 10 [Laceration]
474. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1051302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Laceration]
475. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신과 최대 체력이 가장 높은 아군 1명에게 [BloodDinner]을 최대 10 소모하여, [BloodDinner] 5당 [BloodArmorMeursault] 1 부여 (턴당 1회, 최댓값인 대상 제외)\n- <라만차랜드>소속, <혈귀>(상위 권속)인 아군에게 우선 부여\n- 부여한 아군이 <라만차랜드>소속이면, [BloodArmorMeursault] 1 추가 부여\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음\n<style="highlight">[WhenUse] 대상의 [Laceration] 4당 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [Laceration] 횟수가 3 이상이면, 최종 위력 +1</style>
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=2].desc
   limit: do 750 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodArmorMeursault], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] On self and 1 ally that has the highest max HP: Consume up to 10 [BloodDinner] and apply 1 [BloodArmorMeursault] for every 5 [BloodDinner] this unit consumed (once per turn; excludes allies that have max Stack)\n- Prioritizes <La Manchaland> and <Bloodfiend>(Higher Kindred) allies\n- If the affected ally is from <La Manchaland>, this unit applies 1 additional [BloodArmorMeursault]\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]\n<style="highlight">[WhenUse] Coin Power +1 for every 4 [Laceration] on target (max 2)\n[WhenUse] If target has 3+ [Laceration] Count, Final Power +1</style>
   PL: [WhenUse] Na sobie i 1 Sojuszniku z najwyższym Maks. HP zużywa do 10 [BloodDinner], nakładając 1 [BloodArmorMeursault] za każde 5 zużytego [BloodDinner] (1 raz na turę; wyłączając sojuszników z maks. stosem)\n- Namierza najpierw sojuszników z frakcji <La Manchaland> i <Krwiożerca>(Wyższy Pokrewny)\n- Jeżeli dotknięty sojusznik jest z frakcji <La Manchaland>, nakłada dodatkowo 1 [BloodArmorMeursault]\n- Jeżeli nie zdołała zużyć [BloodDinner], zyskuje 10 [Laceration]\n<style="highlight">[WhenUse] Moc Monet +1 za każde 4 [Laceration] celu (maks. 2)\n[WhenUse] Jeżeli cel ma 3+ Licznika [Laceration], Moc Końcowa +1</style>
478. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 471 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Burst]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Burst]
480. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신과 최대 체력이 가장 높은 아군 1명에게 [BloodDinner]을 최대 10 소모하여, [BloodDinner] 5당 [BloodArmorMeursault] 1 부여 (턴당 1회, 최댓값인 대상 제외)\n- <라만차랜드>소속, <혈귀>(상위 권속)인 아군에게 우선 부여\n- 부여한 아군이 <라만차랜드>소속이면, [BloodArmorMeursault] 1 추가 부여\n- [BloodDinner]을 소모하지 못했으면, [Laceration] 10 얻음\n[WhenUse] 대상의 [Laceration] 4당 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [Laceration] 횟수 3<style="highlight">당 최종 위력 +1 (최대 2)</style>\n<style="highlight">[WhenUse] 자신의 [BloodArmorMeursault] 1당 피해량 +10% (최대 30%)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=4].desc
   limit: do 860 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BloodDinner], [BloodArmorMeursault], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BloodDinner] = 혈찬 / Bloodfeast; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] On self and 1 ally that has the highest max HP: Consume up to 10 [BloodDinner] and apply 1 [BloodArmorMeursault] for every 5 [BloodDinner] this unit consumed (once per turn; excludes allies that have max Stack)\n- Prioritizes <La Manchaland> and <Bloodfiend>(Higher Kindred) allies\n- If the affected ally is from <La Manchaland>, this unit applies 1 additional [BloodArmorMeursault]\n- If this unit failed to consume [BloodDinner], gain 10 [Laceration]\n[WhenUse] Coin Power +1 for every 4 [Laceration] on target (max 2)\n[WhenUse] <style="highlight">Final Power +1 for every 3 [Laceration] Count on target (max 2)</style>\n<style="highlight">[WhenUse] Deal +10% damage for every [BloodArmorMeursault] on self (max 30%)</style>
   PL: [WhenUse] Na sobie i 1 Sojuszniku z najwyższym Maks. HP zużywa do 10 [BloodDinner], nakładając 1 [BloodArmorMeursault] za każde 5 zużytego [BloodDinner] (1 raz na turę; wyłączając sojuszników z maks. stosem)\n- Namierza najpierw sojuszników z frakcji <La Manchaland> i <Krwiożerca>(Wyższy Pokrewny)\n- Jeżeli dotknięty sojusznik jest z frakcji <La Manchaland>, nakłada dodatkowo 1 [BloodArmorMeursault]\n- Jeżeli nie zdołała zużyć [BloodDinner], zyskuje 10 [Laceration]\n[WhenUse] Moc Monet +1 za każde 4 [Laceration] celu (maks. 2)\n[WhenUse] <style="highlight">Moc Końcowa +1 za każde 3 Licznika [Laceration] celu (maks. 2)</style>\n<style="highlight">[WhenUse] Zadaje +10% obrażeń za każde 1 [BloodArmorMeursault] (maks. 30%)</style>
481. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o <style="highlight">2</style>
482. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] Inflict +1 [Burst] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada +1 Licznika [Burst]</style>
483. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]<style="highlight"></style>
484. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Burst]<style="highlight"></style>
485. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [ScarletTakeDamageUp] 1 부여 (턴당 2회)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051302].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ScarletTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ScarletTakeDamageUp] = 색욕 취약 / Lust Fragility
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [ScarletTakeDamageUp] next turn (2 times per turn)</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada w następnej turze 1 [ScarletTakeDamageUp] (2 razy na turę)</style>
486. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 피를 굳히고, 나와 당신에게 두른다.
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=3].name ; dataList[id=1051303].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 60 znaków
   EN: Let us wear the coagulated mantle of blood.
   PL: Ujarzmijmy Skrzepniętą Krew i przyodziejmy ją sobie nawzajem
487. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 40%만큼 체력 회복 (스킬당 최대 50)\n[BeforeUse] 자신의 [BloodArmorMeursault]가 5면, ‘오베르튜레’로 발동됨\n[WhenUse] 대상의 [Laceration] 6당 코인 위력 +1 (최대 2)\n[WhenUse] 자신과 아군 (최대 공명 수)명에게 [BloodArmorMeursault] 1 부여 (턴당 2회, 아군 최대 4명, <라만차랜드>, <혈귀>(상위 권속) 순서로 우선 적용, 최댓값인 대상 제외)\n[EndSkill] 대상이 사망한 경우, [BloodDinner] 20 추가 증가 (턴당 1회)
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=3].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [BloodArmorMeursault], [WhenUse], [Laceration], [EndSkill], [BloodDinner]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [BloodDinner] = 혈찬 / Bloodfeast
   EN: On Hit with this Skill: Heal 40% of the HP damage dealt (max 50 per Skill)\n[BeforeUse] At 5 [BloodArmorMeursault], activate "Ouvertüre" instead\n[WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)\n[WhenUse] Apply 1 [BloodArmorMeursault] to self and (highest Reson.) allies (2 times per turn; up to 4 allies; prioritizes <La Manchaland> first, and <Bloodfiend>(Higher Kindreds) second; excludes allies that have max Stack)\n[EndSkill] If the target is defeated, increase [BloodDinner] by additional 20 (once per turn)
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 40% zadanych obrażeń HP (maks. 50 na Umiejętność)\n[BeforeUse] Przy 5 [BloodArmorMeursault] uruchamia się jako „Ouvertüre”\n[WhenUse] Moc Monet +1 za każde 6 [Laceration] celu (maks. 2)\n[WhenUse] Nakłada 1 [BloodArmorMeursault] na siebie i (najwyższy Rezonans / N) sojuszników (2 razy na turę; maks. 4 sojuszników; najpierw <La Manchaland>, następnie <Krwiożerca>(Wyżsi Pokrewni); wyłączając sojuszników z maks. stosem)\n[EndSkill] Jeżeli cel zostanie pokonany, zwiększa [BloodDinner] dodatkowo o 20 (1 raz na turę)
488. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1051303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1051303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]
490. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1051303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1051303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]
492. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1051303].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1051303].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
494. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [ParadeConcentration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ParadeConcentration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ParadeConcentration] = 라만차 퍼레이드 / La Mancha Parade
   EN: [OnSucceedAttack] Inflict 1 [ParadeConcentration]
   PL: [OnSucceedAttack] Nakłada 1 [ParadeConcentration]
495. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [ParadeConcentration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=3].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ParadeConcentration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ParadeConcentration] = 라만차 퍼레이드 / La Mancha Parade
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [ParadeConcentration] next turn
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada w następnej turze 1 [ParadeConcentration]
496. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 40%만큼 체력 회복 (스킬당 최대 <style="highlight">80</style>)\n[BeforeUse] 자신의 [BloodArmorMeursault]가 5면, ‘오베르튜레’로 발동됨\n[WhenUse] 대상의 [Laceration] 6당 코인 위력 +1 (최대 2)\n<style="highlight">[WhenUse] 대상의 [Laceration] 횟수 2당 피해량 +10% (최대 40%)</style>\n[WhenUse] 자신과 아군 (최대 공명 수)명에게 [BloodArmorMeursault] 1 부여 (턴당 2회, 아군 최대 4명, <라만차랜드>, <혈귀>(상위 권속) 순서로 우선 적용, 최댓값인 대상 제외)\n<style="highlight">- 색욕 공명이면, 최대 체력이 가장 낮은 아군 2명에게 [BloodArmorMeursault] 2 추가 부여</style>\n[EndSkill] 대상이 사망한 경우, [BloodDinner] 20 추가 증가 (턴당 1회)
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=4].desc
   limit: do 900 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeUse], [BloodArmorMeursault], [WhenUse], [Laceration], [EndSkill], [BloodDinner]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [BloodDinner] = 혈찬 / Bloodfeast
   EN: On Hit with this Skill: Heal 40% of the HP damage dealt (max <style="highlight">80</style> per Skill)\n[BeforeUse] At 5 [BloodArmorMeursault], activate "Ouvertüre" instead\n[WhenUse] Coin Power +1 for every 6 [Laceration] on target (max 2)\n<style="highlight">[WhenUse] Deal +10% damage for every 2 [Laceration] Count on target (max 40%)</style>\n[WhenUse] Apply 1 [BloodArmorMeursault] to self and (highest Reson.) allies (2 times per turn; up to 4 allies; prioritizes <La Manchaland> first, and <Bloodfiend>(Higher Kindreds) second; excludes allies that have max Stack)\n<style="highlight">- If it was a Lust Reson., apply 2 [BloodArmorMeursault] to 2 allies that have the lowest max HP as well</style>\n[EndSkill] If the target is defeated, increase [BloodDinner] by additional 20 (once per turn)
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 40% zadanych obrażeń HP (maks. <style="highlight">80</style> na Umiejętność)\n[BeforeUse] Przy 5 [BloodArmorMeursault] uruchamia się jako „Ouvertüre”\n[WhenUse] Moc Monet +1 za każde 6 [Laceration] celu (maks. 2)\n<style="highlight">[WhenUse] Zadaje +10% obrażeń za każde 2 Licznika [Laceration] celu (maks. 40%)</style>\n[WhenUse] Nakłada 1 [BloodArmorMeursault] na siebie i (najwyższy Rezonans / N) sojuszników (2 razy na turę; maks. 4 sojuszników; najpierw <La Manchaland>, następnie <Krwiożerca>(Wyżsi Pokrewni); wyłączając sojuszników z maks. stosem)\n<style="highlight">- Jeżeli był to Rezonans Żądzy, nakłada dodatkowo 2 [BloodArmorMeursault] na 2 sojuszników z najniższym Maks. HP</style>\n[EndSkill] Jeżeli cel zostanie pokonany, zwiększa [BloodDinner] dodatkowo o 20 (1 raz na turę)
497. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Laceration] 2 부여</style>
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack] Inflict 2 [Laceration]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 2 [Laceration]</style>
498. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [ParadeConcentration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ParadeConcentration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ParadeConcentration] = 라만차 퍼레이드 / La Mancha Parade
   EN: [OnSucceedAttack] Inflict 1 [ParadeConcentration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [ParadeConcentration]<style="highlight"></style>
499. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [ParadeConcentration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051303].levelList[level=4].coinlist[#3].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [ParadeConcentration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ParadeConcentration] = 라만차 퍼레이드 / La Mancha Parade
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [ParadeConcentration] next turn<style="highlight"></style>
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada w następnej turze 1 [ParadeConcentration]<style="highlight"></style>
500. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 오베르튜레
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=3].name ; dataList[id=1051305].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Ouvertüre
   PL: Ouvertüre
501. [Umiejętność 4 (×0) (ulepszenie 3) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (스킬당 최대 85)\n[WhenUse] 메인 대상의 [Laceration] 3당 합 위력 +2 (최대 8)\n[WhenUse] 메인 대상의 [Laceration] 횟수 2당 피해량 +5% (최대 20%)\n[WhenUse] 본인을 제외한 아군 (최대 공명 수)명에게 [BloodArmorMeursault] 2 부여 (최대 4명, <라만차랜드>, <혈귀>(상위 권속) 순서로 우선 적용, 최댓값인 대상 제외)\n[EndSkill] 자신의 [BloodArmorMeursault] 전부 소모\n[EndSkill] 이 스킬로 공격 대상이 사망한 경우, 사망 인원 1명당 혈찬 10 추가 증가 (턴당 1회)
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=3].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BloodArmorMeursault], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: Heal 50% of the HP damage dealt (max 85 per Skill)\n[WhenUse] Clash Power +2 for every 3 [Laceration] on the main target (max 8)\n[WhenUse] Deal +5% damage for every 2 [Laceration] Count on the main target (max 20%)\n[WhenUse] Apply 2 [BloodArmorMeursault] to (highest Reson.) other allies (max 4 allies; prioritizes <La Manchaland> first, and <Bloodfiend>(Higher Kindreds) second; excludes allies that have max Stack)\n[EndSkill] Consume all [BloodArmorMeursault] on self\n[EndSkill] If this Skill defeated a target, additionally increase Bloodfeast by 10 for every target defeated by this Skill (once per turn)
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 50% zadanych obrażeń HP (maks. 85 na Umiejętność)\n[WhenUse] Moc Starcia +2 za każde 3 [Laceration] głównego celu (maks. 8)\n[WhenUse] Zadaje +5% obrażeń za każde 2 Licznika [Laceration] głównego celu (maks. 20%)\n[WhenUse] Nakłada 2 [BloodArmorMeursault] na (najwyższy Rezonans / N) innych sojuszników (maks. 4 sojuszników; najpierw <La Manchaland>, następnie <Krwiożerca>(Wyżsi Pokrewni); wyłączając sojuszników z maks. stosem)\n[EndSkill] Zużywa całe własne [BloodArmorMeursault]\n[EndSkill] Jeżeli ta Umiejętność pokonała cel, zwiększa Krwawą Ucztę dodatkowo o 10 za każdego pokonanego (1 raz na turę)
502. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1051305].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 2
503. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1051305].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1051305].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1051305].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 493 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1051305].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada 2 [Laceration]
507. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1051305].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Burst]
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada 1 [Burst]
508. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1051305].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 493 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [ParadeConcentration] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1051305].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ParadeConcentration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ParadeConcentration] = 라만차 퍼레이드 / La Mancha Parade
   EN: [OnSucceedAttack] Inflict 2 [ParadeConcentration]
   PL: [OnSucceedAttack] Nakłada 2 [ParadeConcentration]
510. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 이 스킬 피해로 대상을 흐트러짐, 부위 파괴, 처치했다면, 대상 1명당 다음 턴에 [BloodArmorMeursault] 1 얻음 (최대 3)
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=3].coinlist[#3].coindescs[#2].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [BloodArmorMeursault]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor
   EN: [UnBrokenCoinOnSucceedAttack] Gain 1 [BloodArmorMeursault] next turn for every target this Skill's damage Staggered, Part Broke, or defeated (max 3)
   PL: [UnBrokenCoinOnSucceedAttack] Jeżeli obrażenia tej Umiejętności Ogłuszyły cel, zniszczyły część ciała albo go pokonały, zyskuje w nast. turze 1 [BloodArmorMeursault] za taki cel (maks. 3)
511. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 이 스킬에서 적중 시, 입힌 체력 피해량의 50%만큼 체력 회복 (스킬당 최대 <style="highlight">100</style>)\n[WhenUse] 메인 대상의 [Laceration] 3당 합 위력 +2 (최대 8)\n[WhenUse] 메인 대상의 [Laceration] 횟수 2당 피해량 <style="highlight">+10% (최대 40%)</style>\n[WhenUse] 본인을 제외한 아군 (최대 공명 수)명에게 [BloodArmorMeursault] 2 부여 (최대 4명, <라만차랜드>, <혈귀>(상위 권속) 순서로 우선 적용, 최댓값인 대상 제외)\n<style="highlight">- 색욕 공명이면, [BloodArmorMeursault] 1 추가 부여</style>\n[EndSkill] 자신의 [BloodArmorMeursault] 전부 소모\n[EndSkill] 이 스킬로 공격 대상이 사망한 경우, 사망 인원 1명당 혈찬 10 추가 증가 (턴당 1회)
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=4].desc
   limit: do 890 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [BloodArmorMeursault], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: On Hit with this Skill: Heal 50% of the HP damage dealt (max <style="highlight">100</style> per Skill)\n[WhenUse] Clash Power +2 for every 3 [Laceration] on the main target (max 8)\n[WhenUse] Deal +<style="highlight">10</style>% damage for every 2 [Laceration] Count on the main target (max <style="highlight">40</style>%)\n[WhenUse] Apply 2 [BloodArmorMeursault] to (highest Reson.) other allies (max 4 allies; prioritizes <La Manchaland> first, and <Bloodfiend>(Higher Kindreds) second; excludes allies that have max Stack)\n<style="highlight">- If it was a Lust Reson., apply 1 additional [BloodArmorMeursault]</style>\n[EndSkill] Consume all [BloodArmorMeursault] on self\n[EndSkill] If this Skill defeated a target, additionally increase Bloodfeast by 10 for every target defeated by this Skill (once per turn)
   PL: Przy trafieniu tą Umiejętnością odzyskuje HP równe 50% zadanych obrażeń HP (maks. <style="highlight">100</style> na Umiejętność)\n[WhenUse] Moc Starcia +2 za każde 3 [Laceration] głównego celu (maks. 8)\n[WhenUse] Zadaje +<style="highlight">10</style>% obrażeń za każde 2 Licznika [Laceration] głównego celu (maks. <style="highlight">40</style>%)\n[WhenUse] Nakłada 2 [BloodArmorMeursault] na (najwyższy Rezonans / N) innych sojuszników (maks. 4 sojuszników; najpierw <La Manchaland>, następnie <Krwiożerca>(Wyżsi Pokrewni); wyłączając sojuszników z maks. stosem)\n<style="highlight">- Jeżeli był to Rezonans Żądzy, nakłada dodatkowo 1 [BloodArmorMeursault]</style>\n[EndSkill] Zużywa całe własne [BloodArmorMeursault]\n[EndSkill] Jeżeli ta Umiejętność pokonała cel, zwiększa Krwawą Ucztę dodatkowo o 10 za każdego pokonanego (1 raz na turę)
512. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 3 — opis] <style="highlight">- 자신의 [FocusOnActing]이 2 이상이면, 공격 대상 중 1명에게 [ParadeConcentration] 2 추가 부여 (턴당 1회)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [FocusOnActing], [ParadeConcentration]
   znaczenie tagów: [FocusOnActing] = 연기 집중 / Focused Performance; [ParadeConcentration] = 라만차 퍼레이드 / La Mancha Parade
   EN: <style="highlight">- At 2+ [FocusOnActing], also inflict 2 [ParadeConcentration] to 1 of the targets (once per turn)</style>
   PL: <style="highlight">- Przy 2+ [FocusOnActing] nakłada dodatkowo 2 [ParadeConcentration] na 1 z celów (1 raz na turę)</style>
513. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 이 스킬 피해로 대상을 흐트러짐, 부위 파괴, 처치했다면, 대상 1명당 다음 턴에 [BloodArmorMeursault] 1 얻음 (최대 3)<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051305].levelList[level=4].coinlist[#3].coindescs[#3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [UnBrokenCoinOnSucceedAttack], [BloodArmorMeursault]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor
   EN: [UnBrokenCoinOnSucceedAttack] Gain 1 [BloodArmorMeursault] next turn for every target this Skill's damage Staggered, Part Broke, or defeated (max 3)<style="highlight"></style>
   PL: [UnBrokenCoinOnSucceedAttack] Jeżeli obrażenia tej Umiejętności Ogłuszyły cel, zniszczyły część ciała albo go pokonały, zyskuje w nast. turze 1 [BloodArmorMeursault] za taki cel (maks. 3)<style="highlight"></style>
514. [Obrona (ulepszenia 1,4) — nazwa] 피 굳히기
   źródło: Skills_personality-05.json :: dataList[id=1051304].levelList[level=1].name ; dataList[id=1051304].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Coagulation
   PL: Krzepnięcie Krwi
515. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WinDuel] [BloodArmorMeursault] 1 얻음 (턴당 2회)
   źródło: Skills_personality-05.json :: dataList[id=1051304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WinDuel], [BloodArmorMeursault]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WinDuel] = [합 승리시] / [Clash Win]; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor
   EN: [DuelCounter]\n[WinDuel] Gain 1 [BloodArmorMeursault] (2 times per turn)
   PL: [DuelCounter]\n[WinDuel] Zyskuje 1 [BloodArmorMeursault] (2 razy na turę)
516. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051304].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1051304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n<style="highlight">[WhenUse] 본인을 포함한 아군 2명에게 [Laceration] 5 부여하고 1회 발동, [Laceration] 횟수 1 감소. (턴당 1회, [BloodArmorMeursault]를 가장 많이 보유한 아군 우선 적용, 상위 권속 제외, 이 피해로 체력이 1 미만으로 감소하지 않음)</style>\n[WinDuel] [BloodArmorMeursault] 1 얻음 (턴당 2회)
   źródło: Skills_personality-05.json :: dataList[id=1051304].levelList[level=4].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [WhenUse], [Laceration], [BloodArmorMeursault], [WinDuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [DuelCounter]\n<style="highlight">[WhenUse] To 2 allies, including this unit, apply 5 [Laceration] and activate it once; then, reduce their [Laceration] Count by 1 (once per turn; prioritizes allies that have the most [BloodArmorMeursault]; does not activate for Higher Kindreds; this damage does not reduce the allies' HP below 1)</style>\n[WinDuel] Gain 1 [BloodArmorMeursault] (2 times per turn)
   PL: [DuelCounter]\n<style="highlight">[WhenUse] Nakłada 5 [Laceration] na 2 sojuszników, łącznie z tą jednostką, i aktywuje go 1 raz; następnie zmniejsza ich Licznik [Laceration] o 1 (1 raz na turę; najpierw sojusznicy z największą liczbą [BloodArmorMeursault]; nie uruchamia się u Wyższych Pokrewnych; te obrażenia nie obniżają HP sojuszników poniżej 1)</style>\n[WinDuel] Zyskuje 1 [BloodArmorMeursault] (2 razy na turę)
518. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Laceration] 1 부여</style>
   źródło: Skills_personality-05.json :: dataList[id=1051304].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Laceration]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [Laceration]</style>
519. [Pasywka bojowa (od ulepszenia 1) — nazwa] 혈찬
   źródło: Passives.json :: dataList[id=1051302].name
   limit: do 40 znaków
   EN: Bloodfeast
   PL: Krwawa Uczta
520. [Pasywka bojowa (od ulepszenia 1) — opis] 이 캐릭터가 전투에 등장해 있거나, 등장할 리스트에 포함되어 있으면, 1턴부터 모든 캐릭터가 받은 [Laceration] 피해만큼 [BloodDinner]이 증가함.\n이 캐릭터가 전투에 등장할 때 전장에 흩뿌려진 잠재된 피가 더욱 드러난다.
   źródło: Passives.json :: dataList[id=1051302].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: If this unit is on field, or is one of the units that can appear on this Stage, increase [BloodDinner] value by the amount of [Laceration] damage collectively received by every unit. \nWhen this unit enters the field, the sleeping blood drenching the battlefield will rise above the surface.
   PL: Jeżeli ta jednostka jest na polu albo znajduje się wśród jednostek mogących wejść na pole w tym spotkaniu, od 1. tury zwiększa [BloodDinner] o wartość obrażeń [Laceration] otrzymanych łącznie przez wszystkie jednostki.\nGdy ta jednostka wchodzi na pole, śpiąca krew przesiąkająca pole bitwy wynurza się na powierzchnię.
521. [Pasywka bojowa (od ulepszenia 1) — nazwa] 왕자였던 자가 해야하는 일
   źródło: Passives.json :: dataList[id=1051303].name
   limit: do 50 znaków
   EN: Responsibility of a Former Prince
   PL: Obowiązek Byłego Księcia
522. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 시작 시 [BloodArmorMeursault]가 최대인 라만차랜드 소속 인격에게 아래 효과 적용\n· [FocusOnActing] 1 얻음\n· 피해로 인한 흐트러짐 상태일 때, 흐트러짐 해제하고 [BloodArmorMeursault] 전부 소모 (스테이지 및 인격당 1회, 강제 흐트러짐 제외)\n\n전투 인원에 라만차랜드 공주 로쟈가 있다면, 라만차랜드 공주 로쟈와 라만차랜드 왕자 뫼르소의 스킬 3 피해량 +15% (강화 스킬 포함)
   źródło: Passives.json :: dataList[id=1051303].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n, [BloodArmorMeursault], [FocusOnActing]
   znaczenie tagów: [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [FocusOnActing] = 연기 집중 / Focused Performance
   EN: Turn Start: The following effects activate for La Manchaland Identities that have max [BloodArmorMeursault] Stack\n· Gain 1 [FocusOnActing]\n· When Staggered due to damage, recover from Stagger; then, consume all [BloodArmorMeursault] on self (once per Stage per Identity; excluding forced Staggers)\n\nIf The Princess of La Manchaland Rodion is on the field, she and The Prince of La Manchaland Meursault both deal +15% damage using their Skill 3 (including Empowered Skills)
   PL: Na początku tury stosuje poniższe efekty na Tożsamościach La Manchaland z maksymalnym stosem [BloodArmorMeursault]\n· Zyskuje 1 [FocusOnActing]\n· W stanie Oszołomienia od obrażeń wydobywa się z Oszołomienia, po czym zużywa całe własne [BloodArmorMeursault] (1 raz na spotkanie per Tożsamość; z wyłączeniem wymuszonego Oszołomienia)\n\nJeżeli na polu znajduje się Rodion, Księżniczka La Manchalandu, ona i Meursault, Książę La Manchalandu zadają +15% obrażeń Umiejętnością 3 (łącznie z Umiejętnościami Wzmocnionymi)
523. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 뫼르소와 로쟈의 스킬 3 피해량 +15%
   źródło: Passives.json :: dataList[id=1051303].summary
   limit: do 120 znaków
   EN: Meursault & Rodion deal +15% damage with their Skill 3
   PL: Meursault i Rodion zadają +15% obrażeń Umiejętnością 3
524. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust, posiadane 3× Pride) — nazwa] ‘피를 두르고, 가면을 쓰고, 피가 명하는 대로’
   źródło: Passives.json :: dataList[id=1051301].name
   limit: do 60 znaków
   EN: 'Bloodied, Masked, and as Blood Commands'
   PL: „Ukoronowani Krwią, Zamaskowani, i wedle Rozkazu Krwi”
525. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust, posiadane 3× Pride) — opis] 전투 시작 시 자신에게 [BloodArmorMeursault]가 있으면, 수치에 따라 아래 효과를 얻음\n- 3 ~ : [AttackUp] 1, [DefenseUp] 1\n- 4 ~ : 다음 턴에 [Agility] 1\n\n[Laceration]을 보유한 적에게 공격 적중 시 자신의 체력이 30% 미만이면, 자신의 최대 체력의 30%만큼 체력 회복 (전투당 1회, 소수점 버림)
   źródło: Passives.json :: dataList[id=1051301].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [BloodArmorMeursault], [AttackUp], [DefenseUp], [Agility], [Laceration]
   znaczenie tagów: [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Agility] = 신속 / Haste; [Laceration] = 출혈 / Bleed
   EN: Combat Start: if this unit has [BloodArmorMeursault], gain the following effects based on Stack:\n- At 3+ Stack: gain 1 [AttackUp] and 1 [DefenseUp]\n- At 4+ Stack: gain 1 [Agility] next turn\n\nOn Hit against enemies that have [Laceration]: if this unit has less than 30% HP, heal 30% HP (once per Encounter; rounded down)
   PL: Na początku walki jeżeli ma [BloodArmorMeursault], zyskuje poniższe efekty zależnie od stosu:\n- Przy stosie 3+: zyskuje 1 [AttackUp] i 1 [DefenseUp]\n- Przy stosie 4+: zyskuje 1 [Agility] w następnej turze\n\nPrzy trafieniu wrogów z [Laceration] jeżeli ma mniej niż 30% HP, odzyskuje 30% Maks. HP (1 raz na spotkanie; zaokrąglone w dół)
526. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust, posiadane 3× Pride) — podsumowanie] 조건 만족 시, 자신의 최대 체력의 30%만큼 체력 회복
   źródło: Passives.json :: dataList[id=1051301].summary
   limit: do 120 znaków
   EN: If conditions are met, heal 30% HP
   PL: Jeżeli warunki są spełnione, odzyskuje 30% HP
527. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust, posiadane 3× Pride) — nazwa] ‘피를 두르고, 가면을 쓰고, 피가 명하는 대로’
   źródło: Passives.json :: dataList[id=1051311].name
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust, posiadane 3× Pride) — opis] 전투 시작 시 자신에게 [BloodArmorMeursault]가 있으면, 수치에 따라 아래 효과를 얻음\n- 3 ~ : [AttackUp] <style="highlight">2</style>, [DefenseUp] <style="highlight">2</style>\n- 4 ~ : 다음 턴에 [Agility] <style="highlight">2</style>\n\n<style="highlight">전투 시작 시 자신에게 [FocusOnActing]이 있으면, 적에게 공격 적중 시 [ParadeConcentration] 1 부여 (턴당 2회, E.G.O 스킬 포함)</style>\n\n[Laceration]을 보유한 적에게 공격 적중 시 자신의 체력이 30% 미만이면, 자신의 최대 체력의 30%만큼 체력 회복 (전투당 1회, 소수점 버림)
   źródło: Passives.json :: dataList[id=1051311].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BloodArmorMeursault], [AttackUp], [DefenseUp], [Agility], [FocusOnActing], [ParadeConcentration], [Laceration]
   znaczenie tagów: [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Agility] = 신속 / Haste; [FocusOnActing] = 연기 집중 / Focused Performance; [ParadeConcentration] = 라만차 퍼레이드 / La Mancha Parade; [Laceration] = 출혈 / Bleed
   EN: Combat Start: if this unit has [BloodArmorMeursault], gain the following effects based on Stack:\n- At 3+ Stack: gain <style="highlight">2</style> [AttackUp] and <style="highlight">2</style> [DefenseUp]\n- At 4+ Stack: gain <style="highlight">2</style> [Agility] next turn\n\n<style="highlight">Combat Start: if this unit has [FocusOnActing], inflict 1 [ParadeConcentration] On Hit against enemies (2 times per turn; including E.G.O Skills)</style>\n\nOn Hit against enemies that have [Laceration]: if this unit has less than 30% HP, heal 30% HP (once per Encounter; rounded down)
   PL: Na początku walki jeżeli ma [BloodArmorMeursault], zyskuje poniższe efekty zależnie od stosu:\n- Przy stosie 3+: zyskuje <style="highlight">2</style> [AttackUp] i <style="highlight">2</style> [DefenseUp]\n- Przy stosie 4+: zyskuje <style="highlight">2</style> [Agility] w następnej turze\n\n<style="highlight">Na początku walki jeżeli ma [FocusOnActing], przy trafieniu wrogów nakłada 1 [ParadeConcentration] (2 razy na turę; łącznie z Umiejętnościami E.G.O)</style>\n\nPrzy trafieniu wrogów z [Laceration] jeżeli ma mniej niż 30% HP, odzyskuje 30% Maks. HP (1 raz na spotkanie; zaokrąglone w dół)
529. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust, posiadane 3× Pride) — podsumowanie] 조건 만족 시, [ParadeConcentration] 1 부여\n조건 만족 시, 자신의 최대 체력의 30%만큼 체력 회복
   źródło: Passives.json :: dataList[id=1051311].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [ParadeConcentration]
   znaczenie tagów: [ParadeConcentration] = 라만차 퍼레이드 / La Mancha Parade
   EN: If conditions are met: inflict 1 [ParadeConcentration]\nIf conditions are met: heal 30% HP
   PL: Jeżeli warunki są spełnione: nakłada 1 [ParadeConcentration]\nJeżeli warunki są spełnione: odzyskuje 30% HP
530. [Pasywka wsparcia (od ulepszenia 3, rezonans 5× Lust) — nazwa] 잔이 넘치도록
   źródło: Passives.json :: dataList[id=1051321].name
   limit: do 40 znaków
   EN: Flood the Chalice
   PL: Przepełnij Kielich
531. [Pasywka wsparcia (od ulepszenia 3, rezonans 5× Lust) — opis] 해당 턴 동안 [BloodDinner]이 생성될 때 1.5배로 생성됨 (전투당 2회, 소수점 버림)
   źródło: Passives.json :: dataList[id=1051321].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [BloodDinner]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast
   EN: For the turn, multiply the amount of [BloodDinner] generated by 1.5 (2 times per Encounter; rounded down)
   PL: W tej turze [BloodDinner] tworzy się x 1.5 (2 razy na spotkanie; zaokrąglone w dół)

## [000] Lobotomy E.G.O:: Hornet 【Alteration】 — Meursault — 로보토미 E.G.O:: 호넷【변조】
- ID Tożsamości: `10514` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9108 · HP bazowe: 72 · szybkość: 3–6 / 3–7 / 4–8 / 4–8
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Burn, Bleed

532. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n호넷【변조】
   źródło: Personalities.json :: dataList[id=10514].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::\nHornet 【Alteration】
   PL: Lobotomy E.G.O::\nHornet 【Zmodyfikowany】
533. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10514].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10514].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Karta Tożsamości — opis] 뫼르소의 열네번째 인격
   źródło: Personalities.json :: dataList[id=10514].desc
   limit: do 120 znaków
   EN: Meursault's 14th Identity
   PL: Czternasta Tożsamość Meursaulta
536. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 위협 사격
   źródło: Skills_personality-05.json :: dataList[id=1051401].levelList[level=1].name ; dataList[id=1051401].levelList[level=2].name ; dataList[id=1051401].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Warning Shot
   PL: Strzał Ostrzegawczy
537. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [MeursaultSporeBulletLong] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051401].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1051401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1051401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MeursaultSporeBulletLong]
   znaczenie tagów: [MeursaultSporeBulletLong] = 포자탄[기본] / Spore Round [Base]
   EN: Spend 1 [MeursaultSporeBulletLong]
   PL: Zużywa 1 [MeursaultSporeBulletLong]
538. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051401].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1051401].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1051401].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [MeursaultSporeBulletLong] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051401].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1051401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051401].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1051401].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[BeforeUse] 자신의 [MeursaultSporeBulletLong]이 최댓값이면, 적중 시 [PenetrateTakeDamageUp] 1 부여 (턴당 1회)\n[WhenUse] 대상의 [Combustion]과 [Laceration]의 합이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-05.json :: dataList[id=1051401].levelList[level=2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeUse], [MeursaultSporeBulletLong], [PenetrateTakeDamageUp], [WhenUse], [Combustion], [Laceration]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [MeursaultSporeBulletLong] = 포자탄[기본] / Spore Round [Base]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[BeforeUse] At max [MeursaultSporeBulletLong], inflict 1 [PenetrateTakeDamageUp] On Hit (once per turn)\n[WhenUse] If target has 6+ ([Combustion] + [Laceration]), Coin Power +1</style>
   PL: <style="highlight">[BeforeUse] Przy maks. [MeursaultSporeBulletLong] przy trafieniu nakłada 1 [PenetrateTakeDamageUp] (1 raz na turę)\n[WhenUse] Jeżeli cel ma 6+ (suma [Combustion] i [Laceration]), Moc Monet +1</style>
542. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">대상의 [MeursaultBeeSpore] 5당 피해량 +10% (최대 30%)</style>\n[BeforeUse] 자신의 [MeursaultSporeBulletLong]이 최댓값이면, 적중 시 [PenetrateTakeDamageUp] 1 부여 (턴당 1회)\n[WhenUse] 대상의 [Combustion]과 [Laceration]의 합 <style="highlight">6당 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051401].levelList[level=4].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [MeursaultBeeSpore], [BeforeUse], [MeursaultSporeBulletLong], [PenetrateTakeDamageUp], [WhenUse], [Combustion], [Laceration]
   znaczenie tagów: [MeursaultBeeSpore] = 포자 / Spore; [BeforeUse] = [사용전] / [Before Use]; [MeursaultSporeBulletLong] = 포자탄[기본] / Spore Round [Base]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">Deal +10% damage for every 5 [MeursaultBeeSpore] on target (max 30%)</style>\n[BeforeUse] At max [MeursaultSporeBulletLong], inflict 1 [PenetrateTakeDamageUp] On Hit (once per turn)\n[WhenUse] <style="highlight">Coin Power +1 for every 6 ([Combustion] + [Laceration]) on target (max 2)</style>
   PL: <style="highlight">Zadaje +10% obrażeń za każde 5 [MeursaultBeeSpore] celu (maks. 30%)</style>\n[BeforeUse] Przy maks. [MeursaultSporeBulletLong] przy trafieniu nakłada 1 [PenetrateTakeDamageUp] (1 raz na turę)\n[WhenUse] <style="highlight">Moc Monet +1 za każde 6 (suma [Combustion] i [Laceration] celu) (maks. 2)</style>
543. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051401].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 471 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] E.G.O 변조 - 산탄
   źródło: Skills_personality-05.json :: dataList[id=1051402].levelList[level=1].name ; dataList[id=1051402].levelList[level=2].name ; dataList[id=1051402].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: E.G.O Alteration - Buckshot
   PL: Zmodyfikowane E.G.O - Śrut
545. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 서브 타겟에게 가하는 피해량 -50%
   źródło: Skills_personality-05.json :: dataList[id=1051402].levelList[level=1].desc
   limit: do 120 znaków
   EN: Deal -50% damage against sub-targets
   PL: Zadaje -50% obrażeń celom drugorzędnym
546. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [MeursaultSporeBulletShort] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1051402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1051402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MeursaultSporeBulletShort]
   znaczenie tagów: [MeursaultSporeBulletShort] = 포자탄[산탄] / Spore Round [Buckshot]
   EN: Spend 1 [MeursaultSporeBulletShort]
   PL: Zużywa 1 [MeursaultSporeBulletShort]
547. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051402].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1051402].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1051402].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [MeursaultSporeBulletShort] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051402].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1051402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [MeursaultSporeBulletShort] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051402].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1051402].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1051402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 서브 타겟에게 가하는 피해량 -50%\n<style="highlight">대상의 [MeursaultBeeSpore] 5당 피해량 +7% (최대 21%)\n[WhenUse] 메인 타겟의 [Combustion]과 [Laceration]의 합이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-05.json :: dataList[id=1051402].levelList[level=2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [MeursaultBeeSpore], [WhenUse], [Combustion], [Laceration]
   znaczenie tagów: [MeursaultBeeSpore] = 포자 / Spore; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: Deal -50% damage against sub-targets\n<style="highlight">Deal +7% damage for every 5 [MeursaultBeeSpore] on target (max 21%)\n[WhenUse] If the main target has 6+ ([Combustion] + [Laceration]), Coin Power +1</style>
   PL: Zadaje -50% obrażeń celom drugorzędnym\n<style="highlight">Zadaje +7% obrażeń za każde 5 [MeursaultBeeSpore] celu (maks. 21%)\n[WhenUse] Jeżeli główny cel ma 6+ (suma [Combustion] i [Laceration]), Moc Monet +1</style>
552. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051402].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 481 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 서브 타겟에게 가하는 피해량 -50%\n대상의 [MeursaultBeeSpore] 5당 피해량 <style="highlight">+15% (최대 45%)</style>\n[WhenUse] 메인 타겟의 [Combustion]과 [Laceration]의 합이 6 이상이면, 코인 위력 +1\n<style="highlight">[WhenUse] 자신에게 [MeursaultWorkerBee]이 있으면, 합 위력 +1\n[WhenUse] 자신의 [MeursaultWorkerBee]만큼 마지막 코인부터 [SuperCoin]으로 변경됨\n[EndSkill] 자신의 [MeursaultSporeBulletLong]이 1개 이하면, [MeursaultSporeBulletReloading]</style>
   źródło: Skills_personality-05.json :: dataList[id=1051402].levelList[level=4].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [MeursaultBeeSpore], [WhenUse], [Combustion], [Laceration], [MeursaultWorkerBee], [SuperCoin], [EndSkill], [MeursaultSporeBulletLong], [MeursaultSporeBulletReloading]
   znaczenie tagów: [MeursaultBeeSpore] = 포자 / Spore; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [MeursaultWorkerBee] = 충성 페로몬 / Loyalty Pheromone; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [EndSkill] = [공격 종료시] / [Attack End]; [MeursaultSporeBulletLong] = 포자탄[기본] / Spore Round [Base] …
   EN: Deal -50% damage against sub-targets\nDeal +<style="highlight">15</style>% damage for every 5 [MeursaultBeeSpore] on target (max <style="highlight">45</style>%)\n[WhenUse] If the main target has 6+ ([Combustion] + [Laceration]), Coin Power +1\n<style="highlight">[WhenUse] If this unit has [MeursaultWorkerBee], Clash Power +1\n[WhenUse] Convert Coins equal to [MeursaultWorkerBee] into [SuperCoin]s, beginning with the final Coin\n[EndSkill] At 1 or fewer [MeursaultSporeBulletLong], [MeursaultSporeBulletReloading]</style>
   PL: Zadaje -50% obrażeń celom drugorzędnym\nZadaje <style="highlight">+15</style>% obrażeń za każde 5 [MeursaultBeeSpore] celu (maks. <style="highlight">45</style>%)\n[WhenUse] Jeżeli główny cel ma 6+ (suma [Combustion] i [Laceration]), Moc Monet +1\n<style="highlight">[WhenUse] Jeżeli ma [MeursaultWorkerBee], Moc Starcia +1\n[WhenUse] Zmienia monety równe [MeursaultWorkerBee] w [SuperCoin], poczynając od ostatniej monety\n[EndSkill] Przy 1 lub mniej [MeursaultSporeBulletLong] [MeursaultSporeBulletReloading]</style>
554. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051402].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 2<style="highlight"></style>
555. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Combustion] 횟수 1 증가</style>
   źródło: Skills_personality-05.json :: dataList[id=1051402].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[OnSucceedAttack] Inflict +1 [Combustion] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Zwiększa Licznik [Combustion] celu o 1</style>
556. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 임상 시험 - 분진 작열
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].name ; dataList[id=1051403].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Field Test - Dust Spark
   PL: Test Terenowy - Pył Iskry
557. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [MeursaultBeeSpore] 5당 피해량 +5% (최대 15%)\n[WhenUse] 메인 타겟의 [Combustion]과 [Laceration]의 합 6당 코인 위력 +1 (최대 2)\n[EndSkill] [MeursaultSporeBulletReloading]
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [MeursaultBeeSpore], [WhenUse], [Combustion], [Laceration], [EndSkill], [MeursaultSporeBulletReloading]
   znaczenie tagów: [MeursaultBeeSpore] = 포자 / Spore; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [EndSkill] = [공격 종료시] / [Attack End]; [MeursaultSporeBulletReloading] = 재장전[포자보충] / Reload [Germination]
   EN: Deal +5% damage for every 5 [MeursaultBeeSpore] on target (max 15%)\n[WhenUse] Coin Power +1 for every 6 ([Combustion] + [Laceration]) on the main target (max 2)\n[EndSkill] [MeursaultSporeBulletReloading]
   PL: Zadaje +5% obrażeń za każde 5 [MeursaultBeeSpore] celu (maks. 15%)\n[WhenUse] Moc Monet +1 za każde 6 (suma [Combustion] i [Laceration] głównego celu) (maks. 2)\n[EndSkill] [MeursaultSporeBulletReloading]
558. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] 이 코인은 1명의 대상에게만 적중함 (메인 타겟 우선 적용)
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1051403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: This Coin hits only a single Target (prioritizes the main target)
   PL: Ta moneta trafia tylko 1 cel (najpierw główny cel)
559. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [MeursaultSporeBulletLong] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1051403].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] 이 코인은 1명의 대상에게만 적중함 (메인 타겟 우선 적용)
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1051403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [MeursaultSporeBulletLong] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1051403].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=1051403].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] 이 코인은 1명의 대상에게만 적중함 (메인 타겟 우선 적용)
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1051403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [MeursaultSporeBulletLong] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1051403].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1051403].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 493 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [MeursaultSporeBulletShort] 1 소모
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1051403].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 3 — opis] 서브 타겟에게 가하는 피해량 -50%
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#3].coindescs[#2].desc ; dataList[id=1051403].levelList[level=4].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [MeursaultBeeSpore]가 최댓값이면, 아래 효과 적용\n- ([Combustion] 위력 x [MeursaultBeeSpore] 수치 / 10) 만큼 분노 피해 (소수점 <noparse>버림</noparse>)\n이 효과로 분노 피해를 입혔으면, [Combustion]이 발동한 것으로 취급함\n-[Combustion] 횟수 1 감소\n-[MeursaultBeeSpore] 소멸<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#3].coindescs[#3].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, <style="highlight">, </style>, \n, [UnBrokenCoinOnSucceedAttack], [MeursaultBeeSpore], [Combustion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [MeursaultBeeSpore] = 포자 / Spore; [Combustion] = 화상 / Burn
   EN: [UnBrokenCoinOnSucceedAttack] If target's [MeursaultBeeSpore] is at max Stack, activate the following:\n- Deal ([Combustion] Potency x [MeursaultBeeSpore] Stack / 10) Wrath damage (rounded down)\n  - Dealing Wrath damage with this effect counts as activating [Combustion]\n- Target loses 1 [Combustion] Count\n- [MeursaultBeeSpore] on target expires<style="highlight"></style>
   PL: [UnBrokenCoinOnSucceedAttack] Jeżeli cel ma maks. stos [MeursaultBeeSpore], uruchamia poniższe:\n- Zadaje obrażenia Gniewu równe (Moc [Combustion] x stos [MeursaultBeeSpore] / 10) (zaokrąglone <noparse>w dół</noparse>)\n  - Zadanie obrażeń Gniewu tym efektem liczy się jako aktywacja [Combustion]\n- Cel traci 1 Licznika [Combustion]\n- Wygasa [MeursaultBeeSpore] celu<style="highlight"></style>
571. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 4 — podsumowanie] 분노 피해, [Combustion] 횟수 1 감소, [MeursaultBeeSpore] 소멸
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#3].coindescs[#3].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Combustion], [MeursaultBeeSpore]
   znaczenie tagów: [Combustion] = 화상 / Burn; [MeursaultBeeSpore] = 포자 / Spore
   EN: Deal Wrath damage, reduce target's [Combustion] Count by 1, [MeursaultBeeSpore] on target expires
   PL: Zadaje obrażenia Gniewu, zmniejsza Licznik [Combustion] celu o 1, wygasa [MeursaultBeeSpore] celu
572. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 5 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가, [Laceration] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=3].coinlist[#3].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count and +1 [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o 1 i Licznik [Laceration] celu o 1
573. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">이 스킬 공격 가중치보다 낮은 공격 대상 1당 피해량 +50% (집중 전투인 경우, 부위로 판정)</style>\n대상의 [MeursaultBeeSpore] 5당 피해량 <style="highlight">+10% (최대 30%)</style>\n<style="highlight">[BeforeUse] 자신의 [MeursaultSporeBulletLong]이 2 이하면, 정신력 6 소모하여 [MeursaultSporeBulletLong] 3 얻음</style>\n[WhenUse] 메인 타겟의 [Combustion]과 [Laceration]의 합 6당 코인 위력 +1 <style="highlight">(최대 3)\n[WhenUse] 자신에게 [MeursaultWorkerBee]이 있으면, 합 위력 +1\n[WhenUse] 자신의 [MeursaultWorkerBee]만큼 3코인부터 [SuperCoin]으로 변경됨\n[WhenUse] 자신의 [MeursaultWorkerBee]이 3이면, 가중치 +1</style>\n[EndSkill] [MeursaultSporeBulletReloading]
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=4].desc
   limit: do 810 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [MeursaultBeeSpore], [BeforeUse], [MeursaultSporeBulletLong], [WhenUse], [Combustion], [Laceration], [MeursaultWorkerBee], [SuperCoin], [EndSkill], [MeursaultSporeBulletReloading]
   znaczenie tagów: [MeursaultBeeSpore] = 포자 / Spore; [BeforeUse] = [사용전] / [Before Use]; [MeursaultSporeBulletLong] = 포자탄[기본] / Spore Round [Base]; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [MeursaultWorkerBee] = 충성 페로몬 / Loyalty Pheromone; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin …
   EN: <style="highlight">Deal +50% damage for every excess Atk Weight beyond the # of actual targets (for Focused Encounters, the part)</style>\nDeal +<style="highlight">10</style>% damage for every 5 [MeursaultBeeSpore] on target (max <style="highlight">30</style>%)\n<style="highlight">[BeforeUse] At 2 or fewer [MeursaultSporeBulletLong], consume 6 SP to gain 3 [MeursaultSporeBulletLong]</style>\n[WhenUse] Coin Power +1 for every 6 ([Combustion] + [Laceration]) on the main target (max <style="highlight">3)\n[WhenUse] If this unit has [MeursaultWorkerBee], Clash Power +1\n[WhenUse] Convert Coins equal to [MeursaultWorkerBee] into [SuperCoin]s, beginning with the 3rd Coin\n[WhenUse] At 3 [MeursaultWorkerBee], gain Atk Weight +1</style>\n[EndSkill] [MeursaultSporeBulletReloading]
   PL: <style="highlight">Zadaje +50% obrażeń za każdego 1 nadmiarowego celu ataku ponad wagę ataku tej Umiejętności (w walce skupionej: części ciała)</style>\nZadaje <style="highlight">+10</style>% obrażeń za każde 5 [MeursaultBeeSpore] celu (maks. <style="highlight">30</style>%)\n<style="highlight">[BeforeUse] Przy 2 lub mniej [MeursaultSporeBulletLong] zużywa 6 Poczytalności, aby zyskać 3 [MeursaultSporeBulletLong]</style>\n[WhenUse] Moc Monet +1 za każde 6 (suma [Combustion] i [Laceration] głównego celu) (maks. <style="highlight">3</style>)\n<style="highlight">[WhenUse] Jeżeli ma [MeursaultWorkerBee], Moc Starcia +1\n[WhenUse] Zmienia monety równe [MeursaultWorkerBee] w [SuperCoin], poczynając od 3. monety\n[WhenUse] Przy 3 [MeursaultWorkerBee] Waga ataku +1</style>\n[EndSkill] [MeursaultSporeBulletReloading]
574. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] <style="highlight">3</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 4 — opis] <style="highlight">자신의 [MeursaultWorkerBee] 1당 이 코인 피해량 +5% (최대 15%)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=4].coinlist[#3].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [MeursaultWorkerBee]
   znaczenie tagów: [MeursaultWorkerBee] = 충성 페로몬 / Loyalty Pheromone
   EN: <style="highlight">This Coin deals +5% damage for every [MeursaultWorkerBee] on self (max 15%)</style>
   PL: <style="highlight">Ta moneta zadaje +5% obrażeń za każde 1 [MeursaultWorkerBee] (maks. 15%)</style>
577. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [MeursaultBeeSpore]가 최댓값이면, 아래 효과 적용\n- ([Combustion] 위력 x [MeursaultBeeSpore] 수치 / 10) 만큼 분노 피해 (소수점 <noparse>버림</noparse>)\n이 효과로 분노 피해를 입혔으면, [Combustion]이 발동한 것으로 취급함\n-[Combustion] 횟수 1 감소\n-[MeursaultBeeSpore] 소멸<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=4].coinlist[#3].coindescs[#4].desc
   (powtórzenie elementu 570 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 6 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가, [Laceration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-05.json :: dataList[id=1051403].levelList[level=4].coinlist[#3].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count and +<style="highlight">2</style> [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o 1 i Licznik [Laceration] celu o <style="highlight">2</style>
579. [Obrona (ulepszenia 1,4) — nazwa] 포자 보충
   źródło: Skills_personality-05.json :: dataList[id=1051404].levelList[level=1].name ; dataList[id=1051404].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Spore Germination
   PL: Rozkiełkowanie Zarodników
580. [Obrona (ulepszenie 1) — opis] [StartBattle] [MeursaultSporeBulletReloading] (턴당 1회)\n[OnSucceedEvade] 자신의 체력 10 회복 (턴당 1회)
   źródło: Skills_personality-05.json :: dataList[id=1051404].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [MeursaultSporeBulletReloading], [OnSucceedEvade]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [MeursaultSporeBulletReloading] = 재장전[포자보충] / Reload [Germination]; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [StartBattle][MeursaultSporeBulletReloading] (once per turn)\n[OnSucceedEvade] Heal 10 HP (once per turn)
   PL: [StartBattle] [MeursaultSporeBulletReloading] (1 raz na turę)\n[OnSucceedEvade] Odzyskuje 10 HP (1 raz na turę)
581. [Obrona (ulepszenie 4) — opis] [StartBattle] [MeursaultSporeBulletReloading] (턴당 1회)\n<style="highlight">[WhenUseEvade] 공격자의 [Combustion]과 [Laceration]의 합 6당 코인 위력 +1 (최대 3)</style>\n[OnSucceedEvade] 자신의 체력 10 회복 (턴당 1회)\n<style="highlight">- [MeursaultWorkerBee] 보유 중이면, 수치당 5씩 회복량 추가</style>
   źródło: Skills_personality-05.json :: dataList[id=1051404].levelList[level=4].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [MeursaultSporeBulletReloading], [WhenUseEvade], [Combustion], [Laceration], [OnSucceedEvade], [MeursaultWorkerBee]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [MeursaultSporeBulletReloading] = 재장전[포자보충] / Reload [Germination]; [WhenUseEvade] = [회피 사용시] / [On Evade Use]; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [MeursaultWorkerBee] = 충성 페로몬 / Loyalty Pheromone
   EN: [StartBattle] [MeursaultSporeBulletReloading] (once per turn)\n<style="highlight">[WhenUseEvade] Coin Power +1 for every 6 ([Combustion] + [Laceration]) on the attacker (max 3)</style>\n[OnSucceedEvade] Heal 10 HP (once per turn)\n<style="highlight">- If this unit has [MeursaultWorkerBee], heal an additional 5 HP for every Stack</style>
   PL: [StartBattle] [MeursaultSporeBulletReloading] (1 raz na turę)\n<style="highlight">[WhenUseEvade] Moc Monet +1 za każde 6 (suma [Combustion] i [Laceration] atakującego) (maks. 3)</style>\n[OnSucceedEvade] Odzyskuje 10 HP (1 raz na turę)\n<style="highlight">- W posiadaniu [MeursaultWorkerBee] odzyskuje dodatkowo 5 HP za każdy stos</style>
582. [Pasywka bojowa (od ulepszenia 1) — nazwa] E.G.O 변조 / 포자탄
   źródło: Passives.json :: dataList[id=1051402].name
   limit: do 50 znaków
   EN: E.G.O Alteration / Spore Round
   PL: Zmodyfikowane E.G.O / Pocisk Zarodnikowy
583. [Pasywka bojowa (od ulepszenia 1) — opis] 상시 적용: [MeursaultSporeBulletLong] 10개, [MeursaultSporeBulletShort] 6개 보유\n\n<noparse>포자</noparse>탄을 소모하는 코인 적중 시\n- [MeursaultSporeBulletLong]을 소모했으면, [MeursaultBeeSpore] 2 부여\n- [MeursaultSporeBulletShort]을 소모했으면, [MeursaultBeeSpore] 3 부여\n- 이 효과는 스킬에서 부정적인 효과를 부여하는 것으로 취급됨\n\n[MeursaultSporeBulletShort]을 소모하는 코인 사용 전 [MeursaultSporeBulletShort]이 없으면,\n정신력 2, [MeursaultSporeBulletLong] 2 소모하여, [MeursaultSporeBulletShort] 1 얻음\n\n스킬 사용 중 포자탄이 부족하면, 다음 코인을 모두 취소하고 [MeursaultSporeBulletReloading]\n\n[MeursaultBeeSpore]가 있는 대상 사망 시 [MeursaultWorkerBee] 1 얻음
   źródło: Passives.json :: dataList[id=1051402].desc
   limit: do 960 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [MeursaultSporeBulletLong], [MeursaultSporeBulletShort], [MeursaultBeeSpore], [MeursaultSporeBulletReloading], [MeursaultWorkerBee]
   znaczenie tagów: [MeursaultSporeBulletLong] = 포자탄[기본] / Spore Round [Base]; [MeursaultSporeBulletShort] = 포자탄[산탄] / Spore Round [Buckshot]; [MeursaultBeeSpore] = 포자 / Spore; [MeursaultSporeBulletReloading] = 재장전[포자보충] / Reload [Germination]; [MeursaultWorkerBee] = 충성 페로몬 / Loyalty Pheromone
   EN: Always Active: Begin Encounters with 10 [MeursaultSporeBulletLong] and 6 [MeursaultSporeBulletShort]\n\nOn Hit using Coins that spend <noparse>Spore</noparse> Round:\n- If [MeursaultSporeBulletLong] was spent, inflict 2 [MeursaultBeeSpore]\n- If [MeursaultSporeBulletShort] was spent, inflict 3 [MeursaultBeeSpore]\n- This counts as "inflicting negative effects with the Skill"\n\nBefore Coin Use of a Coin that spends [MeursaultSporeBulletShort], if this unit does not have [MeursaultSporeBulletShort], consume 2 SP and 2 [MeursaultSporeBulletLong] to gain 1 [MeursaultSporeBulletShort]\n\nIf this unit runs out of <noparse>Spore</noparse> Round mid-Skill, cancel all subsequent Coins and [MeursaultSporeBulletReloading]\n\nWhen targets that have [MeursaultBeeSpore] are killed, gain 1 [MeursaultWorkerBee]
   PL: Zawsze aktywne: rozpoczyna spotkania z 10 [MeursaultSporeBulletLong] i 6 [MeursaultSporeBulletShort]\n\nPrzy trafieniu monetami zużywającymi <noparse>Zarodnik</noparse>owe Pociski:\n- Jeżeli zużyto [MeursaultSporeBulletLong], nakłada 2 [MeursaultBeeSpore]\n- Jeżeli zużyto [MeursaultSporeBulletShort], nakłada 3 [MeursaultBeeSpore]\n- Ten efekt liczy się jako „nakładanie negatywnych efektów Umiejętnością”\n\nPrzed użyciem monety zużywającej [MeursaultSporeBulletShort] jeżeli nie ma [MeursaultSporeBulletShort], zużywa 2 Poczytalności i 2 [MeursaultSporeBulletLong], aby zyskać 1 [MeursaultSporeBulletShort]\n\nJeżeli skończą się Pociski Zarodnikowe w trakcie Umiejętności, anuluje wszystkie kolejne monety i [MeursaultSporeBulletReloading]\n\nGdy giną cele z [MeursaultBeeSpore], zyskuje 1 [MeursaultWorkerBee]
584. [Pasywka bojowa (od ulepszenia 1) — tekst klimatyczny] ‘우리 연구팀에서 확인해 본 결과, 환상체에서 정제 추출한 안정된 장비라 해도 사용자에 따라 미묘한 변형이 일어나더군.\n불완전해서 라기 보단… 진짜 E.G.O처럼 오히려 완전해지는 과정이라고 보아야 할지.\n우선 그걸 변조라 이름 붙이도록 하지.’
   źródło: Passives.json :: dataList[id=1051402].flavor
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "The research team's—that's us—examination has confirmed that even gears that were outcomes of stable, refined extractions may undergo slight mutations depending on the user.\nNo, I wouldn't attribute that to incompleteness. Rather, such changes may even be a process of these gears reaching their own completion, like real E.G.O.\nLet us label this phenomenon "Alteration" for now."
   PL: „Zespół badawczy — to my — potwierdził, że nawet sprzęt pozyskany stabilną, rafinowaną ekstrakcją może przechodzić delikatne mutacje zależnie od użytkownika.\nNie, nie przypisałbym tego niedoskonałości. Raczej takie zmiany można postrzegać jako proces, w którym ten sprzęt osiąga własną pełnię, jak prawdziwe E.G.O.\nNazwijmy to zjawisko »Zmodyfikowaniem«”.
585. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Wrath) — nazwa] 포자 확산
   źródło: Passives.json :: dataList[id=1051401].name
   limit: do 40 znaków
   EN: Spore Diffusion
   PL: Rozprzestrzenianie Zarodników
586. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Wrath) — opis] [MeursaultBeeSpore]를 보유한 적 처치 시, 다음 턴 동안 부여하는 [MeursaultBeeSpore] 수치가 2배가 됨
   źródło: Passives.json :: dataList[id=1051401].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [MeursaultBeeSpore]
   znaczenie tagów: [MeursaultBeeSpore] = 포자 / Spore
   EN: On Kill against targets that have [MeursaultBeeSpore], inflict double the [MeursaultBeeSpore] for the next turn
   PL: Pokonując wrogów z [MeursaultBeeSpore], nakłada w następnej turze 2x więcej [MeursaultBeeSpore]
587. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Wrath) — nazwa] 포자 확산
   źródło: Passives.json :: dataList[id=1051411].name
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Wrath) — opis] [MeursaultBeeSpore]를 보유한 적 처치 시, 아래 효과 적용\n- 다음 턴 동안 부여하는 [MeursaultBeeSpore] 수치가 2배가 됨\n<style="highlight">- 기본 공격 스킬로 처치 시 (해당 스킬에서 소모하는 포자탄 / 2)만큼 포자탄 획득 (소수점 올림, 스킬당 1회)</style>
   źródło: Passives.json :: dataList[id=1051411].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [MeursaultBeeSpore]
   znaczenie tagów: [MeursaultBeeSpore] = 포자 / Spore
   EN: On Kill against targets that have [MeursaultBeeSpore], gain the following effects:\n- Inflict double the [MeursaultBeeSpore] for the next turn\n<style="highlight">- On Kill using a Base Attack Skill, gain (<noparse>Spore</noparse> Round the Skill spends / 2) <noparse>Spore</noparse> Round (rounded up; once per Skill)</style>
   PL: Pokonując wrogów z [MeursaultBeeSpore], stosuje poniższe efekty:\n- Nakłada w następnej turze dwukrotność [MeursaultBeeSpore]\n<style="highlight">- Przy zabiciu podstawową Umiejętnością ataku zyskuje (Pociski Zarodnikowe zużywane przez tę Umiejętność / 2) <noparse>Zarodnik</noparse>owych Pocisków (zaokrąglone w górę; 1 raz na Umiejętność)</style>
589. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Wrath) — nazwa] 일벌
   źródło: Passives.json :: dataList[id=1051421].name
   limit: do 40 znaków
   EN: Worker Bee
   PL: Robotnica
590. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Wrath) — opis] 이번 턴동안 아래 효과 적용 (전투당 최대 2번 발동 가능) \n- 아군의 관통 속성 기본 공격 스킬의 공격 종료 시, 해당 공격으로 입힌 체력 피해량의 10%만큼 체력 회복\n- 스킬 슬롯에 장착한 모든 기본 공격 스킬이 관통 속성이면, 턴 종료 시 모든 아군 정신력 10 회복
   źródło: Passives.json :: dataList[id=1051421].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Apply the following effects for this turn (2 times per Encounter)\n- Attack End of Ally Pierce Base Attack Skill: The said ally heals HP equal to 10% of HP damage dealt using the attack\n- If all Base Attack Skills equipped on allied Skill Slots are Pierce Skills, all allies heal 10 SP at Turn End
   PL: Stosuje poniższe efekty w tej turze (maks. 2 razy na spotkanie)\n- Na koniec ataku sojuszniczą podstawową Umiejętnością Kłucia ten sojusznik odzyskuje HP równe 10% zadanych obrażeń HP tym atakiem\n- Jeżeli wszystkie podstawowe Umiejętności ataku wyposażone w sloty Umiejętności sojuszników są Umiejętnościami Kłucia, na koniec tury wszyscy sojusznicy odzyskują 10 Poczytalności

## [000] The Ring Fauvist Student — Meursault — 약지 야수파 스튜던트
- ID Tożsamości: `10515` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 7 · HP bazowe: 69 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Bleed, Sinking

591. [Karta Tożsamości — tytuł] 약지 야수파\n스튜던트
   źródło: Personalities.json :: dataList[id=10515].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Ring Fauvist\nStudent
   PL: Ringu Fauwista\nStudent
592. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=10515].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities.json :: dataList[id=10515].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Karta Tożsamości — opis] 뫼르소의 열다섯번째 인격
   źródło: Personalities.json :: dataList[id=10515].desc
   limit: do 120 znaków
   EN: Meursault’s 15th Identity
   PL: Piętnasta Tożsamość Meursaulta
595. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 거친 묘사
   źródło: Skills_personality-05.json :: dataList[id=1051501].levelList[level=1].name ; dataList[id=1051501].levelList[level=2].name ; dataList[id=1051501].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Rough Portrayal
   PL: Surowy Szkic
596. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051501].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1051501].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-05.json :: dataList[id=1051501].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1051501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051501].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Laceration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[WhenUse] Coin Power +1 for every 6 ([Laceration] + [Sinking]) on target (max 2)</style>
   PL: <style="highlight">[WhenUse] Moc Monet +1 za każde 6 (suma [Laceration] i [Sinking] celu) (maks. 2)</style>
599. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">대상의 부정적인 효과 1개당, 피해량 +5% (최대 15%)</style>\n[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-05.json :: dataList[id=1051501].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">Deal +5% damage for every type of negative effect on target (max 15%)</style>\n[WhenUse] Coin Power +1 for every 6 ([Laceration] + [Sinking]) on target (max 2)
   PL: <style="highlight">Zadaje +5% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 15%)</style>\n[WhenUse] Moc Monet +1 za każde 6 (suma [Laceration] i [Sinking] celu) (maks. 2)
600. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] <style="highlight">2</style> 부여
   źródło: Skills_personality-05.json :: dataList[id=1051501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 471 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Sinking] 횟수 1 증가</style>
   źródło: Skills_personality-05.json :: dataList[id=1051501].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[OnSucceedAttack] Inflict +1 [Sinking] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Zwiększa Licznik [Sinking] celu o 1</style>
602. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 본능적인 휘갈김
   źródło: Skills_personality-05.json :: dataList[id=1051502].levelList[level=1].name ; dataList[id=1051502].levelList[level=2].name ; dataList[id=1051502].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Visceral Strokes
   PL: Pierwotne Pociągnięcia
603. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 대상에게 [BearClawWoundAlly]가 없으면 합 위력 +1
   źródło: Skills_personality-05.json :: dataList[id=1051502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [BearClawWoundAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BearClawWoundAlly] = 찢긴 색채 [루주] / Mauled Color [Rouge]
   EN: [WhenUse] If target does not have [BearClawWoundAlly], Clash Power +1
   PL: [WhenUse] Jeżeli cel nie ma [BearClawWoundAlly], Moc Starcia +1
604. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051502].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1051502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1051502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051502].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1051502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1051502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051502].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1051502].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1051502].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상에게 [BearClawWoundAlly]가 없으면 합 위력 +1\n<style="highlight">[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051502].levelList[level=2].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BearClawWoundAlly], [Laceration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BearClawWoundAlly] = 찢긴 색채 [루주] / Mauled Color [Rouge]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target does not have [BearClawWoundAlly], Clash Power +1\n<style="highlight">[WhenUse] Coin Power +1 for every 6 ([Laceration] + [Sinking]) on target (max 2)</style>
   PL: [WhenUse] Jeżeli cel nie ma [BearClawWoundAlly], Moc Starcia +1\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 (suma [Laceration] i [Sinking] celu) (maks. 2)</style>
608. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">대상의 부정적인 효과 1개당, 피해량 +5% (최대 20%)</style>\n[WhenUse] 대상에게 [BearClawWoundAlly]가 없으면 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-05.json :: dataList[id=1051502].levelList[level=4].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [BearClawWoundAlly], [Laceration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BearClawWoundAlly] = 찢긴 색채 [루주] / Mauled Color [Rouge]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">Deal +5% damage for every type of negative effect on target (max 20%)</style>\n[WhenUse] If target does not have [BearClawWoundAlly], Clash Power +1\n[WhenUse] Coin Power +1 for every 6 ([Laceration] + [Sinking]) on target (max 2)
   PL: <style="highlight">Zadaje +5% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 20%)</style>\n[WhenUse] Jeżeli cel nie ma [BearClawWoundAlly], Moc Starcia +1\n[WhenUse] Moc Monet +1 za każde 6 (suma [Laceration] i [Sinking] celu) (maks. 2)
609. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Sinking] 1 부여</style>
   źródło: Skills_personality-05.json :: dataList[id=1051502].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Sinking]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [Sinking]</style>
610. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Sinking] 1 부여</style>
   źródło: Skills_personality-05.json :: dataList[id=1051502].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 야수파 - 출품작 전개
   źródło: Skills_personality-05.json :: dataList[id=1051503].levelList[level=3].name ; dataList[id=1051503].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 50 znaków
   EN: Le Fauvisme - Reveal Submission
   PL: Le Fauvisme - Odsłonięcie Pracy
612. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 부정적인 효과 1개당, 피해량 +10% (최대 60%)\n[WhenUse] 자신의 체력이 50% 미만이거나 대상의 찢긴 색채가 5 이상이면, 스킬의 3코인이 추가되며 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_personality-05.json :: dataList[id=1051503].levelList[level=3].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Deal +10% damage for every type of negative effect on target (max 60%)\n[WhenUse] At less than 50% HP, or if target has 5+ Mauled Color, use Coin 3 an additional time and convert all Coins on this Skill to [SuperCoin]s
   PL: Zadaje +10% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 60%)\n[WhenUse] Przy HP poniżej 50% albo gdy cel ma 5+ Rozdartą Barwę, używa dodatkowo monety 3, a wszystkie monety tej Umiejętności zmieniają się w [SuperCoin]
613. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051503].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1051503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051503].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1051503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_personality-05.json :: dataList[id=1051503].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1051503].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] Nakłada 2 [Sinking]
616. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051503].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-05.json :: dataList[id=1051503].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 291 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 부정적인 효과 1개당, 피해량 +10% (최대 60%)\n<style="highlight">[WhenUse] 대상의 [Laceration]과 [Sinking]의 합 4당, 최종 위력 +1 (최대 4)</style>\n[WhenUse] 자신의 체력이 50% 미만이거나 대상의 찢긴 색채가 5 이상이면, 스킬의 3코인이 1개 추가되고, 모든 코인이 [SuperCoin]으로 변경됨<style="highlight">\n- 추가된 코인의 공격 적중 시 대상의 (찢긴 색채/3)만큼 [Laceration] 또는 [Sinking] 위력을 무작위로 부여 (각각 최대 3, 소수점 버림)</style>
   źródło: Skills_personality-05.json :: dataList[id=1051503].levelList[level=4].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [Sinking], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Deal +10% damage for every type of negative effect on target (max 60%)\n<style="highlight">[WhenUse] Final Power +1 for every 4 ([Laceration] + [Sinking]) on target (max 4)</style>\n[WhenUse] At less than 50% HP, or if target has 5+ Mauled Color, use Coin 3 an additional time and convert all Coins on this Skill to [SuperCoin]s\n<style="highlight">- On Hit with the additional Coin: Randomly inflict (Mauled Color on target / 3) [Laceration] or [Sinking] Potency (max 3 each; rounded down)</style>
   PL: Zadaje +10% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 60%)\n<style="highlight">[WhenUse] Moc Końcowa +1 za każde 4 (suma [Laceration] i [Sinking] celu) (maks. 4)</style>\n[WhenUse] Przy HP poniżej 50% albo gdy cel ma 5+ Rozdartą Barwę, używa dodatkowo 1 monety 3, a wszystkie monety tej Umiejętności zmieniają się w [SuperCoin]\n<style="highlight">- Przy trafieniu dodatkową monetą losowo nakłada (Rozdartą Barwę celu / 3) [Laceration] lub [Sinking] Mocy (każdy maks. 3; zaokrąglone w dół)</style>
619. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 554 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-05.json :: dataList[id=1051503].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] <style="highlight">[OnSucceedAttack] [BearClawWoundAlly] 1 부여</style>
   źródło: Skills_personality-05.json :: dataList[id=1051503].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BearClawWoundAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BearClawWoundAlly] = 찢긴 색채 [루주] / Mauled Color [Rouge]
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [BearClawWoundAlly]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [BearClawWoundAlly]</style>
622. [Obrona (ulepszenia 1,4) — nazwa] 채색 준비
   źródło: Skills_personality-05.json :: dataList[id=1051504].levelList[level=1].name ; dataList[id=1051504].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Coloring Preparations
   PL: Przygotowania do Kolorowania
623. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n자신에게 [FaubismMaskMeursault]이 있으면, 기본 위력 +2
   źródło: Skills_personality-05.json :: dataList[id=1051504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [FaubismMaskMeursault]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [FaubismMaskMeursault] = 야수파 - 마스크 드 시앵 / Le Fauvisme - Masque de Chien
   EN: [DuelCounter]\nIf this unit has [FaubismMaskMeursault], Base Power +2
   PL: [DuelCounter]\nJeżeli ma [FaubismMaskMeursault], Moc Bazowa +2
624. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051504].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1051504].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Obrona (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-05.json :: dataList[id=1051504].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1051504].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] Nakłada 1 [Sinking]
626. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n자신에게 [FaubismMaskMeursault]이 있으면, 기본 위력 +2\n<style="highlight">[WhenUse] 대상의 [Laceration]과 [Sinking]의 합이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-05.json :: dataList[id=1051504].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [FaubismMaskMeursault], [WhenUse], [Laceration], [Sinking]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [FaubismMaskMeursault] = 야수파 - 마스크 드 시앵 / Le Fauvisme - Masque de Chien; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Sinking] = 침잠 / Sinking
   EN: [DuelCounter]\nIf this unit has [FaubismMaskMeursault], Base Power +2\n<style="highlight">[WhenUse] If target has 6+ ([Laceration] + [Sinking]), Coin Power +1</style>
   PL: [DuelCounter]\nJeżeli ma [FaubismMaskMeursault], Moc Bazowa +2\n<style="highlight">[WhenUse] Jeżeli cel ma 6+ (suma [Laceration] i [Sinking]), Moc Monet +1</style>
627. [Pasywka bojowa (od ulepszenia 1) — nazwa] 약지 야수파 스튜던트
   źródło: Passives.json :: dataList[id=1051502].name
   limit: do 40 znaków
   EN: The Ring Fauvist Student
   PL: Ringu Fauwista Student
628. [Pasywka bojowa (od ulepszenia 1) — opis] 기본 스킬 적중 시 [BearClawWoundAlly] 1 부여\n- 이 효과는 스킬에서 부정적인 효과를 부여하는 것으로 취급됨\n\n턴 종료 시 이번 전투 동안 자신이 [BearClawWoundAlly]를 10 이상 부여했으면, [FaubismMaskMeursault] 얻음\n\n약지 야수파 도슨트 로쟈의 ‘크리틱’ 스킬 코인 시작 시, 약지 야수파 스튜던트 뫼르소가 [TestWaitingMeursault] 얻음
   źródło: Passives.json :: dataList[id=1051502].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [BearClawWoundAlly], [FaubismMaskMeursault], [TestWaitingMeursault]
   znaczenie tagów: [BearClawWoundAlly] = 찢긴 색채 [루주] / Mauled Color [Rouge]; [FaubismMaskMeursault] = 야수파 - 마스크 드 시앵 / Le Fauvisme - Masque de Chien; [TestWaitingMeursault] = 결점 보완 / Imperfections Addressed
   EN: On Hit with a Base Skill: Inflict 1 [BearClawWoundAlly]\n- This counts as "inflicting negative effects with the Skill"\n\nTurn End: If this unit has inflicted 10+ [BearClawWoundAlly] during this Encounter, gain [FaubismMaskMeursault]\n\nAt Coin Start of The Ring Fauvist Docent Rodion's "Critique" Skill, The Ring Fauvist Student Meursault gains [TestWaitingMeursault]
   PL: Przy trafieniu podstawową Umiejętnością nakłada 1 [BearClawWoundAlly]\n- Ten efekt liczy się jako „nakładanie negatywnych efektów Umiejętnością”\n\nNa koniec tury jeżeli nakładanie 10+ [BearClawWoundAlly] w tym spotkaniu, zyskuje [FaubismMaskMeursault]\n\nNa początku monety Umiejętności „Krytyka” Ringu Fauwista Docentki Rodion, Ringu Fauwista Student Meursault zyskuje [TestWaitingMeursault]
629. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — nazwa] 차오르는 영감
   źródło: Passives.json :: dataList[id=1051501].name
   limit: do 40 znaków
   EN: Welling Inspiration
   PL: Rosnąca Inspiracja
630. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — opis] 자신에게 [FaubismMaskMeursault]이 있으면, [BearClawWoundAlly] 부여량 +1\n\n자신이 [BearClawWoundAlly]를 4 부여 할 때마다, 정신력 5 회복 (턴당 2회)\n- 이 효과로 정신력 회복 시 자신의 정신력이 최대면, 다음 턴에 [HitDamageUp] 1 얻음 (턴당 1회)
   źródło: Passives.json :: dataList[id=1051501].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [FaubismMaskMeursault], [BearClawWoundAlly], [HitDamageUp]
   znaczenie tagów: [FaubismMaskMeursault] = 야수파 - 마스크 드 시앵 / Le Fauvisme - Masque de Chien; [BearClawWoundAlly] = 찢긴 색채 [루주] / Mauled Color [Rouge]; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up
   EN: If this unit has [FaubismMaskMeursault], inflict +1 more [BearClawWoundAlly]\n\nEvery time this unit inflicts 4 [BearClawWoundAlly], heal 5 SP (2 times per turn)\n- If this unit's SP is at max, gain 1 [HitDamageUp] next turn when this unit heals SP with this effect (once per turn)
   PL: Jeżeli ma [FaubismMaskMeursault], nakłada o 1 więcej [BearClawWoundAlly]\n\nZa każde 4 nakładane [BearClawWoundAlly] odzyskuje 5 Poczytalności (2 razy na turę)\n- Jeżeli odzyskując Poczytalność tym efektem ma maks. Poczytalności, zyskuje w następnej turze 1 [HitDamageUp] (1 raz na turę)
631. [Pasywka wsparcia (od ulepszenia 3, posiadane 2× Lust, posiadane 1× Pride) — nazwa] 겹쳐 그린 상흔
   źródło: Passives.json :: dataList[id=1051521].name
   limit: do 40 znaków
   EN: Impastoed Scar
   PL: Nalożona Blizna
632. [Pasywka wsparcia (od ulepszenia 3, posiadane 2× Lust, posiadane 1× Pride) — opis] 속도가 가장 빠른 아군 1명이 공격 적중 시 대상의 부정적인 효과 2개당 [DefenseDown] 1 부여(턴당 최대 1회, 최대 3)
   źródło: Passives.json :: dataList[id=1051521].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [DefenseDown]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: 1 ally with the fastest Speed: On Hit, inflict 1 [DefenseDown] for every 2 types of negative effect on target (once per turn; max 3)
   PL: Gdy 1 Sojusznik z najwyższą Szybkością trafia wroga, nakłada 1 [DefenseDown] za każde 2 rodzaje negatywnych efektów na celu (1 raz na turę; maks. 3)

## [?] A Moonlit Farewell to Home — Meursault — 고향을 떠나야 했던 어느 밤
- ID Tożsamości: `40501` (plik: `Personalities.json`)

633. [Karta Tożsamości — tytuł] 고향을 떠나야 했던 어느 밤
   źródło: Personalities.json :: dataList[id=40501].title
   limit: do 40 znaków
   EN: A Moonlit Farewell to Home
   PL: Nocne Pożegnanie z Domem
634. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities.json :: dataList[id=40501].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Karta Tożsamości — opis] 사영 전투][투전 영사 - 경험기억 한정 보상으로 획득
   źródło: Personalities.json :: dataList[id=40501].desc
   limit: do 120 znaków
   EN: Reflectrial][lairtcelfeR - Mnestic Experience Limited Reward
   PL: Reflectrial][lairtcelfeR - nagroda limitowana Mnestic Experience
636. [Karta Tożsamości — nazwa projekcji wyglądu] [외형 투영] 고향을 떠나야 했던 어느 밤
   źródło: Personalities.json :: dataList[id=40501].skinItemTitle
   limit: do 50 znaków
   EN: [Façade] A Moonlit Farewell to Home
   PL: [Fasadowe] Nocne Pożegnanie z Domem
637. [Karta Tożsamości — opis projekcji wyglądu] 사영 전투][투전 영사 - 경험기억 한정 보상으로 획득
   źródło: Personalities.json :: dataList[id=40501].skinItemDesc
   (powtórzenie elementu 635 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [?] Perky Penguins Sinnerling — Meursault — 펭귄반 수감생
- ID Tożsamości: `400029` (plik: `Personalities-x1p1c1.json`)

638. [Karta Tożsamości — tytuł] 펭귄반 수감생
   źródło: Personalities-x1p1c1.json :: dataList[id=400029].title
   limit: do 40 znaków
   EN: Perky Penguins Sinnerling
   PL: Grzesznik Grupy Penglów
639. [Karta Tożsamości — nazwa] 뫼르소
   źródło: Personalities-x1p1c1.json :: dataList[id=400029].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Karta Tożsamości — nazwa z tytułem] 뫼르소
   źródło: Personalities-x1p1c1.json :: dataList[id=400029].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Karta Tożsamości — opis] 뫼르소의 ??? 인격
   źródło: Personalities-x1p1c1.json :: dataList[id=400029].desc
   limit: do 120 znaków
   EN: Meursault's ??? Identity
   PL: Tożsamość ??? Meursaulta
642. [Pasywka bojowa [40002901] — nazwa] 깍오
   źródło: Passives-x1p1c1.json :: dataList[id=40002901].name
   limit: do 40 znaków
   EN: Stawchnesh
   PL: Stawchnesh
643. [Pasywka bojowa [40002901] — opis] 전투 시작 시 자신의 체력이 50% 미만이면 보호 1을 얻음
   źródło: Passives-x1p1c1.json :: dataList[id=40002901].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Pasywka bojowa [40002902] — nazwa] 등뒤 받쪄주기
   źródło: Passives-x1p1c1.json :: dataList[id=40002902].name
   limit: do 40 znaków
   EN: Backap
   PL: Backap
645. [Pasywka bojowa [40002902] — opis] 최대 체력이 가장 높은 아군 1명 공격 스킬로 받는 피해량 -10%
   źródło: Passives-x1p1c1.json :: dataList[id=40002902].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
