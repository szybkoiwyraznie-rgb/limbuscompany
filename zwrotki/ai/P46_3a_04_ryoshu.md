# Paczka AI P46 (Fala 3 · 3A) — Grzesznik 04 — Ryōshū

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P46_3a_04_ryoshu.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P46_3a_04_ryoshu.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Grzesznik #04: Ryōshū (료슈)
- Imię postaci i oficjalne akta osobowe wyświetlane w profilu więźnia.

1. [Grzesznik — nazwa] 료슈
   źródło: Characters.json :: dataList[id=4].name
   limit: do 40 znaków
   EN: Ryōshū
   PL: Ryōshū
2. [Akta więźnia — nazwa] 료슈
   źródło: IntroduceCharacter.json :: dataList[id=료슈].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [0] LCB Sinner — Ryōshū — LCB 수감자
- ID Tożsamości: `10401` (plik: `Personalities.json`)
- parametry karty: rzadkość `0` · sezon: 0 · HP bazowe: 66 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Poise

3. [Karta Tożsamości — tytuł] LCB\n수감자
   źródło: Personalities.json :: dataList[id=10401].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB\nSinner
   PL: LCB\nGrzesznik
4. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10401].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
5. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10401].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
6. [Karta Tożsamości — opis] 료슈의 첫번째 인격
   źródło: Personalities.json :: dataList[id=10401].desc
   limit: do 120 znaków
   EN: Ryōshū’s 1st Identity
   PL: Pierwsza Tożsamość Ryōshū
7. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 칠하기
   źródło: Skills.json :: dataList[id=1040101].levelList[level=1].name ; dataList[id=1040101].levelList[level=2].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Paint
   PL: Malowanie
8. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 호흡 1 얻음
   źródło: Skills.json :: dataList[id=1040101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain 1 [Breath] next turn
   PL: [OnSucceedAttackHead] Zyskuje w następnej turze 1 Oddechu
9. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1040101].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath] next turn
   PL: [OnSucceedAttack] Zyskuje w następnej turze 2 [Breath]
10. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 흩뿌리기
   źródło: Skills.json :: dataList[id=1040102].levelList[level=1].name ; dataList[id=1040102].levelList[level=2].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Splatter
   PL: Pryskanie
11. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] 대상이 이번 턴에 피해를 받은 상태면 피해량 +10%
   źródło: Skills.json :: dataList[id=1040102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: If target previously took damage this turn, deal +10% damage
   PL: Jeżeli cel otrzymał już w tej turze obrażenia, zadaje +10% obrażeń
12. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] 대상이 이번 턴에 피해를 받은 상태면 피해량 +10%
   źródło: Skills.json :: dataList[id=1040102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
13. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] 대상이 이번 턴에 피해를 받은 상태면 피해량 +30%
   źródło: Skills.json :: dataList[id=1040102].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: If target previously took damage this turn, deal +30% damage
   PL: Jeżeli cel otrzymał już w tej turze obrażenia, zadaje +30% obrażeń
14. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] 대상이 이번 턴에 피해를 받은 상태면 피해량 +30%
   źródło: Skills.json :: dataList[id=1040102].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
15. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 그려내기
   źródło: Skills.json :: dataList[id=1040103].levelList[level=3].name ; dataList[id=1040103].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Brushstroke
   PL: Pociągnięcie Pędzla
16. [Umiejętność 3 (×1) (ulepszenia 3–4) — opis] [StartBattle] 참격 피해량 증가 2를 얻음
   źródło: Skills.json :: dataList[id=1040103].levelList[level=3].desc ; dataList[id=1040103].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [StartBattle] Gain 2 Slash DMG Up
   PL: [StartBattle] Zyskuje 2 Wzrost Obrażeń Cięcia
17. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 호흡 2 얻음
   źródło: Skills.json :: dataList[id=1040103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [Obrona (ulepszenie 1) — nazwa] 회피
   źródło: Skills.json :: dataList[id=1040104].levelList[level=1].name
   kontekst: grzech: Glut. · typ: obrona: unik · moc bazowa: 2 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Evade
   PL: Unik
19. [Pasywka bojowa (od ulepszenia 1, rezonans 3× Glut.) — nazwa] 무차별적 예술
   źródło: Passives.json :: dataList[id=1040101].name
   limit: do 40 znaków
   EN: Indiscriminate Art
   PL: Sztuka bez Refleksji
20. [Pasywka bojowa (od ulepszenia 1, rezonans 3× Glut.) — opis] 자신이 받는 피해량 +25%. 가하는 피해량 +25%
   źródło: Passives.json :: dataList[id=1040101].desc
   limit: do 120 znaków
   EN: Deal and take +25% damage.
   PL: Zadaje i otrzymuje +25% obrażeń.
21. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — nazwa] 등떠밀기
   źródło: Passives.json :: dataList[id=1040121].name
   limit: do 40 znaków
   EN: Hustle
   PL: Najście
22. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Glut.) — opis] 최대 체력이 가장 낮은 아군 1명 가하는 피해량 +20%, 받는 피해량 +20%
   źródło: Passives.json :: dataList[id=1040121].desc
   limit: do 120 znaków
   EN: 1 ally with the lowest Max HP deals and takes +20% damage.
   PL: 1 Sojusznik z najniższym Maks. HP zadaje i otrzymuje +20% obrażeń.

## [00] Seven Assoc. South Section 6 — Ryōshū — 남부 세븐 협회 6과
- ID Tożsamości: `10402` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 63 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture

23. [Karta Tożsamości — tytuł] 남부 세븐 협회\n6과
   źródło: Personalities.json :: dataList[id=10402].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Seven Assoc.\nSouth Section 6
   PL: Południowe Stowarzyszenie Seven\nSekcja 6
24. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10402].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
25. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10402].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
26. [Karta Tożsamości — opis] 료슈의 두번째 인격
   źródło: Personalities.json :: dataList[id=10402].desc
   limit: do 120 znaków
   EN: Ryōshū’s 2nd Identity
   PL: Druga Tożsamość Ryōshū
27. [Umiejętność 1 (×3) (ulepszenia 1–2) — nazwa] 슬래시
   źródło: Skills.json :: dataList[id=1040201].levelList[level=1].name ; dataList[id=1040201].levelList[level=2].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Slash
   PL: Cięcie
28. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 파열 2 부여
   źródło: Skills.json :: dataList[id=1040201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Rupture
   PL: [OnSucceedAttackHead] Nakłada 2 Rozdarcia
29. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 파열 2 부여
   źródło: Skills.json :: dataList[id=1040201].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Rupture
   PL: [OnSucceedAttack] Nakłada 2 Rozdarcia
30. [Umiejętność 2 (×2) (ulepszenia 1–2) — nazwa] 어퍼 슬래시
   źródło: Skills.json :: dataList[id=1040202].levelList[level=1].name ; dataList[id=1040202].levelList[level=2].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 1 (+14)
   limit: do 40 znaków
   EN: Upper Slash
   PL: Cięcie od Góry
31. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WinDuel] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills.json :: dataList[id=1040202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Gain 1 Attack Power Up next turn
   PL: [WinDuel] Zyskuje w następnej turze 1 Wzrost Mocy Ataku
32. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1040202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Defense Level Down
   PL: [OnSucceedAttackHead] Nakłada 2 Spadku Poziomu Obrony
33. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상에게 참격 취약 이 있으면 스킬 위력 +2\n[WinDuel] 다음 턴에 공격 위력 증가 1 얻음
   źródło: Skills.json :: dataList[id=1040202].levelList[level=2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: Skill Power +2 against units that have Slash Fragility\n[WinDuel] Gain 1 Attack Power Up next turn
   PL: Moc Umiejętności +2 wobec jednostek z Wrażliwością na Cięcie\n[WinDuel] Zyskuje w następnej turze 1 Wzrost Mocy Ataku
34. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 방어 레벨 감소 2 부여
   źródło: Skills.json :: dataList[id=1040202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Defense Level Down
   PL: [OnSucceedAttack] Nakłada 2 Spadku Poziomu Obrony
35. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 스워시
   źródło: Skills.json :: dataList[id=1040203].levelList[level=3].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Swash
   PL: Zamaszyste Cięcie
36. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WinDuel] 이 스킬에서 부여하는 참격 취약 2 추가 부여
   źródło: Skills.json :: dataList[id=1040203].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] This skill inflicts 2 additional Slash Fragility
   PL: [WinDuel] Ta Umiejętność nakłada o 2 więcej Wrażliwości na Cięcie
37. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 참격 취약 3 부여
   źródło: Skills.json :: dataList[id=1040203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Slash Fragility next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 3 Wrażliwości na Cięcie
38. [Obrona (ulepszenia 1,4) — nazwa] 반격
   źródło: Skills.json :: dataList[id=1040204].levelList[level=1].name ; dataList[id=1040204].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 8 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Counter
   PL: Kontra
39. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 참격 취약 1 부여
   źródło: Skills.json :: dataList[id=1040204].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Slash Fragility
   PL: [OnSucceedAttack] Nakłada 1 Wrażliwości na Cięcie
40. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — nazwa] 반.갈
   źródło: Passives.json :: dataList[id=1040201].name
   limit: do 40 znaków
   EN: C. I. H.
   PL: C. I. H.
41. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Glut.) — opis] 이번 턴 참격 피해량 +10%
   źródło: Passives.json :: dataList[id=1040201].desc
   limit: do 120 znaków
   EN: Deal +10% Slash damage this turn.
   PL: Zadaje +10% obrażeń Cięcia w tej turze.
42. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — nazwa] 아이스 브레이킹
   źródło: Passives.json :: dataList[id=1040221].name
   limit: do 40 znaków
   EN: Ice Breaker
   PL: Przebijający Lód
43. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Glut.) — opis] 최대 체력이 가장 낮은 아군 1명 파열 부여 값 +1
   źródło: Passives.json :: dataList[id=1040221].desc
   limit: do 120 znaków
   EN: 1 ally that has the lowest Max HP inflicts +1 Rupture
   PL: 1 Sojusznik z najniższym Maks. HP nakłada o 1 więcej Rozdarcia

## [000] Kurokumo Clan Wakashu — Ryōshū — 흑운회 와카슈
- ID Tożsamości: `10403` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 73 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Bleed

44. [Karta Tożsamości — tytuł] 흑운회\n와카슈
   źródło: Personalities.json :: dataList[id=10403].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Kurokumo Clan\nWakashu
   PL: Klan Kurokumo\nWakashu
45. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10403].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
46. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10403].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Karta Tożsamości — opis] 료슈의 세번째 인격
   źródło: Personalities.json :: dataList[id=10403].desc
   limit: do 120 znaków
   EN: Ryōshū’s 3rd Identity
   PL: Trzecia Tożsamość Ryōshū
48. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 발경
   źródło: Skills.json :: dataList[id=1040301].levelList[level=1].name ; dataList[id=1040301].levelList[level=2].name ; dataList[id=1040301].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 5 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Focus Strike
   PL: Skupione Uderzenie
49. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마비 1 부여
   źródło: Skills.json :: dataList[id=1040301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Paralyze
   PL: [OnSucceedAttackHead] Nakłada 1 Paraliżu
50. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 마비 3 부여
   źródło: Skills.json :: dataList[id=1040301].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Paralyze
   PL: [OnSucceedAttack] Nakłada 3 Paraliżu
51. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 출혈 횟수가 2 이상이면, 피해량 +20%
   źródło: Skills.json :: dataList[id=1040301].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target has 2+ Bleed Count, deal +20% damage
   PL: Jeżeli cel ma 2+ Licznika Krwawienia, zadaje +20% obrażeń
52. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 뒷처리
   źródło: Skills.json :: dataList[id=1040302].levelList[level=1].name ; dataList[id=1040302].levelList[level=2].name ; dataList[id=1040302].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 5 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Clean Up
   PL: Posprzątanie
53. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1040302].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1040302].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Bleed
   PL: [OnSucceedAttack] Nakłada 2 Krwawienia
54. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1040302].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Bleed Count
   PL: [OnSucceedAttackHead] Nakłada +1 Licznika Krwawienia
55. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 피해량 감소 2 부여
   źródło: Skills.json :: dataList[id=1040302].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1040302].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Damage Down
   PL: [OnSucceedAttackHead] Nakłada 2 Spadku Obrażeń
56. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 출혈 횟수가 5 이상이면, 피해량 +20%
   źródło: Skills.json :: dataList[id=1040302].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target has 5+ Bleed Count, deal +20% damage
   PL: Jeżeli cel ma 5+ Licznika Krwawienia, zadaje +20% obrażeń
57. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills.json :: dataList[id=1040302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Bleed Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika Krwawienia
58. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 구름 휘젓기
   źródło: Skills.json :: dataList[id=1040303].levelList[level=3].name ; dataList[id=1040303].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 8 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Lenticular Swirl
   PL: Wir Soczewki Chmur
59. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1040303].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1040303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed
   PL: [OnSucceedAttackHead] Nakłada 2 Krwawienia
60. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills.json :: dataList[id=1040303].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1040303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 공격 레벨 감소 5 부여
   źródło: Skills.json :: dataList[id=1040303].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1040303].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Offense Level Down
   PL: [OnSucceedAttack] Nakłada 5 Spadku Poziomu Ataku
62. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 출혈 횟수가 9 이상이면, 피해량 +40%
   źródło: Skills.json :: dataList[id=1040303].levelList[level=4].desc
   limit: do 120 znaków
   EN: If target has 9+ Bleed Count, deal +40% damage
   PL: Jeżeli cel ma 9+ Licznika Krwawienia, zadaje +40% obrażeń
63. [Obrona (ulepszenie 1) — nazwa] 가드
   źródło: Skills.json :: dataList[id=1040304].levelList[level=1].name
   kontekst: grzech: Lust · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+6)
   limit: do 40 znaków
   EN: Guard
   PL: Garda
64. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — nazwa] 흑운도
   źródło: Passives.json :: dataList[id=1040301].name
   limit: do 40 znaków
   EN: Kokuuntō
   PL: Klinga Czarnego Obłoku
65. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Lust) — opis] [Laceration]이 부여된 적 공격 시 피해량 +10 %
   źródło: Passives.json :: dataList[id=1040301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Deal +10% damage to targets that have [Laceration]
   PL: Zadaje +10% obrażeń celom z [Laceration]
66. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — nazwa] 행동대장
   źródło: Passives.json :: dataList[id=1040321].name
   limit: do 40 znaków
   EN: Muscle in Charge
   PL: Mięśnie z Nakazem Władzy
67. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Lust) — opis] 속도가 가장 높은 아군 1명 출혈 부여 값 +1
   źródło: Passives.json :: dataList[id=1040321].desc
   limit: do 120 znaków
   EN: 1 ally with the fastest Speed inflicts +1 Bleed
   PL: 1 Sojusznik z najwyższą Szybkością nakłada o 1 więcej Krwawienia

## [000] R.B. Chef de Cuisine — Ryōshū — 료. 고. 파. 주방장
- ID Tożsamości: `10404` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 1 · HP bazowe: 70 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Bleed

68. [Karta Tożsamości — tytuł] 료. 고. 파.\n주방장
   źródło: Personalities.json :: dataList[id=10404].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: R.B.\nChef de Cuisine
   PL: R. B.\nSzef Kuchni
69. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10404].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10404].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
71. [Karta Tożsamości — opis] 료슈의 네번째 인격
   źródło: Personalities.json :: dataList[id=10404].desc
   limit: do 120 znaków
   EN: Ryōshū’s 4th Identity
   PL: Czwarta Tożsamość Ryōshū
72. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 요.준
   źródło: Skills.json :: dataList[id=1040401].levelList[level=1].name ; dataList[id=1040401].levelList[level=2].name ; dataList[id=1040401].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 2 (+3)
   limit: do 40 znaków
   EN: P.C.
   PL: P. C.
73. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1040401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 갈증 1 얻음
   źródło: Skills.json :: dataList[id=1040401].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040401].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Appetite
   PL: [OnSucceedAttack] Zyskuje 1 Pragnienia
75. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 출혈 횟수 1 증가
   źródło: Skills.json :: dataList[id=1040401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +1 Bleed Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika Krwawienia
76. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 갈증 2 얻음
   źródło: Skills.json :: dataList[id=1040401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 Appetite
   PL: [OnSucceedAttack] Zyskuje 2 Pragnienia
77. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 재.사
   źródło: Skills.json :: dataList[id=1040402].levelList[level=1].name ; dataList[id=1040402].levelList[level=2].name ; dataList[id=1040402].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 3 · monety: 3 (+5)
   limit: do 40 znaków
   EN: I.H.
   PL: I. H.
78. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1040402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bind next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 Spętania
79. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 1 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed
   PL: [OnSucceedAttackHead] Nakłada 1 Krwawienia
80. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈 또는 마비 가 있으면 다음 턴에 체력 회복 감소 1 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed or Paralyze, inflict 1 HP Healing Down next turn
   PL: [OnSucceedAttack] Jeżeli cel ma Krwawienie lub Paraliż, nakłada w następnej turze 1 Spadku Leczenia HP
81. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 2 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈 또는 마비 가 있으면 다음 턴에 체력 회복 감소 3 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed or Paralyze, inflict 3 HP Healing Down next turn
   PL: [OnSucceedAttack] Jeżeli cel ma Krwawienie lub Paraliż, nakłada w następnej turze 3 Spadku Leczenia HP
83. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 갈증 1 얻음
   źródło: Skills.json :: dataList[id=1040402].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 1 Appetite
   PL: [WhenUse] Zyskuje 1 Pragnienia
84. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 출혈 3 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Bleed
   PL: [OnSucceedAttackHead] Nakłada 3 Krwawienia
85. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상에게 출혈 또는 마비 가 있으면 다음 턴에 체력 회복 감소 4 부여
   źródło: Skills.json :: dataList[id=1040402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target has Bleed or Paralyze, inflict 4 HP Healing Down next turn
   PL: [OnSucceedAttack] Jeżeli cel ma Krwawienie lub Paraliż, nakłada w następnej turze 4 Spadku Leczenia HP
86. [Umiejętność 3 (×1) (ulepszenie 3) — nazwa] 무엇이든 요리할 수 있지
   źródło: Skills.json :: dataList[id=1040403].levelList[level=3].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 4 (+3)
   limit: do 40 znaków
   EN: I Can Cook Anything
   PL: Ugotuję Wszystko
87. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 잃은 체력의 5%만큼 피해량이 증가함 (최대 20)
   źródło: Skills.json :: dataList[id=1040403].levelList[level=3].desc
   limit: do 120 znaków
   EN: Boost damage by 5% of target’s missing HP (Max 20)
   PL: Zadaje obrażenia zwiększone o 5% brakującego HP celu (maks. 20)
88. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 10% 증가
   źródło: Skills.json :: dataList[id=1040403].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] The final Coin deals +10% damage
   PL: [OnSucceedAttackHead] Ostatnia Moneta zadaje +10% obrażeń
89. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 5% 증가
   źródło: Skills.json :: dataList[id=1040403].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] The final Coin deals +5% damage
   PL: [OnSucceedAttackHead] Ostatnia Moneta zadaje +5% obrażeń
90. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 5% 증가
   źródło: Skills.json :: dataList[id=1040403].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Obrona (ulepszenie 1) — nazwa] 신.재 발견
   źródło: Skills.json :: dataList[id=1040404].levelList[level=1].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: F.I. in Sight
   PL: F. I. w Zasięgu
92. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 신속 1 얻음
   źródło: Skills.json :: dataList[id=1040404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Gain 1 Haste next turn
   PL: [OnSucceedEvade] Zyskuje w następnej turze 1 Pośpiechu
93. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Lust) — nazwa] 즉흥 조리
   źródło: Passives.json :: dataList[id=1040401].name
   limit: do 40 znaków
   EN: Rustle Up
   PL: Ruch Kuchenny
94. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Lust) — opis] 적 처치 시 체력이 가장 낮은 아군 1명의 체력 15 회복 (턴 당 1회 발동).\n갈증 이 있는 경우 전부 소모하고, 소모한 갈증 에 비례하여 체력 회복량 증가.
   źródło: Passives.json :: dataList[id=1040401].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: After defeating an enemy, heal the ally with the least HP for 15 HP. (Once per turn.)\nIf this unit has an Appetite, spend it to boost the healing based on its Count.
   PL: Po pokonaniu wroga odzyskuje 15 HP Sojusznik z najmniejszym HP. (1 raz na turę.)\nJeżeli ma Pragnienie, zużywa je w całości, a odzysk HP rośnie proporcjonalnie do zużytego Pragnienia.
95. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — nazwa] 예술적인 맛
   źródło: Passives.json :: dataList[id=1040421].name
   limit: do 40 znaków
   EN: Artistic Flavor
   PL: Artystyczny Smak
96. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Lust) — opis] 적 사망 시 체력이 가장 낮은 아군 1명의 체력 15 회복. (턴 당 1회 발동)
   źródło: Passives.json :: dataList[id=1040421].desc
   limit: do 120 znaków
   EN: When an enemy is defeated, the ally with the least HP heals 15 HP. (Once per turn.)
   PL: Gdy wróg ginie, 1 Sojusznik z najmniejszym HP odzyskuje 15 HP. (1 raz na turę.)

## [000] W Corp. L3 Cleanup Agent — Ryōshū — W사 3등급 정리 요원
- ID Tożsamości: `10405` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 0 · HP bazowe: 66 · szybkość: 2–5 / 2–6 / 3–6 / 3–6
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Charge

97. [Karta Tożsamości — tytuł] W사 3등급\n정리 요원
   źródło: Personalities.json :: dataList[id=10405].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. L3\nCleanup Agent
   PL: W Corp. L3\nAgentka Oczyszczania
98. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10405].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10405].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Karta Tożsamości — opis] 료슈의 다섯번째 인격
   źródło: Personalities.json :: dataList[id=10405].desc
   limit: do 120 znaków
   EN: Ryōshū’s 5th Identity
   PL: Piąta Tożsamość Ryōshū
101. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 에.순
   źródło: Skills_personality-04.json :: dataList[id=1040501].levelList[level=1].name ; dataList[id=1040501].levelList[level=2].name ; dataList[id=1040501].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 3 (+2)
   limit: do 40 znaków
   EN: E.C.
   PL: E. C.
102. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040501].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1040501].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain +2 Charge Count
   PL: [OnSucceedAttack] Zyskuje +2 Licznika Ładowania
103. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 충전 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040501].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1040501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 충전 횟수가 10 이상이면, 피해량 +10%
   źródło: Skills_personality-04.json :: dataList[id=1040501].levelList[level=2].desc
   limit: do 120 znaków
   EN: At 10+ Charge Count, deal +10% damage
   PL: Przy 10+ Licznikach Ładowania zadaje +10% obrażeń
105. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 충전 횟수가 10 이상이면, 피해량 +10%\n충전 횟수가 15 이상이면, 추가로 피해량 +10%
   źródło: Skills_personality-04.json :: dataList[id=1040501].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 10+ Charge Count, deal +10% damage\nAt 15+ Charge Count, deal additional +10% damage
   PL: Przy 10+ Licznikach Ładowania zadaje +10% obrażeń\nPrzy 15+ Licznikach Ładowania zadaje dodatkowo +10% obrażeń
106. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 도약
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=1].name ; dataList[id=1040502].levelList[level=2].name ; dataList[id=1040502].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 2 · monety: 3 (+5)
   limit: do 40 znaków
   EN: Leap
   PL: Skok
107. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 충전 횟수 5 증가
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +5 Charge Count
   PL: [WhenUse] Zyskuje +5 Licznika Ładowania
108. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 충전 횟수가 10 이상이면, 참격 취약 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] At 10+ Charge Count, inflict 1 Slash Fragility
   PL: [OnSucceedAttackHead] Przy 10+ Licznikach Ładowania nakłada 1 Wrażliwości na Cięcie
109. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 체력이 30% 미만이면, 피해량 15% 증가
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target’s HP is below 30%, deal +15% damage
   PL: [OnSucceedAttack] Jeżeli HP celu jest poniżej 30%, zadaje +15% obrażeń
110. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 충전 횟수 6 증가\n충전 횟수가 10 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +6 Charge Count\nAt 10+ Charge Count, gain +1 Coin Power
   PL: [WhenUse] Zyskuje +6 Licznika Ładowania\nPrzy 10+ Licznika Ładowania Moc Monet +1
111. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 충전 횟수가 10 이상이면, 참격 취약 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Charge Count, inflict 1 Slash Fragility
   PL: [OnSucceedAttack] Przy 10+ Licznikach Ładowania nakłada 1 Wrażliwości na Cięcie
112. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 체력이 30% 미만이면, 피해량 20% 증가
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target’s HP is below 30%, deal +20% damage
   PL: [OnSucceedAttack] Jeżeli HP celu jest poniżej 30%, zadaje +20% obrażeń
113. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [EnemyKill] 다음 턴에 신속 1을 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Gain 1 Haste next turn
   PL: [EnemyKill] Zyskuje w następnej turze 1 Pośpiechu
114. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 충전 횟수 7 증가\n충전 횟수가 10 이상이면, 코인 위력 +1\n충전 횟수가 15 이상이면, 추가로 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +7 Charge Count\nAt 10+ Charge Count, gain +1 Coin Power\nAt 15+ Charge Count, gain additional +1 Coin Power
   PL: [WhenUse] Zyskuje +7 Licznika Ładowania\nPrzy 10+ Licznikach Ładowania Moc Monet +1\nPrzy 15+ Licznikach Ładowania dodatkowo Moc Monet +1
115. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 충전 횟수가 10 이상이면, 참격 취약 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Charge Count, inflict 2 Slash Fragility
   PL: [OnSucceedAttack] Przy 10+ Licznikach Ładowania nakłada 2 Wrażliwości na Cięcie
116. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 체력이 30% 미만이면, 피해량 30% 증가
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target’s HP is below 30%, deal +30% damage
   PL: [OnSucceedAttack] Jeżeli HP celu jest poniżej 30%, zadaje +30% obrażeń
117. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [EnemyKill] 다음 턴에 신속 3을 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040502].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] Gain 3 Haste next turn
   PL: [EnemyKill] Zyskuje w następnej turze 3 Pośpiechu
118. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 차.마.공.절
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=3].name ; dataList[id=1040503].levelList[level=4].name
   kontekst: grzech: Envy · typ: Slash · moc bazowa: 3 · monety: 4 (+2)
   limit: do 40 znaków
   EN: D.D.E.D.R.
   PL: D. D. E. D. R.
119. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 충전 횟수가 7 이상, 15 미만이면,\n보유한 충전 횟수를 전부 소모하고,\n최대 체력의 3 x (15 - 소모한 충전 횟수)%만큼 체력을 소모하여 코인 위력 +3\n[WhenUse] 충전 횟수를 15 소모하여 코인 위력 +3
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=3].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At 7~14 Charge Count\nConsume all Charge Count,\nAnd consume 3 x (15 - Charge Count Consumed)% HP to gain +3 Coin Power\n[WhenUse] Consume 15 Charge Count to gain +3 Coin Power
   PL: [WhenUse] Przy 7–14 Licznikach Ładowania\nzużywa całe posiadane Ładowanie,\npo czym zużywa HP równe 3 x (15 - zużyte Ładowanie)% Maks. HP, aby zyskać Moc Monet +3\n[WhenUse] Zużywa 15 Licznika Ładowania, aby zyskać Moc Monet +3
120. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +5%
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] The final Coin deals +5% damage
   PL: [OnSucceedAttackHead] Ostatnia Moneta zadaje +5% obrażeń
121. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +5%
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +5%
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [EnemyKill] 스킬 사용시 충전 횟수를 15 소모했다면, 자신과 자신을 제외한 무작위 아군 1명에게 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 5 부여
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] If the skill consumed 15 Charge Count upon use, apply 5 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> to self and 1 other ally
   PL: [EnemyKill] Jeżeli Umiejętność zużyła przy użyciu 15 Licznika Ładowania, nakłada 5 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Barier Ładunku</link></u></color> na siebie i 1 losowego sojusznika
124. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 충전 횟수가 7 이상, 15 미만이면,\n보유한 충전 횟수를 전부 소모하고,\n최대 체력의 3 x (15 - 소모한 충전 횟수)%만큼 체력을 소모하여 코인 위력 +5\n[WhenUse] 충전 횟수를 15 소모하여 코인 위력 +5
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=4].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] At 7~14 Charge Count\nConsume all Charge Count,\nAnd consume 3 x (15 - Charge Count Consumed)% HP to gain +5 Coin Power\n[WhenUse] Consume 15 Charge Count to gain +5 Coin Power
   PL: [WhenUse] Przy 7–14 Licznikach Ładowania\nzużywa całe posiadane Ładowanie,\npo czym zużywa HP równe 3 x (15 - zużyte Ładowanie)% Maks. HP, aby zyskać Moc Monet +5\n[WhenUse] Zużywa 15 Licznika Ładowania, aby zyskać Moc Monet +5
125. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] The final Coin deals +10% damage
   PL: [OnSucceedAttackHead] Ostatnia Moneta zadaje +10% obrażeń
126. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 마지막 코인의 피해량 +10%
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [EnemyKill] 스킬 사용시 충전 횟수를 15 소모했다면, 자신과 자신을 제외한 무작위 아군 1명에게 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">충전 역장</color></link></u> 7 부여
   źródło: Skills_personality-04.json :: dataList[id=1040503].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <sprite name="ChargeForceField">, <color=#f8c200>, <u>, <link="ChargeForceField">, </color>, </link>, </u>, [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] If the skill consumed 15 Charge Count upon use, apply 7 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Charge Barrier</color></link></u> to self and 1 other ally
   PL: [EnemyKill] Jeżeli Umiejętność zużyła przy użyciu 15 Licznika Ładowania, nakłada 7 <sprite name="ChargeForceField"><color=#f8c200><u><link="ChargeForceField">Barier Ładunku</link></u></color> na siebie i 1 losowego sojusznika
129. [Obrona (ulepszenia 1,4) — nazwa] 충전 회피
   źródło: Skills_personality-04.json :: dataList[id=1040504].levelList[level=1].name ; dataList[id=1040504].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Charged Evade
   PL: Unik z Ładowaniem
130. [Obrona (ulepszenie 1) — opis] 충전 횟수 5당 기본 위력 +1 (최대 2)
   źródło: Skills_personality-04.json :: dataList[id=1040504].levelList[level=1].desc
   limit: do 120 znaków
   EN: Base Power +1 per 5 Charge Count (max 2)
   PL: Moc Bazowa +1 za każde 5 Licznika Ładowania (maks. 2)
131. [Obrona (ulepszenie 4) — opis] 충전 횟수 5당 기본 위력 +1 (최대 3)
   źródło: Skills_personality-04.json :: dataList[id=1040504].levelList[level=4].desc
   limit: do 120 znaków
   EN: Base Power +1 per 5 Charge Count (max 3)
   PL: Moc Bazowa +1 za każde 5 Licznika Ładowania (maks. 3)
132. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — nazwa] 차원 마검
   źródło: Passives.json :: dataList[id=1040501].name
   limit: do 40 znaków
   EN: Dimensional Demon Edge
   PL: Wymienny Ostrze Demonów
133. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — opis] 적 처치 시 충전 횟수 2 증가 (턴 당 최대 3회 발동)
   źródło: Passives.json :: dataList[id=1040501].desc
   limit: do 120 znaków
   EN: Upon defeating an enemy, gain +2 Charge Count (3 times per turn)
   PL: Po pokonaniu wroga zyskuje +2 Licznika Ładowania (maks. 3 razy na turę)
134. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — nazwa] 차원 굴절 칼날 - Type: Blade Mk7
   źródło: Passives.json :: dataList[id=1040521].name
   limit: do 70 znaków
   EN: Dimensional Refraction Edge - Type: Blade Mk7
   PL: Wymienna Ostrze Załamująca Wymiary - Type: Blade Mk7
135. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Pride) — opis] 최대 체력이 가장 낮은 아군 1명이 적 처치 시 충전 횟수 2 증가 (턴 당 최대 1회 발동)
   źródło: Passives.json :: dataList[id=1040521].desc
   limit: do 130 znaków
   EN: When an ally with the lowest Max HP defeats an enemy, they gain +2 Charge Count (Once per turn)
   PL: Gdy Sojusznik z najniższym Maks. HP pokonuje wroga, zyskuje +2 Licznika Ładowania (1 raz na turę)

## [00] LCCB Assistant Manager — Ryōshū — LCCB 대리
- ID Tożsamości: `10406` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 3 · HP bazowe: 76 · szybkość: 4–5 / 4–6 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Poise, Tremor, Rupture

136. [Karta Tożsamości — tytuł] LCCB\n대리
   źródło: Personalities.json :: dataList[id=10406].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCCB\nAssistant Manager
   PL: LCCB\nZastępca Kierownika
137. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10406].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10406].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Karta Tożsamości — opis] 료슈의 여섯번째 인격
   źródło: Personalities.json :: dataList[id=10406].desc
   limit: do 120 znaków
   EN: Ryōshū’s 6th Identity
   PL: Szósta Tożsamość Ryōshū
140. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 밀치기
   źródło: Skills_personality-04.json :: dataList[id=1040601].levelList[level=1].name ; dataList[id=1040601].levelList[level=2].name ; dataList[id=1040601].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 5 · monety: 1 (+5)
   limit: do 40 znaków
   EN: Shove
   PL: Odepchnięcie
141. [Umiejętność 1 (×3) (ulepszenia 1–2) — opis] [WhenUse] 자신의 호흡 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040601].levelList[level=1].desc ; dataList[id=1040601].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain +2 Poise Count
   PL: [WhenUse] Zyskuje +2 Licznika Oddechu
142. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 대상의 정신력 4 감소
   źródło: Skills_personality-04.json :: dataList[id=1040601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Target loses 4 SP
   PL: [CriticalOnSucceedAttack] Cel traci 4 Poczytalności
143. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 대상의 정신력 6 감소
   źródło: Skills_personality-04.json :: dataList[id=1040601].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Target loses 6 SP
   PL: [CriticalOnSucceedAttack] Cel traci 6 Poczytalności
144. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 호흡 횟수 2 증가\n<style="highlight">자신의</style> <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></color></link></u><style="highlight">이 7 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1040601].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>, \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 2 Poise Count\n<style="highlight">At 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></color></link></u>, Coin Power +1</style>
   PL: [WhenUse] Zwiększa własny Licznik Oddechu o 2\n<style="highlight">Przy 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Oddechu</color></color></link></u> Moc Monet +1</style>
145. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 대상의 정신력 8 감소
   źródło: Skills_personality-04.json :: dataList[id=1040601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Target loses 8 SP
   PL: [CriticalOnSucceedAttack] Cel traci 8 Poczytalności
146. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 타.무
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=1].name ; dataList[id=1040602].levelList[level=2].name ; dataList[id=1040602].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Hit · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: T.N.
   PL: T. N.
147. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 1 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 1 Poise
   PL: [OnSucceedAttack] Zyskuje 1 Oddechu
148. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 공격 레벨 감소 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1040602].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict 1 Offense Level Down
   PL: [CriticalOnSucceedAttack] Nakłada 1 Spadku Poziomu Ataku
149. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 호흡 1 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040602].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1040602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] 공격 레벨 감소 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1040602].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1040602].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 호흡 2 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 Poise
   PL: [OnSucceedAttack] Zyskuje 2 Oddechu
152. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>이 7 이상이면 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>
   EN: At 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u>, Coin Power +1
   PL: Przy 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Oddechu</link></u></color> Moc Monet +1
153. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 공격 레벨 감소 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040602].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Inflict 2 Offense Level Down
   PL: [CriticalOnSucceedAttack] Nakłada 2 Spadku Poziomu Ataku
154. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 대.박
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].name ; dataList[id=1040603].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: O.O.F.
   PL: O. O. F.
155. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 호흡 4 얻음\n자신의 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>이 10 이상이면 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>, \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 4 Poise\nAt 10+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u>, Coin Power +1
   PL: [WhenUse] Zyskuje 4 Oddechu\nPrzy 10+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Oddechu</link></u></color> Moc Monet +1
156. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] 탄환 1 소모
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1040603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: Spend 1 Ammo
   PL: Zużywa 1 amunicji
157. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] 진동, 파열 의 위력과 횟수가 2배로 부여됨
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1040603].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Double the application of Tremor & Rupture Potency and Count
   PL: [CriticalOnSucceedAttack] Podwaja nakładane Mocy i Liczników Wstrząsu oraz Rozdarcia (x 2)
158. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 진동 3 부여, 진동 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Tremor and +1 Tremor Count
   PL: [OnSucceedAttack] Nakłada 3 Wstrząsu i zwiększa Licznik Wstrząsu o 1
159. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 파열 3 부여, 파열 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Rupture and +1 Rupture Count
   PL: [OnSucceedAttack] Nakłada 3 Rozdarcia i zwiększa Licznik Rozdarcia o 1
160. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 5 — opis] [OnSucceedAttackHead] 진동 폭발
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=3].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Trigger Tremor Burst
   PL: [OnSucceedAttackHead] Wybuch Wstrząsu
161. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 호흡 4 얻음\n자신의 호흡 7당, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 4 Poise\nGain +1 Coin Power for every 7 Poise on self (max 2)
   PL: [WhenUse] Zyskuje 4 Oddechu\nMoc Monet +1 za każde 7 Oddechu (maks. 2)
162. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 자신의 호흡 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Gain +1 Poise Count
   PL: [CriticalOnSucceedAttack] Zwiększa własny Licznik Oddechu o 1
163. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] 자신의 호흡 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 진동 4 부여, 진동 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Tremor and +2 Tremor Count
   PL: [OnSucceedAttack] Nakłada 4 Wstrząsu i zwiększa Licznik Wstrząsu o 2
165. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 파열 4 부여, 파열 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Rupture and +2 Rupture Count
   PL: [OnSucceedAttack] Nakłada 4 Rozdarcia i zwiększa Licznik Rozdarcia o 2
166. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 5 — opis] [OnSucceedAttack] 진동 폭발
   źródło: Skills_personality-04.json :: dataList[id=1040603].levelList[level=4].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Trigger Tremor Burst
   PL: [OnSucceedAttack] Wybuch Wstrząsu
167. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-04.json :: dataList[id=1040604].levelList[level=1].name ; dataList[id=1040604].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Glut.) — nazwa] 담.탐
   źródło: Passives.json :: dataList[id=1040601].name
   limit: do 40 znaków
   EN: A S.B.
   PL: A S. B.
169. [Pasywka bojowa (od ulepszenia 2, posiadane 2× Glut.) — opis] 턴 종료 시 자신에게 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>이 7 이상 있으면, 정신력 8 회복.
   źródło: Passives.json :: dataList[id=1040601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>
   EN: If this unit has 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u> at Turn End, heal 8 SP.
   PL: Na koniec tury, jeżeli ta jednostka ma 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Oddechu</link></u></color>, odzyskuje 8 Poczytalności.
170. [Pasywka bojowa (od ulepszenia 3, posiadane 2× Glut.) — nazwa] 담.탐
   źródło: Passives.json :: dataList[id=1040602].name
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Pasywka bojowa (od ulepszenia 3, posiadane 2× Glut.) — opis] <style="highlight">- 상시 적용 : 탄환 7개 보유</style>\n턴 종료 시 자신에게 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>이 7 이상 있으면, 정신력 8 회복.
   źródło: Passives.json :: dataList[id=1040602].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>, \n
   EN: <style="highlight">- Always Active : Begin encounters with 7 Ammo</style>\n- If this unit has 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u> at Turn End, heal 8 SP.
   PL: <style="highlight">- Zawsze aktywne: rozpoczyna spotkania z 7 amunicją</style>\nNa koniec tury, jeżeli ta jednostka ma 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Oddechu</link></u></color>, odzyskuje 8 Poczytalności.
172. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Glut.) — nazwa] 담.탐
   źródło: Passives.json :: dataList[id=1040611].name
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Pasywka bojowa (od ulepszenia 4, posiadane 2× Glut.) — opis] - 상시 적용 : 탄환 7개 보유\n- 턴 종료 시 자신에게 <sprite name="Breath"><color=#f8c200><u><link="Breath">호흡</color></link></u>이 7 이상 있으면, 정신력 8 회복.\n<style="highlight">- 회복 전 정신력이 최대인 경우, 다음 턴에 호흡 1을 얻음</style>
   źródło: Passives.json :: dataList[id=1040611].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <sprite name="Breath">, <color=#f8c200>, <u>, <link="Breath">, </color>, </link>, </u>, <style="highlight">, </style>, \n
   EN: - Always Active : Begin encounters with 7 Ammo\n- If this unit has 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Poise</color></link></u> at Turn End, heal 8 SP.\n<style="highlight">- If this unit already has max SP upon meeting the above condition, gain 1 Poise next turn</style>
   PL: - Zawsze aktywne: rozpoczyna spotkania z 7 amunicją\n- Na koniec tury, jeżeli ta jednostka ma 7+ <sprite name="Breath"><color=#f8c200><u><link="Breath">Oddechu</link></u></color>, odzyskuje 8 Poczytalności.\n<style="highlight">- Jeżeli Poczytalność jest już maksymalna, zyskuje w następnej turze 1 Oddechu</style>
174. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — nazwa] 돛대
   źródło: Passives.json :: dataList[id=1040621].name
   limit: do 40 znaków
   EN: The Lucky Cig
   PL: Pełna Fajka Szczęścia
175. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — opis] [Bullet]을 가장 적게 보유한 아군 1명이 코인에서 마지막 [Bullet]을 소모하면, 코인의 공격 종료 시, 각 대상에게 해당 코인의 공격으로 입힌 피해량의 50%만큼 추가 피해를 줌. (소수점 반올림)
   źródło: Passives.json :: dataList[id=1040621].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: If 1 ally with the least Ammo uses up their last Ammo with a Coin, deal 50% of the damage dealt by that Coin attack against each target as bonus damage against each individual target. (rounded up)
   PL: Gdy 1 Sojusznik z najmniejszym [Bullet] zużyje ostatnią amunicję monetą, na koniec ataku tej monety zadaje każdemu celowi dodatkowe obrażenia równe 50% obrażeń zadanych przez atak tej monety. (zaokrąglone w górę)
176. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Pride) — nazwa] 돛대
   źródło: Passives.json :: dataList[id=1040631].name
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Pride) — opis] <style="highlight">- [Bullet]을 가장 적게 보유한 아군 1명이 [Bullet]을 소모하는 스킬을 사용할 때, 호흡 3 부여. (턴 당 1회. 탄환이 없는 대상에게는 적용되지 않음)</style>\n[Bullet]을 가장 적게 보유한 아군 1명이 코인에서 마지막 [Bullet]을 소모하면, 코인의 공격 종료 시, 각 대상에게 해당 코인의 공격으로 입힌 피해량의 50%만큼 추가 피해를 줌. (소수점 반올림)
   źródło: Passives.json :: dataList[id=1040631].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: <style="highlight">- If 1 ally with the least [Bullet] uses a Skill that spends [Bullet], gain 3 Poise. (once per turn; does not apply to allies without Ammo)</style>\n- If 1 ally with the least Ammo uses up their last Ammo with a Coin, deal 50% of the damage dealt by that Coin attack against each target as bonus damage against each individual target. (rounded up)
   PL: <style="highlight">- Gdy 1 Sojusznik z najmniejszym [Bullet] użyje Umiejętności zużywającej [Bullet], zyskuje 3 Oddechu. (1 raz na turę; nie dotyczy sojuszników bez amunicji)</style>\nGdy 1 Sojusznik z najmniejszym [Bullet] zużyje ostatnią amunicję monetą, na koniec ataku tej monety zadaje każdemu celowi dodatkowe obrażenia równe 50% obrażeń zadanych przez atak tej monety. (zaokrąglone w górę)

## [00] Liu Assoc. South Section 4 — Ryōshū — 남부 리우 협회 4과
- ID Tożsamości: `10407` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 0 · HP bazowe: 76 · szybkość: 2–6 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Burn

178. [Karta Tożsamości — tytuł] 남부 리우 협회\n4과
   źródło: Personalities.json :: dataList[id=10407].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Liu Assoc.\nSouth Section 4
   PL: Południowe Stowarzyszenie Liu\nSekcja 4
179. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10407].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10407].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Karta Tożsamości — opis] 료슈의 일곱번째 인격
   źródło: Personalities.json :: dataList[id=10407].desc
   limit: do 120 znaków
   EN: Ryōshū's 7th Identity
   PL: Siódma Tożsamość Ryōshū
182. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 전면전
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=1].name ; dataList[id=1040701].levelList[level=2].name ; dataList[id=1040701].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: All-out War
   PL: Wojna na Śmierć i Życie
183. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Combustion]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttackHead] Inflict 1 [Combustion]
   PL: [OnSucceedAttackHead] Nakłada 1 [Combustion]
184. [Umiejętność 1 (×3) (ulepszenia 1,4) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040701].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Umiejętność 1 (×3) (ulepszenie 2) — opis] 대상의 [Combustion]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Clash Power +1
   PL: Jeżeli cel ma 6+ [Combustion], Moc Starcia +1
186. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040701].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]
187. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=2].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Umiejętność 1 (×3) (ulepszenie 4) — opis] 대상의 [Combustion]이 6 이상이면, 합 위력 +1\n<style="highlight">대상의 [Combustion]이 10 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Clash Power +1\n<style="highlight">If target has 10+ [Combustion], Coin Power +1 </style>
   PL: Jeżeli cel ma 6+ [Combustion], Moc Starcia +1\n<style="highlight">Jeżeli cel ma 10+ [Combustion], Moc Monet +1</style>
189. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1040701].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 1 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Combustion]<style="highlight"></style>
190. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 염수격
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=1].name ; dataList[id=1040702].levelList[level=2].name ; dataList[id=1040702].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 2 (+5)
   limit: do 40 znaków
   EN: Fiery Knifehand
   PL: Ognisty Rękoczyn
191. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1040702].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040702].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL: [OnSucceedAttack] Nakłada 2 [Combustion]
192. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 피해량 +20%
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], deal +20% damage
   PL: [OnSucceedAttack] Jeżeli cel ma 6+ [Combustion], zadaje +20% obrażeń
193. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 대상의 [Combustion]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=2].desc
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 피해량 +30%
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], deal +30% damage
   PL: [OnSucceedAttack] Jeżeli cel ma 6+ [Combustion], zadaje +30% obrażeń
195. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 대상의 [Combustion]이 6 이상이면, 합 위력 +1\n<style="highlight">대상의 [Combustion]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Clash Power +1\n<style="highlight">If target has 6+ [Combustion], Coin Power +1</style>
   PL: Jeżeli cel ma 6+ [Combustion], Moc Starcia +1\n<style="highlight">Jeżeli cel ma 6+ [Combustion], Moc Monet +1</style>
196. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 6 이상이면, 피해량 +50%
   źródło: Skills_personality-04.json :: dataList[id=1040702].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 6+ [Combustion], deal +50% damage
   PL: [OnSucceedAttack] Jeżeli cel ma 6+ [Combustion], zadaje +50% obrażeń
197. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 염절
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=3].name ; dataList[id=1040703].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 4 · monety: 4 (+2)
   limit: do 40 znaków
   EN: Flame Cleave
   PL: Rozcięcie Płomienia
198. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상의 [Combustion]이 6 이상이면, 합 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=3].desc
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1040703].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1040703].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1040703].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 10 이상이면, 피해량 +20%
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 10+ [Combustion], deal +20% damage
   PL: [OnSucceedAttack] Jeżeli cel ma 10+ [Combustion], zadaje +20% obrażeń
203. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상의 [Combustion]이 6 이상이면, 합 위력 +1\n<style="highlight">대상의 [Combustion]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: If target has 6+ [Combustion], Clash Power +1\n<style="highlight">If target has 6+ [Combustion], Coin Power +1 </style>
   PL: Jeżeli cel ma 6+ [Combustion], Moc Starcia +1\n<style="highlight">Jeżeli cel ma 6+ [Combustion], Moc Monet +1</style>
204. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion]이 10 이상이면, 피해량 +40%
   źródło: Skills_personality-04.json :: dataList[id=1040703].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] If target has 10+ [Combustion], deal +40% damage
   PL: [OnSucceedAttack] Jeżeli cel ma 10+ [Combustion], zadaje +40% obrażeń
205. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-04.json :: dataList[id=1040704].levelList[level=1].name ; dataList[id=1040704].levelList[level=4].name
   kontekst: grzech: Wrath · typ: obrona: blok · moc bazowa: 8 · monety: 1 (+8)
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — nazwa] 화전
   źródło: Passives.json :: dataList[id=1040701].name
   limit: do 40 znaków
   EN: Flame Spread
   PL: Rozprzestrzenienie Płomienia
207. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — opis] 자신이 [Combustion]이 부여된 적 처치 시 [Combustion]이 없거나 [Combustion] 위력이 가장 낮은 무작위 적 1명에게 [Combustion] 4 부여 (턴 당 1회)\n- 집중 전투에서는 부위에 부여
   źródło: Passives.json :: dataList[id=1040701].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When this unit defeats an enemy that has [Combustion], inflict 4 [Combustion] to 1 random enemy that either has no [Combustion] or has the least [Combustion] Potency (once per turn)\n- In Focused Encounters, inflict to 1 random Part
   PL: Gdy ta jednostka pokonuje wroga z [Combustion], nakłada 4 [Combustion] na 1 losowego wroga bez [Combustion] lub z najniższą Mocą [Combustion] (1 raz na turę)\n- W walce skupionej nakłada na część ciała
208. [Pasywka bojowa (od ulepszenia 2, posiadane 4× Wrath) — podsumowanie] [Combustion]이 부여된 적 처치 시 [Combustion]이 없거나 위력이 가장 낮은 무작위 적 1명에게 [Combustion] 4 부여
   źródło: Passives.json :: dataList[id=1040701].summary
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When this unit defeats an enemy that has [Combustion], inflict 4 [Combustion] to 1 random enemy that either has no [Combustion] or has the least [Combustion] Potency
   PL: Gdy ta jednostka pokonuje wroga z [Combustion], nakłada 4 [Combustion] na 1 losowego wroga bez [Combustion] lub z najniższą Mocą [Combustion]
209. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Wrath) — nazwa] 화전
   źródło: Passives.json :: dataList[id=1040711].name
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Wrath) — opis] 자신이 [Combustion]이 부여된 적 처치 시 [Combustion]이 없거나 [Combustion] 위력이 가장 낮은 무작위 적 2명에게 [Combustion] 4 부여 (턴 당 2회)\n- 집중 전투에서는 부위에 부여
   źródło: Passives.json :: dataList[id=1040711].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When this unit defeats an enemy that has [Combustion], inflict 4 [Combustion] to 2 random enemies that either have no [Combustion] or have the least [Combustion] Potency (2 times per turn)\n- In Focused Encounters, inflict to 2 random Parts
   PL: Gdy ta jednostka pokonuje wroga z [Combustion], nakłada 4 [Combustion] na 2 losowych wrogów bez [Combustion] lub z najniższą Mocą [Combustion] (2 razy na turę)\n- W walce skupionej nakłada na 2 losowe części ciała
211. [Pasywka bojowa (od ulepszenia 4, posiadane 4× Wrath) — podsumowanie] [Combustion]이 부여된 적 처치 시 [Combustion]이 없거나 위력이 가장 낮은 무작위 적 2명에게 [Combustion] 4 부여
   źródło: Passives.json :: dataList[id=1040711].summary
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When this unit defeats an enemy that has [Combustion], inflict 4 [Combustion] to 2 random enemies that either have no [Combustion] or have the least [Combustion] Potency
   PL: Gdy ta jednostka pokonuje wroga z [Combustion], nakłada 4 [Combustion] na 2 losowych wrogów bez [Combustion] lub z najniższą Mocą [Combustion]
212. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Wrath) — nazwa] 전화
   źródło: Passives.json :: dataList[id=1040721].name
   limit: do 40 znaków
   EN: Spread Flame
   PL: Rozdmuchanie Płomienia
213. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Wrath) — opis] 속도가 가장 느린 아군 1명이 [Combustion]이 부여된 적 처치 시 무작위 적 1명에게 [Combustion] 3 부여 (턴 당 1회)\n- 집중 전투에서는 부위에 부여
   źródło: Passives.json :: dataList[id=1040721].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When 1 ally with the slowest Speed defeats an enemy that has [Combustion], inflict 3 [Combustion] on 1 random enemy (once per turn)\n- In Focused Encounters, inflict on 1 random Part
   PL: Gdy 1 Sojusznik z najniższą Szybkością pokonuje wroga z [Combustion], nakłada 3 [Combustion] na 1 losowego wroga (1 raz na turę)\n- W walce skupionej nakłada na 1 losową część ciała
214. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Wrath) — podsumowanie] 속도가 가장 느린 아군 1명이 [Combustion]이 부여된 적 처치 시 무작위 적 1명에게 [Combustion] 3 부여
   źródło: Passives.json :: dataList[id=1040721].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When 1 ally with the slowest Speed defeats an enemy that has [Combustion], inflict 3 [Combustion] on 1 random enemy
   PL: Gdy 1 Sojusznik z najniższą Szybkością pokonuje wroga z [Combustion], nakłada 3 [Combustion] na 1 losowego wroga
215. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Wrath) — nazwa] 전화
   źródło: Passives.json :: dataList[id=1040731].name
   (powtórzenie elementu 212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Wrath) — opis] 속도가 가장 느린 아군 1명이 [Combustion]이 부여된 적 처치 시 무작위 적 2명에게 [Combustion] 3 부여 (턴 당 1회)\n- 집중 전투에서는 부위에 부여
   źródło: Passives.json :: dataList[id=1040731].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When 1 ally with the slowest Speed defeats an enemy that has [Combustion], inflict 3 [Combustion] on 2 random enemies (once per turn)\n- In Focused Encounters, inflict on 2 random Parts
   PL: Gdy 1 Sojusznik z najniższą Szybkością pokonuje wroga z [Combustion], nakłada 3 [Combustion] na 2 losowych wrogów (1 raz na turę)\n- W walce skupionej nakłada na 2 losowe części ciała
217. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Wrath) — podsumowanie] 속도가 가장 느린 아군 1명이 [Combustion]이 부여된 적 처치 시 무작위 적 2명에게 [Combustion] 3 부여
   źródło: Passives.json :: dataList[id=1040731].summary
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: When 1 ally with the slowest Speed defeats an enemy that has [Combustion], inflict 3 [Combustion] on 2 random enemies
   PL: Gdy 1 Sojusznik z najniższą Szybkością pokonuje wroga z [Combustion], nakłada 3 [Combustion] na 2 losowych wrogów

## [000] Edgar Family Chief Butler — Ryōshū — 에드가 가문 치프 버틀러
- ID Tożsamości: `10408` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 4 · HP bazowe: 70 · szybkość: 3–6 / 3–7 / 3–8 / 3–8
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Poise

218. [Karta Tożsamości — tytuł] 에드가 가문\n치프 버틀러
   źródło: Personalities.json :: dataList[id=10408].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Edgar Family\nChief Butler
   PL: Rodzina Edgar\nGłówna Kamerdynerka
219. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10408].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10408].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Karta Tożsamości — opis] 료슈의 여덟번째 인격
   źródło: Personalities.json :: dataList[id=10408].desc
   limit: do 120 znaków
   EN: Ryōshū's 8th Identity
   PL: Ósma Tożsamość Ryōshū
222. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 응접도 1식 사냥
   źródło: Skills_personality-04.json :: dataList[id=1040801].levelList[level=1].name ; dataList[id=1040801].levelList[level=2].name ; dataList[id=1040801].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Receiving Arts 1: The Hunt
   PL: Sztuka Gościny 1: Polowanie
223. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040801].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2
224. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040801].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1040801].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040801].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +2 Licznika [Breath]
225. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MarkOfButler] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040801].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040801].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1040801].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MarkOfButler]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MarkOfButler] = 버.표 / B.M.
   EN: [OnSucceedAttack] Inflict 2 [MarkOfButler]
   PL: [OnSucceedAttack] Nakłada 2 [MarkOfButler]
226. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">대상의 속도가 자신보다 3 이상 느리면, 합 위력 +1</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040801].levelList[level=2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: <style="highlight">If this unit's Speed is faster than the target's by 3 or more, Clash Power +1</style>\n[WhenUse] Gain +2 [Breath] Count
   PL: <style="highlight">Jeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, Moc Starcia +1</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
227. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">대상의 속도가 자신보다 느리면, 대상과의 속도 차이 2 당 합 위력 +1 (최대 3)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040801].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: <style="highlight">If this unit's Speed is faster than the target's, gain Clash Power +1 for every 2 Speed difference (max 3)</style>\n[WhenUse] Gain +2 [Breath] Count
   PL: <style="highlight">Jeżeli Szybkość tej jednostki jest większa niż celu, Moc Starcia +1 za każde 2 różnicy Szybkości (maks. 3)</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
228. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 응접도 제 7식 포착
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=1].name ; dataList[id=1040802].levelList[level=2].name ; dataList[id=1040802].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Receiving Arts 7: Capture
   PL: Sztuka Gościny 7: Kapstwo
229. [Umiejętność 2 (×2) (ulepszenia 1–2) — opis] [StartBattle] 자신의 [Breath] 횟수 6을 소모하여 이 스킬의 가중치 +2
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=1].desc ; dataList[id=1040802].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise
   EN: [StartBattle] Consume 6 [Breath] Count on self to gain +2 Atk Weight for this Skill
   PL: [StartBattle] Zużywa 6 Licznika [Breath], aby nadać tej Umiejętności Wagę ataku +2
230. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL: [OnSucceedAttack] Zyskuje 2 [Breath]
231. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MarkOfButler] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040802].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1040802].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1040802].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL: [OnSucceedAttack] Zyskuje 3 [Breath]
233. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">메인 타겟의 속도가 자신보다 느리면, 대상과의 속도 차이 2 당 합 위력 +1 (최대 3)</style>\n[StartBattle] 자신의 [Breath] 횟수 6을 소모하여 이 스킬의 가중치 +2
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=4].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Breath] = 호흡 / Poise
   EN: <style="highlight">If this unit's Speed is faster than the main target's, gain Clash Power +1 for every 2 Speed difference (max 3)</style>\n[StartBattle] Consume 6 [Breath] Count on self to gain +2 Atk Weight for this Skill
   PL: <style="highlight">Jeżeli Szybkość głównej jednostki jest większa niż celu, Moc Starcia +1 za każde 2 różnicy Szybkości (maks. 3)</style>\n[StartBattle] Zużywa 6 Licznika [Breath], aby nadać tej Umiejętności Wagę ataku +2
234. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [MarkOfButler] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040802].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [MarkOfButler]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [MarkOfButler] = 버.표 / B.M.
   EN: [CriticalOnSucceedAttack] Inflict 1 [MarkOfButler]
   PL: [CriticalOnSucceedAttack] Nakłada 1 [MarkOfButler]
235. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 응접도 제 2식 모.분
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].name ; dataList[id=1040803].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 4 · monety: 2 (+7)
   limit: do 40 znaków
   EN: Receiving Arts 2: S.Y.N.C.
   PL: Sztuka Gościny 2: S. Y. N. C.
236. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상에게 [MarkOfButler]가 있으면 합 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 7 증가
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [MarkOfButler], [WhenUse], [Breath]
   znaczenie tagów: [MarkOfButler] = 버.표 / B.M.; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If target has [MarkOfButler], Clash Power +1\n[WhenUse] Gain +7 [Breath] Count
   PL: Jeżeli cel ma [MarkOfButler], Moc Starcia +1\n[WhenUse] Zwiększa własny Licznik [Breath] o 7
237. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 5 얻음
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1040803].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 5 [Breath]
   PL: [OnSucceedAttack] Zyskuje 5 [Breath]
238. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1040803].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 1 [Binding]
239. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 20%만큼 흐트러짐 손상
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 20% of damage dealt
   PL: [OnSucceedAttack] podniesienie Progu Oszołomienia o 20% zadanych obrażeń
240. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상이 흐트러짐 상태면, 크리티컬 피해량 +20%
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target is Staggered, deal +20% Damage on Critical Hit
   PL: [OnSucceedAttack] Jeżeli cel jest Ogłuszony, zadaje +20% obrażeń przy trafieniu krytycznym
241. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [MarkOfButler] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1040803].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상에게 [MarkOfButler]가 있으면 합 위력 +1\n<style="highlight">대상의 속도가 자신보다 느리면, 대상과의 속도 차이 2 당 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 7 증가
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=4].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [MarkOfButler], [WhenUse], [Breath]
   znaczenie tagów: [MarkOfButler] = 버.표 / B.M.; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: If target has [MarkOfButler], Clash Power +1\n<style="highlight">If this unit's Speed is faster than the target's, gain Coin Power +1 for every 2 Speed difference (max 2)</style>\n[WhenUse] Gain +7 [Breath] Count
   PL: Jeżeli cel ma [MarkOfButler], Moc Starcia +1\n<style="highlight">Jeżeli Szybkość tej jednostki jest większa niż celu, Moc Monet +1 za każde 2 różnicy Szybkości (maks. 2)</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 7
243. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 30%만큼 흐트러짐 손상
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 30% of damage dealt
   PL: [OnSucceedAttack] podniesienie Progu Oszołomienia o 30% zadanych obrażeń
244. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] [MarkOfButler] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=4].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상이 흐트러짐 상태면, 크리티컬 피해량 +40%
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target is Staggered, deal +40% Damage on Critical Hit
   PL: [OnSucceedAttack] Jeżeli cel jest Ogłuszony, zadaje +40% obrażeń przy trafieniu krytycznym
246. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 3 — opis] [EnemyKill] [MarkOfButler]가 있는 무작위 대상에게 스킬 1회 재사용\n(재사용 시 발동하지 않음. [MarkOfButler]가 있는 대상이 없는 경우, 발동하지 않음)
   źródło: Skills_personality-04.json :: dataList[id=1040803].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [EnemyKill], [MarkOfButler]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [MarkOfButler] = 버.표 / B.M.
   EN: [EnemyKill] Reuse Skill once on a random target that has [MarkOfButler]\n(Does not activate on Reuse. Does not activate when there are no remaining targets that have [MarkOfButler])
   PL: [EnemyKill] Używa Umiejętności ponownie na 1 losowym celu z [MarkOfButler]\n(Nie uruchamia się przy ponownym użyciu. Nie uruchamia się, gdy nie ma celów z [MarkOfButler])
247. [Obrona (ulepszenia 1,4) — nazwa] 한심
   źródło: Skills_personality-04.json :: dataList[id=1040804].levelList[level=1].name ; dataList[id=1040804].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Mediocre
   PL: Pośrednio
248. [Obrona (ulepszenie 1) — opis] [OnSucceedEvade] 정신력 3 회복 (턴 당 3회)
   źródło: Skills_personality-04.json :: dataList[id=1040804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [OnSucceedEvade] Heal 3 SP (3 times per turn)
   PL: [OnSucceedEvade] Odzyskuje 3 Poczytalności (3 razy na turę)
249. [Obrona (ulepszenie 4) — opis] [OnSucceedEvade] 정신력 3 회복 (턴 당 <style="highlight">5</style>회)\n<style="highlight">[OnSucceedEvade] 자신의 [Breath] 횟수 1 증가 (턴 당 5회)</style>
   źródło: Skills_personality-04.json :: dataList[id=1040804].levelList[level=4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedEvade], [Breath]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise
   EN: [OnSucceedEvade] Heal 3 SP (<style="highlight">5</style> times per turn)\n<style="highlight">[OnSucceedEvade] Gain +1 [Breath] Count(5 times per turn)</style>
   PL: [OnSucceedEvade] Odzyskuje 3 Poczytalności (<style="highlight">5</style> razy na turę)\n<style="highlight">[OnSucceedEvade] Zwiększa własny Licznik [Breath] o 1 (5 razy na turę)</style>
250. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — nazwa] 집안일 끝내기
   źródło: Passives.json :: dataList[id=1040801].name
   limit: do 40 znaków
   EN: Clearing Household Chores
   PL: Uporządkowanie Domu
251. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — opis] [MarkOfButler]가 있는 대상에게 공격 적중 시 다음 턴에 [Agility] 1 얻음 (턴 당 최대 3회)\n[MarkOfButler]가 있는 대상에게 크리티컬 적중 시 대상의 [MarkOfButler]를 제거하고, 대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1 당 크리티컬 피해량 +5% (최대 30%)
   źródło: Passives.json :: dataList[id=1040801].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [MarkOfButler], [Agility]
   znaczenie tagów: [MarkOfButler] = 버.표 / B.M.; [Agility] = 신속 / Haste
   EN: On Hit against targets that have [MarkOfButler], gain 1 [Agility] next turn (3 times per turn)\nOn Crit against targets that have [MarkOfButler], eliminate [MarkOfButler] on target; then, if this unit's Speed is faster than the target's, deal +5% Damage on Critical Hit for every 1 Speed difference (max 30%)
   PL: Przy trafieniu celu z [MarkOfButler] zyskuje w następnej turze 1 [Agility] (maks. 3 razy na turę)\nPrzy trafieniu krytycznym celu z [MarkOfButler] usuwa jego [MarkOfButler], a jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +5% obrażeń przy trafieniu krytycznym za każde 1 różnicy Szybkości (maks. 30%)
252. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Pride) — nazwa] 집안일 끝내기
   źródło: Passives.json :: dataList[id=1040811].name
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Pride) — opis] [MarkOfButler]가 있는 대상에게 공격 적중 시 [Breath] 횟수 1 증가, 다음 턴에 [Agility] 1 얻음 (턴 당 최대 3회)\n[MarkOfButler]가 있는 대상에게 크리티컬 적중 시 대상의 [MarkOfButler]를 제거하고, 대상의 속도가 자신보다 느리면, 대상과의 속도 차이 1 당 크리티컬 피해량 +10% (최대 60%)
   źródło: Passives.json :: dataList[id=1040811].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [MarkOfButler], [Breath], [Agility]
   znaczenie tagów: [MarkOfButler] = 버.표 / B.M.; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: On Hit against targets that have [MarkOfButler], gain +1 [Breath] Count, and gain 1 [Agility] next turn (3 times per turn)\nOn Crit against targets that have [MarkOfButler], eliminate [MarkOfButler] on target; then, if this unit's Speed is faster than the target's, deal +10% Damage on Critical Hit for every 1 Speed difference (max 60%)
   PL: Przy trafieniu celu z [MarkOfButler] zwiększa Licznik [Breath] o 1 i zyskuje w następnej turze 1 [Agility] (maks. 3 razy na turę)\nPrzy trafieniu krytycznym celu z [MarkOfButler] usuwa jego [MarkOfButler], a jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +10% obrażeń przy trafieniu krytycznym za każde 1 różnicy Szybkości (maks. 60%)
254. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — nazwa] 청소 지휘
   źródło: Passives.json :: dataList[id=1040821].name
   limit: do 40 znaków
   EN: Cleaning Command
   PL: Dowodzenie Sprzątaniem
255. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Pride) — opis] 편성 순서가 가장 뒤인 아군 1명이 합 승리 시 호흡 횟수 1 증가 (턴 당 3회)
   źródło: Passives.json :: dataList[id=1040821].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: When the ally that was deployed last wins a Clash, gain +1 [Breath] Count (3 times per turn)
   PL: Gdy 1 Sojusznik przydzielony najpóźniej wygrywa Starcie, zwiększa Licznik [Breath] o 1 (3 razy na turę)
256. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Pride) — nazwa] 청소 지휘
   źródło: Passives.json :: dataList[id=1040831].name
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Pasywka wsparcia (od ulepszenia 4, posiadane 4× Pride) — opis] 편성 순서가 가장 뒤인 아군 1명이 합 승리 시 [Breath] 횟수 1 증가 (턴 당 3회), 다음 턴에 [Agility] 1 얻음 (턴 당 1회)
   źródło: Passives.json :: dataList[id=1040831].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Breath], [Agility]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: When the ally that was deployed last wins a Clash, gain +1 [Breath] Count (3 times per turn), and gain 1 [Agility] next turn (once per turn)
   PL: Gdy 1 Sojusznik przydzielony najpóźniej wygrywa Starcie, zwiększa Licznik [Breath] o 1 (3 razy na turę) i zyskuje w następnej turze 1 [Agility] (1 raz na turę)

## [00] District 20 Yurodivy — Ryōshū — 20구 유로지비
- ID Tożsamości: `10409` (plik: `Personalities.json`)
- parametry karty: rzadkość `00` · sezon: 4 · HP bazowe: 71 · szybkość: 4–6 / 4–6 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Tremor

258. [Karta Tożsamości — tytuł] 20구\n유로지비
   źródło: Personalities.json :: dataList[id=10409].title
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: District 20\nYurodivy
   PL: Dystrykt 20\nJurodiwyj
259. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10409].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10409].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Karta Tożsamości — opis] 료슈의 아홉번째 인격
   źródło: Personalities.json :: dataList[id=10409].desc
   limit: do 120 znaków
   EN: Ryōshū's 9th Identity
   PL: Dziewiąta Tożsamość Ryōshū
262. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 나사빠진 놈들
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=1].name ; dataList[id=1040901].levelList[level=2].name ; dataList[id=1040901].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Got a Screw Loose?
   PL: Czy Śrubę Kręci Przewrotka?
263. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 2
264. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수 절반만큼 자신의 [Vibration] 횟수 증가 (최대 2)
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain [Vibration] Count equal to (([Vibration] Count on target)/2) (max 2)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Vibration] o połowę Licznika [Vibration] celu (maks. 2)
265. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1040901].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Vibration]
266. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">[WhenUse] 자신의 [Vibration] 횟수가 5 이상이면, 합 위력 +2</style>
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n<style="highlight">[WhenUse] At 5+ [Vibration] Count, Clash Power +2</style>
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 2\n<style="highlight">[WhenUse] Przy 5+ Liczniku [Vibration] Moc Starcia +2</style>
267. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수 절반만큼 자신의 [Vibration] 횟수 증가 (최대 <style="highlight">3</style>)
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain [Vibration] Count equal to (([Vibration] Count on target)/2) (max <style="highlight">3</style>)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Vibration] o połowę Licznika [Vibration] celu (maks. <style="highlight">3</style>)
268. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n[WhenUse] 자신의 [Vibration] 횟수가 <style="highlight">4</style> 이상이면, 합 위력 +2
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n[WhenUse] At <style="highlight">4</style>+ [Vibration] Count, Clash Power +2
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 2\n[WhenUse] Przy <style="highlight">4</style>+ Liczniku [Vibration] Moc Starcia +2
269. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수만큼 자신의 [Vibration] 횟수 증가 (최대 <style="highlight">4</style>)
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Gain [Vibration] Count equal to ([Vibration] Count on target) (max <style="highlight">4</style>)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [Vibration] o wartość Licznika [Vibration] celu (maks. <style="highlight">4</style>)
270. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-04.json :: dataList[id=1040901].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +<style="highlight">2</style> [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +<style="highlight">2</style> Licznika [Vibration]
271. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 압착 태엽 스패너
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=1].name ; dataList[id=1040902].levelList[level=2].name ; dataList[id=1040902].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Compression Wind-up Spanner
   PL: Kompresyjny Klucz Nakrętkowy
272. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=1].desc
   (powtórzenie elementu 263 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Inflict +1 [Vibration] Count
   PL: [OnSucceedAttackHead] Nakłada +1 Licznika [Vibration]
274. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Vibration] 횟수를 소모하여 소모한 [Vibration] 횟수만큼 대상의 [Vibration] 횟수 증가 (최대 5)
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=1040902].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1040902].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Consume [Vibration] Count on self, and inflict the same amount of [Vibration] Count on target (max 5)
   PL: [OnSucceedAttack] Zużywa własny Licznik [Vibration] i nakłada tyle samo Licznika [Vibration] na cel (maks. 5)
275. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">자신의 [Vibration] 횟수가 5 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n<style="highlight">At 5+ [Vibration] Count, Coin Power +1</style>
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 2\n<style="highlight">Przy 5+ Liczniku [Vibration] Moc Monet +1</style>
276. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Vibration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttackHead] Gain +1 [Vibration] Count
   PL: [OnSucceedAttackHead] Zwiększa własny Licznik [Vibration] o 1
277. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n<style="highlight">[WhenUse] 자신의 진동 횟수가 4 이상이면, 합 위력 +1</style>\n자신의 [Vibration] 횟수 <style="highlight">4</style> 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\n<style="highlight">[WhenUse] At 4+ [Vibration] Count, Clash Power +1</style>\nAt <style="highlight">4</style>+ [Vibration] Count, Coin Power +1
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 2\n<style="highlight">[WhenUse] Przy 4+ Liczniku [Vibration] Moc Starcia +1</style>\nPrzy <style="highlight">4</style>+ Liczniku [Vibration] Moc Monet +1
278. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1040902].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 두들기면 고쳐진다
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=3].name ; dataList[id=1040903].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 4 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Percussive Maintenance
   PL: Naprawa via Kopniak
280. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n자신의 [Vibration] 횟수 10 소모하여 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=3].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\nConsume 10 [Vibration] Count on self to gain Coin Power +1
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 2\nZużywa 10 Licznika [Vibration], aby zyskać Moc Monet +1
281. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1040903].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]
282. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1040903].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 2
   PL: [OnSucceedAttack] [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 2
284. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수 2 증가\n[WhenUse] 자신의 [Vibration] 횟수 <style="highlight">8</style> 소모하여 코인 위력 +1\n<style="highlight">대상의 [Vibration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain +2 [Vibration] Count\nConsume <style="highlight">8</style> [Vibration] Count on self to gain Coin Power +1\n<style="highlight">If target has 6+ [Vibration], Coin Power +1</style>
   PL: [WhenUse] Zwiększa własny Licznik [Vibration] o 2\n[WhenUse] Zużywa <style="highlight">8</style> Licznika [Vibration], aby zyskać Moc Monet +1\n<style="highlight">Jeżeli cel ma 6+ [Vibration], Moc Monet +1</style>
285. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 <style="highlight">1</style> 감소
   źródło: Skills_personality-04.json :: dataList[id=1040903].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by <style="highlight">1</style>
   PL: [OnSucceedAttack] [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o <style="highlight">1</style>
286. [Obrona (ulepszenia 1,4) — nazwa] 가드
   źródło: Skills_personality-04.json :: dataList[id=1040904].levelList[level=1].name ; dataList[id=1040904].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 7 · monety: 1 (+6)
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Obrona (ulepszenie 1) — opis] [WhenUse] 자신의 [Vibration] 횟수의 2배만큼 보호막 체력을 얻음 (최대 5)
   źródło: Skills_personality-04.json :: dataList[id=1040904].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain 2 x ([Vibration] Count on self) as Shield HP (max 5)
   PL: [WhenUse] Zyskuje Tarczę HP równą 2 x własnego Licznika [Vibration] (maks. 5)
288. [Obrona (ulepszenie 4) — opis] [WhenUse] 자신의 [Vibration] 횟수의 2배만큼 보호막 체력을 얻음 (최대 <style="highlight">10</style>)
   źródło: Skills_personality-04.json :: dataList[id=1040904].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Gain 2 x ([Vibration] Count on self) as Shield HP (max <style="highlight">10</style>)
   PL: [WhenUse] Zyskuje Tarczę HP równą 2 x własnego Licznika [Vibration] (maks. <style="highlight">10</style>)
289. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Sloth) — nazwa] 제.지
   źródło: Passives.json :: dataList[id=1040901].name
   limit: do 40 znaków
   EN: N.O.
   PL: N. O.
290. [Pasywka bojowa (od ulepszenia 2, rezonans 3× Sloth) — opis] 자신을 제외한 아군의 공격으로 흐트러짐 상태가 된 적을 스킬 1로 공격함. (턴 당 1회)\n여러 적이 흐트러졌을 경우 체력이 가장 낮은 적(환상체일 때, 본체 우선 이후 부위)을 공격함.\n이 효과로 스킬 1을 사용할 때 코인 효과로 자신이 얻는 [Vibration] 횟수가 1 증가하고, 해당 스킬의 마지막 코인 적중시 [VibrationExplosion]
   źródło: Passives.json :: dataList[id=1040901].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [VibrationExplosion]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: - When another ally Staggers an enemy with an attack: follow up with a Skill 1 against the Staggered enemy. (once per Turn)\n- If multiple enemies are Staggered at once, target the enemy with the least HP(for Abnormalities, target the Abnormality with the least HP; then, target the Part with the least HP).\n- When using Skill 1 with this effect, this unit gains +1 more [Vibration] Count from its Coin effects, and triggers a [VibrationExplosion] with the last Coin On Hit
   PL: - Gdy inny sojusznik Ogłuszy wroga atakiem, używa Umiejętności 1 na Ogłuszonym wrogu. (1 raz na turę)\n- Jeżeli Ogłuszono kilku wrogów naraz, namierza wroga z najmniejszym HP (w przypadku Abnormalności: najpierw trzon o najmniejszym HP, potem część ciała).\n- Używając Umiejętności 1 z tym efektem, ta jednostka zyskuje o 1 więcej Licznika [Vibration] z efektów monet, a ostatnia moneta przy trafieniu wywołuje [VibrationExplosion]
291. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Sloth) — nazwa] 조.감
   źródło: Passives.json :: dataList[id=1040921].name
   limit: do 40 znaków
   EN: The A.I.
   PL: The A. I.
292. [Pasywka wsparcia (od ulepszenia 3, posiadane 4× Sloth) — opis] 편성 순서가 1번인 아군이 스킬, 코인 효과로 얻는 [Vibration] 횟수의 값 +1 (턴 당 2회)
   źródło: Passives.json :: dataList[id=1040921].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: #1 Deployed ally gains +1 more Tremor Count from their Skill or Coin effects (2 times per turn)
   PL: Sojusznik przydzielony na 1. pozycji zyskuje o 1 więcej Licznika [Vibration] z efektów Umiejętności i monet (2 razy na turę)

## [000] Lobotomy E.G.O:: Red Eyes & Penitence — Ryōshū — 로보토미 E.G.O:: 적안・참회
- ID Tożsamości: `10410` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9104 · HP bazowe: 69 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×2 (Fatal), Hit ×0,5 (Endured) · słowa kluczowe: Charge, Bleed

293. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n적안・참회
   źródło: Personalities.json :: dataList[id=10410].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::\nRed Eyes &\nPenitence
   PL: Lobotomy E.G.O::\nCzerwone Oczy i\nPokuta
294. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10410].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10410].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Karta Tożsamości — opis] 료슈의 열번째 인격
   źródło: Personalities.json :: dataList[id=10410].desc
   limit: do 120 znaków
   EN: Ryōshū's 10th Identity
   PL: Dziesiąta Tożsamość Ryōshū
297. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 둘 다 닥쳐라
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=1].name ; dataList[id=1041001].levelList[level=2].name ; dataList[id=1041001].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Both of You, Shut Up
   PL: Oboje, Cisza
298. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 3 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 3 [PenanceFirst]
   PL: [OnSucceedAttack] Zyskuje 3 [PenanceFirst]
299. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 2 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 2 [RedEyeFirst]
   PL: [OnSucceedAttack] Zyskuje 2 [RedEyeFirst]
300. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[RedEyeFirst]이 7 이상이면, 코인 위력 +1\n[PenanceFirst]가 7 이상이면, 합 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RedEyeFirst], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence
   EN: <style="highlight">At 7+ [RedEyeFirst], Coin Power +1\nAt 7+ [PenanceFirst], Clash Power +1</style>
   PL: <style="highlight">Przy 7+ [RedEyeFirst] Moc Monet +1\nPrzy 7+ [PenanceFirst] Moc Starcia +1</style>
301. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 3 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 3 [PenanceFirst]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 3 [PenanceFirst]<style="highlight"></style>
302. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041001].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 2 [RedEyeFirst]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 2 [RedEyeFirst]<style="highlight"></style>
303. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Laceration] 1 부여</style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Laceration]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [Laceration]</style>
304. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [RedEyeFirst]이 7 이상이면, 코인 위력 +1\n[PenanceFirst]가 7 이상이면, 합 위력 <style="highlight">+2</style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RedEyeFirst], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence
   EN: At 7+ [RedEyeFirst], Coin Power +1\nAt 7+ [PenanceFirst], Clash Power <style="highlight">+2</style>
   PL: Przy 7+ [RedEyeFirst] Moc Monet +1\nPrzy 7+ [PenanceFirst] Moc Starcia <style="highlight">+2</style>
305. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 3 얻음\n<style="highlight">[OnSucceedAttackHead] [PenanceFirst] 1 얻음</style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [PenanceFirst], [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence; [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttack] Gain 3 [PenanceFirst]\n<style="highlight">[OnSucceedAttackHead] Gain 1 [PenanceFirst]</style>
   PL: [OnSucceedAttack] Zyskuje 3 [PenanceFirst]\n<style="highlight">[OnSucceedAttackHead] Zyskuje 1 [PenanceFirst]</style>
306. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041001].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]<style="highlight"></style>
307. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 거.대 / 해.바
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=1].name ; dataList[id=1041002].levelList[level=2].name ; dataList[id=1041002].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: S.H. / S.F.
   PL: S. H. / S. F.
308. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [RedEyeFirst]과 [PenanceFirst]의 합이 20 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RedEyeFirst], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence
   EN: If the sum of [RedEyeFirst] and [PenanceFirst] is 20 or higher, Coin Power +1
   PL: Jeżeli suma [RedEyeFirst] i [PenanceFirst] wynosi 20 lub więcej, Moc Monet +1
309. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 4 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 4 [PenanceFirst]
   PL: [OnSucceedAttack] Zyskuje 4 [PenanceFirst]
310. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 3 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 3 [RedEyeFirst]
   PL: [OnSucceedAttack] Zyskuje 3 [RedEyeFirst]
311. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]
312. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [RedEyeFirst]과 [PenanceFirst]의 합이 20 이상이면, 코인 위력 +1\n<style="highlight">대상의 [Laceration]이 6 이상이면, 코인 위력 +1</style>
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RedEyeFirst], [PenanceFirst], [Laceration]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence; [Laceration] = 출혈 / Bleed
   EN: If the sum of [RedEyeFirst] and [PenanceFirst] is 20 or higher, Coin Power +1\n<style="highlight">If target has 6+ [Laceration], Coin Power +1</style>
   PL: Jeżeli suma [RedEyeFirst] i [PenanceFirst] wynosi 20 lub więcej, Moc Monet +1\n<style="highlight">Jeżeli cel ma 6+ [Laceration], Moc Monet +1</style>
313. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 4 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1041002].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 4 [PenanceFirst]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 4 [PenanceFirst]<style="highlight"></style>
314. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 3 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041002].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 3 [RedEyeFirst]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 3 [RedEyeFirst]<style="highlight"></style>
315. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1041002].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Laceration]<style="highlight"></style>
316. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 대상의 ([Laceration]/3)만큼 [RedEyeFirst] 얻음 (최대 2)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [RedEyeFirst] = 적안 / Red Eyes
   EN: <style="highlight">[OnSucceedAttack] Gain [RedEyeFirst] equal to ([Laceration] on target/3) (max 2)</style>
   PL: <style="highlight">[OnSucceedAttack] Zyskuje [RedEyeFirst] równy ([Laceration] celu/3) (maks. 2)</style>
317. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [RedEyeFirst]과 [PenanceFirst]의 합이 <style="highlight">15</style> 이상이면, 코인 위력 +1\n대상의 [Laceration]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=4].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RedEyeFirst], [PenanceFirst], [Laceration]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence; [Laceration] = 출혈 / Bleed
   EN: If the sum of [RedEyeFirst] and [PenanceFirst] is <style="highlight">15</style> or higher, Coin Power +1\nIf target has 6+ [Laceration], Coin Power +1
   PL: Jeżeli suma [RedEyeFirst] i [PenanceFirst] wynosi <style="highlight">15</style> lub więcej, Moc Monet +1\nJeżeli cel ma 6+ [Laceration], Moc Monet +1
318. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 대상의 ([Laceration]/<style="highlight">2</style>)만큼 [RedEyeFirst] 얻음 (최대 <style="highlight">3</style>)
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain [RedEyeFirst] equal to ([Laceration] on target/<style="highlight">2</style>) (max <style="highlight">3</style>)
   PL: [OnSucceedAttack] Zyskuje [RedEyeFirst] równy ([Laceration] celu/<style="highlight">2</style>) (maks. <style="highlight">3</style>)
319. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttackHead] [RedEyeFirst]이 7 이상이면, 다음 턴에 [Agility] 1 얻음 (턴 당 2회)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041002].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [RedEyeFirst], [Agility]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [RedEyeFirst] = 적안 / Red Eyes; [Agility] = 신속 / Haste
   EN: <style="highlight">[OnSucceedAttackHead] At 7+ [RedEyeFirst], gain 1 [Agility] next turn (2 times per turn)</style>
   PL: <style="highlight">[OnSucceedAttackHead] Przy 7+ [RedEyeFirst] zyskuje w następnej turze 1 [Agility] (2 razy na turę)</style>
320. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 대가리 터트리기
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].name ; dataList[id=1041003].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Skullbuster
   PL: Rozwalanie Głów
321. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [BeforeUse] [RedEyeFirst]과 [PenanceFirst]가 각각 15 이상이면, '진심 대가리 터트리기'로 발동됨\n대상의 속도가 자신보다 3 이상 느리면, 코인 위력 +1\n[WhenUse] 정신력이 최대일 경우, 코인 위력 +1\n- [EndSkill] 이 효과가 발동되었다면 정신력 15 감소
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeUse], [RedEyeFirst], [PenanceFirst], [WhenUse], [EndSkill]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeUse] If [RedEyeFirst] and [PenanceFirst] are both at 15+, activate 'Serious Skullbuster' instead\nIf this unit's Speed is faster than the target's by 3 or more, Coin Power +1\n[WhenUse] At max SP, Coin Power +1\n- [EndSkill] If this effect activated, lose 15 SP
   PL: [BeforeUse] Jeżeli [RedEyeFirst] i [PenanceFirst] mają po 15 lub więcej, uruchamia „Poważne Rozwalanie Głów”\nJeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, Moc Monet +1\n[WhenUse] Przy pełnej Poczytalności Moc Monet +1\n- [EndSkill] Jeżeli ten efekt się uruchomił, traci 15 Poczytalności
322. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 7 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 7 [RedEyeFirst]
   PL: [OnSucceedAttack] Zyskuje 7 [RedEyeFirst]
323. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [PenanceFirst] 7 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 7 [PenanceFirst]
   PL: [OnSucceedAttack] Zyskuje 7 [PenanceFirst]
324. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신과 현재 체력 비율이 가장 낮은 아군 1명이 각 대상의 최대 체력의 ([PenanceFirst]/3)%만큼 체력 회복
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the lowest HP percentage by ([PenanceFirst]/3)% of each unit's max HP
   PL: [OnSucceedAttack] Odzyskuje HP sobie i 1 Sojusznikowi z najniższym procentem HP równe ([PenanceFirst]/3)% Maks. HP każdej z jednostek
326. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신과 현재 정신력이 가장 낮은 아군 1명을 ([PenanceFirst]-10)만큼 정신력 회복 (최소 0)
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the least SP by ([PenanceFirst] - 10) SP (min 0)
   PL: [OnSucceedAttack] Odzyskuje Poczytalność sobie i 1 sojusznikowi z najniższą Poczyt.  równą ([PenanceFirst] - 10) (min 0)
327. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [BeforeUse] [RedEyeFirst]과 [PenanceFirst]가 각각 15 이상이면, '진심 대가리 터트리기'로 발동됨\n대상의 속도가 <style="highlight">자신보다 느리면</style>, 코인 위력 +1\n[WhenUse] 정신력이 최대일 경우, <style="highlight">합 위력 +2</style>, 코인 위력 +1\n- [EndSkill] 이 효과가 발동되었다면 정신력 15 감소
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [BeforeUse], [RedEyeFirst], [PenanceFirst], [WhenUse], [EndSkill]
   znaczenie tagów: [BeforeUse] = [사용전] / [Before Use]; [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [BeforeUse] If [RedEyeFirst] and [PenanceFirst] are both at 15+, activate 'Serious Skullbuster' instead\nIf this unit's Speed <style="highlight">is faster than the target's</style>, Coin Power +1\n[WhenUse] At max SP, <style="highlight">Clash Power +2</style> and Coin Power +1\n- [EndSkill] If this effect activated, lose 15 SP
   PL: [BeforeUse] Jeżeli [RedEyeFirst] i [PenanceFirst] mają po 15 lub więcej, uruchamia „Poważne Rozwalanie Głów”\nJeżeli Szybkość tej jednostki <style="highlight">jest większa niż celu</style>, Moc Monet +1\n[WhenUse] Przy pełnej Poczytalności <style="highlight">Moc Starcia +2</style> i Moc Monet +1\n- [EndSkill] Jeżeli ten efekt się uruchomił, traci 15 Poczytalności
328. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 7 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 7 [RedEyeFirst]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 7 [RedEyeFirst]<style="highlight"></style>
329. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [PenanceFirst] 7 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 7 [PenanceFirst]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 7 [PenanceFirst]<style="highlight"></style>
330. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] <style="highlight">3</style> 부여
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Laceration]
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Laceration]
331. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] <style="highlight">[OnSucceedAttackHead] [PenanceFirst] 2 얻음</style>
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttackHead], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [PenanceFirst] = 참회 / Penitence
   EN: <style="highlight">[OnSucceedAttackHead] Gain 2 [PenanceFirst]</style>
   PL: <style="highlight">[OnSucceedAttackHead] Zyskuje 2 [PenanceFirst]</style>
332. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신과 현재 체력 비율이 가장 낮은 아군 1명이 각 대상의 최대 체력의 ([PenanceFirst]/<style="highlight">2</style>)%만큼 체력 회복
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the lowest HP percentage by ([PenanceFirst]/<style="highlight">2</style>)% of each unit's max HP
   PL: [OnSucceedAttack] Odzyskuje HP sobie i 1 Sojusznikowi z najniższym procentem HP równe ([PenanceFirst]/<style="highlight">2</style>)% Maks. HP każdej z jednostek
333. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신과 현재 정신력이 가장 낮은 아군 1명을 ([PenanceFirst]-10)만큼 정신력 회복 (최소 0)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041003].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the least SP by ([PenanceFirst] - 10) SP (min 0)<style="highlight"></style>
   PL: [OnSucceedAttack] Odzyskuje Poczytalność sobie i 1 sojusznikowi z najniższą Poczyt.  równą ([PenanceFirst] - 10) (min 0)<style="highlight"></style>
334. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 진심 대가리 터트리기
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].name ; dataList[id=1041005].levelList[level=4].name
   kontekst: grzech: Lust · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Serious Skullbuster
   PL: Poważne Rozwalanie Głów
335. [Umiejętność 4 (×0) (ulepszenia 3–4) — opis] [WhenUse] 보유 중인 [RedEyeFirst]과 [PenanceFirst]를 전부 소모\n- 소모한 [RedEyeFirst] 5당 코인 위력 +1 (최대 4)\n- 소모한 [PenanceFirst] 5당 기본 위력 +1 (최대 4)\n[EndSkill] 정신력이 15 감소하고 다음 턴에 [Emptiness] 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].desc ; dataList[id=1041005].levelList[level=4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [RedEyeFirst], [PenanceFirst], [EndSkill], [Emptiness]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence; [EndSkill] = [공격 종료시] / [Attack End]; [Emptiness] = 하얗게 태워버렸군 / Only Ashes Remain
   EN: [WhenUse] Consume all [RedEyeFirst] and [PenanceFirst] on self\n- Coin Power +1 for every 5 [RedEyeFirst] consumed (max 4)\n- Base Power +1 for every 5 [PenanceFirst] consumed (max 4)\n[EndSkill] Lose 15 SP and gain [Emptiness] next turn
   PL: [WhenUse] Zużywa całe posiadane [RedEyeFirst] i [PenanceFirst]\n- Moc Monet +1 za każde 5 zużytego [RedEyeFirst] (maks. 4)\n- Moc Bazowa +1 za każde 5 zużytego [PenanceFirst] (maks. 4)\n[EndSkill] Traci 15 Poczytalności i zyskuje w następnej turze [Emptiness]
336. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] (소모한 [RedEyeFirst]-15)만큼 [Laceration] 부여 (최대 5)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RedEyeFirst], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict [Laceration] equal to ([RedEyeFirst] consumed - 15) on target (max 5)
   PL: [OnSucceedAttack] Nakłada [Laceration] równy (zużyte [RedEyeFirst] - 15) (maks. 5)
337. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] 소모한 [RedEyeFirst], [PenanceFirst]당 피해량 +2.5% (최대 100%)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RedEyeFirst], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence
   EN: Deal +2.5% damage for every [RedEyeFirst] and [PenanceFirst] consumed (max 100%)
   PL: Zadaje +2.5% obrażeń za każdy 1 zużytego [RedEyeFirst] i [PenanceFirst] (maks. 100%)
338. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신과 현재 체력 비율이 가장 낮은 아군 1명이 각 대상의 최대 체력의 (소모한 [PenanceFirst]/2)%만큼 체력 회복\n- 최대 공명수 2당 회복 대상 수 1 증가 (최대 2명 증가)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the lowest HP percentage by ([PenanceFirst] consumed / 2)% of each unit's max HP\n- Heal 1 additional ally for every 2 highest Reson. (max 2 more allies)
   PL: [OnSucceedAttack] Odzyskuje HP sobie i 1 Sojusznikowi z najniższym procentem HP równe (zużyte [PenanceFirst]/2)% Maks. HP każdej z jednostek\n- Odzysk obejmuje o 1 sojusznika więcej za każde 2 najwyższego Rezonansu (maks. o 2)
339. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신과 현재 정신력이 가장 낮은 아군 1명을 (소모한 [PenanceFirst]-10)만큼 정신력 회복\n- 최대 공명수 2당 회복 대상 수 1 증가 (최대 2명 증가)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the least SP by ([PenanceFirst] consumed - 10) SP\n- Heal 1 additional ally for every 2 highest Reson. (max 2 more allies)
   PL: [OnSucceedAttack] Odzyskuje Poczytalność sobie i 1 sojusznikowi z najniższą Poczyt.  równą (zużyte [PenanceFirst] - 10)\n- Odzysk obejmuje o 1 sojusznika więcej za każde 2 najwyższego Rezonansu (maks. o 2)
340. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3, [Reduction] 2 부여 (턴 당 1회)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=3].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 3 [Binding] and 2 [Reduction] next turn (once per turn)
   PL: [OnSucceedAttack] Nakłada w następnej turze 3 [Binding] i 2 [Reduction] (1 raz na turę)
341. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] (소모한 [RedEyeFirst]-15)만큼 [Laceration] 부여 (최대 5)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [RedEyeFirst], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict [Laceration] equal to ([RedEyeFirst] consumed - 15) on target (max 5)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada [Laceration] równy (zużyte [RedEyeFirst] - 15) (maks. 5)<style="highlight"></style>
342. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] 소모한 [RedEyeFirst], [PenanceFirst]당 피해량 <style="highlight">+4%</style> (최대 <style="highlight">160%</style>)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [RedEyeFirst], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence
   EN: Deal <style="highlight">+4%</style> damage for every [RedEyeFirst] and [PenanceFirst] consumed (max <style="highlight">160%</style>)
   PL: Zadaje <style="highlight">+4%</style> obrażeń za każdy 1 zużytego [RedEyeFirst] i [PenanceFirst] (maks. <style="highlight">160%</style>)
343. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신과 현재 체력 비율이 가장 낮은 아군 1명이 각 대상의 최대 체력의 <style="highlight">(소모한 [PenanceFirst])%</style>만큼 체력 회복\n- 최대 공명수 2당 회복 대상 수 1 증가 (최대 2명 증가)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the lowest HP percentage by <style="highlight">([PenanceFirst] consumed)%</style> of each unit's max HP\n- Heal 1 additional ally for every 2 highest Reson. (max 2 more allies)
   PL: [OnSucceedAttack] Odzyskuje HP sobie i 1 Sojusznikowi z najniższym procentem HP równe <style="highlight">(zużyte [PenanceFirst])%</style> Maks. HP każdej z jednostek\n- Odzysk obejmuje o 1 sojusznika więcej za każde 2 najwyższego Rezonansu (maks. o 2)
344. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신과 현재 정신력이 가장 낮은 아군 1명을 (소모한 [PenanceFirst]-<style="highlight">5</style>)만큼 정신력 회복\n- 최대 공명수 2당 회복 대상 수 1 증가 (최대 2명 증가)
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Heal self and 1 ally with the least SP by ([PenanceFirst] consumed - <style="highlight">5</style>) SP\n- Heal 1 additional ally for every 2 highest Reson. (max 2 more allies)
   PL: [OnSucceedAttack] Odzyskuje Poczytalność sobie i 1 sojusznikowi z najniższą Poczyt.  równą (zużyte [PenanceFirst] - <style="highlight">5</style>)\n- Odzysk obejmuje o 1 sojusznika więcej za każde 2 najwyższego Rezonansu (maks. o 2)
345. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3, [Reduction] 2 부여 (턴 당 1회)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041005].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Binding], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 3 [Binding] and 2 [Reduction] next turn (once per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada w następnej turze 3 [Binding] i 2 [Reduction] (1 raz na turę)<style="highlight"></style>
346. [Obrona (ulepszenia 1,4) — nazwa] 먹고 잘 시간이다
   źródło: Skills_personality-04.json :: dataList[id=1041004].levelList[level=1].name ; dataList[id=1041004].levelList[level=4].name
   kontekst: grzech: Lust · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Mealtime, Bedtime
   PL: Czas na Jedzenie i Sen
347. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 2 얻음 (턴 당 1회)
   źródło: Skills_personality-04.json :: dataList[id=1041004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 2 [RedEyeFirst] (once per turn)
   PL: [OnSucceedAttack] Zyskuje 2 [RedEyeFirst] (1 raz na turę)
348. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 2 얻음 (턴 당 1회)
   źródło: Skills_personality-04.json :: dataList[id=1041004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 2 [PenanceFirst] (once per turn)
   PL: [OnSucceedAttack] Zyskuje 2 [PenanceFirst] (1 raz na turę)
349. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [RedEyeFirst] 2 얻음 (턴 당 1회)\n<style="highlight">- [RedEyeFirst]이 7 미만이면, [RedEyeFirst] 1 추가로 얻음</style>
   źródło: Skills_personality-04.json :: dataList[id=1041004].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [RedEyeFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [RedEyeFirst] = 적안 / Red Eyes
   EN: [OnSucceedAttack] Gain 2 [RedEyeFirst] (once per turn)\n<style="highlight">- At less than 7 [RedEyeFirst], gain +1 additional [RedEyeFirst]</style>
   PL: [OnSucceedAttack] Zyskuje 2 [RedEyeFirst] (1 raz na turę)\n<style="highlight">- Poniżej 7 [RedEyeFirst] zyskuje dodatkowo 1 [RedEyeFirst]</style>
350. [Obrona (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [PenanceFirst] 2 얻음 (턴 당 1회)\n<style="highlight">- [PenanceFirst]가 7 미만이면, [PenanceFirst] 1 추가로 얻음</style>
   źródło: Skills_personality-04.json :: dataList[id=1041004].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [PenanceFirst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PenanceFirst] = 참회 / Penitence
   EN: [OnSucceedAttack] Gain 2 [PenanceFirst] (once per turn)\n<style="highlight">- At less than 7 [PenanceFirst], gain +1 additional [PenanceFirst]</style>
   PL: [OnSucceedAttack] Zyskuje 2 [PenanceFirst] (1 raz na turę)\n<style="highlight">- Poniżej 7 [PenanceFirst] zyskuje dodatkowo 1 [PenanceFirst]</style>
351. [Pasywka bojowa (od ulepszenia 1) — nazwa] E.G.O 동화
   źródło: Passives.json :: dataList[id=1041002].name
   limit: do 40 znaków
   EN: E.G.O Assimilation
   PL: Asymilacja E.G.O
352. [Pasywka bojowa (od ulepszenia 1) — opis] [Charge] 횟수를 획득할 때, 대신 [RedEyeFirst] 또는 [PenanceFirst]를 얻음\n- [RedEyeFirst]과 [PenanceFirst]는 [Charge] 위력의 영향을 받지 않음
   źródło: Passives.json :: dataList[id=1041002].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [RedEyeFirst], [PenanceFirst]
   znaczenie tagów: [Charge] = 충전 / Charge; [RedEyeFirst] = 적안 / Red Eyes; [PenanceFirst] = 참회 / Penitence
   EN: When gaining [Charge] Count, gain [RedEyeFirst] or [PenanceFirst] instead\n- [RedEyeFirst] and [PenanceFirst] are unaffected by [Charge] Potency
   PL: Zyskując Licznik [Charge], zamiast tego zyskuje [RedEyeFirst] lub [PenanceFirst]\n- [RedEyeFirst] i [PenanceFirst] nie podlegają wpływowi Mocy [Charge]
353. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 충전 횟수를 획득할 때, 대신 적안 또는 참회를 얻음
   źródło: Passives.json :: dataList[id=1041002].summary
   limit: do 120 znaków
   EN: When gaining Charge Count, gain Red Eyes or Penitence instead
   PL: Zyskując Licznik Ładowania, zamiast tego zyskuje Czerwone Oko lub Pokutę
354. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust, posiadane 3× Gloom) — nazwa] 거미대가리 / 해골바가지
   źródło: Passives.json :: dataList[id=1041001].name
   limit: do 40 znaków
   EN: Spiderhead/Skullface
   PL: Pajęcza Łeba / Koścista Łeba
355. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust, posiadane 3× Gloom) — opis] [RedEyeFirst]을 얻는 코인을 사용하여 적에게 적중 시\n- 피해량이 ([RedEyeFirst]/2)%만큼 증가\n- 대상에게 [Laceration]이 있으면, [RedEyeFirst] 1 얻음 (턴 당 최대 3)\n\n[PenanceFirst]를 얻는 코인을 사용하여 적에게 적중 시\n- 피해량이 ([PenanceFirst]/2)%만큼 증가\n- 자신의 정신력이 20 이상이면 [PenanceFirst] 1 얻음 (턴 당 최대 3)
   źródło: Passives.json :: dataList[id=1041001].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [RedEyeFirst], [Laceration], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [Laceration] = 출혈 / Bleed; [PenanceFirst] = 참회 / Penitence
   EN: When hitting an enemy with a Coin that gains [RedEyeFirst]:\n- Deal +([RedEyeFirst]/2)% damage\n- If the target has [Laceration], gain 1 [RedEyeFirst] (3 times per turn)\n\nWhen hitting an enemy with a Coin that gains [PenanceFirst]:\n- Deal +([PenanceFirst]/2)% damage\n- At 20+ SP, gain 1 [PenanceFirst] (3 times per turn)
   PL: Przy trafieniu wroga monetą zyskującą [RedEyeFirst]\n- zadaje +([RedEyeFirst]/2)% obrażeń\n- jeżeli cel ma [Laceration], zyskuje 1 [RedEyeFirst] (maks. 3 na turę)\n\nPrzy trafieniu wroga monetą zyskującą [PenanceFirst]\n- zadaje +([PenanceFirst]/2)% obrażeń\n- przy Poczytalności 20+ zyskuje 1 [PenanceFirst] (maks. 3 na turę)
356. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Lust, posiadane 3× Gloom) — podsumowanie] 적안 얻는 코인의 피해량이 증가. 대상에게 출혈이 있으면, 적안 1 얻음\n참회 얻는 코인의 피해량이 증가. 자신의 정신력이 20 이상이면 참회 1 얻음
   źródło: Passives.json :: dataList[id=1041001].summary
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Coins that gain Red Eyes deal more damage; if the target has Bleed, gain 1 Red Eyes\nCoins that gain Penitence deal more damage; at 20+ SP, gain 1 Penitence
   PL: Monety zyskujące Czerwone Oko zadają więcej obrażeń; jeżeli cel ma Krwawienie, zyskuje 1 Czerwone Oko\nMonety zyskujące Pokutę zadają więcej obrażeń; przy Poczytalności 20+ zyskuje 1 Pokuty
357. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust, posiadane 3× Gloom) — nazwa] 거미대가리 / 해골바가지
   źródło: Passives.json :: dataList[id=1041011].name
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust, posiadane 3× Gloom) — opis] [RedEyeFirst]을 얻는 코인을 사용하여 적에게 적중 시\n- 피해량이 ([RedEyeFirst]/2)%만큼 증가\n<style="highlight">- 대상의 속도가 자신보다 3 이상 낮으면, 피해량이 ([RedEyeFirst]/2)%만큼 추가로 증가</style>\n- 대상에게 [Laceration]이 있으면, [RedEyeFirst] 1 얻음 (턴 당 최대 3)\n\n[PenanceFirst]를 얻는 코인을 사용하여 적에게 적중 시\n- 피해량이 ([PenanceFirst]/2)%만큼 증가\n<style="highlight">- 대상의 정신력이 자신보다 낮으면, 피해량이 ([PenanceFirst]/2)%만큼 추가로 증가 (정신력이 없는 대상일 경우, 0으로 계산)</style>\n- 자신의 정신력이 20 이상이면 [PenanceFirst] 1 얻음 (턴 당 최대 3)\n\n<style="highlight">적에게 피격 시, [PenanceFirst] 1 얻음 (최대 3)</style>
   źródło: Passives.json :: dataList[id=1041011].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [RedEyeFirst], [Laceration], [PenanceFirst]
   znaczenie tagów: [RedEyeFirst] = 적안 / Red Eyes; [Laceration] = 출혈 / Bleed; [PenanceFirst] = 참회 / Penitence
   EN: When hitting an enemy with a Coin that gains [RedEyeFirst]:\n- Deal +([RedEyeFirst]/2)% damage\n<style="highlight">- If this unit's Speed is faster than the target's by 3 or more, deal an additional +([RedEyeFirst]/2)% damage</style>\n- If the target has [Laceration], gain 1 [RedEyeFirst] (3 times per turn)\n\nWhen hitting an enemy with a Coin that gains [PenanceFirst]:\n- Deal +([PenanceFirst]/2)% damage\n<style="highlight">- If the target's SP is lower than this unit's, deal an additional +([PenanceFirst]/2)% damage(for targets that are Non-SP Units, their SP counts as 0)</style>\n- At 20+ SP, gain 1 [PenanceFirst] (3 times per turn)\n\n<style="highlight">When hit by an enemy, gain 1 [PenanceFirst] (max 3)</style>
   PL: Przy trafieniu wroga monetą zyskującą [RedEyeFirst]\n- zadaje +([RedEyeFirst]/2)% obrażeń\n<style="highlight">- jeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, zadaje dodatkowo +([RedEyeFirst]/2)% obrażeń</style>\n- jeżeli cel ma [Laceration], zyskuje 1 [RedEyeFirst] (maks. 3 na turę)\n\nPrzy trafieniu wroga monetą zyskującą [PenanceFirst]\n- zadaje +([PenanceFirst]/2)% obrażeń\n<style="highlight">- jeżeli Poczytalność celu jest niższa, zadaje dodatkowo +([PenanceFirst]/2)% obrażeń (cele bez Poczytalności liczone jako 0)</style>\n- przy Poczytalności 20+ zyskuje 1 [PenanceFirst] (maks. 3 na turę)\n\n<style="highlight">Przy trafieniu przez wroga zyskuje 1 [PenanceFirst] (maks. 3)</style>
359. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Lust, posiadane 3× Gloom) — podsumowanie] 적안 얻는 코인의 피해량이 증가. 대상에게 출혈이 있으면, 적안 1 얻음\n참회 얻는 코인의 피해량이 증가. 자신의 정신력이 20 이상이면 참회 1 얻음\n적에게 피격 시, 참회 1 얻음 (최대 3)
   źródło: Passives.json :: dataList[id=1041011].summary
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Coins that gain Red Eyes deal more damage; if the target has Bleed, gain 1 Red Eyes\nCoins that gain Penitence deal more damage; at 20+ SP, gain 1 Penitence\nWhen hit by an enemy, gain 1 Penitence (max 3)
   PL: Monety zyskujące Czerwone Oko zadają więcej obrażeń; jeżeli cel ma Krwawienie, zyskuje 1 Czerwone Oko\nMonety zyskujące Pokutę zadają więcej obrażeń; przy Poczytalności 20+ zyskuje 1 Pokuty\nPrzy trafieniu przez wroga zyskuje 1 Pokuty (maks. 3)
360. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — nazwa] 먹고 자라
   źródło: Passives.json :: dataList[id=1041021].name
   limit: do 40 znaków
   EN: Eat and Sleep
   PL: Jedz i Śpij
361. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — opis] 전투 시작 시\n- 체력 비율이 제일 낮은 아군 1명이 체력 3 회복\n- 정신력이 제일 낮은 아군 1명이 정신력 3 회복
   źródło: Passives.json :: dataList[id=1041021].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Combat Start:\n- 1 ally with the lowest HP percentage heals 3 HP\n- 1 ally with the least SP heals 3 SP
   PL: Na początku walki:\n- 1 Sojusznik z najniższym procentem HP odzyskuje 3 HP\n- 1 Sojusznik z najniższą Poczytalnością odzyskuje 3 Poczytalności
362. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Envy) — podsumowanie] 체력 비율 제일 낮은 아군 체력 회복, 정신력 제일 낮은 아군 정신력 회복
   źródło: Passives.json :: dataList[id=1041021].summary
   limit: do 120 znaków
   EN: Heal HP for 1 ally with the lowest HP percentage, heal SP for 1 ally with the least SP
   PL: Odzysk HP dla 1 Sojusznika z najniższym procentem HP, odzysk Poczytalności dla 1 Sojusznika z najniższą Poczytalnością

## [000] Heishou Pack - Mao Branch — Ryōshū — 흑수 - 묘
- ID Tożsamości: `10411` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 5 · HP bazowe: 69 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Rupture

363. [Karta Tożsamości — tytuł] 흑수 - 묘
   źródło: Personalities.json :: dataList[id=10411].title
   limit: do 40 znaków
   EN: Heishou Pack - Mao Branch
   PL: Wataha Heishou - Gałąź Mao
364. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10411].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
365. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10411].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Karta Tożsamości — opis] 료슈의 열한번째 인격
   źródło: Personalities.json :: dataList[id=10411].desc
   limit: do 120 znaków
   EN: Ryōshū's 11th Identity
   PL: Jedenasta Tożsamość Ryōshū
367. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 순보
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=1].name ; dataList[id=1041101].levelList[level=2].name ; dataList[id=1041101].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Blinkstep
   PL: Szybki Krok
368. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 6+ [Burst], Coin Power +1
   PL: [WhenUse] Jeżeli cel ma 6+ [Burst], Moc Monet +1
369. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL: [OnSucceedAttack] Nakłada 1 [Burst]
370. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]
371. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상의 [Burst]이 <style="highlight">4</style> 이상이면, 코인 위력 +1\n<style="highlight">[WinDuel] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] If target has <style="highlight">4</style>+ [Burst], Coin Power +1\n<style="highlight">[WinDuel] Inflict +1 [Burst] Count</style>
   PL: [WhenUse] Jeżeli cel ma <style="highlight">4</style>+ [Burst], Moc Monet +1\n<style="highlight">[WinDuel] Zwiększa Licznik [Burst] o 1</style>
372. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1041101].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Burst]<style="highlight"></style>
373. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041101].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Burst]<style="highlight"></style>
374. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬당 1회)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=2].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] At 10+ Speed, Reuse Coin once (once per Skill)</style>
   PL: <style="highlight">[OnSucceedAttack] Przy 10+ Szybkości używa monety ponownie (1 raz na Umiejętność)</style>
375. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">자신의 속도가 대상보다 3 이상 높으면, 코인 위력 +1</style>\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: <style="highlight">If this unit's Speed is faster than the target's by 3 or more, Coin Power +1</style>\n[WhenUse] If target has 4+ [Burst], Coin Power +1\n[WinDuel] Inflict +1 [Burst] Count
   PL: <style="highlight">Jeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, Moc Monet +1</style>\n[WhenUse] Jeżeli cel ma 4+ [Burst], Moc Monet +1\n[WinDuel] Zwiększa Licznik [Burst] o 1
376. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041101].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Speed, Reuse Coin once (once per Skill)<style="highlight"></style>
   PL: [OnSucceedAttack] Przy 10+ Szybkości używa monety ponownie (1 raz na Umiejętność)<style="highlight"></style>
377. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 새겨진대로
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=1].name ; dataList[id=1041102].levelList[level=2].name ; dataList[id=1041102].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Slash · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: As Written
   PL: Zgodnie z Wyrytym
378. [Umiejętność 2 (×2) (ulepszenie 1) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n[WhenUse] 대상의 [Burst]이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\n[WhenUse] If target has 6+ [Burst], Coin Power +1
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x Moc [Burst] celu)% obrażeń (maks. 50%)\n[WhenUse] Jeżeli cel ma 6+ [Burst], Moc Monet +1
379. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +10%
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   EN: At 10+ Speed, deal +10% damage
   PL: Przy 10+ Szybkości zadaje +10% obrażeń
381. [Umiejętność 2 (×2) (ulepszenie 2) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n[WhenUse] 대상의 [Burst]이 <style="highlight">4</style> 이상이면, 코인 위력 +1\n<style="highlight">[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴 당 1회)\n[WinDuel] [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=2].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [WhenUse], [Agility], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\n[WhenUse] If target has <style="highlight">4</style>+ [Burst], Coin Power +1\n<style="highlight">[WhenUse] Gain 2 [Agility] next turn (once per turn)\n[WinDuel] Inflict +1 [Burst] Count</style>
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x Moc [Burst] celu)% obrażeń (maks. 50%)\n[WhenUse] Jeżeli cel ma <style="highlight">4</style>+ [Burst], Moc Monet +1\n<style="highlight">[WhenUse] Zyskuje w następnej turze 2 [Agility] (1 raz na turę)\n[WinDuel] Zwiększa Licznik [Burst] celu o 1</style>
382. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1041102].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 372 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 자신의 속도가 10 이상이면, [Burst] 횟수 1 증가</style>
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] At 10+ Speed, inflict +1 [Burst] Count</style>
   PL: <style="highlight">[OnSucceedAttack] Przy 10+ Szybkości zwiększa Licznik [Burst] celu o 1</style>
384. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +<style="highlight">20</style>%
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: At 10+ Speed, deal +<style="highlight">20</style>% damage
   PL: Przy 10+ Szybkości zadaje +<style="highlight">20</style>% obrażeń
385. [Umiejętność 2 (×2) (ulepszenie 4) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n<style="highlight">자신의 속도가 대상보다 3 이상 높으면, 코인 위력 +1</style>\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴 당 1회)\n[WinDuel] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=4].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [WhenUse], [Agility], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\n<style="highlight">If this unit's Speed is faster than the target's by 3 or more, Coin Power +1</style>\n[WhenUse] If target has 4+ [Burst], Coin Power +1\n[WhenUse] Gain 2 [Agility] next turn (once per turn)\n[WinDuel] Inflict +1 [Burst] Count
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x Moc [Burst] celu)% obrażeń (maks. 50%)\n<style="highlight">Jeżeli Szybkość tej jednostki jest większa od celu o 3 lub więcej, Moc Monet +1</style>\n[WhenUse] Jeżeli cel ma 4+ [Burst], Moc Monet +1\n[WhenUse] Zyskuje w następnej turze 2 [Agility] (1 raz na turę)\n[WinDuel] Zwiększa Licznik [Burst] celu o 1
386. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] At 10+ Speed, inflict +1 [Burst] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Przy 10+ Szybkości zwiększa Licznik [Burst] celu o 1<style="highlight"></style>
387. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +<style="highlight">30</style>%
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: At 10+ Speed, deal +<style="highlight">30</style>% damage
   PL: Przy 10+ Szybkości zadaje +<style="highlight">30</style>% obrażeń
388. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 2 — opis] <style="highlight">[OnSucceedAttack] [Burst] 1 부여</style>
   źródło: Skills_personality-04.json :: dataList[id=1041102].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[OnSucceedAttack] Inflict 1 [Burst]</style>
   PL: <style="highlight">[OnSucceedAttack] Nakłada 1 [Burst]</style>
389. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 저주가 새겨진 검을 쑤셔주지
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].name ; dataList[id=1041103].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 5 · monety: 3 (+4)
   limit: do 60 znaków
   EN: I'll gut you with a curse-engraved blade
   PL: Podpiszę cię klątwą wyrytą na ostrzu
390. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n자신의 속도가 대상보다 2 이상 높으면 코인 위력 +1\n[WhenUse] [LegStrength] 3 얻음\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [WhenUse], [LegStrength], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\nIf this unit's Speed is faster than the target's by 2 or more, Coin Power +1\n[WhenUse] Gain 3 [LegStrength]\n[WinDuel] Inflict +2 [Burst] Count
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x Moc [Burst] celu)% obrażeń (maks. 50%)\nJeżeli Szybkość tej jednostki jest większa od celu o 2 lub więcej, Moc Monet +1\n[WhenUse] Zyskuje 3 [LegStrength]\n[WinDuel] Zwiększa Licznik [Burst] celu o 2
391. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 370 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstAgility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: [OnSucceedAttack] Inflict [BurstAgility]
   PL: [OnSucceedAttack] Nakłada [BurstAgility]
393. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +30%
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: At 10+ Speed, deal +30% damage
   PL: Przy 10+ Szybkości zadaje +30% obrażeń
395. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL: [OnSucceedAttack] Nakłada 3 [Burst]
396. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬당 1회)
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] At 10+ Speed, Reuse Coin once (once per Skill)
   PL: [OnSucceedAttack] Przy 10+ Szybkości używa monety ponownie (1 raz na Umiejętność)
397. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 자신의 속도가 대상보다 빠르면, (대상과의 속도 차이 x 대상의 [Burst] 위력)%만큼 피해량이 증가 (최대 50%)\n자신의 속도가 대상보다 <style="highlight">높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 2)\n[WhenUse] 대상의 [Burst]이 15 이상이면, 코인 위력 +1</style>\n[WhenUse] [LegStrength] 3 얻음\n[WinDuel] [Burst] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [Burst], [WhenUse], [LegStrength], [WinDuel]
   znaczenie tagów: [Burst] = 파열 / Rupture; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's, deal +(Speed difference x [Burst] Potency on target)% damage (max 50%)\nIf this unit's Speed is faster than the target's, <style="highlight">gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 2)\n[WhenUse] If target has 15+ [Burst], Coin Power +1</style>\n[WhenUse] Gain 3 [LegStrength]\n[WinDuel] Inflict +2 [Burst] Count
   PL: Jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +(różnica Szybkości x Moc [Burst] celu)% obrażeń (maks. 50%)\nJeżeli Szybkość tej jednostki jest większa niż celu, <style="highlight">zyskuje Moc Monet zależnie od różnicy Szybkości (Moc Monet +1 za każde 2 różnicy Szybkości; maks. 2)\n[WhenUse] Jeżeli cel ma 15+ [Burst], Moc Monet +1</style>\n[WhenUse] Zyskuje 3 [LegStrength]\n[WinDuel] Zwiększa Licznik [Burst] celu o 2
398. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [BurstAgility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: [OnSucceedAttack] Inflict [BurstAgility]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada [BurstAgility]<style="highlight"></style>
400. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 372 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 자신의 속도가 10 이상이면, 피해량 +30%<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: At 10+ Speed, deal +30% damage<style="highlight"></style>
   PL: Przy 10+ Szybkości zadaje +30% obrażeń<style="highlight"></style>
402. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Burst]<style="highlight"></style>
403. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 속도가 10 이상이면, 코인 1회 재사용 (스킬당 1회)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] <style="highlight">[ReUseOnSucceedAttack] [BurstAgility] 부여</style>
   źródło: Skills_personality-04.json :: dataList[id=1041103].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ReUseOnSucceedAttack], [BurstAgility]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: <style="highlight">[ReUseOnSucceedAttack] Inflict [BurstAgility]</style>
   PL: <style="highlight">[ReUseOnSucceedAttack] Nakłada [BurstAgility]</style>
405. [Obrona (ulepszenia 1,4) — nazwa] 각력. 해방. 훗
   źródło: Skills_personality-04.json :: dataList[id=1041104].levelList[level=1].name ; dataList[id=1041104].levelList[level=4].name
   kontekst: grzech: Glut. · typ: obrona: kontra · moc bazowa: 5 · monety: 1 (+8)
   limit: do 40 znaków
   EN: Strider. Unleashed. Heh
   PL: Siła Nóg. Wyzwolenie. Hę
406. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] [LegStrength] 3 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041104].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [LegStrength]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [DuelCounter]\n[WhenUse] Gain 3 [LegStrength]
   PL: [DuelCounter]\n[WhenUse] Zyskuje 3 [LegStrength]
407. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 370 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[WhenUse] [LegStrength] 3 얻음\n<style="highlight">[WhenUse] 자신의 속도가 대상보다 높을수록, 기본 위력 +1 (속도 차이 2 당 기본 위력 +1. 최대 2)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041104].levelList[level=4].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [WhenUse], [LegStrength]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [DuelCounter]\n[WhenUse] Gain 3 [LegStrength]\n<style="highlight">[WhenUse] If this unit's Speed is faster than the target's, gain Base Power based on Speed difference (Base Power +1 for every 2 Speed difference; max 2)</style>
   PL: [DuelCounter]\n[WhenUse] Zyskuje 3 [LegStrength]\n<style="highlight">[WhenUse] Jeżeli Szybkość tej jednostki jest większa niż celu, zyskuje Moc Bazową zależnie od różnicy Szybkości (Moc Bazowa +1 za każde 2 różnicy Szybkości; maks. 2)</style>
409. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041104].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — nazwa] 흑수화[묘]
   źródło: Passives.json :: dataList[id=1041101].name
   limit: do 40 znaków
   EN: Heishou Mutation [Mao]
   PL: Mutacja Heishou [Mao]
411. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Glut.) — opis] 자신에게 [LegStrength]가 있으면 가하는 피해량 +5%
   źródło: Passives.json :: dataList[id=1041101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [LegStrength]
   znaczenie tagów: [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: If this unit has [LegStrength], deal +5% damage
   PL: Jeżeli ta jednostka ma [LegStrength], zadaje +5% obrażeń
412. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Glut.) — nazwa] 흑수화[묘]
   źródło: Passives.json :: dataList[id=1041111].name
   (powtórzenie elementu 410 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Pasywka bojowa (od ulepszenia 4, posiadane 3× Glut.) — opis] 자신에게 [LegStrength]가 있으면 가하는 피해량 +5%\n대상에게 [BurstAgility]이 있으면 가하는 피해량 +5%
   źródło: Passives.json :: dataList[id=1041111].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [LegStrength], [BurstAgility]
   znaczenie tagów: [LegStrength] = 각력【묘】 / Strider【Mao】; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: If this unit has [LegStrength], deal +5% damage\nIf the target has [BurstAgility], deal +5% damage
   PL: Jeżeli ta jednostka ma [LegStrength], zadaje +5% obrażeń\nJeżeli cel ma [BurstAgility], zadaje +5% obrażeń
414. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — nazwa] 부분 흑수화 수련
   źródło: Passives.json :: dataList[id=1041121].name
   limit: do 50 znaków
   EN: Partial Heishou Mutation Training
   PL: Trening Częściowej Mutacji Heishou
415. [Pasywka wsparcia (od ulepszenia 3, posiadane 5× Glut.) — opis] 턴 종료시 속도가 가장 빠른 아군 1명이 다음 턴에 [Agility] 2 얻음
   źródło: Passives.json :: dataList[id=1041121].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Turn End: 1 ally with the fastest Speed gains 2 [Agility] next turn
   PL: Na koniec tury 1 Sojusznik z najwyższą Szybkością zyskuje w następnej turze 2 [Agility]

## [000] N Corp. E.G.O:: Contempt, Awe — Ryōshū — N사 E.G.O:: 경멸, 경외
- ID Tożsamości: `10412` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 69 · szybkość: 3–6 / 3–7 / 4–7 / 4–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Bleed, Tremor

416. [Karta Tożsamości — tytuł] N사 E.G.O::\n경멸, 경외
   źródło: Personalities.json :: dataList[id=10412].title
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: N Corp. E.G.O::\nContempt, Awe
   PL: E.G.O N Corp.::\nPogarda, Groza
417. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10412].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10412].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Karta Tożsamości — opis] 료슈의 열두번째 인격
   źródło: Personalities.json :: dataList[id=10412].desc
   limit: do 120 znaków
   EN: Ryōshū's 12th Identity
   PL: Dwunasta Tożsamość Ryōshū
420. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 경멸스러운 것
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=1].name ; dataList[id=1041201].levelList[level=2].name ; dataList[id=1041201].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Contemptuous Thing
   PL: Rzecz Pełna Pogardy
421. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 대상에게 [GazeRyoshu] 또는 [ContemptRyoshu]이 있으면, 합 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [GazeRyoshu], [ContemptRyoshu]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt
   EN: [WhenUse] If target has [GazeRyoshu] or [ContemptRyoshu], Clash Power +1
   PL: [WhenUse] Jeżeli cel ma [GazeRyoshu] lub [ContemptRyoshu], Moc Starcia +1
422. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [GazeRyoshu] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1041201].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041201].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [GazeRyoshu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GazeRyoshu] = 시선 / Gaze
   EN: [OnSucceedAttack] Inflict 1 [GazeRyoshu]
   PL: [OnSucceedAttack] Nakłada 1 [GazeRyoshu]
423. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상에게 [GazeRyoshu] 또는 [ContemptRyoshu]이 있으면, 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=2].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [GazeRyoshu], [ContemptRyoshu], [Laceration], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has [GazeRyoshu] or [ContemptRyoshu], Clash Power +1\n[WhenUse] At 6+ ([Laceration] + [Vibration]) on target, Coin Power +1
   PL: [WhenUse] Jeżeli cel ma [GazeRyoshu] lub [ContemptRyoshu], Moc Starcia +1\n[WhenUse] Przy 6+ (suma [Laceration] i [Vibration] celu) Moc Monet +1
424. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1041201].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1041201].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL: [OnSucceedAttack] Nakłada +1 Licznika [Laceration]
426. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상에게 [GazeRyoshu] 또는 [ContemptRyoshu]이 있으면, 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 6<style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041201].levelList[level=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [GazeRyoshu], [ContemptRyoshu], [Laceration], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has [GazeRyoshu] or [ContemptRyoshu], Clash Power +1\n[WhenUse] <style="highlight">Coin Power +1 for every 6 ([Laceration] + [Vibration]) on target (max 2)</style>
   PL: [WhenUse] Jeżeli cel ma [GazeRyoshu] lub [ContemptRyoshu], Moc Starcia +1\n[WhenUse] Moc Monet +1 za każde 6 (suma [Laceration] i [Vibration] celu) (maks. 2)
427. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 경외하라
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=1].name ; dataList[id=1041202].levelList[level=2].name ; dataList[id=1041202].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Penetrate · moc bazowa: 4 · monety: 2 (+6)
   limit: do 40 znaków
   EN: Be Awed
   PL: Trzeba Być pod Wrażeniem
428. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 대상에게 [GazeRyoshu] 또는 [ContemptRyoshu]이 있으면, 합 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=1].desc
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1041202].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] Nakłada 1 [Vibration]
430. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1041202].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 1 [Laceration]
   PL: [OnSucceedAttack] Nakłada 1 [Laceration]
431. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1041202].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041202].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
432. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [GazeRyoshu] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상에게 [GazeRyoshu] 또는 [ContemptRyoshu]이 있으면, 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=2].desc
   (powtórzenie elementu 423 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1041202].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=2].coinlist[#1].coindescs[#2].desc ; dataList[id=1041202].levelList[level=4].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [GazeRyoshu] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=2].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [GazeRyoshu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GazeRyoshu] = 시선 / Gaze
   EN: [OnSucceedAttack] Inflict 1 [GazeRyoshu]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [GazeRyoshu]<style="highlight"></style>
437. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 5 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수가 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=2].coinlist[#1].coindescs[#4].desc ; dataList[id=1041202].levelList[level=4].coinlist[#1].coindescs[#4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] If target has 3+ [Vibration] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Jeżeli cel ma 3+ Licznika [Vibration], [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
438. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상에게 [GazeRyoshu] 또는 [ContemptRyoshu]이 있으면, 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 6<style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=4].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [GazeRyoshu] <style="highlight">2</style> 부여
   źródło: Skills_personality-04.json :: dataList[id=1041202].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [GazeRyoshu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GazeRyoshu] = 시선 / Gaze
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [GazeRyoshu]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [GazeRyoshu]
442. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 경외, 경멸
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].name ; dataList[id=1041203].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Awe, Contempt
   PL: Groza, Pogarda
443. [Umiejętność 3 (×1) (ulepszenie 3) — opis] 대상에게 [GazeRyoshu]이 있으면, 이 스킬에서 부여하는 [Laceration], [Vibration] 위력 +2\n[BeforeUse] 모든 적에게 부여된 [GazeRyoshu]의 합이 7 이상 또는 [ContemptRyoshu]의 합이 1 이상이면, ‘<noparse>경멸</noparse> 밑으로 쏟아지는 경외의 시선’으로 발동됨\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합이 8 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 1당, 피해량 +1% (최대 20%)
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [GazeRyoshu], [Laceration], [Vibration], [BeforeUse], [ContemptRyoshu], [WhenUse]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [BeforeUse] = [사용전] / [Before Use]; [ContemptRyoshu] = 경멸 / Contempt; [WhenUse] = [사용시] / [On Use]
   EN: If target has [GazeRyoshu], this Skill inflicts +2 more [Laceration] and [Vibration] potency\n[BeforeUse] At 7+ (sum of [GazeRyoshu] on all enemies), or at 1+ (sum of [ContemptRyoshu] on all enemies), activates 'Cascading <noparse>Gaze</noparse> of <noparse>Awe</noparse> Underneath <noparse>Contempt</noparse>' instead\n[WhenUse] At 8+ ([Laceration] + [Vibration]) on target, Coin Power +1\n[WhenUse] Deal +1% damage for every ([Laceration] + [Vibration]) on target (max 20%)
   PL: Jeżeli cel ma [GazeRyoshu], ta Umiejętność nakłada o 2 więcej Mocy [Laceration] i [Vibration]\n[BeforeUse] Przy 7+ (sumie [GazeRyoshu] na wszystkich wrogach) lub 1+ (sumie [ContemptRyoshu]) uruchamia zamiast tego „<noparse>Pogarda</noparse> pod Wznoszącą się Grozą”\n[WhenUse] Przy 8+ (suma [Laceration] i [Vibration] celu) Moc Monet +1\n[WhenUse] Zadaje +1% obrażeń za każde 1 (suma [Laceration] i [Vibration] celu) (maks. 20%)
444. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 430 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1041203].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1041203].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1041203].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] 대상의 [GazeRyoshu] 1당 피해량 +5% (최대 35%)
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [GazeRyoshu]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze
   EN: Deal +5% damage for every 1 [GazeRyoshu] on target (max 35%)
   PL: Zadaje +5% obrażeń za każde 1 [GazeRyoshu] na celu (maks. 35%)
450. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [GazeRyoshu] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [GazeRyoshu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GazeRyoshu] = 시선 / Gaze
   EN: [OnSucceedAttack] Inflict 2 [GazeRyoshu]
   PL: [OnSucceedAttack] Nakłada 2 [GazeRyoshu]
451. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationBleeding]로 [Switch_Vibration]
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#2].coindescs[#3].desc ; dataList[id=1041203].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationBleeding], [Switch_Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationBleeding] = 진동 - 과다출혈 / Tremor - Hemorrhage; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [Switch_Vibration] into [VibrationBleeding]
   PL: [UnBrokenCoinOnSucceedAttack] Wywołuje [Switch_Vibration] do [VibrationBleeding]
452. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 5 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=3].coinlist[#2].coindescs[#4].desc ; dataList[id=1041203].levelList[level=4].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
453. [Umiejętność 3 (×1) (ulepszenie 4) — opis] 대상에게 [GazeRyoshu]이 있으면, 이 스킬에서 부여하는 [Laceration], [Vibration] 위력 +2<style="highlight"></style>\n[BeforeUse] 모든 적에게 부여된 [GazeRyoshu]의 합이 7 이상 또는 [ContemptRyoshu]의 합이 1 이상이면, ‘<noparse>경멸</noparse> 밑으로 쏟아지는 경외의 시선’으로 발동됨\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 8<style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 1당, 피해량 +1% (최대 <style="highlight">40</style>%)
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=4].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, <noparse>, </noparse>, \n, [GazeRyoshu], [Laceration], [Vibration], [BeforeUse], [ContemptRyoshu], [WhenUse]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [BeforeUse] = [사용전] / [Before Use]; [ContemptRyoshu] = 경멸 / Contempt; [WhenUse] = [사용시] / [On Use]
   EN: If target has [GazeRyoshu], this Skill inflicts +2 more [Laceration] and [Vibration] potency<style="highlight"></style>\n[BeforeUse] At 7+ (sum of [GazeRyoshu] on all enemies), or at 1+ (sum of [ContemptRyoshu] on all enemies), activates 'Cascading <noparse>Gaze</noparse> of <noparse>Awe</noparse> Underneath <noparse>Contempt</noparse>' instead\n[WhenUse] <style="highlight">Coin Power +1 for every 8 ([Laceration] + [Vibration]) on target (max 2)</style>\n[WhenUse] Deal +1% damage for every ([Laceration] + [Vibration]) on target (max <style="highlight">40</style>%)
   PL: Jeżeli cel ma [GazeRyoshu], ta Umiejętność nakłada o 2 więcej Mocy [Laceration] i [Vibration]<style="highlight"></style>\n[BeforeUse] Przy 7+ (sumie [GazeRyoshu] na wszystkich wrogach) lub 1+ (sumie [ContemptRyoshu]) uruchamia zamiast tego „<noparse>Pogarda</noparse> pod Wznoszącą się Grozą”\n[WhenUse] Moc Monet +1 za każde 8 (suma [Laceration] i [Vibration] celu) (maks. 2)\n[WhenUse] Zadaje +1% obrażeń za każde 1 (suma [Laceration] i [Vibration] celu) (maks. <style="highlight">40</style>%)
454. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] 대상의 [GazeRyoshu] 1당 피해량 +<style="highlight">10</style>% (최대 <style="highlight">70</style>%)
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [GazeRyoshu]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze
   EN: Deal +<style="highlight">10</style>% damage for every 1 [GazeRyoshu] on target (max <style="highlight">70</style>%)
   PL: Zadaje +<style="highlight">10</style>% obrażeń za każde 1 [GazeRyoshu] na celu (maks. <style="highlight">70</style>%)
457. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [GazeRyoshu] 3 부여
   źródło: Skills_personality-04.json :: dataList[id=1041203].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [GazeRyoshu]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GazeRyoshu] = 시선 / Gaze
   EN: [OnSucceedAttack] Inflict 3 [GazeRyoshu]
   PL: [OnSucceedAttack] Nakłada 3 [GazeRyoshu]
458. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 경멸 밑으로 쏟아지는 경외의 시선
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].name ; dataList[id=1041205].levelList[level=4].name
   kontekst: grzech: Lust · typ: Penetrate · moc bazowa: 14 · monety: 1 (+14)
   limit: do 60 znaków
   EN: Cascading Gaze of Awe Underneath Contempt
   PL: Pogarda pod Wznoszącą się Grozą
459. [Umiejętność 4 (×0) (ulepszenie 3) — opis] 이 스킬은 외부 효과로 재사용이 불가능함\n[GazeRyoshu] 또는 [ContemptRyoshu]을 보유한 적을 서브 타겟으로 우선 지정함\n- 서브 타겟에게 가하는 피해량 -50%\n공격 대상이 1명이면, 피해량 +200% (집중 전투일 경우, 부위로 판정)\n[WhenUse] 메인 타겟 대상의 [Laceration]과 [Vibration]의 합 4당, 코인 위력 +1 (최대 2)\n[WhenUse] 메인 타겟 대상의 [Laceration]과 [Vibration]의 합 1당, 피해량 +2% (최대 50%)\n[WhenUse] 모든 공격 대상에게 부여된 [GazeRyoshu]의 합 1당, 피해량 +7% (최대 49%)\n[EndSkill] 적중한 모든 대상의 [GazeRyoshu] 또는 [ContemptRyoshu] 전부 소모
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: \n, [GazeRyoshu], [ContemptRyoshu], [WhenUse], [Laceration], [Vibration], [EndSkill]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: External effects cannot trigger this Skill to be Reused\nPrioritizes targeting enemies that have [GazeRyoshu] or [ContemptRyoshu] as sub-targets\n- Deals -50% damage against sub-targets\nIf there is just a single target, deal +200% damage (for Focused Encounters, a Part)\n[WhenUse] Coin Power +1 for every 4 ([Laceration] + [Vibration]) on the main target (max 2)\n[WhenUse] Deal +2% damage for every ([Laceration] + [Vibration]) on the main target (max 50%)\n[WhenUse] Deal +7% damage for every 1 (sum of [GazeRyoshu] on all attack targets) (max 49%)\n[EndSkill] Consumes [GazeRyoshu] or [ContemptRyoshu] on all targets that were hit
   PL: Zewnętrzne efekty nie mogą ponownie uruchomić tej Umiejętności\nNamierza wroga z [GazeRyoshu] lub [ContemptRyoshu] jako cel drugorzędny\n- Zadaje -50% obrażeń celom drugorzędnym\nPrzy 1 celu zadaje +200% obrażeń (w walce skupionej: część ciała)\n[WhenUse] Moc Monet +1 za każde 4 (suma [Laceration] i [Vibration] głównego celu) (maks. 2)\n[WhenUse] Zadaje +2% obrażeń za każde 1 (suma [Laceration] i [Vibration] głównego celu) (maks. 50%)\n[WhenUse] Zadaje +7% obrażeń za każde 1 (suma [GazeRyoshu] na wszystkich celach ataku) (maks. 49%)\n[EndSkill] Zużywa [GazeRyoshu] lub [ContemptRyoshu] wszystkich trafionych celów
460. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1041205].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] 대상에게 [ContemptRyoshu]이 있으면, 피해량 +180%
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ContemptRyoshu]
   znaczenie tagów: [ContemptRyoshu] = 경멸 / Contempt
   EN: If target has [ContemptRyoshu], deal +180% damage
   PL: Jeżeli cel ma [ContemptRyoshu], zadaje +180% obrażeń
462. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 3 부여, [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and +1 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada 3 [Vibration] i zwiększa Licznik [Vibration] o 1
463. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +1 [Laceration] Count
   PL: [OnSucceedAttack] Nakłada 3 [Laceration] i zwiększa Licznik [Laceration] o 1
464. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [VibrationBleeding]로 [Switch_Vibration]
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].coinlist[#0].coindescs[#4].desc ; dataList[id=1041205].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationBleeding], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationBleeding] = 진동 - 과다출혈 / Tremor - Hemorrhage; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationBleeding]
   PL: [OnSucceedAttack] Wywołuje [Switch_Vibration] do [VibrationBleeding]
465. [Umiejętność 4 (×0) (ulepszenia 3–4) — moneta 1, efekt 6 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=3].coinlist[#0].coindescs[#5].desc ; dataList[id=1041205].levelList[level=4].coinlist[#0].coindescs[#5].desc
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Umiejętność 4 (×0) (ulepszenie 4) — opis] 이 스킬은 외부 효과로 재사용이 불가능함\n[GazeRyoshu] 또는 [ContemptRyoshu]을 보유한 적을 서브 타겟으로 우선 지정함<style="highlight"></style>\n- 서브 타겟에게 가하는 피해량 -50%\n공격 대상이 1명이면, 피해량 +200% (집중 전투일 경우, 부위로 판정)\n[WhenUse] 메인 타겟 대상의 [Laceration]과 [Vibration]의 합 4당, 코인 위력 +1 (최대 <style="highlight">4</style>)\n[WhenUse] 메인 타겟 대상의 [Laceration]과 [Vibration]의 합 1당, 피해량 +2% (최대 <style="highlight">100</style>%)\n[WhenUse] 모든 공격 대상에게 부여된 [GazeRyoshu]의 합 1당, 피해량 +10% (최대 70%)\n[EndSkill] 적중한 모든 대상의 [GazeRyoshu] 또는 [ContemptRyoshu] 전부 소모
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=4].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [GazeRyoshu], [ContemptRyoshu], [WhenUse], [Laceration], [Vibration], [EndSkill]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: External effects cannot trigger this Skill to be Reused\nPrioritizes targeting enemies that have [GazeRyoshu] or [ContemptRyoshu] as sub-targets<style="highlight"></style>\n- Deals -50% damage against sub-targets\nIf there is just a single target, deal +200% damage (for Focused Encounters, a Part)\n[WhenUse] Coin Power +1 for every 4 ([Laceration] + [Vibration]) on the main target (max <style="highlight">4</style>)\n[WhenUse] Deal +2% damage for every ([Laceration] + [Vibration]) on the main target (max <style="highlight">100</style>%)\n[WhenUse] Deal +10% damage for every 1 (sum of [GazeRyoshu] on all attack targets) (max 70%)\n[EndSkill] Consumes [GazeRyoshu] or [ContemptRyoshu] on all targets that were hit
   PL: Zewnętrzne efekty nie mogą ponownie uruchomić tej Umiejętności\nNamierza wroga z [GazeRyoshu] lub [ContemptRyoshu] jako cel drugorzędny<style="highlight"></style>\n- Zadaje -50% obrażeń celom drugorzędnym\nPrzy 1 celu zadaje +200% obrażeń (w walce skupionej: część ciała)\n[WhenUse] Moc Monet +1 za każde 4 (suma [Laceration] i [Vibration] głównego celu) (maks. <style="highlight">4</style>)\n[WhenUse] Zadaje +2% obrażeń za każde 1 (suma [Laceration] i [Vibration] głównego celu) (maks. <style="highlight">100</style>%)\n[WhenUse] Zadaje +10% obrażeń za każde 1 (suma [GazeRyoshu] na wszystkich celach ataku) (maks. 70%)\n[EndSkill] Zużywa [GazeRyoshu] lub [ContemptRyoshu] wszystkich trafionych celów
467. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 2 — opis] 대상에게 [ContemptRyoshu]이 있으면, 피해량 +<style="highlight">235</style>%
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [ContemptRyoshu]
   znaczenie tagów: [ContemptRyoshu] = 경멸 / Contempt
   EN: If target has [ContemptRyoshu], deal +<style="highlight">235</style>% damage
   PL: Jeżeli cel ma [ContemptRyoshu], zadaje +<style="highlight">235</style>% obrażeń
468. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 4 부여, [Vibration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada 4 [Vibration] i zwiększa Licznik [Vibration] o 2
469. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041205].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] Nakłada 4 [Laceration] i zwiększa Licznik [Laceration] o 2
470. [Umiejętność 5 (×0) (ulepszenia 3–4) — nazwa] 쏘아내겠소 / 언제든지
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].name ; dataList[id=1041206].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 2 (+7)
   limit: do 40 znaków
   EN: I Shall Fire / Anytime
   PL: Przyjmę Ostrzał / Zawsze
471. [Umiejętność 5 (×0) (ulepszenie 3) — opis] [StartBattle] N사 E.G.O::<noparse>경멸</noparse>, 경외 료슈 우선 공격\n[StartBattle] 자신의 [BoseProjektil] 3당, 공격 가중치 +1 (최대 2)\n[WhenUse] 자신의 [Breath]이 5 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [BoseProjektil]당, [Breath] 1 얻음 (최대 7)\n[EndSkill] 자신의 ([BoseProjektil] X 2) 만큼 정신력 감소 (최대 14 감소)\n[EndSkill] 전투 시작 시 자신의 [BoseProjektil]이 7이면, 전부 소모하고 자신의 정신력 20 회복
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [StartBattle], [BoseProjektil], [WhenUse], [Breath], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [StartBattle] Prioritizes N Corp. E.G.O::<noparse>Contempt</noparse>, Awe Ryōshū\n[StartBattle] Gain +1 Atk Weight for every 3 [BoseProjektil] on self (max 2)\n[WhenUse] At 5+ [Breath], Coin Power +1\n[WhenUse] At 3+ [Breath] Count, Base Power +1\n[WhenUse] Gain 1 [Breath] for every [BoseProjektil] on self (max 7)\n[EndSkill] Lose ([BoseProjektil] on self x 2) SP (max 14)\n[EndSkill] If this unit has 7 [BoseProjektil] at Combat Start, lose them all and heal 20 SP on self
   PL: [StartBattle] Namierza najpierw E.G.O N Corp.::<noparse>Pogarda</noparse>, Groza Ryōshū\n[StartBattle] Waga ataku +1 za każde 3 [BoseProjektil] (maks. 2)\n[WhenUse] Przy 5+ [Breath] Moc Monet +1\n[WhenUse] Przy 3+ Liczniku [Breath] Moc Bazowa +1\n[WhenUse] Zyskuje 1 [Breath] za każde 1 [BoseProjektil] (maks. 7)\n[EndSkill] Traci (własne [BoseProjektil] x 2) Poczytalności (maks. 14)\n[EndSkill] Jeżeli na początku walki ma 7 [BoseProjektil], zużywa je w całości i odzyskuje 20 Poczytalności
472. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1041206].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] 이 코인에는 메인 타겟만 피해를 입음
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1041206].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin deals damage only against the main target
   PL: Ta moneta zadaje obrażenia tylko głównemu celowi
474. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] 이 코인에는 서브 타겟만 피해를 입음
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin deals damage only against the sub-targets
   PL: Ta moneta zadaje obrażenia tylko celom drugorzędnym
476. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 2, efekt 3 — opis] - 첫번째 코인 피해가 크리티컬이 아니고, N사 E.G.O::<noparse>경멸</noparse>, 경외 료슈가 생존했다면, 서브 타겟 중 무작위 1명이 피해를 입음
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#2].desc ; dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n
   EN: - If the first Coin wasn't a Critical Hit, and if N Corp. E.G.O::<noparse>Contempt</noparse>, Awe Ryōshū survived, 1 random sub-target takes damage
   PL: - Jeżeli pierwsza moneta nie była trafieniem krytycznym, a E.G.O N Corp.::<noparse>Pogarda</noparse>, Groza Ryōshū przeżyła, 1 losowy cel drugorzędny otrzymuje obrażenia
477. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 4 — opis] 자신의 [BoseProjektil]당 피해량 +30% (최대 210%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: Deal +30% damage for every [BoseProjektil] on self (max 210%)
   PL: Zadaje +30% obrażeń za każde 1 [BoseProjektil] (maks. 210%)
478. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 5 — opis] [Breath] 위력당, 크리티컬 피해량 +2.5% (최대 25%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: +2.5% Damage on Critical Hit for every [Breath] Potency (max <style="highlight">25%</style>)
   PL: +2,5% obrażeń Krytycznych za każdą Moc [Breath] (maks. 25%)
479. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 6 — opis] 자신의 [BoseProjektil]당, 크리티컬 피해량 +7% (최대 49%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: +7% Damage on Critical Hit for every [BoseProjektil] on self (max 49%)
   PL: +7% obrażeń Krytycznych za każde [BoseProjektil] na tej jednostce (maks. 49%)
480. [Umiejętność 5 (×0) (ulepszenia 3–4) — moneta 2, efekt 7 — opis] 메인 타겟의 잃은 체력 비율만큼 피해량이 증가 (최대 100%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#6].desc ; dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#6].desc
   limit: do 120 znaków
   EN: Deal +1% damage for every 1% missing HP on the main target (max 100%)
   PL: Zadaje +1% obrażeń za każde 1% brakującego HP głównego celu (maks. 100%)
481. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 2, efekt 8 — opis] [OnSucceedAttack] [Laceration] 3 부여, [Laceration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=3].coinlist[#1].coindescs[#7].desc
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Umiejętność 5 (×0) (ulepszenie 4) — opis] [StartBattle] N사 E.G.O::<noparse>경멸</noparse>, 경외 료슈 우선 공격\n[StartBattle] 자신의 [BoseProjektil] 3당, 공격 가중치 +1 (최대 2)\n[WhenUse] 자신의 [Breath]이 5 <style="highlight">당</style>, 코인 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 3 <style="highlight">당</style>, 기본 위력 +1 <style="highlight">(최대 2)</style>\n[WhenUse] 자신의 [BoseProjektil]당, [Breath] 1 얻음 (최대 7)\n[EndSkill] 자신의 ([BoseProjektil] X 2) 만큼 정신력 감소 (최대 14 감소)\n[EndSkill] 전투 시작 시 자신의 [BoseProjektil]이 7이면, 전부 소모하고 자신의 정신력 20 회복
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=4].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, <style="highlight">, </style>, \n, [StartBattle], [BoseProjektil], [WhenUse], [Breath], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [BoseProjektil] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [StartBattle] Prioritizes N Corp. E.G.O::<noparse>Contempt</noparse>, Awe Ryōshū\n[StartBattle] Gain +1 Atk Weight for every 3 [BoseProjektil] on self (max 2)\n[WhenUse] <style="highlight">Coin Power +1 for every 5 [Breath] on self (max 2)</style>\n[WhenUse] <style="highlight">Base Power +1 for every 3 [Breath] Count on self (max 2)</style>\n[WhenUse] Gain 1 [Breath] for every [BoseProjektil] on self (max 7)\n[EndSkill] Lose ([BoseProjektil] on self x 2) SP (max 14)\n[EndSkill] If this unit has 7 [BoseProjektil] at Combat Start, lose them all and heal 20 SP on self
   PL: [StartBattle] Namierza najpierw E.G.O N Corp.::<noparse>Pogarda</noparse>, Groza Ryōshū\n[StartBattle] Waga ataku +1 za każde 3 [BoseProjektil] (maks. 2)\n[WhenUse] Moc Monet +1 za każde 5 [Breath] (maks. 2)\n[WhenUse] Moc Bazowa +1 za każde 3 Licznika [Breath] (maks. 2)\n[WhenUse] Zyskuje 1 [Breath] za każde 1 [BoseProjektil] (maks. 7)\n[EndSkill] Traci (własne [BoseProjektil] x 2) Poczytalności (maks. 14)\n[EndSkill] Jeżeli na początku walki ma 7 [BoseProjektil], zużywa je w całości i odzyskuje 20 Poczytalności
483. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 4 — opis] 자신의 [BoseProjektil]당 피해량 +<style="highlight">40</style>% (최대 <style="highlight">280</style>%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: Deal +<style="highlight">40</style>% damage for every [BoseProjektil] on self (max <style="highlight">280</style>%)
   PL: Zadaje +<style="highlight">40</style>% obrażeń za każde 1 [BoseProjektil] (maks. <style="highlight">280</style>%)
484. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 5 — opis] [Breath] 위력당, 크리티컬 피해량 +<style="highlight">5</style>% (최대 <style="highlight">50</style>%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: +<style="highlight">5</style>% Damage on Critical Hit for every [Breath] Potency (max <style="highlight">50</style>%)
   PL: +<style="highlight">5</style>% obrażeń Krytycznych za każdą Moc [Breath] (maks. <style="highlight">50</style>%)
485. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 6 — opis] 자신의 [BoseProjektil]당, 크리티컬 피해량 +<style="highlight">10</style>% (최대 <style="highlight">70</style>%)
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [BoseProjektil]
   znaczenie tagów: [BoseProjektil] = 찢어진 추억 / Torn Memory
   EN: +<style="highlight">10</style>% Damage on Critical Hit for every [BoseProjektil] on self (max <style="highlight">70</style>%)
   PL: +<style="highlight">10</style>% obrażeń Krytycznych za każde [BoseProjektil] na tej jednostce (maks. <style="highlight">70</style>%)
486. [Umiejętność 5 (×0) (ulepszenie 4) — moneta 2, efekt 8 — opis] [OnSucceedAttack] [Laceration] 5 부여, [Laceration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041206].levelList[level=4].coinlist[#1].coindescs[#7].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration] and +2 [Laceration] Count
   PL: [OnSucceedAttack] Nakłada 5 [Laceration] i zwiększa Licznik [Laceration] o 2
487. [Obrona (ulepszenia 1,4) — nazwa] 움켜쥔다
   źródło: Skills_personality-04.json :: dataList[id=1041204].levelList[level=1].name ; dataList[id=1041204].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: blok · moc bazowa: 10 · monety: 1 (+5)
   limit: do 40 znaków
   EN: To Grasp
   PL: Chwyt
488. [Obrona (ulepszenie 1) — opis] [StartBattle] 자신에게 [ContemptPersonality]이 없고 모든 적에게 부여된 [GazeRyoshu]의 합이 7 이상 또는 [ContemptRyoshu]의 합이 1 이상이면, [ContemptPersonality] 획득 (턴 당 1회)\n[WhenUse] 자신에게 [ContemptPersonality]이 있으면, 최종 위력 +5\n[WhenUse] 이 스킬 사용 중 피격시, 공격자의 [Laceration] 횟수 1 증가 (턴 당 3회 발동)
   źródło: Skills_personality-04.json :: dataList[id=1041204].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [ContemptPersonality], [GazeRyoshu], [ContemptRyoshu], [WhenUse], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ContemptPersonality] = 시선의 경멸 / Contempt of the Gaze; [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [StartBattle] If this unit does not have [ContemptPersonality], and at 7+ (sum of [GazeRyoshu] on all enemies) or 1+ (sum of [ContemptRyoshu] on all enemies), gain [ContemptPersonality] (once per turn)\n[WhenUse] If this unit has [ContemptPersonality], Final Power +5\n[WhenUse] When hit while using this Skill, inflict +1 [Laceration] Count against the attacker (3 times per turn)
   PL: [StartBattle] Jeżeli ta jednostka nie ma [ContemptPersonality], a suma [GazeRyoshu] na wszystkich wrogach wynosi 7+ lub suma [ContemptRyoshu] wynosi 1+, zyskuje [ContemptPersonality] (1 raz na turę)\n[WhenUse] Jeżeli ta jednostka ma [ContemptPersonality], Moc Końcowa +5\n[WhenUse] Gdy zostaje trafiona podczas używania tej Umiejętności, zwiększa Licznik [Laceration] atakującego o 1 (3 razy na turę)
489. [Obrona (ulepszenie 4) — opis] [StartBattle] 자신에게 [ContemptPersonality]이 없고 모든 적에게 부여된 [GazeRyoshu]의 합이 7 이상 또는 [ContemptRyoshu]의 합이 1 이상이면, [ContemptPersonality] 획득 (턴 당 1회)\n[WhenUse] 자신에게 [ContemptPersonality]이 있으면, 최종 위력 +10\n[WhenUse] 이 스킬 사용 중 피격시, 공격자의 [Laceration] 횟수 1 증가 (턴 당 3회 발동)
   źródło: Skills_personality-04.json :: dataList[id=1041204].levelList[level=4].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [ContemptPersonality], [GazeRyoshu], [ContemptRyoshu], [WhenUse], [Laceration]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ContemptPersonality] = 시선의 경멸 / Contempt of the Gaze; [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [StartBattle] If this unit does not have [ContemptPersonality], and at 7+ (sum of [GazeRyoshu] on all enemies) or 1+ (sum of [ContemptRyoshu] on all enemies), gain [ContemptPersonality] (once per turn)\n[WhenUse] If this unit has [ContemptPersonality], Final Power +10\n[WhenUse] When hit while using this Skill, inflict +1 [Laceration] Count against the attacker (3 times per turn)
   PL: [StartBattle] Jeżeli ta jednostka nie ma [ContemptPersonality], a suma [GazeRyoshu] na wszystkich wrogach wynosi 7+ lub suma [ContemptRyoshu] wynosi 1+, zyskuje [ContemptPersonality] (1 raz na turę)\n[WhenUse] Jeżeli ta jednostka ma [ContemptPersonality], Moc Końcowa +10\n[WhenUse] Gdy zostaje trafiona podczas używania tej Umiejętności, zwiększa Licznik [Laceration] atakującego o 1 (3 razy na turę)
490. [Pasywka bojowa (od ulepszenia 1) — nazwa] 쓰러질 수조차 없게 붙드는 손아귀
   źródło: Passives.json :: dataList[id=1041202].name
   limit: do 40 znaków
   EN: Grasp that Forbids Falling
   PL: Uchwyt Nie Pozwalający Paść
491. [Pasywka bojowa (od ulepszenia 1) — opis] 흐트러짐 상태가 되면, [Protection] 4를 얻고 다음 턴에 [ContemptPersonality] 획득 (전투 당 1회)\n\n사망 시, [GazeRyoshu] 또는 [ContemptRyoshu]이 많은 순으로 적 3명에게 아래 효과 적용 (집중 전투일 경우, 부위로 판정)\n- 다음 턴에 [Binding] 2 부여\n- [Laceration] 2 부여, [Laceration] 횟수 1 증가\n- [Vibration] 2 부여, [Vibration] 횟수 1 증가
   źródło: Passives.json :: dataList[id=1041202].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [Protection], [ContemptPersonality], [GazeRyoshu], [ContemptRyoshu], [Binding], [Laceration], [Vibration]
   znaczenie tagów: [Protection] = 보호 / Protection; [ContemptPersonality] = 시선의 경멸 / Contempt of the Gaze; [GazeRyoshu] = 시선 / Gaze; [ContemptRyoshu] = 경멸 / Contempt; [Binding] = 속박 / Bind; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: When Staggered, gain 4 [Protection] and gain [ContemptPersonality] next turn (once per Encounter)\n\nOn death, apply the following effects against 3 enemies that have the most [GazeRyoshu] or [ContemptRyoshu] (in descending order; in Focused Encounters, Parts)\n- Inflict 2 [Binding] next turn\n- Inflict 2 [Laceration] and +1 [Laceration] Count\n- Inflict 2 [Vibration] and +1 [Vibration] Count
   PL: Po Ogłuszeniu zyskuje 4 [Protection] i zyskuje [ContemptPersonality] w następnej turze (1 raz na spotkanie)\n\nPo śmierci stosuje na 3 wrogach z największą liczbą [GazeRyoshu] lub [ContemptRyoshu] (w walce skupionej: częściach ciała) poniższe efekty:\n- Nakłada w następnej turze 2 [Binding]\n- Nakłada 2 [Laceration] i zwiększa Licznik [Laceration] o 1\n- Nakłada 2 [Vibration] i zwiększa Licznik [Vibration] o 1
492. [Pasywka bojowa (od ulepszenia 1) — nazwa] 너희 모두 재밌는 걸 보여주지
   źródło: Passives.json :: dataList[id=1041203].name
   limit: do 70 znaków
   EN: Let me show everyone something very interesting
   PL: Pokażmy wszystkim coś bardzo ciekawego
493. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 시작 시 N사 E.G.O::<noparse>흉탄</noparse> 이상의 ‘대상 조정 사격’이 아래 효과 얻음\n- 사용 전 N사 E.G.O::<noparse>경멸</noparse>, 경외 료슈가 [ContemptPersonality]을 보유 중이고, 기본 스킬을 사용할 수 있으면, 대신 ‘쏘아내겠소 / 언제든지’를 료슈에게 사용함 (턴 당 1회. ‘쏘아내겠소 / 언제든지’는 이상의 동기화 단계가 적용됨)\n- 사용 전 N사 E.G.O::<noparse>경멸</noparse>, 경외 료슈가 메인 타겟이 아니고, 기본 스킬을 사용할 수 있으면, 료슈가 메인 타겟을 스킬 1로 일방공격함 (턴 당 1회. [CantIdentify]. 스킬 1의 피해량 -50%. 해당 스킬로 메인 타겟이 사망하지 않음)
   źródło: Passives.json :: dataList[id=1041203].desc
   limit: do 820 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [ContemptPersonality], [CantIdentify]
   znaczenie tagów: [ContemptPersonality] = 시선의 경멸 / Contempt of the Gaze; [CantIdentify] = [피아식별불가] / [Indiscriminate]
   EN: Combat Start: N Corp. E.G.O::<noparse>Fell Bullet</noparse> Yi Sang's 'Target Readjustment Fire' Skill gains the following effects:\n- Before using the Skill, if N Corp. E.G.O::<noparse>Contempt</noparse>, Awe Ryōshū has [ContemptPersonality] and can use her base Skills, use "I Shall Fire / Anytime" against Ryōshū (once per turn; 'I Shall Fire / Anytime' reflects Yi Sang's Uptie Tier)\n- Before using the Skill, if the Skill's main target isn't N Corp. E.G.O::<noparse>Contempt</noparse>, Awe Ryōshū, and if she can use her base Skills, Ryōshū uses her Skill 1 as an Unopposed Attack against the main target (once per turn; [CantIdentify]; Skill 1 deals -50% damage; the Skill does not kill the main target)
   PL: Na początku walki Umiejętność „Korekta Celowania Ogniem” E.G.O N Corp.::<noparse>Przebity Pocisk</noparse> Yi Sang zyskuje poniższe efekty:\n- Przed użyciem Umiejętności, jeżeli E.G.O N Corp.::<noparse>Pogarda</noparse>, Groza Ryōshū ma [ContemptPersonality] i może użyć podstawowych Umiejętności, używa „Przyjmę Ostrzał / Zawsze” na Ryōshū (1 raz na turę; „Przyjmę Ostrzał / Zawsze” odzwierciedla poziom Uptie Yi Sanga)\n- Przed użyciem Umiejętności, jeżeli głównym celem nie jest E.G.O N Corp.::<noparse>Pogarda</noparse>, Groza Ryōshū i ona może użyć podstawowych Umiejętności, Ryōshū używa swojej Umiejętności 1 jako ataku nieopartego na głównym celu (1 raz na turę; [CantIdentify]; Umiejętność 1 zadaje -50% obrażeń; ta Umiejętność nie zabija głównego celu)
494. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Lust) — nazwa] 놓쳤던 @#$의 손
   źródło: Passives.json :: dataList[id=1041201].name
   limit: do 40 znaków
   EN: @#$'s Hand I Let Slip
   PL: @#$- ręka, której pozwoliłam ujść
495. [Pasywka bojowa (od ulepszenia 2, rezonans 2× Lust) — opis] 적에게 공격 적중 시, [GazeRyoshu] 1 부여 (적 당 턴 당 최대 1회)\n- 자신에게 [GazePersonality]이 있으면, [GazeRyoshu] 1 추가 부여\n\n적에게 피격 시, 공격자에게 [GazeRyoshu] 1 부여 (스킬 당 최대 1회, 턴 당 최대 3회)\n- 자신에게 [ContemptPersonality]이 있으면, 공격자의 마지막 코인 적중 시 공격자에게 해당 코인으로 받은 피해량의 10%만큼 나태 속성 피해를 입힘 (스킬 당 최대 10, 턴 당 최대 30)\n\n기본 공격 스킬로 적의 [GazeRyoshu] 또는 [ContemptRyoshu]을 소모했다면,\n다음 턴에 (소모한 적의 [GazeRyoshu]/2 + 소모한 적의 [ContemptRyoshu]x3)만큼 [GazePersonality] 획득 (턴 당 최대 6. 소수점 버림)
   źródło: Passives.json :: dataList[id=1041201].desc
   limit: do 840 znaków
   tokeny: zachowaj dokładnie: \n, [GazeRyoshu], [GazePersonality], [ContemptPersonality], [ContemptRyoshu]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze; [GazePersonality] = 경멸의 시선 / Gaze of Contempt; [ContemptPersonality] = 시선의 경멸 / Contempt of the Gaze; [ContemptRyoshu] = 경멸 / Contempt
   EN: On Hit against enemies, inflict 1 [GazeRyoshu] (once per turn per enemy)\n- If this unit has [GazePersonality], inflict +1 more [GazeRyoshu]\n\nWhen hit by an enemy, inflict 1 [GazeRyoshu] against the attacker (once per Skill; 3 times per turn)\n- If this unit has [ContemptPersonality]: when hit by the attacker's final Coin, inflict (10% of the damage dealt by that final Coin) Sloth damage (max 10 per Skill; max 30 per turn)\n\nIf this unit used its Base Attack Skills to consume [GazeRyoshu] or [ContemptRyoshu] on an enemy:\nNext turn, gain ((enemy's [GazeRyoshu] consumed/2) + (enemy's [ContemptRyoshu] consumed x 3)) [GazePersonality] (6 per turn; rounded down)
   PL: Przy trafieniu wroga nakłada 1 [GazeRyoshu] (maks. 1 raz na turę na wroga)\n- Jeżeli ta jednostka ma [GazePersonality], nakłada o 1 więcej [GazeRyoshu]\n\nPrzy trafieniu przez wroga nakłada 1 [GazeRyoshu] na atakującego (maks. 1 raz na Umiejętność, 3 razy na turę)\n- Jeżeli ta jednostka ma [ContemptPersonality], gdy ostatnia moneta atakującego trafi, zadaje atakującemu obrażenia Lenistwa równe 10% obrażeń otrzymanych od tej monety (maks. 10 na Umiejętność, maks. 30 na turę)\n\nJeżeli ta jednostka zużyła podstawowymi Umiejętnościami ataku [GazeRyoshu] lub [ContemptRyoshu] wroga, zyskuje w następnej turze [GazePersonality] równy (zużyte [GazeRyoshu] wroga/2 + zużyte [ContemptRyoshu] wroga x 3) (maks. 6 na turę, zaokrąglone w dół)
496. [Pasywka bojowa (od ulepszenia 4, rezonans 2× Lust) — nazwa] 놓쳤던 @#$의 손
   źródło: Passives.json :: dataList[id=1041211].name
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Pasywka bojowa (od ulepszenia 4, rezonans 2× Lust) — opis] 적에게 공격 적중 시, [GazeRyoshu] <style="highlight">2</style> 부여 (적 당 턴 당 최대 1회)\n- 자신에게 [GazePersonality]이 있으면, [GazeRyoshu] 1 추가 부여\n\n적에게 피격 시, 공격자에게 [GazeRyoshu] 1 부여 (스킬 당 최대 1회, 턴 당 최대 3회)\n- 자신에게 [ContemptPersonality]이 있으면, 공격자의 마지막 코인 적중 시 공격자에게 해당 코인으로 받은 피해량의 <style="highlight">20</style>%만큼 나태 속성 피해를 입힘 (스킬 당 최대 <style="highlight">20</style>, 턴 당 최대 <style="highlight">60</style>)\n\n기본 공격 스킬로 적의 [GazeRyoshu] 또는 [ContemptRyoshu]을 소모했다면,\n다음 턴에 (소모한 적의 [GazeRyoshu]/2 + 소모한 적의 [ContemptRyoshu]x3)만큼 [GazePersonality] 획득 (턴 당 최대 6. 소수점 버림)
   źródło: Passives.json :: dataList[id=1041211].desc
   limit: do 840 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [GazeRyoshu], [GazePersonality], [ContemptPersonality], [ContemptRyoshu]
   znaczenie tagów: [GazeRyoshu] = 시선 / Gaze; [GazePersonality] = 경멸의 시선 / Gaze of Contempt; [ContemptPersonality] = 시선의 경멸 / Contempt of the Gaze; [ContemptRyoshu] = 경멸 / Contempt
   EN: On Hit against enemies, inflict <style="highlight">2</style> [GazeRyoshu] (once per turn per enemy)\n- If this unit has [GazePersonality], inflict +1 more [GazeRyoshu]\n\nWhen hit by an enemy, inflict 1 [GazeRyoshu] against the attacker (once per Skill; 3 times per turn)\n- If this unit has [ContemptPersonality]: when hit by the attacker's final Coin, inflict (<style="highlight">20</style>% of the damage dealt by that final Coin) Sloth damage (max <style="highlight">20</style> per Skill; max <style="highlight">60</style> per turn)\n\nIf this unit used its Base Attack Skills to consume [GazeRyoshu] or [ContemptRyoshu] on an enemy:\nNext turn, gain ((enemy's [GazeRyoshu] consumed/2) + (enemy's [ContemptRyoshu] consumed x 3)) [GazePersonality] (6 per turn; rounded down)
   PL: Przy trafieniu wroga nakłada <style="highlight">2</style> [GazeRyoshu] (maks. 1 raz na turę na wroga)\n- Jeżeli ta jednostka ma [GazePersonality], nakłada o 1 więcej [GazeRyoshu]\n\nPrzy trafieniu przez wroga nakłada 1 [GazeRyoshu] na atakującego (maks. 1 raz na Umiejętność, 3 razy na turę)\n- Jeżeli ta jednostka ma [ContemptPersonality], gdy ostatnia moneta atakującego trafi, zadaje atakującemu obrażenia Lenistwa równe <style="highlight">20</style>% obrażeń otrzymanych od tej monety (maks. <style="highlight">20</style> na Umiejętność, maks. <style="highlight">60</style> na turę)\n\nJeżeli ta jednostka zużyła podstawowymi Umiejętnościami ataku [GazeRyoshu] lub [ContemptRyoshu] wroga, zyskuje w następnej turze [GazePersonality] równy (zużyte [GazeRyoshu] wroga/2 + zużyte [ContemptRyoshu] wroga x 3) (maks. 6 na turę, zaokrąglone w dół)
498. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — nazwa] 그건 흐르고 울린다
   źródło: Passives.json :: dataList[id=1041221].name
   limit: do 40 znaków
   EN: It flows and cries
   PL: To płynie i jęczy
499. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — opis] 편성 순서가 가장 빠른 아군 1명이 적에게 공격 적중 시, [Laceration] 1 부여 (적 당 턴 당 최대 1회)\n- 대상에게 [Laceration]이 있으면, 추가로 [Laceration] 횟수 1 증가\n\n편성 순서가 가장 빠른 아군 1명이 적에게 피격시, 공격자에게 [Vibration] 1 부여 (턴 당 최대 3회)\n- 공격자에게 [Vibration]이 있으면, 추가로 [Vibration] 횟수 1 증가
   źródło: Passives.json :: dataList[id=1041221].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Vibration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: If the ally with the earliest Deployment order hits an enemy using its attack, inflict 1 [Laceration] (once per enemy per turn)\n- If target has [Laceration], inflict +1 [Laceration] Count as well\n\nIf the ally with the earliest Deployment order is hit by an enemy, inflict 1 [Vibration] against the attacker (3 times per turn)\n- If the attacker has [Vibration], inflict +1 [Vibration] Count as well
   PL: Gdy 1 Sojusznik przydzielony najwcześniej trafia wroga atakiem, nakłada 1 [Laceration] (maks. 1 raz na turę na wroga)\n- Jeżeli cel ma [Laceration], dodatkowo zwiększa Licznik [Laceration] o 1\n\nGdy 1 Sojusznik przydzielony najwcześniej zostaje trafiona przez wroga, nakłada 1 [Vibration] na atakującego (3 razy na turę)\n- Jeżeli atakujący ma [Vibration], dodatkowo zwiększa Licznik [Vibration] o 1
500. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Lust) — podsumowanie] 적에게 적중 시, [Laceration] 부여하고 이미 있다면 추가로 횟수 증가\n적에게 피격 시, [Vibration] 부여하고 이미 있다면 추가로 횟수 증가
   źródło: Passives.json :: dataList[id=1041221].summary
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Vibration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: On Hit, inflict [Laceration]; inflict Count as well if the target already has the effect\nWhen Hit, inflict [Vibration]; inflict Count as well if the target already has the effect
   PL: Przy trafieniu nakłada [Laceration]; jeżeli cel już go ma, dodatkowo zwiększa Licznik\nPrzy trafieniu przez wroga nakłada [Vibration]; jeżeli cel już go ma, dodatkowo zwiększa Licznik

## [000] Drifting Blade of Hongyuan — Ryōshū — 홍원 방랑무사
- ID Tożsamości: `10413` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 6 · HP bazowe: 82 · szybkość: 3–6 / 4–6 / 4–7 / 4–7
- odporności: Slash ×2 (Fatal), Penetrate ×0,5 (Endured), Hit ×1 (Normal) · słowa kluczowe: Poise, Rupture

501. [Karta Tożsamości — tytuł] 홍원 방랑무사
   źródło: Personalities.json :: dataList[id=10413].title
   limit: do 40 znaków
   EN: Drifting Blade of Hongyuan
   PL: Wędrowne Ostrze Hongyuan
502. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10413].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10413].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Karta Tożsamości — opis] 료슈의 열세번째 인격
   źródło: Personalities.json :: dataList[id=10413].desc
   limit: do 120 znaków
   EN: Ryōshū's 13th Identity
   PL: Trzynasta Tożsamość Ryōshū
505. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 어이, 물러서라
   źródło: Skills_personality-04.json :: dataList[id=1041301].levelList[level=1].name ; dataList[id=1041301].levelList[level=2].name ; dataList[id=1041301].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 6 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Hey, Back Off
   PL: Hej, Odstąp
506. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 1 증가\n[OnDirectAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [OnDirectAttack], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [OnDirectAttack] = [일방 공격 시] / [On Unopposed Attack]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Gain +1 [Breath] Count\n[OnDirectAttack] Inflict +1 [Burst] Count
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 1\n[OnDirectAttack] Zwiększa Licznik [Burst] celu o 1
507. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [Breath] 횟수 1 증가\n[OnDirectAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041301].levelList[level=2].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Burst], [OnDirectAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [OnDirectAttack] = [일방 공격 시] / [On Unopposed Attack]
   EN: <style="highlight">[WhenUse] At 6+ ([Breath] on self + [Burst] on target), Coin Power +1</style>\n[WhenUse] Gain +1 [Breath] Count\n[OnDirectAttack] Inflict +1 [Burst] Count
   PL: <style="highlight">[WhenUse] Przy 6+ (suma własnej Mocy [Breath] i Mocy [Burst] celu) Moc Monet +1</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 1\n[OnDirectAttack] Zwiększa Licznik [Burst] celu o 1
509. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] <style="highlight">2</style> 부여
   źródło: Skills_personality-04.json :: dataList[id=1041301].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Burst]
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Burst]
510. [Umiejętność 1 (×3) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력 합 6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 1 증가\n[OnDirectAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041301].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Burst], [OnDirectAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture; [OnDirectAttack] = [일방 공격 시] / [On Unopposed Attack]
   EN: <style="highlight">[WhenUse] Coin Power +1 for every 6 ([Breath] on self + [Burst] on target) (max 2)</style>\n[WhenUse] Gain +1 [Breath] Count\n[OnDirectAttack] Inflict +1 [Burst] Count
   PL: <style="highlight">[WhenUse] Moc Monet +1 za każde 6 (suma własnej Mocy [Breath] i Mocy [Burst] celu) (maks. 2)</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 1\n[OnDirectAttack] Zwiększa Licznik [Burst] celu o 1
511. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 1 — opis] <style="highlight">크리티컬 피해량 +20%</style>
   źródło: Skills_personality-04.json :: dataList[id=1041301].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: <style="highlight">+20% Damage on Critical Hit</style>
   PL: <style="highlight">+20% obrażeń przy trafieniu krytycznym</style>
512. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041301].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Burst]<style="highlight"></style>
513. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 1, efekt 3 — opis] <style="highlight">[CriticalOnSucceedAttack] [Burst] 1 부여</style>
   źródło: Skills_personality-04.json :: dataList[id=1041301].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Burst] = 파열 / Rupture
   EN: <style="highlight">[CriticalOnSucceedAttack] Inflict 1 [Burst]</style>
   PL: <style="highlight">[CriticalOnSucceedAttack] Nakłada 1 [Burst]</style>
514. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 명기누골[銘肌鏤骨]
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=1].name ; dataList[id=1041302].levelList[level=2].name ; dataList[id=1041302].levelList[level=4].name
   kontekst: grzech: Glut. · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 50 znaków
   EN: Engraved in Flesh and Bone [銘肌鏤骨]
   PL: Wyryte w Ciele i Kości [銘肌鏤骨]
515. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=1].desc
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 370 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] (대상의 [Burst] / 5) + 1 만큼 [Breath] 얻음 (최대 6. 소수점 버림)
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain [Breath] equal to (([Burst] on target / 5) + 1) (max 6; rounded down)
   PL: [OnSucceedAttack] Zyskuje [Breath] równy (([Burst] celu / 5) + 1) (maks. 6, zaokrąglone w dół)
518. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] Nakłada 2 [Burst]
519. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Burst] = 파열 / Rupture
   EN: [CriticalOnSucceedAttack] Inflict 1 [Burst]
   PL: [CriticalOnSucceedAttack] Nakłada 1 [Burst]
520. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력 합이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: <style="highlight">[WhenUse] At 6+ ([Breath] on self + [Burst] on target), Coin Power +1</style>\n[WhenUse] Gain +2 [Breath] Count
   PL: <style="highlight">[WhenUse] Przy 6+ (suma własnej Mocy [Breath] i Mocy [Burst] celu) Moc Monet +1</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
521. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict <style="highlight">+2</style> [Burst] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Burst] celu o <style="highlight">2</style>
522. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] (대상의 [Burst] / 5) + 1 만큼 [Breath] 얻음 (최대 6. 소수점 버림)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain [Breath] equal to (([Burst] on target / 5) + 1) (max 6; rounded down)<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje [Breath] równy (([Burst] celu / 5) + 1) (maks. 6, zaokrąglone w dół)<style="highlight"></style>
523. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=2].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=2].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Burst] = 파열 / Rupture
   EN: [CriticalOnSucceedAttack] Inflict 1 [Burst]<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Nakłada 1 [Burst]<style="highlight"></style>
525. [Umiejętność 2 (×2) (ulepszenie 4) — opis] <style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력 합 6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: <style="highlight">[WhenUse] Coin Power +1 for every 6 ([Breath] on self + [Burst] on target) (max 2)</style>\n[WhenUse] Gain +2 [Breath] Count
   PL: <style="highlight">[WhenUse] Moc Monet +1 za każde 6 (suma własnej Mocy [Breath] i Mocy [Burst] celu) (maks. 2)</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 2
526. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Zwiększa Licznik [Burst] celu o 2<style="highlight"></style>
527. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] (대상의 [Burst] / 5) + <style="highlight">2</style> 만큼 [Breath] 얻음 (최대 6. 소수점 버림)
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Burst], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain [Breath] equal to (([Burst] on target / 5) + <style="highlight">2</style>) (max 6; rounded down)
   PL: [OnSucceedAttack] Zyskuje [Breath] równy (([Burst] celu / 5) + <style="highlight">2</style>) (maks. 6, zaokrąglone w dół)
528. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] <style="highlight">크리티컬 피해량 +20%</style>
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 511 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041302].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 가척아원[加斥我援]
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=3].name ; dataList[id=1041303].levelList[level=4].name
   kontekst: grzech: Pride · typ: Penetrate · moc bazowa: 4 · monety: 4 (+3)
   limit: do 40 znaków
   EN: Aiding Strike [加斥我援]
   PL: Cios Wsparcia [加斥我援]
532. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] [ProtectStanceRyoshu] 2 얻음\n[WhenUse] 대상의 부정적인 효과가 3개 이상이면, 최종 위력 +1\n[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력 합이 6 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=3].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ProtectStanceRyoshu], [Breath], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ProtectStanceRyoshu] = 호위태세 / Protector's Stance; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: [WhenUse] Gain 2 [ProtectStanceRyoshu]\n[WhenUse] If target has 3+ types of negative effects, Final Power +1\n[WhenUse] At 6+ ([Breath] on self + [Burst] on target), Coin Power +1\n[WhenUse] Gain +3 [Breath] Count\n[WhenUse] Gain 3 [Breath]
   PL: [WhenUse] Zyskuje 2 [ProtectStanceRyoshu]\n[WhenUse] Jeżeli cel ma 3+ rodzajów negatywnych efektów, Moc Końcowa +1\n[WhenUse] Przy 6+ (suma własnej Mocy [Breath] i Mocy [Burst] celu) Moc Monet +1\n[WhenUse] Zwiększa własny Licznik [Breath] o 3\n[WhenUse] Zyskuje 3 [Breath]
533. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Burst]
534. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] [Burst] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnStartCoin] (자신의 [Breath] 위력 + 대상의 [Burst] 위력) 1당 크리티컬 피해량 +2% (최대 100%)
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=3].coinlist[#3].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnStartCoin], [Breath], [Burst]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: [OnStartCoin] Deal +2% damage on Critical Hit for every ([Breath] on self + [Burst] on target) (max 100%)
   PL: [OnStartCoin] Zadaje +2% obrażeń przy trafieniu krytycznym za każde 1 (suma własnej Mocy [Breath] i Mocy [Burst] celu) (maks. 100%)
539. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=3].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 518 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] [ProtectStanceRyoshu] 2 얻음\n[WhenUse] 대상의 부정적인 효과가 3개 이상이면, 최종 위력 +1\n<style="highlight">[WhenUse] 자신의 [Breath] 위력과 대상의 [Burst] 위력 합 6당, 코인 위력 +1 (최대 2)</style>\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n[WhenUse] [Breath] 3 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=4].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [ProtectStanceRyoshu], [Breath], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ProtectStanceRyoshu] = 호위태세 / Protector's Stance; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: [WhenUse] Gain 2 [ProtectStanceRyoshu]\n[WhenUse] If target has 3+ types of negative effects, Final Power +1\n<style="highlight">[WhenUse] Coin Power +1 for every 6 ([Breath] on self + [Burst] on target) (max 2)</style>\n[WhenUse] Gain +3 [Breath] Count\n[WhenUse] Gain 3 [Breath]
   PL: [WhenUse] Zyskuje 2 [ProtectStanceRyoshu]\n[WhenUse] Jeżeli cel ma 3+ rodzajów negatywnych efektów, Moc Końcowa +1\n<style="highlight">[WhenUse] Moc Monet +1 za każde 6 (suma własnej Mocy [Breath] i Mocy [Burst] celu) (maks. 2)</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 3\n[WhenUse] Zyskuje 3 [Breath]
541. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 526 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 372 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 372 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] [Burst] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnStartCoin] (자신의 [Breath] 위력 + 대상의 [Burst] 위력) 1당 크리티컬 피해량 +2% <style="highlight">(최대 120%)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=4].coinlist[#3].coindescs[#0].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnStartCoin], [Breath], [Burst]
   znaczenie tagów: [OnStartCoin] = [코인 시작 시] / [Coin Start]; [Breath] = 호흡 / Poise; [Burst] = 파열 / Rupture
   EN: [OnStartCoin] Deal +2% damage on Critical Hit for every ([Breath] on self + [Burst] on target) <style="highlight">(max 120%)</style>
   PL: [OnStartCoin] Zadaje +2% obrażeń przy trafieniu krytycznym za każde 1 (suma własnej Mocy [Breath] i Mocy [Burst] celu) <style="highlight">(maks. 120%)</style>
547. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041303].levelList[level=4].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Obrona (ulepszenia 1,4) — nazwa] 호위
   źródło: Skills_personality-04.json :: dataList[id=1041304].levelList[level=1].name ; dataList[id=1041304].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: blok · moc bazowa: 3 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Sentinel
   PL: Straż Władcy
549. [Obrona (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] [ProtectStanceRyoshu] 2 얻음\n[WhenUse] 자신이 이번 전투에서 잃은 체력 누적 10%당, 이 스킬의 방어 레벨 +1 (최대 6. 발동 시점 최대 체력 기준)\n[WinDuel] 대상의 [Burst]만큼 [Breath] 얻음 (최대 5, 턴당 1회)
   źródło: Skills_personality-04.json :: dataList[id=1041304].levelList[level=1].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [ProtectStanceRyoshu], [WhenUse], [WinDuel], [Burst], [Breath]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [ProtectStanceRyoshu] = 호위태세 / Protector's Stance; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [CanDuelGuard]\n[StartBattle] Gain 2 [ProtectStanceRyoshu]\n[WhenUse] This Skill gains +1 Defense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)\n[WinDuel] Gain [Breath] by [Burst] on target (max 5; once per turn)
   PL: [CanDuelGuard]\n[StartBattle] Zyskuje 2 [ProtectStanceRyoshu]\n[WhenUse] Moc Obrony tej Umiejętności +1 za każde 10% łącznie straconego HP w tym spotkaniu (maks. 6; na podstawie Maks. HP w momencie aktywacji)\n[WinDuel] Zyskuje [Breath] równy [Burst] celu (maks. 5, 1 raz na turę)
550. [Obrona (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-04.json :: dataList[id=1041304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Obrona (ulepszenie 4) — opis] [CanDuelGuard]\n[StartBattle] [ProtectStanceRyoshu] 2 얻음\n[WhenUse] 자신이 이번 전투에서 잃은 체력 누적 10%당, 이 스킬의 방어 레벨 +1 (최대 6. 발동 시점 최대 체력 기준)\n[WinDuel] 대상의 [Burst]만큼 [Breath] 얻음 (최대 5, 턴당 1회)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041304].levelList[level=4].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [CanDuelGuard], [StartBattle], [ProtectStanceRyoshu], [WhenUse], [WinDuel], [Burst], [Breath]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [ProtectStanceRyoshu] = 호위태세 / Protector's Stance; [WhenUse] = [사용시] / [On Use]; [WinDuel] = [합 승리시] / [Clash Win]; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [CanDuelGuard]\n[StartBattle] Gain 2 [ProtectStanceRyoshu]\n[WhenUse] This Skill gains +1 Defense Level for every 10% HP this unit has cumulatively lost in this Encounter (max 6; based on max HP at the time of activation)\n[WinDuel] Gain [Breath] by [Burst] on target (max 5; once per turn)<style="highlight"></style>
   PL: [CanDuelGuard]\n[StartBattle] Zyskuje 2 [ProtectStanceRyoshu]\n[WhenUse] Moc Obrony tej Umiejętności +1 za każde 10% łącznie straconego HP w tym spotkaniu (maks. 6; na podstawie Maks. HP w momencie aktywacji)\n[WinDuel] Zyskuje [Breath] równy [Burst] celu (maks. 5, 1 raz na turę)<style="highlight"></style>
552. [Obrona (ulepszenie 4) — moneta 1, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041304].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]<style="highlight"></style>
   PL: [SuperCoin]<style="highlight"></style>
553. [Pasywka bojowa (od ulepszenia 1) — nazwa] 군.가.곁.좋\n(군주라… 그런 가능성에서 곁을 지켰다면 더할 나위 없이 좋았겠군.)
   źródło: Passives.json :: dataList[id=1041302].name
   limit: do 90 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I.L.T.L.T.\n(I would've Liked to walk The Lord's path Together)
   PL: I. L. T. L. T.\n(Najchętniej Kroczyłbym Drogą\nWładcy Ramię w Ramię.)
554. [Pasywka bojowa (od ulepszenia 1) — opis] 자신을 제외한 아군의 스킬이 적에게 적중하면, 해당 공격 종료시 ‘어이, 물러서라’로 일방 공격 (턴 당 1회)\n\n대기해제 또는 복귀로 등장한 턴에 [ProtectStanceRyoshu] 2 얻음\n홍원 군주 홍루의 ‘흑수군주’ 패시브 효과로 일방공격 명령 받을 때 흑수 또는 가씨 가문 소속으로 간주함
   źródło: Passives.json :: dataList[id=1041302].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n, [ProtectStanceRyoshu]
   znaczenie tagów: [ProtectStanceRyoshu] = 호위태세 / Protector's Stance
   EN: When another ally's Skill hits an enemy: After that Attack, use "Hey, Back Off" as an Unopposed Attack against the enemy (once per turn)\n\nIn the same turn this unit Substituted in or Returned to the battlefield, gain 2 [ProtectStanceRyoshu]\nWhen this unit activates an Unopposed Attack due to The Lord of Hongyuan Hong Lu's "The Heishou Lord" Passive, treat this unit as if it has "Heishou Pack" or "Jia Family" Trait Keywords
   PL: Gdy Umiejętność innego sojusznika trafi wroga, na koniec tego ataku używa „Hej, Odstąp” jako ataku nieopartego (1 raz na turę)\n\nW turze, w której ta jednostka weszła na pole przez Wejście z rezerwy lub Powrót, zyskuje 2 [ProtectStanceRyoshu]\nGdy otrzymuje rozkaz ataku nieopartego od pasywki „Heishou Lord” Władcy Hongyuan Hong Lu, liczy się jako frakcja Watahy Heishou lub Rodu Jia
555. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 아군이 공격한 적에게 스킬 1로 일방공격
   źródło: Passives.json :: dataList[id=1041302].summary
   limit: do 120 znaków
   EN: Use Skill 1 as an Unopposed Attack against the enemy an ally attacked
   PL: Używa Umiejętności 1 jako ataku nieopartego na wrogu zaatakowanym przez sojusznika
556. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — nazwa] 협객
   źródło: Passives.json :: dataList[id=1041301].name
   limit: do 40 znaków
   EN: Loyal Warrior
   PL: Wierny Wojownik
557. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — opis] 적이 아군을 공격하여 해당 아군이 사망했거나 체력이 25% 미만이면, 해당 공격 종료시 홍원 방랑무사 료슈가 ‘가척아원’으로 해당 적 일방 공격 (전투 당 1회)\n- 홍원 군주 홍루는 횟수 제한을 초과하여 이 효과 1회 추가 발동 가능\n\n‘군.가.곁.좋’ 패시브 효과로 ‘어이, 물러서라’ 발동 시, 해당 스킬 크리티컬 피해량 +30%. 자신을 제외한 정신력이 가장 낮은 아군 1명의 정신력 2 ~ 4 회복 (턴 당 1회. 정신력이 -40 이하인 아군 제외)
   źródło: Passives.json :: dataList[id=1041301].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If an ally is killed by enemy attack, or if the attacked ally's HP is at less than 25% after the attack: After that Attack, Drifting Blade of Hongyuan Ryōshū uses "Aiding Strike" as an Unopposed Attack against that enemy (once per Encounter)\n- The Lord of Hongyuan Hong Lu may activate this effect 1 more time past its usage limit\n\nIf "Hey, Back Off" is activated via the Passive 'I.L.T.L.T', the Skill deals +30% damage on Critical Hit and heals 2~4 SP for 1 other ally with the lowest SP (once per turn; excluding allies at -40 or lower SP)
   PL: Jeżeli sojusznik ginie od ataku wroga lub jego HP po ataku spada poniżej 25%, na koniec tego ataku Wędrowne Ostrze Hongyuan Ryōshū używa „Cios Wsparcia” jako ataku nieopartego na tym wrogu (1 raz na spotkanie)\n- Władca Hongyuan Hong Lu może dodatkowo uruchomić ten efekt 1 raz ponad limit\n\nGdy „Hej, Odstąp” uruchamia się dzięki pasywce „I. L. T. L. T.”, ta Umiejętność zadaje +30% obrażeń przy trafieniu krytycznym i odzyskuje 2–4 Poczytalności 1 innemu Sojusznikowi z najniższą Poczytalnością (1 raz na turę; wyłączając sojuszników z Poczytalnością -40 lub niższą)
558. [Pasywka bojowa (od ulepszenia 2, posiadane 3× Pride) — podsumowanie] 아군이 치명적인 피해를 받으면, 공격자에게 스킬 3 사용. 상시 패시브 효과로 발동하는 스킬 1 강화
   źródło: Passives.json :: dataList[id=1041301].summary
   limit: do 160 znaków
   EN: When an ally is hit by a fatal attack, use Skill 3 against the Attacker. Enhance Skill 1 used by the always-active Passive
   PL: Gdy sojusznik otrzyma śmiertelne obrażenia, używa Umiejętności 3 na atakującym. Wzmacnia Umiejętność 1 uruchamianą pasywką Zawsze aktywne
559. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Glut., posiadane 3× Pride) — nazwa] 방랑
   źródło: Passives.json :: dataList[id=1041321].name
   limit: do 40 znaków
   EN: Drifter
   PL: Wędrowiec
560. [Pasywka wsparcia (od ulepszenia 3, posiadane 3× Glut., posiadane 3× Pride) — opis] 전투 시작시 편성 순서가 가장 빠른 아군 1명이 자신의 [Breath] 위력 1당 보호막 1 얻음 (최대 10)
   źródło: Passives.json :: dataList[id=1041321].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Combat Start: The ally with the earliest Deployment order gains 1 Shield for every [Breath] on self (max 10)
   PL: Na początku walki 1 Sojusznik przydzielony najwcześniej zyskuje 1 Tarczy za każde 1 własnej Mocy [Breath] (maks. 10)

## [000] Lobotomy E.G.O:: Faint Aroma & Solitude — Ryōshū — 로보토미 E.G.O:: 잔향・외로움
- ID Tożsamości: `10414` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: wydarzenie 9108 · HP bazowe: 75 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×1 (Normal), Penetrate ×0,5 (Endured), Hit ×2 (Fatal) · słowa kluczowe: Sinking, Tremor

561. [Karta Tożsamości — tytuł] 로보토미 E.G.O::\n잔향・외로움
   źródło: Personalities.json :: dataList[id=10414].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy E.G.O::\nFaint Aroma & Solitude
   PL: Lobotomy E.G.O::\nNikła Woń i\nSamotność
562. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10414].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10414].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Karta Tożsamości — opis] 료슈의 열네번째 인격
   źródło: Personalities.json :: dataList[id=10414].desc
   limit: do 120 znaków
   EN: Ryōshū's 14th Identity
   PL: Czternasta Tożsamość Ryōshū
565. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 탕. 탕.
   źródło: Skills_personality-04.json :: dataList[id=1041401].levelList[level=1].name ; dataList[id=1041401].levelList[level=2].name ; dataList[id=1041401].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 4 · monety: 2 (+4)
   limit: do 40 znaków
   EN: Bang. Bang.
   PL: Kabum. Kabum.
566. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [BulletGodok] 1 소모
   źródło: Skills_personality-04.json :: dataList[id=1041401].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1041401].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1041401].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletGodok]
   znaczenie tagów: [BulletGodok] = 탄환 - 고독 / Bullet - Solitude
   EN: Spend 1 [BulletGodok]
   PL: Zużywa 1 [BulletGodok]
567. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041401].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1041401].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1041401].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Sinking]
568. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — moneta 2, efekt 1 — opis] [BulletGodok] 1 소모
   źródło: Skills_personality-04.json :: dataList[id=1041401].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=1041401].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041401].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 566 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Umiejętność 1 (×3) (ulepszenia 1–2) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041401].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=1041401].levelList[level=2].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [WhenUse] 대상의 [Vibration]과 [Sinking]의 합이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041401].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] If target has 6+ ([Vibration] + [Sinking]), Coin Power +1
   PL: [WhenUse] Jeżeli cel ma 6+ (suma [Vibration] i [Sinking]), Moc Monet +1
571. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 대상의 [Vibration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)
   źródło: Skills_personality-04.json :: dataList[id=1041401].levelList[level=4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking
   EN: [WhenUse] Coin Power +1 for every 6 ([Vibration] + [Sinking]) on target (max 2)
   PL: [WhenUse] Moc Monet +1 za każde 6 (suma [Vibration] i [Sinking] celu) (maks. 2)
572. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_personality-04.json :: dataList[id=1041401].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] Nakłada 3 [Vibration]
573. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 공허에 피어나는 향기
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=1].name ; dataList[id=1041402].levelList[level=2].name ; dataList[id=1041402].levelList[level=4].name
   kontekst: grzech: Envy · typ: Penetrate · moc bazowa: 4 · monety: 3 (+4)
   limit: do 50 znaków
   EN: Blossoming Fragrance in the Void
   PL: Rozkwitający Subtelny Aromat w Pustce
574. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — moneta 1, efekt 1 — opis] [BulletGodok] 1 소모
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=1041402].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1041402].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 566 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Umiejętność 2 (×2) (ulepszenia 1–2) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=1041402].levelList[level=2].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [AlriuneEGOThey] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AlriuneEGOThey]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AlriuneEGOThey] = 잔향 / Faint Aroma
   EN: [OnSucceedAttack] Inflict 2 [AlriuneEGOThey]
   PL: [OnSucceedAttack] Nakłada 2 [AlriuneEGOThey]
577. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [AlriuneEGOThey] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 576 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse] 대상의 [Vibration]과 [Sinking]의 합이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=2].desc
   (powtórzenie elementu 570 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [AlriuneEGOThey] 3 부여
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041402].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AlriuneEGOThey]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AlriuneEGOThey] = 잔향 / Faint Aroma
   EN: [OnSucceedAttack] Inflict 3 [AlriuneEGOThey]
   PL: [OnSucceedAttack] Nakłada 3 [AlriuneEGOThey]
582. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1041402].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada +2 Licznika [Vibration]
583. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [AlriuneEGOThey] 3 부여
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1041402].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 581 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1041402].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 대상의 [Vibration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [AlriuneEGOThey] 1당, 피해량 +1%
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=4].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [Sinking], [AlriuneEGOThey]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking; [AlriuneEGOThey] = 잔향 / Faint Aroma
   EN: [WhenUse] Coin Power +1 for every 6 ([Vibration] + [Sinking]) on target (max 2)\n[WhenUse] Deal +1% damage for every [AlriuneEGOThey] on target
   PL: [WhenUse] Moc Monet +1 za każde 6 (suma [Vibration] i [Sinking] celu) (maks. 2)\n[WhenUse] Zadaje +1% obrażeń za każde 1 [AlriuneEGOThey] na celu
586. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-04.json :: dataList[id=1041402].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] Nakłada +3 Licznika [Sinking]
587. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 만개
   źródło: Skills_personality-04.json :: dataList[id=1041403].levelList[level=3].name ; dataList[id=1041403].levelList[level=4].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Full Bloom
   PL: Pełen Rozkwit
588. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 대상의 [Vibration]과 [Sinking]의 합이 6 이상이면, 코인 위력 +1
   źródło: Skills_personality-04.json :: dataList[id=1041403].levelList[level=3].desc
   (powtórzenie elementu 570 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [AlriuneEGOThey] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041403].levelList[level=3].coinlist[#0].coindescs[#0].desc ; dataList[id=1041403].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AlriuneEGOThey]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AlriuneEGOThey] = 잔향 / Faint Aroma
   EN: [OnSucceedAttack] Inflict 1 [AlriuneEGOThey]
   PL: [OnSucceedAttack] Nakłada 1 [AlriuneEGOThey]
590. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_personality-04.json :: dataList[id=1041403].levelList[level=3].coinlist[#0].coindescs[#1].desc ; dataList[id=1041403].levelList[level=4].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [AlriuneEGOThey] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041403].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1041403].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 589 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_personality-04.json :: dataList[id=1041403].levelList[level=3].coinlist[#1].coindescs[#1].desc ; dataList[id=1041403].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL: [OnSucceedAttack] Nakłada 4 [Sinking]
593. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [AlriuneEGOThey] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041403].levelList[level=3].coinlist[#2].coindescs[#0].desc ; dataList[id=1041403].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 576 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041403].levelList[level=3].coinlist[#2].coindescs[#1].desc ; dataList[id=1041403].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Umiejętność 3 (×1) (ulepszenia 3–4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041403].levelList[level=3].coinlist[#2].coindescs[#2].desc ; dataList[id=1041403].levelList[level=4].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 대상의 [Vibration]과 [Sinking]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [AlriuneEGOThey] 1당, 피해량 +1%
   źródło: Skills_personality-04.json :: dataList[id=1041403].levelList[level=4].desc
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 우울 피해
   źródło: Skills_personality-04.json :: dataList[id=1041403].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Deal Gloom damage equal to [Sinking] on target
   PL: [OnSucceedAttack] Zadaje obrażenia Posępności równe [Sinking] celu
598. [Umiejętność 4 (×0) (ulepszenie 1) — nazwa] 멈추지 않는 이야기
   źródło: Skills_personality-04.json :: dataList[id=1041405].levelList[level=1].name
   kontekst: grzech: Sloth · typ: Penetrate · moc bazowa: 9 · monety: 3 (+1)
   limit: do 40 znaków
   EN: Stories that Never Cease
   PL: Historie, Które Nie Ustają
599. [Umiejętność 4 (×0) (ulepszenie 1) — opis] [CantDuel]\n[WideAreaRampage]\n이 스킬에서 [GodokPanicType]을 부여할 때, 대상이 이번 턴 또는 다음 턴에 부여될 [GodokPanicType]이 있으면 대신 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041405].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WideAreaRampage], [GodokPanicType], [VibrationExplosion], [Vibration]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WideAreaRampage] = 광역 난사 / Unfocused Volley; [GodokPanicType] = 고독 / Solitude; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [CantDuel]\n[WideAreaRampage]\nWhen this Skill inflicts [GodokPanicType], if the target already has [GodokPanicType] this turn, or will be inflicted with [GodokPanicType] next turn, trigger [VibrationExplosion] instead; then, reduce target's [Vibration] Count by 1
   PL: [CantDuel]\n[WideAreaRampage]\nGdy ta Umiejętność nakłada [GodokPanicType], jeżeli cel ma już [GodokPanicType] w tej lub następnej turze, wywołuje zamiast tego [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
600. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count
   PL: [OnSucceedAttack] Zwiększa Licznik [Sinking] celu o 1
601. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [GodokPanicType] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041405].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [GodokPanicType]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GodokPanicType] = 고독 / Solitude
   EN: [OnSucceedAttack] Inflict 2 [GodokPanicType] next turn
   PL: [OnSucceedAttack] Nakłada w następnej turze 2 [GodokPanicType]
602. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041405].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [GodokPanicType] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041405].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 601 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041405].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [GodokPanicType] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041405].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 601 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Umiejętność 5 (×0) (ulepszenie 3) — nazwa] 황홀한 종말
   źródło: Skills_personality-04.json :: dataList[id=1041406].levelList[level=3].name
   kontekst: grzech: Gloom · typ: Penetrate · moc bazowa: 12 · monety: 1 (+7)
   limit: do 40 znaków
   EN: Magnificent End
   PL: Wspaniałomyślny Koniec
607. [Umiejętność 5 (×0) (ulepszenie 3) — opis] [CantDuel]\n이 스킬은 외부 효과로 재사용할 수 없음\n이 스킬 공격 가중치보다 낮은 공격 대상 1당, 피해량 +30% (집중 전투인 경우, 부위로 판정)\n[WhenUse] 모든 대상의 [AlriuneEGOThey] 합 5당 최종 위력 +1 (최대 6)\n\n[EndSkill] 자신의 [AlriuneEGOWe] 소멸
   źródło: Skills_personality-04.json :: dataList[id=1041406].levelList[level=3].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [AlriuneEGOThey], [EndSkill], [AlriuneEGOWe]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [AlriuneEGOThey] = 잔향 / Faint Aroma; [EndSkill] = [공격 종료시] / [Attack End]; [AlriuneEGOWe] = 꽃잎 / Petals
   EN: [CantDuel]\nExternal effects cannot trigger this Skill to be Reused\nDeal +30% damage for every excess Atk Weight beyond the number of actual targets (in Focused Encounters, the Part)\n[WhenUse] Final Power +1 for every 5 (sum of [AlriuneEGOThey] on all targets) (max 6)\n\n[EndSkill] Lose all [AlriuneEGOWe] on self
   PL: [CantDuel]\nZewnętrzne efekty nie mogą ponownie uruchomić tej Umiejętności\nZadaje +30% obrażeń za każdego 1 nadmiarowego celu ataku ponad wagę ataku tej Umiejętności (w walce skupionej: części ciała)\n[WhenUse] Moc Końcowa +1 za każde 5 (sumy [AlriuneEGOThey] na wszystkich celach) (maks. 6)\n\n[EndSkill] Traci całe [AlriuneEGOWe]
608. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [AlriuneEGOThey] 5 부여
   źródło: Skills_personality-04.json :: dataList[id=1041406].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AlriuneEGOThey]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AlriuneEGOThey] = 잔향 / Faint Aroma
   EN: [OnSucceedAttack] Inflict 5 [AlriuneEGOThey]
   PL: [OnSucceedAttack] Nakłada 5 [AlriuneEGOThey]
609. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_personality-04.json :: dataList[id=1041406].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL: [OnSucceedAttack] Nakłada 3 [Sinking]
610. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_personality-04.json :: dataList[id=1041406].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 572 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041406].levelList[level=3].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Umiejętność 5 (×0) (ulepszenie 3) — moneta 1, efekt 5 — opis] [OnSucceedAttack] 대상의 [Sinking]만큼 우울 피해
   źródło: Skills_personality-04.json :: dataList[id=1041406].levelList[level=3].coinlist[#0].coindescs[#4].desc
   (powtórzenie elementu 597 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Obrona (ulepszenia 1,4) — nazwa] 예.감.시.
   źródło: Skills_personality-04.json :: dataList[id=1041404].levelList[level=1].name ; dataList[id=1041404].levelList[level=4].name
   kontekst: grzech: Gloom · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: A.A.T.
   PL: A. A. T.
614. [Obrona (ulepszenia 1,4) — opis] [EndBattle] [AlriuneEGOWe] 10 얻음 (턴당 1회)\n[EndBattle] 다음 턴에 [Vulnerable] 2, [Enhancement] 2 얻음 (턴당 1회)
   źródło: Skills_personality-04.json :: dataList[id=1041404].levelList[level=1].desc ; dataList[id=1041404].levelList[level=4].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [EndBattle], [AlriuneEGOWe], [Vulnerable], [Enhancement]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]; [AlriuneEGOWe] = 꽃잎 / Petals; [Vulnerable] = 취약 / Fragile; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EndBattle] Gain 10 [AlriuneEGOWe] (once per turn)\n[EndBattle] Gain 2 [Vulnerable] and 2 [Enhancement] next turn (once per turn)
   PL: [EndBattle] Zyskuje 10 [AlriuneEGOWe] (1 raz na turę)\n[EndBattle] Zyskuje w następnej turze 2 [Vulnerable] i 2 [Enhancement] (1 raz na turę)
615. [Pasywka bojowa (od ulepszenia 1) — nazwa] 채워지지 않는 공허
   źródło: Passives.json :: dataList[id=1041402].name
   limit: do 40 znaków
   EN: A Void that Cannot be Filled
   PL: Pustka, Której Nie da się Wypełnić
616. [Pasywka bojowa (od ulepszenia 1) — opis] 상시 적용 : [BulletGodok] 6개 보유\n\n[BulletGodok]이 1 이상일 때, 자신 또는 아군의 공격 종료시 적의 정신력이\n-40미만이거나 흐트러짐 상태면 '탕. 탕.'으로 일방공격 (턴당 1회)\n\n자신의 공격 종료시 [BulletGodok]이 0이면, 대상을 '멈추지 않는 이야기'로 일방공격하고 정신력을 10 소모하여 [FullReload]
   źródło: Passives.json :: dataList[id=1041402].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [BulletGodok], [FullReload]
   znaczenie tagów: [BulletGodok] = 탄환 - 고독 / Bullet - Solitude; [FullReload] = 재장전 / Reload
   EN: Always Active: Begin Encounters with 6 [BulletGodok]\n\nAt 1+ [BulletGodok], if the enemy has less than -40 SP or is Staggered at this unit or an ally's Attack End, use 'Bang. Bang.' as an Unopposed Attack (once per turn)\n\nAttack End: At 0 [BulletGodok], use 'Stories that Never Cease' as an Unopposed Attack against the target and consume 10 SP to [FullReload]
   PL: Zawsze aktywne: rozpoczyna spotkania z 6 [BulletGodok]\n\nPrzy 1+ [BulletGodok], jeżeli na koniec ataku tej jednostki lub sojusznika wróg ma Poczytalność poniżej -40 albo jest Ogłuszony, używa „Kabum. Kabum.” jako ataku nieopartego (1 raz na turę)\n\nNa koniec ataku przy 0 [BulletGodok] używa „Historie, Które Nie Ustają” jako ataku nieopartego na celu i zużywa 10 Poczytalności, aby [FullReload]
617. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] '1-1스킬' 발동 및 [FullReload]
   źródło: Passives.json :: dataList[id=1041402].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [FullReload]
   znaczenie tagów: [FullReload] = 재장전 / Reload
   EN: Trigger 'Skill 1-1' and [FullReload]
   PL: Uruchamia „Umiejętność 1-1” i [FullReload]
618. [Pasywka bojowa (od ulepszenia 1, posiadane 1× Sloth, posiadane 2× Gloom) — nazwa] 시들지 않는 꽃
   źródło: Passives.json :: dataList[id=1041401].name
   limit: do 40 znaków
   EN: Unwithering Flower
   PL: Nieześwieżający Kwiat
619. [Pasywka bojowa (od ulepszenia 1, posiadane 1× Sloth, posiadane 2× Gloom) — opis] 적이 [Sinking] 피해를 받으면 [AlriuneEGOWe] 1 얻음\n적에게 부여된 [AlriuneEGOThey]만큼 [AlriuneEGOWe] 얻음\n[VibrationExplosion] 발생 시, [AlriuneEGOWe] 2 얻음
   źródło: Passives.json :: dataList[id=1041401].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [AlriuneEGOWe], [AlriuneEGOThey], [VibrationExplosion]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [AlriuneEGOWe] = 꽃잎 / Petals; [AlriuneEGOThey] = 잔향 / Faint Aroma; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: Gain 1 [AlriuneEGOWe] if the enemy takes [Sinking] damage\nGain [AlriuneEGOWe] equal to [AlriuneEGOThey] inflicted every time enemies gain [AlriuneEGOThey]\nGain 2 [AlriuneEGOWe] every time Tremor Burst is triggered regardless of the unit
   PL: Gdy wróg otrzymuje obrażenia [Sinking], zyskuje 1 [AlriuneEGOWe]\nZyskuje [AlriuneEGOWe] równy nakładanym [AlriuneEGOThey] za każdym razem, gdy wrogowie zyskują [AlriuneEGOThey]\nGdy wywołany zostaje [VibrationExplosion], zyskuje 2 [AlriuneEGOWe]
620. [Pasywka bojowa (od ulepszenia 1, posiadane 1× Sloth, posiadane 2× Gloom) — podsumowanie] [AlriuneEGOWe] 얻음
   źródło: Passives.json :: dataList[id=1041401].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AlriuneEGOWe]
   znaczenie tagów: [AlriuneEGOWe] = 꽃잎 / Petals
   EN: Gain [AlriuneEGOWe]
   PL: Zyskuje [AlriuneEGOWe]
621. [Pasywka bojowa (od ulepszenia 3, posiadane 1× Sloth, posiadane 2× Gloom) — nazwa] 시들지 않는 꽃
   źródło: Passives.json :: dataList[id=1041411].name
   (powtórzenie elementu 618 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Pasywka bojowa (od ulepszenia 3, posiadane 1× Sloth, posiadane 2× Gloom) — opis] 적이 [Sinking] 피해를 받으면 [AlriuneEGOWe] 1 얻음\n적에게 부여되는 [AlriuneEGOThey]만큼 [AlriuneEGOWe] 얻음\n[VibrationExplosion] 발생 시, [AlriuneEGOWe] 2 얻음\n\n자신의 공격 스킬 종료시, 자신의 [AlriuneEGOWe]이 30 이상이면, [AlriuneEGOThey]이 가장 높은 대상에게 '황홀한 종말' 발동\n\n흐트러진 대상에게 가하는 피해량 +(대상의 [AlriuneEGOThey])%\n\n이번 턴에 자신의 체력을 최대 체력의 10% 이상 잃으면, 최대 체력의 3%, 정신력 10 회복 (턴당 1회)
   źródło: Passives.json :: dataList[id=1041411].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [AlriuneEGOWe], [AlriuneEGOThey], [VibrationExplosion]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [AlriuneEGOWe] = 꽃잎 / Petals; [AlriuneEGOThey] = 잔향 / Faint Aroma; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: Gain 1 [AlriuneEGOWe] if the enemy takes [Sinking] damage\nGain [AlriuneEGOWe] equal to [AlriuneEGOThey] inflicted every time enemies gain [AlriuneEGOThey]\nGain 2 [AlriuneEGOWe] every time Tremor Burst is triggered regardless of the unit\n\nAttack Skill End: At 30+ [AlriuneEGOWe], use 'Magnificent End' against the target that has the highest [AlriuneEGOThey] Stack\n\nDeal +([AlriuneEGOThey] on the target)% damage against Staggered targets\n\nIf this unit lost 10%+ HP this turn, heal 3% HP and 10 SP (once per turn)
   PL: Gdy wróg otrzymuje obrażenia [Sinking], zyskuje 1 [AlriuneEGOWe]\nZyskuje [AlriuneEGOWe] równy nakładanym [AlriuneEGOThey] za każdym razem, gdy wrogowie zyskują [AlriuneEGOThey]\nGdy wywołany zostaje [VibrationExplosion], zyskuje 2 [AlriuneEGOWe]\n\nNa koniec Umiejętności ataku przy 30+ [AlriuneEGOWe] uruchamia „Wspaniałomyślny Koniec” na celu z najwyższym Stosem [AlriuneEGOThey]\n\nZadaje +([AlriuneEGOThey] celu)% obrażeń Ogłuszonym celom\n\nJeżeli ta jednostka straciła w tej turze 10%+ HP, odzyskuje 3% HP i 10 Poczytalności (1 raz na turę)
623. [Pasywka bojowa (od ulepszenia 3, posiadane 1× Sloth, posiadane 2× Gloom) — podsumowanie] [AlriuneEGOWe] 얻음
   źródło: Passives.json :: dataList[id=1041411].summary
   (powtórzenie elementu 620 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — nazwa] 봄의 탄생
   źródło: Passives.json :: dataList[id=1041421].name
   limit: do 40 znaków
   EN: Spring's Genesis
   PL: Narodziny Wiosny
625. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — opis] 속도가 가장 빠른 아군 1명이 [Sinking] 위력, 횟수 또는 특수 침잠[TabExplain]을 부여하는 스킬로 적에게 적중 시 [Vibration]을 2 부여하고, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소 (턴당 1회)
   źródło: Passives.json :: dataList[id=1041421].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: [Sinking], [TabExplain], [Vibration], [VibrationExplosion]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: When the ally with the fastest Speed hits an enemy using a Skill that inflicts [Sinking] Potency, Count, or 'Unique Sinking', inflict 2 [Vibration] and trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1 (once per turn)
   PL: Gdy 1 Sojusznik z najwyższą Szybkością trafia wroga Umiejętnością nakładającą Moc, Licznik [Sinking] lub „Specjalne Zatopienie”[TabExplain], nakłada 2 [Vibration] i wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1 (1 raz na turę)
626. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Sloth) — podsumowanie] [Vibration] 부여, [VibrationExplosion]
   źródło: Passives.json :: dataList[id=1041421].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration], [VibrationExplosion]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: Inflict [Vibration], trigger [VibrationExplosion]
   PL: Nakłada [Vibration], wywołuje [VibrationExplosion]

## [000] Blade of the House of Spiders — Ryōshū — 거미집의 검
- ID Tożsamości: `10415` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 7 · HP bazowe: 66 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×2 (Fatal), Hit ×1 (Normal) · słowa kluczowe: Burn, Bleed, Poise

627. [Karta Tożsamości — tytuł] 거미집의 검
   źródło: Personalities.json :: dataList[id=10415].title
   limit: do 50 znaków
   EN: Blade of the House of Spiders
   PL: Ostrze Domu Pajęczyn
628. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10415].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10415].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Karta Tożsamości — opis] 료슈의 열다섯번째 인격
   źródło: Personalities.json :: dataList[id=10415].desc
   limit: do 120 znaków
   EN: Ryōshū's 15th Identity
   PL: Piętnasta Tożsamość Ryōshū
631. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 삼연[三連]
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=1].name ; dataList[id=1041501].levelList[level=2].name ; dataList[id=1041501].levelList[level=4].name
   kontekst: grzech: Lust · typ: Slash · moc bazowa: 3 · monety: 3 (+3)
   limit: do 40 znaków
   EN: Tripleslash [三連]
   PL: Potrójne Cięcie [三連]
632. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [WhenUse] [Breath] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] Zwiększa własny Licznik [Breath] o 2
633. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]
   PL: [OnSucceedAttack] Zyskuje 1 [Breath]
634. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [CriticalOnSucceedAttack] Zwiększa Licznik [Laceration] celu o 2
635. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Combustion] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Combustion]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Combustion] = 화상 / Burn
   EN: [CriticalOnSucceedAttack] Inflict +1 [Combustion] Count
   PL: [CriticalOnSucceedAttack] Zwiększa Licznik [Combustion] celu o 1
637. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [PhantomIncisionID] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PhantomIncisionID]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PhantomIncisionID] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [OnSucceedAttack] Inflict 2 [PhantomIncisionID]
   PL: [OnSucceedAttack] Nakłada 2 [PhantomIncisionID]
639. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 [SojiRyoshuEchoPast]만큼 [PhantomIncisionID] 부여 (최대 4)
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SojiRyoshuEchoPast], [PhantomIncisionID]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SojiRyoshuEchoPast] = 얽힘 / Entanglement; [PhantomIncisionID] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [OnSucceedAttack] Inflict [PhantomIncisionID] equal to [SojiRyoshuEchoPast] on self (max 4)
   PL: [OnSucceedAttack] Nakłada [PhantomIncisionID] równy własnemu [SojiRyoshuEchoPast] (maks. 4)
640. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 4 — opis] [CriticalOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict 2 [Laceration]
   PL: [CriticalOnSucceedAttack] Nakłada 2 [Laceration]
641. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 3, efekt 5 — opis] [CriticalOnSucceedAttack] 이 코인 최종 피해량의 ([SojiRyoshuEchoPast] x 2)% 만큼 참격 피해
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=1].coinlist[#2].coindescs[#4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [SojiRyoshuEchoPast]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [SojiRyoshuEchoPast] = 얽힘 / Entanglement
   EN: [CriticalOnSucceedAttack] Deal Slash damage equal to ([SojiRyoshuEchoPast] x 2)% of this Coin's final damage
   PL: [CriticalOnSucceedAttack] Zadaje obrażenia Cięcia równe ([SojiRyoshuEchoPast] x 2)% końcowych obrażeń tej monety
642. [Umiejętność 1 (×3) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath]이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] [Breath] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: <style="highlight">[WhenUse] At 6+ [Breath], Coin Power +1</style>\n[WhenUse] Gain +<style="highlight">3</style> [Breath] Count
   PL: <style="highlight">[WhenUse] Przy 6+ [Breath] Moc Monet +1</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o <style="highlight">3</style>
643. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 1 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1041501].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 1 [Breath]<style="highlight"></style>
644. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 횟수 2 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1041501].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict +2 [Laceration] Count<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Zwiększa Licznik [Laceration] celu o 2<style="highlight"></style>
645. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041501].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]<style="highlight"></style>
   PL: [OnSucceedAttack] Zyskuje 2 [Breath]<style="highlight"></style>
646. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Combustion] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1041501].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Combustion]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Combustion] = 화상 / Burn
   EN: [CriticalOnSucceedAttack] Inflict +1 [Combustion] Count<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Zwiększa Licznik [Combustion] celu o 1<style="highlight"></style>
647. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1041501].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 645 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [PhantomIncisionID] 2 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1041501].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [PhantomIncisionID]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PhantomIncisionID] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [OnSucceedAttack] Inflict 2 [PhantomIncisionID]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [PhantomIncisionID]<style="highlight"></style>
649. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 [SojiRyoshuEchoPast]만큼 [PhantomIncisionID] 부여 (최대 4)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=2].coinlist[#2].coindescs[#2].desc ; dataList[id=1041501].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [SojiRyoshuEchoPast], [PhantomIncisionID]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SojiRyoshuEchoPast] = 얽힘 / Entanglement; [PhantomIncisionID] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [OnSucceedAttack] Inflict [PhantomIncisionID] equal to [SojiRyoshuEchoPast] on self (max 4)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada [PhantomIncisionID] równy własnemu [SojiRyoshuEchoPast] (maks. 4)<style="highlight"></style>
650. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 4 — opis] [CriticalOnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=2].coinlist[#2].coindescs[#3].desc ; dataList[id=1041501].levelList[level=4].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict 2 [Laceration]<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Nakłada 2 [Laceration]<style="highlight"></style>
651. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 3, efekt 5 — opis] [CriticalOnSucceedAttack] 이 코인 최종 피해량의 ([SojiRyoshuEchoPast] x 2)% 만큼 참격 피해<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=2].coinlist[#2].coindescs[#4].desc ; dataList[id=1041501].levelList[level=4].coinlist[#2].coindescs[#4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [SojiRyoshuEchoPast]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [SojiRyoshuEchoPast] = 얽힘 / Entanglement
   EN: [CriticalOnSucceedAttack] Deal Slash damage equal to ([SojiRyoshuEchoPast] x 2)% of this Coin's final damage<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Zadaje obrażenia Cięcia równe ([SojiRyoshuEchoPast] x 2)% końcowych obrażeń tej monety<style="highlight"></style>
652. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath]이 6 이상이면, 코인 위력 +1\n<style="highlight">[WhenUse] 대상의 [Combustion]과 [Laceration]의 합 6당 최종 위력 +1 (최대 2)</style>\n[WhenUse] [Breath] 횟수 3 증가
   źródło: Skills_personality-04.json :: dataList[id=1041501].levelList[level=4].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Combustion], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] At 6+ [Breath], Coin Power +1\n<style="highlight">[WhenUse] Final Power +1 for every 6 ([Combustion] + [Laceration]) on target (max 2)</style>\n[WhenUse] Gain +3 [Breath] Count
   PL: [WhenUse] Przy 6+ [Breath] Moc Monet +1\n<style="highlight">[WhenUse] Moc Końcowa +1 za każde 6 (suma [Combustion] i [Laceration] celu) (maks. 2)</style>\n[WhenUse] Zwiększa własny Licznik [Breath] o 3
653. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 삼연 - 잔[三連 - 殘]
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=1].name ; dataList[id=1041502].levelList[level=2].name ; dataList[id=1041502].levelList[level=4].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 4 · monety: 3 (+4)
   limit: do 50 znaków
   EN: Tripleslash - Echoshear [三連 - 殘]
   PL: Potrójne Cięcie - Echoshear [三連 - 殘]
654. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse] [Breath] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=1].desc
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict 1 [Laceration]
   PL: [CriticalOnSucceedAttack] Nakłada 1 [Laceration]
657. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 191 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 656 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 191 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 640 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] 이 코인 최종 피해량의 ([SojiRyoshuEchoPast] x 3)%만큼 참격 피해
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [SojiRyoshuEchoPast]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [SojiRyoshuEchoPast] = 얽힘 / Entanglement
   EN: [CriticalOnSucceedAttack] Deal Slash damage equal to ([SojiRyoshuEchoPast] x 3)% of this Coin's final damage
   PL: [CriticalOnSucceedAttack] Zadaje obrażenia Cięcia równe ([SojiRyoshuEchoPast] x 3)% końcowych obrażeń tej monety
662. [Umiejętność 2 (×2) (ulepszenie 2) — opis] <style="highlight">[WhenUse] 자신의 [Breath]이 6 이상이면, 코인 위력 +1</style>\n[WhenUse] [Breath] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=2].desc
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1041502].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 645 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=1041502].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Inflict 1 [Laceration]<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Nakłada 1 [Laceration]<style="highlight"></style>
665. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=1041502].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Combustion]<style="highlight"></style>
666. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 2, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 1 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=1041502].levelList[level=4].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 664 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=1041502].levelList[level=4].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 2 — opis] [CriticalOnSucceedAttack] [Laceration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=1041502].levelList[level=4].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 650 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Umiejętność 2 (×2) (ulepszenia 2,4) — moneta 3, efekt 3 — opis] [CriticalOnSucceedAttack] 이 코인 최종 피해량의 ([SojiRyoshuEchoPast] x 3)%만큼 참격 피해<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=2].coinlist[#2].coindescs[#2].desc ; dataList[id=1041502].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [SojiRyoshuEchoPast]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [SojiRyoshuEchoPast] = 얽힘 / Entanglement
   EN: [CriticalOnSucceedAttack] Deal Slash damage equal to ([SojiRyoshuEchoPast] x 3)% of this Coin's final damage<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Zadaje obrażenia Cięcia równe ([SojiRyoshuEchoPast] x 3)% końcowych obrażeń tej monety<style="highlight"></style>
670. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath]이 6 이상이면, 코인 위력 +1\n<style="highlight">[WhenUse] 대상의 [Combustion]과 [Laceration]의 합 6당 최종 위력 +1 (최대 2)</style>\n[WhenUse] [Breath] 횟수 3 증가
   źródło: Skills_personality-04.json :: dataList[id=1041502].levelList[level=4].desc
   (powtórzenie elementu 652 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 공간참[空間斬]
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=3].name ; dataList[id=1041503].levelList[level=4].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 10 · monety: 1 (+12)
   limit: do 40 znaków
   EN: Rend Space [空間斬]
   PL: Rozprucie Przestrzeni [空間斬]
672. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse] 자신의 [Breath] 4당 최종 위력 +1 (최대 5)\n[WhenUse] 자신의 [SojiRyoshuEchoPast] 1당 피해량 +5%\n[WhenUse] [Breath] 5 얻음\n[WhenUse] 자신의 [SojiRyoshuEchoPast] 2당 가중치 +1 (최대 2)\n[WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당 피해량 +15% (집중 전투의 경우, 부위로 판정)\n[EndSkill] 이 스킬의 적중 대상에게 [PhantomIncisionID]을 (자신의 [SojiRyoshuEchoPast] + 10)만큼 무작위로 나눠서 부여
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=3].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [SojiRyoshuEchoPast], [EndSkill], [PhantomIncisionID]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [SojiRyoshuEchoPast] = 얽힘 / Entanglement; [EndSkill] = [공격 종료시] / [Attack End]; [PhantomIncisionID] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [WhenUse] Final Power +1 for every 4 [Breath] on self (max 5)\n[WhenUse] Deal +5% damage for every [SojiRyoshuEchoPast] on self\n[WhenUse] Gain 5 [Breath]\n[WhenUse] Gain +1 Atk Weight for every 2 [SojiRyoshuEchoPast] on self (max 2)\n[WhenUse] Deal +15% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Parts)\n[EndSkill] Randomly inflict ([SojiRyoshuEchoPast] on self + 10) [PhantomIncisionID] between targets hit by this Skill
   PL: [WhenUse] Moc Końcowa +1 za każde 4 [Breath] (maks. 5)\n[WhenUse] Zadaje +5% obrażeń za każde 1 [SojiRyoshuEchoPast]\n[WhenUse] Zyskuje 5 [Breath]\n[WhenUse] Waga ataku +1 za każde 2 [SojiRyoshuEchoPast] (maks. 2)\n[WhenUse] Zadaje +15% obrażeń za każdego 1 nadmiarowego celu ataku ponad wagę ataku tej Umiejętności (w walce skupionej: części ciała)\n[EndSkill] Losowo rozdziela ([SojiRyoshuEchoPast] + 10) [PhantomIncisionID] między celami trafionymi tą Umiejętnością
673. [Umiejętność 3 (×1) (ulepszenia 3–4) — tekst klimatyczny] “검의 길? 뭐, 미련하게 가다 보면 공간 정돈 벨 수 있게 되지. 아. 물론 아지랑이처럼 잠깐 갈라져서 일렁거리는 게 다야. 시간 좀 지나면 원래대로 돌아오더라구.”
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=3].flavor ; dataList[id=1041503].levelList[level=4].flavor
   limit: do 420 znaków
   EN: "The Way of the Blade, huh? Yeah, sticking to a single path like a one-track-minded dumbass'll eventually get ya to cut stuff like space too. Oh, but don't flatter yourself—it just makes the split space shimmer for a bit like in the heat haze. Give it some time, and the cut closes like it was never even there in the first place."
   PL: „Szkoła Miecza? Cóż, tępo idąc jedną ścieżką, docelowo i przestrzeń się natnie. A, ale nie ma co się czepiać — rozcięcie błyszczy chwilę jak mętna powierzchnia powietrza i po chwili skóra znów jest cała, jakby nigdy nic”.
674. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +30% damage on Critical Hit
   PL: Zadaje +30% obrażeń przy trafieniu krytycznym
675. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] Nakłada 3 [Laceration]
676. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]
   PL: [OnSucceedAttack] Nakłada 3 [Combustion]
677. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] 대상의 [Combustion] 발동. 대상의 [Combustion] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=3].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Combustion]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Combustion] = 화상 / Burn
   EN: [CriticalOnSucceedAttack] Activate [Combustion] on target. Target loses 1 [Combustion] Count
   PL: [CriticalOnSucceedAttack] Uruchamia [Combustion] celu. Cel traci 1 Licznika [Combustion]
678. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 5 — opis] [CriticalOnSucceedAttack] 대상의 [Laceration] 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=3].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Activate [Laceration] on target. Target loses 1 [Laceration] Count
   PL: [CriticalOnSucceedAttack] Uruchamia [Laceration] celu. Cel traci 1 Licznika [Laceration]
679. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 6 — opis] [CriticalOnSucceedAttack] 이 코인 최종 피해량의 ([SojiRyoshuEchoPast] x 3)%만큼 참격 피해
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=3].coinlist[#0].coindescs[#5].desc
   (powtórzenie elementu 661 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Umiejętność 3 (×1) (ulepszenie 4) — opis] [WhenUse] 자신의 [Breath] 4당 최종 위력 +1 (최대 5)\n<style="highlight">[WhenUse] 메인 타겟의 [Combustion]과 [Laceration]의 합 6당 기본 위력 +1 (최대 5)</style>\n[WhenUse] 자신의 [SojiRyoshuEchoPast] 1당 피해량 +5%\n[WhenUse] [Breath] 5 얻음\n[WhenUse] 자신의 [SojiRyoshuEchoPast] 2당 가중치 +1 (최대 2)\n[WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당 피해량 <style="highlight">+30%</style> (집중 전투의 경우, 부위로 판정)\n[EndSkill] 이 스킬의 적중 대상에게 [PhantomIncisionID]을 (자신의 [SojiRyoshuEchoPast] + 10)만큼 무작위로 나눠서 부여
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=4].desc
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [Breath], [Combustion], [Laceration], [SojiRyoshuEchoPast], [EndSkill], [PhantomIncisionID]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [SojiRyoshuEchoPast] = 얽힘 / Entanglement; [EndSkill] = [공격 종료시] / [Attack End]; [PhantomIncisionID] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [WhenUse] Final Power +1 for every 4 [Breath] on self (max 5)\n<style="highlight">[WhenUse] Base Power +1 for every 6 ([Combustion] + [Laceration]) on the main target (max 5)</style>\n[WhenUse] Deal +5% damage for every [SojiRyoshuEchoPast] on self\n[WhenUse] Gain 5 [Breath]\n[WhenUse] Gain +1 Atk Weight for every 2 [SojiRyoshuEchoPast] on self (max 2)\n[WhenUse] Deal <style="highlight">+30%</style> damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Parts)\n[EndSkill] Randomly inflict ([SojiRyoshuEchoPast] on self + 10) [PhantomIncisionID] between targets hit by this Skill
   PL: [WhenUse] Moc Końcowa +1 za każde 4 [Breath] (maks. 5)\n<style="highlight">[WhenUse] Moc Bazowa +1 za każde 6 (suma [Combustion] i [Laceration] głównego celu) (maks. 5)</style>\n[WhenUse] Zadaje +5% obrażeń za każde 1 [SojiRyoshuEchoPast]\n[WhenUse] Zyskuje 5 [Breath]\n[WhenUse] Waga ataku +1 za każde 2 [SojiRyoshuEchoPast] (maks. 2)\n[WhenUse] Zadaje <style="highlight">+30%</style> obrażeń za każdego 1 nadmiarowego celu ataku ponad wagę ataku tej Umiejętności (w walce skupionej: części ciała)\n[EndSkill] Losowo rozdziela ([SojiRyoshuEchoPast] + 10) [PhantomIncisionID] między celami trafionymi tą Umiejętnością
681. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] 크리티컬 피해량 <style="highlight">+50%</style>
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>
   EN: Deal <style="highlight">+50%</style> damage on Critical Hit
   PL: Zadaje <style="highlight">+50</style>% obrażeń przy trafieniu krytycznym
682. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Laceration]<style="highlight"></style>
683. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 3 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=4].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Combustion]<style="highlight"></style>
684. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 4 — opis] [CriticalOnSucceedAttack] 대상의 [Combustion] 발동. 대상의 [Combustion] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=4].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Combustion]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Combustion] = 화상 / Burn
   EN: [CriticalOnSucceedAttack] Activate [Combustion] on target. Target loses 1 [Combustion] Count<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Uruchamia [Combustion] celu. Cel traci 1 Licznika [Combustion]<style="highlight"></style>
685. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 5 — opis] [CriticalOnSucceedAttack] 대상의 [Laceration] 발동. 대상의 [Laceration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=4].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [Laceration]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Laceration] = 출혈 / Bleed
   EN: [CriticalOnSucceedAttack] Activate [Laceration] on target. Target loses 1 [Laceration] Count<style="highlight"></style>
   PL: [CriticalOnSucceedAttack] Uruchamia [Laceration] celu. Cel traci 1 Licznika [Laceration]<style="highlight"></style>
686. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 6 — opis] [CriticalOnSucceedAttack] 이 코인 최종 피해량의 ([SojiRyoshuEchoPast] x <style="highlight">4</style>)%만큼 참격 피해
   źródło: Skills_personality-04.json :: dataList[id=1041503].levelList[level=4].coinlist[#0].coindescs[#5].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [CriticalOnSucceedAttack], [SojiRyoshuEchoPast]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [SojiRyoshuEchoPast] = 얽힘 / Entanglement
   EN: [CriticalOnSucceedAttack] Deal Slash damage equal to ([SojiRyoshuEchoPast] x <style="highlight">4</style>)% of this Coin's final damage
   PL: [CriticalOnSucceedAttack] Zadaje obrażenia Cięcia równe ([SojiRyoshuEchoPast] x <style="highlight">4</style>)% końcowych obrażeń tej monety
687. [Umiejętność 4 (×0) (ulepszenie 1) — nazwa] 천살[天殺]
   źródło: Skills_personality-04.json :: dataList[id=1041505].levelList[level=1].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 16 · monety: 1 (+2)
   limit: do 50 znaków
   EN: Slay the Heavens - Tiansha [天殺]
   PL: Zabicie Niebios - Tiansha [天殺]
688. [Umiejętność 4 (×0) (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않으며, 외부 효과로 재사용이 불가능함\n이 스킬을 사용하는 동안 아군의 기본 정신력 감소 조건을 비활성화\n[WhenUse] 이번 전투 동안 공격 레벨 1 감소, 공격 기본 위력 1 증가 (전투당 4회)\n[TargetKill] 정신력 20 회복\n[TargetKill] 이 스킬로 가한 피해량만큼 [RyoshuEGOPF] 얻음
   źródło: Skills_personality-04.json :: dataList[id=1041505].levelList[level=1].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [TargetKill], [RyoshuEGOPF]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [TargetKill] = [대상 처치 시] / [On Target Kill]; [RyoshuEGOPF] = 나생[羅生] / Entangled Life [羅生]
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills, and external effects cannot trigger this Skill to be Reused\nDeactivates allies' "Base factors decreasing Sanity" while using this Skill\n[WhenUse] For this Encounter, lose 1 Offense Level and gain Base Power +1 for this unit's Attacks (4 times per Encounter)\n[TargetKill] Heal 20 SP\n[TargetKill] Gain [RyoshuEGOPF] equal to damage dealt using this Skill
   PL: [CantDuel]\nTa Umiejętność nie uruchamia Umiejętności obrony, a zewnętrzne efekty nie mogą jej ponownie uruchomić\nPodczas używania tej Umiejętności dezaktywuje warunki spadku Poczytalności sojuszników\n[WhenUse] Na czas tego spotkania traci 1 Poziomu Ataku i zyskuje Moc Bazową +1 (4 razy na spotkanie)\n[TargetKill] Odzyskuje 20 Poczytalności\n[TargetKill] Zyskuje [RyoshuEGOPF] równy obrażeniom zadanym tą Umiejętnością
689. [Umiejętność 4 (×0) (ulepszenie 1) — tekst klimatyczny] “퉷. 부모는 하늘 같다던가?”
   źródło: Skills_personality-04.json :: dataList[id=1041505].levelList[level=1].flavor
   limit: do 150 znaków
   EN: "*spit* How does that saying go again? That ya gotta venerate your parents like you venerate the very heavens?"
   PL: „Pfu. Jak to tam szło? Rodziców ma się czcić jak same niebiosa?”
690. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [PhantomIncisionID] 20 부여
   źródło: Skills_personality-04.json :: dataList[id=1041505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PhantomIncisionID]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PhantomIncisionID] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [OnSucceedAttack] Inflict 20 [PhantomIncisionID]
   PL: [OnSucceedAttack] Nakłada 20 [PhantomIncisionID]
691. [Umiejętność 4 (×0) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 거미집 소속 아군 인격이면, 대상 최대 체력의 120%만큼 고정 피해
   źródło: Skills_personality-04.json :: dataList[id=1041505].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] If target is a The House of Spiders ally, deal 120% HP damage as fixed damage
   PL: [OnSucceedAttack] Jeżeli celem jest sojusznicza Tożsamość Domu Pajęczyn, zadaje 120% HP jako obrażenia stałe
692. [Umiejętność 5 (×0) (ulepszenie 1) — nazwa] 필연쇄[必然殺]
   źródło: Skills_personality-04.json :: dataList[id=1041506].levelList[level=1].name
   kontekst: grzech: Pride · typ: Slash · moc bazowa: 10 · monety: 1 (+4)
   limit: do 40 znaków
   EN: Inevitable Termination [必然殺]
   PL: Nieuchronna Egzekucja [必然殺]
693. [Umiejętność 5 (×0) (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않으며, 외부 효과로 재사용이 불가능함\n[WhenUse] 자신의 [Breath] 횟수 1 증가\n[BeforeAttack] 이 스킬을 호출한 스킬이 스킬 3이면,\n- 가중치가 [SojiRyoshuEchoFuture]을 보유한 모든 적의 수로 변경됨 (최소 1)\n- [SojiRyoshuEchoFuture]을 보유한 적을 대상으로 우선 지정\n[EndSkill] 대상의 [SojiRyoshuEchoFuture] 소멸
   źródło: Skills_personality-04.json :: dataList[id=1041506].levelList[level=1].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [Breath], [BeforeAttack], [SojiRyoshuEchoFuture], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [SojiRyoshuEchoFuture] = 잔영 / Phantom Trace; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills, and external effects cannot trigger this Skill to be Reused\n[WhenUse] Gain +1 [Breath] Count\n[BeforeAttack] If this Skill was triggered by Skill 3,\n- Apply this Skill's Atk Weight equal to the number of enemies that have [SojiRyoshuEchoFuture] (min 1)\n- Prioritize enemies that have [SojiRyoshuEchoFuture]\n[EndSkill] Target's [SojiRyoshuEchoFuture] expires
   PL: [CantDuel]\nTa Umiejętność nie uruchamia Umiejętności obrony, a zewnętrzne efekty nie mogą jej ponownie uruchomić\n[WhenUse] Zwiększa własny Licznik [Breath] o 1\n[BeforeAttack] Jeżeli ta Umiejętność została wywołana przez Umiejętność 3,\n- Waga ataku tej Umiejętności zmienia się równy liczbie wrogów z [SojiRyoshuEchoFuture] (min. 1)\n- Namierza najpierw wrogów z [SojiRyoshuEchoFuture]\n[EndSkill] Wygasa [SojiRyoshuEchoFuture] celu
694. [Umiejętność 5 (×0) (ulepszenie 1) — tekst klimatyczny] “호오… 무언가를 남겨내고 마는 지혜성도를 그런 방식으로도 쓸 수 있었나. 좀 치사하긴 해도, 반드시 맞을 수밖에 없는 공격이라니… 하! 그 검, 마음에 드는군!”
   źródło: Skills_personality-04.json :: dataList[id=1041506].levelList[level=1].flavor
   limit: do 290 znaków
   EN: "Oho... What an ingenious way to use the Dihui Star's Blade, the sword that always leaves a lingering something in its wake. Attacks that are impossible to avoid seem a bit cheap, but... hah! I've got to say, I like that sword!"
   PL: „Oho… Kto by pomyślał, że Gwiazdę Dihui da się tak obracać — żeby zawsze coś zostawało po ostrzu. Ataki nie do uniknięcia to trochę tanio, ale… ha! Muszę przyznać, ten miecz mi się podoba!”
695. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 1, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-04.json :: dataList[id=1041506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 674 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [PhantomIncisionID] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041506].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 638 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 [SojiRyoshuEchoPast]만큼 [PhantomIncisionID] 부여 (최대 4)
   źródło: Skills_personality-04.json :: dataList[id=1041506].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 대상의 [Combustion] 발동. 대상의 [Combustion] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041506].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Activate [Combustion] on target. Target loses 1 [Combustion] Count
   PL: [OnSucceedAttack] Uruchamia [Combustion] celu. Cel traci 1 Licznika [Combustion]
699. [Umiejętność 5 (×0) (ulepszenie 1) — moneta 1, efekt 5 — opis] [CriticalOnSucceedAttack] [SlashTakeDamageUp] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041506].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [SlashTakeDamageUp]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [SlashTakeDamageUp] = 참격 취약 / Slash Fragility
   EN: [CriticalOnSucceedAttack] Inflict 1 [SlashTakeDamageUp]
   PL: [CriticalOnSucceedAttack] Nakłada 1 [SlashTakeDamageUp]
700. [Umiejętność 6 (×0) (ulepszenie 3) — nazwa] 공간참 - 잔 [空間斬 - 殘]
   źródło: Skills_personality-04.json :: dataList[id=1041507].levelList[level=3].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 16 · monety: 2 (+1)
   limit: do 50 znaków
   EN: Rend Space - Echoshear [空間斬 - 殘]
   PL: Rozprucie Przestrzeni - Echoshear [空間斬 - 殘]
701. [Umiejętność 6 (×0) (ulepszenie 3) — opis] [WhenUse] 자신의 ([SojiRyoshuEntangle]) 수치만큼 이 스킬의 기본 위력이 1 감소하고, 스킬의 2코인 사용 전에 1코인이 추가됨\n[WhenUse] 자신의 [SojiRyoshuEchoPast] 수치당 마지막 코인 위력 +1\n[WhenUse] 이 스킬 공격 가중치보다 낮은 공격 대상 1당 피해량 +50% (집중 전투의 경우, 부위로 판정)\n[EndSkill] 자신의 [SojiRyoshuEchoPast] 최솟값, 최댓값이 1 증가하고, [SojiRyoshuEchoPast]을 최솟값으로 초기화 (전투당 최대 2회 증가)\n[EndSkill] [PhantomIncisionTotalID] 50 소모
   źródło: Skills_personality-04.json :: dataList[id=1041507].levelList[level=3].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [SojiRyoshuEntangle], [SojiRyoshuEchoPast], [EndSkill], [PhantomIncisionTotalID]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SojiRyoshuEntangle] = 절연[絕緣] / String Severance [絕緣]; [SojiRyoshuEchoPast] = 얽힘 / Entanglement; [EndSkill] = [공격 종료시] / [Attack End]; [PhantomIncisionTotalID] = 지혜성도 / Dihui Star's Blade
   EN: [WhenUse] For every [SojiRyoshuEntangle] on self, this Skill loses 1 Base Power and gains an extra Coin 1 before using Coin 2\n[WhenUse] The final Coin gains Coin Power +1 for every [SojiRyoshuEchoPast] on self\n[WhenUse] Deal +50% damage for every excess Atk Weight beyond the # of actual targets (in Focused Encounters, the Parts)\n[EndSkill] Raise [SojiRyoshuEchoPast]'s Min & Max Stack cap by 1 and reset [SojiRyoshuEchoPast] on self to minimum Stack (max 2 times per Encounter)\n[EndSkill] Consume 50 [PhantomIncisionTotalID]
   PL: [WhenUse] Za każde 1 [SojiRyoshuEntangle] ta Umiejętność traci 1 Moc Bazową, a przed użyciem monety 2 dodaje dodatkową monetę 1\n[WhenUse] Moc ostatniej monety +1 za każde 1 [SojiRyoshuEchoPast]\n[WhenUse] Zadaje +50% obrażeń za każdego 1 nadmiarowego celu ataku ponad wagę ataku tej Umiejętności (w walce skupionej: części ciała)\n[EndSkill] Podnosi minimalny i maksymalny stos [SojiRyoshuEchoPast] o 1 i resetuje [SojiRyoshuEchoPast] do minimalnego stosu (maks. 2 razy na spotkanie)\n[EndSkill] Zużywa 50 [PhantomIncisionTotalID]
702. [Umiejętność 6 (×0) (ulepszenie 3) — tekst klimatyczny] “처음 보는 렌드 스페이스. 새로운 형태로 공간을 베어내는 참격이네요.”\n”공간을 벤 뒤에도 계속 검을 수련하다 보면, 저마다의 방식으로 공간을 벨 수 있게 된다는 이야기, 들어보셨나요? 자신만의 포인트가 궤적에 묻어나오기 시작하면, 공간을 더 오래 갈라놓을 수도, 오히려 더 찰나와 같이 베어낼 수도 있답니다.”\n”공간을 베는 방법은 검을 쓰는 자들에겐 일종의 프라이드. 그 방식을 두고 말다툼이 벌어지기도 하죠. 후훗. 다른 마에스트로들과 예술로 다투던 때가 떠오르는 걸요?”
   źródło: Skills_personality-04.json :: dataList[id=1041507].levelList[level=3].flavor
   limit: do 950 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "This indeed paves a new avenue in the field of space-rending techniques."\n"Have you heard? One might think that rending the very fabric of space is the culmination of the Way of the Blade, but the path extends beyond that. Continue training, and one develops their own unique style of doing so. It adds another layer of artistry by leaving an unconventional touch to the universal technique, allowing for the rent to linger or, sometimes, even be reduced into the flash of an instant."\n"It is somewhat of a point of pride for those who walk the Way of the Blade, meaning that it is also a frequent point of contention in the field. Fuhu, it is reminiscent of the days I used to engage in discourse of comparable belligerence with the other Maestros."
   PL: „To rzeczywiście otwiera nową ścieżkę w dziedzinie technik rozpruwania przestrzeni”.\n„Czy wie Pan/Pani? Ktoś mógłby pomyśleć, że rozprucie tkanki samej przestrzeni to ukoronowanie Szkoły Miecza, lecz ścieżka biegnie dalej. Kto trwa w ćwiczeniu, wypracuje w końcu własny styl. Wprowadza on dodatkowy strumień sztuki, odbiegając od powszechnej techniki — rozcięcie może trwać dłużej albo, nierzadko, skrócić się do mgnienia oka”.\n„Sposób rozpruwania przestrzeni to pewien punkt dumy dla idących Drogą Miecza; stąd też to częsty przedmiot sporów w tym gronie. Fuhu, przypomina to dni, gdy o sztukę spierałam się z innymi Mistrzami”
703. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041507].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL: [OnSucceedAttack] Zyskuje +1 Licznika [Breath]
704. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Combustion] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041507].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 1 부여
   źródło: Skills_personality-04.json :: dataList[id=1041507].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 430 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_personality-04.json :: dataList[id=1041507].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 674 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [PhantomIncisionID]을 모두 소모하여, 이 코인의 최종 피해량의 (소모값 / 10)%만큼 참격 피해
   źródło: Skills_personality-04.json :: dataList[id=1041507].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [PhantomIncisionID]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [PhantomIncisionID] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: [OnSucceedAttack] Consume all [PhantomIncisionID] on target and deal Slash damage equal to ([PhantomIncisionID] consumed / 10)% of this Coin's final damage
   PL: [OnSucceedAttack] Zużywa całe [PhantomIncisionID] celu i zadaje obrażenia Cięcia równe (zużyte/10)% końcowych obrażeń tej monety
708. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] 이 코인의 최종 피해량의 ([SojiRyoshuEchoPast] x 4)%만큼 참격 피해
   źródło: Skills_personality-04.json :: dataList[id=1041507].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [SojiRyoshuEchoPast]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [SojiRyoshuEchoPast] = 얽힘 / Entanglement
   EN: [CriticalOnSucceedAttack] Deal Slash damage equal to ([SojiRyoshuEchoPast] x 4)% of this Coin's final damage
   PL: [CriticalOnSucceedAttack] Zadaje obrażenia Cięcia równe ([SojiRyoshuEchoPast] x 4)% końcowych obrażeń tej monety
709. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 2, efekt 4 — opis] [CriticalOnSucceedAttack] 대상의 [Combustion] 발동. 대상의 [Combustion] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041507].levelList[level=3].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 677 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Umiejętność 6 (×0) (ulepszenie 3) — moneta 2, efekt 5 — opis] [CriticalOnSucceedAttack] 대상의 [Laceration] 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041507].levelList[level=3].coinlist[#1].coindescs[#4].desc
   (powtórzenie elementu 678 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Umiejętność 7 (×0) (ulepszenie 3) — nazwa] 공간참 - 연[空間斬 - 緣]
   źródło: Skills_personality-04.json :: dataList[id=1041508].levelList[level=3].name
   kontekst: grzech: Wrath · typ: Slash · moc bazowa: 14 · monety: 2 (+3)
   limit: do 60 znaków
   EN: Rend Space - String Connection [空間斬 - 緣]
   PL: Rozprucie Przestrzeni - Połączenie [空間斬 - 緣]
712. [Umiejętność 7 (×0) (ulepszenie 3) — opis] [CantDuel]\n이 스킬은 대상의 수비 스킬을 발동시키지 않음\n[WhenUse] [Breath] 5 얻음\n[WhenUse] [SojiRyoshuShin] 얻음\n[EndSkill] 자신의 가장 높은 흐트러짐 구간 1개 제거 (전투당 1회)
   źródło: Skills_personality-04.json :: dataList[id=1041508].levelList[level=3].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [Breath], [SojiRyoshuShin], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [SojiRyoshuShin] = 신(心) - 지혜성[地慧星] / Shin (心) - Dihui Star [地慧星]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantDuel]\nThis Skill does not trigger the target's Defense Skills\n[WhenUse] Gain 5 [Breath]\n[WhenUse] Gain [SojiRyoshuShin]\n[EndSkill] Remove this unit's first Stagger Threshold (once per Encounter)
   PL: [CantDuel]\nTa Umiejętność nie uruchamia Umiejętności obrony celu\n[WhenUse] Zyskuje 5 [Breath]\n[WhenUse] Zyskuje [SojiRyoshuShin]\n[EndSkill] Usuwa pierwszy Próg Oszołomienia tej jednostki (1 raz na spotkanie)
713. [Umiejętność 7 (×0) (ulepszenie 3) — tekst klimatyczny] “공간을 따라 이미 베어진 궤적에 잠깐이나마 상대를 공간째로 박제하듯 고정시켰는가.”\n”본래 저러한 참격에 당한 자는 너무 예리하게 베여, 베인 사실조차 인지하지 못할 것이오. 혹은 공간을 점한 검흔 때문에 사지를 움직이지 못하다, 뒤늦게 피를 토해냈을 테지.”\n”허나... 저 검격은 다르오.”\n”검으로 벤 것은 하나의 궤적이지만, 납도를 함과 동시에 그 궤적으로 지나갔을 수많은 베어냄을 사고하며 구현한 기예…”\n”으음, 그날 이후로 눈에 자주 밟히는구료. 저 참격과 같이 인과를 뒤집어 놓은 듯한 기예들이.”
   źródło: Skills_personality-04.json :: dataList[id=1041508].levelList[level=3].flavor
   limit: do 940 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Taxidermied and immobilized does the foe lie in the trace the blade has rent in space."\n"Such bladework is oft of utter keenness that its victims know not that they have been hewn; or even if they are somehow cognizant of the fact, they are affixed by a bladetrail that has seized the space they inhabit, only to bleed when the moment passes."\n"Yet... the difference lies in how it cuts."\n"The blade has indeed hewn but a singular trace, yet in sheathing it the wielder has conjured in their mind the multitude of slashes that have followed the same path—a most precise technique."\n"Hm. Oft have I come across techniques such as that slash in the days following the incident, techniques that seem to contradict the very nature of causality."
   PL: „Wrogowie leżą wydybani i unieruchomieni w śladzie rozprutym przez ostrze w przestrzeni”.\n„Takie cięcie jest niekiedy tak niezwykle ostre, że ofiary nie wiedzą nawet, że zostały ścięte; a jeżeli jakoś pojmą ten fakt, przysparza je ślad ostrza zawładnięty przestrzenią, w której przebywają, by dopiero po chwili wykrwawić się”.\n„Jednakże... różnica leży w sposobie cięcia”.\n„Ostrze ścięło co prawda pojedynczy ślad, lecz przy spoczęciu ostrza w pochwie posiadacz wyobraził sobie w myślach mnogość cięć idących tą samą ścieżką — to technika najwyższej precyzji”.\n„Hm. Odtąd często przychodzi mi do oczu techniki podobne temu cięciu — techniki, które zdają się odwracać samą naturę przyczyny i skutku”
714. [Umiejętność 7 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 5 부여
   źródło: Skills_personality-04.json :: dataList[id=1041508].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion]
   PL: [OnSucceedAttack] Nakłada 5 [Combustion]
715. [Umiejętność 7 (×0) (ulepszenie 3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041508].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Umiejętność 7 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Combustion] 발동. 대상의 [Combustion] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041508].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 698 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Obrona (ulepszenia 1,4) — nazwa] 잔상보[殘像步]
   źródło: Skills_personality-04.json :: dataList[id=1041504].levelList[level=1].name ; dataList[id=1041504].levelList[level=4].name
   kontekst: grzech: Pride · typ: obrona: unik · moc bazowa: 4 · monety: 1 (+10)
   limit: do 40 znaków
   EN: Phantom Step [殘像步]
   PL: Krok Fantoma [殘像步]
718. [Obrona (ulepszenie 1) — opis] [StartBattle] 출전 인원 중 편성 순서가 가장 느린 아군 거미집 소속 인격 1명을 지정 (턴당 2회)\n- 자신의 [SojiRyoshuEntangle]이 1 이상이면. 1명 추가 지정\n- 대상이 이번 턴에 장착한 모든 스킬이 종료되거나, 흐트러졌거나, 사용할 스킬이 없으면, 대상을 ‘천살’로 일방공격 (인격당 1회)\n- 거미집 소지 제자 싱클레어는 가장 낮은 지정 우선순위를 가짐\n[StartBattle] 자신의 [Breath] 횟수 3 증가 (턴당 1회)
   źródło: Skills_personality-04.json :: dataList[id=1041504].levelList[level=1].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [SojiRyoshuEntangle], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SojiRyoshuEntangle] = 절연[絕緣] / String Severance [絕緣]; [Breath] = 호흡 / Poise
   EN: [StartBattle] Targets 1 The House of Spiders ally with the lattermost Deployment order (2 times per turn)\n- At 1+ [SojiRyoshuEntangle], target 1 additional ally\n- At Skill End of all of the Skills equipped by target this turn, or if target is Staggered, or if target does not have any Skills remaining to be used, use "Slay the Heavens - Tiansha" against target as an Unopposed Attack (once per Identity)\n - Prioritizes The House of Spiders: The Pinky Apprentice Sinclair last\n[StartBattle] Gain +3 [Breath] Count (once per turn)
   PL: [StartBattle] Namierza 1 sojuszniczą Tożsamość Domu Pajęczyn przydzieloną najpóźniej (2 razy na turę)\n- Przy 1+ [SojiRyoshuEntangle] namierza 1 dodatkowego sojusznika\n- Na koniec wszystkich Umiejętności wyposażonych przez cel w tej turze, albo gdy cel jest Ogłuszony albo nie ma więcej Umiejętności do użycia, używa „Zabicie Niebios - Tiansha” na celu jako ataku nieopartego (1 raz na Tożsamość)\n- Namierza Wyroczni Mały Palec Ucznia Sinclaira Domu Pajęczyn jako ostatniego\n[StartBattle] Zwiększa własny Licznik [Breath] o 3 (1 raz na turę)
719. [Obrona (ulepszenia 1,4) — tekst klimatyczny] “그건 내 잔상이다만”
   źródło: Skills_personality-04.json :: dataList[id=1041504].levelList[level=1].flavor ; dataList[id=1041504].levelList[level=4].flavor
   limit: do 120 znaków
   EN: "What you're pursuing is my phantom."
   PL: „Tym, czego dopatrujesz się, jest mój fantom”.
720. [Obrona (ulepszenie 4) — opis] [StartBattle] 출전 인원 중 편성 순서가 가장 느린 아군 거미집 소속 인격 1명을 지정 (턴당 2회)\n- 자신의 [SojiRyoshuEntangle]이 1 이상이면. 1명 추가 지정\n- 대상이 이번 턴에 장착한 모든 스킬이 종료되거나, 흐트러졌거나, 사용할 스킬이 없으면, 대상을 ‘천살’로 일방공격 (인격당 1회)\n- 거미집 소지 제자 싱클레어는 가장 낮은 지정 우선순위를 가짐\n[StartBattle] 자신의 [Breath] 횟수 3 증가 (턴당 1회)\n<style="highlight">[OnSucceedEvade] [Breath] 1 얻음 (턴당 3회)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041504].levelList[level=4].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [SojiRyoshuEntangle], [Breath], [OnSucceedEvade]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [SojiRyoshuEntangle] = 절연[絕緣] / String Severance [絕緣]; [Breath] = 호흡 / Poise; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [StartBattle] Targets 1 The House of Spiders ally with the lattermost Deployment order (2 times per turn)\n- At 1+ [SojiRyoshuEntangle], target 1 additional ally\n- At Skill End of all of the Skills equipped by target this turn, or if target is Staggered, or if target does not have any Skills remaining to be used, use "Slay the Heavens - Tiansha" against target as an Unopposed Attack (once per Identity)\n - Prioritizes The House of Spiders: The Pinky Apprentice Sinclair last\n[StartBattle] Gain +3 [Breath] Count (once per turn)\n<style="highlight">[OnSucceedEvade] Gain 1 [Breath] (3 times per turn)</style>
   PL: [StartBattle] Namierza 1 sojuszniczą Tożsamość Domu Pajęczyn przydzieloną najpóźniej (2 razy na turę)\n- Przy 1+ [SojiRyoshuEntangle] namierza 1 dodatkowego sojusznika\n- Na koniec wszystkich Umiejętności wyposażonych przez cel w tej turze, albo gdy cel jest Ogłuszony albo nie ma więcej Umiejętności do użycia, używa „Zabicie Niebios - Tiansha” na celu jako ataku nieopartego (1 raz na Tożsamość)\n- Namierza Wyroczni Mały Palec Ucznia Sinclaira Domu Pajęczyn jako ostatniego\n[StartBattle] Zwiększa własny Licznik [Breath] o 3 (1 raz na turę)\n<style="highlight">[OnSucceedEvade] Zyskuje 1 [Breath] (3 razy na turę)</style>
721. [Pasywka bojowa (od ulepszenia 1) — nazwa] 재회[再会]
   źródło: Passives.json :: dataList[id=1041502].name
   limit: do 40 znaków
   EN: Saikai [再会]
   PL: Saikai [再会]
722. [Pasywka bojowa (od ulepszenia 1) — opis] 전투에 첫 등장 시, [SojiRyoshuEchoPast] 0, [SojiRyoshuEntangle] 0 얻음.\n\n전투에 첫 등장 시, 편성된 거미집 소속 아군 인격(자신 포함) 3명당 [SojiRyoshuEchoPast]의 최솟값, 최댓값이 1 증가 (최대 3)\n\n거미집 소속 인격이 출전중이면, 자신이 체력 피해를 받을 때 현재 체력 비율이 가장 낮은 거미집 소속 아군 인격에게 받은 체력 피해를 전가함\n\n체력이 0이 되는 피해를 받을 때 해당 턴 동안 체력이 1 미만으로 감소하지 않음 (전투당 1회)\n\n거미집 소속 아군 인격이 사망한 상태면, 아래 효과 적용\n- [SojiRyoshuEchoPast] 1 얻음\n- 사망한 인격에 따라 이번 전투 동안 아래 추가 효과를 얻음\n · 거미집 검지 아비 이상 : 기본 공격 스킬 사용시 마지막 코인이 [SuperCoin]으로 변경됨. 기본 공격 스킬의 [SuperCoin]의 피해량 +10%\n · 검지 대행자 - 개화[TabExplain] E.G.O:: 대행 돈키호테 : 기본 공격 스킬 사용시 [Breath] 2 얻음. 기본 공격 스킬 크리티컬 적중시 [Sinking] 1 부여\n · 거미집 중지 제자 이스마엘 : 방어 레벨 +2, 기본 스킬로 부여하는 [Combustion] 위력 +1\n · 거미집 약지 아비 홍루 : [MelodyBodyArt] 얻음\n · 거미집 약지 제자 파우스트 : 매 턴 시작시 최대 체력의 10%만큼 보호막 얻음\n · 거미집 소지 제자 싱클레어 : 매 턴 시작시 [Breath] 횟수 1, [CriticalDamageUp] 1 얻음\n\n대기 해제 또는 복귀할 인격이 없으면, 사망 상태인 아군 거미집 소속 인격 3명당 거미집의 검 료슈의 슬롯 수 +1 (최대 3회 증가)\n- 이 효과로 인해 해당 전투의 최대 슬롯 수를 초과하여 슬롯이 증가할 수 없음\n- 일부 콘텐츠의 슬롯 증가 제한 효과를 무시하고 발동 가능\n\n이 인격은 [Combustion], [Laceration], [Breath]을 부여하는 인격으로만 취급됨\n\n특정 조건 달성 시 이번 전투 동안 전투 BGM을 변경 (일부 전투 제외)
   źródło: Passives.json :: dataList[id=1041502].desc
   limit: do 2730 znaków
   tokeny: zachowaj dokładnie: \n, [SojiRyoshuEchoPast], [SojiRyoshuEntangle], [SuperCoin], [TabExplain], [Breath], [Sinking], [Combustion], [MelodyBodyArt], [CriticalDamageUp], [Laceration]
   znaczenie tagów: [SojiRyoshuEchoPast] = 얽힘 / Entanglement; [SojiRyoshuEntangle] = 절연[絕緣] / String Severance [絕緣]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Breath] = 호흡 / Poise; [Sinking] = 침잠 / Sinking; [Combustion] = 화상 / Burn; [MelodyBodyArt] = 신체가 울리는 선율 / Somatic Frisson-inspiring Melody; [CriticalDamageUp] = 크리티컬 피해량 증가 / Crit DMG Up …
   EN: Upon entering the Encounter for the first time, gain 0 [SojiRyoshuEchoPast] and 0 [SojiRyoshuEntangle]\n\nUpon entering the Encounter for the first time, for every 3 The House of Spiders Identities in the Loadout (including this unit), raise [SojiRyoshuEchoPast]'s Min & Max Stack cap by 1 (max 3)\n\nIf any of The House of Spiders allied Identities are on the field, transfer HP damage taken to The House of Spiders Identity that has the lowest current HP percentage\n\nWhen this unit takes damage that brings its HP down to 0, this unit's HP does not drop below 1 for the turn (once per Encounter)\n\nApply the following effects based on The House of Spiders ally death:\n- Gain 1 [SojiRyoshuEchoPast]\n- For this Encounter, gain additional effects based on which of The House of Spiders allied Identity was defeated\n · The House of Spiders: The Index Nursefather Yi Sang: On Base Attack Skill Use, convert the final Coin into [SuperCoin]. Deal +10% damage with Base Attack Skills' [SuperCoin]s\n · The Index Proxy - Effloresced E.G.O::Procuration Don Quixote: On Base Attack Skill Use, gain 2 [Breath]. On Crit using Base Attack Skills, inflict 1 [Sinking]\n · The House of Spiders: The Middle Apprentice Ishmael: Defense Level +2. Inflict +1 more [Combustion] Potency using Base Skills\n · The House of Spiders: The Ring Nursefather Hong Lu: Gain [MelodyBodyArt]\n · The House of Spiders: The Ring Apprentice Faust: Gain Shield equal to 10% HP at every Turn Start\n · The House of Spiders: The Pinky Apprentice Sinclair: Gain +1 [Breath] Count and 1 [CriticalDamageUp] at every Turn Start\n\nIf there are no Identities left to Substitute or Return, Blade of the House of Spiders Ryōshū gains +1 Skill Slot for every 3 The House of Spiders allies that are defeated (max 3 times)\n- This effect cannot increase Skill Slots beyond the maximum Skill Slot cap of this Encounter\n- For certain game contents, this effect can activate regardless of the contents' Skill Slot increase restriction\n\nThis Identity only counts as an "Identity that applies [Combustion], [Laceration], and [Breath]"\n\nWhen conditions are met, change battle music for the rest of the Encounter (excluding certain Encounters)
   PL: Przy pierwszym pojawieniu się na polu zyskuje 0 [SojiRyoshuEchoPast] i 0 [SojiRyoshuEntangle]\n\nPrzy pierwszym pojawieniu się na polu, za każde 3 Tożsamości Domu Pajęczyn w składzie (łącznie z tą jednostką), podnosi minimalny i maksymalny stos [SojiRyoshuEchoPast] o 1 (maks. 3)\n\nJeżeli jakakolwiek sojusznicza Tożsamość Domu Pajęczyn jest na polu, przenosi otrzymane obrażenia HP na sojuszniczą Tożsamość Domu Pajęczyn z najniższym obecnym procentem HP\n\nGdy ta jednostka otrzymuje obrażenia redukujące HP do 0, jej HP nie spada poniżej 1 w tej turze (1 raz na spotkanie)\n\nGdy sojusznicza Tożsamość Domu Pajęczyn ginie, stosuje poniższe efekty:\n- Zyskuje 1 [SojiRyoshuEchoPast]\n- Na czas tego spotkania zyskuje dodatkowe efekty zależnie od tego, która Tożsamość Domu Pajęczyn została pokonana\n · Wyroczni Abi Yi Sang Domu Pajęczyn: przy użyciu podstawowej Umiejętności ataku ostatnia moneta zmienia się w [SuperCoin]. Zadaje +10% obrażeń monetami [SuperCoin] podstawowych Umiejętności ataku\n · Pełnomocnik Wskazującego - Rozkwita E.G.O::Pełnomocnictwo Don Quixote: przy użyciu podstawowej Umiejętności ataku zyskuje 2 [Breath]. Przy trafieniu krytycznym podstawowymi Umiejętnościami ataku nakłada 1 [Sinking]\n · Środkowego Uczeń Ishmael Domu Pajęczyn: Poziom obrony +2. Nakłada o 1 więcej Mocy [Combustion] podstawowymi Umiejętnościami\n · Ringu Abi Hong Lu Domu Pajęczyn: zyskuje [MelodyBodyArt]\n · Ringu Uczeń Faust Domu Pajęczyn: na początku każdej tury zyskuje Tarczę równą 10% HP\n · Wyroczni Mały Palec Uczeń Sinclair Domu Pajęczyn: na początku każdej tury zyskuje +1 Licznika [Breath] i 1 [CriticalDamageUp]\n\nGdy nie ma już Tożsamości do Wejścia z rezerwy lub Powrotu, Ostrze Domu Pajęczyn Ryōshū zyskuje +1 slot Umiejętności za każde 3 pokonane sojusznicze Tożsamości Domu Pajęczyn (maks. 3 razy)\n- Ten efekt nie może zwiększyć slotów Umiejętności ponad maksymalny limit slotów tego spotkania\n- Dla niektórych treści ten efekt może się uruchomić, ignorując ograniczenie zwiększania slotów Umiejętności tych treści\n\nTa Tożsamość liczy się wyłącznie jako „Tożsamość nakładająca [Combustion], [Laceration] i [Breath]”[TabExplain]\n\nPo spełnieniu warunków zmienia muzykę walki na czas tego spotkania (wyłączając niektóre walki)
723. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 받는 피해를 거미집 인격에게 전가
   źródło: Passives.json :: dataList[id=1041502].summary
   limit: do 120 znaków
   EN: Transfer damage taken to The House of Spiders Identities
   PL: Przenosi otrzymane obrażenia na Tożsamości Domu Pajęczyn
724. [Pasywka bojowa (od ulepszenia 1) — tekst klimatyczny] ‘다시 만나고 싶지 않은 것은 다시 만나게 되고, 다시 만나고 싶은 것은 다시 만날 수 없다.’\n’그렇기 때문에 재회의 순간에는 마음을 독하게 먹어야 한다.’
   źródło: Passives.json :: dataList[id=1041502].flavor
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'The things I dread seeing again always come back. The things I ache to see again never do.'\n'That is why I must steel my heart cold in the moment of reunion.'
   PL: „To, czego boję się ujrzeć ponownie, zawsze wraca. To, czego tęsknie pragnę ujrzeć ponownie, nie wraca nigdy”.\n„Dlatego też w chwili ponownego spotkania trzeba nabrać zimnej krwi i stwardnieć sercem”
725. [Pasywka bojowa (od ulepszenia 1) — nazwa] 시공간 잔상 분열
   źródło: Passives.json :: dataList[id=1041504].name
   limit: do 50 znaków
   EN: Spacetime Afterimage Collapse
   PL: Rozpad Fantomu Czasoprzestrzeni
726. [Pasywka bojowa (od ulepszenia 1) — opis] 턴 시작시 무작위 적 1명에게 [SojiRyoshuEchoFuture] 부여 (집중 전투인 경우, 본체로 판정)\n- 사망한 아군 거미집 소속 인격 3명당, 추가로 무작위 적 1명에게 [SojiRyoshuEchoFuture] 부여 (최대 3개 생성)\n- 전투 시작 시 [SojiRyoshuEchoFuture]이 부여된 적을 기본 공격 스킬 메인 타겟으로 지정했으면, 해당 스킬 사용 전 ‘필연쇄’로 일방 공격함. (턴당 1회)\n- [SojiRyoshuEchoFuture]을 보유한 대상에게 기본 공격 스킬 사용시,\n · 해당 스킬 코인이 모두 [SuperCoin]으로 변경되고, 최종 위력 +1\n · [SojiRyoshuEchoPast] 1 얻음 (턴당 1회)
   źródło: Passives.json :: dataList[id=1041504].desc
   limit: do 820 znaków
   tokeny: zachowaj dokładnie: \n, [SojiRyoshuEchoFuture], [SuperCoin], [SojiRyoshuEchoPast]
   znaczenie tagów: [SojiRyoshuEchoFuture] = 잔영 / Phantom Trace; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [SojiRyoshuEchoPast] = 얽힘 / Entanglement
   EN: Turn Start: Inflict [SojiRyoshuEchoFuture] on a random enemy (in Focused Encounters, the Core)\n- Inflict [SojiRyoshuEchoFuture] on 1 additional random enemy for every 3 defeated The House of Spiders allied Identities (max 3)\n- Combat Start: If an enemy that has [SojiRyoshuEchoFuture] is the main target of this unit's Base Attack Skills, use "Inevitable Termination" as an Unopposed Attack before using the said Base Attack Skill (once per turn)\n- On Base Attack Skill Use against target that has [SojiRyoshuEchoFuture],\n · Convert all Coins of the said Skill into [SuperCoin]s and gain Final Power +1\n · Gain 1 [SojiRyoshuEchoPast] (once per turn)
   PL: Na początku tury nakłada [SojiRyoshuEchoFuture] na 1 losowego wroga (w walce skupionej: na trzon)\n- Za każde 3 pokonane sojusznicze Tożsamości Domu Pajęczyn nakłada dodatkowo [SojiRyoshuEchoFuture] na 1 losowego wroga (maks. 3)\n- Na początku walki jeżeli wrogowie z [SojiRyoshuEchoFuture] są głównym celem podstawowych Umiejętności ataku tej jednostki, przed użyciem tej Umiejętności używa „Nieuchronnej Egzekucji” jako ataku nieopartego (1 raz na turę)\n- Przy użyciu podstawowej Umiejętności ataku na celu z [SojiRyoshuEchoFuture],\n · wszystkie monety tej Umiejętności zmieniają się w [SuperCoin] i zyskuje Moc Końcową +1\n · zyskuje 1 [SojiRyoshuEchoPast] (1 raz na turę)
727. [Pasywka bojowa (od ulepszenia 1) — tekst klimatyczny] “끊임없이 나뉘어지고. 나뉘어 갈라진 미래를 마주하고. 그 미래 속에서 다시 베고.”\n”그렇게 분열하면서도 자아를 지켜낼 수 있다니, 근성 하나는 대단하군.”
   źródło: Passives.json :: dataList[id=1041504].flavor
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "To be frayed without cease, and face each frayed strand of the future, and again continue to sever within each and every one of those futures..."\n"To endure that much fragmentation without losing oneself... That's a helluva lot of grit."
   PL: „Wystrzępić się bez końca, spojrzeć w twarz każdej utkanej przyszłości, i znów przeciąć w każdej z tych przyszłości...”\n„Tyle rozedrgań przetrwać, nie tracąc siebie... Spora otucha”
728. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — nazwa] 잔상 반향
   źródło: Passives.json :: dataList[id=1041501].name
   limit: do 40 znaków
   EN: Afterimage Reverberation
   PL: Rezonans Fantoma
729. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — opis] 자신의 20을 초과하는 [Breath] 위력 1당 자신의 기본 공격 스킬 크리티컬 피해량 +1% (최대 10%)\n자신의 기본 공격 스킬이 크리티컬 적중시, [PhantomIncisionID] 1 부여\n\n아군을 대상으로 한 공격 스킬로 삼천대세계 E.G.O 패시브[TabExplain] 발동 가능
   źródło: Passives.json :: dataList[id=1041501].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [PhantomIncisionID], [TabExplain]
   znaczenie tagów: [Breath] = 호흡 / Poise; [PhantomIncisionID] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: Deal +1% damage on Critical Hit using Base Attack Skills for every 1 surplus [Breath] past 20 [Breath] on self (max 10%)\nOn Crit using Base Attack Skills, inflict 1 [PhantomIncisionID]\n\nGreat Trichiliocosm Ryōshū E.G.O Passive can be activated using Attack Skills targeting allies
   PL: Zadaje +1% obrażeń przy trafieniu krytycznym podstawowymi Umiejętnościami ataku za każde 1 nadwyżki [Breath] ponad 20 (maks. 10%)\nPrzy trafieniu krytycznym podstawowymi Umiejętnościami ataku nakłada 1 [PhantomIncisionID]\n\nPasywka „Trzy Tysiące Wielkiego Świata” E.G.O Ryōshū[TabExplain] może zostać uruchomiona Umiejętnościami ataku namierzającymi sojuszników
730. [Pasywka bojowa (od ulepszenia 2, posiadane 5× Pride) — podsumowanie] 크리티컬 피해량 증가[TabExplain], 크리티컬 적중시 [PhantomIncisionID] 부여
   źródło: Passives.json :: dataList[id=1041501].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain], [PhantomIncisionID]
   znaczenie tagów: [PhantomIncisionID] = 검흔[잔상] / Bladetrail [Afterimage]
   EN: Deal more damage on Critical Hit, inflict [PhantomIncisionID] On Crit
   PL: Zadaje więcej obrażeń przy trafieniu krytycznym[TabExplain], nakłada [PhantomIncisionID] przy trafieniu krytycznym
731. [Pasywka bojowa (od ulepszenia 3) — nazwa] 지혜성[地慧星]
   źródło: Passives.json :: dataList[id=1041503].name
   limit: do 40 znaków
   EN: Dihui Star [地慧星]
   PL: Gwiazda Dihui [地慧星]
732. [Pasywka bojowa (od ulepszenia 3) — opis] 자신의 [PhantomIncisionTotalID]가 50 이상이면, 해당 턴의 마지막 순서에 무작위 적에게 ‘공간참 - 연’ 발동 (전투당 1회)\n- 이 효과로 ‘공간참 - 연’을 사용한 후, 자신에게 아래 효과 적용\n· 이번 전투 동안 퇴각 불가\n· 턴 종료시 자신의 [PhantomIncisionTotalID]가 50 이상이면, 다음 턴 시작시 기본 스킬 하나를 ‘공간참 - 잔’으로 변경 (가장 왼쪽 슬롯의 아래 스킬 우선 적용)
   źródło: Passives.json :: dataList[id=1041503].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n, [PhantomIncisionTotalID]
   znaczenie tagów: [PhantomIncisionTotalID] = 지혜성도 / Dihui Star's Blade
   EN: At 50+ [PhantomIncisionTotalID], activate "Rend Space - String Connection" against a random enemy at the very end of that turn (once per Encounter)\n- After using "Rend Space - String Connection" due to this effect, apply the following effects on self:\n· Cannot Retreat for this Encounter\n· Turn End: At 50+ [PhantomIncisionTotalID], replace a Base Skill with "Rend Space - Echoshear" at the next Turn Start (prioritizes the Skill on the leftmost Slot's bottom row on the Dashboard)
   PL: Przy 50+ [PhantomIncisionTotalID] uruchamia „Rozprucie Przestrzeni - Połączenie” na 1 losowym wrogu na samym końcu tury (1 raz na spotkanie)\n- Po użyciu „Rozprucia Przestrzeni - Połączenie” tym efektem stosuje na sobie poniższe efekty:\n· Na czas tego spotkania nie może się wycofać\n· Na koniec tury przy 50+ [PhantomIncisionTotalID] zamienia podstawową Umiejętność w „Rozprucie Przestrzeni - Echoshear” na początku następnej tury (najpierw Umiejętność z lewego dolnego slotu Panelu Sterowania)
733. [Pasywka bojowa (od ulepszenia 3) — tekst klimatyczny] “지혜성도. 천살성도. 별이 벼려진 검을 두 개나 손에 넣었다면, 그대는 대체 어떤 별이라 할 수 있겠는가.”\n”지나친 욕심 끝에 망가지거나 베어져버린 별들이 있음을 그대의 아비 또한 말해주었을 터. 두 자루의 검 중, 오직 하나만을 고르시오.”
   źródło: Passives.json :: dataList[id=1041503].flavor
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Dihui Star's Blade, and Tiansha Star's Blade. If not merely one, but <i>two</i> star-forged blades have come to reside in your hands, then I am moved to wonder, which Star's name could possibly be ideal to represent you?"\n"Your Nursefather, too, must surely have furnished you with the tale—that there had been Stars which, at the terminus of immoderate coveting, were left broken and shorn. Thus, I suggest to you, of these two blades, appoint only one as yours."
   PL: „Miecz Gwiazdy Dihui i Miecz Gwiazdy Tiansha. Skoro nie jedno, lecz <i>dwa</i> ostrza wykute w gwiazdy spoczęły w Twoich dłoniach, kuszę się spytać: czyje imię Gwiazdy mogłoby Cię godnie przedstawić?”\n„Twoja Wyrocznia niechybnie też opowiedziała Ci historię — o Gwiazdach, które u kresu zaborczości zostały połamane i ścięte. Tak więc wybierz spośród tych dwóch mieczów jeden jedyny”
734. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — nazwa] 사사[師事]
   źródło: Passives.json :: dataList[id=1041521].name
   limit: do 40 znaków
   EN: The Master's Tutelage [師事]
   PL: Nauki Mistrza [師事]
735. [Pasywka wsparcia (od ulepszenia 3, rezonans 3× Pride) — opis] 편성 순서가 가장 빠른 아군이 기본 스킬 사용시, [Breath] 위력 2 얻음 (턴당 3회)
   źródło: Passives.json :: dataList[id=1041521].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: When the ally with the earliest Deployment order uses a Base Skill, the said ally gains 2 [Breath] Potency (3 times per turn)
   PL: Gdy 1 Sojusznik przydzielony najwcześniej użyje podstawowej Umiejętności, zyskuje 2 Mocy [Breath] (3 razy na turę)

## [000] Haute Couture:: Le Noir Footwear Hall — Ryōshū — 오트쿠튀르:: 르누아르 신발관
- ID Tożsamości: `10416` (plik: `Personalities.json`)
- parametry karty: rzadkość `000` · sezon: 8 · HP bazowe: 73 · szybkość: 3–5 / 3–6 / 3–7 / 3–7
- odporności: Slash ×0,5 (Endured), Penetrate ×1 (Normal), Hit ×2 (Fatal) · słowa kluczowe: Charge, Tremor

736. [Karta Tożsamości — tytuł] 오트쿠튀르::\n르누아르 신발관
   źródło: Personalities.json :: dataList[id=10416].title
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Haute Couture::\nLe Noir\nFootwear Hall
   PL: Haute Couture::\nLe Noir\nGaleria Obuwia
737. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities.json :: dataList[id=10416].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities.json :: dataList[id=10416].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Karta Tożsamości — opis] 료슈의 열여섯번째 인격
   źródło: Personalities.json :: dataList[id=10416].desc
   limit: do 120 znaków
   EN: Ryōshū's 16th Identity
   PL: Szesnasta Tożsamość Ryōshū
740. [Umiejętność 1 (×3) (ulepszenia 1,2,4) — nazwa] 불결하군
   źródło: Skills_personality-04.json :: dataList[id=1041601].levelList[level=1].name ; dataList[id=1041601].levelList[level=2].name ; dataList[id=1041601].levelList[level=4].name
   kontekst: grzech: Envy · typ: Hit · moc bazowa: 3 · monety: 2 (+4)
   limit: do 40 znaków
   EN: You, Revolting Thing.
   PL: Obrzydliwa Ty.
741. [Umiejętność 1 (×3) (ulepszenie 1) — opis] [StartBattle] 자신의 [ChargeNoirAlly] 위력이 3, [ChargeNoirAlly] 횟수가 12 이상이면,\n[ChargeNoirAlly] 횟수를 6 소모하여 최대 체력의 5%만큼 보호막 얻음 (턴당 2회)\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수가 10 미만이면, 자신의 [ChargeNoirAlly] 횟수 1 증가\n[WhenUse] [RealisationAlly] 최대 15 소모\n- 합 위력 +1\n- 피해량 +(소모한 [RealisationAlly] x 3)% (최대 45%)
   źródło: Skills_personality-04.json :: dataList[id=1041601].levelList[level=1].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [ChargeNoirAlly], [WhenUse], [RealisationAlly]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]; [RealisationAlly] = 아르뮈르 에비이예 / Armure Éveillée
   EN: [StartBattle] At 3+ [ChargeNoirAlly] Potency and 12+ [ChargeNoirAlly] Count, consume 6 [ChargeNoirAlly] Count to gain Shield equal to 5% of this unit's max HP (2 times per turn)\n[WhenUse] At fewer than 10 [ChargeNoirAlly] Count, gain +1 [ChargeNoirAlly] Count\n[WhenUse] Consume up to 15 [RealisationAlly] to apply the following:\n- Clash Power +1\n- Deal +([RealisationAlly] consumed x 3)% damage (max 45%)
   PL: [StartBattle] Przy 3+ Mocy [ChargeNoirAlly] i 12+ Liczniku [ChargeNoirAlly] zużywa 6 Licznika [ChargeNoirAlly], aby zyskać Tarczę równą 5% Maks. HP (2 razy na turę)\n[WhenUse] Poniżej 10 Licznika [ChargeNoirAlly] zwiększa własny Licznik [ChargeNoirAlly] o 1\n[WhenUse] Zużywa do 15 [RealisationAlly], aby stosować poniższe:\n- Moc Starcia +1\n- Zadaje +(zużyte [RealisationAlly] x 3)% obrażeń (maks. 45%)
742. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_personality-04.json :: dataList[id=1041601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [Umiejętność 1 (×3) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 3 증가
   źródło: Skills_personality-04.json :: dataList[id=1041601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +3 [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o 3
744. [Umiejętność 1 (×3) (ulepszenie 2) — opis] [StartBattle] 자신의 [ChargeNoirAlly] 위력이 3, [ChargeNoirAlly] 횟수가 12 이상이면,\n[ChargeNoirAlly] 횟수를 6 소모하여 최대 체력의 5%만큼 보호막 얻음 (턴당 2회)\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수가 10 미만이면, 자신의 [ChargeNoirAlly] 횟수 <style="highlight">2</style> 증가\n[WhenUse] [RealisationAlly] 최대 15 소모\n- 합 위력 +1\n- 피해량 +(소모한 [RealisationAlly] x 3)% (최대 45%)
   źródło: Skills_personality-04.json :: dataList[id=1041601].levelList[level=2].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [ChargeNoirAlly], [WhenUse], [RealisationAlly]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]; [RealisationAlly] = 아르뮈르 에비이예 / Armure Éveillée
   EN: [StartBattle] At 3+ [ChargeNoirAlly] Potency and 12+ [ChargeNoirAlly] Count, consume 6 [ChargeNoirAlly] Count to gain Shield equal to 5% of this unit's max HP (2 times per turn)\n[WhenUse] At fewer than 10 [ChargeNoirAlly] Count, gain +<style="highlight">2</style> [ChargeNoirAlly] Count\n[WhenUse] Consume up to 15 [RealisationAlly] to apply the following:\n- Clash Power +1\n- Deal +([RealisationAlly] consumed x 3)% damage (max 45%)
   PL: [StartBattle] Przy 3+ Mocy [ChargeNoirAlly] i 12+ Liczniku [ChargeNoirAlly] zużywa 6 Licznika [ChargeNoirAlly], aby zyskać Tarczę równą 5% Maks. HP (2 razy na turę)\n[WhenUse] Poniżej 10 Licznika [ChargeNoirAlly] zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">2</style>\n[WhenUse] Zużywa do 15 [RealisationAlly], aby stosować poniższe:\n- Moc Starcia +1\n- Zadaje +(zużyte [RealisationAlly] x 3)% obrażeń (maks. 45%)
745. [Umiejętność 1 (×3) (ulepszenia 2,4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041601].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=1041601].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Vibration]<style="highlight"></style>
746. [Umiejętność 1 (×3) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">4</style> 증가
   źródło: Skills_personality-04.json :: dataList[id=1041601].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +<style="highlight">4</style> [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">4</style>
747. [Umiejętność 1 (×3) (ulepszenie 4) — opis] [StartBattle] 자신의 [ChargeNoirAlly] 위력이 3, [ChargeNoirAlly] 횟수가 12 이상이면,\n[ChargeNoirAlly] 횟수를 6 소모하여 최대 체력의 5%만큼 보호막 얻음 (턴당 2회)\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수가 <style="highlight">12</style> 미만이면, 자신의 [ChargeNoirAlly] 횟수 2 증가\n<style="highlight">[WhenUse] [NoirSuitAlly]가 50 이상이면,\n합 위력 +1, 피해량 +30%</style>\n[WhenUse] [RealisationAlly] 최대 15 소모\n<style="highlight">- 최종 위력 +1</style>\n- 피해량 +(소모한 [RealisationAlly] x 3)% (최대 45%)
   źródło: Skills_personality-04.json :: dataList[id=1041601].levelList[level=4].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [ChargeNoirAlly], [WhenUse], [NoirSuitAlly], [RealisationAlly]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeNoirAlly] = 보존 / Preservation; [WhenUse] = [사용시] / [On Use]; [NoirSuitAlly] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat; [RealisationAlly] = 아르뮈르 에비이예 / Armure Éveillée
   EN: [StartBattle] At 3+ [ChargeNoirAlly] Potency and 12+ [ChargeNoirAlly] Count, consume 6 [ChargeNoirAlly] Count to gain Shield equal to 5% of this unit's max HP (2 times per turn)\n[WhenUse] At fewer than <style="highlight">12</style> [ChargeNoirAlly] Count, gain +2 [ChargeNoirAlly] Count\n<style="highlight">[WhenUse] At 50+ [NoirSuitAlly], Clash Power +1 and deal +30% damage</style>\n[WhenUse] Consume up to 15 [RealisationAlly] to apply the following:\n<style="highlight">- Final Power +1</style>\n- Deal +([RealisationAlly] consumed x 3)% damage (max 45%)
   PL: [StartBattle] Przy 3+ Mocy [ChargeNoirAlly] i 12+ Liczniku [ChargeNoirAlly] zużywa 6 Licznika [ChargeNoirAlly], aby zyskać Tarczę równą 5% Maks. HP (2 razy na turę)\n[WhenUse] Poniżej <style="highlight">12</style> Licznika [ChargeNoirAlly] zwiększa własny Licznik [ChargeNoirAlly] o 2\n<style="highlight">[WhenUse] Przy 50+ [NoirSuitAlly] Moc Starcia +1 i zadaje +30% obrażeń</style>\n[WhenUse] Zużywa do 15 [RealisationAlly], aby stosować poniższe:\n<style="highlight">- Moc Końcowa +1</style>\n- Zadaje +(zużyte [RealisationAlly] x 3)% obrażeń (maks. 45%)
748. [Umiejętność 1 (×3) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">5</style> 증가
   źródło: Skills_personality-04.json :: dataList[id=1041601].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +<style="highlight">5</style> [ChargeNoirAlly] Count
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">5</style>
749. [Umiejętność 2 (×2) (ulepszenia 1,2,4) — nazwa] 와서 시착해봐라
   źródło: Skills_personality-04.json :: dataList[id=1041602].levelList[level=1].name ; dataList[id=1041602].levelList[level=2].name ; dataList[id=1041602].levelList[level=4].name
   kontekst: grzech: Pride · typ: Hit · moc bazowa: 4 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Come and Try It On
   PL: Podbij i Przymierz
750. [Umiejętność 2 (×2) (ulepszenie 1) — opis] [WhenUse]\n- 자신의 [ChargeNoirAlly] 횟수가 12 이상이면, 6 소모하여 합 위력 +1, 피해량 +10%\n- 자신의 [ChargeNoirAlly] 횟수 2 증가\n[WhenUse] [RealisationAlly] 최대 20 소모\n- 합 위력 +1\n- 피해량 +(소모한 [RealisationAlly])% (최대 20%)
   źródło: Skills_personality-04.json :: dataList[id=1041602].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoirAlly], [RealisationAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation; [RealisationAlly] = 아르뮈르 에비이예 / Armure Éveillée
   EN: [WhenUse]\n- At 12+ [ChargeNoirAlly] Count, consume 6 [ChargeNoirAlly] Count to gain Clash Power +1 and deal +10% damage\n- Gain +2 [ChargeNoirAlly] Count\n[WhenUse] Consume up to 20 [RealisationAlly] to apply the following:\n- Clash Power +1\n- Deal +([RealisationAlly] consumed)% damage (max 20%)
   PL: [WhenUse]\n- Przy 12+ Liczniku [ChargeNoirAlly] zużywa 6 Licznika [ChargeNoirAlly], aby zyskać Moc Starcia +1 i zadać +10% obrażeń\n- Zwiększa własny Licznik [ChargeNoirAlly] o 2\n[WhenUse] Zużywa do 20 [RealisationAlly], aby stosować poniższe:\n- Moc Starcia +1\n- Zadaje +(zużyte [RealisationAlly])% obrażeń (maks. 20%)
751. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] (자신의 [ChargeNoirAlly] 위력+1)만큼 자신의 [ChargeNoirAlly] 횟수 증가 (최대 4)
   źródło: Skills_personality-04.json :: dataList[id=1041602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +([ChargeNoirAlly] Potency + 1) [ChargeNoirAlly] Count (max 4)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o wartość (własna Moc [ChargeNoirAlly] + 1) (maks. 4)
752. [Umiejętność 2 (×2) (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 1 증가
   źródło: Skills_personality-04.json :: dataList[id=1041602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +1 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada 2 [Vibration] i zwiększa Licznik [Vibration] o 1
753. [Umiejętność 2 (×2) (ulepszenie 2) — opis] [WhenUse]\n- 자신의 [ChargeNoirAlly] 횟수가 12 이상이면, 6 소모하여 합 위력 +1, 피해량 +10%\n- 자신의 [ChargeNoirAlly] 횟수 2 증가\n[WhenUse] [RealisationAlly] 최대 20 소모\n- 합 위력 +1\n- 피해량 +(소모한 [RealisationAlly])% (최대 20%)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041602].levelList[level=2].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [ChargeNoirAlly], [RealisationAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation; [RealisationAlly] = 아르뮈르 에비이예 / Armure Éveillée
   EN: [WhenUse]\n- At 12+ [ChargeNoirAlly] Count, consume 6 [ChargeNoirAlly] Count to gain Clash Power +1 and deal +10% damage\n- Gain +2 [ChargeNoirAlly] Count\n[WhenUse] Consume up to 20 [RealisationAlly] to apply the following:\n- Clash Power +1\n- Deal +([RealisationAlly] consumed)% damage (max 20%)<style="highlight"></style>
   PL: [WhenUse]\n- Przy 12+ Liczniku [ChargeNoirAlly] zużywa 6 Licznika [ChargeNoirAlly], aby zyskać Moc Starcia +1 i zadać +10% obrażeń\n- Zwiększa własny Licznik [ChargeNoirAlly] o 2\n[WhenUse] Zużywa do 20 [RealisationAlly], aby stosować poniższe:\n- Moc Starcia +1\n- Zadaje +(zużyte [RealisationAlly])% obrażeń (maks. 20%)<style="highlight"></style>
754. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 1, efekt 1 — opis] [OnSucceedAttack] (자신의 [ChargeNoirAlly] 위력+1)만큼 자신의 [ChargeNoirAlly] 횟수 증가 (최대 <style="highlight">6</style>)
   źródło: Skills_personality-04.json :: dataList[id=1041602].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +([ChargeNoirAlly] Potency + 1) [ChargeNoirAlly] Count (max <style="highlight">6</style>)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o wartość (własna Moc [ChargeNoirAlly] + 1) (maks. <style="highlight">6</style>)
755. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 1 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041602].levelList[level=2].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +1 [Vibration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 2 [Vibration] i zwiększa Licznik [Vibration] o 1<style="highlight"></style>
756. [Umiejętność 2 (×2) (ulepszenie 2) — moneta 3, efekt 1 — opis] <style="highlight">[OnSucceedAttack] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, [VibrationExplosion].\n대상의 [Vibration] 횟수 1 감소</style>
   źródło: Skills_personality-04.json :: dataList[id=1041602].levelList[level=2].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [ChargeNoirAlly], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: <style="highlight">[OnSucceedAttack] At 3+ [ChargeNoirAlly] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1</style>
   PL: <style="highlight">[OnSucceedAttack] Przy 3+ Mocy [ChargeNoirAlly] wywołuje [VibrationExplosion].\nZmniejsza Licznik [Vibration] celu o 1</style>
757. [Umiejętność 2 (×2) (ulepszenie 4) — opis] [WhenUse]\n- 자신의 [ChargeNoirAlly] 횟수가 12 이상이면,\n6 소모하여 <style="highlight">최종 위력 +1</style>, 피해량 <style="highlight">+20%</style>\n- 자신의 [ChargeNoirAlly] 횟수 <style="highlight">4</style> 증가\n<style="highlight">[WhenUse] [NoirSuitAlly]가 50 이상이면, 피해량 +15%</style>\n[WhenUse] [RealisationAlly] 최대 20 소모\n<style="highlight">- 최종 위력 +1</style>\n- 피해량 +(소모한 [RealisationAlly])% (최대 20%)
   źródło: Skills_personality-04.json :: dataList[id=1041602].levelList[level=4].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [ChargeNoirAlly], [NoirSuitAlly], [RealisationAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation; [NoirSuitAlly] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat; [RealisationAlly] = 아르뮈르 에비이예 / Armure Éveillée
   EN: [WhenUse]\n- At 12+ [ChargeNoirAlly] Count, consume 6 [ChargeNoirAlly] Count to gain <style="highlight">Final Power +1</style> and deal <style="highlight">+20%</style> damage\n- Gain +<style="highlight">4</style> [ChargeNoirAlly] Count\n<style="highlight">[WhenUse] At 50+ [NoirSuitAlly], deal +15% damage</style>\n[WhenUse] Consume up to 20 [RealisationAlly] to apply the following:\n- <style="highlight">Final Power +1</style>\n- Deal +([RealisationAlly] consumed)% damage (max 20%)
   PL: [WhenUse]\n- Przy 12+ Liczniku [ChargeNoirAlly] zużywa 6 Licznika [ChargeNoirAlly], aby zyskać <style="highlight">Moc Końcową +1</style> i zadać <style="highlight">+20%</style> obrażeń\n- Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">4</style>\n<style="highlight">[WhenUse] Przy 50+ [NoirSuitAlly] zadaje +15% obrażeń</style>\n[WhenUse] Zużywa do 20 [RealisationAlly], aby stosować poniższe:\n<style="highlight">- Moc Końcowa +1</style>\n- Zadaje +(zużyte [RealisationAlly])% obrażeń (maks. 20%)
758. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] (자신의 [ChargeNoirAlly] 위력 + <style="highlight">3</style>)만큼 자신의 [ChargeNoirAlly] 횟수 증가 (최대 6)
   źródło: Skills_personality-04.json :: dataList[id=1041602].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +([ChargeNoirAlly] Potency + <style="highlight">3</style>) [ChargeNoirAlly] Count (max 6)
   PL: [OnSucceedAttack] Zwiększa własny Licznik [ChargeNoirAlly] o wartość (własna Moc [ChargeNoirAlly] + <style="highlight">3</style>) (maks. 6)
759. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 <style="highlight">2</style> 증가
   źródło: Skills_personality-04.json :: dataList[id=1041602].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +<style="highlight">2</style> [Vibration] Count
   PL: [OnSucceedAttack] Nakłada 2 [Vibration] i zwiększa Licznik [Vibration] o <style="highlight">2</style>
760. [Umiejętność 2 (×2) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, [VibrationExplosion].\n대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041602].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [ChargeNoirAlly], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 3+ [ChargeNoirAlly] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL: [OnSucceedAttack] Przy 3+ Mocy [ChargeNoirAlly] wywołuje [VibrationExplosion].\nZmniejsza Licznik [Vibration] celu o 1<style="highlight"></style>
761. [Umiejętność 3 (×1) (ulepszenia 3–4) — nazwa] 트리플 스탬피드 스티칭
   źródło: Skills_personality-04.json :: dataList[id=1041603].levelList[level=3].name ; dataList[id=1041603].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 5 · monety: 3 (+4)
   limit: do 40 znaków
   EN: Triple Stamped Stitching
   PL: Potrójny Podbijany Ścieg
762. [Umiejętność 3 (×1) (ulepszenie 3) — opis] [WhenUse]\n- 자신의 [ChargeNoirAlly] 횟수가 10 이상이면, 최대 20까지 소모하여\n피해량 +(소모한 [ChargeNoirAlly] 횟수)% (최대 20%)\n- 자신의 [ChargeNoirAlly] 횟수 3 증가\n[WhenUse] [NoirSuitAlly] 40당, 합 위력 +1, 피해량 +10% (각각 최대 2, 최대 20%)
   źródło: Skills_personality-04.json :: dataList[id=1041603].levelList[level=3].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoirAlly], [NoirSuitAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation; [NoirSuitAlly] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat
   EN: [WhenUse]\n- At 10+ [ChargeNoirAlly] Count, consume up to 20 [ChargeNoirAlly] Count to deal +([ChargeNoirAlly] Count consumed)% damage (max 20%)\n- Gain +3 [ChargeNoirAlly] Count\n[WhenUse] For every 40 [NoirSuitAlly], Clash Power +1 and deal +10% damage (max 2 and 20% respectively)
   PL: [WhenUse]\n- Przy 10+ Liczniku [ChargeNoirAlly] zużywa do 20 Licznika [ChargeNoirAlly], aby zadać +(zużyte Liczniki [ChargeNoirAlly])% obrażeń (maks. 20%)\n- Zwiększa własny Licznik [ChargeNoirAlly] o 3\n[WhenUse] Moc Starcia +1 i zadaje +10% obrażeń za każde 40 [NoirSuitAlly] (maks. odpowiednio 2 i 20%)
763. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 3 증가
   źródło: Skills_personality-04.json :: dataList[id=1041603].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 743 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_personality-04.json :: dataList[id=1041603].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada 2 [Vibration] i zwiększa Licznik [Vibration] o 2
765. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 1 — opis] 피해량 +([NoirSuitAlly] 수치/2)% (최대 50%)
   źródło: Skills_personality-04.json :: dataList[id=1041603].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NoirSuitAlly]
   znaczenie tagów: [NoirSuitAlly] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat
   EN: Deal +([NoirSuitAlly] Stack / 2)% damage (max 50%)
   PL: Zadaje +([NoirSuitAlly] stos/2)% obrażeń (maks. 50%)
766. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041603].levelList[level=3].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Umiejętność 3 (×1) (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041603].levelList[level=3].coinlist[#2].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoirAlly], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 3+ [ChargeNoirAlly] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Przy 3+ Mocy [ChargeNoirAlly] wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1
768. [Umiejętność 3 (×1) (ulepszenie 4) — opis] <style="highlight">[StartBattle] [NoirSuitAlly] 20 얻음 (턴당 1회)</style>\n[WhenUse]\n- 자신의 [ChargeNoirAlly] 횟수가 10 이상이면, 최대 20까지 소모하여\n피해량 +(소모한 [ChargeNoirAlly] 횟수)% (최대 20%)\n- 자신의 [ChargeNoirAlly] 횟수 <style="highlight">5</style> 증가\n[WhenUse] [NoirSuitAlly] <style="highlight">30</style>당, 합 위력 +1, 피해량 <style="highlight">+20%</style> <style="highlight">(각각 최대 3, 최대 60%)</style>
   źródło: Skills_personality-04.json :: dataList[id=1041603].levelList[level=4].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [StartBattle], [NoirSuitAlly], [WhenUse], [ChargeNoirAlly]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [NoirSuitAlly] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat; [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation
   EN: <style="highlight">[StartBattle] Gain 20 [NoirSuitAlly] (once per turn)</style>\n[WhenUse]\n- At 10+ [ChargeNoirAlly] Count, consume up to 20 [ChargeNoirAlly] Count to deal +([ChargeNoirAlly] Count consumed)% damage (max 20%)\n- Gain +<style="highlight">5</style> [ChargeNoirAlly] Count\n[WhenUse] For every <style="highlight">30</style> [NoirSuitAlly], Clash Power +1 and deal +<style="highlight">20%</style> damage <style="highlight">(max 3 and 60% respectively)</style>
   PL: <style="highlight">[StartBattle] Zyskuje 20 [NoirSuitAlly] (1 raz na turę)</style>\n[WhenUse]\n- Przy 10+ Liczniku [ChargeNoirAlly] zużywa do 20 Licznika [ChargeNoirAlly], aby zadać +(zużyte Liczniki [ChargeNoirAlly])% obrażeń (maks. 20%)\n- Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">5</style>\n[WhenUse] Moc Starcia +1 i zadaje <style="highlight">+20%</style> obrażeń za każde <style="highlight">30</style> [NoirSuitAlly] <style="highlight">(maks. odpowiednio 3 i 60%)</style>
769. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">5</style> 증가
   źródło: Skills_personality-04.json :: dataList[id=1041603].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 748 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] <style="highlight">3</style> 부여, [Vibration] 횟수 <style="highlight">3</style> 증가
   źródło: Skills_personality-04.json :: dataList[id=1041603].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">3</style> [Vibration] and <style="highlight">+3</style> [Vibration] Count
   PL: [OnSucceedAttack] Nakłada <style="highlight">3</style> [Vibration] i zwiększa Licznik [Vibration] o <style="highlight">3</style>
771. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 1 — opis] 피해량 +(<style="highlight">[NoirSuitAlly] 수치</style>)% (최대 <style="highlight">100%</style>)
   źródło: Skills_personality-04.json :: dataList[id=1041603].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [NoirSuitAlly]
   znaczenie tagów: [NoirSuitAlly] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat
   EN: Deal +(<style="highlight">[NoirSuitAlly] Stack</style>)% damage (max <style="highlight">100%</style>)
   PL: Zadaje +(<style="highlight">stos [NoirSuitAlly]</style>)% obrażeń (maks. <style="highlight">100%</style>)
772. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041603].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL: [OnSucceedAttack] Wywołuje [VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1<style="highlight"></style>
773. [Umiejętność 3 (×1) (ulepszenie 4) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, [VibrationExplosion] <style="highlight">2회</style>. 대상의 [Vibration] 횟수 <style="highlight">2</style> 감소
   źródło: Skills_personality-04.json :: dataList[id=1041603].levelList[level=4].coinlist[#2].coindescs[#2].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [ChargeNoirAlly], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 3+ [ChargeNoirAlly] Potency, trigger [VibrationExplosion] <style="highlight">2 times</style>; then, reduce target's [Vibration] Count by <style="highlight">2</style>
   PL: [OnSucceedAttack] Przy 3+ Mocy [ChargeNoirAlly] wywołuje [VibrationExplosion] <style="highlight">2 razy</style>. Zmniejsza Licznik [Vibration] celu o <style="highlight">2</style>
774. [Umiejętność 4 (×0) (ulepszenia 3–4) — nazwa] 원 킥 - 쿠튀르 뮐티플
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=3].name ; dataList[id=1041605].levelList[level=4].name
   kontekst: grzech: Sloth · typ: Hit · moc bazowa: 4 · monety: 4 (+4)
   limit: do 50 znaków
   EN: Single Kick - Couture Multiple
   PL: Jedno Kopnięcie - Couture Multiple
775. [Umiejętność 4 (×0) (ulepszenie 3) — opis] [WhenUse]\n- 자신의 [ChargeNoirAlly] 횟수를 최대 20까지 소모하여,\n피해량 +(소모한 [ChargeNoirAlly] 횟수)% (최대 20%)\n- 자신의 [ChargeNoirAlly] 횟수 3 증가\n[WhenUse] [RealisationAlly] 최대 60 소모\n- 소모한 [RealisationAlly]가 60 이상이면, 최종 위력 +1\n- 피해량 +(소모한 [RealisationAlly]/3)% (최대 20%)
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=3].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoirAlly], [RealisationAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation; [RealisationAlly] = 아르뮈르 에비이예 / Armure Éveillée
   EN: [WhenUse]\n- Consume up to 20 [ChargeNoirAlly] Count to deal +([ChargeNoirAlly] Count consumed)% damage (max 20%)\n- Gain +3 [ChargeNoirAlly] Count\n[WhenUse] Consume up to 60 [RealisationAlly] to apply the following:\n- If 60+ [RealisationAlly] was consumed, Final Power +1\n- Deal +([RealisationAlly] consumed / 3)% damage (max 20%)
   PL: [WhenUse]\n- Zużywa do 20 Licznika [ChargeNoirAlly], aby zadać +(zużyte Liczniki [ChargeNoirAlly])% obrażeń (maks. 20%)\n- Zwiększa własny Licznik [ChargeNoirAlly] o 3\n[WhenUse] Zużywa do 60 [RealisationAlly], aby stosować poniższe:\n- Jeżeli zużyto 60+ [RealisationAlly], Moc Końcowa +1\n- Zadaje +(zużyte [RealisationAlly]/3)% obrażeń (maks. 20%)
776. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 3 증가
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 743 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여, [Vibration] 횟수 3 증가
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and +3 [Vibration] Count
   PL: [OnSucceedAttack] Nakłada 3 [Vibration] i zwiększa Licznik [Vibration] o 3
778. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 위력이 3 이상이면, [VibrationExplosion].\n대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [ChargeNoirAlly], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 3+ [ChargeNoirAlly] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Przy 3+ Mocy [ChargeNoirAlly] wywołuje [VibrationExplosion].\nZmniejsza Licznik [Vibration] celu o 1
779. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 위력이 2 이상이면, [VibrationExplosion].\n대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=3].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [ChargeNoirAlly], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 2+ [ChargeNoirAlly] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] Przy 2+ Mocy [ChargeNoirAlly] wywołuje [VibrationExplosion].\nZmniejsza Licznik [Vibration] celu o 1
780. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=3].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Umiejętność 4 (×0) (ulepszenie 3) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 10%만큼 관통 피해
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=3].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal Pierce damage equal to 10% of this Coin's final damage
   PL: [OnSucceedAttack] Zadaje obrażenia Kłucia równe 10% końcowych obrażeń tej monety
782. [Umiejętność 4 (×0) (ulepszenie 4) — opis] [WhenUse]\n- 자신의 [ChargeNoirAlly] 횟수를 최대 20까지 소모하여,\n피해량 +(소모한 [ChargeNoirAlly] 횟수)% (최대 20%)\n- 자신의 [ChargeNoirAlly] 횟수 <style="highlight">5</style> 증가\n[WhenUse] [RealisationAlly] 최대 60 소모\n- 소모한 [RealisationAlly] <style="highlight">30당</style>, 최종 위력 +1 <style="highlight">(최대 2)</style>\n- 피해량 +(소모한 [RealisationAlly]/3)% (최대 20%)
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=4].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [WhenUse], [ChargeNoirAlly], [RealisationAlly]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation; [RealisationAlly] = 아르뮈르 에비이예 / Armure Éveillée
   EN: [WhenUse]\n- Consume up to 20 [ChargeNoirAlly] Count to deal +([ChargeNoirAlly] Count consumed)% damage (max 20%)\n- Gain +<style="highlight">5</style> [ChargeNoirAlly] Count\n[WhenUse] Consume up to 60 [RealisationAlly] to apply the following:\n- Final Power +1 <style="highlight">for every 30</style> [RealisationAlly] consumed <style="highlight">(max 2)</style>\n- Deal +([RealisationAlly] consumed / 3)% damage (max 20%)
   PL: [WhenUse]\n- Zużywa do 20 Licznika [ChargeNoirAlly], aby zadać +(zużyte Liczniki [ChargeNoirAlly])% obrażeń (maks. 20%)\n- Zwiększa własny Licznik [ChargeNoirAlly] o <style="highlight">5</style>\n[WhenUse] Zużywa do 60 [RealisationAlly], aby stosować poniższe:\n- Moc Końcowa +1 za każde <style="highlight">30</style> zużytego [RealisationAlly] <style="highlight">(maks. 2)</style>\n- Zadaje +(zużyte [RealisationAlly]/3)% obrażeń (maks. 20%)
783. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 횟수 <style="highlight">5</style> 증가
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=4].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 748 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여, [Vibration] 횟수 3 증가<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=4].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and +3 [Vibration] Count<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 3 [Vibration] i zwiększa Licznik [Vibration] o 3<style="highlight"></style>
785. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 위력이 3 이상이면,\n[VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [ChargeNoirAlly], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 3+ [ChargeNoirAlly] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL: [OnSucceedAttack] Przy 3+ Mocy [ChargeNoirAlly] wywołuje\n[VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1<style="highlight"></style>
786. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoirAlly] 위력이 2 이상이면,\n[VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=4].coinlist[#2].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [OnSucceedAttack], [ChargeNoirAlly], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoirAlly] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 2+ [ChargeNoirAlly] Potency, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1<style="highlight"></style>
   PL: [OnSucceedAttack] Przy 2+ Mocy [ChargeNoirAlly] wywołuje\n[VibrationExplosion]. Zmniejsza Licznik [Vibration] celu o 1<style="highlight"></style>
787. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 3, efekt 2 — opis] <style="highlight">[OnSucceedAttack] 이 코인 최종 피해량의 10%만큼 관통 피해</style>
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=4].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: <style="highlight">[OnSucceedAttack] Deal Pierce damage equal to 10% of this Coin's final damage</style>
   PL: <style="highlight">[OnSucceedAttack] Zadaje obrażenia Kłucia równe 10% końcowych obrażeń tej monety</style>
788. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=4].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 772 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Umiejętność 4 (×0) (ulepszenie 4) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 이 코인 최종 피해량의 <style="highlight">15%</style>만큼 관통 피해
   źródło: Skills_personality-04.json :: dataList[id=1041605].levelList[level=4].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal Pierce damage equal to <style="highlight">15</style>% of this Coin's final damage
   PL: [OnSucceedAttack] Zadaje obrażenia Kłucia równe <style="highlight">15</style>% końcowych obrażeń tej monety
790. [Obrona (ulepszenia 1,3,4) — nazwa] 고객 자식! 상품에 주름이 잡히고 있지 않나!
   źródło: Skills_personality-04.json :: dataList[id=1041604].levelList[level=1].name ; dataList[id=1041604].levelList[level=3].name ; dataList[id=1041604].levelList[level=4].name
   kontekst: grzech: Sloth · typ: obrona: kontra · moc bazowa: 5 · monety: 2 (+4)
   limit: do 80 znaków
   EN: Tch. Stupid Customer. You're Wrinkling the Merchandise!
   PL: Cz. Głupi Klient! Gniecie mi towar!
791. [Obrona (ulepszenie 1) — opis] [DuelCounter]\n[StartBattle]\n- 자신의 [NoirSuitAlly]가 60 이상이면, 해당 효과가 다음 턴에 [RealisationAlly]로 변경됨\n- 자신의 [RealisationAlly]가 60 미만이면, 해당 효과가 다음 턴에 [NoirSuitAlly]로 변경됨\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수 2 증가 (턴당 2회)
   źródło: Skills_personality-04.json :: dataList[id=1041604].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [StartBattle], [NoirSuitAlly], [RealisationAlly], [WhenUse], [ChargeNoirAlly]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [NoirSuitAlly] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat; [RealisationAlly] = 아르뮈르 에비이예 / Armure Éveillée; [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [DuelCounter]\n[StartBattle]\n- At 60+ [NoirSuitAlly], convert the said effect into [RealisationAlly] next turn\n- At fewer than 60 [RealisationAlly], convert the said effect into [NoirSuitAlly] next turn\n[WhenUse] Gain +2 [ChargeNoirAlly]  Count (2 times per turn)
   PL: [DuelCounter]\n[StartBattle]\n- Przy 60+ [NoirSuitAlly] efekt ten zmienia się w [RealisationAlly] w następnej turze\n- Poniżej 60 [RealisationAlly] efekt ten zmienia się w [NoirSuitAlly] w następnej turze\n[WhenUse] Zwiększa własny Licznik [ChargeNoirAlly] o 2 (2 razy na turę)
792. [Obrona (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_personality-04.json :: dataList[id=1041604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Obrona (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여 (턴당 2회)
   źródło: Skills_personality-04.json :: dataList[id=1041604].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration] (2 times per turn)
   PL: [OnSucceedAttack] Nakłada 1 [Vibration] (2 razy na turę)
794. [Obrona (ulepszenie 3) — opis] [DuelCounter]\n[StartBattle]\n- 자신의 [NoirSuitAlly]가 60 이상이면,\n해당 효과가 다음 턴에 [RealisationAlly]로 변경됨\n- 자신의 [RealisationAlly]가 60 미만이면,\n해당 효과가 다음 턴에 [NoirSuitAlly]로 변경됨\n<style="highlight">[BeforeUse] 자신의 [RealisationAlly]가 60 이상이면,\n‘원 킥 - 쿠튀르 뮐티플’로 발동됨 (턴당 1회)\n- 이 효과가 발동했으면, 공격 종료 시 [RealisationAlly] 전부 소모</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수 2 증가 (턴당 2회)
   źródło: Skills_personality-04.json :: dataList[id=1041604].levelList[level=3].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [NoirSuitAlly], [RealisationAlly], [BeforeUse], [WhenUse], [ChargeNoirAlly]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [NoirSuitAlly] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat; [RealisationAlly] = 아르뮈르 에비이예 / Armure Éveillée; [BeforeUse] = [사용전] / [Before Use]; [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [DuelCounter]\n[StartBattle]\n- At 60+ [NoirSuitAlly], convert the said effect into [RealisationAlly] next turn\n- At fewer than 60 [RealisationAlly], convert the said effect into [NoirSuitAlly] next turn\n<style="highlight">[BeforeUse] At 60+ [RealisationAlly], activate as "Single Kick - Couture Multiple" (once per turn)\n- If the above effect was triggered, consume all [RealisationAlly] at Attack End</style>\n[WhenUse] Gain +2 [ChargeNoirAlly] Count (2 times per turn)
   PL: [DuelCounter]\n[StartBattle]\n- Przy 60+ [NoirSuitAlly]\nefekt ten zmienia się w [RealisationAlly] w następnej turze\n- Poniżej 60 [RealisationAlly]\nefekt ten zmienia się w [NoirSuitAlly] w następnej turze\n<style="highlight">[BeforeUse] Przy 60+ [RealisationAlly] uruchamia się jako „Jedno Kopnięcie - Couture Multiple” (1 raz na turę)\n- Jeżeli ten efekt się uruchomił, zużywa całe [RealisationAlly] na koniec ataku</style>\n[WhenUse] Zwiększa własny Licznik [ChargeNoirAlly] o 2 (2 razy na turę)
795. [Obrona (ulepszenia 3–4) — moneta 2, efekt 1 — opis] [SuperCoin]<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041604].levelList[level=3].coinlist[#1].coindescs[#0].desc ; dataList[id=1041604].levelList[level=4].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 552 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Obrona (ulepszenie 3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 1 부여 (턴당 2회)<style="highlight"></style>
   źródło: Skills_personality-04.json :: dataList[id=1041604].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration] (2 times per turn)<style="highlight"></style>
   PL: [OnSucceedAttack] Nakłada 1 [Vibration] (2 razy na turę)<style="highlight"></style>
797. [Obrona (ulepszenie 4) — opis] [DuelCounter]\n[StartBattle]\n- 자신의 [NoirSuitAlly]가 60 이상이면,\n해당 효과가 다음 턴에 [RealisationAlly]로 변경됨\n- 자신의 [RealisationAlly]가 60 미만이면,\n해당 효과가 다음 턴에 [NoirSuitAlly]로 변경됨\n[BeforeUse] 자신의 [RealisationAlly]가 60 이상이면,\n‘원 킥 - 쿠튀르 뮐티플’로 발동됨 (턴당 1회)\n- 이 효과가 발동했으면, 공격 종료 시 [RealisationAlly] 전부 소모\n<style="highlight">[WhenUse] 자신의 [ChargeNoirAlly] 위력이 3/5 이상이면, 코인 위력 +1/+2</style>\n[WhenUse] 자신의 [ChargeNoirAlly] 횟수 2 증가 (턴당 2회)
   źródło: Skills_personality-04.json :: dataList[id=1041604].levelList[level=4].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, \n, [DuelCounter], [StartBattle], [NoirSuitAlly], [RealisationAlly], [BeforeUse], [WhenUse], [ChargeNoirAlly]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [NoirSuitAlly] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat; [RealisationAlly] = 아르뮈르 에비이예 / Armure Éveillée; [BeforeUse] = [사용전] / [Before Use]; [WhenUse] = [사용시] / [On Use]; [ChargeNoirAlly] = 보존 / Preservation
   EN: [DuelCounter]\n[StartBattle]\n- At 60+ [NoirSuitAlly], convert the said effect into [RealisationAlly] next turn\n- At fewer than 60 [RealisationAlly], convert the said effect into [NoirSuitAlly] next turn\n[BeforeUse] At 60+ [RealisationAlly], activate as "Single Kick - Couture Multiple" (once per turn)\n- If the above effect was triggered, consume all [RealisationAlly] at Attack End\n<style="highlight">[WhenUse] At 3+/5+ [ChargeNoirAlly] Potency, Coin Power +1/+2</style> \n[WhenUse] Gain +2 [ChargeNoirAlly] Count (2 times per turn)
   PL: [DuelCounter]\n[StartBattle]\n- Przy 60+ [NoirSuitAlly]\nefekt ten zmienia się w [RealisationAlly] w następnej turze\n- Poniżej 60 [RealisationAlly]\nefekt ten zmienia się w [NoirSuitAlly] w następnej turze\n[BeforeUse] Przy 60+ [RealisationAlly] uruchamia się jako „Jedno Kopnięcie - Couture Multiple” (1 raz na turę)\n- Jeżeli ten efekt się uruchomił, zużywa całe [RealisationAlly] na koniec ataku\n<style="highlight">[WhenUse] Przy 3+/5+ Mocy [ChargeNoirAlly] Moc Monet +1/+2</style>\n[WhenUse] Zwiększa własny Licznik [ChargeNoirAlly] o 2 (2 razy na turę)
798. [Obrona (ulepszenie 4) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] <style="highlight">2</style> 부여 (턴당 2회)
   źródło: Skills_personality-04.json :: dataList[id=1041604].levelList[level=4].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlight">, </style>, [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict <style="highlight">2</style> [Vibration] (2 times per turn)
   PL: [OnSucceedAttack] Nakłada <style="highlight">2</style> [Vibration] (2 razy na turę)
799. [Pasywka bojowa (od ulepszenia 1) — nazwa] 르누아르 개버딘 원단
   źródło: Passives.json :: dataList[id=1041602].name
   limit: do 40 znaków
   EN: Le Noir: Gabardine Fabric
   PL: Le Noir: Tkanina Gabardyna
800. [Pasywka bojowa (od ulepszenia 1) — opis] 전장에 등장 시, [NoirSuitAlly] 25 얻음\n\n턴 시작 시, 자신의 최대 체력의 ([NoirSuitAlly]\n+ [RealisationAlly])/5%만큼 보호막 얻음
   źródło: Passives.json :: dataList[id=1041602].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [NoirSuitAlly], [RealisationAlly]
   znaczenie tagów: [NoirSuitAlly] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat; [RealisationAlly] = 아르뮈르 에비이예 / Armure Éveillée
   EN: Upon entering the field, gain 25 [NoirSuitAlly]\n\nTurn Start: Gain Shield equal to (([NoirSuitAlly] + [RealisationAlly]) / 5)% of this unit's max HP
   PL: Przy wejściu na pole zyskuje 25 [NoirSuitAlly]\n\nNa początku tury zyskuje Tarczę równą (([NoirSuitAlly]\n+ [RealisationAlly]) / 5)% Maks. HP
801. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 보호막 얻음
   źródło: Passives.json :: dataList[id=1041602].summary
   limit: do 120 znaków
   EN: Gain Shield
   PL: Zyskuje Tarczę
802. [Pasywka bojowa (od ulepszenia 1) — nazwa] 보존
   źródło: Passives.json :: dataList[id=1041604].name
   limit: do 40 znaków
   EN: Conservation
   PL: Zachowanie
803. [Pasywka bojowa (od ulepszenia 1) — opis] 전투 중 누적으로 자신의 [ChargeNoirAlly] 횟수를\n10 소모할 때마다 [ChargeNoirAlly] 위력 1 얻음\n\n턴 종료 시 자신의 [ChargeNoirAlly] 위력이 3 미만이면, [ChargeNoirAlly] 횟수를 전부 소모하여\n(소모한 수치 x 5)만큼 다음 턴에 보호막을 얻음\n\n자신의 [ChargeNoirAlly] 위력이 3 이상이면, [ChargeNoirAlly] 횟수가 12 미만일 때\n자신의 기본 스킬로 획득하는 [ChargeNoirAlly] 횟수 획득량 +1\n\n기본 공격 스킬 사용 시,\n- 대상의 [Vibration] 위력이 6 이상이면, 코인 위력 +1\n- 자신의 [ChargeNoirAlly] 위력이 3 이상이면, 코인 위력 +1\n- 피해량 +(자신의 [ChargeNoirAlly] 위력 x 2)% (최대 10%)\n· ‘트리플 스탬피드 스티칭’, ‘원 킥 - 쿠튀르 뮐티플’이면,\n대신 피해량 +(자신의 [ChargeNoirAlly] 위력 x 4)% (최대 20%)
   źródło: Passives.json :: dataList[id=1041604].desc
   limit: do 950 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoirAlly], [Vibration]
   znaczenie tagów: [ChargeNoirAlly] = 보존 / Preservation; [Vibration] = 진동 / Tremor
   EN: Gain 1 [ChargeNoirAlly] Potency for every 10 cumulative [ChargeNoirAlly] Count this unit consumes in this Encounter\n\nTurn End: At fewer than 3 [ChargeNoirAlly] Potency, consume all [ChargeNoirAlly] Count to gain ([ChargeNoirAlly] Count consumed x 5) Shield next turn\n\nAt 3+ [ChargeNoirAlly] Potency, this unit's Base Skills gain +1 more [ChargeNoirAlly] Count when this unit has fewer than 12 [ChargeNoirAlly] Count\n\nOn Base Attack Skill Use,\n- If target has 6+ [Vibration] Potency, Coin Power +1\n- At 3+ [ChargeNoirAlly] Potency, Coin Power +1\n- Deal +([ChargeNoirAlly] Potency x 2)% damage (max 10%)\n· If the said Skill is "Triple Stamped Stitching" or "Single Kick - Couture Multiple", deal +([ChargeNoirAlly] Potency x 4)% damage instead (max 20%)
   PL: Za każde łączne zużycie 10 własnego Licznika [ChargeNoirAlly] podczas walki zyskuje 1 Mocy [ChargeNoirAlly]\n\nNa koniec tury poniżej 3 Mocy [ChargeNoirAlly] zużywa całe Liczniki [ChargeNoirAlly], aby zyskać (zużyta wartość x 5) Tarczy w następnej turze\n\nPrzy 3+ Mocy [ChargeNoirAlly] podstawowe Umiejętności tej jednostki zyskują o 1 więcej Licznika [ChargeNoirAlly], gdy ma poniżej 12 Licznika [ChargeNoirAlly]\n\nPrzy użyciu podstawowej Umiejętności ataku,\n- Jeżeli cel ma 6+ Mocy [Vibration], Moc Monet +1\n- Przy 3+ Mocy [ChargeNoirAlly] Moc Monet +1\n- Zadaje +(własna Moc [ChargeNoirAlly] x 2)% obrażeń (maks. 10%)\n· Jeżeli tą Umiejętnością jest „Potrójny Podbijany Ścieg” albo „Jedno Kopnięcie - Couture Multiple”, zamiast tego zadaje +(własna Moc [ChargeNoirAlly] x 4)% obrażeń (maks. 20%)
804. [Pasywka bojowa (od ulepszenia 1) — podsumowanie] 보존 횟수가 일정 수치 미만이면 획득량 증가\n기본 공격 스킬 사용 시 코인 위력과 피해량이 증가
   źródło: Passives.json :: dataList[id=1041604].summary
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At fewer than a certain number of Preservation Count, gain more Preservation Count\nOn Base Attack Skill Use, gain Coin Power and deal more damage
   PL: Poniżej pewnej liczby Licznika Konserwacji zyskuje o więcej Licznika Konserwacji\nPrzy użyciu podstawowej Umiejętności ataku zyskuje Moc Monet i zadaje więcej obrażeń
805. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Sloth, posiadane 1× Pride, posiadane 2× Envy) — nazwa] 되먹임
   źródło: Passives.json :: dataList[id=1041601].name
   limit: do 40 znaków
   EN: Feedback
   PL: Deprawiacja
806. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Sloth, posiadane 1× Pride, posiadane 2× Envy) — opis] 적에게 [VibrationExplosion] 시, [VibrationExplosion]의 흐트러짐 피해량 +15%\n- 자신의 [ChargeNoirAlly] 횟수가 12 이상이면, 대신 [VibrationExplosion] 시 자신의 [ChargeNoirAlly] 횟수 1을 소모하여 [VibrationExplosion]의 흐트러짐 피해량 +30% (대상별로 적용)\n\n자신에게 보호막이 있을 때 적에게 피격 시,\n대상 적에게 [Vibration] 위력 2 부여 (적 별로 턴당 2회)
   źródło: Passives.json :: dataList[id=1041601].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationExplosion], [ChargeNoirAlly], [Vibration]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [ChargeNoirAlly] = 보존 / Preservation; [Vibration] = 진동 / Tremor
   EN: When triggering [VibrationExplosion] on the enemy, increase the Stagger Threshold raise by +15%\n- At 12+ [ChargeNoirAlly] Count, consume 1 [ChargeNoirAlly] Count when triggering [VibrationExplosion] to increase the Stagger Threshold raise by +30% instead (effect applied per target)\n\nWhen hit, if this unit has Shield, inflict 2 [Vibration] Potency on the attacker (2 times per turn per enemy)
   PL: Gdy wywołuje [VibrationExplosion] na wrogu, podniesienie Progu Oszołomienia +15%\n- Przy 12+ Liczniku [ChargeNoirAlly] zamiast tego zużywa 1 Licznika [ChargeNoirAlly] przy wywołaniu [VibrationExplosion], aby podnieść Próg Oszołomienia o +30% (efekt stosowany per cel)\n\nGdy zostaje trafiona, jeżeli ma Tarczę, nakłada 2 Mocy [Vibration] na atakującego wroga (2 razy na turę per wróg)
807. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Sloth, posiadane 1× Pride, posiadane 2× Envy) — podsumowanie] 흐트러짐 피해량 증가
   źródło: Passives.json :: dataList[id=1041601].summary
   limit: do 120 znaków
   EN: Increase Stagger Threshold raise
   PL: Podnosi podniesienie Progu Oszołomienia
808. [Pasywka bojowa (od ulepszenia 2, posiadane 1× Sloth, posiadane 1× Pride, posiadane 2× Envy) — tekst klimatyczny] 르누아르는 강한 진동으로 상대를 흔들리게 함으로써, 상대의 가치를 붕괴시킬 수 있다고 믿는다. 이는 격렬하게 진동할수록 매 순간 변화를 겪는다고 생각하기 때문으로, 르누아르의 전투 기술들은 이러한 방향성 위에서 구성되었다.\n\n그리고 이들은 기억하지도, 경험하지도 못했겠지만, 시지프 백화점 밖에도 같은 원리로 작동하고, 발전한 전투 기술들이 존재한다.
   źródło: Passives.json :: dataList[id=1041601].flavor
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Noirs believe they can collapse their opponents' worth by subjecting them to violent tremors—the more violently the target vibrates, the more changes it must undergo from moment to moment. The combat techniques of the Noirs were built upon that conviction.\n\nAnd though the Noirs neither remember nor have ever experienced it, beyond the Grand Magasin Sisyphe exist fighting techniques founded upon the very same principle and have since been refined far beyond.
   PL: Le Noir wierzy, że gwałtownymi wstrząsami może zburzyć wartość przeciwnika — im mocniej drga, tym więcej zmian przechodzi z chwili na chwilę. Techniki walki Le Noir zbudowano właśnie na tym przekonaniu.\n\nA choć Le Noir nie pamiętają ani nie doświadczyły tego same, poza Dzielnica Sisyphe istnieją techniki walki oparte na tej samej zasadzie, które od tamtej pory rozwinęły się znacznie dalej.
809. [Pasywka bojowa (od ulepszenia 3) — nazwa] 르누아르 개버딘 원단
   źródło: Passives.json :: dataList[id=1041603].name
   (powtórzenie elementu 799 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Pasywka bojowa (od ulepszenia 3) — opis] 전장에 등장 시, [NoirSuitAlly] 25 얻음\n\n턴 시작 시,\n- 자신의 최대 체력의 ([NoirSuitAlly]\n+ [RealisationAlly])/5%만큼 보호막 얻음\n- [RealisationAlly]가 있으면, ‘트리플 스탬피드 스티칭’이 ‘원 킥 - 쿠튀르 뮐티플’로 적용됨
   źródło: Passives.json :: dataList[id=1041603].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [NoirSuitAlly], [RealisationAlly]
   znaczenie tagów: [NoirSuitAlly] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat; [RealisationAlly] = 아르뮈르 에비이예 / Armure Éveillée
   EN: Upon entering the field, gain 25 [NoirSuitAlly]\n\nTurn Start:\n- Gain Shield equal to (([NoirSuitAlly] + [RealisationAlly]) / 5)% of this unit's max HP\n- If this unit has [RealisationAlly], convert "Triple Stamped Stitching" into "Single Kick - Couture Multiple"
   PL: Przy wejściu na pole zyskuje 25 [NoirSuitAlly]\n\nNa początku tury\n- zyskuje Tarczę równą (([NoirSuitAlly]\n+ [RealisationAlly]) / 5)% Maks. HP\n- jeżeli ma [RealisationAlly], „Potrójny Podbijany Ścieg” stosuje się jako „Jedno Kopnięcie - Couture Multiple”
811. [Pasywka bojowa (od ulepszenia 3) — podsumowanie] 보호막 얻음
   źródło: Passives.json :: dataList[id=1041603].summary
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
812. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Sloth) — nazwa] 르누아르의 미덕과 가치
   źródło: Passives.json :: dataList[id=1041621].name
   limit: do 40 znaków
   EN: Le Noir's Virtue and Worth
   PL: Cnota i Wartość Le Noir
813. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Sloth) — opis] [Charge], 특수 [Charge]을 보유한 아군 중 편성 순서가 가장 빠른 아군 1명이 기본 스킬을 사용하여 [VibrationExplosion]로 입히는 흐트러짐 피해량 +12.5%
   źródło: Passives.json :: dataList[id=1041621].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: [Charge], [VibrationExplosion]
   znaczenie tagów: [Charge] = 충전 / Charge; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: Among allies that have [Charge] or Unique [Charge], when 1 ally with the earliest Deployment Order triggers [VibrationExplosion] using its Base Skills, increase the Stagger Threshold raise by +12.5%
   PL: Wśród sojuszników z [Charge] lub Specjalnym [Charge] 1 Sojusznik przydzielony najwcześniej zwiększa podniesienie Progu Oszołomienia przez [VibrationExplosion] wywoływane podstawowymi Umiejętnościami o +12.5%
814. [Pasywka wsparcia (od ulepszenia 3, posiadane 6× Sloth) — podsumowanie] 진동 폭발 시 흐트러짐 피해량이 증가\n피격 시 진동 위력 부여
   źródło: Passives.json :: dataList[id=1041621].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Increase Stagger Threshold raised by Tremor Burst\nInflict Tremor Potency when hit
   PL: Zwiększa podniesienie Progu Oszołomienia przez Wybuch Wstrząsu\nPrzy trafieniu nakłada Moc Wstrząsu

## [?] Early Elephants Sinnerling — Ryōshū — 코끼리반 수감생
- ID Tożsamości: `400028` (plik: `Personalities-x1p1c1.json`)

815. [Karta Tożsamości — tytuł] 코끼리반 수감생
   źródło: Personalities-x1p1c1.json :: dataList[id=400028].title
   limit: do 40 znaków
   EN: Early Elephants Sinnerling
   PL: Grzesznik Grupy Słoników
816. [Karta Tożsamości — nazwa] 료슈
   źródło: Personalities-x1p1c1.json :: dataList[id=400028].name
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Karta Tożsamości — nazwa z tytułem] 료슈
   źródło: Personalities-x1p1c1.json :: dataList[id=400028].nameWithTitle
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Karta Tożsamości — opis] 료슈의 ??? 인격
   źródło: Personalities-x1p1c1.json :: dataList[id=400028].desc
   limit: do 120 znaków
   EN: Ryōshū's ??? Identity
   PL: Tożsamość ??? Ryōshū
819. [Pasywka bojowa [40002801] — nazwa] 무짜별적 예쑬
   źródło: Passives-x1p1c1.json :: dataList[id=40002801].name
   limit: do 40 znaków
   EN: Indiscwiminate Awt
   PL: Indiscwiminate Awt
820. [Pasywka bojowa [40002801] — opis] 자신이 받는 피해량 +25%. 가하는 피해량 +25%
   źródło: Passives-x1p1c1.json :: dataList[id=40002801].desc
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
821. [Pasywka bojowa [40002802] — nazwa] 등떠밀기
   źródło: Passives-x1p1c1.json :: dataList[id=40002802].name
   limit: do 40 znaków
   EN: Hustlwe
   PL: Hustlwe
822. [Pasywka bojowa [40002802] — opis] 최대 체력이 가장 낮은 아군 1명 가하는 피해량 +20%, 받는 피해량 +20%
   źródło: Passives-x1p1c1.json :: dataList[id=40002802].desc
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
