# Paczka AI P48 (Fala 3 · 3A) — Grzesznik 06 — Hong Lu

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P48_3a_06_hong_lu.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P48_3a_06_hong_lu.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Grzesznik #06: Hong Lu (홍루)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 홍루
   źródło: Characters.json :: dataList[id=6].name
   limit: do 40 znaków
   EN: Hong Lu
   PL: Hong Lu
2. [Akta więźnia — nazwa] 홍루
   źródło: IntroduceCharacter.json :: dataList[id=홍루].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [0] LCB Sinner — Hong Lu — LCB 수감자
- ID Tożsamości: `10601` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 66 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×2 (Fatal), Penetrate ×1 (Normal), Hit ×0,5 (Endured) · słowa kluczowe: Sinking, Rupture

3. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10601].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL: LCB\nGrzesznik
4. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10601].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
5. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10601].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — opis] 홍루의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10601].desc
   limit: do 120 znaków
   EN: Hong Lu’s 1st Identity
   PL: Pierwsza Tożsamość Hong Lu
7. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 내려베기
   źródło: Skills.json :: dataList[id=1060101].levelList[level=1].name ; dataList[id=1060101].levelList[level=2].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Downward Cleave
   PL: Cięcie w Dół
8. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1060101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 2 [Sinking]
   PL: [OnSucceedAttackHead] Nakłada 2 Zatonięcia
9. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1060101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] Nakłada 2 Zatonięcia
10. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 이연격
   źródło: Skills.json :: dataList[id=1060102].levelList[level=1].name ; dataList[id=1060102].levelList[level=2].name ; dataList[id=1060102].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Dual Strike
   PL: Podwójne Uderzenie
11. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1060102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 1 [Sinking]
   PL: [OnSucceedAttackHead] Nakłada 1 Zatonięcia
12. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1060102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL: [OnSucceedAttackHead] Nakłada 2 Rozdarcia
13. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] 이전 턴에 피해를 받지 않은 경우 코인 위력 +1
   źródło: Skills.json :: dataList[id=1060102].levelList[level=2].desc ; dataList[id=1060102].levelList[level=4].desc
   limit: do 120 znaków
   EN: If user took no damage last turn, Coin Power +1
   PL: Gdy ta jednostka nie otrzymała obrażeń w poprzedniej turze, Moc Monet +1
14. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 1 부여
   źródło: Skills.json :: dataList[id=1060102].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] Nakłada 1 Zatonięcia
15. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1060102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL: [OnSucceedAttack] Nakłada 2 Rozdarcia
16. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1060102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 선풍
   źródło: Skills.json :: dataList[id=1060103].levelList[level=3].name ; dataList[id=1060103].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 6 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Whirlwind
   PL: Wichr
18. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] 이전 턴에 피해를 받지 않은 경우 코인 위력 +2
   źródło: Skills.json :: dataList[id=1060103].levelList[level=3].desc ; dataList[id=1060103].levelList[level=4].desc
   limit: do 120 znaków
   EN: If user took no damage last turn, Coin Power +2
   PL: Gdy ta jednostka nie otrzymała obrażeń w poprzedniej turze, Moc Monet +2
19. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 공격 위력 감소 2 부여
   źródło: Skills.json :: dataList[id=1060103].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1060103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Attack Power Down
   PL: [OnSucceedAttackHead] Nakłada 2 Spadku Mocy Ataku
20. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 침잠 2 부여
   źródło: Skills.json :: dataList[id=1060103].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
21. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1060103].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
22. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1060104].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: unik · moc bazowa: 2 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL: Unik
23. [Pasywka bojowa (od ulepszenia 1, rezonans 2× Sloth) — nazwa] 유희
   źródło: Passives.json :: dataList[id=1060101].name
   limit: do 40 znaków
   EN: Entertainment
   PL: Rozrywka
24. [Pasywka bojowa (od ulepszenia 1, rezonans 2× Sloth) — opis] 다음 턴 시작 시 정신력 6 회복
   źródło: Passives.json :: dataList[id=1060101].desc
   limit: do 120 znaków
   EN: Heal 6 SP next turn.
   PL: Odzyskuje w następnej turze 6 Poczytalności.
25. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Sloth) — nazwa] 실없는 농담
   źródło: Passives.json :: dataList[id=1060121].name
   limit: do 40 znaków
   EN: Frivolous Jokes
   PL: Bezsensowne Żarty
26. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Sloth) — opis] 정신력이 가장 낮은 아군 1명 전투 시작 시 정신력 6 회복
   źródło: Passives.json :: dataList[id=1060121].desc
   limit: do 120 znaków
   EN: At the start of the combat phase, the ally with the least SP heals 6 SP.
   PL: Na początku walki 1 Sojusznik z najniższą Poczytalnością odzyskuje 6 Poczytalności.

## [00] Kurokumo Clan Wakashu — Hong Lu — 흑운회 와카슈
- ID Tożsamości: `10602` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 76 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed

27. [Karta Tożsamości — tytuł] 흑운회\n와카슈
   źródło: Personalities.json :: dataList[id=10602].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Kurokumo Clan\nWakashu
   PL: Klan Kurokumo\nWakashu
28. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10602].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
29. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10602].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
30. [Karta Tożsamości — opis] 홍루의 두번째 인격
   źródło: Personalities.json :: dataList[id=10602].desc
   limit: do 120 znaków
   EN: Hong Lu’s 2nd Identity
   PL: Druga Tożsamość Hong Lu
31. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 베어내기
   źródło: Skills.json :: dataList[id=1060201].levelList[level=1].name ; dataList[id=1060201].levelList[level=2].name ; dataList[id=1060201].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Cleave
   PL: Rozcięcie
32. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed
   PL: [OnSucceedAttackHead] Nakłada 2 Krwawienia
33. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060201].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL: [OnSucceedAttack] Nakłada 2 Krwawienia
34. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 3 부여
   źródło: Skills.json :: dataList[id=1060201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Bleed
   PL: [OnSucceedAttack] Nakłada 3 Krwawienia
35. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 구름 절개
   źródło: Skills.json :: dataList[id=1060202].levelList[level=1].name ; dataList[id=1060202].levelList[level=2].name ; dataList[id=1060202].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Cloud Cutter
   PL: Przecinacz Chmur
36. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060202].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1060202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
37. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1060202].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1060202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bleed
   PL: [OnSucceedAttack] Nakłada 1 Krwawienia
38. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [BeforeAttack] 대상의 출혈 횟수가 4미만이면 스킬의 1, 2코인이 추가됨
   źródło: Skills.json :: dataList[id=1060202].levelList[level=2].desc ; dataList[id=1060202].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [BeforeAttack] If target has less than 4 Bleed Count, use Coin 1 and 2 an additional time
   PL: [BeforeAttack] Jeżeli cel ma mniej niż 4 Licznika Krwawienia, używa dodatkowo monet 1 i 2 tej Umiejętności
39. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
40. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 구름 파열
   źródło: Skills.json :: dataList[id=1060203].levelList[level=3].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 7 · monety: 3 (+2)
   limit: do 40 znaków
   EN: Cloudburst
   PL: Pęknięcie Chmur
41. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [StartBattle] 이 스킬에서 부여하는 출혈, 마비 1 추가 부여
   źródło: Skills.json :: dataList[id=1060203].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] This skill inflicts 1 additional Bleed and Paralyze
   PL: [StartBattle] Ta Umiejętność nakłada o 1 więcej Krwawienia i Paraliżu
42. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060203].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 마비 5 부여
   źródło: Skills.json :: dataList[id=1060203].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Paralyze
   PL: [OnSucceedAttack] Nakłada 5 Paraliżu
45. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1060204].levelList[level=1].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 9 · monety: 1 (+3)
   limit: do 40 znaków
   EN: Guard
   PL: Blok
46. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — nazwa] 흑운도
   źródło: Passives.json :: dataList[id=1060201].name
   limit: do 40 znaków
   EN: Hēiyúndào
   PL: Klinga Czarnego Obłoku
47. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — opis] 연결한 죄 중 마지막 죄의 마지막 코인으로 공격할 때 출혈 3 부여
   źródło: Passives.json :: dataList[id=1060201].desc
   limit: do 120 znaków
   EN: The last Coin on the last skill in the chain inflicts 3 Bleed.
   PL: Ostatnia moneta ostatniej Umiejętności w łańcuchu łączonej Winy nakłada 3 Krwawienia.
48. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 조직의 보복
   źródło: Passives.json :: dataList[id=1060221].name
   limit: do 40 znaków
   EN: Syndicate Payback
   PL: Odwet Syndykatu
49. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 속도가 가장 높은 아군 1명 출혈 부여 값 +1
   źródło: Passives.json :: dataList[id=1060221].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed inflicts +1 Bleed.
   PL: 1 Sojusznik z najwyższą Szybkością nakłada o 1 więcej Krwawienia.

## [000] Tingtang Gang Gangleader — Hong Lu — 콩콩이파 두목
- ID Tożsamości: `10603` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 1 · HP bazowe: 76 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed

50. [Karta Tożsamości — tytuł] 콩콩이파\n두목
   źródło: Personalities.json :: dataList[id=10603].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Tingtang Gang\nGangleader
   PL: Gang Kongkongi\nSzef Szefów
51. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10603].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10603].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [Karta Tożsamości — opis] 홍루의 세번째 인격
   źródło: Personalities.json :: dataList[id=10603].desc
   limit: do 120 znaków
   EN: Hong Lu’s 3rd Identity
   PL: Trzecia Tożsamość Hong Lu
54. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 목 긋기
   źródło: Skills.json :: dataList[id=1060301].levelList[level=1].name ; dataList[id=1060301].levelList[level=2].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 5 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Throat Slit
   PL: Nacięcie Gardła
55. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1060301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 4 부여
   źródło: Skills.json :: dataList[id=1060301].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 4 Bleed
   PL: [OnSucceedAttackHead] Nakłada 4 Krwawienia
57. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 후비기
   źródło: Skills.json :: dataList[id=1060302].levelList[level=1].name ; dataList[id=1060302].levelList[level=2].name ; dataList[id=1060302].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 3 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Shank
   PL: Dźgnięcie
58. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 추가 피해 +2
   źródło: Skills.json :: dataList[id=1060302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Damage +2
   PL: [OnSucceedAttackHead] Dodatkowe obrażenia +2
59. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 추가 피해 +2
   źródło: Skills.json :: dataList[id=1060302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 추가 피해 +3
   źródło: Skills.json :: dataList[id=1060302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Damage +3
   PL: [OnSucceedAttackHead] Dodatkowe obrażenia +3
61. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 추가 피해 +3
   źródło: Skills.json :: dataList[id=1060302].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 적의 체력이 최대 체력의 25%미만일 때, 대상이 생존한 상태면 이 코인 1회 재사용\n앞면이 나오면 이 코인의 피해량 +50%
   źródło: Skills.json :: dataList[id=1060302].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1060302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] If target is below 25% HP, use this Coin an additional time if target survives\nHeads: +50% Damage for this Coin
   PL: [OnSucceedAttackHead] Jeżeli cel ma poniżej 25% HP, używa tej monety dodatkowo 1 raz, jeżeli cel przeżyje\nAwers: +50% obrażeń tej monety
63. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [ReUseOnSucceedAttackHead] 이 코인 스킬 피해량 +50%
   źródło: Skills.json :: dataList[id=1060302].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1060302].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttackHead]
   znaczenie tagów: [ReUseOnSucceedAttackHead] = [재사용 앞면 적중 시] / [Reuse - Heads Hit]
   EN: [ReUseOnSucceedAttackHead] +50% Damage for this Coin
   PL: [ReUseOnSucceedAttackHead] +50% obrażeń tej monety
64. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Laceration]이 7 이상이면, 피해량 +20%
   źródło: Skills.json :: dataList[id=1060302].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 7+ [Laceration], deal +20% damage
   PL: Jeżeli cel ma 7+ [Laceration], zadaje +20% obrażeń
65. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 난도질
   źródło: Skills.json :: dataList[id=1060303].levelList[level=3].name ; dataList[id=1060303].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 1 (+25)
   limit: do 40 znaków
   EN: Mutilate
   PL: Okaleczenie
66. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] [EnemyKill] 이 스킬 1회 재사용
   źródło: Skills.json :: dataList[id=1060303].levelList[level=3].desc ; dataList[id=1060303].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Use this skill 1 more time
   PL: [EnemyKill] Używa tej Umiejętności dodatkowo 1 raz
67. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 추가 피해 +7
   źródło: Skills.json :: dataList[id=1060303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1060303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Damage +7
   PL: [OnSucceedAttackHead] Dodatkowe obrażenia +7
68. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [ReUseOnSucceedAttackHead] 이 코인 스킬 피해량 +100%
   źródło: Skills.json :: dataList[id=1060303].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttackHead]
   znaczenie tagów: [ReUseOnSucceedAttackHead] = [재사용 앞면 적중 시] / [Reuse - Heads Hit]
   EN: [ReUseOnSucceedAttackHead] +100% Damage for this Coin
   PL: [ReUseOnSucceedAttackHead] +100% obrażeń tej monety
69. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [ReUseOnSucceedAttackHead] 이 코인 스킬 피해량 +100%
   źródło: Skills.json :: dataList[id=1060303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttackHead]
   znaczenie tagów: [ReUseOnSucceedAttackHead] = [재사용 앞면 적중 시] / [Reuse - Heads Hit]
   EN: [ReUseOnSucceedAttackHead] +100% damage for this Coin
   PL: [ReUseOnSucceedAttackHead] +100% obrażeń tej monety
70. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [ReUseOnSucceedAttackHead] 대상의 [Laceration]이 10 이상이면, 피해량 +50%
   źródło: Skills.json :: dataList[id=1060303].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttackHead], [Laceration]
   znaczenie tagów: [ReUseOnSucceedAttackHead] = [재사용 앞면 적중 시] / [Reuse - Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [ReUseOnSucceedAttackHead] If target has 10+ [Laceration], deal +50% damage
   PL: [ReUseOnSucceedAttackHead] Jeżeli cel ma 10+ [Laceration], zadaje +50% obrażeń
71. [Obrona (ulepszenia 1,4) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1060304].levelList[level=1].name ; dataList[id=1060304].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: unik · moc bazowa: 2 · monety: 1 (+14)
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Obrona (ulepszenie 4) — opis] 대상의 [Laceration]이 5 이상이면, 코인 위력 +2\n[OnSucceedEvade] 정신력 3 회복
   źródło: Skills.json :: dataList[id=1060304].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [OnSucceedEvade]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: If target has 5+ [Laceration], Coin Power +2\n[OnSucceedEvade] Heal 3 SP
   PL: Jeżeli cel ma 5+ [Laceration], Moc Monet +2\n[OnSucceedEvade] Odzyskuje 3 Poczytalności
73. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Glut.) — nazwa] 유열
   źródło: Passives.json :: dataList[id=1060301].name
   limit: do 40 znaków
   EN: Gaiety
   PL: Zabawa
74. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Glut.) — opis] 다음 턴 시작 시 (탐식 공명 수 x2) 만큼 정신력 회복
   źródło: Passives.json :: dataList[id=1060301].desc
   limit: do 120 znaków
   EN: Heal (2x Gluttony Reson.) SP next turn.
   PL: Odzyskuje na początku następnej tury Poczytalność równą (Rezonans Obżarstwa x 2).
75. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — nazwa] 승부수
   źródło: Passives.json :: dataList[id=1060321].name
   limit: do 40 znaków
   EN: Gambit
   PL: Gambit
76. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — opis] 정신력이 가장 높은 아군 1명 앞면이 나온 코인의 피해량 +20%
   źródło: Passives.json :: dataList[id=1060321].desc
   limit: do 120 znaków
   EN: 1 ally with the most SP deals +20% damage with Heads Coins.
   PL: 1 Sojusznik z najwyższą Poczytalnością zadaje +20% obrażeń monetami z awersem.

## [00] Liu Assoc. South Section 5 — Hong Lu — 남부 리우 협회 5과
- ID Tożsamości: `10604` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 76 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Burn

77. [Karta Tożsamości — tytuł] 남부 리우 협회\n5과
   źródło: Personalities.json :: dataList[id=10604].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Liu Assoc.\nSouth Section 5
   PL: Południowe Stowarzyszenie Liu\nSekcja 5
78. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10604].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10604].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [Karta Tożsamości — opis] 홍루의 네번째 인격
   źródło: Personalities.json :: dataList[id=10604].desc
   limit: do 120 znaków
   EN: Hong Lu’s 4th Identity
   PL: Czwarta Tożsamość Hong Lu
81. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 몸풀기
   źródło: Skills.json :: dataList[id=1060401].levelList[level=1].name ; dataList[id=1060401].levelList[level=2].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Warm Up
   PL: Rozgrzewka
82. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 화상 1 부여
   źródło: Skills.json :: dataList[id=1060401].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1060401].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Burn
   PL: [OnSucceedAttack] Nakłada 1 Podpalenia
83. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 정신력 3 회복
   źródło: Skills.json :: dataList[id=1060401].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Heal 3 SP
   PL: [WhenUse] Odzyskuje 3 Poczytalności
84. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 흐르는 불꽃
   źródło: Skills.json :: dataList[id=1060402].levelList[level=1].name ; dataList[id=1060402].levelList[level=2].name ; dataList[id=1060402].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 6 · monety: 2 (+2)
   limit: do 40 znaków
   EN: Flowing Flame
   PL: Płynący Płomień
85. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여. 대상에게 [Combustion]이 있으면 1 추가 부여
   źródło: Skills.json :: dataList[id=1060402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1060402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]; if target already has [Combustion], inflict 1 more
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]; jeżeli cel już ma [Combustion], nakłada o 1 więcej
86. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills.json :: dataList[id=1060402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o 1
87. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가. 자신의 정신력이 30 이상이면, 1, 45 이상이면, 2 추가 증가
   źródło: Skills.json :: dataList[id=1060402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count; at 30+ SP, inflict 1 more; at 45+ SP, inflict 2 more
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o 1; przy 30+ Poczytalności o 1 więcej, przy 45+ Poczytalności o 2 więcej
88. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Combustion] 횟수가 6 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1060402].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion] Count, Coin Power +2
   PL: Jeżeli cel ma 6+ Licznika [Combustion], Moc Monet +2
89. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 홍염권
   źródło: Skills.json :: dataList[id=1060403].levelList[level=3].name ; dataList[id=1060403].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 5 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Crimson Blaze Fist
   PL: Pięść Szkarłatnego Płomienia
90. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여. 대상에게 [Combustion]이 있으면 [Combustion] 횟수 1 증가
   źródło: Skills.json :: dataList[id=1060403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1060403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]; if target already has [Combustion], inflict +1 [Combustion] Count
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]; jeżeli cel już ma [Combustion], zwiększa Licznik [Combustion] o 1
91. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 정신력 6 회복
   źródło: Skills.json :: dataList[id=1060403].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1060403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal 6 SP
   PL: [OnSucceedAttackHead] Odzyskuje 6 Poczytalności
92. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Combustion] 횟수가 6 이상이면, 피해량의 30%만큼 흐트러짐 손상을 입힘
   źródło: Skills.json :: dataList[id=1060403].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1060403].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion] Count, raise Stagger Threshold by 30% of damage dealt
   PL: [OnSucceedAttack] Jeżeli cel ma 6+ Licznika [Combustion], podnosi Próg Oszołomienia o 30% zadanych obrażeń
93. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Combustion] 횟수가 6 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1060403].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion] Count, Coin Power +1
   PL: Jeżeli cel ma 6+ Licznika [Combustion], Moc Monet +1
94. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1060404].levelList[level=1].name
   kontekst: grzech: Gloom · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — nazwa] 끓어오르는군요~
   źródło: Passives.json :: dataList[id=1060401].name
   limit: do 40 znaków
   EN: Flaring Up~
   PL: Prawie wrze~
96. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — opis] 자신의 정신력이 30 이상이면 공격 스킬의 스킬 효과, 코인 효과로 부여하는 화상 횟수 부여 값 +1
   źródło: Passives.json :: dataList[id=1060401].desc
   limit: do 120 znaków
   EN: At 30+ SP, inflict +1 Burn Count with the effects of attack skills/coins.
   PL: Przy 30+ Poczytalności podstawowe Umiejętności ataku nakładają o 1 więcej Podpalenia swoimi efektami i monet.
97. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Wrath) — nazwa] 따뜻하죠?
   źródło: Passives.json :: dataList[id=1060421].name
   limit: do 40 znaków
   EN: Isn’t It Warm?
   PL: Ciepło, prawda?
98. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Wrath) — opis] 정신력이 가장 높은 아군 1명의 공격 스킬의 스킬 효과, 코인 효과로 부여하는 화상 횟수 부여 값 +1
   źródło: Passives.json :: dataList[id=1060421].desc
   limit: do 130 znaków
   EN: 1 ally with the most SP inflicts +1 Burn Count with the effects of their attack skills/coins.
   PL: 1 Sojusznik z najwyższą Poczytalnością nakłada o 1 więcej Podpalenia podstawowymi Umiejętnościami ataku i ich efektami.

## [000] K Corp. Class 3 Excision Staff — Hong Lu — K사 3등급 적출직 직원
- ID Tożsamości: `10605` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 2 · HP bazowe: 99 · szybkość: 1–5 / 2–5 / 2–6 / 2–6
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Rupture

99. [Karta Tożsamości — tytuł] K사 3등급\n적출직 직원
   źródło: Personalities.json :: dataList[id=10605].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: K Corp. Class 3\nExcision Staff
   PL: Pracownik Ekstrakcji 3. Klasy\nK Corp.
100. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10605].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10605].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [Karta Tożsamości — opis] 홍루의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10605].desc
   limit: do 120 znaków
   EN: Hong Lu’s 5th Identity
   PL: Piąta Tożsamość Hong Lu
103. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 침입자 차단
   źródło: Skills.json :: dataList[id=1060501].levelList[level=1].name ; dataList[id=1060501].levelList[level=2].name ; dataList[id=1060501].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Impede the Intruder
   PL: Zatrzymaj Napastnika
104. [Umiejętność 1 (×3) (ulepszenie 1) — opis] 대상에게 [Burst]이 5 이상 있으면 코인 위력 +1
   źródło: Skills.json :: dataList[id=1060501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 5+ [Burst], Coin Power +1
   PL: Jeżeli cel ma 5+ [Burst], Moc Monet +1
105. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상에게 [Burst]이 5 이상 있으면 코인 위력 +2
   źródło: Skills.json :: dataList[id=1060501].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 5+ [Burst], Coin Power +2
   PL: Jeżeli cel ma 5+ [Burst], Moc Monet +2
106. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상에게 [Burst]이 5 이상 있으면 코인 위력 +3\n[WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 5 증가
   źródło: Skills.json :: dataList[id=1060501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: If target has 5+ [Burst], Coin Power +3\n[WhenUse] Gain +5 Aggro to this Skill Slot next turn
   PL: Jeżeli cel ma 5+ [Burst], Moc Monet +3\n[WhenUse] Prowokacja tego slotu Umiejętności +5 w następnej turze
107. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 붕괴 칼날
   źródło: Skills.json :: dataList[id=1060502].levelList[level=1].name ; dataList[id=1060502].levelList[level=2].name ; dataList[id=1060502].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 6 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Decay Blade
   PL: Klinga Rozpadu
108. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여\n대상에게 [Burst]이 10 이상 있으면 피해량의 20%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1060502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 Rupture\nIf target has 10+ [Burst], heal by 20% of damage dealt
   PL: [OnSucceedAttack] Nakłada 2 Rozdarcia\nJeżeli cel ma 10+ [Burst], odzyskuje HP równe 20% zadanych obrażeń
109. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여\n대상에게 [Burst]이 10 이상 있으면 피해량의 20%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1060502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
110. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여\n대상에게 [Burst]이 10 이상 있으면 피해량의 50%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1060502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 Rupture\nIf target has 10+ [Burst], heal by 50% of damage dealt
   PL: [OnSucceedAttack] Nakłada 2 Rozdarcia\nJeżeli cel ma 10+ [Burst], odzyskuje HP równe 50% zadanych obrażeń
111. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여\n대상에게 [Burst]이 10 이상 있으면 피해량의 50%만큼 체력 회복
   źródło: Skills.json :: dataList[id=1060502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 5 증가
   źródło: Skills.json :: dataList[id=1060502].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +5 Aggro to this Skill Slot next turn
   PL: [WhenUse] Prowokacja tego slotu Umiejętności +5 w następnej turze
113. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 대상 적출
   źródło: Skills.json :: dataList[id=1060503].levelList[level=3].name ; dataList[id=1060503].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Slash · moc bazowa: 8 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Excise Target
   PL: Wycięcie celu
114. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 현재 체력이 80% 이상이면, 코인 위력 +1
   źródło: Skills.json :: dataList[id=1060503].levelList[level=3].desc
   limit: do 120 znaków
   EN: At 80% or more HP, Coin Power +1
   PL: Przy 80%+ HP Moc Monet +1
115. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 4 부여
   źródło: Skills.json :: dataList[id=1060503].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1060503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Rupture
   PL: [OnSucceedAttack] Nakłada 4 Rozdarcia
116. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] K사 앰플 만큼 파열 횟수 증가. (K사 앰플 x 5)% 만큼 피해량이 증가함
   źródło: Skills.json :: dataList[id=1060503].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1060503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict Rupture Count by the amount of K Corp Ampule; Deal +5% damage per K Corp Ampule
   PL: [OnSucceedAttack] Zwiększa Licznik Rozdarcia o liczbę Ampułek Korp. K; Zadaje +5% obrażeń za każdą Ampułkę Korp. K
117. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 현재 체력이 80% 이상이면, 코인 위력 +2
   źródło: Skills.json :: dataList[id=1060503].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 80% or more HP, Coin Power +2
   PL: Przy 80%+ HP Moc Monet +2
118. [Obrona (ulepszenia 1,4) — nazwa] 앰플 주입
   źródło: Skills.json :: dataList[id=1060504].levelList[level=1].name ; dataList[id=1060504].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 15 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Ampule Injection
   PL: Wstrzyknięcie Ampułki
119. [Obrona (ulepszenie 1) — opis] [WhenUse] 다음 턴에 K사 앰플 1 얻음
   źródło: Skills.json :: dataList[id=1060504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 K Corp Ampule next turn
   PL: [WhenUse] Zyskuje w następnej turze 1 Ampułkę Korp. K
120. [Obrona (ulepszenie 4) — opis] [WhenUse] 다음 턴에 K사 앰플 1 얻음\n[WhenUse] 다음 턴에 이 스킬 슬롯의 도발치 5 증가
   źródło: Skills.json :: dataList[id=1060504].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 K Corp Ampule next turn\n[WhenUse] Gain +5 Aggro to this Skill Slot next turn
   PL: [WhenUse] Zyskuje w następnej turze 1 Ampułkę Korp. K\n[WhenUse] Prowokacja tego slotu Umiejętności +5 w następnej turze
121. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — nazwa] 재생 앰플 활성화
   źródło: Passives.json :: dataList[id=1060501].name
   limit: do 50 znaków
   EN: Regeneration Ampule Activation
   PL: Aktywacja Ampułki Regeneracji
122. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — opis] 피격 시 현재 체력이 최대 체력의 20% 미만이면, 최대 체력의 90%만큼 체력을 회복하고 K사 앰플 1을 얻음\n위 효과가 발동되면 이번 전투동안 매 턴 취약 1을 얻음 (전투 당 1회)
   źródło: Passives.json :: dataList[id=1060501].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When hit, if at less than 20% HP, heal by 90% of Max HP and gain 1 K Corp Ampule.\nAfter this activates, gain 1 Fragile every turn for the rest of the battle. (Once per battle)
   PL: Przy trafieniu, jeżeli ma mniej niż 20% HP, odzyskuje 90% Maks. HP i zyskuje 1 Ampułkę Korp. K.\nPo uruchomieniu tego efektu zyskuje 1 Wrażliwości co turę do końca walki. (1 raz na walkę)
123. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — nazwa] 고농축 앰플
   źródło: Passives.json :: dataList[id=1060521].name
   limit: do 40 znaków
   EN: High-grade Ampule
   PL: Wysoko Skoncentrowana Ampułka
124. [Pasywka wsparcia (od ulepszenia 3, rezonans 4× Glut.) — opis] 전투 시작 시 현재 체력 비율이 가장 낮은 아군 1명에게 K사 앰플 2 부여
   źródło: Passives.json :: dataList[id=1060521].desc
   limit: do 130 znaków
   EN: At the start of the combat phase, give 2 K Corp Ampule to 1 ally with the lowest HP percentage.
   PL: Na początku walki daje 2 Ampułki Korp. K 1 Sojusznikowi z najniższym procentem HP.

## [00] W Corp. L2 Cleanup Agent — Hong Lu — W사 2등급 정리 요원
- ID Tożsamości: `10606` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 82 · szybkość: 3–5 / 4–5 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture, Charge

125. [Karta Tożsamości — tytuł] W사 2등급\n정리 요원
   źródło: Personalities.json :: dataList[id=10606].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L2\nCleanup Agent
   PL: W Corp. L2\nAgentka Oczyszczania
126. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10606].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10606].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Karta Tożsamości — opis] 홍루의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10606].desc
   limit: do 120 znaków
   EN: Hong Lu’s 6th Identity
   PL: Szósta Tożsamość Hong Lu
129. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 에너지 순환
   źródło: Skills_personality-06.json :: dataList[id=1060601].levelList[level=1].name ; dataList[id=1060601].levelList[level=2].name ; dataList[id=1060601].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Energy Cycle
   PL: Obieg Energii
130. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1060601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Charge Count
   PL: [WhenUse] Zyskuje +2 Licznika Ładowania
131. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1060601].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1060601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +1 Charge Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik Ładowania o 1
132. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1060601].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1060601].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 충전 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1060601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +3 Charge Count
   PL: [WhenUse] Zwiększa własny Licznik Ładowania o 3
134. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 4 증가
   źródło: Skills_personality-06.json :: dataList[id=1060601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +4 Charge Count
   PL: [WhenUse] Zwiększa własny Licznik Ładowania o 4
135. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 정리 지원
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=1].name ; dataList[id=1060602].levelList[level=2].name ; dataList[id=1060602].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 6 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Cleanup Support
   PL: Wsparcie Oczyszczania
136. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 2 증가\n자신에게 보호막이 있을 때 합 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Charge Count\nClash Power +1 when Shielded
   PL: [WhenUse] Zwiększa własny Licznik Ładowania o 2\nMoc Starcia +1 w posiadaniu Tarczy
137. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신의 충전 횟수가 10 이상이면, 다음 턴에 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 2를 얻음
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] At 10+ Charge Count, gain 2 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> next turn
   PL: [OnSucceedAttackHead] Przy 10+ Liczniku Ładowania zyskuje w następnej turze 2 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Barier Ładunku</link></u></color>
138. [Umiejętność 2 (×2) (ulepszenia 2,4) — opis] [WhenUse] 자신의 충전 횟수 3 증가\n자신에게 보호막이 있을 때 합 위력 +2
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=2].desc ; dataList[id=1060602].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +3 Charge Count\nClash Power +2 when Shielded
   PL: [WhenUse] Zwiększa własny Licznik Ładowania o 3\nMoc Starcia +2 w posiadaniu Tarczy
139. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +3 Charge Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik Ładowania o 3
140. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수가 10 이상이면, 다음 턴에 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 2를 얻음
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Charge Count, gain 2 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> next turn
   PL: [OnSucceedAttack] Przy 10+ Liczniku Ładowania zyskuje w następnej turze 2 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Barier Ładunku</link></u></color>
141. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수가 5 이상이면, 다음 턴에 충전 횟수 5 당 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 1을 얻음 (최대 4)
   źródło: Skills_personality-06.json :: dataList[id=1060602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 5+ Charge Count, gain 1 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> for every 5 Charge Count next turn (Max 4)
   PL: [OnSucceedAttack] Przy 5+ Liczniku Ładowania zyskuje w następnej turze 1 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Barier Ładunku</link></u></color> za każde 5 Licznika Ładowania (maks. 4)
142. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 충전 역장 전개
   źródło: Skills_personality-06.json :: dataList[id=1060603].levelList[level=3].name ; dataList[id=1060603].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Deploy Charge Barrier
   PL: Rozmieszczenie Bariery Ładunku
143. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] [WhenUse] 자신의 충전 횟수가 10 이상이면, 충전 횟수를 전부 소모하여 자신을 포함하여 현재 체력 비율이 낮은 아군 2명에게 (소모한 충전 횟수/2)만큼 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 부여 (소수점 버림)
   źródło: Skills_personality-06.json :: dataList[id=1060603].levelList[level=3].desc ; dataList[id=1060603].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At 10+ Charge Count, consume all Charge Count to apply (Consumed Charge Count / 2) <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> (Rounded Down) to 2 allies with the lowest HP percentage
   PL: [WhenUse] Przy 10+ Liczniku Ładowania zużywa całe Ładowanie, aby nakładać (zużyte Ładowanie / 2) <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Barier Ładunku</link></u></color> na 2 sojuszników, łącznie z tą jednostką, z najniższym procentem HP (zaokrąglone w dół)
144. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 3 부여
   źródło: Skills_personality-06.json :: dataList[id=1060603].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture
   PL: [OnSucceedAttack] Nakłada 3 Rozdarcia
145. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 2를 얻음
   źródło: Skills_personality-06.json :: dataList[id=1060603].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1060603].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> next turn
   PL: [OnSucceedAttack] Zyskuje w następnej turze 2 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Bariery Ładunku</link></u></color>
146. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 파열 5 부여
   źródło: Skills_personality-06.json :: dataList[id=1060603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Rupture
   PL: [OnSucceedAttack] Nakłada 5 Rozdarcia
147. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-06.json :: dataList[id=1060604].levelList[level=1].name ; dataList[id=1060604].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 12 · monety: 1 (+6)
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Obrona (ulepszenie 1) — opis] [WhenUse] <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 2를 얻음 (턴 당 최대 3회)
   źródło: Skills_personality-06.json :: dataList[id=1060604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> (3 times per turn)
   PL: [WhenUse] Zyskuje 2 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Bariery Ładunku</link></u></color> (maks. 3 razy na turę)
149. [Obrona (ulepszenie 4) — opis] [WhenUse] <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> <style="highlight">3</style>을 얻음 (턴 당 최대 3회)
   źródło: Skills_personality-06.json :: dataList[id=1060604].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, <style="highlight">, </style>, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain <style="highlight">3</style> <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> (3 times per turn)
   PL: [WhenUse] Zyskuje <style="highlight">3</style> <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Barier Ładunku</link></u></color> (maks. 3 razy na turę)
150. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — nazwa] 익숙해진 정리 업무
   źródło: Passives.json :: dataList[id=1060601].name
   limit: do 40 znaków
   EN: Cleanup Mastery
   PL: Opanowane Oczyszczanie
151. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — opis] 전투 시작 시 충전 횟수가 5 이상 있으면, 다음 턴에 신속 2를 얻음
   źródło: Passives.json :: dataList[id=1060601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: If at 5+ Charge Count at the start of the combat phase, gain 2 [Agility] next turn
   PL: Na początku walki przy 5+ Liczniku Ładowania zyskuje 2 Pośpiechu w następnej turze
152. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — nazwa] 열차 정리 매뉴얼 전달
   źródło: Passives.json :: dataList[id=1060621].name
   limit: do 40 znaków
   EN: Train Cleanup Manual
   PL: Przekazanie Podręcznika Oczyszczania
153. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Pride) — opis] 속도가 가장 느린 아군이 전투 시작 시 충전 횟수가 5 이상 있으면, 다음 턴에 신속 2를 얻음
   źródło: Passives.json :: dataList[id=1060621].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: An ally with the slowest Speed gains 2 [Agility] next turn if at 5+ Charge Count at the start of the combat phase
   PL: Sojusznik z najniższą Szybkością zyskuje 2 Pośpiechu w następnej turze, jeżeli na początku walki ma 5+ Licznika Ładowania

## [00] Hook Office Fixer — Hong Lu — 갈고리 사무소 해결사
- ID Tożsamości: `10607` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: wydarzenie 9101 · HP bazowe: 69 · szybkość: 2–6 / 2–7 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed

154. [Karta Tożsamości — tytuł] 갈고리 사무소\n해결사
   źródło: Personalities.json :: dataList[id=10607].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hook Office\nFixer
   PL: Biuro Haka\nFikser
155. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10607].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10607].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Karta Tożsamości — opis] 홍루의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10607].desc
   limit: do 120 znaków
   EN: Hong Lu's 7th Identity
   PL: Siódma Tożsamość Hong Lu
158. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 추적
   źródło: Skills_personality-06.json :: dataList[id=1060701].levelList[level=1].name ; dataList[id=1060701].levelList[level=2].name ; dataList[id=1060701].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Track
   PL: Pościg
159. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1060701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL: [OnSucceedAttackHead] Nakłada 1 Krwawienia
160. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1060701].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1060701].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1060701].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Bleed Count
   PL: [OnSucceedAttackHead] Zwiększa Licznik Krwawienia o 1
161. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1060701].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 신속 이 2 이상이면, 최종 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1060701].levelList[level=4].desc
   limit: do 120 znaków
   EN: At 2+ Haste, Final Power +1
   PL: Przy 2+ Pośpiechu Moc Końcowa +1
163. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 먼저 간다
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=1].name ; dataList[id=1060702].levelList[level=2].name ; dataList[id=1060702].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Goin' First
   PL: Idzie Pierwszy
164. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 다음 턴에 신속 1을 얻음
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Haste next turn
   PL: [WhenUse] Zyskuje w następnej turze 1 Pośpiechu
165. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1060702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1060702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신이 대상보다 속도가 높은 경우, 자신과 대상의 속도 차이만큼 출혈 횟수 증가 (최대 2)
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If this unit is faster than the target, inflict Bleed Count equal to their Speed difference (Max 2)
   PL: [OnSucceedAttack] Jeżeli ta jednostka jest szybsza niż cel, zwiększa Licznik Krwawienia o różnicę Szybkości (maks. 2)
168. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 다음 턴에 신속 2를 얻음
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Haste next turn
   PL: [WhenUse] Zyskuje w następnej turze 2 Pośpiechu
169. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신이 대상보다 속도가 높은 경우, 자신과 대상의 속도 차이만큼 출혈 횟수 증가 (최대 3)
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If this unit is faster than the target, inflict Bleed Count equal to their Speed difference (Max 3)
   PL: [OnSucceedAttack] Jeżeli ta jednostka jest szybsza niż cel, zwiększa Licznik Krwawienia o różnicę Szybkości (maks. 3)
170. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 속도가 6 이상이면, 코인 위력 +1\n[WhenUse] 다음 턴에 신속 2를 얻음
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: At 6+ Speed, Coin Power +1\n[WhenUse] Gain 2 Haste next turn
   PL: Przy 6+ Szybkości Moc Monet +1\n[WhenUse] Zyskuje w następnej turze 2 Pośpiechu
171. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신이 대상보다 속도가 높은 경우, 자신과 대상의 속도 차이만큼 출혈 횟수 증가 (최대 4)
   źródło: Skills_personality-06.json :: dataList[id=1060702].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If this unit is faster than the target, inflict Bleed Count equal to their Speed difference (Max 4)
   PL: [OnSucceedAttack] Jeżeli ta jednostka jest szybsza niż cel, zwiększa Licznik Krwawienia o różnicę Szybkości (maks. 4)
172. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 광란
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=3].name ; dataList[id=1060703].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Rampage
   PL: Furia
173. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 8 이상이면, 코인 위력 +1\n대상의 잃은 체력에 비례하여 피해량이 증가함. (대상의 잃은 체력 1% 당 피해량 0.3% 증가)
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 8+ Speed, Coin Power +1\nDeal more damage based on target's missing HP (+0.3% damage per 1% missing HP)
   PL: Przy 8+ Szybkości Moc Monet +1\nZadaje więcej obrażeń w zależności od brakującego HP celu (+0.3% obrażeń za każde 1% brakującego HP)
174. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 대상의 출혈 1당 정신력 1 회복 (최대 5)
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal 1 SP per Bleed on target (Max 5)
   PL: [OnSucceedAttackHead] Odzyskuje 1 Poczytalności za każde 1 Krwawienia celu (maks. 5)
175. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 속도가 6 이상이면, 코인 위력 +1\n대상의 잃은 체력에 비례하여 피해량이 증가함. (대상의 잃은 체력 1% 당 피해량 0.5% 증가)
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 6+ Speed, Coin Power +1\nDeal more damage based on target's missing HP (+0.5% damage per 1% missing HP)
   PL: Przy 6+ Szybkości Moc Monet +1\nZadaje więcej obrażeń w zależności od brakującego HP celu (+0.5% obrażeń za każde 1% brakującego HP)
178. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 대상의 출혈 1당 정신력 1 회복 (최대 10)
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal 1 SP per Bleed on target (Max 10)
   PL: [OnSucceedAttackHead] Odzyskuje 1 Poczytalności za każde 1 Krwawienia celu (maks. 10)
179. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 출혈 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1060703].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Obrona (ulepszenia 1,4) — nazwa] 재빠름
   źródło: Skills_personality-06.json :: dataList[id=1060704].levelList[level=1].name ; dataList[id=1060704].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 3 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Quickness
   PL: Zwinność
182. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 신속 1을 얻음 (턴 당 최대 3회)
   źródło: Skills_personality-06.json :: dataList[id=1060704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Gain 1 Haste next turn (3 times per turn)
   PL: [OnSucceedEvade] Zyskuje w następnej turze 1 Pośpiechu (maks. 3 razy na turę)
183. [Obrona (ulepszenie 4) — opis] 대상의 출혈 이 7 이상이면 코인 위력 +2\n[OnSucceedEvade] 다음 턴에 신속 1을 얻음 (턴 당 최대 3회)
   źródło: Skills_personality-06.json :: dataList[id=1060704].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: If target has 7+ Bleed, gain +2 Coin Power\n[OnSucceedEvade] Gain 1 Haste next turn (3 times per turn)
   PL: Jeżeli cel ma 7+ Krwawienia, Moc Monet +2\n[OnSucceedEvade] Zyskuje w następnej turze 1 Pośpiechu (maks. 3 razy na turę)
184. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Lust) — nazwa] 갈고리
   źródło: Passives.json :: dataList[id=1060701].name
   limit: do 40 znaków
   EN: Hook
   PL: Hak
185. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Lust) — opis] 적 처치 시 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 최대 1회)
   źródło: Passives.json :: dataList[id=1060701].desc
   limit: do 120 znaków
   EN: Upon defeating an enemy, gain 1 Attack Power Up next turn (Once per turn)
   PL: Po pokonaniu wroga zyskuje w następnej turze 1 Wzrostu Mocy Ataku (maks. 1 raz na turę)
186. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — nazwa] 보급형 생체 장비
   źródło: Passives.json :: dataList[id=1060721].name
   limit: do 40 znaków
   EN: Mass-produced Bionic Gear
   PL: Masowo Produkowany Bioniczny Sprzęt
187. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — opis] 속도가 가장 빠른 아군 1명이 <sprite name="Laceration"><color=#e30000><u><link="Laceration">출혈</color></link></u>이 부여된 적 처치 시 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 최대 1회)
   źródło: Passives.json :: dataList[id=1060721].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <sprite name="Laceration">, <color=#e30000>, <u>, <link="Laceration">, </color>, </link>, </u>
   EN: When 1 ally with the fastest Speed defeats an enemy that has <sprite name="Laceration"><color=#e30000><u><link="Laceration">Bleed</color></link></u>, gain 1 Attack Power Up next turn (Once per turn)
   PL: Gdy 1 Sojusznik z najwyższą Szybkością pokonuje wroga z <sprite name="Laceration"><color=#e30000><u><link="Laceration">Krwawieniem</link></u></color>, zyskuje 1 Wzrostu Mocy Ataku w następnej turze (maks. 1 raz na turę)

## [000] Dieci Assoc. South Section 4 — Hong Lu — 남부 디에치 협회 4과
- ID Tożsamości: `10608` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 79 · szybkość: 2–6 / 2–7 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Sinking

188. [Karta Tożsamości — tytuł] 남부 디에치 협회\n4과
   źródło: Personalities.json :: dataList[id=10608].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Dieci Assoc.\nSouth Section 4
   PL: Południowe Stowarzyszenie Dieci\nSekcja 4
189. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10608].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10608].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Karta Tożsamości — opis] 홍루의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10608].desc
   limit: do 120 znaków
   EN: Hong Lu's 8th Identity
   PL: Ósma Tożsamość Hong Lu
192. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 지식 소모
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=1].name ; dataList[id=1060801].levelList[level=2].name ; dataList[id=1060801].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 5 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Expend Knowledge
   PL: Wydatkowanie Wiedzy
193. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots
   PL: [WhenUse] Odrzuca 1 Umiejętność najwyższego poziomu ze wszystkich slotów Umiejętności tej jednostki
194. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Sinking] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1060801].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060801].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict +1 [Sinking] Count
   PL: [OnSucceedAttackHead] Zwiększa Licznik [Sinking] celu o 1
195. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림\n[WhenUse] [KnowledgeExplored]이 3 이상이면, 합 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [KnowledgeExplored]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots\n[WhenUse] At 3+ [KnowledgeExplored], Clash Power +1
   PL: [WhenUse] Odrzuca 1 Umiejętność najwyższego poziomu ze wszystkich slotów Umiejętności tej jednostki\n[WhenUse] Przy 3+ [KnowledgeExplored] Moc Starcia +1
196. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [KnowledgeExplored]이 3 이상이면, 코인 1회 재사용
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [KnowledgeExplored]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [OnSucceedAttack] At 3+ [KnowledgeExplored], reuse Coin once
   PL: [OnSucceedAttack] Przy 3+ [KnowledgeExplored] ponownie używa monety 1 raz
197. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 등급이 가장 높은 스킬 1개를 버림\n[WhenUse] ([KnowledgeExplored] - 1)만큼 합 위력이 증가
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [KnowledgeExplored]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [WhenUse] Discard 1 Skill of the highest rank in all of this unit's Skill Slots\n[WhenUse] Clash Power +([KnowledgeExplored] - 1)
   PL: [WhenUse] Odrzuca 1 Umiejętność najwyższego poziomu ze wszystkich slotów Umiejętności tej jednostki\n[WhenUse] Zyskuje Moc Starcia równą ([KnowledgeExplored] - 1)
198. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] ([KnowledgeExplored] - 1)만큼 코인 재사용
   źródło: Skills_personality-06.json :: dataList[id=1060801].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [KnowledgeExplored]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [OnSucceedAttack] Reuse Coin ([KnowledgeExplored] - 1) times
   PL: [OnSucceedAttack] Ponownie używa monet ([KnowledgeExplored] - 1) razy
199. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 열어 젖히기
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=1].name ; dataList[id=1060802].levelList[level=2].name ; dataList[id=1060802].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Unveil
   PL: Odsłonięcie
200. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 무작위 스킬 2개를 등급이 낮은 순으로 버림
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Randomly Discard 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots
   PL: [WhenUse] Losowo odrzuca 2 Umiejętności tej jednostki ze wszystkich slotów Umiejętności, w kolejności od najniższego poziomu
201. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] [Sinking] 3 부여
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Sinking]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttackHead] Inflict 3 [Sinking]
   PL: [OnSucceedAttackHead] Nakłada 3 [Sinking]
202. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 무작위 스킬 2개를 등급이 낮은 순으로 버림\n[WhenUse] [KnowledgeExplored]이 3 이상이면, 코인 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [KnowledgeExplored]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [WhenUse] Randomly Discard 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots\n[WhenUse] At 3+ [KnowledgeExplored], Coin Power +1
   PL: [WhenUse] Losowo odrzuca 2 Umiejętności tej jednostki ze wszystkich slotów Umiejętności, w kolejności od najniższego poziomu\n[WhenUse] Przy 3+ [KnowledgeExplored] Moc Monet +1
203. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL: [OnSucceedAttack] Nakłada 3 [Sinking]
204. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 무작위 스킬 2개를 등급이 낮은 순으로 버림\n[WhenUse] ([KnowledgeExplored] - 1)만큼 코인 위력이 증가
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [KnowledgeExplored]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: [WhenUse] Randomly Discard 2 of this unit's Skills in ascending order of ranks from all of its Skill Slots\n[WhenUse] Coin Power +([KnowledgeExplored] - 1)
   PL: [WhenUse] Losowo odrzuca 2 Umiejętności tej jednostki ze wszystkich slotów Umiejętności, w kolejności od najniższego poziomu\n[WhenUse] Moc Monet +([KnowledgeExplored] - 1)
205. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_personality-06.json :: dataList[id=1060802].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL: [OnSucceedAttack] Nakłada 4 [Sinking]
206. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 순환하는 지식
   źródło: Skills_personality-06.json :: dataList[id=1060803].levelList[level=3].name ; dataList[id=1060803].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Cyclical Knowledge
   PL: Cykliczna Wiedza
207. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] [KnowledgeExplored]이 2 이상이면, [KnowledgeExplored] 만큼 코인 위력이 증가\n대상의 [Sinking] 1당 피해량 +1.5% (최대 15%)
   źródło: Skills_personality-06.json :: dataList[id=1060803].levelList[level=3].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] At 2+ [KnowledgeExplored], gain Coin Power equal to [KnowledgeExplored]\nDeal +1.5% damage per [Sinking] on target (Max 15%)
   PL: [WhenUse] Przy 2+ [KnowledgeExplored] zyskuje Moc Monet równą [KnowledgeExplored]\nZadaje +1.5% obrażeń za każde 1 [Sinking] celu (maks. 15%)
208. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1060803].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Sinking]
209. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [EndSkill] 대상이 흐트러짐 상태가 되거나 사망하면, 정신력 10 회복
   źródło: Skills_personality-06.json :: dataList[id=1060803].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1060803].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]
   EN: [EndSkill] If target is Staggered or defeated, heal 10 SP
   PL: [EndSkill] Jeżeli cel zostanie Ogłuszony albo pokonany, odzyskuje 10 Poczytalności
210. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] [KnowledgeExplored]이 2 이상이면, [KnowledgeExplored]만큼 코인 위력이 증가\n대상의 [Sinking] 1당 피해량 +3% (최대 30%)
   źródło: Skills_personality-06.json :: dataList[id=1060803].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [KnowledgeExplored], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [KnowledgeExplored] = 탐구한 지식 / Insight; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] At 2+ [KnowledgeExplored], gain Coin Power equal to [KnowledgeExplored]\nDeal +3% damage per [Sinking] on target (Max 30%)
   PL: [WhenUse] Przy 2+ [KnowledgeExplored] zyskuje Moc Monet równą [KnowledgeExplored]\nZadaje +3% obrażeń za każde 1 [Sinking] celu (maks. 30%)
211. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 4 증가
   źródło: Skills_personality-06.json :: dataList[id=1060803].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +4 [Sinking] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] celu o 4
212. [Obrona (ulepszenia 1,4) — nazwa] 인도하는 걸음
   źródło: Skills_personality-06.json :: dataList[id=1060804].levelList[level=1].name ; dataList[id=1060804].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Guiding Steps
   PL: Kroki Wędrownego Przewodnika
213. [Obrona (ulepszenia 1,4) — opis] [WhenUse] 자신의 모든 스킬 슬롯에서 무작위 스킬 2개를 등급이 낮은 순으로 버림
   źródło: Skills_personality-06.json :: dataList[id=1060804].levelList[level=1].desc ; dataList[id=1060804].levelList[level=4].desc
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — nazwa] 열쇠 들여다보기
   źródło: Passives.json :: dataList[id=1060801].name
   limit: do 40 znaków
   EN: Peering Through a Key
   PL: Wgląd przez Klucz
215. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Gloom) — opis] 자신이 스킬을 버릴 때 버린 스킬의 등급만큼 [AttackDmgUp]를 얻음. (턴 당 최대 3)
   źródło: Passives.json :: dataList[id=1060801].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: When Discarding a Skill, gain [AttackDmgUp] equal to the Discarded Skill's Rank. (Max 3 per turn)
   PL: Odrzucając Umiejętność, zyskuje [AttackDmgUp] równy poziomowi odrzuconej Umiejętności. (maks. 3 na turę)
216. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — nazwa] 열쇠 들여다보기
   źródło: Passives.json :: dataList[id=1060811].name
   (powtórzenie elementu 214 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Pasywka bojowa (od ulepszenia 4, rezonans 3× Gloom) — opis] 자신이 스킬을 버릴 때 버린 스킬의 등급만큼 [AttackDmgUp]를 얻음. (턴 당 최대 3)\n자신을 제외한 아군이 스킬을 버릴 때, 버린 스킬의 등급이 자신의 [KnowledgeExplored]보다 높으면, 자신의 [KnowledgeExplored] +1
   źródło: Passives.json :: dataList[id=1060811].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDmgUp], [KnowledgeExplored]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [KnowledgeExplored] = 탐구한 지식 / Insight
   EN: When Discarding a Skill, gain [AttackDmgUp] equal to the Discarded Skill Rank. (Max 3 per turn)\nWhen other allies Discard a Skill, and if the ally's Discarded Skill Rank is higher than this unit's [KnowledgeExplored] value, this unit gains +1 [KnowledgeExplored].
   PL: Odrzucając Umiejętność, zyskuje [AttackDmgUp] równy poziomowi odrzuconej Umiejętności. (maks. 3 na turę)\nGdy inny sojusznik odrzuca Umiejętność, jeżeli jej poziom jest wyższy niż [KnowledgeExplored] tej jednostki, zyskuje +1 [KnowledgeExplored].
218. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — nazwa] 깨우침
   źródło: Passives.json :: dataList[id=1060821].name
   limit: do 40 znaków
   EN: Enlightenment
   PL: Oświecenie
219. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Gloom) — opis] 정신력이 가장 낮은 아군 1명이 공격 종료 후 대상을 흐트러짐 상태로 만들거나, 처치하면 정신력 7 회복
   źródło: Passives.json :: dataList[id=1060821].desc
   limit: do 170 znaków
   EN: Attack End: If the target is in a staggered or defeated state by an attack from 1 ally with the least SP, the ally heals 7 SP.
   PL: Gdy 1 Sojusznik z najniższą Poczytalnością Ogłusza albo pokonuje cel na koniec ataku, ten sojusznik odzyskuje 7 Poczytalności.

## [000] District 20 Yurodivy — Hong Lu — 20구 유로지비
- ID Tożsamości: `10609` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 4 · HP bazowe: 70 · szybkość: 3–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Tremor

220. [Karta Tożsamości — tytuł] 20구\n유로지비
   źródło: Personalities.json :: dataList[id=10609].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: District 20\nYurodivy
   PL: Dystrykt 20\nJurodiwyj
221. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10609].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10609].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Karta Tożsamości — opis] 홍루의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10609].desc
   limit: do 120 znaków
   EN: Hong Lu's 9th Identity
   PL: Dziewiąta Tożsamość Hong Lu
224. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 추리시작
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=1].name ; dataList[id=1060901].levelList[level=2].name ; dataList[id=1060901].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Deduction Start
   PL: Początek Dedukcji
225. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=1].desc ; dataList[id=1060901].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 2
226. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Vibration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict 2 [Vibration]
   PL: [OnSucceedAttackHead] Nakłada 2 [Vibration]
227. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Gain +2 [Vibration] Count
   PL: [OnSucceedAttackHead] Zwiększa własny Licznik [Vibration] o 2
228. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
229. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1060901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain +2 [Vibration] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Vibration] o 2
230. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">자신의 [Vibration] 횟수가 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-06.json :: dataList[id=1060901].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n<style="highlight">At 6+ [Vibration] Count, Coin Power +1</style>
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 2\n<style="highlight">Przy 6+ Liczniku [Vibration] Moc Monet +1</style>
231. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 변형 지팡이 호신술
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=1].name ; dataList[id=1060902].levelList[level=2].name ; dataList[id=1060902].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Morph Cane Technique
   PL: Technika Morfującej Laski
232. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +3 [Vibration] Count
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 3
233. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1060902].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1060902].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain +3 [Vibration] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Vibration] o 3
234. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]이 9 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 9+ [Vibration], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Jeżeli cel ma 9+ [Vibration], wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
236. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Vibration]이 8 이상이면, 합 위력 +1</style>\n[WhenUse] 자신의 [Vibration] 횟수 3 증가\n<style="highlight">자신의 [Vibration] 횟수가 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[WhenUse] If target has 8+ [Vibration], Clash Power +1</style>\n[WhenUse] Gain +3 [Vibration] Count\n<style="highlight">At 6+ [Vibration] Count, Coin Power +1</style>
   PL: <style="highlight">[WhenUse] Jeżeli cel ma 8+ [Vibration], Moc Starcia +1</style>\n[WhenUse] Zwiększa własny Licznik [Vibration] o 3\n<style="highlight">Przy 6+ Liczniku [Vibration] Moc Monet +1</style>
237. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Vibration]
238. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]이 <style="highlight">7</style> 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has <style="highlight">7</style>+ [Vibration], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Jeżeli cel ma <style="highlight">7</style>+ [Vibration], wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
239. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Vibration]이 <style="highlight">6</style> 이상이면, 합 위력 +1\n[WhenUse] 자신의 [Vibration] 횟수 3 증가\n자신의 [Vibration] 횟수가 <style="highlight">5</style> 이상이면, 코인 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has <style="highlight">6</style>+ [Vibration], Clash Power +1\n[WhenUse] Gain +3 [Vibration] Count\nAt <style="highlight">5</style>+ [Vibration] Count, Coin Power +1
   PL: [WhenUse] Jeżeli cel ma <style="highlight">6</style>+ [Vibration], Moc Starcia +1\n[WhenUse] Zwiększa własny Licznik [Vibration] o 3\nPrzy <style="highlight">5</style>+ Liczniku [Vibration] Moc Monet +1
240. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Vibration]<style="highlight"></style>
241. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration]이 <style="highlight">6</style> 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-06.json :: dataList[id=1060902].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has <style="highlight">6</style>+ [Vibration], trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Jeżeli cel ma <style="highlight">6</style>+ [Vibration], wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
242. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 범인은 당신이군요!
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=3].name ; dataList[id=1060903].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 3 · monety: 4 (+3)
   limit: do 40 znaków
   EN: You're the Culprit!
   PL: To Pan jest sprawcą!
243. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 [Vibration]이 6 이상이면 합 위력 +1\n[WhenUse] 자신의 [Vibration] 횟수를 10 소모하여 코인 위력 +2
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 6+ [Vibration], Clash Power +1\n[WhenUse] Consume 10 [Vibration] Count on self to gain Coin Power +2
   PL: [WhenUse] Jeżeli cel ma 6+ [Vibration], Moc Starcia +1\n[WhenUse] Zużywa 10 Licznika [Vibration], aby zyskać Moc Monet +2
244. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 스킬 사용시 [Vibration] 횟수를 소모했다면, [VibrationEcho]으로 [FusionVibration]
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1060903].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationEcho], [FusionVibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationEcho] = 진동 - 반향 / Tremor - Reverb; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: [OnSucceedAttack] If this Skill consumed [Vibration] Count on use, trigger [FusionVibration] into [VibrationEcho]
   PL: [OnSucceedAttack] Jeżeli ta Umiejętność zużyła Licznik [Vibration] przy użyciu, wywołuje [FusionVibration] przechodzące w [VibrationEcho]
245. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1060903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
246. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- 스킬 사용시 [Vibration] 횟수를 소모하지 못했다면, 위 효과 발동 후 자신에게 [VibrationExplosion]
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- If this unit did not consume [Vibration] Count with Skill use, activate the above effect, then trigger [VibrationExplosion] on self
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1\n- Jeżeli nie zdołała zużyć Licznika [Vibration] przy użyciu Umiejętności, uruchamia powyższy efekt, po czym wywołuje [VibrationExplosion] na sobie
247. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 대상의 [Vibration] <style="highlight">6당</style> 합 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 <style="highlight">[Vibration] 횟수가 15 미만이면,</style> [Vibration] 횟수 10 소모하여 코인 위력 +2\n<style="highlight">[WhenUse] 자신의 [Vibration] 횟수를 15 소모하여 코인 위력 +3</style>
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=4].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Clash Power +1 for every <style="highlight">6</style> [Vibration] on target <style="highlight">(max 2)</style>\n[WhenUse] At <style="highlight"> less than 15 [Vibration] Count on self</style>, consume 10 [Vibration] Count to gain Coin Power +2\n<style="highlight">[WhenUse] Consume 15 [Vibration] Count on self to gain Coin Power +3</style>
   PL: [WhenUse] Moc Starcia +1 za każde <style="highlight">6</style> [Vibration] celu <style="highlight">(maks. 2)</style>\n[WhenUse] Przy <style="highlight">mniej niż 15 Licznika [Vibration]</style> zużywa 10 Licznika [Vibration], aby zyskać Moc Monet +2\n<style="highlight">[WhenUse] Zużywa 15 Licznika [Vibration], aby zyskać Moc Monet +3</style>
248. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 스킬 사용시 [Vibration] 횟수를 10 이상 소모했다면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: <style="highlight">[OnSucceedAttack] If this Skill consumed 10+ [Vibration] Count on Skill Use, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli ta Umiejętność zużyła 10+ Licznika [Vibration] przy użyciu, wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1</style>
249. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 스킬 사용시 [Vibration] 횟수를 10 이상 소모했다면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- 소모한 [Vibration] 횟수가 15 미만이면, 위 효과 발동 후 자신에게도 [VibrationExplosion]</style>
   źródło: Skills_personality-06.json :: dataList[id=1060903].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: <style="highlight">[OnSucceedAttack] If this Skill consumed 10+ [Vibration] Count on Skill Use, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- If this unit consumed less than 15 [Vibration] Count, trigger [VibrationExplosion] on self after activating the above effect</style>
   PL: <style="highlight">[OnSucceedAttack] Jeżeli ta Umiejętność zużyła 10+ Licznika [Vibration] przy użyciu, wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1\n- Jeżeli zużyła mniej niż 15 Licznika [Vibration], wywołuje [VibrationExplosion] na sobie po uruchomieniu powyższego efektu</style>
250. [Obrona (ulepszenia 1,4) — nazwa] 잠깐만요?!
   źródło: Skills_personality-06.json :: dataList[id=1060904].levelList[level=1].name ; dataList[id=1060904].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Wait?!
   PL: Chwileczkę?!
251. [Obrona (ulepszenie 1) — opis] [WhenUse] 대상의 [Vibration] 횟수의 2배만큼 보호막 체력을 얻음 (최대 7)
   źródło: Skills_personality-06.json :: dataList[id=1060904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain 2 x ([Vibration] Count on target) as Shield HP (max 7)
   PL: [WhenUse] Zyskuje Tarczę równą 2 x (Licznik [Vibration] celu) (maks. 7)
252. [Obrona (ulepszenie 4) — opis] [WhenUse] 대상의 [Vibration] 횟수의 2배만큼 보호막 체력을 얻음 (최대 <style="highlight">13</style>)
   źródło: Skills_personality-06.json :: dataList[id=1060904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain 2 x ([Vibration] Count on target) as Shield HP (max <style="highlight">13</style>)
   PL: [WhenUse] Zyskuje Tarczę równą 2 x (Licznik [Vibration] celu) (maks. <style="highlight">13</style>)
253. [Pasywka bojowa (od ulepszenia 2, posiadane 6× Sloth) — nazwa] 진동유착 변형 전투 지팡이 (미허가 발명품)
   źródło: Passives.json :: dataList[id=1060901].name
   limit: do 70 znaków
   EN: Vibroweld Morph-combat Cane (Unauthorized Invention)
   PL: Wibrozgrzewana Morfująca Laska Bojowa (Nieautoryzowany Wynalazek)
254. [Pasywka bojowa (od ulepszenia 2, posiadane 6× Sloth) — opis] 턴 종료 시 이번 턴에 자신이 [VibrationExplosion]을 시킨 횟수만큼 다음 턴에 [AttackDmgUp]를 얻음 (최대 3)
   źródło: Passives.json :: dataList[id=1060901].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion], [AttackDmgUp]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn End: gain [AttackDmgUp] next turn equal to the number of times this unit triggered [VibrationExplosion] this turn (max 3)
   PL: Na koniec tury zyskuje w następnej turze [AttackDmgUp] równy liczbie [VibrationExplosion] wywołanych przez tę jednostkę w tej turze (maks. 3)
255. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — nazwa] 내가 범인이라면...?
   źródło: Passives.json :: dataList[id=1060921].name
   limit: do 40 znaków
   EN: In the Culprit's Shoes
   PL: A gdybym był sprawcą...?
256. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — opis] 편성 순서 1번인 아군의 스킬, 코인 효과로 [VibrationExplosion] 시 25% 확률로 [VibrationExplosion]이 1회 추가로 발동 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1060921].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: When #1 Deployed Identity triggers Tremor Burst with Skill or Coin effects, 25% chance to trigger an additional Tremor Burst (once per turn)
   PL: Gdy Tożsamość przydzielona na 1. pozycji wywołuje [VibrationExplosion] efektami Umiejętności lub monet, 25% szans na dodatkowe wywołanie 1 [VibrationExplosion] (1 raz na turę)

## [00] Fanghunt Office Fixer — Hong Lu — 송곳니 사냥 사무소 해결사
- ID Tożsamości: `10610` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 5 · HP bazowe: 73 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Rupture

257. [Karta Tożsamości — tytuł] 송곳니 사냥 사무소\n해결사
   źródło: Personalities.json :: dataList[id=10610].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Fanghunt Office\nFixer
   PL: Biuro Fanghunt\nFikser
258. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10610].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10610].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Karta Tożsamości — opis] 홍루의 열번째 인격
   źródło: Personalities.json :: dataList[id=10610].desc
   limit: do 120 znaków
   EN: Hong Lu’s 10th Identity
   PL: Dziesiąta Tożsamość Hong Lu
261. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 내려치기
   źródło: Skills_personality-06.json :: dataList[id=1061001].levelList[level=1].name ; dataList[id=1061001].levelList[level=2].name ; dataList[id=1061001].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Slam
   PL: Rozbicie
262. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061001].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1061001].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1061001].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL: [OnSucceedAttack] Nakłada 1 [Burst]
263. [Umiejętność 1 (×3) (ulepszenia 2,4) — opis] 대상의 [Burst]이 6 이상일 때, 코인 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1061001].levelList[level=2].desc ; dataList[id=1061001].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If target has 6+ [Burst], Coin Power +1
   PL: Jeżeli cel ma 6+ [Burst], Moc Monet +1
264. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061001].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061001].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 1 [Burst]
   PL: [OnSucceedAttackHead] Nakłada 1 [Burst]
266. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061001].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 뼈 부수기
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=1].name ; dataList[id=1061002].levelList[level=2].name ; dataList[id=1061002].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Bonecrusher
   PL: Łamacz Kości
268. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1061002].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] Nakłada 2 [Burst]
269. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬에서 [Burst]과 [Burst] 횟수를 부여하지 않는 대신 코인 위력 +1\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not inflict [Burst] or [Burst] Count; instead, gain Coin Power +1\n[WinDuel] Inflict +1 [Burst] Count
   PL: [WhenUse] Jeżeli cel ma 15+ [Burst] Mocy i 3+ Licznika [Burst], ta Umiejętność nie nakłada [Burst] ani Licznika [Burst]; zamiast tego zyskuje Moc Monet +1\n[WinDuel] Zwiększa Licznik [Burst] celu o 1
270. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1061002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]
271. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [TakeHpHealReduce] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TakeHpHealReduce]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down
   EN: [OnSucceedAttack] Inflict 1 [TakeHpHealReduce] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [TakeHpHealReduce]
272. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Burst]이 6 이상일 때, 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬에서 [Burst]과 [Burst] 횟수를 부여하지 않는 대신 코인 위력 +1\n- 대상이 <혈귀>, <피주머니>면, 추가로 코인 위력 +1\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If target has 6+ [Burst], Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not inflict [Burst] or [Burst] Count; instead, gain Coin Power +1\n- If target is a <Bloodfiend> or a <Bloodbag>, gain an additional Coin Power +1\n[WinDuel] Inflict +1 [Burst] Count
   PL: Jeżeli cel ma 6+ [Burst], Moc Monet +1\n[WhenUse] Jeżeli cel ma 15+ [Burst] Mocy i 3+ Licznika [Burst], ta Umiejętność nie nakłada [Burst] ani Licznika [Burst]; zamiast tego zyskuje Moc Monet +1\n- Jeżeli cel jest <Krwiożercą> albo <Workiem Krwi>, zyskuje dodatkowo Moc Monet +1\n[WinDuel] Zwiększa Licznik [Burst] celu o 1
273. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Burst] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict +1 [Burst] Count
   PL: [OnSucceedAttackHead] Zwiększa Licznik [Burst] celu o 1
274. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [TakeHpHealReduce] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061002].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TakeHpHealReduce]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TakeHpHealReduce] = 체력 회복 감소 / HP Healing Down
   EN: [OnSucceedAttack] Inflict 2 [TakeHpHealReduce] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 2 [TakeHpHealReduce]
275. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 상쾌한 사냥 마무리
   źródło: Skills_personality-06.json :: dataList[id=1061003].levelList[level=3].name ; dataList[id=1061003].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: A Cheerful Hunt's End
   PL: Radosne Zakończenie Polowania
276. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬에서 [Burst]과 [Burst] 횟수를 부여하지 않는 대신 코인 위력 +1\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061003].levelList[level=3].desc
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061003].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1061003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Burst] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061003].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1061003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Burst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttackHead] Inflict 2 [Burst]
   PL: [OnSucceedAttackHead] Nakłada 2 [Burst]
279. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Burst]이 6 이상일 때, 코인 위력 +1\n[WhenUse] 대상의 [Burst]이 15, [Burst] 횟수가 3 이상이면, 이 스킬에서 [Burst]과 [Burst] 횟수를 부여하지 않는 대신 코인 위력 +1\n- 대상이 <혈귀>, <피주머니>면, 추가로 코인 위력 +1\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061003].levelList[level=4].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If target has 6+ [Burst], Coin Power +1\n[WhenUse] If target has 15+ [Burst] and 3+ [Burst] Count: this Skill does not inflict [Burst] or [Burst] Count; instead, gain Coin Power +1\n- If target is a <Bloodfiend> or a <Bloodbag>, gain an additional Coin Power +1\n[WinDuel] Inflict +2 [Burst] Count
   PL: Jeżeli cel ma 6+ [Burst], Moc Monet +1\n[WhenUse] Jeżeli cel ma 15+ [Burst] Mocy i 3+ Licznika [Burst], ta Umiejętność nie nakłada [Burst] ani Licznika [Burst]; zamiast tego zyskuje Moc Monet +1\n- Jeżeli cel jest <Krwiożercą> albo <Workiem Krwi>, zyskuje dodatkowo Moc Monet +1\n[WinDuel] Zwiększa Licznik [Burst] celu o 2
280. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 [Burst]이 15 이상이거나, 대상의 현재 체력이 최대 체력의 30% 미만이면, 이 코인 재사용 (스킬 당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] If target has 15+ [Burst], or has less than 30% HP, Reuse this Coin (once per Skill)
   PL: [OnSucceedAttack] Jeżeli cel ma 15+ [Burst] albo mniej niż 30% HP, ponownie używa tej monety (1 raz na Umiejętność)
281. [Obrona (ulepszenia 1,4) — nazwa] 긴급 지혈
   źródło: Skills_personality-06.json :: dataList[id=1061004].levelList[level=1].name ; dataList[id=1061004].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Emergency Styptics
   PL: Awaryjny Środek Zatrzaskujący
282. [Obrona (ulepszenie 4) — opis] [StartBattle] 자신의 [Laceration] 위력 2 감소 (턴 당 3회. [Laceration]이 감소하여 0 이하가 되면, 출혈 소멸)
   źródło: Skills_personality-06.json :: dataList[id=1061004].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Laceration] = 출혈 / Bleed
   EN: [StartBattle] Lose 2 [Laceration] Potency on self (3 times per turn. If [Laceration] Potency drops to 0 or less, the Bleed effect expires)
   PL: [StartBattle] Traci 2 Mocy [Laceration] (3 razy na turę. Jeżeli [Laceration] spadnie do 0 lub mniej, Krwawienie wygasa)
283. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — nazwa] 유쾌한 사냥법
   źródło: Passives.json :: dataList[id=1061001].name
   limit: do 40 znaków
   EN: How to Hunt Cheerfully
   PL: Jak Polować z Uśmiechem
284. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Glut.) — opis] 대상이 <혈귀>, <피주머니>면 피해량 +10%\n스킬 사용시 자신에게 [Laceration]이 있으면, 공격 적중 시 [Burst] 3 부여 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1061001].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Burst]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: If the target is a <Bloodfiend> or a <Bloodbag>, deal +10% damage\nOn Skill Use, if this unit has [Laceration], inflict 3 [Burst] On Hit (once per turn)
   PL: Jeżeli cel jest <Krwiożercą> albo <Workiem Krwi>, zadaje +10% obrażeń\nPrzy użyciu Umiejętności, jeżeli ma [Laceration], przy trafieniu nakłada 3 [Burst] (1 raz na turę)
285. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — nazwa] 유쾌한 사냥법
   źródło: Passives.json :: dataList[id=1061011].name
   (powtórzenie elementu 283 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Glut.) — opis] 대상이 <혈귀>, <피주머니>거나, 대상의 [Burst]이 10 이상이면 피해량 +10%\n스킬 사용시 자신에게 [Laceration]이 있으면, 공격 적중 시 [Burst] 3 부여 (턴 당 2회)
   źródło: Passives.json :: dataList[id=1061011].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Laceration]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Laceration] = 출혈 / Bleed
   EN: If the target is a <Bloodfiend>, <Bloodbag>, or if the target has 10+ [Burst], deal +10% damage\nOn Skill Use, if this unit has [Laceration], inflict 3 [Burst] On Hit (2 times per turn)
   PL: Jeżeli cel jest <Krwiożercą> albo <Workiem Krwi> albo ma 10+ [Burst], zadaje +10% obrażeń\nPrzy użyciu Umiejętności, jeżeli ma [Laceration], przy trafieniu nakłada 3 [Burst] (2 razy na turę)
287. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — nazwa] 혈귀 공략 교본 - 지혈
   źródło: Passives.json :: dataList[id=1061021].name
   limit: do 50 znaków
   EN: Bloodfiend Hunting Manual - Styptics
   PL: Podręcznik Polowania na Krwiożerców - Zatrzask
288. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — opis] 전투 시작 시, [Laceration]과 [Laceration] 횟수의 합이 가장 높은 아군 1명의 [Laceration] 횟수 2 감소\n속도가 가장 빠른 아군 1명이 [Burst]이 있는 적에게 공격 적중시, [DefenseDown] 1 부여 (턴 당 최대 2회)
   źródło: Passives.json :: dataList[id=1061021].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Burst], [DefenseDown]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Combat Start: 1 ally that has the highest sum of [Laceration] Potency and Count loses 2 [Laceration] Count\nWhen 1 ally with the fastest Speed hits an enemy that has [Burst], inflict 1 [DefenseDown] (2 times per turn)
   PL: Na początku walki 1 Sojusznik z najwyższą sumą Mocy [Laceration] i Licznika [Laceration] traci 2 Licznika [Laceration]\nGdy 1 Sojusznik z najwyższą Szybkością trafia wroga z [Burst], nakłada 1 [DefenseDown] (maks. 2 razy na turę)

## [000] Full-Stop Office Rep — Hong Lu — 마침표 사무소 대표
- ID Tożsamości: `10611` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9105 · HP bazowe: 70 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Poise

289. [Karta Tożsamości — tytuł] 마침표 사무소\n대표
   źródło: Personalities.json :: dataList[id=10611].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Full-Stop Office\nRep
   PL: Biuro Kropka\nRep
290. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10611].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10611].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Karta Tożsamości — opis] 홍루의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10611].desc
   limit: do 120 znaków
   EN: Hong Lu’s 11th Identity
   PL: Jedenasta Tożsamość Hong Lu
293. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 발사
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].name ; dataList[id=1061101].levelList[level=2].name ; dataList[id=1061101].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 3 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Take the Shot
   PL: Oddaj Strzał
294. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2
295. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend 1 [Bullet]
   PL: Zużywa 1 [Bullet]
296. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL: [OnSucceedAttack] Zyskuje 1 [Breath]
298. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count<style="highlight"></style>
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2<style="highlight"></style>
301. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1061101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend 1 [Bullet]<style="highlight"></style>
   PL: Zużywa 1 [Bullet]<style="highlight"></style>
302. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] <style="highlight">2</style> 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain <style="highlight">2</style> [Breath]
   PL: [OnSucceedAttack] Zyskuje <style="highlight">2</style> [Breath]
304. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1061101].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Breath] <style="highlight">2</style> 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=2].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +<style="highlight">3</style> [Breath] Count
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o <style="highlight">3</style>
307. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 2 [Breath]<style="highlight"></style>
308. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061101].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 타겟 지정
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=1].name ; dataList[id=1061102].levelList[level=2].name ; dataList[id=1061102].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Target Marked
   PL: Cel Oznaczony
310. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 마침표 사무소 해결사 히스클리프 인격이 전투에 등장해 있으면, 가장 높은 공명 당 20% 확률로 [CoveringFire] 발동\n[WhenUse] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [WhenUse], [CoveringFire], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [CoveringFire] = 타겟 포착 / Target Spotted; [Breath] = 호흡 / Poise
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] If Full-Stop Office Fixer Heathcliff is on the field, every Reson. of the highest Reson. adds 20% chance that this unit activates [CoveringFire]\n[WhenUse] Gain +1 [Breath] Count
   PL: Moc Bazowa +1 za każdy [Bullet], który ta Umiejętność zużyje\n[WhenUse] Jeżeli Fikser Biura Kropka Heathcliff jest na polu, każdy Rezonans najwyższego Rezonansu daje 20% szans na uruchomienie [CoveringFire]\n[WhenUse] Zwiększa własny Licznik [Breath] o 1
311. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL: [OnSucceedAttack] Zyskuje 2 [Breath]
312. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [Bullet] 최대 3 소모
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend up to 3 [Bullet]
   PL: Zużywa do 3 [Bullet]
313. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] 피해량 +(소모한 탄환 x 10)%
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Deal +([Bullet] spent x 10)% damage
   PL: Zadaje +(zużyta amunicja x 10)% obrażeń
314. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [Reduction]
315. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 마침표 사무소 해결사 히스클리프 인격이 전투에 등장해 있으면, 가장 높은 공명 당 20% 확률로 [CoveringFire] 발동\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=2].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet], [WhenUse], [CoveringFire], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [CoveringFire] = 타겟 포착 / Target Spotted; [Breath] = 호흡 / Poise
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] If Full-Stop Office Fixer Heathcliff is on the field, every Reson. of the highest Reson. adds 20% chance that this unit activates [CoveringFire]\n[WhenUse] Gain +<style="highlight">2</style> [Breath] Count
   PL: Moc Bazowa +1 za każdy [Bullet], który ta Umiejętność zużyje\n[WhenUse] Jeżeli Fikser Biura Kropka Heathcliff jest na polu, każdy Rezonans najwyższego Rezonansu daje 20% szans na uruchomienie [CoveringFire]\n[WhenUse] Zwiększa własny Licznik [Breath] o <style="highlight">2</style>
316. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1061102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [Bullet] 최대 3 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend up to 3 [Bullet]<style="highlight"></style>
   PL: Zużywa do 3 [Bullet]<style="highlight"></style>
318. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] 피해량 +(소모한 탄환 x 10)%<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1061102].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Deal +([Bullet] spent x 10)% damage<style="highlight"></style>
   PL: Zadaje +(zużyta amunicja x 10)% obrażeń<style="highlight"></style>
319. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [Binding] 1 부여</style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Binding] next turn</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada w następnej turze 1 [Binding]</style>
320. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 1 [Reduction] next turn<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [Reduction]<style="highlight"></style>
321. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 마침표 사무소 해결사 히스클리프 인격이 전투에 등장해 있으면, 가장 높은 공명 당 25% 확률로 [CoveringFire] 발동\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=4].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet], [WhenUse], [CoveringFire], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [CoveringFire] = 타겟 포착 / Target Spotted; [Breath] = 호흡 / Poise
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] If Full-Stop Office Fixer Heathcliff is on the field, every Reson. of the highest Reson. adds 25% chance that this unit activates [CoveringFire]\n[WhenUse] Gain +<style="highlight">3</style> [Breath] Count
   PL: Moc Bazowa +1 za każdy [Bullet], który ta Umiejętność zużyje\n[WhenUse] Jeżeli Fikser Biura Kropka Heathcliff jest na polu, każdy Rezonans najwyższego Rezonansu daje 25% szans na uruchomienie [CoveringFire]\n[WhenUse] Zwiększa własny Licznik [Breath] o <style="highlight">3</style>
322. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 3 — opis] <style="highlight">크리티컬 피해량 +(소모한 탄환 x 10)%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: <style="highlight">+([Bullet] spent x 10)% Damage on Critical Hit</style>
   PL: <style="highlight">Zadaje +(zużyta amunicja x 10)% obrażeń przy trafieniu krytycznym</style>
323. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">크리티컬 피해량 +20%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+20% Damage on Critical Hit</style>
   PL: <style="highlight">Zadaje +20% obrażeń przy trafieniu krytycznym</style>
324. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [Binding]<style="highlight"></style>
325. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061102].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 삶의 마침표
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].name ; dataList[id=1061103].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 7 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Full-Stop to Life
   PL: Kropka Nad iem Życia
327. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 마침표 사무소 해결사 히스클리프 인격이 전투에 등장해 있으면, [CoveringFire] 발동\n[WhenUse] [Breath] 5 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [WhenUse], [CoveringFire], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [CoveringFire] = 타겟 포착 / Target Spotted; [Breath] = 호흡 / Poise
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] If Full-Stop Office Fixer Heathcliff is on the field, activate [CoveringFire]\n[WhenUse] Gain 5 [Breath]
   PL: Moc Bazowa +1 za każdy [Bullet], który ta Umiejętność zużyje\n[WhenUse] Jeżeli Fikser Biura Kropka Heathcliff jest na polu, uruchamia [CoveringFire]\n[WhenUse] Zyskuje 5 [Breath]
328. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] 피해량 + (소모한 탄환 x 10)%
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Deal +([Bullet] spent x 10)% damage
   PL: Zadaje +(zużyta amunicja x 10)% obrażeń
330. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise the target's Stagger Threshold by 10% of damage dealt
   PL: [OnSucceedAttack] Podnosi Próg Oszołomienia celu o 10% zadanych obrażeń
331. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [Bullet] 최대 2 소모
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend up to 2 [Bullet]
   PL: Zużywa do 2 [Bullet]
332. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] 피해량 + (소모한 탄환 x 10)%
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 329 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 330 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 대상이 흐트러짐 상태면 크리티컬 피해량 +30%
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: If target is Staggered, +30% Damage on Critical Hit
   PL: Jeżeli cel jest Ogłuszony, zadaje +30% obrażeń przy trafieniu krytycznym
335. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [Binding]
336. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [PenetrateTakeDamageUp] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [OnSucceedAttack] Inflict 1 [PenetrateTakeDamageUp]
   PL: [OnSucceedAttack] Nakłada 1 [PenetrateTakeDamageUp]
337. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 마침표 사무소 해결사 히스클리프 인격이 전투에 등장해 있으면, [CoveringFire] 발동\n[WhenUse] [Breath] 5 얻음\n<style="highlight">[WinDuel] 자신의 [Breath] 횟수 2 증가</style>
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet], [WhenUse], [CoveringFire], [Breath], [WinDuel]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [CoveringFire] = 타겟 포착 / Target Spotted; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] If Full-Stop Office Fixer Heathcliff is on the field, activate [CoveringFire]\n[WhenUse] Gain 5 [Breath]\n<style="highlight">[WinDuel] Gain +2 [Breath] Count</style>
   PL: Moc Bazowa +1 za każdy [Bullet], który ta Umiejętność zużyje\n[WhenUse] Jeżeli Fikser Biura Kropka Heathcliff jest na polu, uruchamia [CoveringFire]\n[WhenUse] Zyskuje 5 [Breath]\n<style="highlight">[WinDuel] Zwiększa własny Licznik [Breath] o 2</style>
338. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] 피해량 + (소모한 탄환 x <style="highlight">15</style>)%
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Deal +([Bullet] spent x <style="highlight">15</style>)% damage
   PL: Zadaje +(zużyta amunicja x <style="highlight">15</style>)% obrażeń
340. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 <style="highlight">15</style>%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise the target's Stagger Threshold by <style="highlight">15</style>% of damage dealt
   PL: [OnSucceedAttack] Podnosi Próg Oszołomienia celu o <style="highlight">15</style>% zadanych obrażeń
341. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [Bullet] 최대 2 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Spend up to 2 [Bullet]<style="highlight"></style>
   PL: Zużywa do 2 [Bullet]<style="highlight"></style>
342. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] 피해량 + (소모한 탄환 x <style="highlight">15</style>)%
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 피해량의 <style="highlight">15</style>%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 대상이 흐트러짐 상태면 크리티컬 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: If target is Staggered, +30% Damage on Critical Hit<style="highlight"></style>
   PL: Jeżeli cel jest Ogłuszony, zadaje +30% obrażeń przy trafieniu krytycznym<style="highlight"></style>
345. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] <style="highlight">2</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Binding] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze <style="highlight">2</style> [Binding]
346. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [PenetrateTakeDamageUp] <style="highlight">2</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061103].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenetrateTakeDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenetrateTakeDamageUp] = 관통 취약 / Pierce Fragility
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [PenetrateTakeDamageUp]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [PenetrateTakeDamageUp]
347. [Umiejętność 4 (×0) (ulepszenia 2,4) — nazwa] 연계: 타겟 지정
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].name ; dataList[id=1061105].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 4 · monety: 4 (+4)
   limit: do 40 znaków
   EN: Combo: Target Marked
   PL: Kombinacja: Cel Oznaczony
348. [Umiejętność 4 (×0) (ulepszenie 2) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[DefeatDuel] 최종 위력 +5
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [WhenUse], [Breath], [DefeatDuel]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] Gain +2 [Breath] Count\n[DefeatDuel] Final Power +5
   PL: Moc Bazowa +1 za każdy [Bullet], który ta Umiejętność zużyje\n[WhenUse] Zwiększa własny Licznik [Breath] o 2\n[DefeatDuel] Moc Końcowa +5
349. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 2, efekt 1 — opis] [Bullet] 최대 3 소모
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 2, efekt 2 — opis] 피해량 +(소모한 탄환 x 10)%
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
355. [Umiejętność 4 (×0) (ulepszenie 2) — moneta 4, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=2].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   EN: +30% Damage on Critical Hit
   PL: Zadaje +30% obrażeń przy trafieniu krytycznym
356. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 <style="highlight">3</style> 증가\n[DefeatDuel] 최종 위력 +5
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet], [WhenUse], [Breath], [DefeatDuel]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] Gain +<style="highlight">3</style> [Breath] Count\n[DefeatDuel] Final Power +5
   PL: Moc Bazowa +1 za każdy [Bullet], który ta Umiejętność zużyje\n[WhenUse] Zwiększa własny Licznik [Breath] o <style="highlight">3</style>\n[DefeatDuel] Moc Końcowa +5
357. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [Bullet] 최대 3 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 317 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] 피해량 +(소모한 탄환 x 10)%<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 318 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 3 — opis] <style="highlight">크리티컬 피해량 +(소모한 탄환 x 10)%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 322 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">크리티컬 피해량 +20%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 323 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL: [SuperCoin]<style="highlight"></style>
365. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 2 — opis] 크리티컬 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061105].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: +30% Damage on Critical Hit<style="highlight"></style>
   PL: Zadaje +30% obrażeń przy trafieniu krytycznym<style="highlight"></style>
366. [Umiejętność 5 (×0) (ulepszenia 3–4) — nazwa] 연계: 삶의 마침표
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].name ; dataList[id=1061106].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 7 · monety: 4 (+4)
   limit: do 40 znaków
   EN: Combo: Full-Stop to Life
   PL: Kombinacja: Kropka Nad iem Życia
367. [Umiejętność 5 (×0) (ulepszenie 3) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] [Breath] 5 얻음\n[DefeatDuel] 최종 위력 +5
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [WhenUse], [Breath], [DefeatDuel]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] Gain 5 [Breath]\n[DefeatDuel] Final Power +5
   PL: Moc Bazowa +1 za każdy [Bullet], który ta Umiejętność zużyje\n[WhenUse] Zyskuje 5 [Breath]\n[DefeatDuel] Moc Końcowa +5
368. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [Bullet] 1 소모
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] 피해량 + (소모한 탄환 x 10)%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 329 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 330 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [Bullet] 최대 2 소모
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 331 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 2 — opis] 피해량 + (소모한 탄환 x 10)%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 329 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 330 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] 대상이 흐트러짐 상태면 크리티컬 피해량 +30%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 334 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [PenetrateTakeDamageUp] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 4, efekt 2 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 4, efekt 3 — opis] 피해량 + (대상의 관통 내성 x 50)%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=3].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   EN: Deal +(target's Pierce Res. x 50)% damage
   PL: Zadaje +(przebiciowa odporność celu x 50)% obrażeń
380. [Umiejętność 5 (×0) (ulepszenie 4) — opis] 이 스킬에서 소모할 [Bullet] 1 당 기본 위력 +1\n[WhenUse] [Breath] 5 얻음\n<style="highlight">[WinDuel] 자신의 [Breath] 횟수 2 증가</style>\n[DefeatDuel] 최종 위력 +5
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet], [WhenUse], [Breath], [WinDuel], [DefeatDuel]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Base Power +1 for every [Bullet] about to be spent by this Skill\n[WhenUse] Gain 5 [Breath]\n<style="highlight">[WinDuel] Gain +2 [Breath] Count</style>\n[DefeatDuel] Final Power +5
   PL: Moc Bazowa +1 za każdy [Bullet], który ta Umiejętność zużyje\n[WhenUse] Zyskuje 5 [Breath]\n<style="highlight">[WinDuel] Zwiększa własny Licznik [Breath] o 2</style>\n[DefeatDuel] Moc Końcowa +5
381. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [Bullet] 1 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] 피해량 + (소모한 탄환 x <style="highlight">15</style>)%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 <style="highlight">15</style>%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [Bullet] 최대 2 소모<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] 피해량 + (소모한 탄환 x <style="highlight">15</style>)%
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 피해량의 <style="highlight">15</style>%만큼 흐트러짐 손상
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] 대상이 흐트러짐 상태면 크리티컬 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] <style="highlight">2</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 345 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [PenetrateTakeDamageUp] <style="highlight">2</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 4, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 4, efekt 2 — opis] <style="highlight">크리티컬 피해량 +50%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+50% Damage on Critical Hit</style>
   PL: <style="highlight">Zadaje +50% obrażeń przy trafieniu krytycznym</style>
392. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 4, efekt 3 — opis] 피해량 + (대상의 관통 내성 x 50)%<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061106].levelList[level=4].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal +(target's Pierce Res. x 50)% damage<style="highlight"></style>
   PL: Zadaje +(przebiciowa odporność celu x 50)% obrażeń<style="highlight"></style>
393. [Umiejętność 6 (×0) (ulepszenia 1,4) — nazwa] 근접 지원
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=1].name ; dataList[id=1061108].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Melee Support
   PL: Wsparcie z Bliska
394. [Umiejętność 6 (×0) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=1].desc
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Umiejętność 6 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność 6 (×0) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Umiejętność 6 (×0) (ulepszenie 4) — opis] <style="highlight">크리티컬 피해량 +20%</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: <style="highlight">+20% Damage on Critical Hit</style>\n[WhenUse] Gain +2 [Breath] Count
   PL: <style="highlight">Zadaje +20% obrażeń przy trafieniu krytycznym</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
398. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 1 [Breath]<style="highlight"></style>
399. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061108].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Obrona (ulepszenia 1,4) — nazwa] 전투 호흡
   źródło: Skills_personality-06.json :: dataList[id=1061104].levelList[level=1].name ; dataList[id=1061104].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Combat Poise
   PL: Bojowa Flegma
401. [Obrona (ulepszenie 1) — opis] 턴 시작 시 [Bullet]이 0이면, '그림자의 건너편'으로 변경됨\n[OnSucceedEvade] [Breath] 1 얻음 (턴 당 3회)
   źródło: Skills_personality-06.json :: dataList[id=1061104].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet], [OnSucceedEvade], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: Turn Start: at 0 [Bullet], activate 'Beyond the Shadow' instead\n[OnSucceedEvade] Gain 1 [Breath] (3 times per turn)
   PL: Na początku tury przy 0 [Bullet] stosuje się jako „Po Drugiej Stronie Cienia”\n[OnSucceedEvade] Zyskuje 1 [Breath] (3 razy na turę)
402. [Obrona (ulepszenie 4) — opis] 턴 시작 시 [Bullet]이 0이면, '그림자의 건너편'으로 변경됨\n[OnSucceedEvade] [Breath] 1 얻음 (턴 당 <style="highlight">5</style>회)
   źródło: Skills_personality-06.json :: dataList[id=1061104].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet], [OnSucceedEvade], [Breath]
   znaczenie tagów: [Bullet] = 탄환 / Ammo; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: Turn Start: at 0 [Bullet], activate 'Beyond the Shadow' instead\n[OnSucceedEvade] Gain 1 [Breath] (<style="highlight">5</style> times per turn)
   PL: Na początku tury przy 0 [Bullet] stosuje się jako „Po Drugiej Stronie Cienia”\n[OnSucceedEvade] Zyskuje 1 [Breath] (maks. <style="highlight">5</style> razy na turę)
403. [Obrona (ulepszenia 1,4) — nazwa] 그림자의 건너편
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=1].name ; dataList[id=1061107].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Beyond the Shadow
   PL: Po Drugiej Stronie Cienia
404. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[EndBattle] [FullReload] (전투 당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Breath], [EndBattle], [FullReload]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndBattle] = [턴 종료 시] / [Turn End]; [FullReload] = 재장전 / Reload
   EN: [DuelCounter]\n[WhenUse] Gain +2 [Breath] Count\n[EndBattle] [FullReload] (once per Encounter)
   PL: [DuelCounter]\n[WhenUse] Zwiększa własny Licznik [Breath] o 2\n[EndBattle] [FullReload] (1 raz na spotkanie)
405. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n<style="highlight">크리티컬 피해량 +20%</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가\n[EndBattle] [FullReload] (전투 당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [WhenUse], [Breath], [EndBattle], [FullReload]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndBattle] = [턴 종료 시] / [Turn End]; [FullReload] = 재장전 / Reload
   EN: [DuelCounter]\n<style="highlight">+20% Damage on Critical Hit</style>\n[WhenUse] Gain +2 [Breath] Count\n[EndBattle] [FullReload] (once per Encounter)
   PL: [DuelCounter]\n<style="highlight">Zadaje +20% obrażeń przy trafieniu krytycznym</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2\n[EndBattle] [FullReload] (1 raz na spotkanie)
408. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061107].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Pasywka bojowa (od ulepszenia 1) — nazwa] 집중
   źródło: Passives.json :: dataList[id=1061101].name
   limit: do 40 znaków
   EN: Concentration
   PL: Koncentracja
411. [Pasywka bojowa (od ulepszenia 1) — opis] [Bullet]을 소모하는 코인을 굴릴 때, [Bullet]이 없는 경우에도 해당 코인의 적중시 효과를 부여하지 않는 대신 공격이 취소되지 않음
   źródło: Passives.json :: dataList[id=1061101].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: When flipping a Coin that consumes [Bullet]: even when this unit is out of [Bullet], the attack does not get canceled. However, the affected Coins' On Hit effects do not activate in such cases.
   PL: Podczas rzutu monetą zużywającą [Bullet]: nawet w braku [Bullet] atak nie zostaje anulowany. W takich przypadkach jednak efekty przy trafieniu dotkniętych monet nie uruchamiają się.
412. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — nazwa] 전술적 사격 지원
   źródło: Passives.json :: dataList[id=1061102].name
   limit: do 40 znaków
   EN: Tactical Fire Support
   PL: Taktyczne Wsparcie Ogniowe
413. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — opis] 마침표 사무소 해결사 히스클리프가 [Retreat_FullStop] 상태거나, 대기 인원으로 편성되어 있다면 마침표 사무소 대표 홍루 인격의 스킬2, 스킬3이 강화됨
   źródło: Passives.json :: dataList[id=1061102].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [Retreat_FullStop]
   znaczenie tagów: [Retreat_FullStop] = 후방 지원 배치 / Overwatch Assignment
   EN: If the Full-Stop Office Fixer Heathcliff is in [Retreat_FullStop] state, or has been Deployed as a Backup unit, empower Full-Stop Office Rep. Hong Lu's Skill 2 and Skill 3
   PL: Jeżeli Fikser Biura Kropka Heathcliff jest w stanie [Retreat_FullStop] albo przydzielony jako rezerwa, Umiejętności 2 i 3 Tożsamości Rep Biura Kropka Hong Lu zostają wzmocnione
414. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Pride) — nazwa] 전술적 사격 지원
   źródło: Passives.json :: dataList[id=1061111].name
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Pasywka bojowa (od ulepszenia 4, posiadane 5× Pride) — opis] 마침표 사무소 해결사 히스클리프가 [Retreat_FullStop] 상태거나, 대기 인원으로 편성되어 있다면 마침표 사무소 대표 홍루 인격의 스킬2, 스킬3이 강화됨\n\n전투 시작시 자신의 [Breath] 위력이 20 이상이면, [Breath] 횟수 1 얻음
   źródło: Passives.json :: dataList[id=1061111].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Retreat_FullStop], [Breath]
   znaczenie tagów: [Retreat_FullStop] = 후방 지원 배치 / Overwatch Assignment; [Breath] = 호흡 / Poise
   EN: If the Full-Stop Office Fixer Heathcliff is in [Retreat_FullStop] state, or has been Deployed as a Backup unit, empower Full-Stop Office Rep. Hong Lu's Skill 2 and Skill 3\n\nCombat Start: at 20+ [Breath] Potency, gain +1 [Breath] Count
   PL: Jeżeli Fikser Biura Kropka Heathcliff jest w stanie [Retreat_FullStop] albo przydzielony jako rezerwa, Umiejętności 2 i 3 Tożsamości Rep Biura Kropka Hong Lu zostają wzmocnione\n\nNa początku walki przy 20+ Mocy [Breath] zyskuje +1 Licznika [Breath]
416. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — nazwa] 제압 사격
   źródło: Passives.json :: dataList[id=1061121].name
   limit: do 40 znaków
   EN: Suppressing Fire
   PL: Ostrzał Powstrzymujący
417. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — opis] [Bullet]을 가장 많이 보유한 아군 인격이 [Bullet]을 소모하는 스킬로 가하는 피해량 +10%\n([Bullet]이 없으면 적용되지 않음)
   źródło: Passives.json :: dataList[id=1061121].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Ally Identity that has the most [Bullet] deals +10% damage using Skills that spend [Bullet]\n(Does not activate when out of [Bullet])
   PL: Tożsamość sojusznika z największą liczbą [Bullet] zadaje +10% obrażeń Umiejętnościami zużywającymi [Bullet]\n(Nie uruchamia się w braku [Bullet])

## [000] R Corp. 4th Pack Reindeer — Hong Lu — R사 제 4무리 순록팀
- ID Tożsamości: `10612` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 65 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Charge, Sinking

418. [Karta Tożsamości — tytuł] R사 제 4무리\n순록팀
   źródło: Personalities.json :: dataList[id=10612].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: R Corp. 4th Pack\nReindeer
   PL: R Corp. 4 Pack\nZespół Reniferów
419. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10612].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10612].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Karta Tożsamości — opis] 홍루의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10612].desc
   limit: do 120 znaków
   EN: Hong Lu’s 12th Identity
   PL: Dwunasta Tożsamość Hong Lu
422. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 에너지 강타
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=1].name ; dataList[id=1061201].levelList[level=2].name ; dataList[id=1061201].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Energy Strike
   PL: Energetyczne Uderzenie
423. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [Charge]이 2 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [WhenUse]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: At 2+ [Charge], Coin Power +1\n[WhenUse] Gain +2 [Charge] Count
   PL: Przy 2+ [Charge] Moc Monet +1\n[WhenUse] Zwiększa własny Licznik [Charge] o 2
424. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] Nakłada 1 [Sinking]
425. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[Charge]당 피해량 +2% (최대 10%)</style>\n[Charge]이 2 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [WhenUse]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">Deal +2% damage for every [Charge] (max 10%)</style>\nAt 2+ [Charge], Coin Power +1\n[WhenUse] Gain +2 [Charge] Count
   PL: <style="highlight">Zadaje +2% obrażeń za każde 1 [Charge] (maks. 10%)</style>\nPrzy 2+ [Charge] Moc Monet +1\n[WhenUse] Zwiększa własny Licznik [Charge] o 2
426. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] <style="highlight">[OnSucceedAttack] ([Charge] + 1)만큼 자신의 [Charge] 횟수 증가 (최대 3)</style>
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: <style="highlight">[OnSucceedAttack] Gain +([Charge] + 1) [Charge] Count (max 3)</style>
   PL: <style="highlight">[OnSucceedAttack] Zwiększa własny Licznik [Charge] o wartość ([Charge] + 1) (maks. 3)</style>
427. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Sinking]<style="highlight"></style>
428. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [Charge]당 피해량 <style="highlight">+3%</style> (최대 <style="highlight">15%</style>)\n[Charge]이 2 이상이면, 코인 위력 +1\n<style="highlight">[Charge] 횟수가 5 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [WhenUse]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: Deal <style="highlight">+3%</style> damage for every [Charge] (max <style="highlight">15%</style>)\nAt 2+ [Charge], Coin Power +1\n<style="highlight">At 5+ [Charge] Count, Coin Power +1</style>\n[WhenUse] Gain +2 [Charge] Count
   PL: Zadaje <style="highlight">+3%</style> obrażeń za każde 1 [Charge] (maks. <style="highlight">15%</style>)\nPrzy 2+ [Charge] Moc Monet +1\n<style="highlight">Przy 5+ Liczniku [Charge] Moc Monet +1</style>\n[WhenUse] Zwiększa własny Licznik [Charge] o 2
429. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] ([Charge] + 1)만큼 자신의 [Charge] 횟수 증가 (최대 <style="highlight">4</style>)
   źródło: Skills_personality-06.json :: dataList[id=1061201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] + 1) [Charge] Count (max <style="highlight">4</style>)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o wartość ([Charge] + 1) (maks. <style="highlight">4</style>)
430. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 정신 채찍
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=1].name ; dataList[id=1061202].levelList[level=2].name ; dataList[id=1061202].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 2 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Mind Whip
   PL: Bicz na Umysł
431. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [Charge] 횟수가 5 이상 10 미만이면,\n- [Sinking] 15 얻음, [Charge] 횟수 10으로 증가\n- 이 스킬이 [CantIdentify], [WideAreaRampage] 상태가 되고 공격 가중치 +1\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [Sinking], [CantIdentify], [WideAreaRampage]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [Sinking] = 침잠 / Sinking; [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WideAreaRampage] = 광역 난사 / Unfocused Volley
   EN: [WhenUse] At 5~9 [Charge] Count:\n- Gain 15 [Sinking] and raise this unit's [Charge] Count to 10\n- This Skill gains the following attributes: [CantIdentify], [WideAreaRampage], and Atk Weight +1\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power +1
   PL: [WhenUse] Przy 5-9 Licznika [Charge]:\n- Zyskuje 15 [Sinking] i podnosi własny Licznik [Charge] do 10\n- Ta Umiejętność zyskuje następujące atrybuty: [CantIdentify], [WideAreaRampage] i Waga ataku +1\n[WhenUse] Zużywa 10 Licznika [Charge], aby zyskać Moc Monet +1
432. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Sinking]
436. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[Charge]당 피해량 +2% (최대 10%)</style>\n[WhenUse] [Charge] 횟수가 5 이상 10 미만이면,\n- [Sinking] 15 얻음, [Charge] 횟수 10으로 증가\n- 이 스킬이 [CantIdentify], [WideAreaRampage] 상태가 되고 공격 가중치 +1\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [WhenUse], [Sinking], [CantIdentify], [WideAreaRampage]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WideAreaRampage] = 광역 난사 / Unfocused Volley
   EN: <style="highlight">Deal +2% damage for every [Charge] (max 10%)</style>\n[WhenUse] At 5~9 [Charge] Count:\n- Gain 15 [Sinking] and raise this unit's [Charge] Count to 10\n- This Skill gains the following attributes: [CantIdentify], [WideAreaRampage], and Atk Weight +1\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power +1
   PL: <style="highlight">Zadaje +2% obrażeń za każde 1 [Charge] (maks. 10%)</style>\n[WhenUse] Przy 5-9 Licznika [Charge]:\n- Zyskuje 15 [Sinking] i podnosi własny Licznik [Charge] do 10\n- Ta Umiejętność zyskuje następujące atrybuty: [CantIdentify], [WideAreaRampage] i Waga ataku +1\n[WhenUse] Zużywa 10 Licznika [Charge], aby zyskać Moc Monet +1
437. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1061202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 427 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 피해량의 5%만큼 흐트러짐 손상을 입힘</style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] Raise Stagger Threshold by 5% of damage dealt</style>
   PL: <style="highlight">[OnSucceedAttack] Podnosi Próg Oszołomienia o 5% zadanych obrażeń</style>
439. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 427 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 피해량의 5%만큼 흐트러짐 손상을 입힘</style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1061202].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 427 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 피해량의 5%만큼 흐트러짐 손상을 입힘</style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#3].coindescs[#0].desc ; dataList[id=1061202].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] celu o 2<style="highlight"></style>
444. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 4, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상을 입힘</style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=2].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] Raise Stagger Threshold by 10% of damage dealt</style>
   PL: <style="highlight">[OnSucceedAttack] Podnosi Próg Oszołomienia o 10% zadanych obrażeń</style>
445. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [Charge]당 피해량 <style="highlight">+4%</style> (최대 <style="highlight">20%</style>)\n[WhenUse] [Charge] 횟수가 5 이상 10 미만이면,\n- [Sinking] <style="highlight">10</style> 얻음, [Charge] 횟수 10으로 증가\n- 이 스킬이 [CantIdentify], [WideAreaRampage] 상태가 되고 공격 가중치 +1\n<style="highlight">- [BeforeUse] [Charge]이 5 이상이면, [CantIdentify] 효과가 적용되지 않음</style>\n[WhenUse] [Charge] 횟수를 10 소모하여 코인 위력 <style="highlight">+2</style>\n<style="highlight">[BeforeAttack] 남은 [Charge] 횟수가 8 이상이면, [Charge] 횟수를 8 소모하여 피해량 +40%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=4].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [WhenUse], [Sinking], [CantIdentify], [WideAreaRampage], [BeforeUse], [BeforeAttack]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]; [Sinking] = 침잠 / Sinking; [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WideAreaRampage] = 광역 난사 / Unfocused Volley; [BeforeUse] = [사용전] / [Before Use]; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: Deal <style="highlight">+4%</style> damage for every [Charge] (max <style="highlight">20%</style>)\n[WhenUse] At 5~9 [Charge] Count:\n- Gain <style="highlight">10</style> [Sinking] and raise this unit's [Charge] Count to 10\n- This Skill gains the following attributes: [CantIdentify], [WideAreaRampage], and Atk Weight +1\n<style="highlight">- [BeforeUse] At 5+ [Charge], this Skill does not gain the [CantIdentify] effect</style>\n[WhenUse] Consume 10 [Charge] Count to gain Coin Power <style="highlight">+2</style>\n<style="highlight">[BeforeAttack] At 8+ remaining [Charge] Count, consume 8 [Charge] Count to deal +40% damage</style>
   PL: Zadaje <style="highlight">+4%</style> obrażeń za każde 1 [Charge] (maks. <style="highlight">20%</style>)\n[WhenUse] Przy 5-9 Licznika [Charge]:\n- Zyskuje <style="highlight">10</style> [Sinking] i podnosi własny Licznik [Charge] do 10\n- Ta Umiejętność zyskuje następujące atrybuty: [CantIdentify], [WideAreaRampage] i Waga ataku +1\n<style="highlight">- [BeforeUse] Przy 5+ [Charge] ta Umiejętność nie zyskuje efektu [CantIdentify]</style>\n[WhenUse] Zużywa 10 Licznika [Charge], aby zyskać Moc Monet <style="highlight">+2</style>\n<style="highlight">[BeforeAttack] Przy 8+ pozostałego Licznika [Charge] zużywa 8 Licznika [Charge], aby zadać +40% obrażeń</style>
446. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 피해량의 5%만큼 흐트러짐 손상을 입힘<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 5% of damage dealt<style="highlight"></style>
   PL: [OnSucceedAttack] Podnosi Próg Oszołomienia o 5% zadanych obrażeń<style="highlight"></style>
447. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 피해량의 5%만큼 흐트러짐 손상을 입힘<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 피해량의 5%만큼 흐트러짐 손상을 입힘<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 피해량의 10%만큼 흐트러짐 손상을 입힘<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061202].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 10% of damage dealt<style="highlight"></style>
   PL: [OnSucceedAttack] Podnosi Próg Oszołomienia o 10% zadanych obrażeń<style="highlight"></style>
450. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 집중
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=3].name ; dataList[id=1061203].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Hit · moc bazowa: 8 · monety: 1 (+10)
   (powtórzenie elementu 410 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [Charge]당 코인 위력 +1 (최대 5)\n[Charge] 횟수가 10 이상이면, 최종 위력 +2\n[WhenUse] 자신의 [Charge] 횟수 5 증가
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=3].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [WhenUse]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: Coin Power +1 for every [Charge] (max 5)\nAt 10+ [Charge] Count, Final Power +2\n[WhenUse] Gain +5 [Charge] Count
   PL: Moc Monet +1 za każde 1 [Charge] (maks. 5)\nPrzy 10+ Liczniku [Charge] Moc Końcowa +2\n[WhenUse] Zwiększa własny Licznik [Charge] o 5
452. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] 피해량 +(이 스킬의 위력 x 5)% (최대 100%)
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +(this Skill's Power x 5)% damage (max 100%)
   PL: Zadaje +(Moc tej Umiejętności x 5)% obrażeń (maks. 100%)
453. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] ([Charge] + 1)만큼 자신의 [Charge] 횟수 증가 (최대 6)
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] + 1) [Charge] Count (max 6)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o wartość ([Charge] + 1) (maks. 6)
454. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Sinking] 4 부여, [Sinking] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking] and +2 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada 4 [Sinking] i zwiększa Licznik [Sinking] o 2
455. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [Charge]당 <style="highlight">기본 위력 +1</style>, 코인 위력 +1 <style="highlight">(각각 최대 5)</style>\n[Charge] 횟수가 10 이상이면, 최종 위력 <style="highlight">+4</style>\n[WhenUse] 자신의 [Charge] 횟수 <style="highlight">7</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [WhenUse]
   znaczenie tagów: [Charge] = 충전 / Charge; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">Base Power +1</style> and Coin Power +1 for every [Charge] <style="highlight">(max 5 each)</style>\nAt 10+ [Charge] Count, Final Power <style="highlight">+4</style>\n[WhenUse] Gain <style="highlight">+7</style> [Charge] Count
   PL: <style="highlight">Moc Bazowa +1</style> i Moc Monet +1 za każde 1 [Charge] <style="highlight">(każdy maks. 5)</style>\nPrzy 10+ Liczniku [Charge] Moc Końcowa <style="highlight">+4</style>\n[WhenUse] Zwiększa własny Licznik [Charge] o <style="highlight">7</style>
456. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] 피해량 +(이 스킬의 위력 x 5)% (최대 <style="highlight">150%</style>)
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal +(this Skill's Power x 5)% damage (max <style="highlight">150%</style>)
   PL: Zadaje +(Moc tej Umiejętności x 5)% obrażeń (maks. <style="highlight">150%</style>)
457. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] <style="highlight">[Charge]이 3 이상이면, [Charge]당 피해량 +20% (최대 100%)</style>
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: <style="highlight">At 3+ [Charge], deal +20% damage for every [Charge] (max 100%)</style>
   PL: <style="highlight">Przy 3+ [Charge] zadaje +20% obrażeń za każde 1 [Charge] (maks. 100%)</style>
458. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] ([Charge] + <style="highlight">3</style>)만큼 자신의 [Charge] 횟수 증가 (최대 <style="highlight">8</style>)
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +([Charge] + <style="highlight">3</style>) [Charge] Count (max <style="highlight">8</style>)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Charge] o wartość ([Charge] + <style="highlight">3</style>) (maks. <style="highlight">8</style>)
459. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Sinking] 4 부여, [Sinking] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061203].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking] and <style="highlight">+4</style> [Sinking] Count
   PL: [OnSucceedAttack] Nakłada 4 [Sinking] i zwiększa Licznik [Sinking] o <style="highlight">4</style>
460. [Obrona (ulepszenia 1,4) — nazwa] 에너지 응집
   źródło: Skills_personality-06.json :: dataList[id=1061204].levelList[level=1].name ; dataList[id=1061204].levelList[level=4].name
   kontekst: grzech: Envy · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Energy Condensation
   PL: Zgęstnienie Energii
461. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수가 10 이상이면, 코인 위력 +2\n[WhenUse] 자신의 [Charge] 횟수 3 증가 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061204].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 10+ [Charge] Count, Coin Power +2\n[WhenUse] Gain +3 [Charge] Count (once per turn)
   PL: [WhenUse] Przy 10+ Liczniku [Charge] Moc Monet +2\n[WhenUse] Zwiększa własny Licznik [Charge] o 3 (1 raz na turę)
462. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 [Charge] 횟수가 10 이상이면, 코인 위력 <style="highlight">+4</style>\n[WhenUse] 자신의 [Charge] 횟수 3 증가 (턴당 <style="highlight">2</style>회)
   źródło: Skills_personality-06.json :: dataList[id=1061204].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] At 10+ [Charge] Count, Coin Power <style="highlight">+4</style>\n[WhenUse] Gain +3 [Charge] Count (<style="highlight">2 times</style> per turn)
   PL: [WhenUse] Przy 10+ Liczniku [Charge] Moc Monet <style="highlight">+4</style>\n[WhenUse] Zwiększa własny Licznik [Charge] o 3 (maks. <style="highlight">2</style> razy na turę)
463. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 뇌파 충전 집속 뿔
   źródło: Passives.json :: dataList[id=1061201].name
   limit: do 50 znaków
   EN: Brainwave Charge-focusing Antlers
   PL: Rogi Skupiające Ładowanie Fal Mózgowych
464. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음\n\n[Charge]이 2 이상이면,\n- 기본 공격 스킬로 부여하는 [Sinking] 부여량 +1 ([Sinking] 횟수만 증가하거나 스스로 [Sinking]을 얻는 경우에는 적용되지 않음)\n- 기본 공격 스킬의 피해량이 ([Charge] x 3)%만큼 증가 (최대 15%)
   źródło: Passives.json :: dataList[id=1061201].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [Sinking]
   znaczenie tagów: [Charge] = 충전 / Charge; [Sinking] = 침잠 / Sinking
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\n\nAt 2+ [Charge]:\n- Inflict +1 more [Sinking] using Base Attack Skills (does not activate when inflicting only [Sinking] Count or when inflicting [Sinking] on self)\n- Deal +([Charge] x 3)% damage using Base Attack Skills (max 15%)
   PL: Za każde łączne zużycie 10 własnego Licznika [Charge] podczas walki zyskuje 1 [Charge]\n\nPrzy 2+ [Charge]:\n- Podstawowe Umiejętności ataku nakładają o 1 więcej [Sinking] (nie aktywuje się, gdy nakłada tylko Licznik [Sinking] albo zyskuje [Sinking] na sobie)\n- Podstawowe Umiejętności ataku zadają +(własne [Charge] x 3)% obrażeń (maks. 15%)
465. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — nazwa] 뇌파 충전 집속 뿔
   źródło: Passives.json :: dataList[id=1061211].name
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Envy) — opis] 전투 중 누적으로 자신의 [Charge] 횟수 10을 소모할 때마다, [Charge] 1 얻음\n\n[Charge]이 2 이상이면,\n<style="highlight">- [Charge] 2당 기본 공격 스킬로 부여하는 [Sinking] 부여량 +1 (최대 2, [Sinking] 횟수만 증가하거나 스스로 [Sinking]을 얻는 경우에는 적용되지 않음)</style>\n- 기본 공격 스킬의 피해량이 ([Charge] x <style="highlight">5</style>)%만큼 증가 (최대 <style="highlight">25%</style>)
   źródło: Passives.json :: dataList[id=1061211].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Charge], [Sinking]
   znaczenie tagów: [Charge] = 충전 / Charge; [Sinking] = 침잠 / Sinking
   EN: Gain 1 [Charge] every time this unit consumes 10 cumulative [Charge] Count in this Encounter\n\nAt 2+ [Charge]:\n<style="highlight">- Inflict +1 more [Sinking] using Base Attack Skills for every 2 [Charge] (max 2, does not activate when inflicting only [Sinking] Count or when inflicting [Sinking] on self)</style>\n- Deal +([Charge] x <style="highlight">5</style>)% damage using Base Attack Skills (max <style="highlight">25%</style>)
   PL: Za każde łączne zużycie 10 własnego Licznika [Charge] podczas walki zyskuje 1 [Charge]\n\nPrzy 2+ [Charge]:\n<style="highlight">- Podstawowe Umiejętności ataku nakładają o 1 więcej [Sinking] za każde 2 [Charge] (maks. 2; nie aktywuje się, gdy nakłada tylko Licznik [Sinking] albo zyskuje [Sinking] na sobie)</style>\n- Podstawowe Umiejętności ataku zadają +(własne [Charge] x <style="highlight">5</style>)% obrażeń (maks. <style="highlight">25%</style>)
467. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — nazwa] 충전 분쇄 지원
   źródło: Passives.json :: dataList[id=1061221].name
   limit: do 50 znaków
   EN: Charged Pulverization Support
   PL: Wsparcie Rozdrabniania Ładowaniem
468. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Envy) — opis] [Charge]이 가장 높은 아군 1명이 [Charge] 횟수를 획득하는 기본 공격 스킬 사용 시, 마지막 코인의 피해량 +10%
   źródło: Passives.json :: dataList[id=1061221].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: 1 ally that has the most [Charge]: When using a Base Attack Skill that gains [Charge] Count, deal +10% damage using the final Coin
   PL: Gdy 1 Sojusznik z najwyższym [Charge] użyje podstawowej Umiejętności ataku zyskującej Licznik [Charge], jego ostatnia moneta zadaje +10% obrażeń
469. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Envy) — nazwa] 충전 분쇄 지원
   źródło: Passives.json :: dataList[id=1061231].name
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Pasywka wsparcia (od ulepszenia 4, posiadane 3× Envy) — opis] [Charge]이 가장 높은 아군 1명이 [Charge] 횟수를 획득하는 기본 공격 스킬 사용 시, 마지막 코인의 피해량 <style="highlight">+15%</style>
   źródło: Passives.json :: dataList[id=1061231].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: 1 ally that has the most [Charge]: When using a Base Attack Skill that gains [Charge] Count, deal <style="highlight">+15%</style> damage using the final Coin
   PL: Gdy 1 Sojusznik z najwyższym [Charge] użyje podstawowej Umiejętności ataku zyskującej Licznik [Charge], jego ostatnia moneta zadaje <style="highlight">+15%</style> obrażeń

## [000] The Lord of Hongyuan — Hong Lu — 홍원 군주
- ID Tożsamości: `10613` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 60 · szybkość: 4–6 / 4–7 / 4–8 / 4–8
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture, Poise

471. [Karta Tożsamości — tytuł] 홍원 군주
   źródło: Personalities.json :: dataList[id=10613].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Lord\nof Hongyuan
   PL: Władca\nHongyuan
472. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10613].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10613].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Karta Tożsamości — opis] 홍루의 열세번째 인격
   źródło: Personalities.json :: dataList[id=10613].desc
   limit: do 120 znaków
   EN: Hong Lu's 13th Identity
   PL: Trzynasta Tożsamość Hong Lu
475. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 길을 열고 싶군
   źródło: Skills_personality-06.json :: dataList[id=1061301].levelList[level=1].name ; dataList[id=1061301].levelList[level=2].name ; dataList[id=1061301].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Slash · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: I Wish to Open the Path
   PL: Pragnę Otworzyć Drogę
476. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [StartBattle] 본인을 제외한 아군 1 + (최대 공명 수 / 3)명에게 [Endurance] 1 부여. (턴 당 1회, 최대 3. [SupportProtect]를 보유한 대상에게 우선 부여. 특수 원호 방어[TabExplain] 포함)
   źródło: Skills_personality-06.json :: dataList[id=1061301].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Endurance], [SupportProtect], [TabExplain]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Endurance] = 수비 위력 증가 / Defense Power Up; [SupportProtect] = 원호 방어 / Assist Defense
   EN: [StartBattle] Apply 1 [Endurance] to 1 + (highest Reson. / 3) other allies. (once per turn; max 3; prioritizes targets that have [SupportProtect]; includes Unique Assist Defenses)
   PL: [StartBattle] Nakłada 1 [Endurance] na 1 + (najwyższy Rezonans / 3) innych sojuszników. (1 raz na turę; maks. 3; najpierw cele z [SupportProtect]; łącznie ze Specjalnymi Obronami Wsparcia[TabExplain])
477. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +2 Licznika [Breath]
478. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Burst]
479. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [StartBattle] 본인을 제외한 아군 1 + (최대 공명 수 / 3)명에게 [Endurance] 1 부여. (턴 당 1회, 최대 3. [SupportProtect]를 보유한 대상에게 우선 부여. 특수 원호 방어[TabExplain] 포함)\n<style="highlight">[WhenUse] 대상의 [Burst]과 자신의 [Breath] 합이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-06.json :: dataList[id=1061301].levelList[level=2].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [Endurance], [SupportProtect], [TabExplain], [WhenUse], [Burst], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Endurance] = 수비 위력 증가 / Defense Power Up; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [StartBattle] Apply 1 [Endurance] to 1 + (highest Reson. / 3) other allies. (once per turn; max 3; prioritizes targets that have [SupportProtect]; includes Unique Assist Defenses as well)\n<style="highlight">[WhenUse] At 6+ ([Burst] on target + [Breath] on self), Coin Power +1</style>
   PL: [StartBattle] Nakłada 1 [Endurance] na 1 + (najwyższy Rezonans / 3) innych sojuszników. (1 raz na turę; maks. 3; najpierw cele z [SupportProtect]; łącznie ze Specjalnymi Obronami Wsparcia[TabExplain])\n<style="highlight">[WhenUse] Przy 6+ (suma [Burst] celu i własnego [Breath]) Moc Monet +1</style>
480. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061301].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Breath] o 2<style="highlight"></style>
481. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061301].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061301].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Burst] celu o 2<style="highlight"></style>
482. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [StartBattle] 본인을 제외한 아군 1 + (최대 공명 수 / 3)명에게 [Endurance] 1 부여. (턴 당 1회, 최대 3. [SupportProtect]를 보유한 대상에게 우선 부여. 특수 원호 방어[TabExplain] 포함)\n[WhenUse] 대상의 [Burst]과 자신의 [Breath] 합이 6 이상이면, 코인 위력 +1\n<style="highlight">[WhenUse] 대상의 부정적인 효과가 3개 이상이면, 합 위력 +1</style>
   źródło: Skills_personality-06.json :: dataList[id=1061301].levelList[level=4].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [Endurance], [SupportProtect], [TabExplain], [WhenUse], [Burst], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Endurance] = 수비 위력 증가 / Defense Power Up; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [StartBattle] Apply 1 [Endurance] to 1 + (highest Reson. / 3) other allies. (once per turn; max 3; prioritizes targets that have [SupportProtect]; includes Unique Assist Defenses)\n[WhenUse] At 6+ ([Burst] on target + [Breath] on self), Coin Power +1\n<style="highlight">[WhenUse] If target has 3+ types of negative effects, Clash Power +1</style>
   PL: [StartBattle] Nakłada 1 [Endurance] na 1 + (najwyższy Rezonans / 3) innych sojuszników. (1 raz na turę; maks. 3; najpierw cele z [SupportProtect]; łącznie ze Specjalnymi Obronami Wsparcia[TabExplain])\n[WhenUse] Przy 6+ (suma [Burst] celu i własnego [Breath]) Moc Monet +1\n<style="highlight">[WhenUse] Jeżeli cel ma 3+ rodzajów negatywnych efektów, Moc Starcia +1</style>
483. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +<style="highlight">3</style> [Breath] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Breath] o <style="highlight">3</style>
484. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 오혈절지경성[汚血絕志竟成]
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=1].name ; dataList[id=1061302].levelList[level=2].name ; dataList[id=1061302].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 3 · monety: 4 (+3)
   limit: do 80 znaków
   EN: Tarnished Blood's Absolute Cleaver of Ambitions [汚血絕志竟成]
   PL: Zbrukana Krew Absolutnym Siecznym Ambicji [汚血絕志竟成]
485. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [Breath] 2 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain 2 [Breath]
   PL: [WhenUse] Zyskuje 2 [Breath]
486. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +1 Licznika [Breath]
488. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 대상의 [Burst]과 자신의 [Breath] 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] [Breath] <style="highlight">3</style> 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: <style="highlight">[WhenUse] At 6+ ([Burst] on target + [Breath] on self), Coin Power +1</style>\n[WhenUse] Gain <style="highlight">3</style> [Breath]
   PL: <style="highlight">[WhenUse] Przy 6+ (suma [Burst] celu i własnego [Breath]) Moc Monet +1</style>\n[WhenUse] Zyskuje <style="highlight">3</style> [Breath]
492. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1061302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]<style="highlight"></style>
493. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje +1 Licznika [Breath]<style="highlight"></style>
494. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1061302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Burst] 1 부여</style>
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Burst]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [Burst]</style>
496. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 4, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=2].coinlist[#3].coindescs[#0].desc ; dataList[id=1061302].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 4, efekt 2 — opis] <style="highlight">피해량 +50%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=2].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">Deal +50% damage</style>
   PL: <style="highlight">Zadaje +50% obrażeń</style>
498. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=2].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Burst]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Burst]
499. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">[StartBattle] 자신을 제외한 이번 턴에 탐식 스킬을 장착한 아군에게 [ShamrockDamageUp] 1 부여 (턴 당 1회)</style>\n<style="highlight">[WhenUse] 대상의 [Burst]과 자신의 [Breath] 합 6 당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [ShamrockDamageUp], [WhenUse], [Burst], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ShamrockDamageUp] = 탐식 피해량 증가 / Gluttony DMG Up; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: <style="highlight">[StartBattle] Apply 1 [ShamrockDamageUp] to all other allies that have Gluttony Skills equipped this turn (once per turn)</style>\n<style="highlight">[WhenUse] Coin Power +1 for every 6 ([Burst] on target + [Breath] on self) (max 2)</style>\n[WhenUse] Gain 3 [Breath]
   PL: <style="highlight">[StartBattle] Nakłada 1 [ShamrockDamageUp] na wszystkich innych sojuszników z wyposażoną Umiejętnością Obżarstwa w tej turze (1 raz na turę)</style>\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 (suma [Burst] celu i własnego [Breath]) (maks. 2)</style>\n[WhenUse] Zyskuje 3 [Breath]
500. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 480 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Burst]<style="highlight"></style>
502. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 4, efekt 2 — opis] 피해량 +50%<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal +50% damage<style="highlight"></style>
   PL: Zadaje +50% obrażeń<style="highlight"></style>
503. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 4, efekt 3 — opis] <style="highlight">크리티컬 피해량 +50%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=4].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 4, efekt 4 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061302].levelList[level=4].coinlist[#3].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Burst]<style="highlight"></style>
505. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 흑수들이여 답하라
   źródło: Skills_personality-06.json :: dataList[id=1061303].levelList[level=3].name ; dataList[id=1061303].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 10 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Answer Me, Heishou Packs
   PL: Odpowiedzcie Mi, Wataho Heishou
506. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 이 스킬은 수비 스킬을 발동시키지 않음\n\n[WhenUse] [Breath] 3 얻음, [Breath] 횟수 1 증가\n\n[EndSkill] 현재 행동 가능한 [HeishouComboCount]이 가장 낮은 아군 흑수에게 [HeishouComboCount] 1 부여하고, [HeishouCombo] 명령. (턴 당 1회)\n- [HeishouCombo]이 종료되면, '군주의 길을 열겠다' 사용\n- [HeishouCombo]이 발동하지 않았거나, [HeishouCombo] 종료 전 연계 중인 인격이 흐트러졌거나 사망한 경우, 대신 '혈혈단신, 사생취원' 사용
   źródło: Skills_personality-06.json :: dataList[id=1061303].levelList[level=3].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [EndSkill], [HeishouComboCount], [HeishouCombo]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [HeishouComboCount] = 몰아침 / Unrelenting Storm; [HeishouCombo] = 존명 / Exalted Command
   EN: This Skill does not trigger Defense Skills\n\n[WhenUse] Gain 3 [Breath] and +1 [Breath] Count\n\n[EndSkill] Among ally Heishou Pack units that can act, choose 1 unit that has the least [HeishouComboCount] Stack and apply [HeishouComboCount]; then, bestow [HeishouCombo]. (once per turn)\n- After [HeishouCombo] is complete, The Lord of Hongyuan Hong Lu activates 'I Carve the Path of a Lord'\n- If [HeishouCombo] did not activate, or if the combo Identity is Staggered or defeated before [HeishouCombo] is complete, use 'Lonesome Stand: Sacrifice to Claim the Garden' instead
   PL: Ta Umiejętność nie uruchamia Umiejętności obrony\n\n[WhenUse] Zyskuje 3 [Breath] i zwiększa Licznik [Breath] o 1\n\n[EndSkill] Wśród sojuszniczych Watah Heishou zdolnych do działania wybiera 1 jednostkę z najmniejszym stosem [HeishouComboCount], nakłada [HeishouComboCount], po czym rozkazuje [HeishouCombo]. (1 raz na turę)\n- Po zakończeniu [HeishouCombo] Władca Hongyuan Hong Lu uruchamia „Wytyczam Drogę Władcy”\n- Jeżeli [HeishouCombo] się nie uruchomiło albo Tożsamość wykonująca kombinację zostanie Ogłuszona albo pokonana przed jego zakończeniem, zamiast tego używa „Samotny Stand: Poświęcenie, by Zdobyć Ogród”
507. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061303].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 보유한 부정적인 효과 2종류 당 [AttackDown] 1 부여 (최대 3)
   źródło: Skills_personality-06.json :: dataList[id=1061303].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown] for every 2 types of negative effect on target (max 3)
   PL: [OnSucceedAttack] Nakłada 1 [AttackDown] za każde 2 rodzaje negatywnych efektów na celu (maks. 3)
509. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상이 보유한 주살 1종류 당 [DefenseDown] 1 부여 (최대 3)
   źródło: Skills_personality-06.json :: dataList[id=1061303].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown] for every type of Deathrite on target (max 3)
   PL: [OnSucceedAttack] Nakłada 1 [DefenseDown] za każdy rodzaj Obrzędu Śmierci na celu (maks. 3)
510. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 이 스킬은 수비 스킬을 발동시키지 않음\n\n<style="highlight">[WhenUse] 대상의 [Burst]과 자신의 [Breath] 합 4 당, 코인 위력 +1 (최대 3)</style>\n[WhenUse] [Breath] <style="highlight">5</style> 얻음, [Breath] 횟수 <style="highlight">3</style> 증가\n\n[EndSkill] 현재 행동 가능한 [HeishouComboCount]이 가장 낮은 아군 흑수에게 [HeishouComboCount] 1 부여하고, [HeishouCombo] 명령. (턴 당 1회)\n- [HeishouCombo]이 종료되면, '군주의 길을 열겠다' 사용\n- [HeishouCombo]이 발동하지 않았거나, [HeishouCombo] 종료 전 연계 중인 인격이 흐트러졌거나 사망한 경우, 대신 '혈혈단신, 사생취원' 사용
   źródło: Skills_personality-06.json :: dataList[id=1061303].levelList[level=4].desc
   limit: do 820 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [Breath], [EndSkill], [HeishouComboCount], [HeishouCombo]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]; [HeishouComboCount] = 몰아침 / Unrelenting Storm; [HeishouCombo] = 존명 / Exalted Command
   EN: This Skill does not trigger Defense Skills\n\n<style="highlight">[WhenUse] Coin Power +1 for every 4 ([Burst] on target + [Breath] on self) (max 3)</style>\n[WhenUse] Gain <style="highlight">5</style> [Breath] and +<style="highlight">3</style> [Breath] Count\n\n[EndSkill] Among ally Heishou Pack units that can act, choose 1 unit that has the least [HeishouComboCount] Stack and apply [HeishouComboCount]; then, bestow [HeishouCombo]. (once per turn)\n- After [HeishouCombo] is complete, The Lord of Hongyuan Hong Lu activates 'I Carve the Path of a Lord'\n- If [HeishouCombo] did not activate, or if the combo Identity is Staggered or defeated before [HeishouCombo] is complete, use 'Lonesome Stand: Sacrifice to Claim the Garden' instead
   PL: Ta Umiejętność nie uruchamia Umiejętności obrony\n\n<style="highlight">[WhenUse] Moc Monet +1 za każde 4 (suma [Burst] celu i własnego [Breath]) (maks. 3)</style>\n[WhenUse] Zyskuje <style="highlight">5</style> [Breath] i zwiększa Licznik [Breath] o <style="highlight">3</style>\n\n[EndSkill] Wśród sojuszniczych Watah Heishou zdolnych do działania wybiera 1 jednostkę z najmniejszym stosem [HeishouComboCount], nakłada [HeishouComboCount], po czym rozkazuje [HeishouCombo]. (1 raz na turę)\n- Po zakończeniu [HeishouCombo] Władca Hongyuan Hong Lu uruchamia „Wytyczam Drogę Władcy”\n- Jeżeli [HeishouCombo] się nie uruchomiło albo Tożsamość wykonująca kombinację zostanie Ogłuszona albo pokonana przed jego zakończeniem, zamiast tego używa „Samotny Stand: Poświęcenie, by Zdobyć Ogród”
511. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 보유한 부정적인 효과 2종류 당 [AttackDown] 1 부여 (최대 3)<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061303].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [AttackDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDown] for every 2 types of negative effect on target (max 3)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [AttackDown] za każde 2 rodzaje negatywnych efektów na celu (maks. 3)<style="highlight"></style>
513. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상이 보유한 주살 1종류 당 [DefenseDown] 1 부여 (최대 3)<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061303].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 1 [DefenseDown] for every type of Deathrite on target (max 3)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [DefenseDown] za każdy rodzaj Obrzędu Śmierci na celu (maks. 3)<style="highlight"></style>
514. [Umiejętność 4 (×0) (ulepszenia 1,4) — nazwa] 군주의 길을 열겠다
   źródło: Skills_personality-06.json :: dataList[id=1061305].levelList[level=1].name ; dataList[id=1061305].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 6 · monety: 2 (+4)
   limit: do 40 znaków
   EN: I Carve the Path of a Lord
   PL: Wytyczam Drogę Władcy
515. [Umiejętność 4 (×0) (ulepszenie 1) — opis] [WhenUse] 흑수 필두 인격과 연계했으면, 기본 위력 +1, 코인 위력 +1\n\n[WhenUse] 대상의 [Burst]과 자신의 호흡 합이 6 이상이면, 코인 위력 +1\n[WhenUse] [HeishouComboCountHonglu] 1 당 피해량 +5%\n[EndSkill] [HeishouCombo]을 발동한 흑수 인격에 따라 [HeishouComboCountHonglu] 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061305].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [HeishouComboCountHonglu], [EndSkill], [HeishouCombo], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [HeishouComboCountHonglu] = 흑수환염[黑獣丸染] / Heishou Bolus Contamination [黑獣丸染]; [EndSkill] = [공격 종료시] / [Attack End]; [HeishouCombo] = 존명 / Exalted Command; [Breath] = 호흡 / Poise
   EN: [WhenUse] If this unit activated combo with a Heishou Pack Adept Identity: Base Power +1, Coin Power +1\n\n[WhenUse] At 6+ ([Burst] on target + [Breath] on self), Coin Power +1\n[WhenUse] Deal +5% damage for every [HeishouComboCountHonglu]\n[EndSkill] Gain [HeishouComboCountHonglu] depending on which Heishou Pack Identity activated [HeishouCombo]
   PL: [WhenUse] Jeżeli uruchomiła kombinację z Przewodzącą Tożsamością Watahy Heishou: Moc Bazowa +1, Moc Monet +1\n\n[WhenUse] Przy 6+ (suma [Burst] celu i własnego Oddechu) Moc Monet +1\n[WhenUse] Zadaje +5% obrażeń za każde 1 [HeishouComboCountHonglu]\n[EndSkill] Zyskuje [HeishouComboCountHonglu] zależnie od tego, która Tożsamość Watahy Heishou uruchomiła [HeishouCombo]
516. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061305].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 2, efekt 2 — opis] [EnemyKill] 아군 흑수 인격 중 정신력이 가장 낮은 대상 2명의 정신력 10을 회복하고, 다음 턴에 [Enhancement] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061305].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Enhancement]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EnemyKill] For 2 ally Heishou Pack Identities that have the least SP, heal 10 SP and apply 1 [Enhancement] next turn
   PL: [EnemyKill] Odzyskuje 10 Poczytalności dla 2 Tożsamości Watahy Heishou z najniższą Poczytalnością i nakłada w następnej turze 1 [Enhancement]
519. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [WhenUse] 흑수 필두 인격과 연계했으면, 기본 위력 +1, 코인 위력 +1\n\n<style="highlight">대상과 자신의 잃은 체력 합 1% 당 피해량 +1% (최대 50%)</style>\n<style="highlight">[WhenUse] 대상의 [Burst]과 자신의 호흡 합 6 당, 코인 위력 +1 (최대 3)</style>\n<style="highlight">[WhenUse] 대상의 부정적인 효과 2개 당 피해량 +10% (최대 30%)</style>\n[WhenUse] [HeishouComboCountHonglu] 1 당 피해량 <style="highlight">+10%</style>\n[EndSkill] [HeishouCombo]을 발동한 흑수 인격에 따라 [HeishouComboCountHonglu] 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061305].levelList[level=4].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [HeishouComboCountHonglu], [EndSkill], [HeishouCombo]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [HeishouComboCountHonglu] = 흑수환염[黑獣丸染] / Heishou Bolus Contamination [黑獣丸染]; [EndSkill] = [공격 종료시] / [Attack End]; [HeishouCombo] = 존명 / Exalted Command
   EN: [WhenUse] If this unit activated combo with a Heishou Pack Adept Identity: Base Power +1, Coin Power +1\n\n<style="highlight">Deal +1% damage for every 1% (missing HP percentage on target + missing HP percentage on self) (max 50%)</style>\n[WhenUse] <style="highlight">Coin Power +1 for every 6 ([Burst] on target + Poise on self) (max 3)</style>\n<style="highlight">[WhenUse] Deal +10% damage for every 2 types of negative effects on target (max 30%)</style>\n[WhenUse] Deal <style="highlight">+10%</style> damage for every [HeishouComboCountHonglu]\n[EndSkill] Gain [HeishouComboCountHonglu] depending on which Heishou Identity activated [HeishouCombo]
   PL: [WhenUse] Jeżeli uruchomiła kombinację z Przewodzącą Tożsamością Watahy Heishou: Moc Bazowa +1, Moc Monet +1\n\n<style="highlight">Zadaje +1% obrażeń za każde 1% (suma brakującego HP celu i własnego) (maks. 50%)</style>\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 (suma [Burst] celu i własnego [Breath]) (maks. 3)</style>\n<style="highlight">[WhenUse] Zadaje +10% obrażeń za każde 2 rodzaje negatywnych efektów celu (maks. 30%)</style>\n[WhenUse] Zadaje <style="highlight">+10%</style> obrażeń za każde 1 [HeishouComboCountHonglu]\n[EndSkill] Zyskuje [HeishouComboCountHonglu] zależnie od tego, która Tożsamość Watahy Heishou uruchomiła [HeishouCombo]
520. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061305].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] <style="highlight">크리티컬 피해량 +50%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061305].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">Deal +50% Damage on Critical Hit</style>
   PL: <style="highlight">Zadaje +50% obrażeń przy trafieniu krytycznym</style>
522. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061305].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 3 — opis] <style="highlight">[OnSucceedAttack] 다음 턴에 [SlashResistDown] 1 부여 (턴 당 1회)</style>
   źródło: Skills_personality-06.json :: dataList[id=1061305].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [SlashResistDown] next turn (once per turn)</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada w następnej turze 1 [SlashResistDown] (1 raz na turę)</style>
524. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 4 — opis] [EnemyKill] 아군 흑수 인격 중 정신력이 가장 낮은 대상 2명의 정신력 10을 회복하고, 다음 턴에 [Enhancement] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061305].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EnemyKill], [Enhancement]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EnemyKill] For 2 ally Heishou Pack Identities that have the least SP, heal 10 SP and apply 1 [Enhancement] next turn<style="highlight"></style>
   PL: [EnemyKill] Odzyskuje 10 Poczytalności dla 2 Tożsamości Watahy Heishou z najniższą Poczytalnością i nakłada w następnej turze 1 [Enhancement]<style="highlight"></style>
525. [Umiejętność 5 (×0) (ulepszenia 1,4) — nazwa] 혈혈단신, 사생취원[孑孑單身, 捨生取园]
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=1].name ; dataList[id=1061306].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 6 · monety: 3 (+4)
   limit: do 80 znaków
   EN: Lonesome Stand: Sacrifice to Claim The Garden [孑孑單身, 捨生取园]
   PL: Samotny Stand: Poświęcenie, by Zdobyć Ogród [孑孑單身, 捨生取园]
526. [Umiejętność 5 (×0) (ulepszenie 1) — opis] 자신의 [HeishouDeathCount] 당 피해량 +10%\n대상과 자신의 잃은 체력 합 1% 당 피해량 +1% (최대 50%)\n[WhenUse] [HeishouDeathCount]이 3 이상이면, 이 스킬 가중치 +1\n[WhenUse] 대상의 [Burst]과 자신의 호흡 합이 6 이상이면, 코인 위력 +1\n[WhenUse] [HeishouComboCountHonglu] 1 당 피해량 +5%
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [HeishouDeathCount], [WhenUse], [Burst], [HeishouComboCountHonglu], [Breath]
   znaczenie tagów: [HeishouDeathCount] = 사중구활[死中求活] / Life from Death [死中求活]; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [HeishouComboCountHonglu] = 흑수환염[黑獣丸染] / Heishou Bolus Contamination [黑獣丸染]; [Breath] = 호흡 / Poise
   EN: Deal +10% damage for every [HeishouDeathCount] on self\nDeal +1% damage for every 1% (missing HP percentage on target + missing HP percentage on self) (max 50%)\n[WhenUse] At 3+ [HeishouDeathCount], gain +1 Atk Weight\n[WhenUse] At 6+ ([Burst] on target + [Breath] on self), Coin Power +1\n[WhenUse] Deal +5% damage for every [HeishouComboCountHonglu]
   PL: Zadaje +10% obrażeń za każde 1 własnego [HeishouDeathCount]\nZadaje +1% obrażeń za każde 1% (suma brakującego HP celu i własnego) (maks. 50%)\n[WhenUse] Przy 3+ [HeishouDeathCount] Waga ataku tej Umiejętności +1\n[WhenUse] Przy 6+ (suma [Burst] celu i własnego Oddechu) Moc Monet +1\n[WhenUse] Zadaje +5% obrażeń za każde 1 [HeishouComboCountHonglu]
527. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 3, efekt 1 — opis] 대상이 보유한 부정적인 효과 1개 당 피해량 +10% (최대 50%)
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +10% damage for every type of negative effect on target (max 50%)
   PL: Zadaje +10% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 50%)
530. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [SlashResistDown] 1 부여 (턴 당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [OnSucceedAttack] Inflict 1 [SlashResistDown] next turn (once per turn)
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [SlashResistDown] (1 raz na turę)
532. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 3, efekt 4 — opis] [EnemyKill] 다음 턴에 [Enhancement] 1 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [Enhancement]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EnemyKill] Gain 1 [Enhancement] next turn
   PL: [EnemyKill] Zyskuje w następnej turze 1 [Enhancement]
533. [Umiejętność 5 (×0) (ulepszenie 4) — opis] 자신의 [HeishouDeathCount] 당 피해량 +10%\n대상과 자신의 잃은 체력 합 1% 당 피해량 +1% (최대 50%)\n[WhenUse] [HeishouDeathCount]이 3 이상이면, 이 스킬 가중치 +1\n<style="highlight">[WhenUse] 대상의 [Burst]과 자신의 호흡 합 6 당, 코인 위력 +1 (최대 3)</style>\n<style="highlight">[WhenUse] 대상의 부정적인 효과 2개 당 피해량 +10% (최대 30%)</style>\n[WhenUse] [HeishouComboCountHonglu] 1 당 피해량 <style="highlight">+10%</style>
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=4].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [HeishouDeathCount], [WhenUse], [Burst], [HeishouComboCountHonglu], [Breath]
   znaczenie tagów: [HeishouDeathCount] = 사중구활[死中求活] / Life from Death [死中求活]; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [HeishouComboCountHonglu] = 흑수환염[黑獣丸染] / Heishou Bolus Contamination [黑獣丸染]; [Breath] = 호흡 / Poise
   EN: Deal +10% damage for every [HeishouDeathCount] on self\nDeal +1% damage for every 1% (missing HP percentage on target + missing HP percentage on self) (max 50%)\n[WhenUse] At 3+ [HeishouDeathCount], gain +1 Atk Weight\n<style="highlight">[WhenUse] Coin Power +1 for every 6 ([Burst] on target + [Breath] on self) (max 3)</style>\n<style="highlight">[WhenUse] Deal +10% damage for every 2 types of negative effects on target (max 30%)</style>\n[WhenUse] Deal <style="highlight">+10%</style> damage for every [HeishouComboCountHonglu]
   PL: Zadaje +10% obrażeń za każde 1 własnego [HeishouDeathCount]\nZadaje +1% obrażeń za każde 1% (suma brakującego HP celu i własnego) (maks. 50%)\n[WhenUse] Przy 3+ [HeishouDeathCount] Waga ataku tej Umiejętności +1\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 (suma [Burst] celu i własnego Oddechu) (maks. 3)</style>\n<style="highlight">[WhenUse] Zadaje +10% obrażeń za każde 2 rodzaje negatywnych efektów celu (maks. 30%)</style>\n[WhenUse] Zadaje <style="highlight">+10%</style> obrażeń za każde 1 [HeishouComboCountHonglu]
534. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] 대상이 보유한 부정적인 효과 1개 당 피해량 +10% (최대 50%)<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal +10% damage for every type of negative effect on target (max 50%)<style="highlight"></style>
   PL: Zadaje +10% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 50%)<style="highlight"></style>
537. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [SlashResistDown] 1 부여 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [OnSucceedAttack] Inflict 1 [SlashResistDown] next turn (once per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [SlashResistDown] (1 raz na turę)<style="highlight"></style>
539. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 3, efekt 4 — opis] [EnemyKill] 다음 턴에 [Enhancement] <style="highlight">2</style> 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061306].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [EnemyKill], [Enhancement]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EnemyKill] Gain <style="highlight">2</style> [Enhancement] next turn
   PL: [EnemyKill] Zyskuje w następnej turze <style="highlight">2</style> [Enhancement]
540. [Obrona (ulepszenia 1,4) — nazwa] 흑수이조[黑獣利爪]
   źródło: Skills_personality-06.json :: dataList[id=1061304].levelList[level=1].name ; dataList[id=1061304].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 6 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Heishou Keenclaw [黑獣利爪]
   PL: Heishou Bystry Pazur [黑獣利爪]
541. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] 아군 흑수 인격 (최대 공명 수)명에게 [SlashResultUp] 1 부여 (턴 당 1회)\n\n[StartBattle] 대기 인원이 있으면 현재 체력 비율이 가장 낮은 아군 흑수 1명을 지정.\n- 이 스킬 사용 시 지정한 대상에게 [HeishouAttack] 부여, 턴 종료시 [RetreatForCommon]을 명령하고, 퇴각 시 최대 체력의 10%를 회복시킴 (턴 당 1회)\n- 이 효과로 퇴각한 흑수 인격은, 복귀할 인격 중 흑수가 아닌 인격보다 복귀 순서가 빠르게 배치됨\n[StartBattle] 대기 인원이 없으면, 현재 체력 비율이 가장 낮은 아군 흑수 1명에게 [Enhancement] 2 부여 (턴 당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061304].levelList[level=1].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [SlashResultUp], [HeishouAttack], [RetreatForCommon], [Enhancement]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [SlashResultUp] = 참격 위력 증가 / Slash Power Up; [HeishouAttack] = 뜻에 따라, 베겠습니다. / Your Will Guides My Blade.; [RetreatForCommon] = 전장 퇴각 / Battlefield Retreat; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [DuelCounter]\n[StartBattle] Apply 1 [SlashResultUp] to (highest Reson.) Heishou Pack Identity allies (once per turn)\n\n[StartBattle] If there are Backup Units, select 1 ally Heishou that has the least HP percentage.\n- Upon using this Skill, apply [HeishouAttack] to the selected ally, command [RetreatForCommon], and heal 10% of their HP upon Retreating (once per turn)\n- The Heishou Pack Identity who Retreated due to this effect will be placed earlier in the Return line than non-Heishou Identities\n[StartBattle] If there are no Backup Units, apply 2 [Enhancement] to 1 ally Heishou that has the least HP percentage (once per turn)
   PL: [DuelCounter]\n[StartBattle] Nakłada 1 [SlashResultUp] na (najwyższy Rezonans / N) sojuszniczych Tożsamości Watah Heishou (1 raz na turę)\n\n[StartBattle] Jeżeli są jednostki w rezerwie, namierza 1 sojuszniczą Watahę Heishou z najniższym procentem HP.\n- Przy użyciu tej Umiejętności nakłada [HeishouAttack] na namierzonego sojusznika, rozkazuje [RetreatForCommon] na koniec tury i leczy 10% jego Maks. HP przy Odwrócie (1 raz na turę)\n- Tożsamość Watahy Heishou wycofana tym efektem jest szybciej umieszczana w kolejce Powrotów niż Tożsamości spoza Watah Heishou\n[StartBattle] Jeżeli nie ma jednostek w rezerwie, nakłada 2 [Enhancement] na 1 sojuszniczą Watahę Heishou z najniższym procentem HP (1 raz na turę)
542. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[StartBattle] 아군 흑수 인격 (최대 공명 수)명에게 [SlashResultUp] 1 부여 (턴 당 1회)\n\n[StartBattle] 대기 인원이 있으면 현재 체력 비율이 가장 낮은 아군 흑수 1명을 지정.\n- 이 스킬 사용 시 지정한 대상에게 [HeishouAttack] 부여, 턴 종료시 [RetreatForCommon]을 명령하고, 퇴각 시 최대 체력의 10%를 회복시킴 (턴 당 1회)\n- 이 효과로 퇴각한 흑수 인격은, 복귀할 인격 중 흑수가 아닌 인격보다 복귀 순서가 빠르게 배치됨\n[StartBattle] 대기 인원이 없으면, 현재 체력 비율이 가장 낮은 아군 흑수 1명에게 [Enhancement] 2 부여 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061304].levelList[level=4].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [SlashResultUp], [HeishouAttack], [RetreatForCommon], [Enhancement]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [SlashResultUp] = 참격 위력 증가 / Slash Power Up; [HeishouAttack] = 뜻에 따라, 베겠습니다. / Your Will Guides My Blade.; [RetreatForCommon] = 전장 퇴각 / Battlefield Retreat; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [DuelCounter]\n[StartBattle] Apply 1 [SlashResultUp] to (highest Reson.) Heishou Pack Identity allies (once per turn)\n\n[StartBattle] If there are Backup Units, select 1 ally Heishou that has the least HP percentage.\n- Upon using this Skill, apply [HeishouAttack] to the selected ally, command [RetreatForCommon], and heal 10% of their HP upon Retreating (once per turn)\n- The Heishou Pack Identity who Retreated due to this effect will be placed earlier in the Return line than non-Heishou Identities\n[StartBattle] If there are no Backup Units, apply 2 [Enhancement] to 1 ally Heishou that has the least HP percentage (once per turn)<style="highlight"></style>
   PL: [DuelCounter]\n[StartBattle] Nakłada 1 [SlashResultUp] na (najwyższy Rezonans / N) sojuszniczych Tożsamości Watah Heishou (1 raz na turę)\n\n[StartBattle] Jeżeli są jednostki w rezerwie, namierza 1 sojuszniczą Watahę Heishou z najniższym procentem HP.\n- Przy użyciu tej Umiejętności nakłada [HeishouAttack] na namierzonego sojusznika, rozkazuje [RetreatForCommon] na koniec tury i leczy 10% jego Maks. HP przy Odwrócie (1 raz na turę)\n- Tożsamość Watahy Heishou wycofana tym efektem jest szybciej umieszczana w kolejce Powrotów niż Tożsamości spoza Watah Heishou\n[StartBattle] Jeżeli nie ma jednostek w rezerwie, nakłada 2 [Enhancement] na 1 sojuszniczą Watahę Heishou z najniższym procentem HP (1 raz na turę)<style="highlight"></style>
544. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Obrona (ulepszenie 1) — nazwa] 호위
   źródło: Skills_personality-06.json :: dataList[id=1061307].levelList[level=1].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 2 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Lordsguard
   PL: Straż Władcy
546. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n이 스킬은 해당 스킬을 사용하는 캐릭터의 원호 방어로만 취급되며,\n[SupportProtect] 효과 발동을 체크하는 다른 캐릭터의 효과를 발동시키지 않음.\n[WhenUse] 대상의 부정적인 효과가 3개 이상이면, 합 위력 +1
   źródło: Skills_personality-06.json :: dataList[id=1061307].levelList[level=1].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [SupportProtect], [WhenUse], [TabExplain]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]
   EN: [CanDuelGuard]\nThis Skill counts as Assist Defense[TabExplain] only for the unit that uses the Skill, and does not trigger the effects of other characters that have conditionals that check for [SupportProtect] activation.\n[WhenUse] If target has 3+ types of negative effects, Clash Power +1
   PL: [CanDuelGuard]\nTa Umiejętność liczy się jako Obrona Wsparcia[TabExplain] wyłącznie dla jednostki używającej tej Umiejętności, i nie uruchamia efektów innych postaci sprawdzających aktywację [SupportProtect].\n[WhenUse] Jeżeli cel ma 3+ rodzajów negatywnych efektów, Moc Starcia +1
547. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061307].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Pasywka bojowa (od ulepszenia 1) — nazwa] 흑수군주
   źródło: Passives.json :: dataList[id=1061302].name
   limit: do 40 znaków
   EN: The Heishou Lord
   PL: Heishou Lord
549. [Pasywka bojowa (od ulepszenia 1) — opis] 자신을 제외한 아군 인격이 대기해제 또는 복귀했으면, 정신력을 10 회복하고, 전투 시작시 스킬 1로 무작위 대상에게 일방공격 명령\n- 해당 아군이 흑수 또는 가씨 가문 소속이면 대신 정신력을 20 회복하고, 전투 시작시 기본 스킬 3으로 무작위 대상에게 일방공격 명령 (인격 당 전투 당 2회)\n\n스테이지 시작 시, 대기 인원을 포함하여 편성된 흑수 인격 1명 당 [HeishouSynergy] 1 얻음\n\n전투에서 흑수 인격이 사망 시, 정신력을 20 회복하고, [HeishouDeathCount] 버프 1 얻음\n(자신이 퇴각 상태여도 적용)\n[HeishouComboCountHonglu] 1 당 피해량 +5% (최대 55%)
   źródło: Passives.json :: dataList[id=1061302].desc
   limit: do 930 znaków
   tokeny: zachowaj dokładnie: \n, [HeishouSynergy], [HeishouDeathCount], [HeishouComboCountHonglu]
   znaczenie tagów: [HeishouSynergy] = 모든 흑수의 주인 / Leash-holder of All Heishou; [HeishouDeathCount] = 사중구활[死中求活] / Life from Death [死中求活]; [HeishouComboCountHonglu] = 흑수환염[黑獣丸染] / Heishou Bolus Contamination [黑獣丸染]
   EN: When other ally units Substitute in or Return to the battlefield, they heal 10 SP; then, at Combat Start, command them to use Skill 1 as an Unopposed Attack against a random enemy\n- If the said ally is a Heishou Pack or a Jia Family unit, activate the following instead: heal 20 SP; then, at Combat Start, command them to use their base Skill 3 as an Unopposed Attack against a random enemy (2 times per Encounter per Identity)\n\nEncounter Start: gain 1 [HeishouSynergy] for every Heishou Pack Identity in the Team, including Backup Units\n\nWhen Heishou Units are killed in an Encounter, heal 20 SP and gain 1 [HeishouDeathCount] (activates even when this unit has Retreated)\n\nDeal +5% damage for every 1 [HeishouComboCountHonglu] (max 55%)
   PL: Gdy inne sojusznicze Tożsamości wejdą na pole przez Wejście z rezerwy lub Powrót, odzyskują 10 Poczytalności, a na początku walki otrzymują rozkaz ataku nieopartego Umiejętnością 1 na losowym wrogu\n- Jeżeli tą jednostką jest Wataha Heishou albo frakcja Rodu Jia, zamiast tego odzyskuje 20 Poczytalności, a na początku walki otrzymuje rozkaz ataku nieopartego podstawową Umiejętnością 3 na losowym wrogu (2 razy na spotkanie per Tożsamość)\n\nNa początku spotkania zyskuje 1 [HeishouSynergy] za każdą Tożsamość Watahy Heishou w składzie, łącznie z rezerwą\n\nGdy Tożsamość Watahy Heishou ginie podczas walki, odzyskuje 20 Poczytalności i zyskuje 1 buffu [HeishouDeathCount]\n(działa także, gdy ta jednostka jest wycofana)\nZadaje +5% obrażeń za każde 1 [HeishouComboCountHonglu] (maks. 55%)
550. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] [HeishouComboCountHonglu] 비례 피해량이 증가
   źródło: Passives.json :: dataList[id=1061302].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [HeishouComboCountHonglu]
   znaczenie tagów: [HeishouComboCountHonglu] = 흑수환염[黑獣丸染] / Heishou Bolus Contamination [黑獣丸染]
   EN: Deal more damage based on [HeishouComboCountHonglu]
   PL: Zadaje więcej obrażeń w zależności od [HeishouComboCountHonglu]
551. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — nazwa] 더러운 피마저 받아들이고, 누군가의 피를 묻혀가며 뜻을 이룬다.
   źródło: Passives.json :: dataList[id=1061301].name
   limit: do 90 znaków
   EN: Embrace the Tarnished Blood and Exsanguinate Others For the Cause.
   PL: Przyjmij nawet Zbrukaną Krew i spełnij swój cel, brocząc czyjąś krwią.
552. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — opis] 전투 시작시 자신이 수비스킬을 장착하지 않고 일방공격 당할 예정이면, [SupportProtect] 수치가 가장 낮은 무작위 흑수 아군 (최대 공명 수 / 3)명에게 [HeishouSupportProtect] 1 부여. (최대 2명, 인격 당 1회. [SupportProtect]를 획득하는 스킬 보유 인격 제외)\n\n이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고 해당 턴 동안 체력이 1로 유지되며, [CondensedBlood] 1 얻음 (전투 당 1회)\n\n자신의 [CondensedBlood] 1 당 스킬 피해량 +3%\n\nE.G.O 스킬 ‘오혈읍루 - 종’ 발동 시, 공격 종료시 사망 효과가 발동하지 않고 최대 체력의 60% 회복. 다음 턴부터 매 턴 시작시마다 [AttackDmgUp] 1 얻음 (전투 당 1회)
   źródło: Passives.json :: dataList[id=1061301].desc
   limit: do 1080 znaków
   tokeny: zachowaj dokładnie: \n, [SupportProtect], [HeishouSupportProtect], [CondensedBlood], [AttackDmgUp], [TabExplain]
   znaczenie tagów: [SupportProtect] = 원호 방어 / Assist Defense; [HeishouSupportProtect] = 호위 / Lordsguard; [CondensedBlood] = 오혈 / Tarnished Blood; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Combat Start: If this unit did not equip a Defense Skill and is about to take an Unopposed Attack, apply 1 [HeishouSupportProtect] to (highest Reson. / 3) random Heishou Pack allies that have the least [SupportProtect] Stacks (max 2 allies; once per Identity; excludes Identities that have Skills that gain [SupportProtect])\n\nIn this Encounter, when this unit takes damage that brings their HP down to 0, nullify that damage; then, this unit's HP cannot drop below 1 for the turn, and it gains 1 [CondensedBlood] (once per Encounter)\n\nThis unit's Skills deal +3% damage for every [CondensedBlood] on self\n\nWhen activating the E.G.O Skill 'Tears[TabExplain] of the Tarnished Blood[TabExplain] - The End', nullify the death effect in its Attack End effects; instead, heal 60% HP. Starting next turn, gain 1 [AttackDmgUp] at every Turn Start (once per Encounter)
   PL: Na początku walki jeżeli nie wyposażyła Umiejętności obrony i jest celem nadchodzącego ataku nieopartego, nakłada 1 [HeishouSupportProtect] na (najwyższy Rezonans / 3) losowych sojuszniczych Watah Heishou z najmniejszą liczbą stosów [SupportProtect] (maks. 2 sojuszników; 1 raz na Tożsamość; wyłączając Tożsamości z Umiejętnościami zyskującymi [SupportProtect])\n\nW tym spotkaniu, gdy ta jednostka otrzymuje obrażenia redukujące HP do 0, unieważnia te obrażenia; jej HP nie spada poniżej 1 w tej turze i zyskuje 1 [CondensedBlood] (1 raz na spotkanie)\n\nUmiejętności tej jednostki zadają +3% obrażeń za każde 1 [CondensedBlood]\n\nPrzy uruchomieniu Umiejętności E.G.O „Łzy Splamionej Krwi - Kres” na koniec ataku efekt śmierci nie uruchamia się, zamiast tego odzyskuje 60% Maks. HP. Od następnej tury zyskuje 1 [AttackDmgUp] na początku każdej tury (1 raz na spotkanie)
553. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — podsumowanie] 체력이 0이 되는 피해를 받으면 사망하지 않고 [CondensedBlood] 얻음\n'오혈읍루-종' 발동 시 사망 효과를 무시하고 체력 회복, [AttackDmgUp] 얻음
   źródło: Passives.json :: dataList[id=1061301].summary
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [CondensedBlood], [AttackDmgUp], [TabExplain]
   znaczenie tagów: [CondensedBlood] = 오혈 / Tarnished Blood; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: When taking damage that brings this unit's HP to 0, nullify death, and gain [CondensedBlood]\nWhen activating 'Tears[TabExplain] of the Tarnished Blood[TabExplain]', nullify death, heal HP, and gain [AttackDmgUp]
   PL: Gdy otrzymuje obrażenia redukujące HP do 0, nie ginie i zyskuje [CondensedBlood]\nPrzy uruchomieniu „Łzy Splamionej Krwi - Kres” ignoruje efekt śmierci, odzyskuje HP i zyskuje [AttackDmgUp]
554. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Glut.) — nazwa] 꼬리는 밟히지 말고 처리해주세요.
   źródło: Passives.json :: dataList[id=1061321].name
   limit: do 50 znaków
   EN: Please be traceless in your deeds.
   PL: Nie zostawiaj śladów po swoich uczynkach.
555. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Glut.) — opis] 현재 체력 비율이 가장 낮은 인격이 적에게 가하는 피해량 +(대상이 보유한 주살 종류 x 3)% (최대 15%)
   źródło: Passives.json :: dataList[id=1061321].desc
   limit: do 170 znaków
   EN: Identity that has the least current HP percentage: Deal +(types of Deathrites on target x 3)% damage against the enemy (max 15%)
   PL: Tożsamość z najniższym procentem obecnego HP zadaje +(rodzaje Obrzędów Śmierci na celu x 3)% obrażeń wrogu (maks. 15%)

## [000] The House of Spiders: The Ring Nursefather — Hong Lu — 거미집 약지 아비
- ID Tożsamości: `10614` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 7 · HP bazowe: 66 · szybkość: 4–5 / 4–6 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Charge

556. [Karta Tożsamości — tytuł] 거미집\n약지 아비
   źródło: Personalities.json :: dataList[id=10614].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The House of Spiders:\nThe Ring Nursefather
   PL: Dom Pajęczyn:\nRingu Abi
557. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10614].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10614].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Karta Tożsamości — opis] 홍루의 열네번째 인격
   źródło: Personalities.json :: dataList[id=10614].desc
   limit: do 120 znaków
   EN: Hong Lu's 14th Identity
   PL: Czternasta Tożsamość Hong Lu
560. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 해체
   źródło: Skills_personality-06.json :: dataList[id=1061401].levelList[level=1].name ; dataList[id=1061401].levelList[level=2].name ; dataList[id=1061401].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Anatomize
   PL: Anatomizacja
561. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]
562. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061401].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1061401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown] next turn (once per turn)
   PL: [OnSucceedAttack] Nakłada w następnej turze 2 [DefenseDown] (1 raz na turę)
563. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseUp] 2 얻음 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061401].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1061401].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1061401].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 2 [DefenseUp] next turn (once per turn)
   PL: [OnSucceedAttack] Zyskuje w następnej turze 2 [DefenseUp] (1 raz na turę)
564. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 부정적인 효과 1개당, 피해량 +5% (최대 20%)\n[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 2)
   źródło: Skills_personality-06.json :: dataList[id=1061401].levelList[level=2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: Deal +5% damage for every type of negative effect on target (max 20%)\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)
   PL: Zadaje +5% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 20%)\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] celu (maks. 2)
565. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-06.json :: dataList[id=1061401].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] Nakłada 3 [Laceration]
566. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 부정적인 효과 1개당, 피해량 +<style="highlight">10</style>% (최대 <style="highlight">30</style>%)\n[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 <style="highlight">3</style>)
   źródło: Skills_personality-06.json :: dataList[id=1061401].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: Deal +<style="highlight">10</style>% damage for every type of negative effect on target (max <style="highlight">30</style>%)\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max <style="highlight">3</style>)
   PL: Zadaje <style="highlight">+10</style>% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. <style="highlight">30</style>%)\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] celu (maks. <style="highlight">3</style>)
567. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_personality-06.json :: dataList[id=1061401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] Nakłada 4 [Laceration]
568. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 재료획득 - 피로 목욕하는 오브제
   źródło: Skills_personality-06.json :: dataList[id=1061402].levelList[level=1].name ; dataList[id=1061402].levelList[level=2].name ; dataList[id=1061402].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 60 znaków
   EN: Gather Ingredient - Blood-bathed Objet
   PL: Zdobądź Składnik - Przedmiot Kąpiący się we Krwi
569. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 5 소모하고 아래 효과 적용\n- 합 위력 +1\n- 마지막 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-06.json :: dataList[id=1061402].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] At 10+ [ChargeBodyArt] Count, consume 5 [ChargeBodyArt] Count to gain the following effects:\n- Clash Power +1\n- Convert the final Coin on this Skill to [SuperCoin]
   PL: [WhenUse] Przy 10+ Licznika [ChargeBodyArt] zużywa 5 Licznika [ChargeBodyArt], aby stosować poniższe efekty:\n- Moc Starcia +1\n- Ostatnia moneta tej Umiejętności staje się [SuperCoin]
570. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Laceration]
571. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061402].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1061402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn (once per turn)
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [Binding] (1 raz na turę)
572. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061402].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1061402].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1061402].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 1 [Agility] next turn (once per turn)
   PL: [OnSucceedAttack] Zyskuje w następnej turze 1 [Agility] (1 raz na turę)
573. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeBodyArt] 횟수 4 증가
   źródło: Skills_personality-06.json :: dataList[id=1061402].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1061402].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1061402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeBodyArt]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient
   EN: [OnSucceedAttack] Gain +4 [ChargeBodyArt] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeBodyArt] o 4
574. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 부정적인 효과가 5개 이상이면, 대상에게 ‘설치 미술 제 3호 ‘간이늑골’’ 사용 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061402].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1061402].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1061402].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has 5+ types of negative effects, use "Installation Art no. 3: Improvised Ribcage" Skill against the target (once per turn)
   PL: [OnSucceedAttack] Jeżeli cel ma 5+ rodzajów negatywnych efektów, używa na celu Umiejętności „Sztuka Instalacji nr 3: Improwizowana Klatka Piersiowa” (1 raz na turę)
575. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">대상의 부정적인 효과 1개당, 피해량 +5% (최대 20%)</style>\n<style="highlight">[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 5 소모하고 아래 효과 적용\n- 합 위력 +1\n- 마지막 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-06.json :: dataList[id=1061402].levelList[level=2].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: <style="highlight">Deal +5% damage for every type of negative effect on target (max 20%)</style>\n<style="highlight">[WhenUse] Final Power +1 for every 4 [Laceration] on target (max 2)</style>\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume 5 [ChargeBodyArt] Count to gain the following effects:\n- Clash Power +1\n- Convert the final Coin on this Skill to [SuperCoin]
   PL: <style="highlight">Zadaje +5% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 20%)</style>\n<style="highlight">[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] celu (maks. 2)</style>\n[WhenUse] Przy 10+ Licznika [ChargeBodyArt] zużywa 5 Licznika [ChargeBodyArt], aby stosować poniższe efekty:\n- Moc Starcia +1\n- Ostatnia moneta tej Umiejętności staje się [SuperCoin]
576. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1061402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Laceration] celu o 2
577. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 부정적인 효과 1개당, 피해량 +<style="highlight">10</style>% (최대 <style="highlight">30</style>%)\n[WhenUse] 대상의 [Laceration] 4당, 최종 위력 +1 (최대 <style="highlight">4</style>)\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 5 소모하고 아래 효과 적용\n- 합 위력 +1\n- 마지막 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-06.json :: dataList[id=1061402].levelList[level=4].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Deal +<style="highlight">10</style>% damage for every type of negative effect on target (max <style="highlight">30</style>%)\n[WhenUse] Final Power +1 for every 4 [Laceration] on target (max <style="highlight">4</style>)\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume 5 [ChargeBodyArt] Count to gain the following effects:\n- Clash Power +1\n- Convert the final Coin on this Skill to [SuperCoin]
   PL: Zadaje <style="highlight">+10</style>% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. <style="highlight">30</style>%)\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] celu (maks. <style="highlight">4</style>)\n[WhenUse] Przy 10+ Licznika [ChargeBodyArt] zużywa 5 Licznika [ChargeBodyArt], aby stosować poniższe efekty:\n- Moc Starcia +1\n- Ostatnia moneta tej Umiejętności staje się [SuperCoin]
578. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 티비아의 멜로디 - 해체된 것이 해체되지 않은 것을 해체하는 것
   źródło: Skills_personality-06.json :: dataList[id=1061403].levelList[level=3].name ; dataList[id=1061403].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 90 znaków
   EN: Tibia's Melody - Anatomization of the Unanatomized by the Anatomized
   PL: Melodia Kości Piszczelowej - Anatomizacja Nzanatomizowanego przez Anatomizowane
579. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당, 피해량 +30% (집중 전투인 경우, 부위로 판정)\n[WhenUse] 메인 타겟의 [Laceration] 4당, 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 최대 20까지 소모하고 아래 효과 적용\n- 최종 위력 +2\n- 소모한 수치 1당, 피해량 +1%\n- [ChargeBodyArt]가 3/5 이상이면, 공격 가중치 +1/+2\n- 모든 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-06.json :: dataList[id=1061403].levelList[level=3].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Deal +30% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Part)\n[WhenUse] Final Power +1 for every 4 [Laceration] on the main target (max 2)\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume up to 20 [ChargeBodyArt] Count and gain the following effects:\n- Final Power +2\n- Deal +1% damage for every [ChargeBodyArt] Count consumed\n- At 3+/5+ [ChargeBodyArt], gain +1/+2 Atk Weight\n- Convert all Coins on this Skill to [SuperCoin]s
   PL: [WhenUse] Zadaje +30% obrażeń za każdego nadmiarowego celu ataku poza Wagą ataku tej Umiejętności (w walkach skupionych sądzi się w Partach)\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] głównego celu (maks. 2)\n[WhenUse] Przy 10+ Licznika [ChargeBodyArt] zużywa do 20 Licznika [ChargeBodyArt], aby stosować poniższe efekty:\n- Moc Końcowa +2\n- Zadaje +1% obrażeń za każde zużyte 1 Licznika [ChargeBodyArt]\n- Przy 3+/5+ [ChargeBodyArt] Waga ataku +1/+2\n- Wszystkie monety tej Umiejętności stają się [SuperCoin]ami
580. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-06.json :: dataList[id=1061403].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061403].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1061403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 571 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061403].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1061403].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 572 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061403].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1061403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDmgDown] next turn (once per turn)
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [AttackDmgDown] (1 raz na turę)
584. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [SlashDamageUp] 1 얻음 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061403].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1061403].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: [OnSucceedAttack] Gain 1 [SlashDamageUp] next turn (once per turn)
   PL: [OnSucceedAttack] Zyskuje w następnej turze 1 [SlashDamageUp] (1 raz na turę)
585. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] 대상의 부정적인 효과 1개당, 피해량 +5% (최대 30%)
   źródło: Skills_personality-06.json :: dataList[id=1061403].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1061403].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +5% damage for every type of negative effect on target (max 30%)
   PL: Zadaje +5% obrażeń za każdy 1 rodzaj negatywnych efektów na celu (maks. 30%)
586. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061403].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1061403].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 570 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당, 피해량 +30% (집중 전투인 경우, 부위로 판정)\n[WhenUse] 메인 타겟의 [Laceration] 4당, 최종 위력 +1 (최대 <style="highlight">3</style>)\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 최대 20까지 소모하고 아래 효과 적용\n- 최종 위력 +2\n- 소모한 수치 1당, 피해량 +1%\n- [ChargeBodyArt]가 3/5 이상이면, 공격 가중치 +1/+2\n- 모든 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-06.json :: dataList[id=1061403].levelList[level=4].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Deal +30% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Part)\n[WhenUse] Final Power +1 for every 4 [Laceration] on the main target (max <style="highlight">3</style>)\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume up to 20 [ChargeBodyArt] Count and gain the following effects:\n- Final Power +2\n- Deal +1% damage for every [ChargeBodyArt] Count consumed\n- At 3+/5+ [ChargeBodyArt], gain +1/+2 Atk Weight\n- Convert all Coins on this Skill to [SuperCoin]s
   PL: [WhenUse] Zadaje +30% obrażeń za każdego nadmiarowego celu ataku poza Wagą ataku tej Umiejętności (w walkach skupionych sądzi się w Partach)\n[WhenUse] Moc Końcowa +1 za każde 4 [Laceration] głównego celu (maks. <style="highlight">3</style>)\n[WhenUse] Przy 10+ Licznika [ChargeBodyArt] zużywa do 20 Licznika [ChargeBodyArt], aby stosować poniższe efekty:\n- Moc Końcowa +2\n- Zadaje +1% obrażeń za każde zużyte 1 Licznika [ChargeBodyArt]\n- Przy 3+/5+ [ChargeBodyArt] Waga ataku +1/+2\n- Wszystkie monety tej Umiejętności stają się [SuperCoin]ami
588. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_personality-06.json :: dataList[id=1061403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Umiejętność 4 (×0) (ulepszenia 2,4) — nazwa] 우린 피와 살을 사랑한답니다
   źródło: Skills_personality-06.json :: dataList[id=1061405].levelList[level=2].name ; dataList[id=1061405].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 1 (+4)
   limit: do 60 znaków
   EN: My, How We Love the Flesh and the Blood
   PL: O, Jak Uwielbiamy Ciało i Krew
590. [Umiejętność 4 (×0) (ulepszenie 2) — opis] [CantIdentify]\n[CantDuel]\n이 스킬은 아래 효과가 적용됨\n- 수비 스킬을 발동시키지 않음\n- 외부 효과로 재사용 할 수 없음\n- 공격이 적중하지 않음\n[WhenUse] 대상에게 [AttackUp] 4 부여
   źródło: Skills_personality-06.json :: dataList[id=1061405].levelList[level=2].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [CantDuel], [WhenUse], [AttackUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CantIdentify]\n[CantDuel]\nThis Skill has the following properties:\n- Does not trigger Defense Skills\n- External effects cannot trigger this Skill to be Reused\n- Its attack does not hit\n[WhenUse] Apply 4 [AttackUp] on target
   PL: [CantIdentify]\n[CantDuel]\nTa Umiejętność ma następujące własności:\n- Nie uruchamia Umiejętności obrony\n- Zewnętrzne efekty nie mogą ponownie użyć tej Umiejętności\n- Jej atak nie trafia\n[WhenUse] Nakłada 4 [AttackUp] na cel
591. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [CantIdentify]\n[CantDuel]\n이 스킬은 아래 효과가 적용됨\n- 수비 스킬을 발동시키지 않음\n- 외부 효과로 재사용 할 수 없음\n- 공격이 적중하지 않음\n[WhenUse] 대상에게 [AttackUp] 6 부여
   źródło: Skills_personality-06.json :: dataList[id=1061405].levelList[level=4].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [CantDuel], [WhenUse], [AttackUp]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [CantIdentify]\n[CantDuel]\nThis Skill has the following properties:\n- Does not trigger Defense Skills\n- External effects cannot trigger this Skill to be Reused\n- Its attack does not hit\n[WhenUse] Apply 6 [AttackUp] on target
   PL: [CantIdentify]\n[CantDuel]\nTa Umiejętność ma następujące własności:\n- Nie uruchamia Umiejętności obrony\n- Zewnętrzne efekty nie mogą ponownie użyć tej Umiejętności\n- Jej atak nie trafia\n[WhenUse] Nakłada 6 [AttackUp] na cel
592. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — nazwa] 설치 미술 제 3호 ‘간이늑골’
   źródło: Skills_personality-06.json :: dataList[id=1061408].levelList[level=1].name ; dataList[id=1061408].levelList[level=2].name ; dataList[id=1061408].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 5 · monety: 2 (+4)
   limit: do 60 znaków
   EN: Installation Art no. 3: Improvised Ribcage
   PL: Sztuka Instalacji nr 3: Improwizowana Klatka Piersiowa
593. [Umiejętność 5 (×0) (ulepszenia 1,2,4) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않음\n[WhenUse] 자신의 [ChargeBodyArt] 횟수 4 소모
   źródło: Skills_personality-06.json :: dataList[id=1061408].levelList[level=1].desc ; dataList[id=1061408].levelList[level=2].desc ; dataList[id=1061408].levelList[level=4].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [ChargeBodyArt]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills\n[WhenUse] Consume 4 [ChargeBodyArt] Count
   PL: [CantDuel]\nTa Umiejętność nie uruchamia Umiejętności obrony\n[WhenUse] Zużywa 4 Licznika [ChargeBodyArt]
594. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 정신력 피해 5
   źródło: Skills_personality-06.json :: dataList[id=1061408].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 SP damage
   PL: [OnSucceedAttack] Zadaje 5 obrażeń Poczytalności
595. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 정신력 5 회복
   źródło: Skills_personality-06.json :: dataList[id=1061408].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 5 SP on self
   PL: [OnSucceedAttack] Odzyskuje 5 Poczytalności
596. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [LivingSpecimenPersonality] 부여
   źródło: Skills_personality-06.json :: dataList[id=1061408].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [LivingSpecimenPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LivingSpecimenPersonality] = 신체관극 / Corpus Theater
   EN: [OnSucceedAttack] Inflict [LivingSpecimenPersonality]
   PL: [OnSucceedAttack] Nakłada [LivingSpecimenPersonality]
597. [Umiejętność 5 (×0) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061408].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]
598. [Umiejętność 5 (×0) (ulepszenie 2) — moneta 2, efekt 1 — opis] 대상의 부정적인 효과 1개당, 피해량 +5% (최대 20%)
   źródło: Skills_personality-06.json :: dataList[id=1061408].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +5% damage for every type of negative effect on target (max 20%)
   PL: Zadaje +5% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 20%)
599. [Umiejętność 5 (×0) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 정신력 피해 5<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061408].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1061408].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 SP damage<style="highlight"></style>
   PL: [OnSucceedAttack] Zadaje 5 obrażeń Poczytalności<style="highlight"></style>
600. [Umiejętność 5 (×0) (ulepszenia 2,4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 정신력 5 회복<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061408].levelList[level=2].coinlist[#1].coindescs[#2].desc ; dataList[id=1061408].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 5 SP on self<style="highlight"></style>
   PL: [OnSucceedAttack] Odzyskuje 5 Poczytalności<style="highlight"></style>
601. [Umiejętność 5 (×0) (ulepszenia 2,4) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [LivingSpecimenPersonality] 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061408].levelList[level=2].coinlist[#1].coindescs[#3].desc ; dataList[id=1061408].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [LivingSpecimenPersonality]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LivingSpecimenPersonality] = 신체관극 / Corpus Theater
   EN: [OnSucceedAttack] Inflict [LivingSpecimenPersonality]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada [LivingSpecimenPersonality]<style="highlight"></style>
602. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061408].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] 대상의 부정적인 효과 1개당, 피해량 +<style="highlight">10</style>% (최대 <style="highlight">50</style>%)
   źródło: Skills_personality-06.json :: dataList[id=1061408].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal +<style="highlight">10</style>% damage for every type of negative effect on target (max <style="highlight">50</style>%)
   PL: Zadaje <style="highlight">+10</style>% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. <style="highlight">50</style>%)
604. [Umiejętność 6 (×0) (ulepszenia 3–4) — nazwa] 폐장 - 설치미술 제 1호 ‘여러분이 흩뿌린 살과 뼈가 객석이 되어’
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].name ; dataList[id=1061406].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 5 (+4)
   limit: do 110 znaków
   EN: Closing Time - Installation Art no. 1: Your Flesh and Bones as the Gallery's Seats
   PL: Końcowa Godzina - Sztuka Instalacji nr 1: Twoje Ciało i Kości jako Fotele Galerii
605. [Umiejętność 6 (×0) (ulepszenia 3–4) — opis] [WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당, 피해량 +30% (집중 전투인 경우, 부위로 판정)\n- 공격 대상이 1이면, 추가로 피해량 +100%\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 최대 20까지 소모하고 아래 효과 적용\n- 최종 위력 +2\n- 소모한 수치 1당, 피해량 +1%\n- [ChargeBodyArt]가 3/5 이상이면, 공격 가중치 +1/+2\n[EndSkill] 약지 소속 인격의 정신력을 10 회복하고, 해당 아군에게 [MelodyBodyArt] 부여
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].desc ; dataList[id=1061406].levelList[level=4].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeBodyArt], [EndSkill], [MelodyBodyArt]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [EndSkill] = [공격 종료시] / [Attack End]; [MelodyBodyArt] = 신체가 울리는 선율 / Somatic Frisson-inspiring Melody
   EN: [WhenUse] Deal +30% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Part)\n- When attacking just 1 target, deal +100% additional damage\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume up to 20 [ChargeBodyArt] Count and gain the following effects:\n- Final Power +2\n- Deal +1% damage for every [ChargeBodyArt] Count consumed\n- At 3+/5+ [ChargeBodyArt], gain +1/+2 Atk Weight\n[EndSkill] For all Identities in The Ring faction, heal 10 SP and apply [MelodyBodyArt]
   PL: [WhenUse] Zadaje +30% obrażeń za każdego nadmiarowego celu ataku poza Wagą ataku tej Umiejętności (w walkach skupionych sądzi się w Partach)\n- Przy ataku na jednego celu zadaje dodatkowo +100% obrażeń\n[WhenUse] Przy 10+ Licznika [ChargeBodyArt] zużywa do 20 Licznika [ChargeBodyArt], aby stosować poniższe efekty:\n- Moc Końcowa +2\n- Zadaje +1% obrażeń za każde zużyte 1 Licznika [ChargeBodyArt]\n- Przy 3+/5+ [ChargeBodyArt] Waga ataku +1/+2\n[EndSkill] Odzyskuje 10 Poczytalności dla Tożsamości frakcji Ringu i nakłada na nich [MelodyBodyArt]
606. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1061406].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1061406].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1061406].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 571 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=1061406].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 572 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1061406].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1061406].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [SlashDamageUp] 1 얻음 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1061406].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#3].coindescs[#0].desc ; dataList[id=1061406].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#3].coindescs[#1].desc ; dataList[id=1061406].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 570 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#4].coindescs[#0].desc ; dataList[id=1061406].levelList[level=4].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 5, efekt 2 — opis] 대상의 부정적인 효과 1개당, 피해량 +5% (최대 30%)
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#4].coindescs[#1].desc ; dataList[id=1061406].levelList[level=4].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 5, efekt 3 — opis] [OnSucceedAttack] [Combustion] 5 부여
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#4].coindescs[#2].desc ; dataList[id=1061406].levelList[level=4].coinlist[#4].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion]
   PL: [OnSucceedAttack] Nakłada 5 [Combustion]
619. [Umiejętność 6 (×0) (ulepszenia 3–4) — moneta 5, efekt 4 — opis] [OnSucceedAttack] [LivingSpecimenPersonality] 부여
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=3].coinlist[#4].coindescs[#3].desc ; dataList[id=1061406].levelList[level=4].coinlist[#4].coindescs[#3].desc
   (powtórzenie elementu 596 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Umiejętność 6 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-06.json :: dataList[id=1061406].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Obrona (ulepszenia 1,4) — nazwa] 전시회 주최
   źródło: Skills_personality-06.json :: dataList[id=1061404].levelList[level=1].name ; dataList[id=1061404].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Curating the Exhibition
   PL: Prowadzenie Wystawy
622. [Obrona (ulepszenie 1) — opis] [StartBattle] [SupportProtect] 1 얻음 (턴당 1회)\n[OnSucceedEvade] 공격자에게 다음 턴에 [Binding] 1 부여 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061404].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SupportProtect], [OnSucceedEvade], [Binding]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Binding] = 속박 / Bind
   EN: [StartBattle] Gain 1 [SupportProtect] (once per turn)\n[OnSucceedEvade] Inflict 1 [Binding] next turn against the attacker (once per turn)
   PL: [StartBattle] Zyskuje 1 [SupportProtect] (1 raz na turę)\n[OnSucceedEvade] Nakłada w następnej turze 1 [Binding] na atakującego (1 raz na turę)
623. [Obrona (ulepszenie 4) — opis] [StartBattle] [SupportProtect] 1 얻음 (턴당 1회)\n[OnSucceedEvade] 공격자에게 다음 턴에 [Binding] 1 부여 (턴당 1회)\n[OnSucceedEvade] 다음 턴에 [Agility] 1 얻음 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061404].levelList[level=4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SupportProtect], [OnSucceedEvade], [Binding], [Agility]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Binding] = 속박 / Bind; [Agility] = 신속 / Haste
   EN: [StartBattle] Gain 1 [SupportProtect] (once per turn)\n[OnSucceedEvade] Inflict 1 [Binding] next turn against the attacker (once per turn)\n[OnSucceedEvade] Gain 1 [Agility] next turn (once per turn)
   PL: [StartBattle] Zyskuje 1 [SupportProtect] (1 raz na turę)\n[OnSucceedEvade] Nakłada w następnej turze 1 [Binding] na atakującego (1 raz na turę)\n[OnSucceedEvade] Zyskuje 1 [Agility] w następnej turze (1 raz na turę)
624. [Obrona (ulepszenia 1,4) — nazwa] 반달리즘은 사절이랍니다
   źródło: Skills_personality-06.json :: dataList[id=1061407].levelList[level=1].name ; dataList[id=1061407].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 4 · monety: 2 (+4)
   limit: do 50 znaków
   EN: Please. Vandalism is Prohibited.
   PL: Prosimy. Wandalizm jest Wzbroniony.
625. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[SupportProtect] 전용 스킬\n대상의 부정적인 효과 1개당, 피해량 +5% (최대 20%)\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 5 소모하고 아래 효과 적용\n- 합 위력 +1\n- 마지막 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-06.json :: dataList[id=1061407].levelList[level=1].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [SupportProtect], [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [DuelCounter]\n[SupportProtect] exclusive Skill\nDeal +5% damage for every type of negative effect on target (max 20%)\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume 5 [ChargeBodyArt] Count to gain the following effects:\n- Clash Power +1\n- Convert the final Coin on this Skill to [SuperCoin]
   PL: [DuelCounter]\nUmiejętność wyłącznie dla [SupportProtect]\nZadaje +5% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. 20%)\n[WhenUse] Jeżeli cel ma 6+ [Laceration], Moc Monet +1\n[WhenUse] Przy 10+ Licznika [ChargeBodyArt] zużywa 5 Licznika [ChargeBodyArt], aby stosować poniższe efekty:\n- Moc Starcia +1\n- Ostatnia moneta tej Umiejętności staje się [SuperCoin]
626. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061407].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1061407].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 570 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[SupportProtect] 전용 스킬\n대상의 부정적인 효과 1개당, 피해량 +<style="highlight">10</style>% (최대 <style="highlight">30</style>%)\n[WhenUse] 대상의 [Laceration] 6<style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [ChargeBodyArt] 횟수가 10 이상이면, [ChargeBodyArt] 횟수를 5 소모하고 아래 효과 적용\n- 합 위력 +1\n- 마지막 코인이 [SuperCoin]이 됨
   źródło: Skills_personality-06.json :: dataList[id=1061407].levelList[level=4].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [SupportProtect], [WhenUse], [Laceration], [ChargeBodyArt], [SuperCoin]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [DuelCounter]\n[SupportProtect] exclusive Skill\nDeal +<style="highlight">10</style>% damage for every type of negative effect on target (max <style="highlight">30</style>%)\n[WhenUse] <style="highlight">Coin Power +1 for every 6 [Laceration] on target (max 2)</style>\n[WhenUse] At 10+ [ChargeBodyArt] Count, consume 5 [ChargeBodyArt] Count to gain the following effects:\n- Clash Power +1\n- Convert the final Coin on this Skill to [SuperCoin]
   PL: [DuelCounter]\nUmiejętność wyłącznie dla [SupportProtect]\nZadaje <style="highlight">+10</style>% obrażeń za każdy 1 rodzaj negatywnego efektu na celu (maks. <style="highlight">30</style>%)\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 [Laceration] celu (maks. 2)</style>\n[WhenUse] Przy 10+ Licznika [ChargeBodyArt] zużywa 5 Licznika [ChargeBodyArt], aby stosować poniższe efekty:\n- Moc Starcia +1\n- Ostatnia moneta tej Umiejętności staje się [SuperCoin]
628. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061407].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Pasywka bojowa (od ulepszenia 1) — nazwa] 일생의 작품 티비아
   źródło: Passives.json :: dataList[id=1061404].name
   limit: do 40 znaków
   EN: Magnum Opus: Tibia
   PL: Magnum Opus: Kość Piszczelowa
630. [Pasywka bojowa (od ulepszenia 1) — opis] 스테이지 첫 등장 시 자신의 [ChargeBodyArt] 횟수가 (전장에 있는 약지 소속 아군 수 x 2)만큼 증가 (최대 10)\n\n스킬 종료 시 해당 스킬로 체력 또는 보호막 피해를 입혔으면, 자신의 [ChargeBodyArt] 횟수 5 증가\n- 대상이 사망했으면, 추가로 횟수 3 증가\n\n전투 중 누적으로 자신의 [ChargeBodyArt] 횟수 10을 소모할 때마다 [ChargeBodyArt]를 1 얻음\n- 위 효과로 [ChargeBodyArt] 위력이 2 이상이 되면, [TibiaPersonality] 얻음\n\n기본 공격 스킬과 합 가능 반격 스킬이 [Charge] 횟수를 얻는 스킬로 취급됨
   źródło: Passives.json :: dataList[id=1061404].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeBodyArt], [TibiaPersonality], [Charge]
   znaczenie tagów: [ChargeBodyArt] = 생체 재료 / Corpus Ingredient; [TibiaPersonality] = 작품명: 티비아 / Artwork: Tibia; [Charge] = 충전 / Charge
   EN: Upon entering the Encounter for the first time, gain +(# of The Ring allies on the field x 2) [ChargeBodyArt] Count (max 10)\n\nSkill End: If the Skill dealt HP or Shield damage, gain +5 [ChargeBodyArt] Count\n- If target is killed, gain +3 additional [ChargeBodyArt] Count\n\nGain 1 [ChargeBodyArt] every time this unit consumes 10 cumulative [ChargeBodyArt] Count in this Encounter\n- If the above effect brings this unit's [ChargeBodyArt] Potency to 2 or higher, gain [TibiaPersonality]\n\nBase Attack Skills and Clashable Counter Skill count as Skills that gain [Charge] Count
   PL: Przy pierwszym pojawieniu się na polu zyskuje +2 Licznika [ChargeBodyArt] za każdego sojusznika frakcji Ringu na polu (maks. 10)\n\nNa koniec Umiejętności: jeżeli ta Umiejętność zadała obrażenia HP lub Tarczy, zyskuje +5 Licznika [ChargeBodyArt]\n- Jeżeli cel zginął, zyskuje dodatkowo +3 Licznika [ChargeBodyArt]\n\nZa każde łączne zużycie 10 własnego Licznika [ChargeBodyArt] podczas walki zyskuje 1 [ChargeBodyArt]\n- Jeżeli powyższy efekt podniesie Moc [ChargeBodyArt] do 2 lub wyżej, zyskuje [TibiaPersonality]\n\nPodstawowe Umiejętności ataku oraz Umiejętność Kontry mogącej stoczyć starcie liczą się jako Umiejętności zyskujące Licznik [Charge]
631. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] [ChargeBodyArt] 얻음
   źródło: Passives.json :: dataList[id=1061404].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ChargeBodyArt]
   znaczenie tagów: [ChargeBodyArt] = 생체 재료 / Corpus Ingredient
   EN: Gain [ChargeBodyArt]
   PL: Zyskuje [ChargeBodyArt]
632. [Pasywka bojowa (od ulepszenia 1) — nazwa] 신체극복
   źródło: Passives.json :: dataList[id=1061405].name
   limit: do 40 znaków
   EN: Transcend the Corpus
   PL: Przekroczenie Ciała
633. [Pasywka bojowa (od ulepszenia 1) — opis] 스테이지에 첫 등장 시 [GoldenOpportunity] 21 얻음\n\n약지 소속 아군 인격이 스킬 사용 시 [GoldenOpportunity] 1 감소 (인격별 턴당 1회)\n\n턴 종료 시 자신에게 [GoldenOpportunity]이 없으면, 다음 턴 시작 시 기본 스킬 하나를 ‘폐장 - 설치미술 제 1호 ‘여러분이 흩뿌린 살과 뼈가 객석이 되어’’로 변경 (전투당 1회, 가장 왼쪽 슬롯의 아래 스킬 우선 적용)\n- 변경된 스킬이 다른 스킬로 변경되어 사용할 수 없게 되면, 위 효과를 다시 발동함\n\n턴 종료 시 이번 전투에서 처음으로 흐트러졌으면, 흐트러짐 해제 (강제 흐트러짐 제외)
   źródło: Passives.json :: dataList[id=1061405].desc
   limit: do 910 znaków
   tokeny: zachowaj dokładnie: \n, [GoldenOpportunity]
   znaczenie tagów: [GoldenOpportunity] = 조망 / Viewing the Tableau
   EN: Upon entering the Encounter for the first time, gain 21 [GoldenOpportunity]\n\nWhen The Ring-faction allied Identities use a Skill, lose 1 [GoldenOpportunity] (once per turn per Identity)\n\nTurn End: If this unit does not have [GoldenOpportunity], replace one of its Base Skills with "Closing Time - Installation Art no. 1: Your Flesh and Bones as the Gallery's Seats" at next Turn Start (once per Encounter; Prioritizes the Skill on the leftmost Slot's bottom row on the Dashboard)\n- If the replaced Skill becomes inaccessible due to being replaced by a different Skill, activate the above effect again\n\nTurn End: If this unit was Staggered for the first time in this Encounter, recover from Stagger (excluding forced Stagger)
   PL: Przy pierwszym pojawieniu się na polu zyskuje 21 [GoldenOpportunity]\n\nGdy sojusznicze Tożsamości frakcji Ringu używają Umiejętności, traci 1 [GoldenOpportunity] (1 raz na turę per Tożsamość)\n\nNa koniec tury, jeżeli nie ma [GoldenOpportunity], na początku następnej tury podstawowa Umiejętność zostaje zamieniona na „Końcowa Godzina - Sztuka Instalacji nr 1: Twoje Ciało i Kości jako Fotele Galerii” (1 raz na spotkanie; najpierw Umiejętność lewego dolnego pola slotu po lewej stronie panelu)\n- Jeżeli zamieniona Umiejętność stanie się niedostępna, bo została zamieniona na inną, ponownie uruchamia powyższy efekt\n\nNa koniec tury, jeżeli po raz pierwszy w tym spotkaniu została Ogłuszona, doszodzi z Ogłuszenia (z wyłączeniem wymuszonego Ogłuszenia)
634. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 흐트러짐 해제
   źródło: Passives.json :: dataList[id=1061405].summary
   limit: do 120 znaków
   EN: Recover from Stagger
   PL: Dojdzenie z Ogłuszenia
635. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — nazwa] 마에스트로의 크리틱
   źródło: Passives.json :: dataList[id=1061401].name
   limit: do 40 znaków
   EN: A Maestro's Critique
   PL: Krytyka Maestra
636. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — opis] 거미집 약지 제자 파우스트가 스킬 3(E.G.O 스킬 제외)을 사용하기 전 거미집 약지 아비 홍루가 ‘우린 피와 살을 사랑한답니다’를 파우스트에게 사용함 (턴당 1회)\n\n공격 적중 시 해당 공격 스킬로 부정적인 효과를 부여했으면, 공격 종료 시 자신의 정신력 4 회복 (턴당 3회)
   źródło: Passives.json :: dataList[id=1061401].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Before The House of Spiders: The Ring Apprentice Faust uses its Skill 3(except E.G.O Skills), The House of Spiders: The Ring Nursefather Hong Lu uses "My, How We Love the Flesh and the Blood" on Faust (once per turn)\n\nOn Hit, if the Attack Skill inflicted a negative effect, heal 4 SP at Attack End (3 times per turn)
   PL: Zanim Apprentis Ringu Faust użyje Umiejętności 3 (poza Umiejętnościami E.G.O), Abi Ringu Hong Lu używa na niej „O, Jak Uwielbiamy Ciało i Krew” (1 raz na turę)\n\nPrzy trafieniu, jeżeli Umiejętność ataku nakłada negatywny efekt, odzyskuje 4 Poczytalności na koniec ataku (3 razy na turę)
637. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Lust) — podsumowanie] 자신의 정신력 회복
   źródło: Passives.json :: dataList[id=1061401].summary
   limit: do 120 znaków
   EN: Heal SP on self
   PL: Odzyskuje Poczytalność
638. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — nazwa] 마에스트로의 크리틱
   źródło: Passives.json :: dataList[id=1061411].name
   (powtórzenie elementu 635 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — opis] 거미집 약지 제자 파우스트가 스킬 3(E.G.O 스킬 제외)을 사용하기 전 거미집 약지 아비 홍루가 ‘우린 피와 살을 사랑한답니다’를 파우스트에게 사용함 (턴당 1회)\n\n공격 적중 시 해당 공격 스킬로 부정적인 효과를 부여했으면, 공격 종료 시 자신의 정신력 4 회복 (턴당 3회)\n- 이 효과로 정신력 회복 시 자신의 정신력이 최대면, 다음 턴에 [SlashDamageUp] 1 얻음 (턴당 1회)
   źródło: Passives.json :: dataList[id=1061411].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [SlashDamageUp]
   znaczenie tagów: [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: Before The House of Spiders: The Ring Apprentice Faust uses its Skill 3(except E.G.O Skills), The House of Spiders: The Ring Nursefather Hong Lu uses "My, How We Love the Flesh and the Blood" on Faust (once per turn)\n\nOn Hit, if the Attack Skill inflicted a negative effect, heal 4 SP at Attack End (3 times per turn)\n- If this unit's SP is at max, gain 1 [SlashDamageUp] next turn when this unit heals SP with this effect (once per turn)
   PL: Zanim Apprentis Ringu Faust użyje Umiejętności 3 (poza Umiejętnościami E.G.O), Abi Ringu Hong Lu używa na niej „O, Jak Uwielbiamy Ciało i Krew” (1 raz na turę)\n\nPrzy trafieniu, jeżeli Umiejętność ataku nakłada negatywny efekt, odzyskuje 4 Poczytalności na koniec ataku (3 razy na turę)\n- Jeżeli Poczytalność jest na maksimum w momencie tego odzysku, zyskuje 1 [SlashDamageUp] w następnej turze (1 raz na turę)
640. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Lust) — podsumowanie] 자신의 정신력 회복\n조건 만족 시 다음 턴에 [SlashDamageUp] 얻음
   źródło: Passives.json :: dataList[id=1061411].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [SlashDamageUp]
   znaczenie tagów: [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: Heal SP on self\nGain [SlashDamageUp] next turn if conditions are met
   PL: Odzyskuje Poczytalność\nWarunkowo zyskuje w następnej turze [SlashDamageUp]
641. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — nazwa] 뛰어다니는 관객은 의자에 앉아 감상하시죠
   źródło: Passives.json :: dataList[id=1061421].name
   limit: do 60 znaków
   EN: Please, Do Stop Running and Be Seated
   PL: Prosimy, Przestańcie Biegać i Zasiądźcie na Fotelach
642. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — opis] 턴 종료 시 속도가 가장 빠른 적 1명에게 다음 턴에 [AttackDown] 2 부여하고 [Laceration] 횟수 1 증가 (집중 전투일 경우, 부위로 판정)
   źródło: Passives.json :: dataList[id=1061421].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [AttackDown], [Laceration]
   znaczenie tagów: [AttackDown] = 공격 레벨 감소 / Offense Level Down; [Laceration] = 출혈 / Bleed
   EN: Turn End: Inflict 2 [AttackDown] and +1 [Laceration] Count next turn on 1 enemy with the fastest Speed (in Focused Encounters, the Part)
   PL: Na koniec tury nakłada w następnej turze 2 [AttackDown] i zwiększa Licznik [Laceration] o 1 na 1 wrogu z najwyższą Szybkością (w walkach skupionych sądzi się w Partach)

## [000] S Corp. Ch'unokkun — Hong Lu — S사 추노꾼
- ID Tożsamości: `10615` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 7 · HP bazowe: 84 · szybkość: 3–5 / 4–5 / 4–6 / 4–6
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Bleed, Poise

643. [Karta Tożsamości — tytuł] S사 추노꾼
   źródło: Personalities.json :: dataList[id=10615].title
   limit: do 40 znaków
   EN: S Corp. Ch'unokkun
   PL: Łowca S Corp. Ch'unokkun
644. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10615].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10615].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Karta Tożsamości — opis] 홍루의 열다섯번째 인격
   źródło: Personalities.json :: dataList[id=10615].desc
   limit: do 120 znaków
   EN: Hong Lu's 15th Identity
   PL: Piętnasta Tożsamość Hong Lu
647. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 오랏줄 죄기
   źródło: Skills_personality-06.json :: dataList[id=1061501].levelList[level=1].name ; dataList[id=1061501].levelList[level=2].name ; dataList[id=1061501].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 2 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Constricting Ohra Bonds
   PL: Naciąganie Wiązadeł Ohra
648. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1061501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +3 [Breath] Count
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 3
649. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL: [OnSucceedAttack] Zyskuje 3 [Breath]
650. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061501].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1061501].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1061501].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 576 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061501].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1061501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061501].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1061501].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1061501].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상에게 [TiedRopeHonglu]가 있으면, [TiedRopeHonglu] 수치 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061501].levelList[level=1].coinlist[#2].coindescs[#1].desc ; dataList[id=1061501].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1061501].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TiedRopeHonglu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TiedRopeHonglu] = 포박 [홍루] / Trussed [Hong Lu]
   EN: [OnSucceedAttack] If target has [TiedRopeHonglu], inflict 1 [TiedRopeHonglu]
   PL: [OnSucceedAttack] Jeżeli cel ma [TiedRopeHonglu], zwiększa Moc [TiedRopeHonglu] o 1
654. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1061501].levelList[level=2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] At 6+ ([Breath] on self + [Laceration] on target), Coin Power +1\n[WhenUse] Gain +3 [Breath] Count
   PL: [WhenUse] Przy 6+ (suma własnego [Breath] i [Laceration] celu) Moc Monet +1\n[WhenUse] Zwiększa własny Licznik [Breath] o 3
655. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061501].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1061501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 4 [Breath]
   PL: [OnSucceedAttack] Zyskuje 4 [Breath]
656. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상에게 [TiedRopeHonglu]가 있으면, 최종 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1061501].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration], [TiedRopeHonglu]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [TiedRopeHonglu] = 포박 [홍루] / Trussed [Hong Lu]
   EN: [WhenUse] Coin Power +1 for every 6 ([Breath] on self + [Laceration] on target) (max 2)\n[WhenUse] If target has [TiedRopeHonglu], Final Power +1\n[WhenUse] Gain +3 [Breath] Count
   PL: [WhenUse] Moc Monet +1 za każde 6 (suma własnego [Breath] i [Laceration] celu) (maks. 2)\n[WhenUse] Jeżeli cel ma [TiedRopeHonglu], Moc Końcowa +1\n[WhenUse] Zwiększa własny Licznik [Breath] o 3
657. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 찢어베기
   źródło: Skills_personality-06.json :: dataList[id=1061502].levelList[level=1].name ; dataList[id=1061502].levelList[level=2].name ; dataList[id=1061502].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Avulsion Slash
   PL: Rozdzierające Cięcie
658. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061502].levelList[level=1].desc
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061502].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1061502].levelList[level=2].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061502].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1061502].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1061502].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [TiedRopeHonglu]가 2 이상이면, [TiedRopeHonglu]를 1 소모하여 이 코인 재사용 (스킬당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061502].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1061502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TiedRopeHonglu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TiedRopeHonglu] = 포박 [홍루] / Trussed [Hong Lu]
   EN: [OnSucceedAttack] If target has 2+ [TiedRopeHonglu], consume 1 [TiedRopeHonglu] on target to Reuse this Coin (once per Skill)
   PL: [OnSucceedAttack] Jeżeli cel ma 2+ [TiedRopeHonglu], zużywa 1 [TiedRopeHonglu] celu, aby ponownie użyć tej monety (1 raz na Umiejętność)
662. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [ScratchesHurtID] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061502].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1061502].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1061502].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [ScratchesHurtID]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [ScratchesHurtID] = 찢긴 상처 / Avulsion Wound
   EN: [CriticalOnSucceedAttack] Inflict 1 [ScratchesHurtID]
   PL: [CriticalOnSucceedAttack] Nakłada 1 [ScratchesHurtID]
663. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 3 — opis] [ReUseOnSucceedAttack] 다음 턴에 [Agility] 2 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061502].levelList[level=1].coinlist[#1].coindescs[#2].desc ; dataList[id=1061502].levelList[level=2].coinlist[#1].coindescs[#2].desc ; dataList[id=1061502].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [Agility]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [Agility] = 신속 / Haste
   EN: [ReUseOnSucceedAttack] Gain 2 [Agility] next turn
   PL: [ReUseOnSucceedAttack] Zyskuje 2 [Agility] w następnej turze
664. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 4 — opis] [ReUseOnSucceedAttack] 대상의 [Laceration] 발동, [Laceration] 횟수 1 감소
   źródło: Skills_personality-06.json :: dataList[id=1061502].levelList[level=1].coinlist[#1].coindescs[#3].desc ; dataList[id=1061502].levelList[level=2].coinlist[#1].coindescs[#3].desc ; dataList[id=1061502].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [Laceration]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [Laceration] = 출혈 / Bleed
   EN: [ReUseOnSucceedAttack] Activate [Laceration] on target. Target loses 1 [Laceration] Count
   PL: [ReUseOnSucceedAttack] Uruchamia [Laceration] na celu. Cel traci 1 Licznika [Laceration]
665. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061502].levelList[level=2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] At 6+ ([Breath] on self + [Laceration] on target), Coin Power +1\n[WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Przy 6+ (suma własnego [Breath] i [Laceration] celu) Moc Monet +1\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
666. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상에게 [TiedRopeHonglu]가 있으면, 최종 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061502].levelList[level=4].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration], [TiedRopeHonglu]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [TiedRopeHonglu] = 포박 [홍루] / Trussed [Hong Lu]
   EN: [WhenUse] Coin Power +1 for every 6 ([Breath] on self + [Laceration] on target) (max 2)\n[WhenUse] If target has [TiedRopeHonglu], Final Power +1\n[WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Moc Monet +1 za każde 6 (suma własnego [Breath] i [Laceration] celu) (maks. 2)\n[WhenUse] Jeżeli cel ma [TiedRopeHonglu], Moc Końcowa +1\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
667. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 649 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 추쇄집행
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=3].name ; dataList[id=1061503].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Hunter's Scouring
   PL: Zmiatanie Łowcy
669. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합이 6 이상이면, 코인 위력 +1\n[WhenUse] 대상에게 [TiedRopeHonglu]가 있으면,\n이 스킬의 모든 코인이 [SuperCoin]으로 변경되고 최종 위력 +1, 마지막 코인 적중시 아래 효과 적용\n- [Laceration] 횟수 2 증가\n- 다음 턴에 [Reduction] 1 부여\n[WhenUse] [Breath] 5 얻음\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=3].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration], [TiedRopeHonglu], [SuperCoin], [Reduction]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [TiedRopeHonglu] = 포박 [홍루] / Trussed [Hong Lu]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [WhenUse] At 6+ ([Breath] on self + [Laceration] on target), Coin Power +1\n[WhenUse] If target has [TiedRopeHonglu], convert all Coins in this Skill to [SuperCoin]s, gain Final Power +1, and the final Coin applies the following On Hit:\n- Inflict +2 [Laceration] Count\n- Inflict 1 [Reduction] next turn\n[WhenUse] Gain 5 [Breath]\n[WhenUse] Gain +3 [Breath] Count
   PL: [WhenUse] Przy 6+ (suma własnego [Breath] i [Laceration] celu) Moc Monet +1\n[WhenUse] Jeżeli cel ma [TiedRopeHonglu], wszystkie monety tej Umiejętności stają się [SuperCoin]ami, zyskuje Moc Końcowa +1, a ostatnia moneta stosuje przy trafieniu poniższe efekty:\n- Zwiększa Licznik [Laceration] celu o 2\n- Nakłada w następnej turze 1 [Reduction]\n[WhenUse] Zyskuje 5 [Breath]\n[WhenUse] Zwiększa własny Licznik [Breath] o 3
670. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1061503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [TiedRopeHonglu]가 없으면, [TiedRopeHonglu] 부여
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1061503].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TiedRopeHonglu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TiedRopeHonglu] = 포박 [홍루] / Trussed [Hong Lu]
   EN: [OnSucceedAttack] If target does not have [TiedRopeHonglu], inflict [TiedRopeHonglu]
   PL: [OnSucceedAttack] Jeżeli cel nie ma [TiedRopeHonglu], nakłada [TiedRopeHonglu]
672. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1061503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 576 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1061503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [ScratchesHurtID] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ScratchesHurtID]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ScratchesHurtID] = 찢긴 상처 / Avulsion Wound
   EN: [OnSucceedAttack] Inflict 1 [ScratchesHurtID]
   PL: [OnSucceedAttack] Nakłada 1 [ScratchesHurtID]
676. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 3 — opis] [CriticalOnSucceedAttack] [ScratchesHurtID] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=3].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상에게 [ScratchesHurtID]가 있으면, 피해량 +20%\n[WhenUse] 대상에게 [TiedRopeHonglu]가 있으면,\n이 스킬의 모든 코인이 [SuperCoin]으로 변경되고 최종 위력 +1, 마지막 코인 적중시 아래 효과 적용\n- [Laceration] 횟수 2 증가\n- 다음 턴에 [Reduction] 1 부여\n[WhenUse] [Breath] 5 얻음\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=4].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Laceration], [ScratchesHurtID], [TiedRopeHonglu], [SuperCoin], [Reduction]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [ScratchesHurtID] = 찢긴 상처 / Avulsion Wound; [TiedRopeHonglu] = 포박 [홍루] / Trussed [Hong Lu]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [WhenUse] Coin Power +1 for every 6 ([Breath] on self + [Laceration] on target) (max 2)\n[WhenUse] If target has [ScratchesHurtID], deal +20% damage\n[WhenUse] If target has [TiedRopeHonglu], convert all Coins in this Skill to [SuperCoin]s, gain Final Power +1, and the final Coin applies the following On Hit:\n- Inflict +2 [Laceration] Count\n- Inflict 1 [Reduction] next turn\n[WhenUse] Gain 5 [Breath]\n[WhenUse] Gain +3 [Breath] Count
   PL: [WhenUse] Moc Monet +1 za każde 6 (suma własnego [Breath] i [Laceration] celu) (maks. 2)\n[WhenUse] Jeżeli cel ma [ScratchesHurtID], zadaje +20% obrażeń\n[WhenUse] Jeżeli cel ma [TiedRopeHonglu], wszystkie monety tej Umiejętności stają się [SuperCoin]ami, zyskuje Moc Końcowa +1, a ostatnia moneta stosuje przy trafieniu poniższe efekty:\n- Zwiększa Licznik [Laceration] celu o 2\n- Nakłada w następnej turze 1 [Reduction]\n[WhenUse] Zyskuje 5 [Breath]\n[WhenUse] Zwiększa własny Licznik [Breath] o 3
678. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] 크리티컬 피해량 +50%
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +50% damage on Critical Hit
   PL: Zadaje +50% obrażeń Krytycznych
679. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [ScratchesHurtID] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=4].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 675 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 4 — opis] [CriticalOnSucceedAttack] [ScratchesHurtID] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=4].coinlist[#3].coindescs[#3].desc
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 5 — opis] [CriticalOnSucceedAttack] 다음 턴에 [IndigoTakeDamageUp] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061503].levelList[level=4].coinlist[#3].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [IndigoTakeDamageUp]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [IndigoTakeDamageUp] = 오만 취약 / Pride Fragility
   EN: [CriticalOnSucceedAttack] Inflict 1 [IndigoTakeDamageUp] next turn
   PL: [CriticalOnSucceedAttack] Nakłada w następnej turze 1 [IndigoTakeDamageUp]
683. [Obrona (ulepszenia 1,4) — nazwa] 오랏줄 걸기
   źródło: Skills_personality-06.json :: dataList[id=1061504].levelList[level=1].name ; dataList[id=1061504].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: kontra · moc bazowa: 5 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Throwing the Ohra Bond
   PL: Rzucenie Wiązadeł Ohra
684. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합이 6 이상이면, 합 위력 +2\n[WhenUse] [Breath] 5 얻음
   źródło: Skills_personality-06.json :: dataList[id=1061504].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Breath], [Laceration]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed
   EN: [DuelCounter]\n[WhenUse] At 6+ ([Breath] on self + [Laceration] on target), Clash Power +2\n[WhenUse] Gain 5 [Breath]
   PL: [DuelCounter]\n[WhenUse] Przy 6+ (suma własnego [Breath] i [Laceration] celu) Moc Starcia +2\n[WhenUse] Zyskuje 5 [Breath]
685. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061504].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1061504].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Obrona (ulepszenia 1,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [TiedRopeHonglu] 부여
   źródło: Skills_personality-06.json :: dataList[id=1061504].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1061504].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TiedRopeHonglu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TiedRopeHonglu] = 포박 [홍루] / Trussed [Hong Lu]
   EN: [OnSucceedAttack] Inflict [TiedRopeHonglu]
   PL: [OnSucceedAttack] Nakłada [TiedRopeHonglu]
687. [Obrona (ulepszenia 1,4) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061504].levelList[level=1].coinlist[#0].coindescs[#2].desc ; dataList[id=1061504].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Laceration]
   PL: [UnBrokenCoinOnSucceedAttack] Nakłada 1 [Laceration]
688. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[WhenUse] 자신의 [Breath]과 대상의 [Laceration]의 합이 6 이상이면, 합 위력 +2\n[WhenUse] [Breath] 5 얻음\n[WinDuel] [Breath] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1061504].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [Breath], [Laceration], [WinDuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [DuelCounter]\n[WhenUse] At 6+ ([Breath] on self + [Laceration] on target), Clash Power +2\n[WhenUse] Gain 5 [Breath]\n[WinDuel] Gain +3 [Breath] Count
   PL: [DuelCounter]\n[WhenUse] Przy 6+ (suma własnego [Breath] i [Laceration] celu) Moc Starcia +2\n[WhenUse] Zyskuje 5 [Breath]\n[WinDuel] Zwiększa własny Licznik [Breath] o 3
689. [Pasywka bojowa (od ulepszenia 1) — nazwa] 추노꾼
   źródło: Passives.json :: dataList[id=1061502].name
   limit: do 40 znaków
   EN: Ch'unokkun
   PL: Ch'unokkun
690. [Pasywka bojowa (od ulepszenia 1) — opis] [TiedRopeHonglu]가 부여된 대상이 있으면, [TiedWithRopeID] 얻음\n자신이 [TiedRopeHonglu]를 부여한 적에게 스킬 지정 시 속도에 관계 없이 공격 스킬의 공격 대상을 자신으로 변경할 수 있음 (집중 전투 전용)
   źródło: Passives.json :: dataList[id=1061502].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [TiedRopeHonglu], [TiedWithRopeID]
   znaczenie tagów: [TiedRopeHonglu] = 포박 [홍루] / Trussed [Hong Lu]; [TiedWithRopeID] = 압송 채비 / Prisoner Transport Arrangements
   EN: If a target has [TiedRopeHonglu], gain [TiedWithRopeID]\nWhen chaining Skills, if there is an enemy this unit has inflicted [TiedRopeHonglu] on, then this unit can redirect that enemy's Attack Skill's targeting to itself regardless of Speed (Focused Encounters only)
   PL: Jeżeli cel ma [TiedRopeHonglu], zyskuje [TiedWithRopeID]\nJeżeli istnieje wróg, na którym ta jednostka nakładała [TiedRopeHonglu], przy wskazywaniu Umiejętności może przekierować cel Umiejętności ataku tego wroga na siebie niezależnie od Szybkości (tylko walki skupione)
691. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — nazwa] 추쇄건[推刷巾]
   źródło: Passives.json :: dataList[id=1061501].name
   limit: do 40 znaków
   EN: Scouring Hunterband [推刷巾]
   PL: Taśma Zmiatającego Łowcy [推刷巾]
692. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Pride) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 2)%만큼 피해량이 증가 (최대 10%)\n- 대상이 [TiedRopeHonglu] 상태면, 피해량이 증가하는 효과가 2배로 적용됨 (최대 20%)\n\n전투 시작시 이번 턴에 참격 속성이고, 오만 속성인 스킬을 장착한 아군당 피해량 +5% (최대 30%)
   źródło: Passives.json :: dataList[id=1061501].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [TiedRopeHonglu]
   znaczenie tagów: [TiedRopeHonglu] = 포박 [홍루] / Trussed [Hong Lu]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x 2)% damage (max 10%)\n- If target is [TiedRopeHonglu], double the above damage increase effect (max 20%)\n\nCombat Start: Deal +5% damage for every ally that has a Slash Pride Skill equipped this turn (max 30%)
   PL: Jeżeli ta jednostka jest szybsza niż cel, zadaje +(różnica Szybkości x 2)% obrażeń (maks. 10%)\n- Jeżeli cel ma [TiedRopeHonglu], powyższy efekt zwiększania obrażeń działa dwukrotnie (maks. 20%)\n\nNa początku walki zadaje +5% obrażeń za każdego sojusznika z wyposażoną w tej turze Umiejętnością Sieczną z atrybutem Pychy (maks. 30%)
693. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — nazwa] 악에 받친 추격
   źródło: Passives.json :: dataList[id=1061521].name
   limit: do 40 znaków
   EN: Spiteful Pursuit
   PL: Prześladowanie Pędzone Złością
694. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — opis] 편성 순서가 가장 빠른 아군 1명이 [Binding]이 부여된 적을 공격할 때, 피해량 +10%
   źródło: Passives.json :: dataList[id=1061521].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: When 1 ally with the earliest Deployment order attacks an enemy that has [Binding], deal +10% damage
   PL: Gdy 1 Sojusznik przydzielony najwcześniej na pozycji atakuje wroga z [Binding], zadaje +10% obrażeń

## [000] Cinq Assoc. East Section 3 — Hong Lu — 동부 섕크 협회 3과
- ID Tożsamości: `10616` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 82 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Poise, Burn

695. [Karta Tożsamości — tytuł] 동부 섕크 협회\n3과
   źródło: Personalities.json :: dataList[id=10616].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cinq Assoc.\nEast Section 3
   PL: Stowarzyszenie Cinq\nSekcja Wschodnia 3
696. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10616].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10616].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Karta Tożsamości — opis] 홍루의 열여섯번째 인격
   źródło: Personalities.json :: dataList[id=10616].desc
   limit: do 120 znaków
   EN: Hong Lu's 16th Identity
   PL: Szesnasta Tożsamość Hong Lu
699. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 발경
   źródło: Skills_personality-06.json :: dataList[id=1061601].levelList[level=1].name ; dataList[id=1061601].levelList[level=2].name ; dataList[id=1061601].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 6 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Fa Jin
   PL: Fa Jin
700. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상에게 [DianxueHongLu]가 없으면, 합 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1061601].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DianxueHongLu], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu; [Breath] = 호흡 / Poise
   EN: [WhenUse] If target does not have [DianxueHongLu], Clash Power +1\n[WhenUse] Gain +3 [Breath] Count
   PL: [WhenUse] Jeżeli cel nie ma [DianxueHongLu], Moc Starcia +1\n[WhenUse] Zwiększa własny Licznik [Breath] o 3
701. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061601].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1061601].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]
702. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [DianxueHongLu]가 3 이상이면, 이 코인 재사용 (스킬당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061601].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1061601].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DianxueHongLu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu
   EN: [OnSucceedAttack] If target has 3+ [DianxueHongLu], Reuse this Coin (once per Skill)
   PL: [OnSucceedAttack] Jeżeli cel ma 3+ [DianxueHongLu], ponownie używa tej monety (1 raz na Umiejętność)
703. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">자신의 속도가 대상보다 2 이상 높으면, 코인 위력 +1</style>\n[WhenUse] 대상에게 [DianxueHongLu]가 없으면, 합 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1061601].levelList[level=2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [DianxueHongLu], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu; [Breath] = 호흡 / Poise
   EN: <style="highlight">If this unit's Speed is faster than the target's by 2 or more, Coin Power +1</style>\n[WhenUse] If target does not have [DianxueHongLu], Clash Power +1\n[WhenUse] Gain +3 [Breath] Count
   PL: <style="highlight">Jeżeli ta jednostka jest szybsza niż cel o 2 lub więcej, Moc Monet +1</style>\n[WhenUse] Jeżeli cel nie ma [DianxueHongLu], Moc Starcia +1\n[WhenUse] Zwiększa własny Licznik [Breath] o 3
704. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 3 — opis] <style="highlight">[ReUseOnSucceedAttack] [Combustion] 1 부여</style>
   źródło: Skills_personality-06.json :: dataList[id=1061601].levelList[level=2].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [Combustion]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[ReUseOnSucceedAttack] Inflict 1 [Combustion]</style>
   PL: <style="highlight">[ReUseOnSucceedAttack] Nakłada 1 [Combustion]</style>
705. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 자신의 속도가 대상보다 2 이상 높으면, 코인 위력 +1\n<style="highlight">[WhenUse] 자신의 [Breath]과 대상의 [Combustion]의 합 6당, 합 위력 +1 (최대 2)</style>\n[WhenUse] 대상에게 [DianxueHongLu]가 없으면, 합 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1061601].levelList[level=4].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Combustion], [DianxueHongLu]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu
   EN: If this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n<style="highlight">[WhenUse] Clash Power +1 for every 6 ([Breath] on self + [Combustion] on target) (max 2)</style>\n[WhenUse] If target does not have [DianxueHongLu], Clash Power +1\n[WhenUse] Gain +3 [Breath] Count
   PL: Jeżeli ta jednostka jest szybsza niż cel o 2 lub więcej, Moc Monet +1\n<style="highlight">[WhenUse] Moc Starcia +1 za każde 6 (suma własnego [Breath] i [Combustion] celu) (maks. 2)</style>\n[WhenUse] Jeżeli cel nie ma [DianxueHongLu], Moc Starcia +1\n[WhenUse] Zwiększa własny Licznik [Breath] o 3
706. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]<style="highlight"></style>
707. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [DianxueHongLu]가 3 이상이면, 이 코인 재사용 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061601].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DianxueHongLu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu
   EN: [OnSucceedAttack] If target has 3+ [DianxueHongLu], Reuse this Coin (once per Skill)<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli cel ma 3+ [DianxueHongLu], ponownie używa tej monety (1 raz na Umiejętność)<style="highlight"></style>
708. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 3 — opis] [ReUseOnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061601].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [Combustion]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [Combustion] = 화상 / Burn
   EN: [ReUseOnSucceedAttack] Inflict 1 [Combustion]<style="highlight"></style>
   PL: [ReUseOnSucceedAttack] Nakłada 1 [Combustion]<style="highlight"></style>
709. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 초염장
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=1].name ; dataList[id=1061602].levelList[level=2].name ; dataList[id=1061602].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 6 · monety: 0 (—)
   limit: do 40 znaków
   EN: Virescent Flame Palm
   PL: Wichrzasta Dłoń Płomienia
710. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] [Breath] 3 얻음\n- 대상의 [DianxueHongLu]만큼 추가로 자신의 [Breath] 횟수 증가
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Breath], [DianxueHongLu]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu
   EN: [WinDuel] Gain 3 [Breath]\n- Gain [Breath] Count equal to [DianxueHongLu] on target
   PL: [WinDuel] Zyskuje 3 [Breath]\n- Zwiększa dodatkowo własny Licznik [Breath] o wartość [DianxueHongLu] celu
711. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 487 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [DianxueHongLu]가 2 이상이면, 이 코인 재사용 (스킬당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DianxueHongLu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu
   EN: [OnSucceedAttack] If target has 2+ [DianxueHongLu], Reuse this Coin (once per Skill)
   PL: [OnSucceedAttack] Jeżeli cel ma 2+ [DianxueHongLu], ponownie używa tej monety (1 raz na Umiejętność)
714. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2당 코인 위력 +1. 최대 2)</style>\n[WinDuel] [Breath] 3 얻음\n- 대상의 [DianxueHongLu]만큼 추가로 자신의 [Breath] 횟수 증가
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=2].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WinDuel], [Breath], [DianxueHongLu]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu
   EN: <style="highlight">If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)</style>\n[WinDuel] Gain 3 [Breath]\n- Gain [Breath] Count equal to [DianxueHongLu] on target
   PL: <style="highlight">Im szybsza ta jednostka niż cel, tym więcej Moc Monet (Moc Monet +1 za każde 2 różnicy Szybkości; maks. 2)</style>\n[WinDuel] Zyskuje 3 [Breath]\n- Zwiększa dodatkowo własny Licznik [Breath] o wartość [DianxueHongLu] celu
715. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +<style="highlight">2</style> [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +<style="highlight">2</style> Licznika [Breath]
716. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Combustion]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Combustion]
717. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttack] [Combustion] 횟수 1 증가</style>
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: <style="highlight">[OnSucceedAttack] Inflict +1 [Combustion] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Zwiększa Licznik [Combustion] celu o 1</style>
718. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [DianxueHongLu]가 2 이상이면, 이 코인 재사용 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1061602].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DianxueHongLu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu
   EN: [OnSucceedAttack] If target has 2+ [DianxueHongLu], Reuse this Coin (once per Skill)<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli cel ma 2+ [DianxueHongLu], ponownie używa tej monety (1 raz na Umiejętność)<style="highlight"></style>
719. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 3 — opis] <style="highlight">[ReUseOnSucceedAttack] [DianxueHongLu]만큼 [DefenseDown] 부여 (턴당 1회)</style>
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=2].coinlist[#1].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [DianxueHongLu], [DefenseDown]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: <style="highlight">[ReUseOnSucceedAttack] Inflict [DefenseDown] equal to [DianxueHongLu] on target (once per turn)</style>
   PL: <style="highlight">[ReUseOnSucceedAttack] Nakłada [DefenseDown] równy wartości [DianxueHongLu] celu (1 raz na turę)</style>
720. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2당 코인 위력 +1. 최대 2)\n<style="highlight">[WhenUse] 자신의 [Breath]과 대상의 [Combustion]의 합이 6 이상이면, 최종 위력 +1</style>\n[WinDuel] [Breath] 3 얻음\n- 대상의 [DianxueHongLu]만큼 추가로 자신의 [Breath] 횟수 증가
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=4].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Combustion], [WinDuel], [DianxueHongLu]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn; [WinDuel] = [합 승리시] / [Clash Win]; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu
   EN: If this unit's Speed is faster than the target's, gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)\n<style="highlight">[WhenUse] At 6+ ([Breath] on self + [Combustion] on target), Final Power +1</style>\n[WinDuel] Gain 3 [Breath]\n- Gain [Breath] Count equal to [DianxueHongLu] on target
   PL: Im szybsza ta jednostka niż cel, tym więcej Moc Monet (Moc Monet +1 za każde 2 różnicy Szybkości; maks. 2)\n<style="highlight">[WhenUse] Przy 6+ (suma własnego [Breath] i [Combustion] celu) Moc Końcowa +1</style>\n[WinDuel] Zyskuje 3 [Breath]\n- Zwiększa dodatkowo własny Licznik [Breath] o wartość [DianxueHongLu] celu
721. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 480 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Combustion]<style="highlight"></style>
723. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +1 [Combustion] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Combustion] celu o 1<style="highlight"></style>
724. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 3 — opis] [ReUseOnSucceedAttack] [DianxueHongLu]만큼 [DefenseDown] 부여 (턴당 1회)<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061602].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [DianxueHongLu], [DefenseDown]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [ReUseOnSucceedAttack] Inflict [DefenseDown] equal to [DianxueHongLu] on target (once per turn)<style="highlight"></style>
   PL: [ReUseOnSucceedAttack] Nakłada [DefenseDown] równy wartości [DianxueHongLu] celu (1 raz na turę)<style="highlight"></style>
725. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 마지막 수까지 받아주시겠어요?
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=3].name ; dataList[id=1061603].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 60 znaków
   EN: Take the Hit to the Last Blow, Please?
   PL: Przyjmie Pan Cios aż do Ostatniego Uderzenia?
726. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 대상보다 2 이상 높으면, 코인 위력 +1\n[WinDuel] [Breath] 3 얻음\n- 대상의 [DianxueHongLu]만큼 추가로 자신의 [Breath] 횟수 증가
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=3].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Breath], [DianxueHongLu]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu
   EN: If this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[WinDuel] Gain 3 [Breath]\n- Gain [Breath] Count equal to [DianxueHongLu] on target
   PL: Jeżeli ta jednostka jest szybsza niż cel o 2 lub więcej, Moc Monet +1\n[WinDuel] Zyskuje 3 [Breath]\n- Zwiększa dodatkowo własny Licznik [Breath] o wartość [DianxueHongLu] celu
727. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 701 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +(자신의 [Breath] + 대상의 [Combustion])% (최대 20%)
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath], [Combustion]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn
   EN: Deal +([Breath] on self + [Combustion] on target)% damage on Critical Hit (max 20%)
   PL: Zadaje +(suma własnego [Breath] i [Combustion] celu)% obrażeń przy trafieniu krytycznym (maks. 20%)
730. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] [DefenseDown] 2 부여 (턴당 2회)
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [DefenseDown]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [CriticalOnSucceedAttack] Inflict 2 [DefenseDown] (2 times per turn)
   PL: [CriticalOnSucceedAttack] Nakłada 2 [DefenseDown] (2 razy na turę)
732. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 대상에게 [DianxueHongLu]가 있으면, 이 코인 재사용 (스킬당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DianxueHongLu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu
   EN: [OnSucceedAttack] If target has [DianxueHongLu], Reuse this Coin (once per Skill)
   PL: [OnSucceedAttack] Jeżeli cel ma [DianxueHongLu], ponownie używa tej monety (1 raz na Umiejętność)
733. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 5 — opis] [ReUseOnSucceedAttack] 이 코인 최종 피해량의 (대상의 [Combustion] x 2)%만큼 분노 피해 (최대 40%)
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=3].coinlist[#2].coindescs[#4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [Combustion]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [Combustion] = 화상 / Burn
   EN: [ReUseOnSucceedAttack] Deal Wrath damage equal to ([Combustion] on target x 2)% of this Coin's final damage (max 40%)
   PL: [ReUseOnSucceedAttack] Zadaje obrażenia Gniewu równe ([Combustion] celu x 2)% końcowych obrażeń tej monety (maks. 40%)
734. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 속도가 대상보다 2 이상 높으면, 코인 위력 +1\n<style="highlight">[WhenUse] 자신의 [Breath]과 대상의 [Combustion]의 합이 6 이상이면, 코인 위력 +1</style>\n[WinDuel] [Breath] <style="highlight">5</style> 얻음\n- 대상의 [DianxueHongLu]만큼 추가로 자신의 [Breath] 횟수 증가
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Combustion], [WinDuel], [DianxueHongLu]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn; [WinDuel] = [합 승리시] / [Clash Win]; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu
   EN: If this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n<style="highlight">[WhenUse] At 6+ ([Breath] on self + [Combustion] on target), Coin Power +1</style>\n[WinDuel] Gain <style="highlight">5</style> [Breath]\n- Gain [Breath] Count equal to [DianxueHongLu] on target
   PL: Jeżeli ta jednostka jest szybsza niż cel o 2 lub więcej, Moc Monet +1\n<style="highlight">[WhenUse] Przy 6+ (suma własnego [Breath] i [Combustion] celu) Moc Monet +1</style>\n[WinDuel] Zyskuje <style="highlight">5</style> [Breath]\n- Zwiększa dodatkowo własny Licznik [Breath] o wartość [DianxueHongLu] celu
735. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 716 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
736. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] <style="highlight">2</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 716 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +(자신의 [Breath] + 대상의 [Combustion])% (최대 <style="highlight">30</style>%)
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Breath], [Combustion]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn
   EN: Deal +([Breath] on self + [Combustion] on target)% damage on Critical Hit (max <style="highlight">30</style>%)
   PL: Zadaje +(suma własnego [Breath] i [Combustion] celu)% obrażeń przy trafieniu krytycznym (maks. <style="highlight">30</style>%)
738. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 723 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] [DefenseDown] 2 부여 (턴당 2회)<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [DefenseDown]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [CriticalOnSucceedAttack] Inflict 2 [DefenseDown] (2 times per turn)<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Nakłada 2 [DefenseDown] (2 razy na turę)<style="highlight"></style>
740. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 대상에게 [DianxueHongLu]가 있으면, 이 코인 재사용 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [DianxueHongLu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu
   EN: [OnSucceedAttack] If target has [DianxueHongLu], Reuse this Coin (once per Skill)<style="highlight"></style>
   PL: [OnSucceedAttack] Jeżeli cel ma [DianxueHongLu], ponownie używa tej monety (1 raz na Umiejętność)<style="highlight"></style>
741. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 5 — opis] [ReUseOnSucceedAttack] 이 코인 최종 피해량의 (대상의 [Combustion] x 2)%만큼 분노 피해 (최대 40%)<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061603].levelList[level=4].coinlist[#2].coindescs[#4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [Combustion]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [Combustion] = 화상 / Burn
   EN: [ReUseOnSucceedAttack] Deal Wrath damage equal to ([Combustion] on target x 2)% of this Coin's final damage (max 40%)<style="highlight"></style>
   PL: [ReUseOnSucceedAttack] Zadaje obrażenia Gniewu równe ([Combustion] celu x 2)% końcowych obrażeń tej monety (maks. 40%)<style="highlight"></style>
742. [Obrona (ulepszenia 1,4) — nazwa] 구름처럼 가벼이
   źródło: Skills_personality-06.json :: dataList[id=1061604].levelList[level=1].name ; dataList[id=1061604].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: unik · moc bazowa: 4 · monety: 0 (—)
   limit: do 40 znaków
   EN: Light as a Tuft of Cloud
   PL: Lekka jak Kłębek Chmur
743. [Obrona (ulepszenie 1) — opis] 자신의 속도가 공격자보다 2 이상 높으면, 코인 위력 +1\n[StartBattle] 자신의 [Breath] 횟수 2 증가 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061604].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the attacker's by 2 or more, Coin Power +1\n[StartBattle] Gain +2 [Breath] Count (once per turn)
   PL: Jeżeli Szybkość tej jednostki jest większa niż atakującego o 2 lub więcej, Moc Monet +1\n[StartBattle] Zwiększa własny Licznik [Breath] o 2 (1 raz na turę)
744. [Obrona (ulepszenie 4) — opis] 자신의 속도가 공격자보다 2 이상 높으면, 코인 위력 +1\n[StartBattle] 자신의 [Breath] 횟수 <style="highlight">3</style> 증가 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061604].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise
   EN: If this unit's Speed is faster than the attacker's by 2 or more, Coin Power +1\n[StartBattle] Gain +<style="highlight">3</style> [Breath] Count (once per turn)
   PL: Jeżeli Szybkość tej jednostki jest większa niż atakującego o 2 lub więcej, Moc Monet +1\n[StartBattle] Zwiększa własny Licznik [Breath] o <style="highlight">3</style> (1 raz na turę)
745. [Pasywka bojowa (od ulepszenia 1) — nazwa] 입회하의 결투
   źródło: Passives.json :: dataList[id=1061602].name
   limit: do 40 znaków
   EN: A Duel Witnessed
   PL: Pojedynek pod Okiem Świadków
746. [Pasywka bojowa (od ulepszenia 1) — opis] 스테이지 첫 등장 시 대기 인원 또는 서포트 인원으로 편성된 섕크 협회 소속 아군 인격 수만큼 [DuelSousTemoinsEast] 얻음 (최대 3, 사망자 포함)\n\n기본 공격 스킬로 마지막에 적중한 대상에게 다음 턴에 [DianxueHongLu] 1 부여 (턴당 1회, 집중 전투면, 부위에 부여)
   źródło: Passives.json :: dataList[id=1061602].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [DuelSousTemoinsEast], [DianxueHongLu]
   znaczenie tagów: [DuelSousTemoinsEast] = 입회 - 동부 섕크 / Witnessed - Eastern Cinq; [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu
   EN: Upon entering the Encounter for the first time, gain [DuelSousTemoinsEast] equal to the number of "Cinq Association" Identities set as Backup or Support Units (max 3, including defeated units)\n\nAgainst the target a Base Attack Skill hit last, inflict 1 [DianxueHongLu] next turn (once per turn; in Focused Encounters, the Part)
   PL: Przy pierwszym pojawieniu się na polu zyskuje [DuelSousTemoinsEast] równy liczbie Tożsamości Stowarzyszenia Cinq przydzielonych jako rezerwa lub wsparcie (maks. 3, łącznie z pokonanymi)\n\nNakłada w następnej turze 1 [DianxueHongLu] na cel ostatnio trafiony podstawową Umiejętnością ataku (1 raz na turę; w walkach skupionych na Partach)
747. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Wrath, posiadane 2× Pride) — nazwa] 초염옥구
   źródło: Passives.json :: dataList[id=1061601].name
   limit: do 40 znaków
   EN: Virescent Pyrojade
   PL: Wichrzasty Rubin Płomienia
748. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Wrath, posiadane 2× Pride) — opis] 합 승리 시 대상에게 점혈이 있으면, [DianxueHongLu] 1 부여 (턴당 1회)\n\n턴 종료 시 자신의 [Breath] 위력 5당, 다음 턴에 [Agility] 1 얻음 (최대 2)\n\n크리티컬 피해량 +(대상의 [Combustion] 위력)% (최대 15%)
   źródło: Passives.json :: dataList[id=1061601].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [DianxueHongLu], [Breath], [Agility], [Combustion]
   znaczenie tagów: [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [Combustion] = 화상 / Burn
   EN: On Clash Win, if target has Nerve Strike, inflict 1 [DianxueHongLu] (once per turn)\n\nTurn End: Gain 1 [Agility] next turn for every 5 [Breath] Potency on self (max 2)\n\nDeal +([Combustion] Potency on target)% damage on Critical Hit (max 15%)
   PL: Przy wygranej w starciu, jeżeli cel ma Punkt Witalny, nakłada 1 [DianxueHongLu] (1 raz na turę)\n\nNa koniec tury zyskuje 1 [Agility] w następnej turze za każde 5 Mocy [Breath] (maks. 2)\n\nZadaje +(Moc [Combustion] celu)% obrażeń przy trafieniu krytycznym (maks. 15%)
749. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Wrath, posiadane 2× Pride) — nazwa] 초염옥구
   źródło: Passives.json :: dataList[id=1061611].name
   (powtórzenie elementu 747 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Wrath, posiadane 2× Pride) — opis] 합 승리 시 대상에게 점혈이 있으면, [DianxueHongLu] 1 부여 (턴당 1회)\n\n턴 종료 시 자신의 [Breath] 위력 <style="highlight">3</style>당, 다음 턴에 [Agility] 1 얻음 (최대 2)\n\n크리티컬 피해량 +(대상의 [Combustion] 위력)% (최대 15%)\n<style="highlight">- 대상의 [DianxueHongLu] 1당, 최댓값 5% 증가</style>
   źródło: Passives.json :: dataList[id=1061611].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DianxueHongLu], [Breath], [Agility], [Combustion]
   znaczenie tagów: [DianxueHongLu] = 점혈 - 홍루 / Nerve Strike - Hong Lu; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [Combustion] = 화상 / Burn
   EN: On Clash Win, if target has Nerve Strike, inflict 1 [DianxueHongLu] (once per turn)\n\nTurn End: Gain 1 [Agility] next turn for every <style="highlight">3</style> [Breath] Potency on self (max 2)\n\nDeal +([Combustion] Potency on target)% damage on Critical Hit (max 15%)\n<style="highlight">- Increase max cap by 5% for every 1 [DianxueHongLu] on the target</style>
   PL: Przy wygranej w starciu, jeżeli cel ma Punkt Witalny, nakłada 1 [DianxueHongLu] (1 raz na turę)\n\nNa koniec tury zyskuje 1 [Agility] w następnej turze za każde <style="highlight">3</style> Mocy [Breath] (maks. 2)\n\nZadaje +(Moc [Combustion] celu)% obrażeń przy trafieniu krytycznym (maks. 15%)\n<style="highlight">- Zwiększa maks. pułap o 5% za każde 1 [DianxueHongLu] celu</style>
751. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — nazwa] 퇴로를 녹여둘게요
   źródło: Passives.json :: dataList[id=1061621].name
   limit: do 40 znaków
   EN: I'll Melt Open the Way Out
   PL: Roztopię Drogę Ewakuacji
752. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Wrath) — opis] 속도가 가장 빠른 아군이 [Combustion] 또는 특수 화상을 보유한 적에게 합 승리 시, 다음 턴에 [Binding] 1 부여 (턴당 1회)\n- 대상의 [Combustion] 횟수가 4 이하면, 추가로 이번 턴에 대상의 [Combustion] 횟수 1 증가\n- 대상의 [Combustion] 횟수가 5 이상이면, 추가로 이번 턴에 [Combustion] 3 부여
   źródło: Passives.json :: dataList[id=1061621].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Binding]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Binding] = 속박 / Bind
   EN: 1 ally with the fastest Speed: On Clash Win against enemies that have [Combustion] or "Unique Burn", inflict 1 [Binding] next turn (once per turn)\n- If target has 4- [Combustion] Count, also inflict +1 [Combustion] Count to the said target this turn\n- If target has 5+ [Combustion] Count, also inflict 3 [Combustion] to the said target this turn
   PL: Gdy Sojusznik z najwyższą Szybkością wygrywa starcie z wrogiem mającym [Combustion] albo „Specjalne Poparzenie”, nakłada w następnej turze 1 [Binding] (1 raz na turę)\n- Jeżeli cel ma 4 lub mniej Licznika [Combustion], nakłada dodatkowo w tej turze +1 Licznika [Combustion] temu celowi\n- Jeżeli cel ma 5+ Licznika [Combustion], nakłada dodatkowo w tej turze 3 [Combustion] temu celowi

## [000] Haute Couture:: Le Noir 3F Public Address Room — Hong Lu — 오트쿠튀르:: 르누아르 3F 방송실
- ID Tożsamości: `10617` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 8 · HP bazowe: 95 · szybkość: 3–5 / 3–6 / 4–6 / 4–6
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Charge, Tremor

753. [Karta Tożsamości — tytuł] 오트쿠튀르::\n르누아르 3F 방송실
   źródło: Personalities.json :: dataList[id=10617].title
   limit: do 70 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Haute Couture::\nLe Noir\n3F Public\nAddress Room
   PL: Haute Couture::\nLe Noir\nStudio Nadawczy na 3. Piętrze
754. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities.json :: dataList[id=10617].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities.json :: dataList[id=10617].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Karta Tożsamości — opis] 홍루의 열일곱번째 인격
   źródło: Personalities.json :: dataList[id=10617].desc
   limit: do 120 znaków
   EN: Hong Lu's 17th Identity
   PL: Siedemnasta Tożsamość Hong Lu
757. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 귀를 기울여주세요
   źródło: Skills_personality-06.json :: dataList[id=1061701].levelList[level=1].name ; dataList[id=1061701].levelList[level=2].name ; dataList[id=1061701].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Please Listen to Me
   PL: Prosimy, Posłuchajcie Mnie
758. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +2 [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o 2
759. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-06.json :: dataList[id=1061701].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1061701].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 3 소모하여, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-06.json :: dataList[id=1061701].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [ChargeNoirAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation
   EN: <style="highlight">[WhenUse] Consume 3 [ChargeNoirAlly] Count to gain Coin Power +1 (max 2 times)</style>
   PL: <style="highlight">[WhenUse] Zużywa 3 Licznika [ChargeNoirAlly], aby zyskać Moc Monet +1 (maks. 2 razy)</style>
761. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061701].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +<style="highlight">3</style> [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">3</style>
762. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 [ChargeNoirAlly] 위력 2당 피해량 +5% (최대 10%)</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 3 소모하여, 코인 위력 +1 (최대 2)\n<style="highlight">[EndSkillAll] 자신의 [ChargeNoirAlly] 횟수가 10 미만이면, 자신의 [ChargeNoirAlly] 횟수 3 증가</style>
   źródło: Skills_personality-06.json :: dataList[id=1061701].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeNoirAlly], [WhenUse], [EndSkillAll]
   znaczenie tagów: [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]; [EndSkillAll] = [스킬 종료시] / [Skill End]
   EN: <style="highlight">Deal +5% damage for every 2 [ChargeNoirAlly] Potency on self (max 10%)</style>\n[WhenUse] Consume 3 [ChargeNoirAlly] Count to gain Coin Power +1 (max 2 times)\n<style="highlight">[EndSkillAll] At fewer than 10 [ChargeNoirAlly] Count, gain +3 [ChargeNoirAlly] Count</style>
   PL: <style="highlight">Zadaje +5% obrażeń za każde 2 Mocy [ChargeNoirAlly] (maks. 10%)</style>\n[WhenUse] Zużywa 3 Licznika [ChargeNoirAlly], aby zyskać Moc Monet +1 (maks. 2 razy)\n<style="highlight">[EndSkillAll] Przy mniej niż 10 Licznika [ChargeNoirAlly] zyskuje +3 Licznika [ChargeNoirAlly]</style>
763. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +<style="highlight">4</style> [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">4</style>
764. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 반복 재생 반복
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=1].name ; dataList[id=1061702].levelList[level=2].name ; dataList[id=1061702].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Repeat on Repeat
   PL: Powtarzanie Powtórzeń
766. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Vibration]
767. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +3 [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o 3
768. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] 자신에게 [TimeToListenHonglu]이 있으면, 이 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1061702].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1061702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TimeToListenHonglu]
   znaczenie tagów: [TimeToListenHonglu] = 경청의 시간 / Time to Listen
   EN: If this unit has [TimeToListenHonglu], Reuse this Coin once (once per Skill)
   PL: Jeżeli ma [TimeToListenHonglu], ponownie używa tej monety 1 raz (1 raz na Umiejętność)
769. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [WarinessHonglu] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1061702].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1061702].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [WarinessHonglu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [WarinessHonglu] = 경청 형벌 / Auditive Punishment
   EN: [OnSucceedAttack] Inflict 1 [WarinessHonglu]
   PL: [OnSucceedAttack] Nakłada 1 [WarinessHonglu]
770. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 3 — opis] [ReUseOnSucceedAttack] 정신력 피해 3
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=1].coinlist[#1].coindescs[#2].desc ; dataList[id=1061702].levelList[level=2].coinlist[#1].coindescs[#2].desc ; dataList[id=1061702].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]
   EN: [ReUseOnSucceedAttack] Deal 3 SP damage
   PL: [ReUseOnSucceedAttack] Zadaje 3 obrażenia Poczytalności
771. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 4 — opis] [ReUseOnSucceedAttack] 다음 턴에 [AmberResistDown] 1 부여 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=1].coinlist[#1].coindescs[#3].desc ; dataList[id=1061702].levelList[level=2].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack], [AmberResistDown]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [AmberResistDown] = 나태 내성 약화 / Sloth Resist Down
   EN: [ReUseOnSucceedAttack] Inflict 1 [AmberResistDown] next turn (once per turn)
   PL: [ReUseOnSucceedAttack] Nakłada w następnej turze 1 [AmberResistDown] (1 raz na turę)
772. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 3 소모하여, 코인 위력 +1 (최대 2)</style>
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=2].desc
   (powtórzenie elementu 760 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">+3</style> [Vibration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Vibration] celu o <style="highlight">3</style>
774. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=2].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 763 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">자신의 [ChargeNoirAlly] 위력 2당 피해량 +10% (최대 20%)</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 3 소모하여, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeNoirAlly], [WhenUse]
   znaczenie tagów: [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]
   EN: <style="highlight">Deal +10% damage for every 2 [ChargeNoirAlly] Potency on self (max 20%)</style>\n[WhenUse] Consume 3 [ChargeNoirAlly] Count to gain Coin Power +1 (max 2 times)
   PL: <style="highlight">Zadaje +10% obrażeń za każde 2 Mocy [ChargeNoirAlly] (maks. 20%)</style>\n[WhenUse] Zużywa 3 Licznika [ChargeNoirAlly], aby zyskać Moc Monet +1 (maks. 2 razy)
776. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Vibration] celu o 3<style="highlight"></style>
777. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">5</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +<style="highlight">5</style> [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">5</style>
778. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 4 — opis] [ReUseOnSucceedAttack] <style="highlight">이번 턴과</style> 다음 턴에 [AmberResistDown] 1 부여 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061702].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [AmberResistDown]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [AmberResistDown] = 나태 내성 약화 / Sloth Resist Down
   EN: [ReUseOnSucceedAttack] Inflict 1 [AmberResistDown] <style="highlight">this turn and</style> next turn (once per turn)
   PL: [ReUseOnSucceedAttack] Nakłada 1 [AmberResistDown] <style="highlight">w tej turze i</style> w następnej turze (1 raz na turę)
779. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 끔찍한 반복 재생
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=3].name ; dataList[id=1061703].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Horribly Infinite Replay
   PL: Przerażające Nieskończone Odtwarzanie
780. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 [ChargeNoirAlly] 위력 2당 피해량 +10% (최대 30%)\n[WhenUse] (자신의 [ChargeNoirAlly] 위력 x 2)만큼 [NoirBindArmorAlly] 얻음 (스킬당 최대 10)\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 5 소모하여, 코인 위력 +1 (최대 3)\n[EndSkill] 자신에게 [TimeToListenHonglu]이 없으면, [ReadyToListenHonglu] 1 얻음 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=3].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoirAlly], [WhenUse], [NoirBindArmorAlly], [EndSkill], [TimeToListenHonglu], [ReadyToListenHonglu]
   znaczenie tagów: [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]; [NoirBindArmorAlly] = 르누아르 우스티드 원단 코트 / Le Noir: Worsted Overcoat; [EndSkill] = [공격 종료시] / [Attack End]; [TimeToListenHonglu] = 경청의 시간 / Time to Listen; [ReadyToListenHonglu] = 낭독 준비 / Ready to Narrate
   EN: Deal +10% damage for every 2 [ChargeNoirAlly] Potency on self (max 30%)\n[WhenUse] Gain ([ChargeNoirAlly] Potency on self x 2) [NoirBindArmorAlly] (max 10 per Skill)\n[WhenUse] Consume 5 [ChargeNoirAlly] Count to gain Coin Power +1 (max 3 times)\n[EndSkill] If this unit does not have [TimeToListenHonglu], gain 1 [ReadyToListenHonglu] (once per turn)
   PL: Zadaje +10% obrażeń za każde 2 Mocy [ChargeNoirAlly] (maks. 30%)\n[WhenUse] Zyskuje (2 x Moc własnego [ChargeNoirAlly]) [NoirBindArmorAlly] (maks. 10 na Umiejętność)\n[WhenUse] Zużywa 5 Licznika [ChargeNoirAlly], aby zyskać Moc Monet +1 (maks. 3 razy)\n[EndSkill] Jeżeli nie ma [TimeToListenHonglu], zyskuje 1 [ReadyToListenHonglu] (1 raz na turę)
781. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1061703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] Nakłada 3 [Vibration]
782. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1061703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Vibration] celu o 3
783. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion], 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1061703].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
784. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] 자신에게 [TimeToListenHonglu]이 있으면, 이 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1061703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 768 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [WarinessHonglu] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 769 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [ReUseOnSucceedAttack] 정신력 피해 5
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]
   EN: [ReUseOnSucceedAttack] Deal 5 SP damage
   PL: [ReUseOnSucceedAttack] Zadaje 5 obrażeń Poczytalności
787. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 4 — opis] [ReUseOnSucceedAttack] 이 코인 최종 피해량의 20%만큼 나태 피해
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ReUseOnSucceedAttack]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]
   EN: [ReUseOnSucceedAttack] Deal Sloth Damage equal to 20% of this Coin's final damage
   PL: [ReUseOnSucceedAttack] Zadaje obrażenia Lenistwa równe 20% końcowych obrażeń tej monety
788. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 [ChargeNoirAlly] 위력 2당 피해량 +10% (최대 30%)\n[WhenUse] (자신의 [ChargeNoirAlly] 위력 x <style="highlight">3</style>)만큼 [NoirBindArmorAlly] 얻음 (스킬당 최대 <style="highlight">15</style>)\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 5 소모하여, 코인 위력 +1 (최대 3)\n[EndSkill] 자신에게 [TimeToListenHonglu]이 없으면, [ReadyToListenHonglu] 1 얻음 (턴당 1회)
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeNoirAlly], [WhenUse], [NoirBindArmorAlly], [EndSkill], [TimeToListenHonglu], [ReadyToListenHonglu]
   znaczenie tagów: [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]; [NoirBindArmorAlly] = 르누아르 우스티드 원단 코트 / Le Noir: Worsted Overcoat; [EndSkill] = [공격 종료시] / [Attack End]; [TimeToListenHonglu] = 경청의 시간 / Time to Listen; [ReadyToListenHonglu] = 낭독 준비 / Ready to Narrate
   EN: Deal +10% damage for every 2 [ChargeNoirAlly] Potency on self (max 30%)\n[WhenUse] Gain ([ChargeNoirAlly] Potency on self x <style="highlight">3</style>) [NoirBindArmorAlly] (max <style="highlight">15</style> per Skill)\n[WhenUse] Consume 5 [ChargeNoirAlly] Count to gain Coin Power +1 (max 3 times)\n[EndSkill] If this unit does not have [TimeToListenHonglu], gain 1 [ReadyToListenHonglu] (once per turn)
   PL: Zadaje +10% obrażeń za każde 2 Mocy [ChargeNoirAlly] (maks. 30%)\n[WhenUse] Zyskuje (<style="highlight">3</style> x Moc własnego [ChargeNoirAlly]) [NoirBindArmorAlly] (maks. <style="highlight">15</style> na Umiejętność)\n[WhenUse] Zużywa 5 Licznika [ChargeNoirAlly], aby zyskać Moc Monet +1 (maks. 3 razy)\n[EndSkill] Jeżeli nie ma [TimeToListenHonglu], zyskuje 1 [ReadyToListenHonglu] (1 raz na turę)
789. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 [ChargeNoirAlly] 위력이 2 이상이면, [VibrationExplosion], 대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] At 2+ [ChargeNoirAlly] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL: <style="highlight">[OnSucceedAttack] Przy 2+ Mocy [ChargeNoirAlly] wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1</style>
790. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [WarinessHonglu] 1 부여<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [WarinessHonglu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [WarinessHonglu] = 경청 형벌 / Auditive Punishment
   EN: [OnSucceedAttack] Inflict 1 [WarinessHonglu]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [WarinessHonglu]<style="highlight"></style>
791. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] [ReUseOnSucceedAttack] 정신력 피해 5<style="highlight"></style>
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]
   EN: [ReUseOnSucceedAttack] Deal 5 SP damage<style="highlight"></style>
   PL: [ReUseOnSucceedAttack] Zadaje 5 obrażeń Poczytalności<style="highlight"></style>
792. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 5 — opis] [ReUseOnSucceedAttack] 이 코인 최종 피해량의 <style="highlight">30%</style>만큼 나태 피해
   źródło: Skills_personality-06.json :: dataList[id=1061703].levelList[level=4].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]
   EN: [ReUseOnSucceedAttack] Deal Sloth Damage equal to <style="highlight">30</style>% of this Coin's final damage
   PL: [ReUseOnSucceedAttack] Zadaje obrażenia Lenistwa równe <style="highlight">30</style>% końcowych obrażeń tej monety
793. [Obrona (ulepszenia 1,4) — nazwa] 안내방송
   źródło: Skills_personality-06.json :: dataList[id=1061704].levelList[level=1].name ; dataList[id=1061704].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Customer Announcement
   PL: Komunikat
794. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle] 자신에게 [SupportProtect]가 없으면, [SupportProtect] 1 얻음\n[WhenUse] 자신의 [ChargeNoirAlly] 위력만큼 [NoirBindArmorAlly] 얻음 (스킬당 최대 5)\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수 2 증가
   źródło: Skills_personality-06.json :: dataList[id=1061704].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [SupportProtect], [WhenUse], [ChargeNoirAlly], [NoirBindArmorAlly]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation; [NoirBindArmorAlly] = 르누아르 우스티드 원단 코트 / Le Noir: Worsted Overcoat
   EN: [DuelCounter]\n[StartBattle] If this unit does not have [SupportProtect], gain 1 [SupportProtect]\n[WhenUse] Gain [NoirBindArmorAlly] equal to [ChargeNoirAlly] Potency on self (max 5 per Skill)\n[WhenUse] Gain +2 [ChargeNoirAlly] Count
   PL: [DuelCounter]\n[StartBattle] Jeżeli nie ma [SupportProtect], zyskuje 1 [SupportProtect]\n[WhenUse] Zyskuje (Moc własnego [ChargeNoirAlly]) [NoirBindArmorAlly] (maks. 5 na Umiejętność)\n[WhenUse] Zwiększa własny Licznik [ChargeNoirAlly] o 2
795. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]
796. [Obrona (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-06.json :: dataList[id=1061704].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1061704].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 795 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n<style="highlight">자신의 [ChargeNoirAlly] 위력 2당 피해량 +25% (최대 75%)</style>\n[StartBattle] 자신에게 [SupportProtect]가 없으면, [SupportProtect] 1 얻음\n<style="highlight">[BeforeUse] 자신에게 [TimeToListenHonglu]이 있으면, ‘끔찍한 반복 재생’으로 발동됨 (전투당 1회)\n[WhenUse] 자신의 [ChargeNoirAlly] 위력 3당 코인 위력 +1 (최대 2)</style>\n[WhenUse] <style="highlight">(자신의 [ChargeNoirAlly] 위력 x 3)</style>만큼 [NoirBindArmorAlly] 얻음 (스킬당 최대 <style="highlight">15</style>)\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-06.json :: dataList[id=1061704].levelList[level=4].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [ChargeNoirAlly], [StartBattle], [SupportProtect], [BeforeUse], [TimeToListenHonglu], [WhenUse], [NoirBindArmorAlly]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [ChargeNoirAlly] = 보존 / Preservation; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [BeforeUse] = [사용전] / [Before Use]; [TimeToListenHonglu] = 경청의 시간 / Time to Listen; [WhenUse] = [사용시] / [On Use]; [NoirBindArmorAlly] = 르누아르 우스티드 원단 코트 / Le Noir: Worsted Overcoat
   EN: [DuelCounter]\n<style="highlight">Deal +25% damage for every 2 [ChargeNoirAlly] Potency on self (max 75%)</style>\n[StartBattle] If this unit does not have [SupportProtect], gain 1 [SupportProtect]\n<style="highlight">[BeforeUse] If this unit has [TimeToListenHonglu], activate "Horribly Infinite Replay" instead (once per Encounter)\n[WhenUse] Coin Power +1 for every 3 [ChargeNoirAlly] Potency on self (max 2)</style>\n[WhenUse] <style="highlight">Gain ([ChargeNoirAlly] Potency on self x 3) [NoirBindArmorAlly]</style> (max <style="highlight">15</style> per Skill)\n[WhenUse] Gain +<style="highlight">4</style> [ChargeNoirAlly] Count
   PL: [DuelCounter]\n<style="highlight">Zadaje +25% obrażeń za każde 2 Mocy [ChargeNoirAlly] (maks. 75%)</style>\n[StartBattle] Jeżeli nie ma [SupportProtect], zyskuje 1 [SupportProtect]\n<style="highlight">[BeforeUse] Jeżeli ma [TimeToListenHonglu], stosuje się jako „Przerażające Nieskończone Odtwarzanie” (1 raz na spotkanie)\n[WhenUse] Moc Monet +1 za każde 3 Mocy [ChargeNoirAlly] (maks. 2)</style>\n[WhenUse] <style="highlight">Zyskuje (3 x Moc własnego [ChargeNoirAlly])</style> [NoirBindArmorAlly] (maks. <style="highlight">15</style> na Umiejętność)\n[WhenUse] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">4</style>
798. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여
   źródło: Skills_personality-06.json :: dataList[id=1061704].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Vibration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Vibration]
799. [Obrona (ulepszenia 1,4) — nazwa] 경고방송
   źródło: Skills_personality-06.json :: dataList[id=1061705].levelList[level=1].name ; dataList[id=1061705].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Warning Announcement
   PL: Komunikat Ostrzegawczy
800. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 6 소모하여 다음 턴에 [SupportProtect] 1 얻음 (턴당 1회)\n[WhenUse] 자신에게 [TimeToListenHonglu]이 없으면, [ReadyToListenHonglu] 1 얻음 (턴당 1회)\n[WinDuel] 자신의 [ChargeNoirAlly] 횟수 2 증가\n[WinDuel] [VibrationExplosion], 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-06.json :: dataList[id=1061705].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [SupportProtect], [WhenUse], [ChargeNoirAlly], [TimeToListenHonglu], [ReadyToListenHonglu], [WinDuel], [VibrationExplosion], [Vibration]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation; [TimeToListenHonglu] = 경청의 시간 / Time to Listen; [ReadyToListenHonglu] = 낭독 준비 / Ready to Narrate; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst …
   EN: [CanDuelGuard]\n[SupportProtect] exclusive Skill\n[WhenUse] Consume 6 [ChargeNoirAlly] Count to gain 1 [SupportProtect] next turn (once per turn)\n[WhenUse] If this unit does not have [TimeToListenHonglu], gain 1 [ReadyToListenHonglu] (once per turn)\n[WinDuel] Gain +2 [ChargeNoirAlly] Count\n[WinDuel] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [SupportProtect]\n[WhenUse] Zużywa 6 Licznika [ChargeNoirAlly], aby zyskać 1 [SupportProtect] w następnej turze (1 raz na turę)\n[WhenUse] Jeżeli nie ma [TimeToListenHonglu], zyskuje 1 [ReadyToListenHonglu] (1 raz na turę)\n[WinDuel] Zwiększa własny Licznik [ChargeNoirAlly] o 2\n[WinDuel] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
801. [Obrona (ulepszenia 1,4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-06.json :: dataList[id=1061705].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1061705].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n<style="highlight">자신의 [ChargeNoirAlly] 위력 2당 최종 위력 +1 (최대 3)</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수를 6 소모하여 다음 턴에 [SupportProtect] 1 얻음 (턴당 1회)\n[WhenUse] 자신에게 [TimeToListenHonglu]이 없으면, [ReadyToListenHonglu] 1 얻음 (턴당 1회)\n[WinDuel] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">4</style> 증가\n[WinDuel] [VibrationExplosion], 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-06.json :: dataList[id=1061705].levelList[level=4].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [SupportProtect], [ChargeNoirAlly], [WhenUse], [TimeToListenHonglu], [ReadyToListenHonglu], [WinDuel], [VibrationExplosion], [Vibration]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]; [TimeToListenHonglu] = 경청의 시간 / Time to Listen; [ReadyToListenHonglu] = 낭독 준비 / Ready to Narrate; [WinDuel] = [합 승리시] / [Clash Win]; [VibrationExplosion] = 진동 폭발 / Tremor Burst …
   EN: [CanDuelGuard]\n[SupportProtect] exclusive Skill\n<style="highlight">Final Power +1 for every 2 [ChargeNoirAlly] Potency on self (max 3)</style>\n[WhenUse] Consume 6 [ChargeNoirAlly] Count to gain 1 [SupportProtect] next turn (once per turn)\n[WhenUse] If this unit does not have [TimeToListenHonglu], gain 1 [ReadyToListenHonglu] (once per turn)\n[WinDuel] Gain +<style="highlight">4</style> [ChargeNoirAlly] Count\n[WinDuel] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [CanDuelGuard]\nUmiejętność wyłącznie dla [SupportProtect]\n<style="highlight">Moc Końcowa +1 za każde 2 Mocy [ChargeNoirAlly] (maks. 3)</style>\n[WhenUse] Zużywa 6 Licznika [ChargeNoirAlly], aby zyskać 1 [SupportProtect] w następnej turze (1 raz na turę)\n[WhenUse] Jeżeli nie ma [TimeToListenHonglu], zyskuje 1 [ReadyToListenHonglu] (1 raz na turę)\n[WinDuel] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">4</style>\n[WinDuel] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
803. [Pasywka bojowa (od ulepszenia 1) — nazwa] 경청하셔야죠?
   źródło: Passives.json :: dataList[id=1061702].name
   limit: do 40 znaków
   EN: You Should Listen, You Know?
   PL: Posłuchacie, prawda?
804. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 중 누적으로 자신의 [ChargeNoirAlly] 횟수 10을 소모할 때마다 [ChargeNoirAlly] 위력을 1 얻음\n\n[ReadyToListenHonglu]는 턴당 1만 얻을 수 있음\n- [TimeToListenHonglu]이 있으면, [ReadyToListenHonglu]는 얻을 수 없음\n\n자신의 [ReadyToListenHonglu]가 2이면, 턴 종료시 전부 소모하여 다음 턴에 아래 효과 적용\n- [TimeToListenHonglu] 2 얻음\n- 모든 전장에 있는 적에게 [WarinessHonglu] 2 부여 (턴당 1회, 집중 전투면, 부위로 판정)
   źródło: Passives.json :: dataList[id=1061702].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoirAlly], [ReadyToListenHonglu], [TimeToListenHonglu], [WarinessHonglu]
   znaczenie tagów: [ChargeNoirAlly] = 보존 / Preservation; [ReadyToListenHonglu] = 낭독 준비 / Ready to Narrate; [TimeToListenHonglu] = 경청의 시간 / Time to Listen; [WarinessHonglu] = 경청 형벌 / Auditive Punishment
   EN: Gain 1 [ChargeNoirAlly] Potency every time this unit consumes 10 cumulative [ChargeNoirAlly] Count in this Encounter\n\nCan gain up to 1 [ReadyToListenHonglu] per turn\n- If this unit has [TimeToListenHonglu], this unit cannot gain [ReadyToListenHonglu]\n\nTurn End: At 2 [ReadyToListenHonglu], consume all Stacks and apply the following effects next turn:\n- Gain 2 [TimeToListenHonglu]\n- Inflict 2 [WarinessHonglu] on all enemies on the field (once per turn; in Focused Encounters, all Parts)
   PL: Za każde łączne zużycie 10 własnego Licznika [ChargeNoirAlly] podczas walki zyskuje 1 Mocy [ChargeNoirAlly]\n\n[ReadyToListenHonglu] można zyskać najwyżej 1 na turę\n- Jeżeli ma [TimeToListenHonglu], nie może zyskać [ReadyToListenHonglu]\n\nNa koniec tury przy 2 [ReadyToListenHonglu] zużywa wszystkie stosy, aby stosować w następnej turze poniższe efekty:\n- Zyskuje 2 [TimeToListenHonglu]\n- Nakłada 2 [WarinessHonglu] na wszystkich wrogów na polu (1 raz na turę; w walkach skupionych na wszystkich Partach)
805. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — nazwa] 르누아르 우스티드 원단
   źródło: Passives.json :: dataList[id=1061701].name
   limit: do 40 znaków
   EN: Le Noir: Worsted
   PL: Le Noir: Tkanina Czesankowa
806. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Envy) — opis] 자신의 [ChargeNoirAlly] 위력만큼 수비 스킬 합 위력 +1 (최대 5)\n\n[NoirBindArmorAlly]가 8 이상이면, ‘경고방송’으로 [ChargeNoirAlly] 횟수를 소모한 후 해당 스킬 종료 시 소모한 [ChargeNoirAlly] 횟수만큼 자신의 [ChargeNoirAlly] 횟수 증가 (턴당 1회)
   źródło: Passives.json :: dataList[id=1061701].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoirAlly], [NoirBindArmorAlly]
   znaczenie tagów: [ChargeNoirAlly] = 보존 / Preservation; [NoirBindArmorAlly] = 르누아르 우스티드 원단 코트 / Le Noir: Worsted Overcoat
   EN: Defense Skill Clash Power +1 for every [ChargeNoirAlly] Potency on self (max 5)\n\nAt 8+ [NoirBindArmorAlly], after this unit consumes [ChargeNoirAlly] Count using the "Warning Announcement" Skill, gain +([ChargeNoirAlly] Count consumed by said Skill) [ChargeNoirAlly] Count at Skill End (once per turn)
   PL: Moc Starcia Umiejętności obrony +1 za każdą Moc [ChargeNoirAlly] (maks. 5)\n\nPrzy 8+ [NoirBindArmorAlly] po zużyciu Licznika [ChargeNoirAlly] Umiejętnością „Komunikat Ostrzegawczy” zyskuje na koniec tej Umiejętności Licznik [ChargeNoirAlly] równy liczbie zużytego Licznika [ChargeNoirAlly] (1 raz na turę)
807. [Pasywka bojowa (od ulepszenia 4) — nazwa] 경청하셔야죠?
   źródło: Passives.json :: dataList[id=1061712].name
   (powtórzenie elementu 803 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Pasywka bojowa (od ulepszenia 4) — opis] 전투 중 누적으로 자신의 [ChargeNoirAlly] 횟수 10을 소모할 때마다 [ChargeNoirAlly] 위력을 1 얻음\n\n[ReadyToListenHonglu]는 턴당 1만 얻을 수 있음\n- [TimeToListenHonglu]이 있으면, [ReadyToListenHonglu]는 얻을 수 없음\n\n자신의 [ReadyToListenHonglu]가 2이면, 턴 종료시 전부 소모하여 다음 턴에 아래 효과 적용\n- [TimeToListenHonglu] 2 얻음\n- 모든 전장에 있는 적에게 [WarinessHonglu] 2 부여 (턴당 1회, 집중 전투면, 부위로 판정)\n<style="highlight">- ‘안내방송’의 사용전 효과의 사용 횟수 초기화</style>
   źródło: Passives.json :: dataList[id=1061712].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [ChargeNoirAlly], [ReadyToListenHonglu], [TimeToListenHonglu], [WarinessHonglu]
   znaczenie tagów: [ChargeNoirAlly] = 보존 / Preservation; [ReadyToListenHonglu] = 낭독 준비 / Ready to Narrate; [TimeToListenHonglu] = 경청의 시간 / Time to Listen; [WarinessHonglu] = 경청 형벌 / Auditive Punishment
   EN: Gain 1 [ChargeNoirAlly] Potency every time this unit consumes 10 cumulative [ChargeNoirAlly] Count in this Encounter\n\nCan gain up to 1 [ReadyToListenHonglu] per turn\n- If this unit has [TimeToListenHonglu], this unit cannot gain [ReadyToListenHonglu]\n\nTurn End: At 2 [ReadyToListenHonglu], consume all Stacks and apply the following effects next turn:\n- Gain 2 [TimeToListenHonglu]\n- Inflict 2 [WarinessHonglu] on all enemies on the field (once per turn; in Focused Encounters, all Parts)\n<style="highlight">- Reset the activation limit on the "Before Use" effect on the "Customer Announcement" Skill</style>
   PL: Za każde łączne zużycie 10 własnego Licznika [ChargeNoirAlly] podczas walki zyskuje 1 Mocy [ChargeNoirAlly]\n\n[ReadyToListenHonglu] można zyskać najwyżej 1 na turę\n- Jeżeli ma [TimeToListenHonglu], nie może zyskać [ReadyToListenHonglu]\n\nNa koniec tury przy 2 [ReadyToListenHonglu] zużywa wszystkie stosy, aby stosować w następnej turze poniższe efekty:\n- Zyskuje 2 [TimeToListenHonglu]\n- Nakłada 2 [WarinessHonglu] na wszystkich wrogów na polu (1 raz na turę; w walkach skupionych na wszystkich Partach)\n<style="highlight">- Resetuje limit aktywacji efektu przed użyciem Umiejętności „Komunikat”</style>
809. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — nazwa] 담요 덮어주기
   źródło: Passives.json :: dataList[id=1061721].name
   limit: do 40 znaków
   EN: Tuck Them Under a Blanket
   PL: Okrycie Kocem
810. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — opis] 이번 턴 중 [SupportProtect] 전용 스킬을 가장 먼저 사용한 인격이 해당 스킬 사용 시 [Protection] 1 얻음 (턴당 1회)
   źródło: Passives.json :: dataList[id=1061721].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [SupportProtect], [Protection]
   znaczenie tagów: [SupportProtect] = 원호 방어 / Assist Defense; [Protection] = 보호 / Protection
   EN: The first Identity to use an [SupportProtect] exclusive Skill in a turn gains 1 [Protection] on said Skill Use (once per turn)
   PL: Tożsamość, która jako pierwsza użyje w turze Umiejętności wyłącznie dla [SupportProtect], zyskuje przy jej użyciu 1 [Protection] (1 raz na turę)

## [?] Early Elephants Sinnerling — Hong Lu — 코끼리반 수감생
- ID Tożsamości: `400030` (plik: `Personalities-x1p1c1.json`)

811. [Karta Tożsamości — tytuł] 코끼리반 수감생
   źródło: Personalities-x1p1c1.json :: dataList[id=400030].title
   limit: do 40 znaków
   EN: Early Elephants Sinnerling
   PL: Grzeszniczek Grupy Słoników
812. [Karta Tożsamości — nazwa] 홍루
   źródło: Personalities-x1p1c1.json :: dataList[id=400030].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [Karta Tożsamości — nazwa z tytułem] 홍루
   źródło: Personalities-x1p1c1.json :: dataList[id=400030].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Karta Tożsamości — opis] 홍루의 ??? 인격
   źródło: Personalities-x1p1c1.json :: dataList[id=400030].desc
   limit: do 120 znaków
   EN: Hong Lu's ??? Identity
   PL: ??? Tożsamość Hong Lu
815. [Pasywka bojowa [40003001] — nazwa] 유희
   źródło: Passives-x1p1c1.json :: dataList[id=40003001].name
   limit: do 40 znaków
   EN: Entewtainment
   PL: — nazwa] Rozrywka
816. [Pasywka bojowa [40003001] — opis] 다음 턴 시작 시 정신력 6 회복
   źródło: Passives-x1p1c1.json :: dataList[id=40003001].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Pasywka bojowa [40003002] — nazwa] 씰없는 농담
   źródło: Passives-x1p1c1.json :: dataList[id=40003002].name
   limit: do 40 znaków
   EN: Fwivowous Jokes
   PL: — nazwa] Bezsensowne Żarciki
818. [Pasywka bojowa [40003002] — opis] 정신력이 가장 낮은 아군 1명 전투 시작 시 정신력 6 회복
   źródło: Passives-x1p1c1.json :: dataList[id=40003002].desc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
